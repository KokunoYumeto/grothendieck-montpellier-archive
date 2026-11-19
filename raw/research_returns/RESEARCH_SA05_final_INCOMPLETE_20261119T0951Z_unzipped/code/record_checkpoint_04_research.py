"""Record actual post-checkpoint03 proof audits; this is not a formal review."""
from pathlib import Path
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
events = [
    (
        'thm:B-Brauer-characteristic',
        'targeted proof check',
        'Root read the complete written counterexample over F2 and independently checked the alpha2 injection from F2[t]/F2[t^2], E(A1)=E(F2), and the section-split derived injection from H1(Pic) to H2(Gm). The infinitely many classes have actual order two. This refutes only the literal full-Brauer assertion; the intended prime-to-p finiteness gate remains.'
    ),
    (
        'c:improved-zero-weight',
        'targeted proof check',
        'Root read the full proof and opened Rapoport-Zink Satz2.10--2.13, pp40--43, and Yamamura2026 Proposition1.5/Theorem1.6/Propositions1.7--1.8. The H0 and H1 stratum pairings remove weights2j and2j-1; projectors transfer the bound, and excellent-local-domain curve selection injects the whole R0 stalk into finite-residue local-field invariants. The source hard-Lefschetz twist-sign error is avoided and explicitly corrected.'
    ),
    (
        'c:threefold-weight-gate',
        'independent re-proof',
        'Root independently rederived the H3 threefold equivalence. Extreme maps N^3 and N^2 are already isomorphisms; the only possible weight above3 in kerN is weight4. Its disappearance is exactly injectivity of N:Gr4 to Gr2(-1), and duality makes this equivalent to isomorphism and hence full H3 weight-monodromy.'
    ),
    (
        'c:super-projective-tensors',
        'targeted proof check',
        'Root read the entire written rational projective-injective lemma and the independent D audit. Checked PBW induction, the trivial determinant and even parity of the odd tangent space, rational Harish-Chandra integration, parity-compatible mixed-tensor generation, projective/injective splitting, and projectivity for locally finite targets.'
    ),
    (
        'c:finite-super-criterion',
        'targeted proof check',
        'Root read the entire written finite criterion. Scheme-theoretic super-orbit relations, rectangular general-linear super SFT, projective lifting after fixed P0, and cancellation by the positive trace of an external algebraic parity correspondence all pass. C+(X) is explicit; neither a Chow-idempotent parity lift nor tautological parity is assumed. Root opened the exact Lehrer-Zhang and Masuoka-Shibata primary statements.'
    ),
    (
        'c:product-parity',
        'targeted proof check',
        'Root checked that products of positive marked pairs retain all narrow relations and that E times P1 has no parity projector in its codimension-two point/diagonal correspondence span. This refutes a proposed converse route; it does not by itself reduce the original classification gate.'
    ),
]
path = ROOT / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
added = 0
for identifier, kind, outcome in events:
    if not any(row['statement_id'] == identifier and row['outcome'] == outcome for row in rows):
        rows.append(dict(statement_id=identifier, date='2026-11-19T05:22:00Z',
                         who='GPT-6 Astra / root / current run', type=kind, outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

ledger = ROOT / 'PROGRESS_LEDGER.md'
entry = '''
## 05:22 UTC interim changes after checkpoint03

Checkpoint03 was saved successfully at05:05:27UTC and remains immutable. Its98-page PDF and full current deliverables passed the recorded source, statement, build and visual checks. This entry is not the formal three-hour review, which remains due05:50UTC.

B.3 now refutes the literal unqualified Brauer assertion on12:79. The constant supersingular elliptic curve y^2+y=x^3 over A1/F2 supplies an explicit infinite direct sum of order-two classes in Br(E times A1)/Br(A1). The surrounding ell≠p assertion is different and remains unresolved in its universal form. This is an actual change in the full-Brauer subtask, not a purported counterexample to prime-to-p Tate/BSD finiteness.

C.4 has a strictly smaller endpoint gate. For strictly special weight j, the R0 upper bound is0 for j=0,1 for j=1, and2j−2 for j≥2. Thus the expected endpoint is now proved for j≤2. In the first remaining normalized trait case, j=3 on a semistable projective threefold over a mixed-characteristic local field, the requested invariant-weight bound is equivalent to the H3 weight-monodromy statement. The proof removes the two highest weight rows by the H0 and polarized H1 stratum pairings, then proves the stalk-to-trait transfer. The general higher endpoint remains open.

C.1 has a finite mixed-parity criterion under the explicit sign conjecture C+(X). The proof uses projective superrepresentations to replace an invalid reductive-invariants argument and an external algebraic parity correspondence only in the final trace cancellation. This expands the proved finite-criterion scope; it does not decide its finite Chow vanishings, remove C+, or settle the general K3 transcendental exterior-power gate. The written proof has now passed root and independent audits. Extension of its coefficient-field scope is being checked separately.

Two failed approaches are retained without counting them as gate movement. A positive pair E times P1 has all narrow relations but no parity projector in the narrow correspondence ring, so narrow positivity does not imply tautological parity. The explicit Kahn-route normalization example refutes automatic principalization on one chosen entire normalization; it does not rule out a different neighbourhood and does not refute the Tate conjecture.
'''
if '## 05:22 UTC interim changes after checkpoint03' not in ledger.read_text():
    ledger.write_text(ledger.read_text() + entry)

report = ROOT / 'RESEARCH_SA05_report.md'
addition = '''
## Changes after checkpoint03

The full, unqualified relative Brauer assertion on12:79 is false. For S=A1 over F2 and E:y^2+y=x^3, the Frobenius kernel alpha2 gives F2[t]/F2[t^2] inside H1(S,E)[2]. The zero section splits the derived pushforward of Gm and injects these classes into Br(E times S)/Br(S). The proof gives actual two-torsion classes and does not use a prime-to-characteristic proper-base-change argument. The corresponding prime-to-p equivalences remain proved, while their universal finiteness remains open.

For C.4 the new R0 bound is max(0,2j−2), with the separate value1 at j=1. It proves the expected weight-j endpoint for j≤2. After normalization to middle degree, the first remaining trait case is H3 of a semistable projective threefold in mixed characteristic, where the requested endpoint is exactly equivalent to H3 weight-monodromy. The argument checks the extreme Rapoport-Zink maps through finite-strata and Picard polarizations and supplies the finite-residue trait selection needed for general stalks. The opened2026 source has an erroneous sign in a printed hard-Lefschetz twist; the paper states the correct sign and does not use that faulty formula.

For C.1 a projective-superrepresentation construction gives a finite necessary-and-sufficient list under C+(X), the existence of an algebraic cohomological parity projector. It uses neither an idempotent lift of parity in Chow nor a parity correspondence belonging to the narrow point-and-diagonal ring. The latter stronger requirement is independently disproved by the positive pair E times P1. The finite criterion does not settle arbitrary Chow vanishing or the general K3 finite-dimensionality question.

The characteristic-two Brauer and the Kahn-route normalization examples have explicit finite certificates with their code and measured runtime. The super criterion has exact small signed-tensor certificates checking rectangular identities and the difference between zero superdimension and positive parity trace; those finite tests supplement the general proofs and are not represented as proving them.
'''
if '## Changes after checkpoint03' not in report.read_text():
    report.write_text(report.read_text() + addition)

result = {'root_events': len(rows), 'new_events': added, 'interim_only': True,
          'seconds': round(time.monotonic() - started, 6)}
(ROOT / 'code/record_checkpoint_04_research_output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
