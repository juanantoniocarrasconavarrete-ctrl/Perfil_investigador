from comun import *
D = Doc('Estudio paralelo de investigación', 'Lo que dicen otros estudios, qué significa para La Puerta y qué hacer', 'PRODUCTO I · ESTUDIO PARALELO DE INVESTIGACIÓN', None, 'Proyecto La Puerta · Estudio paralelo de investigación')
g = R['global']; OFd = OF; fo = {r['var']: r for r in OFd['filas']}; S = OFd['semaforo_estudiantes']; h4 = R['H4']

intro(D, 'Comparar lo que encontramos en la encuesta de La Puerta con lo que otros estudios han descubierto sobre la práctica laboral, las redes de contactos y la confianza de los estudiantes, y explicar qué significa y qué conviene hacer.',
 'La encuesta de octubre de 2026 mostró que los estudiantes de Duoc UC San Bernardo se sienten bastante preparados, pero casi no tienen contactos laborales y conocen poco el trabajo real. Antes de decidir acciones, conviene preguntarse: ¿esto que vemos aquí también lo ven otros estudios en otros lugares? A eso le llamamos un **estudio paralelo**: mirar en paralelo lo nuestro y lo que se sabe afuera.',
 'Contrastar los hallazgos de La Puerta con la investigación disponible, para saber qué está respaldado, qué hay que matizar y qué todavía no sabemos, y proponer acciones concretas.',
 ['Explicar con palabras simples qué es un estudio paralelo y cómo lo hicimos.', 'Comparar cinco hallazgos de La Puerta con lo que dicen otros estudios.', 'Describir las consecuencias de actuar, de no actuar y de actuar mal.', 'Proponer acciones para 30 días, 90 días y un año.'],
 'El texto tiene cinco partes: la Introducción (qué es un estudio paralelo y las ideas principales); el Desarrollo (cómo lo hicimos, las cinco comparaciones, las consecuencias y las acciones); la Conclusión (lo aprendido y lo que falta revisar); las Referencias; y los Anexos (las búsquedas realizadas y la declaración de uso de Inteligencia Artificial).')
D.h1('Las ideas principales, en pocas palabras')
D.kpis([('5', 'comparaciones entre\nnuestros datos y la investigación', NAVY), ('4', 'coinciden o casi\ncoinciden', NAVY), ('1', 'mismo límite:\nsolo medimos lo que se cree', NAVY), ('0', 'estudios chilenos\ncomparables revisados a fondo', NAVY)])
D.numbered([
 '**Lo que vimos en Duoc no es raro.** Otros estudios encuentran algo parecido: la experiencia de trabajo ayuda, **pero lo que más pesa es qué tan buena fue esa experiencia**, no solo haberla tenido.',
 '**Los contactos importan.** Estudiantes que se mueven y conocen gente tienen más información y más recursos, y por eso se sienten más empleables. En Duoc, solo 4 de cada 10 dicen tener esos contactos.',
 '**Las simulaciones y proyectos con empresas sirven.** En un estudio, un proyecto real simulado subió la confianza de los estudiantes tanto como una práctica. Es justo lo que nuestros estudiantes piden.',
 '**Casi todos los estudios, incluido el nuestro, miden lo que la gente *cree* de sí misma.** Falta medir si realmente trabajan mejor. Es el límite que más se repite.',
 '**No encontramos estudios chilenos comparables que podamos citar con seguridad.** Hay que seguir buscando antes de hacer afirmaciones sobre Chile.'])
D.callout('Cómo leer este estudio', 'Esto no es una prueba de que las acciones propuestas vayan a funcionar en Duoc. Es una **guía**: muestra que nuestras ideas tienen respaldo en otros lugares y dónde hay que tener cuidado.', None)

