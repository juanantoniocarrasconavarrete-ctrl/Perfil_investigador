# Revisión por agente: Reporte Perfil Docente Investigador (agosto–diciembre)

**Documento revisado:** `5d53e0a0-2025_PAUTA_REPORTE_PERFIL.docx` (12 páginas renderizadas, incluye tablas y anexos como imágenes).
**Fecha del documento:** 05 de enero de 2026.
**Modo:** Tutor para cada hallazgo (explica el criterio y dónde corregir). Sin redactar el texto del autor.

## Cómo leer esta revisión

- **Ubicación:** sección, tabla o fila, según el orden del documento.
- **Severidad:** Crítico, Mayor o Menor, según `docs/tesis-agentes/CONTRATO.md`.
- **[HECHO / INTERPRETACIÓN / HIPÓTESIS / BRECHA]:** estatus de cada afirmación.
- Los ejemplos de redacción son **ficticios** y solo ilustran la forma; no sustituyen contenido del autor.

## Adaptación de los agentes a este documento

Los agentes se diseñaron para tesis. Este documento es un **reporte de desempeño con proyectos en curso**, así que:

- Algunos agentes no tienen material que revisar (estadístico, similitud, respaldo de fuente). Lo declaro en cada sección.
- Otros se aplican sobre partes que el documento no trae (la lista de referencias, el plan de trabajo). Su ausencia es el hallazgo.

---

## 1. `tesis-alineacion-pregunta-metodo`

**Criterio pedagógico:** un objetivo sirve si dice qué se va a medir, en qué población o condición, y con qué método se obtiene esa evidencia. Si falta uno de esos tres elementos, el lector no puede comprobar nada.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| Tabla de detalle, **Islas climatológicas**, fila *Objetivo del Proyecto* | "Crear un software de análisis de temperatura móvil". | Mayor | El objetivo habla de software, pero el resumen de la misma tabla describe intervenciones físicas (superficies reflectantes, pavimentos fríos, arborización). Define cuál es el producto principal. Si el software es un medio para priorizar intervenciones, el objetivo debe decirlo: *"Priorizar zonas de intervención de isla de calor mediante monitoreo térmico con sensores, en la comuna de San Bernardo"*. |
| Tabla de detalle, **Islas**, fila *Resumen* | Promete "reducción promedio de hasta 3 °C" sin indicar cómo se medirá ni contra qué línea base. | Mayor | Ver sección 3 (diseño). Agrega una frase: *"La reducción se medirá comparando temperatura superficial en zonas intervenidas y zonas de control durante N semanas."* |
| Tabla de detalle, **Bomberos 132**, fila *Objetivo del Proyecto* | "juego online que busca mejorar, educar y democratizar la gestión de riesgo…". Es una descripción del producto, no un objetivo: no tiene verbo medible ni población precisa. | Mayor | Formula un objetivo medible. Ejemplo ficticio: *"Evaluar si el uso del juego aumenta la proporción de decisiones correctas en un simulacro, en estudiantes de 8 a 12 años, frente a un grupo que recibe material tradicional."* |
| Tabla de detalle, **ECOWIND**, fila *Objetivo General* | "Alcanzar la generación efectiva de energía limpia y renovable como resultado principal" es un resultado esperado, no un objetivo. No indica cuánta energía ni bajo qué viento. | Mayor | Cuantifica. Ejemplo ficticio: *"Obtener una potencia nominal de X W a una velocidad de viento de Y m/s, medida en prueba de Z horas."* |
| Tabla de detalle, **ECOWIND**, *Objetivos Específicos* | "Adaptabilidad climática… diversas condiciones climáticas" no define qué condiciones (rango de viento, temperatura, humedad). | Menor | Enumera los rangos de prueba. Así el objetivo se puede verificar. |
| Sección **Resumen** (primer párrafo) | Describe solo EcoWind. No menciona Bomberos 132 ni Islas, aunque el periodo cubre los tres proyectos. | Menor | Agrega una frase final que ubique el portafolio: *"Durante el periodo, el perfil articuló tres iniciativas: [proyecto 1, rol], [proyecto 2, rol] y [proyecto 3, rol]."* |

---

