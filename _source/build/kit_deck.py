# -*- coding: utf-8 -*-
"""Renders the day decks from content_slides on the CODED deck engine (assets/deck.css + deck.js).
Two copies per day: public (no notes) and staff (notes on N)."""
import json
import os
from kit_common import ESC, icon, page, qr_svg, CODE
from content_core import DAYS, MAP, HOURS
from content_slides import SLIDES, SECTIONS, FLOW
from content_prompts import PROMPTS

HERE = os.path.dirname(__file__)
DECK_CSS = open(os.path.join(HERE, "assets", "deck.css")).read()
DECK_JS = open(os.path.join(HERE, "assets", "deck.js")).read()


def h(s):
    t = ESC(s["title"])
    if s.get("em"):
        t += f' <em>{ESC(s["em"])}</em>'
    return f'<h2 class="dk-h">{t}</h2>'


def kick(s):
    return f'<div class="dk-kicker">{ESC(s["kicker"])}</div>' if s.get("kicker") else ""


def foot(s):
    return f'<p class="dk-foot">{ESC(s["foot"])}</p>' if s.get("foot") else ""


def step_btn(label="Next step"):
    return f'<button class="rsm-step-btn" type="button">{ESC(label)} →</button>'


def timer(mins, big=True):
    return (f'<div><button class="rsm-timer" type="button" data-minutes="{mins}" aria-label="{mins} minute timer"><span class="t">{mins:02d}:00</span>'
            f'<span class="s">Start · pause</span></button><div class="rsm-tctl"><button type="button" data-tadd="60">+1 min</button>'
            f'<button type="button" data-tadd="-60">−1 min</button><button type="button" data-treset>Reset</button></div></div>')


def file_chips(files, prefix):
    return "".join(f'<a href="{prefix}{f}" download>{ESC(f)}</a>' for f in files)


def result_table(r):
    head = "".join(f"<th>{ESC(c)}</th>" for c in r["cols"])
    rows = "".join("<tr>" + "".join((f'<td><span class="rsm-st {ESC(c)}">{ESC(c)}</span></td>' if j == 1 else f"<td>{ESC(c)}</td>") for j, c in enumerate(row)) + "</tr>"
                   for row in r["rows"])
    flags = "".join(f"<li>{ESC(f)}</li>" for f in r["flags"])
    return (f'<table class="rsm-res"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
            f'<ul class="rsm-flags">{flags}</ul><div class="rsm-last">{ESC(r["last"])}</div>')


# ── slide renderers: return (inner_html, steps) ──
def r_cover(s, d, ctx):
    meta = "".join(f"<span>{ESC(x.strip())}</span>" for x in s["kicker"].split("·"))
    meta += f'<span>Day {d["n"]} of 2</span><span>{ESC(d["date"])}</span><span>{HOURS}</span>'
    return (f'<div class="rsm-cover"><div><div class="meta">{meta}</div><h1>{ESC(s["title"])}</h1><div class="sub">{ESC(s["em"])}</div>'
            f'<p class="lede">{ESC(s["lede"])}</p><div class="wait"><i></i>We\'ll begin shortly</div>'
            f'<div class="hint">Hands-on with Claude and n8n · press → to begin</div></div>'
            f'<div class="rsm-lock dk-glass"><img src="{ctx["p"]}{CODE}-coded-logo.png" alt="CODED"><span class="x">×</span>'
            f'<span class="rsm-client"><span>RSM</span> Albazie</span></div></div>'), 0


def r_opener(s, d, ctx):
    w, st = s["weak"], s["strong"]
    weak = "".join(f"<p>{ESC(p)}</p>" for p in w["reply"])
    head = f'<h2 class="dk-h one">{ESC(s["title"])} <em>{ESC(s["em"])}</em></h2>'
    return (kick(s) + head + f'''<div class="rsm-ws">
<div class="rsm-chat dk-glass"><div class="hd"><b>Claude</b><span class="rsm-tag weak">{ESC(w["label"])}</span></div>
<div class="rsm-msg">{ESC(w["prompt"])}<br><span class="file">{icon("file", 12)} {ESC(s["file"])}</span></div>
<div class="rsm-reply" data-at="1">{weak}</div></div>
<div class="rsm-chat dk-glass"><div class="hd"><b>Claude</b><span class="rsm-tag strong">{ESC(st["label"])}</span></div>
<div class="rsm-msg code">{ESC(st["prompt"])}<br><span class="file">{icon("file", 12)} {ESC(s["file"])}</span></div>
<div class="rsm-reply" data-at="2">{result_table(st["result"])}</div></div></div>
<div data-at="2">{foot(s)}</div>{step_btn("Send")}'''), 2