D.part('DESARROLLO')
D.h1('Cómo lo hicimos')
D.p('Buscamos en internet (octubre de 2026) estudios que respondieran las preguntas que nos dejó la encuesta: ¿ayuda haber hecho una práctica antes?, ¿qué pesa más, haber estado o lo que se aprendió?, ¿importan los contactos?, ¿sirven las simulaciones?, ¿qué tan seguros podemos estar de lo que miden los estudios?')
D.callout('Lo que pudimos y no pudimos hacer', ['**Pudimos:** revisar los resúmenes de cinco estudios de otros países (más una revisión sobre pasantías técnicas, que no pudimos confirmar) y comparar sus resultados con los nuestros.', '**No pudimos:** abrir los textos completos (la conexión del entorno lo impidió) ni consultar bases académicas formales. Los datos de cada estudio salen **de sus resúmenes** y algunos datos de la cita (volumen, páginas) están **por confirmar**.', '**Además:** casi todos los estudios son de otros países y de otras carreras (negocios, ingeniería, hotelería, enseñanza media). Por eso sirven de guía, no de prueba.'], None)
D.p('Para cada comparación usamos la misma ficha: qué vimos en La Puerta, qué dice la investigación, si coincide y qué significa. Marcamos el resultado con tres etiquetas: **COINCIDE** (la investigación va en la misma dirección), **MATIZA** (va en la misma dirección, pero con una diferencia importante) y **MISMO LÍMITE** (ambos tienen la misma debilidad).')

def ficha(num, pregunta, nuestro, afuera, veredicto, color, significa):
    D.h1(f'Comparación {num}: {pregunta}')
    t = D.d.add_table(rows=0, cols=2); borders(t)
    for lab, txt in (('Lo que vimos en La Puerta', nuestro), ('Lo que dice la investigación', afuera), ('Resultado', None), ('Qué significa', significa)):
        r = t.add_row(); keep_row(r); a, b = r.cells; shade(a, LG); cell_margins(a); cell_margins(b)
        p = a.paragraphs[0]; cellp(p); runs(p, lab, 9.5, NAVY, bold=True)
        p = b.paragraphs[0]; cellp(p, 'l', 0, 1.15)
        if txt is None: shade(b, color); runs(p, veredicto, 10.5, text_on(color), bold=True)
        else: runs(p, txt, 10.2)
        if lab != 'Qué significa': a.paragraphs[0].paragraph_format.keep_with_next = True; b.paragraphs[0].paragraph_format.keep_with_next = True
    set_col_widths(t, [4.2, 12.3]); D._spacer(12)

ficha(1, '¿ayuda haber hecho una práctica antes?',
 f"Quienes ya hicieron una práctica se sienten algo más preparados ({n(fo['GLOBAL']['con'])} contra {n(fo['GLOBAL']['sin'])} de 5), pero la diferencia es **pequeña**. Entre quienes no la tienen hay más estudiantes con puntaje bajo (25 % contra 14 %).",
 'Un estudio con 173 estudiantes de hotelería en China (Ocampo y otros, 2020) siguió a los alumnos cinco veces: quienes hicieron una pasantía fueron ganando confianza y capacidad de adaptarse; quienes no, casi no cambiaron. Otro estudio con más de 76 mil egresados de Australia (Jackson y Dean, 2023) encontró que las prácticas en empresas son lo que más se asocia con sentirse preparado para trabajar.',
 'COINCIDE EN LA DIRECCIÓN, PERO MATIZA EL TAMAÑO', AMB,
 'Todo apunta a que la práctica ayuda, igual que aquí. Pero los estudios que la muestran fuerte siguen a los mismos estudiantes en el tiempo; nosotros solo vemos una foto. Con nuestros datos, la ventaja es modesta. No es un motivo para tratar distinto a quien no ha practicado.')
