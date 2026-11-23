from itertools import combinations
from pathlib import Path
import sympy as s,json
# Exterior algebra ordered a1,a2,b1,b2,bar a1,bar a2,bar b1,bar b2.
def add(*args):
 d={}
 for a in args:
  for k,v in a.items():d[k]=d.get(k,0)+v
 return {k:s.simplify(v) for k,v in d.items() if s.simplify(v)!=0}
def scale(c,a):return {k:s.simplify(c*v) for k,v in a.items() if s.simplify(c*v)!=0}
def wedge(a,b):
 d={}
 for I,x in a.items():
  for J,y in b.items():
   if set(I)&set(J):continue
   k=tuple(sorted(I+J));v=(-1)**sum(i>j for i in I for j in J)*x*y;d[k]=d.get(k,0)+v
 return {k:s.simplify(v) for k,v in d.items() if s.simplify(v)!=0}
def power(a,n):
 z={():s.Integer(1)}
 for _ in range(n):z=wedge(z,a)
 return z
beta=add(*[{(i,i+4):s.I} for i in range(4)])
A={(0,1):1};B={(2,3):1};Ab={(4,5):1};Bb={(6,7):1}
w=scale(s.Rational(1,3),add(wedge(A,Bb),wedge(B,Ab)))
S=add(scale(s.Rational(1,6),power(beta,2)),w)
def integral(a):return s.simplify(9*a.get(tuple(range(8)),0))
H11=[{(i,4+j):1} for i in range(4) for j in range(4)]
G=s.Matrix([[integral(wedge(wedge(x,y),S)) for y in H11] for x in H11])
H20=s.Matrix([[integral(wedge(wedge(x,y),S)) for y in [Ab,Bb]] for x in [A,B]])
eigs=[3,3,3,0,0,0,0]
def e(k):return sum(s.prod(t) for t in combinations(eigs,k))
def intersect(theta_num,xi_num):
 # remaining eta power brings integration to dimension theta_num+xi_num.
 return s.factorial(theta_num)*s.factorial(xi_num)*s.binomial(7-xi_num,theta_num)*e(xi_num)
Eeta=9*intersect(0,0)-3*intersect(0,1)+s.Rational(1,2)*intersect(0,2)
Eetat=9*intersect(1,0)-3*intersect(1,1)+s.Rational(1,2)*intersect(1,2)
Ett=9*intersect(2,0)-3*intersect(2,1)+s.Rational(1,2)*intersect(2,2)
checks={'beta_fourth_216':integral(power(beta,4))==216,'Weil_norm_two':integral(power(w,2))==2,'mixed_beta_square_zero':integral(wedge(power(beta,2),w))==0,'H20_block':H20==s.Matrix([[3,3],[3,3]]),'Lagrangian_kernel':H20*s.Matrix([1,-1])==s.zeros(2,1),'H11_rank_twelve':G.rank()==12,'H11_radical_four':len(G.nullspace())==4,'total_eta_square_nine':Eeta==9,'total_eta_theta_36':Eetat==36,'total_theta_square108':Ett==108,'total_Ksquare45':Ett-2*Eetat+Eeta==45,'total_c2_27':Ett/2-3*Eeta==27,'total_chi_six':((Ett-2*Eetat+Eeta)+(Ett/2-3*Eeta))/12==6}
assert all(checks.values()),checks
out={'all_pass':True,'checks':checks,'H20_block':H20.tolist(),'H11_Gram':G.tolist(),'H11_radical':[list(x) for x in G.nullspace()],'normal_form':'beta=i sum dz_j wedge dbarz_j, w=(AbarB+BbarA)/3, integralABbarAbarB=9','scope':'Exact exterior algebra and Chern intersection arithmetic; geometric smoothness, nonzero component and q=4 supplied separately'}
p=Path(__file__).with_name('norm_surface_pairings_certificate.json');p.write_text(json.dumps(out,indent=2,default=str));print(json.dumps({'all_pass':True,'checks':len(checks),'certificate':str(p)}))
