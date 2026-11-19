"""Recheck the earlier-run R17 comparison locally, without unseen LM text."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
J=[(1,0),(0,1),(1,1)]
O=(0,0,0,0); I=(1,0,0,1)
mat=list(itertools.product(range(2),repeat=4))
det=lambda a:(a[0]*a[3]+a[1]*a[2])%2
G=[a for a in mat if det(a)]
sl=[a for a in mat if (a[0]+a[3])%2==0]
mv=lambda a,v:((a[0]*v[0]+a[1]*v[1])%2,(a[2]*v[0]+a[3]*v[1])%2)
mm=lambda a,b:tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2 for i in range(2) for j in range(2))
add=lambda a,b:tuple(x^y for x,y in zip(a,b))
inv=lambda a:(a[3],a[1],a[2],a[0])
cl=lambda f:min(tuple(f),tuple(x^1 for x in f))
wedge=lambda v,w:(v[0]*w[1]+v[1]*w[0])%2
f=lambda a:cl([wedge(v,mv(a,v)) for v in J])
delta=lambda v:cl([int(w==v) for w in J])
assert len({f(a) for a in sl})==4
assert {a for a in sl if f(a)==(0,0,0)}=={O,I}
for a,b in itertools.product(sl,repeat=2): assert f(add(a,b))==cl(add(f(a),f(b)))
for a,g in itertools.product(sl,G):
 lhs=f(mm(mm(g,a),inv(g)))
 rhs=cl([f(a)[J.index(mv(inv(g),v))] for v in J])
 assert lhs==rhs
for a in sl: assert f(a)==delta((a[1],a[2]))
fix={v:next(g for g in G if g!=I and mm(g,g)==I and mv(g,v)==v) for v in J}
fix[(0,0)]=O
for v,w in itertools.product([(0,0)]+J,repeat=2): assert fix[add(v,w)]==add(fix[v],fix[w])
out={'map':'A -> [v -> det(v,Av)] in F2^J/diagonal',
     'trace_zero_matrices':len(sl),'additivity_pairs_checked':64,'equivariance_pairs_checked':48,
     'kernel':[O,I],'image_size':4,'coordinate_comparisons_checked':8,
     'coordinate_formula':'(a,b;c,a) -> [delta_(b,c)], delta_0=0',
     'natural_vector_to_fixing_involution_is_linear':True,
     'scope':'Local algebra only; actual LM_140-2 scan569/R17 endpoint unavailable.'}
(ROOT/'outputs/scalar_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
