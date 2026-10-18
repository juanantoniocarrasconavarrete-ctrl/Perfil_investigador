from docx_lib import *
IT = {i['id']: i for i in R['items']}; DM = {d['id']: d for d in R['dims']}
OF = R['OF']; H1 = {r['var']: r for r in R['H1']}; H2 = {r['var']: r for r in R['H2']}
SHORT = {'P01': 'Conozco las tareas y condiciones reales de trabajo', 'P02': 'Tengo claras las exigencias de las empresas', 'P03': 'Confío en resolver una tarea nueva',
 'P04': 'Explico temas técnicos con claridad', 'P05': 'Aplico lo de clases a casos reales', 'P06': 'Sé qué método sirve en la empresa',
 'P07': 'Dialogo y logro acuerdos en equipo', 'P08': 'Sé cuándo actuar solo/a y cuándo consultar', 'P09': 'He comprobado si el trabajo real calza con mis intereses',
 'P10': 'Me siento seguro/a de adaptarme a un puesto', 'P11': 'Sé cómo contactar a profesionales del sector', 'P12': 'Tengo una red de contactos referentes',
 'P13': 'Aprendo de mis errores', 'P14': 'Priorizo la ética bajo presión', 'P15': 'Quiero participar en proyectos con empresas reales'}
SEMC = {'Fortaleza': '1F8A5B', 'Funcional': '8CBF3F', 'En desarrollo': AMB, 'Brecha': CORAL}
def cell_col(v):  # color de celda para promedios (criterio del informe metodológico: 4,2 / 3,5)
    return 'D9F0E4' if v >= 4.2 else ('FFE9A8' if v >= 3.5 else 'FBD5CB')
Q = R['cual']; N = R['N']
def tag(k): return {'H': '[HECHO]', 'I': '[INTERPRETACIÓN]', 'B': '[BRECHA]', 'Y': '[HIPÓTESIS]'}[k]
def contenido(doc, items):
    doc.h1('Contenido')
    for i, t in enumerate(items, 1):
        p = doc.d.add_paragraph(); runs(p, f'**{i}.**  {t}', 11); p.paragraph_format.space_after = Pt(5)
