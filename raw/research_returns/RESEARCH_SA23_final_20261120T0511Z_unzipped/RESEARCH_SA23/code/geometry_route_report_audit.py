"""Document exact inclusion of the source-route index in the current report."""
from pathlib import Path
import csv, hashlib, json
from datetime import datetime, timezone
base=Path(__file__).resolve().parents[1]
path=base/'notes/manuscript_date_attempts.tsv'
rows=list(csv.DictReader(path.open(),delimiter='\t'))
report=(base/'RESEARCH_SA23_report.md').read_text()
heads=['## Remaining gates, attempts and next steps','### Complete manuscript-date route index','## Check-event and archive integrity']
positions=[report.index(h) for h in heads]
missing=[]
for row in rows:
 rendered='| '+' | '.join(row[k].replace('|','\\|').replace('\r',' ').replace('\n',' ') for k in ['route','evidence','failed_step','next_step','record'])+' |'
 if rendered not in report:missing.append(row['route'])
result={'utc':datetime.now(timezone.utc).isoformat(),'rows':len(rows),'exact_rows_absent_from_report':missing,'section_offsets':positions,'section_order_correct':positions==sorted(positions),'source_records_exist':all((base/p).exists() for row in rows for p in row['record'].split('; ')),'pending_routes':[row['route'] for row in rows if 'pending' in row['route']],'sha256':{str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,base/'code/write_report.py',base/'RESEARCH_SA23_report.md']},'mathematical_movement':False}
(base/'logs/geometry_route_report_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if missing or not result['section_order_correct'] or not result['source_records_exist']:raise SystemExit(1)
