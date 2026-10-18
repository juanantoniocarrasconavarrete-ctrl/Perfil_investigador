from comun import *
D = Doc('Manual de propuestas de mejora', 'Qué hacer, quién, cuándo, con qué recursos y cómo saber si funcionó', 'PRODUCTO G · MANUAL ORIENTADO A LA ACCIÓN', G + 'portada_puerta.png', 'Proyecto La Puerta · Manual de propuestas de mejora')
g = R['global']; O = OF; fo = {r['var']: r for r in O['filas']}; S = O['semaforo_estudiantes']

intro(D, 'Las acciones de mejora derivadas de los resultados de la encuesta del Proyecto La Puerta: qué hacer, quién, cuándo, con qué recursos y cómo medir el éxito.',
 'Los Informes A, B y C identificaron brechas (red de contactos, contacto con el trabajo real, estudiantes en semáforo rojo) y un vacío de medición. Este manual convierte esos hallazgos en acciones concretas para equipos con tiempo comprimido y presupuestos acotados.',
 'Proponer un plan de acción priorizado, con indicadores de seguimiento, cronograma y estrategias de implementación.',
 ['Definir áreas prioritarias de mejora y su evidencia.', 'Detallar acciones concretas con responsables, plazos y nivel de costo.', 'Establecer indicadores, metas y cadencia de seguimiento.', 'Proponer cronograma, gobernanza, riesgos y criterios para escalar.'],
 'El documento se organiza en cinco partes: la Introducción (cómo usar el manual y principios de diseño); el Desarrollo (áreas prioritarias, fichas de acción por área, indicadores, cronograma y estrategias); la Conclusión; las Referencias; y los Anexos (plantilla de microproyecto, protocolo de evaluación y declaración de uso de IA).')
D.h1('Cómo usar este manual')
D.p('Este manual traduce los hallazgos de los Informes A, B y C en **acciones concretas**. Cada una indica qué es, quién podría liderarla, en qué plazo, con qué nivel de costo y **cómo se medirá su éxito**. Está pensado para equipos con **tiempo comprimido y presupuestos acotados**: privilegia actividades que se integran a asignaturas existentes y microproyectos de bajo costo.')
D.table(['Nivel de costo', 'Qué significa', 'Ejemplos'], [
 ['**Bajo (≈ 0)**', 'Usa horas ya contratadas; sin gasto adicional.', 'Rediseño de la encuesta, doble codificación, tutorías dentro de asignaturas.'],
 ['**Microproyecto (≤ $150.000 CLP)**', 'Gasto menor por actividad (colación, materiales, difusión).', '«Café con profesionales», entrevista informativa, taller breve.'],
 ['**Medio ($150.000–$600.000)**', 'Requiere coordinación y algo de financiamiento.', 'Visita con transporte, mini-proyecto con empresa, jornada de ferias.'],
 ['**Mayor (> $600.000)**', 'Requiere gestión institucional.', 'Licencias de software, cursos de idiomas adicionales.']], [4.0, 6.0, 6.6], size=9)
D.callout('Sobre las cifras de costo', 'Los niveles de costo son **estimaciones gruesas del equipo analista**, no cotizaciones. Deben validarse con la Dirección de Escuela y Administración de la sede antes de comprometer recursos. Los plazos asumen el calendario académico semestral.', AMB, 'FFF7E0')
D.h3('Cuatro principios de diseño')
D.numbered(['**Empezar pequeño y medir:** cada acción nace como piloto con indicador y línea base.', '**Integrar, no sumar:** vincular cada actividad a una asignatura y resultado de aprendizaje existente, para no sobrecargar a docentes ni estudiantes.', '**Aprender haciendo (Kolb, 1984):** experiencia → reflexión → aplicación; toda actividad con empresas termina con una bitácora de aprendizaje.', '**Focalizar por necesidad, no por rótulo:** usar el semáforo y las brechas específicas, no el hecho de tener o no práctica previa.'])

