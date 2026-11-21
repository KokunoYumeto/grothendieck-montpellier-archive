"""Record one real-time scheduled research review with its complete row snapshot.

The researcher must supply an actual movement assessment and reasons. Merely
changing prose or regenerating the package is never classified as movement.
"""
from pathlib import Path
import csv, datetime, json, sys

root = Path(__file__).resolve().parent.parent
state_path = root / 'work/run_state.json'
state = json.loads(state_path.read_text())
now = datetime.datetime.now(datetime.timezone.utc)
due = datetime.datetime.fromisoformat(state['progress_review_utc'].replace('Z', '+00:00'))
if now < due:
    raise SystemExit('Formal review is not due until ' + due.isoformat())
assessment = sys.argv[1]
if assessment not in {'movement', 'no-movement'}:
    raise SystemExit('Use movement or no-movement, with an evidence memo path.')
memo = Path(sys.argv[2]).read_text().strip()
number = state.get('progress_review_number', 0) + 1
questions = root / 'deliverables/QUESTIONS.tsv'
snapshot = root / f'work/formal_review_{number:02d}_questions.tsv'
if snapshot.exists():
    raise SystemExit('Refusing to overwrite a previous formal-review snapshot.')
snapshot.write_bytes(questions.read_bytes())
rows = list(csv.DictReader(questions.open(), delimiter='\t'))
streak = 0 if assessment == 'movement' else state.get('consecutive_no_movement_reviews', 0) + 1

def cell(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')

out = [
    f'\n## Formal progress review {number:02d} — {now.strftime("%Y-%m-%d %H:%M:%S UTC")}\n',
    f'Scheduled time: {due.strftime("%H:%M:%S UTC")}. Assessment: **{assessment.upper()}**. '
    f'Consecutive reviews without substantive movement: **{streak}**.\n',
    memo + '\n',
    '### Every treated row at this review\n',
    'This complete snapshot includes every open row and preserves the states of resolved rows. '
    'A proved conditional reduction leaves its stated input gate open; it is not a proof of that input.\n',
    '| ID | State | Current result or gate | Next step |',
    '|---|---|---|---|',
]
for row in rows:
    out.append('| ' + ' | '.join(cell(row[k]) for k in
        ['id', 'state', 'current_gate_or_result', 'next_step']) + ' |')
next_due = due + datetime.timedelta(hours=1)
out += ['', f'The next formal review is scheduled for {next_due.strftime("%H:%M:%S UTC")}. '
        'Checkpoint creation and document preparation do not count as movement.\n']
with (root / 'deliverables/LEDGER.md').open('a') as f:
    f.write('\n'.join(out))
state.setdefault('first_progress_review_utc', state['progress_review_utc'])
state.update(progress_review_number=number, last_progress_review_utc=now.isoformat(),
             progress_review_utc=next_due.isoformat().replace('+00:00', 'Z'),
             consecutive_no_movement_reviews=streak)
state_path.write_text(json.dumps(state, indent=2) + '\n')
print(json.dumps({'review': number, 'assessment': assessment, 'no_movement_streak': streak,
                  'stop_rule_triggered': streak >= 2, 'rows': len(rows),
                  'next_review_utc': state['progress_review_utc']}))
