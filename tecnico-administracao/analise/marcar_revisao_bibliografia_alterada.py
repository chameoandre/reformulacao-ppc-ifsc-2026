# -*- coding: utf-8 -*-
import re

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

authors_updated = [
    "PROENÇA, Graça.",
    "GOMBRICH, Ernst Hans.",
    "LARAIA, Roque de Barros.",
    "LATHAM-KOENIG, Christina.",
    "WHARTON, Sue.",
    "CUNHA, Celso; CINTRA, Luís Filipe Lindley.",
    "SOUSA, João da Cruz e.",
    "GONZÁLEZ HERMOSO, Alfredo. \\textbf{Conjugar es fácil}",
    "CINTRA, Maria; CUNHA, Maria Paula.",
    "FARIAS, Cláudio Vinícius Silva (org.).",
    "MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G.",
    "CORNACHIONE JÚNIOR, Edgard Bruno.",
    "DANTE, Luiz Roberto. \\textbf{Matemática}: contexto",
    "ATKINS, Peter William; JONES, Loretta.",
    "DIAS, Marco Aurélio Pereira.",
    "GIANESI, Irineu Gianesi Netto; CORRÊA, Henrique Luiz.",
    "PALADINI, Edson Pacheco.",
    "MARTINS, Petrônio Garcia; LAUGENI, Fernando Piero.",
    "HOBSBAWM, Eric John.",
    "WALSH, Catherine.",
    "PONTELO, Juliana França; CRUZ, Lucineide A. M.",
    "SARMENTO, Marlon Melo.",
    "GITMAN, Lawrence Jeffrey."
]

# We want to wrap each line or reference containing these authors in \revisao{...} if not already wrapped
for author_sig in authors_updated:
    # Find occurrences in tex
    pos = 0
    while True:
        pos = tex.find(author_sig, pos)
        if pos == -1:
            break
            
        # Check if already inside \revisao{
        # look back 20 chars
        lookback = tex[max(0, pos-20):pos]
        if r"\revisao{" in lookback:
            pos += len(author_sig)
            continue
            
        # Find start of line / newline or cell start
        # Find end of line / \newline or } \\ \hline
        # Let's inspect the boundaries
        p_prev_nl = tex.rfind(r"\newline", 0, pos)
        p_prev_cell = tex.rfind(r"}{", 0, pos)
        p_prev_pipe = tex.rfind(r"|{", 0, pos)
        
        # Start of this reference item
        starts = [p for p in [p_prev_nl + len(r"\newline"), p_prev_cell + 2, p_prev_pipe + 2] if p != -1 and p <= pos]
        start_idx = max(starts) if starts else pos
        
        # End of this reference item
        p_next_nl = tex.find(r"\newline", pos)
        p_next_cell = tex.find(r"} \\ \hline", pos)
        
        ends = [p for p in [p_next_nl, p_next_cell] if p != -1 and p >= pos]
        end_idx = min(ends) if ends else pos + len(author_sig)
        
        ref_text = tex[start_idx:end_idx].strip()
        
        if ref_text.startswith(r"\revisao{"):
            pos = end_idx
            continue
            
        new_ref_text = f"\\revisao{{{ref_text}}}"
        
        # Replace only this exact slice
        tex = tex[:start_idx] + " " + new_ref_text + " " + tex[end_idx:]
        print(f"Marcado com revisao: {author_sig}")
        pos = start_idx + len(new_ref_text) + 2

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Processamento de marcação em azul concluído!")
