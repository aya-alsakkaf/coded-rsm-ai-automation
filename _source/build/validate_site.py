# -*- coding: utf-8 -*-
"""Quality gate for a workshop built by this engine. Every setting comes from the kit. Must print PROBLEMS: 0.

Static: sample files are the kit's (names and bytes); every name starts with coded-<code>-; slide counts equal content.SLIDES;
public decks carry no notes; staff decks carry one note per slide, equal to the kit record, escaped once (no &#..; left after one
unescape) and never empty; no note shares an 8-word run with its slide; the notes pages equal the kit notes; COPY buttons on the
sheets equal the kit's prompts or templates; noindex everywhere (meta, X-Robots-Tag on every path, robots.txt); /staff private,
no-store; the redirects (/, /pre, /post, /survey, /slidesN, the kit's REDIRECTS); package.json named after the code; middleware;
no gold (hex or rgba) anywhere; no leftover words from other builds (the kit's leftover-words.txt); no idioms in engine text;
labs keep answers off the public page; survey payloads (when the kit has SURVEY) have short slugs.
Browser: links resolve; public pages never link to /staff; no console errors; no em dash; no sideways scroll at 390 px; the accent
token is the kit's; every slide carries the kit's words and only the kit's or the engine's words (both ways); the rendered notes
(press N) equal the kit; every player and the opener reach their last step on the arrow key and hand over; every slide fits
1440x810 above the progress bar (players and the opener at their last step, quick checks after a tap); every QR code decodes to its
portal URL and each MAP slide shows the form name, day and time; the lab page saves done marks and checks a flag.

    python3 validate_site.py ../../public
"""
import asyncio, glob, hashlib, json, os, re, sys, collections, html as H
import wk
from wk import C, P, DEMOS, ALL_FILES, DAYS, opt
from playwright.async_api import async_playwright

S = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(wk.ROOT, "public"))
ROOT = os.path.dirname(S)
PROBLEMS = []
def bad(x): PROBLEMS.append(x); print("PROBLEM:", x)
def rd(p): return open(p, encoding="utf-8").read()
def words(t): return collections.Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", H.unescape(str(t)).replace("’", "'").lower()))
def runs(t, n=8):
    w = re.findall(r"[a-z0-9]+", H.unescape(str(t)).replace("’", "'").lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}
REC = {d: json.load(open(os.path.join(wk.RECORD_DIR, f"slides-day-{d}.json"), encoding="utf-8")) for d in DAYS}
NOTES = {d: json.load(open(os.path.join(wk.RECORD_DIR, f"presenter-notes-day-{d}.json"), encoding="utf-8")) for d in DAYS}
SLIDES = opt("SLIDES")
GOLD = [r"#C89A45\b", r"#E2C27F\b", r"#FFB661\b", r"#FF8C00\b", r"#D4AF37\b", r"#FFD700\b", r"#F2A900\b", r"rgba?\(\s*200\s*,\s*154\s*,\s*69", r"rgba?\(\s*255\s*,\s*182\s*,\s*97",
        r"rgba?\(\s*255\s*,\s*140\s*,\s*0\s*[,)]", r"rgba?\(\s*226\s*,\s*194\s*,\s*127", r"\bgold\b"]
IDIOMS = ["walk out able", "walk away with", "leave able to", "hit the ground running", "on the same page", "piece of cake", "in a nutshell", "game changer", "deep dive", "low-hanging fruit", "moves the needle", "moved you"]

def leftover_terms():
    p = os.path.join(wk.KIT_DIR, "leftover-words.txt")
    if not os.path.exists(p): bad("the kit has no leftover-words.txt (copy it from the example kit)"); return []
    terms = []
    for line in rd(p).splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line: continue
        code, rest = line.split(":", 1)
        if code.strip() == wk.CODE: continue                    # this build's own names
        terms += [t.strip() for t in rest.split(",") if t.strip()]
    return terms
TERMS = leftover_terms()
LEFT = re.compile(r"(?<![\w-])(" + "|".join(re.escape(t) for t in sorted(TERMS, key=len, reverse=True)) + r")(?![\w-])", re.I) if TERMS else None

