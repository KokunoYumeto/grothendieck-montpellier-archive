"""Render primary handwritten pages used in the algebraic letter audit."""
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
source = root / 'sources/algebra_manuscript23.pdf'
info = subprocess.run(['pdfinfo', str(source)], capture_output=True, text=True)
print(info.stdout, flush=True)
info.check_returncode()
for page in [44,45,46,47,52,53,54,60,65,96,97,98]:
    dest = root / 'sources' / f'algebra_manuscript23_p{page:03d}'
    command = ['pdftoppm', '-f', str(page), '-l', str(page), '-scale-to',
               '2400', '-singlefile', '-png', str(source), str(dest)]
    result = subprocess.run(command, capture_output=True, text=True)
    print('command', repr(command), 'exit', result.returncode, flush=True)
    if result.stderr:
        print(result.stderr, flush=True)
    result.check_returncode()
print('Elapsed seconds', time.perf_counter() - start, flush=True)
