# -*- coding: utf-8 -*-
"""The slides of AI Innovation and Automation (CODED × RSM Albazie), day by day. The engine's deck.py renders every call.
One helper call is one slide. Every note is written as N(...) parts and never repeats the slide text. The engine adds the close slide."""
from deck import *
import content as C
import content_demos as CD
from content_demos import DEMOS
import data as D
from data import num

SECTIONS = {
 1: [("Opening", "g-mark", ["open"]), ("AI foundations", "g-code", ["b1"]), ("Find the work", "g-frame", ["b2", "b3"]), ("Build", "g-impact", ["b4", "b5", "b6"]), ("Close", "g-progress", ["b7", "close"])],
 2: [("System", "g-mark", ["open", "c1"]), ("Schedule", "g-code", ["c2", "c3"]), ("Rules", "g-frame", ["c4"]), ("Demo Day", "g-impact", ["c5", "c6"]), ("Close", "g-progress", ["c7", "close"])],
}
FLOW = {
 1: (["L1", "L2", "L3", "L4", "L5", "L6", "L7"], {"b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4, "b6": 5, "b7": 6}),
 2: (["L1", "L2", "L3", "L4", "L5", "Demo"], {"c1": 0, "c2": 1, "c3": 2, "c4": 3, "c5": 4, "c6": 5}),
}
COVER_NOTES = {
 1: N(do="Welcome the room. Introduce yourself and CODED in one minute.", more=["Housekeeping: breaks about every hour, lunch and Dhuhr at 11:30, Asr at 14:25. Prayer room and toilets.",
      "Sign-in check: every laptop opens claude.ai with the workshop account, and the workshop site. Helpers walk the room."],
      say="Over two days you will build an agent for a task you repeat every week, and make it run on its own.", silent="ask who has used any AI tool at work this week."),
 2: N(do="Welcome back. Check that every laptop is signed in and the sandbox Drive opens.", more=["Teams sit together from the start today.", "The callback quiz comes after today's map."],
      say="Yesterday every one of you built an agent. Today one agent per team learns to run without you.", silent="ask one person what their skill is called."),
}
OUTCOMES_NOTES = {d: N(do="Read the outcomes. Ask which one matters most for their team.", expect="Most people pick the schedule or the skill.",
                       say="These are the things you will do yourself today, on fictional files.", silent="pick one and say why it matters for audit work.") for d in (1, 2)}
ROAD = {1: {"title": "One firm, one client. <span class=\"hl\">Seven lessons.</span>", "n": N(do="Point to the breaks: the cup button starts the break clock.", say="Mirqab is fictional, so you can make mistakes safely. Every file is made up.")},
        2: {"title": "One agent per team. <span class=\"hl\">One workflow by 14:45.</span>", "n": N(do="Point to Demo Day at 14:45.", say="By the afternoon break your workflow runs on a schedule. Then you show it.")}}
CLOSE = {
 1: {"big": "Card → Project → <span class=\"hl\">skill.</span>", "next": "Tomorrow: your team's agent runs on a schedule, with a review step, and you show it at Demo Day.",
     "n": N(do="Recap the day in one line.", more=["Remind teams that the vote closes at 08:40 tomorrow."], say="Thank you. See you at 08:30.")},
 2: {"big": "Claude does the first pass. <span class=\"hl\">You sign off.</span>", "next": "Thank you. Start with one card for one task this week, on dummy data, in an approved tool.",
     "n": N(do="Recap the two days in one line.", more=["Point to the take-home guide, the cheat sheet and the safe-use card on the site."], say="Your first card this week. Your first schedule this month.")},
}

# ------------------------------------------------------------------ Day 1 · Designing AI Agents for Real Work
def day1():
    opener = [story("b0story", "open", "Opener · one invoice", "Sunday 1 November, 08:40",
        f"Dana, an associate at {D.FIRM}, opens a supplier invoice for {D.CO_SHORT}. She needs the invoice number, the amount and the PO for a working paper. <b>She types three words.</b>",
        "Same tool. Same invoice. <span class=\"hl\">Watch what the request changes.</span>", "See why the request decides the quality of the result.",
        n=N(do="Read the story aloud. Ask what they would type.", expect="Short answers, like a question about the invoice.", silent="Say what most people type: a short question, like Dana."), time="08:45-08:52"),
        showcase("ws", "open", CD.SHOWCASE, n=N(do="Press → through the steps.",
            more=["Step 1: the same invoice in both windows.", "Steps 2 and 3: the weak request and its answer. Read the red flags aloud.",
                  "Steps 4 to 8: Role, Steps, Rules, Format, When unsure, one per press. Ask what each part adds.", "Then the strong answer: point at the exact amount and the Not found.",
                  "Then the scorecard and the lesson.", "Optional: run both live in two windows (prompt sheet, Demo 1.0)."],
            silent="ask before the parts: could the weak answer go into a working paper?", say="Same tool, same invoice. I only changed the request.", time="5 min"))]
    s = opening(1, opener=opener)
    # Lesson 1 · AI foundations
    s.append(story("b1story", "b1", "Lesson 1 · AI foundations", "Sunday 1 November, 08:52",
        "Most of this room already uses AI at work, in more than one tool. <b>Before we build anything, one question: what is it actually doing when it answers?</b>",
        "Know what it does <span class=\"hl\">and where it fails.</span>", "Explain what generative AI does well and where it can be wrong.",
        n=N(do="Run the live poll on the shared board: which AI tools did you use this month, and for what? Read three answers aloud.", expect="ChatGPT, Copilot, some Claude; emails, summaries, Excel help.",
            silent="share your own answer first.", more=["Two minutes for the poll, then move on."]), time="08:52-09:20"))
    s.append(scene("b1an", "b1", "Lesson 1 · the picture", "A very well-read <span class=\"hl\">new joiner.</span>",
        "It has read more than any associate ever will, so its drafts are fast and fluent. It has never seen this client's file, so it fills gaps with what is usual.",
        "Fast and fluent. Not checked.",
        [{"ground": 268}, {"building": (240, 268), "tone": "dim"}, {"person": (110, 268), "tone": "hot", "label": "New joiner", "anim": "bob"},
         {"doc": (330, 250), "label": "Client file", "tone": "dim"}, {"move": "doc", "path": [(140, 200), (240, 150), (320, 200)], "dur": 5},
         {"pill": "Read a lot", "at": (130, 40), "tone": "hot", "delay": 0}, {"pill": "Drafts fast", "at": (340, 40), "tone": "hot", "delay": 1.5}, {"pill": "Never saw this file", "at": (240, 86), "tone": "bad", "delay": 3}],
        n=N(do="Ask: what would you check first in a new joiner's first working paper?", expect="The figures and the sources.", silent="say you would tick every figure.",
            say="Treat it like a talented new joiner. Useful from day one, reviewed every time.")))
    s.append(term("b1t1", "b1", "Lesson 1 · the idea", "What it <span class=\"hl\">really does.</span>", "Generative AI",
        "A model trained on very large amounts of text that writes by <b>predicting the most likely next word</b>, one word at a time. That is why it reads, summarizes, extracts and drafts well.",
        "Like the new joiner's fluent first draft…", "…each word is <b>likely</b>. Likely is not the same as <b>checked</b>.", "It predicts. It does not look things up unless you give it the source.",
        n=N(do="Link back to the new joiner: same idea, much bigger memory.", expect="People connect likely with not checked.", silent="ask: is a likely date always the right date?")))
    s.append(llmslide("b1llm", "b1", "Lesson 1 · live widget", "It writes by guessing <span class=\"hl\">the next word.</span>",
        "At each step, every possible next word gets a score. The model picks one, adds it, and predicts again.", "It predicts <b>likely</b> words. It does not check if they are <b>true</b>.",
        n=N(do="Read the start of the sentence. Ask the room which word comes next, and click their choice.",
            more=["Click Pick the top word: November is the most likely word. It is also right here, by luck.", "Start again and pick Paris (1%). The sentence still sounds confident.",
                  "The percentages are illustrative."], say="It is not looking at the ledger. A posting month is just another word to it.", silent="ask one person to choose for the room.", time="5 min")))
    s.append(term("b1t2", "b1", "Lesson 1 · the risk", "Fluent <span class=\"hl\">and wrong.</span>", "Hallucination",
        "When AI writes something that <b>sounds right but is not true</b>: a wrong amount, date, name or source, written with full confidence.",
        "A confident first draft…", "…that <b>nobody has ticked yet</b>. Professional skepticism applies.", "Tick every figure against the source document.",
        n=N(do="Ask: where in audit work would a wrong figure hurt most?", expect="Reconciliations, confirmations, the report.", silent="say: in a working paper your supervisor signs.")))
    s.append(player("b1demo", "b1", "d11", n=N(expect="Four rows right, one wrong: WDS-20931 shows the figure of another Wafra line.")))
    s.append(term("b1t3", "b1", "Lesson 1 · the data rule", "Dummy data today. <span class=\"hl\">RSM's policy always.</span>", "The data rule",
        "No client data goes into an AI tool that RSM has not approved. Today every file is fictional. Back at work, <b>RSM's AI policy decides</b> what may go in.",
        "Engagement confidentiality for email…", "…applies to <b>AI tools in the same way</b>.", "When you are not sure, treat it as client data and ask first.",
        n=N(do="Point to the safe-use card on the site.", expect="Questions about which tools RSM approves: say IT or Risk Management decides.", silent="ask: would you email a client's ledger to a personal address?")))
    s.append(check("b1chk0", "b1", "A colleague asks you to try your agent on a client's real invoices this afternoon. <b>What do you do first?</b>",
        [("Use it: the agent only reads files, it keeps nothing", 0, "What you upload leaves the firm's control."), ("Check RSM's AI policy and use only an approved tool", 1, "Right. RSM's policy decides."),
         ("Use it, because invoices are not sensitive", 0, "Invoices are client data.")]))
    s.append(cards3("b1tools", "b1", "Lesson 1 · the tools available", "Three families <span class=\"hl\">of AI tools.</span>",
        [("Family 1", "Chat assistants", "Claude, ChatGPT, Microsoft 365 Copilot, Gemini.", "You ask; it drafts."),
         ("Family 2", "AI inside your apps", "Copilot in Excel and Outlook, Gemini in Gmail and Docs.", "AI where the file already is."),
         ("Family 3", "Automation tools", "n8n, Power Automate, scheduled tasks.", "It runs without you.")],
        "This program uses Claude. The method works in all three.",
        n=N(do="Ask which family each person used this week.", expect="Mostly family 1, some family 2.", silent="say which one you use most and why.")))
    s.append(tslide("b1map", "b1", "Lesson 1 · the transfer map", "Same building blocks, <span class=\"hl\">different names.</span>", C.TRANSFER_HEAD, C.TRANSFER,
        "Learn the method once. The card works in any tool.", cls="tight",
        n=N(do="Read one row across. Ask: which tool does RSM use today?", expect="Copilot or ChatGPT for some; the card still applies.", silent="read the Package row: skill, custom GPT, agent, Gem.",
            more=["Feature names change often; the site has the sources and the date checked."])))
    s.append(check("b1chk", "b1", f"Claude gives KWD {D.num(D.AI_WRONG[1])} for an invoice that says KWD {D.num(D.INV[D.AI_WRONG[0]][4])}. <b>Why can this happen?</b>",
        [("It predicted a likely figure and nothing checked it", 1, "Right. It predicts likely words. You tick against the source."),
         ("It rounds amounts on purpose", 0, "It did not round. It took another likely figure."),
         ("The invoice must be wrong", 0, "The invoice is the source. The answer must match it.")]))
    s.append(listslide("b1tour", "b1", "Lesson 1 · the Claude tour", "Where today's tools <span class=\"hl\">live in Claude.</span>",
        ["<b>Chat:</b> the message box, with + to attach a file.", "<b>Projects:</b> instructions and knowledge for every chat inside.",
         "<b>Connectors:</b> Customize, then Connectors. Google Drive today.", "<b>Skills:</b> Customize, then Skills. A method Claude loads when it fits.",
         "<b>Artifacts:</b> tables and files Claude makes, to open and download.", "<b>Scheduled tasks:</b> click Scheduled in the left sidebar. Tomorrow's tool."],
        "One box of the Agent Card at a time.",
        n=N(do="Show each place on the presenting laptop while you talk.", expect="People find Projects and Customize in under a minute.", silent="ask someone to find Customize on their screen.")))
    s.append(task("b1task", "b1", "t11", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 2 · Why chat isn't enough, and finding the work
    s.append(story("b2story", "b2", "Lesson 2 · Why chat isn't enough", "Sunday 1 November, 09:30",
        f"Faisal, a supervisor, gets two reconciliation tables for the same {D.CO_SHORT} invoices. <b>Different columns, different totals.</b> One flags a problem; the other says everything matches.",
        "Same files. <span class=\"hl\">Two answers.</span>", "Feel why one-off chat is not repeatable.",
        n=N(do="Ask: which table would you sign off?", expect="Neither, until they match.", silent="say: neither. Then start the task."), time="09:30-10:20"))
    s.append(task("b2task", "b2", "t12", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(tslide("b2two", "b2", "Debrief · one prompt, two chats", "The answer depended <span class=\"hl\">on the chat.</span>",
        ["", "Chat A", "Chat B"],
        [["Columns", "Invoice, amount, status", "Supplier, invoice, ledger, difference, comment"], ["Rows flagged", "None: every row Matched", "Two rows flagged"], ["Total checked", f"KWD {D.num(sum(r[4] for r in D.INVOICES))}", "5 invoices"]],
        "Same prompt, same files, two different tables.",
        n=N(do="First show three contrasting tables from the room. Then this slide.", expect="People see that the request, not the files, changed.", silent="ask: which chat would you trust?",
            say="Nothing changed except the chat. That is the problem we solve today.")))
    s.append(term("b2t1", "b2", "Lesson 2 · the idea", "A prompt is not <span class=\"hl\">a process.</span>", "Repeatable",
        "A good prompt lives in one chat and is lost next time. A <b>repeatable</b> method keeps the same input, rules and output shape, so every run can be reviewed the same way.",
        "“Cook something nice”…", "…versus a <b>recipe card</b> anyone can follow.", "Audit work needs the same answer every time.",
        n=N(do="Ask: what makes an audit program repeatable?", expect="Written steps, the same working paper.", silent="say: it is written down, so anyone gets the same result.")))
    s.append(check("b2chk", "b2", "Two associates get different tables for the same invoices. <b>What is missing?</b>",
        [("A faster laptop", 0, "Speed was not the problem."), ("Fixed input, rules and output shape", 1, "Right. That is what the next lesson builds."), ("A longer chat", 0, "Longer chats drift more, not less.")]))
    s.append(term("b2t2", "b2", "Lesson 2 · agent-ready", "Which tasks <span class=\"hl\">suit an agent?</span>", "Agent-ready task",
        "A task that <b>repeats weekly</b>, has <b>clear rules</b>, and turns a <b>document in into a document out</b>. Judgment calls and client meetings stay with people.",
        "Three tags on a task…", "…three Yes means a <b>candidate agent</b>.", "Choose the task before you choose the tool.",
        n=N(do="Give one example of each tag from audit work.", expect="Invoice matching, lead schedules, confirmations.", silent="ask: which of your tasks repeats every week?")))
    s.append(player("b2demo", "b2", "d13"))
    s.append(check("b2chk2", "b2", "Which of Dana's tasks is <b>not</b> a first agent?",
        [("Matching supplier invoices to the ledger", 0, "Three Yes: a strong candidate."), ("Discussing findings with the client's CFO", 1, "Right. It needs judgment and trust."), ("Chasing missing documents from clients", 0, "Three Yes: a candidate.")]))
    s.append(task("b2task2", "b2", "t13", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(timer_slide("b2board", "b2", "Board review · 10:17", "What repeats <span class=\"hl\">across departments?</span>",
        "The shared board on screen: one task from each person, grouped by department.", 3,
        n=N(do="Read the clusters aloud. Name the tasks that appear in more than one department.", expect="Reconciliations, chasing documents, status reports.",
            silent="read the Support column first: it shows what the coordinators chase.", more=["Note what the coordinators and Analytics Advisory do: it steers the track choice in Lesson 3.", "Onboarding counts: new-client KYC and acceptance checklists are a Workflow-track candidate for Support and Assurance."])))
    # Lesson 3 · Design the agent, then pick your case
    s.append(story("b3story", "b3", "Lesson 3 · Design the agent", "Sunday 1 November, 10:30",
        "Faisal: <b>“Every associate follows the same audit program and produces the same working paper. Why does every AI table look different?”</b>",
        "Write it down <span class=\"hl\">once.</span>", "Describe a task as an Agent Card, then build it in a Project.",
        n=N(do="Ask: what does an audit program give a new associate?", expect="Steps, rules, the template.", silent="say: it removes the guessing."), time="10:30-11:30"))
    s.append(scene("b3scene", "b3", "Lesson 3 · the picture", "The audit program <span class=\"hl\">every associate follows.</span>",
        "It says what to read, what to do and what the working paper looks like. An Agent Card does the same for an agent, in four boxes.",
        "Input · Instruction · Output · When.",
        [{"ground": 268}, {"doc": (90, 230), "label": "Input", "tone": "hot"}, {"laptop": (240, 250), "label": "Instruction"}, {"doc": (390, 230), "label": "Output", "tone": "ok"},
         {"move": "doc", "path": [(110, 190), (240, 160), (370, 190)], "dur": 5}, {"pill": "Same steps", "at": (140, 50), "tone": "hot", "delay": 0},
         {"pill": "Same shape", "at": (340, 50), "tone": "hot", "delay": 1.5}, {"pill": "When: Day 2", "at": (240, 100), "tone": "", "delay": 3}],
        n=N(do="Point to each box as it appears.", expect="People map their own task to the boxes.", silent="map the invoice task yourself first.",
            say="A card a new joiner could follow is a card Claude can follow.")))
    s.append(term("b3t1", "b3", "Lesson 3 · the idea", "Four boxes <span class=\"hl\">before any build.</span>", "The Agent Card",
        "<b>Input:</b> what it works on. <b>Instruction:</b> the rules it follows. <b>Output:</b> what it hands back, in a fixed shape. <b>When:</b> when it runs without you (empty until Day 2).",
        "Like the audit program…", "…the card fixes the <b>input, the rules and the output</b>.", "This card fixes what went wrong in Task 1.2.",
        n=N(do="Show Dana's invoice card from the site.", expect="People see that each box answers one question.", silent="ask: which box was missing in Task 1.2?")))
    s.append(check("b3chk0", "b3", "Dana writes: <b>the month's supplier invoices (PDF) and the purchase ledger.</b> Which box of the card is this?",
        [("Input", 1, "Right. It is what the agent works on."), ("Instruction", 0, "Instruction holds the rules it follows."), ("Output", 0, "Output is what it hands back.")]))
    s.append(term("b3t2", "b3", "Lesson 3 · literal", "Claude follows <span class=\"hl\">what you write.</span>", "Literal instructions",
        "Claude does what the words say, not what you meant. “Check the invoices” leaves the checking to chance. “Match number, date and amount; flag any difference” does not.",
        "“Check the invoices”…", "…becomes <b>“Match number, date and amount. Flag any difference.”</b>", "Vague words caused the misses in Task 1.2.",
        n=N(do="Rewrite one vague line from the room into a literal one.", expect="People add the fields and the rule.", silent="rewrite “review the leases” as an example.")))
    s.append(check("b3chk", "b3", "Which Instruction line will give the <b>same result every run?</b>",
        [("“Check the invoices carefully.”", 0, "Careful is not a rule."), ("“Match number, date and amount; flag any difference.”", 1, "Right. Fields and a rule."), ("“Do a good reconciliation.”", 0, "Good is not a rule.")]))
    s.append(term("b3t3", "b3", "Lesson 3 · the home", "A Project is <span class=\"hl\">the agent's home.</span>", "Claude Project",
        "A <b>Project</b> keeps instructions and knowledge files. Claude uses them in <b>every chat inside it</b>, so nobody explains the task again.",
        "A client file with the procedures already in it…", "…every new chat starts with <b>the card and the template</b>.", "Projects: + New Project, then Set project instructions.",
        n=N(do="Open Projects on the presenting laptop.", expect="Everyone finds + New Project.", silent="ask: where would you keep the invoice template?")))
    s.append(term("b3t4", "b3", "Lesson 3 · knowledge or input", "Templates stay. <span class=\"hl\">Documents come and go.</span>", "Knowledge versus input",
        "<b>Knowledge:</b> templates, reference files and one example output, saved in the Project. The rules go in the instructions. <b>Input:</b> this month's documents, attached or read with each run.",
        "The template and the example…", "…live in knowledge. <b>The invoices come with each run.</b>", "Mixing the two is the most common build error.",
        n=N(do="Ask: where does next month's ledger go?", expect="With the run, not in knowledge.", silent="say it, then ask why.")))
    s.append(check("b3chk2", "b3", "Where does <b>this month's invoice pack</b> go?",
        [("Into the Project knowledge", 0, "Knowledge is for what stays the same."), ("Into each run: attached, or read from the folder", 1, "Right. Input changes every run."), ("Into the Project instructions", 0, "Instructions are the rules, not the documents.")]))
    s.append(player("b3pp", "b3", "d14"))
    s.append(task("b3task", "b3", "t14", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(term("b3t5", "b3", "Lesson 3 · choosing", "Pick the task <span class=\"hl\">with the highest score.</span>", "Scoring a use case",
        "Score each candidate from 1 to 5 on four points. The points are <b>how often</b>, <b>minutes each time</b>, <b>how clear the rules are</b>, and <b>can it run on a schedule</b>.",
        "The most interesting task…", "…is not always the best <b>first</b> agent.", "Day 2 needs an agent that can run without you.",
        n=N(do="Score one task from the board with the room.", expect="Invoice matching or chasing documents scores high.", silent="score Dana's invoice task yourself.")))
    s.append(player("b3demo", "b3", "d15"))
    s.append(tslide("b3tracks", "b3", "Lesson 3 · the four tracks", "Pick a track <span class=\"hl\">for your agent.</span>", ["Track", "Starting example", "Pack"],
        [[t, ex, pk] for t, ex, _f, pk in CD.TRACKS], "Your own task fits a track. If not, ask Claude for a dummy pack with 2 planted errors (10 minutes).", cls="tight",
        n=N(do="Read the four tracks. Match them to the board clusters.", expect="Assurance picks extraction or analysis; Support picks workflow or reporting.", silent="say which track the coordinators' tasks fit.")))
    s.append(task("b3task2", "b3", "t15", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 4 · Build: Instruction
    s.append(story("b4story", "b4", "Lesson 4 · Build: Instruction", "Sunday 1 November, 12:30",
        "Faisal reviews Dana's first agent. The table looks right, <b>but one supplier had no PO number, and the agent filled in a likely one.</b>",
        "The fifth part is the one <span class=\"hl\">people forget.</span>", "Write instructions in five parts and test them.",
        n=N(do="Approve the remaining cards in the first five minutes while the room reads.", expect="All cards approved by 12:35.", silent="ask: what should the agent have written?"), time="12:30-13:20"))
    s.append(tslide("b4parts", "b4", "Lesson 4 · the five parts", "Five parts. <span class=\"hl\">Every instruction.</span>", ["Part", "It tells Claude", "Invoice agent"],
        [["<b>Role</b>", "Who it is", "An audit associate at Mirqab"], ["<b>Steps</b>", "What to do, in order", "Read, find, compare"], ["<b>Rules</b>", "What must always be true", "KWD, three decimals, never round"],
         ["<b>Output format</b>", "The exact shape", "The template's columns"], ["<b>When unsure</b>", "What to do with a gap", "Write Not found. Never guess."]],
        "Role · Steps · Rules · Output format · When unsure.",
        n=N(do="Map each part to Dana's card.", expect="When unsure is the part people miss.", silent="ask: which part would have saved Dana's PO?")))
    s.append(term("b4t2", "b4", "Lesson 4 · test", "Show one example. <span class=\"hl\">Then test three.</span>", "Example output and testing",
        "One filled <b>example output</b> in the knowledge teaches the shape faster than a description. Then check <b>three cases where you know the answer</b> before you trust it.",
        "A new joiner learns from one good working paper…", "…and you <b>review their first three</b>.", "Fix the instructions, not the answer.",
        n=N(do="Show the template with its example row.", expect="People see the example row in the knowledge file.", silent="ask: how many tests before you trust a new joiner?")))
    s.append(check("b4chk", "b4", "Your agent fills in a likely PO number when the invoice has none. <b>What do you fix?</b>",
        [("The answer, by hand, each time", 0, "Then it happens again next run."), ("The When unsure part: write Not found, never guess", 1, "Right. Fix the instructions."), ("Nothing: the PO looked right", 0, "Looked right is not right.")]))
    s.append(player("b4pp", "b4", "d16"))
    s.append(tslide("b4map", "b4", "Lesson 4 · transfer", "Instructions <span class=\"hl\">in other tools.</span>", ["", "Claude", "ChatGPT", "Microsoft 365 Copilot", "Gemini"],
        [["Instruction"] + C.TRANSFER[0][1:]],
        "The five parts work in every assistant. Paste them where the tool keeps its instructions.", cls="tight",
        n=N(do="Point to the Copilot or ChatGPT cell RSM is most likely to use.", expect="People see the same five parts in a different box.", silent="read the ChatGPT cell.")))
    s.append(task("b4task", "b4", "t16", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 5 · Build: Input and Output
    s.append(story("b5story", "b5", "Lesson 5 · Build: Input and Output", "Sunday 1 November, 13:30",
        "Every Sunday, Noura, a project coordinator, downloads the same files from the shared drive and <b>drags them into a chat, one by one.</b>",
        "The files are already somewhere. <span class=\"hl\">Let the agent read them there.</span>", "Read from a Drive folder and return a fixed-shape output.",
        n=N(do="Ask: how many files do you drag into a tool each week?", expect="Many, every week.", silent="say: tomorrow a schedule cannot drag files."), time="13:30-14:25"))
    s.append(term("b5t1", "b5", "Lesson 5 · input", "A key to one cabinet, <span class=\"hl\">not the whole archive.</span>", "Connector",
        f"A <b>connector</b> lets Claude read from an app such as Google Drive. It reaches every file the signed-in account can open, so today you use a CODED account that opens only the <b>{D.SANDBOX}</b>.",
        "One key, one cabinet…", "…one connector, <b>an account that opens only what the task needs</b>.", "Customize, then Connectors, then Google Drive.",
        n=N(do="Show Google Drive under Customize, then Connectors (connected before Day 1).", expect="The connector and the sandbox folders.", silent="ask: which folders should an audit agent never see?",
            fallback="If sign-in fails, upload the files and continue.")))
    s.append(check("b5chk1", "b5", "Your agent will run tomorrow at 08:00. <b>Why can it not use files you drag in?</b>",
        [("Dragging files is too slow", 0, "Speed is not the reason."), ("Nobody is there to drag them at 08:00", 1, "Right. The input must live where the agent can read it."), ("Drive files are safer", 0, "Safety comes from what you connect, not from Drive.")]))
    s.append(player("b5pp1", "b5", "d17"))
    s.append(task("b5task1", "b5", "t17", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(term("b5t2", "b5", "Lesson 5 · output", "Same shape. <span class=\"hl\">Every run.</span>", "Artifact and fixed shape",
        "An <b>artifact</b> is an output you can open, edit and download, such as a table or a file. A <b>fixed shape</b> means the same columns, order and total line on every run.",
        "The firm's working-paper template…", "…makes <b>this week comparable with last week</b>.", "Name the columns, in order, in the instructions.",
        n=N(do="Show two runs of the invoice agent side by side.", expect="Same columns, same total line.", silent="ask: what does a reviewer look at first?")))
    s.append(check("b5chk2", "b5", "Why does a scheduled agent need a <b>fixed output shape?</b>",
        [("So each run can be compared with the last", 1, "Right. Reviewers compare, they do not reread."), ("So the file is smaller", 0, "Size is not the point."), ("So Claude runs faster", 0, "Speed is not the point.")]))
    s.append(player("b5pp2", "b5", "d18"))
    s.append(tslide("b5map", "b5", "Lesson 5 · transfer", "Input and output <span class=\"hl\">in other tools.</span>", ["", "Claude", "ChatGPT", "Microsoft 365 Copilot", "Gemini"],
        [["Input"] + C.TRANSFER[1][1:], ["Output"] + C.TRANSFER[2][1:]],
        "The boxes stay the same. Only the button names change.", cls="tight",
        n=N(do="Read the Copilot column if RSM uses Microsoft 365.", expect="People recognize SharePoint and OneDrive.", silent="read the ChatGPT column.")))
    s.append(task("b5task2", "b5", "t18", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 6 · Build: Package
    s.append(story("b6story", "b6", "Lesson 6 · Build: Package", "Sunday 1 November, 14:45",
        "Dana's agent works in her Project. Faisal asks: <b>“Can the other two associates use it? And can it run tomorrow without you?”</b>",
        "A method only you can run <span class=\"hl\">is not a method yet.</span>", "Package the method as a skill and test it on a messy sample.",
        n=N(do="Ask: how does the firm share a method today?", expect="A manual, a template, a checklist.", silent="say: the methodology manual."), time="14:45-15:30"))
    s.append(term("b6t1", "b6", "Lesson 6 · the idea", "From your desk <span class=\"hl\">to the firm's manual.</span>", "Skill",
        "A <b>skill</b> is a saved method that Claude loads when a task matches it. It works in any chat, in Cowork and in scheduled tasks, and you can share it.",
        "A Project is one person's desk…", "…a skill is <b>the methodology manual</b>, usable anywhere.", "Customize, then Skills. Code execution must be on.",
        n=N(do="Show the Skills page on the presenting laptop.", expect="People see built-in skills and an empty space for their own.", silent="ask: who else in your team does your task?")))
    s.append(check("b6chk", "b6", "Your method must work in any chat, in Cowork and on a schedule. <b>What do you package it as?</b>",
        [("A Project", 0, "A Project keeps it in one place. A skill travels."), ("A skill", 1, "Right. The skill travels to chats, Cowork and schedules."), ("A saved chat", 0, "Chats do not travel.")]))
    s.append(player("b6pp", "b6", "d19"))
    s.append(tslide("b6map", "b6", "Lesson 6 · transfer", "A packaged method <span class=\"hl\">in other tools.</span>", ["", "Claude", "ChatGPT", "Microsoft 365 Copilot", "Gemini"],
        [["Package"] + C.TRANSFER[3][1:]],
        "Elsewhere it is a ChatGPT skill or custom GPT, a Copilot agent or a Gem. The card inside stays the same.", cls="tight",
        n=N(do="Ask which of these the room has seen at work.", expect="Custom GPTs or Copilot agents.", silent="say: the name changes, the method stays.")))
    s.append(check("b6chk2", "b6", "A colleague in another firm uses ChatGPT. <b>Where would your invoice skill live there?</b>",
        [("In a ChatGPT skill or custom GPT, same card inside", 1, "Right. The name changes; the card stays."), ("Nowhere: only Claude can package a method", 0, "Every assistant has a packaged method."),
         ("In one long chat that she keeps open", 0, "Chats do not travel.")]))
    s.append(task("b6task", "b6", "t19", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(task("b6task2", "b6", "t110", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Lesson 7 · Show and tell, and the Day 2 hook
    s.append(timer_slide("b7show", "b7", "Show and tell · 15:40", "Four teams. <span class=\"hl\">Ninety seconds each person.</span>",
        "Show your card, then run your skill live on one file from your pack. Your team watches and asks one question.", 12,
        n=N(do="Teams demo at their own tables at the same time. Walk between them.", expect="Most agents run; some flag the messy sample.", silent="start the first team yourself.",
            fallback="If a live run hangs, show the last good result.", say="Card, then run. Ninety seconds.")))
    s.append(player("b7demo", "b7", "d111"))
    s.append(wrap("w1", "close", "One card. One Project. <span class=\"hl\">One skill each.</span>",
        [("You built", "Your own agent", "A card, a Project, a folder, a fixed shape and a skill."), ("You found", "2 planted problems", f"SCC-0718 and the {D.CUTOFF_INV} cut-off, plus your messy file."),
         ("The habit", "Flag, never guess", "Claude does the first pass. You review.")],
        "Tomorrow: your team's agent runs on a schedule. Vote on the board for the agent to automate by 08:40."))
    return s

# ------------------------------------------------------------------ Day 2 · Turning Agents into Operational Workflows
def day2():
    s = opening(2)
    # Lesson 1 · From agent to system
    s.append(rule("c1rule", "c1", "Callback · Day 1", "Yesterday it ran at 15:55. <span class=\"hl\">Today it runs every morning.</span>",
        "Each of you has a card, a Project and a skill. Three quick questions, then one agent per team gets its When box.",
        n=N(do="Ask who saw the 15:55 file arrive.", expect="Most hands.", silent="open the Outputs folder and show the file.", time="08:30-09:20")))
    s.append(check("c1chk1", "c1", "Where does this month's invoice pack go in an agent?",
        [("Into the Project knowledge", 0, "Knowledge is what stays the same."), ("Into each run, from the folder", 1, "Right. Input changes every run."), ("Into the instructions", 0, "Instructions hold the rules.")]))
    s.append(check("c1chk2", "c1", "An invoice has no PO number. <b>What should the agent write?</b>",
        [("Not found, and a note", 1, "Right. Flag, never guess."), ("The most likely PO", 0, "That is a guess."), ("Nothing", 0, "A blank hides the gap.")]))
    s.append(check("c1chk3", "c1", "Which one travels to any chat, to Cowork and to a schedule?",
        [("A chat", 0, "Chats do not travel."), ("A Project", 0, "A Project keeps the method in one place."), ("A skill", 1, "Right. A skill goes wherever the task goes.")]))
    s.append(story("c1story", "c1", "Lesson 1 · From agent to system", "Monday 2 November, 08:38",
        "Faisal looks at Dana's agent: <b>“It is good. Who runs it when you are on leave? And who checks it before anyone relies on it?”</b>",
        "An agent that waits for you <span class=\"hl\">is a tool.</span>", "Map a workflow: trigger, steps, output and review.",
        n=N(do="Ask: who runs your weekly tasks when you are on leave?", expect="Nobody, or a colleague who does it differently.", silent="say: usually nobody, until you are back.")))
    s.append(scene("c1scene", "c1", "Lesson 1 · the picture", "A standing instruction <span class=\"hl\">to the bank.</span>",
        "You set it once: on the first of every month, pay this amount to this account. It runs on time. The statement shows every payment, and you review it.",
        "Trigger · Steps · Output · Review.",
        [{"ground": 268}, {"clock": (80, 240), "label": "Trigger", "tone": "hot", "anim": "glow"}, {"building": (230, 268), "tone": "dim"}, {"doc": (380, 240), "label": "Output", "tone": "ok"},
         {"move": "coin", "path": [(110, 200), (230, 140), (360, 200)], "dur": 5}, {"person": (440, 268), "label": "Review", "anim": "nod"},
         {"pill": "Runs on time", "at": (150, 44), "tone": "hot", "delay": 0}, {"pill": "You check the statement", "at": (320, 90), "tone": "", "delay": 2}],
        n=N(do="Ask who has a standing instruction at their bank.", expect="Most hands.", silent="describe your own, for example rent.", say="A workflow is a standing instruction with a review step.")))
    s.append(term("c1t1", "c1", "Lesson 1 · the idea", "Four parts <span class=\"hl\">of a workflow.</span>", "Workflow",
        "A <b>trigger</b> starts it: a time or an event. <b>Steps</b> do the work: your skill. The <b>output</b> goes where a person sees it. <b>Human review</b>: a named person checks before anyone relies on it.",
        "The standing instruction…", "…plus <b>a named reviewer</b>. Audit needs both.", "No workflow runs without a named reviewer.",
        n=N(do="Map the invoice agent to the four parts.", expect="Time trigger, the skill, a file in Outputs, Faisal reviews.", silent="map it yourself, slowly.")))
    s.append(check("c1chk4", "c1", "What starts a scheduled workflow?",
        [("The trigger: a time or an event", 1, "Right. Today the trigger is a time."), ("The reviewer", 0, "The reviewer comes after the output."), ("The skill", 0, "The skill is the steps.")]))
    s.append(player("c1pp", "c1", "d21", n=N(more=["First, two minutes: read the vote from the board's Teams and votes tab and name one agent per team. Each team works on that agent's owner's laptop today."])))
    s.append(task("c1task", "c1", "t21", n=N(do="Start the timer. Walk the room. Ask each team what they found so far.")))
    # Lesson 2 · Make it run on its own
    s.append(story("c2story", "c2", "Lesson 2 · Make it run on its own", "Monday 2 November, 09:30",
        "Dana's invoice agent needs a person to open Claude and type one line. <b>Tomorrow at 08:00 Dana is at a client.</b>",
        "Set it once. <span class=\"hl\">It runs on time.</span>", "Set up a scheduled task that runs your team's skill.",
        n=N(do="Ask: what time would your team's workflow run?", expect="Early morning or Sunday.", silent="say: daily at 08:00 for invoices."), time="09:30-10:20"))
    s.append(term("c2t1", "c2", "Lesson 2 · the idea", "A calendar reminder <span class=\"hl\">that also does the work.</span>", "Scheduled task",
        "A <b>scheduled task</b> is a saved prompt that Claude runs on a frequency: hourly, daily, weekdays, weekly or manual. Its prompt calls your <b>skill</b> and reads through your <b>connectors</b>.",
        "A reminder that only reminds you…", "…versus one that <b>does the work and leaves the file</b>.", "Click Scheduled in the left sidebar, then New task.",
        n=N(do="Click Scheduled in the left sidebar on the presenting laptop.", expect="People see the Scheduled item in the sidebar.", silent="ask: which part of the card does this fill?")))
    s.append(term("c2t2", "c2", "Lesson 2 · what it can do", "It runs in the cloud. <span class=\"hl\">Each run starts fresh.</span>", "How a scheduled run works",
        "The task runs even when your laptop is closed. Each run is <b>its own session</b>. Do not rely on it to recall the last run: the prompt, the skill and the folders must say everything.",
        "A new joiner on each run…", "…who only knows <b>the prompt, the skill and the folders</b>.", "Anything the run needs must be written down.",
        n=N(do="Ask: what can a run count on from yesterday?", expect="Only what the run log and the folders show.", silent="say: only what is written down. That is why we keep a run log.")))
    s.append(listslide("c2steps", "c2", "Lesson 2 · step by step", "Six steps <span class=\"hl\">to a schedule.</span>",
        ["<b>Open:</b> click Scheduled in the left sidebar.", "<b>New task:</b> upper right, then Set up manually.", "<b>Name and prompt:</b> the prompt calls your skill and names the folders.",
         "<b>Approval mode:</b> choose the mode that lets the run save and move files without waiting for you.", "<b>Frequency:</b> daily at 08:00. Kuwait works Sunday to Thursday, so Friday and Saturday runs log No new files.", "<b>Test:</b> run it once on demand and check the output."],
        "If the test run works, the schedule will work.",
        n=N(do="Build the invoice schedule live while you talk.", expect="The task appears on the Scheduled page.", silent="ask which step they would skip. None.",
            more=["If the form has no time field for Daily, use Create with Claude and say the time. The pre-flight checks this."],
            fallback="If Cowork is off on the presenting account, play the next slide.")))
    s.append(check("c2chk", "c2", "Your scheduled task runs at 08:00. <b>What should it rely on from yesterday's run?</b>",
        [("Its memory of yesterday's session", 0, "Each run is its own session."), ("Only what the run log and the folders show", 1, "Right. Write down what each run needs."), ("The last file it read", 0, "Do not rely on it to recall files.")]))
    s.append(player("c2pp", "c2", "d22"))
    s.append(task("c2task", "c2", "t22", n=N(do="Start the timer. Walk the room. Ask each team what they found so far.")))
    s.append(tslide("c2map", "c2", "Lesson 2 · transfer", "Scheduling <span class=\"hl\">in other tools.</span>", ["", "Claude", "ChatGPT", "Microsoft 365 Copilot", "Gemini"],
        [["When", "Scheduled task", "Scheduled task", "Scheduled prompt", "Scheduled action"], ["Event triggers", "n8n or Power Automate", "n8n or Power Automate", "Power Automate", "n8n or Apps Script"]],
        "Time triggers live in the assistant. Event triggers need an automation tool.", cls="tight",
        n=N(do="Read the When row, then the Event row.", expect="People ask about Power Automate: say IT owns it at most firms.", silent="read the Copilot column.")))
    # Lesson 3 · New inputs, outputs and n8n
    s.append(story("c3story", "c3", "Lesson 3 · New inputs and outputs", "Tuesday 3 November, 08:00",
        "The schedule ran at 08:00. <b>It processed yesterday's invoices again</b>, because nobody moved them, and the file in Outputs replaced yesterday's.",
        "New files in. <span class=\"hl\">A named file out.</span>", "Handle new files and an empty folder, and keep a run log.",
        n=N(do="Ask: what went wrong?", expect="Old files read twice; the output overwritten.", silent="say: no Processed folder, no date in the name."), time="10:30-11:30"))
    s.append(term("c3t1", "c3", "Lesson 3 · inputs and outputs", "Inbox, Processed, <span class=\"hl\">Outputs.</span>", "Changing inputs and delivered output",
        "The run reads new files in the <b>Inbox</b> and moves each one to <b>Processed</b>. It saves a file with the date and time in its name to <b>Outputs</b>, or an email draft.",
        "An in-tray and an out-tray…", "…nothing is <b>read twice</b>, nothing is <b>overwritten</b>.", "Name outputs client-task-date-time.",
        n=N(do="Show the three folders in the sandbox Drive.", expect="People see Inbox, Processed, Outputs in their team folder.", silent="ask: what happens if Processed is missing?")))
    s.append(check("c3chk0", "c3", "The 08:00 run has read three new invoices. <b>What happens to them next?</b>",
        [("They stay in the Inbox for the next run", 0, "Then the next run reads them again."), ("The run moves each one to Processed", 1, "Right. Nothing is read twice."),
         ("The run deletes them to save space", 0, "Keep them: Processed is the trail.")]))
    s.append(term("c3t2", "c3", "Lesson 3 · the empty folder", "No files? <span class=\"hl\">One honest line.</span>", "The empty-folder rule",
        "If the Inbox has no new files, the run writes <b>No new files</b> in the run log and stops. It never reprocesses old files to fill the gap.",
        "An automation that breaks on an empty folder…", "…<b>is not an automation</b>.", "Read the run log every morning, even on quiet days.",
        n=N(do="Ask: what should the run do on a public holiday?", expect="One line, then stop.", silent="say: one line in the log, nothing else.")))
    s.append(check("c3chk", "c3", "The Inbox is empty at 08:00. <b>What should the run do?</b>",
        [("Process last week's files again", 0, "That doubles the work and the risk."), ("Write No new files in the run log and stop", 1, "Right. One honest line."), ("Create a sample to process", 0, "That is a made-up input.")]))
    s.append(player("c3pp", "c3", "d23"))
    s.append(task("c3task", "c3", "t23", n=N(do="Start the timer. Walk the room. Ask each team what they found so far.")))
    s.append(rule("c3when", "c3", "Lesson 3 · when n8n", "A time trigger is enough for your week. <span class=\"hl\">Events need more.</span>",
        "Some triggers are events: an email arrives, a form is sent, a file lands. When the trigger is an event or the systems belong to the company, the next step is an automation tool such as n8n.",
        n=N(do="Ask: which of your tasks starts when an email arrives?", expect="Client documents, requests.", silent="say: the request inbox at Mirqab.")))
    s.append(player("c3demo", "c3", "d24", n=N(time="13 min", more=["Built and tested before the workshop. Send one test email live; if it is slow, step through the flow on this slide and show the comparison table."])))
    s.append(tslide("c3cmp", "c3", "Lesson 3 · which tool", "Two tools, <span class=\"hl\">two jobs.</span>", ["", "Claude scheduled task", "n8n"],
        [["Starts", "At a time", "On an event: an email, a form, a file"], ["You build it", "By describing the task", "By connecting blocks (nodes)"],
         ["Best for", "Your own weekly work", "Company systems, many steps, many people"], ["Set up by", "You", "Usually IT or an automation owner"]],
        "Start with a schedule. Move to n8n when the trigger is an event.",
        n=N(do="Ask which column fits each team's workflow.", expect="All four fit the schedule today.", silent="say: all four teams, the schedule column.")))
    s.append(check("c3chk2", "c3", "Client documents arrive by email at any time. The team wants each one logged <b>as it lands</b>. Which tool fits?",
        [("An automation tool such as n8n, set up with IT", 1, "Right. The trigger is an event."), ("A Claude scheduled task, daily at 08:00", 0, "That waits for a time, not for the email."),
         ("One long chat that someone keeps open", 0, "A chat does not run on its own.")]))
    # Lesson 4 · Fit it to your department
    s.append(story("c4story", "c4", "Lesson 4 · Fit it to your department", "Wednesday 4 November, 08:05",
        f"A USD invoice arrived. One rule says show amounts in KWD; another says never convert. <b>The run converted it at a rate it did not show.</b>",
        "Your department's rules, <span class=\"hl\">word for word.</span>", "Add department rules and a human review step.",
        n=N(do="Ask: which rule should win, and who decides?", expect="The department decides: flag other currencies, never convert.", silent="read the Assurance rules from the file."), time="12:30-13:20"))
    s.append(term("c4t1", "c4", "Lesson 4 · rules", "The rules are yours, <span class=\"hl\">not Claude's.</span>", "Department rules",
        "Thresholds, sign-off levels, file names and what never happens (no adjustments, no conversions). Written in the skill <b>word for word</b>, so every run follows them.",
        "The firm's review rules…", "…copied into the skill, <b>not paraphrased</b>.", "A paraphrase is a new rule.",
        n=N(do="Open mirqab-review-rules.docx on screen.", expect="People find their department's section.", silent="read the All departments rules.")))
    s.append(check("c4chk0", "c4", "The Assurance rule says: amounts in another currency are flagged, never converted. <b>How does it go into the skill?</b>",
        [("Word for word, as the firm wrote it", 1, "Right. A paraphrase is a new rule."), ("In shorter words that Claude will follow", 0, "Shorter words can change the rule."),
         ("It stays out: Claude knows audit rules", 0, "It knows what is usual, not your firm's rules.")]))
    s.append(term("c4t2", "c4", "Lesson 4 · review", "Drafts only. <span class=\"hl\">A named person signs off.</span>", "Review step and run log",
        "Every output is marked <b>DRAFT</b> and ends with <b>Reviewed by</b>. Each run saves a <b>run-log</b> file in the Log folder: date, files read, items flagged, file saved.",
        "A working paper with a reviewer's initials…", "…<b>a file with DRAFT and Reviewed by</b>.", "The agent routes. The supervisor decides.",
        n=N(do="Show a DRAFT output with the Reviewed by line.", expect="People recognize the review stamp idea.", silent="ask: who signs your working papers?")))
    s.append(check("c4chk", "c4", "A workflow drafts a follow-up to a client with a wrong deadline. <b>Which change prevents a repeat?</b>",
        [("Run it once a week", 0, "Less often does not mean correct."), ("Drafts only, a reviewer, and a date check", 1, "Right. A person signs off."), ("Use a newer AI model", 0, "Any model can predict a wrong date.")]))
    s.append(player("c4pp", "c4", "d25"))
    s.append(task("c4task", "c4", "t25", n=N(do="Start the timer. Walk the room. Ask each team what they found so far.")))
    # Lesson 5 · Test and prepare the demo
    s.append(story("c5story", "c5", "Lesson 5 · Test and prepare the demo", "Thursday 5 November, 13:30",
        "At 14:45 Dana shows the invoice workflow to the partners. <b>They will ask two things: does it run, and what does it save?</b>",
        "Show the run, <span class=\"hl\">then the number.</span>", "Measure the impact and prepare a five-minute demo.",
        n=N(do="Read the rubric before the story ends.", expect="Questions about how the score works.", silent="say the five criteria."), time="13:30-14:25"))
    s.append(stats("c5stats", "c5", "Lesson 5 · impact", "Minutes saved <span class=\"hl\">every month.</span>",
        [(f"{D.IMPACT_EX['by_hand']} min", "By hand", "One run of the task, done by a person."), (f"{D.IMPACT_EX['agent']} min", "With the agent", "Including the review."),
         (f"{D.IMPACT_MIN} min", "Saved a month", f"({D.IMPACT_EX['by_hand']} − {D.IMPACT_EX['agent']}) × {D.IMPACT_EX['runs']} runs: about 12 hours.")],
        "(Minutes by hand − minutes with the agent) × runs a month.", src="Example figures. Use your own timings from the board's Clock tab.",
        n=N(do="Work one team's numbers with the room.", expect="A few hours a month per task.", silent="work the invoice example: (45 − 6) × 22.")))
    s.append(tslide("c5rubric", "c5", "Lesson 5 · the judges' rubric", "Fifty points. <span class=\"hl\">Five criteria.</span>", ["Criterion", "Points", "Full marks"],
        [[c, str(pt), t] for c, pt, t in CD.RUBRIC_FULL],
        f"Five criteria, 10 points each. Total: {sum(pt for _c, pt, _t in CD.RUBRIC_FULL)}.", cls="tight",
        n=N(do="Read each criterion. Ask how the panel will check source accuracy.", expect="Someone says: pick figures from the output and find them in the file.",
            silent="say: the panel picks three figures from your output, and you show each one in its source file.")))
    s.append(listslide("c5script", "c5", "Lesson 5 · the demo", "Five beats. <span class=\"hl\">Five minutes.</span>",
        ["<b>Problem:</b> what it costs today.", "<b>Card:</b> the workflow card.", "<b>Live run:</b> a run on demand, on screen.", "<b>Impact:</b> minutes saved a month.", "<b>Next:</b> the next task you would automate."],
        "Rehearse the live run. It is the part that fails.",
        n=N(do="Ask each team who presents which beat.", expect="Teams split the beats.", silent="suggest one presenter per beat.")))
    s.append(player("c5pp", "c5", "d26"))
    s.append(check("c5chk", "c5", "A task takes 40 minutes by hand and 5 with the agent, 20 times a month. <b>About how much time does it save?</b>",
        [("About 7 hours", 0, "700 is minutes, not hours: divide by 60."), ("About 12 hours", 1, "Right. 35 × 20 = 700 minutes."), ("About 13 hours", 0, "That counts the full 40 minutes: 40 × 20 = 800.")]))
    s.append(listslide("c5fail", "c5", "Lesson 5 · when a step fails", "When a step fails, <span class=\"hl\">the run says so.</span>",
        [f"<b>Test it:</b> copy {CD.F_LOCKED}, a file no run can read, into the Inbox. Run on demand.",
         "<b>Good run:</b> the run log says Could not read and names the file. The file stays in the Inbox. Nothing is guessed.",
         "<b>Bad run:</b> a silent log, or an output row with made-up values.",
         "<b>Fallback:</b> one line in the prompt says what to do, and the named reviewer checks that file by hand.",
         "<b>No Drive:</b> if the connector is off, no run log is written. A missing log means: check the run."],
        "Test the failure before Demo Day, not during it.",
        n=N(do="Open the run log from the pre-flight locked-file test (Log folder of the test folder) and read its Could not read line. Then show the fallback line on the Day 2 prompt sheet.", expect="Someone asks why not just skip the file. Answer: a skip nobody sees is a gap in the audit file.",
            silent="ask: who checks the locked file by hand on your team?", fallback="If the pre-flight log is missing, show the Task 2.5 backup table.",
            more=["The test is part of Task 2.5. The skill owner adds the fallback line before the test run."])))
    s.append(check("c5chk2", "c5", "The 08:00 run log says <b>Could not read: lease-scan.pdf</b>. The other files are in Outputs. <b>What happens next?</b>",
        [("Run it again until Claude reads the file", 0, "A rerun gives the same result. A person acts."), ("The named reviewer checks that file by hand", 1, "Right. The log told you which file needs a person."), ("Nothing: the other files were processed", 0, "The locked file is still a gap in the work.")]))
    s.append(task("c5task", "c5", "t26", n=N(do="Start the timer. Walk the room. Ask each team what they found so far.")))
    # Lesson 6 · Demo Day
    s.append(timer_slide("c6demo", "c6", "Demo Day · 14:45", "Four teams. <span class=\"hl\">Eight minutes each.</span>",
        "Five minutes of demo, three minutes of questions. The panel scores each automation out of 50.", 8,
        n=N(do="Restart the timer for each team. Score on the board's Teams and votes tab.", expect="Four live runs, four impact numbers.", silent="ask the first panel question yourself.",
            fallback="If a live run fails, the team shows its latest output file and run log.", say="Team one, the floor is yours.", time="14:45-15:30")))
    s.append(tslide("c6order", "c6", "Demo Day · running order", "Who presents <span class=\"hl\">when.</span>", ["Team", "Time", "Workflow"],
        [["Team 1", "14:45", "From the board"], ["Team 2", "14:53", "From the board"], ["Team 3", "15:01", "From the board"], ["Team 4", "15:09", "From the board"]],
        "Scoring and panel comments from 15:17.",
        n=N(do="Fill the workflow names from the board before 14:45.", expect="Teams ready at their laptops.", silent="call Team 1.")))
    s.append(tslide("c6score", "c6", "Demo Day · scoring", "The panel's <span class=\"hl\">score sheet.</span>", ["Criterion", "10", "5", "0"],
        [list(r) for r in CD.RUBRIC_SCORE],
        f"Total out of {sum(pt for _c, pt, _t in CD.RUBRIC_FULL)}. The trainer scores. RSM leadership joins if they attend.", cls="tight",
        n=N(do="Keep this slide up while the panel scores.", expect="Scores on the board within 8 minutes.", silent="read each team's strongest point aloud.")))
    # Close
    s.append(mapslide("c7map", "c7", "after"))
    s.append(timer_slide("c7next", "c7", "Next steps · 15:55", "Your next task. <span class=\"hl\">Your tool.</span>",
        "Post on the board the next task you will automate back at work, and the tool you will use for it.", 5,
        n=N(do="Read three posts aloud.", expect="Tasks from the inventory; Copilot or Claude as the tool.", silent="post your own first.", say="One task, one card, this week.")))
    s.append(wrap("w2", "close", "Card, schedule, review. <span class=\"hl\">Then show it.</span>",
        [("You built", "A scheduled workflow", "Your team's skill, running on new files, with rules and a run log."), ("You showed", "Four automations", "Each with an impact number."),
         ("The habit", "Drafts, never final", "Claude does the first pass. You sign off.")],
        "This week: one card for one task, on dummy data, in an approved tool."))
    return s

TOPICS = {1: {"open": "Opening", "b1": "Lesson 1 · AI foundations", "b2": "Lesson 2 · Why chat isn't enough", "b3": "Lesson 3 · Design the agent",
              "b4": "Lesson 4 · Build: Instruction", "b5": "Lesson 5 · Build: Input and Output", "b6": "Lesson 6 · Build: Package", "b7": "Lesson 7 · Show and tell", "close": "Close"},
          2: {"open": "Opening", "c1": "Lesson 1 · From agent to system", "c2": "Lesson 2 · Make it run on its own", "c3": "Lesson 3 · New inputs, outputs and n8n",
              "c4": "Lesson 4 · Fit it to your department", "c5": "Lesson 5 · Test and prepare the demo", "c6": "Lesson 6 · Demo Day", "c7": "Post-MAP, survey and next steps", "close": "Close"}}
DAYFN = {1: day1, 2: day2}
