def home_template() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Hypernova Server — All Systems Go</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@500&display=swap');
    * { margin:0; padding:0; box-sizing:border-box; }
    body {
      height:100vh;
      overflow:hidden;
      font-family:'Orbitron',sans-serif;
      display:flex; align-items:center; justify-content:center;
      background: linear-gradient(135deg, #0b0f20, #05070c);
      position:relative;
    }
    .particles {
      position:absolute; width:100%; height:100%; background:#05070c;
      background: radial-gradient(circle at center, #001022 0%, #000 80%);
      z-index:0; overflow:hidden;
    }
    .particle {
      position:absolute; background:#00f6ff;
      opacity:0.6; border-radius:50%;
      animation: drift 6s ease-in-out infinite;
    }
    @keyframes drift {
      0% { transform: translate(0,0) scale(0.5); }
      50% { transform: translate(var(--dx), var(--dy)) scale(1); }
      100% { transform: translate(0,0) scale(0.5); }
    }
    .main {
      position:relative; z-index:2;
      background: rgba(0,0,0,0.5);
      padding:3rem 4rem;
      border:2px solid #00f6ff; border-radius:20px;
      box-shadow:
        0 0 20px #00f6ff,
        0 0 40px #ff00ff,
        0 0 80px #00f6ff;
      animation: pulseBox 5s ease-in-out infinite;
      text-align:center;
    }
    @keyframes pulseBox {
      0%,100% { transform:scale(1); box-shadow:0 0 20px #00f6ff,0 0 40px #ff00ff; }
      50% { transform:scale(1.05); box-shadow:0 0 60px #00f6ff,0 0 80px #ff00ff; }
    }
    .icon {
      font-size:6rem; color:#00f6ff;
      text-shadow:0 0 30px #00f6ff,0 0 60px #ff00ff;
      animation: rotateGlow 7s linear infinite;
    }
    @keyframes rotateGlow { 0%{transform:rotate(0deg);}100%{transform:rotate(360deg);} }
    h1 {
      margin:1rem 0; font-size:3rem; color:#fff;
      text-shadow:0 0 20px #00f6ff,0 0 40px #ff00ff;
      animation: flicker 4s infinite;
    }
    @keyframes flicker {
      0%,100% { opacity:1; }
      40%,60% { opacity:0.7; }
    }
    p {
      color:#ccc; font-family:'Rajdhani',sans-serif;
      font-size:1.3rem;
    }
  </style>
</head>
<body>
  <div class="particles" id="particles"></div>
  <div class="main">
    <div class="icon">🚀</div>
    <h1>Hypernova Server Online</h1>
    <p>System fully operational. All channels green, ready for hyperspace requests!</p>
  </div>
  <script>
    const container = document.getElementById('particles');
    for(let i=0;i<15;i++){
      const p=document.createElement('div');
      p.classList.add('particle');
      const size=Math.random()*8+4;
      p.style.width=\`\${size}px\`;
      p.style.height=\`\${size}px\`;
      p.style.top=\`\${Math.random()*100}%\`;
      p.style.left=\`\${Math.random()*100}%\`;
      p.style.setProperty('--dx', (Math.random()*200-100)+'px');
      p.style.setProperty('--dy', (Math.random()*200-100)+'px');
      p.style.animationDelay=\`\${Math.random()*3}s\`;
      container.appendChild(p);
    }
  </script>
</body>
</html>"""