def r_outcomes(s, d, ctx):
    items = "".join(f'<li class="dk-glass"><span class="n">{i + 1:02d}</span><span>{ESC(o)}</span></li>' for i, o in enumerate(s["items"]))
    return f'<h2 class="dk-h one">{ESC(s["title"])}</h2><ol class="rsm-list">{items}</ol>', 0


def r_roadmap(s, d, ctx):
    story = "".join(f'<div class="dk-glass"><b>{ESC(a)}</b><span>{ESC(b)}</span></div>' for a, b in s["story"])
    ros = []
    for t, tm, _ in d["ros"]:
        if t.startswith("BREAK"):
            lab = t.split(":", 1)[1] if ":" in t else "Break"
            ros.append(f'<li class="brk"><span class="t">{tm}</span><span>{ESC(lab)}</span></li>')
        else:
            ros.append(f'<li><span class="t">{tm.split("-")[0]}</span><span>{ESC(t)}</span></li>')
    return (f'<div class="rsm-road"><div>{h(s)}<div class="rsm-story">{story}</div>{foot(s)}</div>'
            f'<ul class="rsm-ros dk-glass">{"".join(ros)}</ul></div>'), 0


def qr_card(which, cap):
    m = MAP[which]
    code = (f'<div class="code">{qr_svg(m["url"], "rsm-qrsvg")}</div>' if m["url"]
            else '<div class="pending">The QR code appears here when the survey is published.</div>')
    return f'<div class="rsm-qr dk-glass"><span class="cap">{ESC(cap)}</span>{code}<b>{ESC(m["name"])}</b></div>'


def r_map(s, d, ctx):
    if s["which"] == "pre":
        qrs = qr_card("pre", "Scan with your phone")
        then = ""
    else:
        qrs = qr_card("post", "First · scan with your phone") + qr_card("survey", "Then · the final survey")
        then = '<p class="rsm-then">Then scan the second code for the final survey.</p>'
    kicker = "MAP test · before" if s["which"] == "pre" else "MAP test · after"
    return (f'<div class="rsm-map"><div><div class="dk-kicker">{kicker}</div>{h(s)}<p class="dk-lede">{ESC(s["lede"])}</p>'
            f'<div style="margin-top:22px">{timer(s["mins"])}</div>{then}</div><div class="rsm-qrs">{qrs}</div></div>'), 0


def r_section(s, d, ctx):
    return (f'<div class="rsm-section">{kick(s)}{h(s)}<p class="dk-lede">{ESC(s["lede"])}</p></div>'), 0


def r_llm(s, d, ctx):
    mx = max(p for _, p in s["cands"])
    cands = "".join(f'<div class="rsm-cand" data-at="1"><b>{ESC(w)}</b><span class="rsm-bar"><i style="--p:{p / mx * 100:.0f}%"></i></span><span class="p">{p}%</span></div>'
                    for w, p in s["cands"])
    src, ans = s["file"]
    return (kick(s) + h(s) + f'''<div class="rsm-llm"><div class="rsm-sent dk-glass">{ESC(s["sentence"])}<span class="cursor"></span></div>
<div class="rsm-cands">{cands}</div>
<div class="rsm-fileans" data-at="2"><span class="src">{icon("file", 14)} With the file · {ESC(src)}</span><b>{ESC(ans)}</b></div>
<div class="rsm-rule" data-at="3">With a rule · IF UNSURE: write "Not found". Never guess a date.</div></div>
<div data-at="3">{foot(s)}</div>{step_btn()}'''), 3


