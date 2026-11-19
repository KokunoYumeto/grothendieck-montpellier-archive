"""Record actual post-checkpoint04 audits without conducting an hourly review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
events = [
    ('c:covariant-polynomial-lifting',
     'Root read the complete lemma and the complete coefficient-basis and commutant proofs of Brundan–Kujawa section5, equations5.1–5.8, Lemma5.1 and Theorem5.2. Also read Hemmer–Kujawa–Nakano section2.1 and the characteristic-zero proof of Theorem4.2.6(a). Maschke and parity averaging prove exactness for finite covariant polynomial modules of fixed degree; no exactness of arbitrary mixed supergroup invariants is asserted.'),
    ('c:finite-unconditional-criterion',
     'Root read the complete 308-line proof, then its explicit modified-diagonal addition. Checked the actual augmentation projector, multiplicative-augmentation condition, high-form recursion, rational schematic super-orbit kernel over an arbitrary Weil field, homogeneous finite generators, covariant lift and rectangular-kernel transport. Bending returns every test to the narrow point/diagonal ring. The criterion removes C+ but does not prove its Chow vanishings or general K3 finite-dimensionality.'),
    ('c:finite-power-cutoff',
     'Root read the complete corollary. The maximum includes arity2 for the normalization tests, 2n+1 for the high modified diagonal, 2a(b+1) for the rectangular correspondence, and every finite form arity. Pullback to that power retracts by intersection with the extra degree-one point factors and pushforward. Finite existence and coefficient-dependent effectiveness remain distinct.'),
    ('c:surface-lowdegree-chow-unramified',
     'Root read the complete low-degree proof and opened Saito2003 Lemma3.9 with its full proof. The Galois-equivariant hard-Lefschetz retraction embeds H^r into a smooth complete intersection of dimension r<=2; its inverse is not claimed algebraic. Rapoport–Zink surface purity, trace, finite-extension descent of purity, and the homogeneous Chow-projector trace criterion yield unramified-flag independence at the original place. This additional case does not settle general C6.'),
    ('lem:B-Gm-proper-kernel',
     'Root read the full written proof and opened Bhatt–Scholze Theorem4.1(ii), Proposition4.5, Lemma4.6 and proof4.1, author pp15–17; Jaffe10.11 and its complete proof sketch, plus the statement10.8; and Stacks59.45.2/4 and69.5.1 with proofs. Perfection identifies etale Gm cohomology with localization at p; line-bundle v-descent gives R1 epsilon_*Gm=0 and the needed H2 injection only. The proper-Cech degree-two kernel embeds in a group filtered by subquotients of the finite Picard/units lattices.'),
    ('prop:B-singular-proper-Brauer-gate',
     'Root read the entire equivalence. A smooth projective alteration has finite ell-Brauer under surface Tate and torsion full H2(Gm); the preceding finite kernel makes the full localized H2 of any proper finite-type base finitely generated. Its torsion is finite. Applying the result to a proper total curve scheme gives the relative conclusion without an invalid torsion lift from Leray. This does not by itself settle nonproper singular bases.'),
    ('prop:B-integral-torsor-lattice',
     'Root read the full independent audit and the complete typeset proof. The actual torsor Cech cocycle has p-primary kernel: its equalizer section has a finite universal-homeomorphism image scheme even when the proper torsor is an algebraic space; relative Frobenius then Verschiebung kills its class. Lang–Neron gives finite section lattices, and Stacks110.74.2–3 gives torsion on the regular cover. Nilpotent and finite-open descent are valid. The relative Picard H1 consequence handles infinite-period degree torsors but does not alone remove the base H2 saturation obstruction.'),
    ('prop:B-rational-blowup-gate',
     'Root read the complete embedding argument and checked the explicit exceptional-divisor maps I_m and R_m. Their composite is the identity by the normal-bundle sign and projective-bundle pushforward. Finite-field projection centres exist after a finite extension and rational restriction/corestriction descends the conclusion. This encodes the original variety as a blow-up centre and is not counted as new main-gate movement.'),
]
path = ROOT / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
added = 0
for identifier, outcome in events:
    if not any(row['statement_id'] == identifier and row['outcome'] == outcome for row in rows):
        rows.append(dict(statement_id=identifier, date=now,
                         who='GPT-6 Astra / root / current run',
                         type='targeted proof check', outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

ledger = ROOT / 'PROGRESS_LEDGER.md'
heading = '## Post-checkpoint04 audited developments'
if heading not in ledger.read_text():
    ledger.write_text(ledger.read_text() + '''

## Post-checkpoint04 audited developments

Checkpoint04 was saved successfully at 05:50 UTC. Its immutable ZIP has 2,025,420 bytes, 219 included files and 49 unchanged-file references. The 117-page PDF passed its recorded build and 35-page visual sample; the formal review01 at 05:50:13 UTC is included. The next checkpoint is due 06:35 UTC and the next formal review 06:50 UTC. This entry is not that review.

C.1 now has a finite necessary-and-sufficient criterion without a sign conjecture or rational form of the Weil cup algebra. Bending to scalar forms on the actual augmentation kernel places the lifting problem in the semisimple covariant polynomial category. The former external-parity cancellation is no longer needed. A finite maximum power detects all the relations. The complete proof passed the owner, D and root checks, with the exact primary representation-theory proofs read. This is a genuine removal of the preceding C+ hypothesis. The actual finite Chow vanishings, including the general K3 transcendental exterior power, remain unresolved.

B.3 now also has finite generation of H1(S,A) tensor Z_(ell) for every finite-type base under surface Tate. This controls the degree obstruction in H1 of the relative Picard sheaf even for infinite-period genus-one torsors. A separate perfection/v-descent argument proves finite generation of full H2(S,Gm) tensor Z_(ell) on every proper finite-type base under the same hypothesis; hence its ell-primary torsion is finite. The nonproper base-image saturation issue is still under active investigation. The all-bases abelian-scheme finiteness equivalence itself was already counted at review01; its typeset integration is not new movement.

The surface/low-degree C.6 extension is a proved additional case. The rational-blow-up B.1 test class retains an arbitrary original variety in its centre. Neither is counted as resolution of its general gate. The programme remains incomplete.
''')

report = ROOT / 'RESEARCH_SA05_report.md'
heading = '## Changes after checkpoint04'
if heading not in report.read_text():
    report.write_text(report.read_text() + '''

## Changes after checkpoint04

The general finite C.1 criterion now has no C+ hypothesis. The proof first uses the point augmentation and the higher modified diagonal to reduce to finitely many scalar forms. Its finite orbit-ideal relations lift inside fixed-degree covariant polynomial representations, whose Schur superalgebra is semisimple in characteristic zero. A rectangular Young relation makes every representation-theoretic equality valid in Chow. The resulting finite-power cut-off has the same exact coefficient-input qualification as the construction. This does not decide rational equivalence or prove the general K3 determinant cycle vanishes. The earlier C+ criterion remains a correct, superseded sufficient method; it has not been silently deleted.

The finite-field B.3 surface gate now controls localized integral torsor groups on every base, including their non-torsion part, and full localized H2(Gm) on proper singular bases. The latter uses only the degree-two injection from etale to v-cohomology after perfection, not an unproved all-degree comparison. Jaffe's opened Theorem10.11 gives the Picard localization; Proposition10.8 is an opened statement whose source refers its proof elsewhere. The relative Picard degree obstruction is removed, while the nonproper base-image issue is being attacked separately.

The additional C.6 case covers homogeneous algebraic Chow summands built from surfaces and supplied low-degree homogeneous summands. The hard-Lefschetz retraction is used as a Galois map, with no claim that its inverse is algebraic. The B.1 blow-up construction gives explicit split maps into rational test varieties but preserves the original phantom obstruction, so it is not counted as progress toward vanishing.

Checkpoint04's save was observed to succeed; its complete current deliverables and the first formal review are preserved in that immutable archive. Its PDF has 117 pages, no overfull boxes, no unresolved citations or references, and no LaTeX/BibTeX warnings. The verification record identifies the 35 pages actually inspected. Subsequent changes in this section belong to checkpoint05.
''')

result = {'recorded_at': now, 'root_events': len(rows), 'new_events': added,
          'formal_review': False, 'seconds': round(time.monotonic() - started, 6)}
(ROOT / 'code/record_checkpoint_05_research_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
