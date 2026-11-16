# -*- coding: utf-8 -*-
"""The slides of AI Innovation and Automation (CODED × RSM Albazie), day by day. The engine's deck.py renders every call.
One helper call is one slide. Every note is written as N(...) parts and never repeats the slide text. The engine adds the close slide."""
from deck import *
import content as C
import content_demos as CD
from content_demos import DEMOS
import data as D
from data import num
from deck import _slide, _merge, _t
import notes_day1
import notes_day2

# ------------------------------------------------------------------ kit-only slide helpers (the engine is never edited)
def askslide(sid, topic, tag, q, ph, take, n=None):
    """A question with a search bar. The trainer types the room's answers; each one shows as a chip on the screen.
    Nothing is saved or sent: the answers live in the page until it reloads."""
    _t(topic)
    bar = (f'<form class="wai-bar" autocomplete="off" role="search"><svg class="wai-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.4 15.4 21 21"/></svg>'
           f'<input class="wai-in" type="text" maxlength="60" spellcheck="false" placeholder="{e(ph)}" aria-label="{e(ph)}"><button class="wai-go" type="submit">Add</button></form>')
    inner = (f'  <div class="wai">\n   {eyebrow(e(tag), rule=True)}\n   <h1 class="cd-h1 wai-q">{hl(q)}</h1>\n   {bar}\n'
             f'   <div class="wai-out" aria-live="polite"></div>\n   <div class="wai-foot"><button class="wai-clear" type="button">Clear</button></div>\n  </div>\n  ' + key(take))
    return _slide(section("cd-slide--stage wai-slide", inner, strip(q), sid=sid), sid, "ask", q, topic, q, [tag, q, take], ["Add", "Clear"], _merge({}, n))

def livedemo(sid, topic, did, n=None, time="4 min", badge="Live in Claude", app="Claude"):
    """A demo the trainer runs live (in Claude, or on the lab page or in n8n). The slide is a holding card: what you will see, what to watch for, the files.
    The prompt is on the prompt sheet; the expected result and a fallback are in the notes and on the staff backup page."""
    _t(topic)
    d = CD.DEMOS[did]
    words = d["title"].split()
    title = (" ".join(words[:-2]) + f' <span class="hl">{" ".join(words[-2:])}.</span>').strip()
    tag = f"Demo {d['skill']} · {d['tool']}"
    files = files_html(d["files"]) if d["files"] else '<p class="lv-none">Nothing to attach.</p>'
    inner = (f'  <div class="lv">\n   <div class="lv-top">{eyebrow(e(tag), rule=True)}<span class="lv-badge"><i></i>{e(badge)}</span></div>\n'
             f'   <h2 class="cd-h1 lv-h">{hl(title)}</h2>\n'
             f'   <div class="lv-row"><div class="lv-card"><span class="lv-k">Watch for</span><p>{e(d["hint"])}</p></div>'
             f'<div class="lv-card"><span class="lv-k">Files</span>{files}<p class="lv-src">Prompt: the prompt sheet, Demo {d["skill"]}</p></div></div>\n  </div>\n  ' + key(d["point"]))
    steps = [x.replace("[T] ", "") for x in d.get("setup", [])]
    base = {"time": time, "do": f"Switch to {app} and run it live. " + " ".join(steps), "expect": d["expected"], "say": d["say"],
            "fallback": (d.get("fallback") or "") + " The expected result is on the staff backup page, Demo " + d["skill"] + ".",
            "more": ["Copy the prompt from the prompt sheet, Demo " + d["skill"] + ". The live answer may use other words; point at what the Watch for line asks."]}
    kit = [tag, title, d["hint"], d["point"], "Demo " + d["skill"]] + list(d["files"])
    chrome = [badge, "Watch for", "Files", "Nothing to attach.", "Prompt: the prompt sheet,", "Prompt", "the prompt sheet"]
    lab = badge[0].lower() + badge[1:]
    return _slide(section("cd-slide--stage lv-slide", inner, f"Demo {d['skill']} · {lab}", sid=sid, dur=240), sid, "live",
                  f"Demo {d['skill']} · {lab}", topic, f"Demo {d['skill']} {lab}: {d['title']}", kit, chrome, _merge(base, n))

def relabel(sl, old, new, old_h, new_h):
    """The same slide with another menu label (the engine names the weak and strong demo after the opener)."""
    out = Slide(str(sl).replace(old, new))
    out.rec = dict(sl.rec, title=sl.rec["title"].replace(old, new))
    out.rec["note"] = dict(sl.rec["note"], h=sl.rec["note"]["h"].replace(old_h, new_h))
    return out

EXTRA_CSS = """
#notes{max-height:46vh;overflow:auto}
#notes p{font-size:17px;line-height:1.6}
.lv-slide .cd-wrap{justify-content:center}
.lv{display:flex;flex-direction:column;gap:clamp(16px,2.4vh,28px);width:100%}
.lv-top{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.lv-top .cd-eyebrow{margin:0}
.lv-badge{display:inline-flex;align-items:center;gap:10px;padding:8px 16px;border-radius:999px;font:700 15px/1 var(--cd-font-mono);letter-spacing:.12em;text-transform:uppercase;
  color:#fff;background:rgba(214,48,49,.18);border:1px solid rgba(255,120,120,.55)}
.lv-badge i{width:11px;height:11px;border-radius:50%;background:#FF5A5A;box-shadow:0 0 0 0 rgba(255,90,90,.7);animation:lvp 1.6s infinite}
@keyframes lvp{0%{box-shadow:0 0 0 0 rgba(255,90,90,.7)}70%{box-shadow:0 0 0 12px rgba(255,90,90,0)}100%{box-shadow:0 0 0 0 rgba(255,90,90,0)}}
.lv-h{margin:0;font-size:clamp(44px,5.2vw,80px);line-height:1.04}
.lv-row{display:grid;grid-template-columns:1.1fr 1fr;gap:20px}
.lv-card{border-radius:18px;padding:22px 26px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);display:flex;flex-direction:column;gap:12px}
.lv-k{font:700 13px/1 var(--cd-font-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--cd-accent)}
.lv-card p{margin:0;font-size:clamp(20px,1.7vw,26px);line-height:1.35}
.lv-card .wk-files{display:flex;flex-wrap:wrap;gap:8px}
.lv-card p.lv-none,.lv-card p.lv-src{font-size:16px;color:var(--cd-text-quiet,#B4C0D3)}
@media (prefers-reduced-motion: reduce){.lv-badge i{animation:none}}
.wai-slide .cd-wrap{justify-content:center}
.wai{display:flex;flex-direction:column;align-items:center;text-align:center;gap:clamp(14px,2.2vh,24px);width:100%;max-width:1080px;margin:0 auto}
.wai .cd-eyebrow{justify-content:center}
.wai-q{margin:0;font-size:clamp(56px,7.4vw,112px);line-height:1}
.wai-bar{display:flex;align-items:center;gap:14px;width:min(860px,92%);padding:10px 10px 10px 26px;border-radius:999px;
  background:rgba(255,255,255,.96);box-shadow:0 22px 60px -24px rgba(0,0,0,.85),0 0 0 1px rgba(255,255,255,.22);transition:box-shadow .2s}
.wai-bar:focus-within{box-shadow:0 22px 60px -24px rgba(0,0,0,.85),0 0 0 5px color-mix(in srgb,var(--cd-accent) 55%,transparent)}
.wai-ic{width:30px;height:30px;flex:none;fill:none;stroke:#3C4A60;stroke-width:2.4;stroke-linecap:round}
.wai-in{flex:1;min-width:0;border:0;outline:0;background:transparent;font:600 clamp(20px,1.9vw,28px)/1.2 var(--cd-font-sans);color:#0C1B33;padding:10px 0}
.wai-in::placeholder{color:#5B677A;font-weight:500}
.wai-go{flex:none;border:0;border-radius:999px;padding:14px 26px;font:700 18px/1 var(--cd-font-sans);color:#fff;background:#007DB4;cursor:pointer}
.wai-go:hover,.wai-go:focus-visible{background:#00699A;outline:none}
.wai-out{display:flex;flex-wrap:wrap;justify-content:center;align-content:flex-start;gap:12px;width:100%;min-height:clamp(120px,20vh,220px);max-height:34vh;overflow:hidden}
.wai-chip{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:12px 22px;cursor:pointer;
  font:600 clamp(20px,1.8vw,27px)/1.15 var(--cd-font-sans);color:var(--cd-text-strong,#fff);
  background:color-mix(in srgb,var(--cd-accent) 22%,rgba(255,255,255,.06));border:1px solid color-mix(in srgb,var(--cd-accent) 60%,transparent)}
.wai-chip:hover{border-color:#fff}
.wai-chip b{font:700 .8em/1 var(--cd-font-mono);color:var(--cd-accent-soft,#9FC0F5)}
.wai-chip b:empty{display:none}
.wai-out.wai-many .wai-chip{font-size:clamp(17px,1.4vw,21px);padding:9px 16px}
.wai-out.wai-lots .wai-chip{font-size:clamp(14px,1.1vw,17px);padding:7px 13px}
.wai-pop{animation:waipop .45s cubic-bezier(.2,1.4,.4,1)}
@keyframes waipop{from{transform:scale(.6);opacity:0}to{transform:none;opacity:1}}
.wai-foot{min-height:30px}
.wai-clear{border:1px solid rgba(255,255,255,.28);background:transparent;color:var(--cd-text-quiet,#B4C0D3);border-radius:999px;padding:7px 18px;font:600 14px/1 var(--cd-font-sans);cursor:pointer}
.wai-clear:hover{color:#fff;border-color:#fff}
.wai-out:empty + .wai-foot .wai-clear{visibility:hidden}
@media (prefers-reduced-motion: reduce){.wai-pop{animation:none}}
"""