def r_cards(s, d, ctx):
    big = " big" if s.get("big") else ""
    cards = "".join(f'<div class="rsm-card dk-glass"><span class="k">{ESC(k)}</span><h3>{ESC(t)}</h3><p>{ESC(p)}</p></div>' for k, t, p in s["cards"])
    return kick(s) + h(s) + f'<div class="rsm-cards c{s["cols"]}{big}">{cards}</div>' + foot(s), 0


def r_compare(s, d, ctx):
    def col(c):
        return f'<div class="dk-glass"><h3>{ESC(c[0])}</h3><ul>{"".join(f"<li>{ESC(i)}</li>" for i in c[1])}</ul></div>'
    return kick(s) + h(s) + f'<div class="rsm-compare">{col(s["left"])}{col(s["right"])}</div>' + foot(s), 0


def r_sort(s, d, ctx):
    chips = "".join(f'<button class="rsm-chip" type="button" data-bin="{b}">{ESC(t)}</button>' for t, b in s["cards"])
    bins = "".join(f'<div class="rsm-bin {k}" role="button" tabindex="0"><b>{ESC(n)}</b><div class="in"></div></div>' for n, k in s["bins"])
    return (kick(s) + h(s) + f'<div class="rsm-sort"><div class="rsm-pool">{chips}</div><div class="rsm-bins">{bins}</div></div>'
            + foot(s) + step_btn("Show the answer")), 1


def where(day, lit):
    return '<div class="rsm-where">' + "".join(f'<span class="{"lit" if i == lit else ""}">{ESC(x)}</span>' for i, x in enumerate(FLOW[day])) + "</div>"


def r_exercise(s, d, ctx):
    t = next((x for x in d["tasks"] if x["id"] == s["task"]), None)
    if t is None:  # a slide-only task (team forming)
        t = {"id": "Teams", "mins": s["mins"], "title": s["title"], "steps": s["steps"], "look": s["look"], "files": s["files"], "tool": "Your team"}
    steps = "".join(f"<li>{ESC(x)}</li>" for x in t["steps"])
    pref = ""
    if s.get("prompt"):
        p = s["prompt"]
        pref = f'<p class="rsm-tool">Prompt {p} · on your Day {d["n"]} prompt sheet</p>'
    files = f'<div class="rsm-files">{file_chips(t["files"], ctx["p"])}</div>' if t["files"] else ""
    band = f'Your turn · {t["id"]} · {t["mins"]} min' if t["id"] != "Teams" else f'Teams · {t["mins"]} min'
    return (f'''<div class="rsm-ex"><div><div class="rsm-band">{ESC(band)}</div><h2>{ESC(t["title"])}</h2>{where(d["n"], s["lit"])}<ol>{steps}</ol></div>
<div class="rsm-side">{timer(t["mins"])}<div class="rsm-look dk-glass"><b>What to look for</b><p>{ESC(t["look"])}</p></div>{files}{pref}
<p class="rsm-tool">{ESC(t["tool"])}</p></div></div>'''), 0


def r_player(s, d, ctx):
    n = len(s["parts"])
    labels = [p[0] for p in s["parts"]] + ["Send", "Result", "Decision"]
    steps = "".join(f'<li data-at="{i + 1}">{ESC(l)}</li>' for i, l in enumerate(labels))
    parts = "".join(f'<span class="part" data-at="{i + 1}">{ESC(txt)}</span>' for i, (_, txt) in enumerate(s["parts"]))
    res = n + 2
    return (kick(s) + h(s) + f'''<div class="rsm-player" data-res="{res}"><ol class="rsm-steps">{steps}</ol>
<div class="rsm-pane dk-glass"><div class="ins-only rsm-ins">{parts}<span class="send" data-at="{n + 1}">→ Sent, with khiran-kyc-pack.pdf attached and the policy in the project knowledge.</span></div>
<div class="res-only">{result_table(s["result"])}</div><div class="rsm-decision" data-at="{n + 3}">{ESC(s["decision"])}</div></div></div>{step_btn()}'''), n + 3


def r_parts(s, d, ctx):
    rows = '<div class="row hdr"><span></span><span class="w">Weak</span><span class="s">Strong</span></div>'
    rows += "".join(f'<div class="row"><span class="lab">{ESC(a)}</span><span class="w">{ESC(b)}</span><span class="s">{ESC(c)}</span></div>' for a, b, c in s["rows"])
    return kick(s) + h(s) + f'<div class="rsm-parts">{rows}</div>', 0


