"""Record the second scheduled movement review against the frozen first review."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

base=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc)
meta=json.loads((base/'work/RUN_METADATA.json').read_text())
start=datetime.fromisoformat(meta['started_utc'].replace('Z','+00:00'))
due=start+timedelta(hours=4)
assert now>=due, f'Review 2 is not due until {due.isoformat()}'
out=base/'work/reviews'; dest=out/'review_02.json'
assert not dest.exists(), 'Never overwrite a recorded review.'
with (base/'deliverable/QUESTIONS.tsv').open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;questions=list(reader)
current={q['id']:q for q in questions}
with (out/'review_01_questions.tsv').open(newline='') as f:
    previous={q['id']:q for q in csv.DictReader(f,delimiter='\t')}

movements=[
    dict(question='Q-MAS-STRIP-TRACE', kind='uniformity gate closed',
         reason='Review1 proved only the fixed-character strip trace and explicitly left all-character uniform estimates open. MT-M27 now proves full-adelic wide-strip trace class unconditionally; MT-M28 proves every positive-width critical strip conditionally on M, with exact kernels and uniform trace-norm sums. This closes the stated remaining analytic gate.', findings=['MT-M27','MT-M28']),
    dict(question='Q-S5-CENTRE', kind='strictly smaller sufficient arithmetic gate',
         reason='Review1 required ζ_H(1/2)≠0. MT-S504 removes central zeros inherited from ζ_F and Lη: the sufficient condition is their relative meromorphic rank-five order≤0, and the conclusion forces equality. MT-S505 also proves that order is nonnegative even under M alone. Only a positive even relative order remains for this route, with no claim it prevents automorphy.', findings=['MT-S504','MT-S505']),
    dict(question='Q-ARTIN-POS', kind='real-axis branch closed in specified S5 family',
         reason='The general and solvable positivity gates remain as in review1, but MT-S505 rules out every real-axis Artin pole in the specified Calegari S5 family under M alone. A central pole would itself trigger MT-S504 and contradict its pole. The residual branch can have only nonreal critical-line poles.', findings=['MT-S504','MT-S505']),
]
for item in movements:
    key=item['question'];item['baseline_review01']=previous[key]['state'];item['current_state']=current[key]['state']
    assert item['baseline_review01']!=item['current_state']
record=dict(review=2,scheduled_utc=due.isoformat(),actual_utc=now.isoformat(),
            elapsed_hours=(now-start).total_seconds()/3600,
            movement=True,consecutive_reviews_without_movement=0,
            decision='Continue research; two consecutive reviews without movement have not occurred.',
            next_review_utc=(due+timedelta(hours=1)).isoformat(),
            comparison='Exact comparison with all question states frozen at review1; only actual gate/status changes count.',
            movements=movements,all_question_count=len(questions),
            all_question_states_file='work/reviews/review_02_questions.tsv',
            other_checked_changes_not_needed_for_movement=[
                'MT-M29 identifies the intrinsic finite arithmetic module and multiplicity-preserving graded determinant, with independent prime/cohomological origin still open.',
                'MT-M30 closes the restricted-test-domain comparison through an unconditional ideal-valued splitting; the independent geometric equality remains.',
                'MT-M31 refutes the actual local Euler closed-range assertion and proves the exact closure replacement; local geometric identification is still open.',
                'AG-LOCAL-SPLICE repairs the exceptional local determinant conclusion while preserving the earlier exponential counterexample.',
            ],
            unchanged_main_gates=[
                'General positive-weight non-CM GL2 GRH is not supplied by the designated rank-one inputs.',
                'General Artin holomorphy and full Heilbronn positivity remain open in their stated scopes.',
                'The geometric trace identity independently of zero location remains the central Masullo-method gate.',
                'Full GUE/unrestricted correlations, ordinate independence, and optimal Nyman–Beurling derivative moment are not supplied.',
                'Independent prime-defined positive cohomology, general cycle algebraicity and integral period comparison remain separate.',
                'General P=BPP and deterministic general integer factoring are not deduced.'
            ])
dest.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
with (out/'review_02_questions.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(questions)
p=base/'work/REVIEWS.json';reviews=json.loads(p.read_text());assert len(reviews)==1;reviews.append(record);p.write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')
with (base/'work/root/ledger_history.md').open('a') as f:
    f.write(f'\n### Scheduled movement review2 — {now.isoformat()}\n\n**Movement: yes. Consecutive reviews without movement: 0. Continue.**\n\n')
    for item in movements:f.write(f"- **{item['question']}**: {item['reason']}\n")
    f.write('\nEvery question state and strongest recorded gate is frozen in `work/reviews/review_02_questions.tsv`; the dated exact baseline/current comparison is `work/reviews/review_02.json`. The next hourly review is due **2026-11-21 06:02 UTC**. New rows, packaging, and unchanged general gates were not counted as movement.\n')
print(json.dumps({k:record[k] for k in ['review','actual_utc','movement','consecutive_reviews_without_movement','next_review_utc','all_question_count']},indent=2))
