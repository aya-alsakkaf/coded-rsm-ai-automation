# -*- coding: utf-8 -*-
"""Builds the public pages (GIG layout, Finance glass theme) and the trainer pages under /staff."""
import os
from kit_common import ESC, icon, lockup, page, head, topbar, foot_mini, map_slot, qr_svg, REVEAL_JS, COPY_JS
from content_core import (CODE, PROGRAM, CLIENT, DAYS, FILES, AGENTS, HABIT, MAP, HOURS, VENUE, VENUE_SHORT, FIRM)
from content_prompts import PROMPTS
from content_takeaways import CHEAT, EXPRESSIONS, SAFE, GUIDE, STOP
from content_slides import SLIDES, SECTIONS
import content_staff as ST

FILE_DESC = {f: d for f, d, _ in FILES}


def n_slides():
    return sum(len(v) for v in SLIDES.values())


def n_tasks():
    return sum(1 for d in DAYS for t in d["tasks"])


def n_prompts():
    return sum(1 + len(p.get("extra", [])) for v in PROMPTS.values() for p in v)


def file_link(f, prefix=""):
    return f'<a href="{prefix}{f}" download>{ESC(f)}</a>'


def res_file(f, prefix=""):
    return (f'<a class="res" href="{prefix}{f}" download><span class="res-ic file">{icon("file", 16)}</span>'
            f'<span class="res-nm">{ESC(f)}</span><span class="res-tag">Fictional file</span></a>')


def res_page(href, name, tag, ic="book"):
    return (f'<a class="res" href="{href}"><span class="res-ic">{icon(ic, 16)}</span>'
            f'<span class="res-nm">{ESC(name)}</span><span class="res-tag">{ESC(tag)}</span></a>')


# ───────────────────────── home ─────────────────────────
def hero_scene():
    nodes = [("Chat", "You ask"), ("Agent", "It knows the job"), ("Workflow", "The work starts it")]
    xs = [130, 460, 790]
    g = []
    for i, (x, (a, b)) in enumerate(zip(xs, nodes)):
        hot = " hot" if i else ""
        g.append(f'<g class="dtbob" style="--delay:{i * .4}s"><circle cx="{x}" cy="62" r="30" fill="rgba(47,116,214,.16)" stroke="#6F9CE8" stroke-width="1.5"/>'
                 f'<circle cx="{x}" cy="62" r="30" fill="none" stroke="#9FC0F5" stroke-width="1" class="dtring" style="--delay:{i}s"/>'
                 f'<text x="{x}" y="67" text-anchor="middle" class="viz-lbl big">{i + 1}</text></g>'
                 f'<text x="{x}" y="118" text-anchor="middle" class="viz-lbl{hot}">{ESC(a)}</text>'
                 f'<text x="{x}" y="138" text-anchor="middle" class="viz-lbl dim">{ESC(b)}</text>')
    lines = (f'<path d="M170 62 H420" stroke="#6F9CE8" stroke-width="1.5" class="dtdash" fill="none"/>'
             f'<path d="M500 62 H750" stroke="#6F9CE8" stroke-width="1.5" class="dtdash" fill="none"/>'
             f'<text x="295" y="48" text-anchor="middle" class="viz-lbl dim">Day 1</text>'
             f'<text x="625" y="48" text-anchor="middle" class="viz-lbl dim">Day 2</text>')
    desk = f'<svg class="viz hero-scene" viewBox="0 0 920 150" role="img" aria-label="Chat, then agent on Day 1, then workflow on Day 2">{lines}{"".join(g)}</svg>'
    mob = ['<svg class="viz hero-scene mob" viewBox="0 0 340 250" role="img" aria-label="Chat, agent, workflow">']
    for i, (a, b) in enumerate(nodes):
        y = 40 + i * 80
        mob.append(f'<circle cx="60" cy="{y}" r="24" fill="rgba(47,116,214,.16)" stroke="#6F9CE8" stroke-width="1.5"/>'
                   f'<text x="60" y="{y + 5}" text-anchor="middle" class="viz-lbl big">{i + 1}</text>'
                   f'<text x="104" y="{y - 2}" class="viz-lbl{" hot" if i else ""}">{ESC(a)}</text><text x="104" y="{y + 16}" class="viz-lbl dim">{ESC(b)}</text>')
        if i < 2:
            mob.append(f'<path d="M60 {y + 26} V{y + 54}" stroke="#6F9CE8" stroke-width="1.5" class="dtdash"/>')
    mob.append("</svg>")
    return f'<div class="hero-scene-wrap">{desk}{"".join(mob)}</div>'


