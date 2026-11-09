# -*- coding: utf-8 -*-
"""Every fictional name and number of the RSM workshop, in one place. Slides, files, prompts, answers and MAP items read them here.
Mirqab & Co. and Abdali Foods are fictional: never a real client, never RSM's own data."""

FIRM = "Mirqab & Co."
FIRM_LONG = "Mirqab & Co., Auditors and Advisors"
CO = "Abdali Foods Co. K.S.C.C."
CO_SHORT = "Abdali Foods"
FICTION = "Fictional training file. Mirqab & Co., Abdali Foods and every name, amount and date here are made up for CODED training."
DANA, FAISAL, NOURA = "Dana", "Faisal", "Noura"          # associate, supervisor, project coordinator (all fictional)
OTHER_CLIENTS = ["Khiran Logistics Co. W.L.L.", "Jabriya Medical Supplies Co. W.L.L."]

def kwd(v): return f"KWD {v:,.3f}"
def num(v): return f"{v:,.3f}"

# ------------------------------------------------------------------ the anchor: five October supplier invoices and the purchase ledger
# (invoice no, supplier, invoice date, PO, amount KWD, description)
INVOICES = [
    ("BPK-4471", "Bayan Packaging Co. W.L.L.", "2026-10-12", "", 2145.750, "Cartons and shrink film"),
    ("WDS-20931", "Wafra Dairy Supplies Co.", "2026-10-14", "PO-2211", 3860.000, "Milk powder, 40 bags"),
    ("SCC-0718", "Shuwaikh Cold Store Co.", "2026-10-18", "PO-2219", 1248.500, "Cold storage, October"),
    ("SGT-11205", "Sulaibiya Grain Traders Co.", "2026-10-21", "PO-2224", 5312.250, "Wheat flour, 9 tonnes"),
    ("FSC-3390", "Fintas Spice Co.", "2026-10-27", "PO-2230", 742.125, "Spice blends"),
]
INV = {r[0]: r for r in INVOICES}
OPENER_INV = INVOICES[0]                     # Demo 1.0: no PO number on it
WRONG_INV, WRONG_LEDGER = "SCC-0718", 1284.500  # posted at 1,284.500 (digits swapped)
WRONG_DIFF = round(WRONG_LEDGER - INV[WRONG_INV][4], 3)   # 36.000
CUTOFF_INV, CUTOFF_POSTED = "FSC-3390", "2026-11-03"     # dated 27 October, posted in November
# October purchase ledger: (posting date, voucher, supplier, invoice no, invoice date, amount KWD, account)
LEDGER = [
    ("2026-10-02", "PV-10411", "Kuwait Gas Cylinders Co.", "KGC-7712", "2026-09-30", 318.000, "Utilities"),
    ("2026-10-05", "PV-10418", "Bayan Packaging Co. W.L.L.", "BPK-4402", "2026-10-01", 1980.250, "Packaging"),
    ("2026-10-08", "PV-10425", "Shamiya Cleaning Services", "SCS-0566", "2026-10-06", 410.000, "Cleaning"),
    ("2026-10-13", "PV-10433", "Bayan Packaging Co. W.L.L.", "BPK-4471", "2026-10-12", 2145.750, "Packaging"),
    ("2026-10-15", "PV-10440", "Wafra Dairy Supplies Co.", "WDS-20931", "2026-10-14", 3860.000, "Raw materials"),
    ("2026-10-16", "PV-10446", "Qurtuba Print House", "QPH-1189", "2026-10-15", 655.500, "Printing"),
    ("2026-10-19", "PV-10452", "Shuwaikh Cold Store Co.", "SCC-0718", "2026-10-18", WRONG_LEDGER, "Storage"),
    ("2026-10-20", "PV-10457", "Ardiya Pallet Co.", "APC-2290", "2026-10-19", 1120.000, "Packaging"),
    ("2026-10-22", "PV-10463", "Sulaibiya Grain Traders Co.", "SGT-11205", "2026-10-21", 5312.250, "Raw materials"),
    ("2026-10-26", "PV-10471", "Wafra Dairy Supplies Co.", "WDS-20988", "2026-10-25", 2240.000, "Raw materials"),
    ("2026-10-28", "PV-10478", "Rai Workshop Tools", "RWT-0431", "2026-10-27", 287.750, "Repairs"),
    ("2026-10-29", "PV-10482", "Shuwaikh Cold Store Co.", "SCC-0702", "2026-10-03", 1248.500, "Storage"),
]
LEDGER_BY_INV = {r[3]: r for r in LEDGER}
def match_rows():
    """The right answer of the invoice match, row by row: (inv, supplier, date, invoice amt, ledger amt or None, diff or None, status, note)."""
    out = []
    for no, sup, dt, _po, amt, _d in INVOICES:
        l = LEDGER_BY_INV.get(no)
        if not l:
            out.append((no, sup, dt, amt, None, None, "Not in ledger", "Not in the October ledger: check cut-off."))
        elif abs(l[5] - amt) > 0.0005:
            out.append((no, sup, dt, amt, l[5], round(l[5] - amt, 3), "Amount differs", "Ledger is KWD 36.000 higher. Digits look swapped."))
        else:
            out.append((no, sup, dt, amt, l[5], 0.0, "Matched", "" if _po else "No PO number on the invoice."))
    return out
