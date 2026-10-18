import json, subprocess, re, os, html
from PIL import Image
R = json.load(open('resultados.json')); OFR = R['OF']; N = R['N']
OUT = '../infografias/'; CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
if not os.path.exists(CHROME):
    import glob; CHROME = (glob.glob('/opt/pw-browsers/chromium-1194/*/chrome') or ['/opt/pw-browsers/chromium/chrome'])[0]
def n(x, d=2): return f'{x:.{d}f}'.replace('.', ',')
def pc(x, d=0): return n(x, d) + ' %'
IT = {i['id']: i for i in R['items']}; DM = {d['id']: d for d in R['dims']}; Q = R['cual']; fo = {r['var']: r for r in OFR['filas']}; H2 = {r['var']: r for r in R['H2']}; h4 = R['H4']; h5 = R['H5']; S = OFR['semaforo_estudiantes']
NAVY, AMB, TEAL, CORAL, GRAY, SKY, GREEN = '#1B2A49', '#F2A900', '#1F8A8A', '#E4572E', '#8892A6', '#4C8BD6', '#1F8A5B'
SHORT = {'P01': 'Conozco las tareas reales', 'P02': 'Tengo claras las exigencias', 'P03': 'Confío ante una tarea nueva', 'P04': 'Explico lo técnico con claridad', 'P05': 'Aplico lo de clases a casos reales', 'P06': 'Sé qué método sirve en la empresa',
         'P07': 'Dialogo y logro acuerdos', 'P08': 'Sé cuándo actuar solo/a o consultar', 'P09': 'Comprobé que el trabajo calza conmigo', 'P10': 'Me siento seguro/a de adaptarme', 'P11': 'Sé cómo contactar profesionales', 'P12': 'Tengo red de contactos', 'P13': 'Aprendo de mis errores', 'P14': 'Priorizo la ética bajo presión', 'P15': 'Quiero proyectos con empresas'}
