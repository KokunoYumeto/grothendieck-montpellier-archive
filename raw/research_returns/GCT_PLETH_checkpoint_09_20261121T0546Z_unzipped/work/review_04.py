from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,sys
ROOT=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,5,1,8,tzinfo=timezone.utc),now
target=ROOT/'work/REVIEW_04.json';assert not target.exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
sys.path.insert(0,str(ROOT/'work'));import build_package
rows=build_package.questions();build_package.merge_events()
openrows=[r for r in rows if not(r['state'].startswith('proved') or 'refuted' in r['state'])]
movement='''G036 changes the entire outer-five coefficient-value question to proved, through G035/T058/T059 and the complete actual stable/complement route: at most152 selected polytopes and11 variables. G037 closes the varying-outer-degree stable-hook family with one polynomial-size polytope, full support and polynomial-bit evaluation, with the exact encoding scope retained; T060 gives the corresponding first-hook kernel modules and positive basis. G034/T055/T056 completed both adjacent walls before the full outer-five synthesis. R040–R045 complete further actual matrix families, all cubic/quadratic endpoints, the entire λ2≤4,λ3≤3 ordered band, and the repeated-four tail(4,4). R046 proves actual full isotypic surjectivity for the entire tail-moment range D+t≤2n+1, upgrading the even-tail preimages to full multiplicity at their bound. A088 determines the actual invariant-base modules in every hook degree. These are changes of mathematical status and actual rank coverage. The source, archive and general varying-shape bounds remain separately open.'''
with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Formal progress review04 — '+stamp+'\n\n')
 f.write('Scheduled hourly review after review03. Movement: **YES**. Consecutive reviews without movement: **0**. Continue. Next review:21November2026,06:01:08UTC (07:01:08Europe/Berlin).\n\n'+movement+'\n\n')
 f.write('The current question table records any additional completed findings; the movement decision above already follows from the listed fully checked results. Work that remains active is not counted as completed. Every open row follows.\n\n| Row | State | Exact current gate |\n|---|---|---|\n')
 for r in openrows:f.write('| '+' | '.join(r[k].replace('|',' / ').replace('\n',' ') for k in ('id','state','finding_ids_or_current_gate'))+' |\n')
 f.write('\nCheckpoint08 is due at this same boundary. Checkpoint09 is due05:46:08UTC (06:46:08Europe/Berlin).\n')
data={'review':4,'time_utc':now.isoformat(),'time_berlin':stamp,'movement':True,'consecutive_no_movement':0,'movement_evidence':movement,'next_review_utc':'2026-11-21T06:01:08+00:00','next_checkpoint_utc':'2026-11-21T05:46:08+00:00','open_rows':openrows,'new_completed_findings':['G-034','G-035','G-036','G-037','T-055','T-056','T-058','T-059','T-060','R-040','R-041','R-042','R-043','R-044','R-045','R-046','A-088'],'refinement_not_counted':['R-038']}
target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
p=ROOT/'work/root/remaining_gates.md';s=p.read_text()
start=s.index('Review03 recorded genuine main-gate movement')
s=s[:start]+'Review04 recorded genuine main-gate movement at '+stamp+' and a zero no-movement streak. Review05 is due06:01:08UTC; Checkpoint08 is due at this review boundary, and Checkpoint09 at05:46:08UTC. This section records active work and does not invoke the stopping rule.\n'
p.write_text(s)
print(stamp,len(openrows),'open rows; movement YES; no-movement streak0')

