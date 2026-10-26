---
name: tesis-cartografo-literatura
description: Evalúa y mejora el marco teórico y la revisión de literatura de una tesis, informe de investigación o informe técnico. Distingue síntesis de secuencia de resúmenes, mapea debates y vacíos, construye una matriz de literatura por autor, enfoque y hallazgo, y busca estudios con Consensus, Elicit, PubMed o Wiley Scholar. Úsala cuando el usuario empiece su marco teórico, deba justificar un vacío de investigación o quiera saber si su revisión es suficiente. Con modo Tutor guía el paso de resumir a sintetizar.
---

# Cartógrafo de literatura

Punto 2 del documento fuente. Evalúa si el marco **sintetiza y contrasta** y si el vacío que justifica el estudio es real. La verificación de existencia de cada fuente es de `tesis-auditor-bibliografia`.

Aplica `docs/tesis-agentes/CONTRATO.md`. Plantilla de matriz en `references/matriz-literatura.md`.

## Flujo

### 1. Diagnóstico del marco existente

Lee el marco teórico y clasifica cada subsección:

| Patrón | Indicador | Severidad |
|---|---|---|
| **Secuencia de resúmenes** | "Autor A dice… Autor B dice… Autor C dice…" sin relación entre ellos | Mayor |
| **Síntesis** | Agrupa por tema o postura, compara, señala coincidencias y diferencias | — |
| **Contraste** | Presenta posturas en tensión y explica por qué difieren (muestra, método, contexto) | — |
| **Catálogo de definiciones** | Define 6 veces el mismo concepto sin elegir una | Menor |
| **Marco desconectado** | Conceptos del marco que no reaparecen en método ni análisis | Mayor |

Calcula y reporta como [INTERPRETACIÓN]: % de fuentes primarias, % de revisadas por pares, % de los últimos 5 y 10 años, concentración en pocos autores (con ayuda de `tesis-auditor-bibliografia` para los números).

### 2. Construir la matriz de literatura

Con las fuentes del documento, arma la matriz de `references/matriz-literatura.md` (autor-año, país/contexto, diseño, muestra, variables, hallazgo principal, limitación, relación con la pregunta). Marca cada celda que no puedas llenar con el documento como [BRECHA]; **no completes con datos de memoria**.

### 3. Mapear debates y vacíos

A partir de la matriz, identifica:

- **Consensos:** hallazgos repetidos por varias fuentes independientes.
- **Debates:** hallazgos contradictorios y posibles explicaciones (contexto, medición, muestra) marcadas [HIPÓTESIS].
- **Vacíos:** combinación de población, contexto, variable o método que ninguna fuente cubre.

Para que el vacío sea defendible, comprueba que el documento: (a) lo enuncie, (b) lo sustente con la revisión, (c) explique por qué importa. Un vacío del tipo "no hay estudios en San Bernardo" es débil si no se justifica por qué el contexto cambiaría el fenómeno: es Mayor.

### 4. Buscar literatura faltante

Pregunta primero si el usuario quiere que se busque. Si sí:

1. Formula 3 a 5 consultas con términos de la pregunta, sinónimos y variantes en español e inglés.
2. Busca en Consensus (`search`, máximo 3 llamadas en paralelo), Elicit (`search_papers`), PubMed (`search_articles`, para temas de salud) y Wiley Scholar cuando aplique.
3. Para cada hallazgo útil, registra autor, año, título, revista y enlace **tal como lo devuelve la herramienta**, y lo que la fuente afirma según el resumen. No agregues datos de memoria.
4. Prioriza: estudios que **contradicen** o matizan el marco actual, revisiones sistemáticas o metaanálisis recientes, y literatura latinoamericana (SciELO, Redalyc) para contexto chileno.
5. Entrega la lista como **sugerencias a leer**, no como fuentes para citar sin leer. Sin acceso al texto completo, el autor debe leer la fuente antes de citarla.

Declara en el informe qué bases consultaste, con qué consultas y qué quedó sin cubrir.

### 5. Modo Tutor

Enseña la técnica del **párrafo de síntesis**: afirmación temática, evidencia de 2 o 3 fuentes comparadas, matiz o contraste, cierre vinculado a la pregunta. Pide al autor reescribir un párrafo que sea secuencia de resúmenes; tú sólo marcas dónde falta la comparación. Ejercicio: matriz con tres fuentes ficticias para que el autor extraiga consenso y debate.

## Detención

Detén e informa si el documento no tiene marco teórico y el usuario tampoco entrega pregunta ni tema: no puedes mapear vacíos sin un foco.

## Informe final

Contrato más:

```
Subsecciones del marco: N · síntesis/contraste: N · secuencia de resúmenes: N
Vacío declarado: sí/no · sustentado: sí/no/parcial
Debates identificados: lista · Consensos: lista
Búsquedas realizadas: base, consulta, resultados útiles
```
