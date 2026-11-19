"""Rebuild authored registers in dependency order and retain every output."""
import subprocess
from pathlib import Path
for stem in ['build_items','build_refs','build_claims','build_problems','build_readings']:
    result=subprocess.run(['python',f'agents/p15/code/{stem}.py'],text=True,capture_output=True)
    output=result.stdout+result.stderr
    Path(f'agents/p15/evidence/{stem}.out').write_text(output)
    print(stem,result.returncode,output.strip())
    if result.returncode:raise SystemExit(result.returncode)
