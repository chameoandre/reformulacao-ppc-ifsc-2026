import re
import os

def update_ementario():
    with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex', 'r', encoding='utf-8') as f:
        tex = f.read()

    # We will replace tables or specific sections in tex with high fidelity
    
    # 1. TABELA 1: Artes — Ano 1 (Bibliografias ajustadas)
    # 2. TABELA 2: Educação Física — Ano 1 (17 objetivos literais, conteúdos com idade, estratégias literais)
    # 3. TABELA 3: Inglês — Ano 1 (remover avaliação inventada)
    # 4. TABELA 4: Língua Portuguesa — Ano 1 (introdução à literatura, bibliografia)
    # 5. TABELA 5: Espanhol — Ano 1 (temáticas transversais)
    # 6. TABELA 6: Biologia — Ano 1 (12 conteúdos, metodologia completa)
    # 7. TABELA 7: Física — Ano 1 (objetivos e metodologia com recursos)
    # 8. TABELA 8: Matemática — Ano 1 (conteúdos completos, remover LIMA espúrio)
    # 9. TABELA 9: Química — Ano 1 (objetivos completos, metodologia/critérios)
    # 10. TABELA 10: Filosofia — Ano 1 (remover LIMA espúrio de matemática, metodologia/avaliação)
    # 11. TABELA 11: Geografia — Ano 1 (preservada conforme instrução)
    # 12. TABELA 12: Sociologia — Ano 1 (metodologia completa)
    # 13. TABELA 13: Introdução à Administração (metodologia e articulação)
    # 14. TABELA 14: Sociedade e Trabalho (textos da fonte)
    # 15. TABELA 15: Gestão de Marketing I (SUBSTITUIÇÃO INTEGRAL)
    # 16. TABELA 16: Organização e Processos (textos da fonte)
    # 17. TABELA 17: Informática Aplicada (textos da fonte)
    # 18. TABELA 18: Artes — Ano 2 (bibliografias)
    # 19. TABELA 19: Educação Física — Ano 2 (19 objetivos literais, metodologias)
    # 20. TABELA 20: Inglês — Ano 2 (remover avaliação inventada)
    # 21. TABELA 21: Língua Portuguesa — Ano 2
    # 22. TABELA 22: Espanhol — Ano 2 (seguir bloco 3 Felix Medina)
    # 23. TABELA 23: Física — Ano 2 (objetivos e metodologia)
    # 24. TABELA 24: Matemática — Ano 2 (conteúdos completos, remover LIMA espúrio)
    # 25. TABELA 25: Química — Ano 2 (objetivos completos)
    # 26. TABELA 26: História — Ano 2
    # 27. TABELA 27: Sociologia — Ano 2 (metodologia completa)
    # 28. TABELA 28: Matemática para Administração
    # 29. TABELA 29: Gestão de Marketing II (SUBSTITUIÇÃO INTEGRAL)
    # 30. TABELA 30: Gestão de Operações e Qualidade
    # 31. TABELA 31: Empreendedorismo I (SUBSTITUIÇÃO INTEGRAL)
    # 32. TABELA 32: Responsabilidade Socioambiental e Sustentabilidade
    # 33. TABELA 33: Oficina de Integração I
    # 34. TABELA 34: Língua Portuguesa — Ano 3
    # 35. TABELA 35: Biologia — Ano 3 (metodologia completa)
    # 36. TABELA 36: Física — Ano 3 (objetivos e metodologia)
    # 37. TABELA 37: Matemática — Ano 3 (conteúdos completos, remover LIMA espúrio)
    # 38. TABELA 38: Química — Ano 3 (objetivos completos)
    # 39. TABELA 39: Filosofia — Ano 3 (remover LIMA espúrio)
    # 40. TABELA 40: Geografia — Ano 3 (preservada conforme instrução)
    # 41. TABELA 41: História — Ano 3
    # 42. TABELA 42: Empreendedorismo II
    # 43. TABELA 43: Gestão de Pessoas e Relações no Trabalho
    # 44. TABELA 44: Gestão Financeira (SUBSTITUIÇÃO INTEGRAL - 5º e 6º sem, 80h)
    # 45. TABELA 45: Oficina de Integração II

    print("Framework ready")

update_ementario()
