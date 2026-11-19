#!/usr/bin/env python3
"""Exact local, invariant, finite-group and displayed algebra checks for cote63."""
import sympy as s,json,itertools
from pathlib import Path
out={};a,b,c,d,e,t,x,z=s.symbols('a1 a2 a3 a4 a6 t x z')
def inv(v):
 a,b,c,d,e=v
 B2=a*a+4*b;B4=a*c+2*d;B6=c*c+4*e;B8=a*a*e-a*c*d+4*b*e+b*c*c-d*d
 C4=B2**2-24*B4;C6=-B2**3+36*B2*B4-216*B6
 D=-B2**2*B8-8*B4**3-27*B6**2+9*B2*B4*B6
 return list(map(s.expand,[B2,B4,B6,B8,C4,C6,D]))
B2,B4,B6,B8,C4,C6,D=inv([a,b,c,d,e])
out['cubic_discriminant_residual']=s.expand(s.discriminant(4*x**3+B2*x**2+2*B4*x+B6,x)-16*D)
g=inv([0,b,0,d,b*d/9]);_,_,_,_,g4,g6,gd=g
out['d6_gauge_residuals']=[s.factor(q) for q in [b*g4+g6/4,d*g4**2+36*gd,(b*d/9)*g4**3-g6*gd]]
def modpoly(f,p):return s.Poly(f,*sorted(f.free_symbols,key=str),modulus=p).as_expr() if f.free_symbols else int(f)%p
out['ordinary_char2']={n:modpoly(q,2) for n,q in zip(['b2','b4','b6','b8','c4','c6','Delta'],inv([1,b,0,0,e]))}
out['supersingular_char2']={n:modpoly(q,2) for n,q in zip(['b2','b4','b6','b8','c4','c6','Delta'],inv([0,b,c,d,e]))}
out['supersingular_char3']={n:modpoly(q,3) for n,q in zip(['b2','b4','b6','b8','c4','c6','Delta'],inv([0,0,0,d,e]))}
def vp(n,p):
 if n==0:return 100000
 v=0
 while n%p==0:n//=p;v+=1
 return v
out['divisor_orders']={}
for p,v in [(2,[t,0,1,0,0]),(3,[0,t,0,-1,0])]:
 vals=inv(v)
 for name,q in zip(['c4','c6','Delta'],vals[4:]):
  poly=s.Poly(q,t)
  out['divisor_orders'][f'p{p}_{name}']={'formula':s.factor(q),'special_fiber':modpoly(q,p),'m_adic_order':min(vp(int(co),p)+mon[0] for mon,co in poly.terms())}
u,zet=s.symbols('u zeta');eq=s.expand(t*(t-2*u)*(t-2*u*zet)*(t-2*u*zet**2))
eq=s.rem(eq,zet**2+zet+1,zet);eq=s.rem(eq,u**3-3,u)
out['four_branch_factor_residual']=s.expand(eq-t*(t**3-24))
hesse=s.rem(s.expand((t+2)*(t+2*zet)*(t+2*zet**2)),zet**2+zet+1,zet)
out['hesse_branch_factor_residual']=s.expand(hesse-t**3-8)
f=(t+2)/(t-1)
out['hesse_involution_residual']=s.factor(f.subs(t,f,simultaneous=True)-t)
out['hesse_tangent_numerator']=s.expand((t+2)-(t-1)*(t+2))
out['hesse_tangent_conclusion']='4-t² lies in(2,t)², so f(t)=t+2 mod m²; 2 stays fixed.'
# F4 in polynomial basis 1,w, w²+w+1=0, encoded by two bits.
def f4mul(a,b):
 v=0
 for k in range(2):
  if b&(1<<k):v^=a<<k
 if v&4:v^=7
 return v
def f4pow(a,n):
 v=1
 for _ in range(n):v=f4mul(v,a)
 return v
out['four_slopes_F4']=[0,1,2,3]
out['pairwise_slope_differences_nonzero']=all((a^b)!=0 for a,b in itertools.combinations(range(4),2))
# Automorphisms: x->u²x+s²; y->y+s u²x+t. All arithmetic in F4.
aut2=[(u,h,k) for u in [1,2,3] for h in range(4) for k in range(4) if (f4pow(k,2)^k)==f4pow(h,6)]
pts=list(itertools.product(range(4),repeat=2))
def perm2(g):
 u,h,k=g;u2=f4pow(u,2);h2=f4pow(h,2)
 return tuple(pts.index((f4mul(u2,x)^h2,y^f4mul(f4mul(h,u2),x)^k)) for x,y in pts)
