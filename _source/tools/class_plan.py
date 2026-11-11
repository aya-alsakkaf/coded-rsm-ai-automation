# -*- coding: utf-8 -*-
"""Write CLASS-PLAN.md at the repo root from the kit: days, blocks, tasks, minutes and points.
    python3 _source/tools/class_plan.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.join(HERE, "..", "kit"); sys.path.insert(0, KIT)
import content as C, content_demos as CD
def mins(r):
    a, b = r.split("-"); f = lambda t: int(t[:2]) * 60 + int(t[3:])
    return f(b) - f(a)
out = [f"# Class plan · {C.TITLE}", "", f"CODED × RSM Albazie · {C.DATES} · {C.HOURS} · {C.VENUE}", "",
       "Generated from `_source/kit/` by `_source/tools/class_plan.py`. Do not edit by hand.", ""]
for d, D in C.DAYS.items():
    out += [f"## Day {d} · {C.DAYDATE[d]} · {D['title']}", "", f"**Claim:** {D['claim']}  ", f"**Integration:** {D['artifact']}", "",
            "| Time | Block | Minutes | What happens |", "|---|---|---|---|"]
    out += [f"| {t} | {n} | {mins(t)} | {w or 'Break'} |" for t, n, w in D["blocks"]]
    teach = sum(mins(t) for t, n, w in D["blocks"] if w)
    out += ["", f"Teaching minutes: {teach}.", "", "| Task | Title | Minutes | Who | Files | Deliverable |", "|---|---|---|---|---|---|"]
    for k, v in CD.DEMOS.items():
        if v["day"] == d and v.get("hands_on"):
            out.append(f"| {v['skill']} | {v['title']} | {v['minutes']} | {v['solo']} | {', '.join(v['files']) or 'your own work'} | {v['deliverable']} |")
    out.append("")
out += ["## Scored work", "", "Demo Day (Day 2, 15:15): each team's automation, 50 points (task relevance 10, working functionality 10, source accuracy 10, human controls 10, test evidence 10).", "",
        f"MAP: {len(C.MAP)} questions, the same on Day 1 (08:35) and Day 2 (16:10), not graded. The key is in the portal description and the Day 2 staff answer key.", ""]
open(os.path.join(HERE, "..", "..", "CLASS-PLAN.md"), "w", encoding="utf-8").write("\n".join(out))
print("CLASS-PLAN.md written")
