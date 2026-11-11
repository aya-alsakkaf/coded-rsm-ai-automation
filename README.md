# CODED × RSM Albazie · AI Innovation and Automation

Two-day workshop site for RSM Albazie & Co., run by CODED Professionals.

- **Cohort:** RSM-AI-Nov/Nov-26
- **Dates:** Sunday 15 and Monday 16 November 2026, 08:30 to 16:30
- **Venue:** CODED, Alsharekh classroom (Frontend Campus)
- **Tools:** Claude (chat, Projects, the Google Drive connector, artifacts, skills, scheduled tasks); n8n as a trainer demo
- **Story:** Mirqab & Co. (a fictional audit firm) and its fictional client Abdali Foods. Every file is made up.

## Pages

| Address | Page | Who |
|---|---|---|
| `/` → `/coded-rsm-ai-automation` | Program home | Everyone |
| `/day1`, `/day2` | Day pages: run of show, outcomes, files, MAP QR | Everyone |
| `/slides1`, `/slides2` | Decks, no speaker notes | Room screen |
| `/prompts1`, `/prompts2` | Prompt sheets with COPY buttons | Everyone |
| `/lab1`, `/lab2` | Browser labs: build your agent; put your workflow on a schedule | Everyone |
| `coded-rsm-ai-automation-cheat-sheet`, `-safe-use-card`, `-take-home-guide` | Take-aways | Everyone |
| `/pre`, `/post`, `/survey` | Pre-MAP, post-MAP, final survey (CODED portal) | Everyone |
| `/staff` | Lesson plan, decks with notes (press N), facilitator kit, runbooks, backups, answer keys, lab keys | Password |

Deck keys: → next, ← back, N notes (staff copy only), F fullscreen, ☕ break clock. Click a task timer to start it.

## Build

Everything in `public/` is generated. Edit only `_source/kit/`, then:

```bash
bash _source/build/build.sh            # sample files, decks, pages, staff pages, config, survey payloads, then the validator (PROBLEMS: 0)
python3 _source/tools/class_plan.py    # CLASS-PLAN.md
```

## Deploy

A push to `main` deploys on Vercel (framework Other, no build command; `vercel.json` sets `public/` as the output).
The staff lock needs `STAFF_PASSWORD` in Vercel → Settings → Environment Variables → Production, then a redeploy. Until then `/staff` returns 503.
Never put the password in Slack, the repo or a chat.

## MAP tests and survey (CODED portal)

| Item | Slug | When |
|---|---|---|
| Pre-MAP test | `coded-rsm-albazie-ai-innovation-and-automation-map-test-pre-day-1` | Day 1, 08:35 |
| Post-MAP test | `coded-rsm-albazie-ai-innovation-and-automation-map-test-post-day-2` | Day 2, 16:10 |
| Final satisfaction survey | `coded-rsm-albazie-ai-innovation-and-automation-final-satisfaction-survey` | Day 2, 16:20 |

Links: `https://platform.joincoded.com/sv/<slug>`. The MAP answer key is in the portal description and the staff pages only.
