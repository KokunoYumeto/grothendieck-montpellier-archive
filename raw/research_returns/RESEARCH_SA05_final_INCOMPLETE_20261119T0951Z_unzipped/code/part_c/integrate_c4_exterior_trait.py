"""Insert the independently audited trait criterion without replacing old text."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[2]
section = root / "sections" / "part_c.tex"
fragment = root / "part_c" / "c4_exterior_trait_criterion.tex"
text = section.read_text()
marker = r"\begin{proposition}[The lower-endpoint gate over a trait]"
label = r"\label{c:exterior-weight-criterion}"
inserted = False
if label not in text:
    assert text.count(marker) == 1, "The insertion anchor is not unique"
    text = text.replace(marker, fragment.read_text().rstrip() + "\n\n" + marker, 1)
    section.write_text(text)
    inserted = True

rows = [
    ["c:exterior-weight-criterion",
     "Monodromy purity is equivalent to upper invariant-weight bounds on finitely many ordinary exterior powers",
     "Proved finite linear-algebra equivalence",
     "sections/part_c.tex, label c:exterior-weight-criterion",
     "Homogeneous Jordan strings; determinant weight; explicit sl2 commutator; related Taylor-Yoshida1.4",
     "12:118-120; C.4",
     "No Frobenius semisimplicity is required. Test through the largest N-string length; no novelty or universal-gate closure claimed."],
    ["c:universal-trait-weight-equivalence",
     "Universal normalized middle-degree trait invariant-weight endpoint is equivalent to weight-monodromy for all smooth projective local varieties",
     "Proved exact universal equivalence; truth of universal assertions unresolved",
     "sections/part_c.tex, label c:universal-trait-weight-equivalence",
     "c:exterior-weight-criterion; RZ2.10/(2.11); deJong6.5; trace; cohomological hard Lefschetz",
     "12:118-120; C.4",
     "For a j-fold the witness uses r<=j+1 and middle H^(rj)(X^r). Separate L_r extensions avoid a false common-model base-change step. Ordinary exterior projector has explicit Koszul sign. Trait scope retained."],
    ["c:single-endpoint-insufficient",
     "A self-dual four-dimensional formal WD module passes its single invariant endpoint but fails the exterior-square endpoint",
     "Proved formal counterexample; no geometric realization asserted",
     "sections/part_c.tex, label c:single-endpoint-insufficient",
     "Exact rational matrix and exterior calculation",
     "C.4 universal trait criterion scope",
     "K=Q2, ell=3, weights6,4,4,2, two length2 strings of centres5 and3. Exact code and JSON supplied; not a counterexample to geometric WM."],
    ["c:trait-exterior-scope",
     "Finite tensor witness and semistable extension do not prove the universal C4 endpoint or bypass general-morphism transfer",
     "Proved scope clarification; general C4 incomplete",
     "sections/part_c.tex, label c:trait-exterior-scope",
     "c:universal-trait-weight-equivalence; c:improved-zero-weight",
     "12:118-120; C.4",
     "r<=j+1 uses actual effective cohomological degree, not arbitrary Tate-twisted weight. Finite inertia may hide original-place witnesses. General f requires the separately proved curve-selection transfer."],
]
results = root / "part_c" / "results.csv"
with results.open(newline="") as f:
    existing = {row[0] for row in csv.reader(f)}
with results.open("a", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        if row[0] not in existing:
            writer.writerow(row)

stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
events = root / "part_c" / "CHECK_EVENTS.tsv"
with events.open("a", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for row in rows:
        writer.writerow([row[0], stamp, "GPT-6 Astra (OpenAI), /root/part_c",
            "targeted proof check",
            "Complete written fragment checked: graded Jordan basis, wedge witness, determinant average, explicit sl2 kernel formula, independent L_r transfers, Koszul sign, trace split and middle-degree retraction. Trait-only scope and unresolved universal assertions retained."])
        writer.writerow([row[0], stamp, "GPT-6 Astra (OpenAI), /root/part_d",
            "independent re-proof",
            "Recorded after D read actual repaired fragment in full. Separate L_r correction and elementary sl2 formula pass; all four statements passed. Mathematical/written audit only; D did not claim independent opening of Taylor-Yoshida."])
        writer.writerow([row[0], stamp, "GPT-6 Astra (OpenAI), /root",
            "independent re-proof",
            "Recorded after root's full written audit, received at clock-confirmed08:57-08:58UTC. String argument, independent extension transfer, Koszul projector and middle-degree split passed. No novelty or movement claim."])
    writer.writerow(["c:single-endpoint-insufficient", stamp,
        "GPT-6 Astra (OpenAI), /root/part_c", "computation or formal certificate",
        "Ran code/part_c/check_c4_exterior_witness.py: exact F-N relation, nondegenerate symmetric pairing, N-skew-adjointness, determinant weight16, invariant weights4/2, and exterior-square invariant weight10>8 all pass. JSON retained; formal WD example only."])
    writer.writerow(["c:exterior-weight-criterion", stamp,
        "GPT-6 Astra (OpenAI), /root/part_c", "used and rechecked in this run",
        "Opened Taylor-Yoshida original author PDF section1 and complete Lemma1.4 proof pp6-7. Related determinant/purity arguments acknowledged; no claim that the exact finite witness formulation is quoted there. Primary source and hash manifest retained."])

output = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "inserted": inserted,
    "source_fragment": str(fragment.relative_to(root)),
    "main_section": str(section.relative_to(root)),
    "labels": [row[0] for row in rows],
    "audit_scope": "Complete mathematical proof; universal trait statements remain unresolved.",
    "model_transfer_repair": "Independent L_r for each power; no ramified common-model base change.",
}
Path(__file__).with_name("integrate_c4_exterior_trait_output.json").write_text(
    json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
