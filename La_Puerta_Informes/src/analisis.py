"""Proyecto La Puerta — análisis de la encuesta (n=184, un solo momento).
Uso: python3 -I analisis.py <ruta_xlsx>
Salida: resultados.json (+ resultados.pkl) en ../ . No exporta correos ni textos con datos personales.
"""
import sys, json, re, pickle, itertools
import numpy as np, pandas as pd
from scipy import stats
import statsmodels.api as sm

SRC = sys.argv[1]
OUT = __file__.rsplit('/src/', 1)[0]
rng = np.random.default_rng(2026)

raw = pd.read_excel(SRC, sheet_name='Form Responses 1')
C = list(raw.columns)
P = [f'P{i:02d}' for i in range(1, 16)]
df = pd.DataFrame({p: pd.to_numeric(raw[C[8 + i]].astype(str).str[0], errors='coerce') for i, p in enumerate(P)})
df = df.replace(0, np.nan)                       # 0 = No sé / No aplica -> excluido
na_n = {p: int(raw[C[8 + i]].astype(str).str.startswith('0').sum()) for i, p in enumerate(P)}

ITEM = {
 'P01': 'Conozco las tareas y condiciones reales de trabajo', 'P02': 'Tengo claras las exigencias de las empresas',
 'P03': 'Confío en resolver una tarea nueva', 'P04': 'Explico temas técnicos con claridad',
 'P05': 'Aplico lo de clases a casos reales', 'P06': 'Identifico qué método sirve para la empresa',
 'P07': 'Dialogo y llego a acuerdos en equipo', 'P08': 'Distingo cuándo actuar solo/a y cuándo consultar',
 'P09': 'He podido comprobar si el trabajo real calza con mis intereses', 'P10': 'Me siento seguro/a de adaptarme a un puesto',
 'P11': 'Sé cómo contactar a profesionales del sector', 'P12': 'Cuento con una red de contactos referentes',
 'P13': 'Aprendo de mis errores', 'P14': 'Priorizo la ética bajo presión', 'P15': 'Me interesa trabajar en proyectos con empresas reales'}
DIM = {'D1': ('Conocer el rol profesional', ['P01', 'P02']),
       'D2': ('Transferir lo aprendido', ['P03', 'P04', 'P05', 'P06']),
       'D3': ('Autoeficacia laboral', ['P07', 'P08', 'P09', 'P10']),
       'D4': ('Redes e interés por vincularse', ['P11', 'P12', 'P15']),
       'D5': ('Aprender del error y ética', ['P13', 'P14'])}
for d, (_, its) in DIM.items():
    df[d] = df[its].mean(axis=1, skipna=True)
df['GLOBAL'] = df[P].mean(axis=1, skipna=True)
df['n_resp'] = df[P].notna().sum(axis=1)

# perfil
yr_map = {C and '1.er o 2.º semestre (Primer año)': '1.º–2.º sem.', '3.er o 4.º semestre (Segundo año)': '3.º–4.º sem.',
          '5.º o 6.º semestre (Tercer año)': '5.º–6.º sem.', '7.º u 8.º semestre (Cuarto año)': '7.º–8.º sem.'}
df['anio'] = raw[C[6]].map(yr_map)
df['anio3'] = df['anio'].replace({'7.º–8.º sem.': '5.º sem. o más', '5.º–6.º sem.': '5.º sem. o más'})
pr_map = {'No, nunca he realizado una práctica formativa previa (esta será mi primera experiencia).': 'Sin práctica previa',
          'Sí, realicé práctica técnica de nivel medio (colegio técnico-profesional / EMTP).': 'Práctica EMTP',
          'Sí, he realizado una práctica laboral intermedia o pasantía en mi carrera actual.': 'Pasantía en la carrera',
          'Sí, realicé una práctica en otra carrera previa (técnica o universitaria).': 'Práctica en otra carrera'}
df['practica'] = raw[C[7]].map(pr_map)
df['con_practica'] = (df['practica'] != 'Sin práctica previa').astype(int)
df['escuela'] = raw[C[5]]
df['abi1'] = raw[C[24]]; df['abi2'] = raw[C[25]]
N = len(df)

R = {'N': N, 'fecha_ini': str(raw.Timestamp.min().date()), 'fecha_fin': str(raw.Timestamp.max().date()),
     'consentimiento': int((raw[C[1]].astype(str).str.startswith('Sí')).sum()),
     'campos_vacios': {'ID02 código': int(raw[C[2]].isna().sum()), 'ID03 momento': int(raw[C[3]].isna().sum()),
                       'ID04 grupo': int(raw[C[4]].isna().sum()), 'POST_EXP1': int(raw[C[23]].isna().sum())},
     'correos_duplicados': int(raw[C[26]].duplicated().sum())}
