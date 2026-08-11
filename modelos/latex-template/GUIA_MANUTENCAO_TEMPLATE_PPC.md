# Guia de Manutenção e Configuração do Template PPC LaTeX (IFSC)

Este documento descreve as decisões de design e os procedimentos técnicos necessários para manter e gerar os documentos de PPC utilizando o template LaTeX customizado.

## 1. Estrutura do Projeto
- `ifsc-ppc.cls`: Classe principal contendo toda a lógica de formatação, fontes e estilos.
- `main_ppc_informatica.tex`: Arquivo mestre do curso de Informática.
- `identidade_visual/`: Pasta contendo os ativos extraídos do template original.

## 2. Extração de Imagens Oficiais
O template original em formato `.docx` contém as imagens de fundo e logos incorporadas. Para extraí-las manualmente:
1. Altere a extensão do arquivo de `.docx` para `.zip`.
2. Abra o arquivo e navegue até a pasta `word/media/`.
3. Copie as imagens para a pasta `identidade_visual/`.
   - **image1.png**: Banner do Cabeçalho / Logo IFSC.
   - **image2.png**: Fundo da Capa (Pattern Verde).

*Dica: O comando `unzip` no terminal também pode ser usado para extração direta.*

## 3. Configuração de Fontes
O template utiliza a fonte **Trebuchet MS** para garantir a fidelidade ao modelo oficial do IFSC.
- **Motor de Compilação:** Necessário utilizar `XeLaTeX` ou `LuaLaTeX` (o comando `tectonic` já faz isso automaticamente).
- **Pacote:** `fontspec`.
- **Configuração na Classe:**
  ```latex
  \setmainfont{Trebuchet MS}
  \setsansfont{Trebuchet MS}
  \renewcommand{\familydefault}{\sfdefault}
  ```

## 4. Design da Capa
- **Fundo:** Inserido via TikZ no comando `\makeifscbackground`, garantindo que a imagem ocupe 100% da área física do papel (`\paperwidth`).
- **Título do Curso:** Definido com tamanho fixo de **48pt** para impacto visual:
  ```latex
  \fontsize{48}{54}\selectfont \itshape \bfseries
  ```
- **Quadro do Campus:** Implementado com `tcolorbox`, configurado como transparente (`opacityback=0`) e sem bordas (`boxrule=0pt`).

## 5. Cabeçalho e Rodapé
- **Cabeçalho (Banner):** Utiliza a `image1.png` expandida para toda a largura da folha (`\paperwidth`) posicionada no topo absoluto via TikZ.
- **Rodapé:** Numeração posicionada à direita no formato `[ n ]`, utilizando a cor `ifscgreen` e estilo itálico.

## 6. Lógica do Sumário (ToC)
A numeração segue o padrão institucional:
- **Nível 1 (Seções):** Algarismos Romanos (`I`, `II`, `III`).
- **Nível 2 (Subseções):** Algarismos Arábicos **contínuos** (`1`, `2`, `3`...).
- **Nível 3 (Sub-subseções):** Hierárquicos (`7.1`, `7.2`).

*Configuração técnica na classe:*
```latex
\usepackage{chngcntr}
\counterwithout{subsection}{section}
```

## 7. Compilação
Recomenda-se o uso do `tectonic` para uma compilação limpa que baixa as dependências automaticamente:
```bash
tectonic main_ppc_informatica.tex
```
