"""Archive the inspected CP14 only after the scheduled time arrives."""
from pathlib import Path
import datetime, json, subprocess, sys
w = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc)
due = datetime.datetime.fromisoformat('2026-11-19T13:20:40+00:00')
assert now >= due, 'Never create a scheduled checkpoint early'
assert json.loads((w / 'outputs/visual_qa_checkpoint14.json').read_text())['status'] == 'PASS'
assert not (w.parent / 'RESEARCH_SA15_checkpoint_14.zip').exists()
for name, arg in [('export_agent_programs.py', None), ('checkpoint.py', '14'),
                  ('verify_checkpoint_archive.py', '14')]:
    cmd = [sys.executable, str(w / 'code' / name)] + ([arg] if arg else [])
    subprocess.run(cmd, check=True, cwd=w)
