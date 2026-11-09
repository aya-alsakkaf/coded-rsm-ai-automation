# -*- coding: utf-8 -*-
"""Single source of truth for the program shape: days, blocks, outcomes, cards, MAP test, labs and trainer kit.
CODED × RSM Albazie · AI Innovation and Automation · built from the approved handoff (8 Nov 2026)."""
import data as D
import content_demos as CD

TITLE = "AI Innovation and Automation"
SUBTITLE = "Design an AI agent for real audit work, then make it run on its own"
CODE = "rsm-ai-automation"
BRAND = "CODED × RSM"
TOOL_MODE = "ai"
CLIENT = {"name": "RSM Albazie & Co.", "short": "RSM", "logo": "rsm-logo-white.png", "logo_scale": 1.0,
          "primary": "#007DB4", "light": "#4CB5E2", "secondary": None, "url": "https://www.rsm.global/kuwait"}
DATES = "Sunday 15 and Monday 16 November 2026"
DAYDATE = {1: "Sunday 15 Nov", 2: "Monday 16 Nov"}
HOURS = "08:30-16:00"
VENUE = "CODED, Alsharekh classroom (Frontend Campus)"
TOOL = "Claude"
TOOLS = "Claude: chat, Projects, the Google Drive connector, artifacts, skills and scheduled tasks. n8n as a trainer demo"
NDAYS = 2
AUDIENCE = "18 RSM Albazie staff: Assurance, Corporate Finance, Support and Analytics Advisory"
SAMPLE_NOTE = "All sample files are fictional, made for training. Mirqab & Co. and Abdali Foods are not real companies, and every name, amount and date is made up."
THRU = "Claude does the first pass. You review and sign off."
STORY = "Everything uses Mirqab & Co., a fictional Kuwaiti audit firm, and its fictional client Abdali Foods. Breaks about every hour, lunch with Dhuhr, and an Asr break."

SOURCES = {
 "projects": ("How can I create and manage projects? (Claude Help Center)", "https://support.claude.com/en/articles/9519177"),
 "skills": ("Use skills in Claude (Claude Help Center)", "https://support.claude.com/en/articles/12512180"),
 "connectors": ("Use Google Workspace connectors (Claude Help Center)", "https://support.claude.com/en/articles/10166901"),
 "scheduled": ("Schedule recurring tasks in Cowork (Claude Help Center)", "https://support.claude.com/en/articles/13854387"),
}

OUTCOMES = ["I can explain what generative AI does well and where it can be wrong, and check its output against the source.",
            "I can find the tasks in my work that suit an agent, and describe one as an Agent Card: input, instruction, output and when.",
            "I can build a Claude Project with instructions and knowledge that gives the same, checkable result on every run.",
            "I can connect an agent to a Drive folder and have it return its output in a fixed format.",
            "I can package my method as a skill and run it on a schedule, with a human review step.",
            "I can match each Claude feature to its equivalent in ChatGPT, Microsoft 365 Copilot and Gemini."]

DAYS = {
1: {"title": "Designing AI Agents for Real Work", "claim": "One card, one Project, one agent you can trust.",
    "sub": "Find the task that repeats every week, describe it as an Agent Card, and build it in Claude, one box at a time.",
    "brief": "Day 1 starts with what AI is and where it fails. Then 18 people do the same task and get 18 different tables. You find the tasks worth an agent, write an Agent Card, and build your own agent in Claude: a Project, a Drive folder, a fixed-shape output and a skill.",
    "artifact": "Your own agent: an Agent Card, a Project, a connected folder, a fixed-shape output and a skill",
    "blocks": [("08:30-08:35", "Welcome and sign-in check", "Open claude.ai and the workshop site"),
               ("08:35-08:45", "Pre-MAP test", "10 minutes. Scan the QR code. It also checks your phone"),
               ("08:45-08:52", "Opener: one invoice, two requests", "The same invoice, a weak and a five-part request"),
               ("08:52-09:20", "Lesson 1 · AI foundations", "What AI is, where it fails, the tools, the transfer map · Task 1.1"),
               ("09:20-09:30", "Break", ""),
               ("09:30-10:20", "Lesson 2 · Why chat isn't enough, and finding the work", "Same task, 18 answers · your task inventory · Tasks 1.2 and 1.3"),
               ("10:20-10:30", "Break", ""),
               ("10:30-11:30", "Lesson 3 · Design the agent, then pick your case", "The Agent Card and Projects · Tasks 1.4 and 1.5"),
               ("11:30-12:30", "Lunch and Dhuhr prayer", ""),
               ("12:30-13:20", "Lesson 4 · Build: Instruction", "The five-part instruction · Task 1.6"),
               ("13:20-13:30", "Break", ""),
               ("13:30-14:25", "Lesson 5 · Build: Input and Output", "Connectors and fixed-shape outputs · Tasks 1.7 and 1.8"),
               ("14:25-14:45", "Asr prayer and break", ""),
               ("14:45-15:30", "Lesson 6 · Build: Package", "Skills, the messy sample and the clock · Tasks 1.9 and 1.10"),
               ("15:30-15:40", "Break", ""),
               ("15:40-16:00", "Lesson 7 · Show and tell, and the Day 2 hook", "Team demos and the agent that ran itself")],
    "outcomes": ["Explain why AI can give a <b>confident figure that is wrong</b>, and tick it against the source.",
                 "Find the tasks in your work that suit an agent, and write an <b>Agent Card</b>.",
                 "Build a <b>Claude Project</b> that gives the same, checkable table every run.",
                 "Read from a <b>Drive folder</b> and return a <b>fixed-shape output</b>.",
                 "Package your method as a <b>skill</b> you can share."]},
2: {"title": "Turning Agents into Operational Workflows", "claim": "An agent that runs on time, with a review step, is a workflow.",
    "sub": "Give your team's agent a When: a schedule, new inputs, department rules, a run log and a named reviewer. Then show it at Demo Day.",
    "brief": "Day 2 answers one question: who runs the agent when you are on leave? Your team turns one Day 1 agent into a scheduled workflow that reads new files, follows your department's rules, writes a run log and waits for a person's review. Each team shows its workflow at Demo Day.",
    "artifact": "Your team's scheduled workflow, shown at Demo Day with its impact number",
    "blocks": [("08:30-09:20", "Lesson 1 · From agent to system", "Callback quiz · trigger, steps, output, review · Task 2.1"),
               ("09:20-09:30", "Break", ""),
               ("09:30-10:20", "Lesson 2 · Make it run on its own", "Scheduled tasks · Task 2.2"),
               ("10:20-10:30", "Break", ""),
               ("10:30-11:30", "Lesson 3 · New inputs, outputs and n8n", "Batch 2 and the empty folder · Task 2.3 · the n8n demo"),
               ("11:30-12:30", "Lunch and Dhuhr prayer", ""),
               ("12:30-13:20", "Lesson 4 · Fit it to your department", "Rules, the review step, the run log · Task 2.4"),
               ("13:20-13:30", "Break", ""),
               ("13:30-14:25", "Lesson 5 · Test and prepare the demo", "Impact, the judges' rubric and the failed-run test · Task 2.5"),
               ("14:25-14:45", "Asr prayer and break", ""),
               ("14:45-15:30", "Lesson 6 · Demo Day", "Four teams, eight minutes each, scored"),
               ("15:30-15:40", "Break", ""),
               ("15:40-15:50", "Post-MAP test", "10 minutes. Scan the first QR code"),
               ("15:50-15:55", "Final survey", "Scan the second QR code"),
               ("15:55-16:00", "Next steps and close", "Post your next task on the board")],
    "outcomes": ["Map a workflow: <b>trigger, steps, output and review</b>.",
                 "Set up a Claude <b>scheduled task</b> that runs your team's skill.",
                 "Handle <b>new files, an empty folder and a failed run</b>, and keep a run log.",
                 "Add <b>department rules</b> and a human review step.",
                 "Show a working automation and its <b>impact</b> at Demo Day."]},
}

