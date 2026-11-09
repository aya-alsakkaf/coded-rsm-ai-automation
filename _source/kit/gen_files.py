# -*- coding: utf-8 -*-
"""The 22 fictional sample files of the RSM workshop (Mirqab & Co. and its fictional client Abdali Foods).
    python3 gen_files.py OUTDIR        (the kit keeps them in ../files; the site copies them unchanged)
Names never change once built: participants download them."""
import sys, os, datetime as dt
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from docx import Document
from docx.shared import Pt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import data as D
import content_demos as CD

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files")
os.makedirs(OUT, exist_ok=True)
FIXED = dt.datetime(2026, 11, 8, 9, 0, 0)
HEAD = Font(bold=True, color="FFFFFF"); FILL = PatternFill("solid", fgColor="14243F")

# ------------------------------------------------------------------ writers
def doc(name, title, blocks):
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    d.add_heading(title, 1)
    for kind, val in blocks:
        if kind == "p": d.add_paragraph(val)
        elif kind == "b": d.add_paragraph(val, style="List Bullet")
        elif kind == "n": d.add_paragraph(val, style="List Number")
        elif kind == "h": d.add_heading(val, 2)
        elif kind == "t":
            head, rows = val
            t = d.add_table(rows=1, cols=len(head)); t.style = "Table Grid"
            for i, h in enumerate(head): t.rows[0].cells[i].text = str(h)
            for r in rows:
                cells = t.add_row().cells
                for i, v in enumerate(r): cells[i].text = str(v)
    d.add_paragraph(D.FICTION).runs[0].italic = True
    cp = d.core_properties; cp.author = "CODED"; cp.title = title; cp.created = FIXED; cp.modified = FIXED; cp.last_modified_by = "CODED"
    d.save(os.path.join(OUT, name))

def xlsx(name, sheets):
    """sheets = [(title, head, rows, widths, note)]"""
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    for title, head, rows, widths, note in sheets:
        ws = wb.create_sheet(title)
        ws.append(head)
        for c in ws[1]: c.font = HEAD; c.fill = FILL; c.alignment = Alignment(vertical="center")
        for r in rows: ws.append(list(r))
        for i, w in enumerate(widths, 1): ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w
        for row in ws.iter_rows(min_row=2):
            for c in row:
                if isinstance(c.value, float): c.number_format = "#,##0.000"
                elif isinstance(c.value, int) and c.column > 1: c.number_format = "#,##0"
        ws.append([]); ws.append([note or D.FICTION])
        ws.cell(ws.max_row, 1).font = Font(italic=True, color="666666")
        ws.freeze_panes = "A2"
    wb.properties.creator = "CODED"; wb.properties.created = FIXED; wb.properties.modified = FIXED; wb.properties.lastModifiedBy = "CODED"
    wb.save(os.path.join(OUT, name))

class Pdf:
    def __init__(self, name):
        self.c = canvas.Canvas(os.path.join(OUT, name), pagesize=A4, invariant=1)
        self.c.setAuthor("CODED"); self.c.setTitle(name)
        self.w, self.h = A4
    def page(self, lines, footer=True):
        c, y = self.c, self.h - 60
        for kind, txt in lines:
            if kind == "title": c.setFont("Helvetica-Bold", 16); c.drawString(50, y, txt); y -= 26
            elif kind == "h": c.setFont("Helvetica-Bold", 11); c.drawString(50, y, txt); y -= 18
            elif kind == "kv": c.setFont("Helvetica", 10); c.drawString(50, y, txt[0]); c.drawString(210, y, txt[1]); y -= 15
            elif kind == "row": c.setFont("Helvetica", 10); [c.drawString(x, y, s) for x, s in txt]; y -= 15
            elif kind == "rule": c.line(50, y + 6, self.w - 50, y + 6); y -= 8
            elif kind == "gap": y -= txt
            else:
                c.setFont("Helvetica", 10)
                for part in wrap(txt, 95): c.drawString(50, y, part); y -= 14
        if footer:
            c.setFont("Helvetica-Oblique", 8); c.drawString(50, 40, D.FICTION)
        c.showPage()
    def save(self): self.c.save()

