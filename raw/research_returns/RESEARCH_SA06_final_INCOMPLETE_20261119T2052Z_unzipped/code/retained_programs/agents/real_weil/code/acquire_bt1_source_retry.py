from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, time, urllib.request

root = Path(__file__).resolve().parents[3]
started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
records = []
for name, url in [
    ('pries_ulmer2022_every_bt1_published', 'https://dlulmer.github.io/research/papers/2021c.pdf'),
    ('milne2008_abelian_varieties_v2', 'https://www.jmilne.org/math/CourseNotes/AV.pdf'),
]:
    entry = dict(name=name, url=url, started_utc=datetime.now(timezone.utc).isoformat())
    source_tick = time.perf_counter()
    try:
        request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        response = urllib.request.urlopen(request, timeout=45)
        data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        target = root / 'sources' / (name + '.pdf')
        target.write_bytes(data)
        result = subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], capture_output=True, text=True)
        entry.update(final_url=response.url, file=str(target.relative_to(root)), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pdftotext_returncode=result.returncode, pdftotext_stderr=result.stderr)
    except Exception as error:
        entry['error'] = repr(error)
    entry.update(finished_utc=datetime.now(timezone.utc).isoformat(), seconds=time.perf_counter()-source_tick)
    records.append(entry)
result = dict(started_utc=started, finished_utc=datetime.now(timezone.utc).isoformat(), seconds=time.perf_counter()-tick, sources=records)
(root / 'agents/real_weil/output/bt1_source_retry_acquisition.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
