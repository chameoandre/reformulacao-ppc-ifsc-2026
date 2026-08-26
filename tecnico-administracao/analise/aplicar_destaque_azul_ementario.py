# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/analise/gerar_ementario_revisado.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's customize the 4 critical UCs and major updates to use \revisacor / \revisao in gerar_ementario_revisado.py

# In Tabela 15:
code = code.replace(
    r"""\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]""",
    r"""\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]"""
)

# Replace the closing of Articulação Curricular in Tab 15
code = code.replace(
    r"""consumo, sociedade, ética, cultura e comportamento.} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Bibliografia Básica:}}}""",
    r"""consumo, sociedade, ética, cultura e comportamento.}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Bibliografia Básica:}}}"""
)

# In Tabela 44 (Gestão Financeira) highlight header + body:
code = code.replace(
    r"""\textbf{Semestre:}} \textbf{5º e 6º}""",
    r"""\textbf{Semestre:}} \textbf{\revisao{5º e 6º}}"""
)
code = code.replace(
    r"""\textbf{00 h} & \textbf{80 h}""",
    r"""\textbf{00 h} & \textbf{\revisao{80 h}}"""
)

with open('tecnico-administracao/analise/gerar_ementario_revisado.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("gerar_ementario_revisado.py atualizado com as tags de revisão!")
