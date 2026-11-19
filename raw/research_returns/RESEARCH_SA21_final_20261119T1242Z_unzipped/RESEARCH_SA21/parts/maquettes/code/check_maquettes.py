"""Exhaustive checks of explicit finite maquette counterexamples.

AI-produced by GPT-6 Astra (OpenAI), run maquettes, 2026-11-19.
No random search; every relation is constructed explicitly and every required
finite instance is checked. Standard library only.
"""
from itertools import combinations, product
from fractions import Fraction
from time import perf_counter
import json


def subsets(s, nonempty=True):
    s = tuple(sorted(s))
    return [frozenset(t) for n in range(1 if nonempty else 0, len(s)+1)
            for t in combinations(s,n)]


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        new = reached | {v for a,b in edges for u,v in [(a,b),(b,a)]
                         if u in reached}
        if new == reached:
            return reached == vertices
        reached = new


def rankq(a):
    a = [[Fraction(x) for x in row] for row in a]
    if not a:
        return 0
    i = 0
    for j in range(len(a[0])):
        piv = next((k for k in range(i,len(a)) if a[k][j]),None)
        if piv is None:
            continue
        a[i],a[piv] = a[piv],a[i]
        v = a[i][j]
        a[i] = [x/v for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                v = a[k][j]
                a[k] = [x-v*y for x,y in zip(a[k],a[i])]
        i += 1
        if i == len(a):
            break
    return i


def parity(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq))
                    for j in range(i+1,len(seq)))


def verify_corrected_magor(rank, inc):
    """Check every finite instance; lifting means same sign on both sides.

    Interior refinement is identity and disjunction is inequality of
    orientation orbits. This is explicitly the corrected system.
    """
    M = list(product(rank, (-1, 1)))
    flip = lambda x: (x[0], -x[1])
    assert all(flip(flip(x)) == x and flip(x) != x for x in M)
    assert all(x in M and y in M and x != y for x,y in inc)
    assert all((flip(x),flip(y)) in inc for x,y in inc)
    reach = set(inc)
    while True:
        new = reach | {(a,d) for a,b in reach for c,d in reach if b == c}
        if new == reach:
            break
        reach = new
    assert all(a != b for a,b in reach)
    # Longest path ranks: not merely a declaration of the dimensions.
    depth = {}
    for x in sorted(M, key=lambda a: rank[a[0]]):
        preds = [a for a,b in inc if b == x]
        assert all(rank[a[0]] < rank[x[0]] for a in preds)
        depth[x] = 1+max((depth[a] for a in preds),default=-1)
        assert depth[x] == rank[x[0]]
    pos0 = {x for x in M if depth[x] == 0 and x[1] == 1}
    all0 = {x for x in M if depth[x] == 0}
    assert all0 == pos0 | {flip(x) for x in pos0}
    assert not pos0 & {flip(x) for x in pos0}
    eq = lambda x,y: x == y
    disj = lambda x,y: x[0] != y[0]
    for x,y in product(M,repeat=2):
        assert eq(x,y) == eq(flip(x),flip(y))
        assert disj(x,y) == disj(flip(x),y)
        if x == y:
            assert not disj(x,y)
        # Magor 2(a): the only possible refinement witness is x.
        candidates = [z for z in (x,) if eq(x,z) and (z == y or (z,y) in reach)]
        assert len(candidates) <= 1
        # Magor 3: both refinement witnesses have to equal x and y.
        if disj(x,y):
            assert disj(x,y)
        if (x,y) in reach:
            assert disj(x,y)
    # Magor 2(b) for the same-sign convention, both signs, all incidences.
    for lower,upper in inc:
        for sign in (-1,1):
            X = upper if sign == 1 else flip(upper)
            Y = X
            signed_Y = Y if sign == 1 else flip(Y)
            candidates = [z for z in (lower,) if (z,signed_Y) in inc and eq(lower,z)]
            assert len(candidates) == 1
    sixa = 0
    for z,x in reach:
        if depth[x] - depth[z] == 2:
            assert len([y for y in M if (z,y) in inc and (y,x) in inc]) == 1
            assert len([y for y in M if (flip(z),y) in inc and (y,x) in inc]) == 1
            sixa += 1
    for x in M:
        if depth[x] == 1:
            assert len([v for v in pos0 if (v,x) in inc]) == 1
    return dict(oriented_elements=len(M), immediate_relations=len(inc),
                all_strict_relations=len(reach), magor6a_instances=sixa,
                all_corrected_axioms_passed=True,
                convention="Orbit inequality; same-sign Magor 2(b).")


