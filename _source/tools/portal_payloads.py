# -*- coding: utf-8 -*-
"""Turn the engine's survey payloads (_source/surveys/*.json) into the portal payloads this program uses (surveys.md rules the engine does not
cover yet, see PLUGIN-FEEDBACK.md): a Part 3 section for the 4 work scenarios, the full MAP intro, q_4/q_5/q_can3.., q_ai and q_safe.
    python3 _source/tools/portal_payloads.py      -> _source/surveys/portal-pre.json, portal-post.json, portal-final.json"""
import json, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__)); SV = os.path.join(HERE, "..", "surveys")
sys.path.insert(0, os.path.join(HERE, "..", "kit")); import content as C
L = lambda en, ar: {"en": en, "ar": ar}
N_SCEN = 4; first_scen = len(C.MAP) - N_SCEN + 1        # q_10 .. q_13

def mapfix(p, kind):
    p = copy.deepcopy(p)
    secs = p["sections"]
    for s in secs:
        if s["title"]["en"].startswith("Part 2: Day 2"):
            s["description"] = L("Four questions. Choose the one best answer.", "أربعة أسئلة. اختر أفضل إجابة واحدة.")
        if s["title"]["en"].startswith("Part 2: Day 1"):
            s["description"] = L("Five questions. Choose the one best answer. Mirqab & Co. and Abdali Foods are fictional companies.",
                                 "خمسة أسئلة. اختر أفضل إجابة واحدة. Mirqab & Co. وAbdali Foods شركتان وهميتان.")
    secs.append({"id": "s_5", "title": L("Part 3: Work scenarios", "الجزء 3: مواقف من العمل"),
                 "description": L("Four questions about real work moments. Choose the one best answer.", "أربعة أسئلة عن مواقف حقيقية في العمل. اختر أفضل إجابة واحدة."), "order": len(secs)})
    for q in p["questions"]:
        if q["id"] == "q_intro":
            q["label"]["en"] = q["label"]["en"].replace(" knowledge questions", " questions")
            q["label"]["ar"] = q["label"]["ar"].replace("سؤالاً معرفياً", "سؤالاً")
            q["label"]["en"] += " It is not graded: it shows us how much you learned in the program."
            q["label"]["ar"] += " هذا الاختبار غير مُقيَّم بدرجات: فهو يبيّن لنا مقدار ما تعلّمته في البرنامج."
        if q["id"].startswith("q_") and q["id"][2:].isdigit() and int(q["id"][2:]) >= first_scen:
            q["sectionId"] = "s_5"
    sit = ("PRE sitting: Day 1, Sun 15 Nov 2026, 08:35 (10 minutes). The POST sitting at the end of Day 2 (Mon 16 Nov, 16:10) has the identical questions."
           if kind == "pre" else
           "POST sitting: Day 2, Mon 16 Nov 2026, 16:10 (10 minutes), before the final satisfaction survey. The PRE sitting (Day 1, Sun 15 Nov, 08:35) has the identical questions.")
    p["description"] = (f"MAP Skills Test for the CODED Professionals client program \"{C.TITLE}\" for RSM Albazie, cohort RSM-AI-Nov/Nov-26, 2 days at {C.VENUE}, {C.HOURS}: "
                        + " · ".join(f"Day {d}, {['', 'Sun 15 Nov 2026', 'Mon 16 Nov 2026'][d]}: {C.DAYS[d]['title']}" for d in (1, 2)) + f". {sit} "
                        f"Part 1: {len(C.CONFIDENCE)} confidence self-ratings (never scored). Part 2: 9 knowledge questions (Day 1: 5, Day 2: 4). Part 3: 4 work scenarios. "
                        f"About 10 minutes. Not graded. Answer key: {C.MAP_KEY}.")
    lbl = "PRE (Day 1)" if kind == "pre" else "POST (Day 2)"
    p["_update"]["brandingTitle"]["en"] = f"{C.TITLE} · MAP Test: {lbl}"
    return p

def finalfix(p):
    p = copy.deepcopy(p)
    ren = {"q_can1": "q_4", "q_can2": "q_5"}
    qs = []
    for q in p["questions"]:
        q["id"] = ren.get(q["id"], q["id"])
        if q["id"] == "q_10":
            sc = q["scaleConfig"]
            qs.append({"id": "q_ai", "type": "scale", "label": L("I check Claude's numbers and sentences before I use them.", "أتحقق من أرقام Claude وعباراته قبل أن أستخدمها."),
                       "required": True, "sectionId": "s_learn", "scaleConfig": sc})
            qs.append({"id": "q_safe", "type": "scale", "label": L("I know which data must never go into Claude.", "أعرف البيانات التي لا يجوز إدخالها إلى Claude أبداً."),
                       "required": True, "sectionId": "s_learn", "scaleConfig": sc})
        qs.append(q)
    for q in qs:
        if q["id"] == "q_pace": q["label"]["ar"] = q["label"]["ar"].replace("ووتيرتها", "ووتيرتهما")
    for i, q in enumerate(qs): q["order"] = i
    p["questions"] = qs
    p["description"] = (f"End-of-program satisfaction survey for CODED × RSM Albazie \"{C.TITLE}\", 2-day program, 15 to 16 Nov 2026, CODED Alsharekh classroom, Frontend Campus, cohort RSM-AI-Nov/Nov-26. "
                        "Taken at the end of Day 2 after the POST MAP test, about 5 minutes. Same 6-point agreement scale as other CODED programs (1 = Strongly disagree ... 6 = Strongly agree). Bilingual EN/AR.")
    return p

for kind, fn in (("pre", lambda p: mapfix(p, "pre")), ("post", lambda p: mapfix(p, "post")), ("final", finalfix)):
    src = json.load(open(os.path.join(SV, f"{kind}.json"), encoding="utf-8"))
    out = fn(src)
    json.dump(out, open(os.path.join(SV, f"portal-{kind}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ids = [q["id"] for q in out["questions"]]
    assert len(ids) == len(set(ids)), f"duplicate ids in {kind}"
    print(kind, len(out["questions"]), "questions,", len(out["sections"]), "sections")
