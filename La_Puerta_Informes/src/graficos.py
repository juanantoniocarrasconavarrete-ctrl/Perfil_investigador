import json, numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import glob
for f in glob.glob('/usr/share/fonts/opentype/inter/Inter-*.otf'): fm.fontManager.addfont(f)
plt.rcParams.update({'font.family': 'Inter', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#999999', 'axes.labelcolor': '#1A1A1A', 'xtick.color': '#1A1A1A', 'ytick.color': '#1A1A1A',
                     'figure.dpi': 100, 'savefig.dpi': 200, 'savefig.bbox': 'tight', 'savefig.facecolor': 'white'})
import re
from matplotlib import text as _mt
_orig = _mt.Text.set_text
def _es(self, t):
    if isinstance(t, str): t = re.sub(r'(?<=\d)\.(?=\d)', ',', t)
    return _orig(self, t)
_mt.Text.set_text = _es
NAVY, AMB, TEAL, CORAL, GRAY, LG, SKY = '#1A1A1A', '#FFB800', '#1A1A1A', '#FFB800', '#666666', '#EEEEEE', '#666666'
MID, TINT = '#BBBBBB', '#FFD866'
SEM = {'Fortaleza': '#1A1A1A', 'Funcional': '#666666', 'En desarrollo': '#FFD866', 'Brecha': '#FFB800'}
R = json.load(open('resultados.json')); OUT = '../graficos/'
df = pd.read_pickle('datos_limpios.pkl')
IT = {i['id']: i for i in R['items']}
SHORT = {'P01': 'Conozco tareas y condiciones reales', 'P02': 'Tengo claras las exigencias de las empresas', 'P03': 'Confío en resolver algo nuevo',
 'P04': 'Explico temas técnicos con claridad', 'P05': 'Aplico lo de clases a casos reales', 'P06': 'Sé qué método sirve en la empresa',
 'P07': 'Dialogo y logro acuerdos en equipo', 'P08': 'Sé cuándo actuar solo/a y cuándo consultar', 'P09': 'He comprobado si el trabajo real calza conmigo',
 'P10': 'Me siento seguro/a de adaptarme', 'P11': 'Sé cómo contactar a profesionales', 'P12': 'Tengo una red de contactos referentes',
 'P13': 'Aprendo de mis errores', 'P14': 'Priorizo la ética bajo presión', 'P15': 'Quiero proyectos con empresas reales'}
DN = {d['id']: d['nombre'] for d in R['dims']}
def save(fig, n): fig.savefig(OUT + n + '.png'); plt.close(fig)
def title(ax, t, s=None):
    ax.set_title(t, loc='left', fontsize=13, fontweight='bold', color=NAVY, pad=18 if s else 8)
    if s: ax.text(0, 1.02, s, transform=ax.transAxes, fontsize=9, color=GRAY)

# 1 perfil
fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.4), gridspec_kw={'width_ratios': [1.2, 1.2, 0.9], 'wspace': 1.0})
a = R['perfil']['anio']; lab = ['1.º–2.º sem.', '3.º–4.º sem.', '5.º–6.º sem.', '7.º–8.º sem.']; v = [a[k] for k in lab]
b = ax[0].barh(lab[::-1], v[::-1], color=['#1A1A1A', '#666666', '#666666', '#BBBBBB'][::-1]); ax[0].bar_label(b, [f'{x} ({100*x/184:.0f} %)' for x in v[::-1]], padding=3, fontsize=9)
ax[0].set_xlim(0, 125); title(ax[0], 'Semestre en curso'); ax[0].set_xticks([])
p = R['perfil']['practica']; lab = ['Sin práctica previa', 'Práctica EMTP', 'Pasantía en la carrera', 'Práctica en otra carrera']; v = [p[k] for k in lab]
b = ax[1].barh(lab[::-1], v[::-1], color=['#FFB800', '#666666', '#666666', '#BBBBBB'][::-1][::-1][::-1]); ax[1].bar_label(b, [f'{x} ({100*x/184:.0f} %)' for x in v[::-1]], padding=3, fontsize=9)
ax[1].set_xlim(0, 160); title(ax[1], 'Práctica previa'); ax[1].set_xticks([])
ax[2].pie([181, 2, 1], colors=['#1A1A1A', '#FFB800', '#BBBBBB'], startangle=90, counterclock=False, wedgeprops=dict(width=.38, edgecolor='white'))
ax[2].text(0, 0, '98 %\nEAN', ha='center', va='center', fontsize=13, fontweight='bold', color=NAVY); title(ax[2], 'Escuela')
ax[2].legend(['Administración y Negocios (181)', 'Ingeniería y RR. NN. (2)', 'Otra área (1)'], loc='upper center', bbox_to_anchor=(.5, 0), fontsize=7.5, frameon=False)
save(fig, 'g01_perfil')

