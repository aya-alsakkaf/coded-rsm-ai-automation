# -*- coding: utf-8 -*-
"""Every demo and hands-on task of the RSM workshop: prompts, expected results, backups, answer keys and prompt-player data.
Numbers come from data.py, so the decks, prompt sheets, runbooks, backups and answer keys always agree."""
import data as D
from data import kwd, num

# ------------------------------------------------------------------ the sample files (names never change once published)
F_LETTER = "abdali-engagement-letter-2026.docx"
F_INV = "abdali-supplier-invoices-oct-2026.pdf"
F_LEDGER = "abdali-purchase-ledger-oct-2026.xlsx"
F_TEMPLATE = "mirqab-invoice-match-template.xlsx"
F_LEASES = "abdali-lease-agreements.pdf"
F_TB = "abdali-trial-balance-fy2024-fy2025.xlsx"
F_PBC = "mirqab-pbc-request-list-abdali.xlsx"
F_EMAILS = "abdali-client-emails-nov-2026.docx"
F_STATUS = "mirqab-engagement-status-wk46.xlsx"
F_M_INV = "abdali-invoice-messy.pdf"
F_M_LEASE = "abdali-lease-messy.pdf"
F_M_TB = "abdali-trial-balance-messy.xlsx"
F_M_EMAIL = "abdali-client-email-messy.docx"
F_M_STATUS = "mirqab-engagement-status-messy.xlsx"
F_STARTER = "mirqab-starter-instructions.docx"
F_RULES = "mirqab-review-rules.docx"
F_INV2 = "abdali-supplier-invoices-nov-wk1.pdf"
F_LEDGER2 = "abdali-purchase-ledger-nov-wk1.xlsx"
F_LEASE2 = "abdali-lease-agreement-new.pdf"
F_MGMT = "abdali-management-accounts-oct-2026.xlsx"
F_EMAILS2 = "abdali-client-emails-wk47.docx"
F_STATUS2 = "mirqab-engagement-status-wk47.xlsx"
F_LOCKED = "mirqab-locked-test-file.pdf"
ALL_FILES = [F_LETTER, F_INV, F_LEDGER, F_TEMPLATE, F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS, F_M_INV, F_M_LEASE, F_M_TB, F_M_EMAIL, F_M_STATUS,
             F_STARTER, F_RULES, F_INV2, F_LEDGER2, F_LEASE2, F_MGMT, F_EMAILS2, F_STATUS2, F_LOCKED]
TRACK_FILES = {"Extraction": [F_LEASES], "Analysis": [F_TB], "Workflow": [F_PBC, F_EMAILS], "Reporting": [F_STATUS]}
MESSY_FILES = [F_M_INV, F_M_LEASE, F_M_TB, F_M_EMAIL, F_M_STATUS]
BATCH2_FILES = [F_INV2, F_LEDGER2, F_LEASE2, F_MGMT, F_EMAILS2, F_STATUS2]

# prompt sheet sections: sec -> (day, name)
BLOCK = {1: (1, "Opener"), 2: (1, "Lesson 1 · AI foundations"), 3: (1, "Lesson 2 · Why chat isn't enough"), 4: (1, "Lesson 3 · Pick and design"),
         5: (1, "Lesson 4 · Build your agent"), 6: (1, "Lesson 5 · Build: Input and Output"), 7: (1, "Lesson 6 · Build: Package"), 8: (1, "Lesson 7 · Show and tell"),
         9: (2, "Lesson 1 · From agent to system"), 10: (2, "Lesson 2 · Make it run on its own"), 11: (2, "Lesson 3 · New inputs, outputs and n8n"),
         12: (2, "Lesson 4 · Fit it to your department"), 13: (2, "Lesson 5 · Test and prepare the demo")}

DEMOS = {}
def demo(did, **kw):
    kw.setdefault("stretch", []); kw.setdefault("stretch_prompts", []); kw.setdefault("files", [])
    kw["card"] = ("Task " if kw.get("hands_on") else "Demo ") + kw["skill"]
    DEMOS[did] = kw
def tbl(head, rows): return ("table", [head] + [list(r) for r in rows])
def joined(parts): return " ".join(f"{k}: {v}" for k, v in parts)

# ===================================================================== the instructions (one place: opener, players, sheets, starter file)
OPENER_PARTS = [["Role", "You are an audit associate at Mirqab & Co."],
                ["Steps", "Read the attached invoice. Find the supplier, the invoice number, the date, the PO number and the amount."],
                ["Rules", "Use only the invoice. Give the amount in KWD with three decimals. Do not round."],
                ["Format", "One table row: Supplier, Invoice no., Date, PO no., Amount (KWD)."],
                ["When unsure", "If a field is not on the invoice, write Not found. Never guess."]]
INVOICE_AGENT = [["Role", "You are an audit associate at Mirqab & Co. You match a client's supplier invoices to its purchase ledger."],
                 ["Steps", "1. Read every invoice in the pack. 2. Find each invoice number in the purchase ledger. 3. Compare the date and the amount in KWD."],
                 ["Rules", "Use only the attached files. Show amounts in KWD with three decimals. Never round, change or convert an amount. Any difference of 0.001 or more counts."],
                 ["Output format", "One table in the columns of the template in the project knowledge. Status is one of: Matched, Amount differs, Not in ledger, Not found."],
                 ["When unsure", "If a field is missing or unclear, write Not found and explain it in the Note column. Never guess."]]
CARD_INVOICE = [["Input", "The month's supplier invoices (PDF) and the purchase ledger (Excel)."],
                ["Instruction", "Match each invoice to the ledger by number. Compare date and amount. Flag every difference. Never guess."],
                ["Output", "One table in the Mirqab template, with a status for every invoice."],
                ["When", "Empty for now. Day 2 fills it."]]
STARTER = {
 "Extraction": [["Role", "You are an audit associate at Mirqab & Co. You extract key terms from lease agreements."],
                ["Steps", "1. Read each lease. 2. Find the premises, lessor, start date, end date, monthly rent and deposit. 3. Find any clause that changes the rent or the term."],
                ["Rules", "Use only the attached leases. Dates as YYYY-MM-DD. Amounts in KWD with three decimals. Quote any special clause word for word."],
                ["Output format", "One table: Lease, Premises, Lessor, Start, End, Monthly rent (KWD), Deposit (KWD), Special terms."],
                ["When unsure", "If a term is missing or unclear, write Not found and flag the lease. Never guess."]],
 "Analysis": [["Role", "You are an audit associate at Mirqab & Co. You review movements in a client's trial balance."],
              ["Steps", "1. For each account, calculate the change in KWD and in percent. 2. Flag accounts where the change is over 10% and over KWD 5,000. 3. Write one question for the client for each flagged account."],
              ["Rules", "Use only the attached trial balance. Calculate with code. Flag only when both limits are passed. Accounts that move together may be a reclassification: say so."],
              ["Output format", "One table: Account, FY2024, FY2025, Change (KWD), Change (%), Flag, Question for the client."],
              ["When unsure", "If a figure is missing, write Not found and do not calculate that account. Never treat a blank as zero."]],
 "Workflow": [["Role", "You are a project coordinator at Mirqab & Co. You track the documents a client has sent against the request list."],
              ["Steps", "1. Read the request list. 2. Read every client email and its attachment names. 3. Mark each request Received, Partly received or Outstanding. 4. Draft one follow-up email for each request that is not fully received."],
              ["Rules", "Use only the attached files. A request is Received only if the right document for the right period is attached. Follow-ups are drafts: never send."],
              ["Output format", "A tracker table: No., Item, Due, Status, Evidence (email date and file), Note. Then the follow-up drafts, one per item."],
              ["When unsure", "If an email says attached but no file is listed, mark the item Partly received and say why. Never guess."]],
 "Reporting": [["Role", "You are a project coordinator at Mirqab & Co. You prepare the weekly engagement summary for the manager."],
               ["Steps", "1. Read the status sheet. 2. For each engagement, calculate hours used against budget. 3. Find the next deadline and the open items."],
               ["Rules", "Use only the attached sheet. Show hours as whole numbers and the budget use in percent. Over budget means used hours above the budget."],
               ["Output format", "A table: Engagement, Type, Budget (h), Used (h), Used (%), Open items, Next deadline. Then three lines: over budget, deadlines this week, what needs the manager."],
               ["When unsure", "If a budget or an hour figure is blank, write Not found and flag it. Never guess."]],
}
TRACKS = [("Extraction", "Lease agreements → a key-terms schedule", F_LEASES, "6 leases, 2 with unusual clauses"),
          ("Analysis", "Two-year trial balance → movements over the threshold, with questions for the client", F_TB, "24 accounts; flag over 10% and over KWD 5,000"),
          ("Workflow", "Request list and client emails → status tracker and follow-up drafts", f"{F_PBC} · {F_EMAILS}", "15 requests, 10 emails"),
          ("Reporting", "Engagement status sheets → one weekly summary for a manager", F_STATUS, "3 engagements")]
FIVE_TEMPLATE = ("Role: You are a [job title] at Mirqab & Co. You [the task in one line]. "
                 "Steps: 1. [read what] 2. [find or compare what] 3. [decide or flag what]. "
                 "Rules: Use only the attached files. [Units, decimals, dates.] [What counts as a difference.] "
                 "Output format: [table columns, in order] [any total line]. "
                 "When unsure: If a field is missing or unclear, write Not found and flag it. Never guess.")
SCHED_PROMPT = (f"Use the [your skill name] skill. Read the new files in Google Drive: {D.SANDBOX} / [your team folder] / Inbox. "
                "Save the result as an Excel file in [your team folder] / Outputs, named [client]-[task]-YYYY-MM-DD-HHMM.xlsx, with the date and time of the run. "
                "Move each file you read to [your team folder] / Processed. "
                "Save a run-log file in [your team folder] / Log, named runlog-YYYY-MM-DD-HHMM.txt, with one line: date, files read, items flagged, file saved. "
                "If there are no new files: write No new files in the run log and stop.")
INVOICE_SCHED = (f"Use the mirqab-invoice-match skill. Read the new files in Google Drive: {D.SANDBOX} / 01 Invoices / Inbox. "
                 "Save the result as an Excel file in 01 Invoices / Outputs, named abdali-invoice-match-YYYY-MM-DD-HHMM.xlsx, with the date and time of the run. "
                 "Move each file you read to 01 Invoices / Processed. "
                 "Save a run-log file in 01 Invoices / Log, named runlog-YYYY-MM-DD-HHMM.txt, with one line: date, files read, items flagged, file saved. "
                 "If there are no new files: write No new files in the run log and stop.")

FALLBACK_LINE = ("If a file cannot be read, do not guess. Write Could not read: [file name] in the run log, leave the file in the Inbox "
                 "and go on. A person checks it by hand.")
RUBRIC_FULL = [("Task relevance", 10, "A real, repeated task with a measured cost"), ("Working functionality", 10, "Saved on the Scheduled page, runs on demand, same shape every run"),
               ("Source accuracy", 10, "Three figures the panel picks all match the source files"), ("Human controls", 10, "Drafts only, your rules, a named reviewer signs off"),
               ("Test evidence", 10, "Run log: three clean runs, the empty folder and a failed run")]
RUBRIC_SCORE = [("Task relevance", "Real task, measured cost", "Real task, no number", "Made-up task"), ("Working functionality", "Scheduled, runs on demand, same shape", "Runs in a chat only", "Does not run"),
                ("Source accuracy", "3 of 3 figures match", "2 of 3 match", "1 or none match"), ("Human controls", "Drafts, rules, named reviewer", "Reviewer, no rules", "No review step"),
                ("Test evidence", "Clean, empty and failed runs logged", "Some of these runs logged", "No run log")]

MATCH_TABLE = [D.TEMPLATE_HEAD[:1] + ["Invoice (KWD)", "Ledger (KWD)", "Difference", "Status"]] + \
              [[r[0], num(r[3]), num(r[4]) if r[4] is not None else "Not found", num(r[5]) if r[5] is not None else "", r[6]] for r in D.MATCH]
MATCH_FULL = [(r[0], r[1], r[2], D.INV[r[0]][3] or "Not found", num(r[3]), num(r[4]) if r[4] is not None else "Not found", num(r[5]) if r[5] is not None else "", r[6], r[7]) for r in D.MATCH]
def _mv(a):
    m = next(x for x in D.MOVES if x[0] == a)
    side = f" (the liability fell from {abs(m[2]):,} to {abs(m[3]):,}; accept either sign)" if m[1] == "Liabilities" else ""
    return f"{a}: {m[4]:+,} KWD ({m[5]:.1f}%){side}, " + ("flagged" if m[6] else "not flagged (under KWD 5,000)")
def _st(r): return f"{r[0].split(' Co.')[0]}: {r[3]} of {r[2]} hours ({round(r[3] / r[2] * 100)}%)"
CHECK3 = [("Extraction", "Leases 1, 4 and 6", "Lease 1: option to renew for 3 years. Lease 4: no rent from 1 April to 30 June 2026. Lease 6: the landlord may end it with 60 days' notice."),
          ("Analysis", "Trade receivables, Accrued expenses, Bank charges", "; ".join(_mv(a) for a in ("Trade receivables", "Accrued expenses", "Bank charges")) + ". Accrued expenses moves with Other payables: ask about a reclassification."),
          ("Workflow", "Items 5, 7 and 8", "5: Partly received (the September listing came). 7: Partly received (nothing attached; accept Outstanding). 8: Outstanding (board minutes next week)."),
          ("Reporting", "The three engagements", "; ".join(_st(r) for r in D.STATUS46) + ". Khiran is " + str(D.OVER_BUDGET[0][1]) + "% over budget.")]
MOVE_ROWS = [(m[0], f"{m[2]:,}", f"{m[3]:,}", f"{m[4]:+,}", f"{m[5]:.1f}%") for m in D.MOVES if m[6]]

# ===================================================================== DAY 1
demo("t11", day=1, skill="1.1", sec=2, title="First Claude chat", tool="Claude", files=[F_LETTER], kind="task", hands_on=True, minutes=7, solo="on your own",
 setup=["Open claude.ai. Start a new chat and attach abdali-engagement-letter-2026.docx with the + button.", "Ask the three questions below, one at a time.",
        "Check one answer against the letter yourself."],
 prompts=[("1 · Summary", "Summarize the attached engagement letter in 5 lines."),
          ("2 · Dates", "List every date and deadline in the letter, with what happens on each date."),
          ("3 · What is missing", "Name the sections a standard audit engagement letter includes that this one does not. Quote the section headings you used.")],
 expected=f"A 5-line summary; the dates (letter {D.LETTER_DATE}, financial year end {D.LETTER['fy_end']}, sign by {D.LETTER['sign_by']}, interim work {D.LETTER['interim']}, year-end work {D.LETTER['year_end_work']}, report by {D.LETTER['report']}); and the missing section: {D.LETTER_MISSING.split(' (')[0].lower()}.",
 say="Three questions, one file. Then you check one answer yourself.",
 point="Ask, read, then check against the source.",
 backup=[("h", "Typical answers"), ("ul", [f"Dates: letter {D.LETTER_DATE}; financial year end {D.LETTER['fy_end']}; sign and return by {D.LETTER['sign_by']}; interim work {D.LETTER['interim']}; year-end work {D.LETTER['year_end_work']}; report by {D.LETTER['report']}.",
                                           f"Missing: a section on {D.LETTER_MISSING.lower()}."])],
 answer=[("h", "The planted gap"), ("p", f"The letter has no section on {D.LETTER_MISSING.lower()}. Its eight headings are: " + "; ".join(D.LETTER_SECTIONS) + "."),
         ("note", "Must find: management's responsibilities. Also accept other standard sections Claude may name (inherent limitations of an audit, written representations) as extras."),
         ("h", "The dates"), tbl(["Date", "What happens"], [(D.LETTER_DATE, "Letter date"), (D.LETTER["fy_end"], "Financial year end (the year under audit)"), (D.LETTER["sign_by"], "Sign and return"), (D.LETTER["interim"], "Interim fieldwork"),
                                                             (D.LETTER["year_end_work"], "Year-end fieldwork"), (D.LETTER["report"], "Audit report")])],
 deliverable="Three answers from Claude, one of them ticked against the letter.",
 fallback="If upload fails, open the letter and paste the Timetable section into the chat.",
 hint="Compare Claude's dates with the Timetable section of the letter.",
 stretch=["Ask Claude which paragraph each date came from, then check two of them."],
 stretch_prompts=[("Where each date came from", "For each date you listed, give the section heading it came from.")])