D.part('DESARROLLO')
D.h1('2. Áreas prioritarias de mejora')
D.p('Los hallazgos se agrupan en **seis áreas**. Las ocho recomendaciones (R1 a R8) de los Informes A, B y C se reparten entre ellas.')
D.table(['Área', 'Recomendaciones', 'Brecha que atiende (línea base)', 'Prioridad'], [
 ['**A1 · Medición y evaluación**', 'R1 · R8', 'Código, momento, grupo, A03/A04 y POST_EXP1 vacíos o no aplicados; respuestas abiertas sin validar.', 'Hacer ya'],
 ['**A2 · Redes profesionales**', 'R2', f"P12 = {pc(IT['P12']['fav'])} de acuerdo; P11 = {pc(IT['P11']['fav'])}.", 'Estratégica'],
 ['**A3 · Contacto con el trabajo real**', 'R3', f"P01 = {pc(IT['P01']['fav'])}; P02 = {pc(IT['P02']['fav'])}; P09 = {pc(IT['P09']['fav'])}; P10 = {pc(IT['P10']['fav'])}.", 'Estratégica'],
 ['**A4 · Acompañamiento focalizado**', 'R4 · R7', f"{S['total']['Rojo']} estudiantes en rojo ({pc(S['pct_total']['Rojo'])}); tramo 3.º–4.º semestre más bajo.", 'Hacer ya'],
 ['**A5 · Competencias de empleabilidad**', 'R5 · R6', f"P04 = {pc(IT['P04']['fav'])}; P06 = {pc(IT['P06']['fav'])}; 20 menciones de inglés, 19 de herramientas.", 'Ajuste / evaluar'],
 ['**A6 · Gobernanza y mejora continua**', 'Transversal', 'Sin responsables ni ciclo de revisión definidos.', 'Hacer ya']], [4.6, 3.0, 6.6, 2.4], size=9, colors={(0, 3): TEAL, (1, 3): NAVY, (2, 3): NAVY, (3, 3): TEAL, (4, 3): AMB, (5, 3): TEAL})
D.fig('g23_prioridad', 'Figura 1. Matriz de priorización de las recomendaciones.', 13.5)

def area(codigo, titulo, evidencia, objetivo, acciones, beneficios, indicadores, riesgos, estrategia):
    D.h1(f'{codigo} · {titulo}')
    D.callout('Por qué esta área', evidencia, CORAL, 'FDEEE9')
    D.p(f'**Objetivo.** {objetivo}')
    D.h3('Acciones concretas')
    D.table(['#', 'Acción', 'Qué es, concretamente', 'Responsable sugerido', 'Plazo', 'Costo'], acciones, [0.9, 3.0, 5.8, 2.7, 1.7, 2.5], size=8.2, align=['c', 'l', 'l', 'l', 'l', 'l'])
    D.h3('Beneficios esperados')
    D.bullets(beneficios)
    D.h3('Indicadores de seguimiento')
    D.table(['Indicador', 'Línea base', 'Meta (2 semestres)', 'Cómo se mide'], indicadores, [6.0, 2.4, 3.2, 5.0], size=8.6, align=['l', 'c', 'c', 'l'])
    D.h3('Riesgos y cómo mitigarlos')
    D.table(['Riesgo', 'Mitigación'], riesgos, [6.8, 9.8], size=8.8)
    D.callout('Estrategia de implementación', estrategia, TEAL)

area('A1', 'Medición y evaluación', 'Sin código único, momento y grupo no se puede evaluar el efecto de La Puerta; tampoco se aplicaron las preguntas A03 y A04 del Informe Metodológico ni POST_EXP1. Es la corrección más barata y la de mayor valor.',
 'Poder responder, en la próxima aplicación, si La Puerta cambia la preparación percibida y el desempeño en práctica.',
 [['1.1', 'Campos obligatorios', 'En el formulario: código de estudiante (con validación de formato), momento (pretest/postest) y grupo (La Puerta/comparación) como preguntas **requeridas**; no mostrar el formulario sin estos datos.', 'Coordinación de investigación', 'Nov–Dic 26', 'Bajo'],
  ['1.2', 'Completar el instrumento', 'Agregar A03 y A04 y hacer visible POST_EXP1 en el postest. Separar P15 (interés) de la dimensión de redes y renombrar D4 como «Redes».', 'Equipo de investigación', 'Dic 26', 'Bajo'],
  ['1.3', 'Piloto con grupo de comparación', 'Aplicar La Puerta a secciones seleccionadas y usar secciones equivalentes (misma sede, semestre y carrera) como comparación; pretest en las primeras semanas y postest al cierre del semestre.', 'Dirección de Escuela + jefaturas', 'Mar–Jul 27', 'Bajo'],
  ['1.4', 'Evaluación de tutor', 'Incorporar la rúbrica Likert de 5 puntos del informe metodológico para que el tutor de empresa evalúe el desempeño observado.', 'Coordinación de práctica', 'Jun–Jul 27', 'Bajo'],
  ['1.5', 'Validar respuestas abiertas', 'Doble codificación humana con libro de códigos; acuerdo entre codificadores (kappa ≥ 0,70).', 'Dos docentes', 'Nov 26', 'Bajo'],
  ['1.6', 'Registrar el plan de análisis', 'Dejar escritas, antes de aplicar, las hipótesis y reglas de decisión (como en el Informe B).', 'Equipo de investigación', 'Feb 27', 'Bajo']],
 ['Se podrá atribuir (o no) cambios al programa con grupo de comparación.', 'Se detectarán diferencias reales de 0,2–0,3 puntos si el tamaño de muestra es adecuado (≈ 110 por grupo; ver Anexo B).', 'Se comparará lo que los estudiantes creen de sí mismos con lo que observa el tutor.', 'Se tomarán decisiones de escalamiento con evidencia.'],
 [['% de registros con código, momento y grupo', '0 %', '100 %', 'Revisión de la base tras cada aplicación'], ['Emparejamiento pretest–postest', 'No medible', '≥ 70 % de los participantes', 'Códigos presentes en ambas mediciones'], ['Acuerdo de codificación (kappa)', 'No medido', '≥ 0,70', 'Doble codificación de una muestra'], ['Cobertura de evaluación de tutor', '0 %', '≥ 60 % de practicantes', 'Rúbricas recibidas']],
 [['Baja tasa de respuesta en el postest', 'Aplicarlo en clase (15 minutos); recordatorios; vincular a una actividad de cierre.'], ['Contaminación del grupo de comparación', 'Asignar por sección completa; evitar mezclar actividades entre secciones.'], ['Privacidad (códigos, correos)', 'Usar códigos seudonimizados, separar la tabla de equivalencias y guardarla con acceso restringido; cumplir la normativa chilena de protección de datos personales.']],
 'Comenzar en noviembre con los cambios del formulario (costo cero). Probar con 10 estudiantes antes de la aplicación masiva. El analista de datos reutiliza los scripts del repositorio para generar el informe en el mismo día del cierre.')