R['perfil'] = {'escuela': df.escuela.value_counts().to_dict(), 'anio': df.anio.value_counts().to_dict(),
               'practica': df.practica.value_counts().to_dict(), 'con_practica': int(df.con_practica.sum())}
R['perfil_pct'] = {'escuela_EAN': round(100 * (df.escuela == 'Escuela de Administración y Negocios').mean(), 1)}
ct = pd.crosstab(df.anio3, df.con_practica)
R['cruce_anio_practica'] = {a: {'sin': int(ct.loc[a, 0]), 'con': int(ct.loc[a, 1])} for a in ct.index}

# calidad
R['calidad'] = {'respuestas_NA_total': int(sum(na_n.values())), 'na_por_item': na_n,
                'pct_celdas_NA': round(100 * sum(na_n.values()) / (N * 15), 2),
                'straightlining_n': int((df[P].nunique(axis=1) == 1).sum()),
                'min_items_resp': int(df.n_resp.min())}

def alpha(x):
    x = x.dropna()
    k = x.shape[1]
    return float(k / (k - 1) * (1 - x.var(ddof=1).sum() / x.sum(axis=1).var(ddof=1)))
def boot_ci(v, f=np.mean, B=4000):
    v = np.asarray(v.dropna()); idx = rng.integers(0, len(v), (B, len(v)))
    b = np.array([f(v[i]) for i in idx]); return [float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))]

# items
it = []
for p in P:
    s = df[p].dropna(); n = len(s)
    it.append({'id': p, 'texto': ITEM[p], 'n': n, 'media': float(s.mean()), 'sd': float(s.std()), 'mediana': float(s.median()),
               'fav': float(100 * (s >= 4).mean()), 'neu': float(100 * (s == 3).mean()), 'des': float(100 * (s <= 2).mean()),
               'p5': float(100 * (s == 5).mean()), 'na': na_n[p], 'ci': boot_ci(s)})
R['items'] = it
dm = []
for d, (nm, its) in DIM.items():
    s = df[d].dropna()
    fav = float(100 * (df[its].stack() >= 4).mean())
    dm.append({'id': d, 'nombre': nm, 'items': its, 'n': len(s), 'media': float(s.mean()), 'sd': float(s.std()),
               'mediana': float(s.median()), 'fav': fav, 'ci': boot_ci(s), 'alpha': alpha(df[its]) if len(its) > 1 else None})
R['dims'] = dm
g = df.GLOBAL.dropna()
R['global'] = {'media': float(g.mean()), 'sd': float(g.std()), 'mediana': float(g.median()), 'ci': boot_ci(g),
               'alpha': alpha(df[P]), 'fav_resp': float(100 * (g >= 4).mean()), 'bajo3': float(100 * (g < 3).mean()),
               'q': [float(x) for x in g.quantile([.1, .25, .5, .75, .9])],
               'fav_items': float(100 * (df[P].stack() >= 4).mean()), 'des_items': float(100 * (df[P].stack() <= 2).mean())}
# alpha sin P15 e item-total
R['global']['alpha_sin_P15'] = alpha(df[[p for p in P if p != 'P15']])
tot = df[P].mean(axis=1)
R['item_total'] = {p: float(df[p].corr(df[[q for q in P if q != p]].mean(axis=1), method='spearman')) for p in P}

# semáforo de brecha (criterio propuesto, alineado a exigencia 70 %)
def sem(f): return 'Fortaleza' if f >= 80 else ('Funcional' if f >= 70 else ('En desarrollo' if f >= 60 else 'Brecha'))
for x in R['items'] + R['dims']: x['semaforo'] = sem(x['fav'])

# ---------- subgrupos ----------
def cliffs(a, b):
    a = np.asarray(a); b = np.asarray(b)
    gt = sum((x > b).sum() for x in a); lt = sum((x < b).sum() for x in a)
    return float((gt - lt) / (len(a) * len(b)))
def holm(pv):
    pv = np.array(pv); o = np.argsort(pv); m = len(pv); adj = np.empty(m); run = 0
    for r, i in enumerate(o):
        run = max(run, (m - r) * pv[i]); adj[i] = min(1, run)
    return adj.tolist()
VARS = ['GLOBAL', 'D1', 'D2', 'D3', 'D4', 'D5']
VN = {'GLOBAL': 'Global'} | {d: DIM[d][0] for d in DIM}

