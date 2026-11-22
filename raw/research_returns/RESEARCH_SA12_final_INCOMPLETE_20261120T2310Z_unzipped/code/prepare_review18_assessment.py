"""Stage root's exact mathematical comparison; do not perform the timed review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv

root = Path(__file__).resolve().parents[1]
assert not (root / 'code/output/formal_review18.json').exists()
manifests = [
    'parts/B/post25_research/integration_manifest_B_comparable_reduction_cycles.json',
    'parts/D/post25_research/integration_manifest_intrinsic_unit_Isom_D.json',
    'parts/D/post25_research/integration_manifest_generated_fixed_determinant_unit_openness_D.json',
    'parts/C/post25_research/integration_manifest_C_finite_Frobenius_object_effectivity.json',
    'parts/C/post25_research/integration_manifest_C_arbitrary_cover_ordinary_growth.json',
    'parts/D/post25_research/integration_manifest_arbitrary_quotient_linear_crowns_D.json',
    'parts/C/post25_research/integration_manifest_C_iterated_wreath_alternating.json',
    'parts/B/post25_research/integration_manifest_B_wild_field_scalar_determinants.json',
    'parts/D/post25_research/integration_manifest_arbitrary_cover_semilinear_growth_D.json',
    'parts/D/post26_research/integration_manifest_arbitrary_quotient_semilinear_crowns_D.json',
]
optional = root / 'parts/C/post26_research/integration_manifest_C_nonnatural_alternating_models.json'
recognition = optional.exists()
if recognition:
    manifests.append(str(optional.relative_to(root)))
snc_manifest = root / 'parts/D/post26_research/integration_manifest_controlled_SNC_refinement_root.json'
snc = snc_manifest.exists()
if snc:
    manifests.append(str(snc_manifest.relative_to(root)))
verified = []
paper = (root / 'parts/D/paper_D.tex').read_text()
for path in manifests:
    m = json.loads((root / path).read_text())
    data = (root / m['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == m['sha256'], m['path']
    assert '\\input{' + m['path'] + '}' in paper, m['path']
    assert 'Candidate:' not in data.decode()
    audits = m.get('audits', m.get('audit_scope'))
    if isinstance(audits, dict):
        items = [(actor, a.get('record', a.get('path'))) for actor, a in audits.items()]
    else:
        items = []
        for a in audits:
            if isinstance(a, str):
                record = json.loads((root / a).read_text())
                items.append((record.get('actor', record.get('auditor')), a))
            else:
                items.append((a.get('actor', a.get('auditor')), a.get('record', a.get('path'))))
    assert {actor for actor, _ in items} == {'root', 'B', 'C', 'D'}
    for actor, audit_path in items:
        record = json.loads((root / audit_path).read_text())
        verdict = record.get('verdict', record.get('outcome', record.get('status', '')))
        assert verdict == 'PASS' or verdict.startswith('PASS: '), (actor, audit_path, verdict)
    verified.append(dict(path=m['path'], sha256=m['sha256'], audit_manifest=path, labels=m['labels']))

with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = list(csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
recognition_text = (' The completed recognition additionally allows every non-natural alternating-socle primitive action: non-natural subset/product models have squared matrix rank at most4N, while the small-order branch uses the checked alternating automorphism model. Natural A_N/S_N actions remain charged.' if recognition else '')
a = dict(
    assessment_actor='root', assessment_staged_utc=datetime.now(timezone.utc).isoformat(),
    formal_review_completed=False, movement=True,
    requested_status_changes=[],
    requested_open=['general D.1', 'general D.2(ii)', 'residual dependent L8'],
    assembled_statement_count=len(rows), central_actual_check_event_count=len(events),
    strict_main_gate_reductions=[
        'One arbitrary-cover hereditary counting/crown reduction since review17: for every fixed complete excellent normal local surface, ordinary GL_r(F_q) and prescribed-field-character semilinear classes on every degree-t punctured cover satisfy q^(A_R t r^2), without quotient-cover, resolution-extension or field-order tameness assumptions. The concrete faithful linear and semilinear crown consequences now allow arbitrary transitive permutation/outer quotients on all such germs, retaining the bounded residual outer index, quadratic simple-order comparison and explicit d(P). This strictly extends the former one-smooth-exceptional-curve/radially-tame crown gate. Geometric, scalar, object-family and counting prerequisites, together with the semilinear-crown closure, are grouped into this one actual consequence.',
        'One finite-puncture restricted-alternating enlargement since review17: replace the squared sizes of uncontrolled whole local orbits by minimum weighted imprimitive-tower energy sum(T_i m_i^2) over unrestricted levels. Exact nonsimple Shapiro on actual degree-T_i punctured covers counts modelled levels at factorial order, including arbitrary-height towers of the qualifying primitive models. The one-level unrestricted certificate recovers the previous square-sum criterion. Finite catalogues, whole-local type transfer, disconnected covers and the stated dimensional/finite-normalization closures belong to this one enlargement.' + recognition_text
    ],
    verified_files=verified, all_required_proof_audits_completed=True,
    remaining_strongest_gates=[
        'Unrestricted alternating simple-quotient multiplicities outside the enlarged matrix/tower criterion. In the finite-puncture scope only uncontrolled weighted tower energy is charged; the existing original-divisorial normal proper surface theorem still has its whole-orbit criterion, because no hereditary original-divisorial local-pair count has been proved.' + recognition_text,
        'Hereditary PROJECTIVE or twisted-gerbe representation counts with constants linear in arbitrary finite-cover degree remain unproved. The ordinary and prescribed-field-character semilinear counts are proved and are no longer missing atlas gates. Twisted determinant enumeration, uniformly controlled gerbe/anchor generation and an actual root-invariant Hom/degree presentation remain outside those proofs.',
        'General monolithic nonabelian crowns outside the precise faithful linear/semilinear models, bounded residual outer index and quadratic order comparison, or the earlier radially tame projective hypotheses. The explicit quotient generator term d(P) remains unbounded without additional input; no full profinite generation follows from these multiplicity estimates alone.',
        'Uncovered cross-characteristic Lie families with order divisible by the ground characteristic and outside the proved linear/order and projective/order criteria.',
        'Full finite generation for the remaining nonprojective normal proper surface punctures and original-boundary tame quotients. Counts of selected simple products do not decide all crowns or the full group.',
        'Higher-dimensional boundary cases outside finite omitted loci, controlled exceptional centres and proved projective-model full-generation reductions; unrestricted nonnormal divisorial descent remains outside the stated closures.',
        'Dependent residual L8.'
    ],
    auxiliary_not_movement=[
        'Comparable cycles, integral unit jets, finite Frobenius object effectivity, weak-cycle generation and fixed-determinant openness are supporting parts of the one completed ordinary/hereditary reduction. Their exact all-ring formal and Noetherian algebraization scopes remain distinct.',
        'The direct twisted-scalar graph/Jacobian estimate, equivariant same-model cycles, short Frobenius cycle cancellation and faithful semilinear crown corollary are parts of that same counting/crown reduction, not separate movements. No nonexistent all-characteristics local H1 bound or ordinary-to-projective inference is used.',
        'The wreath count, minimum tower-energy criterion and any completed primitive-action recognition are one restricted-alternating enlargement. No hereditary extension to original-divisorial local pairs or unrestricted natural alternating action is inferred.',
        ('The completed controlled SNC refinement gives O_R(t) centres, components, nodes and genera, with all specified full nonreduced-cycle scalar budgets and actual ordinary-family data inherited from the old comparable cycles. It also proves the stated Jacobian inequality. This is an auxiliary geometric clarification; it does not supply twisted anchors or bound unsigned adjacent-coefficient products.' if snc else 'Pulling back the old comparable cycles through a blowup preserves their scalar budgets but does not supply the twisted parameter theorem or bound component/node costs.') + ' The separate projective constant/anchor analysis identifies these unproved obligations. No pending anchor candidate is counted.',
        'All earlier projective growth, geometric exclusions and restricted crowns are historical inputs. Source checks, audits, builds, image QA, archive creation, delivery and saving are not research movement.'
    ],
    report_summary='Two grouped consequences strictly reduce the main gate: arbitrary-cover ordinary and prescribed-field-character semilinear counting with the stated faithful crown bounds, and the finite-puncture alternating criterion using weighted imprimitive-tower energy.' + recognition_text + ' The ordinary atlas is now proved; arbitrary-cover projective counts, unrestricted alternating multiplicities and full finite generation remain open.'
)
out = root / 'code/output/review18_main_assessment.json'
out.write_text(json.dumps(a, indent=2) + '\n')
print(json.dumps(dict(path=str(out.relative_to(root)), verified_files=len(verified),
                     recognition_included=recognition, movement=True, formal_review_performed=False)))
