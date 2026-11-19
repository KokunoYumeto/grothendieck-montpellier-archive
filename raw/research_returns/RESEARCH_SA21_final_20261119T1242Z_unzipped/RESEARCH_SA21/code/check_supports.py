"""Finite certificates for Part A and the correspondence dictionary.

Run from any directory with Python 3.10+. No third-party dependencies.
We enumerate all subsets, all closed-set pairs, and (where relevant)
all triples. The output gives the complete finite structures, witnesses,
and exact scope of the checks; no finite run is used to prove an
infinite theorem. AI-produced by GPT-6 Astra (OpenAI), 2026-11-19.
"""
import json
import sys
from itertools import combinations, product
from pathlib import Path
from time import perf_counter

from supports_core import (Orthoset, bits, comparability, figures, incidence,
                           immediate, magasin, natural_posets, supp1_witness)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'parts' / 'axioms'))
from core_models import Magasin


def check_ortholattice(g):
    closed = g.closed()
    assert set(closed) == {a for a in range(1 << g.n) if g.close(a) == a}
    pairs = 0
    for a, b in product(closed, repeat=2):
        meet = a & b
        join = g.join(a, b)
        assert meet in closed and join in closed
        assert all(c & ~meet == 0 for c in closed if c & ~a == c & ~b == 0)
        assert all(join & ~c == 0 for c in closed if a & ~c == b & ~c == 0)
        assert g.polar(g.polar(a)) == a
        assert a & g.polar(a) == 0 and g.join(a, g.polar(a)) == g.full
        assert g.polar(join) == g.polar(a) & g.polar(b)
        pairs += 1
    assert (g.om_witness() is None) == (g.om_equation_witness() is None)
    assert (g.om_witness() is None) == (g.dacey_witness() is None)
    point_boolean = all(any((g.adj[x] | g.adj[y]) & ~g.adj[z] == 0
                            for z in range(g.n))
                        for x, y in product(range(g.n), repeat=2)
                        if not (g.adj[x] >> y & 1))
    assert point_boolean == (g.boolean_witness() is None)
    return dict(subsets=1 << g.n, closed=len(closed), closed_pairs=pairs,
                orthomodular=g.om_witness() is None, Boolean=point_boolean)


def check_identity_magasin(g):
    edges = [(i, j) for i, j in combinations(range(g.n), 2) if g.adj[i] >> j & 1]
    m = Magasin(g.names, [], [], edges)
    m.magaxioms(strong=True)
    m.core()
    assert m.lieux == list(range(g.n))
    assert m.intern == {(i, i) for i in range(g.n)}
    for i, j in product(range(g.n), repeat=2):
        ui = [p for p in m.lieux if (p, i) in m.intern]
        uj = [p for p in m.lieux if (p, j) in m.intern]
        assert ui and uj
        assert ((i, j) in m.orth) == all((p, q) in m.orth for p in ui for q in uj)
    assert all(m.flags().values())
    fs = [sum(1 << x for x in f) for f in m.F]
    # Old absorption: X°=cl{x}, because incidence boundaries are empty.
    absorption = all(g.close(1 << x) == 1 << x for x in range(g.n))
    return m, fs, dict(strong_Mag1_4=True, divisibility=True, MagL2=True,
                       old_L1_L2_L3_CLspac_At_supp=True,
                       old_absorption=absorption, figures=len(fs))


def mask(g, names):
    return sum(1 << g.names.index(x) for x in names)


def ten_element():
    names = ['0', 'ap', 'a', 'b', 'c', 'A', 'Ap', 'B', 'C', '1']
    vals = [0, 1, 3, 4, 8, 12, 14, 11, 7, 15]
    le = lambda a, b: a & ~b == 0
    def meet(a, b):
        lows = [x for x in vals if le(x, a) and le(x, b)]
        greatest = [x for x in lows if all(le(y, x) for y in lows)]
        assert len(greatest) == 1
        return greatest[0]
    def join(a, b):
        ups = [x for x in vals if le(a, x) and le(b, x)]
        least = [x for x in ups if all(le(x, y) for y in ups)]
        assert len(least) == 1
        return least[0]
    for a, b in product(vals, repeat=2):
        meet(a, b); join(a, b)
        assert (15 ^ a) in vals and (15 ^ (15 ^ a)) == a
        assert meet(a, 15 ^ a) == 0 and join(a, 15 ^ a) == 15
        assert not le(a, b) or le(15 ^ b, 15 ^ a)
    for a, b, c in product(vals, repeat=3):
        assert meet(a, meet(b, c)) == meet(meet(a, b), c)
        assert join(a, join(b, c)) == join(join(a, b), c)
    assert le(1, 3) and meet(3, 14) == 0 and join(1, meet(3, 14)) != 3
    three_element_reading = [x for x in vals if x.bit_count() == 3]
    assert three_element_reading == [14, 11, 7]
    assert all(not le(a, b) for a, b in product(three_element_reading, repeat=2) if a != b)
    covers = [(names[i], names[j]) for i, a in enumerate(vals) for j, b in enumerate(vals)
              if a != b and le(a, b) and not any(x not in (a, b) and le(a, x) and le(x, b) for x in vals)]
    return dict(labels=dict(zip(names, vals)), covers=covers,
                meet_table=[[names[vals.index(meet(a, b))] for b in vals] for a in vals],
                join_table=[[names[vals.index(join(a, b))] for b in vals] for a in vals],
                orthocomplement={names[i]:names[vals.index(15 ^ a)] for i, a in enumerate(vals)},
                pairs_checked=100, triples_checked=1000,
                orthomodular=False, witness=['ap', 'a'],
                literal_three_subset_reading=three_element_reading,
                literal_three_subset_reading_is_lattice=False)


