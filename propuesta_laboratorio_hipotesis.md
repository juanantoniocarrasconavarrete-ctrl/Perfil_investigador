# Laboratorio de Hipótesis — Propuesta de producto y plan de desarrollo

Prototipo asociado: `taller_hipotesis.html` (archivo único, funciona sin conexión).
Estado de este documento: propuesta + registro de lo implementado, simulado y pendiente.

## 1. Síntesis del producto y usuarios

**Producto.** Plataforma interactiva que convierte la formulación de hipótesis en un proceso de aprendizaje: el usuario parte de un problema observable, construye una pregunta y una hipótesis, la descompone en piezas, la representa visualmente, la revisa con criterios transparentes y diseña cómo contrastarla. La plataforma revisa la **calidad de la formulación**; nunca declara que una hipótesis sea verdadera ni validada.

**Usuarios.**
| Usuario | Necesidad | Vista |
|---|---|---|
| Estudiante técnico-profesional (adulto trabajador, experiencia tácita) | Pasar de la experiencia a una pregunta investigable | Guiada |
| Docente / tutor de proyectos | Ver razonamiento, no solo el producto final; retroalimentar | Avanzada |
| Investigador aplicado (I+D+i) | Ordenar supuestos, indicadores y diseño de contrastación | Avanzada |

**Criterio central de éxito.** El usuario puede explicar con sus palabras qué propone, cómo se relaciona con el problema, qué supuestos contiene, qué evidencia necesitaría y qué resultados lo llevarían a modificarla (etapa 10, «Reflexión»).

## 2. Recorrido pedagógico (10 etapas)

| # | Etapa | Pregunta guía | Artefacto que queda en el modelo |
|---|---|---|---|
| 1 | Identificar el problema | ¿Qué ocurre y por qué merece investigarse? | Descripción + registro de afirmaciones (observación / interpretación / supuesto / predicción) |
| 2 | Contextualizar | ¿Dónde, a quiénes y en qué circunstancias? | Contexto, actores, consecuencias |
| 3 | Explorar antecedentes | ¿Qué información existe y qué falta? | Panel de evidencias + vacíos |
| 4 | Descomponer el problema | ¿Qué factores y relaciones propuestas hay? | Factores, consecuencias, relaciones |
| 5 | Pregunta de investigación | ¿Qué se quiere comprender o comprobar? | Pregunta + tipo |
| 6 | Construir la hipótesis | ¿Qué respuesta provisional se propone? | Hipótesis, H0, componentes, supuestos, indicadores |
| 7 | Revisión técnica | ¿Es clara, coherente, delimitada, contrastable? | 9 criterios con estado descriptivo y decisión del usuario |
| 8 | Representación visual | ¿Cómo se muestra el problema y la relación? | Mapa, diagrama, escena, secuencia (sincronizados) |
| 9 | Diseño de contrastación | ¿Qué datos, observaciones o mediciones hacen falta? | Plan de contrastación, escenarios de resultados, riesgos éticos |
| 10 | Iteración y cierre | ¿Qué debe cambiar? ¿Qué aprendí? | Versiones comparables + reflexión + entregables |

Cada etapa ofrece: preguntas orientadoras, un ejemplo (ficticio y rotulado), explicación en tres niveles (técnico / cotidiano / situado) y acceso a profundizar.

**Enfoques.** La estructura de campos cambia con el enfoque: *explicativo (efecto)*, *asociación*, *comparación de grupos* y *exploratorio* (sin hipótesis: solo pregunta). No se impone estructura causal a todos.

## 3. Módulos y funcionalidades

| Módulo | Función | Prototipo |
|---|---|---|
| Recorrido guiado | 10 etapas, vista guiada/avanzada | Implementado |
| Registro de afirmaciones | Separar observación, interpretación, supuesto, predicción | Implementado |
| Descomposición de la hipótesis | Componentes editables + resaltado en el texto | Implementado |
| Conceptos en 3 niveles | Técnico, cotidiano, situado (17 conceptos) | Implementado |
| Vista multidimensional | Humana, conceptual, empírica, metodológica, contextual, ética | Implementado |
| Lienzo visual | Mapa del problema, diagrama de variables, escena, secuencia, escenarios | Implementado |
| Sincronización texto↔visual | Avisa qué visuales quedaron desactualizados | Implementado |
| Panel de evidencias | Vincula evidencia a afirmaciones, con clase (dato real / observación / ilustración / hipotético) | Implementado |
| Tutor | Preguntas, ambigüedades, contradicciones, causalidad sin fundamento; aceptar / rechazar / modificar | **Simulado** (reglas locales, sin IA generativa) |
| Panel de revisión | 9 criterios, estados descriptivos, decisión del usuario | Implementado |
| Versiones | Guardar, comparar, comentar, decidir | Implementado |
| Escenarios de resultados | Compatibles, que cuestionan, mixtos, alternativas, no previstos | Implementado (texto + proyección rotulada) |
| Simulación de sensibilidad | Poder, falsas alarmas, sesgo por confusora con datos **sintéticos** | Implementado (rotulado «no es evidencia») |
| Exportación | Markdown, HTML editable, impresión/PDF, PNG/SVG del mapa, JSON | Implementado |
| Generación de imágenes | Solo prompts y carga manual | Pendiente de integración |
| IA generativa | Tutor con LLM | Pendiente de integración |
| Búsqueda de antecedentes | Fuentes bibliográficas | Pendiente (la app no inventa fuentes) |
| Carga y análisis de datos reales | CSV → contraste | Pendiente |
| Colaboración / docente | Comentarios multiusuario | Pendiente |
| Exportación nativa .docx / .pdf | — | Pendiente (hoy HTML + impresión) |