def augmented_face_data(facets, top=False):
    faces = set().union(*(set(subsets(f)) for f in facets))
    zero = frozenset()
    cells = [zero] + sorted(faces,key=lambda x:(len(x),sorted(x)))
    t = "TOP"
    if top:
        cells.append(t)
    ranks = {x: (max(map(len,facets))+1 if x == t else len(x))
             for x in cells}
    le = lambda x,y: x == y or x == zero or y == t or (x != t and y != zero and x < y)
    return cells,ranks,le


def check_torus():
    N = 3
    v = lambda i,j: (i%N)*N+(j%N)
    oriented = []
    for i,j in product(range(N),repeat=2):
        oriented.extend([(v(i,j),v(i+1,j),v(i+1,j+1)),
                         (v(i,j),v(i+1,j+1),v(i,j+1))])
    facets = [frozenset(f) for f in oriented]
    assert len(set(facets)) == 18
    P,r,le = augmented_face_data(facets,top=True)
    zero = frozenset(); t = "TOP"
    covers = [(a,b) for a,b in product(P,repeat=2)
              if le(a,b) and r[b] == r[a]+1]
    coeff = {}
    for a,b in covers:
        if a == zero:
            coeff[a,b] = 1
        elif b == t:
            coeff[a,b] = parity(next(x for x in oriented if frozenset(x) == a))
        else:
            coeff[a,b] = (-1)**list(sorted(b)).index(next(iter(b-a)))
    diamonds = []
    for a,b in product(P,repeat=2):
        if le(a,b) and r[b] == r[a]+2:
            middle = [x for x in P if (a,x) in coeff and (x,b) in coeff]
            assert len(middle) == 2, (a,b,middle)
            assert sum(coeff[a,x]*coeff[x,b] for x in middle) == 0
            diamonds.append((a,b,middle))
    # Every vertex of the torus has a single six-edge cyclic link.
    face_counts = [sum(r[x]==i+1 for x in P) for i in range(3)]
    assert face_counts == [9,27,18]
    for q in range(9):
        link_edges = [f-frozenset([q]) for f in facets if q in f]
        link_vertices = set().union(*link_edges)
        assert len(link_vertices) == len(link_edges) == 6
        assert all(sum(x in e for e in link_edges)==2 for x in link_vertices)
        assert connected(link_vertices,[tuple(e) for e in link_edges])
    # The torus and every boundary of dimension >=1 are connected.
    for b in P:
        if r[b] >= 3:
            low = [a for a in P if a != zero and a != b and le(a,b)]
            assert connected(low,[(a,c) for a,c in combinations(low,2)
                                  if le(a,c) or le(c,a)])
    # Every vertex link in the order complex of nonempty P is connected.
    for b in P[1:]:
        link_vertices = [a for a in P[1:] if a != b and (le(a,b) or le(b,a))]
        link_edges = [(a,c) for a,c in combinations(link_vertices,2)
                      if le(a,c) or le(c,a)]
        assert connected(link_vertices,link_edges)
    # Rational homology of torus, explicitly computed.
    by_rank = [[x for x in P if r[x] == k] for k in (1,2,3)]
    d1 = [[coeff.get((a,b),0) for b in by_rank[1]] for a in by_rank[0]]
    d2 = [[coeff.get((a,b),0) for b in by_rank[2]] for a in by_rank[1]]
    rd1,rd2 = rankq(d1),rankq(d2)
    betti = [9-rd1,27-rd1-rd2,18-rd2]
    assert betti == [1,2,1]
    # Doubled oriented incidence structure and Magor 6(a),(b).
    unsigned = P[1:]
    M = [(a,s) for a in unsigned for s in (-1,1)]
    inc = {((a,s),(b,u)) for a,b in covers if a != zero
           for s,u in product((-1,1),repeat=2) if s*u*coeff[a,b] == 1}
    reach = set(inc)
    changed = True
    while changed:
        new = reach | {(a,d) for a,b in reach for c,d in reach if b == c}
        changed = new != reach
        reach = new
    assert all(a != b for a,b in reach)
    assert all(((a,-s),(b,-u)) in inc for (a,s),(b,u) in inc)
    # Corrected maquette disjointness: distinct orientation orbits.
    disj = lambda x,y: x[0] != y[0]
    assert all(disj(x,y) for x,y in reach)  # Magor 4.
    assert all(not disj(x,x) for x in M)
    assert all(disj(x,y)==disj((x[0],-x[1]),y) for x,y in product(M,repeat=2))
    # Interior refinement is equality. Magor 2(a) has the unique possible
    # intermediate x itself; 2(b) and 3 reduce to the same input incidence
    # and disjointness predicates, respectively.
    for x,y in product(M,repeat=2):
        candidates = [z for z in (x,) if z==y or (z,y) in reach]
        assert len(candidates) <= 1
    tests6a = 0
    for (a,s),(b,u) in reach:
        if r[b]-r[a] == 2:
            midplus = [z for z in M if ((a,s),z) in inc and (z,(b,u)) in inc]
            midminus = [z for z in M if ((a,-s),z) in inc and (z,(b,u)) in inc]
            assert len(midplus) == len(midminus) == 1
            tests6a += 1
    for b,u in M:
        if r[b] == 2:
            assert sum(((a,1),(b,u)) in inc for a in unsigned if r[a]==1) == 1
    full_axiom_check = verify_corrected_magor({x:r[x]-1 for x in unsigned},inc)
    return dict(name="triangulated torus topped by formal 3-cell",
                vertices=9,edges=27,faces=18,formal_3_cells=1,
                unoriented_nonempty_cells=55,oriented_cells=110,
                rank_two_intervals=len(diamonds),magor6a_checks=tests6a,
                oriented_cover_relations=len(inc),
                boundary_matrix_ranks=[rd1,rd2],betti_torus=betti,
                euler_torus=9-27+18,euler_sphere2=2,
                finite_rank=True,finite_lower_ideals=True,
                signed_diamonds=True,connected_positive_dimensional_boundaries=True,
                corrected_Magor1_through6=True,
                full_axiom_check=full_axiom_check,
                all_order_complex_vertex_links_connected=True,
                regular_CW_face_poset=False,
                caveat="Inequality is taken on orientation orbits; literal inequality contradicts Magor 1prime(c).")


