"""Retain exact source versions for the local/global and BGV scope checks."""
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

sources = [
    ("ConradGlobalLocal", "https://math.stanford.edu/~conrad/676Page/handouts/localglobal.pdf", "pdf"),
    ("BGV2025Published", "https://air.unimi.it/retrieve/handle/2434/1158162/2787454/10.4171-jems-1634-online-first.pdf", "pdf"),
    ("AGV2025Erratum", "https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/sixfunctor-formalism-for-rigid-analytic-motives-erratum/DD7D56D8B42CCA8A9D41F60E1EF53071", "html"),
    ("KrasnerStacks09EI", "https://stacks.math.columbia.edu/tag/09EI", "html"),
]
records = []
for name, url, kind in sources:
    record = {"name": name, "url": url, "checked_utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 primary-source research"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            record["resolved_url"] = response.url
        path = (RAW if kind == "pdf" else TEXT) / (name + "." + kind)
        path.write_bytes(data)
        record.update(status="obtained", path=str(path), bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest())
        if kind == "pdf":
            target = TEXT / (name + ".txt")
            subprocess.run(["pdftotext", "-layout", str(path), str(target)], check=True)
            record["text_path"] = str(target)
    except Exception as error:
        record.update(status="not_obtained", error=f"{type(error).__name__}: {error}")
    records.append(record)
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "sources": records}
(OUT / "global_local_followup_fetch_output.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
