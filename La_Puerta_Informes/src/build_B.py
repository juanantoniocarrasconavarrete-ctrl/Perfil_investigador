from comun import *
D = Doc('Informe con hipótesis', 'Qué respaldan —y qué no— los datos de la encuesta frente a las hipótesis del Proyecto La Puerta', 'PRODUCTO B · ANÁLISIS CON CONTRASTE DE HIPÓTESIS', G + 'portada_puerta.png', 'Proyecto La Puerta · Informe B · Análisis con hipótesis')
g = R['global']; O = OF; fo = {r['var']: r for r in O['filas']}; h3 = R['H3']; h4 = R['H4']; h5 = R['H5']; ols = R['ols_global']; sens = R['sens']

intro(D, 'El contraste de las hipótesis del Proyecto La Puerta con los datos de la encuesta de percepción y competencias (n = 184), con foco en el rol de la práctica previa.',
 'El Informe Metodológico del proyecto postula que la práctica previa amortigua el shock de transición al mundo laboral. Este informe pone a prueba esa hipótesis central con los umbrales definidos por el propio proyecto y agrega cuatro hipótesis exploratorias.',
 'Contrastar la hipótesis central del proyecto y cuatro hipótesis complementarias con los datos de la encuesta, e interpretar los resultados en términos prácticos.',
 ['Formular las hipótesis y sus reglas de decisión antes de mirar los resultados.', 'Contrastar cada hipótesis con pruebas apropiadas a datos ordinales, con corrección por comparaciones múltiples.', 'Determinar si los datos permiten evaluar el efecto del programa (antes/después).', 'Derivar recomendaciones coherentes con la evidencia.'],
 'El documento se organiza en cinco partes: la Introducción (resumen ejecutivo y advertencia sobre los datos); el Desarrollo (formulación de hipótesis, metodología, contraste e interpretación y hallazgos); la Conclusión (conclusiones, limitaciones y recomendaciones); las Referencias; y los Anexos (resultados completos, robustez y declaración de uso de IA).')
D.h1('Resumen ejecutivo')
D.p(f"Este informe pone a prueba las hipótesis del Proyecto La Puerta con las respuestas de **{N} estudiantes**. La hipótesis central —tomada del *Informe Metodológico* del proyecto— dice que **haber vivido antes una práctica laboral amortigua el «shock de transición» y fortalece la autoeficacia**, reduciendo las brechas en comunicación, adaptabilidad y autonomía. A esa hipótesis se suman cuatro hipótesis complementarias formuladas por el equipo analista y una sexta (efecto del programa antes/después) que **no se puede evaluar** con estos datos.")
D.fig('g15_hipotesis', 'Figura 1. Tablero de resultados: cuánto respaldan los datos cada hipótesis.')
D.h3('Lo esencial, en cuatro ideas')
D.numbered([
 f"**La práctica previa ayuda, pero mucho menos de lo que el proyecto proyectó.** Quienes ya practicaron puntúan {n(fo['GLOBAL']['dif'])} puntos más (3,97 vs. 3,80). El informe metodológico anticipaba una brecha de 0,8 a 1,2 puntos y una correlación de al menos 0,45; observamos r = {n(O['pearson']['r'])}. La **dirección** es la esperada; la **magnitud** no.",
 f"**El punto débil es la red de contactos, para todos.** Es la dimensión más baja y la afirmación P12 está claramente por debajo de las otras 14, tengan o no práctica previa (hipótesis 3, respaldada).",
 f"**Conocer y probar el trabajo real se asocia con sentirse seguro de adaptarse.** Las afirmaciones sobre conocer el rol, aplicar lo aprendido y haber contrastado el trabajo explican cerca de la mitad de la variación en la seguridad percibida (hipótesis 4, respaldada).",
 f"**Hay una demanda clara y homogénea:** {pc(h5['fav'])} quiere participar en proyectos con empresas reales antes de la práctica (hipótesis 5, respaldada)."])
D.callout('Veredicto sobre la hipótesis central', [f"**Parcialmente respaldada: sí en dirección, no en magnitud.** La cohorte cae en el tramo del «Escenario 2 – hallazgos mixtos» por su promedio ({n(O['media_global'])}), pero **sin** la brecha por experiencia previa que define a ese escenario. Con la muestra actual podemos descartar que la diferencia sea de 0,8 puntos o más; no podemos descartar una diferencia pequeña (entre 0 y 0,36 puntos)."], AMB, 'FFF7E0')
aviso_datos(D)

