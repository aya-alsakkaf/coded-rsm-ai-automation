# -*- coding: utf-8 -*-
"""Slide helpers and the deck builder (CODED Playbook deck kit, glass theme, CODED-only or CODED and client mix).

The kit's build_deck.py does `from deck import *` and writes each day as a list of helper calls:
    def day1():
        s = opening(1, opener=[story(...), showcase(...)])     # cover -> pre-MAP (first day) -> opener -> outcomes -> today's map
        s.append(term("b1t1", "b1", "Block 1 · the idea", ...,  n=N(do="...", expect="...", silent="...", say="...")))
        ...
        return s
    DAYFN = {1: day1, 2: day2}
Every helper takes its speaker note as explicit parts, N(say, do, expect, silent, fallback, more, time). A helper never
copies the slide's own text into the note. Demo and task helpers add the demo's own trainer fields (expected, fallback,
say), which are not on the slide. The close slide is added by the engine.

    python3 deck.py OUTDIR   -> OUTDIR/<deck>.html (public, no notes) + OUTDIR/staff/<deck>.html (trainer copy, notes on N)
                                + _source/kit-pages/slides-day-N.json and presenter-notes-day-N.json (the record the validator checks)
"""
import os, re, sys, json, base64
import wk
from wk import C, e, hl, strip, asset, DEMOS, P

def KB():
    """The kit's build_deck module (imported lazily: it imports this module first)."""
    import build_deck
    return build_deck

# ------------------------------------------------------------------ speaker notes: explicit parts only
def N(say=None, do=None, expect=None, silent=None, fallback=None, more=(), time=None):
    """One speaker note. say: the line to say. do: what the trainer does or asks. expect: the expected answer.
    silent: what to do if the room is silent. fallback: what to do if it fails. more: extra lines. time: the timing."""
    return {"say": say, "do": do, "expect": expect, "silent": silent, "fallback": fallback, "more": list(more or ()), "time": time}
def _merge(base, n):
    out = dict(N()); out.update({k: v for k, v in (base or {}).items() if v})
    if n:
        for k, v in n.items():
            if k == "more": out["more"] = list(out.get("more") or []) + list(v or [])
            elif v: out[k] = v
    return out
def flat_note(n):
    """The note as one plain line (the deck's N panel and the validator use the same text)."""
    parts = []
    if n.get("time"): parts.append(strip(n["time"]) + ".")
    if n.get("do"): parts.append("Do: " + strip(n["do"]))
    if n.get("expect"): parts.append("Expect: " + strip(n["expect"]))
    parts += [strip(x) for x in n.get("more") or []]
    if n.get("silent"): parts.append("If the room is silent: " + strip(n["silent"]))
    if n.get("fallback"): parts.append("Fallback: " + strip(n["fallback"]))
    if n.get("say"): parts.append("Say: “" + strip(n["say"]).strip("“”\"") + "”")
    return wk.fix_text(" · ".join(p for p in parts if p))

# ------------------------------------------------------------------ a slide carries its own record (kit words, engine words, note)
class Slide(str):
    rec = None
def _slide(html, sid, kind, title, topic, head, kit, chrome, note):
    s = Slide(html)
    s.rec = {"id": sid, "kind": kind, "title": strip(title), "topic": topic,
             "kit": [strip(wk.fix_text(str(x))) for x in kit if x not in (None, "")],
             "chrome": [str(x) for x in chrome if x], "note": dict(note, t=topic, k=kind, h=strip(head))}
    return s

STATE = {"day": None, "topic": None}
def ic(name): return f'<svg class="cd-ic"><use href="#{name}"/></svg>'
def key(t, goal=False): return f'<p class="wk-key{" wk-key--goal" if goal else ""}">{t}</p>'
def eyebrow(t, rule=False): return f'<div class="cd-eyebrow">{t}{"<span class=cd-rule></span>" if rule else ""}</div>'
def head(eb, title, chip=None):
    c = f'<div class="wk-chips"><span class="cd-chip">{chip}</span></div>' if chip else ""
    return f'<div class="cd-head"><div>{eyebrow(eb)}<h2 class="cd-h2">{hl(title)}</h2></div>{c}</div>'
