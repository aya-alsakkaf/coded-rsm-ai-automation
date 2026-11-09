# CLAUDE.md · coded-rsm-ai-automation

CODED × RSM Albazie · AI Innovation and Automation · Sun 15 and Mon 16 Nov 2026, 08:30-16:00, CODED Alsharekh.
Read this before you change anything in this repo.

## Rules

- The site is generated from the kit. Edit `_source/kit/` only, then run `bash _source/build/build.sh` (the validator must print `PROBLEMS: 0`).
  Never edit `_source/build/` (the engine) or `public/` by hand.
- Plain English for Gulf ESL readers, American spelling, no em dashes. Website and decks in English only; only the portal surveys are bilingual.
- Fictional data only: Mirqab & Co. and Abdali Foods. Never RSM's name on fake data, never real client data.
- Answers never on a public page. The MAP key lives in the portal description and under `/staff` only.
- Public pages never link to `/staff`. The staff password is set by the user in Vercel (`STAFF_PASSWORD`); never choose, ask for, store or print it.
- Only this program's surveys in the portal (folder `e07488c7-5525-403f-a2c6-f6db15ae710a`). Never edit, close or delete another program's surveys.
- Sample file names never change once published.

## Decisions

| Date | Decision | Why |
|---|---|---|
| 2026-11-08 | Handoff approved: "Approve, and show me the built site before shipping". The approval covers creating and updating the three survey drafts. | One approval (coded-workshop-builder 2b). |
| 2026-11-08 | Rebuilt in full on the coded-workshop-builder engine; the first build of 2 Nov (older code, n8n Day 2) is replaced. Same code and URL. | The plan changed on 3 to 8 Nov (Slack #pro-bd thread; instructor plan). |
| 2026-11-08 | Day 2 builds with Claude scheduled tasks (Cowork); n8n is one trainer demo. Moudhi confirms with Waqas (RSM). | Non-technical room; controllable, repeatable builds. |
| 2026-11-08 | The three portal drafts of 2 Nov are updated in place (PRE 763ba655, POST 775a002d, survey fb337765). | Avoid duplicate surveys for one cohort. |
| 2026-11-08 | Client mix: RSM logo from rsm.global (white wordmark version made for dark pages). Fills `#007DB4` (RSM blue `#0095D6` darkened 16% so white text reaches 4.57:1); accent text `#4CB5E2` (a tint of RSM blue); no secondary (RSM green `#13A538` would clash with green = right). | The engine needs 4.5:1 white on the primary. |
| 2026-11-08 | Hours 08:30-16:00 (Moudhi, cohort). With 16:30, the extra 30 minutes go to Task 1.6. | Open with RSM. |
| 2026-11-08 | AI foundations is 28 minutes, although past rooms asked for a short intro. | Aya's request: Claude may be new. |
| 2026-11-08 | Shared work (poll, task board, Agent Cards, votes, timings, next tasks) is one Google Sheet in the sandbox Drive. Nothing printed. | The site is static; Aya: everything digital. |
| 2026-11-08 | MAP: 13 items (Day 1 5, Day 2 4, 4 work scenarios). The engine groups by day, so the scenarios carry day 2 in the kit; the portal shows them as Part 3. | Professional room (surveys.md section 8). |
| 2026-11-08 | Product facts checked on 8 Nov 2026 against support.claude.com (Projects 9519177, skills 12512180, connectors 10166901, scheduled tasks 13854387). | coded-workshop-builder section 2. |
| 2026-11-08 | Repo must be private (it was public after the first build and held staff answer keys). | Answers never in a public repo. |
| 2026-11-08 | QA round 1 (fresh agent) fixes: Demo 1.1 shows WDS-20931, not a Task 1.2 problem; a data-rule check (Day 1: 69 slides); PO no. column in the invoice template; approval mode in the schedule steps; Demo 2.5 pastes the Assurance rules word for word; MAP q2, q4, q7, q9, q12 rewritten so no item repeats a deck check. Details in _source/QA-REPORT.md. | coded-workshop-qa loop. |
| 2026-11-08 | Drive sign-in: one CODED training Google account per participant (or per team), sent privately before Day 1. | No shared sign-in in the room. |
| 2026-11-08 | QA round 2 fixes: schedules run daily at 08:00 (Kuwait works Sunday to Thursday; weekend runs log No new files); each run saves runlog-[date].txt in a Log folder; transfer slides in Lessons 4 and 6 (Day 1: 71 slides); MAP q1, q2, q3, q7 to q11 rewritten as new work moments; q_safe uses the standard text. | coded-workshop-qa loop, round 2. |
| 2026-11-08 | Button names: the decks say "run it once on demand", because the help page does not name the button. The pre-flight checks the names. | Product facts from support.claude.com only. |
| 2026-11-08 | QA round 3 fixes: outcome 6 practiced (check after the Lesson 6 transfer slide, transfer line in Task 1.9); output and run-log files named YYYY-MM-DD-HHMM; Task 1.6 checks three named items by hand; mirqab-invoice-match built before Day 1 (Demo 1.9 saves -live); Demo 2.5 and Task 2.5 rerun through the Inbox; checks after c3t1 and c4t1 (Day 1: 72, Day 2: 52 slides); MAP q3, q8, q12 rewritten. | coded-workshop-qa loop, round 3. |
| 2026-11-08 | QA round 4 fixes: each team builds its scheduled task on the skill owner's account; finished-early reruns copy files into the Inbox again; your own task list with no client or firm names is green; Task 1.4 hint "at least two rows"; event-trigger check after c3cmp (Day 2: 53 slides); demo Inbox steps are checks, the pre-flight does the copies. | coded-workshop-qa loop, round 4. |
| 2026-11-08 | QA round 5: 8.9 / 10, FAIL (Content 6.5, Tasks 7.0). Five-round limit reached: not shipped. Round 5 findings fixed in the kit and validated, not re-audited; the decision to audit again or ship is Aya's. | coded-workshop-qa loop, section 3. |