area('A2', 'Redes profesionales', f"Solo {pc(IT['P12']['fav'])} dice tener una red de contactos laborales y {pc(IT['P11']['fav'])} sabe cómo contactar a profesionales. La brecha es transversal (con y sin práctica previa, todos los años) y los estudiantes quieren vincularse (P15 = {pc(IT['P15']['fav'])}). Los vínculos con personas fuera del círculo cercano son un recurso clave de información y empleo (Granovetter, 1973).",
 'Que cada estudiante llegue a su práctica con al menos tres contactos profesionales de su área y la confianza para contactar a más.',
 [['2.1', 'Café con profesionales', 'Encuentro mensual de 45 minutos con egresados, practicantes o profesionales de empresas socias; formato de conversación guiada y espacio para preguntas.', 'Coordinación de carrera + Vinculación con el Medio', 'Mar–Jul 27', 'Microproyecto'],
  ['2.2', 'Mentoría entre pares', 'Estudiantes de 5.º semestre o más (con práctica) acompañan a estudiantes de 1.º–2.º; 3 encuentros por semestre (peer-mentoring).', 'Docentes tutores', 'Mar–Jul 27', 'Bajo'],
  ['2.3', 'Entrevista informativa', 'Tarea evaluada en una asignatura: cada estudiante entrevista a un profesional de su rubro con una pauta (qué hace, qué exige, cómo llegó) y entrega un breve informe.', 'Docente de asignatura', 'Abr–Jun 27', 'Bajo'],
  ['2.4', 'Taller «Cómo contactar a un profesional»', '2 horas: guion de presentación, mensaje por correo y LinkedIn, qué preguntar y cómo agradecer; práctica con role-playing.', 'Docente de comunicación', 'Abr 27', 'Bajo'],
  ['2.5', 'Directorio de contactos', 'Base interna de egresados y empresas socias dispuestos a conversar, con consentimiento informado y actualización semestral.', 'Vinculación con el Medio', 'Dic 26–Mar 27', 'Bajo'],
  ['2.6', 'Charlas o feria por rubro', 'Una jornada por semestre con 4–6 empresas (logística, comercio exterior, finanzas, RR. HH.).', 'Dirección de Escuela', 'Jun 27', 'Medio']],
 ['Más contactos y mayor confianza para pedir información o una práctica.', 'Acceso a información realista sobre tareas y exigencias (también mejora P01 y P02).', 'Fortalecimiento de la relación con empresas socias y egresados.'],
 [['P12 · Tengo una red de contactos referentes', pc(IT['P12']['fav']), '≥ 60 % de acuerdo', 'Encuesta pre/post'], ['P11 · Sé cómo contactar a profesionales', pc(IT['P11']['fav']), '≥ 72 % de acuerdo', 'Encuesta pre/post'], ['Contactos profesionales registrados por estudiante', 'No medido', '≥ 3', 'Bitácora / entrevista informativa'], ['Estudiantes que participan en ≥ 1 actividad de redes', 'No medido', '≥ 70 %', 'Listas de asistencia']],
 [['Baja disponibilidad de profesionales', 'Formatos cortos (45 min), virtuales cuando se requiera; rotar entre egresados.'], ['Que las redes dependan de pocas personas', 'Diversificar rubros y empresas; no más de 2 encuentros con la misma persona por semestre.'], ['Uso indebido de datos de contacto', 'Consentimiento explícito y uso exclusivo para fines formativos.']],
 'Partir con una sola carrera como piloto y un solo rubro. El «café» es un microproyecto: colación y difusión no deberían superar los $150.000 por sesión. La entrevista informativa no tiene costo y puede evaluarse con la rúbrica existente de la asignatura.')

