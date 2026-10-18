from comun import *
cover_art('portada_puerta')
D = Doc('Informe descriptivo', 'Cómo perciben su preparación para el mundo laboral los estudiantes de la Escuela de Administración y Negocios', 'PRODUCTO A · ANÁLISIS DESCRIPTIVO (SIN HIPÓTESIS)', G + 'portada_puerta.png', 'Proyecto La Puerta · Informe A · Análisis descriptivo')
g = R['global']; per = R['perfiles']; pp = R['perfiles_pct']; cal = R['calidad']
contenido(D, ['Resumen ejecutivo', 'Contexto y objetivos del estudio', 'Metodología explicada en simple', 'Quiénes respondieron', 'Resultados en detalle', 'Lo que dicen los estudiantes con sus propias palabras', 'Principales hallazgos', 'Conclusiones', 'Recomendaciones de mejora', 'Anexos: ficha técnica, tablas y declaración de uso de IA', 'Bibliografía y referencias'])

# 1 Resumen
D.h1('1. Resumen ejecutivo')
D.p(f"Entre el 13 y el 16 de octubre de 2026, **{N} estudiantes** de Duoc UC Sede San Bernardo respondieron una encuesta confidencial sobre qué tan preparados se sienten para enfrentar el mundo laboral. Este informe cuenta, sin tecnicismos, **qué dijeron**, **dónde están sus fortalezas** y **dónde conviene poner más apoyo**.")
D.kpis([(n(g['media']), 'puntaje global\n(escala 1 a 5)', NAVY), (pc(g['fav_items']), 'de las respuestas\nson «de acuerdo»', TEAL), (pc(IT['P12']['fav']), 'dice tener una red\nde contactos (P12)', CORAL), (pc(IT['P15']['fav']), 'quiere proyectos\ncon empresas reales', AMB)])
D.h3('Los cinco mensajes que hay que recordar')
D.numbered([
 f"**Hay una base sólida.** El puntaje global es {n(g['media'])} de 5 y siete de cada diez respuestas son favorables. Las mayores fortalezas son dialogar en equipo ({pc(IT['P07']['fav'])}), priorizar la ética bajo presión ({pc(IT['P14']['fav'])}), el interés en proyectos reales ({pc(IT['P15']['fav'])}) y la confianza ante tareas nuevas ({pc(IT['P03']['fav'])}).",
 f"**La red de contactos es el punto más débil.** Solo {pc(IT['P12']['fav'])} dice contar con referentes laborales a quienes recurrir, y {pc(IT['P12']['des'])} dice que no. Es la afirmación más baja de las 15, con bastante distancia de las demás.",
 f"**Conocer el trabajo «de verdad» está a medio camino.** Conocer las tareas reales (P01: {pc(IT['P01']['fav'])}), las exigencias de las empresas (P02: {pc(IT['P02']['fav'])}) y haber comprobado si el trabajo calza con los intereses propios (P09: {pc(IT['P09']['fav'])}) quedan bajo la meta de 70 %.",
 f"**Quieren más práctica, no más teoría.** En sus comentarios, lo que más piden antes de la práctica profesional son simulaciones y casos reales ({Q['abi2']['Simulaciones, casos reales y práctica aplicada']} menciones), comunicación y oratoria, inglés, herramientas como ERP y Excel, y salidas a terreno.",
 f"**Quienes ya hicieron una práctica puntúan algo más alto, pero la diferencia es pequeña** (+{n(H1['GLOBAL']['dif'])} puntos). Es una tendencia, no una brecha enorme."])
D.callout('Lo que este informe NO puede decir', 'Con una sola medición no es posible saber si el programa La Puerta cambió algo. Para eso hace falta medir a las mismas personas antes y después (ver R1).', CORAL, 'FDEEE9', '⚠')

