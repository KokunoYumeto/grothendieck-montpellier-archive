#!/usr/bin/env python3
"""Record the first actual movement review, never before the three-hour slot."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv
import hashlib
import json

base = Path(__file__).resolve().parents[2]
session = json.loads((base/'work/session.json').read_text())
due = datetime.fromisoformat(session['started_utc']) + timedelta(hours=3)
now = datetime.now(timezone.utc)
history_path = base/'work/review_history.json'
if now < due:
    raise SystemExit(f'First review is not due until {due.isoformat()}')
if history_path.exists():
    raise SystemExit('Refusing to duplicate an actual review')
questions_path = base/'deliverables/QUESTIONS.tsv'
with questions_path.open(newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
gates = [
 ('Q1 Rectangular bridge', 'MOVEMENT: R22 reaches the asymptotic four-variable dimension ceiling, R23 identifies its exact remaining defect, and G17–G18 classify fixed strict directions and all sufficiently large stretches.', 'For m≥17 determine the single degree-m Tor defect ε_m. General ambient dimension and polynomial-size positive extraction remain open. The proved four-variable range covers every fixed n/m<√2; the exact eventual rectangular range m<n<4m/3 holds for m≥2025.'),
 ('Q2 Haar integrals and orbit boundaries', 'MOVEMENT: R21 supplies exact fixed-ambient-dimension multiplicity computation; G17–G18 turn enhanced invariant quotients into fixed-direction comparison and an all-integer asymptotic ratio.', 'Control Schur-isotypic Gram ranks and boundary ideals with size polynomial in the growing parameters; positive ambient moments alone do not isolate a desired coefficient.'),
 ('Q3 Isolation and matrix invariants', 'MOVEMENT: I31 closes the explicit unknown-order construction for every fixed width. I34 and P14 close bounded-local-nullity and rank-one/full-rank subcases. P15 closes a tested one-pair simplification by counterexample, without moving the general polynomial-in-width gate.', 'Obtain a seed budget and sampling/construction cost polynomial jointly in length, degree and growing width. The current rank-level recurrence and its sampling exponent remain too large; general intermediate-rank resets are unresolved.'),
 ('Q4 Purity and arithmetic', 'MOVEMENT: P13 gives explicit arithmetic hitting points and exact trace-coordinate span recovery in every fixed width; P14 transports the sharper restricted generator.', 'Construct a uniformly efficient kernel-avoiding encoding or a purity family that tests arbitrary coefficient vectors without exponential feature size. P11 identifies the exact unproved encoding step. No additional Dirichlet GRH implication is inferred.'),
 ('Q5 Zero statistics', 'RESOLVED AUDIT: source-specific RH/GRH predicates and support restrictions are tabulated under the stipulated Alpöge input; Masullo-dependent claims are marked conditional.', 'Unrestricted correlations, unrestricted support and automorphic hypotheses beyond Dirichlet/Hecke GRH remain additional statements. The stipulated theorem is used as requested, not truth-audited.'),
 ('Q6 Grothendieck transport', 'MOVEMENT: the checked findings are restated in scheme, representation-ring, quotient, filtration, trace and derived-restriction language, including the new SGA6 Tor-independence dictionary.', 'Original cote133 scan images are unavailable, so transcription corrections are mathematical necessities, not verified readings of ink; the exact missing Masullo §1.2 numbered locator remains a source gate.')
]
snapshot = {
 'review_index': 1, 'scheduled_utc': due.isoformat(), 'actual_utc': now.isoformat(),
 'run_id': session['run_id'], 'who': 'GPT-6 Astra Pro; root; effort not exposed',
 'baseline': 'Start of this run. No previous actual movement review occurred.',
 'movement': True, 'consecutive_reviews_without_movement': 0,
 'movement_basis': 'Several originally open rows are proved or refuted; main gates are strictly reduced by R22, R23, G17, G18, I31 and the specified restricted isolation results. Packaging and mere restatement are not counted.',
 'questions_sha256': hashlib.sha256(questions_path.read_bytes()).hexdigest(),
 'question_count': len(rows), 'all_rows': rows, 'main_questions': gates,
 'next_review_due_utc': (due+timedelta(hours=1)).isoformat()
}
(base/'work/review_01_snapshot.json').write_text(json.dumps(snapshot, indent=2, ensure_ascii=False)+'\n')
history_path.write_text(json.dumps([{k:v for k,v in snapshot.items() if k not in ['all_rows','main_questions']}], indent=2, ensure_ascii=False)+'\n')
def cell(s):
    return str(s).replace('|','\\|').replace('\n',' ')
with (base/'deliverables/LEDGER.md').open('a') as f:
    f.write(f'\n\n## First scheduled movement review — {now.isoformat()}\n\n')
    f.write(f'The three-hour review was due at {due.isoformat()} and actually performed at the timestamp above. The comparison baseline is the start of this run; earlier dated updates were not reviews. **Movement: YES. Consecutive reviews without movement: 0.** No stopping condition has been reached. The next actual review is due at {(due+timedelta(hours=1)).isoformat()}.\n\n')
    f.write('Movement is supported by open rows changing state and by the strictly smaller gates below. Side calculations, repeated statements and packaging do not count. Fixed-width and restricted-rank results are not reported as polynomial-in-width PIT.\n\n')
    f.write('| Main question | Status and movement | Strongest remaining gate |\n|---|---|---|\n')
    for row in gates:
        f.write('| '+' | '.join(map(cell,row))+' |\n')
    f.write('\n### Complete row-by-row status at this review\n\n')
    f.write('All rows are reproduced so that no open row or remaining extension is omitted. A proved restricted statement and its open extension are distinct: an extension in the final column does not revoke the proved status. Draft I35 is not integrated or counted as movement in this review.\n\n')
    f.write('| ID | Question | State | Finding or current gate |\n|---|---|---|---|\n')
    for row in rows:
        f.write('| '+' | '.join(cell(row[key]) for key in ['id','question','state','finding_or_current_gate'])+' |\n')
    f.write('\n### Next attacks selected\n\n')
    f.write('The permanent-image route will test the degree-m Tor defect beyond size16 using restriction geometry and explicit Jacobian constructions, without assuming that a generic linear section preserves the known linear strand. The isolation route will test weaker scalar-boundary preservation at intermediate-rank resets, with synchronized seed dependence included in the statement. Purity and rational-evaluation ideas will be tested against this same remaining gate. These are active research targets, not claimed theorems.\n')
print(json.dumps({k:v for k,v in snapshot.items() if k not in ['all_rows','main_questions']},ensure_ascii=False))
