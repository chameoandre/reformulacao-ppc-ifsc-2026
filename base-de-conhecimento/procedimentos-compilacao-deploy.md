# Procedimentos de Compilação, Sincronização e Deploy

Este documento orienta o fluxo de trabalho automatizado para manutenção dos documentos PPC e deploy contínuo dos artefatos.

---

## 1. Sincronização 1:1 (Markdown e LaTeX)

- A fonte primária de conteúdo detalhado é mantida nos arquivos Markdown de ementário (`todas_ementas_administracao.md` e futuro `todas_ementas_informatica.md`).
- Qualquer alteração textual ou de bibliografia deve ser replicada de maneira sincronizada 1:1 no respectivo arquivo `.tex` (`ementario_adm.tex`).

---

## 2. Compilação Não Interativa com `tectonic`

Para compilar o documento final do PPC sem pausas interativas:
```bash
cd tecnico-administracao/documento-ppc-principal
tectonic main_ppc_administracao.tex
```

O arquivo compilado `main_ppc_administracao.pdf` é gerado na mesma pasta e deve ser versionado no Git para entrega e download direto.

---

## 3. Deploy no GitHub Pages

- O repositório possui páginas estáticas e documentação HTML (`index.html`) servidas pelo GitHub Pages.
- O arquivo `.nojekyll` deve ser mantido na raiz para evitar problemas de processamento de arquivos auxiliares ou PDFs.