def r_check(s, d, ctx):
    opts = "".join(f'<button class="rsm-opt" type="button" data-ok="{1 if ok else 0}"><span class="l">{"ABCD"[i]}</span><span>{ESC(t)}</span></button>'
                   for i, (t, ok) in enumerate(s["options"]))
    return (f'<div class="rsm-check">{kick(s)}<p class="q">{ESC(s["q"])}</p><div class="rsm-opts">{opts}</div>'
            f'<p class="dk-foot rsm-why" data-at="1">{ESC(s["why"])}</p>{step_btn("Show the answer")}</div>'), 1


def r_demo(s, d, ctx):
    steps = "".join(f'<li class="dk-glass">{ESC(x)}</li>' for x in s["steps"])
    return (kick(s) + h(s) + f'<div class="rsm-demo"><ol>{steps}</ol><div class="rsm-side"><div class="rsm-look dk-glass"><b>Files</b>'
            f'<div class="rsm-files">{file_chips(s["files"], ctx["p"])}</div></div><p class="rsm-tool">Instruction: prompt 1.5 on the Day 1 prompt sheet</p></div></div>'), 0


def r_checklist(s, d, ctx):
    items = "".join(f'<li class="dk-glass">{icon("check", 22)}<span>{ESC(i)}</span></li>' for i in s["items"])
    return kick(s) + h(s) + f'<ul class="rsm-checklist">{items}</ul>' + foot(s), 0


def r_agents(s, d, ctx):
    cards = "".join(f'<div class="rsm-agent dk-glass"><span class="k">{ESC(a["kind"])} · {ESC(a["area"])}</span><h3>{ESC(a["name"])}</h3>'
                    f'<p>{ESC(a["output"])}</p><span class="f">{ESC(a["input"])} + {ESC(a["knowledge"])}</span></div>' for a in s["agents"])
    return kick(s) + h(s) + f'<div class="rsm-agents">{cards}</div>' + foot(s), 0


def r_showcase(s, d, ctx):
    steps = "".join(f'<li class="dk-glass">{ESC(x)}</li>' for x in s["steps"])
    side = timer(s["timer"]) if s.get("timer") else ""
    return (kick(s) + h(s) + f'<div class="rsm-demo"><ol>{steps}</ol><div class="rsm-side">{side}<div class="rsm-look dk-glass"><b>Ask the room</b><p>{ESC(s["ask"])}</p></div></div></div>'), 0


def r_end(s, d, ctx):
    lines = "".join(f"<li>{ESC(x)}</li>" for x in s["lines"])
    return f'<div class="rsm-end">{h(s)}<ul>{lines}</ul><p class="next">{ESC(s["next"])}</p></div>', 0


def r_steps(s, d, ctx):
    cells = "".join(f'<div class="dk-glass"><span class="n">{i + 1:02d}</span><b>{ESC(x)}</b></div>' for i, x in enumerate(s["steps"]))
    return kick(s) + h(s) + f'<div class="rsm-strip">{cells}</div>' + foot(s), 0


def r_flow(s, d, ctx):
    nodes = "".join(f'<div class="rsm-node" data-at="{i + 1}"><span class="k">{ESC(sub)}</span><b>{ESC(nm)}</b><p>{ESC(desc)}</p></div>'
                    for i, (nm, sub, desc) in enumerate(s["nodes"]))
    return kick(s) + h(s) + f'<div class="rsm-flow n{len(s["nodes"])}">{nodes}</div>' + foot(s) + step_btn(), len(s["nodes"])


def r_code(s, d, ctx):
    rows = "".join(f'<div class="dk-glass"><code>{ESC(c)}</code><span>{ESC(t)}</span></div>' for c, t in s["items"])
    return kick(s) + h(s) + f'<div class="rsm-code">{rows}</div>' + foot(s), 0


def r_fields(s, d, ctx):
    return (kick(s) + h(s) + f'<div class="rsm-fields"><div class="dk-glass bad"><h3>A paragraph · the IF cannot read it</h3><p>{ESC(s["para"])}</p></div>'
            f'<div class="dk-glass good"><h3>Named fields · the IF reads status</h3><pre class="rsm-json">{ESC(s["json"])}</pre></div></div>' + foot(s)), 0


