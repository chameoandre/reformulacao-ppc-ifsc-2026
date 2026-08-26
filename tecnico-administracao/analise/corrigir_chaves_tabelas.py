# -*- coding: utf-8 -*-

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# Fix Table 5
tex = tex.replace(
    r"\revisao{Abordagem de Temáticas Transversais: Discussão sobre cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes.",
    r"\revisao{Abordagem de Temáticas Transversais: Discussão sobre cidadania e segurança no trânsito, práticas sustentáveis em relação ao meio ambiente, e respeito aos direitos humanos em diferentes culturas hispanofalantes.}"
)

tex = tex.replace(
    r"\textbf{Avaliação:} \revisao{Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva.}} \\ \hline",
    r"\textbf{Avaliação:} \revisao{Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva.} \\ \hline"
)

# Fix Table 35
tex = tex.replace(
    r"O SIGAA será empregado como AVA. \newline\vspace{2pt}",
    r"O SIGAA será empregado como AVA.} \newline\vspace{2pt}"
)

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Chaves de Table 5 e Table 35 corrigidas!")
