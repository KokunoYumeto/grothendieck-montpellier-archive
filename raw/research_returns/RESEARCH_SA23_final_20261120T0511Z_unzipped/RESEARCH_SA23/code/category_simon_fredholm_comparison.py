from pathlib import Path
import hashlib
import subprocess

ROOT = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
jobs = [
    ('Simon1977', ROOT/'notes/category_Simon1977.pdf', ROOT/'notes/category_Simon1977.txt', [2, 3, 5, 11, 13, 14, 15, 29]),
    ('Fredholm1956', ROOT/'notes/geometry_Fredholm1956.pdf', ROOT/'notes/geometry_Fredholm1956_full.txt', [10, 14, 28, 29, 30, 31, 33, 34, 36, 37, 42, 43, 44, 65, 66]),
]
for name, pdf, txt, selected in jobs:
    print('SOURCE', name, 'SHA256', hashlib.sha256(pdf.read_bytes()).hexdigest())
    pages = txt.read_text().split('\f')
    print('EXTRACTED_FORMFEED_PAGES', len(pages))
    for physical in selected:
        print('\nBEGIN_PHYSICAL_PAGE', name, physical)
        print(pages[physical-1])
        print('END_PHYSICAL_PAGE', name, physical)

for name, pdf, physical, printed in [
    ('Simon1977', jobs[0][1], 11, 254),
    ('Simon1977', jobs[0][1], 14, 257),
    ('Simon1977', jobs[0][1], 15, 258),
    ('Fredholm1956', jobs[1][1], 31, 348),
    ('Fredholm1956', jobs[1][1], 36, 353),
    ('Fredholm1956', jobs[1][1], 37, 354),
]:
    target = ROOT/f'notes/category_compare_{name}_p{printed}'
    run = subprocess.run(['pdftoppm', '-f', str(physical), '-l', str(physical), '-scale-to', '1800', '-singlefile', '-png', str(pdf), str(target)], capture_output=True, text=True)
    print('RENDER', name, physical, printed, run.returncode, run.stderr.strip())
    if run.returncode:
        raise RuntimeError('Rendering failed')
