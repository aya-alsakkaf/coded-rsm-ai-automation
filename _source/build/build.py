# -*- coding: utf-8 -*-
"""Builds the whole site into public/. Never hand-edit public/: change the content files and run this again.
Usage: python3 -I _source/build/build.py   (from the repo root, or anywhere)"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PUB = os.path.join(ROOT, "public")

from content_core import CODE, MAP, FILES
import kit_site as S
import kit_deck as K
import content_map as M


def w(rel, text):
    path = os.path.join(PUB, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def favicon():
    from PIL import Image, ImageDraw
    im = Image.new("RGBA", (64, 64), (0, 17, 47, 255))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((4, 4, 59, 59), radius=12, outline=(111, 156, 232, 255), width=3)
    logo = Image.open(os.path.join(HERE, "assets", "coded-logo.png")).convert("RGBA")
    logo.thumbnail((52, 20))
    im.alpha_composite(logo, ((64 - logo.width) // 2, (64 - logo.height) // 2))
    im.save(os.path.join(PUB, f"{CODE}-favicon.png"))


def vercel_json():
    red = [{"source": "/", "destination": f"/{CODE}", "permanent": False}]
    for k in ("pre", "post", "survey"):
        dest = MAP[k]["url"] or f"/{CODE}"
        red.append({"source": f"/{k}", "destination": dest, "permanent": False})
    for n in (1, 2):
        red.append({"source": f"/slides{n}", "destination": f"/{CODE}-day-{n}-deck", "permanent": False})
        red.append({"source": f"/prompts{n}", "destination": f"/{CODE}-prompt-sheet-day-{n}", "permanent": False})
        red.append({"source": f"/day{n}", "destination": f"/{CODE}-day-{n}", "permanent": False})
    sec = [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
           {"key": "X-Frame-Options", "value": "SAMEORIGIN"}, {"key": "X-Robots-Tag", "value": "noindex, nofollow"}]
    nostore = [{"key": "Cache-Control", "value": "private, no-store"}]
    return {"$schema": "https://openapi.vercel.sh/vercel.json", "outputDirectory": "public", "cleanUrls": True, "trailingSlash": False,
            "redirects": red,
            "headers": [{"source": "/(.*)", "headers": sec}, {"source": "/staff", "headers": nostore}, {"source": "/staff/(.*)", "headers": nostore}]}


MIDDLEWARE = r"""// Staff lock: Vercel Routing Middleware. Basic auth on /staff and /staff/*, against STAFF_USER (default "staff")
// and STAFF_PASSWORD. No password set: 503 "locked". Wrong password: 401. Set STAFF_PASSWORD in Vercel, never in code.
import { next } from '@vercel/functions';

export const config = { matcher: ['/staff', '/staff/:path*'] };

const enc = new TextEncoder();
function safeEqual(a, b) {
  const x = enc.encode(a), y = enc.encode(b);
  const len = Math.max(x.length, y.length);
  let diff = x.length ^ y.length;
  for (let i = 0; i < len; i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}
const base = { 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow', 'Content-Type': 'text/plain; charset=utf-8' };

export default function middleware(request) {
  const pass = process.env.STAFF_PASSWORD;
  const user = process.env.STAFF_USER || 'staff';
  if (!pass) return new Response('Locked: the staff password is not set yet.', { status: 503, headers: base });
  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    let decoded = '';
    try { decoded = atob(auth.slice(6)); } catch (e) { decoded = ''; }
    const i = decoded.indexOf(':');
    if (i > -1) {
      const okUser = safeEqual(decoded.slice(0, i), user);
      const okPass = safeEqual(decoded.slice(i + 1), pass);
      if (okUser & okPass) return next();
    }
  }
  return new Response('Authentication required.', { status: 401, headers: { ...base, 'WWW-Authenticate': 'Basic realm="CODED staff", charset="UTF-8"' } });
}
"""


def main():
    if os.path.isdir(PUB):
        shutil.rmtree(PUB)
    os.makedirs(os.path.join(PUB, "staff"))
    # assets
    css = "\n".join(open(os.path.join(HERE, "css", f)).read() for f in sorted(os.listdir(os.path.join(HERE, "css"))))
    w(f"{CODE}-site.css", css)
    for src, dst in [("font-manrope.woff2", "font-manrope.woff2"), ("font-space-mono-400.woff2", "font-space-mono-400.woff2"),
                     ("font-space-mono-700.woff2", "font-space-mono-700.woff2"), ("coded-logo.png", "coded-logo.png")]:
        shutil.copy(os.path.join(HERE, "assets", src), os.path.join(PUB, f"{CODE}-{dst}"))
    favicon()
    # sample files (names never change)
    for f, _, _ in FILES:
        shutil.copy(os.path.join(ROOT, "_source", "files", f), os.path.join(PUB, f))
    # public pages
    w(f"{CODE}.html", S.build_home())
    for d in S.DAYS:
        w(f"{CODE}-day-{d['n']}.html", S.build_day(d))
        w(f"{CODE}-prompt-sheet-day-{d['n']}.html", S.build_prompts(d["n"]))
        w(f"{CODE}-day-{d['n']}-deck.html", K.build_deck(d["n"], staff=False))
        w(f"staff/{CODE}-day-{d['n']}-deck.html", K.build_deck(d["n"], staff=True))
    w(f"{CODE}-cheat-sheet.html", S.build_cheat())
    w(f"{CODE}-safe-use-card.html", S.build_safe())
    w(f"{CODE}-take-home-guide.html", S.build_guide())
    w("404.html", S.build_404())
    w("robots.txt", "User-agent: *\nDisallow: /\n")
    # staff
    w("staff/index.html", S.build_staff_index(M.KEY))
    w(f"staff/{CODE}-facilitator-kit.html", S.build_staff_kit())
    w(f"staff/{CODE}-answer-key.html", S.build_staff_key(M.map_rows()))
    # deploy config
    with open(os.path.join(ROOT, "vercel.json"), "w") as f:
        json.dump(vercel_json(), f, indent=2)
    with open(os.path.join(ROOT, "middleware.js"), "w") as f:
        f.write(MIDDLEWARE)
    with open(os.path.join(ROOT, "package.json"), "w") as f:
        json.dump({"name": CODE, "private": True, "type": "module",
                   "description": "AI Innovation and Automation workshop site, CODED Professionals. Static site in public/, staff lock in middleware.js.",
                   "dependencies": {"@vercel/functions": "3.10.1"}}, f, indent=2)
        f.write("\n")
    n = sum(len(fs) for _, _, fs in os.walk(PUB))
    print(f"built {n} files into public/")


if __name__ == "__main__":
    main()
