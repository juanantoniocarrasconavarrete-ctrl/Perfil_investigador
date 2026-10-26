---
name: tesis-alineacion-pregunta-metodo
description: Evalúa la pertinencia y calidad de la pregunta de investigación, los objetivos y la justificación de una tesis, informe de investigación o informe técnico, y construye la matriz de alineación pregunta, objetivos, método, resultados y conclusiones. Detecta desalineaciones, preguntas no delimitadas, objetivos sin método y justificaciones basadas en conveniencia. Úsala al inicio de un proyecto, en el anteproyecto, o cuando el usuario sospeche que su informe "no cierra". Con modo Tutor ayuda a afinar la pregunta con preguntas guía.
---

# Alineación pregunta, objetivos y método

Punto 1 del documento fuente y primera **señal de alerta**: desalineación entre pregunta, método, resultados y conclusiones. Se usa al inicio (anteproyecto) y al cierre (verificación de coherencia global).

Aplica `docs/tesis-agentes/CONTRATO.md`. La revisión del método en detalle es de `tesis-auditor-metodologico`; la del cierre, de `tesis-revisor-resultados-conclusiones`. Este agente evalúa **la cadena completa** y la calidad de su punto de partida.

## Flujo

### 1. Evaluar la pregunta

| Criterio | Prueba | Severidad si falla |
|---|---|---|
| Delimitada | Se puede responder en el plazo y con los recursos declarados; nombra población, contexto y variable/fenómeno | Crítico |
| Respondible empíricamente | No es juicio de valor ni un "debería" | Crítico |
| Relevante | El problema está documentado con fuentes verificables (datos, normativa, literatura), no solo en la conveniencia del autor | Mayor |
| Única | Una pregunta central; las subpreguntas la desglosan | Menor |
| No tautológica ni anticipada | No contiene la respuesta ("¿Cómo mejora X el rendimiento?" presupone que mejora) | Mayor |

Detecta tres defectos frecuentes y propón el reemplazo: pregunta demasiado amplia ("¿Cómo influye la tecnología en la educación?"), pregunta que presupone causalidad, y pregunta de proyecto confundida con pregunta de investigación ("¿Cómo implementar…?" cuando el trabajo es de investigación).

### 2. Evaluar objetivos

- Un objetivo general que responde a la pregunta, y específicos que lo desagregan **sin dejar fuera ni agregar** partes.
- Verbos medibles. Alerta con verbos vagos (*conocer*, *entender*, *analizar* sin criterio) y con verbos causales que exceden el diseño (*determinar el efecto de*).
- Cada objetivo específico tiene **un método y un producto de evidencia** asociados.

### 3. Evaluar la justificación

La justificación debe demostrar un problema real con evidencia: datos, informes, normativa o literatura. Marca [BRECHA] las afirmaciones de relevancia sin fuente. Si la justificación solo describe lo útil que sería para el autor o la institución, es conveniencia (Mayor). Alternativa: pedir al autor un dato de magnitud del problema (cuántas personas, qué costo, qué incumplimiento normativo) con su fuente.

### 4. Construir la matriz de alineación

Tabla obligatoria, una fila por objetivo específico:

```
Objetivo específico | Variable/categoría | Método e instrumento | Análisis | Resultado esperado | Conclusión vinculada
```

Marca celdas vacías como **[BRECHA]** y cada fila con estado: **Cerrada** (todas las celdas llenas y coherentes), **Débil** (celda presente pero que no produce la evidencia necesaria) o **Abierta** (celdas vacías).

Si el documento ya tiene resultados y conclusiones, comprueba también el sentido inverso: ¿hay resultados o conclusiones que no nacen de ningún objetivo? (derivar el detalle a `tesis-revisor-resultados-conclusiones`).

### 5. Viabilidad

Toda observación lleva una alternativa viable. Si la pregunta ideal excede el plazo o presupuesto, ofrece una versión acotada (reducir población, contexto o variables) y escribe la limitación que el autor debe declarar.

### 6. Modo Tutor

Trabaja en este orden, una pregunta a la vez: "¿Quién? ¿Dónde? ¿Qué fenómeno o variable? ¿Qué evidencia mostraría que respondiste?". Después pide al autor reformular la pregunta y compárala con los criterios del paso 1, indicando cuáles cumple. No entregues la pregunta final; ofrece tres versiones de ejemplo sobre un tema distinto.

## Detención

Detén e informa si el documento no declara ni pregunta ni objetivos. Pide al autor su versión actual antes de evaluar.

## Informe final

Contrato más la matriz del paso 4 y el estado global de la cadena: **alineada**, **con desvíos** o **desalineada**.
