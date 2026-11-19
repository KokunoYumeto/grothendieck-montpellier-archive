"""Reproduce the post-checkpoint-05 primary-source archive."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, urllib.request
root = Path(__file__).resolve().parent
records = []
for name, url in [
    ('CadoretHuiTamagawaGST', 'https://webusers.imj-prg.fr/~anna.cadoret/GST.pdf'),
    ('Qin2021NonproperBrauer', 'https://arxiv.org/pdf/2012.01681'),
]:
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(request, timeout=30).read()
        pdf = root / (name + '.pdf')
        pdf.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(pdf), str(root / (name + '.txt'))], check=True)
        records.append({'name': name, 'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'status': 'downloaded and text extracted'})
    except Exception as exc:
        records.append({'name': name, 'url': url, 'status': 'failed', 'error': str(exc)})
output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'records': records}
(root / 'fetch_output.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