D.part('DESARROLLO')
D.h1('2. Formulación de hipótesis')
D.h2('2.1 De dónde salen las hipótesis')
D.p('El *Informe Metodológico y Análisis Prospectivo de Brechas* del Proyecto La Puerta plantea una premisa: el aprendizaje del currículo es necesario pero **insuficiente** para una transición exitosa; la variable que modula el desempeño es la **trayectoria de práctica previa**. Textualmente, se postula que «la vivencia previa de inmersión laboral actúa como un factor amortiguador del shock de transición, consolidando la autoeficacia ocupacional del estudiante y reduciendo significativamente las brechas conductuales en comunicación, adaptabilidad y autonomía». Esto se apoya en la teoría de la autoeficacia (Bandura, 1997): la experiencia directa de logro es la fuente más fuerte de confianza.')
D.p('El mismo informe propone **tres escenarios** para interpretar los resultados y un **semáforo** de puntajes. Los usamos como reglas de decisión, porque fueron definidos por el equipo del proyecto antes de ver estos datos:')
D.table(['Escenario', 'Criterios del Informe Metodológico', 'Lectura propuesta'], [
 ['1 · Hipótesis confirmada', 'Promedio ≥ 4,20 · correlación práctica previa–índice global r ≥ 0,45 (p < 0,01) · +25 % a +35 % en autonomía y comunicación para quienes tienen práctica previa', 'Brechas bajas, alta madurez laboral'],
 ['2 · Hallazgos mixtos', 'Promedio 3,50–4,10 · brecha de 0,8 a 1,2 puntos entre con y sin práctica previa (p < 0,001; ej. 4,3 vs. 3,3)', 'La falta de práctica previa es un factor de inequidad'],
 ['3 · Alerta temprana', 'Promedio < 3,50 · más de 40 % de la cohorte bajo 3,50 en autonomía y resiliencia', 'Fragilidad conductual generalizada']], [3.6, 9.2, 3.8], size=9, colors={(0, 0): TEAL, (1, 0): AMB, (2, 0): CORAL})
D.h2('2.2 Las hipótesis que se contrastan')
D.p('Ordenadas por importancia. **H1** viene del Informe Metodológico; **H2 a H5** las formuló el equipo analista a partir del mismo instrumento y de lo observado en la descripción (por eso se declaran como exploratorias, **[HIPÓTESIS]**); **H6** se incluye porque es la pregunta de fondo del proyecto, aunque hoy no se pueda responder.')
D.table(['Código', 'Hipótesis (en simple)', 'Variables', 'Se considera respaldada si…'], [
 ['H1\n(central)', '**La práctica previa amortigua la transición:** quienes ya practicaron se sienten más preparados y con menos brechas.', 'Práctica previa (ID07, con/sin) · índice global y dimensiones · semáforo oficial', 'r ≥ 0,45 y brecha ≥ 0,8 puntos (criterios del informe). «Parcial» si la dirección coincide pero la magnitud es menor.'],
 ['H2', '**A más avance en la carrera, mayor percepción de preparación.**', 'Año de estudio (1.º–2.º / 3.º–4.º / 5.º o más) · dimensiones', 'Diferencia entre años con p ajustado < 0,05 y tendencia creciente.'],
 ['H3', '**La red de contactos es el punto más débil** (dimensión D4 y afirmación P12).', 'D1 a D5 · P12 contra las otras 14 afirmaciones', 'D4 y P12 significativamente menores que el resto (p ajustado < 0,05).'],
 ['H4', '**Conocer y probar el trabajo real se asocia con sentirse más seguro de adaptarse.**', 'P01, P05, P09, P12 → P10 (seguridad de adaptarse)', 'Asociación positiva moderada o mayor (rho ≥ 0,30) que se mantiene al controlar por las otras variables.'],
 ['H5', '**Hay una alta demanda de proyectos con empresas reales** (P15).', 'P15 · práctica previa · año', 'Más de 70 % de acuerdo (p < 0,05 frente a 70 %).'],
 ['H6', '**La participación en La Puerta mejora los resultados entre el antes y el después, frente a un grupo de comparación.**', 'Código, momento (pre/post), grupo (piloto/control)', 'Requiere los tres campos. **Hoy no evaluable.**']], [1.7, 5.6, 4.4, 4.9], size=8.8, colors={(0, 0): AMB, (5, 0): GRAY})
