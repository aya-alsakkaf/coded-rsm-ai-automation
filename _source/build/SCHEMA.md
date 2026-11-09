# Kit schema: every field the engine reads

The kit is five Python files and two data files in `_source/kit/`. The engine reads nothing else. "Req" means the build stops (or the
validator fails) without it. "Opt" fields have the default shown. `examples/ai-claude/` (AI tool, CODED only) and `examples/kibs-tirm/`
(no AI tool, client mix) fill every field.

## content.py: the workshop

| Field | Req | Default | Shape and use |
|---|---|---|---|
| `CODE` | Req | | `"acme-ai"`. Every name: pages `coded-<CODE>-…`, assets, fonts, the logo files, `package.json` name, the lab storage key, the QR alt text. |
| `TITLE` | Req | | Program name. Every page title, deck cover, crumb, staff pages, surveys. |
| `SUBTITLE` | Req | | Hub fallback for `HUB["sub"]`, `HUB["program_title"]`, the hub description. |
| `BRAND` | Opt | `"CODED"` | The pill on the hub and the cover, the deck crumb (`"CODED · Professionals"`, `"CODED × KIBS"`). |
| `TOOL_MODE` | Opt | `"ai"` | `"ai"`: prompt players, opener, next-word widget, prompt sheets, safe-use card. `"none"`: no AI helpers (they stop the build with a message), `widget()` topic demos, task sheets with templates, verify card. |
| `CLIENT` | Opt | `None` | `None` = CODED only. Or `{"name", "short", "primary"` (req), `"logo"` (file in the kit folder), `"logo_scale"` (1.0; about 1.3 for a round seal), `"secondary"`, `"light"` (accent text override), `"url"`}. Drives the mix (`mix_theme.py`) of the site, deck and staff CSS, the lockups, `ORG` ("CODED × short"), the footer link. The build stops if white text on `primary` is under 4.5:1 or the accent tint fails on the navy or the lightest glass. |
| `DATES`, `HOURS`, `VENUE`, `TOOLS` | Req | | Hub hero, day pages, cover, lesson plan, survey descriptions. |
| `DAYDATE` | Req | | `{1: "Sunday 20 Dec", …}`: cover, hub cards, lesson plan. |
| `SAMPLE_NOTE`, `THRU`, `STORY` | Req | | Footers and sheets; the habit (hub, cheat sheet, lesson plan); the road slide lede and hub lead fallbacks. |
| `AUDIENCE` | Opt | | Used only by kit text (e.g. `LESSON_INTRO`). |
| `OUTCOMES` | Req | | Hub outcomes, lesson plan, final survey "I can" items (`q_can1…`). |
| `CONFIDENCE` | Req | | MAP Part 1 items (usually `= OUTCOMES`). |
| `DAYS` | Req | | `{d: {"title", "claim", "sub", "brief", "artifact", "blocks": [("08:30-08:40", name, what or "" for a break)], "outcomes": [...]}}` plus hub fields `"cat"`, `"icon"` (doc, dash, eye, scale, mail, flask…), `"tag"`, `"bullets"`. Day pages, run of show (minutes are computed), cover, outcomes and road slides, lesson plan, facilitator kit. |
| `MAP` | Req | | `[{"q", "o": [4], "a": index, "day": d, …}]`: MAP slides (question count), facilitator key, answer key (last day), surveys. |
| `MAP_KEY` | Req | | One-line key string: facilitator kit, survey descriptions. |
| `FORMS` | Req | | `{"pre"|"post"|"survey": {"name", "when", "url", "slug", "id"}}`. `when` = "Day 1 · Sun 20 Dec · 08:40": printed with each QR (MAP slides, hub, day pages, staff index). Redirects `/pre`, `/post`, `/survey`. Slugs: kebab case, at most 80 characters (surveys.py checks). |
| `FORM_DAY` | Opt | `{first: ["pre"], last: ["post", "survey"]}` | Which forms each day page and `opening()` show. |
| `MAP_MIN` | Opt | `10` | MAP slide timer and title, note timing. |
| `MAP_LEDE` | Opt | engine text | `{"before": "...", "after": "..."}` replaces the MAP slide lede. |
| `SLIDES` | Req | | `{d: count}`: the approved slide plan. The validator fails when a deck differs. The engine never asserts a total. |
| `HUB` | Opt | short fallbacks | `"headline"` [line, accent line], `"sub"`, `"meta"` (after the venue), `"program_title"`, `"program_lead"`, `"habit_eyebrow"`, `"habit_title"`, `"habit_text"`, `"habit_list"` [(bold, text)], `"files_title"`, `"takeaway_text"`, `"map_text"`, `"about"`, `"description"`, `"day_tool_note"`, `"stats"` [(value or None for the slide count, label)], `"bands"` [(eyebrow, title, html, [items])]. |
| `SHEET` | Opt | by `TOOL_MODE` | `{"name", "slug", "nav", "what", "howto": [html], "note": html}`: the daily sheet page. |
| `CARD` | Req | name, slug by `TOOL_MODE` | `{"lede", "meta", "cards": [(green|amber|red, heading, text, [examples])], "risks_title", "risks_head", "risks": [rows], "policy_title", "policy": [...]}`: safe-use card or verify card page; the hub habit band links it. |
| `CHEAT` | Req | | `[(part, title, sub, [(name, text, example, note)], summary)]`: cheat sheet. |
| `CHEAT_TABLES`, `CHEAT_LEDE`, `CHEAT_META` | Opt | none | Extra tables `[(title, head, rows)]`, the hero lede, the hero chips. |
| `GUIDE_INTRO`, `GUIDE`, `GUIDE_HABIT` | Req | | Take-home guide: `[(heading, [steps])]`. `GUIDE_META` opt. |
| `SOURCES` | Opt | `{}` | `{key: (title, url)}` for `("sources", [keys])` answer blocks. |
| `LLM` | AI | | `{"tree": {...}, "foot": "Percentages are illustrative."}`: `llmslide()`. |
| `TASK_FALLBACK_LINE` | Opt | engine line | Footer line of the prompt panel on AI task slides. |
| `REWRITE_LABEL` | Opt | "Rewrite these weak prompts" | Label of a task's `examples` on the sheet. |
| `LESSON_INTRO`, `RUNBOOK_PREFLIGHT` | Opt | short defaults | Lesson plan intro; runbook pre-flight list. |
| `FACILITATOR` | Opt | `[]` | `[(id, title, sub, [blocks])]`: facilitator kit sections. The engine adds a run of show per day and the MAP links and key. |
| `LABS` | Opt | `{}` | `{d: {"title", "intro", "steps": [{"title", "do": [...], "hint", "files": [...], "check": {"kind": "flag", "label", "answer"} or {"kind": "note", "label"}, "answer": [blocks]}]}}`: a public lab page per day (done marks in localStorage, hints, a hashed flag check), linked from the day page and hub; answers only on `/staff/…-lab-key-day-N`. |
| `PRACTICE` | Opt | none | `{"title", "pill", "intro", "note", "topics": {key: label}, "questions": [{"topic": key, "q", "o": [4 options], "a": index, "why"}]}`: a public page `coded-<CODE>-practice-questions`, linked from the hub, the day pages and the staff index. One card per question; a pick shows right or wrong, the right option in green and the `why`; a score, a bar per topic, "show only my wrong answers", "start again" and the best score kept in localStorage (try/catch). The right option is stored as a salted SHA-256 hash, not as plain text. Practice only: never scored or sent. The validator checks the shape, the count, the hub link, the saved answers, and that no question shares an 8-word run with a `MAP` question; it also clicks a right and a wrong answer in the browser. |
| `SEGMENTS` | Opt | `{}` | `{d: [("08:30-10:00", "Session 1 · …", [("08:30", minutes, "block"), …])]}`: the minutes inside each session, shown on the lesson plan under the day's run of show. The validator checks that the times follow each other and fill the session. |
| `REDIRECTS` | Opt | `[]` | Extra `[(source, destination)]` in `vercel.json` (the validator checks each one). |
| `SURVEY` | Opt | none | Portal payloads (`surveys.py`): `"program"`, `"program_ar"`, `"client"`, `"subtitle"` {en, ar}, `"folder"`, `"name_prefix"`, `"note"`, `"test_min"`, `"confidence_ar"` [one per outcome], `"map_ar"` [(question, [options])], `"day_ar"` {d: title}, `"hands_on"`, `"materials"`, `"logistics"`, `"relevance"` (en, ar pairs), `"dept_label"`. Without it no payloads are written. |
| `YEAR` | Opt | `2026` | Footers. |

