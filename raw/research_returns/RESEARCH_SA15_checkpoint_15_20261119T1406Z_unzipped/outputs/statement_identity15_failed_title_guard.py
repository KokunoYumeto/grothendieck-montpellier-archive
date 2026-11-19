"""Preserve identity of older scope remarks updated by new proved references."""
from pathlib import Path
import csv,io,zipfile,difflib,json,datetime
w=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_14.zip') as z:
 old={r['id']:r for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new={r['id']:r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open())}
added=set(new)-set(old);removed=set(old)-set(new);pairs=[]
for key in sorted(removed):
 matches=sorted(((difflib.SequenceMatcher(None,old[key]['statement'],new[j]['statement']).ratio(),j) for j in added),reverse=True)
 ratio,target=matches[0]
 assert key.startswith('auto:') and target.startswith('auto:')
 assert old[key]['statement'].split(']',1)[0]==new[target]['statement'].split(']',1)[0]
 pairs.append({'old_id':key,'current_id':target,'text_similarity':ratio,
  'old_statement':old[key]['statement'],'current_statement':new[target]['statement'],
  'reason':'Existing scope remark updated with proved all-odd-degree forward references; content-derived automatic label changed.'})
assert len({r['current_id'] for r in pairs})==len(pairs)
out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'previous_total':len(old),'current_total':len(new),'additional_statements':len(new)-len(old),
 'new_identifiers':len(added),'changed_existing_identifiers':len(pairs),'remark_identity_map':pairs}
dest=w/'outputs/statement_identity_checkpoint15.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
