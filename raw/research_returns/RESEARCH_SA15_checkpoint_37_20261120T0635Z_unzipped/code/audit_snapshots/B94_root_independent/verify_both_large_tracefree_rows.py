#!/usr/bin/env python3
"""Exact finite supplement for the separate B94 candidate.
All computations concern p=5. They supplement, never replace, the
actual-field/ramification proof. No formal-group realization is inferred.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, time, traceback

OUT=Path(__file__).with_suffix('.output.json')
START=time.perf_counter()
counts={}

def enc(*digits):
    n=0
    for d in digits: n=5*n+d
    return n

def mul(A,B):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%125,(a*f+b*h)%125,(c*e+d*g)%125,(c*f+d*h)%125)

def inv(A):
    a,b,c,d=A; z=pow((a*d-b*c)%125,-1,125)
    return (z*d%125,-z*b%125,-z*c%125,z*a%125)

def matrix(u,a0,c0,b1,c1,a1,b2,d1):
    d0=(u*c0-a0)%5
    return (1+5*a0+25*a1,u+5*b1+25*b2,5*c0+25*c1,1+5*d0+25*d1)

def digits(M):
    aa,b,cc,dd=M
    assert aa%5==dd%5==1 and cc%5==0
    a=(aa-1)//5; d=(dd-1)//5; c=cc//5
    u=b%5; a0=a%5; c0=c%5; b1=(b//5)%5; c1=c//5
    assert (a0+d%5-u*c0)%5==0
    return u,a0,c0,b1,c1,a//5,b//25,d//5

def psi(upper,value):
    value=Q(value); prev=Q(0); ans=Q(0); slope=1
    for br in map(Q,upper):
        if value<=br:
            return ans+slope*(value-prev)
        ans+=slope*(br-prev); prev=br; slope*=5
    return ans+slope*(value-prev)

def run():
    # Enumerate every actual matrix in det=1 mod25 Iwahori, and all
    # point/division-field images used in the proof.
    names=['F2','FQ','E','Sh','Eh25','El25','Eh125','Th','El125','ETh','EEl125','Shc1']
    images={k:set() for k in names}
    kernels={'U':0,'Sh':0,'El25':0,'Th':0,'El125':0}
    terminal=0
    for ds in product(range(5),repeat=8):
        u,a0,c0,b1,c1,a1,b2,d1=ds
        M=matrix(*ds); aa,bb,cc,dd=M
        assert (aa*dd-bb*cc)%25==1
        assert digits(M)==ds
        d0=(u*c0-a0)%5
        images['F2'].add(enc(u,a0,c0,b1))
        images['FQ'].add(enc(u,a0,c0,c1))
        images['E'].add(enc(u,a0,c0,b1,c1))
        images['Sh'].add(enc(u,a0,c0))
        images['Eh25'].add(enc(a0,c0))
        images['El25'].add(enc(u,b1,d0))
        images['Eh125'].add(enc(a0,a1,c0,c1))
        images['Th'].add(enc(u,a0,a1,c0,c1))
        images['El125'].add(enc(u,b1,b2,d0,d1))
        images['ETh'].add(enc(u,a0,c0,b1,c1,a1))
        images['EEl125'].add(enc(u,a0,c0,b1,c1,b2,d1))
        images['Shc1'].add(enc(u,a0,c0,c1))
        if u==a0==c0==b1==c1==0:
            kernels['U']+=1; terminal+=1
            assert (((aa*dd-bb*cc)%125)-1)//25==(a1+d1)%5
        if u==a0==c0==0: kernels['Sh']+=1
        if u==b1==d0==0: kernels['El25']+=1
        if u==a0==a1==c0==c1==0: kernels['Th']+=1
        if u==b1==b2==d0==d1==0: kernels['El125']+=1
    expected={'F2':625,'FQ':625,'E':3125,'Sh':125,'Eh25':25,'El25':125,
              'Eh125':625,'Th':3125,'El125':3125,'ETh':15625,'EEl125':78125,'Shc1':625}
    got={k:len(v) for k,v in images.items()}
    assert got==expected,(got,expected)
    assert kernels=={'U':125,'Sh':3125,'El25':3125,'Th':125,'El125':125}
    assert got['E']*got['Th']//got['ETh']==got['Shc1']
    assert got['E']*got['El125']//got['EEl125']==got['El25']
    counts['actual_group_matrices']=5**8
    counts['field_image_maps']=len(names)
    counts['terminal_determinants']=terminal
    # Literal multiplication verifies the two relative quotient maps are
    # homomorphisms, with precisely the asserted actual stabilizer kernels.
    tests=0
    for ds in product(range(5),repeat=5):
        b1,c1,a1,b2,d1=ds
        M=matrix(0,0,0,b1,c1,a1,b2,d1)
        for gen in [matrix(0,0,0,1,0,0,0,0),matrix(0,0,0,0,1,0,0,0),
                    matrix(0,0,0,0,0,1,0,0),matrix(0,0,0,0,0,0,1,0),
                    matrix(0,0,0,0,0,0,0,1)]:
            md=digits(mul(M,gen)); gd=digits(gen)
            assert (md[5],md[4])==((a1+gd[5])%5,(c1+gd[4])%5)
            tests+=1
    for ds in product(range(5),repeat=5):
        c0,c1,a1,b2,d1=ds
        M=matrix(0,0,c0,0,c1,a1,b2,d1)
        for gen in [matrix(0,0,1,0,0,0,0,0),matrix(0,0,0,0,1,0,0,0),
                    matrix(0,0,0,0,0,1,0,0),matrix(0,0,0,0,0,0,1,0),
                    matrix(0,0,0,0,0,0,0,1)]:
            md=digits(mul(M,gen)); gd=digits(gen)
            assert (md[6],md[7])==((b2+gd[6])%5,(d1+gd[7])%5)
            tests+=1
    lower=matrix(0,0,1,0,0,0,0,0); cur=(1,0,0,1)
    for k in range(1,26):
        cur=mul(cur,lower)
        d=digits(cur)
        assert d[2]+5*d[4]==k%25
    assert cur==(1,0,0,1)
    counts['relative_quotient_multiplications']=tests
    counts['cyclic25_powers']=25
    # Tame-conjugation formulas on sl2, and opposite root conjugation.
    conjugations=0
    for a,b,c,t in product(range(5),repeat=4):
        A=(1+5*a,5*b,5*c,1+5*((-a)%5))
        U=(1,t,0,1)
        V=mul(mul(U,A),inv(U))
        assert ((V[0]-1)//5)%5==(a+t*c)%5
        assert (V[1]//5)%5==(b-2*t*a-t*t*c)%5
        assert (V[2]//5)%5==c
        conjugations+=1
    counts['sl2_conjugations']=conjugations
    # Mixed-coordinate coefficient inequalities; endpoint/strict regimes.
    mixed=[]
    for b1,b2 in [(5,9),(5,13),(5,17),(15,19)]:
        assert 60000+630*b1-3630*b2>0
        assert 630*b2-750*b1>0
        for t in range(24,24*b1,24):
            u=15000-630*b2-4*t
            assert u>t
            assert 5*u+5*b1>15000-625*b1
            K=(15000-625*b1)-u
            assert K+t>125*b1
        mixed.append({'b':[b1,b2],'strict_tail_margin':60000+630*b1-3630*b2,
                      'ordinary_first_margin':630*b2-750*b1})
    counts['mixed_parameter_rows']=len(mixed)
    # Four immediate exclusions, including the actual tame congruence and
    # strict residual bound. Mirror rows use the same numerical data.
    rejected=[]
    for b2,y in [(13,264),(17,168)]:
        candidates=[]
        for r in range(18,600-30*b2,24):
            x=y-4*(r-6)
            if 0<x<120 and x%24==0:
                candidates.append((r,x))
                assert 5*r-24>y
        assert candidates
        rejected.append({'pair':[5,b2],'candidate_r_x':candidates})
    counts['immediate_rows_with_mirrors']=4
    # Exactly nine profiles are allowed by the proven necessary inequalities.
    profiles=[(r,x) for r in range(18,600-30*9,24) for x in range(24,120,24)
              if 0<x+4*r-24<360 and x>r]
    assert profiles==[(18,24),(18,48),(18,72),(18,96),(42,48),(42,72),(42,96),(66,72),(66,96)]
    rows=[]
    for r,x in profiles:
        upper=list(map(Q,[6,r,Q(x+4*r,5),126,Q(1866+4*r,5)]))
        assert all(a<b for a,b in zip(upper,upper[1:]))
        lower=[psi(upper,z) for z in upper]
        expected_lower=list(map(Q,[6,5*r-24,5*x-24,15726-20*x-100*r,170226-20*x+400*r]))
        assert lower==expected_lower
        l1,l2,l3,l4,l5=lower
        C=psi(upper,576)
        assert C==803976-20*x-2100*r
        esh_upper=[l4,Q(l5+4*l4,5)]
        for pair,high_u,c1break,low_c,elow_lower in [
            ([5,9],234000,l4,15600,[Q(6),l4]),
            ([15,19],78000,Q(l5+4*l4,5),46800,[l2,l5])]:
            assert high_u>c1break
            ah=Q(high_u+4*c1break,5)
            assert ah>esh_upper[-1]
            Ba=psi(esh_upper,ah)
            elow_upper=[elow_lower[0],Q(elow_lower[1]+4*elow_lower[0],5)]
            assert low_c>elow_upper[-1]
            Bd=psi(elow_upper,low_c)
            if pair==[5,9]:
                assert Ba==489096+80*x-1600*r
                assert Bd==326976+80*x+400*r
            else:
                assert Ba==327096+80*x+400*r
                assert Bd==489576+80*x-1700*r
            assert C>max(Ba,Bd)
            rows.append({'b':pair,'r':r,'x':x,'upper':[str(z) for z in upper],
                         'lower':[str(z) for z in lower],'cyclotomic':str(C),
                         'a1_bound':str(Ba),'d1_bound':str(Bd),
                         'strict_gap':str(C-max(Ba,Bd))})
    counts['ramification_profiles']=len(rows)
    # Verify original/quotient normalized parameter list, removing equal
    # finite-special Frobenius orbits, not just equal exponents.
    remaining=[]
    for b1 in range(5,20,2):
        for b2 in range(b1+2,20,2):
            if (b1-b2)%4: continue
            valid=False
            for c1 in range(1,24,4):
                for c2 in range(1,24,4):
                    if (c1-5*b1)%6 or (c2-5*b2)%6: continue
                    if (c1-5*b1-c2+5*b2)%24: continue
                    if {c1,(5*c1)%24}!={c2,(5*c2)%24}: valid=True
            if valid: remaining.append((b1,b2))
    assert remaining==[(5,9),(5,13),(5,17),(7,15),(7,19),(9,13),(9,17),(11,15),(11,19),(15,19)]
    excluded={(5,9),(5,13),(5,17),(7,19),(11,19),(15,19)}
    survivors=[list(x) for x in remaining if x not in excluded]
    assert survivors==[[7,15],[9,13],[9,17],[11,15]]
    return {'status':'PASS','counts':counts,'field_image_cardinalities':got,
            'stabilizer_cardinalities':kernels,'mixed_rows':mixed,
            'immediate_exclusion_rows':rejected,'profiles':rows,
            'remaining_3_4_pairs':survivors,
            'scope':'Finite exact p=5 supplement only. Actual-field, normality and ramification arguments require the complete written proof. No formal-group realization or least-index conclusion.'}

try:
    result=run()
except BaseException as e:
    result={'status':'FAIL','error':repr(e),'traceback':traceback.format_exc(),'partial_counts':counts}
    result['actual_utc']=datetime.now(timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-START
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise
else:
    result['actual_utc']=datetime.now(timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-START
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
