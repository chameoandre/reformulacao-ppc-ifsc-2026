#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador do Dashboard Interativo, Relatórios em PDF (LaTeX), Planilhas e Sumários Executivos:
Auditoria Normativa de Bibliografia & Quantitativos de Acervo
PPC CST em Gestão Ambiental (IFSC Garopaba) vs. Catálogo Sophia.
"""

import os
import re
import json
import subprocess
import pandas as pd

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/superior-gestao-ambiental"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
EXCEL_PATH = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia_GA.xlsx")
TXT_PATH = os.path.join(CHECK_DIR, "Unidades Curriculares Gestão Ambiental.txt")
DOCX_PATH = os.path.join(CHECK_DIR, "Ementario_Completo_PPC_Gestao_Ambiental_Revisao_Biblioteca.docx")
HTML_OUTPUT_PATH = os.path.join(CHECK_DIR, "dashboard_biblioteca_ga.html")
INDEX_OUTPUT_PATH = os.path.join(CHECK_DIR, "index.html")
TEX_OUTPUT_PATH = os.path.join(CHECK_DIR, "relatorio_auditoria_biblioteca_ga.tex")
PDF_OUTPUT_PATH = os.path.join(CHECK_DIR, "relatorio_auditoria_biblioteca_ga.pdf")
MD_SUMARIO_PATH = os.path.join(CHECK_DIR, "sumario_executivo_david_biblioteca_ga.md")
MD_RELATORIO_PATH = os.path.join(CHECK_DIR, "relatorio_auditoria_biblioteca_ppc_ga.md")

def load_data():
    df_all = pd.read_excel(EXCEL_PATH, sheet_name='Diagnóstico Consolidado')
    df_sophia = pd.read_excel(EXCEL_PATH, sheet_name='Catálogo Sophia Garopaba')
    
    # Import ucs_info directly from analise_acervo_biblioteca_ga for 100% accurate UC names and metadata
    from analise_acervo_biblioteca_ga import parse_txt_ementas
    ucs_info, _ = parse_txt_ementas()
    
    return df_all, df_sophia, ucs_info

def escape_html(text):
    if not isinstance(text, str):
        text = str(text) if text is not None and not pd.isna(text) else ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

def escape_tex(text):
    if not isinstance(text, str):
        text = str(text) if text is not None and not pd.isna(text) else ""
    text = text.replace('–', '--').replace('—', '---')
    text = re.sub(r'_{2,}', '---', text)
    text = text.replace('\\', '')
    rep = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in rep.items():
        text = text.replace(k, v)
    return text

def build_dashboard_html(df_all, df_sophia, ucs_meta):
    total_refs = len(df_all)
    total_sim = len(df_all[df_all['Existe_Biblioteca'] == 'SIM'])
    total_nao = len(df_all[df_all['Existe_Biblioteca'] == 'NÃO'])
    total_var = len(df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE'])
    
    total_deficit_basica = int(df_all[df_all['Tipo'] == 'BÁSICA']['Deficit_Exemplares'].sum())
    total_deficit_comp = int(df_all[df_all['Tipo'] == 'COMPLEMENTAR']['Deficit_Exemplares'].sum())
    total_deficit_geral = total_deficit_basica + total_deficit_comp

    total_exemplares_lib = int(df_sophia['Exemplares'].sum())

    # Agrupar por UC
    uc_groups = []
    for u in ucs_meta:
        uc_name = u['uc_nome']
        sub = df_all[df_all['UC'] == uc_name]
        
        b_sub = sub[sub['Tipo'] == 'BÁSICA']
        c_sub = sub[sub['Tipo'] == 'COMPLEMENTAR']
        
        b_tot = len(b_sub)
        b_sim = len(b_sub[b_sub['Existe_Biblioteca'] == 'SIM'])
        b_nao = len(b_sub[b_sub['Existe_Biblioteca'] == 'NÃO'])
        b_def = int(b_sub['Deficit_Exemplares'].sum())
        
        c_tot = len(c_sub)
        c_sim = len(c_sub[c_sub['Existe_Biblioteca'] == 'SIM'])
        c_nao = len(c_sub[c_sub['Existe_Biblioteca'] == 'NÃO'])
        c_def = int(c_sub['Deficit_Exemplares'].sum())
        
        has_var = len(sub[sub['Status'] == 'EXISTE_EDICAO_DIFERENTE']) > 0
        
        # Status da UC
        if b_def > 0:
            status_code = "CRITICA_BASICA"
            status_label = f"🔴 Crítica: Déficit de {b_def} ex. na Básica"
            badge_class = "badge-nao"
        elif c_def > 0:
            status_code = "ATENCAO_COMPLEMENTAR"
            status_label = f"🟡 Atenção: Falta {c_def} ex. na Complementar"
            badge_class = "badge-var"
        elif has_var:
            status_code = "ATENCAO_EDICAO"
            status_label = "🔵 Atenção: Variação de Edição / Ano"
            badge_class = "badge-var"
        else:
            status_code = "CONFORME_100"
            status_label = "🟢 100% Conforme Normativo"
            badge_class = "badge-sim"
            
        uc_groups.append({
            'meta': u,
            'status_code': status_code,
            'status_label': status_label,
            'badge_class': badge_class,
            'b_tot': b_tot, 'b_sim': b_sim, 'b_nao': b_nao, 'b_def': b_def,
            'c_tot': c_tot, 'c_sim': c_sim, 'c_nao': c_nao, 'c_def': c_def,
            'tot_def': b_def + c_def,
            'items': sub.to_dict('records')
        })

    count_conformes = sum(1 for g in uc_groups if g['status_code'] == 'CONFORME_100')
    count_criticas = sum(1 for g in uc_groups if g['status_code'] == 'CRITICA_BASICA')
    count_atencao_comp = sum(1 for g in uc_groups if g['status_code'] == 'ATENCAO_COMPLEMENTAR')
    count_atencao_var = sum(1 for g in uc_groups if g['status_code'] == 'ATENCAO_EDICAO')
    count_com_problema = len(uc_groups) - count_conformes

    # HTML Generator
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auditoria Normativa de Acervo & Exemplares — CST em Gestão Ambiental | IFSC Garopaba</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <style>
    :root {{
      /* TEMA CLARO (PADRÃO INSTITUCIONAL) */
      --bg-main: #F8FAFC;
      --bg-card: #FFFFFF;
      --bg-hover: #F1F5F9;
      --bg-card-subtle: #F8FAFC;
      --bg-accent: #EBF8F0;
      --border-color: #E2E8F0;
      --border-light: #F1F5F9;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --text-heading: #0F172A;
      --accent-emerald: #059669;
      --accent-emerald-dark: #047857;
      --accent-rose: #E11D48;
      --accent-amber: #D97706;
      --accent-blue: #0284C7;
      --accent-purple: #7C3AED;
      --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
      --card-shadow-hover: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --header-bg: rgba(255, 255, 255, 0.94);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }}

    [data-theme="dark"] {{
      --bg-main: #0B1120;
      --bg-card: #0F172A;
      --bg-hover: #1E293B;
      --bg-card-subtle: rgba(15, 23, 42, 0.8);
      --bg-accent: rgba(16, 185, 129, 0.08);
      --border-color: #334155;
      --border-light: rgba(255, 255, 255, 0.08);
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-heading: #FFFFFF;
      --accent-emerald: #10B981;
      --accent-emerald-dark: #059669;
      --accent-rose: #F43F5E;
      --accent-amber: #F59E0B;
      --accent-blue: #0284C7;
      --accent-purple: #8B5CF6;
      --card-shadow: none;
      --card-shadow-hover: 0 8px 24px rgba(0, 0, 0, 0.3);
      --header-bg: rgba(15, 23, 42, 0.85);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    /* HEADER */
    .app-header {{
      background: var(--header-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.85rem 2rem;
      transition: background 0.2s ease, border-color 0.2s ease;
    }}
    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }}
    .brand-area {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .brand-logo-bg {{
      background: white;
      padding: 4px 8px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      border: 1px solid #E2E8F0;
    }}
    .brand-logo-bg img {{ height: 32px; }}
    .brand-titles h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-heading);
      letter-spacing: -0.01em;
    }}
    .brand-titles p {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-wrap: wrap;
    }}
    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.45rem 0.9rem;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }}
    .btn-emerald {{
      background: linear-gradient(135deg, var(--accent-emerald) 0%, var(--accent-emerald-dark) 100%);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(5, 150, 105, 0.25);
    }}
    .btn-emerald:hover {{
      box-shadow: 0 4px 14px rgba(5, 150, 105, 0.4);
      transform: translateY(-1px);
    }}
    .btn-blue {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.3);
    }}
    .btn-blue:hover {{
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.45);
      transform: translateY(-1px);
    }}
    .btn-outline {{
      background: var(--bg-card);
      border-color: var(--border-color);
      color: var(--text-main);
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }}
    .btn-outline:hover {{
      background: var(--bg-hover);
      border-color: var(--text-muted);
    }}

    /* MAIN CONTENT */
    .main-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 1.5rem 2rem;
      width: 100%;
      flex: 1;
    }}

    /* BANNER NORMATIVO */
    .normative-banner {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-left: 5px solid var(--accent-emerald);
      border-radius: var(--radius-md);
      padding: 1.1rem 1.4rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      box-shadow: var(--card-shadow);
    }}
    .normative-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #FFF1F2;
      border: 1px solid #FECDD3;
      color: var(--accent-rose);
      padding: 0.4rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      transition: all 0.2s ease;
    }}
    .normative-badge:hover {{
      background: #FFE4E6;
      transform: scale(1.02);
    }}

    /* KPI CARDS */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      margin-bottom: 1.8rem;
    }}
    .kpi-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.4rem;
      transition: all 0.2s ease;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      box-shadow: var(--card-shadow);
    }}
    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--card-shadow-hover);
      border-color: #CBD5E1;
    }}
    .kpi-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.4rem;
    }}
    .kpi-title {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }}
    .kpi-icon {{
      font-size: 1.25rem;
    }}
    .kpi-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.9rem;
      font-weight: 800;
      line-height: 1.2;
    }}
    .kpi-desc {{
      font-size: 0.76rem;
      color: var(--text-muted);
      margin-top: 0.35rem;
    }}
    .kpi-rose .kpi-value {{ color: var(--accent-rose); }}
    .kpi-rose .kpi-icon {{ color: var(--accent-rose); }}
    .kpi-amber .kpi-value {{ color: var(--accent-amber); }}
    .kpi-amber .kpi-icon {{ color: var(--accent-amber); }}
    .kpi-emerald .kpi-value {{ color: var(--accent-emerald); }}
    .kpi-emerald .kpi-icon {{ color: var(--accent-emerald); }}
    .kpi-blue .kpi-value {{ color: var(--accent-blue); }}
    .kpi-blue .kpi-icon {{ color: var(--accent-blue); }}
    .kpi-purple .kpi-value {{ color: var(--accent-purple); }}
    .kpi-purple .kpi-icon {{ color: var(--accent-purple); }}

    /* TABS */
    .dashboard-tabs {{
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 1.5rem;
      overflow-x: auto;
      padding-bottom: 2px;
    }}
    .tab-btn {{
      padding: 0.65rem 1.1rem;
      font-size: 0.86rem;
      font-weight: 600;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }}
    .tab-btn:hover {{
      color: var(--text-main);
      background: var(--bg-hover);
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    }}
    .tab-btn.active {{
      color: var(--accent-emerald);
      border-bottom-color: var(--accent-emerald);
      background: var(--bg-accent);
    }}

    /* FILTER BAR */
    .filter-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 0.9rem 1.2rem;
      margin-bottom: 1.5rem;
      display: flex;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      box-shadow: var(--card-shadow);
    }}
    .search-input-wrapper {{
      position: relative;
      flex: 1;
      min-width: 260px;
    }}
    .search-input-wrapper i {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}
    .search-input {{
      width: 100%;
      background: var(--bg-hover);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 0.5rem 1rem 0.5rem 2.3rem;
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
      transition: border-color 0.15s ease;
    }}
    .search-input:focus {{
      border-color: var(--accent-emerald);
      background: var(--bg-card);
    }}
    .select-filter {{
      background: var(--bg-hover);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 0.5rem 0.9rem;
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }}

    /* BADGES */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.22rem 0.6rem;
      font-size: 0.72rem;
      font-weight: 700;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }}
    .badge-sim {{
      background: #ECFDF5;
      color: #047857;
      border: 1px solid #A7F3D0;
    }}
    .badge-nao {{
      background: #FFF1F2;
      color: #BE123C;
      border: 1px solid #FECDD3;
    }}
    .badge-var {{
      background: #FFFBEB;
      color: #B45309;
      border: 1px solid #FDE68A;
    }}
    .badge-basica {{
      background: #F0F9FF;
      color: #0369A1;
      border: 1px solid #BAE6FD;
    }}
    .badge-comp {{
      background: #F8FAFC;
      color: #475569;
      border: 1px solid #E2E8F0;
    }}

    /* TABLES */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow-x: auto;
      margin-bottom: 1.5rem;
      box-shadow: var(--card-shadow);
    }}
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      text-align: left;
    }}
    table.data-table th {{
      background: #F8FAFC;
      color: #475569;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
      text-transform: uppercase;
      font-size: 0.72rem;
      letter-spacing: 0.05em;
    }}
    [data-theme="dark"] table.data-table th {{
      background: var(--bg-hover);
      color: var(--text-muted);
    }}
    table.data-table td {{
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
      color: var(--text-main);
    }}
    table.data-table tr:hover td {{
      background: var(--bg-hover);
    }}

    /* ACCORDION */
    .uc-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 0.9rem;
      overflow: hidden;
      box-shadow: var(--card-shadow);
      transition: all 0.15s ease;
    }}
    .uc-card:hover {{
      border-color: #CBD5E1;
      box-shadow: var(--card-shadow-hover);
    }}
    .uc-header {{
      padding: 0.95rem 1.3rem;
      background: var(--bg-card);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      user-select: none;
    }}
    .uc-header:hover {{
      background: var(--bg-hover);
    }}
    .uc-title-area {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}
    .uc-body {{
      display: none;
      padding: 1.2rem 1.4rem;
      border-top: 1px solid var(--border-color);
      background: var(--bg-main);
    }}
    .uc-card.open .uc-body {{
      display: block;
    }}
    .uc-card.open .uc-chevron {{
      transform: rotate(180deg);
    }}

    /* FOOTER */
    .app-footer {{
      background: var(--bg-card);
      border-top: 1px solid var(--border-color);
      padding: 1.5rem 2rem;
      text-align: center;
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: auto;
    }}
  </style>
</head>

<body>

  <!-- HEADER -->
  <header class="app-header">
    <div class="header-container">
      <div class="brand-area">
        <div class="brand-logo-bg">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Instituto_Federal_de_Santa_Catarina_-_Marca_2015.svg/1200px-Instituto_Federal_de_Santa_Catarina_-_Marca_2015.svg.png" alt="IFSC Logo">
        </div>
        <div class="brand-titles">
          <h1>Auditoria Normativa de Acervo & Exemplares — CST em Gestão Ambiental</h1>
          <p>Aplicação da Regra Institucional: Mínimo de 3 Exs. na Básica e 1 Ex. na Complementar • IFSC Garopaba</p>
        </div>
      </div>

      <div class="header-actions">
        <button class="btn-action btn-outline" id="themeToggleBtn" onclick="toggleTheme()" title="Alternar entre tema Claro e Escuro">
          <i class="bi bi-moon-stars-fill" id="themeIcon"></i> <span id="themeText">Tema Escuro</span>
        </button>
        <button class="btn-action btn-emerald" onclick="switchTab('tab-sumario')">
          <i class="bi bi-envelope-paper-fill"></i> Sumário Executivo (David)
        </button>
        <a href="Ementario_Completo_PPC_Gestao_Ambiental_Revisao_Biblioteca.docx" download class="btn-action btn-blue">
          <i class="bi bi-file-earmark-word-fill"></i> Baixar Ementário (.docx)
        </a>
        <a href="relatorio_auditoria_biblioteca_ga.pdf" target="_blank" class="btn-action btn-outline">
          <i class="bi bi-file-earmark-pdf-fill" style="color:#fb7185;"></i> Relatório PDF
        </a>
        <a href="Analise_Bibliografica_PPC_vs_Acervo_Sophia_GA.xlsx" download class="btn-action btn-outline">
          <i class="bi bi-file-earmark-excel-fill" style="color:#34d399;"></i> Planilha (.xlsx)
        </a>
        <a href="../../../index.html" class="btn-action btn-outline">
          <i class="bi bi-arrow-left"></i> Painel Geral do PPC
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN -->
  <main class="main-container">

    <!-- NORMATIVE BANNER -->
    <div class="normative-banner">
      <div style="display:flex; align-items:center; gap:0.9rem;">
        <i class="bi bi-shield-check text-emerald" style="font-size:1.8rem;"></i>
        <div>
          <strong style="color:#ffffff; font-size:0.95rem; font-family:'Outfit', sans-serif;">Critérios Oficiais de Quantitativos Mínimos da Biblioteca (IFSC):</strong>
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px; line-height:1.7;">
            • <a href="#secao-compras-basica" onclick="scrollToSection('secao-compras-basica'); return false;" style="color:#34d399; font-weight:700; text-decoration:underline; cursor:pointer;">Bibliografia Básica: Mínimo 2 títulos &rarr; ao menos 3 exemplares físicos no acervo (Clique para ver as +{total_deficit_basica} cópias a comprar)</a>.<br>
            • <a href="#secao-compras-comp" onclick="scrollToSection('secao-compras-comp'); return false;" style="color:#fbbf24; font-weight:700; text-decoration:underline; cursor:pointer;">Bibliografia Complementar: Mínimo 3 títulos &rarr; ao menos 1 exemplar físico no acervo (Clique para ver as +{total_deficit_comp} cópias a comprar)</a>.
          </p>
        </div>
      </div>
      <div style="text-align:right;">
        <a href="#secao-compras-basica" onclick="scrollToSection('secao-compras-basica'); return false;" style="text-decoration:none;">
          <span class="normative-badge" style="cursor:pointer;" title="Clique para ver o relatório completo de compras">
            <i class="bi bi-cart-check-fill"></i> Demanda Total de Compras: <strong>+{total_deficit_geral} exemplares</strong> <i class="bi bi-arrow-right-circle-fill ms-1"></i>
          </span>
        </a>
      </div>
    </div>

    <!-- KPI CARDS -->
    <div class="kpi-grid">
      <div class="kpi-card kpi-rose" onclick="scrollToSection('secao-compras-basica')" title="Clique para ver a lista de compras da Básica">
        <div class="kpi-header">
          <span class="kpi-title">Compras Básica (&lt; 3 Exs.)</span>
          <i class="bi bi-cart-plus-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">+{total_deficit_basica} Exs.</div>
        <div class="kpi-desc">Exemplares a adquirir para suprir 3 cópias por título básico (Clique para ver)</div>
      </div>

      <div class="kpi-card kpi-amber" onclick="scrollToSection('secao-compras-comp')" title="Clique para ver a lista de compras da Complementar">
        <div class="kpi-header">
          <span class="kpi-title">Compras Complementar (&lt; 1 Ex.)</span>
          <i class="bi bi-journal-plus kpi-icon"></i>
        </div>
        <div class="kpi-value">+{total_deficit_comp} Exs.</div>
        <div class="kpi-desc">Exemplares a adquirir para suprir 1 cópia dos títulos ausentes (Clique para ver)</div>
      </div>

      <div class="kpi-card kpi-blue" onclick="scrollToSection('secao-variacoes-edicao')" title="Clique para ver as variações de edição">
        <div class="kpi-header">
          <span class="kpi-title">Variação de Edição / Ano</span>
          <i class="bi bi-arrow-repeat kpi-icon"></i>
        </div>
        <div class="kpi-value">{count_atencao_var} Obras</div>
        <div class="kpi-desc">Obras existem no acervo; requer atualização do texto do PPC (Clique para ver)</div>
      </div>

      <div class="kpi-card kpi-emerald" onclick="filterDiagBy('CONFORME_100')">
        <div class="kpi-header">
          <span class="kpi-title">100% Conformes no Acervo</span>
          <i class="bi bi-check-circle-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">{count_conformes} UCs</div>
        <div class="kpi-desc">Ementas com acervo físico plenamente regularizado</div>
      </div>

      <div class="kpi-card kpi-purple" onclick="switchTab('tab-catalogo')">
        <div class="kpi-header">
          <span class="kpi-title">Exemplares no Câmpus</span>
          <i class="bi bi-stack kpi-icon"></i>
        </div>
        <div class="kpi-value">{total_exemplares_lib} Exs.</div>
        <div class="kpi-desc">Total de cópias físicas em 3.003 títulos no Sophia Garopaba</div>
      </div>
    </div>

    <!-- TABS -->
    <div class="dashboard-tabs">
      <button class="tab-btn" onclick="switchTab('tab-sumario')">
        <i class="bi bi-envelope-paper-fill"></i> 📑 Sumário Executivo (David)
      </button>
      <button class="tab-btn active" onclick="switchTab('tab-diagnostico')">
        <i class="bi bi-kanban-fill"></i> Diagnóstico das 33 Ementas <span class="badge badge-nao" style="margin-left:4px;">{count_com_problema} com Pendência</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-ausentes')">
        <i class="bi bi-cart-dash-fill"></i> Títulos Ausentes para Aquisição <span id="count-ausentes" class="badge badge-nao" style="margin-left:4px;">{total_nao}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-variacoes')">
        <i class="bi bi-arrow-left-right"></i> Variações de Edição / Ano <span id="count-variacoes" class="badge badge-var" style="margin-left:4px;">{total_var}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-existentes')">
        <i class="bi bi-check-circle-fill"></i> Acervo Confirmado (Sophia) <span id="count-existentes" class="badge badge-sim" style="margin-left:4px;">{total_sim}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-ucs')">
        <i class="bi bi-folder2-open"></i> Auditoria por UC (Accordion)
      </button>
      <button class="tab-btn" onclick="switchTab('tab-todas')">
        <i class="bi bi-list-columns-reverse"></i> Mapeamento Geral ({total_refs} Obras)
      </button>
      <button class="tab-btn" onclick="switchTab('tab-catalogo')">
        <i class="bi bi-bookshelf"></i> Catálogo Sophia (3.003 Obras & Exemplares)
      </button>
    </div>

    <!-- FILTER BAR -->
    <div class="filter-bar">
      <div class="search-input-wrapper">
        <i class="bi bi-search"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Pesquisar por unidade curricular, livro, autor, ISBN ou palavra-chave..." oninput="applyFilters()">
      </div>

      <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
        <select id="filterStatusEmenta" class="select-filter" onchange="applyFilters()">
          <option value="ALL">Status da Ementa: Todas as 33 UCs</option>
          <option value="COM_PROBLEMA">🚨 Todas as Ementas com Alguma Pendência ({count_com_problema} UCs)</option>
          <option value="CRITICA_BASICA">🔴 Críticas: Déficit na Básica ({count_criticas} UCs)</option>
          <option value="ATENCAO_COMPLEMENTAR">🟡 Atenção: Falta na Complementar ({count_atencao_comp} UCs)</option>
          <option value="ATENCAO_EDICAO">🔵 Atenção: Variação de Edição ({count_atencao_var} UCs)</option>
          <option value="CONFORME_100">🟢 100% Conformes Normativos ({count_conformes} UCs)</option>
        </select>

        <button class="btn-action btn-outline" onclick="resetFilters()">
          <i class="bi bi-arrow-counterclockwise"></i> Limpar Filtros
        </button>
      </div>
    </div>

    <!-- TAB: SUMÁRIO EXECUTIVO DAVID -->
    <div id="tab-sumario" class="tab-pane">
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:2rem; margin-bottom:1.5rem;">
        <div style="border-bottom:2px solid var(--border-color); padding-bottom:1.5rem; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
          <div>
            <span class="badge badge-sim" style="font-size:0.8rem; margin-bottom:0.5rem;"><i class="bi bi-file-earmark-text-fill"></i> Memorando Técnico Oficial</span>
            <h2 style="font-family:'Outfit', sans-serif; font-size:1.45rem; color:var(--text-heading); margin-top:0.3rem;">Sumário Executivo: Auditoria Normativa de Acervo & Quantitativos de Exemplares</h2>
            <div style="margin-top:0.8rem; font-size:0.88rem; color:var(--text-muted); line-height:1.7;">
              <strong>Para:</strong> David (Bibliotecário-Documentalista — IFSC Câmpus Garopaba)<br>
              <strong>De:</strong> Comissão de Reformulação do PPC CST em Gestão Ambiental<br>
              <strong>Data:</strong> 28 de Agosto de 2026<br>
              <strong>Assunto:</strong> Diagnóstico de Cobertura do Catálogo Sophia e Demanda de Aquisição de Exemplares Físicos
            </div>
          </div>
          <div style="display:flex; gap:0.6rem; flex-wrap:wrap;">
            <a href="Ementario_Completo_PPC_Gestao_Ambiental_Revisao_Biblioteca.docx" download class="btn-action btn-blue">
              <i class="bi bi-file-earmark-word-fill"></i> Baixar Ementário (.docx)
            </a>
            <button class="btn-action btn-outline" onclick="window.print()">
              <i class="bi bi-printer-fill"></i> Imprimir / PDF
            </button>
            <a href="relatorio_auditoria_biblioteca_ga.pdf" target="_blank" class="btn-action btn-outline">
              <i class="bi bi-file-earmark-pdf-fill" style="color:#fb7185;"></i> Relatório LaTeX (.pdf)
            </a>
          </div>
        </div>

        <div style="font-size:0.92rem; line-height:1.8; color:var(--text-main);">
          <p style="margin-bottom:1rem;">
            Prezado David,
          </p>
          <p style="margin-bottom:1rem;">
            Apresentamos o relatório consolidado da <strong>auditoria bibliográfica automatizada</strong> realizada entre as <strong>189 referências bibliográficas</strong> das <strong>33 Unidades Curriculares</strong> do novo PPC do <strong>Curso Superior de Tecnologia em Gestão Ambiental</strong> e o acervo físico registrado no Sistema Sophia da Biblioteca do Câmpus Garopaba (3.003 títulos e 4.962 exemplares).
          </p>
          <p style="margin-bottom:1rem;">
            Para fins de planejamento de compras institucionais e conformidade regulatória, aplicamos a <strong>Regra Normativa do IFSC</strong>:
          </p>
          <ul style="margin-left:1.5rem; margin-bottom:1.5rem; color:var(--text-main);">
            <li><strong>Bibliografia Básica (mín. 2 títulos):</strong> Disponibilização de ao menos <strong>3 exemplares físicos</strong> de cada título no acervo do câmpus.</li>
            <li><strong>Bibliografia Complementar (mín. 3 títulos):</strong> Disponibilização de ao menos <strong>1 exemplar físico</strong> de cada título no acervo do câmpus.</li>
          </ul>

          <h3 style="color:var(--text-heading); font-family:'Outfit', sans-serif; font-size:1.15rem; margin:1.5rem 0 0.8rem 0; border-bottom:1px solid var(--border-color); padding-bottom:0.4rem;">
            1. Síntese do Diagnóstico e Demanda de Compras
          </h3>
          
          <table class="data-table" style="margin-bottom:1.5rem;">
            <thead>
              <tr>
                <th>Indicador Normativo</th>
                <th>Quantitativo</th>
                <th>Meta Institucional / Observação</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Unidades Curriculares Analisadas</strong></td>
                <td>33 UCs</td>
                <td>100% da matriz curricular do CST Gestão Ambiental</td>
              </tr>
              <tr>
                <td><strong>Total de Obras Mapeadas</strong></td>
                <td>{total_refs} títulos</td>
                <td>Obras auditadas na matriz do PPC</td>
              </tr>
              <tr>
                <td><strong>Títulos com Acervo Físico Confirmado</strong></td>
                <td><span class="badge badge-sim">{total_sim} títulos ({total_sim/total_refs*100:.1f}%)</span></td>
                <td>Obras localizadas no Sophia Garopaba</td>
              </tr>
              <tr>
                <td><strong>Títulos Ausentes no Acervo</strong></td>
                <td><span class="badge badge-nao">{total_nao} títulos ({total_nao/total_refs*100:.1f}%)</span></td>
                <td>Demanda direta para processo de aquisição</td>
              </tr>
              <tr>
                <td><strong>Obras com Variação de Edição / Ano</strong></td>
                <td><span class="badge badge-var">{total_var} títulos</span></td>
                <td>Acervo possui edição anterior/posterior à citada no PPC</td>
              </tr>
              <tr style="background:rgba(244,63,94,0.06);">
                <td><strong><a href="#secao-compras-basica" onclick="scrollToSection('secao-compras-basica'); return false;" style="color:#e11d48; text-decoration:underline; font-weight:700;">DEMANDA DE COMPRAS: Bibliografia BÁSICA</a></strong></td>
                <td><strong style="color:#e11d48; font-size:1.1rem;">+{total_deficit_basica} exemplares físicos</strong></td>
                <td>Meta: &ge; 3 exemplares por título básico (Clique para ver listagem)</td>
              </tr>
              <tr style="background:rgba(245,158,11,0.06);">
                <td><strong><a href="#secao-compras-comp" onclick="scrollToSection('secao-compras-comp'); return false;" style="color:#d97706; text-decoration:underline; font-weight:700;">DEMANDA DE COMPRAS: Bibliografia COMPLEMENTAR</a></strong></td>
                <td><strong style="color:#d97706; font-size:1.1rem;">+{total_deficit_comp} exemplares físicos</strong></td>
                <td>Meta: &ge; 1 exemplar por título complementar (Clique para ver listagem)</td>
              </tr>
              <tr style="background:rgba(5,150,105,0.08);">
                <td><strong>DEMANDA TOTAL CONSOLIDADA DE AQUISIÇÃO</strong></td>
                <td><strong style="color:#059669; font-size:1.2rem;">+{total_deficit_geral} EXEMPLARES</strong></td>
                <td>Total de cópias físicas para regularização normativa 100%</td>
              </tr>
            </tbody>
          </table>

          <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:2rem;">
            <a href="Ementario_Completo_PPC_Gestao_Ambiental_Revisao_Biblioteca.docx" download class="btn-action btn-blue">
              <i class="bi bi-file-earmark-word-fill"></i> Baixar Ementário (.docx)
            </a>
            <a href="Analise_Bibliografica_PPC_vs_Acervo_Sophia_GA.xlsx" download class="btn-action btn-emerald">
              <i class="bi bi-file-earmark-excel-fill"></i> Baixar Planilha Consolidada (.xlsx)
            </a>
            <a href="relatorio_auditoria_biblioteca_ga.pdf" target="_blank" class="btn-action btn-outline">
              <i class="bi bi-file-earmark-pdf-fill" style="color:#fb7185;"></i> Baixar Relatório em PDF
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB: DIAGNÓSTICO DAS 33 EMENTAS -->
    <div id="tab-diagnostico" class="tab-pane active">
      <div class="table-container">
        <table class="data-table" id="table-diag">
          <thead>
            <tr>
              <th>Sem.</th>
              <th>Unidade Curricular</th>
              <th>CH Total</th>
              <th>Status do Acervo</th>
              <th>Básica (Disp / Deficit)</th>
              <th>Complementar (Disp / Deficit)</th>
              <th>Compras</th>
              <th>Ação</th>
            </tr>
          </thead>
          <tbody>
"""

    for g in uc_groups:
        m = g['meta']
        html_content += f"""            <tr class="diag-row" data-status="{g['status_code']}" data-sem="{m['semestre']}">
              <td style="font-weight:700; color:var(--text-muted);">{m['semestre']}º</td>
              <td><strong style="color:var(--text-heading);">{escape_html(m['uc_nome'])}</strong></td>
              <td>{escape_html(m['ch_total'])}</td>
              <td><span class="badge {g['badge_class']}">{g['status_label']}</span></td>
              <td>{g['b_sim']}/{g['b_tot']} obras {f"<strong style='color:#e11d48;'>(+{g['b_def']} ex.)</strong>" if g['b_def'] > 0 else "<span style='color:#059669; font-weight:700;'>OK</span>"}</td>
              <td>{g['c_sim']}/{g['c_tot']} obras {f"<strong style='color:#d97706;'>(+{g['c_def']} ex.)</strong>" if g['c_def'] > 0 else "<span style='color:#059669; font-weight:700;'>OK</span>"}</td>
              <td>{f"<span class='badge badge-nao'>+{g['tot_def']} ex.</span>" if g['tot_def'] > 0 else "<span class='badge badge-sim'>0 ex.</span>"}</td>
              <td><button class="btn-action btn-outline" style="padding:2px 8px; font-size:0.75rem;" onclick="openUcAccordion({m['id']})"><i class="bi bi-eye"></i> Detalhes</button></td>
            </tr>
"""

    html_content += f"""          </tbody>
        </table>
      </div>

      <!-- SEÇÃO COMPRAS BÁSICA -->
      <div id="secao-compras-basica" style="margin-top:2.5rem; margin-bottom:2rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; border-bottom:2px solid var(--accent-rose); padding-bottom:0.6rem;">
          <h2 style="font-family:'Outfit', sans-serif; font-size:1.3rem; color:var(--text-heading);">
            <i class="bi bi-cart-plus-fill" style="color:var(--accent-rose);"></i> Lista Prioritária de Compras: Bibliografia BÁSICA (+{total_deficit_basica} Exemplares)
          </h2>
          <span class="badge badge-nao" style="font-size:0.85rem;">Meta: &ge; 3 exemplares físicos por título</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Sem.</th>
                <th>Unidade Curricular</th>
                <th>Título Referenciado no PPC</th>
                <th>Autor</th>
                <th>Acervo Garopaba</th>
                <th>Demanda de Compra</th>
              </tr>
            </thead>
            <tbody>
"""

    df_b_def = df_all[(df_all['Tipo'] == 'BÁSICA') & (df_all['Deficit_Exemplares'] > 0)]
    for _, r in df_b_def.iterrows():
        html_content += f"""              <tr>
                <td>{r['Semestre']}º</td>
                <td><strong style="color:var(--text-heading);">{escape_html(r['UC'])}</strong></td>
                <td>{escape_html(r['Titulo_PPC'])}</td>
                <td>{escape_html(r['Autor_PPC'])}</td>
                <td>{r['Exemplares_Acervo']} ex. ({escape_html(r['Status_Legivel'])})</td>
                <td><span class="badge badge-nao" style="font-size:0.85rem;">+{r['Deficit_Exemplares']} exemplares</span></td>
              </tr>
"""

    html_content += f"""            </tbody>
          </table>
        </div>
      </div>

      <!-- SEÇÃO COMPRAS COMPLEMENTAR -->
      <div id="secao-compras-comp" style="margin-top:2.5rem; margin-bottom:2rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; border-bottom:2px solid var(--accent-amber); padding-bottom:0.6rem;">
          <h2 style="font-family:'Outfit', sans-serif; font-size:1.3rem; color:var(--text-heading);">
            <i class="bi bi-journal-plus" style="color:var(--accent-amber);"></i> Lista de Compras: Bibliografia COMPLEMENTAR (+{total_deficit_comp} Exemplares)
          </h2>
          <span class="badge badge-var" style="font-size:0.85rem;">Meta: &ge; 1 exemplar físico por título</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Sem.</th>
                <th>Unidade Curricular</th>
                <th>Título Referenciado no PPC</th>
                <th>Autor</th>
                <th>Acervo Garopaba</th>
                <th>Demanda de Compra</th>
              </tr>
            </thead>
            <tbody>
"""

    df_c_def = df_all[(df_all['Tipo'] == 'COMPLEMENTAR') & (df_all['Deficit_Exemplares'] > 0)]
    for _, r in df_c_def.iterrows():
        html_content += f"""              <tr>
                <td>{r['Semestre']}º</td>
                <td><strong style="color:var(--text-heading);">{escape_html(r['UC'])}</strong></td>
                <td>{escape_html(r['Titulo_PPC'])}</td>
                <td>{escape_html(r['Autor_PPC'])}</td>
                <td>{r['Exemplares_Acervo']} ex. ({escape_html(r['Status_Legivel'])})</td>
                <td><span class="badge badge-var" style="font-size:0.85rem;">+{r['Deficit_Exemplares']} exemplar</span></td>
              </tr>
"""

    html_content += f"""            </tbody>
          </table>
        </div>
      </div>

      <!-- SEÇÃO VARIAÇÕES DE EDIÇÃO -->
      <div id="secao-variacoes-edicao" style="margin-top:2.5rem; margin-bottom:2rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; border-bottom:2px solid var(--accent-blue); padding-bottom:0.6rem;">
          <h2 style="font-family:'Outfit', sans-serif; font-size:1.3rem; color:var(--text-heading);">
            <i class="bi bi-arrow-repeat" style="color:var(--accent-blue);"></i> Obras com Variação de Edição / Ano no Acervo ({total_var} Obras)
          </h2>
          <span class="badge badge-sim" style="font-size:0.85rem;">Disponíveis no Sophia &rarr; Atualizar texto do PPC</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Sem.</th>
                <th>Unidade Curricular</th>
                <th>Tipo</th>
                <th>Referência no PPC</th>
                <th>Edição / Ano no Sophia</th>
                <th>Exemplares</th>
              </tr>
            </thead>
            <tbody>
"""

    df_var_items = df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE']
    for _, r in df_var_items.iterrows():
        html_content += f"""              <tr>
                <td>{r['Semestre']}º</td>
                <td><strong style="color:var(--text-heading);">{escape_html(r['UC'])}</strong></td>
                <td><span class="badge {'badge-basica' if r['Tipo'] == 'BÁSICA' else 'badge-comp'}">{r['Tipo']}</span></td>
                <td>{escape_html(r['Referencia_PPC'])}</td>
                <td><span style="color:var(--accent-blue); font-weight:600;">{escape_html(r['Status_Legivel'])}</span></td>
                <td><span class="badge badge-sim">{r['Exemplares_Acervo']} ex.</span></td>
              </tr>
"""

    html_content += f"""            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB: AUSENTES -->
    <div id="tab-ausentes" class="tab-pane">
      <div class="table-container">
        <table class="data-table" id="table-ausentes">
          <thead>
            <tr>
              <th>Sem.</th>
              <th>Unidade Curricular</th>
              <th>Tipo</th>
              <th>Título Referenciado no PPC</th>
              <th>Autor</th>
              <th>ISBN</th>
              <th>Demanda Compra</th>
            </tr>
          </thead>
          <tbody>
"""

    for _, r in df_all[df_all['Existe_Biblioteca'] == 'NÃO'].iterrows():
        html_content += f"""            <tr>
              <td>{r['Semestre']}º</td>
              <td><strong style="color:var(--text-heading);">{escape_html(r['UC'])}</strong></td>
              <td><span class="badge {'badge-basica' if r['Tipo'] == 'BÁSICA' else 'badge-comp'}">{r['Tipo']}</span></td>
              <td>{escape_html(r['Titulo_PPC'])}</td>
              <td>{escape_html(r['Autor_PPC'])}</td>
              <td><code>{escape_html(r['ISBN_PPC']) or '—'}</code></td>
              <td><span class="badge badge-nao">+{r['Deficit_Exemplares']} ex.</span></td>
            </tr>
"""

    html_content += f"""          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB: VARIAÇÕES -->
    <div id="tab-variacoes" class="tab-pane">
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sem.</th>
              <th>Unidade Curricular</th>
              <th>Tipo</th>
              <th>Referência no PPC</th>
              <th>Diagnóstico Sophia</th>
              <th>Exemplares</th>
            </tr>
          </thead>
          <tbody>
"""

    for _, r in df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE'].iterrows():
        html_content += f"""            <tr>
              <td>{r['Semestre']}º</td>
              <td><strong>{escape_html(r['UC'])}</strong></td>
              <td><span class="badge {'badge-basica' if r['Tipo'] == 'BÁSICA' else 'badge-comp'}">{r['Tipo']}</span></td>
              <td>{escape_html(r['Referencia_PPC'])}</td>
              <td><span style="color:#38bdf8;">{escape_html(r['Status_Legivel'])}</span></td>
              <td><span class="badge badge-sim">{r['Exemplares_Acervo']} ex.</span></td>
            </tr>
"""

    html_content += f"""          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB: EXISTENTES -->
    <div id="tab-existentes" class="tab-pane">
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sem.</th>
              <th>Unidade Curricular</th>
              <th>Tipo</th>
              <th>Título no PPC</th>
              <th>Título no Acervo Sophia</th>
              <th>Exemplares Físicos</th>
            </tr>
          </thead>
          <tbody>
"""

    for _, r in df_all[df_all['Existe_Biblioteca'] == 'SIM'].iterrows():
        html_content += f"""            <tr>
              <td>{r['Semestre']}º</td>
              <td><strong>{escape_html(r['UC'])}</strong></td>
              <td><span class="badge {'badge-basica' if r['Tipo'] == 'BÁSICA' else 'badge-comp'}">{r['Tipo']}</span></td>
              <td>{escape_html(r['Titulo_PPC'])}</td>
              <td><strong style="color:#34d399;">{escape_html(r['Titulo_Acervo'])}</strong> ({escape_html(r['Autor_Acervo'])})</td>
              <td><span class="badge badge-sim">{r['Exemplares_Acervo']} ex.</span></td>
            </tr>
"""

    html_content += f"""          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB: ACCORDION UCS -->
    <div id="tab-ucs" class="tab-pane">
"""

    for g in uc_groups:
        m = g['meta']
        html_content += f"""      <div class="uc-card" id="uc-card-{m['id']}">
        <div class="uc-header" onclick="toggleAccordion({m['id']})">
          <div class="uc-title-area">
            <span class="badge badge-comp">Semestre {m['semestre']}º</span>
            <strong style="color:var(--text-heading); font-size:1.02rem;">{escape_html(m['uc_nome'])}</strong>
            <span style="font-size:0.8rem; color:var(--text-muted);">({escape_html(m['ch_total'])})</span>
            <span class="badge {g['badge_class']}">{g['status_label']}</span>
          </div>
          <div style="display:flex; align-items:center; gap:0.75rem;">
            <span class="badge {'badge-nao' if g['tot_def'] > 0 else 'badge-sim'}">Déficit: +{g['tot_def']} ex.</span>
            <i class="bi bi-chevron-down uc-chevron" style="transition:transform 0.2s ease;"></i>
          </div>
        </div>
        <div class="uc-body">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1rem;">
            <div>
              <h4 style="color:var(--accent-blue); font-size:0.9rem; margin-bottom:0.6rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:700;">
                <i class="bi bi-book-half"></i> Bibliografia Básica ({g['b_sim']}/{g['b_tot']} no acervo)
              </h4>
              <ul style="list-style:none; display:flex; flex-direction:column; gap:0.6rem;">
"""
        for item in g['items']:
            if item['Tipo'] == 'BÁSICA':
                html_content += f"""                <li style="background:var(--bg-hover); border:1px solid var(--border-color); border-radius:6px; padding:0.6rem 0.8rem;">
                  <div style="font-size:0.82rem; margin-bottom:0.3rem; color:var(--text-main);">{escape_html(item['Referencia_PPC'])}</div>
                  <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem;">
                    <span class="badge {'badge-sim' if item['Existe_Biblioteca'] == 'SIM' else 'badge-nao'}">{item['Status_Legivel']}</span>
                    {f"<strong style='color:#e11d48;'>+ {item['Deficit_Exemplares']} ex. a comprar</strong>" if item['Deficit_Exemplares'] > 0 else "<span style='color:#059669; font-weight:700;'>Meta atendida</span>"}
                  </div>
                </li>
"""

        html_content += f"""              </ul>
            </div>
            <div>
              <h4 style="color:var(--text-muted); font-size:0.9rem; margin-bottom:0.6rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:700;">
                <i class="bi bi-journal-text"></i> Bibliografia Complementar ({g['c_sim']}/{g['c_tot']} no acervo)
              </h4>
              <ul style="list-style:none; display:flex; flex-direction:column; gap:0.6rem;">
"""
        for item in g['items']:
            if item['Tipo'] == 'COMPLEMENTAR':
                html_content += f"""                <li style="background:var(--bg-hover); border:1px solid var(--border-color); border-radius:6px; padding:0.6rem 0.8rem;">
                  <div style="font-size:0.82rem; margin-bottom:0.3rem; color:var(--text-main);">{escape_html(item['Referencia_PPC'])}</div>
                  <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem;">
                    <span class="badge {'badge-sim' if item['Existe_Biblioteca'] == 'SIM' else 'badge-nao'}">{item['Status_Legivel']}</span>
                    {f"<strong style='color:#d97706;'>+ {item['Deficit_Exemplares']} ex. a comprar</strong>" if item['Deficit_Exemplares'] > 0 else "<span style='color:#059669; font-weight:700;'>Meta atendida</span>"}
                  </div>
                </li>
"""

        html_content += f"""              </ul>
            </div>
          </div>
        </div>
      </div>
"""

    html_content += f"""    </div>

    <!-- TAB: TODAS AS OBRAS -->
    <div id="tab-todas" class="tab-pane">
      <div class="table-container">
        <table class="data-table" id="table-todas">
          <thead>
            <tr>
              <th>Sem.</th>
              <th>UC</th>
              <th>Tipo</th>
              <th>Referência no PPC</th>
              <th>Status Acervo</th>
              <th>Exemplares</th>
              <th>Déficit Compra</th>
            </tr>
          </thead>
          <tbody>
"""

    for _, r in df_all.iterrows():
        html_content += f"""            <tr>
              <td>{r['Semestre']}º</td>
              <td><strong style="color:var(--text-heading);">{escape_html(r['UC'])}</strong></td>
              <td><span class="badge {'badge-basica' if r['Tipo'] == 'BÁSICA' else 'badge-comp'}">{r['Tipo']}</span></td>
              <td>{escape_html(r['Referencia_PPC'])}</td>
              <td><span class="badge {'badge-sim' if r['Existe_Biblioteca'] == 'SIM' else 'badge-nao'}">{escape_html(r['Status_Legivel'])}</span></td>
              <td>{r['Exemplares_Acervo']} ex.</td>
              <td>{f"<span class='badge badge-nao'>+{r['Deficit_Exemplares']} ex.</span>" if r['Deficit_Exemplares'] > 0 else "<span class='badge badge-sim'>OK</span>"}</td>
            </tr>
"""

    html_content += f"""          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB: CATÁLOGO SOPHIA -->
    <div id="tab-catalogo" class="tab-pane">
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.5rem; margin-bottom:1.5rem;">
        <h3 style="color:var(--text-heading); font-family:'Outfit', sans-serif; font-size:1.2rem; margin-bottom:0.5rem;">
          <i class="bi bi-bookshelf"></i> Inventário Geral do Sistema Sophia (IFSC Câmpus Garopaba)
        </h3>
        <p style="color:var(--text-muted); font-size:0.88rem; margin-bottom:1rem;">
          Total de <strong>3.003 títulos</strong> e <strong>4.962 exemplares físicos</strong> catalogados no acervo local.
        </p>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Título da Obra</th>
                <th>Autor Principal</th>
                <th>Ano</th>
                <th>Edição</th>
                <th>Exemplares no Câmpus</th>
              </tr>
            </thead>
            <tbody>
"""

    for _, r in df_sophia.head(100).iterrows():
        html_content += f"""              <tr>
                <td><strong>{escape_html(r.get('Titulo', ''))}</strong></td>
                <td>{escape_html(r.get('Autor', ''))}</td>
                <td>{escape_html(r.get('Ano', ''))}</td>
                <td>{escape_html(r.get('Edicao', ''))}</td>
                <td><span class="badge badge-sim">{r.get('Exemplares', 1)} ex.</span></td>
              </tr>
"""

    html_content += f"""            </tbody>
          </table>
        </div>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="app-footer">
    <p>Auditoria Normativa Bibliográfica & Quantitativa • PPC CST em Gestão Ambiental • IFSC Câmpus Garopaba</p>
    <p style="margin-top:4px; opacity:0.7;">Relatório gerado em 28/08/2026 • Sistema Integrado de Reformulação Curricular</p>
  </footer>

  <!-- SCRIPT -->
  <script>
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      
      const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (btn) btn.classList.add('active');
      
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function scrollToSection(sectionId) {{
      switchTab('tab-diagnostico');
      setTimeout(() => {{
        const el = document.getElementById(sectionId);
        if (el) {{
          el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}
      }}, 100);
    }}

    function toggleAccordion(id) {{
      const card = document.getElementById('uc-card-' + id);
      if (card) card.classList.toggle('open');
    }}

    function openUcAccordion(id) {{
      switchTab('tab-ucs');
      setTimeout(() => {{
        const card = document.getElementById('uc-card-' + id);
        if (card) {{
          card.classList.add('open');
          card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}
      }}, 100);
    }}

    function filterDiagBy(status) {{
      switchTab('tab-diagnostico');
      document.getElementById('filterStatusEmenta').value = status;
      applyFilters();
    }}

    function applyFilters() {{
      const search = document.getElementById('searchInput').value.toLowerCase();
      const status = document.getElementById('filterStatusEmenta').value;

      document.querySelectorAll('.diag-row').forEach(row => {{
        const text = row.innerText.toLowerCase();
        const rowStatus = row.getAttribute('data-status');
        
        let matchSearch = !search || text.includes(search);
        let matchStatus = (status === 'ALL') ||
                          (status === 'COM_PROBLEMA' && rowStatus !== 'CONFORME_100') ||
                          (rowStatus === status);
                          
        row.style.display = (matchSearch && matchStatus) ? '' : 'none';
      }});
    }}

    function toggleTheme() {{
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('dashboard_theme', newTheme);
      updateThemeButton(newTheme);
    }}

    function updateThemeButton(theme) {{
      const icon = document.getElementById('themeIcon');
      const text = document.getElementById('themeText');
      if (theme === 'dark') {{
        if (icon) icon.className = 'bi bi-sun-fill';
        if (text) text.innerText = 'Tema Claro';
      }} else {{
        if (icon) icon.className = 'bi bi-moon-stars-fill';
        if (text) text.innerText = 'Tema Escuro';
      }}
    }}

    // Initialize Theme from localStorage or default to light
    (function() {{
      const saved = localStorage.getItem('dashboard_theme') || 'light';
      document.documentElement.setAttribute('data-theme', saved);
      updateThemeButton(saved);
    }})();
  </script>
</body>
</html>
"""
    return html_content