demo("t12", day=1, skill="1.2", sec=3, title="Same task, 18 answers", tool="Claude chat", files=[F_INV, F_LEDGER], kind="task", hands_on=True, minutes=12, solo="on your own, then in pairs",
 setup=["Start a new chat. Attach the invoice pack and the October purchase ledger.", "Write your own request: a table that checks each invoice against the ledger. You have 7 minutes.",
        "Compare your table with your neighbor's: columns, totals, and what each of you flagged.", "Be ready to show your table on the screen."],
 prompts=[],
 expected="Tables that differ: different columns and different totals. Many miss one of the two problems: SCC-0718 (ledger 1,284.500, invoice 1,248.500) or FSC-3390 (not in the October ledger).",
 say="Same files, same tool, 18 people. Count how many different tables we get.",
 point="One-off chat is not repeatable. A supervisor cannot review 18 shapes.",
 backup=[("h", "What the right check finds"), tbl(MATCH_TABLE[0], MATCH_TABLE[1:])],
 answer=[("h", "The two planted problems"), ("ul", [f"SCC-0718: the invoice says KWD {num(D.INV['SCC-0718'][4])}; the ledger says KWD {num(D.WRONG_LEDGER)}. Difference KWD {num(D.WRONG_DIFF)} (digits swapped).",
                                                    f"FSC-3390 (27 October 2026, KWD {num(D.INV['FSC-3390'][4])}) is not in the October ledger: a cut-off point to follow up. (Day 2 shows it in the November ledger.)"]),
         ("h", "The full match"), tbl(D.TEMPLATE_HEAD, MATCH_FULL),
         ("note", "Known trap: ledger line SCC-0702 (3 October, KWD 1,248.500) has the same amount as the SCC-0718 invoice. A table that matches by amount marks SCC-0718 Matched. Use it in the debrief: match by number first.")],
 deliverable="Your own reconciliation table, compared with a neighbor's.",
 fallback="If Claude is slow, pairs share one laptop. Show the backup table in the debrief.",
 hint="Check every row against both files: number, date and amount.",
 stretch=["Run the same request again in a new chat. Compare the two tables."])

demo("d10", day=1, skill="1.1", sec=3, title="One invoice, two requests", tool="Claude", files=[F_INV], kind="showcase",
 setup=["[T] Open claude.ai in two windows. Upload abdali-supplier-invoices-oct-2026.pdf to both.", "[T] Type the weak request in one window and the five-part request in the other. Ask about invoice BPK-4471 (page 1)."],
 prompts=[("Weak", "What's in this?"), ("Strong", joined(OPENER_PARTS) + " Use invoice BPK-4471 on page 1.")],
 expected=f"Weak: a readable paragraph about packaging that gives a rounded amount and no invoice number. Strong: one row: {D.OPENER_INV[1]}, {D.OPENER_INV[0]}, 12 October 2026, PO number Not found, KWD {num(D.OPENER_INV[4])}.",
 say="Same tool. Same invoice. The only thing that changed is the request.",
 point="The request decides the result. You still check it.",
 backup=[("h", "Weak request: typical result"), ("p", "“This is an invoice from Bayan Packaging for cartons and shrink film, dated in October, for about 2,100 dinars. It looks like a standard packaging purchase.”"),
         ("h", "Five-part request: typical result"), tbl(["Supplier", "Invoice no.", "Date", "PO no.", "Amount (KWD)"], [(D.OPENER_INV[1], D.OPENER_INV[0], "2026-10-12", "Not found", num(D.OPENER_INV[4]))])],
 fallback="If Claude is slow or the file will not load, read the expected results aloud and keep going.",
 hint="Which answer could go into a working paper today?")

demo("d13", day=1, skill="1.2", sec=3, title="Dana tags her task list", tool="Claude", files=[], kind="player",
 setup=["[T] Paste Dana's seven tasks into a new chat with the prompt below."],
 prompts=[("Tag my tasks", "Role: You help an audit associate plan her work. Task: Tag each task in my list with three tags: repeats weekly, clear rules, document in and document out. "
           "Format: A table with Yes or No for each tag, then my top 3 (tasks with three Yes). My tasks: 1. Match supplier invoices to the ledger. 2. Prepare lead schedules from the trial balance. "
           "3. Chase missing documents from clients. 4. Check new clients' KYC and acceptance documents against the checklist. 5. Draft management letter points. 6. Discuss findings with the client's CFO. 7. Update my time sheet.")],
 expected="A table with three Yes for invoice matching, lead schedules and chasing documents. The CFO discussion gets three No. The KYC check has clear rules but is not weekly: a later agent.",
 say="Three tags. A task that gets three Yes is a candidate agent.",
 point="Repeats, clear rules, document in and out.",
 backup=[("h", "Dana's tagged list"), tbl(["Task", "Weekly", "Clear rules", "Doc in, doc out"], [
     ("Match supplier invoices to the ledger", "Yes", "Yes", "Yes"), ("Prepare lead schedules from the trial balance", "Yes", "Yes", "Yes"),
     ("Chase missing documents from clients", "Yes", "Yes", "Yes"), ("Check new clients' KYC and acceptance documents", "No", "Yes", "Yes"), ("Draft management letter points", "No", "No", "Yes"),
     ("Discuss findings with the client's CFO", "No", "No", "No"), ("Update my time sheet", "Yes", "Yes", "No")])],
 fallback="Show the backup table.",
 hint="Count the Yes answers on each row.",
 player={"parts": [["Role", "You help an audit associate plan her work."], ["Task", "Tag each task with three tags: repeats weekly, clear rules, document in and document out."],
                   ["Format", "A table with Yes or No for each tag, then my top 3."]],
         "table": [["Dana's task", "Weekly", "Clear rules", "Doc in, out"], ["Match invoices to the ledger", "Yes", "Yes", "Yes"], ["Lead schedules from the TB", "Yes", "Yes", "Yes"],
                   ["Chase missing documents", "Yes", "Yes", "Yes"], ["Management letter points", "No", "No", "Yes"], ["Findings with the CFO", "No", "No", "No"]], "best": 0,
         "reco": ["<b>Top 3:</b> invoice matching, lead schedules, chasing documents.", "<b>Not an agent:</b> the CFO meeting. Judgment and trust stay with people.", "<b>Next:</b> do the same with your own week."],
         "control": "You decide the top 3. Claude only sorts your list."})

demo("t13", day=1, skill="1.3", sec=3, title="Your task inventory", tool="The Day 1 lab page", files=[], kind="task", hands_on=True, minutes=8, solo="on your own",
 setup=["Open the Day 1 lab page. List 10 tasks from your last week.", "Tag each one: repeats weekly, clear rules, document in and document out.",
        "Use the prompt card for your role (on the lab page). Pick the 3 tasks with three tags.", "Post your strongest task on the shared board, under your department."],
 prompts=[("Optional: ask Claude to tag your list", "Tag each task in my list with three tags: repeats weekly, clear rules, document in and document out. A table with Yes or No for each tag, then my top 3. My tasks: [paste your list, with no client or firm names].")],
 expected="10 tasks, tagged; a top 3; one task on the shared board under the right department.",
 say="Preparers: what do you rebuild on every engagement? Reviewers: what do you check every time? Coordinators: what do you chase every week, from requests to new-client KYC files?",
 point="The best first agent repeats, follows rules, and turns a document into a document.",
 backup=[("h", "Example: Dana's top 3"), ("ul", ["Match supplier invoices to the ledger", "Prepare lead schedules from the trial balance", "Chase missing documents from clients"])],
 answer=[("h", "What a good inventory has"), ("ul", ["Ten real tasks, written as verbs (match, prepare, chase).", "Three tags on each.", "A top 3 where all three tags are Yes.",
                                                     "No client names: describe the task, not the client."])],
 deliverable="10 tasks tagged, your top 3, and the strongest one on the shared board.",
 fallback="Anyone stuck starts from Dana's list on the slide and changes it to their own work.",
 hint="If a task needs a meeting or a judgment call, it is not your first agent.",
 stretch=["Write the minutes per week for each of your top 3."])

demo("d15", day=1, skill="1.3", sec=4, title="Dana scores her three candidates", tool="Claude", files=[], kind="player",
 setup=["[T] Paste the prompt below into a new chat."],
 prompts=[("Score my candidates", "Score these three tasks from 1 to 5 on four points. The points are: how often it happens, minutes each time, how clear the rules are, and whether it could run on a schedule. "
           "Add a total. Tasks: match supplier invoices to the ledger; prepare lead schedules from the trial balance; chase missing documents from clients.")],
 expected="Invoice matching scores highest (19 of 20), then chasing documents (16), then lead schedules (15).",
 say="Four questions. The total decides the first agent, not the most interesting task.",
 point="Often, long, clear rules, schedulable: pick the highest total.",
 backup=[("h", "Dana's scores"), tbl(["Task", "Often", "Time", "Clear rules", "Schedule", "Total"], [("Invoice matching", 5, 4, 5, 5, 19), ("Chase documents", 5, 3, 3, 5, 16), ("Lead schedules", 3, 4, 4, 4, 15)])],
 fallback="Show the backup table.",
 hint="Which task has the highest total?",
 player={"parts": [["Task", "Score each task from 1 to 5: how often, minutes each time, how clear the rules are, can it run on a schedule."], ["Format", "A table with a total for each task."]],
         "table": [["Task", "Often", "Time", "Rules", "Schedule", "Total"], ["Invoice matching", "5", "4", "5", "5", "19"], ["Chase documents", "5", "3", "3", "5", "16"], ["Lead schedules", "3", "4", "4", "4", "15"]], "best": 5,
         "reco": ["<b>Dana picks invoice matching:</b> 19 of 20.", "<b>Schedulable</b> matters: Day 2 runs it without her.", "<b>Your turn:</b> score your own three."],
         "control": "The score guides you. You and your supervisor decide."})

demo("t15", day=1, skill="1.4", sec=4, title="Write your Agent Card v1", tool="The Day 1 lab page", files=[], kind="task", hands_on=True, minutes=17, solo="on your own",
 setup=["Score your 3 candidates on the four points (4 min).", "Pick one and place it in a track: Extraction, Analysis, Workflow or Reporting (2 min).",
        "Write your Agent Card on the Day 1 lab page: Input, Instruction, Output. Leave When empty (7 min).", "Paste the card on the shared board for approval (4 min)."],
 prompts=[("Optional: ask Claude to challenge your card", "Here is my Agent Card, with no client or firm names: [paste it]. Ask me three questions that would make the Instruction box clearer. Do not write the card for me.")],
 expected="An Agent Card with a clear input file, an instruction with rules, and an output with named columns; placed in one of the four tracks.",
 say="Your card, your task. Build it on the track pack: no real files today.",
 point="A good card is one a new joiner could follow.",
 backup=[("h", "Dana's card"), tbl(["Box", "Dana's card"], CARD_INVOICE)],
 answer=[("h", "Approve a card when"), ("ul", ["Input names a file type and where it comes from.", "Instruction has at least two rules and says what to do when unsure.",
                                               "Output names the columns or headings.", "The task fits a track pack, or the person has a dummy pack."])],
 deliverable="An approved Agent Card v1 on the shared board.",
 fallback="Anyone without a task of their own takes the track pack's starting example.",
 hint="Read your Instruction box as if you were new. Would you know what to do?",
 stretch=["Write a second card for your runner-up task."])

demo("d14", day=1, skill="1.4", sec=4, title="From card to agent", tool="Claude Projects", files=[F_TEMPLATE], kind="player",
 setup=["[T] Show the invoice Agent Card. Build the Project live: + New Project, name it Mirqab invoice match.", "[T] Set project instructions: paste the five parts. Add mirqab-invoice-match-template.xlsx to the knowledge."],
 prompts=[("Project instructions", joined(INVOICE_AGENT))],
 expected="A Project named Mirqab invoice match with the five-part instructions and the template in its knowledge.",
 say="The card says what. The Project keeps it, for every chat inside it.",
 point="Write the card once. Keep it in a Project.",
 backup=[("h", "What the Project holds"), tbl(["Part of the Project", "What goes in", "Mirqab example"], [("Name", "A clear name", "Mirqab invoice match"), ("Instructions", "The card, written as five parts", "Role, steps, rules, format, when unsure"),
                                                                                                   ("Knowledge", "Templates, reference files, one example output", F_TEMPLATE), ("Each run", "This month's documents", f"{F_INV} · {F_LEDGER}")])],
 fallback="Show the backup table and build the Project after the slide.",
 hint="The instructions hold the rules. Knowledge holds the template. The invoices come with each run.",
 player={"parts": CARD_INVOICE,
         "table": [["Part of the Project", "What goes in", "Mirqab example"], ["Name", "A clear name", "Mirqab invoice match"], ["Instructions", "The card, as five parts", "Role, steps, rules, format, when unsure"],
                   ["Knowledge", "Template, an example", "the match template"], ["Each run", "This month's documents", "October invoices and ledger"]], "best": 2,
         "reco": ["<b>Input, Instruction, Output:</b> each box has a home in the Project.", "<b>When</b> stays empty until Day 2.", "<b>Knowledge, not input:</b> the invoices come with each run."],
         "control": "The Project keeps the method. You still check every flag."})

demo("t14", day=1, skill="1.5", sec=4, title="Build the invoice agent with me", tool="Claude Projects", files=[F_INV, F_LEDGER, F_TEMPLATE], kind="task", hands_on=True, minutes=19, solo="on your own, with the trainer",
 setup=["In claude.ai, open Projects and click + New Project. Name it Mirqab invoice match.", "Click Set project instructions. Paste the instructions below. Save.",
        "Add mirqab-invoice-match-template.xlsx to the project knowledge with +.", "Start a chat in the Project. Attach the October invoices and ledger. Type the run line."],
 prompts=[("Project instructions", joined(INVOICE_AGENT)), ("Run line (in a chat inside the Project)", "Match the attached October invoices to the attached October purchase ledger.")],
 expected="The same table for everyone: BPK-4471, WDS-20931 and SGT-11205 Matched; SCC-0718 Amount differs (36.000); FSC-3390 Not in ledger.",
 say="Same files as Task 1.2. This time we all use the same card.",
 point="One card, one shape, both problems found.",
 backup=[("h", "Typical result"), tbl(D.TEMPLATE_HEAD, MATCH_FULL)],
 answer=[("h", "The right table"), tbl(D.TEMPLATE_HEAD, MATCH_FULL), ("note", "Accept any wording in the Note column if it names the swapped digits and says FSC-3390 is not in the October ledger (check cut-off). BPK-4471 has no PO number: the PO column says Not found; accept Matched or Not found as its status."),
         ("note", "Trap: ledger line SCC-0702 has the same amount as the SCC-0718 invoice. If a table marks SCC-0718 Matched, it matched by amount, not by number.")],
 deliverable="A Project named Mirqab invoice match and a table that flags both problems.",
 fallback="Anyone behind copies the instructions from the prompt sheet and runs it with the trainer's next run.",
 hint="Check the Status column: at least two rows should not say Matched.",
 stretch=["Run the same request in a second chat inside the Project. Compare the two tables."])

demo("d16", day=1, skill="1.5", sec=5, title="From card to five-part instructions", tool="Claude Projects", files=[F_INV, F_LEDGER, F_TEMPLATE], kind="player",
 setup=["[T] Open the Mirqab invoice match Project. Show the instructions as five parts.", "[T] Run it. Compare three rows with the answers you checked by hand: BPK-4471, SCC-0718 and FSC-3390."],
 prompts=[("Five-part instructions", joined(INVOICE_AGENT))],
 expected="The full match table, with the two flags explained in the Note column.",
 say="Five parts. The fifth one, when unsure, is the one people forget.",
 point="Role, Steps, Rules, Output format, When unsure. Then test.",
 backup=[("h", "Typical result"), tbl(D.TEMPLATE_HEAD, MATCH_FULL)],
 fallback="Show the backup table.",
 hint="Find the row the agent marked Not in ledger. Why?",
 player={"parts": INVOICE_AGENT, "table": MATCH_TABLE, "best": 4,
         "reco": ["<b>Two flags:</b> SCC-0718 differs by KWD 36.000; FSC-3390 is not in October.", "<b>When unsure</b> made it flag, not guess."],
         "control": "Test on three cases you checked by hand before you trust it."})

