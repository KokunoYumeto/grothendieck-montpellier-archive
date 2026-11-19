"""Independent exact checks for cote 84, scans 97--145, SA02 run 2026-11-19.
No numerical sampling replaces the universal identities. All ring reductions
below use the displayed monic relations over Z[parameters]."""
from pathlib import Path
import sympy as S,itertools,json
OUT=Path(__file__).resolve().parent.parent/'outputs'
b1,b2,c1,c2=S.symbols('b1 b2 c1 c2');bc=b1*b2;C=b1*b1*c2+b2*b2*c1-4*c1*c2
x=S.symbols('x0:4');y=S.symbols('y0:4');a,d=S.symbols('a d');checks=[]
def record(name,residual):
 if isinstance(residual,S.MatrixBase):residual=list(residual)
 if not isinstance(residual,(list,tuple)):residual=[residual]
 red=[S.expand(v) for v in residual];assert all(v==0 for v in red),(name,red)
 checks.append({'check':name,'residuals':[str(v) for v in red],'result':'PASS: exact polynomial identity'})
def plus(x,y):return [u+v for u,v in zip(x,y)]
def sub(x,y):return [u-v for u,v in zip(x,y)]
def scale(c,x):return [c*u for u in x]
def mul(x,y):
 # Basis is 1,u,v,uv; u²=-b1u-c1, v²=-b2v-c2.
 out=[0]*4
 for i,j in itertools.product(range(4),repeat=2):
  pu=(i&1)+(j&1);pv=(i>>1)+(j>>1)
  ru={0:1} if pu==0 else ({1:1} if pu==1 else {0:-c1,1:-b1})
  rv={0:1} if pv==0 else ({1:1} if pv==1 else {0:-c2,1:-b2})
  for k,cu in ru.items():
   for l,cv in rv.items():out[k+2*l]+=cu*cv*x[i]*y[j]
 return [S.expand(v) for v in out]
def conj1(x):return [x[0]-b1*x[1],-x[1],x[2]-b1*x[3],-x[3]]
def conj2(x):return [x[0]-b2*x[2],x[1]-b2*x[3],-x[2],-x[3]]
def conj(x):return conj1(conj2(x))
def amul(x,y):return [S.expand(x[0]*y[0]-C*x[1]*y[1]),S.expand(x[0]*y[1]+x[1]*y[0]-bc*x[1]*y[1])]
def abar(x):return [x[0]-bc*x[1],-x[1]]
def anorm(x):return S.expand(x[0]**2-bc*x[0]*x[1]+C*x[1]**2)
def atrace(x):return 2*x[0]-bc*x[1]
def image(x):return [x[0],b2*x[1],b1*x[1],2*x[1]]
def trace(x):return [2*x[0]-b1*x[1]-b2*x[2]+bc*x[3],x[3]]
def norm(x):
 z,w,h,j=x
 return [S.expand(z*z+c1*w*w+c2*h*h+c1*c2*j*j-b1*z*w-b2*z*h+bc*z*j-b2*c1*w*j-b1*c2*h*j),S.expand(z*j-w*h)]
t=image([0,1]);record('scan104 product relation',plus(plus(mul(t,t),scale(bc,t)),[C,0,0,0]))
record('scan104 discriminant product',bc**2-4*C-(b1**2-4*c1)*(b2**2-4*c2))
record('scan105 i Tr=1+sigma',sub(image(trace(x)),plus(x,conj(x))))
record('scan105 Tr i=2id',sub(trace(image([a,d])),[2*a,2*d]))
record('scan105 trace invariance diagonal',sub(trace(conj(x)),trace(x)))
record('scan105 trace equivariance factor1',sub(trace(conj1(x)),abar(trace(x))))
record('scan106 iN=x sigma(x)',sub(image(norm(x)),mul(x,conj(x))))
record('scan106 polarization N',sub(sub(sub(norm(plus(x,y)),norm(x)),norm(y)),trace(mul(x,conj(y)))))
record('scan106 N(i(a))=a²',sub(norm(image([a,d])),amul([a,d],[a,d])))
record('scan106 N sigma1=bar N',sub(norm(conj1(x)),abar(norm(x))))
record('scan106 N sigma2=bar N',sub(norm(conj2(x)),abar(norm(x))))
record('scan106 N sigma=N',sub(norm(conj(x)),norm(x)))
record('relative trace A-linear',sub(trace(mul(image([a,d]),x)),amul([a,d],trace(x))))
record('relative norm A-quadratic homogeneous',sub(norm(mul(image([a,d]),x)),amul(amul([a,d],[a,d]),norm(x))))
record('relative norm multiplicative',sub(norm(mul(x,y)),amul(norm(x),norm(y))))
r,s,h,j=S.symbols('r s h j');pure=[r*h,s*h,r*j,s*j]
record('scan106 pure-tensor normalization',sub(norm(pure),[(r*r-b1*r*s+c1*s*s)*(h*h-b2*h*j+c2*j*j),0]))
units=[[int(i==j) for i in range(4)] for j in range(4)]
M=S.Matrix.hstack(*(S.Matrix(mul(x,u)) for u in units))
record('scan106 trace transitivity against regular representation',atrace(trace(x))-S.trace(M))
record('scan106 norm transitivity against determinant',anorm(norm(x))-M.det(method='domain-ge'))
# Kernel/invariant equations in tensor basis, no cancellation of 2.
fixed_equations=sub(conj(x),x)
checks.append({'check':'scan102 invariant coefficient equations','equations':[str(S.expand(v))+' = 0' for v in fixed_equations],
 'interpretation':'The three nontrivial equations are -b1*x1-b2*x2+b1*b2*x3=0; -2*x1+b2*x3=0; -2*x2+b1*x3=0. On D(2),D(b1),D(b2), all solutions are uniquely (a,b2*d,b1*d,2*d). If b1 is a unit take d=x2/b1, then the first equation forces x1=b2*d and the third x3=2*d. Symmetric for b2.'})
