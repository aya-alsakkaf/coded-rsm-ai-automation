# -*- coding: utf-8 -*-
"""Day 2 rebuild (Aya, 15 Nov night): the artifact demo file and one department pack per RSM service line.
Every row is fictional (Mirqab & Co. and made-up clients). Each pack hides two problems a good agent must flag.
gen_files.py writes the files; content_demos.py and content.py read the facts here, so the decks, labs and answer keys agree."""
import datetime as dt
import random

FICTION = "Fictional training file. Mirqab & Co., its clients and every name, amount and date here are made up for CODED training."
TODAY = dt.date(2026, 11, 16)
CLIENTS = ["Shuwaikh Steel Works", "Fintas Marine Services", "Salmiya Retail Group", "Mishref Education Co.", "Ardiya Plastics", "Hawally Pharma Distribution",
           "Rai Auto Parts", "Sulaibiya Cold Stores", "Jahra Building Materials", "Farwaniya Textiles", "Surra Dental Centers", "Yarmouk Bakeries",
           "Qadsiya Printing", "Shamiya Furniture", "Rumaithiya Travel", "Kaifan Engineering", "Adailiya Catering", "Egaila Fitness Clubs",
           "Abdali Foods", "Khiran Logistics", "Jabriya Medical Supplies", "Sabhan Cables", "Shuwaikh Port Services", "Salmiya Hotels"]

def d(s): return dt.date.fromisoformat(s)
def iso(x): return x.isoformat()

# ===================================================================== the artifact demo file (Lesson 2): Mirqab's engagement portfolio
F_PORTFOLIO = "mirqab-engagement-portfolio-2026.xlsx"
PORT_HEAD = ["Engagement", "Client", "Service line", "Partner", "Manager", "Budget hours", "Actual hours", "Fee (KWD)", "Billed (KWD)", "Collected (KWD)", "Status", "Report due"]
_r = random.Random(1116)
_lines = ["Audit", "Audit", "Audit", "Tax", "Corporate Finance", "Risk Consulting", "Cybersecurity", "ESG"]
_partners = ["Yousef", "Maryam", "Khaled"]
_managers = ["Faisal", "Huda", "Tariq", "Noura"]
PORTFOLIO = []
for i in range(24):
    line = _lines[i % len(_lines)]
    budget = _r.choice([120, 160, 200, 240, 300, 360, 420])
    actual = int(budget * _r.choice([0.55, 0.7, 0.85, 0.95, 1.05, 1.12, 0.6, 0.9]))
    fee = float(budget * _r.choice([28, 32, 35, 40]))
    billed = float(round(fee * _r.choice([0.5, 0.6, 0.8, 1.0, 0.4, 0.7])))
    collected = float(round(billed * _r.choice([0.6, 0.8, 1.0, 0.5, 0.9])))
    due = TODAY + dt.timedelta(days=_r.choice([-12, -5, 9, 16, 30, 45, 60, 75, 90]))
    status = "Closed" if billed == fee and collected == billed else _r.choice(["On track", "On track", "At risk", "Delayed"])
    PORTFOLIO.append([f"E-2026-{i + 1:03d}", CLIENTS[i], line, _partners[i % 3], _managers[i % 4], budget, actual, fee, billed, collected, status, iso(due)])
# the two planted problems
PORTFOLIO[16][6] = None                                            # E-2026-017: Actual hours blank
PORTFOLIO[8][9] = PORTFOLIO[8][8] + 1250.0                         # E-2026-009: Collected is more than Billed
PORT_ISSUES = [f"{PORTFOLIO[16][0]}: Actual hours is blank. Flag it; never count it as zero.",
               f"{PORTFOLIO[8][0]}: Collected (KWD {PORTFOLIO[8][9]:,.3f}) is more than Billed (KWD {PORTFOLIO[8][8]:,.3f}). Flag it for the finance team."]