# 2 diverging items
order = sorted(R['items'], key=lambda x: x['fav'])
fig, ax = plt.subplots(figsize=(10, 6.2))
for i, x in enumerate(order):
    des, neu, fav = x['des'], x['neu'], x['fav']
    ax.barh(i, -des, color=AMB, height=.68); ax.barh(i, neu / 2, left=0, color=MID, height=.68); ax.barh(i, -neu / 2, left=-des, color=MID, height=.68)
    ax.barh(i, fav, left=neu / 2, color=TEAL, height=.68)
    ax.text(neu / 2 + fav + 1.5, i, f'{fav:.0f} %', va='center', fontsize=9, fontweight='bold', color=NAVY)
    ax.text(-des - neu / 2 - 1.5, i, f'{des:.0f} %', va='center', ha='right', fontsize=8.5, color=GRAY)
ax.set_yticks(range(len(order))); ax.set_yticklabels([f"{x['id']}  {SHORT[x['id']]}" for x in order], fontsize=9)
ax.axvline(0, color='#555', lw=.8); ax.set_xlim(-60, 130); ax.set_xticks([])
for s in ['left', 'bottom']: ax.spines[s].set_visible(False)
ax.tick_params(left=False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=AMB, label='En desacuerdo (1–2)'), Patch(color=MID, label='Neutral (3)'), Patch(color=TEAL, label='De acuerdo (4–5)')], loc='lower right', frameon=False, fontsize=9)
title(ax, 'Cómo respondieron los 184 estudiantes, afirmación por afirmación', 'Cifras en negro: % de acuerdo o muy de acuerdo; en gris: % en desacuerdo')
save(fig, 'g02_items')

# 3 dimensiones
fig, ax = plt.subplots(figsize=(9.5, 4.2))
ds = sorted(R['dims'], key=lambda d: d['media'])
for i, d in enumerate(ds):
    ax.hlines(i, d['ci'][0], d['ci'][1], color=GRAY, lw=3, zorder=1); ax.scatter(d['media'], i, s=230, color=SEM[d['semaforo']], zorder=3, edgecolor='white', lw=1.5)
    ax.text(d['media'], i + .33, f"{d['media']:.2f}", ha='center', fontsize=10, fontweight='bold', color=NAVY)
    ax.text(5.12, i, f"{d['fav']:.0f} % de acuerdo", va='center', fontsize=9, color=NAVY)
ax.axvline(R['global']['media'], color=NAVY, ls='--', lw=1); ax.text(R['global']['media'] - .02, -.62, f"Promedio global {R['global']['media']:.2f}", ha='right', fontsize=8.5, color=NAVY); ax.set_ylim(-.8, len(ds) - .3)
ax.set_yticks(range(len(ds))); ax.set_yticklabels([f"{d['id']} · {d['nombre']}" for d in ds]); ax.set_xlim(3, 5.1); ax.set_xlabel('Promedio (1 a 5)  ·  barra gris: margen de error del 95 %')
title(ax, 'Las cinco dimensiones del estudio', 'Relleno según el % de acuerdo: negro ≥ 80 · gris 70–79 · amarillo claro 60–69 · amarillo < 60')
save(fig, 'g03_dimensiones')

# 4 hist global
fig, ax = plt.subplots(figsize=(8, 3.6))
g = df.GLOBAL.dropna(); n, bins, pat = ax.hist(g, bins=np.arange(1.75, 5.1, .25), color=SKY, edgecolor='white')
for p_, l in zip(pat, bins[:-1]): p_.set_facecolor(AMB if l < 3 else (GRAY if l < 4 else TEAL))
ax.axvline(g.mean(), color=NAVY, ls='--'); ax.text(g.mean() + .05, n.max() * .95, f'Promedio {g.mean():.2f}', color=NAVY, fontsize=9)
ax.set_xlabel('Puntaje global de cada estudiante (1 a 5)'); ax.set_ylabel('Estudiantes')
title(ax, 'Distribución del puntaje global', f"{R['perfiles_pct']['Sólido (≥4)']:.0f} % sólido (≥ 4) · {R['perfiles_pct']['Intermedio (3–3,99)']:.0f} % intermedio · {R['perfiles_pct']['Por fortalecer (<3)']:.0f} % por fortalecer (< 3)")
save(fig, 'g04_global_hist')

# 5 semáforo
fig, ax = plt.subplots(figsize=(9.5, 5.6)); o = sorted(R['items'], key=lambda x: x['fav'])
ax.barh(range(15), [x['fav'] for x in o], color=[SEM[x['semaforo']] for x in o], height=.7)
for i, x in enumerate(o): ax.text(x['fav'] + 1, i, f"{x['fav']:.0f} %", va='center', fontsize=9, fontweight='bold', color=NAVY)
ax.axvline(70, color=NAVY, ls='--', lw=1); ax.text(70.5, 15, 'Meta 70 %', fontsize=8.5, color=NAVY, va='bottom')
ax.set_yticks(range(15)); ax.set_yticklabels([f"{x['id']}  {SHORT[x['id']]}" for x in o], fontsize=9); ax.set_xlim(0, 100); ax.set_xlabel('% de estudiantes de acuerdo o muy de acuerdo')
ax.legend(handles=[Patch(color=SEM[k], label=k) for k in SEM], loc='lower right', frameon=False, fontsize=9)
title(ax, 'Semáforo de resultados frente a la meta de 70 %', 'La meta se alinea con la exigencia del 70 % usada en las rúbricas DUOC (criterio propuesto por el equipo analista)')
save(fig, 'g05_semaforo')