## content_demos.py: demos and tasks

| Field | Req | Shape and use |
|---|---|---|
| `DEMOS` | Req | `{id: {...}}`. Each: `day`, `skill` ("1.2"), `sec` (a `BLOCK` key), `title`, `tool`, `setup` (steps; `"[T] …"` = trainer only), `expected`, `say`, `point`, `fallback`, `hint`, `backup` [blocks], and for tasks `hands_on=True`, `minutes`, `solo`, `deliverable`, `answer` [blocks], `stretch` [...], `points` (opt). AI: `prompts` [(label, text)], `stretch_prompts`, `examples`, `player` {parts, table, best, reco, control}. No AI: `templates` [(label, text)]. The engine fills `card` ("Task 1.2" or "Demo 1.2"), `files`, `kind` and the empty lists. Used by task, player, sortslide, widget slides, sheets, day pages, runbooks, backups, answer keys, lesson plan. `say`, `expected` and `fallback` go into the notes; keep them different from the slide text. |
| `BLOCK` | Req | `{sec: (day, "Block 1 · …")}`: sheet sections, runbook bands, backups. |
| `ALL_FILES` | Req | Every sample file name: copied to `public/` byte for byte (the validator checks the bytes), hub, staff index, lesson plan. |
| `SHOWCASE` | AI | The opener: `eyebrow`, `title`, `tool`, `file`, `weak`, `weak_answer`, `weak_flags`, `parts`, `table`, `strong_answer`, `strong_flags`, `score`, `punch`, `punch_sub`. Passed to `showcase()`. |

