# The workshop engine

One neutral engine builds a whole CODED workshop site from a kit: hub, day pages, decks with speaker notes, prompt or task sheets,
browser labs, cheat sheet, safe-use or verify card, take-home guide, trainer pages under `/staff`, sample files, survey payloads and the
Vercel config. A new workshop writes only its kit files and its logo. It never edits a file in this folder.

## Start a new repo

```
<repo>/_source/build/   <- copy this folder, without examples/   (the engine: never edit)
<repo>/_source/kit/     <- copy the closer example kit, then edit   (yours)
```

1. Copy the engine: everything here except `examples/` goes to `<repo>/_source/build/`.
2. Copy the closer example kit to `<repo>/_source/kit/`: `examples/ai-claude/` for a workshop with an AI tool and no client (CODED only),
   `examples/kibs-tirm/` for a workshop without an AI tool and with a client brand. Keep `leftover-words.txt`.
3. Edit only the kit: `content.py` (set `CODE`, `TOOL_MODE`, `CLIENT`, `FORMS`, `SLIDES` and the words), `content_demos.py`, `data.py`,
   `build_deck.py`, `gen_files.py`, the client logo file, and any topic-demo file (`kt_widgets.py` in the example). `SCHEMA.md` lists every field.
   Leave `leftover-words.txt` as it is: it already flags both examples' names for any new code. Add a line only for a past workshop you copied text from.
4. Build: `bash _source/build/build.sh`. It writes the sample files, the decks, the pages, the staff pages, `vercel.json`,
   `package.json`, `middleware.js`, the survey payloads, and then runs the validator.
5. Check: the validator must print `PROBLEMS: 0`. Then copy `skills/coded-workshop-qa/scripts/qa.cjs` next to the repo (never into
   `public/`) and run `node qa.cjs pages public out/pages` and `node qa.cjs decks public out/decks`. Both must exit 0.

Requirements: Python 3.10+, `playwright` (Chromium), `segno`, `opencv-python` (QR decode), `openpyxl` and `python-docx` (the example
`gen_files.py`), Node 18+ with `playwright` for `qa.cjs`.

## What each file does

| File | Job |
|---|---|
| `build.sh` | Runs the steps in order: `gen_files.py` (kit), `deck.py`, `pages.py`, `staff.py`, `config.py`, `surveys.py`, `validate_site.py`. `WK_KIT=/path` picks another kit folder. |
| `wk.py` | Engine core: finds the kit, reads every setting (names from `CODE`, the `TOOL_MODE` branch, the client, the forms), the theme mix, fonts, text rules (no em dash, American spelling), QR codes, demo defaults, answer blocks. |
| `deck.py` | Slide helpers the kit calls and the deck builder: public deck (no notes) and `/staff` deck (notes on N), on the Playbook deck kit, CODED tokens then the client mix. Writes `_source/kit-pages/slides-day-N.json` and `presenter-notes-day-N.json`, the record the validator compares with the site. Holds `scene()`. |
| `widgets.py` | AI branch only: the prompt player, the weak and strong opener, the next-word widget. |
| `pages.py` | Public pages: hub, day pages, the daily sheet (prompt or task), the browser lab per day, the practice-questions page (when the kit has `PRACTICE`), cheat sheet, card page, take-home guide, 404, index, robots.txt, the site CSS. |
| `staff.py` | Trainer pages: workshop index, lesson plan (with the minutes inside each session when the kit has `SEGMENTS`), facilitator kit, and per day the presenter notes, runbook, backup results, answer keys and lab key. |
| `config.py` | `vercel.json` (redirects from the kit, `X-Robots-Tag: noindex` on every path, `private, no-store` on `/staff`), `package.json` (named `coded-<code>`), `middleware.js`, `.gitignore`, `.vercelignore`. |
| `surveys.py` | PRE, POST and final survey payloads in English and Arabic for the CODED portal (when the kit has `SURVEY`). |
| `validate_site.py` | The quality gate (see its docstring): kit fidelity both ways, notes, counts, files, noindex, redirects, QR, fit at 1440×810, labs, gold, leftover words. |
| `mix_theme.py` | Copy of `site-kit/tools/mix_theme.py`: the CODED and client mix with contrast checks on the navy and on glass. |
| `assets/` | Neutral copies of the site kit (theme `coded-site.css` with `__PFX__` font names, `deck-kit/` with the client prefix renamed `wk-` and the client block left as a placeholder, fonts, CODED logo, favicon), plus the engine's own `deck-extra.css`, `scene.css`, `staff.css`, `middleware.js` and the widget CSS and JS (CODED blues, no gold). When the site kit changes, copy the changed file here and keep it neutral. |
| `examples/` | Two kits that build out of the box (not part of the engine): `ai-claude/` (TOOL_MODE "ai", CODED only) and `kibs-tirm/` (TOOL_MODE "none", client mix with a dark primary). |

## Rules the engine keeps for you

- Day order: cover, the pre-MAP slide on its day, the opener, outcomes, today's map. The close slide is added for you.
- Notes are explicit parts (`N(say, do, expect, silent, fallback, more, time)`), escaped once, never copied from the slide.
  The validator fails a note that shares an 8-word run with its slide.
- No slide totals, files, videos or colors in the engine: counts come from `SLIDES`, files from `ALL_FILES`, colors from `CLIENT`.
- Every text reaches 4.5:1 (3:1 for large text) on its real background, including the client mix on glass; no gold in any form.
- Each QR shows the form name, its day and time, and decodes to its portal URL.
- Labs keep answers off the public page: a flag is checked against a salted SHA-256 hash; done marks and notes live in localStorage (try/catch).
- Practice questions (optional `PRACTICE`) are scored in the browser and never sent; the right option is a salted hash; no question may share an 8-word run with the MAP test.
