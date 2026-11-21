"""Execute the first dated progress review and scheduled immutable checkpoint.

The review uses already checked row closures, not new arithmetic inference.
No review timestamp or package is written before the prescribed due time.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
DUE = datetime.fromisoformat('2026-11-21T18:30:46+00:00')
OUT = BASE.parent/'KTOWER_checkpoint_04.zip'
while True:
    remaining = (DUE-datetime.now(timezone.utc)).total_seconds()
    if remaining <= 0:
        break
    time.sleep(min(30, remaining))

observed = datetime.now(timezone.utc)
assert observed >= DUE
assert not OUT.exists(), 'Never overwrite an earlier checkpoint'
review_path = BASE/'PROGRESS_REVIEWS.json'
assert not review_path.exists(), 'The first review must not replace an existing review'
with (BASE/'QUESTIONS.tsv').open(newline='') as stream:
    rows = list(csv.DictReader(stream, delimiter='\t'))
by_id = {row['id']: row for row in rows}
confirmed_closures = ['KT-Q1D-26', 'KT-Q1D-28', 'KT-Q1D-30', 'KT-Q1C-NEXT-32']
assert all(by_id[key]['state'] == 'PROVED' for key in confirmed_closures)
for key in ['KT-Q1C-NEXT-34', 'KT-Q1C-NEXT-36']:
    if by_id[key]['state'] == 'PROVED':
        confirmed_closures.append(key)
open_rows = [row for row in rows if row['state'].startswith('OPEN')]
review = {
    'number': 1,
    'scheduled_utc': DUE.isoformat(),
    'observed_utc': observed.isoformat(),
    'reviewer': '/root; GPT-6 Astra Pro; effort setting not exposed',
    'movement': True,
    'movement_basis': 'Checked open-row closures only; conservative subset listed.',
    'closed_rows': confirmed_closures,
    'excluded_from_movement': [
        'Exact odd-conormal/Selmer reformulation',
        'Finite algebra/module source audit without integral flatness',
        'Finite-support Frobenius/theta obstruction with universal gate unchanged',
        'Numerical acceleration, replays, formatting and packaging'],
    'consecutive_reviews_without_movement': 0,
    'main_all_weight_status': 'OPEN: all-weight arithmetic residual-prime elimination',
    'all_question_rows': rows,
    'open_question_rows': open_rows,
    'decision': 'Continue work; first review has checked movement.',
    'next_review_due_utc': '2026-11-21T19:30:46Z'
}
review_path.write_text(json.dumps({'reviews': [review]}, indent=2)+'\n')
ledger_path = BASE/'LEDGER.md'
ledger = ledger_path.read_text()
ledger = ledger.replace('No progress review has yet occurred.',
                        'The first progress review occurred at '+observed.isoformat()+'.')
ledger += '\n\n## Progress review 01 — '+observed.isoformat()+'\n\n'
ledger += ('Movement: YES. Checked open rows closed: '+', '.join(confirmed_closures)+
           '. The first review has no preceding no-movement review; streak=0.\n\n')
ledger += ('The all-weight Vandiver target remains open. The odd-conormal equivalence, '
           'finite-normal-module audit, finite-support geometric obstruction, numerical '
           'acceleration and packaging are explicitly excluded from movement.\n\n')
ledger += '| Open row | State | Strongest current gate |\n|---|---|---|\n'
for row in open_rows:
    values = [row['id'], row['state'], row['current_gate_or_scope']]
    ledger += '| '+' | '.join(value.replace('|', '/') for value in values)+' |\n'
ledger += ('\nAll question rows, including closed rows, are frozen in PROGRESS_REVIEWS.json. '
           'Continue; next timed review is19:30:46UTC.\n')
ledger_path.write_text(ledger)
subprocess.run([sys.executable, str(BASE/'merge_checks.py')], cwd=BASE, check=True)
result = subprocess.run([sys.executable, str(BASE/'make_package.py'), str(OUT),
                         '--not-before', '2026-11-21T18:30:46Z'],
                        cwd=BASE, check=True, text=True, capture_output=True)
receipt = json.loads(result.stdout)
(BASE.parent/'KTOWER_checkpoint_04_creation.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({'review_utc': observed.isoformat(), 'movement': True, 'package': receipt}), flush=True)
