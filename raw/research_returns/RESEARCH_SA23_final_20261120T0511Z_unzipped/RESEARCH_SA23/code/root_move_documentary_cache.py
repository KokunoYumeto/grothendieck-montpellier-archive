"""Place an original DjVu scan with retrievable sources before the next archive."""
from pathlib import Path
import datetime, hashlib, json, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
old = root / 'notes/geometry_GohbergKrein1965.djvu'
new = root / 'sources/geometry_GohbergKrein1965.djvu'
assert old.exists() and not new.exists()
digest = hashlib.sha256(old.read_bytes()).hexdigest()
old.rename(new)
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'from': str(old.relative_to(root)), 'to': str(new.relative_to(root)),
          'sha256': digest, 'reason': 'Original retrievable source, not a written deliverable.',
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_move_documentary_cache.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
