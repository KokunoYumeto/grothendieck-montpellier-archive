"""Complete census and explicit witness checks for finite M(L).

AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, 2026-11-19.
Uses the root's finite-polarity implementation, but constructs the cut
certificates and split comparison independently from their proofs.
Every transitive subrelation of one fixed natural total order is tested.
Every isomorphism type is represented; differently linearly labelled
copies are not counted as all labelled posets.
"""
from pathlib import Path
import sys, json, time
from itertools import combinations, product

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'code'))
from supports_core import Orthoset, natural_posets, magasin, bits


def missing_join(n, lt):
    le = lambda x,y: x == y or (x,y) in lt
    for x,y in combinations(range(n),2):
        U = {z for z in range(n) if le(x,z) and le(y,z)}
        if U and not any(all(le(z,w) for w in U) for z in U):
            return x,y,U
    return None


def conditional_witness(n, lt):
    j = missing_join(n,lt)
    if j:
        return 'join',lt,j
    dual = {(y,x) for x,y in lt}
    j = missing_join(n,dual)
    if j:
        return 'meet',dual,j
    return None


def cut_certificate(n, lt, witness):
    x,y,U = witness
    le = lambda a,b: a == b or (a,b) in lt
    I = {a for a in range(n) if all(le(a,u) for u in U)}
    assert U == {u for u in range(n) if all(le(i,u) for i in I)}
    assert I and U and not I & U
    maxima = [a for a in I if not any((a,b) in lt for b in I)]
    assert len(maxima) >= 2
    a,b = maxima[:2]
    minima = [m for m in range(n) if le(m,a) and not any((p,m) in lt for p in range(n))]
    assert minima
    m = minima[0]
    u = min(U)
    g = magasin(n,lt)
    ix = {name:i for i,name in enumerate(g.names)}
    delta = lambda z: z[1:]
    X = sum(1 << k for k,z in enumerate(g.names) if all(v in I for v in delta(z)))
    Y = sum(1 << k for k,z in enumerate(g.names) if all(v in U for v in delta(z)))
    basis_names = [('P',a)] if m == a else [('P',m),('I',m,a),('P',a)]
    B = sum(1 << ix[z] for z in basis_names)
    sep = ix[('I',a,u)]
    missed = ix[('P',b)]
    assert g.polar(X) == Y and g.polar(Y) == X
    assert B & ~X == 0
    assert all(g.adj[i] >> j & 1 for i,j in combinations(bits(B),2))
    assert X & g.polar(B) == 0  # maximality inside X
    assert g.polar(B) >> sep & 1
    assert not (g.adj[sep] >> missed & 1)
    assert X >> missed & 1 and not (g.close(B) >> missed & 1)
    assert g.om_witness() is not None
    return dict(I=sorted(I),U=sorted(U),a=a,b=b,m=m,u=u,
                X=g.decode(X),basis=basis_names,
                separator=g.names[sep],missed=g.names[missed])


def split_space(n, lt):
    def leS(u,v):
        return u == v or (u//2 == v//2 and u%2 < v%2) or (u//2,v//2) in lt
    Q = [(u,v) for u,v in product(range(2*n),repeat=2) if u != v and leS(u,v)]
    edges = [(i,j) for i,j in combinations(range(len(Q)),2)
             if leS(Q[i][1],Q[j][0]) or leS(Q[j][1],Q[i][0])]
    return Orthoset(Q,edges)


def check_transfer(n, lt):
    m = magasin(n,lt)
    q = split_space(n,lt)
    mix = {z:i for i,z in enumerate(m.names)}
    dm = []
    for lo,hi in q.names:
        a,b = lo//2,hi//2
        if a == b:
            pieces = [('P',a)]
        else:
            pieces = ([('P',a)] if lo%2 == 0 else []) + [('I',a,b)]
            if hi%2 == 1:pieces.append(('P',b))
        dm.append(sum(1 << mix[p] for p in pieces))
    for i,j in product(range(q.n),repeat=2):
        allpieces = all(m.adj[a] >> b & 1 for a,b in product(bits(dm[i]),bits(dm[j])))
        assert bool(q.adj[i] >> j & 1) == allpieces
    extension = lambda B: sum(1 << i for i,D in enumerate(dm) if not D & ~B)
    extensions = {extension(B) for B in m.closed()}
    assert extensions == set(q.closed())
    for B in m.closed():
        assert extension(m.polar(B)) == q.polar(extension(B))
    return len(m.closed()),len(q.names)


def source_counterexample():
    P = range(4)
    lt = {(0,1),(2,3)}
    Q = list(sorted(lt))
    le = lambda a,b: a == b or (a,b) in lt
    g = Orthoset(Q,[(i,j) for i,j in combinations(range(2),2)
                   if le(Q[i][1],Q[j][0]) or le(Q[j][1],Q[i][0])])
    assert g.adj == [0,0] and g.closed() == [0,3]
    assert g.close(1) == 3
    down = [r for r in Q if le(Q[0][0],r[0]) and le(r[1],Q[0][1])]
    assert down == [Q[0]]
    return dict(P=list(P),strict_order=sorted(lt),quotients=Q,
                orthogonality_edges=[],closed_sets=[g.decode(C) for C in g.closed()],
                singleton_double_polar=g.decode(g.close(1)),
                singleton_interval_ideal=down,
                refutes='Jenca arXiv2206.08113v1 Corollary4.5 unbounded wording')


def illustrative_models():
    out = []
    for name,lt in [('crown6',{(i,3+j) for i in range(3) for j in range(3) if i!=j}),
                    ('triangle_face_poset',{(i,3+j) for j in range(3) for i in (j,(j+1)%3)})]:
        g = magasin(6,lt)
        assert conditional_witness(6,lt) is None
        assert g.om_witness() is None
        out.append(dict(name=name,supports=len(g.closed()),orthomodular=True,
                        conditional_lattice=True,bounded=False,connected=True))
    return out


if __name__ == '__main__':
    start = time.perf_counter()
    counts = []
    first = None
    transfer_count = 0
    certificates = 0
    for n in range(7):
        t = time.perf_counter()
        row = dict(n=n,total=0,conditional_OM=0,nonconditional_nonOM=0,
                   conditional_nonOM=0,nonconditional_OM=0)
        for lt in natural_posets(n):
            row['total'] += 1
            witness = conditional_witness(n,lt)
            g = magasin(n,lt)
            om = g.om_witness() is None
            conditional = witness is None
            row[('conditional_' if conditional else 'nonconditional_') + ('OM' if om else 'nonOM')] += 1
            assert om == conditional, (n,sorted(lt),witness,g.om_witness())
            if witness is not None:
                direction,oriented_lt,j = witness
                cert = cut_certificate(n,oriented_lt,j)
                certificates += 1
                if first is None:
                    first = dict(n=n,strict_order=sorted(lt),direction=direction,**cert)
            if n <= 4:
                check_transfer(n,lt)
                transfer_count += 1
        row['runtime_seconds'] = round(time.perf_counter()-t,6)
        counts.append(row)
        print(json.dumps({'census_progress':row}),flush=True)
    result = dict(program='check_conditional_lattices.py',census=counts,
                  n6_total=counts[-1]['total'],
                  all_conditional_equivalences_passed=True,
                  exhaustive_cut_certificates=certificates,
                  split_transfer_cases_through_n4=transfer_count,
                  first_cut_certificate=first,
                  source_counterexample=source_counterexample(),
                  illustrative_models=illustrative_models(),
                  total_runtime_seconds=round(time.perf_counter()-start,6))
    print(json.dumps(result,indent=2),flush=True)