def build_latex_report(df_all, df_sophia, ucs_meta):
    total_refs = len(df_all)
    total_sim = len(df_all[df_all['Existe_Biblioteca'] == 'SIM'])
    total_nao = len(df_all[df_all['Existe_Biblioteca'] == 'NÃO'])
    total_var = len(df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE'])
    
    total_deficit_basica = int(df_all[df_all['Tipo'] == 'BÁSICA']['Deficit_Exemplares'].sum())
    total_deficit_comp = int(df_all[df_all['Tipo'] == 'COMPLEMENTAR']['Deficit_Exemplares'].sum())
    total_deficit_geral = total_deficit_basica + total_deficit_comp

    tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{geometry}
\geometry{top=2cm,bottom=2cm,left=2cm,right=2cm}
\usepackage{xcolor}
\definecolor{ifscgreen}{RGB}{16,140,80}
\definecolor{ifscdark}{RGB}{15,23,42}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=ifscgreen,urlcolor=ifscgreen}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{\textcolor{ifscgreen}{\textbf{IFSC Câmpus Garopaba}} -- Auditoria Normativa de Acervo (CST Gestão Ambiental)}
\rfoot{\thepage}

\begin{document}

\begin{center}
    {\large \textbf{INSTITUTO FEDERAL DE SANTA CATARINA}}\\[2pt]
    {\normalsize \textbf{CÂMPUS GAROPABA -- CST EM GESTÃO AMBIENTAL}}\\[6pt]
    {\LARGE \textbf{\textcolor{ifscgreen}{RELATÓRIO OFICIAL DE AUDITORIA BIBLIOGRÁFICA}}}\\[4pt]
    {\large \textbf{Adequação Normativa de Acervo \& Demanda de Compras de Exemplares Físicos}}\\[8pt]
    \rule{\linewidth}{1.5pt}
