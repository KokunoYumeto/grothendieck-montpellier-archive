#!/usr/bin/env python3
"""AM-R-018: exact source-weight spreads and finite fixed-T size intervals.

The primality of the input T is carried from R017's separate exact
certificate. No Lean execution or complete MainX size-window claim.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
inp = ROOT / 'checks/explicit_t_prime_and_stabilizer_certificate.json'
cases = json.loads(inp.read_text())['cases']
out = []
for c in cases:
    k, f, C, T = c['a'], c['f'], c['C'], c['T']
    d = c['b'] - k
    assert d % 2 == 0
    # Literal hcToWeightQ and lamN_eq, then the lamTrue scalar shift.
    w0 = [(2*(k-i)+1)*C + 1-k//2+i for i in range(k)]
    e = [0, 4*C]
    weights = []
    for j in range(3):
        w = [x-j*d//2 for x in w0]
        for block in range(j):
            val = -e[block]+k//2+(2*block+1-j)*d//2
            w += [val]*d
        assert len(w) == k+j*d
        assert all(w[i] >= w[i+1] for i in range(len(w)-1))
        weights.append(w)
    # DataCoeff.spread includes the rank, not just first minus last.
    spreads = [w[0]-w[-1]+len(w) for w in weights]
    closed = [2*(k-1)*C+1,
              (2*k+1)*C+1+d//2,
              (2*k+5)*C+1+d//2]
    assert spreads == closed and spreads[0] < spreads[1] < spreads[2]
    S = spreads[2]
    assert all(2*f*k < g-1 for g in (c['g0'], c['g1']))
    bound = 2*((T-1)//4)-S
    max_r = 0
    while 121*11**(max_r+1) <= bound:
        max_r += 1
    assert 121*11**max_r <= bound < 121*11**(max_r+1)
    checks = []
    for r in range(max_r+2):
        A, B = 11**r, 121*11**r
        for n in (0, A, B):
            for w, s in zip(weights, spreads):
                changed = [w[0]+n]+w[1:]
                assert changed[0]-changed[-1]+len(w) == s+n
        size = (S+B+1)//2
        assert 2*f*c['c']+1 < 4*size
        assert S+B <= 2*size
        assert (4*size < T) == (r <= max_r)
        if r == max_r+1:
            assert 2*(S+B) >= T
        checks.append(dict(r=r,first_increment=A,second_increment=B,
                           max_literal_spread=S+B,size_parameter=size,
                           four_size_parameter=4*size,T_gt=(4*size<T)))
    out.append(dict(name=c['name'],k=k,f=f,d=d,C=C,T=T,
                    baseline_spreads=spreads,max_r=max_r,
                    baseline_covers_size_gt=True,all_g_big=True,
                    bound_for_B=bound,checks=checks))
dest = ROOT / 'checks/selected_fixed_prime_sizes_certificate.json'
dest.write_text(json.dumps(dict(statement_id='AM-R-018',
    scope='Exact literal source weight/size arithmetic; complete global SizeData2 is not asserted.',
    input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),cases=out),indent=2)+'\n')
print(json.dumps([dict(name=x['name'],baseline_spreads=x['baseline_spreads'],
                       max_r=x['max_r'],last_size=x['checks'][-2]['size_parameter'])
                  for x in out],indent=2))
