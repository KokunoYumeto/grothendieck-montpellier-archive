"""Record the exact, independently checked C.3ak range partition."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
columns=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
row=['C.3ak',
     'For every r>=1, ordinary local J^r restriction over C is universally surjective exactly in dimensions N<=r+1; the same universal range holds integrally',
     'Proved',
     'local_surjectivity_classification.tex, paragraph C.3ak',
     'Target dimension; C.3ai for r+2<=N<=2r+1; C.3m for r1,N>=4; C.3aj for r>=2,N>=2r+2',
     '14:107-112',
     'Excellent normal strictly henselian local complex rings with residue C, regular puncture and regular principal divisor puncture; ordinary fixed-product algebraic equivalence. The positive range is target zero. Every other dimension has a specified nontorsion cokernel witness. Higher injectivity and positive-characteristic higher restriction remain separate.']
with (base/'local_surjectivity_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(columns);w.writerow(row)
who='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/cycles'
root='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root'
events=[
 (who,'used and rechecked in this run','Read exact C3m and C3o scopes for r1, and the finalized C3ai/C3aj statements. Checked exhaustive range partition for every positive r,N. No high-codimension injectivity conclusion is imported.'),
 (who,'targeted proof check','For N<=r+1 the punctured divisor has dimension at most N-2<r; for N1 it is empty. Thus the full target Chow group is zero integrally. Every complementary construction has nontorsion ordinary cokernel, giving both integral and rational failure.'),
 (root,'independent targeted proof check','Root read full typed C3ak and passed quantified scope, integral/rational distinction, target-zero range includingN1 and exhaustive three-row partition; integration authorized at09:29-stage.'),
 (who,'typesetting verification','Standalone LuaLaTeX build has no diagnostics, runtime0.9312339300013264 seconds at09:28:53UTC. This corollary has no new external citations; its proved dependencies carry their exact primary references.')]
with (base/'local_surjectivity_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
 for actor,kind,outcome in events:w.writerow(['C.3ak','2026-11-19',actor,kind,outcome])
record={'utc':datetime.now(timezone.utc).isoformat(),'rows':1,'events':len(events),'runtime_seconds':time.perf_counter()-started}
(base/'output/register_local_surjectivity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
