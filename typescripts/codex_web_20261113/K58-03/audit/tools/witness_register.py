"""Capture the individual witness decisions recorded after the freeze."""
from pathlib import Path
from collections import Counter
import csv,sys
p=Path('out');rr=list(csv.DictReader((p/'audit/frozen_places.tsv').open(),delimiter='\t'))
answers={}
for path in Path('work').glob('witness_*.txt'):
 n=int(path.stem.split('_')[-1])
 for line in path.read_text().splitlines():
  pos,reading,st,*tail=line.split('¦');new,ink=tail if len(tail)==2 else ('',tail[0])
  ident=f'{n}.{pos}';assert ident not in answers,(path,ident)
  answers[ident]=(st,reading,new,ink)
assert set(answers)=={r['id'] for r in rr}
fn=['scan','id','location','frozen reading','witness file','witness page','witness account','comparison crop','ink on reinspection','result','replacement or new alternatives']
words={'C':'changed','U':'unchanged','A':'alternative added','N':'uncovered'}
rows=[]
for r in rr:
 ident=r['id']; n=int(r['scan']);st,reading,new,ink=answers[ident]
 batch='batch-01' if n<=21 else 'batch-02';wp=n-1
 other=r['scan'].zfill(3)+'_w'+r['id'].split('.')[1]+'.png'
 used=other if (Path('crops')/other).exists() else r['crop']
 assert (Path('crops')/used).exists() and (st in ('C','A'))==bool(new),ident
 if st=='A':
  assert not set(new.split('|'))&set(r['frozen reading'].split('|')),ident
 if r['scan']=='22':assert st=='N'
 rows.append(dict(zip(fn,[n,ident,r['place'],r['frozen reading'],batch,wp,reading,used,ink,words[st],new])))
with (p/'audit/witness_places.tsv').open('w') as f:
 wr=csv.DictWriter(f,fieldnames=fn,delimiter='\t');wr.writeheader();wr.writerows(rows)
print(Counter(r['result'] for r in rows))