# H1 práctica previa vs sin
H1 = []
for v in VARS:
    a = df.loc[df.con_practica == 1, v].dropna(); b = df.loc[df.con_practica == 0, v].dropna()
    u, p = stats.mannwhitneyu(a, b, alternative='two-sided')
    H1.append({'var': v, 'nombre': VN[v], 'media_con': float(a.mean()), 'media_sin': float(b.mean()), 'dif': float(a.mean() - b.mean()),
               'n_con': len(a), 'n_sin': len(b), 'U': float(u), 'p': float(p), 'cliff': cliffs(a, b), 'A': float(u / (len(a) * len(b))),
               'dif_ci': [float(x) for x in np.percentile([rng.choice(a, len(a)).mean() - rng.choice(b, len(b)).mean() for _ in range(4000)], [2.5, 97.5])]})
for r, ph in zip(H1, holm([r['p'] for r in H1])): r['p_holm'] = ph
R['H1'] = H1
# por ítem (exploratorio)
H1i = []
for p in P:
    a = df.loc[df.con_practica == 1, p].dropna(); b = df.loc[df.con_practica == 0, p].dropna()
    u, pv = stats.mannwhitneyu(a, b, alternative='two-sided')
    H1i.append({'id': p, 'media_con': float(a.mean()), 'media_sin': float(b.mean()), 'dif': float(a.mean() - b.mean()), 'p': float(pv), 'cliff': cliffs(a, b)})
for r, ph in zip(H1i, holm([r['p'] for r in H1i])): r['p_holm'] = ph
R['H1_items'] = H1i
tipos = df.groupby('practica')[VARS].mean().round(3)
R['por_practica_tipo'] = {k: {**tipos.loc[k].to_dict(), 'n': int((df.practica == k).sum())} for k in tipos.index}

# H2 año de estudio
H2 = []
for v in VARS:
    d = df[['anio3', v]].dropna()
    grp = [d.loc[d.anio3 == k, v] for k in ['1.º–2.º sem.', '3.º–4.º sem.', '5.º sem. o más']]
    h, p = stats.kruskal(*grp)
    codes = d.anio3.map({'1.º–2.º sem.': 1, '3.º–4.º sem.': 2, '5.º sem. o más': 3})
    rho, pr = stats.spearmanr(codes, d[v])
    eps = float((h - 3 + 1) / (len(d) - 3))
    H2.append({'var': v, 'nombre': VN[v], 'H': float(h), 'p': float(p), 'eps2': eps, 'rho': float(rho), 'p_rho': float(pr),
               'medias': [float(x.mean()) for x in grp], 'ns': [len(x) for x in grp]})
for r, ph in zip(H2, holm([r['p'] for r in H2])): r['p_holm'] = ph
R['H2'] = H2
H2i = []
for p in P:
    d = df[['anio3', p]].dropna(); codes = d.anio3.map({'1.º–2.º sem.': 1, '3.º–4.º sem.': 2, '5.º sem. o más': 3})
    rho, pv = stats.spearmanr(codes, d[p]); H2i.append({'id': p, 'rho': float(rho), 'p': float(pv),
        'medias': [float(d.loc[d.anio3 == k, p].mean()) for k in ['1.º–2.º sem.', '3.º–4.º sem.', '5.º sem. o más']]})
for r, ph in zip(H2i, holm([r['p'] for r in H2i])): r['p_holm'] = ph
R['H2_items'] = H2i
# efecto conjunto práctica + año en Global (OLS con errores robustos)
d = df[['GLOBAL', 'con_practica', 'anio3']].dropna().copy()
d['anio_c'] = d.anio3.map({'1.º–2.º sem.': 1, '3.º–4.º sem.': 2, '5.º sem. o más': 3})
m = sm.OLS(d.GLOBAL, sm.add_constant(d[['con_practica', 'anio_c']])).fit(cov_type='HC3')
R['ols_global'] = {k: {'b': float(m.params[k]), 'ci': [float(x) for x in m.conf_int().loc[k]], 'p': float(m.pvalues[k])} for k in m.params.index}
R['ols_global']['r2'] = float(m.rsquared); R['ols_global']['n'] = int(m.nobs)

# H3 D4 más débil
dd = df[['D1', 'D2', 'D3', 'D4', 'D5']].dropna()
fr = stats.friedmanchisquare(*[dd[c] for c in dd.columns])
R['H3'] = {'n': len(dd), 'chi2': float(fr.statistic), 'p': float(fr.pvalue), 'W': float(fr.statistic / (len(dd) * 4)), 'pares': []}
pp = []
for c in ['D1', 'D2', 'D3', 'D5']:
    w = stats.wilcoxon(dd['D4'], dd[c]); pp.append({'vs': c, 'dif_media': float((dd['D4'] - dd[c]).mean()), 'p': float(w.pvalue),
        'ci': boot_ci(dd['D4'] - dd[c])})
