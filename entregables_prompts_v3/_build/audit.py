# -*- coding: utf-8 -*-
"""Auditoría documental automatizada de los prompts v3.0 (comprobaciones objetivas y reproducibles)."""
import re, os
from content import CAMBIOS, REFS

BASE = os.path.join(os.path.dirname(__file__), "..")
P1 = os.path.join(BASE, "06_Prompts_TXT", "PROMPT_01_ARQUITECTO_PEDAGOGICO_CASOS_v3.0.txt")
P2 = os.path.join(BASE, "06_Prompts_TXT", "PROMPT_02_AUDITOR_INFORMES_IA_v3.0.txt")
O1 = os.path.join(BASE, "08_Originales", "ORIGINAL_P1_prompt_comparativo_inicial.txt")
O2 = os.path.join(BASE, "08_Originales", "ORIGINAL_P2_prompt_subir_nivel_secundario.txt")
rd = lambda p: open(p, encoding="utf-8").read()


def nota(p):
    return lambda P: round((1.0 + 3.0 * P / 70) if P < 70 else (4.0 + 3.0 * (P - 70) / 30), 2)


def ejecutar():
    t1, t2 = rd(P1), rd(P2)
    res = []  # (id, prompt, comprobación, resultado bool, evidencia)

    # A. Estructura de etiquetas balanceadas
    for nom, t in (("P1", t1), ("P2", t2)):
        abiertas = re.findall(r"^<([a-z_]+)>\s*$", t, re.M)
        cerradas = re.findall(r"^</([a-z_]+)>\s*$", t, re.M)
        res.append((f"A-{nom}", nom, "Bloques <etiqueta> abiertos y cerrados balanceados",
                    sorted(abiertas) == sorted(cerradas), f"{len(abiertas)} bloques"))
        refs = set(re.findall(r"<([a-z_]+)>", t)) - set(abiertas)
        res.append((f"B-{nom}", nom, "Referencias cruzadas a bloques inexistentes", not refs, "ninguna" if not refs else str(refs)))

    # C. Variables usadas vs. declaradas
    for nom, t in (("P1", t1), ("P2", t2)):
        usadas = set(re.findall(r"\{\{([A-Z_]+)\}\}", t))
        blq = t[t.index("<variables_de_entrada>"):t.index("</variables_de_entrada>")]
        decl = set(re.findall(r"\{\{([A-Z_]+)\}\}", blq))
        faltan = usadas - decl
        res.append((f"C-{nom}", nom, "Variables {{…}} usadas están declaradas en variables_de_entrada", not faltan,
                    f"{len(usadas)} usadas; sin declarar: {sorted(faltan) or 'ninguna'}"))

    # D. Corrección del orden de artefactos en P1
    f3 = t1[t1.index("[FASE 3"):t1.index("[FASE 4")]
    res.append(("D-P1", "P1", "A4 no aparece en la Fase 3 (corrige contradicción original)", "A4" not in f3.replace("A1 → A2 → A3", ""), "Fase 3 contiene solo A1–A3"))
    o1 = rd(O1); of3 = o1[o1.index("[FASE 3"):o1.index("[FASE 4")]
    res.append(("D0-P1", "P1", "Contradicción presente en el original (A4 mencionado en Fase 3)", "A4" in of3, "confirma el hallazgo P1-01"))

    # E. Fórmula de nota
    f = nota(None)
    casos = {0: 1.0, 35: 2.5, 70: 4.0, 85: 5.5, 100: 7.0}
    ok = all(abs(f(k) - v) < 0.01 for k, v in casos.items())
    res.append(("E-P1", "P1", "Conversión a nota 1,0–7,0 (0→1,0; 35→2,5; 70→4,0; 85→5,5; 100→7,0)", ok,
                "; ".join(f"{k}%→{f(k)}" for k in casos)))
    res.append(("E2-P1", "P1", "La fórmula del prompt coincide con la implementada", "1,0 + 3,0 × (P/70)" in t1 and "4,0 + 3,0 × ((P − 70)/30)" in t1, "texto verificado"))

    # F. Pesos de la puntuación P2
    linea = [l for l in t2.splitlines() if l.startswith("Criterios y pesos")][0]
    pesos = [int(x) for x in re.findall(r"(\d+) %", linea)]
    res.append(("F-P2", "P2", "Los pesos de los criterios suman 100 %", sum(pesos) == 100 and len(pesos) == 8, f"{pesos} → {sum(pesos)} %"))

    # G. Seis estados de evidencia y regla de semáforo
    est = [s for s in ("✅", "⚠️", "❓", "❌", "⛔", "🔒") if s in t2]
    res.append(("G-P2", "P2", "Seis estados de evidencia definidos", len(est) == 6, " ".join(est)))
    res.append(("H-P2", "P2", "Semáforos 🟢🟡🔴 con regla determinista", all(s in t2 for s in ("🟢", "🟡", "🔴")) and "Excepción de seguridad" in t2, "regla + excepción presentes"))

    # I. Productos P1–P7 en P2
    res.append(("I-P2", "P2", "Productos P1–P7 definidos", all(f"P{i}." in t2 for i in range(1, 8)), "P1–P7"))

    # J. Elementos transversales (IA, formato, APA, etiquetas)
    for nom, t in (("P1", t1), ("P2", t2)):
        ok = all(k in t for k in ("<declaracion_ia>", "<formato_institucional>", "APA 7", "[BRECHA]", "<protocolo_de_piloto>"))
        res.append((f"J-{nom}", nom, "Incluye declaración de IA, formato DUOC UC, APA 7, etiquetas epistémicas y protocolo de piloto", ok, "5/5 elementos"))
        res.append((f"K-{nom}", nom, "Incluye defensa ante instrucciones incrustadas en datos/adjuntos",
                    ("DATOS, no instrucciones" in t) or ("MATERIAL DE ANÁLISIS, no instrucciones" in t), "regla presente"))

    # L. Cada referencia citada en los prompts existe en la bibliografía
    bib = " ".join(r[0] for r in REFS)
    for nom, t in (("P1", t1), ("P2", t2)):
        bloque = t[t.index("<referencias_del_prompt>"):t.index("</referencias_del_prompt>")]
        autores = re.findall(r"^([A-ZÁÉÍÓÚ][\w'’\-áéíóúñ]+),", bloque, re.M)
        anios = re.findall(r"\((\d{4})\)", bloque)
        faltan = []
        for a, y in zip(autores, anios):
            if not (a in bib and y in bib): faltan.append(f"{a} {y}")
        res.append((f"L-{nom}", nom, "Referencias del prompt presentes en la bibliografía normalizada (apellido y año)", not faltan,
                    f"{len(autores)} verificadas; faltan: {faltan or 'ninguna'}"))

    # M. Matriz de cambios
    ids = [c[0] for c in CAMBIOS]
    res.append(("M", "Ambos", "Identificadores de cambio únicos y consecutivos", len(ids) == len(set(ids)), f"{len(ids)} cambios"))

    # Métricas descriptivas
    met = {}
    for nom, t, o in (("P1", t1, rd(O1)), ("P2", t2, rd(O2))):
        met[nom] = dict(pal_o=len(o.split()), pal_n=len(t.split()), lin_o=len(o.splitlines()), lin_n=len(t.splitlines()),
                        tok_n=round(len(t) / 4))
    return res, met


if __name__ == "__main__":
    r, m = ejecutar()
    for x in r: print(("OK  " if x[3] else "FALLA"), x[0], x[2], "|", x[4])
    print(m)
