import sys
import os
import re

def escape_latex(s):
    # Do not double escape already formatted LaTeX
    return s

def format_abnt_ref(ref_str):
    # Apply ABNT bolding rule: bold only the main title up to the colon
    # Example: KOTLER, Philip; KELLER, Kevin Lane. **Administração de marketing**. 15. ed.
    # -> KOTLER, Philip; KELLER, Kevin Lane. \textbf{Administração de marketing}. 15. ed.
    pass

print("Script template ready")
