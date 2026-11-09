# QA report · coded-rsm-ai-automation

Audit: coded-workshop-qa, levels 1 to 8. Levels 1 to 4 run by the builder with the scripts (validate_site.py, qa.cjs pages, qa.cjs decks).
Levels 5 to 8 run by a fresh agent that did not see the build. Pass = 9.5 or more, no Blocking finding, no dimension under 9.0.

## Round 1 · 8 Nov 2026 · 6.8 / 10 · FAIL (four dimensions under 9.0)

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 2.25 |
| Tasks and demos | 10 | 1.5 |
| MAP tests | 10 | 4.75 |
| Final survey | 5 | 9.5 |
| Language and data safety | 10 | 7.5 |

Levels 1 to 4: validator PROBLEMS: 0 (after three fixes: slide b4pp ran 23 px into the progress bar; the Day 2 prompt sheet scrolled sideways at 390 px
because of a long lesson title; a Day 2 note repeated slide c1pp's text). qa.cjs pages: 0 problems (one "check by eye": the hub's gradient button
is readable). qa.cjs decks: 0 problems, 68 + 50 slides, every COPY button and timer works.

Findings from the fresh agent (levels 5 to 8), each with the fix made in the kit:

Blocking · none

Concerning
- OUTLINE "onboarding workflows" not covered · added a new-client KYC check to Dana's task list (Demo 1.3), the coordinator prompt line (Task 1.3, lab) and a board note.
- day-2 c2steps, Task 2.2, cheat sheet · the approval mode of the scheduled task was missing · added as a step everywhere, plus an unattended test in the pre-flight.
- facilitator kit · Team set-up facts missing · added: Plugins & skills policy toggles, Cowork on the web (beta, Chat and Cowork unified) or Claude Desktop, Create and edit files.
- day-2 c3pp (Demo 2.3) · claimed the run reports FSC-3390 in November · the trainer now checks the November ledger; the reco says so.
- day-1 b1t3 · the data rule had no check · new quick check b1chk0 (Day 1 is now 69 slides; the tools block gave 1 minute).
- day-1 b1demo, b1chk, prompt sheet · Demo 1.1 showed the SCC-0718 error before Task 1.2 · Demo 1.1 now shows WDS-20931 read as 2,240.000 (the other Wafra line).
- day-2 c4pp (Demo 2.5) · the rules were reworded · the three Assurance rules are pasted word for word; the review line is a separate instruction; routing is Flag.
- answer key Task 1.6 Workflow · 7 received, 3 partly (item 13 lacks the bank confirmations), 5 outstanding; Outstanding accepted for items 5 and 7; the status notes (47%, 67%) follow.
- answer key Task 1.6 Extraction · lease 1's renewal option expected; a lease 5 expiry flag accepted.
- Task 2.3 Workflow track · the request list moved to Processed · Workflow teams keep it in the skill and read the latest tracker in Outputs (setup and backup).
- Demo 2.4 fallback · named screenshots that do not exist · fallback now steps through the slide; n8n build spec added to the facilitator kit.
- Task 1.7 and facilitator kit · one shared Google sign-in · one CODED training Google account per participant (or team), sent privately.
- MAP q_9, q_7, q_4, q_12 · copied deck quick checks · rewritten as new work moments with new distractors (q_9: 50, 8, 15 runs, about 10.5 hours).
- MAP Arabic · the key was the longest option in 6 of 13 · now 2 of 13 (English 1 of 13).

Nits (all fixed): Demo 1.1 hint timing notes (b4task, c2task) aligned with the Say line; b2two total computed from data.py (13,308.625); wk47 status sheet
week to date and 67%; wk47 emails dated 15 and 16 Nov; c3story and c4story dated before the workshop; a PO no. column added to the invoice template (b4story);
c4pp routing as Flag; "run it once on demand" instead of "Run now"; Artifacts line on b1tour; messy lease moved to Abu Halifa as lease 7 (batch-2 lease is
lease 8); Task 1.4 deliverable no longer names the flags; SCC-0702 trap in the answer key; Task 1.1 key accepts extras; real extras for Tasks 2.2 and 2.3;
lease clause 6 always present; skepticism, labeled; four long sentences split; b3task2 title; MAP q_3 "Agreeing on"; MAP Part 2 Day 1 says the companies are
fictional; q_10 no longer calls Abdali Foods' ledger real; q_safe names Claude and RSM-approved tools; final survey description without nested brackets;
"A live run is stronger than slides."

