"""Analytic teaching figures and plots of the exact widget model; no measured data."""
from pathlib import Path
import os,json,math,subprocess
ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'tmp/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
B='#007dc5'; O='#cf741b'; R='#bd3249'; G='#268565'; GR='#607382'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'axes.labelsize':18,'axes.titlesize':20,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#b8c7d2','grid.color':'#e0e8ed','svg.fonttype':'none','lines.linewidth':3,'legend.frameon':False,'figure.facecolor':'white'})
OUT=ROOT/'figures'
def plot(title=None):
 f,a=plt.subplots(figsize=(10.6,6.5),layout='constrained');a.grid(alpha=.75);a.set_axisbelow(True)
 if title:a.set_title(title,loc='left',pad=16)
 return f,a
def save(f,name):
 f.savefig(OUT/(name+'.svg'));plt.close(f)
t=np.linspace(0,200,1200);pulse=lambda x:np.where(x>30,600*((np.maximum(x-30,0)/22)**2)*np.exp(2-2*np.maximum(x-30,0)/22),0)
rng=np.random.default_rng(8)
f,a=plot('An electrical pulse, not a particle label')
a.plot(t,pulse(t)+rng.normal(0,9,len(t)),color=B,lw=1.8,label='Voltage at the front end');a.plot(t,pulse(t),color=O,lw=2,label='Ideal pulse');a.set(xlabel='Time [ns]',ylabel='Amplitude [mV]',ylim=(-55,710));a.legend();save(f,'signal-pulse')
f,a=plot('Sampling in time; quantization in amplitude')
a.plot(t,pulse(t),color='#9caab4',lw=2,label='Analogue pulse');ts=np.arange(0,201,10);q=np.clip(np.round(pulse(ts)/100),0,7)*100
a.step(ts,q,where='mid',color=B,label='3-bit values (0–7)');a.scatter(ts,q,color=B,s=40,zorder=3);a.set(xlabel='Time [ns]',ylabel='Amplitude [mV]',yticks=np.arange(0,701,100),ylim=(-35,760));a.legend(loc='upper right');save(f,'adc-sampling')
f,a=plot('Arrival order is not event identity')
events=[(1041,B,[1,3,2]),(1042,O,[2,5,4]),(1043,G,[4,6,7])]
for eid,col,ts in events:
 for y,x in enumerate(ts):a.scatter(x,y,color=col,s=250,marker='s');a.text(x,y+.18,str(eid),ha='center',color=col,fontsize=16)
a.set(xlim=(.4,7.7),ylim=(2.6,-.4),yticks=[0,1,2],yticklabels=['Tracker','Calorimeter','Muon system'],xlabel='Fragment arrival time [arbitrary units]');a.grid(axis='y');save(f,'event-fragments')
f,a=plot('A changing gain can imitate changing energy')
x=np.linspace(0,8,81);gain=1+.025*x;obs=100*gain
a.plot(x,obs,color=R,label='Fixed calibration');a.plot(x,obs/gain,color=B,label='Corrected using recorded gain');a.set(xlabel='Run time [hours]',ylabel='Reconstructed energy [GeV]',ylim=(94,125));a.legend();save(f,'gain-drift')
f,a=plot('Continuous recording adds up')
x=np.linspace(0,24,100)
for rate,col in [(1,B),(.2,O)]:a.plot(x,rate*x*3.6,color=col,label=f'{rate:g} GB/s')
a.scatter(24,86.4,color=B);a.annotate('86.4 TB',(24,86.4),xytext=(17,90),color=B);a.set(xlabel='Recording time [hours]',ylabel='Stored data [TB]',xlim=(0,25),ylim=(0,101));a.legend();save(f,'data-per-day')
f,a=plot('Three stages; a new event every time unit')
for event,col in enumerate([B,O,G,R]):
 for stage in range(3):a.broken_barh([(event+stage,.92)],(stage-.3,.6),facecolor=col);a.text(event+stage+.46,stage,chr(65+event),ha='center',va='center',color='white',weight='bold')
