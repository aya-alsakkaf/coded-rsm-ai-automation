# -*- coding: utf-8 -*-
"""The mini project page (Aya, 16 Nov 09:32): its own page, out of the lab. The trainee picks a department, then gets the scenario,
the file, what the agent must do, a Project card filled in for that department, the steps with times and every prompt with COPY.
Written by gen_files.py as a site file (coded-rsm-ai-automation-mini-project.html, short link /project). No answers on this page:
each pack's two hidden problems are only on the staff answer key."""
import html, os
import day2_data as X
import content_demos as CD

FILE = "coded-rsm-ai-automation-mini-project.html"
PFX = "coded-rsm-ai-automation"
def e(s): return html.escape(str(s), quote=True)

# role, scenario, what the agent must do, artifact, when, who reviews, minutes by hand (an example for the impact line)
SCEN = {
 "audit": ("Senior associate, Audit and Assurance",
   "Mirqab's audit team keeps one findings log for 12 clients: 30 findings so far. Every Sunday the partner asks three questions: what is still open, what is overdue, and which high-risk findings need her. Today a supervisor spends about 40 minutes filtering the sheet and writing the email.",
   ["List every finding that is not Closed, grouped by client.", "List the overdue ones: due before today and not Closed.", "List the high-risk findings that are not Closed, first.", "Write one follow-up line for each owner.", "Flag any data problem. Never fix it."],
   "A findings dashboard: tiles for open, overdue and high-risk open; a chart by area; a table by owner; a filter by client.", "Every Sunday at 08:00", "The engagement supervisor", 40),
 "tax": ("Associate, Tax",
   "The tax team keeps one filing calendar: 28 filings for Zakat, NLST, corporate income tax and retention releases. A missed date means a penalty for the client. Every morning someone reads the whole sheet by eye.",
   ["List filings due in the next 14 days that are not Filed, by date.", "List filings past their due date that are not Filed, first.", "List filings with no reviewer.", "Write one reminder line for each preparer.", "Flag any data problem. Never fix it."],
   "A deadline dashboard: due this week, due in 30 days, past due, and status by filing type.", "Every weekday at 08:00", "The tax manager", 20),
 "cf": ("Analyst, Corporate Finance",
   "The Corporate Finance partners review the deal pipeline every Monday: 22 deals, from leads to final reports. The sheet has no totals, no weighted value and no view by stage, so an analyst builds it again every week.",
   ["Total the fee estimates, and the weighted value (fee × probability) by stage.", "List the deals expected to close in the next 30 days.", "List stale deals: the close date has passed and the stage is still Proposal.", "Leave a deal with a blank probability out of the weighted value, and flag it.", "Never guess a probability."],
   "A pipeline dashboard, then a 5-slide update for the partners' meeting.", "Every Monday at 07:30", "The lead partner", 45),
 "risk": ("Consultant, Risk Consulting",
   "A client's board asked Mirqab's risk team for its top risks on one page. The register has 18 risks, but the scores were typed by hand, and some risks have not been reviewed for over a year.",
   ["Recalculate every score: likelihood × impact. Show both numbers where they differ.", "List the top risks (recalculated score 15 or more).", "List risks not reviewed in the last 12 months.", "List risks with no owner.", "Flag problems. Never change the register."],
   "A heat map (likelihood by impact), then a one-page summary for the board.", "On the first Sunday of each month", "The risk consulting manager", 60),
 "cyber": ("Analyst, Cybersecurity",
   "Every Thursday a vulnerability scan of a client's network lists 26 findings. Management wants three answers: what is critical, what is old, and who owns it. Today an analyst sorts the export by hand.",
   ["List open Critical and High findings, Critical first.", "List findings open for more than 30 days.", "Count the open findings by owner.", "Flag any finding whose severity does not match its CVSS score. Do not change either value.", "Use only the scan file."],
   "A severity dashboard, and the top 5 findings to fix this week.", "Every Thursday at 07:00", "The IT security lead", 45),
 "it": ("Coordinator, IT and the Technology Hub",
   "Mirqab's IT manager writes a monthly service report from the helpdesk export: 40 tickets in October. She counts the SLA breaches by hand and copies the numbers into a document.",
   ["Calculate the share of tickets that met the SLA, by priority.", "Count tickets by category.", "List every breach with its hours against the SLA.", "Flag data errors, such as a ticket closed before it was opened.", "Never round or guess hours."],
   "A service dashboard, then a one-page monthly report.", "On the 1st of each month at 08:00", "The IT manager", 60),
 "esg": ("Consultant, ESG and Sustainability",
   "A client needs its first sustainability report. Three sites sent 12 months of electricity, diesel, water and waste data. Nobody has checked it yet.",
   [f"Calculate emissions by site and month with the training factors: electricity {X.EF['electricity']} kg CO2e per kWh, diesel {X.EF['diesel']} kg CO2e per litre.",
    "Total water and waste by site.", "Flag gaps: never fill a blank with an average.", "Flag outliers, such as a value about 1,000 times lower than the other months. Never convert it.", "Say which months are complete."],
   "An emissions dashboard by site and month, then a 5-slide summary for the client's board.", "On the 5th of each month", "The ESG manager", 90),
 "data": ("Analyst, AI and Data Analytics",
   "A retail client sent one month of sales: 60 transactions from 4 branches. Before any analysis, the client wants to know if the data can be trusted.",
   ["Check the data first: duplicate transactions, and Amount equal to Quantity × Unit price.", "Write a short data-quality note on top.", "Then report sales by branch, by category and by week, with duplicates counted once.", "Flag every problem. Never correct a value.", "Use only the file."],
   "A sales dashboard with filters, with the data-quality note on top.", "Every Sunday at 09:00", "The analytics manager", 60),
 "finance": ("Accountant, Finance",
   "Every month Mirqab's finance team explains the budget variances to the managing partner, line by line, in a long email: 40 lines across 4 cost centers.",
   ["Calculate the variance for every line, in KWD and in percent.", "Flag lines more than 10% and more than KWD 1,000 over budget.", "Draft one question for each flagged line.", "Flag a blank actual. Never treat it as zero.", "Use only the file."],
   "A variance dashboard by cost center, then a one-page memo to the managing partner.", "On the 3rd working day of each month", "The finance manager", 50),
 "hr": ("Officer, Human Resources",
   "HR answers the same questions every month: headcount, training hours, leave balances and who is on notice. The people file has 36 employees, with IDs only.",
   ["Count headcount by department and by grade.", "List employees under the 20-hour training target.", "List leave balances to check, such as a negative balance.", "Flag data errors, such as a join date in the future.", "Use employee IDs only. Never add names."],
   "An HR dashboard, then a one-page monthly note for the partners.", "On the last working day of each month", "The HR manager", 45),
 "cx": ("Coordinator, Customer Experience",
   "Client feedback arrives every week: 40 responses with a score from 0 to 10 and a comment. Nobody turns it into a score or a list of what to fix.",
   ["Calculate the NPS by service line: promoters (9 and 10) minus detractors (0 to 6).", "Leave out scores outside 0 to 10, and flag them.", "Count a duplicate response once, and flag it.", "Group the comments into themes.", "List the three things to fix first."],
   "An NPS dashboard, then a 5-slide client-feedback deck.", "Every Sunday at 08:00", "The client service partner", 40),
}
OWN = ("Your own team",
   "Bring a task you repeat at work. Use fictional data only: no client names, no real figures. If you have no file, use the test file you made in Task 2.1, or ask Claude for one with the Make a test file prompt.",
   ["Read the input file.", "Do the steps of your task, with your rules.", "Flag anything missing or strange. Never guess.", "Return the output in a fixed layout."],
   "A dashboard, a report or a short deck: you choose.", "[when it should run]", "[one person's role]", 30)