# 2 Contexto
D.h1('2. Contexto y objetivos del estudio')
D.p('El Proyecto La Puerta nace de una pregunta práctica: **¿cómo llegan los estudiantes a su práctica profesional?** La hipótesis de trabajo del proyecto es que haber vivido antes una experiencia laboral ayuda a enfrentar el «shock de transición» al mundo del trabajo y fortalece la confianza en las propias capacidades (autoeficacia). Para explorarlo, el equipo aplicó una encuesta de percepción con 15 afirmaciones agrupadas en cinco dimensiones, más dos preguntas abiertas.')
D.fig('g14_marco', 'Figura 1. Mapa del estudio: cinco dimensiones que conversan con la seguridad para adaptarse a un puesto de trabajo.')
D.h3('Qué dice la literatura (en pocas palabras)')
D.bullets(['La **autoeficacia** —creer que uno puede lograr una tarea— se construye sobre todo con experiencias directas de logro (Bandura, 1997); en el plano vocacional, esas creencias influyen en los intereses y las decisiones de carrera (Lent et al., 1994).', 'La **empleabilidad** no es solo saber técnico: incluye cómo se piensa y se actúa frente al trabajo y el capital social del egresado (Yorke, 2006; Tomlinson, 2017).', 'Las **redes** de contactos, incluso los vínculos «débiles», abren oportunidades de información y empleo (Granovetter, 1973).', 'Aprender haciendo —ciclos de experiencia, reflexión y aplicación— fortalece lo aprendido en aula (Kolb, 1984), y ver el error como información favorece la persistencia (Dweck, 2006).'])
D.h3('Objetivos de este informe descriptivo')
D.bullets(['Describir cómo respondieron los estudiantes en cada afirmación y dimensión.', 'Identificar fortalezas, oportunidades de mejora y percepciones predominantes.', 'Mostrar diferencias relevantes entre perfiles (año de estudio, práctica previa).', 'Recoger, con sus propias palabras, qué aprendieron y qué apoyo necesitan.', 'Entregar recomendaciones prácticas y alcanzables.'])
D.p('**Importante:** este es el informe «sin hipótesis». Aquí solo se describe lo observado, sin probar teorías. El contraste de hipótesis está en el Informe B, y ambos se integran en el Informe C.', italic=True)

# 3 Metodología
D.h1('3. Metodología explicada en simple')
D.h2('3.1 Qué se preguntó y cómo se respondió')
D.p('Cada afirmación (por ejemplo, «Aprendo de mis errores») se respondió en una escala de 1 a 5, donde **1 = muy en desacuerdo, 3 = ni de acuerdo ni en desacuerdo y 5 = muy de acuerdo**. También existía la opción «No sé / No aplica», que se excluyó del cálculo (representa solo el ' + pc(cal['pct_celdas_NA'], 1) + ' de todas las respuestas posibles).')
D.table(['Dimensión', 'De qué trata', 'Afirmaciones'], [
 ['D1 · Conocer el rol profesional', 'Saber qué se hace en el trabajo y qué exigen las empresas', 'P01, P02'],
 ['D2 · Transferir lo aprendido', 'Usar lo de clases en problemas reales; explicar con claridad', 'P03, P04, P05, P06'],
 ['D3 · Autoeficacia laboral', 'Confianza para trabajar en equipo, decidir y adaptarse', 'P07, P08, P09, P10'],
 ['D4 · Redes e interés por vincularse', 'Contactos profesionales e interés en proyectos con empresas', 'P11, P12, P15'],
 ['D5 · Aprender del error y ética', 'Convertir errores en aprendizaje; mantener la ética', 'P13, P14']], [4.6, 8.2, 3.8], size=9)
D.h2('3.2 Cómo se calcularon los resultados')
D.bullets([
 '**Promedio (1 a 5):** resume cada afirmación o dimensión. Como la escala es de opinión, se usa como orientación, no como medida exacta (Norman, 2010; Sullivan y Artino, 2013).',
 '**% de acuerdo:** porcentaje que respondió 4 o 5. Es la cifra más fácil de comunicar y es la que usamos para el semáforo.',
 '**Semáforo de afirmaciones (criterio propuesto):** Fortaleza ≥ 80 % · Funcional 70–79 % · En desarrollo 60–69 % · Brecha < 60 %. La meta de 70 % se alinea con la exigencia usada en las rúbricas DUOC.',
 '**Semáforo oficial por promedio (del Informe Metodológico del proyecto):** Verde ≥ 4,20 · Amarillo 3,50–4,19 · Rojo < 3,50. Se usa para clasificar estudiantes y grupos.',
 '**Margen de error:** se calculó con un método llamado «bootstrap»; en los gráficos aparece como una barra gris alrededor del promedio.',
 f"**Confiabilidad:** el conjunto de 15 afirmaciones se comporta de forma coherente (alfa de Cronbach = {n(g['alpha'])}; sobre 0,70 es aceptable, Cronbach, 1951). La dimensión D4 es la menos consistente ({n(DM['D4']['alpha'])}) porque mezcla dos ideas distintas: tener contactos (P11, P12) y querer proyectos con empresas (P15)."])
D.h2('3.3 Calidad de los datos')
D.bullets([f"{N} respuestas, todas con consentimiento informado; no hay correos repetidos.", f"{cal['respuestas_NA_total']} respuestas «No sé / No aplica» ({pc(cal['pct_celdas_NA'], 1)}); las afirmaciones con más «no sé» son P09, P12 y P14 (7 cada una).", f"{cal['straightlining_n']} estudiantes ({pc(100*cal['straightlining_n']/N,1)}) marcaron la misma opción en las 15 afirmaciones. Se mantuvieron en el análisis; al quitarlos, los resultados casi no cambian (ver Anexo).", "La Escuela de Administración y Negocios concentra el 98 % de las respuestas, por lo que **no es posible comparar entre escuelas**."])
aviso_datos(D)

