"""Local extraction of already opened public PDFs for exact page locators."""
from pathlib import Path
import subprocess
root=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle/research')
for p in sorted(root.glob('*.pdf')):
    out=p.with_suffix('.txt')
    r=subprocess.run(['pdftotext','-layout',str(p),str(out)],capture_output=True,text=True)
    print(p.name, 'exit',r.returncode,'text_bytes',out.stat().st_size if out.exists() else 0)
    if r.stderr: print(r.stderr)
