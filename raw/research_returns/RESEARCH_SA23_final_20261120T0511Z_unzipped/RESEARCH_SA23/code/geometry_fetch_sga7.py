"""Fetch the public SLMath primary scan and extract its text; no credentials."""
from pathlib import Path
from time import perf_counter
import subprocess, urllib.request

base = Path(__file__).resolve().parents[1]
out = base / 'notes' / 'geometry_SGA7I.pdf'
url = 'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf'
start = perf_counter()
if not out.exists():
    with urllib.request.urlopen(url, timeout=180) as response:
        data = response.read()
    if not data.startswith(b'%PDF'):
        raise ValueError('The public source did not return a PDF')
    out.write_bytes(data)
print('public_source', url)
print('bytes', out.stat().st_size)
subprocess.run(['pdftotext', '-layout', str(out), str(out.with_suffix('.txt'))], check=True)
print('text_path', out.with_suffix('.txt'))
print('elapsed_seconds', round(perf_counter() - start, 3))
