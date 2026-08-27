# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_tr_23 = r"""              <tr>
                <td style="text-align: center; font-weight: 700;">23</td>
                <td><strong>Subitens 23, 24 e 25</strong><br><small style="color: var(--text-muted);">pp. 104–105</small></td>
                <td>Jacqueline Bastos</td>
                <td>Textos de atendimento ao discente, aproveitamento de estudos e avaliação resumidos.</td>
                <td>Restauração do texto completo institucional de Garopaba (Coordenadoria Pedagógica, PEDi, NAE/AEE, PAEVS e recuperação paralela).</td>
                <td style="text-align: center;"><span class="status-badge status-done">Concluído</span></td>
              </tr>"""

new_tr_23 = r"""              <tr>
                <td style="text-align: center; font-weight: 700;">23</td>
                <td><strong>Subitens 23, 24 e 25</strong><br><small style="color: var(--text-muted);">pp. 104–105</small></td>
                <td>Jacqueline Bastos</td>
                <td>Textos institucionais resumidos e constatação de que o subitem 25.1 não existe no formulário novo do CEPE.</td>
                <td>Restauração do texto completo institucional (Coordenadoria Pedagógica, PEDi, NAE/AEE, PAEVS, recuperação paralela) e eliminação da subdivisão 25.1, integrando a CPA ao corpo do Subitem 25.</td>
                <td style="text-align: center;"><span class="status-badge status-done">Concluído</span></td>
              </tr>"""

if old_tr_23 in html:
    html = html.replace(old_tr_23, new_tr_23)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dashboard index.html sincronizado com o ajuste do Item 23 / CEPE!")
