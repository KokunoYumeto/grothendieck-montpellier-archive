"""One bounded Google Books catalogue retry after the earlier rate limit.

Uses the already observed public volumes endpoint. Stops this route on
an access/rate-limit response; no API key or alternate identity is used.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
QUERIES = [
    ("gabber_exact_title", '"Affine analog of the proper base change theorem"'),
    ("fujiwara_exact_title", '"Theory of tubular neighborhood in etale topology"'),
    ("gabber_exact_doi", '"10.1007/BF02773001"'),
    ("fujiwara_exact_doi", '"10.1215/S0012-7094-95-08002-8"'),
    ("gabber_original_volume_retry", 'intitle:"Israel Journal of Mathematics" "87" "1994"'),
    ("fujiwara_original_volume", 'intitle:"Duke Mathematical Journal" "80" "1995"'),
]
results = []
stopped = None
for name, query in QUERIES:
    if stopped:
        results.append({"name": name, "query": query, "not_requested": stopped})
        continue
    url = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode(
        {"q": query, "maxResults": 40})
    row = {"name": name, "query": query, "url": url,
           "utc": datetime.now(timezone.utc).isoformat()}
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"))
    except urllib.error.HTTPError as error:
        data = error.read()
        row.update(status=error.code, final_url=error.url,
                   content_type=error.headers.get("Content-Type"), error=str(error))
        if error.code in (401, 403, 429):
            stopped = "Stopped route after HTTP " + str(error.code)
    except Exception as error:
        data = b""
        row["error"] = repr(error)
        stopped = "Stopped bounded route after request failure"
    row.update(bytes=len(data), sha256=sha256(data).hexdigest(),
               body=data.decode("utf-8", errors="replace"),
               elapsed_seconds=time.perf_counter() - start)
    results.append(row)
    print(json.dumps(row, ensure_ascii=False), flush=True)
record = {"purpose": "Authorized original-page discovery, not a metadata substitute",
          "previous_attempt": "logs/B_Gabber_public_indexes.json; 18:16:50UTC HTTP429",
          "stop_reason": stopped, "results": results}
(BASE / "logs/B_GoogleBooks_original_retry.json").write_text(
    json.dumps(record, indent=2, ensure_ascii=False))
