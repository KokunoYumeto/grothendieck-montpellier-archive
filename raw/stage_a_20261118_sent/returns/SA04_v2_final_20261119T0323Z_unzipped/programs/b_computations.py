"""Exact checks for cote93 scans73–91 and explicitly attributed earlier-run ideas.
No visual reading is selected by this program. Algebraic identities are certificates;
finite enumeration is a diagnostic, not the arbitrary-ring proof in proof_checks.md.
"""
import sympy as s
import itertools,json,math
from pathlib import Path
t,n,r,m=s.symbols('t n r m',nonzero=True)
f=s.Function('f')(t);g=s.Function('g')(t);h=s.Function('h')(t);lam=s.Function('lambda')(t)
out={}
def check(k,x):
    v=s.simplify(x);out[k]=str(v);assert v==0,(k,v)
def cn(F,N):
    N=s.sympify(N)
    return -2*s.diff(F,t,2)/(N*F)+(2*N+1)/N**2*(s.diff(F,t)/F)**2
def G(F):return -2*s.diff(F,t,3)/s.diff(F,t)+3*(s.diff(F,t,2)/s.diff(F,t))**2
check('cn_from_horizontal_connection',2*s.diff(-s.diff(f,t)/(n*f),t)+(-s.diff(f,t)/(n*f))**2-cn(f,n))
check('tensor_power_cn',cn(f**r,n*r)-cn(f,n))
check('gamma_variation',2*s.diff(lam+h,t)+(lam+h)**2-(2*s.diff(lam,t)+lam**2)-2*(s.diff(h,t)+lam*h)-h**2)
check('gamma_beta1_d',cn(s.diff(f,t),1)-G(f))
check('delta_squared',cn(f**2,2)+f**2-(cn(f,1)+f**2))
check('exponential_correction',G(s.exp(f))-G(f)-s.diff(f,t)**2)
check('log_ratio_correct',((s.diff(g,t)/g)/(s.diff(f,t)/f))-(s.diff(g,t)/s.diff(f,t))*f/g)
out['wrong_ratio_test_f_t_g_t2']={'left':'2','printed':'2*t**2'}
out['wrong_second_term_test']={'m':1,'n':2,'f':'t','g':'t**2','correct_difference':str(s.simplify(cn(t**2,2)-cn(t,1))),'printed_difference':str(s.simplify(cn(t**2,2)-(-2*s.diff(t,t,2)/t+3*(s.diff(t**2,t)/t**2)**2)))}
out['horizontal_frame_sign_f_t_g_t2']={'Dg_minus_Df':'-dt/t','printed_dlog_ratio':'dt/t'}
out['arbitrary_power_test_G_t_t2']=str(G(t**2))
out['reciprocal_map']={'derivative':str(s.diff(t+1/t,t)),'critical_points':['1','-1'],'h_nonzero_not_enough':'h=2 forces f=1; non-etale'}
out['genus_count']='g+1+(3*g-3)=4*g-2, assuming smooth proper geometrically connected curve, g>=2'
e=s.Matrix([[0,1],[0,0]]);hh=s.Matrix([[1,0],[0,0]]);ff=s.Matrix([[0,0],[1,0]]);I=s.eye(2)
def br(a,b):return a*b-b*a
def coords(a):return s.Matrix([a[0,1],a[0,0]-a[1,1],a[1,0]])
basis=[e,hh,ff]
ad=[s.Matrix.hstack(*(coords(br(x,y)) for y in basis)) for x in basis]
K=s.Matrix(3,3,lambda i,j:s.trace(ad[i]*ad[j]))
out['pgl2_brackets']={f'{i},{j}':str(coords(br(basis[i],basis[j])).T) for i in range(3) for j in range(i+1,3)}
out['Killing_matrix']=str(K);out['Killing_det']=str(K.det());assert K.det()==-32
a,b,c=s.symbols('a b c');A=s.simplify(a*ad[0]+b*ad[1]+c*ad[2]);out['connection_ad_matrix']=str(A)
assert A==s.Matrix([[b,-a,0],[-2*c,0,2*a],[0,c,-b]])
H=s.diag(1,-1);out['sl2_brackets']=[str(br(e,H)),str(br(ff,H)),str(br(e,ff))]
u=s.symbols('u');T=s.Matrix([[1,u],[0,1]])
out['upper_triangular_transition']=str(s.Matrix.hstack(*(coords(T*x*T.inv()) for x in basis)))
D=s.Matrix([[0,0,0],[0,0,0],[1,0,0]])
def bvec(x,y):return sum((x[i]*ad[i]*y for i in range(3)),s.zeros(3,1))
for i in range(3):
 for j in range(3):
  x=s.eye(3)[:,i];y=s.eye(3)[:,j]
  diff=D*bvec(x,y)-bvec(D*x,y)-bvec(x,D*y)
  assert all(int(z)%2==0 for z in diff)
