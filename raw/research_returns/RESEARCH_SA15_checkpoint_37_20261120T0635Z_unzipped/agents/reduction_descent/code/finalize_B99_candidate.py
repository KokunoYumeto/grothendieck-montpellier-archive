from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
p = own/"B_valuation_one_irreducible_candidate.tex"
code = own/"code/verify_valuation_one_irreducible.py"
out = code.with_suffix(".output.json")
data = json.loads(out.read_text())
assert data["status"] == "PASS"
old = p.read_text()
before = """finite-residue class-field theorem is claimed. An exact standalone
supplement will check these symbolic and finite arithmetic steps;
it will infer no formal-group realization.
"""
after = r"""finite-residue class-field theorem is claimed. The standalone
supplement
\path{code/reduction_descent/verify_valuation_one_irreducible.py}
passed on 20 November 2026 at 06:03:28.889962 UTC in
4.479122429998824 seconds. It checks 15 symbolic identities,
49 sectors at seven primes, including 42 sectors with
$\gcd(t,N)>1$, 103,029 derivative monomials including 1,895
indices divisible by $p$, 98 distinct-residue profiles,
147 critical-boundary checks, 7,893 fixed-ordinary-term
inequalities and 717 two-break Herbrand identities.
The exact rational upper-break census contains 195,496 pairs
and 390,992 terminal comparisons; no integrality of upper
breaks is assumed. The executed program, complete output and
stdout are retained. These symbolic and finite checks supplement
the complete actual-field proof; they infer no formal-group
realization. No mathematical checker failure occurred.
"""
assert old.count(before) == 1
new = old.replace(before, after)
hist = own/"notes/B99_certificate_finalization"
hist.mkdir(exist_ok=False)
(hist/"candidate.before.tex").write_text(old)
(hist/"candidate.diff").write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="candidate.before.tex", tofile=p.name)))
p.write_text(new)
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
source = own/"sources/colmez_corps_locaux.txt"
record = {
    "status": "CANDIDATE",
    "actual_utc": datetime.now(timezone.utc).isoformat(),
    "candidate": str(p), "candidate_sha256": sha(p),
    "labels": re.findall(r"\\label\{([^}]+)\}", new),
    "program": str(code), "program_sha256": sha(code),
    "output": str(out), "output_sha256": sha(out),
    "author_actual_utc": data["actual_utc"],
    "author_runtime_seconds": data["runtime_seconds"],
    "counts": data["counts"],
    "source_read": {
        "path": str(source), "sha256": sha(source),
        "scope": "Fresh complete retained original Colmez Remark3.6, Proposition3.7, Lemma3.8, Corollary3.9, Theorem3.10, Proposition3.13, and Propositions3.17/3.18 with continuation and Corollary3.19; printed14–18. The printed intermediate variable in the derivative prose of3.10 is not imported: the correct compositional variable is used. No new web opening or image inspection.",
        "dependencies": "Complete B79 arbitrary-index orientation, B97 actual-field/coefficient/terminal-span proofs, and B98 Cohen/different proofs reread."
    },
    "retention": "Pre-spacing and pre-certificate sources/diffs retained. The first spacing repair aborted before writing because its expected token count was8 rather than15; exact executed editing script/stderr retained. The mathematical checker passed on its first run.",
    "claim_scope": "Whole potentially supersingular height-two irreducible-residual character recovery from actual p³ at every e=t p(p−1), p∤t, algebraically closed residue and µp. No full least-index, mixed-comparison or reducible-residual extension."
}
(own/"outputs/B99_candidate_record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
