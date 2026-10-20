/* Pure teaching models. SI for muons; c=1 for mass; hbar=m=1 for packets. */
(function(root){
 const gamma=b=>1/Math.sqrt(1-b*b);
 function muon(b,h,f=1){const g=gamma(b),t=h/(b*299.792458)*f,tau=t/g;return {g,t,tau,contracted:h/g,survival:Math.exp(-tau/2.1969811),classical:Math.exp(-t/2.1969811)};}
 function pair(p1,p2,angle,b){const m=.1056583755,a=angle*Math.PI/180,g=gamma(b);const boost=(px,py)=>{const E=Math.hypot(px,py,m);return {E:g*(E-b*px),px:g*(px-b*E),py};};const v1=boost(p1,0),v2=boost(p2*Math.cos(a),p2*Math.sin(a));const E=v1.E+v2.E,px=v1.px+v2.px,py=v1.py+v2.py;return {v1,v2,E,px,py,M:Math.sqrt(Math.max(0,E*E-px*px-py*py))};}
 function packet(x,p,s,t,phase){const u=t/(2*s*s),w=s*Math.sqrt(1+u*u),d=x-p*t,density=Math.exp(-d*d/(2*w*w))/(Math.sqrt(2*Math.PI)*w),arg=p*x-p*p*t/2+phase-.5*Math.atan(u)+d*d*u/(4*s*s*(1+u*u));return {density,re:Math.sqrt(density)*Math.cos(arg),im:Math.sqrt(density)*Math.sin(arg),dx:w,dp:1/(2*s)};}
 const api={gamma,muon,pair,packet};if(typeof module!=='undefined')module.exports=api;else root.Physics=api;
})(globalThis);
