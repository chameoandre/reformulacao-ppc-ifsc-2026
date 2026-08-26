# -*- coding: utf-8 -*-
import os
import re
import sys

def main():
    with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex.bak', 'r', encoding='utf-8') as f:
        orig_tex = f.read()

    pos_uc = orig_tex.find('\\subsection{Unidades curriculares:}')
    header_part = orig_tex[:pos_uc + len('\\subsection{Unidades curriculares:}')]

    # Extract all existing tables
    table_pattern = r"(% -+\s*% TABELA EMENTA ([0-9]+):[^\n]*\s*% -+\s*\\begin\{xltabular\}.*?\\end\{xltabular\})"
    matches = re.findall(table_pattern, orig_tex, re.DOTALL)
    table_dict = {int(num): full_table for full_table, num in matches}

    print(f"Loaded {len(table_dict)} tables from backup.")

    # -------------------------------------------------------------
    # 1. TABELA 1: Artes — Ano 1
    # -------------------------------------------------------------
    # Update bibliographies with ABNT standard
    t1 = """% ---------------------------------------------------------
% TABELA EMENTA 1: Artes — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Artes — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender a Arte como construção histórica, social e cultural e suas imbricações.
    \\item Refletir sobre as relações que envolvem os processos de construção e fruição da Arte.
    \\item Expressar e comunicar ideias e sentimentos por meio de atividades de práticas corporais.
    \\item Desenvolver o senso crítico em relação à arte, à sociedade, à tecnologia e ao meio ambiente.
    \\item Interpretar e analisar o significado de obras de arte a partir de diferentes perspectivas.
    \\item Identificar, experienciar e criar nas diferentes linguagens da arte do corpo em cena (dança, teatro e performance).
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Conceitos básicos: linguagem, objeto de conhecimento, significação e produto. \\newline
Arte contextualizada social, política, histórica e economicamente. \\newline
Manifestações artísticas no decorrer do tempo e do espaço. \\newline
Apreciação e análise de produções artísticas internacionais, nacionais e locais. \\newline
Arte, ciência e meio ambiente: a não separação entre natureza e cultura. \\newline
Arte do corpo em cena na atualidade: apreciação, análise e prática. \\newline
O corpo como instrumento de expressão artística.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas participativas e dialogadas, partindo do conhecimento prévio do estudante, utilizando imagens, textos, vídeos, músicas e corpo; atividades focadas na indissociabilidade entre teoria e prática, com atividades corporais; desenvolvimento de trabalhos, exercícios, pesquisas, seminários e obras artísticas; atividades individuais e em grupos; jogos teatrais e exercícios de improvisação; práticas de dança contemporânea e danças tradicionais brasileiras; utilização da sala de artes para atividades práticas. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Não especificado no documento fonte.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{GOMBRICH, E. H. \\textbf{A história da arte}. Tradução de Álvaro Cabral. 16. ed. Rio de Janeiro: Livros Técnicos e Científicos, 1999. 688 p. ISBN 9788521611851. \\newline
PROENÇA, G. \\textbf{História da arte}. 17. ed. São Paulo: Ática, 2010.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{AGRA, Lucio. \\textbf{História da arte do século XX}: idéias e movimentos. 2. ed. rev. atual. São Paulo: Anhembi, 2004. 192 p. ISBN 8587370146. \\newline
CERTEAU, Michel de. \\textbf{A invenção do cotidiano}: artes de fazer. Tradução de Ephraim Ferreira Alves. 16. ed. Petrópolis, RJ: Vozes, 2009. 315 p. ISBN 9788532611482. \\newline
LARAIA, R. de B. \\textbf{Cultura}: um conceito antropológico. 26. reimp. Rio de Janeiro: Jorge Zahar, 1986. \\newline
SOUZA, Ana Lúcia Silva. \\textbf{Letramentos de reexistência}: poesia, grafite, música, dança : hip-hop. São Paulo: Parábola Editorial, 2011. 171 p. ISBN 9788579340321.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[1] = t1

    # -------------------------------------------------------------
    # 2. TABELA 2: Educação Física — Ano 1 (Expand 17 literal objectives)
    # -------------------------------------------------------------
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
    \\item Promover a reflexão crítica sobre a cultura corporal como construção social, histórica e cultural, desvendando as relações de poder, as desigualdades sociais e as formas de dominação presentes nas práticas corporais.
    \\item Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade contemporânea.
    \\item Desenvolver a autonomia dos estudantes para que possam tomar decisões conscientes sobre suas práticas corporais, promovendo a saúde e o bem-estar de forma integral.
    \\item Promover a valorização da diversidade corporal, cultural e social, combatendo o preconceito e a discriminação em todas as suas formas.
    \\item Estimular a participação ativa dos alunos na transformação da sociedade, utilizando o esporte e as práticas corporais como ferramentas de promoção da justiça social e da igualdade.
    \\item Desenvolver a capacidade de analisar e interpretar informações sobre a cultura corporal, utilizando diferentes fontes e linguagens.
    \\item Promover a cooperação, o respeito mútuo e a valorização das diferenças individuais, contribuindo para a formação de cidadãos solidários e comprometidos com o bem comum.
    \\item Promover a consciência ambiental e a prática de atividades físicas que respeitem o meio ambiente.
    \\item Identificar, compreender, analisar e utilizar as diferentes tecnologias relacionadas à cultura corporal em uma base ética, promovendo a inclusão e o desenvolvimento de novas formas de interação social.
    \\item Analisar como os padrões de beleza e corporeidade são construídos socialmente e como influenciam a autoestima e a saúde dos indivíduos.
    \\item Identificar as representações do corpo nas diferentes mídias e analisar seus impactos na construção da identidade.
    \\item Compreender a importância das práticas corporais para a construção da identidade e dos vínculos sociais.
    \\item Analisar as relações de poder presentes nas práticas esportivas e como elas podem ser utilizadas para promover a inclusão social.
    \\item Relacionar a prática regular de atividade física com a prevenção de doenças crônicas e a promoção da saúde mental.
    \\item Analisar a influência da indústria do esporte e da alimentação na saúde da população.
    \\item Analisar a gênese e as mudanças sócio-históricas do esporte.
    \\item Analisar a produção e o desenvolvimento da técnica e tecnologias do esporte.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\textbf{O corpo como expressão cultural e social:} A construção histórica do corpo e do movimento; O corpo na mídia e a cultura de consumo; O corpo e a diversidade: gênero, raça, classe social, idade e deficiência; A cultura corporal e a identidade. \\newline
\\textbf{Cultura corporal e suas relações sociais:} Danças populares e urbanas: história, significados e diversidade; Lutas e artes marciais: história, filosofia e valores; Esportes coletivos e individuais: regras, técnicas, táticas e valores; Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate; Os jogos e as brincadeiras. \\newline
\\textbf{Esporte, competição e performance:} Esporte e sociedade: relações de poder e desigualdade; Doping e ética no esporte; Saúde mental e desempenho esportivo; Esporte e mídia: representações e consumismo. \\newline
\\textbf{A cultura corporal e o meio ambiente:} Práticas corporais ao ar livre e em contato com a natureza; A importância da sustentabilidade nas práticas esportivas; O impacto do esporte no meio ambiente. \\newline
\\textbf{O esporte na sociedade capitalista e suas manifestações:} A gênese e o desenvolvimento do esporte; Técnica e tecnologia no esporte; Introdução à economia política do esporte.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014. \\newline
BERNARDES, Luciano Andrade (org.). \\textbf{Atividades e esportes de aventura para profissionais de educação física}. São Paulo: Phorte, 2013.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BRACHT, Valter. \\textbf{Sociologia crítica do esporte}: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003. \\newline
CAMARGO, Wagner Xavier de. \\textbf{Leituras de gênero e sexualidade nos esportes}. São Carlos: EDUFSCAR, 2021. \\newline
FOER, Franklin. \\textbf{Como o futebol explica o mundo}: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[2] = t2

    # -------------------------------------------------------------
    # 3. TABELA 3: Inglês — Ano 1
    # -------------------------------------------------------------
    t3 = """% ---------------------------------------------------------
% TABELA EMENTA 3: Inglês — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Inglês — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender a língua inglesa como língua franca e idioma universal, entendendo sua função social como possibilidade de ampliar o acesso à informação e a bens científicos e culturais da humanidade.
    \\item Ampliar de modo autônomo o conhecimento da língua inglesa a partir de estratégias de aprendizagem e compreensão, utilizando ferramentas convencionais e digitais.
    \\item Posicionar-se como usuário ativo da língua inglesa em diferentes cenários, vivenciando práticas de fala, escuta, escrita e de leitura.
    \\item Produzir sentido a partir de elementos linguísticos e extralinguísticos de gêneros textuais (orais, escritos e/ou híbridos), prioritariamente utilizando textos autênticos.
    \\item Conhecer regularidades morfológicas e sintáticas da língua inglesa que auxiliem na compreensão de significados e na ampliação de vocabulário.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Cumprimentos e informações pessoais. \\newline
