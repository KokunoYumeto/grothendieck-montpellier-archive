"""One bounded public catalogue route for Gabriel1932; metadata only."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
QUERIES = {
    "exact_article": 'title:"The rearrangement of positive Fourier coefficients"',
    "journal_1931_1933": 'title:(Proceedings AND London AND Mathematical) '
                         'AND year:[1931 TO 1933]',
    "journal_volume_33": 'title:(Proceedings AND London AND Mathematical) '
                         'AND volume:33',
}


def fetch(item):
    label, query = item
    params = [("q", query), ("output", "json"), ("rows", "100")]
    params += [("fl[]", field) for field in
               ("identifier", "title", "date", "year", "volume", "collection",
                "access-restricted-item")]
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params)
    result = {"label": label, "query": query, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat()}
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            data = response.read()
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        result["data"] = json.loads(data)
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    result["elapsed_seconds"] = time.perf_counter() - start
    result["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return result


with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, QUERIES.items()))
report = {"completed_utc": datetime.now(timezone.utc).isoformat(),
          "scope": "One bounded actual public IA catalogue route; metadata only",
          "results": results}
(BASE / "logs" / "B_Gabriel_IA_catalogue.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + "\n"
)
print(json.dumps(report, indent=2, ensure_ascii=False))