def _port_kpis():
    rows = PORTFOLIO
    fee = sum(r[7] for r in rows); billed = sum(r[8] for r in rows); coll = sum(r[9] for r in rows)
    over = [r[0] for r in rows if r[6] is not None and r[6] > r[5]]
    overdue = [r[0] for r in rows if d(r[11]) < TODAY and r[10] != "Closed"]
    hrs = [(r[5], r[6]) for r in rows if r[6] is not None]
    by_line = {}
    for r in rows: by_line[r[2]] = by_line.get(r[2], 0) + r[7]
    return {"engagements": len(rows), "fee": fee, "billed": billed, "collected": coll, "billed_pct": round(billed / fee * 100, 1),
            "collected_pct": round(coll / billed * 100, 1), "over_budget": over, "overdue": overdue,
            "hours_used_pct": round(sum(a for _b, a in hrs) / sum(b for b, _a in hrs) * 100, 1), "fee_by_line": by_line,
            "at_risk": [r[0] for r in rows if r[10] in ("At risk", "Delayed")]}
PORT_KPI = _port_kpis()

# ===================================================================== one department pack per RSM service line (Lessons 2 and 5)
PACKS = []
def pack(key, dept, file, sheet, head, rows, widths, problem, agent, artifact, schedule, issues, kpis):
    PACKS.append(dict(key=key, dept=dept, file=file, sheet=sheet, head=head, rows=rows, widths=widths, problem=problem,
                      agent=agent, artifact=artifact, schedule=schedule, issues=issues, kpis=kpis))

# 1 · Audit and Assurance: the findings log
r = random.Random(1)
AREAS = ["Revenue", "Inventory", "Payroll", "Fixed assets", "Cash and bank", "Procurement", "Related parties", "IT general controls"]
rows = []
for i in range(30):
    raised = TODAY - dt.timedelta(days=r.randint(5, 150))
    due = raised + dt.timedelta(days=r.choice([30, 45, 60, 90]))
    status = r.choice(["Open", "Open", "In progress", "Closed", "Closed"])
    rows.append([f"F-{i + 101}", r.choice(CLIENTS[:12]), r.choice(AREAS), r.choice(["High", "Medium", "Medium", "Low"]), r.choice(_managers), iso(raised), iso(due), status])
rows[11][4] = None                                                 # no owner
rows[22][6] = iso(d(rows[22][5]) - dt.timedelta(days=10))          # due before raised
_open = [x for x in rows if x[7] != "Closed"]
pack("audit", "Audit and Assurance", "mirqab-audit-findings-log-2026.xlsx", "Findings log",
     ["Finding", "Client", "Area", "Risk", "Owner", "Raised", "Due", "Status"], rows, [10, 28, 18, 9, 10, 12, 12, 12],
     "Partners ask every week which findings are still open, which are overdue and which high-risk ones need them.",
     "Reads the findings log and lists open, overdue and high-risk findings, with a follow-up line for each owner.",
     "A findings dashboard: open by risk, overdue count, by area and by owner.", "Every Sunday at 08:00, from the log in the team's Inbox.",
     [f"{rows[11][0]}: no owner. Flag it; do not assign one.", f"{rows[22][0]}: the due date is before the date it was raised. Flag it as a data error."],
     {"Findings": len(rows), "Not closed": len(_open), "High risk, not closed": sum(1 for x in _open if x[3] == "High"),
      "Overdue (due before 16 Nov 2026, not closed)": sum(1 for x in _open if d(x[6]) < TODAY)})

# 2 · Tax: the filing calendar
r = random.Random(2)
TYPES = ["Zakat return", "NLST return", "Corporate income tax return", "Retention release request", "Withholding statement"]
rows = []
for i in range(28):
    due = TODAY + dt.timedelta(days=r.randint(-20, 75))
    st = r.choice(["Not started", "In preparation", "In review", "Filed", "Filed"])
    rows.append([f"TX-{i + 301}", r.choice(CLIENTS), r.choice(TYPES), "FY2025", iso(due), st, r.choice(["Huda", "Tariq", "Faisal"]), r.choice(["Maryam", "Khaled"])])