# 4 perfil
D.h1('4. Quiénes respondieron')
D.fig('g01_perfil', f"Figura 2. Perfil de los {N} participantes: semestre en curso, práctica previa y escuela.")
D.p(f"La mitad de la muestra ({pc(100*R['perfil']['anio']['1.º–2.º sem.']/N)}) cursa primer año; un {pc(100*R['perfil']['anio']['5.º–6.º sem.']/N)} está en tercer año y apenas una persona en cuarto. Sobre la práctica previa, **{R['perfil']['practica']['Sin práctica previa']} estudiantes ({pc(100*R['perfil']['practica']['Sin práctica previa']/N)}) nunca han hecho una práctica**, {R['perfil']['practica']['Práctica EMTP']} la hicieron en el colegio técnico-profesional (EMTP), {R['perfil']['practica']['Pasantía en la carrera']} hicieron una pasantía en su carrera y {R['perfil']['practica']['Práctica en otra carrera']} en otra carrera.")
cx = R['cruce_anio_practica']
D.callout('Un detalle que conviene recordar', f"Práctica previa y año de estudio **van de la mano**: en 1.º–2.º semestre el {pc(100*cx['1.º–2.º sem.']['con']/(cx['1.º–2.º sem.']['con']+cx['1.º–2.º sem.']['sin']))} tiene práctica previa; en 5.º semestre o más, el {pc(100*cx['5.º sem. o más']['con']/(cx['5.º sem. o más']['con']+cx['5.º sem. o más']['sin']))}. Al comparar grupos hay que tener presente que se mezclan ambos efectos.", SKY, 'EEF4FB')

# 5 resultados
D.h1('5. Resultados en detalle')
D.h2('5.1 Panorama general')
D.p(f"El puntaje global promedio es **{n(g['media'])}** (margen de error 95 %: {n(g['ci'][0])} a {n(g['ci'][1])}). La mitad de los estudiantes está sobre {n(g['mediana'])}. Si clasificamos a cada estudiante por su propio promedio: **{per['Sólido (≥4)']} ({pc(pp['Sólido (≥4)'])}) tienen un perfil sólido** (4 o más), **{per['Intermedio (3–3,99)']} ({pc(pp['Intermedio (3–3,99)'])}) un perfil intermedio** y **{per['Por fortalecer (<3)']} ({pc(pp['Por fortalecer (<3)'])}) un perfil por fortalecer** (menos de 3).")
D.fig('g04_global_hist', 'Figura 3. Cómo se distribuye el puntaje global de los estudiantes.')
D.lee('Cada barra cuenta cuántos estudiantes tienen un puntaje en ese tramo. La mayoría se agrupa entre 3,5 y 4,5; hay una «cola» pequeña hacia abajo (rojo) que corresponde a quienes más necesitan apoyo.')
D.h2('5.2 Afirmación por afirmación')
D.fig('g02_items', 'Figura 4. Distribución de respuestas en las 15 afirmaciones (ordenadas de menor a mayor acuerdo).', 16.4)
D.lee('Cada fila es una afirmación. A la derecha del centro, en verde, quienes están de acuerdo; a la izquierda, en rojo, quienes están en desacuerdo, y en gris los neutrales. Entre más larga la barra verde, mejor. La fila de abajo (P12, contactos) destaca por su barra roja larga.')
D.fig('g05_semaforo', 'Figura 5. Semáforo de las afirmaciones frente a la meta de 70 %.')
rows = []; cols = {}
for i, x in enumerate(sorted(R['items'], key=lambda z: -z['fav'])):
    rows.append([x['id'], SHORT[x['id']], n(x['media']), pc(x['fav']), pc(x['neu']), pc(x['des']), x['semaforo']]); cols[(i, 6)] = SEMC[x['semaforo']]
