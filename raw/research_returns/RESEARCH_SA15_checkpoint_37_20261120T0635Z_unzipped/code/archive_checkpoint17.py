"""Create the complete inspected CP17 only at or after its scheduled time."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-19T15:35:40+00:00'),'Never create a scheduled checkpoint early'
assert json.loads((w/'outputs/visual_qa_checkpoint17.json').read_text())['status']=='PASS'
assert not (w.parent/'RESEARCH_SA15_checkpoint_17.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','17'),('verify_checkpoint_archive.py','17')]:
    cmd=[sys.executable,str(w/'code'/name)]+([arg] if arg else [])
    subprocess.run(cmd,check=True,cwd=w)
