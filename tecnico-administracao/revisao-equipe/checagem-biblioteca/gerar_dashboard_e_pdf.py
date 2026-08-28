#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador da Página Web Interativa (Dashboard) e do Documento PDF Estilizado em LaTeX
para a Auditoria do Acervo Bibliográfico do PPC Técnico em Administração (IFSC Garopaba).
"""

import os
import re
import json
import subprocess
import pandas as pd

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/tecnico-administracao"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
EXCEL_PATH = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx")
ROOT_INDEX_PATH = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/index.html"

def clean_val(val):
    if pd.isna(val) or val is None or str(val).strip() == "" or str(val).strip().lower() == "nan":
        return ""
    s = str(val).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return s

def load_data():
    df_all = pd.read_excel(EXCEL_PATH, sheet_name='Mapeamento_Completo_PPC')
    df_resumo = pd.read_excel(EXCEL_PATH, sheet_name='Resumo_Geral')
    df_uc = pd.read_excel(EXCEL_PATH, sheet_name='Cobertura_Por_UC')
    
    # Clean text columns
    for col in df_all.columns:
        df_all[col] = df_all[col].apply(clean_val)
        
    return df_all, df_resumo, df_uc

def generate_interactive_html(df_all, df_resumo, df_uc):
    records = df_all.to_dict(orient='records')
    uc_records = df_uc.to_dict(orient='records')
    for r in uc_records:
        for k, v in r.items():
            if pd.isna(v):
                r[k] = ""
                
    json_data = json.dumps(records, ensure_ascii=False)
    json_uc_data = json.dumps(uc_records, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auditoria Bibliográfica — PPC Técnico em Administração (IFSC Garopaba)</title>

  <!-- Google Fonts & Bootstrap Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

  <style>
    :root {{
      --ifsc-green: #10b981;
      --ifsc-dark-green: #059669;
      --ifsc-red: #ef4444;
      --bg-dark: #090d16;
      --bg-card: #131b2e;
      --bg-card-hover: #1e293b;
      --border-color: rgba(255, 255, 255, 0.12);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent-blue: #38bdf8;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --accent-rose: #f43f5e;
      --radius-lg: 16px;
      --radius-md: 10px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
    }}

    .font-outfit {{ font-family: 'Outfit', sans-serif; }}
    .font-code {{ font-family: 'Fira Code', monospace; }}

    /* HEADER */
    header.app-header {{
      background: linear-gradient(135deg, #064e3b 0%, #090d16 100%);
      border-bottom: 2px solid var(--border-color);
      padding: 1.8rem 1.5rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }}

    .header-container {{
      max-width: 1380px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.2rem;
    }}

    .brand-area {{
      display: flex;
      align-items: center;
      gap: 1.2rem;
    }}

    .brand-logo-bg {{
      background: #ffffff;
      padding: 6px 12px;
      border-radius: 10px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .brand-logo-bg img {{
      height: 44px;
      object-fit: contain;
    }}

    .brand-titles h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
    }}

    .brand-titles p {{
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    .header-actions {{
      display: flex;
      gap: 0.8rem;
      flex-wrap: wrap;
    }}

    .btn-action {{
      padding: 0.55rem 1.1rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      text-decoration: none;
      transition: all 0.2s ease;
      border: 1px solid transparent;
    }}

    .btn-emerald {{
      background: var(--ifsc-green);
      color: #ffffff;
    }}
    .btn-emerald:hover {{
      background: var(--ifsc-dark-green);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }}

    .btn-outline {{
      background: rgba(255, 255, 255, 0.06);
      border-color: var(--border-color);
      color: var(--text-main);
    }}
    .btn-outline:hover {{
      background: rgba(255, 255, 255, 0.12);
      transform: translateY(-2px);
    }}

    /* MAIN CONTAINER */
    main.main-container {{
      max-width: 1380px;
      margin: 1.5rem auto;
      padding: 0 1.5rem;
      width: 100%;
      flex: 1;
    }}

    /* KPI GRID */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.2rem;
      margin-bottom: 2rem;
    }}

    .kpi-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.4rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .kpi-card:hover {{
      transform: translateY(-3px);
      border-color: rgba(255, 255, 255, 0.25);
    }}

    .kpi-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }}
    .kpi-title {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .kpi-icon {{
      font-size: 1.3rem;
      opacity: 0.9;
    }}
    .kpi-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.1rem;
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 0.3rem;
    }}
    .kpi-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .kpi-emerald {{ border-top: 4px solid var(--accent-emerald); }}
    .kpi-emerald .kpi-value {{ color: var(--accent-emerald); }}
    .kpi-emerald .kpi-icon {{ color: var(--accent-emerald); }}

    .kpi-blue {{ border-top: 4px solid var(--accent-blue); }}
    .kpi-blue .kpi-value {{ color: var(--accent-blue); }}
    .kpi-blue .kpi-icon {{ color: var(--accent-blue); }}

    .kpi-purple {{ border-top: 4px solid var(--accent-purple); }}
    .kpi-purple .kpi-value {{ color: var(--accent-purple); }}
    .kpi-purple .kpi-icon {{ color: var(--accent-purple); }}

    .kpi-rose {{ border-top: 4px solid var(--accent-rose); }}
    .kpi-rose .kpi-value {{ color: var(--accent-rose); }}
    .kpi-rose .kpi-icon {{ color: var(--accent-rose); }}

    .kpi-amber {{ border-top: 4px solid var(--accent-amber); }}
    .kpi-amber .kpi-value {{ color: var(--accent-amber); }}
    .kpi-amber .kpi-icon {{ color: var(--accent-amber); }}

    /* TABS */
    .dashboard-tabs {{
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 1.5rem;
      overflow-x: auto;
      padding-bottom: 4px;
    }}

    .tab-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: 'Outfit', sans-serif;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.75rem 1.2rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .tab-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }}
    .tab-btn.active {{
      color: #ffffff;
      background: rgba(16, 185, 129, 0.2);
      border-bottom: 2px solid var(--accent-emerald);
    }}

    .tab-pane {{ display: none; }}
    .tab-pane.active {{ display: block; animation: fadeIn 0.3s ease; }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(5px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* FILTER BAR */
    .filter-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.2rem;
      margin-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
    }}

    .search-input-wrapper {{
      position: relative;
      flex: 1;
      min-width: 280px;
    }}
    .search-input-wrapper i {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}
    .search-input {{
      width: 100%;
      background: #090d16;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.65rem 1rem 0.65rem 2.5rem;
      border-radius: 8px;
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{ border-color: var(--accent-emerald); }}

    .select-filter {{
      background: #090d16;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.65rem 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      outline: none;
      cursor: pointer;
    }}

    /* TABLES */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow-x: auto;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }}

    table.custom-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }}
    table.custom-table th {{
      background: rgba(15, 23, 42, 0.95);
      color: #94a3b8;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.76rem;
      letter-spacing: 0.6px;
      padding: 1rem 1.2rem;
      border-bottom: 2px solid var(--border-color);
    }}
    table.custom-table td {{
      padding: 0.9rem 1.2rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      vertical-align: middle;
    }}
    table.custom-table tr:hover td {{
      background: rgba(255, 255, 255, 0.03);
    }}

    /* BADGES */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.3rem 0.65rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.3px;
    }}
    .badge-sim {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-nao {{ background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.3); }}
    .badge-var {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-fnde {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-autor {{ background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }}

    .badge-basica {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; }}
    .badge-comp {{ background: rgba(148, 163, 184, 0.15); color: #cbd5e1; }}

    /* PROGRESS BAR */
    .progress-bar-bg {{
      background: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      height: 8px;
      width: 100%;
      overflow: hidden;
      margin-top: 4px;
    }}
    .progress-bar-fill {{
      height: 100%;
      border-radius: 10px;
      background: linear-gradient(90deg, #10b981, #38bdf8);
    }}

    /* ACCORDION */
    .uc-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 0.8rem;
      overflow: hidden;
      transition: border-color 0.2s;
    }}
    .uc-card:hover {{ border-color: rgba(255, 255, 255, 0.25); }}
    .uc-card-header {{
      padding: 1rem 1.3rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
      background: rgba(15, 23, 42, 0.4);
    }}
    .uc-card-body {{
      padding: 1.2rem;
      border-top: 1px solid var(--border-color);
      display: none;
      background: rgba(9, 13, 22, 0.5);
    }}
    .uc-card.open .uc-card-body {{ display: block; }}

    /* FOOTER */
    footer.app-footer {{
      background: #060911;
      border-top: 1px solid var(--border-color);
      padding: 1.5rem;
      text-align: center;
      font-size: 0.85rem;
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
          <h1>Auditoria do Acervo Bibliográfico — PPC Técnico em Administração</h1>
          <p>Cruzamento de 274 Referências do PPC 2026 vs. Catálogo Sophia (3.206 Obras) • IFSC Câmpus Garopaba</p>
        </div>
      </div>

      <div class="header-actions">
        <a href="relatorio_auditoria_biblioteca.pdf" target="_blank" class="btn-action btn-emerald">
          <i class="bi bi-file-earmark-pdf-fill"></i> Baixar Relatório PDF Oficial
        </a>
        <a href="Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx" download class="btn-action btn-outline">
          <i class="bi bi-file-earmark-excel-fill text-emerald"></i> Baixar Planilha Excel (.xlsx)
        </a>
        <a href="../../../index.html" class="btn-action btn-outline">
          <i class="bi bi-arrow-left"></i> Painel Geral do PPC
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN -->
  <main class="main-container">

    <!-- KPI CARDS -->
    <div class="kpi-grid">
      <div class="kpi-card kpi-emerald">
        <div class="kpi-header">
          <span class="kpi-title">Cobertura Geral</span>
          <i class="bi bi-pie-chart-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">73,0%</div>
        <div class="kpi-desc">200 de 274 referências presentes no acervo físico ou PNLD</div>
      </div>

      <div class="kpi-card kpi-blue">
        <div class="kpi-header">
          <span class="kpi-title">Bibliografia Básica</span>
          <i class="bi bi-book-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">78,2%</div>
        <div class="kpi-desc">97 de 124 obras básicas já disponíveis na biblioteca</div>
      </div>

      <div class="kpi-card kpi-purple">
        <div class="kpi-header">
          <span class="kpi-title">Bibliografia Complementar</span>
          <i class="bi bi-journal-text kpi-icon"></i>
        </div>
        <div class="kpi-value">68,7%</div>
        <div class="kpi-desc">103 de 150 obras complementares no catálogo</div>
      </div>

      <div class="kpi-card kpi-rose">
        <div class="kpi-header">
          <span class="kpi-title">Demanda Básica (Compras)</span>
          <i class="bi bi-cart-plus-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">27 Obras</div>
        <div class="kpi-desc">Títulos básicos ausentes para compra física ou Minha Biblioteca</div>
      </div>

      <div class="kpi-card kpi-amber">
        <div class="kpi-header">
          <span class="kpi-title">Variação de Edição</span>
          <i class="bi bi-arrow-repeat kpi-icon"></i>
        </div>
        <div class="kpi-value">24 Obras</div>
        <div class="kpi-desc">Edição diferente disponível (oportunidade de harmonização)</div>
      </div>
    </div>

    <!-- TABS -->
    <div class="dashboard-tabs">
      <button class="tab-btn active" onclick="switchTab('tab-ausentes')">
        <i class="bi bi-cart-dash-fill"></i> Obras Ausentes (Demanda de Aquisição) <span id="count-ausentes" class="badge badge-nao" style="margin-left:4px;">74</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-variacoes')">
        <i class="bi bi-arrow-left-right"></i> Variações de Edição / Ano <span id="count-variacoes" class="badge badge-var" style="margin-left:4px;">24</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-existentes')">
        <i class="bi bi-check-circle-fill"></i> Acervo Confirmado (Sophia) <span id="count-existentes" class="badge badge-sim" style="margin-left:4px;">200</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-ucs')">
        <i class="bi bi-folder2-open"></i> Auditoria por Unidade Curricular (45 UCs)
      </button>
      <button class="tab-btn" onclick="switchTab('tab-todas')">
        <i class="bi bi-list-columns-reverse"></i> Mapeamento Completo (274 Referências)
      </button>
    </div>

    <!-- FILTER BAR -->
    <div class="filter-bar">
      <div class="search-input-wrapper">
        <i class="bi bi-search"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Pesquisar por título do livro, autor, unidade curricular ou ISBN..." oninput="applyFilters()">
      </div>

      <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
        <select id="filterTipo" class="select-filter" onchange="applyFilters()">
          <option value="ALL">Todos os Tipos (Básica e Complementar)</option>
          <option value="Básica">Apenas Bibliografia Básica</option>
          <option value="Complementar">Apenas Bibliografia Complementar</option>
        </select>

        <select id="filterBloco" class="select-filter" onchange="applyFilters()">
          <option value="ALL">Todos os Blocos de Formação</option>
          <option value="Geral">Formação Geral</option>
          <option value="Técnica">Formação Técnica / Profissional</option>
        </select>

        <button class="btn-action btn-outline" onclick="resetFilters()">
          <i class="bi bi-arrow-counterclockwise"></i> Limpar Filtros
        </button>
      </div>
    </div>

    <!-- TAB 1: OBRAS AUSENTES -->
    <div id="tab-ausentes" class="tab-pane active">
      <div class="table-container">
        <table class="custom-table" id="tableAusentes">
          <thead>
            <tr>
              <th style="width: 20%;">Unidade Curricular</th>
              <th style="width: 10%;">Tipo</th>
              <th style="width: 25%;">Título da Obra</th>
              <th style="width: 20%;">Autor Principal</th>
              <th style="width: 10%;">Edição / Ano</th>
              <th style="width: 15%;">Situação no Acervo Sophia</th>
            </tr>
          </thead>
          <tbody id="tbodyAusentes">
            <!-- Dynamic JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 2: VARIAÇÕES DE EDIÇÃO -->
    <div id="tab-variacoes" class="tab-pane">
      <div class="table-container">
        <table class="custom-table" id="tableVariacoes">
          <thead>
            <tr>
              <th style="width: 18%;">Unidade Curricular</th>
              <th style="width: 10%;">Tipo</th>
              <th style="width: 22%;">Título & Autor</th>
              <th style="width: 12%;">Edição no PPC</th>
              <th style="width: 38%;">Edição Disponível no Sophia (Câmpus Garopaba)</th>
            </tr>
          </thead>
          <tbody id="tbodyVariacoes">
            <!-- Dynamic JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 3: EXISTENTES -->
    <div id="tab-existentes" class="tab-pane">
      <div class="table-container">
        <table class="custom-table" id="tableExistentes">
          <thead>
            <tr>
              <th style="width: 18%;">Unidade Curricular</th>
              <th style="width: 8%;">Tipo</th>
              <th style="width: 26%;">Título da Obra</th>
              <th style="width: 18%;">Autor Principal</th>
              <th style="width: 12%;">Exemplares</th>
              <th style="width: 18%;">Status de Disponibilidade</th>
            </tr>
          </thead>
          <tbody id="tbodyExistentes">
            <!-- Dynamic JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 4: AUDITORIA POR UC -->
    <div id="tab-ucs" class="tab-pane">
      <div id="accordionUCs">
        <!-- Dynamic JS -->
      </div>
    </div>

    <!-- TAB 5: MAPEAMENTO COMPLETO -->
    <div id="tab-todas" class="tab-pane">
      <div class="table-container">
        <table class="custom-table" id="tableTodas">
          <thead>
            <tr>
              <th style="width: 18%;">Unidade Curricular</th>
              <th style="width: 8%;">Tipo</th>
              <th style="width: 24%;">Título da Obra</th>
              <th style="width: 16%;">Autor Principal</th>
              <th style="width: 10%;">Exemplares</th>
              <th style="width: 10%;">Existe?</th>
              <th style="width: 14%;">Observação Técnica</th>
            </tr>
          </thead>
          <tbody id="tbodyTodas">
            <!-- Dynamic JS -->
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="app-footer">
    <div class="header-container" style="justify-content: center; text-align: center;">
      <p>Comissão de Reformulação do PPC Técnico em Administração Integrado ao Ensino Médio • IFSC Câmpus Garopaba (2026)</p>
    </div>
  </footer>

  <!-- SCRIPT DE DADOS E INTERATIVIDADE -->
  <script>
    const allData = {json_data};
    const ucData = {json_uc_data};

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      
      document.getElementById(tabId).classList.add('active');
      event.currentTarget.classList.add('active');
    }}

    function renderTables(data) {{
      // 1. Ausentes
      const tbodyAusentes = document.getElementById('tbodyAusentes');
      const ausentes = data.filter(d => d.Existe_Biblioteca === 'NÃO');
      document.getElementById('count-ausentes').innerText = ausentes.length;

      tbodyAusentes.innerHTML = ausentes.map(d => `
        <tr>
          <td><strong>${{d.UC_Nome}}</strong><br><small style="color:var(--text-muted)">${{d.Bloco_Formacao}} • ${{d.Ano_Semestre}}</small></td>
          <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
          <td><strong>${{d.Titulo_Obra}}</strong></td>
          <td>${{d.Autor_Principal || 'Institucional'}}</td>
          <td>${{d.Edicao_PPC ? d.Edicao_PPC + 'ª ed.' : ''}} ${{d.Ano_PPC || ''}}</td>
          <td>
            <span class="badge ${{d.Status === 'NAO_EXISTE_AUTOR_PRESENTE' ? 'badge-autor' : 'badge-nao'}}">
              ${{d.Status === 'NAO_EXISTE_AUTOR_PRESENTE' ? '<i class="bi bi-person-check"></i> Autor no Acervo' : '<i class="bi bi-x-circle"></i> Ausente'}}
            </span>
            <div style="font-size:0.75rem; color:var(--text-muted); margin-top:3px;">${{d.Observacao_Tecnica}}</div>
          </td>
        </tr>
      `).join('');

      // 2. Variações
      const tbodyVariacoes = document.getElementById('tbodyVariacoes');
      const variacoes = data.filter(d => d.Status === 'EXISTE_EDICAO_DIFERENTE');
      document.getElementById('count-variacoes').innerText = variacoes.length;

      tbodyVariacoes.innerHTML = variacoes.map(d => `
        <tr>
          <td><strong>${{d.UC_Nome}}</strong></td>
          <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
          <td><strong>${{d.Titulo_Obra}}</strong><br><small style="color:var(--text-muted)">${{d.Autor_Principal}}</small></td>
          <td><span class="badge badge-var">${{d.Edicao_PPC ? d.Edicao_PPC + 'ª ed.' : ''}} ${{d.Ano_PPC || ''}}</span></td>
          <td>
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:4px;">
              <span class="badge badge-sim"><i class="bi bi-stack"></i> ${{d.Exemplares_Fisicos || 1}} ex. no Câmpus</span>
            </div>
            <div style="font-size:0.82rem; line-height:1.4;">${{d.Referencia_Acervo_Sophia}}</div>
            <div style="font-size:0.75rem; color:#34d399; margin-top:3px;"><i class="bi bi-info-circle"></i> ${{d.Observacao_Tecnica}}</div>
          </td>
        </tr>
      `).join('');

      // 3. Existentes
      const tbodyExistentes = document.getElementById('tbodyExistentes');
      const existentes = data.filter(d => d.Existe_Biblioteca === 'SIM');
      document.getElementById('count-existentes').innerText = existentes.length;

      tbodyExistentes.innerHTML = existentes.map(d => {{
        const exCount = d.Exemplares_Fisicos;
        const exBadge = d.Status === 'MATERIAL_FNDE' 
          ? '<span class="badge badge-fnde"><i class="bi bi-person-fill"></i> PNLD (1/Aluno)</span>'
          : `<span class="badge badge-sim"><i class="bi bi-stack"></i> ${{exCount || 1}} ${{exCount > 1 ? 'Exs.' : 'Ex.'}} Físicos</span>`;

        return `
          <tr>
            <td><strong>${{d.UC_Nome}}</strong></td>
            <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
            <td><strong>${{d.Titulo_Obra}}</strong></td>
            <td>${{d.Autor_Principal}}</td>
            <td>${{exBadge}}</td>
            <td>
              <span class="badge ${{d.Status === 'EXISTE_NO_ACERVO' ? 'badge-sim' : (d.Status === 'MATERIAL_FNDE' ? 'badge-fnde' : 'badge-var')}}">
                <i class="bi bi-check2-circle"></i> ${{d.Status_Legenda}}
              </span>
            </td>
          </tr>
        `;
      }}).join('');

      // 4. Todas
      const tbodyTodas = document.getElementById('tbodyTodas');
      tbodyTodas.innerHTML = data.map(d => {{
        const exCount = d.Exemplares_Fisicos;
        const exBadge = d.Existe_Biblioteca === 'SIM'
          ? (d.Status === 'MATERIAL_FNDE' ? '<span class="badge badge-fnde">PNLD</span>' : `<span class="badge badge-sim"><i class="bi bi-stack"></i> ${{exCount || 1}} ex.</span>`)
          : '<span class="badge badge-nao">0 ex.</span>';

        return `
          <tr>
            <td><strong>${{d.UC_Nome}}</strong></td>
            <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
            <td><strong>${{d.Titulo_Obra}}</strong></td>
            <td>${{d.Autor_Principal}}</td>
            <td>${{exBadge}}</td>
            <td>
              <span class="badge ${{d.Existe_Biblioteca === 'SIM' ? 'badge-sim' : 'badge-nao'}}">
                ${{d.Existe_Biblioteca === 'SIM' ? '<i class="bi bi-check-lg"></i> SIM' : '<i class="bi bi-x-lg"></i> NÃO'}}
              </span>
            </td>
            <td><small style="color:var(--text-muted)">${{d.Observacao_Tecnica}}</small></td>
          </tr>
        `;
      }}).join('');

      // 5. UCs Accordion
      renderUCAccordion(data);
    }}

    function renderUCAccordion(filteredData) {{
      const container = document.getElementById('accordionUCs');
      
      const html = ucData.map(uc => {{
        const ucRefs = filteredData.filter(d => d.UC_ID === uc.UC_ID);
        if (ucRefs.length === 0) return '';
        
        const simCount = ucRefs.filter(d => d.Existe_Biblioteca === 'SIM').length;
        const totalCount = ucRefs.length;
        const pct = Math.round((simCount / totalCount) * 100);

        return `
          <div class="uc-card" id="uc-card-${{uc.UC_ID}}">
            <div class="uc-card-header" onclick="toggleUC(${{uc.UC_ID}})">
              <div style="display:flex; align-items:center; gap:0.8rem;">
                <span class="badge badge-basica font-code">UC ${{uc.UC_ID}}</span>
                <div>
                  <strong style="font-size:1rem; color:#ffffff;">${{uc.UC_Nome}}</strong>
                  <div style="font-size:0.8rem; color:var(--text-muted);">${{uc.Bloco_Formacao}} • ${{uc.Ano_Semestre}}</div>
                </div>
              </div>

              <div style="display:flex; align-items:center; gap:1.2rem; min-width:260px;">
                <div style="flex:1;">
                  <div style="display:flex; justify-content:space-between; font-size:0.78rem; margin-bottom:2px;">
                    <span>Disponibilidade:</span>
                    <strong style="color:${{pct >= 75 ? '#34d399' : (pct >= 50 ? '#fbbf24' : '#fb7185')}}">${{simCount}}/${{totalCount}} (${{pct}}%)</strong>
                  </div>
                  <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width: ${{pct}}%; background:${{pct >= 75 ? '#10b981' : (pct >= 50 ? '#f59e0b' : '#f43f5e')}}"></div>
                  </div>
                </div>
                <i class="bi bi-chevron-down" id="uc-icon-${{uc.UC_ID}}"></i>
              </div>
            </div>

            <div class="uc-card-body" id="uc-body-${{uc.UC_ID}}">
              <table class="custom-table" style="font-size:0.84rem;">
                <thead>
                  <tr>
                    <th>Tipo</th>
                    <th>Título & Autor</th>
                    <th>Exemplares</th>
                    <th>Situação no Sophia</th>
                    <th>Observação</th>
                  </tr>
                </thead>
                <tbody>
                  ${{ucRefs.map(r => `
                    <tr>
                      <td><span class="badge ${{r.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{r.Tipo_Bibliografia}}</span></td>
                      <td><strong>${{r.Titulo_Obra}}</strong><br><small style="color:var(--text-muted)">${{r.Autor_Principal}}</small></td>
                      <td>
                        <span class="badge ${{r.Existe_Biblioteca === 'SIM' ? 'badge-sim' : 'badge-nao'}}">
                          ${{r.Status === 'MATERIAL_FNDE' ? 'PNLD' : (r.Exemplares_Fisicos ? r.Exemplares_Fisicos + ' ex.' : '0 ex.')}}
                        </span>
                      </td>
                      <td>
                        <span class="badge ${{r.Existe_Biblioteca === 'SIM' ? 'badge-sim' : 'badge-nao'}}">
                          ${{r.Status_Legenda}}
                        </span>
                      </td>
                      <td><small style="color:var(--text-muted)">${{r.Observacao_Tecnica}}</small></td>
                    </tr>
                  `).join('')}}
                </tbody>
              </table>
            </div>
          </div>
        `;
      }}).join('');

      container.innerHTML = html || '<p style="text-align:center; padding:2rem; color:var(--text-muted);">Nenhuma unidade curricular encontrada para os filtros selecionados.</p>';
    }}

    function toggleUC(id) {{
      const card = document.getElementById('uc-card-' + id);
      card.classList.toggle('open');
      const icon = document.getElementById('uc-icon-' + id);
      if (card.classList.contains('open')) {{
        icon.className = 'bi bi-chevron-up';
      }} else {{
        icon.className = 'bi bi-chevron-down';
      }}
    }}

    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase();
      const tipo = document.getElementById('filterTipo').value;
      const bloco = document.getElementById('filterBloco').value;

      const filtered = allData.filter(d => {{
        const matchQuery = !query || 
          (d.Titulo_Obra && d.Titulo_Obra.toLowerCase().includes(query)) ||
          (d.Autor_Principal && d.Autor_Principal.toLowerCase().includes(query)) ||
          (d.UC_Nome && d.UC_Nome.toLowerCase().includes(query)) ||
          (d.Referencia_PPC && d.Referencia_PPC.toLowerCase().includes(query));

        const matchTipo = (tipo === 'ALL') || (d.Tipo_Bibliografia === tipo);
        const matchBloco = (bloco === 'ALL') || (d.Bloco_Formacao && d.Bloco_Formacao.includes(bloco));

        return matchQuery && matchTipo && matchBloco;
      }});

      renderTables(filtered);
    }}

    function resetFilters() {{
      document.getElementById('searchInput').value = '';
      document.getElementById('filterTipo').value = 'ALL';
      document.getElementById('filterBloco').value = 'ALL';
      renderTables(allData);
    }}

    // Initial render
    document.addEventListener('DOMContentLoaded', () => {{
      renderTables(allData);
    }});
  </script>

</body>
</html>
"""

    html_path = os.path.join(CHECK_DIR, "dashboard_biblioteca.html")
    index_check_path = os.path.join(CHECK_DIR, "index.html")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(index_check_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Página HTML interativa gerada em: {html_path}")

def generate_latex_pdf_report(df_all, df_resumo, df_uc):
    tex_path = os.path.join(CHECK_DIR, "relatorio_auditoria_biblioteca.tex")
    
    df_nao_b = df_all[(df_all["Existe_Biblioteca"] == "NÃO") & (df_all["Tipo_Bibliografia"] == "Básica")].copy()
    df_var = df_all[df_all["Status"] == "EXISTE_EDICAO_DIFERENTE"].copy()
    
    def escape_tex(text):
        if not text or pd.isna(text) or str(text).lower() == 'nan': return ""
        text = str(text).strip()
        text = text.replace("—", "--").replace("–", "--")
        text = text.replace("\\", "\\textbackslash ")
        text = text.replace("&", "\\&").replace("%", "\\%").replace("$", "\\$")
        text = text.replace("#", "\\#").replace("_", "\\_").replace("{", "\\{").replace("}", "\\}")
        text = text.replace("~", "\\textasciitilde ").replace("^", "\\textasciicircum ")
        return text

    def format_ed_ano(ed, ano):
        ed_str = clean_val(ed)
        ano_str = clean_val(ano)
        parts = []
        if ed_str:
            parts.append(f"{ed_str}. ed.")
        if ano_str:
            parts.append(ano_str)
        return ", ".join(parts) if parts else "N/D"

    tex_content = r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{geometry}
\geometry{top=1.8cm, bottom=1.8cm, left=1.8cm, right=1.8cm}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{tabularx}
\usepackage{xltabular}
\usepackage{float}
\usepackage{booktabs}
\usepackage{colortbl}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{titlesec}

% Cores Oficiais IFSC
\definecolor{ifscgreen}{RGB}{16, 140, 80}
\definecolor{ifsclightgreen}{RGB}{235, 248, 240}
\definecolor{ifscdark}{RGB}{15, 23, 42}
\definecolor{ifscred}{RGB}{220, 38, 38}
\definecolor{ifscamber}{RGB}{217, 119, 6}
\definecolor{cinzaClaro}{RGB}{248, 250, 252}
\definecolor{cinzaBorda}{RGB}{226, 232, 240}

\hypersetup{
    colorlinks=true,
    linkcolor=ifscgreen,
    urlcolor=ifscgreen,
    citecolor=ifscgreen
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textcolor{ifscgreen}{\textbf{IFSC Câmpus Garopaba}} \textbullet{} PPC Técnico em Administração}
\fancyhead[R]{\small Auditoria do Acervo Bibliográfico (Sophia)}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

\titleformat{\section}{\large\bfseries\color{ifscgreen}}{\thesection}{1em}{}[\titlerule]
\titleformat{\subsection}{\normalsize\bfseries\color{ifscdark}}{\thesubsection}{1em}{}

\begin{document}

% --- CABEÇALHO INSTITUCIONAL ---
\begin{center}
    {\large \textbf{INSTITUTO FEDERAL DE SANTA CATARINA}}\\[2pt]
    {\normalsize CÂMPUS GAROPABA}\\[2pt]
    {\small DEPARTAMENTO DE ENSINO, PESQUISA E EXTENSÃO (DEPE)}\\[10pt]
    
    {\LARGE \textbf{\textcolor{ifscgreen}{Relatório Técnico de Auditoria do Acervo Bibliográfico}}}\\[4pt]
    {\large \textbf{Projeto Pedagógico de Curso -- Técnico em Administração Integrado (PPC 2026)}}\\[6pt]
    {\small \textbf{Destinatário:} Bibliotecário David / Equipe da Biblioteca \quad \textbullet{} \quad \textbf{Data:} 28 de Agosto de 2026}
\end{center}

\vspace{0.2cm}
\hrule height 1.2pt \relax
\vspace{0.3cm}

\section{Apresentação e Metodologia}
O presente relatório consolida a auditoria bibliográfica realizada pela Comissão de Reformulação do PPC do Curso Técnico em Administração Integrado ao Ensino Médio do IFSC Câmpus Garopaba. Foi realizado o cruzamento exaustivo entre todas as \textbf{274 referências bibliográficas} adotadas nas 45 Unidades Curriculares do curso e o catálogo do sistema Sophia (\textbf{3.206 títulos catalogados} da Biblioteca do Câmpus Garopaba).

\section{Indicadores Gerais de Cobertura}

\begin{table}[H]
\centering
\small
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Indicador / Métrica}} & \textcolor{white}{\textbf{Quantidade}} & \textcolor{white}{\textbf{Percentual}} \\ \hline
\rowcolor{cinzaClaro}
Total de Unidades Curriculares (UCs) Auditadas & 45 UCs & 100,0\% \\ \hline
Total Geral de Referências no PPC & 274 obras & 100,0\% \\ \hline
\rowcolor{cinzaClaro}
• Bibliografia Básica (Total de Títulos) & 124 obras & 45,3\% \\ \hline
• Bibliografia Complementar (Total de Títulos) & 150 obras & 54,7\% \\ \hline
\rowcolor{ifsclightgreen}
\textbf{Obras EXISTENTES na Biblioteca (Físico / PNLD)} & \textbf{200 obras} & \textbf{73,0\%} \\ \hline
\rowcolor{ifsclightgreen}
\textbf{• Cobertura da Bibliografia Básica} & \textbf{97 obras} & \textbf{78,2\%} \\ \hline
\rowcolor{ifsclightgreen}
• Cobertura da Bibliografia Complementar & 103 obras & 68,7\% \\ \hline
\rowcolor{cinzaClaro}
\textbf{Obras NÃO EXISTENTES no Acervo Físico} & \textbf{74 obras} & \textbf{27,0\%} \\ \hline
\rowcolor{cinzaClaro}
• Ausentes na Bibliografia Básica (Prioridade Alta para Compra) & 27 obras & 21,8\% \\ \hline
• Ausentes na Bibliografia Complementar & 47 obras & 31,3\% \\ \hline
\end{tabularx}
\caption{Quadro Resumo de Disponibilidade do Acervo}
\end{table}

