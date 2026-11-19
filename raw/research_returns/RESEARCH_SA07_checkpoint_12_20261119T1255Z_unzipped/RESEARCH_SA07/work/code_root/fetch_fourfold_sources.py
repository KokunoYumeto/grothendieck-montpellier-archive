"""Record exact original-source retrieval attempts for the 2026 fourfold search."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'work' / 'sources_root_after11'
DEST.mkdir(exist_ok=True)
TARGETS = [
    ('Broe2026.pdf', 'https://arxiv.org/pdf/2608.28651'),
    ('Li2026_abs.html', 'https://arxiv.org/abs/2609.27916v2'),
    ('Broe_research.html', 'https://sites.google.com/view/mattbroe/research'),
]

def fetch(item):
    name, url = item
    begin = time.perf_counter()
    result = {'url': url, 'actual_utc': datetime.now(timezone.utc).isoformat()}
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=35) as response:
            content = response.read()
            status = response.status
            result.update(status=status, final_url=response.url,
                          content_type=response.headers.get('content-type'),
                          bytes=len(content))
        if status == 200:
            path = DEST / name
            path.write_bytes(content)
            result.update(saved=str(path.relative_to(ROOT)),
                          sha256=hashlib.sha256(content).hexdigest())
        else:
            result['error_excerpt'] = content[:160].decode(errors='replace')
    except (URLError, HTTPError, TimeoutError) as error:
        result['error'] = str(error)
    result['seconds'] = time.perf_counter() - begin
    return result

with ThreadPoolExecutor(max_workers=3) as executor:
    records = list(executor.map(fetch, TARGETS))
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(records, indent=2) + '\n')
print(out.read_text())