## 4. Pantallas y navegación

Tres espacios relacionados, siempre visibles en pantallas anchas:

```
┌ Encabezado: título · [Guiada|Avanzada] · Estado del prototipo · Guardar/Exportar ┐
│ Recorrido: ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩  (navegación por teclado, estado «con contenido») │
├──────────────────────┬────────────────────────────┬───────────────────────────────┤
│ PANEL DE CONSTRUCCIÓN│ LIENZO VISUAL              │ PANEL DE ACOMPAÑAMIENTO       │
│ campos de la etapa   │ pestañas: mapa · variables │ propósito · preguntas         │
│ listas editables     │ escena · secuencia ·       │ ejemplo ficticio              │
│ revisión (etapa 7)   │ escenarios · evidencias ·  │ conceptos en 3 niveles        │
│ versiones (etapa 10) │ dimensiones · historial    │ tutor: aceptar/rechazar/mod.  │
└──────────────────────┴────────────────────────────┴───────────────────────────────┘
```
En pantallas angostas los tres espacios se apilan. Accesibilidad: enlace «saltar al contenido», todo operable con teclado, foco visible, contraste AA, `aria-live` para estados, alternativa textual para cada visualización y entrada numérica como alternativa al clic sobre imágenes.

## 5. Modelo de datos

```
Proyecto(enfoque, modo)
 ├─ Problema(ocurre, porque)            ├─ Afirmacion[](texto, tipo)
 ├─ Contexto(donde, cuando, circ)       ├─ Actor[](nombre, rol, consecuencia)
 ├─ Evidencia[](tipo, descripcion, fuente, clase, vinculo→Afirmacion|Hipotesis|Supuesto)
 ├─ Vacios(texto)                       ├─ Factor[](texto, relacion) · Consecuencia[](texto, actor)
 ├─ Pregunta(texto, tipo)
 ├─ Hipotesis(texto, nula, cotidiana)   ├─ Componentes(unidad, tiempo, x, y, direccion, mecanismo,
 │                                      │   confusoras, fundamento, indicadores, instrumentos,
 │                                      │   condicion_de_cuestionamiento, alcance, limitaciones)
 ├─ Supuesto[](texto, tipo)
 ├─ Visual(imagen, tipo_imagen, marcas[], pasos[], escena_actual, escena_posible, instantanea_de_sincronizacion)
 ├─ Contrastacion(datos, muestra, analisis, viabilidad, riesgos_eticos, privacidad)
 ├─ Escenario(compatible, cuestiona, mixto, alternativa, imprevisto)
 ├─ Revision(criterio → decision, nota)  ← el estado se calcula, la decisión es del usuario
 ├─ DecisionTutor(id_sugerencia → aceptada | rechazada | modificada)
 ├─ Version[](fecha, instantanea, que_cambio, comentarios, fundamento)
 └─ Reflexion(5 respuestas)
```
Persistencia del prototipo: `localStorage` + exportación/importación JSON. Los estados de revisión no se almacenan: se **derivan** de los datos, de modo que no pueden quedar inconsistentes.

## 6. Arquitectura técnica

**Prototipo (implementado).** Un solo HTML con CSS y JS embebidos, sin dependencias ni build. Justificación: se abre sin instalación, funciona sin conexión, es auditable por un docente y portable entre equipos de DUOC UC. Límite: sin multiusuario, sin servidor, sin IA generativa.

**Producción (propuesta).**
- Cliente: aplicación web (TypeScript + framework de componentes), el mismo modelo de datos, visuales SVG generados desde el modelo.
- Servicio: API REST + base relacional (proyectos, versiones, comentarios), almacenamiento de archivos para imágenes.
- Capa de IA desacoplada: el tutor consume un contrato JSON (ver §7) y puede ser reglas locales o un modelo de lenguaje intercambiable.
- Privacidad: minimizar datos enviados al modelo, pedir consentimiento antes de enviarlos, permitir modo totalmente local.

