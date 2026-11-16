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
   "Bring a task you repeat at work. Use fictional data only: no client names, no real figures. No file? Use the test file you made this morning, or make one with the Make a test file prompt in step 1.",
   ["Read the input file.", "Do the steps of your task, with your rules.", "Flag anything missing or strange. Never guess.", "Return the output in a fixed layout."],
   "A dashboard, a report or a short deck: you choose.", "[when it should run]", "[one person's role]", 30)

# per department: the skill name, runs a month (for the impact line), and whether the second output is slides or a one-page note
SKILL = {"audit": "audit-findings-followup", "tax": "tax-filing-deadlines", "cf": "cf-pipeline-review", "risk": "risk-register-review",
         "cyber": "vuln-scan-triage", "it": "it-service-report", "esg": "esg-emissions-check", "data": "sales-data-check",
         "finance": "budget-variance-review", "hr": "hr-monthly-numbers", "cx": "client-nps-review"}
RUNS = {"audit": 4, "tax": 22, "cf": 4, "risk": 1, "cyber": 4, "it": 1, "esg": 1, "data": 4, "finance": 1, "hr": 1, "cx": 4}

def info(key):
    """Everything one panel needs, for a department pack or the trainee's own task."""
    if key == "own":
        role, scen, must, art, when, rev, mins = OWN
        return dict(key=key, dept="Your own task", role=role, scen=scen, must=must, art=art, when="[when it should run, for example every Sunday at 08:00]",
                    rev="[one person's role]", mins="[minutes by hand]", runs="[runs a month]", skill="[your skill name]", file="[your file name]",
                    agent="[what the agent does, in one line]", project="[your task] agent", second="a 5-slide presentation or a one-page note")
    p = {q["key"]: q for q in X.PACKS}[key]; role, scen, must, art, when, rev, mins = SCEN[key]
    return dict(key=key, dept=p["dept"], role=role, scen=scen, must=must, art=art, when=when, rev=rev, mins=mins, runs=RUNS[key],
                skill=SKILL[key], file=p["file"], agent=p["agent"], project=f"{p['dept']} agent", p=p,
                second="a 5-slide presentation" if "slide" in art else "a one-page note")

def card(d):
    if d["key"] == "own":
        return ("Department: [your team]\n"
                "Task: [what the agent does, in one line]\n"
                "Skill name: [short, lowercase, with hyphens, for example lease-key-terms]\n"
                "Input: [the file it reads; today it lives inside the skill]\n"
                "Instruction: [the steps in order, two rules, and what to do when unsure]\n"
                "Output: [a dashboard, a report or a deck, and what is on it]\n"
                "When: [for example every Sunday at 08:00]\n"
                "Who reviews: [one person's role]\n"
                "Impact: ([minutes by hand] - [minutes to review the draft]) x [runs a month]")
    return (f"Department: {d['dept']}\n"
            f"Task: {d['agent']}\n"
            f"Skill name: {d['skill']}\n"
            f"Input: {d['file']} (today it lives inside the skill)\n"
            f"Instruction: the steps in What the agent must do. Rules: use only the file; flag every problem, never fix it. When unsure: write Not found, never guess.\n"
            f"Output: {d['art']}\n"
            f"When: {d['when']}\n"
            f"Who reviews: {d['rev']}\n"
            f"Impact: ({d['mins']} minutes by hand - [minutes to review the draft]) x {d['runs']} runs a month")

