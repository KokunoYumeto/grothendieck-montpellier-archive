"""Exact finite calculations supporting the manually proved claims in p1_proofs.md.

Finite sweeps are consistency checks, not proofs of universally quantified claims.
All arithmetic is integral or finite-ring arithmetic; no floating point is used.
"""
from pathlib import Path
from math import gcd, comb
from itertools import product
import json
from fractions import Fraction

OUT=Path(__file__).resolve().parents[1]/'outputs'
OUT.mkdir(exist_ok=True)
result={}

# Periodic resolution of F_l over Z/l^2: ker(l)=im(l), with l^2=0.
rows=[]
for ell in (2,3,5,7):
    modulus=ell**2
    kernel=[a for a in range(modulus) if ell*a%modulus==0]
    image=sorted({ell*a%modulus for a in range(modulus)})
    assert kernel==image and len(kernel)==ell
    rows.append({'ell':ell,'kernel':kernel,'image':image,
                 'tensor_differential_mod_ell':0,'Hom_differential_mod_ell':0,
                 'Tor_and_Ext_dimension_every_degree':1,
                 'two_term_complex_cohomology_cardinalities':[ell,ell],
                 'identity_supertrace_mod_ell_squared':0})
result['periodic_Tor_Ext']=rows

# Dual numbers (a,b)=a+b*epsilon over Q, epsilon^2=0.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
one,eps,zero=(1,0),(0,1),(0,0)
a=add(one,eps)
assert mul(eps,eps)==zero
assert mul(eps,a)==eps
trA=neg(a);trC=one;trB=zero
defect=add(add(trA,trC),neg(trB))
assert defect==(0,-1)
result['triangle_trace_counterexample']={
    'ring':'Q[epsilon]/epsilon^2','A':'R in degree 1',
    'B':'R --epsilon--> R in degrees 0,1','C':'R in degree 0',
    'endomorphisms':{'a':a,'b':one,'c':one},
    'first_square_defect_equals_d_times_h':eps,
    'h_A1_to_B0':one,'connecting_square_eps_times_a':mul(eps,a),
    'trA':trA,'trB':trB,'trC':trC,'trA_plus_trC_minus_trB':defect}

# Supertraces for finite graded diagonal matrices: multiplicativity and signs.
u={-2:[2,-3],0:[5],1:[7,11]};v={-1:[13],0:[17,-19],2:[23]}
def sgn(i): return 1 if i%2==0 else -1
tu=sum(sgn(i)*sum(d) for i,d in u.items())
tv=sum(sgn(j)*sum(d) for j,d in v.items())
tuv=sum(sgn(i+j)*a*b for i,di in u.items() for j,dj in v.items() for a in di for b in dj)
assert tuv==tu*tv
result['supertrace_tensor']={'tr_u':tu,'tr_v':tv,'tr_tensor':tuv,'product':tu*tv}

# A finite sample of the purely formal cancellation Tr(dh)+Tr(hd)=0.
dims={i:(i+6)%4+1 for i in range(-3,4)}
cancel=[]
for i in range(-3,3):
    # Rectangular d_i and h_{i+1}; traces of d_i h and h d have the same sum.
    d=[[2+r-3*c for c in range(dims[i])] for r in range(dims[i+1])]
    h=[[5+2*r+c for c in range(dims[i+1])] for r in range(dims[i])]
    dh=sum(d[r][c]*h[c][r] for r in range(dims[i+1]) for c in range(dims[i]))
    hd=sum(h[r][c]*d[c][r] for r in range(dims[i]) for c in range(dims[i+1]))
    assert dh==hd
    signed=sgn(i+1)*dh+sgn(i)*hd
    assert signed==0
    cancel.append({'degree':i,'tr_dh':dh,'tr_hd':hd,'signed_sum':signed})
result['homotopy_supertrace_cancellation']=cancel

# Artin-Schreier mixed-monomial orbit: highest term obstruction.
# For arbitrary characteristic-p coefficients, the recurrence is
# -h_0=1; h_{r-1}^p-h_r=0; h_N^p=0, incompatible in a field.
as_rows=[]
for p in (2,3,5):
    for N in range(0,5):
        h=[(-1)%p]
        for i in range(1,N+1):h.append(pow(h[-1],p,p))
        terminal=pow(h[-1],p,p)
        assert terminal!=0
        as_rows.append({'p':p,'max_orbit_index':N,'required_coefficients':h,
                        'unwanted_terminal_coefficient':terminal,
                        'terminal_monomial':[p**(N+1),p**(N+1)]})
result['Artin_Schreier_xy_orbit_check']=as_rows

# The cohomological and homological intervals in scan 142 agree.
amp=[]
for a,b,d in [(-3,1,0),(-2,4,1),(0,0,3),(2,5,2)]:
    N,M=-b,-a
    hom=(N-2*d,M);coh=(-hom[1],-hom[0])
    assert coh==(a,b+2*d)
    amp.append({'input_cohomological':[a,b],'relative_dimension':d,
                'input_homological':[N,M],'output_homological':hom,'output_cohomological':coh})
