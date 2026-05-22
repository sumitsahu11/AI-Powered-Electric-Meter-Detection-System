
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&family=JetBrains+Mono:wght@400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
.wrap{width:100%;background:#0a0a14;border-radius:14px;overflow:hidden;position:relative;min-height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:36px 32px 28px;font-family:'Space Grotesk',sans-serif}
canvas#bg{position:absolute;inset:0;width:100%;height:100%}
.orb{position:absolute;border-radius:50%;pointer-events:none}
.orb1{width:420px;height:320px;background:radial-gradient(circle,rgba(99,102,241,.18) 0%,transparent 70%);top:-100px;left:-80px;animation:breathe 7s ease-in-out infinite}
.orb2{width:320px;height:280px;background:radial-gradient(circle,rgba(6,182,212,.14) 0%,transparent 70%);bottom:-80px;right:-60px;animation:breathe 8s ease-in-out infinite reverse}
.orb3{width:240px;height:200px;background:radial-gradient(circle,rgba(167,139,250,.1) 0%,transparent 70%);top:50%;left:45%;animation:breathe 5s ease-in-out infinite 1.5s}
@keyframes breathe{0%,100%{transform:scale(1);opacity:.8}50%{transform:scale(1.15);opacity:1}}
.scanline{position:absolute;left:0;right:0;height:1.5px;background:linear-gradient(90deg,transparent,rgba(99,102,241,.5),rgba(6,182,212,.5),transparent);animation:scan 4s linear infinite;pointer-events:none}
@keyframes scan{0%{top:-2px;opacity:0}5%{opacity:1}95%{opacity:.8}100%{top:100%;opacity:0}}
.corner{position:absolute;width:22px;height:22px}
.c-tl{top:12px;left:12px;border-top:2px solid rgba(99,102,241,.9);border-left:2px solid rgba(99,102,241,.9)}
.c-tr{top:12px;right:12px;border-top:2px solid rgba(6,182,212,.9);border-right:2px solid rgba(6,182,212,.9)}
.c-bl{bottom:12px;left:12px;border-bottom:2px solid rgba(6,182,212,.9);border-left:2px solid rgba(6,182,212,.9)}
.c-br{bottom:12px;right:12px;border-bottom:2px solid rgba(99,102,241,.9);border-right:2px solid rgba(99,102,241,.9)}
.det-boxes{position:absolute;top:0;right:64px;height:100%;width:90px;pointer-events:none}
.dbox{position:absolute;border-radius:2px;border:1.5px solid rgba(6,182,212,.55);animation:blink 3s ease-in-out infinite}
.dbox::before{content:attr(data-label);position:absolute;top:-16px;left:0;font-family:'JetBrains Mono',monospace;font-size:8px;color:rgba(6,182,212,.85);background:rgba(6,182,212,.08);padding:1px 5px;border-radius:2px;white-space:nowrap}
.db1{width:56px;height:42px;top:46px;animation-delay:0s}
.db2{width:44px;height:32px;top:112px;left:20px;border-color:rgba(6,182,212,.4);animation-delay:1.1s}
.db3{width:60px;height:46px;top:182px;border-color:rgba(165,180,252,.5);animation-delay:2s}
.db3::before{color:rgba(165,180,252,.8);background:rgba(165,180,252,.08)}
@keyframes blink{0%,100%{opacity:.28;border-color:rgba(6,182,212,.25)}50%{opacity:1;border-color:rgba(6,182,212,.8)}}
.content{position:relative;z-index:2;text-align:center;width:100%}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:3.5px;color:rgba(99,102,241,.9);margin-bottom:14px;display:flex;align-items:center;justify-content:center;gap:10px;animation:fadeUp .8s ease both}
.eyebrow::before,.eyebrow::after{content:'';width:32px;height:1px;background:linear-gradient(90deg,transparent,rgba(99,102,241,.6))}
.eyebrow::after{background:linear-gradient(90deg,rgba(99,102,241,.6),transparent)}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.title{font-size:clamp(30px,5.5vw,48px);font-weight:700;letter-spacing:-1.5px;line-height:1.05;background:linear-gradient(125deg,#e0e7ff 0%,#a5b4fc 40%,#38bdf8 75%,#c7d2fe 100%);background-size:200% 200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:fadeUp .8s .15s ease both,shimmer 5s ease-in-out infinite}
@keyframes shimmer{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.sub{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:1px;color:rgba(165,180,252,.6);margin-top:8px;animation:fadeUp .8s .3s ease both}
.divline{width:320px;height:1px;background:linear-gradient(90deg,transparent,rgba(99,102,241,.4),rgba(6,182,212,.4),transparent);margin:16px auto 18px;animation:fadeUp .8s .4s ease both}
.stats{display:flex;border:1px solid rgba(99,102,241,.18);border-radius:10px;overflow:hidden;backdrop-filter:blur(8px);background:rgba(255,255,255,.025);animation:fadeUp .8s .5s ease both}
.stat{padding:14px 22px;text-align:center;position:relative;flex:1;min-width:0}
.stat+.stat::before{content:'';position:absolute;left:0;top:18%;height:64%;width:1px;background:rgba(99,102,241,.18)}
.sn{display:block;font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:700;background:linear-gradient(135deg,#a5b4fc,#38bdf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1}
.sl{display:block;font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:1.8px;color:rgba(99,102,241,.6);margin-top:3px;text-transform:uppercase}
.badges{display:flex;gap:7px;margin-top:16px;justify-content:center;flex-wrap:wrap;animation:fadeUp .8s .65s ease both}
.badge{padding:4px 11px;border-radius:20px;font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:500;letter-spacing:.4px}
.bp{background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.28);color:#a5b4fc}
.bc{background:rgba(6,182,212,.08);border:1px solid rgba(6,182,212,.28);color:#67e8f9}
.bv{background:rgba(167,139,250,.08);border:1px solid rgba(167,139,250,.28);color:#c4b5fd}
.particles{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.p{position:absolute;border-radius:50%;animation:rise linear infinite}
@keyframes rise{0%{transform:translateY(0) scale(1);opacity:0}10%{opacity:1}85%{opacity:.5}100%{transform:translateY(-320px) scale(.2);opacity:0}}
</style>

<div class="wrap" role="img" aria-label="Electric Meter Detection System banner">
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div class="orb orb3"></div>
  <div class="scanline"></div>
  <div class="corner c-tl"></div>
  <div class="corner c-tr"></div>
  <div class="corner c-bl"></div>
  <div class="corner c-br"></div>
  <div class="particles" id="pts"></div>
  <div class="det-boxes">
    <div class="dbox db1" data-label="meter 0.96"></div>
    <div class="dbox db2" data-label="meter 0.91"></div>
    <div class="dbox db3" data-label="meter 0.94"></div>
  </div>
  <div class="content">
    <div class="eyebrow">INTERNSHIP PROJECT · TPCODL · 2026</div>
    <div class="title">Electric Meter<br>Detection System</div>
    <div class="sub">automated ai pipeline &nbsp;·&nbsp; yolov5 + pytorch &nbsp;·&nbsp; flask rest api</div>
    <div class="divline"></div>
    <div class="stats">
      <div class="stat"><span class="sn">95%+</span><span class="sl">Precision</span></div>
      <div class="stat"><span class="sn">152</span><span class="sl">FPS GPU</span></div>
      <div class="stat"><span class="sn">0.94</span><span class="sl">mAP@50</span></div>
      <div class="stat"><span class="sn">20×</span><span class="sl">Faster</span></div>
      <div class="stat"><span class="sn">90%</span><span class="sl">Cost Saved</span></div>
    </div>
    <div class="badges">
      <span class="badge bp">YOLOv5 · PyTorch</span>
      <span class="badge bc">Flask REST API</span>
      <span class="badge bv">OpenCV · SQLite</span>
      <span class="badge bp">Python 3.10+</span>
      <span class="badge bc">14 MB · 6.5 ms/img</span>
    </div>
  </div>
</div>

<script>
const pts = document.getElementById('pts');
for(let i=0;i<22;i++){
  const p=document.createElement('div');
  p.className='p';
  const s=Math.random()*2.5+1;
  const colors=['rgba(99,102,241,.5)','rgba(6,182,212,.45)','rgba(167,139,250,.4)'];
  p.style.cssText=`width:${s}px;height:${s}px;background:${colors[Math.floor(Math.random()*3)]};left:${Math.random()*100}%;bottom:-4px;animation-duration:${6+Math.random()*9}s;animation-delay:${Math.random()*9}s;opacity:0`;
  pts.appendChild(p);
}
</script>


<div align="center">

<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIzNDAiIHZpZXdCb3g9IjAgMCAxMjAwIDM0MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGRlZnM+CiAgPCEtLSBCYWNrZ3JvdW5kcyAtLT4KICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwMjBjMWUiLz4KICAgIDxzdG9wIG9mZnNldD0iNDUlIiBzdG9wLWNvbG9yPSIjMDUwZDJhIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwMjA4MTgiLz4KICA8L2xpbmVhckdyYWRpZW50PgoKICA8IS0tIFRpdGxlIGdyYWRpZW50IC0tPgogIDxsaW5lYXJHcmFkaWVudCBpZD0idGciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjAlIj4KICAgIDxzdG9wIG9mZnNldD0iMCUiICAgc3RvcC1jb2xvcj0iI2UyZThmZiIvPgogICAgPHN0b3Agb2Zmc2V0PSIzMCUiICBzdG9wLWNvbG9yPSIjYTViNGZjIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjYwJSIgIHN0b3AtY29sb3I9IiMzOGJkZjgiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI2M0YjVmZCIvPgogIDwvbGluZWFyR3JhZGllbnQ+CgogIDwhLS0gM0QgdGl0bGUgc2hhZG93IGdyYWRpZW50IChib3R0b20gbGF5ZXIpIC0tPgogIDxsaW5lYXJHcmFkaWVudCBpZD0idGczZCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjMWUxYjRiIiBzdG9wLW9wYWNpdHk9IjAuOSIvPgogICAgPHN0b3Agb2Zmc2V0PSI1MCUiICBzdG9wLWNvbG9yPSIjMTY0ZTYzIiBzdG9wLW9wYWNpdHk9IjAuOSIvPgogICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMmUxMDY1IiBzdG9wLW9wYWNpdHk9IjAuOSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CgogIDwhLS0gQWNjZW50IGxpbmUgLS0+CiAgPGxpbmVhckdyYWRpZW50IGlkPSJhbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjNjM2NmYxIiBzdG9wLW9wYWNpdHk9IjAiLz4KICAgIDxzdG9wIG9mZnNldD0iMjAlIiAgc3RvcC1jb2xvcj0iIzYzNjZmMSIgc3RvcC1vcGFjaXR5PSIwLjkiLz4KICAgIDxzdG9wIG9mZnNldD0iNTAlIiAgc3RvcC1jb2xvcj0iIzA2YjZkNCIvPgogICAgPHN0b3Agb2Zmc2V0PSI4MCUiICBzdG9wLWNvbG9yPSIjYTc4YmZhIiBzdG9wLW9wYWNpdHk9IjAuOSIvPgogICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjYTc4YmZhIiBzdG9wLW9wYWNpdHk9IjAiLz4KICA8L2xpbmVhckdyYWRpZW50PgoKICA8IS0tIFN0YXQgY2FyZCBncmFkaWVudCAtLT4KICA8bGluZWFyR3JhZGllbnQgaWQ9InNjMSIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjMWUyZDVhIiBzdG9wLW9wYWNpdHk9IjAuOSIvPgogICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIiBzdG9wLW9wYWNpdHk9IjAuOTUiLz4KICA8L2xpbmVhckdyYWRpZW50PgogIDxsaW5lYXJHcmFkaWVudCBpZD0ic2MyIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjAlIiB5Mj0iMTAwJSI+CiAgICA8c3RvcCBvZmZzZXQ9IjAlIiAgIHN0b3AtY29sb3I9IiMwZTNhNGEiIHN0b3Atb3BhY2l0eT0iMC45Ii8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwZjE3MmEiIHN0b3Atb3BhY2l0eT0iMC45NSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CgogIDwhLS0gM0QgY2FyZCBzaWRlIChkYXJrKSAtLT4KICA8bGluZWFyR3JhZGllbnQgaWQ9ImNzIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIwJSI+CiAgICA8c3RvcCBvZmZzZXQ9IjAlIiAgIHN0b3AtY29sb3I9IiMwNDBkMjIiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzBhMTUzNSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CgogIDwhLS0gQ2FyZCBib3R0b20gZmFjZSAtLT4KICA8bGluZWFyR3JhZGllbnQgaWQ9ImNiIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjAlIiB5Mj0iMTAwJSI+CiAgICA8c3RvcCBvZmZzZXQ9IjAlIiAgIHN0b3AtY29sb3I9IiMwNjBlMjgiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzAzMDgxMiIvPgogIDwvbGluZWFyR3JhZGllbnQ+CgogIDwhLS0gT3JicyAtLT4KICA8cmFkaWFsR3JhZGllbnQgaWQ9Im8xIiBjeD0iNTAlIiBjeT0iNTAlIiByPSI1MCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjNGY0NmU1IiBzdG9wLW9wYWNpdHk9IjAuMzAiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzRmNDZlNSIgc3RvcC1vcGFjaXR5PSIwIi8+CiAgPC9yYWRpYWxHcmFkaWVudD4KICA8cmFkaWFsR3JhZGllbnQgaWQ9Im8yIiBjeD0iNTAlIiBjeT0iNTAlIiByPSI1MCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjMDg5MWIyIiBzdG9wLW9wYWNpdHk9IjAuMjgiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzA4OTFiMiIgc3RvcC1vcGFjaXR5PSIwIi8+CiAgPC9yYWRpYWxHcmFkaWVudD4KICA8cmFkaWFsR3JhZGllbnQgaWQ9Im8zIiBjeD0iNTAlIiBjeT0iNTAlIiByPSI1MCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgICBzdG9wLWNvbG9yPSIjN2MzYWVkIiBzdG9wLW9wYWNpdHk9IjAuMTgiLz4KICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzdjM2FlZCIgc3RvcC1vcGFjaXR5PSIwIi8+CiAgPC9yYWRpYWxHcmFkaWVudD4KCiAgPCEtLSBGaWx0ZXJzIC0tPgogIDxmaWx0ZXIgaWQ9Imdsb3ciIHg9Ii0zMCUiIHk9Ii0zMCUiIHdpZHRoPSIxNjAlIiBoZWlnaHQ9IjE2MCUiPgogICAgPGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iMyIgcmVzdWx0PSJiIi8+CiAgICA8ZmVNZXJnZT48ZmVNZXJnZU5vZGUgaW49ImIiLz48ZmVNZXJnZU5vZGUgaW49IlNvdXJjZUdyYXBoaWMiLz48L2ZlTWVyZ2U+CiAgPC9maWx0ZXI+CiAgPGZpbHRlciBpZD0ic29mdGdsb3ciIHg9Ii01MCUiIHk9Ii01MCUiIHdpZHRoPSIyMDAlIiBoZWlnaHQ9IjIwMCUiPgogICAgPGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iMTAiIHJlc3VsdD0iYiIvPgogICAgPGZlTWVyZ2U+PGZlTWVyZ2VOb2RlIGluPSJiIi8+PGZlTWVyZ2VOb2RlIGluPSJTb3VyY2VHcmFwaGljIi8+PC9mZU1lcmdlPgogIDwvZmlsdGVyPgogIDxmaWx0ZXIgaWQ9InR4dHNoYWRvdyIgeD0iLTUlIiB5PSItNSUiIHdpZHRoPSIxMTAlIiBoZWlnaHQ9IjEzMCUiPgogICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiM2MzY2ZjEiIGZsb29kLW9wYWNpdHk9IjAuNDUiLz4KICA8L2ZpbHRlcj4KICA8ZmlsdGVyIGlkPSJjYXJkc2hhZG93IiB4PSItMTAlIiB5PSItMTAlIiB3aWR0aD0iMTMwJSIgaGVpZ2h0PSIxNTAlIj4KICAgIDxmZURyb3BTaGFkb3cgZHg9IjIiIGR5PSI2IiBzdGREZXZpYXRpb249IjgiIGZsb29kLWNvbG9yPSIjMDAwMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICA8L2ZpbHRlcj4KICA8ZmlsdGVyIGlkPSJpbm5lcmdsb3ciPgogICAgPGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iMiIgcmVzdWx0PSJiIi8+CiAgICA8ZmVDb21wb3NpdGUgaW49IlNvdXJjZUdyYXBoaWMiIGluMj0iYiIgb3BlcmF0b3I9Im92ZXIiLz4KICA8L2ZpbHRlcj4KCiAgPGNsaXBQYXRoIGlkPSJjbGlwIj48cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIzNDAiIHJ4PSIxNiIvPjwvY2xpcFBhdGg+CjwvZGVmcz4KCjwhLS0g4pSA4pSA4pSAIEJhc2Ug4pSA4pSA4pSAIC0tPgo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIzNDAiIHJ4PSIxNiIgZmlsbD0idXJsKCNiZykiLz4KCjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwKSI+Cgo8IS0tIOKUgOKUgOKUgCBHbG93IG9yYnMg4pSA4pSA4pSAIC0tPgo8ZWxsaXBzZSBjeD0iMTgwIiAgY3k9IjExMCIgcng9IjM4MCIgcnk9IjI4MCIgZmlsbD0idXJsKCNvMSkiLz4KPGVsbGlwc2UgY3g9IjEwNTAiIGN5PSIyMzAiIHJ4PSIzMjAiIHJ5PSIyNjAiIGZpbGw9InVybCgjbzIpIi8+CjxlbGxpcHNlIGN4PSI2MDAiICBjeT0iMTUwIiByeD0iMzAwIiByeT0iMjAwIiBmaWxsPSJ1cmwoI28zKSIvPgoKPCEtLSDilIDilIDilIAgU3VidGxlIGdyaWQg4pSA4pSA4pSAIC0tPgo8ZyBzdHJva2U9IiM2MzY2ZjEiIHN0cm9rZS1vcGFjaXR5PSIwLjA1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiPgogIDxsaW5lIHgxPSIwIiB5MT0iNjAiICB4Mj0iMTIwMCIgeTI9IjYwIi8+CiAgPGxpbmUgeDE9IjAiIHkxPSIxMjAiIHgyPSIxMjAwIiB5Mj0iMTIwIi8+CiAgPGxpbmUgeDE9IjAiIHkxPSIxODAiIHgyPSIxMjAwIiB5Mj0iMTgwIi8+CiAgPGxpbmUgeDE9IjAiIHkxPSIyNDAiIHgyPSIxMjAwIiB5Mj0iMjQwIi8+CiAgPGxpbmUgeDE9IjAiIHkxPSIzMDAiIHgyPSIxMjAwIiB5Mj0iMzAwIi8+CiAgPGxpbmUgeDE9IjEyMCIgIHkxPSIwIiB4Mj0iMTIwIiAgeTI9IjM0MCIvPgogIDxsaW5lIHgxPSIyNDAiICB5MT0iMCIgeDI9IjI0MCIgIHkyPSIzNDAiLz4KICA8bGluZSB4MT0iMzYwIiAgeTE9IjAiIHgyPSIzNjAiICB5Mj0iMzQwIi8+CiAgPGxpbmUgeDE9IjQ4MCIgIHkxPSIwIiB4Mj0iNDgwIiAgeTI9IjM0MCIvPgogIDxsaW5lIHgxPSI2MDAiICB5MT0iMCIgeDI9IjYwMCIgIHkyPSIzNDAiLz4KICA8bGluZSB4MT0iNzIwIiAgeTE9IjAiIHgyPSI3MjAiICB5Mj0iMzQwIi8+CiAgPGxpbmUgeDE9Ijg0MCIgIHkxPSIwIiB4Mj0iODQwIiAgeTI9IjM0MCIvPgogIDxsaW5lIHgxPSI5NjAiICB5MT0iMCIgeDI9Ijk2MCIgIHkyPSIzNDAiLz4KICA8bGluZSB4MT0iMTA4MCIgeTE9IjAiIHgyPSIxMDgwIiB5Mj0iMzQwIi8+CjwvZz4KCjwhLS0g4pSA4pSA4pSAIENvcm5lciBicmFja2V0cyDilIDilIDilIAgLS0+CjxwYXRoIGQ9Ik0yNiA2MCBMMjYgMjYgTDYwIDI2IiBmaWxsPSJub25lIiBzdHJva2U9IiM2MzY2ZjEiIHN0cm9rZS13aWR0aD0iMi4yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1vcGFjaXR5PSIwLjk1IiBmaWx0ZXI9InVybCgjZ2xvdykiLz4KPHBhdGggZD0iTTExNzQgNjAgTDExNzQgMjYgTDExNDAgMjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzA2YjZkNCIgc3Ryb2tlLXdpZHRoPSIyLjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLW9wYWNpdHk9IjAuOTUiIGZpbHRlcj0idXJsKCNnbG93KSIvPgo8cGF0aCBkPSJNMjYgMjgwIEwyNiAzMTQgTDYwIDMxNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDZiNmQ0IiBzdHJva2Utd2lkdGg9IjIuMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utb3BhY2l0eT0iMC45NSIgZmlsdGVyPSJ1cmwoI2dsb3cpIi8+CjxwYXRoIGQ9Ik0xMTc0IDI4MCBMMTE3NCAzMTQgTDExNDAgMzE0IiBmaWxsPSJub25lIiBzdHJva2U9IiM2MzY2ZjEiIHN0cm9rZS13aWR0aD0iMi4yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1vcGFjaXR5PSIwLjk1IiBmaWx0ZXI9InVybCgjZ2xvdykiLz4KCjwhLS0g4pSA4pSA4pSAIENpcmN1aXQgdHJhY2VzIGxlZnQg4pSA4pSA4pSAIC0tPgo8ZyBzdHJva2U9IiM2MzY2ZjEiIHN0cm9rZS1vcGFjaXR5PSIwLjIwIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogIDxwYXRoIGQ9Ik0wIDkwIEg5MCBWNzAgSDE0MCIvPgogIDxwYXRoIGQ9Ik0wIDE1NSBINTUgVjEzNSBIMTA1IFYxMTUiLz4KICA8cGF0aCBkPSJNMCAyMTUgSDY1IFYxOTUiLz4KICA8Y2lyY2xlIGN4PSI5MCIgIGN5PSI5MCIgIHI9IjMuNSIgZmlsbD0iIzYzNjZmMSIgZmlsbC1vcGFjaXR5PSIwLjQiIHN0cm9rZT0ibm9uZSIvPgogIDxjaXJjbGUgY3g9IjU1IiAgY3k9IjE1NSIgcj0iMyIgICBmaWxsPSIjNjM2NmYxIiBmaWxsLW9wYWNpdHk9IjAuMzIiIHN0cm9rZT0ibm9uZSIvPgogIDxjaXJjbGUgY3g9IjE0MCIgY3k9IjcwIiAgcj0iMiIgICBmaWxsPSIjNjM2NmYxIiBmaWxsLW9wYWNpdHk9IjAuMjUiIHN0cm9rZT0ibm9uZSIvPgo8L2c+Cgo8IS0tIOKUgOKUgOKUgCBDaXJjdWl0IHRyYWNlcyByaWdodCDilIDilIDilIAgLS0+CjxnIHN0cm9rZT0iIzA2YjZkNCIgc3Ryb2tlLW9wYWNpdHk9IjAuMjAiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyMDAgMTEwIEgxMTAwIFY5MCBIMTA1MCIvPgogIDxwYXRoIGQ9Ik0xMjAwIDE5MCBIMTEzMCBWMTcwIEgxMDgwIFYxNTAiLz4KICA8cGF0aCBkPSJNMTIwMCAyNTUgSDExNDUgVjIzNSIvPgogIDxjaXJjbGUgY3g9IjExMDAiIGN5PSIxMTAiIHI9IjMuNSIgZmlsbD0iIzA2YjZkNCIgZmlsbC1vcGFjaXR5PSIwLjQiICBzdHJva2U9Im5vbmUiLz4KICA8Y2lyY2xlIGN4PSIxMTMwIiBjeT0iMTkwIiByPSIzIiAgIGZpbGw9IiMwNmI2ZDQiIGZpbGwtb3BhY2l0eT0iMC4zMiIgc3Ryb2tlPSJub25lIi8+CjwvZz4KCjwhLS0g4pSA4pSA4pSAIEV5ZWJyb3cg4pSA4pSA4pSAIC0tPgo8dGV4dCB4PSI2MDAiIHk9IjYyIiBmb250LWZhbWlseT0iQ291cmllciBOZXcsIG1vbm9zcGFjZSIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzYzNjZmMSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSI1LjUiPklOVEVSTlNISVAgUFJPSkVDVCAgwrcgIFRQQ09ETCAgwrcgIDIwMjY8L3RleHQ+Cgo8IS0tIOKUgOKUgOKUgCBUb3AgZGl2aWRlciDilIDilIDilIAgLS0+CjxyZWN0IHg9IjE4MCIgeT0iNzIiIHdpZHRoPSI4NDAiIGhlaWdodD0iMS4yIiByeD0iMSIgZmlsbD0idXJsKCNhbCkiLz4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQCiAgICAgM0QgVEVYVCBFRkZFQ1Qg4oCUIEVsZWN0cmljIE1ldGVyCiAgICAgKGRlcHRoIGxheWVycyBiZWhpbmQgKyBmYWNlIG9uIHRvcCkK4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgoKPCEtLSBTaGFkb3cgLyBkZXB0aCBsYXllcnMg4oCUIG9mZnNldCBzdGFja2VkIC0tPgo8dGV4dCB4PSI2MDIiIHk9IjE0OCIgZm9udC1mYW1pbHk9IkFyaWFsIEJsYWNrLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI2NiIgZm9udC13ZWlnaHQ9IjkwMCIgZmlsbD0idXJsKCN0ZzNkKSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9Ii0yIiB0cmFuc2Zvcm09InNrZXdYKC0xKSI+RWxlY3RyaWMgTWV0ZXI8L3RleHQ+Cjx0ZXh0IHg9IjYwMSIgeT0iMTQ2IiBmb250LWZhbWlseT0iQXJpYWwgQmxhY2ssIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjY2IiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSJ1cmwoI3RnM2QpIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iLTIiIHRyYW5zZm9ybT0ic2tld1goLTEpIj5FbGVjdHJpYyBNZXRlcjwvdGV4dD4KPHRleHQgeD0iNjAwIiB5PSIxNDQiIGZvbnQtZmFtaWx5PSJBcmlhbCBCbGFjaywgQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNjYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZpbGw9IiMxYTEwNjAiIGZpbGwtb3BhY2l0eT0iMC43IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iLTIiPkVsZWN0cmljIE1ldGVyPC90ZXh0PgoKPHRleHQgeD0iNjAyIiB5PSIyMTUiIGZvbnQtZmFtaWx5PSJBcmlhbCBCbGFjaywgQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNjYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZpbGw9InVybCgjdGczZCkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSItMiIgdHJhbnNmb3JtPSJza2V3WCgtMSkiPkRldGVjdGlvbiBTeXN0ZW08L3RleHQ+Cjx0ZXh0IHg9IjYwMSIgeT0iMjEzIiBmb250LWZhbWlseT0iQXJpYWwgQmxhY2ssIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjY2IiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSJ1cmwoI3RnM2QpIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iLTIiIHRyYW5zZm9ybT0ic2tld1goLTEpIj5EZXRlY3Rpb24gU3lzdGVtPC90ZXh0Pgo8dGV4dCB4PSI2MDAiIHk9IjIxMSIgZm9udC1mYW1pbHk9IkFyaWFsIEJsYWNrLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI2NiIgZm9udC13ZWlnaHQ9IjkwMCIgZmlsbD0iIzBkMjA0MCIgZmlsbC1vcGFjaXR5PSIwLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSItMiI+RGV0ZWN0aW9uIFN5c3RlbTwvdGV4dD4KCjwhLS0gRmFjZSBsYXllciAodG9wKSB3aXRoIGdsb3cgLS0+Cjx0ZXh0IHg9IjYwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iQXJpYWwgQmxhY2ssIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjY2IiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSJ1cmwoI3RnKSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9Ii0yIiBmaWx0ZXI9InVybCgjdHh0c2hhZG93KSI+RWxlY3RyaWMgTWV0ZXI8L3RleHQ+Cjx0ZXh0IHg9IjYwMCIgeT0iMjA5IiBmb250LWZhbWlseT0iQXJpYWwgQmxhY2ssIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjY2IiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSJ1cmwoI3RnKSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9Ii0yIiBmaWx0ZXI9InVybCgjdHh0c2hhZG93KSI+RGV0ZWN0aW9uIFN5c3RlbTwvdGV4dD4KCjwhLS0g4pSA4pSA4pSAIFN1YnRpdGxlIOKUgOKUgOKUgCAtLT4KPHRleHQgeD0iNjAwIiB5PSIyMzIiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTRhM2I4IiBmaWxsLW9wYWNpdHk9IjAuNzgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIxLjgiPkFVVE9NQVRFRCBBSSBQSVBFTElORSAgwrcgIFlPTE92NSArIFB5VG9yY2ggIMK3ICBGbGFzayBSRVNUIEFQSTwvdGV4dD4KCjwhLS0g4pSA4pSA4pSAIEJvdHRvbSBkaXZpZGVyIOKUgOKUgOKUgCAtLT4KPHJlY3QgeD0iMTgwIiB5PSIyNDEiIHdpZHRoPSI4NDAiIGhlaWdodD0iMSIgICByeD0iMSIgZmlsbD0idXJsKCNhbCkiLz4KPHJlY3QgeD0iMzQwIiB5PSIyNDMiIHdpZHRoPSI1MjAiIGhlaWdodD0iMC42IiByeD0iMSIgZmlsbD0idXJsKCNhbCkiIG9wYWNpdHk9IjAuNSIvPgoKPCEtLSDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAKICAgICAzRCBTVEFUIENBUkRTCiAgICAgRWFjaCBjYXJkOiBib3R0b20gZmFjZSArIHJpZ2h0IGZhY2UgKyB0b3AgZmFjZQrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAgLS0+Cgo8IS0tIGNhcmQgZGVwdGggPSA2cHggZG93bi1yaWdodCAtLT4KCjwhLS0gQ0FSRCAxIOKAlCBQcmVjaXNpb24gLS0+CjwhLS0gQm90dG9tIGZhY2UgLS0+CjxwYXRoIGQ9Ik03OCAyOTYgTDg0IDMwMiBMMTk0IDMwMiBMMTk0IDI5NiBaIiBmaWxsPSJ1cmwoI2NiKSIgb3BhY2l0eT0iMC44Ii8+CjwhLS0gUmlnaHQgZmFjZSAtLT4KPHBhdGggZD0iTTE4OCAyNTYgTDE5NCAyNjIgTDE5NCAzMDIgTDE4OCAyOTYgWiIgZmlsbD0idXJsKCNjcykiIG9wYWNpdHk9IjAuOSIvPgo8IS0tIFRvcCBmYWNlIC0tPgo8cmVjdCB4PSI3OCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjQwIiByeD0iNSIgZmlsbD0idXJsKCNzYzEpIiBzdHJva2U9IiM2MzY2ZjEiIHN0cm9rZS1vcGFjaXR5PSIwLjM1IiBzdHJva2Utd2lkdGg9IjAuOCIgZmlsdGVyPSJ1cmwoI2NhcmRzaGFkb3cpIi8+CjwhLS0gVG9wIGVkZ2UgZ2xvdyAtLT4KPHJlY3QgeD0iNzgiIHk9IjI1NiIgd2lkdGg9IjExMCIgaGVpZ2h0PSIxLjUiIHJ4PSIxIiBmaWxsPSIjNjM2NmYxIiBmaWxsLW9wYWNpdHk9IjAuNiIvPgo8IS0tIENvbnRlbnQgLS0+Cjx0ZXh0IHg9IjEzMyIgeT0iMjgwIiBmb250LWZhbWlseT0iQ291cmllciBOZXcsIG1vbm9zcGFjZSIgZm9udC1zaXplPSIyMCIgZm9udC13ZWlnaHQ9IjcwMCIgZmlsbD0iI2M3ZDhmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsdGVyPSJ1cmwoI2dsb3cpIj45NSUrPC90ZXh0Pgo8dGV4dCB4PSIxMzMiIHk9IjI5MiIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOCIgICBmaWxsPSIjODE4Y2Y4IiBmaWxsLW9wYWNpdHk9IjAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9IjIiPlBSRUNJU0lPTjwvdGV4dD4KCjwhLS0gQ0FSRCAyIOKAlCBGUFMgLS0+CjxwYXRoIGQ9Ik0yMDggMjk2IEwyMTQgMzAyIEwzMjQgMzAyIEwzMjQgMjk2IFoiIGZpbGw9InVybCgjY2IpIiBvcGFjaXR5PSIwLjgiLz4KPHBhdGggZD0iTTMxOCAyNTYgTDMyNCAyNjIgTDMyNCAzMDIgTDMxOCAyOTYgWiIgZmlsbD0idXJsKCNjcykiIG9wYWNpdHk9IjAuOSIvPgo8cmVjdCB4PSIyMDgiIHk9IjI1NiIgd2lkdGg9IjExMCIgaGVpZ2h0PSI0MCIgcng9IjUiIGZpbGw9InVybCgjc2MyKSIgc3Ryb2tlPSIjMDZiNmQ0IiBzdHJva2Utb3BhY2l0eT0iMC4zNSIgc3Ryb2tlLXdpZHRoPSIwLjgiIGZpbHRlcj0idXJsKCNjYXJkc2hhZG93KSIvPgo8cmVjdCB4PSIyMDgiIHk9IjI1NiIgd2lkdGg9IjExMCIgaGVpZ2h0PSIxLjUiIHJ4PSIxIiBmaWxsPSIjMDZiNmQ0IiBmaWxsLW9wYWNpdHk9IjAuNiIvPgo8dGV4dCB4PSIyNjMiIHk9IjI4MCIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMjAiIGZvbnQtd2VpZ2h0PSI3MDAiIGZpbGw9IiM2N2U4ZjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCNnbG93KSI+MTUyIEZQUzwvdGV4dD4KPHRleHQgeD0iMjYzIiB5PSIyOTIiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjgiICAgZmlsbD0iIzIyZDNlZSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5HUFUgU1BFRUQ8L3RleHQ+Cgo8IS0tIENBUkQgMyDigJQgbUFQIChjZW50ZXIsIHNsaWdodGx5IHRhbGxlcikgLS0+CjxwYXRoIGQ9Ik0zMzggMjk5IEwzNDQgMzA1IEw0NTQgMzA1IEw0NTQgMjk5IFoiIGZpbGw9InVybCgjY2IpIiBvcGFjaXR5PSIwLjgiLz4KPHBhdGggZD0iTTQ0OCAyNTMgTDQ1NCAyNTkgTDQ1NCAzMDUgTDQ0OCAyOTkgWiIgZmlsbD0idXJsKCNjcykiIG9wYWNpdHk9IjAuOSIvPgo8cmVjdCB4PSIzMzgiIHk9IjI1MyIgd2lkdGg9IjExMCIgaGVpZ2h0PSI0NiIgcng9IjUiIGZpbGw9InVybCgjc2MxKSIgc3Ryb2tlPSIjYTc4YmZhIiBzdHJva2Utb3BhY2l0eT0iMC40IiBzdHJva2Utd2lkdGg9IjAuOSIgZmlsdGVyPSJ1cmwoI2NhcmRzaGFkb3cpIi8+CjxyZWN0IHg9IjMzOCIgeT0iMjUzIiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjIiIHJ4PSIxIiBmaWxsPSIjYTc4YmZhIiBmaWxsLW9wYWNpdHk9IjAuNyIvPgo8dGV4dCB4PSIzOTMiIHk9IjI3OSIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMjAiIGZvbnQtd2VpZ2h0PSI3MDAiIGZpbGw9IiNjNGI1ZmQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCNnbG93KSI+MC45NDwvdGV4dD4KPHRleHQgeD0iMzkzIiB5PSIyOTEiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjgiICAgZmlsbD0iI2E3OGJmYSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5tQVBANTA8L3RleHQ+Cgo8IS0tIENBUkQgNCDigJQgRmFzdGVyIC0tPgo8cGF0aCBkPSJNNDY4IDI5NiBMNDc0IDMwMiBMNTg0IDMwMiBMNTg0IDI5NiBaIiBmaWxsPSJ1cmwoI2NiKSIgb3BhY2l0eT0iMC44Ii8+CjxwYXRoIGQ9Ik01NzggMjU2IEw1ODQgMjYyIEw1ODQgMzAyIEw1NzggMjk2IFoiIGZpbGw9InVybCgjY3MpIiBvcGFjaXR5PSIwLjkiLz4KPHJlY3QgeD0iNDY4IiB5PSIyNTYiIHdpZHRoPSIxMTAiIGhlaWdodD0iNDAiIHJ4PSI1IiBmaWxsPSJ1cmwoI3NjMikiIHN0cm9rZT0iIzA2YjZkNCIgc3Ryb2tlLW9wYWNpdHk9IjAuMzUiIHN0cm9rZS13aWR0aD0iMC44IiBmaWx0ZXI9InVybCgjY2FyZHNoYWRvdykiLz4KPHJlY3QgeD0iNDY4IiB5PSIyNTYiIHdpZHRoPSIxMTAiIGhlaWdodD0iMS41IiByeD0iMSIgZmlsbD0iIzA2YjZkNCIgZmlsbC1vcGFjaXR5PSIwLjYiLz4KPHRleHQgeD0iNTIzIiB5PSIyODAiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjIwIiBmb250LXdlaWdodD0iNzAwIiBmaWxsPSIjNjdlOGY5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZ2xvdykiPjIww5c8L3RleHQ+Cjx0ZXh0IHg9IjUyMyIgeT0iMjkyIiBmb250LWZhbWlseT0iQ291cmllciBOZXcsIG1vbm9zcGFjZSIgZm9udC1zaXplPSI4IiAgIGZpbGw9IiMyMmQzZWUiIGZpbGwtb3BhY2l0eT0iMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iMiI+RkFTVEVSPC90ZXh0PgoKPCEtLSBDQVJEIDUg4oCUIENvc3QgLS0+CjxwYXRoIGQ9Ik01OTggMjk2IEw2MDQgMzAyIEw3MTQgMzAyIEw3MTQgMjk2IFoiIGZpbGw9InVybCgjY2IpIiBvcGFjaXR5PSIwLjgiLz4KPHBhdGggZD0iTTcwOCAyNTYgTDcxNCAyNjIgTDcxNCAzMDIgTDcwOCAyOTYgWiIgZmlsbD0idXJsKCNjcykiIG9wYWNpdHk9IjAuOSIvPgo8cmVjdCB4PSI1OTgiIHk9IjI1NiIgd2lkdGg9IjExMCIgaGVpZ2h0PSI0MCIgcng9IjUiIGZpbGw9InVybCgjc2MxKSIgc3Ryb2tlPSIjNjM2NmYxIiBzdHJva2Utb3BhY2l0eT0iMC4zNSIgc3Ryb2tlLXdpZHRoPSIwLjgiIGZpbHRlcj0idXJsKCNjYXJkc2hhZG93KSIvPgo8cmVjdCB4PSI1OTgiIHk9IjI1NiIgd2lkdGg9IjExMCIgaGVpZ2h0PSIxLjUiIHJ4PSIxIiBmaWxsPSIjNjM2NmYxIiBmaWxsLW9wYWNpdHk9IjAuNiIvPgo8dGV4dCB4PSI2NTMiIHk9IjI4MCIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMjAiIGZvbnQtd2VpZ2h0PSI3MDAiIGZpbGw9IiNjN2Q4ZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCNnbG93KSI+OTAlPC90ZXh0Pgo8dGV4dCB4PSI2NTMiIHk9IjI5MiIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOCIgICBmaWxsPSIjODE4Y2Y4IiBmaWxsLW9wYWNpdHk9IjAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9IjIiPkNPU1QgU0FWRUQ8L3RleHQ+Cgo8IS0tIENBUkQgNiDigJQgTW9kZWwgU2l6ZSAtLT4KPHBhdGggZD0iTTcyOCAyOTYgTDczNCAzMDIgTDg0NCAzMDIgTDg0NCAyOTYgWiIgZmlsbD0idXJsKCNjYikiIG9wYWNpdHk9IjAuOCIvPgo8cGF0aCBkPSJNODM4IDI1NiBMODQ0IDI2MiBMODQ0IDMwMiBMODM4IDI5NiBaIiBmaWxsPSJ1cmwoI2NzKSIgb3BhY2l0eT0iMC45Ii8+CjxyZWN0IHg9IjcyOCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjQwIiByeD0iNSIgZmlsbD0idXJsKCNzYzIpIiBzdHJva2U9IiMwNmI2ZDQiIHN0cm9rZS1vcGFjaXR5PSIwLjM1IiBzdHJva2Utd2lkdGg9IjAuOCIgZmlsdGVyPSJ1cmwoI2NhcmRzaGFkb3cpIi8+CjxyZWN0IHg9IjcyOCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjEuNSIgcng9IjEiIGZpbGw9IiMwNmI2ZDQiIGZpbGwtb3BhY2l0eT0iMC42Ii8+Cjx0ZXh0IHg9Ijc4MyIgeT0iMjgwIiBmb250LWZhbWlseT0iQ291cmllciBOZXcsIG1vbm9zcGFjZSIgZm9udC1zaXplPSIyMCIgZm9udC13ZWlnaHQ9IjcwMCIgZmlsbD0iIzY3ZThmOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsdGVyPSJ1cmwoI2dsb3cpIj4xNCBNQjwvdGV4dD4KPHRleHQgeD0iNzgzIiB5PSIyOTIiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjgiICAgZmlsbD0iIzIyZDNlZSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5NT0RFTCBTSVpFPC90ZXh0PgoKPCEtLSBDQVJEIDcg4oCUIEltYWdlcyAtLT4KPHBhdGggZD0iTTg1OCAyOTYgTDg2NCAzMDIgTDk3NCAzMDIgTDk3NCAyOTYgWiIgZmlsbD0idXJsKCNjYikiIG9wYWNpdHk9IjAuOCIvPgo8cGF0aCBkPSJNOTY4IDI1NiBMOTc0IDI2MiBMOTc0IDMwMiBMOTY4IDI5NiBaIiBmaWxsPSJ1cmwoI2NzKSIgb3BhY2l0eT0iMC45Ii8+CjxyZWN0IHg9Ijg1OCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjQwIiByeD0iNSIgZmlsbD0idXJsKCNzYzEpIiBzdHJva2U9IiNhNzhiZmEiIHN0cm9rZS1vcGFjaXR5PSIwLjM1IiBzdHJva2Utd2lkdGg9IjAuOCIgZmlsdGVyPSJ1cmwoI2NhcmRzaGFkb3cpIi8+CjxyZWN0IHg9Ijg1OCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjEuNSIgcng9IjEiIGZpbGw9IiNhNzhiZmEiIGZpbGwtb3BhY2l0eT0iMC42Ii8+Cjx0ZXh0IHg9IjkxMyIgeT0iMjgwIiBmb250LWZhbWlseT0iQ291cmllciBOZXcsIG1vbm9zcGFjZSIgZm9udC1zaXplPSIyMCIgZm9udC13ZWlnaHQ9IjcwMCIgZmlsbD0iI2M0YjVmZCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsdGVyPSJ1cmwoI2dsb3cpIj4xLDAwMDwvdGV4dD4KPHRleHQgeD0iOTEzIiB5PSIyOTIiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjgiICAgZmlsbD0iI2E3OGJmYSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5UUkFJTiBJTUdTPC90ZXh0PgoKPCEtLSBDQVJEIDgg4oCUIFJlY2FsbCAtLT4KPHBhdGggZD0iTTk4OCAyOTYgTDk5NCAzMDIgTDExMDQgMzAyIEwxMTA0IDI5NiBaIiBmaWxsPSJ1cmwoI2NiKSIgb3BhY2l0eT0iMC44Ii8+CjxwYXRoIGQ9Ik0xMDk4IDI1NiBMMTEwNCAyNjIgTDExMDQgMzAyIEwxMDk4IDI5NiBaIiBmaWxsPSJ1cmwoI2NzKSIgb3BhY2l0eT0iMC45Ii8+CjxyZWN0IHg9Ijk4OCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjQwIiByeD0iNSIgZmlsbD0idXJsKCNzYzIpIiBzdHJva2U9IiMwNmI2ZDQiIHN0cm9rZS1vcGFjaXR5PSIwLjM1IiBzdHJva2Utd2lkdGg9IjAuOCIgZmlsdGVyPSJ1cmwoI2NhcmRzaGFkb3cpIi8+CjxyZWN0IHg9Ijk4OCIgeT0iMjU2IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjEuNSIgcng9IjEiIGZpbGw9IiMwNmI2ZDQiIGZpbGwtb3BhY2l0eT0iMC42Ii8+Cjx0ZXh0IHg9IjEwNDMiIHk9IjI4MCIgZm9udC1mYW1pbHk9IkNvdXJpZXIgTmV3LCBtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMjAiIGZvbnQtd2VpZ2h0PSI3MDAiIGZpbGw9IiM2N2U4ZjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCNnbG93KSI+OTYlPC90ZXh0Pgo8dGV4dCB4PSIxMDQzIiB5PSIyOTIiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjgiICAgZmlsbD0iIzIyZDNlZSIgZmlsbC1vcGFjaXR5PSIwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5SRUNBTEw8L3RleHQ+Cgo8IS0tIOKUgOKUgOKUgCBGbG9hdGluZyBkZXRlY3Rpb24gYm94ZXMgKHRvcCByaWdodCkg4pSA4pSA4pSAIC0tPgo8ZyBmaWx0ZXI9InVybCgjZ2xvdykiPgogIDxyZWN0IHg9IjEwMDAiIHk9IjM2IiB3aWR0aD0iNzIiIGhlaWdodD0iNTIiIHJ4PSIyIiBmaWxsPSJub25lIiBzdHJva2U9IiMwNmI2ZDQiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2Utb3BhY2l0eT0iMC42NSIvPgogIDwhLS0gY29ybmVyIHRpY2tzIC0tPgogIDxwYXRoIGQ9Ik0xMDAwIDQ0IEwxMDAwIDM2IEwxMDA4IDM2IiBmaWxsPSJub25lIiBzdHJva2U9IiMwNmI2ZDQiIHN0cm9rZS13aWR0aD0iMS4yIiBzdHJva2Utb3BhY2l0eT0iMC45Ii8+CiAgPHBhdGggZD0iTTEwNjQgNDQgTDEwNjQgMzYgTDEwNTYgMzYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzA2YjZkNCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1vcGFjaXR5PSIwLjkiLz4KICA8cGF0aCBkPSJNMTAwMCA4MCBMMTAwMCA4OCBMMTAwOCA4OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDZiNmQ0IiBzdHJva2Utd2lkdGg9IjEuMiIgc3Ryb2tlLW9wYWNpdHk9IjAuOSIvPgogIDxwYXRoIGQ9Ik0xMDY0IDgwIEwxMDY0IDg4IEwxMDU2IDg4IiBmaWxsPSJub25lIiBzdHJva2U9IiMwNmI2ZDQiIHN0cm9rZS13aWR0aD0iMS4yIiBzdHJva2Utb3BhY2l0eT0iMC45Ii8+CiAgPHRleHQgeD0iMTAwMiIgeT0iMzMiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjkuNSIgZmlsbD0iIzA2YjZkNCIgZmlsbC1vcGFjaXR5PSIwLjg1Ij5tZXRlciAwLjk2PC90ZXh0PgoKICA8cmVjdCB4PSIxMDg1IiB5PSI2MCIgd2lkdGg9IjYyIiBoZWlnaHQ9IjQ0IiByeD0iMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjYTc4YmZhIiBzdHJva2Utd2lkdGg9IjEuMyIgc3Ryb2tlLW9wYWNpdHk9IjAuNTUiLz4KICA8cGF0aCBkPSJNMTA4NSA2OCBMMTA4NSA2MCBMMTA5MyA2MCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjYTc4YmZhIiBzdHJva2Utd2lkdGg9IjEuMSIgc3Ryb2tlLW9wYWNpdHk9IjAuOCIvPgogIDxwYXRoIGQ9Ik0xMTM5IDY4IEwxMTM5IDYwIEwxMTMxIDYwIiBmaWxsPSJub25lIiBzdHJva2U9IiNhNzhiZmEiIHN0cm9rZS13aWR0aD0iMS4xIiBzdHJva2Utb3BhY2l0eT0iMC44Ii8+CiAgPHRleHQgeD0iMTA4NyIgeT0iNTciIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjkuNSIgZmlsbD0iI2E3OGJmYSIgZmlsbC1vcGFjaXR5PSIwLjgiPm1ldGVyIDAuOTE8L3RleHQ+CgogIDxyZWN0IHg9IjEwMTAiIHk9IjEwOCIgd2lkdGg9IjY2IiBoZWlnaHQ9IjQ2IiByeD0iMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjNjM2NmYxIiBzdHJva2Utd2lkdGg9IjEuMiIgc3Ryb2tlLW9wYWNpdHk9IjAuNDUiLz4KICA8dGV4dCB4PSIxMDEyIiB5PSIxMDUiIGZvbnQtZmFtaWx5PSJDb3VyaWVyIE5ldywgbW9ub3NwYWNlIiBmb250LXNpemU9IjkuNSIgZmlsbD0iIzgxOGNmOCIgZmlsbC1vcGFjaXR5PSIwLjciPm1ldGVyIDAuOTQ8L3RleHQ+CjwvZz4KCjwhLS0gc2NhbiBsaW5lIC0tPgo8bGluZSB4MT0iOTkyIiB5MT0iODIiIHgyPSIxMTYwIiB5Mj0iODIiIHN0cm9rZT0iIzA2YjZkNCIgc3Ryb2tlLW9wYWNpdHk9IjAuMTIiIHN0cm9rZS13aWR0aD0iMC44Ii8+CjxsaW5lIHgxPSI5OTIiIHkxPSI5NCIgeDI9IjExNjAiIHkyPSI5NCIgc3Ryb2tlPSIjMDZiNmQ0IiBzdHJva2Utb3BhY2l0eT0iMC4wNiIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KCjwhLS0g4pSA4pSA4pSAIEZsb2F0aW5nIGFjY2VudCBkb3RzIOKUgOKUgOKUgCAtLT4KPGNpcmNsZSBjeD0iOTYwIiBjeT0iNDgiICByPSIyLjgiIGZpbGw9IiM2MzY2ZjEiIGZpbGwtb3BhY2l0eT0iMC42NSIgZmlsdGVyPSJ1cmwoI2dsb3cpIi8+CjxjaXJjbGUgY3g9Ijk4MCIgY3k9IjE2MCIgcj0iMiIgICBmaWxsPSIjMDZiNmQ0IiBmaWxsLW9wYWNpdHk9IjAuNTUiIGZpbHRlcj0idXJsKCNnbG93KSIvPgo8Y2lyY2xlIGN4PSI5MCIgIGN5PSIyNjAiIHI9IjIuMiIgZmlsbD0iIzYzNjZmMSIgZmlsbC1vcGFjaXR5PSIwLjQ1Ii8+CjxjaXJjbGUgY3g9IjE0MCIgY3k9IjIzNSIgcj0iMS42IiBmaWxsPSIjYTc4YmZhIiBmaWxsLW9wYWNpdHk9IjAuNSIvPgo8Y2lyY2xlIGN4PSI2OCIgIGN5PSIxOTAiIHI9IjIiICAgZmlsbD0iIzA2YjZkNCIgZmlsbC1vcGFjaXR5PSIwLjM4Ii8+CjxjaXJjbGUgY3g9IjExMzAiIGN5PSIyMzAiIHI9IjIiICBmaWxsPSIjYTc4YmZhIiBmaWxsLW9wYWNpdHk9IjAuNCIvPgoKPC9nPgo8L3N2Zz4=" width="100%" alt="Electric Meter Detection System"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-v7.0.13-00FFFF?style=for-the-badge&logo=github&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

<br/>

![Precision](https://img.shields.io/badge/Precision-95%25+-success?style=flat-square)
![Speed](https://img.shields.io/badge/Speed-152%20FPS-blueviolet?style=flat-square)
![mAP](https://img.shields.io/badge/mAP@50-0.94-orange?style=flat-square)
![Model Size](https://img.shields.io/badge/Model%20Size-14%20MB-blue?style=flat-square)
![Cost Reduction](https://img.shields.io/badge/Cost%20Reduction-90%25-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

<br/>

**Developed by [Sumit Kumar Sahu](https://github.com/sumitkumarsahu) — B.Tech CS (AI & ML)**

*Internship Project — TPCODL Field Operations Automation — 2026*

</div>

---

## 📌 Table of Contents

| # | Section |
|---|---------|
| 1 | [🧠 Project Overview](#-project-overview) |
| 2 | [❗ Problem Statement](#-problem-statement) |
| 3 | [💡 Proposed Solution](#-proposed-solution) |
| 4 | [🏆 Key Results](#-key-results) |
| 5 | [🛠️ Technology Stack](#️-technology-stack) |
| 6 | [🏗️ System Architecture](#️-system-architecture) |
| 7 | [📁 Project Structure](#-project-structure) |
| 8 | [🚀 Getting Started](#-getting-started) |
| 9 | [🔄 5-Step Pipeline](#-5-step-pipeline) |
| 10 | [🌐 Flask REST API](#-flask-rest-api) |
| 11 | [📊 Model Performance](#-model-performance) |
| 12 | [📈 Business Impact](#-business-impact) |
| 13 | [⚠️ Challenges & Solutions](#️-challenges--solutions) |
| 14 | [🔮 Future Scope](#-future-scope) |
| 15 | [🤝 Contributing](#-contributing) |
| 16 | [📄 License](#-license) |

---

## 🧠 Project Overview

> **An end-to-end AI pipeline that automatically detects electric meters in field-survey videos — deployed as a production REST API for TPCODL infrastructure integration.**

This project was built as an internship deliverable for **TPCODL (Tata Power Central Odisha Distribution Limited)** to eliminate manual meter inspection. The system processes raw survey videos, extracts frames, trains a custom YOLOv5 deep learning model, and exposes a web interface + REST API for real-world deployment.

The entire pipeline — from raw video to annotated detections — runs in under **2 hours**, compared to **40+ hours** of manual inspection per building zone.

---

## ❗ Problem Statement

Manual electric meter inspection at TPCODL was:

| Challenge | Impact |
|-----------|--------|
| ⏱ **Time Inefficiency** | 40+ hours per building zone |
| 💸 **High Cost** | ₹20,000–25,000 per inspection |
| 👁 **Human Error** | 5–10% of meters missed due to fatigue |
| 📋 **Zero Scalability** | Serial process; cannot run across multiple buildings in parallel |

These inefficiencies caused **revenue loss**, **compliance failures**, and **operational bottlenecks** across TPCODL's growing grid.

---

## 💡 Proposed Solution

A **5-step AI-powered pipeline** that goes from raw video to automated detection reports:

```
🎥 Video Input
    │
    ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Step 1         │────▶│  Step 2         │────▶│  Step 3         │
│  Frame          │     │  Data           │     │  Dataset        │
│  Extraction     │     │  Annotation     │     │  Preparation    │
│  (OpenCV)       │     │  (LabelImg)     │     │  (Python)       │
│  ~5 min         │     │  ~60 min        │     │  ~2 min         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                        ┌─────────────────────────┐
                                        │  Step 4                 │
                                        │  Model Training         │
                                        │  (YOLOv5 + Transfer     │
                                        │   Learning) ~120 min    │
                                        └─────────────────────────┘
                                                        │
                                                        ▼
                                        ┌─────────────────────────┐
                                        │  Step 5                 │
                                        │  Inference & Results    │
                                        │  (152 FPS, JSON + DB)   │
                                        └─────────────────────────┘
                                                        │
                                                        ▼
                                 📊 Detections | Bounding Boxes | Reports
```

---

## 🏆 Key Results

<div align="center">

| Metric | Value |
|--------|-------|
| 🎯 **Precision** | **95%+** |
| 📡 **Recall** | **96%** |
| 📐 **mAP@50** | **0.94** |
| ⚡ **GPU Inference Speed** | **152 FPS (6.5 ms/image)** |
| 📦 **Model Size** | **14 MB** |
| 🕒 **Training Time** | **~2 hours (RTX 3060)** |
| 🖼️ **Training Images** | **1,000** |

</div>

---

## 🛠️ Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    TECHNOLOGY STACK                         │
├──────────────────┬──────────────────────────────────────────┤
│ Language         │ Python 3.10+                             │
│ Detection Model  │ YOLOv5s v7.0.13 (transfer learning)     │
│ Deep Learning    │ PyTorch 2.0.1 + TorchVision 0.15.2      │
│ Computer Vision  │ OpenCV 4.8.1                             │
│ API Framework    │ Flask 2.3.3 + Flask-CORS 4.0.0          │
│ Image Processing │ Pillow 10.0.1                            │
│ Numerical Ops    │ NumPy 1.24.3                             │
│ Database         │ SQLite (detections.db)                   │
│ Annotation Tools │ LabelImg (primary), Roboflow, CVAT       │
│ GPU Acceleration │ CUDA (CPU fallback available)            │
└──────────────────┴──────────────────────────────────────────┘
```

---

## 🏗️ System Architecture

### Flask REST API Flow

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   CLIENT (Browser / TPCODL System / Mobile App)           │
│                │                                           │
│                │  POST /detect  (image file)               │
│                ▼                                           │
│   ┌─────────────────────────┐                             │
│   │    Flask REST API       │  ← run_flask_app.py         │
│   │    Port: 5000           │  ← app/app.py               │
│   └────────────┬────────────┘                             │
│                │  inference request                        │
│                ▼                                           │
│   ┌─────────────────────────┐                             │
│   │    YOLOv5 Model         │  ← models/best.pt           │
│   │    (PyTorch + CUDA)     │  ← 14 MB, 152 FPS           │
│   └────────────┬────────────┘                             │
│                │                                           │
│                ▼                                           │
│   JSON Response:                                           │
│   { "detections": [...], "total_meters": N,               │
│     "processing_ms": 6.5 }                               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
meter_detection_project/
│
├── 📂 data/
│   ├── 📂 videos/                  ← Input MP4/AVI survey videos
│   ├── 📂 frames/
│   │   ├── extracted/              ← Step 1 output: extracted JPG frames
│   │   └── annotated/              ← Step 2 output: YOLO .txt label files
│   └── 📂 dataset/
│       ├── images/
│       │   ├── train/              ← 700 training images (70%)
│       │   ├── val/                ← 150 validation images (15%)
│       │   └── test/               ← 150 test images (15%)
│       ├── labels/
│       │   ├── train/
│       │   ├── val/
│       │   └── test/
│       └── dataset.yaml            ← YOLO dataset config
│
├── 📂 models/
│   ├── yolov5s.pt                  ← Pretrained COCO weights (14 MB)
│   └── 📂 meter_detection/
│       └── weights/
│           └── best.pt             ← Your trained model (best checkpoint)
│
├── 📂 results/
│   └── detections/                 ← Output annotated images
│
├── 📂 src/
│   ├── config.py                   ← Config class (loads config.json)
│   ├── pipeline.py                 ← Core pipeline (step1–step5 methods)
│   └── utils.py                    ← Helper utilities
│
├── 📂 app/
│   ├── __init__.py
│   └── app.py                      ← Flask app factory + REST API routes
│
├── 📂 templates/
│   ├── index.html                  ← Detection dashboard UI
│   └── login.html                  ← Login / Signup page
│
├── 📂 uploads/                     ← Images uploaded via /api/detect
├── 📂 upload_videos/               ← Videos uploaded via /upload_video
├── 📂 yolov5/                      ← YOLOv5 submodule / library
│
├── run_step_1.py                   ← Frame extraction runner
├── run_step_2.py                   ← (Annotation — manual step)
├── run_step_3.py                   ← Dataset preparation runner
├── run_step_4.py                   ← Model training runner
├── run_step_5.py                   ← Inference runner
├── run_full_pipeline.py            ← Master runner (all 5 steps)
├── run_flask_app.py                ← Start the REST API server
├── fix_labels.py                   ← Fix annotation class ID mismatches
├── show_users.py                   ← View registered users (debug)
├── test_torch_only.py              ← Verify PyTorch install
│
├── detections.db                   ← SQLite database (detection history)
├── config.json                     ← All project settings (single source)
├── requirements.txt                ← All 9 Python dependencies
└── .env                            ← Environment variables (Flask config)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- NVIDIA GPU with CUDA (optional but recommended — CPU fallback available)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/meter-detection-project.git
cd meter-detection-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify PyTorch Installation

```bash
python test_torch_only.py
# Expected: torch version: 2.0.1 | rand: tensor([...])
```

### 5. Add Your Videos

Place your survey `.mp4` / `.avi` videos inside:

```
data/videos/
```

---

## 🔄 5-Step Pipeline

Run each step sequentially, or use the master runner:

```bash
# Run everything at once (with interactive prompts)
python run_full_pipeline.py
```

Or run steps individually:

### Step 1 — Frame Extraction

```bash
python run_step_1.py
```

> Extracts every 5th frame from input videos using OpenCV. A 60-second video at 30 FPS → ~360 JPG images saved to `data/frames/extracted/`.

### Step 2 — Data Annotation *(manual)*

Use **LabelImg** to annotate meters with bounding boxes:

```bash
pip install labelImg
labelImg data/frames/extracted/ data/frames/annotated/
```

YOLO annotation format (saved per image as `.txt`):

```
# <class_id>  <center_x>  <center_y>  <width>  <height>
0              0.45        0.32        0.25     0.30
```

> Alternatively use [Roboflow](https://roboflow.com) for cloud-based annotation with auto-export.

### Step 3 — Dataset Preparation

```bash
python run_step_3.py
```

> Splits annotated frames into **70% Train / 15% Val / 15% Test** and generates `dataset.yaml` for YOLO.

### Step 4 — Model Training

```bash
python run_step_4.py
```

> Trains YOLOv5s using transfer learning from pretrained COCO weights. Training config from `config.json`:

```json
"training": {
    "img_size": 640,
    "batch_size": 16,
    "epochs": 50,
    "device": 0,
    "patience": 20
}
```

**Training progression:**

| Epoch | Total Loss | Precision | Status |
|-------|------------|-----------|--------|
| 1/50  | 2.50       | 32%       | Learning starts |
| 10/50 | 0.80       | 71%       | Improving fast |
| 25/50 | 0.35       | 85%       | Converging |
| 50/50 | 0.22       | **95%**   | ✅ Best model saved |

### Step 5 — Inference & Results

```bash
python run_step_5.py
```

> Runs the trained `best.pt` model on the test set. Outputs annotated images + JSON detection data to `results/detections/`.

---

## 🌐 Flask REST API

### Start the Server

```bash
python run_flask_app.py
```

> Server starts at `http://localhost:5000`

### Environment Config (`.env`)

```env
FLASK_ENV=development
FLASK_APP=run_flask_app.py
API_HOST=0.0.0.0
API_PORT=5000
MODEL_PATH=models/meter_detection/weights/best.pt
DEVICE=cuda
MAX_FILE_SIZE_MB=50
```

### API Endpoint

**`POST /detect`** — Upload an image, get back detections.

```bash
curl -X POST http://localhost:5000/detect \
     -F "file=@your_image.jpg"
```

**Response:**

```json
{
  "detections": [
    {"x1": 102, "y1": 155, "x2": 220, "y2": 280, "conf": 0.96},
    {"x1": 340, "y1": 88,  "x2": 465, "y2": 205, "conf": 0.91}
  ],
  "total_meters": 2,
  "processing_ms": 6.5
}
```

### Web UI Features

| Feature | Description |
|---------|-------------|
| 🔐 Login / Signup | User authentication page |
| 📤 Image Upload | Drag and drop or browse image files |
| 🎚️ Confidence Control | Adjustable confidence threshold slider |
| 🖼️ Live Detection | Annotated output with bounding boxes |
| 📋 Detection History | Last 50 detection results with timestamps |
| ⬇️ Download History | Export detection log as CSV/JSON |

---

## 📊 Model Performance

### Final Metrics on Test Set

```
┌─────────────────────────────────────────────┐
│           MODEL EVALUATION RESULTS          │
├─────────────────┬───────────────────────────┤
│ Precision       │  95%+                     │
│ Recall          │  96%                      │
│ mAP@50          │  0.94                     │
│ Inference Time  │  6.5 ms/image             │
│ FPS (GPU)       │  152 FPS (RTX 3060)       │
│ Model Size      │  14 MB                    │
│ Conf Threshold  │  0.60                     │
│ IOU Threshold   │  0.45 (NMS)               │
└─────────────────┴───────────────────────────┘
```

### Transfer Learning — Why It Works

| Aspect | Without TL | With Transfer Learning (Ours) |
|--------|-----------|-------------------------------|
| Starting point | Random weights | YOLOv5s.pt (1.4M COCO images) |
| Images needed | 10,000+ | **1,000** |
| Training time | 5–7 days | **~2 hours** |
| Expected mAP | 70–80% | **0.94** |

---

## 📈 Business Impact

```
BEFORE  ──────────────────────────────────  AFTER
─────────────────────────────────────────────────
⏱  Time/Building   40+ hours    →    2 hours    (95% reduction)
💰  Cost/Inspect  Rs.25,000     →   Rs.2,000    (90% savings)
👁  Miss Rate      5–10%        →   < 5%        (2x fewer misses)
📊  Accuracy       ~90%         →   95%+        (+5% gain)
📋  Reports        Manual paper →   Auto JSON   (100% digital)
🔁  Scalability    1 team       →   Unlimited   (fully parallel)
```

> **ROI Positive after just 2 buildings inspected.**

---

## ⚠️ Challenges & Solutions

| Challenge | Solution Applied |
|-----------|-----------------|
| 🔴 CUDA Out-of-Memory during training | Reduced batch size from 16 to 8 |
| 🔴 Multiple annotation class IDs from different tools | `fix_labels.py` normalizes all class IDs to `0` |
| 🔴 Model overfitting on small dataset (1000 images) | Early stopping (patience=20) + SGD + weight decay |
| 🔴 PyTorch import conflicts at startup | Moved `import torch` to top of all entry scripts |
| 🔴 Annotation bottleneck with manual labeling | Supplemented LabelImg with Roboflow for speed |

---

## 🔮 Future Scope

```
1. 🏷️  Multi-class Detection    — Analog / Digital / Smart meter types
2. 📡  Real-time Video Stream   — Live CCTV / drone feed integration
3. 🤖  Edge Deployment          — Jetson Nano / Raspberry Pi for offline use
4. 🧠  Active Learning          — Model flags uncertain detections for review
5. 🌙  Night Vision Support     — Low-light images + histogram equalization
6. 🔗  TPCODL System Link       — Direct asset management DB integration
7. 🐳  Docker + Cloud Deploy    — AWS / GCP containerized deployment
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork the repo
git fork https://github.com/YOUR_USERNAME/meter-detection-project

# Create your feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "feat: add amazing feature"

# Push to the branch
git push origin feature/amazing-feature

# Open a Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ by Sumit Kumar Sahu**

*B.Tech Computer Science (AI & ML) | Internship Project 2026*

*Developed for TPCODL Field Operations Automation*

</div>
