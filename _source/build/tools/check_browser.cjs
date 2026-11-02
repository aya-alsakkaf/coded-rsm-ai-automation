// Browser checks with Playwright. Start tools/serve.py first, then: node _source/build/tools/check_browser.cjs http://127.0.0.1:8765
// Checks: no sideways scroll at 390 px, no console errors, decks step to the end with →, notes on N (staff only),
// break clock, timers, card sort, quick checks, menu, COPY buttons.
const { chromium } = require('playwright');
const base = process.argv[2] || 'http://127.0.0.1:8765';
const C = 'coded-rsm-ai-automation';
const pages = ['', '-day-1', '-day-2', '-prompt-sheet-day-1', '-prompt-sheet-day-2', '-cheat-sheet', '-safe-use-card', '-take-home-guide', '-day-1-deck', '-day-2-deck'].map(s => '/' + C + s)
  .concat(['/staff', `/staff/${C}-facilitator-kit`, `/staff/${C}-answer-key`, `/staff/${C}-day-1-deck`, `/staff/${C}-day-2-deck`, '/404.html']);
const fails = [];
const fail = m => { fails.push(m); console.log('FAIL', m); };

(async () => {
  const b = await chromium.launch();
  // 1 · every page at 390 px and 1440 px: sideways scroll and console errors
  for (const w of [390, 1440]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 844 } });
    for (const u of pages) {
      const p = await ctx.newPage(); const errs = [];
      p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
      const r = await p.goto(base + u, { waitUntil: 'networkidle' });
      if (!r || r.status() >= 400) fail(`${u} @${w}: HTTP ${r && r.status()}`);
      const sw = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      if (sw > 1) fail(`${u} @${w}: sideways scroll ${sw}px`);
      if (errs.length) fail(`${u} @${w}: console ${errs.join(' | ')}`);
      await p.close();
    }
    await ctx.close();
  }
  // 2 · decks: keyboard to the end, widgets
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, permissions: ['clipboard-read', 'clipboard-write'] });
  for (const [u, staff] of [[`/${C}-day-1-deck`, false], [`/${C}-day-2-deck`, false], [`/staff/${C}-day-1-deck`, true], [`/staff/${C}-day-2-deck`, true]]) {
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e)));
    await p.goto(base + u, { waitUntil: 'networkidle' });
    const [n, steps] = await p.evaluate(() => [CodedDeck.slides.length, CodedDeck.slides.reduce((a, s) => a + +(s.dataset.steps || 0), 0)]);
    for (let i = 0; i < n - 1 + steps; i++) await p.keyboard.press('ArrowRight');
    const end = await p.evaluate(() => CodedDeck.current);
    if (end !== n - 1) fail(`${u}: → reached slide ${end + 1} of ${n} after ${n - 1 + steps} presses`);
    await p.keyboard.press('ArrowRight');
    if (await p.evaluate(() => CodedDeck.current) !== n - 1) fail(`${u}: → went past the end`);
    // every stepper reached its last step on the way
    const unfinished = await p.evaluate(() => CodedDeck.slides.filter(s => s.dataset.steps && +s.dataset.step !== +s.dataset.steps).length);
    if (unfinished) fail(`${u}: ${unfinished} steppers not at their last step`);
    await p.keyboard.press('Home');
    // notes
    await p.keyboard.press('n');
    const notes = await p.evaluate(() => { const e = document.querySelector('#dk-notes'); return e ? [e.classList.contains('on'), e.innerText.length] : null; });
    if (staff && !(notes && notes[0] && notes[1] > 30)) fail(`${u}: N did not show notes`);
    if (!staff && notes) fail(`${u}: public deck has a notes panel`);
    // menu
    await p.keyboard.press('m');
    if (!await p.evaluate(() => document.querySelector('#dk-menu').classList.contains('on'))) fail(`${u}: M did not open the menu`);
    await p.keyboard.press('Escape');
    // break clock
    await p.click('#dk-break-btn');
    const t1 = await p.textContent('#dk-break .clock'); await p.waitForTimeout(1300); const t2 = await p.textContent('#dk-break .clock');
    if (!(await p.evaluate(() => document.querySelector('#dk-break').classList.contains('on'))) || t1 === t2) fail(`${u}: break clock did not run`);
    await p.keyboard.press('Escape');
    // a timer on the first exercise slide
    const ex = await p.evaluate(() => CodedDeck.slides.findIndex(s => s.classList.contains('k-exercise')));
    await p.evaluate(i => CodedDeck.go(i), ex); await p.waitForTimeout(500);
    const tsel = `#s${ex + 1} .rsm-timer`;
    const a = await p.textContent(`${tsel} .t`); await p.click(tsel); await p.waitForTimeout(1400); const c = await p.textContent(`${tsel} .t`);
    if (a === c) fail(`${u}: exercise timer did not start`);
    await p.click(tsel);
    // card sort and quick check (day 1 public deck)
    if (u.endsWith('day-1-deck')) {
      const si = await p.evaluate(() => CodedDeck.slides.findIndex(s => s.classList.contains('k-sort')));
      await p.evaluate(i => { CodedDeck.go(i); CodedDeck.setStep(CodedDeck.slides[i], 0); }, si); await p.waitForTimeout(500);
      await p.click(`#s${si + 1} .rsm-chip >> nth=0`); await p.click(`#s${si + 1} .rsm-bin >> nth=2`);
      if (!(await p.evaluate(i => !!CodedDeck.slides[i].querySelectorAll('.rsm-bin')[2].querySelector('.rsm-chip'), si))) fail(`${u}: card sort did not move a card`);
      await p.keyboard.press('ArrowRight');
      const sorted = await p.evaluate(i => [CodedDeck.slides[i].querySelectorAll('.rsm-chip.wrong').length, CodedDeck.slides[i].querySelectorAll('.rsm-pool .rsm-chip').length], si);
      if (sorted[0] !== 1 || sorted[1] !== 0) fail(`${u}: card sort reveal wrong ${sorted}`);
      const ci = await p.evaluate(() => CodedDeck.slides.findIndex(s => s.classList.contains('k-check')));
      await p.evaluate(i => CodedDeck.go(i), ci); await p.waitForTimeout(400);
      await p.click(`#s${ci + 1} .rsm-opt >> nth=0`);
      const chk = await p.evaluate(i => [CodedDeck.slides[i].querySelectorAll('.rsm-opt.right').length, CodedDeck.slides[i].querySelectorAll('.rsm-opt.wrong').length], ci);
      if (chk[0] !== 1 || chk[1] !== 1) fail(`${u}: quick check marks ${chk}`);
    }
    if (errs.length) fail(`${u}: ${errs.join(' | ')}`);
    console.log('ok', u, n, 'slides', steps, 'steps');
    await p.close();
  }
  // 3 · COPY buttons
  for (const n of [1, 2]) {
    const p = await ctx.newPage();
    await p.goto(`${base}/${C}-prompt-sheet-day-${n}`, { waitUntil: 'networkidle' });
    const k = await p.locator('.sh-copy').count();
    for (let i = 0; i < k; i++) {
      await p.locator('.sh-copy').nth(i).click(); await p.waitForTimeout(250);
      const txt = await p.locator('.sh-copy').nth(i).textContent();
      const clip = await p.evaluate(() => navigator.clipboard.readText());
      const pre = await p.locator('.sh-promptwrap pre').nth(i).innerText();
      if (txt !== 'COPIED' || clip.trim() !== pre.trim()) fail(`prompt sheet ${n}: COPY ${i + 1} failed`);
    }
    console.log('ok prompt sheet', n, k, 'COPY buttons');
    await p.close();
  }
  await b.close();
  console.log(fails.length ? `BROWSER FAILS: ${fails.length}` : 'BROWSER FAILS: 0');
  process.exit(fails.length ? 1 : 0);
})();