rows[4][4] = iso(TODAY - dt.timedelta(days=9)); rows[4][5] = "Not started"     # past due, not started
rows[17][7] = None                                                              # no reviewer
_nf = [x for x in rows if x[5] != "Filed"]
pack("tax", "Tax", "mirqab-tax-filing-calendar-2026.xlsx", "Filing calendar",
     ["Filing", "Client", "Type", "Period", "Due date", "Status", "Preparer", "Reviewer"], rows, [10, 28, 28, 9, 12, 15, 11, 11],
     "The tax team keeps one calendar for every client filing. A missed date means a penalty for the client.",
     "Reads the calendar and lists filings due in the next 14 days, filings past due, and filings with no reviewer.",
     "A deadline dashboard: due this week, next 30 days, past due, and status by type.", "Every weekday at 08:00.",
     [f"{rows[4][0]}: past its due date and still Not started. Flag it first.", f"{rows[17][0]}: no reviewer. Flag it; do not pick one."],
     {"Filings": len(rows), "Not filed": len(_nf), "Past due, not filed": sum(1 for x in _nf if d(x[4]) < TODAY),
      "Due in the next 14 days, not filed": sum(1 for x in _nf if TODAY <= d(x[4]) <= TODAY + dt.timedelta(days=14))})

# 3 · Corporate Finance: the deal pipeline
r = random.Random(3)
rows = []
for i in range(22):
    stage = r.choice(["Lead", "Proposal", "Proposal", "Engaged", "Fieldwork", "Report"])
    prob = {"Lead": 20, "Proposal": 40, "Engaged": 70, "Fieldwork": 85, "Report": 95}[stage]
    close = TODAY + dt.timedelta(days=r.randint(10, 150))
    rows.append([f"CF-{i + 501}", r.choice(CLIENTS), r.choice(["Valuation", "Financial due diligence", "Buy-side advisory", "Feasibility study", "Business plan review"]),
                 r.choice(["Food", "Logistics", "Healthcare", "Retail", "Industrial", "Education"]), stage, float(r.choice([6000, 8500, 12000, 15000, 22000, 30000])), prob, iso(close), r.choice(_partners)])
rows[6][6] = None                                                   # probability blank
rows[13][4] = "Proposal"; rows[13][7] = iso(TODAY - dt.timedelta(days=21))      # close date in the past, still a proposal
_w = sum(x[5] * x[6] / 100 for x in rows if x[6] is not None)
pack("cf", "Corporate Finance", "mirqab-cf-deal-pipeline-2026.xlsx", "Deal pipeline",
     ["Deal", "Client", "Service", "Sector", "Stage", "Fee estimate (KWD)", "Probability (%)", "Expected close", "Lead partner"], rows, [9, 28, 24, 12, 11, 17, 15, 15, 13],
     "Partners review the pipeline every Monday, but the sheet has no totals, no weighted value and no view by stage.",
     "Reads the pipeline and returns the weighted value by stage, deals closing this month, and stale deals.",
     "A pipeline dashboard and a 5-slide partner update.", "Every Monday at 07:30.",
     [f"{rows[6][0]}: Probability is blank. Flag it; do not use a stage default.", f"{rows[13][0]}: the expected close date has passed and it is still a Proposal. Flag it as stale."],
     {"Deals": len(rows), "Total fee estimate (KWD)": f"{sum(x[5] for x in rows):,.3f}", "Weighted value (KWD), blank probability left out": f"{_w:,.3f}"})

# 4 · Risk Consulting: the risk register
r = random.Random(4)
RISKS = ["Key supplier failure", "Payroll fraud", "Data loss from a laptop", "Late financial close", "Regulatory change", "Key person leaves",
         "Price increase from suppliers", "System outage", "Inventory theft", "Customer credit default", "Fire at the warehouse", "Wrong tax filing",
         "Phishing email to finance", "Contract not renewed", "Project overrun", "Cash shortfall", "Weak segregation of duties", "Outdated policies"]
rows = []
for i, rk in enumerate(RISKS):
    L, I = r.randint(1, 5), r.randint(1, 5)
    rows.append([f"R-{i + 1:02d}", rk, r.choice(["Operational", "Financial", "Compliance", "Technology", "Strategic"]), L, I, L * I,
                 r.choice(["CFO", "COO", "IT manager", "HR manager", "Internal audit"]), r.choice(["Policy and review", "Monthly reconciliation", "Access control", "Insurance", "Backup", "Training"]),
                 iso(TODAY - dt.timedelta(days=r.randint(10, 400)))])