def static_checks():
    # sample files: names and bytes from the kit
    present = sorted(f for f in os.listdir(S) if f in ALL_FILES)
    if present != sorted(ALL_FILES): bad(f"sample files on the site {present} != the kit's {sorted(ALL_FILES)}")
    md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
    for f in ALL_FILES:
        if os.path.exists(f"{S}/{f}") and md5(f"{S}/{f}") != md5(os.path.join(wk.FILES_DIR, f)): bad(f"{f} differs from the kit's file")
    if glob.glob(S + "/**/*.py", recursive=True) or os.path.exists(S + "/_source"): bad("build code or _source inside public/")
    for p in glob.glob(S + "/*") + glob.glob(S + "/staff/*"):
        b = os.path.basename(p)
        if b in ("staff", "index.html", "404.html", "robots.txt") or b in ALL_FILES: continue
        if not b.startswith(wk.PFX + "-") and b != wk.PFX + ".html": bad(f"{b}: name does not start with {wk.PFX}-")
    # decks and notes
    if not SLIDES: bad("content.py has no SLIDES = {day: count} (the approved slide plan)")
    for d in DAYS:
        n = len(REC[d])
        if SLIDES and SLIDES.get(d) != n: bad(f"day {d}: the deck has {n} slides, content.SLIDES says {SLIDES.get(d)}")
        pub = rd(f"{S}/{wk.deckp(d)}.html"); st = rd(f"{S}/staff/{wk.deckp(d)}.html")
        for name, h in (("public", pub), ("staff", st)):
            c = h.count('<section class="cd-slide')
            if c != n: bad(f"day {d} {name} deck has {c} slides, the kit record has {n}")
        if "data-notes=" in pub: bad(f"day {d} public deck carries speaker notes")
        notes = re.findall(r'data-notes="([^"]*)"', st)
        if len(notes) != n: bad(f"day {d} staff deck: {len(notes)} notes for {n} slides")
        for i, (a, k, r) in enumerate(zip(notes, NOTES[d], REC[d]), 1):
            t = H.unescape(a)
            if t != k["flat"]: bad(f"day {d} slide {i} ({r['id']}): the staff note differs from the kit note")
            if re.search(r"&(#\d+|#x[0-9a-f]+|amp|quot|lt|gt|apos);", t, re.I): bad(f"day {d} slide {i}: the note shows an HTML entity ({t[:60]!r}): escaped twice")
            if not (k.get("do") or k.get("say")): bad(f"day {d} slide {i} ({r['id']}): the note has no 'do' and no 'say' part")
        pn = rd(f"{S}/staff/{P(f'notes-day-{d}')}.html")
        flats = [H.unescape(x) for x in re.findall(r'data-flat="([^"]*)"', pn)]
        if flats != [k["flat"] for k in NOTES[d]]: bad(f"day {d}: the presenter notes page differs from the kit notes")
    # sheets: COPY buttons equal the kit's prompts (AI tool) or templates (no AI tool)
    for d in DAYS:
        h = rd(f"{S}/{wk.sheetp(d)}.html")
        want = sum((len(v["prompts"]) + len(v["stretch_prompts"]) if wk.AI else 0) + len(v["templates"]) for _k, v in wk.day_demos(d))
        got = len(re.findall(r'class="sh-copy"[^>]*data-copy=', h))
        if got != want: bad(f"day {d} {wk.SHEET['name'].lower()}: {got} COPY buttons, the kit has {want}")
    # noindex everywhere, staff private
    for p in glob.glob(S + "/*.html") + glob.glob(S + "/staff/*.html"):
        if 'name="robots" content="noindex' not in rd(p): bad(f"{os.path.relpath(p, S)}: page without the noindex meta tag")
    if "Disallow: /" not in rd(S + "/robots.txt"): bad("robots.txt does not disallow all")
    v = json.load(open(ROOT + "/vercel.json"))
    hd = {h["source"]: {x["key"]: x["value"] for x in h["headers"]} for h in v["headers"]}
    if "noindex" not in hd.get("/(.*)", {}).get("X-Robots-Tag", ""): bad("vercel.json: no X-Robots-Tag noindex on every path")
    for sp in ("/staff", "/staff/(.*)"):
        if "no-store" not in hd.get(sp, {}).get("Cache-Control", "") or "private" not in hd.get(sp, {}).get("Cache-Control", ""): bad(f"vercel.json: {sp} is not private, no-store")
    red = {r["source"]: r["destination"] for r in v["redirects"]}
    for k in ("pre", "post", "survey"):
        if k in wk.FORMS and red.get("/" + k) != wk.FORMS[k]["url"]: bad(f"vercel.json: /{k} does not redirect to {wk.FORMS[k]['url']}")
    for d in DAYS:
        if red.get(f"/slides{d}") != "/" + wk.deckp(d): bad(f"vercel.json: /slides{d} missing")
    for s_, d_ in opt("REDIRECTS", []):
        if red.get(s_) != d_: bad(f"vercel.json: the kit's redirect {s_} -> {d_} is missing")
    if red.get("/") != "/" + wk.HUB: bad("vercel.json: / does not redirect to the hub")
    for dest in red.values():
        if dest.startswith("/") and not dest.startswith("/staff") and dest != "/" and not os.path.exists(S + dest + ".html"): bad(f"vercel.json: redirect target {dest} has no page")
    if v.get("outputDirectory") != "public" or not v.get("cleanUrls"): bad("vercel.json: outputDirectory or cleanUrls")
    pk = json.load(open(ROOT + "/package.json"))
    if pk.get("name") != wk.PFX: bad(f"package.json name {pk.get('name')!r} is not {wk.PFX}")
    if pk.get("type") != "module" or "@vercel/functions" not in pk.get("dependencies", {}): bad("package.json: @vercel/functions or type module missing")
    mw = rd(ROOT + "/middleware.js")
    if "STAFF_PASSWORD" not in mw or "/staff/:path*" not in mw: bad("middleware.js: staff lock missing")
    # no gold anywhere (hex and rgba forms), in every page and stylesheet
    for p in glob.glob(S + "/**/*.html", recursive=True) + glob.glob(S + "/**/*.css", recursive=True):
        t = rd(p)
        for g in GOLD:
            m = re.search(g, t, re.I)
            if m: bad(f"{os.path.relpath(p, S)}: gold color {m.group(0)!r}"); break
    # labs: answers only on the staff lab key
    import pages as SITE
    for d, L in wk.LABS.items():
        pub = rd(f"{S}/{wk.labp(d)}.html"); key = rd(f"{S}/staff/{P(f'lab-key-day-{d}')}.html")
        if "localStorage" not in pub or "try{" not in pub: bad(f"day {d} lab: done marks are not saved in localStorage inside try/catch")
        for i, s in enumerate(L["steps"], 1):
            ck = s.get("check") or {}
            if ck.get("kind") == "flag":
                if re.search(r"(?<![\w])" + re.escape(ck["answer"]) + r"(?![\w])", re.sub(r"<script.*?</script>", "", pub, flags=re.S), re.I): bad(f"day {d} lab step {i}: the flag answer shows on the public lab page")
                if SITE.flag_hash(ck["answer"]) not in pub: bad(f"day {d} lab step {i}: the flag check is missing")
                if ck["answer"] not in key: bad(f"day {d} lab step {i}: the flag is not on the staff lab key")
            for _t, val in s.get("answer", []):
                for chunk in ([val] if isinstance(val, str) else []):
                    plain = wk.strip(chunk)
                    if len(plain) > 25 and plain in wk.strip(pub): bad(f"day {d} lab step {i}: answer text on the public lab page")
    # practice questions (optional): shape, count, saved marks, linked from the hub, no overlap with the MAP test
    if wk.PRACTICE:
        Q = wk.PRACTICE; pth = f"{S}/{wk.practp()}.html"
        if not os.path.exists(pth): bad("practice page missing")
        else:
            h = rd(pth)
            if h.count('class="sh-card pq') != len(Q["questions"]): bad("practice page: question count differs from the kit")
            if "localStorage" not in h or "try{" not in h: bad("practice page: answers are not kept in localStorage inside try/catch")
            if f'{wk.practp()}.html' not in rd(f"{S}/{wk.HUB}.html"): bad("the hub does not link the practice page")
        mapruns = set().union(*[runs(m["q"] + " " + " ".join(m["o"])) for m in C.MAP]) if C.MAP else set()
        for i, q in enumerate(Q["questions"], 1):
            if q.get("topic") not in Q["topics"]: bad(f"practice {i}: topic {q.get('topic')!r} is not in PRACTICE['topics']")
            if len(q.get("o", [])) != 4 or q.get("a") not in range(4) or not q.get("why"): bad(f"practice {i}: needs 4 options, an answer index and a 'why'")
            sh = runs(q["q"] + " " + " ".join(q["o"])) & mapruns
            if sh: bad(f"practice {i}: shares words with a MAP question: {sorted(sh)[0]!r}")
    # minutes inside each session (optional SEGMENTS): consecutive times that fill the session
    for d, sess in wk.SEGMENTS.items():
        for rng, nm, segs in sess:
            if sum(m for _t, m, _x in segs) != wk.minutes(rng): bad(f"day {d} {nm}: the segments add up to {sum(m for _t, m, _x in segs)} minutes, the session is {wk.minutes(rng)}")
            t0 = rng.split("-")[0]
            for t, m, _x in segs:
                if t != t0: bad(f"day {d} {nm}: segment at {t} should start at {t0}"); break
                hh, mm = map(int, t.split(":")); mm += m; t0 = f"{hh + mm // 60:02d}:{mm % 60:02d}"
    # survey payloads
    if opt("SURVEY"):
        for name in ("pre", "post", "final"):
            p = os.path.join(wk.SURVEY_DIR, name + ".json")
            if not os.path.exists(p): bad(f"survey payload {name}.json missing (run surveys.py)"); continue
            sl = json.load(open(p))["_update"]["slug"]
            if len(sl) > 80: bad(f"survey {name}: slug longer than 80 characters")

