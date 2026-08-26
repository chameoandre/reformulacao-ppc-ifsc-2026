# -*- coding: utf-8 -*-
import os
import re

with open('tecnico-administracao/analise/gerar_ementario_revisado.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's wrap the modified sections in each table with {\revisacor ...} or \revisao{...}

# 1. Tabela 2: Educação Física 1 (objetivos e conteúdos expandidos)
code = re.sub(
    r'(\\multicolumn\{3\}\{\|p\{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax\}\|\}\{\\textcolor\{ifscgreen\}\{\\textbf\{Objetivos:\}\}\} \\\\ \\hline\n\\multicolumn\{3\}\{\|p\{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax\}\|\}\{\n)(\\begin\{itemize\})',
    r'\1{\\revisacor\n\2',
    code,
    count=0
)

# 2. Let's make sure Tabela 15, 29, 31, 44 are fully highlighted:
# Marketing I (Tab 15)
code = code.replace(
    r"""% TABELA EMENTA 15: Gestão de Marketing I
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão de Marketing I}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{2º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{""",
    r"""% TABELA EMENTA 15: Gestão de Marketing I
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão de Marketing I}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{2º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor"""
)

# Close revisacor before bibliografia in Tab 15 and wrap bibliografias in revisacor
code = code.replace(
    r"""KOTLER, Philip; KELLER, Kevin Lane. \textbf{Administração de marketing}. 12. ed. 5. reimp. São Paulo: Pearson Prentice Hall, 2010. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021.}""",
    r"""{\revisacor KOTLER, Philip; KELLER, Kevin Lane. \textbf{Administração de marketing}. 12. ed. 5. reimp. São Paulo: Pearson Prentice Hall, 2010. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021.}}"""
)
code = code.replace(
    r"""ARBACHE, Fernando Saba. \textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \newline
DANTAS, Edmundo Brandão. \textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \newline
KOTLER, Philip; ARMSTRONG, Gary. \textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}""",
    r"""{\revisacor ARBACHE, Fernando Saba. \textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \newline
DANTAS, Edmundo Brandão. \textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \newline
KOTLER, Philip; ARMSTRONG, Gary. \textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}}"""
)

# Marketing II (Tab 29)
code = code.replace(
    r"""% TABELA EMENTA 29: Gestão de Marketing II
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão de Marketing II}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{3º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]""",
    r"""% TABELA EMENTA 29: Gestão de Marketing II
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão de Marketing II}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{3º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]"""
)
code = code.replace(
    r"""LAS CASAS, Alexandre Luzzi. \textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021. \newline
MATTAR, Fauze Najib. \textbf{Pesquisa de marketing}. 4. ed. compacta 3. reimp. São Paulo: Atlas, 2007. \newline
VIRGILLITO, Salvatore Benito (coord.). \textbf{Pesquisa de marketing}: uma abordagem quantitativa e qualitativa. São Paulo: Saraiva, 2010.}""",
    r"""{\revisacor LAS CASAS, Alexandre Luzzi. \textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021. \newline
MATTAR, Fauze Najib. \textbf{Pesquisa de marketing}. 4. ed. compacta 3. reimp. São Paulo: Atlas, 2007. \newline
VIRGILLITO, Salvatore Benito (coord.). \textbf{Pesquisa de marketing}: uma abordagem quantitativa e qualitativa. São Paulo: Saraiva, 2010.}}"""
)
code = code.replace(
    r"""ARBACHE, Fernando Saba. \textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \newline
DANTAS, Edmundo Brandão. \textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \newline
KOTLER, Philip; ARMSTRONG, Gary. \textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}""",
    r"""{\revisacor ARBACHE, Fernando Saba. \textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \newline
DANTAS, Edmundo Brandão. \textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \newline
KOTLER, Philip; ARMSTRONG, Gary. \textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \newline
LAS CASAS, Alexandre Luzzi. \textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}}"""
)

# Empreendedorismo I (Tab 31)
code = code.replace(
    r"""% TABELA EMENTA 31: Empreendedorismo I
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Empreendedorismo I}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{4º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]""",
    r"""% TABELA EMENTA 31: Empreendedorismo I
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Empreendedorismo I}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{4º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{40 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]"""
)
code = code.replace(
    r"""BESSANT, John; TIDD, Joe; COSTA, Francisco Araújo da. \textbf{Inovação e empreendedorismo}. 3. ed. Porto Alegre: Bookman, 2019. \newline
DORNELAS, José Carlos Assis. \textbf{Empreendedorismo}: transformando idéias em negócios. 3. ed. rev. e atual. Rio de Janeiro: Elsevier, 2008. \newline
DORNELAS, José Carlos Assis. \textbf{Empreendedorismo corporativo}: como ser empreendedor, inovar e se diferenciar na sua empresa. 2. ed. Rio de Janeiro: Elsevier, 2008. \newline
HISRICH, Robert D.; PETERS, Michael P.; SHEPHERD, Dean A. \textbf{Empreendedorismo}. Tradução de Francisco Araújo da Costa. 9. ed. Porto Alegre: AMGH, 2014. \newline
OLIVEIRA, Edson Marques. \textbf{Empreendedorismo social}: da teoria à prática, do sonho à realidade. Rio de Janeiro: Qualitymark, 2008. \newline
SINGER, Paul \textit{et al.} \textbf{Economia Solidária}: introdução, história e experiência brasileira. São Paulo: Editora Unesp, 2023. \newline
WEBERING, Susana Iglesias. \textbf{Autogestão e Cooperação}. Curitiba: Editora Appris, 2020.}""",
    r"""{\revisacor BESSANT, John; TIDD, Joe; COSTA, Francisco Araújo da. \textbf{Inovação e empreendedorismo}. 3. ed. Porto Alegre: Bookman, 2019. \newline
DORNELAS, José Carlos Assis. \textbf{Empreendedorismo}: transformando idéias em negócios. 3. ed. rev. e atual. Rio de Janeiro: Elsevier, 2008. \newline
DORNELAS, José Carlos Assis. \textbf{Empreendedorismo corporativo}: como ser empreendedor, inovar e se diferenciar na sua empresa. 2. ed. Rio de Janeiro: Elsevier, 2008. \newline
HISRICH, Robert D.; PETERS, Michael P.; SHEPHERD, Dean A. \textbf{Empreendedorismo}. Tradução de Francisco Araújo da Costa. 9. ed. Porto Alegre: AMGH, 2014. \newline
OLIVEIRA, Edson Marques. \textbf{Empreendedorismo social}: da teoria à prática, do sonho à realidade. Rio de Janeiro: Qualitymark, 2008. \newline
SINGER, Paul \textit{et al.} \textbf{Economia Solidária}: introdução, história e experiência brasileira. São Paulo: Editora Unesp, 2023. \newline
WEBERING, Susana Iglesias. \textbf{Autogestão e Cooperação}. Curitiba: Editora Appris, 2020.}}"""
)
code = code.replace(
    r"""BERNARDI, Luiz Antônio. \textbf{Manual de empreendedorismo e gestão}: fundamentos, estratégias e dinâmicas. 2. ed. São Paulo: Atlas, 2012. \newline
OLIVEIRA, Djalma de Pinho Rebouças de. \textbf{Empreendedorismo}: vocação, capacitação e atuação direcionadas para o plano de negócios. São Paulo: Editora Atlas, 2014.}""",
    r"""{\revisacor BERNARDI, Luiz Antônio. \textbf{Manual de empreendedorismo e gestão}: fundamentos, estratégias e dinâmicas. 2. ed. São Paulo: Atlas, 2012. \newline
OLIVEIRA, Djalma de Pinho Rebouças de. \textbf{Empreendedorismo}: vocação, capacitação e atuação direcionadas para o plano de negócios. São Paulo: Editora Atlas, 2014.}}"""
)

# Gestão Financeira (Tab 44)
code = code.replace(
    r"""% TABELA EMENTA 44: Gestão Financeira
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão Financeira}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{\revisao{5º e 6º}}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{\revisao{80 h}} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]""",
    r"""% TABELA EMENTA 44: Gestão Financeira
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Gestão Financeira}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{\revisao{5º e 6º}}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{\revisao{80 h}} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]"""
)
code = code.replace(
    r"""ASSAF NETO, Alexandre; LIMA, Fabiano Guasti. \textbf{Curso de administração financeira}. 2. ed. São Paulo: Atlas, 2011. \newline
SARMENTO, Melo, M. \textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas. Rio de Janeiro: Editora Alta Books, 2024.}""",
    r"""{\revisacor ASSAF NETO, Alexandre; LIMA, Fabiano Guasti. \textbf{Curso de administração financeira}. 2. ed. São Paulo: Atlas, 2011. \newline
SARMENTO, Melo, M. \textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas. Rio de Janeiro: Editora Alta Books, 2024.}}"""
)
code = code.replace(
    r"""FARIAS, Cláudio V. S. (org.). \textbf{Técnico em administração}: gestão e negócios. Porto Alegre: Bookman, 2013. \newline
GITMAN, Lawrence J. \textbf{Princípios de administração financeira}. 12. ed. São Paulo: Pearson, 2010. \newline
SOUSA, Antônio de. \textbf{Gerência financeira para micro e pequenas empresas}: um manual simplificado. Rio de Janeiro: Elsevier/Sebrae, 2007.}""",
    r"""{\revisacor FARIAS, Cláudio V. S. (org.). \textbf{Técnico em administração}: gestão e negócios. Porto Alegre: Bookman, 2013. \newline
GITMAN, Lawrence J. \textbf{Princípios de administração financeira}. 12. ed. São Paulo: Pearson, 2010. \newline
SOUSA, Antônio de. \textbf{Gerência financeira para micro e pequenas empresas}: um manual simplificado. Rio de Janeiro: Elsevier/Sebrae, 2007.}}"""
)

# Espanhol 2 (Tab 22 - Bloco 3 Felix Medina)
code = code.replace(
    r"""% TABELA EMENTA 22: Espanhol — Ano 2
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Espanhol — Ano 2}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{3º e 4º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{80 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]""",
    r"""% TABELA EMENTA 22: Espanhol — Ano 2
% ---------------------------------------------------------
\begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\hline
\multirow{3}{=}{\textcolor{ifscgreen}{\textbf{Unidade Curricular:}}\\[3pt]\textbf{\large Espanhol — Ano 2}} & \multicolumn{2}{p{\dimexpr5cm+2\tabcolsep+\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Semestre:}} \textbf{3º e 4º}} \\ \cline{2-3}
 & \textcolor{ifscgreen}{\textbf{CH EaD*:}} & \textcolor{ifscgreen}{\textbf{CH Total*:}} \\ \cline{2-3}
 & \textbf{00 h} & \textbf{80 h} \\ \hline
\endfirsthead
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{\textcolor{ifscgreen}{\textbf{Objetivos:}}} \\ \hline
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
{\revisacor
\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]"""
)

with open('tecnico-administracao/analise/gerar_ementario_revisado.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("gerar_ementario_revisado.py atualizado com todas as cores de revisão!")
