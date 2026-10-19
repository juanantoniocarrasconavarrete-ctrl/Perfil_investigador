from comun import *
import json as _j
AUD = _j.load(open('auditoria_datos.json')); nA = len(AUD); okA = sum(a['coincide'] for a in AUD)
D = Doc('Informe de auditoría y verificación', 'Revisión documental de los productos del Proyecto La Puerta: exactitud, coherencia, formato y fuentes', 'PRODUCTO K · AUDITORÍA Y VERIFICACIÓN', None, 'Proyecto La Puerta · Informe de auditoría y verificación')
intro(D, 'La verificación de la exactitud de las cifras, la coherencia entre documentos, el cumplimiento del formato Duoc UC y el estado de las fuentes de los diez productos del Proyecto La Puerta (A, B, C, D, E, F, G, H, I y J).',
 'Los productos se elaboraron en varias etapas y se modificaron después (formato Duoc UC, estudio paralelo, bibliografía y transparencia sobre IA). Antes de difundirlos conviene comprobar que lo que dicen coincide con los datos, que no se contradicen entre sí y que sus fuentes son sólidas.',
 'Verificar la información de los productos, corregir lo que no esté correcto y dejar constancia de lo que sigue pendiente.',
 ['Recalcular las cifras clave con un método independiente y compararlas con las publicadas.', 'Revisar que el texto, las referencias cruzadas y los términos sean coherentes entre productos.', 'Comprobar el cumplimiento del formato y la paleta Duoc UC.', 'Revisar el estado de cada fuente bibliográfica y la transparencia sobre el uso de IA.', 'Listar hallazgos, correcciones y riesgos que persisten.'],
 'El documento se organiza en cinco partes: la Introducción (resultado en una página); el Desarrollo (alcance y método, verificación de cifras, verificación de fuentes, cumplimiento del formato, coherencia entre productos, hallazgos y riesgos residuales); la Conclusión (opinión de auditoría y controles recomendados); las Referencias; y los Anexos (detalle de las verificaciones numéricas y declaración de uso de IA).')
D.h1('Resultado de la auditoría en una página')
D.kpis([(f'{okA}/{nA}', 'cifras recalculadas\nque coinciden', NAVY), ('10', 'hallazgos\nregistrados', NAVY), ('10', 'corregidos\nen esta revisión', NAVY), ('3', 'pendientes\nde confirmar', AMB)])
D.callout('Opinión de auditoría: aprobado con observaciones', ['Las cifras de los productos **coinciden con la base de datos original** (recálculo independiente sin diferencias). Los hallazgos de forma y de redacción detectados se corrigieron y se regeneraron los productos.', 'Quedan **tres pendientes que no se pueden cerrar desde esta revisión**: insertar el logo oficial de Duoc UC, confirmar algunos datos de dos referencias externas y validar con doble lectura humana la clasificación de respuestas abiertas.', '**Límite importante:** esta revisión la hizo la misma herramienta de IA que elaboró los productos. No es una auditoría independiente; se recomienda una revisión humana antes de difundirlos.'])
D.part('DESARROLLO')
D.h1('Alcance y método')
D.table(['Procedimiento', 'Qué se hizo', 'Evidencia'], [
 ['**Recálculo independiente**', 'Se recalcularon 90 cifras (ítems, dimensiones, pruebas, semáforo, calidad de datos) desde la base original con un camino de cálculo distinto del usado para los informes.', 'Script `src/auditoria_datos.py`; resultados en `auditoria_datos.json`'],
 ['**Contraste texto–datos**', 'Las cifras del texto provienen del mismo archivo de resultados; las cifras escritas a mano se revisaron una a una contra los datos.', 'Revisión de los scripts de cada producto'],
 ['**Coherencia entre productos**', 'Se revisaron referencias cruzadas (capítulos, anexos, códigos R1 a R8), términos y cifras repetidas.', 'Búsqueda sistemática en los textos'],
 ['**Formato Duoc UC**', 'Se inspeccionó el archivo de cada documento (tamaño, márgenes, tipografía, interlineado, colores) y su vista en PDF.', 'Verificación del XML y revisión visual'],
 ['**Fuentes**', 'Se comprobó que cada autor citado esté en las referencias y se buscó en línea el registro de las fuentes externas.', 'Búsquedas web del 18 y 19 de octubre de 2026'],
 ['**Transparencia sobre IA**', 'Se comprobó que cada producto tenga declaración de uso de IA y bibliografía.', 'Lectura de cada producto']], [3.4, 8.6, 4.5], size=8.8)