demo("t16", day=1, skill="1.6", sec=5, title="Build v1 of your agent", tool="Claude Projects", files=[F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS], kind="task", hands_on=True, minutes=65, solo="on your own",
 setup=["Create a Project named after your task. Write the instructions in five parts, from the template below.",
        "Add your template or one example output to the knowledge.",
        "Check 3 items by hand first. Extraction: leases 1, 4, 6. Analysis: Trade receivables, Accrued expenses, Bank charges. Workflow: items 5, 7, 8. Reporting: the 3 engagements.",
        "Run the agent on your pack. Compare those 3 items with yours. Fix the instructions, not the answer."],
 prompts=[("Five-part template", FIVE_TEMPLATE), ("Test run", "Run on the attached file. Then list every row you are not sure about.")],
 expected="A Project per person whose result is right on the three items checked by hand.",
 say="Struggle first. A hint at 15 minutes, then the most common fixes at 30.",
 point="Fix the instructions, not the answer.",
 backup=[("h", "Starter instructions for each track")] + [x for t, p in STARTER.items() for x in (("p", f"<b>{t}</b>"), ("p", joined(p)))],
 answer=[("h", "What each track should find")] + [("ul", [f"Extraction: the rent-free period in lease 4 and the landlord's 60-day termination clause in lease 6 (the two unusual clauses). Lease 1's 3-year renewal option is also expected in Special terms. Accept a flag that lease 5 ends on 31 December 2026.",
                                                         f"Analysis: {', '.join(D.OVER)} over the threshold; {D.RECLASS[0]} and {D.RECLASS[1]} move together (ask about a reclassification); {D.PCT_ONLY} is over 10% but under KWD 5,000, so not flagged.",
                                                         f"Workflow: {D.PBC_COUNTS['Received']} received, {D.PBC_COUNTS['Partly received']} partly received (wrong period on item 5; nothing attached on item 7; item 13 has the loan agreements but not the bank confirmations), {D.PBC_COUNTS['Outstanding']} outstanding. Also accept Outstanding for items 5 and 7.",
                                                         f"Reporting: Khiran Logistics is {D.OVER_BUDGET[0][1]}% over budget; Jabriya's report is due 19 November."]),
         ("h", "The three items to check by hand"), tbl(["Track", "Item", "The right answer"], CHECK3)],
 deliverable="Your own Project, right on the three items you checked by hand.",
 fallback="Hint 3: the trainer opens the worked Project for your track on screen, or gives you its five parts.",
 hint="Hints in order: reread your Instruction box; use the five-part template; open the worked Project for your track.",
 stretch=["Add a second example output to the knowledge. Run again and check the same three items."])

demo("d17", day=1, skill="1.6", sec=6, title="Read from the folder", tool="Claude · Google Drive connector", files=[F_INV, F_LEDGER], kind="player",
 setup=["[T] Customize, then Connectors: show Google Drive, connected before Day 1 with the trainer's CODED training Google account.", f"[T] In the invoice Project, ask it to process the newest pack in {D.SANDBOX} / 01 Invoices / Inbox."],
 prompts=[("Run from the folder", f"Open the Google Drive folder {D.SANDBOX} / 01 Invoices / Inbox. Run the invoice match on the files there. List the files you read.")],
 expected="The same match table, plus the two file names it read from the Inbox.",
 say="No more dragging files. The agent reads where the files already are.",
 point="A connector is a key to one cabinet, not the whole archive.",
 backup=[("h", "Files read"), ("ul", [F_INV, F_LEDGER]), ("h", "Result"), tbl(D.TEMPLATE_HEAD, MATCH_FULL)],
 fallback="If the connector is slow, upload the two files and continue.",
 hint="Check the list of files it read: it should be exactly two.",
 player={"parts": [["Task", f"Open the Google Drive folder {D.SANDBOX} / 01 Invoices / Inbox. Run the invoice match on the files there."], ["Format", "Return the match table. Then list the files you read."]],
         "table": [["File read", "Type", "Used for"], [F_INV, "PDF", "Invoices"], [F_LEDGER, "Excel", "Ledger"]], "best": 0,
         "reco": ["<b>Input box filled:</b> the agent reads from the folder.", "<b>Sandbox only:</b> CODED's practice Drive, no client data.", "<b>Ask for the file list</b> so you know what it read."],
         "control": "Sign in with an account that opens only what the task needs."})