EXTRA_JS = r"""
(function(){
  [].forEach.call(document.querySelectorAll('.wai'), function(w){
    var f = w.querySelector('.wai-bar'), inp = w.querySelector('.wai-in'), out = w.querySelector('.wai-out'), clr = w.querySelector('.wai-clear');
    var seen = {};
    function size(){ var n = out.children.length; out.classList.toggle('wai-many', n > 8); out.classList.toggle('wai-lots', n > 16); }
    function pop(c){ c.classList.remove('wai-pop'); void c.offsetWidth; c.classList.add('wai-pop'); }
    f.addEventListener('submit', function(ev){
      ev.preventDefault();
      var t = (inp.value || '').replace(/\s+/g, ' ').trim(); if (!t) return;
      var k = t.toLowerCase(), c = seen[k];
      if (c) { var n = (+c.getAttribute('data-n') || 1) + 1; c.setAttribute('data-n', n); c.querySelector('b').textContent = '×' + n; pop(c); }
      else {
        c = document.createElement('button'); c.type = 'button'; c.className = 'wai-chip'; c.setAttribute('data-n', '1'); c.title = 'Click to remove';
        var sp = document.createElement('span'); sp.textContent = t; c.appendChild(sp); c.appendChild(document.createElement('b'));
        c.addEventListener('click', function(){ delete seen[k]; c.remove(); size(); });
        out.appendChild(c); seen[k] = c; pop(c);
      }
      inp.value = ''; inp.focus(); size();
    });
    inp.addEventListener('keydown', function(ev){
      var D = window.CD_DECK, empty = !inp.value;
      if (ev.key === 'Escape') { inp.blur(); return; }
      if (!D) return;
      if (ev.key === 'PageDown' || (empty && ev.key === 'ArrowRight')) { ev.preventDefault(); inp.blur(); D.goTo(D.current + 1); }
      else if (ev.key === 'PageUp' || (empty && ev.key === 'ArrowLeft')) { ev.preventDefault(); inp.blur(); D.goTo(D.current - 1); }
    });
    clr.addEventListener('click', function(){ out.innerHTML = ''; seen = {}; size(); inp.focus(); });
  });
})();
"""

