"""Integrate the independently audited refined-Swan zero estimate."""
from pathlib import Path
import csv
import datetime
import json

WORK = Path(__file__).resolve().parents[1]
section = WORK / "F.tex"
source = (WORK / "F_refined_swan_zeros.tex").read_text()
if r"\subsection{A degree-linear bound for refined-Swan zeros}" not in section.read_text():
    section.write_text(section.read_text() + "\n\n" + source)
path = WORK / "results.csv"
with path.open(newline="") as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
new = dict(id="F13e", statement="Refined-Swan zero length is bounded linearly in the degree of every finite etale resolution cover", status="Proved", where_proved="F_refined_swan_zeros.tex; F.tex", depends_on="F10 refined Swan and residue sequence; F13b cutoff; saturation and projection formula; (-B)t=k", manuscript_pages_settled="58:19", notes="Root full proof audit passed; component bound d_a(-B_ii)(t_i-s_a); total at most d sum_i(-B_ii)t_i; no quantitative cleanup or local Betti conclusion inferred")
if new["id"] not in {row["id"] for row in rows}:
    rows.append(new)
with path.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
report = WORK / "report.md"
paragraph = "\n\nF13e bounds the total zero length of the refined-Swan sections on the original exceptional curves by C times the degree of the finite etale resolution cover. More precisely, a component of degree d_a over C_i and positive Swan coefficient s_a has zero length at most d_a(−B_ii)(t_i−s_a). The proof uses saturation, the same residue sequence as F10, the projection formula, and (−B)t=k. Root independently passed every step. It does not bound the successive cleanup blowups or their cohomology; those remain genuine additional requirements for F13.5/F13.6.\n"
if "F13e bounds the total zero length" not in report.read_text():
    report.write_text(report.read_text() + paragraph)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
checks = WORK / "CHECK_EVENTS.tsv"
if "F13e\t" not in checks.read_text():
    with checks.open("a") as handle:
        handle.write("F13e\t" + now + "\troot\tIndependent full proof audit and promotion\tPASS: saturation zero divisor; residue-sequence maximal line degree; finite-etale scaling; disjoint components; projection formula and sign in (-B)t=k. Quantitative cleanup and F13.5 remain open.\n")
result = dict(timestamp=now, integrated="F13e", status="Proved", F13_5="Undecided", F13_6="Undecided")
(WORK / "output" / "integrate_F13e.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