demo("t17", day=1, skill="1.7", sec=6, title="Run from the folder", tool="Claude · Google Drive connector", files=[F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["Customize, then Connectors: connect Google Drive. Sign in with your own CODED training Google account.", "Find your track folder in the sandbox Drive. Your files are in its Inbox.",
        "In your Project, run your agent on the folder. Ask it to list the files it read."],
 prompts=[("Run from your folder", f"Open the Google Drive folder {D.SANDBOX} / [your track folder] / Inbox. Run on the files there. List the files you read.")],
 expected="One run that reads from the track folder and lists the files it used.",
 say="Your Input box now points at a folder.",
 point="The agent reads where the files live.",
 backup=[("h", "The track folders"), ("ul", [f"{D.SANDBOX} / {f} / Inbox" for f in D.FOLDERS])],
 answer=[("h", "Check"), ("ul", ["The run lists the file names it read.", "The result matches the run from Lesson 4.", "The account used for the connector opens only the sandbox."])],
 deliverable="One run from your track folder, with the list of files read.",
 fallback="If Google sign-in fails, upload the files and continue. The trainer fixes the connector at the break.",
 hint="The folder path must match the Drive exactly.",
 stretch=["Ask the agent which files it did not read, and why."])

demo("d18", day=1, skill="1.7", sec=6, title="Same shape every run", tool="Claude · artifacts", files=[F_INV, F_LEDGER, F_TEMPLATE], kind="player",
 setup=["[T] Add the output rule below to the invoice Project.", "Run twice. Put the two artifacts side by side."],
 prompts=[("Output rule", "Return the result as an artifact: a table with exactly the template's columns, in that order. Put flagged rows first. End with one total line: invoices checked, matched, flagged.")],
 expected="Two runs with the same 9 columns, flagged rows first, and the same total line: 5 checked, 3 matched, 2 flagged. If BPK-4471 is marked Not found, accept 5 checked, 2 matched, 3 flagged.",
 say="If the shape changes every run, nobody can compare this week with last week.",
 point="A fixed shape is what makes a run reviewable.",
 backup=[("h", "Total line"), ("p", "Invoices checked: 5 · Matched: 3 · Flagged: 2"), ("note", "Also correct: 5 · 2 · 3, when BPK-4471 (no PO number) is marked Not found.")],
 fallback="Show the backup total line.",
 hint="Compare the columns and the total line of the two runs.",
 player={"parts": [["Output format", "Return an artifact: a table with exactly the template's columns, in order. Flagged rows first."], ["Total line", "End with: invoices checked, matched, flagged."]],
         "table": [["Check", "Run 1", "Run 2"], ["Columns", "9, in template order", "9, in template order"], ["Row order", "Flags first", "Flags first"], ["Total line", "5 · 3 · 2", "5 · 3 · 2"]], "best": 2,
         "reco": ["<b>Same shape twice.</b> The supervisor reviews the flags, not the layout.", "<b>An artifact</b> opens, edits and downloads like a file.", "<b>Next:</b> the same rule in your Project."],
         "control": "Same columns, same order, same total line, every run."})

demo("t18", day=1, skill="1.8", sec=6, title="Fixed-shape output", tool="Claude · artifacts", files=[F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=["Add an output rule to your Project: exact columns, order, a total line.", "Run it twice on your track pack, each time in a new chat in the Project.", "Compare the two results. Fix the rule until they match in shape."],
 prompts=[("Output rule", "Return the result as an artifact with exactly these columns, in this order: [your columns]. End with one total line."),
          ("Save it to Drive", "Save the result as an Excel file in [your track folder] / Outputs, named [client]-[task]-YYYY-MM-DD-HHMM.xlsx, with the date and time of the run.")],
 expected="Two artifacts with the same columns, order and total line.",
 say="Two runs, one shape.",
 point="Fix the shape in the instructions, not by hand.",
 backup=[("h", "A good output rule"), ("p", "Return the result as an artifact with exactly these columns, in this order. Flagged rows first. End with one total line.")],
 answer=[("h", "Check"), ("ul", ["Same columns and order on both runs.", "A total line on both.", "Nothing edited by hand."])],
 deliverable="One artifact or Excel file, in the same shape on two runs.",
 fallback="If artifacts do not open, ask for a markdown table and continue.",
 hint="Name the columns in the order you want them. Claude follows the order you write.",
 stretch=["Run it on the messy file for your track. Check that the shape still holds."])

demo("d19", day=1, skill="1.8", sec=7, title="From Project to skill", tool="Claude · skills", files=[F_TEMPLATE], kind="player",
 setup=["[T] File creation works on this account (the owner turned on code execution for the team).",
        "[T] mirqab-invoice-match was built and tested before Day 1; the 16:25 task uses it. Save this live copy as mirqab-invoice-match-live.",
        "[T] In the invoice Project, ask Claude to turn the instructions into a skill. Save it. Run it in a fresh chat outside the Project."],
 prompts=[("Make the skill", "Turn the instructions of this Project into a skill named mirqab-invoice-match-live. Keep every rule word for word. Include the template as a reference file. Describe when to use it: matching supplier invoices to a purchase ledger.")],
 expected="A skill named mirqab-invoice-match-live, saved under Customize, then Skills. In a fresh chat, the same table appears.",
 say="The Project is my desk. The skill is the firm's manual: it works anywhere, for anyone I share it with.",
 point="Package the method once. Use it anywhere.",
 backup=[("h", "Project or skill"), tbl(["", "Project", "Skill"], [("Lives in", "One Project", "Any chat, Cowork and scheduled tasks"), ("Shared with", "Project members", "Anyone you share it with"), ("Loads", "In every chat of the Project", "When the task matches")])],
 fallback="If the skill does not save, show the backup table and continue with the Project.",
 hint="In the fresh chat, look for the line that says Claude is using the skill.",
 player={"parts": [["Task", "Turn the instructions of this Project into a skill named mirqab-invoice-match-live."], ["Rules", "Keep every rule word for word. Include the template as a reference file."],
                   ["When to use", "Matching supplier invoices to a purchase ledger."]],
         "table": [["", "Project", "Skill"], ["Lives in", "One Project", "Any chat, Cowork, schedules"], ["Shared with", "Project members", "Anyone you share it with"], ["Loads", "Every chat in it", "When the task matches"]], "best": 2,
         "reco": ["<b>Same method, new home:</b> it travels.", "<b>Day 2 needs it:</b> a scheduled task calls the skill.", "<b>Share it</b> from its menu on a Team plan."],
         "control": "Test the skill in a fresh chat before you share it."})

demo("t19", day=1, skill="1.9", sec=7, title="Make your skill", tool="Claude · skills", files=[F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=["Code execution is on for the team: the owner turned it on. If your skill does not save, tell the trainer.", "In your Project, ask Claude to turn your instructions into a skill. Save it.",
        "Open a new chat outside the Project. Attach your pack and ask for the task in one line.", "Check that Claude uses your skill and returns the same shape.",
        "Use the Package row on the transfer slide or the cheat sheet. Add one line to your Agent Card: where this skill would live in ChatGPT, Copilot or Gemini."],
 prompts=[("Make the skill", "Turn the instructions and knowledge of this Project into a skill named [your-skill-name]. Keep every rule word for word. Describe when to use it in one line."),
          ("Test it in a new chat", "[One line that asks for your task], using the attached sample.")],
 expected="A saved skill; a fresh chat that uses it and returns the same shape as the Project; one transfer line on the card.",
 say="Your method, packaged. Tomorrow a scheduled task calls it.",
 point="If it works in a fresh chat, it will work on a schedule.",
 backup=[("h", "Where skills live"), ("ul", ["Customize, then Skills: your skills, on and off.", "Share: the menu next to the skill, then Share (Team plans)."])],
 answer=[("h", "Check"), ("ul", ["The skill name is short and clear.", "The rules are the same as in the Project.", "A fresh chat uses the skill and returns the fixed shape.",
                                   "The transfer line names the skill's home in another tool: a skill or custom GPT (ChatGPT), an agent (Copilot) or a Gem (Gemini)."])],
 deliverable="Your skill, saved and tested in a fresh chat, and one transfer line on your card.",
 fallback="If skills are off on an account, continue with the Project. The trainer turns them on at the break.",
 hint="A skill needs a clear name and one line on when to use it.",
 stretch=["Share the skill with a member of your team."])

demo("t110", day=1, skill="1.10", sec=7, title="The messy sample and the clock", tool="Claude · your skill", files=MESSY_FILES, kind="task", hands_on=True, minutes=14, solo="on your own",
 setup=["Download the messy file for your track. Run your skill on it. Workflow track: attach mirqab-pbc-request-list-abdali.xlsx with the messy email.", "Check: did the agent flag the problem, or guess? Each file hides a gap the agent must flag (the invoice file has two). No file has two values that conflict.",
        "Time the task: minutes by hand, minutes with the agent. Log both on the shared board."],
 prompts=[("Messy run", "Run on the attached file. List anything you could not read or are not sure about. Do not guess.")],
 expected="A flagged result for each track: " + "; ".join(f"{k}: {v[2]}" for k, v in D.MESSY.items()),
 say="A good agent flags what it cannot see. A bad one fills the gap.",
 point="Flag, do not guess.",
 backup=[("h", "What each messy file hides"), tbl(["Track file", "The problem", "The right behavior"], [(v[0], v[1], v[2]) for v in D.MESSY.values()])],
 answer=[("h", "What each messy file hides"), tbl(["Track file", "The problem", "The right behavior"], [(v[0], v[1], v[2]) for v in D.MESSY.values()])],
 deliverable="One flagged messy run and two numbers: minutes by hand and with the agent.",
 fallback="If the agent guesses, add the When unsure rule again and rerun.",
 hint="A missing field or a different unit.",
 stretch=["Add the fix as a rule to your skill and rerun."])

demo("d111", day=1, skill="1.9", sec=8, title="The agent that ran itself", tool="Claude · scheduled task", files=[], kind="player",
 setup=["[T] Before Day 1: build mirqab-invoice-match on this account and test it in a fresh chat. This task uses it.", f"[T] At 08:00, click Scheduled in the left sidebar, then New task. Name it Mirqab invoice match demo. Paste the prompt below. Frequency: daily at {D.SCHED_TIME}.",
        "[T] Approval mode: the mode that lets the run save and move Drive files without waiting.", "[T] Before 16:25, check that 01 Invoices / Inbox holds one copy of the October invoices and ledger.", "Show the Scheduled page, then open Outputs as the file arrives."],
 prompts=[("Scheduled task prompt", INVOICE_SCHED)],
 expected=f"At {D.SCHED_TIME}, the match file for 15 November appears in 01 Invoices / Outputs with the same table, and a run-log file appears in Log.",
 say="Nobody pressed Send. This is tomorrow.",
 point="Today it works when you open Claude. Tomorrow it runs without you.",
 backup=[("h", "The run-log file: runlog-2026-11-15-1625.txt"), ("p", "2026-11-15 16:25 · files read: 2 · flagged: 2 (SCC-0718, FSC-3390) · saved: abdali-invoice-match-2026-11-15-1625.xlsx")],
 fallback="If the run has not arrived, run the task on demand from the Scheduled page, or show the backup run-log file.",
 hint="Watch the Outputs folder.",
 player={"parts": [["When", f"Daily at {D.SCHED_TIME} (for today's demo)."], ["Task", f"Use the mirqab-invoice-match skill on the new files in {D.SANDBOX} / 01 Invoices / Inbox."],
                   ["Output", "Save the table in Outputs, named with the date and time. Save a run-log file in Log."]],
         "table": [["Run log", "Value"], ["Time", f"2026-11-15 {D.SCHED_TIME}"], ["Files read", "2"], ["Flagged", "SCC-0718, FSC-3390"], ["Saved", "abdali-invoice-match-2026-11-15-1625.xlsx"]], "best": 1,
         "reco": ["<b>The When box</b>, filled.", "<b>Same skill</b> as this afternoon.", "<b>Tomorrow:</b> your team's agent does this."],
         "control": "A person still reviews the output before anyone uses it."})

# ===================================================================== DAY 2
demo("d21", day=2, skill="2.1", sec=9, title="The invoice workflow card", tool="Workflow card", files=[], kind="player",
 setup=["[T] Show the invoice Agent Card from Day 1. Fill the workflow card box by box."],
 prompts=[("Check our card", "Here is our workflow card: [paste it]. Ask us three questions about what could go wrong when it runs without us.")],
 expected="Every box filled: a daily morning time, the invoice Inbox folder, the invoice-match skill by name, an Excel file named with the date and time, a run-log file, and Faisal as the reviewer.",
 say="Five boxes. The last one, who reviews, is the one auditors care about most.",
 point="When, Input, Skill, Output, Who reviews.",
 backup=[("h", "The invoice workflow card"), tbl(["Box", "Invoice workflow"], [("When", "Daily at 08:00"), ("Input", "New files in 01 Invoices / Inbox"), ("Skill", "mirqab-invoice-match"),
                                                                               ("Output", "abdali-invoice-match-YYYY-MM-DD-HHMM.xlsx in Outputs, plus a run-log file in Log"), ("Who reviews", "Faisal, the supervisor, before anyone uses it")])],
 fallback="Show the backup card.",
 hint="Who reviews is a name, not a team.",
 player={"parts": [["When", "Daily at 08:00."], ["Input", "New files in 01 Invoices / Inbox."], ["Skill", "mirqab-invoice-match."], ["Output", "A named file in Outputs and a run-log file in Log."], ["Who reviews", "Faisal, before anyone uses it."]],
         "table": [["Box", "Invoice workflow", "Your team"], ["When", "Daily 08:00", "?"], ["Input", "01 Invoices / Inbox", "?"], ["Skill", "mirqab-invoice-match", "?"], ["Output", "File + run log", "?"], ["Who reviews", "Faisal", "?"]], "best": 1,
         "reco": ["<b>Trigger:</b> a time, not a person.", "<b>Review:</b> a named person.", "<b>Your turn:</b> the same card for your team's agent."],
         "control": "No workflow runs without a named reviewer."})

demo("t21", day=2, skill="2.1", sec=9, title="Your team's workflow card", tool="The Day 2 lab page", files=[], kind="task", hands_on=True, minutes=20, solo="in your team",
 setup=["Agree on your team's agent: one Agent Card from Day 1, by a show of hands.", "Fill the workflow card on the Day 2 lab page: When, Input, Skill, Output, Who reviews.", "Show it to the trainer."],
 prompts=[("Check our card", "Here is our workflow card: [paste it]. Ask us three questions about what could go wrong when it runs without us.")],
 expected="One card per team with a time, a folder, a skill, a named output and a named reviewer.",
 say="Fill all five boxes. A blank box is a risk.",
 point="A workflow is a card with a When.",
 backup=[("h", "Example card"), tbl(["Box", "Invoice workflow"], [("When", "Daily at 08:00"), ("Input", "01 Invoices / Inbox"), ("Skill", "mirqab-invoice-match"), ("Output", "A named file and a run-log file"), ("Who reviews", "Faisal")])],
 answer=[("h", "A complete card has"), ("ul", ["A time or a day for When.", "One folder for Input.", "The skill name from Day 1.", "A file name pattern and a run-log file.", "A named reviewer."])],
 deliverable="Your team's workflow card, shown to the trainer.",
 fallback="A team whose agent is not ready takes the invoice workflow: one member turns the Task 1.5 Project into a skill first.",
 hint="Who reviews is one person's name.",
 stretch=["Write the one-line format of your run log."])

demo("d22", day=2, skill="2.2", sec=10, title="Schedule the invoice workflow", tool="Claude · scheduled tasks", files=[], kind="player",
 setup=["[T] Click Scheduled in the left sidebar, then New task, then Set up manually. If the form has no time field for Daily, use Create with Claude and say the time.", "[T] Check that 01 Invoices / Inbox holds the October invoices and ledger (the pre-flight copied them back).", "[T] Name, prompt, approval mode, frequency daily at 08:00. Save. Run it once on demand."],
 prompts=[("Scheduled task prompt", INVOICE_SCHED)],
 expected="A scheduled task on the Scheduled page, daily at 08:00. A test run writes a file to Outputs and moves the two files to Processed.",
 say="Name, prompt, frequency. The prompt calls the skill you made yesterday.",
 point="A scheduled task is a calendar reminder that also does the work.",
 backup=[("h", "The fields"), tbl(["Field", "Value"], [("Name", "Mirqab invoice match, daily"), ("Prompt", "Calls mirqab-invoice-match; reads Inbox; saves to Outputs; moves to Processed; saves a run-log file in Log"), ("Approval mode", "The mode that lets the run save and move Drive files without waiting"), ("Frequency", "Daily at 08:00 (Kuwait works Sunday to Thursday; Friday and Saturday runs log No new files)")])],
 fallback="If Cowork is not on, show the backup fields and run the prompt by hand in a chat.",
 hint="Run it once on demand, then open Outputs.",
 player={"parts": [["Name", "Mirqab invoice match, daily."], ["Prompt", "Use the mirqab-invoice-match skill on the new files in 01 Invoices / Inbox. Save to Outputs. Move files to Processed. Save a run-log file in Log."], ["Frequency", "Daily at 08:00."]],
         "table": [["Step", "Where"], ["Scheduled", "Left sidebar"], ["New task", "Upper right"], ["Set up manually", "Name, prompt, approval, frequency"], ["On demand", "Test it once"]], "best": 1,
         "reco": ["<b>Runs remotely:</b> with Drive, the laptop can be closed.", "<b>Uses</b> your connectors and skills.", "<b>Each run</b> is its own session."],
         "control": "Run it once now and check the output before you trust the schedule."})

demo("t22", day=2, skill="2.2", sec=10, title="Schedule your workflow", tool="Claude · scheduled tasks", files=[], kind="task", hands_on=True, minutes=30, solo="in your team",
 setup=["Work on the laptop of the person who made your team's skill. That person also makes the Task 2.4 edits.", "Copy your pack from the Packs folder into [your team folder] / Inbox. Then click Scheduled in the left sidebar, then New task, then Set up manually.", "Name it. Paste the prompt below and fill the brackets from your card.",
        "Approval mode: choose the mode that lets the run save and move files without waiting for you.", "Frequency: daily at 08:00. Save.", "Run it once on demand. Compare the output with your Day 1 result."],
 prompts=[("Scheduled task prompt", SCHED_PROMPT)],
 expected="A scheduled task per team; one run that writes a named file to Outputs, moves the input files to Processed and saves a run-log file in Log.",
 say="Struggle first. A hint at 10 minutes, then the three most common fixes at 18.",
 point="If the test run works, the schedule will work.",
 backup=[("h", "The invoice version"), ("p", INVOICE_SCHED)],
 answer=[("h", "Check"), ("ul", ["The task shows on the Scheduled page with the right time.", "The test run wrote a file with the right name to Outputs.", "The input files moved to Processed.", "A new run-log file is in Log."])],
 deliverable="A scheduled task, run once, with its output checked against Day 1.",
 fallback="If the form has no time field for Daily, use Create with Claude and say the time. If Cowork is not available on an account, run the same prompt in a chat and schedule it on the trainer's account.",
 hint="Most failures are a folder name that does not match the Drive exactly.",
 stretch=["Add your team name to the output file name. Copy the pack from Packs into the Inbox again, run once more and check the new name."])

demo("d23", day=2, skill="2.3", sec=11, title="New files, then no files", tool="Claude · scheduled tasks", files=[F_INV2, F_LEDGER2], kind="player",
 setup=["[T] Drop batch 2 into 01 Invoices / Inbox. Run the task on demand.", "[T] Run again with the Inbox empty."],
 prompts=[("The empty-folder line (already in the prompt)", "If the Inbox has no new files, write No new files in the run log and stop. Do not process old files.")],
 expected=f"Run 1: {', '.join(D.B2_MATCHED)} matched; {D.B2_FLAG} flagged (USD, not converted). Run 2: the run log says No new files. Then open the November ledger yourself: FSC-3390 is posted on 3 November.",
 say="New files in, a file out. No files in, one honest line.",
 point="An automation that breaks on an empty folder is not an automation.",
 backup=[("h", "Two runs"), tbl(["Run", "Inbox", "Result"], [("1", "Batch 2: 3 invoices and the ledger", f"2 matched; {D.B2_FLAG} flagged (USD)"), ("2", "Empty", "No new files")]),
         ("note", "The agent checks the invoices in the pack, so it does not report FSC-3390. The trainer opens the November ledger: FSC-3390 is posted on 3 November, which confirms the Day 1 cut-off point.")],
 fallback="Show the backup table.",
 hint="Which invoice is not in KWD?",
 player={"parts": [["Input", "Process the new files in the Inbox, then move them to Processed."], ["Output", "Save a named file in Outputs."], ["Empty folder", "If there are no new files, write No new files in the run log and stop."]],
         "table": [["Run", "Inbox", "Result"], ["1", "Batch 2", f"2 matched · {D.B2_FLAG} flagged"], ["2", "Empty", "No new files"]], "best": 2,
         "reco": [f"<b>{D.B2_FLAG}</b> is in USD: flagged, never converted.", "<b>You check the cut-off:</b> FSC-3390 is in the November ledger, not in this pack.", "<b>Empty folder:</b> one line, then stop."],
         "control": "Read the run log every morning, even when it says No new files."})

demo("t23", day=2, skill="2.3", sec=11, title="Batch 2 and the empty folder", tool="Claude · scheduled tasks", files=BATCH2_FILES, kind="task", hands_on=True, minutes=25, solo="in your team",
 setup=["Check that the empty-folder line is in your scheduled task's prompt.",
        "Workflow teams: the skill owner adds mirqab-pbc-request-list-abdali.xlsx to the skill as a reference file, and you add the tracker line below to the prompt. Analysis teams: add the monthly line below.",
        "Copy the batch-2 file for your track from Packs into your team's Inbox. Run the task on demand. Check the output and the run log.", "Run again with the Inbox empty. Check the run log."],
 prompts=[("The empty-folder line (check it is in your prompt)", "If the Inbox has no new files, write No new files in the run log and stop. Do not process old files."),
          ("Workflow teams: the tracker line", "If the Inbox has new files, first open the newest tracker in [your team folder] / Outputs and update it. If there is none, start from the request list in the skill."),
          ("Analysis teams: the monthly line", "For monthly management accounts, compare the two months with the same two limits.")],
 expected=f"Two run-log files per team: one for the run on batch 2 (invoice teams flag {D.B2_FLAG}) and one that says No new files.",
 say="Two runs: new files, then none.",
 point="New files in, a file out. No files, one line.",
 backup=[("h", "Batch 2 by track"), tbl(["Track", "File", "What the run should show"], [
     ("Invoices", f"{F_INV2} · {F_LEDGER2}", f"{', '.join(D.B2_MATCHED)} matched; {D.B2_FLAG} flagged (USD)"), ("Extraction", F_LEASE2, "Lease 8: the 5% rent rise from year 2"),
     ("Analysis", F_MGMT, f"{D.MGMT_FLAG}: up from KWD 3,900 to KWD 9,800, over both limits"), ("Workflow", F_EMAILS2, "Items 5, 7 and 14 now received; item 15 promised by 30 November; item 12 'one more week', no date: flag it"),
     ("Reporting", F_STATUS2, "Jabriya closed; Khiran still over budget (24%)")]),
         ("note", "Workflow teams: the Task 2.2 run moved the request list to Processed. The skill keeps the request list as a reference file, and the run reads the latest tracker in Outputs, so batch 2 (emails only) can update it.")],
 answer=[("h", "Batch 2 by track"), tbl(["Track", "What the run should show"], [("Invoices", f"{', '.join(D.B2_MATCHED)} matched; {D.B2_FLAG} flagged (USD, ledger shows KWD 966.000: do not accept the rate)"),
     ("Extraction", "Lease 8, Mahboula, KWD 1,450.000 a month; special term: rent rises by 5% from the second year"), ("Analysis", f"{D.MGMT_FLAG} +KWD 5,900 (+151%)"),
     ("Workflow", "5, 7, 14 received; 15 outstanding, promised by 30 November; 12 outstanding, 'one more week' with no date: flag it (accept 23 November if the team works out the date). Full tracker: 10 received (1 to 7, 9, 10, 14), 1 partly received (13, bank confirmations), 4 outstanding (8, 11, 12, 15): 67% received"), ("Reporting", "Khiran 471 of 380 hours (24% over); Abdali 291 of 420; Jabriya closed")]),
         ("note", "Empty folder: the run log must say No new files, and no file is written to Outputs.")],
 deliverable="One run on batch 2 and one empty-folder run, each with its own run-log file.",
 fallback="If the run hangs, check the folder name, then run it on demand again.",
 hint="The run log after each run.",
 stretch=["Copy the batch-2 file into the Inbox again. Make the first line of the output a count of files read. Run on demand and check it against the run log."])

demo("d24", day=2, skill="2.4", sec=11, title="The n8n flow", tool="n8n with Claude", files=[], kind="player",
 setup=["[T] Built and tested before the workshop. Open the n8n flow on the presenting laptop.", "[T] Send one test email to the requests inbox. Watch the nodes run."],
 prompts=[("The Claude step in the flow", "Read this client email. Return three fields: request number, status (Received, Partly received or Outstanding), follow-up needed (yes or no).")],
 expected="The email arrives, the Claude node returns the three fields, and a new row appears in the request tracker sheet.",
 say="Same idea, different trigger: an event, not a time.",
 point="n8n is the next step when the trigger is an event or the systems belong to the company.",
 backup=[("h", "Claude scheduled task or n8n"), tbl(["", "Claude scheduled task", "n8n"], [("Starts", "At a time", "On an event: an email, a form, a file"), ("You build it", "By describing the task", "By connecting blocks (nodes)"),
                                                                                        ("Best for", "Your own weekly work", "Company systems, many steps, many people"), ("Set up by", "You", "Usually IT or an automation owner")])],
 fallback="Step through the flow on the slide, then show the comparison table.",
 hint="What starts this flow?",
 player={"parts": [["Trigger", "A new email arrives in the requests inbox."], ["Claude step", "Return: request number, status, follow-up needed."], ["Action", "Add one row to the request tracker sheet."]],
         "table": [["", "Claude scheduled task", "n8n"], ["Starts", "At a time", "On an event"], ["Built by", "Describing", "Connecting nodes"], ["Best for", "Your weekly work", "Company systems"]], "best": 2,
         "reco": ["<b>Event trigger:</b> it runs when the email lands.", "<b>Claude</b> is one step inside the flow.", "<b>For RSM:</b> a conversation with IT, after this week."],
         "control": "Same rule: a person reviews before anything goes to a client."})

demo("d25", day=2, skill="2.5", sec=12, title="Flag for supervisor review", tool="Claude · skills", files=[F_RULES, F_M_INV], kind="player",
 setup=["[T] Add the three Assurance rules below to the mirqab-invoice-match skill, word for word. Then add the review line.",
        f"[T] Check that 01 Invoices / Inbox holds batch 2 ({F_INV2}, {F_LEDGER2}) and {F_M_INV} (the pre-flight copied them from Packs).", "Run the task on demand. Open the output and the run log."],
 prompts=[("Department rules", "Add these rules to the skill, word for word: " + " ".join(D.RULES[0][1])),
          ("The review line", "Put items for the supervisor in a section called For supervisor review. Mark the file DRAFT and end it with: Reviewed by: ____.")],
 expected=f"{' and '.join(D.B2_MATCHED)} Matched. {D.B2_FLAG} and the messy invoice flagged for currency, never converted (the messy invoice also has no number). For supervisor review: empty, because no KWD difference is over KWD {num(D.REVIEW_LIMIT)}; accept {D.B2_FLAG} there too if it is not converted. DRAFT in the title and a Reviewed by line.",
 say="The rules are your department's, not Claude's. Write them down and the agent follows them.",
 point="Drafts only. A named person signs off.",
 backup=[("h", "Routing"), tbl(["Item", "Difference or issue", "Route"], [(D.B2_MATCHED[0], "None", "Matched"), (D.B2_MATCHED[1], "None", "Matched"), (D.B2_FLAG, "USD", "Flag: another currency, never converted"), ("Messy invoice", "USD, no number", "Flag: another currency, no invoice number")])],
 fallback="Show the backup routing table.",
 hint="Which items go to the supervisor?",
 player={"parts": [["Rule 1", D.RULES[0][1][0]], ["Rule 2", D.RULES[0][1][1]], ["Rule 3", D.RULES[0][1][2]], ["Review line", "A section For supervisor review. Mark DRAFT. End with: Reviewed by."]],
         "table": [["Item", "Issue", "Route"], [", ".join(D.B2_MATCHED), "None", "Matched"], [D.B2_FLAG, "USD", "Flag: currency"], ["Messy invoice", "USD, no number", "Flag: currency"]], "best": 2,
         "reco": ["<b>Supervisor section:</b> empty. No KWD difference is over KWD 100.", "<b>Department rules</b> live in the skill, word for word.", "<b>Reviewed by</b> closes every file."],
         "control": "The agent routes. The supervisor decides."})

demo("t25", day=2, skill="2.4", sec=12, title="Your department's rules", tool="Claude · skills", files=[F_RULES], kind="task", hands_on=True, minutes=30, solo="in your team",
 setup=["Open mirqab-review-rules.docx. Pick two rules for your department.", "The skill owner adds them to the skill word for word, with a review step and a DRAFT mark.",
        "Copy the Day 1 messy file for your track from Packs into your team's Inbox. Run the task on demand.", "Check the output and the new run-log file in Log."],
 prompts=[("Add the rules", "Add these rules to our skill, word for word: [two rules from mirqab-review-rules.docx]. Mark every output DRAFT and end it with: Reviewed by: ____.")],
 expected="The skill has two department rules, the DRAFT mark and a Reviewed by line; the messy sample is flagged and routed.",
 say="Your department's rules, word for word.",
 point="The agent routes. A person decides.",
 backup=[("h", "The rules file")] + [x for dpt, rs in D.RULES for x in (("p", f"<b>{dpt}</b>"), ("ul", rs))],
 answer=[("h", "Check"), ("ul", ["Two rules from the file, word for word.", "DRAFT on the output, and a Reviewed by line.", "The messy sample is flagged, not guessed.", "A new run-log file in Log for the rerun."])],
 deliverable="Two rules and a review step in your skill, tested on the messy sample.",
 fallback="A team short of time takes the All departments rules.",
 hint="Copy the rules exactly. A paraphrase is a new rule.",
 stretch=["Add one rule from a second department to the skill. Copy the messy file into the Inbox again, run on demand and check that the output follows the rule."])

demo("d26", day=2, skill="2.6", sec=13, title="A two-minute demo", tool="Claude", files=[], kind="player",
 setup=["[T] Show the five beats with the invoice workflow. Keep it to two minutes."],
 prompts=[("Draft our demo plan", "Draft a 5-minute demo plan for our workflow: the problem, the card, a live run, the impact, the next task. Use only facts from our run log and card.")],
 expected=f"A five-beat plan with one live run and one impact number (the invoice workflow saves about {D.impact(**D.INVOICE_IMPACT) // 60} hours a month).",
 say="Problem, card, live run, impact, next. In that order.",
 point="Show the run, then the number.",
 backup=[("h", "The invoice demo"), tbl(["Beat", "Seconds", "Invoice example"], [("Problem", 20, "45 minutes each time, 22 times a month"), ("Card", 20, "The workflow card"), ("Live run", 50, "A run on demand on batch 2"),
                                                                             ("Impact", 20, f"(45 − 6) × 22 = {D.impact(**D.INVOICE_IMPACT)} minutes, about {D.impact(**D.INVOICE_IMPACT) // 60} hours"), ("Next", 10, "The November cut-off check")])],
 fallback="Show the backup plan.",
 hint="Where does the live run go?",
 player={"parts": [["Problem", "What it costs today."], ["Card", "The workflow card."], ["Live run", "A run on demand, on screen."], ["Impact", "Minutes saved a month."], ["Next", "What we automate next."]],
         "table": [["Beat", "Seconds", "Invoice example"], ["Problem", "20", "45 min × 22 a month"], ["Card", "20", "The workflow card"], ["Live run", "50", "Batch 2"], ["Impact", "20", f"about {D.impact(**D.INVOICE_IMPACT) // 60} h a month"], ["Next", "10", "Cut-off check"]], "best": 2,
         "reco": ["<b>A live run</b> is stronger than slides.", "<b>One number:</b> minutes saved a month.", "<b>Next:</b> one task, not ten."],
         "control": "Every number in the demo comes from your run log."})

demo("t26", day=2, skill="2.5", sec=13, title="Clean runs, a failed run and the script", tool="Claude · scheduled tasks", files=[F_LOCKED], kind="task", hands_on=True, minutes=70, solo="in your team",
 setup=["Copy your track pack into the Inbox and run on demand, three times. Workflow teams: move the trackers in Outputs to Processed before each run (20 min).",
        f"Failed-run test: the skill owner adds the fallback line to the prompt. Copy {F_LOCKED} from Packs into the Inbox, run on demand and read the run log. Then delete it from the Inbox (12 min).",
        "Work out the impact: minutes by hand minus minutes with the agent, times runs a month (6 min).",
        "Write the 5-minute demo plan with the Demo 2.6 prompt. Say who acts when a run fails (12 min).", "Rehearse twice, with a timer. Before Demo Day, copy a pack into the Inbox for the live run (20 min)."],
 prompts=[("The fallback line (add it to your prompt)", FALLBACK_LINE),
          ("Impact", "From our run log, count the runs and the items flagged. Then calculate: ([minutes by hand] minus [minutes with the agent]) times [runs a month]. Take the minutes from our Clock tab.")],
 expected=f"Three clean runs and one failed-run test in the run log (Could not read: {F_LOCKED}, nothing guessed, the file left in the Inbox), one impact number and a timed 5-minute plan per team.",
 say="Three clean runs, one failed run, one number, five minutes.",
 point="Test the failure before Demo Day. A workflow you can trust says when it fails.",
 backup=[("h", "The failed-run test"), tbl(["Check", "A good run", "A bad run"], [("Run log", f"Could not read: {F_LOCKED}", "Silent, or says the run was fine"),
                                                                           ("Output", "No row for the locked file", "A row with made-up values"), ("The file", "Still in the Inbox", "Moved to Processed as if it was read")]),
         ("h", "The rubric (50 points)"), tbl(["Criterion", "Points", "What earns full marks"], RUBRIC_FULL)],
 answer=[("h", "The failed-run test"), ("ul", [f"The run log names {F_LOCKED} as Could not read. Nothing is guessed, and the file stays in the Inbox.",
                                              "If the log is silent or a row has values, the fallback line is missing from the prompt: add it and run on demand again.",
                                              "The fallback for a real file: the named reviewer checks it by hand, and the team asks for a readable copy."]),
         ("h", "Score sheet guide (50 points)"), tbl(["Criterion", "10", "5", "0"], RUBRIC_SCORE),
         ("note", "If the locked file opened and the trainer showed the Drive fallback instead, a team with three clean runs and the No new files run keeps full marks for Test evidence.")],
 deliverable="A Log folder with three clean runs and the failed-run test, and a rehearsed 5-minute demo with its impact number.",
 fallback=f"If {F_LOCKED} does not fail, pause the Google Drive connector on the trainer account, run the invoice task on demand, show that no run log is written, then reconnect. If a live run fails in rehearsal, show the latest output file and the run log instead.",
 hint="Every number on your demo comes from your run log or the Clock tab.",
 stretch=["List the next two tasks your team would automate."])

# ===================================================================== Demo 1.1: one invoice, two requests (Day 1, Lesson 2)
SHOWCASE = {
 "eyebrow": "Demo 1.1 · one invoice", "title": "Same tool. Same invoice. <span class=\"hl\">Two requests.</span>", "tool": "Claude", "file": F_INV,
 "weak": "What's in this?",
 "weak_answer": ["This is an invoice from Bayan Packaging for cartons and shrink film.", "It is dated in October and is for about 2,100 dinars.", "It looks like a standard packaging purchase."],
 "weak_flags": ["No invoice number", "Amount rounded", "PO not mentioned"],
 "parts": OPENER_PARTS,
 "table": [["Field", "Weak answer", "Five-part answer"], ["Invoice no.", "Missing", D.OPENER_INV[0]], ["Amount", "About 2,100", f"KWD {num(D.OPENER_INV[4])}"], ["PO no.", "Not mentioned", "Not found (flagged)"]],
 "strong_answer": [f"<b>{D.OPENER_INV[1]}</b> · {D.OPENER_INV[0]} · 2026-10-12", f"<b>Amount:</b> KWD {num(D.OPENER_INV[4])} · <b>PO no.:</b> Not found"],
 "strong_flags": ["Exact amount", "Flags the gap", "Ready for a working paper"],
 "score": [["Exact figures?", "No", "Yes"], ["Says what is missing?", "No", "Yes"], ["Ready to use?", "Ask again", "After a tick"]],
 "punch": "The request decides the result.", "punch_sub": "Same tool, same invoice. Only the instruction changed.",
}
AI_DEMOS = [k for k, v in DEMOS.items() if v.get("kind") in ("player", "showcase")]

# ===================================================================== Day 1 task steps, written so nobody wonders "where do I find this?" (Aya, 15 Nov)
# Places, always named the same way: the Day 1 lab page (workshop site → Day 1 → Open the lab), the prompt sheet (Day 1 page → Prompts),
# Claude (claude.ai, the workshop account). There is no shared board: cards go to the trainer, numbers go in the lab page.
AGENT_CARD_TEMPLATE = ("Task: [what the agent does, in one line]\n"
                       "Track: [Extraction, Analysis, Workflow or Reporting]\n"
                       "Input: [the files it reads, and where they are]\n"
                       "Instruction: [the rules it follows, as clear steps]\n"
                       "Output: [what it hands back: the columns, in order]\n"
                       "When: [leave empty until Day 2]")
DEMOS["t15"]["prompts"].insert(0, ("Agent Card template", AGENT_CARD_TEMPLATE))
_STEPS = {
 "t11": ["Download abdali-engagement-letter-2026.docx from step 1 of the Day 1 lab page (workshop site → Day 1 → Open the lab).",
         "Go to claude.ai and sign in with the workshop account. Click New chat.",
         "Click + in the message box and attach the letter.",
         "Open the prompt sheet (Day 1 page → Prompts), Task 1.1. Copy question 1, paste it in Claude, press Enter. Then do the same for questions 2 and 3.",
         "Open the letter yourself and check one of Claude's answers against it."],
 "t12": ["Download the invoice pack (PDF) and the October ledger (Excel) from step 2 of the Day 1 lab page.",
         "In Claude, click New chat. Click + and attach both files.",
         "Write your own request, in your own words: a table that checks each invoice against the ledger. There is no prompt to copy. You have 7 minutes.",
         "Compare your table with your neighbor's: the columns, the totals and what each of you flagged.",
         "Keep your table open. The trainer may show it on the screen."],
 "t13": ["Open step 3 of the Day 1 lab page. In its notes box, list 10 tasks you did last week, one per line.",
         "Tag each task Yes or No three times: it repeats every week, the rules are clear, a document goes in and a document comes out.",
         "Not sure what to list? Read the questions for your role in step 3. Then pick your top 3: the tasks with three Yes.",
         "Be ready to say your strongest task aloud. The trainer types each one on the screen."],
 "t15": ["In step 4 of the Day 1 lab page, score your top 3 tasks from 1 to 5: how often, minutes each time, clear rules, can run on a schedule (4 min).",
         "Pick the highest total and choose its track: Extraction, Analysis, Workflow or Reporting (2 min).",
         "Copy the Agent Card template from the prompt sheet, Task 1.4. Paste it in the box in step 4 and fill it in. Leave When empty (7 min).",
         "Raise your hand. The trainer approves your card at your seat (4 min)."],
 "t14": ["Download the three files from step 5 of the Day 1 lab page. In Claude, click Projects, then + New Project. Name it Mirqab invoice match.",
         "Click Set project instructions. Paste Project instructions from the prompt sheet, Task 1.5. Save.",
         "In the Project's knowledge, click + and upload mirqab-invoice-match-template.xlsx.",
         "Start a chat in the Project, attach the pack and the ledger, and send the Run line."],
 "t16": ["Download your track's file from step 7 of the Day 1 lab page. It says which file is yours.",
         "In Claude, click Projects, then + New Project, named after your task. Click Set project instructions, paste the Five-part template (prompt sheet, Task 1.6), fill it in from your card, and save.",
         "Check 3 items by hand first. Extraction: leases 1, 4, 6. Analysis: Trade receivables, Accrued expenses, Bank charges. Workflow: items 5, 7, 8. Reporting: the 3 engagements.",
         "Start a chat in the Project, attach your file and send the Test run line. Compare your 3 items; fix the instructions, not the answer."],
 "t17": ["In Claude, open Customize, then Connectors. Connect Google Drive and sign in with your CODED training Google account (sent to you before today), not your own.",
         "In a new browser tab, open Google Drive with the same account. Open Mirqab sandbox, then your track folder: 02 Leases, 03 Trial balance, 04 Requests or 05 Status. Your files are in Inbox.",
         "In Claude, open your Project and start a new chat. Copy Run from your folder from the prompt sheet, Task 1.7. Put your folder name in the brackets and send it.",
         "Check that the agent lists the files it read from the Inbox."],
 "t18": ["Copy the Output rule from the prompt sheet, Task 1.8. Put your columns in the brackets, in the order you want them.",
         "Open your Project, open its instructions, and paste the rule at the end, under Output format. Save.",
         "Start a new chat in the Project and run your agent on your track files. Then start a second new chat and run it again.",
         "Compare the two results: the same columns, the same order, the same total line? If not, fix the rule and run again."],
 "t19": ["Code execution is on for the team: the owner turned it on. If your skill does not save, tell the trainer.",
         "In a chat inside your Project, copy Make the skill from the prompt sheet, Task 1.9. Put your skill's name in the brackets and send it. Save the skill when Claude offers.",
         "Check that it is saved: open Customize, then Skills, and find your skill's name.",
         "Click New chat, outside the Project. Attach your track file. Copy Test it in a new chat from the prompt sheet, fill in the brackets, and send it. Claude should use your skill and return the same shape.",
         "Open the cheat sheet (Day 1 page → Cheat sheet), find the Package row. Add one line to your Agent Card: where this skill would live in ChatGPT, Copilot or Gemini."],
 "t110": ["Download the messy file for your track from step 11 of the Day 1 lab page. Workflow track: also attach mirqab-pbc-request-list-abdali.xlsx.",
          "Click New chat. Attach the messy file. Copy Messy run from the prompt sheet, Task 1.10, and send it.",
          "Check: did the agent flag the problem, or guess? Each file hides a gap the agent must flag (the invoice file has two). No file has two values that conflict.",
          "Time the task: minutes by hand, minutes with the agent. Write both numbers in the box in step 11 of the lab page."],
}
for _k, _v in _STEPS.items():
    DEMOS[_k]["setup"] = [x for x in DEMOS[_k]["setup"] if x.startswith("[T]")] + _v

DEMOS["t13"]["expected"] = "10 tasks, tagged; a top 3; the strongest task said aloud for the room review."
DEMOS["t13"]["deliverable"] = "10 tasks tagged, your top 3, and your strongest task ready to say aloud."
DEMOS["t15"]["deliverable"] = "An Agent Card v1, approved by the trainer at your seat."
DEMOS["t15"]["prompts"] = [p for p in DEMOS["t15"]["prompts"] if not str(p[0]).startswith("Optional")]

# ===================================================================== a second round for each build block: two Projects, two artifacts, two skills (Aya, 15 Nov)
TRACK_FILES = [F_LEASES, F_TB, F_PBC, F_EMAILS, F_STATUS]
demo("t16b", day=1, skill="1.6b", sec=DEMOS["t16"]["sec"], title="Project 2: a second agent", tool="Claude Projects", files=TRACK_FILES,
 kind="task", hands_on=True, minutes=25, solo="on your own",
 setup=["Pick a second track, not your first one. Download its file from step 8 of the Day 1 lab page.",
        "In Claude, click Projects, then + New Project. Name it after the track's task, for example Lease key terms.",
        "Click Set project instructions. Paste the Five-part template (prompt sheet, Task 1.6b) and fill it in for the track's starting example. Save.",
        "Start a chat in the Project, attach the file and send the Test run line. Check 2 items by hand. Fix the instructions, not the answer."],
 prompts=[("Five-part template", FIVE_TEMPLATE), ("Test run", "Run on the attached file. Then list every row you are not sure about.")],
 expected="A second Project on a different track, right on the two items checked by hand.",
 say="Same five parts, new data. Faster the second time.", point="The method is the same for every task.",
 backup=[("h", "The starting example for each track"), ("ul", ["Extraction: lease agreements to a key-terms schedule.", "Analysis: the two-year trial balance to the movements over 10% and over KWD 5,000, with a question for the client on each.",
          "Workflow: the request list and the client emails to a status tracker and follow-up drafts.", "Reporting: the engagement status sheet to one weekly summary for a manager."])],
 answer=[("h", "Check"), ("ul", ["A second Project, named after its task.", "Five-part instructions written for the new track.", "Two items checked by hand match the agent's result."])],
 deliverable="A second Project, on a different track and a different file.",
 fallback="Anyone stuck copies the structure of their first Project and changes only the Role, the Steps and the Output columns.",
 hint="Copy the structure of your first Project. Change the role, the steps and the columns.",
 stretch=["Run the same request in a second chat inside the Project. Compare the two results."])
demo("t18b", day=1, skill="1.8b", sec=DEMOS["t18"]["sec"], title="Artifact 2: a different kind of output", tool="Claude · artifacts", files=TRACK_FILES,
 kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Open your second Project (Task 1.6b) and start a new chat. Attach that track's file again.",
        "Copy one prompt from the prompt sheet, Task 1.8b: a chart, or a one-page memo. Send it.",
        "Open the artifact. Check two numbers or facts in it against the file.",
        "Ask for one change, such as a new title or one more column, and watch the artifact update."],
 prompts=[("Artifact 2: a chart", "Make an artifact: a bar chart of [what to show, for example the five largest items] from the attached file. Give it a title, label both axes, and list the numbers under the chart. Use only the file."),
          ("Artifact 2: a one-page memo", "Make an artifact: a one-page memo to the engagement manager that sums up the attached file in five bullet points, then lists what needs action this week. Use only the file. Write Not found for anything missing.")],
 expected="One chart or one memo from the second track's file, checked against the file on two points.",
 say="A table is one kind of output. A chart or a memo is another.", point="Ask for the shape the reader needs.",
 backup=[("h", "What a good second artifact looks like"), ("ul", ["Chart: a title, labeled axes, and the numbers listed under it.", "Memo: five bullet points, then the actions for this week, with Not found where data is missing."])],
 answer=[("h", "Check"), ("ul", ["The artifact opens and can be downloaded.", "Two numbers or facts match the file.", "One requested change shows in the same artifact."])],
 deliverable="A second artifact, of a different kind, from different data.",
 fallback="If the chart does not draw, ask for the memo instead.",
 hint="Ask for one change at a time. Claude updates the same artifact.",
 stretch=["Download the artifact, or ask Claude to save it as a file."])
demo("t19b", day=1, skill="1.9b", sec=DEMOS["t19"]["sec"], title="Skill 2: package your second agent", tool="Claude · skills", files=TRACK_FILES,
 kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Open your second Project (Task 1.6b). In a chat, paste Make the skill from the prompt sheet, Task 1.9b, with a new skill name. Save it when Claude offers.",
        "Open Customize, then Skills. Check that both of your skills are listed.",
        "Click New chat, outside any Project. Attach the second track's file and ask for its task in one line. Did Claude pick the right skill?",
        "In another new chat, attach your first track's file. Does Claude pick your first skill this time?"],
 prompts=[("Make the skill", "Turn the instructions and knowledge of this Project into a skill named [your-second-skill-name]. Keep every rule word for word. Describe when to use it in one line."),
          ("Test it in a new chat", "[One line that asks for the second task], using the attached file.")],
 expected="Two saved skills. In a fresh chat, Claude picks the right one for each file.",
 say="Two skills. Claude picks the one whose description fits.", point="A clear one-line description is how Claude picks the right skill.",
 backup=[("h", "If Claude picks the wrong skill"), ("ul", ["Open the skill and make its one-line description more specific: name the file type and the task.", "Test again in a new chat."])],
 answer=[("h", "Check"), ("ul", ["Two skills under Customize, then Skills.", "Each file gets the right skill in a fresh chat."])],
 deliverable="Two skills saved, each picked for the right file.",
 fallback="If skills are off on an account, continue with the Project. The trainer turns them on at the break.",
 hint="Each skill needs a name and one line on when to use it, so Claude can tell them apart.",
 stretch=["Share one of your skills with a member of your team."])
# keep each second round next to its first round (the prompt sheet and the lab follow this order)
def _after(new, base):
    global DEMOS
    items = [(k, v) for k, v in DEMOS.items() if k != new]
    i = [k for k, _v in items].index(base) + 1
    items.insert(i, (new, DEMOS[new]))
    DEMOS.clear(); DEMOS.update(items)
_after("t16b", "t16"); _after("t18b", "t18"); _after("t19b", "t19")
# the first rounds get shorter so both rounds fit in the same lessons
DEMOS["t16"]["minutes"] = 40; DEMOS["t16"]["say"] = "Struggle first. A hint at 10 minutes, then the most common fixes at 20."
DEMOS["t17"]["minutes"] = 12; DEMOS["t18"]["minutes"] = 11; DEMOS["t19"]["minutes"] = 14; DEMOS["t110"]["minutes"] = 8
DEMOS["t110"]["setup"] = [x.replace("step 11 of the Day 1 lab page", "step 14 of the Day 1 lab page") for x in DEMOS["t110"]["setup"]]
DEMOS["t16"]["minutes"] = 48; DEMOS["t16b"]["minutes"] = 29

# ===================================================================== Artifacts and skills move to Day 2 (Aya, 15 Nov, after Day 1)
# Day 1 ended after connectors. Day 2 opens with the output lesson (Demo 1.7, Tasks 1.8 and 1.8b) and the package lesson
# (Demo 1.8, Tasks 1.9, 1.9b and 1.10), because every Day 2 task uses the team's skill. Numbers stay, so nothing on Day 2 is renumbered.
BLOCK.update({6: (1, "Lesson 5 · Build: Input"), 7: (2, "Lesson 2 · Build: Package"), 8: (1, "Lesson 6 · Show and tell"),
              9: (2, "Lesson 3 · From agent to system"), 10: (2, "Lesson 4 · Make it run on its own"), 11: (2, "Lesson 5 · New inputs, outputs and n8n"),
              12: (2, "Lesson 6 · Fit it to your department"), 13: (2, "Lesson 7 · Test and prepare the demo"), 14: (2, "Lesson 1 · Build: Output")})
_MOVED = {"d18": 14, "t18": 14, "t18b": 14, "d19": 7, "t19": 7, "t19b": 7, "t110": 7}
for _k, _s in _MOVED.items():
    DEMOS[_k]["day"] = 2; DEMOS[_k]["sec"] = _s
_items = [(k, v) for k, v in DEMOS.items() if k not in _MOVED]
_i = [k for k, _v in _items].index("d21")
_items[_i:_i] = [(k, DEMOS[k]) for k in _MOVED]
DEMOS.clear(); DEMOS.update(_items)

# Places, named the same way on Day 2: the Day 2 lab page (workshop site → Day 2 → Open the lab), the prompt sheet (Day 2 page → Open the prompt sheet),
# Claude (claude.ai), and the sandbox Drive (Mirqab sandbox → Packs, and each team's folder with Inbox, Processed, Outputs and Log).
LAB2 = "the Day 2 lab page"
SHEET2 = "the prompt sheet (Day 2 page → Open the prompt sheet)"
TEAM = f"{D.SANDBOX} → [your team folder]"
WORKFLOW_CARD_TEMPLATE = ("When: [a day and a time, for example daily at 08:00]\n"
                          f"Input: [your team folder: {D.SANDBOX} / Team 1 to Team 4 / Inbox]\n"
                          "Skill: [your skill's name, as it shows under Customize, then Skills]\n"
                          "Output: [the file name in Outputs, with the date and time, and a run-log file in Log]\n"
                          "Who reviews: [one person's name]")
DEMOS["t21"]["prompts"].insert(0, ("Workflow card template", WORKFLOW_CARD_TEMPLATE))
_STEPS2 = {
 "t18": ["Get your track's file from step 1 of the Day 2 lab page, or use yesterday's copy.",
         'Copy the Output rule from the prompt sheet (Day 2 page → Open the prompt sheet), Task 1.8. Put your columns in the brackets, in order.',
         "Paste the rule at the end of your first Project's instructions, under Output format. Save.",
         'Run it twice, each time in a new chat in the Project. Same columns, order and total line? If not, fix the rule.'],
 "t18b": [f"Open your second Project (Task 1.6b) and start a new chat. Attach that track's file again: it is under step 2 of {LAB2}.",
          f"Copy one prompt from {SHEET2}, Task 1.8b: a chart, or a one-page memo. Send it.",
          "Open the artifact. Check two numbers or facts in it against the file.",
          "Ask for one change, such as a new title or one more column, and watch the artifact update."],
 "t19": ["Code execution is on for the team: the owner turned it on. If your skill does not save, tell the trainer.",
         f"In Claude, open your first Project and start a chat. Copy Make the skill from {SHEET2}, Task 1.9. Put your skill's name in the brackets and send it. Save the skill when Claude offers.",
         "Check that it is saved: open Customize, then Skills, and find your skill's name.",
         f"Click New chat, outside the Project. Attach your track file (step 3 of {LAB2}). Copy Test it in a new chat, fill in the brackets, and send it. Claude should use your skill and return the same shape.",
         f"Open the cheat sheet (Day 2 page → Cheat sheet) and find the Package row. In the box in step 3 of {LAB2}, write where this skill would live in ChatGPT, Copilot or Gemini."],
 "t19b": [f"Open your second Project (Task 1.6b). In a chat, paste Make the skill from {SHEET2}, Task 1.9b, with a new skill name. Save it when Claude offers.",
          "Open Customize, then Skills. Check that both of your skills are listed.",
          f"Click New chat, outside any Project. Attach the second track's file (step 4 of {LAB2}) and ask for its task in one line. Did Claude pick the right skill?",
          "In another new chat, attach your first track's file. Does Claude pick your first skill this time?"],
 "t110": [f"Download the messy file for your track from step 5 of {LAB2}. Workflow track: also attach mirqab-pbc-request-list-abdali.xlsx (same step).",
          f"Click New chat. Attach the messy file. Copy Messy run from {SHEET2}, Task 1.10, and send it. Claude should use your skill.",
          "Check: did the agent flag the problem, or guess? Each file hides a gap the agent must flag (the invoice file has two). No file has two values that conflict.",
          f"Time the task: minutes by hand, minutes with the agent. Write both numbers in the box in step 5 of {LAB2}. You need them for your impact number this afternoon."],
 "t21": ["As a team, pick one Day 1 agent by a show of hands. You work on that person's laptop today: they are your skill owner.",
         f"Copy the Workflow card template from {SHEET2}, Task 2.1. Paste it in the box in step 6 of {LAB2}.",
         f"Fill in When, Input, Skill, Output and Who reviews. Input is your team folder: {D.SANDBOX} → Team 1 to Team 4 → Inbox.",
         "Raise your hand. The trainer checks your card at your table."],
 "t22": ["Work on the skill owner's laptop. In Google Drive, copy your track pack from Mirqab sandbox → Packs into your team folder's Inbox.",
         'In Claude, click Scheduled in the left sidebar, then New task, then Set up manually.',
         'Name it. Paste the Scheduled task prompt from the prompt sheet (Day 2 page → Open the prompt sheet), Task 2.2. Fill the brackets from your card (lab step 6).',
         'Approval mode: the one that saves and moves files without waiting. Daily at 08:00. Save.',
         'Run it once on demand. Check Outputs and Log, and compare with your Day 1 result.'],
 "t23": ['In Scheduled (left sidebar), open your task. Check its prompt has the empty-folder line (prompt sheet, Task 2.3).',
         'Workflow teams: add the request list to the skill as a reference file, and the tracker line. Analysis teams: add the monthly line.',
         "Copy your batch-2 file from Packs into your team's Inbox. Run on demand. Check Outputs and Log (lab step 8).",
         'Empty the Inbox and run again. The new run log should say No new files (lab step 9).'],
 "t25": [f"Download mirqab-review-rules.docx from step 10 of {LAB2}. Pick two rules for your department.",
         f"The skill owner copies Add the rules from {SHEET2}, Task 2.4, puts the two rules in the brackets word for word, and sends it in a new chat. Save the skill when Claude offers.",
         f"In Google Drive, copy your track's messy file from {D.SANDBOX} → Packs into {TEAM} → Inbox. In Claude, run the task on demand.",
         "Open Outputs and Log. Check: DRAFT in the title, a Reviewed by line, and the messy item flagged, not guessed."],
 "t26": ["Clean runs (10 min): copy your pack from Packs into your team's Inbox and run on demand, three times. Workflow teams: move the Outputs trackers to Processed first.",
         "Failed run (7 min): add the Fallback line (prompt sheet, Task 2.5) to the task's prompt. Copy mirqab-locked-test-file.pdf into the Inbox, run, read the log, delete it.",
         'Impact (4 min): your two times from lab step 5, and the formula on the impact slide.',
         'Demo plan (6 min): the Demo 2.6 prompt from the prompt sheet. Say who acts when a run fails.',
         'Rehearse once with a timer (10 min). Then copy a pack into the Inbox for the live run.'],
}
for _k, _v in _STEPS2.items():
    DEMOS[_k]["setup"] = [x for x in DEMOS[_k]["setup"] if x.startswith("[T]")] + _v

# Day 2 minutes: the moved lessons take 78 minutes, so Day 2's own tasks get shorter. Demo Day stays at 15:15.
DEMOS["t18"]["minutes"] = 12; DEMOS["t18b"]["minutes"] = 13
DEMOS["t21"]["minutes"] = 12; DEMOS["t22"]["minutes"] = 25; DEMOS["t23"]["minutes"] = 20; DEMOS["t25"]["minutes"] = 28; DEMOS["t26"]["minutes"] = 37
DEMOS["t21"]["deliverable"] = "Your team's workflow card, checked by the trainer at your table."
DEMOS["t22"]["say"] = "Struggle first. A hint at 8 minutes, then the three most common fixes at 15."
DEMOS["t19"]["say"] = "Your method, packaged. This afternoon a scheduled task calls it."
DEMOS["t19"]["answer"] = [("h", "Check"), ("ul", ["The skill name is short and clear.", "The rules are the same as in the Project.", "A fresh chat uses the skill and returns the fixed shape.",
                                                   "The transfer line names the skill's home in another tool: a skill or custom GPT (ChatGPT), an agent (Copilot) or a Gem (Gemini)."])]
DEMOS["t19"]["deliverable"] = "Your skill, saved and tested in a fresh chat, and one transfer line in the lab page."
DEMOS["t110"]["deliverable"] = "One flagged messy run and two numbers in the lab page: minutes by hand and with the agent."
DEMOS["t26"]["prompts"] = [p if p[0] != "Impact" else ("Impact", "From our run log, count the runs and the items flagged. Then calculate: ([minutes by hand] minus [minutes with the agent]) times [runs a month]. Our two times come from Task 1.10.")
                           for p in DEMOS["t26"]["prompts"]]
DEMOS["t26"]["hint"] = "Every number on your demo comes from your run log or your Task 1.10 times."
DEMOS["t26"]["expected"] = (f"Three clean runs and one failed-run test in the run log (Could not read: {F_LOCKED}, nothing guessed, the file left in the Inbox), "
                            "one impact number and a 5-minute plan per team, rehearsed once.")
DEMOS["t26"]["deliverable"] = "A Log folder with three clean runs and the failed-run test, and a 5-minute demo, rehearsed once, with its impact number."
# Day 2 demos run live: the trainer's steps say where things are
DEMOS["d21"]["setup"] = [f"[T] Open step 6 of {LAB2} on the presenting laptop. Paste the Workflow card template and fill it in box by box for the invoice workflow.",
                         "[T] Copy the finished card. In Claude, start a new chat and send Check our card with the card pasted in."]
DEMOS["d21"]["hint"] = "Who reviews is a name, not a team."
DEMOS["d111"]["fallback"] = "If the day ends before 16:25, run the task on demand from the Scheduled page, or show the backup run-log file."
DEMOS["t23"]["stretch"] = ["Make the first line of the output a count of files read. Rerun and check it against the run log."]
DEMOS["t23"]["setup"] = [x.replace("Copy your batch-2 file from Packs into your team's Inbox. Run on demand.", "Copy your batch-2 file from Packs into the Inbox. Run on demand.") for x in DEMOS["t23"]["setup"]]
DEMOS["t23"]["setup"] = ["Open your task under Scheduled. Check it has the empty-folder line (prompt sheet, Task 2.3).",
                         "Workflow teams: add the request list to the skill, and the tracker line. Analysis teams: the monthly line.",
                         "Copy your batch-2 file from Packs into the Inbox. Run on demand. Check Outputs and Log (lab step 8).",
                         "Empty the Inbox and run again. The run log should say No new files (lab step 9)."]

# ===================================================================== Day 2 rebuild (Aya, 15 Nov night)
# New order: skills (own task), artifacts (dashboards and decks), scheduled tasks, Claude or n8n or Power Automate (with the n8n demo),
# then a mini project on a department pack, project demos, Post-MAP, survey and certificates. The old Day 2 demos and tasks
# (the moved Day 1 output and package tasks, the team workflow card, batch 2, the rules, the failed run and Demo Day) are retired.
import day2_data as X
F_PORTFOLIO = X.F_PORTFOLIO
F_BRIEFS = X.F_BRIEFS
ALL_FILES = ALL_FILES + [F_PORTFOLIO] + X.PACK_FILES + [F_BRIEFS]
_OLD2 = [k for k, v in DEMOS.items() if v.get("day") == 2]     # retired at the end of content.py (its Day 1 lab still reads them while it loads)
def retire_old_day2():
    for _k in _OLD2: DEMOS.pop(_k, None)
BLOCK.update({20: (2, "Lesson 1 · Skills"), 21: (2, "Lesson 2 · Artifacts"), 22: (2, "Lesson 3 · Scheduled tasks"),
              23: (2, "Lesson 4 · Claude, n8n or Power Automate"), 24: (2, "Lesson 5 · Mini project"), 25: (2, "Lesson 6 · Project demos")})
LAB2 = "the Day 2 lab page"
SHEET2 = "the prompt sheet (Day 2 page → Open the prompt sheet)"
_K = X.PORT_KPI
def _kwd(x): return f"KWD {x:,.3f}"

SKILL_FROM_CARD = ("Help me build a Claude skill for a task I repeat at work. Here is my Agent Card, with no client or firm names: [paste your card]. "
                   "First ask me up to five questions about the steps, the rules and the output. Then write the skill: a short name in lowercase with hyphens, "
                   "a one-line description that says exactly when to use it, the steps, the rules, the output format with the columns in order, "
                   "and what to do when unsure (write Not found, never guess). Then make it a skill file I can save.")
TEST_FILE = ("Make a fictional test file for this skill: [file type, for example an Excel sheet] with 10 to 15 rows and 2 planted problems the skill should flag. "
             "Use made-up names and amounts only. Do not tell me where the problems are.")
DESC_FIX = ("Here is my skill's description: [paste it]. Rewrite it in one or two sentences so Claude uses the skill for [my task] with [file type], "
            "and not for other requests. Keep it under 200 characters. Then update the skill so I can save it again.")
DASH_DEMO = ("Role: You are a reporting analyst at Mirqab & Co. Data: the attached engagement portfolio. Build an interactive dashboard artifact for the partners. "
             "KPI tiles at the top: total fee, billed as % of fee, collected as % of billed, hours used as % of budget, engagements over budget, "
             "reports overdue (due before 16 November 2026 and not Closed). Charts: fee by service line; budget against actual hours by engagement. "
             "A table of engagements that are At risk or Delayed. A filter by service line. Rules: use only the file and calculate with code. "
             "If a value is blank or does not make sense, leave it out of that KPI and list it under Data issues. Never guess. Show the date of the data.")
DECK_DEMO = ("Turn this dashboard into a 5-slide presentation for Monday's partners' meeting: a title, the KPIs, what is at risk, the data issues, "
             "and the decisions we need. Use only the dashboard's figures. One idea per slide.")
DASH_TEMPLATE = ("Role: You are a [job title] at Mirqab & Co. Data: the attached [file]. Build an interactive dashboard artifact for [who reads it]. "
                 "KPI tiles at the top: [3 to 6 numbers, each with how to calculate it]. Charts: [1 or 2 charts]. A table of [the rows that need action]. "
                 "A filter by [a column]. Rules: use only the file and calculate with code. If a value is blank or does not make sense, "
                 "leave it out of that KPI and list it under Data issues. Never guess. Show the date of the data.")
DASH_CHECK = "List every KPI on the dashboard with the formula you used and the rows you left out. Do not change the dashboard."
DECK_TEMPLATE = ("Turn this dashboard into a [5]-slide presentation for [audience and meeting]: a title, the key numbers, what needs attention, "
                 "the data issues, and the decision or next step. Use only the dashboard's figures. One idea per slide.")
ARTIFACT_IN_SKILL = ("Add this to my skill [skill name]: after the analysis, always build the dashboard in this exact layout: [the tiles, the charts and the table, in order]. "
                     "Keep every other rule word for word. Then update the skill so I can save it again.")
PERSONAL_SCHED = (f"Use the [your skill name] skill. Read the files in Google Drive: {D.SANDBOX} / [your Day 1 track folder] / Inbox whose names start with [your initials]. "
                  "Do not move, rename or delete any file: the folder is shared today. Save the result in [your folder] / Outputs, named "
                  "[your initials]-[task]-YYYY-MM-DD-HHMM, with the date and time of the run. Save a run log in [your folder] / Log, named "
                  "runlog-[your initials]-YYYY-MM-DD-HHMM.txt, with one line: date, files read, items flagged, file saved. "
                  "If there are no files to read, write No new files in the run log and stop.")
PROJECT_CARD = ("Department: [your department pack, or your own team]\n"
                "Task: [what the agent does, in one line]\n"
                "Input: [the file it reads, and where it lives]\n"
                "Instruction: [the steps and two rules; what to do when unsure]\n"
                "Output: [the artifact: a dashboard, a report or a deck, and its layout]\n"
                "When: [the schedule, for example every Sunday at 08:00]\n"
                "Who reviews: [one person's role or name]\n"
                "Impact: [minutes by hand] - [minutes with the agent] x [runs a month]")
BUILD_PLAN = ("Here is my project card: [paste it]. Give me a build plan for Claude in five steps: Project, skill, artifact, scheduled task, test. "
              "Two lines for each step. Do not build anything yet.")
CHECK3 = "List three figures from my output and the exact rows they come from in the source file, so I can check them by hand. Do not change anything."
DEMO_SCRIPT = ("Write a 3-minute demo script for my project: the problem, the card, a live run, the artifact, the impact "
               "((minutes by hand minus minutes with the agent) times runs a month), and what I would automate next. Use only facts from my files and runs.")

# ------------------------------------------------------------------ Lesson 1 · Skills
demo("e21", day=2, skill="2.1", sec=20, title="The invoice-match skill, live", tool="Claude · skills", files=[F_INV, F_LEDGER], kind="demo",
 setup=["[T] Open Customize, then Skills. Open mirqab-invoice-match (built before Day 1). Show its name, its one-line description and its steps.",
        "[T] Click New chat, outside any Project. Attach the October invoices and ledger. Send the Run line.",
        "[T] Point at the line where Claude says it is using the skill, then at the table.",
        "[T] In a new chat, send the email request. No skill loads: the description does not match."],
 prompts=[("Run line (new chat, no Project)", "Match the attached October invoices to the attached October purchase ledger."),
          ("A request that should not use the skill", "Draft a short thank-you email to Abdali Foods for sending the October documents.")],
 expected="Claude says it is using mirqab-invoice-match and returns the Task 1.5 table: BPK-4471, WDS-20931 and SGT-11205 Matched; SCC-0718 Amount differs (36.000); FSC-3390 Not in ledger. The email request runs without the skill.",
 say="One skill, three places: any chat, any Project, any schedule. The description decides when it loads.",
 point="The description decides when Claude uses a skill.",
 backup=[("h", "What the skill holds"), tbl(["Part", "mirqab-invoice-match"], [("Name", "mirqab-invoice-match"), ("Description", "Match supplier invoices to a purchase ledger and flag every difference."),
         ("Steps and rules", "The five parts of the invoice Project, word for word"), ("Reference file", F_TEMPLATE)]),
         ("h", "The result in a fresh chat"), tbl(D.TEMPLATE_HEAD, MATCH_FULL)],
 fallback="If the skill does not load, say Use the mirqab-invoice-match skill in the request. If it still fails, show the backup table.",
 hint="Find the line where Claude names the skill it is using.")

demo("u21", day=2, skill="2.1", sec=20, title="A skill for your own task", tool="Claude · skills", files=[], kind="task", hands_on=True, minutes=25, solo="on your own",
 setup=["Open your Agent Card from yesterday: step 4 of the Day 1 lab page. No card? Use your strongest task from Task 1.3.",
        f"In Claude, click New chat. Copy Turn my task into a skill from {SHEET2}, Task 2.1. Paste your card in the brackets and answer Claude's questions.",
        "When Claude shows the skill, save it. Check it is listed: Customize, then Skills.",
        "In the same chat, send Make a test file with the brackets filled. Download the file.",
        "Click New chat. Attach the test file and ask for your task in one line. Does Claude use your skill and flag both planted problems?"],
 prompts=[("Turn my task into a skill", SKILL_FROM_CARD), ("Make a test file", TEST_FILE), ("Test it in a new chat", "[One line that asks for your task], using the attached file.")],
 expected="A saved skill with a short name and a one-line description; a fresh chat that names the skill, returns the fixed shape and flags both planted problems.",
 say="Your own task this time, not the invoices. Struggle first; a hint at 8 minutes.",
 point="A skill is your method, written once, used anywhere.",
 backup=[("h", "A good skill has"), ("ul", ["A short name in lowercase with hyphens, for example lease-key-terms.", "One line on when to use it: the task and the file type.",
                                            "Steps, rules, the output columns in order, and When unsure.", "No client or firm names, and no real figures."])],
 answer=[("h", "Approve a skill when"), ("ul", ["The name is short and clear.", "The description names the task and the file type.", "It has steps, at least two rules, the output columns and a When unsure line.",
                                                 "No client names or real data: it can be shared.", "A fresh chat names the skill and flags both planted problems."])],
 deliverable="Your own skill, saved and tested in a fresh chat on a fictional test file.",
 fallback="If saving fails, keep the skill text, run it as Project instructions for now, and the trainer helps at the break. Code execution must be on (Settings, then Capabilities).",
 hint="If Claude does not use your skill, make its description name the task and the file type.",
 stretch=["Share the skill with a colleague: Customize, then Skills, the ... menu, then Share."])

demo("u22", day=2, skill="2.2", sec=20, title="Will Claude pick your skill?", tool="Claude · skills", files=[], kind="task", hands_on=True, minutes=8, solo="on your own",
 setup=["Click New chat. Ask for your task in your own words, with the test file. Did Claude use your skill?",
        "Click New chat. Ask for the same task in different words. Did it use the skill again?",
        "Click New chat. Ask for something unrelated, such as an email. The skill should not load.",
        f"If a test failed, send Sharpen the description from {SHEET2}, Task 2.2, save the skill again and repeat the test."],
 prompts=[("Sharpen the description", DESC_FIX)],
 expected="Two requests that load the skill and one that does not. A description that names the task and the file type.",
 say="Three chats: two that should load your skill, one that should not.",
 point="A clear description is how Claude picks the right skill.",
 backup=[("h", "Weak and strong descriptions"), tbl(["Weak", "Strong"], [("Helps with Excel files.", "Match supplier invoices (PDF) to a purchase ledger (Excel) and flag every difference."),
         ("Audit helper.", "Extract key terms from lease agreements (PDF) into a schedule with dates in YYYY-MM-DD.")])],
 answer=[("h", "Check"), ("ul", ["Two of two matching requests load the skill.", "The unrelated request does not.", "The description names the task and the file type."])],
 deliverable="Three test chats and, if needed, a sharper description.",
 fallback="If the skill never loads, write Use the [name] skill at the start of the request, and fix the description at the break.",
 hint="Name the task and the file type in the description.",
 stretch=["Ask a neighbor to request your task in their own words. Does your skill load for them on your laptop?"])

# ------------------------------------------------------------------ Lesson 2 · Artifacts
demo("e22", day=2, skill="2.2", sec=21, title="A KPI dashboard, then a deck", tool="Claude · artifacts", files=[F_PORTFOLIO], kind="demo",
 setup=["[T] Click New chat. Attach mirqab-engagement-portfolio-2026.xlsx. Send the Dashboard request.",
        "[T] Click a service line in the filter. Read two KPI tiles aloud and show where each comes from in the file.",
        "[T] Open Data issues: two rows. Then send the Deck request in the same chat."],
 prompts=[("Dashboard request", DASH_DEMO), ("Deck request", DECK_DEMO)],
 expected=(f"KPI tiles: total fee {_kwd(_K['fee'])}; billed {_K['billed_pct']}% of fee; collected {_K['collected_pct']}% of billed; hours used {_K['hours_used_pct']}% of budget "
           f"({X.PORTFOLIO[16][0]} left out); {len(_K['over_budget'])} engagements over budget; {len(_K['overdue'])} reports overdue. "
           f"Data issues: {X.PORTFOLIO[16][0]} (blank hours) and {X.PORTFOLIO[8][0]} (collected more than billed). Then a 5-slide deck with the same figures."),
 say="One file, one request: a dashboard the partners can click. Then the same figures as slides.",
 point="Ask for the audience, the KPIs with their formulas, the layout and the rules.",
 backup=[("h", "The KPI tiles"), tbl(["KPI", "Value"], [("Total fee", _kwd(_K["fee"])), ("Billed (% of fee)", f"{_K['billed_pct']}%"), ("Collected (% of billed)", f"{_K['collected_pct']}%"),
         ("Hours used (% of budget)", f"{_K['hours_used_pct']}% ({X.PORTFOLIO[16][0]} left out)"), ("Over budget", ", ".join(_K["over_budget"])), ("Reports overdue", ", ".join(_K["overdue"]))]),
         ("h", "Data issues"), ("ul", X.PORT_ISSUES), ("h", "Fee by service line (KWD)"), tbl(["Service line", "Fee"], [(k, f"{v:,.3f}") for k, v in _K["fee_by_line"].items()])],
 fallback="If the dashboard does not draw, ask for the KPI table first, then the charts. Show the backup tiles.",
 hint="Every KPI tile must match the file. The two data issues must be listed, not hidden.")

demo("u23", day=2, skill="2.3", sec=21, title="Your KPI dashboard", tool="Claude · artifacts", files=[], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=[f"Pick one department pack in step 3 of {LAB2} and download it. Or use the test file from Task 2.1.",
        f"Click New chat and attach the file. Copy the Dashboard request from {SHEET2}, Task 2.3. Fill the brackets: who reads it, 3 to 6 KPIs with formulas, the charts, the table.",
        "Check three KPI tiles by hand in Excel, for example with SUM or COUNTIF. Send Check it to see each formula.",
        "Ask for one change, such as a new filter or a different chart, and watch the dashboard update."],
 prompts=[("Dashboard request", DASH_TEMPLATE), ("Check it", DASH_CHECK)],
 expected="A dashboard with KPI tiles, one or two charts, a table and a filter; three KPIs that match a hand check; both planted problems listed under Data issues.",
 say="Your audience, your KPIs, your rules. Then check three tiles by hand.",
 point="A dashboard is only as good as the three numbers you checked.",
 backup=[("h", "The department packs")] + [("p", f"<b>{p['dept']}</b> · {p['file']} · {p['artifact']}") for p in X.PACKS],
 answer=[("h", "What each pack should show")] + [x for p in X.PACKS for x in (("p", f"<b>{p['dept']}</b> ({p['file']})"),
          ("ul", [f"{k}: {v}" for k, v in p["kpis"].items()] + [f"Data issue: {i}" for i in p["issues"]]))],
 deliverable="A dashboard from one file, three KPIs checked by hand, and both planted problems under Data issues.",
 fallback="If the dashboard does not draw, ask for the KPI table first, then one chart at a time.",
 hint="Each pack hides two problems. Look for blanks, duplicates and values that do not add up.",
 stretch=["Add a second filter and a notes box that says who reviewed the dashboard."])

demo("u24", day=2, skill="2.4", sec=21, title="From dashboard to presentation", tool="Claude · artifacts", files=[], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"In the same chat as your dashboard, copy the Deck request from {SHEET2}, Task 2.4. Fill in the audience and the number of slides. Send it.",
        "Check: every number on the slides is on the dashboard. Nothing new, nothing rounded differently.",
        "Ask for one change, such as a shorter title or one more slide.",
        "Put the layout in your skill: send Put it in my skill, then save the skill again. Next month, the same dashboard comes back."],
 prompts=[("Deck request", DECK_TEMPLATE), ("Put it in my skill", ARTIFACT_IN_SKILL)],
 expected="A short deck whose figures all match the dashboard, and a skill that now builds the dashboard in a fixed layout.",
 say="The same figures, a different reader. Then the layout goes into the skill.",
 point="Write the layout into the skill, and every run returns the same dashboard.",
 backup=[("h", "A good partner deck"), ("ol", ["Title and the date of the data", "The key numbers", "What needs attention", "Data issues", "The decision or next step"])],
 answer=[("h", "Check"), ("ul", ["Every figure on the slides is on the dashboard.", "The data issues have their own slide.", "The skill now names the dashboard layout, and it was saved again."])],
 deliverable="A short deck from your dashboard, and your skill updated with the dashboard layout.",
 fallback="If the deck does not draw, ask for a one-page memo with the same five parts.",
 hint="Every number on a slide must be on the dashboard.",
 stretch=["Ask for a one-page memo for a manager who will not open the deck."])

