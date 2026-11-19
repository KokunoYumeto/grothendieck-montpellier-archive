"""Exact symbolic and finite-field checks for SA04.

The certificates are deliberately distinguished from general proofs in
parts/root_computation_notes.md. No numerical floating-point evidence is used.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, math
import sympy as S

OUT={"run_utc":datetime.now(timezone.utc).isoformat(),"engine":"Python3; SymPy exact rational/integer polynomial arithmetic"}
a1,a2,a3,a4,a6,u,r,s,t,x,y,lam=S.symbols('a1 a2 a3 a4 a6 u r s t x y lambda')
aa=[a1,a2,a3,a4,a6]
def invs(a):
    a1,a2,a3,a4,a6=a
    b2=a1*a1+4*a2;b4=a1*a3+2*a4;b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    d6=b2*b4-18*b6;d8=b2*b2*b4-48*b4*b4+18*b2*b6
    c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
    delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return [b2,b4,b6,b8,d6,d8,c4,c6,delta]
b2,b4,b6,b8,d6,d8,c4,c6,delta=invs(aa)
basechecks={
 "b2b6-b4^2=4b8":S.expand(b2*b6-b4*b4-4*b8)==0,
 "12d6=c6+b2c4":S.expand(12*d6-c6-b2*c4)==0,
 "-12d8=c4^2+b2c6":S.expand(-12*d8-c4*c4-b2*c6)==0,
 "1728Delta=c4^3-c6^2":S.expand(c4**3-c6**2-1728*delta)==0,
 "alternative_Delta":S.expand(delta-(b4**3-27*b6*b6+b8*(36*b4-b2*b2)))==0,
}
apr=[(a1+2*s)/u,(a2-s*a1+3*r-s*s)/u**2,(a3+r*a1+2*t)/u**3,
 (a4-s*a3+2*a2*r-(t+r*s)*a1+3*r*r-2*s*t)/u**4,
 (a6+r*a4+r*r*a2+r**3-t*a3-t*t-r*t*a1)/u**6]
F=y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6
Fp=y*y+apr[0]*x*y+apr[2]*y-x**3-apr[1]*x*x-apr[3]*x-apr[4]
basechecks['all_coordinate_coefficients']=S.expand(F.subs({x:u*u*x+r,y:u**3*y+s*u*u*x+t},simultaneous=True)-u**6*Fp)==0
basechecks['a4_rhs_requires_F_x']=S.expand(u**4*apr[3]+S.diff(F,x).subs({x:r,y:t})+s*S.diff(F,y).subs({x:r,y:t}))==0
expected=[b2+12*r,b4+r*b2+6*r*r,b6+2*r*b4+r*r*b2+4*r**3,
 b8+3*r*b6+3*r*r*b4+r**3*b2+3*r**4,d6+c4*r,d8-c6*r,c4,c6,delta]
for name,wt,v,e in zip(['b2','b4','b6','b8','d6','d8','c4','c6','Delta'],[2,4,6,8,6,8,4,6,12],invs(apr),expected):
    basechecks['transformation_'+name]=S.expand(u**wt*v-e)==0
assert all(basechecks.values())
leg=invs([0,-1-lam,0,lam,0]);legj=S.factor(leg[-3]**3/leg[-1])
basechecks['Legendre_j']=S.cancel(legj-256*(1-lam+lam*lam)**3/(lam*lam*(1-lam)**2))==0
hasse=[]
for p in [3,5,7,11,13,17,19]:
    rr=(p-1)//2
    coeff=S.Poly((x*(x-1)*(x-lam))**rr,x).coeff_monomial(x**(p-1))
    formula=(-1)**rr*sum(math.comb(rr,i)**2*lam**i for i in range(rr+1))
    ok=S.expand(coeff-formula)==0;assert ok
    hasse.append({'p':p,'coefficient':str(S.expand(coeff)),'exact_integer_identity':ok})
OUT['weierstrass']={'identities':basechecks,'Legendre_j':str(legj),'Hasse_coefficient_checks':hasse}

N=16
def mul(a,b):
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]
def power(a,n):
    b=[1]+[0]*N
    for _ in range(n):b=mul(a,b)
    return b
def sigma(n,k):return sum(d**k for d in range(1,n+1) if n%d==0)
e4=[1]+[240*sigma(n,3) for n in range(1,N+1)]
e6=[1]+[-504*sigma(n,5) for n in range(1,N+1)]
qprod=[1]+[0]*N
for n in range(1,N+1):
    f=[0]*(N+1)
    for j in range(min(24,N//n)+1):f[n*j]=(-1)**j*math.comb(24,j)
    qprod=mul(qprod,f)
qdelta=[0]+qprod[:-1]
qdifference=[a-b-1728*c for a,b,c in zip(power(e4,3),power(e6,2),qdelta)]
assert not any(qdifference)
OUT['q_series']={'precision':f'mod q^{N+1}, finite check only','E4':e4,'E6':e6,'Delta':qdelta,'identity_difference':qdifference}

z=S.symbols('z');f=S.Function('f')(z);g=S.exp(f)
def G(h):return -2*S.diff(h,z,3)/S.diff(h,z)+3*(S.diff(h,z,2)/S.diff(h,z))**2
diff=S.simplify(G(g)-G(f)-S.diff(f,z)**2)
assert diff==0
OUT['Schwarzian_exponential']={'G(exp(f))-G(f)-(fprime)^2':str(diff),'G':'-2 hthird/hprime+3(hsecond/hprime)^2','hypothesis':'fprime nonzero; characteristic0 differential ring'}

pair=[];jac=[]
for p in [2,3,5,7,11,13,17,19]:
    M=S.Matrix([[j%p if i+j==p else 0 for j in range(1,p)] for i in range(1,p)])
    determinant=int(M.det())%p
    formula=((-1)**((p-1)*(p-2)//2)*math.factorial(p-1))%p
    assert determinant==formula and determinant!=0
    pair.append({'p':p,'matrix':[[int(v) for v in row] for row in M.tolist()],'determinant_mod_p':determinant,'formula_mod_p':formula,'manuscript_plus_one':determinant==1})
    if p<=7:
        D=S.zeros(p);X=S.zeros(p)
        for i in range(1,p):D[i-1,i]=i
        for i in range(p-1):X[i+1,i]=1
        tests=[]
        for coeffs in [[int(i==j) for i in range(p)] for j in range(p)]+[[i+1 for i in range(p)]]:
            C=sum((coeffs[i]*(X**i) for i in range(p)),S.zeros(p))
            derivconst=coeffs[p-1]*math.factorial(p-1)
            residual=((D+C)**p-D**p-C**p-derivconst*S.eye(p)).applyfunc(lambda q:int(q)%p)
            ok=residual==S.zeros(p);assert ok
            tests.append({'c_coefficients_mod_p':[v%p for v in coeffs],'identity':ok})
        jac.append({'p':p,'ring':'Fp[x]/(x^p)','tests':tests})
OUT['Cartier']={'p2_additivity_defect':{'dx_coefficient':'y','dy_coefficient':'x','equals':'d(x*y), nonzero in Omega1(F2[x,y])'},'pairing':pair,'Jacobson_finite_certificates':jac}

class GF2:
    def __init__(self,n,poly):self.n=n;self.q=1<<n;self.poly=poly
    def add(self,a,b):return a^b
    def mul(self,a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.poly
        return r
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def eval(self,c,a):
        r=0
        for b in c[::-1]:r=self.mul(r,a)^b
        return r
counts=[]
for n,poly in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011)]:
    k=GF2(n,poly);pts=[]
    for xx in range(k.q):
        h=k.eval([1,1,1],xx);ff=k.eval([1,0,1,1,0,1],xx)
        for zz in range(k.q):
            if k.mul(zz,zz)^k.mul(h,zz)^ff==0:pts.append([xx,zz])
    counts.append({'n':n,'field_modulus_bits':poly,'affine_points':pts,'point_at_infinity':1,'N':len(pts)+1})
assert [c['N'] for c in counts]==[3,7,9,31]
T=S.symbols('T');N1,N2=counts[0]['N'],counts[1]['N'];q=2
c1=N1-q-1;c2=(N2-q*q-1+c1*c1)//2
P=1+c1*T+c2*T*T+q*c1*T**3+q*q*T**4
h=x*x+x+1;ff=x**5+x**3+x*x+1
assert S.Poly(ff-x*h*h-h,x,modulus=2).is_zero
smooth=S.rem(S.diff(ff,x),h,domain=S.GF(2))
assert smooth==1
OUT['genus2_counterexample']={'equation':'z^2+(x^2+x+1)z=x^5+x^3+x^2+1','counts':counts,'P(T)':str(P),'P_mod2':str(S.Poly(P,T,modulus=2).as_expr()),'P(1)':int(P.subs(T,1)),'affine_smoothness_fprime_mod_h':str(smooth),'Artin_Schreier_form':'y^2+y=x+1/(x^2+x+1), z=(x^2+x+1)*y','poles':'three geometric simple poles; genus=(-4+3*2+2)/2=2','conclusion':'#J(F2)=6 => dim_F2 J(F2)[2]=1; root1 of Pmod2 has algebraic multiplicity2'}

k=GF2(2,0b111)
autos=[]
for uu in range(1,4):
 for ss in range(4):
  rr=k.pow(ss,2)
  for tt in range(4):
   if k.pow(uu,3)==1 and (k.pow(tt,2)^tt)==k.pow(rr,3):autos.append((uu,rr,ss,tt))
def compose(a,b):
    u,r,s,t=a;v,rp,sp,tp=b
    return (k.mul(u,v),r^k.mul(k.pow(u,2),rp),s^k.mul(u,sp),t^k.mul(k.pow(u,3),tp)^k.mul(k.mul(s,k.pow(u,2)),rp))
eid=(1,0,0,0)
orders={}
for a in autos:
 b=eid
 for i in range(1,25):
  b=compose(b,a)
  if b==eid:orders[str(a)]=i;break
assert len(autos)==24 and all(compose(a,b) in autos for a in autos for b in autos)
kernel=[a for a in autos if a[0]==1]
assert sorted(orders[str(a)] for a in kernel)==[1,2,4,4,4,4,4,4]
OUT['elliptic_aut_char2']={'curve':'y^2+y=x^3 over F4','automorphisms':autos,'orders':orders,'count':24,'u1_kernel_orders':[orders[str(a)] for a in kernel],'kernel_identification':'Q8: order8 with unique involution and six elements of order4; u gives split quotient C3','full_law':'(u,r,s,t)*(v,rp,sp,tp)=(uv,r+u^2rp,s+u sp,t+u^3tp+s u^2rp)'}
OUT['elliptic_aut_char3']={'curve':'y^2=x^3-x','equations':'s=t=0, u^4=1, r^3=r','count_over_F9':'4*3=12','proof':'roots of u^4-1 distinct in F9, roots of r^3-r are 0,+1,-1; coordinate formulas above show necessity and sufficiency'}

out=Path(__file__).resolve().parents[1]/'outputs/root_computations.json'
out.write_text(json.dumps(OUT,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':str(out),'checks':'all exact assertions passed','Weierstrass_identity_count':len(basechecks),'finite_field_counts':[c['N'] for c in counts],'pairing_determinants':[(a['p'],a['determinant_mod_p']) for a in pair],'elliptic_char2_aut_count':len(autos)},indent=2))
with (out.parents[1]/'progress.log').open('a') as log:log.write(f"{OUT['run_utc']}\tcomputation\troot_computations.py; all assertions passed; outputs/root_computations.json\n")
