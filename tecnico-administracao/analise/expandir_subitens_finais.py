# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# Target block from Subitem 21 to Subitem 25
old_block_pattern = r"\\subsection\{Atividade em EaD:\}.*?\\subsubsection\{Autoavaliação do Curso e Atuação da CPA:\}"

new_block = r"""\subsection{Atividade em EaD:}
Conforme estabelecido no item 7.6.2 deste PPC, o Curso Técnico em Administração Integrado ao Ensino Médio do IFSC Câmpus Garopaba é estruturado com matriz curricular presencial (0 horas a distância / 0\% de carga horária fixa em EaD). \revisao{Todavia, em consonância com o Regulamento Didático-Pedagógico (RDP) do IFSC, faculta-se aos docentes o desenvolvimento de até 10\% da carga horária das unidades curriculares por meio de atividades não presenciais mediadas por tecnologias digitais de informação e comunicação (utilizando o Ambiente Virtual de Aprendizagem Moodle), visando ao suporte pedagógico, estudos orientados e ampliação dos recursos didáticos.}

\subsection{Certificações intermediárias:}
Não há previsão de certificação profissional intermediária ao longo do curso. A diplomação técnica integral ocorre mediante a conclusão com aprovação de todas as Unidades Curriculares e cumprimento da carga horária mínima de 3.200 horas-relógio.

\subsection{Atendimento e acompanhamento ao discente:}
\revisao{No intuito de contribuir de forma decisiva com as políticas de permanência e êxito escolar, o Câmpus Garopaba oferece acompanhamento sistemático e especializado aos discentes por meio de sua equipe multiprofissional da Coordenadoria Pedagógica, composta por psicólogo, pedagoga, assistente social, assistentes de alunos e técnicos em assuntos educacionais.}

\revisao{Para atender às especificidades de aprendizagem e ritmos formativos individuais, conforme o Art. 18 do Regulamento Didático-Pedagógico (RDP) do IFSC e a Nota Técnica CEPE/IFSC nº 01/2016, poderão ser ofertados Planos de Estudo Diferenciado (PEDi), elaborados conjuntamente pela Coordenação de Curso e Coordenadoria Pedagógica, permitindo a adequação da matriz e estratégias individualizadas de atendimento, nivelamento e apoio ao ensino.}

\revisao{Como suporte à permanência estudantil e ao desenvolvimento integral, os discentes têm acesso a programas de assistência estudantil (Programa de Atendimento ao Estudante em Vulnerabilidade Social -- PAEVS/PAE), bem como a oportunidades de participação em projetos de monitoria, pesquisa e extensão.}

\revisao{O Câmpus conta ainda, em caráter permanente, com o Núcleo de Acessibilidade Educacional (NAE / NAPNE), que identifica, acolhe e acompanha estudantes com deficiência, transtornos globais do desenvolvimento e altas habilidades/superdotação, promovendo ações de acessibilidade metodológica, instrumental e comunicacional, e viabilizando o Atendimento Educacional Especializado (AEE) e tecnologias assistivas para assegurar a plena inclusão escolar.}

\subsection{Critérios de aproveitamento de conhecimentos e experiências anteriores:}
\revisao{O aproveitamento de estudos e a validação de saberes e competências profissionais anteriormente adquiridos no ensino formal, no mundo do trabalho ou em processos informais de qualificação serão processados em estrita observância ao Regulamento Didático-Pedagógico (RDP) do IFSC e às normativas institucionais vigentes.}

\revisao{O processo de validação de conhecimentos ocorrerá mediante requerimento formal do estudante junto à Secretaria Escolar / Registro Acadêmico, acompanhado da documentação comprobatória cabível (histórico escolar, ementas, certificados ou declarações de atuação profissional), sendo submetido à avaliação teórica e/ou prática conduzida por banca examinadora constituída por docentes da área do conhecimento correspondente.}

% =========================================================
\section{AVALIAÇÃO}
\subsection{Avaliação do processo de ensino e aprendizagem:}
\revisao{A avaliação da aprendizagem possui caráter eminentemente diagnóstico, processual e formativo, orientando-se pelos princípios do Projeto Pedagógico Institucional (PPI) e pelas diretrizes do Regulamento Didático-Pedagógico (RDP) do IFSC. A avaliação constitui um instrumento de diagnóstico, orientação e reorientação contínua da prática pedagógica, visando à construção significativa dos conhecimentos e ao acompanhamento do desenvolvimento do perfil profissional do egresso.}

\revisao{Em consonância com o Art. 96 do RDP, cada docente realizará, no mínimo, duas avaliações formais por semestre em cada unidade curricular, fornecendo devolutivas aos estudantes com análise de avanços e dificuldades no prazo máximo regimental de 15 (quinze) dias letivos após a aplicação. Os instrumentos avaliativos são diversificados, incluindo observação sistemática, projetos integradores, relatórios técnicos, estudos dirigidos, atividades práticas, autoavaliações e avaliações escritas.}

\revisao{Em atendimento ao Art. 98 do RDP, é assegurado a todos os estudantes o direito à recuperação paralela de estudos ao longo do período letivo, desenvolvida preferencialmente no horário regular de aulas ou em horários de atendimento pedagógico, prevalecendo a maior nota obtida. É garantido também o direito à realização de atividades avaliativas em segunda chamada (Art. 97) por motivo justificado e à solicitação de revisão de avaliação (Art. 99).}

\subsubsection{Autoavaliação do Curso e Atuação da CPA:}"""

tex = re.sub(old_block_pattern, lambda m: new_block, tex, flags=re.DOTALL)

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("main_ppc_administracao.tex atualizado com as seções institucionais completas!")
