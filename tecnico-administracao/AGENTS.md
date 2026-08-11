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

1. **Formação Geral (BNCC + Diversificada):** Minimum **2.100 hours** (clock-hours).
2. **Formação Técnica Profissional (Administração):** **1.000 hours** (conforme Catálogo Nacional CNCT).
3. **Núcleo Politécnico Comum (Projetos & Oficinas de Integração):** Minimum **120 hours**.
4. **Carga Horária Total Mínima:** **3.100 horas-relógio**.
5. **Duração do Curso:** 3 anos (6 semestres) com ingresso anual de 40 vagas no Câmpus Garopaba.

---

## 4. Compilation & Verification Directives

- Always compile TeX files using `tectonic`:
  `cd tecnico-administracao/documento-ppc-principal && tectonic main_ppc_administracao.tex`
- Ensure PDF builds cleanly with 0 errors before presenting to the user.