# ------------------------------------------------------------------ next-word widget: an audit sentence about cut-off
LLM_TREE = {
 "start": {"prompt": "The cut-off test for Abdali Foods shows the invoice was posted in", "opts": [["November", 36], ["October", 29], ["the", 14], ["error", 9], ["December", 6], ["time", 5], ["Paris", 1]]},
 "November": [["2026,", 48], ["3,", 30], ["by", 20], ["purple", 1]],
 "October": [["2026,", 46], ["27,", 30], ["by", 22], ["purple", 1]],
 "the": [["wrong", 44], ["next", 30], ["November", 24], ["moon", 1]],
 "error": [["by", 44], ["and", 30], ["after", 24], ["dancing", 1]],
 "_2": [["2026,", 40], ["by", 30], ["after", 26], ["purple", 1]],
 "2026,": [["so it is a cut-off point.", 60], ["one week late.", 24], ["as expected.", 14], ["on Mars.", 1]],
 "3,": [["2026.", 66], ["so check cut-off.", 22], ["one week late.", 10], ["on Mars.", 1]],
 "27,": [["2026.", 64], ["as expected.", 24], ["so it is fine.", 10], ["on Mars.", 1]],
 "by": [["the accountant.", 44], ["mistake.", 30], ["the system.", 24], ["a camel.", 1]],
 "wrong": [["period.", 60], ["month.", 24], ["ledger.", 14], ["planet.", 1]],
 "next": [["month.", 66], ["period.", 22], ["week.", 10], ["century.", 1]],
 "_3": [["period.", 44], ["month.", 30], ["week.", 24], ["on Mars.", 1]],
}
LLM = {"tree": LLM_TREE, "foot": "Percentages are illustrative."}
SORT_LABELS = {"green": "Green · go ahead", "amber": "Amber · approved account, no names", "red": "Red · never"}

# ------------------------------------------------------------------ the transfer map (Lesson 1, every build lesson, the cheat sheet)
TRANSFER_HEAD = ["Agent Card box", "Claude (today)", "ChatGPT", "Microsoft 365 Copilot", "Gemini"]
TRANSFER = [["Instruction: saved rules and files", "Project", "Project or custom GPT", "Agent (Agent Builder) or Notebook", "Gem"],
            ["Input: reach your files and email", "Connectors", "Apps (formerly connectors)", "Work data in SharePoint, OneDrive, Outlook", "Connected apps (Gmail, Drive, Docs)"],
            ["Output: a file you open and edit", "Artifact or file", "Canvas", "Copilot Page", "Canvas"],
            ["Package: a reusable method", "Skill", "Skill (beta) or custom GPT", "Agent", "Gem"],
            ["When: runs on its own", "Scheduled task", "Scheduled task", "Scheduled prompt", "Scheduled action"]]
CARD_BOXES = [("Input", "What the agent works on, and where it comes from", "The month's invoices (PDF) and the purchase ledger (Excel)", "Connectors · Lesson 5"),
              ("Instruction", "The rules it follows, in five parts", "Match by number, compare date and amount, flag every difference, never guess", "Project · Lessons 3 and 4"),
              ("Output", "What it hands back, in a fixed shape", "One table in the Mirqab template, with a status for each invoice", "Artifacts · Lesson 5"),
              ("When", "When it runs without you", "Empty until Day 2", "Scheduled tasks · Day 2")]

# ------------------------------------------------------------------ MAP test: same 13 questions before and after (approved handoff, section 6)
CONFIDENCE = OUTCOMES
MAP = [
 {"q": "Claude summarizes the engagement letter and gives the report date as 31 March 2026. The letter says 31 March 2027. What do you do next?",
  "o": ["Fix it from the letter and check every other date", "Ask Claude to try again until the year looks right", "Keep it: the day and month are right, the year is minor", "Stop using Claude to summarize engagement letters"],
  "a": 0, "day": 1, "topic": "Where AI fails", "where": "Day 1 · Lesson 1 · where it fails, and Task 1.1"},
 {"q": "Every month, three coordinators turn the same client emails into a request tracker, each in their own chat. Their trackers never look the same. What fixes this best?",
  "o": ["Each coordinator writes a longer, more detailed prompt", "Ask Claude to be careful and check its work twice", "Save the rules and an example output in a Project", "Use a different AI tool that gives more stable answers"],
  "a": 2, "day": 1, "topic": "Repeatable", "where": "Day 1 · Lessons 2 and 3 · repeatable, the Agent Card and Projects"},
 {"q": "Which task is the best first agent for an audit team?",
  "o": ["Filling in the client-acceptance checklist once a year", "Choosing each week which findings to raise with the client", "Joining the weekly progress call with the client's finance team", "Matching each week's bank statement to the cash book"],
  "a": 3, "day": 1, "topic": "Agent-ready tasks", "where": "Day 1 · Lessons 2 and 3 · agent-ready tasks and scoring a use case"},
 {"q": "Your invoice agent lives in a Claude Project. Your supervisor adds a rule: \"Flag any difference over KWD 100.\" Where does the rule go?",
  "o": ["In the files you attach to each month's run", "In the chat, typed again at the start of each run", "In the Rules part of the agent's instructions", "In the output file name, so the reviewer sees it"],
  "a": 2, "day": 1, "topic": "Rules versus input", "where": "Day 1 · Lessons 3 and 4 · knowledge versus input; the five-part instruction"},
 {"q": "Your firm later moves to Microsoft 365 Copilot. What carries over from today?",
  "o": ["The Agent Card: input, instruction, output, when", "Nothing, because every AI tool works differently", "Only the exact prompts, copied word for word", "Only the sample files and the output template"],
  "a": 0, "day": 1, "topic": "Transfer", "where": "Day 1 · Lesson 1 · the transfer map, and every build lesson"},
 {"q": "Your agent works only when you open Claude and attach files. What lets it run each morning without you?",
  "o": ["A longer prompt that tells Claude to remember the task", "A skill, a connected input folder and a scheduled task", "A rule in the Project that says run every morning", "Sharing the Project with a colleague who presses Send"],
  "a": 1, "day": 2, "topic": "Scheduled tasks", "where": "Day 2 · Lessons 1 and 2"},
 {"q": "On Thursday, the reviewer opens the Log folder. There is a run-log file for every day this week except Monday. What should the reviewer conclude?",
  "o": ["Monday had no new files, so the run had nothing to log", "The Monday run failed or did not start: check it", "Claude probably merged Monday's log into Tuesday's file", "Nothing: one missing log file in a week is normal"],
  "a": 1, "day": 2, "topic": "The empty-folder rule and the run log", "where": "Day 2 · Lesson 3 · the empty-folder rule; Lesson 4 · the run log"},
 {"q": "Your workflow writes the weekly status summary for your manager every Thursday at 08:00. Where does the human review step belong?",
  "o": ["Before the trigger, so nothing starts without approval", "Only at year end, when the audit file is signed", "Nowhere, once the agent has passed three tests", "After the output, before anyone sends or relies on it"],
  "a": 3, "day": 2, "topic": "Review step", "where": "Day 2 · Lessons 1 and 4"},
 {"q": "Task A takes 50 minutes by hand and 8 with the agent, 15 times a month. Task B takes 20 minutes by hand and 5 with the agent, 40 times a month. Which saves more time each month?",
  "o": ["Task B, about 10 hours a month", "Both save exactly the same time", "Task A, about 10.5 hours a month", "Task B, because it runs more often"],
  "a": 2, "day": 2, "topic": "Impact", "where": "Day 2 · Lesson 5 · the impact formula"},
 {"q": "A colleague wants to share his invoice skill with the whole team. Its instructions name a real client and quote two of its invoice amounts. What should he do first?",
  "o": ["Remove the client details and test it on dummy data", "Share it, since only colleagues can open the skill", "Share it, and ask the team not to copy the amounts", "Rename the skill so the client's name is not visible"],
  "a": 0, "day": 2, "topic": "Work scenario: data", "where": "Day 1 · Lesson 1 · the data rule; Lesson 6 · skills; the safe-use card"},
 {"q": "Your invoice agent passed three tests. Next month, an invoice dated in December arrives in the November pack, and the agent marks it Matched. What is the best next step?",
  "o": ["Accept it, because the amount matches the ledger", "Take December invoices out of the folder by hand", "Ask Claude in the same chat if the date is fine", "Add a rule to flag out-of-period dates; retest"],
  "a": 3, "day": 2, "topic": "Work scenario: rules", "where": "Day 1 · Lessons 4 and 6; Day 2 · Lesson 4"},
 {"q": "Each week, your team's scheduled task flags a few new invoices as \"Amount differs\". A month later, nobody has acted on any of the flags. What fixes this?",
  "o": ["Lower the KWD limit so the task flags more invoices", "Name a reviewer who reads each run and signs off", "Delete the flag rule, since nobody acts on it", "Email the output file to the whole team each morning"],
  "a": 1, "day": 2, "topic": "Work scenario: review", "where": "Day 2 · Lessons 1 and 4 · a named reviewer; read the run log every morning"},
 {"q": "A supervisor asks which of your team's four agents to automate first. Which is the best choice?",
  "o": ["The one with the most steps and the longest instruction", "The one that runs often and has clear, checkable rules", "The newest one, because it uses the latest features", "The one built by the most senior member of the team"],
  "a": 1, "day": 2, "topic": "Work scenario: choice", "where": "Day 1 · Lesson 3 · scoring; Day 2 · Lesson 1"},
]
MAP_KEY = " · ".join(f"{i} {'abcd'[q['a']]}" for i, q in enumerate(MAP, 1))
MAP_MIN = 10
MAP_LEDE = {"before": f"{len(MAP)} questions and {len(OUTCOMES)} confidence ratings, about {MAP_MIN} minutes. The same test at the end of Day 2. Not graded. Phone only: no notes, no search, no AI."}

