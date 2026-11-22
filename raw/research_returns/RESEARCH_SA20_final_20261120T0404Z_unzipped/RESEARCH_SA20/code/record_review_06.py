#!/usr/bin/env python3
"""Record the sixth scheduled review with the original movement criterion."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 19, 19, 4, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('Sixth review is not due yet')
path = root / 'logs/progress_review_06.json'
if path.exists():
    raise SystemExit('Sixth review already recorded')
assert (root / 'logs/A131_root_integration.json').exists()
audits = [
    'notes/root_A131_effective_model_audit.md',
    'agents/tensor_and_finite/notes/A131/independent_audit.md',
    'notes/root_B082_universal_audit.md',
    'notes/root_D027_source_comparison_audit.md'
]
for item in audits:
    assert (root / item).exists(), item
record = {
    'review': 6, 'scheduled_utc': '2026-11-19T19:04:00Z',
    'display_time': '19 November 2026, 20:04 Europe/Berlin',
    'baseline_review': 5, 'movement': True,
    'consecutive_without_movement': 0, 'main_A1_gate_changed': True,
    'task_status_changes': [
        {'item': 'B.2(c)', 'before': 'unsettled arbitrary-ring criterion', 'after': 'proved in full arbitrary-ring generality by B.082'},
        {'item': 'D.1 literature comparison', 'before': 'original-book comparison pending', 'after': 'closed with exact original locators and D.027 counterexample/repair'}
    ],
    'qualifying_movement': [
        'A.131 supplies whole effective PL and semialgebraic concordance models and complete recursive presentations of all homotopy groups, in all unstable dimensions. A.113 supplies all definable components and the real TOP whole model in base dimension at least five. Remaining main gates are higher definable/SA comparison and low-dimensional real TOP comparison.',
        'B.082 proves a necessary-and-sufficient coefficient-syzygy criterion for every unital commutative ring inclusion, including nonflat and non-Noetherian cases, with the entire tensor kernel and cokernel identified.',
        'D.027 and the original Slodowy/Steinberg page audit complete the requested source comparison. The unrestricted subregular ordinary-versal claim is refuted by an explicit Sp4/A3 tangent-dimension calculation, and the ADE/fixed-symmetry qualification is stated.'
    ],
    'proof_audit': audits,
    'not_counted': [
        'A.130 free-abelian subgroup in three-dimensional concordance components; it does not determine the whole group.',
        'C.023 repairs a previously overbroad closed-row claim; the correction is recorded but is not separately used to satisfy the movement rule.',
        'Proper/open conic counterexample to a proposed universal Thom-stratification route; not a counterexample to maximal-locus definability.',
        'Further unsuccessful Hartshorne1968/Ogus1973 original-source searches.',
        'Builds, visual QA, audits as packaging, and checkpoint10.'
    ],
    'next_review_utc': '2026-11-19T20:04:00Z',
    'stop_authorized': False, 'actual_recorded_utc': now.isoformat()
}
path.write_text(json.dumps(record, indent=2) + '\n')
intro = '''
## Formal progress review06 — 19 November 2026, 20:04 Europe/Berlin (19:04 UTC)

Baseline: review05 at 19:04 Europe/Berlin. **Movement: YES. Consecutive reviews without movement: 0.** Two original unresolved rows are now closed, and the main A.1 problem has a proved smaller remaining gate. We do not count packaging, extra special cases or failed methods as movement.

**A.1 reduction.** A.131 gives a complete effective countable simplicial group for each entire PL and semialgebraic concordance space in every dimension over every real closed field. Finite integer simplex codes and graph equality are decidable; multiplication, inverse, faces and degeneracies are total algorithms. The full Moore quotient yields complete recursive presentations of every homotopy group. The proof retains all higher attachment data in the simplicial model. A.113 identifies its PL component presentation with every fixed o-minimal definable component group, and supplies the real TOP whole model when every base component has dimension at least five. This closes the separate effective unstable PL/SA full-space gate. It is not a finite invariant-factor evaluation or a terminating isotopy decision. Higher PL-to-SA/arbitrary-definable comparison and low-dimensional real PL-to-TOP comparison remain.

**B.2(c) closure.** B.082 supplies the criterion for every unital inclusion of commutative rings, using the determinant-colon coefficient ring, polynomial-value module, finite matrix epicness certificates, Tor groups through degree two and explicit transgressions. The proof calculates the entire tensor kernel and cokernel, proving both existence and uniqueness. Nonflat and non-Noetherian cases are included. The general ring task is no longer represented by a collection of special cases.

**D.1 source closure.** The exact original Slodowy introduction and Steinberg appendix statements suffice for all required comparisons, without relying on the later sections still marked unread. The ordinary unrestricted deformation statement fails in the explicit Sp4 subregular example: the A3 deformation tangent dimension exceeds the quotient-base dimension. D.027 proves this counterexample and gives the ADE/fixed-symmetry repair. All required source-dependent assertions now have opened original locators.

**Correction recorded without extra movement credit.** C.023 corrects the previously overbroad global-dimension formulation of projective Cohen–Macaulay duality. It gives the complete componentwise chain, including the dimension-equals-threshold endpoint injection, and a finite independently checked counterexample to the literal mixed-dimensional claim. Historical tables are retained rather than silently rewritten. A.130's three-dimensional subgroup result and the obstruction to a universal Thom-stratification argument are also retained, but neither by itself closes its original parent task.

### Every remaining scope and its current gate

| Scope | Current proved boundary and smallest unresolved case | Attempts and next attack |
|---|---|---|
| A.1(b), higher definable comparison | Whole PL/SA models and all recursive homotopy presentations are explicit. For base dimensions at least five, PL-to-SA is injective in all degrees and an isomorphism on components and pi1. The first remaining comparison is real pi2 surjectivity, already for T6; arbitrary o-minimal higher families remain separate. | Scalar straightening does not preserve two parameters. Total-space triangulation, ordinary homotopy comparison, slicewise PL contractions, infinite concatenations and the unmodified Hudson construction do not supply the required joint relative family. Attack the trivial-bundle relative Hauptvermutung or construct a class in the forgetful kernel. |
| A.1(b), low-dimensional TOP comparison | The real TOP concordance space has the complete PL model in base dimension at least five. A general weak comparison in lower dimensions has not been established. | The earlier base-four smooth-to-PL injection was rejected because its cited proof uses a dimension-restricted input. Check exact relative product-structure hypotheses on the five-dimensional cylinder with a free four-dimensional top; do not infer them from stable TOP/PL. |
| A.5, maximal proper-map bundle locus | Definable for finite or graph fibres, for every target of dimension at most two, and for triangulable maps. Remaining target dimension is at least three and fibre dimension at least two; recursion already refuted. | Properness, openness and constant fibre dimension do not force finite Thom a_f stratification, as the recorded conic example shows. Its own bundle locus is definable, so it refutes only that route. Continue uniform germ recognition or a genuine nondefinable-locus construction. |
| C.2(b), original-source comparison | The mathematical duality chain, its mixed-dimensional repair and SGA2/Hartshorne1970–1971/Speiser comparisons are proved. Hartshorne1968 Proposition4.3/Theorem7.5 and Ogus1973 Section3 remain unread in the originals. | Public publisher, exact-title, DOI, institutional, author, repository and full-text-copy searches continue to return metadata or later citations. An accessible original theorem text is required. No source request was sent and no access restriction bypassed. |
| A.6 and all other qualified completed scopes | Reconstruction with explicit conical controls/corners and the specified compact groupoid augmentation are proved; literal unrestricted alternatives have counterexamples. | Preserve the hypotheses and do not infer an unrestricted noncompact classification or identify undefined manuscript terms by assertion. No newly open mathematical row is introduced by this scope reminder. |

This review does not authorize a final return. The next review is due at 21:04 Europe/Berlin (20:04 UTC). The stopping count is reset to zero under the user's rule.

### Full current task and lead table

'''
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write(intro + (root / 'notes/outcome_table.md').read_text())
print(json.dumps(record, indent=2))
