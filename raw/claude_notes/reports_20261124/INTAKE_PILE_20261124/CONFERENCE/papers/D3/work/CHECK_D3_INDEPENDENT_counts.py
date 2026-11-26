# Independent recount of the sizes stated in the note D3 (25 Nov 2026, afceadd46f7598ec4,
# Claude Fable 5.2 at effort max). Standard library only. Run: python -I -B d3_counts.py
import itertools


def suspension_faces(m, poles=("a", "b")):
    """Non-empty simplices of the suspension of the polygon C_m (vertices 0..m-1, edges {i,i+1})."""
    faces = set()
    verts = list(range(m))
    for i in verts:
        faces.add(frozenset([i]))
        faces.add(frozenset([i, (i + 1) % m]))
    for p in poles:
        faces.add(frozenset([p]))
        for i in verts:
            faces.add(frozenset([p, i]))
            faces.add(frozenset([p, i, (i + 1) % m]))
    return faces


def image(face, vmap):
    return frozenset(vmap(x) for x in face)


def leq_pairs(faces):
    return sum(1 for s in faces for t in faces if s <= t)


# Section 4.3: L_8 -> L_4, i -> i mod 4
L8, L4 = suspension_faces(8), suspension_faces(4)
h = lambda x: x if isinstance(x, str) else x % 4
assert all(image(s, h) in L4 for s in L8)
assert all(len(image(s, h)) == len(s) for s in L8)  # injective on each simplex
print("faces of L_8, L_4:", len(L8), len(L4))
print("double collage of Q <-f- P -> e:", len(L8) + len(L4) + 1,
      "; of Q <-id- Q -> e:", len(L4) + len(L4) + 1)

# Section 4.2: crowns with two cone points
print("C_8 and C_4 with t+, t-:", 8 + 2, 4 + 2)

# Section 4.4: S_6 -> S_3, the maps u (0,0,1,1,2,2) and v (0,1,2,0,1,2)
S6, S3 = suspension_faces(6, ("N", "S")), suspension_faces(3, ("N", "S"))
ulist, vlist = [0, 0, 1, 1, 2, 2], [0, 1, 2, 0, 1, 2]
u = lambda x: x if isinstance(x, str) else ulist[x]
v = lambda x: x if isinstance(x, str) else vlist[x]
assert all(image(s, u) in S3 for s in S6) and all(image(s, v) in S3 for s in S6)
print("faces of S_6, S_3:", len(S6), len(S3), "; objects of P:", len(S6) + len(S3))
arrows_L = leq_pairs(S6)
arrows_K = leq_pairs(S3)
arrows_u = sum(1 for a in S6 for b in S3 if image(a, u) <= b)
arrows_v = sum(1 for a in S6 for b in S3 if image(a, v) <= b)
print("arrows of L, of K, label 0, label 1:", arrows_L, arrows_K, arrows_u, arrows_v,
      "; total:", arrows_L + arrows_K + arrows_u + arrows_v)


# degrees on H_2: push the fundamental cycle forward (oriented triangles [p, i, i+1])
def degree(m_src, m_tgt, vmap, poles):
    # count, with sign, the triangles [poles[0], i, i+1] of the source mapping onto [poles[0], 0, 1]
    total = 0
    for i in range(m_src):
        a, b = vmap(i), vmap((i + 1) % m_src)
        if a == b:
            continue
        if (a, b) == (0, 1):
            total += 1
        elif (a, b) == (1, 0):
            total -= 1
    return total


print("degree of h (L_8 -> L_4):", degree(8, 4, h, ("a", "b")))
print("degrees of u, v (S_6 -> S_3):", degree(6, 3, u, ("N", "S")), degree(6, 3, v, ("N", "S")))

# Section 4.1: the six-element ordered set of the Loc (6'a) failure for W_pi
rel = {(0, 1), (0, 3), (2, 1), (2, 3), (0, "m"), ("q", "m")}
elems = [0, 1, 2, 3, "q", "m"]
le = lambda x, y: x == y or (x, y) in rel
X1, X2 = {0, 1, 2, 3, "q"}, {0, "q", "m"}
is_sieve = lambda U: all(x in U for y in U for x in elems if le(x, y))
print("X_1, X_2 sieves:", is_sieve(X1), is_sieve(X2), "; cover:", X1 | X2 == set(elems),
      "; X_0:", sorted(map(str, X1 & X2)))


def components(U):
    U = set(U)
    comps = []
    while U:
        stack = [U.pop()]
        comp = set(stack)
        while stack:
            x = stack.pop()
            for y in list(U):
                if le(x, y) or le(y, x):
                    U.discard(y)
                    comp.add(y)
                    stack.append(y)
        comps.append(comp)
    return comps


print("components of X_0, X_1, X_2, X:", len(components(X1 & X2)), len(components(X1)),
      len(components(X2)), len(components(elems)))
# Euler characteristic of the order complex of X (chains): vertices - edges (no chains of length 3)
chains1 = [(x, y) for x in elems for y in elems if x != y and le(x, y)]
chains2 = [(x, y, z) for (x, y) in chains1 for z in elems if z != y and le(y, z)]
print("X: vertices, edges, 2-chains:", len(elems), len(chains1), len(chains2),
      "; Euler characteristic:", len(elems) - len(chains1) + len(chains2))