for r, ph in zip(pp, holm([r['p'] for r in pp])): r['p_holm'] = ph
R['H3']['pares'] = pp
# D4 sin P15 (redes puras)
df['D4_redes'] = df[['P11', 'P12']].mean(axis=1)
dd2 = df[['D1', 'D2', 'D3', 'D5', 'D4_redes']].dropna()
R['H3']['D4_redes_media'] = float(df.D4_redes.mean())
R['H3']['redes_vs_otros'] = [{'vs': c, 'dif': float((dd2['D4_redes'] - dd2[c]).mean()), 'p': float(stats.wilcoxon(dd2['D4_redes'], dd2[c]).pvalue)} for c in ['D1', 'D2', 'D3', 'D5']]
# P12 el más bajo
pw = []
for p in P:
    if p == 'P12': continue
    x = df[['P12', p]].dropna(); pw.append({'vs': p, 'dif': float((x.P12 - x[p]).mean()), 'p': float(stats.wilcoxon(x.P12, x[p]).pvalue)})
for r, ph in zip(pw, holm([r['p'] for r in pw])): r['p_holm'] = ph
R['H3']['P12_vs'] = pw

# H4 vínculo conocimiento/experiencia -> seguridad
def sp(a, b):
    x = df[[a, b]].dropna(); r, p = stats.spearmanr(x[a], x[b]); return {'rho': float(r), 'p': float(p), 'n': len(x)}
R['H4'] = {'P09_P10': sp('P09', 'P10'), 'D1_P10': sp('D1', 'P10'), 'P12_P10': sp('P12', 'P10'), 'P11_P12': sp('P11', 'P12'),
           'P05_P10': sp('P05', 'P10'), 'P03_P10': sp('P03', 'P10'), 'P01_P10': sp('P01', 'P10'), 'P02_P10': sp('P02', 'P10')}
d = df[['P10', 'P09', 'P01', 'P02', 'P12', 'P05', 'con_practica']].dropna().copy()
d['anio_c'] = df.loc[d.index, 'anio3'].map({'1.º–2.º sem.': 1, '3.º–4.º sem.': 2, '5.º sem. o más': 3})
m4 = sm.OLS(d.P10, sm.add_constant(d[['P09', 'P01', 'P12', 'P05', 'con_practica', 'anio_c']])).fit(cov_type='HC3')
R['H4']['ols'] = {k: {'b': float(m4.params[k]), 'ci': [float(x) for x in m4.conf_int().loc[k]], 'p': float(m4.pvalues[k])} for k in m4.params.index}
R['H4']['ols']['r2'] = float(m4.rsquared); R['H4']['ols']['n'] = int(m4.nobs)
# estandarizado (beta)
zs = d[['P10', 'P09', 'P01', 'P12', 'P05']].apply(lambda s: (s - s.mean()) / s.std())
mz = sm.OLS(zs.P10, sm.add_constant(zs[['P09', 'P01', 'P12', 'P05']])).fit(cov_type='HC3')
R['H4']['beta_std'] = {k: float(mz.params[k]) for k in ['P09', 'P01', 'P12', 'P05']}
corr = df[P].corr(method='spearman'); R['corr_items'] = corr.round(3).values.tolist()
cd = df[['D1', 'D2', 'D3', 'D4', 'D5']].corr(method='spearman'); R['corr_dims'] = cd.round(3).values.tolist()

# H5 demanda de proyectos reales
s15 = df.P15.dropna(); k = int((s15 >= 4).sum())
bt = stats.binomtest(k, len(s15), 0.70, alternative='greater')
R['H5'] = {'k': k, 'n': len(s15), 'fav': float(100 * k / len(s15)), 'p_vs70': float(bt.pvalue), 'ci_wilson': [float(x) for x in stats.binomtest(k, len(s15)).proportion_ci(method='wilson')]}
a = df.loc[df.con_practica == 1, 'P15'].dropna(); b = df.loc[df.con_practica == 0, 'P15'].dropna()
R['H5']['practica'] = {'media_con': float(a.mean()), 'media_sin': float(b.mean()), 'p': float(stats.mannwhitneyu(a, b).pvalue), 'fav_con': float(100 * (a >= 4).mean()), 'fav_sin': float(100 * (b >= 4).mean())}
grp = [df.loc[df.anio3 == k, 'P15'].dropna() for k in ['1.º–2.º sem.', '3.º–4.º sem.', '5.º sem. o más']]
R['H5']['anio'] = {'medias': [float(x.mean()) for x in grp], 'fav': [float(100 * (x >= 4).mean()) for x in grp], 'p': float(stats.kruskal(*grp).pvalue)}
# interés (P15) vs. falta de contraste P09
R['H5']['P15_P09'] = sp('P15', 'P09')
# bajo P09 -> P15
lowP09 = df.loc[df.P09 <= 3, 'P15'].dropna(); hiP09 = df.loc[df.P09 >= 4, 'P15'].dropna()
R['H5']['P15_por_P09'] = {'fav_bajo': float(100 * (lowP09 >= 4).mean()), 'fav_alto': float(100 * (hiP09 >= 4).mean()), 'n_bajo': len(lowP09), 'n_alto': len(hiP09)}