# 6 práctica dumbbell
fig, ax = plt.subplots(figsize=(9, 4.2)); H1 = {r['var']: r for r in R['H1']}
vars_ = ['D1', 'D2', 'D3', 'D4', 'D5', 'GLOBAL']
for i, v in enumerate(vars_[::-1]):
    r = H1[v]; ax.plot([r['media_sin'], r['media_con']], [i, i], color='#CCCCCC', lw=4, zorder=1)
    ax.scatter(r['media_sin'], i, s=120, color=CORAL, zorder=3); ax.scatter(r['media_con'], i, s=120, color=TEAL, zorder=3)
    ax.text(5.0, i, f"+{r['dif']:.2f}  (p = {r['p']:.2f})", va='center', fontsize=9, color=NAVY)
ax.set_yticks(range(6)); ax.set_yticklabels([('Global' if v == 'GLOBAL' else f'{v} · {DN[v]}') for v in vars_[::-1]]); ax.set_xlim(3.4, 5.4)
ax.legend(handles=[plt.Line2D([], [], marker='o', color='w', markerfacecolor=CORAL, markersize=9, label=f"Sin práctica previa (n={R['H1'][0]['n_sin']})"),
                   plt.Line2D([], [], marker='o', color='w', markerfacecolor=TEAL, markersize=9, label=f"Con práctica previa (n={R['H1'][0]['n_con']})")], loc='upper left', frameon=False, fontsize=9, bbox_to_anchor=(0, -.12), ncol=2)
title(ax, 'Quienes ya hicieron una práctica puntúan algo más alto…', '…pero las diferencias son pequeñas y no resisten la corrección por comparaciones múltiples')
save(fig, 'g06_practica')