def card(key):
    if key == "own":
        role, scen, must, art, when, rev, mins = OWN
        return CD.PROJECT_CARD
    p = {q["key"]: q for q in X.PACKS}[key]; role, scen, must, art, when, rev, mins = SCEN[key]
    return (f"Department: {p['dept']}\n"
            f"Task: {p['agent']}\n"
            f"Input: {p['file']} (today it lives inside the skill)\n"
            f"Instruction: [your steps and two rules; what to do when unsure]\n"
            f"Output: {art}\n"
            f"When: {when}\n"
            f"Who reviews: {rev} [name]\n"
            f"Impact: [{mins} minutes by hand] - [minutes with the agent] x [runs a month]")

def promptbox(pid, label, text):
    return (f'<div class="sh-plab">{e(label)}</div><div class="sh-promptwrap"><pre id="{pid}">{e(text)}</pre>'
            f'<button class="sh-copy" type="button" data-copy="{pid}">COPY</button></div>')

def panel(key):
    if key == "own":
        role, scen, must, art, when, rev, mins = OWN; dept = "Your own task"; files = ""
    else:
        p = {q["key"]: q for q in X.PACKS}[key]; role, scen, must, art, when, rev, mins = SCEN[key]; dept = p["dept"]
        files = (f'<div><b class="sh-lab">Your file</b><div class="sh-files"><a href="{e(p["file"])}" download>{e(p["file"])}</a></div>'
                 f'<p class="pj-small">{len(p["rows"])} rows · {e(", ".join(p["head"]))}</p></div>')
    hidden = ('<p class="pj-hidden"><b>Heads up:</b> this file hides two problems. A good agent finds and flags them. It never fixes them.</p>' if key != "own" else "")
    return f'''<section class="sh-card pj-panel" id="pj-{key}" data-dept="{key}" hidden>
  <div class="sh-top"><span class="sh-blk">Your scenario</span><span class="sh-time">{e(role)}</span><span class="sh-tag sh-team">Task 2.6 · 85 min</span></div>
  <h3>{e(dept)}</h3>
  <p class="pj-scen">{e(scen)}</p>
  <p class="pj-goal"><b>Your job today:</b> build an agent that does this work for the team, shows the result as an artifact, and runs on a schedule. A person still reviews every run.</p>
  {hidden}
  <div class="sh-meta sh-meta--3">
    {files}
    <div><b class="sh-lab">The artifact</b>{e(art)}</div>
    <div><b class="sh-lab">When and who</b>{e(when)}. Reviewed by {e(rev[0].lower() + rev[1:])}.</div>
  </div>
  <div class="sh-plab">What the agent must do</div>
  <ul class="pj-must">{"".join(f"<li>{e(m)}</li>" for m in must)}</ul>
  {promptbox(f"card-{key}", "Your Project card (copy it, then fill the brackets)", card(key))}
</section>'''

