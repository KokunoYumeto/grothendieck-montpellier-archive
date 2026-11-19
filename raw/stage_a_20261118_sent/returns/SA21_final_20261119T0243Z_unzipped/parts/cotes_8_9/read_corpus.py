from pathlib import Path
import sys, datetime, json
ROOT=Path('/workspace/scratch/4017236f14bf')
OUT=ROOT/'SA21_work/parts/cotes_8_9'
(OUT/'read_outputs').mkdir(exist_ok=True)
chunks=[]
for folder in sys.argv[1:]:
    for kind,suffix in [('notes','notes.md'),('texts','transcription.tex')]:
        p=ROOT/'sources'/kind/'codex'/f'{folder}_{suffix}'
        chunks.append(f'FILE {p.relative_to(ROOT)}\n'+''.join(f'{i:04d} {line}\n' for i,line in enumerate(p.read_text().splitlines(),1)))
text='\n'.join(chunks)
name='__'.join(sys.argv[1:])+'.txt'
(OUT/'read_outputs'/name).write_text(text)
with (OUT/'operations.jsonl').open('a') as f:
    f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'program':'read_corpus.py','argv':sys.argv[1:],'output':'read_outputs/'+name})+'\n')
print(text)
