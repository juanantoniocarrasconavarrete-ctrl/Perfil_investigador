---
name: tesis-auditor-estadistico
description: Audita el análisis de datos de una tesis, informe de investigación o informe técnico. Verifica que las pruebas correspondan al tipo de variable y a sus supuestos, recalcula los valores p reportados, detecta señales de búsqueda selectiva de significancia u omisión de resultados negativos, revisa tamaño del efecto y potencia, y evalúa la reproducibilidad de datos, scripts y software. Úsala cuando el usuario pida revisar estadística, validar p-valores, elegir una prueba o preparar un análisis reproducible. Con modo Tutor enseña a elegir y reportar pruebas.
---

# Auditor estadístico

Punto 4 del documento fuente. Evalúa **el análisis**, no el diseño (`tesis-auditor-metodologico`) ni la interpretación (`tesis-revisor-resultados-conclusiones`).

Aplica `docs/tesis-agentes/CONTRATO.md`.

## Flujo

### 1. Recalcular los valores p reportados

```bash
python3 -I .claude/skills/tesis-auditor-estadistico/scripts/statcheck.py <archivo>
```

Reconoce `t`, `F`, `χ²` y `r` en formato APA (por ejemplo `t(28) = 2.10, p = .045`) y recalcula el p con los grados de libertad. Python puro, sin dependencias.

- Reportado ≠ recalculado: Mayor. Si cambia la decisión respecto de α = .05: Crítico.
- Solo reconoce lo escrito en formato APA. Pruebas con otro formato (tablas pegadas como imagen, salidas de software) quedan como [BRECHA]: pide los datos o la tabla en texto.
- El script no sabe si la prueba era de una o dos colas ni si hubo correcciones (Welch, Greenhouse-Geisser): si el resultado difiere levemente, pregunta antes de concluir que hay error.

### 2. Señal de búsqueda selectiva

El script cuenta valores p entre .040 y .049 frente a .050 y .059. Un exceso de los primeros es una **señal, no una prueba**. Además, revisa en el texto:

- Número de pruebas realizadas vs. número de pruebas reportadas (¿hay variables medidas que no aparecen?).
- Múltiples comparaciones sin corrección (Bonferroni, Holm, FDR) ni declaración de que el análisis es exploratorio.
- Hipótesis formuladas después de ver los resultados presentadas como previas.
- Resultados negativos o no significativos omitidos o relegados.
- Subgrupos analizados sin justificación previa.

Formula como pregunta al autor: "Hay N variables en el instrumento y se reportan M; ¿dónde están el resto?". Si la omisión se confirma: Mayor.

### 3. Pertinencia de la prueba

Para cada análisis, verifica con esta tabla:

| Situación | Prueba habitual | Supuestos a declarar y verificar |
|---|---|---|
| 2 grupos independientes, variable continua | t de Student/Welch; Mann-Whitney | Normalidad (o n suficiente), homogeneidad de varianzas, independencia |
| 2 mediciones pareadas | t pareada; Wilcoxon | Normalidad de las diferencias |
| 3+ grupos | ANOVA; Kruskal-Wallis | Normalidad de residuos, homocedasticidad, post hoc corregido |
| Variable ordinal | pruebas no paramétricas; correlación de Spearman | Escala ordinal justificada |
| Dos categóricas | χ² / Fisher | Frecuencias esperadas ≥ 5 (si no, Fisher) |
| Asociación continua | Pearson / Spearman | Linealidad, valores atípicos |
| Predicción | regresión lineal/logística | Independencia, multicolinealidad, tamaño muestral por predictor |
| Escala (Likert) con ítems | confiabilidad (α/ω), análisis factorial | Tamaño muestral y estructura declarados |

Hallazgos típicos: ANOVA con n = 5 por grupo sin verificar normalidad (Mayor), t de Student con datos ordinales (Mayor), correlación de Pearson con valores atípicos extremos no discutidos (Menor), Likert de un solo ítem tratado como variable continua sin justificar (Menor).

### 4. Tamaño del efecto, intervalos y potencia

- Todo contraste debe informar **tamaño del efecto** (d, r, η², OR) e idealmente **IC 95 %**. Ausencia: Mayor.
- Muestras de conveniencia pequeñas: pregunta por la potencia. Resultados no significativos con potencia baja no permiten concluir ausencia de efecto: esa conclusión es Mayor.
- Distingue **significancia estadística** de **relevancia práctica**; ver también `tesis-revisor-resultados-conclusiones`.

### 5. Reproducibilidad

Lista de verificación:

- Base de datos disponible o descripción de cómo acceder a ella, anonimizada.
- Diccionario de variables y codificación.
- Script o procedimiento paso a paso (R, Python, SPSS sintaxis, Excel con fórmulas visibles).
- Versión del software y de los paquetes.
- Tratamiento de datos perdidos y valores atípicos declarado.
- Si procede, semilla aleatoria.

Ausencia total de trazabilidad de los datos: Crítico. Ausencia de script: Mayor. Si el análisis es manual (Excel), pide las celdas de cálculo.

Si el usuario entrega los datos, **reproduce** el análisis principal con Python (pandas, statsmodels) y compara con lo reportado; informa las diferencias. Si no los entrega, declara [BRECHA]: *reproducción no realizada*.

### 6. Modo Tutor

Pregunta primero por la pregunta de investigación y el tipo de variables, y deja que el autor elija la prueba con la tabla del paso 3. Explica cómo reportar en APA 7 (estadístico, gl, p exacto, tamaño del efecto, IC), con ejemplo numérico inventado. No ejecutes el análisis por él salvo para ilustrar con datos ficticios.

## Detención

Detén e informa si el documento no contiene análisis cuantitativo (por ejemplo, estudio cualitativo): en ese caso solo ofrece revisar el rigor del análisis cualitativo (codificación, triangulación, saturación) con `tesis-auditor-metodologico`.

## Informe final

Contrato más:

```
Pruebas reconocidas: N · Inconsistentes: N · Cambian decisión: N
p entre .040 y .049: N · entre .050 y .059: N
Pruebas sin supuestos verificados: lista
Reproducibilidad: datos [sí/no] · script [sí/no] · software [sí/no] · reproducción realizada [sí/no]
```