def old_eight_strata():
    names = ['a', 'b', 'X', 'p', 'e', 'w', 'h', 'g']
    idx = {x: i for i, x in enumerate(names)}
    pairs = [('a', 'b'), ('a', 'p'), ('b', 'p'), ('a', 'e'),
             ('b', 'w'), ('p', 'w'), ('e', 'h'), ('h', 'g'), ('g', 'w')]
    internal_edges = pairs + [('X', 'a'), ('X', 'b'), ('X', 'w')]
    m = Magasin(names, [(idx['a'], idx['X']), (idx['b'], idx['X'])],
                [(idx['p'], idx['X'])], [(idx[x], idx[y]) for x, y in internal_edges])
    m.magaxioms(); m.core()
    flags = m.flags()
    assert all(flags.values()), flags
    # Old supports use full figure disjointness, not primitive internal disjunction.
    full_edges = [(i, j) for i, j in combinations(range(8), 2) if m.fd(m.down[i], m.down[j])]
    g = Orthoset(names, full_edges)
    open_masks = []
    for i in range(8):
        down = sum(1 << j for j in m.down[i])
        boundary = down ^ (1 << i)
        op = g.close(down) & g.polar(boundary)
        open_masks.append(op)
        assert all((j, i) in m.ref for j in bits(op))  # old absorption
        scan90 = sum(1 << j for j in m.M if (j, i) in m.ref and (g.polar(boundary) >> j) & 1)
        lieu_open = sum(1 << p for p in m.lieux if (p, i) in m.intern)
        assert op == scan90
        assert g.polar(op) == g.polar(lieu_open)
    for figure in m.F:
        deployment_mask = sum(1 << i for i in figure)
        union_open = 0
        for i in figure: union_open |= open_masks[i]
        assert g.polar(deployment_mask) == g.polar(union_open)
    assert open_masks[idx['X']] == mask(g, ['p'])
    S = lambda indices: g.close(sum((open_masks[idx[i]] for i in indices), 0))
    # The three open masks here are disjoint singletons, so sum is union.
    assert S(['a', 'b', 'X']) == g.full
    complement_left = S(['a', 'b', 'X']) & g.polar(S(['a']))
    complement_right = S(['b', 'X'])
    meet_left = S(['a', 'X']) & S(['a', 'b'])
    assert complement_left == mask(g, ['b', 'p', 'e'])
    assert complement_right == mask(g, ['b', 'p'])
    assert meet_left == mask(g, ['a', 'w']) and S(['a']) == mask(g, ['a'])
    return dict(model=g.describe(), internal_edges=internal_edges,
                old_axiom_flags=flags, absorption=True, figures=len(m.F),
                scan87_scan90_open_sets_equal=True, open_lieu_polars_checked=8,
                theorem94_part_d_figures_checked=len(m.F),
                open_parts={names[i]:g.decode(a) for i,a in enumerate(open_masks)},
                complement_failure=[g.decode(complement_left),g.decode(complement_right)],
                meet_failure=[g.decode(meet_left),g.decode(S(['a']))],
                lattice=check_ortholattice(g))


def check_external():
    m = Magasin(['a', 'b'], [], [(0, 1)], [])
    m.magaxioms(); m.core()
    supports = [frozenset({'p'}), frozenset({'p', 'q'})]
    for i, j in product(range(2), repeat=2):
        assert ((i,j) in m.orth) == (not supports[i] & supports[j])
        if (i,j) in m.intern: assert supports[i] <= supports[j]
        lower_intersects = any((k,i) in m.intern and (k,j) in m.intern for k in range(2))
        assert ((i,j) in m.orth) == (not lower_intersects)
    assert frozenset().union(*supports) == {'p','q'}
    full_left = frozenset().union(*(supports[z] for z in range(2) if (z,0) in m.orth))
    full_right = frozenset({'p','q'}) - supports[0]
    assert full_left != full_right
    return dict(vertices=m.names,incidence='identity',interior_refinement=[['a','a'],['b','b'],['a','b']],
                disjunction=[],supports=[sorted(s) for s in supports],faithful=True,
                normalized=True,fully_faithful=False,witness=[sorted(full_left),sorted(full_right)])


