\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ifsc-ppc}[2026/05/08 Classe para PPCs do IFSC Garopaba]

\LoadClass[12pt,a4paper]{article}

% --- Pacotes Básicos ---
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[brazil]{babel}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{geometry}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{tikz}
\RequirePackage{tcolorbox}
\RequirePackage{float}
\RequirePackage{tabularx}
\RequirePackage{enumitem}
\RequirePackage{colortbl}
\RequirePackage{fontspec}
\setmainfont{Trebuchet MS}
\setsansfont{Trebuchet MS}
\renewcommand{\familydefault}{\sfdefault} % Garante que TODO o documento use a Sans (Trebuchet)

% --- Definição de Cores ---
\definecolor{ifscgreen}{RGB}{50, 160, 65}
\definecolor{ifsclightgreen}{RGB}{240, 250, 240}
\definecolor{ifscreed}{RGB}{200, 30, 30}
\definecolor{cinzaTabela}{RGB}{240, 240, 240}

% --- Margens ---
\geometry{
    top=4cm,
    bottom=2.5cm,
    left=3cm,
    right=2.5cm,
    headheight=3cm
}

% --- Fundo da Capa (Imagem Real) ---
\newcommand{\makeifscbackground}{
    \begin{tikzpicture}[remember picture,overlay]
        \node[inner sep=0pt] at (current page.center) {
            \includegraphics[width=\paperwidth,height=\paperheight]{../../modelos/latex-shared/identidade_visual/image2.png}
        };
    \end{tikzpicture}
}

% --- Ajuste de Numeração (Padrão IFSC) ---
\renewcommand{\thesection}{\Roman{section}}
\renewcommand{\thesubsection}{\arabic{subsection}}
\renewcommand{\thesubsubsection}{\thesubsection.\arabic{subsubsection}}
\renewcommand{\theparagraph}{\thesubsubsection.\arabic{paragraph}}

% Habilitar numeração e exibição no sumário até o 4º nível
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{4}

% Fazer a numeração das subseções ser contínua (não reinicia na seção)
\usepackage{chngcntr}
\counterwithout{subsection}{section}

% --- Estilo de Títulos ---
\titleformat{\section}
    {\color{ifscgreen}\Large\bfseries\uppercase}
    {\thesection\ --}{1em}{}
    [\titlerule]

\titleformat{\subsection}
    {\color{ifscgreen}\large}
    {\thesubsection.}{1em}{}

\titleformat{\subsubsection}
    {\color{ifscgreen}\normalsize}
    {\thesubsubsection.}{1em}{}

\titleformat{\paragraph}
    {\normalsize}
    {\theparagraph}{1em}{}

% --- Configuração de Cabeçalho e Rodapé ---
\pagestyle{fancy}
\fancyhf{}
% Cabeçalho expandido por TODA a largura da folha (sangrado)
\fancyhead[C]{
    \begin{tikzpicture}[remember picture,overlay]
        \node[anchor=north, inner sep=0pt] at (current page.north) {
            \includegraphics[width=\paperwidth,height=2.8cm]{../../modelos/latex-shared/identidade_visual/image1.png}
        };
    \end{tikzpicture}
} 
% Rodapé com numeração à direita formatada como [ n ]
\fancyfoot[R]{\color{ifscgreen} \textbf{[ \textit{\thepage} ]}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% --- Comando para a Capa ---
\newcommand{\capaPPC}[2]{
    \thispagestyle{empty}
    \makeifscbackground
    
    \begin{center}
        \vspace*{1cm}
        % Quadro sem borda (boxrule=0pt) e texto em itálico
        \begin{tcolorbox}[standard jigsaw, colframe=ifscgreen, opacityback=0, boxrule=0pt, width=1.0\textwidth, center]
            \centering \itshape \bfseries \color{ifscgreen} \Large INSTITUTO FEDERAL DE SANTA CATARINA \\ \large CÂMPUS GAROPABA
        \end{tcolorbox}
        
        \vfill
        
        % Título unificado, em itálico e com tamanho 48pt
        {\fontsize{48}{54}\selectfont \itshape \bfseries \color{ifscgreen} #1} \\
        \vspace{1cm}
        % Texto vermelho removido conforme solicitado
        
        \vfill
        
        % Logo e texto removidos do rodapé pois já constam na imagem de fundo oficial
    \end{center}
    \newpage
}