JS_TEXT = """(sel)=>[...document.querySelectorAll(sel)].map(s=>{const w=document.createTreeWalker(s,NodeFilter.SHOW_TEXT);let t=[],n;while(n=w.nextNode()){const p=n.parentElement;if(p&&p.closest('script,style'))continue;t.push(n.nodeValue)}
  s.querySelectorAll('[data-full]').forEach(e=>t.push(e.getAttribute('data-full')));return t.join(' ')})"""   # players type their prompt from data-full
CHROME = words("Where we are · Your time min Reset +1 min Time Copy Quick check A B C D Correct Not quite tap to reveal The idea Day of × END close")

async def fidelity(pg, base):
    for d in DAYS:
        await pg.goto(f"{base}staff/{wk.deckp(d)}.html"); await pg.wait_for_timeout(700)
        site = await pg.evaluate(JS_TEXT, "#deck .cd-slide")
        if len(site) != len(REC[d]): bad(f"day {d}: the record has {len(REC[d])} slides, the site {len(site)}"); continue
        for r, s in zip(REC[d], site):
            kw, sw = words(" ".join(r["kit"])), words(s)
            miss = {w: c for w, c in (kw - sw).items() if not w.isdigit()}
            if miss: bad(f"day {d} slide {r['n']} ({r['id']}): kit words missing on the site: {dict(list(miss.items())[:8])}")
            allowed = set(kw) | set(words(" ".join(r["chrome"]))) | set(CHROME)
            extra = sorted(w for w in sw if w not in allowed and not w.isdigit())
            if extra: bad(f"day {d} slide {r['n']} ({r['id']}): words on the site that are not in the kit or the engine: {extra[:8]}")
            # notes never repeat the slide text
            shared = runs(NOTES[d][r["n"] - 1]["flat"]) & runs(s)
            if shared: bad(f"day {d} slide {r['n']} ({r['id']}): the note repeats the slide text: {sorted(shared)[0]!r}")

