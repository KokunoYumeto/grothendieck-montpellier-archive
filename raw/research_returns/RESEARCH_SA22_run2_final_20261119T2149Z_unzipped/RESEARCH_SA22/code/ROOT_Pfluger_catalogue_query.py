"""Two ordinary GET searches of the publisher's advertised public catalogue."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://informatics-journals-api-he3ivhb46a-el.a.run.app/api/public/search/all"


def query(term):
    params = {"query": term, "page": 1, "limit": 20,
              "engine": "metadata_text", "withAnswer": "false"}
    url = term if term.startswith("https://") else BASE + "?" + urllib.parse.urlencode(params)
    row = {"query": term, "url": url,
           "started_utc": datetime.now(timezone.utc).isoformat()}
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
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
        row.update(status=error.code, error=str(error),
                   response_text=data.decode("utf-8", "replace"))
    except Exception as error:
        row["error"] = repr(error)
    row["seconds"] = time.perf_counter() - start
    row["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return row


if __name__ == "__main__":
    article_mode = "--article-metadata" in sys.argv
    targets = (["https://informatics-journals-api-he3ivhb46a-el.a.run.app/api/public/article/16922",
                "https://doi.org/10.18311/jims/1960/16922"]
               if article_mode else ["Pfluger", "Verheftung"])
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(query, targets))
    output = {"scope": "The unauthenticated public catalogue/article-metadata GET routes advertised by the current publisher client; not a full-text bypass", "results": rows}
    filename = "ROOT_Pfluger_article_metadata.json" if article_mode else "ROOT_Pfluger_catalogue_query.json"
    (ROOT / "logs" / filename).write_text(json.dumps(output, indent=2) + "\n")
    for row in rows:
        print(json.dumps(row, indent=2))
