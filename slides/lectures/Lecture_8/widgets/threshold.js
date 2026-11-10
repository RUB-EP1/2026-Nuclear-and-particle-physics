'use strict';
const $=id=>document.getElementById(id),sample=DAQ.triggerSample();
const binsS=Array(41).fill(0),binsB=Array(41).fill(0);
for(const x of sample.signal)binsS[Math.min(40,Math.floor(x*2))]++;
for(const x of sample.background)binsB[Math.min(40,Math.floor(x*2))]++;
function draw(){
 const threshold=+$('cut').value,signalRate=+$('signal').value,backgroundRate=+$('background').value*1000,eventKB=+$('size').value,budgetMB=+$('budget').value;
 const v=DAQ.triggerStats(sample,{threshold,signalRate,backgroundRate,eventKB,budgetMB});
 for(const [id,text] of Object.entries({cut:threshold.toFixed(1)+' GeV/c',signal:signalRate+' Hz',background:backgroundRate/1000+' kHz',size:eventKB+' kB',budget:budgetMB+' MB/s'}))$(id+'Value').textContent=text;
 $('effS').textContent=(100*v.effS).toFixed(1)+'%';$('effB').textContent=(100*v.effB).toFixed(2)+'%';$('purity').textContent=v.purity===null?'undefined':(100*v.purity).toFixed(1)+'%';$('output').textContent=v.total>=1000?(v.total/1000).toFixed(2)+' kHz':v.total.toFixed(1)+' Hz';
 $('signalOut').textContent=`Signal kept: ${v.s.toFixed(1)} Hz`;$('backgroundOut').textContent=`Background kept: ${v.b.toFixed(1)} Hz`;
 $('budgetStatus').textContent=`${v.bandwidth.toFixed(1)} MB/s required / ${budgetMB} MB/s available · ${v.within?'within budget':'over budget'}`;$('budgetStatus').className='budget '+(v.within?'under':'over');
 let {c,w,h}=Plot.setup($('chart'));const left=68,right=w-20,top=35,bottom=h-47;
 const x=p=>left+(right-left)*p/22, y=r=>bottom-(bottom-top)*(Math.log10(Math.max(.1,r))+1)/7;
 c.fillStyle='#f0f3f6';c.fillRect(left,top,x(threshold)-left,bottom-top);
 for(let k=-1;k<=6;k++){const yy=y(10**k);Plot.line(c,left,yy,right,yy);Plot.text(c,10**k>=1000?(10**k/1000)+'k':String(10**k),left-9,yy+5,'#526675','right');}
 Plot.text(c,'Rate [Hz / bin] · log scale',left,20);
 for(let p=0;p<=20;p+=4)Plot.text(c,p===20?'20+':String(p),x(p),bottom+24,'#526675','center');
 Plot.text(c,'pT [GeV/c]',right,bottom+44,'#526675','right');
 for(const [bins,rate,color] of [[binsB,backgroundRate,'#c86418'],[binsS,signalRate,'#007dc5']]){
  c.strokeStyle=color;c.lineWidth=2.5;c.beginPath();for(let i=0;i<41;i++){const a=x(i/2),b=x((i+1)/2),yy=y(bins[i]*rate/30000);if(!i)c.moveTo(a,yy);else c.lineTo(a,yy);c.lineTo(b,yy);}c.stroke();
 }
 Plot.line(c,x(threshold),top,x(threshold),bottom,'#bd3249',2);Plot.text(c,'cut '+threshold.toFixed(1),Math.min(right-45,Math.max(left+50,x(threshold))),top+18,'#bd3249','center');
 ({c,w,h}=Plot.setup($('bandwidth')));const max=Math.max(budgetMB*1.4,v.bandwidth*1.1,1),trackW=w-40;
 c.fillStyle='#edf3f7';c.fillRect(20,30,trackW,25);c.fillStyle=v.within?'#007dc5':'#bd3249';c.fillRect(20,30,trackW*v.bandwidth/max,25);
 const bx=20+trackW*budgetMB/max;Plot.line(c,bx,18,bx,65,'#152d40',2);Plot.text(c,'budget',Math.min(w-45,Math.max(48,bx)),86,'#526675','center');
 window.thresholdState={...v,threshold};
}
for(const id of ['cut','signal','background','size','budget'])$(id).addEventListener('input',draw);
$('reset').onclick=()=>{for(const [id,v]of Object.entries({cut:7,signal:100,background:100,size:200,budget:200}))$(id).value=v;draw();};
window.addEventListener('resize',draw);draw();
