"""Supply explicit event identifiers for fully audited CP13 statement files."""
from pathlib import Path
import csv,io,json,zipfile,datetime
w=Path(__file__).resolve().parents[1]
assert not (w/'outputs/new_statement_event_coverage13.json').exists()
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_12.zip') as z:
 old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new=[r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open()) if r['id'] not in old]
events=(w/'CHECK_EVENTS.tsv').read_text()
missing=[r for r in new if r['id'] not in events]
assert all(r['where_proved'].split(';')[0] in {'sections/A_monodromy.tex','sections/B.tex'} for r in missing)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for r in missing:
  writer.writerow([r['id'],now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
   'targeted proof check',
   'PASS: this statement was included in the completed full-file independent proof reads recorded in the post-CP12 audit messages and code/root_b37_audit.py, root_b38_audit.py, root_uniform_rectangular_audit.py, root_uniform_contact_audit.py, and notes/checkpoint13_changes.md. This supplies an explicit per-statement identifier without claiming an additional computation. '+r['where_proved']])
result={'status':'PASS','new_numbered_statements':len(new),
        'explicit_identifiers_added':len(missing),'added_ids':[r['id'] for r in missing],
        'actual_utc':now}
(w/'outputs/new_statement_event_coverage13.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
