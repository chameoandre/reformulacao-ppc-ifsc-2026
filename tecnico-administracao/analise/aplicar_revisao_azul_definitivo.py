# -*- coding: utf-8 -*-
import os
import re

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# Separate header from tables
pos_uc = tex.find('\\subsection{Unidades curriculares:}')
header_part = tex[:pos_uc + len('\\subsection{Unidades curriculares:}')]
tables_part = tex[pos_uc + len('\\subsection{Unidades curriculares:}'):]

# Extract each table block
table_pattern = r"(% -+\s*% TABELA EMENTA ([0-9]+):[^\n]*\s*% -+\s*\\begin\{xltabular\}.*?\\end\{xltabular\})"
matches = re.findall(table_pattern, tex, re.DOTALL)
table_dict = {int(num): full_table for full_table, num in matches}
print(f"Loaded {len(table_dict)} tables.")

def wrap_revisao(text):
    return f"\\revisao{{{text}}}"

# 1. TABELA 15 (Gestão de Marketing I - 100% REVISADA)
t15 = """% ---------------------------------------------------------
% TABELA EMENTA 15: Gestão de Marketing I
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Gestão de Marketing I}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Compreender os fundamentos do marketing e sua importância na criação, comunicação e entrega de valor para clientes e organizações.}
    \\item \\revisao{Identificar características do mercado e dos consumidores que influenciam as decisões de marketing das organizações.}
    \\item \\revisao{Aplicar conceitos e ferramentas básicas de marketing nas decisões relacionadas ao composto de marketing, considerando a perspectiva da organização e do consumidor.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{Conceito e papel do marketing.} \\newline
\\revisao{Necessidades, desejo, demanda e criação de valor.} \\newline
\\revisao{Ambiente de marketing.} \\newline
\\revisao{Comportamento do consumidor e processo de decisão de compra.} \\newline
\\revisao{Segmentação do mercado.} \\newline
\\revisao{Composto de marketing e sua evolução: 4Ps e abordagens contemporâneas orientadas ao cliente.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, articulando os fundamentos conceituais do marketing a situações práticas e contextualizadas. Poderão ser desenvolvidos estudos de caso, resolução de problemas, análise do comportamento do consumidor, análise de organizações, atividades de observação do mercado, oficinas práticas e simulações. As atividades buscarão promover a compreensão e a aplicação dos conceitos de marketing em diferentes contextos organizacionais, considerando as transformações no comportamento do consumidor, nos mercados, nas tecnologias e nas formas de criação, comunicação e entrega de valor, preferencialmente relacionadas à realidade do território. Entre os espaços físicos, a unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar e centro multiuso, podendo também desenvolver atividades de observação e pesquisa em organizações e em outros espaços da comunidade.} \\newline\\vspace{2pt}
\\textbf{Avaliação:} \\revisao{A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular e a progressão das aprendizagens. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo, estudos de caso, resolução de problemas, relatórios, produções gráficas e digitais, apresentações, projetos, portfólios, autoavaliação, avaliação por pares e avaliações escritas, quando pertinentes.} \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} \\revisao{A unidade curricular buscará estabelecer conexões com outros componentes curriculares, especialmente Língua Portuguesa, Língua Inglesa e Língua Espanhola, nos processos de comunicação e produção de conteúdos; Artes, nos aspectos relacionados à criatividade, linguagem visual e comunicação; e Sociologia e Filosofia, na análise crítica das relações entre consumo, sociedade, ética, cultura e comportamento.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{KOTLER, Philip; KELLER, Kevin Lane. \\textbf{Administração de marketing}. 12. ed. 5. reimp. São Paulo: Pearson Prentice Hall, 2010.} \\newline
\\revisao{LAS CASAS, Alexandre Luzzi. \\textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{ARBACHE, Fernando Saba. \\textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011.} \\newline
\\revisao{DANTAS, Edmundo Brandão. \\textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011.} \\newline
\\revisao{KOTLER, Philip; ARMSTRONG, Gary. \\textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015.} \\newline
\\revisao{LAS CASAS, Alexandre Luzzi. \\textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}} \\\\ \\hline
\\end{xltabular}"""
table_dict[15] = t15

