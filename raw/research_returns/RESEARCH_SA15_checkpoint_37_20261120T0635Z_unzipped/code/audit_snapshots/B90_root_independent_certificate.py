"""Exact finite consequences of the B90 actual-field proof; no existence test.

Every executed version and output is retained.  The final nonintegral average
is the contradiction to a hypothetical actual torsion comparison, not a
ramification profile asserted to occur.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from datetime import datetime, timezone
import json, time

start = time.perf_counter()
p = 5
rows = {
    1: [(95, 3125, 59375, 'diag'), (15, 9375, 28125, 'off')],
    2: [(5, 3125, 59375, 'off'), (45, 9375, 28125, 'diag')],
}

def possible_first_prime(A, actual):
    """Necessary fixed-coefficient constraints at two specified lower breaks."""
    forced = []
    for b, D in actual:
        leading = A + p*b
        if leading < D:
            forced.append(A + (p-1)*b)
        elif leading > D:
            forced.append(D-b)
    if forced and any(J != forced[0] for J in forced):
        return None
    J = forced[0] if forced else None
    if J is not None and (J <= A or J % p == 0):
        return None
    for b, D in actual:
        lead = A+p*b
        other = J+b if J is not None else float('inf')
        lower = min(lead, other)
        if lower > D or (lower < D and lead != other):
            return None
    return J if J is not None else 'infinity_allowed'

case_records = []
survivors = []
for i, last, large, residue in (
    (1, 'off', 606, 0), (1, 'diag', 1872, 6),
    (2, 'diag', 624, 18), (2, 'off', 1866, 0),
):
    for t in range(1, large):
        if t % 24 != residue:
            continue
        u = p*large-(p-1)*t
        assert u > t
        tests = []
        for A, D0, D1, high in rows[i]:
            at_t = D0 if high == last else D1
            at_u = D1 if high == last else D0
            tests.append(possible_first_prime(A, [(t, at_t), (u, at_u)]))
        rec = {'field':i, 'last_line':last, 't':t, 'u':u,
               'larger_cyclic_break':large, 'first_prime_tests':tests,
               'survives': all(v is not None for v in tests)}
        case_records.append(rec)
        if rec['survives']:
            survivors.append(rec)
assert [(r['field'],r['last_line'],r['t'],r['u']) for r in survivors] == [
    (1,'diag',606,6936),(2,'off',624,6834)]
assert [r['first_prime_tests'] for r in survivors] == [[27839,2439],[27341,2541]]

def lower_to_upper(breaks):
    prev = Q(0)
    upper = Q(0)
    answer = []
    for j,b in enumerate(breaks):
        upper += Q(b-prev, p**j)
        answer.append(upper)
        prev = b
    return answer

def upper_to_lower(breaks):
    prev = Q(0)
    lower = Q(0)
    answer = []
    for j,b in enumerate(breaks):
        lower += (b-prev)*p**j
        assert lower.denominator == 1
        answer.append(int(lower))
        prev = b
    return answer

old_subgroup_lower = {1:[96,1146], 2:[6,1896]}
old_subgroup_upper = {i:lower_to_upper(v) for i,v in old_subgroup_lower.items()}
assert old_subgroup_upper == {1:[Q(96),Q(306)],2:[Q(6),Q(384)]}
new_point_upper = {1:lower_to_upper([606,6936]),2:lower_to_upper([624,6834])}
assert new_point_upper == {1:[Q(606),Q(1872)],2:[Q(624),Q(1866)]}
composite_upper = {i:sorted(old_subgroup_upper[i]+new_point_upper[i]) for i in (1,2)}
composite_lower = {i:upper_to_lower(v) for i,v in composite_upper.items()}
assert composite_lower == {1:[96,1146,8646,166896],2:[6,1896,7896,163146]}
terminal_column_lower = {i:composite_lower[i][2:] for i in (1,2)}
terminal_column_upper = {i:lower_to_upper(v) for i,v in terminal_column_lower.items()}
assert terminal_column_upper == {1:[Q(8646),Q(40296)],2:[Q(7896),Q(38946)]}
terminal_upper = sorted(terminal_column_upper[1]+terminal_column_upper[2])
terminal_lower = upper_to_lower(terminal_upper)
assert terminal_upper == [Q(7896),Q(8646),Q(38946),Q(40296)]
assert terminal_lower == [7896,11646,769146,937896]

def break_of(A,B):
    a,b,c,d = A
    if c: return 6
    if d: return 96
    if b: return 1146
    if a: return 1896
    a,b,c,d = B
    if d: return 7896
    if c: return 11646
    if b: return 769146
    if a: return 937896
    raise AssertionError('Identity has no finite lower break')

fiber_records = []
for r in range(1,p):
    distribution = Counter()
    for A in product(range(p), repeat=4):
        a,b,c,d = A
        if (a+d) % p:
            continue
        carry = (a+d)//p
        detA = a*d-b*c
        for B in product(range(p), repeat=4):
            aa,bb,cc,dd = B
            if (carry+aa+dd+detA-r) % p:
                continue
            # Independently use the actual determinant over Z/125.
            X00,X01,X10,X11 = [A[j]+p*B[j] for j in range(4)]
            actual_det = ((1+p*X00)*(1+p*X11)-p*p*X01*X10) % 125
            assert actual_det == 1+25*r
            distribution[break_of(A,B)] += 1
    expected = {6:12500,96:2500,1146:500,7896:100,11646:20,769146:4,937896:1}
    assert dict(distribution) == expected
    assert sum(distribution.values()) == p**6
    numerator = sum(b*n for b,n in distribution.items())
    average = Q(numerator,p**6)
    assert numerator == 5925000 and average == Q(1896,5)
    assert average.denominator == 5
    fiber_records.append({'target_determinant':1+25*r,
                          'fiber_size':sum(distribution.values()),
                          'break_multiplicities':dict(sorted(distribution.items())),
                          'break_sum':numerator,'average':str(average),
                          'integer':False})

# Group identities behind the actual intersections/composita, checked on
# every first-layer matrix in the relevant two-dimensional stabilizer.
group_checks = 0
for i in (0,1):
    mats = [A for A in product(range(p), repeat=4)
            if A[i] == 0 and A[i+2] == 0]
    assert len(mats) == p**2
    for A in mats:
        for C in mats:
            def mul(X,Y):
                a,b,c,d=X; e,f,g,h=Y
                return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
            AC,CA=mul(A,C),mul(C,A)
            bracket=tuple((AC[j]-CA[j])%p for j in range(4))
            assert bracket[i] == bracket[i+2] == 0
            group_checks += 1

record = {'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
          'runtime_seconds':time.perf_counter()-start,
          'scope':'Exact necessary finite arithmetic under the hypothetical actual B90 comparison; the noninteger quotient average is its contradiction, not a realized field profile.',
          'counts':{'bounded_lower_break_cases':len(case_records),'surviving_cases':len(survivors),
                    'actual_determinant_fibers':len(fiber_records),'determinant_elements':4*p**6,
                    'stabilizer_commutators':group_checks},
          'surviving_point_fields':survivors,
          'all_bounded_lower_break_cases':case_records,
          'old_subgroup_lower':old_subgroup_lower,
          'old_subgroup_upper':old_subgroup_upper,
          'new_point_upper':new_point_upper,
          'composite_upper':composite_upper,'composite_lower':composite_lower,
          'terminal_column_lower':terminal_column_lower,'terminal_column_upper':terminal_column_upper,
          'terminal_upper':terminal_upper,'terminal_lower':terminal_lower,
          'determinant_fibers':fiber_records}
out = Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps({k:record[k] for k in ('status','actual_utc','runtime_seconds','counts')},indent=2))
