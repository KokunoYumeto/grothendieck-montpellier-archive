"""Exact certificates for the cyclic-cover coherent Lefschetz counterexample.

The geometry is proved in sections/A_coherent_counterexample.tex. This program
checks the finite Lauritzen--Rao cokernel functional and the cyclic-algebra
multiplication, not a random sample of smooth branch divisors.
"""
from pathlib import Path
import itertools, json, math, time

started = time.perf_counter()
ROOT = Path(__file__).resolve().parents[1]

def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for rest in compositions(total - i, length - 1):
                yield (i,) + rest

def phi(alpha, beta, p):
    """Apolar pairing with (z0*y1-z1*y0)^(p-2), then the truncated-y trace."""
    m = p - 2
    if sum(alpha) != m or sum(beta) != 3*p - 2:
        return 0
    if any(b >= p or b < 0 for b in beta):
        return 0
    if alpha[2:] != (0, 0):
        return 0
    j = alpha[1]
    if alpha != (m-j, j, 0, 0):
        return 0
    if beta != (p-1-j, j+1, p-1, p-1):
        return 0
    return math.factorial(m) * ((-1)**j) % p

records = []
for p in (2, 3, 5, 7, 11, 13):
    m = p-2
    witness_a = (m, 0, 0, 0)
    witness_b = (p-1, 1, p-1, p-1)
    witness_value = phi(witness_a, witness_b, p)
    assert witness_value != 0
    checked = 0
    if m:
        # Any term with beta_i >= p vanishes in the truncated algebra.
        # Enumerate the surviving beta using complementary low-degree monomials.
        bs = [tuple(p-1-c for c in cs)
              for cs in compositions(p-1, 4)
              if max(cs) < p]
        for a in compositions(m-1, 4):
            for b in bs:
                total = 0
                for i in range(4):
                    aa, bb = list(a), list(b)
                    aa[i] += 1
                    bb[i] += 1
                    total += phi(tuple(aa), tuple(bb), p)
                assert total % p == 0, (p, a, b, total)
                checked += 1
    records.append(dict(p=p, witness_x_exponents=witness_a,
                        witness_y_exponents=witness_b,
                        witness_functional_value=witness_value,
                        incidence_relations_checked=checked,
                        all_relations_annihilated=True))

# In characteristic two the cokernel is exactly one-dimensional.
quadrics = list(compositions(2,4))
quartics = list(compositions(4,4))
column_exponents = []
for i in range(4):
    for a in quadrics:
        v = list(a); v[i] += 2
        column_exponents.append(tuple(v))
missing = sorted(set(quartics)-set(column_exponents))
assert len(column_exponents) == 40
assert len(quartics) == 35
assert len(set(column_exponents)) == 34
assert missing == [(1,1,1,1)]

# Multiplication by the tautological root has a unit in row1,column0.
# Its qth power is b*Id in Z[b], checked with exact polynomial dictionaries.
def padd(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def pmul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,0)+x*y
    return out
def mmul(a,b):
    n=len(a); out=[[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):out[i][j]=padd(out[i][j],pmul(a[i][k],b[k][j]))
    return out
cyclic=[]
for q in (2,3,5):
    mat=[[{} for _ in range(q)] for _ in range(q)]
    for j in range(q-1):mat[j+1][j]={0:1}
    mat[0][q-1]={1:1}
    power=[[{0:1} if i==j else {} for j in range(q)] for i in range(q)]
    for _ in range(q):power=mmul(power,mat)
    assert power==[[{1:1} if i==j else {} for j in range(q)] for i in range(q)]
    assert mat[1][0]=={0:1}
    cyclic.append(dict(q=q, qth_power_equals_b_identity=True,
                       source_character_zero_to_target_character_one=1))

answer=dict(
    status="PASS",
    scope="Exact cokernel functional and cyclic multiplication; smoothness is the geometric Jacobian/Bertini proof, not a numerical experiment.",
    general_prime_functional=records,
    characteristic_two_cokernel=dict(source_dimension=40,target_dimension=35,
                                    rank=34,cokernel_dimension=1,
                                    surviving_monomial_exponents=missing[0]),
    cyclic_multiplication=cyclic,
    sixfold_ambient_section_count=4*math.comb(8,3)*4,
    elapsed_seconds=time.perf_counter()-started)
destination=ROOT/"outputs/coherent_restriction_counterexample.json"
destination.write_text(json.dumps(answer,indent=2)+"\n")
print(json.dumps(answer,indent=2))