# perfiles de respuesta
df['perfil'] = pd.cut(df.GLOBAL, [0, 3, 4, 5.01], labels=['Por fortalecer (<3)', 'Intermedio (3–3,99)', 'Sólido (≥4)'], right=False)
R['perfiles'] = df.perfil.value_counts().sort_index().to_dict()
R['perfiles_pct'] = (100 * df.perfil.value_counts(normalize=True).sort_index()).round(1).to_dict()
# heat item x año / práctica
R['heat_anio'] = {p: [float(df.loc[df.anio3 == k, p].mean()) for k in ['1.º–2.º sem.', '3.º–4.º sem.', '5.º sem. o más']] for p in P}
R['heat_pract'] = {p: [float(df.loc[df.con_practica == k, p].mean()) for k in [0, 1]] for p in P}
R['dim_anio'] = {d: [float(df.loc[df.anio3 == k, d].mean()) for k in ['1.º–2.º sem.', '3.º–4.º sem.', '5.º sem. o más']] for d in DIM}
R['dim_pract'] = {d: [float(df.loc[df.con_practica == k, d].mean()) for k in [0, 1]] for d in DIM}
R['dim_pract_cross'] = {d: float(df[d].mean()) for d in DIM}

# ---------- cualitativo ----------
def has(s, pats): return bool(re.search('|'.join(pats), s, flags=re.I)) if isinstance(s, str) else False
T1 = {
 'Habilidades blandas (equipo, comunicación, responsabilidad, adaptación)': [r'trabajo en equipo', r'comunicar|comunicaci', r'responsab', r'adapta', r'empat', r'liderazgo', r'habilidades blandas', r'proactiv', r'relacionarme|relaciones con otras', r'expresar|expresión|expresarme', r'presentacion|disertacion|hablar|en publico|en público', r'compromiso', r'seguir aprendiendo|aprender cosas nuevas|capacidad de aprend|siempre se aprende'],
 'Conocimiento técnico del área (finanzas, logística, comex, marketing, RR.HH.)': [r'finanz', r'log[ií]stic', r'comex|comercio exterior', r'marketing', r'ventas', r'contabilidad', r'auditor', r'cadenas? ', r'contenedor|naviera', r'presupuesto', r'sueldos|liquidaciones|tipos de contrato', r'descripci[oó]n de cargo|descriptor', r'econom[ií]a', r'documentaci', r'tesorer|control de gesti'],
 'Herramientas digitales (Excel, Power BI, datos, IA, web)': [r'excel', r'power ?bi', r'an[aá]lisis de datos|big data', r'\bia\b', r'sitios? web|landing', r'herramientas tecnol', r'programas vanguardistas'],
 'Ética, inclusión y normativa': [r'[eé]tic', r'inclusi', r'discapacidad', r'normativa|leyes|derechos y deberes|prejuicios|sesgos|barreras'],
 'Mayor claridad sobre el campo laboral y su carrera': [r'campo laboral', r'oportunidades (de|que|laborales|hay)', r'encaminada', r'rubro', r'c[oó]mo funciona|como funciona|funcionamiento', r'aspirar', r'trabajos que me gustan', r'muchas áreas', r'realidad laboral', r'condiciones laboral', r'moverme en el mundo laboral', r'como se mueve'],
 'Redes y contactos': [r'contactos', r'colegas', r'conocer (a )?(diferentes |a más |más )?personas nuevas|personas nuevas'],
 'Brecha teoría–práctica': [r'no siempre lo que se ense', r'relleno', r'solo margen te[oó]rico', r'todo lo te[oó]rico'],
 'Sin aprendizaje claro / no sabe': [r'^\W*(ninguno|nada|no lo se|no lose|non|a[uú]n non|no lo tengo claro|ninguno particular)\W*$', r'no (he|e) tenido', r'no hemos tenido', r'la verdad no', r'no sabr', r'todabia no', r'me falta mucho|falta aprender|me falta'],
}
T2 = {
 'Preparación para la práctica y el empleo (entrevista, CV, inducción, apoyo)': [r'entrevista', r'curr[ií]culum|\bcv\b', r'pre ?-?pr[aá]ctica|inducci', r'supervisi[oó]n de pr', r'ayudant[ií]a', r'linkedin|marca personal', r'busquen la pr[aá]ctica|encontrar pr[aá]ctica|buscar pr[aá]cticas|encontrar práctica', r'seminarios y procesos de explicaci', r'capacite para la pr[aá]ctica|tutos? que nos diga', r'preparaci[oó]n para (la|el)'],
 'Simulaciones, casos reales y práctica aplicada': [r'simulaci', r'casos reales', r'clases m[aá]s pr[aá]cticas|ramos pr[aá]cticos|m[aá]s pr[aá]ctic[oa]s?\b|talleres m[aá]s pr[aá]cticos|talleres pr[aá]cticos', r'realismo|toque de realidad|realidad en lugar|problem[aá]ticas reales|situaciones reales', r'proyectos? que simulen', r'aplicar lo aprendido|poner en pr[aá]ctica|aplicando conocimientos|aplicar todo', r'actividades (que sean )?laborales|actividades pr[aá]cticas', r'pr[aá]ctica de una profesi[oó]n|mundo laboral'],
 'Salidas a terreno, visitas, ferias y charlas': [r'salidas?', r'visitas?', r'paseos', r'terreno', r'ferias', r'charlas', r'ir a otra bodega'],
 'Software y herramientas (ERP, SAP, Softland, Excel, Python, Power BI, IA)': [r'\bsap\b', r'softland', r'erp', r'excel+l?', r'python|payton', r'power ?bi', r'software|sistemas de administraci|programas de administraci', r'ia para|big ?data', r'marketing digital|herramientas tecnol|herramientas corporativas|creaci[oó]n de contenido', r'herramientas o procesos'],
 'Idiomas (inglés principalmente)': [r'ingl[eé]s|idioma|portugu|franc[eé]s|mandar[ií]n|chino'],
 'Comunicación, oratoria y habilidades blandas': [r'comunicaci', r'hablar|oratoria|p[uú]blico|presentaci', r'liderazgo|autoconocimiento|emocional|escucha|confianza|habilidades blandas|protocolo|lenguaje corporal|imagen personal|vestimenta|pedir ayuda|comportarnos|ambiente laboral'],
 'Legislación laboral, contratos y remuneraciones': [r'remuneraci|contratos|legislaci|derechos laborales|acciones legales|relaci[oó]n laboral'],
 'Inclusión (lengua de señas, accesibilidad)': [r'lengua de se[ñn]as|braill|inclusi[oó]n|discapacidad'],
 'Sin sugerencia / conforme': [r'^\W*(ninguno particular|no se|nose|non|todo bien|s[ií] muy de acuerdo|\.)\W*$', r'por el momento esta bien', r'est[aá] bien as[ií]', r'no he participado'],
}
def code(col, T):
    res = {}; tags = []
    ser = df[col]
    base = ser.notna() & (ser.astype(str).str.strip().str.len() > 1)
    for k, pats in T.items():
        m = ser.apply(lambda s: has(s, pats)); res[k] = int(m.sum())
    return res, int(ser.notna().sum())