D.p('**Escala de severidad:** *Alta* (cambia una conclusión o una cifra), *Media* (puede inducir a error o afecta la trazabilidad) y *Baja* (forma o redacción).'.replace('*', ''), 10, GRAY)

D.h1('Verificación de cifras')
grupos = [('Tamaño de muestra y consentimiento', lambda s: s['verificacion'] in ('N', 'consentimiento')), ('Ítems P01–P15 (n, promedio, % de acuerdo, % de desacuerdo)', lambda s: s['verificacion'].startswith('P') and ' ' in s['verificacion'] and s['verificacion'][1:3].isdigit()), ('Dimensiones D1–D5 y puntaje global; alfa', lambda s: s['verificacion'].startswith('D') or s['verificacion'].startswith('global') or s['verificacion'].startswith('alfa')),
          ('Comparación con y sin práctica previa (diferencia, pruebas, correlación)', lambda s: any(k in s['verificacion'] for k in ('dif global', 'MW', 'Welch', 'Pearson', 'n con', 'n sin'))), ('Semáforo oficial (verdes, amarillos, rojos)', lambda s: s['verificacion'] in ('verde', 'amarillo', 'rojo', 'rojo sin práctica', 'rojo con práctica')), ('Otras hipótesis (Friedman, correlación P09–P10, P15)', lambda s: any(k in s['verificacion'] for k in ('Friedman', 'rho', 'P15', 'binomial'))), ('Calidad de los datos y respuestas abiertas', lambda s: any(k in s['verificacion'] for k in ('celdas', 'idénticas', 'correos', 'campos', 'abiertas')))]
usadas = set(); rows = []
for nom, f in grupos:
    sel = [s for s in AUD if f(s) and s['verificacion'] not in usadas]; usadas |= {s['verificacion'] for s in sel}
    rows.append([nom, len(sel), 'Coinciden' if all(s['coincide'] for s in sel) else 'Hay diferencias'])
rows.append(['**Total**', sum(r[1] for r in rows), f'{okA} de {nA} coinciden'])
D.table(['Bloque verificado', 'N.º de verificaciones', 'Resultado'], rows, [9.6, 3.4, 3.5], size=9, align=['l', 'c', 'c'])
D.p('Las comparaciones usan una tolerancia de 0,000001 para promedios, porcentajes y valores p (0 para conteos). **No hubo diferencias.** El detalle está en el Anexo A.')
D.callout('Qué no cubre esta verificación', ['Verifica que las cifras publicadas sean las que resultan de la base; **no** valida que la base sea representativa ni que las respuestas sean veraces.', 'Los modelos (regresión, pruebas) usan las mismas librerías en ambos recálculos; una discrepancia conceptual entre pruebas no se detectaría. Por eso se recomienda que una persona con formación estadística revise el Informe B.'])

