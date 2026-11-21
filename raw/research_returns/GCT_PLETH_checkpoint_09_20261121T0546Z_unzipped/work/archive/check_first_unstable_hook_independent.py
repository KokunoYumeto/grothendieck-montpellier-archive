"""Independent exact evaluation matrices and deleted-point encodings for T061."""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial
from collections import Counter
import sys, json

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "theta" / "unstable_hook"))
import first_unstable_hook_positive as target


def exact_rank(columns):
    pivots = {}
    for source in columns:
        col = {k: Fraction(v) for k, v in source.items() if v}
        while col:
            p = min(col)
            if p not in pivots:
                s = col[p]
                pivots[p] = {k: v/s for k, v in col.items()}
                break
            s = col[p]
            for k, v in pivots[p].items():
                col[k] = col.get(k, 0) - s*v
                if not col[k]:
                    del col[k]
    return len(pivots)


def adjoint_columns(m, r):
    """Frame e_1,...,e_d,-sum e_i; exterior quotient bases are explicit."""
    d = m-1
    for i in range(m):
        vector = {i: 1} if i < d else {j: -1 for j in range(d)}
        quotient_basis = [j for j in range(d) if j != (i if i < d else d-1)]
        for subset in combinations(quotient_basis, r):
            wedge = {}
            for j, value in vector.items():
                if j in subset:
                    continue
                indices = tuple(sorted((j,) + subset))
                wedge[indices] = value * (-1)**sum(k < j for k in subset)
            yield {(j, indices): value*coefficient
                   for j, value in vector.items()
                   for indices, coefficient in wedge.items()}


def specht_dimension(shape):
    hooks = 1
    for i, width in enumerate(shape):
        for j in range(width):
            hooks *= width-j + sum(v > j for v in shape[i+1:])
    return factorial(sum(shape)) // hooks


@lru_cache(None)
def tableaux(shape):
    if not shape:
        return ((),)
    result = []
    for i, width in enumerate(shape):
        if i+1 < len(shape) and shape[i+1] == width:
            continue
        smaller = list(shape)
        smaller[i] -= 1
        while smaller and smaller[-1] == 0:
            smaller.pop()
        result.extend(T + ((i+1, width),) for T in tableaux(tuple(smaller)))
    return tuple(result)