q1, n1 = code('abi1', T1); q2, n2 = code('abi2', T2)
# 'sin sugerencia' no debe contar 'inglés' único: ajuste
R['cual'] = {'abi1_n': n1, 'abi2_n': n2, 'abi1': q1, 'abi2': q2,
             'abi1_largo_medio': float(df.abi1.dropna().str.len().mean()), 'abi2_largo_medio': float(df.abi2.dropna().str.len().mean())}
# comparación temas por práctica previa (descriptivo)
for nm, col, T in [('abi1', 'abi1', T1), ('abi2', 'abi2', T2)]:
    out = {}
    for k, pats in T.items():
        m = df[col].apply(lambda s: has(s, pats))
        out[k] = {'con': int(m[df.con_practica == 1].sum()), 'sin': int(m[df.con_practica == 0].sum())}
    R['cual'][nm + '_por_practica'] = out
df['t1_sin'] = df.abi1.apply(lambda s: has(s, T1['Sin aprendizaje claro / no sabe']))
sc = df.groupby('t1_sin').GLOBAL.mean(); R['cual']['global_si_sin_aprendizaje'] = {str(k): float(v) for k, v in sc.items()}
_a = df.loc[df.t1_sin, 'GLOBAL'].dropna(); _b = df.loc[df.abi1.notna() & ~df.t1_sin, 'GLOBAL'].dropna()
R['cual']['sin_aprendizaje_test'] = {'n_sin': len(_a), 'n_con': len(_b), 'media_sin': float(_a.mean()), 'media_con': float(_b.mean()), 'p': float(stats.mannwhitneyu(_a, _b).pvalue), 'cliff': cliffs(_a, _b)}
# citas textuales ilustrativas (anónimas, sin datos personales) — selección manual por patrones
def pick(col, pat, k=1):
    s = df[col].dropna(); s = s[s.str.contains(pat, case=False, regex=True) & (s.str.len() < 330)]
    return s.head(k).tolist()