CSS = '''
html{background:#1B2A49}*{box-sizing:border-box;margin:0;padding:0}body{font-family:Inter,"Noto Color Emoji",sans-serif;background:#F1F4FA;color:#1B2A49;width:1200px;-webkit-font-smoothing:antialiased}
.wrap{padding:0 48px 0}
.hero{background:linear-gradient(135deg,#1B2A49 0%,#26406e 100%);color:#fff;padding:54px 48px 46px;position:relative;overflow:hidden;min-height:330px}
.hero .kicker{color:#F2A900;font-weight:800;letter-spacing:.14em;font-size:15px;text-transform:uppercase}
.hero h1{font-size:50px;line-height:1.08;font-weight:900;margin:14px 0 14px;max-width:760px;letter-spacing:-.02em}
.hero p{font-size:20px;color:#D5DCEC;max-width:700px;line-height:1.4}
.chips{display:flex;gap:10px;margin-top:24px;flex-wrap:wrap}.chip{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);border-radius:30px;padding:8px 16px;font-size:15px;font-weight:600}
.arch{position:absolute;right:30px;top:20px;opacity:.95}
.sec{margin-top:34px}.sh{display:flex;align-items:center;gap:14px;margin-bottom:16px}.num{width:44px;height:44px;border-radius:50%;background:#F2A900;color:#1B2A49;font-weight:900;font-size:22px;display:flex;align-items:center;justify-content:center;flex:none}
.sh h2{font-size:28px;font-weight:800;letter-spacing:-.01em}.sh small{display:block;font-size:15px;font-weight:500;color:#6B7690;margin-top:2px}
.card{background:#fff;border-radius:20px;padding:24px 26px;box-shadow:0 2px 10px rgba(27,42,73,.07)}
.grid{display:grid;gap:18px}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}
.ico{font-size:38px;line-height:1}.card h3{font-size:19px;font-weight:800;margin:10px 0 6px}.card p{font-size:16px;line-height:1.45;color:#3A4663}
.big{font-size:72px;font-weight:900;line-height:1;letter-spacing:-.03em}.lab{font-size:15px;color:#5A6580;font-weight:600}
.row{display:grid;grid-template-columns:230px 1fr 64px;gap:12px;align-items:center;margin:9px 0;font-size:15.5px;font-weight:600}
.trk{background:#E7ECF4;border-radius:8px;height:22px;position:relative;overflow:hidden}.fill{height:100%;border-radius:8px}.val{font-weight:800;text-align:right;font-size:16px}
.meta{position:absolute;top:-3px;bottom:-3px;width:2px;background:#1B2A49}
.tag{display:inline-block;border-radius:30px;padding:5px 14px;font-size:14px;font-weight:800;color:#fff}
.quote{border-left:5px solid #F2A900;background:#FFF7E0;border-radius:0 14px 14px 0;padding:16px 20px;font-size:17px;font-style:italic;color:#3A4663;line-height:1.45}
.msg{border-top:6px solid;border-radius:18px}.msg .n{font-size:34px;font-weight:900}
.foot{background:#1B2A49;color:#C9D1E3;margin-top:40px;padding:28px 48px;font-size:14px;line-height:1.55}
.foot b{color:#fff}.warn{background:#FDEEE9;border-left:6px solid #E4572E;border-radius:0 14px 14px 0;padding:14px 20px;font-size:16px;line-height:1.45;color:#3A2A28;margin-top:22px}
.kpi{text-align:center}.kpi .v{font-size:52px;font-weight:900;letter-spacing:-.02em}.kpi .l{font-size:15px;color:#5A6580;font-weight:600;margin-top:4px;line-height:1.3}
.tbl{width:100%;border-collapse:separate;border-spacing:0 8px;font-size:15px}.tbl th{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:#6B7690;text-align:left;padding:0 12px}.tbl td{background:#fff;padding:14px 12px;vertical-align:top;line-height:1.38}.tbl td:first-child{border-radius:14px 0 0 14px;font-weight:800}.tbl td:last-child{border-radius:0 14px 14px 0}
.pill{display:inline-block;border-radius:8px;padding:3px 10px;font-size:13px;font-weight:800;color:#fff}
.dumb{position:relative;height:38px;margin:6px 0}.dumb .line{position:absolute;top:18px;height:5px;background:#C5CBD8;border-radius:3px}.dumb .dot{position:absolute;top:10px;width:20px;height:20px;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 1px #ccd}
'''
def page(body, name, hero_kicker, hero_h1, hero_p, chips, foot_extra=''):
    arch = '<svg class="arch" width="300" height="300" viewBox="0 0 300 300"><rect x="55" y="25" width="190" height="300" rx="95" fill="#2c4272"/><rect x="80" y="50" width="140" height="300" rx="70" fill="#4C8BD6"/><rect x="100" y="70" width="100" height="300" rx="50" fill="#1F8A8A"/><rect x="118" y="88" width="64" height="300" rx="32" fill="#F2A900"/><rect x="130" y="100" width="40" height="300" rx="20" fill="#1B2A49"/></svg>'
    ch = ''.join(f'<span class="chip">{c}</span>' for c in chips)
    foot = f'''<div class="foot"><b>Fuente y método.</b> Encuesta confidencial de percepción · {N} estudiantes · Duoc UC Sede San Bernardo · 13–16 oct. 2026 · escala 1 a 5 («No sé/No aplica» excluido) · datos de una sola medición. {foot_extra}<br><b>Uso de Inteligencia Artificial.</b> Análisis, redacción y diseño elaborados con apoyo de Claude (Anthropic); requieren revisión y validación del equipo del Proyecto La Puerta. Ilustraciones propias (sin fotografías de personas). Informe completo: Productos A, B y C.</div>'''
    h = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{name}</title><style>{CSS}</style></head><body><div class="hero">{arch}<div class="kicker">{hero_kicker}</div><h1>{hero_h1}</h1><p>{hero_p}</p><div class="chips">{ch}</div></div><div class="wrap">{body}</div>{foot}<script>document.fonts.ready.then(function(){{setTimeout(function(){{document.title="H="+Math.ceil(document.body.getBoundingClientRect().height)}},400)}})</script></body></html>'
    path = os.path.abspath(OUT + name + '.html'); open(path, 'w').write(h); return path
def sec(num, title, sub, inner): return f'<div class="sec"><div class="sh"><div class="num">{num}</div><div><h2>{title}</h2><small>{sub}</small></div></div>{inner}</div>'
def bar(label, pct, color, text=None, meta=None, scale=100):
    m = f'<div class="meta" style="left:{meta/scale*100}%"></div>' if meta else ''
    return f'<div class="row"><div>{label}</div><div class="trk"><div class="fill" style="width:{pct/scale*100}%;background:{color}"></div>{m}</div><div class="val" style="color:{color if color!=AMB else NAVY}">{text or pc(pct)}</div></div>'