out['char2_outer_derivation']='D(e)=f,D(h)=D(f)=0 satisfies derivation identities mod2; all inner maps send e into span(e,h), so D is outer.'
out['char2_automorphisms']='W=<e,f> abelian, [h,w]=w; (A,v) in GL(W) semidirect W gives h->h+v,w->Aw: dimension6.'
out['transverse_factor']='c12=-2*c; c23=c; c12=-2*c23'
x=s.symbols('x0:9'); generic=s.Matrix(3,3,x)
eq=[]
for i in range(3):
 for j in range(i+1,3):
  ei=s.eye(3)[:,i];ej=s.eye(3)[:,j]
  eq.extend(generic*bvec(ei,ej)-bvec(generic*ei,ej)-bvec(ei,generic*ej))
sol=s.linsolve(eq,x)
out['all_derivations_when_2_invertible']=str(sol)
solution=list(sol)[0]
expected=A.subs({a:-solution[1],b:solution[0],c:solution[7]})
assert s.Matrix(3,3,solution)==expected
out['derivation_scope']='Linear solution uses division only by2; valid over a commutative base with2 invertible. It is not the characteristic2 solution.'
out['jet_rank']='H0(P1,O(1)) rank2; H0(O(1)|sigma) rank1; O(1)(-2sigma)=O(-1) has H0=H1=0'
def hd(v,j,p):return [((math.comb(k+j,j)*v[k+j])%p) if k+j<len(v) else 0 for k in range(len(v))]
def mul(x,y,p):
 q=len(x);return [sum(x[i]*y[k-i] for i in range(k+1))%p for k in range(q)]
for p,q in [(2,4),(3,9),(5,5)]:
 cnt=0
 for vv in itertools.product(range(p),repeat=q):
  if vv[1]==0:continue
  v=list(vv);d1,d2,d3=(hd(v,j,p) for j in [1,2,3])
  if all((x-y)%p==0 for x,y in zip(mul(d1,d3,p),mul(d2,d2,p))):cnt+=1
 out[f'nilpotent_diagnostic_F{p}_q{q}']={'solutions_Q0_unit_derivative':cnt,'homography_count':p*p*(p-1)}
 assert cnt==p*p*(p-1)
 out[f'binomial_units_p{p}_q{q}']=[math.comb(d,3)%p for d in range(3,q)]
 assert all(out[f'binomial_units_p{p}_q{q}'])
out['determinant_one_counterexample_F5']={'map':'s=2t mod t^5','possible_determinants_mod_squares':[2,3],'square_classes':[1,4]}
out['cartier_nonadditivity_F2']={'psi_d_x_plus_y':'(x+y)(dx+dy)','psi_dx_plus_psi_dy':'x dx+y dy','defect':'x dy+y dx=d(xy) nonzero as a form, zero as a cohomology class'}
root=Path(__file__).resolve().parents[1]
text=json.dumps(out,ensure_ascii=False,indent=2)
(root/'outputs/b_computations.json').write_text(text+'\n')
print(text)
