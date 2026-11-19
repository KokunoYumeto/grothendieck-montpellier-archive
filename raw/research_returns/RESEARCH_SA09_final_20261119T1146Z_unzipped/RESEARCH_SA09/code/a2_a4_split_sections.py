#!/usr/bin/env python3
"""One-time split of the completed A2/A4 proof fragment for manuscript order."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'sections/A2_A4.tex'
text=p.read_text()
marker='\\section{A.4. Strict boundedness, fibre ranks, and perfection}'
if marker not in text:
    print('Already split; no change.')
else:
    a2,a4=text.split(marker,1)
    (root/'sections/A2.tex').write_text(a2)
    (root/'sections/A4.tex').write_text(marker+a4)
    p.write_text('% Compatibility wrapper; assembly may input A2 and A4 separately.\n\\input{sections/A2.tex}\n\\input{sections/A4.tex}\n')
    print('Split A2.tex and A4.tex; kept a compatibility wrapper.')
