#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auditoria Bibliográfica & Análise Normativa de Quantitativos de Acervo
PPC Técnico em Administração Integrado (IFSC Garopaba) vs. Catálogo Sophia (Acervo e exemplares.XLS).

Premissa Normativa Institucional do IFSC:
1. Bibliografia Básica: Mínimo de 2 títulos por UC; cada título deve dispor de ao menos 3 exemplares físicos no acervo do câmpus (ou livro PNLD).
2. Bibliografia Complementar: Mínimo de 3 títulos por UC; cada título deve dispor de ao menos 1 exemplar físico no acervo do câmpus.
"""

import os
import re
import unicodedata
from collections import defaultdict
import pandas as pd
from difflib import SequenceMatcher

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/tecnico-administracao"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
MD_PATH = os.path.join(BASE_DIR, "todas_ementas_administracao.md")
ACERVO_EXEMPLARES_PATH = os.path.join(CHECK_DIR, "Acervo e exemplares.XLS")
ACERVO_ABNT_PATH = os.path.join(CHECK_DIR, "Acervo ABNT.XLS")

STOPWORDS = {
    "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "da", "do", "das", "dos",
    "em", "na", "no", "nas", "nos", "por", "para", "com", "sem", "e", "ou", "se",
    "ed", "edicao", "vol", "volume", "editora", "traducao", "reimpressao", "p", "paginas",
    "sobre", "como", "ao", "aos", "pelos", "pelas", "isbn", "inclui", "bibliografia", "il", "color"
}

def normalize_str(text):
    if not text:
        return ""
    text = unicodedata.normalize("NFKD", str(text)).encode("ASCII", "ignore").decode("ASCII").lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def get_keywords(text):
    words = normalize_str(text).split()
    return [w for w in words if len(w) > 2 and w not in STOPWORDS]

def is_title_match(t_ppc, t_cand):
    norm_p = normalize_str(t_ppc)
    norm_c = normalize_str(t_cand)
    if not norm_p or not norm_c:
        return False
    if norm_p == norm_c or norm_p in norm_c or norm_c in norm_p:
        shared_len = min(len(norm_p), len(norm_c))
        if shared_len >= 8:
            return True
            
    k_p = set(get_keywords(t_ppc))
    k_c = set(get_keywords(t_cand))
    if not k_p or not k_c:
        return False
        
    jaccard = len(k_p.intersection(k_c)) / len(k_p.union(k_c))
    overlap = len(k_p.intersection(k_c)) / len(k_p)
    ratio = SequenceMatcher(None, norm_p, norm_c).ratio()
    
    return (jaccard >= 0.60 and overlap >= 0.75) or ratio >= 0.75

def extract_metadata(ref_text):
    cleaned = ref_text.replace("**", "").strip()
    
    # Generic PNLD/FNDE check
    if any(k in cleaned for k in ["LIVRO didático fornecido", "Material didático fornecido", "Fundo Nacional de Desenvolvimento"]):
        return {
            "autor": "FNDE / MEC (PNLD)",
            "primeiro_autor": "fnde",
            "primeiro_autor_raw": "FNDE / MEC",
            "titulo": cleaned,
            "titulo_curto": "Livro didático FNDE (PNLD)",
            "edicao": "",
            "ano": "",
            "isbn": "",
            "is_generic": True,
            "is_authorless": True
        }
    
    # ISBN
    isbn_match = re.search(r'ISBN\s*([\d\-xX]+)', cleaned)
    isbn = re.sub(r'[^\dxX]', '', isbn_match.group(1)) if isbn_match else ""
    
    # Year
    year_match = re.search(r'\b(19\d\d|20[0-2]\d)\b', cleaned)
    ano = year_match.group(1) if year_match else ""
    
    # Edition
    ed_match = re.search(r'(\d+)\.\s*ed\b', cleaned, re.IGNORECASE)
    edicao = ed_match.group(1) if ed_match else ""
    
    # Author & Title
    md_title_match = re.search(r'\*\*([^*]+)\*\*', ref_text)
    if md_title_match:
        titulo = md_title_match.group(1).strip()
        autor_part = ref_text.split('**')[0].strip().rstrip('.')
    else:
        parts = cleaned.split('.')
        autor_part = parts[0].strip() if len(parts) > 0 else ""
        titulo = parts[1].strip() if len(parts) > 1 else cleaned
        
    autor_clean = re.sub(r'\(org\.\)|\(coord\.\)|\(org\)|\(orgs\.\)|\(Coautor\)', '', autor_part).strip()
    first_author_raw = autor_clean.split(';')[0].split(',')[0].strip() if autor_clean else ""
    first_author = normalize_str(first_author_raw)
    
    is_authorless = False
    if not autor_clean or first_author in ["dicionario", "enciclopedia", "brasil", "ifsc", "manual", "guia", "livro"]:
        is_authorless = True
        
    titulo_curto = titulo.split(':')[0].strip()
    
    return {
        "autor": autor_clean if autor_clean else "Obra Institucional / Sem Autor Específico",
        "primeiro_autor": first_author,
        "primeiro_autor_raw": first_author_raw,
        "titulo": titulo,
        "titulo_curto": titulo_curto,
        "edicao": edicao,
        "ano": ano,
        "isbn": isbn,
        "is_generic": False,
        "is_authorless": is_authorless
    }

class AcervoIndex:
    def __init__(self, items):
        self.items = items
        self.isbn_map = {}
        self.author_map = defaultdict(list)
        self.word_map = defaultdict(list)
        
        for idx, item in enumerate(items):
            meta = item["meta"]
            if meta["isbn"]:
                self.isbn_map[meta["isbn"]] = idx
            
            author = meta["primeiro_autor"]
            if author and len(author) >= 3:
                self.author_map[author].append(idx)
            
            title_words = get_keywords(meta["titulo"])
            for w in title_words:
                self.word_map[w].append(idx)

    def find_candidates(self, meta):
        candidate_indices = set()
        
        if meta["isbn"] and meta["isbn"] in self.isbn_map:
            candidate_indices.add(self.isbn_map[meta["isbn"]])
            
        author = meta["primeiro_autor"]
        if author and not meta["is_authorless"]:
            if author in self.author_map:
                candidate_indices.update(self.author_map[author])
            else:
                for a_key, idxs in self.author_map.items():
                    if len(author) >= 4 and (author in a_key or a_key in author):
                        candidate_indices.update(idxs)
                    
        words = get_keywords(meta["titulo_curto"])
        if words:
            word_counts = defaultdict(int)
            for w in words:
                for idx in self.word_map.get(w, []):
                    word_counts[idx] += 1
            threshold = 1 if len(words) <= 2 else 2
            for idx, count in word_counts.items():
                if count >= threshold:
                    candidate_indices.add(idx)
                    
        return [self.items[i] for i in candidate_indices]

def load_and_index_acervo():
    target_path = ACERVO_EXEMPLARES_PATH if os.path.exists(ACERVO_EXEMPLARES_PATH) else ACERVO_ABNT_PATH
    df = pd.read_excel(target_path)
    col = df.columns[1]
    raw_list = df[col].dropna().tolist()
    
    acervo_items = []
    for raw in raw_list:
        text = str(raw).strip()
        if not text or text.startswith('Referência bibliográfica') or text.startswith('(Ordenadas') or text == 'IFSC - Câmpus Garopaba' or re.match(r'^\d{2}/\d{2}/\d{4}$', text):
            continue
        if text.startswith('Total:') or ('IFSC - Garopaba - ' in text and len(text) < 40 and not 'ISBN' in text):
            continue
            
        exemplares = 1
        m = re.search(r'Exemplares:\s*IFSC\s*-\s*Garopaba\s*-\s*(\d+)\s*Ex', text)
        if m:
            exemplares = int(m.group(1))
        else:
            m2 = re.search(r'Total\s*-\s*(\d+)\s*Ex', text)
            if m2:
                exemplares = int(m2.group(1))
                
        ref_text_clean = re.sub(r'Exemplares:.*$', '', text).strip()
        meta = extract_metadata(ref_text_clean)
        acervo_items.append({
            "raw": ref_text_clean,
            "raw_with_exemplares": text,
            "norm": normalize_str(ref_text_clean),
            "exemplares": exemplares,
            "meta": meta
        })
        
    return AcervoIndex(acervo_items), acervo_items

def parse_ppc_md():
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
            "basica": bb_items,
            "complementar": bc_items
        })
    return ucs

def match_single_reference(ref_raw, meta, index_obj, all_acervo, tipo_ref):
    # Meta Normativa do IFSC
    meta_exemplares = 3 if tipo_ref == "Básica" else 1

    if meta.get("is_generic"):
        return {
            "status": "MATERIAL_FNDE",
            "status_label": "Material PNLD/FNDE (MEC)",
            "score": 100,
            "exemplares": 1,
            "exemplares_label": "PNLD (1/Aluno)",
            "meta_exemplares": meta_exemplares,
            "deficit_exemplares": 0,
            "status_normativo": "CONFORME (PNLD)",
            "acervo_item": "Material didático oficial distribuído pelo FNDE / MEC a cada estudante",
            "obs": "Disponibilizado aos estudantes via Programa Nacional do Livro Didático (PNLD)"
        }
    
    # 1. Exact ISBN Match
    if meta["isbn"] and meta["isbn"] in index_obj.isbn_map:
        matched_item = index_obj.items[index_obj.isbn_map[meta["isbn"]]]
        ex_count = matched_item["exemplares"]
        deficit = max(0, meta_exemplares - ex_count)
        status_norm = "CONFORME" if deficit == 0 else f"DÉFICIT DE {deficit} EX."
        
        return {
            "status": "EXISTE_NO_ACERVO",
            "status_label": "Existe no Acervo (Confirmado por ISBN)",
            "score": 100,
            "exemplares": ex_count,
            "exemplares_label": f"{ex_count} ex.",
            "meta_exemplares": meta_exemplares,
            "deficit_exemplares": deficit,
            "status_normativo": status_norm,
            "acervo_item": matched_item["raw"],
            "obs": f"Disponível no acervo ({ex_count} ex.). Meta normativa: {meta_exemplares} ex. Faltam comprar: {deficit} ex."
        }
        
    candidates = index_obj.find_candidates(meta)
    
    norm_author = meta["primeiro_autor"]
    is_authorless = meta["is_authorless"]
    
    best_candidate = None
    best_score = 0
    best_type = None
    
    for cand in candidates:
        cand_meta = cand["meta"]
        cand_norm = cand["norm"]
        cand_author = cand_meta["primeiro_autor"]
        
        same_author = False
        if is_authorless:
            same_author = True
        elif norm_author:
            if norm_author == cand_author or (len(norm_author) >= 4 and norm_author in cand_norm):
                same_author = True
                
        if not same_author and not is_authorless:
            continue
            
        if is_title_match(meta["titulo"], cand_meta["titulo"]) or is_title_match(meta["titulo_curto"], cand_meta["titulo_curto"]):
            same_ed = (meta["edicao"] == cand_meta["edicao"]) if meta["edicao"] and cand_meta["edicao"] else True
            same_yr = (meta["ano"] == cand_meta["ano"]) if meta["ano"] and cand_meta["ano"] else True
            
            score = 95 if (same_ed and same_yr) else 85
            if score > best_score:
                best_score = score
                best_candidate = cand
                best_type = "EXISTE_NO_ACERVO" if (same_ed and same_yr) else "EXISTE_EDICAO_DIFERENTE"
                
    if best_candidate:
        ex_count = best_candidate["exemplares"]
        deficit = max(0, meta_exemplares - ex_count)
        status_norm = "CONFORME" if deficit == 0 else f"DÉFICIT DE {deficit} EX."

        if best_type == "EXISTE_NO_ACERVO":
            return {
                "status": "EXISTE_NO_ACERVO",
                "status_label": "Existe no Acervo (Confirmado)",
                "score": best_score,
                "exemplares": ex_count,
                "exemplares_label": f"{ex_count} ex.",
                "meta_exemplares": meta_exemplares,
                "deficit_exemplares": deficit,
                "status_normativo": status_norm,
                "acervo_item": best_candidate["raw"],
                "obs": f"Disponível no acervo ({ex_count} ex.). Meta normativa: {meta_exemplares} ex. Faltam comprar: {deficit} ex."
            }
        else:
            ppc_ed = f"{meta['edicao']}ª ed." if meta['edicao'] else (meta.get('ano') or 'N/D')
            acervo_ed = f"{best_candidate['meta']['edicao']}ª ed." if best_candidate['meta'].get('edicao') else (best_candidate['meta'].get('ano') or 'N/D')
            return {
                "status": "EXISTE_EDICAO_DIFERENTE",
                "status_label": "Existe no Acervo (Variação de Edição/Ano)",
                "score": best_score,
                "exemplares": ex_count,
                "exemplares_label": f"{ex_count} ex.",
                "meta_exemplares": meta_exemplares,
                "deficit_exemplares": deficit,
                "status_normativo": f"{status_norm} (Variação)",
                "acervo_item": best_candidate["raw"],
                "obs": f"PPC indica ({ppc_ed}); Acervo possui ({acervo_ed}, {ex_count} ex.). Meta: {meta_exemplares} ex. Faltam: {deficit} ex."
            }
            
    # Check if author has other works in acervo
    if norm_author and not is_authorless:
        author_items = [item for item in all_acervo if len(norm_author) >= 4 and norm_author in item["norm"]]
        if author_items:
            other_work = author_items[0]["raw"]
            return {
                "status": "NAO_EXISTE_AUTOR_PRESENTE",
                "status_label": "Não Existe no Acervo (Autor possui outras obras na biblioteca)",
                "score": 30,
                "exemplares": 0,
                "exemplares_label": "0 ex.",
                "meta_exemplares": meta_exemplares,
                "deficit_exemplares": meta_exemplares,
                "status_normativo": f"AUSENTE (Déficit de {meta_exemplares} ex.)",
                "acervo_item": other_work,
                "obs": f"Obra ausente. Meta: {meta_exemplares} ex. Faltam comprar: {meta_exemplares} ex."
            }
        
    return {
        "status": "NAO_EXISTE",
        "status_label": "Não Existe no Acervo (Ausente)",
        "score": 0,
        "exemplares": 0,
        "exemplares_label": "0 ex.",
        "meta_exemplares": meta_exemplares,
        "deficit_exemplares": meta_exemplares,
        "status_normativo": f"AUSENTE (Déficit de {meta_exemplares} ex.)",
        "acervo_item": "Nenhum exemplar localizado no catálogo Sophia do Câmpus Garopaba",
        "obs": f"Obra ausente no catálogo. Meta normativa: {meta_exemplares} ex. Faltam comprar: {meta_exemplares} ex."
    }

def run_full_audit():
    print("Iniciando auditoria completa com regras normativas de quantitativos...")
    index_obj, all_acervo = load_and_index_acervo()
    ucs = parse_ppc_md()
    
    records = []
    
    for uc in ucs:
        uc_id = uc["id"]
        uc_nome = uc["uc_nome"]
        semestre = uc["semestre"]
        bloco = uc["bloco"]
        ch = uc["ch"]
        
        # Basica
        for idx, ref in enumerate(uc["basica"], 1):
            meta = extract_metadata(ref)
            res = match_single_reference(ref, meta, index_obj, all_acervo, "Básica")
            records.append({
                "UC_ID": uc_id,
                "UC_Nome": uc_nome,
                "Ano_Semestre": semestre,
                "Bloco_Formacao": bloco,
                "Carga_Horaria": ch,
                "Tipo_Bibliografia": "Básica",
                "Ordem_UC": idx,
                "Referencia_PPC": ref.replace("**", ""),
                "Autor_Principal": meta["autor"],
                "Titulo_Obra": meta["titulo"],
                "Edicao_PPC": meta["edicao"],
                "Ano_PPC": meta["ano"],
                "Status": res["status"],
                "Status_Legenda": res["status_label"],
                "Existe_Biblioteca": "SIM" if res["status"] in ["EXISTE_NO_ACERVO", "EXISTE_EDICAO_DIFERENTE", "MATERIAL_FNDE"] else "NÃO",
                "Exemplares_Disponiveis": res["exemplares"],
                "Exemplares_Label": res["exemplares_label"],
                "Meta_Normativa_Exemplares": res["meta_exemplares"],
                "Deficit_Exemplares_Compra": res["deficit_exemplares"],
                "Status_Normativo": res["status_normativo"],
                "Referencia_Acervo_Sophia": res["acervo_item"],
                "Observacao_Tecnica": res["obs"]
            })
            
        # Complementar
        for idx, ref in enumerate(uc["complementar"], 1):
            meta = extract_metadata(ref)
            res = match_single_reference(ref, meta, index_obj, all_acervo, "Complementar")
            records.append({
                "UC_ID": uc_id,
                "UC_Nome": uc_nome,
                "Ano_Semestre": semestre,
                "Bloco_Formacao": bloco,
                "Carga_Horaria": ch,
                "Tipo_Bibliografia": "Complementar",
                "Ordem_UC": idx,
                "Referencia_PPC": ref.replace("**", ""),
                "Autor_Principal": meta["autor"],
                "Titulo_Obra": meta["titulo"],
                "Edicao_PPC": meta["edicao"],
                "Ano_PPC": meta["ano"],
                "Status": res["status"],
                "Status_Legenda": res["status_label"],
                "Existe_Biblioteca": "SIM" if res["status"] in ["EXISTE_NO_ACERVO", "EXISTE_EDICAO_DIFERENTE", "MATERIAL_FNDE"] else "NÃO",
                "Exemplares_Disponiveis": res["exemplares"],
                "Exemplares_Label": res["exemplares_label"],
                "Meta_Normativa_Exemplares": res["meta_exemplares"],
                "Deficit_Exemplares_Compra": res["deficit_exemplares"],
                "Status_Normativo": res["status_normativo"],
                "Referencia_Acervo_Sophia": res["acervo_item"],
                "Observacao_Tecnica": res["obs"]
            })
            
    df_all = pd.DataFrame(records)
    print(f"Auditoria concluída com sucesso! Total de {len(df_all)} referências auditadas.")
    
    excel_path = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia.xlsx")
    
    total_ref = len(df_all)
    total_b = len(df_all[df_all["Tipo_Bibliografia"] == "Básica"])
    total_c = len(df_all[df_all["Tipo_Bibliografia"] == "Complementar"])
    sim_total = len(df_all[df_all["Existe_Biblioteca"] == "SIM"])
    sim_b = len(df_all[(df_all["Tipo_Bibliografia"] == "Básica") & (df_all["Existe_Biblioteca"] == "SIM")])
    sim_c = len(df_all[(df_all["Tipo_Bibliografia"] == "Complementar") & (df_all["Existe_Biblioteca"] == "SIM")])
    nao_total = len(df_all[df_all["Existe_Biblioteca"] == "NÃO"])
    nao_b = len(df_all[(df_all["Tipo_Bibliografia"] == "Básica") & (df_all["Existe_Biblioteca"] == "NÃO")])
    nao_c = len(df_all[(df_all["Tipo_Bibliografia"] == "Complementar") & (df_all["Existe_Biblioteca"] == "NÃO")])
    
    # Calculate Total Physical Exemplars & Deficit
    total_exemplares_disponiveis = df_all["Exemplares_Disponiveis"].sum()
    total_deficit_basica = df_all[df_all["Tipo_Bibliografia"] == "Básica"]["Deficit_Exemplares_Compra"].sum()
    total_deficit_comp = df_all[df_all["Tipo_Bibliografia"] == "Complementar"]["Deficit_Exemplares_Compra"].sum()
    total_deficit_geral = total_deficit_basica + total_deficit_comp
    
    summary_data = {
        "Métrica / Indicador Normativo": [
            "Total de Unidades Curriculares (UCs) no PPC",
            "Total de Referências Bibliográficas Analisadas",
            "  • Títulos de Bibliografia Básica (Norma: Mínimo 2 por UC)",
            "  • Títulos de Bibliografia Complementar (Norma: Mínimo 3 por UC)",
            "Total de Títulos EXISTENTES na Biblioteca (Físico / PNLD)",
            "  • Cobertura de Títulos na Bibliografia Básica (%)",
            "  • Cobertura de Títulos na Bibliografia Complementar (%)",
            "  • Cobertura Global de Títulos do Curso (%)",
            "PREMISSA NORMATIVA DE QUANTITATIVOS FÍSICOS (IFSC)",
            "  • Meta Básica: ao menos 3 exemplares físicos por título",
            "  • Meta Complementar: ao menos 1 exemplar físico por título",
            "Total de Exemplares Físicos Atualmente Disponíveis para o Curso",
            "DEMANDA TOTAL DE EXEMPLARES FÍSICOS PARA AQUISIÇÃO",
            "  • Cópias Físicas a Adquirir para a Bibliografia BÁSICA (Meta >= 3 ex.)",
            "  • Cópias Físicas a Adquirir para a Bibliografia COMPLEMENTAR (Meta >= 1 ex.)",
            "  • TOTAL GERAL DE EXEMPLARES FÍSICOS A COMPRAR"
        ],
        "Valor": [
            len(ucs),
            total_ref,
            total_b,
            total_c,
            sim_total,
            f"{(sim_b / total_b * 100):.1f}% ({sim_b} de {total_b} títulos)",
            f"{(sim_c / total_c * 100):.1f}% ({sim_c} de {total_c} títulos)",
            f"{(sim_total / total_ref * 100):.1f}% ({sim_total} de {total_ref} títulos)",
            "—",
            "3 exemplares / título básico",
            "1 exemplar / título complementar",
            f"{total_exemplares_disponiveis} exemplares físicos",
            "—",
            f"{total_deficit_basica} exemplares físicos",
            f"{total_deficit_comp} exemplares físicos",
            f"{total_deficit_geral} exemplares físicos para 100% de conformidade"
        ]
    }
    
    uc_summary = df_all.groupby(["UC_ID", "UC_Nome", "Ano_Semestre", "Bloco_Formacao"]).agg(
        Total_Ref=('Referencia_PPC', 'count'),
        Basica_Total=('Tipo_Bibliografia', lambda x: (x == 'Básica').sum()),
        Basica_Existente=('Existe_Biblioteca', lambda x: ((df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Básica') & (x == 'SIM')).sum()),
        Basica_Ausente=('Existe_Biblioteca', lambda x: ((df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Básica') & (x == 'NÃO')).sum()),
        Basica_Deficit_Exemplares=('Deficit_Exemplares_Compra', lambda x: df_all.loc[x.index[df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Básica'], 'Deficit_Exemplares_Compra'].sum()),
        Comp_Total=('Tipo_Bibliografia', lambda x: (x == 'Complementar').sum()),
        Comp_Existente=('Existe_Biblioteca', lambda x: ((df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Complementar') & (x == 'SIM')).sum()),
        Comp_Ausente=('Existe_Biblioteca', lambda x: ((df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Complementar') & (x == 'NÃO')).sum()),
        Comp_Deficit_Exemplares=('Deficit_Exemplares_Compra', lambda x: df_all.loc[x.index[df_all.loc[x.index, 'Tipo_Bibliografia'] == 'Complementar'], 'Deficit_Exemplares_Compra'].sum()),
        Total_Existente=('Existe_Biblioteca', lambda x: (x == 'SIM').sum()),
        Total_Ausente=('Existe_Biblioteca', lambda x: (x == 'NÃO').sum()),
        Total_Deficit_Exemplares=('Deficit_Exemplares_Compra', 'sum')
    ).reset_index()
    uc_summary["Cobertura_Perc"] = (uc_summary["Total_Existente"] / uc_summary["Total_Ref"] * 100).round(1).astype(str) + "%"
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        pd.DataFrame(summary_data).to_excel(writer, sheet_name="Resumo_Geral", index=False)
        df_nao = df_all[df_all["Existe_Biblioteca"] == "NÃO"].copy()
        df_nao.sort_values(by=["Tipo_Bibliografia", "UC_Nome"], ascending=[True, True]).to_excel(writer, sheet_name="Obras_Ausentes_Aquisicao", index=False)
        df_var = df_all[df_all["Status"] == "EXISTE_EDICAO_DIFERENTE"].copy()
        df_var.sort_values(by=["UC_Nome"]).to_excel(writer, sheet_name="Variacao_Edicao_Acervo", index=False)
        df_sim = df_all[df_all["Existe_Biblioteca"] == "SIM"].copy()
        df_sim.sort_values(by=["Tipo_Bibliografia", "UC_Nome"]).to_excel(writer, sheet_name="Obras_Existentes", index=False)
        df_all.to_excel(writer, sheet_name="Mapeamento_Completo_PPC", index=False)
        uc_summary.to_excel(writer, sheet_name="Cobertura_Por_UC", index=False)

    print(f"Planilha consolidada gravada em: {excel_path}")
    return df_all, ucs, summary_data, uc_summary

def generate_markdown_reports(df_all, ucs, summary_data, uc_summary):
    david_md_path = os.path.join(CHECK_DIR, "sumario_executivo_david_biblioteca.md")
    relatorio_md_path = os.path.join(CHECK_DIR, "relatorio_auditoria_biblioteca_ppc.md")
    
    total_deficit_basica = df_all[df_all["Tipo_Bibliografia"] == "Básica"]["Deficit_Exemplares_Compra"].sum()
    total_deficit_comp = df_all[df_all["Tipo_Bibliografia"] == "Complementar"]["Deficit_Exemplares_Compra"].sum()
    total_deficit_geral = total_deficit_basica + total_deficit_comp
    
    df_nao_b = df_all[(df_all["Existe_Biblioteca"] == "NÃO") & (df_all["Tipo_Bibliografia"] == "Básica")].copy()
    df_var = df_all[df_all["Status"] == "EXISTE_EDICAO_DIFERENTE"].copy()
    
    lines_david = [
        "# Sumário Executivo: Auditoria Normativa de Acervo e Quantitativos de Exemplares Físicos",
        "",
        "**Para:** David (Bibliotecário-Documentalista — IFSC Câmpus Garopaba)  ",
        "**De:** Comissão de Reformulação do PPC Técnico em Administração Integrado  ",
        "**Data:** 28 de Agosto de 2026  ",
        "**Assunto:** Análise Normativa de Acervo (Mínimo de 3 ex. Básica e 1 ex. Complementar)  ",
        "",
        "---",
        "",
        "## 1. Premissas Normativas da Análise (IFSC)",
        "",
        "Em consonância com as normas de regulação e avaliação de cursos do IFSC, a auditoria aplicou os seguintes critérios de quantitativos mínimos:",
        "1. **Bibliografia Básica:** Mínimo de **2 títulos de livros** por Unidade Curricular, devendo o acervo do câmpus disponibilizar **ao menos 3 exemplares físicos de cada título** (ou livro PNLD com 1 exemplar por estudante).",
        "2. **Bibliografia Complementar:** Mínimo de **3 títulos de livros** por Unidade Curricular, devendo o acervo do câmpus disponibilizar **ao menos 1 exemplar físico de cada título**.",
        "",
        "---",
        "",
        "## 2. Síntese Quantitativa e Demanda de Aquisição",
        "",
        pd.DataFrame(summary_data).to_markdown(index=False),
        "",
        "---",
        "",
        f"### 🎯 Demanda Consolidada de Compras para o Câmpus Garopaba:",
        f"- **Bibliografia Básica:** Aquisição de **{total_deficit_basica} exemplares físicos** (para suprir os títulos ausentes com 3 cópias e complementar títulos com acervo reduzido de 1 ou 2 cópias).",
        f"- **Bibliografia Complementar:** Aquisição de **{total_deficit_comp} exemplares físicos** (1 cópia de cada título ausente).",
        f"- **Total Geral de Compras:** **{total_deficit_geral} exemplares físicos** para atingir 100% de conformidade normativa no câmpus.",
        "",
        "---",
        "",
        "## 3. Relação Prioritária: Bibliografia BÁSICA (Demanda de 3 Exemplares por Título)",
        "",
        "| Unidade Curricular | Autor | Título da Obra | Edição / Ano | Exemplares no Sophia | Déficit de Compras |",
        "| :--- | :--- | :--- | :---: | :---: | :---: |"
    ]
    
    for _, row in df_nao_b.iterrows():
        autor_fmt = str(row['Autor_Principal'])[:35] if pd.notna(row['Autor_Principal']) else 'Sem Autor / Institucional'
        titulo_fmt = str(row['Titulo_Obra'])[:45]
        ed_fmt = f"{row['Edicao_PPC']}ª ed., {row['Ano_PPC']}" if row['Edicao_PPC'] else str(row['Ano_PPC'])
        lines_david.append(f"| **{row['UC_Nome']}** | {autor_fmt} | *{titulo_fmt}* | {ed_fmt} | 0 ex. | **+3 ex. (Básica)** |")
        
    lines_david.extend([
        "",
        "---",
        "",
        "## 4. Obras com Variação de Edição/Ano Disponíveis no Sophia",
        "",
        "| Unidade Curricular | Tipo | Autor | Título | Edição PPC | Edição & Exemplares no Sophia |",
        "| :--- | :---: | :--- | :--- | :---: | :--- |"
    ])
    
    for _, row in df_var.iterrows():
        autor_fmt = str(row['Autor_Principal'])[:25]
        titulo_fmt = str(row['Titulo_Obra'])[:35]
        tipo_fmt = row['Tipo_Bibliografia']
        ed_ppc = f"{row['Edicao_PPC']}ª ed." if row['Edicao_PPC'] else str(row['Ano_PPC'])
        ex_info = f"{row['Exemplares_Disponiveis']} ex. - " if row['Exemplares_Disponiveis'] else ""
        ref_acervo_short = ex_info + str(row['Referencia_Acervo_Sophia'])[:50] + "..."
        lines_david.append(f"| **{row['UC_Nome']}** | {tipo_fmt} | {autor_fmt} | *{titulo_fmt}* | {ed_ppc} | {ref_acervo_short} |")
        
    lines_david.extend([
        "",
        "---",
        "",
        "**Comissão de Reformulação do PPC Técnico em Administração Integrado**  ",
        "IFSC — Câmpus Garopaba"
    ])
    
    with open(david_md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines_david))
    print(f"Sumário executivo gerado em: {david_md_path}")

def run_all():
    df_all, ucs, summary_data, uc_summary = run_full_audit()
    generate_markdown_reports(df_all, ucs, summary_data, uc_summary)
    print("Processo de auditoria normativa concluído com sucesso!")

if __name__ == "__main__":
    run_all()
