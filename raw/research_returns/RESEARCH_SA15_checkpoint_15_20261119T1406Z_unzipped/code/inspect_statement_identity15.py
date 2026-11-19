"""Print complete old/new scope passages for root identity review before mapping."""
from pathlib import Path
import csv,io,zipfile,difflib,json
w=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_14.zip') as z:
 old={r['id']:r for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new={r['id']:r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open())}
added=set(new)-set(old);removed=set(old)-set(new);out=[]
for key in sorted(removed):
 ratio,target=max((difflib.SequenceMatcher(None,old[key]['statement'],new[j]['statement']).ratio(),j) for j in added)
 out.append({'old_id':key,'current_id':target,'similarity':ratio,
  'old':old[key]['statement'],'current':new[target]['statement']})
dest=w/'outputs/statement_identity15_inspection.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