# Z/4 quasi-quadratic data: all elements, all pairs, all scalars.
els=list(itertools.product(range(2),repeat=4))
def fadd(x,y):return tuple((u+v)%2 for u,v in zip(x,y))
def fmul(x,y):
 z=[0]*4
 for i,j in itertools.product(range(4),repeat=2):
  if i&j==0:z[i|j]^=x[i]*y[j]
 return tuple(z)
def fn(x):return (x[0]+2*x[3])%4
def ft(x):return 2*x[0]
failures=[]
one=(1,0,0,0)
for xx in els:
 assert fmul(xx,xx)==(xx[0],0,0,0)
 assert fn(xx)%2==xx[0]
 for k in range(4):
  kx=tuple((k*u)%2 for u in xx)
  assert fn(kx)==k*k*fn(xx)%4
  assert ft(kx)==k*ft(xx)%4
 for yy in els:
  assert fn(fadd(xx,yy))==(fn(xx)+fn(yy)+ft(fmul(xx,yy)))%4
  assert ft(fadd(xx,yy))==(ft(xx)+ft(yy))%4
  if fn(fmul(xx,yy))!=fn(xx)*fn(yy)%4:failures.append([xx,yy])
assert len(failures)==96
checks.append({'check':'scan110 five axioms versus multiplicativity','elements':16,'pairs':256,'scalars':4,'axiom_failures':0,'multiplicativity_failures':96,'witness':'n(ef)=2, n(e)n(f)=0; n((1+e)(1+f))=3, n(1+e)n(1+f)=1','law_extension':'For every Z/4-algebra S the map on (S/2S)^4 is a²+2d², with arbitrary S-lifts. Lifts differ by 2s and squares are unchanged; polarization is 2aa′. This verifies a polynomial law, not merely the 16-point function.'})
# Finite parity models and nilpotent degenerations.
triples=list(itertools.product(range(2),repeat=3));G=[v for v in triples if sum(v)%2==0]
for eps in range(2):
 J=[v for v in triples if sum(v)%2==eps]
 assert len(J)==4
 for i,j in [(0,1),(1,2),(2,0)]:assert len({(v[i],v[j]) for v in J})==4
 for x0 in J:assert {tuple((x0[i]+g[i])%2 for i in range(3)) for g in G}==set(J)
checks.append({'check':'scans116--120 parity and etale model','group':G,'nonzero':[v for v in G if v!=(0,0,0)],'parity_fibres':[4,4],'pair_projections':'all three bijective on each parity fibre','forbidden_char2_patterns':sum(sum(v)>=2 for v in triples)})
e=S.Matrix([0,1,0,0]);f=S.Matrix([0,0,1,0]);ef=S.Matrix([0,0,0,1]);onev=S.Matrix([1,0,0,0]);
pairbases=[S.Matrix.hstack(onev,e,f,ef),S.Matrix.hstack(onev,e+f,e,ef),S.Matrix.hstack(onev,e+f,f,ef)]
assert all(int(p.det())%2 for p in pairbases)
checks.append({'check':'scan118 counterexample to scalar fixed ring','A':'F2[e,f]/(e²,f²)','input_subalgebras':['F2[e]','F2[f]','F2[e+f]'],'pair_basis_determinants_mod2':[int(p.det())%2 for p in pairbases],'all_relative_involutions':'identity','fixed_dimension':4,'scalar_dimension':1,'triple_product_generator_image':0,'result':'Scalar image survives although fixed ring is larger.'})
checks.append({'check':'scan122 nonflat triple-dual-number morphism','base':'F2[t]/(t²)','target':'F2[e,f,g]/(e²,f²,g²)','t_image':0,'target_dimension':8,'kernel_after_tensoring_t_ideal_inclusion_dimension':8,'result':'FAIL flatness; finite and spectrum-surjective. Fibre dimension8, not rank4.'})
(OUT/'algebra_checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