## Round 2 · 8 Nov 2026 · 7.2 / 10 · FAIL (three dimensions under 9.0)

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 3.75 |
| Tasks and demos | 10 | 2.75 |
| MAP tests | 10 | 3.5 |
| Final survey | 5 | 9.75 |
| Language and data safety | 10 | 8.75 |

Levels 1 to 4: validator PROBLEMS: 0 (after one fix: a custom task title counted its words twice), qa.cjs pages 0, qa.cjs decks 0 (69 + 50 slides).
A second fresh agent re-derived all 13 MAP answers before reading the key (all match) and recomputed every number (all agree).

Concerning findings and the fix made in the kit:
- Google Drive connector scope · it reaches every file the signed-in account can open · cheat sheet, b5t1 and d17 now say to use an account that opens only the sandbox.
- Skill sharing · the Share button appears only after an owner turns on a sharing toggle · facilitator kit says Share with organization.
- "Weekdays" schedule · Kuwait works Sunday to Thursday · every schedule is daily at 08:00; weekend runs log No new files; the pre-flight checks the first weekend run.
- Run log location · the prompts never named it · each run saves runlog-[date].txt in a Log folder (prompts, rules file, c4t2, cheat sheet, Drive set-up).
- Transfer lines missing in Lessons 4 and 6 · new slides b4map and b6map (Day 1: 71 slides; 1 minute each from the demos).
- Task 1.2 public hint pointed to both planted errors · now "Check every row against both files: number, date and amount."
- Day 1 keys expected the 3 November posting · Day 1 now says "not in the October ledger: check cut-off".
- Demo 1.11 had no approval mode · added. Day 2 Demo 2.2 Inbox was empty · pre-flight copies the October files back; the demo task is paused after Day 1.
- Task 2.2 Inbox empty · first step copies the track pack into the team Inbox; a Packs folder holds the copies.
- MAP q_1, q_3, q_7, q_10, q_11 repeated deck checks or examples · rewritten as new work moments (letter date, bank statement task, a missing log file, sharing a skill with client details, an out-of-period invoice); q_2, q_8, q_9 reworked too. Right answer longest: English 0 of 13, Arabic 1 of 13.

Nits fixed: b5map before Task 1.8; Day 2 Lesson 3 lesson-plan order; story dates in one order; Cowork wording in the facilitator kit; BPK-4471 note and status; Task 1.7 files; real extras for Tasks 1.4, 1.6, 1.8, 2.2 and 2.3; lab step 3 wording; Task 2.6 inputs; Analysis batch-2 line; q_intro says 13 questions; q_safe uses the standard text; q_pace Arabic dual; split long prompt sentences (Demos 1.3, 1.5); recognize; "find where it fails".
Not changed: no quick check for b3t5 (scoring is practiced in Demo 1.5 and Task 1.5), so MAP q13 stays a new moment.

## Round 3 · 8 Nov 2026 · 8.2 / 10 · FAIL (three dimensions under 9.0)

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 5.25 |
| Tasks and demos | 10 | 3.25 |
| MAP tests | 10 | 7.75 |
| Final survey | 5 | 10 |
| Language and data safety | 10 | 10 |

Levels 1 to 4: validator PROBLEMS: 0 (29 pages), qa.cjs pages 0, qa.cjs decks 0 (71 + 50 slides, every COPY button and timer works).
The fresh agent re-derived all 13 MAP answers (all match the key) and recomputed every number (all agree except the c5chk feedback).

