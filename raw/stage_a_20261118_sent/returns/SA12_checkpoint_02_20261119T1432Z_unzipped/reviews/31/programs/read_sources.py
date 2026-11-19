from pathlib import Path
import re,sys,datetime
root=Path('/workspace/scratch/a77a578fa7d4/source')
out=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31')
mode=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); source=sys.argv[4] if len(sys.argv)>4 else 'MPL_31_002-051'
if mode=='notes':
 s=(root/f'SA12_notes/pro/{source}_notes.md').read_text(); entries=re.split(r'^### ',s,flags=re.M)[1:]; parts=[]
 for n,e in enumerate(entries,1):
  if a<=n<=b:
   # Only repeated contextual-search boilerplate is omitted in this reading view; later context view retains it.
   core=e.split('**Context comparison:**')[0]
   after=e[e.find('**Checked primary comparison:'): ] if '**Checked primary comparison:' in e else ''
   # calculations can occur after contexts, preserve all paragraphs not boilerplate
   if '**Context comparison:**' in e:
    tail=e.split('**Context comparison:**',1)[1]
    tail=re.sub(r'\*\*Context search.*?(?=\*\*|\Z)','',tail,flags=re.S)
    core += '\nCONTEXT AND REMAINDER:\n'+tail
   parts.append(f'ENTRY {n}: '+core)
 result='\n\n'.join(parts)
elif mode=='tex':
 folder='pro' if source.startswith('MPL_') else 'codex'
 ls=(root/f'SA12_texts/{folder}/{source}_transcription.tex').read_text().splitlines()
 result='\n'.join(f'{i}: {l}' for i,l in enumerate(ls,1) if a<=i<=b)
elif mode=='doubts':
 ls=(root/f'SA12_notes/pro/{source}_doubts.md').read_text().splitlines(); result='\n'.join(f'{i}: {l}' for i,l in enumerate(ls,1) if a<=i<=b)
else: raise ValueError(mode)
f=out/'outputs'/f'{mode}_{source}_{a:04}_{b:04}.txt'; f.write_text(result)
with (out/'read_log.tsv').open('a') as log: log.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()}\t{mode}\t{source}\t{a}-{b}\t{f.relative_to(out)}\n')
print(result)