def build_home():
    d1, d2 = DAYS
    stats = [(len(DAYS), "days"), (n_slides(), "slides"), (n_tasks(), "hands-on tasks"), (n_prompts(), "prompts to copy"), (len(FILES), "sample files")]
    strip = "".join(f'<div class="stat rvl"><b data-count="{n}">{n}</b><span>{ESC(l)}</span></div>' for n, l in stats)
    cards = []
    for d in DAYS:
        n = d["n"]
        lis = "".join(f'<li>{icon("check", 16)}<span>{ESC(b)}</span></li>' for b in d["bullets"])
        cards.append(f'''<article class="pcard rvl"><div class="phead h-d{n}"><span class="cat">{ESC(d["cat"])}</span><span class="head-icon">{icon(d["icon"], 30)}</span>
<div class="head-meta"><span class="chip">{icon("cal", 13)} Day {n} · {ESC(d["date"])}</span><span class="chip">{icon("clock", 13)} {HOURS}</span></div></div>
<div class="pbody"><div class="kicker">Day 0{n}</div><h3>{ESC(d["title"])}</h3><p class="tagline">{ESC(d["objective"])}</p><p class="pdesc">{ESC(d["lede"])}</p>
<ul class="plist">{lis}</ul><a class="pbtn btn-d{n}" href="{page(f"day-{n}")}">Open day {n} <span class="arr">→</span></a></div></article>''')
    outcomes = "".join(f'<li>{icon("check", 16)}<span><b>Day {d["n"]}</b> · {ESC(o)}</span></li>' for d in DAYS for o in d["outcomes"])
    habit = "".join(f'<li>{icon("check", 16)}<span><b>{ESC(a)}</b> {ESC(b)}</span></li>' for a, b in HABIT["items"])
    files = "".join(res_file(f) for f, _, _ in FILES)
    body = f'''<body>
<header class="hero"><div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div><div class="glow g4"></div>
<div class="inner"><div class="pill"><span class="dot"></span>CODED Professionals · Client program</div>
<div class="lockup">{lockup()}</div>
<h1 class="headline">AI Innovation<br><span class="accent">and Automation</span></h1>
<p class="sub">A two-day, hands-on program for {ESC(CLIENT)} associates, senior associates and supervisors. Find the tasks that eat your week,
design an AI agent in <b>Claude</b>, and turn it into a workflow in <b>n8n</b>. No coding needed.</p>
<div class="meta"><span>{icon("cal", 16)} 15 and 16 Nov 2026</span><span>{icon("clock", 16)} {HOURS}</span><span>{icon("pin", 16)} {VENUE_SHORT}</span></div>
<a class="cta" href="#program">Explore the program <span class="arr">→</span></a></div>
{hero_scene()}
<div class="scrollhint">the two days ↓</div></header>
<main>
<section class="strip"><div class="wrap">{strip}</div></section>
<section class="programme" id="program"><div class="wrap">
<div class="eyebrow">The program</div><h2 class="sec-title">Two days, task to workflow.</h2>
<p class="sec-lead">{ESC(FIRM)}, a fictional audit firm in Kuwait, and two of its clients run through both days. Every file is made up,
so you can practice safely. You need a Claude account with Projects and an n8n account.</p>
<div class="cards">{"".join(cards)}</div></div></section>
<section class="band"><div class="wrap band-grid"><div class="rvl"><div class="eyebrow">Outcomes</div><h2>What you will be able to do.</h2></div>
<div><ul class="leave">{outcomes}</ul></div></div></section>
<section class="band"><div class="wrap band-grid"><div class="rvl"><div class="eyebrow">The habit</div><h2>{ESC(HABIT["title"])}</h2></div>
<div><p>{ESC(HABIT["lead"])}</p><ul class="leave">{habit}</ul>
<a class="ghost-btn" href="{page("cheat-sheet")}">{icon("book", 16)} Cheat sheet <span class="arr">→</span></a></div></div></section>
<section class="band" id="files"><div class="wrap band-grid"><div class="rvl"><div class="eyebrow">Sample files</div><h2>One firm. Two days of practice files.</h2></div>
<div><p>All sample files are fictional, made for training. {ESC(FIRM)} and its clients are not real companies. Each prompt sheet card links the file it needs.</p>
<div class="res-list">{files}</div></div></div></section>
<section class="band"><div class="wrap band-grid"><div class="rvl"><div class="eyebrow">Take away</div><h2>Keep these after the program.</h2></div>
<div><p>The cheat sheet: the framework, the instruction, the tests and the workflow skeleton on one page. The take-home guide: repeat it on your own work, safely.
Every prompt from each day is on that day's prompt sheet with a COPY button.</p>
<div class="sheet-links"><a class="ghost-btn" href="{page("cheat-sheet")}">Cheat sheet <span class="arr">→</span></a>
<a class="ghost-btn" href="{page("safe-use-card")}">Safe-use card <span class="arr">→</span></a>
<a class="ghost-btn" href="{page("take-home-guide")}">Take-home guide <span class="arr">→</span></a>
<a class="ghost-btn" href="{page("prompt-sheet-day-1")}">Day 1 prompts <span class="arr">→</span></a>
<a class="ghost-btn" href="{page("prompt-sheet-day-2")}">Day 2 prompts <span class="arr">→</span></a></div></div></div></section>
<section class="band"><div class="wrap band-grid"><div class="rvl"><div class="eyebrow">Before and after</div><h2>A short skills check, twice. Then the survey.</h2></div>
<div><p>Same questions on Day 1 and Day 2. Not graded. It measures what this program changes. Phone only, no AI.
Scan the QR code on the screen, or open the link on your phone. On Day 2, the final survey comes right after.</p>
<div class="map-list">{map_slot("pre")}{map_slot("post")}{map_slot("survey")}</div></div></div></section>
</main>
<footer class="site-foot"><div class="wrap"><div class="foot-top"><div class="foot-brand"><div class="f-lockup">{lockup()}</div>
<p>{ESC(PROGRAM)} is a CODED Professionals program for {ESC(CLIENT)}, delivered in person at CODED.</p></div>
<div class="foot-cols"><div class="foot-col"><p class="fh">The days</p><a href="{page("day-1")}">Day 1 · {ESC(d1["title"])}</a><a href="{page("day-2")}">Day 2 · {ESC(d2["title"])}</a></div>
<div class="foot-col"><p class="fh">Take away</p><a href="{page("cheat-sheet")}">Cheat sheet</a><a href="{page("safe-use-card")}">Safe-use card</a><a href="{page("take-home-guide")}">Take-home guide</a></div>
<div class="foot-col"><p class="fh">Prompts</p><a href="{page("prompt-sheet-day-1")}">Day 1</a><a href="{page("prompt-sheet-day-2")}">Day 2</a></div></div></div>
<div class="foot-divider"></div><div class="foot-bottom"><span>© 2026 CODED · Kuwait.</span><span>All sample files are fictional, made for training.</span></div></div></footer>
{REVEAL_JS}
</body></html>'''
    return head(f"{PROGRAM} · {CLIENT} · CODED", f"Two-day CODED program for {CLIENT}: AI agents in Claude and workflows in n8n.") + body