## 7. Integración del asistente de IA y de los recursos visuales

**Contrato del tutor** (entrada: estado del proyecto + etapa; salida: lista de sugerencias):
```json
{ "id":"h_vag_mejora", "tipo":"Ambigüedad", "texto":"…", "porque":"…",
  "propuesta": {"campo":"h.texto","reemplazar":"mejora","por":"episodios de dolor ≥3/10"} }
```
Reglas de seguridad pedagógica (aplicadas hoy por el motor local y exigibles a cualquier modelo):
1. Preguntar antes de redactar: no ofrece alternativas de hipótesis hasta que el usuario escribió un borrador.
2. No inventar datos, fuentes ni resultados; solo señala qué falta.
3. Toda sugerencia explica su razón y puede aceptarse, rechazarse o modificarse; queda registrada.
4. Nunca expresa que una hipótesis esté validada o sea verdadera.

**Recursos visuales.** Mapas y diagramas se generan de forma determinista desde el modelo (no son texto libre), por lo que pueden señalar cuándo quedaron desactualizados. Toda imagen lleva una clase obligatoria (ilustración, registro de observación, dato real, escenario hipotético) y una descripción textual; los gráficos con datos sintéticos llevan rótulo visible «simulado — no es evidencia». La generación de imágenes con IA queda pendiente; hoy la plataforma entrega prompts y acepta imágenes propias.

## 8. Alcance del producto mínimo viable

**Dentro del MVP (prototipo actual):** recorrido completo de 10 etapas, cuatro enfoques, descomposición, mapa y diagrama, escena con marcas, secuencia, evidencias, revisión de 9 criterios, versiones con comparación, escenarios, simulación sintética, tutor por reglas, exportaciones locales, vista guiada/avanzada, accesibilidad básica.
**Fuera del MVP:** IA generativa, generación de imágenes, búsqueda bibliográfica, análisis de datos reales, multiusuario, .docx/.pdf nativos.

## 9. Criterios de aceptación y pruebas

| # | Criterio de aceptación |
|---|---|
| A1 | Dado un proyecto vacío, cuando el usuario avanza por las 10 etapas, entonces cada etapa muestra preguntas, ejemplo y conceptos en tres niveles. |
| A2 | Dado un enfoque exploratorio, entonces no se exige hipótesis y la revisión evalúa la pregunta. |
| A3 | Dado que el usuario aún no escribió un borrador, entonces el tutor no ofrece alternativas de redacción. |
| A4 | Dada una sugerencia del tutor, el usuario puede aceptarla, rechazarla o modificarla y la decisión queda registrada. |
| A5 | Dado un cambio en una variable, entonces el lienzo indica qué visualizaciones requieren actualización. |
| A6 | Dada una imagen cargada, entonces no puede guardarse sin clase y se muestra siempre con su rótulo. |
| A7 | Todo gráfico con datos generados por la app muestra el rótulo «simulado / no es evidencia». |
| A8 | La revisión muestra estados descriptivos, nunca una puntuación de validez. |
| A9 | Dadas dos versiones guardadas, se muestran los campos que cambiaron con valor anterior y nuevo. |
| A10 | El usuario obtiene los entregables: ficha, pregunta, hipótesis y componentes, representación, matriz variable–indicador, supuestos y limitaciones, contrastación, escenarios, historial, reflexión. |
| A11 | Toda la aplicación es operable con teclado y cada visual tiene alternativa textual. |
| A12 | Sin conexión, la aplicación funciona y conserva los datos. |

**Pruebas.** (1) Unitarias de funciones estadísticas contra valores de referencia (p de t, n requerido, poder); (2) extremo a extremo con navegador automatizado recorriendo las 10 etapas; (3) accesibilidad: recorrido por teclado y revisión de contraste; (4) **estudio con usuarios**: ¿mejora la capacidad de explicar la hipótesis con las propias palabras? Esto último es una hipótesis del producto, aún [BRECHA]: no existe evidencia de impacto pedagógico y debe medirse (p. ej. diseño pre-post con grupo de comparación).

## 10. Plan de desarrollo por etapas

| Fase | Contenido | Resultado |
|---|---|---|
| 0 | Prototipo monolítico del recorrido central | **Hecho** |
| 1 | Pilotos con 2–3 cursos; ajustar textos, ejemplos y criterios; instrumentos de medición del aprendizaje | MVP validado con usuarios |
| 2 | Tutor con modelo de lenguaje tras el contrato JSON; consentimiento y modo local | Tutor generativo con salvaguardas |
| 3 | Backend, cuentas, vista docente, comentarios, exportación nativa | Uso institucional |
| 4 | Generación de imágenes, carga de datos reales y contraste, evaluación de impacto | Versión de producción |
