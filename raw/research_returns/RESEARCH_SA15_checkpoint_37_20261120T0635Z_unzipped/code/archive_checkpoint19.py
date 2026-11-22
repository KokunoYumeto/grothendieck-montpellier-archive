"""Never archive early or overwrite an immutable checkpoint."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
assert datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-11-19T17:05:40+00:00')
assert json.loads((w/'outputs/visual_qa_checkpoint19.json').read_text())['status']=='PASS'
assert not(w.parent/'RESEARCH_SA15_checkpoint_19.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','19'),('verify_checkpoint_archive.py','19')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
