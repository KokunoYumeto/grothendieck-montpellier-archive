"""Archive checkpoint24 only when due, after final QA and actual review16."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
assert datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-11-19T20:50:40+00:00')
assert json.loads((w/'outputs/visual_qa_checkpoint24.json').read_text())['status']=='PASS'
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==json.loads((w/'outputs/visual_qa_checkpoint24.json').read_text())['pdf_sha256']
assert json.loads((w/'notes/progress_review_16.json').read_text())['review']==16
assert not(w.parent/'RESEARCH_SA15_checkpoint_24.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','24'),('verify_checkpoint_archive.py','24')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