async def deck_checks(pg, base, name, d, trainer):
    acc = (await pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--cd-accent').trim()")).lower()
    want = wk.theme("--x:#6F9CE8").split(":")[1].lower()
    if acc != want: bad(f"{name}: accent is {acc}, not the kit's {want}")
    recs = REC[d]
    n = len(recs)
    # players and the opener reach their last step and hand over
    for i, r in enumerate(recs):
        if r["kind"] not in ("player", "showcase"): continue
        await pg.evaluate(f"window.CD_DECK.goTo({i})"); await pg.wait_for_timeout(500)
        done_sel = ".pp-decide.on" if r["kind"] == "player" else ".ws-punch.on"
        for _ in range(14):
            if await pg.evaluate(f"!!document.getElementById('{r['id']}').querySelector('{done_sel}')"): break
            await pg.keyboard.press("ArrowRight"); await pg.wait_for_timeout(1500)
        if not await pg.evaluate(f"!!document.getElementById('{r['id']}').querySelector('{done_sel}')"): bad(f"{name}: {r['id']} did not reach its last step on the arrow key")
        await pg.keyboard.press("ArrowRight"); await pg.wait_for_timeout(500)
        if await pg.evaluate("window.CD_DECK.current") != i + 1: bad(f"{name}: {r['id']} did not hand over to the next slide")
    # rendered notes (press N) equal the kit
    if trainer:
        await pg.evaluate("window.CD_DECK.goTo(0)"); await pg.wait_for_timeout(300)
        await pg.keyboard.press("n"); await pg.wait_for_timeout(300)
        for i in range(n):
            await pg.evaluate(f"window.CD_DECK.goTo({i})"); await pg.wait_for_timeout(120)
            t = await pg.evaluate("(document.getElementById('notesBody')||{}).textContent||''")
            t = re.sub(r"^\[[^\]]*\] ", "", t)
            if t != NOTES[d][i]["flat"]: bad(f"{name}: slide {i + 1} rendered note differs from the kit ({t[:50]!r})"); break
        await pg.keyboard.press("n"); await pg.wait_for_timeout(200)
    # every slide fits 1440x810 above the progress bar: players and the opener at their last step, quick checks after a tap
    await pg.set_viewport_size({"width": 1440, "height": 810})
    FIT = """()=>{const s=document.querySelectorAll('#deck .cd-slide')[window.CD_DECK.current];const bar=document.querySelector('.cd-bar').getBoundingClientRect().top;
        const vis=e=>{for(let x=e;x&&x!==s;x=x.parentElement){const c=getComputedStyle(x);if(c.opacity==='0'||c.visibility==='hidden'||c.display==='none')return false}return true};
        let worst=0;const w=document.createTreeWalker(s,NodeFilter.SHOW_TEXT);let n;
        while(n=w.nextNode()){if(!n.nodeValue.trim())continue;const p=n.parentElement;if(!p||p.closest('script,style,.cd-ghost-word,.ws-punch,svg')||!vis(p))continue;
          const r=document.createRange();r.selectNodeContents(n);const b=r.getBoundingClientRect();if(b.height)worst=Math.max(worst,b.bottom-bar)}return worst}"""
    for i, r in enumerate(recs):
        await pg.evaluate(f"window.CD_DECK.goTo({i})"); await pg.wait_for_timeout(300)
        if r["kind"] in ("player", "showcase"):
            for _ in range(14):
                if await pg.evaluate(f"!!document.getElementById('{r['id']}').querySelector('.pp-decide.on,.ws-score.on')"): break
                await pg.keyboard.press("ArrowRight"); await pg.wait_for_timeout(1300)
            await pg.wait_for_timeout(1600)
        if r["kind"] == "check":
            await pg.evaluate(f"(()=>{{const b=document.getElementById('{r['id']}').querySelector('.cd-mcq button:not([data-correct])');if(b)b.click()}})()"); await pg.wait_for_timeout(300)
            ok = await pg.evaluate(f"(()=>{{const c=document.getElementById('{r['id']}').querySelector('button[data-correct]');const m=getComputedStyle(c).borderTopColor.match(/\\d+/g).map(Number);return m[1]>m[0]+40&&m[1]>m[2]}})()")
            if not ok: bad(f"{name}: slide {i + 1} ({r['id']}): the right answer does not show green after a wrong tap")
        over = await pg.evaluate(FIT)
        if over > 2: bad(f"{name}: slide {i + 1} ({r['id']}) runs {over:.0f}px into the progress bar at 1440x810")
    await pg.evaluate(f"window.CD_DECK.goTo({n - 1})"); await pg.wait_for_timeout(300)
    if await pg.evaluate("window.CD_DECK.current") != n - 1: bad(f"{name}: last slide not reachable")

def decode(png, scale=1):
    """The decoded text of a QR screenshot (tries a few sizes, like a phone moving closer)."""
    import cv2, numpy as np
    img0 = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_GRAYSCALE)
    for f in (scale, 1, 2, 0.5, 1.5):
        img = img0 if f == 1 else cv2.resize(img0, None, fx=f, fy=f, interpolation=cv2.INTER_AREA if f < 1 else cv2.INTER_NEAREST)
        img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
        img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=255)
        v = cv2.QRCodeDetector().detectAndDecode(img)[0]
        if v: return v
    return ""
