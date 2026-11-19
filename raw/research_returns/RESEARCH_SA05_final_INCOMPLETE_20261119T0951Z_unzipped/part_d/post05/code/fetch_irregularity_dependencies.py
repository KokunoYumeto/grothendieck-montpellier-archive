"""Archive primary-source text and hashes; keep raw PDFs outside deliverables."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request

post = Path(__file__).resolve().parents[1]
raw = post.parents[2] / 'pending_post05_sources_d'
raw.mkdir(exist_ok=True)
records = []
for name, url in [
    ('Poonen2004Bertini', 'https://math.mit.edu/~poonen/papers/bertini.pdf'),
    ('Tate1966Bourbaki306', 'https://www.numdam.org/item/SB_1964-1966__9__415_0.pdf'),
]:
    record = {'name': name, 'url': url, 'retrieved_utc': datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(request, timeout=30).read()
        pdf = raw / (name + '.pdf')
        pdf.write_bytes(data)
        target = post / 'sources' / (name + '.txt')
        subprocess.run(['pdftotext', '-layout', str(pdf), str(target)], check=True)
        record.update(status='downloaded', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), text=str(target))
    except Exception as error:
        record.update(status='failed', error=str(error))
    records.append(record)
output = post / 'output' / 'irregularity_dependencies_fetch_output.json'
output.write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
