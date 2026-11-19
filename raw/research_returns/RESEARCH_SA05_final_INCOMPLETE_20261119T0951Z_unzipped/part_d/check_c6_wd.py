"""Exact certificates for the formal limitation of unramifiedness tests.

These are abstract Weil--Deligne pairs, not claimed realizations of motives.
They disprove a proposed formal implication, not a motivic conjecture.
"""
from pathlib import Path
import json
import sympy as sp

root = Path(__file__).resolve().parent
q = sp.Integer(4)
n_regular = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
n_subregular = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
f_regular = sp.diag(q, 1, 1/q)
f_subregular = sp.diag(2, sp.Rational(1, 2), 1)
zero = sp.zeros(3)

def certificate(name, frobenius, nilpotent):
    assert frobenius.det() == 1
    assert frobenius * nilpotent * frobenius.inv() == q * nilpotent
    assert nilpotent**3 == zero
    return {
        "name": name,
        "frobenius": [[str(x) for x in row] for row in frobenius.tolist()],
        "nilpotent": nilpotent.tolist(),
        "rank_N": nilpotent.rank(),
        "rank_N_squared": (nilpotent**2).rank(),
        "dimension_inertia_invariants": 3-nilpotent.rank(),
        "det_F": str(frobenius.det()),
        "AdF_N_equals_qN": True,
        "N_cubed_zero": True,
    }

out = {
    "scope": "Abstract WD pairs only; no motivic counterexample asserted.",
    "q": int(q),
    "pairs": [
        certificate("principal, pure of weight zero", f_regular, n_regular),
        certificate("subregular, pure of weight zero", f_subregular, n_subregular),
        certificate("same Weil part as principal, not asserted pure", f_regular, n_subregular),
    ],
    "representation_theoretic_argument": (
        "For every rational algebraic representation r of SL3, dr(N)=0 for a "
        "nonzero N if and only if r is trivial: ker(dr) is an ideal in the simple "
        "Lie algebra sl3. Thus all three pairs have identical unramifiedness "
        "tests in Rep(SL3), including after finite extension, while their "
        "nilpotent Jordan types differ. This argument, not finite testing of "
        "representations, proves the universal assertion."
    ),
}
assert out["pairs"][0]["rank_N"] == 2
assert out["pairs"][1]["rank_N"] == 1
assert out["pairs"][0]["rank_N_squared"] == 1
assert out["pairs"][1]["rank_N_squared"] == 0
text = json.dumps(out, indent=2, default=int)
(root / "check_c6_wd_output.json").write_text(text + "\n")
print(text)
