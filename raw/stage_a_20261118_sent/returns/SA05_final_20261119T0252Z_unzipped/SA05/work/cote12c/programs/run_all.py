"""Reproduce authored tables and exact checks, preserving every program output."""
import subprocess, sys
from pathlib import Path
B = Path('SA05/work/cote12c')
names = ['build_data.py','build_claims.py','build_tables.py','build_evidence.py','finalize.py','check_calculations.py','validate_scope.py']
logs = []
for name in names:
    result = subprocess.run([sys.executable,str(B/'programs'/name)],text=True,capture_output=True)
    log = f'PROGRAM {name}\nEXIT {result.returncode}\nSTDOUT\n{result.stdout}\nSTDERR\n{result.stderr}'
    (B/'outputs'/(name.removesuffix('.py')+'_run.txt')).write_text(log)
    logs.append(log)
    print(f'{name}: exit {result.returncode}')
    if result.returncode:
        print(result.stdout,result.stderr)
        (B/'outputs'/'build_log.txt').write_text('\n\n'.join(logs))
        raise SystemExit(result.returncode)
(B/'outputs'/'build_log.txt').write_text('\n\n'.join(logs))
