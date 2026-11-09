# -*- coding: utf-8 -*-
"""The AI branch's in-slide widgets: the prompt player (one prompt part per press), the weak and strong opener and the
next-word widget. Each returns slide-body markup; deck.py wraps it in a slide. CSS uses the deck tokens only (CODED blues,
no gold), so the client mix applies. JS lives in assets/widgets/ and binds to every widget of its kind on the deck."""
import json
from wk import e, asset

SPARK = '<svg class="icn" viewBox="0 0 24 24"><path d="M12 3l2.5 5.5L20 11l-5.5 2.5L12 19l-2.5-5.5L4 11l5.5-2.5z"/></svg>'
SEND = '<svg class="icn" viewBox="0 0 24 24"><path d="M4 12l16-8-6 16-3-7z"/></svg>'
CLIP = '<svg class="pp-clip" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11l-8.5 8.5a5 5 0 01-7-7L14 4a3.5 3.5 0 015 5l-8.5 8.5a2 2 0 01-3-3L15 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
KIND = {'docx': ('W', 'Word', '#1F64B4'), 'xlsx': ('X', 'Excel', '#17744A'), 'pptx': ('P', 'PowerPoint', '#C4471F'), 'pdf': ('PDF', 'PDF', '#C8303A'),
        'csv': ('CSV', 'CSV', '#17744A'), 'eml': ('@', 'Email', '#2F74D6'), 'txt': ('T', 'Text', '#3B5478')}
def kind(f): return KIND.get(f.rsplit('.', 1)[-1].lower(), ('F', 'File', '#3B5478'))
def att(f, cls="pp"):
    ic, kd, col = kind(f)
    return (f'<span class="{cls}-att" style="--fc:{col}"><span class="{cls}-ic">{ic}</span>'
            f'<span class="{cls}-fn"><b>{e(f)}</b><i>{kd} file · attached</i></span></span>')

# ------------------------------------------------------------------ prompt player
def player(d, tool):
    """d: a kit demo with d["player"] = {parts, table, best, reco, control}. Returns (body, kit strings shown)."""
    P = d["player"]; files = d["files"]
    steps = [p[0] for p in P["parts"]] + ["Send", "Result", "Decision"]
    stepper = ''.join(f'<li data-s="{i+1}"><span class="pp-n">{i+1}</span>{e(t)}</li>' for i, t in enumerate(steps))
    segs = ''.join(f'<span class="pp-seg" data-k="{i}"><span class="pp-tag">{e(k)}</span><span class="pp-txt" data-full="{e(v)}"></span></span>' for i, (k, v) in enumerate(P["parts"]))
    bc = P.get("best", -1)
    th = ''.join(f'<th class="{"best" if j == bc else ""}">{c}</th>' for j, c in enumerate(P["table"][0]))
    rows = ''.join('<tr class="pp-row">' + ''.join(f'<td class="{"best" if j == bc else ""}">{c}</td>' for j, c in enumerate(r)) + '</tr>' for r in P["table"][1:])
    reco = ''.join(f'<li>{x}</li>' for x in P["reco"])
    nf = len(files)
    fl = (f'<div class="pp-flbl">{CLIP} {nf} file{"s" if nf != 1 else ""} attached</div><div class="pp-files">{"".join(att(f) for f in files)}</div>' if nf else '<div class="pp-files"></div>')
    body = f'''<div class="pp-top"><div><div class="cd-eyebrow">{e(d["card"])} · Prompt playback</div><span class="cd-chip wk-tool">{e(tool)} · Example · typical result</span>
<h2 class="cd-h2">{e(d["title"])}</h2></div></div>
<div class="pp">
 <div class="pp-win">
  <div class="chat-bar"><div class="chat-av">{SPARK}</div><div><div class="chat-who">{e(tool)}</div><div class="chat-sub">the perfect run · fictional data</div></div></div>
  <div class="pp-body">
   <div class="pp-empty" data-r="empty">Press <kbd>→</kbd> to build the prompt, one part at a time.</div>
   <div class="pp-sent" data-r="sent"></div>
   <div class="pp-think" data-r="think"><span></span><span></span><span></span></div>
   <div class="pp-ans" data-r="ans">
     <div class="pp-tw"><table class="pp-table"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>
     <ul class="pp-reco" data-r="reco">{reco}</ul>
   </div>
  </div>
  <div class="pp-compose" data-r="compose">
   {fl}
   <div class="pp-box"><div class="pp-ph">Message {e(tool)}</div><div class="pp-prompt" data-r="prompt">{segs}<span class="pp-caret"></span></div>
   <button class="pp-send" data-r="send" type="button" aria-label="Send">{SEND}</button></div>
  </div>
 </div>
 <aside class="pp-side">
  <div class="pp-lbl">The formula</div>
  <ol class="pp-steps" data-r="steps">{stepper}</ol>
  <div class="pp-decide" data-r="decide"><span class="pp-tag ok">Decision</span><div>{e(P["control"])}</div></div>
  <div class="pp-ctrl">
   <button class="pp-btn" data-r="back" type="button">‹ Back</button><button class="pp-btn" data-r="replay" type="button">↺ Replay</button><button class="pp-btn pri" data-r="next" type="button">Next ›</button>
  </div>
  <div class="pp-keys"><kbd>→</kbd> <kbd>Space</kbd> <kbd>Enter</kbd> next step · <kbd>←</kbd> back · <kbd>R</kbd> replay</div>
 </aside>
</div>
<p class="wk-src">Playback of the ideal run. The live tool may word it differently. All figures are fictional training data.</p>'''
    kit = [d["card"], d["title"], tool, P["control"]] + [x for p in P["parts"] for x in p] + [c for r in P["table"] for c in r] + list(P["reco"]) + files
    return body, kit

