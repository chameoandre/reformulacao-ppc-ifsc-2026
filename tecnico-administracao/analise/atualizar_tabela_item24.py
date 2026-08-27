# -*- coding: utf-8 -*-

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read()

new_row = """| **24** | Seção V (Estrutura Curricular) | Ementário das UCs (Bibliografias — Nomes Completos / Sophia Web FBN) | pp. 12–104 | BIBLIOTECA / ANDRE LUIZ SILVA DE MORAES | Presença de autores com prenomes abreviados por iniciais (ex: PROENÇA, G.; GOMBRICH, E. H.; DANTE, L. R.; GITMAN, Lawrence J.) e falhas pontuais de quebra de tags nos nomes de autores. | Padronização integral de todos os prenomes de autores por extenso em 100% das referências das ementas, alinhando com os registros de autoridade do Sophia Web (Fundação Biblioteca Nacional) e NBR 6023, além do saneamento das tags nos autores Manzano, Gianesi e Sarmento. | **Padronização concluída nas ementas.** 100% dos prenomes dos autores foram expandidos para o formato por extenso completo conforme a autoridade da Biblioteca Nacional (Graça Proença, Ernst Hans Gombrich, Roque de Barros Laraia, Alfredo González Hermoso, Luiz Roberto Dante, Eric John Hobsbawm, Lawrence Jeffrey Gitman, etc.) e saneamento dos nomes de André Luiz Manzano, Irineu Gianesi Netto e Marlon Melo Sarmento. | **Concluído** |
"""

if "| **24** |" not in text:
    text = text.strip() + "\n" + new_row

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Tabela de correções atualizada com o Item 24!")
