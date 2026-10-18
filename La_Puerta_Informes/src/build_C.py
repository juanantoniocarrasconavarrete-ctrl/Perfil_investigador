from comun import *
D = Doc('Informe consolidado', 'Lo que dicen juntos el análisis descriptivo y el análisis de hipótesis: conclusiones estratégicas y camino a seguir', 'PRODUCTO C · INFORME CONSOLIDADO E INTEGRADO', G + 'portada_puerta.png', 'Proyecto La Puerta · Informe C · Consolidado')
g = R['global']; O = OF; fo = {r['var']: r for r in O['filas']}; S = O['semaforo_estudiantes']
contenido(D, ['Síntesis ejecutiva', 'Comparación entre ambos enfoques', 'Coincidencias y discrepancias', 'Factores críticos', 'Oportunidades de mejora', 'Recomendaciones estratégicas priorizadas', 'Conclusiones generales', 'Anexo: trazabilidad y declaración de uso de IA', 'Bibliografía integrada'])

D.h1('1. Síntesis ejecutiva')
D.p(f"Los **{N} estudiantes** que respondieron la encuesta del Proyecto La Puerta muestran una preparación percibida **razonablemente buena (3,87 de 5)**, con fortalezas de actitud (diálogo en equipo, ética, ganas de aprender) y una brecha nítida en lo que depende del **contacto con el mundo laboral real**: conocer las tareas y exigencias, comprobar si el trabajo calza con los propios intereses y, sobre todo, **contar con una red de contactos**.")
D.kpis([(n(g['media']), 'puntaje global\n(1 a 5)', NAVY), (pc(IT['P12']['fav']), 'tiene red de contactos\n(brecha mayor)', CORAL), (pc(IT['P15']['fav']), 'quiere proyectos\ncon empresas', TEAL), ('+' + n(fo['GLOBAL']['dif']), 'ventaja con práctica\nprevia (esperada: 0,8–1,2)', AMB)])
D.h3('La historia en cinco frases')
D.numbered([
 '**Hay una base sólida:** siete de cada diez respuestas son favorables y ninguna dimensión cae bajo el 3,50.',
 '**El punto débil es la red de contactos**, y lo es para todos los perfiles: lo confirman tanto la descripción como la prueba de hipótesis.',
 '**Lo que se asocia con sentirse seguro de adaptarse es conocer y probar el trabajo real**, más que haber tenido una práctica previa en sí.',
 '**La práctica previa ayuda, pero la brecha es pequeña** (+0,17) frente a la proyectada por el proyecto (0,8–1,2): la hipótesis central se sostiene en dirección, no en magnitud.',
 '**El efecto de La Puerta sigue sin poder medirse** porque la base no trae código, momento ni grupo; es la corrección más urgente y más barata.'])
D.callout('Mensaje para la toma de decisiones', 'Invertir en **contacto real con el trabajo y con personas de empresas** (redes, microexperiencias, simulaciones) responde a lo que los datos muestran como brecha, a lo que los estudiantes piden con sus palabras y a una demanda alta y homogénea (83 %). Antes de escalar el programa, **corregir el diseño de medición** para poder demostrar su efecto.', TEAL)
aviso_datos(D)

D.h1('2. Comparación entre ambos enfoques')
D.p('Los dos informes parten de los mismos datos y responden preguntas distintas. Mirarlos juntos evita dos errores frecuentes: **creer que toda diferencia observada es real** (error del descriptivo solo) y **creer que lo «no significativo» no existe** (error del contraste solo).')
D.table(['', 'Informe A · Descriptivo', 'Informe B · Con hipótesis'], [
 ['**Pregunta que responde**', '¿Cómo se perciben hoy los estudiantes? ¿Dónde están las fortalezas y brechas?', '¿Las diferencias entre perfiles son suficientemente grandes como para no deberse al azar? ¿Se cumple lo que el proyecto esperaba?'],
 ['**Qué hace**', 'Describe promedios, porcentajes, semáforo, perfiles y comentarios abiertos.', 'Contrasta 6 hipótesis con reglas de decisión definidas de antemano, corrige comparaciones múltiples y estima tamaños de efecto.'],
 ['**Fortaleza**', 'Cercano, intuitivo, útil para priorizar y comunicar.', 'Disciplina frente a la sobreinterpretación; usa los umbrales del propio proyecto.'],
 ['**Riesgo**', 'Leer como «real» una diferencia pequeña o casual (p. ej., el «valle» de 3.º–4.º).', 'Poca potencia: no detecta diferencias menores a 0,28 puntos; no responde causalidad.'],
 ['**Qué aporta al otro**', 'Identifica qué mirar: P12, D1, tramo 3.º–4.º, semáforo rojo.', 'Dice cuáles de esas pistas resisten un examen riguroso y cuáles no.']], [3.2, 6.7, 6.7], size=9)
