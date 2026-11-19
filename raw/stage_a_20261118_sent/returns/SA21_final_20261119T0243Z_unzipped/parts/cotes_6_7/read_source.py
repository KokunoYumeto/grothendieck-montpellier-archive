from pathlib import Path
import sys,datetime,json
root=Path('/workspace/scratch/4017236f14bf')
out=root/'SA21_work/parts/cotes_6_7';(out/'read_outputs').mkdir(exist_ok=True)
for name in sys.argv[1:]:
 p=root/'sources/texts/codex'/f'{name}_transcription.tex'
 lines=[]
 for n,l in enumerate(p.read_text().splitlines(),1):
  # The repeated hand-drawn crossed diamond denotes compatibility. Preserve all prose/formula content.
  marker=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]'
  while marker in l:
   a=l.index(marker); b=a+len(r'\mathrel'); depth=0; end=b
   for k in range(b,len(l)):
    if l[k]=='{':depth+=1
    elif l[k]=='}':
     depth-=1
     if depth==0:end=k+1;break
   l=l[:a]+r'\operatorname{Compat}'+l[end:]
  if l.strip():lines.append(f'{n}: {l}')
 t='FILE '+p.name+'\n'+'\n'.join(lines)
 (out/'read_outputs'/f'{name}.txt').write_text(t)
 print(t)
 with (out/'read_log.tsv').open('a') as f:f.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()}\t{name}\tcomplete text emitted with original line numbers\n')
