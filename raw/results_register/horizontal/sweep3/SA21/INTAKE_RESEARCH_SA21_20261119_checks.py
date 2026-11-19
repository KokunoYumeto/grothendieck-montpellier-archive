# Independent finite checks for the intake of RESEARCH_SA21 (final of 19 Nov 2026, GPT-6 Astra, ChatGPT Pro mode).
# Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. It imports and runs no program of the return.
# Definitions as in the run's parts/supports/supports.tex: an orthoset (E, perp) with perp symmetric and irreflexive,
# N(A) = common perp-neighbourhood, supports = closed sets N(N(A)); comparability disjoncteur of a poset: strict
# comparability; interval magasin M(L): points P_a, intervals I_ab (a<b), positional order U < V iff U != V and every
# endpoint of U is <= every endpoint of V; its disjunction is strict positional comparability.
# Usage: python -I -B INTAKE_RESEARCH_SA21_20261119_checks.py
from itertools import combinations, permutations

def posets(n):                       # naturally labelled posets on 0..n-1, up to isomorphism
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen, out = set(), []
    for m in range(1 << len(pairs)):
        rel = {pairs[k] for k in range(len(pairs)) if m >> k & 1}
        if any((i, k) not in rel for (i, j) in rel for (j2, k) in rel if j == j2):
            continue
        canon = min(tuple(sorted((q[i], q[j]) for i, j in rel)) for q in permutations(range(n)))
        if canon not in seen:
            seen.add(canon); out.append(rel)
    return out

def support_lattice(E, perp):
    N = lambda A: frozenset(x for x in E if all(perp(x, a) for a in A))
    closed = {frozenset(E)}
    frontier = [N([x]) for x in E]
    for c in frontier:
        closed.add(c)
    changed = True
    while changed:
        changed = False
        for a in list(closed):
            for b in list(closed):
                c = a & b
                if c not in closed:
                    closed.add(c); changed = True
    return closed, N

def classify(E, perp):
    closed, N = support_lattice(E, perp)
    cl = lambda A: N(N(A))
    join = lambda a, b: cl(a | b)
    oml = all(join(b, a & N(b)) == a for a in closed for b in closed if b <= a)
    if not oml:
        return len(closed), False, False
    boolean = all(join(a & b, a & N(b)) == a for a in closed for b in closed)
    return len(closed), True, boolean

def M(L, n):
    less = lambda a, b: (a, b) in L
    le = lambda a, b: a == b or less(a, b)
    E = [('P', a) for a in range(n)] + [('I', a, b) for a, b in sorted(L)]
    ends = {e: ({e[1]} if e[0] == 'P' else {e[1], e[2]}) for e in E}
    lt = lambda U, V: U != V and all(le(u, v) for u in ends[U] for v in ends[V])
    return E, (lambda U, V: lt(U, V) or lt(V, U))

def conditional_lattice(L, n):
    le = lambda a, b: a == b or (a, b) in L
    for a, b in combinations(range(n), 2):
        ub = [c for c in range(n) if le(a, c) and le(b, c)]
        if ub and not any(all(le(j, c) for c in ub) for j in ub):
            return False
        lb = [c for c in range(n) if le(c, a) and le(c, b)]
        if lb and not any(all(le(c, m) for c in lb) for m in lb):
            return False
    return True

def nonisolated_chain(L, n):
    nis = [a for a in range(n) if any((a, b) in L or (b, a) in L for b in range(n))]
    return all((a, b) in L or (b, a) in L for a, b in combinations(nis, 2))

def cograph(L, n):                   # comparability graph P4-free
    adj = lambda a, b: (a, b) in L or (b, a) in L
    for q in permutations(range(n), 4):
        a, b, c, d = q
        if adj(a, b) and adj(b, c) and adj(c, d) and not adj(a, c) and not adj(b, d) and not adj(a, d):
            return False
    return True

def boolean_test_A04(E, perp):       # the run's Theorem A04: x not perp y => exists z with N(x) u N(y) in N(z)
    N1 = {x: frozenset(z for z in E if perp(z, x)) for x in E}
    return all(any(N1[x] | N1[y] <= N1[z] for z in E) for x in E for y in E if not perp(x, y))

for n in range(1, 6):
    Ps = posets(n)
    bad_oml = bad_bool = bad_a04 = 0; cd_oml = cd_cog_not_oml = 0; cd_oml_not_cog = []
    for L in Ps:
        E, perp = M(L, n)
        k, oml, boo = classify(E, perp)
        bad_oml += (oml != conditional_lattice(L, n))
        bad_bool += (boo != nonisolated_chain(L, n))
        bad_a04 += (boo != boolean_test_A04(E, perp))
        Ec = list(range(n)); pc = lambda x, y, L=L: (x, y) in L or (y, x) in L
        kc, omlc, booc = classify(Ec, pc)
        cd_oml += omlc
        cog = cograph(L, n)
        cd_cog_not_oml += (cog and not omlc)
        if omlc and not cog:
            cd_oml_not_cog.append(sorted(L))
    print('n=%d: %d posets; M(L): OML differs from "conditional lattice" in %d, Boolean differs from "nonisolated '
          'points form a chain" in %d, A04 test differs from Boolean in %d; comparability disjoncteur of L: OML in %d, '
          'cograph but not OML %d, OML but not cograph %d%s'
          % (n, len(Ps), bad_oml, bad_bool, bad_a04, cd_oml, cd_cog_not_oml, len(cd_oml_not_cog),
             (' (first: %s)' % cd_oml_not_cog[0]) if cd_oml_not_cog else ''))

crown = {(0, 2), (0, 3), (1, 2), (1, 3)}
E, perp = M(crown, 4)
k, oml, boo = classify(E, perp)
print('four-point crown: strata %d, supports %d, orthomodular %s' % (len(E), k, oml))

# atoms: supp of a lieu (point symbol P_x) is cl({P_x}); an atom = minimal nonzero support
def atom_claim(n):
    bad = 0
    for L in posets(n):
        E, perp = M(L, n)
        closed, N = support_lattice(E, perp)
        nonzero = [c for c in closed if c]
        atoms = {c for c in nonzero if not any(d < c for d in nonzero)}
        allatoms = all(N(N([('P', x)])) in atoms for x in range(n))
        isolated = [a for a in range(n) if not any((a, b) in L or (b, a) in L for b in range(n))]
        claim = (not L) or not isolated
        bad += (allatoms != claim)
    return bad
print('atom question (every lieu support an atom iff L is an antichain or has no isolated points): disagreements',
      [atom_claim(n) for n in range(1, 6)])
