"""RESEARCH_SA20 A.401: independent check that the families M_n (empty relation and finite conjunctions of
x_i = x_j, Q(x_i), T(x_i,x_j) on R = {a,b,c}, Q = {b,c}, T = {(a,b),(a,c)}) are closed under injective
coordinate projections for n <= 4, while the image of T under the first projection, {a}, is not in M_1.
Claude Opus 5.5 at effort max, acf08879a01b97ed4, 22 Nov 2026."""
import itertools
R = "abc"; Q = {"b", "c"}; T = {("a", "b"), ("a", "c")}
def family(n):
    full = frozenset(itertools.product(R, repeat=n))
    atoms = []
    for i in range(n):
        atoms.append(frozenset(t for t in full if t[i] in Q))
        for j in range(n):
            atoms.append(frozenset(t for t in full if (t[i], t[j]) in T))
            if i < j: atoms.append(frozenset(t for t in full if t[i] == t[j]))
    fam = {full, frozenset()}; frontier = [full]
    while frontier:
        new = []
        for S in frontier:
            for A in atoms:
                X = S & A
                if X not in fam: fam.add(X); new.append(X)
        frontier = new
    return fam
fams = {n: family(n) for n in range(0, 5)}
print("family sizes:", {n: len(f) for n, f in fams.items()})
print("M_1 =", sorted(sorted(S) for S in fams[1]))
bad = 0; checked = 0
for n in range(1, 5):
    for S in fams[n]:
        for k in range(0, n):
            for keep in itertools.combinations(range(n), k):
                img = {}
                for t in S: img.setdefault(tuple(t[i] for i in keep), []).append(t)
                if all(len(v) == 1 for v in img.values()):
                    checked += 1
                    if frozenset(img) not in fams[k]: bad += 1
print("injective projections checked:", checked, "images outside the family:", bad)
proj = frozenset((x,) for (x, y) in T)
print("first projection of T:", sorted(proj), "in M_1:", proj in fams[1])