STEPS = [("Card", 10, "Pick your department above and copy your Project card into Claude or a document. Fill the brackets."),
         ("Build", 25, "In Claude, create a Project named after your department. Ask Claude for a build plan from your card. Write the five-part instructions in the Project. Then turn the Project into a skill, and save it."),
         ("Output", 20, "Attach your file in the Project. Write your own dashboard request with your department's KPIs. Check three tiles by hand. Then send Put the layout in my skill and save the skill again."),
         ("When", 15, "Send Add my file to the skill, and save the skill again. Click Scheduled in the left sidebar, New task, Set up manually. Paste the Scheduled task prompt. Run it once on demand."),
         ("Check and demo", 15, "Ask Claude where three figures come from, and check them in the file. Mark the output DRAFT with a Reviewed by line. Work out your impact. Plan a 3-minute demo in your own words.")]
# write these yourself first: hint, another hint, then the prompt (Aya, 16 Nov 10:02)
LAYERED = [
 ("Build plan", "Step 2: before you build anything.",
  "Look at your Project card. Each line is one part of the build: Input is the file, Instruction is the Project, Output is the artifact, When is the schedule.",
  "Give Claude your card and ask for a plan, not the build: five short steps in order (Project, skill, artifact, schedule, test).", CD.BUILD_PLAN),
 ("Turn the Project into a skill", "Step 2: after the Project gives a good result.",
  "Think back to Task 2.1. A skill needs a short name, one line on when to use it, the steps, the rules, the output columns, and what to do when unsure.",
  "Paste your Project card and ask Claude to ask you questions first. Then ask it to write the skill with those six parts as a file you can save.", CD.SKILL_FROM_CARD),
 ("Dashboard request", "Step 3: with your file attached.",
  "Use the five parts from Lesson 2: who reads it, which data, the KPIs with their formulas, the layout, and the rules.",
  "Your KPIs are in What the agent must do: turn each line into a tile (a count or a total). Add the rule: list blanks under Data issues and never guess.", CD.DASH_TEMPLATE),
 ("Check three figures", "Step 5: before you trust the output.",
  "You need three numbers from the output, and where each one comes from in the file.",
  "Ask Claude to show the exact rows behind each number and to change nothing. Then check them yourself in Excel with a filter or SUM.", CD.CHECK3),
 ("Demo script", "Step 5: for the demos at 14:40.",
  "Four minutes: the problem, your card, a run or your artifact, your impact number, and what you would automate next.",
  "Impact is (minutes by hand minus minutes with the agent) times runs a month. Use only numbers from your files and your runs.", CD.DEMO_SCRIPT)]
