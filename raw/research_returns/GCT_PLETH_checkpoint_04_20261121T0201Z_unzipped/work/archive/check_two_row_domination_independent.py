"""Independent G021 domination via ambient Schur sections minus actual jets.

The root computation uses the two-row quotient resolution. This check uses
the complementary-rectangle Borel--Weil module and a 3x3 Jacobi--Trudi
determinant. Differences use a direct Stirling-number formula.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from math import comb,factorial
import ast,json,hashlib
import sympy as s

HERE=Path(__file__).resolve().parent
TARGET=HERE.parent/"root"/"TWO_ROW_QUOTIENT_POLYNOMIAL_BOUND.json"
x,b,k,t=s.symbols("x b k t")
variables=(x,b,k,t);a=x+b;c=2*k+t
target=json.loads(TARGET.read_text())
def residue(expr,p,modulus):
    return int(s.sympify(expr).subs(dict(zip(variables,p))))%modulus
def h(expr,kind,p):
    n=s.sympify(expr)
    if kind=="id":return (n+1)*(n+2)*(n+3)/6
    if kind=="trans":
        return ((n+2)**2-residue(n,p,2))/4
    if kind=="double":
        return s.Integer(0) if residue(n,p,2) else (n+2)/2
    if kind=="three":
        return (n+3-residue(n,p,3))/3
    raise ValueError(kind)
def as_dict(expr):
    return {tuple(exponent):Fraction(int(value.p),int(value.q))
            for exponent,value in s.Poly(s.expand(expr),*variables).terms() if value}
def ambient_minus_jets(kind,p):
    H=lambda n:h(n,kind,p)
    # tau=(a+c,a,a-b,0); the last Jacobi--Trudi row is (0,0,0,1).
    ambient=s.det(s.Matrix([[H(a+c),H(a+c+1),H(a+c+2)],
                            [H(a-1),H(a),H(a+1)],
                            [H(x-2),H(x-1),H(x)]]))
    if kind=="trans":
        ambient*=(-1)**((p[0]+p[1])%2)
    HW=lambda n:H(n)-H(n-1)
    fiber=HW(a)*HW(b)-HW(a+1)*HW(b-1)
    fixed={"id":5,"trans":3,"double":1,"three":2}[kind]
    return as_dict(ambient-fixed*H(k-1)*fiber)

identity=ambient_minus_jets("id",(0,0,0,0))
compact=(b+1)*(x+1)*(b+x+2)/2 * (
    ((c+1)*(c+2)*(c+3)-5*k*(k+1)*(k+2))/6
    +(2*b+x)*(c+1)*(c+2)/6
    +b*(b+x+1)*(c+1)/6)
assert identity==as_dict(compact)
target_identity={ast.literal_eval(key):Fraction(value)
                 for key,value in target["identity_polynomial"].items()}
assert identity==target_identity and len(identity)==122
assert all(value>0 for value in identity.values())
downset=set()
for exponent in identity:downset.update(product(*(range(e+1) for e in exponent)))
assert downset==set(identity)
assert sorted(downset)==[tuple(v) for v in target["downset"]]
print("Independent ambient identity: 122 positive monomials, downset PASS",flush=True)

phases={}
phase_receipts={}
for kind,modulus,degree in (("trans",2,3),("double",2,2),("three",3,1)):
    polys=[ambient_minus_jets(kind,p) for p in product(range(modulus),repeat=4)]
    actual_degree=max((sum(e) for poly in polys for e in poly),default=-1)
    assert actual_degree==degree
    phases[kind]=polys
    canonical=[{str(e):str(v) for e,v in sorted(poly.items())} for poly in polys]
    phase_receipts[kind]={"phase_count":len(polys),"total_degree":degree,
                          "sha256":hashlib.sha256(json.dumps(canonical,sort_keys=True).encode()).hexdigest()}
    print(kind,len(polys),"ambient phase polynomials; degree",degree,flush=True)

stirling=[[0]*7 for _ in range(7)];stirling[0][0]=1
for n in range(1,7):
    for r in range(1,n+1):stirling[n][r]=stirling[n-1][r-1]+r*stirling[n-1][r]
def monomial_difference(exponent,order):
    choices=[]
    for power,number in zip(exponent,order):
        if number==0:choices.append([(power,1)])
        elif power<number:return []
        else:
            choices.append([(power-removed,comb(power,removed)*60**removed*
                             factorial(number)*stirling[removed][number])
                            for removed in range(number,power+1)])
    terms=[]
    for selected in product(*choices):
        e=tuple(pair[0] for pair in selected);coeff=1
        for _,v in selected:coeff*=v
        terms.append((e,coeff))
    return terms
def difference(poly,order):
    out={}
    for exponent,value in poly.items():
        for e,mult in monomial_difference(exponent,order):
            out[e]=out.get(e,Fraction(0))+value*mult
    return {e:v for e,v in out.items() if v}
orders=[order for order in product(range(4),repeat=4) if 1<=sum(order)<=3]
expected_rows={tuple(row["order"]):row for row in target["positive_order_checks"]}
rows=[];smallest=None
for order in orders:
    dominant=difference(identity,order)
    absolute={}
    for kind,weight in (("trans",10),("double",15),("three",20)):
        maxima={}
        for poly in phases[kind]:
            for exponent,value in difference(poly,order).items():
                maxima[exponent]=max(maxima.get(exponent,Fraction(0)),abs(value))
        for exponent,value in maxima.items():
            absolute[exponent]=absolute.get(exponent,Fraction(0))+weight*value
    margins={e:dominant.get(e,Fraction(0))-absolute.get(e,Fraction(0))
             for e in set(dominant)|set(absolute)}
    assert all(value>=0 for value in margins.values())
    constant=margins.get((0,0,0,0),Fraction(0))
    assert constant>0
    smallest=constant if smallest is None else min(smallest,constant)
    expected=expected_rows[order]
    assert constant==Fraction(expected["constant_margin"])
    assert min(margins.values())==Fraction(expected["minimum_coefficient_margin"])
    rows.append({"order":order,"constant_margin":str(constant),
                 "minimum_coefficient_margin":str(min(margins.values())),
                 "complete_margin_polynomial":{str(e):str(v) for e,v in sorted(margins.items())}})
assert len(rows)==34 and smallest==29260

# Higher active orders have no nonidentity term and a positive constant from
# their own positive identity monomial. This checks every one of them.
higher=[]
for order in sorted(downset):
    if sum(order)<4:continue
    dp=difference(identity,order)
    assert all(v>0 for v in dp.values()) and dp[(0,0,0,0)]>0
    assert all(not difference(poly,order) for pp in phases.values() for poly in pp)
    higher.append(order)
assert len(higher)==87
receipt={"statement":"Independent G021 exact polynomial domination",
 "status":"PASS","method":"Ambient complementary-rectangle Schur module minus point jets; 3x3 Jacobi--Trudi; direct Stirling finite differences.",
 "identity_positive_monomials":122,"identity_total_degree":6,
 "active_downset":[list(e) for e in sorted(downset)],"phase_data":phase_receipts,
 "positive_low_order_checks":rows,"minimum_constant_margin":str(smallest),
 "higher_active_orders_checked":len(higher),
 "all_positive_active_orders":121,
 "target_sha256":hashlib.sha256(TARGET.read_bytes()).hexdigest()}
(HERE/"TWO_ROW_DOMINATION_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","positive_monomials":122,
 "low_orders":34,"higher_orders":len(higher),"minimum_margin":str(smallest)},indent=2))
