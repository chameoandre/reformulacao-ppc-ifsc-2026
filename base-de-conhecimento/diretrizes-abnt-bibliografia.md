# Diretrizes Normativas ABNT NBR 6023 para Bibliografias dos PPCs

Este documento estabelece as regras oficiais da Biblioteca do IFSC, as diretrizes do **Sistema de Bibliotecas do IFSC (SIBI)** e o alinhamento com a autoridade de catalogação da **Fundação Biblioteca Nacional (Sophia Web / FBN)** aplicadas às seções de **Bibliografia Básica** e **Bibliografia Complementar** de todas as Unidades Curriculares do Ementário.

---

## 1. Regra de Destaque Tipográfico (Negrito vs. Subtítulo)

### 🔴 Incorreto:
- `\textbf{História da arte do século XX: idéias e movimentos}.`
- `**A invenção do cotidiano: artes de fazer**.`

### 🟢 Correto:
- `\textbf{História da arte do século XX}: idéias e movimentos.`
- `**A invenção do cotidiano**: artes de fazer.`

> **Regra:** O destaque tipográfico (negrito) aplica-se **exclusivamente ao título principal** da obra. O caractere `:` (dois pontos) e todo o subtítulo que o segue devem permanecer em texto regular/normal (sem negrito).

---

## 2. Nomes dos Autores por Extenso (Autoridade Sophia Web / FBN)

Em conformidade com a NBR 6023 e as recomendações do SIBI/IFSC para evitar ambiguidades de autoria no acervo institucional:
- **Padrão Obrigatório:** Grafar **todos os prenomes dos autores por extenso**, reservando as iniciais apenas para o nome do meio quando for a forma consagrada da edição.
- **Conformidade com a Biblioteca Nacional:** As entradas de autoridade devem espelhar o catálogo do Sophia Web da Fundação Biblioteca Nacional.

### 📋 Exemplos de Padronização por Extenso:
| 🔴 Incorreto / Abreviado | 🟢 Correto (Por Extenso / FBN) | Obra |
| :--- | :--- | :--- |
| `PROENÇA, G.` | `PROENÇA, Graça.` | *História da arte* |
| `GOMBRICH, E. H.` | `GOMBRICH, Ernst Hans.` | *A história da arte* |
| `LARAIA, R. de B.` | `LARAIA, Roque de Barros.` | *Cultura: um conceito antropológico* |
| `CINTRA, M.; CUNHA, M. P.` | `CINTRA, Maria; CUNHA, Maria Paula.` | *Rotinas administrativas* |
| `HERMOSO, A. G.` | `GONZÁLEZ HERMOSO, Alfredo.` | *Conjugar es fácil* |
| `DANTE, L. R.` | `DANTE, Luiz Roberto.` | *Matemática: contexto e aplicações* |
| `DIAS, Marco Aurélio P.` | `DIAS, Marco Aurélio Pereira.` | *Administração de materiais* |
| `PALADINI, Edson P.` | `PALADINI, Edson Pacheco.` | *Gestão estratégica da qualidade* |
| `MARTINS, Petrônio G.; LAUGENI, Fernando P.` | `MARTINS, Petrônio Garcia; LAUGENI, Fernando Piero.` | *Administração da produção* |
| `HOBSBAWM, E. J.` | `HOBSBAWM, Eric John.` | *Era dos extremos* |
| `GITMAN, Lawrence J.` | `GITMAN, Lawrence Jeffrey.` | *Princípios de administração financeira* |
| `SARMENTO, Melo, M.` | `SARMENTO, Marlon Melo.` | *Gestão financeira por fluxo de caixa* |

---

## 3. Integridade das Tags de Autoria
- As tags de formatação (`\textbf{...}`) **nunca devem capturar prenomes, sobrenomes ou iniciais de coautores**.
- **Exemplo Incorreto:** `MANZANO, André Luiz N. \textbf{G.; MANZANO, Maria Izabel N. G. Estudo dirigido...}`
- **Exemplo Correto:** `MANZANO, André Luiz N. G.; MANZANO, Maria Izabel N. G. \textbf{Estudo dirigido de informática básica}...`

---

## 4. Uso Restrito de Itálico (*et al.*)

- O itálico **não deve ser utilizado** para destacar títulos de livros (no padrão IFSC para PPCs, utiliza-se negrito como elemento de destaque único).
- A locução latina **et al.** deve ser grafada obrigatoriamente em itálico:
  - LaTeX: `\textit{et al.}` (ou `[\textit{et al.}]`)
  - Markdown: `*et al.*` (ou `[*et al.*]`)

---

## 5. Obras com Entrada por Título (Sem Autor Declarado)

- Quando a autoria for anônima ou a obra for coletiva de referência (dicionários, atlas, guias institucionais sem autor específico):
  - A primeira palavra do título é grafada em **MAIÚSCULAS (Caixa Alta)**.
  - O título principal recebe negrito até o início do subtítulo (se houver).
- **Exemplo:** `\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014.`

---

## 6. Ausência de Numeração Manual nas Listas

- As referências não devem conter marcadores numéricos manuais (`1.`, `2.`, `3.`) nem marcadores de lista não ordenada (`-`) no documento final em LaTeX.
- As entradas são ordenadas alfabeticamente pelo sobrenome do primeiro autor ou primeira palavra do título e separadas pelo comando `\newline`.