## 2. `tesis-cartografo-literatura`

**Criterio pedagógico:** una revisión de literatura no es una lista de ideas con fecha. Se valora por la **comparación** entre autores y por el **vacío** que justifica el proyecto. Sin autores identificables, no hay comparación posible.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **Revisión del Estado del Arte**, párrafo 1 (2020–2025) | Describe una evolución de la tecnología sin ninguna fuente ni criterio de búsqueda. | Mayor | Registra el protocolo: bases consultadas, palabras clave y años. Luego, para cada afirmación, una fuente. |
| *Avances tecnológicos recientes*, párrafo 1 | "Entre 2020 y 2025 se observan innovaciones en el diseño aerodinámico… uso de materiales compuestos…". Lista tendencias sin autores ni ejemplos. | Mayor | Convierte cada tendencia en un párrafo de síntesis: *"[Autor A, año] describe palas de material compuesto que mejoran la captura a viento bajo, mientras [Autor B, año] reporta…"*. |
| *Pequeños aerogeneradores en entornos rurales*, párrafo 1 | "Los estudios recientes… resaltan el rol…" sin ningún estudio nombrado. | Crítico | Nombra al menos dos estudios concretos y sus contextos (rural, urbano, insular). Sin eso, el vacío que justifica EcoWind no se sostiene. |
| *Estado del arte específico*, párrafo 1 | "Trabajos de revisión publicados en 2021–2022… Informes de I+D recientes identifican…". Se refiere a obras que el lector no puede localizar. | Crítico | Cita cada trabajo: autor, año, título, medio. Si no puedes identificarlo, no lo menciones. |
| *Oportunidades y brechas para EcoWind*, párrafo 1 | Cita entre comillas "grandes desafíos" sin fuente ni página. | Mayor | Cita con autor, año y página, o parafrasea sin comillas. |
| *Oportunidades y brechas*, párrafo 1 | "tu proyecto puede alinearse con el estado del arte…". El cambio de persona (segunda) es propio de una conversación, no de un informe. | Menor | Reescribe en tercera persona o primera del plural: *"EcoWind puede alinearse con el estado del arte al enfatizar…"*. |
| Todo el apartado | No hay matriz de literatura posible: ninguna fila tiene autor identificable. | [BRECHA] | Usa `references/matriz-literatura.md` del agente una vez tengas al menos 8 fuentes. Búsquedas sugeridas: *small wind turbine low wind speed*, *hybrid wind solar microgrid rural storage*, *distributed wind urban*. Revisa la norma **IEC 61400-2** (pequeños aerogeneradores), en su edición vigente. |

---

## 3. `tesis-auditor-metodologico`

**Criterio pedagógico:** las afirmaciones causales ("reduce", "mejora", "supera") necesitan un diseño que las sostenga: grupo de comparación, línea base y medición definida. Si el diseño falta, la frase debe bajar de fuerza.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **Bomberos 132**, *Resumen* | "validación empírica mediante ensayos controlados (RCTs)" con niños desde 8 años. No hay tamaño de muestra, aleatorización, grupo control, medición pre y post, ni plan de consentimiento. | Mayor (Crítico si se ejecuta sin esto) | Agrega una ficha de diseño: n por grupo, criterio de asignación, instrumento de medición y momentos de medición. Incluye consentimiento de apoderados y asentimiento de los menores, y solicita revisión a comité de ética antes de aplicar. |
| **Islas**, *Resumen* | "reducción promedio de hasta 3 °C" sin diseño: no dice cuántos sensores, dónde, durante cuánto tiempo, ni cómo se separa el efecto de la intervención de otras causas (clima, tráfico). | Mayor | Describe un diseño pre-post con zonas de control no intervenidas. Declara la limitación: sin control, la reducción es una asociación. |
| **ECOWIND**, *Resumen* | "Aerogenerador más eficiente que los modelos tradicionales" es una comparación sin banco de pruebas ni referencia. | Mayor | Define el modelo de comparación (un aerogenerador comercial, con su ficha técnica citada) y el protocolo de prueba (condiciones de viento, duración, instrumento). |
| **ECOWIND**, *Resumen* | "Adaptarse a distintas condiciones climáticas" sin condición probada. | Menor | Declara qué condiciones se probarán. Lo no probado va como trabajo futuro, no como capacidad. |

