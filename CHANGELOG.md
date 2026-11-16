# Changelog

## 2026-11-16 11:15 · Submission tidy (Aya)

- Project page: the five-part instructions are out of the submission document (8 items; the build prompt renumbered); the Open the
  submission form button sits after the list and the prompt; the Your notes box is gone (plan step 1 no longer points to it).

## 2026-11-16 11:10 · Project submission (Aya)

- Project page: a Submit section before the Done-when list: Aya's Google Form (short link /submit), the nine things the Word document holds
  (name and department, Project card, five-part instructions, skill name and description, artifact link or screenshot, scheduled task and the
  first line of its run, three figures checked, the problems flagged, impact and next task), and a COPY prompt that builds the document in the
  Project chat with [missing] for gaps. New Done-when tick. Lab step 7, Task 2.6's deliverable and the Task 2.6 script name the form.

## 2026-11-16 10:05 · Project prompts behind three steps of help (Aya)

- Project page: Build plan, Turn the Project into a skill, Dashboard request, Check three figures and Demo script are "write it yourself"
  cards: Stuck? Show a hint → Still stuck? Show another hint → Still stuck? Show the prompt (state kept in the browser).
  Put the layout in my skill, Add my file to the skill and the scheduled task prompt stay as COPY. The 85-minute plan says "write your own".
- Task 2.6 slide and prompt sheet: only the two schedule prompts and the blank Project card; the thinking prompts are only behind the hints.

## 2026-11-16 09:45 · The mini project has its own page (Aya)

- New page coded-rsm-ai-automation-mini-project.html (short link /project), built by `kit/project_page.py` from gen_files.py as a site file:
  pick one of 11 departments or Your own task; each shows a work scenario, the file, what the agent must do, the artifact, when and who
  reviews, and a Project card filled in for that department (COPY). Below: the 85-minute plan, every project prompt with COPY,
  a Done-when checklist and a notes box (saved in the browser). No answers on the page.
- Lab Day 2: steps 7 and 8 replaced by one pointer step to the page (7 steps). Task 2.6 step 1 and the packs slide name coded-rsm.vercel.app/project.

## 2026-11-16 08:35 · The n8n video plays on the Demo 2.4 slide (Aya)

- New kit helper `videodemo` in build_deck.py: the Demo 2.4 live-demo slide shows the video player in place of the Files card
  (root-absolute src, so the public and /staff decks both load it); the file chip stays under the player as a download.

## 2026-11-16 06:10 · The n8n demo is the video only (Aya)

