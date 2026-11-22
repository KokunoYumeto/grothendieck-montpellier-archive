"""Record an actual progress review from an explicitly written assessment.

The assessment records mathematical changes, never packaging as movement.
Historical review files are immutable. This script supplies the actual time.
"""
from pathlib import Path
import datetime,json,sys
w=Path(__file__).resolve().parents[1]
num=int(sys.argv[1]);assessment=json.loads(Path(sys.argv[2]).read_text())
now=datetime.datetime.now(datetime.timezone.utc)
path=w/'notes'/f'progress_review_{num:02d}.json'
if path.exists():raise RuntimeError('Review already recorded')
due=datetime.datetime.fromisoformat(assessment['due_utc'])
if now<due:raise RuntimeError('Do not predate a scheduled actual review')
previous=json.loads((w/'notes'/f'progress_review_{num-1:02d}.json').read_text())
rows=json.loads((w/'notes/item_status.json').read_text())
openrows=[r for r in rows if r['status'].startswith('OPEN')]
movement=assessment['movement']
streak=0 if movement else previous['no_movement_streak']+1
nextdue=due+datetime.timedelta(hours=1)
record=dict(review=num,actual_utc=now.isoformat(),baseline_review=num-1,
 baseline_actual_utc=previous['actual_utc'],movement=movement,
 open_rows=openrows,unresolved_refinements=assessment.get('unresolved_refinements',[]),
 no_movement_streak=streak,next_review_due_utc=nextdue.isoformat(),
 next_checkpoint_due_utc=assessment['next_checkpoint_due_utc'],
 disposition='Stop and prepare final INCOMPLETE package under the two-review rule' if streak>=2 else 'Continue')
path.write_text(json.dumps(record,indent=2)+'\n')
text='\n## '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+f': required progress review {num:02d}\n\n'
text+=f"This is an actual review against review{num-1:02d}, recorded at {previous['actual_utc']}. Source retrieval, writing, numbering and checkpoint production are not counted as mathematical movement.\n\n"
text+='| Open item | Current status | Strongest proved reduction / exact remaining gate |\n|---|---|---|\n'
for r in openrows:text+='| '+r['item']+' | '+r['status']+' | '+r['gate']+' |\n'
text+='\n### Qualifying movement since the preceding review\n\n'
text+='\n'.join('- '+m for m in movement) if movement else 'No open row changed status and no main gate became strictly smaller.'
text+='\n\n### Explicitly unresolved refinements\n\n'
text+='\n'.join('- '+m for m in record['unresolved_refinements']) or 'None beyond the open rows.'
text+=f"\n\nReview conclusion: consecutive no-movement count **{streak}**. {record['disposition']}. Next hourly review due {nextdue.isoformat()}; next checkpoint due {assessment['next_checkpoint_due_utc']}.\n"
with (w/'PROGRESS_LEDGER.md').open('a') as f:f.write(text)
print(json.dumps(record,indent=2))
