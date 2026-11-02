# -*- coding: utf-8 -*-
"""Quality gate. Run after every build: python3 -I _source/build/validate_site.py   Must print PROBLEMS: 0.
Static checks here; browser checks (390 px, widgets, decks, COPY, QR decode) are in tools/check_browser.js."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PUB = os.path.join(ROOT, "public")

from content_core import CODE, DAYS, FILES, MAP
from content_slides import SLIDES
from content_prompts import PROMPTS
import content_map as M
import content_staff as ST

problems, warnings = [], []


def bad(msg):
    problems.append(msg)


def html_files():
    for dp, _, fs in os.walk(PUB):
        for f in fs:
            if f.endswith(".html"):
                yield os.path.join(dp, f)


def resolve(base_dir, href):
    href = href.split("#")[0].split("?")[0]
    if not href:
        return True
    p = os.path.normpath(os.path.join(PUB, href.lstrip("/"))) if href.startswith("/") else os.path.normpath(os.path.join(base_dir, href))
    return os.path.exists(p) or os.path.exists(p + ".html") or os.path.exists(os.path.join(p, "index.html"))


pages = list(html_files())
for path in pages:
    rel = os.path.relpath(path, PUB)
    t = open(path, encoding="utf-8").read()
    public = not rel.startswith("staff")
    # 1 links and assets
    for attr, href in re.findall(r'\b(href|src)="([^"]+)"', t):
        if href.startswith(("http://", "https://", "mailto:", "data:", "#")):
            continue
        if not resolve(os.path.dirname(path), href):
            bad(f"{rel}: broken {attr} {href}")
        # 2 public pages never link to /staff
        if public and "staff" in href.split("/"):
            bad(f"{rel}: public page links to staff: {href}")
    # 3 no em dashes
    if "—" in t:
        bad(f"{rel}: em dash found")
    # 4 noindex
    if 'name="robots" content="noindex, nofollow"' not in t:
        bad(f"{rel}: missing noindex meta")
    # answers never on a public page
    if public:
        for needle in [M.KEY, "Answer key", "3 of 6 invoices match", "6 accounts flagged", "Huda Al-Saleh (25%"]:
            if needle in t:
                bad(f"{rel}: answer text on a public page: {needle[:40]}")
    # no gold
    if re.search(r"#7A5A22|gold", t, re.I) and "deck" not in rel:
        bad(f"{rel}: gold found")

# robots, vercel.json, middleware, package.json
if open(os.path.join(PUB, "robots.txt")).read().strip() != "User-agent: *\nDisallow: /":
    bad("robots.txt is not Disallow all")
vj = json.load(open(os.path.join(ROOT, "vercel.json")))
if vj.get("outputDirectory") != "public" or not vj.get("cleanUrls") or vj.get("trailingSlash") is not False:
    bad("vercel.json: outputDirectory/cleanUrls/trailingSlash")
hdr = {h["key"]: h["value"] for h in vj["headers"][0]["headers"]}
for k in ("X-Content-Type-Options", "Referrer-Policy", "X-Frame-Options", "X-Robots-Tag"):
    if k not in hdr:
        bad(f"vercel.json: missing header {k}")
srcs = {h["source"] for h in vj["headers"]}
if not {"/staff", "/staff/(.*)"} <= srcs:
    bad("vercel.json: no-store on /staff missing")
reds = {r["source"]: r["destination"] for r in vj["redirects"]}
for s in ("/", "/pre", "/post", "/survey", "/slides1", "/slides2"):
    if s not in reds:
        bad(f"vercel.json: redirect {s} missing")
pk = json.load(open(os.path.join(ROOT, "package.json")))
if "@vercel/functions" not in pk.get("dependencies", {}) or pk.get("type") != "module":
    bad("package.json: @vercel/functions or type module missing")
mw = open(os.path.join(ROOT, "middleware.js")).read()
for needle in ["matcher: ['/staff', '/staff/:path*']", "STAFF_PASSWORD", "status: 503", "status: 401", "safeEqual"]:
    if needle not in mw:
        bad(f"middleware.js: missing {needle}")

# decks: slide counts, notes only on staff, timers match tasks
css = open(os.path.join(PUB, f"{CODE}-site.css")).read()
if "#6F9CE8" not in css or "#2F74D6" not in css:
    bad("site css: CODED accent blues missing")
if re.search(r"#7A5A22|rgba\(201,\s*162", css):
    bad("site css: old gold found")
for d in DAYS:
    n = d["n"]
    pub = open(os.path.join(PUB, f"{CODE}-day-{n}-deck.html"), encoding="utf-8").read()
    stf = open(os.path.join(PUB, "staff", f"{CODE}-day-{n}-deck.html"), encoding="utf-8").read()
    for name, t in (("public", pub), ("staff", stf)):
        c = t.count('class="dk-slide ')
        if c != len(SLIDES[n]):
            bad(f"day {n} {name} deck: {c} slides, expected {len(SLIDES[n])}")
    if "data-notes=" in pub:
        bad(f"day {n} public deck has speaker notes")
    if stf.count("data-notes=") != len(SLIDES[n]):
        bad(f"day {n} staff deck: notes missing on some slides")
    mins = {t["id"]: t["mins"] for t in d["tasks"]}
    for s in SLIDES[n]:
        if s["type"] == "exercise" and s["task"] in mins and s["dur"] != mins[s["task"]] * 60:
            bad(f"day {n} task {s['task']}: slide dur {s['dur']} != {mins[s['task']]} min")
    for s in SLIDES[n]:
        if s["type"] == "exercise" and s["task"] in mins and f'data-minutes="{mins[s["task"]]}"' not in pub:
            bad(f"day {n} task {s['task']}: timer minutes missing in deck")
    # slide time within 10% of teaching time (day minus breaks and lunch)
    teach = 480 - (15 + 60 + 15 if n == 1 else 15 + 60 + 10)
    total = sum(s["dur"] for s in SLIDES[n]) / 60
    if abs(total - teach) > teach * 0.1:
        bad(f"day {n}: slide time {total:.0f} min vs teaching time {teach} min")
    # every task on the day page
    day = open(os.path.join(PUB, f"{CODE}-day-{n}.html"), encoding="utf-8").read()
    for t in d["tasks"]:
        if f"Your turn · {t['id']} · {t['mins']} min" not in day:
            bad(f"day {n} page: task {t['id']} missing")

# prompt sheets: COPY count
for n, ps in PROMPTS.items():
    t = open(os.path.join(PUB, f"{CODE}-prompt-sheet-day-{n}.html"), encoding="utf-8").read()
    want = sum(1 + len(p.get("extra", [])) for p in ps)
    if t.count('class="sh-copy"') != want or t.count("<pre>") != want:
        bad(f"prompt sheet {n}: {t.count('class=\"sh-copy\"')} COPY buttons, expected {want}")
    for p in ps:
        for f in p["files"]:
            if f not in {x for x, _, _ in FILES}:
                bad(f"prompt {p['id']}: unknown file {f}")

# sample files: same bytes as the source, names unchanged
for f, _, _ in FILES:
    a, b = os.path.join(ROOT, "_source", "files", f), os.path.join(PUB, f)
    if not os.path.exists(b) or os.path.getsize(a) != os.path.getsize(b):
        bad(f"sample file {f}: missing or changed")
for d in DAYS:
    for f in d["files"] + [x for t in d["tasks"] for x in t["files"]]:
        if f not in {x for x, _, _ in FILES}:
            bad(f"day {d['n']}: unknown file {f}")

# MAP: same questions PRE and POST, key format
pre, post = M.map_payload("pre"), M.map_payload("post")
if [q["label"] for q in pre["questions"]] != [q["label"] for q in post["questions"]]:
    bad("MAP PRE and POST questions differ")
for p in (pre, post, M.survey_payload()):
    for q in p["questions"]:
        if not q["label"]["en"] or not q["label"]["ar"]:
            bad(f"{p['name']}: {q['id']} missing EN or AR")
        for o in q.get("options", []):
            if not o["label"]["en"] or not o["label"]["ar"]:
                bad(f"{p['name']}: {q['id']} option missing EN or AR")
    for s in p["sections"]:
        if not s["title"]["en"] or not s["title"]["ar"]:
            bad(f"{p['name']}: section {s['id']} title missing EN or AR")
    if "—" in json.dumps(p, ensure_ascii=False):
        bad(f"{p['name']}: em dash")
if "Answer key: " + M.KEY not in pre["description"]:
    bad("MAP PRE description: answer key missing")
for k in ("pre", "post", "survey"):
    if not MAP[k]["url"]:
        warnings.append(f"MAP {k}: no URL yet (surveys not published); QR codes show a placeholder")
    else:
        home = open(os.path.join(PUB, f"{CODE}.html"), encoding="utf-8").read()
        if MAP[k]["url"] not in home:
            bad(f"MAP {k}: URL not on the home page")
        if reds.get(f"/{k}") != MAP[k]["url"]:
            bad(f"vercel.json: /{k} does not point to the portal")

# em dashes in the sources too
for f in os.listdir(HERE):
    if f.startswith("content") and f.endswith(".py") and "—" in open(os.path.join(HERE, f), encoding="utf-8").read():
        bad(f"{f}: em dash in the source")

for w_ in warnings:
    print("WARNING:", w_)
for p in problems:
    print("PROBLEM:", p)
print(f"pages: {len(pages)} · slides: {sum(len(v) for v in SLIDES.values())} · prompts: {sum(len(v) for v in PROMPTS.values())} · files: {len(FILES)}")
print(f"PROBLEMS: {len(problems)}")
sys.exit(1 if problems else 0)
