"""Small exact computation supporting F-SM-05. No external packages."""

def add(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)


def mul(x, y):
    # F_9 = F_3[i] / (i^2 + 1).
    return ((x[0] * y[0] - x[1] * y[1]) % 3,
            (x[0] * y[1] + x[1] * y[0]) % 3)


def power(x, exponent):
    result = (1, 0)
    for _ in range(exponent):
        result = mul(result, x)
    return result


elements = [(a, b) for a in range(3) for b in range(3)]
counts = {
    x: sum(add(power(y, 3), y) == power(x, 4) for y in elements)
    for x in elements
}
assert set(counts.values()) == {3}
assert sum(counts.values()) == 27
print("Field: F_3[i]/(i^2+1)")
print("Equation: y^3+y=x^4")
print("Affine solutions per x:", counts)
print("Affine points:", sum(counts.values()))
print("Projective points (one point at infinity):", sum(counts.values()) + 1)
