"""Archive only at/after the scheduled time and after observed final PDF QA."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-19T16:20:40+00:00'),'Never create a scheduled checkpoint early'
assert json.loads((w/'outputs/visual_qa_checkpoint18.json').read_text())['status']=='PASS'
assert not(w.parent/'RESEARCH_SA15_checkpoint_18.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','18'),('verify_checkpoint_archive.py','18')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
