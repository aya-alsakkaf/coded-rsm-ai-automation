# -*- coding: utf-8 -*-
"""Public pages in the CODED workshop template (site-kit/theme/coded-site.css, mixed with the client colors when there is one):
hub, one page per day, one sheet per day (prompt sheet with an AI tool, task sheet without), one browser lab per day (when the
kit has LABS), cheat sheet, the card page (safe-use card or verify card), take-home guide, 404, index and robots.txt.
Every word comes from the kit. Run deck.py first: the hub counts the slides.

    python3 pages.py OUTDIR
"""
import os, re, sys, glob, shutil, hashlib, json
import wk
from wk import C, e, P, HUB, DAYS, dayp, deckp, sheetp, labp, cardp, opt, day_demos, DEMOS, BLOCK, ALL_FILES

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(wk.ROOT, "public")
HB = opt("HUB", {})

# ------------------------------------------------------------------ icons
def svg(body, s=16, w=2): return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
I = {
 "cal": '<rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3 2"/>',
 "pin": '<path d="M21 10.5c0 6.5-9 12.5-9 12.5s-9-6-9-12.5a9 9 0 0118 0z"/><circle cx="12" cy="10.5" r="3"/>',
 "cup": '<path d="M4 9h12v5a5 5 0 01-5 5H9a5 5 0 01-5-5z"/><path d="M16 10h1.5a2.5 2.5 0 010 5H16"/>',
 "check": '<path d="M4 12l5 5L20 6"/>',
 "slides": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M4 16V5a1 1 0 011-1h11"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>',
 "sheet": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M10 3v18"/>',
 "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h6M9 16h6"/>',
 "grid": '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
 "out": '<path d="M7 17L17 7M9 7h8v8"/>',
 "dl": '<path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M5 21h14"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
 "dash": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M7 14v-3M12 14V8M17 14v-5"/>',
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "scale": '<path d="M12 3v18M5 21h14M6 7h12M6 7l-3 7h6zM18 7l-3 7h6z"/>',
 "flask": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 002 3h10a2 2 0 002-3l-5-9V3"/><path d="M7.5 15h9"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
}
def ico(n, s=16, w=2): return svg(I.get(n, I["doc"]), s, w)
def kind_icon(f):
    x = f.rsplit(".", 1)[-1]
    return {"xlsx": "sheet", "csv": "sheet", "eml": "mail"}.get(x, "doc")

# ------------------------------------------------------------------ page shell
def lockup(cls):
    c = f'<img class="coded-logo" src="{P("coded-logo.png")}" alt="CODED" width="320" height="120">'
    if wk.CLIENT and wk.CLIENT_LOGO:
        c += f'<span class="x">×</span><img class="partner-logo" src="{P("client-logo.png")}" alt="{e(wk.CLIENT["name"])}" width="192" height="192">'
    return f'<span class="{cls}">{c}</span>'
