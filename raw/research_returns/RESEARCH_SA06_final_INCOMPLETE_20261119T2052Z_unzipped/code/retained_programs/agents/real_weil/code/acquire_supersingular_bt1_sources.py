from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, time, urllib.request

root = Path(__file__).resolve().parents[3]
sources = [
    ('pries_ulmer2022_every_bt1_published', 'https://archive.math.arizona.edu/ulmer/research/papers/2021c.pdf'),
    ('viehmann2026_oort_v2', 'https://arxiv.org/pdf/2603.06033v2'),
    ('karemaker_yobuko_yu2021_mass_v2', 'https://arxiv.org/pdf/2002.10960v2'),
    ('hatcher2002_AT_chapter3', 'https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf'),
    ('milne2008_abelian_varieties_v2', 'https://www.jmilne.org/math/CourseNotes/AV.pdf'),
]

def acquire(item):
    name, url = item
    started = datetime.now(timezone.utc).isoformat()
    tick = time.perf_counter()
    record = dict(name=name, url=url, started_utc=started)
    try:
        response = urllib.request.urlopen(url, timeout=45)
        record['final_url'] = response.url
        data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        target = root / 'sources' / (name + '.pdf')
        target.write_bytes(data)
        proc = subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], capture_output=True, text=True)
        record.update(file=str(target.relative_to(root)), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pdftotext_returncode=proc.returncode, pdftotext_stderr=proc.stderr)
    except Exception as error:
        record['error'] = repr(error)
    record.update(finished_utc=datetime.now(timezone.utc).isoformat(), seconds=time.perf_counter()-tick)
    return record

started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    records = list(pool.map(acquire, sources))
result = dict(started_utc=started, finished_utc=datetime.now(timezone.utc).isoformat(), seconds=time.perf_counter()-tick, sources=records)
output = root / 'agents/real_weil/output/supersingular_bt1_sources_acquisition.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
