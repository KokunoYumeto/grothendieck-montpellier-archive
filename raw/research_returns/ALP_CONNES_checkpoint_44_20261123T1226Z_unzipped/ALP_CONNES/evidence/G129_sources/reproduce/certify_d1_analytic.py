"""Rigorous-ball numerical component of a proposed p-class certificate.
The algebraic/analytic identities need a separate reviewed proof. No claim that
PARI's provisional class group is certified by merely running this script.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import comb, prod
from time import perf_counter
import json
from flint import arb, acb, arb_mat, ctx
import flint

ctx.prec = 900
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'exact_units' / 'all_units_exact_certificate.json'
units = json.loads(SOURCE.read_text())['units']
assert len(units) == 5
start = perf_counter()

def astr(x):
    return x.str(280, more=True)

def coeffs(limit):
    spf = list(range(limit+1))
    for p in range(2, int(limit**0.5)+1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    a = [0]*(limit+1)
    a[1] = 1
    for n in range(2, limit+1):
        p = spf[n]
        m, k = n, 0
        while m % p == 0:
            m //= p
            k += 1
        if p == 269:
            local = 0
        elif p == 3:
            local = 1
        elif p % 3 == 2:
            local = int(k % 2 == 0)
        else:
            ap = 2 if pow(269, (p-1)//3, p) == 1 else -1
            u, v = 1, ap
            for _ in range(2, k+1):
                u, v = v, ap*v-u
            local = v
        a[n] = a[m]*local
        assert abs(a[n]) <= n
    return a

# Six embeddings, one from each conjugate pair: t -> rho*omega^j,
# zeta5 -> zeta5^b, j=0,1,2 and b=1,2. Coordinates are log|sigma(u)|^2.
rho = arb(269).root(3)
omega = acb(-arb(1)/2, arb(3).sqrt()/2)
zeta = (acb(0, 2*arb.pi()/5)).exp()
rows = []
for j in range(3):
    for b in [1,2]:
        t, z = rho*(omega**j), zeta**b
        row = []
        for unit in units:
            assert unit['monic_integral'] and unit['exact_annihilation']
            value = acb(0)
            for k, c in enumerate(unit['numerators']):
                value += c*(t**(k//4))*(z**(k%4))
            value /= unit['common_denominator']
            norm2 = value.real**2 + value.imag**2
            assert norm2 > 0
            row.append(norm2.log())
        rows.append(row)
for i in range(5):
    assert sum((row[i] for row in rows), arb(0)).contains(0)
regulator = abs(arb_mat(rows[:5]).det())
assert regulator > 20872891 and regulator < 20872892
P = prod(4*comb(12,j)+1 for j in range(1,13))
lower_denominator = (120*(P+1))**5
M = 20872892*lower_denominator
assert arb(M) > regulator*lower_denominator
print(json.dumps({'stage':'regulator','regulator':astr(regulator), 'M_digits':len(str(M)), 'elapsed_seconds':perf_counter()-start}), flush=True)

N5, N0 = 200000, 40000
an = coeffs(N5)

def sum_conductor(Q, N, residues):
    scale = 2*arb.pi()/arb(Q).sqrt()
    A, B, T = [[arb(0) for _ in range(residues)] for __ in range(3)]
    for n in range(1,N+1):
        c = an[n]
        slot = n % residues if residues > 1 else 0
        if c == 0 or (residues == 5 and slot == 0):
            continue
        x = scale*n
        ex = (-x).exp()
        A[slot] += c*ex/n
        B[slot] += c*x.expint(1)
        T[slot] += c*ex
        if n % 10000 == 1:
            print(json.dumps({'stage':'sum','Q':Q,'n':n,'elapsed_seconds':perf_counter()-start}), flush=True)
    # |a_n| <= n. E1(x)<=exp(-x)/x for x>0.
    # For each residue subtotal, bounding by the full positive tail is safe.
    z = (-scale).exp()
    first = (-(N+1)*scale).exp()
    tailA = first/(1-z)
    tailB = tailA/scale
    tailT = first*((N+1)-N*z)/(1-z)**2
    for j in range(residues):
        A[j] += arb(0,tailA.upper())
        B[j] += arb(0,tailB.upper())
        T[j] += arb(0,tailT.upper())
    return scale,A,B,T,{'Q':Q,'N':N,'tail_A_per_residue':astr(tailA),'tail_B_per_residue':astr(tailB),'tail_theta_per_residue':astr(tailT)}

s0,A0,B0,T0,tail0 = sum_conductor(217083,N0,1)
# Real coefficients and nonzero theta force epsilon=1 by the theta FE.
assert not T0[0].contains(0)
L0 = A0[0] + s0*B0[0]
s5,A5,B5,T5,tail5 = sum_conductor(5427075,N5,5)
def quad(v): return v[1]-v[2]-v[3]+v[4]
def quartic(v): return acb(v[1]-v[4],v[2]-v[3])
assert not quad(T5).contains(0)
Lquad = quad(A5) + s5*quad(B5)
theta = quartic(T5)
assert theta.abs_lower() > 0
root_number = theta/theta.conjugate()
Lquartic = quartic(A5) + root_number*s5*quartic(B5).conjugate()
Lquartic_norm2 = Lquartic.real**2 + Lquartic.imag**2
D = (3*269**2)**4 * 5**9
assert D == 4337438179275555809220703125
phi = (1+arb(5).sqrt())/2
dirichlet_product = 4*arb.pi()**2*phi.log()/(25*arb(5).sqrt())
residue = dirichlet_product*L0*Lquad*Lquartic_norm2
hR = residue*10*arb(D).sqrt()/(2*arb.pi())**6
ratio = hR/regulator
error = abs(ratio-189)
threshold = arb(1)/M
success = bool(error < threshold)
result = {
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'NUMERICAL_INTERVAL_COMPONENT_PASS_PENDING_PROOF_REVIEW' if success else 'FAILED_INTEGER_ISOLATION',
 'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'unit_input_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
 'runtime':{'python_flint':flint.__version__,'precision_bits':ctx.prec},
 'regulator':astr(regulator), 'log_embedding_matrix':[[astr(x) for x in row] for row in rows],
 'P':P, 'regulator_lower_bound_reciprocal':lower_denominator,
 'unit_index_upper_bound':M,'integer_target':189,'target_prime':269,
 'tails':[tail0,tail5], 'theta0':astr(T0[0]),'theta_quadratic':astr(quad(T5)),
 'theta_quartic':{'real':astr(theta.real),'imag':astr(theta.imag)},
 'root_number_quartic':{'real':astr(root_number.real),'imag':astr(root_number.imag)},
 'L_standard':astr(L0),'L_quadratic_twist':astr(Lquad),
 'L_quartic_twist':{'real':astr(Lquartic.real),'imag':astr(Lquartic.imag)},
 'discriminant':D,'roots_of_unity':10,'dirichlet_product':astr(dirichlet_product),
 'zeta_residue':astr(residue),'h_times_R':astr(hR),'h_over_unit_index':astr(ratio),
 'absolute_error_from_189':astr(error),'separation_threshold':astr(threshold),
 'strict_integer_isolation':success,
 'elapsed_seconds':perf_counter()-start,
 'scope':'Rigorous interval component conditional on separately verified field/FE/class formula/coarse regulator identities and exact p-saturation. Not by itself a full class-group structure certificate.'
}
(HERE/'d1_analytic_interval.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','L_standard','L_quadratic_twist','L_quartic_twist','root_number_quartic','h_over_unit_index','absolute_error_from_189','separation_threshold','strict_integer_isolation','elapsed_seconds']},indent=2),flush=True)
