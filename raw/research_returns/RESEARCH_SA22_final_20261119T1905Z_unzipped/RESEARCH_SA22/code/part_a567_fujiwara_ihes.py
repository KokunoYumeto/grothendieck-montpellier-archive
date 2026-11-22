#!/usr/bin/env python3
"""Read two ordinary public IHES preprint-catalogue searches; no content bypass."""
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import re
import time

ROOT = Path(__file__).resolve().parents[1]

def run(term):
    # GET action and collection selector observed on IHES's public search form.
    url = "https://archives.ihes.fr/items/browse?" + urlencode({"search": term, "collection": "59"})
    start = time.monotonic()
    result = {"query": term, "url": url}
    try:
        with urlopen(url, timeout=40) as response:
            body = response.read()
            result.update(status=response.status, bytes=len(body))
        path = ROOT / "sources" / ("part_a567_ihes_" + term.lower() + ".html")
        path.write_bytes(body)
        markup = body.decode("utf-8", "replace")
        plain = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", markup, flags=re.I)
        plain = unescape(re.sub(r"<[^>]*>", " ", plain))
        plain = " ".join(plain.split())
        result["visible_text"] = plain
        result["item_links"] = list(dict.fromkeys(re.findall(r'href=["\x27]([^"\x27]*items/show/[^"\x27]*)', markup)))
        result["saved_html"] = str(path.relative_to(ROOT))
    except Exception as error:
        result["error"] = str(error)
    result["elapsed_seconds"] = time.monotonic() - start
    return result

if __name__ == "__main__":
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, ("Fujiwara", "tubular")))
    output = {"purpose": "Original Fujiwara1995 / 1992-preprint source discovery only", "elapsed_seconds": time.monotonic() - start, "results": results}
    (ROOT / "code" / "part_a567_fujiwara_ihes_output.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    for result in results:
        print(json.dumps(result, ensure_ascii=False))
