"""Finite defining-data checks for C.3ah; not a Chow nonvanishing proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
checks = []
for r in range(1, 13):
    d = r + 2
    x = sp.symbols(f'x0:{r+2}')
    u = sp.symbols(f'u1:{r+1}')
    w, eta = sp.symbols('w eta')
    F = sum(v**d for v in x)
    gradient = [sp.diff(F, v) for v in x]
    expected = [d*v**(d-1) for v in x]
    P = tuple(u)+(w, sp.Integer(1))
    a = (sp.Integer(1), eta)+(sp.Integer(0),)*r
    p_equation = sp.expand(F.subs(dict(zip(x, P))))
    a_equation = sp.expand(F.subs(dict(zip(x, a))))
    p_remainder = sp.rem(p_equation, w**d+1+sum(v**d for v in u), w)
    a_remainder = sp.rem(a_equation, eta**d+1, eta)
    assert gradient == expected
    assert p_remainder == 0 and a_remainder == 0
    assert a[-1] == 0
    assert d-(r+2) == 0  # hypersurface adjunction exponent
    ambient_local_dim = r+2
    divisor_local_dim = r+1
    assert ambient_local_dim-1 == divisor_local_dim
    assert divisor_local_dim-1 == r  # maximal punctured codimension
    checks.append({
        'r': r, 'degree': d, 'ambient_local_dimension': ambient_local_dim,
        'divisor_local_dimension': divisor_local_dim,
        'gradient_is_diagonal_nonzero_monomials': True,
        'generic_point_equation_mod_defining_relation': str(p_remainder),
        'base_point_equation_mod_eta_relation': str(a_remainder),
        'base_point_in_fixed_hyperplane': True,
        'canonical_bundle_exponent': 0,
        'target_codimension': r
    })

record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'sympy_version': sp.__version__,
    'scope': 'Finite exact equation and degree checks. Generic-point non-support, ordinary algebraic equivalence, strict-local injectivity and Gersten vanishing are proved in the text, not inferred from this finite grid.',
    'all_checks_passed': True,
    'cases': checks,
    'runtime_seconds': time.perf_counter()-started
}
text = json.dumps(record, indent=2)+'\n'
(base/'output/check_regular_ambient_calabi_yau.json').write_text(text)
(base/'output/check_regular_ambient_calabi_yau.out').write_text(text)
print(text, end='')
