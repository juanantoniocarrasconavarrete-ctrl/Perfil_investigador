import json, re, io
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement
import numpy as np
from PIL import Image, ImageDraw

R = json.load(open('/home/user/Perfil_investigador/La_Puerta_Informes/src/resultados.json'))
G = '/home/user/Perfil_investigador/La_Puerta_Informes/graficos/'
NAVY, AMB, TEAL, CORAL, GRAY, LG, SKY = '1B2A49', 'F2A900', '1F8A8A', 'E4572E', '8892A6', 'EEF1F6', '4C8BD6'
FONT = 'Calibri'

def n(x, d=2):  # número con coma decimal
    return f'{x:.{d}f}'.replace('.', ',')
def pc(x, d=0): return n(x, d) + ' %'
def pv(p):
    return 'p < 0,001' if p < 0.001 else 'p = ' + n(p, 3 if p < 0.01 else 2)

def shade(cell, hexcolor):
    cell._tc.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{hexcolor}"/>'))
def cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr(); m = OxmlElement('w:tcMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); m.append(e)
    tcPr.append(m)
def borders(table, color='D5DAE3', sz=4, inside=True):
    tbl = table._tbl; tblPr = tbl.tblPr; b = OxmlElement('w:tblBorders')
    for k in ['top', 'left', 'bottom', 'right'] + (['insideH', 'insideV'] if inside else []):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), str(sz)); e.set(qn('w:color'), color); b.append(e)
    tblPr.append(b)
def no_borders(table):
    tblPr = table._tbl.tblPr; b = OxmlElement('w:tblBorders')
    for k in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        e = OxmlElement(f'w:{k}'); e.set(qn('w:val'), 'nil'); b.append(e)
    tblPr.append(b)
def set_col_widths(table, widths):
    table.autofit = False
    tbl = table._tbl; tblPr = tbl.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    tw = tblPr.find(qn('w:tblW'))
    if tw is None: tw = OxmlElement('w:tblW'); tblPr.append(tw)
    tw.set(qn('w:type'), 'dxa'); tw.set(qn('w:w'), str(int(sum(widths) * 567)))
    grid = tbl.tblGrid
    for gc in list(grid): grid.remove(gc)
    for w in widths:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(int(w * 567))); grid.append(gc)
    for row in table.rows:
        for i, w in enumerate(widths): row.cells[i].width = Cm(w)
def keep_row(row):
    trPr = row._tr.get_or_add_trPr(); e = OxmlElement('w:cantSplit'); trPr.append(e)
def repeat_header(row):
    trPr = row._tr.get_or_add_trPr(); e = OxmlElement('w:tblHeader'); e.set(qn('w:val'), 'true'); trPr.append(e)

def runs(p, text, size=None, color=None, bold=None, italic=None):
    """Soporta **negrita** y _cursiva_ simples."""
    for part in re.split(r'(\*\*.+?\*\*)', text):
        if not part: continue
        b = part.startswith('**') and part.endswith('**')
        r = p.add_run(part[2:-2] if b else part); r.font.name = FONT; r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor.from_string(color)
        r.bold = True if (b or bold) else None
        if italic: r.italic = True
    return p

