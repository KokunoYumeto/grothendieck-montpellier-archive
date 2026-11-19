"""Archive the opened primary finiteness source for the invariant audit."""
from pathlib import Path
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
url = "https://www.college-de-france.fr/sites/default/files/media/document/2023-11/Jean-Pierre%20Serre_Groupes%20d%27homotopie%20et%20classes%20de%20groupes%20ab%C3%A9liens.pdf"
started = time.perf_counter()
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request, timeout=45) as stream:
    data = stream.read()
assert data.startswith(b"%PDF")
pdf = root / "sources/B_serre1953_classes.pdf"
pdf.write_bytes(data)
txt = root / "sources/B_serre1953_classes.txt"
subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
receipt = {
    "url": url,
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "runtime_seconds": time.perf_counter() - started,
    "opened_scope": "Chapter I section6.1 p264; Chapter II section6 Proposition8 p271, with Proposition7A pp270-271.",
    "claim_used": "K(A,n) has finitely generated integral homology in each degree for finitely generated abelian A.",
}
(root / "logs/B_serre1953_fetch.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt))
