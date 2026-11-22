"""Two new public IA metadata queries motivated by the actually read MGP1967 date."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json

BASE = Path(__file__).resolve().parent
QUERIES = [
    'title:("Algebraic cycles") AND year:1967',
    'title:("Non-Singular Complex Projective")',
]

def query(q):
    params = [('q', q), ('fl[]', 'identifier'), ('fl[]', 'title'),
              ('fl[]', 'creator'), ('fl[]', 'year'), ('rows', '50'),
              ('output', 'json')]
    url = 'https://archive.org/advancedsearch.php?' + urlencode(params)
    t0 = perf_counter()
    row = {'query': q, 'url': url}
    try:
        with urlopen(url, timeout=35) as r:
            data = json.load(r)
            row.update(status=r.status, result=data)
    except (HTTPError, URLError, TimeoutError) as e:
        row.update(error=repr(e), status=getattr(e, 'code', None))
    row['elapsed_seconds'] = perf_counter() - t0
    return row

started = datetime.now(timezone.utc).isoformat()
t0 = perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:
    rows = list(pool.map(query, QUERIES))
result = {'started_utc': started, 'elapsed_seconds': perf_counter() - t0,
          'scope': 'Two public metadata searches only; no file content requested.',
          'requests': rows}
out = json.dumps(result, ensure_ascii=False, indent=2)
(BASE / 'part_c_lieberman_1967_metadata_output.json').write_text(out + '\n')
(BASE / 'part_c_lieberman_1967_metadata_output.txt').write_text(out + '\n')
print(out)
