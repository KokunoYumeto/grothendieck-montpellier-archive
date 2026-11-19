"""Independent exact checks for the literal finite-group fixed-point claim.
The spherical-building argument and its convexity convention are written in
parts/b/git_primary_followup.md. Matrix enumeration is a check, not its proof.
"""
import json
from pathlib import Path
import sympy as s

i=s.I
A=s.diag(i,-i)
B=s.Matrix([[0,1],[-1,0]])
I=s.eye(2)
def key(M):
    return tuple(str(s.simplify(x)) for x in M)
group={key(I):I}
todo=[I]
while todo:
    x=todo.pop()
    for g in (A,B):
        y=s.simplify(x*g)
        if key(y) not in group:
            group[key(y)]=y
            todo.append(y)
e1=s.Matrix([1,0])
e2=s.Matrix([0,1])
out={
  "A":str(A), "B":str(B),
  "det_A":str(A.det()), "det_B":str(B.det()),
  "A_squared_minus_identity": A*A == -I,
  "B_squared_minus_identity": B*B == -I,
  "anticommutation": B*A == -A*B,
  "generated_group_order": len(group),
  "A_distinct_eigenvalues": A[0,0] != A[1,1],
  "B_swaps_coordinate_lines": B*e1 == -e2 and B*e2 == e1,
  "conclusion": "Any common invariant line must be an A eigenline; B exchanges the two, so there is none.",
  "scope": "Exact symbolic matrix check. Convexity of the whole rank-one spherical building and isometry are justified separately in prose."
}
assert out["det_A"]=="1" and out["det_B"]=="1"
assert len(group)==8
assert all(out[k] for k in ["A_squared_minus_identity","B_squared_minus_identity","anticommutation","A_distinct_eigenvalues","B_swaps_coordinate_lines"])
dest=Path("/workspace/scratch/594d1dc856a9/SA04_work/outputs/b_tits_check.json")
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

