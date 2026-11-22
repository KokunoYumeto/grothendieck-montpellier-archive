"""Record the third scheduled movement review against the frozen second review."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

base = Path(__file__).resolve().parents[2]
now = datetime.now(timezone.utc)
meta = json.loads((base / 'work/RUN_METADATA.json').read_text())
start = datetime.fromisoformat(meta['started_utc'].replace('Z', '+00:00'))
due = start + timedelta(hours=5)
assert now >= due, f'Review 3 is not due until {due.isoformat()}'
out = base / 'work/reviews'
dest = out / 'review_03.json'
assert not dest.exists(), 'Never overwrite a recorded review.'
with (base / 'deliverable/QUESTIONS.tsv').open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields, questions = rd.fieldnames, list(rd)
current = {q['id']: q for q in questions}
with (out / 'review_02_questions.tsv').open(newline='') as f:
    previous = {q['id']: q for q in csv.DictReader(f, delimiter='\t')}

movements = [
    dict(question='Q-S5-CENTRE', kind='strictly smaller analytic input and exact central comparison gate',
         reason='Review2 required universal M and used only the sufficient relative-order test beta-b<=0. MT-S508 needs only the off-centre real zeros of one degree-six quadratic Hecke factor, retains the known automorphic numerator order n, and proves beta>=b+n with equality exactly equivalent to the specified all-place comparison. The remaining excess is beta-b-n>=1. This is a proved refinement, not an evaluation of the unknown central orders.',
         findings=['MT-S508']),
    dict(question='Q-ARTIN-POS', kind='strictly smaller residual S5 pole configurations',
         reason='Review2 left arbitrary nonreal critical-line poles in the specified Calegari S5 branch. MT-S506 obtains critical-line pole support from A_D alone for every S5/Q extension; MT-S507 exhausts all43 monomial tests and forces explicit common zeros and relative Dedekind order>=4 times any rank-five pole order, or>=6 when the corresponding rank-four factor is nonzero. Relative order<=3 excludes the poles. General Artin positivity remains unchanged.',
         findings=['MT-S506', 'MT-S507']),
    dict(question='AG-Q13', kind='specified geometric branch resolved by actual inverse cycles',
         reason='Review2 had only a cycle/rank comparison plus denominator gate. AG-LEFSCH-CYCLES now constructs actual localized integral Chow inverse correspondences on every product-polarized elliptic product, with exact identities before killing torsion and the optimal denominator. Arbitrary varieties, polarizations and the requested theta-chain comparison remain explicit; the new theorem is independent of A/M.',
         findings=['AG-LEFSCH-SMITH', 'AG-LEFSCH-CYCLES']),
    dict(question='AG-Q36', kind='Smith ambiguity and cycle realization closed for the product family',
         reason='Review2 computed only total index and left Smith-group ambiguity and cycle realization. AG-LEFSCH-SMITH/CYCLES determine the full integral cokernel and realize the least inverse denominator by actual cycles for product-polarized elliptic curves. The stronger Fourier comparison is now separated into its exact minimal-class, rational-Chow-lift and nonzero2-torsion gates.',
         findings=['AG-LEFSCH-SMITH', 'AG-LEFSCH-CYCLES', 'AG-FOURIER-MIN', 'AG-FOURIER-CM2']),
    dict(question='AG-Q18', kind='inherited-only theorem status resolved with indexed integral consequences',
         reason='The frozen row carried K8(Z)=0 without an independently checked primary proof locator. AG-K8 now locates and checks the exact2019 theorem/final integral reduction and separates its2026 publication date. AG-K8-TWIST proves the precise twist5, cyclotomic omega^-4 and periodic p-primary consequences. These are independent classical inputs; no indexed K-group theorem is newly attributed to the adopted A endpoint, and the full LM6 gate stays open.',
         findings=['AG-K8', 'AG-K8-TWIST'])
]
for item in movements:
    key = item['question']
    item['baseline_review02'] = previous[key]['state']
    item['current_state'] = current[key]['state']
    assert item['baseline_review02'] != item['current_state']

record = dict(
    review=3, scheduled_utc=due.isoformat(), actual_utc=now.isoformat(),
    elapsed_hours=(now-start).total_seconds()/3600,
    movement=True, consecutive_reviews_without_movement=0,
    decision='Continue research; two consecutive reviews without movement have not occurred.',
    next_review_utc=(due+timedelta(hours=1)).isoformat(),
    comparison='Exact comparison with question states frozen at review2; only proved status/gate changes count. The S5 changes alone suffice for movement.',
    movements=movements, all_question_count=len(questions),
    all_question_states_file='work/reviews/review_03_questions.tsv',
    other_checked_changes_not_needed_for_movement=[
        'MT-M32-M37 repair local trace/normalization interfaces and rule out specified cutoff/compatible-indentation routes, with a trace-norm criterion for the varying-diagonal case. The independent geometric equality remains open.',
        'NT-A18/A19 prove the exact reciprocal-prime torus gate and a finite-Dirichlet-family example; these broaden the consequence catalogue rather than close the main conjectural gates.',
        'NT-A20/A21 locate Euclidean ideal-class sufficiency and prove one-point Euclidean localization with the exact extra unit-Kummer RH family.',
        'The exact Fourier obstruction is nonzero2-torsion for a concrete CM elliptic curve, while the cited very-general complex obstruction is kept separate from CM/Qbar scope.',
        'The elliptic isogeny-detection derivation has completed author and peer readings; its registered state in the frozen questions is controlling. No movement count relies on a draft or on the number of new rows.'
    ],
    unchanged_main_gates=[
        'General positive-weight non-CM GL2 GRH is not supplied by the designated rank-one inputs.',
        'General Artin holomorphy and full Heilbronn positivity remain open outside the explicitly narrowed branches.',
        'The geometric trace identity independently of zero location remains the central Masullo-method gate.',
        'Full GUE/unrestricted correlations, ordinate independence and optimal Nyman-Beurling derivative moments remain additional inputs.',
        'General theta-chain cycle comparison, independent prime-defined positive cohomology and full LM6 relation/generator normalization remain open.',
        'General P=BPP and deterministic general integer factoring are not deduced.'
    ])
dest.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
with (out / 'review_03_questions.tsv').open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(questions)
p = base / 'work/REVIEWS.json'
reviews = json.loads(p.read_text())
assert len(reviews) == 2
reviews.append(record)
p.write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + '\n')
with (base / 'work/root/ledger_history.md').open('a') as f:
    f.write(f'\n### Scheduled movement review3 — {now.isoformat()}\n\n**Movement: yes. Consecutive reviews without movement:0. Continue.**\n\n')
    for item in movements:
        f.write(f"- **{item['question']}**: {item['reason']}\n")
    f.write('\nThe complete question states are frozen in `work/reviews/review_03_questions.tsv`, with exact previous/current comparison in `work/reviews/review_03.json`. The next hourly review is due **2026-11-21 07:02 UTC**. New row counts, packaging and unchanged main gates were not counted as movement.\n')
print(json.dumps({k:record[k] for k in ['review','actual_utc','movement','consecutive_reviews_without_movement','next_review_utc','all_question_count']}, indent=2))
