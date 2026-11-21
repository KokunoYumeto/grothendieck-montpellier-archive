"""Exact new quadratic Schur checks for MA-RB-005.

Uses the previously checked S5 table; does not rerun old certificates.
No arithmetic field, zero-location assertion or analytic formalization.
"""
from pathlib import Path
from collections import Counter
from math import gcd
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT / "s5_hecke_cone.json").read_text())
classes = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes = [1,10,15,20,20,30,24]
table = sp.Matrix([old["character_table"][str(c)] for c in classes])

def power_class(c, j):
    return tuple(sorted([length // gcd(length, j)
                         for length in c for _ in range(gcd(length, j))],
                        reverse=True))

chi = table[:,4]
chi2 = sp.Matrix([old["character_table"][str(power_class(c,2))][4]
                  for c in classes])
sym_chi = sp.Matrix([(chi[i]**2+chi2[i])/2 for i in range(7)])
ext_chi = sp.Matrix([(chi[i]**2-chi2[i])/2 for i in range(7)])
sym_coeff = sp.Matrix([1,0,1,0,1,1,0])
ext_coeff = sp.Matrix([0,0,0,1,0,0,1])
assert table*sym_coeff == sym_chi
assert table*ext_coeff == ext_chi

a,b,nu = sp.symbols("a b nu", nonzero=True)
spin = [a,b,nu/a,nu/b]
ext_spin = [sp.factor(spin[j]*spin[k]/nu)
            for j in range(4) for k in range(j+1,4)]
std = ext_spin.copy()
std.remove(sp.Integer(1))
assert len(std)==5
sym_spin = [sp.factor(spin[j]*spin[k]/nu)
            for j in range(4) for k in range(j,4)]
ext_std = [sp.factor(std[j]*std[k])
           for j in range(5) for k in range(j+1,5)]
assert Counter(sym_spin) == Counter(ext_std)

T=sp.Symbol("T")
pi=[1,1,1,sp.I,-sp.I]
W=[1,-1,-1,sp.I,-sp.I]
def schur(e, exterior):
    return [sp.simplify(e[j]*e[k]) for j in range(len(e))
            for k in range(j+(1 if exterior else 0),len(e))]
def poly(e):
    return sp.expand(sp.prod(1-z*T for z in e))
delta=((1+T)/(1-T))**2
ratios={}
for label,exterior in [("Sym2_varpi",False),("Exterior2_varpi",True)]:
    ratio=sp.factor(poly(schur(W,exterior))/poly(schur(pi,exterior)))
    assert sp.cancel(ratio-delta)==0
    twisted=sp.factor(ratio.subs(T,-T))
    assert sp.cancel(twisted-1/delta)==0
    ratios[label]=str(ratio)
    ratios[label+"_eta"]=str(twisted)

bb,n,v0,v1,e,x1,k=sp.symbols("b n v0 v1 e x1 k")
x=n+k
orders={
 "Sym2_Pi_normalized":v1+e-k,
 "Sym2_Pi_normalized_eta":v0+e+k,
 "Sym2_varpi":sp.expand(v0+x+x1-k),
 "Sym2_varpi_eta":sp.expand(bb+v1+x+x1+k),
 "Exterior2_varpi":v1+e-k,
 "Exterior2_varpi_eta":v0+e+k,
}
assert orders["Sym2_varpi"]==v0+n+x1
assert orders["Sym2_varpi_eta"]==bb+v1+n+x1+2*k
witness={bb:0,n:0,v0:0,v1:1,e:0,x1:0,k:1}
values={label:int(expr.subs(witness)) for label,expr in orders.items()}
assert min(values.values())>=0
assert int((bb+4*v0+4*v1+5*x+5*x1+6*e).subs(witness))==9
general_witness={bb:0,n:0,v0:0,v1:k,e:0,x1:0}
assert [sp.expand(orders[label].subs(general_witness))
        for label in ("Sym2_Pi_normalized","Sym2_Pi_normalized_eta",
                      "Sym2_varpi","Sym2_varpi_eta")] == [0,k,0,3*k]
out={
 "date":"2026-11-21",
 "model":"GPT-6 Astra Pro; effort inherited/not externally exposed",
 "scope":"Only the new quadratic Schur and order calculations; no arithmetic realization",
 "class_order":[list(c) for c in classes],
 "Sym2_W_character":[int(v) for v in sym_chi],
 "Exterior2_W_character":[int(v) for v in ext_chi],
 "Sym2_W_coefficients":[int(v) for v in sym_coeff],
 "Exterior2_W_coefficients":[int(v) for v in ext_coeff],
 "GSp4_general_weight_identity":True,
 "local_Euler_ratios":ratios,
 "pointwise_orders":{key:str(value) for key,value in orders.items()},
 "off_center_formal_witness_values":values,
 "formal_regular_order":9,
 "all_assertions_passed":True,
}
(ROOT/"s5_quadratic_schur.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"new_character_identities":2,"general_GSp4_identity":1,
                  "new_Euler_ratios":4,"order_forms":6,
                  "all_assertions_passed":True}))
