"""Merge complete selected certificates, replacing two finite-seed deficits."""
from pathlib import Path
import csv,gzip,hashlib
HERE=Path(__file__).resolve().parent
FOLDER=HERE/'polarization_r6_parts'
def parse(path):
    it=iter(map(int,path.read_text().split()))
    head=tuple(next(it) for _ in range(6));r,L,b,blocks,p,np=head
    points=tuple(tuple(next(it) for _ in range(42)) for _ in range(np))
    data={}
    for _ in range(blocks):
        lam=tuple(next(it) for _ in range(6));m,rank=next(it),next(it)
        seeds=[tuple(next(it) for _ in range(64)) for _ in range(rank)]
        rows=tuple(next(it) for _ in range(rank))
        matrix=[tuple(next(it) for _ in range(rank)) for _ in range(rank)]
        d=next(it);data[lam]=(m,rank,seeds,rows,matrix,d)
    assert next(it,None) is None
    return head,points,data
def write(path,points,data):
    with path.open('w') as f:
        print(6,1,5,len(data),1000003,len(points),file=f)
        for point in points:print(*point,file=f)
        for lam,(m,rank,seeds,rows,matrix,d) in data.items():
            assert m==rank and d
            print(*lam,m,rank,file=f)
            for seed in seeds:print(*seed,file=f)
            print(*rows,file=f)
            for row in matrix:print(*row,file=f)
            print(d,file=f)
refined={};reference=None
for path in sorted(FOLDER.glob('refine*.selected')):
    _,points,data=parse(path)
    reference=points if reference is None else reference
    assert points==reference
    refined.update(data)
allblocks={}
for part in range(16):
    _,points,data=parse(FOLDER/f'part{part:02d}.selected');assert points==reference
    for lam in data:
        if lam in refined:data[lam]=refined[lam]
    write(FOLDER/f'audit{part:02d}.selected',points,data)
    assert not (allblocks.keys()&data.keys());allblocks.update(data)
source={tuple(map(int,r['partition'].split(','))):int(r['source_multiplicity'])
        for r in csv.DictReader((HERE/'POLARIZATION_R6_L1_B5_SOURCE.tsv').open(),delimiter='\t')}
assert source.keys()==allblocks.keys()
assert all(v[0]==v[1]==source[k] for k,v in allblocks.items())
path=HERE/'POLARIZATION_R6_L1_B5_SELECTED.compact'
write(path,reference,allblocks)
gzpath=Path(str(path)+'.gz')
with gzip.open(gzpath,'wb',compresslevel=9) as f:f.write(path.read_bytes())
print('blocks',len(allblocks),'vectors',sum(v[0] for v in allblocks.values()),
      'entries',sum(v[0]**2 for v in allblocks.values()),
      'compressed_bytes',gzpath.stat().st_size,'SHA256',hashlib.sha256(gzpath.read_bytes()).hexdigest())
