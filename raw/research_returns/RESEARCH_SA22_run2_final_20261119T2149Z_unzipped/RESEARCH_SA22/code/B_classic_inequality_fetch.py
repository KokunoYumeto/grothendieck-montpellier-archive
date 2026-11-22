"""Ordinary public-source retrieval for the two requested inequality works."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import time
import urllib.error
import urllib.request

BASE = Path(__file__).resolve().parents[1]
ITEMS = [
    ("HLP1952", "https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/inequalities-hardy-littlewood-polya.pdf", "B_HLP1952.pdf"),
    ("Gabriel1932_OUP", "https://academic.oup.com/plms/article-abstract/s2-33/1/32/1523057", "B_Gabriel1932_OUP.html"),
]

def fetch(item):
    name, url, filename = item
    row = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    started = time.perf_counter()
    data = bytearray()
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"),
                       advertised_length=response.headers.get("Content-Length"))
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                data.extend(chunk)
                if len(data) % (5 * 1024 * 1024) == 0:
                    print(name, "downloaded", len(data), "bytes", flush=True)
        is_pdf = data.startswith(b"%PDF")
        row["is_pdf"] = is_pdf
        if filename.endswith(".pdf") and not is_pdf:
            filename = filename + ".response.html"
        destination = BASE / "literature" / filename
        destination.write_bytes(data)
        row["saved_path"] = str(destination.relative_to(BASE))
    except urllib.error.HTTPError as error:
        data = bytearray(error.read())
        row.update(status=error.code, final_url=error.url, error=str(error),
                   response_excerpt=data.decode("utf-8", errors="replace")[:1500])
    except Exception as error:
        row["error"] = repr(error)
    row.update(bytes=len(data), sha256=sha256(data).hexdigest(),
               elapsed_seconds=time.perf_counter() - started)
    print(json.dumps(row, ensure_ascii=False), flush=True)
    return row

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, ITEMS))
(BASE / "logs/B_classic_inequality_fetch.json").write_text(
    json.dumps(results, indent=2, ensure_ascii=False))
