/* ===== next-word widget (illustrative probabilities from the kit) ===== */
var LLM=__TREE__;
var llm={step:0,words:[],temp:1};
function llmOpts(){if(llm.step===0)return LLM.start.opts;var last=llm.words[llm.words.length-1];
  if(llm.step===1)return LLM[last]||LLM._2;return LLM[last]||LLM._3;}
function llmProbs(opts){var T=llm.temp,w=opts.map(function(o){return Math.pow(o[1],1/T);}),s=w.reduce(function(a,b){return a+b;},0);
  return opts.map(function(o,i){return {w:o[0],p:w[i]/s};});}
function llmRender(){var el=document.getElementById('llm');if(!el)return;
  var sent='<span class="pr">'+LLM.start.prompt+'</span>'+llm.words.map(function(w){return '<span class="tk">'+w+'</span>';}).join('');
  var done=llm.step>=3;
  document.getElementById('llm-sent').innerHTML=sent+(done?'':'<span class="cur"></span>');
  var box=document.getElementById('llm-opts');box.innerHTML='';
  document.getElementById('llm-q').textContent=done?'Sentence complete':'Step '+(llm.step+1)+' of 3 · what word comes next? Click one.';
  if(done){document.getElementById('llm-top').disabled=true;document.getElementById('llm-auto').disabled=true;return;}
  document.getElementById('llm-top').disabled=false;document.getElementById('llm-auto').disabled=false;
  var ps=llmProbs(llmOpts()).sort(function(a,b){return b.p-a.p;});
  ps.forEach(function(o){var b=document.createElement('button');b.type='button';b.className='llm-row'+(o.p<0.04?' low':'');b.dataset.w=o.w;
    b.innerHTML='<span class="w">'+o.w+'</span><span class="bar"><i style="width:'+Math.max(1,o.p*100).toFixed(1)+'%"></i></span><span class="pc">'+(o.p*100).toFixed(o.p<0.1?1:0)+'%</span>';
    box.appendChild(b);});}
function llmPick(w){var p=llmProbs(llmOpts()).filter(function(o){return o.w===w;})[0];llm.words.push(w);llm.step++;
  var n=document.getElementById('llm-note');
  if(p&&p.p<0.04)n.innerHTML='You picked a <b>very unlikely</b> word ('+(p.p*100).toFixed(1)+'%). The sentence still sounds confident. That is how a wrong answer can look right.';
  else if(llm.step>=3)n.innerHTML='Done. The model repeats this <b>one word at a time</b> for every sentence. It predicts likely words. It does not check facts.';
  else n.innerHTML='It added <b>'+w+'</b> ('+(p?(p.p*100).toFixed(0):'?')+'%). Now it predicts again, using the whole sentence so far.';
  llmRender();}
function llmSample(){var ps=llmProbs(llmOpts()),r=Math.random(),a=0;for(var i=0;i<ps.length;i++){a+=ps[i].p;if(r<=a)return ps[i].w;}return ps[ps.length-1].w;}
function llmTemp(v){llm.temp=+v;var lab=v<0.6?'focused':(v<=1.2?'balanced':'creative');
  document.getElementById('llm-tv').textContent=(+v).toFixed(1)+' · '+lab;llmRender();
  document.getElementById('llm-note').innerHTML=v<0.6?'Low temperature: the top word wins almost every time. <b>Predictable</b> answers.':(v>1.2?'High temperature: unlikely words get more chances. <b>More creative, more risk.</b>':'');}
window.llmReset=llmReset;
function llmReset(){llm.step=0;llm.words=[];var t=document.getElementById('llm-temp');if(t){t.value=1;llm.temp=1;document.getElementById('llm-tv').textContent='1.0 · balanced';}
  var n=document.getElementById('llm-note');if(n)n.innerHTML='';llmRender();}
(function(){var el=document.getElementById('llm');if(!el)return;
  el.addEventListener('click',function(e){e.stopPropagation();var r=e.target.closest('.llm-row');if(r&&llm.step<3)llmPick(r.dataset.w);});
  document.getElementById('llm-temp').addEventListener('input',function(e){llmTemp(e.target.value);});
  document.getElementById('llm-top').addEventListener('click',function(){if(llm.step<3){var ps=llmProbs(llmOpts()).sort(function(a,b){return b.p-a.p;});llmPick(ps[0].w);}});
  document.getElementById('llm-auto').addEventListener('click',function(){if(llm.step<3)llmPick(llmSample());});
  document.getElementById('llm-reset').addEventListener('click',llmReset);
  llmReset();})();
