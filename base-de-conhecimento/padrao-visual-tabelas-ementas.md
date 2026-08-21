# Padrão Visual e Estrutura das Tabelas de Ementas em LaTeX

Este documento detalha o padrão de implementação visual das tabelas de Unidades Curriculares adotado nos Projetos Pedagógicos de Curso do IFSC Câmpus Garopaba.

---

## 1. Ambiente `xltabular` e Quebra de Página

- Cada Unidade Curricular é isolada em sua própria página utilizando `\clearpage` antes da declaração da tabela.
- Utiliza-se o ambiente `xltabular` para permitir quebras de página automáticas e consistentes caso o conteúdo exceda uma única página:
  ```latex
  \clearpage
  % ---------------------------------------------------------
  % TABELA EMENTA N: <Nome da UC>
  % ---------------------------------------------------------
  \begin{xltabular}{\linewidth}{|X|p{2.5cm}|p{2.5cm}|}
  \hline
  ...
  \endfirsthead
  ...
  \end{xltabular}
  ```

---

## 2. Paleta de Cores Institucional

- **Verde IFSC:** `\textcolor{ifscgreen}{...}` ou `\rowcolor{ifscgreen!20}` para títulos de blocos e cabeçalhos de campos.
- **Cinza Tabela:** `\rowcolor{cinzaTabela}` para linhas de subtítulos e divisores.

---

## 3. Campos Obrigatórios de Cada Ementa

1. **Cabeçalho:** Nome da UC, Semestre, CH EaD e CH Total.
2. **Objetivos:** Lista de itens (`\begin{itemize}[leftmargin=*,noitemsep,topsep=2pt]`).
3. **Conteúdos:** Itens temáticos separados por `\newline`.
4. **Estratégias de Ensino e Aprendizagem:** Metodologia e Avaliação.
5. **Bibliografia Básica:** Obras de referência básica formatadas em ABNT NBR 6023, separadas por `\newline`.
6. **Bibliografia Complementar:** Obras complementares formatadas em ABNT NBR 6023, separadas por `\newline`.