\section{Prioridade 1: Bibliografia BÁSICA Ausente no Acervo Físico}
Solicita-se à equipe da biblioteca priorizar a conferência destas 27 obras nas plataformas virtuais (\textit{Minha Biblioteca / Pearson}) ou a inclusão na lista prioritária de aquisições:

\vspace{0.2cm}
\begin{xltabular}{\linewidth}{|p{3.8cm}|p{3.2cm}|X|p{2.2cm}|}
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Autor Principal}} & \textcolor{white}{\textbf{Título da Obra}} & \textcolor{white}{\textbf{Edição/Ano}} \\ \hline
\endfirsthead
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Autor Principal}} & \textcolor{white}{\textbf{Título da Obra}} & \textcolor{white}{\textbf{Edição/Ano}} \\ \hline
\endhead
"""

    for _, row in df_nao_b.iterrows():
        uc_t = escape_tex(row['UC_Nome'])
        aut_t = escape_tex(str(row['Autor_Principal'])[:35]) if str(row['Autor_Principal']).strip() else 'Institucional / MEC'
        tit_t = escape_tex(str(row['Titulo_Obra'])[:45])
        ed_ano = escape_tex(format_ed_ano(row['Edicao_PPC'], row['Ano_PPC']))
        tex_content += f"{uc_t} & {aut_t} & \\textbf{{{tit_t}}} & {ed_ano} \\\\ \\hline\n"

    tex_content += r"""\end{xltabular}