D.h1('Verificación de fuentes y referencias')
D.p('Se comprobó que **todo autor citado en el texto aparezca en la lista de referencias** de cada documento (sin faltantes) y que cada documento tenga su bibliografía y su declaración de uso de IA. Luego se revisó el estado de cada fuente externa del Estudio paralelo (Producto I):')
D.table(['Fuente', 'Estado', 'Observación'], [
 ['Batistic y Tymon (2017), *Education + Training*', 'Confirmada', 'Revista, volumen, páginas y DOI en registros en línea.'],
 ['Gamboa, Paixão y Jesus (2013), *J. Vocational Behavior*', 'Confirmada', 'Autoría, revista, volumen, páginas, DOI y muestra (346 estudiantes de enseñanza media, 12.º grado, Portugal).'],
 ['Ocampo y otros (2020), *J. Vocational Behavior*', 'Confirmada', 'Siete autores, revista, volumen, artículo y DOI.'],
 ['Pianda y otros (2024), *Cogent Business & Management*', 'Confirmada, con pendiente', 'Revista, volumen, artículo y DOI en tres registros; iniciales de autores por confirmar.'],
 ['Jollands (2017), conferencia', 'Confirmada', 'Es un trabajo de conferencia no arbitrado (pp. 170–175); se agregó la salvedad en el texto.'],
 ['Jackson y Dean (2023), *Higher Education Research & Development*', 'Parcial', 'Autores, revista, año y resultados confirmados; volumen, páginas y DOI por confirmar (un agregador indica el DOI 10.1080/07294360.2022.2048638).'],
 ['Clásicos (Bandura, Granovetter, Kolb, Cronbach, Holm, entre otros)', 'No verificada en línea', 'Seleccionadas desde el conocimiento de la herramienta; son referencias estándar, pero deben verificarse antes de publicar.'],
 ['Informe Metodológico y base de datos (Duoc UC)', 'Verificadas', 'El informe se leyó completo desde Drive y se contrastó con los umbrales usados; la base se recalculó.']], [5.6, 3.2, 7.7], size=8.6, colors={(0, 1): '1A1A1A', (1, 1): '1A1A1A', (2, 1): '1A1A1A', (3, 1): 'FFB800', (4, 1): '1A1A1A', (5, 1): 'FFB800', (6, 1): '666666', (7, 1): '1A1A1A'})
D.p('Nota sobre la verificación: se hizo con registros bibliográficos y resúmenes encontrados en línea; **no se abrieron los textos completos** porque el entorno no permitió descargar páginas. Las conclusiones de cada estudio se citan como las describe su resumen.', 10, GRAY)

D.h1('Cumplimiento del formato Duoc UC')
D.table(['Requisito de la norma', 'Resultado', 'Detalle'], [
 ['Papel carta y márgenes normales', 'Cumple', '21,59 × 27,94 cm; márgenes de 2,54 cm.'],
 ['Tipografía Calibri; cuerpo 11 pt', 'Cumple', 'Calibri en todo el texto; cuerpo 11 pt.'],
 ['Interlineado 1,5 en el cuerpo; texto justificado', 'Cumple', 'Cuerpo a 1,5 y justificado. Tablas y cajas de nota usan interlineado menor para legibilidad.'],
 ['Portada: título en mayúscula, 14 pt, negrita, sin punto final, filete amarillo, datos centrados', 'Cumple', 'Verificado en cada documento.'],
 ['Portada: logo oficial', 'Pendiente', 'Hay un recuadro «[Insertar logo Duoc UC]». No se generó ni imitó el logo.'],
 ['Portada: alumnos en orden alfabético, docente, asignatura y fecha', 'Parcial', 'Se indica autor/docente, proyecto y fecha; no aplica lista de alumnos. Revisar asignatura.'],
 ['Índice con número de página', 'Cumple', 'Generado a partir del PDF; páginas verificadas.'],
 ['Numeración de página (excepto portada)', 'Cumple', 'Pie de página con número desde la página 2.'],
 ['Estructura: Introducción, Desarrollo, Conclusión, Referencias, Anexos', 'Cumple', 'Cinco partes numeradas.'],
 ['Paleta oficial; máximo dos acentos por página', 'Cumple', 'Negro, amarillo, gris y gris claro. Tras la corrección, ningún color fuera de paleta en el contenido de los documentos ni en las infografías.'],
 ['Títulos con filete amarillo; tablas con encabezado oscuro y filas alternas; cajas con borde amarillo', 'Cumple', 'Verificado visualmente.'],
 ['Referencias según la norma indicada (APA 7)', 'Cumple, con pendientes', 'Ver verificación de fuentes.']], [6.0, 2.6, 7.9], size=8.6, colors={(0, 1): '1A1A1A', (1, 1): '1A1A1A', (2, 1): '1A1A1A', (3, 1): '1A1A1A', (4, 1): 'FFB800', (5, 1): 'FFB800', (6, 1): '1A1A1A', (7, 1): '1A1A1A', (8, 1): '1A1A1A', (9, 1): '1A1A1A', (10, 1): '1A1A1A', (11, 1): 'FFB800'})