---

## 4. `tesis-auditor-estadistico`

**Criterio pedagógico:** un p-valor solo aparece cuando hay datos comparados. En este reporte no hay pruebas, así que el agente no tiene nada que recalcular.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| Todo el documento | El script `statcheck.py` reconoce **0 pruebas** en formato APA. | No aplica | Ninguna corrección ahora. |
| **Bomberos 132**, *Resumen* | El RCT planificado declarará diferencias entre grupos. | Previa | Antes de ejecutar, define el plan de análisis: prueba principal, α, tamaño del efecto esperado (d de Cohen) y tamaño de muestra que lo detecta. Así evitas buscar significancia después de ver los datos. |
| **Islas**, *Resumen* | La cifra "hasta 3 °C" necesitará comparación estadística cuando haya mediciones. | Previa | Reporta media, desviación y un intervalo de confianza del 95 %, no solo el mejor valor. |

---

## 5. `tesis-revisor-resultados-conclusiones`

**Criterio pedagógico:** la conclusión debe ser proporcional a la evidencia. "Consolidación", "alto potencial" o "posicionamiento" son juicios que requieren datos que este documento no muestra.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **Conclusiones**, párrafo 1 | "se observa una consolidación del perfil como docente investigador aplicado". Es un juicio sobre el autor basado en una lista de actividades. | Menor | Reemplaza el juicio por el registro: *"Durante el periodo se registran tres iniciativas, dos participaciones en eventos y cinco reuniones con una alianza."* Así el lector llega a la conclusión. |
| **Conclusiones**, párrafo 2 | "fortalece el posicionamiento del perfil en investigación aplicada de alto potencial de transferencia". No hay indicadores de transferencia (licencias, convenios firmados, usuarios). | Mayor | Limita la afirmación a lo que existe, o agrega el indicador. Ejemplo ficticio: *"Las alianzas en proceso con dos instituciones son la base para evaluar transferencia en el siguiente periodo."* |
| **Bomberos 132**, *Resumen* | "La propuesta sostiene que la inmersión… superan a los métodos didácticos tradicionales". Es una **hipótesis** presentada como si fuera un hecho. | Mayor | Marca el estatus: *"Se hipotetiza que la inmersión supera a los métodos tradicionales; la hipótesis se contrastará con un RCT."* |
| **Islas**, *Resumen* | Presenta "reducción de hasta 3 °C" como resultado esperado sin indicar que es una meta. | Mayor | Cambia a "meta": *"Se propone una meta de reducción de hasta 3 °C, sujeta a verificación."* |
| Documento completo | No hay sección de **resultados** ni de **limitaciones**. | Mayor | Agrega un apartado breve de limitaciones: alcance de las pruebas, dependencia de un solo evaluador, alianzas aún sin convenio firmado. |
| **Conclusiones**, párrafo 2 | "en línea con las prioridades institucionales en sostenibilidad…" sin referencia a las prioridades. | Menor | Cita el documento institucional de prioridades. |

---

## 6. `tesis-verificador-citas`

**Criterio pedagógico:** toda cifra, cita textual o idea ajena necesita su fuente. El documento no tiene ninguna fuente, así que el script no puede cruzar citas con referencias. Eso mismo es el hallazgo.

**Resultado del script:** 0 citas en texto, 0 referencias, advertencia "no se encontró lista de referencias". Un falso positivo: el título "Islas Climatológicas de Seguridad Térmica" entre comillas, que no es cita textual.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **Revisión del Estado del Arte**, párrafos 1, 2 y 4 | Afirmaciones con periodo (2020–2025, 2021–2022) sin cita. | Crítico | Agrega cita APA 7 en cada afirmación. Ejemplo de forma: *(Apellido, año)*. |
| **Islas**, *Resumen* | "pérdidas económicas estimadas en 2,5 millones de dólares anuales" sin fuente. | Mayor | Cita la estimación con su fuente y año. Si es un cálculo propio, dilo y muestra el método. |
| **Islas**, *Resumen* | "principales riesgos ambientales" sin fuente. | Menor | Cita un informe de riesgo ambiental o reformula como opinión. |
| **Bomberos 132**, *Resumen* | "segmento vulnerable ante la carencia de currículos motivadores" sin fuente. | Mayor | Cita el diagnóstico curricular o el estudio que lo sustenta. |
| **Oportunidades y brechas**, párrafo 1 | Cita entre comillas "grandes desafíos" sin autor ni página. | Mayor | Ver sección 2. |
| Documento completo | Falta la lista de referencias. | Crítico | Crea una sección *Referencias* en formato APA 7 con todas las fuentes citadas. |

