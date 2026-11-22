"""Independent exact fixed-minor reconstruction from the displayed f1 polar tensor."""
from pathlib import Path
from datetime import datetime,timezone
import itertools,json,time
from sympy.polys.rings import ring
from sympy.polys.domains import GF
started=time.perf_counter();w=Path(__file__).resolve().parents[1]
R,a,b=ring('a,b',GF(2));zero=R.zero;one=R.one
terms={tuple(int(ch)-1 for ch in s):one for s in ['158','167','179','247','259','268','349','367','457']}
for s in ['148','157']:terms[tuple(int(ch)-1 for ch in s)]=a
for s in ['126','135']:terms[tuple(int(ch)-1 for ch in s)]=b
removed={(0,1,2),(2,3,4),(2,4,5)};rowlabels=[t for t in itertools.combinations(range(9),3) if t not in removed];cols=list(itertools.product(range(9),repeat=2))
assert len(rowlabels)==81;index={t:i for i,t in enumerate(rowlabels)};A=[[zero for _ in cols] for _ in rowlabels]
for j,(u,v) in enumerate(cols):
    for t,coefficient in terms.items():
        for pos in range(3):
            if t[pos]!=v:continue
            tt=list(t);tt[pos]=u
            if len(set(tt))!=3:continue
            tt=tuple(sorted(tt))
            if tt in index:A[index[tt]][j]+=coefficient
rows=list(range(81));columns=list(range(81));pivots=[]
while columns:
    found=next(((i,j) for i in rows for j in columns if A[i][j]==one),None)
    if found is None:break
    i,j=found;pivots.append({'row_triple':[x+1 for x in rowlabels[i]],'column_E':[x+1 for x in cols[j]]});rows.remove(i);columns.remove(j)
    for ii in rows:
        coefficient=A[ii][j]
        if coefficient:
            for jj in columns:A[ii][jj]-=coefficient*A[i][jj]
            A[ii][j]=zero
assert len(pivots)==77 and len(rows)==len(columns)==4
residual=[[A[i][j] for j in columns] for i in rows];det=zero
for permutation in itertools.permutations(range(4)):
    term=one
    for i,j in enumerate(permutation):term*=residual[i][j]
    det+=term
assert det==b**4
result={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'ring':'F2[a,b]','polar_terms':13,'matrix_shape':[81,81],'deleted_exterior_rows':[[1,2,3],[3,4,5],[3,5,6]],'unit_pivots':pivots,'residual_rows':[[x+1 for x in rowlabels[i]] for i in rows],'residual_columns':[[x+1 for x in cols[j]] for j in columns],'residual_matrix':[[str(x) for x in row] for row in residual],'determinant':str(det),'scope':'Independent exact polynomial-ring reconstruction of the fixed81minor from the printed13-term tensor. No parameter specialization; invertible precisely where b!=0. Geometric normal-form/Coble transfer needs separate proof.'}
p=w/'outputs/root_p_rank_one_polar_independent.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='unit_pivots'},indent=2))
