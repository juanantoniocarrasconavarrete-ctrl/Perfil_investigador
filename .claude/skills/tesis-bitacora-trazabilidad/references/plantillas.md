# Plantillas de bitácora

## Registro de reunión

```
Reunión N.º: …   Fecha: AAAA-MM-DD   Duración: …
Asistentes: …
Avance presentado desde la reunión anterior: …
Observaciones del guía:
  O-<N>.1 …
  O-<N>.2 …
Acuerdos (qué, quién, para cuándo):
  A-<N>.1 …
Próxima reunión: AAAA-MM-DD
```

## Seguimiento de observaciones

| ID | Origen (guía/comisión/revisión) | Fecha | Observación | Estado | Dónde se atendió | Cerrada con el guía |
|---|---|---|---|---|---|---|
| O-1.1 | | | | Recibida / En trabajo / Atendida / Cerrada | sección y página | sí/no |

## Cronograma (CSV para `scripts/cronograma.py`)

```
actividad,inicio,fin,avance_pct,dependencia
Marco teórico,2026-08-01,2026-09-15,100,
Instrumento,2026-09-01,2026-10-01,40,Marco teórico
```

Fechas AAAA-MM-DD. `dependencia` es el nombre exacto de la actividad que debe terminar antes (opcional).

## Registro de versiones

| Versión | Fecha | Cambios mayores | Motivo | Respaldo en |
|---|---|---|---|---|
| v01 | | | | |
