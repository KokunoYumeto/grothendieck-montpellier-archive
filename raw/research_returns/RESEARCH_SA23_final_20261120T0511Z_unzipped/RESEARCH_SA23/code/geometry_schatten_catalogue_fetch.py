"""Preserve accessible official catalogue pages once; no denied portal retries."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.request import urlopen
from urllib.error import HTTPError
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.ignored = 0
    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}: self.ignored += 1
    def handle_endtag(self, tag):
        if tag in {"script", "style"}: self.ignored = max(0, self.ignored - 1)
    def handle_data(self, data):
        if not self.ignored and data.strip(): self.parts.append(data.strip())

root = Path(__file__).resolve().parents[1]
sources = [
    ("hunter_finding_aids", "https://library.hunter.cuny.edu/archives/finding-aids"),
    ("hunter_academic_departments", "https://library.hunter.cuny.edu/archives/collection-categories/academic-departments"),
    ("cuny_archives_guide", "https://guides.cuny.edu/archives/")]
started = time.perf_counter()

def fetch(item):
    name, url = item
    record = {"url": url, "started_utc": datetime.now(timezone.utc).isoformat()}
    tick = time.perf_counter()
    try:
        with urlopen(url, timeout=30) as response:
            content = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(content), elapsed_seconds=time.perf_counter()-tick)
        if record["status"] != 200:
            record["stopped_without_retry"] = True
            return record
        source = root / f"sources/geometry_schatten_{name}.html"
        source.write_bytes(content)
        parser = TextParser()
        parser.feed(content.decode("utf-8", errors="replace"))
        text = "\n".join(parser.parts)
        target = source.with_suffix(".txt")
        target.write_text(text)
        record.update(source=str(source.relative_to(root)), sha256=hashlib.sha256(content).hexdigest(), text=str(target.relative_to(root)), target_name_counts={word: text.casefold().count(word) for word in ["schatten", "grothendieck"]})
        if name == "hunter_finding_aids":
            start = text.rfind("Faculty Papers/Collections")
            end = text.find("General Collections", start)
            section = text[start:end]
            excerpt = root / "notes/geometry_schatten_hunter_faculty_section.txt"
            excerpt.write_text(section + "\n")
            record["faculty_section_finding_aid_excerpt"] = str(excerpt.relative_to(root))
        if name == "hunter_academic_departments":
            start = text.find("Mathematics & Statistics Department")
            record["mathematics_entry"] = text[start:start+180]
    except Exception as exc:
        record.update(error=repr(exc), elapsed_seconds=time.perf_counter()-tick, stopped_without_retry=True)
    return record

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(fetch, sources))
result = {"utc": datetime.now(timezone.utc).isoformat(), "records": records, "runtime_seconds": time.perf_counter()-started, "restricted_portals_not_requested": ["https://archives.library.hunter.cuny.edu/", "https://archives.library.gc.cuny.edu/"]}
(root / "logs/geometry_schatten_catalogue_fetch.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
