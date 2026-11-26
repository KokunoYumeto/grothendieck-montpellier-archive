# KRON A-030 / OBS S-003 key steps: Muir identity H(det_3)=c*det_3^3; Hessian rank of det_3 at rank-2 matrix = 6;
# Theta(per_3) != 0: Hessian of per_3 nondegenerate at some zero with dP != 0.
import sympy as sp, random
n=3
X=sp.Matrix(n,n,lambda i,j: sp.Symbol(f"x{i}{j}"))
vs=list(X)
det=X.det(); per=X.per()
def hess(f): return sp.Matrix([[sp.diff(f,a,b) for b in vs] for a in vs])
Hd=hess(det); Hp=hess(per)
random.seed(1)
ratios=[]
for t in range(4):
    pt={v:sp.Rational(random.randint(-9,9),random.randint(1,5)) for v in vs}
    hd=Hd.subs(pt).det(); dd=det.subs(pt)
    ratios.append(sp.nsimplify(hd/dd**3) if dd!=0 else None)
print("H(det3)/det3^3 at random points:",ratios)
# rank of Hessian of det3 at a rank-2 matrix
M={vs[k]:v for k,v in enumerate([1,2,3,4,5,6,5,7,9])} # row3=row1+row2 -> rank 2
print("rank of det-matrix:",sp.Matrix(3,3,[M[v] for v in vs]).rank(),"Hessian rank of det3 there:",Hd.subs(M).rank())
# per3 zero with dP!=0 and Hessian rank 9: search small integer points
found=None
for t in range(20000):
    vals=[random.randint(-3,3) for _ in range(9)]
    pt=dict(zip(vs,vals))
    if per.subs(pt)!=0: continue
    if all(sp.diff(per,v).subs(pt)==0 for v in vs): continue
    r=Hp.subs(pt).rank()
    if r==9: found=(vals,r); break
print("per3 zero with full-rank Hessian:",found)
# Theta(F)=q*H*dF - n*F*dH at that point: since F=0, Theta = q*H*dF, nonzero iff H!=0 and dF!=0