# ------------------------------------------------------------------ Lesson 3 · Scheduled tasks
demo("e23", day=2, skill="2.3", sec=22, title="Schedule the invoice skill", tool="Claude · scheduled tasks", files=[], kind="demo",
 setup=["[T] Before 11:00, check that 01 Invoices / Inbox holds one copy of the October invoices and ledger.",
        "[T] Click Scheduled in the left sidebar, then New task, then Set up manually. If the form has no time field for Daily, use Create with Claude and say the time.",
        "[T] Name, prompt, approval mode, frequency daily at 08:00. Save. Run it once on demand.",
        "[T] Open Outputs and Log in the Drive while it runs."],
 prompts=[("Scheduled task prompt", INVOICE_SCHED)],
 expected="The task shows on the Scheduled page, daily at 08:00. The test run saves a match file in Outputs and a run-log file in Log, and moves the two files to Processed.",
 say="Name, prompt, frequency. The prompt calls the skill from this morning.",
 point="A scheduled task is a calendar reminder that also does the work.",
 backup=[("h", "The fields"), tbl(["Field", "Value"], [("Name", "Mirqab invoice match, daily"), ("Prompt", "Calls mirqab-invoice-match; reads Inbox; saves to Outputs; moves to Processed; saves a run-log file in Log"),
         ("Approval mode", "The mode that lets the run save and move Drive files without waiting"), ("Frequency", "Daily at 08:00 (Kuwait works Sunday to Thursday; Friday and Saturday runs log No new files)")])],
 fallback="If Cowork is not on, show the backup fields and run the prompt by hand in a chat.",
 hint="Run it once on demand, then open Outputs and Log.")