# ───────────────────────── day pages ─────────────────────────
def day_path(d):
    items = [r for r in d["ros"] if not r[0].startswith("BREAK")]
    n = len(items)
    w = 1000
    step = (w - 80) / (n - 1)
    parts = [f'<path d="M40 40 H{w - 40}" stroke="rgba(255,255,255,.18)" stroke-width="1.5"/>',
             f'<path d="M40 40 H{w - 40}" stroke="#6F9CE8" stroke-width="1.5" class="dtdash"/>']
    for i, (t, tm, _) in enumerate(items):
        x = 40 + i * step
        parts.append(f'<g class="dtlight" style="--delay:{i * .35}s;--dur:6s"><circle cx="{x:.0f}" cy="40" r="13" fill="#0E1F3D" stroke="#6F9CE8" stroke-width="1.5"/>'
                     f'<text x="{x:.0f}" y="44.5" text-anchor="middle" class="viz-lbl hot">{i + 1}</text></g>'
                     f'<text x="{x:.0f}" y="78" text-anchor="middle" class="viz-lbl dim">{tm.split("-")[0]}</text>')
    return (f'<div class="day-path-wrap"><div class="dp-eyebrow">The day in one line · {HOURS}</div>'
            f'<svg class="viz" viewBox="0 0 {w} 92" role="img" aria-label="The day in {n} blocks">{"".join(parts)}</svg></div>')


def ros_html(d):
    out, n = [], 0
    for t, tm, desc in d["ros"]:
        if t.startswith("BREAK"):
            label = t.split(":", 1)[1] if ":" in t else "Break"
            out.append(f'<li class="is-brk"><span class="brk">{icon("clock", 14)}</span><div class="rc"><div class="rt"><b>{ESC(label)}</b><span class="time">{tm}</span></div></div></li>')
        else:
            n += 1
            out.append(f'<li><span class="num">{n}</span><div class="rc"><div class="rt"><b>{ESC(t)}</b><span class="time">{tm}</span></div><div class="rd">{ESC(desc)}</div></div></li>')
    return "".join(out)


