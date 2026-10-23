# Análise do retorno do CEPE — PPC Técnico em Administração Integrado

**Processo:** 23292.030989/2026-91
**Recebido via:** DEPE Garopaba, 13/10/2026
**Documentos analisados** (em `anexos-cepe/`):
- `Conformidade_DIREN_...docx`: checklist de conformidade, **Etapa 1 – Análise da DIREN**. A Etapa 2 (parecerista do CEPE) ainda está em branco, então o PPC ainda não foi relatado no CEPE.
- `parecer 1.pdf`: despacho da Coordenadoria do Sistema de Bibliotecas (SiBI) sobre normalização ABNT NBR 6023:2018.

**Base de comparação:** `documento-ppc-principal/main_ppc_administracao.tex` e `ementario_adm.tex` (versão de 11/09/2026).

---

## 1. Resumo

| # | Apontamento | Origem | Tipo | Decisão da comissão? |
|---|---|---|---|---|
| A | CH técnica 680 h < 800 h mínimas; distribuição do Núcleo Politécnico (160 h) entre FG e FT não explicitada | DIREN itens 2.1, 2.2 | Estrutural (matriz) | **Sim** |
| B | Indicar Espanhol/Libras na matriz e incluir ementa de Libras | DIREN itens 17, 18 | Estrutural (matriz + ementa) | **Sim** |
| C | Reconferir matriz × ementas × CH total após o ajuste A | DIREN item 20 | Conferência | Não (decorre de A) |
| D | Divergências de formatação/organização em relação ao formulário padrão do CEPE | DIREN item 12 | Formatação | Não |
| E | Turno integral: atividades em mais de dois dias no contraturno | DIREN item 4 | Observação | Não (só conferir o texto) |
| F | Referências: autoria invertida, pontuação, `[S. l.]` | SiBI itens 2 e 3 | Correção pontual | Não |
| G | Revisão integral da normalização bibliográfica pela biblioteca e retorno ao SiBI | SiBI (fecho) | Fluxo | Não |
| — | Item 1 do SiBI (referência "Livro didático… FNDE") | SiBI item 1 | **Desconsiderar** (confirmado pela Biblioteca do câmpus em 13/10) | — |

Itens verificados **sem pendência** pela DIREN: nome do curso, vagas (40), início 2027/1, matrícula seriada, oferta anual, ingresso, regime semestral, CNCT, integralização, perfil e área do egresso, objetivos/conteúdos, CH múltipla de 20 h, eixo × planejamento do câmpus.

---

## 2. Ponto A — Carga horária técnica e Núcleo Politécnico (crítico)

### Situação atual do PPC (conferida no `ementario_adm.tex`)

| Bloco | 1º ano | 2º ano | 3º ano | Total |
|---|---|---|---|---|
| Formação Geral | 880 h | 800 h | 600 h | **2.280 h** |
| Formação Técnica | 240 h | 240 h | 200 h | **680 h** |
| Núcleo Politécnico (OI I + OI II) | — | 80 h | 80 h | **160 h** |
| **Total** | 1.120 h | 1.120 h | 880 h | **3.120 h** |

As somas estão corretas. O problema é de **contabilização**: sem atribuir parte do Núcleo Politécnico à FT, o curso fica com 680 h técnicas, abaixo das **800 h** do CNCT para Administração.

### A regra citada pela DIREN (Diretrizes dos Integrados do IFSC)
- (c) Com o Núcleo Politécnico no mínimo de **120 h**, ele é dividido entre FG e FT, **preferencialmente de modo paritário**.
- (d) O que **passar de 120 h** pode ir para a FT ou ampliar a CH total do curso (limite de 10%).

### Cenários

| Cenário | Distribuição dos 160 h | FT | FG | Total | Atende 800 h? | Observação |
|---|---|---|---|---|---|---|
| **1. Proposta da área de Administração** | 120 h FT / 40 h FG | **800 h** | 2.320 h | 3.120 h | Sim, no limite | Não mexe na matriz. Usa a flexibilidade do "preferencialmente". O e-mail fala em "120 h técnica e 60 h geral", mas isso soma 180 h; com 160 h a conta fecha com **120/40**. |
| **2. Leitura estrita da regra (c)+(d)** | 60 FG / 60 FT (base paritária) + 40 h excedente → FT = 100 h FT / 60 h FG | 780 h | 2.340 h | 3.120 h | **Não (faltam 20 h)** | Exigiria **+20 h numa UC técnica** (ex.: no 6º semestre, que tem 400 h) → FT 800 h, total 3.140 h (dentro do limite de 3.300 h). |
| **3. Sugestão do DEPE: "unificar" FG e FT na UC integradora** | Declarar a OI como componente compartilhado, com a CH contabilizada nas duas formações em proporção explícita | depende da proporção | — | 3.120 h | Depende | Na prática converge para o cenário 1 ou 2: a DIREN pede que a proporção apareça **explicitamente**. |

**Leitura técnica:** o cenário 1 resolve o problema sem reabrir a matriz. O risco é o parecerista do CEPE entender que 120/40 se afasta demais do "paritário". O cenário 2 é o mais seguro diante da regra, mas custa 20 h a mais e mexe em alguma UC técnica. Fica para a reunião da comissão.

