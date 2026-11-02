# -*- coding: utf-8 -*-
"""RSM Albazie · AI Innovation and Automation: program facts, days, run of show, files.

Single source of truth for everything the site and the decks say about the program.
Written for Gulf ESL readers: plain English, American spelling, no em dashes.
All client data in this workshop is fictional. Mirqab & Co., Khiran Logistics,
Abdali Foods and Salwa Trading are made-up names, made for training.
"""

CODE = "coded-rsm-ai-automation"
PREFIX = "rsm"                      # deck class prefix
PROGRAM = "AI Innovation and Automation"
PROGRAM_AR = "الابتكار والأتمتة بالذكاء الاصطناعي"
CLIENT = "RSM Albazie"
CLIENT_AR = "آر إس إم البزيع"
CLIENT_ACCENT = "#009CDE"           # RSM blue, used only as a small client accent
COHORT = "RSM-AI-Nov/Nov-26"
VENUE = "CODED, Morning Alsharekh"
VENUE_SHORT = "In person · CODED"
HOURS = "08:30-16:30"
TOOLS = "Claude and n8n"
FIRM = "Mirqab & Co."               # the fictional audit firm in every practice file
SITE_URL = "https://coded-rsm-ai-automation.vercel.app"

DAYS = [
    {
        "n": 1,
        "date": "Sun 15 Nov 2026",
        "date_long": "Sunday 15 November 2026",
        "title": "Designing AI Agents for Real Work",
        "cat": "Agents",
        "icon": "agent",
        "objective": "Identify and build a working AI agent that replaces a real task from daily work.",
        "lede": "Find the task that eats your week. Design an agent for it. Build it in Claude.",
        "brief": [
            "Day 1 starts with one KYC pack and two instructions. Then: how an AI model writes, which tasks are worth automating, "
            "the Agent Design Framework (input, instruction, output), and a working agent in Claude that you test and improve.",
        ],
        "build_today": "Your agent in a Claude Project, version 2, with three test cases.",
        "bullets": [
            "Find the repetitive tasks in audit and onboarding",
            "Design an agent: input, instruction, output",
            "Build and test a working agent in Claude",
        ],
        "outcomes": [
            "Explain why an AI model can give a wrong date or number, and how a file and a clear instruction prevent it.",
            "Use four questions to find the tasks in audit and onboarding that are worth automating.",
            "Design an agent with a clear input, instruction and output.",
            "Build a working agent in a Claude Project and run it on a real case file.",
            "Test the agent with three cases and fix the instruction, not the answer.",
        ],
        "ros": [
            ("Opener: same file, two instructions", "08:30-08:45", "One KYC pack, a weak instruction and a designed one"),
            ("MAP test (before)", "08:45-08:55", "10 minutes. Scan the QR code from the CODED portal"),
            ("Reframing work", "08:55-10:15", "How an AI model writes, the chat, agent, workflow ladder, and the tasks worth automating"),
            ("BREAK", "10:15", ""),
            ("Agent Design Framework", "10:30-11:40", "Input, instruction, output, and the five parts of a strong instruction"),
            ("Use case selection", "11:40-12:00", "Four agent cards. Pick one and form your team"),
            ("BREAK:Lunch and Dhuhr prayer", "12:00", ""),
            ("Build in Claude", "13:00-14:15", "A Claude Project is an agent you can reuse. Build version 1"),
            ("BREAK", "14:15", ""),
            ("Test and improve", "14:30-15:30", "Three test cases. Fix the instruction, not the answer"),
            ("Safe use in an audit firm", "15:30-15:55", "Green, amber, red. AI output is evidence you still test"),
            ("Show and close", "15:55-16:30", "Three agents on the big screen, and tomorrow's problem"),
        ],
        "ros_note": "A guide, not a script. Breaks at 10:15 and 14:15; lunch and Dhuhr prayer at 12:00.",
        "tasks": [
            {"id": "1.1", "mins": 10, "title": "Your task list, filtered",
             "steps": ["Write 5 tasks from your last two weeks.",
                       "Score each task with the four questions.",
                       "Circle your top 3. Share one with your table."],
             "look": "Three candidate tasks, each with four yes or no answers.",
             "files": [], "tool": "PAPER OR CLAUDE"},
            {"id": "1.2", "mins": 20, "title": "Fill one Agent Card",
             "steps": ["Pick one candidate task from the morning.",
                       "Fill the Agent Card: job, input, instruction, output, three tests.",
                       "Swap with a partner. Could a new joiner run your card?"],
             "look": "A card where every part is specific: a named file, numbered steps, fixed output columns.",
             "files": [], "tool": "AGENT CARD"},
            {"id": "1.3", "mins": 40, "title": "Build sprint 1: your agent, version 1",
             "steps": ["Create a Claude Project with your agent's name.",
                       "Paste the starter instruction from your prompt sheet into the project instructions.",
                       "Add the knowledge file. Start a new chat and attach the case file.",
                       "Check three values in the output against the source file."],
             "look": "An output in the exact format your card asks for, with file and page for every fact.",
             "files": ["jabriya-kyc-pack.pdf", "salwa-kyc-pack.pdf", "mirqab-client-acceptance-policy.docx",
                       "abdali-trial-balance-fy2025.xlsx", "mirqab-materiality-memo-abdali.docx",
                       "abdali-sales-listing-sample.xlsx", "abdali-invoices-sample.pdf",
                       "abdali-field-notes.docx", "mirqab-management-letter-template.docx"],
             "tool": "CLAUDE"},
            {"id": "1.4", "mins": 40, "title": "Build sprint 2: three tests, one fix",
             "steps": ["Run your three test cases. Write the expected answer first.",
                       "Note what failed.",
                       "Change one line of the instruction. Run all three tests again."],
             "look": "Version 2 of your instruction and a short test log: case, expected, actual, fixed.",
             "files": [], "tool": "CLAUDE"},
        ],
        "files": ["khiran-kyc-pack.pdf", "jabriya-kyc-pack.pdf", "salwa-kyc-pack.pdf", "mirqab-client-acceptance-policy.docx",
                  "abdali-trial-balance-fy2025.xlsx", "mirqab-materiality-memo-abdali.docx",
                  "abdali-sales-listing-sample.xlsx", "abdali-invoices-sample.pdf",
                  "abdali-field-notes.docx", "mirqab-management-letter-template.docx"],
    },
    {
        "n": 2,
        "date": "Mon 16 Nov 2026",
        "date_long": "Monday 16 November 2026",
        "title": "Turning Agents into Operational Workflows",
        "cat": "Workflows",
        "icon": "flow",
        "objective": "Convert the agent into a repeatable, automated workflow.",
        "lede": "Yesterday you built an agent. Today it runs on its own when the work arrives.",
        "brief": [
            "Day 2 starts from your Day 1 agent and the problem it still has: it waits for you. Then: triggers, workflows and "
            "integrations, a first n8n workflow, the KYC workflow from form to review table, your own team workflow, and Demo Day.",
        ],
        "build_today": "A working n8n workflow for your team's agent, shown live on Demo Day.",
        "bullets": [
            "Triggers, workflows and integrations",
            "Build in n8n: input → AI → output",
            "Your team's workflow, shown on Demo Day",
        ],
        "outcomes": [
            "Explain how a trigger, a workflow and an integration turn an agent into a system.",
            "Build an n8n workflow that connects a form, Claude and a result page.",
            "Ask Claude for named fields so the workflow can route each case.",
            "Adapt the workflow to your department's task and rules.",
            "Present your solution and choose the next task to automate, with an owner and a review rule.",
        ],
        "ros": [
            ("Callback: your agent waits for you", "08:30-08:45", "Five manual steps every time. Today we remove them"),
            ("From agent to system", "08:45-09:25", "Trigger, read, AI, decide, output. Where the human check sits"),
            ("Your first n8n workflow", "09:25-10:15", "Form → Claude → answer page, built by everyone"),
            ("BREAK", "10:15", ""),
            ("Workflow build: the KYC workflow", "10:30-12:00", "Upload a pack, read it, let Claude decide, route and record"),
            ("BREAK:Lunch and Dhuhr prayer", "12:00", ""),
            ("Customization: team build", "13:00-14:15", "Same skeleton, your department's job"),
            ("BREAK", "14:15", ""),
            ("Demo Day prep", "14:25-14:55", "A 3-minute demo in four beats"),
            ("Demo Day", "14:55-15:40", "Every team shows its workflow running"),
            ("Next steps", "15:40-15:55", "Owner, test set, review rule, and what to automate next"),
            ("MAP test (after) and final survey", "15:55-16:10", "10 minutes, then the survey"),
            ("Close", "16:10-16:30", "Input, instruction, output. Then a trigger"),
        ],
        "ros_note": "A guide, not a script. Breaks at 10:15 and 14:15; lunch and Dhuhr prayer at 12:00.",
        "tasks": [
            {"id": "2.1", "mins": 20, "title": "Build: form → Claude → answer page",
             "steps": ["Create a new workflow. Add the trigger On form submission with one field.",
                       "Add a Basic LLM Chain with the Anthropic Chat Model and the workshop credential.",
                       "Add a Form Ending page that shows Claude's answer. Test it."],
             "look": "You open the form, type a question, and the answer page shows Claude's reply.",
             "files": [], "tool": "N8N"},
            {"id": "2.2", "mins": 20, "title": "KYC workflow, part 1: form and file",
             "steps": ["Add the trigger On form submission with two fields: Client name and KYC pack (file).",
                       "Upload khiran-kyc-pack.pdf through the test form.",
                       "Add Extract from File (Extract From PDF). Run it and read the text."],
             "look": "The pack's text appears in the output panel of Extract from File.",
             "files": ["khiran-kyc-pack.pdf"], "tool": "N8N"},
            {"id": "2.3", "mins": 25, "title": "KYC workflow, part 2: Claude decides",
             "steps": ["Add a Basic LLM Chain with prompt 2.2 and your Day 1 instruction.",
                       "Attach the Anthropic Chat Model with the workshop credential.",
                       "Turn on a fixed output format with a Structured Output Parser. Run it."],
             "look": "The output has named fields: client, status, issues, summary.",
             "files": ["khiran-kyc-pack.pdf"], "tool": "N8N"},
            {"id": "2.4", "mins": 25, "title": "KYC workflow, part 3: route and record",
             "steps": ["Create two data tables: KYC review queue and KYC ready.",
                       "Add an IF on status, then one insert row step on each route.",
                       "Add a Form Ending with the summary. Run both packs from the form."],
             "look": "One pack lands in the review queue and the other lands in the ready list. Check that each one is right.",
             "files": ["khiran-kyc-pack.pdf", "salwa-kyc-pack.pdf"], "tool": "N8N"},
            {"id": "2.5", "mins": 60, "title": "Team build: your agent as a workflow",
             "steps": ["Copy the KYC workflow. Rename it after your agent.",
                       "Swap three things: the input, the instruction, the output fields and route.",
                       "Test with the practice files. Stretch: add a second route or a schedule."],
             "look": "Your team's workflow runs from start to finish on a practice file, with a human check before anything leaves.",
             "files": ["abdali-trial-balance-fy2025.xlsx", "abdali-sales-listing-sample.xlsx",
                       "abdali-invoices-sample.pdf", "abdali-field-notes.docx"], "tool": "N8N"},
            {"id": "2.6", "mins": 25, "title": "Prepare your demo",
             "steps": ["Fill the demo card: task, time before and after, live run, what is next.",
                       "Rehearse once with a timer.",
                       "Choose one presenter and one driver."],
             "look": "A 3-minute demo that runs live on a practice file.",
             "files": [], "tool": "DEMO CARD"},
        ],
        "files": ["khiran-kyc-pack.pdf", "salwa-kyc-pack.pdf", "jabriya-kyc-pack.pdf",
                  "abdali-trial-balance-fy2025.xlsx", "abdali-sales-listing-sample.xlsx",
                  "abdali-invoices-sample.pdf", "abdali-field-notes.docx"],
    },
]

