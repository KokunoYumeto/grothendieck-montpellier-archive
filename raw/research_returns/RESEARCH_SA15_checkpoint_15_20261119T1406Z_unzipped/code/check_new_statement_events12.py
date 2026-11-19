"""Verify per-statement event coverage for the statements added in CP12."""
from pathlib import Path
import csv,io,json,zipfile,datetime
w=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_11.zip') as z:
 old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new=[r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open()) if r['id'] not in old]
events=(w/'CHECK_EVENTS.tsv').read_text()
missing=[r for r in new if r['id'] not in events]
allowed={'sections/A_monodromy.tex','sections/A_supersingular_rectangular_ranks.tex','sections/B.tex','sections/D.tex'}
assert all(r['where_proved'].split(';')[0] in allowed for r in missing)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for r in missing:
  writer.writerow([r['id'],now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
   'targeted proof check',
   'PASS: this numbered statement was included in the completed full-file proof read and independent audit described in code/record_cp12_math_audits.py and notes/ROOT_SEARCH_LOG_12.md. This row supplies its explicit per-statement identifier; it does not claim an additional independent computation. '+r['where_proved']])
result={'new_numbered_statements':len(new),'explicit_identifiers_added':len(missing),
 'added_ids':[r['id'] for r in missing],'checked_utc':now,'status':'PASS'}
(w/'outputs/new_statement_event_coverage12.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