demo("u25", day=2, skill="2.5", sec=22, title="Schedule your skill", tool="Claude · scheduled tasks", files=[], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"Rename your test file (or pack file) so it starts with your initials. Upload it to {D.SANDBOX} → your Day 1 track folder → Inbox.",
        "In Claude, click Scheduled in the left sidebar, then New task, then Set up manually.",
        f"Name it. Paste the Scheduled task prompt from {SHEET2}, Task 2.5, and fill the brackets.",
        "Approval mode: the one that saves files without waiting. Frequency: weekly, Sunday at 08:00. Save.",
        "Run it once on demand. Open Outputs and Log: your file and your run log, both with your initials."],
 prompts=[("Scheduled task prompt", PERSONAL_SCHED)],
 expected="A weekly task on the Scheduled page; one run on demand that saves an output and a run log with the person's initials; nothing moved or deleted.",
 say="Your skill, on a schedule. Run it once now, so you trust Sunday's run.",
 point="If the test run works, the schedule will work.",
 backup=[("h", "No Drive today?"), ("p", "Schedule a task that needs no files, for example: Every Sunday at 08:00, use my [skill] skill to draft this week's checklist. Run it once on demand.")],
 answer=[("h", "Check"), ("ul", ["The task is on the Scheduled page, weekly.", "The run on demand saved a file named with the initials and the date and time.", "A run log with one line is in Log.", "No file was moved or deleted."])],
 deliverable="Your skill on a weekly schedule, run once on demand, with an output and a run log.",
 fallback="If the form has no time field, use Create with Claude and say the time. If Cowork is off on an account, run the prompt in a chat and schedule it on the trainer's account.",
 hint="Most failures are a folder name that does not match the Drive exactly.",
 stretch=["Add one line to the prompt: the first line of the output says how many files were read."])