D.p('Límite: la verificación se hizo sobre el archivo y su vista en PDF (LibreOffice). No se abrió en Microsoft Word; conviene abrir un documento en Word y confirmar portada e índice.', 10, GRAY)

D.h1('Coherencia entre productos')
D.table(['Aspecto', 'Resultado'], [
 ['Cifras que se repiten (puntaje global 3,87; 41 % con red de contactos; 83 % quiere proyectos con empresas; +0,17 con práctica previa; 38 estudiantes, 21 %, en semáforo rojo)', 'Iguales en todos los productos donde aparecen.'],
 ['Hipótesis central del Informe Metodológico y sus umbrales (0,8–1,2 puntos; r ≥ 0,45; escenarios 1, 2 y 3)', 'Citados de forma igual en los Informes B y C y en las infografías E y H.'],
 ['Códigos de recomendaciones R1 a R8', 'Mismo significado en A, B, C, G, I y las infografías.'],
 ['Declaración de IA y bibliografía', 'Presentes en los diez productos.'],
 ['Referencias cruzadas entre capítulos', 'Se corrigieron las que habían quedado obsoletas tras el cambio de estructura (hallazgos H-01).'],
 ['Colores del semáforo', 'En los documentos se nombran verde, amarillo y rojo, pero se dibujan en negro, amarillo y gris por la paleta Duoc UC; se aclara en el Informe A.']], [9.0, 7.5], size=8.8)

D.h1('Hallazgos y correcciones')
H = [
 ('H-01', 'Media', 'F, G, A, B, C', 'Referencias cruzadas y numeración de subtítulos obsoletas tras reestructurar según la norma (p. ej., «Sección 3», «Sección 6.2»).', 'Se eliminó la numeración fija de subtítulos y se reescribieron las referencias.', 'Corregido'),
 ('H-02', 'Alta', 'I, J', 'El estudio de Gamboa y otros (2013) se describía como de «enseñanza media técnica». La fuente indica estudiantes de enseñanza media (12.º grado); no dice que sea técnica.', 'Se corrigió y se verificó la muestra (346).', 'Corregido'),
 ('H-03', 'Media', 'I, J', 'Jollands (2017) se presentaba sin aclarar que es un trabajo de conferencia no arbitrado de un solo curso.', 'Se agregó la salvedad en el texto y en la infografía.', 'Corregido'),
 ('H-04', 'Media', 'E, B', '«Cuatro de cinco dimensiones suben con práctica» era inexacto para las dimensiones del estudio: suben las cinco. «Cuatro de cinco» corresponde a las dimensiones equivalentes del Informe Metodológico.', 'Se corrigió y se distinguió cada caso.', 'Corregido'),
 ('H-05', 'Baja', 'D', 'La leyenda de colores de las dimensiones seguía describiendo la paleta anterior (verde y ámbar).', 'Se actualizó a la paleta Duoc UC.', 'Corregido'),
 ('H-06', 'Baja', 'F', '«Más de 80 %» para P08 (80,0 %).', 'Se cambió a «80 % o más».', 'Corregido'),
 ('H-07', 'Media', 'I, J', '«Sin experiencias que contar» confundía «nunca ha hecho una práctica» (61 %) con no tener ninguna experiencia laboral.', 'Se reemplazó por «nunca han hecho una práctica».', 'Corregido'),
 ('H-08', 'Baja', 'F', 'Un color de celda fuera de la paleta Duoc UC.', 'Se reemplazó por gris claro #EEEEEE.', 'Corregido'),
 ('H-09', 'Media', 'I, J', 'Referencias con datos por confirmar (autoría, muestra, volumen). Se buscaron en línea.', 'Se confirmaron Gamboa y otros (2013), Ocampo y otros (2020, siete autores) y Pianda y otros (2024), que se incorporó al estudio.', 'Corregido; queda pendiente Jackson y Dean (volumen, páginas, DOI)'),
 ('H-10', 'Baja', 'B', 'El valor p ajustado de la tabla de equivalencia (nueve comparaciones) difiere del Anexo 1 (seis); podía parecer incoherente.', 'Se agregó una nota explicativa.', 'Corregido')]
