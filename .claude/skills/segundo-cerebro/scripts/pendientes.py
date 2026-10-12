#!/usr/bin/env python3
"""Clasifica los archivos de entrada del segundo cerebro.

Salida JSON por stdout con tres listas:
  pendientes      archivos legibles cuyo contenido (sha256) aún no está registrado
  ya_procesados   archivos cuyo contenido ya figura en el registro (se omiten)
  omitidos        archivos con formato no admitido o vacíos, con motivo

Uso: python3 pendientes.py [--entradas /entradas] [--cerebro /cerebro]
Solo lectura: no modifica ningún archivo.
"""
import argparse
import hashlib
import json
import os
import sys

FORMATOS = {".md", ".txt", ".vtt", ".srt", ".csv", ".json", ".pdf", ".docx"}


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cargar_registro(ruta):
    if not os.path.exists(ruta):
        return {}
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)  # un registro corrupto debe detener la ejecución
    return {e["sha256"]: e for e in datos.get("procesados", [])}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--entradas", default="/entradas")
    p.add_argument("--cerebro", default="/cerebro")
    a = p.parse_args()

    if not os.path.isdir(a.entradas):
        sys.exit(f"ERROR: no existe la carpeta de entradas: {a.entradas}")

    registro = cargar_registro(os.path.join(a.cerebro, ".procesados.json"))
    res = {"pendientes": [], "ya_procesados": [], "omitidos": []}

    for raiz, _, nombres in os.walk(a.entradas):
        for nombre in sorted(nombres):
            if nombre.startswith("."):
                continue
            ruta = os.path.join(raiz, nombre)
            rel = os.path.relpath(ruta, a.entradas)
            ext = os.path.splitext(nombre)[1].lower()
            if ext not in FORMATOS:
                res["omitidos"].append({"archivo": rel, "motivo": f"formato no admitido ({ext or 'sin extensión'})"})
                continue
            if os.path.getsize(ruta) == 0:
                res["omitidos"].append({"archivo": rel, "motivo": "archivo vacío"})
                continue
            try:
                digest = sha256(ruta)
            except OSError as e:
                sys.exit(f"ERROR de lectura en {rel}: {e}")
            if digest in registro:
                res["ya_procesados"].append({"archivo": rel, "sha256": digest, "nota": registro[digest].get("nota")})
            else:
                res["pendientes"].append({"archivo": rel, "sha256": digest})

    json.dump(res, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