def head(title, desc):
    t = f"{title} · {C.TITLE} · {wk.ORG}" if title else f"{C.TITLE} · {wk.ORG}"
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(t)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#00112F">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{P("favicon.png")}" type="image/png">
<link rel="apple-touch-icon" href="{P("favicon.png")}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(t)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:site_name" content="{e(wk.BRAND)} · {e(C.TITLE)}">
<link rel="stylesheet" href="{P("site.css")}">
</head><body>
'''
REVEAL_JS = """<script>(function(){var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function fmt(n,d,g){var s=n.toFixed(d);if(g){var p=s.split('.');p[0]=p[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,',');s=p.join('.');}return s}
function count(el){if(el.dataset.done||RM)return;el.dataset.done=1;var t=parseFloat(el.dataset.count),d=+(el.dataset.dec||0),pre=el.dataset.prefix||'',suf=el.dataset.suffix||'',g=el.dataset.group==='1',st=performance.now();
  function tick(now){var p=Math.min(1,(now-st)/900),e=1-Math.pow(1-p,3);el.textContent=pre+fmt(t*e,d,g)+suf;if(p<1)requestAnimationFrame(tick)}requestAnimationFrame(tick)}
var els=[].slice.call(document.querySelectorAll('.rvl,[data-count]'));
if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('on');count(e)});return}
var t0=performance.now();var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){if(performance.now()-t0<900)x.target.classList.add('now');x.target.classList.add('on');if(x.target.dataset.count)count(x.target);io.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'});
els.forEach(function(e){if(e.getBoundingClientRect().top<innerHeight*1.6){e.classList.add('now','on');if(e.dataset.count)count(e)}else io.observe(e)});})();</script>"""
COPY_JS = """<script>document.addEventListener('click',function(e){var b=e.target.closest('[data-copy]');if(!b)return;var t=document.getElementById(b.getAttribute('data-copy'));if(!t)return;var txt=t.innerText;
function done(ok){b.textContent=ok?'COPIED':'SELECT';if(ok)b.classList.add('done');setTimeout(function(){b.textContent='COPY';b.classList.remove('done');},1500);}
function fb(){var ta=document.createElement('textarea');ta.value=txt;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();var ok=false;try{ok=document.execCommand('copy');}catch(x){}document.body.removeChild(ta);done(ok);}
if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(txt).then(function(){done(true);},fb);else fb();});</script>"""
TOPBAR_H_JS = """<script>(function(){var b=document.querySelector('main > .wrap:first-child');if(!b)return;function s(){document.documentElement.style.setProperty('--topbar-h',b.offsetHeight+'px')}s();addEventListener('resize',s);})();</script>"""

def topbar(active):
    sd = int(active[1:]) if str(active).startswith("p") and str(active)[1:].isdigit() else DAYS[0]
    tabs = [(f"Day {d}", dayp(d)) for d in DAYS] + [(wk.SHEET["nav"], sheetp(sd)), ("Cheat sheet", P("cheat-sheet"))]
    nav = "".join(f'<a href="{h}.html"' + (' class=on aria-current=page' if (active == n or (str(active).startswith("p") and n == wk.SHEET["nav"])) else "") + f">{e(n)}</a>" for n, h in tabs)
    both = "both days" if wk.NDAYS == 2 else f"all {wk.NDAYS} days"
    return (f'<div class="wrap"><div class="topbar"><a class="back" href="{HUB}.html"><span class="ar">←</span> {e(C.TITLE)} · {both}</a>'
            f'<nav class="daynav" aria-label="Pages">{nav}</nav></div></div>')
def dhero(hd, pill, h1, lede, meta):
    m = "".join(f"<span>{ico(i)} {t}</span>" for i, t in meta)
    return (f'<div class="wrap hero-wrap"><div class="d-hero h-d{(hd - 1) % 3 + 1}"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span> {pill}</span>'
            f'<div class="d-logos">{lockup("lk")}</div></div><h1>{h1}</h1><p class="lede">{lede}</p><div class="d-meta">{m}</div></div></div>')
def foot_mini():
    return (f'<footer class="foot-mini"><div class="wrap"><div class="foot-row"><a class="f-lockup" href="{HUB}.html" aria-label="{e(C.TITLE)} home">'
            f'{lockup("lk")}</a><span class="copy">© {opt("YEAR", 2026)} {e(wk.ORG)} · {e(C.SAMPLE_NOTE)}</span></div></div></footer>')
def res(href, nm, tag, icon="list", dl=False):
    d = f' download="{e(href)}"' if dl else ""
    return f'<a class="res" href="{href}"{d}><span class="res-ic">{ico(icon, 18)}</span><span class="res-nm">{e(nm)}</span><span class="res-tag">{tag}</span>{ico("dl" if dl else "out", 13)}</a>'
def cta(icon, h, p, href, btn, ghost=False):
    return (f'<section class="panel cta-panel"><div class="cta-ico">{ico(icon, 22)}</div><h3>{h}</h3><p>{p}</p>'
            f'<a class="slides-btn{" ghost" if ghost else ""}" href="{href}"><span>{btn}</span> <span class="ar">→</span></a></section>')
def map_slot(k):
    m = wk.FORMS[k]
    return (f'<div class="map-slot map-slot--live"><div class="map-qr" aria-hidden="true">{wk.qr_svg(m["url"], label=m["name"])}</div>'
            f'<div class="map-txt"><b>{e(m["name"])}</b><small>{e(m["when"])}</small></div>'
            f'<a class="go" href="{e(m["url"])}" target="_blank" rel="noopener">Open {ico("out", 13)}</a></div>')
def page(title, desc, body, js=""):
    return wk.text_rules(head(title, desc) + body + REVEAL_JS + js + "</body></html>\n")
def both(): return "Both days" if wk.NDAYS == 2 else f"All {wk.NDAYS} days"

# ------------------------------------------------------------------ 404 (Vercel serves it for any unknown address, so links are root-absolute)
def not_found():
    links = "".join(res(f"{dayp(d)}.html", f"Day {d} · {C.DAYS[d]['title']}", f"Day {d}") for d in DAYS)
    links += res(f"{HUB}.html", both(), "Workshop", "home")
    body = ('<main>' + topbar(None) + '<div class="wrap hero-wrap"><div class="d-hero h-d1"><div class="d-hero-top"><span class="cat-pill"><span class="dot"></span> 404</span>'
            f'<div class="d-logos">{lockup("lk")}</div></div><h1>This page is not here.</h1><p class="lede">The address may be old or mistyped. Pick a page below.</p></div></div>'
            f'<div class="wrap"><section class="panel" style="margin:28px 0 60px"><h2>Go to</h2><div class="res-list">{links}</div></section></div></main>' + foot_mini())
    h = page("Page not found", f"This page is not here. Go to {C.TITLE}.", body)
    return re.sub(rf'(href|src)="({re.escape(wk.PFX)}[^"]*)"', r'\1="/\2"', h)

# ------------------------------------------------------------------ hub
def hero_scene():
    """The days as stations on one path, with people walking it (drawn for any number of days)."""
    n = wk.NDAYS; W_ = 910
    path = "M40 150 C 200 150, 250 92, 470 92 S 720 150, 870 150"
    xs = [round(150 + (W_ - 300) * i / max(1, n - 1)) if n > 1 else W_ // 2 for i in range(n)]
    nodes = "".join(f'<g class="dtlight" style="--dur:10s;--delay:{1.2 + 3 * i}s"><circle cx="{x}" cy="120" r="22" fill="rgba(47,116,214,.16)" stroke="#6F9CE8" stroke-width="2.5"></circle>'
                    f'<text x="{x}" y="125" class="viz-lbl hot" text-anchor="middle" font-size="14">{d}</text><text x="{x}" y="170" class="viz-lbl" text-anchor="middle" font-size="13">{e(C.DAYS[d].get("cat", C.DAYS[d]["title"]))}</text></g>' for i, (d, x) in enumerate(zip(DAYS, xs)))
    walker = lambda col, dur, begin: (f'<g><g class="dtstep"><g transform="translate(0,-30) scale(0.55)"><circle r="11" fill="none" stroke="{col}" stroke-width="2.5"></circle>'
                                      f'<path d="M0 13 v26 M0 19 l-13 9 M0 19 l13 9 M0 39 l-11 18 M0 39 l11 18" fill="none" stroke="{col}" stroke-width="2.5" stroke-linecap="round"></path></g></g>'
                                      f'<animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" rotate="0" path="{path}"></animateMotion></g>')
    tags = [C.DAYS[d].get("tag") for d in DAYS]
    tw = lambda t: max(140, round(len(t) * 7.1 + 26))
    tg = "".join(f'<g class="dtbob" style="--dur:{3.2 + .2 * i}s;--delay:{.5 * i}s"><rect x="{x - tw(t) / 2:g}" y="24" width="{tw(t)}" height="26" rx="13" fill="rgba(255,255,255,.06)" stroke="rgba(255,255,255,.18)" stroke-width="1.2"></rect>'
                 f'<text x="{x}" y="41" class="viz-lbl dim" text-anchor="middle" font-size="11">{e(t)}</text></g>' for i, (t, x) in enumerate(zip(tags, xs)) if t)
    desk = (f'<svg viewBox="0 0 910 210" class="viz hero-scene" aria-hidden="true" focusable="false"><path d="{path}" fill="none" stroke="rgba(255,255,255,.16)" stroke-width="2" stroke-linecap="round" class="dtdraw" style="--c:900;--dur:10s"></path>'
            f'{nodes}{walker("#6F9CE8", 13, 0)}{walker("#9FC0F5", 15, -5)}{walker("#A9B6C9", 14, -9)}{tg}</svg>')
    return f'<div class="hero-scene-wrap" aria-hidden="true">{desk}</div>'
def stat(n, label): return f'<div class="stat rvl"><b data-count="{n}" data-dec="0" data-prefix="" data-suffix="" data-group="0">{n}</b><span>{label}</span></div>'
def hub(nslides):
    tasks = sum(1 for v in DEMOS.values() if v.get("hands_on"))
    demos = sum(1 for v in DEMOS.values() if not v.get("hands_on"))
    strip_ = HB.get("stats") or [(wk.NDAYS, "days"), (nslides, "slides"), (tasks, "hands-on tasks"), (demos, "prompt demos" if wk.AI else "in-slide demos"),
                                 (len(ALL_FILES), "sample files"), (len(C.MAP), "MAP questions")]
    strip_html = "".join(stat(nslides if a is None else a, b) for a, b in strip_)
    cards = ""
    for d in DAYS:
        Dd = C.DAYS[d]
        lis = "".join(f"<li>{ico('check', 15, 2.5)} {x}</li>" for x in Dd.get("bullets", []))
        cards += (f'<article class="pcard rvl"><div class="phead h-d{(d - 1) % 3 + 1}"><span class="cat">{e(Dd.get("cat", "Day " + str(d)))}</span><span class="head-icon">{ico(Dd.get("icon", "doc"), 42, 1.5)}</span>'
                  f'<div class="head-meta"><span class="chip">{ico("cal", 13)} Day {d}</span><span class="chip">{ico("clock", 13)} {e(C.HOURS)}</span></div></div>'
                  f'<div class="pbody"><div class="kicker">Day {d:02d} · {e(C.DAYDATE[d])}</div><h3>{e(Dd["title"])}</h3><p class="pdesc">{e(Dd["sub"])}</p>'
                  f'<ul class="plist">{lis}</ul><a class="pbtn btn-d{(d - 1) % 3 + 1}" href="{dayp(d)}.html">Open day {d} <span class="arr">→</span></a></div></article>')
    outcomes = "".join(f'<li>{ico("check", 15, 2.5)}<span>{e(x)}</span></li>' for x in C.OUTCOMES)
    habit = "".join(f'<li>{ico("check", 15, 2.5)}<span><b>{e(a)}.</b> {e(b)}</span></li>' for a, b in HB.get("habit_list", []))
    files = "".join(f'<a class="ghost-btn file-btn" href="{f}" download>{ico(kind_icon(f), 16)} {e(f)}</a>' for f in ALL_FILES)
    hl1, hl2 = (HB.get("headline") or [C.TITLE, ""]) + [""] * (2 - len(HB.get("headline") or [C.TITLE, ""]))
    extra = "".join(f'''<section class="band"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">{e(eb)}</div><h2>{e(t)}</h2></div>
  <div><p>{p}</p>{('<ul class="leave">' + "".join(f'<li>{ico("check", 15, 2.5)}<span>{x}</span></li>' for x in lst) + "</ul>") if lst else ""}</div>
