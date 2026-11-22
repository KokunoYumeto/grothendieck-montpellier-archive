from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
p = own/"B_second_wild_trace_arc_candidate.tex"
code = own/"code/verify_second_wild_trace_arc.py"
out = code.with_suffix(".output.json")
data = json.loads(out.read_text())
assert data["status"] == "PASS"
old = p.read_text()
before = """or Bondarko is claimed. A standalone exact supplement
will check the weights, logarithm homogeneity and
upper recurrence, without replacing any effectivity step.
"""
after = r"""or Bondarko is claimed. The standalone exact supplement
\path{code/reduction_descent/verify_second_wild_trace_arc.py}
passed at 06:09:28.323449 UTC on 20 November 2026 in
0.15055808699980844 seconds. It checks ten symbolic
identities and 5,296 arcs at the 24 primes from five
through101, including 216 corrected choices avoiding
$N\mid A$ and 3,558 nonfaithful special actions.
It checks 100,608 intermediate-coefficient weights,
26,480 tail and $p$-coefficient cutoffs, 14,592 exact
logarithm monomials, and 44 independently inverted
multiplication coefficients through degree $p^2$
at $p=5,7,11,13$. All 24 explicit second-wild
examples and their actual-target upper recurrences
are included. The complete executed program, output
and stdout are retained. No mathematical checker
failure occurred. These computations supplement
the proof; they do not replace any effectivity step.
"""
assert old.count(before) == 1
new = old.replace(before, after)
hist = own/"notes/B100_certificate_finalization"
hist.mkdir(exist_ok=False)
(hist/"candidate.before.tex").write_text(old)
(hist/"candidate.diff").write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="candidate.before.tex", tofile=p.name)))
p.write_text(new)
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
record = {
    "status": "CANDIDATE", "actual_utc": datetime.now(timezone.utc).isoformat(),
    "candidate": str(p), "candidate_sha256": sha(p),
    "labels": re.findall(r"\\label\{([^}]+)\}", new),
    "program": str(code), "program_sha256": sha(code),
    "output": str(out), "output_sha256": sha(out),
    "author_actual_utc": data["actual_utc"],
    "author_runtime_seconds": data["runtime_seconds"], "counts": data["counts"],
    "source_read": {
        "primary": "Hopkins and Gross, Equivariant vector bundles on the Lubin–Tate moduli space (1994)",
        "url": "https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf",
        "opened_refs": ["turn904084965view0", "turn904084965view1", "turn206076777view0", "turn206076777view1", "turn206076777view2", "turn375026507view0", "turn375026507view1"],
        "scope": "Fresh indexed original equations5.3–5.8, full Proposition5.7 statement and coefficient congruence; specialization12.1–12.9 and Proposition12.10 with its complete written proof. Proposition5.7 cites Hazewinkel for integrality; no new Hazewinkel book reading is claimed. No page image or fresh Kisin/Bondarko opening.",
        "dependencies": "Complete canonical B62 arc, generic quotient, determinant and compatible-cocycle lifting proofs; full B64 actual-target coefficient/logarithm/projection/graph proof; B76 mixed, determinant and exhaustion proofs."
    },
    "claim_scope": "Actual p³ character ambiguity for every p>=5 and p(p−1)|e with e>p², allowing larger vp(e); existential mixed threshold at vp(e)=1; exact full height-two index ν_min(p,2p(p−1),2)=3 only. One whole good group versus an explicitly filtered group; no claim both are whole potentially good.",
    "retention": "Initial full candidate, precise certificate diff, exact standalone program/output/stdout, and earlier exploratory outline retained. No mathematical checker failure. No canonical or shared-file edits."
}
(own/"outputs/B100_candidate_record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