def wrap(t, n):
    out, line = [], ""
    for w in t.split():
        if len(line) + len(w) + 1 > n: out.append(line); line = w
        else: line = (line + " " + w).strip()
    return out + ([line] if line else [])

def invoice_page(no, supplier, date, po, amount, desc, cur="KWD"):
    lines = [("title", supplier), ("p", "Kuwait · Commercial registration: fictional"), ("gap", 8), ("h", "TAX INVOICE" if False else "INVOICE"), ("rule", None),
             ("kv", ("Invoice no.:", no or "")), ("kv", ("Invoice date:", date)), ("kv", ("Bill to:", D.CO)), ("kv", ("Customer PO:", po or ""))]
    lines += [("gap", 10), ("row", [(50, "Description"), (330, "Qty"), (420, f"Amount ({cur})")]), ("rule", None),
              ("row", [(50, desc), (330, "1 lot"), (420, f"{amount:,.3f}" if cur == "KWD" else f"{amount:,.2f}")]), ("rule", None),
              ("row", [(330, "Total"), (420, f"{cur} {amount:,.3f}" if cur == "KWD" else f"{cur} {amount:,.2f}")]),
              ("gap", 16), ("p", "Payment terms: 30 days from the invoice date. Bank transfer only.")]
    return lines

# ------------------------------------------------------------------ 1 · the engagement letter (Task 1.1): no section on management's responsibilities
L = D.LETTER
doc(CD.F_LETTER, f"Audit engagement letter: {D.CO}", [
    ("p", f"{D.FIRM_LONG} · Kuwait · {D.LETTER_DATE}"),
    ("p", f"To the Board of Directors, {D.CO}"),
    ("p", f"You have asked us to audit the financial statements of {D.CO} for the year ending {L['fy_end']}. This letter confirms the terms of our engagement."),
    ("h", D.LETTER_SECTIONS[0]), ("p", "We will audit the statement of financial position, the statements of profit or loss, changes in equity and cash flows, and the notes. "
                                     "Our objective is reasonable assurance that the financial statements as a whole are free from material misstatement, and to issue an auditor's report."),
    ("h", D.LETTER_SECTIONS[1]), ("p", "We will plan and perform the audit in line with International Standards on Auditing. We will tell you in writing about significant deficiencies in internal control that we find."),
    ("h", D.LETTER_SECTIONS[2]), ("p", "The financial statements will be prepared under IFRS Accounting Standards as adopted in Kuwait."),
    ("h", D.LETTER_SECTIONS[3]), ("p", "We expect to issue an unmodified opinion. If we cannot, we will discuss the reasons with you first."),
    ("h", D.LETTER_SECTIONS[4]), ("b", f"Interim fieldwork: {L['interim']}."), ("b", f"Year-end fieldwork: {L['year_end_work']}."), ("b", f"Auditor's report: by {L['report']}."),
    ("h", D.LETTER_SECTIONS[5]), ("p", f"Our fee is KWD {L['fee']:,.3f}, plus out-of-pocket costs. We bill 40% after interim fieldwork and 60% on the report."),
    ("h", D.LETTER_SECTIONS[6]), ("p", "Your staff will give us the records and information we ask for, on the dates in our request list."),
    ("h", D.LETTER_SECTIONS[7]), ("p", f"Please sign and return a copy of this letter by {L['sign_by']}."),
    ("p", "Yours faithfully, Partner, Mirqab & Co."),
])

# ------------------------------------------------------------------ 2 · the October invoices (5 pages) and 3 · the October ledger
p = Pdf(CD.F_INV)
for no, sup, date, po, amt, desc in D.INVOICES: p.page(invoice_page(no, sup, date, po, amt, desc))
p.save()
LH = ["Posting date", "Voucher", "Supplier", "Invoice no.", "Invoice date", "Amount (KWD)", "Account"]
xlsx(CD.F_LEDGER, [("Purchase ledger Oct 2026", LH, [list(r) for r in D.LEDGER], [13, 11, 30, 13, 13, 15, 15], None)])

