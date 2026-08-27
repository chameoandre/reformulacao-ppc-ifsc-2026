# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# Helper to wrap list items with \revisao{...}
def wrap_items(block):
    return re.sub(r'\\item\s+((?!\\revisao\{).+)$', r'\\item \\revisao{\1}', block, flags=re.MULTILINE)

# 1. Justificativa (Subitem 10)
p1 = "A oferta do Curso Técnico Integrado em Administração no IFSC Câmpus Garopaba teve início em 2018"
p2 = "favorecendo, consequentemente, o desenvolvimento econômico e social da região."

p_start = tex.find(r"\subsection{Justificativa da Oferta do Curso no Câmpus:}")
p_end = tex.find(r"\subsection{Público-alvo:}")

if p_start != -1 and p_end != -1:
    just_block = tex[p_start:p_end]
    # Wrap text paragraphs in \revisao{...}
    # We will replace paragraphs outside tables
    lines = just_block.split('\n\n')
    new_lines = []
    in_table = False
    for l in lines:
        l_str = l.strip()
        if r"\begin{table}" in l_str:
            in_table = True
        if in_table:
            new_lines.append(l)
            if r"\end{table}" in l_str:
                in_table = False
            continue
        if l_str.startswith(r"\subsection"):
            new_lines.append(l)
        elif l_str.startswith(r"\begin{itemize}"):
            new_lines.append(wrap_items(l))
        elif l_str and not l_str.startswith(r"\revisao{"):
            new_lines.append(f"\\revisao{{{l_str}}}")
        else:
            new_lines.append(l)
    tex = tex[:p_start] + "\n\n".join(new_lines) + tex[p_end:]
    print("Justificativa marcada com revisao!")

# 2. Objetivos (Subitem 11)
p_obj_start = tex.find(r"\subsection{Objetivo do curso:}")
p_obj_end = tex.find(r"\subsection{Perfil profissional do egresso:}")
if p_obj_start != -1 and p_obj_end != -1:
    obj_block = tex[p_obj_start:p_obj_end]
    lines = obj_block.split('\n\n')
    new_lines = []
    for l in lines:
        l_str = l.strip()
        if l_str.startswith(r"\subsection") or l_str.startswith(r"\subsubsection"):
            new_lines.append(l)
        elif l_str.startswith(r"\begin{itemize}"):
            new_lines.append(wrap_items(l))
        elif l_str and not l_str.startswith(r"\revisao{"):
            new_lines.append(f"\\revisao{{{l_str}}}")
        else:
            new_lines.append(l)
    tex = tex[:p_obj_start] + "\n\n".join(new_lines) + tex[p_obj_end:]
    print("Objetivos marcados com revisao!")

# 3. Perfil do Egresso e Outras Características (Subitens 13 e 15)
p_perf_start = tex.find(r"\subsection{Perfil profissional do egresso:}")
p_perf_end = tex.find(r"\subsection{Áreas/campo de atuação do egresso:}")
if p_perf_start != -1 and p_perf_end != -1:
    perf_block = tex[p_perf_start:p_perf_end]
    lines = perf_block.split('\n\n')
    new_lines = []
    for l in lines:
        l_str = l.strip()
        if l_str.startswith(r"\subsection"):
            new_lines.append(l)
        elif l_str.startswith(r"\begin{itemize}"):
            new_lines.append(wrap_items(l))
        elif l_str and not l_str.startswith(r"\revisao{"):
            new_lines.append(f"\\revisao{{{l_str}}}")
        else:
            new_lines.append(l)
    tex = tex[:p_perf_start] + "\n\n".join(new_lines) + tex[p_perf_end:]
    print("Perfil e Outras Características marcados com revisao!")

# 4. Metodologia Pedagógica (Subitem 17)
p_met_start = tex.find(r"\subsection{Metodologia de desenvolvimento pedagógico do curso:}")
p_met_end = tex.find(r"\subsection{Matriz curricular:}")
if p_met_start != -1 and p_met_end != -1:
    met_block = tex[p_met_start:p_met_end]
    lines = met_block.split('\n\n')
    new_lines = []
    for l in lines:
        l_str = l.strip()
        if l_str.startswith(r"\subsection"):
            new_lines.append(l)
        elif l_str.startswith(r"\begin{quote}"):
            new_lines.append(l)
        elif l_str and not l_str.startswith(r"\revisao{"):
            new_lines.append(f"\\revisao{{{l_str}}}")
        else:
            new_lines.append(l)
    tex = tex[:p_met_start] + "\n\n".join(new_lines) + tex[p_met_end:]
    print("Metodologia Pedagógica marcada com revisao!")

# 5. Subitem 29: Referência da Metodologia de Ciclos Temáticos
tex = tex.replace(
    r"\item SILVA, E. \textbf{Metodologia de Ciclos Temáticos e Oficinas de Integração na Educação Profissional Técnica}. Florianópolis: IFSC, 2016.",
    r"\item \revisao{SILVA, E. \textbf{Metodologia de Ciclos Temáticos e Oficinas de Integração na Educação Profissional Técnica}. Florianópolis: IFSC, 2016.}"
)

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Todas as seções iniciais e metodológicas atualizadas e marcadas com revisao!")