# ------------------------------------------------------------------ weak and strong opener
def showcase(W):
    ic, _k, col = kind(W["file"])
    a = f'<span class="ws-att" style="--fc:{col}"><span class="ws-ic">{ic}</span><b>{e(W["file"])}</b></span>'
    segs = ''.join(f'<span class="ws-seg" data-k="{i}"><span class="ws-tag">{e(k)}</span><span class="ws-txt" data-full="{e(v)}"></span></span>' for i, (k, v) in enumerate(W["parts"]))
    weak_ans = ''.join(f'<p>{e(p)}</p>' for p in W["weak_answer"])
    th = ''.join(f'<th>{c}</th>' for c in W["table"][0])
    rows = ''.join('<tr class="ws-row">' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in W["table"][1:])
    strong_ans = ''.join(f'<li class="ws-li">{x}</li>' for x in W["strong_answer"])
    wflags = ''.join(f'<span class="ws-flag bad">✗ {e(x)}</span>' for x in W["weak_flags"])
    sflags = ''.join(f'<span class="ws-flag good">✓ {e(x)}</span>' for x in W["strong_flags"])
    score = ''.join(f'<div class="ws-sk">{a_}</div><div class="ws-sw">{b}</div><div class="ws-ss">{c}</div>' for a_, b, c in W["score"])
    STEPS = ["Same file", "Weak prompt", "Weak result"] + [p[0] for p in W["parts"]] + ["Strong result", "Compare", "The lesson"]
    dots = ''.join(f'<li data-s="{i}"><span>{i+1}</span><em>{e(t)}</em></li>' for i, t in enumerate(STEPS))
    tool = W["tool"]
    def chat(side, label, prompt_html, body_html):
        return f'''<div class="ws-win {side}" data-r="{side}">
  <div class="ws-head"><span class="ws-lbl {side}">{label}</span><div class="chat-av">{SPARK}</div><div class="chat-who">{e(tool)}</div></div>
  <div class="ws-body"><div class="ws-sent" data-r="{side}-sent"></div><div class="ws-think" data-r="{side}-think"><span></span><span></span><span></span></div><div class="ws-ans" data-r="{side}-ans">{body_html}</div></div>
  <div class="ws-flags" data-r="{side}-flags">{wflags if side == "weak" else sflags}</div>
  <div class="ws-compose" data-r="{side}-compose"><div class="ws-files">{a}</div>
    <div class="ws-box" data-ph="Message {e(tool)}"><div class="ws-prompt" data-r="{side}-prompt">{prompt_html}<span class="ws-caret"></span></div><button class="ws-send" data-r="{side}-send" type="button" aria-label="Send the {side} prompt">{SEND}</button></div></div>
</div>'''
    weak_win = chat("weak", "Weak prompt", f'<span class="ws-weaktxt" data-full="{e(W["weak"])}"></span>', f'<div class="ws-wall">{weak_ans}<div class="ws-fade"></div></div>')
    strong_win = chat("strong", "Strong prompt", segs, f'<div class="ws-tw"><table class="ws-table"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div><ul class="ws-ul">{strong_ans}</ul>')
    body = f'''<div class="ws-top"><div><div class="cd-eyebrow">{W["eyebrow"]}</div><h2 class="cd-h2">{W["title"]}</h2></div><ol class="ws-steps" data-r="steps">{dots}</ol></div>
<div class="ws-grid">{weak_win}{strong_win}<div class="ws-score" data-r="score"><div class="ws-sk h"></div><div class="ws-sw h">Weak</div><div class="ws-ss h">Strong</div>{score}</div></div>
<div class="ws-punch" data-r="punch"><div class="ws-pt">{W["punch"]}</div><div class="ws-ps">{W["punch_sub"]}</div></div>
<div class="ws-foot"><span class="ws-keys"><kbd>→</kbd> <kbd>Space</kbd> <kbd>Enter</kbd> next · <kbd>←</kbd> back · <kbd>R</kbd> replay</span><span class="wk-src">Example · typical result. Fictional training data from {e(W["file"])}.</span></div>'''
    kit = [W["eyebrow"], W["title"], W["file"], W["weak"], tool, W["punch"], W["punch_sub"]] + list(W["weak_answer"]) + list(W["weak_flags"]) + \
        [x for p in W["parts"] for x in p] + [c for r in W["table"] for c in r] + list(W["strong_answer"]) + list(W["strong_flags"]) + [c for r in W["score"] for c in r]
    return body, kit

