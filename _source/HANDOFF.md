# Handoff · CODED × RSM Albazie · AI Innovation and Automation

> **Review round 1 (10 Nov 2026, Ahmad Maher) changes this handoff:** the Demo Day rubric is five criteria of 10 points, 50 in total (task relevance, working functionality, source accuracy, human controls, test evidence); Task 2.6 (now Task 2.5) adds a failed-run test with a fallback line; demos and tasks are renumbered without gaps (old Task 2.5 and 2.6 are 2.4 and 2.5; old Demos 1.3 to 1.9 and 1.11 are 1.2 to 1.9). Where this file says otherwise, CHANGELOG.md and the kit win.

Written 8 Nov 2026 from `_source/OUTLINE.md` (the instructor plan of 8 Nov and the outline sent to RSM). One approval covers everything below,
including creating and updating the three portal survey drafts.

## 1 · Summary

| Item | Value |
|---|---|
| Title | AI Innovation and Automation |
| Client | RSM Albazie (client workshop, CODED and RSM mixed theme) |
| Audience | 18 RSM Albazie staff: Assurance 12, Corporate Finance 2, Support 3 (project coordinators), Analytics Advisory 1. They use AI already; Claude may be new |
| Days and dates | 2 days · Sunday 15 and Monday 16 November 2026 |
| Daily times | 08:30 to 16:00 (5 h 30 min teaching, breaks about every hour, lunch with Dhuhr, Asr break) |
| Venue | CODED, Alsharekh classroom (Frontend Campus) |
| Tools | Claude: chat, Projects, the Google Drive connector, artifacts and files, skills, scheduled tasks. n8n: one instructor demo only |
| Trainer | Aya |
| Cohort | RSM-AI-Nov/Nov-26 (exists in the portal) |
| Fictional company | **Mirqab & Co.**, a fictional Kuwaiti audit and advisory firm, and its fictional audit client **Abdali Foods Co. K.S.C.C.** (two more fictional clients in the status sheets) |
| The habit | Claude does the first pass. You review and sign off. |
| Code and URL | `rsm-ai-automation` · https://coded-rsm-ai-automation.vercel.app · repo `aya-alsakkaf/coded-rsm-ai-automation` (exists, from the first build) |
| Closest past workshops | Alshaya AI in Workflow (client, Claude), AI Essentials in the Workplace (Claude, scheduled tasks), and the first RSM build of 2 Nov (names and file ideas) |
| Slides | Day 1: 73 · Day 2: 53 |
| Everything digital | Site pages, forms on the site, and one shared workshop board (a Google Sheet in the sandbox Drive). Nothing printed |

## 2 · Outcomes

1. I can explain what generative AI does well and where it can be wrong, and check its output against the source.
2. I can find the tasks in my work that suit an agent, and describe one as an Agent Card: input, instruction and output.
3. I can build a Claude Project with instructions and knowledge that gives the same, checkable result on every run.
4. I can connect an agent to a Drive folder and have it return its output in a fixed format.
5. I can package my method as a skill and run it on a schedule, with a human review step.
6. I can match each Claude feature to its equivalent in ChatGPT, Microsoft 365 Copilot and Gemini.

## 3 · Day by day

Numbering: Demo 1.N comes right before Task 1.N. Every task has minutes, solo or team, a file (or your own work with a Mirqab example),
a deliverable and a "Finished early?" extra. Struggle windows: struggle, unlock, fix.

### Day 1 · Sunday 15 November · Designing AI Agents for Real Work

**Claim:** One card, one Project, one agent you can trust.
**Integration moment:** each person's own agent: an Agent Card turned into a Project, fed from a Drive folder, returning a fixed-shape artifact, packaged as a skill.
**Hook for Day 2:** the empty **When** box. "Today your agent works when you open Claude. Tomorrow it runs without you."

| Time | Block | Min | What happens |
|---|---|---|---|
| 08:30-08:35 | Welcome and sign-in check | 5 | Laptops open claude.ai (CODED account) and the workshop site |
| 08:35-08:45 | Pre-MAP test | 10 | QR on the screen; phone only. Doubles as the pre-flight |
| 08:45-08:52 | Opener: one invoice, two requests | 7 | Demo 1.0, then outcomes and today's map |
| 08:52-09:20 | Lesson 1 · AI foundations | 28 | What AI is, why we need it, where it fails, the tools, the transfer map · Task 1.1 |
| 09:20-09:30 | Break | 10 | |
| 09:30-10:20 | Lesson 2 · Why chat isn't enough, and finding the work | 50 | Task 1.2 · Demo 1.3 · Task 1.3 · board review |
| 10:20-10:30 | Break | 10 | |
| 10:30-11:30 | Lesson 3 · Design the agent, then pick your case | 60 | Agent Card, Projects · Demo and Task 1.4 · Demo and Task 1.5 |
| 11:30-12:30 | Lunch and Dhuhr prayer (about 11:33) | 60 | Trainer groups the approved cards into 4 teams |
| 12:30-13:20 | Lesson 4 · Build: Instruction | 50 | Five-part instruction · Demo and Task 1.6 |
| 13:20-13:30 | Break | 10 | |
| 13:30-14:25 | Lesson 5 · Build: Input and Output | 55 | Connectors, artifacts · Demo and Task 1.7, Demo and Task 1.8 |
| 14:25-14:45 | Asr prayer and break (about 14:33) | 20 | |
| 14:45-15:30 | Lesson 6 · Build: Package | 45 | Skills · Demo and Task 1.9 · Task 1.10 |
| 15:30-15:40 | Break | 10 | |
| 15:40-16:00 | Lesson 7 · Show and tell, and the Day 2 hook | 20 | Team demos · Demo 1.11 · wrap |