# 7 año
fig, ax = plt.subplots(figsize=(8.5, 4.2)); x = [0, 1, 2]; sty = {'D1': ('#1A1A1A', '-', 'o'), 'D2': ('#666666', '-', 's'), 'D3': ('#1A1A1A', '--', '^'), 'D4': ('#FFB800', '-', 'D'), 'D5': ('#666666', '--', 'v')}
for d, (c, ls, mk) in sty.items():
    y = R['dim_anio'][d]; ax.plot(x, y, marker=mk, color=c, ls=ls, lw=2.4, label=f'{d} · {DN[d]}')
    ax.text(2.05, y[2] + {'D1': -.025, 'D3': .025}.get(d, 0), d, color='#1A1A1A', fontsize=9, va='center', fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels([f"1.º–2.º sem.\n(n={R['H2'][0]['ns'][0]})", f"3.º–4.º sem.\n(n={R['H2'][0]['ns'][1]})", f"5.º sem. o más\n(n={R['H2'][0]['ns'][2]})"])
ax.set_ylim(3.4, 4.4); ax.set_ylabel('Promedio (1 a 5)'); ax.legend(frameon=False, fontsize=8, loc='upper left', bbox_to_anchor=(1.03, 1))
title(ax, 'Las dimensiones según el año de estudio', 'Sin una escalera clara: el tramo de 3.º–4.º semestre baja y el de 5.º en adelante repunta')
save(fig, 'g07_anio')

# 8 correlaciones items
fig, ax = plt.subplots(figsize=(8.2, 6.8)); C = np.array(R['corr_items']); im = ax.imshow(C, cmap='Greys', vmin=-.2, vmax=.9)
ax.set_xticks(range(15)); ax.set_yticks(range(15)); ax.set_xticklabels([f'P{i:02d}' for i in range(1, 16)], rotation=90, fontsize=8); ax.set_yticklabels([f'P{i:02d}' for i in range(1, 16)], fontsize=8)
for i in range(15):
    for j in range(15):
        if i != j: ax.text(j, i, f'{C[i,j]:.2f}'[1:] if C[i, j] >= 0 else f'{C[i,j]:.2f}', ha='center', va='center', fontsize=6, color='white' if C[i, j] > .5 else '#1A1A1A')
for s in ax.spines.values(): s.set_visible(False)
cb = plt.colorbar(im, shrink=.7); cb.set_label('Correlación de Spearman')
title(ax, 'Qué afirmaciones se mueven juntas')
save(fig, 'g08_correlaciones')

# 9 P09 x P10
fig, ax = plt.subplots(figsize=(6.4, 4.8)); d = df[['P09', 'P10']].dropna(); ct = pd.crosstab(d.P10, d.P09).reindex(index=[5, 4, 3, 2, 1], columns=[1, 2, 3, 4, 5], fill_value=0)
ctp = ct.div(ct.sum(axis=0), axis=1) * 100
im = ax.imshow(ctp.values, cmap='Greys', vmin=0, vmax=75)
for i in range(5):
    for j in range(5): ax.text(j, i, f'{ct.values[i,j]}', ha='center', va='center', fontsize=10, color='white' if ctp.values[i, j] > 40 else NAVY, fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels([1, 2, 3, 4, 5]); ax.set_yticks(range(5)); ax.set_yticklabels([5, 4, 3, 2, 1])
ax.set_xlabel('P09 · He comprobado si el trabajo real calza con mis intereses'); ax.set_ylabel('P10 · Me siento seguro/a de adaptarme')
for s in ax.spines.values(): s.set_visible(False)
title(ax, 'Quien probó el mundo laboral se siente más seguro', f"Número de estudiantes por casilla (color = % dentro de cada columna) · rho = {R['H4']['P09_P10']['rho']:.2f}")
save(fig, 'g09_p09_p10')

# 10/11 cualitativo
def barq(d, n, tit, sub, name, col):
    items = sorted(d.items(), key=lambda kv: kv[1]); fig, ax = plt.subplots(figsize=(9.5, 4.4))
    b = ax.barh([k for k, _ in items], [v for _, v in items], color=[MID if 'Sin ' in k else col for k, _ in items], height=.68)
    ax.bar_label(b, [f'{v}  ({100*v/n:.0f} %)' for _, v in items], padding=3, fontsize=9, color=NAVY); ax.set_xlim(0, max(d.values()) * 1.3); ax.set_xticks([])
    for s in ['left', 'bottom']: ax.spines[s].set_visible(False)
    ax.tick_params(left=False); title(ax, tit, sub); save(fig, name)
barq(R['cual']['abi1'], R['cual']['abi1_n'], 'Lo más valioso que aprendieron este semestre', f"{R['cual']['abi1_n']} respuestas · una respuesta puede tocar más de un tema", 'g10_abi1', '#1A1A1A')
barq(R['cual']['abi2'], R['cual']['abi2_n'], 'Qué apoyo pedirían antes de la práctica', f"{R['cual']['abi2_n']} respuestas · una respuesta puede tocar más de un tema", 'g11_abi2', '#666666')

# 12 box por dimensión
fig, ax = plt.subplots(figsize=(9, 4.2)); dat = [df[d].dropna() for d in ['D1', 'D2', 'D3', 'D4', 'D5']]
bp = ax.boxplot(dat, vert=True, patch_artist=True, widths=.55, medianprops=dict(color=NAVY, lw=2), flierprops=dict(marker='o', markersize=3, markerfacecolor=GRAY, alpha=.5, markeredgecolor='none'))
for p_, c in zip(bp['boxes'], [MID, MID, MID, AMB, MID]): p_.set_facecolor(c); p_.set_alpha(1); p_.set_edgecolor('#666666')
for i, dd in enumerate(dat): ax.scatter(i + 1, dd.mean(), marker='D', color='white', edgecolor=NAVY, zorder=5, s=36)
ax.set_xticks(range(1, 6)); ax.set_xticklabels([f"{d}\n{DN[d].split(' y ')[0].replace('Conocer el ','').replace('Redes e interés por vincularse','Redes e interés')}" for d in ['D1', 'D2', 'D3', 'D4', 'D5']], fontsize=8.5)
ax.set_ylabel('Promedio por estudiante'); title(ax, 'Redes (D4) queda más abajo que las demás dimensiones', 'Caja = 50 % central · línea = mediana · rombo = promedio')
save(fig, 'g12_cajas')

# 13 forest H4 (beta estandarizados)
fig, ax = plt.subplots(figsize=(8, 3.6)); bs = R['H4']['beta_std']; lab = {'P05': 'P05 · Aplico lo de clases a casos reales', 'P01': 'P01 · Conozco tareas y condiciones reales', 'P09': 'P09 · He comprobado si el trabajo calza conmigo', 'P12': 'P12 · Tengo red de contactos'}
ks = sorted(bs, key=lambda k: bs[k]); ax.barh([lab[k] for k in ks], [bs[k] for k in ks], color=[NAVY if R['H4']['ols'][k]['p'] < .05 else MID for k in ks], height=.6)
for i, k in enumerate(ks): ax.text(bs[k] + .008, i, f"β = {bs[k]:.2f}", va='center', fontsize=9, color=NAVY)
ax.set_xlim(0, .38); ax.set_xlabel('Peso relativo para explicar «me siento seguro/a de adaptarme» (P10)')
title(ax, 'Qué se asocia más con la seguridad para adaptarse', f"Negro: asociación estadísticamente clara · gris claro: dudosa · el modelo explica ≈ {100*R['H4']['ols']['r2']:.0f} % de la variación")
save(fig, 'g13_h4')

# 16 desglose redes
fig, ax = plt.subplots(figsize=(9, 3.4))
for i, p in enumerate(['P15', 'P11', 'P12']):
    x = IT[p]; ax.barh(i, -x['des'], color=AMB, height=.55); ax.barh(i, x['neu'] / 2, color=MID, height=.55); ax.barh(i, -x['neu'] / 2, left=-x['des'], color=MID, height=.55); ax.barh(i, x['fav'], left=x['neu'] / 2, color=TEAL, height=.55)
    ax.text(x['neu'] / 2 + x['fav'] + 1.5, i, f"{x['fav']:.0f} %", va='center', fontweight='bold', color=NAVY); ax.text(-x['des'] - x['neu'] / 2 - 1.5, i, f"{x['des']:.0f} %", va='center', ha='right', color=GRAY)
ax.set_yticks(range(3)); ax.set_yticklabels([f'P15 · {SHORT["P15"]}', f'P11 · {SHORT["P11"]}', f'P12 · {SHORT["P12"]}']); ax.axvline(0, color='#555', lw=.8); ax.set_xticks([]); ax.set_xlim(-65, 125)
for s in ['left', 'bottom']: ax.spines[s].set_visible(False)
title(ax, 'Dentro de D4: mucho interés, poca red', 'Quieren vincularse con empresas (P15), pero todavía no tienen a quién recurrir (P12)')
save(fig, 'g16_redes')

# 19 ABI2 por práctica
fig, ax = plt.subplots(figsize=(9.5, 4.2)); q = R['cual']['abi2_por_practica']; ks = [k for k in q if not k.startswith('Sin')]; ks = sorted(ks, key=lambda k: q[k]['con'] + q[k]['sin'])
y = np.arange(len(ks)); ax.barh(y + .2, [100 * q[k]['sin'] / 76 if False else q[k]['sin'] for k in ks], .38, color=CORAL, label='Sin práctica previa'); ax.barh(y - .2, [q[k]['con'] for k in ks], .38, color=TEAL, label='Con práctica previa')
ax.set_yticks(y); ax.set_yticklabels([k.split(' (')[0] for k in ks], fontsize=9); ax.legend(frameon=False, fontsize=9, loc='lower right'); ax.set_xlabel('Número de menciones')
title(ax, 'Lo que piden quienes no han hecho práctica vs. quienes sí', 'Quien no la ha hecho pide terreno y simulación; quien sí, habilidades de comunicación')
save(fig, 'g19_abi2_practica')

# 17 donut perfiles
fig, ax = plt.subplots(figsize=(4.6, 4.2)); pf = R['perfiles']; vals = [pf['Por fortalecer (<3)'], pf['Intermedio (3–3,99)'], pf['Sólido (≥4)']]
ax.pie(vals, colors=[AMB, GRAY, TEAL], startangle=90, counterclock=False, wedgeprops=dict(width=.4, edgecolor='white'), labels=[f'{v}\n{l}' for v, l in zip(vals, ['Por fortalecer', 'Intermedio', 'Sólido'])], textprops=dict(fontsize=9))
ax.text(0, 0, f"{R['global']['media']:.2f}\npromedio", ha='center', va='center', fontsize=14, fontweight='bold', color=NAVY); save(fig, 'g17_perfiles')

# 18 brechas vs meta 70
fig, ax = plt.subplots(figsize=(9.5, 4.8)); o = sorted(R['items'], key=lambda x: x['fav'])[:8][::-1]
for i, x in enumerate(o):
    ax.barh(i, 70, color=LG, height=.6, edgecolor='#CCCCCC'); ax.barh(i, min(x['fav'], 70), color=SEM[x['semaforo']], height=.6)
    gap = 70 - x['fav']; ax.text(71, i, (f'faltan {gap:.0f} pts' if gap > 0 else 'meta lograda'), va='center', fontsize=9, color=NAVY, fontweight='bold'); ax.text(x['fav'] - 1, i, f"{x['fav']:.0f} %", va='center', ha='right', fontsize=9, color='white' if SEM[x['semaforo']] in ('#1A1A1A','#666666') else NAVY, fontweight='bold')
ax.set_yticks(range(len(o))); ax.set_yticklabels([f"{x['id']}  {SHORT[x['id']]}" for x in o], fontsize=9); ax.set_xlim(0, 90); ax.set_xticks([])
for s in ['left', 'bottom']: ax.spines[s].set_visible(False)
title(ax, 'Las 8 brechas frente a la meta de 70 %', 'Distancia (en puntos porcentuales) entre el % de acuerdo y la meta')
save(fig, 'g18_brechas')

# 14 marco conceptual (diagrama)
fig, ax = plt.subplots(figsize=(11, 4.6)); ax.axis('off'); ax.set_xlim(0, 11); ax.set_ylim(0, 4.6)
def box(x, y, w, h, t, c, fs=9.5, tc='white'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.15', fc=c, ec='none')); ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=fs, color=tc, fontweight='bold', wrap=True)
box(.05, 1.7, 2.2, 1.2, 'Práctica previa\ny vínculo con la\nempresa (La Puerta)', NAVY, 9.5)
ds_ = [('D1', 'Conocer el rol\nprofesional', '#666666', 3.6), ('D2', 'Transferir lo\naprendido', '#1A1A1A', 2.75), ('D3', 'Autoeficacia\nlaboral', '#666666', 1.9), ('D4', 'Redes e interés\npor vincularse', '#FFB800', 1.05), ('D5', 'Aprender del error\ny ética', '#1A1A1A', .2)]
for d, t, c, y in ds_:
    box(3.4, y, 2.7, .72, f'{d} · {t.replace(chr(10), " ")}', c, 8.5, 'white' if d != 'D4' else NAVY)
    ax.add_patch(FancyArrowPatch((2.25, 2.3), (3.38, y + .36), arrowstyle='-|>', mutation_scale=10, color=GRAY, lw=1, connectionstyle='arc3,rad=0'))
box(7.0, 1.7, 1.9, 1.2, 'Seguridad para\nadaptarse a\nun puesto (P10)', '#666666', 9.5)
for y in [3.96, 3.11, 2.26, 1.41, .56]: ax.add_patch(FancyArrowPatch((6.15, y), (6.95, 2.3), arrowstyle='-|>', mutation_scale=10, color=GRAY, lw=1))
box(9.2, 1.7, 1.7, 1.2, 'Empleabilidad\ny práctica\nprofesional', NAVY, 9.5)
ax.add_patch(FancyArrowPatch((8.93, 2.3), (9.17, 2.3), arrowstyle='-|>', mutation_scale=9, color=NAVY, lw=1.5, shrinkA=0, shrinkB=0))
ax.text(5.5, 4.45, 'Marco del estudio: 15 afirmaciones agrupadas en 5 dimensiones', ha='center', fontsize=11, color=NAVY, fontweight='bold'); save(fig, 'g14_marco')

# 20 diseño futuro pre-post
fig, ax = plt.subplots(figsize=(11, 3.2)); ax.axis('off'); ax.set_xlim(0, 11); ax.set_ylim(0, 3.2)
steps = [('1  Código único\nANTES de aplicar', '#1A1A1A'), ('2  Pretest\n(semana 1)', '#666666'), ('3  Intervención\nLa Puerta', '#1A1A1A'), ('4  Postest\n(semana final)', '#666666'), ('5  Comparar con\ngrupo control', '#FFB800')]
for i, (t, c) in enumerate(steps):
    box(.1 + i * 2.15, 1.1, 1.85, 1.1, t, c, 9.5, 'white' if c != '#FFB800' else NAVY)
    if i < 4: ax.add_patch(FancyArrowPatch((1.98 + i * 2.15, 1.65), (2.22 + i * 2.15, 1.65), arrowstyle='-|>', mutation_scale=12, color=NAVY, lw=2))
ax.text(5.5, 2.85, 'Qué falta para medir el efecto real de La Puerta', ha='center', fontsize=11, color=NAVY, fontweight='bold')
ax.text(5.5, .55, 'Campos que hoy están vacíos: Código_Estudiante · Momento_Medición · Grupo_Asignación · POST_EXP1', ha='center', fontsize=9, color=GRAY)
save(fig, 'g20_diseno_futuro')

# 15 resumen hipótesis (tabla visual)
H = [('H1', 'Hipótesis central: la práctica previa amortigua la transición', 'Parcial', AMB, f"+{R['H1'][0]['dif']:.2f} pts (esperado 0,8–1,2); r = {R['OF']['pearson']['r']:.2f}"),
     ('H2', 'A más semestres, mayor percepción', 'No respaldada', '#666666', f"p ajustado = {R['H2'][0]['p_holm']:.2f}; sin escalera"),
     ('H3', 'Redes (D4) es la dimensión más débil', 'Respaldada', '#1A1A1A', f"P12 = {IT['P12']['media']:.2f} (el más bajo); p < 0,001"),
     ('H4', 'Conocer y probar el trabajo → más seguridad', 'Respaldada', '#1A1A1A', f"rho = {R['H4']['P09_P10']['rho']:.2f}–{R['H4']['D1_P10']['rho']:.2f}; R² ≈ {100*R['H4']['ols']['r2']:.0f} %"),
     ('H5', 'Alto interés en proyectos reales (> 70 %)', 'Respaldada', '#1A1A1A', f"{R['H5']['fav']:.0f} % de acuerdo; p < 0,001"),
     ('H6', 'La Puerta mejora el pre-post vs. control', 'No evaluable', '#BBBBBB', 'Sin código, momento ni grupo')]
fig, ax = plt.subplots(figsize=(12.6, 4.4)); ax.axis('off'); ax.set_xlim(0, 12.2); ax.set_ylim(0, 6.6)
for i, (k, t, v, c, e) in enumerate(H):
    y = 5.8 - i * 1.0; ax.add_patch(FancyBboxPatch((.05, y - .35), 12.1, .8, boxstyle='round,pad=0.01,rounding_size=0.1', fc='#EEEEEE', ec='none'))
    ax.text(.3, y + .05, k, fontsize=13, fontweight='bold', color=NAVY, va='center'); ax.text(1.1, y + .05, t, fontsize=10, color=NAVY, va='center')
    ax.add_patch(FancyBboxPatch((6.4, y - .22), 1.75, .5, boxstyle='round,pad=0.01,rounding_size=0.2', fc=c, ec='none')); ax.text(7.275, y + .03, v, fontsize=8.5, color='white' if c in ('#666666','#1A1A1A') else NAVY, ha='center', va='center', fontweight='bold')
    ax.text(8.35, y + .05, e, fontsize=8.3, color='#2B3548', va='center')
save(fig, 'g15_hipotesis')

# 21 criterios oficiales vs observado
O = R['OF']; fig, ax = plt.subplots(figsize=(10, 4.6)); gl = [r for r in O['filas'] if r['var'] == 'GLOBAL'][0]
rows = [('Promedio de la cohorte', f"{O['media_global']:.2f}", 'Esc. 1: ≥ 4,20 · Esc. 2: 3,50–4,10', 'Esc. 2 (mixto)', '#FFB800'),
        ('Correlación práctica previa ↔ índice global (r)', f"{O['pearson']['r']:.2f}", 'Esc. 1: r ≥ 0,45 (p < 0,01)', 'No se cumple', '#666666'),
        ('Brecha con vs. sin práctica (puntos)', f"+{gl['dif']:.2f}  [{gl['ci'][0]:.2f} a {gl['ci'][1]:.2f}]", 'Esc. 2: 0,8 a 1,2 (p < 0,001)', 'No se cumple', '#666666'),
        ('Estudiantes < 3,5 en Autonomía', f"{O['crit']['E3_pct_AUT_lt35']:.0f} %", 'Esc. 3: > 40 %', 'No se activa', '#1A1A1A'),
        ('Estudiantes < 3,5 en Resiliencia/error', f"{O['crit']['E3_pct_RES_lt35']:.0f} %", 'Esc. 3: > 40 %', 'No se activa', '#1A1A1A')]
ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 6.9)
for h, x in [('Criterio del Informe Metodológico', .1), ('Observado', 4.1), ('Umbral del informe', 5.9), ('Lectura', 8.5)]: ax.text(x, 5.8, h, fontsize=9, fontweight='bold', color=GRAY)
for i, (a_, b_, c_, d_, col) in enumerate(rows):
    y = 4.8 - i * 1.0; ax.add_patch(FancyBboxPatch((0, y - .4), 10, .8, boxstyle='round,pad=0.01,rounding_size=0.1', fc='#EEEEEE', ec='none'))
    ax.text(.15, y, a_, fontsize=9.5, color=NAVY, va='center'); ax.text(4.1, y, b_, fontsize=10, color=NAVY, fontweight='bold', va='center'); ax.text(5.9, y, c_, fontsize=8.8, color='#2B3548', va='center')
    ax.add_patch(FancyBboxPatch((8.45, y - .2), 1.45, .4, boxstyle='round,pad=0.01,rounding_size=0.15', fc=col, ec='none')); ax.text(9.17, y, d_, fontsize=8, color='white' if col != '#FFB800' else NAVY, ha='center', va='center', fontweight='bold')
ax.text(0, 6.85, 'Qué esperaba el proyecto y qué muestran los datos', fontsize=13, fontweight='bold', color=NAVY, va='top')
save(fig, 'g21_criterios')

# 22 semáforo oficial con/sin práctica
fig, ax = plt.subplots(figsize=(8.6, 3.8)); S = O['semaforo_estudiantes']; col = {'Verde': '#1A1A1A', 'Amarillo': '#FFB800', 'Rojo': '#666666'}
for i, (k, lab) in enumerate([('sin', 'Sin práctica previa'), ('con', 'Con práctica previa')]):
    tot = sum(S[k].values()); left = 0
    for c in ['Verde', 'Amarillo', 'Rojo']:
        w = 100 * S[k][c] / tot; ax.barh(1 - i, w, left=left, color=col[c], height=.55); ax.text(left + w / 2, 1 - i, f'{w:.0f} %', ha='center', va='center', color='white' if c != 'Amarillo' else NAVY, fontweight='bold'); left += w
ax.set_yticks([1, 0]); ax.set_yticklabels([f'Sin práctica previa\n(n={sum(S["sin"].values())})', f'Con práctica previa\n(n={sum(S["con"].values())})']); ax.set_xticks([]); ax.set_xlim(0, 100)
for s_ in ['left', 'bottom']: ax.spines[s_].set_visible(False)
ax.legend(handles=[Patch(color=col['Verde'], label='Semáforo verde ≥ 4,20 (negro)'), Patch(color=col['Amarillo'], label='Amarillo 3,50–4,19'), Patch(color=col['Rojo'], label='Rojo < 3,50 (gris)')], loc='upper center', bbox_to_anchor=(.5, -.02), ncol=3, frameon=False, fontsize=9)
title(ax, 'Semáforo oficial del proyecto, por estudiante', f"Rojos: {100*S['con']['Rojo']/sum(S['con'].values()):.0f} % con práctica vs. {100*S['sin']['Rojo']/sum(S['sin'].values()):.0f} % sin práctica (p = {O['rojo_fisher']['p']:.2f})")
save(fig, 'g22_semaforo_oficial')
print('ok')

# 23 matriz de prioridad
fig, ax = plt.subplots(figsize=(9, 5.6))
RECS = [('R1', 'Rediseñar la medición\n(código, momento, grupo)', 1.2, 4.8, NAVY), ('R2', 'Programa de redes\n(mentorías, ferias)', 2.9, 4.6, '#1A1A1A'), ('R3', 'Microexperiencias reales\n(visitas, simulación)', 3.0, 4.2, '#1A1A1A'),
        ('R4', 'Focalizar por semáforo rojo', 1.6, 3.7, '#666666'), ('R5', 'Taller de comunicación', 1.9, 3.1, '#666666'), ('R6', 'Inglés y herramientas\n(ERP, Excel, BI)', 4.3, 3.3, AMB), ('R7', 'Atender el valle\nde 3.º–4.º semestre', 2.6, 2.7, AMB), ('R8', 'Validar respuestas abiertas\n(doble codificación)', 1.0, 2.0, GRAY)]
ax.axhline(3.5, color='#CCCCCC', lw=1, ls='--'); ax.axvline(2.75, color='#CCCCCC', lw=1, ls='--')
for k, t, x, y, c in RECS:
    ax.scatter(x, y, s=620, color=c, zorder=3, edgecolor='white', lw=2); ax.text(x, y, k, ha='center', va='center', color='white' if c != AMB else NAVY, fontweight='bold', fontsize=10, zorder=4)
    ax.text(x + .22, y, t, va='center', fontsize=8.5, color=NAVY)
ax.set_xlim(.5, 5.4); ax.set_ylim(1.5, 5.4); ax.set_xticks([]); ax.set_yticks([])
ax.text(.55, 5.3, 'HACER YA', fontsize=9, color=NAVY, fontweight='bold'); ax.text(2.8, 5.3, 'PROYECTOS ESTRATÉGICOS', fontsize=9, color=NAVY, fontweight='bold'); ax.text(.55, 1.6, 'AJUSTES RÁPIDOS', fontsize=9, color=GRAY, fontweight='bold'); ax.text(2.8, 1.6, 'EVALUAR / DEJAR PARA DESPUÉS', fontsize=9, color=GRAY, fontweight='bold')
ax.set_xlabel('Esfuerzo y costo  →'); ax.set_ylabel('Impacto esperado  →')
title(ax, 'Matriz de priorización de las recomendaciones', 'Juicio del equipo analista; no es un cálculo. Debe validarse con las jefaturas de carrera.')
save(fig, 'g23_prioridad')

# 24 cronograma referencial
fig, ax = plt.subplots(figsize=(11, 5.2))
M = ['Nov 26', 'Dic', 'Ene 27', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
T = [('R1 · Rediseñar instrumento y base (código, momento, grupo, A03/A04)', 0, 2, NAVY), ('R8 · Validar respuestas abiertas (doble codificación)', 0, 1, GRAY), ('R4 · Identificar y acompañar al grupo en semáforo rojo', 1, 9, SKY),
     ('R1 · Pretest (semanas 1–3 de marzo)', 4, 5, NAVY), ('R2 · Programa de redes (mentorías, ferias, charlas)', 4, 9, TEAL), ('R3 · Microexperiencias de contacto real (visitas, simulaciones)', 5, 9, TEAL),
     ('R5 · Taller de comunicación y presentación profesional', 5, 8, SKY), ('R1 · Postest y comparación con grupo de control', 8, 9.6, NAVY), ('R6 · Piloto de inglés y herramientas (ERP, Excel, BI)', 9, 13, AMB),
     ('R7 · Actividades para 3.º–4.º semestre (si se confirma el valle)', 9, 13, AMB), ('Informe de evaluación y decisión de escalamiento', 12, 14, CORAL)]
for i, (t, a, b, c) in enumerate(T):
    ax.barh(len(T) - 1 - i, b - a, left=a, color=c, height=.55, zorder=3); ax.text(-.2, len(T) - 1 - i, t, ha='right', va='center', fontsize=8.6, color=NAVY)
ax.set_xlim(0, 14); ax.set_ylim(-.7, len(T) - .3); ax.set_yticks([]); ax.set_xticks(np.arange(14) + .5); ax.set_xticklabels(M, fontsize=8.5)
for x in [2, 4, 9]: ax.axvline(x, color='#CCCCCC', lw=1, ls='--', zorder=1)
ax.text(1, len(T) - .25, 'Fase 0\nPreparación', ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=GRAY); ax.text(6.5, len(T) - .25, 'Fase 1 · 1.er semestre 2027\nPiloto con medición', ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=TEAL); ax.text(11.5, len(T) - .25, 'Fase 2 · 2.º semestre 2027\nExpansión y evaluación', ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=NAVY)
ax.set_ylim(-.7, len(T) + .7); ax.spines['left'].set_visible(False); ax.xaxis.grid(False)
title(ax, 'Cronograma referencial (14 meses)', 'Calendario tentativo alineado al año académico; las fechas exactas deben validarse con la Dirección de Escuela')
save(fig, 'g24_cronograma')