Perguntas com Wh. \\newline
Artigos. \\newline
Substantivos (objetos, pessoas e lugares). \\newline
Expressões de tempo (horas, dias, meses). \\newline
Pronomes pessoais e demonstrativos. \\newline
Verbo To Be, números e profissões. \\newline
Verbos comuns e Imperativo. \\newline
Presente simples e Advérbios de frequência. \\newline
Presente contínuo. \\newline
Caracterização de objetos, pessoas e lugares. \\newline
Adjetivos (comparativos e superlativos) e Pronomes relativos.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas dialogadas e contextualizadas, buscando aproximação com o cotidiano dos estudantes; apresentação dos conteúdos trabalhados por meio da audição, conversação, leitura e produção de textos e/ou apresentações com recursos multimídia; projetos e atividades envolvendo gêneros textuais de natureza lúdica (música e vídeo), informativa (notícias e textos científicos), literárias (poemas e obras) e/ou técnica e científica; atividades que propiciem ao estudante a oportunidade de compartilhar conhecimento com os colegas.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
\\textbf{DICIONÁRIO Escolar Longman Inglês-Português, Português-Inglês}. Harlow: Pearson Longman, 2004. \\newline
LATHAM-KOENIG, C. \\textbf{English File}: Intermediate Student's Book. Oxford: Oxford University Press, 2018.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FRANCO, C. P. \\textbf{English vibes for Brazilian learners}: volume único. 1. ed. São Paulo: FTD, 2020. \\newline
MURPHY, Raymond. \\textbf{Essential Grammar in Use}. 4th ed. Cambridge: Cambridge University Press, 2015. \\newline
WHARTON, S. \\textbf{500 tips for tesol}: (teaching english to speakers of other languages). London: Kogan Page, 1999.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[3] = t3

    # -------------------------------------------------------------
    # 4. TABELA 4: Língua Portuguesa e Literatura — Ano 1
    # -------------------------------------------------------------
    t4 = """% ---------------------------------------------------------
% TABELA EMENTA 4: Língua Portuguesa e Literatura — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Língua Portuguesa e Literatura — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Reconhecer a Língua Portuguesa como um instrumento de inserção social indispensável ao pleno desenvolvimento do educando, visando seu preparo para o pleno exercício da cidadania e a qualificação para o trabalho.
    \\item Compreender a Língua Portuguesa a partir de seus diversos usos e situações comunicativas, entendendo-a como algo mutável no tempo e no espaço, dotada, portanto, de historicidade.
    \\item Entender a literatura como arte representativa de questões humanas, sociais e históricas, dotada de características específicas, como linguagem e forma.
    \\item Reconhecer a língua como elemento cultural perpassado por questões sociológicas e de constituição da identidade.
    \\item Conhecer as heranças afro-indígenas nos mais variados âmbitos do português brasileiro, seja na fonética, semântica, morfossintaxe ou léxico, bem como na literatura nacional.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Conceitos de Linguagem. \\newline
Leitura, compreensão, análise e produção de textos de diferentes tipologias e gêneros. \\newline
Aspectos gramaticais da Língua Portuguesa: fonética e fonologia. \\newline
Introdução à Literatura. Identificação do contexto e das características de movimentos literários (Trovadorismo ao Arcadismo). \\newline
Introdução a obras literárias produzidas por autores negros e indígenas brasileiros. \\newline
Introdução aos aspectos históricos do português brasileiro, bem como sua influência na formação da língua.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BAGNO, Marcos. \\textbf{Nada na língua é por acaso}: por uma pedagogia da variação linguística. 2. ed. São Paulo: Parábola Editorial, 2008. 238 p. ISBN 9788588456624. \\newline
CINTRA, Luís F. Lindley (coautor). \\textbf{Nova gramática do português contemporâneo}. 5. ed. Rio de Janeiro: Lexikon, 2008. 762 p. \\newline
PRIETO, Heloisa (org.). \\textbf{Antologia de contos indígenas de ensinamento}: tempo de histórias. São Paulo: Richmond Educação, 2021. 103 p. ISBN 9786557950104.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BAGNO, Marcos. \\textbf{Preconceito linguístico}. 56. ed. rev. e ampl. São Paulo: Parábola Editorial, 2015. 350 p. ISBN 9788579340987. \\newline
BAGNO, Marcos. \\textbf{Gramática, pra que te quero?}: os conhecimentos linguísticos nos livros didáticos de português. Curitiba: Aymará, 2010. 319 p. Bibliografia: p. 313-319. ISBN 9788578416201.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[4] = t4

    # -------------------------------------------------------------
    # 5. TABELA 5: Espanhol — Ano 1
    # -------------------------------------------------------------
    t5 = """% ---------------------------------------------------------
% TABELA EMENTA 5: Espanhol — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Espanhol — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender os aspectos fonéticos e de pronúncia introdutórios da língua espanhola.
    \\item Aplicar cumprimentos, apresentações e vocabulário básico (cores, números, família, dias da semana) em interações cotidianas.
    \\item Utilizar estruturas gramaticais básicas no tempo presente, pronomes pessoais e artigos (definidos e indefinidos) em contextos de comunicação simples.
    \\item Comunicar-se em situações práticas do dia a dia, tais como compras, restaurantes e transportes.
    \\item Reconhecer e discutir aspectos de interculturalidade, incluindo costumes, tradições, cidadania, segurança no trânsito, práticas sustentáveis (meio ambiente) e direitos humanos em culturas hispanofalantes.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Introdução à língua espanhola: fonética e pronúncia. \\newline
Cumprimentos e apresentações. \\newline
Vocabulário básico: cores, números, família, dias da semana. \\newline
Estruturas gramaticais básicas: verbos no presente, pronomes pessoais, artigos definidos e indefinidos. \\newline
Interculturalidade: costumes e tradições em países de língua espanhola. \\newline
Comunicação em situações cotidianas: compras, restaurantes, transportes. \\newline
Abordagem de Temáticas Transversais: Discussão sobre cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas com uso de recursos audiovisuais (vídeos, áudios) e atividades práticas (diálogos, role-playing). Estratégias de ensino colaborativo, promovendo discussões interculturais e resolução de problemas. Em caso de carga horária EAD: utilização exclusiva do Ambiente Virtual de Aprendizagem Moodle, com livros digitais, fóruns de discussão, quizzes e vídeo-aulas. As interações síncronas serão realizadas via videoconferências e fóruns de debate, com encontros presenciais agendados para avaliações orais e escritas. Tutoria no AVA realizada pelo docente da UC. Sem divisão de turma. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FANJUL, Adrián (org.). \\textbf{Gramática y práctica de español para brasileños}. 2. ed. São Paulo: Moderna, 2011. 287 p. ISBN 9788516074272. \\newline
MORENO, Concha; TUTS, Martina. \\textbf{Cinco estrellas}: español para el turismo. 2. ed. Madrid: SGEL, 2011. 223 p. ISBN 9788497784849.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BALLESTERO-ALVAREZ, M. E.; BALBÁS, M. S. \\textbf{Minidicionário}: espanhol-português, português-espanhol. São Paulo: FTD, 2007. \\newline
GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar}: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p. ISBN 9788477117186. \\newline
HERMOSO, A. G. \\textbf{Conjugar es fácil}. Madrid: Edelsa, 1997. \\newline
PEREZ, Aquilino Sanches. \\textbf{Diccionario básico de la lengua española}. Madrid: SGEL, 1987.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[5] = t5

    # -------------------------------------------------------------
    # 6. TABELA 6: Biologia — Ano 1
    # -------------------------------------------------------------
    t6 = """% ---------------------------------------------------------
% TABELA EMENTA 6: Biologia — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Biologia — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender a Biologia como uma ciência em permanente construção, reconhecendo sua importância para o entendimento da origem, evolução e diversificação da vida, bem como sua relação com o desenvolvimento científico, tecnológico e social.
    \\item Reconhecer a célula como unidade estrutural, funcional e genética dos seres vivos, compreendendo a organização celular, os processos metabólicos e os mecanismos envolvidos na manutenção da vida.
    \\item Entender os processos de multiplicação celular, reprodução sexuada e anatomofisiologia do corpo humano, relacionando-os à continuidade da vida, à diversidade genética e à saúde humana.
    \\item Desenvolver habilidades de observação, investigação e experimentação, utilizando procedimentos próprios das ciências biológicas para formular hipóteses, analisar evidências, interpretar resultados e resolver problemas.
    \\item Promover o autocuidado, o empoderamento e o respeito à pluralidade de corpos e gêneros por meio da compreensão dos princípios da educação alimentar e nutricional, da saúde integral e da sexualidade na adolescência.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Origem da vida: teorias e descobertas recentes. \\newline
Astrobiologia. \\newline
A invenção do microscópio e a descoberta da célula. \\newline
Células procarióticas e eucarióticas (animais e vegetais). \\newline
Componentes químicos celulares: água, macromoléculas, vitaminas e sais minerais. \\newline
Educação Alimentar e Nutricional. \\newline
Estrutura e funcionamento celular: membrana plasmática, citoplasma, organelas citoplasmáticas, citoesqueleto e núcleo. \\newline
Metabolismo energético: respiração celular, fermentação, fotossíntese e quimiossíntese. \\newline
Ciclo celular: interfase e divisão celular (mitose e meiose). \\newline
Reprodução animal: fecundação e desenvolvimento embrionário. \\newline
Histologia, anatomia e fisiologia humana: tecidos básicos e sistemas orgânicos. \\newline
Saúde e sexualidade na adolescência.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} O processo de ensino-aprendizagem será conduzido por meio de uma abordagem dialógica, contextualizada e investigativa, buscando o levantamento dos saberes prévios dos estudantes, a problematização de situações reais, a articulação com outras áreas do conhecimento e o desenvolvimento do pensamento crítico e científico. Metodologia baseada em estratégias didáticas diversificadas: aulas expositivo-dialogadas utilizando quadro e projetor multimídia; atividades práticas em campo e laboratório; análise de experimentos e estudos de caso; discussão de textos, imagens e vídeos científicos; uso de atlas digitais, softwares de animação e simulação, modelos didáticos tridimensionais e jogos educativos; debate de temas transversais; e participação em visitas técnicas e eventos científicos. As aulas práticas serão realizadas preferencialmente no pátio do câmpus e no Laboratório de Biociências, compondo uma média de 20h anuais, divididas em 10h para cada semestre letivo. Caso houver um segundo professor ministrante da UC, a turma poderá ser dividida em A e B, considerando a capacidade do espaço e a dinâmica da atividade proposta. O SIGAA será empregado como AVA para disponibilização de plano de ensino, cronograma de conteúdos e atividades, materiais de apoio, tarefas avaliativas, orientações e acompanhamento da frequência e do desempenho escolar. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação da aprendizagem se dará em uma perspectiva processual e formativa, observando-se a evolução dos conhecimentos construídos ao longo do período letivo. Os instrumentos avaliativos serão aplicados de forma individual ou coletiva, podendo ser: estudos dirigidos; listas de exercícios focados em ENEM e vestibulares; provas teóricas; relatórios de atividades experimentais; projetos, seminários ou oficinas temáticas; e avaliação atitudinal.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{JUNQUEIRA, Luiz Carlos Uchoa; CARNEIRO, José. \\textbf{Biologia celular e molecular}. 9. ed. Rio de Janeiro: Guanabara Koogan, 2012. 364 p. ISBN 9788527720786. \\newline
Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
SADAVA, David \\textit{et al.} \\textbf{Vida}: a ciência da biologia: volume 1: célula e hereditariedade. 8. ed. Porto Alegre: Artmed, 2009. 461 p. ISBN 9788536319216.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BRUCE, Alberts \\textit{et al.} \\textbf{Biologia molecular da célula}. 6. ed. Porto Alegre: Artmed, 2017. 1427 p. ISBN 9788582714225. \\newline
CAMPBELL, Mary K.; FARRELL, Shawn O. \\textbf{Bioquímica}. 2. ed. São Paulo: Cengage Learning, 2016. 812 p. ISBN 9788522118700. \\newline
KIERSZENBAUM, Abraham L.; TRES, Laura L. \\textbf{Histologia e biologia celular}: uma introdução à patologia. 3. ed. Rio de Janeiro: Elsevier, 2012. 699 p. ISBN 9788535247374.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[6] = t6

    # -------------------------------------------------------------
    # 7. TABELA 7: Física — Ano 1
    # -------------------------------------------------------------
    t7 = """% ---------------------------------------------------------
