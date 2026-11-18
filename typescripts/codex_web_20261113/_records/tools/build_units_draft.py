"""A draft map of the archive's natural units, by script (18 Nov 2026, the main session, Claude Opus 5.5 Max).

The user, 18 Nov 2026: "Organizing the natural units is probably smart, just as administrative stuff."
Every Work return (Astra 6.2 Max or Astra 6 Max, template K/K2) has a section "What the pages do" in its mathnotes:
one paragraph per mathematical unit, led by a bold title that names its scans. This script collects those leads, keeps
the scan numbers that belong to the folder (ASSIGNMENTS.tsv), and writes one row per unit. Run A of each folder sets
the final boundaries against the ink (COMPANION_DESIGN_20261118.md sections 2.3, 4.1); this is the administrative draft.
Pro returns (headings without a fixed unit format) are not parsed here.
Writes ../../UNITS_DRAFT_20261118.tsv and prints a summary. Reads the returns' text files only.
usage: python -I -B tools/build_units_draft.py"""
import csv
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
CW = pathlib.Path(__file__).resolve().parent.parent
T = CW.parent
assign = {}
for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t"):
    assign[r["folder"]] = (r["cote"], [int(n) for n in re.findall(r"\d+", r["scans"])])
SEC = re.compile(r"(?is)#+\s*What the pages do\s*\n(.*?)(?=\n#+\s|\Z)")
LEAD = re.compile(r"(?m)^\s*(?:[-*]\s*)?\*\*(.+?)\*\*")

rows, no_section, no_assign = [], [], []
for d in sorted((CW / "returns").iterdir()):
    if not d.is_dir() or "_" in d.name:   # skip second deliveries such as K161-2-06_2
        continue
    fid = d.name
    if fid not in assign:
        no_assign.append(fid)
        continue
    cote, scans = assign[fid]
    files = sorted(d.rglob("*mathnotes*.md"))
    text = files[0].read_text(encoding="utf-8", errors="replace") if files else ""
    m = SEC.search(text)
    if not m:
        no_section.append(fid)
        continue
    allowed = set(scans)
    n = 0
    for lead in LEAD.findall(m.group(1)):
        nums = [int(x) for x in re.findall(r"\b(\d{1,3})\b", lead)]
        found = []
        rng = re.findall(r"\b(\d{1,3})\s*[–—-]\s*(\d{1,3})\b", lead)
        for a, b in rng:
            a, b = int(a), int(b)
            if a in allowed and b in allowed and a <= b:
                found += [s for s in scans if a <= s <= b]
        found += [x for x in nums if x in allowed]
        found = sorted(set(found))
        title = re.sub(r"\b(?:scans?|pp?\.)\s*", "", lead, flags=re.I)
        title = re.sub(r"\b\d{1,3}\s*[–—-]\s*\d{1,3}\b|\b\d{1,3}\b", "", title)
        title = re.sub(r"^[\s·,.:;()M-]+|[\s·,.:;()]+$", "", title)
        title = re.sub(r"\(\s*\)|\s{2,}", " ", title).strip(" ,.;·")
        n += 1
        rows.append(dict(cote=cote, folder=fid, unit=f"{fid}.u{n:02d}",
                         scans=(f"{found[0]}-{found[-1]}" if len(found) > 1 else (str(found[0]) if found else "")),
                         title=title[:160], source=files[0].relative_to(T).as_posix()))

out = T / "UNITS_DRAFT_20261118.tsv"
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["cote", "folder", "unit", "scans", "title", "source"], delimiter="\t",
                       lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
cotes = {}
for r in rows:
    cotes.setdefault(r["cote"], []).append(r)
print(out)
print(f"units drafted: {len(rows)} in {len(cotes)} cotes, from {len({r['folder'] for r in rows})} folders; "
      f"without scans found: {sum(1 for r in rows if not r['scans'])}; folders without the section: {len(no_section)}; "
      f"not in ASSIGNMENTS: {len(no_assign)}")
for c in sorted(cotes, key=lambda c: [int(x) for x in c.split("-")])[:8]:
    print(f"  cote {c}: {len(cotes[c])} units; e.g. {cotes[c][0]['scans']} {cotes[c][0]['title'][:70]}")
