"""K-008: is the run's mod-16 spectral list complete?  Own enumeration and own certificate check; only data files are read.

A semistable case has every eigenvalue covered by a supported triple and can be shifted so that a supported triple
is (0,0,0); a unit scales the exponent sum to 2 (character order 8) or 1 (order 16).  So it is one of the triples of
multisets containing 0 that are enumerated below, and it must be an image of a certified row under a permutation of
the factors, a supported shift, or a unit fixing the exponent sum.
"""
import json, pathlib, sys
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product

K = pathlib.Path(sys.argv[1])
S = [X for X in combinations_with_replacement(range(16), 4) if X[0] == 0]
idx = {X: i for i, X in enumerate(S)}
mask = [sum(1 << v for v in set(X)) for X in S]
need = [[[(1 << ((-a - b) % 16)) for b in set(Y)] for a in range(16)] for Y in S]
neg = [[sum(set_) for set_ in nd] for nd in need]  # neg[j][a] = mask of -a-B
bysum = [[i for i, X in enumerate(S) if sum(X) % 16 == r] for r in range(16)]
for char, target in ((8, 2), (16, 1)):
    units = [u for u in range(1, 16, 2) if u * target % 16 == target]
    images = set()
    cnt = Counter()
    for line in (K / ('m16_chi%d_certificates.jsonl' % char)).open():
        r = json.loads(line)
        W = [tuple(X) for X in r['W']]
        sets = [sorted(set(X)) for X in W]
        mult = [Counter(X) for X in W]
        E = [e for e in product(*sets) if sum(e) % 16 == 0]
        rows = [(j, v) for j in range(3) for v in sets[j]]
        if 'y' in r:
            y = dict(zip(rows, map(Fraction, r['y'])))
            assert all(sum(y[j, e[j]] for j in range(3)) >= 0 for e in E)
            assert sum(y[j, v] * mult[j][v] for j, v in rows) < 0
            cnt['Farkas'] += 1
        else:
            x = list(map(Fraction, r['x']))
            assert len(x) == len(E) and all(t > 0 for t in x)
            assert all(sum(x[k] for k, e in enumerate(E) if e[j] == v) == mult[j][v] for j, v in rows)
            cnt['feasible'] += 1
        for e, u in product(E, units):
            images.add(tuple(sorted(idx[tuple(sorted(u * (v - e[j]) % 16 for v in X))] for j, X in enumerate(W))))
    covered = missing = 0
    for i, A in enumerate(S):
        sa = set(A)
        for j in range(i, len(S)):
            nj = neg[j]
            allowed = 0
            for a in sa:
                allowed |= nj[a]
            for k in bysum[(target - sum(A) - sum(S[j])) % 16]:
                if k < j:
                    continue
                c = mask[k]
                if c & allowed != c:
                    continue
                if any(not (nj[a] & c) for a in sa):
                    continue
                ni = neg[i]
                if any(not (ni[b] & c) for b in set(S[j])):
                    continue
                covered += 1
                if (i, j, k) not in images:
                    missing += 1
    print('character order', char, dict(cnt), '| covered normalised triples', covered, '| not represented in the list:', missing, flush=True)
