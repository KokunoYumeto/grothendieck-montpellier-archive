"""Independent check of the benzel shell note (Papors/Chatnotes/Benzel), written by the OLDER_NOTES finder.

Region (axial coords as in the note): B_{a,b} = {(q,r): -(a-1) <= L_i(q,r) <= b-1}, L1=2q+r-1, L2=r-q, L3=1-q-2r.
Type 103 prototiles: R={(0,0),(1,0),(0,1)}, H, V, D bones. Counts tilings by simple exact-cover backtracking
(first uncovered cell in a fixed order must be covered by a tile placement containing it).
Also checks Lemma (three translates inside B_n) and the uniqueness of the A-shell tiling for small n.
"""
import sys
from functools import lru_cache

R = [(0, 0), (1, 0), (0, 1)]
H = [(0, 0), (1, 0), (2, 0)]
V = [(0, 0), (0, 1), (0, 2)]
D = [(0, 0), (1, -1), (2, -2)]
TILES = {'R': R, 'H': H, 'V': V, 'D': D}


def region(a, b):
    cells = set()
    for q in range(-3 * (a + b), 3 * (a + b)):
        for r in range(-3 * (a + b), 3 * (a + b)):
            Ls = (2 * q + r - 1, r - q, 1 - q - 2 * r)
            if all(-(a - 1) <= L <= b - 1 for L in Ls):
                cells.add((q, r))
    return frozenset(cells)


def placements(cells, kinds):
    pl = {}
    for c in cells:
        pl[c] = []
    for k in kinds:
        shape = TILES[k]
        for (q, r) in cells:
            for (dq, dr) in shape:
                ox, oy = q - dq, r - dr
                t = frozenset((ox + x, oy + y) for (x, y) in shape)
                if t <= cells:
                    pl[(q, r)].append((k, t))
    # dedupe
    for c in pl:
        seen = set()
        out = []
        for k, t in pl[c]:
            if (k, t) not in seen:
                seen.add((k, t))
                out.append((k, t))
        pl[c] = out
    return pl


def count_tilings(cells, kinds='RHVD', collect=False, limit=None):
    order = sorted(cells, key=lambda c: (c[1], c[0]))
    pl = placements(cells, kinds)
    res = []
    counts = {}
    cnt = [0]

    def rec(covered, used):
        # first uncovered
        for c in order:
            if c not in covered:
                break
        else:
            cnt[0] += 1
            vec = tuple(sum(1 for k, _ in used if k == x) for x in 'HVDR')
            counts[vec] = counts.get(vec, 0) + 1
            if collect:
                res.append(list(used))
            return
        for k, t in pl[c]:
            if covered.isdisjoint(t):
                used.append((k, t))
                rec(covered | t, used)
                used.pop()
                if limit and cnt[0] >= limit:
                    return
    rec(frozenset(), [])
    return cnt[0], counts, res


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    for n in range(5, nmax + 1):
        Bn = region(n, 2 * n - 3)
        area_formula = (3 * n * n - 9 * n + 6) // 2
        t, counts, _ = count_tilings(Bn)
        print(f"n={n} (a,b)=({n},{2*n-3}) |B_n|={len(Bn)} formula={area_formula} T103={t} patterns={len(counts)}")
        Rn = {v[3] for v in counts}
        print(f"   right-stone counts {sorted(Rn)}  expected {(n-2)*(n-5)//2}")
        if n >= 6:
            Bp = region(n - 1, 2 * n - 5)
            for name, (dq, dr) in {'A': (-1, 1), 'B': (0, -1), 'C': (1, 0)}.items():
                tr = frozenset((q + dq, r + dr) for (q, r) in Bp)
                inside = tr <= Bn
                shell = Bn - tr
                ts, cs, _ = count_tilings(shell)
                print(f"   shell {name}: translate inside={inside} |shell|={len(shell)} tilings={ts} vec={list(cs.keys())}")
        # predicted simplex
        pred = set()
        for a_ in range(n - 4):
            for b_ in range(n - 4 - a_):
                c_ = n - 5 - a_ - b_
                pred.add((3 + 2 * b_ + c_, 3 + 2 * a_ + b_, 3 + a_ + 2 * c_, (n - 2) * (n - 5) // 2))
        print(f"   observed patterns == shell simplex: {set(counts) == pred}")
    # straight family (n, 2n): claim T103 = 1
    for n in range(2, 8):
        E = region(n, 2 * n)
        t, counts, _ = count_tilings(E)
        print(f"(n,2n)=({n},{2*n}) |E|={len(E)} T103={t} {list(counts.keys())}")


if __name__ == '__main__':
    main()