Concerning findings and the fix made in the kit:
- Outcome 6 (transfer) not practiced · a quick check after b6map (b6chk2) and a transfer line on the Agent Card in Task 1.9 (lab step too); Task 1.10 is 14 minutes.
- c5chk feedback · distractor "About 13 hours" (40 × 20 = 800 minutes); "About 7 hours" now says 700 is minutes, divide by 60.
- Daily time of day not on the help page · the pre-flight checks for a time field; if there is none, Create with Claude with the time stated (c2steps note, d22, t22 fallback).
- Task 1.6 "3 samples" did not exist · each track checks three named items by hand (leases 1, 4, 6; three accounts; items 5, 7, 8; the three engagements); the staff key lists the answers; Demo 1.6 compares three invoices; b4t2 says "three cases".
- Demo 1.11 depended on the live Demo 1.9 skill · mirqab-invoice-match is built and tested before Day 1; Demo 1.9 saves mirqab-invoice-match-live.
- Demo 2.5 showed SCC-0718 and had no inputs · the trainer copies batch 2 and the messy invoice from Packs into the Inbox and runs on demand; routing table and expected output follow.
- Task 2.5 rerun in a chat left no run log · teams copy the messy file into the Inbox and run on demand; "attached" removed.
- Same-day runs replaced each other · output and run-log files are named YYYY-MM-DD-HHMM (prompts, rules file, cheat sheet, c3t1, keys).
- MAP q_3 · distractors now each fail one tag (yearly checklist, choosing findings, a weekly call); the key is a weekly bank statement match.
- MAP q_12 · new invoices flagged each week; believable distractors (lower the limit, email the file to the team).

Nits fixed: settings path for Team (owner turns on code execution; participants check file creation); cheat sheet adds Set up manually; Lesson 2 minutes (Demo 1.3 slot 5, board review 3 at 10:17) and b4chk before Demo 1.6; quick checks after c3t1 and c4t1 (Day 2: 52 slides); handoff extras, opener time and Noura's day synced with the kit; c5story dated Thursday 5 November; Task 1.1 key lists the financial year end; d18 accepts 5 · 2 · 3; t23 checks the empty-folder line and the Analysis line comes first; t22 Save comes last; t25 extra adds a second department's rule; After Day 2 section pauses every scheduled task; MAP q_8 is a weekly status summary.

## Round 4 · 8 Nov 2026 · 8.6 / 10 · FAIL (three dimensions under 9.0)

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 9.75 |
| Pages | 10 | 10 |
| Decks | 15 | 9 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 7.5 |
| Tasks and demos | 10 | 5.25 |
| MAP tests | 10 | 10 |
| Final survey | 5 | 10 |
| Language and data safety | 10 | 7.75 |

Levels 1 to 4: validator PROBLEMS: 3 on the audited build (Concerning: b4task ran 25 px into the progress bar after Task 1.6 gained a step; Nit: the b7demo note repeated the new file name). qa.cjs pages 0, qa.cjs decks 0 (72 + 52 slides). Both fixed in the kit; the next build is validated again.
The fresh agent re-derived all 13 MAP answers (all match) and recomputed every number (all agree). MAP and the final survey had no finding.

Concerning findings and the fix made in the kit:
- Site older than the kit at audit time · the two validator fixes were made after the build; rebuilt and validated before round 5.
- Task 1.4 hint "two rows should not say Matched" · BPK-4471 may be Not found, so the hint (and the lab hint) says "at least two rows".
- Task 2.2 and Task 2.5 extras reran on an empty Inbox · each extra copies the files into the Inbox again first; Task 2.3's extra too.
- Whose account runs the team's task · each team works on the laptop of the person who made the team's skill; that person makes the Task 2.5 edits (shared skills cannot be edited by others); facilitator kit and c1pp note say so.
- Task 1.3 and 1.5 prompts vs the safe-use card · "your own task list, with no client or firm names" is green; both prompts say no client or firm names.
- Task 1.5 trainer line implied real files were fine · "Build it on the track pack: no real files today."

Nits fixed: Noura's Sunday in the lesson plan; the vote result is read before Demo 2.1 (c1pp note); c2t2 and c2chk no longer claim a run "remembers nothing" (do not rely on recall); CLASS-PLAN.md regenerated and no longer prints the MAP key; a quick check on event triggers after c3cmp (Day 2: 53 slides; Demo 2.4 13 minutes); Drive connected before Day 1 and Demo 1.7 only shows it; Demo 1.6's line naming the Task 1.2 rows is trainer-only; the Day 1 Inboxes hold only their own pack; MAP q_2 option d says "more stable".
Also fixed from my own run-order review: demo setup lines check the Inbox instead of copying files a second time (the pre-flight does the copies), so no run reads a duplicate; worked Projects for Task 1.6 hint 3 are built before Day 1; Task 1.9 attaches the whole pack.

