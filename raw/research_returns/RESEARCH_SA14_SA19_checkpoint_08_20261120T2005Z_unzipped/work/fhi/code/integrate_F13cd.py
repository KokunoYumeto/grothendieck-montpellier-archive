"""Idempotently integrate the audited F13c/F13d sufficient reduction."""
from pathlib import Path
import csv
import datetime
import json

WORK = Path(__file__).resolve().parents[1]
source = (WORK / "F_bounded_cyclic_reduction.tex").read_text()
section = WORK / "F.tex"
if r"\subsection{Removing unramified order" not in section.read_text():
    section.write_text(section.read_text() + "\n\n" + source)

path = WORK / "results.csv"
with path.open(newline="") as handle:
    reader = csv.DictReader(handle)
    columns = reader.fieldnames
    rows = list(reader)
new = [
    dict(id="F13c", statement="Uniform bounded p-power ramified order modulo an unramified twist on every finite etale resolution cover", status="Proved", where_proved="F_bounded_cyclic_reduction.tex; F.tex", depends_on="F13b; F10 Witt restriction; proper henselian specialization; Artin-Schreier H2(D,Fp)=0", manuscript_pages_settled="58:19", notes="Root full proof audit passed; same exponent e on every cover; Swan conductors unchanged by the unramified twist"),
    dict(id="F13d", statement="A degree-linear tame-generator bound for cyclic covers of fixed bounded p-power degree suffices for the remaining metabelian coefficient estimate", status="Proved", where_proved="F_bounded_cyclic_reduction.tex; F.tex", depends_on="F13c; F13a; prime-to-coefficient cyclic restriction; tame affine cocycles; Shapiro", manuscript_pages_settled="58:19", notes="Root full proof audit passed; only sufficient reduction proved; geometric bound F13.6 and complete-local Betti bound F13.5 remain Undecided"),
]
existing = {row["id"] for row in rows}
rows.extend(row for row in new if row["id"] not in existing)
with path.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)

report = WORK / "report.md"
paragraph = "\n\nF13c removes unbounded unramified order from the rank-one gate: on every finite etale resolution cover, each p-primary character is an unramified twist of a character of order at most p^e, with one e independent of the cover degree. The proof derives divisibility of unramified p-primary characters from Artin–Schreier H2(D,Fp)=0. F13d gives a complete sufficient reduction to a degree-linear tame-generator bound for cyclic ramified covers of degree at most p^e. Root independently passed the reduction. The latter geometric bound F13.6 remains an explicit unproved hypothesis; neither F13.5 nor derived length three is promoted.\n"
if "F13c removes unbounded" not in report.read_text():
    report.write_text(report.read_text() + paragraph)

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
checks = WORK / "CHECK_EVENTS.tsv"
if "F13c; F13d\t" not in checks.read_text():
    with checks.open("a") as handle:
        handle.write("F13c; F13d\t" + now + "\troot\tIndependent full proof audit and promotion\tPASS: AS H2(D,Fp)=0 gives divisible unramified character group; F13b/F10 give uniform e; cyclic restriction, tame affine cocycles and Shapiro give sufficient reduction. F13.6 remains an unproved geometric bound.\n")
result = dict(timestamp=now, integrated_rows=[row["id"] for row in new], F13_6="Undecided", F13_5="Undecided")
output = WORK / "output" / "integrate_F13cd.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
