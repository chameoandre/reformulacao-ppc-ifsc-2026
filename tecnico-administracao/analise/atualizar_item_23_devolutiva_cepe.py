# -*- coding: utf-8 -*-

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_23 = r"""| **23** | Seção V & VI (Subitens 23, 24 e 25) | Atendimento ao Discente, Aproveitamento de Conhecimentos e Avaliação | pp. 104–105 | JACQUELINE NARCISO BASTOS | Não estão no PDF os textos do PPC antigo. Está resumido de uma forma estranha (Subitens 23 e 24). | Restaurar o texto completo e detalhado do Câmpus Garopaba e do RDP para Atendimento ao Discente (Coordenadoria Pedagógica, PEDi, NAE/AEE, PAEVS), Aproveitamento de Conhecimentos e Avaliação da Aprendizagem. | Texto completo restaurado. Substituído o resumo preliminar pela redação institucional integral do Câmpus Garopaba e do RDP, detalhando a atuação da Coordenadoria Pedagógica, concessão de PEDi (Plano de Estudo Diferenciado), NAE/AEE para Educação Especial, PAEVS, os critérios regimentais de validação de saberes/aproveitamento de estudos e as diretrizes completas de avaliação formativa e recuperação paralela. | **Concluído** |"""

new_23 = r"""| **23** | Seções V & VI (Subitens 23, 24 e 25) | Atendimento ao Discente, Aproveitamento de Estudos e Avaliação (Ajuste Formulário CEPE) | pp. 104–105 | JACQUELINE NARCISO BASTOS | Não constavam no PDF os textos integrais do PPC do Câmpus Garopaba e do RDP (Subitens 23, 24 e 25) e identificação de que o subitem 25.1 não existe no formulário novo do CEPE. | Restaurar o texto completo institucional do Câmpus Garopaba e do RDP para Atendimento ao Discente, Aproveitamento de Conhecimentos e Avaliação da Aprendizagem, além de remover a subdivisão 25.1 para adequação estrita ao formulário do CEPE. | **Texto integral restaurado e formulário CEPE adequado.** Restaurada a redação institucional completa com detalhamento da Coordenadoria Pedagógica, PEDi (Art. 18 RDP / NT 01/2016), NAE/AEE, PAEVS, validação de estudos por bancas, avaliação formativa (Art. 96 RDP), devolução em 15 dias e recuperação paralela (Art. 98). A subdivisão 25.1 foi removida em conformidade com o novo formulário do CEPE, integrando a autoavaliação e a CPA diretamente ao corpo do Subitem 25. | **Concluído** |"""

if old_23 in text:
    text = text.replace(old_23, new_23)
else:
    lines = text.split('\n')
    for i, l in enumerate(lines):
        if l.startswith('| **23** |'):
            lines[i] = new_23
    text = '\n'.join(lines)

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Item 23 atualizado com a devolutiva completa do CEPE e Subitem 25!")
