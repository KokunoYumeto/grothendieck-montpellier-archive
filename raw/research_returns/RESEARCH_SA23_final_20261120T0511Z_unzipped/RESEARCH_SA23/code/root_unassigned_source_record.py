"""Record the actual six-page visual inspection of Montpellier cote162-6."""
from pathlib import Path
import csv, datetime, hashlib, json, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_unassigned_source_record.json'
if target.exists():
    raise SystemExit('Unassigned-page inspection already recorded.')
source=root/'sources/root_montpellier162_6.pdf'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='6c820490653cd3cd3e27466d29f96c90c382bc3e18e9c18ac08cdb10efc3efe5'
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome','where'],delimiter='\t')
    writer.writerow({'statement_id':'geo-H-history','date':'2026-11-20',
      'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
      'type':'used and rechecked in this run',
      'outcome':'Followed the advertised public cote162-6 scan and individually displayed all six physical pages, including its five unassigned original pages. They concern gamma/L-factors, Weil-group and idele/torus diagrams, with no identified trace/genus-zero duplicate, date or matching enclosure. No date-gate movement.',
      'where':'notes/root_montpellier162_6_date_audit.md;logs/root_history_fetch17.json;logs/render_source_pages_root_montpellier162_6.json'})
record={'created_utc':stamp,'source_sha256':sha,'physical_pages_directly_viewed':[1,2,3,4,5,6],
        'original_pages_directly_viewed':[2,3,4,5,6],'new_events':1,'date_gate_changed':False,
        'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
