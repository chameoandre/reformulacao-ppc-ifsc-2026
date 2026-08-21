# Padrão Oficial de Estrutura e Nomenclatura das Seções do PPC (IFSC)

Este documento documenta a hierarquia oficial e nomenclatura exata de seções e subitens estabelecida pelo modelo institucional do IFSC (Google Docs / Formulário oficial de PPC Técnico), assegurando 100% de conformidade com os modelos exigidos pela CEPE/DEPE.

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
    11. Justificativa da Oferta do Curso no Câmpus:
    12. Público-alvo:
    13. Objetivo do curso:
        13.1. Objetivo Geral:
        13.2. Objetivos Específicos:
    14. Perfil profissional do egresso:
    15. Outras características gerais do egresso:
    16. Áreas/campo de atuação do egresso:
V – ESTRUTURA CURRICULAR DO CURSO
    17. Metodologia de desenvolvimento pedagógico do curso:
    18. Matriz curricular:
        18.1. Matriz Curricular Resumida (Distribuição por Blocos):
        18.2. Matriz Curricular Detalhada por Anos e Blocos:
    19. Unidades curriculares: (Ementário visual em tabelas xltabular)
    20. Estágio curricular supervisionado:
    21. Atividade em EaD:
    22. Certificações intermediárias:
    23. Atendimento e acompanhamento ao discente:
    24. Critérios de aproveitamento de conhecimentos e experiências anteriores:
VI – AVALIAÇÃO
    25. Avaliação do processo de ensino e aprendizagem:
        25.1. Autoavaliação do Curso e Atuação da CPA:
VII – INFRAESTRUTURA E ACESSIBILIDADE
    26. Instalações e Equipamentos:
    27. Biblioteca:
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

## ⚙️ Implementação Técnica no LaTeX (`ifsc-ppc.cls`)

- As seções macro utilizam `\section{...}` e são formatadas com numeração romana (`I --`, `II --`, ..., `X --`).
- Os subitens utilizam `\subsection{...}` com contador contínuo `\thesubsection` (sem reinicialização por seção), gerando automaticamente a numeração linear `1.` a `30.`.
- As subdivisões de 3º nível utilizam `\subsubsection{...}` gerando numeração dependente `\thesubsection.\arabic{subsubsection}.` (ex.: `13.1.`, `18.1.`, `28.1.`).
