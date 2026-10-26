#!/usr/bin/env python3
"""Recalcula valores p reportados en formato APA y detecta señales de búsqueda de significancia.

Reconoce:  t(gl) = x, p = .xxx   F(gl1, gl2) = x, p = .xxx   χ2(gl) = x, p = .xxx   r(gl) = x, p = .xxx
Salida JSON: pruebas (reportado vs recalculado), inconsistentes, y resumen de p cercanos a .05.
Python puro (sin scipy). Dos colas para t y r. Solo lectura. Admite .docx, .md, .txt.

Uso: python3 statcheck.py archivo
"""
import json
import math
import re
import sys

# ---- funciones especiales (Numerical Recipes) ----
def _betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1e-30 if abs(d) < 1e-30 else d
    d = 1 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = 1e-30 if abs(d) < 1e-30 else d
        c = 1 + aa / c; c = 1e-30 if abs(c) < 1e-30 else c
        d = 1 / d; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = 1e-30 if abs(d) < 1e-30 else d
        c = 1 + aa / c; c = 1e-30 if abs(c) < 1e-30 else c
        d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 3e-12:
            break
    return h


def betainc(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1 - bt * _betacf(b, a, 1 - x) / b


def gammainc_q(a, x):  # cola superior Q(a, x)
    if x <= 0: return 1.0
    if x < a + 1:
        ap, s, d = a, 1 / a, 1 / a
        for _ in range(500):
            ap += 1; d *= x / ap; s += d
            if abs(d) < abs(s) * 1e-14: break
        return 1 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))
    b = x + 1 - a; c = 1e30; d = 1 / b; h = d
    for i in range(1, 500):
        an = -i * (i - a); b += 2
        d = an * d + b; d = 1e-30 if abs(d) < 1e-30 else d
        c = b + an / c; c = 1e-30 if abs(c) < 1e-30 else c
        d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 1e-14: break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def p_t(t, df):   return betainc(df / 2, 0.5, df / (df + t * t))
def p_f(f, d1, d2): return betainc(d2 / 2, d1 / 2, d2 / (d2 + d1 * f))
def p_chi(x, df): return gammainc_q(df / 2, x / 2)
def p_r(r, df):
    t = r * math.sqrt(df / (1 - r * r)) if abs(r) < 1 else float("inf")
    return p_t(t, df)

NUM = r"(-?\d*[.,]?\d+)"
PVAL = r",?\s*p\s*([=<>])\s*(\.?\d*[.,]?\d+)"
PATRONES = [
    ("t",  re.compile(rf"\bt\s?\(\s*(\d+(?:[.,]\d+)?)\s*\)\s*=\s*{NUM}{PVAL}", re.I)),
    ("F",  re.compile(rf"\bF\s?\(\s*(\d+)\s*,\s*(\d+)\s*\)\s*=\s*{NUM}{PVAL}")),
    ("chi2", re.compile(rf"(?:χ2|χ²|chi2|chi-square)\s?\(\s*(\d+)(?:\s*,\s*N\s*=\s*\d+)?\s*\)\s*=\s*{NUM}{PVAL}", re.I)),
    ("r",  re.compile(rf"\br\s?\(\s*(\d+)\s*\)\s*=\s*{NUM}{PVAL}")),
]
def f(x):
    x = x.replace(",", ".")
    x = "-0" + x[1:] if x.startswith("-.") else ("0" + x if x.startswith(".") else x)
    return float(x)

def leer(ruta):
    if ruta.lower().endswith(".docx"):
        import docx
        return "\n".join(p.text for p in docx.Document(ruta).paragraphs)
    return open(ruta, encoding="utf-8", errors="replace").read()


def main():
    texto = leer(sys.argv[1])
    pruebas = []
    for nombre, rx in PATRONES:
        for m in rx.finditer(texto):
            g = m.groups()
            try:
                if nombre == "t":   est, rep_op, rep_p = f(g[1]), g[2], f(g[3]); calc = p_t(est, f(g[0])); gl = g[0]
                elif nombre == "F": est, rep_op, rep_p = f(g[2]), g[3], f(g[4]); calc = p_f(est, int(g[0]), int(g[1])); gl = f"{g[0]},{g[1]}"
                elif nombre == "chi2": est, rep_op, rep_p = f(g[1]), g[2], f(g[3]); calc = p_chi(est, int(g[0])); gl = g[0]
                else: est, rep_op, rep_p = f(g[1]), g[2], f(g[3]); calc = p_r(est, int(g[0])); gl = g[0]
            except (ValueError, ZeroDivisionError):
                continue
            if rep_op == "=":
                # tolerancia por redondeo del p reportado (3 decimales)
                dec = len(re.search(r"[.,](\d+)", m.group(0).split("p")[-1]).group(1)) if re.search(r"[.,](\d+)", m.group(0).split("p")[-1]) else 3
                ok = abs(calc - rep_p) <= 0.5 * 10 ** -dec + 1e-9
            elif rep_op == "<":
                ok = calc < rep_p + 1e-9
            else:
                ok = calc > rep_p - 1e-9
            decision_distinta = (rep_p < 0.05) != (calc < 0.05) if rep_op == "=" else False
            pruebas.append({"texto": m.group(0).strip(), "prueba": nombre, "gl": gl, "estadistico": est,
                            "p_reportado": f"{rep_op}{rep_p}", "p_recalculado": round(calc, 4), "consistente": ok,
                            "cambia_decision_a_.05": decision_distinta})
    ps = [t["p_recalculado"] for t in pruebas]
    reportados = [f(x) for x in re.findall(r"\bp\s*=\s*(\.\d+|0[.,]\d+)", texto)]
    cerca = [p for p in reportados if 0.04 <= p < 0.05]
    justo_sobre = [p for p in reportados if 0.05 <= p < 0.06]
    resumen = {
        "pruebas_reconocidas": len(pruebas),
        "inconsistentes": sum(1 for t in pruebas if not t["consistente"]),
        "cambian_decision": sum(1 for t in pruebas if t["cambia_decision_a_.05"]),
        "p_reportados_total": len(reportados),
        "p_entre_.040_y_.049": len(cerca),
        "p_entre_.050_y_.059": len(justo_sobre),
        "nota": "Un exceso de p entre .040 y .049 frente a .050-.059 es señal, no prueba, de búsqueda selectiva de significancia. Solo pruebas en formato APA son reconocidas; las demás quedan como [BRECHA]."
    }
    json.dump({"resumen": resumen, "pruebas": pruebas}, sys.stdout, ensure_ascii=False, indent=2)
    print()

if __name__ == "__main__":
    main()
