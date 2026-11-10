'use strict';
window.Plot={
 setup(canvas){const r=canvas.getBoundingClientRect(),d=devicePixelRatio||1;canvas.width=r.width*d;canvas.height=r.height*d;const c=canvas.getContext('2d');c.scale(d,d);c.font=(r.width>1200?'20':'17')+'px Helvetica,Arial,sans-serif';return{c,w:r.width,h:r.height};},
 text(c,s,x,y,color='#526675',align='left'){c.fillStyle=color;c.textAlign=align;c.fillText(s,x,y);},
 line(c,x1,y1,x2,y2,color='#dce5eb',width=1){c.strokeStyle=color;c.lineWidth=width;c.beginPath();c.moveTo(x1,y1);c.lineTo(x2,y2);c.stroke();}
};
