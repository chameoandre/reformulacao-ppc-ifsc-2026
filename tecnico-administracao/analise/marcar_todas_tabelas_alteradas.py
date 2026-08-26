# -*- coding: utf-8 -*-
import os
import re

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

pos_uc = tex.find('\\subsection{Unidades curriculares:}')
header_part = tex[:pos_uc + len('\\subsection{Unidades curriculares:}')]

table_pattern = r"(% -+\s*% TABELA EMENTA ([0-9]+):[^\n]*\s*% -+\s*\\begin\{xltabular\}.*?\\end\{xltabular\})"
matches = re.findall(table_pattern, tex, re.DOTALL)
table_dict = {int(num): full_table for full_table, num in matches}

def tag_items(block):
    # wrap item contents with \revisao{...} if not already wrapped
    def repl_item(m):
        content = m.group(1).strip()
        if content.startswith('\\revisao{'):
            return f"    \\item {content}"
        return f"    \\item \\revisao{{{content}}}"
    return re.sub(r'^\s*\\item\s+(.+)$', repl_item, block, flags=re.MULTILINE)

def tag_paragraphs(block):
    lines = block.split('\\newline')
    new_lines = []
    for l in lines:
        l_str = l.strip()
        if not l_str:
            new_lines.append(l)
            continue
        if '\\revisao{' in l_str:
            new_lines.append(l)
        else:
            new_lines.append(f"\\revisao{{{l_str}}}")
    return " \\newline\n".join(new_lines)

# 1. TABELA 1: Artes 1
t1 = table_dict[1]
t1 = t1.replace("Aulas participativas e dialogadas", "\\revisao{Aulas participativas e dialogadas")
t1 = t1.replace("para atividades práticas.", "para atividades práticas.}")
table_dict[1] = t1

# 2. TABELA 3 e 20: Inglês 1 e 2 (Metodologia)
for num in [3, 20]:
    t = table_dict[num]
    t = t.replace("Aulas expositivas dialogadas e contextualizadas", "\\revisao{Aulas expositivas dialogadas e contextualizadas")
    t = t.replace("conhecimento com os colegas.", "conhecimento com os colegas.}")
    table_dict[num] = t

# 3. TABELA 5: Espanhol 1 (Transversais e Metodologia)
t5 = table_dict[5]
t5 = t5.replace("Abordagem de Temáticas Transversais:", "\\revisao{Abordagem de Temáticas Transversais:")
t5 = t5.replace("culturas hispanofalantes.", "culturas hispanofalantes.}")
t5 = t5.replace("Aulas expositivas com uso de recursos audiovisuais", "\\revisao{Aulas expositivas com uso de recursos audiovisuais")
t5 = t5.replace("Sem divisão de turma.", "Sem divisão de turma.}")
t5 = t5.replace("Avaliação contínua baseada em tarefas orais", "\\revisao{Avaliação contínua baseada em tarefas orais")
t5 = t5.replace("testes de compreensão auditiva.", "testes de compreensão auditiva.}")
table_dict[5] = t5

# 4. TABELA 6 e 35: Biologia 1 e 3 (Conteúdos desdobrados e Metodologia com laboratório)
for num in [6, 35]:
    t = table_dict[num]
    t = t.replace("O processo de ensino-aprendizagem será conduzido", "\\revisao{O processo de ensino-aprendizagem será conduzido")
    t = t.replace("do desempenho escolar.", "do desempenho escolar.}")
    t = t.replace("A avaliação da aprendizagem se dará em uma perspectiva", "\\revisao{A avaliação da aprendizagem se dará em uma perspectiva")
    t = t.replace("e avaliação atitudinal.", "e avaliação atitudinal.}")
    table_dict[num] = t

# 5. TABELA 7, 23, 36: Física 1, 2, 3 (Metodologia e Recursos)
for num in [7, 23, 36]:
    t = table_dict[num]
    t = t.replace("Aulas expositivas e dialogadas, sob a perspectiva", "\\revisao{Aulas expositivas e dialogadas, sob a perspectiva")
    t = t.replace("imagens e vídeos da área.", "imagens e vídeos da área.}")
    table_dict[num] = t

