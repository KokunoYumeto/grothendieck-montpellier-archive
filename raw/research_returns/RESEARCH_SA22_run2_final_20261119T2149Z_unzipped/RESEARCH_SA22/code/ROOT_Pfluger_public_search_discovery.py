"""Read only the public script advertised by the current publisher page.

Purpose: identify its unauthenticated catalogue search, not private APIs or
protected full-text routes. No credentials or account state are inspected.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "literature/ROOT_Pfluger1960_current_publisher.html").read_text()
match = re.search(r'<script[^>]+src="(/assets/[^"]+\.js)"', html)
if not match:
    raise SystemExit("No advertised public application script found")
url = "https://informaticsjournals.com" + match.group(1)
row = {"url": url, "started_utc": datetime.now(timezone.utc).isoformat()}
start = time.perf_counter()
try:
    with urllib.request.urlopen(url, timeout=25) as response:
        data = response.read()
        row.update(status=response.status, final_url=response.url,
                   bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    path = ROOT / "literature/ROOT_Pfluger_current_publisher_app.js"
    path.write_bytes(data)
    row["local_path"] = str(path.relative_to(ROOT))
    source = data.decode("utf-8", "replace")
    # Report only catalogue/API base URL contexts; ignore unrelated assets,
    # tracking configuration, and any account/sign-in implementation.
    pattern = r'.{0,110}(?:baseURL|searchArticles|/public/search|/articles/search|api\.informatics|journals-api).{0,190}'
    contexts = list(dict.fromkeys(re.findall(pattern, source)))
    row["public_search_contexts"] = contexts
except Exception as error:
    row["error"] = repr(error)
row["seconds"] = time.perf_counter() - start
row["completed_utc"] = datetime.now(timezone.utc).isoformat()
(ROOT / "logs/ROOT_Pfluger_public_search_discovery.json").write_text(json.dumps(row, indent=2) + "\n")
print(json.dumps(row, indent=2))
