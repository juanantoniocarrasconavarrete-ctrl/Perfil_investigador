---
name: tesis-revisor-resultados-conclusiones
description: Revisa los capítulos de resultados, discusión y conclusiones de una tesis, informe de investigación o informe técnico. Verifica que resultados e interpretación estén separados, que las conclusiones respondan a los objetivos sin introducir temas nuevos, detecta sobreinterpretación (correlación como causalidad, un caso como tendencia), confronta la discusión con la literatura incluyendo contradicciones y exige limitaciones explícitas. Úsala cuando el usuario pida revisar conclusiones, la discusión o la consistencia entre objetivos y hallazgos. Con modo Tutor guía la redacción sin escribirla.
---

# Revisor de resultados, discusión y conclusiones

Es el punto 5 del documento fuente y, junto con metodología y citación, uno de los tres puntos de mayor poder de detección de debilidad sustantiva ([HIPÓTESIS] del documento fuente).

Aplica `docs/tesis-agentes/CONTRATO.md`.

## Flujo

### 1. Construir la matriz objetivo → resultado → conclusión

Extrae los objetivos del documento y, para cada uno, localiza el resultado que lo responde y la conclusión que lo cierra. Tabla obligatoria:

```
Objetivo | Resultado que lo responde (ubicación) | Conclusión (ubicación) | Estado
```

Estados: **Alineado**, **Resultado sin objetivo** (huérfano), **Objetivo sin resultado**, **Conclusión sin resultado** (infundada), **Conclusión sobre tema no investigado**.

| Hallazgo | Severidad |
|---|---|
| Objetivo sin resultado ni conclusión | Crítico |
| Conclusión sin resultado que la sostenga | Crítico |
| Conclusión sobre un tema no investigado | Mayor |
| Resultado relevante sin objetivo que lo explique | Menor |

### 2. Separación resultado / interpretación

En el capítulo de resultados, marca frases que interpretan: *esto demuestra*, *se debe a*, *lo que indica que*, *gracias a*, adjetivos valorativos (*excelente*, *preocupante*). Interpretar dentro de resultados no es error grave si el diseño lo permite (cualitativo con análisis integrado), pero debe declararse. Para diseños cuantitativos: Menor si ocurre, Mayor si la interpretación contradice los datos.

### 3. Detectar sobreinterpretación

Revisa cada conclusión con esta lista; cada coincidencia es un hallazgo con ubicación y cita de la frase:

| Patrón | Ejemplo | Severidad |
|---|---|---|
| Correlación presentada como causa | "El taller **produjo** una mejora del 20%" sin grupo de control | Crítico |
| Caso o muestra pequeña → tendencia | "Los trabajadores del rubro **tienden** a…" con n = 8 | Mayor |
| Significancia estadística = relevancia práctica | p < 0,05 con efecto despreciable | Mayor |
| Ausencia de efecto = efecto nulo | p > 0,05 interpretado como "no hay diferencia" con muestra pequeña | Mayor |
| Generalización fuera de la población muestreada | muestra de una sede → "los estudiantes de Chile" | Mayor |
| Porcentajes de submuestras minúsculas sin n | "75%" con 3 de 4 casos | Menor |
| Resultado exploratorio como confirmación | hipótesis surgida del análisis presentada como previa | Mayor |
| Recomendación sin base en resultados | propuesta que no se deriva de ningún hallazgo | Mayor |

Alternativa regenerativa por patrón: reescribe **el patrón** con ejemplo en otro tema, o propone el verbo adecuado (*se asoció con*, *en esta muestra*, *es compatible con*), no la frase del autor completa en modo Tutor.

### 4. Discusión frente a la literatura

Verifica que la discusión:

1. Retome los hallazgos principales y los compare con **al menos** los estudios del marco teórico que trataron lo mismo.
2. Incluya los hallazgos que **no coinciden** con la literatura y ofrezca explicaciones posibles marcadas como [HIPÓTESIS].
3. No introduzca literatura nueva que no esté en el marco (Menor) ni use la discusión para repetir el marco teórico (Menor).
4. No se limite a resumir resultados (Mayor).

Si la discusión solo cita estudios coincidentes: señálalo como [BRECHA] de rigor y sugiere buscar evidencia en contra con las herramientas disponibles (Consensus, Elicit, PubMed). Pregunta primero si el usuario quiere esa búsqueda.

### 5. Limitaciones

Debe existir un apartado explícito que cubra, según corresponda: muestra, diseño, instrumentos, contexto, sesgos (selección, deseabilidad social, del investigador) y alcance de la generalización.

- Ausencia total: Mayor.
- Limitaciones genéricas ("el tiempo fue corto") sin relación con las conclusiones: Menor.
- Limitaciones declaradas pero ignoradas en las conclusiones (se afirma lo que la limitación impide): Mayor.
- Limitaciones minimizadas ("no afectan los resultados") sin evidencia: Mayor.

### 6. Calidad de las conclusiones

Una conclusión sólida: responde al objetivo, está acotada a la muestra, indica el grado de certeza, señala implicancias viables en el contexto (presupuesto, normativa chilena, tiempos) y propone líneas futuras derivadas de las limitaciones.

### 7. Modo Tutor

Trabaja con la matriz del paso 1: el autor la completa y tú señalas celdas vacías. Para sobreinterpretación, pide: "Subraya el verbo de tu conclusión. ¿Qué diseño necesitarías para sostener ese verbo?" y deja que reformule. Cierra con un ejercicio: tres frases ficticias, el autor identifica cuál sobreinterpreta y por qué.

## Detención

Detén e informa si el documento no declara objetivos o si los capítulos de resultados y conclusiones no están presentes. Sin objetivos no hay matriz: pide el documento completo o los objetivos.

## Informe final

Contrato más la matriz del paso 1, la lista de patrones de sobreinterpretación con la frase y su ubicación, y el estado de las limitaciones (ausentes / genéricas / adecuadas).
