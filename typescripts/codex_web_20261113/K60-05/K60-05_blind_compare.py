"""Compare blind records with the first-pass collation and the audited page files.

After the witness check, restore the audited reading in memory using only the
recorded witness substitutions. No file in pages/ is modified by this script.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent
def table(name):
    with (ROOT / ("K60-05_" + name + ".tsv")).open(newline="") as fd:
        return list(csv.DictReader(fd, delimiter="\t"))
def norm(s):
    # The TSV transcribes the ink. Use the first candidate, ignoring editorial wrappers.
    while r"\unsure{" in s:
        i = s.index(r"\unsure{")
        begin = i + len(r"\unsure{")
        end, level = begin, 1
        while level:
            ch = s[end]
            level += (ch == "{") - (ch == "}")
            end += 1
        s = s[:i] + s[begin:end-1].split("|")[0] + s[end:]
    s = re.sub(r"\\(?:handwritten|uline|uuline|inserted|deleted|text|margin|boxed)(?![A-Za-z])","",s)
    return re.sub(r"[\s{}&$]", "", s)
def recover_audit():
    pages = {int(p.stem[-3:]): p.read_text() for p in (ROOT / "pages").glob("*.tex")}
    if (ROOT / "K60-05_witness.tsv").exists():
        for rec in reversed(table("witness")):
            n, at = int(rec["scan"]), int(rec["final offset"])
            before, after = rec["frozen token"], rec["final token"]
            assert pages[n][at:at+len(after)] == after, (n, at, after)
            pages[n] = pages[n][:at] + before + pages[n][at+len(after):]
    return pages
def esc(s):
    return s.replace("|",r"\|")
def main():
    blind = table("blind")
    coll = {(a["scan"],a["place"]):a for a in table("collation")}
    pages = {n:norm(txt) for n,txt in recover_audit().items()}
    differences, extra, misses = [], [], []
    assert len(coll) == len(blind)
    for b in blind:
        n, loc, obs = b["scan"], b["place"], b["what the crop shows"]
        c = coll[n,loc]
        first, audited = c["first pass"], c["audited reading"]
        if norm(audited) not in pages[int(n)]:
            misses.append((n,loc,audited))
        row = f"| {n} | {loc} | {esc(first)} | {esc(obs)} | {esc(audited)} | {esc(c['decision'])} |"
        if norm(obs) != norm(first):
            differences.append(row)
        elif norm(obs) != norm(audited):
            extra.append(row)
    hdr = ["| Scan | Place | First pass | Blind crop | Audited page | Decision |",
           "|---|---|---|---|---|---|"]
    lines = ["# Blind comparison","",f"{len(blind)} crop entries across {len(pages)} scans. Anchors are compared with the audited files with editorial wrappers and spacing removed. The first candidate represents the ink reading. The corresponding first-pass excerpts are recorded in the collation TSV. Witness substitutions, if present, are reversed in memory before comparison.","",
             f"## Blind readings differing from the first pass ({len(differences)})","",*hdr,*differences,"",
             f"## Further changes on comparing the crop and the page ({len(extra)})","",*hdr,*extra,"",
             "The visual audit also restored layout on scans 53 (the bracket covering both questioned lines), 54 (three sequences of arrows), 55 (the circled quotient and four leaders), and 57 (two leaders). Those layout features lie outside the short text anchors.","",
             f"Audited anchors located in the page files: {len(blind)-len(misses)}/{len(blind)}."]
    for miss in misses:
        lines.append("Missing anchor: "+repr(miss))
    (ROOT / "K60-05_blind_compare.md").write_text("\n".join(lines)+"\n")
    print(f"{len(blind)} collated; {len(differences)} first-pass differences; {len(extra)} additional; missing {misses}")
    if misses:
        raise SystemExit(1)
if __name__ == "__main__":
    main()

