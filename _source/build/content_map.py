# -*- coding: utf-8 -*-
"""MAP tests (PRE and POST, identical questions) and the final satisfaction survey, bilingual EN/AR.
Written by CODED from the workshop content (there was no handoff kit). Model: Finance Iter 2 in the portal.
The answer key goes only in the portal description and the staff answer key, never on a participant page.
Run this file to write the portal payloads to _source/surveys/."""
import json
import os

PROG_EN, PROG_AR = "AI Innovation and Automation", "الابتكار والأتمتة بالذكاء الاصطناعي"
CLIENT_EN, CLIENT_AR = "RSM Albazie", "آر إس إم البزيع"
NAME = f"CODED × {CLIENT_EN} {PROG_EN}"
SLUG = "coded-rsm-albazie-ai-innovation-and-automation"   # matches the portal slugs
COHORT = "RSM-AI-Nov/Nov-26"


def L(en, ar):
    return {"en": en, "ar": ar}


CONF = [
    ("I can find the tasks in my work that are worth automating.", "أستطيع تحديد المهام في عملي التي تستحق الأتمتة."),
    ("I can design an AI agent with a clear input, instruction and output.", "أستطيع تصميم وكيل ذكاء اصطناعي بمدخلات وتعليمات ومخرجات واضحة."),
    ("I can build a working agent in Claude.", "أستطيع بناء وكيل يعمل في Claude."),
    ("I can test an agent and improve its instruction.", "أستطيع اختبار الوكيل وتحسين تعليماته."),
    ("I can build a workflow in n8n that connects input, AI and output.", "أستطيع بناء سير عمل في n8n يربط المدخلات والذكاء الاصطناعي والمخرجات."),
    ("I can present an automation and choose the next task to automate.", "أستطيع عرض حل أتمتة واختيار المهمة التالية للأتمتة."),
]

