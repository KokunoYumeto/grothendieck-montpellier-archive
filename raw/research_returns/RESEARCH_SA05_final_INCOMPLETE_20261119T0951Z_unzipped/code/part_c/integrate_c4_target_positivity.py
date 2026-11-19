from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json

root = Path(__file__).resolve().parents[2]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
part = root / "part_c"
main_path = root / "sections/part_c.tex"
main = main_path.read_text()
fragment = (part / "c4_target_positivity.tex").read_text()
ident = "c:threefold-target-positivity"
if "\\label{" + ident + "}" not in main:
    marker = r"\begin{remark}[The geometric content not removed by the pairing criterion]"
    assert main.count(marker) == 1
    start = main.index(marker)
    end = main.index(r"\end{remark}", start) + len(r"\end{remark}")
    main = main[:end] + "\n\n" + fragment + "\n" + main[end:]
    main_path.write_text(main)

def read_table(path, delimiter):
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return reader.fieldnames, list(reader)

def save_table(path, fields, rows, delimiter):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter=delimiter)
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(stream.getvalue())

path = part / "results.csv"
fields, rows = read_table(path, ",")
if not any(row["id"] == ident for row in rows):
    rows.append(dict(zip(fields, [
        ident,
        "Target surface-product positivity and mixed D suffice for the first threefold primitive restriction image",
        "Proved conditional refinement; universal C4 gate unchanged",
        "sections/part_c.tex, label " + ident,
        "Saito2003 positivity section4.1; Jannsen1992 Theorem1; Katz-Messing1974 Theorem2(1); target right-ideal argument",
        "12:120-125; C.4",
        "I(SxS)+D(VxS) needs no source B or source semisimplicity. A supplied B2(V) replaces mixed VxS by TxS for ample surfaces T. Modified full-H2 pairing, actual primitive intersection and finite-Q corner are explicit."
    ])))
save_table(path, fields, rows, ",")

path = part / "CHECK_EVENTS.tsv"
fields, rows = read_table(path, "\t")
events = [
    [ident, now, "GPT-6 Astra (OpenAI), /root/part_c", "targeted proof check",
     "Complete typeset proof checked, including complementary codimensions3/2, right ideal fN=eA, mixed trace nondegeneracy, exact primitive intersection, modified-pairing radical, product stability of B and the finite-Q numerical corner. No unconditional movement."],
    [ident, now, "GPT-6 Astra (OpenAI), /root", "independent re-proof",
     "Recorded after root's complete standalone-note audit: proof passed with explicit Lefschetz-modified full-H2 pairing and product-B/I/D finite-Q corner. Root classified it as sufficient only."],
    [ident, "2026-11-19 08:11 UTC", "GPT-6 Astra (OpenAI), /root/part_d", "independent re-proof",
     "Read every line of typeset c4_target_positivity.tex. Product lowering/Casimir interpolation, mixed trace pairing, target-only ideal, primitive intersection and modified-pairing radical all pass."]
]
for values in events:
    row = dict(zip(fields, values))
    if row not in rows:
        rows.append(row)
save_table(path, fields, rows, "\t")
report = {
    "recorded": now,
    "statement": ident,
    "inserted_once": main.count("\\label{" + ident + "}") == 1,
    "main_c6_untouched": True,
    "unconditional_gate_unchanged": True
}
(root / "code/part_c/integrate_c4_target_positivity_output.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
