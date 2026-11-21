"""The six non-unimodal constants of P-F-E3-01 as a hexagon of labels (main session, Claude Opus 5.5 at effort max,
21 Nov 2026 ~19:0x UTC). Uses only the facts of E4_RANK_FOUR_20261121.md section 6 (agent a8d75352): each element of
the chi^2 cell is written (first letter, last letter) of its word; gamma_x gamma_y lands in (first(x), last(y)); the
alternating products have last(x) != first(y); the six failures are the 8 alternating products minus the two
shortest, (g1, g2; g12) and (g2, g1; g21); the table's symmetries act on the cell by the Dynkin swap sigma and the
anti-involution t (x -> x^t, product order reversed).
Checks: (1) label (first(x), last(x), last(y)) is a bijection from the 8 alternating products to {1,2}^3; (2) the two
excluded products are an antipodal pair; (3) the six remaining labels with cube edges form one 6-cycle; (4) the
symmetry group of the cube fixing that antipodal pair has order 12 and acts on the six as the dihedral group of the
hexagon; (5) sigma and t act on labels as -1 and (x,y,z) -> (z,-y,x), generating a Klein group whose orbits on the six
are exactly section 6's orbits 4 + 2; (6) the order-3 rotation about the diagonal is sigma composed with the cyclic
slot rotation (x, y, z^v) -> (y, z^v, x), on labels, with the J-ring dual z^v = z^t."""
import itertools
import sys

sys.stdout.reconfigure(encoding="utf-8")
CELL = {"1": ("1", "1"), "2": ("2", "2"), "12": ("1", "2"), "21": ("2", "1")}  # word -> (first, last)
BY_FL = {v: k for k, v in CELL.items()}
bar = {"1": "2", "2": "1"}

alt = [(x, y) for x in CELL for y in CELL if CELL[x][1] != CELL[y][0]]
assert len(alt) == 8
lab = {(x, y): (CELL[x][0], CELL[x][1], CELL[y][1]) for (x, y) in alt}
assert sorted(lab.values()) == sorted(itertools.product("12", repeat=3))  # (1)
excluded = [("1", "2"), ("2", "1")]
ex = [lab[e] for e in excluded]
sgn = lambda t: tuple(1 if c == "1" else -1 for c in t)
assert tuple(-c for c in sgn(ex[0])) == sgn(ex[1])  # (2) antipodal
six = [p for p in alt if p not in excluded]
V = [sgn(lab[p]) for p in six]
adj = {v: [w for w in V if sum(a != b for a, b in zip(v, w)) == 1] for v in V}
assert all(len(adj[v]) == 2 for v in V)  # (3) every vertex has degree 2 ...
seen, cur, prev = [V[0]], V[0], None
while True:  # ... and the graph is one cycle
    nxt = [w for w in adj[cur] if w != prev][0]
    if nxt == V[0]:
        break
    seen.append(nxt); prev, cur = cur, nxt
assert len(seen) == 6
# (4) signed permutation matrices = cube symmetries; stabilizer of the excluded pair
d = sgn(ex[0])
def act(g, v):
    perm, signs = g
    return tuple(signs[i] * v[perm[i]] for i in range(3))
cube = [(p, s) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
stab = [g for g in cube if act(g, d) in (d, tuple(-c for c in d))]
assert len(cube) == 48 and len(stab) == 12
assert all(sorted(act(g, v) for v in V) == sorted(V) for g in stab)
# (5) sigma: complement every letter; t: (x, y; z) -> (y^t, x^t; z^t)
def t_label(x, y):
    xt, yt = BY_FL[CELL[y][::-1]], BY_FL[CELL[x][::-1]]
    return (xt, yt)
def sig_label(x, y):
    return (BY_FL[tuple(bar[c] for c in CELL[x])], BY_FL[tuple(bar[c] for c in CELL[y])])
for p in six:
    assert sig_label(*p) in six and t_label(*p) in six
    assert sgn(lab[sig_label(*p)]) == tuple(-c for c in sgn(lab[p]))
    a, b, c = sgn(lab[p])
    assert sgn(lab[t_label(*p)]) == (c, -b, a)
orbits, left = [], set(six)
while left:
    p = left.pop(); orb = {p, sig_label(*p), t_label(*p), sig_label(*t_label(*p))}
    left -= orb; orbits.append(sorted(orb))
print("orbits of <sigma, t> on the six:", [len(o) for o in orbits])
for o in orbits:
    print("  ", ["(g%s, g%s; g%s)" % (x, y, BY_FL[(CELL[x][0], CELL[y][1])]) for x, y in o])
# (6) cyclic slot rotation (x, y, z^v) -> (y, z^v, x) with z^v = z^t, read back as a structure-constant label
def slot_rot(a, b, c):  # labels in signs: x = (a, b), y = (-b, c), z = (a, c), z^v = (c, a)
    # new x' = y = (-b, c); new y' = z^v = (c, a): new label (first(x'), last(x'), last(y')) = (-b, c, a)
    return (-b, c, a)
rot = lambda v: tuple(-c for c in slot_rot(*v))  # sigma o slot rotation
assert rot(d) == d and rot(rot(rot(V[0]))) == V[0] and rot(V[0]) != V[0]
assert sorted(rot(v) for v in V) == sorted(V)
print("sigma o (cyclic slot rotation) fixes the excluded pair, has order 3 and permutes the six cyclically:",
      [V.index(rot(v)) for v in V])
print("table symmetry group on labels: Klein four (order 4) = index 3 in the hexagon's dihedral group (order 12)")
