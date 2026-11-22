"""Read the first-page preview actually linked by the saved 2020 Euclid landing.

This ordinary public request does not request the subscription-controlled
full article. It is an access attempt, not a mathematical verification.
"""
from pathlib import Path
import hashlib
import json
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
url = ('https://web.archive.org/web/20200812020402/'
       'https://www.projecteuclid.org/first_page/euclid.dmj/1077245853')
result = {
    'url': url,
    'provenance': 'sources/fujiwara1995_archived_landing.html, line 343, First page link',
    'scope': 'one ordinary advertised first-page-preview request; not full article',
}
started = time.perf_counter()
try:
    with urllib.request.urlopen(url, timeout=45) as response:
        result['status'] = response.status
        result['final_url'] = response.geturl()
        result['content_type'] = response.headers.get('Content-Type')
        data = response.read(2 * 1024 * 1024 + 1)
    result['bytes'] = len(data)
    result['truncated_at_limit'] = len(data) > 2 * 1024 * 1024
    result['sha256'] = hashlib.sha256(data).hexdigest()
    target = root / 'sources/part_a567_fujiwara_first_page.html'
    target.write_bytes(data)
    result['saved_response'] = str(target.relative_to(root))
except Exception as error:
    result['error'] = f'{type(error).__name__}: {error}'
result['elapsed_seconds'] = time.perf_counter() - started
output = root / 'code/part_a567_fujiwara_preview_output.json'
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
