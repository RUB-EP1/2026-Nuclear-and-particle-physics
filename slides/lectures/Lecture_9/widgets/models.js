/* Deterministic teaching models. Rates: kHz (events/ms), times: ms. */
(function(root){
'use strict';
function rng(seed=821){let s=seed>>>0;return()=>{s=(1664525*s+1013904223)>>>0;return (s+0.5)/4294967296;};}
function arrivals(rate,duration,burst=false,seed=821){
 const r=rng(seed), out=[];if(rate<=0)return out;
 // Thinning: same mean rate. First fifth of every 20 ms has 4x rate; remainder 0.25x.
 const peak=rate*(burst?4:1);let t=0;
 while((t+=-Math.log(r())/peak)<duration){if(!burst||r()<(t%20<4?1:0.0625))out.push(t);}
 return out;
}
function simulateQueue({rate=8,duration=200,adc=0.02,cpu=0.1,capacity=8,burst=false,mode='buffer',seed=821,input=null}={}){
 if(duration<=0||adc<0||cpu<=0||capacity<0||rate<0)throw Error('Invalid queue parameters');
 const times=input===null?arrivals(rate,duration,burst,seed):input.filter(t=>t>=0&&t<duration);
 if(times.some((t,i)=>i&&t<times[i-1]))throw Error('Arrivals must be ordered');
 let i=0,t=0,adcEnd=Infinity,cpuEnd=Infinity,q=0,arrived=0,adcDrop=0,fullDrop=0,done=0,adcBusy=0,cpuBusy=0;
 const history=[];
 function snap(){history.push({t,arrived,adcDrop,fullDrop,done,q,adcActive:Number(adcEnd<Infinity),cpuActive:Number(cpuEnd<Infinity),adcBusy,cpuBusy});}
 snap();
 function startCPU(){cpuEnd=t+cpu;}
 while(true){
  const next=Math.min(i<times.length?times[i]:Infinity,adcEnd,cpuEnd);
  if(next>duration||!Number.isFinite(next))break;
  if(adcEnd<Infinity)adcBusy+=next-t;if(cpuEnd<Infinity)cpuBusy+=next-t;t=next;
  // Completion precedes arrivals at an identical timestamp.
  if(cpuEnd===t){done++;cpuEnd=Infinity;if(q){q--;startCPU();}}
  if(adcEnd===t){adcEnd=Infinity;if(cpuEnd===Infinity)startCPU();else if(q<capacity)q++;else fullDrop++;}
  if(i<times.length&&times[i]===t){
   arrived++;i++;
   if(mode==='dead'){
    if(cpuEnd<Infinity)adcDrop++;
    else cpuEnd=t+adc+cpu; // one non-paralyzable busy stage; ADC time included
   }else if(adcEnd<Infinity)adcDrop++;
   else if(adc>0)adcEnd=t+adc;
   else if(cpuEnd===Infinity)startCPU();else if(q<capacity)q++;else fullDrop++;
  }
  snap();
 }
 if(adcEnd<Infinity)adcBusy+=duration-t;if(cpuEnd<Infinity)cpuBusy+=duration-t;t=duration;snap();
 return {history,final:history.at(-1),rate,duration,adc,cpu,capacity,mode,burst};
}
function sampleAt(run,t){let a=0,b=run.history.length-1;while(a<b){let m=Math.ceil((a+b)/2);if(run.history[m].t<=t)a=m;else b=m-1;}
 const v={...run.history[a]},dt=t-v.t;v.adcBusy+=dt*v.adcActive;v.cpuBusy+=dt*v.cpuActive;v.t=t;return v;}
function triggerSample(n=30000,seed=809){const r=rng(seed),signal=[],background=[];
 while(signal.length<n){const z=Math.sqrt(-2*Math.log(r()))*Math.cos(2*Math.PI*r()),x=8+2*z;if(x>=0)signal.push(x);}
 for(let i=0;i<n;i++)background.push(-1.5*Math.log(r()));return{signal,background};}
function triggerStats(sample,{threshold=7,signalRate=100,backgroundRate=100000,eventKB=200,budgetMB=200}={}){
 const effS=sample.signal.filter(x=>x>=threshold).length/sample.signal.length;
 const effB=sample.background.filter(x=>x>=threshold).length/sample.background.length;
 const s=effS*signalRate,b=effB*backgroundRate,total=s+b,bandwidth=total*eventKB/1000;
 return{effS,effB,s,b,total,purity:total?s/total:null,bandwidth,budgetMB,within:bandwidth<=budgetMB};
}
const api={rng,arrivals,simulateQueue,sampleAt,triggerSample,triggerStats};
if(typeof module!=='undefined')module.exports=api;else root.DAQ=api;
})(typeof window!=='undefined'?window:globalThis);
