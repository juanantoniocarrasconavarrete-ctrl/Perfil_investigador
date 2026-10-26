#!/usr/bin/env python3
"""Compara dos documentos por fragmentos coincidentes (n-gramas de palabras) para detectar autoplagio
o reutilización no declarada entre trabajos del mismo autor. También busca la declaración de uso de IA.

NO sustituye a la herramienta institucional de similitud (no consulta Internet ni bases de datos).

Uso: python3 similitud_interna.py actual [anterior] [--n 8]
Salida JSON: porcentaje de n-gramas de 'actual' presentes en 'anterior', pasajes coincidentes más largos,
y declaración de IA en 'actual'.
"""
import argparse, json, re, unicodedata

def leer(ruta):
    if ruta.lower().endswith(".docx"):
        import docx
        return "\n".join(p.text for p in docx.Document(ruta).paragraphs)
    return open(ruta, encoding="utf-8", errors="replace").read()

def tokens(t):
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9ñ]+", t)

def pasajes(a, b, n):
    ng_b = {tuple(b[i:i+n]) for i in range(len(b) - n + 1)}
    marc = [tuple(a[i:i+n]) in ng_b for i in range(len(a) - n + 1)]
    res, i = [], 0
    while i < len(marc):
        if marc[i]:
            j = i
            while j < len(marc) and marc[j]: j += 1
            res.append((i, j + n - 1)); i = j
        else: i += 1
    return marc, res

DECL_IA = re.compile(r"(inteligencia artificial|chatgpt|claude|gemini|copilot|modelo de lenguaje|\bIA\b|generative ai|\bllm\b)", re.I)
DECL_CONTEXTO = re.compile(r"(declaro|declaraci[oó]n de uso|se utiliz[oó]|se emple[oó]|asistencia de|apoyo de).{0,120}(inteligencia artificial|chatgpt|claude|gemini|copilot|\bIA\b)", re.I | re.S)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("actual"); ap.add_argument("anterior", nargs="?"); ap.add_argument("--n", type=int, default=8)
    a = ap.parse_args()
    texto = leer(a.actual)
    salida = {"declaracion_ia": {"menciona_ia": bool(DECL_IA.search(texto)), "con_declaracion_explicita": bool(DECL_CONTEXTO.search(texto))}}
    if a.anterior:
        A, B = tokens(texto), tokens(leer(a.anterior))
        marc, res = pasajes(A, B, a.n)
        largos = sorted(res, key=lambda r: r[0] - r[1])[:10]
        salida["similitud_interna"] = {
            "n": a.n, "palabras_actual": len(A),
            "porcentaje_ngramas_coincidentes": round(100 * sum(marc) / max(1, len(marc)), 1),
            "pasajes_mas_largos": [{"palabras": e - s, "texto": " ".join(A[s:e])[:200]} for s, e in largos],
            "nota": "Coincidencia literal. Puede ser cita correcta, bibliografía o texto técnico habitual: interpretar con criterio, no como veredicto."}
    print(json.dumps(salida, ensure_ascii=False, indent=2))
