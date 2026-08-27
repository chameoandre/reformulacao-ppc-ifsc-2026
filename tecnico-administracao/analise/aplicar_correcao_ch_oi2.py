# -*- coding: utf-8 -*-
import re

# 1. Atualizar main_ppc_administracao.tex
with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    main_tex = f.read()

# Atualizar Tabela 7 (Dados do Curso)
main_tex = main_tex.replace(
    r"\textcolor{ifscgreen}{\textbf{\textit{7.6. CH Total:}}} & \multicolumn{3}{p{\dimexpr\linewidth-4.4cm-4\tabcolsep-3\arrayrulewidth\relax}|}{3.200 horas} \\ \hline" + "\n" +
    r"\textcolor{ifscgreen}{\textbf{7.6.1 CH Aulas presenciais}} & 3.200 horas & \textcolor{ifscgreen}{\textbf{7.6.2. CH Aulas EaD:}} & 0 h \\ \hline",
    r"\textcolor{ifscgreen}{\textbf{\textit{7.6. CH Total:}}} & \multicolumn{3}{p{\dimexpr\linewidth-4.4cm-4\tabcolsep-3\arrayrulewidth\relax}|}{\revisao{3.280 horas}} \\ \hline" + "\n" +
    r"\textcolor{ifscgreen}{\textbf{7.6.1 CH Aulas presenciais}} & \revisao{3.280 horas} & \textcolor{ifscgreen}{\textbf{7.6.2. CH Aulas EaD:}} & 0 h \\ \hline"
)

# Atualizar Matriz Resumida (Subitem 18.1)
old_matriz_res = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular (Res. 142/2025)} & \textbf{Carga Horária Mínima} & \textbf{Percentual Total} \\ \hline
Formação Geral (BNCC + Diversificada) & 2.280 h & 71,25\% \\ \hline
Formação Técnica Profissional (Administração) & 680 h & 21,25\% \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & 240 h & 7,50\% \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{Carga Horária Total Geral do Curso} & \textbf{3.200 h} & \textbf{100,0\%} \\ \hline"""

new_matriz_res = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular (Res. 142/2025)} & \textbf{Carga Horária Mínima} & \textbf{Percentual Total} \\ \hline
Formação Geral (BNCC + Diversificada) & \revisao{2.320 h} & \revisao{70,73\%} \\ \hline
Formação Técnica Profissional (Administração) & \revisao{800 h} & \revisao{24,39\%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{4,88\%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{Carga Horária Total Geral do Curso} & \revisao{\textbf{3.280 h}} & \textbf{100,0\%} \\ \hline"""

main_tex = main_tex.replace(old_matriz_res, new_matriz_res)

# Atualizar Subitem 22 (Certificações intermediárias)
main_tex = main_tex.replace("3.200 horas-relógio", r"\revisao{3.280 horas-relógio}")

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(main_tex)

print("main_ppc_administracao.tex atualizado com a CH Total de 3.280h!")

# 2. Atualizar ementario_adm.tex
with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    em_tex = f.read()

# Atualizar Tabela do 3º Ano (Subitem 18.2)
old_tabela_3ano = r"""3º Ano & Oficina de Integração II & Núcleo Politécnico & 160 h \\ \hline
\multicolumn{3}{|r|}{\textbf{Subtotal 3º Ano (600h FG + 200h FT + 160h NP):}} & \textbf{960 h} \\ \hline"""

new_tabela_3ano = r"""3º Ano & Oficina de Integração II & Núcleo Politécnico & \revisao{80 h} \\ \hline
\multicolumn{3}{|r|}{\revisao{\textbf{Subtotal 3º Ano (640h FG + 240h FT + 80h NP):}}} & \textbf{960 h} \\ \hline"""

em_tex = em_tex.replace(old_tabela_3ano, new_tabela_3ano)

# Atualizar Quadro Síntese Final (Subitem 18.2)
old_sintese = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular} & \textbf{Carga Horária (horas-relógio)} & \textbf{Percentual Total} \\ \hline
Formação Geral (Base Nacional Comum Curricular) & 2.280 h & 71,25 \% \\ \hline
Formação Técnica Profissional (Eixo Gestão e Negócios) & 680 h & 21,25 \% \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & 240 h & 7,50 \% \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{CARGA HORÁRIA TOTAL GERAL DO CURSO} & \textbf{3.200 h} & \textbf{100,0 \%} \\ \hline"""

new_sintese = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular} & \textbf{Carga Horária (horas-relógio)} & \textbf{Percentual Total} \\ \hline
Formação Geral (Base Nacional Comum Curricular) & \revisao{2.320 h} & \revisao{70,73 \%} \\ \hline
Formação Técnica Profissional (Eixo Gestão e Negócios) & \revisao{800 h} & \revisao{24,39 \%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{4,88 \%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{CARGA HORÁRIA TOTAL GERAL DO CURSO} & \revisao{\textbf{3.280 h}} & \textbf{100,0 \%} \\ \hline"""

em_tex = em_tex.replace(old_sintese, new_sintese)

# Atualizar Tabela 45 (Ementa da Oficina de Integração II)
old_t45_ch = r""" & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{160 h} \\ \hline"""

new_t45_ch = r""" & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \revisao{\textbf{80 h}} \\ \hline"""

em_tex = em_tex.replace(old_t45_ch, new_t45_ch)

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(em_tex)

print("ementario_adm.tex atualizado com a CH de 80h na OI II e quadro síntese!")
