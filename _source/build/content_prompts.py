# -*- coding: utf-8 -*-
"""Every prompt, instruction and template, in teaching order. The prompt sheets, the decks and the
take-aways all read from here, so the wording is the same everywhere."""

KYC_INSTRUCTION = """ROLE
You are a client onboarding assistant at Mirqab & Co., an audit firm in Kuwait. You check a new client's KYC document pack against the firm's Client Acceptance Policy (in the project knowledge).

STEPS
1. List every document in the pack. For each one, record its type, who it belongs to, and its expiry date if it has one.
2. Compare the list with the required documents in Section 2 of the policy. Mark each one Present, Missing or Expired.
3. Check every expiry date against today's date. Flag any document that has expired or expires within 60 days.
4. Find the ultimate beneficial owners: people who own 25% or more, directly or through a company.
5. Check the high-risk indicators in Section 4 of the policy. Quote the line in the pack that triggers each one.

RULES
- Use only the documents in this chat and the policy. No outside knowledge.
- Give the file name and page for every fact.
- Do not decide whether to accept the client. A partner makes that decision.

IF UNSURE
If a document or a fact is not in the pack, write "Not found". Never guess a date, a name or a percentage.

OUTPUT
1. A table: Required document | Status (Present, Missing, Expired) | Evidence (file and page) | Note
2. Risk flags: one line each, with the policy section and the quote.
3. One last line: "Ready for partner review" or "Not ready: [number] items to resolve"."""

TB_INSTRUCTION = """ROLE
You are an audit assistant at Mirqab & Co., an audit firm in Kuwait. You review the movements in a client's trial balance before fieldwork.

STEPS
1. Check that total debits equal total credits for each year. Report the totals.
2. For each account, calculate the movement: FY2025 minus FY2024, in KWD and as a percentage.
3. Use the review threshold in the materiality memo (in the project knowledge). Flag an account only if it passes both tests in the memo.
4. For each flagged account, write one clear question for the client's finance team.

RULES
- Use only the trial balance and the memo. No outside knowledge about the client.
- Show your calculation for every flagged account.
- Amounts in KWD with three decimals.
- Do not say an account is wrong. You flag; the auditor decides.

IF UNSURE
If an account is zero in one year, flag it as "New account" or "Closed account". If a number is missing, write "Not found". Never guess.

OUTPUT
1. One line per year: total debits, total credits, balanced or not.
2. A table: Account | FY2025 | FY2024 | Movement (KWD) | Movement (%) | Question for the client
3. One last line: "[number] accounts flagged"."""

VOUCH_INSTRUCTION = """ROLE
You are an audit assistant at Mirqab & Co., an audit firm in Kuwait. You vouch sales invoices to the client's sales listing for the Abdali Foods audit. The year end is 31 December 2025.

STEPS
1. Read the six lines of the sales listing sample: invoice number, date, customer, amount.
2. Find each invoice in the invoice PDF by its invoice number.
3. Compare four fields: invoice number, date, customer name, amount.
4. Check cut-off: flag any invoice dated after 31 December 2025 that the listing records in FY2025.

RULES
- Compare exact values. 12,540.000 and 12,450.000 are different amounts.
- Give the PDF page for every invoice.
- Do not correct the listing. Report what you see.

IF UNSURE
If an invoice is not in the PDF, write "Not found". If a customer name is close but not the same, write "Check" and show both names.

OUTPUT
1. A table: Invoice | Listing date | Invoice date | Listing customer | Invoice customer | Listing amount | Invoice amount | Result (Match, Mismatch, Check) | Page
2. Mismatches: one line each, with the difference.
3. One last line: "[number] of 6 invoices match"."""

ML_INSTRUCTION = """ROLE
You are an audit senior at Mirqab & Co., an audit firm in Kuwait. You turn rough field notes into management letter points in the firm's format (in the project knowledge).

STEPS
1. Read the field notes. Find each separate control finding.
2. For each finding, write: Title, Observation, Risk rating, Risk, Recommendation, Management response.
3. Use the risk ratings and definitions in the management letter template.

RULES
- Facts only. Use the numbers in the notes, for example "4 of 25 samples".
- Neutral, professional tone. No blame.
- Never name a person. Use the role, for example "the accounts payable clerk".
- Management response is always "[To be completed by management]".
- One finding per point. Leave out notes that are not control findings.

IF UNSURE
If the notes do not give enough facts for a finding, write "More information needed:" and the question to ask.

OUTPUT
Each point in this order: Title · Observation · Risk rating (High, Medium or Low) · Risk · Recommendation · Management response.
Then one list: "Notes left out, and why"."""