area('A3', 'Contacto con el trabajo real', f"Conocer tareas y exigencias (P01 = {pc(IT['P01']['fav'])}; P02 = {pc(IT['P02']['fav'])}) y haber contrastado el trabajo con los intereses (P09 = {pc(IT['P09']['fav'])}) están bajo la meta, y se asocian con sentirse seguro de adaptarse (R² ≈ 49 %). En sus palabras, lo más pedido son simulaciones, casos reales y salidas a terreno. Entre quienes no han hecho práctica, 13 de 15 que dicen «no tener aprendizaje laboral» son estudiantes sin práctica previa.",
 'Que todo estudiante tenga, antes de su práctica, al menos una vivencia concreta del trabajo real y una reflexión escrita sobre ella.',
 [['3.1', 'Visitas guiadas con pauta', 'Dos visitas por semestre a centros de distribución, puertos u oficinas; con guía de observación (tareas, herramientas, roles) y breve puesta en común.', 'Jefaturas de carrera', 'Abr–Jun 27', 'Medio'],
  ['3.2', 'Simulación de la práctica', 'Role-play de entrevista, primer día y conversación con jefatura, con retroalimentación de docentes o empresas socias; incluye casos de dudas y errores.', 'Docentes de comunicación y práctica', 'Abr–Jun 27', 'Bajo'],
  ['3.3', 'Mini-proyecto con empresa', 'Desafío real acotado (2–4 semanas) planteado por una empresa socia, resuelto por equipos y presentado a la empresa.', 'Docentes + empresa socia', 'May–Jul 27', 'Medio'],
  ['3.4', 'Jornada de observación (shadowing)', 'Una jornada acompañando a un profesional; registro de tareas, decisiones y preguntas.', 'Coordinación de práctica', 'Jun–Jul 27', 'Bajo'],
  ['3.5', 'Bitácora de aprendizaje', 'Registro de una página tras cada actividad: qué vi, qué me sorprendió, qué quiero preguntar, qué cambiaría; reflexión al estilo del ciclo de Kolb (1984).', 'Todos los docentes', 'Todo el semestre', 'Bajo'],
  ['3.6', 'Casos reales de docentes con experiencia', 'Incorporar en clase situaciones vividas por docentes y egresados (por ejemplo, el uso de descriptores de cargo en reclutamiento).', 'Docentes', 'Todo el semestre', 'Bajo']],
 ['Expectativas más realistas, menor shock de transición.', 'Mayor seguridad de adaptarse a un puesto (P10).', 'Estudiantes sin práctica previa con experiencias concretas que contar.', 'Mejor retroalimentación para ajustar contenidos de asignaturas.'],
 [['P01 · Conozco tareas y condiciones reales', pc(IT['P01']['fav']), '≥ 75 %', 'Encuesta pre/post'], ['P02 · Tengo claras las exigencias', pc(IT['P02']['fav']), '≥ 75 %', 'Encuesta pre/post'], ['P09 · He comprobado si el trabajo calza conmigo', pc(IT['P09']['fav']), '≥ 70 %', 'Encuesta pre/post'], ['P10 · Me siento seguro/a de adaptarme', pc(IT['P10']['fav']), '≥ 75 %', 'Encuesta pre/post'], ['Estudiantes con ≥ 1 vivencia real antes de la práctica', 'No medido', '100 %', 'Bitácoras entregadas']],
 [['Visitas difíciles de coordinar', 'Priorizar empresas ya vinculadas; alternar con visitas virtuales; planificar con un semestre de anticipación.'], ['Sobrecarga de docentes', 'Insertar en asignaturas existentes y reutilizar la bitácora como evaluación formativa.'], ['Experiencias superficiales', 'Exigir pauta de observación y reflexión; evaluar con rúbrica.']],
 'Elegir 2 asignaturas ancla por carrera donde ya existan casos y proyectos. Probar la bitácora en una sección antes de generalizarla. Priorizar la **calidad de la reflexión**: los datos sugieren que lo que importa no es solo «haber estado», sino **lo que se aprendió**.')

