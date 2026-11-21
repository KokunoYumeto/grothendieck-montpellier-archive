from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,sys
ROOT=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,4,1,8,tzinfo=timezone.utc),now
target=ROOT/'work/REVIEW_03.json';assert not target.exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
sys.path.insert(0,str(ROOT/'work'));import build_package
rows=build_package.questions();build_package.merge_events()
openrows=[r for r in rows if not(r['state'].startswith('proved') or 'refuted' in r['state'])]
movement='''G031 changes the complete outer-five nonvanishing question from an open central-wall/intersection gate to proved: all344 normalized deficient nodes and both stable directions are exhausted. G030/T051 finish all second-order and three-below slices, and G032 finishes every ideal order≤3. T054/G033 finish both entire central equal-row walls at unbounded order; the remaining direct coefficient gate is strictly smaller, k≥4,b≥1,1≤c≤2k−4 after completed complements and special families. T052 closes the exact charged oscillator/theta branching comparison, and T053 gives the actual incidence/Rees algebra map plus fixed positive row-weight polytopes, with the finite projectors still explicit. R033–R036 add the unit two-column family, capped linear ranges and entire second-row≤3 rank laws/cokernels. R037 gives explicit even-tail preimages, and R039 determines the higher-row width-four unit-family actual ranks. These are completed proofs and actual map computations, not packaging or restatements.'''
with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Formal progress review03 — '+stamp+'\n\n')
 f.write('Scheduled hourly review after review02. Movement: **YES**. Consecutive reviews without movement: **0**. Continue. Next review:21November2026,05:01:08UTC (06:01:08Europe/Berlin).\n\n'+movement+'\n\n')
 f.write('R038 records an explicit quartic matrix/inverse inside the known binary canonical isomorphism; it is not counted as a newly removed rank gate. T055 and the rank-three general triple formula/c1 continuation remain active research at this review and are not counted as completed movement. The varying-rank #P-description, general map and named-source/archive gates remain open.\n\n')
 f.write('Every open row and its current strongest gate follows.\n\n| Row | State | Exact current gate |\n|---|---|---|\n')
 for r in openrows:f.write('| '+' | '.join(r[k].replace('|',' / ').replace('\n',' ') for k in ('id','state','finding_ids_or_current_gate'))+' |\n')
 f.write('\nCheckpoint07 remains due04:16:08UTC (05:16:08Europe/Berlin). This review creates no extra checkpoint.\n')
data={'review':3,'time_utc':now.isoformat(),'time_berlin':stamp,'movement':True,'consecutive_no_movement':0,'movement_evidence':movement,'next_review_utc':'2026-11-21T05:01:08+00:00','next_checkpoint_utc':'2026-11-21T04:16:08+00:00','open_rows':openrows,'new_completed_findings':['G-030','G-031','G-032','G-033','T-051','T-052','T-053','T-054','R-033','R-034','R-035','R-036','R-037','R-039'],'refinement_not_counted':['R-038'],'not_counted_pending':['T-055','rank-three general triple formula and c1 continuation']}
target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
p=ROOT/'work/root/remaining_gates.md';s=p.read_text().replace('Review03 is due04:01:08UTC; Checkpoint07 is due04:16:08UTC. Review02 recorded genuine main-gate movement and a zero no-movement streak.','Review03 recorded genuine main-gate movement at '+stamp+' and a zero no-movement streak. Review04 is due05:01:08UTC; Checkpoint07 is due04:16:08UTC.');p.write_text(s)
print(stamp,len(openrows),'open rows; movement YES; no-movement streak0')
