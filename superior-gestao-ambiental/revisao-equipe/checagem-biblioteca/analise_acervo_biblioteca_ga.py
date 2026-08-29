#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auditoria Bibliográfica & Análise Normativa de Quantitativos de Acervo
PPC CST em Gestão Ambiental (IFSC Garopaba) vs. Catálogo Sophia (Acervo e exemplares.XLS).

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

BASE_DIR = "/Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/superior-gestao-ambiental"
CHECK_DIR = os.path.join(BASE_DIR, "revisao-equipe", "checagem-biblioteca")
TXT_PATH = os.path.join(CHECK_DIR, "Unidades Curriculares Gestão Ambiental.txt")
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

def extract_metadata(ref_text, prev_author=''):
    cleaned = ref_text.replace("**", "").replace("*", "").strip()
    cleaned = re.sub(r'^\d+[\.\)]\s*', '', cleaned)
    
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
    
    # Repetition author ______
    t = cleaned
    if t.startswith('______') or t.startswith('____.'):
        t = re.sub(r'^_+[\.\s]*', '', t).strip()
        autor_part = prev_author if prev_author else 'MESMO AUTOR'
        resto = t
    else:
        # Step 1: Protect (Org.), (Orgs.), (Coord.), (Ed.), (Eds.)
        t = re.sub(r'\(([A-Za-z\s\.]+)\)', lambda m: '(' + m.group(1).replace('.', '_DOT_') + ')', t)
        t = re.sub(r'\.\s*\(', '_DOT_ (', t)
        
        # Step 2: Institutional Authors at the start (e.g. EMBRAPA., IBGE., BRASIL., BANCO MUNDIAL., UNESCO., etc.)
        m_inst = re.match(r'^(BRASIL|EMBRAPA|IBGE|BANCO MUNDIAL|UNESCO|WHO|ONU|CONAMA|AGÊNCIA NACIONAL DE ÁGUAS|MINISTÉRIO [^.]+?|SECRETARIA [^.]+?|INSTITUTO [^.]+?)\.\s+(.+)$', t, re.IGNORECASE)
        if m_inst:
            autor_part = m_inst.group(1).strip()
            resto = m_inst.group(2).strip()
        else:
            # Step 3: Protect author dots before author-separating ';' or '&'
            while True:
                new_t = re.sub(r'\.(?=[^.]*(?:;\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇ\s\-]{2,}\s*,|&\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇ\s\-]{2,}\s*,|;\s*et\s+al|&\s*et\s+al))', '_DOT_', t)
                if new_t == t:
                    break
                t = new_t
                
            # Step 4: Protect 'et al.' -> keep the final dot as boundary
            t = re.sub(r'\bet\s+al\.', r'et al.', t)
            
            # Step 5: Protect author initials like 'J. David.' right after surname
            t = re.sub(r'([A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,},\s+[A-Z])\.\s+([A-Z][a-z]+)\.', r'\1_DOT_ \2.', t)
            
            # Step 6: Protect consecutive initials and particles
            for _ in range(8):
                t = re.sub(r'([A-Z])\.\s*(?=(?:de|da|do|dos|das|e|&)\b)', r'\1_DOT_ ', t)
                t = re.sub(r'\b(de|da|do|dos|das)\s+([A-Z])\.\s*(?=[A-Z](?:\.|\_DOT\_)|\b(?:de|da|do|dos|das)\b)', r'\1 \2_DOT_ ', t)
                t = re.sub(r'([A-Z])\.\s*(?=[A-Z](?:\.|\_DOT\_))', r'\1_DOT_ ', t)
                t = re.sub(r'([A-Z])\.\s*(?=\([A-Za-z\s\.]+\))', r'\1_DOT_ ', t)
                t = re.sub(r'([A-Z])\.\s*(?=et\s+al)', r'\1_DOT_ ', t)
                
            if '.' in t:
                parts = t.split('.', 1)
                autor_part = parts[0].replace('_DOT_', '.').strip()
                resto = parts[1].replace('_DOT_', '.').strip()
            else:
                autor_part = "AUTOR DESCONHECIDO"
                resto = t.replace('_DOT_', '.').strip()

    autor_part = re.sub(r'\s+', ' ', autor_part).strip(' .,;')
    
    # Extract Title from resto
    resto_clean = resto
    resto_clean = re.sub(r'(\d+)\.\s*ed\b', r'\1_ED_', resto_clean, flags=re.IGNORECASE)
    resto_clean = re.sub(r'\bv\.\s*(\d+)', r'v_DOT_\1', resto_clean)
    resto_clean = re.sub(r'\bn\.\s*(\d+)', r'n_DOT_\1', resto_clean)
    resto_clean = re.sub(r'\bp\.\s*(\d+)', r'p_DOT_\1', resto_clean)
    resto_clean = re.sub(r'\b(In|in)\.:', r'In_DOT_:', resto_clean)
    resto_clean = re.sub(r'\bDisponível em:', r'_DISP_', resto_clean)
    
    parts_t = resto_clean.split('. ')
    titulo = parts_t[0].replace('_ED_', '. ed').replace('_DOT_', '.').replace('_DISP_', 'Disponível em:').strip()
    
    # If title starts with '(org.)' or '(orgs.)', move it to author
    m_org_tit = re.match(r'^\s*\((\s*(?:org|orgs|coord|coords|ed|eds)\.?\s*)\)\.?\s*(.+)$', titulo, re.IGNORECASE)
    if m_org_tit:
        autor_part = f'{autor_part} ({m_org_tit.group(1).strip()})'
        titulo = m_org_tit.group(2).strip()
        
    if len(titulo) < 3 and len(parts_t) > 1:
        titulo = parts_t[1].replace('_ED_', '. ed').replace('_DOT_', '.').strip()
        
    # If title has comma before city: publisher (e.g. 'Educação & atualidade brasileira, São Paulo: Cortez')
    titulo = re.split(r',\s*(?:São Paulo|Rio de Janeiro|Belo Horizonte|Brasília|Porto Alegre|Curitiba|Florianópolis|Campinas|[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-zÀ-ÿ]+)\s*:', titulo)[0].strip()
    titulo = re.sub(r'\s+', ' ', titulo).strip(' .,;')

    titulo_curto = titulo.split(':')[0].strip() if ':' in titulo else titulo
    autor_sobrenome = autor_part.split(',')[0].strip() if ',' in autor_part else autor_part.split()[0] if autor_part.split() else ""
    primeiro_autor = normalize_str(autor_sobrenome)
    
    return {
        "autor": autor_part,
        "primeiro_autor": primeiro_autor,
        "primeiro_autor_raw": autor_sobrenome,
        "titulo": titulo,
        "titulo_curto": titulo_curto,
        "edicao": edicao,
        "ano": ano,
        "isbn": isbn,
        "is_generic": False,
        "is_authorless": len(primeiro_autor) == 0
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
    print(f"Lendo Acervo Sophia em: {target_path}")
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
        
    print(f"Total de registros carregados do Sophia: {len(acervo_items)} títulos | Total de exemplares físicos: {sum(r['exemplares'] for r in acervo_items)}")
    return AcervoIndex(acervo_items), acervo_items

def merge_reference_lines(raw_text):
    # 1. Split concatenated refs on same line
    t = raw_text
    t = re.sub(r'(\b\d{4}\.)\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,},\s+)', r'\1\n\2', t)
    t = re.sub(r'(\b\d{4}\.)\s+(______[\.\s])', r'\1\n\2', t)
    t = re.sub(r'(\b______\.\s+[^\n]+?\b\d{4}\.)\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,},\s+|______)', r'\1\n\2', t)

    lines = [l.strip() for l in t.split('\n') if l.strip()]
    merged = []
    for l in lines:
        if l.startswith('(*)') or 'CH Total' in l or 'CH EaD' in l:
            continue
        if not merged:
            merged.append(l)
        else:
            is_new_ref = False
            if not (merged[-1].rstrip().endswith(';') or merged[-1].rstrip().endswith('&')):
                if re.match(r'^[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}(?:\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,})*,\s+[A-Za-zÀ-ÿ]', l):
                    is_new_ref = True
                elif re.match(r'^(BRASIL|EMBRAPA|IBGE|MMA|MEC|UNESCO|WHO|ONU|CONAMA|BANCO MUNDIAL|INSTITUTO|MINISTÉRIO|SECRETARIA|FNDE|AGÊNCIA)\b', l, re.IGNORECASE):
                    is_new_ref = True
                elif re.match(r'^\d+[\.\)]\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}', l):
                    is_new_ref = True
                elif l.startswith('LIVRO didático') or l.startswith('Material didático'):
                    is_new_ref = True
                elif l.startswith('______') or l.startswith('____.'):
                    is_new_ref = True
                
            if is_new_ref:
                merged.append(l)
            else:
                merged[-1] = merged[-1] + ' ' + l
                
    return [r.strip() for r in merged if len(r.strip()) > 10]

def parse_txt_ementas():
    with open(TXT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    raw_blocks = text.split('------------------------------------------------------------')
    if len(raw_blocks) < 10:
        raw_blocks = re.split(r'\n(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ\s\-\/\(\)]{3,60}\n\s*Semestre\s*:)', text)
        if len(raw_blocks) < 10:
            raw_blocks = [u.strip() for u in text.split('Unidade Curricular:') if u.strip()]

    ucs_info = []
    all_refs = []
    
    idx = 0
    for block in raw_blocks:
        if 'Semestre:' not in block:
            continue
        idx += 1
        
        # UC Name
        b_lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
        uc_nome = "UC DESCONHECIDA"
        for i, l in enumerate(b_lines):
            if 'Semestre:' in l:
                if i > 0:
                    uc_nome = b_lines[i-1]
                break
                
        # Clean uc_nome
        uc_nome = re.sub(r'^\d+[\.\-\s]+', '', uc_nome).strip()
        uc_nome = uc_nome.replace('UC:', '').replace('Unidade Curricular:', '').strip()
        
        # Semestre
        sem_match = re.search(r'Semestre\s*:\s*(\d+)', block)
        sem_val = int(sem_match.group(1)) if sem_match else 1
        
        # Cargas Horárias
        ch_match = re.search(r'CH Total\s*\(\*\)\s*:\s*(\d+)', block)
        ch_val = ch_match.group(1) + "h" if ch_match else "60h"
        
        ch_ead_match = re.search(r'CH EaD\s*\(\*\)\s*:\s*(\d+)', block)
        ch_ead_val = ch_ead_match.group(1) + "h" if ch_ead_match else "0h"
        
        ch_ext_match = re.search(r'CH Extensão\s*:\s*(\d+)', block)
        ch_ext_val = ch_ext_match.group(1) + "h" if ch_ext_match else "0h"
        
        ch_pres_match = re.search(r'CH Presencial\s*:\s*(\d+)', block)
        ch_pres_val = ch_pres_match.group(1) + "h" if ch_pres_match else ch_val
        
        # Objectives
        obj_items = []
        if 'Objetivos:' in block:
            obj_part = block.split('Objetivos:')[1]
            if 'Conteúdos:' in obj_part:
                obj_part = obj_part.split('Conteúdos:')[0]
            for l in obj_part.split('\n'):
                l_str = l.strip()
                if l_str.startswith('*') or l_str.startswith('•') or l_str.startswith('-'):
                    obj_items.append(l_str.lstrip('*•- ').strip())
                elif l_str and len(l_str) > 15:
                    obj_items.append(l_str)

        # Contents
        cont_text = ""
        if 'Conteúdos:' in block:
            cont_part = block.split('Conteúdos:')[1]
            if 'Estratégias de ensino' in cont_part:
                cont_part = cont_part.split('Estratégias de ensino')[0]
            cont_text = cont_part.strip()

        # Strategies
        estr_text = ""
        if 'Estratégias de ensino' in block:
            estr_part = block.split('Estratégias de ensino')[1]
            if 'Bibliografia Básica:' in estr_part:
                estr_part = estr_part.split('Bibliografia Básica:')[0]
            estr_text = estr_part.strip().lstrip(': \n')

        # BB
        bb_list = []
        if 'Bibliografia Básica:' in block:
            bb_part = block.split('Bibliografia Básica:')[1]
            if 'Bibliografia Complementar:' in bb_part:
                bb_part = bb_part.split('Bibliografia Complementar:')[0]
            else:
                bb_part = bb_part.split('(*)')[0]
            bb_list = merge_reference_lines(bb_part)
                    
        # BC
        bc_list = []
        if 'Bibliografia Complementar:' in block:
            bc_part = block.split('Bibliografia Complementar:')[1].split('(*)')[0]
            bc_list = merge_reference_lines(bc_part)

        uc_data = {
            'id': idx,
            'uc_nome': uc_nome,
            'semestre': sem_val,
            'ch_total': ch_val,
            'ch_ead': ch_ead_val,
            'ch_ext': ch_ext_val,
            'ch_pres': ch_pres_val,
            'objetivos': obj_items,
            'conteudos': cont_text,
            'estrategias': estr_text,
            'qtd_bb': len(bb_list),
            'qtd_bc': len(bc_list),
            'bb': bb_list,
            'bc': bc_list
        }
        ucs_info.append(uc_data)

        prev_author_bb = ""
        for b in bb_list:
            meta = extract_metadata(b, prev_author=prev_author_bb)
            prev_author_bb = meta['autor']
            all_refs.append({
                'uc_id': idx,
                'uc': uc_nome,
                'semestre': sem_val,
                'tipo': 'BÁSICA',
                'ref_raw': b,
                'meta': meta
            })

        prev_author_bc = ""
        for c in bc_list:
            meta = extract_metadata(c, prev_author=prev_author_bc)
            prev_author_bc = meta['autor']
            all_refs.append({
                'uc_id': idx,
                'uc': uc_nome,
                'semestre': sem_val,
                'tipo': 'COMPLEMENTAR',
                'ref_raw': c,
                'meta': meta
            })

    print(f"Total de UCs analisadas: {len(ucs_info)} | Total de Obras Referenciadas no PPC: {len(all_refs)}")
    return ucs_info, all_refs

def audit_bibliografia(all_refs, acervo_index, all_acervo):
    results = []
    
    for ref in all_refs:
        meta = ref['meta']
        ref_raw = ref['ref_raw']
        tipo = ref['tipo']
        uc = ref['uc']
        semestre = ref['semestre']
        
        meta_exemplares = 3 if tipo == 'BÁSICA' else 1
        
        # PNLD check
        if meta.get('is_generic') or 'pnld' in meta.get('primeiro_autor', ''):
            results.append({
                'UC': uc,
                'Semestre': semestre,
                'Tipo': tipo,
                'Referencia_PPC': ref_raw,
                'Titulo_PPC': meta['titulo'],
                'Autor_PPC': meta['autor'],
                'Edicao_PPC': meta['edicao'],
                'Ano_PPC': meta['ano'],
                'ISBN_PPC': meta['isbn'],
                'Existe_Biblioteca': 'SIM',
                'Status': 'PNLD_FNDE',
                'Status_Legivel': 'Disponibilizado via PNLD / FNDE (1 por aluno)',
                'Titulo_Acervo': 'Material Didático PNLD / FNDE',
                'Autor_Acervo': 'MEC / FNDE',
                'Edicao_Acervo': 'Edição PNLD Vigente',
                'Ano_Acervo': '2024-2026',
                'Exemplares_Acervo': 40,
                'Meta_Normativa_IFSC': meta_exemplares,
                'Deficit_Exemplares': 0,
                'Detalhes_Correspondencia': 'Livro Didático atendido pelo Programa Nacional do Livro Didático (PNLD).'
            })
            continue

        p_autor = meta['primeiro_autor']
        p_tit = meta['titulo']
        p_tit_curto = meta['titulo_curto']
        p_isbn = meta['isbn']
        p_ano = meta['ano']
        p_ed = meta['edicao']

        # Candidates from Index
        candidates = acervo_index.find_candidates(meta)
        
        best_match = None
        best_score = 0
        best_match_type = ""

        # 1. ISBN
        if p_isbn:
            for cand in candidates:
                c_isbn = cand["meta"]["isbn"]
                if c_isbn and p_isbn == c_isbn:
                    best_match = cand
                    best_score = 100
                    best_match_type = "ISBN_EXATO"
                    break

        # 2. Similarity Matching
        if not best_match:
            for cand in candidates:
                c_meta = cand["meta"]
                c_autor = c_meta["primeiro_autor"]
                c_tit = c_meta["titulo"]
                c_tit_curto = c_meta["titulo_curto"]
                
                # Check author compatibility
                author_match = False
                if meta["is_authorless"] or c_meta["is_authorless"]:
                    author_match = True
                elif p_autor and c_autor:
                    if p_autor == c_autor or p_autor in c_autor or c_autor in p_autor:
                        author_match = True
                    elif SequenceMatcher(None, p_autor, c_autor).ratio() >= 0.8:
                        author_match = True
                        
                # Check title compatibility
                title_match = is_title_match(p_tit, c_tit) or is_title_match(p_tit_curto, c_tit_curto)
                
                if author_match and title_match:
                    score = SequenceMatcher(None, normalize_str(p_tit), normalize_str(c_tit)).ratio()
                    if score > best_score:
                        best_score = score
                        best_match = cand
                        best_match_type = "AUTOR_TITULO"

        if best_match:
            ex_count = best_match['exemplares']
            deficit = max(0, meta_exemplares - ex_count)
            c_meta = best_match["meta"]
            
            is_ed_diff = bool(p_ed and c_meta['edicao'] and p_ed != c_meta['edicao'])
            is_ano_diff = bool(p_ano and c_meta['ano'] and abs(int(p_ano) - int(c_meta['ano'])) >= 2 if p_ano.isdigit() and c_meta['ano'].isdigit() else False)
            
            if is_ed_diff or is_ano_diff:
                status = "EXISTE_EDICAO_DIFERENTE"
                status_leg = f"Disponível no Acervo ({ex_count} ex.), porém edição/ano diverge (PPC: {p_ed}ª ed. {p_ano} vs. Acervo: {c_meta['edicao']}ª ed. {c_meta['ano']})"
            else:
                status = "EXISTE_CONFIRMADO"
                status_leg = f"Disponível no Acervo com {ex_count} exemplar(es) físico(s)"

            results.append({
                'UC': uc,
                'Semestre': semestre,
                'Tipo': tipo,
                'Referencia_PPC': ref_raw,
                'Titulo_PPC': meta['titulo'],
                'Autor_PPC': meta['autor'],
                'Edicao_PPC': meta['edicao'],
                'Ano_PPC': meta['ano'],
                'ISBN_PPC': meta['isbn'],
                'Existe_Biblioteca': 'SIM',
                'Status': status,
                'Status_Legivel': status_leg,
                'Titulo_Acervo': c_meta['titulo'],
                'Autor_Acervo': c_meta['autor'],
                'Edicao_Acervo': c_meta['edicao'],
                'Ano_Acervo': c_meta['ano'],
                'Exemplares_Acervo': ex_count,
                'Meta_Normativa_IFSC': meta_exemplares,
                'Deficit_Exemplares': deficit,
                'Detalhes_Correspondencia': f"Correspondência via {best_match_type} no Sophia."
            })
        else:
            deficit = meta_exemplares
            results.append({
                'UC': uc,
                'Semestre': semestre,
                'Tipo': tipo,
                'Referencia_PPC': ref_raw,
                'Titulo_PPC': meta['titulo'],
                'Autor_PPC': meta['autor'],
                'Edicao_PPC': meta['edicao'],
                'Ano_PPC': meta['ano'],
                'ISBN_PPC': meta['isbn'],
                'Existe_Biblioteca': 'NÃO',
                'Status': 'NAO_EXISTE',
                'Status_Legivel': f'Título Ausente no Acervo Físico (Demanda de Compra: {deficit} exemplar(es))',
                'Titulo_Acervo': '—',
                'Autor_Acervo': '—',
                'Edicao_Acervo': '—',
                'Ano_Acervo': '—',
                'Exemplares_Acervo': 0,
                'Meta_Normativa_IFSC': meta_exemplares,
                'Deficit_Exemplares': deficit,
                'Detalhes_Correspondencia': 'Título não localizado no inventário físico de Garopaba.'
            })

    return pd.DataFrame(results)

def main():
    acervo_index, all_acervo = load_and_index_acervo()
    ucs_info, all_refs = parse_txt_ementas()
    df_results = audit_bibliografia(all_refs, acervo_index, all_acervo)

    excel_output_path = os.path.join(CHECK_DIR, "Analise_Bibliografica_PPC_vs_Acervo_Sophia_GA.xlsx")
    
    with pd.ExcelWriter(excel_output_path, engine='openpyxl') as writer:
        df_results.to_excel(writer, sheet_name='Diagnóstico Consolidado', index=False)
        
        # Aba Compras Básica (< 3 exemplares)
        df_compras_basica = df_results[(df_results['Tipo'] == 'BÁSICA') & (df_results['Deficit_Exemplares'] > 0)]
        df_compras_basica.to_excel(writer, sheet_name='Compras Básica (<3 Exs)', index=False)
        
        # Aba Compras Complementar (< 1 exemplar)
        df_compras_comp = df_results[(df_results['Tipo'] == 'COMPLEMENTAR') & (df_results['Deficit_Exemplares'] > 0)]
        df_compras_comp.to_excel(writer, sheet_name='Compras Complementar (<1 Ex)', index=False)

        # Aba Variações de Edição
        df_var = df_results[df_results['Status'] == 'EXISTE_EDICAO_DIFERENTE']
        df_var.to_excel(writer, sheet_name='Variações Edição e Ano', index=False)

        # Aba Catálogo Sophia Completo
        df_sophia_full = pd.DataFrame([{
            'Titulo': r['meta']['titulo'],
            'Autor': r['meta']['autor'],
            'Ano': r['meta']['ano'],
            'Edicao': r['meta']['edicao'],
            'Exemplares': r['exemplares'],
            'Referencia_Completa': r['raw']
        } for r in all_acervo])
        df_sophia_full.to_excel(writer, sheet_name='Catálogo Sophia Garopaba', index=False)

    print(f"\nPlanilha Excel gerada com sucesso em:\n{excel_output_path}")

    # Resumo Geral
    total_obras = len(df_results)
    total_sim = len(df_results[df_results['Existe_Biblioteca'] == 'SIM'])
    total_nao = len(df_results[df_results['Existe_Biblioteca'] == 'NÃO'])
    total_var = len(df_results[df_results['Status'] == 'EXISTE_EDICAO_DIFERENTE'])
    
    deficit_basica = df_results[df_results['Tipo'] == 'BÁSICA']['Deficit_Exemplares'].sum()
    deficit_comp = df_results[df_results['Tipo'] == 'COMPLEMENTAR']['Deficit_Exemplares'].sum()
    deficit_total = deficit_basica + deficit_comp

    print("\n==================================================")
    print("📊 RESUMO NORMATIVO — CST EM GESTÃO AMBIENTAL (IFSC)")
    print("==================================================")
    print(f"Total de Unidades Curriculares: 33 UCs")
    print(f"Total de Referências Analisadas: {total_obras}")
    print(f"  • Títulos Disponíveis no Acervo: {total_sim} ({total_sim/total_obras*100:.1f}%)")
    print(f"  • Títulos Ausentes no Acervo: {total_nao} ({total_nao/total_obras*100:.1f}%)")
    print(f"  • Variações de Edição / Ano: {total_var}")
    print(f"🚨 DEMANDA DE COMPRAS DE EXEMPLARES:")
    print(f"  • Bibliografia BÁSICA (< 3 exs.): +{deficit_basica} exemplares físicos")
    print(f"  • Bibliografia COMPLEMENTAR (< 1 ex.): +{deficit_comp} exemplares físicos")
    print(f"  • DEMANDA TOTAL DE COMPRAS: +{deficit_total} EXEMPLARES FÍSICOS")
    print("==================================================\n")

if __name__ == "__main__":
    main()