rows[7][5] = rows[7][3] * rows[7][4] + 6                            # score is not Likelihood x Impact
rows[12][6] = None                                                  # no owner
pack("risk", "Risk Consulting", "mirqab-risk-register-2026.xlsx", "Risk register",
     ["Risk", "Description", "Category", "Likelihood (1-5)", "Impact (1-5)", "Score", "Owner", "Key control", "Last reviewed"], rows, [7, 30, 13, 15, 13, 7, 15, 22, 13],
     "A client's board wants the top risks on one page, with the risks nobody reviewed this year.",
     "Reads the register, recalculates every score, and lists the top risks and the risks not reviewed in 12 months.",
     "A heat map (likelihood by impact) and a one-page board summary.", "On the first Sunday of each month.",
     [f"{rows[7][0]}: the score is not Likelihood × Impact. Flag it and show both numbers.", f"{rows[12][0]}: no owner. Flag it."],
     {"Risks": len(rows), "Score 15 or more (recalculated)": sum(1 for x in rows if x[3] * x[4] >= 15),
      "Not reviewed in 12 months": sum(1 for x in rows if d(x[8]) < TODAY - dt.timedelta(days=365))})

# 5 · Cybersecurity: the vulnerability scan
r = random.Random(5)
VULNS = [("Missing operating system patch", "High", 8.1), ("Outdated TLS version", "Medium", 5.9), ("Default admin password on a printer", "Critical", 9.8),
         ("Unsupported database version", "High", 7.5), ("Open remote desktop port", "High", 8.8), ("Weak password policy", "Medium", 5.3),
         ("Expired SSL certificate", "Medium", 5.0), ("Old antivirus definitions", "Low", 3.1), ("Unencrypted backup share", "High", 7.2)]
rows = []
for i in range(26):
    v = r.choice(VULNS); first = TODAY - dt.timedelta(days=r.randint(1, 70))
    rows.append([f"V-{i + 701}", f"{r.choice(['SRV', 'WKS', 'PRN', 'NAS'])}-{r.randint(10, 99)}", f"10.20.{r.randint(1, 9)}.{r.randint(10, 250)}", v[0], v[1], v[2], iso(first),
                 (TODAY - first).days, r.choice(["Open", "Open", "In progress", "Fixed"]), r.choice(["IT team", "Network team", "Vendor"])])
rows[3][3:6] = ["Default admin password on a printer", "Critical", 9.8]; rows[3][6] = iso(TODAY - dt.timedelta(days=45)); rows[3][7] = 45; rows[3][8] = "Open"
rows[19][4] = "Low"; rows[19][5] = 8.8                              # severity does not match the CVSS score
pack("cyber", "Cybersecurity", "mirqab-cyber-vulnerability-scan-nov.xlsx", "Scan results",
     ["Finding", "Asset", "IP address", "Vulnerability", "Severity", "CVSS", "First seen", "Days open", "Status", "Owner"], rows, [9, 9, 13, 34, 10, 7, 12, 10, 12, 13],
     "The scan finds the same issues every week. Management wants to know what is critical, what is old and who owns it.",
     "Reads the scan and lists open Critical and High findings, findings open over 30 days, and the count by owner.",
     "A risk dashboard: open by severity, age buckets, and the top 5 to fix this week.", "Every Thursday at 07:00, after the weekly scan.",
     [f"{rows[3][0]}: Critical and open for 45 days. Put it first.", f"{rows[19][0]}: severity says Low but the CVSS score is 8.8. Flag the mismatch; do not change either value."],
     {"Findings": len(rows), "Not fixed": sum(1 for x in rows if x[8] != "Fixed"), "Critical or High, not fixed": sum(1 for x in rows if x[8] != "Fixed" and x[4] in ("Critical", "High")),
      "Open over 30 days, not fixed": sum(1 for x in rows if x[8] != "Fixed" and x[7] > 30)})

