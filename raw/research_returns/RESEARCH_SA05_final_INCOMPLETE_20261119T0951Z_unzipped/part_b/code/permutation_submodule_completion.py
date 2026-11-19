"""Finite congruence checks for the formal permutation-submodule diagnostic.

These checks do not establish the infinite inverse-limit statement, whose
proof is written in b1_milnor_divisibility_attempt.md, Section 7.
"""
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json

started_utc = datetime.now(timezone.utc).isoformat()
started_monotonic = perf_counter()
rows = []
for r in range(1, 9):
    modulus = 3 ** r
    period = 3 ** (r - 1)
    wrap = pow(4, period, modulus)
    transition_image = 3 * Fraction(1, 3 ** (r + 1)) - Fraction(1, modulus)
    eigen_image = (Fraction(1, modulus) - 4 * Fraction(1, modulus)
                   if r == 1 else
                   Fraction(4, modulus) - 4 * Fraction(1, modulus))
    assert wrap == 1
    assert transition_image.denominator == 1
    assert eigen_image.denominator == 1
    assert all(Fraction(3 ** s, modulus).denominator != 1 for s in range(r))
    assert Fraction(3 ** r, modulus).denominator == 1
    rows.append({
        'r': r,
        'modulus': modulus,
        'cycle_length': period,
        'four_to_cycle_length_mod_modulus': wrap,
        'transition_parenthesis_image_mod_Z': '0',
        'eigen_parenthesis_image_mod_Z': '0',
        'lambda_class_order': modulus,
    })

result = {
    'scope': 'Finite levels 1 through 8 only; infinite proof is separate.',
    'started_utc': started_utc,
    'finished_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': perf_counter() - started_monotonic,
    'checks': rows,
}
out = Path(__file__).resolve().parents[1] / 'output/permutation_submodule_completion.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
