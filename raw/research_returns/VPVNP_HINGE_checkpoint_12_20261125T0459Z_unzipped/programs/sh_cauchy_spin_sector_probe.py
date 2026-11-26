"""Exact r=4 multiplicity-sector probe for central spin projectors.

The local covectors annihilate Sym^3 and retain the two-dimensional
multiplicity slice of the spin1/2 sector.  Failure of this projected
linear identity refutes only scalar central-projector lifts, not dense
noncentral multiplicity maps.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,itertools,json
import sympy as sp

W=Path(__file__).resolve().parents[1]
ip=W/'inputs/sh_cauchy_spin_sector_probe.json';cfg=json.loads(ip.read_text())
r=cfg['r'];assert r==4
weights=cfg['local_weights'];assert len(weights)==8 and all(x in(1,2)for x in weights)
ports=[tuple(j for j in range(r)if j!=i)for i in range(r)]
local=[]
for weight in weights:
    cov=[[(1,1),(2,-1)],[(2,1),(4,-1)]]
    if weight==2:cov=[[(7-mask,coef)for mask,coef in row]for row in cov]
    inv={}
    for choice,row in enumerate(cov):
        for mask,coef in row:inv.setdefault(mask,[]).append((choice,coef))
    local.append(inv)

def target_edges():
    es=[]
    for shift in (0,r):
        for i in range(r):
            for j in range(i+1,r):
                es.append((shift+i,ports[i].index(j),shift+j,ports[j].index(i)))
    return es

def crown_edges(sigma):
    return [(i,ports[i].index(j),r+sigma[j],ports[sigma[j]].index(sigma[i]))
            for i in range(r)for j in range(r)if i!=j]

def projected(edges):
    ans=[0]*256
    for word in range(1<<len(edges)):
        masks=[0]*8;sign=1
        for e,(a,pa,b,pb)in enumerate(edges):
            bit=(word>>e)&1;masks[a]|=bit<<pa;masks[b]|=(1-bit)<<pb
            if bit:sign=-sign
        opts=[local[i].get(mask)for i,mask in enumerate(masks)]
        if any(x is None for x in opts):continue
        terms=[(0,sign)]
        for i,row in enumerate(opts):
            terms=[(index+(choice<<i),coef*c)for index,coef in terms for choice,c in row]
        for index,coef in terms:ans[index]+=coef
    return ans

perms=list(itertools.permutations(range(r)))
h=projected(target_edges());cols=[projected(crown_edges(s))for s in perms]
M=sp.Matrix(256,24,lambda i,j:cols[j][i]);H=sp.Matrix(h)
_,piv=M.rref();rank=len(piv)
C=M[:,list(piv)].row_join(H);_,cpiv=C.rref();aug=len(cpiv)
out={'status':'EXACT SECTOR PROBE','input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'r':r,'local_weights':weights,'permutations':[list(s)for s in perms],
     'matrix_columns':cols,'target':h,'rank_crowns':rank,'rank_augmented':aug,
     'target_nonzero_coordinates':sum(x!=0 for x in h),
     'scope':'central spin projectors only; no conclusion for arbitrary local maps on multiplicity spaces'}
if aug>rank:
    _,rows=C.T.rref();rows=list(rows[:aug])
    B=C[rows,:];assert B.rows==B.cols==aug
    rhs=sp.zeros(aug,1);rhs[-1]=1
    w=B.T.inv()*rhs
    full=sp.zeros(256,1)
    for i,x in zip(rows,w):full[i]=x
    assert (full.T*M)==sp.zeros(1,24) and (full.T*H)[0]==1
    den=sp.ilcm(*[x.q for x in w]);integers=[int(den*x)for x in w]
    assert all(sum(integers[j]*cols[c][rows[j]] for j in range(len(rows))) == 0 for c in range(24))
    target_value=sum(integers[j]*h[rows[j]]for j in range(len(rows)))
    assert target_value==int(den)>0
    out.update(status='PASS exact obstruction to central-projector-only Cauchy lift',
               witness_rows=rows,witness_coefficients=integers,witness_target_value=target_value,
               independent_crown_columns=list(piv))
else:
    sol=sp.linsolve((M,H));out['solution_set']=str(sol)
binary_pivots={};binary_witness=None
for i in range(256):
    word=sum((cols[j][i]%2)<<j for j in range(24))|((h[i]%2)<<24)
    comb=1<<i
    while word&((1<<24)-1):
        p=((word&((1<<24)-1))&-(word&((1<<24)-1))).bit_length()-1
        if p in binary_pivots:
            row,other=binary_pivots[p];word^=row;comb^=other
        else:
            binary_pivots[p]=(word,comb);break
    else:
        if word>>24&1:binary_witness=[j for j in range(256)if comb>>j&1];break
out['characteristic_two_witness_rows']=binary_witness
if binary_witness is not None:
    assert all(sum(cols[c][i] for i in binary_witness) % 2 == 0 for c in range(24))
    assert sum(h[i]for i in binary_witness)%2==1
dest=W/cfg['output'];tmp=dest.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(dest)
print(json.dumps({k:v for k,v in out.items()if k not in('matrix_columns','target','permutations','solution_set')},indent=2))