# ------------------------------------------------------------------ the approved slide plan
SLIDES = {1: 73, 2: 55}

# ------------------------------------------------------------------ MAP tests and the final survey (the three portal drafts of this program, updated in place)
PORTAL = "https://platform.joincoded.com/sv/"
FORMS = {
    "pre": {"name": "Pre-MAP test", "when": "Day 1 · Sun 15 Nov · 08:35", "slug": "coded-rsm-albazie-ai-innovation-and-automation-map-test-pre-day-1",
            "url": PORTAL + "coded-rsm-albazie-ai-innovation-and-automation-map-test-pre-day-1", "id": "763ba655-010d-48b6-a83b-1f56e2ca3825"},
    "post": {"name": "Post-MAP test", "when": "Day 2 · Mon 16 Nov · 15:40", "slug": "coded-rsm-albazie-ai-innovation-and-automation-map-test-post-day-2",
             "url": PORTAL + "coded-rsm-albazie-ai-innovation-and-automation-map-test-post-day-2", "id": "775a002d-c926-4bb6-92d3-956c751139de"},
    "survey": {"name": "Final satisfaction survey", "when": "Day 2 · Mon 16 Nov · 15:50", "slug": "coded-rsm-albazie-ai-innovation-and-automation-final-satisfaction-survey",
               "url": PORTAL + "coded-rsm-albazie-ai-innovation-and-automation-final-satisfaction-survey", "id": "fb337765-7220-49c0-a508-1f955343f9cd"},
}

# ------------------------------------------------------------------ the workshop home (hub)
DAYS[1].update({"cat": "Design and build", "icon": "doc", "tag": "the Agent Card",
                "bullets": ["What AI is, where it fails, and the tools it lives in", "Find the work worth an agent; write the Agent Card", "Build it in Claude: Project, connector, output, skill"]})
DAYS[2].update({"cat": "Automate", "icon": "dash", "tag": "scheduled workflows",
                "bullets": ["Trigger, steps, output and review", "A scheduled task that runs your skill on new files", "Department rules, a run log and Demo Day"]})
HABIT = [("One card", "Input, Instruction, Output. Then When."), ("Five parts", "Role, Steps, Rules, Output format, When unsure."),
         ("Flag, never guess", "A missing field is written as Not found."), ("Drafts only", "A named person reviews before anyone relies on it."),
         ("Dummy data", "No client data in any tool RSM has not approved.")]
HUB = {
    "headline": ["AI Innovation", "and Automation"],
    "sub": "A two-day, hands-on program for RSM Albazie. Design an AI agent for a task you repeat every week and build it in Claude. Then turn it into a workflow that runs on its own, with a review step.",
    "meta": "Claude",
    "program_title": "Two days, from a weak request to a workflow that runs without you.",
    "program_lead": "One fictional audit firm, Mirqab & Co., and its fictional client, Abdali Foods, are used on both days. The files are invoices, a ledger, leases, a trial balance, a request list and status sheets. Every file is made up, so you can practice safely. Shared work goes on the workshop board your trainer links in the room.",
    "habit_eyebrow": "How the days run", "habit_title": "Claude does the first pass. You review.",
    "habit_text": "Five habits from the two days:", "habit_list": HABIT,
    "files_title": "One firm. One client. Both days.",
    "takeaway_text": "The cheat sheet has the Agent Card, the five-part instruction, the Claude menu paths and the transfer map to ChatGPT, Copilot and Gemini. The safe-use card says what never goes into an AI tool. The take-home guide says what to do in your first week and first month. Every prompt is on its day's prompt sheet with a COPY button.",
    "map_text": "13 questions. The same on Day 1 and Day 2. Not graded. It measures what the program changes. Phone only, no AI. Scan the QR code on the screen, or open the link on your phone. On Day 2, the final survey comes right after.",
    "about": "AI Innovation and Automation is a CODED Professionals program for RSM Albazie & Co.",
    "day_tool_note": "Use Claude at claude.ai with the workshop account from CODED.",
}
SHEET = {"howto": ["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card, or open it from your track folder in the sandbox Drive.",
                   "Click <b>COPY</b>, paste the prompt into Claude, then fill any [brackets] with your own details.", "<b>Check the answer</b> against the file before you trust it: every figure, date and flag."],
         "note": "<b>Answers vary.</b> Claude may word things differently from the trainer's screen. That is normal, and it is why we check. Use only the fictional files here."}
TASK_FALLBACK_LINE = "Claude slow or a file not loading? Continue from the backup on the screen."
LESSON_INTRO = "CODED × RSM Albazie client program. 18 participants: Assurance 12, Corporate Finance 2, Support 3, Analytics Advisory 1. They use AI already; Claude may be new. Story: Mirqab & Co. and Abdali Foods (fictional)."

# ------------------------------------------------------------------ safe-use card
SAFE = [("green", "Green: go ahead", "Fictional or public data, and your own drafting.", ["The Mirqab and Abdali sample files", "A public standard or a published article", "Rewriting your own short email", "Your own task list, with no client or firm names"]),
        ("amber", "Amber: RSM-approved account only", "RSM internal documents that hold no client data, in an account RSM approved, with names removed.", ["An internal checklist or template", "An internal procedure or training note"]),
        ("red", "Red: never, unless RSM approves it", "Client data and personal data, in any AI tool RSM has not approved.", ["A client's ledger or trial balance", "KYC documents and IDs", "Client names in a prompt", "Draft financial statements"])]
