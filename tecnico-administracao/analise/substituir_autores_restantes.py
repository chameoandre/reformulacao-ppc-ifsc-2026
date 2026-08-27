# -*- coding: utf-8 -*-

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

direct_replacements = [
    ("PROENÇA, G. \\textbf{História da arte}", "PROENÇA, Graça. \\textbf{História da arte}"),
    ("GOMBRICH, E. H. \\textbf{A história da arte}", "GOMBRICH, Ernst Hans. \\textbf{A história da arte}"),
    ("CINTRA, Luís F. Lindley (coautor). \\textbf{Nova gramática do português contemporâneo}", "CUNHA, Celso; CINTRA, Luís Filipe Lindley. \\textbf{Nova gramática do português contemporâneo}"),
    ("CINTRA, M.; CUNHA, M. P. \\textbf{Rotinas administrativas}", "CINTRA, Maria; CUNHA, Maria Paula. \\textbf{Rotinas administrativas}"),
    ("SOUSA, Cruz e. \\textbf{Broquéis, Faróis}", "SOUSA, João da Cruz e. \\textbf{Broquéis, Faróis}"),
    ("HERMOSO, A. G. \\textbf{Conjugar es fácil}", "GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar es fácil}"),
    ("MANZANO, André Luiz N. \\textbf{G.; MANZANO, Maria Izabel N. G. Estudo dirigido de informática básica}", "MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G. \\textbf{Estudo dirigido de informática básica}"),
    ("JR., Edgard Bruno C. \\textbf{Informática Aplicada às Áreas de Contabilidade, Administração e Economia}", "CORNACHIONE JÚNIOR, Edgard Bruno. \\textbf{Informática aplicada às áreas de contabilidade, administração e economia}"),
    ("DANTE, L. R. \\textbf{Matemática contexto e aplicações}", "DANTE, Luiz Roberto. \\textbf{Matemática}: contexto e aplicações"),
    ("GIANESI, Irineu G. \\textbf{N.; CORRÊA, Henrique Luiz. Administração estratégica de serviços}", "GIANESI, Irineu Gianesi Netto; CORRÊA, Henrique Luiz. \\textbf{Administração estratégica de serviços}"),
    ("MARTINS, Petrônio G.; LAUGENI, Fernando P. \\textbf{Administração da produção}", "MARTINS, Petrônio Garcia; LAUGENI, Fernando Piero. \\textbf{Administração da produção}"),
    ("GITMAN, Lawrence J. \\textbf{Princípios de administração financeira}", "GITMAN, Lawrence Jeffrey. \\textbf{Princípios de administração financeira}")
]

for old, new in direct_replacements:
    if old in tex:
        print(f"Substituindo: {old[:30]} -> {new[:30]}")
        tex = tex.replace(old, new)
    else:
        print(f"Não encontrado: {old}")

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Substituições diretas concluídas!")