R['citas'] = {'abi1': {'equipo': pick('abi1', r'trabajo en equipo.*comunicarse|no solo importa'), 'teoria': pick('abi1', r'no siempre lo que se ense'),
                       'inclusion': pick('abi1', r'liderazgo y la diversidad'), 'duda': pick('abi1', r'^no he tenido pr[aá]ctica|ninguno si todabia'),
                       'diseno': pick('abi1', r'diseño de trabajo')},
              'abi2': {'simul': pick('abi2', r'simulaciones en cuanto'), 'entrevista': pick('abi2', r'entrevistas por competencias'),
                       'brecha': pick('abi2', r'estudiar y hacer la practica'), 'ingles': pick('abi2', r'MUY IMPORTANTE TALLER'), 'inclusion': pick('abi2', r'lengua de se[ñn]as para los'),
                       'terreno': pick('abi2', r'salidas a áreas laborales|puertos')}}
R['texto_stats'] = {'abi1_resp': n1, 'abi2_resp': n2}


# ================= HIPÓTESIS OFICIAL (Informe Metodológico Proyecto La Puerta) =================
# Equivalencia entre el informe (COM, EQ, AUT, RES, ET) y los ítems realmente aplicados. [INTERPRETACIÓN]
df['O_COM'] = df[['P04', 'P11']].mean(axis=1); df['O_EQ'] = df['P07']; df['O_AUT'] = df[['P03', 'P08']].mean(axis=1)
df['O_RES'] = df['P13']; df['O_ET'] = df['P14']; df['O_HB'] = df[['O_COM', 'O_EQ', 'O_AUT', 'O_RES', 'O_ET']].mean(axis=1)
ON = {'O_HB': 'Índice HB (promedio de 5)', 'O_COM': 'Comunicación (P04, P11)', 'O_EQ': 'Trabajo en equipo (P07)', 'O_AUT': 'Autonomía (P03, P08)', 'O_RES': 'Resiliencia (P13)', 'O_ET': 'Ética (P14)'}
def welch(a, b):
    t = stats.ttest_ind(a, b, equal_var=False); sp = np.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    return float(t.statistic), float(t.pvalue), float((a.mean() - b.mean()) / sp)
OF = {'equiv': ON, 'filas': []}
for v in list(ON) + ['GLOBAL', 'D3', 'D5']:
    a = df.loc[df.con_practica == 1, v].dropna(); b = df.loc[df.con_practica == 0, v].dropna()
    t, p, d = welch(a, b); u, pm = stats.mannwhitneyu(a, b)
    OF['filas'].append({'var': v, 'nombre': ON.get(v, VN.get(v, v)), 'con': float(a.mean()), 'sin': float(b.mean()), 'dif': float(a.mean() - b.mean()),
        'pct': float(100 * (a.mean() - b.mean()) / b.mean()), 't': t, 'p_t': p, 'd': d, 'p_mw': float(pm),
        'ci': [float(x) for x in np.percentile([rng.choice(a, len(a)).mean() - rng.choice(b, len(b)).mean() for _ in range(4000)], [2.5, 97.5])]})
for r, ph in zip(OF['filas'], holm([r['p_mw'] for r in OF['filas']])): r['p_holm'] = ph
x = df[['GLOBAL', 'con_practica']].dropna(); rp, pp_ = stats.pearsonr(x.con_practica, x.GLOBAL); rs, ps_ = stats.spearmanr(x.con_practica, x.GLOBAL)
bs = [stats.pearsonr(x.con_practica.values[i], x.GLOBAL.values[i])[0] for i in (rng.integers(0, len(x), len(x)) for _ in range(3000))]
OF['pearson'] = {'r': float(rp), 'p': float(pp_), 'ci': [float(q) for q in np.percentile(bs, [2.5, 97.5])], 'spearman': float(rs), 'p_sp': float(ps_), 'n': len(x)}
# tipo de práctica (ID07)
tp = [df.loc[df.practica == k, 'GLOBAL'].dropna() for k in ['Sin práctica previa', 'Práctica EMTP', 'Pasantía en la carrera']]
OF['tipos_kw'] = {'H': float(stats.kruskal(*tp).statistic), 'p': float(stats.kruskal(*tp).pvalue)}
# escenarios y semáforo oficial
gm = float(df.GLOBAL.mean()); OF['media_global'] = gm
OF['escenario_por_media'] = 'Escenario 1' if gm >= 4.2 else ('Escenario 2' if gm >= 3.5 else 'Escenario 3')
OF['crit'] = {'E1_media_ge_4_2': gm >= 4.2, 'E1_r_ge_045': rp >= 0.45, 'E2_brecha_ge_08': float(OF['filas'][[r['var'] for r in OF['filas']].index('GLOBAL')]['dif']) >= 0.8,
              'E2_media_entre_35_41': 3.5 <= gm <= 4.1, 'E3_media_lt_35': gm < 3.5,
              'E3_pct_AUT_lt35': float(100 * (df.D3.dropna() < 3.5).mean()), 'E3_pct_RES_lt35': float(100 * (df.D5.dropna() < 3.5).mean()),
              'E3_pct_AUT_RES_ambos': float(100 * ((df.D3 < 3.5) & (df.D5 < 3.5)).sum() / df[['D3', 'D5']].dropna().shape[0])}