D.callout('Un aviso sobre el instrumento', 'El Informe Metodológico describe seis dimensiones (práctica previa A02–A04 y cinco de habilidades blandas: COM, EQ, AUT, RES, ET). La encuesta aplicada mide **15 afirmaciones en cinco dimensiones distintas (D1–D5)** y no incluye las preguntas A03 (impacto percibido de la práctica previa) ni A04 (valoración formativa de la experiencia). Para contrastar H1 se construyó una **equivalencia** entre ambos instrumentos [INTERPRETACIÓN]: Comunicación ≈ P04 y P11; Trabajo en equipo ≈ P07; Autonomía ≈ P03 y P08; Resiliencia ≈ P13; Ética ≈ P14. Es una aproximación razonable, no una medición idéntica.', SKY, 'EEF4FB')

D.h1('3. Metodología de análisis')
D.p('Pensamos esta sección como si tuviéramos que explicársela a un colega que no es estadístico. Para cada pregunta hay una herramienta; estas son las que usamos y por qué.')
D.table(['Pregunta', 'Herramienta', 'Por qué esta y no otra'], [
 ['¿Dos grupos (con/sin práctica) puntúan distinto?', 'Prueba t de Welch (la del informe metodológico, sin suponer varianzas iguales) y, como control, U de Mann-Whitney', 'La escala es de opinión (ordinal); si ambas pruebas coinciden, la conclusión es más confiable (Norman, 2010; Mann y Whitney, 1947).'],
 ['¿Qué tan grande es la diferencia?', 'Diferencia de promedios con intervalo de confianza; d de Cohen; probabilidad de superioridad', 'Un valor p solo dice si algo es «raro»; el tamaño dice si **importa** (Cohen, 1988; Vargha y Delaney, 2000).'],
 ['¿Hay una relación entre dos afirmaciones?', 'Correlación de Spearman (rho)', 'Trabaja con rangos; no exige escala perfecta.'],
 ['¿Cambian los resultados entre tres años de estudio?', 'Prueba de Kruskal-Wallis y correlación de Spearman', 'Alternativa a ANOVA para datos ordinales (Kruskal y Wallis, 1952).'],
 ['¿Una dimensión es más baja que otras en las mismas personas?', 'Prueba de Friedman y comparaciones de Wilcoxon por pares', 'Compara medidas repetidas en las mismas personas.'],
 ['¿Qué pesa más para explicar la seguridad de adaptarse?', 'Regresión lineal con errores robustos (HC3)', 'Permite ver el aporte de cada variable manteniendo las demás constantes.'],
 ['¿Es mayor al 70 %?', 'Prueba binomial exacta e intervalo de Wilson', 'Apropiada para porcentajes.']], [4.4, 5.6, 6.6], size=8.8)
D.h3('Reglas para no engañarnos')
D.bullets(['**Varias pruebas a la vez aumentan el riesgo de «falsos hallazgos».** Por eso, cuando se hacen varias comparaciones en una misma familia, se aplica la corrección de Holm (1979) y se informan ambos valores p (sin y con corrección).', '**Nivel de significación:** 0,05, bilateral (puede haber diferencias en ambas direcciones).', '**Tamaño mínimo detectable:** con 72 estudiantes con práctica y 112 sin práctica, y una desviación típica de 0,67, la menor diferencia que esta muestra detecta de manera confiable (80 % de poder) es de unos **' + n(O['mde_80']) + ' puntos** (Cohen, 1988). Diferencias menores pueden existir pero quedarían «invisibles».', '**Robustez:** se repitió la comparación principal sin las respuestas idénticas, sin otras escuelas y solo en primer año (Anexo 2).', '**Correlación no es causalidad.** Todos los datos son autopercepciones de una sola medición (Podsakoff et al., 2003); cuando se dice «se asocia», no se dice «causa».'])

