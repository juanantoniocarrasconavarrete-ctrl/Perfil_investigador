"""Auditoría independiente: recalcula las cifras clave desde la base original con un camino distinto al de analisis.py
(numpy/scipy puros, sin pandas para los cálculos) y las compara con resultados.json. Uso: python3 -I auditoria_datos.py <xlsx>"""
import sys, json, re, openpyxl, numpy as np
from scipy import stats
R = json.load(open(__file__.rsplit('/', 1)[0] + '/resultados.json'))
ws = openpyxl.load_workbook(sys.argv[1], read_only=True)['Form Responses 1']
rows = list(ws.iter_rows(values_only=True)); hdr, data = rows[0], rows[1:]
N = len(data); res = []
def chk(nombre, esperado, obtenido, tol=0.005):
    ok = abs(esperado - obtenido) <= tol; res.append((nombre, esperado, obtenido, ok)); return ok
def code(v): m = re.match(r'\s*(\d)', str(v)) if v is not None else None; x = int(m.group(1)) if m else None; return np.nan if x in (None, 0) else float(x)
P = np.array([[code(r[8 + i]) for i in range(15)] for r in data])            # 184 x 15
anio = [r[6] for r in data]; prac = [r[7] for r in data]
con = np.array([0 if str(p).startswith('No, nunca') else 1 for p in prac])
chk('N', R['N'], N, 0)
chk('consentimiento', R['consentimiento'], sum(str(r[1]).startswith('Sí') for r in data), 0)
for i in range(15):
    c = P[:, i][~np.isnan(P[:, i])]
    it = R['items'][i]
    chk(f"P{i+1:02d} n", it['n'], len(c), 0); chk(f"P{i+1:02d} media", it['media'], c.mean(), 1e-6)
    chk(f"P{i+1:02d} %fav", it['fav'], 100 * (c >= 4).mean(), 1e-6); chk(f"P{i+1:02d} %des", it['des'], 100 * (c <= 2).mean(), 1e-6)
DIMS = {'D1': [0, 1], 'D2': [2, 3, 4, 5], 'D3': [6, 7, 8, 9], 'D4': [10, 11, 14], 'D5': [12, 13]}
D = {k: np.nanmean(P[:, v], axis=1) for k, v in DIMS.items()}; glob = np.nanmean(P, axis=1)
for d in R['dims']: chk(f"{d['id']} media", d['media'], np.nanmean(D[d['id']]), 1e-6)
chk('global media', R['global']['media'], np.nanmean(glob), 1e-6)
# alfa global (listwise)
X = P[~np.isnan(P).any(axis=1)]; k = 15; alpha = k / (k - 1) * (1 - X.var(axis=0, ddof=1).sum() / X.sum(axis=1).var(ddof=1)); chk('alfa global', R['global']['alpha'], alpha, 1e-6)
# H1
a, b = glob[con == 1], glob[con == 0]
chk('n con práctica', 72, len(a), 0); chk('n sin práctica', 112, len(b), 0)
chk('dif global', R['H1'][0]['dif'], a.mean() - b.mean(), 1e-6)
u = stats.mannwhitneyu(a, b, alternative='two-sided'); chk('MW p global', R['H1'][0]['p'], u.pvalue, 1e-6)
w = stats.ttest_ind(a, b, equal_var=False); chk('Welch p global', R['OF']['filas'][[r['var'] for r in R['OF']['filas']].index('GLOBAL')]['p_t'], w.pvalue, 1e-6)
chk('Pearson práctica-global', R['OF']['pearson']['r'], np.corrcoef(con, glob)[0, 1], 1e-6)
# semáforo oficial
sem = np.where(glob >= 4.2, 'V', np.where(glob >= 3.5, 'A', 'R')); chk('verde', R['OF']['semaforo_estudiantes']['total']['Verde'], (sem == 'V').sum(), 0); chk('amarillo', R['OF']['semaforo_estudiantes']['total']['Amarillo'], (sem == 'A').sum(), 0); chk('rojo', R['OF']['semaforo_estudiantes']['total']['Rojo'], (sem == 'R').sum(), 0)
chk('rojo sin práctica', R['OF']['semaforo_estudiantes']['sin']['Rojo'], ((sem == 'R') & (con == 0)).sum(), 0); chk('rojo con práctica', R['OF']['semaforo_estudiantes']['con']['Rojo'], ((sem == 'R') & (con == 1)).sum(), 0)
# H3, H4, H5
cols = np.column_stack([D[k] for k in ['D1', 'D2', 'D3', 'D4', 'D5']]); m = ~np.isnan(cols).any(axis=1)
chk('Friedman chi2', R['H3']['chi2'], stats.friedmanchisquare(*[cols[m][:, j] for j in range(5)]).statistic, 1e-6)
ok = ~np.isnan(P[:, 8]) & ~np.isnan(P[:, 9]); chk('rho P09-P10', R['H4']['P09_P10']['rho'], stats.spearmanr(P[ok, 8], P[ok, 9])[0], 1e-6)
c15 = P[:, 14][~np.isnan(P[:, 14])]; chk('P15 favorables', R['H5']['k'], (c15 >= 4).sum(), 0)
chk('binomial p vs 70%', R['H5']['p_vs70'], stats.binomtest(int((c15 >= 4).sum()), len(c15), .7, alternative='greater').pvalue, 1e-9)
# calidad
na = int(sum(1 for r in data for i in range(15) if str(r[8 + i]).startswith('0'))); chk('celdas No sé/No aplica', R['calidad']['respuestas_NA_total'], na, 0)
sl = sum(1 for row in P if len(set(row[~np.isnan(row)])) == 1); chk('respuestas idénticas en todo', R['calidad']['straightlining_n'], sl, 0)
chk('correos duplicados', R['correos_duplicados'], len(data) - len(set(r[26] for r in data)), 0)
vac = [sum(1 for r in data if r[j] in (None, '')) for j in (2, 3, 4, 23)]; chk('campos vacíos ID02/03/04/POST_EXP1', 184 * 4, sum(vac), 0)
chk('abiertas ABI1', R['cual']['abi1_n'], sum(1 for r in data if r[24] not in (None, '')), 0); chk('abiertas ABI2', R['cual']['abi2_n'], sum(1 for r in data if r[25] not in (None, '')), 0)
bad = [r for r in res if not r[3]]
print(f'{len(res)} verificaciones · {len(res)-len(bad)} coinciden · {len(bad)} difieren')
for r in bad: print('  DIFIERE:', r)
json.dump([{'verificacion': a, 'esperado': float(b), 'recalculado': float(c), 'coincide': bool(d)} for a, b, c, d in res], open(__file__.rsplit('/', 1)[0] + '/auditoria_datos.json', 'w'), ensure_ascii=False, indent=1)