ficha(2, '¿qué pesa más: haber estado en una práctica o lo que se vivió allí?',
 f"Lo que más acompaña a la seguridad de adaptarse es **conocer las tareas reales, saber aplicar lo aprendido y haber comprobado si el trabajo calza con uno**. Estas tres cosas explican cerca de la mitad de las diferencias. Haber hecho una práctica antes deja de importar cuando se tienen en cuenta.",
 'Un estudio con 346 estudiantes de enseñanza media técnica en Portugal (Gamboa y otros, 2013) midió seis rasgos de una práctica: autonomía, retroalimentación de colegas, apoyo social, oportunidades de aprender, formación y apoyo del supervisor. Casi todos predijeron cuánto exploraron su futura carrera los estudiantes, es decir, **la calidad de la práctica importó**. El estudio de Ocampo y otros (2020) también encontró que cómo partían los estudiantes influyó en cómo evolucionaron.',
 'COINCIDE', NAVY,
 'Es la coincidencia más útil. Dice que no basta con «mandar a practicar»: importa que la práctica enseñe, dé autonomía y apoyo. Por eso las acciones de La Puerta deberían cuidar la calidad de cada experiencia, no solo la cantidad.')
ficha(3, '¿importan los contactos?',
 f"Solo {pc(IT['P12']['fav'])} dice tener una red de contactos laborales. Es lo más bajo de las 15 afirmaciones. Pasa igual con y sin práctica previa.",
 'Un estudio con 376 estudiantes de negocios (Batistic y Tymon, 2017) encontró que quienes se mueven y arman redes se sienten más empleables, sobre todo porque así consiguen más información y recursos. La idea de fondo es antigua y conocida: los contactos fuera del círculo cercano traen información nueva (Granovetter, 1973).',
 'COINCIDE', NAVY,
 'Tener contactos no es un «extra»: es una forma de recibir información y oportunidades. Y es algo que se puede enseñar y practicar: cómo presentarse, cómo escribir a un profesional, qué preguntar. Hoy los estudiantes quieren vincularse (83 %) pero no tienen puentes.')
ficha(4, '¿sirven las simulaciones y los proyectos aunque no sean una práctica real?',
 'Lo más pedido por los estudiantes en sus comentarios son simulaciones, casos reales y visitas a empresas. Además, 83 % quiere participar en proyectos con empresas antes de su práctica.',
 'En una universidad de Australia (Jollands, 2017), estudiantes de ingeniería que hicieron un proyecto real, acompañados por un profesional de una empresa, **subieron su confianza para trabajar tanto como con una práctica**. En el estudio grande de Australia (Jackson y Dean, 2023), las actividades que no ocurren en una empresa fueron mejores para desarrollar el trabajo en equipo y la colaboración, y las prácticas en empresas, para sentirse preparado en general.',
 'COINCIDE, CON CAUTELA', AMB,
 'Las simulaciones y proyectos son una buena apuesta para quienes aún no han practicado. Pero ojo: en ese estudio se midió la **confianza** de los estudiantes, no si después les fue mejor al buscar o hacer un trabajo. Hay que medirlo.')
ficha(5, '¿cuánto podemos creerle a lo que los estudiantes dicen de sí mismos?',
 'Todo lo que medimos es lo que los estudiantes **creen** de sí mismos. No medimos si trabajan mejor ni qué opina su jefatura.',
 'Casi todos los estudios revisados miden también la percepción: el estudio de Australia (Jackson y Dean, 2023) trabaja con la sensación de estar preparado; el de ingeniería (Jollands, 2017) mide la confianza; y los otros miden exploración o adaptabilidad según los propios estudiantes. Un resumen de estudios sobre pasantías en carreras técnicas señala además que **aún hay pocas revisiones** sobre el tema.',
 'MISMO LÍMITE', GRAY,
 'No estamos peor que otros estudios, pero compartimos la misma debilidad. Para saber si lo que se cree se convierte en buen desempeño, hace falta que **las jefaturas de práctica también evalúen** y que se mida a los mismos estudiantes antes y después.')

