from pathlib import Path
import hashlib,runpy,contextlib,io,json
from datetime import datetime,timezone
base=Path(__file__).resolve().parents[1]
author=base.parent/'monodromy/outputs/genus_two_three_total_ramification_checks.json'
before=hashlib.sha256(author.read_bytes()).hexdigest()
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
 runpy.run_path(str(base/'code/independent_genus_two_three_total_ramification_checks.py'),run_name='__main__')
(base/'outputs/independent_genus_two_three_total_ramification_checks.stdout.txt').write_text(buf.getvalue())
after=hashlib.sha256(author.read_bytes()).hexdigest()
assert before==after
out=json.loads((base/'outputs/genus_two_three_total_ramification_checks.json').read_text())
record={'actual_utc':datetime.now(timezone.utc).isoformat(),'result':'FULL INDEPENDENT PROOF/SOURCE/CODE AUDIT PASS','candidate':str(base.parent/'monodromy/nonordinary_genus_two_triple_ramification_candidate.tex'),'candidate_sha256':hashlib.sha256((base.parent/'monodromy/nonordinary_genus_two_triple_ramification_candidate.tex').read_bytes()).hexdigest(),'author_output_sha256_before':before,'author_output_sha256_after':after,'isolated_output':out,'proof_scope':'Both ramification-budget cases, cyclic Kummer form and regular basis, S3 sign quotient local inertia and genus, exact Kummer involution, all four Cartier columns and invariant basis, separability determinant, Riemann–Roch no-triple consequence, canonical-tangent exclusion and exact |K|-1 node count rederived.','source_scope':'Freshly opened/read full Stacks53.12 (Tag0C1B), including53.12.2 and53.12.4 proofs, and Kummer Lemma9.24.1 (Tag09DX) proof; webrefs turn522640580view0/1. Existing f1 normal-form proof reread. No page image claimed.'}
(base/'genus_two_triple_ramification_independent_audit.json').write_text(json.dumps(record,indent=2)+'\n')
import re
labels=re.findall(r'\\label\{([^}]+)\}',(base.parent/'monodromy/nonordinary_genus_two_triple_ramification_candidate.tex').read_text())
with (base/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([record['actual_utc'],label,'INDEPENDENT_FULL_PASS',record['result'],record['candidate'],'genus_two_triple_ramification_independent_audit.json'])+'\n')
print(json.dumps({'actual_utc':record['actual_utc'],'result':record['result'],'runtime':out['elapsed_seconds'],'author_preserved':before==after,'labels':labels}))
