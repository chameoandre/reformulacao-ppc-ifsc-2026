# Padrão Oficial de Estrutura e Nomenclatura das Seções do PPC (IFSC)

Este documento documenta a hierarquia oficial, nomenclatura exata de seções e subitens e as diretrizes conceituais estabelecidas pela **Resolução CONSUP/IFSC nº 142/2025** e pelo modelo institucional do IFSC (Google Docs / Formulário oficial de PPC Técnico), assegurando 100% de conformidade com os modelos exigidos pela CEPE/DEPE para todos os cursos técnicos integrados.

---

## 🏛️ Estrutura Canônica (Seções Romanas I a X e Subitens 1 a 30)

```
I – DADOS DA INSTITUIÇÃO
II – DADOS DO CÂMPUS PROPONENTE
    1. Câmpus:
    2. Endereço e Telefone do Câmpus:
III – DADOS DOS RESPONSÁVEIS PELO PPC
    3. Chefia DEPE/ Departamento:
    4. Coordenador do curso/proponente:
    5. Equipe elaboradora do projeto de curso:
    6. Aprovação no Câmpus:
IV – DADOS DO CURSO
    7. Dados do Curso: (Tabela oficial com itens 7.1 a 7.6.4)
    8. Dados da Oferta: (Tabela oficial com itens 8.1 a 8.10)
    9. Requisito de Acesso:
    10. Legislação (profissional e educacional) aplicada ao curso:
    11. Justificativa da Oferta do Curso no Câmpus: (Diagnóstico socioeconômico regional e contextualização)
    12. Público-alvo:
    13. Objetivo do curso:
        13.1. Objetivo Geral:
        13.2. Objetivos Específicos:
    14. Perfil profissional do egresso: (Conforme CNCT 4ª edição)
    15. Outras características gerais do egresso: (Competências socioemocionais, éticas e sustentabilidade)
    16. Áreas/campo de atuação do egresso:
V – ESTRUTURA CURRICULAR DO CURSO
    17. Metodologia de desenvolvimento pedagógico do curso: (Pedagogia Histórico-Crítica, Ciclos Temáticos e Oficinas)
    18. Matriz curricular:
        18.1. Matriz Curricular Resumida (Distribuição por Blocos - Res. 142/2025):
        18.2. Matriz Curricular Detalhada por Anos e Blocos:
    19. Unidades curriculares: (Ementário visual em tabelas xltabular com 45 UCs)
    20. Estágio curricular supervisionado: (Não obrigatório, conforme RDP)
    21. Atividade em EaD: (Matriz presencial com faculdade regulamentar de até 10% no AVA Moodle via RDP)
    22. Certificações intermediárias:
    23. Atendimento e acompanhamento ao discente: (Coordenadoria Pedagógica, PEDi, NAE/NAPNE, AEE e PAEVS)
    24. Critérios de aproveitamento de conhecimentos e experiências anteriores: (Validação regimental via RDP e bancas)
VI – AVALIAÇÃO
    25. Avaliação do processo de ensino e aprendizagem: (Avaliação formativa, prazo de 15 dias e recuperação paralela)
        25.1. Autoavaliação do Curso e Atuação da CPA:
VII – INFRAESTRUTURA E ACESSIBILIDADE
    26. Instalações e Equipamentos:
    27. Biblioteca: (Normativas de acervos digitais, Pearson/Minha Biblioteca e Target GEDWeb)
VIII – CORPO DOCENTE E TUTORIAL
    28. Corpo docente e técnico do curso:
        28.1. Corpo Docente:
        28.2. Corpo Técnico-Administrativo:
IX – REFERÊNCIAS
    29. Referências:
X – ANEXOS
    30. Anexos:
```

---

## 📋 Diretrizes Conceituais Obrigatórias (Resolução CONSUP 142/2025)

1. **Subitem 11 (Justificativa Regional):**
   - Deve apresentar dados socioeconômicos consolidados da microrregião de abrangência do Câmpus (população, IDH, PIBM/IBGE), setores econômicos predominantes (serviços, comércio, turismo, pesca, indústria) e justificativa da demanda por formação técnica.
2. **Subitem 15 (Outras Características do Egresso):**
   - Deve cobrir as 9 dimensões formativas: responsabilidade socioambiental, ética, pensamento crítico, comunicação, integridade e segurança digital, trabalho em equipe e compreensão do mundo do trabalho.
3. **Subitem 17 (Metodologia Pedagógica):**
   - Fundamentação na **Pedagogia Histórico-Crítica** (*Saviani, 2020*), concepção de **omnilateralidade** e formação humana integral.
   - Metodologia de **Ciclos Temáticos** (*Silva, 2016*) para as *Oficinas de Integração I e II* do Núcleo Politécnico Comum (problematização, instrumentalização, experimentação, orientação, sistematização e socialização).
   - Diretrizes de saídas de campo, visitas técnicas e transporte oficial do câmpus.
4. **Subitem 21 (Atividade em EaD):**
   - Registro de curso presencial (0h fixa na matriz), ressalvando a faculdade regulamentar de até 10% da carga horária em atividades mediadas por tecnologia (AVA Moodle) nos termos do RDP.
5. **Subitens 23 e 24 (Atendimento e Aproveitamento):**
   - Atuação da equipe multidisciplinar da Coordenadoria Pedagógica;
   - Concessão de **PEDi** (Plano de Estudo Diferenciado - Art. 18 do RDP e Nota Técnica CEPE 01/2016);
   - Inclusão via **NAE / NAPNE** e Atendimento Educacional Especializado (**AEE**);
   - Políticas de permanência via **PAEVS / PAE**;
   - Validação de saberes e aproveitamento de estudos via bancas examinadoras conforme o RDP.
6. **Subitem 25 (Avaliação da Aprendizagem):**
   - Avaliação processual e formativa;
   - Prazo regimental máximo de 15 dias letivos para devolução e análise dos instrumentos avaliativos;
   - Garantia de **recuperação paralela de estudos (Art. 98 do RDP)** e direito a segunda chamada (Art. 97).

---

## ⚙️ Implementação Técnica no LaTeX (`ifsc-ppc.cls`)

- As seções macro utilizam `\section{...}` e são formatadas com numeração romana (`I --`, `II --`, ..., `X --`).
- Os subitens utilizam `\subsection{...}` com contador contínuo `\thesubsection` (sem reinicialização por seção), gerando automaticamente a numeração linear `1.` a `30.`.
- As subdivisões de 3º nível utilizam `\subsubsection{...}` gerando numeração dependente `\thesubsection.\arabic{subsubsection}.` (ex.: `13.1.`, `18.1.`, `28.1.`).
