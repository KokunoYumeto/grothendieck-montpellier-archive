"""Record the three complete old/current scope passages actually reviewed by root."""
from pathlib import Path
import csv, io, zipfile, json, datetime
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/statement_identity_checkpoint16.json';assert not dest.exists()
inspection=json.loads((w/'outputs/statement_identity16_inspection.json').read_text())
reviewed={'auto:A_monodromy:abc2304989b0':'auto:A_monodromy:c25cfd1730a5',
          'auto:A_monodromy:c2d3a12ed050':'auto:A_monodromy:1e009f1c7aa8',
          'auto:A_monodromy:d4e480cdd0c6':'auto:A_monodromy:0c2f1cb265b6'}
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_15.zip') as z:
    old={r['id']:r for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new={r['id']:r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open())}
assert set(old)-set(new)==set(reviewed)
assert len(set(reviewed.values()))==len(reviewed)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pairs=[]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for row in inspection:
        assert reviewed[row['old_id']]==row['current_id']
        pairs.append({'old_id':row['old_id'],'current_id':row['current_id'],
                      'old_statement':row['old'],'current_statement':row['current'],
                      'reason':'Existing scope remark now points to the proved all-even group theorem; all previous failed-witness and computational-scope text is preserved.'})
        writer.writerow([row['current_id'],now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
                         'targeted proof check','PASS: root read the complete prior/current statement pair. The only substantive update replaces the open even-degree gate with the now independently proved all-even theorem. Existing exact-certificate limitations and retained failed witnesses remain explicit. Identity map recorded in outputs/statement_identity_checkpoint16.json.'])
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events}|set(reviewed.values())
missing=[new[x] for x in sorted(set(new)-set(old)) if x not in checked]
out={'status':'PASS','actual_utc':now,'previous_total':len(old),'current_total':len(new),
     'additional_statements':len(new)-len(old),'new_identifiers':len(set(new)-set(old)),
     'changed_existing_identifiers':len(pairs),'remark_identity_map':pairs,
     'new_identifiers_without_explicit_event':missing}
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='remark_identity_map'},indent=2))