# copy these: they are steps to follow, not thinking
PROMPTS = [("Put the layout in my skill", CD.ARTIFACT_IN_SKILL), ("Add my file to the skill", CD.ADD_TO_SKILL), ("Scheduled task prompt", CD.SKILL_SCHED)]
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScjFXZ-xs_VUAvfXrdxP5ccN6zkgv_gMx3UIlcIyh633pVbMQ/viewform"
SUBMIT_ITEMS = ["Your name and your department.", "Your Project card, filled in.",
                "Your skill: its name and its one-line description.",
                "A link to your artifact. In Claude, share or publish the artifact and copy its link. No link option on your account? Add a screenshot instead.",
                "Your scheduled task: its name, how often it runs, and the first line of its run.",
                "Three figures you checked, and the rows they come from in the file.", "The two hidden problems your agent flagged.",
                "Your impact number, and the next task you would automate."]
SUBMIT_PROMPT = ("Put together my mini project submission as a Word document I can download. Use only what is in this chat and this Project. "
                 "Sections in this order: 1. My name and department: [name, department]. 2. My Project card. "
                 "3. My skill: name and one-line description. 4. The artifact link: [paste the link, or write Screenshot attached]. "
                 "5. My scheduled task: name, frequency, and the first line of its run. 6. Three figures I checked, with their rows in the file. "
                 "7. The problems the agent flagged. 8. My impact: (minutes by hand minus minutes with the agent) times runs a month, and my next task to automate. "
                 "Where you do not have something, write [missing] so I can fill it. Do not invent anything.")
LABELS = ["Stuck? Show a hint", "Still stuck? Show another hint", "Still stuck? Show the prompt"]

def layered(i, label, when, h1, h2, text):
    return (f'<div class="pj-layer" id="ly-{i}" data-level="0"><div class="sh-plab">{e(label)}</div><p class="pj-small">{e(when)}</p>'
            f'<div class="pj-h" data-l="1" hidden><b>Hint 1.</b> {e(h1)}</div>'
            f'<div class="pj-h" data-l="2" hidden><b>Hint 2.</b> {e(h2)}</div>'
            f'<div class="pj-h" data-l="3" hidden>{promptbox(f"lp-{i}", "The prompt", text)}</div>'
            f'<button class="pj-more" type="button">{e(LABELS[0])}</button></div>')
DONE = ["My Project card is filled in.", "My Project has five-part instructions.", "My skill is saved and tested in a new chat.",
        "My dashboard or report has a fixed layout, written in the skill.", "My scheduled task ran once on demand, with a run-log line.",
        "I checked three figures against the file.", "My output says DRAFT and Reviewed by.", "I know my impact number and my 3-minute demo.",
        "I submitted my document in the submission form."]

CSS = """
.pj-pick{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px;margin-top:14px}
.pj-pick button{font:inherit;text-align:left;padding:14px 16px;border-radius:14px;cursor:pointer;color:inherit;background:rgba(255,255,255,.04);border:1px solid rgba(127,140,160,.35);line-height:1.3}
.pj-pick button b{display:block;font-size:16px}.pj-pick button span{display:block;font-size:13px;opacity:.75;margin-top:4px}
.pj-pick button:hover{border-color:#4CB5E2}.pj-pick button[aria-pressed=true]{background:#007DB4;border-color:#007DB4;color:#fff}
.pj-empty{margin:18px 0 0;opacity:.8}
.pj-scen{font-size:18px;line-height:1.6;margin:6px 0 10px}.pj-goal{margin:0 0 10px}
.pj-hidden{padding:10px 14px;border-radius:12px;border:1px dashed #4CB5E2;margin:0 0 12px}
.pj-must{margin:6px 0 14px 20px;line-height:1.6}.pj-small{font-size:13px;opacity:.75;margin:6px 0 0}
.pj-steps{counter-reset:s;list-style:none;margin:10px 0 0;padding:0;display:grid;gap:10px}
.pj-steps li{padding:14px 16px;border-radius:14px;border:1px solid rgba(127,140,160,.3);line-height:1.55}
.pj-steps li b{color:#4CB5E2;margin-right:6px}
.pj-done label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;line-height:1.45}
.pj-layer{padding:16px 18px;border-radius:14px;border:1px solid rgba(127,140,160,.3);margin:12px 0}
.pj-layer .sh-plab{margin-top:0}.pj-h{margin:10px 0 0;padding:10px 14px;border-radius:12px;background:rgba(76,181,226,.08);line-height:1.55}
.pj-more{font:inherit;font-size:14px;margin-top:12px;padding:8px 16px;border-radius:999px;cursor:pointer;color:inherit;background:transparent;border:1px solid #4CB5E2}
.pj-more:hover{background:#007DB4;border-color:#007DB4;color:#fff}
.pj-submit a.pj-go{display:inline-flex;align-items:center;gap:8px;margin:16px 0 4px;padding:12px 22px;border-radius:999px;background:#007DB4;color:#fff;font-weight:700;text-decoration:none}
.pj-submit a.pj-go:hover{filter:brightness(1.1)}.pj-submit ol{margin:6px 0 14px 20px;line-height:1.6}
.pj-note textarea{width:100%;min-height:150px;margin-top:8px;font:inherit;padding:12px;border-radius:12px}
"""

