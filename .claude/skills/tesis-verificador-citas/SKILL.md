---
name: tesis-verificador-citas
description: Revisa las citas en texto de una tesis, informe de investigación o informe técnico (APA 7) y las cruza con la lista de referencias. Detecta citas huérfanas, referencias sin citar, citas textuales sin página o excesivas, formato de cita incorrecto y paráfrasis o datos sin atribución. Úsala cuando el usuario pida revisar citas, verificar que todo lo citado esté en la bibliografía o corregir el sistema de citación. Con modo Tutor enseña a citar.
---

# Verificador de citas

Audita el vínculo **texto ↔ lista final**. No evalúa si las fuentes existen (eso es `tesis-auditor-bibliografia`) ni si dicen lo que se afirma (eso es `tesis-verificador-respaldo-fuente`).

Aplica `docs/tesis-agentes/CONTRATO.md` (modos, anti-alucinación, severidad, informe final).

## Entrada

Archivo `.docx`, `.md` o `.txt` con encabezado *Referencias* o *Bibliografía*. Si es PDF, extrae el texto primero; si no puedes, detente e informa (no revises de memoria).

## Flujo

### 1. Extraer y cruzar

```bash
python3 -I .claude/skills/tesis-verificador-citas/scripts/extraer_citas.py <archivo>
```

La salida JSON trae `citas`, `referencias`, `huerfanas`, `sin_citar`, `textuales` y `advertencias`. Si `advertencias` indica que no halló la lista de referencias, pídele al usuario la ubicación; no inventes el cruce.

### 2. Validar la salida del script

El script es heurístico. Antes de reportar, revisa a mano cada hallazgo del script contra el texto:

- **Falso huérfano:** autor con apellido compuesto, acento distinto, o dos obras del mismo autor y año (`2020a`, `2020b`).
- **Cita no detectada:** el script no ve citas con formatos atípicos (autor institucional con sigla, citas en notas al pie, "citado en"). Haz una lectura de control de al menos una sección completa.

Reporta como [BRECHA] las secciones que no leíste.

### 3. Revisar criterios APA 7 en el texto

| Criterio | Hallazgo | Severidad |
|---|---|---|
| Cita en texto sin referencia en la lista | huérfana | Crítico |
| Referencia sin ninguna cita en el texto | sin citar | Menor |
| Cita textual sin página (`p.`/`pp.`) | falta localizador | Mayor |
| Cita textual ≥ 40 palabras entre comillas | debe ir en bloque con sangría | Menor |
| Más de 3 citas textuales largas seguidas o textuales que superan ~10% de una sección | exceso de cita textual | Mayor |
| 3+ autores citados con lista completa en la primera mención | usar *et al.* desde la primera cita (APA 7) | Menor |
| Mezcla de estilos (numérico + autor-año, `y` + `&` en paréntesis) | inconsistencia | Menor |
| Dato, cifra, figura o idea claramente ajena sin cita | atribución ausente | Mayor; Crítico si es dato central de la tesis |
| Mismo autor y año sin sufijo `a`/`b` | ambigüedad | Menor |
| Cita secundaria sin "como se citó en" | fuente no consultada declarada como leída | Mayor |

Para atribución ausente: busca párrafos con cifras, porcentajes, años, definiciones o verbos de autoridad ("se ha demostrado", "la literatura indica") sin cita. Es [INTERPRETACIÓN]: el autor puede estar usando conocimiento propio; formula como pregunta.

### 4. Modo Tutor

Por cada tipo de error distinto (máximo 3 por sesión), explica la regla, muestra un ejemplo **con un autor ficticio de otro tema** y pide al autor corregir su caso. No reescribas sus citas. Cierra con un mini-ejercicio de 3 ítems.

## Detención

Detén e informa si el archivo no se puede leer, está vacío o no contiene lista de referencias y el usuario no la entrega. No sigas con un cruce parcial presentándolo como completo.

## Informe final

Sigue el formato del contrato y agrega:

```
Citas detectadas: N · Referencias: N
Huérfanas: lista · Sin citar: lista
Citas textuales con problema: N
Falsos positivos descartados del script: N
```
