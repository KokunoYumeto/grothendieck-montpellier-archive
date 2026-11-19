"""Archive primary follow-up sources; exact read scope is in the audit note."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parents[2] / "pending_post06_sources_d"
TEXT = BASE / "sources"
OUT = BASE / "output"
for directory in (RAW, TEXT, OUT):
    directory.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ("AyoubGallauerVezzani2022", "https://user.math.uzh.ch/ayoub/PDF-Files/AGV.pdf"),
    ("Ayoub2014Etale", "https://smf.emath.fr/download/pdf/44402"),
    ("Park2024LogNearby", "https://arxiv.org/pdf/2405.14083"),
    ("GabberZavyalovAlgebraization", "https://bogdanzavyalov.com/refs/papers/artin-grothendieck-vanishing.pdf"),
]

def fetch(source):
    name, url = source
    record = {"name": name, "url": url, "checked_utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 primary-source research"})
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
            record["resolved_url"] = response.url
        path = RAW / (name + ".pdf")
        path.write_bytes(data)
        target = TEXT / (name + ".txt")
        subprocess.run(["pdftotext", "-layout", str(path), str(target)], check=True)
        record.update(status="obtained", path=str(path), text_path=str(target), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        record.update(status="not_obtained", error=f"{type(error).__name__}: {error}")
    return record

with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(fetch, SOURCES))
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "sources": records}
(OUT / "bgv_followup_fetch_output.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
