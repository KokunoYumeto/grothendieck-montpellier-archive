"""Record a due, human-reasoned movement review and its complete question snapshot.

This does not infer mathematical progress from text changes.  The controlling
agent must first supply a concrete evidence note and a yes/no movement decision.
It never creates a checkpoint or overwrites an earlier review.
"""
from pathlib import Path
import csv
import datetime as dt
import sys

root = Path(__file__).resolve().parents[1]
r = root / 'research'
d = root / 'deliverables'
n = int(sys.argv[1])
evidence = Path(sys.argv[2]).read_text().strip()
movement = sys.argv[3].lower()
assert movement in {'yes', 'no'}
start = dt.datetime.fromisoformat((r / 'RUN_START.txt').read_text().strip())
now = dt.datetime.now(dt.timezone.utc)
due = start + dt.timedelta(hours=n+2)
if now < due:
    raise SystemExit('Review not due: ' + due.isoformat())
note = r / f'movement_review_{n:02d}.md'
snapshot = r / f'movement_review_{n:02d}_questions.tsv'
if note.exists() or snapshot.exists():
    raise SystemExit('Refusing to overwrite an earlier review')
registry = r / 'movement_reviews.tsv'
prior = list(csv.DictReader(registry.open(), delimiter='\t')) if registry.exists() else []
if len(prior) != n-1:
    raise SystemExit('Review sequence mismatch')
streak = 0 if movement == 'yes' else (int(prior[-1]['consecutive_no_movement']) if prior else 0)+1
qtext = (d / 'QUESTIONS.tsv').read_text()
rows = list(csv.DictReader(qtext.splitlines(), delimiter='\t'))
def clean(x):
    return x.replace('|', r'\|').replace('\n', ' ')
table = '| Question | Current state | Strongest proved result or remaining gate |\n|---|---|---|\n'
table += ''.join('| ' + ' | '.join(clean(row[k]) for k in ('id','state','finding_ids_or_gate')) + ' |\n' for row in rows)
body = f'''## Formal movement review {n:02d}: {now.isoformat()}

Scheduled due time: {due.isoformat()}. Elapsed work: {(now-start).total_seconds()/3600:.4f} hours.
Movement decision: **{movement}**. Consecutive reviews without movement: **{streak}**.
This decision uses changes to original question status or strict reductions in
main-question gates, as required. Packaging, restatement and side results alone
are excluded from the decision.

{evidence}

The following complete snapshot includes all {len(rows)} current rows, so every
open row and its actual gate is retained. It supersedes earlier status snapshots
without deleting their historical record.

{table}
'''
note.write_text(body)
snapshot.write_text(qtext)
with (d / 'LEDGER.md').open('a') as f:
    f.write('\n\n' + body)
ledger = (d / 'LEDGER.md').read_text()
import re
ledger = re.sub(r'Last update: [^\n]+', 'Last update: '+now.isoformat()+'. User-facing calendar: Europe/Berlin, 21 November 2026.', ledger, count=1)
ledger = ledger.replace('No such review is yet due.', f'The latest completed formal review is {n:02d}; the consecutive no-movement count is {streak}.')
(d / 'LEDGER.md').write_text(ledger)
fields = ['review','scheduled_due_utc','actual_utc','movement','consecutive_no_movement','question_count','evidence_note']
with registry.open('a') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    if not prior: writer.writeheader()
    writer.writerow(dict(zip(fields,[n,due.isoformat(),now.isoformat(),movement,streak,len(rows),str(note.relative_to(root))])))
print({'review':n,'movement':movement,'consecutive_no_movement':streak,'questions':len(rows),'stop_required':streak>=2,'actual_utc':now.isoformat()})