class Doc:
    def __init__(self, titulo, subtitulo, codigo, cover_img, header_text):
        self.d = Document(); self.titulo = titulo; d = self.d
        s = d.sections[0]; s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = Cm(2.2); s.top_margin = Cm(2.3); s.bottom_margin = Cm(2.0)
        st = d.styles['Normal']; st.font.name = FONT; st.font.size = Pt(10.5); st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.12
        for nm, sz, col, sb, sa in (('Heading 1', 20, NAVY, 18, 8), ('Heading 2', 14, TEAL, 14, 4), ('Heading 3', 11.5, NAVY, 10, 2)):
            h = d.styles[nm]; h.font.name = FONT; h.font.size = Pt(sz); h.font.bold = True; h.font.color.rgb = RGBColor.from_string(col)
            h.element.rPr.rFonts.set(qn('w:eastAsia'), FONT); h.element.rPr.rFonts.set(qn('w:ascii'), FONT); h.element.rPr.rFonts.set(qn('w:hAnsi'), FONT)
            h.paragraph_format.space_before = Pt(sb); h.paragraph_format.space_after = Pt(sa); h.paragraph_format.keep_with_next = True
        self.W = 16.6; self.header_text = header_text; self._cover(titulo, subtitulo, codigo, cover_img)
    # portada: sección propia sin encabezado
    def _cover(self, titulo, subtitulo, codigo, img):
        d = self.d; s = d.sections[0]; s.different_first_page_header_footer = True
        t = d.add_table(rows=1, cols=1); no_borders(t); c = t.rows[0].cells[0]; shade(c, NAVY); c.width = Cm(self.W); cell_margins(c, 700, 500, 500, 500); set_col_widths(t, [self.W])
        trPr = t.rows[0]._tr.get_or_add_trPr(); hh = OxmlElement('w:trHeight'); hh.set(qn('w:val'), str(int(24.6 * 567))); hh.set(qn('w:hRule'), 'exact'); trPr.append(hh)
        p = c.paragraphs[0]; runs(p, 'PROYECTO LA PUERTA', 11, AMB, bold=True); p.paragraph_format.space_after = Pt(2)
        p = c.add_paragraph(); runs(p, 'Duoc UC · Escuela de Administración y Negocios · Sede San Bernardo', 9.5, 'C9D1E3')
        c.add_paragraph().paragraph_format.space_after = Pt(60)
        p = c.add_paragraph(); runs(p, codigo, 10, AMB, bold=True)
        p = c.add_paragraph(); runs(p, titulo, 30, 'FFFFFF', bold=True); p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_after = Pt(8)
        p = c.add_paragraph(); runs(p, subtitulo, 13, 'DDE3F0'); p.paragraph_format.space_after = Pt(30)
        if img:
            p = c.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.add_run().add_picture(img, width=Cm(11.5))
        c.add_paragraph().paragraph_format.space_after = Pt(18)
        p = c.add_paragraph(); runs(p, f"Encuesta de percepción y competencias · {R['N']} estudiantes · aplicada del 13 al 16 de octubre de 2026", 9.5, 'C9D1E3')
        p = c.add_paragraph(); runs(p, 'Elaborado con apoyo de herramientas de Inteligencia Artificial (ver declaración al final) · Octubre de 2026', 9, 'AEB8CF')
        # header/footer normales
        hp = s.header.paragraphs[0]; runs(hp, self.header_text, 8.5, GRAY); hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT; runs(fp, 'Proyecto La Puerta · Página ', 8.5, GRAY); self._field(fp, 'PAGE')
    def _field(self, p, code):
        r = p.add_run(); r.font.size = Pt(8.5); r.font.color.rgb = RGBColor.from_string(GRAY)
        for t, txt in (('begin', None), (None, code), ('end', None)):
            if t: e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), t)
            else: e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt
            r._r.append(e)
    def pagebreak(self): self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    def h1(self, t, newpage=True):
        h = self.d.add_heading(t, 1)
        if newpage: h.paragraph_format.page_break_before = True
        return h
    def h2(self, t): return self.d.add_heading(t, 2)
    def h3(self, t): return self.d.add_heading(t, 3)
    def p(self, t, size=None, color=None, italic=False, align=None, after=None):
        p = self.d.add_paragraph(); runs(p, t, size, color, italic=italic)
        if align == 'c': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if after is not None: p.paragraph_format.space_after = Pt(after)
        return p
    def bullets(self, items, size=None):
        for it in items:
            p = self.d.add_paragraph(style='List Bullet'); runs(p, it, size); p.paragraph_format.space_after = Pt(3)
    def numbered(self, items):
        for i, it in enumerate(items, 1):
            p = self.d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.9); p.paragraph_format.first_line_indent = Cm(-0.6); p.paragraph_format.space_after = Pt(4)
            runs(p, f'**{i}.**  ' + it)
    def callout(self, titulo, texto, color=TEAL, bg=None, icon=''):
        t = self.d.add_table(rows=1, cols=2); no_borders(t); a, b = t.rows[0].cells; a.width = Cm(.35); b.width = Cm(self.W - .35)
        shade(a, color); shade(b, bg or 'F3F6FA'); cell_margins(b, 120, 120, 200, 160); cell_margins(a, 0, 0, 0, 0); keep_row(t.rows[0])
        p = b.paragraphs[0]; runs(p, (icon + ' ' if icon else '') + titulo, 10.5, color, bold=True); p.paragraph_format.space_after = Pt(2)
        for line in (texto if isinstance(texto, list) else [texto]):
            q = b.add_paragraph(); runs(q, line, 10); q.paragraph_format.space_after = Pt(2)
        set_col_widths(t, [.35, self.W - .35]); self.d.add_paragraph().paragraph_format.space_after = Pt(2)
    def kpis(self, items):  # [(valor, etiqueta, color)]
        k = len(items); t = self.d.add_table(rows=1, cols=k); no_borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, (v, lab, col) in enumerate(items):
            c = t.rows[0].cells[i]; c.width = Cm(self.W / k); shade(c, 'F3F6FA'); cell_margins(c, 140, 140, 120, 120)
            tcPr = c._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders'); e = OxmlElement('w:top'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '24'); e.set(qn('w:color'), col); b.append(e); tcPr.append(b)
            p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; runs(p, v, 22, col, bold=True); p.paragraph_format.space_after = Pt(0)
            q = c.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER; runs(q, lab, 8.8, '2B3548'); q.paragraph_format.space_after = Pt(0)
        set_col_widths(t, [self.W / k] * k); self.d.add_paragraph().paragraph_format.space_after = Pt(2)
    def table(self, header, rows, widths, hcolor=NAVY, size=9, zebra=True, colors=None, align=None):
        t = self.d.add_table(rows=1, cols=len(header)); borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, h in enumerate(header):
            c = t.rows[0].cells[i]; shade(c, hcolor); cell_margins(c, 70, 70, 90, 90); p = c.paragraphs[0]; runs(p, h, size, 'FFFFFF', bold=True); p.paragraph_format.space_after = Pt(0)
        repeat_header(t.rows[0])
        for ri, row in enumerate(rows):
            r = t.add_row(); keep_row(r)
            for i, v in enumerate(row):
                c = r.cells[i]; cell_margins(c, 60, 60, 90, 90); c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                if zebra and ri % 2: shade(c, 'F7F9FC')
                p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
                col = None
                if colors and colors.get((ri, i)): shade(c, colors[(ri, i)]); col = NAVY if colors[(ri, i)] in (AMB, 'FFE9A8', 'D9F0E4', 'FBD5CB', 'DCE9F8', 'F0F3F8') else 'FFFFFF'
                runs(p, str(v), size, col, bold=bool(col) and col == 'FFFFFF')
                if align and align[i] == 'c': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_col_widths(t, widths); self.d.add_paragraph().paragraph_format.space_after = Pt(2); return t
    def fig(self, name, caption, width=16.2):
        p = self.d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True; p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(G + name + '.png', width=Cm(width))
        q = self.d.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER; runs(q, caption, 8.8, GRAY, italic=True); q.paragraph_format.space_after = Pt(10)
    def lee(self, texto):  # "cómo leerlo"
        self.callout('Cómo leer este gráfico', texto, SKY, 'EEF4FB')
    def save(self, path): self.d.save(path)

