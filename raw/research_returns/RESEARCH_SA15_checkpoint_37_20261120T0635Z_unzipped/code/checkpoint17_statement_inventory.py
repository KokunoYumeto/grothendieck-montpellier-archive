"""Compare actual CP17 statement identities with the immutable preceding ZIP."""
from pathlib import Path
import csv,datetime,io,json,zipfile
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/checkpoint17_statement_inventory.json'
assert not dest.exists()
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_16.zip') as z:
    old={r['id']:r for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current={r['id']:r for r in csv.DictReader((w/'RESEARCH_SA15_results.csv').open())}
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events}
new=set(current)-set(old);removed=set(old)-set(current)
out={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'old_count':len(old),'current_count':len(current),'new_count':len(new),
     'removed':[old[k] for k in sorted(removed)],
     'new_without_explicit_event':[current[k] for k in sorted(new-checked)],
     'new_identifiers':sorted(new)}
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