INSTRUCTIONS = {"kyc": KYC_INSTRUCTION, "tb": TB_INSTRUCTION, "vouch": VOUCH_INSTRUCTION, "ml": ML_INSTRUCTION}

AGENT_CARD = """AGENT CARD
Name:
Job (one sentence):
Input (file name, fields, format):
Knowledge (the policy, memo or template it follows):

INSTRUCTION
Role:
Steps (numbered):
Rules:
If unsure:
Output (columns or sections, in order):

TESTS (write the expected answer first)
1. Normal case:
2. Missing data:
3. Trap:

REVIEWER CHECK
What a person checks before anyone uses the output:"""

TASK_FINDER = """You are a process analyst. Help me find the tasks in my work that an AI agent could do.
Ask me 5 questions, one at a time, about my last two weeks of work in [audit / onboarding].
Then list my repetitive tasks in a table:
Task | How often | Minutes each time | Input (file or system) | Rules written down? (yes or no) | Can a reviewer check it in 2 minutes? (yes or no)
Do not suggest tools yet."""

CRITIC = """Here is the instruction for my agent. Act as a strict reviewer.
Find up to 3 places where the agent could guess, skip a step, or give an output a reviewer cannot check quickly.
For each one, quote the line and suggest a better line. Do not rewrite the whole instruction.

[paste your instruction here]"""

N8N_FIRST_PROMPT = """{{ $json['Your question'] }}"""
N8N_FIRST_ENDING = """{{ $json.text }}"""

KYC_POLICY_SUMMARY = """POLICY RULES (from the Client Acceptance Policy, Sections 2 and 4)
Required documents for a W.L.L.: 1. Commercial license, valid. 2. Articles of association. 3. Shareholder register. 4. ID copy for every person who is a shareholder, an ultimate beneficial owner or an authorized signatory. 5. Authorized signatory list. 6. For every company shareholder: its registration certificate and its own shareholder list.
Expiry rule: flag a document that has expired or expires within 60 days.
High-risk indicators: (a) ownership through a company registered outside Kuwait; (b) a politically exposed person; (c) a cash-intensive business; (d) a sector in Appendix A; (e) documents that do not match each other, for example different names or numbers."""

N8N_KYC_PROMPT = """[Paste your Day 1 KYC instruction here, from ROLE to IF UNSURE.]

""" + KYC_POLICY_SUMMARY + """

Today's date: {{ $now.toFormat('dd LLL yyyy') }}
Client name from the form: {{ $('On form submission').item.json['Client name'] }}

The KYC pack, as text:
{{ $json.text }}

Fill every field in the output format. status is "Needs review" if anything is Missing, Expired or flagged. Otherwise status is "Ready"."""

N8N_KYC_SCHEMA = """{
  "client": "Example Client W.L.L.",
  "status": "Needs review",
  "items_to_resolve": 2,
  "issues": ["Example: Articles of association missing (no page)", "Example: Signatory ID copy expires within 60 days (page 4)"],
  "risk_flags": ["Example: Section 4(a), company shareholder registered outside Kuwait (page 3)"],
  "summary": "Not ready: 2 items to resolve"
}"""

N8N_IF_CONDITION = """{{ $json.output.status }}   is equal to   Needs review"""

N8N_ROW_MAPPING = """client           {{ $json.output.client }}
status           {{ $json.output.status }}
items_to_resolve {{ $json.output.items_to_resolve }}
issues           {{ $json.output.issues.join('; ') }}
risk_flags       {{ $json.output.risk_flags.join('; ') }}
checked_at       {{ $now.toISO() }}"""

N8N_ENDING = """{{ $('Basic LLM Chain').item.json.output.summary }}"""

