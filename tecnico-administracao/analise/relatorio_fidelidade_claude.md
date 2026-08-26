<USER_REQUEST>
segue o relatório.... Checagem de Fidelidade — Ementário do PPC Técnico em Administração (IFSC)
Data da checagem: 24/08/2026 Escopo: As 28 ementas-fonte (Google Drive, pasta ementas/) que alimentam as 45 tabelas do curso Técnico em Administração, comparadas contra o arquivo ementario_adm.tex atualmente em produção no Drive (baixado e conferido nesta data). Metodologia: Para cada UC, o texto-fonte foi extraído na íntegra e literalmente do Google Doc correspondente (sem resumir) e comparado seção por seção com o bloco correspondente em ementario_adm.tex. Todas as divergências concretas foram registradas. O texto corrido de cada fonte está reproduzido abaixo, ao lado das divergências, para permitir a correção direta.
Status dos 3 bugs conhecidos (nota de handoff de 12/08/2026)
O arquivo ementario_adm.tex foi resincronizado em 21/08/2026 (comentário no cabeçalho do arquivo: "Sincronizado 1:1 a partir do acervo real de ementas do Drive") — os 3 bugs relatados na nota de handoff anterior já estão corrigidos na versão atual:
Erro aritmético 840h→880h: corrigido. O subtotal do 1º Ano já mostra "880h FG + 240h FT = 1.120h" e o total geral do curso mostra "3.200 h" (valor correto).
Matemática para Administração fora de posição: corrigido. A UC já aparece corretamente na tabela do 2º Ano (linha 60 da matriz).
Padding de bibliografia com placeholder "[Título pendente...]": corrigido. Nenhuma ocorrência desse placeholder foi encontrada no arquivo atual.
As 13 partes ementario_adm_CORRIGIDO*.tex de uma sessão anterior (que continham essas correções) não precisam mais ser aplicadas — o arquivo em produção já as incorpora e, aparentemente, foi ainda mais atualizado desde então (a estrutura de blocos mudou: 45 tabelas na versão atual vs. 46 nas partes corrigidas antigas).
Achados críticos (prioridade máxima)
🔴 Causa-raiz identificada: 4 UCs foram "preenchidas" no .tex sem usar o texto do docente
A planilha de revisão da equipe (revisao-PPC-Técnico em Administração, item nº 13, status Concluído) registra que, em uma correção anterior, as UCs Geografia I/III, Marketing I/II e Gestão Financeira estavam com "marcadores pendentes e ausência de Objetivos/Conteúdos" e foram todas "preenchidas e saneadas" para eliminar os pendentes e fechar o PDF oficial. Ou seja: como o Google Doc de origem ainda não tinha conteúdo do docente na época dessa correção, alguém (ou alguma IA) escreveu conteúdo novo diretamente no .tex para essas UCs, em vez de deixá-las como pendente.
O problema é que, depois dessa correção, os docentes responsáveis preencheram de fato as ementas no Google Drive — só que o ementario_adm.tex nunca foi atualizado com esse conteúdo real. Por isso a comparação desta checagem encontrou, nestas 4 UCs, objetivos/conteúdos/bibliografias inteiramente diferentes entre fonte e .tex — não é um erro de digitação, é conteúdo de origens diferentes:
Gestão de Marketing I (TABELA EMENTA 15) — ver relatório completo abaixo.
Gestão de Marketing II (TABELA EMENTA 29) — mesmo padrão.
Empreendedorismo I (TABELA EMENTA 31) — mesmo padrão (item nº 12 da planilha confirma que esta UC foi escrita do zero com "modelo Business Model Canvas", não copiada da fonte).
Gestão Financeira (TABELA EMENTA 44) — mesmo padrão. Semestre e CH confirmados pelo André em 24/08/2026: Ano 3, 5º e 6º semestre, 40h cada (80h total) — estes valores coincidem com os já registrados na fonte; é o .tex (que hoje mostra apenas "6º" e "40h") que precisa ser corrigido para "5º e 6º" e "80h", junto com a substituição do restante do conteúdo.
Recomendação: estas 4 UCs merecem prioridade máxima na correção — não é um ajuste de redação, é uma substituição de conteúdo. O texto corrido do docente (fonte oficial) está reproduzido integralmente em cada relatório abaixo, pronto para substituir o conteúdo atualmente no .tex. Vale confirmar com a coordenação se o conteúdo "provisório" escrito anteriormente tem algum elemento que valha a pena preservar (ex.: a obrigatoriedade de temáticas transversais) antes de descartá-lo.
🟡 Geografia — mesma causa-raiz, aparentemente já resolvida (confirmar)
O mesmo item nº 13 da planilha também lista "Geografia I/III" entre as UCs que estavam pendentes e foram preenchidas nessa correção anterior. A checagem desta vez não encontrou divergência de conteúdo faltante nessas duas tabelas (Geografia Ano 1 e Ano 3 têm texto real e specific, embora com algumas divergências pontuais listadas abaixo) — mas note que o documento-fonte no Drive contém uma terceira UC, "Geografia II" (Ano 2), que não tem tabela correspondente no ementário nem entrada na matriz curricular. Não está claro se isso é intencional (o curso pode não ter Geografia no 2º ano) ou se é uma lacuna herdada do mesmo processo de saneamento. Recomenda-se confirmar com a coordenação do curso.
Itens que PARECEM divergência mas já são correções aprovadas pela equipe (não mexer sem necessidade)
Cruzando os achados desta checagem com a planilha revisao-PPC-Técnico em Administração (itens 1, 7 e 8, todos com status Concluído), os seguintes "semestres divergentes" e uma "carga horária divergente" encontrados NÃO são bugs — são realinhamentos de semestre/CH que a equipe já decidiu e aplicou deliberadamente, porque o documento-fonte no Drive tem redação ambígua ou desatualizada (ex.: ementas herdadas de outro PPC, como "Técnico em Lazer"). O .tex está correto nestes casos; é o Google Doc de origem que ainda não foi atualizado com o semestre real de oferta:
Língua Portuguesa — Ano 1: fonte "1º e 1º" (rasura) → .tex "1º e 2º" ✅ correção aprovada (item 1)
Física — Ano 3: fonte "4 e 5" → .tex "5º e 6º" ✅ correção aprovada (item 7)
Química — Ano 2: fonte "2º e 3º" → .tex "3º e 4º" ✅ correção aprovada (item 7)
Química — Ano 3: fonte "1º" → .tex "5º" ✅ correção aprovada (item 7)
Gestão de Operações e Qualidade: fonte "4 e 5" → .tex "3º e 4º" ✅ correção aprovada (item 7)
Biologia — Ano 3: fonte "1º e 2º" → .tex "5º e 6º" ✅ correção aprovada (item 7)
Oficina de Integração I: fonte "4 e 5" → .tex "3º e 4º" ✅ correção aprovada (item 8)
Oficina de Integração II — CH Total: fonte "80h" → .tex "160h" ✅ correção aprovada (item 8, atualização de carga horária no 3º Ano)
Matemática para Administração (TABELA 28): fonte "04" (4º) → .tex "3º" ✅ confirmado pelo André em 24/08/2026, de acordo com a planilha de cargas horárias do curso — o .tex está correto, a fonte no Drive está desatualizada.
Gestão de Marketing II — CH Total: fonte "00h" → .tex "40h" ✅ confirmado pelo André em 24/08/2026 — 40h é o valor correto.
Organização e Processos — CH Total: fonte "00h" → .tex "40h" ✅ confirmado pelo André em 24/08/2026 — 40h é o valor correto.
Filosofia — Ano 1 e Ano 3 — CH Total: fonte "00h" (não preenchida) → .tex "80h" cada ano ✅ confirmado pelo André em 24/08/2026 — 80h por ano está correto (40h por semestre × 2 semestres, Ano 1 e Ano 3).
Recomendação: não é preciso agir sobre nenhum destes itens no .tex — todos os semestres e cargas horárias sinalizados nesta checagem já foram confirmados como corretos pela equipe/coordenação. Se possível, seria útil atualizar os próprios documentos-fonte no Drive para refletir esses valores, evitando que uma futura checagem de fidelidade os aponte de novo como "divergência".
Nota: a UC "Gestão de Marketing II" segue com achado crítico de conteúdo (objetivos/conteúdos/bibliografia totalmente diferentes da fonte — ver seção "Achados críticos" acima); apenas a carga horária foi confirmada correta, o restante do conteúdo ainda precisa ser substituído pelo texto do docente.
Achados de prioridade média (ainda sem correção registrada)
Nenhum item de semestre ou carga horária permanece em aberto — todos foram tratados na seção acima. Os achados remanescentes de prioridade média/baixa estão listados a seguir.
Achados de prioridade baixa (recorrentes em quase todas as UCs)
Presentes em praticamente todas as 28 fontes, sem risco de descaracterizar o conteúdo pedagógico, mas que afetam a fidelidade literal do documento:
Bibliografia: paginação, ISBN, tradutor, "Acesso em: [data]" e outros metadados bibliográficos presentes na fonte são sistematicamente omitidos no .tex (economia de espaço editorial, mas gera divergência de fidelidade).
Objetivos e Metodologia: parafraseados/resumidos em relação ao texto literal da fonte em várias UCs (especialmente Educação Física, Física, História, Geografia, Química, Matemática) — sentido geralmente preservado, mas com perda de detalhamento.
Reestruturação editorial: onde a fonte tem um parágrafo corrido de "Estratégias de Ensino e Aprendizagem", o .tex frequentemente separa em "Metodologia:" e "Avaliação:" — mudança estrutural sem perda de conteúdo relevante na maioria dos casos.
Pequenas divergências de nomenclatura de UC (ex.: "Gestão de Pessoas" → "Gestão de Pessoas e Relações no Trabalho"; "Biologia I/II" → "Biologia — Ano 1/3"; "Filosofia I/2" → "Filosofia — Ano 1/3").
Índice das 28 UCs verificadas
Artes — Ano 1 e Ano 2 (TABELA 1, 18)
Educação Física — Ano 1 e Ano 2 (TABELA 2, 19)
Inglês — Ano 1 e Ano 2 (TABELA 3, 20)
Língua Portuguesa e Literatura — Ano 1, 2 e 3 (TABELA 4, 21, 34)
Espanhol — Ano 1 e Ano 2 (TABELA 5, 22)
Biologia — Ano 1 e Ano 3 (TABELA 6, 35)
Física — Ano 1, 2 e 3 (TABELA 7, 23, 36)
Matemática — Ano 1, 2 e 3 (TABELA 8, 24, 37)
Química — Ano 1, 2 e 3 (TABELA 9, 25, 38)
Filosofia — Ano 1 e Ano 3 (TABELA 10, 39)
Geografia — Ano 1 e Ano 3 (TABELA 11, 40) — ⚠️ falta Geografia II
Sociologia — Ano 1 e Ano 2 (TABELA 12, 27)
Introdução à Administração (TABELA 13)
Sociedade e Trabalho (TABELA 14)
Gestão de Marketing I (TABELA 15) — 🔴 crítico
Organização e Processos (TABELA 16)
Informática Aplicada (TABELA 17)
História — Ano 2 e Ano 3 (TABELA 26, 41)
Matemática para Administração (TABELA 28)
Gestão de Marketing II (TABELA 29) — 🔴 crítico
Gestão de Operações e Qualidade (TABELA 30)
Empreendedorismo I (TABELA 31) — 🔴 crítico
Responsabilidade Socioambiental e Sustentabilidade (TABELA 32)
Oficina de Integração I (TABELA 33)
Empreendedorismo II (TABELA 42)
Gestão de Pessoas e Relações no Trabalho (TABELA 43)
Gestão Financeira (TABELA 44) — 🔴 crítico
Oficina de Integração II (TABELA 45)
Relatórios individuais por UC
Artes — Ano 1 e Ano 2 (TABELA EMENTA 1 e 18)
Fonte: Google Drive, fileId 1Sw2ZBpdy8JNl7nN37C0u-tIJbYWntNdsvSUFUNvzX1E (ementa-artes-adm). Comparado com: /tmp/ppc/ementario_adm_LIVE.tex, linhas 127–171 (TABELA EMENTA 1) e 893–942 (TABELA EMENTA 18).
Texto de origem extraído do Google Drive (na íntegra)
Cabeçalho do documento
Unidade Curricular: Arte
Editada pelo Docente: Mariana Reis Leal Fernandes
Bloco 1 — "Arte 1"
Unidade Curricular: Arte 1 | Semestre: 1 e 2 CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Compreender a Arte como construção histórica, social e cultural e suas imbricações;
Refletir sobre as relações que envolvem os processos de construção e fruição da Arte;
Expressar e comunicar ideias e sentimentos por meio de atividades de práticas corporais;
Desenvolver o senso crítico em relação à arte, à sociedade, à tecnologia e ao meio ambiente;
Interpretar e analisar o significado de obras de arte a partir de diferentes perspectivas;
Identificar, experienciar e criar nas diferentes linguagens da arte do corpo em cena (dança, teatro e performance).
Conteúdos:
Conceitos básicos: linguagem, objeto de conhecimento, significação e produto;
Arte contextualizada social, política, histórica e economicamente;
Manifestações artísticas no decorrer do tempo e do espaço;
Apreciação e análise de produções artísticas internacionais, nacionais e locais;
Arte, ciência e meio ambiente: a não separação entre natureza e cultura;
Arte do corpo em cena na atualidade: apreciação, análise e prática;
O corpo como instrumento de expressão artística.
Estratégias de ensino e aprendizagem:
Aulas participativas e dialogadas, partindo do conhecimento prévio do estudante, utilizando imagens, textos, vídeos, músicas e corpo;
Atividades focadas na indissociabilidade entre teoria e prática, com atividades corporais;
Desenvolvimento de trabalhos, exercícios, pesquisas, seminários e obras artísticas;
Atividades individuais e em grupos;
Jogos teatrais e exercícios de improvisação;
Práticas de dança contemporânea e danças tradicionais brasileiras;
Utilização da sala de artes para atividades práticas.
Avaliação: (campo não presente no documento-fonte — nenhuma seção de Avaliação foi encontrada)
Bibliografia Básica: GOMBRICH, E. H. A história da arte. Tradução de Álvaro Cabral. 16. ed. Rio de Janeiro: Livros Técnicos e Científicos, 1999. 688 p., il., color., 25 cm. ISBN 9788521611851. PROENÇA, G. História da arte. 17. ed. São Paulo: Ática, 2010.
Bibliografia Complementar: AGRA, Lucio. História da arte do século XX: idéias e movimentos. 2. ed. rev. atual. São Paulo: Anhembi, 2004. 192 p., il. (Moda e comunicação). ISBN 8587370146. CERTEAU, Michel de. A invenção do cotidiano: artes de fazer. Tradução de Ephraim Ferreira Alves. 16. ed. Petrópolis, RJ: Vozes, 2009. 315 p. ISBN 9788532611482. LARAIA, R. de B. Cultura: um conceito antropológico. 26. reimp. Rio de Janeiro: Jorge Zahar, 1986. SOUZA, Ana Lúcia Silva. Letramentos de reexistência: poesia, grafite, música, dança : hip-hop. São Paulo: Parábola Editorial, 2011. 171 p., il. (Estratégias de ensino, 26). Inclui bibliografia. ISBN 9788579340321.
Bloco 2 — "Arte 2"
Unidade Curricular: Arte 2 | Semestre: 3 e 4 CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Refletir sobre os conceitos básicos dos fenômenos artísticos ocidentais e suas relações com outras formas de pensamento;
Analisar o uso de manifestações tradicionais brasileiras como constituintes de saberes, territórios e identidades;
Vivenciar práticas corporais tradicionais;
Experienciar e criar nas diferentes linguagens da arte do corpo em cena (dança, teatro e performance);
Valorizar a diversidade cultural brasileira;
Analisar o papel da arte como ferramenta de denúncia e conscientização;
Refletir sobre a relação entre arte, política, ciência, tecnologia e meio ambiente;
Estabelecer diálogos entre a arte contemporânea e os saberes tradicionais.
Conteúdos:
Manifestações populares e tradicionais no Brasil;
Cultura indígena, afro-brasileira e africana;
Artivismo;
Abordagens em arte contra a hegemonia, em diálogo com os saberes e as tradições decoloniais;
Práticas de movimentos, passos e técnicas em dança e teatro;
Estudo teórico-prático de técnicas de improvisação em dança e teatro;
Panorama histórico da dança e do teatro no Brasil;
Pesquisa, elaboração de ideias, criação, produção e apresentação de obras em artes do corpo em cena;
Improvisação e criação coletiva.
Estratégias de ensino e aprendizagem:
Aulas participativas e dialogadas, partindo do conhecimento prévio do estudante, utilizando imagens, textos, vídeos, músicas e corpo;
Atividades focadas na indissociabilidade entre teoria e prática, com atividades corporais;
Desenvolvimento de trabalhos, exercícios, pesquisas, seminários e obras artísticas;
Atividades individuais e em grupos;
Jogos teatrais e exercícios de improvisação;
Práticas de dança contemporânea e danças tradicionais brasileiras;
Utilização da sala de artes para atividades práticas.
Avaliação: (campo não presente no documento-fonte — nenhuma seção de Avaliação foi encontrada)
Bibliografia Básica: CONDURU, Roberto. Arte afro-brasileira. Orientação de Lucia Gouvêa Pimentel, Alexandrino Ducarmo. Belo Horizonte: C/Arte, 2007. 126 p., il., color. (Historiando a arte brasileira. Coleção Didática, 2). Bibliografia: p. [125]-126. ISBN 9788576540472. GOMBRICH, E. H. A história da arte. Tradução de Álvaro Cabral. 16. ed. Rio de Janeiro: Livros Técnicos e Científicos, 1999. 688 p., il., color., 25 cm. ISBN 9788521611851. PROENÇA, G. História da arte. 17. ed. São Paulo: Ática, 2010.
Bibliografia Complementar: NILSON, Afonso. Seis textos breves para estudantes de teatro. Florianópolis: Letras Contemporâneas, 2017. 71 p. ISBN 9788594445001. MACHADO, Lúcia. A modernidade no teatro: [ali e aqui] : reflexos estilhaçados. Recife: Ed. do autor, 2009. 450 p., il. Bibligrafia: p. 434-445. ISBN 9788591007806. PIMENTEL, Spency. O índio que mora na nossa cabeça: sobre as dificuldades para entender os povos indígenas. São Paulo: Prumo, 2012. 88 p., il.; color. Inclui bibliografia. ISBN 9788579272486. SANT'ANNA, Márcia (org.). Os sambas brasileiros: diversidade, apropriação e salvaguarda. Brasília, DF: IPHAN, 2011. 144 p., il. (Anais, 1). ISBN 9788573341911.
Divergências identificadas em relação ao ementario_adm.tex
Nomenclatura da UC (Ano 1): a fonte nomeia a unidade curricular como "Arte 1" (singular); o ementário usa "Artes — Ano 1" (plural + formato "Ano N"). Mudança de nomenclatura não documentada.
Nomenclatura da UC (Ano 2): a fonte nomeia a unidade curricular como "Arte 2" (singular); o ementário usa "Artes — Ano 2". Mesmo padrão de divergência de nome.
Bibliografia Básica — Ano 1 (GOMBRICH): o ementário omite a descrição física e o ISBN presentes na fonte ("688 p., il., color., 25 cm. ISBN 9788521611851.").
Bibliografia Complementar — Ano 1 (AGRA): o ementário omite "192 p., il. (Moda e comunicação). ISBN 8587370146." presentes na fonte.
Bibliografia Complementar — Ano 1 (CERTEAU): o ementário omite "315 p. ISBN 9788532611482." presentes na fonte.
Bibliografia Complementar — Ano 1 (SOUZA): o ementário omite "171 p., il. (Estratégias de ensino, 26). Inclui bibliografia. ISBN 9788579340321." presentes na fonte.
Bibliografia Básica — Ano 2 (CONDURU): o ementário omite "Orientação de Lucia Gouvêa Pimentel, Alexandrino Ducarmo." e a descrição física/ISBN ("126 p., il., color. (Historiando a arte brasileira. Coleção Didática, 2). Bibliografia: p. [125]-126. ISBN 9788576540472.") presentes na fonte.
Bibliografia Básica — Ano 2 (GOMBRICH): mesmo caso do item 3 — descrição física e ISBN omitidos.
Bibliografia Complementar — Ano 2 (NILSON): o ementário omite "71 p. ISBN 9788594445001." presentes na fonte.
Bibliografia Complementar — Ano 2 (MACHADO): o ementário omite "450 p., il. Bibligrafia: p. 434-445. ISBN 9788591007806." presentes na fonte.
Bibliografia Complementar — Ano 2 (PIMENTEL): o ementário omite "88 p., il.; color. Inclui bibliografia. ISBN 9788579272486." presentes na fonte.
Bibliografia Complementar — Ano 2 (SANT'ANNA): o ementário omite "144 p., il. (Anais, 1). ISBN 9788573341911." presentes na fonte.
Itens verificados SEM divergência (para registro)
Objetivos (Ano 1 e Ano 2): todos os itens conferem literalmente com a fonte, apenas convertidos de marcadores "●"/"-" para \item.
Conteúdos (Ano 1 e Ano 2): todos os itens conferem literalmente com a fonte.
Estratégias de Ensino/Metodologia (Ano 1 e Ano 2): texto idêntico ao da fonte, apenas reformatado de lista para parágrafo corrido.
Carga horária (CH EaD 00h / CH Total 80h) e semestres (1º/2º e 3º/4º): corretos e consistentes com a fonte (fonte usa "1 e 2"/"3 e 4" sem indicador ordinal — diferença puramente tipográfica, não é divergência de conteúdo).
Avaliação: a fonte não possui campo de Avaliação; o ementário corretamente sinaliza "Não especificado no documento fonte." — não é um placeholder indevido, é uma constatação correta.
Educação Física — Ano 1 e Ano 2 (TABELA EMENTA 2 e 19)
Fonte: Google Drive, fileId 1tvdDonbiWVVeX8-pVoFDqtHV7wX8TkHWG_sCeVEqGRU ("ementa-educacao-fisica-adm") Comparado com: /tmp/ppc/ementario_adm_LIVE.tex, TABELA EMENTA 2 (linhas 171–210) e TABELA EMENTA 19 (linhas 942–981).
Texto de origem extraído do Google Drive (na íntegra)
BLOCO — Educação Física — Ano 1
Unidade Curricular: Educação Física — Ano 1 Semestre: 1º e 2º CH EaD*: não se aplica CH Total*: 80 h
Objetivos:
Promover a reflexão crítica sobre a cultura corporal como construção social, histórica e cultural, desvendando as relações de poder, as desigualdades sociais e as formas de dominação presentes nas práticas corporais.
Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade contemporânea.
Desenvolver a autonomia dos estudantes para que possam tomar decisões conscientes sobre suas práticas corporais, promovendo a saúde e o bem-estar de forma integral.
Promover a valorização da diversidade corporal, cultural e social, combatendo o preconceito e a discriminação em todas as suas formas.
Estimular a participação ativa dos alunos na transformação da sociedade, utilizando o esporte e as práticas corporais como ferramentas de promoção da justiça social e da igualdade.
Desenvolver a capacidade de analisar e interpretar informações sobre a cultura corporal, utilizando diferentes fontes e linguagens.
Promover a cooperação, o respeito mútuo e a valorização das diferenças individuais, contribuindo para a formação de cidadãos solidários e comprometidos com o bem comum.
Promover a consciência ambiental e a prática de atividades físicas que respeitem o meio ambiente.
Identificar, compreender, analisar e utilizar as diferentes tecnologias relacionadas à cultura corporal em uma base ética, promovendo a inclusão e o desenvolvimento de novas formas de interação social.
Analisar como os padrões de beleza e corporeidade são construídos socialmente e como influenciam a autoestima e a saúde dos indivíduos.
Identificar as representações do corpo nas diferentes mídias e analisar seus impactos na construção da identidade.
Compreender a importância das práticas corporais para a construção da identidade e dos vínculos sociais.
Analisar as relações de poder presentes nas práticas esportivas e como elas podem ser utilizadas para promover a inclusão social.
Relacionar a prática regular de atividade física com a prevenção de doenças crônicas e a promoção da saúde mental.
Analisar a influência da indústria do esporte e da alimentação na saúde da população.
Analisar a gênese e as mudanças sócio-históricas do esporte
Analisar oa produção e o desenvolvimento da técnica e tecnologias do esporte
(nota: "Analisar oa produção..." — typo presente no documento-fonte, reproduzido literalmente)
Conteúdos:
O corpo como expressão cultural e social: A construção histórica do corpo e do movimento
O corpo na mídia e a cultura de consumo
O corpo e a diversidade: gênero, raça, classe social, idade e deficiência
A cultura corporal e a identidade
Cultura corporal e suas relações sociais: Danças populares e urbanas: história, significados e diversidade
Lutas e artes marciais: história, filosofia e valores
Esportes coletivos e individuais: regras, técnicas, táticas e valores
Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate
Os jogos e as brincadeiras
Esporte, competição e performance: Esporte e sociedade: relações de poder e desigualdade
Doping e ética no esporte
Saúde mental e desempenho esportivo
Esporte e mídia: representações e consumismo
A cultura corporal e o meio ambiente: Práticas corporais ao ar livre e em contato com a natureza
A importância da sustentabilidade nas práticas esportivas
O impacto do esporte no meio ambiente
O esporte na sociedade capitalista e suas manifestações: A gênese e o desenvolvimento do esporte
Técnica e tecnologia no esporte
Introdução à economia política do esporte
Estratégias de ensino e aprendizagem: Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.
Bibliografia Básica:
Dicionário crítico de educação física. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014.
BERNARDES, Luciano Andrade (org.). Atividades e esportes de aventura para profissionais de educação física. São Paulo: Phorte, 2013.
Bibliografia Complementar:
BRACHT, Valter. Sociologia crítica do esporte: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003.
CAMARGO, Wagner Xavier de. Leituras de gênero e sexualidade nos esportes. São Carlos: EDUFSCAR, 2021.
FOER, Franklin. Como o futebol explica o mundo: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.
Notas de rodapé da tabela (idênticas para Ano 1 e Ano 2, presentes no documento-fonte): () CH – Carga horária total da unidade curricular, em horas. () CH Prática – Carga horária associada às atividades que têm por objetivo a aplicação de conhecimentos teóricos adquiridos, podendo ocorrer em ambiente interno ou externo, conforme diretrizes curriculares nacionais do curso. () CH EaD – Carga horária a distância, se houver. () CH com Divisão de Turma – Carga horária desenvolvida em laboratório que necessite divisão de turma ou presença de um segundo docente.
BLOCO — Educação Física — Ano 2
Unidade Curricular: Educação Física — Ano 2 Semestre: 1º e 2º (sic — texto-fonte repete "1º e 2º" também no bloco do Ano 2) CH EaD*: não se aplica CH Total*: 80 h
Objetivos:
Compreender a cultura corporal em suas diversas manifestações e dimensões, relacionando-a com os contextos históricos, sociais e culturais.
Acessar e apreender diferentes manifestações da cultura corporal, compreendendo a história, o desenvolvimento, as técnicas e táticas, suas representações e significados na sociedade conetmprânea.
Analisar criticamente as representações sociais do corpo e do movimento, desconstruindo estereótipos e preconceitos.
Investigar a história e a evolução das práticas corporais, valorizando a diversidade cultural.
Refletir sobre a influência da mídia e do consumo nas práticas corporais.
Promover a sensibilização para a inclusão social através do esporte e do lazer, combatendo o preconceito e a discriminação.
Desenvolver projetos que promovam a inclusão de pessoas com deficiência, LGBTQIA+, idosos e outros grupos minoritários.
Analisar as políticas públicas de esporte e lazer e suas implicações sociais.
Desenvolver a capacidade de analisar criticamente as relações de poder presentes nas práticas corporais e no esporte.
Identificar as desigualdades sociais e as relações de gênero presentes no esporte e no lazer.
Refletir sobre o papel do esporte como instrumento de transformação social.
Desenvolver os estudantes técnicos capazes de atuar em diferentes contextos, utilizando as tecnologias digitais como ferramentas para o ensino e a gestão de projetos.
Desenvolver uma consciência crítica em relação ao meio ambiente e à sustentabilidade.
Promover a prática de atividades físicas ao ar livre e o contato com a natureza.
Incentivar a produção de eventos esportivos e de lazer sustentáveis.
Compreender a domesticação dos corpos marginalizados, como mulheres, pessoas negras, LGBTQIA+, e pessoas com deficiência, e os impactos dessa disciplina na ocupação dos espaços destinados ao lazer.
Analisar o impacto da vigilância e da moralização nos corpos que ocupam espaços de lazer, promovendo a identificação de práticas de exclusão e estigmatização.
Promover discussões interseccionais de gênero, raça e classe social e a domesticação dos corpos nos espaços de lazer.
Desenvolver práticas educacionais que fomentem o acesso igualitário ao lazer, subvertendo os mecanismos de exclusão e disciplinamento dos corpos.
(nota: "conetmprânea" — typo presente no documento-fonte, reproduzido literalmente)
Conteúdos:
Lazer e tempo livre: Lazer e tempo livre: conceitos, históricos e transformações
Políticas públicas de lazer e suas implicações sociais
Turismo e lazer: relações e perspectivas
Lazer e tecnologia: impactos e possibilidades
Saúde, corpo e movimento: Atividade física e saúde: evidências científicas
Alimentação e nutrição para o desempenho esportivo
Lesões esportivas: prevenção e tratamento
Saúde do trabalhador e ergonomia
Cultura corporal e trabalho: Trabalho e lazer: relações históricas e contemporâneas
Saúde do trabalhador e qualidade de vida
Diversidade, gênero e inclusão: Corpo, gênero e sexualidade na cultura corporal
Esporte e pessoas com deficiência
Racismo e discriminação no esporte
LGBTQIA+ e esporte
Cultura corporal e suas relações sociais: Danças populares e urbanas: história, significados e diversidade
Lutas e artes marciais: história, filosofia e valores
Esportes coletivos e individuais: regras, técnicas, táticas e valores
Práticas corporais alternativas e de aventura: yoga, pilates, surf, skate
Estratégias de ensino e aprendizagem: Aulas com caráter reflexivo, pautadas na interação, no diálogo e na mediação entre professor e aluno, partindo da prática social como ponto de partida e de chegada no processo de apreensão do conhecimento. Aulas expositivas dialogadas; aulas práticas com vivências corporais; participação e organização de eventos/atividades esportivas e recreativas na natureza; estudos dirigidos; discussões em grupo. Atividades práticas realizadas no laboratório de cultura corporal do câmpus, em ambiente externo e com saídas técnicas na região.
Bibliografia Básica:
Dicionário crítico de educação física. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014.
BERNARDES, Luciano Andrade (org.). Atividades e esportes de aventura para profissionais de educação física. São Paulo: Phorte, 2013.
Bibliografia Complementar:
BRACHT, Valter. Sociologia crítica do esporte: uma introdução. 2. ed. Ijuí: Ed. da Unijuí, 2003.
CAMARGO, Wagner Xavier de. Leituras de gênero e sexualidade nos esportes. São Carlos: EDUFSCAR, 2021.
FOER, Franklin. Como o futebol explica o mundo: um olhar inesperado sobre a globalização. Rio de Janeiro: Jorge Zahar Editor, 2005.
Notas de rodapé: idênticas às do bloco Ano 1 (reproduzidas acima, presentes também após o bloco Ano 2 no documento-fonte).
Divergências identificadas em relação ao ementario_adm.tex
[Ano 2] Semestre divergente: o documento-fonte registra "Semestre: 1º e 2º" também no bloco Educação Física — Ano 2 (repetição idêntica ao bloco Ano 1). O .tex (linha 946) registra "Semestre: 3º e 4º" para o Ano 2. Há discrepância entre fonte e ementário quanto à classificação de semestre do Ano 2 — necessário confirmar com a coordenação qual valor é o correto antes de decidir a correção.
[Ano 1] Objetivos drasticamente resumidos: a fonte lista 17 objetivos específicos detalhados (autonomia do estudante, cooperação/respeito mútuo, tecnologias digitais na cultura corporal, padrões de beleza/mídia/autoestima, prevenção de doenças crônicas e saúde mental, influência da indústria do esporte/alimentação na saúde, gênese sócio-histórica do esporte, técnica/tecnologia do esporte, entre outros). O .tex (linhas 182–186) reduz isso a apenas 5 itens genéricos, omitindo a maior parte do conteúdo da fonte.
[Ano 2] Objetivos drasticamente resumidos: a fonte lista 19 objetivos específicos, incluindo eixos críticos importantes — "domesticação dos corpos marginalizados" (mulheres, pessoas negras, LGBTQIA+, pessoas com deficiência), "impacto da vigilância e da moralização nos corpos que ocupam espaços de lazer", "discussões interseccionais de gênero, raça e classe social", tecnologias digitais para ensino/gestão de projetos, políticas públicas de esporte e lazer. O .tex (linhas 953–957) reduz para 5 itens genéricos e omite completamente os objetivos sobre domesticação/vigilância/moralização dos corpos e a abordagem interseccional de gênero/raça/classe, que são conteúdo substantivo específico da fonte.
[Ano 1] Conteúdos — subitem "idade" ausente: a fonte especifica a diversidade como "gênero, raça, classe social, idade e deficiência"; o .tex (linha 191) lista apenas "gênero, raça, classe, deficiência", omitindo "idade".
[Ano 1 e Ano 2] Conteúdos reestruturados em prosa: a fonte apresenta os conteúdos em lista hierárquica (tópico + subtópicos); o .tex condensa tudo em parágrafos corridos. Os temas de topo são majoritariamente preservados, mas a granularidade dos subitens (ex.: "jogos e brincadeiras" como item próprio no Ano 1; "turismo e lazer", "lazer e tecnologia" como subitens específicos no Ano 2) fica implícita/reduzida no texto corrido, não sendo uma transcrição literal da fonte.
[Ano 1 e Ano 2] Estratégias de Ensino — frase adicionada sem correspondência na fonte: o .tex (linha 198 e linha 969) acrescenta ao final do parágrafo de Estratégias a frase "O processo avaliativo será contínuo, formativo e processual, contemplando diferentes instrumentos de reflexão e vivência prática.", que não consta no documento-fonte (nem como parte das Estratégias, nem em seção de Avaliação separada — a fonte não possui seção de Avaliação para esta UC).
[Ano 1 e Ano 2] CH EaD — representação diferente: a fonte registra "CH EaD*: não se aplica"; o .tex (linha 177 e linha 948) registra "CH EaD*: 00 h". Mesmo sentido (zero carga EaD), mas literalmente divergente do texto-fonte.
Nenhum placeholder do tipo "[pendente...]" foi encontrado no ementário para esta UC. Bibliografia Básica e Bibliografia Complementar (Ano 1 e Ano 2) conferem integralmente com a fonte, sem adições ou omissões.
Inglês — Ano 1 e Ano 2 (TABELA EMENTA 3 e 20)
Texto de origem extraído do Google Drive (na íntegra)
Bloco Ano 1
Unidade Curricular: Inglês — Ano 1 | Semestre: 1º e 2º CH EaD*: não se aplica | CH Total*: 80 h
Objetivos:
Compreender a língua inglesa como língua franca e idioma universal, entendendo sua função social como possibilidade de ampliar o acesso à informação e a bens científicos e culturais da humanidade;
Ampliar de modo autônomo o conhecimento da língua inglesa a partir de estratégias de aprendizagem e compreensão, utilizando ferramentas convencionais e digitais;
Posicionar-se como usuário ativo da língua inglesa em diferentes cenários, vivenciando práticas de fala, escuta, escrita e de leitura;
Produzir sentido a partir de elementos linguísticos e extralinguísticos de gêneros textuais (orais, escritos e/ou híbridos), prioritariamente utilizando textos autênticos;
Conhecer regularidades morfológicas e sintáticas da língua inglesa que auxiliem na compreensão de significados e na ampliação de vocabulário.
Conteúdos:
Cumprimentos e informações pessoais;
Perguntas com Wh;
Artigos;
Substantivos (objetos, pessoas e lugares);
Expressões de tempo (horas, dias, meses);
Pronomes pessoais;
Pronomes demonstrativos;
Verbo To Be;
Números;
Profissões;
Verbos comuns;
Imperativo;
Presente simples;
Advérbios de frequência;
Presente contínuo;
Caracterização de objetos, pessoas e lugares;
Adjetivos (comparativos e superlativos);
Pronomes relativos.
Estratégias de ensino e aprendizagem:
Aulas expositivas dialogadas e contextualizadas, buscando aproximação com o cotidiano dos estudantes;
A apresentação dos conteúdos trabalhados ocorrerá por meio da audição, conversação, leitura e produção de textos e/ou apresentações com recursos multimídia;
Projetos/Atividades envolvendo gêneros textuais de natureza lúdica (como música e vídeo), informativa (como notícias e textos científicos), literárias (como poemas e obras) e/ou técnica e científica;
Atividades que propiciem ao estudante a oportunidade de compartilhar conhecimento com os colegas.
(Não há seção "Avaliação" separada no documento-fonte para o Ano 1.)
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). DICIONÁRIO Escolar Longman Inglês-Português, Português-Inglês. Harlow : Pearson Longman, 2004. LATHAM-KOENIG, C. English File [livro] : Intermediate Student's Book. Oxford : Oxford University Press, 2018.
Bibliografia Complementar: FRANCO, C. P. English vibes for Brazilian learns: volume único. 1. ed. São Paulo: FTD, 2020. MURPHY, Raymond. Essential Grammar in Use. 4th ed. Cambridge: Cambridge University Press, 2015. WHARTON, S. 500 tips for tesol : (teaching english to speakers of other languages). London: Kogan Page, 1999.
Bloco Ano 2
Unidade Curricular: Inglês — Ano 2 | Semestre: 3º e 4º CH EaD*: não se aplica | CH Total*: 80 h
Objetivos:
Compreender a língua inglesa como língua franca e idioma universal, entendendo sua função social como possibilidade de ampliar o acesso à informação e a bens científicos e culturais da humanidade;
Ampliar de modo autônomo o conhecimento da língua inglesa a partir de estratégias de aprendizagem e compreensão, utilizando ferramentas convencionais e digitais;
Posicionar-se como usuário ativo da língua inglesa em diferentes cenários, vivenciando práticas de fala, escuta, escrita e de leitura;
Produzir sentido a partir de elementos linguísticos e extralinguísticos de gêneros textuais (orais, escritos e/ou híbridos), prioritariamente utilizando textos autênticos;
Conhecer regularidades morfológicas e sintáticas da língua inglesa que auxiliem na compreensão de significados e na ampliação de vocabulário.
Conteúdos:
Eventos e fatos passados: passado simples, contínuo e presente perfeito;
Preposições de tempo e lugar;
Futuro Simples;
Futuro com Going to;
Conjunções (contraste, adição, conclusão, causa, finalidade);
Marcadores sequenciais;
Advérbios;
Formação de palavras;
Prefixos e sufixos;
Expressões idiomáticas;
Voz passiva;
Verbos frasais;
Gerúndio;
Verbos modais (can, should, must, would);
Condicionais.
Estratégias de ensino e aprendizagem:
Aulas expositivas dialogadas e contextualizadas, buscando aproximação com o cotidiano dos estudantes;
A apresentação dos conteúdos trabalhados ocorrerá por meio da audição, conversação, leitura e produção de textos e/ou apresentações com recursos multimídia;
Projetos/Atividades envolvendo gêneros textuais de natureza lúdica (como música e vídeo), informativa (como notícias e textos científicos), literárias (como poemas e obras) e/ou técnica e científica;
Atividades que propiciem ao estudante a oportunidade de compartilhar conhecimento com os colegas.
(Não há seção "Avaliação" separada no documento-fonte para o Ano 2.)
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). DICIONÁRIO Escolar Longman Inglês-Português, Português-Inglês. Harlow : Pearson Longman, 2004. LATHAM-KOENIG, C. English File [livro] : Intermediate Student's Book. Oxford : Oxford University Press, 2018.
Bibliografia Complementar: FRANCO, C. P. English vibes for Brazilian learns: volume único. 1. ed. São Paulo: FTD, 2020. MURPHY, Raymond. Essential Grammar in Use. 4th ed. Cambridge: Cambridge University Press, 2015. WHARTON, S. 500 tips for tesol : (teaching english to speakers of other languages). London: Kogan Page, 1999.
Divergências identificadas em relação ao ementario_adm.tex
[Ano 1] CH EaD divergente: fonte diz "não se aplica"; ementário (linha 216) apresenta "00 h" — texto literal diferente do documento-fonte.
[Ano 1] Seção "Avaliação" inexistente na fonte: o ementário (linha 251) inclui um parágrafo "Avaliação: Avaliação contínua e processual, acompanhando o desenvolvimento das quatro habilidades linguísticas (ouvir, falar, ler e escrever)..." que não consta em nenhum lugar do documento-fonte para o Ano 1 — a fonte só traz "Estratégias de ensino e aprendizagem" (4 itens), sem bloco de avaliação separado. Trecho aparentemente adicionado/inventado no ementário.
[Ano 1] Bibliografia Básica — anotação "[livro]" ausente: a fonte registra "LATHAM-KOENIG, C. English File [livro] : Intermediate Student's Book..."; o ementário (linha 255) omite a marcação "[livro]".
[Ano 1] Bibliografia Complementar — grafia divergente: fonte tem "English vibes for Brazilian learns" (provável erro de digitação no documento-fonte); ementário (linha 257) tem "English vibes for Brazilian learners" — texto não é literal em relação à fonte.
[Ano 2] CH EaD divergente: fonte diz "não se aplica"; ementário (linha 987) apresenta "00 h".
[Ano 2] Seção "Avaliação" inexistente na fonte: o ementário (linha 1019) inclui o mesmo parágrafo de "Avaliação" que não existe no documento-fonte para o Ano 2 — a fonte só traz "Estratégias de ensino e aprendizagem" (4 itens).
[Ano 2] Bibliografia Básica — anotação "[livro]" ausente: mesma omissão do Ano 1 (ementário linha 1023 vs. fonte).
[Ano 2] Bibliografia Complementar — grafia divergente: mesma divergência "learns" (fonte) vs. "learners" (ementário, linha 1025).
Observações: Objetivos, Conteúdos Programáticos, Semestre (1º/2º e 3º/4º) e CH Total (80h) conferem integralmente com a fonte em ambos os anos. Não foram encontrados placeholders do tipo "[pendente...]" no ementário.
Língua Portuguesa e Literatura — Ano 1, 2 e 3 (TABELA EMENTA 4, 21 e 34)
Fonte: Google Drive, fileId 1ZDfYaTJxy3pnwqlPEVQAD48aZnBLFWK8g3VFneyhMmM (ementa-lingua-portuguesa-literatura-adm) Comparado com: /tmp/ppc/ementario_adm_LIVE.tex, TABELA EMENTA 4 (linhas 264–299), TABELA EMENTA 21 (linhas 1032–1066) e TABELA EMENTA 34 (linhas 1603–1640).
Texto de origem extraído do Google Drive (na íntegra)
Bloco — Ano 1
Unidade Curricular: Língua Portuguesa e Literatura — Ano CH Total*: 80 Semestre: 1º e 1º CH* Prática: 10h CH EaD*: não há CH com Divisão de Turma*: (em branco)
Objetivos
Reconhecer a Língua Portuguesa como um instrumento de inserção social indispensável ao pleno desenvolvimento do educando, visando seu preparo para o pleno exercício da cidadania e a qualificação para o trabalho;
Compreender a Língua Portuguesa a partir de seus diversos usos e situações comunicativas, entendendo-a como algo mutável no tempo e no espaço, dotada, portanto, de historicidade;
Entender a literatura como arte representativa de questões humanas, sociais e históricas, dotada de características específicas, como linguagem e forma;
Reconhecer a língua como elemento cultural perpassado por questões sociológicas e de constituição da identidade;
Conhecer as heranças afro-indígenas nos mais variados âmbitos do português brasileiro, seja na fonética, semântica, morfossintaxe ou léxico, bem como na literatura nacional.
Conteúdos
Conceitos de Linguagem;
Leitura, compreensão, análise e produção de textos de diferentes tipologias e gêneros;
Aspectos gramaticais da Língua Portuguesa: fonética e fonologia;
Introdução à Literatura. Identificação do contexto e das características de movimentos literários (Trovadorismo ao Arcadismo);
Introdução a obras literárias produzidas por autores negros e indígenas brasileiros;
Introdução aos aspectos históricos do português brasileiro, bem como sua influência na formação da língua.
Estratégias de ensino e aprendizagem Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem.
Bibliografia Básica BAGNO, Marcos. Nada na língua é por acaso: por uma pedagogia da variação linguística. 2. ed. São Paulo: Parábola Editorial, 2008. 238 p., il. (Educação linguística, 1). ISBN 9788588456624. CINTRA, Luís F. Lindley (Coautor). Nova gramática do português contemporâneo. 5. ed. Rio de Janeiro: Lexikon, 2008. 762 p. PRIETO, Heloisa (org.). Antologia de contos indígenas de ensinamento: tempo de histórias. São Paulo: Richmond Educação, 2021. 103 p. ISBN 9786557950104.
Bibliografia Complementar BAGNO, Marcos. Preconceito linguístico. 56. ed. rev. e ampl. São Paulo: Parábola Editorial, 2015. 350 p. (Parábola Breve, 6). ISBN 9788579340987. BAGNO, Marcos. Gramática, pra que te quero?: os conhecimentos linguísticos nos livros didáticos de português. Curitiba: Aymará, 2010. 319 p., il. col. (Mundo das ideias). Bibliografia: p.313-319. ISBN 9788578416201.
Notas de rodapé do documento (comuns aos três blocos): (*) CH – Carga horária total da unidade curricular, em horas. (*) CH Prática – Carga horária associada às atividades que têm por objetivo a aplicação de conhecimentos teóricos adquiridos, podendo ocorrer em ambiente interno ou externo, conforme diretrizes curriculares nacionais do curso. (*) CH EaD – Carga horária a distância, se houver. (*) CH com Divisão de Turma – Carga horária desenvolvida em laboratório que necessite divisão de turma ou presença de um segundo docente.
Bloco — Ano 2
Unidade Curricular: Língua Portuguesa e Literatura — Ano 2 CH Total*: 80 Semestre: 3º e 4º CH* Prática: 10h CH EaD*: não há CH com Divisão de Turma*: —
Objetivos
Reconhecer a Língua Portuguesa como um instrumento de inserção social indispensável ao pleno desenvolvimento do educando, visando seu preparo para o pleno exercício da cidadania e a qualificação para o trabalho;
Compreender a Língua Portuguesa a partir de seus diversos usos e situações comunicativas, entendendo-a como algo mutável no tempo e no espaço, dotada, portanto, de historicidade;
Entender a literatura como arte representativa de questões humanas, sociais e históricas, dotada de características específicas, como linguagem e forma.
Reconhecer a língua como elemento cultural perpassado por questões sociológicas e de constituição da identidade;
Conhecer as heranças afro-indígenas nos mais variados âmbitos do português brasileiro, seja na fonética, semântica, morfossintaxe ou léxico, bem como na literatura nacional.
Conteúdos
Leitura, compreensão, análise e produção de textos de diferentes tipologias e gêneros;
Aspectos da gramática: morfologia e morfossintaxe;
Literatura brasileira: do Romantismo ao Simbolismo;
Estudo de obras literárias produzidas por autores negros e indígenas brasileiros presentes nos movimentos literários a serem estudados;
Estudo de aspectos históricos do português brasileiro, bem como sua influência na formação da língua.
Estratégias de ensino e aprendizagem Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem.
Bibliografia Básica ASSIS, Machado de. Memórias póstumas de Brás Cubas. [S.l.]: Editora Sol, [20--?]. 243 p. SOUSA, Cruz e. Broquéis, Faróis. Jaraguá do Sul: Avenida, 2007. 219 p. (Grandes obras da língua portuguesa). ISBN 9788598610849. KRENAK, Ailton. Ideias para adiar o fim do mundo. 2. ed. 8. reimp. São Paulo: Companhia das Letras, 2020. 102 p. ISBN 9788535933581.
Bibliografia Complementar CEREJA, William Roberto; MAGALHÃES, Thereza Cochar. Gramática: texto, reflexão e uso. 3. ed. reform. São Paulo: Atual, 2008. 496 p. ISBN 9788535709988.
Bloco — Ano 3
Unidade Curricular: Língua Portuguesa e Literatura — Ano 3 CH Total*: 80 Semestre: 5º e 6º CH* Prática: 10h CH EaD*: não há CH com Divisão de Turma*: —
Objetivos
Reconhecer a Língua Portuguesa como um instrumento de inserção social indispensável ao pleno desenvolvimento do educando, visando seu preparo para o pleno exercício da cidadania e a qualificação para o trabalho;
Compreender a Língua Portuguesa a partir de seus diversos usos e situações comunicativas, entendendo-a como algo mutável no tempo e no espaço, dotada, portanto, de historicidade;
Entender a literatura como arte representativa de questões humanas, sociais e históricas, dotada de características específicas, como linguagem e forma;
Desenvolver a comunicação específica para o curso Técnico elencado.
Reconhecer a língua como elemento cultural perpassado por questões sociológicas e de constituição da identidade;
Conhecer as heranças afro-indígenas nos mais variados âmbitos do português brasileiro, seja na fonética, semântica, morfossintaxe ou léxico, bem como na literatura nacional.
Conteúdos
Leitura, compreensão, análise e produção de textos de diferentes tipologias e gêneros;
Aspectos gramaticais da Língua Portuguesa: sintaxe;
Literatura Brasileira: Pré-Modernismo, Modernismo e Literatura contemporânea;
Estudo da cultura e literatura afro-brasileira, africana e indígena;
Estudo de obras literárias produzidas por autores negros e indígenas brasileiros presentes nos movimentos literários a serem estudados;
Estudo de aspectos históricos do português brasileiro, bem como sua influência na formação da língua.
Estratégias de ensino e aprendizagem Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem.
Bibliografia Básica BARBOSA, Francisco de Assis (org.). Lima Barreto: melhores contos. 8. ed. São Paulo: Global, 2002. 174 p., 20,5 cm. (Melhores contos). ISBN 8526000810. CHAVES, Rita (org.). Contos africanos dos países de língua portuguesa. Ilustrações de Apo Fousek. São Paulo: Ática, 2021. 120 p., il. (Para gostar de ler, 44). Inclui bibliografia. ISBN 9786557670750. JESUS, Carolina Maria de. Quarto de despejo: diário de uma favelada. Ilustrações de Vinicius Rossignol Felipe. 10. ed. São Paulo: Ática, 2016. 199 p. ISBN 9788508171279.
Bibliografia Complementar BAGNO, Marcos. Preconceito linguístico. 56. ed. rev. e ampl. São Paulo: Parábola Editorial, 2015. 350 p. (Parábola Breve, 6). ISBN 9788579340987. CASTRO, Eduardo Viveiros de, 1951- (prefaciador). A queda do céu: palavras de um xamã yanomami. São Paulo: Companhia das Letras, 2015. 729 p., il. (algumas color.), 23 cm. Bibliografia: p. 694-707. ISBN 9788535926200. POLESSO, Natalia Borges. Amora: contos. São Paulo: Fundação Dorina Nowill para Cegos, 2018. 4 v. em braille.
Notas de rodapé idênticas às do bloco Ano 1 e 2.
Rodapé final do documento: "Editada pelas docentes: Karyna e Sandra"
Divergências identificadas em relação ao ementario_adm.tex
Campo "CH Prática" ausente nos 3 blocos do .tex — a fonte registra explicitamente "CH* Prática: 10h" para Ano 1, Ano 2 e Ano 3; a estrutura de tabela do ementario_adm_LIVE.tex (linhas 266, 1034, 1605) só possui colunas para "CH EaD" e "CH Total", sem nenhum campo de CH Prática — essa informação (10h de carga prática em cada um dos três anos) não aparece em lugar nenhum do ementário.
Campo "CH com Divisão de Turma" ausente nos 3 blocos do .tex — presente na fonte (em branco no Ano 1, "—" no Ano 2 e Ano 3), mas a estrutura de tabela do .tex não contempla esse campo em nenhum dos três blocos.
Ano 1 — Semestre divergente: a fonte registra "Semestre: 1º e 1º" (linha da tabela do Google Docs; aparente erro de digitação no documento de origem, provavelmente deveria ser "1º e 2º"), enquanto o .tex (linha 268) registra "Semestre: 1º e 2º". É uma divergência literal entre os dois textos — vale confirmar com as docentes responsáveis qual é o valor correto antes de decidir se o .tex deve ser alterado.
Ano 1 — Conteúdos, redação alterada: a fonte traz "Introdução à Literatura. Identificação do contexto e das características de movimentos literários (Trovadorismo ao Arcadismo);" (frase nova após ponto final, "Identificação" com inicial maiúscula); o .tex (linha 284) reformula para "Introdução à Literatura: identificação do contexto e das características de movimentos literários (Trovadorismo ao Arcadismo);" (dois-pontos, "identificação" com inicial minúscula) — alteração textual pontual, não apenas de formatação.
Ano 1 — Bibliografia Complementar incompleta: falta no .tex (linha 294) o trecho "Bibliografia: p.313-319." presente na referência de BAGNO, Marcos, Gramática, pra que te quero? na fonte.
Ano 2 — Objetivos, pontuação alterada: a fonte encerra o item "Entender a literatura como arte representativa de questões humanas, sociais e históricas, dotada de características específicas, como linguagem e forma." com ponto final (fim de item de lista), enquanto o .tex (linha 1045) usa ponto e vírgula, unindo-o ao item seguinte na mesma frase corrida — divergência apenas de pontuação, sem alteração de conteúdo.
Ano 3 — Bibliografia Básica incompleta: falta no .tex (linha 1630) o trecho "Inclui bibliografia." presente na referência de CHAVES, Rita (org.), Contos africanos dos países de língua portuguesa na fonte.
Ano 3 — Bibliografia Complementar incompleta (data de nascimento do autor): a fonte registra "CASTRO, Eduardo Viveiros de, 1951- (prefaciador)"; o .tex (linha 1634) omite ", 1951-".
Ano 3 — Bibliografia Complementar incompleta (paginação da bibliografia interna): falta no .tex (linha 1634) o trecho "Bibliografia: p. 694-707." presente na mesma referência de CASTRO, Eduardo Viveiros de, na fonte.
Observações gerais: os campos de Objetivos, Conteúdos, Metodologia/Estratégias de Ensino e Aprendizagem e as referências bibliográficas principais (autor, título, edição, local, editora, ano, ISBN) estão, de resto, fielmente reproduzidos no .tex para os três anos — não foi encontrado nenhum placeholder do tipo "[pendente...]" nos três blocos, e as cargas horárias totais (80h) e os semestres do Ano 2 e Ano 3 coincidem com a fonte.
Espanhol — Ano 1 e Ano 2 (TABELA EMENTA 5 e 22)
Fonte: Google Drive fileId 1RlWi2BTIlB1MKojNL5cTBNu5IZYiUz1Hjg4OoRxqWbA (ementa-espanhol-adm) Ementário local: /tmp/ppc/ementario_adm_LIVE.tex
TABELA EMENTA 5 — "Espanhol — Ano 1" — linhas 299–342
TABELA EMENTA 22 — "Espanhol — Ano 2" — linhas 1066–1109
Texto de origem extraído do Google Drive (na íntegra)
O documento-fonte contém três blocos de tabela, nesta ordem: um para o Ano 1, e dois blocos concorrentes para o Ano 2 (uma versão "importada do PPC Lazer" e uma versão posterior "editada pelo docente Felix Medina"). Todos os três são reproduzidos abaixo, literalmente (apenas a marcação Markdown de escape do documento original foi normalizada para leitura; nenhuma palavra foi adicionada, removida ou reordenada).
Bloco 1 — Ano 1 — [Editada pelo Docente: FELIX LOZANO]
Unidade Curricular: Espanhol — Ano 1 | Semestre: 80 CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Compreender os aspectos fonéticos e de pronúncia introdutórios da língua espanhola.
Aplicar cumprimentos, apresentações e vocabulário básico (cores, números, família, dias da semana) em interações cotidianas.
Utilizar estruturas gramaticais básicas no tempo presente, pronomes pessoais e artigos (definidos e indefinidos) em contextos de comunicação simples.
Comunicar-se em situações práticas do dia a dia, tais como compras, restaurantes e transportes.
Reconhecer e discutir aspectos de interculturalidade, incluindo costumes, tradições, cidadania, segurança no trânsito, práticas sustentáveis (meio ambiente) e direitos humanos em culturas hispanofalantes.
Conteúdos: Introdução à língua espanhola: fonética e pronúncia. Cumprimentos e apresentações. Vocabulário básico: cores, números, família, dias da semana. Estruturas gramaticais básicas: verbos no presente, pronomes pessoais, artigos definidos e indefinidos. Interculturalidade: costumes e tradições em países de língua espanhola. Comunicação em situações cotidianas: compras, restaurantes, transportes. Abordagem de Temáticas Transversais: Discussão sobre cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes.
Estratégias de ensino e aprendizagem: Aulas expositivas com uso de recursos audiovisuais (vídeos, áudios) e atividades práticas (diálogos, role-playing). Estratégias de ensino colaborativo, promovendo discussões interculturais e resolução de problemas. Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva. Em caso de carga horária EAD: utilização exclusiva do Ambiente Virtual de Aprendizagem Moodle, com livros digitais, fóruns de discussão, quizzes e vídeo-aulas. As interações síncronas serão realizadas via videoconferências e fóruns de debate, com encontros presenciais agendados para avaliações orais e escritas. A tutoria no AVA será realizada pelo próprio docente da unidade curricular. Critérios para divisão de turma: Sem divisão de turma.
Bibliografia Básica: FANJUL, Adrián (org.). Gramática y práctica de español para brasileños. 2. ed. São Paulo: Moderna, 2011. 287 p., il., + 1 CD-ROM. ISBN 9788516074272. MORENO, Concha; TUTS, Martina. Cinco estrellas: español para el turismo. 2. ed. Madrid: SGEL, 2011. 223 p., il., + 1 CD-ROM. ISBN 9788497784849.
Bibliografia Complementar: GONZÁLEZ HERMOSO, Alfredo. Conjugar: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p., il., + 1 CD-ROM. ISBN 9788477117186. HERMOSO, A. G. Conjugar es fácil. [s.l.]: EDELSA, 1997. PEREZ, Aquilino Sanches. Diccionario básico de la lengua española. [s.l.]: SGEL, 1987. BALLESTERO-ALVAREZ, M. E.; BALBÁS, M. S. Minidicionário: espanhol-português, português-espanhol. São Paulo: FTD, 2007.
(*) CH – Carga horária EaD, se houver. (*) CH – Carga horária total da unidade curricular em horas.
Bloco 2 — Ano 2 — [importada diretamente do PPC Lazer]
Unidade Curricular: Espanhol — Ano 2 | CH Total*: 80 | Semestre: 3º e 4º CH* Prática: [A preencher] | CH EaD*: — | CH com Divisão de Turma*: —
(Este bloco não possui seção "Objetivos".)
Conteúdos: Revisão de estruturas gramaticais básicas. Tempos verbais no passado: pretérito perfeito e imperfeito. Vocabulário ampliado: alimentos, roupas, lazer, clima. Interculturalidade: celebrações, festividades e cultura popular nos países hispanofalantes. Comunicação em situações intermediárias: descrevendo pessoas, lugares e eventos. Introdução à escrita de textos breves: cartas e e-mails informais. História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões sobre os direitos humanos.
Estratégias de ensino e aprendizagem: Abordagem comunicativa com ênfase em situações da vida real, incluindo simulações e diálogos. Uso de plataformas digitais para atividades de escrita colaborativa e discussões sobre temas culturais e transversais. Em caso de EAD: Moodle será utilizado com quizzes interativos, fóruns de discussão, e vídeo-aulas. Sessões síncronas para prática de fala e escrita ocorrerão via videoconferência, com encontros presenciais opcionais para reforço e avaliações. O AVA será revisado periodicamente para assegurar a acessibilidade e melhorar a experiência de aprendizagem.
Bibliografia Básica: FANJUL, Adrián (org.). Gramática y práctica de español para brasileños. 2. ed. São Paulo: Moderna, 2011. 287 p., il., + 1 CD-ROM. ISBN 9788516074272. Atenção: as referências indicadas no PPC devem ser elaboradas de acordo com a norma NBR 6023:2018.
Bibliografia Complementar: GONZÁLEZ HERMOSO, Alfredo. Conjugar: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p., il., + 1 CD-ROM. ISBN 9788477117186. COTO BAUTISTA, Vanessa; TURZA FERRÉ, Anna. Tema a tema B1: español lengua extranjera : curso de conversación. Madrid: Edelsa, 2011. 111 p., il., 28 cm. ISBN 9788477117209. Wildner, Ana Kaciara. Espanhol para o turismo / Ana Kaciara Wildner, Leandra Cristina de Oliveira, Mary Anne Warken Sobottka. – Florianópolis: Publicação do IFSC, 2014. Atenção: as referências indicadas no PPC devem ser elaboradas de acordo com a norma NBR 6023:2018.
(*) CH – Carga horária total da unidade curricular, em horas. (*) CH Prática – Carga horária associada às atividades que têm por objetivo a aplicação de conhecimentos teóricos adquiridos, podendo ocorrer em ambiente interno ou externo, conforme diretrizes curriculares nacionais do curso. (*) CH EaD – Carga horária a distância, se houver. (*) CH com Divisão de Turma – Carga horária desenvolvida em laboratório que necessite divisão de turma ou presença de um segundo docente.
Bloco 3 — Ano 2 — [Editada pelo Docente: Felix Medina]
Unidade Curricular: Espanhol — Ano 2 | Semestre: 80 CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Revisar e consolidar as estruturas gramaticais básicas da língua espanhola.
Compreender e aplicar tempos verbais no passado (pretérito perfeito e imperfeito).
Expandir o vocabulário em eixos temáticos específicos, tais como alimentos, roupas, lazer e clima.
Desenvolver habilidades de comunicação em situações de nível intermediário, capacitando para a descrição de pessoas, lugares e eventos.
Redigir textos breves e funcionais, como cartas e e-mails informais.
Analisar criticamente manifestações da cultura popular e celebrações hispânicas, articulando reflexões sobre direitos humanos, alimentação saudável e História e Cultura Afro-Brasileira e Indígena.
Conteúdos: Revisão de estruturas gramaticais básicas. Tempos verbais no passado: pretérito perfeito e imperfeito. Vocabulário ampliado: alimentos, roupas, lazer, clima. Interculturalidade: celebrações, festividades e cultura popular nos países hispanofalantes. Comunicação em situações intermediárias: descrevendo pessoas, lugares e eventos. Introdução à escrita de textos breves: cartas e e-mails informais. Abordagem de Temáticas Transversais: História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões integradas sobre os direitos humanos.
Estratégias de ensino e aprendizagem: Abordagem comunicativa com ênfase em situações da vida real, priorizando o uso prático do idioma por meio de simulações e diálogos. Uso de plataformas digitais para o desenvolvimento de atividades de escrita colaborativa e debates sobre temas culturais e transversais. Em caso de oferta de carga horária EAD: utilização exclusiva do Ambiente Virtual de Aprendizagem Moodle, incorporando quizzes interativos, fóruns de discussão orientados e vídeo-aulas. Serão implementadas sessões síncronas via videoconferência voltadas especificamente para a prática de fala e produção escrita, com suporte de momentos assíncronos e encontros presenciais opcionais para reforço e avaliações. A tutoria no AVA será realizada diretamente pelo docente da UC. Critérios para divisão de turma: Sem divisão de turma.
Bibliografia Básica: FANJUL, Adrián (org.). Gramática y práctica de español para brasileños. 2. ed. São Paulo: Moderna, 2011. 287 p., il., + 1 CD-ROM. ISBN 9788516074272. MORENO, Concha; TUTS, Martina. Cinco estrellas: español para el turismo. 2. ed. Madrid: SGEL, 2011. 223 p., il., + 1 CD-ROM. ISBN 9788497784849.
Bibliografia Complementar: GONZÁLEZ HERMOSO, Alfredo. Conjugar: verbos de España y de América. Madrid: Edelsa Grupo Didascalia, 2011. 318 p., il., + 1 CD-ROM. ISBN 9788477117186. COTO BAUTISTA, Vanessa; TURZA FERRÉ, Anna. Tema a tema B1: español lengua extranjera : curso de conversación. Madrid: Edelsa, 2011. 111 p., il., 28 cm. ISBN 9788477117209. WILDNER, Ana Kaciara; OLIVEIRA, Leandra Cristina de; SOBOTTKA, Mary Anne Warken. Espanhol para o turismo. Florianópolis: Publicação do IFSC, 2014. (Referência ajustada formalmente de acordo com a NBR 6023:2018).
(*) CH – Carga horária EaD, se houver. (*) CH – Carga horária total da unidade curricular em horas.
Divergências identificadas em relação ao ementario_adm.tex
O ementário (linhas 299–342 e 1066–1109) segue, em conteúdo, o Bloco 1 (Ano 1 — Felix Lozano) e o Bloco 3 (Ano 2 — Felix Medina), ignorando o Bloco 2 (Ano 2 — versão importada do PPC Lazer). Isso está correto/coerente, pois o Bloco 3 é a versão editada pelo docente que substitui o rascunho importado, e o texto do ementário corresponde quase palavra por palavra a ela. Ainda assim, foram identificadas as seguintes divergências concretas:
[Ano 1 e Ano 2] Bibliografia Básica e Complementar — dados bibliográficos omitidos. A fonte traz, em toda referência, paginação, ilustrações, indicação de CD-ROM e ISBN (ex.: "287 p., il., + 1 CD-ROM. ISBN 9788516074272."). O ementário (linhas 331–332, 334–337, 1099–1100, 1102–1104) mantém apenas autor, título, edição, cidade, editora e ano, removendo sistematicamente paginação/ilustração/CD-ROM/ISBN de todas as 9 referências (2 básicas + 4 complementares no Ano 1; 2 básicas + 3 complementares no Ano 2).
[Ano 1 e Ano 2] Campo "Semestre" não confirmável literalmente na fonte. Nos blocos editados pelos docentes (Bloco 1 e Bloco 3), a célula de cabeçalho da tabela-fonte mostra "Semestre: 80" (aparentemente um erro/artefato de preenchimento da tabela no Google Docs, repetindo o valor de CH Total em vez de um semestre). O ementário exibe "1º e 2º" (linha 303) para o Ano 1 e "3º e 4º" (linha 1070) para o Ano 2 — valores plausíveis (o "3º e 4º" só aparece literalmente no Bloco 2, a versão importada e não utilizada), mas não confirmáveis letra-por-letra nos blocos-fonte efetivamente seguidos pelo ementário. Recomenda-se confirmar com o docente responsável se "80" no campo Semestre da fonte é de fato um erro de digitação/tabela.
[Ano 1] Paráfrase no encerramento de "Conteúdos". Fonte: "Abordagem de Temáticas Transversais: Discussão sobre cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes." Ementário (linha 325): "Temáticas transversais: cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes." — sentido preservado, mas não é cópia literal ("Abordagem de" e "Discussão sobre" foram suprimidos).
[Ano 2] Paráfrase equivalente no encerramento de "Conteúdos". Fonte: "Abordagem de Temáticas Transversais: História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões integradas sobre os direitos humanos." Ementário (linha 1093): "Temáticas transversais: História e Cultura Afro-Brasileira e Indígena em contextos hispanofalantes, alimentação saudável e educação alimentar, e reflexões integradas sobre os direitos humanos." — mesmo padrão de simplificação da 3.
[Ano 2] Paráfrase na Metodologia. Fonte: "Serão implementadas sessões síncronas via videoconferência voltadas especificamente para a prática de fala e produção escrita, com suporte de momentos assíncronos e encontros presenciais opcionais para reforço e avaliações." Ementário (linha 1096): "sessões síncronas via videoconferência voltadas à prática de fala e produção escrita, com momentos assíncronos e encontros presenciais opcionais para reforço e avaliações" — conteúdo preservado, mas reescrito (não literal).
[Fonte] Duas versões conflitantes do Ano 2 no documento-fonte, apenas uma delas usada. O documento-fonte contém o Bloco 2 ("importada diretamente do PPC Lazer" — sem seção de Objetivos, com CH Prática "[A preencher]", CH EaD "—", CH com Divisão de Turma "—", bibliografia básica com apenas 1 título e nota de NBR 6023:2018) e o Bloco 3 ("Editada pelo Docente: Felix Medina" — com Objetivos, CH EaD "00 h", bibliografia básica com 2 títulos). O ementário usa integralmente o Bloco 3. Isso parece correto (versão mais completa/final), mas fica registrado pois representa uma divergência estrutural real dentro da própria fonte que merece confirmação institucional sobre qual versão é a oficial.
[Ano 2] Notas editoriais da fonte não reproduzidas no ementário. A nota "Atenção: as referências indicadas no PPC devem ser elaboradas de acordo com a norma NBR 6023:2018" (presente na Bibliografia Básica e Complementar dos Blocos 2) e a nota "(Referência ajustada formalmente de acordo com a NBR 6023:2018)" (após a referência WILDNER no Bloco 3) não aparecem no ementário. São instruções/observações editoriais, não referências bibliográficas em si — omissão de baixo impacto, mas registrada por completude.
Nenhuma divergência foi encontrada em: Objetivos (Ano 1 e Ano 2 — reproduzidos literalmente), ordem e conteúdo essencial dos Conteúdos, CH EaD (00h) e CH Total (80h) de ambos os anos, "Sem divisão de turma" em ambos os anos, e no campo Avaliação do Ano 2 (o ementário registra corretamente "Não especificado no documento fonte", pois a fonte de fato não traz uma sentença de avaliação separada para o Ano 2 na versão Felix Medina). Não foram encontrados placeholders do tipo "[pendente...]" cobrindo conteúdo que a fonte já preenche.
Biologia — Ano 1 e Ano 3 (TABELA EMENTA 6 e 35)
Texto de origem extraído do Google Drive (na íntegra)
Cabeçalho do documento
Unidade Curricular: Biologia
Ano 1 [Editada pelo Docente: Cristiane Oliveira da Silva]
Campo
Conteúdo
Unidade Curricular:
Biologia I
Ano:
1
Semestre:
1º e 2º
CH EaD*:
00 h
CH Total*:
80 h
Objetivos:
Compreender a Biologia como uma ciência em permanente construção, reconhecendo sua importância para o entendimento da origem, evolução e diversificação da vida, bem como sua relação com o desenvolvimento científico, tecnológico e social.
Reconhecer a célula como unidade estrutural, funcional e genética dos seres vivos, compreendendo a organização celular, os processos metabólicos e os mecanismos envolvidos na manutenção da vida.
Entender os processos de multiplicação celular, reprodução sexuada e anatomofisiologia do corpo humano, relacionando-os à continuidade da vida, à diversidade genética e à saúde humana.
Desenvolver habilidades de observação, investigação e experimentação, utilizando procedimentos próprios das ciências biológicas para formular hipóteses, analisar evidências, interpretar resultados e resolver problemas.
Promover o autocuidado, o empoderamento e o respeito à pluralidade de corpos e gêneros por meio da compreensão dos princípios da educação alimentar e nutricional, da saúde integral e da sexualidade na adolescência.
Conteúdos:
Origem da vida: teorias e descobertas recentes.
Astrobiologia.
A invenção do microscópio e a descoberta da célula.
Células procarióticas e eucarióticas (animais e vegetais).
Componentes químicos celulares: água, macromoléculas, vitaminas e sais minerais.
Educação Alimentar e Nutricional.
Estrutura e funcionamento celular: membrana plasmática, citoplasma, organelas citoplasmáticas, citoesqueleto e núcleo.
Metabolismo energético: respiração celular, fermentação, fotossíntese e quimiossíntese.
Ciclo celular: interfase e divisão celular (mitose e meiose).
Reprodução animal: fecundação e desenvolvimento embrionário.
Histologia, anatomia e fisiologia humana: tecidos básicos e sistemas orgânicos.
Saúde e sexualidade na adolescência.
Estratégias de ensino e aprendizagem: O processo de ensino-aprendizagem será conduzido por meio de uma abordagem dialógica, contextualizada e investigativa, buscando o levantamento dos saberes prévios dos estudantes, a problematização de situações reais, a articulação com outras áreas do conhecimento e o desenvolvimento do pensamento crítico e científico. A metodologia de ensino será baseada em estratégias didáticas diversificadas, conforme os objetivos de aprendizagem e as especificidades de cada conteúdo, tais como: aulas expositivo-dialogadas utilizando quadro e projetor multimídia; atividades práticas em campo e laboratório; análise de experimentos e estudos de caso; discussão de textos, imagens e vídeos científicos; uso de atlas digitais, softwares de animação e simulação, modelos didáticos tridimensionais e jogos educativos; debate de temas transversais; e participação em visitas técnicas e eventos científicos. As aulas práticas serão realizadas, preferencialmente, no pátio do câmpus e no Laboratório de Biociências, compondo uma média de 20h anuais, divididas em 10h para cada semestre letivo. Caso houver um segundo professor ministrante da UC, a turma poderá ser dividida em A e B, considerando a capacidade do espaço e a dinâmica da atividade proposta. A avaliação da aprendizagem se dará em uma perspectiva processual e formativa, observando-se a evolução dos conhecimentos construídos ao longo do período letivo. Os instrumentos avaliativos serão aplicados de forma individual ou coletiva, podendo ser: estudos dirigidos; listas de exercícios focados em ENEM e vestibulares; provas teóricas; relatórios de atividades experimentais; projetos, seminários ou oficinas temáticas; e avaliação atitudinal. O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) será empregado como Ambiente Virtual de Aprendizagem (AVA) para disponibilização de plano de ensino, cronograma de conteúdos e atividades, materiais de apoio, tarefas avaliativas, orientações e acompanhamento da frequência e do desempenho escolar.
Bibliografia Básica: JUNQUEIRA, Luiz Carlos Uchoa; CARNEIRO, José. Biologia celular e molecular. 9. ed. Rio de Janeiro: Guanabara Koogan, 2012. 364 p., il., color.;, 28 cm. ISBN 9788527720786. SADAVA, David et al. Vida: a ciência da biologia: volume 1: célula e hereditariedade. 8. ed. Porto Alegre: Artmed, 2009. 461 p., il. ISBN 9788536319216. Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE).
Bibliografia Complementar: BRUCE, Alberts et al. Biologia molecular da célula. 6. ed. Porto Alegre: Artmed, 2017. 1427 p., il., color. ISBN 9788582714225. CAMPBELL, Mary K.; FARRELL, Shawn O. Bioquímica. 2. ed. São Paulo: Cengage Learning, 2016. 812 p., il., color. Inclui bibliografia e índice. ISBN 9788522118700. KIERSZENBAUM, Abraham L.; TRES, Laura L. Histologia e biologia celular: uma introdução à patologia. 3. ed. Rio de Janeiro: Elsevier, 2012. 699 p., il., color. ISBN 9788535247374.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Ano 3 [Editada pelo Docente: Cristiane Oliveira da Silva]
Campo
Conteúdo
Unidade Curricular:
Biologia II
Ano:
3
Semestre:
1º e 2º
CH EaD*:
00 h
CH Total*:
80 h
Objetivos:
Analisar a estrutura e a expressão do material genético, compreendendo os mecanismos da variabilidade genética e da hereditariedade e suas aplicações em diferentes contextos científicos e tecnológicos.
Avaliar criticamente os avanços da Biotecnologia e suas implicações éticas, sociais, ambientais e econômicas, fundamentando-se em evidências científicas para a tomada de decisões responsáveis frente aos desafios tecnológicos e socioambientais contemporâneos.
Compreender a diversidade dos seres vivos, reconhecendo suas categorias taxonômicas, relações evolutivas, características biológicas, estratégias adaptativas, interações com o ambiente e importância para o equilíbrio dos ecossistemas e a sustentabilidade das sociedades humanas.
Desenvolver habilidades de observação e experimentação científica de modo a identificar e explicar fenômenos biológicos e processos tecnológicos decorrentes da utilização de organismos vivos na produção industrial, na saúde pública e na conservação ambiental.
Valorizar a diversidade biológica e cultural dos ecossistemas regionais, reconhecendo a contribuição dos saberes tradicionais africanos e indígenas para a relação com a natureza, o uso sustentável dos recursos naturais e a promoção da saúde individual e coletiva.
Conteúdos:
Biologia molecular: DNA, RNA e expressão gênica (transcrição e tradução).
Genética e hereditariedade: conceitos básicos, leis de Mendel e padrões de herança.
Temas contemporâneos em Biotecnologia e Bioética: células-tronco, clonagem, transgênicos, edição genética, experimentação animal, genética forense, entre outros.
Evolução biológica: teorias, evidências e mecanismos evolutivos.
Diversidade e classificação dos seres vivos: vírus, bactérias, algas, protozoários, fungos, plantas e animais.
Ecologia: sistemas ecológicos e serviços ecossistêmicos.
Educação Ambiental e Cultura Oceânica.
História e Cultura Afro-Brasileira, Africana e Indígena.
Estratégias de ensino e aprendizagem: O processo de ensino-aprendizagem será conduzido por meio de uma abordagem dialógica, contextualizada e investigativa, buscando o levantamento dos saberes prévios dos estudantes, a problematização de situações reais, a articulação com outras áreas do conhecimento e o desenvolvimento do pensamento crítico e científico. A metodologia de ensino será baseada em estratégias didáticas diversificadas, conforme os objetivos de aprendizagem e as especificidades de cada conteúdo, tais como: aulas expositivo-dialogadas utilizando quadro e projetor multimídia; atividades práticas em campo e laboratório; análise de experimentos e estudos de caso; discussão de textos, imagens e vídeos científicos; uso de atlas digitais, softwares de animação e simulação, modelos didáticos tridimensionais e jogos educativos; debate de temas transversais; e participação em visitas técnicas e eventos científicos. As aulas práticas serão realizadas, preferencialmente, no pátio do câmpus e no Laboratório de Biociências, compondo uma média de 20h anuais, divididas em 10h para cada semestre letivo. Caso houver um segundo professor ministrante da UC, a turma poderá ser dividida em A e B, considerando a capacidade do espaço e a dinâmica da atividade proposta. A avaliação da aprendizagem se dará em uma perspectiva processual e formativa, observando-se a evolução dos conhecimentos construídos ao longo do período letivo. Os instrumentos avaliativos serão aplicados de forma individual ou coletiva, podendo ser: estudos dirigidos; listas de exercícios focados em ENEM e vestibulares; provas teóricas; relatórios de atividades experimentais; projetos, seminários ou oficinas temáticas; e avaliação atitudinal. O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) será empregado como Ambiente Virtual de Aprendizagem (AVA) para disponibilização de plano de ensino, cronograma de conteúdos e atividades, materiais de apoio, tarefas avaliativas, orientações e acompanhamento da frequência e do desempenho escolar.
Bibliografia Básica: GRIFFITHS, Anthony J. F. Introdução à genética. Tradução de Idilia Vanzellotti. 10. ed. Rio de Janeiro: Guanabara Koogan, 2013. 710 p., il., color. ISBN 9788527721912. REECE, Jane B. Biologia de Campbell. Revisão de Denise Cantarelli Machado, Gaby Renard, Paulo Luiz de Oliveira. 10. ed. Porto Alegre: Artmed, 2015. xlv, 1442, il. (algumas col.). ISBN 9788582712160. Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE).
Bibliografia Complementar: BEGON, Michael; TOWNSEND, Colin R.; HARPER, John L. Ecologia: de indivíduos a ecossistemas. 4. ed. Porto Alegre: Artmed, 2007. 740 p., 21X28. Inclui bibliografia. ISBN 9788536308845. CASTRO, Peter; HUBER, Michael E. Biologia marinha. 8. ed. Porto Alegre: Artmed, 2012. 461 p., il., color. Inclui bibliografia e índice. ISBN 9788580551020. DARWIN, Charles, 1809-1882. A origem das espécies e a seleção natural. Tradução de Soraya Freitas. São Paulo: Madras, 2011. 462 p. ISBN 9788537006573.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Divergências identificadas em relação ao ementario_adm.tex
Nome da UC (Ano 1 e Ano 3): a fonte nomeia a unidade curricular como "Biologia I" (Ano 1) e "Biologia II" (Ano 3); o LaTeX (linhas 346 e 1644) usa apenas "Biologia — Ano 1" e "Biologia — Ano 3", sem a numeração I/II presente na fonte.
Semestre do Ano 3 divergente: a fonte indica, textualmente, "Semestre: 1º e 2º" para a UC do Ano 3 (Biologia II) — idêntico ao valor do Ano 1 —, enquanto o LaTeX (linha 1644, TABELA EMENTA 35) registra "5º e 6º". Há divergência de classificação de semestre entre fonte e ementário; é necessário verificar junto ao docente/coordenação qual valor está correto, pois a fonte pode conter um erro de preenchimento (repetição do valor do Ano 1), mas o ementário não pode simplesmente divergir sem essa confirmação.
Conteúdos — Ano 1, itens fundidos: na fonte, "Origem da vida: teorias e descobertas recentes." e "Astrobiologia." são dois itens de lista separados; no LaTeX (linha 362) foram unidos em um único item: "Origem da vida: teorias e descobertas recentes; astrobiologia." (com "astrobiologia" em minúsculo). Da mesma forma, "Componentes químicos celulares: água, macromoléculas, vitaminas e sais minerais." e "Educação Alimentar e Nutricional." são dois itens separados na fonte, mas foram unidos em um único item no LaTeX (linha 365): "...sais minerais; Educação Alimentar e Nutricional." O conteúdo textual foi preservado, mas a estrutura de itens (12 itens na fonte → 10 itens no LaTeX) foi alterada/resumida.
Metodologia (Ano 1 e Ano 3) — texto substancialmente resumido: o campo "Metodologia" do ementário é uma versão condensada do texto da fonte, com as seguintes perdas de conteúdo:
Omitida a frase "a articulação com outras áreas do conhecimento e o desenvolvimento do pensamento crítico e científico".
Omitido o detalhamento "divididas em 10h para cada semestre letivo" (o ementário mantém apenas "média de 20h anuais").
Omitida integralmente a frase: "Caso houver um segundo professor ministrante da UC, a turma poderá ser dividida em A e B, considerando a capacidade do espaço e a dinâmica da atividade proposta."
O uso do SIGAA foi reduzido a "SIGAA utilizado como Ambiente Virtual de Aprendizagem", omitindo o detalhamento da fonte: "para disponibilização de plano de ensino, cronograma de conteúdos e atividades, materiais de apoio, tarefas avaliativas, orientações e acompanhamento da frequência e do desempenho escolar." Essa mesma perda de conteúdo se repete identicamente no bloco do Ano 3, pois a fonte usa o mesmo parágrafo de metodologia/avaliação para as duas UCs.
Bibliografia Básica e Complementar (Ano 1 e Ano 3) — detalhamento bibliográfico omitido: as referências (autor, título, edição, editora, ano) coincidem entre fonte e ementário para todos os títulos (JUNQUEIRA/CARNEIRO; SADAVA; livro FNDE; BRUCE et al.; CAMPBELL/FARRELL; KIERSZENBAUM/TRES no Ano 1 — e GRIFFITHS; REECE; livro FNDE; BEGON/TOWNSEND/HARPER; CASTRO/HUBER; DARWIN no Ano 3). Porém, o ementário omite, em todas as entradas, o número de páginas e o ISBN presentes na fonte (e, no caso de REECE e DARWIN, também omite os nomes dos revisores/dados biográficos do autor). Não há referências ausentes ou adicionadas — apenas informação complementar suprimida.
Nenhum placeholder do tipo "[pendente...]" foi encontrado no ementário para esta UC; as cargas horárias (00h EaD / 80h Total) coincidem em ambos os anos.
Física — Ano 1, 2 e 3 (TABELA EMENTA 7, 23 e 36)
Fonte: Google Drive, fileId 15dWZqVtRKttF23x4cFABjNLdTZ9X0StIX2Mavz43dcM (ementa-fisica-adm). Nota: o documento-fonte traz o cabeçalho "[Editada pelo Docente: JEAN]" e nomeia as UCs como Física I, Física II e Física III (não "Física — Ano 1/2/3"); é a mesma convenção de nomes ao longo de toda a fonte.
Texto de origem extraído do Google Drive (na íntegra)
Bloco 1 — Física I
Unidade Curricular: Física I | Semestre: 2 CH EaD:* 00 h | CH Total:* 40 h
Objetivos:
Compreender a Física como ciência, reconhecendo sua evolução histórica, seus principais ramos e sua importância para a compreensão dos fenômenos naturais e para o desenvolvimento científico e tecnológico.
Identificar e utilizar corretamente as grandezas físicas fundamentais e derivadas, bem como o Sistema Internacional de Unidades (SI) e suas conversões.
Desenvolver a capacidade de interpretar fenômenos físicos por meio da linguagem matemática, da análise de gráficos, tabelas e relações entre grandezas.
Compreender os conceitos fundamentais da Cinemática, descrevendo e analisando o movimento de corpos em diferentes referenciais.
Aplicar as equações do Movimento Uniforme (MU) e do Movimento Uniformemente Variado (MUV) na resolução de problemas envolvendo deslocamento, velocidade e aceleração.
Interpretar e construir gráficos de posição, velocidade e aceleração em função do tempo, relacionando suas características aos diferentes tipos de movimento.
Compreender os conceitos fundamentais da Dinâmica, identificando as forças que atuam sobre um corpo e seus efeitos sobre o movimento.
Analisar e aplicar as Leis de Newton na interpretação e resolução de problemas relacionados ao equilíbrio e ao movimento de corpos.
Desenvolver o raciocínio lógico e quantitativo na resolução de problemas físicos, empregando estratégias adequadas, argumentação científica e interpretação dos resultados obtidos.
Relacionar os conceitos estudados com situações do cotidiano, reconhecendo a presença e a aplicação dos princípios da Mecânica em diferentes contextos científicos, tecnológicos e sociais.
Conteúdos: Introdução à Física: a origem da Física, as áreas da Física, grandezas físicas e unidades de medidas; Noções básicas de Cinemática; Cinemática ; Movimento Uniforme e Movimento Uniformemente Variado; Dinâmica (introdução) ; Leis de Newton e suas aplicações.
Estratégias de ensino e aprendizagem: As aulas serão em sua maioria expositivas e dialogadas, sob a perspectiva de uma proposta dialógico-problematizadora a partir de fenômenos naturais, tecnológicos e produtivos do mundo do trabalho. A prática docente será pautada em três momentos pedagógicos: a problematização inicial, a organização e a aplicação dos conhecimentos. Os conteúdos serão tratados de forma contextualizada e interdisciplinar, sempre seguidos de resolução de listas de exercícios e problemas. Outros procedimentos didático-metodológicos serão utilizados, tais como: exposição de vídeos; seminários; trabalhos de pesquisa; montagem e apresentação de experimentos; elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica; desenvolvimento de projetos; interpretação de textos técnicos e científicos relacionados aos conteúdos trabalhados. Os recursos utilizados serão: livros didáticos, livros digitais, listas de exercícios, apostilas, lousa, projetor multimídia, computador, equipamentos de laboratório, textos e artigos acadêmicos da área, reproduções de imagens e vídeos da área. A avaliação se dará em uma perspectiva formativa levando em conta todas as atividades realizadas pelos estudantes.
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). HEWITT, Paul G. Física conceitual. 12. ed. Porto Alegre: Bookman, 2015. LUZ, Antônio Máximo Ribeiro da; ALVARENGA, Beatriz Gonçalves de. Curso de física, volume 1. 6. ed. rev. ampl. São Paulo: Scipione, 2006.
Bibliografia Complementar: BARRETO FILHO, Benigno; SILVA, Cláudio Xavier da. 360º: física: aula por aula: volume único. 3. ed. São Paulo: FTD, 2015. YAMAMOTO, Kazuhito; FUKE, Luiz Felipe. Física para o ensino médio 1: mecânica. 3. ed. São Paulo: Saraiva, 2013. KNIGHT, Randall D. Física: uma abordagem estratégica: volume 1: mecânica newtoniana, gravitação, oscilações e ondas. Tradução de Trieste Freire Ricci. 2. ed. Porto Alegre: Bookman, 2009.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Bloco 2 — Física II
Unidade Curricular: Física II | Semestre: 3 e 4 CH EaD:* 00 h | CH Total:* 80 h
Objetivos:
Compreender os conceitos de trabalho, energia e potência, analisando as transformações de energia e aplicando o princípio da conservação da energia mecânica na interpretação e resolução de problemas físicos.
Analisar os conceitos de impulso e quantidade de movimento, aplicando o princípio da conservação da quantidade de movimento na resolução de problemas envolvendo colisões e interações entre corpos.
Compreender os fundamentos da Gravitação Universal, relacionando a interação gravitacional aos movimentos de corpos celestes e aos fenômenos observados no cotidiano.
Identificar e aplicar os princípios da Hidrostática, analisando pressão, empuxo e equilíbrio dos fluidos em repouso em situações práticas e tecnológicas.
Compreender os conceitos de temperatura, calor, dilatação térmica e comportamento dos gases ideais, interpretando os fenômenos térmicos por meio de modelos físicos e relações matemáticas.
Aplicar as Leis da Termodinâmica na análise das transformações de energia, reconhecendo o funcionamento, as limitações e a eficiência das máquinas térmicas.
Compreender os fenômenos da reflexão e da refração da luz, analisando a formação de imagens e a propagação da luz em diferentes meios.
Compreender os princípios do movimento ondulatório, identificando as características das ondas e relacionando os fenômenos de propagação, reflexão, refração, difração e interferência a situações do cotidiano e aplicações tecnológicas.
Desenvolver o raciocínio lógico, quantitativo e científico por meio da resolução de problemas, da interpretação de gráficos, tabelas e representações matemáticas relacionadas aos fenômenos físicos estudados.
Relacionar os conceitos de Mecânica, Termologia, Óptica e Ondulatória com fenômenos naturais, aplicações tecnológicas e situações do cotidiano, reconhecendo a importância da Física para a compreensão do mundo e para o desenvolvimento científico e tecnológico.
Conteúdos: Trabalho de uma força e Conservação da Energia Mecânica; Impulso e Conservação da quantidade de movimento; Gravitação Universal; Hidrostática; Termometria, Dilatação Térmica e Gás Ideal; Leis da Termodinâmica e Máquinas Térmicas; Reflexão da Luz e Refração da Luz; Movimento Ondulatório.
Estratégias de ensino e aprendizagem: As aulas serão em sua maioria expositivas e dialogadas, sob a perspectiva de uma proposta dialógico-problematizadora a partir de fenômenos naturais, tecnológicos e produtivos do mundo do trabalho. A prática docente será pautada em três momentos pedagógicos: a problematização inicial, a organização e a aplicação dos conhecimentos. Os conteúdos serão tratados de forma contextualizada e interdisciplinar, sempre seguidos de resolução de listas de exercícios e problemas. Outros procedimentos didático-metodológicos serão utilizados, tais como: exposição de vídeos; seminários; trabalhos de pesquisa; montagem e apresentação de experimentos; elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica; desenvolvimento de projetos; interpretação de textos técnicos e científicos relacionados aos conteúdos trabalhados. Os recursos utilizados serão: livros didáticos, livros digitais, listas de exercícios, apostilas, lousa, projetor multimídia, computador, equipamentos de laboratório, textos e artigos acadêmicos da área, reproduções de imagens e vídeos da área. A avaliação se dará em uma perspectiva formativa levando em conta todas as atividades realizadas pelos estudantes.
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). HEWITT, Paul G. Física conceitual. 12. ed. Porto Alegre: Bookman, 2015. LUZ, Antônio Máximo Ribeiro da; ALVARENGA, Beatriz Gonçalves de. Curso de física, volume 1. 6. ed. rev. ampl. São Paulo: Scipione, 2006. LUZ, Antônio Máximo Ribeiro da; ALVARENGA, Beatriz Gonçalves de. Curso de física, volume 2. 6. ed. rev. ampl. São Paulo: Scipione, 2006.
Bibliografia Complementar: BARRETO FILHO, Benigno; SILVA, Cláudio Xavier da. 360º: física: aula por aula: volume único. 3. ed. São Paulo: FTD, 2015. YAMAMOTO, Kazuhito; FUKE, Luiz Felipe. Física para o ensino médio 2: termologia, óptica, ondulatória. 3. ed. São Paulo: Saraiva, 2013. KNIGHT, Randall D. Física: uma abordagem estratégica: volume 2: termodinâmica e óptica. Tradução de Trieste Freire Ricci. 2. ed. Porto Alegre: Bookman, 2009.
Bloco 3 — Física III
Unidade Curricular: Física III | Semestre: 4 e 5 CH EaD:* 00 h | CH Total:* 80 h
Objetivos:
Compreender os conceitos fundamentais da eletrostática, analisando a interação entre cargas elétricas por meio da força eletrostática, do campo elétrico, do potencial elétrico e da energia potencial elétrica.
Aplicar os conceitos de corrente elétrica, tensão, resistência e potência na análise e resolução de problemas envolvendo circuitos elétricos de corrente contínua (CC) e corrente alternada (CA).
Identificar as características e aplicações dos principais componentes de circuitos elétricos, interpretando esquemas elétricos e analisando associações de resistores em série e em paralelo.
Compreender os princípios do magnetismo, analisando a interação entre campos magnéticos, correntes elétricas e materiais magnéticos em diferentes contextos físicos e tecnológicos.
Explicar os fenômenos da indução eletromagnética, relacionando-os ao funcionamento de dispositivos como geradores, transformadores e motores elétricos.
Compreender a natureza e as propriedades das ondas eletromagnéticas, reconhecendo sua propagação, classificação e aplicações nas diferentes tecnologias de comunicação, medicina, indústria e pesquisa científica.
Identificar os fundamentos da Física Moderna, reconhecendo as limitações da Física Clássica e compreendendo os princípios básicos da Relatividade e da Mecânica Quântica, bem como suas principais aplicações tecnológicas.
Desenvolver o raciocínio lógico, quantitativo e científico por meio da resolução de problemas, da interpretação de gráficos, tabelas, diagramas e modelos matemáticos relacionados aos fenômenos eletromagnéticos e modernos.
Relacionar os conceitos de Eletrostática, Eletrodinâmica, Magnetismo, Ondas Eletromagnéticas e Física Moderna com fenômenos naturais, aplicações tecnológicas e situações do cotidiano, reconhecendo sua importância para o avanço científico e tecnológico.
Conteúdos: Carga elétrica, Força Eletrostática, Campo Elétrico, Potencial Elétrico e Energia Potencial Elétrica; Corrente elétrica, Tipos de Corrente Elétrica, Resistores e Circuitos Elétricos CC e CA; Diagramas de circuitos — unifilar e multifilar (aplicações); Magnetismo e Indução Eletromagnética; Ondas Eletromagnéticas; Introdução à Física Moderna.
Estratégias de ensino e aprendizagem: As aulas serão em sua maioria expositivas e dialogadas, sob a perspectiva de uma proposta dialógico-problematizadora a partir de fenômenos naturais, tecnológicos e produtivos do mundo do trabalho. A prática docente será pautada em três momentos pedagógicos: a problematização inicial, a organização e a aplicação dos conhecimentos. Os conteúdos serão tratados de forma contextualizada e interdisciplinar, sempre seguidos de resolução de listas de exercícios e problemas. Outros procedimentos didático-metodológicos serão utilizados, tais como: exposição de vídeos; seminários; trabalhos de pesquisa; montagem e apresentação de experimentos; elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica; desenvolvimento de projetos; interpretação de textos técnicos e científicos relacionados aos conteúdos trabalhados. Os recursos utilizados serão: livros didáticos, livros digitais, listas de exercícios, apostilas, lousa, projetor multimídia, computador, equipamentos de laboratório, textos e artigos acadêmicos da área, reproduções de imagens e vídeos da área. A avaliação se dará em uma perspectiva formativa levando em conta todas as atividades realizadas pelos estudantes.
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). HEWITT, Paul G. Física conceitual. 12. ed. Porto Alegre: Bookman, 2015. LUZ, Antônio Máximo Ribeiro da; ALVARENGA, Beatriz Gonçalves de. Curso de física, volume 3. 6. ed. rev. ampl. São Paulo: Scipione, 2006.
Bibliografia Complementar: BARRETO FILHO, Benigno; SILVA, Cláudio Xavier da. 360º: física: aula por aula: volume único. 3. ed. São Paulo: FTD, 2015. YAMAMOTO, Kazuhito; FUKE, Luiz Felipe. Física para o ensino médio 3: eletricidade, física moderna. 3. ed. São Paulo: Saraiva, 2013. KNIGHT, Randall D. Física: uma abordagem estratégica: volume 3: eletricidade e magnetismo. 2. ed. Porto Alegre: Bookman, 2009.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Divergências identificadas em relação ao ementario_adm.tex
TABELA EMENTA 7 — Física — Ano 1 (linhas 388–434)
Semestre, CH EaD e CH Total: sem divergência (2º; 00h; 40h — igual à fonte "Semestre: 2").
Objetivo 6: LaTeX omite a cláusula final "relacionando suas características aos diferentes tipos de movimento" (fonte: "...em função do tempo, relacionando suas características aos diferentes tipos de movimento.").
Objetivo 9: LaTeX omite "empregando estratégias adequadas, argumentação científica e interpretação dos resultados obtidos" (fonte tem essa cláusula; LaTeX termina em "...problemas físicos.").
Objetivo 10: LaTeX resume "reconhecendo a presença e a aplicação dos princípios da Mecânica" para "reconhecendo os princípios da Mecânica", perdendo "a presença e a aplicação de".
Conteúdos: a fonte lista "Noções básicas de Cinemática; Cinemática ;" como dois itens distintos (aparente redundância/erro da fonte, mas está lá); o LaTeX traz apenas "noções básicas de Cinemática", sem o item avulso "Cinemática".
Metodologia: LaTeX resume/parafraseia o parágrafo da fonte e omite o procedimento "elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica" da lista de procedimentos didático-metodológicos.
Recursos: LaTeX traz uma lista de recursos abreviada ("livros didáticos e digitais, apostilas, projetor multimídia, equipamentos de laboratório"), omitindo da fonte: "listas de exercícios", "lousa", "computador", "textos e artigos acadêmicos da área" e "reproduções de imagens e vídeos da área".
Bibliografia Básica: sem divergência de conteúdo (mesmas 2 obras + FNDE).
Bibliografia Complementar — obra de KNIGHT: LaTeX omite o crédito de tradução "Tradução de Trieste Freire Ricci." presente na fonte.
TABELA EMENTA 23 — Física — Ano 2 (linhas 1109–1159)
Semestre, CH EaD e CH Total: sem divergência (3º e 4º; 00h; 80h — igual à fonte "Semestre: 3 e 4").
Objetivo 1: LaTeX omite "na interpretação e resolução de problemas físicos" ao final.
Objetivo 2: LaTeX parafraseia "aplicando o princípio da conservação da quantidade de movimento na resolução de problemas envolvendo colisões" para "...em colisões", perdendo "na resolução de problemas envolvendo".
Objetivo 3: LaTeX encurta "aos fenômenos observados no cotidiano" para "a fenômenos do cotidiano".
Objetivo 4: LaTeX omite "em situações práticas e tecnológicas" ao final.
Objetivo 5: LaTeX omite "interpretando os fenômenos térmicos por meio de modelos físicos e relações matemáticas" ao final.
Objetivo 6: LaTeX omite "reconhecendo o funcionamento, as limitações e a eficiência" (fica só "...das máquinas térmicas").
Objetivo 7: LaTeX omite "e a propagação da luz em diferentes meios" ao final.
Objetivo 8: LaTeX omite "identificando as características das ondas e" no início da cláusula e "e aplicações tecnológicas" no final; mantém apenas parte da frase da fonte.
Objetivo 9: LaTeX omite "da interpretação de gráficos, tabelas e representações matemáticas relacionadas aos fenômenos físicos estudados", terminando em "...resolução de problemas."
Objetivo 10: LaTeX omite "reconhecendo a importância da Física para a compreensão do mundo e para o desenvolvimento científico e tecnológico" ao final.
Conteúdos: sem divergência (todos os 8 itens presentes e idênticos).
Metodologia: LaTeX omite inteiramente a frase de "Recursos" (nem a versão abreviada do Ano 1 aparece) — a fonte traz a lista completa de recursos e o LaTeX não reproduz nenhuma menção a recursos nesta UC.
Metodologia: LaTeX também omite "elaboração de conclusões de experimentos e/ou assuntos trabalhados de forma teórica" da lista de procedimentos (mesmo padrão do Ano 1).
Bibliografia Básica: sem divergência (FNDE + HEWITT + LUZ vol.1 + LUZ vol.2, iguais).
Bibliografia Complementar — obra de KNIGHT: LaTeX omite "Tradução de Trieste Freire Ricci." presente na fonte.
TABELA EMENTA 36 — Física — Ano 3 (linhas 1684–1730)
Semestre — divergência de classificação: a fonte indica "Semestre: 4 e 5" para Física III, mas o LaTeX indica "5º e 6º". A carga horária (00h EaD / 80h total) está correta, mas o semestre está incorreto no ementário.
Objetivo 4: LaTeX omite "em diferentes contextos físicos e tecnológicos" ao final.
Objetivo 5: LaTeX omite a palavra "dispositivos" (fonte: "...funcionamento de dispositivos como geradores..."; LaTeX: "...funcionamento de geradores...").
Objetivo 6: LaTeX resume fortemente a frase, omitindo "reconhecendo sua propagação, classificação e aplicações nas diferentes tecnologias de comunicação, medicina, indústria e pesquisa científica" (LaTeX: apenas "...e suas aplicações tecnológicas.").
Objetivo 7: LaTeX omite "bem como suas principais aplicações tecnológicas" ao final.
Objetivo 8: LaTeX reestrutura a frase e omite "por meio da resolução de problemas, da interpretação de gráficos, tabelas, diagramas e modelos matemáticos".
Objetivo 9: LaTeX omite "e situações do cotidiano, reconhecendo sua importância para o avanço científico e tecnológico" ao final.
Conteúdos: sem divergência (todos os 6 itens presentes e idênticos).
Metodologia: LaTeX omite a cláusula "Conteúdos contextualizados e interdisciplinares, com resolução de listas de exercícios" (presente nas versões do Ano 1 e Ano 2 do próprio LaTeX, mas ausente aqui), correspondente a "sempre seguidos de resolução de listas de exercícios e problemas" da fonte.
Metodologia: LaTeX omite inteiramente a frase de "Recursos" (mesma omissão do Ano 2).
Bibliografia Básica: sem divergência (FNDE + HEWITT + LUZ vol.3, iguais).
Bibliografia Complementar: sem divergência (BARRETO FILHO + YAMAMOTO + KNIGHT, iguais — nesta UC a fonte já não traz crédito de tradução no KNIGHT, coerente com o LaTeX).
Observação geral (não contabilizada como divergência de conteúdo)
A fonte nomeia as UCs como "Física I", "Física II" e "Física III"; o LaTeX usa "Física — Ano 1/2/3". É uma convenção de nomenclatura aplicada uniformemente no documento consolidado, não uma perda de conteúdo — mas fica registrado para conferência de nomenclatura.
Não há nenhum placeholder do tipo "[pendente...]" em nenhum dos três blocos do LaTeX; todas as seções já têm conteúdo redigido, embora resumido/parafraseado em vários pontos como listado acima.
Matemática — Ano 1, 2 e 3 (TABELA EMENTA 8, 24 e 37)
Fonte: Google Drive fileId 1DxuRTi5jMvzetXTbYq8NoIb3nZUn_sbIYfWMruylZf8 (ementa-matematica-adm) Documento local: /tmp/ppc/ementario_adm_LIVE.tex (linhas 434–469, 1159–1202, 1730–1770)
Texto de origem extraído do Google Drive (na íntegra)
Cabeçalho do documento
Unidade Curricular: Matemática
Editada pelo Docente: Diego Marlon de Castro (repetido antes de cada bloco/ano)
BLOCO 1 — Matemática 1
Campo
Conteúdo
Unidade Curricular:
Matemática 1
Semestre:
1°e 2°
CH EaD*:
00 h
CH Total*:
80 h
Objetivos: ● Compreender e utilizar adequadamente a linguagem matemática na resolução de problemas, relacionado-a ao contexto da área de Administração; ● Analisar, interpretar e utilizar os conhecimentos elencados pela disciplina, na resolução de problemas relacionados à área de Administração.
Conteúdos:
Parte I - Fundamentos Potenciação: definição; propriedades da potenciação; potências com expoentes fracionários. Radiciação: definição; propriedades dos radicais; simplificação de radicais; radicais com radicandos reais; racionalização; equações com radicais; gráficos de funções com radicais e aplicação da radiciação. Conjuntos numéricos: definição de conjunto dos naturais, inteiros, racionais, irracionais e reais, suas operações e propriedades. Propriedades gerais (identidade, inversos e distributividade). Conversão entre números decimais e frações. Diferença entre dízimas periódicas e não periódicas. Equações do 1º grau: definição e resolução de equações do primeiro grau, com coeficientes e raízes reais. Equações do 2º grau: definição e resolução de equações do segundo grau, com coeficientes e raízes reais. Sistemas lineares 2x2: definição de sistemas lineares e sistemas não lineares. Método da adição e substituição.
Parte II - Matemática Ensino Médio Conjuntos: conceitos e operações (união, intersecção, diferença e complementar); problemas envolvendo conjuntos; diagrama de Venn. Funções: definição; crescimento e decrescimento; domínio, contradomínio e imagem; função aplicada num ponto. Função afim: definição; gráfico da função afim; coeficiente angular e linear; propriedades da função afim; aplicações da função afim. Função quadrática: definição; gráfico; vértice; raízes (zero da função); interceptos vertical e horizontal; concavidade e aplicações da função quadrática. Teorema de Pitágoras, razões trigonométricas e aplicações. Noções de estatística: coleta de dados, variáveis, construção de tabelas e gráficos, distribuição de frequência, médias estatísticas: aritmética e ponderada, mediana, moda e desvio padrão.
Estratégias de ensino e aprendizagem: Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal, por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem; experimentação no ensino de matemática; produção de vídeos de matemática por estudantes.
Bibliografia Básica BONJORNO, José Roberto; GIOVANNI JÚNIOR, José Ruy; GIOVANNI, José Ruy. Matemática fundamental: uma nova abordagem: ensino médio: 1° ano, 3.ed. São Paulo: FTD, 2013. 560 p. DANTE, Luiz Roberto. Projeto Múltiplo: matemática: ensino médio. 1° ano. São Paulo: Ática, 2014. 240 p. GIOVANNI, José Ruy; GIOVANNI JÚNIOR, José Ruy; BONJORNO, José Roberto; SOUZA, Paulo Roberto C. 360º matemática fundamental: uma nova abordagem: parte I, II, III, volume único, 2ª ed. São Paulo: FTD, 2015. 283 p.
Bibliografia Complementar LIMA, E. L.; CARVALHO, Paulo Cesar P. A Matemática do ensino médio: volume único, 7.ed. Rio de Janeiro, v.2: SBM, 2016. PAIVA, Manoel. Matemática: Paiva: 1º ano, 2 ed. São Paulo: Moderna, 2013. 304 p.
(Não há referência a "LIMA, Elon Lages et al. — volume 1 — 10. ed." nesta seção da fonte.)
BLOCO 2 — Matemática 2
Campo
Conteúdo
Unidade Curricular:
Matemática 2
Semestre:
3° e 4°
CH EaD*:
00 h
CH Total*:
80 h
Objetivos: ● Compreender e utilizar adequadamente a linguagem matemática na resolução de problemas, relacionado-a ao contexto da área de Administração; ● Analisar, interpretar e utilizar os conhecimentos elencados pela disciplina, na resolução de problemas relacionados à área de Administração.
Conteúdos: Equação exponencial. Função exponencial: definição; propriedades; gráfico e aplicações; e inversa (função logarítmica). Logaritmos: definição e propriedades. Equação logarítmica. Função logarítmica: definição; propriedades dos logaritmos; gráfico da função logarítmica; aplicações. Círculo trigonométrico: definição; coordenadas; ângulos; quadrantes; seno, cosseno e tangente no círculo trigonométrico; periodicidade e aplicações. Funções trigonométricas: principais funções trigonométricas (seno, cosseno, tangente, secante, cossecante e cotangente), gráficos das funções, aplicação. Identidades trigonométricas. Área e perímetro de figuras planas: triângulos, quadriláteros, hexágono regular e círculo. Geometria espacial: área das superfícies/planificação e volume de prismas, pirâmides (tronco), cilindro, cone (tronco) e esfera.
Estratégias de ensino e aprendizagem: Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal, por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem; experimentação no ensino de matemática; produção de vídeos de matemática por estudantes.
Bibliografia Básica: BONJORNO, José Roberto; GIOVANNI JÚNIOR, José Ruy; GIOVANNI, José Ruy. Matemática fundamental: uma nova abordagem: ensino médio: volume único, 3.ed. São Paulo: FTD, 2013. 560 p. DANTE, Luiz Roberto. Projeto Múltiplo: matemática: ensino médio: 2° ano. São Paulo: Ática, 2014. 240 p. GIOVANNI, José Ruy; GIOVANNI JÚNIOR, José Ruy; BONJORNO, José Roberto; SOUZA, Paulo Roberto C. 360º matemática fundamental: uma nova abordagem: parte I, II, III, volume único, 2ª ed. São Paulo: FTD, 2015. 283 p.
Bibliografia Complementar: LIMA, E. L.; CARVALHO, Paulo Cesar P. A Matemática do ensino médio: volume único, 7.ed. Rio de Janeiro, v.2: SBM, 2016. PAIVA, Manoel. Matemática: Paiva: 2º ano, 2 ed. São Paulo: Moderna, 2013. 304 p.
BLOCO 3 — Matemática 3
Campo
Conteúdo
Unidade Curricular:
Matemática 3
Semestre:
5° e 6°
CH EaD*:
00 h
CH Total*:
80 h
Objetivos: ● Compreender e utilizar adequadamente a linguagem matemática na resolução de problemas, relacionado-a ao contexto da área de Administração; ● Analisar, interpretar e utilizar os conhecimentos elencados pela disciplina, na resolução de problemas relacionados à área de Administração.
Conteúdos: Matrizes: definição; tipos de matrizes (transposta, nula, identidade, oposta); operações com matrizes; matriz inversa e aplicação de matrizes. Determinante de ordens 1, 2 e 3; solução por Sarrus; propriedade dos determinantes. Sistemas lineares: sistemas equivalentes e sistemas homogêneos, resolução de sistemas por escalonamento; sistemas com variáveis livres. Geometria analítica (distância entre pontos); estudo das retas. Análise combinatória: princípio da contagem, fatorial, arranjos, permutações e combinações. Probabilidade: espaço amostral e evento, probabilidade; união de probabilidade; probabilidade condicional. Polinômios: função polinomial, valor numérico e polinômio nulo, operações com polinômios.
Estratégias de ensino e aprendizagem: Aulas expositivas dialogadas; aulas de exercícios; avaliações qualitativas e quantitativas durante o semestre; apresentação em linguagem verbal, por escrito ou em diálogos na sala de aula; discussões em grupos; estudos dirigidos; leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado; pesquisas conduzidas em laboratório de informática; seminários; trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais; trabalhos individuais e em grupos; uso de jogos e objetos de aprendizagem; experimentação no ensino de matemática; produção de vídeos de matemática por estudantes.
Bibliografia Básica: BONJORNO, José Roberto; GIOVANNI JÚNIOR, José Ruy; GIOVANNI, José Ruy. Matemática fundamental: uma nova abordagem: ensino médio: volume único, 3.ed. São Paulo: FTD, 2013. 560 p. DANTE, Luiz Roberto. Projeto Múltiplo: matemática: ensino médio: 3º ano. São Paulo: Ática, 2014. 240 p. GIOVANNI, José Ruy; GIOVANNI JÚNIOR, José Ruy; BONJORNO, José Roberto; SOUZA, Paulo Roberto C. 360º matemática fundamental: uma nova abordagem: parte I, II, III, volume único, 2ª ed. São Paulo: FTD, 2015. 283 p.
Bibliografia Complementar: LIMA, E. L.; CARVALHO, Paulo Cesar P. A Matemática do ensino médio, 7.ed. Rio de Janeiro, v.2: SBM, 2016. PAIVA, Manoel. Matemática: Paiva: 3º ano, 2 ed. São Paulo: Moderna, 2013. 304 p.
Divergências identificadas em relação ao ementario_adm.tex
Estrutural / geral (presente nos 3 anos)
Nome da UC no cabeçalho: a fonte identifica cada bloco como "Matemática 1", "Matemática 2", "Matemática 3"; o ementário usa "Matemática — Ano 1/2/3" (nomenclatura diferente do documento-fonte).
"Objetivos": a fonte grafa "relacionado-a" (concordância incorreta); o ementário corrige para "relacionando-a" — texto alterado em relação ao original.
Estrutura "Metodologia"/"Avaliação": a fonte apresenta um único bloco corrido "Estratégias de ensino e aprendizagem" sem subdivisão explícita; o ementário separa em campos distintos "Metodologia:" e "Avaliação:", deslocando a frase "avaliações qualitativas e quantitativas durante o semestre" do meio do parágrafo para um campo próprio ao final.
Metodologia: a fonte diz "leitura e interpretação por meio do uso de datashow com projeção de textos sobre o conteúdo abordado"; o ementário resume para "leitura e interpretação por meio de datashow", perdendo a especificação "com projeção de textos sobre o conteúdo abordado".
Metodologia: a fonte diz "trabalho em laboratório de informática e na biblioteca para consulta a livros e acervos digitais"; o ementário resume para "trabalho em laboratório de informática e na biblioteca", omitindo "para consulta a livros e acervos digitais".
Metodologia: a fonte diz "pesquisas conduzidas em laboratório de informática"; o ementário altera para "pesquisas em laboratório de informática", omitindo a palavra "conduzidas".
Conteúdos — Ano 1 (Matemática 1)
"Conjuntos numéricos": a fonte inclui "Propriedades gerais (identidade, inversos e distributividade)", totalmente ausente no ementário.
"Sistemas lineares 2x2": a fonte inclui "definição de sistemas lineares e sistemas não lineares"; o ementário mantém apenas "(método da adição e substituição)", omitindo a distinção entre sistemas lineares e não lineares.
"Radiciação": a fonte cita "radicais com radicandos reais" como tópico específico; ausente no ementário.
"Conjuntos" (Parte II): a fonte detalha as operações "união, intersecção, diferença e complementar" e cita "problemas envolvendo conjuntos"; o ementário resume para "(operações, diagrama de Venn)", perdendo a especificação das operações e a menção a problemas envolvendo conjuntos.
"Funções": a fonte inclui "função aplicada num ponto"; ausente no ementário.
"Função afim": a fonte inclui "propriedades da função afim"; ausente no ementário (mantém apenas gráfico, coeficientes, aplicações).
"Função quadrática": a fonte inclui "interceptos vertical e horizontal"; ausente no ementário.
"Noções de estatística": a fonte detalha "variáveis", "distribuição de frequência" e "médias estatísticas: aritmética e ponderada, mediana, moda e desvio padrão"; o ementário resume para "medidas de tendência central e desvio padrão", perdendo as menções específicas a variáveis, distribuição de frequência e aos tipos de média/mediana/moda.
Conteúdos — Ano 2 (Matemática 2)
"Função logarítmica": a fonte lista "definição" explicitamente; o ementário lista apenas "(propriedades, gráfico, aplicações)", omitindo "definição".
"Círculo trigonométrico": a fonte lista "definição" explicitamente; ausente no ementário.
"Geometria espacial": a fonte especifica "pirâmides (tronco)" e "cone (tronco)"; o ementário lista apenas "pirâmides" e "cone", omitindo a menção a troncos de pirâmide e de cone.
Conteúdos — Ano 3 (Matemática 3)
"Matrizes": a fonte especifica os tipos "(transposta, nula, identidade, oposta)"; o ementário generaliza para "tipos", sem especificá-los.
Bibliografia Básica (presente nos 3 anos)
Referência BONJORNO/GIOVANNI JÚNIOR/GIOVANNI (Matemática fundamental): a fonte inclui "560 p."; o ementário omite a paginação.
Referência DANTE (Projeto Múltiplo): a fonte inclui "240 p."; o ementário omite a paginação.
Referência GIOVANNI (360º matemática fundamental): a fonte lista os quatro autores por extenso ("GIOVANNI, José Ruy; GIOVANNI JÚNIOR, José Ruy; BONJORNO, José Roberto; SOUZA, Paulo Roberto C.") e especifica "parte I, II, III" e "283 p."; o ementário abrevia para "GIOVANNI, José Ruy et al." e remove tanto "parte I, II, III" quanto a paginação.
Bibliografia Complementar (presente nos 3 anos)
Referência LIMA/CARVALHO (A Matemática do ensino médio): a fonte inclui "v.2" ("Rio de Janeiro, v.2: SBM"); o ementário omite "v.2".
Referência PAIVA (Matemática): a fonte inclui "304 p."; o ementário omite a paginação.
O ementário inclui, nos 3 anos, uma referência complementar adicional que NÃO consta no documento-fonte: "LIMA, Elon Lages et al. A matemática do ensino médio: volume 1. 10. ed. Rio de Janeiro: SBM, 2016. 240 p." — referência acrescentada sem correspondência na fonte.
Nenhum placeholder do tipo "[pendente...]" foi encontrado no ementário para este bloco; todo o conteúdo da fonte está representado, ainda que resumido/alterado nos pontos acima.
Química — Ano 1, 2 e 3 (TABELA EMENTA 9, 25 e 38)
Fonte: Google Drive, fileId 1SRM9qHIAhFXEvUAvgjpQKiqc76lH0FE9xIzWnxsDjkg ("ementa-quimica-adm"). Comparado com /tmp/ppc/ementario_adm_LIVE.tex — TABELA EMENTA 9 (linhas 469–519), TABELA EMENTA 25 (linhas 1202–1251), TABELA EMENTA 38 (linhas 1770–1813).
Texto de origem extraído do Google Drive (na íntegra)
Ano 1 — [Editada pelo Docente: Sabrina / Carmine]
Unidade Curricular: Química — Ano 1 | Semestre: 2º CH EaD*: 00 h | CH Total*: 40 h
Objetivos:
Estabelecer relações entre os conhecimentos sobre a matéria, sua constituição e suas transformações com situações do contexto social, tecnológico, ambiental e profissional, contribuindo para a formação integral dos estudantes.
Compreender a Química como ciência, reconhecendo sua importância para a compreensão dos fenômenos naturais, para o desenvolvimento científico e tecnológico e para os processos produtivos.
Identificar as propriedades da matéria, distinguindo substâncias puras e misturas e reconhecendo os principais métodos de separação empregados no cotidiano, na indústria e na preservação ambiental.
Compreender a evolução dos modelos atômicos, reconhecendo sua importância para a construção do conhecimento científico e para o entendimento da estrutura da matéria.
Identificar a estrutura do átomo, relacionando partículas subatômicas, distribuição eletrônica e propriedades dos elementos químicos.
Interpretar a organização da Tabela Periódica, correlacionando a posição dos elementos às suas propriedades periódicas e às suas aplicações no cotidiano.
Compreender a formação das ligações químicas, relacionando os diferentes tipos de ligação às propriedades das substâncias e aos materiais presentes no cotidiano.
Reconhecer a geometria molecular e sua influência nas propriedades das substâncias, relacionando a polaridade das moléculas ao seu comportamento físico e químico.
Identificar as forças intermoleculares, compreendendo sua influência nas propriedades macroscópicas dos materiais e em fenômenos observados na natureza e nas atividades humanas.
Conteúdos:
Química: objeto de estudo, aplicações e importância para a sociedade, o meio ambiente e os processos produtivos.
Matéria: propriedades, estados físicos, substâncias puras e misturas.
Processos de separação de misturas.
Modelos atômicos.
Estrutura atômica.
Tabela periódica.
Ligações químicas.
Geometria molecular.
Forças intermoleculares.
Estratégias de ensino e aprendizagem: O processo de ensino-aprendizagem será desenvolvido por meio de metodologias diversificadas, selecionadas conforme os objetivos de aprendizagem e as especificidades de cada conteúdo, priorizando a contextualização dos conceitos químicos em situações do cotidiano, dos processos produtivos e das questões ambientais. As estratégias didáticas buscarão promover a participação ativa dos estudantes, a construção coletiva do conhecimento e o desenvolvimento do pensamento crítico e científico. Entre os procedimentos metodológicos propostos destacam-se: aulas expositivas dialogadas, com valorização dos conhecimentos prévios dos estudantes; resolução de exercícios; estudos dirigidos; utilização de modelos didáticos e representações da estrutura da matéria; jogos didáticos; exibição e discussão de vídeos; utilização de softwares de simulação e animação; realização de atividades experimentais no Laboratório de Química, especialmente relacionadas às propriedades da matéria, separação de misturas e identificação de substâncias; bem como atividades investigativas que favoreçam a compreensão dos modelos explicativos da Química. O acompanhamento da aprendizagem ocorrerá de forma contínua e processual, contemplando instrumentos de avaliação diversificados, como relatórios de práticas laboratoriais, listas de exercícios, estudos dirigidos, seminários, participação nas atividades propostas, produções individuais e coletivas, bem como avaliações individuais escritas. O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) será empregado como Ambiente Virtual de Aprendizagem (AVA) para disponibilização de materiais de apoio, orientações, atividades complementares e acompanhamento do desempenho dos estudantes. Critérios para divisão de turma: Nas atividades práticas de laboratório, as turmas poderão ser divididas em subgrupos, respeitando as normas de segurança e a capacidade do espaço.
Bibliografia Básica: CHANG, Raymond. Química geral: conceitos essenciais. Tradução de Maria José Ferreira Rebelo. 4. ed. Porto Alegre: AMGH, 2010. 778 p., il. ISBN 9788563308047. FELTRE, Ricardo. Química 1: química geral. Colaboração de Ricardo Arissa Feltre. 7. ed. São Paulo: Moderna, 2008. v. 1. 527 p., il. ISBN 9788516061111. FRANCO, Dalton. 360º: química: cotidiano e transformações: volume único. São Paulo: FTD, 2015. 3 v., il. color. ISBN 9788596001113. PERUZZO, Francisco Miragaia; CANTO, Eduardo Leite do. Química na abordagem do cotidiano: volume único. 3. ed. São Paulo: Moderna, 2007. 760 p., il. Inclui bibliografia. ISBN 9788516056612.
Bibliografia Complementar: ATKINS, P. W.; JONES, Loretta. Princípios de química: questionando a vida moderna e o meio ambiente. Tradução de Ricardo Bicca de Alencastro. 5. ed. Porto Alegre: Bookman, 2012. 922 p., il. ISBN 9788540700383. BRADY, James E.; HUMISTON, Gerard E. Química geral. 2. ed. Rio de Janeiro: LTC, 2011. v. 1. 424 p., il., 24 cm. ISBN 9788521604488. USBERCO, João; SALVADOR, Edgard. Química: volume único. 5. ed. reform. São Paulo: Saraiva, 2002. 672 p. ISBN 8502040278.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Ano 2
Unidade Curricular: Química — Ano 2 | Semestre: 2º e 3º CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Estabelecer relações entre os conhecimentos sobre as transformações químicas e situações do contexto social, tecnológico, ambiental e profissional, contribuindo para a formação integral dos estudantes.
Identificar as principais funções inorgânicas, reconhecendo suas propriedades, nomenclatura, aplicações e ocorrência no cotidiano, nos processos produtivos e no meio ambiente.
Compreender as reações químicas como processos de transformação da matéria, representando-as por meio de equações químicas corretamente balanceadas.
Aplicar as relações estequiométricas na resolução de problemas envolvendo reagentes, produtos e rendimento das reações químicas.
Compreender os conceitos relacionados às soluções, interpretando diferentes formas de expressar concentração e reconhecendo suas aplicações em contextos científicos, industriais e cotidianos.
Analisar as transformações energéticas envolvidas nas reações químicas, compreendendo os princípios da termoquímica e sua importância para processos naturais e tecnológicos.
Compreender os fatores que influenciam a velocidade das reações químicas e o estabelecimento do equilíbrio químico, relacionando esses fenômenos a processos biológicos, ambientais e industriais.
Compreender os princípios da eletroquímica, relacionando as reações de oxirredução ao funcionamento de pilhas, baterias, processos eletrolíticos e tecnologias associadas.
Reconhecer os fundamentos da radioatividade, identificando suas aplicações, benefícios, riscos e implicações para a saúde, o meio ambiente e o desenvolvimento científico e tecnológico.
Conteúdos:
Funções Inorgânicas.
Reações químicas e balanceamento de equações.
Relações estequiométricas.
Soluções.
Termoquímica.
Cinética química.
Equilíbrio químico.
Eletroquímica.
Radioatividade.
Estratégias de ensino e aprendizagem: O processo de ensino-aprendizagem será desenvolvido por meio de metodologias diversificadas, compatíveis com os objetivos de aprendizagem e os conteúdos da unidade curricular, priorizando a contextualização dos conceitos químicos em situações do cotidiano, dos processos produtivos, da saúde e do meio ambiente. Serão utilizadas estratégias como aulas expositivas dialogadas, resolução de exercícios, estudos dirigidos, atividades investigativas, experimentação em laboratório, utilização de recursos audiovisuais e digitais, simulações computacionais, jogos didáticos, seminários e atividades individuais e em grupo. A aprendizagem será acompanhada de forma contínua e processual, por meio de instrumentos diversificados, como atividades escritas, relatórios, listas de exercícios, seminários, práticas laboratoriais, produções individuais e coletivas e avaliações individuais. O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) será utilizado como Ambiente Virtual de Aprendizagem (AVA) para disponibilização de materiais didáticos, atividades complementares, orientações e acompanhamento do desempenho dos estudantes. Critérios para divisão de turma: Nas atividades práticas de laboratório, as turmas poderão ser divididas em subgrupos, respeitando as normas de segurança e a capacidade do espaço.
Bibliografia Básica: CHANG, Raymond. Química geral: conceitos essenciais. Tradução de Maria José Ferreira Rebelo. 4. ed. Porto Alegre: AMGH, 2010. 778 p., il. ISBN 9788563308047. ATKINS, P. W.; JONES, Loretta. Princípios de química: questionando a vida moderna e o meio ambiente. Tradução de Ricardo Bicca de Alencastro. 5. ed. Porto Alegre: Bookman, 2012. 922 p., il. ISBN 9788540700383. PERUZZO, Francisco Miragaia; CANTO, Eduardo Leite do. Química na abordagem do cotidiano: volume único. 3. ed. São Paulo: Moderna, 2007. 760 p., il. Inclui bibliografia. ISBN 9788516056612.
Bibliografia Complementar: BRADY, James E.; HUMISTON, Gerard E. Química geral. Tradução de Cristina Maria Pereira dos Santos. 2. ed. Reimpr. Rio de Janeiro: LTC, 2014. v. 2. 661 p., il. ISBN 9788521604495. FELTRE, Ricardo. Química: físico-química volume 2. Colaboração de Ricardo Arissa Feltre. 7. ed. São Paulo: Moderna, 2008. 560 p., il. ISBN 9788516061135. FRANCO, Dalton. 360º: química: cotidiano e transformações: volume único. São Paulo: FTD, 2015. 3 v., il. color. ISBN 9788596001113.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Ano 3
Unidade Curricular: Química III | Semestre: 1º CH EaD*: 00 h | CH Total*: 40 h
Objetivos:
Estabelecer relações entre os conhecimentos de Química Orgânica e situações do contexto social, ambiental e profissional, contribuindo para a formação integral dos estudantes.
Identificar as propriedades do átomo de carbono que justificam a diversidade dos compostos orgânicos e sua importância para os seres vivos, os materiais e os processos industriais.
Classificar as cadeias carbônicas quanto à sua estrutura, reconhecendo suas características e correlacionando-as às propriedades dos compostos orgânicos.
Reconhecer os principais grupos funcionais da Química Orgânica, relacionando suas propriedades físicas e químicas às suas aplicações no cotidiano.
Compreender os conceitos de isomeria plana e espacial, identificando como diferenças estruturais podem influenciar as propriedades e aplicações dos compostos orgânicos.
Conhecer as principais reações orgânicas, reconhecendo sua relevância em processos naturais, industriais e tecnológicos.
Conteúdos:
O átomo de carbono e suas propriedades.
Cadeias carbônicas: definição e classificações.
Principais grupos funcionais e suas propriedades (hidrocarbonetos, álcool, enol, fenol, éter, aldeído, cetona, ácido carboxílico, éster, amina e amida).
Isomeria Plana e Espacial.
Noções de Reações Orgânicas. Temáticas transversais: meio ambiente, saúde, educação alimentar e nutricional. (no documento-fonte, "Temáticas transversais..." está no mesmo item/bullet de "Noções de Reações Orgânicas.", não é um item separado)
Estratégias de ensino e aprendizagem: O processo de ensino-aprendizagem será desenvolvido por meio de metodologias diversificadas, selecionadas conforme os objetivos de aprendizagem e as especificidades de cada conteúdo, priorizando situações reais vinculadas ao cotidiano dos estudantes. As estratégias didáticas buscarão promover a participação ativa dos estudantes, a construção coletiva do conhecimento e o desenvolvimento do pensamento crítico e científico. Entre os procedimentos metodológicos propostos destacam-se: aulas expositivas dialogadas, com valorização dos conhecimentos prévios dos estudantes, resolução de exercícios, estudos dirigidos, utilização de jogos didáticos, exibição e discussão de vídeos e filmes, realização de seminários e desenvolvimento de atividades experimentais no Laboratório de Química. Para a execução das atividades, serão utilizados recursos como quadro, projetor multimídia (data show), recursos audiovisuais, softwares de simulação e animação, jogos didáticos, materiais e equipamentos laboratoriais. O acompanhamento da aprendizagem ocorrerá de forma contínua e processual, contemplando instrumentos de avaliação diversificados, como relatórios de práticas laboratoriais, listas de exercícios, estudos dirigidos, seminários, participação nas atividades propostas, produções individuais e coletivas, bem como avaliações individuais escritas. O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) será empregado como Ambiente Virtual de Aprendizagem (AVA) para disponibilização de materiais de apoio, orientações, atividades complementares e acompanhamento do desempenho dos estudantes. Critérios para divisão de turma: Nas atividades práticas de laboratório, as turmas poderão ser divididas em subgrupos, respeitando as normas de segurança e a capacidade do espaço.
Bibliografia Básica: ATKINS, P. W.; JONES, Loretta. Princípios de química: questionando a vida moderna e o meio ambiente. Tradução de Ricardo Bicca de Alencastro. 5. ed. Porto Alegre: Bookman, 2012. 922 p., il. ISBN 9788540700383. MCMURRY, John. Química orgânica: combo. Revisão de Robson Mendes Matos. 3. ed. São Paulo, SP: Cengage Learning, 2016. 1268 p. ISBN 9788522125869. Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE).
Bibliografia Complementar: CHANG, Raymond. Química geral: conceitos essenciais. Tradução de Maria José Ferreira Rebelo. 4. ed. Porto Alegre: AMGH, 2010. 778 p., il. ISBN 9788563308047. DALMAZ, Carla; CALCAGNOTTO, Maria Elisa (revisão técnica). Bioquímica ilustrada. 7. ed. Porto Alegre: Artmed, 2019. 567 p., il., color. ISBN 9788582714850. ZUBRICK, James W. Manual de sobrevivência no laboratório de química orgânica: guia de técnicas para o aluno. Tradução de Edilson Clemente da Silva, Márcio José Estillac de Mello Cardoso. Rio de Janeiro: LTC, 2005. 262 p., il. ISBN 9788521614401.
Divergências identificadas em relação ao ementario_adm.tex
Divergências maiores (dados estruturais)
Ano 2 — Semestre incorreto (linha 1206): a fonte indica "2º e 3º"; o ementário registra "3º e 4º".
Ano 3 — Título da UC divergente (linha 1774): a fonte nomeia a UC "Química III"; o ementário usa "Química — Ano 3" (padrão de nomenclatura diferente do documento-fonte).
Ano 3 — Semestre incorreto (linha 1774): a fonte indica "1º"; o ementário registra "5º".
Objetivos — trechos resumidos/omitidos
Ano 1, objetivo 1 (linha 480): ementário omite o final ", contribuindo para a formação integral dos estudantes."
Ano 1, objetivo 4 (linha 483): ementário omite "e para o entendimento da estrutura da matéria."
Ano 1, objetivo 6 (linha 485): ementário omite "no cotidiano" (após "aplicações").
Ano 1, objetivo 7 (linha 486): ementário omite "e aos materiais presentes no cotidiano."
Ano 1, objetivo 9 (linha 488): ementário omite "e em fenômenos observados na natureza e nas atividades humanas."
Ano 2, objetivo 1 (linha 1213): ementário omite ", contribuindo para a formação integral dos estudantes."
Ano 2, objetivo 5 (linha 1217): ementário omite "e reconhecendo suas aplicações em contextos científicos, industriais e cotidianos."
Ano 2, objetivo 6 (linha 1218): ementário omite "e sua importância para processos naturais e tecnológicos."
Ano 2, objetivo 7 (linha 1219): ementário omite ", relacionando esses fenômenos a processos biológicos, ambientais e industriais."
Ano 2, objetivo 8 (linha 1220): ementário omite "e tecnologias associadas."
Ano 3, objetivo 1 (linha 1781): ementário omite ", contribuindo para a formação integral dos estudantes."
Ano 3, objetivo 3 (linha 1783): ementário omite "reconhecendo suas características e" (entre "estrutura," e "correlacionando-as").
Estratégias de Ensino e Aprendizagem / Critérios de divisão de turma
Ano 1 (linha 504): ementário omite a menção a "atividades investigativas que favoreçam a compreensão dos modelos explicativos da Química" entre as estratégias metodológicas.
Ano 1, 2 e 3 (linhas 504, 1237, 1799): em todos os três anos, o critério de divisão de turma da fonte termina com ", respeitando as normas de segurança e a capacidade do espaço" — cláusula ausente nas três tabelas do ementário.
Ano 3 (linha 1799): ementário omite "(data show)" ao citar o projetor multimídia entre os recursos.
Conteúdos — divergência estrutural (não de conteúdo)
Ano 3, Conteúdos (linhas 1795–1796): na fonte, "Noções de Reações Orgânicas." e "Temáticas transversais: meio ambiente, saúde, educação alimentar e nutricional." formam um único item; o ementário os separa em dois itens com \newline. O texto em si está preservado, mas a estrutura de tópicos diverge da fonte.
Bibliografia — detalhes divergentes
Ano 1, Bibliografia Básica — FELTRE (linha 508): fonte inclui "v. 1" após o ano (2008); ementário omite a indicação de volume.
Ano 2, Bibliografia Complementar — BRADY/HUMISTON (linha 1244): fonte indica "2. ed. Reimpr." (reimpressão); ementário registra apenas "2. ed.", omitindo "Reimpr.".
Observação geral (não listada individualmente por item)
Em todas as referências bibliográficas dos três anos, o ementário remove sistematicamente dados presentes na fonte (tradutor/revisor, número de páginas, ISBN); as obras, edições, editoras e anos citados coincidem em todos os demais casos — não configura divergência de conteúdo bibliográfico, apenas de nível de detalhe.
Não foram encontrados placeholders do tipo "[pendente...]" em nenhuma das três tabelas — todos os campos do ementário já têm conteúdo redigido.
Filosofia — Ano 1 e Ano 3 (TABELA EMENTA 10 e 39)
Texto de origem extraído do Google Drive (na íntegra)
Fonte: Google Drive, fileId 1gqcqMbVBdhkFAFezgJeXJS3LGzny-waliPP9VrdgdR8 ("ementa-filosofia-adm").
Cabeçalho do documento (texto de orientação, não faz parte da ementa em si):
Unidade Curricular: Filosofia
Esse é o conteúdo base herdado do PPC Técnico em Lazer e o novo template a ser preenchido. Para cada Unidade Curricular (UC), utilize as informações do PPC de origem e preencha diretamente o respectivo template, seguindo rigorosamente sua estrutura, formatação e todos os campos exigidos.
Observe também as orientações referentes às bibliografias básicas e complementares, bem como a matriz curricular, para identificar corretamente o semestre de oferta de cada UC. Após o preenchimento, elimine textos escritos em vermelho.
Formatação: fonte Trebuchet MS tamanho 10, espaçamento simples. Respeitar os marcadores originais e os recuos de parágrafos.
[Editada pelo Docente: João Eduardo Navachi]
BLOCO 1 — "Filosofia I" (Semestre 1 e 2)
Unidade Curricular: Filosofia I Semestre: 1 e 2 CH EaD*: 00 h CH Total*: 00 h
Objetivos:
Conhecer a origem da Filosofia, os campos de investigação da Filosofia e os períodos da história da Filosofia.
Estimular os primeiros contatos com a tradição filosófica e com a abstração conceitual típica da filosofia.
Adquirir conhecimentos sobre a estrutura do pensamento metafísico através da história da Filosofia.
Conhecer aspectos gerais da filosofia dos pré-socráticos, Sócrates e Platão.
Conhecer aspectos gerais da filosofia de Aristóteles.
Conhecer as escolas filosóficas inerentes ao período helenístico.
Relacionar os conteúdos analisados em sala de aula aos mais distintos aspectos da vida contemporânea.
Promover a troca de ideias e, por conseguinte, o respeito às distintas visões de mundo presentes na sala de aula.
Conteúdos: O que é o Mito? Passagem do Mito à Filosofia. Conceitos de Filosofia: o que é Filosofia e para que serve. Filosofia e as outras formas de conhecimento. A Razão: regras e princípios. As concepções de verdade – Dogmatismo e busca da verdade. Períodos da História da Filosofia. Filosofia Antiga. A Filosofia grega e os pré-socráticos. Os sofistas. Sócrates e a busca pela verdade. Platão e o mito da caverna. O amor a partir de Platão. As cavernas contemporâneas. Aristóteles, ética e política. O homem como animal social. As virtudes e a moderação. A prudência. A coragem. As escolas helenísticas. O estoicismo e a arte de bem viver. O epicurismo e o prazer. O ceticismo e o conhecimento. O cinismo e o cosmopolitismo.
Estratégias de ensino e aprendizagem: As aulas apresentarão o seguinte trajeto metodológico: aulas expositivas, leituras interpretativas e críticas, seminários e apresentações individuais e/ou em grupo de alunos, pesquisa bibliográfica, produção de textos. A avaliação seguirá o caminho processual com notas de 0 a 10 e considerará as seguintes questões: Participação dos alunos nas atividades propostas pelo professor; trabalho de pesquisa individual e coletiva e prova escrita. A proposta inicial é a realização de dois (2) momentos avaliativos formais durante o semestre, considerando sempre que estes momentos não contemplarão a totalidade da nota do aluno, mas serão tomados como parte do processo integral da relação ensino-aprendizagem.
Bibliografia Básica: ARANHA, M. L. A.; MARTINS, M. H. P. Filosofando: introdução à filosofia. São Paulo: Moderna, 1993. CHAUÍ, Marilena. Convite à filosofia. 13.ed. São Paulo: Ática, 2009.
Bibliografia Complementar: GAARDER, Jostein. O mundo de Sofia: romance da história da filosofia. São Paulo: Seguinte, 2012. MARCONDES, Danilo. Textos básicos de filosofia: dos pré-socráticos a Wittgenstein. Rio de Janeiro: Jorge Zahar, 2000.
(Não há mais entradas de bibliografia complementar na fonte — o bloco termina aqui.)
BLOCO 2 — "Filosofia 2" (Semestre 5 e 6)
Unidade Curricular: Filosofia 2 Semestre: 5 e 6 CH EaD*: 00 h CH Total*: 00 h
Objetivos:
Conhecer os aspectos gerais da filosofia medieval cristã.
Refletir acerca de autores e questões atinentes à filosofia moderna.
Conhecer o conceito de subjetividade a partir de Montaigne.
Compreender a centralidade da atividade política a partir de Maquiavel, Hobbes, Rousseau e Locke.
Estudar a ética do dever de Kant, bem como a centralidade do conceito de esclarecimento no período iluminista.
Conhecer aspectos gerais do irracionalismo e a crise da razão.
Refletir acerca da crise de valores morais e a problemática do niilismo.
Compreender o existencialismo e os conceitos de projeto e liberdade. Investigar a relação existente entre existencialismo e feminismo.
Visualizar o trabalho como elemento transformador na vida do homem.
Refletir acerca de questões éticas relacionadas a relação homem e meio ambiente.
Promover a troca de ideias e, por conseguinte, o respeito às distintas visões de mundo presentes na sala de aula.
Conteúdos: Filosofia Medieval Cristã. A relação entre fé e razão. A Patrística de Santo Agostinho. A Escolástica de São Tomás de Aquino. A Filosofia Moderna. A filosofia política em Maquiavel. O pensamento Ensaístico de Montaigne. Locke, Rousseau e Hobbes: a filosofia política. Filosofia moderna e Contemporânea. Kant, a ética do dever e o esclarecimento. Schopenhauer, pessimismo, vontade e irracionalismo. Nietzsche e a crise dos valores. Niilismo e a crise da razão. Existencialismo e liberdade. A condição da mulher nos séculos XX e XXI. Existencialismo, feminismo e liberdade. Política, Estado e Poder na contemporaneidade. Ética e meio ambiente. O mundo do trabalho e a alienação. Indústria Cultural e consumo.
Estratégias de ensino e aprendizagem: As aulas apresentarão o seguinte trajeto metodológico: aulas expositivas, leituras interpretativas e críticas, seminários e apresentações individuais e/ou em grupo de alunos, pesquisa bibliográfica, produção de textos. A avaliação seguirá o caminho processual com notas de 0 a 10 e considerará as seguintes questões: Participação dos alunos nas atividades propostas pelo professor; trabalho de pesquisa individual e coletiva e prova escrita. A proposta inicial é a realização de dois (2) momentos avaliativos formais durante o semestre, considerando sempre que estes momentos não contemplarão a totalidade da nota do aluno, mas serão tomados como parte do processo integral da relação ensino-aprendizagem.
Bibliografia Básica: ARANHA, M. L. A.; MARTINS, M. H. P. Filosofando: introdução à filosofia. São Paulo: Moderna, 1993. CHAUÍ, Marilena. Convite à filosofia. 13.ed. São Paulo: Ática, 2009.
Bibliografia Complementar: GAARDER, Jostein. O mundo de Sofia: romance da história da filosofia. São Paulo: Seguinte, 2012. MARCONDES, Danilo. Textos básicos de filosofia: dos pré-socráticos a Wittgenstein. Rio de Janeiro: Jorge Zahar, 2000.
(Não há mais entradas de bibliografia complementar na fonte — o bloco termina aqui. Não há seção "Observações" no documento.)
Divergências identificadas em relação ao ementario_adm.tex
CH Total divergente — Ano 1 (linha 525): a fonte traz "CH Total*: 00 h" (campo não preenchido/placeholder) para Filosofia I, enquanto o .tex apresenta "CH Total: 80 h". Não há, no documento-fonte, nenhum valor de carga horária total que sustente os "80 h" — é preciso confirmar a origem desse número (matriz curricular?) pois na ementa ele não está literalmente presente.
CH Total divergente — Ano 3 (linha 1819): mesmo problema do item 1, agora para Filosofia 2: fonte traz "CH Total*: 00 h", .tex traz "80 h".
Bibliografia Complementar com item estranho ao tema — Ano 1 (linha 575): o .tex inclui um terceiro item de bibliografia complementar ausente da fonte: "LIMA, Elon Lages et al. A matemática do ensino médio: volume 1. 10. ed. Rio de Janeiro: SBM, 2016. 240 p." Este é um livro de Matemática, sem relação com a UC de Filosofia — parece um resíduo de copy-paste de outra ementa. A fonte lista apenas GAARDER e MARCONDES.
Bibliografia Complementar com item estranho ao tema — Ano 3 (linha 1869): mesmo item espúrio de Matemática ("LIMA, Elon Lages...") incluído indevidamente na bibliografia complementar de Filosofia — Ano 3, ausente na fonte.
Metodologia/Avaliação resumida — Ano 1 (linhas 567–568): o .tex condensa e reformula o texto da fonte, e OMITE a frase final da fonte: "...considerando sempre que estes momentos não contemplarão a totalidade da nota do aluno, mas serão tomados como parte do processo integral da relação ensino-aprendizagem." O .tex também reestrutura a redação em dois campos separados ("Metodologia:"/"Avaliação:") que não existem como rótulos distintos na fonte (lá é um único parágrafo "Estratégias de ensino e aprendizagem").
Metodologia/Avaliação resumida — Ano 3 (linhas 1861–1862): mesma omissão/paráfrase do item 5, repetida no bloco de Filosofia — Ano 3.
Renomeação da UC e do campo Semestre — Ano 1 (linhas 522–523): a fonte identifica a UC como "Filosofia I" com "Semestre: 1 e 2"; o .tex renomeia para "Filosofia — Ano 1" e reformata o semestre como "1º e 2º (Filosofia I)" — adiciona ordinais e um parêntese que não constam literalmente da fonte.
Renomeação da UC e do campo Semestre — Ano 3 (linhas 1816–1817): a fonte identifica a UC como "Filosofia 2" com "Semestre: 5 e 6"; o .tex usa "Filosofia — Ano 3" e "5º e 6º (Filosofia 2)".
Objetivo parafraseado — Ano 3, item 8 (linha 1831): a fonte tem duas frases distintas: "Compreender o existencialismo e os conceitos de projeto e liberdade. Investigar a relação existente entre existencialismo e feminismo." O .tex funde em uma única frase: "Compreender o existencialismo e os conceitos de projeto e liberdade, investigando a relação entre existencialismo e feminismo."
Objetivo alterado — Ano 3, item 11 (linha 1834): a fonte traz "Promover a troca de ideias e, por conseguinte, o respeito às distintas visões de mundo presentes na sala de aula."; o .tex remove "por conseguinte": "Promover a troca de ideias e o respeito às distintas visões de mundo presentes na sala de aula." (O mesmo objetivo no Ano 1, linha 537, preserva "por conseguinte" corretamente — a omissão ocorre só no bloco do Ano 3.)
Não foram encontrados placeholders do tipo "[pendente...]" no .tex; os Conteúdos Programáticos e a Bibliografia Básica de ambos os blocos conferem integralmente com a fonte (apenas variações triviais de capitalização em "Ensaístico"/"Contemporânea" no Ano 3, sem impacto de conteúdo).
Geografia — Ano 1 e Ano 3 (TABELA EMENTA 11 e 40)
Fonte: Google Drive fileId 1cGa-p9rG55QwIbdjU26_tjIbUsPx-oUkg7ArKo4-TQ4 (ementa-geografia-adm) Comparado com: /tmp/ppc/ementario_adm_LIVE.tex, linhas 581–623 (TABELA EMENTA 11) e 1875–1916 (TABELA EMENTA 40)
ATENÇÃO — estrutura do documento-fonte: o documento-fonte contém TRÊS unidades curriculares de Geografia (Geografia I / Ano 1, Geografia II / Ano 2, Geografia III / Ano 3), enquanto o ementário local só possui DUAS entradas de Geografia na matriz curricular (linha 28: "1º Ano & Geografia -- Ano 1", linha 89: "3º Ano & Geografia -- Ano 3") e apenas duas tabelas de ementa (TABELA 11 e TABELA 40). Ver seção de divergências abaixo.
Texto de origem extraído do Google Drive (na íntegra)
Bloco 1 — Geografia I (Ano 1)
[Editada pelo Docente: JOAO QUOOS]
Unidade Curricular: Geografia I | Ano: 1 — Semestre: 1º e 2º CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Compreender a organização do espaço geográfico e as relações entre sociedade, natureza e atividades econômicas.
Interpretar mapas, gráficos, tabelas e outras representações geográficas e socioeconômicas.
Aplicar conhecimentos de cartografia e geotecnologias na análise do território.
Relacionar os aspectos naturais e ambientais à ocupação territorial, às atividades produtivas e ao desenvolvimento sustentável.
Analisar questões territoriais, ambientais e culturais, desenvolvendo uma atuação crítica e responsável na sociedade e nas organizações.
Conteúdos: Introdução ao espaço geográfico: categorias de lugar, paisagem, território e região e suas relações com a organização da sociedade e das atividades econômicas. O espaço geográfico local por meio de saída técnica, considerando as formas de ocupação, infraestrutura, atividades econômicas, comércio e serviços. A leitura e interpretação do mundo pela Cartografia. Formas de orientação, coordenadas geográficas e fusos horários e suas relações com a organização territorial e os fluxos econômicos. Representações cartográficas: projeções cartográficas, elementos do mapa, escalas e produção de mapas. A cartografia temática para compreender o espaço geográfico e apoiar a interpretação de informações territoriais e socioeconômicas: mapas, gráficos e tabelas. Geomática: Sensoriamento Remoto (fotografias aéreas, VANTs, drones e imagens de satélite) e Sistemas de Informação Geográfica aplicados à análise e ao planejamento territorial. Geodiversidade e sustentabilidade e suas relações com o desenvolvimento e as atividades econômicas. Formação e evolução da Terra: deriva continental e tectônica de placas. Solos e geomorfologia: uso e conservação no planejamento territorial e no desenvolvimento das atividades humanas e econômicas. Recursos hídricos: ciclo hidrológico, disponibilidade de água e sua relação com o uso humano e as atividades produtivas. Climatologia: fatores e elementos climáticos e suas implicações na organização do espaço, nas atividades econômicas e na sociedade. Sociedade e Natureza: interação entre fenômenos naturais, ocupação humana, produção e organização do território. Diversidade cultural e ambiental e sua importância para as comunidades, organizações e desenvolvimento local. Práticas de preservação ambiental e uso responsável dos recursos naturais no contexto do desenvolvimento sustentável e das organizações. Discussão de questões sobre história e cultura afro-brasileira, africana e indígena no contexto da formação, ocupação e organização socioeconômica do território brasileiro. Reflexão sobre os direitos humanos e sua relação com o uso dos recursos naturais, a organização do território, o trabalho e as atividades econômicas. Análise crítica de temas contemporâneos como mudanças climáticas, biodiversidade, conservação ambiental, desenvolvimento sustentável e seus impactos sobre a sociedade e as atividades econômicas.
Estratégias de ensino e aprendizagem: A unidade curricular será desenvolvida de forma integrada entre teoria e prática, por meio de aulas expositivas dialogadas, estudos de caso, atividades individuais e colaborativas, práticas de laboratório e saídas técnicas. As abordagens buscarão relacionar os conteúdos geográficos à realidade socioeconômica, ambiental e territorial, com atenção às atividades produtivas, às organizações e ao desenvolvimento local e regional. As atividades práticas, correspondentes a 20 horas, serão desenvolvidas principalmente no Laboratório de Meio Ambiente e Geomática (MAGe) e no Laboratório de Informática, envolvendo leitura e produção de mapas temáticos, interpretação de imagens de satélite e outras geotecnologias, bem como análise de gráficos, tabelas, indicadores e dados territoriais e socioeconômicos. As saídas técnicas possibilitarão a observação e análise do espaço geográfico local, relacionando aspectos ambientais, sociais e econômicos aos conteúdos estudados. Serão utilizados mapas, imagens, recursos audiovisuais, bases de dados, softwares de cartografia e geoprocessamento, pesquisas bibliográficas e estudos dirigidos. Sempre que pertinente, as atividades serão articuladas com outros componentes curriculares da formação técnica em Administração, especialmente na análise de informações territoriais, socioeconômicas, ambientais e das atividades produtivas. A avaliação será contínua e diversificada, considerando atividades teóricas e práticas, exercícios, trabalhos individuais e em grupo, produção e interpretação de mapas, gráficos e tabelas, relatórios de atividades e saídas técnicas, apresentações e avaliações escritas.
Bibliografia Básica:
LONGLEY, Paul A. Sistemas e ciência da informação geográfica. 3. ed. Porto Alegre: Bookman, 2013. 540 p.
PRESS, F.; SIEVER, R.; GROTZINGER, J.; JORDAN, T. H. Para entender a terra. 6. ed. Porto Alegre: Bookman, 2013.
Bibliografia Complementar:
CHRISTOFOLETTI, Antônio. Geomorfologia. 2. ed. São Paulo: Blucher, 1980. 188 p.
LOCH, Carlos. A interpretação de imagens aéreas: noções básicas e algumas aplicações nos campos profissionais. 5. ed. Florianópolis: Ed. da UFSC, 2008. 103 p.
MENDONÇA, Francisco; DANNI-OLIVEIRA, Inês Moresco. Climatologia: noções básicas e climas do Brasil. São Paulo: Oficina de Textos, 2007. 206 p.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Bloco 2 — Geografia II (Ano 2) — SEM CORRESPONDÊNCIA NO EMENTÁRIO LOCAL
Unidade Curricular: Geografia II | Ano: 2 — Semestre: 4º CH EaD*: 00 h | CH Total*: 40 h
Objetivos:
Compreender os impactos da globalização nas dinâmicas locais, regionais e globais e suas transformações econômicas, políticas, sociais e territoriais.
Analisar o sistema capitalista e suas transformações, considerando a revolução tecnológica, o mundo do trabalho, os blocos econômicos e os organismos multilaterais.
Analisar criticamente as desigualdades e os conflitos globais, relacionando desenvolvimento econômico, sustentabilidade, justiça social e preservação ambiental às atividades produtivas e às organizações.
Conteúdos: Mundo contemporâneo e globalização: economia, geopolítica e sociedade no contexto globalizado. Fases do capitalismo: comercial, industrial, financeiro e informacional e suas relações com as transformações das atividades econômicas e das organizações. Regionalização do espaço global: blocos econômicos (Mercosul, União Europeia, APEC, entre outros), integração econômica e comércio internacional. Organizações internacionais e relações de poder global: FMI, OMC, G20 e outros organismos multilaterais. Nova ordem mundial: desigualdades, conflitos, tensões territoriais e seus impactos econômicos e sociais. Revolução tecnológica e transformações no mundo do trabalho, na produção, na comunicação, nos transportes e nas organizações. Redes, fluxos, cadeias produtivas e circulação de mercadorias, pessoas, capitais e informações. Dinâmica da indústria e do comércio global e brasileiro: internacionalização da produção, mercados e dependência tecnológica. Fontes de energia renováveis e não renováveis: sustentabilidade, atividades produtivas e geopolítica energética. Desigualdades sociais, direitos humanos e diversidade cultural nas relações globais. História e cultura afro-brasileira, africana e indígena no contexto das desigualdades e das relações socioeconômicas. Mudanças climáticas, sustentabilidade e conservação ambiental frente às dinâmicas econômicas globais.
Estratégias de ensino e aprendizagem: A unidade curricular será desenvolvida por meio de aulas expositivas dialogadas, estudos de caso, debates, atividades individuais e colaborativas e práticas de análise geográfica, promovendo a articulação entre os conteúdos teóricos e questões contemporâneas. As abordagens buscarão relacionar globalização, geopolítica, economia, tecnologia e sustentabilidade às transformações do mundo do trabalho, das atividades produtivas e das organizações. As atividades práticas serão desenvolvidas principalmente no Laboratório de Meio Ambiente e Geomática (MAGe) e no Laboratório de Informática, utilizando mapas, dados cartográficos, gráficos, indicadores socioeconômicos, recursos audiovisuais e ferramentas digitais para análise das dinâmicas globais e de suas manifestações locais e regionais. Estudos de caso envolvendo blocos econômicos, comércio internacional, conflitos geopolíticos, cadeias produtivas, energia e mudanças climáticas contribuirão para aproximar os conteúdos da formação técnica em Administração. Poderão ser desenvolvidos trabalhos em grupo, debates, painéis temáticos, pesquisas, apresentações e atividades interdisciplinares, bem como saídas técnicas que possibilitem relacionar os processos globais às atividades econômicas e à organização do território. Questões relacionadas à diversidade cultural, aos direitos humanos, às desigualdades sociais e à preservação ambiental serão abordadas de forma integrada aos conteúdos da unidade curricular. A avaliação será contínua e diversificada, considerando atividades teóricas e práticas, estudos de caso, participação em debates, pesquisas, trabalhos individuais e em grupo, apresentações orais e avaliações escritas.
Bibliografia Básica:
SANTOS, Milton. Por uma outra globalização: do pensamento único à consciência universal. 23. ed. Rio de Janeiro: Record, 2013.
SANTOS, Milton. Técnica, espaço, tempo: globalização e meio técnico-científico-informacional. São Paulo: EdUSP, 2008.
Bibliografia Complementar:
BRIZOLA, Ana Lídia Campos; ZANELLA, Andréa V.; GESSER, Marivete (org.). Práticas sociais, políticas públicas e direitos humanos. Florianópolis: Abrapso, 2013. 271 p. Inclui bibliografia.
BOLIGIAN, Levon; BOLIGIAN, Andressa Turcatel Alves. Geografia espaço e identidade: ensino médio: volume único. São Paulo: Ed. do Brasil, 2016. 672 p.
CAREGNATO, Célia Elizabete; BOMBASSARO, Luiz Carlos (org.). Diversidade cultural: viver diferenças e enfrentar desigualdades na educação. Erechim, RS: Novello & Carbonelli, 2013.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Bloco 3 — Geografia III (Ano 3)
Unidade Curricular: Geografia III | Ano: 3 — Semestre: 5º e 6º CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Compreender os impactos da globalização nas dinâmicas locais, regionais e globais e suas transformações econômicas, políticas, sociais e territoriais.
Analisar o sistema capitalista e suas transformações, considerando a revolução tecnológica, o mundo do trabalho, os blocos econômicos e os organismos multilaterais.
Analisar criticamente as desigualdades e os conflitos globais, relacionando desenvolvimento econômico, sustentabilidade, justiça social e preservação ambiental às atividades produtivas e às organizações.
(Nota: os objetivos de Geografia III estão idênticos, literalmente, aos objetivos de Geografia II no documento-fonte — possível reaproveitamento de texto no próprio documento de origem, não é um problema do ementário local.)
Conteúdos: Brasil: população, urbanização, campo e economia — Concentraria a organização interna do território brasileiro: Dinâmica urbana e rural no Brasil: urbanização, ruralidade e suas relações econômicas e territoriais. Urbanização brasileira, redes urbanas, metropolização e organização das atividades econômicas. Demografia brasileira: crescimento populacional, estrutura etária e pirâmides etárias. População Economicamente Ativa (PEA), emprego, mercado de trabalho e desenvolvimento econômico. Movimentos migratórios internos e internacionais e suas implicações sociais, econômicas e territoriais. Estrutura fundiária brasileira: distribuição de terras, reforma agrária e conflitos fundiários. Agropecuária brasileira: modernização do campo, sistemas agrícolas, agricultura familiar e agronegócio. Tecnologia, biotecnologia e agricultura de precisão e seus impactos na produção. Relações entre campo e cidade, cadeias produtivas, circulação e abastecimento. Leitura e interpretação de indicadores demográficos, econômicos, sociais e territoriais aplicados à compreensão das desigualdades regionais brasileiras. Brasil: globalização, geopolítica, economia e sustentabilidade — Aqui ficariam os conteúdos mais diretamente relacionados à inserção do Brasil na economia global e, portanto, com uma conexão particularmente boa com Administração: Inserção do Brasil na globalização e seus reflexos econômicos, políticos, sociais e territoriais. Organização da economia brasileira e participação dos diferentes setores econômicos. Indústria, comércio e serviços no Brasil e suas transformações territoriais. Revolução tecnológica e transformações nas formas de produção, circulação, consumo e organização do trabalho. Redes de transporte, infraestrutura, logística e circulação de mercadorias no território brasileiro. Inserção do Brasil nas cadeias produtivas e nos fluxos nacionais e internacionais de mercadorias, capitais e informações. Geopolítica brasileira: papel do Brasil no cenário mundial e suas relações internacionais. Posição estratégica do Brasil na América Latina, integração regional e Mercosul. Desigualdades regionais e desenvolvimento econômico e territorial brasileiro. Questões ambientais no Brasil: desmatamento, mudanças climáticas e gestão dos recursos naturais. Políticas públicas ambientais, sustentabilidade e suas relações com as atividades econômicas e produtivas. Análise de indicadores socioeconômicos e territoriais como subsídio à compreensão de cenários regionais e nacionais.
(Nota: o texto-fonte contém anotações de rascunho do redator — "Concentraria a organização interna..." e "Aqui ficariam os conteúdos mais diretamente relacionados... com uma conexão particularmente boa com Administração" — mantidas aqui literalmente por serem parte do texto do documento-fonte.)
Estratégias de ensino e aprendizagem: A unidade curricular será desenvolvida por meio de aulas expositivas dialogadas, estudos de caso, debates, atividades práticas, resolução de problemas e saídas técnicas, promovendo a articulação dos conhecimentos geográficos com a realidade econômica, social, ambiental e territorial brasileira. As atividades práticas poderão ser desenvolvidas no Laboratório de Meio Ambiente e Geomática (MAGe) e no Laboratório de Informática, utilizando mapas, geotecnologias, bases de dados, indicadores socioeconômicos e ambientais, gráficos e informações estatísticas. Serão realizadas análises de situações relacionadas à urbanização, demografia, atividades produtivas, mercado de trabalho, agropecuária, logística, globalização, geopolítica e sustentabilidade, estabelecendo relações com a formação técnica em Administração. Por se tratar do último ano do Ensino Médio, serão desenvolvidas atividades voltadas também à preparação para o ENEM, vestibulares e outros processos seletivos, mediante interpretação de textos, mapas, gráficos e dados estatísticos, resolução e discussão de questões, revisão de conteúdos e análise de temas geográficos contemporâneos. Poderão ser utilizados estudos dirigidos, pesquisas, seminários, trabalhos individuais e colaborativos, recursos audiovisuais e atividades interdisciplinares. As questões relacionadas aos direitos humanos, diversidade cultural, desigualdades sociais e regionais e sustentabilidade serão integradas às diferentes abordagens. A avaliação será contínua e diversificada, considerando atividades teóricas e práticas, resolução de questões e problemas, estudos de caso, pesquisas, relatórios, trabalhos individuais e em grupo, apresentações e avaliações escritas.
Bibliografia Básica:
RIBEIRO, Darcy. O povo brasileiro: a formação e o sentido do Brasil. 3. ed. São Paulo: Companhia do Bolso, 2008.
SANTOS, Milton. Técnica, espaço, tempo: globalização e meio técnico-científico-informacional. São Paulo: EdUSP, 2008.
Bibliografia Complementar:
PHILIPPI JUNIOR, Arlindo; ROMERO, Marcelo de Andrade; BRUNA, Gilda Collet (Ed.). Curso de gestão ambiental. 2. ed. atual. e ampl. São Paulo: Manole, 2014.
ROSS, Jurandyr Luciano Sanches. Ecogeografia do Brasil: subsídios para planejamento ambiental. São Paulo: Oficina de Textos, 2006.
VIEIRA, Paulo Freire (Org.). Desenvolvimento territorial sustentável no Brasil: subsídios para uma política de fomento. Florianópolis: Secco, 2010.
() CH – Carga horária EaD, se houver. () CH – Carga horária total da unidade curricular em horas.
Divergências identificadas em relação ao ementario_adm.tex
UC inteira ausente do ementário: o documento-fonte define TRÊS unidades curriculares de Geografia — Geografia I (Ano 1, 4º sem... 1º e 2º sem, 80h), Geografia II (Ano 2, 4º semestre, 40h) e Geografia III (Ano 3, 5º e 6º sem, 80h). O ementario_adm_LIVE.tex só contém DUAS: "Geografia — Ano 1" (linha 28 da matriz + TABELA 11) e "Geografia — Ano 3" (linha 89 da matriz + TABELA 40). Geografia II (Ano 2, 4º semestre, CH Total 40h) não existe em nenhum lugar do arquivo — nem na matriz curricular, nem como tabela de ementa própria. Isso corresponde a 40h de carga horária de Geografia do PPC ausentes do documento consolidado.
TABELA 11 (Geografia — Ano 1) — Objetivos totalmente diferentes do texto-fonte. Os 5 objetivos do ementário (linhas 592–596: "Compreender a Geografia como ciência social...", "Analisar a formação e as transformações do espaço geográfico sob o impacto da industrialização, urbanização e produção capitalista...", etc.) não correspondem a nenhum dos 5 objetivos do texto-fonte de Geografia I (que tratam de "organização do espaço geográfico e relações entre sociedade, natureza e atividades econômicas", "interpretar mapas, gráficos e tabelas", "aplicar cartografia e geotecnologias", "relacionar aspectos naturais/ambientais à ocupação territorial e desenvolvimento sustentável", "questões territoriais/ambientais/culturais... na sociedade e nas organizações"). Nenhuma frase coincide.
TABELA 11 — Conteúdos totalmente diferentes do texto-fonte. O bloco de conteúdos do ementário (linhas 601–606) não reflete o conteúdo programático de Geografia I do documento-fonte. Faltam por completo tópicos centrais da fonte: saída técnica ao espaço geográfico local, fusos horários, geomática/sensoriamento remoto (VANTs, drones, SIG), geodiversidade, solos e geomorfologia associados a planejamento territorial, recursos hídricos/ciclo hidrológico, e a vinculação explícita de quase todo o conteúdo às "atividades econômicas e organizações" (foco do curso de Administração). Em vez disso, o ementário traz "Dinâmicas demográficas: crescimento populacional, transição demográfica, migrações internas e internacionais" — tema que no texto-fonte pertence a Geografia III (Ano 3), não a Geografia I.
TABELA 11 — Metodologia/Avaliação divergentes e incompletas. O texto-fonte especifica que as atividades práticas correspondem a 20 horas, realizadas no "Laboratório de Meio Ambiente e Geomática (MAGe)" e no Laboratório de Informática, com saídas técnicas e articulação com outros componentes da formação em Administração. Nada disso aparece no ementário (linha 609), que descreve uma metodologia genérica ("aulas expositivas dialogadas, leitura e interpretação de mapas... seminários e pesquisas conduzidas em laboratório de informática") sem menção ao laboratório MAGe, às 20h práticas ou às saídas técnicas.
TABELA 11 — Bibliografia Básica integralmente diferente. Fonte: LONGLEY (Sistemas e ciência da informação geográfica) e PRESS/SIEVER/GROTZINGER/JORDAN (Para entender a terra). Ementário (linhas 612–614): ROSS (Geografia do Brasil), VESENTINI (Geografia: o mundo em transição) e MENDONÇA/DANNI-OLIVEIRA (Climatologia). Nenhuma das duas referências-fonte aparece no ementário.
TABELA 11 — MENDONÇA/DANNI-OLIVEIRA "Climatologia" reclassificada e com paginação alterada. No texto-fonte essa obra está na Bibliografia Complementar de Geografia I, com "206 p." O ementário a coloca na Bibliografia Básica (linha 614), com "208 p." — mudança de classificação (Complementar → Básica) e divergência de paginação (206 p. → 208 p.).
TABELA 11 — Bibliografia Complementar integralmente diferente. Fonte: CHRISTOFOLETTI (Geomorfologia), LOCH (A interpretação de imagens aéreas) e MENDONÇA/DANNI-OLIVEIRA (Climatologia, já citada acima). Ementário (linhas 616–618): MOREIRA (O pensamento geográfico brasileiro), SANTOS (Por uma outra globalização) e ALMEIDA/RIGOLIN (Fronteiras da Geografia) — nenhuma coincide com a fonte de Geografia I. Note-se ainda que SANTOS, "Por uma outra globalização" pertence, no texto-fonte, à Bibliografia Básica de Geografia II (23. ed., 2013), e aparece no ementário como Complementar de Geografia I com edição diferente (18. ed., 2009).
TABELA 40 (Geografia — Ano 3) — Objetivos totalmente diferentes do texto-fonte. Os 4 objetivos do ementário (linhas 1886–1889) não correspondem aos 3 objetivos de Geografia III no texto-fonte ("compreender os impactos da globalização...", "analisar o sistema capitalista...", "analisar criticamente as desigualdades e os conflitos globais..."). Nenhuma frase coincide; o ementário também tem uma quantidade diferente de itens (4 vs. 3).
TABELA 40 — Conteúdos totalmente diferentes e sem o foco no Brasil que a fonte exige. O texto-fonte de Geografia III é fortemente centrado no Brasil ("Brasil: população, urbanização, campo e economia" e "Brasil: globalização, geopolítica, economia e sustentabilidade"), cobrindo temas como PEA/mercado de trabalho, estrutura fundiária e reforma agrária, agronegócio/agricultura familiar, geopolítica brasileira, Mercosul e desigualdades regionais brasileiras. O ementário (linhas 1894–1899) traz conteúdo genérico de geopolítica mundial ("Ordem Geopolítica Mundial: da Guerra Fria à multipolaridade...", "Espaço agrário: modelos de produção agropecuária, agronegócio..."), sem o recorte specificamente brasileiro exigido pela fonte, e sem citar PEA, estrutura fundiária, Mercosul ou geopolítica brasileira.
TABELA 40 — Metodologia/Avaliação divergentes; omite a preparação para o ENEM/vestibular. O texto-fonte destaca explicitamente que, por ser o último ano do Ensino Médio, a UC dedica atividades à preparação para o ENEM, vestibulares e outros processos seletivos, além de usar o Laboratório MAGe. O ementário (linha 1902) não menciona ENEM, vestibulares nem o laboratório MAGe; descreve metodologia genérica com "júris simulados" e "notícias contemporâneas de geopolítica", ausentes da fonte.
TABELA 40 — Bibliografia Básica integralmente diferente. Fonte: RIBEIRO (O povo brasileiro) e SANTOS (Técnica, espaço, tempo: globalização e meio técnico-científico-informacional). Ementário (linhas 1905–1907): SANTOS (A natureza do espaço: técnica e tempo, razão e estrutura — obra diferente do mesmo autor), LUCCI/BRANCO/MENDONÇA (Território e sociedade no mundo globalizado) e HAESBAERT (O mito da desterritorialização). Nenhuma referência-fonte aparece no ementário.
TABELA 40 — Bibliografia Complementar integralmente diferente. Fonte: PHILIPPI JUNIOR/ROMERO/BRUNA (Curso de gestão ambiental), ROSS (Ecogeografia do Brasil) e VIEIRA (Desenvolvimento territorial sustentável no Brasil). Ementário (linhas 1909–1911): HARVEY (O enigma do capital), MAGNOLI (História da Geopolítica) e SENE/MOREIRA (Geografia geral e do Brasil) — nenhuma coincide com a fonte de Geografia III.
Resumo: nas duas tabelas comparadas (11 e 40), a carga horária, o semestre e o rótulo "CH EaD" batem com a fonte, mas todo o conteúdo pedagógico (objetivos, conteúdos programáticos, metodologia, avaliação, bibliografia básica e complementar) foi substituído por texto diferente do documento-fonte oficial, sem correspondência literal em nenhuma das seções. Além disso, uma unidade curricular inteira do documento-fonte (Geografia II — Ano 2, 4º semestre, 40h) está completamente ausente do ementário e da matriz curricular.
Sociologia — Ano 1 e Ano 2 (TABELA EMENTA 12 e 27)
Documento-fonte (Google Drive, fileId 1ub0lx76gd5gI8pyBo76cAXrgnXkJvzGUVV1uvf5vZdQ): "ementa-sociologia-adm"
Texto de origem extraído do Google Drive (na íntegra)
Cabeçalho geral do documento (antes das tabelas)
Unidade Curricular: Sociologia
Conteúdo base herdado do PPC Técnico em Lazer (Sociologia I e II) — revisar adequação ao perfil de egresso da Administração antes de aprovar. No ADM, esta UC ocorre no Ano 1 e no Ano 2 (o Ano 3 não possui esta UC).
Para cada Unidade Curricular (UC), utilize as informações do PPC de origem e preencha diretamente o respectivo template, seguindo rigorosamente sua estrutura, formatação e todos os campos exigidos.
Observe também as orientações referentes às bibliografias básicas e complementares, bem como a matriz curricular, para identificar corretamente o semestre de oferta de cada UC. Após o preenchimento, elimine textos escritos em vermelho.
Formatação: fonte Trebuchet MS tamanho 10, espaçamento simples. Respeitar os marcadores originais e os recuos de parágrafos.
ANO 1
Subtítulo: Ano 1 Nota de autoria: [Editada pelo Docente: José Rodrigo Barth Adams]
Unidade Curricular: Sociologia — Ano 1 Semestre: 1º e 2º CH EaD*: (campo em branco — nenhum valor informado na fonte) CH Total*: 80 h
Objetivos: Analisar os diferentes discursos sobre a realidade: as explicações das Ciências Sociais amparadas nos vários paradigmas teóricos; Compreender as transformações que ocorrem nas sociedades humanas; Evidenciar a relação entre as questões individuais e as questões sociais; Formular questionamentos que permitam alcançar um conhecimento mais preciso da sociedade e uma postura crítica em relação às vivências que nos condicionam e limitam; Entender o processo de constituição, consolidação e desenvolvimento das sociedades modernas.
Conteúdos:
As Ciências Sociais e o objeto de estudo da Sociologia;
Contexto de surgimento da Sociologia;
Relação indivíduo/sociedade;
Socialização;
Instituições Sociais;
Clássicos das Ciências Sociais;
Cidadania e Direitos Humanos;
Cultura e Ideologia;
Cultura do ponto de vista antropológico;
Multiculturalismo;
Identidade e diferenças culturais;
Cultura dominante e Indústria cultural.
Subcultura/"Tribos urbanas";
Estratégias de ensino e aprendizagem: O ensino será desenvolvido através da leitura, análise, discussão e exposição de textos e imagens em sala de aula, visando o exercício do debate e da reflexão crítica sobre os temas e conceitos estudados; de aulas expositivas e dialogadas; de recursos didáticos-pedagógicos como filmes, seminários, documentários, e entrevistas; do estímulo à autonomia investigativa e socialização de temas relacionados ao programa curricular. O desenvolvimento das competências previstas para a disciplina será facilitado por meio dos seguintes recursos didáticos: textos (livros, apostilas, artigos, estudos de caso, etc.); quadro e pincel; recursos audiovisuais (filmes, séries, música, pesquisas, arte); equipamentos de informática (retroprojetor, computador, Internet etc.).
(Não há campo/rótulo separado de "Avaliação" na fonte — está integrado ao mesmo campo acima.)
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). OLIVEIRA, Pérsio Santos de. Introdução à Sociologia: Série Brasil. São Paulo: Editora Ática, 2011.
Bibliografia Complementar: COSTA, Maria Cristina. Sociologia: introdução à ciência da sociedade. 5. ed. São Paulo: Editora Moderna, 2016. OLIVEIRA, Luiz Fernandes de; COSTA, Ricardo Cesar Rocha da. Sociologia para jovens do século XXI. Rio de Janeiro: Imperial Novo Milênio, 2013. HELENA, Bomeny [et. al.]. Tempos Modernos, tempos de sociologia. 4. ed. São Paulo: Ed. do Brasil, 2016.
ANO 2
Subtítulo: Ano 2 Nota de autoria: [Editada pelo Docente: NOME] (placeholder não preenchido na fonte)
Unidade Curricular: Sociologia — Ano 2 Semestre: 3º e 4º CH EaD*: (campo em branco — nenhum valor informado na fonte) CH Total*: 80 h
Objetivos: Analisar os diferentes discursos sobre a realidade: as explicações das Ciências Sociais amparadas nos vários paradigmas teóricos; Compreender as transformações que ocorrem nas sociedades humanas; Evidenciar a relação entre as questões individuais e as questões sociais; Formular questionamentos que permitam alcançar um conhecimento mais preciso da sociedade e uma postura crítica em relação às vivências que nos condicionam e limitam; Entender o processo de constituição, consolidação e desenvolvimento das sociedades modernas.
Conteúdos:
Política e Cidadania — Etimologia, História e conceituação das palavras;
Clássicos da Política;
Estado, Governo e Nação;
Formas de organização do Estado;
Regimes de Governo;
Estratificação Social;
Classes sociais e desigualdades; Castas e Estamentos
Movimentos sociais, sindicalismo e democracia;
Novos Movimentos Sociais;
Cidadania, Direitos Humanos e Meio Ambiente.
Estratégias de ensino e aprendizagem: O ensino será desenvolvido através da leitura, análise, discussão e exposição de textos e imagens em sala de aula, visando o exercício do debate e da reflexão crítica sobre os temas e conceitos estudados; de aulas expositivas e dialogadas; de recursos didáticos-pedagógicos como filmes, seminários, documentários, e entrevistas; do estímulo à autonomia investigativa e socialização de temas relacionados ao programa curricular. O desenvolvimento das competências previstas para a disciplina será facilitado por meio dos seguintes recursos didáticos: textos (livros, apostilas, artigos, estudos de caso, etc.); quadro e pincel; recursos audiovisuais (filmes, séries, música, pesquisas, arte); equipamentos de informática (retroprojetor, computador, Internet etc.).
(Não há campo/rótulo separado de "Avaliação" na fonte — está integrado ao mesmo campo acima.)
Bibliografia Básica: Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). OLIVEIRA, Pérsio Santos de. Introdução à Sociologia: Série Brasil. São Paulo: Editora Ática, 2011.
Bibliografia Complementar: COSTA, Maria Cristina. Sociologia: introdução à ciência da sociedade. 5. ed. São Paulo: Editora Moderna, 2016. OLIVEIRA, Luiz Fernandes de; COSTA, Ricardo Cesar Rocha da. Sociologia para jovens do século XXI. Rio de Janeiro: Imperial Novo Milênio, 2013. HELENA, Bomeny [et. al.]. Tempos Modernos, tempos de sociologia. 4. ed. São Paulo: Ed. do Brasil, 2016.
Divergências identificadas em relação ao ementario_adm.tex
CH EaD fabricada (Ano 1 e Ano 2, linhas 628-629 e 1303-1304): a fonte deixa o campo "CH EaD*" em branco (nenhum valor informado); o .tex preenche "00 h" para ambas as tabelas — valor não sustentado pela fonte.
Metodologia resumida/parafraseada (Ano 1, linha 658, e Ano 2, linha 1330): o texto do .tex é uma versão condensada da fonte. Trechos omitidos: "sobre os temas e conceitos estudados" e "e socialização de temas relacionados ao programa curricular" (após "estímulo à autonomia investigativa"); o detalhamento "recursos audiovisuais (filmes, séries, música, pesquisas, arte)" foi reduzido a "recursos audiovisuais"; "equipamentos de informática (retroprojetor, computador, Internet etc.)" foi reduzido a "equipamentos de informática"; e "estudos de caso, etc." foi reduzido a "estudos de caso" (perda do "etc.").
Nota editorial de contexto ausente no .tex: a fonte traz a observação "Conteúdo base herdado do PPC Técnico em Lazer (Sociologia I e II) — revisar adequação ao perfil de egresso da Administração antes de aprovar", que não consta em nenhum lugar do ementario_adm.tex nas seções correspondentes.
Atribuição de edição docente ausente no .tex: a fonte identifica "Editada pelo Docente: José Rodrigo Barth Adams" para o Ano 1, e traz um placeholder não preenchido "[Editada pelo Docente: NOME]" para o Ano 2 (ou seja, a própria fonte está incompleta nesse ponto para o Ano 2); nenhuma dessas informações de autoria consta no .tex.
Formatação de "et al." na Bibliografia Complementar (Ano 1 e Ano 2): a fonte grafa "HELENA, Bomeny [et. al.]"; o .tex normaliza para "HELENA, Bomeny \textit{et al.}" — diferença apenas de formatação/estilo, sem alteração do conteúdo bibliográfico (referência mantida corretamente).
Demais campos (Semestre, CH Total, Objetivos, Conteúdos — incluindo ordem e todos os itens —, Bibliografia Básica e as demais referências da Bibliografia Complementar) conferem fielmente entre a fonte e o .tex, tanto para o Ano 1 quanto para o Ano 2.
Introdução à Administração (TABELA EMENTA 13)
Texto de origem extraído do Google Drive (na íntegra)
Unidade Curricular: Introdução à Administração | Semestre: 1 CH EaD*: 00 h | CH Total*: 80 h
Objetivos:
Compreender o papel da Administração nas organizações e sua evolução histórica, relacionando as principais teorias administrativas às transformações econômicas, tecnológicas e organizacionais da sociedade contemporânea;
Reconhecer o perfil profissional, as competências e os campos de atuação do Técnico em Administração;
Diferenciar os tipos de organizações quanto às suas finalidades, estruturas e formas de gestão, considerando os fatores do ambiente interno e externo que influenciam seu funcionamento;
Identificar as funções administrativas, os níveis organizacionais e a estrutura hierárquica em sua aplicação nas rotinas de trabalho;
Reconhecer tendências contemporâneas que impactam as organizações e a prática administrativa;
Compreender as etapas básicas do processo decisório na identificação de problemas em situações organizacionais.
Conteúdos:
Conceito, importância e campo de atuação da Administração;
Perfil profissional, competências e áreas de atuação do Técnico em Administração;
Organizações: conceitos, tipos, objetivos, recursos e classificação;
Ambiente organizacional: fatores internos e externos;
Estrutura organizacional, níveis hierárquicos e papéis gerenciais;
Evolução das teorias administrativas;
Funções administrativas: planejamento, organização, direção e controle;
Tendências contemporâneas em administração;
Processo decisório nas organizações: etapas básicas e sua relação com as funções administrativas.
Estratégias de ensino e aprendizagem: A unidade curricular será desenvolvida por meio de metodologias ativas de aprendizagem, articuladas a aulas expositivas dialogadas. As estratégias de ensino buscarão aproximar os estudantes da realidade das organizações e do mundo do trabalho, promovendo a análise de situações reais, a observação de diferentes contextos organizacionais e a resolução de problemas compatíveis com o nível de formação dos estudantes. Além da sala de aula, serão utilizados espaços do Câmpus como a biblioteca, sala multidisciplinar, centro multiuso e laboratório de informática. A avaliação será contínua, processual e formativa, acompanhando o desenvolvimento dos estudantes ao longo de toda a unidade curricular. Serão considerados aspectos como participação, envolvimento nas atividades propostas e atitudes em sala de aula. As atividades poderão contemplar estudos de caso, exercícios, provas, simulações, dinâmicas de grupos, jogos, seminários, participação em debates, análise de filmes, esquetes teatrais, relatórios, atividades reflexivas, autoavaliações, rodas de conversa com profissionais da área, além de visitas técnicas e outras práticas que favoreçam a articulação entre teoria e prática. Por ser uma unidade curricular basilar da formação profissional, mantém diálogo com as demais unidades da formação profissional. Além disso, os conteúdos poderão ser articulados com as unidades curriculares de Sociologia, Sociedade e Trabalho, Língua Portuguesa, História e Geografia, abordando temáticas como as transformações do mundo do trabalho, ética nas relações trabalhistas e modos de produção.
Bibliografia Básica: DIAS, Reinaldo; ZAVAGLIA, Tércia; CASSAR, Maurício. Introdução à administração: da competitividade à sustentabilidade. 3. ed. rev. Campinas, SP: Alínea, 2013. 250 p., il. Inclui bibliografia. ISBN 9788575166659. MAXIMIANO, Antonio Cesar Amaru. Introdução à administração. 8. ed. rev. e ampl. São Paulo: Atlas, 2011. xxiii, 419 p. ISBN 9788522462889.
Bibliografia Complementar: CHIAVENATO, Idalberto. Administração nos novos tempos. 2. ed. rev. e atual. Rio de Janeiro: Elsevier, 2010. 610 p. Inclui bibliografia. ISBN 9788535237719. LACOMBE, Francisco José Masset; HEILBORN, Gilberto Luiz José. Administração: princípios e tendências. 3. ed. São Paulo: Saraiva, 2015. 545 p., il. ISBN 9788502634480. NASCIMENTO, Edson Ronaldo. Gestão Pública. São Paulo: Saraiva, 2010.
Divergências identificadas em relação ao ementario_adm.tex
Metodologia — trecho final omitido: o ementário (linha 703) encerra a frase das atividades em "...rodas de conversa com profissionais da área e visitas técnicas.", omitindo o trecho da fonte "...além de visitas técnicas e outras práticas que favoreçam a articulação entre teoria e prática."
Metodologia — articulação interdisciplinar incompleta: o ementário (linha 703) termina em "...pode articular-se com Sociologia, Sociedade e Trabalho, Língua Portuguesa, História e Geografia.", omitindo a continuação da fonte: ", abordando temáticas como as transformações do mundo do trabalho, ética nas relações trabalhistas e modos de produção."
Estrutura do bloco de Estratégias de Ensino: a fonte apresenta um único parágrafo corrido "Estratégias de ensino e aprendizagem" (metodologia e avaliação entrelaçadas); o ementário reorganiza esse conteúdo em dois subitens separados, "Metodologia:" e "Avaliação:" (linhas 703–704). O conteúdo é preservado (exceto pelos itens 1 e 2 acima), mas é uma reestruturação editorial do texto-fonte.
Bibliografia Básica — DIAS, ZAVAGLIA, CASSAR: o ementário (linha 706) omite os dados físicos/ISBN presentes na fonte: "250 p., il. Inclui bibliografia. ISBN 9788575166659."
Bibliografia Básica — MAXIMIANO: o ementário (linha 707) omite os dados físicos/ISBN presentes na fonte: "xxiii, 419 p. ISBN 9788522462889."
Bibliografia Complementar — CHIAVENATO: o ementário (linha 709) omite os dados físicos/ISBN presentes na fonte: "610 p. Inclui bibliografia. ISBN 9788535237719."
Bibliografia Complementar — LACOMBE, HEILBORN: o ementário (linha 710) omite os dados físicos/ISBN presentes na fonte: "545 p., il. ISBN 9788502634480."
Não foram encontradas divergências em: título da UC, semestre (1º), carga horária (CH EaD 00h / CH Total 80h), Objetivos (todos os 6 itens presentes e fiéis), Conteúdos Programáticos (todos os 9 itens presentes e fiéis), e nas referências bibliográficas em si (autor, título, edição, local, editora, ano — todos idênticos; apenas os dados complementares de páginas/ISBN foram suprimidos, conforme itens 4–7).
Sociedade e Trabalho (TABELA EMENTA 14)
Texto de origem extraído do Google Drive (na íntegra)
Formatação: fonte Trebuchet MS tamanho 10, espaçamento simples. Respeitar os marcadores originais e os recuos de parágrafos.
[Editada pelo Docente]
Unidade Curricular: Sociedade e Trabalho
Semestre:
CH EaD*:
**CH Total*:**40 h
**Objetivos:**Compreender as transformações que ocorrem nas sociedades humanas e sua relação com o trabalho; Evidenciar a relação entre as questões individuais e as questões sociais; Formular questionamentos que permitam alcançar um conhecimento mais preciso da sociedade e do trabalho, possibilitando a construção de uma postura crítica em relação às vivências que nos condicionam e limitam; Entender o processo de constituição, consolidação e desenvolvimento das Sociedades modernas e a importância do trabalho na dinâmica de funcionamento das sociedades.
Conteúdos: O que é Trabalho; História do Trabalho; Revolução Industrial e Trabalho assalariado; Trabalho nas sociedades modernas; Formas de organização do mundo do Trabalho; 
<truncated 132238 bytes>

NOTE: The output was truncated because it was too long. Use a more targeted query or a smaller range to get the information you need.