a.set(xlim=(-.1,6.3),ylim=(2.7,-.7),yticks=[0,1,2],yticklabels=['Stage 1','Stage 2','Stage 3'],xlabel='Time [arbitrary units]');a.grid(axis='x');save(f,'pipeline-timing')
f,a=plot('Lost arrivals do not extend the busy interval')
arr=[.5,1,1.8,3,3.4,5.2,6,7.7,8.2];end=-1
for x in arr:
 accepted=x>=end
 if accepted:end=x+2;a.broken_barh([(x,2)],(-.23,.46),facecolor=B,alpha=.2)
 a.vlines(x,0,1.0 if accepted else .65,color=B if accepted else R,lw=3);a.scatter(x,1.0 if accepted else .65,color=B if accepted else R,marker='o' if accepted else 'x',s=90)
a.plot([],[],color=B,marker='o',label='Accepted');a.plot([],[],color=R,marker='x',label='Lost while busy');a.set(xlabel='Time [arbitrary units]',yticks=[],xlim=(0,11),ylim=(-.4,1.7));a.legend(ncol=2,loc='upper left');a.text(3.9,-.13,'busy time τ = 2',fontsize=17,color=B);save(f,'deadtime-timeline')
# Export the same event-model outputs used by the interactive queue.
js="""const fs=require('fs'),m=require('./widgets/models.js');const history=[0,8].map(capacity=>m.simulateQueue({rate:8,adc:0,cpu:.1,capacity,burst:true,duration:60}));const sweep=[8,15].map(rate=>({rate,points:[0,1,2,4,8,16,32,64].map(capacity=>{const a=m.simulateQueue({rate,adc:0,cpu:.1,capacity,duration:2000}).final;return{capacity,loss:100*(a.adcDrop+a.fullDrop)/a.arrived}})}));console.log(JSON.stringify({history,sweep}));"""
d=json.loads(subprocess.check_output(['node','-e',js],cwd=ROOT))
f,axes=plt.subplots(2,1,figsize=(10.6,6.5),layout='constrained',sharex=True)
for a,run in zip(axes,d['history']):
 h=run['history'];times=[z['t'] for z in h];out=[z['done'] for z in h];a.step(times,out,where='post',color=B);a.step(times,[z['arrived'] for z in h],where='post',color='#9aabb6',label='Arrived');a.set_ylabel('Event count');a.grid(alpha=.6);last=run['final'];a.set_title(f"{run['capacity']} waiting slots: {last['fullDrop']} lost",loc='left')
axes[0].legend();axes[-1].set_xlabel('Time [ms]');axes[-1].text(2,400,'Blue: completed\nGrey: arrived',fontsize=15,color=GR);save(f,'buffer-bursts')
f,a=plot('More memory does not create service capacity')
for run,col in zip(d['sweep'],[B,R]):a.plot([z['capacity'] for z in run['points']],[z['loss'] for z in run['points']],marker='o',color=col,label=f"{run['rate']} kHz input")
a.set(xlabel='FIFO waiting slots',ylabel='Lost arrivals [%]',ylim=(-1,65));a.legend();a.text(22,45,'Processor capacity: 10 kHz\nADC time: 0 (isolate buffering)',fontsize=16,color=GR);save(f,'buffer-capacity')
x=np.linspace(0,18,400);effS=np.array([.5*math.erfc((v-8)/math.sqrt(8)) for v in x])/(.5*math.erfc(-8/math.sqrt(8)));effB=np.exp(-x/1.5)
f,a=plot('The same cut treats two spectra differently')
a.plot(x,effS,color=B,label='Signal efficiency');a.plot(x,effB,color=O,label='Background acceptance');a.plot(x,100*effS/(100*effS+1e5*effB),color=G,ls='--',label='Selected signal fraction');a.set(xlabel='Threshold [GeV/c]',ylabel='Fraction',ylim=(0,1.05));a.legend();save(f,'efficiency-purity')
f,a=plot('Rare signal sits under a much larger background')
s=100/(2*np.sqrt(2*np.pi)*(.5*math.erfc(-8/math.sqrt(8))))*np.exp(-.5*((x-8)/2)**2);b=1e5/1.5*np.exp(-x/1.5)
a.semilogy(x,b,color=O,label='Background: 100 kHz');a.semilogy(x,s,color=B,label='Signal: 100 Hz');a.axvline(7,color=R,ls='--',label='Threshold: 7 GeV/c');a.axvspan(0,7,color='#dce4e9',alpha=.4);a.set(xlabel='Candidate pT [GeV/c]',ylabel='Rate density [Hz / (GeV/c)]',ylim=(.05,2e5));a.legend();save(f,'threshold-spectra')
f,a=plot('A threshold reshapes the recorded spectrum')
density=np.exp(-.5*((x-8)/2)**2)/(2*np.sqrt(2*np.pi)*(.5*math.erfc(-8/math.sqrt(8))));a.plot(x,density,color='#7c8c97',label='Before selection');a.fill_between(x,0,density,where=x>=7,color=B,alpha=.25);a.plot(x,np.where(x>=7,density,np.nan),color=B,label='Kept (not renormalized)');a.axvline(7,color=R,ls='--');a.set(xlabel='Candidate pT [GeV/c]',ylabel='Probability density [(GeV/c)⁻¹]',ylim=(0,.24));a.legend();save(f,'selection-bias')
f,a=plot('A busy stage saturates')
x=np.linspace(0,50,300);a.plot(x,x/(1+.12*x),color=B,label='Non-paralyzable output');a.plot(x,x,color='#9aabb6',ls=':',label='No dead time');a.axhline(1/.12,color=R,ls='--',label='Limit: 1/τ = 8.33 kHz');a.set(xlabel='Input rate [kHz]',ylabel='Output rate [kHz]',ylim=(0,12));a.legend(loc='lower right');save(f,'deadtime-rate')
# Source-derived figure crop: complete physical and logical panels from Neufeld p16.
im=Image.open(ROOT.parents[2]/'reference/lecture-notes/figures/neufeld-daq-16.png');w,h=im.size
im.crop((int(w*.13),int(h*.43),int(w*.88),int(h*.845))).save(OUT/'neufeld-readout-chain.png')