D.fig('g15_hipotesis', 'Figura 1. Resultados de las seis hipótesis (síntesis del Informe B).')

D.h1('3. Coincidencias y discrepancias')
D.h2('3.1 Donde ambos enfoques coinciden')
D.table(['Hallazgo', 'Informe A (descriptivo)', 'Informe B (hipótesis)', 'Confianza'], [
 ['**Red de contactos débil**', 'P12 = 41 % de acuerdo; la más baja de las 15.', 'H3 respaldada: P12 menor que las otras 14 afirmaciones (p ajustado < 0,001).', 'Alta'],
 ['**Alta demanda de vincularse con empresas**', 'P15 = 83 % de acuerdo; tema más pedido en comentarios (simulación, terreno).', 'H5 respaldada: > 70 % (p < 0,001); homogénea entre perfiles.', 'Alta'],
 ['**Práctica previa: ventaja pequeña**', 'Con práctica puntúan algo más (+0,17); 14 % rojos vs. 25 %.', 'H1 parcial: dirección esperada, magnitud mucho menor a la proyectada; no concluyente.', 'Media-alta'],
 ['**Conocer el trabajo real importa**', 'P01, P02, P09 bajo 70 %; piden salidas y simulaciones; sin práctica «no tienen aprendizaje que contar».', 'H4 respaldada: P01, P05 y P09 se asocian con seguridad de adaptarse (R² ≈ 49 %).', 'Media (asociación)'],
 ['**Año de estudio no ordena los resultados**', 'Sin escalera; 3.º–4.º semestre más bajo.', 'H2 no respaldada (p ajustado ≥ 0,49).', 'Media']], [3.4, 4.8, 5.4, 3.0], size=8.8, colors={(0, 3): TEAL, (1, 3): TEAL, (2, 3): SKY, (3, 3): SKY, (4, 3): SKY})
D.h2('3.2 Donde se separan (y cómo leerlo)')
D.table(['Aspecto', 'Lectura descriptiva', 'Lectura con hipótesis', 'Cómo integrarlo'], [
 ['**Práctica previa**', 'Puntúan más alto en las 5 dimensiones; mayor distancia en D1 (+0,33).', 'Ninguna diferencia resiste la corrección por pruebas múltiples; el efecto detectable mínimo es 0,28.', 'Hay una **tendencia positiva real pero pequeña**; no basar decisiones fuertes en D1 solamente.'],
 ['**Dimensión D4**', 'D4 = 3,72 («amarillo»): parece una dimensión regular.', 'D4 mezcla P15 (alto) y P11–P12 (bajos); alfa = 0,64. Redes puras = 3,45.', '**Separar «interés» de «red»** en el próximo instrumento; el promedio de D4 oculta el problema.'],
 ['**Año de estudio**', '5.º semestre o más puntúa más alto (3,99).', 'No significativo (p ajustado 0,49).', 'Tratar el «valle» de 3.º–4.º como **hipótesis para la próxima cohorte**, no como hecho.'],
 ['**Magnitud del problema**', 'Cohorte en el rango «mixto» (3,87).', 'Pero sin la brecha por experiencia previa que define a ese escenario.', 'No segregar por «práctica previa sí/no»; focalizar por **semáforo rojo** y por brechas específicas.'],
 ['**Qué sostiene la confianza**', 'Comentarios abiertos: «el resto es solo relleno», «no he tenido práctica».', 'Quienes no declaran aprendizaje tienen índice más bajo (3,64 vs. 3,92; p = 0,023).', 'La voz estudiantil y los datos **coinciden**; vale la pena tomar en serio las respuestas «negativas».']], [2.9, 4.4, 4.7, 4.6], size=8.8)
D.callout('Una convergencia con consecuencias', 'Tanto la descripción como el contraste señalan lo mismo desde dos ángulos: **lo que cambia la seguridad de los estudiantes no es el rótulo «tiene o no tiene práctica», sino lo que aprendió o vio en ella.** Por eso, intervenciones breves que acerquen el trabajo real a todos los estudiantes son más promisorias que una política basada en el historial de práctica.', TEAL)