MATCH = match_rows()
MATCHED = [r[0] for r in MATCH if r[6] == "Matched"]
TEMPLATE_HEAD = ["Invoice no.", "Supplier", "Invoice date", "PO no.", "Invoice amount (KWD)", "Ledger amount (KWD)", "Difference (KWD)", "Status", "Note"]
TEMPLATE_EXAMPLE = ["EX-0001", "Example Supplier W.L.L.", "2026-09-30", "PO-0000", "1,000.000", "1,000.000", "0.000", "Matched", "Example row: delete it"]
STATUSES = ["Matched", "Amount differs", "Not in ledger", "Not found"]

# what a weak chat answer typically gets wrong (Demo 1.1 and the Task 1.2 debrief)
AI_WRONG = ("WDS-20931", 2240.000)           # Demo 1.1: the AI took the amount of the other Wafra line (WDS-20988), not a Task 1.2 problem

# ------------------------------------------------------------------ Task 1.1: the engagement letter (planted: no section on management's responsibilities)
LETTER_DATE = "7 September 2026"
LETTER = {"sign_by": "30 September 2026", "interim": "16 November to 3 December 2026", "year_end_work": "1 to 25 February 2027",
          "report": "31 March 2027", "fee": 18500.000, "fy_end": "31 December 2026"}
LETTER_SECTIONS = ["Objective and scope of the audit", "Our responsibilities", "The financial reporting framework", "Form and content of our report",
                   "Timetable", "Fees and billing", "Access to people and records", "Agreement of terms"]
LETTER_MISSING = "Responsibilities of management (for the financial statements, internal control and giving the auditor access)"

# ------------------------------------------------------------------ track packs
# Extraction: six leases. (no, premises, lessor, start, end, monthly rent, deposit, special clause or "")
LEASES = [
    (1, "Warehouse, Shuwaikh Industrial", "Mutlaq Real Estate Co.", "2024-01-01", "2028-12-31", 4200.000, 8400.000, "Option to renew for 3 years."),
    (2, "Outlet, Salmiya", "Hamra Properties Co.", "2025-03-01", "2028-02-29", 1850.000, 3700.000, ""),
    (3, "Outlet, Jahra", "Qasr Real Estate Co.", "2023-07-01", "2027-06-30", 1300.000, 2600.000, ""),
    (4, "Outlet, Fahaheel", "Dhaher Investment Co.", "2026-04-01", "2029-03-31", 1580.000, 3160.000, "No rent for the first 3 months (1 April to 30 June 2026)."),
    (5, "Head office, Sharq", "Burj Sharq Real Estate Co.", "2022-01-01", "2026-12-31", 2950.000, 5900.000, ""),
    (6, "Cold room, Sabhan", "Sabhan Storage Co.", "2025-09-01", "2028-08-31", 2400.000, 4800.000, "The landlord may end the lease early with 60 days' written notice."),
]
UNUSUAL = {4: "Rent-free period: no rent for the first 3 months", 6: "Landlord may end the lease with 60 days' notice"}
LEASE_HEAD = ["Lease", "Premises", "Lessor", "Start", "End", "Monthly rent (KWD)", "Deposit (KWD)", "Special terms"]