# Fixed-latency pipeline: every 25 ns crossing waits 2.5 us for the Level-1 decision.
f,a=plot('Every crossing waits for its Level-1 decision')
lat=2.5;dt=.025;n=161;acc={20,61,95,140}
for i in range(n):
 t0=i*dt;col=B if i in acc else '#c3ced6'
 a.plot([t0,t0+lat],[i,i],color=col,lw=2.6 if i in acc else .9,solid_capstyle='butt')
 if i in acc:a.scatter(t0+lat,i,color=B,s=60,zorder=3)
a.axvline(3.5,color=R,ls='--',lw=2);a.text(3.58,8,'at any moment:\n100 crossings stored',color=R,fontsize=16)
a.annotate('',xy=(61*dt+lat,61),xytext=(61*dt,61),arrowprops=dict(arrowstyle='<->',color=GR,lw=1.6),annotation_clip=False)
a.text(61*dt+lat/2,66,'decision latency 2.5 µs',ha='center',color=GR,fontsize=16)
a.plot([],[],color=B,lw=3,marker='o',label='Accepted: read out');a.plot([],[],color='#c3ced6',lw=3,label='Rejected: slot released')
a.set(xlabel='Time [µs]',ylabel='Crossing number (one per 25 ns)',xlim=(0,6.8),ylim=(-3,n+4));a.legend(loc='upper left');save(f,'pipeline-buffer')
# Tag and probe: invariant-mass spectra of tag-probe pairs, split by the probe's trigger decision.
rng=np.random.default_rng(91);m=np.arange(70,110.01,1.0);c=.5*(m[1:]+m[:-1])
def zshape(x):return np.exp(-.5*((x-91.19)/2.6)**2)/(2.6*np.sqrt(2*np.pi))
def bshape(x):return np.exp(-(x-70)/25)/(25*(1-np.exp(-40/25)))
f,axes=plt.subplots(1,2,figsize=(10.6,6.5),layout='constrained',sharey=False)
for a,(lab,ns,nb) in zip(axes,[('Probe passes',18400,600),('Probe fails',1600,900)]):
 sig=ns*zshape(c);bkg=nb*bshape(c);obs=rng.poisson(sig+bkg)
 a.fill_between(c,0,bkg,step='mid',color=O,alpha=.3,label='Background');a.plot(c,sig+bkg,color=B,label='Signal + background')
 a.errorbar(c,obs,yerr=np.sqrt(obs),fmt='o',ms=4,color='#26323a',label='Pseudo-data');a.set_title(f'{lab}: N_sig = {ns:,}',loc='left',fontsize=18)
 a.set(xlabel='Tag–probe mass [GeV]',ylim=(0,None));a.grid(alpha=.6)