D.h1('4. Contraste e interpretación de las hipótesis')
D.h2('4.1 H1 (central): la práctica previa amortigua la transición')
D.h3('Qué esperaba el proyecto y qué muestran los datos')
D.fig('g21_criterios', 'Figura 2. Criterios del Informe Metodológico frente a lo observado.')
D.p(f"**1) Nivel de la cohorte.** El promedio es {n(O['media_global'])}: por nivel cae en el Escenario 2 (3,50–4,10), no en el 1 (≥ 4,20) ni en el 3 (< 3,50).")
D.p(f"**2) Correlación.** La relación entre tener práctica previa y el índice global es r = {n(O['pearson']['r'])} (intervalo de confianza 95 %: {n(O['pearson']['ci'][0])} a {n(O['pearson']['ci'][1])}; {pv(O['pearson']['p'])}). Es una relación **débil**, muy lejos del 0,45 anticipado. En términos cotidianos: saber si alguien ya hizo una práctica ayuda muy poco a adivinar cuánto puntúa.")
D.p(f"**3) Brecha entre grupos.** Quienes tienen práctica previa obtienen **{n(fo['GLOBAL']['con'])}** y quienes no **{n(fo['GLOBAL']['sin'])}**: una diferencia de **+{n(fo['GLOBAL']['dif'])}** puntos (intervalo 95 %: {n(fo['GLOBAL']['ci'][0])} a {n(fo['GLOBAL']['ci'][1])}). La prueba t da {pv(fo['GLOBAL']['p_t'])} y la de Mann-Whitney {pv(fo['GLOBAL']['p_mw'])}; con la corrección por comparaciones múltiples, ninguna resiste (Holm ≥ 0,25). El tamaño del efecto es **pequeño** (d = {n(fo['GLOBAL']['d'])}). El proyecto esperaba 0,8 a 1,2 puntos: **los datos descartan una brecha de esa magnitud**.")
D.fig('g06_practica', 'Figura 3. Con y sin práctica previa, por dimensión.')
D.lee('Cada fila compara dos puntos: el amarillo (sin práctica) y el negro (con práctica). Cuanto más separados, mayor la diferencia. A la derecha: cuánto es y su valor p sin corregir. Las diferencias más visibles son en D1 y D3.')
D.h3('Equivalencia con las dimensiones del Informe Metodológico')
rows = []; cols = {}
for i, v in enumerate(['O_COM', 'O_EQ', 'O_AUT', 'O_RES', 'O_ET', 'O_HB']):
    r = fo[v]; rows.append([O['equiv'][v], n(r['con']), n(r['sin']), ('+' if r['dif'] >= 0 else '') + n(r['dif']), pc(r['pct'], 1), n(r['d']), n(r['p_t'], 2), n(r['p_holm'], 2)])
D.table(['Dimensión (equivalencia)', 'Con práctica', 'Sin práctica', 'Diferencia', 'Diferencia %', 'd de Cohen', 'p (Welch)', 'p ajustado'], rows, [4.6, 1.8, 1.8, 1.7, 1.8, 1.6, 1.6, 1.7], size=8.5, align=['l'] + ['c'] * 7)
D.p(f"El informe proyectaba aumentos de **25 % a 35 %** en autonomía y comunicación. Observamos **+{n(fo['O_AUT']['pct'],1)} %** en autonomía y **+{n(fo['O_COM']['pct'],1)} %** en comunicación. Ninguna diferencia es estadísticamente clara; la más grande (autonomía, +{n(fo['O_AUT']['dif'])}) es compatible con un efecto real pequeño. En trabajo en equipo y resiliencia, las diferencias son prácticamente nulas ({n(fo['O_EQ']['dif'])} y +{n(fo['O_RES']['dif'])}): **el «amortiguador» no aparece donde se esperaba con más fuerza.**")
D.h3('Semáforo oficial: ¿hay menos estudiantes en rojo con práctica previa?')
D.fig('g22_semaforo_oficial', 'Figura 4. Semáforo oficial por estudiante, con y sin práctica previa.')
S = O['semaforo_estudiantes']
D.p(f"Con práctica previa, **{pc(100*S['con']['Rojo']/sum(S['con'].values()))}** está en rojo (menos de 3,50) frente a **{pc(100*S['sin']['Rojo']/sum(S['sin'].values()))}** sin práctica; y {pc(100*S['con']['Verde']/sum(S['con'].values()))} está en verde frente a {pc(100*S['sin']['Verde']/sum(S['sin'].values()))}. El sentido es el esperado, pero no alcanza significación (rojos: {pv(O['rojo_fisher']['p'])}; verdes: {pv(O['verde_fisher']['p'])}). Un dato importante para decidir: de los **38 estudiantes en rojo**, {S['sin']['Rojo']} no tienen práctica previa y {S['con']['Rojo']} sí. **Tener práctica previa no «vacuna»:** 1 de cada 7 estudiantes con práctica igual queda en rojo.")
D.h3('Tipo de práctica y año de estudio')
t = R['por_practica_tipo']
D.p(f"Por tipo de práctica, la pasantía en la carrera ({n(t['Pasantía en la carrera']['GLOBAL'])}) y la práctica EMTP ({n(t['Práctica EMTP']['GLOBAL'])}) puntúan algo sobre quienes no han practicado ({n(t['Sin práctica previa']['GLOBAL'])}), sin diferencias claras entre los tres grupos (Kruskal-Wallis, {pv(O['tipos_kw']['p'])}). Además, práctica previa y año de estudio están entrelazados (63 % de quienes llevan 5.º semestre o más tienen práctica; solo 33 % en 1.º–2.º). Al analizarlos **a la vez**, la práctica previa suma +{n(ols['con_practica']['b'])} puntos (intervalo {n(ols['con_practica']['ci'][0])} a {n(ols['con_practica']['ci'][1])}; {pv(ols['con_practica']['p'])}) y el año de estudio +{n(ols['anio_c']['b'])} por tramo ({pv(ols['anio_c']['p'])}); juntos explican apenas el {pc(100*ols['r2'],1)} de las diferencias entre estudiantes. Dentro del primer año, donde ambos no se mezclan, la diferencia cae a +{n(sens['Solo 1.º–2.º semestre']['dif'])}.")
D.h3('Interpretación práctica de H1')
D.bullets([
 f"**{tag('H')} La práctica previa se asocia con puntajes algo más altos** en cuatro de cinco dimensiones; el efecto es pequeño (d ≈ 0,2–0,3) y no es estadísticamente concluyente con esta muestra (que solo detecta diferencias de 0,28 o más).",
 f"**{tag('H')} El Escenario 2 no se cumple en su rasgo central:** no hay una brecha de 0,8–1,2 puntos. La cohorte es «mixta» por su nivel (3,87), pero **no polarizada por experiencia previa**.",
 f"**{tag('I')} Por qué la brecha puede ser menor a la proyectada:** (a) las cifras del informe (4,3 vs. 3,3) eran proyecciones ilustrativas, no estimaciones empíricas; (b) las prácticas previas son muy distintas entre sí (EMTP, pasantías, otra carrera) y pueden ser de hace años; (c) con autopercepciones tiende a haber «techo»: casi todos se evalúan bien; (d) quienes no tienen práctica quizá se evalúan con optimismo por no conocer aún las exigencias; (e) la encuesta no mide A03 ni A04, que son el corazón del mecanismo propuesto.",
 f"**{tag('B')} Brecha:** falta medir el desempeño observado en el centro de práctica (evaluación de jefaturas) para saber si la práctica previa se traduce en mejor desempeño real y no solo en mejor autopercepción."])