async def qr_checks(b, base):
    pg = await b.new_page(viewport={"width": 1440, "height": 900})
    for d in DAYS:
        for r in [r for r in REC[d] if r["kind"] == "map"]:
            keys = ["post", "survey"] if "after" in r["title"] else ["pre"]
            keys = [k for k in keys if k in wk.FORMS]
            await pg.goto(f"{base}{wk.deckp(d)}.html"); await pg.wait_for_timeout(500)
            await pg.evaluate(f"window.CD_DECK.goTo({r['n'] - 1})"); await pg.wait_for_timeout(900)
            els = await pg.query_selector_all(f"#{r['id']} svg.wk-qr-code")
            if len(els) != len(keys): bad(f"day {d} {r['id']}: {len(els)} QR codes, expected {len(keys)}")
            txt = await pg.evaluate(f"document.getElementById('{r['id']}').textContent")
            for el, k in zip(els, keys):
                box = await el.bounding_box()
                if box["width"] < 150: bad(f"day {d} {r['id']}: QR {k} only {box['width']:.0f}px wide at 1440px")
                if decode(await el.screenshot()) != wk.FORMS[k]["url"]: bad(f"day {d} {r['id']}: QR {k} does not decode to its portal URL")
                for f in ("name", "when"):
                    if wk.FORMS[k][f] not in txt: bad(f"day {d} {r['id']}: the MAP slide does not show the {f} of {k} ({wk.FORMS[k][f]!r})")
    targets = [(wk.HUB + ".html", [k for k in ("pre", "post", "survey") if k in wk.FORMS]), ("staff/index.html", [k for k in ("pre", "post", "survey") if k in wk.FORMS])]
    targets += [(wk.dayp(d) + ".html", [k for k in wk.FORM_DAY.get(d, []) if k in wk.FORMS]) for d in DAYS if wk.FORM_DAY.get(d)]
    await pg.close(); pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=3)   # the small page codes, shot sharp
    for page, keys in targets:
        await pg.goto(base + page); await pg.wait_for_timeout(400)
        els = await pg.query_selector_all("svg.wk-qr-code")
        if len(els) != len(keys): bad(f"{page}: {len(els)} QR codes, expected {len(keys)}")
        for el, k in zip(els, keys):
            await el.scroll_into_view_if_needed()
            if decode(await el.screenshot()) != wk.FORMS[k]["url"]: bad(f"{page}: QR {k} does not decode to its portal URL")
    await pg.close()

