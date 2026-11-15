# Day 2 speaker notes as a script: what the trainer says, word for word (Aya, 15 Nov, same pattern as notes_day1.py).
# SCRIPT[slide id] = (short cue or None, what to say). Words in (brackets) are stage directions, not to be read aloud.
# build_deck.day2() applies this: live demos keep their click steps and fallback; tasks keep the answer key and fallback; checks keep the answer.
# The output and package slides (b5..., b6...) moved here from Day 1 on 15 Nov; their scripts moved with them.

HANDS = "Ask for hands up on each option, then tap the most popular one."

SCRIPT = {
 "cover2": ("Leave this up while people arrive. Press → at 08:30.",
  "Good morning, and welcome back. Please sit with your team today, and open claude.ai and the workshop site on your laptop. We start in a few minutes."),
 "outcomes2": (None,
  "Here is today. This morning you finish your own agent: one fixed shape for every run, a second artifact, and two skills. "
  "Then your team turns one agent into a workflow that runs without you, with your department's rules and one named reviewer. At 15:15 you show it to the panel. "
  "Which of these matters most for your team? (Take two answers.)"),
 "road2": (None,
  "This is our day, in eight short lessons. The first two finish yesterday's build. The next five turn your team's agent into a workflow. The last one is Demo Day, at quarter past three. "
  "We still break about every hour; lunch and Dhuhr are at 11:30, and Asr is at 14:55."),
 "c1rule": ("Open the Outputs folder and show the 16:25 file.",
  "Before we start, look at this. (Show the 16:25 file and its run log.) Yesterday at 16:25 nobody was at a laptop. The scheduled task ran anyway: it read the folder, saved this file and wrote this log. "
  "That is where today ends, with your own team's agent. But first we finish yesterday's build. You each already have an Agent Card, two Projects and a Drive folder. Let us warm up with two quick questions."),
 "c1chk1": (HANDS,
  "Where do this month's invoices go? (Wait for hands.) The middle one: they come with each run, from the folder. Knowledge is only for what stays the same."),
 "c1chk2": (HANDS,
  "And an invoice with no PO number? (Wait for hands.) The first one: Not found, with a note. A guess or a blank hides the gap from the reviewer."),
 "o2story": (None,
  "Lesson 1. Picture Faisal on a Monday morning. He opens this week's result from Dana's agent and last week's, side by side. The columns are different, the order is different, and nothing adds up at the bottom. "
  "So he cannot compare them: he reads both, line by line. What does a reviewer look at first? (Expected: the columns and the totals.) Exactly. So this morning we fix the shape once, in the instructions."),
 "b5t2": (None,
  "An artifact is something Claude makes that you can open and download, like a table or a spreadsheet. But a reviewer needs more than a file. "
  "They need the same shape every time: the same columns, in the same order, with the same total line. Like the firm's working-paper template, that is what lets you compare this week with last week."),
 "b5chk2": (HANDS,
  "Why must a scheduled agent always return the same shape? (Wait for hands.) So that this week's result lines up with last week's. That is how a reviewer spots what changed."),
 "b5pp2": (None,
  "I add an output rule to the invoice Project: the exact columns, in order, and a total line. Then I run it twice. (Put the two results side by side.) "
  "Compare the columns and the total line. The same shape, both times. That is what a reviewer needs."),
 "b5map": (None,
  "And in other tools: in Copilot, the input is your work data in SharePoint, OneDrive and Outlook, and the output is a Copilot Page. In ChatGPT, it is apps and canvas. Different buttons, same four boxes."),
 "b5task2": ("Start the timer. Walk the room.",
  "Now give your agent a fixed shape. Your track file is on the Day 2 lab page, step 1, if you need it again. Take the output rule from today's prompt sheet, write your own columns in the order you want them, and add it to your first Project's instructions. "
  "Then run it two times, in two new chats, and compare. Same columns, same order, same total? If not, fix the rule. You have 12 minutes, and then you make a second artifact."),
 "b5task3": ("Start the timer. Walk the room.",
  "Now a second artifact, and a different kind. Open your second Project, attach that track's file again from step 2 of the lab page, and pick one of the two prompts on the prompt sheet: a chart, or a one-page memo for a manager. "
  "When it appears, check two numbers or facts against the file. Then request a single edit, say a different heading, and see the artifact change in place. You have 13 minutes."),
 "b6story": (None,
  "Lesson 2. Dana's agent is now consistent: one shape, every run. But it only works inside her own Project. Faisal asks: could her two colleagues use it too? "
  "How does the firm share a method today? (Expected: a manual, a template, a checklist.) Right. A method that only one person can run is not really a method yet."),
 "b6t1": ("Show the Skills page under Customize.",
  "That is what a skill solves. Think of a skill as a stored method: Claude picks it up automatically when your request fits. It works in any chat, not only inside one Project, and it works in scheduled tasks, so this afternoon's schedule can use it. "
  "And you can share it with your team. A Project is your desk. A skill is the firm's methodology manual: anyone can use it, anywhere."),
 "b6chk": (HANDS,
  "If the method has to work everywhere, including on a schedule, how do you package it? (Wait for hands.) A skill. A Project lives in one place; a skill goes with you."),
 "b6pp": (None,
  "Let me turn the invoice Project into a skill. (Ask Claude to make the skill, then save it.) Now the real test: a fresh chat, outside the Project. I attach the files and ask in one line. "
  "Watch for Claude saying it is using the skill. The same table, the same shape. Package it once, and use it anywhere."),
 "b6map": (None,
  "In other tools the same idea has other names: a skill or a custom GPT in ChatGPT, an agent in Copilot, a Gem in Gemini. The name changes; the method inside does not."),
 "b6chk2": (HANDS,
  "Imagine a friend at another firm who only has ChatGPT. Where would your method go? (Wait for hands.) The first one: a ChatGPT skill or custom GPT, with the same card inside."),
 "b6task": ("Start the timer. Walk the room.",
  "Welcome back. Now package your own method. In your first Project, use the prompt from the prompt sheet to turn your instructions into a skill, and save it. Check that it appears under Customize, then Skills. "
  "Then the real test: a brand-new chat, outside the Project. Attach your file and ask in one line. Claude should use your skill and give you the same shape. Write the transfer line in step 3 of the lab page. You have 14 minutes."),
 "b6task1b": ("Start the timer. Walk the room.",
  "Now package your second agent as a second skill. Then the interesting part: start a fresh chat with no Project, add the file from your second track, and make a one-line request. Does Claude pick the right skill? "
  "Then try your first file in another new chat. Claude chooses a skill by its one-line description, so if it picks the wrong one, make that line more specific. You have 12 minutes."),
 "b6task2": ("Start the timer. Walk the room.",
  "The last task of the build, and my favorite. Real files are messy. Get your track's messy file from the lab page, step 5, and run your skill on it. "
  "Each file hides a gap. A good agent flags it; a bad agent guesses. Which one is yours? Then time it: how long by hand, and how long with the agent. Write the two numbers in step 5. This afternoon they become your impact number. You have 8 minutes."),
 "c1story": (None,
  "Lesson 3. Your agents now have a fixed output and a skill. Faisal looks at Dana's agent and asks two hard questions. Who runs it while Dana is away on leave? And who looks at it before anyone uses the result? "
  "Who runs your weekly tasks when you are away? (Take two answers.) Usually nobody, until you come back. If the agent waits for you, it is only a tool. From now on, it becomes a system."),
 "c1scene": (None,
  "Think of a standing instruction at your bank. You set it up one time: on the first day of every month, send this amount to that account. It goes out on time, and you do nothing. "
  "And your statement lists each payment, so you can check it. Who here has one? (Show of hands.) A workflow works the same way: it runs by itself, and a person checks what it did."),
 "c1t1": (None,
  "Every workflow has four parts. A trigger starts it: a time, like eight every morning, or an event, like an email arriving. The steps do the work: that is the skill you made this morning. "
  "The output lands where a person sees it. And review: one named person checks it before anyone relies on it. In audit, that part is never optional. "
  "Dana's invoice agent: the trigger is eight o'clock, the steps are her skill, the output is a file in Outputs, and Faisal reviews."),
 "c1chk4": (HANDS,
  "What starts a scheduled workflow? (Wait for hands.) The first one: the trigger. Today our trigger is a time."),
 "c1pp": (None,
  "Let me fill in a workflow card for Dana's invoice agent, live on the lab page. (Paste the template in step 6 and fill it in.) When: daily at eight. Input: the invoice Inbox. Skill: the invoice-match skill, by its exact name. "
  "Output: a file named with the date and time, plus a run log. And who reviews: Faisal, by name, not the team. (Copy the card. Send Check our card in Claude.) "
  "Claude asks three questions about what could go wrong. Those questions are your test plan. Now, as a team, pick one agent from yesterday by a show of hands. You work on that person's laptop all day."),
 "c1task": ("Start the timer. Walk the tables and check cards.",
  "Welcome back. Your turn, as a team. Open the Day 2 lab page and go to step 6. Take the workflow card template from today's prompt sheet, Task 2.1, put it in that step's box, and fill in all five boxes for your team's agent. "
  "An empty box is a risk. Who reviews must be one person's name. When you finish, raise your hand and I come to your table. You have 12 minutes."),
 "c2story": (None,
  "Lesson 4. Dana's invoice agent still waits for her: someone has to open Claude and ask. And tomorrow at eight, she is at a client's office. "
  "What time would your team's workflow run? (Take two answers.) For invoices, every morning at eight. So we set it once, and it runs on time."),
 "c2t1": ("Click Scheduled in the left sidebar on your screen.",
  "That is a scheduled task: a prompt you save once, and Claude runs it as often as you choose. Every hour, every day, on weekdays, every week, or only when you click. "
  "The prompt calls your skill, and it reads the files through your connector. A normal reminder only reminds you; this one does the work and leaves the file. It lives here, under Scheduled."),
 "c2t2": (None,
  "Two things to know. First, a task that reads from Drive runs in the cloud, so you can close your laptop. If the task needs files that sit on your own laptop, that laptop must be on. "
  "Second, every run starts from zero. It does not remember yesterday. So everything it needs must be written in the prompt, the skill and the folders. "
  "What can a run count on from yesterday? (Expected: only what the run log and the folders show.) Exactly. That is why we keep a run log."),
 "c2steps": ("Point to each step. Do not build it yet.",
  "Six steps. Open Scheduled. Start a new task and set it up by hand. Give it a name and a prompt that calls your skill and names your folders. "
  "Choose the approval mode that lets it save and move files without stopping to ask you. Set it to run every day at eight; Kuwait works Sunday to Thursday, so the Friday and Saturday runs simply log that nothing came in. "
  "And test it once, right away. Which step would you skip? (None.) I build it live in a moment."),
 "c2chk": (HANDS,
  "Your task runs at eight. What should it count on from yesterday? (Wait for hands.) The middle one: the run log and the folders, nothing else. Each run is a new session."),
 "c2pp": (None,
  "Let me build Dana's schedule live. (Scheduled, New task, Set up manually.) A name. The prompt from the prompt sheet: it calls the invoice-match skill and names the Inbox, Outputs, Processed and Log folders. "
  "The approval mode. Daily at eight. Save. Now the most important click: run it once on demand. (Open Outputs, then Processed.) "
  "A new file with the date and time in its name, and the two input files moved to Processed. If this test works, the schedule works."),
 "c2task": ("Start the timer. Hint at 8 minutes; common fixes at 15.",
  "Now your team does the same, on the skill owner's laptop. First, in Google Drive, take your track pack from the Packs folder and copy it into your team's Inbox. "
  "Then in Claude: Scheduled, New task, Set up manually. Paste the prompt from today's prompt sheet, Task 2.2, and complete the brackets using your card. "
  "Approval mode, daily at eight, save, and run it once on demand. Then compare the result with your Day 1 result. Struggle a little first; that is where you learn. You have 25 minutes."),
 "c2map": (None,
  "In other tools, scheduling has other names: a scheduled task in ChatGPT, a scheduled prompt in Copilot, a scheduled action in Gemini. All of them start at a time. "
  "If a task must start on an event, like an email arriving, you need an automation tool such as n8n or Power Automate. We see n8n after lunch."),
 "c3story": (None,
  "Lesson 5. Imagine Tuesday at eight. The schedule ran, but it read yesterday's invoices a second time: nobody had moved them. And the new output file wrote over yesterday's file. "
  "What went wrong? (Expected: old files read twice, the output overwritten.) Two missing rules: nothing moves the files out of the Inbox, and the output name has no date. Before lunch, the first rule."),
 "c3t1": ("Show the three folders in the sandbox Drive.",
  "So we use folders like an in-tray and an out-tray. The run reads only the new files in the Inbox. When it finishes a file, it moves it to Processed, so nothing is read twice. "
  "And it saves its result in Outputs with the date and time in the name, so nothing is overwritten. Your team folder already has all of them."),
 "c3chk0": (HANDS,
  "Three new invoices have been read. Where do they go next? (Wait for hands.) The middle one: the run moves each file to Processed. Never delete them: Processed is your audit trail. Enjoy your lunch."),
 "c3t2": (None,
  "Welcome back. One more rule. Some mornings the Inbox is empty: a public holiday, or a quiet day. A bad automation then reads old files again, or breaks. "
  "A good one writes one honest line in the run log, no new files, and stops. And you check the run log each morning, quiet days included."),
 "c3chk": (HANDS,
  "The Inbox is empty at eight. What should the run do? (Wait for hands.) The middle one: write No new files in the log and stop."),
 "c3pp": (None,
  "Watch two runs. First I drop batch two into the invoice Inbox and run the task on demand. (Run it.) Two invoices match. One is in US dollars: it is flagged, and nothing is converted. "
  "Now I run it again with the Inbox empty. (Run it.) The run log has one line: no new files. Then I check the November ledger myself: last month's cut-off invoice was posted on the third of November."),
 "c3task": ("Start the timer. Walk the room.",
  "Your turn. Check that the empty-folder line is in your task's prompt; it is on today's prompt sheet, Task 2.3. Workflow and Analysis teams have one extra line there too. "
  "Then copy your track's batch-two file from Packs into your Inbox and run on demand. Check the output and the new run log. Then empty the Inbox, run again, and read the log. You have 20 minutes."),
 "c3when": (None,
  "A time is enough for most of your weekly work. But some tasks start with something happening: an email comes in, a form is sent, a file lands. "
  "Which of your tasks starts when an email arrives? (Take two answers.) For those, and for the firm's own systems, you move on to a tool like n8n."),
 "c3demo": (None,
  "Here is a flow I built in n8n before the workshop. (Open the flow.) It starts when an email lands in a requests inbox. A Claude step reads the email and returns three things. Then one row goes into a tracker sheet. "
  "Let me send a test email. (Send it, then watch the blocks light up.) Same idea as our schedule, but it starts on an event. At RSM, this is a conversation with IT."),
 "c3cmp": (None,
  "So which tool for which job? Our scheduled task starts at a set time; you build it by describing it; it suits your own weekly work, and you set it up yourself. "
  "n8n starts when something happens; you build it from connected blocks; it suits company systems with many steps, and IT usually owns it. "
  "Which column fits your team's workflow? (Expected: the schedule.) Right, for all four teams today."),
 "c3chk2": (HANDS,
  "Documents arrive by email at any hour, and the team wants each one logged the moment it lands. Which tool? (Wait for hands.) The first one: n8n or a similar tool, set up with IT. A daily schedule waits for its time."),
 "c4story": (None,
  "Lesson 6. A US dollar invoice arrives. One rule says to show amounts in Kuwaiti dinars. Another says never to convert. The run converted it anyway, using a rate it never showed. "
  "Which rule should win, and who decides? (Expected: the department decides.) Right: flag other currencies, never convert. The department makes the rules, not Claude."),
 "c4t1": ("Open mirqab-review-rules.docx on your screen.",
  "Every department has its own rules: limits, who signs off at which level, how files are named, and things that must never happen, like adjustments or conversions. "
  "These rules go into the skill exactly as the firm wrote them. Why exactly? Because the moment you put a rule in your own words, you have made a new rule. Find your department's section in the file."),
 "c4chk0": (HANDS,
  "The Assurance rule: other currencies are flagged, never converted. How do you put it in the skill? (Wait for hands.) Word for word. Shorter words can change what the rule means."),
 "c4t2": (None,
  "And every output is only a draft. The file says DRAFT in its title and ends with a line for the reviewer's name. Each run also saves a log in the Log folder: the date, the files it read, what it flagged, and the file it saved. "
  "It is like a working paper with the reviewer's initials. The agent sorts the work. The supervisor makes the call."),
 "c4chk": (HANDS,
  "A workflow drafts a client email with the wrong deadline. What stops it happening again? (Wait for hands.) The middle one: drafts only, a named reviewer, and a check on dates. Any model can get a date wrong."),
 "c4pp": (None,
  "Welcome back. Watch me add the three Assurance rules to the invoice skill, word for word, and then the review line. (Run the task on demand. Open the output.) "
  "Two invoices match. The dollar invoice and the messy one are flagged for currency, and nothing is converted. The supervisor section is empty, because no difference is over one hundred dinars. "
  "DRAFT in the title, and a line for the reviewer's name at the end."),
 "c4task": ("Start the timer. Walk the room.",
  "Your turn. Download the rules file from the lab page, step 10, and choose two rules that fit your department. Then the skill owner adds them to the skill word for word, with the prompt from today's prompt sheet, Task 2.4. "
  "Then copy your track's messy file from Packs into the Inbox and run on demand. Check three things: DRAFT, the reviewer line, and that the messy item is flagged instead of guessed. You have 28 minutes."),
 "c5story": (None,
  "Lesson 7. At quarter past three, Dana presents her invoice workflow to the partners. Expect two questions: does it really run, and what does it save? "
  "So this lesson is about your demo: a live run first, then one number."),
 "c5stats": ("Point to the source line under the numbers.",
  "Here is how you get the number. Take the minutes by hand, subtract the minutes with the agent, and multiply by how many times it runs in a month. "
  "In this example: forty minutes by hand, five with the agent, twenty times a month. That is about twelve hours back every month. Your own two times are in step 5 of the lab page, from Task 1.10 this morning."),
 "c5rubric": (None,
  "The panel scores each team out of fifty: five criteria, ten points each. Is it a real task with a measured cost? Does it run from the Scheduled page, in the same shape every time? "
  "Do the figures match the source? Are there human controls: drafts, your rules, a named reviewer? And is there test evidence in the run log? "
  "How will the panel check the figures? (Expected: pick figures and find them in the file.) Yes. They pick three figures from your output, and you show each one in its source file."),
 "c5script": (None,
  "Your demo has five parts in five minutes. What the problem costs today. Your workflow card. A live run, on demand, on screen. Your impact number. And the next task you would automate. "
  "Decide now who presents which part. And rehearse the live run, because that is what usually breaks."),
 "c5pp": (None,
  "Let me draft a demo plan for the invoice workflow. (Paste the Demo 2.6 prompt into Claude.) The problem: 45 minutes, 22 times a month. The card. A live run on batch two. "
  "The impact: about fourteen hours a month. And next: the cut-off check. Two minutes, five parts. And every number comes from the run log."),
 "c5chk": (HANDS,
  "Thirty minutes by hand, six with the agent, twenty-five times a month. About how much does it save? (Wait for hands.) The middle one, about ten hours. Thirty minus six is twenty-four, and twenty-four times twenty-five is six hundred minutes."),
 "c5fail": ("Open the pre-flight run log and read its Could not read line.",
  "One more test before Demo Day: a run that fails. We put a file in the Inbox that no run can open. A good run says so in the log, names the file, leaves it where it is, and invents nothing. "
  "A bad run says nothing, or makes up a row. One line in your prompt tells the run what to do, and your reviewer checks that file by hand. "
  "And if the connector is off, no log appears at all. A missing log also means: go and check the run."),
 "c5chk2": (HANDS,
  "The log says one file could not be read; the others moved on. What happens next? (Wait for hands.) The middle one: the reviewer named on the card opens that file and checks it by hand. Running it again gives the same result."),
 "c5task": ("Start the timer. Call out each part as its time ends.",
  "The last task before Demo Day: 37 minutes, in five parts, with the minutes for each part on the slide. Three clean runs from your pack. The failed-run test with the locked file. "
  "Your impact number, from your two times in step 5 of the lab page. Your demo plan, with the Demo 2.6 prompt. And one full rehearsal with a timer. "
  "Before 15:15, put a pack back in the Inbox for your live run. Go."),
 "c6demo": ("Restart the timer for each team.",
  "Welcome back, and welcome to our guests. It is Demo Day. Each team has eight minutes: five to show, three for questions. Each automation gets a score out of fifty from the panel. "
  "Team one, the floor is yours."),
 "c6order": ("Say each team's workflow name.",
  "Here is the running order: Team one now, then a new team every eight minutes. Scores and the panel's comments come after the fourth team."),
 "c6score": ("Keep this up while the panel scores. Then read each team's strongest point aloud.",
  "While the panel adds up the scores, here is the sheet they use: ten, five or zero on each criterion. Thank you, all four teams. Every workflow today ran on its own."),
 "c7map": ("Check the response count in the portal before you move on.",
  "Now the same test you took yesterday morning. Scan the first QR code with your phone. Phone only: no notes, no searching, no AI. It is not graded; it shows how far you came in two days. "
  "Then scan the second code for a short survey about the program. Please be honest. It helps us make it better."),
 "b7map": (None,
  "Before we close, here is everything you built over two days in one table, with the names in other tools. Read one row across: what Claude calls a Project, ChatGPT calls a Project or a custom GPT, Copilot calls an agent, and Gemini calls a Gem. "
  "You used every row, from the card to the schedule. Which tool does RSM use today? (Take answers.) Learn the method once, and it travels with you."),
 "c7next": ("Walk the tables. Read three answers aloud.",
  "Last question, for each of you: what will you automate first back at work, and in which tool? Tell your table. One task, one card, this week."),
 "w2": (None,
  "Two days. Yesterday each of you built an agent. This morning you gave it a fixed shape and made it a skill. Then each team put one agent on a schedule, with new files, an empty folder, a failed run, your department's rules and a named reviewer, "
  "and you showed it to the panel. The habit to keep: Claude drafts, and a person signs off."),
 "close2": (None,
  "Thank you all. This week, pick one task, write its card, and try it on dummy data in a tool RSM has approved. Your first schedule can come this month. It has been a pleasure working with you."),
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
