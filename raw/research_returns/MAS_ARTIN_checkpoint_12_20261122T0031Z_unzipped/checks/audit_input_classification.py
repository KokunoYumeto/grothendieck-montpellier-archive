#!/usr/bin/env python3
"""Independent coverage/integrity audit; never chooses mathematical classes.

This reads the emitted TSV and supplied sources, not the builder's assignments.
It verifies exact catalogue coverage, source-field preservation, named outside
inputs, intake range expansion, evidence paths, and separation of missing gates.
"""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
SOURCES = WORK.parent / "sources"
GRH = next(SOURCES.glob("RETURN_GRH_NIGHT_checkpoint_07_*"))


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def canonical(name):
    return re.sub(r"^F-SM(\d{2})$", r"F-SM-\1", name)


def numbered_mentions(text):
    """Expand full and abbreviated numeric ranges in the intake prose."""
    found = set()
    pattern = re.compile(
        r"(?<![A-Za-z0-9-])"
        r"(?P<prefix>F-SM-?|BR-\d{3}|BR-\d{2}-|CC-[A-Z]+|CX-[RKNEG])"
        r"(?P<start>\d{2})(?P<suffix>[a-z]?)"
        r"(?:\s*(?:to|[–—-])\s*"
        r"(?:(?:F-SM-?|BR-\d{3}|BR-\d{2}-|CC-[A-Z]+|CX-[RKNEG])|[RKNEG])?"
        r"(?P<end>\d{2}))?"
    )
    for match in pattern.finditer(text):
        prefix = match.group("prefix")
        first = int(match.group("start"))
        suffix = match.group("suffix")
        last = int(match.group("end")) if match.group("end") else first
        assert last >= first and last-first < 100, match.group()
        if suffix:
            found.add(canonical(f"{prefix}{first:02d}{suffix}"))
        else:
            found.update(canonical(f"{prefix}{number:02d}") for number in range(first, last+1))
    return found


rows = read_tsv(WORK / "INPUT_CLASSIFICATION.tsv")
assert rows, "empty classification"
keys = [(row["run"], row["row_id"]) for row in rows]
assert len(keys) == len(set(keys)), "duplicate run/id"
allowed = {"A", "M", "outside preprint", "none"}
assert all(row["input_class"] in allowed for row in rows), "not exactly one permitted class"
by_key = {(row["run"], row["row_id"]): row for row in rows}

original = read_tsv(GRH / "CONSEQUENCES.tsv")
original_ids = {row["id"] for row in original}
classified_ids = {row["row_id"] for row in rows if row["run"] == "GRH_NIGHT"}
assert len(original) == 362 and len(original_ids) == 362
assert original_ids == classified_ids, {
    "missing": sorted(original_ids-classified_ids),
    "extra": sorted(classified_ids-original_ids),
}
for source in original:
    target = by_key[("GRH_NIGHT", source["id"])]
    for old, new in [
        ("statement", "statement"), ("input", "stated_input"),
        ("status", "source_status"), ("where_the_proof_is", "original_proof_locator"),
        ("where_it_lives", "grothendieck_locator"),
    ]:
        assert source[old] == target[new], (source["id"], "changed original field", old)

for row in rows:
    assert row["evidence_locator"] and row["audit_status"] and row["residual_notes"]
    if row["input_class"] == "outside preprint":
        assert row["outside_keys"] and row["outside_preprints"], row["row_id"]
    if row["outside_keys"]:
        assert row["input_class"] in {"M", "outside preprint"}, row["row_id"]
    locator = row["evidence_locator"].split(":", 1)[0]
    assert (SOURCES / locator).is_file(), ("missing evidence file", locator)
    if row["run"] == "CX_GRH":
        assert "intake-only" in row["audit_status"]
        assert "no proof recheck" in row["audit_status"]

for identifier in ["NT-Z13", "NT-Z15", "NT-Z16"]:
    row = by_key[("GRH_NIGHT", identifier)]
    assert row["input_class"] == "M" and row["input_flag"]
