"""Bounded exact product-Cartier determinant probe, separate from the paper.

The coefficient matrices are copied literally from the proved DE-XC1 and
the untwisted elliptic matrix.  This checks full nine-variable polynomials,
not only their restriction to decomposable functionals.  No indecomposable
ppav or global monodromy conclusion is inferred.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import signal
import time
import traceback
import sympy as sp
from sympy.polys.matrices import DomainMatrix

start = time.perf_counter()
out = Path(__file__).with_suffix('.output.json')
result = {'status': 'RUNNING', 'actual_utc': datetime.now(timezone.utc).isoformat(),
          'scope': 'Two explicit twists on the supersingular elliptic product; complete nine-variable determinant and derivative gcd only.',
          'cases': []}

def save():
    result['runtime_seconds'] = time.perf_counter()-start
    out.write_text(json.dumps(result, indent=2)+'\n')

def timeout(signum, frame):
    raise TimeoutError('Retained bounded 90-second determinant/gcd probe timed out')

signal.signal(signal.SIGALRM, timeout)
signal.alarm(90)
save()
try:
    xs = sp.symbols('x00 x01 x02 x10 x11 x12 x20 x21 x22')
    domain = sp.GF(2).poly_ring(*xs)
    A = [sp.Matrix([[1,0,0],[0,0,0],[0,1,0]]),
         sp.Matrix([[0,0,1],[0,1,0],[1,0,0]]),
         sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])]
    B = [sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
         sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
         sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])]
    result['twisted_point'] = {'a': 0, 'b': 0, 'equation_check': 'b^2+b=a^3'}
    result['twisted_coefficients'] = [[[int(v) for v in row] for row in a.tolist()] for a in A]
    result['untwisted_coefficients'] = [[[int(v) for v in row] for row in b.tolist()] for b in B]
    for name, second in [('one_nontrivial_factor', B), ('two_nontrivial_factors', A)]:
        case_start = time.perf_counter()
        mat = sum((xs[3*i+j]*sp.kronecker_product(A[i], second[j])
                   for i in range(3) for j in range(3)), sp.zeros(9))
        dm = DomainMatrix.from_Matrix(mat).convert_to(domain)
        d = dm.det()
        expr = domain.to_sympy(d)
        poly = sp.Poly(expr, *xs, modulus=2)
        row = {'case': name, 'determinant_total_degree': poly.total_degree(),
               'determinant_term_count': len(poly.terms()),
               'determinant_terms': [[list(m), int(c)%2] for m,c in poly.terms()],
               'determinant_seconds': time.perf_counter()-case_start}
        result['cases'].append(row)
        save()
        common = poly
        derivative_data = []
        for x in xs:
            derivative = poly.diff(x)
            derivative_data.append({'variable': str(x), 'term_count': len(derivative.terms()) if not derivative.is_zero else 0})
            common = sp.gcd(common, derivative)
            if common.total_degree() == 0:
                break
        row['derivatives_inspected'] = derivative_data
        row['derivative_gcd_degree'] = common.total_degree()
        row['derivative_gcd_terms'] = [[list(m), int(c)%2] for m,c in common.terms()]
        row['case_seconds'] = time.perf_counter()-case_start
        save()
    result['status'] = 'PASS'
except Exception as exc:
    result['status'] = 'FAILED_OR_BOUNDED_TIMEOUT'
    result['error_type'] = type(exc).__name__
    result['error'] = str(exc)
    result['traceback'] = traceback.format_exc()
finally:
    signal.alarm(0)
    save()
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','twisted_coefficients','untwisted_coefficients')}, indent=2))
    print(json.dumps([dict((k,v) for k,v in row.items() if not k.endswith('_terms')) for row in result['cases']], indent=2))
