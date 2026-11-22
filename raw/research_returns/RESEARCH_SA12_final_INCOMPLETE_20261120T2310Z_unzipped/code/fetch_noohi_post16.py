"""Fetch primary Noohi material for the finite-band gerbe comparison."""
from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import hashlib
import json
import tarfile
import io
import time

root = Path(__file__).resolve().parents[1]
dest = root / 'parts/D/sources/Noohi2004'
dest.mkdir(parents=True, exist_ok=True)
records = []
for url, name in [
    ('https://arxiv.org/src/math/0201021', 'arxiv-source.tar'),
    ('https://arxiv.org/pdf/math/0201021', 'arxiv.pdf'),
]:
    t = time.perf_counter()
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=35).read()
        (dest / name).write_bytes(data)
        rec = dict(url=url, path=str((dest / name).relative_to(root)), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), seconds=time.perf_counter()-t)
        if name.endswith('.tar'):
            try:
                with tarfile.open(fileobj=io.BytesIO(data)) as archive:
                    members = archive.getmembers()
                    for member in members:
                        target = (dest / 'source' / member.name).resolve()
                        assert target.is_relative_to((dest / 'source').resolve())
                        assert not member.issym() and not member.islnk()
                    archive.extractall(dest / 'source', filter='data')
                    rec['extracted_files'] = [member.name for member in members if member.isfile()]
            except tarfile.ReadError:
                rec['extraction'] = 'Response is not a tar archive; preserved without claiming extraction.'
        records.append(rec)
    except Exception as exc:
        records.append(dict(url=url, error=str(exc), seconds=time.perf_counter()-t))
record = dict(utc=datetime.now(timezone.utc).isoformat(), downloads=records)
(root / 'code/output/fetch_noohi_post16.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
