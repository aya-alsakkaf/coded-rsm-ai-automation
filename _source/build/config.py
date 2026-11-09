# -*- coding: utf-8 -*-
"""The repo-root files for Vercel, all from the kit's code: vercel.json (clean URLs, the redirects, security headers,
X-Robots-Tag noindex on every path, private no-store on /staff), package.json (named after the code), middleware.js
(the staff password on /staff), .gitignore and .vercelignore. Extra redirects come from content.py REDIRECTS.

    python3 config.py REPO_ROOT
"""
import json, os, sys, shutil
import wk
from wk import P, HUB, DAYS, dayp, deckp, sheetp, labp, cardp, opt

R = lambda s, d: {"source": s, "destination": d, "permanent": False}
def redirects():
    red = [R("/", "/" + HUB)]
    red += [R(f"/{k}", wk.FORMS[k]["url"]) for k in ("pre", "post", "survey") if k in wk.FORMS]
    for d in DAYS:
        red += [R(f"/day{d}", "/" + dayp(d)), R(f"/slides{d}", "/" + deckp(d)), R(f"/deck-day-{d}", "/" + deckp(d)), R(f"/{wk.SHEET['slug']}-day-{d}", "/" + sheetp(d)),
                R(f"/presenter-notes-day-{d}", f"/staff/{P(f'notes-day-{d}')}"), R(f"/demo-runbook-day-{d}", f"/staff/{P(f'runbook-day-{d}')}"),
                R(f"/backup-outputs-day-{d}", f"/staff/{P(f'backup-day-{d}')}"), R(f"/answer-key-day-{d}", f"/staff/{P(f'answer-key-day-{d}')}")]
        if d in wk.LABS: red.append(R(f"/lab-day-{d}", "/" + labp(d)))
    red += [R("/cheat-sheet", "/" + P("cheat-sheet")), R("/" + wk.CARD["slug"], "/" + cardp()), R("/take-home-guide", "/" + P("take-home-guide")),
            R("/facilitator-kit", "/staff/" + P("facilitator-kit")), R("/lesson-plan", "/staff/" + P("lesson-plan")), R("/workshop-index", "/staff")]
    red += [R(s, d) for s, d in opt("REDIRECTS", [])]
    return red
SEC = [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
       {"key": "X-Frame-Options", "value": "SAMEORIGIN"}, {"key": "X-Robots-Tag", "value": "noindex, nofollow"}]
STAFF = [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}, {"key": "Cache-Control", "value": "private, no-store"}]
def vercel():
    return {"$schema": "https://openapi.vercel.sh/vercel.json", "outputDirectory": "public", "cleanUrls": True, "trailingSlash": False, "redirects": redirects(),
            "headers": [{"source": "/(.*)", "headers": SEC}, {"source": "/staff/(.*)", "headers": STAFF}, {"source": "/staff", "headers": STAFF}]}
def package():
    return {"name": wk.PFX, "private": True, "type": "module",
            "description": f"{wk.ORG} · {wk.C.TITLE} workshop site (static, in public/) with a staff password on /staff.",
            "dependencies": {"@vercel/functions": "^3.10.4"}}

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else wk.ROOT
    v = vercel()
    open(os.path.join(root, "vercel.json"), "w", encoding="utf-8").write(json.dumps(v, indent=1) + "\n")
    open(os.path.join(root, "package.json"), "w", encoding="utf-8").write(json.dumps(package(), indent=2) + "\n")
    shutil.copy2(os.path.join(wk.ASSETS, "middleware.js"), os.path.join(root, "middleware.js"))
    open(os.path.join(root, ".gitignore"), "w").write("__pycache__/\n*.pyc\n.DS_Store\nnode_modules/\n.vercel\n")
    open(os.path.join(root, ".vercelignore"), "w").write("_source\nREADME.md\nCLAUDE.md\nCHANGELOG.md\n")
    print(len(v["redirects"]), "redirects -> vercel.json · package.json", wk.PFX)
