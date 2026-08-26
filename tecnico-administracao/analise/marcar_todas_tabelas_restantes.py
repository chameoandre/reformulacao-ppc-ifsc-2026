# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

pos_uc = tex.find('\\subsection{Unidades curriculares:}')
header_part = tex[:pos_uc + len('\\subsection{Unidades curriculares:}')]

table_pattern = r"(% -+\s*% TABELA EMENTA ([0-9]+):[^\n]*\s*% -+\s*\\begin\{xltabular\}.*?\\end\{xltabular\})"
matches = re.findall(table_pattern, tex, re.DOTALL)
table_dict = {int(num): full_table for full_table, num in matches}

# Tabela 4 (LPL 1 - Metodologia)
t4 = table_dict[4]
if "\\revisao{" not in t4:
    t4 = t4.replace("Aulas expositivas dialogadas; aulas de exercícios;", "\\revisao{Aulas expositivas dialogadas; aulas de exercícios;")
    t4 = t4.replace("uso de jogos e objetos de aprendizagem.", "uso de jogos e objetos de aprendizagem.}")
    table_dict[4] = t4

# Tabela 23 e 36 (Física 2 e 3)
for num in [23, 36]:
    t = table_dict[num]
    if "\\revisao{" not in t:
        t = t.replace("Aulas expositivas e dialogadas, sob a perspectiva", "\\revisao{Aulas expositivas e dialogadas, sob a perspectiva")
        t = t.replace("imagens e vídeos da área.", "imagens e vídeos da área.}")
        table_dict[num] = t

# Tabela 25 e 38 (Química 2 e 3)
for num in [25, 38]:
    t = table_dict[num]
    if "\\revisao{" not in t:
        t = t.replace("contribuindo para a formação integral dos estudantes.", "\\revisao{contribuindo para a formação integral dos estudantes.}")
        t = t.replace("Aulas expositivas dialogadas; resolução de exercícios;", "\\revisao{Aulas expositivas dialogadas; resolução de exercícios;")
        t = t.replace("e a capacidade do espaço.", "e a capacidade do espaço.}")
        table_dict[num] = t

# Tabela 27 (Sociologia 2)
t27 = table_dict[27]
if "\\revisao{" not in t27:
    t27 = t27.replace("Leitura, análise, discussão e exposição de textos e imagens", "\\revisao{Leitura, análise, discussão e exposição de textos e imagens")
    t27 = t27.replace("projetor multimídia).", "projetor multimídia).}")
    table_dict[27] = t27

# Rebuild ementario_adm.tex
out_lines = [header_part.strip(), "\n\n"]
for num in sorted(table_dict.keys()):
    out_lines.append("\n\\clearpage\n")
    out_lines.append(table_dict[num].strip())
    out_lines.append("\n")

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write("".join(out_lines))

print("Todas as tabelas restantes marcadas com sucesso!")