area('A4', 'Acompañamiento focalizado', f"{S['total']['Rojo']} estudiantes ({pc(S['pct_total']['Rojo'])}) están en rojo (menos de 3,50); {S['sin']['Rojo']} no tienen práctica previa y {S['con']['Rojo']} sí. La práctica previa no «vacuna»: 1 de cada 7 estudiantes con práctica también está en rojo. El tramo 3.º–4.º semestre es el más bajo (a confirmar).",
 'Que ningún estudiante en rojo llegue a la práctica sin un plan de acompañamiento.',
 [['4.1', 'Tamizaje con semáforo', 'Aplicar la encuesta antes de la práctica y clasificar: verde (≥ 4,20), amarillo (3,50–4,19), rojo (< 3,50).', 'Coordinación de práctica', 'Feb–Mar 27', 'Bajo'],
  ['4.2', 'Plan individual para rojos', 'Conversación de 30 minutos, identificación de 2–3 brechas (por ejemplo, P01, P09, P12) y plan de 5 sesiones de tutoría.', 'Docente tutor', 'Mar–Jul 27', 'Bajo'],
  ['4.3', 'Seguimiento quincenal', 'Para amarillos y rojos, contacto cada 15 días durante las primeras semanas de práctica (criterio del informe metodológico).', 'Docente tutor', 'En práctica', 'Bajo'],
  ['4.4', 'Talleres de nivelación', 'Para rojos: talleres cortos antes o durante las dos primeras semanas (comunicación, manejo del error, pedir ayuda).', 'Docentes de comunicación', 'Previo a práctica', 'Microproyecto'],
  ['4.5', 'Reconexión 3.º–4.º semestre', 'Una actividad de contacto laboral en cada semestre de este tramo (visita, charla o proyecto breve).', 'Jefaturas de carrera', 'Ago–Dic 27', 'Medio'],
  ['4.6', 'Revisión del criterio', 'No segregar por práctica previa; reevaluar el criterio cuando haya datos pre/post.', 'Comité del proyecto', 'Dic 27', 'Bajo']],
 ['Detección temprana y apoyo antes de que aparezcan problemas en la empresa.', 'Menor riesgo de mala experiencia o abandono de práctica.', 'Mejor uso de horas de tutoría (se focalizan donde se necesitan).'],
 [['% de estudiantes en rojo', pc(S['pct_total']['Rojo']), '≤ 12 %', 'Semáforo en pretest y postest'], ['% de rojos con plan de acompañamiento', 'No medido', '100 %', 'Registro de tutorías'], ['Promedio global', n(g['media']), '≥ 4,05', 'Encuesta pre/post'], ['Diferencia 3.º–4.º vs. resto', n(H2['GLOBAL']['medias'][1] - 0.5 * (H2['GLOBAL']['medias'][0] + H2['GLOBAL']['medias'][2])), '≈ 0', 'Encuesta pre/post']],
 [['Estigmatizar a quienes están en rojo', 'Presentar el semáforo como «señal de apoyo», comunicarlo en privado, no publicar listas.'], ['Falta de horas docentes', 'Priorizar a rojos; agrupar tutorías en sesiones pequeñas de 3–4 estudiantes.'], ['Que el semáforo refleje solo modestia', 'Complementar con evaluación de tutor y conversación individual.']],
 'Comenzar con los 38 estudiantes que hoy están en rojo (si siguen en el programa) y evaluar el efecto en el postest. Priorizar un formato grupal de tutoría para no multiplicar horas.')

area('A5', 'Competencias de empleabilidad', f"Explicar con claridad (P04 = {pc(IT['P04']['fav'])}) y elegir el método adecuado para la empresa (P06 = {pc(IT['P06']['fav'])}) están bajo la meta. En los comentarios, comunicación y oratoria (22), inglés (20), preparación para entrevistas y CV (19), herramientas como ERP y Excel (19), y legislación laboral (6) son los apoyos más pedidos.",
 'Que los estudiantes comuniquen con claridad, se presenten profesionalmente y usen las herramientas que encontrarán en la empresa.',
 [['5.1', 'Taller de comunicación estructurada', '8 horas: explicar lo técnico a personas no técnicas, marco SCQA (Situación, Complejidad, Pregunta, Respuesta), presentaciones breves y retroalimentación entre pares.', 'Docentes de comunicación', 'Abr–Jun 27', 'Bajo'],
  ['5.2', 'Taller entrevista, CV y LinkedIn', '4 horas con simulaciones de entrevista por competencias y revisión de CV.', 'Docentes + empresas', 'Mar–Abr 27', 'Microproyecto'],
  ['5.3', 'Módulo de legislación laboral básica', '2–4 horas: contratos, remuneraciones, derechos y deberes en práctica.', 'Docente de RR. HH.', 'Abr 27', 'Bajo'],
  ['5.4', 'Inglés técnico', 'Revisar la oferta de talleres de inglés (incluido horario vespertino); explorar un módulo de inglés para comercio exterior y logística.', 'Dirección de Escuela', 'Ago–Dic 27', 'Mayor'],
  ['5.5', 'Herramientas reales', 'Talleres de Excel avanzado y Power BI; evaluar licencias o programas educativos para ERP (SAP, Softland) y su uso en laboratorio.', 'Jefaturas + TI', 'Ago–Dic 27', 'Mayor'],
  ['5.6', 'Inclusión laboral', 'Sensibilización y lengua de señas básica (opcional; 4 menciones).', 'Vinculación con el Medio', 'Ago–Dic 27', 'Microproyecto']],
 ['Mejor integración al equipo y comprensión de lo que se dice y se pide.', 'Menor desfase entre aula y empresa.', 'Mayor confianza para entrevistas y primeras semanas de trabajo.'],
 [['P04 · Explico temas técnicos con claridad', pc(IT['P04']['fav']), '≥ 75 %', 'Encuesta pre/post'], ['P06 · Sé qué método sirve en la empresa', pc(IT['P06']['fav']), '≥ 72 %', 'Encuesta pre/post'], ['Menciones de «inglés» y «herramientas» como apoyo pedido', '20 y 19', '< 10 cada una', 'Siguiente levantamiento abierto'], ['Asistencia a talleres', 'No medido', '≥ 70 % del curso objetivo', 'Listas de asistencia']],
 [['Costo de licencias e inglés', 'Explorar convenios y programas educativos existentes antes de comprar; priorizar herramientas gratuitas o de uso libre.'], ['Talleres poco aplicados', 'Evaluación con casos reales y práctica; invitar a empresas.'], ['Superposición con asignaturas', 'Mapear los resultados de aprendizaje y evitar duplicar contenidos.']],
 'Comenzar por lo de costo bajo (5.1–5.3) en el primer semestre y dejar 5.4–5.5 para el segundo, una vez revisados convenios, licencias y oferta ya disponible.')