D.h1('Mapa de coincidencias y diferencias')
D.table(['Tema', 'En La Puerta', 'En la investigación', 'Resultado'], [
 ['Práctica previa', 'Ayuda poco (+0,17 de 5)', 'Ayuda a ganar confianza (se mide en el tiempo)', 'COINCIDE / MATIZA'],
 ['Calidad de la experiencia', 'Conocer, aplicar y comprobar pesan más', 'La calidad de la práctica predice la exploración de carrera', 'COINCIDE'],
 ['Contactos', 'Solo 4 de cada 10 tiene red', 'Los contactos dan información y sensación de empleabilidad', 'COINCIDE'],
 ['Simulaciones y proyectos', 'Es lo más pedido', 'Un proyecto simulado sube la confianza como una práctica', 'COINCIDE, CON CAUTELA'],
 ['Medir lo que cree vs. lo que hace', 'Solo percepción', 'También casi solo percepción', 'MISMO LÍMITE']], [3.4, 4.5, 5.2, 3.4], size=9, colors={(0, 3): 'FFB800', (1, 3): '1A1A1A', (2, 3): '1A1A1A', (3, 3): 'FFB800', (4, 3): '666666'})

D.h1('Qué consecuencias tiene')
D.p('Las consecuencias que siguen son **escenarios razonados**, no predicciones exactas. Sirven para conversar y decidir.')
D.table(['Para…', 'Si actuamos bien', 'Si no hacemos nada', 'Si actuamos mal'], [
 ['**Estudiantes**', 'Llegan a la práctica con contactos y con al menos una vivencia real; menos susto el primer día.', 'La red depende de la suerte (quién conoce a alguien). Quienes no han practicado (6 de cada 10) siguen sin experiencias que contar.', 'Se sienten etiquetados («sin práctica previa»). Se les promete más de lo que se puede cumplir.'],
 ['**Docentes**', 'Tienen casos y visitas que dan vida a las clases; saben qué pedir a cada estudiante.', 'Siguen enseñando «para el aula» mientras los estudiantes piden «para el trabajo».', 'Se sobrecargan con actividades extra sin tiempo ni apoyo.'],
 ['**Empresas socias**', 'Reciben practicantes más preparados y una relación más cercana con la escuela.', 'Siguen viendo a estudiantes que conocen poco el día a día laboral.', 'Pierden la paciencia con actividades mal planificadas.'],
 ['**Escuela / Duoc**', 'Tiene evidencia propia para decidir y mostrar el impacto de La Puerta.', 'No puede demostrar si La Puerta funciona; la decisión se toma sin pruebas.', 'Escala un modelo sin comprobar si sirve y gasta recursos donde no corresponde.']], [2.6, 4.6, 4.6, 4.7], size=8.8)
D.callout('Lo que más conviene evitar', ['**Separar a los estudiantes por «tener o no tener práctica previa».** La ventaja es pequeña y no justifica una política especial.', '**Decir que La Puerta «funciona».** Con los datos de hoy solo podemos decir cómo están los estudiantes, no que el programa los haya cambiado.'], None)