# 2. TABELA 29 (Gestão de Marketing II - 100% REVISADA)
t29 = """% ---------------------------------------------------------
% TABELA EMENTA 29: Gestão de Marketing II
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Gestão de Marketing II}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{3º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Compreender os fundamentos do planejamento e das estratégias de marketing, reconhecendo a importância da pesquisa e das informações de mercado para a tomada de decisões.}
    \\item \\revisao{Analisar práticas de posicionamento, marca, comunicação, vendas e relacionamento com clientes em diferentes contextos organizacionais.}
    \\item \\revisao{Compreender as práticas de marketing digital e sua aplicação na comunicação e no relacionamento com os clientes.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{Fundamentos do planejamento e das estratégias de marketing.} \\newline
\\revisao{Pesquisa de marketing: etapas, coleta e análise básica de dados.} \\newline
\\revisao{Posicionamento, marca e experiência do cliente.} \\newline
\\revisao{Comunicação de marketing: comunicação integrada, marketing digital, mídias sociais e conteúdo.} \\newline
\\revisao{Vendas, atendimento e relacionamento com o cliente.} \\newline
\\revisao{Tecnologias e indicadores aplicados ao marketing: métricas básicas, dados e inteligência artificial.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, articulando os conhecimentos de marketing às situações práticas e contextualizadas. Poderão ser desenvolvidos estudos de caso, resolução de problemas, pesquisas de marketing, análise de organizações e marcas, oficinas práticas e atividades envolvendo comunicação, vendas, relacionamento com clientes e marketing digital. As atividades buscarão favorecer a compreensão e a aplicação dos conceitos estudados, por meio da análise de situações mercadológicas e da proposição de ações de marketing. Poderão ser utilizadas ferramentas digitais e de inteligência artificial como apoio às atividades, considerando aspectos éticos relacionados à sua utilização. Entre os espaços físicos, a unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar e centro multiuso, podendo também desenvolver atividades de observação e pesquisa em organizações e outros espaços da comunidade.} \\newline\\vspace{2pt}
\\textbf{Avaliação:} \\revisao{A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular e a progressão das aprendizagens. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo, estudos de caso, resolução de problemas, relatórios, produções gráficas e digitais, apresentações, projetos, portfólios, autoavaliação, avaliação por pares e avaliações escritas, quando pertinentes.} \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} \\revisao{A unidade curricular buscará estabelecer conexões com outros componentes curriculares, especialmente Gestão de Marketing I, Língua Portuguesa, Língua Inglesa e Língua Espanhola, nos processos de comunicação e produção de conteúdos; Artes, nos aspectos relacionados à criatividade, linguagem visual e comunicação; e Sociologia e Filosofia, na análise crítica das relações entre consumo, sociedade, ética, cultura e comportamento.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{LAS CASAS, Alexandre Luzzi. \\textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021.} \\newline
\\revisao{MATTAR, Fauze Najib. \\textbf{Pesquisa de marketing}. 4. ed. compacta 3. reimp. São Paulo: Atlas, 2007.} \\newline
\\revisao{VIRGILLITO, Salvatore Benito (coord.). \\textbf{Pesquisa de marketing}: uma abordagem quantitativa e qualitativa. São Paulo: Saraiva, 2010.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{ARBACHE, Fernando Saba. \\textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011.} \\newline
\\revisao{DANTAS, Edmundo Brandão. \\textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011.} \\newline
\\revisao{KOTLER, Philip; ARMSTRONG, Gary. \\textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015.} \\newline
\\revisao{LAS CASAS, Alexandre Luzzi. \\textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.}} \\\\ \\hline
\\end{xltabular}"""
table_dict[29] = t29

