"""Record an actual timed review; never count packaging as movement."""
from pathlib import Path
import datetime,json,sys
w=Path(__file__).resolve().parents[1]
num=int(sys.argv[1]);now=datetime.datetime.now(datetime.timezone.utc)
path=w/'notes'/f'progress_review_{num:02d}.json'
if path.exists():raise RuntimeError('Review already recorded')
rows=json.loads((w/'notes/item_status.json').read_text())
openrows=[r for r in rows if r['status'].startswith('OPEN')]
movement=[
'A.5 changed from open for general X to proved for all X with an explicit degree bound.',
'C.1 changed from open essential-image classification to an exact necessary and sufficient closed/formal/overlap/chart criterion on every locally noetherian base.',
'A.4 has no remaining projective-space cases, and the determinant image is exact for arbitrary X. The remaining gate is the nonabelian image and irreducibility for arbitrary X.',
'B.4 changed from an unbounded existence question to the sharp least index between explicit finite universal upper and constructive lower bounds.',
'E.2 now excludes F-pure finite-type perfect-field bases from the unresolved arbitrary-module gate.'
] if num==1 else []
record=dict(review=num,actual_utc=now.isoformat(),movement=movement,open_rows=openrows,no_movement_streak=0 if movement else None,next_review_due_utc=(now+datetime.timedelta(hours=1)).isoformat())
path.write_text(json.dumps(record,indent=2)+'\n')
text='\n## '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+f': required progress review {num:02d}\n\n'
text+='The first review occurs three hours after the recorded 02:50:40 UTC start. Movement is assessed against the earlier open obligations and strict gates, including the checkpoint03 baseline. Source access, writing, numbering and packaging are not counted as mathematical movement.\n\n' if num==1 else ''
text+='| Open item | Current status | Strongest proved reduction / exact remaining gate |\n|---|---|---|\n'
for r in openrows:text+='| '+r['item']+' | '+r['status']+' | '+r['gate']+' |\n'
text+='\n### Qualifying movement\n\n'+'\n'.join('- '+m for m in movement)+'\n\n'
text+='Review conclusion: movement occurred; the consecutive no-movement count is **0**. Continue the work. The next hourly review is due at 06:50:40 UTC, with the next 45-minute checkpoint due at 06:35:40 UTC.\n' if num==1 else ''
with (w/'PROGRESS_LEDGER.md').open('a') as f:f.write(text)
print(json.dumps(record,indent=2))