# 6 · IT and the Technology Hub: the helpdesk tickets
r = random.Random(6)
rows = []
for i in range(40):
    opened = dt.datetime(2026, 10, 1, 8) + dt.timedelta(hours=r.randint(0, 24 * 30))
    pri = r.choice(["P1", "P2", "P3", "P3", "P4"]); sla = {"P1": 4, "P2": 8, "P3": 24, "P4": 72}[pri]
    res = round(sla * r.choice([0.3, 0.5, 0.8, 1.0, 1.4, 0.6]), 1)
    closed = opened + dt.timedelta(hours=res)
    rows.append([f"T-{i + 9001}", opened.strftime("%Y-%m-%d %H:%M"), closed.strftime("%Y-%m-%d %H:%M"), r.choice(["Password reset", "Laptop", "Printer", "Email", "VPN", "Software install", "Access request"]),
                 pri, sla, res, r.choice(["Ali", "Sara", "Omar"]), "Closed"])
rows[9][2] = (dt.datetime.strptime(rows[9][1], "%Y-%m-%d %H:%M") - dt.timedelta(hours=3)).strftime("%Y-%m-%d %H:%M")   # closed before opened
rows[25][4] = "P1"; rows[25][5] = 4; rows[25][6] = 11.5                                                                    # P1 SLA breach
pack("it", "IT and the Technology Hub", "mirqab-it-helpdesk-tickets-oct.xlsx", "Tickets October",
     ["Ticket", "Opened", "Closed", "Category", "Priority", "SLA (hours)", "Resolution (hours)", "Assigned to", "Status"], rows, [9, 17, 17, 16, 9, 11, 17, 12, 9],
     "The IT manager writes a monthly service report by hand from the ticket export.",
     "Reads the ticket export and returns SLA met by priority, tickets by category, and every breach with its hours.",
     "A service dashboard and a one-page monthly report.", "On the 1st of each month at 08:00.",
     [f"{rows[9][0]}: closed before it was opened. Flag it as a data error.", f"{rows[25][0]}: a P1 ticket took 11.5 hours against a 4-hour SLA. It must show as a breach."],
     {"Tickets": len(rows), "SLA breaches (resolution over SLA)": sum(1 for x in rows if x[6] > x[5]),
      "SLA met (%)": round(sum(1 for x in rows if x[6] <= x[5]) / len(rows) * 100, 1)})

# 7 · ESG and Sustainability: energy and emissions
r = random.Random(7)
SITES = ["Head office, Sharq", "Warehouse, Sulaibiya", "Branch, Salmiya"]
MONTHS = [f"2025-{m:02d}" for m in range(1, 13)]
rows = []
for s in SITES:
    base = {"Head office, Sharq": 42000, "Warehouse, Sulaibiya": 88000, "Branch, Salmiya": 15000}[s]
    for m in MONTHS:
        mm = int(m[-2:]); season = 1.0 + (0.55 if mm in (6, 7, 8) else 0.3 if mm in (5, 9) else 0.0)
        rows.append([s, m, int(base * season * r.uniform(0.95, 1.05)), int(r.uniform(300, 900) if "Warehouse" in s else r.uniform(0, 120)), int(r.uniform(150, 600)), int(r.uniform(400, 2200))])
_mi = [i for i, x in enumerate(rows) if x[0] == SITES[0] and x[1] == "2025-07"][0]; rows[_mi][2] = None              # missing electricity
_mu = [i for i, x in enumerate(rows) if x[0] == SITES[1] and x[1] == "2025-03"][0]; rows[_mu][2] = round(rows[_mu][2] / 1000, 1)   # entered in MWh, not kWh
EF = {"electricity": 0.6, "diesel": 2.68}
pack("esg", "ESG and Sustainability", "mirqab-esg-energy-emissions-2025.xlsx", "Energy 2025",
     ["Site", "Month", "Electricity (kWh)", "Diesel (litres)", "Water (m3)", "Waste (kg)"], rows, [22, 10, 17, 15, 12, 12],
     "A client needs its first sustainability report. The data comes from three sites, by month, and nobody has checked it.",
     f"Reads the monthly data, calculates emissions with the factors in the file (electricity {EF['electricity']} kg CO2e per kWh, diesel {EF['diesel']} kg CO2e per litre), and flags gaps and outliers.",
     "An emissions dashboard by site and month, and a 5-slide summary for the client's board.", "On the 5th of each month, when the site data arrives.",
     [f"{rows[_mi][0]}, {rows[_mi][1]}: electricity is blank. Flag it; do not fill it with an average.",
      f"{rows[_mu][0]}, {rows[_mu][1]}: electricity is {rows[_mu][2]}, about 1,000 times lower than other months. It looks like MWh, not kWh. Flag it; do not convert it."],
     {"Rows": len(rows), "Sites": len(SITES), "Factors (training only)": f"electricity {EF['electricity']} kg CO2e per kWh; diesel {EF['diesel']} kg CO2e per litre"})

