"""Independent symbolic reconstruction of the displayed f0 polar tensor action.

Uses SymPy polynomial-ring arithmetic rather than the author's monomial-set
Pfaffian implementation. It verifies the specified 81x81 determinant over
F2[a,b,c] by constant-unit elimination, with no parameter specialization.
"""
from pathlib import Path
from datetime import datetime,timezone
import itertools,json,time
from sympy.polys.rings import ring
from sympy.polys.domains import GF
started=time.perf_counter();w=Path(__file__).resolve().parents[1]
R,a,b,c=ring('a,b,c',GF(2));zero=R.zero;one=R.one
terms={tuple(int(ch)-1 for ch in s):one for s in ['129','138','156','179','236','259','268','349','367','457']}
for s in ['134','148','157']:terms[tuple(int(ch)-1 for ch in s)]=a
terms[(0,3,5)]=b
for s in ['126','135']:terms[tuple(int(ch)-1 for ch in s)]=c
triples=list(itertools.combinations(range(9),3));removed={(3,5,6),(3,6,7),(4,6,7)};rowlabels=[t for t in triples if t not in removed];assert len(rowlabels)==81
cols=list(itertools.product(range(9),repeat=2));A=[[zero for _ in cols] for _ in rowlabels];index={t:i for i,t in enumerate(rowlabels)}
for j,(u,v) in enumerate(cols):
    for t,coefficient in terms.items():
        for pos in range(3):
            if t[pos]!=v:continue
            tt=list(t);tt[pos]=u
            if len(set(tt))!=3:continue
            tt=tuple(sorted(tt))
            if tt in index:A[index[tt]][j]+=coefficient
active_rows=list(range(81));active_cols=list(range(81));pivots=[]
while active_cols:
    found=next(((i,j) for i in active_rows for j in active_cols if A[i][j]==one),None)
    assert found is not None,{'completed_pivots':len(pivots),'remaining':len(active_cols)}
    i,j=found;pivots.append({'row_triple':[x+1 for x in rowlabels[i]],'column_E':[x+1 for x in cols[j]]});active_rows.remove(i);active_cols.remove(j)
    for ii in active_rows:
        coefficient=A[ii][j]
        if coefficient:
            for jj in active_cols:A[ii][jj]-=coefficient*A[i][jj]
            A[ii][j]=zero
result={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'ring':'F2[a,b,c]','polar_terms':16,'matrix_shape':[81,81],'deleted_exterior_rows':[[4,6,7],[4,7,8],[5,7,8]],'unit_pivots':pivots,'determinant':'1','scope':'Independent exact reconstruction from the printed16-term polar tensor, using a different polynomial arithmetic implementation. No geometric theorem is inferred from this computation alone.'}
p=w/'outputs/root_p_rank_zero_polar_independent.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='unit_pivots'},indent=2))