RISKS = [("Wrong figures", "A confident table with one figure from the wrong document.", "Tick every figure against the source, as you would a junior's working paper."),
         ("Client data leaving the firm", "A real ledger in a personal or free account.", "Sort the task first: green, amber or red. RSM's policy decides."),
         ("Automation without review", "A scheduled output that nobody reads.", "Drafts only, a named reviewer, and a run log you read every morning.")]
CARD = {"lede": "<b>Before you put anything into an AI tool, sort the task.</b> RSM's AI and data policy always comes first.",
        "meta": [("shield", "Green, amber, red"), ("check", "Three risks"), ("pin", "RSM policy first")],
        "cards": SAFE, "risks_title": "Three risks, three habits", "risks_head": ["Risk", "What it looks like", "The habit"], "risks": RISKS,
        "policy_title": "RSM's policy comes first",
        "policy": ["Ask IT or Risk Management which AI tools and accounts RSM approves.", "If there is no approved account, amber becomes red.",
                   "Engagement confidentiality applies to AI tools exactly as it applies to email.", "When you are not sure, treat the task as red and ask first."]}

# ------------------------------------------------------------------ cheat sheet and take-home guide
CHEAT = [("Part 1 · The Agent Card", "Four boxes", "Fill the first three on Day 1. Day 2 fills When.",
          [(a, b, c, d) for a, b, c, d in CARD_BOXES], "Input, Instruction, Output. Then When."),
         ("Part 2 · The five-part instruction", "Write the Instruction box in five parts", "The invoice agent as the example.",
          [(k, {"Role": "Who Claude is", "Steps": "What to do, in order", "Rules": "What must always be true", "Output format": "The exact shape", "When unsure": "What to do with a gap"}[k], v, "")
           for k, v in CD.INVOICE_AGENT], "Role · Steps · Rules · Output format · When unsure."),
         ("Part 3 · Build it in Claude", "Where each part lives", "Menu names as of November 2026.",
          [("Project", "Instruction and knowledge", "Projects, + New Project, Set project instructions, then + for knowledge files.", "Rules in the instructions, templates in knowledge; documents come with each run."),
           ("Connector", "Input", "Customize, then Connectors, then Google Drive. Sign in.", "It reaches every file the account can open. Use an account that opens only what the task needs."),
           ("Artifact or file", "Output", "Ask for an artifact or an Excel file with exact columns and a total line.", "Same columns, same order, every run."),
           ("Skill", "Package", "Ask Claude to turn the Project into a skill. Find it under Customize, then Skills.", "Code execution and file creation must be on."),
           ("Scheduled task", "When", "Click Scheduled in the left sidebar, then New task, then Set up manually. Name, prompt, approval mode, frequency. Run it once on demand to test.", "Runs in the cloud; uses connectors and skills.")],
          "Each Claude feature fills one box of the card."),
         ("Part 4 · Run rules", "Before anything runs on its own", "The rules every team added on Day 2.",
          [("Inbox, then Processed", "Changing inputs", "Read new files in the Inbox; move each one to Processed.", "Nothing is read twice."),
           ("Empty folder", "No new files", "Write No new files in the run log and stop.", "Never process old files to fill a gap."),
           ("Drafts only", "Review step", "Mark the output DRAFT. End with Reviewed by.", "A person signs off."),
           ("Run log", "One file per run", "runlog-YYYY-MM-DD-HHMM.txt in Log: date, files read, items flagged, file saved.", "Read it every morning."),
           ("Owner", "A named person", "Every workflow has one owner and one reviewer.", "Who runs it when you are on leave?")],
          "Flag, never guess. Drafts, never final.")]
CHEAT_TABLES = [("The transfer map: the same skill in other tools", TRANSFER_HEAD, TRANSFER)]
CHEAT_LEDE = "The Agent Card, the five-part instruction, where each part lives in Claude, the run rules, and the same skills in ChatGPT, Copilot and Gemini. On one page."
GUIDE_INTRO = "Repeat what you built, safely. Start with dummy or green data. RSM's AI and data policy comes first."
GUIDE = [("Your first week", ["Pick your top task from the inventory. Write its Agent Card.", "Build it in an RSM-approved tool, on dummy data first.",
                             "Test it on three cases where you know the answer."]),
         ("Your first month", ["Run it every week. Log the minutes by hand and with the agent.", "Add your department's rules and a review step.",
                               "Share the skill with one colleague and ask them to find where it fails."]),
         ("In any tool", ["Use the transfer map: the same card becomes a ChatGPT Project, a Copilot agent or a Gemini Gem.",
                          "Keep the five-part instruction. It works in every assistant.", "Schedule it only after it passes your tests."])]
GUIDE_HABIT = "Claude does the first pass. You review and sign off. RSM's AI and data policy comes first."
GUIDE_META = [("home", "Your own work, safely"), ("list", "First week, first month"), ("shield", "RSM policy first")]

# ------------------------------------------------------------------ trainer pages
RUNBOOK_PREFLIGHT = ["Sign in to claude.ai on the presenting laptop with the trainer account. Open the invoice Project.",
                     "File creation works on the trainer account: ask Claude for a small Excel file and open it.",
                     "Before Day 1: build mirqab-invoice-match on the trainer account from the invoice Project and test it in a fresh chat. The 15:55 task and the Day 2 demos use it. Demo 1.8 saves its live copy as mirqab-invoice-match-live.",
                     "Check that Set up manually takes a time of day for Daily. If it does not, create each task with Create with Claude and say the time (for example, daily at 08:00).",
                     "Customize, then Connectors: Google Drive is connected before Day 1 with the trainer's CODED training Google account. Open the sandbox folders once. Demo 1.6 only shows the connector.",
                     "Day 1 only: at 08:00, create the 15:55 scheduled task (Demo 1.9). Before 13:30, check that the October invoices and ledger are in 01 Invoices / Inbox: Demo 1.6 reads them, and the 15:55 run moves them to Processed.",
                     "Before each day: run one scheduled task unattended (laptop closed) on a test folder, not a demo Inbox, with the approval mode set so it can save and move Drive files. Check the output file and the run-log file in Log, and that the inputs moved to Processed with no approval request waiting.",
                     "After Day 1: pause or delete the 15:55 demo task. Day 2, before 09:30: copy the October invoices and ledger back into 01 Invoices / Inbox for Demo 2.2. Before 12:40: copy batch 2 and abdali-invoice-messy.pdf from Packs into the same Inbox for Demo 2.5.",
                     "Daily schedules run every day. Kuwait works Sunday to Thursday, so Friday and Saturday runs log No new files. Check this on the first weekend run.",
                     "Confirm the names on the Scheduled page (New task, Set up manually, the approval mode, running a task on demand). If a name changed, say the new one in the room.",
                     "Before Day 2: on a test folder, run one task on demand with mirqab-locked-test-file.pdf in the Inbox and the fallback line in the prompt. The run log must say Could not read. If the file opens, use the Task 2.5 fallback (pause the Drive connector for one run).",
                     "Open this runbook, the backup results and the answer key on your own screen. Test the projector with the deck at full screen (F)."]
