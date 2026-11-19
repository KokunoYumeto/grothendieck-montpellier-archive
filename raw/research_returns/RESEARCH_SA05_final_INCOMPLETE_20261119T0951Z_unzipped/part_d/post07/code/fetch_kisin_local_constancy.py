"""Fetch Kisin's original author DVI and retain exact conversion provenance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parents[2] / "pending_post07_sources_d"
TEXT = BASE / "sources"
OUT = BASE / "output"
for directory in (RAW, TEXT, OUT):
    directory.mkdir(parents=True, exist_ok=True)

url = "https://people.math.harvard.edu/~kisin/dvifiles/locconstpap.dvi"
record = {"name": "Kisin1999LocalConstancy", "url": url,
          "checked_utc": datetime.now(timezone.utc).isoformat()}
try:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 primary-source research"})
    with urllib.request.urlopen(request, timeout=40) as response:
        data = response.read()
        record["resolved_url"] = response.url
    dvi = RAW / "Kisin1999LocalConstancy.dvi"
    pdf = RAW / "Kisin1999LocalConstancy.pdf"
    txt = TEXT / "Kisin1999LocalConstancy.txt"
    dvi.write_bytes(data)
    record.update(status="obtained", path=str(dvi), bytes=len(data),
                  sha256=hashlib.sha256(data).hexdigest())
    conversion = subprocess.run(["dvipdfmx", "-o", str(pdf), str(dvi)],
                                text=True, capture_output=True, check=True)
    record["conversion_stdout"] = conversion.stdout
    record["conversion_stderr"] = conversion.stderr
    subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
    record.update(pdf_path=str(pdf), text_path=str(txt),
                  pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest())
except Exception as error:
    record.update(status="not_obtained", error=f"{type(error).__name__}: {error}")
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "source": record}
(OUT / "kisin_fetch_output.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
