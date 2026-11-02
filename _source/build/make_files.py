# -*- coding: utf-8 -*-
"""Generates the fictional practice files into _source/files/. Run once; the build copies them to public/.
Every file says FICTIONAL · FOR TRAINING. No real client, person or ID number appears anywhere.

Planted findings (the answer key lives in content_staff.py, never on a participant page):
  khiran   : license expired, company name mismatch, company shareholder abroad with no documents,
             one shareholder ID copy missing, one signatory ID expiring within 60 days.
  jabriya  : articles missing, a politically exposed shareholder, one ID expiring within 60 days.
  salwa    : complete and valid.
  TB       : 6 accounts pass both tests; marketing, statutory reserve and accumulated depreciation pass only one.
  invoices : 3 match, 1 amount mismatch, 1 cut-off mismatch, 1 customer name to check.
  notes    : 3 control findings, 1 needs more information, 1 is not a finding, 2 staff names to remove.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from docx import Document
from docx.shared import Pt, RGBColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

OUT = os.path.join(os.path.dirname(__file__), "..", "files")
os.makedirs(OUT, exist_ok=True)
TAG = "FICTIONAL · FOR TRAINING · NOT A REAL COMPANY"
NAVY = (0, 17 / 255, 47 / 255)


# ───────────────────────── PDF helpers ─────────────────────────
class Pdf:
    def __init__(self, name, title):
        self.c = canvas.Canvas(os.path.join(OUT, name), pagesize=A4)
        self.c.setTitle(title)
        self.c.setAuthor("CODED training (fictional)")
        self.c.setSubject(TAG)
        self.page = 0
        self.title = title

    def new(self, heading, sub=""):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        w, h = A4
        c.setFillColorRGB(*NAVY)
        c.rect(0, h - 22 * mm, w, 22 * mm, fill=1, stroke=0)
        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(18 * mm, h - 13 * mm, heading)
        c.setFont("Helvetica", 8.5)
        c.drawRightString(w - 18 * mm, h - 13 * mm, TAG)
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 8)
        c.drawString(18 * mm, 12 * mm, f"{self.title} · page {self.page}")
        c.drawRightString(w - 18 * mm, 12 * mm, TAG)
        self.y = h - 34 * mm
        if sub:
            self.text(sub, size=9.5, gap=7)

    def text(self, s, size=10.5, bold=False, gap=6.2, x=18):
        c = self.c
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawString(x * mm, self.y, s)
        self.y -= gap * mm

    def kv(self, rows, x2=78):
        for k, v in rows:
            self.c.setFont("Helvetica-Bold", 10.5)
            self.c.drawString(18 * mm, self.y, k)
            self.c.setFont("Helvetica", 10.5)
            self.c.drawString(x2 * mm, self.y, v)
            self.y -= 7 * mm

    def table(self, cols, rows, widths):
        c = self.c
        x0 = 18 * mm
        c.setFont("Helvetica-Bold", 9.5)
        x = x0
        for col, wd in zip(cols, widths):
            c.drawString(x, self.y, col)
            x += wd * mm
        self.y -= 2.5 * mm
        c.line(x0, self.y, x0 + sum(widths) * mm, self.y)
        self.y -= 5 * mm
        c.setFont("Helvetica", 9.5)
        for r in rows:
            x = x0
            for v, wd in zip(r, widths):
                c.drawString(x, self.y, str(v))
                x += wd * mm
            self.y -= 6.5 * mm
        self.y -= 3 * mm

    def save(self):
        self.c.save()


def kyc_pack(fname, company, lic_name, art_name, lic_no, lic_exp, activity, capital, managers,
             shareholders, sh_note, signatories, ids, articles=True, index=None):
    p = Pdf(fname, f"{company} · KYC pack")
    p.new("Commercial License", "Ministry of Commerce and Industry · State of Kuwait (fictional example)")
    p.kv([("License holder", lic_name), ("License number", lic_no), ("Legal form", "With Limited Liability (W.L.L.)"),
          ("Activity", activity), ("Address", "Block 4, Street 12, Kuwait City (fictional)"),
          ("Issue date", "01 Oct 2023"), ("Expiry date", lic_exp)])
    p.y -= 6 * mm
    p.text("This page is a made-up training example. It is not a government document.", size=9)
    if articles:
        p.new("Articles of Association (extract)")
        p.kv([("Company name", art_name), ("Legal form", "With Limited Liability (W.L.L.)"),
              ("Share capital", capital), ("Objects", activity), ("Managers", managers),
              ("Signed", "12 Sep 2023 (fictional)")])
    else:
        p.new("Pack index", "Documents received from the client with this pack")
        p.table(["Document", "Received", "Client note"], index, [70, 30, 70])
    p.new("Shareholder Register", f"{company} · as at 01 Nov 2026")
    p.table(["Shareholder", "Type", "Registered in", "Shares %"], shareholders, [62, 28, 52, 24])
    for line in sh_note:
        p.text(line, size=9.5)
    p.new("Authorized Signatory List", f"{company} · approved by the managers")
    p.table(["Name", "Role", "Signing limit (KWD)"], signatories, [60, 60, 50])
    p.new("ID Copies Received", "Index of identity document copies received with this pack (no ID numbers on this page)")
    p.table(["Name", "Role in the company", "Document", "Expiry", "Copy received"], ids, [42, 48, 22, 28, 26])
    p.save()


def make_pdfs():
    kyc_pack("khiran-kyc-pack.pdf", "Khiran Logistics", "Khiran Logistic Co. W.L.L.", "Khiran Logistics Company W.L.L.",
             "2023/48213", "30 Sep 2026", "Freight forwarding and warehousing", "KWD 250,000",
             "Faisal Al-Mansour; Tariq Al-Shatti",
             [["Khiran Holding Ltd", "Company", "Dubai, UAE", "40"], ["Faisal Al-Mansour", "Person", "Kuwait", "35"],
              ["Huda Al-Saleh", "Person", "Kuwait", "25"]],
             ["Khiran Holding Ltd is a company. Its owners are not listed in this pack."],
             [["Faisal Al-Mansour", "Manager", "No limit"], ["Tariq Al-Shatti", "Finance manager", "50,000"]],
             [["Faisal Al-Mansour", "Shareholder, manager", "Civil ID", "14 Feb 2029", "Yes"],
              ["Tariq Al-Shatti", "Signatory", "Civil ID", "20 Dec 2026", "Yes"]])
    kyc_pack("jabriya-kyc-pack.pdf", "Jabriya Medical Supplies", "Jabriya Medical Supplies W.L.L.", "",
             "2021/30577", "12 Mar 2028", "Import and sale of medical supplies", "KWD 150,000", "",
             [["Mona Al-Hajri", "Person", "Kuwait", "60"], ["Khalid Al-Hajri", "Person", "Kuwait", "40"]],
             ["Note from the client: Khalid Al-Hajri was a member of the Municipal Council from 2019 to 2023."],
             [["Mona Al-Hajri", "Manager", "No limit"]],
             [["Mona Al-Hajri", "Shareholder, manager", "Civil ID", "02 Jan 2027", "Yes"],
              ["Khalid Al-Hajri", "Shareholder", "Civil ID", "09 Jul 2030", "Yes"]],
             articles=False,
             index=[["Commercial license", "Yes", ""], ["Articles of association", "No", "To follow next week"],
                    ["Shareholder register", "Yes", ""], ["Authorized signatory list", "Yes", ""],
                    ["ID copies", "Yes", "See the last page"]])
    kyc_pack("salwa-kyc-pack.pdf", "Salwa Trading", "Salwa Trading Co. W.L.L.", "Salwa Trading Co. W.L.L.",
             "2022/17764", "18 Aug 2028", "General trading of office furniture", "KWD 100,000",
             "Reem Al-Fadhli",
             [["Reem Al-Fadhli", "Person", "Kuwait", "50"], ["Bader Al-Fadhli", "Person", "Kuwait", "50"]],
             ["All shareholders are persons."],
             [["Reem Al-Fadhli", "Manager", "No limit"], ["Bader Al-Fadhli", "Partner", "25,000"]],
             [["Reem Al-Fadhli", "Shareholder, manager", "Civil ID", "03 May 2029", "Yes"],
              ["Bader Al-Fadhli", "Shareholder, signatory", "Civil ID", "21 Nov 2028", "Yes"]])

    # invoices: one page each
    inv = [("INV-25-1142", "05/11/2025", "Qurtuba Fresh Market", "8,215.500", [("Frozen chicken, 1 kg x 1,200", "4,320.000"), ("Basmati rice, 10 kg x 300", "3,895.500")]),
           ("INV-25-1150", "12/11/2025", "Hawally Star Restaurant Group", "3,480.000", [("Cooking oil, 18 L x 120", "3,480.000")]),
           ("INV-25-1163", "20/11/2025", "Bayan Catering Co.", "15,900.750", [("Mixed vegetables, frozen x 2,100", "9,450.000"), ("Tomato paste, carton x 850", "6,450.750")]),
           ("INV-25-1187", "02/12/2025", "Golden Dune Hotels", "12,450.000", [("Dairy pack, weekly x 30", "12,450.000")]),
           ("INV-25-1196", "18/12/2025", "Blue Gulf Supermarkets", "6,730.250", [("Dates, 5 kg x 410", "4,100.000"), ("Tea, 500 g x 1,050", "2,630.250")]),
           ("INV-25-1203", "03/01/2026", "Nakheel Bakery", "9,120.000", [("Flour, 50 kg x 380", "9,120.000")])]
    p = Pdf("abdali-invoices-sample.pdf", "Abdali Foods · sales invoices sample")
    for no, date, cust, total, lines in inv:
        p.new("Abdali Foods Co. K.S.C.C. · Sales invoice", "Abdali, Kuwait (fictional) · Tel. +965 0000 0000")
        p.kv([("Invoice number", no), ("Invoice date", date), ("Customer", cust), ("Payment terms", "60 days")], x2=60)
        p.y -= 4 * mm
        p.table(["Description", "Amount (KWD)"], lines, [120, 40])
        p.text(f"Total (KWD): {total}", bold=True)
    p.save()


# ───────────────────────── DOCX helpers ─────────────────────────
def doc_base(title, sub):
    d = Document()
    st = d.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    sec = d.sections[0]
    sec.header.paragraphs[0].text = TAG
    sec.footer.paragraphs[0].text = "Mirqab & Co. is a fictional firm made for CODED training. " + TAG
    h = d.add_heading(title, level=0)
    p = d.add_paragraph(sub)
    p.runs[0].italic = True
    return d


def make_docs():
    d = doc_base("Client Acceptance Policy", "Mirqab & Co. · Version 3.2 · Owner: Risk and Quality · Fictional")
    d.add_heading("1. Purpose", 1)
    d.add_paragraph("This policy sets the minimum checks before the firm accepts a new client. The onboarding team collects and checks "
                    "the documents. A partner makes every acceptance decision.")
    d.add_heading("2. Required documents for a W.L.L.", 1)
    for s in ["Commercial license, valid on the day of the check.",
              "Articles of association.",
              "Shareholder register.",
              "ID copy for every person who is a shareholder, an ultimate beneficial owner or an authorized signatory.",
              "Authorized signatory list.",
              "For every company shareholder: its registration certificate and its own shareholder list."]:
        d.add_paragraph(s, style="List Number")
    d.add_heading("3. Expiry rule", 1)
    d.add_paragraph("Flag any document that has expired, or that expires within 60 days of the check. An expired document "
                    "counts as missing until the client sends a valid copy.")
    d.add_heading("4. High-risk indicators", 1)
    for s in ["(a) Ownership through a company registered outside Kuwait.",
              "(b) A politically exposed person (PEP): for example a minister, a member of parliament or of a municipal council, "
              "now or in the last five years, or a close family member of one.",
              "(c) A cash-intensive business.",
              "(d) A sector listed in Appendix A.",
              "(e) Documents that do not match each other, for example different company names or numbers."]:
        d.add_paragraph(s)
    d.add_heading("5. Escalation", 1)
    d.add_paragraph("Any high-risk indicator needs enhanced due diligence and written partner approval before the firm accepts "
                    "the client. Ultimate beneficial owners are people who own 25% or more, directly or through a company.")
    d.add_heading("Appendix A · High-risk sectors", 1)
    for s in ["Money exchange", "Precious metals and stones", "Real estate brokerage", "Used car trading"]:
        d.add_paragraph(s, style="List Bullet")
    d.save(os.path.join(OUT, "mirqab-client-acceptance-policy.docx"))

    d = doc_base("Materiality Memo · Abdali Foods Co. K.S.C.C.", "Audit of the year ended 31 December 2025 · Mirqab & Co. · Fictional")
    t = d.add_table(rows=0, cols=2)
    t.style = "Light Grid Accent 1"
    for k, v in [("Benchmark", "Profit before tax, FY2025 draft"), ("Overall materiality", "KWD 60,000"),
                 ("Performance materiality", "KWD 45,000 (75% of overall)"), ("Clearly trivial threshold", "KWD 3,000"),
                 ("Year end", "31 December 2025")]:
        r = t.add_row().cells
        r[0].text, r[1].text = k, v
    d.add_heading("Review threshold for trial balance movements", 1)
    d.add_paragraph("Flag an account for review only if the movement from FY2024 to FY2025 passes BOTH tests:")
    d.add_paragraph("Test 1: the movement is more than 10% of the FY2024 balance.", style="List Bullet")
    d.add_paragraph("Test 2: the movement is more than KWD 45,000 (performance materiality).", style="List Bullet")
    d.add_paragraph("An account that is new (zero in FY2024) or closed (zero in FY2025) is flagged if its balance is more than KWD 45,000.")
    d.add_paragraph("Prepared by: audit senior · Reviewed by: audit manager (fictional)")
    d.save(os.path.join(OUT, "mirqab-materiality-memo-abdali.docx"))

    d = doc_base("Field notes · Abdali Foods audit", "Rough notes from fieldwork, week 2 · not reviewed · Fictional")
    for s in ["PO approval: tested 25 purchases. 4 POs approved AFTER the supplier invoice date. Purchasing manager says these were "
              "urgent orders. No written policy for urgent orders.",
              "Supplier master data: 2 changes to supplier bank accounts in October. Both made by Rashed (AP clerk), who also processes "
              "payments. No second person reviews the changes. No call-back to the supplier to confirm.",
              "Inventory count 31 Dec at the Shuwaikh warehouse: count sheets not signed by the counters (12 of 12 sheets unsigned). "
              "Recounts were done but not documented.",
              "Petty cash: small difference at the count. Need the amount from Dana.",
              "Client asked to move the closing meeting to Thursday at 10:00."]:
        d.add_paragraph(s, style="List Bullet")
    d.save(os.path.join(OUT, "abdali-field-notes.docx"))

    d = doc_base("Management Letter Point · Format", "Mirqab & Co. · How we write each point · Fictional")
    d.add_heading("Order of each point", 1)
    for s in ["Title: five to eight words, names the control.", "Observation: what we found, with numbers.",
              "Risk rating: High, Medium or Low.", "Risk: what could go wrong for the client.",
              "Recommendation: one or two actions the client can take.",
              "Management response: always [To be completed by management]."]:
        d.add_paragraph(s, style="List Number")
    d.add_heading("Risk ratings", 1)
    t = d.add_table(rows=0, cols=2)
    t.style = "Light Grid Accent 1"
    for k, v in [("High", "Could lead to a material error, a loss or fraud."), ("Medium", "Weakens a key control."),
                 ("Low", "Good practice. No direct risk of error.")]:
        r = t.add_row().cells
        r[0].text, r[1].text = k, v
    d.add_heading("Style rules", 1)
    for s in ["Facts only. Neutral tone. No blame.", "Never name a person. Use the role.",
              "One finding per point."]:
        d.add_paragraph(s, style="List Bullet")
    d.add_heading("Example (not from a real client)", 1)
    for k, v in [("Title", "Bank reconciliations not reviewed"),
                 ("Observation", "For 3 of 12 months, the bank reconciliation had no reviewer's signature."),
                 ("Risk rating", "Medium"), ("Risk", "Errors in the cash balance may not be found in time."),
                 ("Recommendation", "A second person reviews and signs each monthly reconciliation."),
                 ("Management response", "[To be completed by management]")]:
        p = d.add_paragraph()
        p.add_run(k + ": ").bold = True
        p.add_run(v)
    d.save(os.path.join(OUT, "mirqab-management-letter-template.docx"))


# ───────────────────────── XLSX ─────────────────────────
TB = [  # account, type, FY2025, FY2024  (debit positive, credit negative)
    ("Cash at bank", "Asset", 412300.000, 687150.000),
    ("Trade receivables", "Asset", 1845600.000, 1337400.000),
    ("Allowance for doubtful debts", "Asset", -92280.000, -88500.000),
    ("Inventory", "Asset", 1226700.000, 1005500.000),
    ("Provision for slow-moving inventory", "Asset", 0.000, -60000.000),
    ("Prepayments", "Asset", 48900.000, 45100.000),
    ("Property, plant and equipment", "Asset", 6072250.000, 6181150.000),
    ("Accumulated depreciation", "Asset", -1410000.000, -1290000.000),
    ("Suspense account", "Asset", 52300.000, 0.000),
    ("Trade payables", "Liability", -965400.000, -912800.000),
    ("Accrued expenses", "Liability", -184200.000, -171900.000),
    ("Due to related party", "Liability", -450000.000, -400000.000),
    ("Bank loan", "Liability", -1350000.000, -1450000.000),
    ("Share capital", "Equity", -2000000.000, -2000000.000),
    ("Statutory reserve", "Equity", -420000.000, -380000.000),
    ("Retained earnings (opening)", "Equity", -1863100.000, -1700000.000),
    ("Revenue", "Income", -7840000.000, -7260000.000),
    ("Other income", "Income", -18200.000, -15600.000),
    ("Cost of sales", "Expense", 5410000.000, 5008000.000),
    ("Salaries and staff costs", "Expense", 980000.000, 935000.000),
    ("Rent", "Expense", 240000.000, 240000.000),
    ("Marketing", "Expense", 84950.000, 54800.000),
    ("Depreciation", "Expense", 120000.000, 118000.000),
    ("Bad debt expense", "Expense", 3780.000, 12400.000),
    ("Finance costs", "Expense", 96400.000, 104300.000),
]


def tb_rows():
    rows = []
    s25 = sum(r[2] for r in TB if r[2] is not None)
    s24 = sum(r[3] for r in TB if r[3] is not None)
    assert abs(s25) < 0.0005 and abs(s24) < 0.0005, (s25, s24)
    return [tuple(r) for r in TB]


def make_xlsx():
    thin = Side(style="thin", color="C8D2E3")
    head = PatternFill("solid", fgColor="00112F")
    wb = Workbook()
    ws = wb.active
    ws.title = "Trial balance"
    ws.append(["Abdali Foods Co. K.S.C.C. · Trial balance · KWD · " + TAG])
    ws.append(["Account", "Type", "FY2025 Debit", "FY2025 Credit", "FY2024 Debit", "FY2024 Credit"])
    for c in ws[2]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head
    rows = tb_rows()
    for a, t, v25, v24 in rows:
        ws.append([a, t, v25 if v25 > 0 else None, -v25 if v25 < 0 else None,
                   v24 if v24 > 0 else None, -v24 if v24 < 0 else None])
    n = ws.max_row
    ws.append(["Total", "", f"=SUM(C3:C{n})", f"=SUM(D3:D{n})", f"=SUM(E3:E{n})", f"=SUM(F3:F{n})"])
    for c in ws[ws.max_row]:
        c.font = Font(bold=True)
    for row in ws.iter_rows(min_row=3, min_col=3, max_col=6):
        for c in row:
            c.number_format = "#,##0.000"
    ws.column_dimensions["A"].width = 38
    ws.column_dimensions["B"].width = 11
    for col in "CDEF":
        ws.column_dimensions[col].width = 16
    ws.freeze_panes = "A3"
    wb.save(os.path.join(OUT, "abdali-trial-balance-fy2025.xlsx"))

    wb = Workbook()
    ws = wb.active
    ws.title = "Sample"
    ws.append(["Invoice number", "Date", "Customer", "Amount (KWD)", "Period"])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head
    for r in [("INV-25-1142", "05/11/2025", "Qurtuba Fresh Market", 8215.500, "FY2025"),
              ("INV-25-1150", "12/11/2025", "Hawally Star Restaurants", 3480.000, "FY2025"),
              ("INV-25-1163", "20/11/2025", "Bayan Catering Co.", 15900.750, "FY2025"),
              ("INV-25-1187", "02/12/2025", "Golden Dune Hotels", 12540.000, "FY2025"),
              ("INV-25-1196", "18/12/2025", "Blue Gulf Supermarkets", 6730.250, "FY2025"),
              ("INV-25-1203", "28/12/2025", "Nakheel Bakery", 9120.000, "FY2025")]:
        ws.append(list(r))
    for row in ws.iter_rows(min_row=2, min_col=4, max_col=4):
        for c in row:
            c.number_format = "#,##0.000"
    ws.append([])
    ws.append(["Abdali Foods Co. K.S.C.C. · Sales listing sample, year ended 31 Dec 2025 · " + TAG])
    for col, wd in zip("ABCDE", (16, 12, 30, 16, 10)):
        ws.column_dimensions[col].width = wd
    wb.save(os.path.join(OUT, "abdali-sales-listing-sample.xlsx"))


if __name__ == "__main__":
    make_pdfs()
    make_docs()
    make_xlsx()
    rows = tb_rows()
    print("TB balanced:", round(sum(r[2] for r in rows), 3), round(sum(r[3] for r in rows), 3))
    for a, t, v25, v24 in rows:
        mv = v25 - v24
        pct = (mv / abs(v24) * 100) if v24 else None
        both = (pct is None and abs(v25 or v24) > 45000) or (pct is not None and abs(pct) > 10 and abs(mv) > 45000)
        print(f"{a:38s} {v25:>15,.3f} {v24:>15,.3f} {mv:>13,.3f} {('%.1f%%' % pct) if pct is not None else 'n/a':>8} {'FLAG' if both else ''}")
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)))
