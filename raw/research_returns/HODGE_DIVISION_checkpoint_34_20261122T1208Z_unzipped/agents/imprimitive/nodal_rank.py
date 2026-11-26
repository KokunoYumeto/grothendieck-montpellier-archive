#!/usr/bin/env python3
"""Exact finite-field minor certificate for a nodal cyclic Prym differential.

Reduction of integral Z[zeta_d] polynomial coefficients modulo 1009.
If a minor is nonzero, it was nonzero in characteristic zero.
No floating point arithmetic is used.
"""
import json

P = 1009

def trim(v):
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return v

def mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i + j] = (ans[i + j] + x * y) % P
    return trim(ans)

def add(a, b, k=1):
    ans = [0] * max(len(a), len(b))
    for i, x in enumerate(a): ans[i] += x
    for i, x in enumerate(b): ans[i] += k*x
    return trim([x % P for x in ans])

def poly_without(points, excluded):
    ans = [1]
    for a in points:
        if a != excluded: ans = mul(ans, [-a % P, 1])
    return ans

def rank_pivots(mat):
    a = [row[:] for row in mat]
    pivots = []
    row = 0
    for col in range(len(a[0])):
        piv = next((i for i in range(row,len(a)) if a[i][col] % P), None)
        if piv is None: continue
        a[row], a[piv] = a[piv], a[row]
        iv = pow(a[row][col], -1, P)
        a[row] = [(x*iv)%P for x in a[row]]
        for i in range(len(a)):
            if i == row: continue
            v = a[i][col]
            if v: a[i] = [(x-v*y)%P for x,y in zip(a[i],a[row])]
        pivots.append(col)
        row += 1
        if row == len(a): break
    return row, pivots

def determinant(a):
    a = [row[:] for row in a]
    ans = 1
    for j in range(len(a)):
        i = next((i for i in range(j,len(a)) if a[i][j]%P), None)
        if i is None: return 0
        if i != j:
            a[j], a[i] = a[i], a[j]
            ans = -ans
        pivot = a[j][j] % P
        ans = ans*pivot % P
        inv = pow(pivot,-1,P)
        for k in range(j+1,len(a)):
            v = a[k][j]*inv % P
            for l in range(j,len(a)):
                a[k][l] = (a[k][l]-v*a[j][l])%P
    return ans%P

def primitive_root_of_order(d):
    for z in range(2,P):
        if pow(z,d,P) == 1 and all(pow(z,k,P)!=1 for k in range(1,d)):
            return z
    raise ValueError(d)

def certificate(d, g=6):
    z = primitive_root_of_order(d)
    points = list(range(1,2*g+1))
    partials = {i: poly_without(points,i) for i in points}
    def forms(q):
        aa = [add(partials[2*j+1],partials[2*j+2],-q) for j in range(g)]
        return [add(aa[j],aa[-1],-1) for j in range(g-1)]
    f, h = forms(z), forms(pow(z,-1,P))
    assert all(len(x)<=2*g-1 for x in f+h)
    cols = [mul(a,b) for a in f for b in h]
    rows = [[col[k] if k<len(col) else 0 for col in cols] for k in range(4*g-3)]
    rank, column_ids = rank_pivots(rows)
    selected = [[row[j] for j in column_ids] for row in rows]
    _, row_ids = rank_pivots(list(map(list,zip(*selected))))
    minor = [[rows[i][j] for j in column_ids] for i in row_ids]
    det = determinant(minor)
    assert det != 0
    return {"d":d,"g":g,"prime":P,"zeta_mod_prime":z,
            "node_pairs":[[2*j+1,2*j+2] for j in range(g)],
            "rank_mod_prime":rank,"column_ids_zero_based":column_ids,
            "row_ids_zero_based":row_ids,"minor_determinant_mod_prime":det,
            "minor":minor}

if __name__ == "__main__":
    print(json.dumps([certificate(d) for d in [3,4,6]],indent=2))
