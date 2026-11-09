/* ===== PROMPT PLAYER: one part per press (every .pp-slide on the deck) ===== */
function ppInit(slide){
  var NPARTS=slide.querySelectorAll('[data-r="prompt"] .pp-seg').length, LAST=NPARTS+3;   /* parts, then Send, Result, Decision */
  var st=0, timers=[];
  var $=function(r){return slide.querySelector('[data-r="'+r+'"]');};
  var segs=[].slice.call(slide.querySelectorAll('[data-r="prompt"] .pp-seg'));
  var rows=[].slice.call(slide.querySelectorAll('.pp-row'));
  var recos=[].slice.call(slide.querySelectorAll('[data-r="reco"] li'));
  var lis=[].slice.call(slide.querySelectorAll('[data-r="steps"] li'));
  function clear(){timers.forEach(clearTimeout);timers=[];}
  function later(fn,ms){timers.push(setTimeout(fn,ms));}
  function typeIn(el,instant){var full=el.getAttribute('data-full');
    if(instant){el.textContent=full;return;}
    var i=0;el.textContent='';(function t(){i=Math.min(full.length,i+2);el.textContent=full.slice(0,i);if(i<full.length)later(t,14);})();}
  function render(animate){clear();
    segs.forEach(function(sg,i){var on=st>i;sg.classList.toggle('on',on);var tx=sg.querySelector('.pp-txt');
      if(on){typeIn(tx,!(animate&&st===i+1));}else tx.textContent='';});
    $('empty').style.display=st===0?'block':'none';
    $('send').classList.toggle('ready',st===NPARTS);
    var sent=st>NPARTS;
    $('compose').classList.toggle('sent',sent);
    $('prompt').querySelector('.pp-caret').style.display=sent?'none':'inline-block';
    var box=$('sent');
    if(sent){box.innerHTML='';segs.forEach(function(sg,i){var w=document.createElement('span');w.className='pp-seg on';w.setAttribute('data-k',i);
        w.appendChild(sg.querySelector('.pp-tag').cloneNode(true));w.appendChild(document.createTextNode(sg.querySelector('.pp-txt').getAttribute('data-full')));
        if(i)box.appendChild(document.createTextNode(' '));box.appendChild(w);});
      var fl=slide.querySelector('.pp-files');if(fl&&fl.children.length){var fc=document.createElement('div');fc.className='pp-sfiles';fc.innerHTML=fl.innerHTML;box.appendChild(fc);}
      box.style.display='block';}
    else box.style.display='none';
    var showAns=st>=NPARTS+1;
    if(st===NPARTS+1&&animate){$('think').style.display='flex';$('ans').style.display='none';
      rows.forEach(function(r){r.classList.remove('on');});recos.forEach(function(r){r.classList.remove('on');});
      later(function(){$('think').style.display='none';$('ans').style.display='flex';
        rows.forEach(function(r,i){later(function(){r.classList.add('on');},180*i);});},1100);}
    else{$('think').style.display='none';$('ans').style.display=showAns?'flex':'none';
      rows.forEach(function(r){r.classList.toggle('on',showAns);});}
    if(st>=NPARTS+2){recos.forEach(function(r,i){if(animate&&st===NPARTS+2){r.classList.remove('on');later(function(){r.classList.add('on');},260*i);}else r.classList.add('on');});}
    else if(!(st===NPARTS+1&&animate))recos.forEach(function(r){r.classList.remove('on');});
    $('decide').classList.toggle('on',st>=LAST);
    slide.classList.toggle('pp-done',st>=LAST);
    lis.forEach(function(li,i){li.classList.toggle('done',st>i+1||(st===LAST&&i===LAST-1));li.classList.toggle('cur',st===i+1&&st!==LAST);});
    if(st===LAST)lis[LAST-1].classList.add('cur');
    $('next').textContent=st>=LAST?'Next slide ›':'Next ›';
  }
  function fwd(){if(st<LAST){st++;render(true);return true;}return false;}
  function back(){if(st>0){st--;render(false);return true;}return false;}
  function replay(){st=0;render(false);}
  function active(){return slide.classList.contains('active');}
  document.addEventListener('keydown',function(e){if(!active()||e.target.tagName==='INPUT')return;
    var k=e.key;
    if(k==='ArrowRight'||k===' '||k==='Enter'||k==='PageDown'){if(fwd()){e.preventDefault();e.stopImmediatePropagation();}}
    else if(k==='ArrowLeft'||k==='PageUp'){if(back()){e.preventDefault();e.stopImmediatePropagation();}}
    else if(k==='r'||k==='R'){replay();e.preventDefault();e.stopImmediatePropagation();}
  },true);
  document.addEventListener('click',function(e){if(!active()||!slide.contains(e.target))return;
    if(e.target.closest('[data-r="back"]')){back();}else if(e.target.closest('[data-r="replay"]')){replay();}
    else if(e.target.closest('[data-r="next"]')){if(!fwd())next();}
    else if(e.target.closest('a,.wk-copy'))return;
    else{if(!fwd())next();}
    e.stopPropagation();},true);
  window.wkOnSlide.push(function(s){if(s===slide)replay();});
  replay();
}
[].slice.call(document.querySelectorAll('.pp-slide')).forEach(ppInit);
