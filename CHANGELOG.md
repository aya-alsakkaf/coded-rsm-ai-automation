# Changelog

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
