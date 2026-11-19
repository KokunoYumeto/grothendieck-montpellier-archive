#!/usr/bin/env python3
"""Exact audits of displayed cote-63 formulas. Original transcriptions unchanged."""
from pathlib import Path
import sympy as s
import json,itertools,importlib.util
out={}
a1,a2,a3,a4,a6,r,v,h,u,x,y,z,L,N,t=s.symbols('a1 a2 a3 a4 a6 r s t u x y z lambda nu T')
def inv(A):
    a,b,c,d,e=A
    b2=a*a+4*b; b4=a*c+2*d; b6=c*c+4*e
    b8=a*a*e-a*c*d+4*b*e+b*c*c-d*d
    c4=b2*b2-24*b4; c6=-b2**3+36*b2*b4-216*b6
    delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return list(map(s.expand,[b2,b4,b6,b8,c4,c6,delta]))
B=inv([a1,a2,a3,a4,a6]); b2,b4,b6,b8,c4,c6,D=B
out['invariant_residuals']={
 '4b8-(b2b6-b4^2)':s.expand(4*b8-b2*b6+b4*b4),
 'c4^3-c6^2-1728Delta':s.expand(c4**3-c6*c6-1728*D),
 'second_discriminant':s.expand(D-(b4**3-27*b6*b6+b8*(36*b4-b2*b2))),
 '12d6':s.expand(12*(b2*b4-18*b6)-c6-b2*c4),
 '-12d8':s.expand(-12*(b2*b2*b4-48*b4*b4+18*b2*b6)-c4*c4-b2*c6)}
AA=[(a1+2*v)/u,(a2-v*a1+3*r-v*v)/u**2,(a3+r*a1+2*h)/u**3,
    (a4-v*a3+2*r*a2-(h+r*v)*a1+3*r*r-2*v*h)/u**4,
    (a6+r*a4+r*r*a2+r**3-h*a3-h*h-r*h*a1)/u**6]
XX=u*u*x+r; YY=u**3*y+v*u*u*x+h
F=YY*YY+a1*XX*YY+a3*YY-XX**3-a2*XX*XX-a4*XX-a6
G=y*y+AA[0]*x*y+AA[2]*y-x**3-AA[1]*x*x-AA[3]*x-AA[4]
out['coordinate_substitution_residual']=s.expand(F/u**6-G)
BP=inv(AA)
expected=[b2+12*r,b4+r*b2+6*r*r,b6+2*r*b4+r*r*b2+4*r**3,
 b8+3*r*b6+3*r*r*b4+r**3*b2+3*r**4,c4,c6,D]
out['weighted_coordinate_residuals']=[s.factor(u**w*b-e) for w,b,e in zip([2,4,6,8,4,6,12],BP,expected)]
J=s.symbols('J'); g=inv([1,0,0,-36/(J-1728),-1/(J-1728)])
out['generic_j_model']={k:s.factor(val) for k,val in zip(['b2','b4','b6','b8','c4','c6','Delta'],g)}
out['generic_j_reconstruction']=s.factor(g[4]**3/g[6])
wp=z**3
for _ in range(9):
    wp=s.series(z**3+a1*z*wp+a2*z*z*wp+a3*wp*wp+a4*z*wp*wp+a6*wp**3,z,0,10).removeO().expand()
xp=s.series(z/wp,z,0,3)
yp=-xp/z
om=s.series(s.diff(xp.removeO(),z)/(2*yp.removeO()+a1*xp.removeO()+a3),z,0,4)
out['formal_w_through_z9']=wp
out['formal_x_through_z2']=s.expand(xp)
out['formal_omega_through_z3']=s.expand(om)
out['formal_truncation_scope']='w through z^9; x only through z^2 and omega only through z^3 are claimed. More terms of x would need more terms of w.'
poly=s.Poly((L*z+N)*(1-a1*z-a3*(L*z+N))-z**3-a2*z*z*(L*z+N)-a4*z*(L*z+N)**2-a6*(L*z+N)**3,z)
actual=s.factor(-poly.nth(2)/poly.nth(3))
transcribed=(a1*L+a3*L*L-a2*N-2*a4*L*N-3*a6*L*L*N)/(1+a2*L+a4*L*L+a6*L**3)
out['viete_sum_actual']=actual
out['viete_transcription_residual']=s.factor(transcribed-actual)
out['versal_at_2']=dict(zip(['b2','b4','b6','b8','c4','c6','Delta'],map(s.factor,inv([t,0,1,0,0]))))
out['versal_at_3']=dict(zip(['b2','b4','b6','b8','c4','c6','Delta'],map(s.factor,inv([0,t,0,-1,0]))))
out['torsor_counts_Z1over6']={'mu6':2*6*6,'mu4':2*4*4}
M=s.Matrix([[26,3],[14,21]])
out['U29_charpoly']=s.Poly(M.charpoly().as_expr(),M.charpoly().gen,modulus=29).as_expr()
out['U29_mu_roots']=[i for i in range(29) if (i*i-8*i+5)%29==0]
out['U29_determinant_mod29']=int(M.det()%29)
out['U29_power840_mod29']=[[int(e%29) for e in row] for row in (M**840).tolist()]
# Group calculations over F_3; index-two subgroups would give a nontrivial C2 quotient.
els=[q for q in itertools.product(range(3),repeat=4) if (q[0]*q[3]-q[1]*q[2])%3==1]
def mul(A,B): return ((A[0]*B[0]+A[1]*B[2])%3,(A[0]*B[1]+A[1]*B[3])%3,(A[2]*B[0]+A[3]*B[2])%3,(A[2]*B[1]+A[3]*B[3])%3)
one=(1,0,0,1)
def inverse(A):return (A[3],-A[1]%3,-A[2]%3,A[0])
def closure(S):
    V={one};todo=list(S)
    while todo:
        a=todo.pop()
        if a in V:continue
        old=list(V);V.add(a)
        for b in old:
            for c in (mul(a,b),mul(b,a)):
                if c not in V:todo.append(c)
    return V
comm=closure({mul(mul(mul(A,B),inverse(A)),inverse(B)) for A in els for B in els})
out['SL2F3']={'order':len(els),'derived_order':len(comm),'abelianization_order':len(els)//len(comm),'no_index_two_subgroup':'abelianization has odd order 3, so no quotient C2, hence no subgroup of order12'}
# Tensor-real-structure audit; beta=-2i rho and standard pairing <omega,y>=1.
aa,bb=s.symbols('alpha alphabar');rho=s.symbols('rho',positive=True,real=True)
beta=-2*s.I*rho; c=(aa*bb-1)/beta
out['real_structure']={'sigma':s.simplify(c/(2*s.I)),'4rho_sigma':s.simplify(4*rho*c/(2*s.I)),
 'square_lattice_counterexample':'alpha=0, rho=1, sigma=-1/4: 4rho sigma=-1, not 1. Pairing-compatible conjugation matrix [[0,-i/2],[-2i,0]].'}
out['optional_libraries']={n:importlib.util.find_spec(n) is not None for n in ['flint','numpy','mpmath']}
out={k:v for k,v in out.items()}
txt=json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n'
path=Path(__file__).resolve().parents[1]/'outputs/c63_algebra.json';path.write_text(txt)
print(txt)
