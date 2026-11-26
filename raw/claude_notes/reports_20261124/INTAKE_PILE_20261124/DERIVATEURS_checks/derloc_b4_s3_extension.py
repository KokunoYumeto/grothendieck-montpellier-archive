# Check (Claude Opus 5.5 at effort high, 24 Nov 2026) of DER_LOCALIZERS B.4's group-theoretic step: for the free-group
# endomorphism phi: a -> a, b -> b[a,b] (an H_1-isomorphism), the assignment a -> (23), b -> (12) into S_3 does not
# factor through phi, i.e. no psi with psi(a) = (23), psi(b[a,b]) = (12). Both commutator conventions tested.
import itertools
def comp(p, q): return tuple(p[q[i]] for i in range(3))      # p after q
def inv(p): r = [0]*3; [r.__setitem__(p[i], i) for i in range(3)]; return tuple(r)
S3 = list(itertools.permutations(range(3)))
t23 = (0, 2, 1); t12 = (1, 0, 2)
def w(*xs):
    r = (0, 1, 2)
    for x in xs: r = comp(r, x)
    return r
for name, br in (('[a,b]=aba^-1b^-1', lambda a, b: w(a, b, inv(a), inv(b))), ('[a,b]=a^-1b^-1ab', lambda a, b: w(inv(a), inv(b), a, b))):
    sols = [y for y in S3 if comp(y, br(t23, y)) == t12]
    print(name, 'solutions psi(b):', sols)
# also: image of phi on homology is the identity matrix (a -> a, b -> b + 0)