# ------------------------------------------------------------------ next-word widget (illustrative probabilities from the kit)
LLM_CSS = """
.wk-w .llm{margin-top:6px;max-width:1060px;width:100%;flex:none;background:var(--panel);border:1px solid var(--w1);border-radius:15px;padding:16px 20px;box-shadow:0 18px 50px rgba(0,0,0,.4)}
.llm-sent{font-size:clamp(20px,2.1vw,28px);font-weight:700;line-height:1.35;letter-spacing:-.4px;min-height:1.4em}
.llm-sent .pr{color:var(--w8)}
.llm-sent .tk{color:var(--rose-lt);border-bottom:2px solid var(--crimson);padding:0 2px;margin-left:6px}
.llm-sent .cur{display:inline-block;width:12px;height:1.05em;margin-left:6px;vertical-align:-3px;background:var(--rose);animation:llmblink 1s steps(1) infinite}
@keyframes llmblink{50%{opacity:0}}
.llm-q{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--w6);margin:12px 0 8px}
.llm-opts{display:flex;flex-direction:column;gap:5px}
.llm-row{display:grid;grid-template-columns:minmax(120px,210px) 1fr 58px;align-items:center;gap:12px;background:none;border:1px solid transparent;border-radius:9px;padding:3px 8px;cursor:pointer;font-family:inherit;color:var(--w8);text-align:left}
.llm-row:hover,.llm-row:focus-visible{border-color:var(--rose);outline:none}
.llm-row .w{font-size:16px;font-weight:700}
.llm-row .bar{height:14px;border-radius:7px;background:var(--w06);overflow:hidden}
.llm-row .bar i{display:block;height:100%;border-radius:7px;background:linear-gradient(90deg,var(--maroon),var(--crimson),var(--rose));transition:width .35s cubic-bezier(.2,.7,.2,1)}
.llm-row .pc{font-family:var(--mono);font-size:13px;color:var(--rose-lt);text-align:right;font-variant-numeric:tabular-nums}
.llm-row.low .w{color:var(--w6)}
.llm-ctrl{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;margin-top:12px;padding-top:10px;border-top:1px solid var(--w1)}
.llm-ctrl label{font-family:var(--mono);font-size:11px;color:var(--w7);display:flex;align-items:center;gap:10px}
.llm-ctrl input[type=range]{width:170px;accent-color:var(--crimson)}
.llm-ctrl .tv{color:var(--rose-lt);min-width:84px}
.llm-btn{font-family:inherit;font-size:13px;font-weight:700;color:#fff;background:var(--maroon);border:none;border-radius:9px;padding:8px 13px;cursor:pointer}
.llm-btn.ghost{background:var(--w06);border:1px solid var(--w1);color:var(--w8)}
.llm-btn[disabled]{opacity:.45;cursor:default}
.llm-note{font-size:13.5px;color:var(--w7);margin-top:8px;min-height:1.3em}
.llm-note b{color:var(--rose-lt)}
.llm-foot{font-family:var(--mono);font-size:11px;color:var(--w6);margin-top:6px}
"""
def llm(cfg):
    """cfg: the kit's LLM = {"tree": {...}, "foot": "..."}. Returns (body, kit strings, js)."""
    tree = cfg["tree"]; foot = cfg.get("foot", "Percentages are illustrative.")
    body = f'''<div class="llm" id="llm">
  <div class="llm-sent" id="llm-sent"></div>
  <div class="llm-q" id="llm-q">What word comes next? Click one.</div>
  <div class="llm-opts" id="llm-opts"></div>
  <div class="llm-ctrl">
    <label for="llm-temp">Temperature <input type="range" id="llm-temp" min="0.2" max="2" step="0.1" value="1"><span class="tv" id="llm-tv">1.0 · balanced</span></label>
    <button class="llm-btn" id="llm-top" type="button">Pick the top word</button>
    <button class="llm-btn ghost" id="llm-auto" type="button">Let the AI choose</button>
    <button class="llm-btn ghost" id="llm-reset" type="button">Start again</button>
  </div>
  <div class="llm-note" id="llm-note"></div>
  <div class="llm-foot">{e(foot)}</div>
</div>'''
    js = asset("widgets", "llm.js").replace("__TREE__", json.dumps(tree))
    return body, [tree["start"]["prompt"], foot], js

def css():
    return asset("widgets", "pp.css") + asset("widgets", "ws.css") + LLM_CSS
def js():
    return asset("widgets", "pp.js") + "\n" + asset("widgets", "ws.js")