assert by_key[("GRH_NIGHT", "AG-CYCLIC-DIV")]["outside_keys"] == "PF26"
for identifier in ["CX-ALG-027", "CX-ALG-028"]:
    row = by_key[("GRH_NIGHT", identifier)]
    assert row["input_class"] == "M" and "PF26" in row["outside_keys"]

intake_text = "\n".join(path.read_text(encoding="utf-8") for path in sorted(SOURCES.glob("INTAKE*.md")))
mentioned = numbered_mentions(intake_text)
relevant = {name for name in mentioned if name.startswith(("BR-", "CC-", "F-SM-"))}
relevant |= {name for name in mentioned if re.fullmatch(r"CX-[RKNEG]\d{2}", name)}
actual_findings = {row["row_id"] for row in rows}
assert relevant <= actual_findings, {"missing_intake_numeric_ids": sorted(relevant-actual_findings)}

# Contextual, nonnumeric shorthand in the two supplied ALPOGE intakes is
# intentionally enumerated independently of the builder.  The source paragraph
# names the prefix once and then lists these parallel finding suffixes.
contextual = {
    "AQ-14-QUASIPROJECTIVE", "AQ-14-NONPROPER", "AQ-14-ALTERATION",
    "AQ-67-EXACT", "AQ-67-NONHOLO", "AQ-136-STRICT", "AQ-136-SEMILOCAL",
    "AQ-136-COSPAN", "AQ-136-CONNECTED-SOURCES", "AQ-136-SEMILOCAL-SOURCES",
    "AQ-136-FIRST-SKELETON", "AQ-136-FREE-ZERO-FORMS", "AQ-136-HIGHER-COMPLETION",
    "AQ-136-MULTIPLICATIVE", "AQ-136-PD-OPERATIONS", "AQ-136-PD-RIGIDITY",
    "BR-14-SEP", "BR-15-CLASSBOUND", "BR-15-SLOPEBOUND", "BR-15-ORBIT-RETRACT",
    "BR-15-QUADRIC-DISCRIMINANT", "BR-15-QUADRIC-TATE",
}
assert contextual <= actual_findings, {"missing_contextual_ids": sorted(contextual-actual_findings)}
cx_expected = {f"CX-{letter}{number:02d}" for letter, stop in [("R", 2), ("K", 8), ("N", 15), ("E", 8), ("G", 6)] for number in range(1, stop+1)}
cx_actual = {row["row_id"] for row in rows if row["run"] == "CX_GRH"}
assert len(cx_expected) == 39 and cx_expected == cx_actual

gates = read_tsv(WORK / "INPUT_UNCLASSIFIED_GATES.tsv")
cx_gate_ids = {row["row_id"] for row in gates if row["run"] == "CX_GRH"}
assert cx_gate_ids == {f"CX-U{number:02d}" for number in range(1, 7)}
assert not cx_gate_ids & actual_findings
assert all(row["input_class"] not in allowed for row in gates)

events = read_tsv(WORK / "modules/inputs_events.tsv")
event_ids = {row["statement_id"] for row in events}
assert all(f"{run}:{identifier}" in event_ids for run, identifier in keys)

report = {
    "result": "PASS",
    "date": "2026-11-21",
    "counts_by_run": dict(Counter(row["run"] for row in rows)),
    "counts_by_class": dict(Counter(row["input_class"] for row in rows)),
    "original_GRH_rows": 362,
    "GRH_missing": [], "GRH_extra": [], "duplicate_run_id_pairs": [],
    "original_GRH_source_fields_preserved": True,
    "intake_numeric_or_range_finding_ids_checked": len(relevant),
    "contextual_nonnumeric_ids_checked": len(contextual),
    "CX_intake_findings_checked": 39,
    "CX_unprovided_gates_separately_recorded": sorted(cx_gate_ids),
    "classification_sha256": hashlib.sha256((WORK / "INPUT_CLASSIFICATION.tsv").read_bytes()).hexdigest(),
    "scope": "Coverage, integrity and evidence-link verification only; mathematical classifications remain documented editorial judgments, not outputs of the range parser.",
}
(WORK / "checks/input_independent_audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
