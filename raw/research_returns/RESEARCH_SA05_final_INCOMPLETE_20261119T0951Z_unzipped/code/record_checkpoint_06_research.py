"""Preserve completed audits and attempted routes; not a formal hourly review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

root = Path(__file__).resolve().parents[1]
start = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
events = [
 ('prop:B-paired-corank', 'Root read the entire written proof, GP program and both complete outputs. An independent execution with PARI2.19.1 passed all three two-Selmer bases, rational points on every basis cover, and exact symbolic covering-map identities in 0.04028 seconds. Root opened the official ellrank and ell2cover definitions, including the distinction between Sha[2] and Sha[2]/2Sha[4], and independently read the complete proofs of Silverman IV.6.4(b), p132, and VII.2.2, p191. The local closure proof uses a nonzero formal logarithm in 4Z2, not a numerical approximation. A and B have identical dimension, global rank and entire 2-primary Sha, but local closure ranks1 and2, giving coranks1 and0. The wrapper initial false alarm was solely the announced stack-size change and is preserved in its history log.'),
 ('c:threefold-pairing-kernel', 'Root read the complete written kernel calculation and independently opened Morihiko Saito2003 Theorem0.2 and the complete sections2.1–2.7. Subtracting the shared boundary gives representatives(r,0); adjointness identifies ker gamma with the orthogonal of im rho, and the residual ambiguity is precisely K0. The primitive Gysin condition is already settled by the degree-two surface monodromy argument. The exact radical quotient and primitive criterion are valid; the remaining primitive nondegeneracy is not proved, and a representation of the old kernel is not automatically stopping-rule movement.'),
 ('c:threefold-divisor-split', 'Root read the complete written corollary, then independently opened Ito2004 Claim4.6 and its full proof, authorpp12–13. The rational divisor-image primitive subspace has a nonzero rational Gram determinant by Hodge index and splits orthogonally over Qell. It is not identified with all algebraic vectors in the restriction image. Under the separately stated all-surface Tate hypothesis, Kahn Theorem8 and all finite constant extensions exclude every root-of-unity eigenvalue from the orthogonal complement, including generalized blocks; restriction then preserves the two spectral blocks. No general Frobenius semisimplicity is assumed.'),
 ('c:threefold-pairing-scope', 'Root checked the full scope remark and independently opened Milne2002 submitted Remark4.10 with footnote3, p14, and the published Theorem3.3/Corollary3.4. Motive-category equivalence does not itself transport the geometric primitive form into the abelian polarization cone. The Q5 isotropic-line example refutes only that linear-algebra inference, not geometric weight–monodromy.'),
 ('prop:B-surface-supported-CH2', 'Root read the entire generic-point and alteration-factorization proof. The transposed diagonal terms factor through CH2 of a smooth surface alteration and CH1 of a smooth divisor alteration, with the stated codimensions. Numerical equivalence is respected by the projection formula; the degree-zero zero-cycle and Picard-zero finite-field arguments kill the intermediate numerical kernels. The generic-point criterion is equivalent to support after every field extension, not merely support over the finite base. Root requested the explicit scalar-extension injectivity step using a nondegenerate rational numerical pairing. Fu–Vial and Poonen source reopening for this new lemma is performed by the owner/D, not claimed as an additional root source read here.'),
 ('cor:B-uniruled-threefold', 'Root read the full rational-curve proof. A generic-fibre point of the generically finite rational map T×P1→X has finite residue extension and maps to the generic point of T. The rational map on P1 over that extension extends by properness, relates the two rational points, and corestriction gives the generic-point support after dividing by its finite degree, including inseparable degree. The conclusion is ordinary Chow equality; no individual Parshin theorem or universal higher-codimension gate is inferred.'),
]
path = root / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
added = 0
for identifier, outcome in events:
    if not any(r['statement_id'] == identifier and r['outcome'] == outcome for r in rows):
        rows.append(dict(statement_id=identifier, date=now,
                         who='GPT-6 Astra / root / current run',
                         type='targeted proof check', outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

# Preserve the already executed canonical-surface audit's exact text as data.
# This does not rewrite its historical timestamp or invent a new audit.
canonical = [r for r in rows if r['statement_id'] == 'cor:B-canonical-surface-gate']
(root / 'code/canonical_surface_root_audit_record.json').write_text(
    json.dumps(canonical, indent=2) + '\n')

entry = '''

## Post-review02 proofs and unsuccessful extensions

The paired arithmetic counterexample has a full independent exact PARI rerun in `code/check_paired_corank_root.py` and `part_b/output/paired_corank_root.txt`. Two products over the identical base have dimension2, Mordell–Weil rank2 and zero entire 2-primary Sha, yet arithmetic H1 coranks1 and0. Every two-Selmer basis cover has a displayed rational point and its covering map satisfies the exact curve identity. The local closure ranks are proved by formal groups. The initially overstrict wrapper flagged the harmless stack-size announcement; that run and the precisely corrected diagnostic are recorded. This does not change the remaining finite-field surface-Tate gate.

The threefold monodromy block now has an exact radical-quotient description and a primitive surface-pairing criterion. The rational primitive divisor restriction image splits unconditionally by its rational Hodge-index form. Under the separate surface-Tate hypothesis, only the transcendental restriction image remains. The full written proofs passed owner, D and root checks. Root also independently read Ito Claim4.6 and the relevant Saito proof. The universal pairing nondegeneracy remains unresolved, and the new representation is not automatically classified as qualifying progress.

The first B1 Chow gate has a complete surface-support criterion and an uniruled-threefold consequence. The hypothesis concerns zero-cycles after arbitrary field extension. The proof transposes a generic-point diagonal decomposition and factors through finite-field surface zero-cycles and divisors, where the numerical kernels vanish rationally. This establishes ordinary Chow equality in the stated class, without a Parshin or full-motive conclusion. Whether this affects the stopping-rule gate is left to the next scheduled review; an additional solved class is not automatically counted.

A new attempted B3 refinement is under active source and proof audit: remove the finite prime-to-characteristic geometric fundamental group of Yuan's abelian-fibration model by its universal finite étale cover, preserve the ample Hodge bundle through the generic isogeny, reconstruct the regular model, and use ample Lefschetz sections to obtain a geometrically simply connected surface. It is not declared proved in this entry. Its complete notes and subsequent audit state govern any later theorem.

The general C6 conductor route did not close the gap. Root opened Kato–Takeshi Saito2004 only at the introduction, pp5–7: its alternating conductor and Swan formulas do not supply the individual tame inertia codimension for an arbitrary motivic summand. Root rechecked Takeshi Saito2003 Theorem0.1 and Corollaries0.2/0.4, and the local-invariant-cycle obstruction in Esnault–Wittenberg2016 section3.1, p494. No high-dimensional mixed-characteristic purity theorem was inferred. A separate conditional correspondence-rank approach is being investigated; no exact converse or arbitrary nonalgebraic projector assertion is recorded as proved.

Root read all mathematical sections1–4 of the live25-page van Hoften–Sempliner2026 CM-Hodge preprint. Its theorem is retained as the explicitly identified current external input for abelian-type results. This is a reading of the complete argument, not an independent verification of every external theta and representation-theoretic theorem it invokes. It remains separate from the two withdrawn October2026 K3 preprints. No general geometric-positivity conclusion is imported from it.
'''
heading = '## Post-review02 proofs and unsuccessful extensions'
for filename in ['PROGRESS_LEDGER.md', 'RESEARCH_SA05_report.md', 'ROOT_CURRENT_SOURCE_RECHECK.md']:
    path = root / filename
    content = path.read_text() if path.exists() else ''
    if heading not in content:
        path.write_text(content + entry)

result = dict(recorded_at=now, root_events=len(rows), new_events=added,
              formal_review=False, seconds=round(time.monotonic()-start, 6))
(root / 'code/record_checkpoint_06_research_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
