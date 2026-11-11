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
BLOCK = {1: (1, "Opener"), 2: (1, "Lesson 1 · AI foundations"), 3: (1, "Lesson 2 · Why chat isn't enough"), 4: (1, "Lesson 3 · Design the agent"),
         5: (1, "Lesson 4 · Build: Instruction"), 6: (1, "Lesson 5 · Build: Input and Output"), 7: (1, "Lesson 6 · Build: Package"), 8: (1, "Lesson 7 · Show and tell"),
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
demo("d10", day=1, skill="1.0", sec=1, title="One invoice, two requests", tool="Claude", files=[F_INV], kind="showcase",
 setup=["[T] Open claude.ai in two windows. Upload abdali-supplier-invoices-oct-2026.pdf to both.", "[T] Type the weak request in one window and the five-part request in the other. Ask about invoice BPK-4471 (page 1)."],
 prompts=[("Weak", "What's in this?"), ("Strong", joined(OPENER_PARTS) + " Use invoice BPK-4471 on page 1.")],
 expected=f"Weak: a readable paragraph about packaging that gives a rounded amount and no invoice number. Strong: one row: {D.OPENER_INV[1]}, {D.OPENER_INV[0]}, 12 October 2026, PO number Not found, KWD {num(D.OPENER_INV[4])}.",
 say="Same tool. Same invoice. The only thing that changed is the request.",
 point="The request decides the result. You still check it.",
 backup=[("h", "Weak request: typical result"), ("p", "“This is an invoice from Bayan Packaging for cartons and shrink film, dated in October, for about 2,100 dinars. It looks like a standard packaging purchase.”"),
         ("h", "Five-part request: typical result"), tbl(["Supplier", "Invoice no.", "Date", "PO no.", "Amount (KWD)"], [(D.OPENER_INV[1], D.OPENER_INV[0], "2026-10-12", "Not found", num(D.OPENER_INV[4]))])],
 fallback="Play the opener slide step by step.",
 hint="Which answer could go into a working paper today?")

demo("d11", day=1, skill="1.1", sec=2, title="Where it goes wrong", tool="Claude", files=[F_INV, F_LEDGER, F_LETTER], kind="player",
 setup=["[T] Upload the invoices and the ledger to one chat.", "Ask for every invoice and its amount in one short line. Compare one row with page 2 of the invoices.",
        "[T] Then attach abdali-engagement-letter-2026.docx and ask when the client must sign and return it. Check the answer against the letter."],
 prompts=[("A short request", "List each invoice in the attached files and its amount."), ("A date to check", "By what date must the client sign and return the attached engagement letter? Quote the sentence.")],
 expected=f"Most rows are right. In the typical wrong run, {D.AI_WRONG[0]} shows KWD {num(D.AI_WRONG[1])} (the amount of the other Wafra line, WDS-20988) instead of KWD {num(D.INV[D.AI_WRONG[0]][4])} (the invoice).",
 say="It reads well and it is wrong in one place. Only the source tells you which place.",
 point="Tick every figure against the source, as you would a junior's working paper.",
 backup=[("h", "A typical wrong answer"), tbl(["Invoice", "AI answer (KWD)", "The invoice says (KWD)"], [(r[0], num(D.AI_WRONG[1] if r[0] == D.AI_WRONG[0] else r[4]), num(r[4])) for r in D.INVOICES])],
 fallback=f"Show the backup table: the wrong row is {D.AI_WRONG[0]}.",
 hint=f"Open page 2 of the invoice pack and compare it with the {D.AI_WRONG[0]} row.",
 player={"parts": [["Task", "List each invoice in the attached files and its amount."]],
         "table": [["Invoice", "AI answer (KWD)", "The invoice says (KWD)"]] + [[r[0], num(D.AI_WRONG[1] if r[0] == D.AI_WRONG[0] else r[4]), num(r[4])] for r in D.INVOICES], "best": 2,
         "reco": [f"<b>Four rows are right.</b> One is not: {D.AI_WRONG[0]}.", f"<b>Why:</b> the ledger has two Wafra lines; the AI took the other one's {num(D.AI_WRONG[1])}, not the invoice.", "<b>The habit:</b> tick each figure against the source document."],
         "control": "Tick every figure against the source before it goes into a working paper."})

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

demo("t12", day=1, skill="1.2", sec=3, title="Same task, 18 answers", tool="Claude chat", files=[F_INV, F_LEDGER], kind="task", hands_on=True, minutes=18, solo="on your own, then in pairs",
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

demo("t13", day=1, skill="1.3", sec=3, title="Your task inventory", tool="The Day 1 lab page", files=[], kind="task", hands_on=True, minutes=12, solo="on your own",
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

demo("d14", day=1, skill="1.3", sec=4, title="From card to agent", tool="Claude Projects", files=[F_TEMPLATE], kind="player",
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

demo("t14", day=1, skill="1.4", sec=4, title="Build the invoice agent with me", tool="Claude Projects", files=[F_INV, F_LEDGER, F_TEMPLATE], kind="task", hands_on=True, minutes=20, solo="on your own, with the trainer",
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

demo("d15", day=1, skill="1.4", sec=4, title="Dana scores her three candidates", tool="Claude", files=[], kind="player",
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

demo("t15", day=1, skill="1.5", sec=4, title="Write your Agent Card v1", tool="The Day 1 lab page", files=[], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=["Score your 3 candidates on the four points (5 min).", "Pick one and place it in a track: Extraction, Analysis, Workflow or Reporting (2 min).",
        "Write your Agent Card on the Day 1 lab page: Input, Instruction, Output. Leave When empty (8 min).", "Paste the card on the shared board for approval (5 min)."],
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
        "Use the transfer map. Add one line to your Agent Card: where this skill would live in ChatGPT, Copilot or Gemini."],
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
 setup=["Agree on your team's agent (the board vote).", "Fill the workflow card on the Day 2 lab page: When, Input, Skill, Output, Who reviews.", "Post it on the shared board."],
 prompts=[("Check our card", "Here is our workflow card: [paste it]. Ask us three questions about what could go wrong when it runs without us.")],
 expected="One card per team with a time, a folder, a skill, a named output and a named reviewer.",
 say="Fill all five boxes. A blank box is a risk.",
 point="A workflow is a card with a When.",
 backup=[("h", "Example card"), tbl(["Box", "Invoice workflow"], [("When", "Daily at 08:00"), ("Input", "01 Invoices / Inbox"), ("Skill", "mirqab-invoice-match"), ("Output", "A named file and a run-log file"), ("Who reviews", "Faisal")])],
 answer=[("h", "A complete card has"), ("ul", ["A time or a day for When.", "One folder for Input.", "The skill name from Day 1.", "A file name pattern and a run-log file.", "A named reviewer."])],
 deliverable="Your team's workflow card on the shared board.",
 fallback="A team whose agent is not ready takes the invoice workflow: one member turns the Task 1.4 Project into a skill first.",
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

# ===================================================================== the opener (Day 1)
SHOWCASE = {
 "eyebrow": "Opener · one invoice", "title": "Same tool. Same invoice. <span class=\"hl\">Two requests.</span>", "tool": "Claude", "file": F_INV,
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