def semc(f): return GREEN if f >= 80 else ('#8CBF3F' if f >= 70 else (AMB if f >= 60 else CORAL))
def render(path):
    name = os.path.basename(path)[:-5]
    out = subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=3000', '--dump-dom', 'file://' + path], capture_output=True, text=True).stdout
    Hh = int(re.search(r'<title>H=(\d+)</title>', out).group(1)) + 6
    png = OUT + name + '.png'
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', f'--window-size=1200,{Hh+200}', '--force-device-scale-factor=2', f'--screenshot={png}', 'file://' + path], capture_output=True)
    im = Image.open(png); im.crop((0, 0, im.size[0], min(im.size[1], Hh * 2))).save(png)
    src = open(path).read().replace('</style>', f'@page{{size:1200px {Hh}px;margin:0}}html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}</style>')
    p2 = path.replace('.html', '_pdf.html'); open(p2, 'w').write(src)
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', f'--print-to-pdf={OUT + name}.pdf', '--no-pdf-header-footer', 'file://' + p2], capture_output=True); os.remove(p2)
    print(name, Hh, Image.open(png).size)

# ======================= D · Infografía 1 =======================
g = R['global']; per = R['perfiles']
dims = sorted(R['dims'], key=lambda d: -d['media'])
fort = ['P07', 'P14', 'P15', 'P03']; brech = ['P12', 'P09', 'P11', 'P06']
a1 = Q['abi1']; a2 = Q['abi2']
t1 = [('Habilidades blandas', a1['Habilidades blandas (equipo, comunicación, responsabilidad, adaptación)']), ('Conocimiento técnico del área', a1['Conocimiento técnico del área (finanzas, logística, comex, marketing, RR.HH.)']), ('Claridad sobre el campo laboral', a1['Mayor claridad sobre el campo laboral y su carrera']), ('Sin aprendizaje claro', a1['Sin aprendizaje claro / no sabe'])]
t2 = [('Simulaciones y práctica aplicada', a2['Simulaciones, casos reales y práctica aplicada']), ('Comunicación y oratoria', a2['Comunicación, oratoria y habilidades blandas']), ('Inglés', a2['Idiomas (inglés principalmente)']), ('Preparación para la práctica', a2['Preparación para la práctica y el empleo (entrevista, CV, inducción, apoyo)']), ('Herramientas (ERP, Excel…)', a2['Software y herramientas (ERP, SAP, Softland, Excel, Python, Power BI, IA)']), ('Salidas a terreno', a2['Salidas a terreno, visitas, ferias y charlas'])]
body = ''
body += sec(1, '¿Para qué se hizo este estudio?', 'Tres preguntas que guían el Proyecto La Puerta', '<div class="grid g3"><div class="card"><div class="ico">🧭</div><h3>Saber cómo se sienten</h3><p>Conocer qué tan preparados se perciben los estudiantes para enfrentar el mundo laboral.</p></div><div class="card"><div class="ico">🔍</div><h3>Encontrar brechas</h3><p>Identificar dónde hace falta más apoyo antes de la práctica profesional.</p></div><div class="card"><div class="ico">🛠️</div><h3>Decidir mejor</h3><p>Orientar acciones concretas y alcanzables para Duoc UC y las empresas socias.</p></div></div>')
perfil = f'''<div class="grid g4">
<div class="card kpi"><div class="v" style="color:{NAVY}">{N}</div><div class="l">estudiantes respondieron<br>(100 % con consentimiento)</div></div>
<div class="card kpi"><div class="v" style="color:{TEAL}">{R['perfil_pct']['escuela_EAN']:.0f} %</div><div class="l">de la Escuela de<br>Administración y Negocios</div></div>
<div class="card kpi"><div class="v" style="color:{AMB}">{100*R['perfil']['anio']['1.º–2.º sem.']/N:.0f} %</div><div class="l">cursa 1.º–2.º semestre<br>(primer año)</div></div>
<div class="card kpi"><div class="v" style="color:{CORAL}">{100*R['perfil']['practica']['Sin práctica previa']/N:.0f} %</div><div class="l">nunca ha hecho<br>una práctica</div></div></div>
<div class="card" style="margin-top:18px"><div style="font-weight:800;margin-bottom:8px">Semestre en curso</div>
{bar('1.º–2.º semestre', 100*90/N, SKY, '90')}{bar('3.º–4.º semestre', 100*43/N, SKY, '43')}{bar('5.º–6.º semestre', 100*50/N, SKY, '50')}
<div style="font-weight:800;margin:16px 0 8px">Práctica previa</div>
{bar('Sin práctica previa', 100*112/N, CORAL, '112')}{bar('Práctica EMTP (colegio técnico)', 100*44/N, AMB, '44')}{bar('Pasantía en la carrera', 100*23/N, AMB, '23')}{bar('Práctica en otra carrera', 100*5/N, AMB, '5')}</div>'''
body += sec(2, '¿Quiénes respondieron?', 'Perfil de las y los participantes', perfil)
dimrows = ''.join(bar(f"{d['id']} · {d['nombre']}", d['media'], semc(d['fav']), n(d['media']), None, 5) for d in dims)
res = f'''<div class="grid" style="grid-template-columns:330px 1fr"><div class="card kpi" style="display:flex;flex-direction:column;justify-content:center"><div class="l">Puntaje global (1 a 5)</div><div class="big" style="color:{NAVY};margin:10px 0">{n(g['media'])}</div><div class="l">{pc(g['fav_items'])} de las respuestas son «de acuerdo» o «muy de acuerdo»</div><div style="margin-top:12px"><span class="tag" style="background:{TEAL}">{per['Sólido (≥4)']} sólidos</span> <span class="tag" style="background:{SKY}">{per['Intermedio (3–3,99)']} intermedios</span> <span class="tag" style="background:{CORAL};margin-top:6px">{per['Por fortalecer (<3)']} por fortalecer</span></div></div>
<div class="card"><div style="font-weight:800;margin-bottom:6px">Las cinco dimensiones (promedio)</div>{dimrows}<p style="font-size:14px;margin-top:8px">Color según % de acuerdo: verde claro 70–79 % · ámbar 60–69 %. Ninguna llega al verde oscuro (≥ 4,20).</p></div></div>'''
body += sec(3, 'Principales resultados', 'Una base sólida, con espacio para mejorar', res)
fr = ''.join(bar(SHORT[p], IT[p]['fav'], semc(IT[p]['fav']), meta=70) for p in fort); br = ''.join(bar(SHORT[p], IT[p]['fav'], semc(IT[p]['fav']), meta=70) for p in brech)
body += sec(4, 'Los hallazgos más relevantes', '% de estudiantes de acuerdo o muy de acuerdo · la línea marca la meta de 70 %', f'<div class="grid g2"><div class="card"><div style="font-weight:800;font-size:20px;color:{GREEN}">⭐ Fortalezas</div>{fr}<p style="font-size:14px">Actitud, diálogo, ética y ganas de aprender.</p></div><div class="card"><div style="font-weight:800;font-size:20px;color:{CORAL}">🔧 Oportunidades</div>{br}<p style="font-size:14px"><b>Solo 4 de cada 10</b> dice tener una red de contactos.</p></div></div>')
voz = f'''<div class="grid g2"><div class="card"><div style="font-weight:800;margin-bottom:6px">¿Cuál fue tu aprendizaje más valioso? <span style="color:#6B7690;font-weight:500">({Q['abi1_n']} resp.)</span></div>{''.join(bar(a, 100*b/Q['abi1_n'], TEAL if not a.startswith('Sin') else GRAY, str(b), None, 40) for a, b in t1)}</div>
<div class="card"><div style="font-weight:800;margin-bottom:6px">¿Qué apoyo pedirías antes de la práctica? <span style="color:#6B7690;font-weight:500">({Q['abi2_n']} resp.)</span></div>{''.join(bar(a, 100*b/Q['abi2_n'], SKY, str(b), None, 40) for a, b in t2)}</div></div>
<div class="quote" style="margin-top:18px">«Poner en práctica de verdad todo el conocimiento y no ir al vacío suponiendo que aprendemos de verdad, no llegar al vacío a una empresa.»<br><span style="font-size:14px;font-style:normal;color:#6B7690">— Estudiante, respuesta abierta (anónima)</span></div>'''
body += sec(5, 'En sus propias palabras', 'Menciones por tema (una respuesta puede tocar varios temas)', voz)
msgs = [('1', 'Hay una base sólida', f'Puntaje global {n(g["media"])}; la actitud es la mayor fortaleza.', TEAL), ('2', 'La red es la gran brecha', f'Solo {pc(IT["P12"]["fav"])} tiene referentes laborales.', CORAL), ('3', 'Quieren ver el trabajo real', f'{pc(IT["P15"]["fav"])} pide proyectos con empresas; piden simulaciones y salidas.', AMB), ('4', 'La práctica previa ayuda poco', f'+{n(fo["GLOBAL"]["dif"])} puntos con práctica previa: una diferencia pequeña.', SKY), ('5', 'Falta medir el efecto', 'Sin código, momento ni grupo no se puede evaluar a La Puerta.', NAVY)]
mm = ''.join(f'<div class="card msg" style="border-color:{c}"><div class="n" style="color:{c if c!=AMB else NAVY}">{a}</div><h3>{t}</h3><p>{d}</p></div>' for a, t, d, c in msgs)
body += sec(6, 'Mensajes clave para decidir', 'Cinco ideas para llevar a la reunión', f'<div class="grid g5">{mm}</div><div class="warn"><b>⚠ Importante:</b> esta es una fotografía de un solo momento. Sirve para <b>describir</b> cómo se sienten los estudiantes, no para afirmar que el programa La Puerta produjo cambios.</div>')
pD = page(body, 'D_Infografia_1_Estudio_y_Resultados', 'Proyecto La Puerta · Infografía 1', 'Así se sienten los estudiantes frente al mundo laboral', 'Objetivos, participantes, resultados y mensajes clave de la encuesta de percepción y competencias.', [f'👥 {N} estudiantes', '📅 13–16 oct. 2026', '🏫 Duoc UC San Bernardo'])
render(pD)

