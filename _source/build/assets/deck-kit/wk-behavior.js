
/* Workshop deck behavior on top of the kit: task timers with Reset, copy buttons, quick checks,
   and the break timer (the coffee button). Every countdown uses CodedPresenter.timer. */
(function () {
  var $ = function (q, c) { return (c || document).querySelector(q); };
  var $$ = function (q, c) { return [].slice.call((c || document).querySelectorAll(q)); };
  var P = window.CodedPresenter;
  var pad = function (n) { return String(n).padStart(2, '0'); };

  /* task timers: click the clock to start or pause, Reset to go back to the full time */
  $$('.cd-timer[data-wk-min]').forEach(function (el) {
    var mins = +el.getAttribute('data-wk-min') || 5;
    var t = P.timer({ el: el, seconds: mins * 60, warnAt: 60 });
    el.onclick = function () { if (t.done) { t.dismiss(); return; } t.toggle(); };
    var r = el.parentNode.querySelector('.wk-reset:not(.wk-plus)');
    if (r) r.onclick = function () { t.set(mins * 60); };
    var plus = el.parentNode.querySelector('.wk-plus');
    if (plus) plus.onclick = function () { t.add(60); };
  });

  /* copy a prompt exactly as written */
  function copyText(txt, done) {
    function fallback() {
      var ta = document.createElement('textarea'); ta.value = txt; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select();
      var ok = false; try { ok = document.execCommand('copy'); } catch (x) {}
      document.body.removeChild(ta); done(ok);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { done(true); }, fallback);
    else fallback();
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.wk-copy'); if (!b) return;
    e.stopPropagation();
    var t = b.parentNode.querySelector('.ptxt'); if (!t) return;
    copyText(t.innerText, function (ok) {
      b.textContent = ok ? 'Copied' : 'Select and copy';
      if (ok) b.setAttribute('data-done', '');
      setTimeout(function () { b.textContent = 'Copy'; b.removeAttribute('data-done'); }, 1500);
    });
  });

  /* quick checks: one answer, then the right one is shown with a short reason */
  function mcReset(slide) {
    $$('.wk-mcq', slide).forEach(function (box) {
      box.removeAttribute('data-revealed');
      $$('button', box).forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
    });
    $$('.wk-fb', slide).forEach(function (f) { f.innerHTML = ''; });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.wk-mcq button'); if (!b) return;
    var box = b.closest('.wk-mcq'); if (box.hasAttribute('data-revealed')) return;
    e.stopPropagation();
    box.setAttribute('data-revealed', ''); b.setAttribute('aria-pressed', 'true');
    var ok = b.hasAttribute('data-correct');
    var fb = box.parentNode.querySelector('.wk-fb');
    var h = document.createElement('span'); h.className = 'wk-fb-h ' + (ok ? 'ok' : 'no'); h.textContent = ok ? 'Correct' : 'Not quite';
    var p = document.createElement('span'); p.textContent = b.getAttribute('data-fb') || '';
    fb.innerHTML = ''; fb.appendChild(h); fb.appendChild(p);
  });
  var deck = $('#deck');
  if (deck) deck.addEventListener('cd:slide', function (e) { if (e.detail.slide.querySelector('.wk-mcq[data-revealed]')) mcReset(e.detail.slide); });

  /* break timer: dock button (cup) or key C */
  var pick = $('#breakPick'), ov = $('#breakOv'), clockEl = $('#boClock'), eye = $('#boEye'), back = $('#boBack');
  var bt = P.timer({ el: clockEl, seconds: 15 * 60, warnAt: 60, alarm: false,
    onTick: function (left, end) {
      back.innerHTML = (left <= 0 ? 'Time is up: ' : 'Back at ') + '<b>' + pad(end.getHours()) + ':' + pad(end.getMinutes()) + '</b>';
    },
    onDone: function () { eye.textContent = 'Break is over'; } });
  function openPick() { pick.hidden = false; var c = $('#bpCustom'); c.value = ''; setTimeout(function () { var f = $('button', pick); if (f) f.focus(); }, 30); }
  function closePick() { pick.hidden = true; }
  function startBreak(min) {
    min = Math.round(+min); if (!min || min < 1) return; if (min > 180) min = 180;
    closePick(); eye.textContent = min + (min === 1 ? ' minute' : ' minutes');
    bt.set(min * 60); ov.hidden = false; bt.start();
  }
  function endBreak() { bt.stop(); bt.dismiss(); ov.hidden = true; }
  $$('[data-min]', pick).forEach(function (b) { b.onclick = function () { startBreak(b.getAttribute('data-min')); }; });
  $('#bpGo').onclick = function () { startBreak($('#bpCustom').value); };
  $('#bpCustom').addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); startBreak(this.value); } });
  $('#bpCancel').onclick = closePick;
  pick.addEventListener('click', function (e) { if (e.target === pick) closePick(); });
  $('#boAdd').onclick = function () { eye.textContent = 'Break extended'; bt.add(300); if (!bt.running) bt.start(); };
  $('#boEnd').onclick = endBreak;
  var dock = $('.cd-dock');
  if (dock) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'wk-dock-break';
    b.title = 'Start a break timer (C)'; b.setAttribute('aria-label', 'Start a break timer');
    b.innerHTML = '<svg class="cd-ic"><use href="#i-cup"/></svg>';
    b.onclick = openPick; dock.appendChild(b);
  }
  addEventListener('keydown', function (e) {
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.metaKey || e.ctrlKey) return;
    if (e.key === 'Escape') { closePick(); if (!ov.hidden) endBreak(); }
    if (e.key === 'c' || e.key === 'C') { if (pick.hidden && ov.hidden) openPick(); else closePick(); }
  });
})();