FACILITATOR = [
 ("open", "Before Day 1", "by Thursday 12 November", [("ul", [
    "Accounts: 18 Claude accounts from CODED (Ahmad Maher) on a plan with Projects, connectors, skills and Cowork scheduled tasks. Test one account end to end.",
    "Team plan settings (owner): Organization settings, then Plugins & skills, then Policy: turn on Cloud code execution and file creation, Skills, and Share with organization (the Share button appears only after a sharing toggle is on). Turn on the Google Drive connector. Google Drive moves, shares and trashes ask for approval before each action by default: as owner, let members run these actions without asking each time, or no scheduled run can move files to Processed.",
    "Cowork: admins control access with the admin toggle. Cowork on the web is in beta for Team plans. If it is not available on an account, install Claude Desktop on every laptop.",
    "Each account: ask Claude for a small Excel file to check that file creation works. Test a skill and a scheduled task on one account end to end.",
    "Sandbox Drive: owned by CODED. Folders 01 Invoices to 05 Status, each with Inbox, Processed, Outputs and Log, plus Team 1 to Team 4 for Day 2 with the same four folders. Day 1 Inboxes: 01 Invoices holds the October invoices and ledger; 02 to 05 hold their track pack only. Batch-2 and messy files stay in Packs (participants download the messy files from the site on Day 1). Keep a copy of the invoice pack, each track pack, the batch-2 files, the messy files and mirqab-locked-test-file.pdf (Task 2.5) in a Packs folder so teams can copy them into their Inbox.",
    "Google sign-in for the Drive connector: one CODED training Google account per participant (or one per team if CODED cannot make 18), each with edit access to the sandbox folders. Send each sign-in privately before Day 1. Never put a sign-in on a slide, the site or the board.",
    "Worked Projects: build one Project per track from mirqab-starter-instructions.docx and test it on the pack. For Task 1.6 hint 3, open it on the presenting laptop, or give the person its five parts from the starter file.",
    "Shared board: one Google Sheet in the sandbox Drive with the tabs Poll, Task board, Agent Cards, Teams and votes, Clock, Next tasks. Share the link in the room.",
    "Confirm with Moudhi: 16:00 or 16:30 finish; Waqas has approved the Day 2 change; Demo Day panel and award.",
    "The MAP tests and survey are published only after the site QA passes. The QR codes work after that."])]),
 ("room", "Room and laptops", "pre-flight", [("ol", [
    "Four tables of four or five. Teams sit together from Day 1 lunch.",
    "Wi-Fi details on the board before 08:15.",
    "Day 1, 08:30: every laptop opens claude.ai (signed in) and the workshop site. The pre-MAP QR at 08:35 doubles as the phone check.",
    "Nothing is printed. The lab pages, prompt sheets, cheat sheet and safe-use card are on the site."])]),
 ("n8n", "The n8n demo (Demo 2.4)", "built and tested before Day 2", [("ul", [
    "Trigger: a new email in a CODED requests inbox made for the demo (no client mailbox).",
    "Claude step: an Anthropic (Claude) model step with the Demo 2.4 prompt from the Day 2 prompt sheet. It returns request number, status and follow-up needed.",
    "Action: append one row to a Request tracker sheet in the sandbox Drive (04 Requests / Outputs).",
    "Credentials: the CODED automation owner keeps the email, Anthropic and Google credentials inside n8n. Never show them on screen or on any page.",
    "Test the day before with two emails. Keep the two rows in the sheet as the backup. If the live run is slow, step through the flow on the slide."])]),
 ("after", "After Day 2", "the same evening", [("ul", [
    "Pause or delete every scheduled task on the trainer account and the team accounts, so nothing keeps running on CODED accounts.",
    "Empty the Inbox folders in the sandbox Drive, and turn off the n8n demo flow.",
    "Remove the participants' access to the sandbox Drive and the shared board after the results report."])]),
 ("teams", "Forming the four teams", "over Day 1 lunch", [("ul", [
    "Group the approved Agent Cards by similar workflow.", "Put at least one supervisor or the manager in each team.",
    "Write the teams on the board's Teams and votes tab before 12:30.",
    "Day 2: each team builds its scheduled task on the account of the person who made the team's skill. Shared skills cannot be edited by the people they are shared with."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Claude is slow or busy", "Talk through the prompt player slide.", "Show the backup result."],
    ["Google Drive connector will not sign in", "Upload the files to the chat and continue.", "Pair with a neighbor; fix the account at the break."],
    ["Skills are off on an account", "Continue in the Project.", "Turn skills on at the break (owner settings)."],
    ["Cowork or scheduled tasks unavailable", "Run the scheduled prompt by hand in a chat.", "Schedule it on the trainer account and show the run."],
    ["No internet", "Phone hotspot.", "Decks, backups and the site work from the cache; demo from the backup results."]])]),
 ("demoday", "Demo Day", "running order and scoring", [("table", [["Item", "Detail"],
    ["Order", "Teams 1 to 4, 8 minutes each: 5 demo, 3 questions."],
    ["Rubric", ", ".join(f"{c} {pt}" for c, pt, _t in CD.RUBRIC_FULL).capitalize() + f" ({sum(pt for _c, pt, _t in CD.RUBRIC_FULL)} points)."],
    ["Working functionality", "The first 08:00 run comes after Demo Day. Full marks: the task is saved on the Scheduled page with its frequency, the team runs it on demand from there, and the output has the same shape every run."],
    ["Source accuracy", "During the questions, the panel picks three figures from the team's output. The team shows each one in its source file. 3 of 3 match: 10; 2 of 3: 5; 1 or none: 0."],
    ["Test evidence", "The team opens its Log folder: three clean runs, the No new files run (Task 2.3) and the failed-run test (Task 2.5)."],
    ["Panel", "The trainer scores. RSM leadership joins if confirmed."],
    ["Record", "Write each team's scores on the board's Teams and votes tab."]])]),
]

