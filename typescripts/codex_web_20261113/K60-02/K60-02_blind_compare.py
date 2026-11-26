"""Compare the crop record with the page excerpts verified before audit edits."""
import argparse
import csv
from pathlib import Path
import re

root = Path(__file__).resolve().parent
prefix = "K60-02_"
def rows(name):
    with (root / (prefix + name)).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))

def primary(text):
    # Keep nested TeX groups intact and compare the leading ink candidate.
    while r"\unsure{" in text:
        start = text.rindex(r"\unsure{")
        i = start + len(r"\unsure{")
        depth, split = 0, None
        for j in range(i, len(text)):
            ch = text[j]
            if ch == "}" and depth == 0: break
            if ch == "|" and depth == 0 and split is None: split = j
            if ch == "{": depth += 1
            if ch == "}": depth -= 1
        text = text[:start] + text[i:split if split is not None else j] + text[j+1:]
    return re.sub(r"\s+", "", text.replace("$", ""))

def code(text):
    return "<code>" + text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("|","&#124;") + "</code>"

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--verify-first",type=int,help="verify excerpts in this page before audit edits")
args = parser.parse_args()
blind = {(int(r["scan"]), r["place"]):r["what_the_crop_shows"] for r in rows("blind.tsv")}
source = {(int(r["scan"]), r["place"]):r for r in rows("blind_sources.tsv")}
if args.verify_first:
    page = (root/"pages"/f"K60-02_60_scan{args.verify_first:03}.tex").read_text()
    page = re.sub(r"\s+", " ", page)
    for key,r in source.items():
        if key[0] == args.verify_first:
            assert key in blind, key
            assert re.sub(r"\s+", " ",r["first_pass_excerpt"]) in page, (key,r["first_pass_excerpt"])
    exit()
assert blind.keys() == source.keys(), set(blind) ^ set(source)
pages = {n: (root / "pages" / f"K60-02_60_scan{n:03}.tex").read_text() for n in range(14,25)}
out = ["# Blind comparison", "", "The comparison uses the first-pass excerpts checked before each audit correction. Every record is also located in the delivered page file. The final column gives that line and its exact text, including any subsequent witness decision. For the paper punctures it gives the surviving head of the page. The comparison ignores whitespace, math-mode delimiters and secondary uncertainty candidates.", "", "| Scan | Place | Crop reading | First-pass excerpt | Audit settlement | Final page and line |","|---|---|---|---|---|---|"]
changes = 0
for (n,k),b in blind.items():
    s = source[n,k]
    page = pages[n]
    anchor = s["final_page_anchor"]
    pattern = r"\s+".join(map(re.escape,anchor.split()))
    hits = list(re.finditer(pattern,page))
    assert len(hits) == 1, (n,k,"final anchor missing or repeated")
    first = 1 + page.count("\n",0,hits[0].start())
    last = 1 + page.count("\n",0,hits[0].end())
    assert (first,last) == (int(s["first_page_line"]),int(s["last_page_line"])), (n,k,"final line moved")
    if s["old_excerpt_absent"] == "yes":
        assert s["first_pass_excerpt"] not in page, (n,k,"removed text reappeared")
    if primary(b) != primary(s["first_pass_excerpt"]):
        changes += 1
        line = str(first) if first == last else f"{first}–{last}"
        out.append(f'| {n} | {k} | {code(b)} | {code(s["first_pass_excerpt"])} | {s["settlement"]} | {line} · {code(anchor)} |')
out.extend(["",f"{len(blind)} crop records compared. {changes} differences. All {len(blind)} final locations verified against the page files.",""])
(root/(prefix+"blind_compare.md")).write_text("\n".join(out),encoding="utf-8")
