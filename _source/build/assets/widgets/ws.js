/* ===== WEAK vs STRONG OPENER (every .ws-slide on the deck) ===== */
function wsInit(slide){
  var $=function(r){return slide.querySelector('[data-r="'+r+'"]');};
  var segs=[].slice.call(slide.querySelectorAll('[data-r="strong-prompt"] .ws-seg'));
  var NP=segs.length, S_WEAK=1, S_WRES=2, S_P0=3, S_SRES=S_P0+NP, S_CMP=S_SRES+1, LAST=S_CMP+1;
  var st=0,T=[];
  function clr(){T.forEach(clearTimeout);T=[];} function later(f,ms){T.push(setTimeout(f,ms));}
  var weakTxt=slide.querySelector('.ws-weaktxt');
  var wps=[].slice.call(slide.querySelectorAll('.ws-wall p'));
  var rows=[].slice.call(slide.querySelectorAll('.ws-row')), lis=[].slice.call(slide.querySelectorAll('.ws-li'));
  var dots=[].slice.call(slide.querySelectorAll('[data-r="steps"] li'));
  var att=slide.querySelector('.ws-files').innerHTML;
  var punch=$('punch');
  function type(el,full,anim){if(!anim){el.textContent=full;return;}var i=0;el.textContent='';(function t(){i=Math.min(full.length,i+2);el.textContent=full.slice(0,i);if(i<full.length)later(t,16);})();}
  function sent(side,html){var b=$(side+'-sent');b.innerHTML=html+'<div>'+att+'</div>';b.style.display='block';}
  function render(anim){clr();
    var weak=$('weak'),strong=$('strong');
    var wTyped=st>=S_WEAK, wSent=st>=S_WRES;
    type(weakTxt, wTyped?weakTxt.getAttribute('data-full'):'', anim&&st===S_WEAK);
    $('weak-send').classList.toggle('ready', st===S_WEAK);
    $('weak-compose').classList.toggle('sent', wSent);
    weak.classList.toggle('typing', st===S_WEAK);
    if(wSent){var s=document.createElement('span');s.textContent=weakTxt.getAttribute('data-full');sent('weak',s.outerHTML);}else $('weak-sent').style.display='none';
    if(st===S_WRES&&anim){$('weak-think').style.display='flex';$('weak-ans').style.display='none';wps.forEach(function(p){p.classList.remove('on');});$('weak-flags').classList.remove('on');
      later(function(){$('weak-think').style.display='none';$('weak-ans').style.display='flex';
        wps.forEach(function(p,i){later(function(){p.classList.add('on');},550*i);});
        later(function(){$('weak-flags').classList.add('on');},550*wps.length+250);},1100);}
    else{$('weak-think').style.display='none';$('weak-ans').style.display=wSent?'flex':'none';
      wps.forEach(function(p){p.classList.toggle('on',wSent);});$('weak-flags').classList.toggle('on',wSent);}
    segs.forEach(function(sg,i){var on=st>=S_P0+i;sg.classList.toggle('on',on);var tx=sg.querySelector('.ws-txt');
      type(tx,on?tx.getAttribute('data-full'):'',anim&&st===S_P0+i);});
    var sSent=st>=S_SRES;
    strong.classList.toggle('typing', st>=S_P0&&st<S_SRES);
    $('strong-send').classList.toggle('ready', st===S_SRES-1);
    $('strong-compose').classList.toggle('sent', sSent);
    if(sSent){var h=segs.map(function(sg){var w=document.createElement('span');w.className='ws-seg on';w.setAttribute('data-k',sg.dataset.k);
        w.appendChild(sg.querySelector('.ws-tag').cloneNode(true));w.appendChild(document.createTextNode(sg.querySelector('.ws-txt').getAttribute('data-full')));return w.outerHTML;}).join(' ');sent('strong',h);}
    else $('strong-sent').style.display='none';
    if(st===S_SRES&&anim){$('strong-think').style.display='flex';$('strong-ans').style.display='none';
      rows.concat(lis).forEach(function(r){r.classList.remove('on');});$('strong-flags').classList.remove('on');
      later(function(){$('strong-think').style.display='none';$('strong-ans').style.display='flex';
        rows.forEach(function(r,i){later(function(){r.classList.add('on');},200*i);});
        lis.forEach(function(r,i){later(function(){r.classList.add('on');},200*rows.length+350*i);});
        later(function(){$('strong-flags').classList.add('on');},200*rows.length+350*lis.length+250);},1100);}
    else{$('strong-think').style.display='none';$('strong-ans').style.display=sSent?'flex':'none';
      rows.concat(lis).forEach(function(r){r.classList.toggle('on',sSent);});$('strong-flags').classList.toggle('on',sSent);}
    weak.classList.toggle('dim', st>=S_P0&&st<S_CMP); strong.classList.toggle('dim', st>=S_WEAK&&st<S_P0);
    weak.classList.toggle('lit', st>=S_WRES); strong.classList.toggle('lit', st>=S_SRES);
    $('score').classList.toggle('on', st===S_CMP);
    punch.classList.toggle('on', st>=LAST);
    slide.classList.toggle('ws-done', st>=LAST);
    dots.forEach(function(d,i){d.classList.toggle('done',i<st);d.classList.toggle('cur',i===st);});
  }
  function fwd(){if(st<LAST){st++;render(true);return true;}return false;}
  function back(){if(st>0){st--;render(false);return true;}return false;}
  function replay(){st=0;render(false);}
  function active(){return slide.classList.contains('active');}
  document.addEventListener('keydown',function(e){if(!active()||e.target.tagName==='INPUT')return;var k=e.key;
    if(k==='ArrowRight'||k===' '||k==='Enter'||k==='PageDown'){if(fwd()){e.preventDefault();e.stopImmediatePropagation();}}
    else if(k==='ArrowLeft'||k==='PageUp'){if(back()){e.preventDefault();e.stopImmediatePropagation();}}
    else if(k==='r'||k==='R'){replay();e.preventDefault();e.stopImmediatePropagation();}},true);
  document.addEventListener('click',function(e){if(!active())return;
    if(!slide.contains(e.target))return;
    if(e.target.closest('a'))return;
    if(!fwd())next();e.stopPropagation();},true);
  window.wkOnSlide.push(function(s){if(s===slide)replay();else punch.classList.remove('on');});
  replay();
}
[].slice.call(document.querySelectorAll('.ws-slide')).forEach(wsInit);