JS = """<script>(function(){
var KEY='coded-rsm-ai-automation-mini-project';var st={dept:'',done:{},note:'',ly:{}};
try{var v=localStorage.getItem(KEY);if(v){var p=JSON.parse(v);st.dept=p.dept||'';st.done=p.done||{};st.note=p.note||'';st.ly=p.ly||{};}}catch(x){}
var LB=["Stuck? Show a hint","Still stuck? Show another hint","Still stuck? Show the prompt"];
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(x){}}
var btns=[].slice.call(document.querySelectorAll('.pj-pick button')),panels=[].slice.call(document.querySelectorAll('.pj-panel')),empty=document.querySelector('.pj-empty');
function show(k,scroll){var hit=false;panels.forEach(function(p){var on=p.getAttribute('data-dept')===k;p.hidden=!on;if(on)hit=true;});
  btns.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-dept')===k?'true':'false');});
  if(empty)empty.hidden=hit;if(hit){st.dept=k;save();if(history.replaceState)history.replaceState(null,'','#'+k);
  if(scroll){var el=document.getElementById('pj-'+k);if(el)el.scrollIntoView({behavior:'smooth',block:'start'});}}}
btns.forEach(function(b){b.addEventListener('click',function(){show(b.getAttribute('data-dept'),true);});});
var h=(location.hash||'').replace('#','');show(h||st.dept,false);
[].slice.call(document.querySelectorAll('.pj-done input')).forEach(function(c,i){c.checked=!!st.done[i];c.addEventListener('change',function(){st.done[i]=c.checked;save();});});
function lay(box,n){box.setAttribute('data-level',n);[].slice.call(box.querySelectorAll('.pj-h')).forEach(function(h){h.hidden=+h.getAttribute('data-l')>n;});
  var b=box.querySelector('.pj-more');if(n>=3){b.hidden=true;}else{b.hidden=false;b.textContent=LB[n];}}
[].slice.call(document.querySelectorAll('.pj-layer')).forEach(function(box){lay(box,+(st.ly[box.id]||0));
  box.querySelector('.pj-more').addEventListener('click',function(){var n=Math.min(3,+box.getAttribute('data-level')+1);st.ly[box.id]=n;save();lay(box,n);});});
var ta=document.querySelector('.pj-note textarea');if(ta){ta.value=st.note;ta.addEventListener('input',function(){st.note=ta.value;save();});}
document.addEventListener('click',function(ev){var b=ev.target.closest('[data-copy]');if(!b)return;var t=document.getElementById(b.getAttribute('data-copy'));if(!t)return;var txt=t.innerText;
  function done(){b.textContent='COPIED';setTimeout(function(){b.textContent='COPY';},1500);}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){fb();});}else fb();
  function fb(){var a=document.createElement('textarea');a.value=txt;document.body.appendChild(a);a.select();try{document.execCommand('copy');done();}catch(x){}document.body.removeChild(a);}});
})();</script>"""

def build(out_dir):
    picks = "".join(f'<button type="button" data-dept="{p["key"]}" aria-pressed="false"><b>{e(p["dept"])}</b><span>{e(SCEN[p["key"]][0].split(", ")[0])} · {e(p["sheet"])}</span></button>' for p in X.PACKS)
    picks += '<button type="button" data-dept="own" aria-pressed="false"><b>Your own task</b><span>Fictional data only</span></button>'
    panels = "\n".join(panel(p["key"]) for p in X.PACKS) + "\n" + panel("own")
    steps = "".join(f"<li><b>{i}. {e(t)} · {m} min</b>{e(x)}</li>" for i, (t, m, x) in enumerate(STEPS, 1))
    layers = "".join(layered(i, *x) for i, x in enumerate(LAYERED))
    prompts = "".join(promptbox(f"pp-{i}", l, t) for i, (l, t) in enumerate(PROMPTS))
    done = "".join(f'<label><input type="checkbox"> <span>{e(x)}</span></label>' for x in DONE)
    logos = (f'<span class="lk"><img class="coded-logo" src="{PFX}-coded-logo.png" alt="CODED" width="320" height="120"><span class="x">×</span>'
             f'<img class="partner-logo" src="{PFX}-client-logo.png" alt="RSM Albazie &amp; Co." width="192" height="192"></span>')
    title = "Mini project · Day 2 · AI Innovation and Automation · CODED × RSM"
    page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="Day 2 mini project: pick a department, get the scenario and the file, and build its agent.">