---

## 7. `tesis-auditor-bibliografia`

**Resultado del script:** `error: No se encontró encabezado 'Referencias' o 'Bibliografía'`. El agente se detiene aquí por diseño: no audita de memoria.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| Final del documento (después de *Conclusiones*) | No hay bibliografía. | Crítico | Arma una lista de 10 a 15 fuentes para el estado del arte, en APA 7. Cada una debe tener DOI cuando exista. |
| Estado del arte | Ninguna fuente se puede verificar para existencia. | [BRECHA] | Cuando haya lista, el agente verifica DOIs con Crossref (en este entorno el proxy lo bloquea; hay que ejecutarlo en un equipo con red) y con Consensus, Elicit o PubMed. |
| Referencias a aplicar | Norma IEC 61400-2 y normativa chilena que aplique a EcoWind o a la intervención urbana. | [BRECHA] | Incluye la norma como referencia con su edición vigente, verificada en el sitio de la fuente oficial. |

---

## 8. `tesis-verificador-respaldo-fuente`

**Criterio pedagógico:** antes de citar una cifra, hay que poder mostrar la página donde aparece. Sin fuente, el veredicto es [BRECHA].

No hay fuentes para comparar. Estas son las afirmaciones que deben respaldarse primero, porque sostienen decisiones del proyecto:

| Ubicación | Afirmación | Veredicto actual | Qué pedir |
|---|---|---|---|
| **Islas**, *Resumen* | 2,5 millones de dólares anuales en pérdidas | [BRECHA] sin acceso | Informe de origen con página. |
| **Islas**, *Resumen* | Reducción de hasta 3 °C | [BRECHA] | Estudio de referencia en un contexto comparable (clima templado, comuna urbana). |
| **Bomberos 132**, *Resumen* | Inmersión supera métodos tradicionales | [BRECHA] | Estudio de serious games en gestión de riesgo, con diseño comparable. |
| **Revisión del Estado del Arte**, párrafo 4 | "Trabajos de revisión 2021–2022 identifican prioridades" | [BRECHA] | Identifica el trabajo; si no existe, retira la frase. |

---

## 9. `tesis-guardian-integridad`

**Criterio pedagógico:** la declaración de uso de IA es un dato del proceso, no un juicio sobre el autor. Lo que este agente puede observar es el texto mismo.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| Documento completo | No hay declaración de uso de herramientas de IA. El script no detecta ninguna mención. | [BRECHA] | Revisa la normativa vigente de Duoc UC sobre el tema (no la asumo). Si usaste IA para redactar o traducir, decláralo con herramienta, tarea y revisión realizada. |
| **Oportunidades y brechas**, párrafo 1 | "tu proyecto puede alinearse…" es redacción dirigida a un lector, no a un evaluador. | [INTERPRETACIÓN] | Reescribe en tono de informe. Es el mismo punto de la sección 2. |
| **Bomberos 132** y **Islas**, *Resumen* | Ambos resúmenes tienen una estructura parecida (contexto, propuesta, metodología o alcance, valor social). No comparé su texto con otros documentos. | [BRECHA] | Si el autor reutiliza estructuras o párrafos de proyectos anteriores, debe declararlo. Compara con proyectos previos antes de entregar. El agente no tiene acceso a esos documentos. |
| Reporte de similitud | No se entregó. | [BRECHA] | Ejecuta la herramienta institucional y entrega el reporte para interpretarlo con el agente. |

---

## 10. `tesis-simulador-defensa` (modo Tutor)

**Criterio pedagógico:** en una defensa, las preguntas más difíciles son las que se hacen a partir de las propias cifras y contradicciones del documento. Anticípalas.

