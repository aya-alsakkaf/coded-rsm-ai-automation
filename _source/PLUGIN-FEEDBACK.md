# Plugin feedback (coded-workshop-builder), from the RSM build, 8 Nov 2026

1. **MAP Part 3 (work scenarios).** `surveys.md` asks for a Part 3 section for professional rooms, but `surveys.py` groups MAP items by day only.
   The RSM kit marks its 4 scenario items as day 2; the portal drafts were then given a Part 3 section by hand.
2. **Final survey ids.** `surveys.md` keeps `q_4` and `q_5` for the first two can-do items and adds `q_ai` and `q_safe` for AI workshops;
   `surveys.py` writes `q_can1`... and no `q_ai` or `q_safe`. The RSM drafts follow `surveys.md`.
3. **MAP intro.** `surveys.md` ends the intro with "It is not graded: it shows us how much you learned in the program."; `surveys.py` leaves that sentence out.
4. **Light client colors.** A client blue such as RSM's `#0095D6` fails white text at 4.5:1, and `mix_theme.py` stops the build. A kit option for
   navy text on the client color would keep the exact brand color; the RSM kit darkens the fill instead (`#007DB4`) and passes `light`.
5. **Validator run time.** The full validator took over 10 minutes for 118 slides in the cloud workspace; build.sh could print progress per step.
6. **Staff home links (bug).** `vercel.json` sets `trailingSlash: false` and `cleanUrls: true`, so `staff/index.html` is only ever served at
   `/staff`. `staff.py` writes its staff-only links and `staff.css` as relative paths (`coded-<code>-lesson-plan.html`), which then resolve
   at the site root and give the 404 page. Worse, the "Day N slides with speaker notes" link resolves to the public deck, which has no notes.
   Fix in the engine: add `<base href="/staff/">` to the staff index (or write `/staff/...` links). The RSM kit works around the 404s
   with REDIRECTS from the root names to `/staff/...`; the two staff-deck links on the index still open the public decks.