D.callout('Veredicto H1', 'PARCIALMENTE RESPALDADA. Dirección coherente con la hipótesis; magnitud muy inferior a la proyectada y no concluyente estadísticamente. La evidencia **no justifica** una política que segregue por tener o no práctica previa; sí justifica atender al grupo en semáforo rojo, con y sin práctica previa.', AMB, 'FFF7E0')

D.h2('4.2 H2: a más semestres, mayor percepción de preparación')
D.fig('g07_anio', 'Figura 5. Dimensiones según año de estudio.')
rows = []
for v in ['GLOBAL', 'D1', 'D2', 'D3', 'D4', 'D5']:
    r = H2[v]; rows.append([r['nombre'], n(r['medias'][0]), n(r['medias'][1]), n(r['medias'][2]), n(r['p'], 3), n(r['p_holm'], 2), n(r['rho'])])
D.table(['Dimensión', '1.º–2.º sem.\n(n=90)', '3.º–4.º sem.\n(n=43)', '5.º o más\n(n=51)', 'p (Kruskal)', 'p ajustado', 'rho'], rows, [4.8, 2.0, 2.0, 2.0, 2.0, 1.9, 1.9], size=8.8, align=['l'] + ['c'] * 6)
D.p(f"Ninguna diferencia resiste la corrección (p ajustado ≥ 0,49). No hay «escalera»: el tramo 3.º–4.º semestre es el más bajo en casi todo, y el de 5.º en adelante repunta (D1: {n(H2['D1']['medias'][2])}; D5: {n(H2['D5']['medias'][2])}). La correlación entre año y puntaje global es prácticamente cero (rho = {n(H2['GLOBAL']['rho'])}). Exploratoriamente, **la prioridad por la ética bajo presión (P14) sube con el año** (rho = {n(R['H2_items'][13]['rho'])}, {pv(R['H2_items'][13]['p'])} sin corregir; no resiste Holm, p ajustado = {n(R['H2_items'][13]['p_holm'],2)}).")
D.callout('Veredicto H2', f"NO RESPALDADA. Avanzar de semestre, por sí solo, no mejora la percepción de preparación. {tag('I')} Una lectura plausible es la de un «valle» a mitad de carrera: ya pasó la novedad del primer año y aún no llega el contacto con la práctica real. Es una hipótesis para una próxima medición.", CORAL, 'FDEEE9')