</div></section>''' for eb, t, p, lst in HB.get("bands", []))
    sheets = "".join(f'<a class="ghost-btn" href="{sheetp(d)}.html">{ico("copy")} Day {d} {e(wk.SHEET["what"])} <span class="arr">→</span></a>' for d in DAYS)
    labs = "".join(f'<a class="ghost-btn" href="{labp(d)}.html">{ico("flask")} Day {d} lab <span class="arr">→</span></a>' for d in DAYS if d in wk.LABS)
    labs += (f'<a class="ghost-btn" href="{wk.practp()}.html">{ico("check")} Practice questions <span class="arr">→</span></a>' if wk.PRACTICE else "")
    maps = "".join(map_slot(k) for k in ("pre", "post", "survey") if k in wk.FORMS)
    body = f'''<header class="hero">
  <div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div><div class="glow g4"></div>
  <div class="inner">
    <div class="pill"><span class="dot"></span> {e(wk.BRAND)} · Kuwait</div>
    <div class="lockup">{lockup("lk")}</div>
    <h1 class="headline">{e(hl1)}{"<br><span class=accent>" + e(hl2) + "</span>" if hl2 else ""}</h1>
    <p class="sub">{e(HB.get("sub", C.SUBTITLE))}</p>
    <div class="meta"><span>{ico("cal")} {e(C.DATES)}</span><span>{ico("clock")} {e(C.HOURS)}</span><span>{ico("pin")} {e(C.VENUE)}{(" · " + e(HB["meta"])) if HB.get("meta") else ""}</span></div>
    <a href="#program" class="cta">Explore the workshop <span class="arr">→</span></a>
  </div>
  {hero_scene()}
  <div class="scrollhint">the days ↓</div>
</header>
<main>
<section class="strip" aria-label="The workshop in numbers"><div class="wrap">{strip_html}</div></section>
<section class="programme" id="program"><div class="wrap">
  <div class="eyebrow">The workshop</div>
  <h2 class="sec-title">{e(HB.get("program_title", C.SUBTITLE))}</h2>
  <p class="sec-lead">{e(HB.get("program_lead", C.STORY))}</p>
  <div class="cards cards-{min(3, wk.NDAYS)}">{cards}</div>
</div></section>
<section class="band" id="outcomes"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">Outcomes</div><h2>What you will be able to do.</h2></div>
  <div><ul class="leave">{outcomes}</ul></div>
</div></section>
<section class="band" id="format"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">{e(HB.get("habit_eyebrow", "The habit"))}</div><h2>{e(HB.get("habit_title", C.THRU))}</h2></div>
  <div><p>{e(HB.get("habit_text", C.THRU))}</p><ul class="leave">{habit}</ul>
  <a class="ghost-btn" href="{cardp()}.html">{ico("shield")} {e(wk.CARD["name"])} <span class="arr">→</span></a></div>
</div></section>
{extra}
<section class="band" id="files"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">Sample files</div><h2>{e(HB.get("files_title", "The sample files."))}</h2></div>
  <div><p>{e(C.SAMPLE_NOTE)} Each card on the {e(wk.SHEET["name"].lower())}s links the file it needs.</p><div class="file-grid">{files}</div></div>
</div></section>
<section class="band" id="take-away"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">Take away</div><h2>Keep these after the workshop.</h2></div>
  <div><p>{e(HB.get("takeaway_text", ""))}</p>
  <a class="ghost-btn" href="{P("cheat-sheet")}.html">{ico("list")} Cheat sheet <span class="arr">→</span></a> <a class="ghost-btn" href="{cardp()}.html">{ico("shield")} {e(wk.CARD["name"])} <span class="arr">→</span></a> <a class="ghost-btn" href="{P("take-home-guide")}.html">{ico("home")} Take-home guide <span class="arr">→</span></a>
  <div class="sheet-links">{sheets}{labs}</div></div>
</div></section>
<section class="band" id="map"><div class="wrap band-grid">
  <div class="rvl"><div class="eyebrow">Before and after</div><h2>A short skills check, twice. Then the survey.</h2></div>
  <div><p>{e(HB.get("map_text", ""))}</p>
  <div class="map-list">{maps}</div></div>
</div></section>
</main>
<footer class="site-foot"><div class="wrap">
  <div class="foot-top">
    <div class="foot-brand"><div class="f-lockup">{lockup("lk")}</div>
      <p>{e(HB.get("about", C.TITLE))} {e(C.THRU)}</p></div>
    <div class="foot-cols">
      <div class="foot-col"><p class="fh">The days</p>{"".join(f'<a href="{dayp(d)}.html">Day {d} · {e(C.DAYS[d]["title"])}</a>' for d in DAYS)}</div>
      <div class="foot-col"><p class="fh">Take away</p><a href="{P("cheat-sheet")}.html">Cheat sheet</a><a href="{cardp()}.html">{e(wk.CARD["name"])}</a><a href="{P("take-home-guide")}.html">Take-home guide</a>{"".join(f'<a href="{sheetp(d)}.html">Day {d} {e(wk.SHEET["what"])}</a>' for d in DAYS)}</div>
      <div class="foot-col"><p class="fh">Connect</p><a href="https://coded.kw" target="_blank" rel="noopener">CODED</a>{(f'<a href="{e(wk.CLIENT["url"])}" target="_blank" rel="noopener">{e(wk.CLIENT["short"])}</a>') if wk.CLIENT and wk.CLIENT.get("url") else ""}</div>
    </div>
  </div>
  <div class="foot-divider"></div>
  <div class="foot-bottom"><span>© {opt("YEAR", 2026)} {e(wk.ORG)}.</span><span>{e(C.SAMPLE_NOTE)}</span></div>