# ------------------------------------------------------------------ browser labs: one per day; answers only in the staff lab key
LABS = {
 1: {"title": "Build your agent, step by step", "intro": "Work through the steps as the day goes. Your notes and done marks stay in this browser. Paste your card to the shared board when the trainer asks.",
     "steps": [
        {"title": "Your task inventory (Task 1.3)", "do": ["List 10 tasks from your last week.", "Tag each one: repeats weekly, clear rules, document in and document out.",
          "Preparers: what do you rebuild on every engagement? Reviewers: what do you check every time? Coordinators: what do you chase every week, such as requests or new-client KYC files?"],
         "hint": "If a task needs a meeting or a judgment call, it is not your first agent.", "check": {"kind": "note", "label": "Your top 3 tasks"},
         "answer": [("p", "A good top 3 has three Yes tags each, written as verbs, with no client names.")]},
        {"title": "Build the invoice agent with the trainer (Task 1.4)", "do": ["Projects, + New Project: Mirqab invoice match.", "Set project instructions: paste the five parts from the prompt sheet.",
          "Add mirqab-invoice-match-template.xlsx to the knowledge.", "Run it on the October invoices and ledger."],
         "hint": "At least two rows should not say Matched. Look at the amount on page 3.", "check": {"kind": "flag", "label": "Type the invoice number whose amount differs", "answer": "SCC-0718"},
         "answer": [("p", f"SCC-0718: invoice KWD {D.num(D.INV['SCC-0718'][4])}, ledger KWD {D.num(D.WRONG_LEDGER)}. Difference KWD {D.num(D.WRONG_DIFF)}.")]},
        {"title": "Find the cut-off item", "do": ["Look at the row the agent marked Not in ledger.", "Check its date on the invoice. Is it in the October ledger?"],
         "hint": "It is the last invoice in the pack.", "check": {"kind": "flag", "label": "Type the invoice number missing from the October ledger", "answer": "FSC-3390"},
         "answer": [("p", "FSC-3390 is dated 27 October and is not in the October ledger: a cut-off point to follow up.")]},
        {"title": "Agent Card v1 (Task 1.5)", "do": ["Write your card: Input, Instruction, Output. Leave When empty.", "Paste it on the shared board for approval."],
         "hint": "Read your Instruction box as if you were new. Would you know what to do?", "check": {"kind": "note", "label": "Your Agent Card"},
         "answer": [("p", "Approve when the input names a file type, the instruction has two rules and a When unsure line, and the output names its columns.")]},
        {"title": "Build v1 of your agent (Task 1.6)", "do": ["Create your own Project. Write the five parts.", "Add a template or one example output to the knowledge.", "Check 3 items of your pack by hand (the list is in Task 1.6). Run the agent and compare."],
         "hint": "Fix the instructions, not the answer.", "check": {"kind": "note", "label": "Your 3 items: your answer and the agent's"},
         "answer": [("p", "Each track's expected findings are in the Day 1 answer key, Task 1.6.")]},
        {"title": "Read from the folder (Task 1.7)", "do": ["Customize, then Connectors: connect Google Drive.", "Run your agent on your track folder's Inbox. Ask it to list the files it read."],
         "hint": "The folder path must match the Drive exactly.", "check": {"kind": "note", "label": "The files your agent read"},
         "answer": [("p", "The run lists exactly the files in the track folder's Inbox.")]},
        {"title": "Same shape every run (Task 1.8)", "do": ["Add an output rule: exact columns, order and a total line.", "Run twice and compare."],
         "hint": "Name the columns in the order you want them.", "check": {"kind": "note", "label": "Your output columns, in order"},
         "answer": [("p", "Both runs have the same columns, order and total line, with nothing edited by hand.")]},
        {"title": "Make your skill (Task 1.9)", "do": ["Ask Claude to turn your Project into a skill. Save it.", "Test it in a new chat outside the Project.", "Add one line to your card: where this skill would live in ChatGPT, Copilot or Gemini."],
         "hint": "A skill needs a short name and one line on when to use it.", "check": {"kind": "note", "label": "Your skill's name"},
         "answer": [("p", "The fresh chat uses the skill and returns the same shape as the Project. The transfer line names a ChatGPT skill or custom GPT, a Copilot agent or a Gem.")]},
        {"title": "The messy sample and the clock (Task 1.10)", "do": ["Run your skill on the messy file for your track. It hides a gap the agent must flag (the invoice file has two). No two values in it conflict.", "Log the minutes by hand and with the agent on the board."],
         "hint": "A good agent flags what it cannot see.", "check": {"kind": "note", "label": "Minutes by hand, minutes with the agent"},
         "answer": [("ul", [f"{v[0]}: {v[2]}" for v in D.MESSY.values()])]},
     ]},
 2: {"title": "Put your workflow on a schedule", "intro": "Your team works through these steps today. Each person can keep their own notes here; the team's card goes on the shared board.",
     "steps": [
        {"title": "The workflow card (Task 2.1)", "do": ["Fill When, Input, Skill, Output and Who reviews for your team's agent.", "Post it on the shared board."],
         "hint": "Who reviews is one person's name.", "check": {"kind": "note", "label": "Your team's workflow card"},
         "answer": [("p", "A time, one folder, the Day 1 skill, a file name pattern and a run-log file, and a named reviewer.")]},
        {"title": "Create the scheduled task (Task 2.2)", "do": ["Work on the laptop of the person who made your team's skill. Copy your track pack into your team folder's Inbox.", "Click Scheduled in the left sidebar, then New task, then Set up manually. Paste the prompt from the prompt sheet and fill the brackets.", "Approval mode: let the run save and move files without waiting. Daily at 08:00. Save. Run it once on demand."],
         "hint": "Most failures are a folder name that does not match the Drive.", "check": {"kind": "note", "label": "Task name and time"},
         "answer": [("p", "The task shows on the Scheduled page; the test run wrote a file to Outputs, saved a run-log file in Log and moved the inputs to Processed.")]},
        {"title": "Batch 2 (Task 2.3)", "do": ["Copy your track's batch-2 file from Packs into the Inbox.", "Run the task on demand. Check the output and the run log."],
         "hint": "Invoice teams: one invoice is not in KWD.", "check": {"kind": "flag", "label": "Invoice teams: type the invoice number the workflow must flag", "answer": D.B2_FLAG},
         "answer": [("p", f"{D.B2_FLAG} is in USD: flag it, never convert it. {', '.join(D.B2_MATCHED)} match.")]},
        {"title": "The empty folder", "do": ["Empty the Inbox. Run the task on demand.", "Read the run log."],
         "hint": "One honest line, then stop.", "check": {"kind": "flag", "label": "Type the exact words the run log should show", "answer": "No new files"},
         "answer": [("p", "The run log says No new files, and nothing is written to Outputs.")]},
        {"title": "Department rules (Task 2.4)", "do": ["Pick two rules from mirqab-review-rules.docx.", "The skill owner adds them to the skill word for word, with DRAFT and Reviewed by.", "Copy your track's messy file into the Inbox. Run the task on demand."],
         "hint": "A paraphrase is a new rule. Copy them exactly.", "check": {"kind": "note", "label": "Your two rules"},
         "answer": [("p", "Two rules from the file, word for word; DRAFT on the output; a Reviewed by line; the messy sample flagged.")]},
        {"title": "Clean runs and the failed-run test (Task 2.5)", "do": ["Copy your pack into the Inbox and run on demand. Do it three times. Workflow teams: move the trackers in Outputs to Processed before each run.", "The skill owner adds the fallback line from the prompt sheet to the scheduled task's prompt.",
          "Copy mirqab-locked-test-file.pdf from Packs into the Inbox. Run on demand. Read the run log.", "Delete the locked file from the Inbox."],
         "hint": "A good run says what it could not do.", "check": {"kind": "flag", "label": "Type the words the run log should show before the locked file's name", "answer": "Could not read"},
         "answer": [("p", "The run log says Could not read: mirqab-locked-test-file.pdf. Nothing is guessed, and the file stays in the Inbox until you delete it.")]},
        {"title": "Impact and the demo (Task 2.5)", "do": ["Impact: (minutes by hand minus minutes with the agent) times runs a month.", "A 5-minute plan: problem, card, live run, impact, next."],
         "hint": "Every number on your demo comes from your run log or the Clock tab.", "check": {"kind": "note", "label": "Your impact number and demo plan"},
         "answer": [("p", f"Example: (40 − 5) × 20 = {D.IMPACT_MIN} minutes, about 12 hours a month.")]},
     ]},
}