D.h2('4.3 H3: la red de contactos es el punto más débil')
D.fig('g12_cajas', 'Figura 6. Distribución de los puntajes por dimensión: D4 se ubica más abajo.')
pares = {p['vs']: p for p in h3['pares']}
D.p(f"La prueba de Friedman confirma que las cinco dimensiones **no son iguales** (chi² = {n(h3['chi2'],1)}, {pv(h3['p'])}; n = {h3['n']}). Al comparar D4 con cada una de las otras: queda **{n(-pares['D2']['dif_media'])} puntos bajo D2**, **{n(-pares['D3']['dif_media'])} bajo D3** y **{n(-pares['D5']['dif_media'])} bajo D5** (todas con p ajustado < 0,001), y {n(-pares['D1']['dif_media'])} bajo D1 (diferencia no concluyente, p ajustado = {n(pares['D1']['p_holm'],3)}). El efecto global de la dimensión es pequeño (W de Kendall = {n(h3['W'],3)}) porque D4 también contiene el interés en proyectos (P15), que es alto y «sube» su promedio.")
D.p(f"El hallazgo se vuelve contundente cuando se mira la **afirmación P12** (tener una red de contactos): promedio **{n(IT['P12']['media'])}**, y es significativamente menor que cada una de las otras 14 afirmaciones (diferencias de {n(-max(r_['dif'] for r_ in h3['P12_vs']))} a {n(-min(r_['dif'] for r_ in h3['P12_vs']))} puntos; todas con p ajustado < 0,001). Si se toman solo las dos afirmaciones de contactos (P11 y P12), el promedio es {n(h3['D4_redes_media'])}, bajo todas las demás dimensiones (p < 0,001).")
D.fig('g16_redes', 'Figura 7. Interés alto, red baja.')
D.callout('Veredicto H3', f'RESPALDADA (fuerte para P12 y la red de contactos; moderada para la dimensión D4 completa). La red de contactos es la brecha mayor y es transversal: no depende de tener o no práctica previa (P12 promedia {n(R['heat_pract']['P12'][1])} con práctica y {n(R['heat_pract']['P12'][0])} sin práctica, ambos por debajo del resto de las afirmaciones). En línea con Granovetter (1973), los vínculos con personas fuera del círculo cercano son un recurso que hoy los estudiantes no tienen.', TEAL)

D.h2('4.4 H4: conocer y probar el trabajo real se asocia con más seguridad')
D.fig('g09_p09_p10', 'Figura 8. Haber comprobado si el trabajo calza (P09) y seguridad de adaptarse (P10).', 11)
D.p(f"La seguridad de adaptarse a un puesto (P10) se asocia de forma **moderada a fuerte** con conocer las tareas reales (P01: rho = {n(h4['P01_P10']['rho'])}), las exigencias de las empresas (P02: {n(h4['P02_P10']['rho'])}), haber contrastado el trabajo con los propios intereses (P09: {n(h4['P09_P10']['rho'])}), aplicar lo aprendido (P05: {n(h4['P05_P10']['rho'])}), confiar ante lo nuevo (P03: {n(h4['P03_P10']['rho'])}) y tener una red de contactos (P12: {n(h4['P12_P10']['rho'])}). Todas con {pv(0.0001)}.")
D.fig('g13_h4', 'Figura 9. Aporte de cada factor a la seguridad de adaptarse (manteniendo constantes los demás).', 13)
o4 = h4['ols']
D.p(f"Al analizar los factores **a la vez** (regresión, n = {o4['n']}), el modelo explica el **{pc(100*o4['r2'])}** de las diferencias en seguridad. Aportan por sí solos: aplicar lo aprendido (P05; {pv(o4['P05']['p'])}), conocer las tareas reales (P01; {pv(o4['P01']['p'])}) y haber comprobado si el trabajo calza (P09; {pv(o4['P09']['p'])}). La red de contactos (P12) queda en el límite ({pv(o4['P12']['p'])}). **Ni la práctica previa ni el año de estudio aportan una vez controlado lo anterior** ({pv(o4['con_practica']['p'])} y {pv(o4['anio_c']['p'])}).")
D.callout('Veredicto H4', f"RESPALDADA (como asociación). {tag('I')} Un hallazgo valioso para el diseño: lo que parece importar no es «haber tenido una práctica», sino **qué se aprendió en ella** (conocer tareas y exigencias, contrastar con los intereses). Esto sugiere que actividades breves y bien diseñadas de contacto con el trabajo real podrían producir parte del efecto sin esperar una práctica completa. Esto es una **hipótesis a probar**, no una conclusión: los datos no permiten afirmar causalidad y las respuestas provienen todas de la misma persona (Podsakoff et al., 2003).", TEAL)