\end{center}

\vspace{0.3cm}
\noindent \textbf{Para:} David (Bibliotecário-Documentalista)\\
\textbf{De:} Comissão de Reformulação do PPC CST em Gestão Ambiental\\
\textbf{Data:} 28 de Agosto de 2026\\
\textbf{Assunto:} Diagnóstico de Cobertura do Catálogo Sophia \& Quantitativos de Exemplares Físicos

\vspace{0.4cm}
\section*{1. Critérios Normativos Institucionais}
A auditoria aplicou rigorosamente os parâmetros oficiais do IFSC:
\begin{itemize}
    \item \textbf{Bibliografia Básica:} Mínimo de 2 títulos por UC; cada título deve contar com ao menos \textbf{3 exemplares físicos} no acervo local do câmpus.
    \item \textbf{Bibliografia Complementar:} Mínimo de 3 títulos por UC; cada título deve contar com ao menos \textbf{1 exemplar físico} no acervo local do câmpus.
\end{itemize}

\section*{2. Síntese Executiva dos Indicadores}

\begin{table}[h!]
\centering
\begin{tabularx}{\linewidth}{|X|c|X|}
\hline
\textbf{Indicador Normativo} & \textbf{Total} & \textbf{Observação / Diagnóstico} \\ \hline
Unidades Curriculares Auditadas & 33 UCs & 100\% da matriz curricular do CST Gestão Ambiental \\ \hline
Total de Referências Bibliográficas & """ + str(total_refs) + r""" & 85 Básicas e 128 Complementares \\ \hline
Títulos Disponíveis no Acervo Sophia & """ + f"{total_sim} ({total_sim/total_refs*100:.1f}\%)" + r""" & Obras com presença física confirmada no câmpus \\ \hline
Títulos Ausentes no Acervo Sophia & """ + f"{total_nao} ({total_nao/total_refs*100:.1f}\%)" + r""" & Demanda prioritária para aquisição \\ \hline
Variações de Edição / Ano & """ + str(total_var) + r""" & Obras presentes com edição divergente da citada \\ \hline
\textbf{DEMANDA DE COMPRAS: Básica ($<$ 3 ex.)} & \textbf{+""" + str(total_deficit_basica) + r""" ex.} & \textbf{Exemplares para meta de 3 cópias na básica} \\ \hline
\textbf{DEMANDA DE COMPRAS: Complementar ($<$ 1 ex.)} & \textbf{+""" + str(total_deficit_comp) + r""" ex.} & \textbf{Exemplares para meta de 1 cópia na complementar} \\ \hline
\textbf{DEMANDA TOTAL DE COMPRAS} & \textbf{\textcolor{ifscgreen}{+""" + str(total_deficit_geral) + r""" EX.}} & \textbf{Total consolidado para conformidade 100\%} \\ \hline
\end{tabularx}
\end{table}

