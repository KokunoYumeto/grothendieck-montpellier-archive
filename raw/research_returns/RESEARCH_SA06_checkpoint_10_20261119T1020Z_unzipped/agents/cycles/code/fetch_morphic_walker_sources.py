"""Preserve the primary sources used in the morphic-AJ obstruction audit."""
from pathlib import Path
import datetime, hashlib, json, subprocess, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Walker2007": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4A44146CE680F4F3C857048FDEDD9F48/S0010437X07002278a.pdf/the-morphic-abel-jacobi-map.pdf",
    "Ayoub2009Report": "https://user.math.uzh.ch/ayoub/Other-PDF/N-MSH.PDF",
    "Friedlander2000": "https://www.numdam.org/item/10.5802/aif.1785.pdf",
    "Friedlander2000Author": "https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/17.pdf",
}
results = []
for name, url in SOURCES.items():
    item = {"name": name, "url": url}
    try:
        target = ROOT / "sources" / (name + ".pdf")
        if target.exists():
            data = target.read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=55) as response:
                data = response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("The response is not a PDF")
        target.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(target), str(target.with_suffix(".txt"))], check=True)
        item.update(status="opened_downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), path=str(target))
    except Exception as error:
        item.update(status="failed", error=repr(error))
    results.append(item)
record = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "sources": results}
(ROOT / "output" / "fetch_morphic_walker_sources.json").write_text(json.dumps(record, indent=2))
print(json.dumps(record, indent=2))