D.h1('Qué hacer: acciones en 30 días, 90 días y un año')
D.p('Las acciones usan los mismos códigos (R1 a R8) del Manual de propuestas de mejora, pero aquí se explican en lenguaje cotidiano.')
D.table(['Cuándo', 'Qué hacer', 'Para qué', 'Código'], [
 ['**En 30 días**', 'Arreglar la encuesta: que cada estudiante tenga un código, que se sepa si contesta antes o después, y a qué grupo pertenece.', 'Poder comprobar si La Puerta sirve.', 'R1'],
 ['**En 30 días**', 'Ubicar a los 38 estudiantes que hoy puntúan más bajo y ofrecerles acompañamiento, sin etiquetarlos.', 'Prevenir un mal comienzo en la práctica.', 'R4'],
 ['**En 30 días**', 'Pedir a dos personas que lean por separado las respuestas abiertas y comparen cómo las agrupan.', 'Asegurar que las ideas no dependen de una sola lectura.', 'R8'],
 ['**En 90 días**', 'Organizar «cafés con profesionales»: conversaciones de 45 minutos con egresados y gente de empresas; pedir a cada estudiante que entreviste a un profesional.', 'Que cada estudiante tenga contactos y sepa cómo acercarse a otros.', 'R2'],
 ['**En 90 días**', 'Armar visitas a empresas y simulaciones (entrevista, primer día de trabajo), con una hoja de observación y una reflexión escrita.', 'Que todos vean el trabajo real antes de la práctica y aprendan de eso.', 'R3'],
 ['**En 90 días**', 'Un taller corto de comunicación: explicar lo técnico con palabras simples y pedir ayuda.', 'Mejorar lo que más cuesta explicar.', 'R5'],
 ['**En un año**', 'Medir antes y después con un grupo parecido que no participe; sumar la evaluación del tutor de empresa.', 'Saber si lo que se cree se convierte en mejor desempeño.', 'R1'],
 ['**En un año**', 'Revisar inglés y herramientas (ERP, Excel, Power BI) y las actividades para 3.º–4.º semestre, y decidir si se amplía La Puerta.', 'Cerrar brechas que los estudiantes piden y decidir con evidencia.', 'R6 · R7']], [2.4, 7.4, 4.9, 1.8], size=8.8)
D.callout('Un punto de partida que no cuesta casi nada', 'La entrevista a un profesional (R2) y la hoja de observación en las visitas (R3) pueden hacerse **dentro de asignaturas que ya existen**, sin gastos extras. Es la forma más rápida de empezar.', None)

D.part('CONCLUSIÓN')
D.h1('Lo aprendido')
D.numbered([
 '**Nuestros resultados tienen respaldo.** En cuatro de las cinco comparaciones, lo que vimos aquí va en la misma dirección que lo que dicen otros estudios.',
 '**La calidad pesa más que la cantidad.** Una buena experiencia (con autonomía, apoyo y aprendizaje) importa más que el solo hecho de haber hecho una práctica.',
 '**Los contactos y los proyectos reales son buenas apuestas.** Hay evidencia de otros lugares y una demanda clara en Duoc.',
 '**Todos medimos lo que se cree, no lo que se hace.** Hay que sumar la mirada de las jefaturas y medir antes y después.',
 '**Falta mirar a Chile.** La investigación que encontramos viene de otros países; debemos buscar y revisar estudios chilenos antes de generalizar.'])
D.h1('Lo que todavía hay que revisar')
D.bullets(['Abrir y leer los textos completos de los estudios citados y confirmar sus datos (autores, volumen y páginas).', 'Buscar estudios sobre formación técnico-profesional en Chile (por ejemplo, sobre las prácticas iniciales y el rendimiento en el primer año), que aparecieron en la búsqueda pero no pudimos revisar a fondo.', 'Revisar si existe una revisión formal que reúna los estudios sobre pasantías y empleabilidad en estudiantes técnicos; una búsqueda encontró una de 23 artículos (2009–2023), pero no pudimos confirmar sus datos.', 'Repetir este estudio paralelo cuando haya resultados antes/después de La Puerta.'])

