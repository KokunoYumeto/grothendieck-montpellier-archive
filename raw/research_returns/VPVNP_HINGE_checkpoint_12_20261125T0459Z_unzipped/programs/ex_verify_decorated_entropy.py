"""Independent exact entropy comparisons for the decorated determinant witness.

Build the dominating partition by adding its three Young-diagram contributions,
then compare the entropy inequality by factoring the integers and cancelling
prime powers. No floating logarithm decides a comparison.
"""
from collections import Counter
from pathlib import Path
import json,math,os

def factor(z):
    ans=Counter();p=2
    while p*p<=z:
        while z%p==0:ans[p]+=1;z//=p
        p=3 if p==2 else p+2
    if z>1:ans[z]+=1
    return ans

def add_factors(dest,z,mult):
    for p,e in factor(z).items():dest[p]+=mult*e

rows=[]
for q in [2,4,8,16,32,64,128]:
    d=q*q;a=21;b=22
    # det_b^a contributes (a^d); det_c^a contributes its largest
    # possible row (ad); W^b contributes (bq)^q.
    shape=[a]*d;shape[0]+=a*d
    for i in range(q):shape[i]+=b*q
    assert all(shape[i]>=shape[i+1] for i in range(d-1))
    n=sum(shape);assert n==(2*a+b)*d
    exponents=Counter()
    add_factors(exponents,n,4*n)
    add_factors(exponents,q,-5*n)
    for value,count in Counter(shape).items():
        add_factors(exponents,value,-4*value*count)
    left=right=1
    for p,e in sorted(exponents.items()):
        if e>0:left*=pow(p,e)
        elif e<0:right*=pow(p,-e)
    comparison=(left>right)-(left<right)
    assert comparison==(1 if q<=64 else -1)
    rows.append({'q':q,'degree':n,'partition_multiplicities':sorted(Counter(shape).items(),reverse=True),
       'cancelled_prime_exponents':sorted((p,e) for p,e in exponents.items() if e),
       'left_bit_length':left.bit_length(),'right_bit_length':right.bit_length(),
       'entropy_above_five_quarters_log_q':comparison>0,
       'entropy_bits_display':math.log2(n)-sum(v*c*math.log2(v) for v,c in Counter(shape).items())/n})
    print(q,comparison,left.bit_length(),right.bit_length(),flush=True)
out=Path('/workspace/scratch/9f5945cf2012/VPVNP_HINGE_work/outputs/ex_decorated_entropy_independent.json')
temp=out.with_suffix('.json.atomic_tmp')
with temp.open('w') as f:
    json.dump({'status':'PASS exact integer comparisons','scope':'q<=64 witness thresholds pass; q128 is only failure of this particular lower-bound test','results':rows},f,indent=2)
    f.write('\n');f.flush();os.fsync(f.fileno())
os.replace(temp,out)
