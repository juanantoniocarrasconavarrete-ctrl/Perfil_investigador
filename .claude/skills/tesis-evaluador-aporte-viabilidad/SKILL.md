---
name: tesis-evaluador-aporte-viabilidad
description: Evalúa el aporte de una tesis, informe de investigación o informe técnico y la viabilidad de sus recomendaciones. Determina qué aporta que no existía antes y para quién, y comprueba si las implicancias son aplicables en el contexto chileno según presupuesto, normativa vigente, tiempos y capacidades de los usuarios. Aplica el Filtro Yoko (cobertura, coherencia, aplicabilidad, accesibilidad). Úsala al cerrar un informe o al diseñar las recomendaciones. Con modo Tutor ayuda a formular un aporte defendible.
---

# Evaluador de aporte y viabilidad

Punto 9 del documento fuente. Distingue entre un trabajo correcto y un trabajo **útil**.

Aplica `docs/tesis-agentes/CONTRATO.md`.

## Flujo

### 1. Declarar el aporte

Extrae del documento qué dice aportar y a quién. Clasifica el tipo:

| Tipo de aporte | Evidencia que lo sostiene |
|---|---|
| **Teórico** (concepto, modelo, relación) | Contrastación con literatura y datos |
| **Empírico** (dato nuevo de un contexto) | Muestra, método y alcance declarados |
| **Metodológico** (instrumento, procedimiento) | Validación y reutilización posible |
| **Aplicado** (solución, protocolo, prototipo) | Prueba en contexto real y criterios de éxito |
| **Replicación** | Condiciones comparables a las del estudio original |

Preguntas de control:

1. ¿Qué existe ya sobre lo mismo (derivar la búsqueda a `tesis-cartografo-literatura`)?
2. ¿Qué es lo nuevo exactamente: contexto, población, método, combinación?
3. ¿Quién se beneficia y quién podría usarlo mañana?

Aporte declarado que ya existe en la literatura revisada: Mayor. Aporte sin destinatario identificado: Mayor. Aporte exagerado respecto de lo que muestran los datos: Mayor (ver `tesis-revisor-resultados-conclusiones`). Un aporte modesto pero honesto es válido: no lo penalices.

### 2. Evaluar la viabilidad de recomendaciones

Para **cada recomendación**, arma esta ficha. Lo que no esté en el documento, pídelo al autor o márcalo como [BRECHA]; **no inventes costos ni normas**.

```
Recomendación:
Actor responsable (quién la ejecuta):
Costo estimado y fuente de la estimación (CLP):
Plazo de implementación:
Normativa chilena aplicable (cuál y qué exige):
Capacidades requeridas (formación, equipos, turnos):
Riesgos y supuestos:
Evidencia de la tesis que la respalda (resultado/ubicación):
```

Reglas de contexto:

- **Presupuesto:** compara con el orden de magnitud realista del destinatario; una recomendación que exige una inversión fuera de su alcance debe presentarse como etapa futura, con una alternativa de menor costo. Como referencia de este proyecto, un microproyecto de aula ronda los $150.000 CLP.
- **Normativa chilena:** toda recomendación que toque seguridad, salud, datos o educación debe nombrar la norma vigente y verificarse en una fuente oficial (por ejemplo, Ley 20.949 de manejo manual de cargas, normas sectoriales, Ley 19.628 y Ley 21.719 de datos personales). [BRECHA] Confirma vigencia y alcance en la fuente oficial antes de afirmarlo; no confíes en memoria.
- **Tiempos reales:** turnos, calendario académico, ciclos de presupuesto.
- **Población:** adultos trabajadores con experiencia previa, tiempo comprimido y acceso desigual a tecnología: la implementación debe respetarlo.

### 3. Filtro Yoko (FY)

Antes de cerrar, evalúa cada recomendación y el conjunto:

| Eje | Pregunta | Estado |
|---|---|---|
| Cobertura | ¿Aborda todas las competencias, variables y hallazgos clave? | ✔ / parcial / ✘ |
| Coherencia | ¿Se alinean teoría, resultados y propuesta? | ✔ / parcial / ✘ |
| Aplicabilidad | ¿Es viable con el presupuesto y tiempos reales? | ✔ / parcial / ✘ |
| Accesibilidad | ¿Puede entenderla y ejecutarla el destinatario sin formación especial? | ✔ / parcial / ✘ |

Una recomendación con dos ejes en ✘ debe reformularse; con uno en ✘, ajustarse. Hallazgos: recomendación sin respaldo en resultados: Mayor; recomendación inviable sin alternativa: Mayor; omisión de la normativa aplicable: Mayor, y Crítico si la recomendación la infringiría.

### 4. Alternativa regenerativa

Por cada recomendación débil, propone una versión viable con el formato: **[Quiebre] → [Alternativa] → [Verificación de viabilidad]**.

### 5. Modo Tutor

Guía con: "¿Quién haría esto, con qué dinero, bajo qué norma y en cuánto tiempo?". El autor llena la ficha; tú señalas campos vacíos o poco realistas. Ejercicio: reducir una recomendación ficticia de $2.000.000 CLP a una versión de $150.000 manteniendo el objetivo.

## Detención

Detén e informa si el documento no tiene recomendaciones ni implicancias: en ese caso evalúa sólo el aporte e indica que la viabilidad no aplica.

## Informe final

Contrato más:

```
Tipo de aporte y destinatario
Recomendaciones evaluadas: N · viables: N · ajustables: N · a reformular: N
Normas verificadas en fuente oficial: lista · sin verificar: lista
Filtro Yoko: cobertura / coherencia / aplicabilidad / accesibilidad
```
