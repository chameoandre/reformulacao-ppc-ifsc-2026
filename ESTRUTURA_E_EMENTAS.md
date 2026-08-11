# Estrutura do Projeto e Guia para Descarregamento de Ementas (PPC 2026)

## 📁 Estrutura de Diretórios Organizada

```
reformulacao-ppc-informatica-administracao-integrado/
├── tecnico-administracao/
│   ├── main_ppc_administracao.tex    # Documento TeX principal do PPC Administração
│   ├── analise_ppc_administracao.tex   # Análise comparativa e diagnóstica
│   ├── resumo_status_administracao.md # Resumo e status das UCs
│   ├── PPC_Administração_OFICIAL_V2.gdoc
│   └── ementas/                        # 👈 Pasta para receber as ementas (.md, .tex, .docx, .pdf)
├── tecnico-informatica/
│   ├── main_ppc_informatica.tex      # Documento TeX principal do PPC Informática
│   ├── analise_ppc_informatica.tex     # Análise comparativa e diagnóstica
│   ├── resumo_status_informatica.md   # Resumo e status das UCs
│   ├── PPC_Informática_OFICIAL_V2.gdoc
│   ├── integrado-informatica-GPB-original.pdf
│   └── ementas/                        # 👈 Pasta para receber as ementas (.md, .tex, .docx, .pdf)
├── modelos/
│   ├── documentos-oficiais/           # Formulários em .odt, .docx e modelos preenchidos
│   ├── latex-shared/                  # Classe TeX ifsc-ppc.cls e identidade visual (logos, marcas d'água)
│   ├── latex-template/                # Template TeX de referência e guia de manutenção
│   └── ppc-referencia-lazer/          # PPC modelo de referência do Técnico em Lazer GPB
├── normativas-diretrizes/
│   ├── Resoluo_142_Consup...pdf        # Diretrizes Curriculares dos Cursos Técnicos
│   ├── resumo_resolucao_142_2025.tex   # Resumo TeX da Resolução 142/2025
│   └── Diretrizes_gerais_GT...pdf
├── PPC-LATEX-SHARED/                  # Classe TeX ifsc-ppc.cls e logotipos
├── PPC-LATEX-TEMPLATE/                # Guia e templates TeX de referência
├── reunioes/                          # Atas e memórias de reunião
├── plano_reformulacao_master.md       # Plano master da reformulação
└── comparativo_carga_horaria_master.csv
```

---

## 📌 Guia para Descarregamento / Exportação das Ementas do Google Drive

### ⚠️ Por que descarregar/exportar os arquivos `.gdoc`?
Os arquivos `.gdoc` no Google Drive para Desktop são apenas **atalhos de 191 bytes** contendo links da nuvem. O assistente local não consegue ler o texto interno de um arquivo `.gdoc` não exportado.

### 📥 Formatos Recomendados para Salvar nas Pastas de Ementas:
Ao exportar/salvar as ementas do Google Drive para as pastas localizadas em:
- `tecnico-administracao/ementas/`
- `tecnico-informatica/ementas/`

Utilize prioritariamente um dos seguintes formatos:
1. **Markdown (`.md`)** ou **Texto Puro (`.txt`)** *(Recomendado pela simplicidade e parsing imediato)*;
2. **LaTeX (`.tex`)** *(Se já formatado com tabelas de ementa)*;
3. **Microsoft Word (`.docx`)** ou **PDF (`.pdf`)**.

### 🏷️ Padrão Recomendado para Nomeação dos Arquivos:
- `ementa-<nome-da-uc>.md` (ex: `ementa-programacao-web-1.md`, `ementa-banco-de-dados.md`, `ementa-gestao-financeira.md`).