def cover_art(name, accent=AMB):
    """Puerta/arco estilizado (ilustración propia)."""
    W, H = 1400, 700; im = Image.new('RGB', (W, H), (27, 42, 73)); d = ImageDraw.Draw(im)
    rng = np.random.default_rng(7)
    for _ in range(70):
        x, y, r = rng.integers(0, W), rng.integers(0, H), rng.integers(2, 6); d.ellipse((x - r, y - r, x + r, y + r), fill=(60, 80, 120))
    cx = W // 2
    for i, (w, col) in enumerate([(430, (38, 58, 98)), (340, (76, 139, 214)), (250, (31, 138, 138)), (205, (242, 169, 0))]):
        top = 60 + i * 45; d.rounded_rectangle((cx - w // 2, top, cx + w // 2, H + 80), radius=w // 2, fill=col)
    d.rounded_rectangle((cx - 85, 190, cx + 85, H + 80), radius=85, fill=(27, 42, 73))
    for k, (x, y) in enumerate([(cx - 420, 520), (cx - 520, 470), (cx + 440, 500), (cx + 540, 450)]):
        d.ellipse((x - 26, y - 26, x + 26, y + 26), fill=(242, 169, 0) if k % 2 else (76, 139, 214)); d.rectangle((x - 18, y + 26, x + 18, 600), fill=(242, 169, 0) if k % 2 else (76, 139, 214))
    d.line((cx - 600, 600, cx + 600, 600), fill=(76, 139, 214), width=4)
    path = f'/home/user/Perfil_investigador/La_Puerta_Informes/graficos/{name}.png'; im.save(path); return path

# ---- textos compartidos ----
BIB = [
 'Bandura, A. (1997). *Self-efficacy: The exercise of control*. W. H. Freeman.',
 'Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101.',
 'Campbell, D. T., & Stanley, J. C. (1963). *Experimental and quasi-experimental designs for research*. Rand McNally.',
 'Cliff, N. (1993). Dominance statistics: Ordinal analyses to answer ordinal questions. *Psychological Bulletin, 114*(3), 494–509.',
 'Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2.ª ed.). Lawrence Erlbaum.',
 'Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika, 16*(3), 297–334.',
 'Dweck, C. S. (2006). *Mindset: The new psychology of success*. Random House.',
 'Granovetter, M. S. (1973). The strength of weak ties. *American Journal of Sociology, 78*(6), 1360–1380.',
 'Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.',
 'Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall.',
 'Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis. *Journal of the American Statistical Association, 47*(260), 583–621.',
 'Lent, R. W., Brown, S. D., & Hackett, G. (1994). Toward a unifying social cognitive theory of career and academic interest, choice, and performance. *Journal of Vocational Behavior, 45*(1), 79–122.',
 'Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics, 18*(1), 50–60.',
 'Norman, G. (2010). Likert scales, levels of measurement and the “laws” of statistics. *Advances in Health Sciences Education, 15*(5), 625–632.',
 'Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research. *Journal of Applied Psychology, 88*(5), 879–903.',
 'Sullivan, G. M., & Artino, A. R. (2013). Analyzing and interpreting data from Likert-type scales. *Journal of Graduate Medical Education, 5*(4), 541–542.',
 'Tomlinson, M. (2017). Forms of graduate capital and their relationship to graduate employability. *Education + Training, 59*(4), 338–352.',
 'Vargha, A., & Delaney, H. D. (2000). A critique and improvement of the CL common language effect size statistics of McGraw and Wong. *Journal of Educational and Behavioral Statistics, 25*(2), 101–132.',
 'Yorke, M. (2006). *Employability in higher education: What it is – what it is not*. Higher Education Academy.',
 'Duoc UC, Escuela de Administración y Negocios, Sede San Bernardo (2026). *Proyecto La Puerta: Informe metodológico y análisis prospectivo de brechas en habilidades blandas para la práctica profesional* [documento interno].',
 'Duoc UC (2026). *Proyecto La Puerta: Base de datos y matriz de análisis (20261009_1658)* [base de datos interna, no publicada].',
]
def bibliografia(doc, subset=None):
    doc.h1('Bibliografía y referencias')
    doc.p('Las fuentes se ordenan alfabéticamente (formato APA 7). Las dos últimas son documentos internos del proyecto. Las referencias académicas fueron seleccionadas por la herramienta de IA a partir de su conocimiento de la literatura y **no se verificaron en línea durante esta sesión**: conviene confirmar volumen, páginas y DOI antes de una publicación formal.', 9.5, GRAY)
    for b in (BIB if subset is None else [BIB[i] for i in subset]):
        p = doc.d.add_paragraph(); p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1); p.paragraph_format.space_after = Pt(4)
        # cursivas con *...*
        for part in re.split(r'(\*[^*]+\*)', b):
            if not part: continue
            it = part.startswith('*') and part.endswith('*'); r = p.add_run(part[1:-1] if it else part); r.italic = it; r.font.size = Pt(9.5); r.font.name = FONT

def declaracion_ia(doc, rol):
    doc.h2('Declaración sobre el uso de Inteligencia Artificial')
    doc.callout('Este informe se elaboró con apoyo de Inteligencia Artificial',
        [f'Se utilizó **Claude (Anthropic), modelo de IA generativa**, como herramienta de apoyo para: (1) limpiar y calcular los resultados de la base de datos con código reproducible; (2) {rol}; (3) redactar, organizar y diseñar los gráficos y diagramas; y (4) clasificar preliminarmente las respuestas abiertas por temas.',
         '**La IA no reemplaza el juicio experto.** La codificación temática automática es preliminar y debe ser validada por una persona (idealmente con doble codificación). Las interpretaciones, decisiones y recomendaciones deben ser revisadas y asumidas por el equipo responsable del Proyecto La Puerta antes de su difusión institucional.',
         'No se incluyeron nombres, correos ni códigos de estudiantes. Las citas textuales son anónimas.'], AMB, 'FFF7E0')

def aviso_datos(doc):
    c = R['campos_vacios']
    doc.callout('Una advertencia importante sobre los datos',
        [f"La base trae **{R['N']} respuestas de un solo momento**. Los campos que permitirían comparar «antes y después» o «grupo La Puerta vs. grupo de comparación» (código de estudiante, momento de medición y grupo de asignación) vienen **vacíos en las {c['ID02 código']} filas**, igual que la pregunta de valoración del programa (POST_EXP1).",
         'Por eso este análisis describe **cómo se perciben hoy los estudiantes** y contrasta hipótesis sobre **diferencias entre perfiles** (por ejemplo, con y sin práctica previa). **No puede afirmar que el programa La Puerta produzca cambios**: eso requiere medir a las mismas personas antes y después, con un grupo de comparación.'], CORAL, 'FDEEE9', '⚠')
