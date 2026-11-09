# -*- coding: utf-8 -*-
"""Engine core: finds the kit, reads every setting from it, and holds the helpers every other engine file shares.

The engine never names a workshop. Everything below comes from the kit folder (default: ../kit next to this folder,
or the folder named in the WK_KIT environment variable): content.py, content_demos.py, data.py, build_deck.py,
gen_files.py and the client logo. SCHEMA.md lists every field and its default.
"""
import os, sys, re, html, base64, json

ENGINE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ENGINE, "assets")
KIT_DIR = os.path.abspath(os.environ.get("WK_KIT") or os.path.join(ENGINE, "..", "kit"))
SRC = os.path.dirname(KIT_DIR)                      # _source/
ROOT = os.path.dirname(SRC)                         # the repo root (public/, vercel.json, package.json)
FILES_DIR = os.path.join(SRC, "files")              # sample files written by the kit's gen_files.py
RECORD_DIR = os.path.join(SRC, "kit-pages")         # what the kit asked for, slide by slide (the fidelity source)
SURVEY_DIR = os.path.join(SRC, "surveys")
for _f in ("content.py", "content_demos.py", "build_deck.py"):
    if not os.path.exists(os.path.join(KIT_DIR, _f)):
        sys.exit(f"engine: the kit folder {KIT_DIR} has no {_f}. Put the kit in _source/kit/ (or set WK_KIT) and run build.sh again.")
if KIT_DIR not in sys.path: sys.path.insert(0, KIT_DIR)
if ENGINE not in sys.path: sys.path.insert(1, ENGINE)

import content as C            # noqa: E402  (the kit)
import content_demos as CD     # noqa: E402

def rd(p): return open(p, encoding="utf-8").read()
def asset(*p): return rd(os.path.join(ASSETS, *p))
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
e = lambda s: html.escape(str(s), quote=True)
def strip(x): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(x)).replace("&nbsp;", " ")).strip()
def hl(s):
    """Kit text marks the highlight with <span class="hl">; the deck kit draws it as <em>."""
    return re.sub(r'<span class="?hl"?>(.*?)</span>', r'<em>\1</em>', str(s), flags=re.S)
def opt(name, default=None): return getattr(C, name, default)

# ------------------------------------------------------------------ names: every page, asset and package name comes from the kit's CODE
CODE = C.CODE
PFX = f"coded-{CODE}"
def P(name): return f"{PFX}-{name}"
HUB = PFX
DAYS = tuple(sorted(C.DAYS))
NDAYS = len(DAYS)
FIRST, LAST = DAYS[0], DAYS[-1]
STAFF = "staff"
TITLE = C.TITLE
BRAND = opt("BRAND", "CODED")

# ------------------------------------------------------------------ the branch: an AI tool workshop or a workshop without one
TOOL_MODE = opt("TOOL_MODE", "ai")
assert TOOL_MODE in ("ai", "none"), f"content.py TOOL_MODE must be 'ai' or 'none', not {TOOL_MODE!r}"
AI = TOOL_MODE == "ai"
SHEET = ({"name": "Prompt sheet", "slug": "prompt-sheet", "nav": "Prompts", "what": "prompts"} if AI else
         {"name": "Task sheet", "slug": "task-sheet", "nav": "Tasks", "what": "tasks"})
SHEET.update(opt("SHEET", {}))
_card = ({"name": "Safe-use card", "slug": "safe-use-card"} if AI else {"name": "Verify card", "slug": "verify-card"})
CARD = dict(_card, **opt("CARD", {}))
def dayp(d): return P(f"day-{d}")
def deckp(d): return P(f"day-{d}-deck")
def sheetp(d): return P(f"{SHEET['slug']}-day-{d}")
def labp(d): return P(f"lab-day-{d}")
def cardp(): return P(CARD["slug"])
LABS = opt("LABS", {}) or {}
def practp(): return P("practice-questions")
PRACTICE = opt("PRACTICE", None) or None   # optional: a public practice-questions page (scored in the browser, never reported)
SEGMENTS = opt("SEGMENTS", {}) or {}       # optional: the minutes inside each session, shown on the lesson plan

# ------------------------------------------------------------------ the client: None for a CODED-only workshop
CLIENT = opt("CLIENT")
if CLIENT is not None:
    for k in ("name", "short", "primary"):
        assert CLIENT.get(k), f"content.py CLIENT needs '{k}' (or set CLIENT = None for a CODED-only workshop)"
CLIENT_LOGO = None
if CLIENT and CLIENT.get("logo"):
    CLIENT_LOGO = os.path.join(KIT_DIR, CLIENT["logo"])
    assert os.path.exists(CLIENT_LOGO), f"client logo {CLIENT_LOGO} not found in the kit folder"
ORG = (f"CODED × {CLIENT['short']}" if CLIENT else "CODED")

def theme(css):
    """The CODED theme, mixed with the client colors when there is a client (site-kit/tools/mix_theme.py)."""
    if not CLIENT: return css
    import mix_theme
    return mix_theme.mix(css, CLIENT["primary"], CLIENT.get("secondary"), CLIENT.get("light"))[0]
def accent_text():
    """The accent text color on the navy after the mix (CODED soft blue when there is no client)."""
    if not CLIENT: return "#6F9CE8"
    import mix_theme
    return mix_theme.mix("#6F9CE8", CLIENT["primary"], CLIENT.get("secondary"), CLIENT.get("light"))[2]

