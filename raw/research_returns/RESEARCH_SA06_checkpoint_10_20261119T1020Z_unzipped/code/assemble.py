#!/usr/bin/env python3
"""Assemble independently maintained fragments; no mathematical inference."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
ALIASES = {'D_Tate1971':'Tate1971', 'D_Milne1994':'Milne1994',
           'cyJannsen1992':'Jannsen1992', 'D_Kisin2017':'Kisin2017',
           'D_LanglandsRapoport1987':'LanglandsRapoport1987'}
def clean_cites(text):
    def repl(m):
        return m.group(1)+','.join(ALIASES.get(k.strip(), k.strip()) for k in m.group(2).split(','))+m.group(3)
    return re.sub(r'(\\cite\w*(?:\[[^\]]*\]){0,2}\{)([^}]+)(\})',repl,text)
copies = {
    'agents/frobenius/part_B.tex': 'sections/B_frobenius.tex',
    'agents/frobenius/part_E2.tex': 'sections/E2_integrality.tex',
    'agents/cycles/cycles.tex': 'sections/C_cycles.tex',
    'agents/real_weil/part_D.tex': 'sections/D_real_weil.tex',
    'agents/real_weil/part_E456.tex': 'sections/E456_cohomology.tex',
}
for src, dst in copies.items():
    text = (ROOT / src).read_text()
    if 'D_real_weil' in dst:
        text = text.replace('\\section{Real fibre functors', '\\section{D. Real fibre functors')
    (ROOT / dst).write_text(clean_cites(text))
text = (ROOT/'agents/cycles/effectivity_albanese.tex').read_text()
at = text.index('\\subsection{E.3:')
(ROOT/'sections/E1_effectivity.tex').write_text(clean_cites(text[:at]))
(ROOT/'sections/E3_albanese.tex').write_text(clean_cites(text[at:]))
bibs = ([ROOT/'sources/root_references.bib'] + sorted((ROOT/'agents').glob('*/references.bib'))
        + sorted((ROOT/'agents').glob('*/*_references.bib')))
entries = {}
for path in bibs:
    if not path.exists(): continue
    for match in re.finditer(r'^@\w+\{([^,]+),[\s\S]*?(?=^@|\Z)',path.read_text(),re.M):
        key=match.group(1)
        if key in ALIASES: continue
        entry=match.group(0).strip().replace('of W^L(q) omitted','of $W^L(q)$ omitted')
        if not re.search(r'\byear\s*=',entry):
            body=entry[:-1].rstrip()
            entry=body+('' if body.endswith(',') else ',')+'\n  year = {n.d.},\n}'
        entries[key]=entry
(ROOT/'RESEARCH_SA06_references.bib').write_text('\n\n'.join(entries.values())+'\n')
print('Assembled', len(copies) + 2, 'fragments and',len(entries),'bibliographic entries.')
