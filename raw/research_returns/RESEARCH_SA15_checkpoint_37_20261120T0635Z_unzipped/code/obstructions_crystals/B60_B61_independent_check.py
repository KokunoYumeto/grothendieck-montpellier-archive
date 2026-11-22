"""Exact finite arithmetic supplement for B60/B61.
No formal group, point field, or congruent pair is constructed.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import time,math,itertools,json
started=time.perf_counter()
primes=[p for p in range(5,102) if all(p%d for d in range(2,math.isqrt(p)+1))]
counts={'Newton_tame_records':0,'wild_prime_pair_records':0,'wild_divisible_pair_records':0,
        'wild_mixed_point_field_contradictions':0,'tame_residual_pair_checks':0,
        'tame_distinct_type_contradictions':0,'integer_binomial_bound_checks':0}
p5_rows=[];p5_wild=[];p5_tame=[]
for p in primes:
    q=p*p;N=q-1;e=N*(p-1);rows=[]
    for j in range(p+1):
        c=(1+(p-1)*j)%N
        first=c%(p+1)
        if not first:first=p+1
        for B in range(first,p*(p-1),p+1):
            alpha=Fraction(N-B);beta=Fraction(B,p);b=(p-1)*B;x=Fraction(B,p**3)
            assert 0<B<p*(p-1) and B%2==1 and alpha>beta>0
            assert e+alpha==b+p*alpha<q*alpha
            assert b+p*beta==q*beta<e+beta
            assert q*x==beta<e+x and beta<b+p*x
            assert b<e*p/Fraction(p+1) and b%N==((p-1)*c)%N
            high=(c-B)%N;low=(p*c+B)%N
            assert high%(p+1)==0 and low%(p+1)==0
            assert (high+low)%N==(p+1) and high!=low
            rH=high//(p+1);rQ=low//(p+1)
            assert (rH+rQ)%(p-1)==1
            row={'c':c,'B':B,'high':rH,'low':rQ,'type':tuple(sorted({c,p*c%N})),
                 'break_bound':p*N-(p+1)*B}
            if B%p==0:
                z=B//p;assert 1<=z<=p-2 and z%p
                assert x==Fraction(z,q) and x.denominator==q
            else:
                assert (p*x).denominator==q
            rows.append(row);counts['Newton_tame_records']+=1
    # Common wild high-character and exact break for two prime-to-p values.
    seen={}
    for row in rows:
        if row['B']%p:
            key=(row['high'],row['break_bound'])
            if key in seen:assert seen[key]['B']==row['B'] and seen[key]['c']==row['c']
            seen[key]=row;counts['wild_prime_pair_records']+=1
    divisible=[r for r in rows if r['B']%p==0]
    for x,y in itertools.combinations_with_replacement(divisible,2):
        if x['high']!=y['high']:continue
        assert (x['B']//p-y['B']//p)%(p-1)==0
        assert x['B']==y['B'] and x['c']==y['c']
        counts['wild_divisible_pair_records']+=1
    for nd in rows:
        if nd['B']%p==0:continue
        for dv in divisible:
            if nd['high']!=dv['high'] or nd['break_bound']>=dv['break_bound']:continue
            assert nd['B']>dv['B']
            # E/R has degreeq from the reduced valuation denominator.
            assert Fraction(nd['B'],q).denominator==q
            actual_break=N*nd['B']
            required_second_displacement=q*dv['B']
            universal_lower_bound=dv['B']+actual_break
            assert universal_lower_bound>required_second_displacement
            counts['wild_mixed_point_field_contradictions']+=1
            if p==5 and nd['type']!=dv['type']:p5_wild.append([nd,dv])
    for x,y in itertools.combinations_with_replacement(divisible,2):
        if sorted([x['high'],x['low']])!=sorted([y['high'],y['low']]):continue
        bx=x['B']//p;by=y['B']//p
        assert 1<=bx<=p-2 and 1<=by<=p-2
        assert q-(2*p-1)>0  # points outside any union of two lines exist
        if bx!=by:
            assert N*bx!=N*by
        elif x['high']!=y['high']:
            assert q*(N-p*bx)>q*bx
        else:
            assert x['c']==y['c']
        counts['tame_residual_pair_checks']+=1
        if x['type']!=y['type']:
            assert bx!=by or x['high']!=y['high']
            counts['tame_distinct_type_contradictions']+=1
            if p==5:p5_tame.append([x,y])
    if p==5:p5_rows=rows

# Exact integer binomial valuations test the lower-bound lemma's monomial
# step in mixed characteristic, retaining p-divisible coefficients.
def vp(n,p):
    if not n:return 10**9
    a=0
    while n%p==0:n//=p;a+=1
    return a
for p in [5,7,11,13,17,19]:
    for A in range(1,2*p+1):
        for br in range(1,13):
            for e in [1,p-1,(p*p-1)*(p-1)]:
                leading=min(vp(math.comb(A,j),p)*e+A+j*br for j in range(1,A+1))
                assert leading>=A+br
                assert (leading==A+br)==(A%p!=0)
                counts['integer_binomial_bound_checks']+=1
assert len(p5_rows)==20 and len(p5_wild)==8 and len(p5_tame)==2
result={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,**counts,
        'p5_all_Newton_rows':p5_rows,'p5_wild_excluded_rows':p5_wild,'p5_tame_excluded_rows':p5_tame,
        'scope':'Finite Newton, tame-character, valuation-denominator and lower-break arithmetic only. The Galois point-field existence and universal character-recovery assertions are proved in B60/B61, not inferred from these ranges.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if not k.startswith('p5_')},indent=2))