# 3. TABELA 31 (Empreendedorismo I - 100% REVISADA)
t31 = """% ---------------------------------------------------------
% TABELA EMENTA 31: Empreendedorismo I
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Empreendedorismo I}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{4º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Compreender o conceito de empreendedorismo e suas diferentes manifestações no mundo contemporâneo.}
    \\item \\revisao{Identificar características, comportamentos e competências associadas à atitude empreendedora e ao desenvolvimento pessoal e profissional.}
    \\item \\revisao{Reconhecer experiências de economia solidária, cooperativismo e associativismo como formas alternativas de organização e geração de trabalho e renda.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{Empreendedorismo e mundo do trabalho: conceitos, evolução histórica e contexto contemporâneo.} \\newline
\\revisao{Diferentes formas de empreender: empreendedorismo tradicional, corporativo (intraempreendedorismo), social, digital, sustentável, cooperativismo, associativismo e economia solidária.} \\newline
\\revisao{Comportamento e competências empreendedoras: criatividade, iniciativa, visão de oportunidade, planejamento, resolução de problemas, tomada de decisão, liderança, cooperação e responsabilidade social.} \\newline
\\revisao{Inovação: conceitos, tipos e sua relação com o empreendedorismo.} \\newline
\\revisao{Empreendedorismo e território: identificação de potenciais locais e regionais, demandas comunitárias e iniciativas de impacto socioambiental.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, com ênfase em atividades práticas que busquem relacionar os conhecimentos desenvolvidos à realidade dos estudantes, ao mundo do trabalho e ao contexto socioeconômico do território, contemplando também experiências de economia solidária, cooperativismo e associativismo. Entre os espaços físicos, esta unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar, centro multiuso e espaços externos durante as visitas técnicas.} \\newline\\vspace{2pt}
\\textbf{Avaliação:} \\revisao{A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo baseados em estudos de caso, resolução de problemas, pesquisas, dinâmicas, entrevistas, análise de experiências empreendedoras, visitas técnicas e outras atividades que aproximem os estudantes de diferentes formas de empreender e inovar.} \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} \\revisao{A unidade curricular mantém conexão com Responsabilidade Socioambiental e Sustentabilidade; Línguas Inglesa, Portuguesa e Espanhola sobre as expressões e comunicação; Artes sobre as inovações; e Sociologia, Sociedade e Trabalho e Filosofia com reflexões sobre empreendedorismo, ética e sociedade.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{BESSANT, John; TIDD, Joe; COSTA, Francisco Araújo da. \\textbf{Inovação e empreendedorismo}. 3. ed. Porto Alegre: Bookman, 2019.} \\newline
\\revisao{DORNELAS, José Carlos Assis. \\textbf{Empreendedorismo}: transformando idéias em negócios. 3. ed. rev. e atual. Rio de Janeiro: Elsevier, 2008.} \\newline
\\revisao{DORNELAS, José Carlos Assis. \\textbf{Empreendedorismo corporativo}: como ser empreendedor, inovar e se diferenciar na sua empresa. 2. ed. Rio de Janeiro: Elsevier, 2008.} \\newline
\\revisao{HISRICH, Robert D.; PETERS, Michael P.; SHEPHERD, Dean A. \\textbf{Empreendedorismo}. Tradução de Francisco Araújo da Costa. 9. ed. Porto Alegre: AMGH, 2014.} \\newline
\\revisao{OLIVEIRA, Edson Marques. \\textbf{Empreendedorismo social}: da teoria à prática, do sonho à realidade. Rio de Janeiro: Qualitymark, 2008.} \\newline
\\revisao{SINGER, Paul \\textit{et al.} \\textbf{Economia Solidária}: introdução, história e experiência brasileira. São Paulo: Editora Unesp, 2023.} \\newline
\\revisao{WEBERING, Susana Iglesias. \\textbf{Autogestão e Cooperação}. Curitiba: Editora Appris, 2020.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{BERNARDI, Luiz Antônio. \\textbf{Manual de empreendedorismo e gestão}: fundamentos, estratégias e dinâmicas. 2. ed. São Paulo: Atlas, 2012.} \\newline
\\revisao{OLIVEIRA, Djalma de Pinho Rebouças de. \\textbf{Empreendedorismo}: vocação, capacitação e atuação direcionadas para o plano de negócios. São Paulo: Editora Atlas, 2014.}} \\\\ \\hline
\\end{xltabular}"""
table_dict[31] = t31