D.h2('4.5 H5: alta demanda de proyectos con empresas reales')
D.p(f"{h5['k']} de {h5['n']} estudiantes ({pc(h5['fav'],1)}; intervalo 95 %: {pc(100*h5['ci_wilson'][0])} a {pc(100*h5['ci_wilson'][1])}) están de acuerdo con participar en proyectos o consultorías con empresas reales antes de su práctica. Es significativamente mayor al umbral de 70 % ({pv(h5['p_vs70'])}). Es una demanda **homogénea**: 83 % tanto con como sin práctica previa, y entre 71 % y 92 % según el año (sin diferencias claras; {pv(h5['anio']['p'])}). Además, el interés es mayor entre quienes ya contrastaron el trabajo real con sus intereses (P09 alto: {pc(h5['P15_por_P09']['fav_alto'])} vs. P09 bajo: {pc(h5['P15_por_P09']['fav_bajo'])}; rho = {n(h5['P15_P09']['rho'])}): **quien prueba, quiere más.**")
D.callout('Veredicto H5', 'RESPALDADA. Existe una base amplia y transversal de interés para iniciativas tipo La Puerta, incluso entre quienes aún no han tenido contacto con empresas.', TEAL)

D.h2('4.6 H6: efecto de La Puerta (antes/después con grupo de comparación)')
D.fig('g20_diseno_futuro', 'Figura 10. Lo que falta para evaluar el programa.')
D.p('**No evaluable.** Para atribuir cambios al programa se requiere (1) un código único por estudiante que permita emparejar su «antes» y su «después»; (2) el momento de medición; (3) la asignación a grupo (La Puerta/comparación); y (4) la valoración del programa (POST_EXP1). Las cuatro columnas están vacías. Es la brecha más importante del proyecto y, a la vez, la más fácil de corregir antes de la próxima aplicación. La hoja «Matriz_Análisis» contiene solo una fila de demostración (LP-DEMO-01) que **no se usó** en este análisis.')
D.callout('Veredicto H6', 'NO EVALUABLE con esta base. Ver R1.', GRAY, 'F0F3F8')

D.h1('5. Hallazgos principales')
F = [('1', 'La práctica previa se asocia con puntajes algo más altos (+0,17), pero muy por debajo de la brecha proyectada (0,8–1,2) y sin concluir estadísticamente. H1: parcial.', 'H'),
 ('2', 'El Escenario 2 (mixto) describe el nivel de la cohorte, pero no su rasgo central: no hay inequidad marcada por experiencia previa.', 'I'),
 ('3', '38 estudiantes (21 %) están en rojo; 28 no tienen práctica previa y 10 sí.', 'H'),
 ('4', 'La red de contactos es el punto más débil, en todos los perfiles. H3: respaldada.', 'H'),
 ('5', 'Conocer tareas y exigencias, aplicar lo aprendido y contrastar el trabajo real se asocian con más seguridad de adaptarse; la práctica previa deja de importar al controlarlos. H4: respaldada.', 'I'),
 ('6', 'El 83 % quiere proyectos con empresas reales, sin distinción por perfil. H5: respaldada.', 'H'),
 ('7', 'El año de estudio no ordena los puntajes; hay un valle en 3.º–4.º semestre. H2: no respaldada.', 'H'),
 ('8', 'El efecto de La Puerta no se puede evaluar: faltan código, momento, grupo y valoración del programa; tampoco se aplicaron A03 y A04. H6: no evaluable.', 'B')]
D.table(['N.º', 'Hallazgo', 'Estatus'], [[a, b, tag(c)] for a, b, c in F], [1.0, 11.8, 3.8], colors={(i, 2): {'H': TEAL, 'I': SKY, 'B': CORAL}[c] for i, (a, b, c) in enumerate(F)}, size=9.5, align=['c', 'l', 'c'])

