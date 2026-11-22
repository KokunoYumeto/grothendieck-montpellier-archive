"""Exact exploratory 4P+gP interpolation for Rosati norm seventeen.

This script proves only its displayed polynomial identities. It does not
assert that any theta image is nodal or that its fibres have size at most two.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, signal, time, traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start = time.perf_counter()
agent = Path(__file__).resolve().parents[1]
result = {'status': 'RUNNING'}
def timeout(*unused):
    raise TimeoutError('Norm-seventeen interpolation exceeded60seconds')
signal.signal(signal.SIGALRM, timeout)
signal.alarm(60)
try:
    zz = symbols('z')
    base = GF(2).frac_field(zz)
    z = base.gens[0]
    R, p, beta, X, l, c = ring('p,beta,X,l,c', base)
    con = R.ground_new
    a, b, delta = con(z*z), con(z*z+z+1), con(z+1)
    relation = beta*beta+beta+delta
    red = lambda f: f.div([relation])[1]
    checks = []
    def check(name, f):
        rem = red(f)
        assert not rem, (name, str(rem))
        checks.append(name)
    d1 = a*p**4+b*p*p
    d2 = d1*d1+b*p
    G = con(z)*p*p+delta*p+beta
    Z = red(G+d1+d2)
    Yseries = d1*X+d2*X*X+b*X**3
    arbitrary = c*d1*X+(l*d1+c*d2)*X**2+(l*d2+c*b)*X**3
    check('order_four_at_P', ((l*X+c)*Yseries+arbitrary).div([X**4])[1])
    arbitrary_value = (l+c)*G+c*d1+(l*d1+c*d2)+(l*d2+c*b)
    check('single_value_row_at_gP', arbitrary_value+Z*l+(Z+b)*c)
    chosen_l, chosen_c = Z+b, Z
    check('chosen_row_kernel', Z*chosen_l+(Z+b)*chosen_c)
    linear = chosen_l*X+chosen_c
    poly = chosen_c*d1*X+(chosen_l*d1+chosen_c*d2)*X**2+(chosen_l*d2+chosen_c*b)*X**3
    fun = lambda x: a*x**5+b*x**3
    norm = red(poly*poly+linear*poly+linear*linear*(fun(p+X)+fun(p)))
    quotient, rem = norm.div([X**4*(X+1)])
    assert not rem, str(rem)
    residual = red(quotient[0])
    checks.append('full_norm_divides_X4_Xplus1')
    def coefficient_x(f, degree):
        return R({(m[0],m[1],0,m[3],m[4]):value
                  for m,value in f.items() if m[2] == degree})
    A = coefficient_x(residual, 2)
    B = coefficient_x(residual, 1)
    C = coefficient_x(residual, 0)
    check('full_quadratic_residual', residual+A*X**2+B*X+C)
    check('leading_residual_coefficient', A+a*(Z+b)**2)
    # Here Z is the explicit degree-eight additive polynomial. Keeping it
    # literal makes all input coefficients reconstructible without a search.
    result.update({'status': 'PASS_UNIVERSAL_INTERPOLATION_ONLY',
                   'checks': checks, 'Z': str(Z), 'A': str(A), 'B': str(B), 'C': str(C),
                   'scope': 'Six universal characteristic-two identities for 4P+gP and its quadratic residual. The row is nonzero if b!=0. No triple-fibre, nodality, or degree17 monodromy conclusion; b=0 remains separately untreated.'})
except Exception:
    result.update({'status': 'EXPLORATORY_FAILURE', 'traceback': traceback.format_exc()})
finally:
    signal.alarm(0)
    result['actual_utc'] = datetime.now(timezone.utc).isoformat()
    result['runtime_seconds'] = time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_interpolation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
