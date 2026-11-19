from pathlib import Path
import sys,re,json,datetime
base=Path('/workspace/scratch/4017236f14bf')
out=Path(__file__).resolve().parents[1]/'outputs';out.mkdir(parents=True,exist_ok=True)
for folder in sys.argv[1:]:
 blocks=[]
 for kind,suffix in [('texts','transcription.tex'),('notes','notes.md')]:
  p=base/'sources'/kind/'codex'/f'{folder}_{suffix}';lines=p.read_text().splitlines();scan='?'
  blocks.append(f'FILE {p.name} ({len(lines)} lines)')
  for i,line in enumerate(lines,1):
   m=re.search(r'\\scanpage\{([^}]+)\}',line)
   if m:scan=m.group(1)
   blocks.append(f'{i:04d} [s{scan}] {line}')
 text='\n'.join(blocks);(out/f'{folder}_read.txt').write_text(text);print(text)
