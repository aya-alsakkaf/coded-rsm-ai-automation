/* CODED deck engine · RSM Albazie workshop.
   Navigation, section progress, menu (M), speaker notes (N, staff decks only), fullscreen (F), bell (B),
   the ☕ break clock, exercise timers, and on-slide steppers: → first plays the steps of a slide that has
   data-steps (opener, word guess, instruction player, flow, card sort, quick check), then moves on. */
(function () {
  'use strict';
  var $ = function (q, c) { return (c || document).querySelector(q); };
  var $$ = function (q, c) { return [].slice.call((c || document).querySelectorAll(q)); };
  var pad = function (n) { return String(n).padStart(2, '0'); };
  var cfg = window.DECK || { sections: ['Deck'], staff: false };
  var slides = $$('.dk-slide');
  var cur = 0;

  /* ── sound: bell and alarm (Web Audio, no files) ── */
  var ctx = null;
  function ac() { if (ctx) return ctx; var C = window.AudioContext || window.webkitAudioContext; if (!C) return null; try { ctx = new C(); } catch (e) { return null; } return ctx; }
  function tone(c, dest, f, t, d, g) {
    var o = c.createOscillator(); o.type = 'sine'; o.frequency.setValueAtTime(f, t);
    var gn = c.createGain(); gn.gain.setValueAtTime(0, t); gn.gain.linearRampToValueAtTime(g, t + 0.05); gn.gain.exponentialRampToValueAtTime(0.001, t + d);
    o.connect(gn); gn.connect(dest); o.start(t); o.stop(t + d + 0.1);
  }
  function chime() {
    var c = ac(); if (!c) return; if (c.state === 'suspended') c.resume();
    var now = c.currentTime, m = c.createGain(); m.gain.value = 0.5; m.connect(c.destination);
    [[587.33, 0, 1.4, .8], [739.99, .45, 1.4, .8], [880, .9, 1.4, .75], [1174.66, 1.35, 1.6, .6]].forEach(function (n) { tone(c, m, n[0], now + n[1], n[2], n[3]); });
    document.documentElement.classList.add('dk-ring'); setTimeout(function () { document.documentElement.classList.remove('dk-ring'); }, 2600);
  }
  function alarm() {
    var c = ac(); if (!c) return; if (c.state === 'suspended') c.resume();
    var now = c.currentTime, m = c.createGain(); m.gain.value = 0.5; m.connect(c.destination);
    for (var i = 0; i < 3; i++) { tone(c, m, 988, now + i * 1.1, .45, .8); tone(c, m, 740, now + i * 1.1 + .5, .5, .8); }
  }

  /* ── timers ── */
  function fmt(s) { s = Math.max(0, Math.round(s)); return pad(Math.floor(s / 60)) + ':' + pad(s % 60); }
  function makeTimer(el) {
    var total = (+el.dataset.minutes || 5) * 60, left = total, end = null, id = null, out = $('.t', el) || el;
    function render() { out.textContent = fmt(left); el.classList.toggle('warn', id && left <= 120 && left > 0); }
    function tick() { left = Math.max(0, (end - Date.now()) / 1000); render(); if (left <= 0) done(); }
    function done() { clearInterval(id); id = null; el.classList.remove('run', 'warn'); el.classList.add('done'); alarm(); }
    function start() { if (id || left <= 0) return; end = Date.now() + left * 1000; id = setInterval(tick, 250); el.classList.add('run'); render(); }
    function stop() { if (id) { clearInterval(id); id = null; } el.classList.remove('run'); render(); }
    function reset() { stop(); el.classList.remove('done', 'warn'); left = total; render(); }
    function add(s) { left = Math.max(0, left + s); if (id) end = Date.now() + left * 1000; el.classList.remove('done'); render(); }
    el.addEventListener('click', function () { if (el.classList.contains('done')) { reset(); return; } id ? stop() : start(); });
    var box = el.parentElement;
    $$('[data-tadd]', box).forEach(function (b) { b.addEventListener('click', function () { add(+b.dataset.tadd); }); });
    $$('[data-treset]', box).forEach(function (b) { b.addEventListener('click', reset); });
    render();
    return { start: start, stop: stop, reset: reset };
  }
  $$('.rsm-timer[data-minutes]').forEach(makeTimer);

  /* ── the ☕ break clock ── */
  var brk = $('#dk-break'), bid = null, bend = 0;
  function breakRun(min) {
    clearInterval(bid); bend = Date.now() + min * 60000; brk.classList.remove('done');
    var back = new Date(bend); $('.back', brk).textContent = 'Back at ' + pad(back.getHours()) + ':' + pad(back.getMinutes());
    function t() { var l = (bend - Date.now()) / 1000; $('.clock', brk).textContent = fmt(l); if (l <= 0) { clearInterval(bid); brk.classList.add('done'); chime(); } }
    t(); bid = setInterval(t, 250);
  }
  function breakOpen() { brk.classList.add('on'); breakRun(+brk.dataset.default || 15); }
  function breakClose() { brk.classList.remove('on'); clearInterval(bid); }
  if (brk) {
    $$('[data-bmin]', brk).forEach(function (b) { b.addEventListener('click', function () { breakRun(+b.dataset.bmin); }); });
    $('[data-bclose]', brk).addEventListener('click', breakClose);
  }

  /* ── steppers ── */
  function stepsOf(s) { return +(s.dataset.steps || 0); }
  function stepOf(s) { return +(s.dataset.step || 0); }
  function setStep(s, k) {
    k = Math.max(0, Math.min(stepsOf(s), k)); s.dataset.step = k; setTimeout(function () { if (s === slides[cur]) fit(s); }, 380);
    $$('[data-at]', s).forEach(function (e) { var a = +e.dataset.at; e.classList.toggle('on', k >= a); e.classList.toggle('now', k === a); });
    var pl = $('.rsm-player', s); if (pl) pl.classList.toggle('showres', k >= +pl.dataset.res);
    if (s.classList.contains('k-sort')) { k >= 1 ? revealSort(s) : unrevealSort(s); }
    if (s.classList.contains('k-check') && k >= 1) revealCheck(s, null);
    $$('.rsm-step-btn', s).forEach(function (b) { b.disabled = k >= stepsOf(s); });
  }
  $$('.rsm-step-btn').forEach(function (b) { b.addEventListener('click', function () { var s = b.closest('.dk-slide'); setStep(s, stepOf(s) + 1); }); });

  /* card sort: click a card, then a column */
  $$('.k-sort').forEach(function (s) {
    var sel = null;
    $$('.rsm-chip', s).forEach(function (c) {
      c.addEventListener('click', function (e) { e.stopPropagation(); if (s.dataset.revealed) return; if (sel) sel.classList.remove('sel'); sel = (sel === c) ? null : c; if (sel) sel.classList.add('sel'); });
    });
    $$('.rsm-bin', s).forEach(function (b, i) {
      b.addEventListener('click', function () { if (!sel || s.dataset.revealed) return; $('.in', b).appendChild(sel); sel.dataset.placed = i; sel.classList.remove('sel'); sel = null; });
    });
  });
  function revealSort(s) {
    if (s.dataset.revealed) return; s.dataset.revealed = 1;
    var bins = $$('.rsm-bin', s);
    $$('.rsm-chip', s).forEach(function (c) {
      var want = +c.dataset.bin;
      if (c.dataset.placed !== undefined) c.classList.add(+c.dataset.placed === want ? 'right' : 'wrong');
      $('.in', bins[want]).appendChild(c);
    });
  }
  function unrevealSort(s) {
    if (!s.dataset.revealed) return; delete s.dataset.revealed;
    var pool = $('.rsm-pool', s);
    $$('.rsm-chip', s).forEach(function (c) { c.classList.remove('right', 'wrong', 'sel'); delete c.dataset.placed; pool.appendChild(c); });
  }
  /* quick check */
  function revealCheck(s, picked) {
    $$('.rsm-opt', s).forEach(function (o) {
      if (o.dataset.ok === '1') o.classList.add('right');
      if (picked === o && o.dataset.ok !== '1') o.classList.add('wrong');
    });
    var w = $('.rsm-why', s); if (w) w.classList.add('on');
    s.dataset.step = stepsOf(s);
  }
  $$('.k-check').forEach(function (s) {
    $$('.rsm-opt', s).forEach(function (o) { o.addEventListener('click', function () { revealCheck(s, o); }); });
  });

  /* ── navigation ── */
  var countEl = $('#dk-count'), prog = $('#dk-prog'), notesEl = $('#dk-notes'), menu = $('#dk-menu');
  var SEC = cfg.sections;
  var secOf = function (s) { return +(s.dataset.sec || 0); };
  if (prog) {
    prog.innerHTML = SEC.map(function (n, i) { return '<button class="dk-sec" type="button" data-s="' + i + '" title="' + n + '"><span class="dk-rail"><span class="dk-fill"></span></span><span class="dk-lbl">' + n + '</span></button>'; }).join('');
    $$('.dk-sec', prog).forEach(function (b) { b.addEventListener('click', function () { var f = slides.findIndex(function (s) { return secOf(s) === +b.dataset.s; }); if (f > -1) go(f); }); });
  }
  if (menu) {
    $('.grid', menu).innerHTML = SEC.map(function (n, i) {
      return '<section><h5>' + n + '</h5>' + slides.map(function (s, j) { return secOf(s) === i ? '<button type="button" data-g="' + j + '"><span>' + pad(j + 1) + '</span>' + (s.dataset.ch || '') + '</button>' : ''; }).join('') + '</section>';
    }).join('');
    $$('button[data-g]', menu).forEach(function (b) { b.addEventListener('click', function () { go(+b.dataset.g); menu.classList.remove('on'); }); });
    menu.addEventListener('click', function (e) { if (e.target === menu) menu.classList.remove('on'); });
  }
  function mins(sec) { sec = +sec || 0; return sec >= 60 ? Math.round(sec / 60) + ' min' : sec + ' s'; }
  function renderNotes() {
    if (!notesEl) return; var s = slides[cur];
    $('p', notesEl).textContent = (s.dataset.dur ? '[' + mins(s.dataset.dur) + '] ' : '') + (s.dataset.notes || 'No note for this slide.');
  }
  function go(i) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (s, j) { s.classList.toggle('on', j === i); s.setAttribute('aria-hidden', j === i ? 'false' : 'true'); });
    cur = i; var s = slides[i], sec = secOf(s);
    if (countEl) countEl.innerHTML = '<b>' + pad(i + 1) + '</b> / ' + slides.length;
    if (prog) SEC.forEach(function (_, k) {
      var list = slides.filter(function (x) { return secOf(x) === k; }), idx = list.indexOf(s);
      var pct = k < sec ? 100 : k > sec ? 0 : (list.length ? (idx + 1) / list.length * 100 : 0);
      var el = $$('.dk-sec', prog)[k]; el.classList.toggle('now', k === sec); $('.dk-fill', el).style.width = pct + '%';
    });
    if (menu) $$('button[data-g]', menu).forEach(function (b) { b.classList.toggle('now', +b.dataset.g === i); });
    var w = $('.dk-wrap', s); if (w) w.scrollTop = 0;
    fit(s);
    renderNotes();
    try { history.replaceState(null, '', '#' + (i + 1)); } catch (e) { }
  }
  /* fit: a dense slide on a short screen scales down a little (never below 85%) instead of scrolling */
  function fit(s) {
    var f = $('.dk-fit', s), wr = $('.dk-wrap', s); if (!f || !wr) return;
    f.style.zoom = ''; if (innerWidth <= 760) return;
    var r = wr.clientHeight / wr.scrollHeight;
    if (r < 1) f.style.zoom = Math.max(0.85, r - 0.01).toFixed(3);
  }
  addEventListener('resize', function () { fit(slides[cur]); });
  function next() { var s = slides[cur]; if (stepOf(s) < stepsOf(s)) { setStep(s, stepOf(s) + 1); return; } go(cur + 1); }
  function prev() { var s = slides[cur]; if (stepOf(s) > 0) { setStep(s, stepOf(s) - 1); return; } go(cur - 1); }
  slides.forEach(function (s) { if (stepsOf(s)) setStep(s, 0); });

  addEventListener('keydown', function (e) {
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (k === 'Escape') { if (menu) menu.classList.remove('on'); if (brk && brk.classList.contains('on')) breakClose(); return; }
    if (k === 'm' || k === 'M') { if (menu) menu.classList.toggle('on'); return; }
    if (menu && menu.classList.contains('on')) return;
    if (k === 'n' || k === 'N') { if (notesEl && cfg.staff) { notesEl.classList.toggle('on'); renderNotes(); } return; }
    if (k === 'b' || k === 'B') { chime(); return; }
    if (k === 'f' || k === 'F') { if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen().catch(function () { }); return; }
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { e.preventDefault(); next(); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); prev(); }
    else if (k === 'Home') { e.preventDefault(); go(0); }
    else if (k === 'End') { e.preventDefault(); go(slides.length - 1); }
  });
  var nb = $('#dk-next'), pb = $('#dk-prev');
  if (nb) nb.addEventListener('click', next); if (pb) pb.addEventListener('click', prev);
  var bb = $('#dk-bell'); if (bb) bb.addEventListener('click', chime);
  var kb = $('#dk-break-btn'); if (kb) kb.addEventListener('click', breakOpen);
  var fb = $('#dk-fs'); if (fb) fb.addEventListener('click', function () { if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen().catch(function () { }); });
  var mb = $('#dk-menu-btn'); if (mb) mb.addEventListener('click', function () { menu.classList.toggle('on'); });
  var xs = null;
  addEventListener('touchstart', function (e) { xs = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', function (e) { if (xs === null) return; var dx = e.changedTouches[0].clientX - xs; if (Math.abs(dx) > 60) { dx < 0 ? next() : prev(); } xs = null; });

  var start = parseInt((location.hash || '').slice(1), 10);
  go(isNaN(start) ? 0 : start - 1);
  window.CodedDeck = { go: go, next: next, prev: prev, get current() { return cur; }, slides: slides, setStep: setStep };
})();