\newpage
\section{Obras com Variação de Edição/Ano Disponíveis no Sophia}
Foram identificadas 24 obras em que a biblioteca já possui o exemplar físico, porém em edição ou ano distinto daquele citado no PPC (oportunidade para atualização no texto do PPC):

\vspace{0.2cm}
\begin{xltabular}{\linewidth}{|p{3.6cm}|c|p{3.0cm}|X|p{2.4cm}|}
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Tipo}} & \textcolor{white}{\textbf{Autor}} & \textcolor{white}{\textbf{Título}} & \textcolor{white}{\textbf{Edição PPC}} \\ \hline
\endfirsthead
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Tipo}} & \textcolor{white}{\textbf{Autor}} & \textcolor{white}{\textbf{Título}} & \textcolor{white}{\textbf{Edição PPC}} \\ \hline
\endhead
"""

    for _, row in df_var.iterrows():
        uc_t = escape_tex(row['UC_Nome'])
        tipo_t = escape_tex(row['Tipo_Bibliografia'])
        aut_t = escape_tex(str(row['Autor_Principal'])[:25])
        tit_t = escape_tex(str(row['Titulo_Obra'])[:35])
        ed_ano = escape_tex(format_ed_ano(row['Edicao_PPC'], row['Ano_PPC']))
        tex_content += f"{uc_t} & {tipo_t} & {aut_t} & {tit_t} & {ed_ano} \\\\ \\hline\n"

    tex_content += r"""\end{xltabular}

