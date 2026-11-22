"""Independent finite checks for the explicit NN-G020 torus matrix.

This is a finite arithmetic check, not a proof of normality or hardness.
It imports no supplied formula-to-polytope construction. Clauses include
all repeated-literal possibilities, the place where coefficient bounds
and the positive functional require care.
"""
from itertools import combinations_with_replacement, product
from pathlib import Path
import json


def weights(n, clauses):
    m = len(clauses)
    matrix = [[0] * (2*n + m) for _ in range(n+m)]
    for i in range(n):
        matrix[i][2*i] = matrix[i][2*i+1] = 1
    for c, clause in enumerate(clauses):
        for var, negated in clause:
            matrix[n+c][2*var+int(negated)] += 1
        matrix[n+c][2*n+c] = -1
    return matrix


def matvec(matrix, vector):
    return [sum(a*b for a, b in zip(row, vector)) for row in matrix]


def direct_count(n, clauses):
    return sum(all(any(bool(bits[var]) != negated for var, negated in c)
                   for c in clauses) for bits in product((0, 1), repeat=n))


def lattice_vectors(n, clauses, degree):
    for xs in product(range(degree+1), repeat=n):
        xy = [v for x in xs for v in (x, degree-x)]
        slack = [sum(xy[2*i+int(neg)] for i, neg in c)-degree
                 for c in clauses]
        if all(s >= 0 for s in slack):
            yield xy+slack


def main():
    formulas = 0
    degree_counts = 0
    lattice_points = 0
    repeated_occurrence_cases = 0
    unsatisfiable = 0
    for n in (1, 2):
        literals = tuple(product(range(n), (False, True)))
        possible = tuple(combinations_with_replacement(literals, 3))
        for m in range(3):
            for clauses in product(possible, repeat=m):
                formulas += 1
                A = weights(n, clauses)
                beta = [3*m+1]*n + [-1]*m
                assert min(sum(beta[r]*A[r][j] for r in range(n+m))
                           for j in range(2*n+m)) >= 1
                assert n*(3*m+1)-m > 0
                assert matvec(A, [1]*(2*n+m)) == [2]*(n+m)
                if any(len(set(c)) < 3 for c in clauses):
                    repeated_occurrence_cases += 1
                count = direct_count(n, clauses)
                unsatisfiable += int(count == 0)
                for k in range(9):
                    vectors = list(lattice_vectors(n, clauses, k))
                    degree_counts += 1
                    lattice_points += len(vectors)
                    assert all(matvec(A, z) == [k]*(n+m) for z in vectors)
                    if k == 0:
                        assert vectors == [[0]*(2*n+m)]
                    elif k == 1:
                        assert len(vectors) == count
                    else:
                        assert vectors
                        xy = [v for _ in range(n) for v in (k//2, (k+1)//2)]
                        slack = [sum(xy[2*i+int(neg)] for i, neg in c)-k
                                 for c in clauses]
                        z = xy+slack
                        assert min(z) >= 0
                        assert matvec(A, z) == [k]*(n+m)
                        assert z in vectors
    certificate = {
        'finding': 'NN-G020',
        'scope': 'all formulas with n=1,2 and m=0,1,2 from unordered three-position literal multisets; ordered clause sequences; degrees0..8',
        'formulas': formulas,
        'formulas_with_repeated_literal_occurrences': repeated_occurrence_cases,
        'unsatisfiable_formulas': unsatisfiable,
        'degree_counts_checked': degree_counts,
        'lattice_points_checked': lattice_points,
        'checks': ['positive beta on every weight column',
                   'known rational half-point via twice its vector',
                   'degree0 unique constant',
                   'degree1 count agrees with direct truth-table count',
                   'all enumerated exponent vectors satisfy the matrix equations',
                   'universal explicit witness works in degrees2..8'],
        'outcome': 'PASS',
        'limits': 'Finite checks do not certify the unbounded construction, invariant-ring normality, or complexity reductions; those have written proofs.'
    }
    Path('work/gct/toric_sat_family_certificate.json').write_text(
        json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(certificate, indent=2))


if __name__ == '__main__':
    main()