def r_table(s, d, ctx):
    head = "".join(f"<th>{ESC(c)}</th>" for c in s["cols"])
    rows = "".join("<tr>" + "".join(f'<td{" class=mono" if j == 2 else ""}>{ESC(c)}</td>' for j, c in enumerate(r)) + "</tr>" for r in s["rows"])
    return kick(s) + h(s) + f'<div class="dk-glass" style="padding:6px 14px;margin-top:22px;overflow:auto"><table class="rsm-tbl" style="margin-top:0"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>', 0


R = {k[2:]: v for k, v in globals().items() if k.startswith("r_")}


def build_deck(n, staff):
    d = DAYS[n - 1]
    p = "../" if staff else ""
    ctx = {"p": p}
    out = []
    for i, s in enumerate(SLIDES[n]):
        inner, steps = R[s["type"]](s, d, ctx)
        attrs = f' data-sec="{s["sec"]}" data-ch="{ESC(s["ch"])}" data-dur="{s["dur"]}"'
        if steps:
            attrs += f' data-steps="{steps}"'
        if staff:
            attrs += f' data-notes="{ESC(s["notes"])}"'
        out.append(f'<section class="dk-slide k-{s["type"]}" id="s{i + 1}"{attrs} aria-label="Slide {i + 1}"><div class="dk-wrap"><div class="dk-fit">{inner}</div></div></section>')
    css = DECK_CSS.replace("__FONT__", p)
    notes = '<div id="dk-notes" aria-live="polite"><span class="k">Speaker notes · N to hide</span><p></p></div>' if staff else ""
    cfg = json.dumps({"sections": SECTIONS[n], "staff": staff})
    title = f"Day {n} · {d['title']} · AI Innovation and Automation · CODED" + (" · Staff" if staff else "")
    return f'''<!doctype html>
<html lang="en" data-client="rsm">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>{ESC(title)}</title><link rel="icon" href="{p}{CODE}-favicon.png">
<style>{css}</style></head>
<body>
<header class="dk-top"><div class="dk-brand"><img src="{p}{CODE}-coded-logo.png" alt="CODED" width="320" height="120">
<span class="dk-crumb">CODED Professionals · <b>RSM Albazie</b> · AI Innovation and Automation · Day {n} of 2</span>
<a class="dk-daypill" href="{p}{page(f"day-{n}")}">← Day {n} page</a></div>
<div class="dk-tools"><button class="dk-ic opt" id="dk-menu-btn" type="button" title="Slide menu (M)" aria-label="Slide menu">{icon("menu", 16)}</button>
<button class="dk-ic" id="dk-bell" type="button" title="Ring the bell (B)" aria-label="Ring the bell">{icon("bell", 16)}</button>
<button class="dk-ic" id="dk-break-btn" type="button" title="Break clock" aria-label="Break clock">☕</button>
<button class="dk-ic opt" id="dk-fs" type="button" title="Full screen (F)" aria-label="Full screen">{icon("full", 16)}</button></div></header>
<main class="dk-deck">{"".join(out)}</main>
<footer class="dk-bot"><div class="dk-count" id="dk-count"></div><nav class="dk-prog" id="dk-prog" aria-label="Sections"></nav>
<div class="dk-nav"><button id="dk-prev" type="button" aria-label="Previous">←</button><button id="dk-next" type="button" aria-label="Next">→</button></div></footer>
{notes}
<div id="dk-menu" role="dialog" aria-label="All slides"><div class="grid"></div></div>
<div id="dk-break" data-default="15" role="dialog" aria-label="Break"><div><div class="cup">☕</div><h2>Break</h2><div class="clock">15:00</div><div class="back"></div>
<div class="ctl"><button type="button" data-bmin="10">10 min</button><button type="button" data-bmin="15">15 min</button><button type="button" data-bmin="60">Lunch · 60 min</button><button type="button" data-bclose>Back to the slides</button></div></div></div>
<script>window.DECK={cfg};</script>
<script>{DECK_JS}</script>
</body></html>'''