N8N_TB_PROMPT = """[Paste your Day 1 TB instruction here, from ROLE to IF UNSURE.]

REVIEW THRESHOLD (from the materiality memo): flag an account only if the movement is more than 10% AND more than KWD 45,000.

The trial balance rows, as data:
{{ JSON.stringify($json.data) }}

Fill every field in the output format. status is "Needs review" if any account is flagged."""

N8N_TB_SCHEMA = """{
  "client": "Example Client Co.",
  "status": "Needs review",
  "balanced": true,
  "flagged": [{"account": "Example account", "movement_kwd": 50000.000, "movement_pct": 25.0, "question": "Example question for the client"}],
  "summary": "1 account flagged"
}"""

N8N_VOUCH_PROMPT = """[Paste your Day 1 vouching instruction here, from ROLE to IF UNSURE.]

The sales listing lines, pasted from Excel:
{{ $('On form submission').item.json['Sales listing lines'] }}

The invoices, as text:
{{ $json.text }}

Fill every field in the output format. status is "Needs review" if any result is Mismatch or Check."""

N8N_VOUCH_SCHEMA = """{
  "status": "Needs review",
  "matched": 5,
  "results": [{"invoice": "EX-0001", "result": "Mismatch", "difference": "Example: amount 1,200.000 on listing, 1,020.000 on invoice", "page": 1}],
  "summary": "5 of 6 invoices match"
}"""

N8N_ML_PROMPT = """[Paste your Day 1 management letter instruction here, from ROLE to IF UNSURE.]

FORMAT RULES (from the management letter template): Risk rating High = could lead to a material error or a loss; Medium = weakens a key control; Low = good practice. Management response is always "[To be completed by management]".

The field notes:
{{ $json['Field notes'] }}

Fill every field in the output format. status is "Draft for review" for every run."""

N8N_ML_SCHEMA = """{
  "status": "Draft for review",
  "points": [{"title": "Example title", "observation": "Example observation", "risk_rating": "Medium", "risk": "Example risk", "recommendation": "Example recommendation", "management_response": "[To be completed by management]"}],
  "left_out": ["Example: a scheduling note, not a control finding"],
  "summary": "1 point drafted"
}"""

DEMO_CARD = """DEMO CARD (3 minutes)
1. The task (30 seconds): Who does it today? How often?
2. Before and after (30 seconds): Minutes per case today: ___. With the workflow: ___.
3. Live run (90 seconds): Which practice file? What should the audience look at?
4. Next (30 seconds): The human check: who checks what, and when?
   The next task we would automate: ___"""

BACKLOG = """Here is my list of candidate tasks from Day 1, with the four answers for each.
Score each task from 1 to 5 for value (time saved, risk reduced) and from 1 to 5 for ease (clear input, written rules, easy check).
Return a table sorted by value × ease. Then suggest the one task to pilot next, with one sentence on why.

[paste your list here]"""