# ======================= E · Infografía 2 =======================
H = [('H1', 'Hipótesis central', 'La práctica previa amortigua la transición', 'PARCIAL', AMB, f'+{n(fo["GLOBAL"]["dif"])} pts (esperado 0,8–1,2) · r = {n(OFR["pearson"]["r"])}'),
     ('H2', 'Año de estudio', 'A más semestres, más preparación', 'NO RESPALDADA', CORAL, f'sin escalera · p ajustado = {n(H2["GLOBAL"]["p_holm"])}'),
     ('H3', 'Redes', 'La red de contactos es lo más débil', 'RESPALDADA', TEAL, f'P12 = {n(IT["P12"]["media"])} · p < 0,001'),
     ('H4', 'Conocer y probar', 'Conocer el trabajo → más seguridad', 'RESPALDADA', TEAL, f'rho 0,47–0,53 · R² ≈ {100*h4["ols"]["r2"]:.0f} %'),
     ('H5', 'Interés', 'Alta demanda de proyectos reales', 'RESPALDADA', TEAL, f'{pc(h5["fav"])} de acuerdo · p < 0,001'),
     ('H6', 'Efecto del programa', 'La Puerta mejora pre-post vs. control', 'NO EVALUABLE', GRAY, 'faltan código, momento y grupo')]
