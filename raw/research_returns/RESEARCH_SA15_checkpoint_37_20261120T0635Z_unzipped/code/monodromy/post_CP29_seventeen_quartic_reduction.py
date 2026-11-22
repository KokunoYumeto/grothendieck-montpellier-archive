"""Universal quartic necessary conditions for norm seventeen, exploratory."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
import json, signal, time, traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start = time.perf_counter()
agent = Path(__file__).resolve().parents[1]
result = {'status': 'RUNNING', 'stages': []}
def timeout(*unused):
    raise TimeoutError('Norm-seventeen quartic reduction exceeded60seconds')
def stage(name):
    row = {'stage': name, 'seconds': time.perf_counter()-start}
    result['stages'].append(row)
    print(json.dumps(row), flush=True)
signal.signal(signal.SIGALRM, timeout)
signal.alarm(60)
try:
    zz = symbols('z')
    base = GF(2).frac_field(zz)
    z = base.gens[0]
    R, p, T, V, L, beta = ring('p,T,V,L,beta', base)
    con = R.ground_new
    a, b, delta = con(z*z), con(z*z+z+1), con(z+1)
    e = 1/(b*b)
    relp = p*p+L*p+V+e*(T*T+T)
    relT = T**4+T**3+a*L*T*T+b**4
    reduce = lambda f: f.div([relp, relT])[1]
    def coefficient(f, index, degree):
        out = {}
        for monomial, value in f.items():
            if monomial[index] == degree:
                m = list(monomial)
                m[index] = 0
                out[tuple(m)] = value
        return R(out)
    Zexplicit = a*a*p**8+(a*a+1)*p**4+(a+1)*p*p+a*p+beta
    A = a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    right = reduce(Zexplicit+T+b+A*p)
    assert right.degree(p) <= 0
    B = [coefficient(right, 1, j) for j in range(4)]
    assert not reduce(Zexplicit+T+b+A*p+sum(B[j]*T**j for j in range(4)))
    assert all(B[j].degree(V) <= 0 and B[j].degree(beta) <= 0 for j in (1,2,3))
    positive = B[1]*T+B[2]*T*T+B[3]*T**3
    Q = reduce(positive*positive+L*A*positive+A*A*e*(T*T+T))
    r1, r2, r3 = [coefficient(Q, 1, j) for j in (1,2,3)]
    F = r1*r3+a*L*r3*r3+r2*r3+r2*r2
    G = b**4*r3**3+(r3+r2)**2*r1
    stage('quartic_reduction_and_three_root_conditions')
    # Multiplication by the positive-degree part of B in the exact quartic
    # algebra, followed by a literal 24-permutation determinant.
    columns = [reduce(positive*T**j) for j in range(4)]
    matrix = [[coefficient(columns[j], 1, i) for j in range(4)] for i in range(4)]
    zero, one = R.zero, R.one
    def polyadd(x, y):
        return [(x[i] if i<len(x) else zero)+(y[i] if i<len(y) else zero) for i in range(max(len(x),len(y)))]
    def polymul(x, y):
        out = [zero]*(len(x)+len(y)-1)
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                out[i+j] += xi*yj
        return out
    characteristic = [zero]*5
    for perm in permutations(range(4)):
        term = [one]
        for i, j in enumerate(perm):
            term = polymul(term, [matrix[i][j], one] if i==j else [matrix[i][j]])
        characteristic = polyadd(characteristic, term)
    assert characteristic[4] == one
    c0,c1,c2,c3,_ = characteristic
    H = c1*c1+c1*c2*c3+c0*c3*c3
    stage('four_by_four_characteristic_polynomial')
    for name, f in [('A',A),('F',F),('G',G),('H',H)]:
        assert all(m[0] == m[1] == m[2] == m[4] == 0 for m in f), name
    def serialize(f):
        coeffs = [coefficient(f,3,j).get((0,0,0,0,0),base.zero) for j in range(max(0,f.degree(L))+1)]
        def binary(poly):
            return sum((int(value)%2)<<m[0] for m,value in poly.items())
        return [[binary(c.numer),binary(c.denom)] for c in coeffs]
    result.update({'status':'PASS_EXACT_QUARTIC_NECESSARY_CONDITIONS_ONLY',
                   'degrees_L':{name:f.degree(L) for name,f in [('A',A),('F',F),('G',G),('H',H)]},
                   'polynomials':{name:serialize(f) for name,f in [('A',A),('F',F),('G',G),('H',H)]},
                   'B_positive':[str(B[j]) for j in (1,2,3)],
                   'scope':'When b!=0 and T!=0, the residual coefficient gives a separable quartic. A!=0 triple fibres imply F=G=0; A=0 triples imply a collision of B-values, hence H=0. Exact identities only; resultants and all exceptional fibres remain unchecked.'})
except Exception:
    result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0)
    result['actual_utc']=datetime.now(timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_quartic_reduction.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('polynomials','B_positive')},indent=2))
