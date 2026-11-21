"""Exact combined comparison integers for e14,16,18 from full model data."""
from pathlib import Path
from hashlib import sha256
from math import gcd, isqrt, prod
import json

HERE = Path(__file__).parent
UP = HERE/'harmonic_hecke_exact_data.json'
GP = HERE/'gl2_higher2_certificate.json'
FACTORS = {
    14: {2:106, 3:101, 5:7, 53:3, 419:1, 16519:1, 15083:3,
         7547263:3, 42800473:3},
    16: {2:123, 3:147, 5:4, 11:4, 23:1, 401:1, 38177:3,
         36293:3, 13687:1, 25078104767246023:3},
    18: {2:177, 3:180, 5:17, 7:1, 13:8, 19:2, 37:2, 73:1,
         3343:3, 8609:1, 18541:3, 7691:1, 151871:3, 8361790201:3},
}


def evaluate(poly, x):
    z=0
    for a in poly:
        z=z*x+a
    return z


def trial_prime(n):
    return n>=2 and (n==2 or (
        n%2 and all(n%d for d in range(3,isqrt(n)+1,2))))


def prove_prime(n):
    if n!=25078104767246023:
        return trial_prime(n)
    # A full-order Lucas certificate, avoiding trial division to sqrt(n).
    factors={2:1,3:3,10487:1,44284289839:1}
    assert prod(q**a for q,a in factors.items())==n-1
    assert all(trial_prime(q) for q in factors)
    witness=3
    assert pow(witness,n-1,n)==1
    assert all(pow(witness,(n-1)//q,n)!=1 for q in factors)
    # The order of witness is exactly n-1; hence phi(n)>=n-1 and n is prime.
    return True


u={r['e']:r for r in json.loads(UP.read_text())['degrees']}
g={r['e']:r for r in json.loads(GP.read_text())['degrees']}
assert set(u)==set(g)==set(FACTORS)
rows=[]
for e in FACTORS:
    us={r['p']:r for r in u[e]['results']}
    gs={r['p']:r for r in g[e]['results']}
    assert set(us)==set(gs)=={7,13}
    values=[]
    details=[]
    for p in (7,13):
        up,gp=us[p]['charpoly_coefficients'],gs[p]['charpoly_coefficients']
        assert up[0]==gp[0]==1
        assert all(isinstance(a,int) for a in up+gp)
        assert len(gp)-1==(2*e-5)//3+1
        ue,ge=1+p**e+p**(2*e),1+p**(2*e)
        uv,gv=evaluate(up,ue),evaluate(gp,ge)
        assert ue==us[p]['comparison_point']
        assert ge==gs[p]['evaluation_point']
        assert uv==us[p]['comparison_value']!=0
        assert gv==gs[p]['evaluation']!=0
        values.append(uv*gv)
        details.append({'p':p,'U3_evaluation':uv,'GL2_evaluation':gv,
                        'combined_value':uv*gv})
    common=gcd(*values)
    assert common==prod(q**a for q,a in FACTORS[e].items())
    assert all(prove_prime(q) for q in FACTORS[e])
    rows.append({
        'e':e,'conditional_K_degree':2*e,
        'U3_dimension':len(us[7]['charpoly_coefficients'])-1,
        'GL2_dimension':g[e]['dimension'],
        'results':details,'gcd':common,'factorization':FACTORS[e],
        'primes_at_least_2pow31':[q for q in FACTORS[e] if q>=2**31],
    })
out=Path(__file__).with_suffix('.json')
report={
    'status':'PASS: exact combined model comparisons and proved prime factors',
    'U3_data_sha256':sha256(UP.read_bytes()).hexdigest(),
    'GL2_data_sha256':sha256(GP.read_bytes()).hexdigest(),
    'degrees':rows,
    'large_prime_certificate':{
        'n':25078104767246023,'witness':3,
        'n_minus_1_factorization':{2:1,3:3,10487:1,44284289839:1},
        'subfactor_primality':'exact trial division',
    },
    'scope':'Full arithmetic coverage and any Bernoulli/reflection step are separate.',
}
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'output':str(out),
 'summary':[{k:r[k] for k in ('e','U3_dimension','GL2_dimension','factorization',
                             'primes_at_least_2pow31')} for r in rows]}))