hh = ''.join(f'<div class="card" style="border-top:6px solid {c}"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:30px;font-weight:900">{a}</div><span class="tag" style="background:{c};{"color:#1B2A49;" if c==AMB else ""}font-size:12.5px">{v}</span></div><h3>{t}</h3><p style="font-size:15px">{d}</p><p style="font-size:14px;font-weight:700;color:#1B2A49;margin-top:8px">{e}</p></div>' for a, t, d, v, c, e in [(a, t, d, v, c, e) for a, t, d, v, c, e in H])
body = sec(1, 'El tablero de hipótesis', 'Qué respaldan —y qué no— los datos', f'<div class="grid g3">{hh}</div>')
# H1 esperado vs observado
def rng(lo, hi, mn, mx): return f'left:{(lo-mn)/(mx-mn)*100}%;width:{(hi-lo)/(mx-mn)*100}%'
ci = fo['GLOBAL']['ci']; dif = fo['GLOBAL']['dif']; mn, mx = -0.2, 1.4
axis = ''.join(f'<span style="position:absolute;left:{(v-mn)/(mx-mn)*100}%;transform:translateX(-50%)">{n(v,1)}</span>' for v in [0, 0.5, 1.0, 1.4])
h1 = f'''<div class="card"><div style="font-size:17px;margin-bottom:18px">Diferencia entre estudiantes <b>con</b> y <b>sin</b> práctica previa (puntos en la escala 1–5)</div>
<div style="position:relative;height:150px;margin:0 20px">
<div style="position:absolute;left:{(0-mn)/(mx-mn)*100}%;top:0;bottom:30px;width:2px;background:#1B2A49"></div>
<div style="position:absolute;{rng(.8,1.2,mn,mx)};top:8px;height:36px;background:{AMB};border-radius:8px;opacity:.9"></div><div style="position:absolute;{rng(.8,1.2,mn,mx)};top:50px;font-size:15px;font-weight:800;color:#B07C00;white-space:nowrap">Esperado por el proyecto: 0,8 a 1,2</div>
<div style="position:absolute;{rng(ci[0],ci[1],mn,mx)};top:92px;height:8px;background:#9BD0D0;border-radius:4px"></div><div style="position:absolute;left:{(dif-mn)/(mx-mn)*100}%;top:82px;width:28px;height:28px;margin-left:-14px;background:{TEAL};border-radius:50%;border:4px solid #fff;box-shadow:0 0 0 2px {TEAL}"></div>
<div style="position:absolute;left:{(0-mn)/(mx-mn)*100}%;top:118px;font-size:15px;font-weight:800;color:{TEAL};white-space:nowrap;margin-left:-60px">Observado: +{n(dif)} (IC 95 %: {n(ci[0])} a {n(ci[1])})</div></div>
<div style="position:relative;height:22px;margin:0 20px;font-size:13px;color:#6B7690;font-weight:700">{axis}</div><p style="margin-top:6px;font-size:16px"><b>Lectura:</b> la dirección coincide con lo esperado, pero la magnitud es entre 4 y 7 veces menor; con esta muestra se descarta una brecha de 0,8 o más.</p></div>'''
body += sec(2, 'La hipótesis central frente a los datos', 'Informe Metodológico del Proyecto La Puerta', h1)
# comparación dumbbell
def dumb(label, a, b, mn=3.4, mx=4.5):
    pa, pb = (a-mn)/(mx-mn)*100, (b-mn)/(mx-mn)*100
    return f'<div style="display:grid;grid-template-columns:240px 1fr 130px;gap:10px;align-items:center;font-size:15.5px;font-weight:600"><div>{label}</div><div class="dumb"><div class="line" style="left:{min(pa,pb)}%;width:{abs(pb-pa)}%"></div><div class="dot" style="left:calc({pa}% - 10px);background:{CORAL}"></div><div class="dot" style="left:calc({pb}% - 10px);background:{TEAL}"></div></div><div style="font-weight:800;text-align:right">{n(a)} → {n(b)}</div></div>'
