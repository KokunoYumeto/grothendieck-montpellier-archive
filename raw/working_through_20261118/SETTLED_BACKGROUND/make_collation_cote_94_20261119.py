"""Write the 94/004 l.19 reading in second-pass form, beside the verdict, for cote 94's next second pass.

The collation list of the second-pass template (second_pass_pro_20261114/SECOND_PASS_TWO_WITNESSES_TEMPLATE.md, output
3): one row per place where witness H's reading differs from the consolidated reading, columns `folder, their_page,
our_scan, line, their_reading, our_first_pass, final_reading, scan_shows, kind, marked_in_H, confidence`.
The verdict on OBJ_H035 (section 2, row 5; check event READINGS 94/004.19-20) read the place on the scan: "non nul" is
inserted before B. Our first reading (Work, K94-01) has it; witness H (Commutator project, commit aef7db2,
transcripts/94/batch-01.fr.tex) omits it.
usage: python -I -B make_collation_cote_94_20261119.py
Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026.
"""
import csv
import pathlib
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
WT = HERE.parent
OUT = WT / "PILOT_VERDICT_OBJ_H035_20261119_COLLATION_cote94.tsv"
Z = WT / "batch_20261119/033_WT_94_002-013_B/WTB_94_002-013_witnesses.zip"
COLS = ["folder", "their_page", "our_scan", "line", "their_reading", "our_first_pass", "final_reading", "scan_shows",
        "kind", "marked_in_H", "confidence"]


def line_with(text, key):
    return next(x.strip() for x in text.splitlines() if key in x)


with zipfile.ZipFile(Z) as zf:
    ours = zf.read("first/K94-01/94_scan004.tex").decode("utf-8")
    hua = zf.read("hua/transcripts/94/batch-01.fr.tex").decode("utf-8")
o = line_with(ours, "Pour tout quotient")
h = line_with(hua, r"\item[(iv)] Pour tout quotient")
assert "\\inserted{non nul}" in o and "non nul" not in h
row = dict(folder="94", their_page="3", our_scan="4", line="19", their_reading=h, our_first_pass=o, final_reading=o,
           scan_shows=("\"non nul\" written small under \"lim\" on the line above, with a curved leader down to B in "
                       "\"Pour tout quotient B de A\"; the same gesture as the \"non nul\" over B in Théorème 12 (vi) on "
                       "scan 16 (the verdict on OBJ_H035, Claude Opus 5.5 at effort max, 19 Nov 2026, section 2 row 5, "
                       "read on the crop; check event READINGS 94/004.19-20)"),
           kind="omission", marked_in_H="no", confidence="high")
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerow(row)
print(OUT.name, "written:", row["their_reading"][:80], "|", row["final_reading"][:80])
