"""Record the actual seven-input CP36 freeze and final source-only precision."""
from pathlib import Path
import datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs=json.loads((w/'notes/checkpoint36_promoted_inputs.json').read_text());assert len(inputs)==7
for rel in inputs:assert '\\status{Candidate' not in (w/rel).read_text()
old=w/'notes/update_current36.before_final_promotions.py';new=w/'code/update_current36.py'
diff=''.join(difflib.unified_diff(old.read_text().splitlines(True),new.read_text().splitlines(True),fromfile=str(old.relative_to(w)),tofile=str(new.relative_to(w))))
p=w/'notes/update_current36.final_promotions.diff';assert not p.exists();p.write_text(diff)
r={'status':'FROZEN-FOR-BUILD','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'inputs':[{'path':rel,'sha256':sha(w/rel)} for rel in inputs],
 'source_precision':'The root actually read the complete Kleiman citation-only canonical diff and bibliography diff after independently reading original Definition6.1/Theorem6.3/Lemmas6.5--6.6. Final odd-Cartier canonical SHA7eb1824e6b39299e32be4b936a0c5ee7368ffc429af41b9cc2d3e2fd62025181; no mathematical assertion or proof altered. Prior author/root/companion proof audits remain applicable.',
 'source_read_record':'notes/CP36_Kleiman_root_source_read.json',
 'review25':'Prepared only; must actually execute at or after2026-11-20T05:50:40+00:00.',
 'archive36':'Not yet created; must follow final actual-image QA and actual review25, and cannot precede05:50:40UTC.',
 'current_table_change':'B4 current status/gate now states exact(5,20,2) index2 and the actual remaining families. Superseded necessary p5/e20 patterns are retained in the immutable earlier checkpoints, canonical proof history and dated ledger; they are no longer described as current open cases.',
 'updater_diff':str(p.relative_to(w)),'updater_sha256':sha(new)}
dest=w/'notes/checkpoint36_freeze.json';assert not dest.exists();dest.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