def instructions(d):
    if d["key"] == "own":
        return ("Role: You are a [job title] at Mirqab & Co. You [the task in one line].\n"
                "Steps:\n1. Read the attached file.\n2. [find, compare or calculate what]\n3. [decide or flag what]\n"
                "Rules:\n- Use only the file in this Project. Calculate with code.\n- [your rule, for example dates as YYYY-MM-DD]\n- [your rule, for example what counts as a difference]\n"
                "Output format: [table columns, in order]. Put a short Data issues list first.\n"
                "When unsure: If a value is blank or unclear, write Not found and flag it. Never guess. Never change a value in the file.")
    steps = "\n".join(f"{i}. {m}" for i, m in enumerate(d["must"], 2))
    job, team = d["role"].split(", ", 1); job = job.lower(); art_ = "an" if job[0] in "aeiou" else "a"
    return (f"Role: You are {art_} {job} in {team} at Mirqab & Co.\nYour task: {d['agent']}\n"
            f"Steps:\n1. Read {d['file']} in this Project.\n{steps}\n"
            "Rules:\n- Use only the file in this Project. Calculate with code.\n- Show the row ID from the file for every item you list.\n"
            "Output format: First a short Data issues list. Then one table for each step, in the order above.\n"
            "When unsure: If a value is blank or unclear, write Not found and flag it. Never guess. Never change a value in the file.")

def promptbox(pid, label, text):
    return (f'<div class="sh-plab">{e(label)}</div><div class="sh-promptwrap"><pre id="{pid}">{e(text)}</pre>'
            f'<button class="sh-copy" type="button" data-copy="{pid}">COPY</button></div>')

LABELS = ["Stuck? Show a hint", "Still stuck? Show another hint", "Still stuck? Show the prompt"]
def layered(pid, label, h1, h2, text):
    return (f'<div class="pj-layer" id="ly-{pid}" data-level="0"><div class="sh-plab">Write it yourself: {e(label)}</div>'
            f'<div class="pj-h" data-l="1" hidden><b>Hint 1.</b> {e(h1)}</div>'
            f'<div class="pj-h" data-l="2" hidden><b>Hint 2.</b> {e(h2)}</div>'
            f'<div class="pj-h" data-l="3" hidden>{promptbox(f"lp-{pid}", "The prompt", text)}</div>'
            f'<button class="pj-more" type="button">{e(LABELS[0])}</button></div>')

def step(n, name, mins, todo, body):
    return (f'<section class="sh-card pj-step"><div class="sh-top"><span class="sh-blk">Step {n}</span><span class="sh-time">{mins} min</span></div>'
            f'<h3>{e(name)}</h3><ol class="pj-todo">{"".join(f"<li>{x}</li>" for x in todo)}</ol>{body}</section>')

