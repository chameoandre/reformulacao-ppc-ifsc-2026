# Mecanismo de Revisão e Destaque Visual em Azul (LaTeX / PPCs)

Este documento documenta o padrão técnico e a arquitetura da macro de revisão utilizada nos Projetos Pedagógicos de Curso (PPCs) do IFSC Câmpus Garopaba para destacar alterações textuais e ementárias em **azul**, permitindo a alternância instantânea entre a versão de trabalho com destaques e a versão final limpa para publicação institucional.

---

## 1. Arquitetura da Macro no Preâmbulo (`main_ppc_*.tex`)

No arquivo raiz do documento LaTeX, logo após a declaração dos pacotes de cor (`\usepackage{xcolor}`), declara-se a condicional `\ifhighlightchanges`:

```latex
% =========================================================
% CONTROLE DE REVISÃO (DESTAQUE DE ALTERAÇÕES EM AZUL)
% =========================================================
\newif\ifhighlightchanges
\highlightchangestrue   % Mude para \highlightchangesfalse para desativar os destaques

\ifhighlightchanges
  \newcommand{\revisao}[1]{\textcolor{blue}{#1}}
\else
  \newcommand{\revisao}[1]{#1}
\fi
```

### 🎛️ Modos de Operação:
* **Modo Revisão Ativo (`\highlightchangestrue`):** Todas as alterações envolvidas por `\revisao{...}` são renderizadas na cor **azul** no PDF compilado, facilitando a conferência pelos pares, comissão do curso, coordenação pedagógica e biblioteca.
* **Modo Final Limpo (`\highlightchangesfalse`):** O comando `\revisao{...}` atua como uma função identidade (renderiza o texto puro sem alterar a cor), gerando o PDF institucional final sem necessidade de remover nenhuma tag do código-fonte.

---

## 2. Boas Práticas e Regras de Aplicação no Código TeX

### A. Em Parágrafos de Texto Corrido
Envolver o parágrafo ou frase alterada diretamente:
```latex
\revisao{A organização do trabalho pedagógico fundamenta-se nos princípios da Pedagogia Histórico-Crítica e na concepção de formação humana integral.}
```

### B. Em Listas de Itens (`itemize` / `enumerate`)
**Nunca** envolver o comando `\item` dentro da tag `\revisao`. O correto é aplicar o comando ao conteúdo interno de cada item:
```latex
\begin{itemize}
    \item \revisao{Possibilitar a compreensão do mundo e suas transformações históricas e sociais;}
    \item \revisao{Desenvolver conhecimentos e competências profissionais relacionados à gestão.}
\end{itemize}
```

### C. Em Células de Tabelas Longas (`xltabular` / `tabularx`)
Nas tabelas ementárias, aplicar a tag estritamente ao conteúdo textual dentro das células, mantendo comandos de estrutura (`\multicolumn`, `\multirow`, `\newline`, `\\ \hline`) fora da tag:
```latex
\multicolumn{3}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{
\textbf{Metodologia:} \revisao{Aulas dialogadas e práticas em laboratório com uso do AVA Moodle.} \newline
\textbf{Avaliação:} \revisao{Avaliação formativa e processual contínua.}
} \\ \hline
```

### D. Em Referências Bibliográficas (NBR 6023)
Envolver toda a referência individual padronizada:
```latex
\revisao{PROENÇA, Graça. \textbf{História da arte}. 17. ed. São Paulo: Ática, 2010.} \newline
\revisao{GOMBRICH, Ernst Hans. \textbf{A história da arte}. 16. ed. Rio de Janeiro: LTC, 1999.}
```

---

## 3. Escopo de Uso em Outros PPCs
Esta mesma estrutura deve ser replicada para os demais cursos técnicos (ex.: Técnico em Informática Integrado) e cursos superiores do câmpus, garantindo rastreabilidade, transparência nas rodadas de consulta pública e agilidade na aprovação nos órgãos colegiados (Colegiado de Curso, Conselho de Câmpus, CEPE e CONSUP).