def check_correspondences():
    # Classical orthosets have identity double-polar closure: every relation is a bond.
    cases = [(1,2,[3]), (2,1,[1,1])]
    result=[]
    for n,m,alpha in cases:
        f=lambda a: sum(0 for _ in []) if not a else __import__('functools').reduce(int.__or__,(alpha[x] for x in bits(a)),0)
        for a,b in product(range(1<<n), repeat=2):
            assert f(a|b)==f(a)|f(b)
        assert f(0)==0
        result.append(dict(source=n,target=m,relation_images=alpha,join_preserving=True,
                           is_function=all(a.bit_count()==1 for a in alpha),
                           preserves_orthogonality=all(not(alpha[x]&alpha[y]) for x,y in combinations(range(n),2))))
    return result


def graph_census(maxn=5):
    """Independent exhaustive cross-check of the two exact general criteria."""
    out=[]
    for n in range(maxn+1):
        pairs=list(combinations(range(n),2)); total=0; om=0; boolean=0; normal=0
        for k in range(1<<len(pairs)):
            g=Orthoset(range(n),[e for j,e in enumerate(pairs) if k>>j&1])
            assert (g.om_witness() is None)==(g.dacey_witness() is None)
            point_bool=all(any((g.adj[x]|g.adj[y])&~g.adj[z]==0 for z in range(n))
                           for x,y in product(range(n),repeat=2) if not(g.adj[x]>>y&1))
            assert point_bool==(g.boolean_witness() is None)
            cliques=[a for a in range(1<<n) if all(g.adj[x]>>y&1 for x,y in combinations(bits(a),2))]
            assert (g.sumner_witness() is None)==(supp1_witness(g,cliques) is None)
            for x in range(n):
                sx=g.close(1<<x)
                atom=not any(a and a!=sx and a&~sx==0 for a in g.closed())
                test=all(g.adj[x]&~g.adj[y]!=0 or g.adj[x]==g.adj[y] for y in range(n))
                assert atom==test
            total+=1;om+=g.om_witness() is None;boolean+=point_bool;normal+=g.sumner_witness() is None
        out.append(dict(vertices=n,graphs=total,orthomodular=om,Boolean=boolean,Sumner_normal=normal))
    return out


def main():
    started=perf_counter();out={}
    lt={(0,2),(0,3),(1,2),(1,3)}
    g=magasin(4,lt)
    assert len(g.closed())==20
    assert g.om_witness() is not None and g.sumner_witness() is None
    assert supp1_witness(g,figures(g)) is None
    m,fs,axioms=check_identity_magasin(g)
    assert supp1_witness(g,fs) is None
    # Verify the actual interval-magasin relations, not only the identity model.
    le=[(i,j) for i,x in enumerate(g.names) for j,y in enumerate(g.names) if i!=j and incidence(x,y)]
    rho=[(i,j) for i,x in enumerate(g.names) for j,y in enumerate(g.names) if i!=j and immediate(lt,x,y)]
    edges=[(i,j) for i,j in combinations(range(g.n),2) if g.adj[i]>>j&1]
    actual=Magasin(g.names,le,rho,edges);actual.magaxioms();actual.core()
    assert {sum(1<<i for i in f) for f in actual.F}==set(figures(g))
    out['crown_M']=dict(model=g.describe(),lattice=check_ortholattice(g),
                         actual_figures=[g.decode(f) for f in figures(g)],
                         actual_strong_axioms=True,all_figures_supp1=True,
                         identity_lieu_model=axioms)
    for name,names,edges in [
      ('O6',['ap','a','b','bp'],[(0,1),(1,2),(2,3)]),
      ('C5',list(range(5)),[(i,(i+1)%5) for i in range(5)]),
      ('MO2',list(range(4)),[(0,1),(2,3)]),
      ('twins',['x','y'],[]),
      ('Boolean_noncograph',['a','b','c','x','y'],[(0,1),(0,2),(1,2),(2,3),(0,4)])]:
        h=Orthoset(names,edges);m,fs,flags=check_identity_magasin(h)
        w=supp1_witness(h,fs)
        out[name]=dict(model=h.describe(),lattice=check_ortholattice(h),axioms=flags,
                       supp1_witness=[h.decode(a) for a in w] if w else None)
    assert out['Boolean_noncograph']['lattice']['Boolean']
    assert out['Boolean_noncograph']['lattice']['closed']==8
    c5=Orthoset(range(5),[(i,(i+1)%5) for i in range(5)])
    weak=Magasin(list(range(5)),[(0,1),(2,1)],[],[(i,(i+1)%5) for i in range(5)])
    weak.magaxioms(False)
    deps=[tuple(sorted(d)) for d in weak.down]
    assert len(set(deps))==5 and all(c5.close(1<<i)==1<<i for i in range(5))
    assert (0,2) not in weak.orth
    out['weak_Atspat']=dict(incidence=[[0,1],[2,1]],orthogonality='C5',
                            all_point_supports_singleton=True,deployments=deps,
                            injective=True,ordinary_set_target=True,strong_Mag4=False)
    out['ten_element']=ten_element()
    out['R5_eight_strata']=old_eight_strata()
    out['A5_external']=check_external()
    out['L7_correspondences']=check_correspondences()
    out['graph_census']=graph_census(5)
    out['runtime_seconds']=perf_counter()-started
    out['result']='ALL ASSERTIONS PASSED'
    print(json.dumps(out,indent=2))


if __name__=='__main__': main()