Teaching minutes: 5 + 10 + 7 + 28 + 50 + 60 + 50 + 55 + 45 + 20 = 330.

**Opener (7 min).** Story: Sunday 1 November, 08:40. Dana, an associate at Mirqab & Co., opens a supplier invoice for Abdali Foods and types
"What's in this?". **Demo 1.0** (showcase, in the deck): the same invoice, a weak request and a five-part request (Role, Steps, Rules,
Format, When unsure). Weak: a paragraph that reads well and misses the invoice number. Strong: a one-row table with supplier, invoice number,
date and amount in KWD with three decimals, and "Not found" for the missing PO number. Then outcomes (1 min) and today's map (1 min).

**Lesson 1 · AI foundations (28 min):** poll and story 3 · how AI writes 5 · where it fails, Demo 1.1 4 · the data rule and a check 3 · the tools and the
transfer map 4 · quick check 1 · the Claude tour 1 · Task 1.1 7.
- Story: the live poll on the shared board ("Which AI tools did you use this month, and for what?"), read back on screen.
- Analogy → term: *a very well-read new joiner who drafts fast and has never seen this client's file* → **generative AI** (predicts likely
  next words). Next-word widget on an audit sentence ("The cut-off test for Abdali Foods shows the invoice was posted in ...").
- Analogy → term: *a confident first draft that no one has ticked yet* → **hallucination / where it fails**. **Demo 1.1** (in-slide):
  "Where it goes wrong": an AI answer that gives WDS-20931 as KWD 2,240.000 (the other Wafra line in the ledger) next to the invoice that says KWD 3,860.000. It does not show either Task 1.2 problem. Habit: tick it against the source.
- Term: **the data rule**: dummy files today; RSM's AI policy first; no client data in any tool RSM has not approved.
- Term: **three families of tools** (chat assistants; AI inside work apps; automation tools) and **the transfer map** (table below).
- Quick check: why a confident AI figure can be wrong.
- Claude tour (list slide): where chat, Projects, connectors, skills, artifacts and Scheduled live.
- **Task 1.1 · First Claude chat** (7 min, solo). File `abdali-engagement-letter-2026.docx`. Ask Claude: summarize it in 5 lines; list every
  date and deadline; name what a standard engagement letter includes that this one is missing. Check one answer against the letter.
  Deliverable: the three answers, one ticked. Planted: the letter has no section on management's responsibilities. Finished early: ask
  Claude which paragraph each date came from, and check two.

The transfer map (Lesson 1, the cheat sheet and every build lesson):

| Agent Card box | Claude (today) | ChatGPT | Microsoft 365 Copilot | Gemini |
|---|---|---|---|---|
| Instruction: saved rules and reference files | Project | Project or custom GPT | Agent (Agent Builder) or Notebook | Gem |
| Input: reach your files and email | Connectors | Apps (formerly connectors) | Work data in SharePoint, OneDrive and Outlook | Connected apps (Gmail, Drive, Docs) |
| Output: a file you can open and edit | Artifact or file | Canvas | Copilot Page | Canvas |
| Package: a reusable, shareable method | Skill | Skill (beta) or custom GPT | Agent | Gem |
| When: runs on its own | Scheduled task | Scheduled task | Scheduled prompt | Scheduled action |

**Lesson 2 · Why chat isn't enough, and finding the work (50 min):** story 2 · Task 1.2 18 · debrief with the two-chats display 5 · concepts and check 5 ·
agent-ready task, Demo 1.3 and a check 5 · Task 1.3 12 · board review 3.
- **Task 1.2 · Same task, 18 answers** (18 min after the 2-minute story slide: 7 solo work, 5 pairs compare, 6 on screen). Files `abdali-supplier-invoices-oct-2026.pdf`
  (5 invoices) and `abdali-purchase-ledger-oct-2026.xlsx`. Plain chat, own prompt, a reconciliation table. Story: Faisal, a supervisor,
  receives two tables for the same invoices: different columns, different totals, one mismatch missed. Deliverable: your table. Planted:
  SCC-0718 is KWD 1,248.500 on the invoice and KWD 1,284.500 in the ledger; FSC-3390 (27 October) is not in the October ledger (posted in
  November, a cut-off issue). Finished early: run the same prompt in a new chat and compare with your first table.
