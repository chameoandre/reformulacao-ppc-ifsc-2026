import re
import sys

with open('tecnico-administracao/documento-ppc-principal/ementario_adm.tex.bak', 'r', encoding='utf-8') as f:
    orig_tex = f.read()

# Separate header/matrices from tables
pos_uc = orig_tex.find('\\subsection{Unidades curriculares:}')
header_part = orig_tex[:pos_uc + len('\\subsection{Unidades curriculares:}')]

print("Header part length:", len(header_part))
