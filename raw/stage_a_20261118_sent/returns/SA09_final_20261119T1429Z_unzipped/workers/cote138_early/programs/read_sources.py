from pathlib import Path
import re,sys,json
root=Path('/workspace/scratch/81b6665e34a6/source'); work=Path('/workspace/scratch/81b6665e34a6/SA09_work/workers/cote138_early')
pkg='MPL_138_001-045'
kind=sys.argv[1]; lo=int(sys.argv[2]);hi=int(sys.argv[3])
if kind=='notes':
 p=root/'SA09_notes/pro'/f'{pkg}_notes.md';s=p.read_text(); starts=list(re.finditer(r'^### ',s,re.M))
 for i,m in enumerate(starts,1):
  if lo<=i<=hi:
   end=starts[i].start() if i<len(starts) else len(s)
   print(f'ENTRY {pkg}#{i}; notes line {s[:m.start()].count(chr(10))+1}\n'+s[m.start():end])
elif kind=='text':
 p=root/'SA09_texts/pro'/f'{pkg}_transcription.tex';scan=0
 for n,l in enumerate(p.read_text().splitlines(),1):
  m=re.search(r'\\scanpage\{(\d+)\}',l)
  if m:scan=int(m[1])
  if lo<=scan<=hi: print(f'{n:04d} [s{scan:03d}] {l}')
elif kind=='doubts':
 p=root/'SA09_notes/pro'/f'{pkg}_doubts.md'
 for n,l in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n:04d} {l}')
