# Day 2 speaker notes as a script: what the trainer says, word for word (Aya, 15 Nov, same pattern as notes_day1.py).
# SCRIPT[slide id] = (short cue or None, what to say). Words in (brackets) are stage directions, not to be read aloud.
# build_deck.day2() applies this: live demos keep their click steps and fallback; tasks keep the answer key and fallback; checks keep the answer.
# Rebuilt on 15 Nov night for the new Day 2 order: skills, artifacts, scheduled tasks, Claude or n8n or Power Automate, mini project, demos, close.

HANDS = "Ask for hands up on each option, then tap the most popular one."

SCRIPT = {
 "cover2": ("Leave this up while people arrive. Press → at 08:30.",
  "Good morning, and welcome back. Please open claude.ai and the workshop site on your laptop. Today's prompts are on the Day 2 prompt sheet: open it with the button on the Day 2 page. We start in a few minutes."),
 "outcomes2": (None,
  "Here is today. This morning we learn three tools, one by one: skills, artifacts and scheduled tasks. After lunch we look at where Claude stops and tools like n8n and Power Automate take over. "
  "Then the afternoon is yours: you build one agent for one department, from the card to the schedule. Which of these matters most for your work? (Take two answers.)"),
 "road2": (None,
  "This is our day in six short lessons. Skills first, then artifacts, then schedules, all before lunch. After lunch, a short lesson on automation tools, and then the mini project. "
  "At 14:40 I pick a few projects to show the room. We finish at 15:30 with the post-test, the survey and your certificates. Breaks about every hour; Dhuhr at 11:30, Asr at 14:25."),
 "c1rule": ("Click Scheduled in the left sidebar and open the 16:25 run.",
  "Before we start, look at this. (Open the 16:25 run.) Yesterday afternoon, nobody touched a laptop, and the scheduled task still ran by itself and did the work. "
  "By the end of today, your own work runs like that. First, two quick questions about yesterday."),
 "c1chk1": (HANDS,
  "Where do this month's invoices go? (Wait for hands.) The middle one: this month's files come with each run. Knowledge is only for what stays the same."),
 "c1chk2": (HANDS,
  "And an invoice with no PO number? (Wait for hands.) The first one: Not found, with a note. A guess or a blank hides the gap from the reviewer."),
 "s1story": (None,
  "Lesson 1, skills. Dana's agent is good, but it lives in her Project only. When her colleagues want the same method, they would have to copy her whole Project, and soon there are three versions. "
  "How does the firm share a method today? (Expected: a manual, an audit program, a template.) Right. A skill is that, for Claude."),
 "s1blocks": ("Point to one column at a time.",
  "Many people mix up these four words, so let us put them side by side. A prompt is the request you type right now: it is gone when the chat ends. "
  "Project instructions are a standing brief, but only for that one Project. A skill is a method Claude keeps on your account and opens when your request fits it, in any chat or schedule. "
  "And an agent is not one more button: it is all of these working together to do one job. Look at the last row: a question to a colleague, the planning memo, the audit program, and the trained associate."),
 "s1why": (None,
  "So why do we need all of them? Because each one fixes a different gap. The prompt is this run. The Project keeps the client context and the template. The skill keeps the method, so it works anywhere. "
  "The input is the file it reads, and the schedule brings the time. Take one away and something breaks: no skill, and your colleagues cannot use it; no input, and there is nothing to check; no schedule, and someone must press Send."),
 "s1pick": (None,
  "How does Claude know which skill to use? It does not read every skill in full each time. It reads the short description first. If your request fits, it opens the whole skill. "
  "So the description is the most important line you write. If it says helps with Excel, Claude will not know when to use it. If it says match supplier invoices to a purchase ledger, it will."),
 "s1chk": (HANDS,
  "Your method must work everywhere, including on a schedule, for the whole team. (Wait for hands.) The skill, with a clear description. A Project stays in one place, and a saved prompt has to be pasted every time."),
 "s1demo": (None,
  "Let me show you my skill from yesterday's invoice demo. (Open Customize, then Skills, then mirqab-invoice-match.) Look at the name, the description, and the steps: the same five parts we wrote yesterday. "
  "Now a fresh chat, outside any Project. I attach the two files and type one line. (Send the Run line.) Watch for the line where Claude says it is using the skill. Same table as yesterday, with no Project. "
  "Now a different request: a thank-you email. No skill this time, because the description does not fit. Yesterday you used your own tasks for the Agent Card, so now you do the same for the skill."),
 "s1task": ("Start the timer. Walk the room. Hint at 8 minutes: check the description.",
  "Your turn, with your own task, not the invoices. Open your Agent Card from yesterday. Paste it into the first prompt on today's prompt sheet, and answer Claude's questions honestly. "
  "When Claude shows the skill, save it, and check it appears under Customize, then Skills. Then ask Claude to make a fake test file with two hidden problems, and test your skill on it in a new chat. "
  "No real client names anywhere. You have 25 minutes."),
 "s1task2": ("Start the timer. Walk the room.",
  "Now we test the description. Open three new chats. In the first, request your task the way you normally would. In the second, change the wording. In the third, ask for something unrelated, like an email. "
  "The first two should use your skill; the third should not. If one fails, use the prompt on the sheet to sharpen the description, save it again, and test again. Eight minutes."),
 "s1safe": (HANDS,
  "Last question on skills. Before you share one with your team, what matters? (Wait for hands.) The middle one. No client names, no real figures, and it passed a test in a fresh chat. Then it is safe to share, and it works."),
 "a2story": (None,
  "Lesson 2, artifacts. Picture Faisal on a Thursday. He opens a status file with six tabs and scrolls for ten minutes to find three numbers: what is overdue, what is over budget, what has not been collected. "
  "What would help him most? (Expected: a summary, a dashboard.) Yes. The three numbers on top, the details underneath."),
 "a2term": (None,
  "An artifact is a file Claude builds beside the chat. Not a paragraph of text: something you can click, filter, edit and download. A chart, a dashboard, a small tool, or a deck of slides. "
  "And you change it by talking: make the title shorter, add a filter, use a bar chart. It updates in place."),
 "a2cards": (None,
  "Three kinds you will use most. A dashboard, for the people who decide. A presentation, for a meeting. And a small tool, like a tracker or a checklist your team clicks. "
  "The same data can feed all three, so the numbers must match everywhere."),
 "a2dept": ("Ask each department in the room which row is theirs.",
  "Here is what this looks like across RSM's departments. Audit sees open findings by risk. Tax sees what is due this week. Finance sees budget against actual. HR, cyber, ESG: the same idea, a different file. "
  "Which row is closest to your work? (Take answers.) This afternoon you build one of these for real."),
 "a2five": (None,
  "To get a good artifact, ask in five parts, like the five-part prompt yesterday. Who reads it. Which file. Which numbers, and how each one is calculated. How it is laid out. And the rules: calculate with code, and put anything blank or strange under Data issues, never hide it."),
 "a2chk": (HANDS,
  "A tile says thirteen findings are overdue. (Wait for hands.) The first one. Filter the file and count them yourself. Claude may say it is sure and still be wrong, and rounding hides the check."),
 "a2demo": (None,
  "Let me build one. (Attach the engagement portfolio and send the Dashboard request.) While it works, look at what I asked for: the reader, six KPIs with their formulas, two charts, a table and a filter. "
  "(When it appears, click a service line.) Now the most important part: I check two tiles against the file. And look at Data issues: two rows the dashboard did not hide. "
  "Now the same chat: turn it into five slides for Monday's partners' meeting. Same numbers, different reader."),
 "a2task": ("Start the timer. Walk the room. Hint at 7 minutes: look for blanks and duplicates.",
  "Your turn. Pick one department pack from the lab page, step 3, or use your own test file from this morning. Copy the dashboard request, fill the brackets for your reader and your KPIs, and send it. "
  "Then the important part: check three tiles yourself in Excel. Every pack hides two problems. Did your dashboard find them? Twenty minutes."),
 "a2agent": (None,
  "Here is how artifacts become part of your agent. Write the layout into your skill: these tiles, these charts, this table, in this order. "
  "Next month you drop in the new file and get the identical layout back. Partners can compare this month with last month at a glance."),
 "a2task2": ("Start the timer. Walk the room.",
  "Now two things in fifteen minutes. First, in the same chat, turn your dashboard into a short presentation for a real meeting: you choose the audience. Check that every number on the slides is also on the dashboard. "
  "Second, put the layout into your skill with the second prompt, and save the skill again. That is your agent learning its output."),
 "a2gallery": ("Pick three people, from different departments if you can.",
  "Let us see three. One minute each: who reads it, three numbers, and one data issue it caught. (Call the first person.)"),
 "t3story": (None,
  "Lesson 3, schedules. Your skill now builds the dashboard in two minutes. But someone still has to open Claude and ask. On Sunday morning you are at a client. Who presses Send? (Expected: nobody.) So we give it a time."),
 "t3term": ("Click Scheduled in the left sidebar on the presenting laptop.",
  "A scheduled task is a prompt Claude runs by itself on a timetable: every hour, every day, on weekdays, every week, or when you click run. "
  "The prompt calls your skill. Today we keep the file inside the skill, so the run needs no connections to other apps. You saw yesterday's run at 16:25: that was one of these."),
 "t3fresh": (None,
  'One thing to understand. Every run is a brand new session. It does not remember last week, and it does not see your chats. So the prompt names the skill, and the skill holds the file. Today that file sits inside the skill. At work, an approved connection or an automation tool would bring new files each week. Every run starts its answer with one line: when it ran, what it read, what it flagged. And the Scheduled page keeps every run, so you can go back and review.'),
 "t3chk": ('Ask for hands up on each option, then tap the most popular one.',
  'What does the 08:00 run know? (Wait for hands.) The middle one. A run sees nothing but its prompt and its skill, so anything it needs must be written there.'),
 "t3demo": (None,
  'Let me schedule my invoice skill. First, in a chat, I attach the October invoices and ledger and ask Claude to add them to the skill as reference files, then I save the skill again. (Click Scheduled, then New task, then Set up manually.) A name. The prompt from the sheet: it names the skill and the files inside it. Daily at 08:00. Save, and the most important click: run it once now. (Open the run.) The first line says when it ran, what it read and what it flagged. Then the same table as yesterday. If the test works, the schedule works.'),
 "t3task": ('Start the timer. Walk the room. Hint at 6 minutes: is the file inside the skill?',
  'Your turn: your own skill on a schedule, with no connections to other apps. First, attach your test file in a chat and use the first prompt on the sheet to add it to your skill, then save the skill again. Then click Scheduled, New task, Set up manually, and paste the second prompt. Set it for every Sunday morning at eight, save it, test it once right away, and open the result on the Scheduled page. Fifteen minutes.'),
 "t3map": (None,
  "Other tools have the same thing: ChatGPT has scheduled tasks, Copilot has scheduled prompts, Gemini has scheduled actions. But look at the second row. "
  "None of them starts when an email arrives. For that, you need an automation tool. That is our first lesson after lunch. Enjoy your lunch."),
 "n4story": (None,
  "Welcome back. Lesson 4. A client sends a signed confirmation at seven minutes past two. The team wants it in the tracker right away, not tomorrow morning. Can our scheduled task do that? (Expected: no.) Right. It waits for a time. This needs a tool that listens for events."),
 "n4cmp": ("Read one row at a time.",
  "Three tools you will hear about. Claude is best at reading, judging and writing: messy documents, summaries, drafts. n8n and Power Automate are best at connecting systems: when this happens in one app, do that in another. "
  "Power Automate lives inside Microsoft 365. n8n works with almost any app, and a firm can run it on its own server. And look at the last row: these are usually owned by IT, not by one person."),
 "n4limits": (None,
  "To be fair to Claude, here is what it cannot do today. It cannot start when an email arrives. It is not the right tool to copy thousands of rows exactly, every day. It runs on your own account, without the controls IT expects. "
  "It only reaches apps with a connector. And because it is AI, the wording can change from run to run, so you still check. None of this makes it less useful. It tells you where it fits."),
 "n4when": (None,
  "So when do you move to n8n or Power Automate? When the start is an event. When one flow touches three or more systems. When it runs all day, or the output must be identical. When many people depend on it, so IT must own it. "
  "When you need a formal approval with a record. And often the best answer is both: n8n or Power Automate carries the data between systems, and Claude is one step inside the flow that reads and writes."),
 "n4chk": (HANDS,
  "Documents arrive by email at any time and must be logged as they land. (Wait for hands.) The first one: an automation tool, set up with IT, because the start is an event."),
 "n4terms": (None,
  "Before the demo, three words you will hear in every automation tool. The trigger is what starts it. Each node, or action, does one small job: read, calculate, decide, call AI. "
  "And the output is where the result lands. Between the nodes, the data travels as items. Every run is saved, so you can open it and see what happened."),
 "n4demo": (None,
  "Here is a small workflow in n8n, built from the same October invoices. (Play the video.) First the trigger: every weekday at 08:00. Then a Code node: the function that returns this week's invoices. "
  "Then an If node: is the amount over two thousand dinars? Then the two outputs: supervisor review, or approved. (Open the If node.) Three invoices went to review, two were approved. Trigger, nodes, output."),
 "n4chk2": (HANDS,
  "Which node sent each invoice down its own path? (Wait for hands.) The If node. The trigger only starts it, and the Code node only lists the invoices."),
 "m5brief": (None,
  "Lesson 5, your mini project. You build one agent for one department, using everything from the two days. The card first, then a Project, a skill, an artifact, a schedule, and a review. "
  "You can work alone or in pairs, and you can use your own task if you have one, on fictional data."),
 "m5dept1": ("Read the department names. Ask who will take which.",
  "Here are the first six packs, from RSM's own service lines: audit, tax, corporate finance, risk, cyber and IT. Each one is a single fictional Excel file, and each hides two problems your agent should catch."),
 "m5dept2": (None,
  "And five more: sustainability, data analytics, finance, HR and customer experience. The briefs file on the lab page explains each one: the problem, an idea for the agent, the artifact and the schedule."),
 "m5look": (None,
  "When I walk around, this is what I look for. Is it real work, and do you know the time it saves? Does it run: the Project, the skill, the artifact and the schedule? Three numbers you checked against the file. A review step with a named person. "
  "And a run log, with both hidden problems flagged. At 14:40 I will pick four or five of you to show."),
 "m5task": ("Start the timer. At 20 minutes, check everyone has a Project. At 45, check for a skill.",
  "Here is the plan for 85 minutes. Ten minutes for the card. Twenty-five for the Project and the skill. Twenty for the artifact. Fifteen for the schedule. And fifteen to check three figures, mark it DRAFT, and write your demo. "
  "Build in that order. If you fall behind, skip the schedule and say when it would run. Go."),
 "d6demo": ("Call each project. Restart the timer each time.",
  "Welcome back. Time for the projects. Four minutes each: the problem, your card, a run or your artifact, the time it saves, and your next automation. (Call the first person.)"),
 "c7map": ("Check the response count in the portal before you move on.",
  "Now the same test you took yesterday morning. Scan the first QR code with your phone. Phone only: no notes, no searching, no AI. It is not graded; it shows how far you came in two days. "
  "Then scan the second code for a short survey about the program. Please be honest. It helps us make it better."),
 "c7cert": ("Call each name. Hand over the certificate. Group photo at the end.",
  "Thank you for two full days. When I call your name, please come up for your certificate. Then we take one photo together."),
 "b7map": (None,
  "Before we close, everything you built over two days in one table, with the names in other tools. What Claude calls a Project, ChatGPT calls a Project or a custom GPT, Copilot calls an agent, and Gemini calls a Gem. "
  "Which tool does RSM use today? (Take answers.) Learn the method once, and it travels with you."),
 "c7next": ("Walk the tables. Read three answers aloud.",
  "Last question, for each of you: what will you automate first back at work, and in which tool? Tell your table. One task, one card, this week."),
 "w2": (None,
  "Two days. Yesterday each of you built an agent. Today you packaged your own method as a skill, turned data into a dashboard and a deck, put it on a schedule, and saw where n8n and Power Automate fit. "
  "Then you built an agent for a department. The habit to keep: Claude drafts, and a person signs off."),
 "close2": (None,
  "Thank you all. This week, pick one task, write its card, and try it on dummy data in a tool RSM has approved. It has been a pleasure working with you."),
}


def apply(slides):
    """Replace each Day 2 note with its script. Live demos keep their click steps; tasks keep their answers; checks keep the answer."""
    for sl in slides:
        r = sl.rec
        if r["id"] not in SCRIPT:
            continue
        cue, say = SCRIPT[r["id"]]
        old = r["note"]
        if r["kind"] == "live":
            cue = old.get("do")
        r["note"] = dict(old, do=cue, say=say,
                         expect=old.get("expect") if r["kind"] in ("task", "check") else None,
                         silent=None,
                         fallback=old.get("fallback") if r["kind"] in ("task", "live", "map") else None,
                         more=[])
    return slides
