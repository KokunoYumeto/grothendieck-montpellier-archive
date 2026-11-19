"""Display manually selected passages for an audit of claim quotations."""
from pathlib import Path
import json, datetime
root=Path(__file__).resolve().parents[2]
requests={'A57-01':[(70,100),(162,208)],'K57-01':[(160,205)],'K57-03':[(24,40),(62,70),(355,368)],'K57-04':[(120,150)],'K57-07':[(95,155),(192,240)],'K57-09':[(22,38),(97,110),(423,442)],'K57-10':[(38,52),(76,107)]}
out=[]
for a,ranges in requests.items():
    lines=(root/f'sources/SA14_texts/codex/{a}_transcription.tex').read_text().splitlines()
    for start,end in ranges:
        end=min(end,len(lines))
        out.append(f'\n### {a}:{start}-{end}')
        out.extend(f'{i}: {lines[i-1]}' for i in range(start,end+1))
s='\n'.join(out)+'\n'
(root/'SA14_work/outputs/root_quote_audit_001.txt').write_text(s)
with (root/'SA14_work/research/read_events.jsonl').open('a') as f:
    f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reader':'root','event':'Manual quote-locator audit, not generated judgments','ranges':requests})+'\n')
print(s)
