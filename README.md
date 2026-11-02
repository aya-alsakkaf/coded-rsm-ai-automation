# CODED × RSM Albazie · AI Innovation and Automation

Two-day workshop site for RSM Albazie, run by CODED Professionals.

- **Cohort:** RSM-AI-Nov/Nov-26
- **Dates:** Sun 15 Nov 2026 and Mon 16 Nov 2026, 08:30 to 16:30
- **Venue:** CODED, Morning Alsharekh
- **Tools:** Claude (Day 1) and n8n with Claude (Day 2)
- **Practice firm:** Mirqab & Co. (fictional). All clients, people and numbers in the sample files are made up.

## Pages

| Short link | Page | Who |
|---|---|---|
| `/` | Home: both days, MAP links, resources | Participants |
| `/day1`, `/day2` | Day page: run of show, tasks, files | Participants |
| `/slides1`, `/slides2` | Deck (no speaker notes) | Room screen |
| `/prompts1`, `/prompts2` | Prompt sheet with COPY buttons | Participants |
| `/pre`, `/post`, `/survey` | Pre-MAP test, post-MAP test, final survey (portal) | Participants |
| `coded-rsm-ai-automation-cheat-sheet` | Cheat sheet: framework, instruction, tests, workflow skeleton | Participants |
| `coded-rsm-ai-automation-safe-use-card` | Safe use card | Participants |
| `coded-rsm-ai-automation-take-home-guide` | Take-home guide | Participants |
| `/staff` | Staff index (locked) | CODED staff |
| `/staff/coded-rsm-ai-automation-day-1-deck`, `-day-2-deck` | Decks with speaker notes (press N) | Instructor |
| `/staff/coded-rsm-ai-automation-facilitator-kit` | Setup, expected outputs, checks, trouble | Instructor |
| `/staff/coded-rsm-ai-automation-answer-key` | MAP answer key | Instructor |

Deck keys: → next step or slide, ← back, N notes (staff copy only), M menu, F fullscreen, B bell, ☕ break clock. Click a task timer to start or pause it.

## Staff lock

`middleware.js` protects `/staff` with a username and password (Basic auth).

- Username: `staff` (change it with `STAFF_USER` if you want).
- Password: set `STAFF_PASSWORD` yourself in Vercel: **Settings → Environment Variables → Production**, then redeploy.
- Until the password is set, `/staff` returns 503 and stays closed.
- Never put the password in Slack, the repo or a chat.

## MAP tests and survey (CODED portal)

| Item | Portal slug | When |
|---|---|---|
| Pre-MAP test | `coded-rsm-albazie-ai-innovation-and-automation-map-test-pre-day-1` | Day 1, 08:45 |
| Post-MAP test | `coded-rsm-albazie-ai-innovation-and-automation-map-test-post-day-2` | Day 2, 15:55 |
| Final satisfaction survey | `coded-rsm-albazie-ai-innovation-and-automation-final-satisfaction-survey` | Day 2, after the post-MAP |

Public link pattern: `https://platform.joincoded.com/sv/<slug>`. The answer key is in the PRE description in the portal and on the staff answer key page only.

## Build and check

Everything in `public/` is generated. Edit the sources in `_source/build/`, then run:

```bash
python3 _source/build/make_files.py         # only if you change the sample files
python3 _source/build/content_map.py        # only if you change MAP or survey content
python3 _source/build/build.py
python3 -I _source/build/validate_site.py   # must print PROBLEMS: 0
python3 _source/build/tools/serve.py &      # local server on :8765 with clean URLs
NODE_PATH=$(npm root -g) node _source/build/tools/check_browser.cjs http://127.0.0.1:8765   # must print BROWSER FAILS: 0
```

| Source | What it holds |
|---|---|
| `content_core.py` | Program facts, days, run of show, tasks, files, MAP links |
| `content_prompts.py` | Agent instructions, n8n prompts and schemas, prompt sheets |
| `content_slides.py` | Both decks: slides, timings, speaker notes |
| `content_takeaways.py` | Cheat sheet, safe use card, take-home guide |
| `content_staff.py` | Facilitator kit: setup, expected outputs, checks, trouble |
| `content_map.py` | MAP questions (PRE = POST), answer key, final survey |
| `make_files.py` | The 10 fictional sample files |
| `kit_*.py`, `css/`, `assets/` | Page and deck templates, styles, deck engine |

## Deploy

Vercel project linked to this repo. Framework: Other. No build command. Output directory: `public`. Every push to `main` deploys.