## Round 5 · 8 Nov 2026 · 8.9 / 10 · FAIL (two dimensions under 9.0) · the five-round limit is reached: not shipped

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 6.5 |
| Tasks and demos | 10 | 7.0 |
| MAP tests | 10 | 9.5 |
| Final survey | 5 | 10 |
| Language and data safety | 10 | 9.5 |

Levels 1 to 4: validator PROBLEMS: 0, qa.cjs pages 0, qa.cjs decks 0 (72 + 53 slides, every COPY button and timer works).
The fresh agent's 13 MAP answers match the key (its derivation was not fully blind: it read the kit's MAP first; it says so).
No Blocking finding. Every number agrees; every Inbox state works end to end; no language or data-safety breach.

Findings (all fixed in the kit after the round, rebuilt and validated, but not re-audited by a fresh agent):
- Concerning · c1chk3 (and b6chk) marked "a Project" flatly wrong for scheduling; Cowork projects can hold recurring tasks · both checks now ask what travels to any chat, Cowork and a schedule.
- Concerning · transfer map Package row · ChatGPT now has skills (beta) · "Skill (beta) or custom GPT"; b6map, b6chk2 and the Task 1.9 key accept it.
- Concerning · Task 2.3 Workflow teams had no exact line · a COPY line for the tracker; the key shows the full tracker (10 · 1 · 4, 67%).
- Concerning · Task 1.6 linked the starter file (the finished five parts) at minute 0 · removed from the task; it stays as hint 3 and catch-up.
- Nits · knowledge vs rules wording (b3t4, cheat sheet, Demo 1.4); c4story now shows two rules in conflict; Agent Card check b3chk0 (Day 1: 73 slides); Task 1.2 18 minutes after its story; messy status 64 hours; batch-2 lease email covers all three 2026 leases; Task 2.6 Workflow runs start clean; Demo 1.1 also checks a letter date; Tasks 1.8 and 1.9 list the packs; b2two no longer names the planted rows; MAP q_6 option c and q_10 Arabic option a; two plainer sentences (hub, Day 2).

## Round 6 · 10 Nov 2026 · after review round 1 (Ahmad Maher, 9.3 / 10) · 8.9 / 10 · FAIL (two dimensions under 9.0)

Review round 1 fixes applied first: failed-run test in Task 2.5 (was 2.6) with `mirqab-locked-test-file.pdf` and a fallback slide (c5fail);
Demo Day rubric of five criteria, 50 points; "Click Scheduled in the left sidebar"; the Agent Card's four boxes in MAP q5a, q_r2 and final q_5;
Task 1.10 wording; demo and task numbering without gaps.

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 6.5 |
| Tasks and demos | 10 | 7.25 |
| MAP tests | 10 | 9.75 |
| Final survey | 5 | 10 |
| Language and data safety | 10 | 9.0 |

Levels 1 to 4: validator PROBLEMS: 0 after one fix (c5task ran 86 px into the progress bar: the Demo plan prompt moved to Demo 2.6, steps shortened);
qa.cjs pages and decks: 0 problems. MAP: the fresh agent re-derived all 13 answers from the slides before reading the key; all 13 match.

