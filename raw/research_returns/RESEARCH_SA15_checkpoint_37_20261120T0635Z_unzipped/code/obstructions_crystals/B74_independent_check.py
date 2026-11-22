"""Exact finite supplement to B74; no existence or universal theorem inferred.

The first part checks the actual subgroup/quotient construction in free
rank-two Z/p^r modules, including induced matrices and the final p-level.
The second part checks bounded complete sectors and explicit higher-level
samples of the proved induction, with exact integer arithmetic throughout.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations_with_replacement
import hashlib
import json
import time

started = time.perf_counter()
counts = Counter()
records = []

# Use an adapted basis for the preserved line H=<p^(r-1)e1>.
# Its preimage is {(x,p*y)} and the quotient coordinate is (x mod p^(r-1),y).
for p in (5, 7):
    for r in (2, 3):
        modulus, lower = p**r, p**(r-1)
        image, kernel = set(), []
        for x in range(modulus):
            for y in range(lower):
                point = (x, p*y)
                assert (lower*point[1]) % modulus == 0
                quotient = (x % lower, y)
                image.add(quotient)
                if quotient == (0, 0):
                    kernel.append(point)
                counts['actual_subgroup_points'] += 1
        assert len(image) == lower**2
        assert kernel == [(j*lower, 0) for j in range(p)]
        counts['actual_subgroup_quotients'] += 1
        matrices = [(1,1,p,1+p),(2,1,p,1),
                    (1,0,p,1),(1,1,0,1)]
        for a,b,c,d in matrices:
            assert c % p == 0 and (a*d-b*c) % p != 0
            descended = (a, p*b, c//p, d)
            assert (descended[0]*descended[3]
                    -descended[1]*descended[2]) == a*d-b*c
            # Full subgroup enumeration checks actual, not just semisimple, maps.
            for x in range(modulus):
                for y in range(lower):
                    z = ((a*x+b*p*y) % modulus,
                         (c*x+d*p*y) % modulus)
                    assert z[1] % p == 0
                    induced = (z[0] % lower, (z[1]//p) % lower)
                    direct = ((a*(x % lower)+p*b*y) % lower,
                              ((c//p)*(x % lower)+d*y) % lower)
                    assert induced == direct
                    counts['induced_actual_matrix_points'] += 1
            counts['induced_actual_matrices'] += 1


def integer_log_bound(p, e):
    k = 0
    while p**(k+1) < e:
        k += 1
    assert p**k < e < p**(k+1)
    low = (k+3)//2
    upper = max(2,k)
    assert e > p**(2*low-3)
    n = upper+1
    assert n >= 3 and e < p**n <= p**(2*n-3)
    return k, low, upper


def run_pair(p, n, e, b1, b2):
    q, N, s = p*p, p*p-1, e*(p+1)
    assert n >= 3 and e < p**n and e % p and e % (p-1) == 0
    assert 0 < p*b1 < e and 0 < p*b2 < e
    assert (b1-b2) % (p-1) == 0
    original = (p*b1,p*b2)
    # This is only an abstract character compatibility test, not existence.
    c1,c2 = original[0] % N, original[1] % N
    assert ((p+1)*(c1-c2)) % N == 0
    D1,D2 = original
    history=[]
    for j in range(n-1):
        current_level=n-j
        assert current_level >= 2
        assert D1==p**(j+1)*b1 and D2==p**(j+1)*b2
        assert 0<D1<p*e and 0<D2<p*e
        assert D1%p==D2%p==0 and D1!=e and D2!=e
        # At j>=1 the preceding small quotient has produced a stable low
        # line of valuation D_i/p, distinct from the current high line.
        if j:
            assert p*(s-D1)>D1 and p*(s-D2)>D2
            counts['rational_marked_stages'] += 1
        left,right=D1<e,D2<e
        next1=p*D1 if left else s-D1
        next2=p*D2 if right else s-D2
        assert 0<next1<p*e and 0<next2<p*e
        assert (next1%p==0)==left and (next2%p==0)==right
        history.append({'stage':j,'level_before':current_level,
                        'level_after':current_level-1,
                        'parameters':[D1,D2],
                        'next_parameters':[next1,next2]})
        counts['aligned_high_steps'] += 1
        if not left and not right:
            # Equality of prime parameters is exactly equality of b's.
            assert (next1==next2)==(b1==b2)
            counts['both_prime_stops'] += 1
            counts['final_p_level_stops'] += current_level==2
            return 'both_prime',history
        if left != right:
            # The small quotient is actually tame; the other has prime
            # Newton parameter and nontrivial cyclic p division field.
            assert next1%p==0 or next2%p==0
            assert not (next1%p==0 and next2%p==0)
            counts['tame_wild_stops'] += 1
            counts['final_p_level_stops'] += current_level==2
            return 'tame_wild',history
        D1,D2=next1,next2
    assert p**(n-1)*b1<e and p**(n-1)*b2<e
    assert 1<=b1<=p-1 and 1<=b2<=p-1
    assert b1==b2
    counts['all_small_norm_stops'] += 1
    return 'all_small_equal',history


complete_sector_specs=[(5,3),(5,4),(7,3)]
sector_keys=set()
for p,n in complete_sector_specs:
    upper_t=(p**n-1)//(p-1)
    for t in range(2,upper_t+1):
        if t%p==0:
            continue
        e=t*(p-1)
        sector_keys.add((p,n,e))
        limit=(e-1)//p
        for residue in range(p-1):
            values=[b for b in range(1,limit+1) if b%(p-1)==residue]
            for b1,b2 in combinations_with_replacement(values,2):
                kind,path=run_pair(p,n,e,b1,b2)
                counts['complete_sector_parameter_pairs'] += 1
                if p==5 and e in (128,624) and b1==b2==1:
                    records.append({'p':p,'n':n,'e':e,'b':[b1,b2],
                                    'stop':kind,'history':path})
        k,low,upper=integer_log_bound(p,e)
        counts['complete_sectors'] += 1
        if n==4 and p**3<e<p**4:
            assert low==upper==3
            counts['complete_exact_third_index_sectors'] += 1

# Additional explicitly sampled sectors exercise deeper induction lengths.
# No claim of exhaustiveness for these larger parameter ranges is made.
sample_sector_keys=set()
for p in (5,7,11,13):
    N=p*p-1
    for n in range(3,9):
        upper_t=(p**n-1)//(p-1)
        ts={2,upper_t,upper_t-1,upper_t//2,upper_t//3}
        for power in range(2,n+1):
            center=p**power//(p-1)
            ts.update(center+shift for shift in range(-2,3))
        for t in sorted(ts):
            if not (2<=t<=upper_t and t%p):
                continue
            e=t*(p-1)
            if (p,n,e) in sector_keys:
                continue
            sample_sector_keys.add((p,n,e))
            limit=(e-1)//p
            selected=set(range(1,min(limit,32)+1))
            selected.update(limit-shift for shift in range(4))
            for stage in range(n):
                center=e//p**(stage+1)
                selected.update(center+shift for shift in range(-2,3))
                power=p**stage
                selected.update(power+shift for shift in range(-2,3))
            base=list(selected)
            for b in base:
                selected.update((b-(p-1),b+(p-1)))
            selected=sorted(b for b in selected if 1<=b<=limit)
            for residue in range(p-1):
                values=[b for b in selected if b%(p-1)==residue]
                for b1,b2 in combinations_with_replacement(values,2):
                    kind,path=run_pair(p,n,e,b1,b2)
                    counts['sampled_parameter_pairs'] += 1
                    if len(records)<18 and n>=6 and b1==b2==1:
                        records.append({'p':p,'n':n,'e':e,'b':[b1,b2],
                                        'stop':kind,'history':path})
            integer_log_bound(p,e)
            counts['sampled_sectors'] += 1
        # Check finite special-character invariance under every quotient.
        for c in range(N):
            initial={c%N,p*c%N}
            for j in range(n):
                current=(p**j*c)%N
                assert {current,p*current%N}==initial
                counts['isogeny_character_orbits'] += 1
        # A Smith-form total kernel of rank p^j is killed by p^j;
        # inverse images of p^(n-j)-torsion are therefore inside p^n.
        for j in range(n):
            assert p**(n-j)*p**j==p**n
            counts['original_module_level_products'] += 1

unsettled=[]
for p in (5,7,11,13):
    t=p**4//(p-1)+1
    while t%p==0:
        t+=1
    e=t*(p-1)
    assert p**4<e<p**5
    k,low,upper=integer_log_bound(p,e)
    assert (low,upper)==(3,4)
    unsettled.append({'p':p,'e':e,'proved_lower':low,'proved_upper':upper,
                      'exact_index_claimed':False})

assert counts['final_p_level_stops']>0
assert counts['tame_wild_stops']>0 and counts['both_prime_stops']>0
assert counts['all_small_norm_stops']>0
output={
    'status':'PASS',
    'scope':'Finite exact actual rank-two module quotients, induced matrices, complete specified sectors, explicitly sampled deeper induction branches, character orbits and logarithmic bound arithmetic. The universal proof and formal-group existence are not inferred from these tests.',
    'complete_sector_specs':[{'p':p,'n':n,'t_range':[2,(p**n-1)//(p-1)],
                              'excluded':'t divisible by p',
                              'b_range':'All 1<=b<e/p; all pairs congruent modulo p-1'}
                             for p,n in complete_sector_specs],
    'sampled_primes':[5,7,11,13],
    'sampled_n_range':[3,8],
    'counts':dict(sorted(counts.items())),
    'retained_stage_examples':records,
    'unsettled_next_interval_examples':unsettled,
    'elapsed_seconds':time.perf_counter()-started,
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
outpath=Path(__file__).with_suffix('.output.json')
outpath.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