Preguntas que probablemente formularía una comisión, cada una con el punto del documento que la origina:

1. **Islas:** "¿Cuál es el producto principal: el software o las intervenciones urbanas?" *(Tabla de detalle, objetivo y resumen).*
2. **Bomberos 132:** "¿Cómo sabrá que el juego mejora la decisión y no solo que los niños lo disfrutan?" *(Resumen, RCT).*
3. **Islas:** "¿De dónde sale la cifra de 2,5 millones de dólares y cómo se calculó?" *(Resumen).*
4. **Alianzas:** "Las fechas de las reuniones son posteriores a la fecha de este reporte. ¿Cuál es la fecha correcta?" *(Portada y tabla de alianzas).*
5. **Bomberos 132 con menores:** "Explique cómo obtendrá el consentimiento de los apoderados y el asentimiento de los niños." *(Resumen, RCT).*

Para preparar cada respuesta, el autor debe escribir su versión y compararla con el documento. No se entregan respuestas modelo.

---

## 11. `tesis-editor-forma`

**Criterio pedagógico:** los errores de forma no cambian el fondo, pero sí la credibilidad del documento. Son fáciles de corregir y conviene hacerlo antes de entregar.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| Sección *Postulaciones*, párrafo bajo el título | Instrucción de plantilla sin retirar: "Eliminar las que no correspondan". | Menor | Quita la instrucción y deja solo el contenido. |
| Sección *Postulaciones*, párrafo 1 | "Dependiendo de lo establecido en el plan de actividades, seleccionar y describir:". Instrucción de plantilla. | Menor | Quita la instrucción. |
| Encabezado *DETALLE CADA UNA DE LAS POSTULACIONES…* | Mayúsculas y redacción de instrucción. | Menor | Cambia a *Detalle de cada postulación*. |
| **Bomberos 132**, viñeta de postulación | "publico de niños de 8 años" (falta tilde) y una frase sin verbo principal: "…como investigador principal que es un desarrollo de juego online…". | Menor | Corrige a *público* y separa la frase: *"Bomberos 132 Emergencia, como investigador principal. Es un juego online…"*. |
| **Bomberos 132 y nombre del proyecto** | En la tabla se llama "Bomberos 132 Emergencia", en el resumen "EMERGENCIA 132 BOMBEROS". | Menor | Unifica el nombre oficial en todo el documento. |
| **ECOWIND**, celdas *Objetivo* y *Resumen* | Saltos de línea con barra "/" heredados de la copia desde otro archivo. | Menor | Pega el texto como texto plano y elimina las barras. |
| **ECOWIND**, celda *Resumen* | Repite el objetivo general y los específicos. Un resumen ejecutivo debe sintetizar, no copiar. | Menor | Reescribe en 4 o 5 líneas: qué es, para quién, qué se logrará y en qué etapa está. |
| **Divulgación**, instrucciones (3 párrafos) | Texto de plantilla que sigue en el documento. | Menor | Retíralo. |
| **Divulgación**, tabla, fila del Festival | "participo" (debe ser "participó"). Fecha "21 y 22 octubre" sin año. | Menor | Corrige a *participó* y agrega el año (2025). |
| **Divulgación**, tabla, fila del Workshop | "18//12/2025" (doble barra) y "Presentacion" (sin tilde). | Menor | Corrige a *18/12/2025* y *Presentación*. |
| **Divulgación**, encabezado de la columna *Estado* | La columna pide "postulando, aceptado, ya participó". "participo" no es una de esas opciones. | Menor | Usa "ya participó". |
| Siglas | **ENAER** (3 usos) y **MVP** (2 usos) sin definir la primera vez. | Menor | En la primera aparición: *Empresa Nacional de Aeronáutica de Chile (ENAER)* y *mínimo producto viable (MVP)*. |
| Tablas (3 detalles, divulgación, alianzas) | Sin número ni título, y sin fuente. | Menor | Numera y titula cada tabla. Agrega fuente cuando el dato venga de otro lugar. |
| Heading *Propiedad intelectual* | Sin contenido; solo la instrucción. | Mayor | Ver sección 12 (PI en la pauta). |
| **Conclusiones**, último párrafo | Caracteres invisibles (espacio de ancho cero) al final. | Menor | Borra los caracteres con "Mostrar marcas de formato" activado. |
| Anexos | El anexo EJERCITO no se menciona desde el cuerpo del texto. | Menor | En la sección de alianzas, escribe: *"Evidencia en Anexo EJERCITO."* |