result['Tor_amplitude_conversion']=amp

# Count monomials in n variables of total degree <s, including s=0.
mon=[]
for n in range(1,6):
    for s in range(0,7):
        count=sum(sum(e)<s for e in product(range(s),repeat=n)) if s else 0
        formula=comb(n+s-1,n) if s else 0
        assert count==formula
        mon.append({'n':n,'s':s,'count':count,'binomial':formula})
result['regular_local_length_binomial']=mon

# Finite differences of n^d recover d!; tests leading-coefficient calculation.
fd=[]
for d in range(0,8):
    for n in (8,11):
        delta=sum((-1)**i*comb(d,i)*(n-i)**d for i in range(d+1))
        fact=1
        for j in range(1,d+1):fact*=j
        assert delta==fact
        fd.append({'degree':d,'n':n,'difference':delta})
result['Hilbert_Samuel_leading_coefficient']=fd

def primes(n):
    ans=[];p=2
    while p*p<=n:
        if n%p==0:
            ans.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ans.append(n)
    return ans
count=0;examples=[]
for m in range(1,301):
    for n in range(1,m+1):
        if m%n:continue
        for u in range(n):
            if gcd(u,n)!=1:continue
            v=n
            for p in primes(m):
                if u%p:v*=p
            w=u+v
            assert gcd(w,m)==1 and (w-u)%n==0
            count+=1
            if (m,n,u) in [(12,4,3),(30,5,2),(60,12,5)]:
                examples.append({'m':m,'n':n,'u':u,'v':v,'w':w})
result['cyclic_generator_lifting']={'finite_cases_checked':count,'maximum_group_order':300,'examples':examples}

# Every nonzero binary quadratic over F_2 has a nonzero value on P^1(F_2).
quad=[]
for a,b,c in product(range(2),repeat=3):
    if (a,b,c)==(0,0,0):continue
    vals=[(a*x*x+b*x*y+c*y*y)%2 for x,y in [(1,0),(0,1),(1,1)]]
    assert any(vals)
    quad.append({'coefficients':[a,b,c],'values_on_projective_line':vals})
result['finite_field_nontangent_direction']=quad

# A flat finitely presented algebra with separable residue field but non-etale fibre.
# Q[e]/e^2 has vector-space basis 1,e. The relation contributes d(e^2)=2e de,
# so Omega has basis de after imposing e de=0 and is nonzero.
result['residue_only_etale_counterexample']={
    'base':'Q','algebra':'Q[e]/(e^2)','base_module_rank':2,
    'presentation_relations':['e^2'],'residue_extension_degree':1,
    'module_of_differentials':'(Q[e]/e^2)/(e) de = Q de',
    'differential_dimension_over_Q':1,'is_etale':False}

# Coefficients of -t D'(t)/D(t) equal the power traces for D=det(1-tF).
# F has eigenvalues 2,-3,5, giving exact rational/integer arithmetic.
eigenvalues=[2,-3,5]
D=[1]
for a in eigenvalues:
    nxt=[0]*(len(D)+1)
    for i,c in enumerate(D):nxt[i]+=c;nxt[i+1]-=a*c
    D=nxt
inverse=[Fraction(1)]
for n in range(1,11):
    inverse.append(-sum(Fraction(D[j])*inverse[n-j] for j in range(1,min(n,len(D)-1)+1)))
series=[]
for n in range(1,11):
    coeff=-sum(Fraction(j*D[j])*inverse[n-j] for j in range(1,min(n,len(D)-1)+1))
    trace=sum(a**n for a in eigenvalues)
    assert coeff==trace
    series.append({'power':n,'trace':trace,'coefficient':str(coeff)})
result['determinant_trace_series']={'eigenvalues':eigenvalues,'determinant_coefficients':D,'checks':series}

# Compatible traces under reduction of the same finite-projective model.
adic=[]
integer_trace=-17+23-41
for ell in [2,3,5]:
    residues=[integer_trace%(ell**r) for r in range(1,9)]
    assert all(residues[r]%(ell**r)==residues[r-1] for r in range(1,8))
    adic.append({'ell':ell,'integer_supertrace':integer_trace,'residues_mod_ell_powers':residues})
result['adic_trace_compatibility']=adic

# The zero object's intrinsic trace is zero; this termwise infinite sum has no limit.
partial=[sum((-1)**j for j in range(n)) for n in range(1,13)]
assert set(partial)=={0,1}
result['unbounded_termwise_trace_warning']={'partial_sums':partial,'intrinsic_trace_of_contractible_object':0}

dest=OUT/'p1_computations.json'
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for k,v in result.items():
    print(k+': '+(str(len(v))+' rows' if isinstance(v,list) else json.dumps(v,ensure_ascii=False)))
print('All exact finite consistency checks passed. Universal arguments are in shards/p1/proofs.md.')