% TABELA EMENTA 7: Física — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Física — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender a Física como ciência, reconhecendo sua evolução histórica, seus principais ramos e sua importância para a compreensão dos fenômenos naturais e para o desenvolvimento científico e tecnológico.
    \\item Identificar e utilizar corretamente as grandezas físicas fundamentais e derivadas, bem como o Sistema Internacional de Unidades (SI) e suas conversões.
    \\item Desenvolver a capacidade de interpretar fenômenos físicos por meio da linguagem matemática, da análise de gráficos, tabelas e relações entre grandezas.
    \\item Compreender os conceitos fundamentais da Cinemática, descrevendo e analisando o movimento de corpos em diferentes referenciais.
    \\item Aplicar as equações do Movimento Uniforme (MU) e do Movimento Uniformemente Variado (MUV) na resolução de problemas envolvendo deslocamento, velocidade e aceleração.
    \\item Interpretar e construir gráficos de posição, velocidade e aceleração em função do tempo, relacionando suas características aos diferentes tipos de movimento.
    \\item Compreender os conceitos fundamentais da Dinâmica, identificando as forças que atuam sobre um corpo e seus efeitos sobre o movimento.
    \\item Analisar e aplicar as Leis de Newton na interpretação e resolução de problemas relacionados ao equilíbrio e ao movimento de corpos.
    \\item Desenvolver o raciocínio lógico e quantitativo na resolução de problemas físicos, empregando estratégias adequadas, argumentação científica e interpretação dos resultados obtidos.
    \\item Relacionar os conceitos estudados com situações do cotidiano, reconhecendo a presença e a aplicação dos princípios da Mecânica em diferentes contextos científicos, tecnológicos e sociais.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Introdução à Física: a origem da Física, as áreas da Física, grandezas físicas e unidades de medidas. \\newline