area('A6', 'Gobernanza y mejora continua', 'Sin responsables claros ni ciclo de revisión, las acciones se diluyen. Además, el Informe Metodológico propone institucionalizar el modelo solo si la hipótesis se confirma; los datos actuales sugieren **perfeccionar y evaluar** antes de escalar.',
 'Contar con un comité pequeño, un tablero de indicadores y un ciclo semestral de decisiones basadas en evidencia.',
 [['6.1', 'Comité La Puerta', 'Comité de 5–6 personas: Dirección de Escuela, jefaturas, coordinación de práctica, Vinculación con el Medio, analista de datos y un estudiante representante; reunión mensual de 45 minutos.', 'Dirección de Escuela', 'Nov 26', 'Bajo'],
  ['6.2', 'Tablero de indicadores', 'Planilla/tablero con los indicadores de este manual, actualizado cada semestre con los scripts del repositorio.', 'Analista de datos', 'Dic 26', 'Bajo'],
  ['6.3', 'Ciclo semestral', 'Planificar → hacer → medir → ajustar (PDCA): revisión al inicio, a mitad y al cierre del semestre.', 'Comité', 'Cada semestre', 'Bajo'],
  ['6.4', 'Criterios de escalamiento', 'Definir qué debe ocurrir para escalar (ver Sección 6.2).', 'Comité', 'Mar 27', 'Bajo'],
  ['6.5', 'Comunicación', 'Devolver resultados a estudiantes, docentes y empresas con el Manual de resultados y la infografía.', 'Comité', 'Dic 26', 'Bajo']],
 ['Decisiones oportunas, con responsables claros.', 'Transparencia con estudiantes y empresas.', 'Aprendizaje acumulado de cada cohorte.'],
 [['Reuniones del comité realizadas', '0', '≥ 80 % de las programadas', 'Actas'], ['Indicadores actualizados a tiempo', '0', '100 %', 'Tablero'], ['Devolución de resultados a estudiantes', 'No realizada', '1 por semestre', 'Registro de comunicación']],
 [['Rotación de responsables', 'Documentar el proceso; mantener el repositorio de código y datos; designar suplentes.'], ['Sobrecarga de reuniones', 'Reuniones breves con agenda fija; trabajo asincrónico entre sesiones.']],
 'Reutilizar los scripts del repositorio: un solo comando regenera cifras y gráficos con una base nueva. El tablero puede iniciarse en una planilla y, más adelante, conectarse a Power BI.')

