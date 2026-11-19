from pathlib import Path
import sys,re,json,csv
base=Path('/workspace/scratch/a13eb9c84047')
mode=sys.argv[1]
if mode=='lines':
 p=base/sys.argv[2]; lo=int(sys.argv[3]); hi=int(sys.argv[4]); out='\n'.join(f'{i:5d}\t{x}' for i,x in enumerate(p.read_text().splitlines(),1) if lo<=i<=hi)
elif mode=='index':
 p=base/'source/SA03_notes/NOTES_INDEX.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'))
 out='\n'.join(f"{x['entry_id']}\t{x['heading']}" for x in rows if x['package']=='MPL_91_099-143')
elif mode=='scans':
 p=base/sys.argv[2]; lines=p.read_text().splitlines(); hits=[(i,x) for i,x in enumerate(lines,1) if '\\scanpage' in x];out='\n'.join(f'{i}\t{x}' for i,x in hits)
else: raise ValueError(mode)
print(out)
name='read_'+mode+'_'+'_'.join(re.sub('[^a-zA-Z0-9-]','_',s) for s in sys.argv[2:])+'.txt'
(base/'deliverable/parts/c/outputs'/name).write_text(out+'\n')
