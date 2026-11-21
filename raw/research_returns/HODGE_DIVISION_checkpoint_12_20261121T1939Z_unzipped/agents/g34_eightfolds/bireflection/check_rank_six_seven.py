"""Exact necessary scalar/rank profiles; no G34 class or tuple assertion."""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm,prod
import json
HERE=Path(__file__).resolve().parent
phi=lambda n:sum(gcd(a,n)==1 for a in range(1,n+1))
orders=[1,2,3,4,5,6,7,8,9,10,12,14,18]
assert all(phi(d)<=6 for d in orders)
degrees={d:phi(lcm(3,d))//2 for d in orders}
assert [d for d in orders if 1<degrees[d]<=3]==[4,9,12,18]
assert [d for d in orders if degrees[d]==2]==[4,12]
profiles=[]
def partitions(n,k,lo=1):
    if k==0:
        if n==0:yield ()
        return
    for a in range(lo,n//k+1):
        for rest in partitions(n-a,k-1,a):yield(a,)+rest
for r in range(12,15):
    for a in range(3,6):
        for b in range(a,6):
            for inside in partitions(18-a-b,r-2):
                profiles.append({'r':r,'outside':[a,b],'inside':list(inside)})
assert len(profiles)==8
residual={}
for k in range(6):
    mu=Fraction(k,6)
    for eps in [0,Fraction(1,2)]:
        pair=tuple(sorted([(Fraction(1,4)+mu)%1,
                           (Fraction(1,4)+eps-mu)%1]))
        assert sum(pair)%1==(Fraction(1,2)+eps)%1
        spec=[Fraction(0),Fraction(0),Fraction(1,2),Fraction(1,2),*pair]
        order=lcm(*(x.denominator for x in spec))
        sq=[(2*x)%1 for x in spec]
        sqorder=lcm(*(x.denominator for x in sq))
        assert order in [4,12] and sqorder==order//2
        assert sum(x!=0 for x in sq)==2
        assert sum(spec) in [Fraction(3,2),Fraction(2),Fraction(5,2)]
        residual[pair]={'pair':[str(x) for x in pair],'age':str(sum(spec)),
                        'order':order,'square_order':sqorder}
assert len(residual)==7
assert prod([6,12,18,24,30,42])==39191040
assert 2*prod([6,12,18,24,30,42])==78382080
out={'status':'PASS','degree_cases':degrees,'rank_profiles':profiles,
     'rank_four_residual_pairs':list(residual.values()),'rank_seven_eliminated_by_written_proof':True,
     'scope':'Exact cyclotomic compositum, branch-rank partition and spectral arithmetic only. No conjugacy-class occurrence, generating tuple, dominance, or nonsplit polarization asserted.'}
(HERE/'check_rank_six_seven.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'cyclotomic_cases':len(orders),
                  'rank_profiles':len(profiles),'rank_four_pairs':len(residual)}))