def task_card(t, prefix=""):
    steps = "".join(f"<li>{ESC(s)}</li>" for s in t["steps"])
    files = "".join(file_link(f, prefix) for f in t["files"])
    return (f'<div class="act"><div class="kicker">Your turn · {t["id"]} · {t["mins"]} min</div><h3>{ESC(t["title"])}</h3><ol>{steps}</ol>'
            f'<div class="clock"><b>{t["mins"]}:00</b> on the clock · {ESC(t["tool"])}</div>'
            f'<div class="out"><b>What to look for:</b> {ESC(t["look"])}</div>'
            + (f'<div class="act-files">{files}</div>' if files else "") + "</div>")


def build_day(d):
    n = d["n"]
    other = DAYS[1] if n == 1 else DAYS[0]
    tasks = "".join(task_card(t) for t in d["tasks"])
    outs = "".join(f'<li><span class="tn">{i + 1:02d}</span><div><b>{ESC(o)}</b></div></li>' for i, o in enumerate(d["outcomes"]))
    cover = "".join(f'<span class="chip2">{ESC(r[0])}</span>' for r in d["ros"] if not r[0].startswith("BREAK"))
    files = "".join(res_file(f) for f in d["files"])
    if n == 1:
        mp = f'<div class="panel"><h2>Before you start</h2><p class="brief">Scan the QR code on the screen, or open the link on your phone.</p><div class="map-list">{map_slot("pre")}</div></div>'
    else:
        mp = (f'<div class="panel"><h2>At the end of the day</h2><p class="brief">The same skills check as Day 1, then the final survey.</p>'
              f'<div class="map-list">{map_slot("post")}{map_slot("survey")}</div></div>')
    agents = ""
    if n == 1:
        agents = ('<div class="panel"><h2>The four agent cards</h2><p class="brief">Your team picks one at 11:40. Each one matches a kind of work in the outline.</p><div class="agent-grid">'
                  + "".join(f'<div class="act"><div class="kicker">{ESC(a["kind"])} · {ESC(a["area"])}</div><h3>{ESC(a["name"])}</h3><p>{ESC(a["short"])}</p>'
                            f'<div class="act-files">{file_link(a["input"])}{file_link(a["knowledge"])}</div></div>' for a in AGENTS)
                  + "</div></div>")
    body = f'''<body><main>{topbar(f"day-{n}")}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d{n}"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Day {n} · {ESC(d["cat"])}</span>
<div class="d-logos">{lockup()}</div></div><h1>{ESC(d["title"])}</h1><p class="lede">{ESC(d["objective"])} {ESC(d["lede"])}</p>
<div class="d-meta"><span>{icon("cal", 16)} Day {n} of 2 · {ESC(d["date"])}</span><span>{icon("clock", 16)} {HOURS}</span><span>{icon("pin", 16)} {VENUE_SHORT}, Morning Alsharekh</span></div></div></div>
<div class="d-grid"><div class="d-main">{day_path(d)}
<div class="panel"><h2>Day brief</h2>{"".join(f'<p class="brief">{ESC(b)}</p>' for b in d["brief"])}<p class="brief"><b>You build today:</b> {ESC(d["build_today"])}</p></div>
<div class="panel"><h2>Run of show</h2><p class="muted">{ESC(d["ros_note"])}</p><ul class="ros">{ros_html(d)}</ul></div>
<div class="panel"><h2>Your turn</h2><p class="brief">{len(d["tasks"])} hands-on tasks. The timer runs on the main screen. Every prompt is on your prompt sheet.</p><div class="acts">{tasks}</div>
<p class="smallnote">All sample files are fictional, made for training. Never attach real client data to a tool the firm has not approved.</p></div>
{agents}
<div class="panel"><h2>What you'll leave able to do</h2><ul class="tlist">{outs}</ul></div>
<div class="panel"><h2>What we'll cover</h2><div class="chips">{cover}</div></div></div>
<aside class="d-side">
<div class="panel cta-panel"><div class="cta-ico">{icon("slides", 20)}</div><h3>Day {n} slides</h3><p>The deck as run in the room, with every playback and task.</p>
<a class="slides-btn" href="{page(f"day-{n}-deck")}">Open the slides <span class="ar">→</span></a></div>
<div class="panel cta-panel"><div class="cta-ico">{icon("copy", 20)}</div><h3>Your prompt sheet</h3><p>Every prompt from today with a COPY button, and the file each one needs.</p>
<a class="slides-btn" href="{page(f"prompt-sheet-day-{n}")}">Open the prompts <span class="ar">→</span></a></div>
<div class="panel cta-panel"><div class="cta-ico">{icon("book", 20)}</div><h3>Cheat sheet</h3><p>The framework, the instruction, the tests and the workflow skeleton on one page.</p>
<a class="slides-btn ghost" href="{page("cheat-sheet")}">Open the cheat sheet <span class="ar">→</span></a></div>
{mp}
<div class="panel"><h2>Resources and files</h2><div class="res-list">
{res_page(page(f"day-{n}-deck"), f"Day {n} slide deck", "Slides", "slides")}{res_page(page(f"prompt-sheet-day-{n}"), f"Day {n} prompts", "Copy", "copy")}
{res_page(page("cheat-sheet"), "Cheat sheet", "Reference")}{res_page(page("safe-use-card"), "Safe-use card", "Reference", "shield")}
{res_page(page("take-home-guide"), "Take-home guide", "Your work")}{files}</div></div>
<div class="panel"><div class="res-list">{res_page(page(f"day-{other['n']}"), f"Day {other['n']} · {other['title']}", f"Day {other['n']}", "arrow")}
{res_page(page(""), "Back to the program", "Program", "back")}</div></div>
</aside></div></div></main>{foot_mini()}{REVEAL_JS}</body></html>'''
    return head(f"Day {n} · {d['title']} · {PROGRAM} · CODED", d["lede"]) + body


