"""Retrieve explicitly linked public autobiographical/retrospective PDFs and extract text."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.request
import fitz

BASE = Path(__file__).resolve().parents[1]
SOURCES = [
 ("rets_transcription", "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/RetSbis.pdf"),
 ("rets_firstpart_original", "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/RS0orig.pdf"),
 ("rets_complements_original", "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/G-RS-Compl.pdf"),
 ("esquisse1972_original", "https://csg.igrothendieck.org/wp-content/uploads/2024/10/U10.2.pdf"),
 ("cv1972_original", "https://csg.igrothendieck.org/wp-content/uploads/2024/10/U10.1.pdf"),
 ("rapport1984_original", "https://csg.igrothendieck.org/wp-content/uploads/2026/02/U18.pdf"),
]
started = time.monotonic()
def fetch(entry):
    stem, url = entry
    start = time.monotonic()
    result = {"stem": stem, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            path = BASE / "sources" / ("algebra_history_" + stem + ".pdf")
            path.write_bytes(data)
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), file=str(path))
        doc=fitz.open(path)
        pages=[page.get_text("text") for page in doc]
        text_path=path.with_suffix(".txt")
        text_path.write_text("\n\f\n".join(pages),encoding="utf-8")
        result.update(pages=len(doc), extracted_characters=sum(map(len,pages)),
                      text_file=str(text_path), metadata=doc.metadata)
    except Exception as error:
        result["error"]=repr(error)
    result["seconds"]=round(time.monotonic()-start,6)
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,SOURCES))
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
        "seconds":round(time.monotonic()-started,6),"results":results}
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro34.json").write_text(text+"\n",encoding="utf-8")
print(text)
