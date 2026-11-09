---
name: video-ilustracion
description: Crea videos animados (MP4) e ilustraciones vectoriales (SVG/PDF editables en Adobe Illustrator) a partir de una escena SVG/HTML monolítica y determinista, renderizada con Chromium + ffmpeg. Úsala cuando el usuario pida un video animado, explainer, infografía animada, motion graphic, ilustración vectorial, ícono, diagrama o material visual para clases (BSC, mapas estratégicos, casos FT, simulaciones), o exportar algo a Illustrator.
---

# Video animado e ilustración vectorial

Una sola fuente (`escena.html`, SVG + JS, offline, sin build) produce tres salidas: **MP4**, **SVG/PDF para Illustrator** y **PNG**. Modo de salida al usuario: `[HERRAMIENTA]` (código/archivos) con `[BACKSTAGE]` para el guion.

## Enrutamiento (decidir primero)

| Pedido | Ruta |
|---|---|
| Video explicativo/infografía animada, estilo propio, offline | **Esta skill** |
| Video con música sintetizada, personajes, voz, narrativa larga | `animation-studio:animation-studio` |
| GIF corto para chat | `anthropic-skills:slack-gif-creator` |
| Edición/Render sobre material real (recortes, formatos) | MCP Adobe `video_*` / `adobe-for-creativity:*` |
| Diseño de póster/slide editable en Express/Canva/Figma | `create_visual_design_express_skill`, Canva, Figma |
| Ilustración que se abrirá y retocará en Illustrator | **Esta skill** → `exportar_ilustracion.js` |

Limitación honesta: no se controla Illustrator directamente. El puente es SVG/PDF (Illustrator abre ambos con capas por `<g id>`). Un `.ai` nativo requiere guardarlo desde Illustrator.

## Requisitos
`node` + `playwright` (Chromium), `ffmpeg`, `python3`. Verifique: `which ffmpeg node; node -e "require('playwright')"`. Si falta algo, informe y no instale sin consultar.

## Flujo

1. **Brief (≤1 ronda de preguntas):** objetivo de aprendizaje/mensaje, público, duración (default 20–45 s), formato (16:9 aula; 9:16 redes), idioma (es-CL), ¿audio?
2. **Guion por beats** `[BACKSTAGE]`: una idea por escena (M-D: núcleo conceptual → poda → ritmo apretar-aflojar). Máx. ~2,5 palabras/s si hay texto en pantalla. Aplicar Bloom 4–6 si es material de aula.
3. **Escena:** copiar `templates/escena.html` a un directorio de trabajo y reemplazar el contenido. Contrato obligatorio:
   - `window.CFG = {fps, duracion, ancho, alto}`
   - `window.renderAt(t)` **pura**: mismo `t` → mismo cuadro. Prohibido `Math.random`, `Date.now`, `setTimeout`, CSS `@keyframes`.
   - Aleatoriedad solo con PRNG sembrado. Easing/`tramo()` ya incluidos.
   - Estructura con `<g id="...">` semánticos (capas legibles en Illustrator). Texto ≥ 28 px en 720p; márgenes seguros 5 %.
4. **Revisión visual (obligatoria antes del render final):**
   ```bash
   node scripts/exportar_ilustracion.js escena.html 0.5 out/t05   # cuadro clave
   node scripts/exportar_ilustracion.js escena.html 5.5 out/t55
   ```
   Leer los PNG; criticar legibilidad, solapes, contraste, orden de lectura. Corregir y repetir.
5. **Borrador y final:**
   ```bash
   node scripts/render_video.js escena.html out/borrador.mp4 --draft
   node scripts/render_video.js escena.html out/final.mp4 [--audio pista.wav] [--fps 30]
   ```
   Renders >2 min: `run_in_background`.
6. **Ilustración para Illustrator:**
   ```bash
   node scripts/exportar_ilustracion.js escena.html <t> out/ilustracion   # .svg .pdf .png
   python3 scripts/validar_svg.py out/ilustracion.svg
   ```
   Resolver los `✗`; los `!` se comunican (texto → *Create Outlines*; filtros pueden rasterizarse).
7. **Entrega:** rutas, duración, resolución, tamaño; qué se verificó (cuadros revisados, validación SVG) y qué no (audio no escuchado, apertura real en Illustrator no probada).

## Filtro Yoko (antes de entregar material de aula)
- Cobertura: ¿cubre las variables/competencias del brief?
- Coherencia: ¿narración, visual y evaluación alinean?
- Aplicabilidad: ¿corre offline, sin licencias, con ~$150k CLP?
- Accesibilidad: contraste ≥ 4,5:1, texto legible a distancia, sin depender solo del color, subtítulos si hay voz.

## Reglas anti-fallo
- Datos y cifras en pantalla: etiquetar [HECHO]/[HIPÓTESIS]; no inventar normativa ni resultados.
- Sin fuentes externas por URL (render offline): usar `Arial/Helvetica` o incrustar la fuente en base64.
- Sin imágenes remotas; incrustar como `data:` o dibujar en vectores.
- No publicar/subir/commitear sin que el usuario lo pida.
- Si una escena supera ~60 s o necesita personajes y música, derivar a `animation-studio`.

## Archivos
- `templates/escena.html` — plantilla (ejemplo: BSC de 4 perspectivas, 6 s).
- `scripts/render_video.js` — HTML → MP4 (H.264, `+faststart`), `--draft`, `--audio`, `--png-dir`.
- `scripts/exportar_ilustracion.js` — congela `t` → SVG + PDF + PNG.
- `scripts/validar_svg.py` — chequeo de portabilidad a Illustrator.
