from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import hashlib, json, subprocess, urllib.request

base = Path(__file__).resolve().parents[1]
sources = [
    ('vangeemen1996_theta_cycles', 'https://sites.unimi.it/vangeemen/ThetafctsCycles4folds_MathZ1996.pdf'),
    ('vangeemen2022_weil', 'https://sigma-journal.com/2022/097/sigma22-097.pdf'),
    ('vangeemen_rapagnetta2026', 'https://arxiv.org/pdf/2607.18341'),
    ('voisin2026_chow_pirola_v4', 'https://arxiv.org/pdf/2607.07053v4'),
]
started = perf_counter()
report = {'utc_started': datetime.now(timezone.utc).isoformat(), 'sources': []}
for name, url in sources:
    item = {'name': name, 'url': url}
    t = perf_counter()
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mathematical-source-audit/1.0'})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
        assert data.startswith(b'%PDF'), 'The response is not a PDF.'
        p = base / 'sources' / (name+'.pdf')
        p.write_bytes(data)
        item.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), path=str(p))
        subprocess.run(['pdftotext', '-layout', str(p), str(p.with_suffix('.txt'))], check=True)
        item['status'] = 'obtained'
    except Exception as e:
        item.update(status='failed', error=repr(e))
    item['runtime_seconds'] = perf_counter()-t
    report['sources'].append(item)
report['runtime_seconds'] = perf_counter()-started
report['utc_finished'] = datetime.now(timezone.utc).isoformat()
out = base / 'output' / 'fetch_weil_sources_1323.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
