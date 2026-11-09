#!/usr/bin/env node
// Uso: node exportar_ilustracion.js escena.html t salida_base
// Congela renderAt(t) y exporta <salida_base>.svg (editable en Illustrator) + .pdf (vectorial) + .png.
const path = require('path'), fs = require('fs');
const [escena, t, base] = process.argv.slice(2);
if (!escena || t === undefined || !base) { console.error('Uso: exportar_ilustracion.js escena.html t salida_base'); process.exit(2); }
(async () => {
  const { chromium } = require('playwright');
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://' + path.resolve(escena));
  const cfg = await pg.evaluate(() => window.CFG);
  await pg.setViewportSize({ width: cfg.ancho, height: cfg.alto });
  await pg.evaluate(x => window.renderAt(x), +t);
  const svg = await pg.evaluate(() => { const s = document.querySelector('svg').cloneNode(true);
    s.setAttribute('xmlns', 'http://www.w3.org/2000/svg'); s.removeAttribute('style'); s.removeAttribute('id');
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + s.outerHTML; });
  fs.writeFileSync(base + '.svg', svg);
  await pg.screenshot({ path: base + '.png' });
  await pg.pdf({ path: base + '.pdf', width: cfg.ancho + 'px', height: cfg.alto + 'px', printBackground: true, pageRanges: '1' });
  await b.close();
  console.log(`OK ${base}.svg/.pdf/.png`);
})().catch(e => { console.error(e.message); process.exit(1); });