async def practice_checks(b, base):
    if not wk.PRACTICE: return
    import pages as SITE
    ctx = await b.new_context(); pg = await ctx.new_page(); qs = wk.PRACTICE["questions"]
    await pg.goto(base + wk.practp() + ".html"); await pg.wait_for_timeout(300)
    await pg.click(f".pq[data-q='1'] .pq-opt[data-k='{qs[0]['a']}']")
    if "ok" not in (await pg.get_attribute(".pq[data-q='1'] .pq-res", "class")): bad("practice: the right answer is not accepted")
    if len(qs) > 1:
        w = (qs[1]["a"] + 1) % 4
        await pg.click(f".pq[data-q='2'] .pq-opt[data-k='{w}']")
        if "no" not in (await pg.get_attribute(".pq[data-q='2'] .pq-res", "class")): bad("practice: a wrong answer is not marked")
        if "is-right" not in (await pg.get_attribute(f".pq[data-q='2'] .pq-opt[data-k='{qs[1]['a']}']", "class")): bad("practice: the right answer does not show after a wrong pick")
    await pg.reload(); await pg.wait_for_timeout(300)
    if "ok" not in (await pg.get_attribute(".pq[data-q='1'] .pq-res", "class")): bad("practice: answers are not kept after a reload")
    await ctx.close()

