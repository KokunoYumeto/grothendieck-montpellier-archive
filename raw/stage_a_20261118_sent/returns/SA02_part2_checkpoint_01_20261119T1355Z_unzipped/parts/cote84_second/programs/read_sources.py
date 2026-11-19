from pathlib import Path
import re, argparse, json
R=Path('/workspace/scratch/95cd10054c54')
W=R/'SA02_work/parts/cote84_second'
p=argparse.ArgumentParser(); p.add_argument('--entries'); p.add_argument('--scans'); p.add_argument('--codex'); p.add_argument('--inventory',action='store_true'); p.add_argument('--label',required=True); a=p.parse_args()
out=[]
def emit(s):out.append(str(s))
notes=R/'source/SA02_notes/pro/MPL_84_146-193_notes.md'
ls=notes.read_text().splitlines()
starts=[i for i,l in enumerate(ls) if l.startswith('### ')]+[len(ls)]
if a.inventory:
 for n,(s,e) in enumerate(zip(starts,starts[1:]),1):emit(f'{n}\t{s+1}-{e}\t{ls[s]}')
if a.entries:
 lo,hi=map(int,a.entries.split('-'))
 for n in range(lo,hi+1):
  s,e=starts[n-1:n+1];emit(f'ENTRY #{n}')
  for i in range(s,e):emit(f'N{i+1:04d}: {ls[i]}')
if a.scans:
 want=set(map(int,a.scans.split(',')))
 f=R/'source/SA02_texts/pro/MPL_84_146-193_transcription.tex';ls=f.read_text().splitlines();scan=None
 emit('TRANSCRIPTION: '+f.name)
 for i,l in enumerate(ls):
  m=re.search(r'\\scanpage\{(\d+)\}',l)
  if m:scan=int(m[1])
  if scan in want:emit(f'T{i+1:04d}: {l}')
if a.codex:
 for k in a.codex.split(','):
  f=R/f'source/SA02_notes/codex/{k}_notes.md';emit(f.name);emit(f.read_text())
s='\n'.join(out)+'\n';(W/'outputs'/f'{a.label}.txt').write_text(s);print(s)