D.table(['Id', 'Afirmación', 'Prom.', 'De acuerdo', 'Neutral', 'En desac.', 'Semáforo'], rows, [1.0, 7.0, 1.4, 1.9, 1.6, 1.7, 2.0], colors=cols, size=8.5, align=['c', 'l', 'c', 'c', 'c', 'c', 'c'])
D.h3('Fortalezas (80 % o más de acuerdo)')
D.bullets([f"**Diálogo y acuerdos en equipo (P07):** {pc(IT['P07']['fav'])}. Los estudiantes se ven capaces de expresar su punto de vista buscando acuerdos.", f"**Ética bajo presión (P14):** {pc(IT['P14']['fav'])}.", f"**Interés en proyectos con empresas (P15):** {pc(IT['P15']['fav'])}; solo {pc(IT['P15']['des'])} en desacuerdo.", f"**Confianza ante tareas nuevas (P03):** {pc(IT['P03']['fav'])}; es la única afirmación sobre competencia donde el 5 («muy de acuerdo») es la respuesta más frecuente ({pc(IT['P03']['p5'])}).", f"**Autonomía vs. consulta (P08):** {pc(IT['P08']['fav'])}."])
D.h3('Oportunidades de mejora (menos de 70 %)')
D.bullets([f"**Red de contactos (P12):** {pc(IT['P12']['fav'])} de acuerdo y {pc(IT['P12']['des'])} en desacuerdo. Brecha de {n(70-IT['P12']['fav'],0)} puntos respecto de la meta.", f"**Haber comprobado si el trabajo real calza con los intereses (P09):** {pc(IT['P09']['fav'])}.", f"**Saber contactar a profesionales (P11):** {pc(IT['P11']['fav'])}; **método adecuado para la empresa (P06):** {pc(IT['P06']['fav'])}.", f"**Conocer tareas reales (P01) y exigencias de las empresas (P02):** {pc(IT['P01']['fav'])} y {pc(IT['P02']['fav'])}; **explicar con claridad (P04):** {pc(IT['P04']['fav'])}; **sentirse seguro/a de adaptarse (P10):** {pc(IT['P10']['fav'])}."])
D.callout('Un patrón interesante', f"Los estudiantes se sienten **más capaces de actuar** (resolver, dialogar, decidir, ser éticos) que **seguros de cómo es realmente el trabajo** (conocer tareas, exigencias, contactos). Dicho simple: tienen las ganas y la actitud; les falta ver el terreno. Esa diferencia es la que más aparece también en los comentarios abiertos.", TEAL)
D.h2('5.3 Las cinco dimensiones')
D.fig('g03_dimensiones', 'Figura 6. Promedio de cada dimensión con su margen de error.')
D.fig('g12_cajas', 'Figura 7. Dispersión de los puntajes por dimensión.')
D.table(['Dimensión', 'Promedio', 'Margen de error 95 %', '% de acuerdo', 'Semáforo oficial'], [
 [f"{d['id']} · {d['nombre']}", n(d['media']), f"{n(d['ci'][0])} a {n(d['ci'][1])}", pc(d['fav']), OF['semaforo_dims'][d['id']]] for d in sorted(R['dims'], key=lambda z: -z['media'])], [6.2, 2, 3.4, 2.4, 2.6], size=9, align=['l', 'c', 'c', 'c', 'c'])
D.p('Las cinco dimensiones quedan en el tramo **amarillo** del semáforo oficial (entre 3,50 y 4,19): funcionan, pero ninguna alcanza el verde (4,20). La más alta es **aprender del error y ética (D5)**; la más baja, **redes (D4)**. Como los márgenes de error de D1, D2, D3 y D5 se traslapan, no conviene sacar conclusiones fuertes entre ellas; la que sí se separa es D4.')
D.h2('5.4 Un vistazo a cada dimensión')
D.h3('D1 · Conocer el rol profesional')
D.p(f"Promedio {n(DM['D1']['media'])}. Dos de cada tres estudiantes dicen conocer las tareas reales y las exigencias de las empresas. Hay un 10–12 % que se declara en desacuerdo: son estudiantes que probablemente aún no han visto una empresa «por dentro».")
D.h3('D2 · Transferir lo aprendido')
D.p(f"Promedio {n(DM['D2']['media'])}. Dentro de esta dimensión hay dos mundos: **confianza y aplicación** (P03: {pc(IT['P03']['fav'])}; P05: {pc(IT['P05']['fav'])}) y **traducción al lenguaje de la empresa** (P04: {pc(IT['P04']['fav'])}; P06: {pc(IT['P06']['fav'])}). Sienten que saben usar lo aprendido, pero les cuesta más explicarlo y elegir el método adecuado.")
D.h3('D3 · Autoeficacia laboral')
D.p(f"Promedio {n(DM['D3']['media'])}. El diálogo en equipo y la autonomía son muy fuertes (P07 y P08, 80 % o más); en cambio, haber contrastado el trabajo real con los propios intereses (P09: {pc(IT['P09']['fav'])}) y la seguridad de adaptarse (P10: {pc(IT['P10']['fav'])}) son más bajas.")
D.h3('D4 · Redes e interés por vincularse')
D.fig('g16_redes', 'Figura 8. Dentro de D4: muchas ganas de vincularse, poca red construida.')
D.p(f"Promedio {n(DM['D4']['media'])}, pero este número esconde dos realidades: el **interés** es altísimo (P15: {pc(IT['P15']['fav'])}) mientras que la **red real** es débil (P12: {pc(IT['P12']['fav'])}). Si se miran solo las dos afirmaciones de contactos (P11 y P12), el promedio baja a {n(R['H3']['D4_redes_media'])}.")
D.h3('D5 · Aprender del error y ética')
D.p(f"Promedio {n(DM['D5']['media'])}, la dimensión más alta. {pc(IT['P14']['fav'])} prioriza la ética bajo presión y {pc(IT['P13']['fav'])} aprende de sus errores en vez de desmotivarse.")
D.h2('5.5 Diferencias entre perfiles de estudiantes')
D.p(f"Se compararon los resultados según **práctica previa** y **año de estudio**. Aquí solo se describe lo observado; en el Informe B se prueba si las diferencias podrían deberse al azar.")
D.fig('g06_practica', 'Figura 9. Promedio por dimensión: estudiantes con y sin práctica previa.')
D.p(f"**Práctica previa:** quienes la tienen puntúan más alto en las cinco dimensiones (global {n(H1['GLOBAL']['media_con'])} vs. {n(H1['GLOBAL']['media_sin'])}). La mayor distancia está en **conocer el rol profesional** (+{n(H1['D1']['dif'])}) y en **autoeficacia laboral** (+{n(H1['D3']['dif'])}). Se parecen en trabajo en equipo (P07), aplicación de lo aprendido (P05) y aprendizaje del error.")
rows = []; cols = {}
tipos = R['por_practica_tipo']
for i, k in enumerate(['Sin práctica previa', 'Práctica EMTP', 'Pasantía en la carrera', 'Práctica en otra carrera']):
    t = tipos[k]; rows.append([k, t['n'], n(t['GLOBAL']), n(t['D1']), n(t['D2']), n(t['D3']), n(t['D4']), n(t['D5'])])
    for j, kk in enumerate(['GLOBAL', 'D1', 'D2', 'D3', 'D4', 'D5']): cols[(i, 2 + j)] = cell_col(t[kk])
