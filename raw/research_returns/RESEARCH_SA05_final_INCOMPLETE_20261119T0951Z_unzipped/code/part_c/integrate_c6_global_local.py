from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json
import re

root = Path(__file__).resolve().parents[2]
part = root / "part_c"
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
source = root / "part_d/c6_global_local_reduction.tex"
fragment = source.read_text()
assert "in either the algebraic homological category" in fragment
assert "Finite direct sums of different homogeneous weights" in fragment
main_path = root / "sections/part_c.tex"
main = main_path.read_text()
marker = r"\begin{remark}[The remaining general-motive claim]"
assert main.count(marker) == 1
if r"\label{c:local-global-motive-approximation}" not in main:
    main = main.replace(marker, fragment + "\n\n" + marker, 1)
main_path.write_text(main)

bib_path = part / "references.bib"
bib = bib_path.read_text()
donor = (root / "part_d/c6_general_sources.bib").read_text()
keys = ["c_kisin1999localconstancy", "c_conrad_localglobal", "c_bgv2024monodromy"]
for key in keys:
    if re.search(r"(?m)^@\w+\{" + re.escape(key) + r",", bib):
        continue
    found = re.search(r"(?ms)^@\w+\{" + re.escape(key) + r",.*?(?=^@|\Z)", donor)
    assert found, key
    bib += "\n\n" + found.group().strip() + "\n"
bib_path.write_text(bib)

def read_table(path, delim):
    with path.open(newline="") as f:
        r = csv.DictReader(f, delimiter=delim)
        return r.fieldnames, list(r)

def save_table(path, fields, rows, delim):
    s = io.StringIO(newline="")
    w = csv.DictWriter(s, fieldnames=fields, delimiter=delim)
    w.writeheader()
    w.writerows(rows)
    path.write_text(s.getvalue())

new = [
    ("c:local-global-motive-approximation",
     "Any finite collection of local realizations of a homogeneous algebraic homological or Andre motive is realized by one number-field motive with exact completion",
     "Proved globalization reduction; general independence remains unresolved",
     "Kisin1999 Theorem5.1 and Proposition5.2; Conrad Theorem2.1; finite inverse presentation; etale-chart density",
     "Universal number-field unramifiedness independence is equivalent to the finite-p-adic-field assertion in these categories. Only a finite set of coefficient primes is preserved; no arbitrary absolute-Hodge spread is asserted."),
    ("c:bgv-pure-local-boundary",
     "Globalization is removed after a pure local realization, but compact analytic square-zero monodromy still requires purity",
     "Proved scope boundary; converse rank conjecture unresolved",
     "c:local-global-motive-approximation; Binda-Gallauer-Vezzani Corollary4.14",
     "Compact analytic or mixed algebraization does not supply a pure motive or a pure family preserving the ramification flag. No all-prime approximation or converse theorem is claimed."),
]
path = part / "results.csv"
fields, rows = read_table(path, ",")
for ident, statement, status, depends, notes in new:
    if not any(row["id"] == ident for row in rows):
        rows.append(dict(zip(fields, [
            ident, statement, status, "sections/part_c.tex, label " + ident,
            depends, "12:140; C.6", notes
        ])))
save_table(path, fields, rows, ",")

path = part / "CHECK_EVENTS.tsv"
fields, events = read_table(path, "\t")
records = []
for ident, *_ in new:
    records.extend([
        [ident, now, "GPT-6 Astra (OpenAI), /root/part_c", "targeted proof check",
         "Read complete final written fragment: regular spread, projected lisse lattice, finite-prime Kisin neighborhoods, etale algebraic parameter point, exact completion, homogeneous comparison and mixed-weight direct sums pass. Independent source reading: complete Kisin5.1/5.2 proof and Conrad2.1 proof."],
        [ident, now, "GPT-6 Astra (OpenAI), /root", "independent re-proof",
         "Recorded after root's full written audit and direct primary Kisin pp16-17 check; global/local proof passed. The pure local realization gap remains and the result is not pre-counted as universal gate movement."],
    ])
records.append([
    "c:threefold-target-positivity", "2026-11-19 08:16 UTC",
    "GPT-6 Astra (OpenAI), /root", "independent re-proof",
    "Root read the full typeset c4_target_positivity.tex, not only the earlier note. Right ideal, finite-Q corner, actual intersection, modified pairing, radical contradiction and typed surface retraction passed."
])
for values in records:
    record = dict(zip(fields, values))
    if record not in events:
        events.append(record)
save_table(path, fields, events, "\t")

path = part / "sources.tsv"
fields, rows = read_table(path, "\t")
entries = [
    ["c_kisin1999localconstancy",
     "opened original author DVI and converted primary text; complete relevant proof read",
     "https://people.math.harvard.edu/~kisin/dvifiles/locconstpap.dvi",
     "Theorem5.1 authorp16; complete Proposition5.2 and proof of5.1 pp16-18. C independently read retained primary text; D obtained and hashed original DVI; root directly checked primary pp16-17. Applied to projected lisse lattice and finite primes only."],
    ["c_conrad_localglobal",
     "opened original author handout; complete Theorem2.1 proof read",
     "https://math.stanford.edu/~conrad/676Page/handouts/localglobal.pdf",
     "Theorem2.1 pp2-3; separable Krasner approximation yields a dense number subfield with prescribed completion. C opened refs turn711289121view0 and turn205705753view0 and read proof; D independently read."],
    ["c_bgv2024monodromy",
     "opened original arXivv2; complete relevant proofs checked by D with precise scope",
     "https://arxiv.org/pdf/2306.05099v2",
     "Corollary4.14 p32 and surrounding Propositions4.10/4.13; compactness Lemmas2.13/2.17 and Proposition2.32; Proposition4.25 p34; Corollary4.33 p36; Remark4.61 pp42-43. D audit part_d/post06/bgv_converse_scope_audit.md; C checked the exact statement and boundary, not all foundational proofs."]
]
for values in entries:
    record = dict(zip(fields, values))
    rows = [row for row in rows if row["key"] != record["key"]]
    rows.append(record)
save_table(path, fields, rows, "\t")
report = {
    "time": now,
    "new_labels": [item[0] for item in new],
    "new_citation_keys": keys,
    "finite_primes_only": True,
    "all_prior_c6_wording_repairs_preserved": True,
    "general_gate_unresolved": True,
}
(root / "code/part_c/integrate_c6_global_local_output.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