# (question EN, AR, [(option EN, AR) x4], correct letter, day)
MAPQ = [
    ("Which task is the best first candidate for an AI agent?", "أيّ مهمة هي أفضل مرشح أول لوكيل ذكاء اصطناعي؟",
     [("Deciding whether to accept a high-risk client", "تقرير قبول عميل عالي المخاطر أو رفضه"),
      ("Checking the expiry date of every document in a KYC pack", "التحقق من تاريخ انتهاء كل مستند في ملف اعرف عميلك (KYC)"),
      ("Agreeing an adjustment with a client's CFO", "الاتفاق على قيد تسوية مع المدير المالي للعميل"),
      ("Choosing the audit team for a new engagement", "اختيار فريق التدقيق لمهمة جديدة")], "b", 1),
    ("In the Agent Design Framework, what are the three parts of an agent?", "في إطار تصميم الوكلاء، ما الأجزاء الثلاثة للوكيل؟",
     [("Prompt, model and answer", "الأمر النصي والنموذج والإجابة"),
      ("Data, chart and report", "البيانات والرسم البياني والتقرير"),
      ("Input, instruction and output", "المدخلات والتعليمات والمخرجات"),
      ("Trigger, action and alert", "المُشغِّل والإجراء والتنبيه")], "c", 1),
    ("An agent cannot find a document it needs in the file. What should a well-written instruction make it do?",
     "لم يجد الوكيل مستنداً يحتاجه في الملف. ماذا يجب أن تجعله التعليمات الجيدة يفعل؟",
     [("Write \"Not found\" and flag the item for review", "أن يكتب \"Not found\" (غير موجود) ويضع علامة على البند للمراجعة"),
      ("Make the most likely guess", "أن يضع أرجح تخمين"),
      ("Skip the item without saying anything", "أن يتجاوز البند دون أن يذكر شيئاً"),
      ("Stop and give no output at all", "أن يتوقف ولا يعطي أي مخرجات")], "a", 1),
    ("Why can an AI model give a wrong date when you do not attach the file?", "لماذا قد يعطي نموذج الذكاء الاصطناعي تاريخاً خاطئاً عندما لا ترفق الملف؟",
     [("Dates are not allowed in prompts", "لأن التواريخ غير مسموح بها في الأوامر النصية"),
      ("It reads an old copy of the file", "لأنه يقرأ نسخة قديمة من الملف"),
      ("It always rounds numbers and dates", "لأنه يقرّب الأرقام والتواريخ دائماً"),
      ("It writes by predicting likely words, so it can guess", "لأنه يكتب بتوقع الكلمات المحتملة، لذلك قد يخمّن")], "d", 1),
    ("Your agent gives a wrong answer in a test. What is the best next step?", "أعطى وكيلك إجابة خاطئة في أحد الاختبارات. ما أفضل خطوة تالية؟",
     [("Correct the answer by hand and continue", "تصحيح الإجابة يدوياً والمتابعة"),
      ("Change the instruction, then run all the test cases again", "تعديل التعليمات، ثم تشغيل جميع حالات الاختبار من جديد"),
      ("Delete the test case that failed", "حذف حالة الاختبار التي فشلت"),
      ("Ask the same question again until the answer changes", "طرح السؤال نفسه مرة أخرى حتى تتغير الإجابة")], "b", 1),
    ("In an automated workflow, what does the trigger do?", "في سير العمل المؤتمت، ما وظيفة المُشغِّل (Trigger)؟",
     [("It starts the workflow when something happens, for example when a form is sent", "يبدأ سير العمل عند حدوث أمر ما، مثل إرسال نموذج"),
      ("It checks that the AI's answer is correct", "يتحقق من صحة إجابة الذكاء الاصطناعي"),
      ("It stores the result in a table", "يحفظ النتيجة في جدول"),
      ("It sends the final report to the client", "يرسل التقرير النهائي إلى العميل")], "a", 2),
    ("Why do you ask Claude for named fields (structured output) inside a workflow?", "لماذا تطلب من Claude حقولاً مسمّاة (مخرجات منظمة) داخل سير العمل؟",
     [("It makes the answer longer and more detailed", "لأنها تجعل الإجابة أطول وأكثر تفصيلاً"),
      ("It hides the answer from the reviewer", "لأنها تخفي الإجابة عن المراجع"),
      ("The next step, for example an IF, can read one field and choose a route", "لأن الخطوة التالية، مثل IF، تستطيع قراءة حقل واحد واختيار المسار"),
      ("It is needed to sign in to n8n", "لأنها مطلوبة لتسجيل الدخول إلى n8n")], "c", 2),
    ("In the KYC workflow, which step turns the uploaded PDF into text that Claude can read?",
     "في سير عمل KYC، ما الخطوة التي تحوّل ملف PDF المرفوع إلى نص يستطيع Claude قراءته؟",
     [("The data table", "جدول البيانات (Data table)"), ("Extract from File", "خطوة Extract from File"),
      ("The IF node", "عقدة IF"), ("The Form Ending page", "صفحة Form Ending")], "b", 2),
    ("In a KYC workflow, where should the human check sit?", "في سير عمل KYC، أين يجب أن تكون المراجعة البشرية؟",
     [("Before the trigger, so nothing runs without approval", "قبل المُشغِّل، حتى لا يعمل أي شيء دون موافقة"),
      ("Nowhere, because the agent passed its tests", "لا حاجة إليها، لأن الوكيل اجتاز اختباراته"),
      ("Only once a year, at the year-end review", "مرة واحدة في السنة فقط، عند مراجعة نهاية السنة"),
      ("After the AI decides, before anything is sent to the client or marked accepted", "بعد أن يقرر الذكاء الاصطناعي، وقبل إرسال أي شيء إلى العميل أو اعتماد القبول")], "d", 2),
    ("Before an agent workflow is used on real client work, what must it have?", "قبل استخدام سير عمل الوكيل في عمل فعلي لعميل، ماذا يجب أن يتوفر له؟",
     [("A named owner, a test set and a review rule", "مسؤول محدد بالاسم، ومجموعة اختبارات، وقاعدة للمراجعة"),
      ("A company logo and a color theme", "شعار الشركة ونظام ألوان"),
      ("At least ten steps", "عشر خطوات على الأقل"),
      ("A weekly schedule trigger", "مُشغِّل مجدول أسبوعياً")], "a", 2),
]

KEY = " · ".join(f"{i + 1} {q[3]}" for i, q in enumerate(MAPQ))
D1 = sum(1 for q in MAPQ if q[4] == 1)
D2 = len(MAPQ) - D1


def map_rows():
    """for the staff answer key: (number, question, answer text)"""
    out = []
    for i, (q, _, opts, k, _d) in enumerate(MAPQ):
        out.append((str(i + 1), q, f"{k}) " + opts["abcd".index(k)][0]))
    return out


