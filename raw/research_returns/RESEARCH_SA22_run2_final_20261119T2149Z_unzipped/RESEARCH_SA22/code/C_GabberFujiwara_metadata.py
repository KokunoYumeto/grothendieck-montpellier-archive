"""Public journal/archive metadata routes for the two requested originals."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import urllib.parse
import urllib.request

targets = {
    "duke_toc_metadata": "https://archive.org/metadata/sim_duke-mathematical-journal_1995_80_contents",
    "israel_collection_metadata": "https://archive.org/metadata/pub_israel-journal-of-mathematics",
    "duke_collection_metadata": "https://archive.org/metadata/pub_duke-mathematical-journal",
}
for label, doi in (("Gabber", "10.1007/BF02773001"),
                   ("Fujiwara", "10.1215/S0012-7094-95-08002-8")):
    targets[label + "_openalex"] = "https://api.openalex.org/works/https://doi.org/" + doi
    targets[label + "_crossref"] = "https://api.crossref.org/works/" + doi
    targets[label + "_fatcat"] = "https://api.fatcat.wiki/v0/release/lookup?" + urllib.parse.urlencode({"doi": doi})
    targets[label + "_scholar_archive"] = "https://scholar.archive.org/search?" + urllib.parse.urlencode({"q": "doi:" + doi})

def fetch(item):
    label, url = item
    result = {"url": url}
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            data = response.read()
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("content-type"), bytes=len(data))
        try:
            result["data"] = json.loads(data)
        except ValueError:
            result["text"] = data.decode("utf-8", "replace")
    except Exception as exc:
        result["error"] = repr(exc)
    return label, result

responses = dict(ThreadPoolExecutor(max_workers=8).map(fetch, targets.items()))
out = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "responses": responses}
root = Path(__file__).resolve().parents[1]
(root / "logs/C_GabberFujiwara_metadata.json").write_text(json.dumps(out, indent=2) + "\n")
for label, r in responses.items():
    short = {k: v for k, v in r.items() if k not in {"data", "text"}}
    data = r.get("data", {})
    if label.endswith("_openalex"):
        short["locations"] = data.get("locations")
        short["open_access"] = data.get("open_access")
    elif label.endswith("_crossref"):
        short["links"] = data.get("message", {}).get("link")
        short["primary"] = data.get("message", {}).get("resource")
    elif label.endswith("_metadata"):
        short["metadata"] = data.get("metadata")
        short["files"] = [{k: f.get(k) for k in ("name", "format", "size", "private")} for f in data.get("files", [])]
    else:
        short["data"] = data
    print(json.dumps({label: short}, ensure_ascii=False))
