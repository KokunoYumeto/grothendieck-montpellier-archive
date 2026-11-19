"""Inspect the official public archive index for the cited dossier's scan URL."""
from pathlib import Path
import hashlib
import json
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://grothendieck.umontpellier.fr/archives-grothendieck/'
start = time.perf_counter()
with urllib.request.urlopen(URL, timeout=45) as response:
    raw = response.read()
html = raw.decode('utf-8', errors='replace')
dest = ROOT / 'sources' / 'montpellier_archive_index.html'
dest.write_bytes(raw)
matches = []
for match in re.finditer(r'.{0,200}(?:Cote n[^<]{0,25}15|data-target="15").{0,400}', html, re.I):
    text = match.group(0)
    if 'iframe' in text.lower() or re.search(r'\b15\b|015|\.pdf', text, re.I):
        matches.append(text)
report = {
    'url': URL,
    'bytes': len(raw),
    'sha256': hashlib.sha256(raw).hexdigest(),
    'runtime_seconds': time.perf_counter() - start,
    'relevant_index_markup': matches,
}
out = ROOT / 'code' / 'probe_montpellier_archive_output.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
