"""Mix the CODED theme with a client brand (a copy of site-kit/tools/mix_theme.py, used by the engine at build time).

CODED keeps: the navy ground and cards, the glass panels, the 56 px grid, the layout, the fonts and the CODED logo.
The client takes:
  - fills, buttons, highlights and the hero word        CODED blue  #2F74D6 -> client primary
  - accent text and labels                              CODED soft  #6F9CE8 -> light tint of the primary (4.5:1 on the navy)
  - the light and pale blues (no light blue left)        #9FC0F5 / #BCD3F7  -> lighter tints of the primary
  - the royal blue, when the client has a second color  CODED royal #004AA3 -> client secondary
  - the six background glows: primary at top right and upper left, its tint at lower right, secondary (or royal) at left, bottom, right
Green, amber and red keep their meaning.

Usage: python3 mix_theme.py <coded css or html> <out> --primary "#DA1F27" [--secondary "#00417D"] [--light "#F0575E"]
"""
import re, sys, argparse

def hx(c): c = c.lstrip("#"); return tuple(int(c[i:i+2], 16) for i in (0, 2, 4))
def to_hex(t): return "#%02X%02X%02X" % tuple(max(0, min(255, round(v))) for v in t)
def rgb(t): return ",".join(str(max(0, min(255, round(v)))) for v in t)
def lum(t):
    def ch(v):
        v /= 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in t); return 0.2126 * r + 0.7152 * g + 0.0722 * b
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def tint(t, k): return tuple(v + (255 - v) * k for v in t)
BASE = hx("#00112F")
VERBOSE = False
CARD_LIGHT = hx("#16294A")   # the lightest card a small text sits on (the top of the card gradient): text colors must pass 4.5:1 here too

def _rgba(css, old, new):
    return re.sub(r"rgba?\(" + old.replace(",", r"\s*,\s*") + r"(?=\s*[,)])", lambda m: m.group(0)[:m.group(0).index("(") + 1] + new, css)

def _text_tint(p, k):
    """The first tint of p, from k up, that reads at 4.5:1 on the navy base and on the lightest glass card."""
    t = tint(p, k)
    while (contrast(t, BASE) < 4.5 or contrast(t, CARD_LIGHT) < 4.5) and k < 0.95: k += 0.05; t = tint(p, k)
    return t, k

def mix(css, primary, secondary=None, light=None):
    p = hx(primary)
    if light: l, k = hx(light), 0.30
    else: l, k = _text_tint(p, 0.30)
    if contrast(l, BASE) < 4.5 or contrast(l, CARD_LIGHT) < 4.5:
        sys.exit(f"FAIL: the accent text {to_hex(l)} is {contrast(l, BASE):.2f}:1 on the navy and {contrast(l, CARD_LIGHT):.2f}:1 on glass; pass a lighter --light")
    l2, _ = _text_tint(p, max(0.55, k + 0.10)); l3, _ = _text_tint(p, max(0.70, k + 0.25))
    s = hx(secondary) if secondary else hx("#004AA3")
    # glows first (they are matched by their CODED values)
    m = re.search(r"body::before\{[^}]*\}", css, re.S)
    if m:
        blk = m.group(0)
        for old, new in [("rgba(47,116,214,.30)", f"rgba({rgb(p)},.26)"), ("rgba(0,74,163,.50)", f"rgba({rgb(s)},.55)"),
                         ("rgba(111,156,232,.10)", f"rgba({rgb(l)},.13)"), ("rgba(0,74,163,.42)", f"rgba({rgb(s)},.45)"),
                         ("rgba(111,156,232,.16)", f"rgba({rgb(p)},.22)"), ("rgba(0,74,163,.36)", f"rgba({rgb(s)},.38)")]:
            blk = blk.replace(old, new, 1)
        css = css.replace(m.group(0), blk)
    for old, new in [("#2F74D6", to_hex(p)), ("#6F9CE8", to_hex(l)), ("#9FC0F5", to_hex(l2)), ("#BCD3F7", to_hex(l3))]:
        css = re.sub(re.escape(old) + r"\b", new, css, flags=re.I)
    css = _rgba(css, "47,116,214", rgb(p)); css = _rgba(css, "111,156,232", rgb(l)); css = _rgba(css, "159,192,245", rgb(l2))
    if secondary:
        css = re.sub(r"#004AA3\b", to_hex(s), css, flags=re.I); css = _rgba(css, "0,74,163", rgb(s))
    # A dark client color works as a fill but disappears as a line, an icon or small text on the navy (a deep maroon is 1.5:1).
    # Below 3:1, every foreground use of the primary takes the accent tint instead; fills and backgrounds keep the primary.
    swapped = 0
    if contrast(p, BASE) < 3.0:
        P_, L_ = re.escape(to_hex(p)), to_hex(l)
        fg = r"((?<![-\w])(?:color|stroke|fill|outline-color|border(?:-(?:top|right|bottom|left))?-color|text-decoration-color|caret-color)\s*:\s*)" + P_ + r"\b"
        css, n1 = re.subn(fg, lambda m: m.group(1) + L_, css, flags=re.I)
        bd = r"((?<![-\w])(?:border|outline|border-(?:top|right|bottom|left))\s*:\s*[^;{}]*?)" + P_ + r"\b"
        css, n2 = re.subn(bd, lambda m: m.group(1) + L_, css, flags=re.I)
        css, n3 = re.subn(r"((?:stroke|fill)=\")" + P_ + r"\b", lambda m: m.group(1) + L_, css, flags=re.I)
        swapped = n1 + n2 + n3
        if VERBOSE: sys.stderr.write(f"note: {to_hex(p)} is {contrast(p, BASE):.2f}:1 on the navy, so {swapped} line, icon and text uses now take {L_}; "
                         "check the engine's inline CSS and SVG strings the same way (run qa.cjs)\n")
    if contrast(p, (255, 255, 255)) < 4.5:
        sys.exit(f"FAIL: white text on {to_hex(p)} is {contrast(p, (255, 255, 255)):.2f}:1. Use navy text on the client color "
                 "(set the button text to #00112F) and record it under Decisions, or pass a darker --primary")
    return css, to_hex(p), to_hex(l), to_hex(s)

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("src"); a.add_argument("out")
    a.add_argument("--primary", required=True); a.add_argument("--secondary"); a.add_argument("--light")
    o = a.parse_args()
    css, P, L, S = mix(open(o.src, encoding="utf-8").read(), o.primary, o.secondary, o.light)
    open(o.out, "w", encoding="utf-8").write(css)
    print(f"mixed: fills {P}, accent text {L} ({contrast(hx(L), BASE):.2f}:1 on navy), royal -> {S}")
