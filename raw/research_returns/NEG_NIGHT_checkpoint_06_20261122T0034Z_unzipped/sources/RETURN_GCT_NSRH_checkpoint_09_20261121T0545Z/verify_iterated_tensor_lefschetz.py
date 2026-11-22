"""Exact F66 whole-tensor trace/graded-gap certificate; no numerical tests."""
import sympy as s

v = s.symbols("v", nonzero=True)
D = (v + 1 / v) ** 2
d = D ** 2
A = D ** 2 - 8 * D + 8
trace = s.expand(d ** 2 + A ** 2)
expected = {
    -8: 2, -6: 0, -4: 40, -2: 64, 0: 108,
    2: 64, 4: 40, 6: 0, 8: 2,
}
assert s.expand(trace - sum(c * v ** e for e, c in expected.items())) == 0
for e, c in expected.items():
    assert trace.coeff(v, e) == c
    assert c >= 0
    assert expected[-e] == c
assert trace.coeff(v, -8) == 2
assert trace.coeff(v, -6) == 0
assert trace.subs(v, 1) == 320
print("PASS: exact trace expansion, all coefficients, Lefschetz gap and total dimension")
print("T(v) =", trace)
print("degrees -8 and -6:", trace.coeff(v, -8), trace.coeff(v, -6))
