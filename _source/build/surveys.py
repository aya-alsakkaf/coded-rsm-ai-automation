# -*- coding: utf-8 -*-
"""The three CODED portal surveys (PRE and POST MAP test, final satisfaction survey), built from the kit in English and Arabic
(references/surveys.md). Reads content.MAP, CONFIDENCE, OUTCOMES, FORMS and content.SURVEY (the Arabic texts, folder and
names). Writes the payloads for survey_create / survey_update; nothing here is served. Skipped when the kit has no SURVEY.

    python3 surveys.py OUTDIR      -> OUTDIR/pre.json, post.json, final.json
"""
import json, os, re, sys
import wk
from wk import C, opt

def L(en, ar): return {"en": en, "ar": ar}
NUM = {3: ("Three", "ثلاثة"), 4: ("Four", "أربعة"), 5: ("Five", "خمسة"), 6: ("Six", "ستة"), 7: ("Seven", "سبعة"), 8: ("Eight", "ثمانية"), 9: ("Nine", "تسعة"), 10: ("Ten", "عشرة")}
def slug_ok(s): return bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s)) and len(s) <= 80

def map_payload(kind, S):
    pre = kind == "pre"
    n = len(C.MAP); mins = S.get("test_min", wk.MAP_MIN)
    per_day = {d: sum(1 for q in C.MAP if q["day"] == d) for d in wk.DAYS}
    intro = L(f"This short test has {n} knowledge questions and takes about {mins} minutes. Work alone, and do not use an AI tool or search. If you are not sure, choose the answer you think is most likely; there is no penalty for a wrong answer. You take this same test at the start of Day {wk.FIRST} and at the end of Day {wk.LAST}.",
              f"يتضمن هذا الاختبار القصير {n} سؤالاً معرفياً ويستغرق نحو {mins} دقائق. اعمل بمفردك، ولا تستخدم أي أداة ذكاء اصطناعي أو محرك بحث. إذا لم تكن متأكداً، فاختر الإجابة التي تراها الأرجح؛ لا توجد عقوبة على الإجابة الخاطئة. ستؤدي هذا الاختبار نفسه في بداية اليوم {wk.FIRST} وفي نهاية اليوم {wk.LAST}.")
    sections = [{"id": "s_1", "title": L("Before you start", "قبل أن تبدأ"), "description": L("Please read this, then give us your name, work email and department so that we can match your two sittings.", "يُرجى قراءة ما يلي، ثم تزويدنا باسمك وبريدك الإلكتروني للعمل والإدارة التي تعمل بها لكي نطابق بين محاولتيك.")},
                {"id": "s_2", "title": L("Part 1: Confidence", "الجزء 1: الثقة"), "description": L("Rate each statement 1 to 5. 1 = No idea / never done it. 3 = Could attempt with help. 5 = Could do it confidently on my own. There are no right answers here.",
                                                                                        "قيّم كل عبارة من 1 إلى 5. 1 = لا أعرف / لم أفعله من قبل. 3 = أستطيع المحاولة بمساعدة. 5 = أستطيع فعله بثقة وحدي. لا توجد إجابات صحيحة هنا.")}]
    for i, d in enumerate(wk.DAYS):
        if not per_day[d]: continue
        en, ar = NUM.get(per_day[d], (str(per_day[d]), str(per_day[d])))
        sections.append({"id": f"s_{i + 3}", "title": L(f"Part 2: Day {d}, {C.DAYS[d]['title']}", f"الجزء 2: اليوم {d}، {S['day_ar'][d]}"),
                         "description": L(f"{en} questions. Choose the one best answer.", f"{ar} أسئلة. اختر أفضل إجابة واحدة.")})
    secid = {d: f"s_{i + 3}" for i, d in enumerate(wk.DAYS)}
    qs = [{"id": "q_intro", "type": "statement", "label": intro, "required": False, "sectionId": "s_1"},
          {"id": "q_name", "type": "text", "label": L("Your full name", "اسمك الكامل"), "required": True, "sectionId": "s_1"},
          {"id": "q_email", "type": "email", "label": L("Your work email. We use it only to match your two sittings.", "بريدك الإلكتروني للعمل. نستخدمه فقط لمطابقة محاولتيك."), "required": True, "sectionId": "s_1"},
          {"id": "q_dept", "type": "text", "label": L(*S.get("dept_label", ("Your department", "الإدارة التي تعمل بها"))), "required": True, "sectionId": "s_1"}]
    for i, (en, ar) in enumerate(zip(C.CONFIDENCE, S["confidence_ar"])):
        qs.append({"id": f"q_r{i + 1}", "type": "scale", "label": L(en, ar), "required": True, "sectionId": "s_2",
                   "scaleConfig": {"min": 1, "max": 5, "minLabel": L("1: No idea / never done it", "1: لا أعرف / لم أفعله من قبل"), "maxLabel": L("5: Confidently on my own", "5: بثقة وحدي")}})
    for i, (q, (qar, oar)) in enumerate(zip(C.MAP, S["map_ar"])):
        qs.append({"id": f"q_{i + 1}", "type": "select", "label": L(f"{i + 1}. {q['q']}", f"{i + 1}. {qar}"), "required": True, "sectionId": secid[q["day"]],
                   "options": [{"id": f"opt_{v}", "value": v, "label": L(o, oa)} for v, o, oa in zip("abcd", q["o"], oar)]})
    for i, q in enumerate(qs): q["order"] = i + 1
    for i, s in enumerate(sections): s["order"] = i
    f = wk.FORMS[kind]; other = wk.FORMS["post" if pre else "pre"]
    sitting = (f"PRE sitting: {f['when']}. The POST sitting ({other['when']}) has the identical questions." if pre else
               f"POST sitting: {f['when']}, before the final satisfaction survey. The PRE sitting ({other['when']}) has the identical questions.")
    desc = (f"{S.get('note', '')} MAP Skills Test for {S['program']} \"{C.TITLE}\", {wk.NDAYS} days, {C.DATES}, {C.HOURS}. "
            + " · ".join(f"Day {d}: {C.DAYS[d]['title']}" for d in wk.DAYS) + f". {sitting} Part 1: {len(C.CONFIDENCE)} confidence self-ratings (never scored). "
            f"Part 2: {n} knowledge questions (" + ", ".join(f"Day {d}: {per_day[d]}" for d in wk.DAYS) + f"). About {mins} minutes. Not graded. Answer key: {C.MAP_KEY}.").strip()
    label = f"MAP Test {'PRE (Day ' + str(wk.FIRST) + ')' if pre else 'POST (Day ' + str(wk.LAST) + ')'}"
    label_ar = f"اختبار MAP: {'القبلي (اليوم ' + str(wk.FIRST) + ')' if pre else 'البعدي (اليوم ' + str(wk.LAST) + ')'}"
    return {"name": f"{S['name_prefix']} {C.TITLE}: {label}", "description": desc, "audience": "teacher_student", "isAnonymous": False, "folderId": S["folder"],
            "sections": sections, "questions": qs,
            "_update": {"brandingTitle": L(f"{C.TITLE} · {label}", f"{S['program_ar']} · {label_ar}"), "brandingSubtitle": S["subtitle"],
                        "clientName": S.get("client", ""), "cohortName": S.get("cohort", ""), "slug": f.get("slug", "")}}