D.table(['ID', 'Severidad', 'Producto', 'Hallazgo', 'Acción', 'Estado'], [list(h) for h in H], [1.1, 1.5, 1.6, 6.0, 4.0, 2.3], size=8.2, colors={(i, 1): ('FFB800' if h[1] == 'Alta' else ('EEEEEE' if h[1] == 'Baja' else 'FFD866')) for i, h in enumerate(H)}, align=['c', 'c', 'c', 'l', 'l', 'l'])
D.h2('Pendientes que no se pueden cerrar desde esta revisión')
D.numbered(['**Logo oficial de Duoc UC** en portadas e infografías, y revisión de los datos de portada (docente y asignatura).', '**Confirmar** volumen, páginas y DOI de Jackson y Dean (2023) y las iniciales de los autores de Pianda y otros (2024).', '**Doble lectura humana** de la clasificación de las respuestas abiertas y publicación del libro de códigos (R8).'])
D.h1('Riesgos residuales')
D.table(['Riesgo', 'Por qué persiste', 'Qué hacer'], [
 ['Autopercepción y una sola medición', 'La base no permite medir cambios ni desempeño real.', 'Aplicar R1: código, momento y grupo; sumar evaluación de tutores.'],
 ['Muestra voluntaria y concentrada en una escuela', '98 % de Administración y Negocios.', 'No generalizar a otras escuelas; repetir con otras sedes.'],
 ['Poca potencia para diferencias pequeñas', 'Solo se detectan diferencias de 0,28 puntos o más.', 'Aumentar la muestra en el piloto (≈ 110 por grupo).'],
 ['Hipótesis H2–H5 exploratorias', 'Formuladas tras una primera mirada a los datos.', 'Replicar con otra cohorte antes de decisiones de alto costo.'],
 ['Autorrevisión por IA', 'La misma herramienta elaboró y revisó los productos.', 'Revisión humana independiente, en especial del Informe B y de las referencias.'],
 ['Costos y metas del Manual G', 'Son estimaciones del equipo analista.', 'Validar con la Dirección de Escuela y Administración.']], [4.4, 6.0, 6.1], size=8.8)

D.part('CONCLUSIÓN')
D.h1('Opinión de auditoría')
D.p('Con base en el recálculo independiente, la revisión del texto y la revisión del formato, **los productos son consistentes con los datos de la encuesta y cumplen la norma de formato Duoc UC**, con las observaciones señaladas. Los hallazgos de mayor importancia (una descripción inexacta de un estudio externo, una frase inexacta sobre las dimensiones y varias referencias cruzadas obsoletas) se corrigieron.')
D.p('La opinión es **«aprobado con observaciones»** porque quedan tres pendientes (logo, dos datos de referencias y doble lectura de respuestas abiertas) y porque la revisión no es independiente.')
D.h1('Controles recomendados antes de difundir')
D.bullets(['Abrir cada documento en Word y confirmar portada, índice y saltos de página.', 'Insertar el logo oficial y revisar los datos de portada.', 'Completar los datos por confirmar en las referencias.', 'Pedir a una persona con formación estadística que revise el Informe B y a otra que revise las respuestas abiertas.', 'Volver a ejecutar `auditoria_datos.py` si la base cambia; el resultado debe seguir siendo «sin diferencias».', 'Mantener una versión con fecha y registro de cambios por producto.'])