def panel(key):
    d = info(key); k = key; own = key == "own"; sk = d["skill"]; fl = d["file"]
    if own:
        files = ""
        hidden = ""
    else:
        p = d["p"]
        files = (f'<div><b class="sh-lab">Your file</b><div class="sh-files"><a href="{e(fl)}" download>{e(fl)}</a></div>'
                 f'<p class="pj-small">{len(p["rows"])} rows · {e(", ".join(p["head"]))}</p></div>')
        hidden = '<p class="pj-hidden"><b>Heads up:</b> this file hides two problems. A good agent finds and flags them. It never fixes them.</p>'
    head = f"""<section class="sh-card">
  <div class="sh-top"><span class="sh-blk">Your scenario</span><span class="sh-time">{e(d['role'])}</span><span class="sh-tag sh-team">Task 2.6 · 85 min</span></div>
  <h3>{e(d['dept'])}</h3>
  <p class="pj-scen">{e(d['scen'])}</p>
  <p class="pj-goal"><b>Your job today:</b> build an agent that does this work for the team, shows the result as an artifact, and runs on a schedule. A person still reviews every run. Everything you need is on this page, in five steps.</p>
  {hidden}
  <div class="sh-meta sh-meta--3">
    {files}
    <div><b class="sh-lab">The artifact</b>{e(d['art'])}</div>
    <div><b class="sh-lab">When and who</b>{e(d['when'])}. Reviewed by {e(d['rev'][0].lower() + d['rev'][1:]) if not own else e(d['rev'])}.</div>
  </div>
  <div class="sh-plab">What the agent must do</div>
  <ul class="pj-must">{"".join(f"<li>{e(m)}</li>" for m in d['must'])}</ul>
</section>"""
    # step 1 · card
    if own:
        guide = ('<div class="pj-fill"><b>Fill every bracket.</b> Use fictional data only: no client names, no real figures.'
                 '<ul><li><b>Task:</b> one line, for example Reads the lease agreements and lists the key terms.</li>'
                 '<li><b>Skill name:</b> two to four words, lowercase, with hyphens.</li>'
                 '<li><b>Instruction:</b> the steps in order, two rules (for example dates as YYYY-MM-DD), and what to do when unsure.</li>'
                 '<li><b>Output:</b> what the reader sees, for example tiles for the totals and a table of the items to check.</li>'
                 '<li><b>When:</b> a day and a time. <b>Who reviews:</b> a role, for example the engagement manager.</li>'
                 '<li><b>Impact:</b> minutes by hand today, minutes to review the agent\'s draft (write 10 until you know), and how many times a month it runs.</li></ul></div>')
        s1todo = ["Copy the Project card below into a Word document or a note. Fill every bracket, using the guide under the card.",
                  "No file for your task? In Claude, click New chat and send Make a test file. Download the file it makes."]
        s1extra = promptbox(f"{k}-test", "Make a test file", "Make a fictional test file for this task: [your task, in one line]. Make it [file type, for example an Excel sheet] with 10 to 15 rows and 2 planted problems an agent should flag. Use made-up names and amounts only. Do not tell me where the problems are.")
    else:
        guide = ('<div class="pj-fill"><b>Only one bracket to fill:</b> [minutes to review the draft]: how long you need to check the agent\'s work. '
                 'Write 10 for now. After your run in step 4, change it to your real time. Everything else is filled in for you.</div>')
        s1todo = ["Read your scenario and What the agent must do above.",
                  "Copy your Project card below into a Word document or a note. You will paste it into Claude in step 2 and into your submission."]
        s1extra = ""
    s1 = step(1, "Your Project card", 10, s1todo, promptbox(f"{k}-card", "Your Project card", card(d)) + guide + s1extra)
    # step 2 · build
    plan = layered(f"{k}-0", "a build plan (optional)",
                   "Look at your Project card. Each line is one part of the build: Input is the file, Instruction is the Project, Output is the artifact, When is the schedule.",
                   "Give Claude your card and ask for a plan, not the build: five short steps in order (Project, skill, artifact, schedule, test).", CD.BUILD_PLAN)
    skillp = ("Turn this Project into a Claude skill. Here is my Project card: [paste your card]. Use the skill name on the card. "
              "Ask me up to three questions first. Then write the skill: the name, a one-line description that names the task and the file type, "
              "the steps, the rules, the output columns in order, and When unsure (write Not found, never guess). Make it a skill file I can save.")
    sk_layer = layered(f"{k}-1", "turn the Project into a skill",
                       "A skill needs six parts: a short name, one line on when to use it, the steps, the rules, the output columns, and what to do when unsure.",
                       "In the Project chat, paste your Project card. Ask Claude to ask you questions first, then to write the skill with those six parts as a file you can save.", skillp)
    s2todo = ["In Claude, click Projects in the left sidebar, then + New Project. Name it " + (f"<b>{e(d['project'])}</b>" if not own else "after your task, for example Lease terms agent") + " and create it.",
              "Click Set project instructions. Paste Project instructions below" + (". Fill the brackets." if own else ".") + " Save.",
              f"Click + in the project knowledge and add {'<b>' + e(fl) + '</b>' if not own else 'your file'}.",
              "Start a chat in the Project. Send Run it, below. Check the result against What the agent must do. Not right? Fix the instructions, not the result.",
              "Turn the Project into a skill: write the request yourself in the same chat (hints below). When Claude shows the skill, save it. Check it is listed: Customize, then Skills."]
    s2 = step(2, "Build: a Project, then a skill", 25, s2todo,
              plan + promptbox(f"{k}-instr", "Project instructions", instructions(d)) +
              promptbox(f"{k}-run", "Run it (in the Project chat)", "Run the task on the file in this Project. Follow the instructions exactly.") + sk_layer +
              '<p class="pj-small">The skill will not save? Check that code execution is on: Settings, then Capabilities. Then try again.</p>')
    # step 3 · output
    dash = layered(f"{k}-2", "the dashboard request",
                   "Your request needs five things: who reads it, which data, the KPIs with their formulas, the layout, and the rules.",
                   "Your KPIs are in What the agent must do: turn each line into a tile (a count or a total). Add the rule: list blanks under Data issues and never guess.", CD.DASH_TEMPLATE)
    second = (f"Turn this dashboard into {d['second']} for {d['rev'][0].lower() + d['rev'][1:] if not own else '[who reads it]'}: a title and the date of the data, the key numbers, "
              "what needs attention, the data issues, and the next step. Use only the dashboard's figures. Nothing new, nothing rounded differently.")
    layout = (f"Add this to my {sk} skill: after the analysis, always build the dashboard in the same layout as the dashboard in this chat: "
              "the same KPI tiles, charts, table and filter, in the same order. Write that layout into the skill as a list. "
              "Keep every other rule word for word. Then update the skill so I can save it again.")
    s3todo = ["In the Project chat, write your dashboard request (hints below). Your KPIs come from What the agent must do.",
              "Check three KPI tiles by hand in Excel, with a filter, SUM or COUNTIF. Then send Check the dashboard.",
              f"Your artifact also has {'slides' if d['second'].startswith('a 5') else 'a one-page note'}? Send Second output.",
              "Send Put the layout in my skill. Save the skill again when Claude shows it."]
    s3 = step(3, "Output: the artifact", 20, s3todo,
              dash + promptbox(f"{k}-chk", "Check the dashboard", CD.DASH_CHECK) + promptbox(f"{k}-2nd", "Second output", second) +
              promptbox(f"{k}-lay", "Put the layout in my skill", layout))
    # step 4 · when
    addf = f"Add the attached file to my {sk} skill as a reference file. Keep every rule word for word. Then update the skill so I can save it again."
    sched = (f"Use the {sk} skill on its reference file {fl}. Build the output in its fixed layout. Start with one line: "
             "date and time of this run, file read, items flagged. Mark it DRAFT and end with Reviewed by: ____. "
             "If the reference file is missing or cannot be read, say so in that first line and stop. Never guess.")
    fields = (f'<div class="sh-plab">Scheduled task fields</div><table class="pj-tbl"><tr><th>Name</th><td>{e(d["project"])}</td></tr>'
              f'<tr><th>Prompt</th><td>Scheduled task prompt, below</td></tr><tr><th>Frequency</th><td>{e(d["when"])}</td></tr></table>')
    s4todo = [f"In Claude, click New chat (outside the Project). Attach {'<b>' + e(fl) + '</b>' if not own else 'your file'}. Send Add my file to the skill. Save the skill again.",
              "Click Scheduled in the left sidebar, then New task, then Set up manually.",
              "Fill the form with the fields below. Paste the Scheduled task prompt" + (". Fill the brackets." if own else ".") + " Save.",
              "Run it once on demand. Open the run on the Scheduled page: read the first line, then the output."]
    s4 = step(4, "When: a scheduled task", 15, s4todo,
              promptbox(f"{k}-add", "Add my file to the skill", addf) + fields + promptbox(f"{k}-sch", "Scheduled task prompt", sched) +
              '<p class="pj-small">No option for your day or time? Use Create with Claude and say the schedule. The skill will not save with the file? Run the prompt in a chat with the file attached, and say when it would run.</p>')
    # step 5 · check and demo
    chk = layered(f"{k}-3", "check three figures",
                  "You need three numbers from the output, and where each one comes from in the file.",
                  "Ask Claude to show the exact rows behind each number and to change nothing. Then check them yourself in Excel with a filter or SUM.", CD.CHECK3)
    draft = f"Add one line at the top of the dashboard: DRAFT · Reviewed by: ____ ({d['rev'][0].lower() + d['rev'][1:] if not own else '[role]'}). Change nothing else."
    if own:
        impact = "Impact: ([minutes by hand] - [minutes to review the draft]) x [runs a month] = [minutes saved a month]"
        example = "Example: (40 - 10) x 4 = 120 minutes a month."
    else:
        impact = f"Impact: ({d['mins']} - [minutes to review the draft]) x {d['runs']} = [minutes saved a month]"
        example = f"Example: if the review takes 10 minutes, ({d['mins']} - 10) x {d['runs']} = {(d['mins'] - 10) * d['runs']:,} minutes a month."
    outline = ("1. The problem (30 seconds): who does this work today, and how long it takes.\n"
               "2. My card (30 seconds): the task, the file, the schedule, the reviewer.\n"
               "3. A run or my artifact (90 seconds): the first line of the run, the dashboard, one problem the agent flagged.\n"
               "4. My impact (30 seconds): (minutes by hand - minutes to review) x runs a month.\n"
               "5. Next (30 seconds): the next task I would automate.")
    demo = layered(f"{k}-4", "a full demo script (optional)",
                   "Four minutes: the problem, your card, a run or your artifact, your impact number, and what you would automate next.",
                   "Use only numbers from your files and your runs. Ask Claude to keep each part to two or three sentences.", CD.DEMO_SCRIPT)
    s5todo = ["Ask Claude where three figures come from (write it yourself, hints below). Check each one in the file.",
              "Send Mark it DRAFT, so a person signs off every run.",
              "Work out your impact with the line below. Put the number in your Project card.",
              "Plan your 4-minute demo with the demo outline."]
    s5 = step(5, "Check and demo", 15, s5todo,
              chk + promptbox(f"{k}-draft", "Mark it DRAFT", draft) + promptbox(f"{k}-imp", "Your impact line", impact) +
              f'<p class="pj-small">{e(example)}</p>' + promptbox(f"{k}-out", "Demo outline (4 minutes)", outline) + demo)
    return f'<div class="pj-panel" id="pj-{k}" data-dept="{k}" hidden>\n{head}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n</div>'

