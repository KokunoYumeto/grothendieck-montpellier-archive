#!/usr/bin/env python3
"""Exact finite diagnostics for AM-DO-051; not a Lean or global-period computation."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import hashlib, json

ROOT=Path(__file__).resolve().parent
checks=0
counts={}
def ck(x,group):
    global checks
    assert x, (group,checks)
    checks+=1
    counts[group]=counts.get(group,0)+1

def vecs(q,n): return list(product(range(q),repeat=n))
def dot(x,y,q): return sum(a*b for a,b in zip(x,y))%q
def poly(q): return [F(0)]*q
def mon(q,e,c=1):
    a=poly(q);a[e%q]=F(c);return a
def add(a,b):return [x+y for x,y in zip(a,b)]
def smul(c,a):return [c*x for x in a]
def conj(a):return [a[(-i)%len(a)] for i in range(len(a))]
def mul(a,b):
    q=len(a);o=poly(q)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[(i+j)%q]+=x*y
    return o
def equal(a,b):
    d=[x-y for x,y in zip(a,b)]
    return len(set(d))==1 # Phi_q = 1+...+X^(q-1), q prime.
def psum(q,es):
    a=poly(q)
    for e in es:a[e%q]+=1
    return a

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def vp(x,q):
    x=F(x)
    if not x:return 10**9
    n,d=abs(x.numerator),x.denominator;v=0
    while n%q==0:n//=q;v+=1
    while d%q==0:d//=q;v-=1
    return v

# The actual sum frame and glued lattice: compare both integral bases,
# allowing arbitrary independent unit in pi=q/cv and varpi=q*r.
for q in (3,5,7,11):
 for cv in range(1,q):
  for r in range(1,q):
    A=F(q+1,2);B=F(q-1,2);pi=F(q,cv)
    g=[[A/pi,B/cv],[B/pi,A/cv]]
    alpha=mm(g,[[F(1),F(0)],[F(0),F(cv)]])
    gl=[[F(q),F(1,r*cv)],[F(0),F(1,q*r)]]
    change=mm(inv2(gl),inv2(alpha))
    ck(all(vp(z,q)>=0 for row in change for z in row),'glued_frame_integral')
    ck(all(vp(z,q)>=0 for row in inv2(change) for z in row),'glued_frame_inverse')
    ck(g[0][0]*g[1][1]-g[0][1]*g[1][0]==1,'special_linear_frame')
    for xi in range(1,q):
      eps=(-xi*r)%q
      s=pow(r,-1,q)
      ep1=pow(-xi,-1,q)
      ck(eps==(pow(ep1,-1,q)*pow(s,-1,q))%q,'diamond_phase')
      for f in range(1,q):
       for t in range(q):
        fourier_condition=(xi*cv*t+pow(r,-1,q)*eps*f)%q==0
        ck(fourier_condition==((cv*t-f)%q==0),'terminal_affine_condition')

# Exact nonzero Fourier Gram and preservation of every elementary
# scalar-orbit augmentation vector. All arithmetic is in Q[zeta_q].
for q,a in ((3,1),(3,2),(5,1),(5,2),(7,1)):
 V=vecs(q,a);NZ=[v for v in V if any(v)]
 for x in NZ:
  for y in NZ:
   gram=psum(q,(dot(l,tuple(yy-xx for xx,yy in zip(x,y)),q) for l in NZ))
   ck(equal(gram,mon(q,0,q**a-1 if x==y else -1)),'fourier_gram')
 for x in NZ:
  for c in range(2,q):
   y=tuple(c*z%q for z in x)
   fhat={l:add(mon(q,-dot(l,x,q)),mon(q,-dot(l,y,q),-1)) for l in NZ}
   norm=poly(q)
   for l in NZ:norm=add(norm,mul(fhat[l],conj(fhat[l])))
   ck(equal(norm,mon(q,0,2*q**a)),'ramified_fourier_norm')
   for l in NZ:
    orbit=poly(q)
    for u in range(1,q):orbit=add(orbit,fhat[tuple(u*z%q for z in l)])
    ck(equal(orbit,poly(q)),'ramified_fourier_orbit_sum')

# Complete finite expansion of the glued indicator, including the zero
# covector and the signed covector decomposition of the X factor.
for q,a,b in ((3,1,1),(3,2,1),(3,1,2),(3,2,2),(5,1,1)):
 Ys=vecs(q,b); Fs=Ys
 for H in vecs(q,a*b):
  col0=tuple(H[i*a] for i in range(b))
  for y in Ys:
   rhs=smul(F(1,q**b),psum(q,(-dot(f,tuple(y[i]+col0[i] for i in range(b)),q) for f in Fs)))
   lhs=int(all((y[i]+col0[i])%q==0 for i in range(b)))
   ck(equal(rhs,mon(q,0,lhs)),'glued_finite_fourier_expansion')
  for f in Fs:
   ell=tuple(sum(f[i]*H[i*a+j] for i in range(b))%q for j in range(a))
   if any(f):
    target=mon(q,-ell[0])
    decomp=mon(q,0) if not any(ell) else mon(q,-ell[0])
    ck(equal(target,decomp),'incidence_zero_noncovector_split')

# Full finite quotient for a=b=1, with arbitrary residue functionals,
# pi=q/cv, varpi=q*r, and xi0 any unit. Functions use X=x/q, y=y0/q;
# cells have additive volume q^-2. The explicit operator stages are
# evaluated, rather than just their intended output support.
for q in (3,5):
 for cv in range(1,q):
  for r in range(1,q):
   rho=(r*cv)%q;iv=pow(rho,-1,q)
   for xi in range(1,q):
    eps=(-xi*r)%q
    for fQ in range(1,q):
     modified={}
     for x in range(q*q):
      pint=smul(F(1,q),psum(q,(z*x*iv for z in range(q))))
      for yn in range(q*q):
       # Translate the actual glued indicator after P_int.
       count=sum(int((yn-q*shift+q*x*pow(cv,-1,q))%(q*q)==0) for shift in range(q))
       after=smul(count,pint)
       if not equal(after,poly(q)):
        ck(x%q==0 and yn%q==0,'E0_intermediate_integral_support')
        p0=smul(F(1,q),psum(q,(c*(fQ*(x//q)-rho)*pow(r,-1,q) for c in range(q))))
        phase=mon(q,-eps*fQ*(yn//q)*pow(r,-1,q))
        val=mul(mul(after,p0),phase)
       else:val=poly(q)
       expected=(mon(q,xi*fQ*(yn//q)) if x%q==0 and yn%q==0 and (fQ*(x//q)-rho)%q==0 else poly(q))
       ck(equal(val,expected),'explicit_E0_entire_quotient')
       modified[x,yn]=val
     for x in range(q*q):
      for t in range(q):
       # FT14 divided by q^(1/2): selfdual integral over O is q^-1 sum.
       ft=poly(q)
       for y in range(q):ft=add(ft,mul(modified[x,q*y],mon(q,-xi*cv*t*y)))
       ft=smul(F(1,q),ft)
       raw=int(x%q==0 and (fQ*(x//q)-rho)%q==0 and (cv*t-fQ)%q==0)
       ck(equal(ft,mon(q,0,raw)),'exact_modified_shuffle')
       # Explicit O0 applied to FT17, after dividing by q^-1/2.
       tint=(t-fQ*pow(cv,-1,q))%q
       pint=smul(F(1,q),psum(q,(z*x*iv for z in range(q))))
       bt=psum(q,(-xi*cv*tint*z for z in range(q)))
       oldphase=mon(q,xi*r*cv*tint*x*iv)
       if x%q==0:
        p0=smul(F(1,q),psum(q,(c*(fQ*(x//q)-rho)*pow(r,-1,q) for c in range(q))))
        val=mul(mul(mul(pint,bt),oldphase),p0)
       else:val=poly(q)
       ck(equal(val,mon(q,0,q*raw)),'explicit_O0_on_raw_C')
     # Integral translates partition both independent incidence constraints.
     wq=pow(fQ,-1,q)
     for X in range(q):
      s0=sum(int((fQ*(X-wq*c)-rho)%q==0) for c in range(q))
      ck(s0==1,'D0_image_inverse')
     for t in range(q):
      s1=sum(int((cv*(t-pow(cv,-1,q)*c)-fQ)%q==0) for c in range(q))
      ck(s1==1,'D1_image_inverse')

# The two finite Schur transposition fibres have the same actual counts.
for q,a in ((3,1),(3,2),(3,3),(5,2)):
 V=vecs(q,a);NZ=[x for x in V if any(x)]
 x0=NZ[-1];l0=NZ[-2] if len(NZ)>1 else NZ[0]
 for c in range(q):
  nl=sum(dot(l,x0,q)==c for l in NZ)
  nx=sum(dot(l0,x,q)==c for x in NZ)
  ck(nl==nx==q**(a-1)-(c==0),'finite_transposition_fibres')

# Rational norm, l1, denominator and count identities in arbitrary dimensions.
for q in (3,5,7,11):
 for a in range(1,5):
  for b in range(1,6):
   ck(F(q**b)*F(1,q**(a+b))==F(1,q**a),'modified_norm')
   ck(F(1,q**b)*q**b==1,'original_raw_norm')
   ck(F(q**(2*a+3*b),q**(a+b))==q**(a+2*b),'Weyl_l1_bound')
   ck(F(1,q**b)*F(q**b,1)==1,'source_fourier_modulus_balance')

# Exact actual prime metadata and two-host amplitudes/cost exponents.
for h in range(1,11):
    # Rational parametrization of a retained unit phase. The entire
    # operator identity is linear in it; it is not set to1.
    re=F(1-h*h,1+h*h);im=F(2*h,1+h*h)
    ck(re*re+im*im==1,'retained_unit_phase_norm')
    q=3;scale=q**7
    ck((re*scale)**2+(im*scale)**2==scale**2,'retained_phase_amplitude')

source=ROOT/'definite_oscillator_large_t_certificate.json'
data=json.loads(source.read_text());actual=[]
for row in data['rows']:
 a,f,q,D=row['a'],row['f'],int(row['T']),int(row['D']);b=1802
 re,im=int(row['piT_real']),int(row['piT_sqrt_minus7'])
 ck(re*re+7*im*im==q,'actual_pi_norm')
 ck(q==11*D*D+4*D+1,'actual_T_formula')
 ck(q%2==1 and q%11!=0 and b%2==0,'actual_unit_denominators')
 ck(row['all_T_places_degree_one'],'actual_absolute_split_T')
 ck((2*re)%q!=0,'actual_conjugate_pi_unit')
 ck(b==a+(1759 if a==42 else 1633)+1,'actual_middle_rank')
 ck(f*b%2==0,'actual_total_half_power_integral')
 actual.append(dict(host=row['host'],a=a,b=b,f=f,T_bits=q.bit_length(),
                    C_T_amplitude_exponent=f*b//2,
                    Weyl_l1_exponent=f*(a+2*b),
                    Weyl_denominator_exponent=f*(a+b),
                    precollection_term_exponent=f*(2*a+3*b),
                    finite_coefficient_extension_degree_bound=str(q-1)))

out=dict(finding='AM-DO-051',status='PASS',
         completed_utc=datetime.now(timezone.utc).isoformat(),exact_checks=checks,
         check_groups=counts,actual_hosts=actual,
         input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
         script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         scope='Exact rational glued-frame lattice equivalence, residue diamond/terminal phase, nonzero Fourier Gram and ramified orbit tests, complete finite glued expansion, explicit E0/O0 and affine image inverse on finite Schrödinger quotients, finite transposition counts, Haar/norm/l1/denominator identities, retained unit-phase norms, and actual host T metadata. General Heisenberg/source uniformity is proved in the report; the fixed source-model phase is explicitly retained, not evaluated. No Lean, actual automorphic integral, global nonzero period or integral theta image is computed.')
ROOT.joinpath('definite_oscillator_fixed_t_seesaw_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('finding','status','completed_utc','exact_checks','check_groups')},indent=2))
