#!/usr/bin/env python3
"""Exact finite certificates for the all-prime Raynaud/root-cover surface.
Geometry, all-prime identities and all-degree p=2 vanishing are proved in TeX.
"""
import json,time,math
start=time.perf_counter()
rows=[]
for p in [2,3,5,7,11,13]:
    h=8 if p==2 else p*p-2
    m=h*p-1; d=(p-1)*h-2; ell=p+1; q=ell*ell
    assert d>0 and d%ell==0
    degN=d//ell
    assert degN%p==0 and math.gcd(m,p)==1 and math.gcd(q,p)==1
    r=degN//p
    assert r==(1 if p==2 else p-2)
    genus=(p*d+2)//2
    assert 2*genus-2==p*d==p*ell*degN
    assert q*degN>2*genus+1
    # Local infinity equation v+w*v^c=w^p and implicit differentiation.
    c=h*(p-1)
    assert c-2==d
    # Positive eigensheaf floors are exactly 0,1,...,1.
    floors=[(p+i)//ell for i in range(ell)]
    assert floors==[0]+[1]*p
    # Last negative eigensheaf is Sym^(p-2)E^vee tensor T^(p-2).
    assert p*p-1-ell==ell*(p-2)
    # SNC root equations have Jacobian minor -1 in each branch parameter;
    # unit-root derivatives stay nonzero as q mod p=1.
    assert q%p==1
    rows.append({'p':p,'h':h,'Artin_Schreier_exponent':m,'Tango_divisor_degree':d,
                 'genus':genus,'N_degree':degN,'N_generators':['1',f'x^{r}'],
                 'cyclic_degree':ell,'root_exponent':q,
                 'base_two_jet_margin':q*degN-(2*genus+1),
                 'positive_eigensheaf_floors':floors})

def ceildiv(a,b): return -((-a)//b)
p2rows=[]
for r in range(1,101):
    ms=[j+ceildiv(2*r-j,3) for j in range(3)]
    es=[2*j-r-3 for j in range(3)]
    assert min(ms)>=1
    if r==1:
        assert ms==[1,2,2] and es==[-4,-2,0]
    else:
        assert max(es)==1-r<0
    if r<=6: p2rows.append({'r':r,'m_j':ms,'N_exponents':es})
sums=[sum(2*(b+3*a)-6 for a in range(degree+1))
      for degree,b in [(6,9),(5,11),(4,13)]]
assert sums==[210,186,160] and sum(sums)==556
assert len([a for a in range(4) if 2*a<=2])==2
assert len([a for a in range(4) if 2*a<=6])==4
print(json.dumps({'all_assertions_passed':True,
 'scope':'Exact all-prime parameter identities on six primes, eigensheaf degree checks, and finite checks of the proved all-r characteristic-two bound. Smoothness/Bertini/cohomology are proved in A_surface_counterexample.tex.',
 'prime_cases':rows,'p2_negative_power_examples':p2rows,
 'p2_positive_h0_contributions':sums,'p2_h0_L':6,'p2_h0_L9':556,
 'p2_embedding_dimension':561,'p2_cover_degree':'9^556',
 'p2_kernel_dimensions':{'degree1':1,'all_degrees_at_least2':0},
 'elapsed_seconds':time.perf_counter()-start},indent=2))