SECTIONS = {
 1: [("Opening", "g-mark", ["open"]), ("AI foundations", "g-code", ["b1"]), ("Find the work", "g-frame", ["b2", "b3"]), ("Build", "g-impact", ["b4", "b5"]), ("Close", "g-progress", ["b7", "close"])],
 2: [("Finish the build", "g-mark", ["open", "o2", "p2"]), ("System", "g-code", ["c1", "c2"]), ("Inputs and rules", "g-frame", ["c3", "c4"]), ("Demo Day", "g-impact", ["c5", "c6"]), ("Close", "g-progress", ["c7", "close"])],
}
FLOW = {
 1: (["L1", "L2", "L3", "L4", "L5", "L6"], {"b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4, "b7": 5}),
 2: (["L1", "L2", "L3", "L4", "L5", "L6", "L7", "Demo"], {"o2": 0, "p2": 1, "c1": 2, "c2": 3, "c3": 4, "c4": 5, "c5": 6, "c6": 7}),
}
COVER_NOTES = {
 1: N(do="Leave this slide up while people arrive and open their laptops. Press → at 08:30.", more=["The next slide introduces CODED and you."],
      say="Over two days you will build an agent for a task you repeat every week, and make it run on its own."),
 2: N(do="Welcome back. Check that every laptop is signed in and the sandbox Drive opens.", more=["Teams sit together from the start today.", "The callback quiz comes after today's map."],
      say="Yesterday every one of you built an agent. This morning you finish it; then one agent per team learns to run without you.", silent="ask one person what their first Project is called."),
}
OUTCOMES_NOTES = {d: N(do="Read the outcomes. Ask which one matters most for their team.", expect={1: "Most people pick the Project or the prompt.", 2: "Most people pick the skill, the schedule or the review step."}[d],
                       say="These are the things you will do yourself today, on fictional files.", silent="pick one and say why it matters for audit work.") for d in (1, 2)}
ROAD = {1: {"title": "One firm, one client. <span class=\"hl\">Six lessons.</span>", "n": N(do="Point to the breaks: the cup button starts the break clock.", say="Mirqab is fictional, so you can make mistakes safely. Every file is made up.")},
        2: {"title": "One agent per team. <span class=\"hl\">One workflow by 15:15.</span>", "n": N(do="Point to Demo Day at 15:15.", say="By the afternoon break your workflow runs on a schedule. Then you show it.")}}
CLOSE = {
 1: {"big": "Card → Project → <span class=\"hl\">folder.</span>", "next": "Tomorrow: a fixed output and a skill, then your team's agent runs on a schedule, with a review step, and you show it at Demo Day.",
     "n": N(do="Recap the day in one line.", more=["Remind teams that they pick their agent at about 10:15 tomorrow, after the skills."], say="Thank you. See you at 08:30.")},
 2: {"big": "Claude does the first pass. <span class=\"hl\">You sign off.</span>", "next": "Thank you. Start with one card for one task this week, on dummy data, in an approved tool.",
     "n": N(do="Recap the two days in one line.", more=["Point to the take-home guide, the cheat sheet and the safe-use card on the site."], say="Your first card this week. Your first schedule this month.")},
}

# ------------------------------------------------------------------ Day 1 · Designing AI Agents for Real Work
def day1():
    s = [cover(1)]
    s.append(cards3("b0welcome", "open", "Welcome · who we are", "Welcome to <span class=\"hl\">CODED.</span>",
        [("Who we are", "CODED Academy", "Founded in Kuwait in 2015 as the first coding academy in the Middle East. We teach coding and AI to people and to companies.", "CODED Professionals builds programs for teams."),
         ("Who is teaching", "Your trainer", "A CODED Professionals instructor who builds AI workflows and teaches them to teams across Kuwait.", "Ask questions at any time."),
         ("Who is here", "18 RSM colleagues", "Assurance, Corporate Finance, Support and Analytics Advisory. Different jobs, one goal: less time on work that repeats.", "Your examples shape the two days.")],
        "Two hands-on days, on fictional files. You build, and we help.",
        n=N(time="08:30-08:35", do="Introduce yourself in one minute: your name, your role at CODED, and one way you use AI every week.",
            more=["Housekeeping: breaks about every hour, lunch and Dhuhr at 11:30, Asr at 14:55. Prayer room and toilets.",
                  "Sign-in check: every laptop opens claude.ai with the workshop account, and the workshop site. Helpers walk the room.", "The pre-MAP test is the next slide."],
            silent="ask who has used any AI tool at work this week.", say="We teach by building. You do the work on your laptop, and we walk the room.")))
    if "pre" in wk.FORM_DAY.get(1, []): s.append(mapslide("map1", "open", "before"))
    s += [outcomes(1), road(1)]
    # Lesson 1 · AI foundations
    s.append(story("b1story", "b1", "Lesson 1 · AI foundations", "Sunday 1 November, 08:50",
        "Most of this room already uses AI at work, in more than one tool. <b>Before we build anything, one question: what is it actually doing when it answers?</b>",
        "Know what it does <span class=\"hl\">and where it fails.</span>", "Explain what generative AI does well and where it can be wrong.",
        n=N(do="Run the live poll on the shared board: which AI tools did you use this month, and for what? Read three answers aloud.", expect="ChatGPT, Copilot, some Claude; emails, summaries, Excel help.",
            silent="share your own answer first.", more=["Two minutes for the poll, then move on."]), time="08:50-09:20"))
    s.append(askslide("b1ask", "b1", "Lesson 1 · your words", "What is <span class=\"hl\">AI?</span>", "Type an answer from the room, then press Enter",
        "Your answers stay on the screen. Next, we see what AI really does.",
        n=N(time="4 min", do="Click the search bar. Ask the room: what is AI? Type each answer as people say it and press Enter.",
            expect="A chatbot, a search engine, a robot, something that thinks, ChatGPT, automation.",
            more=["The same answer twice shows ×2 on its chip. Click a chip to remove a typo. Clear empties the board.",
                  "Press Esc to leave the search bar, then → to move on. With the bar empty, → and ← still move slides.",
                  "Do not correct anyone yet. The next three slides answer the question. The answers stay until the page reloads, so you can come back here."],
            silent="type the first answer yourself: a smart search engine. Ask if anyone agrees.", say="There are no wrong answers here. First, what does this room think?")))
    s.append(scene("b1an", "b1", "Lesson 1 · the picture", "A very well-read <span class=\"hl\">new joiner.</span>",
        "It has read more than any associate ever will, so its drafts are fast and fluent. It has never seen this client's file, so it fills gaps with what is usual.",
        "Fast and fluent. Not checked.",
        [{"ground": 268}, {"building": (240, 268), "tone": "dim"}, {"person": (110, 268), "tone": "hot", "label": "New joiner", "anim": "bob"},
         {"doc": (330, 250), "label": "Client file", "tone": "dim"}, {"move": "doc", "path": [(140, 200), (240, 150), (320, 200)], "dur": 5},
         {"pill": "Read a lot", "at": (130, 40), "tone": "hot", "delay": 0}, {"pill": "Drafts fast", "at": (340, 40), "tone": "hot", "delay": 1.5}, {"pill": "Never saw this file", "at": (240, 86), "tone": "bad", "delay": 3}],
        n=N(do="Point back to the room's answers: which of them fit this picture? Then ask: what would you check first in a new joiner's first working paper?", expect="The figures and the sources.", silent="say you would tick every figure.",
            say="Treat it like a talented new joiner. Useful from day one, reviewed every time.")))
    s.append(term("b1t1", "b1", "Lesson 1 · the idea", "What it <span class=\"hl\">really does.</span>", "Generative AI",
        "A model trained on very large amounts of text that writes by <b>predicting the most likely next word</b>, one word at a time. That is why it reads, summarizes, extracts and drafts well.",
        "Like the new joiner's fluent first draft…", "…each word is <b>likely</b>. Likely is not the same as <b>checked</b>.", "It predicts. It does not look things up unless you give it the source.",
        n=N(do="Link back to the new joiner: same idea, much bigger memory.", expect="People connect likely with not checked.", silent="ask: is a likely date always the right date?")))
    s.append(llmslide("b1llm", "b1", "Lesson 1 · live widget", "It writes by guessing <span class=\"hl\">the next word.</span>",
        "At each step, every possible next word gets a score. The model picks one, adds it, and predicts again.", "It predicts <b>likely</b> words. It does not check if they are <b>true</b>.",
        n=N(do="Read the start of the sentence. Ask the room which word comes next, and click their choice.",
            more=["Click Pick the top word: November is the most likely word. It is also right here, by luck.", "Start again and pick Paris (1%). The sentence still sounds confident.",
                  "The percentages are illustrative."], say="It is not looking at the ledger. A posting month is just another word to it.", silent="ask one person to choose for the room.", time="5 min")))
    s.append(term("b1t2", "b1", "Lesson 1 · the risk", "Fluent <span class=\"hl\">and wrong.</span>", "Hallucination",
        "When AI writes something that <b>sounds right but is not true</b>: a wrong amount, date, name or source, written with full confidence.",
        "A confident first draft…", "…that <b>nobody has ticked yet</b>. Professional skepticism applies.", "Tick every figure against the source document.",
        n=N(do="Ask: where in audit work would a wrong figure hurt most?", expect="Reconciliations, confirmations, the report.", silent="say: in a working paper your supervisor signs.")))
    s.append(cards3("b1cases", "b1", "Lesson 1 · two real cases", "Confident, fluent <span class=\"hl\">and made up.</span>",
        [("Case 1 · New York, 2023", "Court cases that never existed", "Two lawyers used ChatGPT to find past cases for a client's claim against an airline. It invented the cases and their quotes, and said they were real. The lawyers did not check.",
          "The judge fined the two lawyers and their firm $5,000."),
         ("Case 2 · Canada, 2024", "A refund rule the airline never had", "Air Canada's website chatbot told a customer, whose grandmother had just died, that he could ask for a lower bereavement fare after his flight. The airline's real policy said no.",
          "Air Canada said the chatbot was responsible for its own words. The tribunal disagreed, and the airline paid.")],
        "The AI was wrong, and the people paid. Check before anyone relies on it.",
        src="Sources: Mata v. Avianca, Inc., No. 22-cv-1461 (S.D.N.Y., 22 June 2023); Moffatt v. Air Canada, 2024 BCCRT 149 (14 February 2024).",
        n=N(time="4 min", do="Tell each case in about one minute. Then ask: who paid for the mistake, the tool or the people?", expect="The lawyers and the airline. Nobody blames the tool.",
            more=["Case 1: the lawyer asked ChatGPT if the cases were real, and it said yes. The judge also made them write to each real judge whose name was on a fake decision.",
                  "Case 2: Air Canada argued the chatbot was a separate legal entity. The tribunal rejected this and ordered the airline to pay about CA$812.",
                  "Optional, close to audit work: in October 2025 Deloitte Australia refunded part of a AU$440,000 government fee. Its report had made-up references and a made-up quote from a court judgment. The revised report says a generative AI tool was used."],
            silent="ask: whose name goes on a working paper, yours or Claude's?", say="The tool never signs. You do.")))
    s.append(check("b1chk", "b1", f"Claude gives KWD {D.num(D.AI_WRONG[1])} for an invoice that says KWD {D.num(D.INV[D.AI_WRONG[0]][4])}. <b>Why can this happen?</b>",
        [("It predicted a likely figure and nothing checked it", 1, "Right. It predicts likely words. You tick against the source."),
         ("It rounds amounts on purpose", 0, "It did not round. It took another likely figure."),
         ("The invoice must be wrong", 0, "The invoice is the source. The answer must match it.")]))
    s.append(term("b1t3", "b1", "Lesson 1 · the data rule", "Dummy data today. <span class=\"hl\">RSM's policy always.</span>", "The data rule",
        "No client data goes into an AI tool that RSM has not approved. Today every file is fictional. Back at work, <b>RSM's AI policy decides</b> what may go in.",
        "Engagement confidentiality for email…", "…applies to <b>AI tools in the same way</b>.", "When you are not sure, treat it as client data and ask first.",
        n=N(do="Point to the safe-use card on the site.", expect="Questions about which tools RSM approves: say IT or Risk Management decides.", silent="ask: would you email a client's ledger to a personal address?")))
    s.append(check("b1chk0", "b1", "A colleague asks you to try your agent on a client's real invoices this afternoon. <b>What do you do first?</b>",
        [("Use it: the agent only reads files, it keeps nothing", 0, "What you upload leaves the firm's control."), ("Check RSM's AI policy and use only an approved tool", 1, "Right. RSM's policy decides."),
         ("Use it, because invoices are not sensitive", 0, "Invoices are client data.")]))
    s.append(cards3("b1tools", "b1", "Lesson 1 · the tools available", "Three families <span class=\"hl\">of AI tools.</span>",
        [("Family 1", "Chat assistants", "Claude, ChatGPT, Microsoft 365 Copilot, Gemini.", "You ask; it drafts."),
         ("Family 2", "AI inside your apps", "Copilot in Excel and Outlook, Gemini in Gmail and Docs.", "AI where the file already is."),
         ("Family 3", "Automation tools", "n8n, Power Automate, scheduled tasks.", "It runs without you.")],
        "This program uses Claude. The method works in all three.",
        n=N(do="Ask which family each person used this week.", expect="Mostly family 1, some family 2.", silent="say which one you use most and why.",
            more=["Keep it short. The full map of Claude features in other tools comes at the end of Day 2, after they have used each one."])))
    s.append(listslide("b1tour", "b1", "Lesson 1 · Claude basics", "Three things <span class=\"hl\">for your first chat.</span>",
        ["<b>New chat:</b> start a fresh chat for each new job.", "<b>The + button:</b> attach the file Claude should read.", "<b>The message box:</b> type your request, then press Enter."],
        "Projects, connectors, skills and scheduled tasks come later, one lesson at a time.",
        n=N(do="Show each one on the presenting laptop while you talk.", expect="Everyone finds the + button in under a minute.", silent="ask someone to attach a file on their screen.",
            more=["Keep the rest of Claude closed for now. Each feature gets its own lesson: Projects in Lesson 3, connectors in Lesson 5, artifacts and skills on Day 2 morning, scheduled tasks after them."])))
    s.append(task("b1task", "b1", "t11", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 2 · Why chat isn't enough: a good prompt, what an agent is, and finding the work
    s.append(story("b2story", "b2", "Lesson 2 · Why chat isn't enough", "Sunday 1 November, 09:30",
        f"Faisal, a supervisor, gets two reconciliation tables for the same {D.CO_SHORT} invoices. <b>Different columns, different totals.</b> One flags a problem; the other says everything matches.",
        "Same files. <span class=\"hl\">Two answers.</span>", "Feel why one-off chat is not repeatable.",
        n=N(do="Ask: which table would you sign off?", expect="Neither, until they match.", silent="say: neither. Then start the task."), time="09:30-10:20"))
    s.append(task("b2task", "b2", "t12", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(tslide("b2two", "b2", "Debrief · one prompt, two chats", "The answer depended <span class=\"hl\">on the chat.</span>",
        ["", "Chat A", "Chat B"],
        [["Columns", "Invoice, amount, status", "Supplier, invoice, ledger, difference, comment"], ["Rows flagged", "None: every row Matched", "Two rows flagged"], ["Total checked", f"KWD {D.num(sum(r[4] for r in D.INVOICES))}", "5 invoices"]],
        "Same prompt, same files, two different tables.",
        n=N(do="First show three contrasting tables from the room. Then this slide.", expect="People see that only the chat changed: same prompt, same files.", silent="ask: which chat would you trust?",
            say="Two things changed the tables: the request and the chat. We fix the request first.")))
    s.append(term("b2why", "b2", "Lesson 2 · the prompt", "A better request. <span class=\"hl\">A better result.</span>", "Prompt",
        "A <b>prompt</b> is the request you type. Claude knows only what you write. When the prompt leaves a gap, Claude fills it with what is <b>usual</b>, not with what <b>you need</b>.",
        "A one-line brief to a new joiner…", "…versus a <b>full brief</b>: who, what, the rules and the shape.", "Most of the 18 tables differed because the 18 requests differed.",
        n=N(do="Ask: what did your Task 1.2 request leave out?", expect="The columns, what counts as a difference, what to do when a row is missing.",
            silent="read one short request from the room and ask what it does not say.")))
    s.append(livedemo("b2ws", "b2", "d10", n=N(time="5 min", do="Switch to Claude. Open two chats side by side and attach abdali-supplier-invoices-oct-2026.pdf to both. Send the weak request in one and the five-part request in the other, about invoice BPK-4471 (page 1).",
            more=["Before you send the strong request, read its five parts aloud: Role, Steps, Rules, Format, When unsure. Ask what each part adds.",
                  "Point at the strong answer: the exact amount, the invoice number and PO number Not found.", "Both prompts are on the prompt sheet, Demo 1.1."],
            silent="ask before the strong request: could the weak answer go into a working paper?")))
    s.append(listslide("b2five", "b2", "Lesson 2 · how to write it", "Five parts of <span class=\"hl\">a good prompt.</span>",
        ["<b>Role:</b> who Claude is, and the job in one line.", "<b>Steps:</b> what to do, in order.", "<b>Rules:</b> the source to use, units, dates and limits.",
         "<b>Format:</b> the exact shape, with the columns in order.", "<b>When unsure:</b> what to write when something is missing. Never guess."],
        "Attach the source file. Then check the answer against it.",
        n=N(do="Map each part to the strong request you just saw.", expect="People say When unsure is the part they never write.",
            more=["If the room is fast: two people rewrite their Task 1.2 request with the five parts and run it again, then compare it with their first table."],
            silent="ask: which part was missing from your own Task 1.2 request?")))
    s.append(check("b2pchk", "b2", "Which request gives an answer <b>you can put in a working paper?</b>",
        [("“Summarize this invoice for me.”", 0, "No rules and no format: Claude fills the gaps."), ("Role, steps, rules, format and When unsure, with the invoice attached", 1, "Right. Five parts and the source."),
         ("“Be very accurate with this invoice, please.”", 0, "Accurate is a wish, not a rule.")]))
    s.append(timer_slide("b2try", "b2", "Try it · 3 minutes", "Rewrite your request <span class=\"hl\">with the five parts.</span>",
        "Take your Task 1.2 request. Add Role, Steps, Rules, Format and When unsure. Run it again in a new chat with the same two files. Is your table closer to your neighbor's now?", 3,
        n=N(do="Start the timer. Walk the room and read three rewritten requests.", expect="Tables look more alike: the same columns, and both problems found more often.",
            silent="ask one person to read their When unsure line aloud.", more=["The five parts are on the slide before the check, and on the prompt sheet under Demo 1.1."])))
    s.append(term("b2t1", "b2", "Lesson 2 · the idea", "A prompt is not <span class=\"hl\">a process.</span>", "Repeatable",
        "Even a good prompt lives in one chat, and you type it again next time. A <b>repeatable</b> method keeps the same input, rules and output shape, so every run can be reviewed the same way.",
        "“Cook something nice”…", "…versus a <b>recipe card</b> anyone can follow.", "Audit work needs the same answer every time.",
        n=N(do="Ask: what makes an audit program repeatable?", expect="Written steps, the same working paper.", silent="say: it is written down, so anyone gets the same result.")))
    s.append(check("b2chk", "b2", "Two associates get different tables for the same invoices. <b>What is missing?</b>",
        [("A faster laptop", 0, "Speed was not the problem."), ("Fixed input, rules and output shape", 1, "Right. That is what an agent keeps."), ("A longer chat", 0, "Longer chats drift more, not less.")]))
    s.append(term("b2agent", "b2", "Lesson 2 · the agent", "From a chat <span class=\"hl\">to an agent.</span>", "AI agent",
        "An <b>agent</b> is AI set up to do <b>one job the same way every time</b>. Its instructions are saved, it reads the files it needs, it returns a fixed output, and it can run without you. Today you build one in Claude.",
        "A chat answers one question, once…", "…an agent does <b>one job, every week</b>, from a written method.", "Chat is for questions. Agents are for repeated work.",
        n=N(do="Link each part to the two days: saved instructions in Lessons 3 and 4, files in Lesson 5, a fixed output and a skill on Day 2 morning, then running without you.",
            expect="Some say an agent is a robot or a chatbot. Say: it is a saved method that can reach the files.", silent="say: think of a trained associate with a written procedure and the client file.")))
    s.append(term("b2t2", "b2", "Lesson 2 · agent-ready", "Which tasks <span class=\"hl\">suit an agent?</span>", "Agent-ready task",
        "A task that <b>repeats weekly</b>, has <b>clear rules</b>, and turns a <b>document in into a document out</b>. Judgment calls and client meetings stay with people.",
        "Three tags on a task…", "…three Yes means a <b>candidate agent</b>.", "Choose the task before you choose the tool.",
        n=N(do="Give one example of each tag from audit work.", expect="Invoice matching, lead schedules, confirmations.", silent="ask: which of your tasks repeats every week?")))
    s.append(sortslide("b2sort", "b2", "Lesson 2 · agent or not?", "Can an agent <span class=\"hl\">do this task?</span>",
        [("Copy figures from 30 PDF reports into one Excel table", "green"), ("Turn meeting notes into a list of actions, owners and dates", "green"),
         ("Send a weekly list of new files in a shared folder", "green"), ("Draft a reply to an upset client's email", "amber"),
         ("Write the first draft of a proposal", "amber"), ("Decide which candidate to hire", "red"),
         ("Negotiate a fee with a client", "red"), ("Approve a payment to a supplier", "red")],
        {"green": "Yes: an agent can do it", "amber": "Partly: AI drafts, you decide", "red": "No: keep it human"},
        n=N(time="4 min", do="Read each card aloud. Ask: can an agent do this? Hands up for yes, partly or no. Then tap the card to show the answer.",
            expect="People argue about the amber cards. Good: AI can draft and check, but a person decides and signs.",
            silent="say: if it needs judgment, a relationship or a signature, it stays with you.",
            more=["Link each green card to the four points on the slide before: it repeats, it takes minutes each time, the rules are clear, and it can run on a schedule.",
                  "Then Demo 1.2: Dana does the same with her own task list."])))
    s.append(livedemo("b2demo", "b2", "d13", time="3 min"))
    s.append(check("b2chk2", "b2", "Which of Dana's tasks is <b>not</b> a first agent?",
        [("Matching supplier invoices to the ledger", 0, "Three Yes: a strong candidate."), ("Discussing findings with the client's CFO", 1, "Right. It needs judgment and trust."), ("Chasing missing documents from clients", 0, "Three Yes: a candidate.")]))
    s.append(task("b2task2", "b2", "t13", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(askslide("b2board", "b2", "Lesson 2 · what repeats?", "What repeats <span class=\"hl\">across departments?</span>", "Type a person's strongest task, then press Enter",
        "The tasks that come up most are the best first agents.", n=N(time="2 min", do="Type each answer.")))
    # Lesson 3 · Pick your task, design the agent, then build one together
    s.append(story("b3story", "b3", "Lesson 3 · Pick and design", "Sunday 1 November, 10:30",
        "Faisal: <b>“Every associate follows the same audit program and produces the same working paper. Why does every AI table look different?”</b>",
        "Write it down <span class=\"hl\">once.</span>", "Pick your task, describe it as an Agent Card, then build one together in a Project.",
        n=N(do="Ask: what does an audit program give a new associate?", expect="Steps, rules, the template.", silent="say: it removes the guessing."), time="10:30-11:30"))
    s.append(term("b3t5", "b3", "Lesson 3 · choosing", "Pick the task <span class=\"hl\">with the highest score.</span>", "Scoring a use case",
        "Score each candidate from 1 to 5 on four points. The points are <b>how often</b>, <b>minutes each time</b>, <b>how clear the rules are</b>, and <b>can it run on a schedule</b>.",
        "The most interesting task…", "…is not always the best <b>first</b> agent.", "Day 2 needs an agent that can run without you.",
        n=N(do="Start from the board you just reviewed. Score one task with the room.", expect="Invoice matching or chasing documents scores high.", silent="score Dana's invoice task yourself.")))
    s.append(livedemo("b3demo", "b3", "d15"))
    s.append(tslide("b3tracks", "b3", "Lesson 3 · the four tracks", "Pick a track <span class=\"hl\">for your agent.</span>", ["Track", "Starting example", "Pack"],
        [[t, ex, pk] for t, ex, _f, pk in CD.TRACKS], "Your own task fits a track. If not, ask Claude for a dummy pack with 2 planted errors (10 minutes).", cls="tight",
        n=N(do="Read the four tracks. Match them to the board clusters.", expect="Assurance picks extraction or analysis; Support picks workflow or reporting.", silent="say which track the coordinators' tasks fit.")))
    s.append(scene("b3scene", "b3", "Lesson 3 · the picture", "The audit program <span class=\"hl\">every associate follows.</span>",
        "It says what to read, what to do and what the working paper looks like. An Agent Card does the same for an agent, in four boxes.",
        "Input · Instruction · Output · When.",
        [{"ground": 268}, {"doc": (90, 230), "label": "Input", "tone": "hot"}, {"laptop": (240, 250), "label": "Instruction"}, {"doc": (390, 230), "label": "Output", "tone": "ok"},
         {"move": "doc", "path": [(110, 190), (240, 160), (370, 190)], "dur": 5}, {"pill": "Same steps", "at": (140, 50), "tone": "hot", "delay": 0},
         {"pill": "Same shape", "at": (340, 50), "tone": "hot", "delay": 1.5}, {"pill": "When: Day 2", "at": (240, 100), "tone": "", "delay": 3}],
        n=N(do="Point to each box as it appears.", expect="People map their own task to the boxes.", silent="map the invoice task yourself first.",
            say="A card a new joiner could follow is a card Claude can follow.")))
    s.append(term("b3t1", "b3", "Lesson 3 · the idea", "Four boxes <span class=\"hl\">before any build.</span>", "The Agent Card",
        "<b>Input:</b> what it works on. <b>Instruction:</b> the rules it follows. <b>Output:</b> what it hands back, in a fixed shape. <b>When:</b> when it runs without you (empty until Day 2).",
        "Like the audit program…", "…the card fixes the <b>input, the rules and the output</b>.", "This card fixes what went wrong in Task 1.2.",
        n=N(do="Show Dana's invoice card from the site.", expect="People see that each box answers one question.", silent="ask: which box was missing in Task 1.2?")))
    s.append(check("b3chk0", "b3", "Dana writes: <b>the month's supplier invoices (PDF) and the purchase ledger.</b> Which box of the card is this?",
        [("Input", 1, "Right. It is what the agent works on."), ("Instruction", 0, "Instruction holds the rules it follows."), ("Output", 0, "Output is what it hands back.")]))
    s.append(term("b3t2", "b3", "Lesson 3 · literal", "Claude follows <span class=\"hl\">what you write.</span>", "Literal instructions",
        "Claude does what the words say, not what you meant. “Check the invoices” leaves the checking to chance. “Match number, date and amount; flag any difference” does not.",
        "“Check the invoices”…", "…becomes <b>“Match number, date and amount. Flag any difference.”</b>", "Vague words caused the misses in Task 1.2.",
        n=N(do="Rewrite one vague line from the room into a literal one.", expect="People add the fields and the rule.", silent="rewrite “review the leases” as an example.")))
    s.append(check("b3chk", "b3", "Which Instruction line will give the <b>same result every run?</b>",
        [("“Check the invoices carefully.”", 0, "Careful is not a rule."), ("“Match number, date and amount; flag any difference.”", 1, "Right. Fields and a rule."), ("“Do a good reconciliation.”", 0, "Good is not a rule.")]))
    s.append(task("b3task2", "b3", "t15", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(term("b3t3", "b3", "Lesson 3 · the home", "A Project is <span class=\"hl\">the agent's home.</span>", "Claude Project",
        "A <b>Project</b> keeps instructions and knowledge files. Claude uses them in <b>every chat inside it</b>, so nobody explains the task again.",
        "A client file with the procedures already in it…", "…every new chat starts with <b>the card and the template</b>.", "Projects: + New Project, then Set project instructions.",
        n=N(do="Open Projects on the presenting laptop.", expect="Everyone finds + New Project.", silent="ask: where would you keep the invoice template?")))
    s.append(term("b3t4", "b3", "Lesson 3 · knowledge or input", "Templates stay. <span class=\"hl\">Documents come and go.</span>", "Knowledge versus input",
        "<b>Knowledge:</b> templates, reference files and one example output, saved in the Project. The rules go in the instructions. <b>Input:</b> this month's documents, attached or read with each run.",
        "The template and the example…", "…live in knowledge. <b>The invoices come with each run.</b>", "Mixing the two is the most common build error.",
        n=N(do="Ask: where does next month's ledger go?", expect="With the run, not in knowledge.", silent="say it, then ask why.")))
    s.append(check("b3chk2", "b3", "Where does <b>this month's invoice pack</b> go?",
        [("Into the Project knowledge", 0, "Knowledge is for what stays the same."), ("Into each run: attached, or read from the folder", 1, "Right. Input changes every run."), ("Into the Project instructions", 0, "Instructions are the rules, not the documents.")]))
    s.append(livedemo("b3pp", "b3", "d14", time="5 min"))
    s.append(task("b3task", "b3", "t14", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 4 · Build your agent (the five parts are not taught again: Lessons 2 and 3 already did)
    s.append(term("b4t2", "b4", "Lesson 4 · test", "Show one example. <span class=\"hl\">Then test three.</span>", "Example output and testing",
        "One filled <b>example output</b> in the knowledge teaches the shape faster than a description. Then check <b>three cases where you know the answer</b> before you trust it.",
        "A new joiner learns from one good working paper…", "…and you <b>review their first three</b>.", "Fix the instructions, not the answer.",
        n=N(do="Show the template with its example row.", expect="People see the example row in the knowledge file.", silent="ask: how many tests before you trust a new joiner?")))
    s.append(task("b4task", "b4", "t16", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(task("b4task2", "b4", "t16b", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 5 · Build: Input and Output
    s.append(story("b5story", "b5", "Lesson 5 · Build: Input", "Sunday 1 November, 14:00",
        "Every Sunday, Noura, a project coordinator, downloads the same files from the shared drive and <b>drags them into a chat, one by one.</b>",
        "The files are already somewhere. <span class=\"hl\">Let the agent read them there.</span>", "Connect your agent to a Drive folder, so it reads the files where they live.",
        n=N(do="Ask: how many files do you drag into a tool each week?", expect="Many, every week.", silent="say: tomorrow a schedule cannot drag files."), time="14:00-14:55"))
    s.append(term("b5t1", "b5", "Lesson 5 · input", "A key to one cabinet, <span class=\"hl\">not the whole archive.</span>", "Connector",
        f"A <b>connector</b> lets Claude read from an app such as Google Drive. It reaches every file the signed-in account can open, so today you use a CODED account that opens only the <b>{D.SANDBOX}</b>.",
        "One key, one cabinet…", "…one connector, <b>an account that opens only what the task needs</b>.", "Customize, then Connectors, then Google Drive.",
        n=N(do="Show Google Drive under Customize, then Connectors (connected before Day 1).", expect="The connector and the sandbox folders.", silent="ask: which folders should an audit agent never see?",
            fallback="If sign-in fails, upload the files and continue.")))
    s.append(check("b5chk1", "b5", "Your agent will run tomorrow at 08:00. <b>Why can it not use files you drag in?</b>",
        [("Dragging files is too slow", 0, "Speed is not the reason."), ("Nobody is there to drag them at 08:00", 1, "Right. The input must live where the agent can read it."), ("Drive files are safer", 0, "Safety comes from what you connect, not from Drive.")]))
    s.append(livedemo("b5pp1", "b5", "d17"))
    s.append(task("b5task1", "b5", "t17", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 6 · Show and tell, and the Day 2 hook (artifacts and skills moved to Day 2 morning, Aya, 15 Nov)
    s.append(timer_slide("b7show", "b7", "Show and tell · 15:15", "Four teams. <span class=\"hl\">Ninety seconds each person.</span>",
        "Show your card, then run your agent live on one file from your track folder. Your team watches and asks one question.", 15,
        n=N(do="Teams demo at their own tables at the same time. Walk between them.", expect="Most agents run; some flag the messy sample.", silent="start the first team yourself.",
            fallback="If a live run hangs, show the last good result.", say="Card, then run. Ninety seconds.")))
    s.append(livedemo("b7demo", "b7", "d111"))
    s.append(wrap("w1", "close", "One card. One Project. <span class=\"hl\">One folder each.</span>",
        [("You built", "Your own agent", "A card, two Projects and a connected folder."), ("You found", "2 planted problems", f"SCC-0718 and the {D.CUTOFF_INV} cut-off, in the invoice agent."),
         ("The habit", "Flag, never guess", "Claude does the first pass. You review.")],
        "Tomorrow: first a fixed output and a skill. Then your team's agent runs on a schedule."))
    notes_day1.apply(s)
    return s

# ------------------------------------------------------------------ Day 2 · Turning Agents into Operational Workflows (rebuilt by Aya's plan, 15 Nov night)
# Skills (own task) → artifacts → scheduled tasks → Claude, n8n or Power Automate (n8n demo) → mini project on a department pack → demos → close.
import day2_data as X
PACK_SHORT = {"audit": ("Findings log · 30 findings", "Open, overdue and high-risk findings dashboard"), "tax": ("Filing calendar · 28 filings", "Deadline dashboard and a weekly alert list"),
              "cf": ("Deal pipeline · 22 deals", "Weighted pipeline dashboard and a partner deck"), "risk": ("Risk register · 18 risks", "Heat map and a board summary"),
              "cyber": ("Vulnerability scan · 26 findings", "Severity dashboard and the top 5 to fix"), "it": ("Helpdesk tickets · 40 tickets", "SLA dashboard and a monthly report"),
              "esg": ("Energy data · 3 sites, 12 months", "Emissions dashboard and a board deck"), "data": ("Sales transactions · 60 rows", "Data-quality check and a sales dashboard"),
              "finance": ("Budget against actual · 40 lines", "Variance dashboard and a memo"), "hr": ("People data · 36 employees, IDs only", "HR dashboard and a monthly note"),
              "cx": ("Client survey · 40 responses", "NPS dashboard and a feedback deck")}
LOOK_FOR = [("Task relevance", "A real department task, with an impact number"), ("It works", "Project, skill and artifact; the task runs on demand"),
            ("Source accuracy", "Three figures match the file"), ("Human controls", "DRAFT, your rules, a named reviewer"), ("Test evidence", "A run log, and both hidden problems flagged")]

def day2():
    s = opening(2)
    # Callback · Day 1
    s.append(rule("c1rule", "open", "Callback · Day 1", "Yesterday you built it. <span class=\"hl\">Today you package it and schedule it.</span>",
        "Each of you has an Agent Card and a Project. Two quick questions, then skills.",
        n=N(do="Click Scheduled in the left sidebar and open yesterday's 16:25 run.", time="08:33-08:35")))
    s.append(check("c1chk1", "open", "Where does this month's invoice pack go in an agent?",
        [("Into the Project knowledge", 0, "Knowledge is what stays the same."), ("Into each run, with this month's files", 1, "Right. Input changes every run."), ("Into the instructions", 0, "Instructions hold the rules.")]))
    s.append(check("c1chk2", "open", "An invoice has no PO number. <b>What should the agent write?</b>",
        [("Not found, and a note", 1, "Right. Flag, never guess."), ("The most likely PO", 0, "That is a guess."), ("Nothing", 0, "A blank hides the gap.")]))
    # Lesson 1 · Skills
    s.append(story("s1story", "s1", "Lesson 1 · Skills", "Monday 16 November, 08:40",
        "Dana's invoice agent works, but only inside her own Project. Faisal asks: <b>“Can the other two associates use your method in their own chats, without copying your Project?”</b>",
        "Write the method once. <span class=\"hl\">Use it anywhere.</span>", "Know the four building blocks, then package your own task as a skill.", time="08:40-09:35"))
    s.append(tslide("s1blocks", "s1", "Lesson 1 · four building blocks", "Four building blocks. <span class=\"hl\">Four jobs.</span>", ["", "Prompt", "Project instructions", "Skill", "Agent"],
        [["What it is", "The request you type now", "A standing brief for one workspace", "A saved method Claude loads when the task matches", "One job, done the same way every time"],
         ["Where it lives", "One message", "One Project", "Your account: any chat, Project or schedule", "Built from all of these"],
         ["How long it lasts", "One answer", "Every chat in that Project", "Until you change it; you can share it", "Every run, even without you"],
         ["At the firm", "A question to a colleague", "The engagement's planning memo", "The firm's audit program", "A trained associate with the file and a calendar"]],
        "A prompt asks once. Instructions set the context. A skill holds the method. An agent puts them together.", cls="tight"))
    s.append(listslide("s1why", "s1", "Lesson 1 · why combine them", "Why we <span class=\"hl\">combine them.</span>",
        ["<b>Prompt:</b> says what to do on this run. Alone, it is gone when the chat ends.", "<b>Project instructions:</b> keep the context and the template. Alone, they stay in one Project.",
         "<b>Skill:</b> keeps the method: steps, rules, output. Alone, it has no files and no schedule.", "<b>The input and a schedule:</b> the files to read, and the When.",
         "<b>Together:</b> the same checked result, every run, without you."],
        "Prompt: this run. Project: this context. Skill: this method. Agent: all of them."))
    s.append(term("s1pick", "s1", "Lesson 1 · how a skill loads", "How Claude <span class=\"hl\">picks a skill.</span>", "Skill description",
        "Claude reads each skill's <b>name and one-line description</b>. When your request matches, it loads the full skill. A vague description means the skill is never used, or used for the wrong task.",
        "A label on a binder…", "…tells you <b>which procedure to open</b>.", "Name the task and the file type in the description."))
    s.append(check("s1chk", "s1", "Your method must work in any chat and on a schedule, for your whole team. <b>What do you build?</b>",
        [("Project instructions", 0, "They stay in one Project."), ("A skill with a clear description", 1, "Right. A skill travels to chats, Projects and schedules."),
         ("A long prompt saved in a note", 0, "You would paste it every time.")]))
    s.append(livedemo("s1demo", "s1", "e21", time="6 min"))
    s.append(task("s1task", "s1", "u21", n=N(do="Start the timer. Walk the room. Ask each person what their task is.")))
    s.append(task("s1task2", "s1", "u22", n=N(do="Start the timer. Walk the room.")))
    s.append(check("s1safe", "s1", "Before you share a skill with your team, <b>what do you check first?</b>",
        [("It has a long, detailed name", 0, "A short, clear name is better."), ("No client names or real figures, and it passed a fresh-chat test", 1, "Right. Safe to share, and it works."),
         ("It was made in the last week", 0, "Age does not matter. Content does.")]))
    # Lesson 2 · Artifacts
    s.append(story("a2story", "a2", "Lesson 2 · Artifacts", "Thursday 19 November, 09:00",
        "Every Thursday, Faisal gets the engagement status as a six-tab Excel file. <b>He scrolls for ten minutes to find the three numbers he needs.</b>",
        "Show the three numbers first. <span class=\"hl\">Build a dashboard.</span>", "Turn one file into a KPI dashboard and a short deck, and check the numbers.", time="09:45-10:55"))
    s.append(term("a2term", "a2", "Lesson 2 · the idea", "An artifact is <span class=\"hl\">a working file.</span>", "Artifact",
        "Something Claude builds next to the chat that you can <b>open, click, edit, download and share</b>: a dashboard, a chart, a slide deck, a document or a small tool. You change it by asking in plain words.",
        "A printed report…", "…becomes <b>a live page you can click and change</b>.", "Ask for what the reader needs to see, not only the data."))
    s.append(cards3("a2cards", "a2", "Lesson 2 · what you can build", "What you can <span class=\"hl\">build.</span>",
        [("Dashboard", "KPIs at a glance", "Tiles for the key numbers, charts, a table of what needs action, and a filter.", "For partners and managers"),
         ("Presentation", "Slides from the same numbers", "Five slides for a meeting: the numbers, the risks and the decision.", "For meetings and clients"),
         ("Tool", "A small working page", "A checklist, a tracker, a calculator or a form that people click.", "For your team")],
        "One file can feed all three. The numbers must match."))
    s.append(tslide("a2dept", "a2", "Lesson 2 · by department", "Artifacts <span class=\"hl\">by department.</span>", ["Department", "Dashboard", "Deck, memo or tool"],
        [["Audit", "Open findings by risk and owner", "Partner update"], ["Tax", "Filings due this week and past due", "Deadline tracker"],
         ["Finance", "Budget against actual", "Memo to the managing partner"], ["HR", "Headcount and training hours", "Monthly people note"],
         ["Cybersecurity", "Open findings by severity", "Top 5 to fix this week"], ["ESG", "Emissions by site and month", "Board summary"]],
        "Your mini project this afternoon starts from one of these.", cls="tight"))
    s.append(listslide("a2five", "a2", "Lesson 2 · how to ask", "Ask for an artifact <span class=\"hl\">in five parts.</span>",
        ["<b>Reader:</b> who opens it, and what they decide.", "<b>Data:</b> the file, and only the file.", "<b>KPIs:</b> three to six numbers, each with its formula.",
         "<b>Layout:</b> tiles on top, then charts, then the action table.", "<b>Rules:</b> calculate with code; list blanks under Data issues; never guess."],
        "Then check three numbers by hand."))
    s.append(check("a2chk", "a2", "A dashboard tile says 13 findings are overdue. <b>Before you show it to the partner, what do you do?</b>",
        [("Filter the file and count them yourself", 1, "Right. Check the tile against the source."), ("Ask Claude if it is sure", 0, "Claude may say yes and still be wrong."),
         ("Round it to about a dozen", 0, "Rounding hides the check.")]))
    s.append(livedemo("a2demo", "a2", "e22", time="7 min"))
    s.append(task("a2task", "a2", "u23", n=N(do="Start the timer. Walk the room. Ask which pack each person picked.")))
    s.append(term("a2agent", "a2", "Lesson 2 · inside your agent", "Put the layout <span class=\"hl\">in your skill.</span>", "Artifacts inside your agent",
        "Write the dashboard's layout into your skill: the tiles, the charts and the table, in order. Next month a new file goes in, and <b>the same dashboard comes out</b>, ready to compare.",
        "A new layout every month…", "…<b>the same layout, new numbers</b>.", "Fixed layout, new data, every run."))
    s.append(task("a2task2", "a2", "u24", n=N(do="Start the timer. Walk the room.")))
    s.append(timer_slide("a2gallery", "a2", "Gallery · 5 minutes", "Three dashboards <span class=\"hl\">on the big screen.</span>",
        "Three people show their dashboard for one minute each: the reader, three KPIs, and one data issue it found.", 5))
    # Lesson 3 · Scheduled tasks
    s.append(story("t3story", "t3", "Lesson 3 · Scheduled tasks", "Sunday 22 November, 08:00",
        "Your skill builds the dashboard in two minutes. <b>But on Sunday at 08:00 you are in a client meeting, and nobody opens Claude.</b>",
        "Set it once. <span class=\"hl\">It runs on time.</span>", "Put your own skill on a weekly schedule and test it once.", time="10:55-11:30"))
    s.append(term("t3term", "t3", "Lesson 3 · the idea", "A calendar reminder <span class=\"hl\">that also does the work.</span>", "Scheduled task",
        "A <b>scheduled task</b> is a saved prompt that Claude runs hourly, daily, on weekdays, weekly or on demand. Its prompt calls your <b>skill</b>, and the run reads the file stored in that skill.",
        "A reminder that only reminds you…", "…versus one that <b>does the work and leaves the file</b>.", "Click Scheduled in the left sidebar, then New task."))
    s.append(listslide("t3fresh", "t3", "Lesson 3 · how a run works", "Each run <span class=\"hl\">starts fresh.</span>",
        ["<b>No memory:</b> the prompt and the skill must say everything.", "<b>Runs remotely:</b> your laptop can be closed.",
         "<b>Input inside the skill:</b> today the file is a reference file in your skill. At work, an approved tool brings new files.",
         "<b>Run log:</b> the first line of every run: date and time, file read, items flagged.", "<b>History:</b> the Scheduled page keeps every past run for review."],
        "Open the latest run every morning, even on quiet days."))
    s.append(check("t3chk", "t3", "Your scheduled task runs at 08:00. <b>What does each run know?</b>",
        [("Everything from last week's run", 0, "Each run is its own session."), ("Only what the prompt and the skill say", 1, "Right. Write down everything a run needs."), ("What you typed in your last chat", 0, "A run does not see your chats.")]))
    s.append(livedemo("t3demo", "t3", "e23", time="5 min"))
    s.append(task("t3task", "t3", "u25", n=N(do="Start the timer. Walk the room.")))
    s.append(tslide("t3map", "t3", "Lesson 3 · transfer", "Scheduling <span class=\"hl\">in other tools.</span>", ["", "Claude", "ChatGPT", "Microsoft 365 Copilot", "Gemini"],
        [["When", "Scheduled task", "Scheduled task", "Scheduled prompt", "Scheduled action"], ["Event triggers", "n8n or Power Automate", "n8n or Power Automate", "Power Automate", "n8n or Apps Script"]],
        "Time triggers live in the assistant. Event triggers need an automation tool: that is after lunch.", cls="tight"))
    # Lesson 4 · Claude, n8n or Power Automate
    s.append(story("n4story", "n4", "Lesson 4 · Claude, n8n or Power Automate", "Tuesday 17 November, 14:07",
        "A client emails a signed confirmation at 14:07. The team wants it logged in the tracker <b>within a minute, not at tomorrow's 08:00 run.</b>",
        "Some work starts with an event. <span class=\"hl\">That needs an automation tool.</span>", "Know what Claude cannot do yet, and when n8n or Power Automate takes over.", time="12:30-12:55"))
    s.append(tslide("n4cmp", "n4", "Lesson 4 · side by side", "Three tools, <span class=\"hl\">three strengths.</span>", ["", "Claude", "n8n", "Power Automate"],
        [["Starts", "At a time, or when you ask", "On any event, or at a time", "On a Microsoft 365 event, or at a time"],
         ["Best at", "Reading, judging, writing", "Moving data between many apps", "Flows and approvals in Microsoft 365"],
         ["You build it", "In plain words", "Nodes on a canvas", "Actions in a flow"],
         ["Runs under", "Your Claude account", "n8n cloud or the firm's server", "The firm's Microsoft 365"],
         ["Usually owned by", "You", "IT or an automation owner", "IT, or staff trained by IT"]],
        "Claude reads and writes. n8n and Power Automate connect systems.", cls="tight"))
    s.append(listslide("n4limits", "n4", "Lesson 4 · the limits", "What Claude <span class=\"hl\">cannot do yet.</span>",
        ["<b>Event triggers:</b> scheduled tasks start at a time or on demand, not when an email or a file arrives.", "<b>Exact, high-volume moves:</b> copying thousands of rows the same way every time is a job for fixed steps.",
         "<b>Company controls:</b> it runs on your account, without the retries, alerts and approval trail IT expects.", "<b>Every system:</b> it reaches only the apps your firm allows it to connect to.",
         "<b>Same words every time:</b> AI may word a result differently on each run, so you still check it."],
        "Where Claude stops, an automation tool starts."))
    s.append(listslide("n4when", "n4", "Lesson 4 · when to switch", "When to <span class=\"hl\">switch.</span>",
        ["The trigger is an <b>event</b>: an email, a form, a new file, a system update.", "One flow touches <b>three or more systems</b>.",
         "It runs <b>hundreds of times a day</b>, or must give exactly the same output.", "Many people rely on it, so <b>IT must own it</b>: logs, retries, alerts, access.",
         "It needs a <b>formal approval</b>, with a record of who approved."],
        "Use both: the automation tool moves the data, and Claude reads and writes inside the flow."))
    s.append(check("n4chk", "n4", "Client documents arrive by email at any time. The team wants each one logged <b>as it lands</b>. Which tool fits?",
        [("An automation tool such as n8n or Power Automate, set up with IT", 1, "Right. The trigger is an event."), ("A Claude scheduled task, daily at 08:00", 0, "That waits for a time, not for the email."),
         ("One long chat that someone keeps open", 0, "A chat does not run on its own.")]))
    s.append(tslide("n4terms", "n4", "Lesson 4 · the words", "Three words <span class=\"hl\">for any automation.</span>", ["Word", "What it means", "In n8n", "In Power Automate"],
        [["Trigger", "What starts the flow", "Schedule, Gmail, Webhook or Form trigger", "When an email arrives; Recurrence"],
         ["Node or action", "One step: read, calculate, decide, call AI", "Code, If, Edit Fields, HTTP Request, AI Agent", "Condition, Compose, Excel, AI Builder"],
         ["Output", "Where the result lands", "A sheet row, an email draft, a file", "A SharePoint item, an Outlook draft, a Teams post"]],
        "Data moves from node to node as items. Each run is an execution you can open.", cls="tight"))
    s.append(livedemo("n4demo", "n4", "e24", badge="n8n · video", app="n8n", time="9 min"))
    s[-1].rec["note"]["do"] = ("Play the video: click the video file on the slide (100 seconds, captioned, no sound). Talk over it. "
                               "Pause on the If step (3 invoices true, 2 false) and on the final run. Do not build a flow live.")
    s.append(check("n4chk2", "n4", "In the n8n demo, <b>which step decided where each invoice went?</b>",
        [("The trigger", 0, "The trigger only starts the run."), ("The If node", 1, "Right. It sends each item down the true or the false branch."), ("The Code node", 0, "It only listed the invoices.")]))
    # Lesson 5 · Mini project
    s.append(listslide("m5brief", "m5", "Lesson 5 · Mini project", "Your department's agent: <span class=\"hl\">the checklist.</span>",
        ["<b>Card:</b> department, task, input, instruction, output, when, who reviews, impact.", "<b>Project:</b> five-part instructions and one example output.",
         "<b>Skill:</b> saved and tested in a fresh chat.", "<b>Artifact:</b> a dashboard, report or deck, in a fixed layout.",
         "<b>Schedule:</b> a task run once on demand, with a run log.", "<b>Review:</b> three figures checked, DRAFT and Reviewed by."],
        "Everything from two days, on one department's work.", n=N(time="12:55-13:00")))
    _p = {p["key"]: p for p in X.PACKS}
    _order = [p["key"] for p in X.PACKS]
    s.append(tslide("m5dept1", "m5", "Lesson 5 · the packs, 1 of 2", "Pick a department. <span class=\"hl\">Packs 1 to 6.</span>", ["Department", "The file", "What to build"],
        [[_p[k]["dept"], PACK_SHORT[k][0], PACK_SHORT[k][1]] for k in _order[:6]], "Every file is fictional. Each one hides two problems.", cls="tight"))
    s.append(tslide("m5dept2", "m5", "Lesson 5 · the packs, 2 of 2", "Pick a department. <span class=\"hl\">Packs 7 to 11.</span>", ["Department", "The file", "What to build"],
        [[_p[k]["dept"], PACK_SHORT[k][0], PACK_SHORT[k][1]] for k in _order[6:]], "Or bring your own task, on fictional data.", cls="tight"))
    s.append(tslide("m5look", "m5", "Lesson 5 · what I look for", "What a strong project <span class=\"hl\">shows.</span>", ["What I look for", "Strong"],
        [list(r) for r in LOOK_FOR], "I pick four or five projects to show at 14:40.", cls="tight"))
    s.append(task("m5task", "m5", "u26", n=N(do="Start the timer. Walk the room. At 20 minutes, check that everyone has a Project.")))
    # Lesson 6 · Project demos
    s.append(timer_slide("d6demo", "d6", "Project demos · 14:40", "Four minutes each. <span class=\"hl\">Show it working.</span>",
        "The problem, your card, a live run or your artifact, the impact number, and what you would automate next.", 20))
    # Close
    s.append(mapslide("c7map", "c7", "after"))
    s.append(rule("c7cert", "c7", "Certificates · 15:15", "Two days. <span class=\"hl\">An agent each.</span>",
        "Come up for your certificate of completion when your name is called, then stay for one group photo."))
    s.append(tslide("b7map", "c7", "Close · the transfer map", "Same building blocks, <span class=\"hl\">different names.</span>", C.TRANSFER_HEAD, C.TRANSFER,
        "Learn the method once. The card works in any tool.", cls="tight"))
    s.append(timer_slide("c7next", "c7", "Next steps · 15:25", "Your next task. <span class=\"hl\">Your tool.</span>",
        "Tell your table the next task you will automate back at work, and the tool you will use for it.", 3))
    s.append(wrap("w2", "close", "Skill, artifact, schedule. <span class=\"hl\">Then your own agent.</span>",
        [("You built", "A skill and a dashboard", "Your own task, packaged, then shown as KPIs and slides."), ("You scheduled", "A task that runs without you", "With a run log you read every morning."),
         ("The habit", "Drafts, never final", "Claude does the first pass. You sign off.")],
        "This week: one card, one skill, on dummy data, in an approved tool."))
    notes_day2.apply(s)
    return s

TOPICS = {1: {"open": "Opening", "b1": "Lesson 1 · AI foundations", "b2": "Lesson 2 · Why chat isn't enough", "b3": "Lesson 3 · Pick and design",
              "b4": "Lesson 4 · Build your agent", "b5": "Lesson 5 · Build: Input", "b7": "Lesson 6 · Show and tell", "close": "Close"},
          2: {"open": "Opening and callback", "s1": "Lesson 1 · Skills", "a2": "Lesson 2 · Artifacts", "t3": "Lesson 3 · Scheduled tasks",
              "n4": "Lesson 4 · Claude, n8n or Power Automate", "m5": "Lesson 5 · Mini project", "d6": "Lesson 6 · Project demos",
              "c7": "Post-MAP, survey, certificates and next steps", "close": "Close"}}
DAYFN = {1: day1, 2: day2}

# Day 2 rebuild (Aya, 15 Nov night): sections, lesson flow, map and close for the new order
SECTIONS[2] = [("Skills", "g-mark", ["open", "s1"]), ("Artifacts and schedules", "g-code", ["a2", "t3"]), ("Automation tools", "g-frame", ["n4"]),
               ("Mini project", "g-impact", ["m5", "d6"]), ("Close", "g-progress", ["c7", "close"])]
FLOW[2] = (["L1", "L2", "L3", "L4", "L5", "L6"], {"s1": 0, "a2": 1, "t3": 2, "n4": 3, "m5": 4, "d6": 5})
COVER_NOTES[2] = N(do="Leave this up while people arrive. Check that every laptop has claude.ai and the workshop site open.",
                   say="Yesterday every one of you built an agent. Today you package it, schedule it, and build one for a department.")
OUTCOMES_NOTES[2] = N(do="Read the outcomes. Ask which one matters most for their team.", expect="Most people pick the skill, the dashboard or the schedule.",
                      say="These are the things you will do yourself today, on fictional files.")
ROAD[2] = {"title": "Skills, artifacts, schedules. <span class=\"hl\">Then your own agent.</span>",
           "n": N(do="Point to the mini project at 12:55 and the demos at 14:40.", say="The morning teaches the parts. The afternoon is yours.")}
CLOSE[2] = {"big": "Claude does the first pass. <span class=\"hl\">You sign off.</span>", "next": "Thank you. This week: one card, one skill, on dummy data, in an approved tool.",
            "n": N(do="Recap the two days in one line.", more=["Point to the take-home guide, the cheat sheet and the safe-use card on the site."], say="Your first skill this week. Your first schedule this month.")}
