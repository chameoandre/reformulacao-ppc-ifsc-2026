# -*- coding: utf-8 -*-

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

old_sec_vi = r"""% =========================================================
\section{AVALIAÇÃO}
\subsection{Avaliação do processo de ensino e aprendizagem:}
\revisao{A avaliação da aprendizagem possui caráter eminentemente diagnóstico, processual e formativo, orientando-se pelos princípios do Projeto Pedagógico Institucional (PPI) e pelas diretrizes do Regulamento Didático-Pedagógico (RDP) do IFSC. A avaliação constitui um instrumento de diagnóstico, orientação e reorientação contínua da prática pedagógica, visando à construção significativa dos conhecimentos e ao acompanhamento do desenvolvimento do perfil profissional do egresso.}

\revisao{Em consonância com o Art. 96 do RDP, cada docente realizará, no mínimo, duas avaliações formais por semestre em cada unidade curricular, fornecendo devolutivas aos estudantes com análise de avanços e dificuldades no prazo máximo regimental de 15 (quinze) dias letivos após a aplicação. Os instrumentos avaliativos são diversificados, incluindo observação sistemática, projetos integradores, relatórios técnicos, estudos dirigidos, atividades práticas, autoavaliações e avaliações escritas.}

\revisao{Em atendimento ao Art. 98 do RDP, é assegurado a todos os estudantes o direito à recuperação paralela de estudos ao longo do período letivo, desenvolvida preferencialmente no horário regular de aulas ou em horários de atendimento pedagógico, prevalecendo a maior nota obtida. É garantido também o direito à realização de atividades avaliativas em segunda chamada (Art. 97) por motivo justificado e à solicitação de revisão de avaliação (Art. 99).}

\subsubsection{Autoavaliação do Curso e Atuação da CPA:}
A avaliação do curso é realizada periodicamente em articulação com a Comissão Própria de Avaliação (CPA) do IFSC, comitês pedagógicos e reuniões do Colegiado do Curso, promovendo a melhoria contínua da infraestrutura, matriz curricular e metodologias de ensino."""

new_sec_vi = r"""% =========================================================
\section{AVALIAÇÃO}
\subsection{Avaliação do processo de ensino e aprendizagem:}
\revisao{A avaliação da aprendizagem possui caráter eminentemente diagnóstico, processual e formativo, orientando-se pelos princípios do Projeto Pedagógico Institucional (PPI) e pelas diretrizes do Regulamento Didático-Pedagógico (RDP) do IFSC. A avaliação constitui um instrumento de diagnóstico, orientação e reorientação contínua da prática pedagógica, visando à construção significativa dos conhecimentos e ao acompanhamento do desenvolvimento do perfil profissional do egresso.}

\revisao{Em consonância com o Art. 96 do RDP, cada docente realizará, no mínimo, duas avaliações formais por semestre em cada unidade curricular, fornecendo devolutivas aos estudantes com análise de avanços e dificuldades no prazo máximo regimental de 15 (quinze) dias letivos após a aplicação. Os instrumentos avaliativos são diversificados, incluindo observação sistemática, projetos integradores, relatórios técnicos, estudos dirigidos, atividades práticas, autoavaliações e avaliações escritas.}

\revisao{Em atendimento ao Art. 98 do RDP, é assegurado a todos os estudantes o direito à recuperação paralela de estudos ao longo do período letivo, desenvolvida preferencialmente no horário regular de aulas ou em horários de atendimento pedagógico, prevalecendo a maior nota obtida. É garantido também o direito à realização de atividades avaliativas em segunda chamada (Art. 97) por motivo justificado e à solicitação de revisão de avaliação (Art. 99).}

\revisao{A avaliação institucional e autoavaliação contínua do curso serão realizadas em articulação permanente com a Comissão Própria de Avaliação (CPA) do IFSC, comitês pedagógicos e reuniões periódicas do Colegiado do Curso e Conselhos de Classe, promovendo a identificação de potencialidades, o aprimoramento da infraestrutura, a atualização da matriz curricular e o aperfeiçoamento constante das metodologias de ensino.}"""

tex = tex.replace(old_sec_vi, new_sec_vi)

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Subitem 25 ajustado para conformidade com o formulário novo do CEPE (sem 25.1) e texto completo integrado!")
