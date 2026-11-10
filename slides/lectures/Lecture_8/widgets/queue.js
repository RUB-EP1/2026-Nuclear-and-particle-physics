'use strict';
const $=id=>document.getElementById(id);let run,playing=false,last=0,clock=200;
const ids=['mode','rate','adc','cpu','capacity','burst'];
function rebuild(){playing=false;$('play').textContent='Replay';clock=200;$('time').value=clock;
 run=DAQ.simulateQueue({rate:+$('rate').value,adc:+$('adc').value/1000,cpu:+$('cpu').value/1000,capacity:+$('capacity').value,burst:$('burst').value==='burst',mode:$('mode').value});
 for(const id of ['rate','adc','cpu','capacity'])$(id+'Value').textContent=$(id).value+({rate:' kHz',adc:' µs',cpu:' µs',capacity:''}[id]);
 $('capacity').disabled=run.mode==='dead';$('capacityLabel').classList.toggle('disabled',run.mode==='dead');draw();}
function draw(){
 const v=DAQ.sampleAt(run,clock),lost=v.adcDrop+v.fullDrop,pending=v.q+v.adcActive+v.cpuActive;
 $('out').textContent=clock?(v.done/clock).toFixed(2)+' kHz':'—';$('loss').textContent=v.arrived?(100*lost/v.arrived).toFixed(1)+'%':'—';
 $('busy').textContent=clock?(100*v.cpuBusy/clock).toFixed(1)+'%':'—';$('pending').textContent=pending;
 $('timeValue').textContent=clock.toFixed(1)+' ms';
 $('counts').textContent=`Arrived ${v.arrived} = completed ${v.done} + lost ${lost} + pending ${pending}. Lost while busy: ${v.adcDrop}; lost at full FIFO: ${v.fullDrop}.`;
 const dead=run.mode==='dead';
 $('theory').textContent=dead?(!run.burst?`Steady-rate prediction: r = R / (1 + Rτ) = ${(run.rate/(1+run.rate*(run.adc+run.cpu))).toFixed(2)} kHz; τ = ${Math.round(1000*(run.adc+run.cpu))} µs.`:'The steady Poisson dead-time formula is not the prediction for this burst pattern.'):`Service capacity = ${(1/run.cpu).toFixed(1)} kHz. ADC busy time = ${clock?(100*v.adcBusy/clock).toFixed(1):'0'}%.`;
 $('assumptions').textContent=dead?'Non-paralyzable model: an arrival while busy is lost and does not extend the busy period. Busy time τ = ADC time + processing time. No waiting slots.':'One ADC, one processor. ADC-busy arrivals are lost. At conversion completion, an idle processor takes the event; otherwise it waits in the FIFO, or is lost if full. Waiting slots exclude events in the ADC and processor.';
 let {c,w,h}=Plot.setup($('timeline'));const xs=[w*.11,w*.49,w*.87],y=h*.44;
 Plot.line(c,xs[0],y,xs[2],y,'#b7c7d4',3);
 if(dead){c.fillStyle=v.cpuActive?'#007dc5':'#eef3f7';c.fillRect(w*.26,y-30,w*.48,60);Plot.text(c,v.cpuActive?'BUSY · event being processed':'READY · waiting for arrival',w*.5,y+6,v.cpuActive?'#fff':'#526675','center');}
 else{
  for(const [j,label,on] of [[0,'ADC',v.adcActive],[2,'Processor',v.cpuActive]]){c.fillStyle=on?'#007dc5':'#edf3f7';c.fillRect(xs[j]-60,y-28,120,56);Plot.text(c,on?'Busy':'Ready',xs[j],y+6,on?'#fff':'#526675','center');Plot.text(c,label,xs[j],y+60,'#526675','center');}
  const cw=Math.min(13,w*.38/Math.max(1,run.capacity));
  for(let i=0;i<run.capacity;i++){c.fillStyle=i<v.q?'#007dc5':'#e4edf4';c.fillRect(xs[1]-run.capacity*cw/2+i*cw,y-22,cw-2,44);}
  Plot.text(c,`FIFO: ${v.q} / ${run.capacity} waiting`,xs[1],y+60,'#526675','center');
 }
 ({c,w,h}=Plot.setup($('chart')));const left=50,right=w-20,top=32,bottom=h-62,max=dead?1:Math.max(1,run.capacity);
 for(let i=0;i<=4;i++){const y=bottom-(bottom-top)*i/4;Plot.line(c,left,y,right,y);Plot.text(c,(max*i/4).toFixed(max>3?0:1),left-8,y+5,'#526675','right');}
 for(let t=0;t<=200;t+=50){const x=left+(right-left)*t/200;Plot.text(c,t.toString(),x,bottom+25,'#526675','center');}
 Plot.text(c,dead?'Busy state (0 / 1)':'FIFO occupancy (waiting events)',left,20);Plot.text(c,'Time [ms]',right,bottom+50,'#526675','right');
 c.strokeStyle='#007dc5';c.lineWidth=2;c.beginPath();let first=true,previous=0;
 for(const a of run.history){if(a.t>clock)break;const x=left+(right-left)*a.t/200,y=bottom-(bottom-top)*(dead?a.cpuActive:a.q)/max;if(first){c.moveTo(x,y);first=false;}else{c.lineTo(x,previous);c.lineTo(x,y);}previous=y;}
 c.lineTo(left+(right-left)*clock/200,previous);c.stroke();Plot.line(c,left+(right-left)*clock/200,top,left+(right-left)*clock/200,bottom,'#c86418',2);
 window.queueState={...v,clock,mode:run.mode};
}
ids.forEach(id=>$(id).addEventListener('input',rebuild));
$('time').addEventListener('input',()=>{clock=+$('time').value;playing=false;$('play').textContent='Replay';draw();});
$('play').onclick=()=>{playing=!playing;if(playing&&clock>=200)clock=0;$('play').textContent=playing?'Pause':'Replay';last=performance.now();};
$('reset').onclick=()=>{for(const [id,value] of Object.entries({mode:'buffer',rate:8,adc:20,cpu:100,capacity:8,burst:'steady'}))$(id).value=value;rebuild();};
function tick(now){if(playing){clock=Math.min(200,clock+(now-last)*.02);$('time').value=clock;draw();if(clock>=200){playing=false;$('play').textContent='Replay';}}last=now;requestAnimationFrame(tick);}
window.addEventListener('resize',draw);rebuild();requestAnimationFrame(tick);
