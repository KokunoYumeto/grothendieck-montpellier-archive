"""Locator bookkeeping only: no model verdicts or proof checks are generated."""
from pathlib import Path
import re,json
HERE=Path(__file__).parent
SOURCE=HERE.parents[2]/'sources'/'texts'/'codex'
if not SOURCE.exists(): SOURCE=Path('/workspace/scratch/4017236f14bf/sources/texts/codex')
folders=[f'J156-8-{i:02d}' for i in range(1,17)]+[f'J156-9-{i:02d}' for i in range(1,9)]
pages={};cross=[]
for folder in folders:
    lines=(SOURCE/(folder+'_transcription.tex')).read_text().splitlines()
    starts=[(i+1,int(m.group(1))) for i,line in enumerate(lines) for m in [re.search(r'\\scanpage\{(\d+)\}',line)] if m]
    for j,(start,scan) in enumerate(starts):
        end=starts[j+1][0]-1 if j+1<len(starts) else len(lines)
        pages[f'{folder.split("-")[1]}:{scan}']={'file':folder,'start':start,'end':end}
    for i,line in enumerate(lines,1):
        if re.search(r'\b(?:cf|Cf|Comparer|CF|loc\.\s*cit)|pages?\s+\\unsure|p\.\s*[~ ]?\d',line) and not line.lstrip().startswith('%'):
            scan=max((s for start,s in starts if start<=i),default=None)
            cross.append(f'{folder} scan{scan} line{i}: {line}')
(HERE/'scan_locator_map.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
(HERE/'crossref_inventory.txt').write_text('\n'.join(cross)+'\n')
print(f'{len(folders)} folders; {len(pages)} scan markers; {len(cross)} cross-reference candidate lines. Manual review required.')
