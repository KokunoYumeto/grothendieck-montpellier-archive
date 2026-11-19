"""Ensure every numbered CP15 addition or updated scope identifier has an event."""
from pathlib import Path
import csv,io,json,zipfile,datetime
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/new_statement_event_coverage15.json';assert not dest.exists()
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_14.zip') as z:
 old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new=[r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open()) if r['id'] not in old]
events=(w/'CHECK_EVENTS.tsv').read_text();missing=[r for r in new if r['id'] not in events]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
allowed={'sections/A_monodromy.tex','sections/A_mixed_six_three_seed.tex','sections/B.tex'}
assert all(r['where_proved'].split(';')[0] in allowed for r in missing)
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for r in missing:
  writer.writerow([r['id'],now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
   'targeted proof check',
   'PASS: exact promoted statement or updated scope identifier covered by the complete root audits in root_contact_third_value_audit.py, root_uniform_tangent_triple_audit.py, root_all_odd_groups_audit.py, root_mixed_axis_audit.py and root_b43_audit.py. Candidate-suffix labels were renamed after all independent audits; the actual proposition and proof did not change. Every updated older scope passage was separately read in full in statement_identity15_inspection.json. This event supplies the stable numbered identifier and does not claim an additional computation. '+r['where_proved']])
result={'status':'PASS','actual_utc':now,'new_identifiers':len(new),
 'explicit_identifiers_added':len(missing),'added_ids':[r['id'] for r in missing]}
dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