D.part('REFERENCIAS')
D.p('Referencias en formato APA 7, ordenadas alfabéticamente. Las cinco primeras son estudios revisados **a través de sus resúmenes**; los datos marcados con [por confirmar] deben verificarse en la fuente. Las demás son referencias de apoyo, no verificadas en línea durante esta sesión.', 10, GRAY)
refs = [
 'Batistic, S., & Tymon, A. (2017). Networking behaviour, graduate employability: A social capital perspective. *Education + Training, 59*(4), 374–388. https://doi.org/10.1108/ET-06-2016-0100',
 'Gamboa, V., Paixão, M. P., & Jesus, S. N. (2013). Internship quality predicts career exploration of high school students. *Journal of Vocational Behavior, 83*, 78–87. https://doi.org/10.1016/j.jvb.2013.02.009 [autoría y datos inferidos por coincidencia de título y diseño; por confirmar]',
 'Jackson, D., & Dean, B. A. (2023). The contribution of different types of work-integrated learning to graduate employability. *Higher Education Research & Development*. https://ro.ecu.edu.au/ecuworks2022-2026/651 [volumen y páginas por confirmar]',
 'Jollands, M. (2017). A non-placement authentic simulated work integrated learning project for final year students. En *Proceedings of the Australian Conference on Science and Mathematics Education (2016)* (pp. 170–175). University of Queensland. https://openjournals.library.sydney.edu.au/IISME/article/view/10742 [trabajo no arbitrado]',
 'Ocampo, A. C. G., et al. (2020). The role of internship participation and conscientiousness in developing career adaptability: A five-wave growth mixture model analysis. *Journal of Vocational Behavior, 120*, Article 103426. https://doi.org/10.1016/j.jvb.2020.103426 [lista completa de autores por confirmar]',
 'Granovetter, M. S. (1973). The strength of weak ties. *American Journal of Sociology, 78*(6), 1360–1380.',
 'Bandura, A. (1997). *Self-efficacy: The exercise of control*. W. H. Freeman.',
 'Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall.',
 'Tomlinson, M. (2017). Forms of graduate capital and their relationship to graduate employability. *Education + Training, 59*(4), 338–352.',
 'Yorke, M. (2006). *Employability in higher education: What it is – what it is not*. Higher Education Academy.',
 'Duoc UC (2026). *Proyecto La Puerta: Base de datos y matriz de análisis (20261009_1658)* [base de datos interna, no publicada].']
for b in sorted(refs[:5] + refs[5:10], key=lambda x: x.lower()) + refs[10:]:
    p = D.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT; p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1); p.paragraph_format.space_after = Pt(5); p.paragraph_format.line_spacing = 1.15
    for part in re.split(r'(\*[^*]+\*)', b):
        if not part: continue
        it = part.startswith('*') and part.endswith('*'); r = p.add_run(part[1:-1] if it else part); r.italic = it; r.font.size = Pt(10.5); r.font.name = FONT

D.part('ANEXOS')
D.h1('Búsquedas realizadas')
D.p('Todas las búsquedas se hicieron el 18 de octubre de 2026, en la web, y se revisaron los resúmenes que devolvió el buscador.', 10.5)
D.table(['Pregunta', 'Qué se buscó', 'Qué se encontró y se usó'], [
 ['¿Ayuda la práctica?', 'Prácticas y empleabilidad (revisiones y estudios)', 'Jackson y Dean (2023); una revisión de pasantías en estudiantes técnicos (23 artículos, 2009–2023) por confirmar'],
 ['¿Importan los contactos?', 'Redes y empleabilidad en educación superior', 'Batistic y Tymon (2017)'],
 ['¿Cómo es en Chile?', 'Práctica profesional y empleabilidad en la educación técnica chilena', 'Documentos generales de contexto y estudios de prácticas iniciales por revisar; no se citan resultados'],
 ['¿Sube la confianza?', 'Pasantías, confianza y adaptabilidad', 'Ocampo y otros (2020); Gamboa y otros (2013)'],
 ['¿Sirven las simulaciones?', 'Aprendizaje simulado y empleabilidad', 'Jollands (2017); otros informes de menor solidez, no citados'],
 ['Verificación de citas', 'Datos bibliográficos de los estudios principales', 'Confirmados: Batistic y Tymon (revista, volumen, páginas, DOI); Ocampo y otros (revista, volumen, artículo, DOI). Por confirmar: el resto']], [3.4, 5.5, 7.6], size=8.8)
declaracion_ia(D, 'buscar y resumir estudios, compararlos con los resultados de La Puerta y redactar el texto en lenguaje cotidiano')
D.save('/home/user/Perfil_investigador/La_Puerta_Informes/informes/I_Estudio_Paralelo_Investigacion.docx'); print('I ok')
