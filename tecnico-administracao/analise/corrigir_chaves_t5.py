# -*- coding: utf-8 -*-

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

tex = tex.replace(
    r"\textbf{Avaliação:} \revisao{Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva.} \\ \hline",
    r"\textbf{Avaliação:} \revisao{Avaliação contínua baseada em tarefas orais e escritas, além de testes de compreensão auditiva.}} \\ \hline"
)

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("Chave de Table 5 corrigida com sucesso!")
