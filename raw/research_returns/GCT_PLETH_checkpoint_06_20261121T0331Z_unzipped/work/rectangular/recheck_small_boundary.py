"""Independent MN characters and NumPy/Laplace selected-entry checks."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations,permutations
from collections import defaultdict
from math import gcd
from fractions import Fraction
import numpy as np
import csv,gzip
from verify_rectangular import partitions,character,power_sum_plethysm
HERE=Path(__file__).resolve().parent
P=1000003
def determinant(A):
    if not A:return 1
    return sum((-1)**j*A[0][j]*determinant(tuple(tuple(row[k] for k in range(len(A)) if k!=j)
                                                    for row in A[1:]))
               for j in range(len(A)))%P
def run(r,L,b):
    stem=HERE/f'POLARIZATION_R{r}_L{L}_B{b}'
    source={tuple(map(int,row['partition'].split(','))):int(row['source_multiplicity'])
            for row in csv.DictReader(Path(str(stem)+'_SOURCE.tsv').open(),delimiter='\t')}
    ps=power_sum_plethysm(r,b);checked=0
    for lam in partitions(r*b):
        if len(lam)>r:continue
        padded=lam+(0,)*(r-len(lam))
        value=sum((c*character(lam,cyc) for cyc,c in ps.items()),Fraction())
        assert value==source.get(padded,0),(r,L,b,lam,value,source.get(padded,0))
        checked+=1
    it=iter(map(int,Path(str(stem)+'.selected').read_text().split()))
    rr,LL,bb,blocks,prime,npnt=(next(it) for _ in range(6))
    assert(rr,LL,bb,prime)==(r,L,b,P) and blocks==len(source)
    points=[tuple(next(it) for _ in range(r*r+r)) for _ in range(npnt)]
    minors=[I for h in range(1,r+1) for I in combinations(range(r),h)]
    index={I:i for i,I in enumerate(minors)};M=len(minors)
    @lru_cache(None)
    def forms(point):
        pt=points[point];X=tuple(tuple(pt[r*i+j] for j in range(r)) for i in range(r));x=pt[r*r:]
        result=[]
        for I in minors:
            h=len(I);A=tuple(tuple(X[i][j] for j in I) for i in range(h))
            linear=[0]*r
            for j,k in enumerate(I):
                C=tuple(tuple(x[i] if jj==j else A[i][jj] for jj in range(h)) for i in range(h))
                linear[k]=determinant(C)
            result.append((determinant(A),linear))
        return result
    @lru_cache(None)
    def coefficient(counts,point):
        dp=np.zeros((L+1,)*r,dtype=np.int64);dp[(0,)*r]=1
        for z in range(M-1,-1,-1):
            d,a=forms(point)[z]
            for _ in range(counts[z]):
                nd=dp*d
                for j in minors[z]:
                    dst=[slice(None)]*r;src=dst.copy();dst[j]=slice(1,None);src[j]=slice(None,-1)
                    nd[tuple(dst)]+=a[j]*dp[tuple(src)]
                dp=nd%P
        return int(dp[(L,)*r])
    def average(counts):
        result=defaultdict(int)
        for p in permutations(range(r)):
            target=[0]*M;sg=1
            for z,I in enumerate(minors):
                if not counts[z]:continue
                J=tuple(p[i] for i in I)
                sg*=(-1)**(counts[z]*sum(J[i]>J[j] for i in range(len(J)) for j in range(i+1,len(J))))
                target[index[tuple(sorted(J))]]+=counts[z]
            result[tuple(target)]+=sg
        result={k:v for k,v in result.items() if v}
        assert result
        divisor=0
        for v in result.values():divisor=gcd(divisor,abs(v))
        if result[min(result)]<0:divisor=-divisor
        return [(counts,c//divisor) for counts,c in result.items()]
    entries=0;ranktotal=0;kernel=0;seen=set()
    for _ in range(blocks):
        lam=tuple(next(it) for _ in range(r));m,rank=next(it),next(it)
        assert lam not in seen and source[lam]==m;seen.add(lam)
        expected_kernel=int(lam==(b,)*r and b%2==0 and r*L==b+1)
        assert rank==m-expected_kernel
        if expected_kernel:assert m==1 and rank==0
        selected=[]
        for j in range(rank):
            oldindex=next(it);counts=tuple(next(it) for _ in range(M))
            assert tuple(sum(counts[z] for z,I in enumerate(minors) if len(I)>i) for i in range(r))==lam
            assert all(sum(counts[z] for z,I in enumerate(minors) if i in I)==b for i in range(r))
            selected.append(average(counts))
        rows=[next(it) for _ in range(rank)]
        matrix=[tuple(next(it) for _ in range(rank)) for _ in range(rank)]
        d=next(it);assert determinant(tuple(matrix))==d!=0
        for i,point in enumerate(rows):
            for j,terms in enumerate(selected):
                value=sum(c*coefficient(counts,point) for counts,c in terms)%P
                assert value==matrix[i][j],(r,L,b,lam,i,j,value,matrix[i][j])
                entries+=1
        ranktotal+=rank;kernel+=expected_kernel
    assert seen==set(source) and next(it,None) is None
    with gzip.open(Path(str(stem)+'.selected.gz'),'wb',compresslevel=9) as f:
        f.write(Path(str(stem)+'.selected').read_bytes())
    result=dict(r=r,L=L,b=b,source_constituents=len(source),source_HW_dimension=sum(source.values()),
                image_HW_rank=ranktotal,rectangular_kernel_multiplicity=kernel,
                independent_character_partitions=checked,selected_entries=entries,
                Taylor_evaluations=coefficient.cache_info().currsize,status='PASS')
    print(result,flush=True)
    return result
if __name__=='__main__':
    results=[run(*case) for case in [(3,2,5),(3,3,8),(5,1,4)]]
    with (HERE/'SMALL_BOUNDARY_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]),delimiter='\t');w.writeheader();w.writerows(results)
