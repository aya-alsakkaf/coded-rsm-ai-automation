# -*- coding: utf-8 -*-
"""Names, icons, the lockup, QR codes and the page shell shared by the site and the decks."""
import html
import io
import segno
from content_core import CODE, PROGRAM, CLIENT, MAP, DAYS, HOURS, VENUE_SHORT, VENUE

ESC = lambda s: html.escape(str(s), quote=True)


def page(name):
    """public file name for a page key, e.g. page('day-1') -> coded-rsm-ai-automation-day-1.html"""
    return f"{CODE}.html" if name == "" else f"{CODE}-{name}.html"


# ── icons: simple stroke icons, 24x24 ──
_P = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "back": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5"/>',
    "cal": '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "pin": '<path d="M12 21s-6.5-5.6-6.5-11A6.5 6.5 0 0 1 18.5 10c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "file": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/>',
    "slides": '<rect x="3" y="4.5" width="18" height="12" rx="1.8"/><path d="M12 16.5V20M8 20h8"/>',
    "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4h-9A1.5 1.5 0 0 0 4 5.5v9A1.5 1.5 0 0 0 5.5 16H8"/>',
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
    "shield": '<path d="M12 3l7.5 3v6c0 4.6-3.2 8.2-7.5 9-4.3-.8-7.5-4.4-7.5-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "agent": '<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M9.5 16.5h5"/><circle cx="12" cy="3.5" r="1"/>',
    "flow": '<rect x="3" y="4" width="6" height="5" rx="1.2"/><rect x="15" y="4" width="6" height="5" rx="1.2"/><rect x="9" y="15" width="6" height="5" rx="1.2"/><path d="M9 6.5h6M18 9v3H12v3M6 9v3h6"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    "timer": '<circle cx="12" cy="13" r="7.5"/><path d="M12 9v4l2.5 1.5M9.5 3h5"/>',
    "full": '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19.5c.6-3.2 2.8-5 5.5-5s4.9 1.8 5.5 5"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.6c2.4.2 4.2 1.8 4.7 4.4"/>',
    "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    "qr": '<rect x="4" y="4" width="6" height="6"/><rect x="14" y="4" width="6" height="6"/><rect x="4" y="14" width="6" height="6"/><path d="M14 14h2v2h-2zM18 18h2v2h-2zM14 18h2M18 14v2"/>',
}


def icon(name, size=18, cls=""):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


def lockup(prefix=""):
    """CODED logo beside the client name. The CODED logo is never removed. The client name is text until RSM's
    official logo files arrive (see CLAUDE.md, Decisions)."""
    return (f'<span class="lk"><img class="coded-logo" src="{prefix}{CODE}-coded-logo.png" alt="CODED" width="320" height="120">'
            f'<span class="x">×</span><span class="client-name">RSM <span>Albazie</span></span></span>')


def qr_svg(url, cls="qr"):
    if not url:
        return ""
    q = segno.make(url, error="m")
    buf = io.StringIO()
    q.save(buf, kind="svg", dark="#00112F", light="#ffffff", border=2, scale=1, xmldecl=False, svgns=True, svgclass=cls, lineclass=None, omitsize=True)
    return buf.getvalue()


def map_url(which):
    return MAP[which]["url"]


HEAD = """<!doctype html>
<html lang="en"{html_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{prefix}{code}-favicon.png">
{css}
<script>document.documentElement.classList.add("js")</script>
</head>
"""


def head(title, desc, prefix="", css="", html_attr=""):
    if not css:
        css = f'<link rel="stylesheet" href="{prefix}{CODE}-site.css">'
    return HEAD.format(title=ESC(title), desc=ESC(desc), prefix=prefix, code=CODE, css=css, html_attr=html_attr)


REVEAL_JS = r"""<script>(function(){var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function fmt(n,d){return n.toFixed(d)}
function count(el){if(el.dataset.done||RM)return;el.dataset.done=1;var t=parseFloat(el.dataset.count),d=+(el.dataset.dec||0),st=performance.now();
 function tick(now){var p=Math.min(1,(now-st)/900),e=1-Math.pow(1-p,3);el.textContent=fmt(t*e,d);if(p<1)requestAnimationFrame(tick)}requestAnimationFrame(tick)}
var els=[].slice.call(document.querySelectorAll('.rvl,[data-count]'));
if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('on');count(e)});return}
var t0=performance.now();var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){if(performance.now()-t0<900)x.target.classList.add('now');x.target.classList.add('on');if(x.target.dataset.count)count(x.target);io.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'});
els.forEach(function(e){if(e.getBoundingClientRect().top<innerHeight*1.6){e.classList.add('now','on');if(e.dataset.count)count(e)}else io.observe(e)});})();</script>"""

COPY_JS = r"""<script>document.querySelectorAll('.sh-copy').forEach(function(b){b.addEventListener('click',function(){var pre=b.parentElement.querySelector('pre');var t=pre.innerText;
function ok(){b.textContent='COPIED';b.classList.add('done');setTimeout(function(){b.textContent='COPY';b.classList.remove('done')},1600)}
if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok,function(){fb()})}else fb();
function fb(){var a=document.createElement('textarea');a.value=t;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){}document.body.removeChild(a)}})});</script>"""


def topbar(active="", prefix="", staff=False):
    links = [("day-1", "Day 1"), ("day-2", "Day 2"), ("prompt-sheet-day-1", "Prompts"), ("cheat-sheet", "Cheat sheet")]
    nav = "".join(f'<a href="{prefix}{page(k)}"{" class=\"on\"" if k == active else ""}>{ESC(t)}</a>' for k, t in links)
    if staff:
        nav += '<a href="index.html" class="on">Staff</a>' if active == "staff" else '<a href="index.html">Staff</a>'
    return (f'<div class="wrap"><div class="topbar"><a class="back" href="{prefix}{page("")}"><span class="ar">←</span> Back to the program</a>'
            f'<nav class="daynav">{nav}</nav></div></div>')


def foot_mini(prefix=""):
    return (f'<footer class="foot-mini"><div class="wrap"><div class="foot-row"><div class="f-lockup">{lockup(prefix)}</div>'
            f'<span class="copy">© 2026 CODED · Kuwait. All sample files are fictional, made for training.</span></div></div></footer>')


def map_slot(which, prefix="", qr=True):
    m = MAP[which]
    url = m["url"]
    q = f'<div class="map-qr">{qr_svg(url, "qr")}</div>' if (qr and url) else ""
    go = (f'<a class="go" href="{ESC(url)}" target="_blank" rel="noopener">Open {icon("arrow", 14)}</a>' if url
          else '<span class="go" aria-disabled="true">Soon</span>')
    return (f'<div class="map-slot map-slot--live">{q}<div class="map-txt"><b>{ESC(m["name"])}</b><small>{ESC(m["when"])}</small></div>{go}</div>')
