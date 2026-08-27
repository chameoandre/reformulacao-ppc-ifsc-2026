# -*- coding: utf-8 -*-

# 1. Atualizar tabela_de_correcoes_ppc.md
with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'r', encoding='utf-8') as f:
    text = f.read().strip()

new_row = """| **28** | Seção VII (Infraestrutura e Acessibilidade) | Subitem 27 (Biblioteca — Caracterização e Aderência do Acervo) | p. 105 | DAVID MILHOMENS (BIBLIOTECA) | Necessidade de inserção da descrição técnica oficial da biblioteca do Câmpus Garopaba e validação da aderência das bibliografias ao acervo físico e digital. | Substituição da redação preliminar pelo texto técnico oficial do Bibliotecário David Milhomens, detalhando vinculação ao SiBI/IFSC (Res. 025/2018/CEPE), área física (233,52 m²), 90% de cobertura do acervo físico, plataformas virtuais (Minha Biblioteca), sistema Sophia e normas de circulação. | **Caracterização oficial da Biblioteca inserida.** Inserido o texto institucional completo no Subitem 27 (Biblioteca), descrevendo as salas temáticas, equipamentos, 32 assentos para estudo em grupo, equipe de servidores, cobertura de 90% dos títulos em acervo físico e 100% via Minha Biblioteca/Pearson, sistema Sophia e atendimento de 12h diárias, devidamente destacado em azul para conferência pelos revisores. | **Concluído** |
"""

if "| **28** |" not in text:
    text = text + "\n" + new_row

with open('base-de-conhecimento/tabela_de_correcoes_ppc.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Item 28 adicionado à tabela de correções!")

# 2. Atualizar index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Atualizar KPI de 27 para 28
html = html.replace('<div class="kpi-value">27 Itens</div>', '<div class="kpi-value">28 Itens</div>')
html = html.replace('Checklist & Auditoria (27 Itens)', 'Checklist & Auditoria (28 Itens)')
html = html.replace('Tabela de Controle e Histórico de Correções do PPC (27 Itens)', 'Tabela de Controle e Histórico de Correções do PPC (28 Itens)')

tr_28 = """              <tr>
                <td style="text-align: center; font-weight: 700;">28</td>
                <td><strong>Subitem 27 (Biblioteca)</strong><br><small style="color: var(--text-muted);">p. 105</small></td>
                <td>David Milhomens</td>
                <td>Validação da aderência dos títulos das bibliografias e caracterização técnica oficial da biblioteca.</td>
                <td>Inserido o texto institucional completo do SiBI/IFSC (Res. 025/2018/CEPE), estrutura de 233,52 m², 90% de acervo físico + Minha Biblioteca, Sophia e atendimento 12h/dia.</td>
                <td style="text-align: center;"><span class="status-badge status-done">Concluído</span></td>
              </tr>
"""

html = html.replace('<tbody>\n', '<tbody>\n' + tr_28)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dashboard index.html atualizado para 28 itens com o apontamento da Biblioteca!")
