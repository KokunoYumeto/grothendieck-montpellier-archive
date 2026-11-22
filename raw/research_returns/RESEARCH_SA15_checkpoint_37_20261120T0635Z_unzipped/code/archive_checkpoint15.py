"""Archive the fully inspected CP15 only at/after its scheduled time."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime.fromisoformat('2026-11-19T14:05:40+00:00')
assert now>=due,'Never create a scheduled checkpoint early'
assert json.loads((w/'outputs/visual_qa_checkpoint15.json').read_text())['status']=='PASS'
assert not (w.parent/'RESEARCH_SA15_checkpoint_15.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),('checkpoint.py','15'),('verify_checkpoint_archive.py','15')]:
 cmd=[sys.executable,str(w/'code'/name)]+([arg] if arg else [])
 subprocess.run(cmd,check=True,cwd=w)