# Analysis: two-year trial balance. (account, group, FY2024, FY2025). Threshold: change over 10% AND over KWD 5,000.
THRESH_PCT, THRESH_AMT = 10, 5000
TB = [
    ("Cash at bank", "Assets", 186400, 201700), ("Trade receivables", "Assets", 412300, 486900), ("Allowance for doubtful debts", "Assets", -18600, -19900),
    ("Inventories", "Assets", 298450, 301200), ("Prepayments", "Assets", 22800, 24100), ("Property, plant and equipment", "Assets", 1240000, 1196500),
    ("Right-of-use assets", "Assets", 402300, 381000), ("Trade payables", "Liabilities", -356200, -371400), ("Accrued expenses", "Liabilities", -64800, -12300),
    ("Other payables", "Liabilities", -18200, -71900), ("Lease liabilities", "Liabilities", -398900, -377800), ("Staff indemnity", "Liabilities", -142600, -149300),
    ("Share capital", "Equity", -1000000, -1000000), ("Retained earnings (opening)", "Equity", -193850, -207800), ("Revenue", "Income", -3850000, -4120000),
    ("Other income", "Income", -12400, -12900), ("Cost of sales", "Expenses", 2695000, 2904000), ("Staff costs", "Expenses", 540000, 566500),
    ("Marketing", "Expenses", 48000, 52100), ("Utilities", "Expenses", 36500, 39900), ("Repairs and maintenance", "Expenses", 22400, 35900),
    ("Bank charges", "Expenses", 4100, 6000), ("Depreciation", "Expenses", 126300, 128100), ("Finance costs on leases", "Expenses", 21000, 19400),
]
def movements():
    out = []
    for a, g, p, c in TB:
        d = c - p; pct = (abs(d) / abs(p) * 100) if p else 0
        out.append((a, g, p, c, d, pct, abs(d) > THRESH_AMT and pct > THRESH_PCT))
    return out
MOVES = movements()
OVER = [m[0] for m in MOVES if m[6]]                      # Trade receivables, Accrued expenses, Other payables, Repairs and maintenance
RECLASS = ("Accrued expenses", "Other payables")          # the two move together: ask the client if it is a reclassification
PCT_ONLY = "Bank charges"                                 # over 10% but under KWD 5,000: not flagged

# Workflow: the request list (PBC) for the Abdali Foods interim audit. (no, item, due, status after the emails, note)
PBC = [
    (1, "Trial balance at 31 October 2026", "2026-11-12", "Received", ""),
    (2, "Bank statements and bank reconciliations, October 2026", "2026-11-12", "Received", ""),
    (3, "Fixed asset register with additions for 2026", "2026-11-15", "Received", ""),
    (4, "Purchase ledger, October 2026", "2026-11-12", "Received", ""),
    (5, "Sales listing, October 2026", "2026-11-12", "Partly received", "The email sent September, not October"),
    (6, "Payroll summary, January to October 2026", "2026-11-15", "Received", ""),
    (7, "Lease agreements signed in 2026", "2026-11-15", "Partly received", "The email says attached, but nothing was attached"),
    (8, "Board minutes, 2026", "2026-11-19", "Outstanding", ""),
    (9, "Inventory count plan for 31 December 2026", "2026-11-19", "Received", ""),
    (10, "Aged receivables at 31 October 2026", "2026-11-12", "Received", ""),
    (11, "Legal letters and open claims", "2026-11-22", "Outstanding", ""),
    (12, "Related-party transactions list", "2026-11-22", "Outstanding", ""),
    (13, "Loan agreements and bank confirmations", "2026-11-19", "Partly received", "The agreements came; the bank confirmations come later, from the banks"),
    (14, "Management accounts, October 2026", "2026-11-15", "Outstanding", ""),
    (15, "Tax and Zakat assessments", "2026-11-26", "Outstanding", ""),
]
PBC_COUNTS = {s: sum(1 for r in PBC if r[3] == s) for s in ("Received", "Partly received", "Outstanding")}   # 7 / 3 / 5
# the 10 client emails (from Abdali Foods' finance team). (date, from, subject, body, items covered)
EMAILS = [
    ("2026-11-09", "Hessa, Finance Manager", "Trial balance and bank", "Dear Mirqab team, please find attached the trial balance at 31 October and the October bank statements with reconciliations.", [1, 2]),
    ("2026-11-09", "Hessa, Finance Manager", "Purchase ledger", "Attached is the purchase ledger for October 2026.", [4]),
    ("2026-11-10", "Bader, Accountant", "Sales listing", "Here is the sales listing you asked for. File: sales-listing-sep-2026.xlsx", [5]),
    ("2026-11-10", "Bader, Accountant", "Fixed assets", "Attached: the fixed asset register with all 2026 additions.", [3]),
    ("2026-11-10", "Hessa, Finance Manager", "Payroll", "Payroll summary January to October attached.", [6]),
    ("2026-11-11", "Bader, Accountant", "Leases", "Please find attached the lease agreements we signed this year.", [7]),
    ("2026-11-11", "Hessa, Finance Manager", "Count plan", "Our inventory count plan for 31 December is attached.", [9]),
    ("2026-11-11", "Bader, Accountant", "Receivables", "Attached is the aged receivables report at 31 October.", [10]),
    ("2026-11-12", "Hessa, Finance Manager", "Loans", "Attached are the loan agreements. We asked both banks to send confirmations to you directly.", [13]),
    ("2026-11-12", "Hessa, Finance Manager", "Board minutes", "The board minutes need the chairman's approval. We expect to send them next week.", []),
]
EMAIL_ATTACH = {1: ["tb-31-oct-2026.xlsx", "bank-oct-2026.pdf"], 2: ["purchase-ledger-oct-2026.xlsx"], 3: ["sales-listing-sep-2026.xlsx"], 4: ["fa-register-2026.xlsx"],
                5: ["payroll-jan-oct-2026.xlsx"], 6: [], 7: ["count-plan-2026.pdf"], 8: ["aged-ar-31-oct-2026.xlsx"], 9: ["loans-2026.pdf"], 10: []}
