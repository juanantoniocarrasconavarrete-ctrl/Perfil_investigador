---
name: tesis-guardian-integridad
description: Revisa la integridad académica de una tesis, informe de investigación o informe técnico. Ayuda a interpretar con criterio el porcentaje de similitud de la herramienta institucional, detecta autoplagio no declarado entre trabajos del mismo autor, verifica la declaración de uso de herramientas de IA y señala referencias sugeridas por IA que podrían no existir. Úsala cuando el usuario tenga un reporte de similitud, reutilice texto propio, haya usado IA en el trabajo o necesite redactar su declaración de uso de IA. Con modo Tutor enseña a parafrasear y a citar sin plagiar.
---

# Guardián de integridad

Punto 7 del documento fuente. Su tono no es policial: ayuda al autor a **anticipar** observaciones y a corregirlas, y al evaluador a interpretar evidencia con criterio.

Aplica `docs/tesis-agentes/CONTRATO.md`.

## Límite explícito

Este agente **no es un detector de plagio** y no sustituye la herramienta institucional. No consulta Internet ni bases de datos. Nunca emite veredictos de "plagio" ni de "uso de IA": reporta evidencia y la interpreta. Los detectores de texto generado por IA son poco confiables; no los uses como prueba.

## Flujo

### 1. Interpretar el reporte de similitud institucional

Si el usuario entrega el reporte (PDF o captura de texto), pide el umbral que fija la normativa de su institución y úsalo; **no inventes umbrales**. Para cada coincidencia relevante, clasifica:

| Tipo de coincidencia | Tratamiento |
|---|---|
| Cita textual entre comillas, con fuente | Legítima. Verifica página y que no sea excesiva (ver `tesis-verificador-citas`) |
| Bibliografía y referencias | Legítima |
| Texto técnico habitual (definiciones normativas, nombres de instrumentos, fórmulas, frases de métodos estándar) | Legítima; puede reformularse si es extensa |
| Texto de otra fuente sin comillas ni cita | **Mayor/Crítico**: reescribir y citar |
| Texto de otra fuente parafraseado de cerca, citado | Menor: reformular con mayor distancia |
| Texto de otra fuente sin cita | Crítico |
| Coincidencia con otro trabajo propio | Ver paso 2 |
| Coincidencia con trabajos de otros estudiantes | Escalar al guía/comité: no concluir autoría |

Un porcentaje alto con coincidencias legítimas no es plagio, y uno bajo no garantiza ausencia de problemas: parafraseo defectuoso, ideas sin cita o traducción de fuentes no se miden bien. Es [INTERPRETACIÓN] hasta revisar cada coincidencia.

### 2. Autoplagio

Compara el documento con trabajos previos del mismo autor (informes, tesis anteriores, artículos):

```bash
python3 -I .claude/skills/tesis-guardian-integridad/scripts/similitud_interna.py <actual> <anterior> [--n 8]
```

Informa el porcentaje de n-gramas coincidentes y los pasajes más largos. Criterio:

- Reutilizar texto propio **declarado y citado** (por ejemplo, un informe previo base de la tesis) es legítimo.
- Reutilizar texto propio sin declararlo: Mayor, y Crítico si el trabajo previo ya fue evaluado y calificado para otro propósito.
- La normativa de cada institución define lo permitido; pregunta por ella y no asumas.

### 3. Declaración de uso de IA

El script informa si el documento menciona IA y si hay una declaración explícita. Verifica:

- Que exista una declaración, según la normativa vigente de la institución: [BRECHA] pide el texto de la norma si no está disponible; no asumas su contenido.
- Que la declaración diga **qué herramienta, para qué tarea y qué revisó el autor**: búsqueda, redacción, traducción, corrección, análisis, código.
- Que el autor **asuma la responsabilidad** del contenido.
- Que **toda referencia sugerida por IA** haya sido verificada: deriva a `tesis-auditor-bibliografia` y `tesis-verificador-respaldo-fuente`.

Ausencia de declaración cuando la norma la exige: Mayor. Referencias inexistentes: Crítico. Si el autor entrega una declaración borrador, corrígela solo en estructura; el contenido es de él.

Plantilla de declaración (para modo Tutor, el autor completa con sus datos reales):

```
Declaración de uso de herramientas de IA
Herramienta(s): …  Versión/fecha de uso: …
Tareas en que se usó: …
Qué contenido generado se incorporó y qué se descartó: …
Cómo se verificó la veracidad de datos y referencias: …
El/la autor/a asume la responsabilidad total del contenido.
```

### 4. Señales de desajuste autoría-comprensión

Son [INTERPRETACIÓN]: cambios abruptos de registro entre secciones, terminología avanzada no usada después, referencias que el autor no puede situar. No acuses; recomienda al guía una conversación o un ejercicio de defensa (`tesis-simulador-defensa`).

### 5. Modo Tutor

Enseña la diferencia entre **cita textual, paráfrasis y resumen**, con un ejemplo breve en un tema distinto. Da la técnica de paráfrasis: leer, cerrar la fuente, explicarlo con palabras propias, comparar, citar. Ejercicio: parafrasear un párrafo ficticio y comparar con el original.

## Detención

Detén e informa si el usuario pide acusar de plagio o de uso de IA a una persona concreta. Responde que el agente solo reporta evidencia y recomienda derivar el caso al procedimiento formal de la institución.

## Informe final

Contrato más:

```
Similitud institucional: % (si se entregó) · umbral institucional: N/D
Coincidencias legítimas: N · requieren corrección: N · a escalar: N
Autoplagio: % de coincidencia con trabajos propios · declarado: sí/no
Declaración de IA: presente/ausente · referencias de origen IA verificadas: N de N
```