---

## 12. `tesis-evaluador-aporte-viabilidad`

**Criterio pedagógico:** un aporte se defiende cuando se dice qué existía antes, qué es nuevo y para quién. Una recomendación se defiende cuando tiene costo, responsable, plazo y norma.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **ECOWIND**, todo el proyecto | No declara el aporte frente a aerogeneradores comerciales de baja potencia. | Mayor | Compara con dos o tres productos del mercado (fuente y ficha técnica citadas). Identifica qué mejora y para quién. |
| **Conclusiones**, párrafo 2 | Recomienda MVP, pilotos, propiedad intelectual y alianzas. No tiene costo, plazo ni responsable. | Mayor | Crea una ficha por recomendación con la plantilla del agente (actor, costo en CLP, plazo, norma, riesgo). |
| **Islas**, *Resumen* | "Modelo replicable a escala barrial" sin evaluar permisos municipales ni costos por cuadra. | Mayor | Describe el costo de una intervención piloto y la normativa municipal que la regula. [BRECHA]: no la verifiqué; hay que consultarla en la fuente oficial. |
| **Bomberos 132**, *Resumen* | "integración curricular formal" sin describir qué currículo ni quién decide. | Mayor | Identifica la vía: adopción en establecimientos, convenio o recurso complementario. Describe el actor que decide. |
| **Bomberos 132**, *Resumen* | Datos de menores en un juego online. | Mayor | Revisa la Ley 19.628 y la Ley 21.719 de datos personales (verificar vigencia en fuente oficial). [BRECHA] |
| Presupuesto | Ningún proyecto declara monto. El financiamiento es "Interno". | Mayor | Declara el monto de cada proyecto. Como referencia de microproyecto en este contexto, el orden es de unos $150.000 CLP. |
| **Filtro Yoko** (resumen) | Cobertura: parcial (faltan PI y plan de trabajo). Coherencia: parcial (Islas). Aplicabilidad: no evaluada. Accesibilidad: aceptable. | — | Completa las secciones faltantes antes de volver a evaluar. |

---

## 13. `tesis-bitacora-trazabilidad`

**Criterio pedagógico:** la trazabilidad es que cualquiera pueda reconstruir qué pasó, cuándo y con quién. Hoy hay buena evidencia de reuniones, pero las fechas no cuadran con el documento.

| Ubicación | Componente encontrado | Severidad | Propuesta de mejora |
|---|---|---|---|
| **Portada** (fecha) vs. **tabla de alianzas** | La portada dice "Santiago, 05 de enero de 2026". La tabla registra reuniones del 11/08, 21/08, 11/09, 16/09 y 25/09 **de 2026**, y del Ejército el 22/04/2026 y el 25/09/2026. Son fechas posteriores al documento. | Mayor | Revisa el año. Si las reuniones son de 2025, corrige la tabla. Si son de 2026, cambia la fecha de portada y el periodo. |
| **Tabla de alianzas**, fila ENAER | Registra cinco reuniones con fecha, pero la columna *Evidencia* solo dice "CORREO : / 11/08/2026". | Mayor | Por cada reunión, anota la evidencia concreta: correo, acta o invitación, con su ubicación en el anexo. |
| **Tabla de alianzas**, fila Ejército (teniente) | *Evidencia*: "MENSAJERIA: 25/09/2026". *Estado*: vacío. | Menor | Completa el estado y la evidencia. |
| **Tabla de alianzas**, columna *RUT* | Vacía en todas las filas. | Menor | Completa el RUT de la institución o indica que no aplica. |
| **Alianzas**, instrucción | La pauta pide vincular el plan con la **Dirección de Investigación Aplicada e Innovación, la Escuela y la Sede**. No aparece. | Mayor | Agrega una fila o párrafo con esas unidades internas y su rol. |
| Plan de trabajo | La pauta pide un plan con resultados esperados. No está en el documento. | Mayor | Agrega una tabla: actividad, responsable, fecha, resultado esperado y estado. |
| Respaldo de versiones | No hay forma de verificar versiones del documento. | Menor | Guarda cada versión con fecha en el nombre y registra qué cambió. |

