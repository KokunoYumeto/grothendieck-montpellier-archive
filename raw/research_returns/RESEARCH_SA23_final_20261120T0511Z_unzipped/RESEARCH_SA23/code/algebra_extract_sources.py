"""Extract original sources and index exact printed locators for Part D."""
from pathlib import Path
import re
import subprocess
import time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
jobs = {
    'EGA0IV.pdf': ['19.3.12', '19.5.5', '19.5.6', '20.4.6', '20.4.13'],
    'EGAIV4.pdf': ['16.1.5', '16.1.6', '19.5.5', '19.5.6', '20.1.3', '21.6.2'],
    'EGAIII1.pdf': ['4.3.6'],
}
for name, locators in jobs.items():
    pdf = root / 'sources' / name
    if not pdf.exists():
        print('NOT YET DOWNLOADED', name, flush=True)
        continue
    txt = root / 'sources' / ('algebra_' + pdf.stem + '.txt')
    subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True)
    pages = txt.read_text().split('\f')
    print(name, 'pages', len(pages)-1, 'text bytes', txt.stat().st_size, flush=True)
    for locator in locators:
        pattern = r'\s*\.\s*'.join(map(re.escape, locator.split('.')))
        found = [i+1 for i, page in enumerate(pages) if re.search(pattern, page)]
        print('locator', locator, 'PDF physical pages', found, flush=True)
print('Elapsed seconds', time.perf_counter()-start)