# ───────────────────────── prompt sheets ─────────────────────────
def prompt_card(p, prefix=""):
    when = "".join(f"<li>{ESC(s)}</li>" for s in p["when"])
    extra = "".join(f'<div class="sh-extra"><div class="sh-plab">{ESC(lab)}</div><div class="sh-promptwrap"><pre>{ESC(txt)}</pre>'
                    f'<button class="sh-copy" type="button">COPY</button></div></div>' for lab, txt in p.get("extra", []))
    files = "".join(file_link(f, prefix) for f in p["files"]) or '<span class="sh-none">No file needed</span>'
    team = '<span class="sh-tag sh-team">Team</span>' if p.get("team") else ""
    return f'''<section class="sh-card" id="p{p["id"].replace(".", "-")}"><div class="sh-top"><span class="sh-blk">{ESC(p["id"])} · {ESC(p["block"])}</span><span class="sh-time">{p["time"]}</span>{team}<span class="sh-tag">{ESC(p["tool"])}</span></div>
<h3>{ESC(p["title"])}</h3><ol>{when}</ol>
<div class="sh-plab">{ESC(p["label"])}</div><div class="sh-promptwrap"><pre>{ESC(p["prompt"])}</pre><button class="sh-copy" type="button">COPY</button></div>{extra}
<div class="sh-meta"><div><span class="sh-lab">What to look for</span>{ESC(p["look"])}</div><div><span class="sh-lab">Files</span><div class="sh-files">{files}</div></div></div></section>'''


def build_prompts(n):
    d = DAYS[n - 1]
    ps = PROMPTS[n]
    sub = "".join(f'<a href="#p{p["id"].replace(".", "-")}">{ESC(p["id"])} · {ESC(p["title"])}</a>' for p in ps)
    if n == 1:
        how = ('<ol><li>Open <b>Claude</b>. For the agent builds, work inside a <b>Project</b>: the instruction goes in the project instructions, the rules file in the project knowledge.</li>'
               '<li>Press <b>COPY</b> on a card and paste. Replace anything in [square brackets].</li><li>Attach the file the card names. Every file is fictional.</li></ol>'
               '<p><b>Hint:</b> when an output is wrong, change the instruction, not the answer.</p>')
    else:
        how = ('<ol><li>Open <b>n8n</b>. Each card says which node the text goes into.</li>'
               '<li>Press <b>COPY</b> and paste into that field. Lines with <b>{{ }}</b> are expressions: drag the field from the input panel when you can.</li>'
               '<li>Paste your Day 1 instruction where the card says so. n8n has no project knowledge, so the rules go in the prompt.</li></ol>'
               '<p><b>Hint:</b> the trainer shares the workshop key for Claude on paper. Never paste it in a chat or a shared document.</p>')
    body = f'''<body><main>{topbar(f"prompt-sheet-day-{n}")}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d{n}"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Day {n} · Prompt sheet</span><div class="d-logos">{lockup()}</div></div>
<h1>Day {n} prompts</h1><p class="lede">Every prompt and template from {ESC(d["title"])}, in teaching order, with a COPY button.</p></div></div>
<div class="sheet"><div class="sh-howto"><b>How to use this sheet</b>{how}</div>
<nav class="subnav"><div class="in">{sub}</div></nav>
<div class="sh-dayhead"><h2>Day {n} · {ESC(d["title"])}</h2><span class="sh-time">{ESC(d["date"])} · {HOURS}</span></div>
{"".join(prompt_card(p) for p in ps)}
<div class="sheet-foot"><a class="ghost-btn" href="{page(f"day-{n}")}">Back to Day {n} <span class="arr">→</span></a></div></div></div></main>{foot_mini()}{COPY_JS}</body></html>'''
    return head(f"Day {n} prompts · {PROGRAM} · CODED", f"Every Day {n} prompt with a COPY button.") + body