# 8 · AI and Data Analytics: a client's sales transactions
r = random.Random(8)
rows = []
for i in range(60):
    q = r.randint(1, 12); p = float(r.choice([1.250, 2.750, 4.500, 7.900, 12.000, 18.500]))
    rows.append([f"S-{i + 40001}", iso(dt.date(2026, 10, 1) + dt.timedelta(days=r.randint(0, 30))), r.choice(["Salmiya", "Jahra", "Hawally", "Fahaheel"]),
                 r.choice(["Bakery", "Dairy", "Frozen", "Snacks", "Drinks"]), q, p, round(q * p, 3), r.choice(["Walk-in", "Delivery", "Corporate"])])
rows[33] = list(rows[12]); rows[33][0] = rows[12][0]                # duplicate transaction
rows[47][6] = round(rows[47][4] * rows[47][5] + 10, 3)              # amount is not quantity x price
_tot = sum(x[6] for i, x in enumerate(rows) if i != 33)
pack("data", "AI and Data Analytics", "mirqab-data-sales-transactions-oct.xlsx", "Sales October",
     ["Transaction", "Date", "Branch", "Category", "Quantity", "Unit price (KWD)", "Amount (KWD)", "Channel"], rows, [12, 12, 11, 11, 10, 17, 15, 11],
     "A retail client wants to know what sells, where and when, and whether its sales data can be trusted.",
     "Checks the data first (duplicates, amount equals quantity times price), then reports sales by branch, category and week.",
     "A sales dashboard with filters, and a data-quality note on page one.", "Every Sunday at 09:00, on last week's export.",
     [f"{rows[12][0]}: appears twice. Count it once and flag the duplicate.", f"{rows[47][0]}: Amount is not Quantity × Unit price (off by KWD 10.000). Flag it; do not correct it."],
     {"Rows": len(rows), "Unique transactions": len(rows) - 1, "Total sales, duplicate removed (KWD)": f"{_tot:,.3f}"})

# 9 · Finance: budget against actual
r = random.Random(9)
ACCTS = [("Salaries", 48000), ("Rent", 9500), ("Travel", 2400), ("Training", 1800), ("Software", 3200), ("Marketing", 2600), ("Office supplies", 700), ("Professional fees", 4100), ("Utilities", 1300), ("Insurance", 900)]
rows = []
for cc in ["Assurance", "Advisory", "Tax", "Support"]:
    for a, b in ACCTS:
        bud = round(b * {"Assurance": 1.0, "Advisory": 0.6, "Tax": 0.4, "Support": 0.3}[cc] * 10)
        rows.append([cc, a, float(bud), float(round(bud * r.uniform(0.82, 1.12)))])
_ix = [i for i, x in enumerate(rows) if x[0] == "Advisory" and x[1] == "Travel"][0]; rows[_ix][3] = round(rows[_ix][2] * 1.42)
_iy = [i for i, x in enumerate(rows) if x[0] == "Support" and x[1] == "Software"][0]; rows[_iy][3] = None
pack("finance", "Finance", "mirqab-finance-budget-vs-actual-2026.xlsx", "Jan to Oct 2026",
     ["Cost center", "Account", "Budget Jan-Oct (KWD)", "Actual Jan-Oct (KWD)"], rows, [14, 20, 22, 22],
     "Every month the finance team explains the variances to the partners, line by line, in a long email.",
     "Calculates the variance in KWD and percent for every line, flags lines over 10% and over KWD 1,000, and drafts one question per flag.",
     "A variance dashboard by cost center and a one-page memo to the managing partner.", "On the 3rd working day of each month.",
     [f"{rows[_ix][0]} / {rows[_ix][1]}: 42% over budget. It must be flagged.", f"{rows[_iy][0]} / {rows[_iy][1]}: Actual is blank. Flag it; never treat it as zero."],
     {"Lines": len(rows), "Lines over 10% and over KWD 1,000": sum(1 for x in rows if x[3] is not None and (x[3] - x[2]) > 1000 and (x[3] - x[2]) / x[2] > 0.10)})

