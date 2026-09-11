# Workspace Rules & Directives for PPC Técnico em Administração (Resolução 142/2025)

The rules in this file are automatically enforced when working inside `tecnico-administracao/`.

---

## 1. Directory Structure Directives

All course assets must remain strictly organized in the following subdirectories:
- `documento-ppc-principal/`: Contains the main TeX document (`main_ppc_administracao.tex`), auxiliary ementário TeX files (`ementario_adm.tex`), and compiled PDF (`main_ppc_administracao.pdf`).
- `ementas/`: Contains imported syllabus files (`.md`, `.tex`, `.docx`, `.pdf`) and cloud shortcuts.
- `analise/`: Contains comparative analysis files (`analise_ppc_administracao.tex`), diagnostic reports, and status summaries.

---

## 2. TeX Formatting Directives for Ementa Tables

1. **Table Environment:**
   - Every Unidade Curricular ementa MUST be formatted inside a `tabularx` environment:
     `\begin{tabularx}{\linewidth}{|l|X|l|X|}`

2. **Spanned Rows (`\multicolumn` Width Fix):**
   - For rows spanning all 4 columns (Ementa, Objetivos, Conteúdo Programático, Metodologia e Bibliografia), DO NOT use `\multicolumn{4}{|X|}{...}` as `tabularx` will squeeze the text into column 1 width.
   - ALWAYS use exact full-width dimensioning:
     `\multicolumn{4}{|p{\dimexpr\linewidth-2\tabcolsep-2\arrayrulewidth\relax}|}{...}`

3. **Color Tokens (IFSC Palette):**
   - Table Main Header: `\rowcolor{ifscgreen!20}`
   - Section Bars (1. EMENTA, etc.): `\cellcolor{cinzaTabela}`

---

## 3. Curriculum Directives (Resolução CONSUP/IFSC nº 142/2025)

1. **Formação Geral Integrada:** Minimum **2.100 hours** (clock-hours).
2. **Formação Técnica Profissional (Administração):** **1.000 hours** (conforme Catálogo Nacional CNCT).
3. **Núcleo Politécnico Comum (Projetos & Oficinas de Integração):** Minimum **120 hours**.
4. **Carga Horária Total Mínima:** **3.100 horas-relógio**.
5. **Duração do Curso:** 3 anos (6 semestres) com ingresso anual de 40 vagas no Câmpus Garopaba.

---

## 5. Diretrizes Oficiais para Bibliografias (SIBI/IFSC e Parecer de Biblioteca)

1. **Quantitativo Rigoroso por Unidade Curricular:**
   - **Bibliografia Básica:** EXATAMENTE **2 títulos de livros** (nem 1, nem 3+).
     - *Cursos Técnicos Integrados:* O livro didático do FNDE pode constar como um dos 2 títulos da Bibliografia Básica, devendo ser citado **exatamente como**: `Livro didático fornecido pelo Fundo Nacional de Desenvolvimento da Educação (FNDE).`
   - **Bibliografia Complementar:** NO MÍNIMO **3 títulos de livros**.
     - Artigos, leis, normas e teses podem ser citados, mas **NÃO contam** para o mínimo regulamentar de 3 livros.
     - **Espaço Reservado (Placeholder):** Caso a UC não possua o quantitativo completo, incluir formalmente a indicação de reserva: `[Título pendente de indicação docente e validação pelo acervo da Biblioteca do Câmpus]`.

2. **Vedações e Proibições:**
   - **Proibido Manuais/Apostilas:** Apostilas, cartilhas e manuais internos da instituição **NÃO podem compor a bibliografia do PPC** (devem constar apenas no Plano de Ensino).
   - **Sem Fusão de Listas:** Bibliografia Básica e Bibliografia Complementar devem ser mantidas como duas listas **separadas e identificadas**.

3. **Padronização ABNT & Tipografia:**
   - **Formato:** `SOBRENOME, Nome. \textbf{Título do Livro: subtítulo}. X. ed. Cidade: Editora, Ano.`
   - **Destaque:** O título do livro deve ser formatado com **negrito** (`\textbf{...}`) em todas as referências para garantir padronização uniforme.
   - **Ordenação Alfabética:** Todas as referências dentro de cada lista (Básica e Complementar) DEVEM estar rigorosamente em **ordem alfabética pelo sobrenome do primeiro autor**.

4. **Exemplares Mínimos na Biblioteca (Parecer da Biblioteca):**
   - **Livros Impressos:** Pelo menos 3 exemplares físicos na Biblioteca do Câmpus por título básico (ou conforme necessidade da coordenação) e 1 exemplar por título complementar.
   - **Acervo Virtual IFSC (Minha Biblioteca/Pearson):** A biblioteca precisa disponibilizar ao menos 2 exemplares físicos do título básico e 1 exemplar físico do título complementar.

---

## 6. Governança de Arquivos DOCX e Bloqueio Editorial Permanente

1. **Bloqueio Permanente e Intocabilidade de Arquivos DOCX:**
   - O arquivo `Ementario_Completo_PPC_Tecnico_Administracao_Revisao_Biblioteca.docx` (e quaisquer outros arquivos `.docx` no repositório) está **PERMANENTEMENTE BLOQUEADO PARA EDIÇÕES**.
   - Esses arquivos representam artefatos colaborativos sob custódia direta da Biblioteca (David Milhomens) e do corpo docente.
   - **Regra de Bloqueio Estrito:** A IA está terminantemente proibida de editar, modificar, sobrescrever ou regenerar arquivos `.docx`, mantendo-os permanentemente bloqueados para edições **sem questionar se pode alterar**. O assistente jamais deverá sugerir, propor ou tentar modificar o `.docx`.
   - Toda e qualquer conferência do trabalho da biblioteca deve ser feita por leitura/auditoria direta (online no Google Docs ou leitura do `.docx` de referência), transpondo eventuais ajustes exclusivamente para o código-fonte LaTeX.

2. **Fonte Única da Verdade do PPC:**
   - A fonte oficial do PPC para compilação via `tectonic` e submissão ao DEPE reside exclusivamente nos arquivos LaTeX (`main_ppc_administracao.tex` e `ementario_adm.tex`).

3. **Intocabilidade Textual dos Blocos Pedagógicos (Zero-Paraphrase Rule):**
   - **Soberania Docente:** Os campos **Ementa**, **Objetivos**, **Conteúdo Programático**, **Metodologia** e **Avaliação** de todas as 45 UCs são blocos autorais protegidos e invioláveis (*verbatim*).
   - **Veto a Modificações Textuais:** É terminantemente vedado à IA resumir, sintetizar, parafrasear, omitir ou alterar a redação de qualquer trecho pedagógico aprovado pelos docentes.
   - **Fronteira Operacional:** A IA atua única e exclusivamente na tipografia/diagramação LaTeX (tabelas, quebras de página, compilação via `tectonic`), conformidade bibliográfica ABNT NBR 6023 e consistência aritmética das cargas horárias. Toda transposição textual deve ser 100% literal.


