"""Fetch supplementary primary-source checks for the residual D1/D2 gate."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import hashlib, json, subprocess, time

root = Path(__file__).resolve().parents[1]
sources = root / "sources"
jobs = [
    ("EsnaultSrinivasBost2014", "https://page.mi.fu-berlin.de/esnault/preprints/helene/113-ES_B.pdf"),
    ("EsnaultKindlerErratum2016", "https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf"),
    ("ACMV2019", "https://www.math.colostate.edu/~achter/math/algrep1119.pdf"),
]

def fetch(job):
    name, url = job
    start = time.monotonic()
    result = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        data = urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=35).read()
        path = sources / (name + ".pdf")
        path.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True)
        result.update(status="downloaded and extracted", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        result.update(status="failed", error=repr(error))
    result["seconds"] = round(time.monotonic() - start, 4)
    return result

with ThreadPoolExecutor(max_workers=3) as pool:
    out = list(pool.map(fetch, jobs))
(root / "code" / "fetch_supplementary_output.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