# 4. TABELA 44 (Gestão Financeira - 100% REVISADA)
t44 = """% ---------------------------------------------------------
% TABELA EMENTA 44: Gestão Financeira
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Gestão Financeira}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{\\revisao{5º e 6º}}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{\\revisao{80 h}} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Conhecer os principais conceitos relacionados às rotinas financeiras.}
    \\item \\revisao{Organizar informações financeiras para gestão de empreendimentos de micro e pequeno porte.}
    \\item \\revisao{Elaborar controles e demonstrativos financeiros.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{Controles financeiros básicos: contas a pagar, contas a receber, caixa, movimentação bancária.} \\newline
\\revisao{Tipos de Custos.} \\newline
\\revisao{Formação de preços.} \\newline
\\revisao{Fluxo de caixa e planejamento financeiro.} \\newline
\\revisao{Capital de giro.} \\newline
\\revisao{Demonstrações financeiras e suas análises.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{A unidade curricular será desenvolvida por meio de aulas expositivas dialogadas e metodologias ativas de aprendizagem, com enfoque teórico-prático, promovendo a participação dos estudantes na compreensão dos processos relacionados à gestão financeira. Serão adotadas estratégias metodológicas com exercícios práticos, análises de caso e simulações. As atividades de aprendizagem poderão incluir análise de práticas organizacionais, simulações, exercícios práticos, interações com organizações e profissionais da área, articulando os conhecimentos desenvolvidos na unidade curricular com situações reais do mundo do trabalho. Entre os espaços físicos, esta unidade curricular fará uso da sala de aula da turma, laboratório de informática e sala multidisciplinar, bem como espaços de organizações externas.} \\newline\\vspace{2pt}
\\textbf{Avaliação:} \\revisao{O processo de avaliação será contínuo, processual e formativo, contemplando diferentes instrumentos, como produções escritas, apresentações orais, resolução de estudos de caso, atividades práticas, relatórios, registros reflexivos e participação nas atividades propostas. As avaliações poderão ser realizadas de forma individual ou em grupo, considerando o desenvolvimento dos conhecimentos, das habilidades e das atitudes previstas para a unidade curricular.} \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} \\revisao{Esta unidade curricular se articula com Empreendedorismo, Gestão de Pessoas e Matemática para Administração. Com a formação geral, há articulação especialmente com Matemática.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{ASSAF NETO, Alexandre; LIMA, Fabiano Guasti. \\textbf{Curso de administração financeira}. 2. ed. São Paulo: Atlas, 2011.} \\newline
\\revisao{SARMENTO, Melo, M. \\textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas. Rio de Janeiro: Editora Alta Books, 2024.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{FARIAS, Cláudio V. S. (org.). \\textbf{Técnico em administração}: gestão e negócios. Porto Alegre: Bookman, 2013.} \\newline
\\revisao{GITMAN, Lawrence J. \\textbf{Princípios de administração financeira}. 12. ed. São Paulo: Pearson, 2010.} \\newline
\\revisao{SOUSA, Antônio de. \\textbf{Gerência financeira para micro e pequenas empresas}: um manual simplificado. Rio de Janeiro: Elsevier/Sebrae, 2007.}} \\\\ \\hline
\\end{xltabular}"""
table_dict[44] = t44