# ------------------------------------------------------------------ the minutes inside each session (lesson plan)
SEGMENTS = {
 1: [("08:30-08:52", "Opening", [("08:30", 5, "Welcome and sign-in check"), ("08:35", 10, "Pre-MAP test"), ("08:45", 7, "Opener: Demo 1.0, outcomes, today's map")]),
     ("08:52-09:20", "Lesson 1 · AI foundations", [("08:52", 3, "Live poll and story"), ("08:55", 5, "How AI writes: the next-word widget"), ("09:00", 4, "Where it fails: Demo 1.1"),
                                                   ("09:04", 3, "The data rule, with a check"), ("09:07", 4, "Three families of tools and the transfer map"), ("09:11", 1, "Quick check"),
                                                   ("09:12", 1, "The Claude tour"), ("09:13", 7, "Task 1.1 · First Claude chat")]),
     ("09:30-10:20", "Lesson 2 · Why chat isn't enough, and finding the work", [("09:30", 2, "Story: two tables"), ("09:32", 18, "Task 1.2 · Same task, 18 answers"), ("09:50", 5, "Debrief: three tables, two chats"),
                                                   ("09:55", 5, "Repeatable: concept and check"), ("10:00", 5, "Agent-ready tasks, Demo 1.2 and a check"), ("10:05", 12, "Task 1.3 · Task inventory"), ("10:17", 3, "Board review")]),
     ("10:30-11:30", "Lesson 3 · Design the agent, then pick your case", [("10:30", 10, "The Agent Card, literal instructions, Projects, knowledge versus input, with checks"), ("10:40", 5, "Demo 1.3 · From card to agent"),
                                                   ("10:45", 20, "Task 1.4 · Build the invoice agent with me"), ("11:05", 5, "Scoring a use case and Demo 1.4"), ("11:10", 20, "Task 1.5 · Agent Card v1")]),
     ("12:30-13:20", "Lesson 4 · Build: Instruction", [("12:30", 5, "Late approvals and the story"), ("12:35", 5, "The five-part instruction, an example output, test before you trust, with a check"),
                                                   ("12:40", 4, "Demo 1.5"), ("12:44", 1, "Transfer: instructions in other tools"), ("12:45", 35, "Task 1.6 · Build v1 (struggle 20, unlock 8, fix 7)")]),
     ("13:30-14:25", "Lesson 5 · Build: Input and Output", [("13:30", 2, "Story: Noura's Sunday"), ("13:32", 3, "Connectors and the sandbox, with a check"), ("13:35", 5, "Demo 1.6"),
                                                   ("13:40", 15, "Task 1.7 · Run from the folder"), ("13:55", 5, "Artifacts and a fixed shape, with a check"), ("14:00", 5, "Demo 1.7 and the transfer slide (before the task)"),
                                                   ("14:05", 20, "Task 1.8 · Fixed-shape output")]),
     ("14:45-15:30", "Lesson 6 · Build: Package", [("14:45", 5, "Skills: story, concept and check"), ("14:50", 4, "Demo 1.8"), ("14:54", 2, "Transfer: packaged methods in other tools, with a check"), ("14:56", 20, "Task 1.9 · Make your skill"), ("15:16", 14, "Task 1.10 · The messy sample and the clock")]),
     ("15:40-16:00", "Lesson 7 · Show and tell, and the Day 2 hook", [("15:40", 12, "Team demos"), ("15:52", 5, "Demo 1.9 · The agent that ran itself"), ("15:57", 3, "Wrap, the When box and the team vote")])],
 2: [("08:30-09:20", "Lesson 1 · From agent to system", [("08:30", 8, "Callback and three checks"), ("08:38", 2, "Story: who runs it when you are on leave?"), ("08:40", 8, "Trigger, steps, output and review, with a check"),
                                                   ("08:48", 2, "The team vote result"), ("08:50", 5, "Demo 2.1"), ("08:55", 20, "Task 2.1 · Workflow card"), ("09:15", 5, "Share-back")]),
     ("09:30-10:20", "Lesson 2 · Make it run on its own", [("09:30", 2, "Story"), ("09:32", 5, "Scheduled tasks: what they are and the steps"), ("09:37", 1, "Quick check"),
                                                   ("09:38", 5, "Demo 2.2"), ("09:43", 30, "Task 2.2 · Schedule your workflow"), ("10:13", 7, "The transfer slide and buffer")]),
     ("10:30-11:30", "Lesson 3 · New inputs, outputs and n8n", [("10:30", 2, "Story"), ("10:32", 8, "Changing inputs and delivered output, the empty-folder rule, two checks"), ("10:40", 5, "Demo 2.3"),
                                                   ("10:45", 25, "Task 2.3 · Batch 2 and the empty folder"), ("11:10", 5, "When n8n"), ("11:15", 13, "Demo 2.4 · The n8n flow"), ("11:28", 2, "Which tool: the comparison and a check")]),
     ("12:30-13:20", "Lesson 4 · Fit it to your department", [("12:30", 2, "Story"), ("12:32", 8, "Department rules, the review step and the run log, two checks"),
                                                   ("12:40", 5, "Demo 2.5"), ("12:45", 30, "Task 2.4 · Your department's rules"), ("13:15", 5, "Buffer")]),
     ("13:30-14:25", "Lesson 5 · Test and prepare the demo", [("13:30", 2, "Story"), ("13:32", 3, "Impact"), ("13:35", 3, "The judges' rubric"), ("13:38", 2, "The demo script"),
                                                   ("13:40", 3, "Demo 2.6 and a check"), ("13:43", 2, "When a step fails: the fallback and a check"), ("13:45", 40, "Task 2.5 · Clean runs, a failed run and the script")]),
     ("14:45-15:30", "Lesson 6 · Demo Day", [("14:45", 32, "Four teams, 8 minutes each"), ("15:17", 8, "Changeovers and scoring"), ("15:25", 5, "Panel comments")]),
     ("15:40-16:00", "Close", [("15:40", 10, "Post-MAP test"), ("15:50", 5, "Final survey"), ("15:55", 5, "Next steps and close")])],
}

REDIRECTS = [("/prompts1", "/coded-rsm-ai-automation-prompt-sheet-day-1"), ("/prompts2", "/coded-rsm-ai-automation-prompt-sheet-day-2"),
             ("/lab1", "/coded-rsm-ai-automation-lab-day-1"), ("/lab2", "/coded-rsm-ai-automation-lab-day-2")]
# The staff home is served at /staff (trailingSlash false), so its relative links to staff-only pages resolve at the site root.
# Send those root addresses to /staff/... (the staff password still applies there). See PLUGIN-FEEDBACK.md.
REDIRECTS += [(f"/coded-rsm-ai-automation-{p}", f"/staff/coded-rsm-ai-automation-{p}") for p in
              ["lesson-plan", "facilitator-kit", "staff.css"] + [f"{k}-day-{d}" for d in (1, 2) for k in ("notes", "runbook", "backup", "answer-key", "lab-key")]]

# ------------------------------------------------------------------ portal survey words (bilingual)
PROG_AR = "الابتكار والأتمتة بالذكاء الاصطناعي"
CLIENT_AR = "آر إس إم البزيع"
CONF_AR = ["أستطيع أن أوضح ما يُجيده الذكاء الاصطناعي التوليدي وأين قد يخطئ، وأن أتحقق من مخرجاته مقابل المصدر.",
           "أستطيع تحديد المهام في عملي التي تناسب وكيلاً ذكياً، ووصف إحداها في بطاقة وكيل: المدخلات والتعليمات والمخرجات ومتى يعمل.",
           "أستطيع بناء مشروع (Project) في Claude بتعليمات ومعرفة تعطي النتيجة نفسها القابلة للتحقق في كل تشغيل.",
           "أستطيع ربط وكيل بمجلد في Drive وجعله يُخرج نتيجته بتنسيق ثابت.",
           "أستطيع تحويل طريقة عملي إلى مهارة (Skill) وتشغيلها وفق جدول زمني، مع خطوة مراجعة بشرية.",
           "أستطيع ربط كل ميزة في Claude بما يقابلها في ChatGPT وMicrosoft 365 Copilot وGemini."]
