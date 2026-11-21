"""Independent transcription and full-polynomial verification of F026."""
from itertools import product, permutations
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as sp

rows = [
    [1,0,0,0,0,0,0],
    [0,4,2,-3,-1,0,-3],
    [2,1,3,4,1,3,-3],
    [0,3,4,-1,2,-2,2],
    [-3,-4,-2,-1,1,-2,3],
    [3,3,0,2,-3,4,2],
    [-2,-3,-3,3,1,-1,3],
    [0,-1,2,2,1,4,-1],
    [4,-3,-1,-3,-1,4,-1],
]
target = sorted(e for e in product(range(4),repeat=7) if sum(e)==3 and sum(e[2:])<=2)
columns = list(range(7,48))+list(range(49,55))+[56,57]

def expand(A):
    result = {}
    for permutation in permutations(range(3)):
        factors = [A[3*i+permutation[i]] for i in range(3)]
        for choices in product(range(7),repeat=3):
            coefficient = factors[0][choices[0]]*factors[1][choices[1]]*factors[2][choices[2]]
            if coefficient:
                exponent = tuple(choices.count(k) for k in range(7))
                result[exponent] = result.get(exponent,0)+coefficient
    return result

base = expand(rows)
J = [[0]*63 for _ in target]
for source in range(63):
    varied = [row[:] for row in rows]
    varied[source//7][source%7] += 1
    new = expand(varied)
    for row,exponent in enumerate(target):
        J[row][source] = new.get(exponent,0)-base.get(exponent,0)
M = sp.Matrix([[row[j] for j in columns] for row in J])
det = int(M.det(method="domain-ge"))
assert len(columns)==49 and min(columns)>=7
assert det == 31568108869448599905478876197553019094163200564336768
assert det % 1000003 == 641253
result = {
    "date_utc":datetime.now(timezone.utc).isoformat(),
    "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
    "method":"Fresh transcription of the displayed pencil and49allowedcolumns; full six-product permanent expansion; all63 exact coefficient differences; integer square determinant by Sympy domain-ge.",
    "rows":49,"source_columns":63,"fixed_source_columns":list(range(7)),
    "selected_columns":columns,"integer_determinant":str(det),
    "prime":1000003,"residue":det%1000003,"status":"PASS",
}
Path(__file__).with_name("fixed_per3_witness_independent_certificate.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
