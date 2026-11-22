"""Exact finite check of P-F40k, independently enumerating its representations."""
from itertools import combinations_with_replacement
from collections import Counter

P, n = 85, 8
weights = [(-2)**i % P for i in range(n)]
expected = [(1,1,0,4,4),(3,3,2,4,4),(6,3,2,4,4),
            (7,1,0,3,4),(9,2,1,4,3),(15,2,1,4,4),(18,2,1,4,5)]
cubic = Counter((-(weights[i]+weights[j]+weights[k])) % P
                for i,j,k in combinations_with_replacement(range(n),3))
adjoint = Counter((weights[i]-weights[j]) % P
                  for i in range(n) for j in range(n) if i != j)
seen = set()
for b, mc, ma, h1, h3 in expected:
    orbit = {b*pow(-2,j,P) % P for j in range(n)}
    assert len(orbit) == 8 and not seen.intersection(orbit)
    seen.update(orbit)
    assert {cubic[x] for x in orbit} == {mc}
    assert {adjoint[x] for x in orbit} == {ma}
    assert sum(orbit) == P*h1
    assert sum((3*x) % P for x in orbit) == P*h3
assert set(cubic)-{0} == seen
assert set(adjoint) <= seen
for a, age in [(1,27),(3,28)]:
    numerator = sum(c*((a*x)%P) for x,c in cubic.items())
    numerator -= sum(c*((a*x)%P) for x,c in adjoint.items())
    assert numerator == P*age
print('P-F40k PASS: all table rows; ages 27,28; C1 negative and C3 positive.')
