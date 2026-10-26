#!/usr/bin/env python3
"""Revisa forma de un informe/tesis: numeración y mención de tablas/figuras, siglas sin definir y estructura.

Salida JSON:
  tablas/figuras   numeración detectada en títulos ("Tabla 3", "Figura 2"), saltos, duplicados,
                   títulos sin mención en el texto, menciones sin título, títulos sin 'Fuente' próxima
  siglas           siglas (2-6 mayúsculas) usadas ≥2 veces sin definición "Nombre (SIGLA)" ni glosario
  estructura       encabezados detectados y presencia de índice, resumen, anexos, referencias
Uso: python3 revisar_forma.py archivo   (.docx, .md, .txt). Solo lectura.
"""
import json
import re
import sys
from collections import Counter

def leer(ruta):
    if ruta.lower().endswith(".docx"):
        import docx
        return [p.text for p in docx.Document(ruta).paragraphs]
    return open(ruta, encoding="utf-8", errors="replace").read().splitlines()

def revisar(lineas, tipo, plural):
    titulo = re.compile(rf"^\s*\**{tipo}\s+(\d+)(?:\.(\d+))?\s*[.:\-–—]?\s*(.*)$", re.I)
    mencion = re.compile(rf"\b{tipo}\s+(\d+(?:\.\d+)?)", re.I)
    titulos, menciones = {}, Counter()
    for i, l in enumerate(lineas):
        m = titulo.match(l)
        if m and len(l) < 250:
            num = m.group(1) + (f".{m.group(2)}" if m.group(2) else "")
            titulos.setdefault(num, []).append(i)
        else:
            for mm in mencion.finditer(l):
                menciones[mm.group(1)] += 1
    out = {"numeros": sorted(titulos, key=lambda x: [int(p) for p in x.split(".")])}
    enteros = sorted(int(n.split(".")[0]) for n in titulos if "." not in n)
    out["saltos"] = [n for n in range(1, (enteros[-1] if enteros else 0) + 1) if "." not in str(n) and n not in enteros and not any(t.startswith(f"{n}.") for t in titulos)]
    out["titulos_duplicados"] = [n for n, v in titulos.items() if len(v) > 1]
    out["sin_mencion_en_texto"] = [n for n in titulos if menciones[n] == 0]
    out["mencion_sin_titulo"] = [n for n in menciones if n not in titulos]
    sin_fuente = []
    for n, idx in titulos.items():
        ventana = " ".join(lineas[idx[0]: idx[0] + 12]).lower()
        if not re.search(r"fuente|elaboraci[oó]n propia|adaptad|nota\.", ventana):
            sin_fuente.append(n)
    out["sin_fuente_cercana"] = sin_fuente
    return out

def siglas(lineas):
    texto = "\n".join(lineas)
    glosario = bool(re.search(r"^\s*#*\s*(glosario|lista de (siglas|abreviaturas)|siglas)\b", texto, re.I | re.M))
    cuenta = Counter(re.findall(r"\b[A-ZÁÉÍÓÚÑ]{2,6}\b", texto))
    ignorar = {"APA", "DOI", "URL", "PDF", "ISO", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI"}
    sin_def = []
    for s, n in cuenta.items():
        if n >= 2 and s not in ignorar and not re.search(rf"\(\s*{s}\s*\)", texto):
            sin_def.append({"sigla": s, "usos": n})
    return {"glosario_presente": glosario, "sin_definir": sorted(sin_def, key=lambda x: -x["usos"])[:30]}

def estructura(lineas):
    t = "\n".join(lineas).lower()
    chk = lambda rx: bool(re.search(rx, t, re.M))
    return {
        "indice": chk(r"^\s*#*\s*(índice|indice|tabla de contenido|contenidos)\b"),
        "resumen_abstract": chk(r"^\s*#*\s*(resumen|abstract)\b"),
        "introduccion": chk(r"^\s*#*\s*\d*\.?\s*introducci[oó]n"),
        "conclusiones": chk(r"^\s*#*\s*\d*\.?\s*conclusi"),
        "referencias": chk(r"^\s*#*\s*(referencias|bibliograf)"),
        "anexos": chk(r"^\s*#*\s*(anexos?|ap[eé]ndices?)\b"),
        "anexos_mencionados_en_texto": len(re.findall(r"\banexo\s+[a-z0-9]+", t)),
    }

if __name__ == "__main__":
    L = leer(sys.argv[1])
    json.dump({"tablas": revisar(L, "tabla", "tablas"), "figuras": revisar(L, "figura", "figuras"),
               "siglas": siglas(L), "estructura": estructura(L),
               "nota": "Heurístico: la numeración automática de Word (campos) puede no aparecer como texto. Verifica en el documento original."},
              sys.stdout, ensure_ascii=False, indent=2)
    print()
