# CLAUDE.md · coded-rsm-ai-automation

Read this before you change anything in this repo.

## Rules

- `public/` is generated. Edit `_source/build/`, run `build.py`, then `validate_site.py` (PROBLEMS: 0) and `tools/check_browser.cjs` (BROWSER FAILS: 0).
- Plain English for ESL readers. American spelling. No em dashes anywhere (the validator checks).
- Answers never go on a public page: no MAP key, no expected outputs, no planted findings. Those live under `/staff` only.
- Public pages never link to `/staff`.
- No gold. CODED navy and blues; RSM accent `#009CDE` only in the client name. Amber only for the traffic light.
- The workshop Anthropic API key is never on a slide, page, file or in this repo. Staff hand it out in the room.
- Never choose, ask for, store or print the staff password. The user sets `STAFF_PASSWORD` in Vercel.
- Never use a token or password pasted in chat. If someone pastes one, do not use it and tell them to revoke it.
- Only touch this program's surveys in the portal (folder `e07488c7-5525-403f-a2c6-f6db15ae710a`). Never edit, close or delete another program's surveys.
- Commit, push, publish surveys or post to Slack only after a clear yes from the user.

## Decisions

| Date | Decision | Why |
|---|---|---|
| 2026-11-02 | No handoff kit. CODED wrote all content from the outline in Notion and the final outline in chat. | The user asked to ignore the handoff build. |
| 2026-11-02 | Visual reference: coded-ai-finance.vercel.app (Finance glass theme). | Reference repos were not reachable. |
| 2026-11-02 | This cohort only (RSM-AI-Nov/Nov-26). | User choice. |
| 2026-11-02 | CODED navy with RSM accent `#009CDE`. Text lockup "RSM Albazie" until RSM logo files arrive. | User choice; no logo files provided. `#009CDE` is assumed, confirm with RSM. |
| 2026-11-02 | CODED provides one shared Anthropic key for n8n on Day 2. | User choice. |
| 2026-11-02 | Fictional tasks and data. Practice firm "Mirqab & Co."; clients Khiran, Jabriya, Salwa, Abdali. | User choice: no real RSM data. |
| 2026-11-02 | Hours 08:30 to 16:30, venue CODED, Morning Alsharekh. | User gave 8 hours per day; start time assumed. |
| 2026-11-02 | Own deck engine in the Playbook grammar, two copies per day (public without notes, staff with notes). | Notes must not reach participants. |
| 2026-11-02 | No videos and no PDF exports of decks. | Not in scope. |
| 2026-11-02 | Day 2 n8n node names follow the current n8n UI; a dry run before Day 2 is required. | n8n renames nodes between versions. |