def map_payload(which):
    pre = which == "pre"
    sit = "PRE (Day 1)" if pre else "POST (Day 2)"
    sit_ar = "القبلي (اليوم 1)" if pre else "البعدي (اليوم 2)"
    sections = [
        {"id": "s_1", "order": 0, "title": L("Before you start", "قبل أن تبدأ"),
         "description": L("Please read this, then give us your name, work email and department so that we can match your two sittings.",
                          "يرجى قراءة ما يلي، ثم كتابة اسمك وبريدك الإلكتروني للعمل والإدارة التي تعمل بها، حتى نتمكن من مطابقة محاولتيك.")},
        {"id": "s_2", "order": 1, "title": L("Part 1: Confidence", "الجزء 1: الثقة"),
         "description": L("Rate each statement 1 to 5. 1 = No idea / never done it. 3 = Could attempt with help. 5 = Could do it confidently on my own. There are no right answers here.",
                          "قيّم كل عبارة من 1 إلى 5. ‏1 = لا أعرف / لم أفعله من قبل. ‏3 = أستطيع المحاولة بمساعدة. ‏5 = أستطيع فعله بثقة وحدي. لا توجد إجابات صحيحة أو خاطئة هنا.")},
        {"id": "s_3", "order": 2, "title": L("Part 2: Day 1, Designing AI Agents for Real Work", "الجزء 2: اليوم 1، تصميم وكلاء الذكاء الاصطناعي للعمل الفعلي"),
         "description": L("Five questions. Choose the one best answer.", "خمسة أسئلة. اختر أفضل إجابة واحدة.")},
        {"id": "s_4", "order": 3, "title": L("Part 2: Day 2, Turning Agents into Operational Workflows", "الجزء 2: اليوم 2، تحويل الوكلاء إلى سير عمل تشغيلي"),
         "description": L("Five questions. Choose the one best answer.", "خمسة أسئلة. اختر أفضل إجابة واحدة.")},
    ]
    qs = [
        {"id": "q_intro", "type": "statement", "required": False, "order": 1, "sectionId": "s_1",
         "label": L(f"This short test has {len(MAPQ)} knowledge questions and takes about 10 minutes. Work alone, and do not use an AI tool or search. "
                    "If you are not sure, choose the answer you think is most likely; there is no penalty for a wrong answer. You take this same test at the start of Day 1 "
                    "and at the end of Day 2. It is not graded: it shows us how much the program moved you.",
                    f"يتكون هذا الاختبار القصير من {len(MAPQ)} أسئلة معرفية ويستغرق نحو 10 دقائق. أجب وحدك، ولا تستخدم أي أداة ذكاء اصطناعي أو بحث. "
                    "إذا لم تكن متأكداً، فاختر الإجابة التي تراها الأرجح؛ فلا توجد عقوبة على الإجابة الخاطئة. ستؤدي الاختبار نفسه في بداية اليوم الأول "
                    "وفي نهاية اليوم الثاني. هذا الاختبار غير مُقيَّم بدرجات: فهو يبيّن لنا مدى تقدمك خلال البرنامج.")},
        {"id": "q_name", "type": "text", "required": True, "order": 2, "sectionId": "s_1", "label": L("Your full name", "اسمك الكامل")},
        {"id": "q_email", "type": "email", "required": True, "order": 3, "sectionId": "s_1",
         "label": L("Your work email. We use it only to match your two sittings.", "بريدك الإلكتروني للعمل. نستخدمه فقط لمطابقة محاولتيك.")},
        {"id": "q_dept", "type": "text", "required": True, "order": 4, "sectionId": "s_1", "label": L("Your department", "الإدارة التي تعمل بها")},
    ]
    order = 5
    for i, (en, ar) in enumerate(CONF):
        qs.append({"id": f"q_r{i + 1}", "type": "scale", "required": True, "order": order, "sectionId": "s_2", "label": L(en, ar),
                   "scaleConfig": {"min": 1, "max": 5, "minLabel": L("1: No idea / never done it", "1: لا أعرف / لم أفعله من قبل"),
                                   "maxLabel": L("5: Confidently on my own", "5: بثقة وحدي")}})
        order += 1
    for i, (en, ar, opts, k, day) in enumerate(MAPQ):
        qs.append({"id": f"q_{i + 1}", "type": "select", "required": True, "order": order, "sectionId": "s_3" if day == 1 else "s_4",
                   "label": L(f"{i + 1}. {en}", f"{i + 1}. {ar}"),
                   "options": [{"id": f"opt_{l}", "value": l, "label": L(o[0], o[1])} for l, o in zip("abcd", opts)]})
        order += 1
    other = "POST sitting at the end of Day 2 (15:55)" if pre else "PRE sitting at the start of Day 1 (08:45)"
    when = "PRE sitting: start of Day 1, 08:45 (10 minutes)." if pre else "POST sitting: end of Day 2, 15:55 (10 minutes), before the final satisfaction survey."
    desc = (f"MAP Skills Test for the CODED Professionals client program \"{PROG_EN}\" for {CLIENT_EN}, cohort {COHORT}, 2 days at CODED (Morning Alsharekh), 08:30-16:30: "
            "Day 1, Sun 15 Nov 2026: Designing AI Agents for Real Work · Day 2, Mon 16 Nov 2026: Turning Agents into Operational Workflows. "
            f"{when} The {other} has the identical questions. Part 1: {len(CONF)} confidence self-ratings (never scored). "
            f"Part 2: {len(MAPQ)} knowledge questions (Day 1: {D1}, Day 2: {D2}), written by CODED from the workshop content (there was no handoff kit). "
            f"About 10 minutes. Not graded. Answer key: {KEY}.")
    return {
        "name": f"{NAME}: MAP Test {'PRE (Day 1)' if pre else 'POST (Day 2)'}",
        "slug": f"{SLUG}-map-test-{'pre-day-1' if pre else 'post-day-2'}",
        "description": desc, "audience": "teacher_student", "isAnonymous": False,
        "brandingTitle": L(f"{PROG_EN} · MAP Test: {sit}", f"{PROG_AR} · اختبار MAP: {sit_ar}"),
        "brandingSubtitle": L(f"CODED × {CLIENT_EN}", f"CODED × {CLIENT_AR}"),
        "clientName": CLIENT_EN, "cohortName": COHORT, "sections": sections, "questions": qs,
    }


