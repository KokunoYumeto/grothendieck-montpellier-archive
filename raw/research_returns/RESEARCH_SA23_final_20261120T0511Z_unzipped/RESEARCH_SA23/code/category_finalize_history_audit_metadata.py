"""Append current-run source checks without inventing historical check events."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / "notes/category_CHECK_EVENTS.tsv"
events = [
    ["geo-H-history", "2026-11-20", "GPT-6 Astra, inherited effort, crystalline_categories",
     "specific correspondence dating-source check",
     "Read Guichardet2004 pp78–79, Dieudonne11J inventory pp20–21/24–32, Schneps chap3 early-letter discussion, Dieudonne1989 pp299–300, Grothendieck–Serre 1Sep1956 p49, IAS/ETH Weyl collection descriptions. None identifies cote1 trace sheets; ETH full finding aid not opened after errors. notes/category_correspondence_date_audit.md"],
    ["geo-H-history", "2026-11-20", "GPT-6 Astra, inherited effort, crystalline_categories",
     "independent alternative-proof source and implication check",
     "Directly viewed memoir II Remark4 pp20–22: Hilbert spectral map has actual unordered lp target Sigma_(p), so p1 plus finite-rank approximation implies full trace formula. Passage sketches Banach reduction to Hilbert continuity but does not prove that assertion. Checked II pp5–6/13–16/65, AppendixI194–195 and Resume168. notes/category_memoir_continuity_audit.md"],
]
existing = path.read_text(encoding="utf-8")
with path.open("a", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    for row in events:
        if row[-1] not in existing:
            writer.writerow(row)
            print("APPENDED", row[0], row[3])
        else:
            print("ALREADY PRESENT", row[0], row[3])

print("NOTES", "category_correspondence_date_audit.md", "category_memoir_continuity_audit.md")
