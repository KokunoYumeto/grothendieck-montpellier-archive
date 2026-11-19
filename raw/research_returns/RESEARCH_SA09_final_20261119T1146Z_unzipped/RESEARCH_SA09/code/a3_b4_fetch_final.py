"""Record final primary-source access checks; never replace an HTML block by a PDF."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import time
import argparse

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    ("ribet1979_publisher", "https://projecteuclid.org/journals/duke-mathematical-journal/volume-46/issue-4/Kummer-theory-on-extensions-of-abelian-varieties-by-tori/10.1215/S0012-7094-79-04638-6.pdf"),
    ("ribet1979_legacy", "https://projecteuclid.org/download/pdf_1/euclid.dmj/1077313720"),
    ("ribet1979_berkeley", "https://math.berkeley.edu/~ribet/Articles/kummer.pdf"),
    ("bashmakov1972", "https://www.mathnet.ru/links/8fdb68daddc8efc3c5140e6e477fb41f/rm5139_eng.pdf"),
    ("belyi1979_translation", "https://www.mathnet.ru/links/d602ac745ada601583cfc6140ec7c36a/im1682_eng.pdf"),
    ("perucca_sgobba2019", "https://orbilu.uni.lu/bitstream/10993/35969/1/PeruccaSgobba-update.pdf"),
]

def fetch(job):
    name, url = job
    row = {"name": name, "url": url, "started": time.time()}
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"), bytes=len(data),
                       sha256=hashlib.sha256(data).hexdigest())
        row["pdf"] = data.startswith(b"%PDF")
        if row["pdf"]:
            target = ROOT / "sources" / (name + ".pdf")
            target.write_bytes(data)
            row["saved"] = str(target.relative_to(ROOT))
        else:
            row["result"] = "Non-PDF response; primary text not opened by this fetch"
    except Exception as exc:
        row["error"] = f"{type(exc).__name__}: {exc}"
    row["elapsed_seconds"] = round(time.time() - row.pop("started"), 3)
    return row

parser = argparse.ArgumentParser()
parser.add_argument("names", nargs="*")
args = parser.parse_args()
selected = [job for job in JOBS if not args.names or job[0] in args.names]
assert len(selected) == (len(args.names) if args.names else len(JOBS))
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch, selected))
log_name = "a3_b4_fetch_supplement.json" if args.names else "a3_b4_fetch_final.json"
(ROOT / "logs" / log_name).write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