# ------------------------------------------------------------------ 4 · the output template (knowledge for the invoice agent)
xlsx(CD.F_TEMPLATE, [("Invoice match", D.TEMPLATE_HEAD, [D.TEMPLATE_EXAMPLE], [13, 30, 13, 11, 18, 18, 15, 16, 40],
                      "Status is one of: " + ", ".join(D.STATUSES) + ". Amounts in KWD with three decimals. " + D.FICTION)])

# ------------------------------------------------------------------ 5 · the six leases (Extraction)
def lease_page(no, prem, lessor, start, end, rent, dep, special):
    ls = [("title", f"Lease agreement no. {no}"), ("p", f"Between {lessor} (the landlord) and {D.CO} (the tenant)."), ("gap", 6),
          ("h", "1. Premises"), ("p", prem + ", Kuwait."), ("h", "2. Term"),
          ("p", f"The lease starts on {start} and ends on {end}." if end else f"The lease starts on {start} and continues until further notice.")]
    ls += [("h", "3. Rent"), ("p", f"The monthly rent is KWD {rent:,.3f}, paid in advance on the first day of each month."),
           ("h", "4. Deposit"), ("p", f"The tenant pays a deposit of KWD {dep:,.3f}, returned at the end of the lease.")]
    ls += [("h", "5. Use"), ("p", "The tenant uses the premises for food storage, sales and offices only.")]
    ls += [("h", "6. Special terms"), ("p", special or "None.")]
    ls += [("h", "7. Law"), ("p", "This lease follows the laws of the State of Kuwait.")]
    return ls
p = Pdf(CD.F_LEASES)
for r in D.LEASES: p.page(lease_page(*r))
p.save()

# ------------------------------------------------------------------ 6 · the two-year trial balance (Analysis)
xlsx(CD.F_TB, [("Trial balance", ["Account", "Group", "FY2024 (KWD)", "FY2025 (KWD)"], [list(r) for r in D.TB], [32, 12, 16, 16],
                f"Debits positive, credits negative. Threshold for review: change over {D.THRESH_PCT}% and over KWD {D.THRESH_AMT:,}. " + D.FICTION)])

# ------------------------------------------------------------------ 7 · the request list and 8 · the client emails (Workflow)
xlsx(CD.F_PBC, [("Request list", ["No.", "Item requested", "Due date", "Status"], [[r[0], r[1], r[2], ""] for r in D.PBC], [6, 52, 12, 16],
                 f"Interim audit of {D.CO}, FY2026. Mirqab & Co. " + D.FICTION)])
def email_blocks(emails, start=1):
    out = []
    for i, (date, frm, subj, body, _items) in enumerate(emails, start):
        att = D.EMAIL_ATTACH.get(i, []) if start == 1 else []
        out += [("h", f"Email {i} · {date} · {subj}"), ("p", f"From: {frm}, {D.CO_SHORT} · To: Mirqab audit team"), ("p", body),
                ("p", "Attachments: " + (", ".join(att) if att else "none"))]
    return out
doc(CD.F_EMAILS, f"Client emails: {D.CO_SHORT}, 9 to 12 November 2026", email_blocks(D.EMAILS))

# ------------------------------------------------------------------ 9 · the weekly status sheet, week 46 (Reporting)
SH = ["Engagement", "Type", "Budget (hours)", "Used (hours)", "Open items", "Next deadline", "Note"]
xlsx(CD.F_STATUS, [("Week 46", SH, [list(r) for r in D.STATUS46], [34, 32, 14, 13, 11, 30, 30], "Week 46: 8 to 12 November 2026. " + D.FICTION)])

# ------------------------------------------------------------------ 10 to 14 · the messy samples (Task 1.10)
p = Pdf(CD.F_M_INV)
p.page(invoice_page("", "Gulf Trade Imports FZE", "2026-10-29", "PO-2236", 2300.00, "Spare parts for the packing line", cur="USD")); p.save()
p = Pdf(CD.F_M_LEASE)
p.page(lease_page(7, "Outlet, Abu Halifa", "Mangaf Real Estate Co.", "2026-06-01", "", 1320.000, 2640.000, "")); p.save()
xlsx(CD.F_M_TB, [("Trial balance", ["Account", "Group", "FY2024 (KWD)", "FY2025 (KWD)"],
                  [[a, g, (None if a == "Repairs and maintenance" else p_), c] for a, g, p_, c in D.TB], [32, 12, 16, 16], "One figure is missing. " + D.FICTION)])