---

## 14. `tesis-orquestador-revision` (consolidación)

**Método de puntaje:** se agrupan los hallazgos por **causa raíz** para no contar dos veces la misma falla. El contrato descuenta 15 (Crítico), 7 (Mayor) y 2 (Menor) por causa raíz.

| Causa raíz | Severidad | Descuento | Hallazgos que agrupa (sección) |
|---|---|---|---|
| R1. Sin fuentes: ni lista de referencias ni citas para tendencias, cifras ni cita textual | Crítico | 15 | 2, 6, 7, 8 |
| R2. Plantilla incompleta: PI vacía, plan de trabajo ausente, comprobantes faltantes, evidencia de alianzas incompleta, instrucciones sin retirar | Mayor | 7 | 11, 12, 13 |
| R3. Inconsistencias de datos: fechas posteriores al documento, financiamiento "financiado" vs. "en desarrollo", Islas con objetivo distinto del resumen | Mayor | 7 | 1, 13 |
| R4. Ética y datos personales: RCT con menores sin consentimiento descrito; anexos con capturas de terceros | Mayor | 7 | 3, 12 |
| R5. Sobreinterpretación y objetivos no medibles | Mayor | 7 | 1, 5 |
| R6. Forma y redacción: errores tipográficos, siglas, tablas sin título, lenguaje conversacional | Menor | 2 | 11 |

**Puntaje referencial:** 100 − (15 + 4×7 + 2) = **55/100**, nivel **Inicial** (menos de 70).

**Nota de calibración:** si se suman los hallazgos sin agrupar, el puntaje cae a 0 por saturación. Por eso el agrupamiento por causa raíz es el criterio correcto aquí. Conviene ajustar el contrato para documentos de avance: que el descuento máximo por causa raíz sea un tope.

**Señales de alerta (documento fuente, sección 3):**

| Señal | Estado | Detalle |
|---|---|---|
| 1. Desalineación pregunta-método-resultados-conclusiones | Observada | Islas tiene objetivo de software y resumen de infraestructura; objetivos de ECOWIND y Bomberos no son medibles. |
| 2. Referencias inexistentes o citas que no corresponden | **Crítica** | No hay lista de referencias ni fuentes para cifras y tendencias. |
| 3. Datos sin trazabilidad | Observada | Cifras sin fuente; fechas posteriores al documento; evidencia de alianzas incompleta. |
| 4. Conclusiones causales sin diseño | Observada | "Reducción de 3 °C" (Islas) y "supera a los métodos tradicionales" (Bomberos) sin diseño de comparación. |
| 5. Limitaciones omitidas | **Presente** | No hay sección de limitaciones. |

**Plan de corrección (prioridad por impacto en la validez):**

1. **Crear la lista de referencias** y citar cada cifra y tendencia. Responsable: autor. Plazo: antes de cualquier nueva entrega.
2. **Revisar fechas y financiamiento**: corregir el año de las reuniones y la fecha de portada; decidir si ECOWIND está financiado o en desarrollo; declarar el monto de cada proyecto.
3. **Completar la pauta** con PI, plan de trabajo, limitaciones y evidencia de alianzas. Retirar anexos con datos de terceros o solicitar su consentimiento, y definir el protocolo ético antes de cualquier RCT con menores.

**Verificaciones no realizadas [BRECHA]:**

- Lista de referencias: no existe, no se puede verificar DOIs.
- Crossref: bloqueado en este entorno.
- Resolución Rectoría Nº13/2023 (afiliación institucional): no tengo el texto para verificar la declaración de afiliación de la sección *Divulgación*.
- Ley 21.719 y Ley 19.628: verificar vigencia y alcance en fuente oficial.
- Anexos (págs. 11–12): los revisé a baja resolución. Antes de publicar, confirma si aparecen teléfonos o correos personales de terceros.
- Reporte de similitud institucional: no entregado.
