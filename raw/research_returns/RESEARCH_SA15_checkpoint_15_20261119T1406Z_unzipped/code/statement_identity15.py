"""Preserve identity of older scope remarks updated by new proved references."""
from pathlib import Path
import csv,io,zipfile,difflib,json,datetime
w=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_14.zip') as z:
 old={r['id']:r for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new={r['id']:r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open())}
added=set(new)-set(old);removed=set(old)-set(new);pairs=[]
reviewed={
 'auto:A_monodromy:29bcddd205c3':'auto:A_monodromy:9f1f96604bfd',
 'auto:A_monodromy:724365bda838':'auto:A_monodromy:b303eb6cd268',
 'auto:A_monodromy:9558ba2e7808':'auto:A_monodromy:c2d3a12ed050',
 'auto:A_monodromy:d90696dd4f6d':'auto:A_monodromy:abc2304989b0'}
assert removed==set(reviewed)
for key in sorted(removed):
 matches=sorted(((difflib.SequenceMatcher(None,old[key]['statement'],new[j]['statement']).ratio(),j) for j in added),reverse=True)
 ratio,target=matches[0]
 assert key.startswith('auto:') and target.startswith('auto:')
 assert target==reviewed[key], 'Root reviewed all four full old/current passage pairs before approving this exact map.'
 pairs.append({'old_id':key,'current_id':target,'text_similarity':ratio,
  'old_statement':old[key]['statement'],'current_statement':new[target]['statement'],
  'reason':'Existing scope remark updated with proved all-odd-degree forward references; content-derived automatic label changed.'})
assert len({r['current_id'] for r in pairs})==len(pairs)
out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'previous_total':len(old),'current_total':len(new),'additional_statements':len(new)-len(old),
 'new_identifiers':len(added),'changed_existing_identifiers':len(pairs),'remark_identity_map':pairs,
 'initial_guard_failure':'The first bookkeeping utility required identical scope-remark titles. Two titles were appropriately changed from remaining gates to proved consequences. Root read all four complete old/current pairs and approved this explicit injective identity map; the failed utility and traceback are retained.'}
dest=w/'outputs/statement_identity_checkpoint15.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