doc(CD.F_M_EMAIL, f"Client email: {D.CO_SHORT}, 13 November 2026", [
    ("h", "Email · 2026-11-13 · Two items"), ("p", f"From: Hessa, Finance Manager, {D.CO_SHORT} · To: Mirqab audit team"),
    ("p", "Board minutes and legal letters: we will send both next week."), ("p", "Attachments: none")])
xlsx(CD.F_M_STATUS, [("Week 46", SH, [list(r) if r[0] != D.STATUS46[2][0] else [r[0], r[1], None, 64, r[4], r[5], r[6]] for r in D.STATUS46],
                      [34, 32, 14, 13, 11, 30, 30], "One budget is blank. " + D.FICTION)])

# ------------------------------------------------------------------ 15 · the catch-up file: a starter instruction for each track
blocks = [("p", "For anyone who missed Day 1, or wants a clean start. Paste one track into the project instructions, then change it to your task.")]
for t, parts in CD.STARTER.items():
    blocks.append(("h", t))
    for k, v in parts: blocks.append(("b", f"{k}: {v}"))
blocks += [("h", "The invoice agent (the trainer's example)")] + [("b", f"{k}: {v}") for k, v in CD.INVOICE_AGENT]
doc(CD.F_STARTER, "Starter instructions: five parts for each track", blocks)

# ------------------------------------------------------------------ 16 · the department rules (Day 2 Lesson 4)
blocks = [("p", "Add the rules for your department to your skill, word for word.")]
for dpt, rs in D.RULES:
    blocks.append(("h", dpt)); blocks += [("b", r) for r in rs]
doc(CD.F_RULES, "Mirqab & Co. review rules for AI workflows", blocks)

# ------------------------------------------------------------------ 17 to 22 · batch 2 (Day 2 Lesson 3)
p = Pdf(CD.F_INV2)
for no, sup, date, po, amt, cur, desc in D.INVOICES_B2: p.page(invoice_page(no, sup, date, po, amt, desc, cur=cur))
p.save()
xlsx(CD.F_LEDGER2, [("Purchase ledger Nov wk1", LH, [list(r) for r in D.LEDGER_B2], [13, 11, 30, 13, 13, 15, 15], "1 to 5 November 2026. " + D.FICTION)])
p = Pdf(CD.F_LEASE2); p.page(lease_page(*D.NEW_LEASE)); p.save()
xlsx(CD.F_MGMT, [("Management accounts", ["Line", "September 2026 (KWD)", "October 2026 (KWD)"], [list(r) for r in D.MGMT], [28, 20, 20],
                  f"Month on month. Threshold: over {D.THRESH_PCT}% and over KWD {D.THRESH_AMT:,}. " + D.FICTION)])
doc(CD.F_EMAILS2, f"Client emails: {D.CO_SHORT}, 15 to 16 November 2026", email_blocks(D.EMAILS_B2, start=11) and [
    x for i, (date, frm, subj, body, _it) in enumerate(D.EMAILS_B2, 11)
    for x in (("h", f"Email {i} · {date} · {subj}"), ("p", f"From: {frm}, {D.CO_SHORT} · To: Mirqab audit team"), ("p", body),
              ("p", "Attachments: " + ({11: "sales-listing-oct-2026.xlsx", 12: "lease-fahaheel.pdf, lease-abu-halifa.pdf, lease-mahboula.pdf", 13: "mgmt-accounts-oct-2026.xlsx"}.get(i, "none"))))])
xlsx(CD.F_STATUS2, [("Week 47", SH, [list(r) for r in D.STATUS47], [34, 32, 14, 13, 11, 30, 30], "Week 47 to date: 15 to 16 November 2026. " + D.FICTION)])

missing = [f for f in CD.ALL_FILES if not os.path.exists(os.path.join(OUT, f))]
assert not missing, missing
print(f"files: {len(CD.ALL_FILES)} written to {OUT}")
