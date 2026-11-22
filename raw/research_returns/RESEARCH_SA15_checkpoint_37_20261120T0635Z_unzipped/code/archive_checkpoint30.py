"""Archive CP30 after its due time, completed review20 and actual final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T01:20:40+00:00')
review=json.loads((w/'notes/progress_review_20.json').read_text())
assert review['review']==20
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T00:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint30.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_30.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','30'),('verify_checkpoint_archive.py','30')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