- Debrief: three contrasting tables on screen, then one prompt in two chats with two different answers.
- Analogy → term: *a recipe card versus "cook something nice"* → **repeatable**: one-off chat is not repeatable; a prompt is not a process. Quick check.
- Term: **an agent-ready task**: repeats weekly, has clear rules, document in and document out.
- **Demo 1.3** (in-slide table): Dana's task inventory with the three tags and her top 3.
- **Task 1.3 · Task inventory** (12 min, solo, your own work; Dana's inventory as the example). Template on the Day 1 lab page; role prompt
  cards on the site (preparers: "What do you rebuild on every engagement?"; reviewers: "What do you check every time you review?";
  coordinators: "What do you chase every week?"). Deliverable: 10 tasks tagged, the top 3, the strongest posted on the shared board under
  your department. Finished early: estimate the minutes per week for each of your top 3.
- Board review (3): the board on screen; tasks that repeat across departments; what the coordinators and Analytics Advisory do.

**Lesson 3 · Design the agent, then pick your case (60 min):** concepts 10 · Demo 1.4 5 · Task 1.4 20 · scoring and Demo 1.5 5 · Task 1.5 20.
- Story: Faisal: "Every associate follows the same audit program. Why does every AI table look different?"
- Analogy → term: *the audit program every associate follows* → **the Agent Card**: Input, Instruction, Output, and an empty When box. Scene slide.
- Term: **literal instructions**: Claude follows what is written, not what you meant. Quick check.
- Analogy → term: *a client file with the procedures already in it* → **a Claude Project** (instructions and knowledge used in every chat in it).
- Term: **knowledge versus input**: rules, templates and an example output go in the Project; the documents to process come with each run.
- **Demo 1.4 · From card to agent** (prompt player): the invoice Agent Card, box by box, becomes Project instructions.
- **Task 1.4 · Build the invoice agent with me** (20 min, solo, guided: 12 build, 4 rerun, 4 compare). Files: the invoice pack, the ledger and
  `mirqab-invoice-match-template.xlsx` (columns and one example row) as knowledge. Deliverable: a Project "Mirqab invoice match" and a
  rerun table that catches both mismatches. Finished early: run the same request in a second chat inside the Project and compare the two tables.
- Term: **scoring a use case**: how often, how long, how clear the rules, can it run on a schedule.
- **Demo 1.5** (in-slide table): Dana scores her three candidates.
- **Task 1.5 · Agent Card v1** (20 min, solo, your own work; Dana's card as the example): score your 3 candidates (5), pick one and place it in a
  track (2), write the card on the Day 1 lab page (8), paste it to the board for approval (5; the rest are approved in the first 5 minutes of
  Lesson 4). Deliverable: an approved Agent Card v1. Finished early: write a second card for your runner-up task.

| Track | Starting example (fictional Abdali Foods files) | Pack |
|---|---|---|
| Extraction | Lease agreements → key-terms schedule | `abdali-lease-agreements.pdf` (6 leases, 2 unusual clauses) |
| Analysis | Two-year trial balance → movements over the threshold, with questions for the client | `abdali-trial-balance-fy2024-fy2025.xlsx` (threshold: over 10% and over KWD 5,000) |
| Workflow | Document request list and client emails → status tracker and follow-up drafts | `mirqab-pbc-request-list-abdali.xlsx` (15 items) and `abdali-client-emails-nov-2026.docx` (10 emails) |
| Reporting | Engagement status sheets → one weekly summary for a manager | `mirqab-engagement-status-wk46.xlsx` (3 engagements) |

A participant whose task fits no track asks Claude for a dummy pack with 2 planted errors (10-minute cap).

**Lesson 4 · Build: Instruction (50 min):** late approvals and story 5 · concepts and check 5 · Demo 1.6 4 · transfer 1 · Task 1.6 35.
- Story: Faisal reviews Dana's first agent: it skipped the "Not found" rule.
- Terms: **the five-part instruction** (Role, Steps, Rules, Output format, When unsure); **an example output as knowledge**; **test before you
  trust** (3 cases where you know the answer). Quick check (before the demo).
- **Demo 1.6 · From card to instructions** (prompt player): Dana's card becomes five-part instructions plus one example output.
- **Task 1.6 · Build v1** (35 min, solo: struggle 20, unlock 8, fix 7). Your track pack. First check 3 items by hand (Extraction leases 1, 4, 6;
  Analysis Trade receivables, Accrued expenses, Bank charges; Workflow items 5, 7, 8; Reporting the 3 engagements). Deliverable: your own Project, right on those 3 items.
  Hints in order: reread your Instruction box; use the five-part template; open the worked Project for your track (trainer shares it).
  Finished early: add a second example output to the knowledge, run again and check the same three items.
- Transfer slide (instructions in ChatGPT, Copilot and Gemini).

**Lesson 5 · Build: Input and Output (55 min).** Part A 25: story 2 · concepts 3 · Demo 1.7 5 · Task 1.7 15. Part B 30: concepts and check 5 · Demo 1.8 5 · Task 1.8 20.
- Story: Noura, a project coordinator, downloads and drags the same files into Claude every Sunday.
- Analogy → term: *a key to one cabinet, not the whole archive* → **a connector** (Google Drive). **The sandbox**: a CODED-owned Drive with one
  folder per track; no client data.
- **Demo 1.7 · Read from the folder** (prompt player): show the Google Drive connector (connected before Day 1), then "process the newest pack in 01 Invoices".
- **Task 1.7 · Run from the folder** (15 min, solo: struggle 10, unlock 3, fix 2). Deliverable: one run that reads from your track folder.
  Finished early: ask the agent which files it did not read, and why.
- Analogy → term: *the firm's working-paper template* → **an artifact or file** with a **fixed output shape**. Quick check.
- **Demo 1.8 · Same shape every run** (prompt player): the invoice tracker, rerun, same columns.
- **Task 1.8 · Fixed-shape output** (20 min, solo: struggle 12, unlock 4, fix 4). Deliverable: an artifact or Excel file in the same shape on two
  runs. Finished early: run it on your track's messy file and check that the shape holds.
- Transfer slide (connectors and artifacts in ChatGPT, Copilot and Gemini).

**Lesson 6 · Build: Package (45 min):** story and concepts 5 · Demo 1.9 4 · transfer and check 2 · Task 1.9 20 · Task 1.10 14.
- Analogy → term: *the firm's methodology manual, not one person's notes* → **a skill** (a saved method Claude loads when the task matches;
  it can be shared and called by a scheduled task). Project or skill: a table. Quick check.
- **Demo 1.9 · From Project to skill** (prompt player): ask Claude to turn the invoice Project into a skill; save it as mirqab-invoice-match-live
  (the pre-built mirqab-invoice-match runs the 15:55 task); run it in a fresh chat.
- Transfer slide (a packaged method in ChatGPT, Copilot and Gemini) and a quick check.
- **Task 1.9 · Make your skill** (20 min, solo). Deliverable: your skill, saved and tested in a fresh chat, and one line on your card saying where
  it would live in ChatGPT, Copilot or Gemini. Finished early: share it with a team member.
- **Task 1.10 · The messy sample and the clock** (14 min, solo). The messy file for your track (a missing field or an odd format). The agent
  must flag, not guess. Then log the minutes by hand and with the agent on the board. Deliverable: one flagged messy run and two numbers.
  Finished early: add the fix as a rule to your skill and rerun.

**Lesson 7 · Show and tell, and the Day 2 hook (20 min):** team demos 12 · Demo 1.11 5 · wrap and vote 3.
- Team demos: 4 teams (formed at lunch), 90 seconds each person: the card and a live run on one file from their pack.
- **Demo 1.11 · The agent that ran itself**: the trainer's invoice skill, scheduled at 08:00 in Cowork to run daily at 15:55, delivers its file
  to the Outputs folder while the room watches.
- Wrap, the empty When box, and each team votes on the board for the agent to automate tomorrow (vote closes at 08:40 on Day 2).

### Day 2 · Monday 16 November · Turning Agents into Operational Workflows

**Claim:** An agent that waits for you is a tool. An agent that runs on time, with a review step, is a workflow.
**Integration moment:** each team's scheduled workflow, running on new files, with department rules, a review step and a run log, shown at Demo Day.

| Time | Block | Min | What happens |
|---|---|---|---|
| 08:30-09:20 | Lesson 1 · From agent to system | 50 | Callback quiz · trigger, steps, output, review · Demo and Task 2.1 |
| 09:20-09:30 | Break | 10 | |
| 09:30-10:20 | Lesson 2 · Make it run on its own | 50 | Scheduled tasks · Demo and Task 2.2 |
| 10:20-10:30 | Break | 10 | |
| 10:30-11:30 | Lesson 3 · New inputs, outputs and n8n | 60 | Demo and Task 2.3 · Demo 2.4 (n8n) |
| 11:30-12:30 | Lunch and Dhuhr prayer (about 11:33) | 60 | |
| 12:30-13:20 | Lesson 4 · Fit it to your department | 50 | Rules, review step, run log · Demo and Task 2.5 |
| 13:20-13:30 | Break | 10 | |
| 13:30-14:25 | Lesson 5 · Test and prepare the demo | 55 | Impact, the judges' rubric · Demo and Task 2.6 |
| 14:25-14:45 | Asr prayer and break (about 14:33) | 20 | |
| 14:45-15:30 | Lesson 6 · Demo Day | 45 | 4 teams × 8 minutes, scoring |
| 15:30-15:40 | Break | 10 | |
| 15:40-15:50 | Post-MAP test | 10 | QR on the screen |
| 15:50-15:55 | Final survey | 5 | Second QR |
| 15:55-16:00 | Next steps and close | 5 | Post your next task on the board |

Teaching minutes: 50 + 50 + 60 + 50 + 55 + 45 + 10 + 5 + 5 = 330.

**Lesson 1 · From agent to system (50 min):** callback and 3 checks 8 · story 2 · concepts and check 8 · vote result 2 · Demo 2.1 5 · Task 2.1 20 · share-back 5.
- Callback: yesterday's skill and the 15:55 run. Three quick checks on Day 1.
- Story: Faisal: "Your agent is good. Who runs it when you are on leave?"
- Analogy → term: *a standing instruction to the bank* → **trigger** (time or event), **steps**, **output**, **human review**. Scene slide. Quick check.
- **Demo 2.1 · The invoice workflow card** (prompt player): When → Input → Skill → Output → Who reviews.
- **Task 2.1 · Workflow card** (20 min, team; the team's chosen agent; the invoice card as the example). Deliverable: the workflow card on the
  board. Finished early: write the one-line format for your run log.

**Lesson 2 · Make it run on its own (50 min):** story 2 · concepts and steps 5 · check 1 · Demo 2.2 5 · Task 2.2 30 · transfer and buffer 7.
- Analogy → term: *a calendar reminder that also does the work* → **a scheduled task** (Cowork: Scheduled → New task; daily, weekdays, weekly,
  hourly or manual; runs in the cloud; uses connectors and skills).
- **Demo 2.2 · Schedule the invoice workflow** (prompt player): daily at 08:00, the prompt calls the skill, reads 01 Invoices / Inbox, saves to Outputs, moves files to Processed, saves a run-log file in Log.
- **Task 2.2 · Schedule your workflow** (30 min, team: struggle 18, unlock 6, fix 6). Deliverable: a scheduled task, run once now, output
  checked against the Day 1 result. The team works on the laptop of the person who made the team's skill. Finished early: add your team name to the output file name, copy the pack in again and run once more.
- Transfer slide: scheduled tasks in ChatGPT, scheduled prompts in Copilot, scheduled actions in Gemini; n8n and Power Automate for events.

**Lesson 3 · New inputs, outputs and n8n (60 min):** story 2 · concepts and two checks 8 · Demo 2.3 5 · Task 2.3 25 · when n8n 5 · Demo 2.4 13 · comparison and check 2.
- Terms: **changing inputs** (process the Inbox, move each file to Processed), **delivered output** (a file in Outputs named with the date and time, or an email draft), **the empty-folder rule** ("No new files" in the run log, then stop).
- **Demo 2.3 · New files, then no files** (prompt player): drop batch 2, run, then run on an empty Inbox.
- **Task 2.3 · Batch 2 and the empty folder** (25 min, team). Files: the batch-2 file for your track. Deliverable: one run on batch 2 and one
  empty-folder run, each with its own run-log file. Finished early: copy the batch-2 file in again, write the count of files read as the first line of the output and check it against the run log.
- **Demo 2.4 · The n8n flow** (instructor only, built and tested in advance): a new email arrives → Claude reads it → the result is filed.
  Shown as the next step for event triggers and company-owned systems. Teams do not build in n8n. Then the comparison table and a quick check (which tool fits an event).

**Lesson 4 · Fit it to your department (50 min):** story 2 · concepts and two checks 8 · Demo 2.5 5 · Task 2.5 30 · buffer 5.
- Terms: **department rules** (thresholds, sign-off levels, file names), **the review step** (drafts only; a person approves), **the run log** (what ran, when, what it found).
- **Demo 2.5 · Flag for supervisor review** (prompt player): the three Assurance rules, word for word (including "differences over KWD 100 go to
  the supervisor"), then a run on demand on batch 2 and the messy invoice, copied into the Inbox.
- **Task 2.5 · Your department's rules** (30 min, team). File `mirqab-review-rules.docx`. Deliverable: 2 rules and a review step added, tested
  on the Day 1 messy file copied into the team's Inbox and run on demand; the skill owner makes the edits. Finished early: add one rule from a second department, copy the messy file in again and run again.

**Lesson 5 · Test and prepare the demo (55 min):** story 2 · impact 3 · rubric 3 · demo script 2 · Demo 2.6 3 · Task 2.6 40 · buffer 2.
- **Impact:** (minutes by hand − minutes with the agent) × runs per month = minutes saved.
- **The judges' rubric** (30 points): problem relevance 10, solution quality 10, deployment potential 10.
- **Demo 2.6 · A two-minute demo** (in-slide): the problem, the card, a live run, the impact, what comes next.
- **Task 2.6 · Three clean runs and the script** (40 min, team: runs 15, impact 5, script and rehearsal 20). Deliverable: 3 clean runs in the
  run log, the impact numbers and a 5-minute demo plan. Finished early: list the next two tasks to automate.

**Lesson 6 · Demo Day (45 min).** 4 teams × 8 minutes (5 demo, 3 questions) = 32; changeovers and scoring 8; panel comments 5. The trainer scores
each automation on the rubric. If RSM leadership attends, they judge with the trainer.

**Post-MAP, survey, close (20 min).** Post-MAP 10 · final survey 5 · each person posts the next task and the tool they will use 5.

## 4 · Sample files (all fictional, made for training)

| File | Contents | Used by |
|---|---|---|
| `abdali-engagement-letter-2026.docx` | Engagement letter, FY2026 audit; no section on management's responsibilities (planted) | Task 1.1 |
| `abdali-supplier-invoices-oct-2026.pdf` | 5 supplier invoices, October 2026 | Demo 1.0, Tasks 1.2, 1.4, Demos 1.4 to 1.9 |
| `abdali-purchase-ledger-oct-2026.xlsx` | October purchase ledger, 12 lines; SCC-0718 posted at 1,284.500 (invoice 1,248.500); FSC-3390 missing (posted 3 Nov) | Tasks 1.2, 1.4 |
| `mirqab-invoice-match-template.xlsx` | The output template: columns and one example row | Task 1.4 (knowledge) |
| `abdali-lease-agreements.pdf` | 6 short leases; lease 4 has a 3-month rent-free period, lease 6 lets the landlord end it with 60 days' notice | Extraction track |
| `abdali-trial-balance-fy2024-fy2025.xlsx` | Two-year trial balance, 24 accounts; 4 movements over the threshold, one of them a reclassification | Analysis track |
| `mirqab-pbc-request-list-abdali.xlsx` | 15 requested items with due dates | Workflow track |
| `abdali-client-emails-nov-2026.docx` | 10 client emails; one says "attached" with no attachment, one sends the wrong period | Workflow track |
| `mirqab-engagement-status-wk46.xlsx` | 3 engagements (Abdali Foods, Khiran Logistics, Jabriya Medical Supplies): hours, budget, open items, deadlines; one 18% over budget | Reporting track |
| `abdali-invoice-messy.pdf` | An invoice in USD with no invoice number | Task 1.10 (invoice) |
| `abdali-lease-messy.pdf` | A lease with no end date | Task 1.10 (extraction) |
| `abdali-trial-balance-messy.xlsx` | A trial balance with one account missing its prior-year figure | Task 1.10 (analysis) |
| `abdali-client-email-messy.docx` | An email that answers two request items in one line | Task 1.10 (workflow) |
| `mirqab-engagement-status-messy.xlsx` | A status sheet with a blank budget cell | Task 1.10 (reporting) |
| `mirqab-starter-instructions.docx` | Catch-up: a five-part starter instruction for each track | Anyone who missed Day 1 |
| `mirqab-review-rules.docx` | Department rules: thresholds, sign-off levels, file names, "drafts only" | Task 2.5 |
| `abdali-supplier-invoices-nov-wk1.pdf` | Batch 2: 3 invoices, one in USD | Task 2.3 (invoice) |
| `abdali-purchase-ledger-nov-wk1.xlsx` | Batch 2 ledger | Task 2.3 (invoice) |
| `abdali-lease-agreement-new.pdf` | Batch 2: one new lease | Task 2.3 (extraction) |
| `abdali-management-accounts-oct-2026.xlsx` | Batch 2: October against September, month to date | Task 2.3 (analysis) |
| `abdali-client-emails-wk47.docx` | Batch 2: 5 new client emails | Task 2.3 (workflow) |
| `mirqab-engagement-status-wk47.xlsx` | Batch 2: the next week's status | Task 2.3 (reporting) |

The sandbox Drive mirrors these files: `Mirqab sandbox / 01 Invoices · 02 Leases · 03 Trial balance · 04 Requests · 05 Status`, each with
`Inbox`, `Processed`, `Outputs` and `Log`, plus one folder per team on Day 2 and a `Packs` folder with copies of every pack.

## 5 · Take-aways

- **Cheat sheet:** 1 the Agent Card; 2 the five-part instruction; 3 build it in Claude (Project, connector, artifact, skill, scheduled task, with menu paths); 4 the transfer map; 5 run rules (Processed folder, empty folder, drafts only, run log, owner).
- **Safe-use card:** green (Mirqab dummy files, public information, your own drafting, your own task list with no client or firm names); amber (RSM internal, non-client documents, only in an RSM-approved account, names removed); red (client ledgers, KYC documents, client names, financial statements, personal data: never in any AI tool RSM has not approved). RSM's AI policy comes first.
- **Take-home guide:** first week (one Agent Card for your top task, built on dummy data in an RSM-approved tool); first month (run it weekly, log the minutes, share the skill); in any tool (use the transfer map).

## 6 · Assessment

**MAP (PRE Day 1 08:35, POST Day 2 15:40; same questions; not graded; 10 minutes).**
Part 1: 6 confidence items (the outcomes in section 2). Part 2: Day 1 (5), Day 2 (4). Part 3: Work scenarios (4).

| # | Question | a | b | c | d | Key | Taught in |
|---|---|---|---|---|---|---|---|
| 1 | Claude summarizes the engagement letter and gives the report date as 31 March 2026. The letter says 31 March 2027. What do you do next? | Fix it from the letter and check every other date | Ask Claude to try again until the year looks right | Keep it: the day and month are right, the year is minor | Stop using Claude to summarize engagement letters | a | D1 L1 |
| 2 | Every month, three coordinators turn the same client emails into a request tracker, each in their own chat. Their trackers never look the same. What fixes this best? | Each coordinator writes a longer, more detailed prompt | Ask Claude to be careful and check its work twice | Save the rules and an example output in a Project | Use a different AI tool that gives more stable answers | c | D1 L2, L3 |
| 3 | Which task is the best first agent for an audit team? | Filling in the client-acceptance checklist once a year | Choosing each week which findings to raise with the client | Joining the weekly progress call with the client's finance team | Matching each week's bank statement to the cash book | d | D1 L2, L3 |
| 4 | Your invoice agent lives in a Claude Project. Your supervisor adds a rule: "Flag any difference over KWD 100." Where does the rule go? | In the files you attach to each month's run | In the chat, typed again at the start of each run | In the Rules part of the agent's instructions | In the output file name, so the reviewer sees it | c | D1 L3, L4 |
| 5 | Your firm later moves to Microsoft 365 Copilot. What carries over from today? | The Agent Card: input, instruction and output | Nothing, because every AI tool works differently | Only the exact prompts, copied word for word | Only the sample files and the output template | a | D1 L1, transfer lines |
| 6 | Your agent works only when you open Claude and attach files. What lets it run each morning without you? | A longer prompt that tells Claude to remember the task | A skill, a connected input folder and a scheduled task | A rule in the Project that says run every morning | Sharing the Project with a colleague who presses Send | b | D2 L1, L2 |
| 7 | On Thursday, the reviewer opens the Log folder. There is a run-log file for every day this week except Monday. What should the reviewer conclude? | Monday had no new files, so the run had nothing to log | The Monday run failed or did not start: check it | Claude probably merged Monday's log into Tuesday's file | Nothing: one missing log file in a week is normal | b | D2 L3, L4 |
| 8 | Your workflow writes the weekly status summary for your manager every Thursday at 08:00. Where does the human review step belong? | Before the trigger, so nothing starts without approval | Only at year end, when the audit file is signed | Nowhere, once the agent has passed three tests | After the output, before anyone sends or relies on it | d | D2 L1, L4 |
| 9 | Task A takes 50 minutes by hand and 8 with the agent, 15 times a month. Task B takes 20 minutes by hand and 5 with the agent, 40 times a month. Which saves more time each month? | Task B, about 10 hours a month | Both save exactly the same time | Task A, about 10.5 hours a month | Task B, because it runs more often | c | D2 L5 |
| 10 | A colleague wants to share his invoice skill with the whole team. Its instructions name a real client and quote two of its invoice amounts. What should he do first? | Remove the client details and test it on dummy data | Share it, since only colleagues can open the skill | Share it, and ask the team not to copy the amounts | Rename the skill so the client's name is not visible | a | D1 L1, safe-use card |
| 11 | Your invoice agent passed three tests. Next month, an invoice dated in December arrives in the November pack, and the agent marks it Matched. What is the best next step? | Accept it, because the amount matches the ledger | Take December invoices out of the folder by hand | Ask Claude in the same chat if the date is fine | Add a rule to flag out-of-period dates; retest | d | D1 L4, L6; D2 L4 |
| 12 | Each week, your team's scheduled task flags a few new invoices as "Amount differs". A month later, nobody has acted on any of the flags. What fixes this? | Lower the KWD limit so the task flags more invoices | Name a reviewer who reads each run and signs off | Delete the flag rule, since nobody acts on it | Email the output file to the whole team each morning | b | D2 L1, L4 |
| 13 | A supervisor asks which of your team's four agents to automate first. Which is the best choice? | The one with the most steps and the longest instruction | The one that runs often and has clear, checkable rules | The newest one, because it uses the latest features | The one built by the most senior member of the team | b | D1 L3; D2 L1 |

**Answer key: 1 a · 2 c · 3 d · 4 c · 5 a · 6 b · 7 b · 8 d · 9 c · 10 a · 11 d · 12 b · 13 b** (a 3, b 4, c 3, d 3; the key is the single longest option in 0 of 13 questions in English and 1 of 13 in Arabic).

**Scored automation:** each team's Demo Day automation, 30 points (problem relevance 10, solution quality 10, deployment potential 10), scored by the trainer (joint panel if RSM attends).

**Final survey:** the full client form (section 9 of the standard), "program" wording, hands-on items "the Agent Card, building your own agent in Claude, the scheduled workflow and Demo Day", tools "Claude and the sandbox Drive", can-do items from the outcomes, `q_ai` and `q_safe` for Claude.

## 7 · Trainer material (`/staff`, password)

Lesson plan (both days with minutes); decks with notes; facilitator kit (pre-flight, room, accounts, sandbox Drive set-up, the shared board,
the 15:55 scheduled task, the n8n demo, Demo Day running order and score sheet, fail plan); per day: runbook, backup results for every live
step, answer key (tasks, quick checks; MAP key on Day 2), lab key.

## 8 · Coverage

| Outline item | Day and block | Task |
|---|---|---|
| Reframing Work: repetitive tasks across audit and onboarding | D1 L2 | 1.2, 1.3 |
| Agent Design Framework: input, instruction, output | D1 L3, L4 | 1.4, 1.6 |
| Use Case Selection: analysis, extraction, workflow, reporting | D1 L3 | 1.5 |
| Build (Using Claude): a working agent | D1 L4 to L6 | 1.6 to 1.10 |
| From Agent → System: triggers, workflows, integrations | D2 L1, L3 (n8n demo) | 2.1 |
| Workflow Build: input → AI → output | D2 L2, L3 | 2.2, 2.3 |
| Customization: department-specific needs | D2 L4 | 2.5 |
| Demo & Next Steps | D2 L5, L6, close | 2.6, Demo Day |
| Promised: pre and post assessment, results report | D1 08:35, D2 15:40 | MAP |
| Promised: instructor scores each automation | D2 L6 | rubric |
| Instructor plan: AI foundations and transferable skills (outcome 6) | D1 L1; transfer slides in D1 L4 to L6 and D2 L2; a quick check after D1 L6 | 1.1, 1.9 (the transfer line on the card) |

## 9 · Decisions

1. **Source.** Built from the instructor plan (8 Nov), which keeps the outline sent to RSM in order. The Day 2 build uses Claude scheduled tasks; n8n is one instructor demo. Moudhi is confirming this with Waqas.
2. **Rebuild in the same repo.** The first build (2 Nov, older code, n8n plan) is replaced in full by the current engine, same code `rsm-ai-automation`, same URL.
3. **Repo visibility.** The repo is public and holds the first build's staff answer keys. It must be private (you change it once on GitHub).
4. **Surveys.** The three portal drafts from 2 Nov (folder `e07488c7`) are updated in place, not duplicated. The approval covers creating and updating them.
5. **Fictional names** from the first build: Mirqab & Co., Abdali Foods Co. K.S.C.C., Khiran Logistics, Jabriya Medical Supplies.
6. **Hours** 08:30 to 16:00 (Moudhi and the cohort). The proposal's 16:30 stays open; with 16:30, the extra 30 minutes go to Task 1.6.
7. **AI foundations stays at 28 minutes** although past rooms asked for a short intro: your request, because Claude may be new.
8. **Shared work** (poll, task board, Agent Cards, votes, timings, next tasks) lives in one Google Sheet in the sandbox Drive, linked from the site, because the site is static and cannot store shared answers. Personal notes on the lab pages stay in each browser.
9. **Tracks** follow the outline's four types, re-skinned to audit work; the board in Lesson 2 can replace the starting examples.
10. **MAP:** 13 items (Day 1 5, Day 2 4, Part 3 scenarios 4) because the room is professional; still 10 minutes.
11. **Demo Day** is scored by the trainer; a joint panel and an award only if RSM confirms (open with Moudhi).
12. **Product facts checked today** (8 Nov 2026), all from the vendor help pages:
    - Scheduled tasks run in Cowork: Scheduled → New task (or "Create with Claude"); hourly, daily, weekly, weekdays or manual; they run in the cloud when the computer is asleep; they use connectors and skills; Team plans: Cowork on the web is in beta and an admin turns it on. [Help Center](https://support.claude.com/en/articles/13854387)
    - Skills: Customize → Skills; "Code execution and file creation" (Create and edit files) must be on; Team plans share a skill from its ⋯ menu → Share; Claude can create a skill in a conversation. [Help Center](https://support.claude.com/en/articles/12512180), [Academy](https://academy.claude.com/tutorials/how-to-create-a-skill-with-claude-through-conversation)
    - Connectors: Customize → Connectors; on Team plans an owner enables Google Workspace first; Claude can read and move Drive files and save files to Drive; Drive files can be added to private Projects only. [Help Center](https://support.claude.com/en/articles/10166901)
    - Projects: + New Project, Set project instructions, knowledge with +; all plans. [Help Center](https://support.claude.com/en/articles/9519177)
    - Transfer map sources: ChatGPT scheduled tasks and apps ([PortEden, June 2026](https://porteden.com/blog/chatgpt-scheduled-tasks-tools/)); Copilot scheduled prompts for agents ([roadmap RM531759](https://mc.merill.net/message/RM531759)); Gemini scheduled actions ([TechRadar](https://www.techradar.com/computing/artificial-intelligence/geminis-new-scheduled-actions-feature-puts-catching-up-with-chatgpt-on-its-dayplanner)).
13. **Prayer times** for 15 November: Dhuhr 11:33, Asr 14:33 ([TrueCalendar](https://truecalendar.com/prayer-times/kuwait/kuwait-city/2026-11-15)).
14. **No PDFs of the take-aways and no videos** (not asked for).
15. **Website and decks in English only**; only the portal surveys are bilingual.
16. **Changes after QA round 1 (8 Nov):** Demo 1.1 no longer shows a Task 1.2 problem; a quick check follows the data rule (Day 1: 69 slides); the invoice template has a PO no. column; the scheduled-task steps include the approval mode; Demo 2.5 pastes the Assurance rules word for word and flags (none goes to the supervisor); Demo 2.3 leaves the FSC-3390 cut-off check to the trainer; Workflow teams keep the request list in the skill; Dana's list adds a new-client KYC check (onboarding); the PBC key is 7 received, 3 partly, 5 outstanding; the messy lease is lease 7 (Abu Halifa) and the batch-2 lease is lease 8; MAP items 2, 4, 7, 9 and 12 are new work moments, so no MAP item repeats a slide's quick check.
17. **Drive sign-in:** one CODED training Google account per participant (or per team), sent privately before Day 1. Never a shared sign-in on a slide, the site or the board.
18. **Changes after QA round 2 (8 Nov):** schedules run daily at 08:00 (Kuwait works Sunday to Thursday; weekend runs log No new files); each run saves a run-log file in a Log folder; the connector reaches every file the signed-in account can open, so the account opens only the sandbox; transfer slides in Lessons 4 and 6 (Day 1: 71 slides); Task 1.2's hint no longer points to the errors; Day 1 keys say "not in the October ledger" (no November date); Demo 1.11 and Task 2.2 steps include the approval mode and copying the pack into the Inbox; MAP items 1, 2, 3, 7, 8, 9, 10 and 11 are new work moments, so no item repeats a deck check; q_safe uses the standard text. Scoring a use case (b3t5) is practiced in Demo 1.5 and Task 1.5, not in a quick check, so MAP q13 stays a new moment.

19. **Changes after QA round 3 (8 Nov):** outcome 6 is practiced (a quick check after the Lesson 6 transfer slide and a transfer line on the card in Task 1.9; Task 1.10 is 14 minutes); quick checks on changing inputs and on department rules (Day 1: 72 slides, Day 2: 52); output and run-log files are named with the date and time (YYYY-MM-DD-HHMM), so runs on the same day never replace each other; Task 1.6 checks three named items by hand instead of "3 samples"; Task 1.8 runs twice on the pack; mirqab-invoice-match is built before Day 1 and Demo 1.9 saves its live copy as mirqab-invoice-match-live; Demo 2.5 and Task 2.5 copy their inputs into the Inbox and run on demand, so every rerun has a run-log file; the pre-flight checks for a time field on Daily (else Create with Claude) and that file creation works; scheduled tasks are paused after Day 2; Task 1.1 lists the financial year end; the finished-early extras in section 3 now match the kit; MAP q3 (distractors that each fail one tag), q8 (a status summary) and q12 (new invoices each week, believable distractors) rewritten.
20. **Product facts rechecked (8 Nov):** the scheduled-tasks page lists "Create with Claude" and "Set up manually", and the fields name, prompt, approval mode, frequency, model and folder; it does not say whether Daily takes a time of day, so the pre-flight checks it. For Team plans, code execution is turned on by an owner (Organization settings → Plugins & skills), so participants only check that file creation works. [Help Center](https://support.claude.com/en/articles/13854387), [Help Center](https://support.claude.com/en/articles/12512180)

21. **Changes after QA round 4 (8 Nov):** Day 2 Lesson 3 ends with a quick check on event triggers (Demo 2.4 is 13 minutes; Day 2: 53 slides); each team builds its scheduled task on the account of the person who made the team's skill (shared skills cannot be edited by the people they are shared with); finished-early reruns copy the files into the Inbox again; the Task 1.4 hint says at least two rows are not Matched (BPK-4471 may be Not found); your own task list with no client or firm names is green on the safe-use card; Task 1.5 says no real files today; a scheduled run is its own session, so the decks say not to rely on it to recall the last run (the help page does not say more); Drive is connected before Day 1 and Demo 1.7 only shows it; the Day 1 Inboxes hold only their own pack; the vote result is read before Demo 2.1; MAP q2 option d says "more stable".

22. **Changes after QA round 5 (8 Nov), made after the five-round limit and not yet re-audited:** ChatGPT now has skills (beta, turned on by workspace owners), so the transfer map's Package row says "Skill (beta) or custom GPT" ([OpenAI Academy](https://academy.openai.com/public/resources/skills)); c1chk3 and b6chk ask what travels to any chat, Cowork and a schedule, because Cowork projects can hold recurring tasks ([Help Center](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)); knowledge holds templates and examples, the rules go in the instructions (b3t4, cheat sheet, Demo 1.4); a quick check on the Agent Card boxes (Day 1: 73 slides); Task 1.2 is 18 minutes after its story slide; the Task 1.2 debrief slide no longer names the planted rows; Task 1.6 no longer links the starter file at minute 0 (it is hint 3); Tasks 1.8 and 1.9 list the track packs; Demo 1.1 also checks the sign-by date in the letter; Task 2.3 gives Workflow teams an exact tracker line and the key the full tracker (10 received, 1 partly, 4 outstanding: 67%); Task 2.6 Workflow runs start from the request list; c4story is about two rules that conflict; the messy status sheet uses Jabriya's 64 hours; the batch-2 lease email covers all three 2026 leases; MAP q6 option c and the Arabic of q10 option a rewritten; two hub and Day 2 sentences made plainer.

## 10 · Missing facts

- RSM's logo files (white for dark pages, color for light): the theme takes RSM's colors from them.
- The Slack channel for the team message.
- Before the push: make the repo private, and approve Vercel access for your personal scope (link in chat).
