---
name: tesis-verificador-respaldo-fuente
description: Comprueba que las fuentes citadas en una tesis, informe de investigación o informe técnico realmente respaldan lo que el texto afirma. Detecta citas no leídas, atribuciones falsas, afirmaciones que exageran el hallazgo original y datos mal transcritos. Úsala cuando el usuario sospeche de referencias sugeridas por IA, pida validar afirmaciones clave contra la fuente o quiera auditar el marco teórico. Con modo Tutor enseña a leer y citar con fidelidad.
---

# Verificador de respaldo de la fuente

Responde una pregunta: **¿la fuente dice lo que el texto le atribuye?** Es el control más costoso, así que se aplica por muestreo dirigido, no sobre todo el documento.

Aplica `docs/tesis-agentes/CONTRATO.md`. Requiere que `tesis-auditor-bibliografia` haya confirmado que la fuente existe; no verifiques respaldo de una referencia cuya existencia está en duda.

## Flujo

### 1. Seleccionar las afirmaciones a verificar

Extrae del documento las afirmaciones de mayor peso, en este orden de prioridad:

1. Datos numéricos, porcentajes y tamaños de efecto atribuidos a una fuente.
2. Afirmaciones que fundamentan la pregunta, la justificación o el vacío de investigación.
3. Definiciones centrales y decisiones metodológicas "según X".
4. Afirmaciones causales ("X provoca Y") con cita.
5. Citas textuales.

Máximo **15 afirmaciones por ejecución** (ajustable por el usuario). Declara en el informe el criterio de selección y cuántas afirmaciones totales quedaron sin verificar.

### 2. Obtener el pasaje fuente

Orden de acceso, deteniéndote en el primero que dé texto utilizable:

1. El usuario entrega el PDF o el fragmento (siempre preferible).
2. Texto completo abierto: PubMed (`get_full_text_article`, solo si `get_copyright_status` lo permite), Elicit (`get_library_source_full_text` si el paper está en su biblioteca), Wiley Scholar (`search_wiley_fulltext`).
3. Resumen y metadatos vía Consensus, Elicit o PubMed.
4. Si solo hay resumen, el veredicto máximo es *Compatible con el resumen*: nunca *Respaldado*.

Si no obtuviste el pasaje, el estatus es [BRECHA] y pides al usuario el fragmento. No uses tu memoria sobre el contenido del paper como evidencia.

### 3. Comparar y clasificar

Para cada afirmación, cita el pasaje de la fuente (con página o sección) junto a la frase del texto, y clasifica:

| Veredicto | Significado | Severidad |
|---|---|---|
| **Respaldado** | La fuente dice lo mismo, con el mismo alcance | — |
| **Respaldado con matiz** | Dice lo mismo, pero el texto omite una condición o limitación del original | Menor |
| **Exagerado** | El texto generaliza más que la fuente (muestra, contexto, fuerza causal) | Mayor |
| **Distorsionado** | El texto cambia el sentido, la cifra o el sentido causal | Crítico |
| **No respaldado** | La fuente no trata el tema; la cita parece decorativa | Crítico |
| **Contradicho** | La fuente afirma lo opuesto | Crítico |
| **Compatible con el resumen** | Solo se pudo leer el resumen | [BRECHA] |
| **Sin acceso** | No se obtuvo texto | [BRECHA] |

Fíjate especialmente en: correlación del original tratada como causalidad, muestra de un contexto (país, nivel educativo) generalizada, hallazgo "no significativo" citado como efecto, y cifras transpuestas.

### 4. Señales de cita no leída

Son [INTERPRETACIÓN]; no acuses de mala fe, presenta como preguntas al autor:

- Cita que respalda algo que el paper no trata, pero cuyo título suena afín.
- Mismas 3-5 fuentes citadas siempre juntas, sin diferenciar aportes.
- Cita a una obra de revisión para un hallazgo que corresponde a un estudio primario dentro de ella (falta "como se citó en").
- Referencia plausible que no existe (derivar a `tesis-auditor-bibliografia`).

### 5. Modo Tutor

Toma 2 afirmaciones del autor y haz el ejercicio con él: "Lee el párrafo 3 de la fuente. ¿Qué dice exactamente sobre tu muestra? ¿Coincide con lo que escribiste?". Enséñale la técnica *afirmación → pasaje → alcance* y a escribir una paráfrasis que conserve la fuerza del original (verbos: *sugiere*, *se asocia con*, *encontró*, *demostró* solo con diseño experimental).

## Detención

Detén e informa si no hay lista de referencias ni forma de acceder a ninguna fuente. Presenta lo verificado y lo no verificado por separado; no mezcles.

## Informe final

Contrato más una tabla:

```
Afirmación (ubicación) | Fuente | Pasaje de la fuente (ubicación) | Veredicto | Corrección propuesta
```

y los conteos: afirmaciones totales detectadas · verificadas con texto completo · solo con resumen · sin acceso.
