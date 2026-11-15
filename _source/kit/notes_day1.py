# Day 1 speaker notes as a script: what the trainer says, word for word (Aya, 15 Nov).
# SCRIPT[slide id] = (short cue or None, what to say). Words in (brackets) are stage directions, not to be read aloud.
# build_deck.day1() applies this: live demos keep their click steps and fallback; tasks keep the answer key and fallback; checks keep the answer.

HANDS = "Ask for hands up on each option, then tap the most popular one."

SCRIPT = {
 "cover1": ("Leave this up while people arrive. Press → at 08:30.",
  "Good morning, everyone, and welcome. Please find a seat and open your laptop. We start in a few minutes."),
 "b0welcome": (None,
  "Welcome to CODED. My name is [your name], and I am with you for these two days. CODED started in Kuwait in 2015, and today we train people and companies to use coding and AI in their real work. "
  "About me: [your role at CODED, and one way you use AI every week]. You come from four teams, but you share one problem: tasks that come back every week. By tomorrow afternoon, each team will have an agent that does one of them. "
  "Two practical points. We take a break about every hour; lunch and Dhuhr are at 11:30, and Asr is at 14:55. And please open claude.ai with the workshop account, and the workshop site. If anything does not open, raise your hand and we come to you."),
 "map1": ("Check the response count in the portal before you move on.",
  "Before we teach anything, we want to see where you are today. Scan the QR code with your phone. It takes about ten minutes. "
  "Use only your phone: nothing else open, no searching, no AI tools. It is not graded. If you are not sure, choose your best guess. "
  "You take the same test at the end of tomorrow, so we can see how far you came."),
 "outcomes1": (None,
  "Here is what you will be able to do by 16:30. Notice the verbs: explain, write, find, build, read, package. You will do every one of these yourself, on your own laptop. "
  "Which one matters most for your team? (Take two answers.)"),
 "road1": (None,
  "This is our day. Everything today uses one fictional audit firm, Mirqab and Co., and its fictional client, Abdali Foods. Every file is made up, so you can make mistakes safely, and no real client data goes anywhere. "
  "We work in seven short lessons, with a break about every hour."),
 "b1story": ("Ask for a show of hands.",
  "Let us start with a show of hands. Who used an AI tool at work this month? Keep your hand up if it was ChatGPT. Copilot? Claude? What did you use it for? (Take three answers.) "
  "So most of us already use AI. Before we build anything, I want us to agree on one thing: what is really happening when it gives you an answer?"),
 "b1ask": ("Click the search bar. Type each answer and press Enter. Esc leaves the bar; → moves on.",
  "In your own words: what is AI? There is no wrong answer. Call it out, and I will type it. (Type each answer. Do not correct anyone yet.) "
  "Good. Keep these answers in mind. In the next few minutes we will see which ones are closest to how it really works."),
 "b1an": (None,
  "Here is the picture I want you to keep all day. Imagine a new joiner who has read more than anyone in this firm. Ask for a draft and it comes back in seconds, well written. "
  "But this new joiner has never seen your client's file. So when something is missing, it writes what is normal, not what is true. "
  "Look back at your answers: which of them fit this picture? And with a new joiner's first working paper, what would you check first? (Expected: the figures and the sources.) Exactly. Useful from day one, reviewed every time."),
 "b1t1": (None,
  "So what is it really doing? It learned from a huge amount of text. When it writes, it looks at the words so far and picks the word that most often comes next. Then the next one, and the next. "
  "That is why it is so good at reading, summarizing and drafting. But a likely word is not a checked word. Unless you give it the source, it is not looking anything up."),
 "b1llm": ("Read the sentence. Click the room's choice. Then click Pick the top word, start again, and pick Paris.",
  "Let me show you. Here is the start of a sentence from an audit file. Which word comes next? Call it out. (Click their choice.) "
  "Every possible word gets a score, and the model picks one. Now watch: I pick Paris, which has only a one percent chance. Read the sentence now. It still sounds confident. "
  "The model is not looking at the ledger. To it, a month is just another word. The percentages here are only an illustration."),
 "b1t2": (None,
  "This has a name: hallucination. It produces text that sounds correct, yet is false. A wrong amount, a wrong date, a source that does not exist. And it says it with full confidence, with no warning. "
  "Where in your work would a wrong figure hurt most? (Expected: reconciliations, confirmations, the report.) Yes. That is why professional skepticism still applies: every figure gets ticked against its source."),
 "b1cases": ("Tell each case in about one minute.",
  "This is not theory. Two real cases. In New York in 2023, two lawyers asked ChatGPT for past court decisions to support their client. It made the cases up, with quotes, and when the lawyer asked if they were real, it said yes. "
  "Nobody checked. The judge fined them and their firm 5,000 dollars, and made them write to every real judge whose name was on a fake decision. "
  "In Canada in 2024, Air Canada's chatbot invented a refund rule for a customer whose grandmother had died. The airline argued the chatbot should answer for what it said. The tribunal disagreed: the company is responsible, and the airline paid. "
  "So who paid for the mistake: the tool, or the people? (Expected: the people.) Exactly. The tool never signs. You do. "
  "(Optional, closer to our work: in 2025, Deloitte Australia refunded part of a government fee after a report with made-up references and a made-up court quote.)"),
 "b1chk": (HANDS,
  "Quick check. Read the question with me. (Wait for hands.) The answer is the first one: the model guessed a figure that looked likely, and no one checked it. The invoice is the source, and the answer must match it."),
 "b1t3": (None,
  "Now an important rule. Today every file is fictional, so you can try anything. Back at RSM it is different: client data only goes into tools that RSM has approved. "
  "Think of email. You would never send a client's ledger to your personal email. The same care applies to AI tools. Which tools are approved is RSM's decision, made by IT or Risk, not by us. "
  "If in doubt, assume it is client data and ask before you upload. The safe-use card on the workshop site has this rule."),
 "b1chk0": (HANDS,
  "Another quick check. What do you do first? (Wait for hands.) The answer is the second one: you look at the firm's policy first, and you only use a tool RSM has approved. What you upload leaves the firm's control, and invoices are client data."),
 "b1tools": (None,
  "AI tools come in three families. First, chat assistants such as Claude, ChatGPT, Copilot and Gemini: you ask, and it drafts. Second, AI built into the apps you already use, like Copilot in Excel and Outlook. "
  "Third, automation tools that run on their own. Which family did you use this week? (Take two answers.) In this program we use Claude, but the method you learn works in all three."),
 "b1tour": ("Show each one on your own screen as you say it.",
  "Before your first task, you need only three things in Claude. Watch my screen. Here is New chat: start a fresh one for every new job, so old answers do not mix in. "
  "Here is the plus button: this is how you give Claude the file to read. And here is where you type. That is all for now. The other features come later, one lesson at a time."),
 "b1task": ("Start the timer. Walk the room.",
  "Your first task. Open the Day 1 lab page and download the engagement letter from step 1. Start a new chat, attach the letter, and ask the three questions from the prompt sheet, one at a time. "
  "Then read the letter and verify one answer for yourself. You have 7 minutes. Raise your hand if anything does not open."),
 "b2story": (None,
  "Welcome back. Meet Faisal, a supervisor at Mirqab. Two associates send him a reconciliation for the same invoices. The columns are different, and so are the totals. "
  "One finds a problem, and the other says all is fine. Which one would you sign off? (Expected: neither.) Right, neither. Let us see if the same thing happens in this room."),
 "b2task": ("Start the timer. Walk the room.",
  "Now you do Faisal's task. Download the invoice pack and the October ledger from step 2 of the lab page. In a new chat, attach both. "
  "Then ask Claude, in your own words, to compare every invoice with the ledger in a table. There is nothing to copy this time. You have 7 minutes, and then you compare with your neighbor. Let us count how many different tables we get."),
 "b2two": ("First show three tables from the room. Then this slide.",
  "Let us look at three of your tables. (Show three.) Different columns, different totals, and some missed a problem. Now look at this: one request, one set of files, two chats, and still two different tables. "
  "Two things changed the result: the request, and the chat. We fix the request first."),
 "b2why": (None,
  "A prompt is simply what you type. And here is the key point: Claude can only use the words you give it. If your request does not say which columns, what counts as a difference, or what to do when something is missing, Claude fills the gap with what is common, not with what you need. "
  "It is like briefing a new joiner in one line and then being surprised by the result. What did your own request leave out? (Expected: the columns, the rules, what to do with gaps.)"),
 "b2ws": (None,
  "Let me show you the difference, live. One invoice, two chats. On the left, a weak request, the kind we all write. On the right, a request with five parts. (Send the weak one.) "
  "It reads well, but there is no invoice number, and the amount is rounded. Could this go into a working paper? (No.) "
  "Now the strong one. Before I send it, listen to its five parts: who Claude is, the steps, the rules, the format, and what to do when unsure. (Send it.) "
  "One clean row with the exact amount. And where the PO number is missing, it says Not found instead of guessing. Same tool, same invoice. I only changed the request."),
 "b2five": (None,
  "So here is the recipe, in five parts. Role: tell Claude who it is and what the job is. Steps: the order of the work. Rules: the source to use, the units and the dates. Format: the exact shape you want back. "
  "And the last part: what Claude should do when information is missing. That last one is the part people forget, and it is the part that stops the guessing. "
  "Then always attach the file, and check the answer yourself. Which part was missing from your request in Task 1.2?"),
 "b2pchk": (HANDS,
  "Which request gives you something you can put in a working paper? (Wait for hands.) The middle one. The first has no rules and no format, so Claude fills the gaps. The third is only a wish: being accurate is not a rule Claude can follow."),
 "b2try": ("Start the timer. Walk the room.",
  "Now you try. Take the request you wrote in Task 1.2 and rewrite it using the five parts. Open a new chat, attach the two files again, and run it. Then compare with your neighbor's table. Are they closer now? "
  "You have 3 minutes. The five parts are also on the prompt sheet, under Demo 1.1."),
 "b2t1": (None,
  "A good prompt is a big step. But think about next week. Where is your prompt? In an old chat, somewhere. You will type it again, a little differently, and get a slightly different table. "
  "That is a prompt, not a process. Think of an audit program: written steps, the same working paper, whoever does the work. That is what we want from AI: the same input, the same rules, the same shape, every time."),
 "b2chk": (HANDS,
  "Two associates, same invoices, different tables. What is missing? (Wait for hands.) The middle one: a fixed input, fixed rules and a fixed shape. And that is exactly what an agent keeps for you."),
 "b2agent": (None,
  "So what is an agent? It is AI that you prepare for one job, and it does that job identically each time. Its instructions are saved, so you never type them again. It can reach the files it needs. It always gives back the same shape. "
  "And from tomorrow, it can run on a schedule, without you. Think of a trained associate with a written procedure and access to the client file. A chat answers a question. An agent does a job. Today you build your first one, piece by piece."),
 "b2t2": (None,
  "Not every task should become an agent. Ask three questions about a task. Does it come back every week? Are the rules clear enough to write down? Does a document go in, and a document come out? "
  "Three yes answers, and you have a candidate. Anything that needs judgment, or a meeting with a client, stays with you. Pick the task first, and the tool second."),
 "b2sort": ("Read a card. Count the thumbs. Tap the card.",
  "Let us practice together. I read a task, and you decide: can an agent do it? Thumbs up for yes, thumbs sideways for partly, thumbs down for no. Everyone votes, from every department. (Read each card, count the thumbs, then tap it.) "
  "Do you see the pattern? If a task repeats and the rules are clear, an agent can do it. If it needs judgment, a relationship or a signature, it stays with a person. And in the middle, AI drafts and you decide."),
 "b2demo": (None,
  "Now let us watch Dana, an associate at Mirqab, do this with her own task list. She asks Claude to tag each of her tasks with the three questions. (Run it.) "
  "Count how many yes answers each row gets. Three yes means a candidate agent. The meeting with the client's CFO gets three no. That one stays with Dana."),
 "b2chk2": (HANDS,
  "Which of Dana's tasks should not be her first agent? (Wait for hands.) The CFO discussion. It is a meeting that needs judgment, not a document in and a document out."),
 "b2task2": ("Start the timer. Walk the room.",
  "Now your own work. Open step 3 of the lab page. Write down ten things you worked on last week, each on its own line. Then ask the three questions about each one, and pick your top three. "
  "Preparers, think about what you rebuild on every engagement. Reviewers, think about what you check every time. Coordinators, think about what you chase every week. You have 8 minutes. Then I ask each of you for your strongest task."),
 "b2board": ("Click the search bar. Type each person's strongest task and press Enter. A repeat shows ×2.",
  "Let us hear them. One at a time, tell me your strongest task and your department. (Type each one.) "
  "Look at what comes up more than once, across departments. Those are the best first agents. Keep yours in mind: in the next lesson, you choose one."),
 "b3story": (None,
  "Welcome back. Faisal asks a good question: everyone at Mirqab follows one audit program and fills the same working paper, so why are the AI tables all different? Because nothing was written down. "
  "In this lesson, you pick your task, write it down as an Agent Card, and then we build one together."),
 "b3t5": (None,
  "You have your top three. Now pick one, with a score. Give each task 1 to 5 on four points: how often it happens, how many minutes it takes, how clear the rules are, and whether it can run on a schedule. Add them up; the highest total wins. "
  "Be careful: the most exciting task is often not the best first agent. Tomorrow your agent has to run without you, so pick one that can."),
 "b3demo": (None,
  "Let us watch Dana score her three candidates. (Run it.) Which task has the highest total? (Expected: invoice matching, 19 out of 20.) "
  "Not the most exciting task, but the one that comes back every month, takes time, and has clear rules. That is Dana's first agent."),
 "b3tracks": (None,
  "Your task fits one of four tracks. Extraction: pulling information out of documents, like lease terms. Analysis: comparing numbers, like a trial balance over two years. "
  "Workflow: requests and follow-ups, like chasing missing documents. Reporting: turning status sheets into one weekly summary. Each track has a practice pack of fictional files, so you never use real client data. Which track fits the task you picked?"),
 "b3scene": (None,
  "Think about the audit program a new associate follows. It lists the documents to read, the steps to follow, and how the final working paper must look. "
  "The Agent Card gives an agent that same structure, in four boxes: Input, Instruction, Output and When. If a new joiner could follow your card, Claude can follow it too."),
 "b3t1": (None,
  "Four boxes. Input: the files the agent reads. Instruction: its rules. Output: the result it returns, in the same shape every time. And When: when it runs without you. "
  "Leave When empty today; that is tomorrow's job. This card fixes exactly what happened in Task 1.2, where each of us had a different input, different rules and a different shape."),
 "b3chk0": (HANDS,
  "Dana writes down the month's invoices and the ledger. Which box is that? (Wait for hands.) Input. It is what the agent works on."),
 "b3t2": (None,
  "One more thing about the Instruction box. Claude follows your exact words. It cannot read your mind. If you write: check the invoices, how should it check? It guesses. "
  "If you write: match the invoice number, the date and the amount, then flag every difference, there is nothing left to guess. Give me a vague line from your own work, and let us make it exact together."),
 "b3chk": (HANDS,
  "Which line gives the same result every run? (Wait for hands.) The middle one. Careful and good are wishes. Number, date and amount are things Claude can actually check."),
 "b3task2": ("Start the timer. Walk the room and approve cards.",
  "Now write your own card. Open step 4 of the lab page. First, score your top three tasks and pick the winner, then choose its track. "
  "Next, open the prompt sheet, grab the Agent Card template, paste it into the box, and fill in each line. Leave When empty. When you finish, raise your hand, and I come to approve your card. You have 17 minutes."),
 "b3t3": ("Open Projects on your screen.",
  "Where does a card live in Claude? In a Project. A Project keeps your instructions and your reference files, and every chat inside it uses them, so nobody has to explain the task again. "
  "It is like a client file that already has the procedures inside. Watch my screen: Projects, New Project, and then the instructions."),
 "b3t4": (None,
  "One difference matters a lot. Some files stay the same: the template, a reference list, one example of a finished output. Those go into the Project's knowledge. "
  "Other files change every month: this month's invoices and this month's ledger. Those come with each run. So where does next month's ledger go? (Expected: with the run.) Right. Mixing these up is the mistake we see most."),
 "b3chk2": (HANDS,
  "So, this month's invoices: where do they belong? (Wait for hands.) The middle one: it comes with each run, either attached or taken from the folder. Knowledge is only for what stays the same."),
 "b3pp": (None,
  "Let me turn Dana's card into an agent, live. (Create the Project.) A new Project, named Mirqab invoice match. In the instructions, I paste the card's rules, in five parts. "
  "In the knowledge, I add the template, because it never changes. The invoices are not here: they come with each run. One card, saved once, used in every chat."),
 "b3task": ("Start the timer. Build it on your screen, step by step.",
  "Now you build the same agent with me, step by step. Get the three files from the lab page, step 5. Together we create the Project, paste the instructions from the prompt sheet, add the template, and run it. "
  "Follow my screen. If you fall behind, raise your hand and we help you catch up. When it finishes, look at the Status column: two rows should show a problem."),
 "b4story": ("Approve the last Agent Cards while the room settles.",
  "Welcome back from lunch. Faisal reviews Dana's first agent. At first glance the table is fine. Then he spots it: an invoice without a PO number, and the agent made one up. "
  "What should the agent have written? (Expected: Not found.) Exactly. This lesson is about instructions that stop that from happening."),
 "b4parts": (None,
  "Remember the five parts from this morning? Here they are again, now saved as the agent's instructions. Look at the invoice agent column. "
  "Which part would have saved Dana's PO number? (Expected: When unsure.) Yes. It is the part people forget, and the part that stops the agent from guessing."),
 "b4t2": (None,
  "Two habits make agents reliable. First, show one example: a single finished output saved in the Project shows Claude the shape better than any long explanation. "
  "Second, test before you trust: check three cases where you already know the answer. It is what you do with a new joiner: you give them one model working paper, then check the first three they do. And when something is wrong, change the instructions, not the result."),
 "b4chk": (HANDS,
  "Your agent invents a PO number when there is none. What do you fix? (Wait for hands.) The When unsure part: tell it to write Not found, and never to guess. Fix the rule once, instead of fixing every answer by hand."),
 "b4pp": (None,
  "Let me show you a full run of Dana's agent. Here are the instructions, in five parts. (Run it.) I checked three rows by hand before, so I can compare. BPK-4471: matched. SCC-0718: the amount differs. "
  "And FSC-3390 is not in the ledger. Why? (Expected: it is outside the October ledger, a cut-off item.) The agent found it because the rules told it exactly what to compare."),
 "b4map": (None,
  "A quick note for your work at RSM. These five parts work in any assistant. In ChatGPT they go into a Project or a custom GPT, in Copilot into an agent, and in Gemini into a Gem. Different box, same five parts."),
 "b4task": ("Start the timer. Hint at 15 minutes; common fixes at 30.",
  "Now the big one: you build your own agent. You have 40 minutes. Get your track's file from the lab page, step 7. Create your own Project, paste the five-part template from the prompt sheet, and fill it in from your Agent Card. "
  "Before you run it, check three items by hand, so you know the right answer. Then run it and compare. If something is wrong, fix the instructions and run again. "
  "Struggle a little first; that is where the learning happens. I give a hint at 10 minutes, and show the most common fixes at 20. After that, you build a second one."),
 "b4task2": ("Start the timer. Walk the room.",
  "Round two. You build a second agent, on a different track and different data. Pick any track you did not use, and get its file from the lab page, step 8. "
  "Same five parts, new task. Use the track's starting example from this morning's tracks slide. You will see it goes much faster the second time, because the method does not change. "
  "Check two items by hand, and fix the instructions if one is wrong. You have 25 minutes."),
 "b5story": (None,
  "Meet Noura, a project coordinator. Each week she takes the same files out of the drive and drops them into a chat, one at a time. How many files do you drag into a tool each week? "
  "Tomorrow your agent runs at eight in the morning. Nobody will be there to drag the files. So the agent has to read them where they already are."),
 "b5t1": ("Show Google Drive under Customize, then Connectors.",
  "That is what a connector does. It lets Claude read from an app, like Google Drive. But be careful: it reaches everything the logged-in account is allowed to see. "
  "That is why, today, everyone signs in with a CODED training account that only sees the Mirqab practice folders. It is a key to one cabinet, not to the whole archive. At RSM, IT decides which keys are allowed."),
 "b5chk1": (HANDS,
  "Your agent runs tomorrow at eight. Why won't dragging files in work? (Wait for hands.) Because nobody is there to drag them at eight. The files must be somewhere the agent can reach on its own."),
 "b5pp1": (None,
  "Watch. Google Drive is already connected here. In the invoice Project, I ask the agent to process the newest files in the Inbox folder. (Run it.) "
  "The same table as before. And look: it lists the files it read, exactly two. It read only what it needed."),
 "b5task1": ("Start the timer. Walk the room.",
  "Your turn. Connect Google Drive with your CODED training account, not your personal one. Then find your track folder in the Mirqab sandbox; your files are in its Inbox. "
  "In your Project, copy the folder prompt from the prompt sheet, add your folder name, and run it. Make sure it tells you which files it read. You have 12 minutes."),
 "b5t2": (None,
  "Now the output. An artifact is something Claude makes that you can open and download, like a table or a spreadsheet. But a reviewer needs more than a file. "
  "They need the same shape every time: the same columns, in the same order, with the same total line. Like the firm's working-paper template, that is what lets you compare this week with last week."),
 "b5chk2": (HANDS,
  "Why must a scheduled agent always return the same shape? (Wait for hands.) So that this week's result lines up with last week's. That is how a reviewer spots what changed."),
 "b5pp2": (None,
  "I add an output rule to the invoice Project: the exact columns, in order, and a total line. Then I run it twice. (Put the two results side by side.) "
  "Compare the columns and the total line. The same shape, both times. That is what a reviewer needs."),
 "b5map": (None,
  "And in other tools: in Copilot, the input is your work data in SharePoint, OneDrive and Outlook, and the output is a Copilot Page. In ChatGPT, it is apps and canvas. Different buttons, same four boxes."),
 "b5task2": ("Start the timer. Walk the room.",
  "Now give your agent a fixed shape. Take the output rule from the prompt sheet, write your own columns in the order you want them, and add it to your Project's instructions. "
  "Then run it twice, each time in a new chat, and compare. Same columns, same order, same total? If not, fix the rule. You have 11 minutes, and then you make a second artifact."),
 "b5task3": ("Start the timer. Walk the room.",
  "Now a second artifact, and a different kind. Open your second Project, attach that track's file again, and pick one of the two prompts on the prompt sheet: a chart, or a one-page memo for a manager. "
  "When it appears, check two numbers or facts against the file. Then request a single edit, say a different heading, and see the artifact change in place. You have 12 minutes."),
 "b6story": (None,
  "Welcome back. Dana's agent works, but only in her own Project. Faisal asks two questions: could her colleagues use it too? And could it work tomorrow while Dana is busy? "
  "How does the firm share a method today? (Expected: a manual, a template, a checklist.) Right. A method that only one person can run is not really a method yet."),
 "b6t1": ("Show the Skills page under Customize.",
  "That is what a skill solves. Think of a skill as a stored method: Claude picks it up automatically when your request fits. It works in any chat, not only inside one Project, and it works in scheduled tasks, so tomorrow's agent can use it. "
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
  "Now package your own method. In your Project, use the prompt from the prompt sheet to turn your instructions into a skill, and save it. Check that it appears under Customize, then Skills. "
  "Then the real test: a brand-new chat, outside the Project. Attach your file and ask in one line. Claude should use your skill and give you the same shape. You have 14 minutes."),
 "b6task1b": ("Start the timer. Walk the room.",
  "Now package your second agent as a second skill. Then the interesting part: start a fresh chat with no Project, add the file from your second track, and make a one-line request. Does Claude pick the right skill? "
  "Then try your first file in another new chat. Claude chooses a skill by its one-line description, so if it picks the wrong one, make that line more specific. You have 12 minutes."),
 "b6task2": ("Start the timer. Walk the room.",
  "The last task of the day, and my favorite. Real files are messy. Get the messy file for your track from the lab page, step 14, and run your skill on it. "
  "Each file hides a gap. A good agent flags it; a bad agent guesses. Which one is yours? Then time it: how long by hand, and how long with the agent. Note the two numbers on your lab page. You have 8 minutes."),
 "b7show": ("Teams show at their own tables at the same time. Walk between them.",
  "Show time. Four teams, at your own tables. Each person has ninety seconds: first the card, then a live run on one of your files. Your team watches and asks one question. "
  "If a run hangs, show your last good result. Go."),
 "b7demo": (None,
  "One last thing before we close. This morning at eight, I set up a scheduled task for Dana's invoice agent, to run at 16:25. Nobody touches it. (Open the Scheduled page, then the Outputs folder.) "
  "Watch the Outputs folder. (When the file appears.) Nobody pressed send. The agent ran by itself. That is tomorrow: your team's agent, on a schedule."),
 "b7map": (None,
  "Here is everything you built today, in one table, with the names in other tools. Read one row across: what Claude calls a Project, ChatGPT calls a Project or a custom GPT, Copilot calls an agent, and Gemini calls a Gem. "
  "You used the first four rows today. Tomorrow we fill in the When row. Learn the method once, and it travels to any tool."),
 "w1": (None,
  "What a day. Each of you built your own agent. You wrote a card, set up a Project, connected a folder, fixed the output shape, and packaged a skill. You found the two planted problems, and you tested a messy file. "
  "And the habit to keep: when something is missing, the agent says so instead of guessing, and a person always reviews. Who will try this first at work, and on what? (Take two answers.)"),
 "close1": (None,
  "Thank you all. Tomorrow we put your agents on a schedule, add a human review step, and present them at Demo Day. First thing tomorrow, each team chooses which agent to automate. See you at 08:30."),
}


def apply(slides):
    """Replace each Day 1 note with its script. Live demos keep their click steps; tasks keep their answers; checks keep the answer."""
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