### Onde alterar depois da decisão
- `ementario_adm.tex`, Quadro Síntese (≈ l. 110–130): mostrar a FT e a FG **com a parcela do Núcleo Politécnico** (ex.: "Formação Técnica: 680 h + 120 h NP = 800 h").
- Ementas de **Oficina de Integração I** (≈ l. 1626) e **II** (≈ l. 2191): incluir a linha "Distribuição da CH: X h Formação Técnica / Y h Formação Geral".
- `main_ppc_administracao.tex` l. 374 (texto da matriz curricular): citar a distribuição e a regra das Diretrizes.
- Campos de CH do formulário (item 7.6, l. 136–137) e qualquer outro lugar que traga 680 h ou 2.280 h.
- Se for o cenário 2: alterar a UC escolhida, os subtotais do semestre e do ano, e a CH total (3.120 → 3.140) em **todas** as menções (l. 136, 137, 374, 385).

---

## 3. Ponto B — Espanhol / Libras (decisão da comissão)

**O que a DIREN pede** (art. 7º, §§ 1º e 2º da normativa): o estudante deve cursar ao menos **uma** entre Espanhol e Libras, além do Inglês. Se houver estudante surdo matriculado, **Libras** tem que ser ofertada. A DIREN recomenda:
1. indicar na matriz a possibilidade de oferta **"Língua Espanhola / Libras"**;
2. incluir a **ementa de Libras**, mesmo que a oferta dependa da situação prevista na normativa.

**Situação atual:** o Espanhol **já está** na matriz (Ano 1 e Ano 2, 80 h + 80 h = 160 h, Formação Geral). Então o pedido **não é incluir Espanhol**, e sim:
- renomear as linhas da matriz para "Língua Espanhola / Libras — Ano 1/2", com nota de rodapé explicando a regra de oferta;
- **redigir duas ementas de Libras** (Ano 1 e Ano 2, 80 h cada, no mesmo padrão das outras);
- não mexe na CH total.

**Pontos para a reunião:**
- O quadro docente do PPC **não tem professor de Libras**. A equipe de Educação Especial pode ajudar a redigir as ementas, e o item 31 da Etapa 2 (recursos humanos) pode cobrar isso.
- Quem redige as ementas de Libras e qual o prazo.

---

## 4. Pontos sem decisão (execução direta)

### C — Reconferência (DIREN item 20)
Depois de fechar o ponto A, conferir de novo: soma das ementas = matriz = quadro síntese = campos 7.6 = textos das l. 374 e 385. Dá para automatizar com script, como foi feito nos itens 23/25 em `analise/`.

### D — Formulário padrão (DIREN item 12)
A DIREN não lista quais são as divergências. Ação: comparar seção por seção com o modelo do CEPE (ver `modelos/`) e anotar as diferenças de título, ordem e numeração.

### E — Turno (DIREN item 4)
A DIREN só registra que o turno é integral (atividades em mais de dois dias no contraturno). Basta conferir se o PPC declara "Integral" de forma coerente com o horário.

### F — Correções bibliográficas do SiBI (itens 2 e 3)

| Item | Onde no `.tex` | Atual | Corrigir para |
|---|---|---|---|
| 2 | `ementario_adm.tex` l. 687 e l. 1392 | `HELENA, Bomeny et al.` | `BOMENY, Helena et al.` |
| 3 | `ementario_adm.tex` l. 171 | `dança : hip-hop` | `dança: hip-hop` |
| 3 | `ementario_adm.tex` l. 916 | `[s.l.]` | `[S. l.]` |
| 3 | `ementario_adm.tex` l. 917 | `[S.l.]` | `[S. l.]` |
| 3 | `ementario_adm.tex` l. 1144 | `extranjera : curso` | `extranjera: curso` |

Vale também procurar outros casos parecidos (`" : "`, `[s.l.]`, `[S.l.]`, `s.n.`), porque o SiBI diz que essas foram só **exemplos**.

### G — Fluxo da bibliografia
O SiBI pede revisão **integral** pela biblioteca do câmpus (entradas de autor, títulos e subtítulos, edição, local, editora, ano, pontuação, destaque, URLs e datas de acesso). Depois disso, o PPC **volta ao SiBI** para nova conferência. A Biblioteca do câmpus pediu o arquivo editável **depois** das correções da comissão.

---

## 5. Encaminhamentos sugeridos

1. **Convocar a reunião da comissão** (pedido do DEPE), aberta a todos os servidores interessados. Pauta:
   - Ponto A: escolher o cenário 1 ou 2 (ou outra distribuição);
   - Ponto B: Espanhol/Libras, quem redige as ementas de Libras e a questão do docente.
2. Aplicar já as correções F e preparar o comparativo D (não dependem da reunião).
3. Depois da reunião: aplicar A e B, fazer a reconferência C, recompilar o PDF.
4. Enviar o arquivo editável à Biblioteca do câmpus para a revisão integral (G).
5. Devolver o PPC atualizado ao DEPE para reenvio ao CEPE.

## 6. Observações paralelas
- O `AGENTS.md` desta pasta registra **"Formação Técnica (Administração): 1.000 h"**, mas a DIREN usa **800 h** como mínimo do CNCT para Administração. Vale corrigir o `AGENTS.md` para não induzir erro nas próximas edições.
- Os itens 17/18 (Espanhol/Libras) são uma exigência geral dos integrados, então devem aparecer também na análise do **PPC de Informática**.
