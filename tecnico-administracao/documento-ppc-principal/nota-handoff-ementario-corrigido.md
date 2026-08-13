# Nota de handoff — Ementário Administração (ementario_adm.tex) — versão corrigida

**Data:** 12/08/2026
**Para:** André (Coordenação PPC, Técnico em Administração Integrado — IFSC Câmpus Garopaba)

## 1. Problema no arquivo original (`ementario_adm.tex`, fileId `19-2ClpYCRHVVMsPBrbPtw8i82QRtJ5W0`)

Ao auditar o arquivo gerado pela ferramenta "Antigravity" contra a fonte de verdade (`todas_ementas_administracao.md`, 46 blocos de Unidade Curricular), foram encontrados os seguintes problemas remanescentes no arquivo vivo no Drive:

- **Bug de padding em Bibliografia Complementar:** em blocos onde a UC tem menos de 3 títulos reais na Bibliografia Complementar, o template original inseria um "3º título ... pendente" como item fantasma após o conteúdo real (em vez de listar apenas os títulos que de fato existem na fonte). Isso é um artefato de geração automática, não um dado real.
- **Matemática para Administração** aparecia posicionada na tabela do 1º Ano da "Matriz Curricular Detalhada", quando na verdade — conforme a fonte (`Ano/Semestre: Ano 2, 3º semestre`) e o Bloco de Formação (Formação Específica, não Formação Geral) — deveria estar no 2º Ano.
- **Erro aritmético nos subtotais:** o subtotal de Formação Geral do 1º Ano estava declarado como 840h, quando a soma real dos componentes é 880h. Esse erro se propagava para a tabela de síntese (total geral 3.160h em vez de 3.200h).
- Demais pontos citados originalmente (bibliografia sistematicamente truncada, Espanhol com apenas 1 bloco, blocos fabricados de Geografia/História) **já estavam corrigidos** na versão mais recente do arquivo no Drive (modificado em 12/08/2026 14:58) — ou seja, o diagnóstico antigo (`divergencias-ementario-tex-vs-fonte-real.md`) estava desatualizado em relação ao estado atual do arquivo.

## 2. O que foi corrigido

Foi produzido um arquivo `.tex` completo e corrigido, com os 46 blocos de Unidade Curricular (`% TABELA EMENTA 1` a `46`) na mesma estrutura/template do arquivo original (cores `ifscgreen`/`cinzaTabela`, ambiente `xltabular`, mesmos marcadores de comentário), mas com:

- Conteúdo (Objetivos, Conteúdos, Estratégias de Ensino e Aprendizagem, Bibliografia Básica, Bibliografia Complementar) transcrito **literalmente** da fonte `todas_ementas_administracao.md`, sem resumir, sem inventar e sem truncar bibliografias — todos os títulos reais de cada UC estão listados.
- Para as UCs marcadas como **[PENDENTE — aguardando preenchimento pelo docente responsável]** na fonte (Educação Física Ano1/Ano2, Inglês Ano1/Ano2, Língua Portuguesa e Literatura Ano1/2/3, Geografia Ano1/Ano3, Oficina de Integração I — Ano 2, Gestão de Marketing I, Gestão de Marketing II, Empreendedorismo I, Gestão Financeira): usados placeholders explícitos em itálico indicando pendência docente — **nenhum conteúdo foi inventado**.
- **Espanhol** corrigido para 2 blocos distintos (Ano 1 e Ano 2), cada um com seu próprio conteúdo e bibliografia da fonte.
- **Geografia** presente apenas para Ano 1 e Ano 3 (não há bloco de Ano 2 na fonte).
- **História** presente apenas para Ano 2 e Ano 3 (não há bloco de Ano 1 na fonte).
- Total final: **46 blocos**, batendo exatamente com os 46 blocos `# Unidade Curricular:` da fonte.

### Correções de Carga Horária (CH) na Matriz Curricular Detalhada

Usando a fonte `.md` como verdade (não os valores sugeridos na solicitação original, que foram conferidos e não todos batiam):