axes[0].set_ylabel('Pairs / GeV');axes[0].legend(loc='upper left',fontsize=13)
axes[1].text(71,250,'ε = 18,400 / 20,000\n   = 0.92',fontsize=18,color=B,va='top');save(f,'tag-and-probe')
# Threshold versus prescale for one path and a 100 Hz allocation.
f,a=plot('Two ways to meet a 100 Hz allocation')
x=np.linspace(10,60,300);rate=lambda q:2e4*(q/10)**-4;P=40
a.semilogy(x,rate(x),color=B,label='Path passing rate');a.semilogy(x,rate(x)/P,color=O,ls='--',label=f'Same path, prescale P = {P}');a.axhline(100,color=R,ls=':',label='Allocation: 100 Hz')
ca=10*200**.25;a.scatter([ca,15],[100,rate(15)/P],color=[B,O],s=110,zorder=4)
a.annotate(f'A: threshold {ca:.0f} GeV, P = 1',(ca,100),xytext=(ca+1,250),color=B,fontsize=16)
a.annotate('B: threshold 15 GeV, P = 40',(15,rate(15)/P),xytext=(16.5,150),color=O,fontsize=16)
a.set(xlabel='Threshold [GeV]',ylabel='Rate [Hz]',ylim=(5,3e4));a.legend(loc='upper right');save(f,'prescale-threshold')
# Synchrotron radiation: energy lost per turn, Delta E = C_gamma E^4 / rho (C_gamma = 8.85e-5 m/GeV^3 for electrons).
f,a=plot('Energy radiated per turn in a 27 km ring')
E=np.geomspace(1,1e4,300);me_mp=0.000510999/0.938272
lossE=lambda e:8.85e-5*e**4/3096;lossP=lambda e:8.85e-5*e**4/2804*me_mp**4
a.loglog(E,lossE(E),color=R,label='Electrons (ρ = 3.1 km)');a.loglog(E,lossP(E),color=B,label='Protons (ρ = 2.8 km)');a.loglog(E,E,color='#9aabb6',ls=':',label='Entire beam energy')
a.scatter([104.5,7000],[lossE(104.5),lossP(7000)],color=[R,B],s=90,zorder=3)
a.annotate(f'LEP2, 104.5 GeV: {lossE(104.5):.1f} GeV/turn',(104.5,lossE(104.5)),xytext=(110,1e-2),color=R,fontsize=16)
a.annotate(f'LHC, 7 TeV: {lossP(7000)*1e6:.1f} keV/turn',(7000,lossP(7000)),xytext=(150,3e-7),color=B,fontsize=16)
a.set(xlabel='Beam energy [GeV]',ylabel='Energy lost per turn [GeV]',ylim=(1e-12,1e5));a.legend(loc='upper left');save(f,'synchrotron-loss')
# Time of flight over 5 m: arrival-time peaks at 2 GeV/c and separation versus momentum.
L=5.0;sig=.1;mass={'π':.13957,'K':.49368,'p':.93827};cols={'π':B,'K':O,'p':G}
tof=lambda p,mm:L/.299792458*np.sqrt(1+(mm/p)**2)
f,(a1,a2)=plt.subplots(1,2,figsize=(10.6,6.5),layout='constrained')
tt=np.linspace(-.4,2.3,600)
for k,mm in mass.items():
 mu=tof(2,mm)-L/.299792458;a1.plot(tt,np.exp(-.5*((tt-mu)/sig)**2),color=cols[k],label=k);a1.text(mu,1.05,k,ha='center',color=cols[k],fontsize=18)
a1.set(xlabel='t − L/c [ns]',ylabel='Relative counts',ylim=(0,1.2),yticks=[]);a1.set_title('p = 2 GeV/c, σ_t = 100 ps',loc='left',fontsize=17);a1.grid(alpha=.6)
pp=np.linspace(.5,6,300)
for (u,v),col in [(('π','K'),O),(('K','p'),G)]:a2.semilogy(pp,(tof(pp,mass[v])-tof(pp,mass[u]))/sig,color=col,label=f'{u}/{v}')
a2.axhline(3,color=R,ls='--',label='3σ');a2.set(xlabel='Momentum [GeV/c]',ylabel='Separation [σ_t]',ylim=(.3,300));a2.set_title('L = 5 m',loc='left',fontsize=17);a2.legend();a2.grid(alpha=.6)
save(f,'tof-separation')
print('18 reproducible plots and one attributed source crop generated.')
