# -*- coding: utf-8 -*-

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

old_bib = r"""\subsection{Biblioteca:}
Atendimento às normativas do GT de Acervos Digitais e Diretrizes do IFSC, garantindo aos discentes acesso à Plataforma de Livros Digitais (Minha Biblioteca/Pearson), base de dados Target GEDWeb e periódicos científicos."""

new_bib = r"""\subsection{Biblioteca:}
\revisao{Vinculada ao Sistema de Bibliotecas Integradas do IFSC (SiBI/IFSC), formalizado pela Resolução nº 025/2018/CEPE, de 15 de março de 2018, a biblioteca do Câmpus Garopaba dispõe de ampla infraestrutura física, totalizando 233,52 m², dividida nas seguintes salas temáticas: sala para pesquisa virtual e acesso à internet com 11 (onze) computadores; sala de estudo individual; e sala de processamento técnico. No hall de entrada, conta com balcão de atendimento e empréstimo e mesas para estudo em grupo. Seu quadro funcional é composto atualmente por 1 (um) Bibliotecário-Documentalista e 2 (duas) Auxiliares de Biblioteca.}

\revisao{A Sala de Pesquisa Virtual possui 11 mesas, cadeiras e computadores conectados à internet com programas instalados para uso dos estudantes e da comunidade externa, dando suporte permanente às atividades de Ensino, Pesquisa e Extensão. O espaço do acervo conta com 6 mesas redondas, 2 retangulares e um total de 32 assentos para estudos em grupo. A Sala de Estudos Individuais dispõe de 2 mesas e 15 cadeiras. A biblioteca conta com cobertura de rede Wi-Fi institucional, iluminação adequada e climatização completa no salão principal, no espaço do acervo físico e na sala de processamento técnico.}

\revisao{A formação e desenvolvimento do acervo visa contemplar materiais e bibliografias que deem suporte rigoroso às atividades curriculares do curso. Para o Curso Técnico em Administração, a biblioteca dispõe de aproximadamente 90\% dos títulos indicados nas bibliografias básica e complementar das unidades curriculares em seu acervo físico, estando as demais obras em processo de aquisição e plenamente acessíveis via acervos digitais (Minha Biblioteca/Pearson e bases conveniadas). O acesso aos espaços e materiais é livre para todos os estudantes, com atendimento de segunda a sexta-feira, em regime de no mínimo 12 horas diárias.}

\revisao{O gerenciamento do acervo e os serviços de consulta, reserva e empréstimo são realizados por meio do software Sophia Biblioteca (\url{https://biblioteca.ifsc.edu.br/}), permitindo o empréstimo domiciliar de até 10 exemplares com renovação quinzenal. O acesso à biblioteca virtual (Minha Biblioteca) ocorre mediante cadastro institucional em até 48 horas. Informações complementares sobre os serviços do SiBI/IFSC encontram-se disponíveis no portal do câmpus (\url{https://www.ifsc.edu.br/web/campus-garopaba/bibliotecas}).}"""

if old_bib in tex:
    tex = tex.replace(old_bib, new_bib)
else:
    print("ERRO: Bloco da biblioteca antigo não encontrado!")

with open('tecnico-administracao/documento-ppc-principal/main_ppc_administracao.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Subitem 27 (Biblioteca) atualizado com a redação oficial do Bibliotecário David Milhomens!")