# 5. TABELA 22 (Espanhol 2 - Bloco 3 Felix Medina)
t22 = """% ---------------------------------------------------------
% TABELA EMENTA 22: Espanhol — Ano 2
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Espanhol — Ano 2}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{3º e 4º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Revisar e consolidar as estruturas gramaticais básicas da língua espanhola.}
    \\item \\revisao{Compreender e aplicar tempos verbais no passado (pretérito perfeito e imperfeito).}
    \\item \\revisao{Expandir o vocabulário em eixos temáticos específicos, tais como alimentos, roupas, lazer e clima.}
    \\item \\revisao{Desenvolver habilidades de comunicação em situações de nível intermediário, capacitando para a descrição de pessoas, lugares e eventos.}
    \\item \\revisao{Redigir textos breves e funcionais, como cartas e e-mails informais.}
    \\item \\revisao{Analisar criticamente manifestações da cultura popular e celebrações hispânicas, articulando reflexões sobre direitos humanos, alimentação saudável e História e Cultura Afro-Brasileira e Indígena.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{Revisão de estruturas gramaticais básicas.} \\newline
\\revisao{Tempos verbais no passado: pretérito perfeito e imperfeito.} \\newline
\\revisao{Vocabulário ampliado: alimentos, roupas, lazer, clima.} \\newline
\\revisao{Interculturalidade: celebrações, festividades e cultura popular nos países hispanofalantes.} \\newline
\\revisao{Comunicação em situações intermediárias: descrevendo pessoas, lugares e eventos.} \\newline
\\revisao{Introdução à escrita de textos breves: cartas e e-mails informais.} \\newline
\\revisao{Abordagem de Temáticas Transversais: História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões integradas sobre os direitos humanos.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{Abordagem comunicativa com ênfase em situações da vida real, priorizando o uso prático do idioma por meio de simulações e diálogos. Uso de plataformas digitais para o desenvolvimento de atividades de escrita colaborativa e debates sobre temas culturais e transversais. Em caso de oferta de carga horária EAD: utilização exclusiva do Moodle, incorporando quizzes interativos, fóruns orientados e vídeo-aulas. Sessões síncronas via videoconferência para prática de fala e escrita, com momentos assíncronos e encontros presenciais opcionais para reforço e avaliações. Tutoria no AVA realizada diretamente pelo docente da UC. Sem divisão de turma.} \\newline\\vspace{2pt}
\\textbf{Avaliação:} \\revisao{Avaliação diagnóstica, processual e formativa através de tarefas orais, produções escritas e testes de compreensão auditiva.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FANJUL, Adrián (org.). \\textbf{Gramática y práctica de español para brasileños}. 2. ed. São Paulo: Moderna, 2011. 287 p. ISBN 9788516074272. \\newline
MORENO, Concha; TUTS, Martina. \\textbf{Cinco estrellas}: español para el turismo. 2. ed. Madrid: SGEL, 2011. 223 p. ISBN 9788497784849.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\revisao{COTO BAUTISTA, Vanessa; TURZA FERRÉ, Anna. \\textbf{Tema a tema B1}: español lengua extranjera : curso de conversación. Madrid: Edelsa, 2011. 111 p. ISBN 9788477117209.} \\newline
GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar}: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p. ISBN 9788477117186. \\newline
\\revisao{WILDNER, Ana Kaciara; OLIVEIRA, Leandra Cristina de; SOBOTTKA, Mary Anne Warken. \\textbf{Espanhol para o turismo}. Florianópolis: Publicação do IFSC, 2014.}} \\\\ \\hline
\\end{xltabular}"""
table_dict[22] = t22