</div></footer>
'''
    return page("", HB.get("description", C.SUBTITLE), body)

# ------------------------------------------------------------------ day pages
def day_path(d):
    blocks = [(t, n) for t, n, x in C.DAYS[d]["blocks"] if x]
    n = len(blocks); W_ = 900; x0, x1 = 40, 860
    xs = [x0 + (x1 - x0) * i / max(1, n - 1) for i in range(n)]
    path = f"M{x0} 70 L{x1} 70"
    nodes = "".join(f'<g class="dtlight" style="--dur:12s;--delay:{.4 + 10 * i / n:.2f}s"><circle cx="{x:.0f}" cy="70" r="15" fill="rgba(47,116,214,.16)" stroke="#6F9CE8" stroke-width="2"></circle>'
                    f'<text x="{x:.0f}" y="74.5" class="viz-lbl hot" text-anchor="middle" font-size="12">{i + 1}</text>'
                    f'<text x="{x:.0f}" y="{108 if i % 2 == 0 else 38}" class="viz-lbl dim" text-anchor="middle" font-size="11">{t[:5]}</text></g>' for i, ((t, nm), x) in enumerate(zip(blocks, xs)))
    walker = (f'<g><g class="dtstep"><g transform="translate(0,-14) scale(0.5)"><circle r="11" fill="none" stroke="#9FC0F5" stroke-width="2.5"></circle>'
              f'<path d="M0 13 v26 M0 19 l-13 9 M0 19 l13 9 M0 39 l-11 18 M0 39 l11 18" fill="none" stroke="#9FC0F5" stroke-width="2.5" stroke-linecap="round"></path></g></g>'
              f'<animateMotion dur="16s" repeatCount="indefinite" rotate="0" path="{path}"></animateMotion></g>')
    return (f'<div class="day-path-wrap rvl" aria-hidden="true"><div class="dp-eyebrow">The day in one line · {e(C.HOURS)}</div>'
            f'<svg viewBox="0 0 {W_} 125" class="viz" aria-hidden="true" focusable="false"><path d="{path}" stroke="rgba(255,255,255,.16)" stroke-width="2" class="dtdraw" style="--c:830;--dur:12s"></path>{nodes}{walker}</svg></div>')
def breaks_line(d):
    b = [t.split("-")[0] for t, n, x in C.DAYS[d]["blocks"] if not x]
    return f"A guide, not a script. Breaks at {' and '.join(b)}. The trainer calls the breaks." if b else "A guide, not a script."
def daypage(d):
    Dd = C.DAYS[d]; ros = ""; k = 0
    for t, blk, desc in Dd["blocks"]:
        if not desc:
            ros += f'<li class="is-brk"><span class="brk">{ico("cup", 14)}</span><div class="rc"><div class="rt"><b>{e(blk)}</b><span class="time">{t.split("-")[0]}</span></div></div></li>'
        else:
            k += 1; ros += f'<li><span class="num">{k}</span><div class="rc"><div class="rt"><b>{e(blk)}</b><span class="time">{t}</span></div><div class="rd">{e(desc)}</div></div></li>'
    tasks = ""
    for did, v in day_demos(d):
        if not v.get("hands_on"): continue
        st = "".join(f"<li>{e(x)}</li>" for x in wk.task_steps(v))
        fl = "".join(f'<a href="{f}" download>{e(f)}</a>' for f in v["files"])
        fin = f'<div class="out"><b>Finished early?</b> {e(" ".join(v["stretch"]))}</div>' if v["stretch"] else ""
        pts = f' · {v["points"]} points' if v.get("points") else ""
        tasks += (f'<article class="act rvl"><div class="kicker">Your turn · {e(v["card"])} · {v["minutes"]} min · {e(v["solo"])}{pts}</div><h3>{e(v["title"])}</h3><ol>{st}</ol>'
                  f'<div class="clock"><b>{v["minutes"]}:00 on the clock</b> · {e(v["tool"])}</div>'
                  + (f'<div class="out"><b>You hand in:</b> {e(v["deliverable"])}</div>' if v["deliverable"] else "")
                  + f'<div class="out"><b>Look for:</b> {e(v["hint"])}</div>{fin}' + (f'<div class="act-files">{fl}</div>' if fl else "") + "</article>")
    nt = sum(1 for _k, v in day_demos(d) if v.get("hands_on"))
    files = sorted({f for _k, v in day_demos(d) for f in v["files"]})
    chips = "".join(f'<span class="chip2">{e(n)}</span>' for _t, n, x in Dd["blocks"] if x)
    keys = [k for k in wk.FORM_DAY.get(d, []) if k in wk.FORMS]
    side_map = (f'<section class="panel"><h3>{"Before you start" if "pre" in keys else "Before you leave"}</h3><p class="muted">Scan the QR code on the screen, or open the link on your phone.</p>'
                f'<div class="map-list">{"".join(map_slot(k) for k in keys)}</div></section>') if keys else ""
    lab = cta("flask", f"Day {d} lab", e(wk.LABS[d]["intro"]), f"{labp(d)}.html", "Open the lab", True) if d in wk.LABS else ""
    ress = (res(f"{deckp(d)}.html", f"Day {d} slide deck", "Slides", "slides") + res(f"{sheetp(d)}.html", f"Day {d} {wk.SHEET['name'].lower()}", "Copy", "copy")
            + (res(f"{labp(d)}.html", f"Day {d} lab", "Lab", "flask") if d in wk.LABS else "")
            + (res(f"{wk.practp()}.html", "Practice questions", "Practice", "check") if wk.PRACTICE else "")
            + res(f'{P("cheat-sheet")}.html', "Cheat sheet", "Reference") + res(f'{cardp()}.html', wk.CARD["name"], "Reference", "shield")
            + res(f'{P("take-home-guide")}.html', "Take-home guide", "After the workshop", "home")
            + "".join(res(f, f, "Fictional file", kind_icon(f), dl=True) for f in files)
            + "".join(res(f"{dayp(x)}.html", f"Day {x} · {C.DAYS[x]['title']}", f"Day {x}", "cal") for x in DAYS if x != d)
            + res(f"{HUB}.html", both(), "Workshop", "grid"))
    sheet_line = ("Every prompt is on your prompt sheet." if wk.AI else "Every task, file and template is on your task sheet.")
    body = f'''<main>{topbar(f"Day {d}")}
{dhero(d, f"Day {d} · {e(Dd['title'])}", e(Dd["title"]), e(Dd["sub"]), [("cal", f"Day {d} of {wk.NDAYS} · {e(C.DAYDATE[d])}"), ("clock", e(C.HOURS)), ("pin", f"In person · {e(C.VENUE)}")])}
<div class="wrap"><div class="d-grid">
<div class="d-main">
  {day_path(d)}
  <section class="panel rvl"><h2>Day brief</h2><p class="brief">{e(Dd["brief"])}</p><p class="muted" style="margin-top:12px"><b>You build today:</b> {e(Dd["artifact"])}.</p></section>
  <section class="panel rvl"><h2>Run of show</h2><p class="muted">{breaks_line(d)}</p><ol class="ros">{ros}</ol></section>
  <section class="panel rvl"><h2>Your turn</h2><p class="muted">{nt} hands-on tasks. The timer runs on the main screen. {sheet_line}</p><div class="acts">{tasks}</div>
    <p class="smallnote">{e(C.SAMPLE_NOTE)} {e(HB.get("day_tool_note", ""))}</p></section>
</div>
<aside class="d-side">
  <section class="panel"><h3>What you will be able to do</h3><ul class="leave">{"".join(f"<li>{ico('check', 15, 2.5)}<span>{x}</span></li>" for x in Dd["outcomes"])}</ul></section>
  <section class="panel"><h3>What we will cover</h3><div class="chips">{chips}</div></section>
  {cta("slides", f"Day {d} slides", "The deck as run in the room, with every demo. Arrows to move, F for full screen.", f"{deckp(d)}.html", "Open the slides")}
  {cta("copy", "Your " + wk.SHEET["name"].lower(), ("Every prompt from today with a COPY button, and the file each one needs." if wk.AI else "Every task from today: the steps, the file and a template to copy."), f"{sheetp(d)}.html", "Open the " + wk.SHEET["name"].lower(), True)}
  {lab}
  {side_map}
  <section class="panel"><h3>Resources and files</h3><div class="res-list">{ress}</div></section>
