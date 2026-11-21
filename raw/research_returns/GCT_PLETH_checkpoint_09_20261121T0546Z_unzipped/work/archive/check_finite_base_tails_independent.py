"""R032: finite kernels from the independent arrangement character, then all tails."""
from pathlib import Path
from itertools import combinations_with_replacement
import csv,json,hashlib
HERE=Path(__file__).resolve().parent
source=HERE/"check_outer5_canonical_independent.py"
ns={"__file__":str(source)}
exec(compile(source.read_text().split('path=HERE.parent/')[0],str(source),"exec"),ns)
coefficient=ns['coefficient'];partitions=ns['partitions']
BASES={t:[] for t in range(1,6)};tested=0
for t in range(1,5):
    for lam in partitions(5*t):
        if len(lam)>5:continue
        lam=lam+(0,)*(5-len(lam))
        if lam[1]>t:continue
        kernel=coefficient(5,t,lam)-coefficient(t,5,lam)
        tested+=1
        assert kernel>=0
        if kernel:BASES[t].append((lam,kernel))
# All eight square-map summands, from the previously checked primary CIM theorem.
SQUARE=((14,7,2,2,0),(13,7,2,2,1),(12,7,3,2,1),(12,6,3,2,2),
        (12,5,4,3,1),(11,5,4,4,1),(10,8,4,2,1),(9,7,6,3,0))
BASES[5]=[(lam,1) for lam in SQUARE if lam[1]<=5]
targetpath=HERE.parent/'rectangular/FINITE_BASE_KERNELS.tsv'
with targetpath.open(newline='') as f:target=list(csv.DictReader(f,delimiter='\t'))
expected={(int(r['t']),tuple(map(int,r['partition'].split(','))),int(r['kernel_multiplicity'])) for r in target}
computed={(t,lam,k) for t,rows in BASES.items() for lam,k in rows}
assert computed==expected and len(expected)==28
assert [len(BASES[t]) for t in range(1,6)]==[0,3,4,19,2]
MINIMAL={};tailchecks=[];longchecks=0
for t in range(1,6):
    tails=set(lam[1:] for lam,k in BASES[t])
    mins=sorted(tail for tail in tails if not any(other!=tail and all(x<=y for x,y in zip(other,tail)) for other in tails))
    MINIMAL[t]=mins
    for tail0 in combinations_with_replacement(range(t+1),4):
        tail=tuple(reversed(tail0))
        contained=any(all(x<=y for x,y in zip(mu,tail)) for mu in tails)
        q=1+sum(x>=2 for x in tail)
        safe=tail[0]+q<=t+2 if t<=4 else (tail[0]<=4 or tail[1]<=3 or tail[2]<=2 or tail[3]==0)
        assert safe==(not contained)
        tailchecks.append((t,tail,safe))
    # The criterion uses the complete column height, including rows past five.
    for length in range(5,9):
        for raw in combinations_with_replacement(range(t+1),length):
            tail=tuple(reversed(raw))
            contained=any(all(x<=y for x,y in zip(mu,tail)) for mu in tails)
            q=1+sum(x>=2 for x in tail)
            safe=tail[0]+q<=t+2 if t<=4 else (tail[0]<=4 or tail[1]<=3 or tail[2]<=2 or tail[3]==0)
            assert safe==(not contained)
            longchecks+=1
assert len(tailchecks)==251
assert MINIMAL=={1:[],2:[(2,2,0,0)],3:[(2,2,2,0),(3,2,0,0)],
 4:[(2,2,2,2),(3,2,2,0),(4,2,0,0)],5:[(5,4,3,1)]}
def strip(mu,lam,n):
    size=max(len(mu),len(lam));mu=mu+(0,)*(size+1-len(mu));lam=lam+(0,)*(size+1-len(lam))
    return sum(lam)-sum(mu)==n and all(lam[i]>=mu[i]>=lam[i+1] for i in range(size))
padding_example=((2,2,2,2,2),(25,2,2,2,2,2),(30,2,2,2,2,2,2))
assert strip(padding_example[0],padding_example[1],25) and strip(padding_example[1],padding_example[2],7)
receipt=dict(statement='R032 complete finite kernel tails',status='PASS',
 independently_evaluated_lower_band_partitions=tested,kernel_rows=28,
 counts=[len(BASES[t]) for t in range(1,6)],minimal_tails=MINIMAL,
 four_coordinate_tail_comparisons=len(tailchecks),longer_tail_comparisons=longchecks,
 method='selected-subset arrangement characters independently recomputed for every second-row band at t1..4; t5 uses the previously checked exact eight CIM kernel types; antichain extraction and full column-height comparisons',
 input_sha256=hashlib.sha256(targetpath.read_bytes()).hexdigest(),
 values_sha256=hashlib.sha256(json.dumps(sorted(computed),separators=(',',':')).encode()).hexdigest(),
 row_padding_correction_example=padding_example)
(HERE/'FINITE_BASE_TAILS_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
