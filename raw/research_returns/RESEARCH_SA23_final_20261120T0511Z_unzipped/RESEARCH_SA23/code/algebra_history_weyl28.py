"""Extract the complete returned Hs 91 displayed child-list, with bounded checks.

The input is the public HTML string returned by GetArchivplanChildrenHtml.
This does not infer the contents of unexamined physical letters.
"""
import csv
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time

BASE = Path(__file__).resolve().parents[1]
start = time.monotonic()
source = BASE / "sources" / "algebra_history_eth_hs91_children.json"
html = json.loads(source.read_text())

class Records(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = None
        self.items = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "a" and data.get("href", "").startswith("#/de/archiv/einheit/"):
            self.active = {"href": data["href"], "text": ""}
    def handle_data(self, data):
        if self.active is not None:
            self.active["text"] += data
    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.active["text"] = " ".join(self.active["text"].split())
            self.items.append(self.active)
            self.active = None

parser = Records()
parser.feed(html)
with (BASE / "notes" / "algebra_weyl_catalogue_children.tsv").open("w") as handle:
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(["public_record_url", "catalogue_call_number_and_title"])
    for item in parser.items:
        writer.writerow(["https://vls.hsa.ethz.ch/client/" + item["href"], item["text"]])
terms = ["groth", "schwartz", "dieud", "choquet", "schauder", "lids", "koethe", "köthe", "schatten", "carleman", "smithies", "trace", "spur", "determin", "eigenwert", "fredholm"]
matches = {term: [item for item in parser.items if term in item["text"].lower()] for term in terms}
record = json.loads((BASE / "sources" / "algebra_history_eth_hs91_record.json").read_text())
report = {
    "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "seconds": time.monotonic() - start,
    "source": str(source),
    "child_links_returned": len(parser.items),
    "catalogue_child_count": record.get("childCount"),
    "matches": matches,
    "method_note": record.get("_metadata",{}).get("inhaltUndInnereOrdnung",{}).get("detailData.ordnungKlassifikation",{}).get("value"),
}
text = json.dumps(report, ensure_ascii=False, indent=2)
(BASE / "logs" / "algebra_history_weyl28.json").write_text(text + "\n")
print(text)