cmp = ''.join(dumb(f"{d['id']} · {d['nombre']}", R['dim_pract'][d['id']][0], R['dim_pract'][d['id']][1]) for d in R['dims'])
body += sec(3, 'Comparación de resultados', 'Promedio por dimensión, sin práctica previa vs. con práctica previa', f'<div class="card">{cmp}<p style="font-size:14.5px;margin-top:10px"><span style="color:{CORAL};font-weight:800">● Sin práctica (n=112)</span> &nbsp; <span style="color:{TEAL};font-weight:800">● Con práctica (n=72)</span> · Cuatro de cinco dimensiones suben con práctica, pero ninguna diferencia resiste la corrección estadística; las mayores son conocer el rol (D1) y autoeficacia (D3).</p></div>')
# factores asociados
fa = [('P01', 'Conozco las tareas reales'), ('P02', 'Tengo claras las exigencias'), ('P09', 'Comprobé que el trabajo calza'), ('P05', 'Aplico lo de clases a casos reales'), ('P03', 'Confío ante una tarea nueva'), ('P12', 'Tengo red de contactos')]
fb = ''.join(bar(t, abs(h4[f'{p}_P10']['rho'])*100, TEAL if h4[f'{p}_P10']['rho'] > .4 else SKY, n(h4[f'{p}_P10']['rho']), None, 60) for p, t in fa)
body += sec(4, 'Factores asociados', 'Relación (rho de Spearman) con «me siento seguro/a de adaptarme a un puesto»', f'<div class="grid" style="grid-template-columns:1.4fr 1fr"><div class="card">{fb}<p style="font-size:14.5px;margin-top:6px">Entre más alto, más fuerte la relación. Todas son moderadas a fuertes.</p></div><div class="card" style="text-align:center"><div class="l">Variación de la seguridad que explican, en conjunto, estos factores</div><div class="big" style="color:{TEAL};margin:12px 0">{100*h4["ols"]["r2"]:.0f} %</div><div style="font-size:16px;line-height:1.4"><b>La práctica previa y el año de estudio dejan de pesar</b> al considerar lo anterior.</div></div></div>')
# explicación visual: red vs interés
rv = bar('P15 · Quiero proyectos con empresas', IT['P15']['fav'], GREEN, pc(IT['P15']['fav']), 70) + bar('P11 · Sé cómo contactar profesionales', IT['P11']['fav'], AMB, pc(IT['P11']['fav']), 70) + bar('P12 · Tengo red de contactos', IT['P12']['fav'], CORAL, pc(IT['P12']['fav']), 70)
body += sec(5, 'Explicación visual del hallazgo principal', 'Mucho interés, poca red', f'<div class="card">{rv}<div class="quote" style="margin-top:14px">Hay <b>ganas de sobra</b> de vincularse con empresas, pero <b>pocos puentes</b>: P12 es significativamente más baja que cada una de las otras 14 afirmaciones (p ajustado &lt; 0,001), con y sin práctica previa.</div></div>')
recs = [('🧪', 'R1 · Medir bien', 'Código, momento y grupo obligatorios; agregar A03/A04. Sin esto no se puede evaluar a La Puerta.', NAVY), ('🤝', 'R2 · Construir redes', 'Mentorías, «café con profesionales», entrevistas informativas, ferias.', TEAL), ('🏢', 'R3 · Acercar el trabajo real', 'Visitas, simulaciones, mini-proyectos con empresas y bitácoras de aprendizaje.', AMB), ('🎯', 'R4 · Focalizar', f'Acompañar a los {S["total"]["Rojo"]} estudiantes en rojo, con o sin práctica previa.', SKY)]
rr = ''.join(f'<div class="card" style="border-top:6px solid {c}"><div class="ico">{i}</div><h3>{t}</h3><p style="font-size:15px">{d}</p></div>' for i, t, d, c in recs)
body += sec(6, 'Recomendaciones derivadas', 'Qué hacer con lo que muestran las hipótesis', f'<div class="grid g4">{rr}</div><div class="warn"><b>⚠ Cuidado:</b> los resultados muestran asociaciones en una sola medición, basadas en autopercepciones. Las hipótesis H2–H5 son exploratorias y deben replicarse con otra cohorte.</div>')
pE = page(body, 'E_Infografia_2_Hipotesis_y_Factores', 'Proyecto La Puerta · Infografía 2', '¿Qué dicen los datos sobre nuestras hipótesis?', 'Contraste de hipótesis, comparación de resultados, factores asociados y recomendaciones.', ['🧪 6 hipótesis', '⚖️ Reglas de decisión previas', f'📈 {N} estudiantes'], foot_extra='Pruebas: t de Welch, Mann-Whitney, Kruskal-Wallis, Friedman, Spearman, regresión robusta; corrección de Holm; IC por bootstrap.')
render(pE)