- Demo 2.4: no live n8n build. The slide badge reads "n8n · video"; the notes say play the video and talk over it. The prompt sheet's
  n8n Code step is replaced by "Plan my workflow" (Claude describes the trainee's own event-driven task as trigger, steps and output; nothing is built).
  Lab step 6, the lesson plan, the runbook and the facilitator kit say video only.

## 2026-11-15 22:45 · No connectors on Day 2 (Aya: the trainees cannot use MCP on their work accounts)

- Task 2.5 and Demo 2.3: the schedule runs the skill on a reference file stored inside the skill (new prompts: Add my file to the skill,
  and a scheduled prompt whose first line is the run log, marked DRAFT with Reviewed by). No Drive folders, no uploads, nothing moved.
- Lesson 3 slides and script: "reads through your connectors" and the folder rules replaced by input inside the skill, the first-line run log
  and the Scheduled page history; new check "What does each run know?". Callback: no "connected folder"; the 16:25 run is opened on the Scheduled page.
- Lesson 1 "why combine": "the input and a schedule" instead of connectors. Lesson 4 limit: "only the apps your firm allows it to connect to".
- Mini project: the file goes inside the skill before the schedule. Lab steps 5 and 7, the runbook and the prompt-sheet how-to updated.
  The transfer map at the close still names connectors as the Claude feature for Input (a name map, not a task).

## 2026-11-15 night · Day 2 rebuilt on Aya's new order (skills, artifacts, schedules, automation tools, mini project)

- New Day 2 (53 slides, 08:30 to 15:30): callback (two checks) → Lesson 1 · Skills (four building blocks: prompt, Project instructions,
  skill, agent; why combine them; how a skill loads; Demo 2.1 the trainer's mirqab-invoice-match skill live; Task 2.1 a skill for your own task,
  25 min; Task 2.2 will Claude pick it, 8 min; safe sharing) → Lesson 2 · Artifacts (what you can build, by department, five-part request,
  Demo 2.2 a KPI dashboard then a deck from mirqab-engagement-portfolio-2026.xlsx; Task 2.3 your KPI dashboard, 20 min; layout in the skill;
  Task 2.4 dashboard to presentation, 15 min; gallery) → Lesson 3 · Scheduled tasks (fresh runs, run log, No new files; Demo 2.3; Task 2.5 schedule
  your own skill, read-only on the shared track folders, 15 min) → Lesson 4 · Claude, n8n or Power Automate (side by side, what Claude cannot do yet,
  when to switch, trigger / node / output, Demo 2.4 the n8n workflow as a captioned video or live) → Lesson 5 · Mini project (11 department packs
  from RSM's service lines; Task 2.6, 85 min, on your own or in pairs) → Lesson 6 · Project demos picked by the trainer (14:40) → Post-MAP 15:00,
  survey 15:10, certificates 15:15, transfer map and close.
- Retired from Day 2: Tasks 1.8 to 1.10, Demos 1.7 and 1.8 (moved there on 15 Nov), the team workflow card, batch 2 and the empty folder as a task,
  department rules, the failed-run test and the scored Demo Day. Their sample files stay published (names never change).
- New files (14): mirqab-engagement-portfolio-2026.xlsx (Demo 2.2), 11 department packs (audit findings, tax filing calendar, CF deal pipeline,
  risk register, cyber vulnerability scan, IT helpdesk tickets, ESG energy and emissions, sales transactions, budget against actual, HR people data
  with IDs only, CX client survey), each with two planted problems, mirqab-mini-project-briefs.docx, and mirqab-n8n-demo-invoice-routing.mp4
  (100 s, captioned, recorded in Aya's n8n workspace: Schedule Trigger → Code → If over KWD 2,000 → Supervisor review / Approved).
- Script: `kit/notes_day2.py` rewritten for every new slide. Day 2 lab: 8 steps (flag: the blank-hours engagement in the demo file).
  Hours now 08:30-15:30. Portal surveys unchanged (the staff descriptions in the portal still name the old times).

## 2026-11-15 · Artifacts and skills move to Day 2, and the Day 1 changes repeat on Day 2 (Aya, after Day 1)

- Day 1 ended after connectors and show and tell (about 15:40). Removed from Day 1: the output lesson (artifact concept, check, Demo 1.7,
  the input and output transfer slide, Tasks 1.8 and 1.8b), all of Lesson 6 (skills: Demo 1.8, Tasks 1.9 and 1.9b) and Task 1.10. Lesson 5 is
  "Build: Input" (Task 1.7 is 20 minutes, then catch-up); Lesson 7 is now Lesson 6 (show and tell runs the agent, not a skill). The transfer map moves
  to the Day 2 close. Day 1 outcomes, map, wrap, close and lab (9 steps) updated. Day 1 is 62 slides.
- Day 2 opens with the callback (two checks; the skill check moved into the skills lesson), then Lesson 1 · Build: Output (a new story slide,
  Demo 1.7, Tasks 1.8 12 min and 1.8b 13 min) and Lesson 2 · Build: Package (Demo 1.8, Tasks 1.9, 1.9b and 1.10). Their numbers stay. Day 2's own
  lessons are now 3 to 8. Demo Day stays at 15:15: Task 2.1 12 min, 2.2 25, 2.3 20, 2.4 28, 2.5 37 (one rehearsal); the n8n part 13 min; no buffers.
- The Day 1 changes, repeated on Day 2: every demo runs live (Demos 2.2, 2.3, 2.5, 2.6 in Claude; Demo 2.1 on the lab page; Demo 2.4 in n8n);
  a word-for-word speaker script for every slide (`kit/notes_day2.py`); every task and lab step names its place (lab step, prompt sheet entry,
  Claude button, Drive folder); lab steps list their files; a Workflow card template with a COPY button (Task 2.1); no Your turn section on the
  Day 2 page; the transfer map at the end. Repeat cut: the six-steps slide no longer builds the schedule live, because Demo 2.2 does.
- Day 2 lab: 12 steps (1 to 5 are the moved Day 1 tasks). Task 2.5 and the impact slide take the times from lab step 5 (the old Clock tab is gone).
- Staff: lesson plan minutes, MAP "where taught" lines, card boxes, cheat sheet, pre-flight times and class plan updated. Day 2 is 71 slides.
  Portal surveys unchanged.
- Day 2 steps send people to the prompt sheet with the Day 2 page's Open the prompt sheet button: the top-bar Prompts tab on the day and lab pages
  opens the Day 1 sheet (engine behavior, not changed). The Day 2 cover script says this.

## 2026-11-15 · Lesson 4 goes straight to building (Aya, 13:00)

- Removed the repeated Lesson 4 teaching: the PO story, the five parts table, its check, Demo 1.5 (live) and the instructions transfer slide.
  Lesson 4 is now: test before you trust, Task 1.6 (48 min), Task 1.6b (29 min). Lesson 4 is called "Build your agent". Day 1 is 78 slides.
- Demo 1.5 stays on the prompt sheet as a five-part example; it has no slide, so Day 1 demos go 1.4, then 1.6.

## 2026-11-15 · Day 1: a second round for each build block (Aya)

- Two Projects, two artifacts, two skills. New tasks, each with a slide, a lab step, prompt-sheet entries and a script:
  Task 1.6b Project 2 (a second agent on another track, 25 min), Task 1.8b Artifact 2 (a chart or a one-page memo from that data, 12 min),
  Task 1.9b Skill 2 (package the second agent; check Claude picks the right skill for each file, 12 min).
- To keep 08:30-16:30: Task 1.6 is 40 min (hint at 10, fixes at 20), Task 1.7 12, Task 1.8 11, Task 1.9 14, Task 1.10 8.
- Lab steps after Task 1.6 move by one: Task 1.7 is step 9 and the messy file is step 14. Day 1 is 83 slides.

## 2026-11-15 · Day 1: speaker script, clear task steps, no shared board (Aya)

- Day 1 speaker notes are a script: what to say, word for word, with short stage directions in brackets (`_source/kit/notes_day1.py`).
  Live demos keep their click steps and fallback; tasks keep the answer key; checks keep the answer. The notes panel scrolls and reads at 17px.
- No shared board (Google Sheet) on either day. Day 1: the poll is a show of hands; Task 1.3's strongest tasks are typed on screen
  (the board review slide is now a search-bar slide); Agent Cards are approved by the trainer at the seat; Task 1.10 times go in the lab page.
  Day 2: teams pick their agent by a show of hands; the panel writes scores down; next tasks are said at the table.
- Every Day 1 task step says where things are: the lab page step, the prompt sheet entry, the Claude button, the Drive folder.
  The lab page steps match. Task 1.4 has an Agent Card template with a COPY button (prompt sheet, task slide).
- The Lesson 2 card sort uses everyday tasks from every department, not only audit.

## 2026-11-15 · Day 1 lab files and the Day 1 page (Aya)

- Lesson 2: a new card sort after "Which tasks suit an agent?" (slide 31): Can an agent do this task? Eight audit tasks, tap to show Yes, Partly or No.
  To fit it, Task 1.2 is 12 minutes, the Try it 3, Task 1.3 8, the board review 2 (10:18). Day 1 is 80 slides.
- Day 1 lab: each step shows the files to download (Tasks 1.1, 1.2, 1.5, 1.6 and 1.10). Task 1.6 says which track uses which file.
- Day 1 page: the Your turn section is gone; the lab and the prompt sheet carry the tasks. Day 2 keeps it.
  This needed one opt-in engine switch, `HUB["day_your_turn_off"]` in `_source/build/pages.py` (default: unchanged).

## 2026-11-15 · Day 1: live demos and a step-by-step order (Aya)

- Every Day 1 demo (1.1 to 1.9) runs live in Claude. Each playback slide is now a "Live in Claude" holding slide: the demo title, what to watch for,
  the files and where the prompt is (the prompt sheet). The notes keep the steps, the expected result and the fallback (the staff backup page).
  Day 2 demos are unchanged for now.
- Lesson 1: the Claude tour shows only what Task 1.1 needs (new chat, the + button, the message box). Projects, connectors, skills and scheduled
  tasks each come in their own lesson.
- Lesson 2: a 4-minute Try it after the five parts: rewrite your Task 1.2 request with the five parts and run it again. Task 1.2 is 13 minutes,
  Task 1.3 is 9, the board review is 3 again.
- Lesson 3 order: score and pick (Demo 1.3, Dana scores), the four tracks, the Agent Card, literal instructions, **Task 1.4 Agent Card v1**,
  Projects and knowledge, Demo 1.4 (from card to agent), **Task 1.5 build the invoice agent together**. Renumbered: old Demo 1.3/1.4 and
  Task 1.4/1.5 swap numbers. The lab and the prompt sheet follow the new order. Lesson 3 is now "Pick and design".
- Day 1 is 79 slides.

## 2026-11-14 · Day 1 edits (Aya)

- Opening: the Dana story and the weak-and-strong opener are gone. Day 1 now runs cover, **Welcome to CODED** (who we are, your trainer, who is
  here; generic, the trainer introduces themselves), pre-MAP, outcomes, today's map. Opening 08:30-08:50; Lesson 1 starts 08:50.
- Lesson 1: a **What is AI?** slide after the AI foundations story, with a search bar. The trainer types the room's answers; each shows as a chip
  (a repeat shows ×2, a click removes a typo, Clear empties it). Nothing is saved or sent. Esc leaves the bar; with the bar empty, → and ← move slides.
- Lesson 1: Demo 1.1 (the wrong invoice row) is replaced by **two real hallucination cases**: Mata v. Avianca (fake court cases, 2023) and
  Moffatt v. Air Canada (a chatbot's made-up refund rule, 2024), with sources on the slide. The quick check on a wrong invoice figure follows it.
- The **transfer map** moves from Lesson 1 to the end of Day 1 (Lesson 7, before the wrap). The Lesson 4 to 6 transfer slides stay.
- Lesson 2, after Task 1.2: why the prompt matters, **Demo 1.1** (the weak and strong request, moved here from the opener and renumbered from 1.0),
  the five parts of a good prompt, a check, then repeatable, **what an agent is**, then agent-ready tasks. Task 1.2 is 15 minutes (was 18),
  Task 1.3 is 10 (was 12), the board review 2 (was 3), so Lesson 2 still ends at 10:20.
- Day 1 outcomes add "Write a five-part prompt". Day 1 is 78 slides (was 73).
- Day 1 lab page: Task 1.1 and Task 1.2 added as the first two steps (it started at Task 1.3).
- Lesson plan, class plan, prompt sheet, answer key, backups, notes, day page and hub rebuilt from the kit. Portal surveys unchanged.

## 2026-11-11 · Hours 08:30-16:30

- Both days now run 08:30-16:30 (was 16:00). Day 1: Task 1.6 is 65 minutes (struggle 30, unlock 15, fix 20; hint at 15, common fixes at 30).
  Day 2: Task 2.5 is 70 minutes (three clean runs 20, failed-run test 12, impact 6, demo plan 12, rehearse twice 20).
- Everything after those tasks moves 30 minutes later on both days: Asr 14:55-15:15, Day 1 Lesson 6 15:15, Lesson 7 16:10;
  Demo Day 15:15 (teams at 15:15, 15:23, 15:31, 15:39, scoring from 15:47), Post-MAP 16:10, final survey 16:20, close 16:25.
- The Day 1 trainer scheduled task (Demo 1.9) runs at 16:25; the pre-flight, demo backups and Day 2 callback say 16:25.
- Lesson plan, run of show, facilitator kit, decks and notes, day pages, class plan, README and survey payloads rebuilt from the kit.

## 2026-11-10 · Review round 1 fixes (Ahmad Maher, 9.3 / 10)

- Task 2.6 is now **Task 2.5** (numbering) and adds a failed-run test: the skill owner adds a fallback line to the scheduled prompt, the team runs on
  `mirqab-locked-test-file.pdf` (a new, password-locked sample file no run can read), and the run log must say Could not read with nothing guessed.
  New Day 2 slide 46, "When a step fails, the run says so", and a check on slide 47 (Day 2 is now 55 slides). Lesson plan, lab step, answer key,
  pre-flight and Packs updated.
- The Demo Day rubric has five criteria, 10 points each, 50 in total: task relevance, working functionality, source accuracy, human controls, test
  evidence. Day 2 slides 42 and 51 (was 49), the Demo Day timer slide, the Task 2.5 backup and key, the facilitator kit and the class plan.
  Working functionality full marks: saved on the Scheduled page and run on demand (the first 08:00 run comes after Demo Day).
- The Scheduled steps say "Click Scheduled in the left sidebar" (Day 1 slide 18, Day 2 slides 15 and 17, demos, prompt sheet, cheat sheet, lab),
  checked against support.claude.com article 13854387 on 10 Nov 2026.
- The Agent Card has all four boxes (input, instruction, output, when) in MAP question 5 option a, confidence item 2 (q_r2) and final survey q_5,
  in English and Arabic.
- Task 1.10 says what each messy file holds: one problem, such as a missing value or a different currency, and no conflicting values
  (all five files checked: none has two values that conflict).
- Numbering: demos run 1.0 to 1.9 and 2.1 to 2.6; tasks run 1.1 to 1.10 and 2.1 to 2.5 (no gaps).
- Independent audit (round 6, 8.9) fixes: the Drive approval setting the owner must allow for unattended moves (support.claude.com 10166901),
  Task 1.10 says the invoice file has two gaps, task notes say person or team, footer hints removed from two messy files, the Workflow
  tracker line runs only on new files, impact minutes come from the Clock tab, MAP q5 Arabic option shortened, hub lead sentence split.
- Audit round 7 (9.3) fixes: Task 1.10 Workflow track attaches the request list; remote-run wording; new c5chk numbers; lab and key fixes.
- Audit round 8: 9.8 / 10, PASS (no Blocking or Concerning). Four quick nits fixed after it.
- 23 sample files (one new; no published file name changed).

## 2026-11-09 · Shipped for review

- The three portal surveys (PRE, POST, final) checked against the kit and published; Ahmad Maher, Moudhi and Yousif invited to all three.
- Staff password set in Vercel by Aya; the site redeployed.
- Staff home fix: its links resolved at the site root and gave the 404 page. Kit REDIRECTS now send the root names of staff-only pages to
  `/staff/...` (the password still applies). The two "slides with speaker notes" links on the staff home still open the public decks: an
  engine bug, logged in `_source/PLUGIN-FEEDBACK.md`.

## 2026-11-08 · Rebuild on the coded-workshop-builder engine

- New plan from the instructor plan of 8 Nov: Day 1 builds each person's agent in Claude (Project, Drive connector, fixed-shape output, skill);
  Day 2 turns one agent per team into a Claude scheduled task, with department rules, a run log and Demo Day. n8n is a trainer demo.
- Day 1 opens with a 28-minute AI foundations lesson and a transfer map to ChatGPT, Microsoft 365 Copilot and Gemini.
- 2 decks (73 and 53 slides), 2 prompt sheets, 2 browser labs, cheat sheet, safe-use card, take-home guide, 22 fictional sample files.
- Staff pages: lesson plan, decks with notes, facilitator kit, runbooks, backups, answer keys, lab keys.
- CODED × RSM theme: RSM logo; fills `#007DB4`, accent `#4CB5E2`.
- MAP: 13 questions (Day 1 5, Day 2 4, 4 work scenarios); the 2 Nov portal drafts updated in place.
- QA round 1 fixes (fresh-agent audit): Demo 1.1, data-rule check, PO no. column, approval mode, Demo 2.3 and 2.5, Workflow keys, onboarding (KYC) task,
  trainer set-up facts, n8n build spec, per-person Google sign-in, five MAP items rewritten. Day 1 is now 69 slides.
- QA round 2 fixes: daily schedules for a Sunday-to-Thursday week, a Log folder with one run-log file per run, transfer slides in Lessons 4 and 6,
  connector scope, Inbox set-up steps, and eight MAP items rewritten as new work moments. Day 1 is now 71 slides.
- QA round 3 fixes: transfer practiced in Lesson 6 and Task 1.9, file names with date and time, Task 1.6 checks three named items by hand,
  a pre-built invoice skill for the 15:55 run, Demo 2.5 and Task 2.5 rerun through the Inbox, two more Day 2 checks, MAP q3, q8 and q12 rewritten.
  Day 1 is now 72 slides and Day 2 52.
- QA round 4 fixes: skill-owner accounts for Day 2, reruns that refill the Inbox, safe-use wording for your own task list, an event-trigger check
  (Day 2 is now 53 slides), and Inbox checks instead of second copies.
- QA round 5 (8.9, limit reached, not shipped): fixes for ChatGPT skills in the transfer map, what travels to Cowork, the Workflow tracker line,
  the Task 1.6 starter file, and an Agent Card check (Day 1 is now 73 slides).

## 2026-11-02 · First build (replaced)

- Older build code, n8n on Day 2, 10 sample files. Replaced in full on 8 Nov.
