"""Retrieve primary documents; retain logs, excluding raw works from deliverables."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time, urllib.request

BASE = Path('/workspace/scratch/6215ed17d0f0')
RAW = BASE / 'primary_sources/part_b/post07'
OUT = BASE / 'RESEARCH_SA05_work/part_b/output/post07_primary_capture.json'
RAW.mkdir(parents=True, exist_ok=True)
TASKS = [
    ('loewit2026.html', 'https://arxiv.org/html/2507.09392v2'),
    ('diaz2019.pdf', 'https://arxiv.org/pdf/1807.08163v3'),
    ('deglise2026.html', 'https://www.sciencedirect.com/science/article/pii/S0019357725000795'),
    ('deglise2026_author.html', 'https://arxiv.org/html/2408.06233v3'),
    ('scavia_suzuki_coniveau2024.pdf', 'https://arxiv.org/pdf/2304.08560v2'),
    ('jannsen1988.pdf', 'https://epub.uni-regensburg.de/26684/1/jannsen12.pdf'),
    ('kahn2012_full_faithfulness.pdf', 'https://webusers.imj-prg.fr/~bruno.kahn/preprints/full-faithfulnessIHES7.pdf'),
    ('richarz_scholbach2025.pdf', 'https://ems.press/content/serial-article-files/49857'),
    ('ruimy_tubach_wolf2026.html', 'https://arxiv.org/html/2601.07358v1'),
]
records = json.loads(OUT.read_text()) if OUT.exists() else []
for row in records:
    if row.get('bytes', 0) < 1000 and row.get('obtained'):
        row.update(obtained=False, content_validation='HTTP200 site-unavailable stub; not a primary document')
for name, url in TASKS:
    if any(row.get('url') == url for row in records):
        continue
    began = time.monotonic()
    row = {'file': name, 'url': url, 'utc': datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get('Content-Type', ''))
        (RAW / name).write_bytes(data)
        row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                   raw_path=str(RAW / name), obtained=len(data) >= 1000)
        if len(data) < 1000:
            row['content_validation'] = 'Short response: inspect before treating as primary document'
    except Exception as exc:
        row.update(obtained=False, error=f'{type(exc).__name__}: {exc}')
    row['seconds'] = round(time.monotonic() - began, 6)
    records.append(row)
OUT.write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
