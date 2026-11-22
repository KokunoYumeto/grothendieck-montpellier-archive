"""Disclose the preserved metadata preflight failure without changing the frozen PDF."""
from pathlib import Path
import json,datetime
w=Path(__file__).resolve().parents[1]
p=w/'outputs/visual_qa_checkpoint21.json';r=json.loads(p.read_text());r['metadata_finalization_preflight_failures']=1;r['metadata_failure_record']='outputs/checkpoint21_finalizer_preflight_failure.txt';p.write_text(json.dumps(r,indent=2)+'\n')
paragraph='\n### Finalizer metadata correction\n\nThe first finalizer invocation stopped before writing any result because one actual reviewer used the explicit JSON keys result/actual_images_viewed while the other reviewers used status/pages. The corrected finalizer accepts both schemas and then passed. The exact failed program and error are retained in code/finalize_checkpoint21_initial_metadata_failure.py and outputs/checkpoint21_finalizer_preflight_failure.txt. This was a metadata preflight failure, not a failed mathematical computation, failed compilation or unperformed visual inspection.\n'
for rel in ['notes/checkpoint21_changes.md','RESEARCH_SA15_report.md']:
    with (w/rel).open('a') as f:f.write(paragraph)
print(datetime.datetime.now(datetime.timezone.utc).isoformat(),'Finalizer correction disclosed; PDF unchanged.')