\newpage
\section*{3. Lista Prioritária de Aquisições: Bibliografia BÁSICA (+""" + str(total_deficit_basica) + r""" exemplares)}

\begin{longtable}{|p{1.2cm}|p{3.5cm}|p{6cm}|p{3.5cm}|c|}
\hline
\textbf{Sem.} & \textbf{Unidade Curricular} & \textbf{Título Referenciado no PPC} & \textbf{Autor} & \textbf{Déficit} \\ \hline
\endfirsthead
\hline
\textbf{Sem.} & \textbf{Unidade Curricular} & \textbf{Título Referenciado no PPC} & \textbf{Autor} & \textbf{Déficit} \\ \hline
\endhead
"""

    df_b_def = df_all[(df_all['Tipo'] == 'BÁSICA') & (df_all['Deficit_Exemplares'] > 0)]
    for _, r in df_b_def.iterrows():
        tex += f"{r['Semestre']}º & {escape_tex(r['UC'])} & {escape_tex(r['Titulo_PPC'])} & {escape_tex(r['Autor_PPC'])} & \\textbf{{+{r['Deficit_Exemplares']} ex.}} \\\\ \\hline\n"

    tex += r"""\end{longtable}

\newpage
\section*{4. Lista de Aquisições: Bibliografia COMPLEMENTAR (+""" + str(total_deficit_comp) + r""" exemplares)}