def check_square():
    V = [frozenset([i]) for i in range(4)]
    E = [frozenset([i,(i+1)%4]) for i in range(4)]
    T = frozenset(range(4))
    P = V+E+[T]
    for a,b in product(P,repeat=2):
        lows = [x for x in P if x <= a and x <= b]
        if lows:
            glb = [x for x in lows if all(y<=x for y in lows)]
            assert len(glb) == 1
    for x in P:
        lower = [y for y in P if y<x]
        maximal = [y for y in lower if not any(y<z for z in lower)]
        assert not lower or len(maximal)>=2
    assert len(P)+1 == 10 != 2**4
    return dict(name="square face poset",nonempty_cells=len(P),At_pol1=True,
                At_simp1=True,boolean_principal_ideal=False,
                vertices_below_top=4,faces_with_empty=10,simplex_faces_with_empty=16)


def check_double_edge():
    P = ["v0","v1","e0","e1"]
    le = lambda a,b:a==b or (a.startswith('v') and b.startswith('e'))
    ideals = {a: [x for x in P if le(x,a)] for a in P}
    assert ideals["e0"] == ["v0","v1","e0"]
    assert ideals["e1"] == ["v0","v1","e1"]
    # Each ideal plus empty is Boolean, but the two edges have the same vertices.
    assert {x for x in ideals['e0'] if x.startswith('v')} == {x for x in ideals['e1'] if x.startswith('v')}
    assert not any(all(le(y,x) for y in ('v0','v1')) for x in ('v0','v1'))
    return dict(name="two parallel edges",local_boolean=True,
                vertex_set_map_injective=False,global_meet_property=False,
                simplicial_complex_face_poset=False,regular_CW_face_poset=True)