OUTSTANDING = [r[1] for r in PBC if r[3] == "Outstanding"]

# Reporting: weekly status, week 46 (8 to 12 November 2026). (engagement, type, budget h, used h, open items, next deadline, note)
STATUS46 = [
    ("Abdali Foods Co. K.S.C.C.", "Interim audit, FY2026", 420, 248, 6, "Interim fieldwork starts 16 Nov", "Request list 47% received"),
    ("Khiran Logistics Co. W.L.L.", "Year-end audit, FY to 30 Sep 2026", 380, 448, 9, "Draft report to client 26 Nov", "Inventory testing took longer"),
    ("Jabriya Medical Supplies Co. W.L.L.", "Agreed-upon procedures", 120, 64, 2, "Report due 19 Nov", "On track"),
]
def over_pct(b, u): return round((u - b) / b * 100)
OVER_BUDGET = [(r[0], over_pct(r[2], r[3])) for r in STATUS46 if r[3] > r[2]]   # Khiran 18%

# ------------------------------------------------------------------ Task 1.10: the messy samples (the agent must flag, not guess)
MESSY = {
    "invoice": ("A supplier invoice in USD with no invoice number", "Gulf Trade Imports FZE, 29 October 2026, USD 2,300.00, no invoice number",
                "Flag: no invoice number, and the amount is in USD. Do not convert it."),
    "lease": ("A lease with no end date", "Lease 7, Outlet, Abu Halifa: start 1 June 2026, monthly KWD 1,320.000, end date: until further notice",
              "Flag: no end date. Ask for the term before you schedule it."),
    "tb": ("A trial balance with one prior-year figure missing", "Repairs and maintenance: FY2025 KWD 35,900, FY2024 blank",
           "Flag: the movement cannot be calculated. Do not treat the blank as zero."),
    "email": ("An email that answers two requests in one line", "Board minutes and legal letters: we will send both next week.",
              "Mark both items Outstanding with the client's promised date, and add one follow-up for each."),
    "status": ("A status sheet with a blank budget", "Jabriya Medical Supplies: hours used 64, budget blank",
               "Flag: the budget is blank, so over or under budget cannot be calculated."),
}

