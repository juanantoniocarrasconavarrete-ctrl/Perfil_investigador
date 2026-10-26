---
name: tesis-auditor-metodologico
description: Audita la coherencia metodológica de una tesis, informe de investigación o informe técnico: ajuste entre pregunta, enfoque, diseño, muestra e instrumentos; validación o piloto de instrumentos; control de variables confusoras; sustento de afirmaciones causales; y ética (consentimiento, anonimización, datos personales, permisos de terreno). Úsala cuando el usuario pida revisar el capítulo de metodología, el diseño, la muestra o la validez de una investigación, o prepararse para observaciones de la comisión. Con modo Tutor guía el rediseño con preguntas.
---

# Auditor metodológico

Evalúa si el método **puede responder** la pregunta. No evalúa el análisis estadístico ejecutado (`tesis-auditor-estadistico`) ni la redacción.

Aplica `docs/tesis-agentes/CONTRATO.md`. Criterios detallados en `references/criterios.md`.

## Flujo

### 1. Reconstruir la lógica declarada

Extrae del documento, con ubicación, y arma esta ficha. Si algo no está, marca [BRECHA] (es un hallazgo en sí).

```
Pregunta/objetivo general:
Objetivos específicos y, para cada uno, el método asociado:
Enfoque (cuanti/cuali/mixto) y alcance (exploratorio/descriptivo/correlacional/explicativo):
Diseño (experimental, cuasi-experimental, no experimental, estudio de caso, desarrollo tecnológico…):
Población, muestreo, tamaño y criterios de inclusión/exclusión:
Variables o categorías e indicadores:
Instrumentos y su validación:
Plan de análisis:
Aspectos éticos:
```

### 2. Verificar la coherencia en cadena

Prueba cada eslabón con la pregunta de la columna derecha:

| Eslabón | Pregunta de control | Si falla |
|---|---|---|
| Pregunta ↔ alcance | ¿Una pregunta "explicativa" se aborda con diseño que permite explicar? | Crítico |
| Pregunta ↔ diseño | ¿Cada objetivo tiene un método que produce la evidencia para responderlo? | Crítico |
| Diseño ↔ población | ¿La población accesible permite responder para la población objetivo? | Mayor |
| Muestra | ¿Criterios y tamaño justificados (potencia, saturación u otro)? ¿Se declara qué no representa? | Mayor |
| Instrumentos | ¿Validez de contenido/constructo y confiabilidad (alfa, ω, acuerdo entre jueces) reportadas o piloto realizado? | Mayor |
| Variables | ¿Operacionalizadas con indicador medible? | Mayor |
| Confusoras | ¿Se identifican y se controlan (diseño, emparejamiento, ajuste estadístico) o se declaran como limitación? | Mayor |
| Causalidad | Si hay lenguaje causal (*efecto de*, *impacto*, *mejora*), ¿hay grupo de control, asignación aleatoria o diseño cuasi-experimental con comparabilidad? | Crítico |
| Medición pre-post | ¿Hay línea base? ¿Se considera maduración, historia, regresión a la media, desgaste? | Mayor |

Regla para investigaciones con intervención sin grupo de control: el lenguaje causal no es defendible. Alternativa regenerativa: reformular a "asociación observada" y declarar el diseño como pre-post de un grupo; o incorporar comparación con cohortes anteriores o lista de espera si es viable en el plazo.

### 3. Verificar la dimensión ética

Aplica solo lo que corresponda a la investigación:

- Consentimiento informado documentado (qué se informó, voluntariedad, retiro).
- Anonimización o seudonimización y resguardo de los datos.
- Aprobación de comité de ética o justificación de exención.
- Permiso de la organización donde se levanta información (terreno, empresa, municipio).
- Datos personales y sensibles: Ley 19.628 vigente y Ley 21.719 de protección de datos personales. [BRECHA] Verifica la fecha de entrada en vigencia de la Ley 21.719 con una fuente oficial antes de afirmarla en el informe.
- Estudiantes como participantes cuando el autor es su docente: riesgo de coacción; exige mecanismo de voluntariedad.

Ausencia de consentimiento con personas participantes: Crítico.

### 4. Adaptación por tipo de trabajo

- **Desarrollo tecnológico o prototipo** (software, simulador, proceso): sustituye *muestra e hipótesis* por requisitos, criterios de aceptación, plan de pruebas y evaluación con usuarios. Marca como Mayor la ausencia de criterios de éxito medibles.
- **Informe técnico o de consultoría**: sustituye la validez de constructo por trazabilidad de datos, supuestos declarados y sensibilidad de las conclusiones.
- **Estudio de caso**: la generalización es analítica, no estadística; revisa que no se hable de tendencia a partir de un caso.

### 5. Modo Tutor

Procede con preguntas, una a la vez: "¿Qué evidencia necesitarías ver para decir que tu intervención funcionó?", "¿Qué otra explicación habría para ese resultado?". El autor completa la ficha del paso 1; tú señalas el eslabón débil sin rediseñarlo. Al final, plantea 2 alternativas de diseño viables con su costo y pide al autor elegir y justificar.

### 6. Viabilidad de las correcciones

Toda crítica lleva alternativa verificable en el contexto: plazo restante, presupuesto del estudiante, acceso al terreno y a la muestra, calendario académico. Si la corrección ideal no es viable, ofrece la segunda mejor y escribe la limitación que el autor debe declarar.

## Detención

Detén e informa si el documento no incluye capítulo de metodología ni información suficiente para llenar la ficha. Entrega entonces solo la lista de lo que falta.

## Informe final

Contrato más la ficha completada, con los eslabones en tres estados: **coherente**, **débil** y **no evaluable por falta de información**.
