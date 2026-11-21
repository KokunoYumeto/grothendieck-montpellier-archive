"""Independent symbolic audit of the G017 module presentation and all tags."""
from pathlib import Path
import json
import sympy as s
from verify_rectangular import partitions,character,z as class_z

HERE=Path(__file__).resolve().parent
A,B,C,D,E=s.symbols("A B C D E")
variables=(A,B,C,D,E)
x,y,z,w=s.symbols("x y z w")
coords=(x,y,z,w)
t=s.symbols("t")
F=A*D*(E-B-C)-B*C*(E-A-D)
K=s.Matrix([
 [0,E-B,0,-C,-B*C+B*D+C*D-D*E],
 [0,A-E,D,0,-A*C+A*D-C*D+C*E],
 [D-E,0,0,A,-A*B+A*D-B*D+B*E],
 [E-C,0,-B,0,A*B+A*C-A*E-B*C],
 [C-D,B-A,0,0,-A*D+B*C]])
out=[]
assert s.expand(K.det(method="domain-ge")-3*F**2)==0
adj=K.adjugate(method="domain-ge")
entries=[]
for q in adj:
    quotient,remainder=s.div(s.Poly(q,variables),s.Poly(F,variables))
    assert remainder.is_zero
    entries.append(quotient.as_expr())
P=s.Matrix(5,5,entries)
assert list(P[4,:])==[-A,-B,-C,-D,-E]
assert all(s.expand(v)==0 for v in P*K-3*F*s.eye(5))
assert all(s.expand(v)==0 for v in K*P-3*F*s.eye(5))
assert s.expand(P.det(method="domain-ge")-81*F**3)==0
assert s.expand(P[:2,:2].det()+3*A*B*(A*D-B*C))==0
out.append("PASS exact K,P, determinant identities, divisibility and nonzero 2x2 minor")
print(out[-1],flush=True)

f=s.Matrix([x*z-x*y,x*w-x*y,y*z-x*y,y*w-x*y,z*w-x*y])
h=s.Matrix([f[0]*(x+y+z-2*w),f[1]*(x+y+w-2*z),
            f[2]*(x+y+z-2*w),f[3]*(x+y+w-2*z),
            z*w*(z+w-2*x-2*y)-x*y*(x+y-2*z-2*w)])
for i in range(4):
    for j in range(5):
        residual=f[j]*coords[i]**2-P[i,j].subs(dict(zip(variables,f)),simultaneous=True)-coords[i]*h[j]
        assert s.expand(residual)==0,(i,j)
out.append("PASS all twenty exact quotient-line correction identities")
print(out[-1],flush=True)

# Derive actual U action matrices by substituting the literal point-frame
# action. This does not use the producer's character rational functions.
ell=[s.eye(4)[:,i] for i in range(4)]+[-s.ones(4,1)]
mons=[x*y,x*z,x*w,y*z,y*w,z*w]
fc=s.Matrix([[s.Poly(q,coords).coeff_monomial(m) for m in mons] for q in f])
denominator=s.prod(1-t**j for j in (2,4,6,10))
class_H={}
for cyc in partitions(5):
    perm=list(range(5))
    start=0
    for size in cyc:
        for j in range(size):
            perm[start+j]=start+(j+1)%size
        start+=size
    g=s.Matrix.hstack(*(ell[perm[i]] for i in range(4)))
    gv=g.inv()*s.Matrix(coords)
    rows=[]
    for q in f:
        qg=s.expand(q.subs(dict(zip(coords,gv)),simultaneous=True))
        coefficients=s.Matrix([s.Poly(qg,coords).coeff_monomial(m) for m in mons])
        c=fc.T.gauss_jordan_solve(coefficients)[0]
        assert s.expand(qg-sum(c[j]*f[j] for j in range(5)))==0
        rows.append(list(c))
    mat=s.Matrix(rows)
    hpoly=s.cancel(denominator*(s.trace(g)+t-s.trace(mat)*t*t)/(s.eye(5)-t*mat).det())
    hpoly=s.Poly(hpoly,t)
    assert hpoly.degree()<=19
    class_H[cyc]=hpoly
catalog=json.loads((HERE.parent/"root"/"FIVE_POINT_Q_TAGS.json").read_text())
tags={tuple(row["label"]):row["coefficients"] for row in catalog["tags"]}
for mu in partitions(5):
    coeff=[]
    for degree in range(20):
        value=sum((120//class_z(cyc))*character(mu,cyc)*poly.nth(degree)
                  for cyc,poly in class_H.items())/120
        assert value.is_Integer and value>=0
        coeff.append(int(value))
    assert coeff==tags[mu],(mu,coeff,tags[mu])
    out.append(f"PASS tag row {mu}: all twenty degrees; total {sum(coeff)}")
assert class_H[(1,1,1,1,1)].eval(1)==4320
assert all(poly.eval(1)==0 for cyc,poly in class_H.items() if cyc!=(1,1,1,1,1))
out.append("PASS all140 tag coefficients from actual quadratic action; regular character36 times")
(HERE/"FIVE_POINT_Q_MODULE_INDEPENDENT_CHECK.txt").write_text("\n".join(out)+"\n")
print("\n".join(out[2:]))
