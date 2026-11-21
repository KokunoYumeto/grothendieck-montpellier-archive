"""Exact new Rankin cross-product checks for MA-RB-006.

Reuses the already checked S5 character table. No arithmetic realization,
zero-location calculation or higher functorial lift is asserted.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT / "s5_hecke_cone.json").read_text())
classes = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes = [1,10,15,20,20,30,24]
table = sp.Matrix([old["character_table"][str(c)] for c in classes])
indices = [4,5,2,3,6]
names = ["A","Aeta","V","Veta","X"]
artin_names = ["W","Weta","V","Veta","X"]
T = sp.Symbol("T")
delta = ((1+T)/(1-T))**2
v = [1,-1,sp.I,-sp.I]
w = [1,-1,-1,sp.I,-sp.I]
a = [1,1,1,sp.I,-sp.I]
x = [sp.simplify(v[i]*v[j]) for i in range(4) for j in range(i+1,4)]
auto = [a,[-t for t in a],v,[-t for t in v],x]
artin = [w,[-t for t in w],v,[-t for t in v],x]

def poly_tensor(left,right):
    return sp.expand(sp.prod(1-sp.simplify(x*y)*T for x in left for y in right))

b,n,v0,v1,e,x1,k = sp.symbols("b n v0 v1 e x1 k")
orders = sp.Matrix([0,b,v0,v1,n+k,x1,e])
witness = {b:0,n:0,v0:0,v1:k,e:0,x1:0}
matrix_E = sp.zeros(5)
matrix_witness = sp.zeros(5)
rows = []
for i in range(5):
    for j in range(i,5):
        product = sp.matrix_multiply_elementwise(table[:,indices[i]],table[:,indices[j]])
        coefficients = table.T*sp.diag(*sizes)*product/120
        assert all(t.is_Integer and t >= 0 for t in coefficients)
        assert table*coefficients == product
        exponent = 2 if i == j and i < 2 else (-2 if (i,j)==(0,1) else 0)
        ratio = sp.factor(poly_tensor(artin[i],artin[j])/poly_tensor(auto[i],auto[j]))
        assert sp.cancel(ratio-delta**exponent)==0
        order = sp.expand((coefficients.T*orders)[0]-exponent*k)
        formal_order = sp.expand(order.subs(witness))
        formal_coefficient = sp.simplify(formal_order/k)
        assert formal_coefficient.is_Integer and formal_coefficient >= 0
        matrix_E[i,j] = matrix_E[j,i] = exponent
        matrix_witness[i,j] = matrix_witness[j,i] = formal_coefficient
        rows.append({
            "automorphic_pair":[names[i],names[j]],
            "Artin_pair":[artin_names[i],artin_names[j]],
            "tensor_coefficients":[int(t) for t in coefficients],
            "Euler_discrepancy_exponent":exponent,
            "local_ratio":str(ratio),
            "pointwise_order":str(order),
            "formal_order_divided_by_k":int(formal_coefficient),
        })
expected = sp.Matrix([[0,4,1,2,2],[4,0,2,1,2],[1,2,1,1,2],
                      [2,1,1,1,2],[2,2,2,2,3]])
assert matrix_witness == expected
assert all(sp.simplify(sum(z**j for z in eigenvalues))==0
           for eigenvalues in (v,[-t for t in v],x) for j in (1,3))
out = {
    "statement":"MA-RB-006",
    "date":"2026-11-21",
    "model":"GPT-6 Astra Pro; effort inherited/not externally exposed",
    "scope":"Fifteen Rankin pairs using the checked finite table; no arithmetic realization",
    "row_order":names,
    "irreducible_order":["1","eta","V","Veta","W","Weta","X"],
    "discrepancy_exponent_matrix":[[int(t) for t in row] for row in matrix_E.tolist()],
    "formal_order_matrix_divided_by_k":[[int(t) for t in row] for row in matrix_witness.tolist()],
    "pairs":rows,
    "all_assertions_passed":True,
}
(ROOT/"s5_rankin_cross.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"pairs":15,"exact_tensor_decompositions":15,
                  "exact_local_ratios":15,"formal_matrix_nonnegative":True,
                  "all_assertions_passed":True}))
