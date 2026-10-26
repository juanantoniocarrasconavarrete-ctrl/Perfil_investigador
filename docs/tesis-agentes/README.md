# Agentes para tesis e informes

Basados en el documento "Elementos a considerar al revisar una tesis". Contrato común en `CONTRATO.md`.

| Agente (`.claude/skills/…`) | Punto del documento | Código |
|---|---|---|
| `tesis-orquestador-revision` | Todos | — |
| `tesis-alineacion-pregunta-metodo` | 1 | — |
| `tesis-cartografo-literatura` | 2 | `references/matriz-literatura.md` |
| `tesis-auditor-metodologico` | 3 | `references/criterios.md` |
| `tesis-auditor-estadistico` | 4 | `scripts/statcheck.py` |
| `tesis-revisor-resultados-conclusiones` | 5 | — |
| `tesis-verificador-citas` | 6 | `scripts/extraer_citas.py` |
| `tesis-auditor-bibliografia` | 6, 2 | `scripts/auditar_bibliografia.py` |
| `tesis-verificador-respaldo-fuente` | 6 | — |
| `tesis-guardian-integridad` | 7 | `scripts/similitud_interna.py` |
| `tesis-simulador-defensa` | 7 | — |
| `tesis-editor-forma` | 8 | `scripts/revisar_forma.py` |
| `tesis-evaluador-aporte-viabilidad` | 9 | — |
| `tesis-bitacora-trazabilidad` | 10 | `scripts/cronograma.py`, `references/plantillas.md` |

## Requisitos

Python 3.9+. `python-docx` solo para leer `.docx`. Sin otras dependencias (no requieren scipy).

## Límites conocidos

- Crossref/OpenAlex pueden estar bloqueados en entornos restringidos; la existencia de referencias se verifica entonces con Consensus, Elicit o PubMed.
- Los scripts son heurísticos: los agentes validan cada hallazgo a mano antes de reportarlo.
- `similitud_interna.py` no reemplaza la herramienta institucional de similitud.
- Pendiente de verificar en fuente oficial: vigencia de la Ley 21.719.
