# LM8_PUSH C.46 witness word [[x^2,y^2],[y^2,z^2]] in SL2(Z/12); E.58 normalization q([x,y]) = [[1,8],[8,5]]
import itertools
N = 12
def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
def inv(A):
    (a, b), (c, d) = A
    return ((d % N, -b % N), (-c % N, a % N))
def comm(A, B):
    return mul(mul(A, B), mul(inv(A), inv(B)))
def pw(A, k):
    R = ((1, 0), (0, 1))
    for _ in range(k): R = mul(R, A)
    return R
for sx, sy in itertools.product((2, -2), repeat=2):
    x = ((1, sx % N), (0, 1)); y = ((1, 0), (sy % N, 1))
    z = inv(mul(x, y))
    c = comm(x, y)
    w = comm(comm(pw(x, 2), pw(y, 2)), comm(pw(y, 2), pw(z, 2)))
    print('x upper', sx, 'y lower', sy, '[x,y]=', c, '[x,y]^2=', mul(c, c), ' word=', w)