# Prompt sheet cards, in teaching order. kind: prompt (COPY), template (COPY), n8n (COPY, n8n field)
# Each card: id, block, time, title, when (steps), prompt, label, files, look (hint), tool, team
PROMPTS = {
    1: [
        {"id": "1.1", "block": "Opener", "time": "08:30", "title": "The weak instruction (demo)",
         "when": ["Trainer demo. New chat in Claude, no project.", "Attach khiran-kyc-pack.pdf, then send the line below."],
         "prompt": "Check this KYC pack.", "label": "Prompt",
         "files": ["khiran-kyc-pack.pdf"], "look": "A friendly paragraph. Can you act on it? What did it check?", "tool": "Claude"},
        {"id": "1.2", "block": "Opener", "time": "08:35", "title": "The designed instruction (demo)",
         "when": ["Same file, new chat.", "Paste the whole instruction below, then attach the pack."],
         "prompt": KYC_INSTRUCTION, "label": "Instruction",
         "files": ["khiran-kyc-pack.pdf", "mirqab-client-acceptance-policy.docx"],
         "look": "A table you can check line by line, and a clear last line.", "tool": "Claude"},
        {"id": "1.3", "block": "Reframing work", "time": "09:55", "title": "Find your repetitive tasks", "team": False,
         "when": ["Your turn 1.1. Use this if you want help listing tasks.", "Answer the five questions about your own work. Use no client names."],
         "prompt": TASK_FINDER, "label": "Prompt", "files": [],
         "look": "A table of your tasks. Then score each one with the four questions on the slide.", "tool": "Claude"},
        {"id": "1.4", "block": "Agent Design Framework", "time": "11:15", "title": "The Agent Card",
         "when": ["Your turn 1.2. Copy the card into a note or a chat and fill every line.",
                  "Every line must be specific: a file name, numbered steps, named output columns."],
         "prompt": AGENT_CARD, "label": "Template", "files": [],
         "look": "Could a new joiner run your card without asking you a question?", "tool": "Notes or Claude"},
        {"id": "1.5", "block": "Build in Claude", "time": "13:35", "title": "Starter instruction: KYC intake checker", "team": True,
         "when": ["Your turn 1.3, team KYC. Create a project, paste this into the project instructions.",
                  "Add mirqab-client-acceptance-policy.docx to the project knowledge. New chat, attach jabriya-kyc-pack.pdf."],
         "prompt": KYC_INSTRUCTION, "label": "Project instructions",
         "files": ["jabriya-kyc-pack.pdf", "salwa-kyc-pack.pdf", "mirqab-client-acceptance-policy.docx"],
         "look": "Every required document has a status and a page. Check every expiry date yourself.", "tool": "Claude Project"},
        {"id": "1.6", "block": "Build in Claude", "time": "13:35", "title": "Starter instruction: TB movement reviewer", "team": True,
         "when": ["Your turn 1.3, team TB. Create a project, paste this into the project instructions.",
                  "Add mirqab-materiality-memo-abdali.docx to the project knowledge. New chat, attach the trial balance."],
         "prompt": TB_INSTRUCTION, "label": "Project instructions",
         "files": ["abdali-trial-balance-fy2025.xlsx", "mirqab-materiality-memo-abdali.docx"],
         "look": "The memo has two tests. Check one flagged account against both of them yourself.", "tool": "Claude Project"},
        {"id": "1.7", "block": "Build in Claude", "time": "13:35", "title": "Starter instruction: Invoice vouching assistant", "team": True,
         "when": ["Your turn 1.3, team Vouching. Create a project, paste this into the project instructions.",
                  "Add the sales listing to the project knowledge. New chat, attach the invoice PDF."],
         "prompt": VOUCH_INSTRUCTION, "label": "Project instructions",
         "files": ["abdali-sales-listing-sample.xlsx", "abdali-invoices-sample.pdf"],
         "look": "Read every amount digit by digit, and every date against the year end.", "tool": "Claude Project"},
        {"id": "1.8", "block": "Build in Claude", "time": "13:35", "title": "Starter instruction: Management letter writer", "team": True,
         "when": ["Your turn 1.3, team ML. Create a project, paste this into the project instructions.",
                  "Add mirqab-management-letter-template.docx to the project knowledge. New chat, attach the field notes."],
         "prompt": ML_INSTRUCTION, "label": "Project instructions",
         "files": ["abdali-field-notes.docx", "mirqab-management-letter-template.docx"],
         "look": "Every point in the firm's order. Look for any person's name in the output.", "tool": "Claude Project"},
        {"id": "1.9", "block": "Test and improve", "time": "14:35", "title": "Ask a strict reviewer", "team": False,
         "when": ["Your turn 1.4. Use this before you change your instruction.",
                  "Paste your current instruction where the brackets are."],
         "prompt": CRITIC, "label": "Prompt", "files": [],
         "look": "Change one line at a time, then run all three tests again.", "tool": "Claude"},
    ],
    2: [
        {"id": "2.1", "block": "Your first n8n workflow", "time": "09:40", "title": "Form → Claude → answer page",
         "when": ["Your turn 2.1. Trigger: On form submission, one field named Your question.",
                  "Basic LLM Chain: set the prompt to the line below. Form Ending: show the second line."],
         "prompt": N8N_FIRST_PROMPT, "label": "Basic LLM Chain · prompt",
         "extra": [("Form Ending · message", N8N_FIRST_ENDING)],
         "files": [], "look": "Drag the field from the left panel instead of typing it. The name must match exactly.", "tool": "n8n"},
        {"id": "2.2", "block": "Workflow build", "time": "10:55", "title": "KYC workflow: Claude decides (part 2)",
         "when": ["Your turn 2.3. Add a Basic LLM Chain after Extract from File.",
                  "Paste your Day 1 instruction at the top. Turn on Require Specific Output Format and add a Structured Output Parser."],
         "prompt": N8N_KYC_PROMPT, "label": "Basic LLM Chain · prompt",
         "extra": [("Structured Output Parser · JSON example", N8N_KYC_SCHEMA)],
         "files": ["khiran-kyc-pack.pdf", "salwa-kyc-pack.pdf"],
         "look": "In n8n there is no project knowledge. The policy rules must be in the prompt.", "tool": "n8n"},
        {"id": "2.3", "block": "Workflow build", "time": "11:25", "title": "KYC workflow: route and record (part 3)",
         "when": ["Your turn 2.4. IF after the chain. True: insert a row in KYC review queue. False: insert a row in KYC ready.",
                  "Then a Form Ending page with the summary."],
         "prompt": N8N_IF_CONDITION, "label": "IF · condition",
         "extra": [("Data table · insert row (both tables)", N8N_ROW_MAPPING), ("Form Ending · message", N8N_ENDING)],
         "files": ["khiran-kyc-pack.pdf", "salwa-kyc-pack.pdf", "jabriya-kyc-pack.pdf"],
         "look": "Run both packs. Open both data tables. One row each, in the right table.", "tool": "n8n"},
        {"id": "2.4", "block": "Customization", "time": "13:05", "title": "Team TB: trial balance workflow", "team": True,
         "when": ["Your turn 2.5, team TB. Form: one file field. Extract from File: Extract From XLSX. Then Aggregate: All Item Data, into the field data.",
                  "Basic LLM Chain with the prompt below and this JSON example. Route on status."],
         "prompt": N8N_TB_PROMPT, "label": "Basic LLM Chain · prompt",
         "extra": [("Structured Output Parser · JSON example", N8N_TB_SCHEMA)],
         "files": ["abdali-trial-balance-fy2025.xlsx"],
         "look": "Without Aggregate, Claude runs once per row. One run for the whole trial balance is what you want.", "tool": "n8n"},
        {"id": "2.5", "block": "Customization", "time": "13:05", "title": "Team Vouching: invoice workflow", "team": True,
         "when": ["Your turn 2.5, team Vouching. Form: a text area named Sales listing lines and a file field for the invoice PDF.",
                  "Extract from File: Extract From PDF. Basic LLM Chain with the prompt below. Route on status."],
         "prompt": N8N_VOUCH_PROMPT, "label": "Basic LLM Chain · prompt",
         "extra": [("Structured Output Parser · JSON example", N8N_VOUCH_SCHEMA)],
         "files": ["abdali-sales-listing-sample.xlsx", "abdali-invoices-sample.pdf"],
         "look": "Copy the six listing rows from Excel, with the header row, into the text area.", "tool": "n8n"},
        {"id": "2.6", "block": "Customization", "time": "13:05", "title": "Team ML: management letter workflow", "team": True,
         "when": ["Your turn 2.5, team ML. Form: a text area named Field notes. No file step: n8n cannot read .docx files, so paste the text.",
                  "Basic LLM Chain with the prompt below. Every run goes to a Drafts table for a reviewer."],
         "prompt": N8N_ML_PROMPT, "label": "Basic LLM Chain · prompt",
         "extra": [("Structured Output Parser · JSON example", N8N_ML_SCHEMA)],
         "files": ["abdali-field-notes.docx"],
         "look": "No IF needed: every draft goes to a person. That is your human check.", "tool": "n8n"},
        {"id": "2.7", "block": "Demo Day prep", "time": "14:25", "title": "The demo card",
         "when": ["Your turn 2.6. Fill it as a team.", "Rehearse once with a 3-minute timer."],
         "prompt": DEMO_CARD, "label": "Template", "files": [],
         "look": "Show the workflow running, not the slides about it.", "tool": "Notes"},
        {"id": "2.8", "block": "Next steps", "time": "15:40", "title": "What to automate next", "team": False,
         "when": ["Use your task list from Day 1, your turn 1.1.", "Use no client names."],
         "prompt": BACKLOG, "label": "Prompt", "files": [],
         "look": "A short list with one clear first pick, an owner and a review rule.", "tool": "Claude"},
    ],
}
