"""Read-only bibliographic/archive retrieval, with no authenticated requests.

Run from RESEARCH_SA22.  This records metadata and response status, not a claim
that the chapter itself has been opened.  An empty/blocked route is retained.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import urllib.error
import urllib.request

TARGETS = {
    "ia_isbn": "https://archive.org/advancedsearch.php?q=isbn%3A9780821853405&output=json",
    "ia_title": "https://archive.org/advancedsearch.php?q=title%3A%28Quasiconformal+Mappings%29+AND+year%3A2012&output=json",
    "openlibrary_isbn": "https://openlibrary.org/isbn/9780821853405.json",
    "openalex": "https://api.openalex.org/works/https://doi.org/10.1090/conm/575/11411",
    "crossref": "https://api.crossref.org/works/10.1090/conm/575/11411",
    "googlebooks": "https://www.googleapis.com/books/v1/volumes/pvKdD74g6UEC",
    "hathitrust": "https://catalog.hathitrust.org/api/volumes/brief/isbn/9780821853405.json",
    "semantic_scholar": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/conm/575/11411?fields=title,openAccessPdf,url",
    "wayback_him_cdx": "https://web.archive.org/cdx/search/cdx?url=him.uni-bonn.de%2F*2010b30*&output=json&filter=statuscode%3A200&collapse=urlkey",
    "wayback_author_cdx": "https://web.archive.org/cdx/search/cdx?url=www.math.cornell.edu%2F~earle%2F*&output=json&filter=mimetype%3Aapplication%2Fpdf&filter=statuscode%3A200&collapse=urlkey",
}

def get(item):
    key, url = item
    entry = {"url": url}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AcademicSourceAudit/1.0"})
        with urllib.request.urlopen(request, timeout=18) as response:
            content = response.read()
            entry.update(status=response.status, final_url=response.url,
                         content_type=response.headers.get("content-type"), bytes=len(content))
        try:
            entry["response_json"] = json.loads(content)
        except ValueError:
            entry["response_text"] = content.decode("utf-8", "replace")[:20000]
    except Exception as exc:
        entry["error"] = repr(exc)
    return key, entry

with ThreadPoolExecutor(max_workers=6) as executor:
    responses = dict(executor.map(get, TARGETS.items()))
record = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
          "purpose": "Independent archive/library route to original Earle--Marden 2012 chapter",
          "chapter_opened": False, "responses": responses}
out = Path("logs/C_EarleMarden_retrieval_metadata.json")
out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
for key, entry in responses.items():
    compact = {k: v for k, v in entry.items() if k not in {"response_json", "response_text"}}
    data = entry.get("response_json", {})
    if key == "openalex":
        compact["locations"] = data.get("locations")
        compact["open_access"] = data.get("open_access")
    elif key == "crossref":
        compact["link"] = data.get("message", {}).get("link")
    elif key == "googlebooks":
        compact["accessInfo"] = data.get("accessInfo")
    elif key.startswith("ia_"):
        compact["response"] = data.get("response")
    else:
        compact["data"] = data
    print(json.dumps({key: compact}, ensure_ascii=False))
print(str(out))