D.h1('Indicadores de seguimiento (tablero maestro)')
D.p('El siguiente tablero reúne los indicadores clave, con su línea base (esta encuesta), una meta referencial a dos semestres y el tipo de seguimiento. Las metas son **propuestas del equipo analista** y deben validarse con la Dirección de Escuela.')
rows = []
metas = [('P12 · Red de contactos', IT['P12']['fav'], 60, 'Resultado'), ('P11 · Sé cómo contactar a profesionales', IT['P11']['fav'], 72, 'Resultado'), ('P01 · Conozco tareas reales', IT['P01']['fav'], 75, 'Resultado'), ('P02 · Claridad de exigencias', IT['P02']['fav'], 75, 'Resultado'), ('P09 · Comprobé que el trabajo calza', IT['P09']['fav'], 70, 'Resultado'), ('P10 · Seguridad de adaptarme', IT['P10']['fav'], 75, 'Resultado'), ('P04 · Explico lo técnico con claridad', IT['P04']['fav'], 75, 'Resultado'), ('P06 · Método adecuado para la empresa', IT['P06']['fav'], 72, 'Resultado')]
for nm, b, m, tp in metas: rows.append([nm, pc(b), pc(m), 'Encuesta pre/post', tp])
rows += [['Promedio global', n(g['media']), '≥ 4,05', 'Encuesta pre/post', 'Resultado'], ['% de estudiantes en rojo', pc(S['pct_total']['Rojo']), '≤ 12 %', 'Semáforo', 'Resultado'], ['Registros con código, momento y grupo', '0 %', '100 %', 'Base de datos', 'Proceso'], ['Estudiantes con ≥ 1 vivencia real', 'No medido', '100 %', 'Bitácoras', 'Proceso'], ['Contactos profesionales por estudiante', 'No medido', '≥ 3', 'Bitácora', 'Proceso'], ['Evaluación del tutor de empresa (1–5)', 'No medido', '≥ 4,0', 'Rúbrica tutor', 'Impacto']]
D.table(['Indicador', 'Línea base', 'Meta', 'Fuente', 'Tipo'], rows, [6.4, 2.2, 2.2, 3.4, 2.4], size=8.8, align=['l', 'c', 'c', 'l', 'c'])
D.h3('Cadencia de seguimiento')
D.table(['Frecuencia', 'Qué se revisa', 'Quién'], [['**Mensual**', 'Indicadores de proceso: asistencia, cobertura, actividades realizadas.', 'Comité'], ['**Semestral**', 'Indicadores de resultado: encuesta pre/post, semáforo, comparación con grupo control.', 'Comité + analista'], ['**Anual**', 'Impacto: evaluación del tutor, continuidad en práctica, empleabilidad a 6 meses, costo por estudiante.', 'Dirección de Escuela']], [3.0, 9.4, 4.2], size=9)

D.h1('Cronograma referencial')
D.fig('g24_cronograma', 'Figura 2. Cronograma de 14 meses (noviembre 2026 – diciembre 2027).', 16.4)
D.table(['Hito', 'Cuándo', 'Producto'], [['Rediseño del instrumento y de la base', 'Nov–Dic 2026', 'Formulario con campos obligatorios, A03/A04 y POST_EXP1'], ['Constitución del comité y tablero', 'Nov–Dic 2026', 'Acta de constitución; tablero inicial'], ['Pretest', 'Marzo 2027', 'Línea base pareada por código, con grupo de comparación'], ['Ejecución de actividades de redes, contacto real y comunicación', 'Mar–Jul 2027', 'Actividades con registro de asistencia y bitácoras'], ['Postest y comparación', 'Julio 2027', 'Informe de cambios pre/post vs. grupo de comparación'], ['Expansión selectiva (inglés, herramientas, 3.º–4.º semestre)', 'Ago–Dic 2027', 'Pilotos con indicadores'], ['Informe de evaluación y decisión de escalamiento', 'Dic 2027', 'Decisión del comité con criterios previos']], [6.4, 3.2, 7.0], size=9)

D.h1('Estrategias de implementación')
D.h2('6.1 Gobernanza y roles')
D.table(['Rol', 'Responsabilidad'], [['**Dirección de Escuela**', 'Patrocinio, asignación de horas y recursos, decisión de escalamiento.'], ['**Jefaturas de carrera**', 'Integrar actividades en asignaturas; coordinar visitas y mini-proyectos.'], ['**Coordinación de práctica**', 'Tamizaje, seguimiento de estudiantes en rojo, evaluación de tutor.'], ['**Vinculación con el Medio**', 'Relación con empresas socias, egresados y directorio de contactos.'], ['**Analista de datos**', 'Medición, tablero y reportes (scripts del repositorio).'], ['**Representante estudiantil**', 'Retroalimentación de las actividades; vocería hacia sus compañeros.']], [4.6, 12.0], size=9)
D.h2('6.2 Criterios para escalar (decisión de continuar, ajustar o detener)')
D.table(['Criterio', 'Umbral sugerido', 'Decisión'], [
 ['Efecto en el índice global (diferencia en diferencias, pre/post vs. control)', '≥ +0,20 puntos con intervalo de confianza que no incluya 0', 'Escalar'],
 ['Red de contactos (P12)', '≥ 60 % de acuerdo en el grupo La Puerta', 'Escalar la línea de redes'],
 ['Satisfacción con las actividades', '≥ 4,0 de 5', 'Mantener / ajustar'],
 ['Cobertura de medición pareada', '≥ 70 %', 'Resultados interpretables'],
 ['Costo por estudiante', 'Dentro del presupuesto fijado por la Escuela', 'Escalar solo si es sostenible'],
 ['Efecto nulo o negativo en dos mediciones', 'Sin cambio o deterioro', 'Rediseñar o detener']], [7.2, 6.0, 3.4], size=9)
