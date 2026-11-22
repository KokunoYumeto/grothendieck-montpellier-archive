"""Preserve three observed public Birman sources; do not request protected chapters."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
import time

root = Path(__file__).resolve().parents[1]
jobs = [
    ("author_list", "https://www.math.columbia.edu/~jb/papers.html", ".html"),
    ("errata", "https://www.math.columbia.edu/~jb/errataBLMCG.pdf", ".pdf"),
    ("preview", "https://api.pageplace.de/preview/DT0400.9781400881420_A26691398/preview-9781400881420_A26691398.pdf", ".pdf"),
]
def fetch(job):
    name, url, suffix = job
    started = datetime.now(timezone.utc).isoformat()
    clock = time.perf_counter()
    record = {"name": name, "url": url, "started_at_utc": started}
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            body = response.read()
            record.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"))
        destination = root / "literature" / ("A567_Birman_" + name + suffix)
        destination.write_bytes(body)
        record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                      saved=str(destination.relative_to(root)))
        if suffix == ".pdf" and body.startswith(b"%PDF"):
            subprocess.run(["pdftotext", "-layout", str(destination), str(destination.with_suffix(".txt"))], check=True)
    except HTTPError as error:
        record.update(http_status=error.code, reason=str(error.reason))
    except Exception as error:
        record.update(error=type(error).__name__, message=str(error))
    record.update(finished_at_utc=datetime.now(timezone.utc).isoformat(),
                  elapsed_seconds=time.perf_counter()-clock)
    return record

clock = time.perf_counter()
started = datetime.now(timezone.utc).isoformat()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch, jobs))
renders = []
qa = root / "qa" / "A567_Birman"
qa.mkdir(exist_ok=True)
for name, page in [("preview",2), ("preview",3), ("preview",10), ("errata",3)]:
    source = root / "literature" / ("A567_Birman_" + name + ".pdf")
    if not source.exists():
        continue
    output = qa / f"{name}_pdfpage_{page}"
    subprocess.run(["pdftoppm", "-f",str(page),"-l",str(page),"-r","130","-png","-singlefile",str(source),str(output)],check=True)
    image = output.with_suffix(".png")
    renders.append({"source":str(source.relative_to(root)), "pdf_page":page,
                    "image":str(image.relative_to(root)),
                    "sha256":hashlib.sha256(image.read_bytes()).hexdigest()})
report = {
    "started_at_utc":started,
    "finished_at_utc":datetime.now(timezone.utc).isoformat(),
    "scope":"Three observed public author/preview sources; no authentication, protected chapter request, or mathematical test",
    "requests_count":len(jobs), "rendered_pages_count":len(renders),
    "elapsed_seconds":time.perf_counter()-clock,
    "results":results,"renders":renders,
}
(root/"logs/A567_Birman_public_sources.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
