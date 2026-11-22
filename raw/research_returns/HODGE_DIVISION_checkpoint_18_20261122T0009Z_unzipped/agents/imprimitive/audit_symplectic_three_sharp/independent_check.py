"""Independent integer arithmetic for D-HOS-16; no author code imported.

The mathematical/source audit is separate. This file certifies only exact
constants, thresholds and the numerical contradiction used in that audit.
"""
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import time

start = time.perf_counter()
root = Path(__file__).resolve().parent
siblings = root.parent.parent / 'g34_eightfolds' / 'bireflection'
proof = siblings / 'higher_odd_symplectic_three_sharp_section.tex'
published = siblings / 'sources' / 'LST2011_Waring_published.pdf'
assert sha256(proof.read_bytes()).hexdigest() == 'ce8fc689891738dbf571cdae6f92879bca88937129ac66bf278b6ec6f72cdd3f'
assert sha256(published.read_bytes()).hexdigest() == 'dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e'

def reduced(a, b):
    assert b > 0
    g = gcd(a, b)
    return a // g, b // g

def less(a, b):
    return a[0] * b[1] < b[0] * a[1]

# Derive the rational constant from integer exponentiation, then compare by
# cross multiplication; the author's Fraction implementation is not used.
c_num, c_den = 19**9, 20**9
assert (c_num, c_den) == (322687697779, 512000000000)
delta = reduced(c_den - c_num, 2 * c_den)
assert delta == (189312302221, 1024000000000)
assert less((1, 6), delta)
assert less(delta, (2, 9))
assert less((2, 9), (1, 4))
assert less(delta, (4, 15))

# The first published exponent is sqrt(N/7), so N=7*9^2 makes it 9.
N = 7 * 9**2
assert N == 567
assert 2 * 283 < N <= 2 * 284
assert (2 * 284 - N) == 1
assert reduced(1 * (9 - 1), 4 * 9) == (2, 9)
assert reduced(1 * 4 * (3 - 1), 2 * 5 * 3) == (4, 15)

# 12 delta e <= 2e+6. Derive the ceiling by clearing the denominator.
dnum, dden = delta
denominator = 12 * dnum - 2 * dden
assert denominator > 0
ceiling = reduced(6 * dden, denominator)
assert ceiling == (1536000000000, 55936906663)
assert less(ceiling, (28, 1))
assert 3**283 > 28

# Verify every integer degree at/above the first excluded integer directly
# by the positive slope, without a floating-point boundary comparison.
assert 28 * denominator > 6 * dden
assert 27 * denominator <= 6 * dden

out = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds': time.perf_counter() - start,
    'scope': 'Independent integer constants only; published theorem and universal group argument audited separately',
    'author_code_imported': False,
    'author_code_previously_read': True,
    'c_star': [c_num, c_den],
    'delta_star': list(delta),
    'source_degree_ceiling': list(ceiling),
    'maximum_integral_source_degree': 27,
    'published_support_threshold': N,
    'first_excluded_half_rank': 284,
    'surviving_transitive_half_ranks': [4, 283],
    'proof_sha256': sha256(proof.read_bytes()).hexdigest(),
    'published_pdf_sha256': sha256(published.read_bytes()).hexdigest(),
    'model': 'GPT-6 Astra Pro',
    'effort': 'inherited/not exposed',
    'run': 'HODGE_DIVISION',
}
(root / 'independent_checked.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
