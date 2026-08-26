# -*- coding: utf-8 -*-
import re

# 1. Update main_ppc_administracao.tex with macro switch
with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    main_tex = f.read()

macro_block = """% -------------------------------------------------------------
% CONTROLE DE DESTACAMENTO DE ALTERAÇÕES (REVISÃO EM AZUL)
% -------------------------------------------------------------
\\newif\\ifhighlightchanges
\\highlightchangestrue  % Altere para \\highlightchangesfalse para gerar o documento final em preto

\\ifhighlightchanges
  \\newcommand{\\revisao}[1]{\\textcolor{blue}{#1}}
  \\newcommand{\\revisacor}{\\color{blue}}
\\else
  \\newcommand{\\revisao}[1]{#1}
  \\newcommand{\\revisacor}{}
\\fi
"""

if "\\ifhighlightchanges" not in main_tex:
    main_tex = main_tex.replace(
        "\\documentclass{../../modelos/latex-shared/ifsc-ppc}",
        "\\documentclass{../../modelos/latex-shared/ifsc-ppc}\n\n" + macro_block
    )

# Highlight the adjusted line in methodology
old_phrase = "Assim, a formação proposta pelo curso transcende a sala de aula e os conhecimentos do currículo, incentivando e promovendo a participação em atividades integradoras, projetos de extensão e ações formativas nas suas vertentes científicas, tecnológicas, culturais, artísticas, esportivas e de gestão."
if old_phrase in main_tex and "\\revisao{" + old_phrase not in main_tex:
    main_tex = main_tex.replace(old_phrase, "\\revisao{" + old_phrase + "}")

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(main_tex)

print("main_ppc_administracao.tex atualizado com a chave de controle!")
