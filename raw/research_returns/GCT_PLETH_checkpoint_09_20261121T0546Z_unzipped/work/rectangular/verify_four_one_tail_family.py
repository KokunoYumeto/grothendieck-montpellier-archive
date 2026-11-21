"""R039: literal affine-minor canonical pairing and independent MN tests."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, comb
import csv
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_two_column_tail_unit_family import det
from verify_second_row_two_rank_law import product_form

HERE = Path(__file__).resolve().parent


def literal_pairing(a, n, m, vectors):
    product = product_form(vectors)
    pair = {}
    for beta, value in product.items():
        norm = Fraction(value, factorial(n))
        for b in beta:
            norm *= factorial(b)
        pair[beta] = norm
    perms = tuple((p, sign(p)) for p in permutations(range(m+1)))
    answer = Fraction(0)
    outside = pair.get((n,) + (0,)*m, 0) ** (a-m-1)
    # det(x,y_1,...,y_m) times
    # det(x^2,xy_1,...,xy_(m-1),y_1^2), in each occupied slot.
    for sigma, s1 in perms:
        for tau, s2 in perms:
            value = outside*s1*s2
            for i in range(m+1):
                beta = [n-3]+[0]*m
                beta[sigma[i]] += 1
                if tau[i] == 0:
                    beta[0] += 2
                elif tau[i] == m:
                    beta[1] += 2
                else:
                    beta[0] += 1
                    beta[tau[i]] += 1
                value *= pair.get(tuple(beta), 0)
                if not value:
                    break
            answer += value
    return comb(a, m+1)*answer


def affine_polynomial(vectors):
    m = len(vectors[0])-1
    affine = [(Fraction(1),) + tuple(Fraction(v, row[0]) for v in row[1:])
              for row in vectors]
    answer = Fraction(0)
    for I in combinations(range(len(vectors)), m+1):
        R = [affine[i] for i in I]
        B = [row[:m] + (row[1]**2,) for row in R]
        answer += det(R)*det(B)
    return answer


def target_polynomial(a, vectors):
    u = 1
    for row in vectors:
        u *= row[0]
    return u**a * affine_polynomial(vectors)


def centered_cramer(vectors):
    a = len(vectors)
    m = len(vectors[0])-1
    w = [tuple(Fraction(v, row[0]) for v in row[1:]) for row in vectors]
    mean = [sum(row[p] for row in w)/a for p in range(m)]
    z = [tuple(row[p]-mean[p] for p in range(m)) for row in w]
    S = [[sum(row[p]*row[q] for row in z) for q in range(m)]
         for p in range(m)]
    c = [sum(row[p]*row[0]**2 for row in z) for p in range(m)]
    for p in range(m):
        S[p][-1] = c[p]
    return det(S)


def sample(n, m, tag):
    if tag == 0 and n >= m+1:
        lower = [tuple(int(i == p) for i in range(m)) for p in range(m)]
        lower += [(-1,)*m] + [(0,)*m]*(n-m-1)
    else:
        lower = [tuple((i+1)**(p+1) + tag*(p+1) for p in range(m))
                 for i in range(n)]
    return [(i+2,) + tuple((i+2)*v for v in row)
            for i, row in enumerate(lower)]


def write(name, rows):
    with (HERE/name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = []
    for a in range(3, 7):
        for n in range(3, 7):
            for m in range(2, min(a, 5)):
                for tag in (0, 1):
                    vectors = sample(n, m, tag)
                    A = affine_polynomial(vectors)
                    H = centered_cramer(vectors)
                    assert A == n*H, (a,n,m,tag,A,H)
                    if tag == 0 and n >= m+1:
                        assert H == -2
                    left = literal_pairing(a,n,m,vectors)
                    target = target_polynomial(a,vectors)
                    scalar = Fraction(2*(-1)**(m-1)*factorial(a),
                        factorial(a-m-1)*n**(m+1)*(n-1)**m*(n-2))
                    assert left == scalar*target, (a,n,m,tag,left,scalar,target)
                    if tag == 0:
                        assert bool(left) == (n >= m+1)
                    rows.append(dict(a=a,n=n,m=m,sample=tag,
                        literal_pairing=str(left),scalar=str(scalar),
                        target_polynomial=str(target),affine_equals_n_cramer=True,
                        status='PASS'))
        print('literal affine-minor checks completed a',a,flush=True)
    write('FOUR_ONE_TAIL_CANONICAL_SCALAR_CHECK.tsv',rows)
    print('PASS literal affine-minor pairings',len(rows),flush=True)
    rows=[]
    for a in range(3,8):
        for n in range(3,6):
            for m in range(2,a):
                lam=(a*n-2*m-1,4)+(2,)*(m-2)+(1,)
                assert tuple(sorted(lam,reverse=True))==lam
                target=actual((a,),n,lam)
                source=actual((n,),a,lam)
                assert target==1,(a,n,m,target)
                assert source==int(n>=m+1),(a,n,m,source)
                rows.append(dict(a=a,n=n,m=m,output=','.join(map(str,lam)),
                    target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('MN family checks completed a',a,'cases',len(rows),flush=True)
    write('FOUR_ONE_TAIL_MN_CHECK.tsv',rows)
    print('PASS independent target/source MN pairs',len(rows),flush=True)


if __name__ == '__main__':
    main()