D.h1('4. Factores críticos')
D.p('Los factores críticos son los pocos puntos donde se concentra el riesgo o la oportunidad. Se priorizaron por **magnitud de la brecha**, **consistencia entre ambos informes** y **posibilidad real de intervenir**.')
D.table(['#', 'Factor crítico', 'Evidencia', 'Riesgo si no se aborda', 'Consistencia'], [
 ['1', '**Ausencia de red de contactos** (P12)', '41 % de acuerdo; 30 % en desacuerdo; transversal a todos los perfiles.', 'Llegar a la práctica y al empleo sin referentes; dependencia de redes familiares.', 'A + B'],
 ['2', '**Poco contacto con el trabajo real** (P01, P02, P09)', '62–69 % de acuerdo; se asocian con la seguridad de adaptarse.', 'Expectativas irreales; shock de transición.', 'A + B + voz estudiantil'],
 ['3', '**Medición que no permite evaluar el programa**', 'Código, momento, grupo y POST_EXP1 vacíos; A03/A04 no aplicados.', 'Imposibilidad de demostrar el impacto; decisiones sin evidencia.', 'A + B'],
 ['4', '**21 % de estudiantes en rojo**', '38 estudiantes < 3,50; 28 sin práctica previa y 10 con.', 'Mayor riesgo de mala experiencia de práctica y deserción.', 'A + B'],
 ['5', '**Brecha en traducir lo técnico** (P04, P06)', '68 % y 66 %; 22 menciones sobre comunicación.', 'Dificultad para integrarse y ser comprendidos en la empresa.', 'A + voz estudiantil'],
 ['6', '**Herramientas e inglés**', '20 y 19 menciones; ERP, Excel, Power BI, inglés.', 'Desfase con lo que usan las empresas.', 'Solo A (cualitativo)']], [0.8, 3.6, 4.6, 4.6, 3.0], size=8.6, align=['c', 'l', 'l', 'l', 'l'])

D.h1('5. Oportunidades de mejora')
D.fig('g18_brechas', 'Figura 2. Las ocho afirmaciones con mayor distancia a la meta de 70 %.')
D.bullets([
 '**La demanda existe:** 83 % quiere proyectos con empresas; la institución no parte de cero ni debe convencer a los estudiantes.',
 '**Hay un mecanismo plausible a intervenir:** conocer tareas, exigencias y contrastar el trabajo con los intereses se asocia con la seguridad de adaptarse.',
 '**Las fortalezas de actitud** (diálogo, ética, confianza ante lo nuevo) permiten trabajar con estudiantes dispuestos a aprender.',
 '**Los estudiantes ya propusieron las soluciones:** simulaciones, salidas, herramientas reales, comunicación, inglés.',
 '**La corrección de medición es barata** y multiplica el valor de todo lo demás: con un código y un campo de grupo se podrá demostrar el impacto de La Puerta.'])

D.h1('6. Recomendaciones estratégicas priorizadas')
D.fig('g23_prioridad', 'Figura 3. Matriz impacto–esfuerzo de las recomendaciones.', 14)
D.table(['Prioridad', 'Recomendación', 'Resultado esperado', 'Indicador de éxito', 'Plazo'], [
 ['**1 · Hacer ya**\nR1', '**Rediseñar la medición:** código único, momento, grupo y POST_EXP1 obligatorios; agregar A03 y A04; considerar evaluación de jefatura.', 'Poder evaluar el efecto de La Puerta.', '100 % de registros con código, momento y grupo.', 'Próxima aplicación'],
 ['**2 · Hacer ya**\nR4', '**Focalizar por semáforo rojo** (en vez de por «sin práctica previa»).', 'Acompañar a quienes más lo necesitan.', '% de estudiantes en rojo que reciben apoyo antes de la práctica.', 'Antes de la práctica'],
 ['**3 · Estratégico**\nR2', '**Programa de redes** (mentorías, ferias, charlas, visitas).', 'Aumentar la red de contactos.', 'P12 ≥ 60 % de acuerdo; ≥ 3 contactos por estudiante.', '1–2 semestres'],
 ['**4 · Estratégico**\nR3', '**Microexperiencias de contacto real:** simulaciones, visitas, proyectos cortos con empresas.', 'Conocer el trabajo real; mayor seguridad.', 'P01, P02, P09 ≥ 70 %; P10 ≥ 75 %.', '1–2 semestres'],
 ['**5 · Ajuste**\nR5', '**Taller de comunicación** y presentación profesional.', 'Explicar lo técnico con claridad.', 'P04 ≥ 75 %.', '1 semestre'],
 ['**6 · Evaluar**\nR6', '**Inglés y herramientas** (ERP, Excel, BI) donde corresponda.', 'Reducir el desfase con la empresa.', 'Menciones de este tema en el siguiente levantamiento < 10.', '2 semestres'],
 ['**7 · Evaluar**\nR7', '**Atender el tramo 3.º–4.º semestre.**', 'Evitar el «valle» (si se confirma).', 'Brecha 3.º–4.º vs. otros < 0,1.', '1–2 semestres'],
 ['**8 · Ajuste**\nR8', '**Validar las respuestas abiertas** (doble codificación) y publicar el libro de códigos.', 'Rigor de la evidencia cualitativa.', 'Acuerdo entre codificadores ≥ 0,70 (kappa).', '1 mes']], [2.3, 5.4, 3.3, 3.8, 1.8], size=8.4)