S6 = {"min": 1, "max": 6, "minLabel": L("Strongly disagree", "لا أوافق بشدة"), "maxLabel": L("Strongly agree", "أوافق بشدة")}


def survey_payload():
    sections = [{"id": "s_1", "order": 0, "title": L("Your feedback", "رأيك")},
                {"id": "s_learn", "order": 1, "title": L("What you can do now", "ما أصبحت قادراً عليه")},
                {"id": "s_team", "order": 2, "title": L("Education Team", "فريق التدريب")},
                {"id": "s_comments", "order": 3, "title": L("Comments", "ملاحظات")}]
    rated = [
        ("s_1", "q_2", "The program met my expectations as a learning experience.", "لبّى البرنامج توقعاتي كتجربة تعليمية."),
        ("s_1", "q_1", "I am satisfied with the program overall.", "أنا راضٍ عن البرنامج بشكل عام."),
        ("s_1", "q_3", f"The content was high quality and relevant to my work at {CLIENT_EN}.", f"كان المحتوى عالي الجودة وذا صلة بعملي في {CLIENT_AR}."),
        ("s_1", "q_9", "The hands-on parts, such as the agent builds in Claude, the n8n workflows, the practice files and the prompt sheets, helped me apply what I learned.",
         "ساعدتني الأجزاء التطبيقية، مثل بناء الوكلاء في Claude وسير العمل في n8n والملفات التدريبية وأوراق الأوامر النصية (Prompts)، على تطبيق ما تعلّمته."),
        ("s_1", "q_materials", "The program website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
         "كان موقع البرنامج وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد البرنامج واضحة ومفيدة."),
        ("s_1", "q_pace", "The length and pace of the 2 days were right for me.", "كانت مدة اليومين ووتيرتهما مناسبة لي."),
        ("s_1", "q_logistics", "The venue, the daily timing and access to Claude and n8n worked well for me.",
         "كان المكان والتوقيت اليومي وإمكانية الوصول إلى Claude وn8n مناسبة لي."),
        ("s_learn", "q_4", "I can find the tasks in my work that are worth automating.", "أستطيع تحديد المهام في عملي التي تستحق الأتمتة."),
        ("s_learn", "q_5", "I can design an AI agent with a clear input, instruction and output.", "أستطيع تصميم وكيل ذكاء اصطناعي بمدخلات وتعليمات ومخرجات واضحة."),
        ("s_learn", "q_build", "I can build a working agent in Claude and test it.", "أستطيع بناء وكيل يعمل في Claude واختباره."),
        ("s_learn", "q_workflow", "I can turn an agent into a workflow in n8n.", "أستطيع تحويل الوكيل إلى سير عمل في n8n."),
        ("s_learn", "q_ai", "I check Claude's numbers and sentences before I use them.", "أتحقق من أرقام Claude وعباراته قبل أن أستخدمها."),
        ("s_learn", "q_safe", "I know which data must never go into an AI tool.", "أعرف البيانات التي لا يجوز إدخالها إلى أي أداة ذكاء اصطناعي أبداً."),
        ("s_learn", "q_10", "I will use what I learned, and the tools from the program, in my work.", "سأطبّق ما تعلّمته والأدوات التي حصلت عليها في البرنامج في عملي."),
        ("s_team", "q_6", "The instructor delivered the program effectively, and the teaching style was clear and easy to follow.",
         "قدّم المدرّب البرنامج بفعالية، وكان أسلوب التدريس واضحاً وسهل المتابعة."),
        ("s_team", "q_7", "The instructor and facilitators were knowledgeable, professional, and available to help me.", "كان المدرّب والميسّرون متمكنين ومحترفين ومتاحين لمساعدتي."),
        ("s_team", "q_11", "I would recommend this program to a colleague.", "أنصح زملائي بهذا البرنامج."),
    ]
    qs = [{"id": "intro", "type": "statement", "required": False, "order": 0, "sectionId": "s_1",
           "label": L("For each statement, tap a number from 1 to 6. 1 = Strongly disagree · 2 = Disagree · 3 = Somewhat disagree · 4 = Somewhat agree · 5 = Agree · 6 = Strongly agree.",
                      "لكل عبارة، اختر رقماً من 1 إلى 6. 1 = لا أوافق بشدة · 2 = لا أوافق · 3 = لا أوافق إلى حدٍّ ما · 4 = أوافق إلى حدٍّ ما · 5 = أوافق · 6 = أوافق بشدة.")},
          {"id": "q_dept", "type": "text", "required": False, "order": 1, "sectionId": "s_1", "label": L("Your department", "الإدارة التي تعمل بها")}]
    o = 2
    for sec, qid, en, ar in rated:
        qs.append({"id": qid, "type": "scale", "required": True, "order": o, "sectionId": sec, "label": L(en, ar), "scaleConfig": S6})
        o += 1
    for qid, en, ar in [("q_12", "Which part of the 2 days was most useful to you, and why?", "ما الجزء الأكثر فائدة لك خلال اليومين، ولماذا؟"),
                        ("q_13", "What would you change or add to make the program better?", "ما الذي تقترح تغييره أو إضافته لتحسين البرنامج؟"),
                        ("q_8", "General comments and suggestions", "ملاحظات واقتراحات عامة")]:
        qs.append({"id": qid, "type": "textarea", "required": False, "order": o, "sectionId": "s_comments", "label": L(en, ar)})
        o += 1
    desc = (f"End-of-program satisfaction survey for CODED × {CLIENT_EN} \"{PROG_EN}\", 2-day program (15-16 Nov 2026, CODED, Morning Alsharekh), cohort {COHORT}. "
            "Taken at the end of Day 2 after the POST MAP test, about 5 minutes. Same 6-point agreement scale as other CODED programs "
            "(1 = Strongly disagree ... 6 = Strongly agree). Bilingual EN/AR.")
    return {"name": f"{NAME}: Final Satisfaction Survey", "slug": f"{SLUG}-final-satisfaction-survey", "description": desc,
            "audience": "teacher_student", "isAnonymous": False,
            "brandingTitle": L(f"{PROG_EN} · Final Satisfaction Survey", f"{PROG_AR} · استبيان الرضا الختامي"),
            "brandingSubtitle": L(f"CODED × {CLIENT_EN}", f"CODED × {CLIENT_AR}"),
            "clientName": CLIENT_EN, "cohortName": COHORT, "sections": sections, "questions": qs}


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "surveys")
    os.makedirs(out, exist_ok=True)
    for k, p in [("map-pre", map_payload("pre")), ("map-post", map_payload("post")), ("final-survey", survey_payload())]:
        with open(os.path.join(out, k + ".json"), "w") as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
        print(k, p["name"], len(p["questions"]), "questions", len(p["slug"]), "slug chars")
    print("KEY:", KEY, "| day split", D1, D2)
