from pathlib import Path
from datetime import datetime,timezone
import sys
root=Path('/workspace/scratch/4017236f14bf')
out=Path(__file__).parent
(out/'read_outputs').mkdir(exist_ok=True)
for name in sys.argv[1:]:
    blocks=[]
    for base,suffix in [('texts','transcription.tex'),('notes','notes.md')]:
        p=root/'sources'/base/'codex'/f'{name}_{suffix}'
        blocks.append('FILE '+p.name+'\n'+'\n'.join(f'{i}: {line}' for i,line in enumerate(p.read_text().splitlines(),1)))
    text='\n\n'.join(blocks)
    (out/'read_outputs'/f'{name}.txt').write_text(text+'\n')
    print(text)
    with (out/'read_log.tsv').open('a') as f:
        f.write(datetime.now(timezone.utc).isoformat()+'\t'+name+'\tcomplete transcription and short note emitted with original line numbers\n')