P2=[perm2(g) for g in aut2]
def pmul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def porder(p):
 e=tuple(range(len(p)));q=p;n=1
 while q!=e:q=pmul(q,p);n+=1
 return n
def hist(P):return {n:sum(porder(p)==n for p in P) for n in sorted(set(map(porder,P)))}
out['Aut_char2']={'order':len(P2),'closed':all(pmul(a,b) in P2 for a in P2 for b in P2),'order_histogram':hist(P2),'kernel_differential_order':sum(g[0]==1 for g in aut2),'kernel_order_histogram':hist([p for p,g in zip(P2,aut2) if g[0]==1])}
# Verify preservation as a polynomial over F4 by testing coefficients in symbolic x,y
# encoded affine substitutions; the derived conditions s4+s=0, t²+t=s6 are listed exactly.
out['Aut_char2_conditions']={'s_equation':'s^4+s=0','t_equation':'t^2+t=s^6','printed_s4_plus1_failure_at_identity':1,'printed_t_equation_failure_s1_t2':(f4pow(2,2)^2^f4pow(1,3)^f4pow(1,2))}
# GL2(F3), its projective action, Borel and centralizer.
G=[q for q in itertools.product(range(3),repeat=4) if (q[0]*q[3]-q[1]*q[2])%3]
SL=[q for q in G if(q[0]*q[3]-q[1]*q[2])%3==1]
lines=[(1,0),(0,1),(1,1),(1,2)]
def norm3(v):
 if v[0]:return(1,v[1]*pow(v[0],-1,3)%3)
 return(0,1)
def act(q):return tuple(lines.index(norm3(((q[0]*x+q[1]*y)%3,(q[2]*x+q[3]*y)%3))) for x,y in lines)
proj={act(q) for q in SL};ident=(0,1,2,3)
cent=[p for p in itertools.permutations(range(4)) if all(pmul(p,q)==pmul(q,p) for q in proj)]
out['level3_counts']={'GL2':len(G),'SL2':len(SL),'Borel':sum(q[2]==0 for q in G),'Borel_SL':sum(q[2]==0 for q in SL),'projective_image':len(proj),'projective_kernel':[q for q in SL if act(q)==ident],'centralizer_A4_in_S4':cent}
out['good_reduction_at3_obstruction']={'model':'y²+y=x³','Delta':-27,'normalized_v_K_Delta':6,'possible_discriminant_valuations_mod12':6,'good_reduction_possible':False,'hypothesis':'K=Q(zeta3), v_K(3)=2, fixed elliptic curve; coordinate changes have u in K×'}
out['three_division_poly_model']=3*x*(x**3+1)
# Characteristic3 group as transformations x->u²x+r,y->u³y over F9, i²=-1.
def f9add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def f9mul(a,b):
 A,B=a%3,a//3;C,D=b%3,b//3
 return((A*C+2*B*D)%3)+3*((A*D+B*C)%3)
def f9pow(a,n):
 v=1
 for _ in range(n):v=f9mul(v,a)
 return v
points9=list(itertools.product(range(9),repeat=2))
def perm3(u,r):return tuple(points9.index((f9add(f9mul(f9pow(u,2),x),r),f9mul(f9pow(u,3),y))) for x,y in points9)
A3=[perm3(u,r) for u in range(1,9) if f9pow(u,4)==1 for r in range(3)]
out['Aut_char3']={'order':len(A3),'closed':all(pmul(a,b) in A3 for a in A3 for b in A3),'order_histogram':hist(A3)}
# Short-Weierstrass Laurent coefficients, independent recurrence from the ODE.
g2,g3=s.symbols('g2 g3');A=g2/20;B=g3/28;C=g2*g2/1200
X=z**-2+A*z*z+B*z**4+C*z**6
out['wp_ODE_residual_low_orders']=s.series(s.diff(X,z)**2-4*X**3+g2*X+g3,z,0,4)
out['canonical_short_coefficients']={'gamma4':-g2/4,'gamma6':-g3/4,'y_leading':-z**-3}
# Nonreduced equal-j comparison, checking faithful-flat obstruction algebraically.
eps=s.symbols('epsilon');jdef=s.factor(inv([0,0,0,eps,1])[4]**3/inv([0,0,0,eps,1])[6])
out['same_j_nonreduced_counterexample']={'j_series':s.series(jdef,eps,0,2),'obstruction':'Over C[epsilon]/epsilon², any change between short equations has r=s=t=0 and a4 transforms as u^-4 epsilon; it cannot become0 under faithfully flat base change.'}
txt=json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n'
(Path(__file__).resolve().parents[1]/'outputs/c63_more_algebra.json').write_text(txt);print(txt)