D.table(['Tipo de práctica previa', 'n', 'Global', 'D1', 'D2', 'D3', 'D4', 'D5'], rows, [5.2, 1.2, 1.7, 1.6, 1.6, 1.6, 1.6, 1.6], colors=cols, size=9, align=['l'] + ['c'] * 7)
D.p('**Cuidado:** el grupo «otra carrera» tiene solo 5 personas; su promedio alto (4,51) no es generalizable.', 9, GRAY)
D.fig('g07_anio', 'Figura 10. Dimensiones según año de estudio.')
D.p(f"**Año de estudio:** no hay una «escalera» que suba semestre a semestre. El grupo de 3.º–4.º semestre es el que puntúa más bajo (global {n(H2['GLOBAL']['medias'][1])}) y quienes están en 5.º semestre o más puntúan más alto ({n(H2['GLOBAL']['medias'][2])}), sobre todo en conocer el rol (D1: {n(H2['D1']['medias'][2])}) y en ética y error (D5: {n(H2['D5']['medias'][2])}). Una posible lectura es que el segundo año es un «valle» entre el entusiasmo inicial y el contacto real con la práctica ({tag('I')}).")
D.h3('Detalle por afirmación y perfil (promedios)')
rows = []; cols = {}
for i, p_ in enumerate([f'P{k:02d}' for k in range(1, 16)]):
    a = R['heat_anio'][p_]; b = R['heat_pract'][p_]; rows.append([p_, SHORT[p_], n(a[0]), n(a[1]), n(a[2]), n(b[0]), n(b[1])])
    for j, v in enumerate(a + b): cols[(i, 2 + j)] = cell_col(v)
D.table(['Id', 'Afirmación', '1.º–2.º', '3.º–4.º', '5.º o más', 'Sin prác.', 'Con prác.'], rows, [1.0, 6.9, 1.6, 1.6, 1.8, 1.8, 1.9], colors=cols, size=8.5, align=['c', 'l', 'c', 'c', 'c', 'c', 'c'])
D.p('Color: verde ≥ 4,20 · amarillo 3,50–4,19 · rosado < 3,50. La red de contactos (P12) es la única fila que se mantiene amarilla o más baja en todos los perfiles.', 9, GRAY)
D.h2('5.6 Semáforo oficial por estudiante')
D.fig('g22_semaforo_oficial', 'Figura 11. Clasificación de cada estudiante según el semáforo del Informe Metodológico.')
sm = OF['semaforo_estudiantes']
D.p(f"Con los cortes oficiales (verde ≥ 4,20; rojo < 3,50), **{sm['total']['Verde']} estudiantes ({pc(sm['pct_total']['Verde'])}) quedan en verde, {sm['total']['Amarillo']} ({pc(sm['pct_total']['Amarillo'])}) en amarillo y {sm['total']['Rojo']} ({pc(sm['pct_total']['Rojo'])}) en rojo**. Estos 38 estudiantes en rojo son el grupo que, según el diseño del proyecto, requeriría nivelación focalizada antes de su práctica. Entre quienes ya hicieron práctica, el rojo es 14 %; entre quienes no, 25 %.")

