#!/usr/bin/env python3
"""Compara el cronograma declarado con el avance real.

CSV con encabezado: actividad,inicio,fin,avance_pct,dependencia   (fechas AAAA-MM-DD; dependencia opcional = nombre de otra actividad)
Salida JSON: avance esperado por actividad a la fecha, atraso en puntos, ruta crítica simple y actividades en riesgo.
Uso: python3 cronograma.py cronograma.csv [--hoy AAAA-MM-DD]
"""
import argparse, csv, datetime as dt, json

def d(s): return dt.date.fromisoformat(s.strip())

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--hoy", default=dt.date.today().isoformat())
    a = ap.parse_args(); hoy = d(a.hoy)
    filas = list(csv.DictReader(open(a.csv, encoding="utf-8")))
    out, riesgo = [], []
    for f in filas:
        ini, fin = d(f["inicio"]), d(f["fin"])
        dur = max(1, (fin - ini).days)
        esperado = 100 if hoy >= fin else 0 if hoy <= ini else round(100 * (hoy - ini).days / dur)
        real = float(f["avance_pct"] or 0)
        atraso = esperado - real
        est = "atrasada" if atraso > 20 else "con desvío" if atraso > 5 else "en plazo"
        dep = (f.get("dependencia") or "").strip()
        bloquea = [g["actividad"] for g in filas if (g.get("dependencia") or "").strip() == f["actividad"]]
        item = {"actividad": f["actividad"], "esperado_pct": esperado, "real_pct": real, "atraso_pts": round(atraso), "estado": est,
                "bloquea_a": bloquea, "dias_restantes": (fin - hoy).days}
        out.append(item)
        if est != "en plazo" or (hoy > fin and real < 100): riesgo.append(item["actividad"])
    total_dur = sum(max(1, (d(f["fin"]) - d(f["inicio"])).days) for f in filas)
    ponderado_esp = sum(o["esperado_pct"] * max(1, (d(f["fin"]) - d(f["inicio"])).days) for o, f in zip(out, filas)) / total_dur
    ponderado_real = sum(o["real_pct"] * max(1, (d(f["fin"]) - d(f["inicio"])).days) for o, f in zip(out, filas)) / total_dur
    print(json.dumps({"fecha": hoy.isoformat(), "avance_esperado_global": round(ponderado_esp), "avance_real_global": round(ponderado_real),
                      "en_riesgo": riesgo, "actividades": out}, ensure_ascii=False, indent=2))
