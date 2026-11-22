"""Integrate root-audited F13f and BCE's I7b without changing open parent gates."""
from pathlib import Path
import csv
import datetime
import json

WORK = Path(__file__).resolve().parents[1]
f = WORK / "F.tex"
if r"\begin{corollary}[F13f:" not in f.read_text():
    f.write_text(f.read_text() + "\n\n" + (WORK / "F_small_conductor_corollary.tex").read_text())
i = WORK / "I.tex"
input_line = r"\input{work/bce/I_strict_dense_columns.tex}"
if input_line not in i.read_text():
    i.write_text(i.read_text() + "\n\n" + input_line + "\n")

p = WORK / "results.csv"
with p.open(newline="") as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
new = [
    dict(id="F13f", statement="The strict subunit post-cover conductor cutoff gives uniform finite generation at derived length three", status="Proved", where_proved="F_small_conductor_corollary.tex; F.tex", depends_on="F13a/b; integral rank-one Swan; F9 tame affine cocycles; F12; complement count", manuscript_pages_settled="58:19", notes="Root audit passed; extra hypothesis t_i<1 on the fixed post-F10b resolution; no assertion that such a cover always exists and no arbitrary solvable extrapolation"),
    dict(id="I7b", statement="Residual Hom-column differentials have open dense image without assuming the regular local ring complete", status="Proved", where_proved="work/bce/I_strict_dense_columns.tex; I.tex", depends_on="I6 density; finite Ext annihilator correction; product topology on whole source columns", manuscript_pages_settled="43:64-66", notes="BCE proof and root independent audit passed; arbitrary-target extension is conditional on preceding-degree continuity; whole-family continuity and endpoint assembly remain open"),
]
known = {row["id"] for row in rows}
rows.extend(row for row in new if row["id"] not in known)
with p.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

report = WORK / "report.md"
paragraphs = [
    "F13f records the strict subunit cutoff subclass: if every t_i is less than one on the fixed post-F10b resolution, integer rank-one Swan conductors force the induced systems tame, closing the coefficient bound and derived-length-three case in that subclass. Root passed the proof. No claim that the numerical hypothesis is automatic is made, and this corollary is not a separate formal-review movement.",
    "I7b, proved by BCE and independently passed by root, removes completeness from the open dense image assertion for residual Hom columns, including whole products of source columns. The arbitrary-target extension statement remains conditional on continuity in the preceding degree. The broad topological universal presentation is still Undecided; this result does not silently replace that missing premise."
]
for paragraph in paragraphs:
    if paragraph.split(",")[0] not in report.read_text():
        report.write_text(report.read_text() + "\n\n" + paragraph + "\n")
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
checks = WORK / "CHECK_EVENTS.tsv"
events = [
    ("F13f", "root", "PASS under stated strict t_i<1 hypothesis: integer Swan zero, tame unramified induction, semisimple wild inertia for ell not p, affine cocycles, F12 composition series; no general-F promotion."),
    ("I7b", "BCE; root", "BCE proof and root independent audit PASS: openness onto the existing image uses its existing preimage and needs no completeness; product columns open and dense. Prior-degree continuity and endpoint assembly retained as open premises.")
]
for ident, author, outcome in events:
    if ident + "\t" not in checks.read_text():
        with checks.open("a") as handle:
            handle.write(ident + "\t" + now + "\t" + author + "\tIndependent proof audit and integration\t" + outcome + "\n")
result = dict(timestamp=now, integrated=[row["id"] for row in new], broad_I="Undecided", general_F13_5="Undecided")
(WORK / "output" / "integrate_F13f_I7b.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
