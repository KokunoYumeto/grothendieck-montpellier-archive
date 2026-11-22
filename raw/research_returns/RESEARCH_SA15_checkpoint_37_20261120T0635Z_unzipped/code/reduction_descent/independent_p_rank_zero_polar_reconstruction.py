"""Independent symbolic reconstruction for the uniform f=0 polar tensor.
Uses SymPy polynomial-ring arithmetic, a prescribed 81-row minor, no trace row.
"""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import itertools,json,time
from sympy.polys.rings import ring
from sympy.polys.domains import GF
start=time.perf_counter()
R,*vars=ring(','.join([f'x{i}' for i in range(1,10)]+['a','b','c']),GF(2))
x=vars[:9];a,b,c=vars[9:]
base=['267','258','348','169','357','249','178','456','235']
terms={tuple(int(j)-1 for j in t):R.one for t in base}
terms.update({(0,3,6):a,(0,3,4):b,(0,2,3):c})
M=[[R.zero for j in range(9)] for i in range(9)]
for triple,coef in terms.items():
    for i,j in itertools.combinations(triple,2):
        k=next(k for k in triple if k not in (i,j))
        M[i][j]+=coef*x[k];M[j][i]+=coef*x[k]
@lru_cache(None)
def pf(indices):
    if not indices:return R.one
    i=indices[0]
    return sum((M[i][j]*pf(tuple(k for k in indices[1:] if k!=j)) for j in indices[1:]),R.zero)
qs=[]
for omit in range(9):
    q,rem=pf(tuple(i for i in range(9) if i!=omit)).div(x[omit])
    assert not rem
    qs.append(q)
assert all(q==qs[0] for q in qs)
S,aa,bb,cc=ring('a,b,c',GF(2));params=[aa,bb,cc]
B={}
for exps,coef in qs[0].items():
    if sum(exps[:9])==3 and max(exps[:9])==1:
        idx=tuple(i for i,v in enumerate(exps[:9]) if v)
        v=S.one
        for z,e in zip(params,exps[9:]):v*=z**e
        B[idx]=B.get(idx,S.zero)+v
expected={tuple(int(j)-1 for j in t):S.one for t in ['129','138','156','179','236','259','268','349','367','457']}
for coef,triples in [(aa,['134','148','157']),(bb,['146']),(cc,['126','135'])]:
    for t in triples:expected[tuple(int(j)-1 for j in t)]=coef
assert B==expected
triples=list(itertools.combinations(range(9),3));removed={(3,5,6),(3,6,7),(4,6,7)}
rows=[t for t in triples if t not in removed];assert len(rows)==81
columns=list(itertools.product(range(9),repeat=2))
# Independent exterior coefficient formula: E_ab replaces one occurrence of b
# by a. All signs are positive in characteristic two.
D=[]
for out in rows:
    row=[]
    for aa_i,bb_i in columns:
        val=S.zero
        for inp,coef in B.items():
            if bb_i not in inp:continue
            new=[aa_i if t==bb_i else t for t in inp]
            if len(set(new))==3 and tuple(sorted(new))==out:val+=coef
        row.append(val)
    D.append(row)
remaining_rows=list(range(81));remaining_cols=list(range(81));pivots=[]
while remaining_cols:
    found=next(((i,j) for i in remaining_rows for j in remaining_cols if D[i][j]==S.one),None)
    assert found is not None,'Prescribed minor lacks a unit pivot'
    i,j=found;pivots.append([list(rows[i]),list(columns[j])]);remaining_rows.remove(i);remaining_cols.remove(j)
    for k in remaining_rows:
        coeff=D[k][j]
        if coeff:
            for l in remaining_cols:D[k][l]-=coeff*D[i][l]
            D[k][j]=S.zero
assert len(pivots)==81
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
 'all_nine_pfaffian_divisions':True,'common_cubic':str(qs[0]),'polar_tensor':{''.join(str(i+1) for i in k):str(v) for k,v in B.items()},
 'prescribed_removed_rows':['467','478','578'],'unit_pivots':pivots,'pivot_count':81,
 'determinant_over_F2_a_b_c':'1','trace_row_used':False,
 'scope':'Independent polynomial-ring reconstruction and prescribed minor, no field specialization.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['unit_pivots','common_cubic','polar_tensor']},indent=2))
