"""Record actual visual inspection of assigned final-guide pages 28--54.

Rendering and extracted text do not count as inspection.  The record command
accepts only pages actually opened and inspected, with page-specific notes.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

P = Path(__file__).resolve().parents[1]
R = P / "records"
parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["next", "record"])
parser.add_argument("--limit", type=int, default=6)
args = parser.parse_args()
selection = json.loads((R / "QA_SELECTION_PS_GUIDE.json").read_text())
pdf = P / selection["pdf"]
digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest == selection["pdf_sha256"], "Guide changed since selection."
target = R / "FINAL_VISUAL_QA_guide_134_3_4.json"
evidence = json.loads(target.read_text()) if target.exists() else {
    "pdf": selection["pdf"], "pdf_sha256": digest, "entries": []}
assert evidence["pdf_sha256"] == digest, "Evidence concerns another snapshot."
by_page = {r["page"]: r for r in selection["selections"] if 28 <= r["page"] <= 54}
assert set(by_page) == set(range(28, 55)), "Assigned guide selection incomplete."
entries = evidence["entries"]
if args.command == "record":
    for item in json.load(sys.stdin):
        assert item.get("viewed") is True, "Affirm actual image inspection."
        page = item["page"]
        assert page in by_page, ("Page outside assignment", page)
        observation = item["observation"].strip()
        assert observation, ("Missing specific observation", page)
        row = by_page[page]
        image = P / row["image"]
        assert image.exists(), ("Missing rendered image", row["image"])
        entry = {
            "pdf": selection["pdf"], "pdf_sha256": digest, "page": page,
            "image": row["image"],
            "image_sha256": hashlib.sha256(image.read_bytes()).hexdigest(),
            "key": row["key"], "viewed": True, "observation": observation}
        entries[:] = [x for x in entries if x["page"] != page]
        entries.append(entry)
    entries.sort(key=lambda x: x["page"])
    target.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")
done = {x["page"] for x in entries if x.get("viewed") is True}
remaining = [by_page[p] for p in sorted(by_page) if p not in done]
print(json.dumps({"reviewed": len(done), "selected": len(by_page),
                  "remaining": len(remaining), "next": remaining[:args.limit]},
                 ensure_ascii=False, indent=2))
