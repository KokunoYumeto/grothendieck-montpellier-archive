"""Render the primary EGA pages whose exact words affect Part D."""
from pathlib import Path
import subprocess
import time

root=Path(__file__).resolve().parents[1]
jobs={
    'EGA0IV.pdf':[84,85,93,124,126],
    'EGAIV4.pdf':[5,6,206,207,208,226,227,228],
}
start=time.perf_counter()
for name,pages in jobs.items():
    source=root/'sources'/name
    if not source.exists():
        continue
    for page in pages:
        dest=root/'sources'/f'algebra_{source.stem}_p{page:03d}'
        command=['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1800',
                 '-singlefile','-png',str(source),str(dest)]
        completed=subprocess.run(command,capture_output=True,text=True)
        print('command',repr(command),'exit',completed.returncode,flush=True)
        if completed.stderr:
            print(completed.stderr,flush=True)
        completed.check_returncode()
print('Elapsed seconds',time.perf_counter()-start)
