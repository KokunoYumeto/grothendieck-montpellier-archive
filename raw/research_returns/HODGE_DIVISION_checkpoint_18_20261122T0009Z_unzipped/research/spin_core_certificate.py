#!/usr/bin/env python3
"""Root's exact small-cover input verification for HD-SPIN-01.

This does not import the GAP scan or its row selections. It reads the
complete published tables and uses integer cyclotomic polynomials.
Group/table identification and the all-n spin minimum are cited inputs.
"""
from pathlib import Path
from functools import lru_cache
from math import lcm
import hashlib, json
import sympy as sp
from flint import fmpz_poly

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT/"agents/imprimitive/sporadic/alternating_cover_inputs.json"
X = sp.Symbol("x")

@lru_cache(None)
def modulus(n):
    coeffs = sp.Poly(sp.cyclotomic_poly(n, X), X).all_coeffs()
    return fmpz_poly([int(a) for a in reversed(coeffs)])

def conductor(value):
    return 1 if isinstance(value, int) else value[0]

def polynomial(value, n, conjugate=False):
    if isinstance(value, int):
        return fmpz_poly([value])
    m, coeffs = value
    assert n % m == 0
    out = [0]*n
    for j, coefficient in enumerate(coeffs):
        exponent = j*(n//m)*(-1 if conjugate else 1)
        out[exponent % n] += coefficient
    return fmpz_poly(out) % modulus(n)

def equal(a, b, conjugate_b=False):
    n = lcm(conductor(a), conductor(b))
    return polynomial(a,n) == polynomial(b,n,conjugate_b)

def norm_upper(value):
    n = conductor(value)
    p = (polynomial(value,n)*polynomial(value,n,True)) % modulus(n)
    return sum(abs(int(c)) for c in p.coeffs())

def indicator(table, character):
    p2 = next(row["map"] for row in table["power_maps"] if row["prime"]==2)
    values = [character[j-1] for j in p2]
    n = lcm(*(conductor(v) for v in values))
    total = fmpz_poly([0])
    for size, value in zip(table["sizes"], values):
        total += size*polynomial(value,n)
    total %= modulus(n)
    assert total.degree()<=0
    value = int(total[0])
    assert value % table["order"] == 0
    return value//table["order"]

raw = INPUT.read_bytes()
data = json.loads(raw)
assert [t["name"] for t in data["tables"]] == ["2.A6","2.A8","2.A9","2.A10","2.A11"]
result = {"status":"PASS", "input_sha256":hashlib.sha256(raw).hexdigest(),
          "scope":"Exact finite published inputs, not classification or all-n degree proof",
          "tables":[], "local_ratio_entries":0}
for table in data["tables"]:
    chars = table["characters"]
    assert sum(c[0]**2 for c in chars) == table["order"]
    assert sum(table["sizes"]) == table["order"]
    central = [j for j,s in enumerate(table["sizes"]) if s==1]
    assert len(central)==2
    z = next(j for j in central if table["orders"][j]==2)
    # Select from the actual values, not the supplied selected_rows metadata.
    rows = [i for i,c in enumerate(chars) if c[z]==-c[0]]
    assert all(c[0]>=4 for i,c in enumerate(chars) if i in rows)
    record = {"name":table["name"], "faithful_degrees":[chars[i][0] for i in rows],
              "degree24":[]}
    if table["name"]=="2.A6":
        for i in rows:
            e = chars[i][0]
            for j,value in enumerate(chars[i]):
                if j in central:
                    continue
                assert 4*norm_upper(value)<=e*e, (i+1,j+1)
                result["local_ratio_entries"] += 1
    for i in rows:
        chi = chars[i]
        if chi[0]!=24:
            continue
        nonreal = [j+1 for j,v in enumerate(chi) if not equal(v,v,True)]
        assert nonreal
        conjugates = [k+1 for k,c in enumerate(chars)
                      if all(equal(a,b,True) for a,b in zip(chi,c))]
        assert len(conjugates)==1 and conjugates[0]!=i+1
        fs = indicator(table,chi)
        assert fs==0
        # All nonrational values live in Q(zeta_7); the nonreal
        # quadratic field identification is explicit in the written proof.
        assert set(conductor(v) for v in chi) <= {1,7}
        record["degree24"].append({"row":i+1, "indicator":fs,
                                  "conjugate_row":conjugates[0],
                                  "nonreal_classes":nonreal})
    result["tables"].append(record)
assert [(r["name"],len(r["degree24"])) for r in result["tables"]] == [
    ("2.A6",0),("2.A8",2),("2.A9",0),("2.A10",0),("2.A11",0)]
ceil = lambda a,b: (a+b-1)//b
allowed = [e for e in range(9,25) if 2*ceil(e,2)+10*ceil(e,8)<=2*e+6]
assert allowed==[14,15,16,24]
result["ESD_ceiling_degrees_9_through_24"] = allowed
assert [e for e in allowed if e>=24] == [24]
result["after_independent_BI09_lower_bound"] = [24]
result["written_continuous_bound"] = "e<=24; no finite truncation is used for larger e"
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"PASS", "tables":len(data["tables"]),
                  "local_ratio_entries":result["local_ratio_entries"],
                  "degree24":"only the two nonreal 2.A8 rows",
                  "input_sha256":result["input_sha256"]}))
