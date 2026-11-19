#!/usr/bin/env python3
"""Record the performed independent audits, exact input IDs, and check scope.

Only the three small arithmetic certificates lacking a saved runtime are
rerun. Existing exhaustive and floating-point certificates are read without
rerunning them. No download is performed by this metadata program.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
INPUT = WORKSPACE / "inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv"
WHO = "GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed; part_c_algebra agent)"
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")

with INPUT.open(newline="") as fp:
    original = list(csv.DictReader(fp, delimiter="\t"))
original_by_id = {row["id"]: (index + 2, row) for index, row in enumerate(original)}

mapping = [
    ("SA22-10 (68/036-038: Th. 1, Remark, Examples, Th. 2)",
     "C-exp-log; C-qcoh", "independent algebraic re-derivation",
     "Finite polynomial exp/log identities and universal-parameter coefficient comparisons rechecked; the nil versus nilpotent ideal distinction in Examples 1 and 2 is explained in notes/part_c_input_audit.md. The units functor of a fixed algebra is distinguished from the automorphism functor of an arbitrary module."),
    ("SA22-10 (68/039, (**))", "C-qcoh", "refined statement with complete proof",
     "Ordinary actions correspond to locally nilpotent endomorphisms for every K-module. The old wording 'false for M not finitely generated' is too strong: bijectivity of the uniformly nilpotent map holds exactly when every locally nilpotent endomorphism is uniformly nilpotent; the infinite diagonal module in C-qcoh disproves necessity of finite generation."),
    ("SA22-10 (68/040-043)", "C-intertwine; C-exp-log", "independent proof and typing check",
     "Pointwise logarithms extend the intertwining equivalence to arbitrary modules and locally nilpotent maps. The displayed delta proof has coefficient -1/(i+j+1)! and ambient module Hom_K(M,N), not End_K(M). Tensor-product derivation criterion rechecked."),
    ("SA22-10 (68/044)", "C-functor-criterion; C-functor-counter; C-filtered", "independent proof and counterexamples",
     "Composition replaces addition for commuting scheme exponentials; uniform nilpotence locally on the scheme is distinguished from pointwise local nilpotence. The previously unanswered arbitrary-functor maps have exact logarithmic image/fibre criteria and explicit failures of injectivity/surjectivity."),
    ("SA22-10 (68/045-046)", "C-filtered; C-differential; C-other-autos", "independent proof and counterexamples",
     "Iterated commutators give differential order iff J^(n+1)=0. Exponentials are exactly the uniformly unipotent conormal actions. Square-zero and epsilon*d/depsilon counterexamples rechecked without Noetherian assumptions. The last order-bound sentence on 046 is correct only for differential algebra automorphisms, not arbitrary differential operators."),
    ("SA22-2 (68/019-020)", "C-rearrangement", "independent layer-cake proof",
     "Rearrangement equality iff positive superlevel sets are nested, and all weak-majorization tests, proved for finite support on every group, including uncountable discrete groups; no countability assumption used."),
    ("SA22-2 (68/017)", "C-chain-true; C-K-counter; C-literal-class; C-extension", "original-image and exact finite-certificate review",
     "Original scan017 rechecked for the two clauses labelled d, the specified two-torsion kernel, the undefined B in c, and absent completed fullness clause. The exact C4 interval instance used here has 400 certified atom pairs. No reliance on an unproved general cyclic-family assertion; the purported implication to Condition K is refuted."),
    ("SA22-2 (68/021, tassé implies prétassé)", "C-rearrangement; C-K-replacement", "independent proof",
     "The convolution maximum is at most the sorted inner product; choose an equimeasurable reflected factor attaining that inner product and use the k=1 majorization inequality for a tasse pair. This proves the retained implication."),
    ("SA22-2 (68/022, brackets)", "C-rearrangement; C-chain-true", "independent mathematical reading check",
     "For equal profiles the rearrangement equality condition forces equal aligned superlevel sets, hence f=delta_s*check(f). The bracket is a pretasse assertion, not a tasse assertion. This verifies the mathematical reading; the handwritten glyphs at022 were not independently re-decided."),
]

events = []
map_rows = []
for old_id, new_ids, event_type, outcome in mapping:
    line, old = original_by_id[old_id]  # fail if any old ID was altered
    locator = f"inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv:{line}"
    events.append([old_id, NOW, WHO, event_type,
                   f"New statement IDs: {new_ids}. Input: {locator}. {outcome}"])
    map_rows.append([old_id, locator, new_ids, outcome])
events.append(["L8", NOW, WHO, "independent refutation review",
               "C-K-counter refutes the full lead by exact C4 triple-convolution maxima 4>3 even with all positive cardinalities; C-chain-true and C-K-replacement state the surviving theorem and exact missing majorization condition."])
with (ROOT / "checks/part_c_input_events.tsv").open("w", newline="") as fp:
    out = csv.writer(fp, delimiter="\t")
    out.writerow(["statement_id", "date", "who", "type", "outcome"])
    out.writerows(events)
with (ROOT / "notes/part_c_input_id_map.tsv").open("w", newline="") as fp:
    out = csv.writer(fp, delimiter="\t")
    out.writerow(["original_statement_id", "exact_input_locator", "new_statement_ids", "outcome"])
    out.writerows(map_rows)

geometry = [
    ("A3-graph", "independent proof review and explicit repair",
     "Verified the QC-compatible-star hypothesis and replaced the shorthand smooth-sector argument by a common radial exponent c=Omega/sum(alpha_j), logarithmic radial interpolation, and bounded invertible derivative matrices. Orientation-reversing pairings and an oriented quotient are now explicit. Direct Beltrami integration includes the vertex."),
    ("A3-slit", "independent proof and original-page review",
     "Verified prime-end banks, one tip/two roots, triple normalization, quotient topology, doubled-tip quasisymmetry and removable-seam uniqueness. Reopened original scan073: the uncertain f(omega|0)=0 is not silently read as f(0)=0; the valid normalization is the boundary tip mapping to0. Milnor1991 Theorems15.9,16.6,16.7 opened with their proofs."),
    ("A3-L5", "independent scope check",
     "For actual geodesic cuts the cap identification is theta->theta0-theta, hence analytic and quasisymmetric; smooth boundary diffeomorphisms are bi-Lipschitz on compact circles. A differentiable homeomorphism with flat derivative alone does not supply this hypothesis. Arbitrary embedded-cut antiisomorphism failure is separately recorded in A1-nontoric-cut."),
    ("A3-welding", "primary-source and proof review",
     "Independently read Beurling-Ahlfors1956 Theorem1 p126 and Bishop2007 Section1 pp613-615 and Section4 pp630-632. Inserted actual LaTeX citations. Quasisymmetry is sufficient, not necessary; Bishop Theorem3 supplies nonquasisymmetric weldings. Quasiarc removability proof checked."),
    ("A4-orange-extremal", "independent geometric and exact-inequality review",
     "The locus Q0 has |z+1/2|<=sqrt(7)/2<4/3; point1 lies at distance3/2. The annulus with radii4/3,7/5 lies in the hypothesized pant and encloses exactly its cap. Inclusion gives Ext_P<=2pi/log(21/20), whereas area2pi and geodesic length32 give Ext_P>=1024/(2pi). Exact bound log(21/20)>1/21 and 1024/21>4(22/7)^2 closes the contradiction."),
    ("A4-orange-jets", "independent proof review",
     "Concentric rescaling U/lambda preserves the normalized quadratic coefficient b. The two positive-length pants have b=1/2 and5/4, so no fixed family of independently concentric cap discs can represent all pants. This is independent of the specific spherical model."),
    ("A4-grafting", "independent original-source comparison",
     "Re-read Mondello source lines3494-3550, Theorem5.4: equivariant homeomorphism preserving topological type and real-analytic diffeomorphism on each finite topological stratum. Semi-infinite cylinder exp(2pi i(s+iy)/ell) is the canonical pointed cap; cusps receive no cylinder. The all-zero decoration simplex is collapsed on both sides."),
    ("A4-action", "independent full-scope review",
     "Coordinatewise multiplication transported through the proved cap/length homeomorphism is an intrinsic continuous monoid action including mixed zero lengths. Units act freely and transitively only on positive fibres. Scaling all lengths by1-t fixes the punctured locus and gives the strong deformation retraction; no pants coordinates enter."),
]
with (ROOT / "checks/part_a34_secondary_events.tsv").open("w", newline="") as fp:
    out = csv.writer(fp, delimiter="\t")
    out.writerow(["statement_id", "date", "who", "type", "outcome"])
    for statement_id, event_type, outcome in geometry:
        out.writerow([statement_id, NOW, WHO, event_type, outcome])

# Re-run only certificates which previously recorded no elapsed time.
timed = []
for name in ["part_a1_cut_checks.py", "part_a1_bordered_checks.py", "part_c_b3_audit.py"]:
    script = ROOT / "code" / name
    started = time.perf_counter()
    proc = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                          text=True, capture_output=True, check=False)
    elapsed = time.perf_counter() - started
    transcript = ROOT / "code" / ("part_c_runtime_" + script.stem + ".txt")
    transcript.write_text(proc.stdout + proc.stderr)
    if proc.returncode:
        raise RuntimeError(f"{name} failed: {proc.returncode}; see {transcript}")
    timed.append({"script": name, "wall_seconds_including_python_startup": elapsed,
                  "returncode": proc.returncode,
                  "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
                  "transcript": str(transcript.relative_to(ROOT))})

finite = json.loads((ROOT / "code/part_c_finite_checks_output.json").read_text())
extensions = json.loads((ROOT / "code/part_c_extensions_output.json").read_text())
diagnostics = json.loads((ROOT / "code/part_a2b_checks_output.json").read_text())
times = {item["script"]: item["wall_seconds_including_python_startup"] for item in timed}
program_rows = [
    ["part_c_finite_checks.py", "Exact integers; exhaustive specified C4 and S3 systems",
     "C4:8 chains,20 symmetry atoms,400 convolution atom pairs,64 alignments,16 torsion pairs; S3:30 profiles per factor,900 rearrangement pairs",
     f"{finite['runtime_seconds']:.9f} (internal)",
     "A complete certificate for these finite examples and their counterexample values; not a classification of all finite groups."],
    ["part_c_extensions.py", "Exact integers; two specified extensions of C2",
     "Each extension:4 chains,6 symmetric atoms,36 convolution pairs,16 alignments,8 kernel pairs;2 extension systems total",
     f"{extensions['runtime_seconds']:.9f} (internal)",
     "Certifies nonuniqueness via C4 and C2xC2; not a classification of all extensions."],
    ["part_a2b_checks.py", "Float64 scipy loggamma/digamma; fixed seed22021119",
     "1209 Hessians (1200 random+9 specified),30 finite-difference Jacobians,600 monotonicity pairs",
     f"{diagnostics['runtime_seconds']:.9f} (internal)",
     "Diagnostic evidence only, with no implication of general positivity/injectivity. The analytic proof is A2b-energy and A2b-image."],
    ["part_a1_cut_checks.py", "Exact rational constants in one analytic welding",
     "2 assertions: derivative interval is strictly negative; endpoint derivatives differ",
     f"{times['part_a1_cut_checks.py']:.9f} (wall)",
     "Certifies the finite arithmetic; collar holomorphicity and failure of a pointed-disc antiisomorphism are proved in the manuscript."],
    ["part_a1_bordered_checks.py", "Exact Fraction arithmetic; one two-jet contradiction",
     "4 assertions: original jets,nonzero determinant,unique candidate coefficients,zero forced squared lengths",
     f"{times['part_a1_bordered_checks.py']:.9f} (wall)",
     "Certifies the 2x2 algebraic contradiction; does not numerically construct caps or establish the analytic range theorem."],
    ["part_c_b3_audit.py", "Exact sparse polynomial arithmetic over Z,F7,F3",
     "7 assertions:1 universal coefficient identity,2 discriminant+Cartier examples,1 Legendre coefficient,1 Legendre discriminant",
     f"{times['part_c_b3_audit.py']:.9f} (wall)",
     "Certifies arithmetic inputs only; cohomology, p-ranks and specialization are justified by the source theorems and proofs."],
]
md = ["# Program scope, finite counts, and recorded runtime", "",
      f"Recorded {NOW} by {WHO}.", "",
      "Each program listed below was actually run. Existing exhaustive checks and floating-point diagnostics were not rerun merely to increase a count. The three short scripts without saved runtimes were rerun once to measure the missing wall time. Internal times start after imports; wall times include interpreter startup, so the columns should not be used to compare algorithmic speed.", "",
      "| Program (under `code/`) | Arithmetic and scope | Complete tested count | Seconds | What the computation does not prove |",
      "|---|---|---|---:|---|"]
md.extend("| " + " | ".join(row) + " |" for row in program_rows)
md.extend(["", "## Diagnostic values", "",
           f"All {diagnostics['sample_count']} normalized sampled Hessians were positive. Minimum sampled eigenvalue: {diagnostics['worst_normalized_hessian_sample']['normalized_eigenvalues'][0]:.12g}. Maximum normalized symmetry residual: {diagnostics['max_normalized_symmetry_residual']:.12g}; maximum scaled finite-difference residual: {diagnostics['max_scaled_finite_difference_residual']:.12g}. All {diagnostics['random_strict_monotonicity_pairs']} sampled monotonicity pairings were positive, with minimum {diagnostics['minimum_monotonicity_pairing']:.12g}. No finite sample is used as a proof.", "",
           "## Source-fetch and metadata utilities", "",
           "`part_c_fetch_sources.py` made3 retrieval attempts: EGA_IV4 downloaded49,852,990 bytes in733.783871 s; HLP downloaded26,986,622 bytes in6.781591 s; Milne local fetch returned406 in4.799427 s (the primary web PDF was separately opened). `part_a2b_fetch_sources.py` made2 attempts: Ahlfors-Bers returned403 in11.651925 s (web PDF separately opened); Solynin downloaded4,227,450 bytes in31.946015 s. These are retrieval times, not mathematical tests; their original JSON outputs retain the SHA256 values and status.", "",
           "`part_c_make_metadata.py`, `part_a2b_make_metadata.py`, and this final-audit program are record-generation utilities. They are not theorem verifiers and their generated ledger-row counts are not counted as independent mathematical checks.", "",
           "The first C4 JSON-generation run reused the S3 variable `f` when serializing the C4 record. That output-only bug was fixed by retaining `c4_f`, and the mathematical certificate was rerun successfully. The attached current C4 JSON and the complete400-decomposition/64-alignment certificate are the corrected versions; no failed output is presented as a valid witness.", ""])
(ROOT / "notes/part_c_program_scope.md").write_text("\n".join(md))

report = {"date": NOW, "preserved_exact_input_ids": len(mapping),
          "input_events": len(events), "geometry_audit_events": len(geometry),
          "program_scope_rows": len(program_rows), "timed_reruns": timed,
          "status": "passed"}
text = json.dumps(report, indent=2) + "\n"
(ROOT / "code/part_c_finalize_audits_output.json").write_text(text)
(ROOT / "code/part_c_finalize_audits_output.txt").write_text(text)
print(text, end="")
