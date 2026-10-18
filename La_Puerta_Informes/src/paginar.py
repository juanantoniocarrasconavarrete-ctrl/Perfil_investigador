"""Calcula la página de cada título (partes y capítulos) a partir del PDF y la guarda para el índice. Uso: paginar.py A_Informe_Descriptivo ..."""
import sys, json, subprocess, re, os
B = '/home/user/Perfil_investigador/La_Puerta_Informes/'
def norm(s): return re.sub(r'\s+', ' ', s).strip().lower()
for base in sys.argv[1:]:
    name = base + '.docx'
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', B + 'informes', B + 'informes/' + name], capture_output=True)
    pdf = B + 'informes/' + base + '.pdf'
    npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    pages = [norm(subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', pdf, '-'], capture_output=True, text=True).stdout) for i in range(1, npg + 1)]
    heads = json.load(open(B + 'src/heads_' + name + '.json'))
    idx_last = max([i for i, t in enumerate(pages, 1) if '.....' in t or '. . . .' in t] or [2])
    res = {}
    for lvl, txt in heads:
        key = norm(txt)[:40]; found = None
        for i in range(idx_last, npg):  # páginas posteriores al índice (índice 1-based => página idx_last+1 ...)
            if key in pages[i]: found = i + 1; break
        res[txt] = found if found else '—'
    json.dump(res, open(B + 'src/pages_' + name + '.json', 'w'), ensure_ascii=False)
    print(base, npg, 'pág. índice hasta', idx_last, 'sin hallar:', [t for t, p in res.items() if p == '—'])