</aside>
</div></div></main>{foot_mini()}'''
    return page(f"Day {d} · {Dd['title']}", f"Day {d} of {C.TITLE}: {Dd['sub']}", body, TOPBAR_H_JS)

# ------------------------------------------------------------------ the sheet of the day: prompts (AI tool) or tasks and templates (no AI tool)
def sheet(d):
    items = day_demos(d); secs = []
    for _k, v in items:
        if v["sec"] not in secs: secs.append(v["sec"])
    nav = '<a href="#start">Start here</a>' + "".join(f'<a href="#s{s}">{e(BLOCK[s][1])}</a>' for s in secs)
    cards = ""
    pw = lambda lab, txt, i: f'<div class="sh-plab">{e(lab)}</div><div class="sh-promptwrap"><pre id="{i}">{e(txt)}</pre><button class="sh-copy" type="button" data-copy="{i}">COPY</button></div>'
    for s in secs:
        cards += f'<section id="s{s}"><div class="sh-dayhead"><h2>{e(BLOCK[s][1])}</h2></div>'
        for did, v in [(k, x) for k, x in items if x["sec"] == s]:
            pid = f"p{d}-{did}"; hands = v.get("hands_on")
            steps = wk.task_steps(v)
            body = f'<div class="sh-when"><ol>{"".join(f"<li>{e(x)}</li>" for x in steps)}</ol></div>' if steps else '<div class="sh-noprompt">Watch it in the slide. The trainer runs it with the room.</div>'
            if hands and v["deliverable"]: body += f'<div class="sh-plab">You hand in</div><p class="sh-deliv">{e(v["deliverable"])}</p>'
            body += "".join(pw(l, t, f"{pid}-{j}") for j, (l, t) in enumerate(v["prompts"] if wk.AI else []))
            body += "".join(pw(l, t, f"{pid}-t{j}") for j, (l, t) in enumerate(v["templates"]))
            if v.get("examples"):
                body += f'<div class="sh-plab">{e(opt("REWRITE_LABEL", "Rewrite these weak prompts"))}</div>' + "".join(f'<div class="sh-ask">“{e(a)}”</div>' for a in v["examples"])
            if v["stretch"]:
                body += '<div class="sh-plab">Finished early? Extra task</div><ul class="sh-stretch">' + "".join(f"<li>{e(x)}</li>" for x in v["stretch"]) + "</ul>"
                body += "".join(pw(l, t, f"{pid}-s{j}") for j, (l, t) in enumerate(v["stretch_prompts"] if wk.AI else []))
            files = '<div class="sh-files">' + "".join(f'<a href="{f}" download>{e(f)}</a>' for f in v["files"]) + "</div>" if v["files"] else '<span class="sh-none">No file needed.</span>'
            pts = f' · {v["points"]} points' if v.get("points") else ""
            tag = (f'<span class="sh-tag sh-team">Your turn · {v["minutes"]} min{pts}</span>' if hands
                   else f'<span class="sh-tag">{"Watch, then try" if (wk.AI and v["prompts"]) else "Watch"}</span>')
            cards += (f'<div class="sh-card" id="{pid}"><div class="sh-top"><span class="sh-blk">{e(v["card"])}</span><span class="sh-time">{e(v["tool"])}</span>{tag}</div>'
                      f'<h3>{e(v["title"])}</h3>{body}<div class="sh-meta sh-meta--3"><div><b class="sh-lab">What to look for</b>{e(v["hint"])}</div><div><b class="sh-lab">Files</b>{files}</div><div><b class="sh-lab">Takeaway</b>{e(v["point"])}</div></div></div>')
        cards += "</section>"
    S = opt("SHEET", {})
    howto_default = (["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card.", "Click <b>COPY</b> and paste the prompt into the tool.", "<b>Check the answer</b> against the file before you trust it."]
                     if wk.AI else ["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card and open it.", "Use the <b>template</b> on the card: click <b>COPY</b> and paste it into your notes or the file."])
    howto = ('<div class="sh-howto" id="start"><b>How to use this</b><ol>' + "".join(f"<li>{x}</li>" for x in S.get("howto", howto_default)) + "</ol>"
             + (f'<p>{S["note"]}</p>' if S.get("note") else "") + "</div>")
    foot = (f'<p class="smallnote sheet-foot">{e(wk.ORG)} · {e(C.TITLE)} · Day {d}. {e(C.SAMPLE_NOTE)} '
            f'<a href="{P("cheat-sheet")}.html">Cheat sheet</a> · <a href="{P("take-home-guide")}.html">Take-home guide</a> · <a href="{dayp(d)}.html">Back to Day {d}</a></p>')
    nm = wk.SHEET["name"]
    lede = ("Every prompt from today, in teaching order. Click <b>COPY</b>, then paste it into the tool. Download the file on the card first." if wk.AI
            else "Every task from today, in teaching order: the steps, the file, what you hand in, and a template to copy.")
    meta = [("copy", "Prompts with COPY" if wk.AI else "Templates with COPY"), ("check", "Check before you trust" if wk.AI else "Steps and hints"), ("shield", "Fictional data only")]
    body = f'''<main>{topbar(f"p{d}")}
{dhero(d, f"Day {d} · {nm.lower()}", f"Your {nm.lower()} · Day {d}", lede, meta)}
<div class="wrap"><nav class="subnav" aria-label="On this page"><div class="in">{nav}</div></nav></div>
<div class="wrap"><div class="sheet">{howto}{cards}{foot}</div></div>
</main>{foot_mini()}'''
    return page(f"Day {d} · {nm}", f"Every {wk.SHEET['what'][:-1]} from Day {d} of {C.TITLE}, with COPY buttons.", body, COPY_JS + TOPBAR_H_JS)

# ------------------------------------------------------------------ cheat sheet, card page, take-home guide
def cheat():
    out = ""
    for ph, pt, ps, items, sm in C.CHEAT:
        g = "".join(f'<div class="sh-item"><div class="sh-nm">{e(it[0])}</div><div class="sh-st">{e(it[1])}</div>' + (f'<div class="sh-an">{e(it[2])}</div>' if len(it) > 2 and it[2] else "")
                    + (f'<div class="sh-df">{e(it[3])}</div>' if len(it) > 3 and it[3] else "") + '</div>' for it in items)
        out += f'<div class="sh-part rvl"><div class="sh-ph">{e(ph)}</div><div class="sh-pt">{e(pt)}</div><div class="sh-psub">{e(ps)}</div><div class="sh-grid">{g}</div><div class="sh-sum">{e(sm)}</div></div>'
    for title, headr, rows in opt("CHEAT_TABLES", []):
        tr = "".join("<tr>" + "".join(f"<td>{'<b>' + e(c) + '</b>' if j == 0 else e(c)}</td>" for j, c in enumerate(r)) + "</tr>" for r in rows)
        out += f'<div class="sh-part rvl"><div class="sh-ph">{e(title)}</div><div class="tblwrap"><table class="tbl"><thead><tr>{"".join(f"<th>{e(h)}</th>" for h in headr)}</tr></thead><tbody>{tr}</tbody></table></div></div>'
    out += f'<div class="sh-note"><span class="sh-ic">!</span><span><b>{e(C.THRU)}</b></span></div>'
    out += f'<p class="smallnote"><a href="{cardp()}.html">{e(wk.CARD["name"])}</a> · <a href="{P("take-home-guide")}.html">Take-home guide</a> · <a href="{HUB}.html">{both()}</a></p>'
    meta = opt("CHEAT_META", [("list", f"{len(C.CHEAT)} parts"), ("check", "One page"), ("shield", "Fictional data")])
    body = f'''<main>{topbar("Cheat sheet")}
{dhero(1, "Cheat sheet · " + both().lower(), "Cheat sheet", e(opt("CHEAT_LEDE", "The main ideas of the workshop on one page.")), meta)}
<div class="wrap"><div class="sheet">{out}</div></div></main>{foot_mini()}'''
    return page("Cheat sheet", f"The main ideas of {C.TITLE} on one page.", body)

def card_page():
    K_ = wk.CARD
    tone = {"green": "safe-g", "amber": "safe-a", "red": "safe-r"}
    cards = "".join(f'<div class="safe-card {tone.get(c, "safe-a")} rvl"><h3>{e(h)}</h3><p>{e(p)}</p><ul>' + "".join(f"<li>{e(x)}</li>" for x in ex_) + "</ul></div>" for c, h, p, ex_ in K_["cards"])
    risks = "".join("<tr>" + "".join(f"<td>{'<b>' + e(c) + '</b>' if j == 0 else e(c)}</td>" for j, c in enumerate(r)) + "</tr>" for r in K_.get("risks", []))
    rt = (f'<div class="sh-part rvl"><div class="sh-ph">{e(K_["risks_title"])}</div><div class="tblwrap"><table class="tbl"><thead><tr>{"".join(f"<th>{e(h)}</th>" for h in K_["risks_head"])}</tr></thead><tbody>{risks}</tbody></table></div></div>'
          if K_.get("risks") else "")
    pol = (f'<div class="sh-part rvl"><div class="sh-ph">{e(K_["policy_title"])}</div><ul class="leave">' + "".join(f"<li>{ico('check', 15, 2.5)}<span>{e(x)}</span></li>" for x in K_["policy"]) + "</ul></div>"
           if K_.get("policy") else "")
    body = f'''<main>{topbar(K_["name"])}
{dhero(min(2, wk.NDAYS), K_["name"] + " · " + both().lower(), e(K_["name"]), K_["lede"], K_.get("meta", [("shield", "Green, amber, red")]))}
<div class="wrap"><div class="sheet">
  <div class="safe-grid">{cards}</div>
  {rt}{pol}
  <p class="smallnote"><a href="{P("cheat-sheet")}.html">Cheat sheet</a> · <a href="{P("take-home-guide")}.html">Take-home guide</a> · <a href="{HUB}.html">{both()}</a></p>
