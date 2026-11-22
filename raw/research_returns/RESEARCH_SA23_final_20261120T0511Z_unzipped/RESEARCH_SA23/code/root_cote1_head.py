"""Record header diagnostics for the slow original manuscript download."""
import json, time, urllib.request
from pathlib import Path
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
record = {'url':'https://grothendieck.umontpellier.fr/1.pdf','method':'HEAD'}
try:
    request = urllib.request.Request(record['url'], method='HEAD')
    with urllib.request.urlopen(request, timeout=25) as response:
        record.update(status=response.status, headers=dict(response.headers))
except Exception as error:
    record['error'] = str(error)
record['elapsed_seconds'] = time.perf_counter()-started
(root/'logs'/'root_cote1_head.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2), flush=True)
