from pathlib import Path
import argparse,re,json,datetime
ROOT=Path('/workspace/scratch/95cd10054c54')
PART=ROOT/'SA02_work/parts/cote84_first'
p=argparse.ArgumentParser();p.add_argument('--entries');p.add_argument('--scans');p.add_argument('--codex');p.add_argument('--doubts',action='store_true');p.add_argument('--out',required=True);a=p.parse_args()
out=[]
def emit(s):out.append(s)
if a.entries:
 f=ROOT/'source/SA02_notes/pro/MPL_84_097-145_notes.md';ls=f.read_text().splitlines();hs=[i for i,s in enumerate(ls) if s.startswith('### ')]+[len(ls)];lo,hi=map(int,a.entries.split(':'))
 for n in range(lo,hi+1):
  emit(f'ENTRY {n}, {f.name}, lines {hs[n-1]+1}-{hs[n]}')
  emit('\n'.join(f'{i+1}: {ls[i]}' for i in range(hs[n-1],hs[n])))
if a.scans or a.codex:
 f=ROOT/'source/SA02_texts/pro/MPL_84_097-145_transcription.tex'
 if a.codex:f=ROOT/f'source/SA02_texts/codex/{a.codex}_transcription.tex'
 ls=f.read_text().splitlines();heads=[(i,int(re.search(r'\\scanpage\{(\d+)\}',s).group(1))) for i,s in enumerate(ls) if re.search(r'\\scanpage\{(\d+)\}',s)];heads.append((len(ls),-1))
 want=set(map(int,a.scans.split(','))) if a.scans else {x[1] for x in heads}
 for k,(start,n) in enumerate(heads[:-1]):
  if n in want:emit(f'SOURCE {f.name} SCAN {n}\n'+'\n'.join(f'{i+1}: {ls[i]}' for i in range(start,heads[k+1][0])))
if a.doubts:
 f=ROOT/'source/SA02_notes/pro/MPL_84_097-145_doubts.md';emit(f.read_text())
s='\n\n'.join(out);(PART/'outputs'/a.out).write_text(s);print(s)
with (PART/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' READ '+str(vars(a))+'\n')