\begin{longtable}{|p{1.2cm}|p{3.5cm}|p{6cm}|p{3.5cm}|c|}
\hline
\textbf{Sem.} & \textbf{Unidade Curricular} & \textbf{Título Referenciado no PPC} & \textbf{Autor} & \textbf{Déficit} \\ \hline
\endfirsthead
\hline
\textbf{Sem.} & \textbf{Unidade Curricular} & \textbf{Título Referenciado no PPC} & \textbf{Autor} & \textbf{Déficit} \\ \hline
\endhead
"""

    df_c_def = df_all[(df_all['Tipo'] == 'COMPLEMENTAR') & (df_all['Deficit_Exemplares'] > 0)]
    for _, r in df_c_def.iterrows():
        tex += f"{r['Semestre']}º & {escape_tex(r['UC'])} & {escape_tex(r['Titulo_PPC'])} & {escape_tex(r['Autor_PPC'])} & +{r['Deficit_Exemplares']} ex. \\\\ \\hline\n"

    tex += r"""\end{longtable}

\end{document}
"""
    return tex

def build_markdown_summary(df_all, ucs_meta):
    total_refs = len(df_all)
    total_sim = len(df_all[df_all['Existe_Biblioteca'] == 'SIM'])
    total_nao = len(df_all[df_all['Existe_Biblioteca'] == 'NÃO'])
    total_var = len(df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE'])
    
    total_deficit_basica = int(df_all[df_all['Tipo'] == 'BÁSICA']['Deficit_Exemplares'].sum())
    total_deficit_comp = int(df_all[df_all['Tipo'] == 'COMPLEMENTAR']['Deficit_Exemplares'].sum())
    total_deficit_geral = total_deficit_basica + total_deficit_comp

    md = f"""# Sumário Executivo: Auditoria Normativa de Acervo & Quantitativos de Exemplares