\vspace{0.5cm}
\noindent\rule{\linewidth}{0.4pt}
\begin{center}
    \small \textbf{Comissão de Reformulação do PPC Técnico em Administração Integrado ao Ensino Médio}\\
    IFSC Câmpus Garopaba \textbullet{} Agosto de 2026
\end{center}

\end{document}
"""

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    print(f"Código LaTeX gerado em: {tex_path}")
    
    # Compile with tectonic
    cmd = f"tectonic {tex_path}"
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=CHECK_DIR)
        if res.returncode == 0:
            print("PDF compilado com sucesso via Tectonic: relatorio_auditoria_biblioteca.pdf")
        else:
            print("Erro ao compilar PDF:", res.stderr)
    except Exception as e:
        print("Exceção ao compilar:", e)

def update_root_dashboard():
    with open(ROOT_INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    if "tab-biblioteca" not in html:
        old_tabs = '<button class="tab-btn" onclick="showTab(\'tab-base\')"><i class="bi bi-folder-fill"></i> Base de Conhecimento</button>'
        new_tabs = '<button class="tab-btn" onclick="showTab(\'tab-biblioteca\')"><i class="bi bi-book-half"></i> Auditoria de Biblioteca (Sophia)</button>\n      ' + old_tabs
        html = html.replace(old_tabs, new_tabs)

        tab_pane_html = """
    <!-- TAB 6: AUDITORIA DE BIBLIOTECA (SOPHIA) -->
    <div id="tab-biblioteca" class="tab-pane">
      <div class="panel-card">
        <div class="panel-header">
          <div class="panel-title">
            <i class="bi bi-journal-check"></i>
            Auditoria do Acervo Bibliográfico (PPC vs. Sistema Sophia)
          </div>
          <div style="display: flex; gap: 0.8rem;">
            <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/dashboard_biblioteca.html" target="_blank" class="btn-action btn-emerald">
              <i class="bi bi-window-fullscreen"></i> Abrir Dashboard Interativo da Biblioteca
            </a>
            <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/relatorio_auditoria_biblioteca.pdf" target="_blank" class="btn-action btn-outline">
              <i class="bi bi-file-earmark-pdf-fill"></i> Baixar Relatório PDF (David)
            </a>
          </div>
        </div>

        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
          Cruzamento automatizado entre todas as <strong>274 referências bibliográficas</strong> adotadas no PPC do Técnico em Administração e o inventário oficial de <strong>3.206 obras</strong> do Sistema Sophia da Biblioteca do Câmpus Garopaba.
        </p>

        <div class="grid-2">
          <div>
            <h3 style="color: var(--accent-emerald); font-size: 1.1rem; margin-bottom: 1rem; font-family: 'Outfit', sans-serif;">
              <i class="bi bi-bar-chart-fill me-1"></i> Indicadores de Cobertura do Acervo:
            </h3>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(16,185,129,0.2); color:var(--accent-emerald);"><i class="bi bi-check-circle-fill"></i></div>
              <div class="step-content">
                <h4>78,2% da Bibliografia Básica Atendida</h4>
                <p>97 de 124 obras básicas já estão fisicamente disponíveis na biblioteca ou via PNLD/FNDE.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(56,189,248,0.2); color:var(--accent-blue);"><i class="bi bi-pie-chart-fill"></i></div>
              <div class="step-content">
                <h4>73,0% de Cobertura Global do Curso</h4>
                <p>200 títulos disponíveis no acervo para suporte imediato às aulas das 45 Unidades Curriculares.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(244,63,94,0.2); color:var(--accent-rose);"><i class="bi bi-cart-plus-fill"></i></div>
              <div class="step-content">
                <h4>27 Obras Básicas Mapeadas para Aquisição</h4>
                <p>Lista prioritária gerada para conferência nas plataformas virtuais (Minha Biblioteca/Pearson) e compra.</p>
              </div>
            </div>
          </div>

          <div>
            <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-bottom: 1rem; font-family: 'Outfit', sans-serif;">
              <i class="bi bi-file-earmark-spreadsheet-fill me-1"></i> Documentos & Artefatos Disponíveis:
            </h3>

            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.2rem; display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/dashboard_biblioteca.html" target="_blank" style="color:var(--accent-emerald); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-box-arrow-up-right"></i> Painel Interativo da Biblioteca com Filtros Dinâmicos
              </a>
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/relatorio_auditoria_biblioteca.pdf" target="_blank" style="color:var(--accent-blue); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-file-earmark-pdf"></i> Relatório Oficial de Auditoria em PDF (Formatado em LaTeX)
              </a>
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx" download style="color:var(--accent-amber); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-file-earmark-excel"></i> Planilha Consolidada de Auditoria (.xlsx com 6 abas)
              </a>
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/sumario_executivo_david_biblioteca.md" target="_blank" style="color:var(--text-main); text-decoration:none; font-size:0.9rem; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-envelope-paper-fill"></i> Memorando Executivo para o Bibliotecário David (.md)
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
        html = html.replace('<!-- TAB 5: BASE DE CONHECIMENTO -->', tab_pane_html + '\n    <!-- TAB 5: BASE DE CONHECIMENTO -->')
        
        with open(ROOT_INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(html)
        print("Root index.html atualizado com a nova Tab da Biblioteca!")

def main():
    df_all, df_resumo, df_uc = load_data()
    generate_interactive_html(df_all, df_resumo, df_uc)
    generate_latex_pdf_report(df_all, df_resumo, df_uc)
    update_root_dashboard()
    print("Todas as tarefas concluídas com sucesso!")

if __name__ == "__main__":
    main()