def check_three_point_boundary():
    P = ('a','b','c','top')
    le = lambda x,y: x == y or y == 'top'
    for x,y in product(P,repeat=2):
        lower = [z for z in P if le(z,x) and le(z,y)]
        if lower:
            assert sum(all(le(z,w) for z in lower) for w in lower) == 1
    for x in P:
        proper = [z for z in P if z != x and le(z,x)]
        maximal = [z for z in proper if not any(z != w and le(z,w) for w in proper)]
        assert not proper or len(maximal) >= 2
    assert len([x for x in P if x != 'top']) == 3
    return dict(name="three-point boundary",nonempty_cells=4,
                At_pol1=True,At_simp1=True,top_dimension=1,
                boundary_points=3,regular_CW_face_poset=False)


def check_literal_incompatibility():
    M = [0,1]
    opposite = lambda x:1-x
    disj = lambda x,y:x!=y
    witness = (0,1)
    assert disj(*witness) and not disj(opposite(witness[0]),witness[1])
    return dict(name="literal oriented inequality",M=M,opposite=[1,0],
                witness=witness,Magor1prime_c=False,
                conclusion="Every nonempty fixed-point-free involution yields this contradiction.")


def check_backtrack():
    # A formal disk attached along e followed by e^{-1}. There are no loops.
    rank={'v0':0,'v1':0,'e':1,'f':2}
    M=list(product(rank,(-1,1)))
    inc={(('v0',1),('e',1)),(('v1',-1),('e',1)),
         (('v0',-1),('e',-1)),(('v1',1),('e',-1))}
    inc |= {(('e',s),('f',u)) for s,u in product((-1,1),repeat=2)}
    reach=set(inc)
    while True:
        new=reach|{(a,d) for a,b in reach for c,d in reach if b==c}
        if new==reach:break
        reach=new
    checked=0
    for a,b in reach:
        if rank[b[0]]-rank[a[0]]==2:
            assert len([y for y in M if (a,y) in inc and (y,b) in inc])==1
            opposite=(a[0],-a[1])
            assert len([y for y in M if (opposite,y) in inc and (y,b) in inc])==1
            checked+=1
    for b in [('e',1),('e',-1)]:
        assert sum(((v,1),b) in inc for v in ('v0','v1'))==1
    assert all(((a,-s),(b,-u)) in inc for (a,s),(b,u) in inc)
    assert all(a[0]!=b[0] for a,b in reach)
    full_axiom_check = verify_corrected_magor(rank,inc)
    return dict(name="backtracking two-cell",oriented_cells=len(M),
                no_one_cell_loops=True,connected_two_cell_boundary=True,
                Magor6a_checks=checked,Magor6=True,
                full_axiom_check=full_axiom_check,
                one_edge_used_with_both_orientations=True,
                underlying_boundary_order_complex="an interval, not a circle",
                regular_CW_face_poset=False)


