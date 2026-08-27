# -*- coding: utf-8 -*-

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_27 = r"""| **27** | Seção IV & V (Subitens 7, 18.1, 18.2, 19 e 22) | Correção da CH da Oficina de Integração II e Recálculo da Matriz Geral | pp. 8, 11, 102 | JACQUELINE NARCISO BASTOS | Carga horária da Oficina de Integração II constando erroneamente como 160h na tabela do 3º ano e na ementa, gerando divergência nas somas do Núcleo Politécnico, Formação Geral, Formação Técnica e Total do Curso. | Ajuste da CH da Oficina de Integração II para 80h na matriz do 3º ano e na ementa (p. 102), com recálculo dos somatórios em todo o PPC: Formação Geral (2.320h), Formação Técnica (800h), Núcleo Politécnico (160h) e Total Geral do Curso (3.280h). | **Carga horária e somatórios corrigidos.** Ajustada a CH da Oficina de Integração II para 80h (tabela do 3º ano e ementa da Tabela 45). Atualizados todos os quadros e tabelas do PPC: Dados do Curso (Item 7), Matriz Resumida (Item 18.1), Matriz Detalhada do 3º Ano (Item 18.2), Quadro Síntese Final e Certificações (Item 22), consolidando o curso em 3.280h totais (2.320h FG + 800h FT + 160h NP), tudo destacado em azul para revisão. | **Concluído** |"""

new_27 = r"""| **27** | Seção IV & V (Subitens 7, 18.1, 18.2, 19 e 22) | Correção da CH da Oficina de Integração II e Recálculo da Matriz Geral Conforme Planilha Oficial | pp. 8, 11, 102 | JACQUELINE NARCISO BASTOS / COMISSÃO | Carga horária da Oficina de Integração II constando erroneamente como 160h na tabela do 3º ano e na ementa, gerando divergência nas somas do Núcleo Politécnico e do Total Geral do Curso. | Ajuste da CH da Oficina de Integração II para 80h na matriz do 3º ano e na ementa (p. 102), com harmonização integral de todos os somatórios com a planilha oficial de aulas/semestres da matriz: Formação Geral (2.280h / 74,03%), Formação Técnica (640h / 20,78%), Núcleo Politécnico (160h / 5,19%) e Total Geral do Curso (3.080h / 100,0%). | **Carga horária e somatórios 100% harmonizados com a planilha oficial.** Ajustada a CH da Oficina de Integração II para 80h (tabela do 3º ano e ementa da Tabela 45). Atualizados todos os quadros do PPC: Dados do Curso (Item 7), Matriz Resumida (Item 18.1), Matriz Detalhada do 3º Ano (Item 18.2 com subtotal de 880h), Quadro Síntese Final e Certificações (Item 22), consolidando o curso com 3.080h totais (1.120h 1º ano + 1.120h 2º ano + 880h 3º ano), com todas as alterações destacadas em azul para conferência pelos pares. | **Concluído** |"""

if old_27 in text:
    text = text.replace(old_27, new_27)
else:
    # try line replace
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('| **27** |'):
            lines[i] = new_27
    text = '\n'.join(lines)

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Item 27 na tabela atualizado com a precisão de 3.080h!")
