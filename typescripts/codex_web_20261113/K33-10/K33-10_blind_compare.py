"""Compare the dated blind record, first-pass excerpts and located final page text."""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read_table(name):
    with (ROOT / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))
def quoted(value):
    return chr(96) + value.replace("\n", " ").replace("|", r"\|") + chr(96)
def normal(value):
    return re.sub(r"\s+", " ", value.replace("’", "'")).strip()

blind = read_table("K33-10_blind.tsv")
anchors = {(row["scan"], row["place"]): row for row in read_table("K33-10_collation.tsv")}
if len(blind) != len(anchors):
    raise ValueError("Blind and located records differ in length")
detail, exact = [], Counter()
independent_differences = 0
for row in blind:
    scan, place, reading = row.values()
    entry = anchors[scan, place]
    page = (ROOT / "pages" / f"K33-10_33_scan{scan}.tex").read_text()
    final = entry.get("final_anchor", entry["audit_anchor"])
    offset = entry.get("final_offset")
    if offset:
        if not page.startswith(final, int(offset)):
            raise ValueError(f"Final anchor moved at {scan}, {place}")
    elif final not in page:
        raise ValueError(f"Final anchor missing at {scan}, {place}")
    first, audit = entry["first_pass_anchor"], entry["audit_anchor"]
    independent_match = normal(reading) == normal(first) == normal(audit)
    independent_differences += not independent_match
    if independent_match and audit == final:
        exact[scan] += 1
        continue
    reason = entry["settlement"].removeprefix("Δ ")
    if audit != final:
        reason += " The later witness disposition appears in the doubts register."
    detail.append("| " + " | ".join([scan, place, quoted(reading), quoted(first), quoted(audit),
                    quoted(final), reason.replace("|", r"\|")]) + " |")
out = ["# Comparison of the blind readings", "",
       f"{len(blind)} located records. {sum(exact.values())} agree as strings after whitespace and apostrophe normalization. The other {len(detail)} records are shown below. A longer anchor can include adjacent words or markup specifying a position, an alphabet, a strike or a range of alternatives. These representation differences are shown alongside disagreements about the ink.",
       "", f"The independent comparison differs in wording, extent or markup at {independent_differences} places. After the witness check the full comparison includes {len(detail) - independent_differences} additional entries. Each row preserves the blind wording and both stages of the collation.",
       "", "The first-pass column was located in each page before the audit edits. The final column is verified against the current page files. The blind TSV preserves the original entries, including two missing spacing-command backslashes on scan 177.",
       "", "| Scan | Place | Blind entry | First-pass excerpt | Independently audited excerpt | Final excerpt | Settlement |",
       "|---|---|---|---|---|---|---|", *detail, ""]
(ROOT / "K33-10_blind_compare.md").write_text("\n".join(out), encoding="utf-8")