def final_payload(S):
    scale = lambda: {"min": 1, "max": 6, "minLabel": L("Strongly disagree", "لا أوافق بشدة"), "maxLabel": L("Strongly agree", "أوافق بشدة")}
    Q = lambda i, sec, en, ar: {"id": i, "type": "scale", "label": L(en, ar), "required": True, "sectionId": sec, "scaleConfig": scale()}
    T = lambda i, en, ar: {"id": i, "type": "textarea", "label": L(en, ar), "required": False, "sectionId": "s_comments"}
    sections = [{"id": "s_1", "title": L("Your feedback", "رأيك")}, {"id": "s_learn", "title": L("What you can do now", "ما أصبحت قادراً عليه")},
                {"id": "s_team", "title": L("Education Team", "فريق التدريب")}, {"id": "s_comments", "title": L("Comments", "ملاحظات")}]
    days = "two days" if wk.NDAYS == 2 else f"{wk.NDAYS} days"; days_ar = "اليومين" if wk.NDAYS == 2 else "الأيام"
    qs = [{"id": "intro", "type": "statement", "required": False, "sectionId": "s_1",
           "label": L("For each statement, tap a number from 1 to 6. 1 = Strongly disagree · 2 = Disagree · 3 = Somewhat disagree · 4 = Somewhat agree · 5 = Agree · 6 = Strongly agree.",
                      "لكل عبارة، اختر رقماً من 1 إلى 6. 1 = لا أوافق بشدة · 2 = لا أوافق · 3 = لا أوافق إلى حدٍّ ما · 4 = أوافق إلى حدٍّ ما · 5 = أوافق · 6 = أوافق بشدة.")},
          {"id": "q_dept", "type": "text", "label": L(*S.get("dept_label", ("Your department", "الإدارة التي تعمل بها"))), "required": False, "sectionId": "s_1"},
          Q("q_2", "s_1", "The program met my expectations as a learning experience.", "لبّى البرنامج توقعاتي كتجربة تعليمية."),
          Q("q_1", "s_1", "I am satisfied with the program overall.", "أنا راضٍ عن البرنامج بشكل عام."),
          Q("q_3", "s_1", *S.get("relevance", ("The content was high quality and relevant to my work.", "كان المحتوى عالي الجودة وذا صلة بعملي."))),
          Q("q_9", "s_1", *S["hands_on"]),
          Q("q_materials", "s_1", *S["materials"]),
          Q("q_pace", "s_1", f"The length and pace of the {days} were right for me.", f"كانت مدة {days_ar} ووتيرتها مناسبة لي."),
          Q("q_logistics", "s_1", *S["logistics"])]
    for i, (en, ar) in enumerate(zip(C.OUTCOMES, S["confidence_ar"]), 1): qs.append(Q(f"q_can{i}", "s_learn", en, ar))
    qs += [Q("q_10", "s_learn", "I will use what I learned, and the tools from the program, in my work.", "سأطبّق ما تعلّمته والأدوات التي حصلت عليها في البرنامج في عملي."),
           Q("q_6", "s_team", "The instructor delivered the program effectively, and the teaching style was clear and easy to follow.", "قدّم المدرّب البرنامج بفعالية، وكان أسلوب التدريس واضحاً وسهل المتابعة."),
           Q("q_7", "s_team", "The instructor and facilitators were knowledgeable, professional, and available to help me.", "كان المدرّب والميسّرون متمكنين ومحترفين ومتاحين لمساعدتي."),
           Q("q_11", "s_team", "I would recommend this program to a colleague.", "أنصح زملائي بهذا البرنامج."),
           T("q_12", f"Which part of the {days} was most useful to you, and why?", f"ما الجزء الأكثر فائدة لك خلال {days_ar}، ولماذا؟"),
           T("q_13", "What would you change or add to make the program better?", "ما الذي تقترح تغييره أو إضافته لتحسين البرنامج؟"),
           T("q_8", "General comments and suggestions", "ملاحظات واقتراحات عامة")]
    for i, q in enumerate(qs): q["order"] = i
    for i, s in enumerate(sections): s["order"] = i
    desc = (f"{S.get('note', '')} End-of-program satisfaction survey for {S['program']} \"{C.TITLE}\", {wk.NDAYS} days ({C.DATES}). Taken at the end of Day {wk.LAST} after the POST MAP test, "
            "about 5 minutes. The same 6-point agreement scale as other CODED programs (1 = Strongly disagree ... 6 = Strongly agree). Bilingual EN/AR.").strip()
    return {"name": f"{S['name_prefix']} {C.TITLE}: Final Satisfaction Survey", "description": desc, "audience": "teacher_student", "isAnonymous": False, "folderId": S["folder"],
            "sections": sections, "questions": qs,
            "_update": {"brandingTitle": L(f"{C.TITLE} · Final Satisfaction Survey", f"{S['program_ar']} · استبيان الرضا الختامي"), "brandingSubtitle": S["subtitle"],
                        "clientName": S.get("client", ""), "cohortName": S.get("cohort", ""), "slug": wk.FORMS["survey"].get("slug", "")}}