<meta name="theme-color" content="#00112F">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{PFX}-favicon.png" type="image/png">
<link rel="stylesheet" href="{PFX}-site.css">
<style>{CSS}</style>
</head><body>
<main><div class="wrap"><div class="topbar"><a class="back" href="{PFX}.html"><span class="ar">←</span> AI Innovation and Automation · both days</a><nav class="daynav" aria-label="Pages"><a href="{PFX}-day-1.html">Day 1</a><a href="{PFX}-day-2.html">Day 2</a><a href="{PFX}-lab-day-2.html">Day 2 lab</a><a href="{PFX}-prompt-sheet-day-2.html">Prompts</a></nav></div></div>
<div class="wrap hero-wrap"><div class="d-hero h-d2"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span> Day 2 · mini project</span><div class="d-logos">{logos}</div></div>
<h1>Your department's agent</h1><p class="lede">Pick a department. You get a work scenario, the file, what the agent must do and a Project card filled in for you. Then build it in 85 minutes, on your own or in pairs.</p></div></div>
<div class="wrap"><div class="sheet">
<section class="sh-card"><div class="sh-top"><span class="sh-blk">Step 0</span><span class="sh-time">1 minute</span></div><h3>Pick your department</h3>
<div class="pj-pick">{picks}</div><p class="pj-empty">Pick a department to see your scenario and your file.</p></section>
{panels}
<section class="sh-card"><div class="sh-top"><span class="sh-blk">The plan</span><span class="sh-time">85 minutes</span></div><h3>Build in this order</h3><ol class="pj-steps">{steps}</ol>
<p class="pj-small">Behind at 45 minutes? Skip the schedule. Show the skill and the artifact, and say when it would run.</p></section>
<section class="sh-card"><div class="sh-top"><span class="sh-blk">Write it yourself</span><span class="sh-time">hints if you are stuck</span></div><h3>Write these requests yourself first</h3>
<p class="pj-small">You wrote each of these once today. Try on your own for a few minutes. Stuck? Open one hint at a time. The full prompt is the last step.</p>{layers}</section>
<section class="sh-card"><div class="sh-top"><span class="sh-blk">Copy these</span><span class="sh-time">COPY, then fill the brackets</span></div><h3>Steps to follow</h3>{prompts}</section>
<section class="sh-card pj-submit"><div class="sh-top"><span class="sh-blk">Submit</span><span class="sh-time">before 14:40</span></div><h3>Submit your project</h3>
<p>Send one Word document through the submission form. Read what goes in it first, build it with the prompt, then open the form.</p>
<div class="sh-plab">Your document has</div><ol>{"".join(f"<li>{e(x)}</li>" for x in SUBMIT_ITEMS)}</ol>
{promptbox("pp-submit", "Make my submission document (in your Project chat)", SUBMIT_PROMPT)}
<p class="pj-small">Check the document before you send it: every number must match your files, and no real client names.</p>
<a class="pj-go" href="{FORM}" target="_blank" rel="noopener">Open the submission form <span class="ar">→</span></a>
<p class="pj-small">Short link: coded-rsm.vercel.app/submit</p></section>
<section class="sh-card pj-done"><div class="sh-top"><span class="sh-blk">Before the demos</span><span class="sh-time">14:40</span></div><h3>Done when</h3>{done}
<p class="pj-small">The trainer picks four or five projects to show: four minutes each. Your ticks stay in this browser.</p></section>
<p class="smallnote sheet-foot">{e(X.FICTION)} <a href="{PFX}-day-2.html">Back to Day 2</a></p>
</div></div></main>
<footer class="foot-mini"><div class="wrap"><div class="foot-row"><a class="f-lockup" href="{PFX}.html" aria-label="AI Innovation and Automation home">{logos}</a><span class="copy">© 2026 CODED × RSM · {e(X.FICTION)}</span></div></div></footer>
{JS}
</body></html>
'''
    with open(os.path.join(out_dir, FILE), "w", encoding="utf-8") as f:
        f.write(page)
