"""Record the actual AG5 primary-page reading and update its existing history result."""
from pathlib import Path
import csv
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
FILES = ["sections/geometry_H.tex", "notes/geometry_results.csv", "notes/outcome_table.tsv", "notes/manuscript_date_attempts.tsv", "notes/geometry_CHECK_EVENTS.tsv"]
before = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in FILES}
key = "algGrothendieckCR1951Tensor"
p = ROOT / FILES[0]
s = p.read_text()
s = s.replace(r"\subsection{The historical lead: what the printed memoir actually contains}", r"\subsection{The historical lead: what the printed sources contain}", 1)
anchor = "\\label{geo-H-history}\nThe inspected fourth printing"
assert s.count(anchor) == 1
s = s.replace(anchor, "\\label{geo-H-history}\nA 1951 \\emph{Comptes rendus} note already announces genus zero for\nFredholm determinants of trace operators on Hilbert space, while\npromising a detailed treatment elsewhere.\nThe inspected fourth printing", 1)
anchor = "The primary memoir has now been inspected directly\n"
assert s.count(anchor) == 1
paragraph = r"""The earlier primary announcement is explicit
\cite[p.~1557, \S1, final paragraph]{algGrothendieckCR1951Tensor}.
After introducing trace operators and their Fredholm determinants, the
1951 note asserts genus at most one in general and genus zero when the
space is Hilbert, without imposing normality. The same paragraph promises
a detailed Fredholm exposition elsewhere; the three-page note does not
give the Hilbert genus-zero proof. Its first page records presentation on
3 December 1951. This establishes an earlier printed announcement of the
result, without identifying or dating the particular cote~1 proof sheets.

"""
s = s.replace(anchor, paragraph + anchor, 1)
anchor = "The inspected memoir states both genus zero and the sufficient $\\ell^1$\n"
assert s.count(anchor) == 1
s = s.replace(anchor, "The 1951 note already announces Hilbert genus zero and promises a fuller\ntreatment elsewhere. The inspected memoir states both genus zero and the sufficient $\\ell^1$\n", 1)
p.write_text(s)

def edit_table(name, delimiter, mutate):
    p = ROOT / name
    with p.open(newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        fields = reader.fieldnames
        rows = list(reader)
    mutate(rows)
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def result(rows):
    r = next(r for r in rows if r["id"] == "geo-H-history")
    assert r["status"] == "Known"
    assert key not in r["depends_on"]
    r["depends_on"] = key + ";" + r["depends_on"]
    r["notes"] = "The original 1951 CR note, p1557 section1 final paragraph, announces Hilbert genus zero without proof and promises a detailed Fredholm treatment elsewhere; the starred presentation date is 3 December 1951. This dates the announcement, not the cote1 proof sheets. " + r["notes"]
edit_table(FILES[1], ",", result)

def outcome(rows):
    r = next(r for r in rows if r["item"].startswith("Lead6,"))
    assert r["state"] == "Publication comparison proved; manuscript date unsettled"
    r["outcome"] = "The original 1951 CR note already announces Hilbert genus zero at p1557 and promises a detailed treatment elsewhere; it does not print the proof or date the manuscript. " + r["outcome"]
edit_table(FILES[2], "\t", outcome)

def routes(rows):
    route = "Original 1951 Comptes rendus announcement (AG5)"
    assert all(r["route"] != route for r in rows)
    rows.append({"route": route,
        "evidence": "All three original facsimile pages 1556-1558 visually read by algebra and geometry; root independently read p1557. Section1 final paragraph announces general Hilbert genus zero without normality and promises detailed Fredholm treatment elsewhere. The starred presentation date on p1556 is 3 December 1951.",
        "failed_step": "The earlier announcement identifies no particular proof manuscript or dated enclosure and does not print the Hilbert genus-zero argument; the cote1 sheet-date gate is unchanged.",
        "next_step": "Locate an explicit dated original proof or enclosure identification matching the particular cote1 leaves; do not transfer the announcement year to them.",
        "record": "notes/algebra_earlynotices_source_audit.md; logs/geometry_history_1951_update.json"})
edit_table(FILES[3], "\t", routes)

def events(rows):
    for statement_id in ["geo-H-history", "SA23-49"]:
        rows.append({"statement_id": statement_id, "date": datetime.now(timezone.utc).date().isoformat(),
            "who": "GPT-6 Astra Pro, inherited effort, geometry_analysis",
            "type": "used and rechecked in this run",
            "outcome": "Visually read all three original AG5 pages1556-1558; p1557 section1 final paragraph explicitly announces Hilbert genus zero and promises a detailed Fredholm exposition elsewhere. The p1556 starred presentation date is3December1951. Added the earlier printed announcement to the existing history proposition and Lead6 wording without changing status or dating the cote1 sheets. This is a documentary check, not an independent proof. Source key algGrothendieckCR1951Tensor; exact audit in algebra_earlynotices_source_audit.md."})
edit_table(FILES[4], "\t", events)

record = {"utc": datetime.now(timezone.utc).isoformat(), "source": "sources/algebra_earlynotice_AG5.pdf", "source_sha256": hashlib.sha256((ROOT / "sources/algebra_earlynotice_AG5.pdf").read_bytes()).hexdigest(), "actual_visual_reading": "All three original facsimile pages1556-1558. Page1557 was displayed before context compaction; pages1556/1558 were successfully displayed individually afterwards. An intervening truncated multi-image output was not counted as a reading.", "change_scope": "Existing historical proposition, source comparison, registry, Lead6 wording, route index and actual-run documentary events; no new numbered statement, no status change, no manuscript-date inference.", "files": [{"path": n, "before_sha256": before[n], "after_sha256": hashlib.sha256((ROOT / n).read_bytes()).hexdigest()} for n in FILES]}
(ROOT / "logs/geometry_history_1951_update.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"utc": record["utc"], "edited": FILES, "date_routes": 51, "new_numbered_statements": 0, "status_changed": False}))