| UC | CH confirmada na fonte | Observação |
|---|---|---|
| Química — Ano 1 | 40h | já estava correta no arquivo original |
| Informática Aplicada | 40h | já estava correta |
| Matemática para Administração | 40h | **corrigida a posição**: movida da tabela do 1º Ano para a tabela do 2º Ano (Ano 2, 3º semestre, Formação Específica) |
| Organização e Processos | 40h | já estava correta |
| Sociedade e Trabalho | 40h | já estava correta (semestre não especificado na fonte) |
| Oficina de Integração I | 80h | já estava correta |

Além disso, corrigido o **Subtotal do 1º Ano** (Formação Geral: 880h, não 840h como constava) e, por consequência, a **tabela de síntese final** (Formação Geral 2.280h / 71,3%; Formação Técnica 680h / 21,3%; Núcleo Politécnico 240h / 7,5%; TOTAL 3.200h / 100,0%).

## 3. Limitação técnica desta sessão — arquivo dividido em partes

As ferramentas de Google Drive disponíveis nesta sessão **não permitem sobrescrever, anexar ou apagar** o arquivo `ementario_adm.tex` original — apenas criar arquivos novos com conteúdo enviado inline em uma única chamada. Como o arquivo corrigido completo tem ~209 KB, ele foi dividido em **13 arquivos sequenciais**, todos na mesma pasta (`documento-ppc-principal`, id `1aU5o-NfdMonI8WCcox4rudJxYgUrcy47`):

| Ordem | Arquivo | Conteúdo | fileId |
|---|---|---|---|
| 1 | `ementario_adm_CORRIGIDO.tex` | Cabeçalho + Matriz Curricular Detalhada (3 tabelas por Ano + síntese) | `1UvVbaEbI8Kbi34z97S0frWyd_HA71KBE` |
| 2 | `ementario_adm_CORRIGIDO_parte2.tex` | TABELA EMENTA 1–2 (Artes Ano1/2) | `1JqQGDNL7qS0lIhEsPz7MZ-Q_4-RQn_qK` |
| 3 | `ementario_adm_CORRIGIDO_parte3.tex` | TABELA EMENTA 3–9 (Ed. Física, Inglês, LPL) | `1VuwL5deoT9cygKk8Gg2KrHLS2AX0I5Vf` |
| 4 | `ementario_adm_CORRIGIDO_parte4.tex` | TABELA EMENTA 10–13 (Espanhol Ano1/2, Biologia Ano1/3) | `1_RQNPGhUzO8B9-1sr6sbIf7pr4zrRcz9` |
| 5 | `ementario_adm_CORRIGIDO_parte5.tex` | TABELA EMENTA 14–19 (Física Ano1/2/3, Matemática Ano1/2/3) | `1m1Kz1UBJsWkaKbfuV_bd-GkW4H_wULfJ` |
| 6 | `ementario_adm_CORRIGIDO_parte6.tex` | TABELA EMENTA 20–24 (Química Ano1/2/3, Filosofia Ano1/3) | `1PqbaM8UqSjIpJ8HX7SLHoOaLWGY0iLwd` |
| 7 | `ementario_adm_CORRIGIDO_parte7.tex` | TABELA EMENTA 25–30 (Geografia Ano1/3, História Ano2/3, Sociologia Ano1/2) | `1njXQ_MNRtWPPy8GVhmEiMp-ZnwB419Df` |
| 8 | `ementario_adm_CORRIGIDO_parte8.tex` | TABELA EMENTA 31–33 (Oficina de Integração I —Sem.4e5, —Ano2, Oficina II) | `16MvuPd5b2pKZxGgsTHW8qmdJAPt9v5JO` |
| 9 | `ementario_adm_CORRIGIDO_parte9.tex` | TABELA EMENTA 34–36 (Introd. à Administração, Sociedade e Trabalho, Matemática p/ Administração) | `1_336selNY_A9Tmh7xryq-rsnUszu4vBS` |
| 10 | `ementario_adm_CORRIGIDO_parte10.tex` | TABELA EMENTA 37–39 (Gestão de Marketing I, Organização e Processos, Informática Aplicada) | `1eiQ-CDf7NB1TqJvygJ4SMCD7s5CS1HZW` |
| 11 | `ementario_adm_CORRIGIDO_parte11.tex` | TABELA EMENTA 40–41 (Gestão de Marketing II, Gestão de Operações e Qualidade) | `14iMgCi5CAfkCnL_Q4i6zK3torwEJdVTg` |
| 12 | `ementario_adm_CORRIGIDO_parte12.tex` | TABELA EMENTA 42–44 (Empreendedorismo I, Resp. Socioambiental, Empreendedorismo II) | `11_t4HYbgXt7tClvvivRgzXsKcWYRXYLC` |
| 13 | `ementario_adm_CORRIGIDO_parte13.tex` | TABELA EMENTA 45–46 (Gestão de Pessoas, Gestão Financeira) | `1BN16c63ru6ckOUwVwYoeiUYlnYPgbPUq` |

