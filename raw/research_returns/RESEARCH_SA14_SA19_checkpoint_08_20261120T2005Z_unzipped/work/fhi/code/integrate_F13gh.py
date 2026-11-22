"""Reproduce the stable F13g/h integration and the strengthened F13f statement.

The first integration was performed at 2026-11-20 19:56:38 UTC. This script
is idempotent and records subsequent verification times separately.
"""
from pathlib import Path
import csv
import datetime
import json

WORK = Path(__file__).resolve().parents[1]
f = WORK / "F.tex"
g = (WORK / "F_swan_residue_gap.tex").read_text()
if r"\subsection{A residue obstruction and a stronger conductor gap}" not in f.read_text():
    f.write_text(f.read_text() + "\n\n" + g)
corollary = WORK / "F_small_conductor_corollary.tex"
old = corollary.read_text()
new = old.replace("the strict subunit cutoff case", "the cutoff below the characteristic").replace("satisfies $t_i<1$", "satisfies $t_i<p$").replace("Its $p$-primary part has integral\nSwan conductors bounded by $t_i<1$ under F13b; hence all those\nconductors are zero.", "Its $p$-primary part has\nSwan conductors bounded by $t_i<p$ under F13b; F13g then forces\nall those conductors to be zero.").replace("$t_i<1$ always exists", "$t_i<p$ always exists")
if new != old:
    corollary.write_text(new)
    f.write_text(f.read_text().replace(old, new))
path = WORK / "results.csv"
with path.open(newline="") as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row["id"] == "F13f":
        row.update(statement="A post-cover conductor cutoff below p gives uniform finite generation at derived length three", depends_on="F13a/b/g; rank-one residue conductor gap; F9 tame affine cocycles; F12; complement count", notes="Root audit passed; extra hypothesis t_i<p on the fixed post-F10b resolution; earlier t_i<1 criterion sharpened; no assertion such a cover always exists")
new_rows = [
    dict(id="F13g", statement="A negative Swan intersection forces its positive coefficient to be divisible by p; nonzero Swan divisors have maximum coefficient at least p", status="Proved", where_proved="F_swan_residue_gap.tex; F.tex", depends_on="Yatagawa2017Cycle Definition2.1 and formula2.5; Krishna-Majumder Cor9.6/9.7 and Lemma9.11; residue sequence; negative definiteness", manuscript_pages_settled="58:19", notes="Root full proof and exact primary-source audit passed; applies on every finite etale resolution cover"),
    dict(id="F13h", statement="The uniform unramified exponent improves to any e with p^(e+1) greater than the maximal conductor cutoff", status="Proved", where_proved="F_swan_residue_gap.tex; F.tex", depends_on="F13g residue conductor gap; F10 Witt restriction; F13c divisibility; purity", manuscript_pages_settled="58:19", notes="Root audit passed; sharpens the stated sufficient exponent by one p-step where applicable; F13.5 and F13.6 still open"),
]
known = {row["id"] for row in rows}
rows.extend(row for row in new_rows if row["id"] not in known)
with path.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
result = dict(original_integration="2026-11-20 19:56:38 UTC", verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), ids=[row["id"] for row in new_rows], F13f_cutoff="t_i<p", required_citation_present="Lemma~9.11" in g)
(WORK / "output" / "verify_F13gh_integration.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
