#!/usr/bin/env node
// Uso: node render_video.js escena.html salida.mp4 [--draft] [--fps N] [--audio pista.wav] [--png-dir dir]
// Renderiza renderAt(t) cuadro a cuadro con Chromium (Playwright) y codifica con ffmpeg. Determinista.
const { spawn } = require('child_process');
const path = require('path'), fs = require('fs');
const args = process.argv.slice(2);
const flag = (n, d) => { const i = args.indexOf(n); return i < 0 ? d : args[i + 1]; };
const [escena, salida] = args.filter(a => !a.startsWith('--') && a !== flag('--fps') && a !== flag('--audio') && a !== flag('--png-dir'));
if (!escena || !salida) { console.error('Uso: render_video.js escena.html salida.mp4 [--draft] [--fps N] [--audio f] [--png-dir d]'); process.exit(2); }
const draft = args.includes('--draft');
(async () => {
  const { chromium } = require('playwright');
  const b = await chromium.launch();
  const p0 = await b.newPage();
  await p0.goto('file://' + path.resolve(escena));
  const cfg = await p0.evaluate(() => window.CFG);
  if (!cfg || typeof (await p0.evaluate(() => typeof window.renderAt)) !== 'string') throw new Error('Falta window.CFG o renderAt');
  await p0.close();
  const fps = +flag('--fps', cfg.fps || 30), esc = draft ? .5 : 1;
  let W = Math.round(cfg.ancho * esc), H = Math.round(cfg.alto * esc); W -= W % 2; H -= H % 2;
  const page = await b.newPage({ viewport: { width: W, height: H } });
  await page.goto('file://' + path.resolve(escena));
  const n = Math.round(cfg.duracion * fps), pngDir = flag('--png-dir');
  if (pngDir) fs.mkdirSync(pngDir, { recursive: true });
  const ff = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
  const audio = flag('--audio'); if (audio) ff.push('-i', audio);
  ff.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', draft ? '28' : '18', '-preset', draft ? 'veryfast' : 'medium');
  if (audio) ff.push('-c:a', 'aac', '-shortest');
  ff.push('-movflags', '+faststart', salida);
  const enc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
  const fin = new Promise(r => enc.on('close', r));
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.renderAt(t), i / fps);
    const png = await page.screenshot({ type: 'png' });
    if (pngDir) fs.writeFileSync(path.join(pngDir, `f${String(i).padStart(5, '0')}.png`), png);
    if (!enc.stdin.write(png)) await new Promise(r => enc.stdin.once('drain', r));
  }
  enc.stdin.end(); const code = await fin; await b.close();
  if (code) process.exit(code);
  console.log(`OK ${salida} · ${n} cuadros · ${fps} fps · ${W}x${H} · ${cfg.duracion}s`);
})().catch(e => { console.error(e.message); process.exit(1); });