**Curso:** Curso Superior de Tecnologia em Gestão Ambiental (CST GA) — PPC 2026  
**Câmpus:** IFSC Câmpus Garopaba  
**Destinatário:** David (Bibliotecário-Documentalista)  
**Data:** 28 de Agosto de 2026  

---

### 1. Critérios Normativos Oficiais do IFSC
* **Bibliografia Básica (mín. 2 títulos):** Mínimo de **3 exemplares físicos** de cada título no acervo local do câmpus.
* **Bibliografia Complementar (mín. 3 títulos):** Mínimo de **1 exemplar físico** de cada título no acervo local do câmpus.

---

### 2. Quadro Resumo de Auditoria

| Indicador Normativo | Quantitativo | Diagnóstico / Observação |
| :--- | :---: | :--- |
| **Unidades Curriculares Auditadas** | **33 UCs** | 100% da matriz curricular do CST Gestão Ambiental |
| **Total de Obras Referenciadas** | **{total_refs} títulos** | 85 na Básica e 128 na Complementar |
| **Títulos com Acervo Confirmado (Sophia)** | **{total_sim} ({total_sim/total_refs*100:.1f}%)** | Obras localizadas no inventário físico de Garopaba |
| **Títulos Ausentes no Acervo** | **{total_nao} ({total_nao/total_refs*100:.1f}%)** | Demanda direta para processo de aquisição |
| **Variações de Edição / Ano** | **{total_var} títulos** | Obra disponível; recomenda-se atualizar citação no PPC |
| **DEMANDA DE COMPRAS: Bibliografia BÁSICA** | **+{total_deficit_basica} exemplares** | Meta: $\ge$ 3 exemplares por título básico |
| **DEMANDA DE COMPRAS: Bibliografia COMPLEMENTAR** | **+{total_deficit_comp} exemplares** | Meta: $\ge$ 1 exemplar por título complementar |
| **DEMANDA TOTAL CONSOLIDADA DE AQUISIÇÃO** | **+{total_deficit_geral} EXEMPLARES** | Total físico para atingir 100% de conformidade normativa |

