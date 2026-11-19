#!/usr/bin/env python3
"""Fetch the primary unsigned shuffle source used in the C24 derivation."""
from pathlib import Path
import hashlib
import json
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
url = "https://reutenauer.math.uqam.ca/wp-content/uploads/2024/04/LyndonWordsFreeAlgebras-Shuffles1989.pdf"
started = time.perf_counter()
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request, timeout=40) as response:
    data = response.read()
assert data.startswith(b"%PDF"), "The response is not a PDF"
target = root / "sources/C_melancon_reutenauer1989.pdf"
target.write_bytes(data)
receipt = {
    "url": url,
    "path": str(target.relative_to(root)),
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "runtime_seconds": time.perf_counter() - started,
    "locator": "Section4, printed589--590; PDF pages13--14",
}
(root / "logs/C_shuffle_source_fetch.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
