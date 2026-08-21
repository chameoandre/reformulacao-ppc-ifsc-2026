# Diretrizes Normativas ABNT NBR 6023 para Bibliografias dos PPCs

Este documento estabelece as regras oficiais da Biblioteca do IFSC e da norma ABNT NBR 6023 aplicadas às seções de **Bibliografia Básica** e **Bibliografia Complementar** de todas as Unidades Curriculares do Ementário.

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

## 2. Iniciais de Autores e Autoria

- As iniciais de prenomes de autores ou abreviações (ex.: `M. P.`, `S.`, `A.`) pertencem ao elemento de autoria e **nunca** devem ser capturadas dentro da tag de negrito do título.
- **Exemplo Incorreto:** `CINTRA, M.; CUNHA, M. \textbf{P. Rotinas administrativas}.`
- **Exemplo Correto:** `CINTRA, M.; CUNHA, M. P. \textbf{Rotinas administrativas}.`

---

## 3. Uso Restrito de Itálico (*et al.*)

- O itálico **não deve ser utilizado** para destacar títulos de livros (no padrão IFSC para PPCs, utiliza-se negrito como elemento de destaque único).
- A locução latina **et al.** deve ser grafada obrigatoriamente em itálico:
  - LaTeX: `\textit{et al.}` (ou `[\textit{et al.}]`)
  - Markdown: `*et al.*` (ou `[*et al.*]`)

---

## 4. Obras com Entrada por Título (Sem Autor Declarado)

- Quando a autoria for anônima ou a obra for coletiva de referência (dicionários, atlas, guias institucionais sem autor específico):
  - A primeira palavra do título é grafada em **MAIÚSCULAS (Caixa Alta)**.
  - O título principal recebe negrito até o início do subtítulo (se houver).
- **Exemplo:** `\textbf{DICIONÁRIO crítico de educação física}. 3. ed. rev. e ampl. Ijuí, RS: Ed. UNIJUÍ, 2014.`

---

## 5. Ausência de Numeração Manual nas Listas

- As referências não devem conter marcadores numéricos manuais (`1.`, `2.`, `3.`) nem marcadores de lista não ordenada (`-`) no documento final em LaTeX.
- As entradas são ordenadas alfabeticamente pelo sobrenome do primeiro autor ou primeira palavra do título e separadas pelo comando `\newline`.
