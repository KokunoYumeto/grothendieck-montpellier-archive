"""Record one externally assessed scheduled review; never infer mathematical movement."""
from pathlib import Path
from datetime import datetime, timezone
import csv, sys

root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
due=datetime.strptime(sys.argv[2], '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
movement=sys.argv[3]=='movement'
assessment=sys.argv[4]
now=datetime.now(timezone.utc)
if now<due:
    raise SystemExit('Refusing an early scheduled review')
target=root/'provenance/PROGRESS_REVIEWS.tsv'
previous=list(csv.DictReader(target.open(),delimiter='\t')) if target.exists() else []
if any(int(r['review'])==number for r in previous):
    raise SystemExit('Refusing to overwrite an existing review')
streak=0 if movement else (int(previous[-1]['no_movement_streak'])+1 if previous else 1)
rows=list(csv.DictReader((root/'QUESTIONS.tsv').open(),delimiter='\t'))
snapshot=root/f'provenance/review_{number:02d}_questions.tsv'
if snapshot.exists():
    raise SystemExit('Refusing to overwrite review snapshot')
snapshot.write_bytes((root/'QUESTIONS.tsv').read_bytes())
stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')
record={'review':number,'scheduled_utc':due.strftime('%Y-%m-%d %H:%M:%S UTC'),
        'actual_utc':stamp,'movement':'yes' if movement else 'no',
        'no_movement_streak':streak,'actor':'/root; GPT-6 Astra Pro; effort not exposed; DEG_L_20261121',
        'assessment':assessment,'question_snapshot':str(snapshot.relative_to(root))}
with target.open('a') as f:
    writer=csv.DictWriter(f,fieldnames=record,delimiter='\t',lineterminator='\n')
    if not previous: writer.writeheader()
    writer.writerow(record)
open_rows=[r for r in rows if r['state']=='OPEN']
text=f'\n\n## {stamp} — scheduled progress review {number:02d}\n\n'
text+=f'Scheduled time: {record["scheduled_utc"]}. Actual clock verified. '
text+=assessment+'\n\n'
text+='Every currently open row is listed below, with its current proved reduction. The complete question snapshot is retained in `'+record['question_snapshot']+'`.\n\n'
text+='| Open row | State | Current gate |\n|---|---|---|\n'
for row in open_rows:
    text+='| '+row['id']+' | '+row['state']+' | '+row['current_gate_or_scope'].replace('|','/')+' |\n'
text+=f'\nMovement: {record["movement"]}. Consecutive no-movement reviews: {streak}. '
text+=('The stopping rule has been met; prepare the final package.' if streak>=2 else 'The stopping rule has not been met; continue the main research.')+'\n'
with (root/'LEDGER.md').open('a') as f:f.write(text)
print(stamp, 'review',number,'open_rows',len(open_rows),'no_movement_streak',streak)