FORM = "https://platform.joincoded.com/sv/rsm-albazie-ai-innovation-and-automation-project-submission"
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
                 "7. The problems the agent flagged. 8. My impact: (minutes by hand minus minutes to review the draft) times runs a month, and my next task to automate. "
                 "Where you do not have something, write [missing] so I can fill it. Do not invent anything.")
LOOK_FOR = [("Task relevance", "A real department task, with an impact number"), ("It works", "Project, skill and artifact; the task runs on demand"),
            ("Source accuracy", "Three figures match the file"), ("Human controls", "DRAFT, your rules, a named reviewer"), ("Test evidence", "A run log, and both hidden problems flagged")]
DONE = ["My Project card is filled in.", "My Project has its instructions and my file.", "My skill is saved and listed under Customize, then Skills.",
        "My dashboard or report has a fixed layout, written in the skill.", "My scheduled task ran once on demand, with a run-log line.",
        "I checked three figures against the file.", "My output says DRAFT and Reviewed by.", "I know my impact number and my 4-minute demo.",
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
.pj-todo{margin:8px 0 6px 20px;line-height:1.6}.pj-todo li{margin:4px 0}
.pj-fill{margin:10px 0 0;padding:12px 14px;border-radius:12px;background:rgba(76,181,226,.08);line-height:1.55}.pj-fill ul{margin:6px 0 0 18px}
.pj-tbl{border-collapse:collapse;margin:6px 0 4px;width:100%}.pj-tbl th,.pj-tbl td{border:1px solid rgba(127,140,160,.3);padding:8px 12px;text-align:left;vertical-align:top}.pj-tbl th{width:130px;opacity:.85}
.pj-panel{display:flex;flex-direction:column;gap:10px}.pj-panel[hidden]{display:none}
.pj-look td,.pj-look th{border:1px solid rgba(127,140,160,.3);padding:8px 12px;text-align:left}.pj-look{border-collapse:collapse;width:100%;margin-top:8px}
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
document.addEventListener('click',function(ev){var b=ev.target.closest('[data-copy]');if(!b)return;var t=document.getElementById(b.getAttribute('data-copy'));if(!t)return;var txt=t.innerText;
  function done(){b.textContent='COPIED';setTimeout(function(){b.textContent='COPY';},1500);}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){fb();});}else fb();
  function fb(){var a=document.createElement('textarea');a.value=txt;document.body.appendChild(a);a.select();try{document.execCommand('copy');done();}catch(x){}document.body.removeChild(a);}});
})();</script>"""

def build(out_dir):
    picks = "".join(f'<button type="button" data-dept="{p["key"]}" aria-pressed="false"><b>{e(p["dept"])}</b><span>{e(SCEN[p["key"]][0].split(", ")[0])} · {e(p["sheet"])}</span></button>' for p in X.PACKS)
    picks += '<button type="button" data-dept="own" aria-pressed="false"><b>Your own task</b><span>Fictional data only</span></button>'
    panels = "\n".join(panel(p["key"]) for p in X.PACKS) + "\n" + panel("own")
    done = "".join(f'<label><input type="checkbox"> <span>{e(x)}</span></label>' for x in DONE)
    look = "".join(f"<tr><th>{e(a)}</th><td>{e(b)}</td></tr>" for a, b in LOOK_FOR)
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
<h1>Your department's agent</h1><p class="lede">Pick a department. You get a work scenario, the file, what the agent must do, and five steps with every template filled in for you. Build it in 85 minutes, on your own or in pairs.</p></div></div>
<div class="wrap"><div class="sheet">
<section class="sh-card"><div class="sh-top"><span class="sh-blk">The plan</span><span class="sh-time">85 minutes</span></div><h3>Five steps, in this order</h3>
<p>1. Your Project card · 10 min &nbsp; 2. Build: a Project, then a skill · 25 min &nbsp; 3. Output: the artifact · 20 min &nbsp; 4. When: a scheduled task · 15 min &nbsp; 5. Check and demo · 15 min</p>
<p class="pj-small">Every template is in your department's steps, filled in for you. The requests you wrote this morning have hints: try first, then open one hint at a time. Behind at 45 minutes? Skip step 4. Show the skill and the artifact, and say when it would run.</p></section>
<section class="sh-card"><div class="sh-top"><span class="sh-blk">Step 0</span><span class="sh-time">1 minute</span></div><h3>Pick your department</h3>
<div class="pj-pick">{picks}</div><p class="pj-empty">Pick a department to see your scenario, your file and your five steps.</p></section>
{panels}
<section class="sh-card"><div class="sh-top"><span class="sh-blk">The demos</span><span class="sh-time">14:40</span></div><h3>What the trainer looks for</h3>
<table class="pj-look">{look}</table><p class="pj-small">The trainer picks four or five projects to show: four minutes each.</p></section>
<section class="sh-card pj-submit"><div class="sh-top"><span class="sh-blk">Submit</span><span class="sh-time">before 14:40</span></div><h3>Submit your project</h3>
<p>Send one Word document through the submission form. Read what goes in it first, build it with the prompt, then open the form.</p>
<div class="sh-plab">Your document has</div><ol>{"".join(f"<li>{e(x)}</li>" for x in SUBMIT_ITEMS)}</ol>
{promptbox("pp-submit", "Make my submission document (in your Project chat)", SUBMIT_PROMPT)}
<p class="pj-small">Check the document before you send it: every number must match your files, and no real client names.</p>
<a class="pj-go" href="{FORM}" target="_blank" rel="noopener">Open the submission form <span class="ar">→</span></a>
<p class="pj-small">Short link: coded-rsm.vercel.app/submit</p></section>
<section class="sh-card pj-done"><div class="sh-top"><span class="sh-blk">Before the demos</span><span class="sh-time">14:40</span></div><h3>Done when</h3>{done}
<p class="pj-small">Your ticks stay in this browser.</p></section>
<p class="smallnote sheet-foot">{e(X.FICTION)} <a href="{PFX}-day-2.html">Back to Day 2</a></p>
</div></div></main>
<footer class="foot-mini"><div class="wrap"><div class="foot-row"><a class="f-lockup" href="{PFX}.html" aria-label="AI Innovation and Automation home">{logos}</a><span class="copy">© 2026 CODED × RSM · {e(X.FICTION)}</span></div></div></footer>
{JS}
</body></html>
'''
    with open(os.path.join(out_dir, FILE), "w", encoding="utf-8") as f:
        f.write(page)