# 6. TABELA 8, 24, 37: Matemática 1, 2, 3 (Conteúdos detalhados e metodologia)
for num in [8, 24, 37]:
    t = table_dict[num]
    t = t.replace("\\textbf{Parte I - Fundamentos:}", "\\revisao{\\textbf{Parte I - Fundamentos:}")
    t = t.replace("moda e desvio padrão.", "moda e desvio padrão.}")
    t = t.replace("Aulas expositivas dialogadas; aulas de exercícios;", "\\revisao{Aulas expositivas dialogadas; aulas de exercícios;")
    t = t.replace("vídeos de matemática por estudantes.", "vídeos de matemática por estudantes.}")
    table_dict[num] = t

# 7. TABELA 9, 25, 38: Química 1, 2, 3 (Objetivos formação integral e metodologia)
for num in [9, 25, 38]:
    t = table_dict[num]
    t = t.replace("contribuindo para a formação integral dos estudantes.", "\\revisao{contribuindo para a formação integral dos estudantes.}")
    t = t.replace("Aulas expositivas dialogadas; resolução de exercícios;", "\\revisao{Aulas expositivas dialogadas; resolução de exercícios;")
    t = t.replace("e a capacidade do espaço.", "e a capacidade do espaço.}")
    table_dict[num] = t

# 8. TABELA 10 e 39: Filosofia 1 e 3 (Metodologia e Bibliografia corrigida)
for num in [10, 39]:
    t = table_dict[num]
    t = t.replace("Aulas expositivas, leituras interpretativas e críticas,", "\\revisao{Aulas expositivas, leituras interpretativas e críticas,")
    t = t.replace("relação ensino-aprendizagem.", "relação ensino-aprendizagem.}")
    table_dict[num] = t

# 9. TABELA 12 e 27: Sociologia 1 e 2 (Metodologia e Recursos)
for num in [12, 27]:
    t = table_dict[num]
    t = t.replace("Leitura, análise, discussão e exposição de textos e imagens", "\\revisao{Leitura, análise, discussão e exposição de textos e imagens")
    t = t.replace("projetor multimídia).", "projetor multimídia).}")
    table_dict[num] = t

# 10. TABELA 13: Introdução à Administração (Articulação e Metodologia)
t13 = table_dict[13]
t13 = t13.replace("Metodologias ativas de aprendizagem articuladas", "\\revisao{Metodologias ativas de aprendizagem articuladas")
t13 = t13.replace("ética nas relações trabalhistas e modos de produção.", "ética nas relações trabalhistas e modos de produção.}")
table_dict[13] = t13

# 11. TABELA 14: Sociedade e Trabalho
t14 = table_dict[14]
t14 = t14.replace("Desafios do mundo do trabalho na atualidade: inteligência artificial e impactos no emprego.", "\\revisao{Desafios do mundo do trabalho na atualidade: inteligência artificial e impactos no emprego.}")
t14 = t14.replace("Aulas expositivas e dialogadas; leitura e discussão", "\\revisao{Aulas expositivas e dialogadas; leitura e discussão")
t14 = t14.replace("estudos de caso e trabalhos individuais/coletivos.", "estudos de caso e trabalhos individuais/coletivos.}")
table_dict[14] = t14

# 12. TABELA 18: Artes 2
t18 = table_dict[18]
t18 = t18.replace("Aulas participativas e dialogadas, partindo do conhecimento", "\\revisao{Aulas participativas e dialogadas, partindo do conhecimento")
t18 = t18.replace("utilização da sala de artes para atividades práticas.", "utilização da sala de artes para atividades práticas.}")
table_dict[18] = t18

# Rebuild ementario_adm.tex
out_lines = [header_part.strip(), "\n\n"]
for num in sorted(table_dict.keys()):
    out_lines.append("\n\\clearpage\n")
    out_lines.append(table_dict[num].strip())
    out_lines.append("\n")

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write("".join(out_lines))

print("Todas as tabelas de ementas marcadas com tags de revisao!")
