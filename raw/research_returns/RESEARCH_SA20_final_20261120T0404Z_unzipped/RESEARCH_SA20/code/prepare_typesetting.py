#!/usr/bin/env python3
"""Apply reversible common-wrapper and line-break edits before compiling."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
for rel in ('agents/tensor_and_finite/part_B.tex',
            'agents/tensor_and_finite/part_E.tex',
            'agents/singularities_duality/part_C.tex',
            'agents/lie_theory/part_D.tex'):
    p=root/rel
    s=p.read_text()
    s=re.sub(r'\A(\s*)\\section\{[^\n]*\}\n', r'\1', s, count=1)
    p.write_text(s)
    print('Used common section heading:',rel)
p=root/'agents/lie_theory/part_A5.tex'
s=p.read_text().replace(r'\texttt{code/A5\_mapping\_cylinder.py}',
                       r'\path{code/A5_mapping_cylinder.py}')
s=s.replace(r'\texttt{logs/A5\_mapping\_cylinder.json}',
            r'\path{logs/A5_mapping_cylinder.json}')
p.write_text(s)
print('Allowed breaks in A5 program paths.')
