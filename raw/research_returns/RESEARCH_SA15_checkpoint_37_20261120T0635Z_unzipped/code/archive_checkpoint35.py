"""Archive CP35 only after05:05:40UTC, completed review24 and actual final-page QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T05:05:40+00:00')
review=json.loads((w/'notes/progress_review_24.json').read_text());assert review['review']==24
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T04:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint35.json').read_text());assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_35.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','35'),('verify_checkpoint_archive.py','35')]:
 command=[sys.executable,str(w/'code'/name)]
 if arg is not None:command.append(arg)
 subprocess.run(command,check=True,cwd=w)