D.part('REFERENCIAS')
D.p('Referencias en formato APA 7. Las fuentes externas se listan como en el Estudio paralelo (Producto I).', 10, GRAY)
refs = [
 'Batistic, S., & Tymon, A. (2017). Networking behaviour, graduate employability: A social capital perspective. *Education + Training, 59*(4), 374–388. https://doi.org/10.1108/ET-06-2016-0100',
 'Gamboa, V., Paixão, M. P., & Jesus, S. N. (2013). Internship quality predicts career exploration of high school students. *Journal of Vocational Behavior, 83*(1), 78–87. https://doi.org/10.1016/j.jvb.2013.02.009',
 'Jackson, D., & Dean, B. A. (2023). The contribution of different types of work-integrated learning to graduate employability. *Higher Education Research & Development*. https://ro.ecu.edu.au/ecuworks2022-2026/651 [volumen, páginas y DOI por confirmar]',
 'Jollands, M. (2017). A non-placement authentic simulated work integrated learning project for final year students. En *Proceedings of the Australian Conference on Science and Mathematics Education (2016)* (pp. 170–175). University of Queensland. https://openjournals.library.sydney.edu.au/IISME/article/view/10742',
 'Ocampo, A. C., Reyes, M. L., Chen, Y., Restubog, S. L. D., Chih, Y. Y., Chua-Garcia, L., & Guan, P. (2020). The role of internship participation and conscientiousness in developing career adaptability: A five-wave growth mixture model analysis. *Journal of Vocational Behavior, 120*, Article 103426. https://doi.org/10.1016/j.jvb.2020.103426',
 'Pianda, D., Hilmiana, Widianto, S., & Sartika, D. (2024). The impact of internship experience on the employability of vocational students: A bibliometric and systematic review. *Cogent Business & Management, 11*(1), Article 2386465. https://doi.org/10.1080/23311975.2024.2386465 [iniciales por confirmar]',
 'Duoc UC, Escuela de Administración y Negocios, Sede San Bernardo (2026). *Proyecto La Puerta: Informe metodológico y análisis prospectivo de brechas en habilidades blandas para la práctica profesional* [documento interno].',
 'Duoc UC (2026). *Proyecto La Puerta: Base de datos y matriz de análisis (20261009_1658)* [base de datos interna, no publicada].',
 'Bibliotecas Duoc UC. *Norma de formato de informes* [guía institucional de formato aplicada mediante la habilidad «formato de informes Duoc»; documento no verificado en línea].']
for b in refs:
    p = D.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT; p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1); p.paragraph_format.space_after = Pt(5); p.paragraph_format.line_spacing = 1.15
    for part in re.split(r'(\*[^*]+\*)', b):
        if not part: continue
        it = part.startswith('*') and part.endswith('*'); r = p.add_run(part[1:-1] if it else part); r.italic = it; r.font.size = Pt(10.5); r.font.name = FONT

D.part('ANEXOS')
D.h1('Detalle de las verificaciones numéricas')
D.p(f'Se listan las {nA} cifras recalculadas. «Publicado» es el valor del archivo de resultados que alimenta los productos; «Recalculado» es el valor obtenido con el método independiente.', 10.5)
D.table(['Verificación', 'Publicado', 'Recalculado', 'Coincide'], [[a['verificacion'], n(a['esperado'], 4) if abs(a['esperado']) < 1000 and a['esperado'] != int(a['esperado']) else str(int(a['esperado'])), n(a['recalculado'], 4) if abs(a['recalculado']) < 1000 and a['recalculado'] != int(a['recalculado']) else str(int(a['recalculado'])), 'Sí' if a['coincide'] else 'NO'] for a in AUD], [7.2, 3.3, 3.3, 2.7], size=8, align=['l', 'c', 'c', 'c'])
declaracion_ia(D, 'recalcular de forma independiente las cifras clave, revisar el texto y el formato de los productos y registrar hallazgos y correcciones; esta revisión fue hecha por la misma herramienta que elaboró los productos, por lo que no es independiente')
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/K_Informe_Auditoria_Verificacion.docx'); print('K ok')
