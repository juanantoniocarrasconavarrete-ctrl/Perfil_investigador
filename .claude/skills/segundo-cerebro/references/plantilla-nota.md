# Plantilla de nota de resumen

Copia esta estructura. Todos los campos son obligatorios: si no aplica, escribe *No aplica*.

```markdown
---
fecha_procesamiento: AAAA-MM-DD
fuente: <ruta o título original, tal como aparece en /entradas/>
sha256: <hash del archivo>
etiquetas: [etiqueta-1, etiqueta-2]
---

# <Título descriptivo>

## Resumen ejecutivo
Tres a cinco frases: qué es, qué afirma y por qué importa.

## Ideas clave
- [ESTATUS] Idea 1 …
- [ESTATUS] Idea 2 …

## Conceptos relevantes
- **Concepto**: definición según el documento.

## Metodología
Cómo se obtuvo la información (método, muestra, periodo, fuentes). Si el documento no lo indica, escribe "No declarada en el documento" y márcalo como [BRECHA].

## Hallazgos y conclusiones
Resultados y conclusiones tal como los plantea el documento.

## Próximas acciones / aplicaciones prácticas
- Acción o aplicación, con responsable o contexto si el documento lo indica.

## Enlaces relacionados
- [[Nota existente]] — motivo de la relación

## Notas de procesamiento
- Advertencias, dudas de extracción o limitaciones (por ejemplo, texto ilegible o tabla no extraída).
```

## Reglas de la plantilla

- Estatus permitidos en `[ESTATUS]`: `HECHO`, `INTERPRETACIÓN`, `HIPÓTESIS`, `BRECHA`.
- `etiquetas`: minúsculas, sin tildes, con guiones. Reutiliza las etiquetas ya presentes en `INDEX.md` antes de crear nuevas.
- Enlaces con `[[Nombre exacto]]`, sin extensión `.md` ni rutas.
- La nota resume; no transcribe el documento. Si una cita literal es imprescindible, va entre comillas con su ubicación (página, minuto o sección).