# ======================= H · Infografía comparativa de brechas =======================
exp = fo['GLOBAL']['dif']
rowsH = [
 ('Red de contactos', 'A', f'{pc(IT["P12"]["fav"])} de acuerdo; <b>29 pts bajo la meta</b> (70 %)', f'B (H3): P12 menor que las otras 14 (p &lt; 0,001), también con práctica', 'Ausencia de referentes; la red se arma recién en la práctica', 'ALTO', 'Llegar sin puntos de apoyo ni información', 'Demanda alta (83 %): mentorías, ferias, entrevistas informativas', 'R2'),
 ('Conocer el trabajo real', 'A', f'P01 {pc(IT["P01"]["fav"])} · P02 {pc(IT["P02"]["fav"])} · P09 {pc(IT["P09"]["fav"])} (<b>1 a 8 pts bajo la meta</b>)', f'B (H4): se asocian con la seguridad de adaptarse (R² ≈ {100*h4["ols"]["r2"]:.0f} %)', 'Poco contacto con tareas y exigencias reales', 'ALTO', 'Expectativas irreales; shock de transición', 'Visitas, simulaciones, mini-proyectos y bitácoras', 'R3'),
 ('Efecto de la práctica previa', 'A↔B', f'A: +{n(exp)} puntos (14 % rojos con práctica vs. 25 % sin)', f'B (H1): no concluyente; <b>esperado 0,8–1,2, observado {n(exp)}</b>', 'Proyección sobredimensionada; autopercepción con «techo»; falta medir A03/A04', 'MEDIO', 'Segregar por «sin práctica previa» sin evidencia', 'Focalizar por semáforo y brechas específicas', 'R4'),
 ('Estudiantes en rojo', 'A', f'{S["total"]["Rojo"]} estudiantes ({pc(S["pct_total"]["Rojo"])}) bajo 3,50', f'B: {S["sin"]["Rojo"]} sin práctica y {S["con"]["Rojo"]} con práctica', 'Brechas combinadas de conocimiento del trabajo y redes', 'ALTO', 'Mala experiencia o abandono de la práctica', 'Detección temprana y tutoría grupal', 'R4'),
 ('Evaluación del programa', 'B', 'A: no se puede describir un cambio con una sola medición', 'B (H6): <b>no evaluable</b>; código, momento, grupo y POST_EXP1 vacíos', 'Diseño de recolección de datos', 'ALTO', 'No demostrar el impacto; decidir sin evidencia', 'Corrección barata: campos obligatorios y piloto con control', 'R1'),
 ('Año de estudio (¿«valle» 3.º–4.º?)', 'A↔B', f'A: 3.º–4.º es el tramo más bajo ({n(H2["GLOBAL"]["medias"][1])})', f'B (H2): <b>no respaldada</b> (p ajustado = {n(H2["GLOBAL"]["p_holm"])})', 'Posible desconexión entre el entusiasmo inicial y la práctica', 'MEDIO', 'Sobreinterpretar una diferencia que puede ser azar', 'Verificar en la próxima cohorte', 'R7')]