# ------------------------------------------------------------------ fonts (Manrope + Space Mono, self-hosted, SIL OFL)
FONTS = os.path.join(ASSETS, "fonts")
FONT_FILES = {"font-manrope.woff2": "manrope-latin-variable.woff2", "font-space-mono-400.woff2": "space-mono-latin-400-normal.woff2",
              "font-space-mono-700.woff2": "space-mono-latin-700-normal.woff2"}
def font_css_embedded():
    s = "/* Manrope + Space Mono, embedded so the decks open offline (SIL OFL) */\n"
    s += f"@font-face{{font-family:'Manrope';font-style:normal;font-weight:200 800;font-display:swap;src:url(data:font/woff2;base64,{b64(os.path.join(FONTS, FONT_FILES['font-manrope.woff2']))}) format('woff2')}}\n"
    for w in (400, 700):
        s += f"@font-face{{font-family:'Space Mono';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b64(os.path.join(FONTS, FONT_FILES[f'font-space-mono-{w}.woff2']))}) format('woff2')}}\n"
    return s

# ------------------------------------------------------------------ visible-text rules: no em dashes, American spelling
SPELL = (("summarise", "summarize"), ("Summarise", "Summarize"), ("organisation", "organization"), ("Organisation", "Organization"),
         ("licence", "license"), ("favour", "favor"), ("recognise", "recognize"), ("Recognise", "Recognize"), ("analyse", "analyze"), ("prioritise", "prioritize"))
def fix_text(t):
    t = t.replace(" — ", ": ").replace("—", "-")
    for a, b in SPELL: t = t.replace(a, b)
    return t
def text_rules(h):
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', h, flags=re.S)
    return "".join(p if p.startswith(("<script", "<style")) else re.sub(r'>([^<]+)<', lambda m: '>' + fix_text(m.group(1)) + '<', p) for p in parts)

# ------------------------------------------------------------------ MAP tests and the final survey (CODED portal forms, from the kit)
FORMS = C.FORMS                     # {"pre": {...}, "post": {...}, "survey": {...}}: name, when, url (and id, slug)
FORM_DAY = opt("FORM_DAY") or {FIRST: ["pre"], LAST: ["post", "survey"]}
MAP_MIN = opt("MAP_MIN", 10)
def qr_svg(url, cls="wk-qr-code", label=""):
    """QR code as inline SVG: CODED navy on white with a quiet zone (build.md section 11)."""
    import segno
    s = segno.make(url, error="m").svg_inline(dark="#00112F", light="#ffffff", border=3, omitsize=True)
    return s.replace('class="segno"', f'class="{cls}" role="img" aria-label="QR code: {e(label or url)}"', 1)

# ------------------------------------------------------------------ the kit's demos and tasks, with every optional field filled
def _norm(did, v):
    v.setdefault("files", []); v.setdefault("stretch", []); v.setdefault("stretch_prompts", []); v.setdefault("prompts", [])
    v.setdefault("templates", []); v.setdefault("setup", []); v.setdefault("backup", []); v.setdefault("answer", [])
    v.setdefault("kind", "task" if v.get("hands_on") else "demo")
    v.setdefault("solo", "in pairs"); v.setdefault("minutes", 10)
    for k in ("expected", "say", "point", "fallback", "hint"): v.setdefault(k, "")
    v.setdefault("card", ("Task " if v.get("hands_on") else "Demo ") + v["skill"])
    v.setdefault("deliverable", "")
    return v
DEMOS = {k: _norm(k, v) for k, v in CD.DEMOS.items()}
BLOCK = CD.BLOCK
ALL_FILES = list(getattr(CD, "ALL_FILES", []))
def day_demos(d): return [(k, v) for k, v in DEMOS.items() if v["day"] == d]
def task_steps(v): return [x for x in v["setup"] if not x.startswith("[T]")]

# ------------------------------------------------------------------ answer and backup blocks (h, p, ul, ol, table, note, sources)
_TAG = re.compile(r"<(?!/?(?:b|i|em|strong|code|br|span|small|a|sup|sub|div|ul|ol|li|p)\b)")
def _lt(x): return _TAG.sub("&lt;", str(x))
def blocks_html(blocks):
    out = []
    for t, v in blocks:
        if t == "h": out.append(f'<h4 class="bk-h">{v}</h4>')
        elif t == "p": out.append(f'<p class="bk-p">{v}</p>')
        elif t == "note": out.append(f'<div class="bk-note">{v}</div>')
        elif t in ("ul", "ol"): out.append(f'<{t} class="bk-list">' + "".join(f"<li>{_lt(x)}</li>" for x in v) + f"</{t}>")
        elif t == "table":
            h = "".join(f"<th>{_lt(x)}</th>" for x in v[0])
            rows = "".join("<tr>" + "".join(f"<td>{_lt(x)}</td>" for x in r) + "</tr>" for r in v[1:])
            out.append(f'<div class="bk-tw"><table class="bk-table"><thead><tr>{h}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif t == "sources":
            S = opt("SOURCES", {})
            out.append('<ul class="bk-list">' + "".join(f'<li><a href="{S[k][1]}" target="_blank" rel="noopener">{e(S[k][0])}</a></li>' for k in v) + "</ul>")
        else:
            raise ValueError(f"unknown block type {t!r} (use h, p, ul, ol, table, note or sources)")
    return "\n".join(out)

def minutes(span):
    a, z = span.split("-"); return (int(z[:2]) * 60 + int(z[3:])) - (int(a[:2]) * 60 + int(a[3:]))

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