def sem_of(v): return 'Verde' if v >= 4.2 else ('Amarillo' if v >= 3.5 else 'Rojo')
df['sem_of'] = df.GLOBAL.apply(lambda v: sem_of(v) if pd.notna(v) else np.nan)
ct = pd.crosstab(df.con_practica, df.sem_of).reindex(columns=['Verde', 'Amarillo', 'Rojo'], fill_value=0)
OF['semaforo_estudiantes'] = {'total': df.sem_of.value_counts().reindex(['Verde', 'Amarillo', 'Rojo']).fillna(0).astype(int).to_dict(),
    'sin': ct.loc[0].to_dict(), 'con': ct.loc[1].to_dict()}
OF['semaforo_estudiantes']['pct_total'] = {k: float(100 * v / df.sem_of.notna().sum()) for k, v in OF['semaforo_estudiantes']['total'].items()}
chi = stats.fisher_exact([[ct.loc[1, 'Rojo'], ct.loc[1, 'Verde'] + ct.loc[1, 'Amarillo']], [ct.loc[0, 'Rojo'], ct.loc[0, 'Verde'] + ct.loc[0, 'Amarillo']]])
OF['rojo_fisher'] = {'or': float(chi.statistic), 'p': float(chi.pvalue)}
chi2 = stats.fisher_exact([[ct.loc[1, 'Verde'], ct.loc[1, 'Amarillo'] + ct.loc[1, 'Rojo']], [ct.loc[0, 'Verde'], ct.loc[0, 'Amarillo'] + ct.loc[0, 'Rojo']]])
OF['verde_fisher'] = {'or': float(chi2.statistic), 'p': float(chi2.pvalue)}
OF['semaforo_dims'] = {d: sem_of(float(df[d].mean())) for d in ['D1', 'D2', 'D3', 'D4', 'D5']}
OF['semaforo_dims_valor'] = {d: float(df[d].mean()) for d in ['D1', 'D2', 'D3', 'D4', 'D5']}
# ¿cuánta de la brecha 0,8–1,2 se observa? poder: diferencia mínima detectable (n 72 vs 112, sd)
sdp = float(df.GLOBAL.std()); OF['mde_80'] = float(2.8 * sdp * np.sqrt(1 / 72 + 1 / 112))
# sensibilidad: restringir a EMTP vs sin; y año controlado (OLS ya en ols_global)
R['OF'] = OF


# sensibilidad
sens = {}
def _h1(mask, label):
    a = df.loc[mask & (df.con_practica == 1), 'GLOBAL'].dropna(); b = df.loc[mask & (df.con_practica == 0), 'GLOBAL'].dropna()
    sens[label] = {'n': int(len(a) + len(b)), 'dif': float(a.mean() - b.mean()), 'p_mw': float(stats.mannwhitneyu(a, b).pvalue), 'media': float(pd.concat([a, b]).mean())}
sl = df[P].nunique(axis=1) == 1
_h1(pd.Series(True, index=df.index), 'Base completa'); _h1(~sl, 'Sin las 12 respuestas idénticas en todo'); _h1(df.escuela == 'Escuela de Administración y Negocios', 'Solo Administración y Negocios')
_h1(df.anio3 == '1.º–2.º sem.', 'Solo 1.º–2.º semestre'); _h1(df.n_resp >= 12, 'Con ≥ 12 ítems respondidos')
R['sens'] = sens
R['cual']['abi_n_por_practica'] = {'abi1': {'con': int(df.loc[df.con_practica == 1, 'abi1'].notna().sum()), 'sin': int(df.loc[df.con_practica == 0, 'abi1'].notna().sum())},
                                   'abi2': {'con': int(df.loc[df.con_practica == 1, 'abi2'].notna().sum()), 'sin': int(df.loc[df.con_practica == 0, 'abi2'].notna().sum())}}

# distribuciones para gráficos
R['dist_global'] = np.histogram(df.GLOBAL.dropna(), bins=np.arange(1, 5.26, 0.25))[0].tolist()
df.drop(columns=['abi1', 'abi2', 'escuela']).to_pickle(f'{OUT}/src/datos_limpios.pkl')   # sin textos ni correos
json.dump(R, open(f'{OUT}/src/resultados.json', 'w'), ensure_ascii=False, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
print('OK', N, 'global', round(R['global']['media'], 3))
