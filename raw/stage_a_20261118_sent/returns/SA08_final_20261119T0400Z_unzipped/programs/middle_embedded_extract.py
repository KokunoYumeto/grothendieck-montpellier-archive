"""Extract explicitly delimited embedded notes for a human coverage audit.
This program makes no mathematical verdicts and does not assign item IDs.
"""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
p=root/'sources/notes/pro/MPL_136_095-141_notes.md'
rows=p.read_text().splitlines();starts=[i for i,l in enumerate(rows) if re.match(r'^#### [NROL]\d{2} ',l)]
out=[]
for a,z in zip(starts,starts[1:]+[len(rows)]):
 block='\n'.join(rows[a:z]);math=block.split('**Context:**')[0].split('## 6.')[0]
 out.append({'embedded_id':rows[a].split()[1],'notes_lines':f'{a+1}-{z}','heading':rows[a],'text':math.strip()})
dest=root/'work/middle/embedded_source.json';dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Extracted {len(out)} embedded notes, without verdicts: {dest}')
(root/'work/middle/embedded_read.txt').write_text('\n\n'.join(f"{x['embedded_id']} notes lines{x['notes_lines']}\n{x['text']}" for x in out)+'\n')