MAP_AR = [
 ("يلخّص Claude خطاب التكليف ويذكر أن موعد التقرير هو 31 مارس 2026، بينما ينص الخطاب على 31 مارس 2027. ما خطوتك التالية؟",
  ["تصحيح التاريخ من الخطاب ومراجعة كل التواريخ الأخرى", "الطلب من Claude المحاولة مجدداً حتى تبدو السنة صحيحة", "إبقاؤه كما هو: اليوم والشهر صحيحان والسنة تفصيل بسيط", "التوقف عن استخدام Claude لتلخيص خطابات التكليف"]),
 ("يحوّل ثلاثة منسقين كل شهر رسائل العميل نفسها إلى متتبع طلبات، كلٌّ في محادثته الخاصة، ولا تتشابه متتبعاتهم أبداً. ما أفضل حل لذلك؟",
  ["أن يكتب كلٌّ منهم أمراً أطول وأكثر تفصيلاً", "أن يُطلب من Claude الحرص ومراجعة عمله مرتين", "حفظ القواعد ومثال على المخرجات في مشروع (Project)", "استخدام أداة ذكاء اصطناعي أخرى تعطي إجابات أكثر ثباتاً"]),
 ("ما أفضل مهمة لتكون أول وكيل لفريق تدقيق؟",
  ["تعبئة قائمة التحقق لقبول العملاء مرة واحدة في السنة", "اختيار النتائج التي تُعرض على العميل كل أسبوع", "حضور الاجتماع الأسبوعي لمتابعة التقدم مع الفريق المالي للعميل", "مطابقة كشف الحساب البنكي الأسبوعي مع دفتر النقدية"]),
 ("يعمل وكيل الفواتير لديك داخل مشروع (Project) في Claude. يضيف مشرفك قاعدة: \"أشِر إلى أي فرق يزيد على 100 دينار كويتي\". أين توضع هذه القاعدة؟",
  ["في الملفات التي ترفقها مع تشغيل كل شهر", "في المحادثة، تُكتب من جديد في بداية كل تشغيل", "في جزء القواعد (Rules) من تعليمات الوكيل", "في اسم ملف المخرجات، ليراها المراجع"]),
 ("انتقلت شركتك لاحقاً إلى Microsoft 365 Copilot. ما الذي ينتقل معك من اليوم؟",
  ["بطاقة الوكيل: المدخلات والتعليمات والمخرجات ومتى", "لا شيء، لأن كل أداة ذكاء اصطناعي تعمل بطريقة مختلفة", "الأوامر نفسها فقط، منسوخة حرفياً", "الملفات التدريبية وقالب المخرجات فقط"]),
 ("لا يعمل وكيلك إلا عندما تفتح Claude وترفق الملفات. ما الذي يجعله يعمل كل صباح دون تدخلك؟",
  ["أمر أطول يطلب من Claude تذكّر المهمة", "مهارة (Skill) ومجلد مدخلات متصل ومهمة مجدولة", "قاعدة في المشروع (Project) تقول: شغّل الوكيل كل صباح", "مشاركة المشروع مع زميل يضغط زر الإرسال"]),
 ("يفتح المراجع مجلد السجل (Log) يوم الخميس. يوجد ملف سجل تشغيل لكل يوم من هذا الأسبوع ما عدا يوم الاثنين. ما الذي يجب أن يستنتجه المراجع؟",
  ["لم تصل ملفات جديدة يوم الاثنين، فلم يكن لدى التشغيل ما يسجّله", "تشغيل يوم الاثنين فشل أو لم يبدأ: يجب التحقق منه", "ربما دمج Claude سجل الاثنين في ملف يوم الثلاثاء", "لا شيء: غياب ملف سجل واحد في الأسبوع أمر طبيعي"]),
 ("يكتب سير العمل لديك ملخص الحالة الأسبوعي لمديرك كل يوم خميس الساعة 08:00. أين تقع خطوة المراجعة البشرية؟",
  ["قبل المُشغِّل، حتى لا يبدأ شيء دون موافقة", "في نهاية السنة فقط، عند اعتماد ملف التدقيق", "لا حاجة إليها بعد أن يجتاز الوكيل ثلاثة اختبارات", "بعد المخرجات، وقبل أن يرسلها أحد أو يعتمد عليها"]),
 ("تستغرق المهمة (أ) 50 دقيقة يدوياً و8 دقائق مع الوكيل، 15 مرة في الشهر. وتستغرق المهمة (ب) 20 دقيقة يدوياً و5 دقائق مع الوكيل، 40 مرة في الشهر. أيهما توفر وقتاً أكثر كل شهر؟",
  ["المهمة (ب)، نحو 10 ساعات في الشهر", "توفر المهمتان الوقت نفسه تماماً", "المهمة (أ)، نحو 10.5 ساعة في الشهر", "المهمة (ب)، لأنها تتكرر أكثر من الأخرى"]),
 ("يريد زميل مشاركة مهارة الفواتير الخاصة به مع الفريق كله. تذكر تعليماتها اسم عميل حقيقي وتقتبس مبلغين من فواتيره. ماذا يجب أن يفعل أولاً؟",
  ["حذف بيانات العميل واختبار المهارة على بيانات تدريبية", "مشاركتها، لأن الزملاء وحدهم يستطيعون فتح المهارة", "مشاركتها، مع الطلب من الفريق عدم نسخ المبالغ", "تغيير اسم المهارة كي لا يظهر اسم العميل الحقيقي"]),
 ("اجتاز وكيل الفواتير ثلاثة اختبارات. في الشهر التالي وصلت فاتورة بتاريخ ديسمبر ضمن حزمة نوفمبر، فوضع الوكيل عليها حالة Matched. ما أفضل خطوة تالية؟",
  ["قبولها، لأن المبلغ يطابق دفتر الأستاذ", "إخراج فواتير ديسمبر من المجلد يدوياً", "سؤال Claude في المحادثة نفسها إن كان التاريخ مقبولاً", "إضافة قاعدة للتواريخ خارج الفترة وإعادة الاختبار"]),
 ("كل أسبوع، تُشير المهمة المجدولة لفريقك إلى بعض الفواتير الجديدة بعبارة \"Amount differs\". وبعد شهر، لم يتخذ أحد أي إجراء بشأن هذه الإشارات. ما الحل؟",
  ["خفض الحد بالدينار حتى تُشير المهمة إلى فواتير أكثر", "تسمية مراجع يقرأ كل تشغيل ويعتمده", "حذف قاعدة الإشارة، لأن أحداً لا يتصرف بناءً عليها", "إرسال ملف المخرجات بالبريد إلى الفريق كله كل صباح"]),
 ("يسألك مشرف أيّ وكلاء فريقك الأربعة يُؤتمت أولاً. ما الخيار الأفضل؟",
  ["الوكيل الذي فيه أكثر الخطوات وأطول التعليمات", "الذي يعمل كثيراً وقواعده واضحة وقابلة للتحقق", "الأحدث بينها، لأنه يستخدم أحدث ميزات الأداة", "الوكيل الذي بناه أقدم عضو في الفريق"]),
]
DAY_AR = {1: "تصميم وكلاء الذكاء الاصطناعي للعمل الفعلي", 2: "تحويل الوكلاء إلى سير عمل تشغيلي"}
SURVEY = {
    "program": "CODED × RSM Albazie", "program_ar": PROG_AR, "client": "RSM Albazie", "cohort": "RSM-AI-Nov/Nov-26",
    "subtitle": {"en": "CODED × RSM Albazie", "ar": f"CODED × {CLIENT_AR}"}, "folder": "e07488c7-5525-403f-a2c6-f6db15ae710a",
    "name_prefix": "CODED × RSM Albazie", "note": "", "test_min": MAP_MIN,
    "confidence_ar": CONF_AR, "map_ar": MAP_AR, "day_ar": DAY_AR,
    "relevance": ("The content was high quality and relevant to my work at RSM Albazie.", f"كان المحتوى عالي الجودة وذا صلة بعملي في {CLIENT_AR}."),
    "hands_on": ("The hands-on parts, such as the Agent Card, building my own agent in Claude, the scheduled workflow and Demo Day, helped me apply what I learned.",
                 "ساعدتني الأجزاء التطبيقية، مثل بطاقة الوكيل وبناء وكيلي الخاص في Claude وسير العمل المجدول ويوم العرض، على تطبيق ما تعلّمته."),
    "materials": ("The program website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
                  "كانت مواد البرنامج (الموقع وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد البرنامج) واضحةً ومفيدة."),
    "logistics": ("The venue, the daily timing and access to Claude and the sandbox Drive worked well for me.",
                  "كان المكان والتوقيت اليومي وإمكانية الوصول إلى Claude ومجلد Drive التدريبي مناسباً لي."),
}
