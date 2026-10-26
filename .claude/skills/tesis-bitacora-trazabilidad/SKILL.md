---
name: tesis-bitacora-trazabilidad
description: Registra y verifica el proceso de una tesis o informe de investigación: reuniones con el profesor guía y atención a las observaciones, coherencia entre cronograma declarado y avance real, y respaldo de datos y versiones del documento. Compara el cronograma con el avance y detecta atrasos y dependencias críticas. Úsala para llevar la bitácora, preparar una reunión con el guía, planificar el cierre o probar que el proceso fue ordenado. Con modo Tutor enseña a gestionar el proyecto y a documentar.
---

# Bitácora y trazabilidad

Punto 10 del documento fuente. Evidencia **cómo** se hizo el trabajo, no sólo el resultado. Sirve al autor (control de su avance) y al guía o evaluador (evidencia del proceso).

Aplica `docs/tesis-agentes/CONTRATO.md`. Plantillas en `references/plantillas.md`.

## Flujo

### 1. Registro de reuniones y observaciones

Por cada reunión con el guía, registra con la plantilla de `references/plantillas.md`: fecha, asistentes, temas, **observaciones numeradas**, acuerdos, plazo y responsable. El registro lo redacta el autor; tú lo ordenas y le das estructura. No inventes reuniones ni acuerdos: lo que el usuario no te entregue queda como [BRECHA].

Luego controla la **trazabilidad de observaciones**: cada observación del guía o de la comisión pasa por los estados *Recibida → En trabajo → Atendida (dónde, en qué página) → Cerrada con el guía*. Observaciones recibidas hace más de dos reuniones sin cierre: Mayor. Observación descartada sin justificar al guía: Mayor.

### 2. Cronograma vs. avance

Pide el cronograma en CSV (`actividad,inicio,fin,avance_pct,dependencia`):

```bash
python3 -I .claude/skills/tesis-bitacora-trazabilidad/scripts/cronograma.py cronograma.csv --hoy AAAA-MM-DD
```

Entrega avance esperado vs. real por actividad y global, estado (*en plazo*, *con desvío* con atraso > 5 puntos, *atrasada* con atraso > 20) y las actividades que bloquean a otras. Es un cálculo lineal sobre fechas: no mide esfuerzo real. Tómalo como alerta, no como medición exacta.

| Hallazgo | Severidad |
|---|---|
| Actividad atrasada que bloquea otra | Mayor |
| Avance global real más de 20 puntos bajo el esperado a menos de un tercio del plazo restante | Mayor |
| Cronograma sin dependencias entre actividades | Menor |
| Cronograma no actualizado en más de un mes | Menor |
| Ausencia de plan para aplicación de instrumentos / terreno cuando depende de terceros | Mayor |

Si hay atraso, aplica la crítica regenerativa: [Atraso] → [Replanificación: reducir alcance, paralelizar, pedir apoyo, renegociar fechas] → [Verificación: alcanza el plazo restante y no compromete la pregunta ni la validez]. Recuerda recortar **alcance**, no rigor.

### 3. Respaldo de datos y versiones

Checklist (el autor responde; tú no ves su equipo):

- Al menos **dos copias** de datos y documento en lugares distintos (regla 3-2-1 como referencia).
- Nombres de archivo con fecha y versión (`tesis_v07_2026-10-26.docx`).
- Datos crudos conservados e intactos; las transformaciones se hacen sobre copias o con script.
- Registro de cambios mayores del documento (qué cambió y por qué).
- Control de acceso a datos con información personal (ver `tesis-auditor-metodologico`).
- Fecha de último respaldo comprobado.

Datos crudos sin respaldo o sobrescritos: Mayor. Sin control de versiones del documento: Menor.

### 4. Puntos de control

Propón hitos con criterio de salida, no solo fechas: anteproyecto aprobado, instrumento validado, datos recolectados y respaldados, análisis completo, borrador completo, revisión del guía, versión final y defensa.

### 5. Modo Tutor

Enseña a convertir una reunión en acuerdos verificables: "¿Qué quedó decidido? ¿Quién, qué y para cuándo?". El autor redacta la bitácora de su última reunión y tú revisas que cada observación tenga estado. Cierra con un ejercicio: priorizar tres atrasos ficticios por dependencia y proponer una replanificación.

## Detención

Detén e informa si no hay cronograma ni registro previo: ofrece construirlos desde cero con el autor, no los inventes.

## Informe final

Contrato más:

```
Reuniones registradas: N · Observaciones: N (atendidas N, en trabajo N, sin cerrar N)
Avance esperado vs. real: N% vs. N%
Actividades en riesgo y qué bloquean
Respaldo: copias N · versionado [sí/no] · último respaldo comprobado: fecha
```