**Nota:** o arquivo da parte 1 tem o nome `ementario_adm_CORRIGIDO.tex` (igual ao "nome final" desejado), mas na verdade contém **apenas a Matriz Curricular**, não o ementário completo — isso é um efeito colateral de eu não conseguir apagar/renomear esse primeiro arquivo criado antes de perceber a necessidade de particionamento. Não usar esse arquivo isoladamente como se fosse o `.tex` completo.

### Como reconstituir o arquivo único

Para gerar o `ementario_adm.tex` corrigido completo e substituir o arquivo usado pelo pipeline local do Antigravity:

1. Baixar os 13 arquivos acima, na ordem da tabela (parte 1 → parte 13).
2. Concatená-los em sequência, exatamente nessa ordem, em um único arquivo `.tex` (ex.: `cat parte1 parte2 ... parte13 > ementario_adm.tex` em um terminal, preservando a ordem — não há necessidade de remover ou adicionar nenhuma linha entre eles, o conteúdo já foi dividido em pontos de corte "limpos", entre o fim de um bloco `\end{xltabular}` e o início do comentário `% TABELA EMENTA N` seguinte).
3. Abrir o resultado e conferir visualmente se as 46 tabelas aparecem em sequência (comentários `% TABELA EMENTA 1` até `% TABELA EMENTA 46`) e se a Matriz Curricular está no topo.
4. Substituir manualmente o conteúdo do arquivo `ementario_adm.tex` (fileId `19-2ClpYCRHVVMsPBrbPtw8i82QRtJ5W0`) usado pela pipeline de compilação local do Antigravity por este conteúdo reconstituído — isso precisa ser feito manualmente porque as ferramentas de Drive disponíveis nesta sessão não têm função de sobrescrever/substituir um arquivo existente.
5. Recompilar o PPC principal (`\input`/`\include` deste arquivo) para validar visualmente.

## 4. Verificação de qualidade realizada

- Contagem de blocos: 46/46 (`% TABELA EMENTA` markers), batendo exatamente com os 46 títulos `# Unidade Curricular:` da fonte `.md`.
- Balanceamento de ambientes LaTeX no arquivo local de referência: 46 `\begin{xltabular}` / 46 `\end{xltabular}`; 92 `\begin{itemize}`/`\end{itemize}`; 4 `\begin{table}`/`\end{table}`.
- Contagem de referências bibliográficas (Básica/Complementar) verificada manualmente contra a fonte para as seguintes UCs, todas batendo exatamente (sem padding, sem truncamento):
  - **Matemática — Ano 1:** 3 básica / 2 complementar
  - **Matemática para Administração:** 2 básica / 4 complementar
  - Artes — Ano 1: 2 básica / 4 complementar
  - História — Ano 3: 2 básica / 13 complementar (bibliografia extensa real, não erro)
  - Informática Aplicada: 2 básica / 6 complementar
  - Empreendedorismo II: 5 básica / 4 complementar

## 5. Ambiguidade encontrada (reportada, não resolvida por conta própria)

- **Sociedade e Trabalho:** a fonte `.md` traz explicitamente `Ano/Semestre: Não especificado no documento fonte`. Mantive essa informação como está no ementário corrigido (campo "Semestre" com o texto "Não especificado no documento fonte"), em vez de inferir um semestre. Recomendo que a coordenação/docente responsável esclareça esse dado para a versão final do PPC.
- Alguns registros de CH na fonte trazem a ressalva "horas, se disponível no documento" (ex.: Gestão de Marketing I/II, Empreendedorismo I, Gestão Financeira) — mantive os valores exatamente como informados na fonte, sem arredondar ou presumir.