D.callout('Un criterio para escalar', 'Antes de institucionalizar el modelo La Puerta en otras sedes, exigir la evidencia de un piloto con **grupo de comparación y medición antes/después**. El Informe Metodológico define como acción del Escenario 1 «institucionalizar el modelo»; con los datos actuales (Escenario 2 sin brecha de origen marcada) corresponde más bien **perfeccionar y evaluar**.', AMB, 'FFF7E0')

D.h1('7. Conclusiones generales')
D.numbered([
 '**La preparación percibida es buena y se apoya en la actitud; lo que falta es el contacto con el mundo real.** El puntaje global (3,87) y las fortalezas en diálogo, ética y confianza son una buena plataforma.',
 '**La red de contactos es la prioridad estratégica nº 1 de contenido.** Es la brecha mayor, nítida y transversal.',
 '**La hipótesis central del proyecto se sostiene en dirección, no en magnitud.** La práctica previa se asocia con mejores percepciones, pero no es el gran divisor que se proyectaba; lo que importa es lo que se vive y aprende en el contacto con el trabajo.',
 '**Los estudiantes piden lo que los datos sugieren:** más práctica real, simulación, terreno, herramientas, comunicación e inglés.',
 '**La evaluación del programa es la deuda metodológica de mayor valor.** Corregir la medición permitirá, en la próxima aplicación, responder la pregunta de fondo.',
 '**Cuidado con tres tentaciones:** (a) segregar por «tiene o no práctica previa»; (b) tomar como hecho el «valle» de 3.º–4.º; (c) afirmar que La Puerta funciona con datos de una sola medición.'])

D.h1('Anexo: trazabilidad y declaración de uso de IA')
D.table(['Cifra clave', 'Valor', 'Dónde se calculó'], [
 ['Puntaje global', f"{n(g['media'])} [{n(g['ci'][0])}; {n(g['ci'][1])}]", 'Informe A, 5.1'],
 ['P12 de acuerdo', pc(IT['P12']['fav']), 'Informe A, 5.2 · Informe B, 4.3'],
 ['Brecha con–sin práctica', f"+{n(fo['GLOBAL']['dif'])} [{n(fo['GLOBAL']['ci'][0])}; {n(fo['GLOBAL']['ci'][1])}]", 'Informe B, 4.1'],
 ['Correlación práctica–índice global', f"r = {n(O['pearson']['r'])}", 'Informe B, 4.1'],
 ['Estudiantes en rojo', f"{S['total']['Rojo']} ({pc(S['pct_total']['Rojo'])})", 'Informe A, 5.6'],
 ['R² del modelo de seguridad de adaptarse', pc(100 * R['H4']['ols']['r2']), 'Informe B, 4.4'],
 ['Diferencia mínima detectable (80 % poder)', n(O['mde_80']) + ' puntos', 'Informe B, 3']], [6.4, 4.6, 5.6], size=9)
D.p('Todos los números se generan con `src/analisis.py` y quedan en `src/resultados.json`; los gráficos con `src/graficos.py`. Si la base cambia, basta volver a ejecutar ambos scripts.', 9.5)
declaracion_ia(D, 'integrar los resultados de ambos enfoques, comparar sus conclusiones y proponer una priorización de recomendaciones')
bibliografia(D)
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/C_Informe_Consolidado.docx'); print('C ok')
