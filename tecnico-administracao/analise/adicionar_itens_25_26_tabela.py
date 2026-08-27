# -*- coding: utf-8 -*-

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read().strip()

new_rows = """| **25** | Seções IV, V & IX (Subitens 10, 11, 13, 15, 17 e 29) | Destaque Visual em Azul das Seções Iniciais e Metodológicas | pp. 6–10, 106 | EQUIPE DE REVISÃO / ANDRE LUIZ SILVA DE MORAES | Textos conceituais da reformulação (justificativa socioeconômica regional, objetivos formativos da Res. 142/2025, perfil CNCT 4ª ed., 9 características socioemocionais do egresso e metodologia de ciclos temáticos/omnilateralidade) não estavam marcados em azul para visualização dos revisores. | Aplicação da macro \\revisao{...} em todos os parágrafos, listas de competências e fundamentações conceituais introduzidas na reformulação de 2026. | **Destaque em azul concluído.** Todos os blocos textuais, dados socioeconômicos regionais (IBGE), competências do egresso, fundamentação na Pedagogia Histórico-Crítica (Saviani) e Ciclos Temáticos (Silva, 2016) foram marcados em azul no PDF para facilitar a conferência pelos pares. | **Concluído** |
| **26** | BASE DE CONHECIMENTO GERAL | Documentação e Consolidação das Diretrizes dos PPCs | -- | COMISSÃO DO PPC / ANDRE LUIZ SILVA DE MORAES | Necessidade de centralizar e padronizar as regras de formatação, manipulação de texto, arquitetura da macro de revisão e diretrizes bibliográficas para reaproveitamento nos demais PPCs do Câmpus (ex.: Técnico em Informática). | Criação de documento específico para o mecanismo de revisão e atualização das diretrizes bibliográficas (Sophia Web/FBN) e da estrutura canônica de 30 subitens da Res. CONSUP 142/2025. | **Base de conhecimento atualizada e consolidada.** Criado o guia mecanismo-revisao-destaque-azul.md e atualizadas as diretrizes ABNT/FBN e o padrão oficial de seções, assegurando que toda a engenharia pedagógica e tipográfica esteja pronta para ser replicada em outros PPCs. | **Concluído** |
"""

if "| **25** |" not in text:
    text = text + "\n" + new_rows

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Itens 25 e 26 adicionados à tabela de correções!")
