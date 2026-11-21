"""Small deterministic lists of Reynolds seeds for r6,L1,b5."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from random import Random
import csv

HERE=Path(__file__).resolve().parent
R,B=6,5
MINORS=[I for h in range(1,R+1) for I in combinations(range(R),h)]
INDEX={I:i for i,I in enumerate(MINORS)}

@lru_cache(None)
def predecessors(lam,j):
    target=(j-1)*B;out=[]
    def visit(i,left,mu):
        if i==R:
            if left==0:out.append(tuple(mu))
            return
        low=lam[i+1] if i+1<R else 0
        high=lam[i]
        if i>=j-1:high=0
        if low>high:return
        for v in range(min(high,left),low-1,-1):
            visit(i+1,left-v,mu+[v])
    visit(0,target,[])
    return tuple(out)

@lru_cache(None)
def number(lam,j):
    if j==0:return int(not any(lam))
    return sum(number(mu,j-1) for mu in predecessors(lam,j))

def seed_at(lam,index):
    shapes=[None]*(R+1);shapes[R]=lam
    for j in range(R,0,-1):
        for mu in predecessors(shapes[j],j):
            k=number(mu,j-1)
            if index>=k:index-=k
            else:shapes[j-1]=mu;break
        else:raise AssertionError('index overflow')
    assert index==0
    rows=[]
    for i in range(R):
        row=[]
        for j in range(1,R+1):row += [j-1]*(shapes[j][i]-shapes[j-1][i])
        rows.append(row)
    counts=[0]*len(MINORS)
    for col in range(lam[0]):
        I=tuple(rows[i][col] for i in range(R) if col<len(rows[i]))
        assert I==tuple(sorted(set(I)))
        counts[INDEX[I]]+=1
    assert all(sum(counts[k] for k,I in enumerate(MINORS) if i in I)==B for i in range(R))
    return tuple(counts)

def main():
    rows=list(csv.DictReader((HERE/'POLARIZATION_R6_L1_B5_SOURCE.tsv').open(),delimiter='\t'))
    files=[]
    parts=16
    for part in range(parts):
        selected=rows[part::parts];data=[]
        for z,row in enumerate(selected):
            lam=tuple(map(int,row['partition'].split(',')));mult=int(row['source_multiplicity'])
            k=number(lam,R);cap=min(k,max(64,8*mult))
            rng=Random(20261121+sum((i+1)*v*100**i for i,v in enumerate(lam)))
            ids=sorted(rng.sample(range(k),cap)) if cap<k else list(range(k))
            rng.shuffle(ids)
            seeds=[seed_at(lam,i) for i in ids]
            assert len(set(seeds))==len(seeds)
            data.append((lam,mult,k,seeds))
        folder=HERE/'polarization_r6_parts';folder.mkdir(exist_ok=True)
        f=folder/f'part{part:02d}.seeds'
        with f.open('w') as out:
            print(R,1,B,len(data),file=out)
            for lam,m,k,seeds in data:
                print(*lam,m,k,len(seeds),file=out)
                for seed in seeds:print(*seed,file=out)
        print(part,len(data),'seeds',sum(len(z[3]) for z in data),'maxK',max(z[2] for z in data),flush=True)
    print('GT_cache',number.cache_info())

if __name__=='__main__':main()