# ------------------------------------------------------------------ Lesson 4 · Claude, n8n or Power Automate
demo("e24", day=2, skill="2.4", sec=23, title="Build a workflow in n8n", tool="n8n", files=[], kind="demo",
 setup=["[T] Play the n8n demo video from the staff backup page, Demo 2.4. Or open the workflow Mirqab · invoice routing in the n8n workspace and click Execute workflow.",
        "[T] Name each part as it appears: the trigger, the Code step, the If step, the two outputs.",
        "[T] Open the If step after the run: show the items on the true branch and on the false branch."],
 prompts=[("The Code step: this week's invoices (JavaScript in n8n)", "return [{json:{invoice:'BPK-4471',supplier:'Bayan Packaging',amount_kwd:2145.750}},{json:{invoice:'WDS-20931',supplier:'Wafra Dairy Supplies',amount_kwd:3860.000}},{json:{invoice:'SCC-0718',supplier:'Shuwaikh Cold Store',amount_kwd:1248.500}},{json:{invoice:'SGT-11205',supplier:'Sulaibiya Grain Traders',amount_kwd:5312.250}},{json:{invoice:'FSC-3390',supplier:'Fintas Spice',amount_kwd:742.125}}];")],
 expected="The run turns every step green. The trigger starts it, the Code step returns 5 invoices, and the If step sends 3 to Supervisor review (over KWD 2,000: BPK-4471, WDS-20931, SGT-11205) and 2 to Approved (SCC-0718, FSC-3390).",
 say="Trigger, steps, output. Same words in Claude, n8n and Power Automate.",
 point="n8n connects systems step by step. Claude reads, judges and writes.",
 backup=[("h", "The workflow"), tbl(["Step", "n8n node", "What it does"], [("Trigger", "Schedule Trigger", "Starts the workflow every weekday at 08:00, or by hand with Execute workflow"),
         ("Function", "Code", "Returns this week's invoices as items"), ("Condition", "If", "amount_kwd is larger than 2000"),
         ("Output, true", "Edit Fields: Supervisor review", "Sets status Supervisor review and the reviewer"), ("Output, false", "Edit Fields: Approved", "Sets status Approved")])],
 fallback="If n8n is slow or signed out, play the video. If the video does not play, step through the backup table.",
 hint="What starts this workflow, and where does each invoice end up?")

