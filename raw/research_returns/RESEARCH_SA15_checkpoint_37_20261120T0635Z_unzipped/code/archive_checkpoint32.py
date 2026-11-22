"""Archive CP32 only after its due time, actual review22 and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T02:50:40+00:00')
review=json.loads((w/'notes/progress_review_22.json').read_text())
assert review['review']==22
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T02:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint32.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_32.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','32'),('verify_checkpoint_archive.py','32')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
