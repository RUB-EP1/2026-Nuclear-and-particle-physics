/* Pure teaching models. SI for muons; c=1 for mass; hbar=m=1 for packets. */
(function(root){
 const gamma=b=>1/Math.sqrt(1-b*b);
 function muon(b,h,f=1){const g=gamma(b),t=h/(b*299.792458)*f,tau=t/g;return {g,t,tau,contracted:h/g,survival:Math.exp(-tau/2.1969811),classical:Math.exp(-t/2.1969811)};}
 function pair(p1,p2,angle,b){const m=.1056583755,a=angle*Math.PI/180,g=gamma(b);const boost=(px,py)=>{const E=Math.hypot(px,py,m);return {E:g*(E-b*px),px:g*(px-b*E),py};};const v1=boost(p1,0),v2=boost(p2*Math.cos(a),p2*Math.sin(a));const E=v1.E+v2.E,px=v1.px+v2.px,py=v1.py+v2.py;return {v1,v2,E,px,py,M:Math.sqrt(Math.max(0,E*E-px*px-py*py))};}
 function packet(x,p,s,t,phase){const u=t/(2*s*s),w=s*Math.sqrt(1+u*u),d=x-p*t,density=Math.exp(-d*d/(2*w*w))/(Math.sqrt(2*Math.PI)*w),arg=p*x-p*p*t/2+phase-.5*Math.atan(u)+d*d*u/(4*s*s*(1+u*u));return {density,re:Math.sqrt(density)*Math.cos(arg),im:Math.sqrt(density)*Math.sin(arg),dx:w,dp:1/(2*s)};}
 // ---- Lecture 3 additions (natural units unless stated) ----
 const HBARC=0.1973269804;            // GeV fm
 const HBAR_EVS=6.582119569e-16;      // eV s
 const HBARC_EVM=1.973269804e-7;      // eV m
 // uniform-sphere form factor, x = Q R / (hbar c)
 function sphereFF(x){x=Math.abs(x);return x<1e-3?1-x*x/10:3*(Math.sin(x)-x*Math.cos(x))/(x*x*x);}
 // momentum transfer of elastic scattering through angle theta (degrees)
 const qTransfer=(p,thetaDeg)=>2*p*Math.sin(thetaDeg*Math.PI/360);
 // area-normalised Breit-Wigner and Gaussian
 const lorentzian=(E,M,G)=>(G/(2*Math.PI))/((E-M)*(E-M)+G*G/4);
 const gaussian=(x,s)=>Math.exp(-x*x/(2*s*s))/(Math.sqrt(2*Math.PI)*s);
 // Olivero-Longbothum approximation to the Voigt FWHM (fL, fG are FWHMs)
 const voigtFWHM=(fL,fG)=>0.5346*fL+Math.sqrt(0.2166*fL*fL+fG*fG);
 // two-flavour oscillation: L in km, E in GeV, dm2 in eV^2
 const oscPhase=(dm2,L,E)=>1.26693*dm2*L/E;
 const oscProb=(sin22,dm2,L,E)=>sin22*Math.pow(Math.sin(oscPhase(dm2,L,E)),2);
 // normalised |Y_l^m|^2 as a function of cos(theta)
 function Ylm2(l,m,x){m=Math.abs(m);let pmm=1;if(m>0){const s=Math.sqrt(Math.max(0,1-x*x));let f=1;for(let i=1;i<=m;i++){pmm*=-f*s;f+=2;}}
  let p;if(l===m)p=pmm;else{let pm1=x*(2*m+1)*pmm;if(l===m+1)p=pm1;else{let pl2=pmm,pl1=pm1;for(let ll=m+2;ll<=l;ll++){const cur=((2*ll-1)*x*pl1-(ll+m-1)*pl2)/(ll-m);pl2=pl1;pl1=cur;}p=pl1;}}
  let fac=1;for(let i=l-m+1;i<=l+m;i++)fac*=i;return (2*l+1)/(4*Math.PI)/fac*p*p;}
 // golden rule: discrete initial state coupled with strength V to a ladder of
 // final levels with spacing d (density of states 1/d); returns P_out(t)
 function goldenP(V,d,t,K=400){let s=0;for(let k=-K;k<=K;k++){const x=k*d*t/2;const sinc=Math.abs(x)<1e-9?1:Math.sin(x)/x;s+=V*V*t*t*sinc*sinc;}return s;}
 const api={gamma,muon,pair,packet,HBARC,HBAR_EVS,HBARC_EVM,sphereFF,qTransfer,lorentzian,gaussian,voigtFWHM,oscPhase,oscProb,Ylm2,goldenP};if(typeof module!=='undefined')module.exports=api;else root.Physics=api;
})(globalThis);
