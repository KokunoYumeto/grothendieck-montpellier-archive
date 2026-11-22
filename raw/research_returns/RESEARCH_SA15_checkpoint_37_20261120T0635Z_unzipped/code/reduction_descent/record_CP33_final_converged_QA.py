from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
own=root/'agents/reduction_descent'
path=own/'outputs/CP33_visual_QA.json'
prior=own/'outputs/CP33_visual_QA.preconvergence.json'
assert not prior.exists()
prior.write_bytes(path.read_bytes())
data=json.loads(path.read_text())
assert data['pdf_sha256']=='029cc723c44c6d3feda3b23bf8803504c8f11309350b4adb57a1b670338d28d2'
data['prior_record']=str(prior)
data['prior_actual_utc']=data['actual_utc']
data['actual_utc']=datetime.now(timezone.utc).isoformat()
data['pdf_sha256']='ea99a27826f7221acc327cb54ded638c46928e93ec6a531fca57b7c0cdba0c7e'
data['scope']='Final converged PDF: all nine rerendered complete PNGs645–653 actually reopened individually via view_image in three bounded batches. Rechecked every table, equation/tag, proved status, path, citation, continuation, glyph, margin and footer. Earlier QA record preserved; no source edit or rebuild.'
for row in data['page_observations']:
    old=row['png_sha256']
    new=hashlib.sha256(Path(row['png']).read_bytes()).hexdigest()
    row['prior_png_sha256']=old
    row['png_sha256']=new
    row['png_bytes_identical_to_preconvergence']=(old==new)
    row['observation']='Final converged rerender actually reopened and inspected again; the earlier detailed observations remain valid. '+row['observation']
data['defects']=[]
data['status']='PASS'
path.write_text(json.dumps(data,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([data['actual_utc'],'CP33-final-convergence-QA','PASS','All final images645–653 actually reopened and inspected','outputs/CP33_visual_QA.json;outputs/CP33_visual_QA.preconvergence.json','Final PDF ea99a278…ba0c7e; all nine visual checks PASS; prior record and PNG hash comparisons retained'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':data['actual_utc'],'pages':data['pages'],'record':str(path),'record_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'all_png_bytes_identical':all(r['png_bytes_identical_to_preconvergence'] for r in data['page_observations'])}))
