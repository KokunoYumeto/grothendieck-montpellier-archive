"""Preserve the opened author version and an exact acquisition manifest."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request

root = Path(__file__).resolve().parents[2]
target = root / "part_c" / "sources" / "taylor_yoshida2006_author.pdf"
url = "https://virtualmath1.stanford.edu/~rltaylor/monod2.pdf"
request = urllib.request.Request(url, headers={"User-Agent": "Research source archive"})
with urllib.request.urlopen(request, timeout=40) as response:
    data = response.read()
assert data.startswith(b"%PDF"), "The primary endpoint did not return a PDF"
target.write_bytes(data)
textfile = target.with_suffix(".txt")
subprocess.run(["pdftotext", "-layout", str(target), str(textfile)], check=True)
record = {
    "retrieved_utc": datetime.now(timezone.utc).isoformat(),
    "url": url,
    "local_pdf": str(target.relative_to(root)),
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "local_text": str(textfile.relative_to(root)),
    "opened_scope": "Section1 WD and weight definitions; Lemma1.4 complete proof, author pp6-7.",
    "not_claimed": "No audit of the full automorphic theorem or the entire paper.",
}
output = Path(__file__).with_name("fetch_taylor_yoshida_source_output.json")
output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
