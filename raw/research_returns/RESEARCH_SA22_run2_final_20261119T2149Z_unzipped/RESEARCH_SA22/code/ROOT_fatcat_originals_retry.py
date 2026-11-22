"""One bounded public metadata retry after the earlier Fatcat HTTP 503.

This does not request protected full text, use credentials, or interpret
metadata as an opened original theorem. The initial URLs were already
observed in C_GabberFujiwara_metadata.py.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "Gabber1994": "10.1007/BF02773001",
    "Fujiwara1995": "10.1215/S0012-7094-95-08002-8",
}


def fetch(item):
    label, doi = item
    url = "https://api.fatcat.wiki/v0/release/lookup?" + urllib.parse.urlencode({"doi": doi})
    row = {"label": label, "doi": doi, "url": url,
           "started_utc": datetime.now(timezone.utc).isoformat()}
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("content-type"),
                       bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            try:
                row["response"] = json.loads(data)
            except ValueError:
                row["response_text"] = data.decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        data = error.read()
        row.update(status=error.code, final_url=error.url,
                   error=str(error), bytes=len(data),
                   sha256=hashlib.sha256(data).hexdigest(),
                   response_text=data.decode("utf-8", "replace"))
    except Exception as error:
        row["error"] = repr(error)
    row["seconds"] = time.perf_counter() - start
    row["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return row


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(fetch, TARGETS.items()))
    output = {"scope": "public metadata retry; not a theorem reading", "results": rows}
    path = ROOT / "logs/ROOT_fatcat_originals_retry.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps([{k: v for k, v in row.items()
                      if k not in {"response", "response_text"}}
                     for row in rows], indent=2))
