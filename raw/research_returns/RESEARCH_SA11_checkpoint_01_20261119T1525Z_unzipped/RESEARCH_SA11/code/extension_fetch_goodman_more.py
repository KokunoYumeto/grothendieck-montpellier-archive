"""Fetch discovered primary-paper scans; OCR their title pages for identification.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
"""
from pathlib import Path
import urllib.request, subprocess, concurrent.futures, time, json, hashlib

root = Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
base = 'https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/'
items = [(f'Goodman{k}', f'Goodman{k}.pdf') for k in range(1, 5)]
items += [('Pollack5', 'PollackRichard/Pollack5.pdf'),
          ('Pollack7', 'PollackRichard/Pollack7.pdf')]

def one(item):
    name, rel = item
    start = time.monotonic()
    url = base + rel
    data = urllib.request.urlopen(url, timeout=45).read()
    path = root / f'sources/extension_{name}.pdf'
    path.write_bytes(data)
    subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))],
                   check=True, capture_output=True)
    out = root / f'audit/extension_{name}_p1'
    subprocess.run(['pdftoppm', '-f', '1', '-singlefile', '-r', '150', '-png',
                    str(path), str(out)], check=True, capture_output=True)
    subprocess.run(['tesseract', str(out) + '.png', str(out), '--psm', '3'],
                   check=True, capture_output=True)
    return dict(name=name, url=url, sha256=hashlib.sha256(data).hexdigest(),
                bytes=len(data), runtime_s=time.monotonic()-start,
                page1=out.with_suffix('.txt').read_text())

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(one, items))
(root / 'audit/extension_fetch_goodman_more_output.json').write_text(
    json.dumps(results, indent=2))
for result in results:
    print(json.dumps(result), flush=True)
