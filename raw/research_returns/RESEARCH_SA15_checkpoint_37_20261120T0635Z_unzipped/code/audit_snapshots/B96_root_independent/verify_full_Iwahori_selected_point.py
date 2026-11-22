#!/usr/bin/env python3
"""B96 exact finite supplement; actual-field proofs remain indispensable.
Standalone; no external input. Preserve this file and every executed output.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import time, json, traceback

OUT=Path(__file__).with_suffix('.output.json')
assert not OUT.exists(), 'Preserve the previous executed output before rerunning'
start=time.perf_counter()
counts={}

def enc(ds):
    n=0
    for x in ds:n=5*n+x
    return n

def mat(ds):
    v0,a0,w0,d0,v1,w1,a1,v2,d1=ds
    return (1+5*a0+25*a1,v0+5*v1+25*v2,
            5*w0+25*w1,1+5*d0+25*d1)

def digits(M):
    aa,v,ww,dd=M
    assert aa%5==dd%5==1 and ww%5==0
    a=(aa-1)//5; d=(dd-1)//5; w=ww//5
    return (v%5,a%5,w%5,d%5,(v//5)%5,w//5,
            a//5,v//25,d//5)

def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%125,(a*f+b*h)%125,
            (c*e+d*g)%125,(c*f+d*h)%125)

def inv(A):
    a,b,c,d=A;z=pow((a*d-b*c)%125,-1,125)
    return (z*d%125,-z*b%125,-z*c%125,z*a%125)

def psi(breaks,x):
    x=Q(x);prev=Q(0);ans=Q(0);slope=1
    for b in map(Q,breaks):
        if x<=b:return ans+slope*(x-prev)
        ans+=slope*(b-prev);prev=b;slope*=5
    return ans+slope*(x-prev)

def run():
    names=['F2','FQ','E','Eh','Sh','Phplus','Th','QEh','QSh',
           'QPhplus','QTh','ZQ','ZM','Shw1','QSv1']
    images={x:set() for x in names}
    kernels={x:0 for x in ['Eh','Sh','Phplus','Th','QEh','QSh','QPhplus','QTh']}
    for ds in product(range(5),repeat=9):
        v0,a0,w0,d0,v1,w1,a1,v2,d1=ds
        M=mat(ds);aa,v,ww,dd=M
        assert digits(M)==ds
        coords={
          'F2':(v0,v1,w0,a0,d0),'FQ':(w0,w1,v0,a0,d0),
          'E':(v0,v1,w0,w1,a0,d0),'Eh':(a0,w0),
          'Sh':(a0,w0,v0),'Phplus':(a0,a1,w0,w1),
          'Th':(a0,a1,w0,w1,v0),'QEh':(d0,v0),
          'QSh':(d0,v0,w0),'QPhplus':(d0,d1,v0,v1),
          'QTh':(d0,d1,v0,v1,w0),'ZQ':(w0,w1,a0),
          'ZM':(v0,v1,d0),'Shw1':(w0,v0,a0,w1),
          'QSv1':(v0,w0,d0,v1)}
        for k,x in coords.items():images[k].add(enc(x))
        # Direct vector stabilizers, rather than digit counts alone.
        checks={
          'Eh':(aa%25==1 and ww%25==0),
          'Phplus':(aa==1 and ww==0),
          'QEh':(v%5==0 and dd%25==1),
          'QPhplus':(v%25==0 and dd==1)}
        checks['Sh']=checks['Eh'] and v0==0
        checks['Th']=checks['Phplus'] and v0==0
        checks['QSh']=checks['QEh'] and w0==0
        checks['QTh']=checks['QPhplus'] and w0==0
        for k,fixes in checks.items():
            assert fixes==(enc(coords[k])==0)
            kernels[k]+=int(fixes)
    expected={'F2':3125,'FQ':3125,'E':15625,'Eh':25,'Sh':125,
       'Phplus':625,'Th':3125,'QEh':25,'QSh':125,'QPhplus':625,
       'QTh':3125,'ZQ':125,'ZM':125,'Shw1':625,'QSv1':625}
    got={k:len(v) for k,v in images.items()}
    assert got==expected,(got,expected)
    assert all(kernels[k]*expected[k]==5**9 for k in kernels)
    counts['actual_Iwahori_matrices']=5**9
    counts['field_image_maps']=len(names)
    counts['direct_vector_stabilizer_tests']=8*5**9

    # All elements of each S subgroup times each elementary digit generator.
    # Full written multiplication formulas establish the homomorphisms;
    # these literal products check every digit/carry instance here.
    tests=0
    for fixed,free,target in [({0:0,1:0,2:0},[3,4,5,6,7,8],(6,5)),
                               ({0:0,2:0,3:0},[1,4,5,6,7,8],(8,4))]:
        gens=[]
        for j in free:
            x=[0]*9;x[j]=1;gens.append(mat(x))
        for vals in product(range(5),repeat=6):
            ds=[0]*9
            for j,x in zip(free,vals):ds[j]=x
            M=mat(ds)
            for G in gens:
                gd=digits(G);out=digits(mul(M,G))
                assert all(out[j]==0 for j in fixed)
                assert tuple(out[j] for j in target)==tuple((ds[j]+gd[j])%5 for j in target)
                tests+=1
    counts['relative_quotient_products']=tests

    # Conjugation in the full traceful M2 first layer.
    tests=0
    for a,b,c,d,t in product(range(5),repeat=5):
        X=(1+5*a,5*b,5*c,1+5*d)
        U=(1,t,0,1)
        Y=mul(mul(U,X),inv(U))
        assert ((Y[0]-1)//5)%5==(a+t*c)%5
        assert ((Y[3]-1)//5)%5==(d-t*c)%5
        assert (Y[1]//5)%5==(b+t*(d-a)-t*t*c)%5
        assert (Y[2]//5)%5==c
        tests+=1
    counts['traceful_M2_conjugations']=tests

    # Independent first nonzero binomial coefficient checks, through625.
    bc=0
    for j in range(1,626):
        k=j;first=1
        while k%5==0:k//=5;first*=5
        for r in range(1,first):assert comb(j,r)%5==0;bc+=1
        assert comb(j,first)%5!=0;bc+=1
    counts['binomial_coefficients']=bc

    # Every integer t in the mixed (15,19) non-high-last alternative.
    # The prime row forces u+4t=120m2. Each possible tie contradicts
    # the actual low displacement in the divisible row.
    m1,m2=15,19;A=5*m1;D0=125*m1
    ties=0
    for t in range(1,24*m2):
        u=120*m2-4*t
        assert u>t
        assert A+1+u+4*t>D0                  # N>A, order1+ordinary
        assert A+24*t+u>D0                    # order2+ordinary
        assert A+20*t+5*u>D0                  # order2+order1
        assert A+24*t+1+u>D0                  # any later ordinary
        ties+=4
    counts['mixed_last_line_inequalities']=ties

    pairs=[(5,9),(5,13),(5,17),(7,15),(11,15)]
    table=[(15,19,list(range(24,337,24)),606,7086),
           (11,19,[264],606,8814),(7,19,[168],606,11118),
           (9,17,[216],858,16266),(9,13,[216],1362,28866)]
    rows=[];conversions=0
    for (b1,b2),(m1,m2,ts,C,lower) in zip(pairs,table):
        assert (24-b2,24-b1)==(m1,m2)
        assert C==3000-126*m2
        deltas=[3125*b-25*(24-b) for b in (b1,b2)]
        lowlast=Q(9*min(deltas),25);first=Q(max(deltas),5)
        assert lower>lowlast and lower>first
        zs=[]
        for t in ts:
            u=15000-630*m2-4*t
            assert u>t and Q(u+4*t,5)==C and 0<t<C
            if m1%5:assert t==24*m1
            else:assert t<24*m1
            for sigma in range(1,t):
                z=psi([sigma,t],C)
                assert z==25*C-20*t-4*sigma
                assert z>25*C-24*t>=lower
                assert z>lowlast and z>first
                zs.append(z);conversions+=1
        gaps=[15625*(24-b)-3125*b for b in (b1,b2)]
        assert gaps[0]!=gaps[1]
        assert all(25*(24-b)<3125*b<15625*(24-b)<1500000 for b in (b1,b2))
        rows.append({'pair':[b1,b2],'opposite':[m1,m2],
          't_prime_values':ts,'C_prime':C,'strict_z_lower':lower,
          'minimum_checked_z':str(min(zs)),
          'nonhigh_last_upper':str(lowlast),'ordinary_threshold':str(first),
          'strict_margins':[str(lower-lowlast),str(lower-first)],
          'displacement_gaps':gaps})
    counts['actual_Herbrand_arithmetic_cases']=conversions
    counts['chosen_orientations']=len(rows)

    # Recover the necessary finite-character census independently.
    census=set()
    for b1 in range(5,20,2):
        for b2 in range(b1+2,20,2):
            for c1 in range(24):
                for c2 in range(24):
                    if not(c1%4==c2%4==1):continue
                    if (c1-5*b1)%6 or (c2-5*b2)%6:continue
                    if (c1-5*b1-c2+5*b2)%24:continue
                    if {c1,5*c1%24}=={c2,5*c2%24}:continue
                    census.add((b1,b2))
    expected_pairs={(5,9),(5,13),(5,17),(7,15),(7,19),(9,13),
                    (9,17),(11,15),(11,19),(15,19)}
    assert census==expected_pairs
    covered=set(pairs)|{(24-b2,24-b1) for b1,b2 in pairs}
    assert covered==census
    counts['different_character_rows']=len(census)
    return {'field_images':got,'actual_stabilizer_orders':kernels,
            'threshold_rows':rows,'necessary_character_rows':[list(x) for x in sorted(census)]}

try:
    data=run();status='PASS';error=None
except Exception:
    status='FAIL';error=traceback.format_exc();data={}
result={'status':status,'actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,'counts':counts,
        'scope':'Exact finite supplement to the separate B96 actual-field proof. Enumerates the full Iwahori matrix image, actual original and selected quotient-point stabilizers, literal relative quotient products and traceful conjugations, finite binomial coefficients, all displayed conductor arithmetic and character rows. It does not replace the selected-point existence, normality, ramification or coefficient proofs and asserts no realization or unrestricted least-index equality.',
        'data':data,'error':error}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='data'},indent=2))
if status!='PASS':raise SystemExit(1)
