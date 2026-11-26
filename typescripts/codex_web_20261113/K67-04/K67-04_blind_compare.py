"""Compare the independent crop readings with the first and final page texts.

Run from any directory with Python 3. The TSV of manual settlements adjudicates
genuine reading differences. Written-out symbols and visual descriptions in the
blind record often have no word-for-word equivalent in the LaTeX.
"""
import csv
import hashlib
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

root = Path(__file__).resolve().parent
base = "K67-04"

def rows(suffix):
    with (root / (base + suffix)).open(newline="") as source:
        return list(csv.DictReader(source, delimiter="\t"))

def cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ")

def mdrow(*items):
    return "| " + " | ".join(map(cell, items)) + " |"

def tokens(value):
    # Preserve accents and letter case. Convert only notation/typography here.
    words = {
        "nu":"ν", "sigma":"σ", "Sigma":"Σ", "partial":"∂", "in":"∈",
        "geq":"≥", "leq":"≤", "times":"×", "subset":"⊂", "cap":"∩",
        "cup":"∪", "simeq":"≃", "lambda":"λ", "longrightarrow":"→",
        "to":"→", "longmapsto":"↦", "smallsetminus":"∖", "setminus":"∖",
        "mathbb":"", "mathcal":"", "mathrm":"", "operatorname":"",
        "text":"", "inserted":"", "deleted":"", "unsure":"", "uline":"",
        "uuline":"", "margin":"", "mspage":""
    }
    for source,dest in {"ℝ":"R","ℂ":"C","𝔻":"D","ℙ":"P","’":"'","′":"'","–":"-","−":"-"}.items():
        value = value.replace(source,dest)
    value = re.sub(r"\\([A-Za-z]+)", lambda m: " " + words.get(m[1], m[1]) + " ", value)
    return re.findall(r"[^\W_]+|[=+×≥≤↦→≃∂∩∪⊂∈]",value)

def compare(blind, page):
    a,b = tokens(blind),tokens(page)
    blocks = SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks()
    hit = set()
    for i,_,size in blocks:
        hit.update(range(i,i+size))
    i,_,size = max(blocks,key=lambda block:block.size)
    anchor = " ".join(a[i:i+size]) if size else "—"
    unmatched = " ".join(word for j,word in enumerate(a) if j not in hit)
    return anchor, unmatched or "—", f"{len(hit)}/{len(a)}"

blind = rows("_blind.tsv")
locations = {(r["scan"],r["place"]):r for r in rows("_blind_locations.tsv")}
settled = {(r["scan"],r["place"]):r for r in rows("_blind_settlements.tsv")}
assert set(settled) <= set(locations)
assert {(r["scan"],r["place"]) for r in blind} == set(locations)
report = [
    "# Blind reading and settlement", "",
    f"{len(blind)} regions were recorded from the images before the corresponding page file was reopened. "
    f"The two readings differed in {len(settled)} regions. Each disagreement is listed below, "
    "including cases where the first reading stood after another look at the ink.", "",
    "The first table for each scan records the human decision at audit. Some of its readings changed later "
    "at the witness check. The final alignment section compares the blind words and symbols against the "
    "first-pass region and against the current page file. Compressed visual descriptions, alternative signs, "
    "abbreviations and the scope of a cancellation require a human decision.", ""
]
details = defaultdict(list)
alignment = []
changed_regions = []
for entry in blind:
    key = entry["scan"],entry["place"]
    place = locations[key]
    a,b = int(place["first_line"]),int(place["last_line"])
    page = root/"pages"/f"{base}_67_scan{int(key[0]):03}.tex"
    lines = page.read_text().splitlines()
    assert 1 <= a <= b <= len(lines)
    current = " ".join(s for s in lines[a-1:b] if s and not s.startswith("%"))
    assert current
    observed = entry["what the crop shows"]
    original = place["first_pass_region"]
    old_anchor,missing,old_hits = compare(observed,original)
    new_anchor,_,new_hits = compare(observed,current)
    valid = hashlib.sha256(current.encode("utf-8")).hexdigest() == place["reviewed_final_sha256"]
    if not valid:
        changed_regions.append(mdrow(*key, f"{a}–{b}", current))
    if key in settled:
        d = settled[key]
        details[key[0]].append(mdrow(key[1],observed,d["first_pass_excerpt"],d["final_audit_excerpt"],d["settlement"]))
    extent = str(a) if a==b else f"{a}–{b}"
    alignment.append(mdrow(*key,extent,old_anchor,missing,old_hits,new_anchor,new_hits,
                           "reviewed" if valid else "changed since review"))
for scan, group in details.items():
    report.extend(["", "## Scan "+scan, "",
        "| Place | Blind reading | First reading, local excerpt | Reading at audit | Settlement on the ink |",
        "|---|---|---|---|---|", *group])
report.extend(["", "## Reproducible page-file alignment", "",
    "Token coverage counts the tokens of the blind entry aligned in order with the corresponding page-file span. "
    "Accents and case are retained. The common run and unmatched tokens are diagnostic aids. "
    "A repeated word in another part of the span is not proof that the two readings agree. "
    "The last column checks whether the current region still has its reviewed final checksum.", "",
    "| Scan | Place | Final TeX lines | Longest shared run, first pass | Blind tokens outside aligned runs, first pass | First coverage | Longest shared run, final | Final coverage | Current span |",
    "|---|---|---:|---|---|---:|---|---:|---|", *alignment])
if changed_regions:
    report.extend(["", "## Page-file regions changed since review", "",
                   "| Scan | Place | Lines | Current text |","|---|---|---|---|",*changed_regions])
(root/(base+"_blind_compare.md")).write_text("\n".join(report)+"\n")
print(f"{len(blind)} regions compared, {len(settled)} adjudicated differences, {len(changed_regions)} spans changed since review.")