# Sample files: name -> (description, day first used). Names never change.
FILES = [
    ("khiran-kyc-pack.pdf", "Khiran Logistics KYC pack: license, articles, shareholders, signatories, ID copies received", "1"),
    ("jabriya-kyc-pack.pdf", "Jabriya Medical Supplies KYC pack: the KYC team's practice case", "1"),
    ("salwa-kyc-pack.pdf", "Salwa Trading KYC pack: a complete pack, the normal test case", "1"),
    ("mirqab-client-acceptance-policy.docx", "The firm's Client Acceptance Policy: required documents, expiry rule, risk indicators", "1"),
    ("abdali-trial-balance-fy2025.xlsx", "Abdali Foods trial balance, FY2025 and FY2024", "1"),
    ("mirqab-materiality-memo-abdali.docx", "Materiality memo for the Abdali Foods audit", "1"),
    ("abdali-sales-listing-sample.xlsx", "Six sampled lines from the Abdali sales listing", "1"),
    ("abdali-invoices-sample.pdf", "The six matching sales invoices", "1"),
    ("abdali-field-notes.docx", "Rough field notes from the Abdali audit", "1"),
    ("mirqab-management-letter-template.docx", "The firm's management letter point format", "1"),
]

# The four agent cards (Day 1 use case selection, Day 2 team builds)
AGENTS = [
    {"key": "kyc", "kind": "Extraction", "area": "Onboarding", "name": "KYC intake checker",
     "input": "jabriya-kyc-pack.pdf", "knowledge": "mirqab-client-acceptance-policy.docx",
     "output": "A required-document table, risk flags, and one line: ready or not ready.",
     "short": "Pack + policy → document table, risk flags, ready or not"},
    {"key": "tb", "kind": "Analysis", "area": "Audit", "name": "TB movement reviewer",
     "input": "abdali-trial-balance-fy2025.xlsx", "knowledge": "mirqab-materiality-memo-abdali.docx",
     "output": "Accounts over the review threshold, the movement, and one question for the client each.",
     "short": "Trial balance + memo → flagged accounts, questions for the client"},
    {"key": "vouch", "kind": "Workflow", "area": "Audit", "name": "Invoice vouching assistant",
     "input": "abdali-invoices-sample.pdf", "knowledge": "abdali-sales-listing-sample.xlsx",
     "output": "A match table: invoice, date, customer, amount, match or mismatch, and why.",
     "short": "Listing + invoices → match table with mismatch flags"},
    {"key": "ml", "kind": "Reporting", "area": "Audit", "name": "Management letter writer",
     "input": "abdali-field-notes.docx", "knowledge": "mirqab-management-letter-template.docx",
     "output": "Findings in the firm's format: observation, risk, recommendation, management response left blank.",
     "short": "Field notes + template → findings in the firm's format"},
]

