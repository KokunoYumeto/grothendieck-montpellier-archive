"""Emit complete cross-reference target scans with original line locators.
Run: python source_checks.py > source_checks.txt
These excerpts support endpoint checks, not a claim to read other agents' whole corpora.
"""
from pathlib import Path
import re
ROOT=Path('/workspace/scratch/4017236f14bf/sources/texts/codex')
TARGETS={
 'J156-9-04':[31,32], 'J156-9-12':[90], 'J156-9-13':[104],
 'J156-8-09':[71], 'J156-8-10':[79,80], 'J156-8-11':[83,86,87],
 'J156-8-07':[55,56], 'J156-8-05':[36,37],
}
for stem,targets in TARGETS.items():
    print('\n### '+stem)
    selected=False
    for n,line in enumerate((ROOT/(stem+'_transcription.tex')).read_text().splitlines(),1):
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m:selected=int(m.group(1)) in targets
        if selected:print(f'{n:4d} {line}')
