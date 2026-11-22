"""Archive CP37 only after06:35:40UTC, completed review25 and actual final-page QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T06:35:40+00:00')
review=json.loads((w/'notes/progress_review_25.json').read_text());assert review['review']==25
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T05:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint37.json').read_text());assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_37.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','37'),('verify_checkpoint_archive.py','37')]:
 command=[sys.executable,str(w/'code'/name)]
 if arg is not None:command.append(arg)
 subprocess.run(command,check=True,cwd=w)