def table(headr, rows, cls=""):
    return (f'<div class="wk-tw"><table class="wk-table {cls}"><thead><tr>' + "".join(f"<th>{x}</th>" for x in headr) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")
def files_html(files):
    if not files: return ""
    return '<div class="wk-files">' + "".join(f'<span class="cd-chip wk-file">{ic("i-folder")}{e(f)}</span>' for f in files) + "</div>"
TIMER_WORDS = ["+1 min", "Reset", "Your time", "min", "Time"]
def timer(mins):
    return (f'<span class="wk-timer-pair"><button class="cd-timer" type="button" aria-pressed="false" data-wk-min="{mins}" title="Click to start or pause">'
            f'<span class="cd-dot"></span><span class="cd-t">{mins}:00</span></button><button class="wk-reset wk-plus" type="button" aria-label="Add one minute">+1 min</button>'
            f'<button class="wk-reset" type="button" aria-label="Reset the timer">Reset</button></span>')
def topics(day): return KB().TOPICS[day]
def sections(day):
    kb = KB()
    if getattr(kb, "SECTIONS", None) and day in kb.SECTIONS: return kb.SECTIONS[day]
    glyphs = ["g-mark", "g-code", "g-frame", "g-impact", "g-future", "g-progress"]
    out = []
    for i, (t, name) in enumerate(topics(day).items()):
        out.append((name.split(" · ")[0], glyphs[min(i, len(glyphs) - 1)] if t != "close" else "g-progress", [t]))
    return out
def flow(day):
    kb = KB()
    if getattr(kb, "FLOW", None) and day in kb.FLOW: return kb.FLOW[day]
    ts = [t for t in topics(day) if t not in ("open", "close")]
    return ([topics(day)[t].split(" · ")[0] for t in ts], {t: i for i, t in enumerate(ts)})
def where():
    steps, lit = flow(STATE["day"])
    k = lit.get(STATE["topic"])
    if k is None: return ""
    name = topics(STATE["day"]).get(STATE["topic"], "")
    return f'<div class="where"><span class="s7-k">Where we are</span><div class="big-fc mini" data-flow="day" data-lit="s{k + 1}"></div><small>{e(name)}</small></div>'
def section(cls, inner, title, sid=None, dur=None, extra=""):
    i = f' id="{sid}"' if sid else ""
    d = f' data-dur="{int(dur)}"' if dur else ""
    return (f'<section class="cd-slide {cls}"{i} data-sec="§SEC§" data-ch="{e(strip(title))}" data-screen-label="§LBL§ {e(strip(title))}"{d} data-notes="§NOTE§"{extra}>\n'
            f' <div class="cd-wrap">\n{inner}\n </div>\n</section>\n')
def _t(topic): STATE["topic"] = topic

# ------------------------------------------------------------------ teaching slides
def story(sid, topic, label, al, text, hook, main, n=None, time=None):
    _t(topic)
    m = re.match(r"\D*?(\d+)", label.split(" ·")[0])
    num = f'{int(m.group(1)):02d}' if m else "·"
    inner = (f'  <div class="cd-sec-panel"><span class="cd-sec-num">{num}</span><span class="cd-sec-lbl">{e(label)}</span></div>\n'
             f'  <div class="cd-sec-body">\n    {eyebrow(e(label.split(" · ", 1)[-1]), rule=True)}\n'
             f'    <div class="wk-story"><span class="cd-k">The starting point · {e(al)}</span><p>{text}</p></div>\n'
             f'    <h1 class="cd-h1">{hl(hook)}</h1>\n    {key("<b>By the end of this block:</b> " + e(main), goal=True)}\n  </div>')
    return _slide(section("cd-slide--section wk-story-slide", inner, label, sid=sid), sid, "story", label, topic, label,
                  [label, al, text, hook, main, num], ["The starting point", "By the end of this block:"], _merge({"time": time}, n))

def rule(sid, topic, tag, big, sub, n=None):
    _t(topic)
    inner = f'  {eyebrow(e(tag), rule=True)}\n  <h2 class="cd-h1 wk-rule">{hl(big)}</h2>\n  <p class="cd-lede wk-lead">{sub}</p>'
    return _slide(section("cd-slide--stage wk-statement", inner, strip(big), sid=sid), sid, "rule", big, topic, big, [tag, big, sub], [], _merge({}, n))

def term(sid, topic, tag, title, t, defn, frm, to, take, n=None):
    _t(topic)
    inner = (head(e(tag), title, "The idea") + f'\n  <div class="wk-def"><span class="cd-k">{e(t.upper())}</span><p>{defn}</p></div>'
             f'\n  <div class="wk-link"><div>{frm}</div><span class="wk-link-ar">{ic("i-arrow")}</span><div class="wk-link-to">{to}</div></div>\n  ' + key(take))
    return _slide(section("cd-slide--stage", inner, title, sid=sid), sid, "term", title, topic, title, [tag, title, t, defn, frm, to, take], ["The idea"], _merge({}, n))

def listslide(sid, topic, tag, title, items, take, n=None):
    _t(topic)
    li = "".join(f'<li class="cd-up" style="--i:{i}">{ic("i-check")}<span>{x}</span></li>' for i, x in enumerate(items))
    inner = head(e(tag), title) + f'\n  <ul class="wk-checks wk-checks--big">{li}</ul>\n  ' + key(take)
    return _slide(section("cd-slide--stage", inner, title, sid=sid), sid, "list", title, topic, title, [tag, title, take] + list(items), [], _merge({}, n))

def cards3(sid, topic, tag, title, cards, take, src=None, n=None):
    """Three (or four) cards: (label, heading, text, small line) or (kind, label, heading, text, small line).
    The kinds green, amber and red keep their meaning."""
    _t(topic)
    cc, kit = "", [tag, title, take, src]
    for i, c in enumerate(cards):
        k, a, b, c_, d = (c if len(c) == 5 else ("",) + tuple(c))
        kit += [a, b, c_, d]
        cc += (f'<div class="cd-card cd-up wk-c3{" wk-c3--" + k if k else ""}" style="--i:{i}"><span class="cd-k">{e(a)}</span><b>{b}</b><p>{c_}</p>'
               + (f'<small>{d}</small>' if d else "") + '</div>')
    inner = (head(e(tag), title) + f'\n  <div class="cd-cards cd-cols-{min(4, len(cards))} wk-cards">{cc}</div>\n  ' + key(take)
             + (f'\n  <p class="wk-src">{src}</p>' if src else ""))
    return _slide(section("cd-slide--stage", inner, title, sid=sid), sid, "cards", title, topic, title, kit, [], _merge({}, n))

def stats(sid, topic, tag, title, cards, take, src=None, n=None):
    """Big numbers: (number, label, text). Every number needs a source line."""
    _t(topic)
    cc = "".join(f'<div class="cd-card cd-up wk-stat" style="--i:{i}"><b class="wk-stat-n">{e(a)}</b><span class="cd-k">{e(b)}</span><p>{c}</p></div>' for i, (a, b, c) in enumerate(cards))
    inner = (head(e(tag), title) + f'\n  <div class="cd-cards cd-cols-{min(4, len(cards))} wk-cards">{cc}</div>\n  ' + key(take)
             + (f'\n  <p class="wk-src">{src}</p>' if src else ""))
    return _slide(section("cd-slide--stage", inner, title, sid=sid), sid, "stats", title, topic, title, [tag, title, take, src] + [x for c in cards for x in c], [], _merge({}, n))

def tslide(sid, topic, tag, title, headr, rows, take, cls="", n=None):
    _t(topic)
    tc = " ".join({"tight": "wk-table--tight", "dims": "wk-table--dims"}.get(x, "") for x in cls.split())
    inner = head(e(tag), title) + "\n  " + table(headr, rows, tc) + "\n  " + key(take)
    return _slide(section("cd-slide--stage", inner, title, sid=sid), sid, "table", title, topic, title, [tag, title, take] + list(headr) + [c for r in rows for c in r], [], _merge({}, n))

def check(sid, topic, q, opts, n=None):
    """Quick check: opts = [(text, 1 if right else 0, feedback)]. After any tap the right answer shows green."""
    _t(topic)
    ok = [i for i, o in enumerate(opts) if o[1] == 1]
    assert len(ok) == 1, f"{sid}: a quick check needs exactly one right option"
    letters = "ABCD"
    bt = "".join(f'<button type="button" aria-pressed="false"{" data-correct" if k == 1 else ""} data-fb="{e(fb)}"><span class="cd-key">{letters[i]}</span><span>{e(t)}</span></button>'
                 for i, (t, k, fb) in enumerate(opts))
    inner = (f'  <span class="cd-hint wk-check-hint">{ic("i-chat")}Quick check</span>\n  <h2 class="cd-h2 wk-check-q">{q}</h2>\n'
             f'  <div class="cd-mcq wk-mcq">{bt}</div>\n  <div class="wk-fb" aria-live="polite"></div>')
    base = {"time": "1 min", "do": "Read the question. Ask for hands up on each option, then tap the most popular one.",
            "expect": f"Option {letters[ok[0]]}.", "silent": "ask one table to choose together, then tap their choice."}
    s = _slide(section("cd-slide--stage wk-check", inner, "Quick check", sid=sid), sid, "check", "Quick check", topic, "Quick check",
               [q] + [o[0] for o in opts], ["Quick check"] + list(letters[:len(opts)]) + ["Correct", "Not quite"], _merge(base, n))
    s.rec["answer"] = opts[ok[0]][0]; s.rec["question"] = strip(q)
    return s

SORT_KIND = {"green": "green", "amber": "amber", "red": "red"}
def sortslide(sid, topic, tag, title, items, labels, did=None, n=None):
    """Card sort: items = [(text, key)], labels = {key: label}. green, amber, red keep their meaning; other keys get accent shades."""
    _t(topic)
    keys = list(labels)
    kind = {k: SORT_KIND.get(k, f"a{i % 3 + 1}") for i, k in enumerate(keys)}
    cards = "".join(f'<button class="wk-sc cd-up wk-sc--{kind[c]}" style="--i:{i}" type="button"><span class="wk-sc-t">{e(t)}</span><span class="wk-sc-ans">{e(labels[c])}</span><span class="wk-sc-q">tap to reveal</span></button>'
                    for i, (t, c) in enumerate(items))
    leg = "".join(f'<span><i class="wk-dot wk-dot--{kind[c]}"></i>{e(l)}</span>' for c, l in labels.items())
    inner = head(e(tag), title) + f'\n  <div class="wk-sort wk-sort--{3 if len(items) <= 6 else 4}">{cards}</div><div class="wk-sc-legend">{leg}</div>'
    d = DEMOS.get(did, {}) if did else {}
    base = {"time": "8 min", "do": "Read each card aloud. The room calls the answer, then tap the card.",
            "expect": d.get("expected"), "fallback": d.get("fallback"), "say": d.get("say")}
    return _slide(section("cd-slide--stage wk-sort-slide", inner, title, sid=sid, dur=480), sid, "sort", title, topic, title,
                  [tag, title] + [t for t, _c in items] + list(labels.values()), ["tap to reveal"], _merge(base, n))

def widget(sid, topic, did, tag, title, html, take, n=None, time=None):
    """A topic demo the kit draws itself (no AI tool): the kit's HTML goes in the slide as it is."""
    _t(topic)
    d = DEMOS[did]
    inner = head(e(tag), title, e(d["tool"])) + f'\n  {html}\n  ' + key(take)
    base = {"time": time, "do": " ".join(x.replace("[T] ", "") for x in d["setup"]), "expect": d["expected"], "fallback": d["fallback"], "say": d["say"]}
    return _slide(section("cd-slide--stage wk-demo", inner, f"Demo {d['skill']}", sid=sid), sid, "widget", f"Demo {d['skill']}", topic,
                  f"Demo {d['skill']}: {d['title']}", [tag, title, take, d["tool"], _text(html)], [], _merge(base, n))
def _text(h):
    """The visible words of kit HTML (scripts and styles dropped)."""
    import html as H
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
    return H.unescape(re.sub(r"<[^>]+>", " ", h)).replace("<", " ").replace(">", " ")   # an address in <...> stays text

def task(sid, topic, did, title=None, steps=None, n=None):
    """A hands-on task slide: steps, files, timer, what to look for, finished early. Prompts (AI) or templates (no AI) show in a panel."""
    _t(topic)
    d = DEMOS[did]; mins = d["minutes"]; solo = d["solo"]
    st = steps or wk.task_steps(d)
    pts = f' · {d["points"]} points' if d.get("points") else ""
    fin = f'<p class="wk-more"><b>Finished early?</b> {e(" ".join(d["stretch"]))}</p>' if d["stretch"] else ""
    ex_ = table(["Weak prompt", "Your rewrite"], [[f"“{e(a)}”", "…"] for a in d["examples"]], "wk-table--tight") if d.get("examples") else ""
    kit = [d["card"], solo, d["tool"], title, d["hint"], " ".join(d["stretch"])] + list(d["files"]) + list(st) + list(d.get("examples", []))
    chrome = ["Your turn", "Finished early?", "What to look for", "Weak prompt", "Your rewrite", "points"] + TIMER_WORDS
    if wk.AI and d["prompts"]:
        tl = sum(len(t) for _l, t in d["prompts"])
        body = "".join(f'<div class="wk-msg wk-msg--me"><span class="wk-msg-k">{e(l)}</span><span class="ptxt">{e(t)}</span><button class="wk-copy" type="button">Copy</button></div>' for l, t in d["prompts"])
        body += f'<div class="wk-msg wk-msg--them"><span class="wk-msg-k">What to look for</span>{e(d["hint"])}</div>'
        foot = f'{e(d["card"])} is on your {e(wk.SHEET["name"].lower())}. {e(opt_text("TASK_FALLBACK_LINE", "If the tool is slow, continue from the backup on the screen."))}'
        panel = (f'<div class="wk-chat{" wk-chat--tight" if tl > 300 or len(st) > 3 else ""}"><div class="wk-chat-bar"><span class="wk-chat-av">{ic("i-chat")}</span>'
                 f'<div><b>{e(d["tool"])}</b><small>copy, paste, then check</small></div></div><div class="wk-chat-body">{body}</div><div class="wk-chat-foot">{foot}</div></div>')
        kit += [x for p in d["prompts"] for x in p] + [opt_text("TASK_FALLBACK_LINE", "")]
        chrome += ["Copy", "copy, paste, then check", "is on your", wk.SHEET["name"].lower(), "If the tool is slow, continue from the backup on the screen."]
    else:
        panel = (f'<div class="cd-deliverable wk-task-note"><span><b>You hand in</b> {e(d["deliverable"])}</span></div>' if d["deliverable"] else "")
        panel += f'<div class="cd-deliverable wk-task-note"><span><b>What to look for</b> {e(d["hint"])}</span></div>'
        kit += [d["deliverable"]]; chrome += ["You hand in"]
    ttl = title or ("Your turn: <span class=\"hl\">" + e(d["title"][0].lower() + d["title"][1:]) + ".</span>")
    kit += [ttl]
    steps_html = "".join(f"<li>{e(x)}</li>" for x in st)
    inner = (f'  <div class="cd-rail">\n    <div class="cd-eyebrow wk-task-eyebrow">{e(d["card"])} · Your turn · {e(solo)} · {mins} min{pts}</div>\n'
             f'    <div class="cd-band">{ic("i-hand")}{e(d["tool"])}</div>\n    <h2 class="cd-h2">{hl(ttl)}</h2>\n    {files_html(d["files"])}\n    {where()}\n    {fin}\n  </div>\n'
             f'  <div class="cd-exercise">\n    <div class="cd-exercise-head"><span class="cd-chip">Your time: {mins} min</span>{timer(mins)}</div>\n'
             f'    <ol class="cd-steps">{steps_html}</ol>\n    {ex_}{panel}\n  </div>')
    base = {"time": f"{mins} min work, then share", "do": "Start the timer. Walk the room. Ask each pair what they found so far.",
            "expect": d["expected"], "more": [f"Give the hint at about {max(3, mins // 3)} min."], "fallback": d["fallback"], "say": d["say"]}
    if d["stretch"]: base["more"].append("Fast finishers have an extra task on the slide.")
    kit += [topics(STATE["day"]).get(topic, "")]
    chrome += ["Where we are"] + flow(STATE["day"])[0]
    return _slide(section("cd-slide--split cd-slide--exercise", inner, f"Your turn {d['skill']}", sid=sid, dur=mins * 60), sid, "task", f"Your turn {d['skill']}", topic,
                  f"Your turn {d['skill']}: {d['title']} ({mins} min, {solo}{pts})", kit, chrome, _merge(base, n))
def opt_text(name, default): return getattr(C, name, default)

# ------------------------------------------------------------------ AI branch: prompt player, opener, next-word widget
def _ai(name):
    if not wk.AI: raise SystemExit(f"{name}() is for an AI-tool workshop (content.py TOOL_MODE = 'ai'). Use widget() or scene() for a workshop without an AI tool.")
def player(sid, topic, did, n=None):
    _ai("player"); _t(topic)
    import widgets as W
    d = DEMOS[did]
    tool = d["tool"].split(" (")[0].split(" +")[0].split(" ·")[0]
    body, kit = W.player(d, tool)
    base = {"time": "3 to 4 min", "do": "Press → once per part and ask the room what each part adds. After Send, point to the table first, then the bullets. Read the decision line aloud.",
            "expect": d["expected"], "more": ["This is the ideal run. Then run the same prompt live from the prompt sheet; the live answer may use other words."],
            "fallback": d["fallback"], "say": d["say"]}
    chrome = ["Prompt playback", "Example", "typical result", "the perfect run", "fictional data", "Press", "to build the prompt, one part at a time", "file attached", "files attached",
              "Message", "The formula", "Send", "Result", "Decision", "Back", "Replay", "Next", "next step", "back", "replay", "Space", "Enter", "R",
              "Playback of the ideal run. The live tool may word it differently. All figures are fictional training data.", "Word", "Excel", "PowerPoint", "PDF", "Email", "Text", "file", "W", "X", "P", "CSV", "T", "F"]
    return _slide(section("cd-slide--stage wk-pp pp-slide", f'<div class="wk-widget">{hl(body)}</div>', f"{d['card']} · playback", sid=sid, dur=210),
                  sid, "player", f"{d['card']} · playback", topic, f"Prompt playback, {d['card']}: {d['title']}", kit, chrome, _merge(base, n))
_OPENER_JS = []
def showcase(sid, topic, W_, n=None):
    """The weak and strong opener (one per deck): the same request, a weak and a strong prompt, step by step."""
    _ai("showcase"); _t(topic)
    import widgets as W
    body, kit = W.showcase(W_)
    chrome = ["Same file", "Weak prompt", "Weak result", "Strong result", "Compare", "The lesson", "Strong prompt", "Weak", "Strong", "Message", "next", "back", "replay",
              "Space", "Enter", "R", "Example", "typical result", "Fictional training data from", "W", "X", "P", "PDF"]
    return _slide(section("cd-slide--stage wk-ws ws-slide", f'<div class="wk-widget">{hl(body)}</div>', "Opener · weak and strong prompt", sid=sid, dur=600),
                  sid, "showcase", "Opener · weak and strong prompt", topic, "Opener: weak and strong prompt", kit, chrome, _merge({"time": "10 min"}, n))
_LLM = {}
def llmslide(sid, topic, tag, title, lede, take, n=None):
    """The next-word widget, from content.py LLM = {"tree": ..., "foot": ...} (illustrative percentages)."""
    _ai("llmslide"); _t(topic)
    import widgets as W
    body, kit, js = W.llm(C.LLM)
    _LLM["js"] = js
    first = [w for w, _p in C.LLM["tree"]["start"]["opts"]]          # shown at once; the later words show only after a pick
    words = {w for k, v in C.LLM["tree"].items() if k != "start" for w, _p in v}
    inner = head(e(tag), title, "How it writes") + f'\n  <p class="cd-lede">{lede}</p>\n  <div class="wk-w">{body}</div>\n  ' + key(take)
    chrome = ["How it writes", "What word comes next? Click one.", "Temperature", "balanced", "Pick the top word", "Let the AI choose", "Start again", "Step", "of",
              "focused", "creative", "Sentence complete", "It added", "Now it predicts again, using the whole sentence so far"]
    return _slide(section("cd-slide--stage wk-llm-slide", inner, title, sid=sid, dur=420), sid, "llm", title, topic, title,
                  [tag, title, lede, take] + kit + first, chrome + sorted(words), _merge({"time": "7 min"}, n))

# ------------------------------------------------------------------ scene(): an analogy drawn as a scene, not text alone
def _person(x, y, cls="sc-line", s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="11" cy="-46" class="{cls}"/>'
            f'<path d="M0 -33 v26 M0 -27 l-13 9 M0 -27 l13 9 M0 -7 l-11 18 M0 -7 l11 18" class="{cls}"/></g>')
def _building(x, y, cls="sc-line", w=96, h=118):
    win = "".join(f'<rect x="{x - w / 2 + 14 + c * (w - 28) / 3:.0f}" y="{y - h + 22 + r * 24}" width="14" height="12" rx="2" class="sc-win dtlight" style="--dur:6s;--delay:{(r * 3 + c) * .5:.1f}s"/>'
                  for r in range(max(1, int((h - 44) / 24))) for c in range(3))
    roof = f'<path d="M{x - w / 2 - 8} {y - h} L{x} {y - h - 26} L{x + w / 2 + 8} {y - h} Z" class="{cls} sc-fill"/>'
    return f'<g>{roof}<rect x="{x - w / 2}" y="{y - h}" width="{w}" height="{h}" rx="3" class="{cls} sc-fill"/>{win}<rect x="{x - 10}" y="{y - 26}" width="20" height="26" class="{cls}"/></g>'
def _house(x, y, cls="sc-line"):
    return f'<g><path d="M{x - 34} {y - 44} L{x} {y - 74} L{x + 34} {y - 44}" class="{cls}"/><rect x="{x - 28}" y="{y - 44}" width="56" height="44" class="{cls} sc-fill"/><rect x="{x - 8}" y="{y - 22}" width="16" height="22" class="{cls}"/></g>'
def _laptop(x, y, cls="sc-line"):
    return f'<g><rect x="{x - 30}" y="{y - 44}" width="60" height="38" rx="4" class="{cls} sc-fill"/><path d="M{x - 40} {y} h80 l-8 -6 h-64 Z" class="{cls}"/><path d="M{x - 18} {y - 30} h36 M{x - 18} {y - 20} h24" class="sc-dim"/></g>'
def _phone(x, y, cls="sc-line"):
    return f'<g><rect x="{x - 14}" y="{y - 52}" width="28" height="52" rx="5" class="{cls} sc-fill"/><circle cx="{x}" cy="{y - 7}" r="2.4" class="{cls}"/></g>'
def _doc(x, y, cls="sc-line"):
    return f'<g><path d="M{x - 18} {y - 50} h24 l12 12 v38 h-36 Z" class="{cls} sc-fill"/><path d="M{x - 10} {y - 30} h20 M{x - 10} {y - 20} h20 M{x - 10} {y - 10} h14" class="sc-dim"/></g>'
def _mail(x, y, cls="sc-line"):
    return f'<g><rect x="{x - 22}" y="{y - 30}" width="44" height="30" rx="3" class="{cls} sc-fill"/><path d="M{x - 22} {y - 30} l22 17 l22 -17" class="{cls}"/></g>'
def _coin(x, y, cls="sc-line"):
    return f'<g><circle cx="{x}" cy="{y - 16}" r="16" class="{cls} sc-fill"/><path d="M{x} {y - 25} v18 M{x - 5} {y - 21} h8 a3 3 0 010 6 h-6 a3 3 0 000 6 h8" class="{cls}"/></g>'
def _lock(x, y, cls="sc-line"):
    return f'<g><rect x="{x - 18}" y="{y - 30}" width="36" height="30" rx="4" class="{cls} sc-fill"/><path d="M{x - 11} {y - 30} v-9 a11 11 0 0122 0 v9" class="{cls}"/></g>'
def _shield(x, y, cls="sc-line"):
    return f'<g><path d="M{x} {y - 56} l24 9 v18 c0 15 -10 24 -24 29 c-14 -5 -24 -14 -24 -29 v-18 Z" class="{cls} sc-fill"/><path d="M{x - 9} {y - 28} l6 6 l12 -12" class="{cls}"/></g>'
def _clock(x, y, cls="sc-line"):
    return f'<g><circle cx="{x}" cy="{y - 22}" r="22" class="{cls} sc-fill"/><path d="M{x} {y - 36} v14 l9 6" class="{cls}"/></g>'
def _chart(x, y, cls="sc-line"):
    return f'<g><path d="M{x - 30} {y} v-50 M{x - 30} {y} h60" class="sc-dim"/><path d="M{x - 20} {y} v-16 M{x - 6} {y} v-28 M{x + 8} {y} v-22 M{x + 22} {y} v-40" class="{cls}" style="stroke-width:7"/></g>'
def _magnifier(x, y, cls="sc-line"):
    return f'<g><circle cx="{x - 6}" cy="{y - 30}" r="16" class="{cls} sc-fill"/><path d="M{x + 6} {y - 18} l14 14" class="{cls}" style="stroke-width:4"/></g>'
DRAW = {"person": _person, "building": _building, "house": _house, "laptop": _laptop, "phone": _phone, "doc": _doc, "mail": _mail,
        "coin": _coin, "lock": _lock, "shield": _shield, "clock": _clock, "chart": _chart, "magnifier": _magnifier}
TONE = {None: "sc-line", "": "sc-line", "hot": "sc-hot", "dim": "sc-dim", "bad": "sc-bad", "ok": "sc-ok"}
ANIM = {"bob": "dtbob", "nod": "dtnod", "glow": "dtglow", "pop": "dtpop", None: ""}
def _pill(x, y, text, tone="", delay=None):
    w = max(70, round(len(text) * 9.2 + 28))
    t = {"hot": "hot", "bad": "bad", "ok": "ok"}.get(tone, "")
    g = (f'<rect x="{x - w / 2:.0f}" y="{y - 15}" width="{w}" height="28" rx="14" class="sc-pill {t}"/>'
         f'<text x="{x}" y="{y + 4}" text-anchor="middle" class="viz-lbl {t}">{e(text)}</text>')
    return f'<g class="dtpop" style="--dur:8s;--delay:{delay}s">{g}</g>' if delay is not None else f'<g>{g}</g>'
def scene_svg(draw, w=480, h=300):
    """draw: a list of dicts. Objects: {"person"|"building"|"house"|"laptop"|"phone"|"doc"|"mail"|"coin"|"lock"|"shield"|"clock"|"chart"|"magnifier": (x, y),
    "label": "text under it", "tone": "hot|dim|bad|ok", "anim": "bob|nod|glow|pop", "delay": s, "scale": 1.0}.
    Motion: {"move": "mail|coin|doc|person", "path": [(x, y), ...], "dur": 5, "tone": ...} moves an object along a dashed path.
    Extras: {"pill": "text", "at": (x, y), "tone": ..., "delay": s}, {"stamp": "STOP", "at": (x, y)}, {"ring": (x, y)},
    {"line": [(x, y), ...], "tone": ..., "dash": True}, {"text": "label", "at": (x, y), "tone": ...}, {"ground": y}."""
    out, labels = [], []
    for it in draw:
        tone = TONE.get(it.get("tone"), "sc-line")
        if "ground" in it:
            out.append(f'<path d="M10 {it["ground"]} H{w - 10}" class="sc-ground"/>'); continue
        if "move" in it:
            pts = it["path"]; d = "M" + " L".join(f"{x} {y}" for x, y in pts)
            fn = DRAW[it["move"]]
            obj = fn(0, 0, tone) if it["move"] != "person" else _person(0, 0, tone, .7)
            out.append(f'<path d="{d}" class="sc-path dtdash"/>')
            out.append(f'<g>{obj}<animateMotion dur="{it.get("dur", 5)}s" begin="{it.get("delay", 0)}s" repeatCount="indefinite" path="{d}"/></g>'); continue
        if "pill" in it:
            x, y = it["at"]; out.append(_pill(x, y, it["pill"], it.get("tone", ""), it.get("delay"))); labels.append(it["pill"]); continue
        if "stamp" in it:
            x, y = it["at"]; t = it["stamp"]; w2 = len(t) * 15 + 30
            out.append(f'<g class="dtstamp" style="--dur:6s;--delay:{it.get("delay", 0)}s"><rect x="{x - w2 / 2}" y="{y - 20}" width="{w2}" height="36" rx="6" class="sc-stamp" transform="rotate(-8 {x} {y})"/>'
                       f'<text x="{x}" y="{y + 6}" text-anchor="middle" class="sc-stamp-t" transform="rotate(-8 {x} {y})">{e(t)}</text></g>'); labels.append(t); continue
        if "ring" in it:
            x, y = it["ring"]; out.append(f'<circle cx="{x}" cy="{y}" r="18" class="sc-hot dtring" style="--delay:{it.get("delay", 0)}s"/>'); continue
        if "line" in it:
            d = "M" + " L".join(f"{x} {y}" for x, y in it["line"])
            out.append(f'<path d="{d}" class="{tone}{" sc-path dtdash" if it.get("dash") else ""}"/>'); continue
        if "text" in it:
            x, y = it["at"]; t = {"sc-hot": "hot", "sc-bad": "bad", "sc-ok": "ok"}.get(tone, "")
            out.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="viz-lbl {t}">{e(it["text"])}</text>'); labels.append(it["text"]); continue
        kind = next(k for k in DRAW if k in it)
        x, y = it[kind]
        g = DRAW[kind](x, y, tone) if kind != "person" else _person(x, y, tone, it.get("scale", 1.0))
        a = ANIM.get(it.get("anim"), "")
        if a: g = f'<g class="{a}" style="--delay:{it.get("delay", 0)}s">{g}</g>'
        out.append(g)
        if it.get("label"):
            t = {"sc-hot": "hot", "sc-bad": "bad", "sc-ok": "ok"}.get(tone, "")
            out.append(f'<text x="{x}" y="{y + 22}" text-anchor="middle" class="viz-lbl {t}">{e(it["label"])}</text>'); labels.append(it["label"])
    svg = f'<svg viewBox="0 0 {w} {h}" class="wk-scene" role="img" aria-label="{e(" · ".join(labels))}">{"".join(out)}</svg>'
    return svg, labels
def scene(sid, topic, tag, title, text, take, draw, n=None):
    """An analogy slide with a drawn scene: words on the left, the scene on the right."""
    _t(topic)
    svg, labels = scene_svg(draw)
    inner = (f'  <div class="wk-ana"><div class="wk-ana-text">{eyebrow(e(tag), rule=True)}<h2 class="cd-h1 wk-rule">{hl(title)}</h2>'
             f'<p class="cd-lede">{text}</p>{key(take)}</div><div class="wk-ana-viz cd-up" style="--i:1">{svg}</div></div>')
    return _slide(section("cd-slide--stage wk-scene-slide", inner, title, sid=sid), sid, "scene", title, topic, title, [tag, title, text, take] + labels, [], _merge({}, n))

# ------------------------------------------------------------------ MAP test and survey slide (build.md section 11: each QR shows its name, day and time)
def mapslide(sid, topic, when, n=None):
    _t(topic)
    after = when == "after"
    keys = [k for k in (["post", "survey"] if after else ["pre"]) if k in wk.FORMS]
    nq = len(C.MAP)
    lede = (opt_text("MAP_LEDE", {}).get(when) or
            (f"{nq} questions, the same as on Day {wk.FIRST}. Not graded. Phone only: no notes, no search, no AI. Then scan the second code for the final survey." if after else
             f"{nq} questions, the same on Day {wk.FIRST} and Day {wk.LAST}. Not graded. It measures what this workshop changes. Phone only: no notes, no search, no AI."))
    qrs = "".join(f'<a class="wk-qr-card" href="{wk.FORMS[k]["url"]}" target="_blank" rel="noopener">{wk.qr_svg(wk.FORMS[k]["url"], label=wk.FORMS[k]["name"])}'
                  f'<span class="wk-qr-lbl">{i + 1 if len(keys) > 1 else ""}{" · " if len(keys) > 1 else ""}{e(wk.FORMS[k]["name"])}</span><span class="wk-qr-when">{e(wk.FORMS[k]["when"])}</span></a>'
                  for i, k in enumerate(keys))
    inner = (f'  <div class="wk-map-grid{" wk-map-grid--two" if len(keys) > 1 else ""}">\n   <div class="wk-map-text">{eyebrow("MAP test · " + e(when), rule=True)}'
             f'<h2 class="cd-h2">Scan the QR code. <em>{wk.MAP_MIN} minutes.</em></h2><p class="cd-lede">{lede}</p>'
             f'<div class="wk-map-timer"><span class="cd-chip">Time</span>{timer(wk.MAP_MIN)}</div></div>\n'
             f'   <div class="wk-qr"><span class="cd-k wk-qr-kicker">Scan with your phone</span><div class="wk-qr-row">{qrs}</div></div>\n  </div>')
    pts = (["Leave the slide up. Code 1 is the MAP test; code 2 is the final survey, right after it."] if after else
           ["Leave the slide up while they scan. The same link is on the workshop home and the day page.", "This is also the pre-flight check: help anyone whose phone does not open the link."])
    base = {"time": f"{wk.MAP_MIN} min", "do": "Phones only. No notes, no search, no AI. It is not graded.",
            "more": pts + ["Check the response count in the portal before you move on."],
            "fallback": f"read out the short link (/{'post' if after else 'pre'}) if a phone cannot scan.",
            "say": "Answer honestly. If you are not sure, pick your best guess. This measures the workshop, not you."}
    kit = [wk.FORMS[k]["name"] for k in keys] + [wk.FORMS[k]["when"] for k in keys] + [lede, when]
    chrome = ["MAP test", "Scan the QR code.", "minutes", "Scan with your phone", "Time"] + TIMER_WORDS
    return _slide(section("cd-slide--stage wk-map-slide", inner, f"MAP test · {when}", sid=sid, dur=wk.MAP_MIN * 60), sid, "map", f"MAP test · {when}", topic,
                  "MAP test (after) and the final survey" if after else "MAP test (before)", kit, chrome, _merge(base, n))

def wrap(sid, topic, title, items, nxt, n=None):
    """Day wrap-up: items = [(label, heading, text)]. The label shows exactly as the kit writes it."""
    _t(topic)
    cards = "".join(f'<div class="cd-card cd-up" style="--i:{i}"><span class="cd-k">{e(k)}</span><b>{e(a)}</b><p>{e(b)}</p></div>' for i, (k, a, b) in enumerate(items))
    inner = head("Today · wrap-up", title) + f'\n  <div class="cd-cards cd-cols-{min(4, len(items))} wk-cards">{cards}</div>\n  ' + key(f"Next → {e(nxt)}")
    base = {"do": "Ask two people what they will use first at work.", "silent": "say what you will use yourself first."}
    return _slide(section("cd-slide--stage", inner, "Wrap-up", sid=sid), sid, "wrap", "Wrap-up", topic, "Day wrap-up",
                  [title, nxt] + [str(x) for it in items for x in it], ["Today", "wrap-up", "Next"], _merge(base, n))

def timer_slide(sid, topic, tag, title, lead, mins, n=None):
    _t(topic)
    inner = (f'  {eyebrow(e(tag), rule=True)}\n  <h2 class="cd-h1 wk-rule">{hl(title)}</h2>\n  <p class="cd-lede wk-lead">{lead}</p>\n'
             f'  <div class="wk-map-timer"><span class="cd-chip">Time</span>{timer(mins)}</div>')
    return _slide(section("cd-slide--stage wk-statement", inner, title, sid=sid, dur=mins * 60), sid, "timer", title, topic, title, [tag, title, lead], TIMER_WORDS, _merge({"time": f"{mins} min"}, n))

# ------------------------------------------------------------------ opening and close
def lockup(kind):
    """The CODED wordmark, and the client logo beside it at the same height (a round seal may be larger: CLIENT["logo_scale"])."""
    c = ""
    if wk.CLIENT and wk.CLIENT_LOGO:
        sc = wk.CLIENT.get("logo_scale", 1.0)
        c = (f'<span class="wk-x" aria-hidden="true">×</span><img src="data:image/png;base64,{wk.b64(wk.CLIENT_LOGO)}" alt="{e(wk.CLIENT["name"])}" style="height:calc(var(--lh,26px)*{sc})">')
    return f'<div class="wk-lockup wk-lockup--{kind}"><svg class="cd-logo" role="img" aria-label="CODED"><use href="#coded-wordmark"/></svg>{c}</div>'

def cover(day):
    _t("open")
    D_ = C.DAYS[day]
    inner = (f'  <div>\n    <div class="cd-brandline"><span>{ic("i-hub")}{e(wk.BRAND)} · Kuwait</span><span>{ic("i-cal")}Day {day} of {wk.NDAYS} · {e(C.DAYDATE[day])} · {e(C.HOURS)}</span></div>\n'
             f'    <h1 class="cd-display wk-cover-h">{e(C.TITLE)}</h1>\n    <p class="wk-cover-day"><span>Day {day} ·</span> <em>{e(D_["title"])}</em></p>\n'
             f'    <p class="cd-lede cd-sub">{e(D_["sub"])}</p>\n    <div class="wk-standby"><span class="wk-pdot"></span>We start shortly</div>\n'
             f'    <div class="cd-foot">{e(C.VENUE)} · Press → to begin</div>\n  </div>\n'
             f'  <div class="wk-cover-side">{lockup("cover")}</div>')
    n = getattr(KB(), "COVER_NOTES", {}).get(day)
    return _slide(section("cd-slide--cover", inner, "Cover", sid=f"cover{day}"), f"cover{day}", "cover", "Cover", "open", "Cover: welcome",
                  [wk.BRAND, C.DAYDATE[day], C.HOURS, C.TITLE, D_["title"], D_["sub"], C.VENUE, "Kuwait"],
                  ["Day", "of", "We start shortly", "Press → to begin", "Kuwait", "×"], _merge({"time": f"{D_['blocks'][0][0][:5]} · cover"}, n))

def outcomes(day):
    _t("open")
    D_ = C.DAYS[day]
    li = "".join(f'<li class="cd-up" style="--i:{i}">{ic("i-check")}<span>{x}</span></li>' for i, x in enumerate(D_["outcomes"]))
    inner = head("Outcomes for today", f'By the end of Day {day}, <span class="hl">you will be able to:</span>') + f'\n  <ul class="wk-checks wk-checks--big">{li}</ul>'
    n = getattr(KB(), "OUTCOMES_NOTES", {}).get(day)
    base = {"do": "Read the outcomes. Ask which one matters most for their own job.", "silent": "ask one person to pick one and say why."}
    return _slide(section("cd-slide--stage", inner, "Outcomes", sid=f"outcomes{day}"), f"outcomes{day}", "outcomes", "Outcomes", "open", "Outcomes",
                  list(D_["outcomes"]), ["Outcomes for today", "By the end of Day", "you will be able to:"], _merge(base, n))

def road(day):
    _t("open")
    D_ = C.DAYS[day]
    R = getattr(KB(), "ROAD", {}).get(day, {})
    rt = R.get("title", f"Day {day}: <span class=\"hl\">{e(D_['title'])}.</span>")
    lede = R.get("lede", C.STORY)
    blocks = [(t, nm, d) for t, nm, d in D_["blocks"] if d]
    ag = "".join(f'<div class="cd-up" style="--i:{i}"><span class="cd-n">{t[:5]}</span><b>{e(nm)}<small>{e(d)}</small></b><span class="cd-dur">{t}</span></div>' for i, (t, nm, d) in enumerate(blocks))
    rail = (f'  <div class="cd-rail">\n    {eyebrow("The shape of Day " + str(day), rule=True)}\n    <h2 class="cd-h2">{hl(rt)}</h2>\n'
            f'    <p class="cd-lede">{e(lede)}</p>\n  </div>\n  <div class="cd-agenda wk-agenda">{ag}</div>')
    base = {"do": "Point to the blocks and the breaks on the map.", "silent": "ask which block they expect to be hardest."}
    return _slide(section("cd-slide--split wk-roadmap", rail, "Today's map", sid=f"road{day}"), f"road{day}", "road", "Today's map", "open", f"Road: the shape of Day {day}",
                  [rt, lede] + [x for b in blocks for x in b], ["The shape of Day"], _merge(base, R.get("n")))

def opening(day, opener=()):
    """cover -> pre-MAP slide (the first day) -> the opener (if any) -> outcomes -> today's map (build.md H3 order)."""
    s = [cover(day)]
    if "pre" in wk.FORM_DAY.get(day, []): s.append(mapslide(f"map{day}", "open", "before"))
    s += list(opener)
    s += [outcomes(day), road(day)]
    return s

def close_slide(day):
    _t("close")
    CL = getattr(KB(), "CLOSE", {}).get(day, {})
    big = CL.get("big", "Thank you.")
    nxt = CL.get("next", "")
    inner = (f'  <span class="cd-hint">Day {day} · close</span>\n  <h1 class="cd-h1">{hl(big)}</h1>\n  {key(e(nxt)) if nxt else ""}\n  {lockup("close")}')
    h = section("cd-slide--end wk-close", '<div class="cd-ghost-word" aria-hidden="true">END</div>' + inner, "Close", sid=f"close{day}")
    h = h.replace(' <div class="cd-wrap">\n<div class="cd-ghost-word" aria-hidden="true">END</div>', ' <div class="cd-ghost-word" aria-hidden="true">END</div>\n <div class="cd-wrap">\n')
    base = {"time": "last 5 min", "do": "Recap the day in one line."}
    return _slide(h, f"close{day}", "close", "Close", "close", "Close", [big, nxt], ["Day", "close", "×"], _merge(base, CL.get("n")))

# ------------------------------------------------------------------ deck CSS: kit + workshop pieces, CODED tokens, then the client mix
CLIENT_BLOCK = """html[data-course][data-client="wk"]{
  --wk-royal:#004AA3; --wk-blue:#2F74D6; --wk-soft:#6F9CE8; --wk-light:#9FC0F5; --wk-pale:#BCD3F7; --wk-ink:#00112F; --wk-amber:#E3A33B;
  --wk-copper:#2F74D6; --wk-indigo:#004AA3; --wk-mint:#004AA3; --wk-navy:#00112F;
  --cd-font-sans:'Manrope',system-ui,-apple-system,"Segoe UI",sans-serif;
  --cd-font-mono:'Space Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  --cd-font-arabic:'Manrope',system-ui,sans-serif;
  --cd-accent:#6F9CE8; --cd-accent-bright:#8FB3F0; --cd-accent-soft:#9FC0F5; --cd-accent-deep:__DEEP__;
  --cd-accent-ink:#FFFFFF; --cd-accent-dark:#004AA3; --cd-accent-page:#E3ECFB;
  --cd-faint:rgba(255,255,255,.66); --cd-muted:#B4C0D3;
  --cd-fill-live:linear-gradient(160deg,color-mix(in srgb,var(--wk-blue) 24%,transparent),color-mix(in srgb,var(--wk-blue) 6%,transparent));
  --cd-ring-live:0 0 0 4px color-mix(in srgb,var(--wk-blue) 22%,transparent);
  --cd-echo-1:color-mix(in srgb,var(--wk-blue) 12%,transparent);
  --cd-echo-2:color-mix(in srgb,var(--wk-royal) 34%,transparent);
  --panel:var(--cd-surf-2); --surf:var(--cd-surf); --w:var(--cd-w); --w8:var(--cd-text-body); --w7:var(--cd-text-body); --w6:var(--cd-text-quiet);
  --w5:var(--cd-text-quiet); --w4:var(--cd-text-faint); --w2:var(--cd-line); --w1:var(--cd-line); --w06:var(--cd-surf);
  --rose:var(--cd-accent); --rose-lt:var(--cd-accent-soft); --crimson:var(--cd-accent-deep); --maroon:var(--wk-royal);
  --mono:var(--cd-font-mono); --mf:var(--cd-font-sans);
}"""
WK_CSS = asset("deck-extra.css")

def deck_css():
    deep = wk.CLIENT["primary"] if wk.CLIENT else "#1F5FC0"
    css = asset("deck-kit", "deck-css.css").replace("/*__CLIENT_BLOCK__*/", CLIENT_BLOCK)
    css += "\n/* ===== workshop pieces ===== */\n" + WK_CSS + asset("scene.css")
    if wk.AI:
        import widgets as W
        css += "\n/* ===== widgets (prompt player, weak and strong, next word) ===== */\n" + W.css()
    css += getattr(KB(), "EXTRA_CSS", "").replace("<style>", "").replace("</style>", "")
    css = wk.theme(css).replace("__DEEP__", deep)
    return css

BRIDGE = r"""
/* ---- bridge: the widgets on the kit engine ---- */
window.wkOnSlide=[];
(function(){
  var deck=document.getElementById('deck'); if(!deck)return;
  var slides=[].slice.call(deck.querySelectorAll('.cd-slide'));
  window.next=function(){ if(window.CD_DECK) window.CD_DECK.goTo(window.CD_DECK.current+1); };
  deck.addEventListener('cd:slide',function(e){
    slides.forEach(function(s){ s.classList.toggle('active', s===e.detail.slide); });
    window.wkOnSlide.forEach(function(f){ f(e.detail.slide); });
  });
  if(window.CD_DECK){ var c=slides[window.CD_DECK.current]; if(c) c.classList.add('active'); }
})();
document.addEventListener('click',function(e){var c=e.target.closest('.wk-sc');if(!c)return;e.stopPropagation();c.classList.toggle('on');});
window.wkOnSlide.push(function(s){[].forEach.call(s.querySelectorAll('.wk-sc.on'),function(c){c.classList.remove('on');}); if(s.querySelector('#llm')&&typeof window.llmReset==='function')window.llmReset();});
"""
def behavior_js():
    js = asset("deck-kit", "wk-behavior.js") + BRIDGE
    if wk.AI:
        import widgets as W
        js += W.js() + "\n" + _LLM.get("js", "")
    js += "\n" + getattr(KB(), "EXTRA_JS", "").replace("<script>", "").replace("</script>", "")
    return js

SHELL_HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr" data-course="workshops" data-client="wk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="§DESC§">
<meta name="theme-color" content="#0c1b33">
<link rel="icon" href="§ROOT§§FAV§" type="image/png">
<title>§TITLE§</title>
<style id="cd-kit-fonts">§FONTS§</style>
<style id="cd-kit-css">§KITCSS§</style>
<style id="deck-css">§DECKCSS§</style>
</head>
<body>
<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" aria-hidden="true" id="cd-kit-sprite">§SPRITE§</svg>
§EXTRASPRITE§
<div class="cd-ground" aria-hidden="true">
  <svg id="echo" class="cd-echo" viewBox="-500 -500 1000 1000" preserveAspectRatio="xMidYMid meet">
    <circle r="60"/><circle r="120"/><circle r="185"/><circle r="255"/><circle r="330"/><circle r="410"/><circle r="495"/>
  </svg>
  <div class="cd-grain"></div>
</div>
<header class="cd-mark">
  <svg class="cd-logo" role="img" aria-label="CODED"><use href="#coded-wordmark"/></svg>
  <span class="cd-sep"></span><span class="cd-crumb">§CRUMB§</span>
  <a class="wk-back" href="§BACK§" title="Back to the Day §D§ page"><svg class="cd-ic"><use href="#i-back"/></svg>Day §D§ page</a>
</header>
<main class="cd-deck" id="deck">
"""
SHELL_TAIL = """</main>
<nav class="cd-bar" aria-label="Deck progress">
  <div class="cd-count" id="count"></div>
  <div class="cd-prog" id="prog"></div>
  <div class="cd-keys"><kbd>←</kbd><kbd>→</kbd> move · <kbd>M</kbd> menu · <kbd>B</kbd> bell · <kbd>T</kbd> timer · <kbd>C</kbd> break§NKEY§ · <kbd>F</kbd> full</div>
</nav>
<div class="cd-menu" id="menu"><div class="cd-menu-grid" id="menuGrid"></div></div>
§BREAK§
<script src="data:text/javascript;base64,§KITJS§"></script>
<script>
window.CD_DECK = CodedKit.mount(§MOUNT§);
</script>
<script>
§BEHAVIOR§
</script>
<script>addEventListener("keydown",function(e){if((e.key===" "||e.key==="Enter")&&e.target&&e.target.closest&&e.target.closest("button,input,a,.wk-w")){e.stopPropagation();}},true);</script>
</body>
</html>
"""

def build(day, trainer):
    """One deck. trainer=True keeps the notes (N) and the slide timings; the public copy drops both. Returns (html, records)."""
    STATE["day"] = day; _LLM.clear()
    kb = KB()
    sl = list(kb.DAYFN[day]()) + [close_slide(day)]
    for i, s in enumerate(sl):
        if not isinstance(s, Slide): raise SystemExit(f"day {day} item {i + 1} is not a slide made by a deck helper")
    ids = [s.rec["id"] for s in sl]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup: raise SystemExit(f"day {day}: slide ids used twice: {dup}")
    secmap = {}
    for i, (_n, _g, tps) in enumerate(sections(day)):
        for t in tps: secmap[t] = i
    out, recs = [], []
    for i, s in enumerate(sl):
        r = s.rec
        if r["topic"] not in secmap: raise SystemExit(f"day {day} slide {r['id']}: topic {r['topic']!r} is in no section (build_deck.py SECTIONS or TOPICS)")
        h = str(s).replace("§SEC§", str(secmap[r["topic"]]), 1).replace("§LBL§", f"{i + 1:02d}", 1)
        flat = flat_note(r["note"])
        h = h.replace("§NOTE§", e(flat), 1) if trainer else h.replace(' data-notes="§NOTE§"', "", 1)
        if not trainer: h = re.sub(r' data-dur="\d+"', "", h, count=1)
        out.append(h); recs.append(dict(r, n=i + 1, flat=flat))
    steps, _lit = flow(day)
    mount = {"sections": [{"n": n, "g": g} for n, g, _t2 in sections(day)],
             "flows": {"day": {"steps": steps, "stages": {f"s{k + 1}": [k] for k in range(len(steps))}}}}
    root = "../" if trainer else ""
    T = C.DAYS[day]["title"]
    hd = (SHELL_HEAD.replace("§DESC§", e(f"Day {day} · {T}. Slides for {C.TITLE}, a {wk.ORG} workshop."))
          .replace("§ROOT§", root).replace("§FAV§", P("favicon.png"))
          .replace("§TITLE§", e(f"Day {day} · {T} · {C.TITLE} · {wk.ORG}" + (" · trainer copy" if trainer else "")))
          .replace("§FONTS§", wk.font_css_embedded()).replace("§KITCSS§", asset("deck-kit", "cd-kit-css.css"))
          .replace("§DECKCSS§", deck_css()).replace("§SPRITE§", asset("deck-kit", "sprite-inner.svg"))
          .replace("§EXTRASPRITE§", asset("deck-kit", "extra-sprite.svg"))
          .replace("§CRUMB§", e(f"{wk.BRAND} · {C.TITLE} · Day {day} of {wk.NDAYS}"))
          .replace("§BACK§", root + wk.dayp(day) + ".html").replace("§D§", str(day)))
    tail = (SHELL_TAIL.replace("§NKEY§", " · <kbd>N</kbd> notes" if trainer else "")
            .replace("§BREAK§", asset("deck-kit", "break.html"))
            .replace("§KITJS§", base64.b64encode(asset("deck-kit", "coded-deck.js").encode()).decode())
            .replace("§MOUNT§", json.dumps(mount)).replace("§BEHAVIOR§", behavior_js()))
    h = wk.text_rules(hd + "".join(out) + tail)
    if not trainer:
        h = h.replace("</body>", "<script>(function(){var n=document.getElementById('notes');if(n)n.remove();addEventListener('keydown',function(e){if(e.key==='n'||e.key==='N'){e.stopImmediatePropagation();}},true);})();</script>\n</body>", 1)
    return h, recs

def all_records():
    """Every day's slide records (the staff pages and the validator read the same list)."""
    return {d: build(d, True)[1] for d in wk.DAYS}

def main(argv):
    out = argv[1] if len(argv) > 1 else os.path.join(wk.ROOT, "public")
    os.makedirs(os.path.join(out, wk.STAFF), exist_ok=True); os.makedirs(wk.RECORD_DIR, exist_ok=True)
    for d in wk.DAYS:
        for trainer in (False, True):
            h, recs = build(d, trainer)
            p = os.path.join(out, wk.STAFF, wk.deckp(d) + ".html") if trainer else os.path.join(out, wk.deckp(d) + ".html")
            open(p, "w", encoding="utf-8").write(h)
        json.dump([{k: r[k] for k in ("n", "id", "kind", "title", "topic", "kit", "chrome")} for r in recs], open(os.path.join(wk.RECORD_DIR, f"slides-day-{d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        json.dump([dict(r["note"], flat=r["flat"]) for r in recs], open(os.path.join(wk.RECORD_DIR, f"presenter-notes-day-{d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print("deck", d, len(recs), "slides", len(h) // 1024, "KB")

if __name__ == "__main__":
    import deck as _deck          # the kit imports "deck": run the same module object, not __main__
    _deck.main(sys.argv)
