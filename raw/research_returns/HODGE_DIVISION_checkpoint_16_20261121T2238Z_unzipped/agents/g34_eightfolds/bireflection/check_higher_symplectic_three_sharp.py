"""Exact arithmetic supplement to D-HOS16; no group/source verification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import time
from datetime import datetime, timezone

start = time.perf_counter()
c = F(19, 20) ** 9
delta = (1 - c) / 2
ceiling = 6 / (12 * delta - 2)
assert c == F(322687697779, 512000000000)
assert delta == F(189312302221, 1024000000000)
assert F(1, 6) < delta < F(2, 9) < F(1, 4)
assert ceiling == F(1536000000000, 55936906663) < 28
assert 567 == 7 * 9 ** 2
assert 2 * 283 < 567 <= 2 * 284
assert 3 ** (284 - 1) > 28
assert F(1, 4) * (1 - F(1, 9)) == F(2, 9)
assert F(1, 2) * F(4, 5) * (1 - F(1, 3)) == F(4, 15) > delta

root = Path(__file__).resolve().parent
source = root / 'sources' / 'LST2011_Waring_published.pdf'
source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_sha == 'dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e'
out = {
    'status': 'PASS',
    'scope': 'Exact rational constants and thresholds only; no group enumeration or verification of the published theorem',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds': time.perf_counter() - start,
    'c_star': str(c), 'delta_star': str(delta),
    'degree_ceiling': str(ceiling),
    'published_support_threshold': 567,
    'algebraic_closure_support_half_rank_threshold': 567,
    'published_mu2_support_half_rank_threshold': 284,
    'transitive_surviving_half_rank_interval': [4, 283],
    'published_pdf_sha256': source_sha,
    'model': 'GPT-6 Astra Pro', 'effort': 'inherited/unexposed',
}
target = root / 'check_higher_symplectic_three_sharp.json'
target.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
