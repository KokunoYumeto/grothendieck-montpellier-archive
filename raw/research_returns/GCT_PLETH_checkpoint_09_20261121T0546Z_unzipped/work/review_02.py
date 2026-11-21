from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,sys

ROOT=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,3,1,8,tzinfo=timezone.utc)
target=ROOT/'work/REVIEW_02.json'
assert not target.exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
sys.path.insert(0,str(ROOT/'work'))
import build_package
rows=build_package.questions()
openrows=[r for r in rows if not(r['state'].startswith('proved') or 'refuted' in r['state'])]
with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n## Formal progress review 02 — '+stamp+'\n\n')
 f.write('Scheduled hourly review after review01. Movement: **YES**. Consecutive reviews without movement: **0**. Continue. Next formal review:21November2026,04:01:08UTC (05:01:08Europe/Berlin).\n\n')
 f.write('Main-gate movement since review01: G027/T049 close the exact flag-model row and replace unspecified cohomology ranks by a proved saturated product, regular diagonal quotient and explicit character counts. G026 completes every order-one family in combination with T045/G021. T050 completes every two-below family, and T047/T048 evaluate the stated full stable-defect and defect-three families. G028 completes strict five-row support; G029 completes the two outer equal-row walls with all other gaps positive. Their exhaustions strictly reduce the remaining support gate to the central walls and multiple-wall intersections. R031 closes the complete outer-five actual canonical-rank row. R028–R030 remove both cofactor strips, and R032 removes five further explicit preceding-degree families from the varying-rank map gate through an actual iterated annihilator injection.\n\n')
 f.write('T051 has a completed report and independent finite checks but its full root/archive proof readings are in progress at this review. The second-order zero-twist positive conversion and the explicit oscillator charge/coinvariant transport remain active approaches. Neither is counted as proved movement here.\n\n')
 f.write('Every currently open row and its strongest recorded gate follows. The varying-rank polynomial-description, width-seven valuation, archive-definition and named-source comparison gates remain explicitly open; no absence of a mathematical relation is asserted.\n\n| Row | State | Exact current gate |\n|---|---|---|\n')
 for r in openrows:
  f.write('| '+' | '.join(r[key].replace('|',' / ').replace('\n',' ') for key in ('id','state','finding_ids_or_current_gate'))+' |\n')
 f.write('\nCheckpoint06 remains due03:31:08UTC (04:31:08Europe/Berlin); this review creates no extra checkpoint.\n')
data={'review':2,'time_utc':now.isoformat(),'time_berlin':stamp,'movement':True,'consecutive_no_movement':0,'next_review_utc':'2026-11-21T04:01:08+00:00','next_checkpoint_utc':'2026-11-21T03:31:08+00:00','open_rows':openrows,'new_completed_findings':['G-024','G-025','G-026','G-027','G-028','G-029','T-047','T-048','T-049','T-050','R-028','R-029','R-030','R-031','R-032'],'not_counted_pending':['T-051','second-order zero-twist positive formula','oscillator positive-charge coinvariant transport']}
target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(stamp,len(openrows),'open rows; movement YES; no-movement streak0')
