"""Run the full verifier with zero-term deletion and integer Faddeev recursion.

Every mathematical check remains enabled. Two exact arithmetic rewrites
omit zero harmonic terms and clear denominators in the Faddeev recursion.
The frozen verifier is read, not modified. Additional prints expose stages.
The rational matrix is cleared by its exact common denominator D; integer
Faddeev coefficients are then divided by D**i, with all checks retained.
"""
from pathlib import Path
import sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'harmonic_hecke_certificate.py'
source = SOURCE.read_text()
old = '''def harmonic_evaluate(expanded, k, H, z, w):
    values = orbit_values(expanded, k, z, w)
    return ([sum(H[i][j]*values[i][0] for i in range(len(H))) for j in range(len(H[0]))],
            [sum(H[i][j]*values[i][1] for i in range(len(H))) for j in range(len(H[0]))])
'''
new = '''_harmonic_sparse_cache = (None, None)

def harmonic_evaluate(expanded, k, H, z, w):
    global _harmonic_sparse_cache
    if _harmonic_sparse_cache[0] is not H:
        columns = [tuple((i, H[i][j]) for i in range(len(H)) if H[i][j])
                   for j in range(len(H[0]))]
        _harmonic_sparse_cache = (H, columns)
    columns = _harmonic_sparse_cache[1]
    values = orbit_values(expanded, k, z, w)
    return ([sum(c*values[i][0] for i,c in column) for column in columns],
            [sum(c*values[i][1] for i,c in column) for column in columns])
'''
assert source.count(old) == 1
source = source.replace(old,new)
stages = [
 ("    assert all(x == 0 for row in matmul(lap, H) for x in row)\n",
  "    print(json.dumps({'stage':'complete harmonic kernel','e':e,'dimension':d}),flush=True)\n"),
 ("    assert det and str(det) == degree['evaluation_determinant']\n",
  "    print(json.dumps({'stage':'exact identifying determinant','e':e}),flush=True)\n"),
 ("        assert B1 == [list(map(int, row)) for row in record['transformed_evaluations_omega']]\n",
  "        print(json.dumps({'stage':'all transformed evaluations','e':e,'p':p}),flush=True)\n"),
 ("        assert poly == record['charpoly_coefficients']\n",
  "        print(json.dumps({'stage':'whole characteristic polynomial','e':e,'p':p}),flush=True)\n"),
]
for anchor,progress in stages:
    assert source.count(anchor) == 1
    source = source.replace(anchor,anchor+progress)
old_faddeev = '''def characteristic_polynomial(a):
    # Faddeev--LeVerrier with exact rational arithmetic.
    n = len(a)
    b = identity(n)
    coefficients = [F(1)]
    for k in range(1, n+1):
        b = matmul(a, b)
        c = -sum(b[i][i] for i in range(n))/F(k)
        coefficients.append(c)
        for i in range(n):
            b[i][i] += c
    assert all(x == 0 for row in b for x in row)
    return coefficients
'''
new_faddeev = '''def characteristic_polynomial(a):
    # det(X-DA)=D**n det(X/D-A), with exact integer Faddeev.
    from math import lcm
    n = len(a)
    denominator = lcm(*(x.denominator for row in a for x in row))
    integral = [[x.numerator*(denominator//x.denominator) for x in row]
                for row in a]
    assert all(F(integral[i][j],denominator) == a[i][j]
               for i in range(n) for j in range(n))
    b = identity(n)
    coefficients = [F(1)]
    for k in range(1,n+1):
        b = matmul(integral,b)
        quotient,remainder = divmod(sum(b[i][i] for i in range(n)),k)
        assert remainder == 0
        c = -quotient
        coefficients.append(F(c,denominator**k))
        for i in range(n):
            b[i][i] += c
    assert all(x == 0 for row in b for x in row)
    return coefficients
'''
assert source.count(old_faddeev) == 1
source = source.replace(old_faddeev,new_faddeev)
exec(compile(source,str(SOURCE),'exec'),{'__name__':'__main__','__file__':str(SOURCE)})
