#!/usr/bin/env python3
"""Extrae citas en texto y lista de referencias de un informe/tesis y las cruza (APA 7).

Entrada: .docx, .md o .txt. Salida JSON por stdout:
  citas            citas detectadas en el cuerpo (autor, año, página, contexto)
  referencias      entradas de la lista final (autor, año, texto)
  huerfanas        citas del texto sin referencia en la lista
  sin_citar        referencias que ninguna cita del texto menciona
  textuales        citas textuales sin página o que superan 40 palabras
  advertencias     seccion de referencias no hallada, etc.

Uso: python3 extraer_citas.py archivo [--indent 2]
Solo lectura. No usa red.
"""
import argparse
import json
import re
import sys
import unicodedata

ENCABEZADOS = re.compile(r"^\s*#*\s*(referencias( bibliogr[aá]ficas)?|bibliograf[ií]a)\s*$", re.I)
AÑO = r"(?:\d{4}[a-z]?|s\.\s?f\.|en prensa)"
AUTOR = r"[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñü'’\-]+(?:\s(?:de|del|la|van|von|da)\s[A-ZÁÉÍÓÚÑ][\wáéíóúñü'’\-]+)?"
GRUPO = rf"{AUTOR}(?:(?:,\s{AUTOR})*(?:,?\s(?:&|y|and)\s{AUTOR})|\set\sal\.)?"
# Parentética: (Autor, 2020), (Autor & Autor, 2020, p. 4), (Autor, 2020; Otro et al., 2019)
RE_PAREN = re.compile(r"\(([^()]*?" + AÑO + r"[^()]*?)\)")
# Narrativa: Autor (2020), Autor y Autor (2020), Autor et al. (2020)
RE_NARR = re.compile(rf"({GRUPO})\s\((" + AÑO + r")(?:,\s(pp?\.\s?[\d\-–, ]+))?\)")
RE_SEG = re.compile(rf"({GRUPO}),\s({AÑO})(?:,\s(pp?\.\s?[\d\-–, ]+))?")


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s)


def leer(ruta):
    if ruta.lower().endswith(".docx"):
        import docx
        return [p.text for p in docx.Document(ruta).paragraphs]
    with open(ruta, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def separar(lineas):
    for i, l in enumerate(lineas):
        if ENCABEZADOS.match(l) and len(l) < 40:
            return lineas[:i], [x for x in lineas[i + 1:] if x.strip()]
    return lineas, []


def primer_autor(texto):
    return norm(re.split(r"[,&]| y | et al| and ", texto.strip(), maxsplit=1)[0])


def parse_referencia(txt):
    m = re.search(r"\((" + AÑO + r")\)", txt)
    return {"autor": primer_autor(txt), "año": m.group(1).lower().replace(" ", "") if m else None, "texto": txt.strip()}


def citas_en(cuerpo):
    citas = []
    for m in RE_NARR.finditer(cuerpo):
        citas.append({"autor": primer_autor(m.group(1)), "autor_texto": m.group(1), "año": m.group(2).lower().replace(" ", ""),
                      "pagina": m.group(3), "forma": "narrativa", "pos": m.start()})
    for m in RE_PAREN.finditer(cuerpo):
        for seg in m.group(1).split(";"):
            s = RE_SEG.search(seg.strip())
            if s:
                citas.append({"autor": primer_autor(s.group(1)), "autor_texto": s.group(1),
                              "año": s.group(2).lower().replace(" ", ""), "pagina": s.group(3),
                              "forma": "parentetica", "pos": m.start()})
    return citas


def textuales(cuerpo):
    out = []
    for m in re.finditer(r"[“\"]([^”\"]{20,}?)[”\"]", cuerpo):
        n = len(m.group(1).split())
        if n < 5:
            continue
        cola = cuerpo[m.end():m.end() + 120]
        cita = re.search(r"\(([^()]*" + AÑO + r"[^()]*)\)", cola)
        if not (cita and re.search(r"pp?\.", cita.group(1))):
            out.append({"cita": m.group(1)[:80], "palabras": n, "problema": "sin número de página"})
        if n >= 40:
            out.append({"cita": m.group(1)[:80], "palabras": n, "problema": "≥40 palabras: debe ir en bloque sin comillas (APA 7)"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--indent", type=int, default=2)
    a = ap.parse_args()
    cuerpo_l, refs_l = separar(leer(a.archivo))
    adv = []
    if not refs_l:
        adv.append("No se encontró un encabezado 'Referencias' o 'Bibliografía': no se pudo cruzar con la lista final.")
    cuerpo = "\n".join(cuerpo_l)
    citas = citas_en(cuerpo)
    refs = [parse_referencia(r) for r in refs_l]
    claves = {(r["autor"], r["año"]) for r in refs}
    cit_claves = {(c["autor"], c["año"]) for c in citas}
    huerfanas = sorted({(c["autor_texto"], c["año"]) for c in citas if refs_l and (c["autor"], c["año"]) not in claves})
    sin_citar = [r["texto"][:100] for r in refs if (r["autor"], r["año"]) not in cit_claves]
    for r in refs:
        if r["año"] is None:
            adv.append(f"Referencia sin año reconocible: {r['texto'][:80]}")
    for c in citas:
        c.pop("pos")
    json.dump({"citas": citas, "referencias": refs, "huerfanas": [list(h) for h in huerfanas], "sin_citar": sin_citar,
               "textuales": textuales(cuerpo), "advertencias": adv}, sys.stdout, ensure_ascii=False, indent=a.indent)
    print()


if __name__ == "__main__":
    main()