# 6 cualitativo
D.h1('6. Lo que dicen los estudiantes con sus propias palabras')
D.p(f"Respondieron la pregunta abierta sobre aprendizaje **{Q['abi1_n']} personas** ({pc(100*Q['abi1_n']/N)}) y la pregunta sobre apoyo institucional **{Q['abi2_n']}** ({pc(100*Q['abi2_n']/N)}). Las respuestas se agruparon por temas (análisis temático; Braun y Clarke, 2006) con ayuda de IA; una respuesta puede tocar varios temas. Es una lectura preliminar que debe ser revisada por una persona.")
D.h2('6.1 ¿Cuál ha sido tu aprendizaje más valioso?')
D.fig('g10_abi1', 'Figura 12. Temas del aprendizaje más valioso (n = 142).')
D.bullets([f"**Habilidades blandas ({Q['abi1']['Habilidades blandas (equipo, comunicación, responsabilidad, adaptación)']} menciones):** trabajo en equipo, comunicación, responsabilidad, adaptación. Es el tema más frecuente.", f"**Conocimiento técnico ({Q['abi1']['Conocimiento técnico del área (finanzas, logística, comex, marketing, RR.HH.)']}):** finanzas, logística, comercio exterior, marketing, remuneraciones.", f"**Más claridad sobre el campo laboral ({Q['abi1']['Mayor claridad sobre el campo laboral y su carrera']}):** «hay muchas áreas en las que puede trabajar», «voy encaminada hacia algo que realmente quiero ejercer».", f"**Ética, inclusión y normativa ({Q['abi1']['Ética, inclusión y normativa']}):** destaca la inclusión de personas con discapacidad y la diversidad.", f"**Sin aprendizaje claro ({Q['abi1']['Sin aprendizaje claro / no sabe']}):** de ellas, {Q['abi1_por_practica']['Sin aprendizaje claro / no sabe']['sin']} son estudiantes sin práctica previa. Dicen cosas como «no he tenido experiencia laboral, no sabría si tengo algún aprendizaje»."])
D.callout('En sus palabras', ['«Lo más valioso que aprendí es que en el trabajo no solo importa saber hacer las cosas, sino también saber comunicarse, trabajar en equipo y tener buena disposición para aprender.»', '«Entender que los problemas en el trabajo no son las personas, son del diseño de trabajo.»', '«Podría ser que no siempre lo que se enseña en la teoría es lo que se aplica en la realidad. Por ejemplo, en mi práctica participé en procesos de reclutamiento y selección en donde la utilización de descriptores de cargo era casi nula…»'], TEAL)
D.h2('6.2 ¿Qué apoyo debería incorporar la institución antes de la práctica?')
D.fig('g11_abi2', 'Figura 13. Temas del apoyo solicitado (n = 136).')
D.bullets([f"**Simulaciones, casos reales y práctica aplicada ({Q['abi2']['Simulaciones, casos reales y práctica aplicada']}):** lo más pedido. «…simular una práctica de una empresa con el fin de que el alumno sepa a lo que se va a enfrentar».", f"**Comunicación, oratoria y habilidades blandas ({Q['abi2']['Comunicación, oratoria y habilidades blandas']}):** hablar en público, escucha activa, liderazgo, presentación personal.", f"**Inglés y otros idiomas ({Q['abi2']['Idiomas (inglés principalmente)']}):** aparece con insistencia; algunos señalan que su malla no incluye un ramo de inglés.", f"**Preparación para la práctica y el empleo ({Q['abi2']['Preparación para la práctica y el empleo (entrevista, CV, inducción, apoyo)']}):** entrevistas, currículum, LinkedIn, inducción, ayudantías para buscar práctica.", f"**Software y herramientas reales ({Q['abi2']['Software y herramientas (ERP, SAP, Softland, Excel, Python, Power BI, IA)']}):** SAP, Softland, Excel avanzado, Power BI, Python.", f"**Salidas a terreno, visitas y ferias ({Q['abi2']['Salidas a terreno, visitas, ferias y charlas']}):** visitar puertos, centros de distribución, bodegas y ferias laborales.", f"Temas menos frecuentes pero relevantes: **legislación laboral y remuneraciones** ({Q['abi2']['Legislación laboral, contratos y remuneraciones']}) e **inclusión** ({Q['abi2']['Inclusión (lengua de señas, accesibilidad)']}; por ejemplo, lengua de señas)."])
D.fig('g19_abi2_practica', 'Figura 14. Qué piden quienes tienen y no tienen práctica previa (número de menciones).')
D.p(f"Un matiz: entre quienes **no** han hecho práctica, lo más pedido son **salidas a terreno** ({Q['abi2_por_practica']['Salidas a terreno, visitas, ferias y charlas']['sin']} vs. {Q['abi2_por_practica']['Salidas a terreno, visitas, ferias y charlas']['con']}) y **simulaciones** ({Q['abi2_por_practica']['Simulaciones, casos reales y práctica aplicada']['sin']} vs. {Q['abi2_por_practica']['Simulaciones, casos reales y práctica aplicada']['con']}): quieren ver el trabajo antes de vivirlo. Entre quienes sí la hicieron, destaca la **comunicación y las habilidades blandas** ({Q['abi2_por_practica']['Comunicación, oratoria y habilidades blandas']['con']} vs. {Q['abi2_por_practica']['Comunicación, oratoria y habilidades blandas']['sin']}): ya saben que ahí está el desafío.")
sa = Q['sin_aprendizaje_test']
D.callout('Cuando los números y las palabras coinciden', f"Los {sa['n_sin']} estudiantes que dijeron no tener un aprendizaje claro también puntúan más bajo en el índice global ({n(sa['media_sin'])} vs. {n(sa['media_con'])}). Y los estudiantes que piden «ver el trabajo» son los mismos que en la encuesta dicen no haber comprobado si el trabajo calza con ellos (P09).", SKY, 'EEF4FB')

