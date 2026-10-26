---
name: tesis-auditor-bibliografia
description: Audita la lista de referencias de una tesis, informe de investigación o informe técnico. Verifica formato APA 7, existencia de cada fuente y validez del DOI, datos bibliográficos correctos, proporción de fuentes primarias y revisadas por pares, actualidad y duplicados. Úsala cuando el usuario pida revisar la bibliografía, validar DOIs, detectar referencias inventadas por IA o evaluar la calidad de las fuentes. Con modo Tutor enseña a armar referencias.
---

# Auditor de bibliografía

Audita la **lista final**. El cruce con las citas del texto lo hace `tesis-verificador-citas`; la verificación de que la fuente respalda la afirmación, `tesis-verificador-respaldo-fuente`.

Aplica `docs/tesis-agentes/CONTRATO.md`.

## Flujo

### 1. Análisis formal automático

```bash
python3 -I .claude/skills/tesis-auditor-bibliografia/scripts/auditar_bibliografia.py <archivo>
```

Devuelve por referencia: tipo (artículo, libro, tesis, web), defectos de formato APA 7, DOI hallado, y un resumen con proporciones, antigüedad, duplicados y orden alfabético. El tipo se infiere por heurística: verifica los casos `indeterminado` a mano.

`--online` consulta Crossref por DOI. En este entorno el proxy bloquea Crossref y OpenAlex (403): el script lo informa como `no verificable`, **no** como válido. Usa `--online` solo si el usuario lo ejecuta en una máquina con red.

### 2. Verificar existencia con herramientas de búsqueda

La existencia es el control más importante: las referencias inventadas por IA suelen tener formato perfecto.

Orden de verificación por referencia (para en la primera que confirme):

1. DOI → `--online` (Crossref), si hay red.
2. Título + primer autor → Consensus (`search`), Elicit (`search_papers`), PubMed (`lookup_article_by_citation`) o Wiley Scholar.
3. Libros e informes: WebSearch por título exacto y editorial.

Para cada referencia, resultado posible:

| Resultado | Estatus | Severidad |
|---|---|---|
| Encontrada y metadatos coinciden (autores, año, título, revista, volumen, páginas) | [HECHO] | — |
| Encontrada pero con datos distintos (año, volumen, páginas, autores) | [HECHO] | Mayor |
| DOI no existe o apunta a otra obra | [HECHO] | Crítico |
| No encontrada tras 2 búsquedas con títulos exactos | [BRECHA]: *posible referencia inexistente* | Crítico si no se aclara con el autor |
| No pude consultar (límite de herramientas, sin red) | [BRECHA] | Informar, sin severidad |

**Nunca declares inexistente una referencia solo porque una búsqueda no la halló**: libros, informes institucionales y literatura gris no siempre se indexan. Pide al autor el enlace, PDF o ejemplar.

Si hay más de 40 referencias, verifica primero las que sustentan afirmaciones centrales del marco teórico y las conclusiones; declara en el informe cuántas verificaste y cuántas quedaron sin verificar.

### 3. Evaluar la calidad de la base documental

Informa como [INTERPRETACIÓN] y deja que el contexto lo matice:

- Proporción de artículos revisados por pares vs. web, blogs e informes sin revisión.
- Proporción de fuentes con más de 10 años; son legítimas si son referentes clásicos justificados en el texto.
- Dependencia de pocos autores (autocitación o autores repetidos en más del 25% de las referencias).
- Fuentes secundarias (manuales, apuntes, Wikipedia) usadas donde existe fuente primaria.
- Cobertura regional: para temas chilenos, presencia de fuentes nacionales (SciELO, Redalyc, informes oficiales, normativa vigente).

Para informes técnicos y normativos (Ley 20.949, ISO 11228, etc.) exige la norma o el documento oficial, no un resumen de terceros.

### 4. Defectos APA 7 frecuentes

DOI sin `https://doi.org/`, prefijo `doi:`, `dx.doi.org`, falta de cursiva (no detectable en texto plano: [BRECHA], revisar en el documento original), mayúsculas excesivas en títulos de artículos, `et al.` en la lista, ausencia de editorial en libros, sin fecha de consulta innecesaria en contenido estable. Todos Menor, salvo que impidan localizar la fuente (Mayor).

### 5. Modo Tutor

Elige las 3 referencias con más defectos y guía al autor: "¿Qué elementos de una referencia de artículo faltan aquí?" antes de mostrar la plantilla `Apellido, I., & Apellido, I. (Año). Título del artículo. *Revista, vol*(núm), pp-pp. https://doi.org/…`. Entrega un ejercicio con una referencia ficticia incompleta para que el autor la complete.

## Detención

Detén e informa si no hay lista de referencias detectable. No audites de memoria.

## Informe final

Contrato más:

```
Referencias: N · Con DOI: N · Verificadas como existentes: N · No verificadas: N
Proporciones: artículos X% · libros X% · web X% · >10 años X%
Referencias sospechosas (posible inexistencia): lista con la búsqueda hecha
Defectos APA 7: conteo por tipo
```
