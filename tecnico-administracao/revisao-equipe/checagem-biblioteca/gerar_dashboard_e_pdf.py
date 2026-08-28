#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador da Página Web Interativa (Dashboard) e do Documento PDF Estilizado em LaTeX
para a Auditoria do Acervo Bibliográfico do PPC Técnico em Administração (IFSC Garopaba).
Aplica a Regra Normativa do IFSC:
- Bibliografia Básica: Mínimo de 2 títulos com ao menos 3 exemplares físicos no acervo do câmpus.
- Bibliografia Complementar: Mínimo de 3 títulos com ao menos 1 exemplar físico no acervo do câmpus.
"""

import os
import re
import json
import subprocess
import pandas as pd

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/tecnico-administracao"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
EXCEL_PATH = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx")
ACERVO_EXEMPLARES_PATH = os.path.join(CHECK_DIR, "Acervo e exemplares.XLS")
ROOT_INDEX_PATH = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/index.html"

def clean_val(val):
    if pd.isna(val) or val is None or str(val).strip() == "" or str(val).strip().lower() == "nan":
        return ""
    s = str(val).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return s

def clean_entry(text):
    t = str(text).strip()
    if not t or t.startswith('Referência bibliográfica') or t.startswith('(Ordenadas') or t == 'IFSC - Câmpus Garopaba' or re.match(r'^\d{2}/\d{2}/\d{4}$', t):
        return None
    if t.startswith('Total:') or ('IFSC - Garopaba - ' in t and len(t) < 40 and not 'ISBN' in t):
        return None
    return t

def load_data():
    df_all = pd.read_excel(EXCEL_PATH, sheet_name='Mapeamento_Completo_PPC')
    df_resumo = pd.read_excel(EXCEL_PATH, sheet_name='Resumo_Geral')
    df_uc = pd.read_excel(EXCEL_PATH, sheet_name='Cobertura_Por_UC')
    
    # Clean text columns
    for col in df_all.columns:
        df_all[col] = df_all[col].apply(clean_val)
        
    # Build UC Diagnostic Summaries
    uc_diagnostics = []
    for uc_id, group in df_all.groupby('UC_ID'):
        uc_nome = group['UC_Nome'].iloc[0]
        semestre = group['Ano_Semestre'].iloc[0]
        bloco = group['Bloco_Formacao'].iloc[0]
        
        b_group = group[group['Tipo_Bibliografia'] == 'Básica']
        c_group = group[group['Tipo_Bibliografia'] == 'Complementar']
        
        b_total = len(b_group)
        b_sim = len(b_group[b_group['Existe_Biblioteca'] == 'SIM'])
        b_nao = len(b_group[b_group['Existe_Biblioteca'] == 'NÃO'])
        b_deficit = pd.to_numeric(b_group['Deficit_Exemplares_Compra'], errors='coerce').fillna(0).astype(int).sum()
        
        c_total = len(c_group)
        c_sim = len(c_group[c_group['Existe_Biblioteca'] == 'SIM'])
        c_nao = len(c_group[c_group['Existe_Biblioteca'] == 'NÃO'])
        c_deficit = pd.to_numeric(c_group['Deficit_Exemplares_Compra'], errors='coerce').fillna(0).astype(int).sum()
        
        total_deficit = b_deficit + c_deficit
        var_ed = len(group[group['Status'] == 'EXISTE_EDICAO_DIFERENTE'])
        
        # Missing books details
        b_missing_books = b_group[b_group['Existe_Biblioteca'] == 'NÃO'][['Titulo_Obra', 'Autor_Principal', 'Edicao_PPC', 'Ano_PPC']].to_dict(orient='records')
        c_missing_books = c_group[c_group['Existe_Biblioteca'] == 'NÃO'][['Titulo_Obra', 'Autor_Principal', 'Edicao_PPC', 'Ano_PPC']].to_dict(orient='records')
        
        # Books needing extra physical copies
        b_low_copies = b_group[(b_group['Existe_Biblioteca'] == 'SIM') & (pd.to_numeric(b_group['Deficit_Exemplares_Compra'], errors='coerce') > 0)][['Titulo_Obra', 'Autor_Principal', 'Exemplares_Disponiveis', 'Deficit_Exemplares_Compra']].to_dict(orient='records')
        
        if b_nao > 0 or b_deficit > 0:
            status_code = 'CRITICA_BASICA'
            status_badge = 'badge-nao'
            status_label = f'Crítica: Déficit na Básica (+{b_deficit} ex.)'
            status_icon = 'bi-exclamation-octagon-fill'
            acao_sugerida = f"Aquisição/validação de {b_deficit} exemplar(es) para atingir a meta de 3 cópias por título básico."
        elif c_nao > 0 or c_deficit > 0:
            status_code = 'ATENCAO_COMPLEMENTAR'
            status_badge = 'badge-var'
            status_label = f'Atenção: Falta Complementar (+{c_deficit} ex.)'
            status_icon = 'bi-exclamation-triangle-fill'
            acao_sugerida = f"Básica regularizada (>= 3 ex.). Adquirir {c_deficit} exemplar(es) da bibliografia complementar."
        elif var_ed > 0:
            status_code = 'ATENCAO_EDICAO'
            status_badge = 'badge-fnde'
            status_label = 'Quantitativo Atendido c/ Variação'
            status_icon = 'bi-arrow-repeat'
            acao_sugerida = f"Exemplares atendidos no câmpus. Harmonizar {var_ed} edição(ões) no texto do PPC."
        else:
            status_code = 'CONFORME_100'
            status_badge = 'badge-sim'
            status_label = '100% Conforme Normativo'
            status_icon = 'bi-check-circle-fill'
            acao_sugerida = "Ementa 100% conforme: >= 2 títulos básicos (>= 3 ex.) e >= 3 títulos complementares (>= 1 ex.)."
            
        total_ref = len(group)
        sim_total = b_sim + c_sim
        pct_cobertura = round((sim_total / total_ref) * 100) if total_ref > 0 else 0
        pct_basica = round((b_sim / b_total) * 100) if b_total > 0 else 100

        uc_diagnostics.append({
            'uc_id': int(uc_id),
            'uc_nome': uc_nome,
            'semestre': semestre,
            'bloco': bloco,
            'b_total': b_total,
            'b_sim': b_sim,
            'b_nao': b_nao,
            'b_deficit': b_deficit,
            'c_total': c_total,
            'c_sim': c_sim,
            'c_nao': c_nao,
            'c_deficit': c_deficit,
            'total_deficit': total_deficit,
            'var_ed': var_ed,
            'total_ref': total_ref,
            'sim_total': sim_total,
            'pct_cobertura': pct_cobertura,
            'pct_basica': pct_basica,
            'status_code': status_code,
            'status_badge': status_badge,
            'status_label': status_label,
            'status_icon': status_icon,
            'acao_sugerida': acao_sugerida,
            'b_missing_books': b_missing_books,
            'c_missing_books': c_missing_books,
            'b_low_copies': b_low_copies
        })
        
    # Load all 3003 library items with copy counts
    df_raw_lib = pd.read_excel(ACERVO_EXEMPLARES_PATH)
    col1 = df_raw_lib[df_raw_lib.columns[1]].dropna().tolist()
    
    ppc_titles_norm = set()
    for _, row in df_all.iterrows():
        t = str(row['Titulo_Obra']).lower()
        if t: ppc_titles_norm.add(t[:25])

    all_library_items = []
    for idx, entry in enumerate(col1, 1):
        cleaned = clean_entry(entry)
        if not cleaned: continue
        
        ex_count = 1
        m = re.search(r'Exemplares:\s*IFSC\s*-\s*Garopaba\s*-\s*(\d+)\s*Ex', cleaned)
        if m:
            ex_count = int(m.group(1))
        else:
            m2 = re.search(r'Total\s*-\s*(\d+)\s*Ex', cleaned)
            if m2:
                ex_count = int(m2.group(1))
                
        ref_clean = re.sub(r'Exemplares:.*$', '', cleaned).strip()
        is_ppc = any(k in ref_clean.lower() for k in ppc_titles_norm if len(k) > 6)
        
        all_library_items.append({
            'id': idx,
            'ref': ref_clean,
            'exemplares': ex_count,
            'is_ppc': is_ppc
        })
        
    return df_all, df_resumo, df_uc, all_library_items, uc_diagnostics

def generate_interactive_html(df_all, df_resumo, df_uc, all_library_items, uc_diagnostics):
    def json_serial(obj):
        if hasattr(obj, 'item'):
            return obj.item()
        return str(obj)

    records = df_all.to_dict(orient='records')
    json_data = json.dumps(records, ensure_ascii=False, default=json_serial)
    json_diag_data = json.dumps(uc_diagnostics, ensure_ascii=False, default=json_serial)
    json_catalog_data = json.dumps(all_library_items, ensure_ascii=False, default=json_serial)
    
    total_exemplares_lib = sum(x['exemplares'] for x in all_library_items)
    
    # Calculate counts of UC statuses
    count_criticas = len([u for u in uc_diagnostics if u['status_code'] == 'CRITICA_BASICA'])
    count_atencao_comp = len([u for u in uc_diagnostics if u['status_code'] == 'ATENCAO_COMPLEMENTAR'])
    count_atencao_var = len([u for u in uc_diagnostics if u['status_code'] == 'ATENCAO_EDICAO'])
    count_conformes = len([u for u in uc_diagnostics if u['status_code'] == 'CONFORME_100'])
    count_com_problema = count_criticas + count_atencao_comp + count_atencao_var
    
    total_deficit_geral = sum(u['total_deficit'] for u in uc_diagnostics)
    total_deficit_basica = sum(u['b_deficit'] for u in uc_diagnostics)
    total_deficit_comp = sum(u['c_deficit'] for u in uc_diagnostics)
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auditoria Normativa de Acervo & Exemplares — PPC Técnico em Administração (IFSC Garopaba)</title>

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
      max-width: 1420px;
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
      font-size: 1.55rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
    }}

    .brand-titles p {{
      font-size: 0.85rem;
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
      max-width: 1420px;
      margin: 1.5rem auto;
      padding: 0 1.5rem;
      width: 100%;
      flex: 1;
    }}

    /* NORMATIVE BANNER */
    .normative-banner {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: var(--radius-lg);
      padding: 1.1rem 1.4rem;
      margin-bottom: 1.8rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }}
    .normative-badge {{
      background: rgba(16, 185, 129, 0.2);
      color: var(--accent-emerald);
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* KPI GRID */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 1.1rem;
      margin-bottom: 2rem;
    }}

    .kpi-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.3rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, border-color 0.2s ease;
      cursor: pointer;
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
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .kpi-icon {{
      font-size: 1.25rem;
      opacity: 0.9;
    }}
    .kpi-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 0.3rem;
    }}
    .kpi-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}

    .kpi-rose {{ border-top: 4px solid var(--accent-rose); }}
    .kpi-rose .kpi-value {{ color: var(--accent-rose); }}
    .kpi-rose .kpi-icon {{ color: var(--accent-rose); }}

    .kpi-amber {{ border-top: 4px solid var(--accent-amber); }}
    .kpi-amber .kpi-value {{ color: var(--accent-amber); }}
    .kpi-amber .kpi-icon {{ color: var(--accent-amber); }}

    .kpi-blue {{ border-top: 4px solid var(--accent-blue); }}
    .kpi-blue .kpi-value {{ color: var(--accent-blue); }}
    .kpi-blue .kpi-icon {{ color: var(--accent-blue); }}

    .kpi-emerald {{ border-top: 4px solid var(--accent-emerald); }}
    .kpi-emerald .kpi-value {{ color: var(--accent-emerald); }}
    .kpi-emerald .kpi-icon {{ color: var(--accent-emerald); }}

    .kpi-purple {{ border-top: 4px solid var(--accent-purple); }}
    .kpi-purple .kpi-value {{ color: var(--accent-purple); }}
    .kpi-purple .kpi-icon {{ color: var(--accent-purple); }}

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
      font-size: 0.92rem;
      font-weight: 600;
      padding: 0.75rem 1.1rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
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

    /* DIAGNOSTIC CARDS */
    .diag-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }}

    .diag-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.3rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .diag-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(255, 255, 255, 0.3);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }}

    .diag-card-critica {{ border-left: 5px solid var(--accent-rose); }}
    .diag-card-atencao {{ border-left: 5px solid var(--accent-amber); }}
    .diag-card-edicao {{ border-left: 5px solid var(--accent-blue); }}
    .diag-card-conforme {{ border-left: 5px solid var(--accent-emerald); }}

    .diag-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.8rem;
      gap: 0.5rem;
    }}
    .diag-uc-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.3;
    }}
    .diag-uc-meta {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    .diag-stats-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
      background: rgba(15, 23, 42, 0.6);
      padding: 0.7rem;
      border-radius: 8px;
      margin-bottom: 0.8rem;
      font-size: 0.8rem;
    }}

    .diag-missing-box {{
      background: rgba(244, 63, 94, 0.08);
      border: 1px dashed rgba(244, 63, 94, 0.3);
      border-radius: 8px;
      padding: 0.7rem;
      margin-bottom: 0.8rem;
      font-size: 0.8rem;
    }}
    .diag-missing-box strong {{
      color: #fb7185;
      display: block;
      margin-bottom: 0.3rem;
    }}
    .diag-missing-list {{
      list-style: none;
      padding-left: 0;
    }}
    .diag-missing-list li {{
      margin-bottom: 0.25rem;
      line-height: 1.35;
      color: #f1f5f9;
    }}

    .diag-action-box {{
      font-size: 0.8rem;
      color: #94a3b8;
      border-top: 1px solid var(--border-color);
      padding-top: 0.6rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
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
      font-size: 0.75rem;
      letter-spacing: 0.6px;
      padding: 1rem 1.2rem;
      border-bottom: 2px solid var(--border-color);
    }}
    table.custom-table td {{
      padding: 0.85rem 1.2rem;
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
    .badge-ppc-tag {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); font-weight: 800; }}

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
          <h1>Auditoria Normativa de Acervo & Exemplares — PPC Técnico em Administração</h1>
          <p>Aplicação da Regra Institucional: Mínimo de 3 Exs. na Básica e 1 Ex. na Complementar • IFSC Garopaba</p>
        </div>
      </div>

      <div class="header-actions">
        <button class="btn-action btn-emerald" onclick="switchTab('tab-sumario')">
          <i class="bi bi-envelope-paper-fill"></i> Ver Sumário Executivo (David)
        </button>
        <a href="relatorio_auditoria_biblioteca.pdf" target="_blank" class="btn-action btn-outline">
          <i class="bi bi-file-earmark-pdf-fill"></i> Relatório PDF Oficial
        </a>
        <a href="Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx" download class="btn-action btn-outline">
          <i class="bi bi-file-earmark-excel-fill text-emerald"></i> Planilha Excel (.xlsx)
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
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">
            • <strong>Bibliografia Básica:</strong> Mínimo 2 títulos de livros &rarr; <strong>ao menos 3 exemplares físicos</strong> de cada título no acervo do câmpus (ou PNLD).<br>
            • <strong>Bibliografia Complementar:</strong> Mínimo 3 títulos de livros &rarr; <strong>ao menos 1 exemplar físico</strong> de cada título no acervo do câmpus.
          </p>
        </div>
      </div>
      <div style="text-align:right;">
        <span class="normative-badge">
          <i class="bi bi-cart-check-fill"></i> Demanda Total de Compras: <strong>+{total_deficit_geral} exemplares</strong>
        </span>
      </div>
    </div>

    <!-- KPI CARDS FOCADOS EM QUANTITATIVOS NORMATIVOS -->
    <div class="kpi-grid">
      <div class="kpi-card kpi-rose" onclick="filterDiagBy('CRITICA_BASICA')">
        <div class="kpi-header">
          <span class="kpi-title">Compras Básica (&lt; 3 Exs.)</span>
          <i class="bi bi-cart-plus-fill kpi-icon"></i>
        </div>
        <div class="kpi-value">+{total_deficit_basica} Exs.</div>
        <div class="kpi-desc">Exemplares a adquirir para atingir a meta de 3 cópias por título básico</div>
      </div>

      <div class="kpi-card kpi-amber" onclick="filterDiagBy('ATENCAO_COMPLEMENTAR')">
        <div class="kpi-header">
          <span class="kpi-title">Compras Complementar (&lt; 1 Ex.)</span>
          <i class="bi bi-journal-plus kpi-icon"></i>
        </div>
        <div class="kpi-value">+{total_deficit_comp} Exs.</div>
        <div class="kpi-desc">Exemplares a adquirir para suprir 1 cópia dos títulos ausentes</div>
      </div>

      <div class="kpi-card kpi-blue" onclick="filterDiagBy('ATENCAO_EDICAO')">
        <div class="kpi-header">
          <span class="kpi-title">Variação de Edição / Ano</span>
          <i class="bi bi-arrow-repeat kpi-icon"></i>
        </div>
        <div class="kpi-value">{count_atencao_var} UCs</div>
        <div class="kpi-desc">Obras existem no acervo; requer atualização do texto do PPC</div>
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
        <i class="bi bi-kanban-fill"></i> Diagnóstico das 45 Ementas <span class="badge badge-nao" style="margin-left:4px;">{count_com_problema} com Pendência</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-ausentes')">
        <i class="bi bi-cart-dash-fill"></i> Títulos Ausentes para Aquisição <span id="count-ausentes" class="badge badge-nao" style="margin-left:4px;">{len(df_all[df_all['Existe_Biblioteca'] == 'NÃO'])}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-variacoes')">
        <i class="bi bi-arrow-left-right"></i> Variações de Edição / Ano <span id="count-variacoes" class="badge badge-var" style="margin-left:4px;">{len(df_all[df_all['Status'] == 'EXISTE_EDICAO_DIFERENTE'])}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-existentes')">
        <i class="bi bi-check-circle-fill"></i> Acervo Confirmado (Sophia) <span id="count-existentes" class="badge badge-sim" style="margin-left:4px;">{len(df_all[df_all['Existe_Biblioteca'] == 'SIM'])}</span>
      </button>
      <button class="tab-btn" onclick="switchTab('tab-ucs')">
        <i class="bi bi-folder2-open"></i> Auditoria por UC (Accordion)
      </button>
      <button class="tab-btn" onclick="switchTab('tab-todas')">
        <i class="bi bi-list-columns-reverse"></i> Mapeamento Geral (272 Obras)
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
          <option value="ALL">Status da Ementa: Todas as 45 UCs</option>
          <option value="COM_PROBLEMA">🚨 Todas as Ementas com Alguma Pendência ({count_com_problema} UCs)</option>
          <option value="CRITICA_BASICA">🔴 Críticas: Déficit na Básica ({count_criticas} UCs)</option>
          <option value="ATENCAO_COMPLEMENTAR">🟡 Atenção: Falta na Complementar ({count_atencao_comp} UCs)</option>
          <option value="ATENCAO_EDICAO">🔵 Atenção: Variação de Edição ({count_atencao_var} UCs)</option>
          <option value="CONFORME_100">🟢 100% Conformes Normativos ({count_conformes} UCs)</option>
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

    <!-- TAB EXCLUSIVA: SUMÁRIO EXECUTIVO PARA O DAVID -->
    <div id="tab-sumario" class="tab-pane">
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:2rem; margin-bottom:1.5rem;">
        
        <!-- Header do Memorando -->
        <div style="border-bottom:2px solid var(--border-color); padding-bottom:1.5rem; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
          <div>
            <span class="badge badge-sim" style="font-size:0.8rem; margin-bottom:0.5rem;"><i class="bi bi-file-earmark-text-fill"></i> Memorando Técnico Oficial</span>
            <h2 style="font-family:'Outfit', sans-serif; font-size:1.45rem; color:#ffffff; margin-top:0.3rem;">Sumário Executivo: Auditoria Normativa de Acervo & Quantitativos de Exemplares</h2>
            <div style="margin-top:0.8rem; font-size:0.88rem; color:var(--text-muted); line-height:1.7;">
              <strong>Para:</strong> David (Bibliotecário-Documentalista — IFSC Câmpus Garopaba)<br>
              <strong>De:</strong> Comissão de Reformulação do PPC Técnico em Administração Integrado<br>
              <strong>Data:</strong> 28 de Agosto de 2026<br>
              <strong>Assunto:</strong> Diagnóstico de Cobertura do Catálogo Sophia e Demanda de Aquisição de Exemplares Físicos
            </div>
          </div>
          <div style="display:flex; gap:0.6rem;">
            <button class="btn-action btn-emerald" onclick="window.print()">
              <i class="bi bi-printer-fill"></i> Imprimir / Salvar PDF
            </button>
            <a href="relatorio_auditoria_biblioteca.pdf" target="_blank" class="btn-action btn-outline">
              <i class="bi bi-file-earmark-pdf-fill"></i> Baixar Relatório LaTeX (.pdf)
            </a>
          </div>
        </div>

        <!-- Seção 1: Premissas Normativas -->
        <div style="margin-bottom:1.8rem;">
          <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:var(--accent-emerald); margin-bottom:0.6rem;">
            <i class="bi bi-1-circle-fill me-1"></i> 1. Premissas Normativas Institucionais (IFSC)
          </h3>
          <div style="background:rgba(15,23,42,0.6); border:1px solid var(--border-color); border-radius:10px; padding:1rem; font-size:0.88rem; line-height:1.6;">
            <p>Em consonância com as normas de regulação e avaliação de cursos do IFSC, a auditoria aplicou os seguintes critérios de quantitativos mínimos:</p>
            <ul style="margin-top:0.5rem; padding-left:1.2rem; color:#f1f5f9;">
              <li><strong>Bibliografia Básica:</strong> Mínimo de <strong>2 títulos de livros</strong> por Unidade Curricular, devendo o acervo do câmpus disponibilizar <strong>ao menos 3 exemplares físicos de cada título</strong> (ou livro PNLD com 1 exemplar por estudante).</li>
              <li><strong>Bibliografia Complementar:</strong> Mínimo de <strong>3 títulos de livros</strong> por Unidade Curricular, devendo o acervo do câmpus disponibilizar <strong>ao menos 1 exemplar físico de cada título</strong>.</li>
            </ul>
          </div>
        </div>

        <!-- Seção 2: Síntese de Indicadores & Demanda de Compras -->
        <div style="margin-bottom:1.8rem;">
          <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:var(--accent-emerald); margin-bottom:0.6rem;">
            <i class="bi bi-2-circle-fill me-1"></i> 2. Síntese Geral de Cobertura e Demanda de Aquisição
          </h3>
          <div class="table-container" style="margin-bottom:1rem;">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Indicador / Métrica Normativa</th>
                  <th>Quantitativo Mapeado</th>
                  <th>Percentual / Meta Institucional</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Total de Unidades Curriculares (UCs) Auditadas</td>
                  <td><strong>45 UCs</strong></td>
                  <td><span class="badge badge-sim">100% da Matriz</span></td>
                </tr>
                <tr>
                  <td>Total Geral de Títulos Bibliográficos no PPC</td>
                  <td><strong>272 títulos</strong></td>
                  <td>122 Básicos + 150 Complementares</td>
                </tr>
                <tr>
                  <td>Títulos EXISTENTES no Sophia de Garopaba (Físico / PNLD)</td>
                  <td><strong>200 títulos</strong></td>
                  <td><span class="badge badge-sim">73,5% de Cobertura</span></td>
                </tr>
                <tr>
                  <td>• Cobertura de Títulos na Bibliografia Básica</td>
                  <td><strong>97 títulos</strong></td>
                  <td><span class="badge badge-sim">79,5% Atendidos</span></td>
                </tr>
                <tr>
                  <td>• Cobertura de Títulos na Bibliografia Complementar</td>
                  <td><strong>103 títulos</strong></td>
                  <td><span class="badge badge-var">68,7% Atendidos</span></td>
                </tr>
                <tr style="background:rgba(244,63,94,0.08);">
                  <td><strong style="color:#fb7185;">DEMANDA DE COMPRAS: Bibliografia BÁSICA</strong></td>
                  <td><strong style="color:#fb7185;">+{total_deficit_basica} exemplares físicos</strong></td>
                  <td>Meta: &ge; 3 exemplares por título básico</td>
                </tr>
                <tr style="background:rgba(245,158,11,0.08);">
                  <td><strong style="color:#fbbf24;">DEMANDA DE COMPRAS: Bibliografia COMPLEMENTAR</strong></td>
                  <td><strong style="color:#fbbf24;">+{total_deficit_comp} exemplares físicos</strong></td>
                  <td>Meta: &ge; 1 exemplar por título complementar</td>
                </tr>
                <tr style="background:rgba(16,185,129,0.12);">
                  <td><strong style="color:#34d399; font-size:0.95rem;">TOTAL GERAL DE COMPRAS PARA O CÂMPUS GAROPABA</strong></td>
                  <td><strong style="color:#34d399; font-size:1.05rem;">+{total_deficit_geral} exemplares físicos</strong></td>
                  <td><span class="badge badge-sim">100% de Conformidade Normativa</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Seção 3: Relação Prioritária de Compras da Básica -->
        <div style="margin-bottom:1.8rem;">
          <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:#fb7185; margin-bottom:0.6rem;">
            <i class="bi bi-cart-plus-fill me-1"></i> 3. Prioridade 1: Relação de Obras da Bibliografia BÁSICA para Aquisição (Meta: 3 Exs.)
          </h3>
          <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:0.6rem;">
            Estas são as obras da Bibliografia Básica que exigem compra de 3 exemplares físicos ou verificação de licenças digitais na plataforma <em>Minha Biblioteca / Pearson</em>:
          </p>
          <div class="table-container">
            <table class="custom-table" style="font-size:0.84rem;">
              <thead>
                <tr>
                  <th>Unidade Curricular</th>
                  <th>Autor Principal</th>
                  <th>Título da Obra</th>
                  <th>Edição / Ano</th>
                  <th>Demanda</th>
                </tr>
              </thead>
              <tbody id="tbodySumarioBasica">
                <!-- Dynamic JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Seção 4: Obras com Variação de Edição -->
        <div style="margin-bottom:1rem;">
          <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:var(--accent-blue); margin-bottom:0.6rem;">
            <i class="bi bi-arrow-repeat me-1"></i> 4. Obras com Variação de Edição/Ano Disponíveis no Sophia
          </h3>
          <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:0.6rem;">
            A biblioteca possui <strong>24 títulos físicos</strong> no acervo, porém em edição ou ano distinto da citação no PPC. A comissão docente pode harmonizar a redação do PPC:
          </p>
          <div class="table-container">
            <table class="custom-table" style="font-size:0.84rem;">
              <thead>
                <tr>
                  <th>Unidade Curricular</th>
                  <th>Tipo</th>
                  <th>Título & Autor</th>
                  <th>Edição PPC</th>
                  <th>Edição & Exemplares no Sophia (Garopaba)</th>
                </tr>
              </thead>
              <tbody id="tbodySumarioVariacoes">
                <!-- Dynamic JS -->
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

    <!-- TAB 0: DIAGNÓSTICO DE EMENTAS -->
    <div id="tab-diagnostico" class="tab-pane active">
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.2rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
          <div>
            <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:var(--accent-emerald); margin-bottom:0.2rem;">
              <i class="bi bi-kanban-fill me-1"></i> Painel Diagnóstico de Conformidade Normativa das 45 Ementas
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted);">
              Mapeamento de conformidade com a premissa de <strong>3 exemplares por título básico</strong> e <strong>1 por título complementar</strong>.
            </p>
          </div>
          <div style="display:flex; gap:0.5rem; flex-wrap:wrap;" id="filterButtonsContainer">
            <button class="btn-action btn-outline" style="font-size:0.78rem; padding:0.4rem 0.8rem;" onclick="setDiagFilter('ALL')">Todas (45)</button>
            <button class="btn-action btn-outline" style="font-size:0.78rem; padding:0.4rem 0.8rem; color:#fb7185; border-color:rgba(244,63,94,0.4);" onclick="setDiagFilter('CRITICA_BASICA')">🔴 Déficit Básica ({count_criticas})</button>
            <button class="btn-action btn-outline" style="font-size:0.78rem; padding:0.4rem 0.8rem; color:#fbbf24; border-color:rgba(245,158,11,0.4);" onclick="setDiagFilter('ATENCAO_COMPLEMENTAR')">🟡 Falta Complementar ({count_atencao_comp})</button>
            <button class="btn-action btn-outline" style="font-size:0.78rem; padding:0.4rem 0.8rem; color:#34d399; border-color:rgba(16,185,129,0.4);" onclick="setDiagFilter('CONFORME_100')">🟢 100% Conformes ({count_conformes})</button>
          </div>
        </div>
      </div>

      <div class="diag-grid" id="diagCardsGrid">
        <!-- Dynamic JS -->
      </div>
    </div>

    <!-- TAB 1: OBRAS AUSENTES -->
    <div id="tab-ausentes" class="tab-pane">
      <div class="table-container">
        <table class="custom-table" id="tableAusentes">
          <thead>
            <tr>
              <th style="width: 18%;">Unidade Curricular</th>
              <th style="width: 10%;">Tipo</th>
              <th style="width: 25%;">Título da Obra</th>
              <th style="width: 18%;">Autor Principal</th>
              <th style="width: 12%;">Meta Normativa</th>
              <th style="width: 17%;">Demanda de Compra</th>
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
              <th style="width: 38%;">Edição & Exemplares no Sophia (Garopaba)</th>
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
              <th style="width: 16%;">Autor Principal</th>
              <th style="width: 14%;">Exemplares vs Meta</th>
              <th style="width: 18%;">Situação no Acervo</th>
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
              <th style="width: 16%;">Unidade Curricular</th>
              <th style="width: 8%;">Tipo</th>
              <th style="width: 24%;">Título da Obra</th>
              <th style="width: 16%;">Autor Principal</th>
              <th style="width: 10%;">Exemplares</th>
              <th style="width: 12%;">Meta / Déficit</th>
              <th style="width: 14%;">Observação</th>
            </tr>
          </thead>
          <tbody id="tbodyTodas">
            <!-- Dynamic JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 6: CATÁLOGO GERAL SOPHIA -->
    <div id="tab-catalogo" class="tab-pane">
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.2rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
          <div>
            <h3 style="font-family:'Outfit', sans-serif; font-size:1.15rem; color:var(--accent-blue); margin-bottom:0.2rem;">
              <i class="bi bi-bookshelf me-1"></i> Catálogo Completo do Câmpus Garopaba (Sistema Sophia)
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted);">
              Inventário total de <strong>3.003 títulos</strong> e <strong>{total_exemplares_lib} exemplares físicos</strong> catalogados no acervo.
            </p>
          </div>
          <div style="display:flex; gap:0.6rem; align-items:center;">
            <span class="badge badge-sim" id="badge-total-catalogo">3003 Obras Listadas</span>
          </div>
        </div>
      </div>

      <div class="table-container">
        <table class="custom-table" id="tableCatalogo">
          <thead>
            <tr>
              <th style="width: 8%;">ID</th>
              <th style="width: 62%;">Referência Bibliográfica Completa (ABNT NBR 6023)</th>
              <th style="width: 15%;">Exemplares no Câmpus</th>
              <th style="width: 15%;">Vínculo com PPC</th>
            </tr>
          </thead>
          <tbody id="tbodyCatalogo">
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
    const diagData = {json_diag_data};
    const catalogData = {json_catalog_data};

    let activeTabId = 'tab-diagnostico';

    function switchTab(tabId) {{
      activeTabId = tabId;
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      
      const targetPane = document.getElementById(tabId);
      if (targetPane) targetPane.classList.add('active');

      const targetBtn = document.querySelector(`.tab-btn[onclick*="${{tabId}}"]`);
      if (targetBtn) targetBtn.classList.add('active');
      
      if (tabId === 'tab-catalogo') {{
        renderCatalogo(catalogData);
      }}
      window.scrollTo({{ top: 320, behavior: 'smooth' }});
    }}

    function filterDiagBy(statusCode) {{
      switchTab('tab-diagnostico');
      document.getElementById('filterStatusEmenta').value = statusCode;
      applyFilters();
    }}

    function setDiagFilter(statusCode) {{
      document.getElementById('filterStatusEmenta').value = statusCode;
      applyFilters();
    }}

    function renderDiagnosticCards(data) {{
      const container = document.getElementById('diagCardsGrid');
      
      if (data.length === 0) {{
        container.innerHTML = '<p style="grid-column: 1/-1; text-align:center; padding:3rem; color:var(--text-muted); font-size:1.05rem;">Nenhuma ementa encontrada para os filtros selecionados.</p>';
        return;
      }}

      container.innerHTML = data.map(u => {{
        let cardClass = 'diag-card-conforme';
        if (u.status_code === 'CRITICA_BASICA') cardClass = 'diag-card-critica';
        else if (u.status_code === 'ATENCAO_COMPLEMENTAR') cardClass = 'diag-card-atencao';
        else if (u.status_code === 'ATENCAO_EDICAO') cardClass = 'diag-card-edicao';

        const missingBasicHtml = u.b_missing_books && u.b_missing_books.length > 0 ? `
          <div class="diag-missing-box">
            <strong><i class="bi bi-cart-plus-fill me-1"></i> Faltam ${{u.b_nao}} Obra(s) na Básica (Déficit de ${{u.b_deficit}} ex.):</strong>
            <ul class="diag-missing-list">
              ${{u.b_missing_books.map(b => `
                <li>• <strong>${{b.Titulo_Obra}}</strong> (${{b.Autor_Principal || 'Institucional'}} ${{b.Edicao_PPC ? b.Edicao_PPC + 'ª ed.' : ''}} ${{b.Ano_PPC || ''}}) <span class="badge badge-nao" style="font-size:0.7rem; padding:0.15rem 0.4rem;">+3 ex.</span></li>
              `).join('')}}
            </ul>
          </div>
        ` : '';

        const lowCopiesHtml = u.b_low_copies && u.b_low_copies.length > 0 ? `
          <div style="background:rgba(245,158,11,0.08); border:1px dashed rgba(245,158,11,0.3); border-radius:8px; padding:0.6rem; margin-bottom:0.8rem; font-size:0.78rem;">
            <strong style="color:#fbbf24; display:block; margin-bottom:0.2rem;"><i class="bi bi-stack me-1"></i> Título Básico com Acervo Reduzido (&lt; 3 Exs.):</strong>
            <ul class="diag-missing-list" style="color:#f1f5f9;">
              ${{u.b_low_copies.map(b => `
                <li>• <strong>${{b.Titulo_Obra}}</strong> (Possui ${{b.Exemplares_Disponiveis}} ex. &rarr; <span style="color:#fbbf24; font-weight:700;">Comprar +${{b.Deficit_Exemplares_Compra}} ex.</span>)</li>
              `).join('')}}
            </ul>
          </div>
        ` : '';

        const missingCompHtml = u.c_missing_books && u.c_missing_books.length > 0 ? `
          <div style="background:rgba(245,158,11,0.08); border:1px dashed rgba(245,158,11,0.3); border-radius:8px; padding:0.6rem; margin-bottom:0.8rem; font-size:0.78rem;">
            <strong style="color:#fbbf24; display:block; margin-bottom:0.2rem;"><i class="bi bi-journal-x me-1"></i> Faltam ${{u.c_nao}} Obra(s) na Complementar (+${{u.c_deficit}} ex.):</strong>
            <ul class="diag-missing-list" style="color:var(--text-muted);">
              ${{u.c_missing_books.slice(0, 2).map(b => `
                <li>• ${{b.Titulo_Obra}} (${{b.Autor_Principal || 'Institucional'}})</li>
              `).join('')}}
              ${{u.c_missing_books.length > 2 ? `<li style="font-style:italic;">+ mais ${{u.c_missing_books.length - 2}} obra(s)...</li>` : ''}}
            </ul>
          </div>
        ` : '';

        return `
          <div class="diag-card ${{cardClass}}">
            <div>
              <div class="diag-card-header">
                <div>
                  <span class="badge badge-basica font-code" style="margin-bottom:4px;">UC ${{u.uc_id}}</span>
                  <div class="diag-uc-title">${{u.uc_nome}}</div>
                  <div class="diag-uc-meta">${{u.bloco}} • ${{u.semestre}}</div>
                </div>
                <span class="badge ${{u.status_badge}}">
                  <i class="bi ${{u.status_icon}}"></i> ${{u.status_label}}
                </span>
              </div>

              <div class="diag-stats-row">
                <div>
                  <span style="color:var(--text-muted); display:block; font-size:0.72rem; text-transform:uppercase;">Títulos Básicos:</span> 
                  <strong style="color:${{u.b_nao === 0 ? '#34d399' : '#fb7185'}}; font-size:0.92rem;">${{u.b_sim}} de ${{u.b_total}} títulos (${{u.pct_basica}}%)</strong>
                </div>
                <div>
                  <span style="color:var(--text-muted); display:block; font-size:0.72rem; text-transform:uppercase;">Demanda de Compras:</span> 
                  <strong style="color:${{u.total_deficit === 0 ? '#34d399' : '#fb7185'}}; font-size:0.92rem;">${{u.total_deficit === 0 ? 'Conforme (0 ex.)' : '+' + u.total_deficit + ' exemplares'}}</strong>
                </div>
              </div>

              ${{missingBasicHtml}}
              ${{lowCopiesHtml}}
              ${{missingCompHtml}}
            </div>

            <div class="diag-action-box">
              <i class="bi bi-lightbulb-fill text-amber"></i>
              <span><strong>Ação:</strong> ${{u.acao_sugerida}}</span>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function renderCatalogo(data) {{
      const query = document.getElementById('searchInput').value.toLowerCase();
      let filtered = data;
      if (query) {{
        filtered = filtered.filter(item => item.ref.toLowerCase().includes(query));
      }}

      document.getElementById('badge-total-catalogo').innerText = `${{filtered.length}} Obras Encontradas`;

      const tbody = document.getElementById('tbodyCatalogo');
      const displayItems = filtered.slice(0, 250);

      tbody.innerHTML = displayItems.map(item => `
        <tr>
          <td><span class="badge font-code" style="background:rgba(255,255,255,0.06);">${{item.id}}</span></td>
          <td style="font-size:0.86rem; line-height:1.45;">${{item.ref}}</td>
          <td>
            <span class="badge ${{item.exemplares >= 3 ? 'badge-sim' : (item.exemplares === 2 ? 'badge-var' : 'badge-fnde')}}">
              <i class="bi bi-stack"></i> ${{item.exemplares}} ${{item.exemplares > 1 ? 'Exemplares' : 'Exemplar'}}
            </span>
          </td>
          <td>
            ${{item.is_ppc ? '<span class="badge badge-ppc-tag"><i class="bi bi-bookmark-check-fill"></i> No PPC ADM</span>' : '<span style="color:var(--text-muted); font-size:0.75rem;">Geral Acervo</span>'}}
          </td>
        </tr>
      `).join('') + (filtered.length > 250 ? `<tr><td colspan="4" style="text-align:center; padding:1.2rem; color:var(--text-muted); font-weight:600;">Exibindo os primeiros 250 resultados de ${{filtered.length}} obras. Refine a pesquisa para filtrar títulos específicos.</td></tr>` : '');
    }}

    function renderTables(data, filteredDiag) {{
      renderDiagnosticCards(filteredDiag);

      // 0. Sumário Executivo Tables
      const tbodySumarioBasica = document.getElementById('tbodySumarioBasica');
      if (tbodySumarioBasica) {{
        const ausentesBasica = data.filter(d => d.Tipo_Bibliografia === 'Básica' && d.Existe_Biblioteca === 'NÃO');
        tbodySumarioBasica.innerHTML = ausentesBasica.map(d => `
          <tr>
            <td><strong>${{d.UC_Nome}}</strong></td>
            <td>${{d.Autor_Principal || 'Institucional'}}</td>
            <td><strong>${{d.Titulo_Obra}}</strong></td>
            <td><span class="badge badge-var">${{d.Edicao_PPC ? d.Edicao_PPC + 'ª ed.' : ''}} ${{d.Ano_PPC || ''}}</span></td>
            <td><span class="badge badge-nao"><i class="bi bi-cart-plus-fill"></i> +3 ex. Físicos</span></td>
          </tr>
        `).join('');
      }}

      const tbodySumarioVariacoes = document.getElementById('tbodySumarioVariacoes');
      if (tbodySumarioVariacoes) {{
        const variacoes = data.filter(d => d.Status === 'EXISTE_EDICAO_DIFERENTE');
        tbodySumarioVariacoes.innerHTML = variacoes.map(d => `
          <tr>
            <td><strong>${{d.UC_Nome}}</strong></td>
            <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
            <td><strong>${{d.Titulo_Obra}}</strong><br><small style="color:var(--text-muted)">${{d.Autor_Principal}}</small></td>
            <td><span class="badge badge-var">${{d.Edicao_PPC ? d.Edicao_PPC + 'ª ed.' : ''}} ${{d.Ano_PPC || ''}}</span></td>
            <td>
              <div style="font-size:0.82rem; line-height:1.4;">
                <span class="badge badge-sim" style="margin-bottom:2px;"><i class="bi bi-stack"></i> ${{d.Exemplares_Disponiveis || 1}} ex. no Sophia</span><br>
                ${{d.Referencia_Acervo_Sophia}}
              </div>
            </td>
          </tr>
        `).join('');
      }}

      // 1. Ausentes
      const tbodyAusentes = document.getElementById('tbodyAusentes');
      const ausentes = data.filter(d => d.Existe_Biblioteca === 'NÃO');

      tbodyAusentes.innerHTML = ausentes.map(d => `
        <tr>
          <td><strong>${{d.UC_Nome}}</strong><br><small style="color:var(--text-muted)">${{d.Bloco_Formacao}} • ${{d.Ano_Semestre}}</small></td>
          <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
          <td><strong>${{d.Titulo_Obra}}</strong></td>
          <td>${{d.Autor_Principal || 'Institucional'}}</td>
          <td><span class="badge badge-var">${{d.Meta_Normativa_Exemplares}} ex. recomendados</span></td>
          <td>
            <span class="badge badge-nao">
              <i class="bi bi-cart-plus"></i> Comprar +${{d.Deficit_Exemplares_Compra}} ex.
            </span>
          </td>
        </tr>
      `).join('');

      // 2. Variações
      const tbodyVariacoes = document.getElementById('tbodyVariacoes');
      const variacoes = data.filter(d => d.Status === 'EXISTE_EDICAO_DIFERENTE');

      tbodyVariacoes.innerHTML = variacoes.map(d => `
        <tr>
          <td><strong>${{d.UC_Nome}}</strong></td>
          <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
          <td><strong>${{d.Titulo_Obra}}</strong><br><small style="color:var(--text-muted)">${{d.Autor_Principal}}</small></td>
          <td><span class="badge badge-var">${{d.Edicao_PPC ? d.Edicao_PPC + 'ª ed.' : ''}} ${{d.Ano_PPC || ''}}</span></td>
          <td>
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:4px;">
              <span class="badge badge-sim"><i class="bi bi-stack"></i> ${{d.Exemplares_Disponiveis || 1}} ex. no Câmpus</span>
              <span class="badge ${{d.Deficit_Exemplares_Compra === 0 ? 'badge-sim' : 'badge-var'}}">${{d.Deficit_Exemplares_Compra === 0 ? 'Meta Atendida' : 'Faltam +' + d.Deficit_Exemplares_Compra + ' ex.'}}</span>
            </div>
            <div style="font-size:0.82rem; line-height:1.4;">${{d.Referencia_Acervo_Sophia}}</div>
          </td>
        </tr>
      `).join('');

      // 3. Existentes
      const tbodyExistentes = document.getElementById('tbodyExistentes');
      const existentes = data.filter(d => d.Existe_Biblioteca === 'SIM');

      tbodyExistentes.innerHTML = existentes.map(d => {{
        const exCount = d.Exemplares_Disponiveis;
        const exBadge = d.Status === 'MATERIAL_FNDE' 
          ? '<span class="badge badge-fnde"><i class="bi bi-person-fill"></i> PNLD (1/Aluno)</span>'
          : `<span class="badge badge-sim"><i class="bi bi-stack"></i> ${{exCount || 1}} ${{exCount > 1 ? 'Exs.' : 'Ex.'}} (Meta: ${{d.Meta_Normativa_Exemplares}})</span>`;

        return `
          <tr>
            <td><strong>${{d.UC_Nome}}</strong></td>
            <td><span class="badge ${{d.Tipo_Bibliografia === 'Básica' ? 'badge-basica' : 'badge-comp'}}">${{d.Tipo_Bibliografia}}</span></td>
            <td><strong>${{d.Titulo_Obra}}</strong></td>
            <td>${{d.Autor_Principal}}</td>
            <td>${{exBadge}}</td>
            <td>
              <span class="badge ${{d.Deficit_Exemplares_Compra === 0 ? 'badge-sim' : 'badge-var'}}">
                ${{d.Status_Normativo}}
              </span>
            </td>
          </tr>
        `;
      }}).join('');

      // 4. Todas
      const tbodyTodas = document.getElementById('tbodyTodas');
      tbodyTodas.innerHTML = data.map(d => {{
        const exCount = d.Exemplares_Disponiveis;
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
              <span class="badge ${{d.Deficit_Exemplares_Compra === 0 ? 'badge-sim' : 'badge-nao'}}">
                ${{d.Deficit_Exemplares_Compra === 0 ? 'Conforme' : 'Déficit +' + d.Deficit_Exemplares_Compra + ' ex.'}}
              </span>
            </td>
            <td><small style="color:var(--text-muted)">${{d.Observacao_Tecnica}}</small></td>
          </tr>
        `;
      }}).join('');

      // 5. UCs Accordion
      renderUCAccordion(data);
      renderCatalogo(catalogData);
    }}

    function renderUCAccordion(filteredData) {{
      const container = document.getElementById('accordionUCs');
      
      const html = diagData.map(uc => {{
        const ucRefs = filteredData.filter(d => d.UC_ID === uc.uc_id);
        if (ucRefs.length === 0) return '';
        
        const simCount = ucRefs.filter(d => d.Existe_Biblioteca === 'SIM').length;
        const totalCount = ucRefs.length;
        const pct = Math.round((simCount / totalCount) * 100);

        return `
          <div class="uc-card" id="uc-card-${{uc.uc_id}}">
            <div class="uc-card-header" onclick="toggleUC(${{uc.uc_id}})">
              <div style="display:flex; align-items:center; gap:0.8rem;">
                <span class="badge badge-basica font-code">UC ${{uc.uc_id}}</span>
                <div>
                  <strong style="font-size:1rem; color:#ffffff;">${{uc.uc_nome}}</strong>
                  <div style="font-size:0.8rem; color:var(--text-muted);">${{uc.bloco}} • ${{uc.semestre}}</div>
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
                <i class="bi bi-chevron-down" id="uc-icon-${{uc.uc_id}}"></i>
              </div>
            </div>

            <div class="uc-card-body" id="uc-body-${{uc.uc_id}}">
              <table class="custom-table" style="font-size:0.84rem;">
                <thead>
                  <tr>
                    <th>Tipo</th>
                    <th>Título & Autor</th>
                    <th>Exemplares vs Meta</th>
                    <th>Situação Normativa</th>
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
                          ${{r.Status === 'MATERIAL_FNDE' ? 'PNLD' : (r.Exemplares_Disponiveis + ' de ' + r.Meta_Normativa_Exemplares + ' ex.')}}
                        </span>
                      </td>
                      <td>
                        <span class="badge ${{r.Deficit_Exemplares_Compra === 0 ? 'badge-sim' : 'badge-nao'}}">
                          ${{r.Status_Normativo}}
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
      const statusEmenta = document.getElementById('filterStatusEmenta').value;
      const bloco = document.getElementById('filterBloco').value;

      // Filter Diagnostic UCs
      const filteredDiag = diagData.filter(u => {{
        const matchQuery = !query || 
          u.uc_nome.toLowerCase().includes(query) ||
          u.bloco.toLowerCase().includes(query) ||
          (u.b_missing_books && u.b_missing_books.some(b => b.Titulo_Obra.toLowerCase().includes(query))) ||
          (u.c_missing_books && u.c_missing_books.some(b => b.Titulo_Obra.toLowerCase().includes(query)));

        let matchStatus = true;
        if (statusEmenta === 'COM_PROBLEMA') {{
          matchStatus = u.status_code !== 'CONFORME_100';
        }} else if (statusEmenta !== 'ALL') {{
          matchStatus = u.status_code === statusEmenta;
        }}

        const matchBloco = (bloco === 'ALL') || (u.bloco && u.bloco.includes(bloco));

        return matchQuery && matchStatus && matchBloco;
      }});

      // Filter All References
      const filteredAll = allData.filter(d => {{
        const matchQuery = !query || 
          (d.Titulo_Obra && d.Titulo_Obra.toLowerCase().includes(query)) ||
          (d.Autor_Principal && d.Autor_Principal.toLowerCase().includes(query)) ||
          (d.UC_Nome && d.UC_Nome.toLowerCase().includes(query)) ||
          (d.Referencia_PPC && d.Referencia_PPC.toLowerCase().includes(query));

        const matchBloco = (bloco === 'ALL') || (d.Bloco_Formacao && d.Bloco_Formacao.includes(bloco));

        return matchQuery && matchBloco;
      }});

      renderTables(filteredAll, filteredDiag);
    }}

    function resetFilters() {{
      document.getElementById('searchInput').value = '';
      document.getElementById('filterStatusEmenta').value = 'ALL';
      document.getElementById('filterBloco').value = 'ALL';
      renderTables(allData, diagData);
    }}

    // Initial render
    document.addEventListener('DOMContentLoaded', () => {{
      renderTables(allData, diagData);
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
    
    {\LARGE \textbf{\textcolor{ifscgreen}{Relatório Técnico de Auditoria Normativa do Acervo}}}\\[4pt]
    {\large \textbf{Projeto Pedagógico de Curso -- Técnico em Administração Integrado (PPC 2026)}}\\[6pt]
    {\small \textbf{Destinatário:} Bibliotecário David / Equipe da Biblioteca \quad \textbullet{} \quad \textbf{Data:} 28 de Agosto de 2026}
\end{center}

\vspace{0.2cm}
\hrule height 1.2pt \relax
\vspace{0.3cm}

\section{Premissas Normativas da Auditoria}
O presente relatório consolida a auditoria bibliográfica do PPC Técnico em Administração Integrado do IFSC Câmpus Garopaba aplicando a premissa de quantitativos mínimos do IFSC:
\begin{itemize}[leftmargin=*,noitemsep]
    \item \textbf{Bibliografia Básica:} Mínimo de 2 títulos por UC, devendo o acervo do câmpus disponibilizar \textbf{ao menos 3 exemplares físicos de cada título} (ou livro didático PNLD/FNDE).
    \item \textbf{Bibliografia Complementar:} Mínimo de 3 títulos por UC, devendo o acervo do câmpus disponibilizar \textbf{ao menos 1 exemplar físico de cada título}.
\end{itemize}

\section{Indicadores Gerais de Cobertura e Demanda de Aquisição}

\begin{table}[H]
\centering
\small
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Indicador / Métrica Normativa}} & \textcolor{white}{\textbf{Quantidade}} & \textcolor{white}{\textbf{Percentual / Meta}} \\ \hline
\rowcolor{cinzaClaro}
Total de Unidades Curriculares (UCs) Auditadas & 45 UCs & 100,0\% \\ \hline
Total Geral de Títulos no PPC & 272 títulos & 100,0\% \\ \hline
\rowcolor{cinzaClaro}
• Títulos de Bibliografia Básica (Meta: $\ge$ 2 por UC) & 122 títulos & 44,9\% \\ \hline
• Títulos de Bibliografia Complementar (Meta: $\ge$ 3 por UC) & 150 títulos & 55,1\% \\ \hline
\rowcolor{ifsclightgreen}
\textbf{Títulos EXISTENTES na Biblioteca (Físico / PNLD)} & \textbf{200 títulos} & \textbf{73,5\%} \\ \hline
\rowcolor{ifsclightgreen}
\textbf{• Cobertura de Títulos na Bibliografia Básica} & \textbf{97 títulos} & \textbf{79,5\%} \\ \hline
\rowcolor{ifsclightgreen}
• Cobertura de Títulos na Bibliografia Complementar & 103 títulos & 68,7\% \\ \hline
\rowcolor{cinzaClaro}
\textbf{DEMANDA DE AQUISIÇÃO DE EXEMPLARES FÍSICOS} & \textbf{Cópias Físicas} & \textbf{Meta por Título} \\ \hline
\rowcolor{cinzaClaro}
• Cópias a Adquirir para a Bibliografia BÁSICA & 99 exemplares & Meta: 3 ex. / título básico \\ \hline
• Cópias a Adquirir para a Bibliografia COMPLEMENTAR & 47 exemplares & Meta: 1 ex. / título comp. \\ \hline
\rowcolor{ifsclightgreen}
\textbf{TOTAL GERAL DE EXEMPLARES FÍSICOS A COMPRAR} & \textbf{146 exemplares} & \textbf{100\% de Conformidade} \\ \hline
\end{tabularx}
\caption{Quadro Resumo de Cobertura e Demanda de Compras}
\end{table}

\section{Prioridade 1: Obras da Bibliografia BÁSICA para Aquisição (Meta: 3 Exs.)}
Relação de obras básicas com necessidade de aquisição (3 exemplares por título) ou validação nas plataformas virtuais (\textit{Minha Biblioteca / Pearson}):

\vspace{0.2cm}
\begin{xltabular}{\linewidth}{|p{3.8cm}|p{3.2cm}|X|p{2.2cm}|}
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Autor Principal}} & \textcolor{white}{\textbf{Título da Obra}} & \textcolor{white}{\textbf{Demanda}} \\ \hline
\endfirsthead
\hline
\rowcolor{ifscgreen}
\textcolor{white}{\textbf{Unidade Curricular}} & \textcolor{white}{\textbf{Autor Principal}} & \textcolor{white}{\textbf{Título da Obra}} & \textcolor{white}{\textbf{Demanda}} \\ \hline
\endhead
"""

    for _, row in df_nao_b.iterrows():
        uc_t = escape_tex(row['UC_Nome'])
        aut_t = escape_tex(str(row['Autor_Principal'])[:35]) if str(row['Autor_Principal']).strip() else 'Institucional / MEC'
        tit_t = escape_tex(str(row['Titulo_Obra'])[:45])
        tex_content += f"{uc_t} & {aut_t} & \\textbf{{{tit_t}}} & +3 ex. Físicos \\\\ \\hline\n"

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
            Auditoria Normativa do Acervo & Diagnóstico de Ementas (PPC vs. Sophia)
          </div>
          <div style="display: flex; gap: 0.8rem;">
            <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/dashboard_biblioteca.html" target="_blank" class="btn-action btn-emerald">
              <i class="bi bi-window-fullscreen"></i> Abrir Painel Diagnóstico de Ementas
            </a>
            <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/relatorio_auditoria_biblioteca.pdf" target="_blank" class="btn-action btn-outline">
              <i class="bi bi-file-earmark-pdf-fill"></i> Baixar Relatório PDF (David)
            </a>
          </div>
        </div>

        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
          Cruzamento automatizado entre todas as <strong>272 referências bibliográficas</strong> adotadas no PPC do Técnico em Administração e o inventário oficial de <strong>3.003 títulos</strong> e <strong>4.962 exemplares físicos</strong> do Sistema Sophia da Biblioteca do Câmpus Garopaba, aplicando a regra de <strong>3 ex. na Básica</strong> e <strong>1 ex. na Complementar</strong>.
        </p>

        <div class="grid-2">
          <div>
            <h3 style="color: var(--accent-emerald); font-size: 1.1rem; margin-bottom: 1rem; font-family: 'Outfit', sans-serif;">
              <i class="bi bi-bar-chart-fill me-1"></i> Indicadores Normativos & Demanda de Compras:
            </h3>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(244,63,94,0.2); color:var(--accent-rose);"><i class="bi bi-cart-plus-fill"></i></div>
              <div class="step-content">
                <h4>Demanda de Compras da Básica: +99 exemplares</h4>
                <p>Necessários para assegurar 3 exemplares físicos de cada título básico no câmpus.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(16,185,129,0.2); color:var(--accent-emerald);"><i class="bi bi-check-circle-fill"></i></div>
              <div class="step-content">
                <h4>79,5% dos Títulos Básicos já Atendidos</h4>
                <p>97 de 122 títulos da bibliografia básica já estão disponíveis no acervo do câmpus ou PNLD.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-icon" style="background:rgba(56,189,248,0.2); color:var(--accent-blue);"><i class="bi bi-pie-chart-fill"></i></div>
              <div class="step-content">
                <h4>4.962 Exemplares Físicos no Câmpus Garopaba</h4>
                <p>Catálogo completo de 3.003 títulos consultável no painel com contagem de cópias por obra.</p>
              </div>
            </div>
          </div>

          <div>
            <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-bottom: 1rem; font-family: 'Outfit', sans-serif;">
              <i class="bi bi-file-earmark-spreadsheet-fill me-1"></i> Documentos & Artefatos Disponíveis:
            </h3>

            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.2rem; display: flex; flex-direction: column; gap: 0.8rem;">
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/dashboard_biblioteca.html" target="_blank" style="color:var(--accent-emerald); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-box-arrow-up-right"></i> Painel Diagnóstico de Ementas & Acervo da Biblioteca
              </a>
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/relatorio_auditoria_biblioteca.pdf" target="_blank" style="color:var(--accent-blue); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-file-earmark-pdf"></i> Relatório Oficial de Auditoria em PDF (Formatado em LaTeX)
              </a>
              <a href="tecnico-administracao/revisao-equipe/checagem-biblioteca/Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx" download style="color:var(--accent-amber); text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">
                <i class="bi bi-file-earmark-excel"></i> Planilha Consolidada de Auditoria com Contagem de Exemplares (.xlsx)
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
    df_all, df_resumo, df_uc, all_library_items, uc_diagnostics = load_data()
    generate_interactive_html(df_all, df_resumo, df_uc, all_library_items, uc_diagnostics)
    generate_latex_pdf_report(df_all, df_resumo, df_uc)
    update_root_dashboard()
    print("Todas as tarefas concluídas com sucesso!")

if __name__ == "__main__":
    main()