# 7 hallazgos
D.h1('7. Principales hallazgos')
D.p('Cada hallazgo se etiqueta según su solidez: **[HECHO]** dato observado; **[INTERPRETACIÓN]** lectura razonada que depende del contexto; **[BRECHA]** algo que falta saber o medir.', 9.5, GRAY)
F = [
 ('1', 'Base sólida: puntaje global 3,87 y 70 % de respuestas favorables. Ninguna dimensión llega a verde (4,20).', 'H'),
 ('2', 'La red de contactos (P12) es la afirmación más débil: 41 % de acuerdo, 30 % en desacuerdo.', 'H'),
 ('3', 'El interés por proyectos con empresas es muy alto (83 %) y homogéneo entre perfiles.', 'H'),
 ('4', 'Sienten más capacidad de actuar que conocimiento del trabajo real (P01, P02, P09 bajo 70 %).', 'I'),
 ('5', 'Quienes tienen práctica previa puntúan algo más alto (+0,17 global; +0,33 en conocer el rol), con diferencias pequeñas.', 'H'),
 ('6', 'El año de estudio no ordena los resultados; 3.º–4.º semestre es el tramo más bajo.', 'H'),
 ('7', '21 % de los estudiantes queda en rojo (< 3,50) según el semáforo oficial.', 'H'),
 ('8', 'Los comentarios piden práctica real: simulaciones, terreno, herramientas, inglés y comunicación.', 'H'),
 ('9', 'Quienes no han hecho práctica sienten que no tienen «aprendizajes laborales» que contar.', 'I'),
 ('10', 'No se puede medir el efecto de La Puerta: faltan código, momento y grupo, y la valoración del programa.', 'B')]
D.table(['N.º', 'Hallazgo', 'Estatus'], [[a, b, tag(c)] for a, b, c in F], [1.0, 11.8, 3.8], colors={(i, 2): {'H': TEAL, 'I': SKY, 'B': CORAL}[c] for i, (a, b, c) in enumerate(F)}, size=9.5, align=['c', 'l', 'c'])

# 8 conclusiones
D.h1('8. Conclusiones')
D.numbered([
 f"**Los estudiantes llegan a la práctica con confianza razonable.** Siete de cada diez de sus respuestas son favorables (de acuerdo o muy de acuerdo); la actitud (ética, diálogo, ganas de aprender) es la base más fuerte.",
 "**El vacío está en el contacto con el mundo real**, no en la motivación. Conocer tareas, exigencias, contactos y comprobar si el trabajo les gusta son los puntos más bajos.",
 "**La red de contactos es la brecha más nítida y transversal**: aparece en todos los perfiles, años y tipos de práctica.",
 "**La práctica previa ayuda, pero no explica todo.** Quienes ya trabajaron se sienten algo más preparados; la diferencia es moderada y parte de ella se confunde con el año de estudio.",
 "**Los propios estudiantes ya dicen qué necesitan:** simulaciones realistas, salidas a terreno, herramientas de uso real, inglés y comunicación.",
 "**Con esta base solo se puede describir, no evaluar el programa.** El diseño pre-post con grupo de comparación sigue pendiente."])
D.h2('Limitaciones')
D.bullets(['Todos los datos son **autopercepciones**: lo que cada estudiante cree de sí mismo, no una medición de su desempeño ni la mirada de jefaturas; además, al venir todo de la misma fuente, las respuestas tienden a parecerse entre sí (Podsakoff et al., 2003).', 'Es una **sola medición**; no se puede saber qué cambió ni por qué.', 'La muestra es **voluntaria** y concentrada en una escuela; no representa a toda la institución.', 'Las respuestas abiertas se codificaron con ayuda de IA; requieren validación humana.', 'El instrumento aplicado (15 afirmaciones, 5 dimensiones) **no coincide con el descrito en el Informe Metodológico** (que incluye las preguntas A03 y A04 sobre preparación percibida y valoración de la experiencia previa): esa parte no pudo analizarse.'])

