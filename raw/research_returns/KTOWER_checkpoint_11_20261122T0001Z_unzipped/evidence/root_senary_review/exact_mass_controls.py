"""Exact small normalization controls for the senary trace, not a mass proof."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib
import json
from sympy import Rational, bernoulli, factorint, kronecker_symbol

BASE = Path(__file__).resolve().parents[2]
rows = []
for disc in (-3, -7, -79):
    conductor = -disc
    b3 = sum(
        Fraction(int(kronecker_symbol(disc, a)))
        * (Fraction(a**3, conductor) - Fraction(3*a*a, 2)
           + Fraction(conductor*a, 2))
        for a in range(1, conductor + 1)
    )
    beta3 = b3 / 3
    mass = beta3 / (2**(len(factorint(conductor))-1) * 23040)
    rows.append(dict(D=disc, B3=str(b3), beta3=str(beta3), mass=str(mass)))
assert [row['mass'] for row in rows] == ['1/103680', '1/10080', '31/720']
b17 = sum(
    Rational(int(kronecker_symbol(-79, a))) * 79**16
    * bernoulli(17, Rational(a, 79))
    for a in range(1, 80)
)
beta17 = b17 / 17
reduction = int(beta17.p) * pow(int(beta17.q), -1, 31) % 31
assert reduction == 20
report = dict(
    date_utc=datetime.now(timezone.utc).isoformat(),
    scope='Exact Bernoulli polynomial controls; no general local density re-proof.',
    rows=rows,
    beta17_mod31=reduction,
    trace_mod31=0,
    individual_coefficient_mod31=(-reduction) % 31,
    proof_sha256=hashlib.sha256(
        (BASE/'evidence/main_gate/senary_trace_detector.tex').read_bytes()
    ).hexdigest(),
)
print(json.dumps(report, indent=2))