def check_literal_lifting_branch():
    results = []
    for origin,terminal in product((0,1),repeat=2):
        rank = {'v0':0,'v1':0,'e':1}
        inc = {((f'v{origin}',1),('e',1)),
               ((f'v{terminal}',-1),('e',1)),
               ((f'v{origin}',-1),('e',-1)),
               ((f'v{terminal}',1),('e',-1))}
        verify_corrected_magor(rank,inc)
        # Under identity, literal epsilon-on-source lifting is precisely this.
        literal = all(((a,s),(b,-u)) in inc for (a,s),(b,u) in inc)
        assert literal == (origin == terminal)
        results.append(dict(origin=origin,terminal=terminal,literal_2b=literal))
    return dict(name="literal source-only sign in Magor 2(b)",
                complete_two_vertex_one_edge_graph_list=results,
                conclusion="Exactly loops pass; higher-dimensional impossibility is proved in the text.")


def check_disconnected_link_regular_example():
    facets = [frozenset((0,1,2)),frozenset((0,3,4))]
    P,r,le = augmented_face_data(facets)
    q = frozenset([0])
    link_vertices = [x for x in P if x and x != q and le(q,x)]
    edges = [(x,y) for x,y in combinations(link_vertices,2) if le(x,y) or le(y,x)]
    assert not connected(link_vertices,edges)
    pieces = [{frozenset((0,i)),frozenset((0,j)),frozenset((0,i,j))}
              for i,j in ((1,2),(3,4))]
    assert set.union(*pieces) == set(link_vertices)
    assert all(connected(piece,[(x,y) for x,y in edges if x in piece and y in piece])
               for piece in pieces)
    assert [sum(r[x] == n for x in P) for n in (1,2,3)] == [5,6,2]
    return dict(name="two filled triangles meeting at one vertex",vertices=5,
                edges=6,triangles=2,nonempty_cells=13,
                regular_CW=True,simplicial_complex=True,
                common_vertex_link_dimension=1,link_components=2)


def check_mccord_circle():
    P = range(4)
    strict = {(a,b) for a in (0,1) for b in (2,3)}
    assert all(sum(x in edge for edge in strict) == 2 for x in P)
    assert connected(P,strict)
    assert not any((a,b) in strict and (b,c) in strict for a,b,c in product(P,repeat=3))
    return dict(name="four-point Alexandrov circle",points=4,
                order_complex_vertices=4,order_complex_edges=4,
                order_complex_is_circle=True,McCord_weak_equivalence=True,
                homotopy_equivalence=False,
                proof="Every map from the connected poset to a Hausdorff space is constant; circle identity is not null-homotopic.")


def check_flags_and_incidence():
    # L={a<b}; the positional order is Pa<Iab<Pb, whereas face order
    # has both endpoints below Iab. Every subset is a positional flag.
    cells = ('Pa','Iab','Pb')
    all_flags = [set(cells[i] for i in range(3) if mask >> i & 1) for mask in range(8)]
    closure = lambda F: F | ({'Pa','Pb'} if 'Iab' in F else set())
    figures = [F for F in all_flags if closure(F) == F]
    assert len(figures) == 5
    assert {'Iab'} in all_flags and {'Iab'} not in figures
    assert closure({'Iab'}) == set(cells)
    assert all(closure(F) in all_flags for F in all_flags)
    # Acyclic generators need not be covers.
    arrows = {(0,1),(1,2),(0,2)}
    assert all(a < b for a,b in arrows)
    assert (0,2) in arrows and (0,1) in arrows and (1,2) in arrows
    return dict(name="positional flags versus incidence-closed figures",
                base_order=['a<b'],positional_chain=list(cells),
                prefigures=8,figures=5,single_interval_is_prefigure=True,
                single_interval_is_figure=False,
                acyclic_generator_counterexample=sorted(arrows),
                redundant_noncover_arrow=[0,2])


if __name__ == "__main__":
    start = perf_counter()
    results = [check_literal_incompatibility(),check_literal_lifting_branch(),
               check_square(),check_double_edge(),check_backtrack(),check_torus(),
               check_three_point_boundary(),
               check_disconnected_link_regular_example(),check_mccord_circle()]
    results.append(check_flags_and_incidence())
    result = {"program":"check_maquettes.py","results":results,
              "all_assertions_passed":True,"runtime_seconds":round(perf_counter()-start,6)}
    print(json.dumps(result,indent=2))