# ------------------------------------------------------------------ Day 2: batch 2 (new inputs) and the department rules
INVOICES_B2 = [
    ("WDS-21077", "Wafra Dairy Supplies Co.", "2026-11-02", "PO-2241", 2980.000, "KWD", "Milk powder, 31 bags"),
    ("BPK-4518", "Bayan Packaging Co. W.L.L.", "2026-11-03", "PO-2243", 1615.250, "KWD", "Cartons"),
    ("GTI-0091", "Gulf Trade Imports FZE", "2026-11-04", "PO-2246", 3150.000, "USD", "Vacuum sealer parts"),
]
LEDGER_B2 = [
    ("2026-11-03", "PV-11002", "Fintas Spice Co.", "FSC-3390", "2026-10-27", 742.125, "Raw materials"),
    ("2026-11-03", "PV-11004", "Wafra Dairy Supplies Co.", "WDS-21077", "2026-11-02", 2980.000, "Raw materials"),
    ("2026-11-04", "PV-11009", "Bayan Packaging Co. W.L.L.", "BPK-4518", "2026-11-03", 1615.250, "Packaging"),
    ("2026-11-05", "PV-11013", "Gulf Trade Imports FZE", "GTI-0091", "2026-11-04", 966.000, "Repairs"),
]
B2_FLAG = "GTI-0091"           # in USD: flag it, never convert
B2_MATCHED = ["WDS-21077", "BPK-4518"]
NEW_LEASE = (8, "Outlet, Mahboula", "Funaitees Real Estate Co.", "2026-11-01", "2029-10-31", 1450.000, 2900.000, "Rent rises by 5% from the second year.")
MGMT = [("Revenue", 352400, 371900), ("Cost of sales", 246700, 262100), ("Staff costs", 47100, 47600), ("Marketing", 3900, 9800),
        ("Utilities", 3200, 3350), ("Repairs and maintenance", 2600, 2750), ("Bank charges", 480, 520)]   # September, October (KWD)
MGMT_FLAG = "Marketing"        # month on month: +151%, +KWD 5,900
EMAILS_B2 = [
    ("2026-11-15", "Hessa, Finance Manager", "Sales listing (October)", "Sorry for the mix-up. Attached is the October sales listing.", [5]),
    ("2026-11-15", "Bader, Accountant", "Leases again", "Now attached: the three lease agreements signed in 2026 (Fahaheel, Abu Halifa and Mahboula).", [7]),
    ("2026-11-16", "Hessa, Finance Manager", "Management accounts", "October management accounts attached.", [14]),
    ("2026-11-16", "Bader, Accountant", "Tax", "The tax and Zakat assessments will come from our tax adviser by 30 November.", []),
    ("2026-11-16", "Hessa, Finance Manager", "Related parties", "We are preparing the related-party list. Please give us one more week.", []),
]
STATUS47 = [
    ("Abdali Foods Co. K.S.C.C.", "Interim audit, FY2026", 420, 291, 4, "Interim fieldwork ends 3 Dec", "Request list 67% received"),
    ("Khiran Logistics Co. W.L.L.", "Year-end audit, FY to 30 Sep 2026", 380, 471, 5, "Draft report to client 26 Nov", "Partner review booked 24 Nov"),
    ("Jabriya Medical Supplies Co. W.L.L.", "Agreed-upon procedures", 120, 96, 0, "Report sent 16 Nov", "Closed"),
]
RULES = [
    ("Assurance", ["A difference over KWD 100 goes to the supervisor for review.", "Never post or propose an adjustment: flag it with the evidence.",
                   "Amounts in another currency are flagged, never converted."]),
    ("Corporate Finance", ["Every figure in a summary shows its source file and cell.", "Projections are labeled draft until a senior associate reviews them."]),
    ("Support", ["Follow-ups to clients are drafts only. A person reads and sends them.", "Use the client's name and the request number in every follow-up."]),
    ("Analytics Advisory", ["Every chart or table names its period and its source.", "Movements are flagged on both rules: over 10% and over KWD 5,000."]),
    ("All departments", ["Outputs are named client-task-YYYY-MM-DD-HHMM.", "Each run saves one run-log file in Log: date, files read, items flagged, file saved.",
                         "If there are no new files: write No new files in the run log and stop."]),
]
REVIEW_LIMIT = 100.000

# ------------------------------------------------------------------ Day 2 impact (Lesson 5, MAP Q9 shape)
IMPACT_EX = {"by_hand": 40, "agent": 5, "runs": 20}          # minutes, minutes, runs a month
def impact(by_hand, agent, runs): return (by_hand - agent) * runs
IMPACT_MIN = impact(**IMPACT_EX)                              # 700 minutes, about 12 hours
INVOICE_IMPACT = {"by_hand": 45, "agent": 6, "runs": 22}      # the trainer's invoice workflow: 858 minutes, about 14 hours

# ------------------------------------------------------------------ the trainer's scheduled demo (Day 1 Lesson 7)
SCHED_TIME = "15:55"
SANDBOX = "Mirqab sandbox"
FOLDERS = ["01 Invoices", "02 Leases", "03 Trial balance", "04 Requests", "05 Status"]