async def lab_checks(b, base):
    for d, L in wk.LABS.items():
        ctx = await b.new_context(); pg = await ctx.new_page()
        await pg.goto(f"{base}{wk.labp(d)}.html"); await pg.wait_for_timeout(400)
        await pg.click(".lab-step[data-step='1'] .lab-done input")
        flag = next(((i, s["check"]["answer"]) for i, s in enumerate(L["steps"], 1) if (s.get("check") or {}).get("kind") == "flag"), None)
        if flag:
            i, ans = flag
            await pg.fill(f".lab-step[data-step='{i}'] .lab-flag", "wrong answer"); await pg.click(f".lab-step[data-step='{i}'] .lab-go")
            if "no" not in (await pg.get_attribute(f".lab-step[data-step='{i}'] .lab-res", "class")): bad(f"day {d} lab: a wrong flag is not refused")
            await pg.fill(f".lab-step[data-step='{i}'] .lab-flag", ans.upper()); await pg.click(f".lab-step[data-step='{i}'] .lab-go")
            if "ok" not in (await pg.get_attribute(f".lab-step[data-step='{i}'] .lab-res", "class")): bad(f"day {d} lab: the right flag is not accepted")
        await pg.reload(); await pg.wait_for_timeout(400)
        if not await pg.is_checked(".lab-step[data-step='1'] .lab-done input"): bad(f"day {d} lab: the done mark is not kept after a reload")
        await ctx.close()

async def browser_checks(base):
    pages = sorted(os.path.relpath(p, S) for p in glob.glob(S + "/*.html") + glob.glob(S + "/staff/*.html"))
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name in pages:
            staff = name.startswith("staff/"); deck = name.endswith("-deck.html")
            pg = await b.new_page(viewport={"width": 1440, "height": 900})
            errs = []
            pg.on("pageerror", lambda x: errs.append(str(x)))
            pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
            await pg.goto(base + name); await pg.wait_for_timeout(500)
            for h in await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))"):
                if h.startswith(("http", "#", "mailto")): continue
                f = os.path.normpath(h.split("#")[0].lstrip("/") if h.startswith("/") else os.path.join(os.path.dirname(name), h.split("#")[0]))
                if not os.path.exists(f"{S}/{f}") and not os.path.exists(f"{S}/{f}.html"): bad(f"{name}: broken link {h}")
                if not staff and (f.startswith("staff") or "staff/" in h): bad(f"{name}: public page links to a staff page {h}")
            text = await pg.evaluate("document.body.innerText")
            if "—" in text: bad(f"{name}: em dash in visible text")
            if LEFT:
                m = LEFT.search(text) or LEFT.search(await pg.title())
                if m: bad(f"{name}: leftover word from another build: {m.group(0)!r}")
            low = text.lower()
            for idi in IDIOMS:
                if idi in low: bad(f"{name}: idiom {idi!r} in visible text (plain English only)")
            if deck:
                await deck_checks(pg, base, name, int(re.search(r"day-(\d+)-deck", name).group(1)), staff)
            else:
                await pg.set_viewport_size({"width": 390, "height": 844}); await pg.wait_for_timeout(300)
                sw = await pg.evaluate("document.documentElement.scrollWidth")
                if sw > 392: bad(f"{name}: sideways scroll at phone width ({sw}px)")
            errs = [x for x in errs if "favicon" not in x]
            if errs: bad(f"{name}: console errors {errs[:3]}")
            await pg.close()
        pg = await b.new_page(viewport={"width": 1440, "height": 900})
        await fidelity(pg, base); await pg.close()
        await qr_checks(b, base)
        await lab_checks(b, base)
        await practice_checks(b, base)
        await b.close()
    return len(pages)

def serve():
    """public/ over HTTP with Vercel-style clean URLs, so root links and the 404 page work."""
    import functools, http.server, socketserver, threading
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def translate_path(self, path):
            p = super().translate_path(path)
            if not os.path.exists(p) and os.path.exists(p + ".html"): return p + ".html"
            return p
    srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(Q, directory=S)); threading.Thread(target=srv.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{srv.server_address[1]}/"

if __name__ == "__main__":
    base = serve()
    static_checks()
    n = asyncio.run(browser_checks(base))
    print(f"{n} pages checked · PROBLEMS: {len(PROBLEMS)}")
    sys.exit(1 if PROBLEMS else 0)
