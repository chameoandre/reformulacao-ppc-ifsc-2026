# -*- coding: utf-8 -*-
import re
import json

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

table_blocks = re.findall(r"% TABELA EMENTA ([0-9]+):\s*([^\n]+)(.*?)(?=(?:% TABELA EMENTA|\Z))", tex, re.DOTALL)

print(f"Total tabelas encontradas: {len(table_blocks)}")

results = []

for num_str, name, t_content in table_blocks:
    num = int(num_str)
    
    # Locate Bibliografia Básica
    p_bb = t_content.find("Bibliografia Básica:")
    p_bc = t_content.find("Bibliografia Complementar:")
    p_end = t_content.find(r"\end{xltabular}")
    
    def extract_between(block):
        # find the first \multicolumn after header
        m = re.search(r"\\multicolumn\{3\}\{[^\}]+\}\{\s*(.*?)\s*\}\s*\\\\\s*\\hline", block, re.DOTALL)
        if m:
            return m.group(1)
        # fallback: find content inside {...}
        m2 = re.search(r"\{\s*(.*?)\s*\}\s*\\\\\s*\\hline", block, re.DOTALL)
        if m2:
            return m2.group(1)
        return ""

    if p_bb != -1:
        if p_bc != -1:
            bb_raw = t_content[p_bb:p_bc]
            bc_raw = t_content[p_bc:p_end]
        else:
            bb_raw = t_content[p_bb:p_end]
            bc_raw = ""
            
        bb_text = extract_between(bb_raw[len("Bibliografia Básica:"):])
        bc_text = extract_between(bc_raw[len("Bibliografia Complementar:"):]) if bc_raw else ""
        
        def parse_refs(block_text, tipo):
            if not block_text:
                return
            clean = block_text.replace(r'\revisao{', '').replace('}', '').strip()
            for line in clean.split(r'\newline'):
                line = line.strip()
                if line:
                    results.append({"tabela": num, "uc": name.strip(), "tipo": tipo, "texto": line})
                    
        parse_refs(bb_text, "Básica")
        parse_refs(bc_text, "Complementar")

print(f"Total de referências extraídas: {len(results)}")

for r in results:
    line = r["texto"]
    issues = []
    
    # Check initials in authors
    # Matches "SOBRENOME, A." or "SOBRENOME, A. B." or "SOBRENOME, Antonio B."
    m_author = re.match(r'^([A-ZÀ-Ú\s\-\'\.]+),\s+([^\.]+)\.', line)
    has_initials = False
    author_initials = ""
    if m_author:
        prenome = m_author.group(2).strip()
        parts = [p for p in prenome.split() if p]
        if any(len(p.replace('.', '')) == 1 for p in parts):
            has_initials = True
            author_initials = prenome
            issues.append(f"Prenome abreviado por inicial ({prenome}.)")
            
    # Missing year
    if not re.search(r'\b(19\d\d|20\d\d)\b', line):
        issues.append("Ano de publicação ausente")
        
    # Missing publisher/place
    if ':' not in line:
        issues.append("Local de publicação e editora ausentes (sem ':')")
        
    # Truncated or very short
    if len(line) < 35 or line.endswith(','):
        issues.append("Referência aparentemente incompleta/truncada")
        
    has_isbn = "ISBN" in line
    
    r["issues"] = issues
    r["has_initials"] = has_initials
    r["author_initials"] = author_initials
    r["has_isbn"] = has_isbn

with open('tecnico-administracao/analise/diagnostico_referencias_biblioteca.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

initials_list = [r for r in results if r["has_initials"]]
crit_list = [r for r in results if any(not i.startswith("Prenome abreviado") for i in r["issues"])]

md = ["# Diagnóstico Detalhado das Referências Bibliográficas (NBR 6023 / Biblioteca)\n\n"]
md.append(f"Foram analisadas **{len(results)} referências bibliográficas** distribuídas nas 45 Unidades Curriculares do PPC.\n\n")

md.append(f"- **Total de Obras Catalogadas:** {len(results)}\n")
md.append(f"- **Obras com Autores/Prenomes Abreviados por Iniciais:** {len(initials_list)} ({len(initials_list)/len(results)*100:.1f}%)\n")
md.append(f"- **Obras com Pendências Estruturais (sem Local/Editora/Ano ou Incompletas):** {len(crit_list)}\n")
md.append(f"- **Obras sem registro de ISBN:** {sum(1 for r in results if not r['has_isbn'])}\n\n")

md.append("## 🚨 1. Obras com Pendências Críticas (Dados Faltantes ou Incompletos)\n\n")
md.append("| UC (Tabela) | Tipo | Referência Atual | Pendência Identificada |\n")
md.append("| :--- | :---: | :--- | :--- |\n")
for r in crit_list:
    crit_desc = [i for i in r["issues"] if not i.startswith("Prenome abreviado")]
    md.append(f"| **Tab. {r['tabela']} - {r['uc']}** | {r['tipo']} | `{r['texto']}` | {', '.join(crit_desc)} |\n")

md.append("\n## 👤 2. Relação de Obras com Prenomes Abreviados por Iniciais (Candidatas à Expansão por Extenso)\n\n")
md.append("| UC (Tabela) | Tipo | Autor Atual | Título da Obra | Referência Completa |\n")
md.append("| :--- | :---: | :--- | :--- | :--- |\n")

for r in initials_list:
    author_part = r['texto'].split(r'\textbf')[0] if r'\textbf' in r['texto'] else r['texto'].split('.')[0]
    title_match = re.search(r'\\textbf\{([^\}]+)\}', r['texto'])
    title = title_match.group(1) if title_match else ""
    md.append(f"| **Tab. {r['tabela']} - {r['uc']}** | {r['tipo']} | `{author_part.strip()}` | *{title}* | {r['texto']} |\n")

with open('tecnico-administracao/analise/RELATORIO_AUDITORIA_BIBLIOGRAFIA.md', 'w', encoding='utf-8') as f:
    f.write("".join(md))

print(f"Diagnóstico concluído! Total: {len(results)} obras. Com iniciais: {len(initials_list)}. Com pendências críticas: {len(crit_list)}.")