# ------------------------------------------------------------------ Lesson 5 · Mini project
demo("u26", day=2, skill="2.6", sec=24, title="Mini project: your department's agent", tool="Claude · everything", files=[], kind="task", hands_on=True, minutes=85, solo="on your own or in pairs",
 setup=[f"Pick a department pack in step 7 of {LAB2}, or your own task. Fill the Project card from {SHEET2}, Task 2.6, in the box in step 7 (10 min).",
        "Build: a Project with five-part instructions, then a skill from it (25 min).",
        "Output: a dashboard or report artifact, with its layout written in the skill (20 min).",
        "When: a scheduled task, run once on demand, with a run log (15 min).",
        "Check three figures against the file. Mark the output DRAFT with a Reviewed by line. Write your impact number and a 3-minute demo script (15 min)."],
 prompts=[("Project card", PROJECT_CARD), ("Build plan", BUILD_PLAN), ("Check three figures", CHECK3), ("Demo script", DEMO_SCRIPT)],
 expected="Each person or pair has an agent for one department: a Project, a skill, an artifact in a fixed layout, a scheduled task run once, three figures checked, and an impact number.",
 say="Everything from two days, on one department's work. Struggle first; I come round at 20 minutes.",
 point="Card, Project, skill, artifact, schedule, review: one agent.",
 backup=[("h", "The department packs")] + [x for p in X.PACKS for x in (("p", f"<b>{p['dept']}</b> · {p['file']}"), ("ul", [p["problem"], "Agent: " + p["agent"], "Artifact: " + p["artifact"], "When: " + p["schedule"]]))],
 answer=[("h", "What each pack hides (two problems each)")] + [("ul", [f"{p['dept']}: " + " ".join(p["issues"]) for p in X.PACKS])],
 deliverable="Your department agent: Project, skill, artifact, a scheduled task run once, three figures checked, and an impact number.",
 fallback="Behind at 45 minutes? Skip the schedule; show the skill and the artifact, and say when it would run.",
 hint="Build in order: card, Project, skill, artifact, schedule. Check before you polish.",
 stretch=["Share your skill with a colleague from the same department and ask them to break it."])

# keep the task slides inside 1440 x 810: the extra prompts go on the prompt sheet only (templates have COPY buttons there)
DEMOS["u21"]["templates"] = [p for p in DEMOS["u21"]["prompts"] if p[0] == "Test it in a new chat"]
DEMOS["u21"]["prompts"] = [p for p in DEMOS["u21"]["prompts"] if p[0] != "Test it in a new chat"]
DEMOS["u26"]["templates"] = [("Build plan", BUILD_PLAN), ("Demo script", DEMO_SCRIPT)]
DEMOS["u26"]["prompts"] = [p for p in DEMOS["u26"]["prompts"] if p[0] in ("Project card", "Check three figures")]

# shorter task slides (validator: three Day 2 task slides ran into the progress bar)
SKILL_FROM_CARD = ("Help me build a Claude skill for a task I repeat at work. My Agent Card, with no client or firm names: [paste your card]. "
                   "Ask me up to five questions first. Then write the skill: a short lowercase name with hyphens, a one-line description of when to use it, "
                   "the steps, the rules, the output columns in order, and When unsure (write Not found, never guess). Make it a skill file I can save.")
DEMOS["u21"]["prompts"] = [("Turn my task into a skill", SKILL_FROM_CARD), ("Make a test file", TEST_FILE)]
DEMOS["u21"]["setup"] = ["Open your Agent Card (Day 1 lab page, step 4), or your strongest task from Task 1.3.",
                         "New chat: paste Turn my task into a skill (prompt sheet, Task 2.1) with your card. Answer the questions.",
                         "Save the skill. Check it under Customize, then Skills. Then send Make a test file.",
                         "New chat: attach the test file and ask for your task in one line. Skill used? Both problems flagged?"]
DEMOS["u23"]["setup"] = [f"Download one department pack (step 3 of {LAB2}), or use your Task 2.1 test file.",
                         "New chat: attach it and paste the Dashboard request (prompt sheet, Task 2.3). Fill the brackets.",
                         "Check three KPI tiles by hand in Excel. Then send Check it.",
                         "Ask for one change and watch the dashboard update."]
DEMOS["u26"]["templates"] = [("Project card", PROJECT_CARD), ("Demo script", DEMO_SCRIPT)]
DEMOS["u26"]["prompts"] = [("Build plan", BUILD_PLAN), ("Check three figures", CHECK3)]
DEMOS["u26"]["setup"] = [f"Card (10 min): pick a pack (step 7 of {LAB2}) or your own task. Fill the Project card from the prompt sheet.",
                         "Build (25 min): a Project with five-part instructions, then a skill.",
                         "Output (20 min): a dashboard or report, its layout written in the skill.",
                         "When (15 min): a scheduled task, run once on demand, with a run log.",
                         "Check (15 min): three figures, DRAFT and Reviewed by, impact, demo script."]

# the n8n demo video (recorded in Aya's n8n workspace on 15 Nov night, captioned): a file on the Demo 2.4 slide, the prompt sheet and lab step 6
F_N8N_VIDEO = "mirqab-n8n-demo-invoice-routing.mp4"
ALL_FILES = ALL_FILES + [F_N8N_VIDEO]
DEMOS["e24"]["files"] = [F_N8N_VIDEO]
DEMOS["e24"]["setup"] = ["[T] Click the video file on the slide (100 seconds, captioned). Or open the workflow Mirqab · invoice routing in your n8n workspace and click Execute.",
                         "[T] Name each part as it appears: the trigger, the Code step, the If step, the two outputs.",
                         "[T] Pause on the If step: 3 invoices on the true branch, 2 on the false branch."]
DEMOS["e24"]["expected"] = ("Every node turns green. The trigger starts it, the Code step returns 5 invoices, and the If step sends 3 to Supervisor review "
                            "(over KWD 2,000: BPK-4471, WDS-20931, SGT-11205) and 2 to Approved (SCC-0718, FSC-3390).")
DEMOS["e24"]["fallback"] = "If the video does not play, step through the backup table. If n8n is signed out, the video is enough."
DEMOS["e24"]["backup"][1] = tbl(["Step", "n8n node", "What it does"], [("Trigger", "Schedule Trigger", "Starts the workflow every day at 08:00, or by hand with Execute workflow"),
         ("Function", "Code (Get this week's invoices)", "Returns this week's invoices as items"), ("Condition", "If (Over KWD 2,000?)", "amount_kwd is greater than 2000"),
         ("Output, true", "Edit Fields: Supervisor review", "Sets status Supervisor review and reviewer Faisal"), ("Output, false", "Edit Fields: Approved", "Sets status Approved")])

# no connectors on Day 2 (Aya, 15 Nov 22:45: the trainees cannot use MCP connectors on their work accounts).
# Scheduled tasks run the skill on a reference file stored inside the skill; output and the run-log line live in the run on the Scheduled page.
ADD_TO_SKILL = ("Add the attached file to my [skill name] skill as a reference file. Keep every rule word for word. "
                "Then update the skill so I can save it again.")
SKILL_SCHED = ("Use the [skill name] skill on its reference file [file name]. Build the output in its fixed layout. Start with one line: "
               "date and time of this run, file read, items flagged. Mark it DRAFT and end with Reviewed by: ____. "
               "If the reference file is missing or cannot be read, say so in that first line and stop. Never guess.")
INVOICE_SKILL_SCHED = ("Use the mirqab-invoice-match skill on its reference files abdali-supplier-invoices-oct-2026.pdf and abdali-purchase-ledger-oct-2026.xlsx. "
                       "Return the match table in the template's columns. Start with one line: date and time of this run, files read, items flagged. "
                       "Mark it DRAFT and end with Reviewed by: ____. If a file is missing or cannot be read, say so in that first line and stop. Never guess.")
DEMOS["e23"].update(files=[F_INV, F_LEDGER],
 setup=["[T] In Claude, click New chat. Attach the October invoices and ledger. Send Add the files to the skill, then save the skill again.",
        "[T] Click Scheduled in the left sidebar, then New task, then Set up manually. If the form has no time field for Daily, use Create with Claude and say the time.",
        "[T] Name, the Scheduled task prompt, frequency daily at 08:00. Save. Run it once on demand.",
        "[T] Open the run on the Scheduled page: the first line, then the table."],
 prompts=[("Add the files to the skill", "Add the two attached files to my mirqab-invoice-match skill as reference files. Keep every rule word for word. Then update the skill so I can save it again."),
          ("Scheduled task prompt", INVOICE_SKILL_SCHED)],
 expected="The task shows on the Scheduled page, daily at 08:00. The run on demand starts with one line (date and time, 2 files read, 2 flagged: SCC-0718, FSC-3390), then the match table, marked DRAFT with a Reviewed by line.",
 backup=[("h", "The fields"), tbl(["Field", "Value"], [("Name", "Mirqab invoice match, daily"), ("Prompt", "Calls mirqab-invoice-match on its two reference files; first line is the run log; DRAFT and Reviewed by"),
         ("Frequency", "Daily at 08:00 (Kuwait works Sunday to Thursday)"), ("Connectors", "None: the files live in the skill")]),
         ("h", "The first line of the run"), ("p", "2026-11-16 11:05 · files read: 2 · flagged: 2 (SCC-0718, FSC-3390)")],
 fallback="If the skill does not save with the files, run the scheduled prompt in a chat with the two files attached, and show the backup first line.",
 hint="Read the first line of the run: when, what it read, what it flagged.")
DEMOS["u25"].update(
 setup=["New chat: attach your Task 2.1 test file (or your pack file). Send Add my file to the skill (prompt sheet, Task 2.5). Save the skill again.",
        "Click Scheduled in the left sidebar, then New task, then Set up manually.",
        "Name it. Paste the Scheduled task prompt (prompt sheet, Task 2.5) and fill the brackets.",
        "Frequency: weekly, Sunday at 08:00. Save. Run it once on demand.",
        "Open the run on the Scheduled page: the first line, then your output."],
 prompts=[("Add my file to the skill", ADD_TO_SKILL), ("Scheduled task prompt", SKILL_SCHED)],
 expected="A weekly task on the Scheduled page; one run on demand that starts with a run-log line, returns the skill's fixed output from the file inside the skill, and is marked DRAFT. No connectors used.",
 backup=[("h", "Why the file lives in the skill today"), ("p", "Connectors are off on these accounts. The skill carries a sample file, so the schedule can run with no other app. At work, new files would come through a connector RSM approves, or through an automation tool such as n8n or Power Automate.")],
 answer=[("h", "Check"), ("ul", ["The task is on the Scheduled page, weekly.", "The run on demand starts with one line: date and time, file read, items flagged.", "The output has the skill's fixed shape, DRAFT and a Reviewed by line.", "No connector was used."])],
 fallback="If the form has no time field, use Create with Claude and say the time. If the skill will not save with the file, run the scheduled prompt in a chat with the file attached.",
 hint="If the run says the file is missing, the file is not inside the skill yet.",
 stretch=["Add a rule to the prompt: list the two items that need the reviewer first."])
DEMOS["u26"]["setup"] = [x.replace("When (15 min): a scheduled task, run once on demand, with a run log.", "When (15 min): the file inside your skill, then a scheduled task run once on demand.") for x in DEMOS["u26"]["setup"]]
PROJECT_CARD = PROJECT_CARD.replace("Input: [the file it reads, and where it lives]", "Input: [the file it reads; today it lives inside the skill]")
DEMOS["u26"]["templates"] = [("Project card", PROJECT_CARD) if l == "Project card" else (l, t) for l, t in DEMOS["u26"]["templates"]]

# n8n is a video only (Aya, 16 Nov 06:09: no flow built from scratch in class). The sheet keeps one prompt: plan your own workflow, build nothing.
PLAN_FLOW = ("Here is a task from my department that starts with an event: [the task]. Describe it as an automation for n8n or Power Automate: "
             "the trigger, each step in order, and the output. Mark the one step where Claude would read or write. Do not build anything.")
DEMOS["e24"].update(
 setup=["[T] Click the video file on the slide: 100 seconds, captioned, no sound. Talk over it.",
        "[T] Name each part as it appears: the trigger, the Code step, the If step, the two outputs.",
        "[T] Pause on the If step: 3 invoices on the true branch, 2 on the false branch."],
 prompts=[("Plan my workflow (after the video, no build)", PLAN_FLOW)],
 expected=("In the video every node turns green. The trigger starts it, the Code step returns 5 invoices, and the If step sends 3 to Supervisor review "
           "(over KWD 2,000: BPK-4471, WDS-20931, SGT-11205) and 2 to Approved (SCC-0718, FSC-3390)."),
 fallback="If the video does not play from the slide, download it from step 6 of the Day 2 lab page, or step through the backup table.")

# the mini project gets its own page (Aya, 16 Nov 09:32): pick a department, get the scenario, the file, a Project card and every prompt.
# Built by kit/project_page.py from gen_files.py; short link /project.
F_PROJECT_PAGE = "coded-rsm-ai-automation-mini-project.html"
ALL_FILES = ALL_FILES + [F_PROJECT_PAGE]
DEMOS["u26"]["setup"] = ["Card (10 min): open coded-rsm.vercel.app/project, pick your department and copy its Project card."] + DEMOS["u26"]["setup"][1:]

# the project's thinking prompts sit behind hints on the project page (Aya, 16 Nov 10:02), so the Task 2.6 slide and the prompt sheet
# carry only the steps to follow and the blank Project card
DEMOS["u26"]["prompts"] = [("Add my file to the skill", ADD_TO_SKILL), ("Scheduled task prompt", SKILL_SCHED)]
DEMOS["u26"]["templates"] = [("Project card", PROJECT_CARD)]
DEMOS["u26"]["hint"] = "Write your own requests first. Stuck? The project page has a hint, another hint, then the prompt."