D.h2('6.3 Gestión de riesgos transversales')
D.table(['Riesgo', 'Probabilidad', 'Impacto', 'Mitigación'], [
 ['Sobrecarga de docentes y estudiantes', 'Alta', 'Alto', 'Integrar a asignaturas existentes; privilegiar acciones de bajo costo; priorizar.'], ['Baja participación en pre/post', 'Media', 'Alto', 'Aplicar en clase; recordatorios; incentivos simbólicos.'], ['Empresas con baja disponibilidad', 'Media', 'Medio', 'Convenios con anticipación; formatos cortos y virtuales.'], ['Interpretar mal el semáforo', 'Media', 'Medio', 'Formación breve para tutores; comunicación empática.'], ['Datos personales', 'Baja', 'Alto', 'Códigos seudonimizados; acceso restringido; consentimiento.'], ['Expectativas desmedidas sobre el programa', 'Media', 'Medio', 'Comunicar que se está evaluando y que los resultados se compartirán.']], [4.6, 2.0, 1.8, 8.2], size=8.8)
D.h2('6.4 Comunicación')
D.bullets(['**A estudiantes:** devolver los resultados con lenguaje simple (infografía y manual); explicar qué cambiará y por qué.', '**A docentes:** presentar los hallazgos y pedir su participación en 2 asignaturas ancla por carrera.', '**A empresas socias:** compartir los resultados y proponer formatos de colaboración breves.', '**Cierre del ciclo:** al terminar el semestre, informar qué funcionó, qué se ajustó y qué sigue.'])

D.part('CONCLUSIÓN')
D.h1('Conclusión y próximos pasos')
D.p('El plan reúne ocho recomendaciones (R1 a R8) en seis áreas. Tres ideas ordenan su ejecución: (1) **medir bien desde el inicio**, porque sin código, momento y grupo no se podrá demostrar el efecto de La Puerta; (2) **acercar el trabajo real a todos los estudiantes** mediante redes, simulaciones, visitas y proyectos breves, que es lo que los datos y los propios estudiantes señalan; y (3) **focalizar el acompañamiento por necesidad** (semáforo y brechas específicas) y no por el solo hecho de tener o no práctica previa.')
D.p('Los próximos pasos inmediatos son constituir el comité, corregir el formulario de medición (costo cero) y definir el grupo de comparación para el pretest de marzo de 2027. Las metas y costos son propuestas del equipo analista que deben validarse con la Dirección de Escuela.')
bibliografia(D, [2, 4, 5, 7, 8, 9, 11, 14, 15, 16, 18, 19, 20])
D.part('ANEXOS')
D.h1('Plantillas y protocolos')
D.h2('Anexo A. Plantilla de microproyecto (≤ $150.000 CLP)')
D.table(['Campo', 'Qué completar'], [['Nombre de la actividad', ''], ['Área y recomendación (A1–A6, R1–R8)', ''], ['Brecha que atiende (indicador y línea base)', ''], ['Descripción (qué se hará, para quiénes, cuántas personas)', ''], ['Resultado de aprendizaje o asignatura vinculada', ''], ['Responsable y equipo', ''], ['Fecha y duración', ''], ['Presupuesto (colación, materiales, difusión, otros)', ''], ['Indicadores y forma de medición', ''], ['Riesgos y mitigación', ''], ['Evidencia a recolectar (asistencia, bitácora, fotos con consentimiento, encuesta breve)', ''], ['Retroalimentación esperada y ajustes para la próxima vez', '']], [7.4, 9.2], size=9, zebra=False)
D.h2('Anexo B. Protocolo de evaluación pre/post con grupo de comparación')
D.numbered(['**Diseño:** cuasi-experimental con grupo de comparación no equivalente, medición antes y después en ambos grupos (Campbell y Stanley, 1963).', '**Asignación:** por sección completa; los grupos deben ser parecidos en carrera, semestre y práctica previa; registrar esas variables.', '**Medición:** misma encuesta (con A03/A04 corregidos) en las semanas 1–3 y en la última semana del semestre; código único obligatorio.', f"**Tamaño de muestra de referencia:** para detectar una diferencia de 0,3 desviaciones estándar entre grupos (≈ 0,2 puntos en el índice global), con 80 % de poder, 5 % de significación y una correlación pre–post asumida de 0,6, se necesitan unos **110 estudiantes por grupo** (cálculo aproximado con ajuste por la medición inicial; Cohen, 1988). **[HIPÓTESIS]** La correlación pre–post debe verificarse con datos propios.", '**Análisis:** comparar el postest entre grupos ajustando por el pretest y por práctica previa y año; informar tamaño del efecto e intervalos de confianza; corregir por comparaciones múltiples (Holm, 1979).', '**Indicadores de calidad:** emparejamiento ≥ 70 %; comparar a quienes respondieron ambos momentos con quienes no, para ver si hay sesgo de desgaste.', '**Complemento:** evaluación del tutor de empresa y respuestas abiertas codificadas por dos personas.'])
declaracion_ia(D, 'proponer acciones, indicadores, cronograma y criterios de decisión a partir de los hallazgos')
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/G_Manual_Propuestas_Mejora.docx'); print('G ok')
