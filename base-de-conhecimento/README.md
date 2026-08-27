# Base de Conhecimento — Reformulação dos PPCs (IFSC Câmpus Garopaba)

Este diretório centraliza o conhecimento técnico, diretrizes institucionais, padrões normativos da ABNT, regras de formatação tipográfica e procedimentos operacionais adotados na elaboração, revisão e compilação dos Projetos Pedagógicos de Curso (PPCs) dos Cursos Técnicos Integrados ao Ensino Médio:
- **Técnico em Administração Integrado**
- **Técnico em Informática Integrado**

---

## 📚 Estrutura da Base de Conhecimento

1. [diretrizes-abnt-bibliografia.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/diretrizes-abnt-bibliografia.md)
   - Regras oficiais da Biblioteca, SIBI/IFSC e ABNT NBR 6023 para bibliografias básica e complementar.
   - Padrão de nomes de autores por extenso alinhados à autoridade da **Fundação Biblioteca Nacional (Sophia Web / FBN)**.
   - Padrão de destaque tipográfico (negrito restrito ao título principal, subtítulo normal após dois pontos `:`).
   - Regras para *et al.* em itálico, entradas por título e integridade de tags de autoria.

2. [mecanismo-revisao-destaque-azul.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/mecanismo-revisao-destaque-azul.md)
   - Arquitetura da macro `\revisao{...}` e controle condicional `\ifhighlightchanges`.
   - Modos de operação: **Modo Revisão Ativo** (destaques em azul) e **Modo Final Limpo** (publicação institucional sem alterações de código).
   - Boas práticas para aplicação em parágrafos, listas `itemize`, células de `xltabular` e referências.

3. [padrao-visual-tabelas-ementas.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/padrao-visual-tabelas-ementas.md)
   - Especificação do ambiente visual `xltabular` em LaTeX.
   - Identidade visual do IFSC (`ifscgreen`, `cinzaTabela`).
   - Dimensionamento de colunas, larguras de `\dimexpr`, quebras de página e estrutura de campos de cada UC.

4. [padrao-estrutura-secoes-modelo-oficial.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/padrao-estrutura-secoes-modelo-oficial.md)
   - Hierarquia oficial das 10 Seções Macro (I a X) e dos 30 Subitens Contínuos (1 a 30) do formulário de PPC do IFSC.
   - Diretrizes conceituais obrigatórias da **Resolução CONSUP 142/2025** (justificativa regional, omnilateralidade, Ciclos Temáticos, EaD até 10%, PEDi, NAE/AEE, avaliação formativa e recuperação paralela).

5. [procedimentos-compilacao-deploy.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/procedimentos-compilacao-deploy.md)
   - Procedimento de compilação não interativa via `tectonic`.
   - Sincronização 1:1 entre os arquivos Markdown (`todas_ementas_*.md`) e LaTeX (`ementario_*.tex`).
   - Higiene de repositório, commits e deploy automatizado no GitHub Pages.

6. [tabela_de_correcoes_ppc.md](file:///Users/chameoandre/Google-Drive-chameoandre/INSTITUTO-FEDERAL-SANTA-CATARINA/CURSOS/TECNICO/informatica-integrado/reformulacao-ppc-informatica-administracao-integrado/base-de-conhecimento/tabela_de_correcoes_ppc.md)
   - Registro e histórico de todas as 24 revisões, auditorias e apontamentos da equipe, biblioteca e pareceres da DEPE com a coluna oficial de **Devolutiva da Correção**.