def coin_tuples(weights, degree):
    if degree < 0:
        return
    if not weights:
        if degree == 0:
            yield ()
        return
    for exponent in range(degree//weights[0]+1):
        for tail in coin_tuples(weights[1:], degree-weights[0]*exponent):
            yield (exponent,) + tail


def witnesses(m, a, r, shape):
    """Enumerate directly from tableaux, chosen cells and all coin solutions."""
    D = a+r
    if shape == (m,):
        assert r == 0
        for exponents in coin_tuples(tuple(range(2,m+1)), D):
            least = min(i for i,v in enumerate(exponents,2) if v)
            yield {**{f"z{i}": int(i == least) for i in range(2,m+1)},
                   **{f"y{i}": 0 for i in range(2,m+1)},
                   **{f"b{i}": v for i,v in enumerate(exponents,2)}}
        return
    cells = tuple((i+1,j+1) for i,width in enumerate(shape) for j in range(width))
    retained = tuple(c for c in cells if c not in ((1,1),(2,1)))
    for T in tableaux(shape):
        desc = {j: int(T[j][0] > T[j-1][0]) for j in range(1,m)}
        degree = sum((m-j)*v for j,v in desc.items())
        for chosen in combinations(retained,r):
            remainder = D-degree-sum(j-i+1 for i,j in chosen)
            for exponents in coin_tuples(tuple(range(2,m+1)),remainder):
                yield {
                    **{f"X{i}_{j}_{label}": int(T[label-1] == (i,j))
                       for i,j in cells for label in range(1,m+1)},
                    **{f"d{j}": v for j,v in desc.items()},
                    **{f"Y{i}_{j}": int((i,j) in chosen) for i,j in retained},
                    **{f"c{i}": v for i,v in enumerate(exponents,2)}
                }


def accepts(polytope, point):
    if set(point) != set(polytope["variables"]):
        return False
    for row in polytope["constraints"]:
        value = sum(c*point[v] for v,c in row["coefficients"].items())
        rhs, relation = row["rhs"], row["relation"]
        if relation == "=" and value != rhs:
            return False
        if relation == "<=" and value > rhs:
            return False
        if relation == ">=" and value < rhs:
            return False
    return True


def main():
    counts = Counter()
    matrices = []
    for m in range(4,9):
        d = m-1
        for r in range(m-1):
            rank = exact_rank(adjoint_columns(m,r))
            target_dimension = m*comb(d-1,r)
            defect = int(r == m-2)
            assert rank == target_dimension-defect, (m,r,rank)
            source_dimension = d*comb(d,r+1)-(comb(d,r+2) if r+2 <= d else 0)
            kernel_dimension = source_dimension-rank
            if r <= m-4:
                shape = (m-r-2,2)+(1,)*r
                assert kernel_dimension == specht_dimension(shape)
                counts["degree_two_valid_kernel_dimensions"] += 1
            else:
                assert kernel_dimension == 0
            matrices.append({"m":m,"r":r,"rank":rank,
                             "target_dimension":target_dimension,
                             "cokernel_dimension":defect})
            counts["exact_adjoint_matrices"] += 1

    for m in range(4,7):
        for r in range(m-1):
            for a in range(3,7):
                for shape in target.target_labels(m,r):
                    data = target.polytopes(m,a,r,0,shape)
                    removed = data["removed_point"]
                    pieces = data["polytopes"]
                    base = target.stable.module_polytope(m,a,r,shape)
                    assert accepts(base,removed)
                    assert not any(accepts(P,removed) for P in pieces)
                    original = retained = removed_occurrences = 0
                    for point in witnesses(m,a,r,shape):
                        assert accepts(base,point)
                        original += 1
                        if point == removed:
                            removed_occurrences += 1
                            continue
                        variables = base["variables"]
                        j = next(j for j,v in enumerate(variables) if point[v] != removed[v])
                        direction = 0 if point[variables[j]] < removed[variables[j]] else 1
                        assert accepts(pieces[2*j+direction],point)
                        if m == 4:
                            assert sum(accepts(P,point) for P in pieces) == 1
                            counts["complete_membership_checks"] += 1
                        retained += 1
                    assert removed_occurrences == 1
                    assert original-1 == retained == target.coefficient(m,a,r,0,shape)
                    counts["deleted_point_cases"] += 1
                    counts["exported_piece_matrices"] += len(pieces)
                    counts["original_lattice_points"] += original
                    counts["retained_lattice_points"] += retained

    # Large binary degree and full retained-subset endpoints are tested literally.
    for m in (4,7,12):
        for r in sorted({0,1,m-3,m-2}):
            for a in (3,4,10**40+1):
                for shape in target.target_labels(m,r):
                    point = target.canonical_removed_point(m,a,r,shape)
                    assert accepts(target.stable.module_polytope(m,a,r,shape),point)
                    counts["large_or_endpoint_removed_points"] += 1
    out = {
        "statement":"T061 independent evaluation and deleted-point audit",
        "status":"PASS",
        "methods":[
            "rational column elimination of actual frame exterior adjoints",
            "independent removable-corner tableaux and all coin solutions",
            "literal exported inequalities and unique first-difference pieces"
        ],
        **dict(counts),
        "adjoint_matrices":matrices,
        "original_cycle_sweep":"not repeated"
    }
    (HERE/"FIRST_UNSTABLE_HOOK_INDEPENDENT_RECEIPT.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="adjoint_matrices"},indent=2))


if __name__ == "__main__":
    main()