HABIT = {
    "title": "Input, instruction, output.",
    "lead": "The agent does the first pass. You sign the file.",
    "items": [
        ("Input.", "Name the exact file and the fields the agent reads."),
        ("Instruction.", "Role, steps, rules, what to do when unsure, output."),
        ("Output.", "A fixed format a reviewer can check in two minutes."),
    ],
}

# MAP links: filled after the surveys are published (section 10 of the skill)
MAP = {
    "pre": {"name": "Pre-MAP test", "when": "Day 1 · Sun 15 Nov · 08:45", "id": "763ba655-010d-48b6-a83b-1f56e2ca3825",
            "slug": "coded-rsm-albazie-ai-innovation-and-automation-map-test-pre-day-1", "url": ""},
    "post": {"name": "Post-MAP test", "when": "Day 2 · Mon 16 Nov · 15:55", "id": "775a002d-c926-4bb6-92d3-956c751139de",
             "slug": "coded-rsm-albazie-ai-innovation-and-automation-map-test-post-day-2", "url": ""},
    "survey": {"name": "Final satisfaction survey", "when": "Day 2 · right after the post-MAP test", "id": "fb337765-7220-49c0-a508-1f955343f9cd",
               "slug": "coded-rsm-albazie-ai-innovation-and-automation-final-satisfaction-survey", "url": ""},
}
PORTAL_FOLDER = "e07488c7-5525-403f-a2c6-f6db15ae710a"   # AI Innovation and Automation (Nov 26)
# After survey_publish: set each url to https://platform.joincoded.com/sv/<slug>, rebuild, validate.
