"""Preserve the primary sources opened for the D.1/D.2 smallness upgrade."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
items = [
    ("Deglise2014_XXI.pdf", "https://www.numdam.org/item/AST_2014__363-364__529_0.pdf"),
    ("Conrad_An_simple.pdf", "https://kconrad.math.uconn.edu/blurbs/grouptheory/Ansimple.pdf"),
    ("Stacks_0EYG.html", "https://stacks.math.columbia.edu/tag/0EYG"),
    ("Stacks_0BRM.html", "https://stacks.math.columbia.edu/tag/0BRM"),
    ("Stacks_0EXT.html", "https://stacks.math.columbia.edu/tag/0EXT"),
    ("Stein_weak_approximation.html", "https://www.wstein.org/books/ant/ant/node95.html"),
]

def fetch(item):
    name, url = item
    record = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            record["http_status"] = response.status
        path = root / "sources" / name
        if path.suffix == ".pdf":
            assert data.startswith(b"%PDF")
        path.write_bytes(data)
        record.update(path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        if path.suffix == ".pdf":
            result = subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], capture_output=True)
            record["pdftotext_exit"] = result.returncode
    except Exception as error:
        record["error"] = repr(error)
    return record

started = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(fetch, items))
output = {"results": results, "elapsed_seconds": time.perf_counter() - started}
(root / "code" / "fetch_smallness_sources_output.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