# 9 recomendaciones
D.h1('9. Recomendaciones de mejora')
D.p('Se ordenan por urgencia e impacto esperado. Los detalles de implementación están en el Manual de propuestas de mejora (Producto G).')
D.table(['Cód.', 'Recomendación', 'Por qué', 'Plazo'], [
 ['R1', '**Corregir el diseño de medición:** código único obligatorio, momento (pre/post) y grupo (La Puerta/comparación) como campos requeridos; agregar A03 y A04.', 'Sin esto no se puede evaluar el programa.', 'Antes de la próxima aplicación'],
 ['R2', '**Construir redes desde el primer año:** mentorías con egresados y practicantes, ferias y charlas con empresas.', 'P12 = 41 % de acuerdo; es la brecha mayor.', '1 semestre'],
 ['R3', '**Microexperiencias de contacto real:** simulaciones de la práctica (entrevista, primer día, conversación con jefatura), visitas y salidas a terreno.', 'Es lo más pedido; apunta a P01, P02 y P09.', '1 semestre'],
 ['R4', '**Acompañamiento focalizado al 21 % en semáforo rojo.**', 'Prevención temprana del shock de transición.', 'Antes de la práctica'],
 ['R5', '**Taller de comunicación y presentación profesional** (oratoria, explicar lo técnico, pedir ayuda).', 'P04 = 68 %; 22 menciones en comentarios.', '1 semestre'],
 ['R6', '**Reforzar inglés y herramientas reales** (ERP, Excel avanzado, Power BI) en carreras que lo requieren.', '20 y 19 menciones respectivamente.', '2 semestres'],
 ['R7', '**Atención especial al tramo 3.º–4.º semestre.**', 'Es el tramo con puntajes más bajos.', '1–2 semestres'],
 ['R8', '**Validar la codificación de respuestas abiertas** con doble lectura humana y publicar el libro de códigos.', 'Rigor y transparencia.', '1 mes']], [1.0, 8.0, 4.7, 2.9], size=9, align=['c', 'l', 'l', 'l'])

# anexos
D.h1('Anexos')
D.h2('Anexo 1. Ficha técnica')
D.table(['Elemento', 'Detalle'], [
 ['Población y muestra', f"Estudiantes de Duoc UC Sede San Bernardo; {N} respuestas válidas (muestra voluntaria)."],
 ['Fecha de aplicación', '13 al 16 de octubre de 2026 (Google Forms).'],
 ['Instrumento', '15 afirmaciones tipo Likert (1–5, más «No sé/No aplica»), 3 preguntas de caracterización y 2 abiertas.'],
 ['Escuelas', 'Administración y Negocios 181 · Ingeniería y Recursos Naturales 2 · Otra área 1.'],
 ['Tratamiento de «No sé / No aplica»', 'Excluido del cálculo (no se imputó).'],
 ['Puntajes', 'Promedios por ítem; dimensión = promedio de sus ítems disponibles; global = promedio de los 15 ítems.'],
 ['Intervalos de confianza', 'Bootstrap percentil (4.000 remuestreos).'],
 ['Fiabilidad', f"Alfa de Cronbach global = {n(g['alpha'])}; D1 {n(DM['D1']['alpha'])}, D2 {n(DM['D2']['alpha'])}, D3 {n(DM['D3']['alpha'])}, D4 {n(DM['D4']['alpha'])}, D5 {n(DM['D5']['alpha'])}."],
 ['Software', 'Python (pandas, SciPy, statsmodels, matplotlib). Código en la carpeta src del repositorio.'],
 ['Privacidad', 'No se incluyen correos, nombres ni códigos. La base original no se versiona.']], [4.2, 12.4], size=9)
D.h2('Anexo 2. Verificación de robustez')
sens = R['sens']
D.p('Se repitió la comparación «con vs. sin práctica previa» (puntaje global) en distintos subconjuntos, para ver si el resultado depende de quiénes se incluyen:')
D.table(['Subconjunto', 'n', 'Diferencia (con – sin)', 'Valor p (U de Mann-Whitney)'], [[k, v['n'], '+' + n(v['dif']), n(v['p_mw'], 3)] for k, v in sens.items()], [7.4, 1.6, 3.6, 4], size=9, align=['l', 'c', 'c', 'c'])
D.p('La diferencia se mantiene entre +0,17 y +0,21 puntos al excluir respuestas idénticas o la escuela minoritaria. Dentro del primer año (donde práctica y año no se mezclan) cae a +0,07, lo que sugiere que parte de la diferencia refleja el avance en la carrera.', 9.5)
declaracion_ia(D, 'apoyar el diseño de las visualizaciones y la redacción en lenguaje claro, adaptando los hallazgos a públicos no especializados')
bibliografia(D, [0, 1, 5, 6, 7, 9, 11, 13, 14, 15, 16, 18, 19, 20])
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/A_Informe_Descriptivo.docx'); print('A ok')
