const assert=require('node:assert/strict');
const {simulateQueue,sampleAt,triggerSample,triggerStats}=require('../widgets/models.js');
function conserved(run){for(const v of run.history){assert.equal(v.arrived,v.done+v.adcDrop+v.fullDrop+v.q+v.adcActive+v.cpuActive);assert(v.q<=run.capacity);}}
for(const mode of ['dead','buffer'])for(const capacity of [0,1,8,32])for(const burst of [false,true])conserved(simulateQueue({mode,capacity,burst}));
let v=simulateQueue({rate:0}).final;assert.equal(v.arrived,0);assert.equal(v.done,0);
v=simulateQueue({input:[0,1,2],adc:0,cpu:0.1,duration:3}).final;assert.equal(v.done,3);assert.equal(v.adcDrop+v.fullDrop,0);
// An arrival exactly at completion is accepted; busy arrivals do not prolong dead time.
v=simulateQueue({input:[0,.05,.1],mode:'dead',adc:0,cpu:.1,duration:1}).final;assert.equal(v.done,2);assert.equal(v.adcDrop,1);
// FIFO capacity excludes service; a slot becomes available at CPU completion.
v=simulateQueue({input:[0,.01,.02],adc:0,cpu:1,capacity:1,duration:3}).final;assert.equal(v.done,2);assert.equal(v.fullDrop,1);
v=simulateQueue({input:[0,.01,.02],adc:.05,cpu:.1,duration:1}).final;assert.equal(v.adcDrop,2);assert.equal(v.done,1);
const long=simulateQueue({rate:8,duration:20000,mode:'dead',adc:.02,cpu:.1});assert(Math.abs(long.final.done/20000-8/(1+8*.12))<.04);
const short=simulateQueue({input:[0],adc:.05,cpu:1,duration:2});assert.equal(sampleAt(short,.025).adcActive,1);assert(Math.abs(sampleAt(short,.025).adcBusy-.025)<1e-10);
const input=Array.from({length:100},(_,i)=>i*.05);assert(simulateQueue({input,adc:0,cpu:.1,capacity:32,duration:5}).final.fullDrop>0);
const sample=triggerSample();assert.deepEqual(sample,triggerSample());
assert.equal(triggerStats(sample,{threshold:0}).effS,1);assert.equal(triggerStats(sample,{threshold:0}).effB,1);
assert.equal(triggerStats(sample,{threshold:Infinity}).purity,null);
const a=triggerStats(sample,{threshold:4}),b=triggerStats(sample,{threshold:8});assert(b.total<a.total);assert(b.effS<a.effS);assert(b.purity>a.purity);
assert.equal(triggerStats(sample,{threshold:0,signalRate:100,backgroundRate:900,eventKB:200}).bandwidth,200);
assert.equal(triggerStats(sample,{signalRate:0,backgroundRate:0}).purity,null);
console.log('Queue conservation, boundary cases, dead-time rate, deterministic samples and trigger limits passed.');