---

### 3. Artefatos Oficiais Gerados:
1. **Painel Interativo:** `dashboard_biblioteca_ga.html`
2. **Relatório em PDF:** `relatorio_auditoria_biblioteca_ga.pdf`
3. **Planilha Consolidada:** `Analise_Bibliografica_PPC_vs_Acervo_Sophia_GA.xlsx`
4. **Ementário Word Completo:** `Ementario_Completo_PPC_Gestao_Ambiental_Revisao_Biblioteca.docx`
"""
    return md

def main():
    print("Iniciando geração completa do Dashboard e Relatórios de Gestão Ambiental...")
    df_all, df_sophia, ucs_meta = load_data()

    # 1. HTML Dashboard
    html_code = build_dashboard_html(df_all, df_sophia, ucs_meta)
    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_code)
    with open(INDEX_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"Dashboard HTML gerado em:\n{HTML_OUTPUT_PATH}")

    # 2. LaTeX Report
    tex_code = build_latex_report(df_all, df_sophia, ucs_meta)
    with open(TEX_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Código LaTeX gerado em:\n{TEX_OUTPUT_PATH}")

    # Compile PDF via Tectonic
    try:
        subprocess.run(["tectonic", TEX_OUTPUT_PATH], check=True)
        print(f"PDF compilado com sucesso via Tectonic: {PDF_OUTPUT_PATH}")
    except Exception as e:
        print(f"Aviso na compilação do LaTeX via Tectonic: {e}")

    # 3. Markdown Summaries
    md_summary = build_markdown_summary(df_all, ucs_meta)
    with open(MD_SUMARIO_PATH, "w", encoding="utf-8") as f:
        f.write(md_summary)
    with open(MD_RELATORIO_PATH, "w", encoding="utf-8") as f:
        f.write(md_summary)
    print(f"Sumários Markdown salvos com sucesso.")

    print("\n✅ Todas as tarefas de Gestão Ambiental concluídas com sucesso!")

if __name__ == "__main__":
    main()
