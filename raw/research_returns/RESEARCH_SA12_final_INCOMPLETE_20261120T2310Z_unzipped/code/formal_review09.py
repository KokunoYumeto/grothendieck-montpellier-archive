"""Record the actual scheduled review09; refuses early or duplicate execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
scheduled = datetime(2026, 11, 20, 11, 10, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= scheduled, 'The scheduled review has not begun.'
out = root / 'code/output/formal_review09.json'
assert not out.exists(), 'An actual review09 record already exists.'
proofs = [
    'parts/D/D_generic_surface_finite_punctures.tex',
    'parts/B/post14_research/D_nonnormal_finite_puncture_transfer_B.tex',
    'parts/D/D_generic_surface_controlled_boundary.tex',
    'parts/B/post14_research/D_nonnormal_controlled_boundary_B.tex',
    'parts/D/D_codimension_one_projective_model.tex',
]
for rel in proofs:
    text = (root / rel).read_text()
    assert '[Candidate:' not in text and '[Proved:' in text, rel
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
review = dict(
    review_number=9, scheduled_utc=scheduled.isoformat(), actual_utc=now.isoformat(),
    preceding_review_actual_utc='2026-11-20T10:11:50.214788+00:00',
    requested_status_changes=[],
    requested_open=['general D.1', 'general D.2(ii)', 'residual dependent L8'],
    movement=True, consecutive_no_movement_reviews=0,
    strict_main_gate_reductions=[
        'Finite omitted loci in every global dimension now reduce to one fixed normal proper surface over a finite-transcendence algebraically closed extension. The map surjects onto the fundamental group of the original scheme and works simultaneously for all original covers. All-field linear H1, defining-characteristic quadratic counts, bounded-scalar projective counts, prosolvable generation and the specified simple-product bounds transfer; finite normalization extends the quantitative statements to nonnormal proper schemes.',
        'The geometric-generic surface reduction also applies to positive-dimensional boundaries when, on a fixed normal projective modification, every exceptional divisor centred inside the boundary has point image. Exact Kummer pullback preserves the original divisorial tameness. The corresponding nonnormal codimension-at-least-two statement is proved with the condition imposed on normalized components.',
        'Full finite generation is proved when a dense open of the original normal proper variety is isomorphic to an open in a projective normal model whose complement has codimension at least two. No codimension condition is required on the original side and no morphism to the projective model is required. Fujino--Sato supplies this for all complete toric varieties in arbitrary characteristic and arbitrary, possibly noninvariant, boundary. Finite normalization gives the stated nonnormal D2 class. The toric application and the one-sided precision are counted within this one new criterion, not as separate future movement.',
    ],
    auxiliary_not_movement=[
        'Exceptional arithmetic genus, inverse-Frobenius saturation, weighted core budgets, RDP contractions and the weighted chain compression are auxiliary until they supply a hereditary cover atlas or the missing nonabelian count.',
        'The superperfect-product example shows that linear H1 and H2 plus all-field quadratic counts and smallness still do not imply abstract finite generation; no geometric realization is asserted.',
        'The explicit ample Chow-slicing and RDP branch-deletion obstructions identify failed shortcuts and do not close any requested row.',
        'The newly proposed Jacobian bound for all punctured-cover exceptional chains is still under proof/source audit at this review and is not counted as a main reduction.',
        'Recognition within the earlier bounded-scalar criterion, repeated audits, finite certificates, reconstruction, packaging and PDF QA are not movement.',
    ],
    remaining_strongest_gates=[
        'Alternating simple-quotient multiplicities and the remaining simple families outside the proved linear/order and bounded-scalar/order criteria.',
        'Defining-characteristic projective linear and unitary families with unbounded natural centre.',
        'Uncovered cross-characteristic Lie families with order divisible by the ground characteristic.',
        'General monolithic nonabelian crowns with permutation, field or semilinear actions; simple-product bounds alone do not suffice.',
        'Full finite generation for the residual nonprojective normal proper surface punctures and original-boundary tame quotients.',
        'Higher-dimensional boundary reductions outside the finite-omitted-locus and controlled-exceptional-centre hypotheses, and outside the proved projective-model full-generation class; nonnormal D2 scope retained.',
        'Dependent residual L8.',
    ],
    latest_successful_checkpoint=14,
    latest_completed_visual_verification=dict(build=qa['build'], pages=qa['pages'], sha256=qa['sha256']),
    checked_proofs=[dict(path=rel,sha256=hashlib.sha256((root/rel).read_bytes()).hexdigest()) for rel in proofs],
    next_review_utc='2026-11-20T12:10:00+00:00',
    next_scheduled_checkpoint_utc='2026-11-20T11:25:00+00:00',
    note='Actual root comparison with review08 at the scheduled review09 period. All main proofs have root and independent actual-file checks, with exact fresh primary locators retained. No requested row has closed; the stopping condition is not met. A rebuilding PDF is not claimed visually verified until its separate actual image inspection.'
)
out.write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')

ledger = root / 'PROGRESS_LEDGER.md'
with ledger.open('a') as f:
    f.write('\n\n## Formal review09: 2026-11-20 11:10 UTC\n\n')
    f.write('INCOMPLETE. Actual review: '+now.isoformat()+'. Compared with review08, all A/B/C requested rows remain decided, and general D.1, D.2(ii), and residual L8 remain open. No requested row closes.\n\n')
    f.write('The main gate strictly shrank in three linked respects. Finite omitted loci in arbitrary dimension now reduce to one fixed normal proper surface detecting every original cover, and finite normalization descends the quantitative bounds to nonnormal schemes. A controlled-exceptional-centre condition extends this reduction to positive-dimensional boundaries and preserves original-divisorial tameness. Separately, the one-sided projective-model criterion proves full finite generation for varieties sharing a dense open with a projective normal model whose complement has codimension at least two. The current Fujino--Sato theorem supplies all complete toric varieties, with arbitrary noninvariant boundaries; the stated nonnormal normalization descent is also full finite generation. These are complete checked theorems, not numerical evidence.\n\n')
    f.write('Alternating and uncovered Lie-family multiplicities, unbounded projective centres, and general nonabelian crowns remain. Full generation is still open on the residual surfaces, and the remaining unrestricted-dimensional boundary cases are not covered by the new geometric hypotheses. Weighted graph and RDP refinements, abstract superperfect counterexamples, failed slicing routes, the still-audited Jacobian chain idea, recognition and packaging are not counted as additional movement.\n\n')
    f.write('Movement: YES. Consecutive no-movement reviews:0. The stopping condition is not met. Next formal review10 is12:10UTC; next scheduled immutable checkpoint15 is11:25UTC. Checkpoint14 remains the latest saved archive. Latest completed visual verification at review time is '+qa['build']+', '+str(qa['pages'])+'pages; subsequent builds require their own actual QA.\n')

p = root / 'code/assemble.py'; s = p.read_text()
summary = 'Formal review09 was completed during the scheduled11:10 UTC review period. All A/B/C rows remain decided; general D.1, D.2(ii), and residual L8 remain open. The strongest gate strictly shrank through the finite-puncture dimensional reduction, the controlled-exceptional-centre extension, and the full-generation projective-model criterion with its complete-toric application. The exact comparison and excluded auxiliary work are in code/output/formal_review09.json. No requested row closed. Consecutive no-movement reviews:0. Next formal review10 is12:10UTC and next immutable checkpoint15 is11:25UTC. Checkpoint14 is the latest saved archive. The stopping condition is not met.'
lines=s.splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith("'Formal review08 was completed"):
        lines[i]=repr(summary)+',\n'
        break
else:
    raise AssertionError('Expected review08 summary was not found.')
s=''.join(lines)
old='This is proposed main-gate movement for formal review09; the review has not been pre-recorded.'
new='This dimensional reduction was counted at formal review09 and is not additional movement after that review.'
s=s.replace(old,new)
p.write_text(s)
# Keep a later idempotent integration pass from restoring the superseded wording.
p=root/'code/integrate_post14.py'; p.write_text(p.read_text().replace(old,new))
print(json.dumps(dict(review=9,actual_utc=now.isoformat(),movement=True,consecutive_no_movement_reviews=0)))