D.part('CONCLUSIÓN')
D.h1('6. Conclusiones')
D.numbered(['**La hipótesis central del proyecto se sostiene en dirección, pero no en tamaño.** La práctica previa no es el gran divisor que se proyectaba. Hoy no hay evidencia para tratar a los estudiantes sin práctica previa como un grupo de riesgo por esa sola condición.', '**Lo que sí distingue a los estudiantes más seguros es el contacto con el trabajo real**: saber qué se hace, qué se exige y si el trabajo calza con uno. Eso se puede intervenir sin esperar una práctica completa.', '**La red de contactos es la carencia más clara y más intervenible.**', '**El interés en vincularse con empresas es alto y parejo**, lo que da legitimidad y demanda a La Puerta.', '**La evaluación del programa sigue pendiente**; el principal obstáculo es de diseño de datos, no de análisis.'])
D.h2('Limitaciones')
D.bullets(['Datos transversales y autopercibidos; no se puede establecer causalidad.', f"Poder estadístico acotado: solo detecta diferencias de {n(O['mde_80'])} puntos o más; diferencias menores no se pueden descartar.", 'Las hipótesis H2–H5 son exploratorias (formuladas tras una primera mirada descriptiva); sus resultados deben replicarse con otra cohorte antes de tomar decisiones de alto costo.', 'La equivalencia entre el instrumento del informe metodológico y el aplicado es aproximada.', 'La práctica previa se autoinforma y agrupa experiencias muy distintas; no se conoce su duración ni calidad.'])

D.h1('7. Recomendaciones de mejora')
D.table(['Cód.', 'Recomendación', 'Hipótesis que la sustenta'], [
 ['R1', '**Rediseñar la medición para poder evaluar La Puerta:** código único, momento y grupo obligatorios; incluir A03 y A04; considerar la evaluación de la jefatura en práctica. Realizar un piloto con grupo de comparación y pretest/postest.', 'H6 · limitaciones de H1'],
 ['R2', '**Programa de redes:** mentorías con egresados y practicantes, ferias y charlas con empresas, «café con profesionales».', 'H3'],
 ['R3', '**Microexperiencias de contacto real** (visitas, proyectos cortos con empresas, shadowing de 1–2 jornadas) para todos los años; es la palanca que H4 sugiere y que H5 muestra que los estudiantes quieren.', 'H4 · H5'],
 ['R4', '**Ajustar el criterio de focalización:** en vez de «sin práctica previa», usar el semáforo (rojo < 3,50) y la combinación de brechas (P01, P02, P09, P12).', 'H1 (brecha pequeña); 21 % en rojo'],
 ['R7', '**Atender el tramo 3.º–4.º semestre** con actividades que reconecten con el mundo laboral.', 'H2 (valle)']], [1.0, 10.8, 4.8], size=9, align=['c', 'l', 'l'])
bibliografia(D, [0, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 17, 19, 20, 2, 11])
D.part('ANEXOS')
D.h2('Anexo 1. Resultados completos de H1 por dimensión')
rows = []
for r in R['H1']:
    rows.append([r['nombre'], n(r['media_con']), n(r['media_sin']), '+' + n(r['dif']), f"{n(r['dif_ci'][0])} a {n(r['dif_ci'][1])}", n(r['p'], 3), n(r['p_holm'], 2), n(r['cliff'])])
D.table(['Dimensión', 'Con', 'Sin', 'Diferencia', 'IC 95 %', 'p (MW)', 'p Holm', 'Cliff δ'], rows, [4.8, 1.5, 1.5, 1.9, 2.8, 1.6, 1.5, 1.4], size=8.8, align=['l'] + ['c'] * 7)
D.p('IC = intervalo de confianza (bootstrap). MW = U de Mann-Whitney. Cliff δ = diferencia de dominancia (de −1 a +1; 0 = sin diferencia; Cliff, 1993). Holm corrige por las seis comparaciones.', 9, GRAY)
D.h2('Anexo 2. Verificación de robustez (puntaje global, con vs. sin práctica)')
D.table(['Subconjunto', 'n', 'Diferencia', 'p (MW)'], [[k, v['n'], '+' + n(v['dif']), n(v['p_mw'], 3)] for k, v in sens.items()], [8, 2, 3.2, 3.4], size=9, align=['l', 'c', 'c', 'c'])
D.p('Sin las 12 respuestas «idénticas en todo», la diferencia sube a +0,21 (p = 0,011 sin corregir) y sigue lejos de 0,8. Dentro de primer año baja a +0,07. Ninguna variante se acerca a la brecha proyectada.', 9.5)
D.h2('Anexo 3. Código y reproducibilidad')
D.p('Todo el análisis puede reproducirse con `src/analisis.py` (Python: pandas, SciPy, statsmodels) y `src/graficos.py`. La semilla aleatoria es fija (2026). La base original no se incluye en el repositorio por contener correos.')
declaracion_ia(D, 'proponer el marco de contraste, calcular las pruebas estadísticas y redactar la interpretación de las hipótesis')
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/B_Informe_Hipotesis.docx'); print('B ok')
