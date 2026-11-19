"""Exact arithmetic certificate for the bounded BGV v2 wording check."""
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
import json

q = 2
tate_index = 1
cohomological_shift = 2
eigenvalue = Fraction(q) ** (-tate_index)
inverse_twist_eigenvalue = Fraction(q)
weight = -2 * tate_index
checks = {
    'inverse_twist_normalization': eigenvalue * inverse_twist_eigenvalue == 1,
    'cohomological_degree_matches_weight': -cohomological_shift == weight,
    'spectral_weight': eigenvalue ** 2 == Fraction(q) ** weight,
    'reduced_denominator_nontrivial': eigenvalue.denominator == 2,
    'not_a_rational_algebraic_integer': eigenvalue.denominator != 1,
}
assert all(checks.values())
record = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'source_version': 'arXiv:2306.05099v2',
    'source_locators': 'Definition2.42(3), Example2.43(2), Example3.29(1), Definition4.40, Remark4.41, Proposition4.44(2)',
    'field': 'F_2',
    'object': '1(1)[2]',
    'nonzero_cohomological_degree': -cohomological_shift,
    'spectral_weight': weight,
    'eigenvalue': str(eigenvalue),
    'numerator': eigenvalue.numerator,
    'denominator': eigenvalue.denominator,
    'checks': checks,
    'status': 'all exact arithmetic checks passed',
    'scope': 'Literal algebraic-integrality wording only; no monodromy-equivalence or final comparison theorem refutation.',
}
out = Path(__file__).resolve().parents[1] / 'output' / 'bgv_twist_purity_certificate.json'
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
