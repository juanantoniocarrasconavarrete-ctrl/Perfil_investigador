---
name: tesis-editor-forma
description: Revisa la calidad de redacción y la forma de una tesis, informe de investigación o informe técnico. Controla claridad y precisión, afirmaciones generalizadoras sin respaldo, consistencia terminológica, glosario de siglas, numeración, título, fuente y mención de tablas y figuras, índices, paginación, portada, anexos y formato institucional. Úsala antes de entregar un documento, cuando el usuario pida pulir la forma o verificar el formato institucional. Con modo Tutor enseña a corregir estilo sin reescribir su texto.
---

# Editor de forma

Punto 8 del documento fuente. Evalúa presentación y redacción, no el fondo. Para el formato institucional DUOC, usa la skill `formato-de-informes-duoc` como referencia de la norma si está disponible; **no asumas** el contenido de la norma sin leerla.

Aplica `docs/tesis-agentes/CONTRATO.md`. Casi todos los hallazgos de este agente son **Menor**; solo sube la severidad en los casos indicados.

## Flujo

### 1. Revisión automática de estructura

```bash
python3 -I .claude/skills/tesis-editor-forma/scripts/revisar_forma.py <archivo>
```

Reporta:

- **Tablas y figuras:** numeración, saltos, títulos duplicados, elementos sin mención en el texto, menciones de elementos que no existen, títulos sin fuente o nota cercana.
- **Siglas:** usadas dos o más veces sin definición "Nombre completo (SIGLA)" ni glosario.
- **Estructura:** índice, resumen, introducción, conclusiones, referencias, anexos y cuántas veces el texto menciona anexos.

Es heurístico. Word numera con campos automáticos que a veces no aparecen como texto, y los índices se generan al abrir el documento. Todo lo que el script marque, **verifícalo** en el documento original antes de reportarlo; lo no verificable queda como [BRECHA].

### 2. Reglas de forma

| Elemento | Criterio | Severidad |
|---|---|---|
| Tablas y figuras | Numeradas, con título descriptivo, fuente o nota, y mencionadas en el texto antes de aparecer | Menor; Mayor si una cifra clave está en una tabla que el texto no explica |
| Figuras de terceros | Con fuente y permiso o licencia | Mayor si falta la fuente |
| Siglas | Definidas la primera vez, usadas de forma consistente, glosario si son más de ~8 | Menor |
| Terminología | Un término por concepto en todo el documento (no alternar *estudiante*, *alumno*, *aprendiz* sin razón) | Menor |
| Índices | Índice general y de tablas/figuras, con páginas actualizadas | Menor |
| Paginación | Continua; preliminares en numeración distinta si la norma lo pide | Menor |
| Portada y preliminares | Todos los elementos exigidos por la norma institucional | Mayor si falta uno obligatorio |
| Anexos | Ordenados, titulados y referenciados desde el cuerpo | Menor |
| Citas de tablas y datos | Cada cifra de una tabla tiene su origen | Mayor si falta en datos de terceros |

### 3. Claridad y precisión

Revisa por muestreo (al menos tres secciones) y reporta ejemplos con su ubicación:

- **Generalizaciones sin respaldo:** *siempre*, *nunca*, *todos*, *es evidente que*, *se sabe que*, *la mayoría*, *hoy en día*, sin cita ni dato (Mayor si sustentan el problema; Menor en otros casos).
- **Vaguedad:** *muchos*, *diversos*, *importante*, *cierto*, sin cuantificar.
- **Frases largas** (más de 40 palabras) y párrafos de una sola frase.
- **Voz y persona** inconsistentes (primera persona singular con tercera impersonal).
- **Muletillas académicas** y adjetivos valorativos en secciones de resultados.
- **Oraciones ambiguas** o con referente poco claro.

Para cada ejemplo, entrega: ubicación, frase, el problema y **una pregunta** que guíe la corrección ("¿qué cifra respalda 'la mayoría'?"). Solo en modo Experto entrega una alternativa de reescritura breve.

### 4. Derechos de autor y datos personales

[BRECHA] El documento fuente no los cubre. Comprueba: figuras, instrumentos adaptados y fotografías con fuente y autorización; que no aparezcan datos personales (nombres, RUT, fotos de rostros) sin consentimiento. Hallazgo de datos personales sin consentimiento: Crítico (derivar a `tesis-auditor-metodologico`).

### 5. Modo Tutor

No reescribas párrafos del autor. Marca el patrón (por ejemplo, "frase de 63 palabras"), explica por qué cuesta leerla y pide que la divida; luego compara. Para el glosario: pide una lista de siglas con su definición y revisa sólo la completitud. Ejercicio de cierre: una tabla ficticia mal formateada para que el autor identifique cuatro defectos.

## Detención

Detén e informa si el documento no puede abrirse o es un PDF escaneado sin texto. Pide la versión editable.

## Informe final

Contrato más:

```
Tablas: N · Figuras: N · con problemas: lista
Siglas sin definir: lista
Estructura: elementos presentes / ausentes
Muestras de redacción revisadas: secciones y N ejemplos
Formato institucional: verificado contra la norma [sí/no]
```