# ───────────────────────── take-aways ─────────────────────────
def build_cheat():
    parts = []
    for c in CHEAT:
        items = "".join(f'<div class="sh-item"><span class="sh-nm">{ESC(a)}</span><span class="sh-st">{ESC(b)}</span><span class="sh-df">{ESC(cc)}</span>'
                        + (f'<span class="sh-ex">{ESC(e)}</span>' if e else "") + "</div>" for a, b, cc, e in c["items"])
        summ = f'<div class="sh-sum">{ESC(c["sum"])}</div>' if c.get("sum") else ""
        parts.append(f'<section class="sh-part"><div class="sh-ph">{ESC(c["ph"])}</div><div class="sh-pt">{ESC(c["pt"])}</div><p class="sh-psub">{ESC(c["sub"])}</p><div class="sh-grid">{items}</div>{summ}</section>')
    expr = "".join(f'<tr><td class="ex-code">{ESC(a)}</td><td>{ESC(b)}</td></tr>' for a, b in EXPRESSIONS)
    parts.append(f'<section class="sh-part"><div class="sh-ph">Part 6</div><div class="sh-pt">n8n expressions</div><p class="sh-psub">Drag a field from the input panel and n8n writes these for you.</p>'
                 f'<div class="tblwrap"><table class="tbl"><thead><tr><th>Expression</th><th>What it means</th></tr></thead><tbody>{expr}</tbody></table></div></section>')
    parts.append(f'<div class="sh-note"><span class="sh-ic">!</span><div>Before you paste anything into an AI tool, check the <a href="{page("safe-use-card")}">safe-use card</a>. The firm\'s policy decides.</div></div>')
    body = f'''<body><main>{topbar("cheat-sheet")}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d1"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Take away · Cheat sheet</span><div class="d-logos">{lockup()}</div></div>
<h1>Cheat sheet</h1><p class="lede">The framework, the instruction, the tests and the workflow skeleton, on one page.</p></div></div>
<div class="sheet">{"".join(parts)}</div></div></main>{foot_mini()}</body></html>'''
    return head(f"Cheat sheet · {PROGRAM} · CODED", "Input, instruction, output, and the workflow skeleton.") + body


def build_safe():
    cards = "".join(f'<div class="safe-card safe-{k}"><h3>{ESC(t)}</h3><p>{ESC(p)}</p><ul>{"".join(f"<li>{ESC(i)}</li>" for i in items)}</ul></div>'
                    for k, t, p, items in SAFE["cards"])
    before = "".join(f"<li>{ESC(b)}</li>" for b in SAFE["before"])
    rules = "".join(f'<li>{icon("check", 16)}<span>{ESC(r)}</span></li>' for r in SAFE["rules"])
    body = f'''<body><main>{topbar("safe-use-card")}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d2"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Take away · Safe use</span><div class="d-logos">{lockup()}</div></div>
<h1>Safe-use card</h1><p class="lede">{ESC(SAFE["intro"])}</p></div></div>
<div class="sheet"><div class="safe-grid">{cards}</div>
<section class="sh-part"><div class="sh-ph">Before you paste</div><div class="sh-pt">Three questions</div><ol class="guide-steps">{before}</ol></section>
<section class="sh-part"><div class="sh-ph">After the AI answers</div><div class="sh-pt">AI output is a first pass</div><ul class="leave">{rules}</ul></section></div></div></main>{foot_mini()}</body></html>'''
    return head(f"Safe-use card · {PROGRAM} · CODED", "Green, amber, red: sort the data before you paste.") + body


def build_guide():
    secs = "".join(f'<section class="sh-part"><div class="sh-ph">{ESC(w)}</div><div class="sh-pt">{ESC(t)}</div><ol class="guide-steps">{"".join(f"<li>{ESC(s)}</li>" for s in steps)}</ol></section>'
                   for w, t, steps in GUIDE)
    stop = "".join(f"<li>{ESC(s)}</li>" for s in STOP)
    body = f'''<body><main>{topbar("take-home-guide")}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d1"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Take away · Your work</span><div class="d-logos">{lockup()}</div></div>
<h1>Take-home guide</h1><p class="lede">Repeat what you built, on your own work, safely. Two weeks from one task to a decision.</p></div></div>
<div class="sheet">{secs}
<section class="sh-part"><div class="sh-ph">When to stop</div><div class="sh-pt">Three signs a task is not ready</div><ol class="guide-steps">{stop}</ol></section>
<div class="sh-note"><span class="sh-ic">i</span><div>Use the <a href="{page("cheat-sheet")}">cheat sheet</a> for the Agent Card and the instruction, and the <a href="{page("safe-use-card")}">safe-use card</a> before you paste anything.
The prompt sheets for <a href="{page("prompt-sheet-day-1")}">Day 1</a> and <a href="{page("prompt-sheet-day-2")}">Day 2</a> keep every template.</div></div></div></div></main>{foot_mini()}</body></html>'''
    return head(f"Take-home guide · {PROGRAM} · CODED", "Repeat it on your own work, safely.") + body


