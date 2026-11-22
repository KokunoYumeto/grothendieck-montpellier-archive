"""Archive the inspected CP13 only when its scheduled time has arrived."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime.fromisoformat('2026-11-19T12:35:40+00:00')
assert now>=due, 'Never create a scheduled checkpoint early'
assert json.loads((w/'outputs/visual_qa_checkpoint13.json').read_text())['status']=='PASS'
assert not (w.parent/'RESEARCH_SA15_checkpoint_13.zip').exists()
for name,arg in [('export_agent_programs.py',None),('checkpoint.py','13'),('verify_checkpoint_archive.py','13')]:
 cmd=[sys.executable,str(w/'code'/name)]+([arg] if arg else [])
 subprocess.run(cmd,check=True,cwd=w)