Noções básicas de Cinemática. \\newline
Movimento Uniforme e Movimento Uniformemente Variado. \\newline
Dinâmica (introdução). \\newline
Leis de Newton e suas aplicações.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas e dialogadas, sob a perspectiva de uma proposta dialógico-problematizadora a partir de fenômenos naturais, tecnológicos e produtivos do mundo do trabalho. A prática docente será pautada em três momentos pedagógicos: problematização inicial, organização e aplicação dos conhecimentos. Conteúdos tratados de forma contextualizada e interdisciplinar, com resolução de listas de exercícios e problemas. Procedimentos didático-metodológicos: exposição de vídeos; seminários; trabalhos de pesquisa; montagem e apresentação de experimentos; elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica; desenvolvimento de projetos; interpretação de textos técnicos e científicos. Recursos utilizados: livros didáticos e digitais, listas de exercícios, apostilas, lousa, projetor multimídia, computador, equipamentos de laboratório, textos e artigos acadêmicos da área, reproduções de imagens e vídeos da área. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação se dará em uma perspectiva formativa levando em conta todas as atividades realizadas pelos estudantes.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{HEWITT, Paul G. \\textbf{Física conceitual}. 12. ed. Porto Alegre: Bookman, 2015. \\newline
Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
LUZ, Antônio Máximo Ribeiro da; ALVARENGA, Beatriz Gonçalves de. \\textbf{Curso de física}, volume 1. 6. ed. rev. ampl. São Paulo: Scipione, 2006.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BARRETO FILHO, Benigno; SILVA, Cláudio Xavier da. \\textbf{360º}: física: aula por aula: volume único. 3. ed. São Paulo: FTD, 2015. \\newline
KNIGHT, Randall D. \\textbf{Física}: uma abordagem estratégica: volume 1: mecânica newtoniana, gravitação, oscilações e ondas. Tradução de Trieste Freire Ricci. 2. ed. Porto Alegre: Bookman, 2009. \\newline
YAMAMOTO, Kazuhito; FUKE, Luiz Felipe. \\textbf{Física para o ensino médio 1}: mecânica. 3. ed. São Paulo: Saraiva, 2013.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[7] = t7

    # -------------------------------------------------------------
    # 8. TABELA 8: Matemática — Ano 1
    # -------------------------------------------------------------
    t8 = """% ---------------------------------------------------------
% TABELA EMENTA 8: Matemática — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Matemática — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender e utilizar adequadamente a linguagem matemática na resolução de problemas, relacionando-a ao contexto da área de Administração.
    \\item Analisar, interpretar e utilizar os conhecimentos elencados pela disciplina na resolução de problemas relacionados à área de Administração.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\textbf{Parte I - Fundamentos:} Potenciação: definição, propriedades da potenciação, potências com expoentes fracionários. Radiciação: definição, propriedades dos radicais, simplificação de radicais, radicais com radicandos reais, racionalização, equações com radicais, gráficos de funções com radicais e aplicação da radiciação. Conjuntos numéricos: definição de conjunto dos naturais, inteiros, racionais, irracionais e reais, suas operações e propriedades. Propriedades gerais (identidade, inversos e distributividade). Conversão entre números decimais e frações. Diferença entre dízimas periódicas e não periódicas. Equações do 1º grau: definição e resolução com coeficientes e raízes reais. Equações do 2º grau: definição e resolução com coeficientes e raízes reais. Sistemas lineares 2x2: definição de sistemas lineares e sistemas não lineares, método da adição e substituição. \\newline
\\textbf{Parte II - Matemática Ensino Médio:} Conjuntos: conceitos e operações (união, intersecção, diferença e complementar), problemas envolvendo conjuntos, diagrama de Venn. Funções: definição, crescimento e decrescimento, domínio, contradomínio e imagem, função aplicada num ponto. Função afim: definição, gráfico, coeficientes angular e linear, propriedades e aplicações. Função quadrática: definição, gráfico, vértice, raízes (zero da função), interceptos vertical e horizontal, concavidade e aplicações. Teorema de Pitágoras, razões trigonométricas e aplicações. Noções de estatística: coleta de dados, variáveis, construção de tabelas e gráficos, distribuição de frequência, médias estatísticas (aritmética e ponderada), mediana, moda e desvio padrão.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas dialogadas; aulas de exercícios; apresentação em linguagem verbal, por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem; experimentação no ensino de matemática; produção de vídeos de matemática por estudantes. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Avaliações qualitativas e quantitativas processuais durante o semestre letivo.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BONJORNO, José Roberto; GIOVANNI JÚNIOR, José Ruy; GIOVANNI, José Ruy. \\textbf{Matemática fundamental}: uma nova abordagem: ensino médio: 1° ano. 3. ed. São Paulo: FTD, 2013. 560 p. \\newline
DANTE, Luiz Roberto. \\textbf{Projeto Múltiplo}: matemática: ensino médio: 1° ano. São Paulo: Ática, 2014. 240 p. \\newline
GIOVANNI, José Ruy; GIOVANNI JÚNIOR, José Ruy; BONJORNO, José Roberto; SOUZA, Paulo Roberto C. \\textbf{360º matemática fundamental}: uma nova abordagem: parte I, II, III, volume único. 2. ed. São Paulo: FTD, 2015. 283 p.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{LIMA, E. L.; CARVALHO, Paulo Cesar P. \\textbf{A Matemática do ensino médio}: volume único. 7. ed. Rio de Janeiro: SBM, 2016. v. 2. \\newline
PAIVA, Manoel. \\textbf{Matemática}: Paiva: 1º ano. 2. ed. São Paulo: Moderna, 2013. 304 p.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[8] = t8

    # -------------------------------------------------------------
    # 9. TABELA 9: Química — Ano 1
    # -------------------------------------------------------------
    t9 = """% ---------------------------------------------------------
% TABELA EMENTA 9: Química — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Química — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Estabelecer relações entre os conhecimentos sobre a matéria, sua constituição e suas transformações com situações do contexto social, tecnológico, ambiental e profissional, contribuindo para a formação integral dos estudantes.
    \\item Compreender a Química como ciência, reconhecendo sua importância para a compreensão dos fenômenos naturais, para o desenvolvimento científico e tecnológico e para os processos produtivos.
    \\item Identificar as propriedades da matéria, distinguindo substâncias puras e misturas e reconhecendo os principais métodos de separação empregados no cotidiano, na indústria e na preservação ambiental.
    \\item Compreender a evolução dos modelos atômicos, reconhecendo sua importância para a construção do conhecimento científico e para o entendimento da estrutura da matéria.
    \\item Identificar a estrutura do átomo, relacionando partículas subatômicas, distribuição eletrônica e propriedades dos elementos químicos.
    \\item Interpretar a organização da Tabela Periódica, correlacionando a posição dos elementos às suas propriedades periódicas e às suas aplicações no cotidiano.
    \\item Compreender a formação das ligações químicas, relacionando os diferentes tipos de ligação às propriedades das substâncias e aos materiais presentes no cotidiano.
    \\item Reconhecer a geometria molecular e sua influência nas propriedades das substâncias, relacionando a polaridade das moléculas ao seu comportamento físico e químico.
    \\item Identificar as forças intermoleculares, compreendendo sua influência nas propriedades macroscópicas dos materiais e em fenômenos observados na natureza e nas atividades humanas.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Química: objeto de estudo, aplicações e importância para a sociedade, o meio ambiente e os processos produtivos. \\newline
Matéria: propriedades, estados físicos, substâncias puras e misturas. \\newline
Processos de separação de misturas. \\newline
Modelos atômicos e Estrutura atômica. \\newline
Tabela periódica. \\newline
Ligações químicas. \\newline
Geometria molecular e Forças intermoleculares.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas dialogadas; resolução de exercícios; estudos dirigidos; modelos didáticos e representações da matéria; jogos didáticos; vídeos; simulação e animação; atividades experimentais no Laboratório de Química (propriedades da matéria, separação de misturas e identificação de substâncias); atividades investigativas que favoreçam a compreensão dos modelos explicativos da Química. SIGAA empregado como AVA. Nas atividades práticas de laboratório, as turmas poderão ser divididas em subgrupos, respeitando as normas de segurança e a capacidade do espaço. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Acompanhamento contínuo e processual: relatórios de práticas laboratoriais, listas de exercícios, estudos dirigidos, seminários, participação, produções individuais/coletivas e avaliações individuais escritas.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{CHANG, Raymond. \\textbf{Química geral}: conceitos essenciais. Tradução de Maria José Ferreira Rebelo. 4. ed. Porto Alegre: AMGH, 2010. 778 p. ISBN 9788563308047. \\newline
FELTRE, Ricardo. \\textbf{Química 1}: química geral. Colaboração de Ricardo Arissa Feltre. 7. ed. São Paulo: Moderna, 2008. v. 1. 527 p. ISBN 9788516061111. \\newline
FRANCO, Dalton. \\textbf{360º}: química: cotidiano e transformações: volume único. São Paulo: FTD, 2015. 3 v. ISBN 9788596001113. \\newline
PERUZZO, Francisco Miragaia; CANTO, Eduardo Leite do. \\textbf{Química na abordagem do cotidiano}: volume único. 3. ed. São Paulo: Moderna, 2007. 760 p. ISBN 9788516056612.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ATKINS, P. W.; JONES, Loretta. \\textbf{Princípios de química}: questionando a vida moderna e o meio ambiente. Tradução de Ricardo Bicca de Alencastro. 5. ed. Porto Alegre: Bookman, 2012. 922 p. ISBN 9788540700383. \\newline
BRADY, James E.; HUMISTON, Gerard E. \\textbf{Química geral}. 2. ed. Rio de Janeiro: LTC, 2011. v. 1. 424 p. ISBN 9788521604488. \\newline
USBERCO, João; SALVADOR, Edgard. \\textbf{Química}: volume único. 5. ed. reform. São Paulo: Saraiva, 2002. 672 p. ISBN 8502040278.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[9] = t9

    # -------------------------------------------------------------
    # 10. TABELA 10: Filosofia — Ano 1
    # -------------------------------------------------------------
    t10 = """% ---------------------------------------------------------
% TABELA EMENTA 10: Filosofia — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Filosofia — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Conhecer a origem da Filosofia, os campos de investigação da Filosofia e os períodos da história da Filosofia.
    \\item Estimular os primeiros contatos com a tradição filosófica e com a abstração conceitual típica da filosofia.
    \\item Adquirir conhecimentos sobre a estrutura do pensamento metafísico através da história da Filosofia.
    \\item Conhecer aspectos gerais da filosofia dos pré-socráticos, Sócrates e Platão.
    \\item Conhecer aspectos gerais da filosofia de Aristóteles.
    \\item Conhecer as escolas filosóficas inerentes ao período helenístico.
    \\item Relacionar os conteúdos analisados em sala de aula aos mais distintos aspectos da vida contemporânea.
    \\item Promover a troca de ideias e, por conseguinte, o respeito às distintas visões de mundo presentes na sala de aula.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
O que é o Mito? Passagem do Mito à Filosofia. \\newline
Conceitos de Filosofia: o que é Filosofia e para que serve. \\newline
Filosofia e as outras formas de conhecimento. \\newline
A Razão: regras e princípios. As concepções de verdade -- Dogmatismo e busca da verdade. \\newline
Períodos da História da Filosofia. \\newline
Filosofia Antiga: A Filosofia grega e os pré-socráticos; Os sofistas; Sócrates e a busca pela verdade; Platão e o mito da caverna; O amor a partir de Platão; As cavernas contemporâneas; Aristóteles, ética e política; O homem como animal social; As virtudes e a moderação; A prudência; A coragem. \\newline
As escolas helenísticas: O estoicismo e a arte de bem viver; O epicurismo e o prazer; O ceticismo e o conhecimento; O cinismo e o cosmopolitismo.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas, leituras interpretativas e críticas, seminários e apresentações individuais e/ou em grupo de alunos, pesquisa bibliográfica, produção de textos. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação seguirá o caminho processual com notas de 0 a 10 e considerará: participação dos alunos nas atividades propostas pelo professor; trabalho de pesquisa individual e coletiva e prova escrita. Realização de dois momentos avaliativos formais durante o semestre, considerando que estes momentos não contemplarão a totalidade da nota, mas serão tomados como parte do processo integral da relação ensino-aprendizagem.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ARANHA, M. L. A.; MARTINS, M. H. P. \\textbf{Filosofando}: introdução à filosofia. São Paulo: Moderna, 1993. \\newline
CHAUÍ, Marilena. \\textbf{Convite à filosofia}. 13. ed. São Paulo: Ática, 2009.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{GAARDER, Jostein. \\textbf{O mundo de Sofia}: romance da história da filosofia. São Paulo: Seguinte, 2012. \\newline
MARCONDES, Danilo. \\textbf{Textos básicos de filosofia}: dos pré-socráticos a Wittgenstein. Rio de Janeiro: Jorge Zahar, 2000.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[10] = t10

    # -------------------------------------------------------------
    # 12. TABELA 12: Sociologia — Ano 1
    # -------------------------------------------------------------
    t12 = """% ---------------------------------------------------------
% TABELA EMENTA 12: Sociologia — Ano 1
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Sociologia — Ano 1}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º e 2º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Analisar os diferentes discursos sobre a realidade: as explicações das Ciências Sociais amparadas nos vários paradigmas teóricos.
    \\item Compreender as transformações que ocorrem nas sociedades humanas.
    \\item Evidenciar a relação entre as questões individuais e as questões sociais.
    \\item Formular questionamentos que permitam alcançar um conhecimento mais preciso da sociedade e uma postura crítica em relação às vivências que nos condicionam e limitam.
    \\item Entender o processo de constituição, consolidação e desenvolvimento das sociedades modernas.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
As Ciências Sociais e o objeto de estudo da Sociologia. \\newline
Contexto de surgimento da Sociologia. \\newline
Relação indivíduo/sociedade. \\newline
Socialização e Instituições Sociais. \\newline
Clássicos das Ciências Sociais. \\newline
Cidadania e Direitos Humanos. \\newline
Cultura e Ideologia; Cultura do ponto de vista antropológico. \\newline
Multiculturalismo, identidade e diferenças culturais. \\newline
Cultura dominante e Indústria cultural; Subcultura e tribos urbanas.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Leitura, análise, discussão e exposição de textos e imagens em sala de aula, visando o exercício do debate e da reflexão crítica sobre os temas e conceitos estudados; aulas expositivas e dialogadas; recursos didático-pedagógicos como filmes, seminários, documentários e entrevistas; estímulo à autonomia investigativa e socialização de temas relacionados ao programa curricular. Recursos didáticos: textos (livros, apostilas, artigos, estudos de caso, etc.); quadro e pincel; recursos audiovisuais (filmes, séries, música, pesquisas, arte); equipamentos de informática (computador, Internet, projetor multimídia). \\newline\\vspace{2pt}
\\textbf{Avaliação:} Avaliação contínua e formativa através de trabalhos individuais e em grupo, debates e produções textuais.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
OLIVEIRA, Pérsio Santos de. \\textbf{Introdução à Sociologia}: Série Brasil. São Paulo: Editora Ática, 2011.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{COSTA, Maria Cristina. \\textbf{Sociologia}: introdução à ciência da sociedade. 5. ed. São Paulo: Editora Moderna, 2016. \\newline
HELENA, Bomeny \\textit{et al.} \\textbf{Tempos Modernos, tempos de sociologia}. 4. ed. São Paulo: Ed. do Brasil, 2016. \\newline
OLIVEIRA, Luiz Fernandes de; COSTA, Ricardo Cesar Rocha da. \\textbf{Sociologia para jovens do século XXI}. Rio de Janeiro: Imperial Novo Milênio, 2013.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[12] = t12

    # -------------------------------------------------------------
    # 13. TABELA 13: Introdução à Administração
    # -------------------------------------------------------------
    t13 = """% ---------------------------------------------------------
% TABELA EMENTA 13: Introdução à Administração
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Introdução à Administração}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender o papel da Administração nas organizações e sua evolução histórica, relacionando as principais teorias administrativas às transformações econômicas, tecnológicas e organizacionais da sociedade contemporânea.
    \\item Reconhecer o perfil profissional, as competências e os campos de atuação do Técnico em Administração.
    \\item Diferenciar os tipos de organizações quanto às suas finalidades, estruturas e formas de gestão, considerando os fatores do ambiente interno e externo que influenciam seu funcionamento.
    \\item Identificar as funções administrativas, os níveis organizacionais e a estrutura hierárquica em sua aplicação nas rotinas de trabalho.
    \\item Reconhecer tendências contemporâneas que impactam as organizações e a prática administrativa.
    \\item Compreender as etapas básicas do processo decisório na identificação de problemas em situações organizacionais.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Conceito, importância e campo de atuação da Administração. \\newline
Perfil profissional, competências e áreas de atuação do Técnico em Administração. \\newline
Organizações: conceitos, tipos, objetivos, recursos e classificação. \\newline
Ambiente organizacional: fatores internos e externos. \\newline
Estrutura organizacional, níveis hierárquicos e papéis gerenciais. \\newline
Evolução das teorias administrativas. \\newline
Funções administrativas: planejamento, organização, direção e controle. \\newline
Tendências contemporâneas em administração. \\newline
Processo decisório nas organizações: etapas básicas e sua relação com as funções administrativas.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Metodologias ativas de aprendizagem articuladas a aulas expositivas dialogadas. As atividades poderão contemplar estudos de caso, exercícios, provas, simulações, dinâmicas de grupos, jogos, seminários, participação em debates, análise de filmes, esquetes teatrais, relatórios, atividades reflexivas, autoavaliações, rodas de conversa com profissionais da área, além de visitas técnicas e outras práticas que favoreçam a articulação entre teoria e prática. Espaços do Câmpus utilizados: sala de aula, biblioteca, sala multidisciplinar, centro multiuso e laboratório de informática. Por ser basilar, articula-se com as demais UCs da formação profissional e com Sociologia, Sociedade e Trabalho, Língua Portuguesa, História e Geografia, abordando temáticas como transformações do mundo do trabalho, ética nas relações trabalhistas e modos de produção. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação será contínua, processual e formativa, acompanhando o desenvolvimento dos estudantes por meio de participação, envolvimento e instrumentos individuais e coletivos.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{DIAS, Reinaldo; ZAVAGLIA, Tércia; CASSAR, Maurício. \\textbf{Introdução à administração}: da competitividade à sustentabilidade. 3. ed. rev. Campinas, SP: Alínea, 2013. 250 p. ISBN 9788575166659. \\newline
MAXIMIANO, Antonio Cesar Amaru. \\textbf{Introdução à administração}. 8. ed. rev. e ampl. São Paulo: Atlas, 2011. 419 p. ISBN 9788522462889.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{CHIAVENATO, Idalberto. \\textbf{Administração nos novos tempos}. 2. ed. rev. e atual. Rio de Janeiro: Elsevier, 2010. 610 p. ISBN 9788535237719. \\newline
LACOMBE, Francisco José Masset; HEILBORN, Gilberto Luiz José. \\textbf{Administração}: princípios e tendências. 3. ed. São Paulo: Saraiva, 2015. 545 p. ISBN 9788502634480. \\newline
NASCIMENTO, Edson Ronaldo. \\textbf{Gestão Pública}. São Paulo: Saraiva, 2010.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[13] = t13

    # -------------------------------------------------------------
    # 14. TABELA 14: Sociedade e Trabalho
    # -------------------------------------------------------------
    t14 = """% ---------------------------------------------------------
% TABELA EMENTA 14: Sociedade e Trabalho
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Sociedade e Trabalho}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{1º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{40 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender as transformações que ocorrem nas sociedades humanas e sua relação com o trabalho.
    \\item Evidenciar a relação entre as questões individuais e as questões sociais.
    \\item Formular questionamentos que permitam alcançar um conhecimento mais preciso da sociedade e do trabalho, possibilitando a construção de uma postura crítica em relação às vivências que nos condicionam e limitam.
    \\item Entender o processo de constituição, consolidação e desenvolvimento das sociedades modernas e a importância do trabalho na dinâmica de funcionamento das sociedades.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
O que é Trabalho; História do Trabalho. \\newline
Revolução Industrial e Trabalho assalariado. \\newline
Trabalho nas sociedades modernas; Formas de organização do mundo do Trabalho. \\newline
Trabalho e Sociedade no Brasil: da escravidão ao trabalho livre; O trabalho no Brasil contemporâneo. \\newline
O Mundo do Trabalho contemporâneo: novas formas de trabalho; Precarização do Trabalho. \\newline
Desafios do mundo do trabalho na atualidade: inteligência artificial e impactos no emprego.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas e dialogadas; leitura e discussão de textos e imagens; seminários, documentários, debates e entrevistas; estímulo à autonomia investigativa. Recursos: textos, quadro, filmes, pesquisas e ferramentas de informática. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Acompanhamento contínuo e formativo mediante participação em debates, seminários, estudos de caso e trabalhos individuais/coletivos.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ANTUNES, Ricardo. \\textbf{Os sentidos do trabalho}: ensaio sobre a afirmação e a negação do trabalho. 2. ed. São Paulo: Boitempo, 2009. \\newline
DE MASI, Domenico. \\textbf{O futuro do trabalho}: fadiga e ócio na sociedade pós-industrial. 5. ed. Rio de Janeiro: José Olympio, 2001. \\newline
OLIVEIRA, Pérsio Santos de. \\textbf{Introdução à Sociologia}: Série Brasil. São Paulo: Ática, 2011.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{GORZ, André. \\textbf{Metamorfoses do trabalho}: crítica da razão econômica. São Paulo: Annablume, 2003. \\newline
KONDER, Leandro. \\textbf{O futuro da filosofia da práxis}. Rio de Janeiro: Paz e Terra, 1992. \\newline
MARX, Karl. \\textbf{O capital}: crítica da economia política: Livro I. São Paulo: Boitempo, 2013.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[14] = t14

    # -------------------------------------------------------------
    # 15. TABELA 15: Gestão de Marketing I (SUBSTITUIÇÃO INTEGRAL)
    # -------------------------------------------------------------
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
    \\item Compreender os fundamentos do marketing e sua importância na criação, comunicação e entrega de valor para clientes e organizações.
    \\item Identificar características do mercado e dos consumidores que influenciam as decisões de marketing das organizações.
    \\item Aplicar conceitos e ferramentas básicas de marketing nas decisões relacionadas ao composto de marketing, considerando a perspectiva da organização e do consumidor.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Conceito e papel do marketing. \\newline
Necessidades, desejo, demanda e criação de valor. \\newline
Ambiente de marketing. \\newline
Comportamento do consumidor e processo de decisão de compra. \\newline
Segmentação do mercado. \\newline
Composto de marketing e sua evolução: 4Ps e abordagens contemporâneas orientadas ao cliente.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, articulando os fundamentos conceituais do marketing a situações práticas e contextualizadas. Poderão ser desenvolvidos estudos de caso, resolução de problemas, análise do comportamento do consumidor, análise de organizações, atividades de observação do mercado, oficinas práticas e simulações. As atividades buscarão promover a compreensão e a aplicação dos conceitos de marketing em diferentes contextos organizacionais, considerando as transformações no comportamento do consumidor, nos mercados, nas tecnologias e nas formas de criação, comunicação e entrega de valor, preferencialmente relacionadas à realidade do território. Entre os espaços físicos, a unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar e centro multiuso, podendo também desenvolver atividades de observação e pesquisa em organizações e em outros espaços da comunidade. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular e a progressão das aprendizagens. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo, estudos de caso, resolução de problemas, relatórios, produções gráficas e digitais, apresentações, projetos, portfólios, autoavaliação, avaliação por pares e avaliações escritas, quando pertinentes. \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} A unidade curricular buscará estabelecer conexões com outros componentes curriculares, especialmente Língua Portuguesa, Língua Inglesa e Língua Espanhola, nos processos de comunicação e produção de conteúdos; Artes, nos aspectos relacionados à criatividade, linguagem visual e comunicação; e Sociologia e Filosofia, na análise crítica das relações entre consumo, sociedade, ética, cultura e comportamento.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{KOTLER, Philip; KELLER, Kevin Lane. \\textbf{Administração de marketing}. 12. ed. 5. reimp. São Paulo: Pearson Prentice Hall, 2010. \\newline
LAS CASAS, Alexandre Luzzi. \\textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ARBACHE, Fernando Saba. \\textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \\newline
DANTAS, Edmundo Brandão. \\textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \\newline
KOTLER, Philip; ARMSTRONG, Gary. \\textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \\newline
LAS CASAS, Alexandre Luzzi. \\textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[15] = t15

    # -------------------------------------------------------------
    # 18. TABELA 18: Artes — Ano 2
    # -------------------------------------------------------------
    t18 = """% ---------------------------------------------------------
% TABELA EMENTA 18: Artes — Ano 2
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Artes — Ano 2}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{3º e 4º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Refletir sobre os conceitos básicos dos fenômenos artísticos ocidentais e suas relações com outras formas de pensamento.
    \\item Analisar o uso de manifestações tradicionais brasileiras como constituintes de saberes, territórios e identidades.
    \\item Vivenciar práticas corporais tradicionais.
    \\item Experienciar e criar nas diferentes linguagens da arte do corpo em cena (dança, teatro e performance).
    \\item Valorizar a diversidade cultural brasileira.
    \\item Analisar o papel da arte como ferramenta de denúncia e conscientização.
    \\item Refletir sobre a relação entre arte, política, ciência, tecnologia e meio ambiente.
    \\item Estabelecer diálogos entre a arte contemporânea e os saberes tradicionais.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Manifestações populares e tradicionais no Brasil. \\newline
Cultura indígena, afro-brasileira e africana. \\newline
Artivismo. \\newline
Abordagens em arte contra a hegemonia, em diálogo com os saberes e as tradições decoloniais. \\newline
Práticas de movimentos, passos e técnicas em dança e teatro. \\newline
Estudo teórico-prático de técnicas de improvisação em dança e teatro. \\newline
Panorama histórico da dança e do teatro no Brasil. \\newline
Pesquisa, elaboração de ideias, criação, produção e apresentação de obras em artes do corpo em cena. \\newline
Improvisação e criação coletiva.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas participativas e dialogadas, partindo do conhecimento prévio do estudante, utilizando imagens, textos, vídeos, músicas e corpo; atividades focadas na indissociabilidade entre teoria e prática, com atividades corporais; desenvolvimento de trabalhos, exercícios, pesquisas, seminários e obras artísticas; atividades individuais e em grupos; jogos teatrais e exercícios de improvisação; práticas de dança contemporânea e danças tradicionais brasileiras; utilização da sala de artes para atividades práticas. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Não especificado no documento fonte.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{CONDURU, Roberto. \\textbf{Arte afro-brasileira}. Belo Horizonte: C/Arte, 2007. 126 p. ISBN 9788576540472. \\newline
GOMBRICH, E. H. \\textbf{A história da arte}. Tradução de Álvaro Cabral. 16. ed. Rio de Janeiro: Livros Técnicos e Científicos, 1999. 688 p. ISBN 9788521611851. \\newline
PROENÇA, G. \\textbf{História da arte}. 17. ed. São Paulo: Ática, 2010.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{MACHADO, Lúcia. \\textbf{A modernidade no teatro}: [ali e aqui]: reflexos estilhaçados. Recife: Ed. do autor, 2009. 450 p. ISBN 9788591007806. \\newline
NILSON, Afonso. \\textbf{Seis textos breves para estudantes de teatro}. Florianópolis: Letras Contemporâneas, 2017. 71 p. ISBN 9788594445001. \\newline
PIMENTEL, Spency. \\textbf{O índio que mora na nossa cabeça}: sobre as dificuldades para entender os povos indígenas. São Paulo: Prumo, 2012. 88 p. ISBN 9788579272486. \\newline
SANT'ANNA, Márcia (org.). \\textbf{Os sambas brasileiros}: diversidade, apropriação e salvaguarda. Brasília, DF: IPHAN, 2011. 144 p. ISBN 9788573341911.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[18] = t18

    # -------------------------------------------------------------
    # 19. TABELA 19: Educação Física — Ano 2 (Expand 19 literal objectives)
    # -------------------------------------------------------------
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
    \\item Compreender a cultura corporal em suas diversas manifestações e dimensões, relacionando-a com os contextos históricos, sociais e culturais.
    \\item Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade contemporânea.
    \\item Analisar criticamente as representações sociais do corpo e do movimento, desconstruindo estereótipos e preconceitos.
    \\item Investigar a história e a evolução das práticas corporais, valorizando a diversidade cultural.
    \\item Refletir sobre a influência da mídia e do consumo nas práticas corporais.
    \\item Promover a sensibilização para a inclusão social através do esporte e do lazer, combatendo o preconceito e a discriminação.
    \\item Desenvolver projetos que promovam a inclusão de pessoas com deficiência, LGBTQIA+, idosos e outros grupos minoritários.
    \\item Analisar as políticas públicas de esporte e lazer e suas implicações sociais.
    \\item Desenvolver a capacidade de analisar criticamente as relações de poder presentes nas práticas corporais e no esporte.
    \\item Identificar as desigualdades sociais e as relações de gênero presentes no esporte e no lazer.
    \\item Refletir sobre o papel do esporte como instrumento de transformação social.
    \\item Desenvolver os estudantes técnicos capazes de atuar em diferentes contextos, utilizando as tecnologias digitais como ferramentas para o ensino e a gestão de projetos.
    \\item Desenvolver uma consciência crítica em relação ao meio ambiente e à sustentabilidade.
    \\item Promover a prática de atividades físicas ao ar livre e o contato com a natureza.
    \\item Incentivar a produção de eventos esportivos e de lazer sustentáveis.
    \\item Compreender a domesticação dos corpos marginalizados, como mulheres, pessoas negras, LGBTQIA+, e pessoas com deficiência, e os impactos dessa disciplina na ocupação dos espaços destinados ao lazer.
    \\item Analisar o impacto da vigilância e da moralização nos corpos que ocupam espaços de lazer, promovendo a identificação de práticas de exclusão e estigmatização.
    \\item Promover discussões interseccionais de gênero, raça e classe social e a domesticação dos corpos nos espaços de lazer.
    \\item Desenvolver práticas educacionais que fomentem o acesso igualitário ao lazer, subvertendo os mecanismos de exclusão e disciplinamento dos corpos.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\textbf{Lazer e tempo livre:} Lazer e tempo livre: conceitos, históricos e transformações; Políticas públicas de lazer e suas implicações sociais; Turismo e lazer: relações e perspectivas; Lazer e tecnologia: impactos e possibilidades. \\newline
\\textbf{Saúde, corpo e movimento:} Atividade física e saúde: evidências científicas; Alimentação e nutrição para o desempenho esportivo; Lesões esportivas: prevenção e tratamento; Saúde do trabalhador e ergonomia. \\newline
\\textbf{Cultura corporal e trabalho:} Trabalho e lazer: relações históricas e contemporâneas; Saúde do trabalhador e qualidade de vida. \\newline
\\textbf{Diversidade, gênero e inclusão:} Corpo, gênero e sexualidade na cultura corporal; Esporte e pessoas com deficiência; Racismo e discriminação no esporte; LGBTQIA+ e esporte. \\newline
\\textbf{Cultura corporal e suas relações sociais:} Danças populares e urbanas: história, significados e diversidade; Lutas e artes marciais: história, filosofia e valores; Esportes coletivos e individuais: regras, técnicas, táticas e valores; Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014. \\newline
BERNARDES, Luciano Andrade (org.). \\textbf{Atividades e esportes de aventura para profissionais de educação física}. São Paulo: Phorte, 2013.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BRACHT, Valter. \\textbf{Sociologia crítica do esporte}: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003. \\newline
CAMARGO, Wagner Xavier de. \\textbf{Leituras de gênero e sexualidade nos esportes}. São Carlos: EDUFSCAR, 2021. \\newline
FOER, Franklin. \\textbf{Como o futebol explica o mundo}: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[19] = t19

    # -------------------------------------------------------------
    # 20. TABELA 20: Inglês — Ano 2
    # -------------------------------------------------------------
    t20 = """% ---------------------------------------------------------
% TABELA EMENTA 20: Inglês — Ano 2
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Inglês — Ano 2}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{3º e 4º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Compreender a língua inglesa como língua franca e idioma universal, entendendo sua função social como possibilidade de ampliar o acesso à informação e a bens científicos e culturais da humanidade.
    \\item Ampliar de modo autônomo o conhecimento da língua inglesa a partir de estratégias de aprendizagem e compreensão, utilizando ferramentas convencionais e digitais.
    \\item Posicionar-se como usuário ativo da língua inglesa em diferentes cenários, vivenciando práticas de fala, escuta, escrita e de leitura.
    \\item Produzir sentido a partir de elementos linguísticos e extralinguísticos de gêneros textuais (orais, escritos e/ou híbridos), prioritariamente utilizando textos autênticos.
    \\item Conhecer regularidades morfológicas e sintáticas da língua inglesa que auxiliem na compreensão de significados e na ampliação de vocabulário.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Eventos e fatos passados: passado simples, contínuo e presente perfeito. \\newline
Preposições de tempo e lugar. \\newline
Futuro Simples e Futuro com Going to. \\newline
Conjunções (contraste, adição, conclusão, causa, finalidade) e Marcadores sequenciais. \\newline
Advérbios, formação de palavras, prefixos e sufixos. \\newline
Expressões idiomáticas, voz passiva, verbos frasais e gerúndio. \\newline
Verbos modais (can, should, must, would) e Condicionais.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas dialogadas e contextualizadas, buscando aproximação com o cotidiano dos estudantes; apresentação dos conteúdos trabalhados por meio da audição, conversação, leitura e produção de textos e/ou apresentações com recursos multimídia; projetos e atividades envolvendo gêneros textuais de natureza lúdica (música e vídeo), informativa (notícias e textos científicos), literárias (poemas e obras) e/ou técnica e científica; atividades que propiciem ao estudante a oportunidade de compartilhar conhecimento com os colegas.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
\\textbf{DICIONÁRIO Escolar Longman Inglês-Português, Português-Inglês}. Harlow: Pearson Longman, 2004. \\newline
LATHAM-KOENIG, C. \\textbf{English File}: Intermediate Student's Book. Oxford: Oxford University Press, 2018.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FRANCO, C. P. \\textbf{English vibes for Brazilian learners}: volume único. 1. ed. São Paulo: FTD, 2020. \\newline
MURPHY, Raymond. \\textbf{Essential Grammar in Use}. 4th ed. Cambridge: Cambridge University Press, 2015. \\newline
WHARTON, S. \\textbf{500 tips for tesol}: (teaching english to speakers of other languages). London: Kogan Page, 1999.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[20] = t20

    # -------------------------------------------------------------
    # 22. TABELA 22: Espanhol — Ano 2 (Docente Felix Medina)
    # -------------------------------------------------------------
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
    \\item Revisar e consolidar as estruturas gramaticais básicas da língua espanhola.
    \\item Compreender e aplicar tempos verbais no passado (pretérito perfeito e imperfeito).
    \\item Expandir o vocabulário em eixos temáticos específicos, tais como alimentos, roupas, lazer e clima.
    \\item Desenvolver habilidades de comunicação em situações de nível intermediário, capacitando para a descrição de pessoas, lugares e eventos.
    \\item Redigir textos breves e funcionais, como cartas e e-mails informais.
    \\item Analisar criticamente manifestações da cultura popular e celebrações hispânicas, articulando reflexões sobre direitos humanos, alimentação saudável e História e Cultura Afro-Brasileira e Indígena.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Revisão de estruturas gramaticais básicas. \\newline
Tempos verbais no passado: pretérito perfeito e imperfeito. \\newline
Vocabulário ampliado: alimentos, roupas, lazer, clima. \\newline
Interculturalidade: celebrações, festividades e cultura popular nos países hispanofalantes. \\newline
Comunicação em situações intermediárias: descrevendo pessoas, lugares e eventos. \\newline
Introdução à escrita de textos breves: cartas e e-mails informais. \\newline
Abordagem de Temáticas Transversais: História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões integradas sobre os direitos humanos.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Abordagem comunicativa com ênfase em situações da vida real, priorizando o uso prático do idioma por meio de simulações e diálogos. Uso de plataformas digitais para o desenvolvimento de atividades de escrita colaborativa e debates sobre temas culturais e transversais. Em caso de oferta de carga horária EAD: utilização exclusiva do Moodle, incorporando quizzes interativos, fóruns orientados e vídeo-aulas. Sessões síncronas via videoconferência para prática de fala e escrita, com momentos assíncronos e encontros presenciais opcionais para reforço e avaliações. Tutoria no AVA realizada diretamente pelo docente da UC. Sem divisão de turma. \\newline\\vspace{2pt}
\\textbf{Avaliação:} Avaliação diagnóstica, processual e formativa através de tarefas orais, produções escritas e testes de compreensão auditiva.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FANJUL, Adrián (org.). \\textbf{Gramática y práctica de español para brasileños}. 2. ed. São Paulo: Moderna, 2011. 287 p. ISBN 9788516074272. \\newline
MORENO, Concha; TUTS, Martina. \\textbf{Cinco estrellas}: español para el turismo. 2. ed. Madrid: SGEL, 2011. 223 p. ISBN 9788497784849.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{COTO BAUTISTA, Vanessa; TURZA FERRÉ, Anna. \\textbf{Tema a tema B1}: español lengua extranjera : curso de conversación. Madrid: Edelsa, 2011. 111 p. ISBN 9788477117209. \\newline
GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar}: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p. ISBN 9788477117186. \\newline
WILDNER, Ana Kaciara; OLIVEIRA, Leandra Cristina de; SOBOTTKA, Mary Anne Warken. \\textbf{Espanhol para o turismo}. Florianópolis: Publicação do IFSC, 2014.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[22] = t22

    # -------------------------------------------------------------
    # 29. TABELA 29: Gestão de Marketing II (SUBSTITUIÇÃO INTEGRAL)
    # -------------------------------------------------------------
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
    \\item Compreender os fundamentos do planejamento e das estratégias de marketing, reconhecendo a importância da pesquisa e das informações de mercado para a tomada de decisões.
    \\item Analisar práticas de posicionamento, marca, comunicação, vendas e relacionamento com clientes em diferentes contextos organizacionais.
    \\item Compreender as práticas de marketing digital e sua aplicação na comunicação e no relacionamento com os clientes.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Fundamentos do planejamento e das estratégias de marketing. \\newline
Pesquisa de marketing: etapas, coleta e análise básica de dados. \\newline
Posicionamento, marca e experiência do cliente. \\newline
Comunicação de marketing: comunicação integrada, marketing digital, mídias sociais e conteúdo. \\newline
Vendas, atendimento e relacionamento com o cliente. \\newline
Tecnologias e indicadores aplicados ao marketing: métricas básicas, dados e inteligência artificial.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, articulando os conhecimentos de marketing às situações práticas e contextualizadas. Poderão ser desenvolvidos estudos de caso, resolução de problemas, pesquisas de marketing, análise de organizações e marcas, oficinas práticas e atividades envolvendo comunicação, vendas, relacionamento com clientes e marketing digital. As atividades buscarão favorecer a compreensão e a aplicação dos conceitos estudados, por meio da análise de situações mercadológicas e da proposição de ações de marketing. Poderão ser utilizadas ferramentas digitais e de inteligência artificial como apoio às atividades, considerando aspectos éticos relacionados à sua utilização. Entre os espaços físicos, a unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar e centro multiuso, podendo também desenvolver atividades de observação e pesquisa em organizações e outros espaços da comunidade. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular e a progressão das aprendizagens. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo, estudos de caso, resolução de problemas, relatórios, produções gráficas e digitais, apresentações, projetos, portfólios, autoavaliação, avaliação por pares e avaliações escritas, quando pertinentes. \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} A unidade curricular buscará estabelecer conexões com outros componentes curriculares, especialmente Gestão de Marketing I, Língua Portuguesa, Língua Inglesa e Língua Espanhola, nos processos de comunicação e produção de conteúdos; Artes, nos aspectos relacionados à criatividade, linguagem visual e comunicação; e Sociologia e Filosofia, na análise crítica das relações entre consumo, sociedade, ética, cultura e comportamento.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{LAS CASAS, Alexandre Luzzi. \\textbf{Marketing Digital}. Rio de Janeiro: Atlas, 2021. \\newline
MATTAR, Fauze Najib. \\textbf{Pesquisa de marketing}. 4. ed. compacta 3. reimp. São Paulo: Atlas, 2007. \\newline
VIRGILLITO, Salvatore Benito (coord.). \\textbf{Pesquisa de marketing}: uma abordagem quantitativa e qualitativa. São Paulo: Saraiva, 2010.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ARBACHE, Fernando Saba. \\textbf{Gestão de logística, distribuição e trade marketing}. 4. ed. Rio de Janeiro: FGV Ed., 2011. \\newline
DANTAS, Edmundo Brandão. \\textbf{Atendimento ao público nas organizações}: quando o marketing de serviços mostra a cara. 5. ed. Brasília, DF: Senac-DF, 2011. \\newline
KOTLER, Philip; ARMSTRONG, Gary. \\textbf{Princípios de marketing}. Tradução de Sabrina Cairo. 15. ed. São Paulo: Pearson Education do Brasil, 2015. \\newline
LAS CASAS, Alexandre Luzzi. \\textbf{Marketing}: conceitos, exercícios, casos. 9. ed. São Paulo: Atlas, 2017.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[29] = t29

    # -------------------------------------------------------------
    # 31. TABELA 31: Empreendedorismo I (SUBSTITUIÇÃO INTEGRAL)
    # -------------------------------------------------------------
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
    \\item Compreender o conceito de empreendedorismo e suas diferentes manifestações no mundo contemporâneo.
    \\item Identificar características, comportamentos e competências associadas à atitude empreendedora e ao desenvolvimento pessoal e profissional.
    \\item Reconhecer experiências de economia solidária, cooperativismo e associativismo como formas alternativas de organização e geração de trabalho e renda.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Empreendedorismo e mundo do trabalho: conceitos, evolução histórica e contexto contemporâneo. \\newline
Diferentes formas de empreender: empreendedorismo tradicional, corporativo (intraempreendedorismo), social, digital, sustentável, cooperativismo, associativismo e economia solidária. \\newline
Comportamento e competências empreendedoras: criatividade, iniciativa, visão de oportunidade, planejamento, resolução de problemas, tomada de decisão, liderança, cooperação e responsabilidade social. \\newline
Inovação: conceitos, tipos e sua relação com o empreendedorismo. \\newline
Empreendedorismo e território: identificação de potenciais locais e regionais, demandas comunitárias e iniciativas de impacto socioambiental.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} As estratégias de ensino e aprendizagem serão fundamentadas em metodologias ativas, com ênfase em atividades práticas que busquem relacionar os conhecimentos desenvolvidos à realidade dos estudantes, ao mundo do trabalho e ao contexto socioeconômico do território, contemplando também experiências de economia solidária, cooperativismo e associativismo. Entre os espaços físicos, esta unidade curricular fará uso da sala de aula da turma, laboratório de informática, sala multidisciplinar, centro multiuso e espaços externos durante as visitas técnicas. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação será diagnóstica, processual e formativa, considerando os objetivos previstos na unidade curricular. Serão utilizados instrumentos diversificados, tais como atividades individuais e em grupo baseados em estudos de caso, resolução de problemas, pesquisas, dinâmicas, entrevistas, análise de experiências empreendedoras, visitas técnicas e outras atividades que aproximem os estudantes de diferentes formas de empreender e inovar. \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} A unidade curricular mantém conexão com Responsabilidade Socioambiental e Sustentabilidade; Línguas Inglesa, Portuguesa e Espanhola sobre as expressões e comunicação; Artes sobre as inovações; e Sociologia, Sociedade e Trabalho e Filosofia com reflexões sobre empreendedorismo, ética e sociedade.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BESSANT, John; TIDD, Joe; COSTA, Francisco Araújo da. \\textbf{Inovação e empreendedorismo}. 3. ed. Porto Alegre: Bookman, 2019. \\newline
DORNELAS, José Carlos Assis. \\textbf{Empreendedorismo}: transformando idéias em negócios. 3. ed. rev. e atual. Rio de Janeiro: Elsevier, 2008. \\newline
DORNELAS, José Carlos Assis. \\textbf{Empreendedorismo corporativo}: como ser empreendedor, inovar e se diferenciar na sua empresa. 2. ed. Rio de Janeiro: Elsevier, 2008. \\newline
HISRICH, Robert D.; PETERS, Michael P.; SHEPHERD, Dean A. \\textbf{Empreendedorismo}. Tradução de Francisco Araújo da Costa. 9. ed. Porto Alegre: AMGH, 2014. \\newline
OLIVEIRA, Edson Marques. \\textbf{Empreendedorismo social}: da teoria à prática, do sonho à realidade. Rio de Janeiro: Qualitymark, 2008. \\newline
SINGER, Paul \\textit{et al.} \\textbf{Economia Solidária}: introdução, história e experiência brasileira. São Paulo: Editora Unesp, 2023. \\newline
WEBERING, Susana Iglesias. \\textbf{Autogestão e Cooperação}. Curitiba: Editora Appris, 2020.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BERNARDI, Luiz Antônio. \\textbf{Manual de empreendedorismo e gestão}: fundamentos, estratégias e dinâmicas. 2. ed. São Paulo: Atlas, 2012. \\newline
OLIVEIRA, Djalma de Pinho Rebouças de. \\textbf{Empreendedorismo}: vocação, capacitação e atuação direcionadas para o plano de negócios. São Paulo: Editora Atlas, 2014.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[31] = t31

    # -------------------------------------------------------------
    # 35. TABELA 35: Biologia — Ano 3 (5º e 6º sem, 80h)
    # -------------------------------------------------------------
    t35 = """% ---------------------------------------------------------
% TABELA EMENTA 35: Biologia — Ano 3
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Biologia — Ano 3}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{5º e 6º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Analisar a estrutura e a expressão do material genético, compreendendo os mecanismos da variabilidade genética e da hereditariedade e suas aplicações em diferentes contextos científicos e tecnológicos.
    \\item Avaliar criticamente os avanços da Biotecnologia e suas implicações éticas, sociais, ambientais e econômicas, fundamentando-se em evidências científicas para a tomada de decisões responsáveis frente aos desafios tecnológicos e socioambientais contemporâneos.
    \\item Compreender a diversidade dos seres vivos, reconhecendo suas categorias taxonômicas, relações evolutivas, características biológicas, estratégias adaptativas, interações com o ambiente e importância para o equilíbrio dos ecossistemas e a sustentabilidade das sociedades humanas.
    \\item Desenvolver habilidades de observação e experimentação científica de modo a identificar e explicar fenômenos biológicos e processos tecnológicos decorrentes da utilização de organismos vivos na produção industrial, na saúde pública e na conservação ambiental.
    \\item Valorizar a diversidade biológica e cultural dos ecossistemas regionais, reconhecendo a contribuição dos saberes tradicionais africanos e indígenas para a relação com a natureza, o uso sustentável dos recursos naturais e a promoção da saúde individual e coletiva.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Biologia molecular: DNA, RNA e expressão gênica (transcrição e tradução). \\newline
Genética e hereditariedade: conceitos básicos, leis de Mendel e padrões de herança. \\newline
Temas contemporâneos em Biotecnologia e Bioética: células-tronco, clonagem, transgênicos, edição genética, experimentação animal, genética forense, entre outros. \\newline
Evolução biológica: teorias, evidências e mecanismos evolutivos. \\newline
Diversidade e classificação dos seres vivos: vírus, bactérias, algas, protozoários, fungos, plantas e animais. \\newline
Ecologia: sistemas ecológicos e serviços ecossistêmicos. \\newline
Educação Ambiental e Cultura Oceânica. \\newline
História e Cultura Afro-Brasileira, Africana e Indígena.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} O processo de ensino-aprendizagem será conduzido por meio de uma abordagem dialógica, contextualizada e investigativa, buscando o levantamento dos saberes prévios dos estudantes, a problematização de situações reais, a articulação com outras áreas do conhecimento e o desenvolvimento do pensamento crítico e científico. Metodologia baseada em estratégias didáticas diversificadas: aulas expositivo-dialogadas utilizando quadro e projetor multimídia; atividades práticas em campo e laboratório; análise de experimentos e estudos de caso; discussão de textos, imagens e vídeos científicos; uso de atlas digitais, softwares de animação e simulação, modelos didáticos tridimensionais e jogos educativos; debate de temas transversais; e participação em visitas técnicas e eventos científicos. As aulas práticas serão realizadas preferencialmente no pátio do câmpus e no Laboratório de Biociências, compondo uma média de 20h anuais, divididas em 10h para cada semestre letivo. Caso houver um segundo professor ministrante da UC, a turma poderá ser dividida em A e B, considerando a capacidade do espaço e a dinâmica da atividade proposta. O SIGAA será empregado como AVA. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação da aprendizagem se dará em uma perspectiva processual e formativa, observando-se a evolução dos conhecimentos construídos ao longo do período letivo. Instrumentos avaliativos: estudos dirigidos; listas de exercícios focados em ENEM e vestibulares; provas teóricas; relatórios de atividades experimentais; projetos, seminários ou oficinas temáticas; e avaliação atitudinal.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{GRIFFITHS, Anthony J. F. \\textbf{Introdução à genética}. Tradução de Idilia Vanzellotti. 10. ed. Rio de Janeiro: Guanabara Koogan, 2013. 710 p. ISBN 9788527721912. \\newline
Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). \\newline
REECE, Jane B. \\textbf{Biologia de Campbell}. 10. ed. Porto Alegre: Artmed, 2015. 1442 p. ISBN 9788582712160.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{BEGON, Michael; TOWNSEND, Colin R.; HARPER, John L. \\textbf{Ecologia}: de indivíduos a ecossistemas. 4. ed. Porto Alegre: Artmed, 2007. 740 p. ISBN 9788536308845. \\newline
CASTRO, Peter; HUBER, Michael E. \\textbf{Biologia marinha}. 8. ed. Porto Alegre: Artmed, 2012. 461 p. ISBN 9788580551020. \\newline
DARWIN, Charles. \\textbf{A origem das espécies e a seleção natural}. Tradução de Soraya Freitas. São Paulo: Madras, 2011. 462 p. ISBN 9788537006573.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[35] = t35

    # -------------------------------------------------------------
    # 39. TABELA 39: Filosofia — Ano 3 (remover matemática espúria)
    # -------------------------------------------------------------
    t39 = """% ---------------------------------------------------------
% TABELA EMENTA 39: Filosofia — Ano 3
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Filosofia — Ano 3}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{5º e 6º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Conhecer os aspectos gerais da filosofia medieval cristã.
    \\item Refletir acerca de autores e questões atinentes à filosofia moderna.
    \\item Conhecer o conceito de subjetividade a partir de Montaigne.
    \\item Compreender a centralidade da atividade política a partir de Maquiavel, Hobbes, Rousseau e Locke.
    \\item Estudar a ética do dever de Kant, bem como a centralidade do conceito de esclarecimento no período iluminista.
    \\item Conhecer aspectos gerais do irracionalismo e a crise da razão.
    \\item Refletir acerca da crise de valores morais e a problemática do niilismo.
    \\item Compreender o existencialismo e os conceitos de projeto e liberdade. Investigar a relação existente entre existencialismo e feminismo.
    \\item Visualizar o trabalho como elemento transformador na vida do homem.
    \\item Refletir acerca de questões éticas relacionadas à relação homem e meio ambiente.
    \\item Promover a troca de ideias e, por conseguinte, o respeito às distintas visões de mundo presentes na sala de aula.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Filosofia Medieval Cristã: A relação entre fé e razão; A Patrística de Santo Agostinho; A Escolástica de São Tomás de Aquino. \\newline
A Filosofia Moderna: A filosofia política em Maquiavel; O pensamento ensaístico de Montaigne; Locke, Rousseau e Hobbes: a filosofia política. \\newline
Filosofia Moderna e Contemporânea: Kant, a ética do dever e o esclarecimento; Schopenhauer, pessimismo, vontade e irracionalismo; Nietzsche e a crise dos valores; Niilismo e a crise da razão. \\newline
Existencialismo e liberdade; A condição da mulher nos séculos XX e XXI; Existencialismo, feminismo e liberdade. \\newline
Política, Estado e Poder na contemporaneidade; Ética e meio ambiente; O mundo do trabalho e a alienação; Indústria Cultural e consumo.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} Aulas expositivas, leituras interpretativas e críticas, seminários e apresentações individuais e/ou em grupo de alunos, pesquisa bibliográfica, produção de textos. \\newline\\vspace{2pt}
\\textbf{Avaliação:} A avaliação seguirá o caminho processual com notas de 0 a 10 e considerará: participação dos alunos nas atividades propostas pelo professor; trabalho de pesquisa individual e coletiva e prova escrita. Realização de dois momentos avaliativos formais durante o semestre, considerando que estes momentos não contemplarão a totalidade da nota, mas serão tomados como parte do processo integral da relação ensino-aprendizagem.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ARANHA, M. L. A.; MARTINS, M. H. P. \\textbf{Filosofando}: introdução à filosofia. São Paulo: Moderna, 1993. \\newline
CHAUÍ, Marilena. \\textbf{Convite à filosofia}. 13. ed. São Paulo: Ática, 2009.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{GAARDER, Jostein. \\textbf{O mundo de Sofia}: romance da história da filosofia. São Paulo: Seguinte, 2012. \\newline
MARCONDES, Danilo. \\textbf{Textos básicos de filosofia}: dos pré-socráticos a Wittgenstein. Rio de Janeiro: Jorge Zahar, 2000.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[39] = t39

    # -------------------------------------------------------------
    # 44. TABELA 44: Gestão Financeira (SUBSTITUIÇÃO INTEGRAL - 5º e 6º sem, 80h)
    # -------------------------------------------------------------
    t44 = """% ---------------------------------------------------------
% TABELA EMENTA 44: Gestão Financeira
% ---------------------------------------------------------
\\begin{xltabular}{\\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
\\hline
\\multirow{3}{=}{\\textcolor{ifscgreen}{\\textbf{Unidade Curricular:}}\\\\[3pt]\\textbf{\\large Gestão Financeira}} & \\multicolumn{2}{p{\\dimexpr5cm+2\\tabcolsep+\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Semestre:}} \\textbf{5º e 6º}} \\\\ \\cline{2-3}
 & \\textcolor{ifscgreen}{\\textbf{CH EaD*:}} & \\textcolor{ifscgreen}{\\textbf{CH Total*:}} \\\\ \\cline{2-3}
 & \\textbf{00 h} & \\textbf{80 h} \\\\ \\hline
\\endfirsthead
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Objetivos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
\\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]
    \\item Conhecer os principais conceitos relacionados às rotinas financeiras.
    \\item Organizar informações financeiras para gestão de empreendimentos de micro e pequeno porte.
    \\item Elaborar controles e demonstrativos financeiros.
\\end{itemize}
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Conteúdos:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{
Controles financeiros básicos: contas a pagar, contas a receber, caixa, movimentação bancária. \\newline
Tipos de Custos. \\newline
Formação de preços. \\newline
Fluxo de caixa e planejamento financeiro. \\newline
Capital de giro. \\newline
Demonstrações financeiras e suas análises.
} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Estratégias de Ensino e Aprendizagem:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textbf{Metodologia:} A unidade curricular será desenvolvida por meio de aulas expositivas dialogadas e metodologias ativas de aprendizagem, com enfoque teórico-prático, promovendo a participação dos estudantes na compreensão dos processos relacionados à gestão financeira. Serão adotadas estratégias metodológicas com exercícios práticos, análises de caso e simulações. As atividades de aprendizagem poderão incluir análise de práticas organizacionais, simulações, exercícios práticos, interações com organizações e profissionais da área, articulando os conhecimentos desenvolvidos na unidade curricular com situações reais do mundo do trabalho. Entre os espaços físicos, esta unidade curricular fará uso da sala de aula da turma, laboratório de informática e sala multidisciplinar, bem como espaços de organizações externas. \\newline\\vspace{2pt}
\\textbf{Avaliação:} O processo de avaliação será contínuo, processual e formativo, contemplando diferentes instrumentos, como produções escritas, apresentações orais, resolução de estudos de caso, atividades práticas, relatórios, registros reflexivos e participação nas atividades propostas. As avaliações poderão ser realizadas de forma individual ou em grupo, considerando o desenvolvimento dos conhecimentos, das habilidades e das atitudes previstas para a unidade curricular. \\newline\\vspace{2pt}
\\textbf{Articulação Curricular:} Esta unidade curricular se articula com Empreendedorismo, Gestão de Pessoas e Matemática para Administração. Com a formação geral, há articulação especialmente com Matemática.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Básica:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{ASSAF NETO, Alexandre; LIMA, Fabiano Guasti. \\textbf{Curso de administração financeira}. 2. ed. São Paulo: Atlas, 2011. \\newline
SARMENTO, Melo, M. \\textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas. Rio de Janeiro: Editora Alta Books, 2024.} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{\\textcolor{ifscgreen}{\\textbf{Bibliografia Complementar:}}} \\\\ \\hline
\\multicolumn{3}{|p{\\dimexpr\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}|}{FARIAS, Cláudio V. S. (org.). \\textbf{Técnico em administração}: gestão e negócios. Porto Alegre: Bookman, 2013. \\newline
GITMAN, Lawrence J. \\textbf{Princípios de administração financeira}. 12. ed. São Paulo: Pearson, 2010. \\newline
SOUSA, Antônio de. \\textbf{Gerência financeira para micro e pequenas empresas}: um manual simplificado. Rio de Janeiro: Elsevier/Sebrae, 2007.} \\\\ \\hline
\\end{xltabular}"""
    table_dict[44] = t44

    # -------------------------------------------------------------
    # Reassemble ementario_adm.tex
    # -------------------------------------------------------------
    out_lines = [header_part.strip(), "\n\n"]
    for num in sorted(table_dict.keys()):
        out_lines.append("\n\\clearpage\n")
        out_lines.append(table_dict[num].strip())
        out_lines.append("\n")

    full_output = "".join(out_lines)

    with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
        f.write(full_output)

    print("Successfully generated updated ementario_adm.tex!")

if __name__ == '__main__':
    main()
