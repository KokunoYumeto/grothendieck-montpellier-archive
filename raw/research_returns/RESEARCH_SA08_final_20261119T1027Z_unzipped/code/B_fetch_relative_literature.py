"""Archive primary sources examined for the C32 local relative-repair gate."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "menichi2001_fiber": "https://arxiv.org/pdf/math/0201134",
    "scheerer_tanre1991_tame": "https://mat.uab.es/pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av35%282%29/FileName%3A35291_05.pdf",
    "scott2005_hopf": "https://msp.org/agt/2005/5-1/agt-v5-n1-p07-p.pdf",
    "anick1989_hopf": "https://www.ams.org/jams/1989-02-03/S0894-0347-1989-0991015-7/S0894-0347-1989-0991015-7.pdf",
    "hanke2009_stable_rank": "https://arxiv.org/pdf/0803.3572",
}

def fetch(item):
    name, url = item
    started = time.perf_counter()
    record = {"name": name, "url": url}
    try:
        existing = ROOT / f"sources/B_{name}.pdf"
        if existing.exists():
            data = existing.read_bytes()
            record.update(status="already_downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pdf=str(existing), txt=str(existing.with_suffix(".txt")))
            record["runtime_seconds"] = time.perf_counter() - started
            return record
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=40) as stream:
            data = stream.read()
            record["resolved_url"] = stream.url
        assert data.startswith(b"%PDF"), "Response is not PDF"
        pdf = ROOT / f"sources/B_{name}.pdf"
        pdf.write_bytes(data)
        txt = pdf.with_suffix(".txt")
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        record.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pdf=str(pdf), txt=str(txt))
    except Exception as exc:
        record.update(status="not_downloaded", error=repr(exc))
    record["runtime_seconds"] = time.perf_counter() - started
    return record

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, SOURCES.items()))
    target = ROOT / "logs/B_relative_literature_fetch.json"
    target.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps(records, indent=2))
