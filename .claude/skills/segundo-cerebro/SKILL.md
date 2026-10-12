---
name: segundo-cerebro
description: Procesa los archivos nuevos de /entradas/ (transcripciones, artículos, documentos) y genera notas de resumen enlazadas en /cerebro/resumenes/, actualizando /cerebro/INDEX.md. Úsala cuando el usuario pida procesar entradas, ingerir documentos al segundo cerebro, resumir material pendiente o actualizar el índice de conocimiento.
---

# Segundo cerebro: ingesta de conocimiento

Procesa material pendiente de `/entradas/` y lo integra en la base de conocimiento Obsidian de `/cerebro/`. Cada ejecución es un lote: detecta, resume, enlaza, indexa e informa.

## Rutas

| Ruta | Función |
|---|---|
| `/entradas/` | Fuente. Material pendiente (solo lectura). |
| `/cerebro/resumenes/` | Destino de las notas de resumen. |
| `/cerebro/INDEX.md` | Índice navegable de todas las notas. |
| `/cerebro/.procesados.json` | Registro de control (ver formato abajo). |
| `references/plantilla-nota.md` | Estructura obligatoria de cada nota. |
| `scripts/pendientes.py` | Clasifica las entradas por contenido. Solo lectura. |

Si `/cerebro/` no existe o no tiene `resumenes/`, `INDEX.md` o `.procesados.json`, créalos vacíos (el registro como `{"procesados": []}`) y repórtalo como advertencia. No es un error.

## Parámetros

- **Límite de lote:** 10 notas creadas o actualizadas por ejecución. Si el usuario indica otro valor, úsalo.
- **Formatos admitidos:** `.md`, `.txt`, `.vtt`, `.srt`, `.csv`, `.json`, `.pdf`, `.docx`.

## Flujo

### 1. Detectar pendientes

Ejecuta:

```bash
python3 .claude/skills/segundo-cerebro/scripts/pendientes.py --entradas /entradas --cerebro /cerebro
```

La salida es JSON con `pendientes`, `ya_procesados` y `omitidos`. Si el script termina con error de lectura o de registro corrupto, detén la ejecución e informa (ver *Detención*).

Si `pendientes` está vacío, termina con el estado **Sin pendientes** e informa. No es un error.

### 2. Leer cada archivo pendiente

- Lee el contenido completo antes de resumir. Un documento parcialmente leído produce resúmenes falsos.
- `.pdf` y `.docx` requieren extraer el texto con las herramientas disponibles. Si no puedes extraerlo, muévelo a `omitidos` con el motivo *formato no legible* y continúa.
- Un archivo corrupto o vacío se omite con motivo y no detiene el lote.

### 3. Analizar

Identifica, en este orden: tesis o propósito, ideas clave, conceptos relevantes (con su definición en el texto), metodologías, hallazgos, conclusiones y acciones recomendadas.

Marca el estatus de las afirmaciones relevantes con las etiquetas del sistema:

- **[HECHO]**: dato o norma verificable en el propio documento.
- **[INTERPRETACIÓN]**: deducción del autor o tuya, sujeta a contexto.
- **[HIPÓTESIS]**: proposición que el documento plantea y no demuestra.
- **[BRECHA]**: vacío de información o riesgo que el documento no cubre.

No añadas conocimiento externo al documento. Si lo consideras útil, va en la sección *Enlaces relacionados* con la nota existente que lo contenga, nunca como hecho de la nota nueva.

### 4. Buscar relaciones antes de crear

Antes de crear una nota:

1. Comprueba que el `sha256` no esté ya en el registro (el script ya lo hace; no lo repitas a mano).
2. Busca notas existentes con temas afines en `/cerebro/resumenes/` (nombre, etiquetas y títulos de `INDEX.md`).
3. Si una nota existente cubre el mismo contenido (mismo documento con otro nombre o versión), **actualízala** en lugar de crear un duplicado. Registra la actualización.
4. Usa los nombres exactos de las notas existentes para los enlaces `[[Nota]]`. Mantén la terminología ya usada en el repositorio.

### 5. Escribir la nota

- Usa `references/plantilla-nota.md`. Todos sus campos son obligatorios; si un campo no aplica, escribe *No aplica* y no lo elimines.
- Nombre de archivo: `resumenes/<Título en formato corto>.md`. Sin caracteres que Obsidian rechace (`# | ^ [ ] :`).
- Frontmatter YAML con `fecha_procesamiento`, `fuente`, `etiquetas` y `sha256`.
- Enlaces bidireccionales: en cada nota existente relacionada, añade el enlace a la nueva en su sección *Enlaces relacionados*. **Añade, nunca borres ni reescribas el contenido existente.**

### 6. Actualizar INDEX.md

Añade la nota nueva (o actualiza su entrada) en la sección temática correspondiente, en orden alfabético dentro de la sección. Formato de cada línea:

```
- [[Nombre de la nota]] — resumen de una línea · `etiqueta1`, `etiqueta2`
```

Si `INDEX.md` no puede escribirse, detén la ejecución (ver *Detención*). Una nota sin entrada en el índice cuenta como fallida.

### 7. Registrar

Tras crear o actualizar cada nota con éxito, añade su entrada a `/cerebro/.procesados.json`:

```json
{"procesados": [
  {"sha256": "…", "archivo": "sub/entrada.md", "nota": "[[Nombre de la nota]]", "procesado": "AAAA-MM-DD"}
]}
```

Registra solo después de escribir la nota y actualizar el índice. Así un fallo a mitad de camino no deja un archivo marcado como procesado sin nota.

### 8. Repetir

Vuelve al paso 2 mientras existan pendientes y no hayas alcanzado el límite de lote. Si el límite se alcanza con pendientes restantes, termina con el estado **Lote completo, quedan pendientes** e indícalo en el informe.

## Detención

**Detén inmediatamente** e informa al usuario si ocurre cualquiera de estos casos:

1. Error de permisos o de lectura/escritura en `/entradas/`, `/cerebro/` o sus archivos de control.
2. `.procesados.json` o `INDEX.md` no se pueden leer, están corruptos o no se pueden escribir.
3. Inconsistencia crítica en la base: `INDEX.md` enlaza a notas que no existen, dos notas tienen el mismo nombre o el mismo `sha256` aparece en dos notas distintas.
4. Se alcanza el límite de lote.

Otros casos **no detienen** el lote: un archivo con formato no admitido, vacío, corrupto o ilegible se omite con motivo y se continúa con el siguiente.

## Informe final

Entrega siempre este informe, aunque no haya pendientes:

```
Estado: [Sin pendientes | Completado | Lote completo, quedan pendientes | Detenido: <causa>]
Archivos detectados: N
Archivos procesados: N
Notas creadas: [[…]], …
Notas actualizadas: [[…]], …
Omitidos: archivo — motivo
Enlaces generados: N (lista de origen → destino)
Errores y advertencias: lista, o "Ninguno"
Pendientes restantes: N
```

No omitas incidencias, conflictos ni limitaciones. Si una nota se creó pero su entrada en el índice falló, repórtalo como fallida y no la registres.