col = {'ALTO': CORAL, 'MEDIO': AMB}
tr = ''.join(f'<tr><td>{a}</td><td style="font-weight:500">{b}<br><span style="color:#5A6580">{c}</span></td><td style="font-weight:500">{d}</td><td><span class="pill" style="background:{col[e]};{"color:#1B2A49;" if e=="MEDIO" else ""}">{e}</span><div style="font-weight:500;margin-top:6px">{f}</div></td><td style="font-weight:500">{g_}</td><td><span class="pill" style="background:{NAVY}">{h}</span></td></tr>' for a, _, b, c, d, e, f, g_, h in rowsH)
body = sec(1, 'Las brechas, lado a lado', 'Qué muestra cada informe y qué distancia hay entre lo esperado y lo observado', f'<table class="tbl"><tr><th>Brecha</th><th>Evidencia (A · descriptivo / B · hipótesis)</th><th>Factor explicativo</th><th>Impacto potencial y riesgo</th><th>Oportunidad</th><th>Rec.</th></tr>{tr}</table>')
# gráfico distancia a meta
dist = ''.join(bar(f'{p} · {SHORT[p]}', max(0, 70-IT[p]['fav']), CORAL if 70-IT[p]['fav'] > 10 else AMB, f"−{n(70-IT[p]['fav'],0)} pts" if 70-IT[p]['fav'] > 0 else 'ok', None, 30) for p in ['P12', 'P09', 'P11', 'P06', 'P04', 'P01', 'P02'])
body += sec(2, 'Distancia a la meta de 70 %', 'Puntos porcentuales que faltan en cada afirmación (Informe A)', f'<div class="grid" style="grid-template-columns:1.5fr 1fr"><div class="card">{dist}</div><div class="card"><div class="ico">📏</div><h3>La brecha de expectativa</h3><p>El proyecto anticipaba una diferencia de <b>0,8 a 1,2 puntos</b> entre estudiantes con y sin práctica previa. Los datos muestran <b style="color:{TEAL}">+{n(exp)}</b>. Hay una brecha de <b>{n(0.8-exp)} a {n(1.2-exp)} puntos</b> entre la hipótesis y la evidencia.</p></div></div>')
riesgos = [('⚠️', 'Riesgos asociados', ['Segregar por «sin práctica previa»: no hay evidencia de que sea el factor decisivo.', 'Tomar como hecho el «valle» de 3.º–4.º.', 'Afirmar que La Puerta funciona con una sola medición.', 'Estigmatizar a quienes están en rojo.']), ('🌱', 'Oportunidades de mejora', [f'Demanda alta y homogénea de proyectos con empresas ({pc(IT["P15"]["fav"])}).', 'Mecanismo plausible: conocer y probar el trabajo real.', 'Fortalezas de actitud: diálogo, ética, confianza.', 'Corrección de medición de bajo costo.']), ('⭐', 'Recomendaciones prioritarias', ['R1 · Medir bien: código, momento, grupo.', 'R2 · Construir redes desde primer año.', 'R3 · Contacto real: simulaciones, visitas, mini-proyectos.', 'R4 · Acompañar a quienes están en rojo.'])]
rc = ''.join(f'<div class="card"><div class="ico">{i}</div><h3>{t}</h3><ul style="padding-left:20px;font-size:15.5px;line-height:1.5;color:#3A4663">{"".join(f"<li style=\"margin-bottom:6px\">{x}</li>" for x in L)}</ul></div>' for i, t, L in riesgos)
body += sec(3, 'Riesgos, oportunidades y prioridades', 'Para pasar de la brecha a la acción', f'<div class="grid g3">{rc}</div><div class="warn"><b>⚠ Brecha metodológica mayor:</b> mientras la base no registre código, momento y grupo, la distancia entre <i>lo que se cree</i> del programa y <i>lo que se puede demostrar</i> seguirá abierta.</div>')
pH = page(body, 'H_Infografia_Comparativa_de_Brechas', 'Proyecto La Puerta · Infografía comparativa', 'Brechas: lo que muestran los dos informes', 'Comparación entre el análisis descriptivo (A) y el análisis con hipótesis (B): brechas, factores, impacto, riesgos, oportunidades y recomendaciones.', ['📊 Informe A', '🧪 Informe B', '🔗 Informe C'])
render(pH)
