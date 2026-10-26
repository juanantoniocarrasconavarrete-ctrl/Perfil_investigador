#!/usr/bin/env python3
"""Audita la lista de referencias de un informe/tesis (formato APA 7 y estructura de fuentes).

Salida JSON por stdout con, por referencia, los defectos formales detectados, y un resumen
(proporción por tipo, antigüedad, duplicados, orden alfabético).

  --online   consulta Crossref por DOI (título y año). Sin red, la existencia queda como
             "no verificada": nunca se asume válida.
  --anio-actual AAAA   año de referencia para antigüedad (por defecto, año del sistema)
  --umbral-antiguedad N   años a partir de los cuales una fuente se marca como antigua (10)

Uso: python3 auditar_bibliografia.py archivo [--online]
"""
import argparse
import datetime
import difflib
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tesis-verificador-citas", "scripts"))
from extraer_citas import leer, separar, parse_referencia  # noqa: E402

DOI = re.compile(r"10\.\d{4,9}/[^\s]+", re.I)
TIPOS = [
    ("articulo", re.compile(r"\b\d+\s*\(\d+\)|\bvol\.|revista|journal|\bpp?\.\s?\d", re.I)),
    ("tesis", re.compile(r"tesis|thesis|dissertation|memoria de t[ií]tulo", re.I)),
    ("libro", re.compile(r"editorial|press\b|ediciones|publisher|\bed\.\)", re.I)),
    ("web", re.compile(r"https?://(?!doi\.org)", re.I)),
]


def tipo(txt):
    for nombre, rx in TIPOS:
        if rx.search(txt):
            return nombre
    return "indeterminado"


def defectos(txt, año):
    d = []
    if año is None:
        d.append("sin año de publicación")
    if not re.match(r"^[^\d(]+?,\s?[A-ZÁÉÍÓÚÑ]\.", txt):
        d.append("autor no sigue 'Apellido, I.' (verificar autor institucional)")
    if re.search(r"\bdoi:\s?10\.", txt, re.I):
        d.append("DOI con prefijo 'doi:'; APA 7 usa https://doi.org/…")
    m = DOI.search(txt)
    if m and "doi.org/" not in txt:
        d.append("DOI sin formato de URL (https://doi.org/…)")
    if m and m.group(0).rstrip(".,;") != m.group(0):
        d.append("DOI termina con signo de puntuación")
    if "dx.doi.org" in txt:
        d.append("URL obsoleta dx.doi.org")
    if not re.search(r"\)\.\s+\S", txt):
        d.append("falta punto tras el año o título ausente")
    if re.search(r"\bet al\.", txt.split("(")[0]):
        d.append("'et al.' en la lista de referencias: APA 7 lista hasta 20 autores")
    if tipo(txt) == "web" and not re.search(r"(Recuperado|Retrieved|https?://)", txt):
        d.append("fuente web sin URL")
    return d


def crossref(doi, titulo):
    try:
        req = urllib.request.Request(f"https://api.crossref.org/works/{doi}", headers={"User-Agent": "tesis-auditor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            m = json.load(r)["message"]
        t = (m.get("title") or [""])[0]
        sim = difflib.SequenceMatcher(None, t.lower(), titulo.lower()).ratio()
        return {"existe": True, "titulo_crossref": t, "similitud_titulo": round(sim, 2)}
    except urllib.error.HTTPError as e:
        return {"existe": False if e.code == 404 else None, "detalle": f"HTTP {e.code}"}
    except Exception as e:  # sin red, proxy, timeout
        return {"existe": None, "detalle": f"no verificable: {type(e).__name__}"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--anio-actual", type=int, default=datetime.date.today().year)
    ap.add_argument("--umbral-antiguedad", type=int, default=10)
    a = ap.parse_args()

    _, refs_l = separar(leer(a.archivo))
    if not refs_l:
        print(json.dumps({"error": "No se encontró encabezado 'Referencias' o 'Bibliografía'."}, ensure_ascii=False))
        sys.exit(2)

    salida, conteo, antiguas, vistos, duplicados = [], {}, [], {}, []
    for txt in refs_l:
        r = parse_referencia(txt)
        año = r["año"]
        t = tipo(txt)
        conteo[t] = conteo.get(t, 0) + 1
        item = {"referencia": txt[:120], "tipo": t, "defectos": defectos(txt, año)}
        m = re.match(r"\d{4}", año or "")
        if m and a.anio_actual - int(m.group(0)) > a.umbral_antiguedad:
            antiguas.append(txt[:80])
        clave = (r["autor"], año, re.sub(r"\W", "", txt.split(").", 1)[-1][:40].lower()))
        if clave in vistos:
            duplicados.append(txt[:80])
        vistos[clave] = True
        doi = DOI.search(txt)
        item["doi"] = doi.group(0).rstrip(".,;") if doi else None
        if a.online and item["doi"]:
            titulo = txt.split(").", 1)[-1].strip().split(".")[0]
            item["verificacion_crossref"] = crossref(item["doi"], titulo)
        elif not item["doi"] and t == "articulo":
            item["defectos"].append("artículo sin DOI: buscar en Crossref/PubMed o justificar su ausencia")
        salida.append(item)

    claves = [parse_referencia(x)["autor"] for x in refs_l]
    resumen = {
        "total": len(refs_l),
        "por_tipo": conteo,
        "proporcion_articulos": round(conteo.get("articulo", 0) / len(refs_l), 2),
        "proporcion_web": round(conteo.get("web", 0) / len(refs_l), 2),
        "antiguas": antiguas,
        "duplicados": duplicados,
        "orden_alfabetico": claves == sorted(claves),
        "con_doi": sum(1 for s in salida if s["doi"]),
        "doi_confirmados": sum(1 for s in salida if s.get("verificacion_crossref", {}).get("existe") is True),
        "doi_no_verificables": sum(1 for s in salida if s["doi"] and s.get("verificacion_crossref", {}).get("existe") is not True),
        "nota": "La existencia no se verifica sin --online o sin herramientas de búsqueda (Consensus, PubMed, Elicit)."
    }
    json.dump({"resumen": resumen, "referencias": salida}, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