def check(S):
    assert len(S["map_ar"]) == len(C.MAP), "SURVEY map_ar needs one (question, [options]) per MAP question"
    assert len(S["confidence_ar"]) == len(C.CONFIDENCE) == len(C.OUTCOMES), "SURVEY confidence_ar needs one line per outcome"
    for q, (qa, oa) in zip(C.MAP, S["map_ar"]): assert len(oa) == len(q["o"]), q["q"]
    for k in ("pre", "post", "survey"):
        sl = wk.FORMS[k].get("slug", "")
        assert slug_ok(sl), f"FORMS[{k!r}] slug must be kebab case and at most 80 characters (the portal cuts longer slugs): {sl!r}"

if __name__ == "__main__":
    S = opt("SURVEY")
    if not S:
        print("surveys: the kit has no SURVEY; no payloads written"); sys.exit(0)
    check(S)
    out = sys.argv[1] if len(sys.argv) > 1 else wk.SURVEY_DIR
    os.makedirs(out, exist_ok=True)
    for name, p in (("pre", map_payload("pre", S)), ("post", map_payload("post", S)), ("final", final_payload(S))):
        t = json.dumps(p, ensure_ascii=False, indent=1)
        assert "—" not in t, f"{name}: em dash in the survey text"
        assert not re.findall(r'"(?:en|ar)": ""', t), f"{name}: an empty label"
        open(os.path.join(out, name + ".json"), "w", encoding="utf-8").write(t)
        print("survey", name, len(p["questions"]), "questions", len(p["description"]), "chars")