# 6. TABELA 2 (Educação Física 1 - 17 Objetivos)
t2 = """% ---------------------------------------------------------
% TABELA EMENTA 2: Educação Física — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Educação Física — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Promover a reflexão crítica sobre a cultura corporal como construção social, histórica e cultural, desvendando as relações de poder, as desigualdades sociais e as formas de dominação presentes nas práticas corporais.}
    \\item \\revisao{Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade contemporânea.}
    \\item \\revisao{Desenvolver a autonomia dos estudantes para que possam tomar decisões conscientes sobre suas práticas corporais, promovendo a saúde e o bem-estar de forma integral.}
    \\item \\revisao{Promover a valorização da diversidade corporal, cultural e social, combatendo o preconceito e a discriminação em todas as suas formas.}
    \\item \\revisao{Estimular a participação ativa dos alunos na transformação da sociedade, utilizando o esporte e as práticas corporais como ferramentas de promoção da justiça social e da igualdade.}
    \\item \\revisao{Desenvolver a capacidade de analisar e interpretar informações sobre a cultura corporal, utilizando diferentes fontes e linguagens.}
    \\item \\revisao{Promover a cooperação, o respeito mútuo e a valorização das diferenças individuais, contribuindo para a formação de cidadãos solidários e comprometidos com o bem comum.}
    \\item \\revisao{Promover a consciência ambiental e a prática de atividades físicas que respeitem o meio ambiente.}
    \\item \\revisao{Identificar, compreender, analisar e utilizar as diferentes tecnologias relacionadas à cultura corporal em uma base ética, promovendo a inclusão e o desenvolvimento de novas formas de interação social.}
    \\item \\revisao{Analisar como os padrões de beleza e corporeidade são construídos socialmente e como influenciam a autoestima e a saúde dos indivíduos.}
    \\item \\revisao{Identificar as representações do corpo nas diferentes mídias e analisar seus impactos na construção da identidade.}
    \\item \\revisao{Compreender a importância das práticas corporais para a construção da identidade e dos vínculos sociais.}
    \\item \\revisao{Analisar as relações de poder presentes nas práticas esportivas e como elas podem ser utilizadas para promover a inclusão social.}
    \\item \\revisao{Relacionar a prática regular de atividade física com a prevenção de doenças crônicas e a promoção da saúde mental.}
    \\item \\revisao{Analisar a influência da indústria do esporte e da alimentação na saúde da população.}
    \\item \\revisao{Analisar a gênese e as mudanças sócio-históricas do esporte.}
    \\item \\revisao{Analisar a produção e o desenvolvimento da técnica e tecnologias do esporte.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{\\textbf{O corpo como expressão cultural e social:} A construção histórica do corpo e do movimento; O corpo na mídia e a cultura de consumo; O corpo e a diversidade: gênero, raça, classe social, idade e deficiência; A cultura corporal e a identidade.} \\newline
\\revisao{\\textbf{Cultura corporal e suas relações sociais:} Danças populares e urbanas: história, significados e diversidade; Lutas e artes marciais: história, filosofia e valores; Esportes coletivos e individuais: regras, técnicas, táticas e valores; Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate; Os jogos e as brincadeiras.} \\newline
\\revisao{\\textbf{Esporte, competição e performance:} Esporte e sociedade: relações de poder e desigualdade; Doping e ética no esporte; Saúde mental e desempenho esportivo; Esporte e mídia: representações e consumismo.} \\newline
\\revisao{\\textbf{A cultura corporal e o meio ambiente:} Práticas corporais ao ar livre e em contato com a natureza; A importância da sustentabilidade nas práticas esportivas; O impacto do esporte no meio ambiente.} \\newline
\\revisao{\\textbf{O esporte na sociedade capitalista e suas manifestações:} A gênese e o desenvolvimento do esporte; Técnica e tecnologia no esporte; Introdução à economia política do esporte.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014. \\newline
BERNARDES, Luciano Andrade (org.). \\textbf{Atividades e esportes de aventura para profissionais de educação física}. São Paulo: Phorte, 2013.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BRACHT, Valter. \\textbf{Sociologia crítica do esporte}: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003. \\newline
CAMARGO, Wagner Xavier de. \\textbf{Leituras de gênero e sexualidade nos esportes}. São Carlos: EDUFSCAR, 2021. \\newline
FOER, Franklin. \\textbf{Como o futebol explica o mundo}: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.} \\\\ \\hline
\\end{xltabular}"""
table_dict[2] = t2

