"""Finite exact arithmetic supplement to the uniform B66 proof.
No finite sample is used as proof for arbitrary primes or formal groups.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,datetime,itertools
start=time.perf_counter()
primes=(5,7,11,13,17,19,23,29,31)
counts=Counter();summaries=[]
def polygon(points):
    hull=[]
    for x,y in sorted(points):
        while len(hull)>=2:
            x0,y0=hull[-2];x1,y1=hull[-1]
            if F(y1-y0,x1-x0)>=F(y-y1,x-x1):hull.pop()
            else:break
        hull.append((x,y))
    return [(F(y0-y1,x1-x0),x1-x0) for (x0,y0),(x1,y1) in zip(hull,hull[1:]) if y0>y1]
for p in primes:
    N=p*p-1;e=N//2;s=e*(p+1);a=e*N
    assert e%2==0 and e%(p-1)==0 and e%p and s%p and e>p and e<p**3 and s%N==0
    def high(B):return p*B if B<e else s-B
    def orb(c):return tuple(sorted({c%N,p*c%N}))
    local=Counter()
    for B in range(1,p*e,2):
        alpha=F(s-B);beta=F(B,p);b=(p-1)*B
        assert polygon([(0,a),(p-1,b),(N,0)])==[(alpha,p-1),(beta,p*p-p)]
        assert polygon([(0,beta),(1,a),(p,b),(p*p,0)])==[(F(B,p**3),p*p)]
        inv=polygon([(0,alpha),(1,a),(p,b),(p*p,0)])
        if B<e:assert inv==[(F(s-p*B,p),p),(beta,p*p-p)]
        else:assert inv==[(alpha/(p*p),p*p)]
        result=Counter({F(B):p-1})
        for z,n in inv:
            assert z<alpha and n*(p-1)%p==0
            result[p*z]+=n*(p-1)//p
        Bp=high(B)
        assert result==Counter({F(s-Bp):p-1,F(Bp,p):p*p-p})
        cs=[c for c in range(1,N,p-1) if (B-c)%(p+1)==0]
        assert len(cs)==2
        for c in cs:
            cp=p*c%N
            assert cp%(p-1)==1 and (Bp-cp)%(p+1)==0 and orb(cp)==orb(c)
            local['tangent_quotient_weights']+=1
        local['newton_and_high_quotient_records']+=1
        if B%p==0:
            low=B//p
            assert 0<low<p*e
            assert alpha+(p-1)*beta==s-low
            assert p*beta/(p*p)==F(low,p)
            for c in cs:assert (low-p*c)%(p+1)==0
            local['low_quotient_records']+=1
    small=[b for b in range(1,e) if p*b<e]
    assert all(2*b<p for b in small)
    for b,c in itertools.product(small,repeat=2):
        if (b-c)%(p-1)==0:assert b==c
        local['wild_small_congruences']+=1
    big=[]
    for b in range(1,e):
        B=p*b;Bp=high(B)
        if B<e:assert Bp%p==0
        else:assert Bp%p!=0;big.append(Bp)
        local['wild_divisible_transformations']+=1
    assert len(big)==len(set(big))
    ks=[k for k in range(1,e) if p*k<e]
    for k in ks:
        B2=p*p*k
        assert B2>e and high(B2)%p and (B2//p)%p==0
        for b in range(1,e):
            if b%p==0:continue
            alpha=s-p*b
            assert alpha>=e+p
            assert p*p*(alpha-p*k)>b-p*k
            B1=p*b
            if B1<e:assert high(B1)%p==0
            else:assert high(B1)%p and high(B1)!=high(B2)
            local['tame_prime_divisible_comparisons']+=1
    for k,l in itertools.product(ks,repeat=2):
        B1=p*p*k;B2=p*p*l
        assert high(B1)%p and (B2//p)%p==0
        if high(B1)==high(B2):assert k==l
        local['tame_two_divisible_comparisons']+=1
    for c,d in itertools.product(range(1,N,p-1),repeat=2):
        assert (orb(c+e)==orb(d+e))==(orb(c)==orb(d))
        local['equal_slope_character_comparisons']+=1
    square=[]
    for m in range(1,p+2):
        if (p+1)%m:continue
        aa=e*m;q0=1;q1=min(aa+q0,p*q0+1,p*p*q0)
        q2=min(aa+q1,p*q1+1,p*p*q1)
        assert q1>=p+1 and q2>=F(aa,p-1)
        square.append({'m':m,'a':aa,'q1':q1,'q2':q2,'threshold':str(F(aa,p-1))})
        local['square_target_log_bounds']+=1
    counts.update(local);summaries.append({'p':p,'e':e,'s':s,'counts':dict(local),'square_bounds':square})
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'primes':primes,'counts':dict(counts),'per_prime':summaries,'scope':'Exact finite Newton and quotient arithmetic, character congruences and displayed inequalities at nine primes. No finite enumeration substitutes for the complete all-prime B66 proof or establishes any formal-group existence.'}
out=Path(__file__).with_suffix('.output.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='per_prime'},indent=2))
