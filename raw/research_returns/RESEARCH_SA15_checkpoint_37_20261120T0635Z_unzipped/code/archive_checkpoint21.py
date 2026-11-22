"""Archive only when due, with verified final QA and the latest actual review."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
assert datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-11-19T18:35:40+00:00')
assert json.loads((w/'outputs/visual_qa_checkpoint21.json').read_text())['status']=='PASS'
assert json.loads((w/'notes/progress_review_13.json').read_text())['review']==13
assert not(w.parent/'RESEARCH_SA15_checkpoint_21.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','21'),('verify_checkpoint_archive.py','21')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
