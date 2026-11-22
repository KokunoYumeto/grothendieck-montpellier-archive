#!/usr/bin/env python3
"""Certificate for the rejected PD-torsion-free candidate F_p[x,y,z]/(xy,xz).

The universal PD presentation is proved in notes/B_research.md, using
Stacks Lemma 60.2.4 (07HC). In multidegree (p^2+p,p^2,p^2), its relations
are the linear divided-power relations and all scalar syzygies
z^q gamma_q(xy) = y^q gamma_q(xz), with their divided-monomial multiples.
The coefficient of the (p^2,p) basis vector is an F_p-linear functional
annihilating EVERY relation in this finite graded presentation. It
evaluates to 1 on the explicitly p-torsion class tau. The proof in the
notes handles all primes; this certificate checks p=2,3,5,7.

This is a supplementary rejected-candidate certificate. It is not the
finite detector certificate requested for the original three bases;
that independent certificate is B_finish_PD_detector.py.
"""
from math import comb
from pathlib import Path
import datetime
import hashlib
import json
import time


def certify(p):
    started = time.monotonic()
    a, b, c = p*p+p, p*p, p*p
    corner = (p*p, p)
    other = (p, p*p)
    pts = {(m, n) for m in range(min(a, b)+1)
           for n in range(min(a-m, c)+1)}
    counts = {'linear': 0, 'syzygy': 0}

    def check(terms, kind):
        counts[kind] += 1
        assert all(pos in pts for pos, _ in terms)
        assert sum(co for pos, co in terms if pos == corner) % p == 0

    for m, n in pts:
        if (m+1, n) in pts:
            check([((m+1, n), m+1), ((m, n), -1)], 'linear')
        if (m, n+1) in pts:
            check([((m, n+1), n+1), ((m, n), -1)], 'linear')
        for q in range(1, min(a-m-n, b-m, c-n)+1):
            check([((m+q, n), comb(m+q, q)),
                   ((m, n+q), -comb(n+q, q))], 'syzygy')

    # The q=p^2-p syzygy multiplied by gamma_p(xy)gamma_p(xz)
    # gives binom(p^2,p)*tau=0. This coefficient is p times a p-adic unit.
    multiplier = comb(p*p, p)
    assert multiplier % p == 0 and multiplier % (p*p) != 0
    assert corner in pts and other in pts and corner != other
    tau = [(corner, 1), (other, -1)]
    tau_value = sum(co for pos, co in tau if pos == corner) % p
    assert tau_value == 1
    return {'p': p, 'multidegree': [a,b,c], 'basis_size': len(pts),
            'relations_checked': counts, 'functional': {'corner': list(corner)},
            'annihilates_all_relations': True, 'tau_image': tau_value,
            'torsion_multiplier': str(multiplier), 'multiplier_p_valuation': 1,
            'tau_is_nonzero_p_torsion': True,
            'seconds': round(time.monotonic()-started,6)}


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    out = {
        'statement': 'Rejected candidate F_p[x,y,z]/(xy,xz) is not PD torsion free',
        'status': 'finite graded certificates; all-prime proof in notes/B_research.md',
        'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
        'model_run': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); RESEARCH_SA17_FINISH-20261119; agent dieudonne',
        'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'results': [certify(p) for p in (2,3,5,7)]}
    (root/'logs/B_finish_PD_two_generator.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
