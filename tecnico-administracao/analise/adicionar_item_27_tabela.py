# -*- coding: utf-8 -*-

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read().strip()

new_row = """| **27** | Seção IV & V (Subitens 7, 18.1, 18.2, 19 e 22) | Correção da CH da Oficina de Integração II e Recálculo da Matriz Geral | pp. 8, 11, 102 | JACQUELINE NARCISO BASTOS | Carga horária da Oficina de Integração II constando erroneamente como 160h na tabela do 3º ano e na ementa, gerando divergência nas somas do Núcleo Politécnico, Formação Geral, Formação Técnica e Total do Curso. | Ajuste da CH da Oficina de Integração II para 80h na matriz do 3º ano e na ementa (p. 102), com recálculo dos somatórios em todo o PPC: Formação Geral (2.320h), Formação Técnica (800h), Núcleo Politécnico (160h) e Total Geral do Curso (3.280h). | **Carga horária e somatórios corrigidos.** Ajustada a CH da Oficina de Integração II para 80h (tabela do 3º ano e ementa da Tabela 45). Atualizados todos os quadros e tabelas do PPC: Dados do Curso (Item 7), Matriz Resumida (Item 18.1), Matriz Detalhada do 3º Ano (Item 18.2), Quadro Síntese Final e Certificações (Item 22), consolidando o curso em 3.280h totais (2.320h FG + 800h FT + 160h NP), tudo destacado em azul para revisão. | **Concluído** |
"""

if "| **27** |" not in text:
    text = text + "\n" + new_row

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Item 27 adicionado à tabela de correções!")