# 7. TABELA 19 (Educação Física 2 - 19 Objetivos)
t19 = """% ---------------------------------------------------------
% TABELA EMENTA 19: Educação Física — Ano 2
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Educação Física — Ano 2}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{3º e 4º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item \\revisao{Compreender a cultura corporal em suas diversas manifestações e dimensões, relacionando-a com os contextos históricos, sociais e culturais.}
    \\item \\revisao{Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade contemporânea.}
    \\item \\revisao{Analisar criticamente as representações sociais do corpo e do movimento, desconstruindo estereótipos e preconceitos.}
    \\item \\revisao{Investigar a história e a evolução das práticas corporais, valorizando a diversidade cultural.}
    \\item \\revisao{Refletir sobre a influência da mídia e do consumo nas práticas corporais.}
    \\item \\revisao{Promover a sensibilização para a inclusão social através do esporte e do lazer, combatendo o preconceito e a discriminação.}
    \\item \\revisao{Desenvolver projetos que promovam a inclusão de pessoas com deficiência, LGBTQIA+, idosos e outros grupos minoritários.}
    \\item \\revisao{Analisar as políticas públicas de esporte e lazer e suas implicações sociais.}
    \\item \\revisao{Desenvolver a capacidade de analisar criticamente as relações de poder presentes nas práticas corporais e no esporte.}
    \\item \\revisao{Identificar as desigualdades sociais e as relações de gênero presentes no esporte e no lazer.}
    \\item \\revisao{Refletir sobre o papel do esporte como instrumento de transformação social.}
    \\item \\revisao{Desenvolver os estudantes técnicos capazes de atuar em diferentes contextos, utilizando as tecnologias digitais como ferramentas para o ensino e a gestão de projetos.}
    \\item \\revisao{Desenvolver uma consciência crítica em relação ao meio ambiente e à sustentabilidade.}
    \\item \\revisao{Promover a prática de atividades físicas ao ar livre e o contato com a natureza.}
    \\item \\revisao{Incentivar a produção de eventos esportivos e de lazer sustentáveis.}
    \\item \\revisao{Compreender a domesticação dos corpos marginalizados, como mulheres, pessoas negras, LGBTQIA+, e pessoas com deficiência, e os impactos dessa disciplina na ocupação dos espaços destinados ao lazer.}
    \\item \\revisao{Analisar o impacto da vigilância e da moralização nos corpos que ocupam espaços de lazer, promovendo a identificação de práticas de exclusão e estigmatização.}
    \\item \\revisao{Promover discussões interseccionais de gênero, raça e classe social e a domesticação dos corpos nos espaços de lazer.}
    \\item \\revisao{Desenvolver práticas educacionais que fomentem o acesso igualitário ao lazer, subvertendo os mecanismos de exclusão e disciplinamento dos corpos.}
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\revisao{\\textbf{Lazer e tempo livre:} Lazer e tempo livre: conceitos, históricos e transformações; Políticas públicas de lazer e suas implicações sociais; Turismo e lazer: relações e perspectivas; Lazer e tecnologia: impactos e possibilidades.} \\newline
\\revisao{\\textbf{Saúde, corpo e movimento:} Atividade física e saúde: evidências científicas; Alimentação e nutrição para o desempenho esportivo; Lesões esportivas: prevenção e tratamento; Saúde do trabalhador e ergonomia.} \\newline
\\revisao{\\textbf{Cultura corporal e trabalho:} Trabalho e lazer: relações históricas e contemporâneas; Saúde do trabalhador e qualidade de vida.} \\newline
\\revisao{\\textbf{Diversidade, gênero e inclusão:} Corpo, gênero e sexualidade na cultura corporal; Esporte e pessoas com deficiência; Racismo e discriminação no esporte; LGBTQIA+ e esporte.} \\newline
\\revisao{\\textbf{Cultura corporal e suas relações sociais:} Danças populares e urbanas: história, significados e diversidade; Lutas e artes marciais: história, filosofia e valores; Esportes coletivos e individuais: regras, técnicas, táticas e valores; Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate.}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} \\revisao{Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014. \\newline
BERNARDES, Luciano Andrade (org.). \\textbf{Atividades e esportes de aventura para profissionais de educação física}. São Paulo: Phorte, 2013.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BRACHT, Valter. \\textbf{Sociologia crítica do esporte}: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003. \\newline
CAMARGO, Wagner Xavier de. \\textbf{Leituras de gênero e sexualidade nos esportes}. São Carlos: EDUFSCAR, 2021. \\newline
FOER, Franklin. \\textbf{Como o futebol explica o mundo}: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.} \\\\ \\hline
\\end{xltabular}"""
table_dict[19] = t19

# Reassemble ementario_adm.tex
out_lines = [header_part.strip(), "\n\n"]
for num in sorted(table_dict.keys()):
    out_lines.append("\n\\clearpage\n")
    out_lines.append(table_dict[num].strip())
    out_lines.append("\n")

full_output = "".join(out_lines)

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(full_output)

print("ementario_adm.tex gerado com todas as tags de revisao!")