def build_404():
    body = f'''<body><main class="notfound"><div class="lockup">{lockup("/")}</div><h1>Page not found.</h1>
<p>This page does not exist. Go back to the program home for the days, the slides and the prompt sheets.</p>
<a class="cta" href="/{page("")}">Back to the program <span class="arr">→</span></a></main></body></html>'''
    return head(f"Page not found · {PROGRAM} · CODED", "Page not found.", prefix="/", css=f'<link rel="stylesheet" href="/{CODE}-site.css">') + body


# ───────────────────────── staff ─────────────────────────
def staff_banner():
    return '<div class="fac-banner"><div class="wrap-n"><span><b>Trainer pages</b> · do not share this link or the password</span><span>CODED Professionals · RSM Albazie</span></div></div>'


def build_staff_index(map_key):
    slots = "".join(map_slot(k, "../") for k in ("pre", "post", "survey"))
    setup = "".join(f'<div class="panel"><h2>{ESC(w)}</h2><ul class="leave">{"".join(f"<li>{icon('check', 16)}<span>{ESC(s)}</span></li>" for s in items)}</ul></div>' for w, items in ST.SETUP)
    body = f'''<body>{staff_banner()}<main>{topbar("staff", "../", staff=True)}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d2"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Staff · Trainer index</span><div class="d-logos">{lockup("../")}</div></div>
<h1>Trainer pages</h1><p class="lede">Decks with speaker notes, the facilitator kit, the answer key and the backups. Press <span class="kbd">N</span> in a deck for notes.</p></div></div>
<div class="staff-grid">
<div class="panel cta-panel"><div class="cta-ico">{icon("slides", 20)}</div><h3>Day 1 deck with notes</h3><p>{len(SLIDES[1])} slides. N for notes, M for the menu, B for the bell.</p><a class="slides-btn" href="{page("day-1-deck")}">Open <span class="ar">→</span></a></div>
<div class="panel cta-panel"><div class="cta-ico">{icon("slides", 20)}</div><h3>Day 2 deck with notes</h3><p>{len(SLIDES[2])} slides. The ☕ button starts the break clock.</p><a class="slides-btn" href="{page("day-2-deck")}">Open <span class="ar">→</span></a></div>
<div class="panel cta-panel"><div class="cta-ico">{icon("users", 20)}</div><h3>Facilitator kit</h3><p>Setup, run of show with every slide and note, troubleshooting.</p><a class="slides-btn" href="{page("facilitator-kit")}">Open <span class="ar">→</span></a></div>
<div class="panel cta-panel"><div class="cta-ico">{icon("lock", 20)}</div><h3>Answer key and backups</h3><p>Expected agent outputs, sort keys, quick checks and the MAP answer key.</p><a class="slides-btn" href="{page("answer-key")}">Open <span class="ar">→</span></a></div>
</div>
<div class="panel" style="margin-top:20px"><h2>MAP tests and survey</h2><p class="brief">Short links on the public site: /pre, /post and /survey. MAP answer key: {ESC(map_key)}</p><div class="map-list">{slots}</div></div>
<div class="staff-grid">{setup}</div></div></main>{foot_mini("../")}</body></html>'''
    return head(f"Staff · {PROGRAM} · CODED", "Trainer pages.", prefix="../") + body