## build_deck.py: the slides

`from deck import *`, then one function per day returning a list of helper calls, and these names:

| Name | Req | Default | Use |
|---|---|---|---|
| `DAYFN` | Req | | `{d: day_function}`. The engine appends the close slide. |
| `TOPICS` | Req | | `{d: {"open": "Opening", "b1": "Block 1 · …", …, "close": "Close"}}`: notes pages, the where-we-are strip, derived sections. Every slide's topic must be in a section. |
| `SECTIONS` | Opt | one per topic | `{d: [(label, glyph, [topics])]}`: the progress bar. |
| `FLOW` | Opt | topics minus open and close | `{d: ([labels], {topic: index})}`: the strip on task slides. |
| `COVER_NOTES`, `OUTCOMES_NOTES` | Opt | engine `do` lines | `{d: N(...)}`. |
| `ROAD` | Opt | title from the day | `{d: {"title", "lede", "n"}}`: today's map. |
| `CLOSE` | Opt | "Thank you." | `{d: {"big", "next", "n"}}`: the close slide. |
| `EXTRA_CSS`, `EXTRA_JS` | Opt | `""` | The kit's own topic-demo CSS and JS (e.g. `kt_widgets.CSS/JS`), themed with the deck. |

Helpers (each returns one slide; `n=N(say, do, expect, silent, fallback, more, time)` is its note):
`opening(day, opener=[...])` (cover → pre-MAP on its day → opener → outcomes → today's map), `story`, `rule`, `term`, `listslide`,
`cards3`, `stats`, `tslide`, `check`, `sortslide(sid, topic, tag, title, items, labels, did=None)`, `widget(sid, topic, did, tag, title, html, take)`,
`task(sid, topic, did)`, `scene(sid, topic, tag, title, text, take, draw)`, `mapslide(sid, topic, "before"|"after")`, `wrap`, `timer_slide`;
AI only: `player(sid, topic, did)`, `showcase(sid, topic, SHOWCASE)`, `llmslide(sid, topic, tag, title, lede, take)`.
`scene()` draws `person, building, house, laptop, phone, doc, mail, coin, lock, shield, clock, chart, magnifier` at `(x, y)` in a
480×300 box with `label`, `tone` (hot, dim, bad, ok) and `anim` (bob, nod, glow, pop), plus `move` (an object along a dashed path),
`pill`, `stamp`, `ring`, `line`, `text` and `ground` (see `deck.scene_svg`).

## gen_files.py and the other kit files

| File | Req | Use |
|---|---|---|
| `gen_files.py` | Req | `python3 gen_files.py OUTDIR` writes every file in `ALL_FILES` to `_source/files/` (build.sh runs it first). |
| `data.py` | Opt | The kit's own numbers and names; the engine never reads it. |
| `leftover-words.txt` | Req | `code: name, name` lines of names from other builds; the validator fails when one shows on a page. The line whose code is this kit's `CODE` is skipped. Keep both example lines when you copy. |
| client logo | Opt | The file named in `CLIENT["logo"]`, in the kit folder. Copied as `coded-<code>-client-logo.png` and inlined in the decks. |
| `kt_widgets.py` (any name) | Opt | Topic demos without an AI tool: HTML for `widget()`, CSS and JS for `EXTRA_CSS` / `EXTRA_JS`. |
