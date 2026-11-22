"""Retain the exact opened primary source; no theorem is inferred by download."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import urllib.request

root = Path(__file__).resolve().parent.parent
pdf = root / "sources/brock_howe_richelot_2025_v2.pdf"
pdf.parent.mkdir(parents=True, exist_ok=True)
url = "https://arxiv.org/pdf/2002.02122v2"
with urllib.request.urlopen(url, timeout=30) as response:
    payload = response.read()
pdf.write_bytes(payload)
subprocess.run(
    ["pdftotext", "-layout", str(pdf), str(pdf.with_suffix(".txt"))],
    check=True,
)
record = {
    "actual_timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "url": url,
    "path": str(pdf),
    "bytes": len(payload),
    "sha256": hashlib.sha256(payload).hexdigest(),
    "access_scope": "Lemma 2.1 statements and its order-four automorphism proof, printed pages 4–7; statements and short proofs of Lemmas 3.2–3.4, printed page 9. The full main Richelot theorem was not audited.",
    "use_scope": "Source census only. This paper does not supply nodality of odd theta norm images; its purely inseparable isogenies are not substituted for the etale norm-transfer argument.",
}
(root / "outputs/brock_howe_primary_access.json").write_text(
    json.dumps(record, indent=2) + "\n"
)
print(json.dumps(record, indent=2))
