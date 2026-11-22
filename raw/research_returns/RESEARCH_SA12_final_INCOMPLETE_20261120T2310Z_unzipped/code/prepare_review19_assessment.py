"""Stage the exact root comparison for review19; do not perform a timed review."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

root = Path(__file__).resolve().parents[1]
assert not (root / 'code/output/formal_review19.json').exists()
paper = (root / 'parts/D/paper_D.tex').read_text()
manifests = [
    'parts/D/post27_research/integration_manifest_finite_Morita_Frobenius_effectivity_D.json',
    'parts/B/post27_research/integration_manifest_B_bounded_period_hereditary_projective_growth.json',
    'parts/B/post27_research/integration_manifest_B_bounded_period_arbitrary_quotient_crowns.json',
    'parts/C/post27_research/integration_manifest_C_wild_field_twisted_H2.json',
    'parts/D/post27_research/integration_manifest_bounded_period_semilinear_projective_growth_D.json',
]
for folder in ['parts/B/post27_research', 'parts/C/post27_research', 'parts/D/post27_research']:
    for path in sorted((root / folder).glob('integration_manifest*.json')):
        rel = str(path.relative_to(root))
        if rel in manifests:
            continue
        m = json.loads(path.read_text())
        if '\\input{' + m['path'] + '}' in paper:
            manifests.append(rel)

verified = []
for path in manifests:
    m = json.loads((root / path).read_text())
    data = (root / m['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == m['sha256'], m['path']
    assert '\\input{' + m['path'] + '}' in paper, m['path']
    assert 'Candidate:' not in data.decode()
    audits = m['audit_scope'] if isinstance(m.get('audit_scope'), dict) else m.get('audits', m.get('audit_scope'))
    if isinstance(audits, dict):
        items = [(actor, value.get('record', value.get('path'))) for actor, value in audits.items()]
    else:
        items = [(value.get('actor', value.get('auditor')), value.get('record', value.get('path'))) for value in audits]
    assert {actor for actor, _ in items} == {'root', 'B', 'C', 'D'}
    candidate = m.get('audited_candidate_sha256', m.get('audited_candidate', {}).get('sha256'))
    audit_records = []
    for actor, audit_path in items:
        record = json.loads((root / audit_path).read_text())
        verdict = record.get('verdict', record.get('outcome', record.get('status', '')))
        assert verdict == 'PASS' or verdict.startswith('PASS: '), (actor, audit_path, verdict)
        if candidate:
            assert record['sha256'] == candidate, (actor, audit_path)
        audit_records.append(dict(actor=actor, path=audit_path, sha256=hashlib.sha256((root / audit_path).read_bytes()).hexdigest()))
    verified.append(dict(path=m['path'], sha256=m['sha256'], audit_manifest=path,
                         labels=m['labels'], audit_records=audit_records,
                         typography_delta=m.get('post_promotion_typography_delta')))

labels = {label for entry in verified for label in entry['labels']}
global_transfer = 'D:global-finite-puncture-hereditary-bounded-local-period' in labels
semilinear_crowns = 'D:bounded-period-arbitrary-quotient-projective-semilinear-crowns' in labels
global_skew_transfer = 'D:global-finite-puncture-hereditary-semilinear-local-period' in labels
form_recognition = 'D:arbitrary-quotient-symplectic-orthogonal-crowns' in labels
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = list(csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))

closure = (' The corresponding faithful projective-semilinear crown closure also allows arbitrary prescribed field images; its explicit semisimilitude criterion kills the full twisted scalar obstruction by2.' if semilinear_crowns else '')
if form_recognition:
    closure += ' The completed exact recognition covers every stated defining-characteristic symplectic and orthogonal row in unbounded rank, including the q-squared minus-orthogonal model and bounded triality/exceptional graph quotient. Type A and unitary Hermitian models are not inferred from the square-multiplier argument.'
transfer = (' The finite-puncture proper-surface transfer uses one fixed detecting curve and proves linear-in-cover-degree genus, normalized different, total jet length and completed-source budgets. It yields q^(A_S,T,B t r^2) for ordinary projective classes with bounded local geometric periods, counting each surface-cover factor once.' if global_transfer else '')
if global_skew_transfer:
    transfer += ' The completed global transfer also permits every prescribed field character, with period measured after each local field kernel. Genuine affine-curve twisted H2 vanishing, the exact downstairs scalar-lift cardinal q_x-1, deck-invariant curve references and nu*a=f cancellation supply this same degree-linear bound.'
reduction = ('One bounded-period hereditary projective counting/crown enlargement since review18: for every fixed complete excellent normal local surface and every fixed geometric Brauer-period bound B, ordinary PGL_r(F_q) classes on every degree-t punctured cover satisfy q^(A_R,B t r^2), with unrestricted scalar coefficient order. The same bound now holds for every prescribed projective-semilinear field character, including field-image order divisible by p, measuring period after field-kernel restriction. Actual coherent coefficient gerbes, simultaneous Morita effectivity, same-marking coverage, crossed determinant lists and generated fixed-determinant Isom openness complete the previously missing atlas. The ordinary faithful projective crown consequence allows arbitrary permutation quotients under its bounded residual outer index and quadratic simple-order comparison, retaining d(P).' + closure + transfer + ' All supporting lemmas, semilinear closure and any completed global transfer are grouped into this one actual reduction; none is counted again as an independent event.')
a = dict(
    assessment_actor='root', assessment_staged_utc=datetime.now(timezone.utc).isoformat(),
    formal_review_completed=False, movement=True,
    requested_status_changes=[], requested_open=['general D.1', 'general D.2(ii)', 'residual dependent L8'],
    assembled_statement_count=len(rows), central_actual_check_event_count=len(events),
    strict_main_gate_reductions=[reduction], verified_files=verified,
    all_required_proof_audits_completed=True,
    remaining_strongest_gates=[
        'Unbounded-geometric-period hereditary projective and projective-semilinear counts on arbitrary punctured covers. The constants in the new theorem may depend on B; full scalar coefficient order is already unrestricted. No bounded-degree etale splitter or bounded-rank anchor at unbounded period has been supplied.',
        'Unrestricted alternating simple-quotient multiplicities outside the proved finite-puncture minimum weighted tower-energy criterion. Unbounded natural A_N/S_N actions retain their cost. The original-divisorial theorem retains its earlier whole-orbit criterion because hereditary original-divisorial local-pair counting is not proved.',
        'General monolithic nonabelian crowns outside the precise faithful linear/projective/semilinear models, bounded residual outer index, quadratic simple-order comparison and the stated geometric period condition. The quotient generator term d(P) remains explicit, so these multiplicity estimates do not imply full profinite generation.',
        'Uncovered cross-characteristic Lie families with order divisible by the ground characteristic and outside the proved faithful model/order criteria.',
        'Full finite generation for the remaining nonprojective normal proper surface punctures and original-boundary tame quotients. Global hereditary bounds beyond the stated bounded-local-period scope and hereditary original-divisorial local pairs remain unproved.',
        'Higher-dimensional boundary cases outside finite omitted loci, controlled exceptional centres and proved projective-model full-generation reductions; unrestricted nonnormal divisorial descent remains outside the stated closures.',
        'Dependent residual L8.'
    ],
    auxiliary_not_movement=[
        'The full-order conductor, scaled separability, action Newton correction, exact Morita inverse normalization, overlap gluing and generated fixed-determinant comparison are supporting parts of this one completed projective enlargement. Arbitrary-coefficient formal effectivity and Noetherian completed-base algebraization retain their distinct scopes.',
        'The genuinely twisted H2 estimate, including the Cartan-Leray (1,1) term and exceptional-lattice quotient correction, is a supporting input. The short coherent skew cycle cancels the field-cover degree against its number of phases; neither statement is a separate movement.',
        'The ordinary and any completed semilinear crown consequences, explicit algebraic sufficient period tests and any completed numerical-curve/global transfer belong to the same reduction. No unverified named-family recognition or whole-group generation is inferred.',
        'All earlier ordinary/linear, restricted alternating, tame-projective and fixed-surface results are historical inputs. Source checks, audits, builds, typography changes, image QA, archive creation, delivery and saving are not research movement.'
    ],
    report_summary='One grouped consequence strictly reduces the main gate: bounded-geometric-period hereditary ordinary and prescribed-field projective-semilinear growth on arbitrary complete-local covers, with the stated faithful projective crown bounds.' + closure + transfer + ' Unbounded-period hereditary counts, unrestricted alternating multiplicities and full finite generation remain open.'
)
out = root / 'code/output/review19_main_assessment.json'
out.write_text(json.dumps(a, indent=2) + '\n')
print(json.dumps(dict(path=str(out.relative_to(root)), verified_files=len(verified),
                     global_transfer=global_transfer, semilinear_crowns=semilinear_crowns,
                     movement=True, formal_review_performed=False)))
