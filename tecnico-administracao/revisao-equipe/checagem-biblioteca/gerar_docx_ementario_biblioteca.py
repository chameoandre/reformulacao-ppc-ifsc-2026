#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Documento Word (.docx) Editável para a Biblioteca:
Ementário Completo das 45 Unidades Curriculares do PPC Técnico em Administração Integrado (IFSC Garopaba).

Inclui campos de anotações, conferência de exemplares físicos do Sophia e sugestão de harmonização.
"""

import os
import re
import pandas as pd
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/tecnico-administracao"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
MD_PATH = os.path.join(BASE_DIR, "todas_ementas_administracao.md")
EXCEL_PATH = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx")
DOCX_OUTPUT_PATH = os.path.join(CHECK_DIR, "Ementario_Completo_PPC_Tecnico_Administracao_Revisao_Biblioteca.docx")

# Colors
COLOR_IFSC_GREEN = RGBColor(16, 140, 80)      # #108C50
COLOR_DARK = RGBColor(15, 23, 42)             # #0F172A
COLOR_MUTED = RGBColor(100, 116, 139)         # #64748B
COLOR_RED = RGBColor(220, 38, 38)             # #DC2626
HEX_IFSC_GREEN = "108C50"
HEX_LIGHT_GREEN = "EBF8F0"
HEX_LIGHT_GRAY = "F8FAFC"
HEX_BORDER = "CBD5E1"
HEX_ROSE_BG = "FFF1F2"
HEX_AMBER_BG = "FFFBEB"

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def load_audit_data():
    if os.path.exists(EXCEL_PATH):
        df_all = pd.read_excel(EXCEL_PATH, sheet_name="Mapeamento_Completo_PPC")
        return df_all
    return None

def parse_markdown_ementas():
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    sections = content.split('# Unidade Curricular: ')
    ucs = []
    
    for idx, sec in enumerate(sections[1:], 1):
        lines = sec.strip().split('\n')
        title = lines[0].strip()
        
        sem = "Não especificado"
        bloco = "Formação Geral"
        ch = ""
        for l in lines:
            if l.startswith('**Ano/Semestre:**'):
                sem = l.replace('**Ano/Semestre:**', '').strip()
            elif l.startswith('**Bloco de Formação:**'):
                bloco = l.replace('**Bloco de Formação:**', '').strip()
            elif l.startswith('**Carga Horária Total:**'):
                ch = l.replace('**Carga Horária Total:**', '').strip()
                
        def get_section_text(sec_text, title_start, title_end=None):
            if title_start not in sec_text:
                return ""
            part = sec_text.split(title_start)[1]
            if title_end and title_end in part:
                part = part.split(title_end)[0]
            return part.strip()
            
        ementa_resumo = get_section_text(sec, '### 1. Ementa (Resumo do Componente)', '### 2.')
        objetivos = get_section_text(sec, '### 2. Objetivos de Aprendizagem & Competências', '### 3.')
        conteudos = get_section_text(sec, '### 3. Conteúdo Programático', '### 4.')
        metodologia = get_section_text(sec, '### 4. Metodologia de Ensino e Avaliação', '### 5.')
        
        bb_part = ''
        bc_part = ''
        if '**Básica:**' in sec:
            after_b = sec.split('**Básica:**')[1]
            if '**Complementar:**' in after_b:
                bb_part = after_b.split('**Complementar:**')[0].strip()
                bc_part = after_b.split('**Complementar:**')[1].split('---')[0].strip()
            else:
                bb_part = after_b.split('---')[0].strip()
                
        bb_items = [i.strip() for i in bb_part.split('\n') if i.strip() and not i.strip().startswith('---')]
        bc_items = [i.strip() for i in bc_part.split('\n') if i.strip() and not i.strip().startswith('---')]
        
        ucs.append({
            "id": idx,
            "uc_nome": title,
            "semestre": sem,
            "bloco": bloco,
            "ch": ch,
            "ementa_resumo": ementa_resumo,
            "objetivos": objetivos,
            "conteudos": conteudos,
            "metodologia": metodologia,
            "basica": bb_items,
            "complementar": bc_items
        })
    return ucs

def create_ementario_docx():
    print("Gerando Documento Word (.docx) Editável com todas as Ementas do PPC...")
    ucs = parse_markdown_ementas()
    df_audit = load_audit_data()
    
    doc = Document()
    
    # Page Setup (A4 Margins)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Styles
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Arial'
    style_normal.font.size = Pt(10)
    style_normal.font.color.rgb = COLOR_DARK
    
    # Header Institucional
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("INSTITUTO FEDERAL DE SANTA CATARINA — CÂMPUS GAROPABA\nDEPARTAMENTO DE ENSINO, PESQUISA E EXTENSÃO (DEPE)")
    r_inst.font.bold = True
    r_inst.font.size = Pt(11)
    r_inst.font.color.rgb = COLOR_IFSC_GREEN
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("PROJETO PEDAGÓGICO DE CURSO (PPC 2026)\nTÉCNICO INTEGRADO EM ADMINISTRAÇÃO\n")
    r_title.font.bold = True
    r_title.font.size = Pt(14)
    r_title.font.color.rgb = COLOR_DARK
    
    r_sub = p_title.add_run("Ementário Completo das 45 Unidades Curriculares\nDocumento de Trabalho & Revisão da Biblioteca (Sistema Sophia)")
    r_sub.font.bold = True
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = COLOR_MUTED
    
    # Box de Instruções para o David e Equipe da Biblioteca
    p_box = doc.add_paragraph()
    p_box.paragraph_format.space_before = Pt(10)
    p_box.paragraph_format.space_after = Pt(15)
    
    tbl_inst = doc.add_table(rows=1, cols=1)
    tbl_inst.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_inst = tbl_inst.cell(0, 0)
    cell_inst.width = Inches(6.8)
    set_cell_background(cell_inst, HEX_LIGHT_GREEN)
    set_cell_margins(cell_inst, top=140, bottom=140, left=180, right=180)
    set_table_borders(tbl_inst, color=HEX_IFSC_GREEN, sz="8")
    
    p_c_inst = cell_inst.paragraphs[0]
    r_ci_1 = p_c_inst.add_run("📋 ORIENTAÇÕES E PREMISSAS NORMATIVAS PARA A BIBLIOTECA (IFSC):\n")
    r_ci_1.font.bold = True
    r_ci_1.font.size = Pt(10.5)
    r_ci_1.font.color.rgb = COLOR_IFSC_GREEN
    
    r_ci_2 = p_c_inst.add_run(
        "1. Bibliografia Básica: Mínimo de 2 títulos de livros por UC. O acervo do câmpus deve dispor de ao menos 3 exemplares físicos de cada título (ou livro didático do PNLD/FNDE, computado como 1/aluno).\n"
        "2. Bibliografia Complementar: Mínimo de 3 títulos de livros por UC. O acervo do câmpus deve dispor de ao menos 1 exemplar físico de cada título.\n"
        "3. Como utilizar este arquivo: Este documento editável contém a estrutura curricular completa do curso com todas as 45 ementas. A equipe da biblioteca pode anotar na coluna 'Anotações da Biblioteca' o status real no Sophia, sugerir substituição de títulos sem exemplares ou harmonizar edições existentes."
    )
    r_ci_2.font.size = Pt(9.5)
    
    doc.add_page_break()
    
    # Render all 45 UCs
    for uc in ucs:
        uc_id = uc["id"]
        uc_nome = uc["uc_nome"]
        semestre = uc["semestre"]
        bloco = uc["bloco"]
        ch = uc["ch"]
        
        # Heading UC
        p_uc_h = doc.add_paragraph()
        p_uc_h.paragraph_format.space_before = Pt(14)
        p_uc_h.paragraph_format.space_after = Pt(4)
        r_uch = p_uc_h.add_run(f"UC {uc_id:02d} — {uc_nome}")
        r_uch.font.bold = True
        r_uch.font.size = Pt(12.5)
        r_uch.font.color.rgb = COLOR_IFSC_GREEN
        
        # Meta table
        tbl_meta = doc.add_table(rows=2, cols=3)
        tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl_meta, color=HEX_BORDER)
        
        headers = ["Bloco de Formação", "Ano / Semestre", "Carga Horária Total"]
        vals = [bloco, semestre, ch or "40 horas"]
        
        for c_idx in range(3):
            c_head = tbl_meta.cell(0, c_idx)
            set_cell_background(c_head, HEX_LIGHT_GRAY)
            set_cell_margins(c_head, top=60, bottom=60, left=100, right=100)
            p_h = c_head.paragraphs[0]
            p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_h = p_h.add_run(headers[c_idx])
            r_h.font.bold = True
            r_h.font.size = Pt(8.5)
            r_h.font.color.rgb = COLOR_MUTED
            
            c_val = tbl_meta.cell(1, c_idx)
            set_cell_margins(c_val, top=60, bottom=60, left=100, right=100)
            p_v = c_val.paragraphs[0]
            p_v.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_v = p_v.add_run(vals[c_idx])
            r_v.font.bold = True
            r_v.font.size = Pt(9.5)
            
        # 1. Ementa Resumo
        if uc["ementa_resumo"]:
            p_e_title = doc.add_paragraph()
            p_e_title.paragraph_format.space_before = Pt(8)
            p_e_title.paragraph_format.space_after = Pt(2)
            r_et = p_e_title.add_run("1. Ementa (Resumo do Componente):")
            r_et.font.bold = True
            r_et.font.size = Pt(9.5)
            r_et.font.color.rgb = COLOR_DARK
            
            p_e_body = doc.add_paragraph(uc["ementa_resumo"])
            p_e_body.paragraph_format.space_after = Pt(6)
            p_e_body.runs[0].font.size = Pt(9.5)
            
        # 2. Objetivos
        if uc["objetivos"]:
            p_o_title = doc.add_paragraph()
            p_o_title.paragraph_format.space_before = Pt(4)
            p_o_title.paragraph_format.space_after = Pt(2)
            r_ot = p_o_title.add_run("2. Objetivos de Aprendizagem & Competências:")
            r_ot.font.bold = True
            r_ot.font.size = Pt(9.5)
            
            p_o_body = doc.add_paragraph(uc["objetivos"])
            p_o_body.paragraph_format.space_after = Pt(6)
            p_o_body.runs[0].font.size = Pt(9)
            
        # 3. Conteúdo Programático
        if uc["conteudos"]:
            p_c_title = doc.add_paragraph()
            p_c_title.paragraph_format.space_before = Pt(4)
            p_c_title.paragraph_format.space_after = Pt(2)
            r_ct = p_c_title.add_run("3. Conteúdo Programático:")
            r_ct.font.bold = True
            r_ct.font.size = Pt(9.5)
            
            p_c_body = doc.add_paragraph(uc["conteudos"])
            p_c_body.paragraph_format.space_after = Pt(6)
            p_c_body.runs[0].font.size = Pt(9)

        # 4. Bibliografia Básica (Tabela com campo para Biblioteca)
        p_bb_title = doc.add_paragraph()
        p_bb_title.paragraph_format.space_before = Pt(8)
        p_bb_title.paragraph_format.space_after = Pt(3)
        r_bbt = p_bb_title.add_run("4. Bibliografia BÁSICA (Norma: Mínimo 2 títulos — Meta: ≥ 3 exemplares no Câmpus):")
        r_bbt.font.bold = True
        r_bbt.font.size = Pt(9.5)
        r_bbt.font.color.rgb = COLOR_IFSC_GREEN
        
        tbl_bb = doc.add_table(rows=1 + max(1, len(uc["basica"])), cols=3)
        tbl_bb.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl_bb, color=HEX_BORDER)
        
        tbl_bb.cell(0, 0).width = Inches(3.8)
        tbl_bb.cell(0, 1).width = Inches(1.3)
        tbl_bb.cell(0, 2).width = Inches(1.7)
        
        bb_headers = ["Obra Adotada no PPC (ABNT NBR 6023)", "Situação Sophia", "Anotações da Biblioteca"]
        for c_idx in range(3):
            c_h = tbl_bb.cell(0, c_idx)
            set_cell_background(c_h, HEX_LIGHT_GREEN)
            set_cell_margins(c_h, top=60, bottom=60, left=80, right=80)
            p = c_h.paragraphs[0]
            r = p.add_run(bb_headers[c_idx])
            r.font.bold = True
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_IFSC_GREEN
            
        for r_idx, b_ref in enumerate(uc["basica"], 1):
            row_cell_ref = tbl_bb.cell(r_idx, 0)
            row_cell_status = tbl_bb.cell(r_idx, 1)
            row_cell_notes = tbl_bb.cell(r_idx, 2)
            
            set_cell_margins(row_cell_ref, top=50, bottom=50, left=80, right=80)
            set_cell_margins(row_cell_status, top=50, bottom=50, left=80, right=80)
            set_cell_margins(row_cell_notes, top=50, bottom=50, left=80, right=80)
            
            p_ref = row_cell_ref.paragraphs[0]
            r_ref = p_ref.add_run(b_ref.replace("**", ""))
            r_ref.font.size = Pt(8.5)
            
            # Match status from audit dataframe if present
            status_text = "Conferir Sophia"
            status_bg = HEX_LIGHT_GRAY
            if df_audit is not None:
                match_df = df_audit[(df_audit["UC_ID"] == uc_id) & (df_audit["Tipo_Bibliografia"] == "Básica") & (df_audit["Ordem_UC"] == r_idx)]
                if not match_df.empty:
                    m_row = match_df.iloc[0]
                    ex_d = m_row["Exemplares_Disponiveis"]
                    def_c = m_row["Deficit_Exemplares_Compra"]
                    if m_row["Status"] == "MATERIAL_FNDE":
                        status_text = "PNLD (1/Aluno)"
                        status_bg = HEX_LIGHT_GREEN
                    elif m_row["Existe_Biblioteca"] == "SIM":
                        if def_c == 0:
                            status_text = f"Disponível ({ex_d} ex.)"
                            status_bg = HEX_LIGHT_GREEN
                        else:
                            status_text = f"Possui {ex_d} ex. (Faltam +{def_c})"
                            status_bg = HEX_AMBER_BG
                    else:
                        status_text = "Ausente (+3 ex.)"
                        status_bg = HEX_ROSE_BG
                        
            set_cell_background(row_cell_status, status_bg)
            p_stat = row_cell_status.paragraphs[0]
            r_stat = p_stat.add_run(status_text)
            r_stat.font.bold = True
            r_stat.font.size = Pt(8)
            
            p_note = row_cell_notes.paragraphs[0]
            p_note.add_run("[ ] OK  [ ] Substituir  [ ] Comprar")
            p_note.runs[0].font.size = Pt(7.5)
            p_note.runs[0].font.color.rgb = COLOR_MUTED

        # 5. Bibliografia Complementar (Tabela com campo para Biblioteca)
        p_bc_title = doc.add_paragraph()
        p_bc_title.paragraph_format.space_before = Pt(8)
        p_bc_title.paragraph_format.space_after = Pt(3)
        r_bct = p_bc_title.add_run("5. Bibliografia COMPLEMENTAR (Norma: Mínimo 3 títulos — Meta: ≥ 1 exemplar no Câmpus):")
        r_bct.font.bold = True
        r_bct.font.size = Pt(9.5)
        r_bct.font.color.rgb = COLOR_DARK
        
        tbl_bc = doc.add_table(rows=1 + max(1, len(uc["complementar"])), cols=3)
        tbl_bc.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl_bc, color=HEX_BORDER)
        
        tbl_bc.cell(0, 0).width = Inches(3.8)
        tbl_bc.cell(0, 1).width = Inches(1.3)
        tbl_bc.cell(0, 2).width = Inches(1.7)
        
        bc_headers = ["Obra Adotada no PPC (ABNT NBR 6023)", "Situação Sophia", "Anotações da Biblioteca"]
        for c_idx in range(3):
            c_h = tbl_bc.cell(0, c_idx)
            set_cell_background(c_h, HEX_LIGHT_GRAY)
            set_cell_margins(c_h, top=60, bottom=60, left=80, right=80)
            p = c_h.paragraphs[0]
            r = p.add_run(bc_headers[c_idx])
            r.font.bold = True
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            
        for r_idx, c_ref in enumerate(uc["complementar"], 1):
            row_cell_ref = tbl_bc.cell(r_idx, 0)
            row_cell_status = tbl_bc.cell(r_idx, 1)
            row_cell_notes = tbl_bc.cell(r_idx, 2)
            
            set_cell_margins(row_cell_ref, top=50, bottom=50, left=80, right=80)
            set_cell_margins(row_cell_status, top=50, bottom=50, left=80, right=80)
            set_cell_margins(row_cell_notes, top=50, bottom=50, left=80, right=80)
            
            p_ref = row_cell_ref.paragraphs[0]
            r_ref = p_ref.add_run(c_ref.replace("**", ""))
            r_ref.font.size = Pt(8.5)
            
            status_text = "Conferir Sophia"
            status_bg = HEX_LIGHT_GRAY
            if df_audit is not None:
                match_df = df_audit[(df_audit["UC_ID"] == uc_id) & (df_audit["Tipo_Bibliografia"] == "Complementar") & (df_audit["Ordem_UC"] == r_idx)]
                if not match_df.empty:
                    m_row = match_df.iloc[0]
                    ex_d = m_row["Exemplares_Disponiveis"]
                    if m_row["Existe_Biblioteca"] == "SIM":
                        status_text = f"Disponível ({ex_d} ex.)"
                        status_bg = HEX_LIGHT_GREEN
                    else:
                        status_text = "Ausente (+1 ex.)"
                        status_bg = HEX_AMBER_BG
                        
            set_cell_background(row_cell_status, status_bg)
            p_stat = row_cell_status.paragraphs[0]
            r_stat = p_stat.add_run(status_text)
            r_stat.font.bold = True
            r_stat.font.size = Pt(8)
            
            p_note = row_cell_notes.paragraphs[0]
            p_note.add_run("[ ] OK  [ ] Sugerir Edição")
            p_note.runs[0].font.size = Pt(7.5)
            p_note.runs[0].font.color.rgb = COLOR_MUTED
            
        doc.add_page_break()
        
    doc.save(DOCX_OUTPUT_PATH)
    print(f"Documento Word (.docx) editável gerado com sucesso em:\n{DOCX_OUTPUT_PATH}")

if __name__ == "__main__":
    create_ementario_docx()
