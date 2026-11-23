"""G170 research: the1072 additional odd character components of H48.

Exact primitive-conductor floor operators; finite arithmetic only.  This
does not prove reflection, even-class vanishing, strict zero or a window.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd, isqrt
import hashlib
import json

BASE = Path(__file__).resolve().parent
P, I = 269, 82
assert all(P % q for q in range(2, isqrt(P)+1))
assert I*I % P == P-1
powers = [pow(2, j, P) for j in range(P-1)]
assert len(set(powers)) == P-1
phi_exp = {1: 0, 7: 0, 13: 1, 11: 1, 9: 2, 15: 2, 5: 3, 3: 3}

def tame_value(n, sigma, a, b, inverse=False):
    if n % 2 == 0 or (b and n % 3 == 0):
        return 0
    e = sigma*phi_exp[n % 16]
    if inverse:
        e = -e
    out = pow(I, e, P)
    if a and n % 4 == 3:
        out = -out
    if b and n % 3 == 2:
        out = -out
    return out % P

def horner(coefficients, x):
    out = 0
    for c in reversed(coefficients):
        out = (out*x+c) % P
    return out

rows = []
for sigma in (1, -1):
    for a in (0, 1):
        for b in (0, 1):
            f0 = 16*3**b
            # phi(9)=-1 forces the exact2-part16; the chi_-3 factor,
            # when present, has its coprime primitive3-part.
            assert tame_value(9 if not b else 25, sigma, a, b) == P-1
            f = f0*P
            operators = [c for c in range(2, 32) if gcd(c, f) == 1]
            bins = {c: [0]*P for c in operators}
            for n in range(1, f+1):
                if gcd(n, f) == 1:
                    weight = tame_value(n, sigma, a, b, inverse=True)
                    for c in operators:
                        bins[c][n % P] = (bins[c][n % P]+weight*(c*n//f)) % P
            ordered = {c: [bins[c][r] for r in powers] for c in operators}
            for k in range(P-1):
                if (k+a+b) % 2 != 0:
                    continue
                assert tame_value(-1, sigma, a, b)*pow(P-1, k, P) % P == P-1
                if k == 0:
                    modulus = f0
                    values = {
                        c: sum(tame_value(n, sigma, a, b, inverse=True)*(c*n//f0)
                               for n in range(1, f0+1) if gcd(n, f0) == 1) % P
                        for c in operators
                    }
                else:
                    modulus = f
                    ratio = pow(2, -k, P)
                    values = {c: horner(ordered[c], ratio) for c in operators}
                nonzero = next((c for c in operators if values[c] != 0), None)
                rows.append({
                    'sigma': sigma, 'a': a, 'b': b, 'k': k,
                    'primitive_conductor': modulus,
                    'character': 'phi16^sigma*chi_-4^a*chi_-3^b*omega269^k',
                    'integral_operator': '(c-sigma_c)theta_f',
                    'eigenvalue_convention': 'sum_{n unit modf}floor(cn/f)*tame(n)^(-1)*n^(-k) modulo269',
                    'values': {str(c): values[c] for c in operators},
                    'nonzero_witness': nonzero,
                    'witness_value': None if nonzero is None else values[nonzero],
                })
assert len(rows) == 1072
assert len({(r['sigma'],r['a'],r['b'],r['k']) for r in rows}) == 1072
uncovered = [{k: r[k] for k in ('sigma','a','b','k','primitive_conductor')}
             for r in rows if r['nonzero_witness'] is None]
result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'EXACT_FINITE_TABLE_ONLY_REFLECTION_STRICT_PENDING',
    'p': P, 'i_mod_p': I, 'ambient_conductor': 48*P,
    'ambient_degree': 16*(P-1),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'algorithm': 'Grouped integerfloor coefficients modulo269 followed by primitive-root Horner evaluation; exactk0primitive conductor handled separately.',
    'rows': rows, 'no_nonzero_witness': uncovered,
    'counts': {'rows': len(rows), 'nonzero_witnesses': len(rows)-len(uncovered),
               'listed_values': sum(len(r['values']) for r in rows)},
    'scope': 'Exactly1072newoddquarticcomponents, disjointfromtheoldquadraticDtables. Primitiveconductors16or48,times269onlyifk!=0. No reflection/evencomponent/strict/window theorem; zero rows refer onlyto listedoperators anddo notassertclassnonvanishing.'
}
(BASE/'quartic_odd_annihilator_table.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'rows'},indent=2))
