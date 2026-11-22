"""Bounded exact universal norm-eleven coefficient elimination.

Substitution t=v^2, r=v^2+v removes the quadratic coefficient extension.
This is exploratory algebra, not a triple-fibre or nodality certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, signal, time, traceback
from post_CP27_binary_coefficient_ring import E, G, self_check

start = time.perf_counter()
agent = Path(__file__).resolve().parents[1]
result = {"status": "RUNNING", "stages": []}


def timeout(*unused):
    raise TimeoutError("Rational-parameter universal quintic exceeded60seconds")


def stage(name, **kw):
    row = {"stage": name, "seconds": time.perf_counter()-start, **kw}
    result["stages"].append(row)
    print(json.dumps(row), flush=True)


signal.signal(signal.SIGALRM, timeout)
signal.alarm(60)
try:
    assert self_check() == 120
    zero, one = E(), E(1)
    v, L = E(2), E([0, 1])
    t, r = v*v, v*v+v
    assert t*t+t == r*r
    D = r*r
    z = (D+1)/(r**3)
    a, b = z*z, z*z+z+1
    alpha, beta = t/D, t/D+1
    gamma = (r**6+r**5+r+1)*t/(r**4)+(r**3+r+1)/(r*r)
    assert alpha == E(1, (0, 2, 0))
    assert beta == E(4, (0, 2, 0))
    assert gamma == E(G, (0, 4, 0))
    inverse_gamma = gamma.inverse_constant()
    inverse_alpha_squared = (alpha*alpha).inverse_constant()
    A4 = a*D
    A2 = (r**6+r*r+1)/(r**4)
    A1 = (r**4+1)/(r*r)
    A = A4*L**3+A2*L+A1
    theta_const = a*t**5+b*t**3+t*t*(z+1)
    L0 = a*D*D*(L+t+1)+theta_const
    aa, bb, gg = alpha*alpha, beta*beta, gamma*gamma
    C = [inverse_alpha_squared*x for x in
         [L0*gg, gg, L0*bb, bb, L0*aa+1, aa]]
    assert C[5] == one

    def trim(p):
        while p and not p[-1]:
            p.pop()
        return p

    def padd(p, q):
        return trim([(p[i] if i < len(p) else zero)+
                     (q[i] if i < len(q) else zero)
                     for i in range(max(len(p), len(q)))])

    def scale(p, c):
        return trim([x*c for x in p])

    def reduce_y(p):
        p = trim(p)
        while len(p) > 5:
            shift, lead = len(p)-6, p[-1]
            for i in range(6):
                p[shift+i] = p[shift+i]+lead*C[i]
            trim(p)
        return p

    def pmul(p, q):
        out = [zero]*(len(p)+len(q)-1) if p and q else []
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i+j] = out[i+j]+x*y
        return reduce_y(out)

    factor = t*t*inverse_gamma*inverse_gamma
    u = scale([bb*L0, bb, aa*L0+1, aa], factor)
    assert not padd(pmul(u, [zero, zero, one]), scale([L0, one], t*t))
    Zpoly = [gamma, beta, alpha]
    assert not padd(pmul(u, pmul(Zpoly, Zpoly)), [zero, zero, t*t])
    B = padd([zero, one], padd(scale(padd(scale(u, L*L), pmul(u, u)), A4), scale(u, A2)))
    P = padd(pmul(B, B), padd(scale(B, L*A), scale(u, A*A)))
    stage("quintic_and_polynomial_u")

    def matrix_of(f):
        cols = [pmul(f, [zero]*i+[one]) for i in range(5)]
        return [[col[j] if j < len(col) else zero for col in cols] for j in range(5)]

    def berkowitz(matrix):
        n = len(matrix)
        if not n:
            return [one]
        sub = [row[1:] for row in matrix[1:]]
        c = berkowitz(sub)
        toe = [one, matrix[0][0]]
        row = matrix[0][1:]
        vec = [line[0] for line in matrix[1:]]
        for power in range(n-1):
            toe.append(sum((x*y for x, y in zip(row, vec)), zero))
            if power < n-2:
                vec = [sum((x*y for x, y in zip(line, vec)), zero) for line in sub]
        return [sum((toe[i-j]*c[j] for j in range(max(0, i-n), min(i, n-1)+1)), zero)
                for i in range(n+1)]

    cp = berkowitz(matrix_of(P))
    stage("characteristic_P", L_degrees=[len(f.p)-1 for f in cp])
    cb = berkowitz(matrix_of(B))
    stage("characteristic_B", L_degrees=[len(f.p)-1 for f in cb])
    assert cp[0] == cb[0] == one
    _, c4, c3, c2, c1, c0 = cp
    condition1 = c2**4+c3**3*c2**2+c1*c3**4
    condition2 = c2**5+c4*c2**4*c3+c1*c2*c3**4+c0*c3**5
    exceptional = c0+c4*c1
    stage("triple_collision_necessary_polynomials",
          L_degrees=[len(x.p)-1 for x in [condition1, condition2, c3, c2, exceptional]])

    from gf16_exact_domain import K16, F16
    from sympy.polys.rings import ring
    RL, ll = ring("L", K16)
    vv = F16(10)  # t+r in the retained r=2, t=8 instance.
    def binary_eval(p):
        ans = F16(0)
        for i in range(p.bit_length()-1, -1, -1):
            ans = ans*vv+F16((p >> i) & 1)
        return ans
    gv = binary_eval(G)
    def specialize(f):
        da, db, dc = f.d
        den = vv**da*(vv+F16(1))**db*gv**dc
        return sum((ll**i*(binary_eval(co)/den) for i, co in enumerate(f.p)), RL.zero)
    retained = json.loads((agent/"outputs/probe_eleven_finite_quintic.json").read_text())
    env = {"L": ll, **{f"u{i}": F16(i) for i in range(16)}}
    for actual, expected in zip(cp, retained["charpoly_P"]):
        assert specialize(actual) == eval(expected, {"__builtins__": {}}, env)
    stage("entire_retained_F16_characteristic_reproduced")
    result.update({"status": "PASS_UNIVERSAL_QUINTIC_IDENTITIES_ONLY",
        "coefficient_encoding": "Numerators are polynomials in L with F2[v] coefficients encoded as binary hexadecimal; denominator exponents refer to v,v+1,G=v10+v7+v5+v3+1.",
        "substitution": "t=v^2, r=v^2+v",
        "regular_u_Z_squared_identity": True,
        "A": A.serial(), "L0": L0.serial(),
        "quintic_coefficients_ascending": [x.serial() for x in C],
        "u_coefficients_ascending": [x.serial() for x in u],
        "charpoly_P": [x.serial() for x in cp],
        "charpoly_B": [x.serial() for x in cb],
        "triple_conditions": [x.serial() for x in [condition1, condition2, c3, c2, exceptional]],
        "scope": "Universal coefficient identities and the entire retained F16 characteristic polynomial checked. Parameter exceptional loci, special fibres, triple-fibre exclusion and nodality remain unproved."})
except Exception:
    result.update({"status": "EXPLORATORY_FAILURE", "traceback": traceback.format_exc()})
finally:
    signal.alarm(0)
    result["actual_utc"] = datetime.now(timezone.utc).isoformat()
    result["runtime_seconds"] = time.perf_counter()-start
    out = agent/"outputs/post_CP27_eleven_rational_quintic.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ["status", "actual_utc", "runtime_seconds", "stages"]}, indent=2))