def build_staff_kit():
    days = []
    for d in DAYS:
        n = d["n"]
        cards = []
        for i, s in enumerate(SLIDES[n]):
            title = s.get("title", "") + (" " + s["em"] if s.get("em") else "")
            if s["type"] == "exercise":
                title = s.get("title") or next((t["title"] for t in d["tasks"] if t["id"] == s["task"]), "")
            if s["type"] == "check":
                title = s["q"]
            mins = round(s["dur"] / 60) if s["dur"] >= 60 else s["dur"]
            unit = "min" if s["dur"] >= 60 else "s"
            cards.append(f'<div class="slidecard"><div class="head"><span class="n">{i + 1:02d}</span><span class="k">{ESC(SECTIONS[n][s["sec"]])} · {ESC(s["ch"])} · {mins} {unit}</span></div>'
                         f'<h2>{ESC(title)}</h2><p class="rec">{ESC(s["notes"])}</p></div>')
        total = sum(s["dur"] for s in SLIDES[n]) // 60
        days.append(f'<section class="sec" id="day{n}"><div class="eyebrow">Day {n} · {ESC(d["date"])} · {HOURS}</div><h2>{ESC(d["title"])}</h2>'
                    f'<p class="smallnote">{len(SLIDES[n])} slides · about {total} minutes of slide time · breaks and lunch as in the run of show.</p>{"".join(cards)}</section>')
    trouble = "".join(f'<tr><td><b>{ESC(a)}</b></td><td>{ESC(b)}</td></tr>' for a, b in ST.TROUBLE)
    body = f'''<body>{staff_banner()}<main>{topbar("staff", "../", staff=True)}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d1"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Staff · Facilitator kit</span><div class="d-logos">{lockup("../")}</div></div>
<h1>Facilitator kit</h1><p class="lede">Every slide with its timing and what you do or ask. Fallbacks are in the notes.</p></div></div>
<nav class="toc"><a href="#day1">Day 1</a><a href="#day2">Day 2</a><a href="#trouble">Troubleshooting</a><a href="{page("answer-key")}">Answer key</a></nav>
{"".join(days)}
<section class="sec" id="trouble"><div class="eyebrow">Troubleshooting</div><h2>What usually goes wrong</h2>
<div class="panel"><div class="tblwrap"><table class="tbl"><thead><tr><th>Symptom</th><th>Fix</th></tr></thead><tbody>{trouble}</tbody></table></div></div></section>
</div></main>{foot_mini("../")}</body></html>'''
    return head(f"Facilitator kit · {PROGRAM} · CODED", "Trainer run of show.", prefix="../") + body


def build_staff_key(map_rows):
    sorts = "".join(f'<div class="panel"><h2>{ESC(k)}</h2><div class="tblwrap"><table class="tbl"><tbody>{"".join(f"<tr><td>{ESC(a)}</td><td><b>{ESC(b)}</b></td></tr>" for a, b in v)}</tbody></table></div></div>'
                    for k, v in ST.SORT_KEYS.items())
    checks = "".join(f'<tr><td class="t">{ESC(a)}</td><td>{ESC(b)}</td><td><b>{ESC(c)}</b></td></tr>' for a, b, c in ST.CHECKS)
    exp = []
    for e in ST.EXPECTED:
        rows = "".join("<tr>" + "".join(f"<td>{ESC(c)}</td>" for c in r) + "</tr>" for r in e["rows"])
        flags = "".join(f"<li>{icon('check', 16)}<span>{ESC(f)}</span></li>" for f in e["flags"])
        exp.append(f'<div class="panel"><h2>{ESC(e["agent"])}</h2><p class="muted">{ESC(e["file"])}</p><div class="tblwrap"><table class="tbl exp-tbl"><tbody>{rows}</tbody></table></div>'
                   f'<ul class="leave">{flags}</ul><p class="exp-last">{ESC(e["last"])}</p></div>')
    mp = "".join(f'<tr><td class="t">{q}</td><td>{ESC(t)}</td><td><b>{ESC(a)}</b></td></tr>' for q, t, a in map_rows)
    body = f'''<body>{staff_banner()}<main>{topbar("staff", "../", staff=True)}
<div class="wrap"><div class="hero-wrap"><div class="d-hero h-d2"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span>Staff · Answer key</span><div class="d-logos">{lockup("../")}</div></div>
<h1>Answer key and backups</h1><p class="lede">What each agent should find, the card sort keys, the quick checks and the MAP key. If a live run fails, show the expected output from here.</p></div></div>
<nav class="toc"><a href="#agents">Expected agent outputs</a><a href="#sorts">Card sorts</a><a href="#checks">Quick checks</a><a href="#map">MAP key</a></nav>
<section class="sec" id="agents"><div class="eyebrow">Backups</div><h2>Expected agent outputs</h2>{"".join(exp)}</section>
<section class="sec" id="sorts"><div class="eyebrow">Card sorts</div><h2>Sort keys</h2><div class="staff-grid">{sorts}</div></section>
<section class="sec" id="checks"><div class="eyebrow">Quick checks</div><h2>Right answers</h2><div class="panel"><div class="tblwrap"><table class="tbl"><tbody>{checks}</tbody></table></div></div></section>
<section class="sec" id="map"><div class="eyebrow">MAP test</div><h2>Answer key (same for PRE and POST)</h2><div class="panel"><div class="tblwrap"><table class="tbl"><thead><tr><th>#</th><th>Question</th><th>Answer</th></tr></thead><tbody>{mp}</tbody></table></div></div></section>
</div></main>{foot_mini("../")}</body></html>'''
    return head(f"Answer key · {PROGRAM} · CODED", "Trainer answer key.", prefix="../") + body