</div></div></main>{foot_mini()}'''
    return page(K_["name"], f"{K_['name']}: green, amber or red. {C.TITLE}, {wk.ORG}.", body)

def guide():
    out = "".join(f'<div class="sh-card rvl"><div class="sh-top"><span class="sh-blk">{i + 1:02d}</span></div><h3>{e(h)}</h3><ol class="guide-steps">' + "".join(f"<li>{e(x)}</li>" for x in st) + "</ol></div>" for i, (h, st) in enumerate(C.GUIDE))
    out += f'<div class="sh-note"><span class="sh-ic">!</span><span><b>The habit · every time.</b> {e(C.GUIDE_HABIT)}</span></div>'
    out += f'<p class="smallnote"><a href="{cardp()}.html">{e(wk.CARD["name"])}</a> · <a href="{P("cheat-sheet")}.html">Cheat sheet</a> · <a href="{HUB}.html">{both()}</a></p>'
    body = f'''<main>{topbar("Take-home guide")}
{dhero(min(2, wk.NDAYS), "Take-home guide · after the workshop", "Take-home guide", e(C.GUIDE_INTRO), opt("GUIDE_META", [("home", "Your own work"), ("list", "First week, first month"), ("shield", "Policy first")]))}
<div class="wrap"><div class="sheet">{out}</div></div></main>{foot_mini()}'''
    return page("Take-home guide", f"Repeat what you practiced in {C.TITLE}, at work.", body)

# ------------------------------------------------------------------ browser lab: steps, done marks saved in this browser, hints, a check per step
def norm_flag(s): return re.sub(r"[^a-z0-9]", "", str(s).lower())
def flag_hash(s): return hashlib.sha256(f"{wk.PFX}:{norm_flag(s)}".encode()).hexdigest()
LAB_JS = r"""<script>(function(){
/* SHA-256 (ASCII), so a flag is checked in the page without the answer in it */
function sha256(a){function r(v,n){return(v>>>n)|(v<<(32-n));}var mp=Math.pow,mw=mp(2,32),i,j,res='',w=[],bl=a.length*8,h=[],k=[],pc=0,ic={};
for(var c=2;pc<64;c++){if(!ic[c]){for(i=0;i<313;i+=c)ic[i]=c;h[pc]=(mp(c,.5)*mw)|0;k[pc++]=(mp(c,1/3)*mw)|0;}}
a+='\x80';while(a.length%64-56)a+='\x00';for(i=0;i<a.length;i++){j=a.charCodeAt(i);if(j>>8)return '';w[i>>2]|=j<<((3-i)%4)*8;}
w[w.length]=((bl/mw)|0);w[w.length]=bl;
for(j=0;j<w.length;){var x=w.slice(j,j+=16),o=h;h=h.slice(0,8);for(i=0;i<64;i++){var w15=x[i-15],w2=x[i-2],A=h[0],E=h[4];
var t1=h[7]+(r(E,6)^r(E,11)^r(E,25))+((E&h[5])^((~E)&h[6]))+k[i]+(x[i]=(i<16)?x[i]:(x[i-16]+(r(w15,7)^r(w15,18)^(w15>>>3))+x[i-7]+(r(w2,17)^r(w2,19)^(w2>>>10)))|0);
var t2=(r(A,2)^r(A,13)^r(A,22))+((A&h[1])^(A&h[2])^(h[1]&h[2]));h=[(t1+t2)|0].concat(h);h[4]=(h[4]+t1)|0;}for(i=0;i<8;i++)h[i]=(h[i]+o[i])|0;}
for(i=0;i<8;i++)for(j=3;j+1;j--){var b=(h[i]>>(j*8))&255;res+=((b<16)?0:'')+b.toString(16);}return res;}
var root=document.querySelector('[data-lab]');if(!root)return;var KEY=root.getAttribute('data-lab'),SALT=root.getAttribute('data-salt');
var st={done:{},notes:{},ok:{}};
function load(){try{var v=localStorage.getItem(KEY);if(v){var p=JSON.parse(v);st.done=p.done||{};st.notes=p.notes||{};st.ok=p.ok||{};}}catch(x){}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(x){}}
var steps=[].slice.call(root.querySelectorAll('.lab-step'));
function paint(){var n=0;steps.forEach(function(s){var i=s.getAttribute('data-step'),cb=s.querySelector('.lab-done input');cb.checked=!!st.done[i];s.classList.toggle('is-done',!!st.done[i]);if(st.done[i])n++;
  var ta=s.querySelector('textarea');if(ta&&document.activeElement!==ta)ta.value=st.notes[i]||'';var r=s.querySelector('.lab-res');if(r&&st.ok[i]){r.textContent='Correct';r.className='lab-res ok';}});
  var c=root.querySelector('[data-r="count"]');c.textContent=n+' of '+steps.length+' done';root.querySelector('[data-r="bar"]').style.width=(100*n/steps.length)+'%';}
root.addEventListener('change',function(e){var s=e.target.closest('.lab-step');if(!s||!e.target.matches('.lab-done input'))return;st.done[s.getAttribute('data-step')]=e.target.checked;save();paint();});
root.addEventListener('input',function(e){var s=e.target.closest('.lab-step');if(!s||e.target.tagName!=='TEXTAREA')return;st.notes[s.getAttribute('data-step')]=e.target.value;save();});
function check(s){var inp=s.querySelector('.lab-flag'),r=s.querySelector('.lab-res'),i=s.getAttribute('data-step');var v=(inp.value||'').toLowerCase().replace(/[^a-z0-9]/g,'');
  if(!v){r.textContent='Type an answer first';r.className='lab-res';return;}
  if(sha256(SALT+':'+v)===inp.getAttribute('data-h')){st.ok[i]=true;st.done[i]=true;save();paint();r.textContent='Correct';r.className='lab-res ok';}
  else{r.textContent='Not yet. Read the hint and try again.';r.className='lab-res no';}}
root.addEventListener('click',function(e){var b=e.target.closest('.lab-go');if(b){check(b.closest('.lab-step'));return;}
  if(e.target.closest('[data-r="reset"]')){st={done:{},notes:{},ok:{}};save();steps.forEach(function(s){var r=s.querySelector('.lab-res');if(r){r.textContent='';r.className='lab-res';}var f=s.querySelector('.lab-flag');if(f)f.value='';});paint();}});
root.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.classList.contains('lab-flag')){e.preventDefault();check(e.target.closest('.lab-step'));}});
load();paint();})();</script>"""
def lab(d):
    L = wk.LABS[d]
    steps = ""
    for i, s in enumerate(L["steps"], 1):
        ck = s.get("check") or {"kind": "note", "label": "Your notes"}
        if ck["kind"] == "flag":
            cid = f"lab{d}-{i}"
            chk = (f'<div class="lab-check"><label for="{cid}">{e(ck["label"])}</label><div class="lab-row"><input class="lab-flag" id="{cid}" type="text" autocomplete="off" spellcheck="false" data-h="{flag_hash(ck["answer"])}">'
                   f'<button class="lab-go" type="button">Check</button></div><span class="lab-res" aria-live="polite"></span></div>')
        else:
            cid = f"lab{d}-{i}"
            chk = (f'<div class="lab-check"><label for="{cid}">{e(ck["label"])}</label><textarea id="{cid}" rows="3"></textarea>'
                   f'<small class="lab-small">Saved in this browser only. The trainer checks it with you.</small></div>')
        files = "".join(f'<a href="{f}" download>{e(f)}</a>' for f in s.get("files", []))
        steps += (f'<article class="sh-card lab-step rvl" id="step{i}" data-step="{i}"><div class="sh-top"><span class="sh-blk">Step {i}</span>'
                  f'<label class="lab-done"><input type="checkbox"> Done</label></div><h3>{e(s["title"])}</h3>'
                  f'<ol class="lab-do">{"".join(f"<li>{e(x)}</li>" for x in s["do"])}</ol>' + (f'<div class="sh-files">{files}</div>' if files else "")
                  + (f'<details class="lab-hint"><summary>Show a hint</summary><p>{e(s["hint"])}</p></details>' if s.get("hint") else "") + chk + "</article>")
    prog = (f'<div class="lab-prog panel"><span data-r="count">0 of {len(L["steps"])} done</span><div class="lab-bar"><i data-r="bar"></i></div>'
            f'<button class="lab-reset" type="button" data-r="reset">Reset my marks</button></div>')
    body = f'''<main>{topbar(f"Day {d}")}
{dhero(d, f"Day {d} · lab", e(L["title"]), e(L["intro"]), [("flask", f"{len(L['steps'])} steps"), ("check", "A check on each step"), ("shield", "Saved in this browser")])}
<div class="wrap"><div class="sheet" data-lab="{wk.PFX}-lab-day-{d}" data-salt="{wk.PFX}">{prog}{steps}
<p class="smallnote sheet-foot">{e(C.SAMPLE_NOTE)} Your marks and notes stay in this browser; nothing is sent. <a href="{dayp(d)}.html">Back to Day {d}</a></p></div></div>
</main>{foot_mini()}'''
    return page(f"Day {d} · Lab", f"Day {d} lab of {C.TITLE}: {L['title']}.", body, LAB_JS + TOPBAR_H_JS)

# ------------------------------------------------------------------ practice questions (optional PRACTICE): scored in the browser, nothing sent
def practice_hash(i, k): return hashlib.sha256(f"{wk.PFX}:pq{i}:{k}".encode()).hexdigest()
PRACTICE_JS = r"""<script>(function(){
var root=document.querySelector('[data-pq]');if(!root)return;var KEY=root.getAttribute('data-pq'),SALT=root.getAttribute('data-salt');
var SHA=window.wkSha256;var cards=[].slice.call(root.querySelectorAll('.pq'));var st={ans:{},best:0};
function load(){try{var v=localStorage.getItem(KEY);if(v){var p=JSON.parse(v);st.ans=p.ans||{};st.best=p.best||0;}}catch(x){}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(x){}}
function right(c){var i=c.getAttribute('data-q'),h=c.getAttribute('data-h');for(var k=0;k<4;k++){if(SHA(SALT+':pq'+i+':'+k)===h)return k;}return -1;}
function paint(){var tot=cards.length,done=0,ok=0,by={};
 cards.forEach(function(c){var i=c.getAttribute('data-q'),t=c.getAttribute('data-t'),a=st.ans[i],r=c.querySelector('.pq-res'),w=c.querySelector('.pq-why');
  by[t]=by[t]||{n:0,ok:0,done:0};by[t].n++;var bs=[].slice.call(c.querySelectorAll('.pq-opt'));
  bs.forEach(function(b){b.classList.remove('is-pick','is-right','is-wrong');b.disabled=false;});
  if(a===undefined){r.textContent='';r.className='pq-res';w.hidden=true;c.classList.remove('is-wrong','is-ok');return;}
  var k=right(c);done++;by[t].done++;bs.forEach(function(b){b.disabled=true;});bs[a].classList.add('is-pick');if(k>=0)bs[k].classList.add('is-right');
  if(a===k){ok++;by[t].ok++;r.textContent='Correct';r.className='pq-res ok';c.classList.add('is-ok');c.classList.remove('is-wrong');}
  else{bs[a].classList.add('is-wrong');r.textContent='Not quite: the right answer is green';r.className='pq-res no';c.classList.add('is-wrong');c.classList.remove('is-ok');}
  w.hidden=false;});
 if(done===tot&&ok>st.best){st.best=ok;save();}
 root.querySelector('[data-r="score"]').textContent=ok+' right of '+done+' answered ('+tot+' questions)';
 root.querySelector('[data-r="best"]').textContent=st.best?('Your best: '+st.best+' of '+tot):'';
 root.querySelector('[data-r="bar"]').style.width=(100*done/tot)+'%';
 [].slice.call(root.querySelectorAll('.pq-topic')).forEach(function(row){var t=row.getAttribute('data-t'),b=by[t]||{n:0,ok:0,done:0};
  row.querySelector('b').textContent=b.ok+' / '+b.n;row.querySelector('i').style.width=(b.n?100*b.ok/b.n:0)+'%';});}
root.addEventListener('click',function(e){var b=e.target.closest('.pq-opt');if(b){var c=b.closest('.pq'),i=c.getAttribute('data-q');if(st.ans[i]!==undefined)return;
  st.ans[i]=+b.getAttribute('data-k');save();paint();return;}
 if(e.target.closest('[data-r="reset"]')){st.ans={};save();root.classList.remove('only-wrong');paint();return;}
 if(e.target.closest('[data-r="wrong"]')){root.classList.toggle('only-wrong');}});
load();paint();})();</script>"""
def practice():
    Q = wk.PRACTICE; T = Q["topics"]; qs = Q["questions"]
    cards = ""
    for i, q in enumerate(qs, 1):
        opts = "".join(f'<button type="button" class="pq-opt" data-k="{k}"><span class="pq-key">{"ABCD"[k]}</span><span>{e(o)}</span></button>' for k, o in enumerate(q["o"]))
        cards += (f'<article class="sh-card pq rvl" id="q{i}" data-q="{i}" data-t="{e(q["topic"])}" data-h="{practice_hash(i, q["a"])}">'
                  f'<div class="sh-top"><span class="sh-blk">Question {i} · {e(T[q["topic"]])}</span><span class="pq-res" aria-live="polite"></span></div>'
                  f'<h3>{e(q["q"])}</h3><div class="pq-opts">{opts}</div><p class="pq-why" hidden><b>Why:</b> {e(q["why"])}</p></article>')
    topics = "".join(f'<div class="pq-topic" data-t="{e(k)}"><span>{e(v)}</span><div class="lab-bar"><i></i></div><b>0 / 0</b></div>' for k, v in T.items())
    panel = (f'<div class="lab-prog panel pq-panel"><div class="pq-score"><span data-r="score"></span><small data-r="best"></small></div><div class="lab-bar"><i data-r="bar"></i></div>'
             f'<button class="lab-reset" type="button" data-r="wrong">Show only my wrong answers</button><button class="lab-reset" type="button" data-r="reset">Start again</button>'
             f'<div class="pq-topics"><div class="pq-th">Right answers by topic</div>{topics}</div></div>')
    body = f'''<main>{topbar(both())}
{dhero(1, e(Q.get("pill", "Practice")), e(Q.get("title", "Practice questions")), e(Q.get("intro", "")), [("check", f"{len(qs)} questions"), ("list", f"{len(T)} topics"), ("shield", "Saved in this browser")])}
<div class="wrap"><div class="sheet" data-pq="{wk.PFX}-practice" data-salt="{wk.PFX}">{panel}{cards}
<p class="smallnote sheet-foot">{e(Q.get("note", "Practice only: your answers are not scored or sent. They stay in this browser."))} <a href="{HUB}.html">Back to the workshop</a></p></div></div>
</main>{foot_mini()}'''
    sha = LAB_JS.split("/* SHA-256 (ASCII), so a flag is checked in the page without the answer in it */\n")[1].split("\nvar root=")[0]
    return page(Q.get("title", "Practice questions"), f"Practice questions for {C.TITLE}.", body,
                "<script>window.wkSha256=" + sha.replace("function sha256(a)", "function(a)", 1) + "</script>" + PRACTICE_JS + TOPBAR_H_JS)

# ------------------------------------------------------------------ site CSS: the CODED glass theme, then the client mix
SITE_EXTRA = """
/* ============ engine additions ============ */
@media (min-width:1001px){.cards.cards-2{grid-template-columns:repeat(2,1fr);max-width:960px}}
.act .out + .out{margin-top:6px}
.sh-deliv{color:var(--ink);font-size:15px;line-height:1.55;margin:4px 0 10px}
/* a fill color is never used as text or an icon on the navy */
.leave li svg,.leave svg,.plist li svg,.ros .num,.map-slot--live .map-txt b{color:var(--rose-lt)}
.lk .partner-logo{border-radius:4px}
/* the hero word and the small dots use the light accent, never the fill (a dark client fill disappears on the navy) */
.headline .accent{background:linear-gradient(100deg,var(--rose-lt) 0%,var(--rose) 30%,#ffffff 50%,var(--rose) 70%,var(--rose-lt) 100%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text}
.pill .dot,.cat-pill .dot{background:var(--rose-lt);box-shadow:0 0 10px var(--rose-lt)}
/* practice questions */
.pq-panel{display:grid;grid-template-columns:1fr;gap:12px}.pq-score{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;font-family:var(--mono);font-size:13px;color:var(--ink)}
.pq-score small{color:var(--ink-dim)}.pq-panel .lab-reset{justify-self:start}.pq-topics{display:grid;gap:8px;margin-top:4px}.pq-th{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-dim)}
.pq-topic{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(80px,2fr) 54px;gap:10px;align-items:center;font-size:14px;color:var(--ink)}.pq-topic b{font-family:var(--mono);font-size:13px;text-align:right}
.pq-opts{display:grid;gap:8px;margin-top:10px}.pq-opt{display:flex;gap:10px;align-items:flex-start;text-align:left;width:100%;font:inherit;font-size:15px;line-height:1.45;color:var(--ink);background:rgba(255,255,255,.04);border:1px solid var(--line-2);border-radius:10px;padding:10px 12px;cursor:pointer}
.pq-opt:hover:not(:disabled){border-color:var(--rose-lt)}.pq-opt:disabled{cursor:default}.pq-key{font-family:var(--mono);font-size:12px;min-width:18px;color:var(--ink-dim);padding-top:2px}
.pq-opt.is-right{border-color:#3DC873;background:rgba(61,200,115,.14)}.pq-opt.is-wrong{border-color:#F84B4B;background:rgba(248,75,75,.12)}
.pq-res{font-family:var(--mono);font-size:12px;color:var(--ink-dim)}.pq-res.ok{color:#7BE3A4}.pq-res.no{color:#FF9C9C}.pq-why{margin-top:10px;font-size:14.5px;line-height:1.55;color:var(--ink)}
.only-wrong .pq.is-ok,.only-wrong .pq:not(.is-wrong):not(.is-ok){display:none}
@media (max-width:560px){.pq-topic{grid-template-columns:1fr 54px}.pq-topic .lab-bar{grid-column:1 / -1;grid-row:2}}
/* browser lab */
.lab-prog{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:18px 0;padding:14px 18px}
.lab-prog [data-r="count"]{font-family:var(--mono);font-size:13px;color:var(--ink)}
.lab-bar{flex:1;min-width:160px;height:10px;border-radius:6px;background:rgba(255,255,255,.08);overflow:hidden}
.lab-bar i{display:block;height:100%;width:0;background:var(--rose);transition:width .3s}
.lab-reset,.lab-go{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);background:rgba(255,255,255,.06);border:1px solid var(--line-2);border-radius:8px;padding:8px 12px;cursor:pointer}
.lab-go{background:var(--crimson);border-color:var(--crimson);color:#fff}
.lab-step.is-done{border-color:rgba(61,200,115,.45)}
.lab-done{margin-inline-start:auto;display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:12px;color:var(--ink);cursor:pointer}
.lab-done input{width:18px;height:18px;accent-color:#3DC873}
.lab-do{margin:8px 0 8px 20px;color:var(--ink);line-height:1.6;font-size:15px}
.lab-hint{margin:10px 0;border:1px dashed var(--line-2);border-radius:10px;padding:8px 12px;color:var(--ink-dim)}
.lab-hint summary{cursor:pointer;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--rose-lt)}
.lab-hint p{margin-top:6px;color:var(--ink);font-size:14.5px}
.lab-check{display:flex;flex-direction:column;gap:6px;margin-top:10px}
.lab-check label{font-size:14px;font-weight:700;color:var(--ink)}
.lab-row{display:flex;gap:8px;flex-wrap:wrap}
.lab-check input[type=text],.lab-check textarea{flex:1;min-width:0;width:100%;font:inherit;font-size:15px;color:var(--ink);background:rgba(0,0,0,.25);border:1px solid var(--line-2);border-radius:8px;padding:9px 11px}
.lab-row input[type=text]{width:auto}
.lab-small{font-size:12.5px;color:var(--ink-dim)}
.lab-res{min-height:1.3em;font-family:var(--mono);font-size:13px;color:var(--ink-dim)}
.lab-res.ok{color:#7FE0A8}.lab-res.no{color:#FF8A8A}
"""
def site_css():
    css = wk.asset("coded-site.css").replace("__PFX__", wk.PFX) + SITE_EXTRA
    if wk.CLIENT and wk.CLIENT.get("logo_scale"):
        css += f".lk .partner-logo{{height:calc(var(--lh,24px)*{wk.CLIENT['logo_scale']})}}\n"   # a round seal reads larger than a wordmark
    return wk.theme(css)

def assets(out):
    sh = lambda a, b: shutil.copy2(a, os.path.join(out, b))
    for name, src in wk.FONT_FILES.items(): sh(os.path.join(wk.FONTS, src), P(name))
    sh(os.path.join(wk.ASSETS, "coded-logo.png"), P("coded-logo.png"))
    sh(os.path.join(wk.ASSETS, "favicon.png"), P("favicon.png"))
    if wk.CLIENT_LOGO: sh(wk.CLIENT_LOGO, P("client-logo.png"))
    for f in ALL_FILES:
        src = os.path.join(wk.FILES_DIR, f)
        if not os.path.exists(src): sys.exit(f"site: sample file {f} is missing from {wk.FILES_DIR} (run the kit's gen_files.py)")
        shutil.copy2(src, os.path.join(out, f))
    open(os.path.join(out, P("site.css")), "w", encoding="utf-8").write(site_css())
    open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assets(OUT)
    nslides = sum(open(p, encoding="utf-8").read().count('<section class="cd-slide') for p in glob.glob(os.path.join(OUT, P("day-*-deck.html"))))
    pub = {HUB + ".html": hub(nslides), P("cheat-sheet") + ".html": cheat(), cardp() + ".html": card_page(), P("take-home-guide") + ".html": guide()}
    for d in DAYS:
        pub[dayp(d) + ".html"] = daypage(d); pub[sheetp(d) + ".html"] = sheet(d)
        if d in wk.LABS: pub[labp(d) + ".html"] = lab(d)
    if wk.PRACTICE: pub[wk.practp() + ".html"] = practice()
    for n, h in pub.items(): open(os.path.join(OUT, n), "w", encoding="utf-8").write(h)
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(not_found())
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow"><meta http-equiv="refresh" content="0; url={HUB}.html"><title>{e(C.TITLE)} · {e(wk.ORG)}</title><link rel="canonical" href="{HUB}.html"></head><body><p><a href="{HUB}.html">{e(C.TITLE)}</a></p></body></html>\n')
    print(len(pub), "public pages ·", nslides, "slides")