Blocking · none
Concerning · c5rubric, c6score, facilitator kit · "Working functionality" full marks needed a scheduled run, but the first 08:00 run is after Demo Day · 10 = saved on the Scheduled page, runs on demand, same shape (fixed)
Concerning · facilitator kit owner settings, pre-flight · Drive move, share and trash ask for approval before each action by default (support.claude.com 10166901); runs could not move files to Processed · owner lets members run them without asking; pre-flight checks no approval waits (fixed)
Concerning · c5fail · new concept with no demo and no check · notes show the pre-flight locked-file run log; new check c5chk2 (Day 2: 55 slides) (fixed)
Concerning · Task 1.10 · "one problem" but the invoice messy file has two · "a gap the agent must flag (the invoice file has two)" (fixed)
Nit · b1tour, c2t1, c2steps · "In Cowork" not named · kept: the reviewer's wording, matches article 13854387 (decision)
Nit · c5rubric, c6score, facilitator row · rubric typed by hand · built from CD.RUBRIC_FULL and RUBRIC_SCORE (fixed)
Nit · Task 2.5 key · how to score Test evidence if the trainer fallback was used · note added (fixed)
Nit · Task 2.5 hint and Impact prompt · minutes come from the Clock tab, not the run log · "run log or the Clock tab", bracketed Impact prompt (fixed)
Nit · two messy files · footers told the agent what to flag · footers removed (fixed)
Nit · Task 2.3 Workflow tracker line · ran before the empty-folder check · "If the Inbox has new files, first…" (fixed)
Nit · Day 2 lab step 6 · Workflow trackers line missing · added (fixed)
Nit · every task note · "Ask each pair" · kit notes say person (Day 1) or team (Day 2) (fixed)
Nit · Task 2.5 deliverable · four items · one deliverable (fixed)
Nit · MAP q5 option a (Arabic) · longest option · shortened to "ومتى" (fixed)
Nit · c5rubric · "Five questions" · "Five criteria" (fixed)
Nit · b1tour, c2steps · capital after the colon · lower case (fixed)
Nit · hub program lead · 31 words · split (fixed)
Nit · Task 1.10 and 2.3 hints · "Look for: Look for…" · hints reworded (fixed)

## Round 7 · 10 Nov 2026 · 9.3 / 10 (9.275) · FAIL (two dimensions under 9.0)

| Dimension | Weight | Score |
|---|---|---|
| Files, links and config | 10 | 10 |
| Pages | 10 | 10 |
| Decks | 15 | 10 |
| Interactivity | 10 | 10 |
| Content coherence | 20 | 8.0 |
| Tasks and demos | 10 | 7.75 |
| MAP tests | 10 | 9.25 |
| Final survey | 5 | 10 |
| Language and data safety | 10 | 9.75 |

Levels 1 to 4: validator PROBLEMS: 0 (Day 2: 55 slides); qa.cjs pages and decks: 0 problems. A new fresh agent re-derived all 13 MAP answers; all match.

Blocking · none
Concerning · c2t2, c2pp, cheat sheet · "runs in the cloud, laptop closed" stated for every case · re-checked article 13854387 today: tasks run remotely; tasks that need local files run only on the computer. Wording now says so (fixed)
Concerning · Task 1.10 Workflow track · the messy email had no request list to work from · attach mirqab-pbc-request-list-abdali.xlsx; key: items 8 and 11 Outstanding, "next week" has no date: flag it (fixed)
Nit · c5chk · repeated the c5stats example · new numbers: (30 − 6) × 25 = 600 minutes (fixed)
Nit · Day 2 lab step "Batch 2" · invoice-only check, no track lines · track lines and a per-track key (fixed)
Nit · Task 2.3 · request list "in the skill" never added · the skill owner adds it as a reference file (fixed)
Nit · score sheet · no middle case for Test evidence; trainer-account fallback · "Some of these runs logged"; fallback counts the same (fixed)
Nit · Task 1.1 key · access section · key says the access section covers records only (fixed)
Nit · Demo 1.1 note · no line for a correct live run · line added (fixed)
Nit · MAP q5 option a (Arabic) · bare "ومتى" · "ومتى يعمل", as in q_r2 and final q_5 (fixed)
Nit · day pages "Breaks at … and … and …" · engine string · logged in PLUGIN-FEEDBACK.md item 7
Nit · MAP q_intro · "13 questions", not "13 knowledge questions" · kept: 4 of the 13 are work scenarios (earlier decision)
Nit · MAP q_1 c and q_12 c · weak distractors · kept: the reviewer judged the wrong options believable; the tests are live
Nit · b1map note, b3tracks, b4t2 · source list, dummy-pack prompt, a check for "test three" · kept for now (pre-existing, no reviewer finding)
