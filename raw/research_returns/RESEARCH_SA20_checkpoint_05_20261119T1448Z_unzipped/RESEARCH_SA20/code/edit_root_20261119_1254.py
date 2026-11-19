#!/usr/bin/env python3
"""Record the root-only manuscript ordering and typesetting edits."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = root/'parts/axioms.tex'
s = p.read_text()
start = s.index(r'\subsection{The all-arity repair and the compact open core}')
end = s.index(r'\begin{saresult}{A.302}', start) if r'\begin{saresult}{A.302}' in s[start:] else -1
if end >= 0:
    block = s[start:end]
    s = s[:start]+s[end:]
    s = s.rstrip()+'\n\n'+block.rstrip()+'\n'
p.write_text(s)
p = root/'parts/collars.tex'
s = p.read_text().replace('maps,+proving', 'maps,\nproving')
p.write_text(s)
print('Ordered A.301--307; repaired the A.113 prose line break.')
