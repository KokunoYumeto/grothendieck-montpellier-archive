from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base = Path(__file__).resolve().parents[1]
items = [
    ("B67", "B_tame_irreducible_arbitrary_index_candidate.tex",
     "verify_irreducible_arbitrary_index",
     r"""The retained exact supplement
\path{code/reduction_descent/verify_irreducible_arbitrary_index.py}
checks \(150\) varying prime-to-\(p\) indices, \(450\) field
normalizations, \(8{,}093\) direct binomial first terms, \(60\)
higher-divisibility terms, \(30{,}450\) leading-character cases,
\(38{,}689\) cubic Cartan comparisons, \(31{,}489\) single-break
and \(12{,}948\) two-break full-wild patterns. It also checks
all \(221\) two-planes in the cubic fields over
\(\mathbf F_5,\mathbf F_7,\mathbf F_{11}\), with
\(200{,}449\) exact root tests and \(806\) directly multiplied
polynomial coefficients; the middle coefficient is retained
and nonzero in these planes. The author run passed in
\(2.847146783999051\) seconds at 20:57:06 UTC.
These are finite arithmetic checks of the proof, not formal-group
or pair constructions.
""",
     "Arbitrary prime-to-p e, height-two whole potentially supersingular comparison with irreducible residual inertia: actual p² recovers finite special character. Candidate pending full audits."),
    ("B68", "B_initial_tame_sector_candidate.tex",
     "verify_initial_tame_sector",
     r"""The retained exact supplement
\path{code/reduction_descent/verify_initial_tame_sector.py}
checks all \(60\) sectors \(2\le t\le p-1\) at
\(p=5,7,11,13,17,19\). It independently computes
\(56{,}916\) Newton/high-quotient records, \(3{,}420\) low
quotients, \(113{,}832\) tangent weights, \(63{,}018\)
mixed-divisibility point-field inequalities and \(322\)
actual-target logarithm bounds, together with every stated
small-parameter and two-divisible congruence in those ranges.
The author run passed in \(2.3066381700045895\) seconds at
20:57:28 UTC. The all-prime assertion is the preceding proof
and does not follow from this finite enumeration.
""",
     "Candidate exact full-monodromy nu_min(p,t(p−1),2)=2 for p>=5 and 2<=t<=p−1, including p5/e16; depends on B67 and actual high/low quotient proofs.")
]
stamp = datetime.now(timezone.utc).isoformat()
for number, name, stem, paragraph, scope in items:
    path = base / name
    before = base / "notes" / (path.stem+".before_certificate.tex")
    assert not before.exists()
    before.write_bytes(path.read_bytes())
    text = path.read_text()
    pos = text.rfind(r"\end{remark}")
    assert pos >= 0
    text = text[:pos]+paragraph+text[pos:]
    path.write_text(text)
    output_path = base / "code" / (stem+".output.json")
    output = json.loads(output_path.read_text())
    assert output["status"] == "PASS"
    record = {
        "status": "CANDIDATE_WITH_EXACT_FINITE_SUPPLEMENT",
        "recorded_utc": stamp,
        "candidate": name,
        "candidate_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "pre_certificate": str(before.relative_to(base)),
        "labels": re.findall(r"\\label\{([^}]+)\}", text),
        "program": "code/"+stem+".py",
        "program_sha256": hashlib.sha256((base/"code"/(stem+".py")).read_bytes()).hexdigest(),
        "output": "code/"+stem+".output.json",
        "output_sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
        "author_runtime_seconds": output["runtime_seconds"],
        "author_actual_utc": output["actual_utc"],
        "counts": output["counts"],
        "scope": scope,
        "failure_history": "No failed execution occurred in this supplement. Each program retains source and traceback automatically on any later assertion failure."
    }
    (base/"outputs"/(number+"_candidate_record.json")).write_text(json.dumps(record, indent=2)+"\n")
    with (base/"CHECK_EVENTS.tsv").open("a") as f:
        f.write("\t".join([stamp, number+"-candidate", "CANDIDATE_COMPUTED",
                           scope, name+";code/"+stem+".py;code/"+stem+".output.json",
                           "Complete proof written; exact finite supplement PASS; no promotion before full root and companion audits"])+"\n")
    print(json.dumps({k:record[k] for k in ("candidate","candidate_sha256","author_runtime_seconds","labels")}))
with (base/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {stamp} — B67/B68 complete candidates\n\n"
            "B67 fully rewrites the irreducible-residual p² ramification proof for arbitrary p∤e with μp. "
            "B68 combines it with actual high and low cyclic quotients to propose exact ν_min(p,t(p−1),2)=2 for 2≤t≤p−1, including p5/e16. "
            "Both complete proofs and exact finite supplements are retained; neither is promoted before complete independent audits. "
            "The full filtered monodromy reduction and sharp lower examples are explicit in B68.\n")