# 10 · HR: people data (IDs only, no names)
r = random.Random(10)
rows = []
for i in range(36):
    join = dt.date(2026, 11, 1) - dt.timedelta(days=r.randint(60, 3000))
    rows.append([f"EMP-{i + 2101}", r.choice(["Assurance", "Assurance", "Advisory", "Tax", "Support"]), r.choice(["Associate", "Senior associate", "Supervisor", "Manager"]),
                 iso(join), r.randint(2, 30), r.randint(0, 40), r.choice(["Active", "Active", "Active", "On leave", "Notice period"])])
rows[5][3] = "2027-02-01"                                           # join date in the future
rows[28][4] = -6                                                    # negative leave balance
pack("hr", "Human Resources", "mirqab-hr-people-data-2026.xlsx", "People Nov 2026",
     ["Employee", "Department", "Grade", "Join date", "Leave balance (days)", "Training hours 2026", "Status"], rows, [11, 13, 17, 12, 19, 19, 14],
     "HR answers the same questions every month: headcount, training hours, leave balances and who is on notice.",
     "Reads the people file and returns headcount by department and grade, training hours under the 20-hour target, and leave balances to check.",
     "An HR dashboard and a one-page monthly note for the partners. Employee IDs only, never names.", "On the last working day of each month.",
     [f"{rows[5][0]}: the join date is in 2027. Flag it as a data error.", f"{rows[28][0]}: leave balance is -6 days. Flag it for HR to check."],
     {"Employees": len(rows), "Under 20 training hours": sum(1 for x in rows if x[5] < 20), "On notice": sum(1 for x in rows if x[6] == "Notice period")})

# 11 · Customer Experience: the client survey
r = random.Random(11)
COMMENTS = ["Clear and on time.", "Too many document requests.", "Very helpful team.", "Report came late.", "Good value.", "Hard to reach the manager.", "Excellent advice.", "Fees were not clear.", ""]
rows = []
for i in range(40):
    sc = r.choice([10, 10, 9, 9, 9, 8, 8, 7, 6, 5, 3])
    rows.append([f"CX-{i + 801}", r.choice(["Audit", "Tax", "Corporate Finance", "Risk Consulting"]), iso(dt.date(2026, 10, 1) + dt.timedelta(days=r.randint(0, 40))), sc, r.choice(COMMENTS)])
rows[14][3] = 11                                                    # out of range
rows[31] = list(rows[30]); rows[31][0] = f"CX-{832}"; rows[31][0] = rows[30][0]   # the same response twice
_valid = [x for i, x in enumerate(rows) if i != 31 and 0 <= x[3] <= 10]
_nps = round((sum(1 for x in _valid if x[3] >= 9) - sum(1 for x in _valid if x[3] <= 6)) / len(_valid) * 100)
pack("cx", "Customer Experience", "mirqab-cx-client-survey-2026.xlsx", "Responses",
     ["Response", "Service line", "Date", "Score (0-10)", "Comment"], rows, [10, 18, 12, 13, 36],
     "Client feedback arrives every week, but nobody turns it into a score or a list of what to fix.",
     "Calculates the NPS by service line, groups the comments into themes, and lists the three things to fix first.",
     "An NPS dashboard and a 5-slide quarterly client-feedback deck.", "Every Sunday at 08:00.",
     [f"{rows[14][0]}: score 11 is outside 0 to 10. Leave it out of the NPS and flag it.", f"{rows[30][0]}: appears twice. Count it once."],
     {"Responses": len(rows), "Valid, unique responses": len(_valid), "NPS (valid, unique)": _nps})

PACK_FILES = [p["file"] for p in PACKS]
DEPTS = [p["dept"] for p in PACKS]
F_BRIEFS = "mirqab-mini-project-briefs.docx"
