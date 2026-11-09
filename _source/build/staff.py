# -*- coding: utf-8 -*-
"""Trainer pages under /staff (behind the staff password), written from the kit: the workshop index, the lesson plan, the
facilitator kit, and for each day the presenter notes, the demo runbook, the backup results, the answer keys and the lab key.
Answers live only here (and in _source/ and the portal descriptions). The notes and quick checks come from the same
build as the decks (deck.all_records), so the notes pages always equal the staff decks.

    python3 staff.py OUTDIR      (OUTDIR/staff/...)
"""
import os, sys, json
import wk
from wk import C, e, P, DAYS, HUB, dayp, deckp, sheetp, labp, cardp, opt, day_demos, DEMOS, BLOCK, ALL_FILES, blocks_html
import deck as DK

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(wk.ROOT, "public")
TT = lambda t: f"{t} | {C.TITLE} · {wk.ORG}"

def shell(title, body):
    return wk.text_rules(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{e(TT(title))}</title>
<link rel="icon" href="../{P("favicon.png")}" type="image/png"><link rel="stylesheet" href="{P("staff.css")}">
</head><body>
{body}
<div class="foot">Staff only. Public pages never link here. Never share these links with participants.</div>
</body></html>
''')
def bar(title, sub, tabs, tag="staff only"):
    t = "".join(f'<a class="tab" href="#{a}">{e(b)}</a>' for a, b in tabs)
    return (f'<div class="bar"><div class="bar-in"><div class="brand"><span class="dot"></span>{e(title)} · <b>{e(sub)}</b><span class="tag-demo">{e(tag)}</span></div>'
            + (f'<div class="tabs">{t}</div>' if tabs else "") + '</div></div>\n')
def sec(sid, h2, c, sub, inner):
    return (f'<section id="{sid}"><div class="sec-h"><h2>{e(h2)}</h2><span class="c">{e(c)}</span></div>'
            + (f'<div class="sec-sub">{sub}</div>' if sub else "") + inner + "</section>\n")
def dl(files): return ('<div class="dl">' + "".join(f'<a href="../{f}" download>{e(f)}</a>' for f in files) + "</div>") if files else ""
def qr_row():
    return '<div class="qr-row">' + "".join(f'<a href="{wk.FORMS[k]["url"]}" target="_blank" rel="noopener">{wk.qr_svg(wk.FORMS[k]["url"], label=wk.FORMS[k]["name"])}{e(wk.FORMS[k]["name"])} · {e(wk.FORMS[k]["when"])}</a>'
                                          for k in ("pre", "post", "survey") if k in wk.FORMS) + "</div>"
def map_where(recs):
    s = [f"Day {d} slide {r['n']}" for d in DAYS for r in recs[d] if r["kind"] == "map"]
    return ", ".join(s)
def ros_rows(d):
    rows, tot = [], 0
    for t, n, desc in C.DAYS[d]["blocks"]:
        m = wk.minutes(t); tot += m; rows.append([t, m, f"<b>{e(n)}</b>", e(desc) if desc else "Break"])
    return rows, tot

# ------------------------------------------------------------------ pages
def staff_index(recs):
    row = lambda href, url, t: f'<div class="chk"><div class="q"><a href="{href}">{e(url)}</a></div><div class="a">{e(t)}</div></div>'
    pub = ([(HUB, "Workshop home")] + [(dayp(d), f"Day {d} overview") for d in DAYS] + [(deckp(d), f"Day {d} slides (no notes)") for d in DAYS]
           + [(sheetp(d), f"Day {d} {wk.SHEET['name'].lower()}") for d in DAYS] + [(labp(d), f"Day {d} lab") for d in DAYS if d in wk.LABS] + ([(wk.practp(), "Practice questions")] if wk.PRACTICE else [])
           + [(P("cheat-sheet"), "Cheat sheet"), (cardp(), wk.CARD["name"]), (P("take-home-guide"), "Take-home guide")])
    st = [(P("lesson-plan"), "The lesson plan: run of show, blocks, demos, tasks, files and the MAP sittings"),
          (P("facilitator-kit"), "Before the workshop, run of show, room, failure plan, MAP links and key")]
    for d in DAYS:
        st += [(deckp(d), f"Day {d} slides with speaker notes (press N)"), (P(f"notes-day-{d}"), f"Day {d} presenter notes"), (P(f"runbook-day-{d}"), f"Day {d} demo runbook"),
               (P(f"backup-day-{d}"), f"Day {d} backup results"), (P(f"answer-key-day-{d}"), f"Day {d} answer keys")]
        if d in wk.LABS: st.append((P(f"lab-key-day-{d}"), f"Day {d} lab key"))
    b = bar("Workshop index", C.TITLE, []) + '<main><section><div class="sec-sub">Every page and file of this workshop. Pages under /staff need the staff password.</div>'
    b += '<div class="grp-lbl">Public site</div><div class="checks">' + "".join(row(f"../{p}.html", f"/{p}", t) for p, t in pub) + "</div>"
    b += '<div class="grp-lbl">Staff only (password)</div><div class="checks">' + "".join(row(f"{p}.html", f"/staff/{p}", t) for p, t in st) + row("index.html", "/staff", "This page") + "</div>"
    b += '<div class="grp-lbl">Sample files (public, fictional)</div>' + dl(ALL_FILES)
    b += (f'<div class="grp-lbl">MAP test and survey (CODED portal)</div><div class="sec-sub">The QR codes are on the MAP slides ({map_where(recs)}), the workshop home and the day pages.</div>'
          + qr_row() + '<div class="checks">' + "".join(row(wk.FORMS[k]["url"], wk.FORMS[k].get("slug", wk.FORMS[k]["url"]), f'{wk.FORMS[k]["name"]} · {wk.FORMS[k]["when"]}') for k in ("pre", "post", "survey") if k in wk.FORMS) + "</div>")
    b += "</section></main>\n"
    return shell("Workshop index", b)

def lesson_plan(recs):
    tabs = [(f"d{d}", f"Day {d}") for d in DAYS] + [("map", "MAP sittings"), ("files", "Files")]
    b = bar("Lesson plan", C.TITLE, tabs) + "<main>"
    b += (f'<div class="intro"><b>{e(C.TITLE)}</b> · {e(wk.ORG)} · {e(C.DATES)} · {e(C.HOURS)} · {e(C.VENUE)}. {e(opt("LESSON_INTRO", ""))} '
          f'Tools: {e(C.TOOLS)}. Habit: <b>{e(C.THRU)}</b></div>')
    b += '<div class="grp-lbl">Outcomes</div>' + blocks_html([("ol", [e(x) for x in C.OUTCOMES])])
    for d in DAYS:
        Dd = C.DAYS[d]; rows, tot = ros_rows(d)
        inner = blocks_html([("p", f"<b>{e(Dd['claim'])}</b> · {len(recs[d])} slides · {tot} minutes on the agenda. You build: {e(Dd['artifact'])}."),
                             ("table", [["Time", "Min", "Block", "What happens"]] + rows)])
        trs = [[f'<b>{e(v["card"])}</b>', e(v["title"]), (f'{v["minutes"]} min · {e(v["solo"])}' + (f' · {v["points"]} points' if v.get("points") else "")) if v.get("hands_on") else "in the slide",
                ", ".join(f"<code>{e(f)}</code>" for f in v["files"]) or "none", e(v["deliverable"] or v["point"]), " · ".join(e(x) for x in v["stretch"]) or "none"] for _k, v in day_demos(d)]
        for rng, nm, segs in wk.SEGMENTS.get(d, []):
            inner += blocks_html([("h", f"{rng} · {nm} · minutes inside the session"), ("table", [["Time", "Min", "Block"]] + [[t, m, x] for t, m, x in segs] + [["", f"<b>{sum(m for _t, m, _x in segs)}</b>", "<b>Total</b>"]])])
        inner += blocks_html([("h", "Demos and tasks"), ("table", [["Card", "What", "Time", "Files", "Deliverable", "Finished early?"]] + trs)])
        b += sec(f"d{d}", f"Day {d} · {Dd['title']}", f"{C.DAYDATE[d]} · {C.HOURS}", "", inner)
    b += sec("map", "MAP sittings and the final survey", "CODED portal", f"Same {len(C.MAP)} questions before and after, not graded. The key is on the facilitator kit and the last day's answer keys.",
             blocks_html([("table", [["What", "When", "Link"]] + [[e(wk.FORMS[k]["name"]), e(wk.FORMS[k]["when"]), f'<code>{e(wk.FORMS[k]["url"])}</code>'] for k in ("pre", "post", "survey") if k in wk.FORMS])]))
    b += sec("files", "Sample files", "all fictional", e(C.SAMPLE_NOTE),
             blocks_html([("table", [["File", "Used in"]] + [[f"<code>{e(f)}</code>", ", ".join(v["card"] for v in DEMOS.values() if f in v["files"]) or "none"] for f in ALL_FILES])]))
    return shell("Lesson plan", b + "</main>\n")

def facilitator(recs):
    F = opt("FACILITATOR", [])
    tabs = [(sid, t) for sid, t, _c, _b in F] + [(f"ros{d}", f"Day {d} run of show") for d in DAYS] + [("map", "MAP links and key")]
    b = bar("Facilitator kit", C.TITLE, tabs) + "<main>"
    for sid, t, c, blocks in F: b += sec(sid, t, c, "", blocks_html(blocks))
    for d in DAYS:
        rows, tot = ros_rows(d)
        b += sec(f"ros{d}", f"Day {d} run of show", f"{C.DAYDATE[d]} · {tot} minutes · {len(recs[d])} slides",
                 f'Deck: <a href="{deckp(d)}.html">{deckp(d)}</a> · Notes: <a href="{P(f"notes-day-{d}")}.html">{P(f"notes-day-{d}")}</a> · Runbook: <a href="{P(f"runbook-day-{d}")}.html">{P(f"runbook-day-{d}")}</a>',
                 blocks_html([("table", [["Time", "Min", "Block", "What happens"]] + rows + [["", f"<b>{tot}</b>", "<b>Total</b>", ""]])]))
    mq = [["#", "Day", "Question", "Answer"]] + [[i + 1, q.get("day", ""), e(q["q"]), f"<b>{'abcd'[q['a']]}</b> · {e(q['o'][q['a']])}"] for i, q in enumerate(C.MAP)]
    b += sec("map", "MAP links and the answer key", "CODED portal", f"QR codes: the MAP slides ({map_where(recs)}), the workshop home and the day pages. The key stays here and in the portal description.",
             qr_row() + blocks_html([("p", f"<b>Answer key:</b> {e(opt('MAP_KEY', ''))}"), ("table", mq)]))
    return shell("Facilitator kit", b + "</main>\n")

def runbook(d):
    items = day_demos(d)
    tabs = [("pre", "Pre-flight")] + [(f"c{i}", f"{i:02d} {v['card']}") for i, (_k, v) in enumerate(items, 1)]
    b = bar(f"Day {d}", "Demo runbook", tabs) + "<main>"
    b += (f'<div class="intro">Every demo and hands-on task for Day {d}, in teaching order: <b>what to open, what to do, what you should see, and what to do if it fails.</b></div>'
          '<div class="pre" id="pre"><h3>Pre-flight (30 minutes before)</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in opt("RUNBOOK_PREFLIGHT", [f"Open the Day {d} staff deck and press N to check the notes.", "Step through every demo slide once with the arrow key.", "Open today's sample files on the presenting laptop."])) + "</ul></div>")
    band = None
    for i, (_k, v) in enumerate(items, 1):
        if band != v["sec"]: band = v["sec"]; b += f'<div class="sec-band">{e(BLOCK[band][1])}</div>'
        steps = "".join(f"<li>{('<b>Trainer:</b> ' + e(x[4:])) if x.startswith('[T] ') else e(x)}</li>" for x in v["setup"])
        chips = "".join(f'<div class="flag"><span class="k">{e(l)}</span><span class="v">{e(t)}</span></div>' for l, t in (v["prompts"] if wk.AI else v["templates"]))
        pts = f" · {v['points']} points" if v.get("points") else ""
        b += (f'<div class="card" id="c{i}"><div class="ch-top"><span class="num">{i:02d}</span><span class="cat">{e(v["card"])} · {e(v["tool"])}</span>'
              f'<span class="pts">{("Your turn · " + str(v["minutes"]) + " min · " + e(v["solo"]) + pts) if v.get("hands_on") else "In the slide"}</span></div><h3>{e(v["title"])}</h3>'
              f'<div class="scn">{("Files: " + ", ".join(e(f) for f in v["files"])) if v["files"] else "No file needed."}</div>'
              + (f'<div class="say"><span class="ic">▶</span><span class="t"><span class="lbl">Say</span>“{e(v["say"])}”</span></div>' if v["say"] else "")
              + f'<ol class="steps">{steps}</ol>' + (f'<div class="plabel">{"Prompts: paste in this order" if wk.AI else "Templates"}</div>{chips}' if chips else "")
              + f'<div class="expect"><span class="lbl">What you should see</span>{e(v["expected"])}</div>'
              + (f'<div class="point"><span class="ic">+</span><span class="t"><span class="lbl">Finished early</span>{" · ".join(e(x) for x in v["stretch"])}</span></div>' if v["stretch"] else "")
              + f'<div class="point fail"><span class="ic">!</span><span class="t"><span class="lbl">If it fails</span>{e(v["fallback"])} The result is on the backup results page.</span></div>'
              + dl(v["files"]) + f'<div class="point"><span class="ic">◆</span><span class="t"><span class="lbl">Land this</span>{e(v["point"])}</span></div></div>\n')
    return shell(f"Day {d} · Demo runbook", b + "</main>\n")

def backups(d):
    items = day_demos(d)
    b = bar(f"Day {d}", "Backup results", [("demos", "Backup results"), ("files", "Files")]) + "<main>"
    cards = "".join(f'<div class="card lab"><span class="tag">{e(BLOCK[v["sec"]][1])} · {e(v["card"])}</span><h3>{e(v["title"])}</h3>'
                    f'<div class="meta">{e(v["tool"])}{(" · input: " + ", ".join(e(f) for f in v["files"])) if v["files"] else ""}</div>{blocks_html(v["backup"])}</div>' for _k, v in items)
    b += sec("demos", "Backup results", "if a demo fails", "The result each demo and task should produce, from the fictional files. " + e(C.SAMPLE_NOTE), cards)
    b += sec("files", "Files", f"Day {d}", "", dl(sorted({f for _k, v in items for f in v["files"]})))
    return shell(f"Day {d} · Backup results", b + "</main>\n")

def answer_key(d, recs):
    tasks = [(k, v) for k, v in day_demos(d) if v.get("hands_on")]
    checks = [r for r in recs[d] if r["kind"] == "check"]
    tabs = [(f"t{v['skill']}", f"Task {v['skill']}") for _k, v in tasks] + [("checks", "Quick checks")] + ([("mapkey", "MAP key")] if d == wk.LAST else [])
    b = bar(f"Day {d}", "Answer keys", tabs) + '<main><div class="intro"><b>Trainer only.</b> Every task answer and every quick-check answer. Participant pages give hints, never these answers.</div>'
    for _k, v in tasks:
        inner = (f'<div class="card lab"><span class="tag">{e(v["card"])} · {v["minutes"]} min · {e(v["solo"])}' + (f' · {v["points"]} points' if v.get("points") else "") + f'</span><h3>{e(v["title"])}</h3>'
                 f'<div class="meta">{", ".join(e(f) for f in v["files"]) or "No file"}</div><div class="hint"><span class="lbl">Hint (the participant pages show this)</span>{e(v["hint"])}</div>'
                 f'<div class="ans"><span class="lbl">Answer</span>{blocks_html(v["answer"] or v["backup"])}</div></div>')
        b += sec(f"t{v['skill']}", f"Task {v['skill']}", v["deliverable"], "", inner)
    rows = [["Slide", "Question", "Answer"]] + [[r["n"], e(r["question"]), f"<b>{e(r['answer'])}</b>"] for r in checks]
    b += sec("checks", "Quick checks", f"{len(checks)} in the deck", "Each quick check shows the right answer in green after the first tap.", blocks_html([("table", rows)]))
    if d == wk.LAST:
        mq = [["#", "Question", "Answer"]] + [[i + 1, e(q["q"]), f"<b>{'abcd'[q['a']]}</b> · {e(q['o'][q['a']])}"] for i, q in enumerate(C.MAP)]
        b += sec("mapkey", "MAP test key", "the same in the portal description", "", blocks_html([("table", mq)]))
    return shell(f"Day {d} · Answer keys", b + "</main>\n")

LABELS = (("time", "Time"), ("do", "Do"), ("expect", "Expect"), ("more", ""), ("silent", "If silent"), ("fallback", "Fallback"), ("say", "Say"))
def notes_page(d, recs):
    T = DK.topics(d)
    b = bar(f"Day {d}", "Presenter notes", []) + f'<main><div class="intro">Day {d} · {e(C.DAYS[d]["title"])} · <span id="pt">{len(recs[d])}</span> slides. The same notes show in the staff deck when you press N.</div>'
    for r in recs[d]:
        n = r["note"]; li = ""
        for k, lab in LABELS:
            v = n.get(k)
            if not v: continue
            if k == "more": li += "".join(f"<li>{e(wk.strip(x))}</li>" for x in v)
            else: li += f"<li><b>{lab}</b>{e(wk.strip(v))}</li>"
        b += (f'<div class="note-card" id="n{r["n"]}" data-flat="{e(r["flat"])}"><div class="nh"><span class="nn">{r["n"]:02d}</span><span class="nt">{e(n["h"])}</span>'
              f'<span class="nk">{e(T.get(n["t"], n["t"]))} · {e(r["kind"])}</span></div><ul>{li}</ul></div>')
    return shell(f"Day {d} · Presenter notes", b + "</main>\n")

def lab_key(d):
    L = wk.LABS[d]
    b = bar(f"Day {d}", "Lab key", []) + f'<main><div class="intro"><b>{e(L["title"])}</b>. The public lab page checks flags without showing them. The answers are only here.</div>'
    for i, s in enumerate(L["steps"], 1):
        ck = s.get("check") or {}
        flag = f'<div class="ans"><span class="lbl">Flag</span><b>{e(ck["answer"])}</b></div>' if ck.get("kind") == "flag" else ""
        b += (f'<div class="card lab"><span class="tag">Step {i}</span><h3>{e(s["title"])}</h3><div class="meta">{e(ck.get("label", ""))}</div>{flag}'
              f'<div class="ans"><span class="lbl">Answer</span>{blocks_html(s.get("answer", []))}</div></div>')
    return shell(f"Day {d} · Lab key", b + "</main>\n")

def pages():
    recs = DK.all_records()
    out = {"index.html": staff_index(recs), P("lesson-plan") + ".html": lesson_plan(recs), P("facilitator-kit") + ".html": facilitator(recs)}
    for d in DAYS:
        out[P(f"runbook-day-{d}") + ".html"] = runbook(d)
        out[P(f"backup-day-{d}") + ".html"] = backups(d)
        out[P(f"answer-key-day-{d}") + ".html"] = answer_key(d, recs)
        out[P(f"notes-day-{d}") + ".html"] = notes_page(d, recs)
        if d in wk.LABS: out[P(f"lab-key-day-{d}") + ".html"] = lab_key(d)
    return out

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, wk.STAFF), exist_ok=True)
    open(os.path.join(OUT, wk.STAFF, P("staff.css")), "w", encoding="utf-8").write(wk.theme(wk.asset("staff.css").replace("__PFX__", wk.PFX)))
    pg = pages()
    for n, h in pg.items(): open(os.path.join(OUT, wk.STAFF, n), "w", encoding="utf-8").write(h)
    print(len(pg), "staff pages")
