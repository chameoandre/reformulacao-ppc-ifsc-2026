# -*- coding: utf-8 -*-

# 1. Atualizar main_ppc_administracao.tex
with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    main_tex = f.read()

# Item 7.6. CH Total
main_tex = main_tex.replace(r"\revisao{3.280 horas}", r"\revisao{3.080 horas}")
main_tex = main_tex.replace(r"3.280 horas", r"\revisao{3.080 horas}")
main_tex = main_tex.replace(r"3.200 horas", r"\revisao{3.080 horas}")

# Item 18.1 Matriz Resumida
old_matriz_res = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular (Res. 142/2025)} & \textbf{Carga Horária Mínima} & \textbf{Percentual Total} \\ \hline
Formação Geral (BNCC + Diversificada) & \revisao{2.320 h} & \revisao{70,73\%} \\ \hline
Formação Técnica Profissional (Administração) & \revisao{800 h} & \revisao{24,39\%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{4,88\%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{Carga Horária Total Geral do Curso} & \revisao{\textbf{3.280 h}} & \textbf{100,0\%} \\ \hline"""

new_matriz_res = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular (Res. 142/2025)} & \textbf{Carga Horária Mínima} & \textbf{Percentual Total} \\ \hline
Formação Geral (BNCC + Diversificada) & \revisao{2.280 h} & \revisao{74,03\%} \\ \hline
Formação Técnica Profissional (Administração) & \revisao{640 h} & \revisao{20,78\%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{5,19\%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{Carga Horária Total Geral do Curso} & \revisao{\textbf{3.080 h}} & \textbf{100,0\%} \\ \hline"""

if old_matriz_res in main_tex:
    main_tex = main_tex.replace(old_matriz_res, new_matriz_res)
else:
    # try replacing loosely
    pass

# Item 22 Certificações intermediárias
main_tex = main_tex.replace(r"\revisao{3.280 horas-relógio}", r"\revisao{3.080 horas-relógio}")
main_tex = main_tex.replace(r"3.280 horas-relógio", r"\revisao{3.080 horas-relógio}")

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(main_tex)

print("main_ppc_administracao.tex atualizado para 3.080h!")

# 2. Atualizar ementario_adm.tex
with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    em_tex = f.read()

# Subtotal 3º Ano
em_tex = em_tex.replace(
    r"\multicolumn{3}{|r|}{\revisao{\textbf{Subtotal 3º Ano (640h FG + 240h FT + 80h NP):}}} & \textbf{960 h} \\ \hline",
    r"\multicolumn{3}{|r|}{\revisao{\textbf{Subtotal 3º Ano (600h FG + 200h FT + 80h NP):}}} & \revisao{\textbf{880 h}} \\ \hline"
)

# Quadro Síntese Final
old_sintese = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular} & \textbf{Carga Horária (horas-relógio)} & \textbf{Percentual Total} \\ \hline
Formação Geral (Base Nacional Comum Curricular) & \revisao{2.320 h} & \revisao{70,73 \%} \\ \hline
Formação Técnica Profissional (Eixo Gestão e Negócios) & \revisao{800 h} & \revisao{24,39 \%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{4,88 \%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{CARGA HORÁRIA TOTAL GERAL DO CURSO} & \revisao{\textbf{3.280 h}} & \textbf{100,0 \%} \\ \hline"""

new_sintese = r"""\rowcolor{cinzaTabela}
\textbf{Bloco Curricular} & \textbf{Carga Horária (horas-relógio)} & \textbf{Percentual Total} \\ \hline
Formação Geral (Base Nacional Comum Curricular) & \revisao{2.280 h} & \revisao{74,03 \%} \\ \hline
Formação Técnica Profissional (Eixo Gestão e Negócios) & \revisao{640 h} & \revisao{20,78 \%} \\ \hline
Núcleo Politécnico Comum (Oficinas de Integração) & \revisao{160 h} & \revisao{5,19 \%} \\ \hline
\hline
\rowcolor{ifscgreen!10}
\textbf{CARGA HORÁRIA TOTAL GERAL DO CURSO} & \revisao{\textbf{3.080 h}} & \textbf{100,0 \%} \\ \hline"""

if old_sintese in em_tex:
    em_tex = em_tex.replace(old_sintese, new_sintese)

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(em_tex)

print("ementario_adm.tex atualizado para 3.080h e subtotal 3º ano de 880h!")
