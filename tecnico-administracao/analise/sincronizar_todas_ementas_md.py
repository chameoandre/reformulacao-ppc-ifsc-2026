import re

with open('tecnico-administracao/todas_ementas_administracao.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Make backup
with open('tecnico-administracao/todas_ementas_administracao.md.bak', 'w', encoding='utf-8') as f:
    f.write(text)

print("todas_ementas_administracao.md backed up.")
