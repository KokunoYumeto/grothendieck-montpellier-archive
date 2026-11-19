"""Repair a literal underscore in the accessed-source bibliography note."""
from pathlib import Path
w=Path(__file__).resolve().parents[1]
p=w/'agents/monodromy/references.bib'
s=p.read_text()
s=s.replace('parent ROOT_SEARCH_LOG11','parent root search log 11')
p.write_text(s)
print('Bibliography path typography repaired; failed-build output retained.')
