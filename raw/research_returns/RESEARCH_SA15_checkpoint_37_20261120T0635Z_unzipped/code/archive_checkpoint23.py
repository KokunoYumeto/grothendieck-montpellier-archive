"""Archive checkpoint23 only when due, after final QA and actual review15."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
assert datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-11-19T20:05:40+00:00')
assert json.loads((w/'outputs/visual_qa_checkpoint23.json').read_text())['status']=='PASS'
assert json.loads((w/'notes/progress_review_15.json').read_text())['review']==15
assert not(w.parent/'RESEARCH_SA15_checkpoint_23.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','23'),('verify_checkpoint_archive.py','23')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
