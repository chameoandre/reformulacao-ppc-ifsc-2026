# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# Substitutions mapping
replacements = [
    # 1. Artes 1 e 2
    ("PROENÇA, G. \\textbf{História da arte.", "PROENÇA, Graça. \\textbf{História da arte}."),
    ("PROENÇA, G. \\textbf{História da arte.}", "PROENÇA, Graça. \\textbf{História da arte}."),
    ("GOMBRICH, E. H. \\textbf{A história da arte.", "GOMBRICH, Ernst Hans. \\textbf{A história da arte}."),
    ("GOMBRICH, E. H. \\textbf{A história da arte.}", "GOMBRICH, Ernst Hans. \\textbf{A história da arte}."),
    ("LARAIA, R. de B. \\textbf{Cultura: um conceito antropológico.", "LARAIA, Roque de Barros. \\textbf{Cultura}: um conceito antropológico."),
    ("LARAIA, R. de B. \\textbf{Cultura}: um conceito antropológico.", "LARAIA, Roque de Barros. \\textbf{Cultura}: um conceito antropológico."),

    # 2. Inglês 1 e 2
    ("LATHAM-KOENIG, C. \\textbf{English File: Intermediate Student's Book.", "LATHAM-KOENIG, Christina. \\textbf{English File}: Intermediate Student's Book."),
    ("LATHAM-KOENIG, C. \\textbf{English File}: Intermediate Student's Book.", "LATHAM-KOENIG, Christina. \\textbf{English File}: Intermediate Student's Book."),
    ("WHARTON, S. \\textbf{500 tips for tesol: (teaching english to speakers of other languages).", "WHARTON, Sue. \\textbf{500 tips for tesol}: (teaching english to speakers of other languages)."),
    ("WHARTON, S. \\textbf{500 tips for tesol}: (teaching english to speakers of other languages).", "WHARTON, Sue. \\textbf{500 tips for tesol}: (teaching english to speakers of other languages)."),

    # 3. LPL 1 e 2
    ("CINTRA, Luís F. Lindley (coautor). \\textbf{Nova gramática do português contemporâneo.", "CUNHA, Celso; CINTRA, Luís Filipe Lindley. \\textbf{Nova gramática do português contemporâneo}."),
    ("SOUSA, Cruz e. \\textbf{Broquéis, Faróis.", "SOUSA, João da Cruz e. \\textbf{Broquéis, Faróis}."),
    ("SOUSA, Cruz e. \\textbf{Broquéis, Faróis.}", "SOUSA, João da Cruz e. \\textbf{Broquéis, Faróis}."),

    # 4. Espanhol 1
    ("HERMOSO, A. G. \\textbf{Conjugar es fácil.", "GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar es fácil}."),
    ("HERMOSO, A. G. \\textbf{Conjugar es fácil.}", "GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar es fácil}."),

    # 5. Organização e Processos
    ("CINTRA, M.; CUNHA, M. P. \\textbf{Rotinas administrativas.", "CINTRA, Maria; CUNHA, Maria Paula. \\textbf{Rotinas administrativas}."),
    ("CINTRA, M.; CUNHA, M. P. \\textbf{Rotinas administrativas.}", "CINTRA, Maria; CUNHA, Maria Paula. \\textbf{Rotinas administrativas}."),
    ("FARIAS, Cláudio V. S. (org.). \\textbf{Técnico em administração: gestão e negócios.", "FARIAS, Cláudio Vinícius Silva (org.). \\textbf{Técnico em administração}: gestão e negócios."),
    ("FARIAS, Cláudio V. S. (org.). \\textbf{Técnico em administração}: gestão e negócios.", "FARIAS, Cláudio Vinícius Silva (org.). \\textbf{Técnico em administração}: gestão e negócios."),

    # 6. Informática Aplicada
    ("MANZANO, André Luiz N. \\textbf{G.; MANZANO, Maria Izabel N. G. Estudo dirigido de informática básica.", "MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G. \\textbf{Estudo dirigido de informática básica}."),
    ("MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G. \\textbf{Estudo dirigido de informática básica.", "MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G. \\textbf{Estudo dirigido de informática básica}."),
    ("JR., Edgard Bruno C. \\textbf{Informática Aplicada às Áreas de Contabilidade, Administração e Economia.", "CORNACHIONE JÚNIOR, Edgard Bruno. \\textbf{Informática aplicada às áreas de contabilidade, administração e economia}."),
    ("JR., Edgard Bruno C. \\textbf{Informática Aplicada às Áreas de Contabilidade, Administração e Economia.}", "CORNACHIONE JÚNIOR, Edgard Bruno. \\textbf{Informática aplicada às áreas de contabilidade, administração e economia}."),

    # 7. Matemática para Administração
    ("DANTE, L. R. \\textbf{Matemática contexto e aplicações.", "DANTE, Luiz Roberto. \\textbf{Matemática}: contexto e aplicações."),
    ("DANTE, L. R. \\textbf{Matemática contexto e aplicações.}", "DANTE, Luiz Roberto. \\textbf{Matemática}: contexto e aplicações."),

    # 8. Química 2
    ("ATKINS, P. W.; JONES, Loretta. \\textbf{Princípios de química: questionando a vida moderna e o meio ambiente.", "ATKINS, Peter William; JONES, Loretta. \\textbf{Princípios de química}: questionando a vida moderna e o meio ambiente."),
    ("ATKINS, P. W.; JONES, Loretta. \\textbf{Princípios de química}: questionando a vida moderna e o meio ambiente.", "ATKINS, Peter William; JONES, Loretta. \\textbf{Princípios de química}: questionando a vida moderna e o meio ambiente."),

    # 9. Gestão de Operações e Qualidade
    ("DIAS, Marco Aurélio P. \\textbf{Administração de materiais: uma abordagem logística.", "DIAS, Marco Aurélio Pereira. \\textbf{Administração de materiais}: uma abordagem logística."),
    ("DIAS, Marco Aurélio P. \\textbf{Administração de materiais}: uma abordagem logística.", "DIAS, Marco Aurélio Pereira. \\textbf{Administração de materiais}: uma abordagem logística."),
    ("GIANESI, Irineu G. \\textbf{N.; CORRÊA, Henrique Luiz. Administração estratégica de serviços: operações para a satisfação do cliente.", "GIANESI, Irineu Gianesi Netto; CORRÊA, Henrique Luiz. \\textbf{Administração estratégica de serviços}: operações para a satisfação do cliente."),
    ("GIANESI, Irineu G. N.; CORRÊA, Henrique Luiz. \\textbf{Administração estratégica de serviços: operações para a satisfação do cliente.", "GIANESI, Irineu Gianesi Netto; CORRÊA, Henrique Luiz. \\textbf{Administração estratégica de serviços}: operações para a satisfação do cliente."),
    ("PALADINI, Edson P. \\textbf{Gestão estratégica da qualidade: princípios, métodos e processos.", "PALADINI, Edson Pacheco. \\textbf{Gestão estratégica da qualidade}: princípios, métodos e processos."),
    ("PALADINI, Edson P. \\textbf{Gestão estratégica da qualidade}: princípios, métodos e processos.", "PALADINI, Edson Pacheco. \\textbf{Gestão estratégica da qualidade}: princípios, métodos e processos."),
    ("MARTINS, Petrônio G.; LAUGENI, Fernando P. \\textbf{Administração da produção.", "MARTINS, Petrônio Garcia; LAUGENI, Fernando Piero. \\textbf{Administração da produção}."),
    ("MARTINS, Petrônio G.; LAUGENI, Fernando P. \\textbf{Administração da produção.}", "MARTINS, Petrônio Garcia; LAUGENI, Fernando Piero. \\textbf{Administração da produção}."),

    # 10. História 3
    ("HOBSBAWM, E. J. \\textbf{Era dos extremos: o breve século XX: 1914-1991.", "HOBSBAWM, Eric John. \\textbf{Era dos extremos}: o breve século XX: 1914-1991."),
    ("HOBSBAWM, E. J. \\textbf{Era dos extremos}: o breve século XX: 1914-1991.", "HOBSBAWM, Eric John. \\textbf{Era dos extremos}: o breve século XX: 1914-1991."),
    ("WALSH, C. \\textbf{Pedagogías decoloniales: prácticas insurgentes de resistir, (re)existir y (re)vivir.", "WALSH, Catherine. \\textbf{Pedagogías decoloniales}: prácticas insurgentes de resistir, (re)existir y (re)vivir."),
    ("WALSH, C. \\textbf{Pedagogías decoloniales}: prácticas insurgentes de resistir, (re)existir y (re)vivir.", "WALSH, Catherine. \\textbf{Pedagogías decoloniales}: prácticas insurgentes de resistir, (re)existir y (re)vivir."),

    # 11. Gestão de Pessoas e Relações no Trabalho
    ("IPONTELO, Juliana F.; CRUZ, Lucineide A. M. \\textbf{Gestão de pessoas: manual de rotinas trabalhistas.", "PONTELO, Juliana França; CRUZ, Lucineide A. M. \\textbf{Gestão de pessoas}: manual de rotinas trabalhistas."),
    ("IPONTELO, Juliana F.; CRUZ, Lucineide A. M. \\textbf{Gestão de pessoas}: manual de rotinas trabalhistas.", "PONTELO, Juliana França; CRUZ, Lucineide A. M. \\textbf{Gestão de pessoas}: manual de rotinas trabalhistas."),

    # 12. Gestão Financeira
    ("SARMENTO, Melo, M. \\textbf{Gestão financeira por fluxo de caixa: a evolução das finanças para empresas.", "SARMENTO, Marlon Melo. \\textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas."),
    ("SARMENTO, Melo, M. \\textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas.", "SARMENTO, Marlon Melo. \\textbf{Gestão financeira por fluxo de caixa}: a evolução das finanças para empresas."),
    ("GITMAN, Lawrence J. \\textbf{Princípios de administração financeira.", "GITMAN, Lawrence Jeffrey. \\textbf{Princípios de administração financeira}."),
    ("GITMAN, Lawrence J. \\textbf{Princípios de administração financeira.}", "GITMAN, Lawrence Jeffrey. \\textbf{Princípios de administração financeira}.")
]

count = 0
for old, new in replacements:
    if old in tex:
        tex = tex.replace(old, new)
        count += 1

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print(f"Total de substituições aplicadas com sucesso: {count}")
