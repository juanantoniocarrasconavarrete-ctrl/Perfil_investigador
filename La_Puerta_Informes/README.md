# Proyecto La Puerta — informes de análisis (encuesta oct. 2026, n = 184)

Entregables (carpeta `informes/` e `infografias/`):

| Cód. | Producto | Archivo |
|---|---|---|
| A | Informe descriptivo (sin hipótesis) | `informes/A_Informe_Descriptivo.docx` / `.pdf` |
| B | Informe con hipótesis | `informes/B_Informe_Hipotesis.docx` / `.pdf` |
| C | Informe consolidado | `informes/C_Informe_Consolidado.docx` / `.pdf` |
| D | Infografía 1 (estudio y resultados) | `infografias/D_Infografia_1_Estudio_y_Resultados.png` / `.pdf` |
| E | Infografía 2 (hipótesis y factores) | `infografias/E_Infografia_2_Hipotesis_y_Factores.png` / `.pdf` |
| F | Manual explicativo de resultados | `informes/F_Manual_Explicativo_Resultados.docx` / `.pdf` |
| G | Manual de propuestas de mejora | `informes/G_Manual_Propuestas_Mejora.docx` / `.pdf` |
| H | Infografía comparativa de brechas | `infografias/H_Infografia_Comparativa_de_Brechas.png` / `.pdf` |
| I | Estudio paralelo de investigación (lenguaje cotidiano) | `informes/I_Estudio_Paralelo_Investigacion.docx` / `.pdf` |
| J | Infografía comparada: La Puerta vs. investigación | `infografias/J_Infografia_Comparada_Investigacion.png` / `.pdf` |

## Descarga rápida

Todos los productos en un solo archivo: `descargas/Proyecto_La_Puerta_Productos.zip` (informes en Word/PDF e infografías en PNG/PDF, con `LEEME.txt`). En GitHub: abrir el archivo y pulsar **Download**.

## Formato Duoc UC

Los cinco documentos siguen la norma de informes de Bibliotecas Duoc UC: tamaño carta, márgenes normales, Calibri 11, interlineado 1,5, texto justificado, numeración de página (excepto portada), portada con título en mayúscula (14 pt, negrita, sin punto final) y filete amarillo, índice con páginas, y estructura Introducción → Desarrollo → Conclusión → Referencias (APA 7) → Anexos. Paleta: negro #1A1A1A, amarillo #FFB800, gris #666666 y gris claro #EEEEEE. Las infografías usan la misma paleta.

**Pendiente:** insertar el logo oficial de Duoc UC en el recuadro «[Insertar logo Duoc UC]» de cada portada e infografía (no se generó ni se imitó el logo). Revisar en la portada los datos de autor/docente y la asignatura.

## Reproducir

```bash
cd src
python3 -I analisis.py "<ruta>/Proyecto_La_Puerta_-_Base_de_Datos_y_Matriz_de_Analisis.xlsx"   # genera resultados.json y datos_limpios.pkl
python3 -I graficos.py                                                                           # genera ../graficos/*.png
for f in A B C F G; do python3 build_$f.py; done                                                 # genera los .docx
python3 paginar.py A_Informe_Descriptivo B_Informe_Hipotesis C_Informe_Consolidado F_Manual_Explicativo_Resultados G_Manual_Propuestas_Mejora  # calcula páginas del índice (luego repetir build_*.py)
python3 build_info.py                                                                            # genera las infografías (requiere Chromium)
```

La base original **no** se versiona (contiene correos electrónicos). `datos_limpios.pkl` tampoco (se regenera).

## Limitaciones conocidas

- **Estudio paralelo (I, J):** la búsqueda se hizo en la web el 18-oct-2026 y solo se pudieron leer resúmenes (el entorno no permitió abrir textos completos). Varios datos de cita están marcados «por confirmar». No se revisaron a fondo estudios chilenos.

- La base es de **un solo momento**; `Código_Estudiante`, `Momento_Medición`, `Grupo_Asignación` y `POST_EXP1` están vacíos, por lo que **no se puede evaluar el efecto de La Puerta** (H6).
- El instrumento aplicado (15 ítems, D1–D5) difiere del descrito en el Informe Metodológico (A02–A04, COM/EQ/AUT/RES/ET); se usó una equivalencia aproximada.
- La codificación de respuestas abiertas es automática y preliminar; requiere doble codificación humana.
- Las referencias bibliográficas no se verificaron en línea; confirmar antes de publicar.
- Los costos del Manual G son estimaciones gruesas a validar.

Elaborado con apoyo de IA (Claude, Anthropic).
