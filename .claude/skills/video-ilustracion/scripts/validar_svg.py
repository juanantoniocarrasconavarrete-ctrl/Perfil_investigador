#!/usr/bin/env python3
"""Valida que un SVG abra limpio en Illustrator. Uso: validar_svg.py archivo.svg"""
import sys, re, xml.etree.ElementTree as ET
p = sys.argv[1]; s = open(p, encoding='utf-8').read(); err, adv = [], []
try: r = ET.fromstring(s)
except ET.ParseError as e: sys.exit(f"✗ XML inválido: {e}")
if 'viewBox' not in r.attrib: err.append("falta viewBox")
if re.search(r'(href|src)\s*=\s*["\']https?:', s): err.append("referencias externas (no portable)")
if '<script' in s: err.append("contiene <script>")
if '<foreignObject' in s: err.append("foreignObject: Illustrator lo ignora")
if re.search(r'<style[^>]*>.*?(animation|@keyframes)', s, re.S): adv.append("CSS animado: Illustrator no lo ejecuta (exporte cuadro fijo)")
if '<text' in s: adv.append("hay <text>: use fuentes instaladas o conviértalo a contornos (Type > Create Outlines)")
if 'filter' in s: adv.append("filtros SVG: pueden rasterizarse en Illustrator")
for e in err: print("✗", e)
for a in adv: print("!", a)
print("✓ válido" if not err else "✗ con errores"); sys.exit(1 if err else 0)
