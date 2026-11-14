#!/usr/bin/env python3
"""Update provenance hashes after byte-identical reader regeneration.

This does not compile or visually inspect a PDF. It proves that regeneration
under the current inputs produced exactly the already-compiled TeX bytes.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from edition_core import sha256, read_tsv, write_tsv
from compile_readers import mechanical_gates

EDITION = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readers", nargs="+")
    args = parser.parse_args()
    ledger = EDITION / "records/BUILD_INPUT_REVALIDATION.tsv"
    history = read_tsv(ledger) if ledger.is_file() else []
    for name in args.readers:
        source = EDITION / "readers" / (name + ".tex")
        pdf = EDITION / "build" / name / (name + ".pdf")
        report_path = pdf.parent / "audit/report.json"
        expectation = json.loads((EDITION / "records" / ("LINK_EXPECTATIONS_" + name + ".json")).read_text())
        report = json.loads(report_path.read_text())
        source_hash = sha256(source.read_text())
        pdf_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if source_hash != report["source_sha256"] or source_hash != expectation["reader_sha256"]:
            raise SystemExit("Regenerated reader bytes differ; compilation and a new visual review are required: " + name)
        if pdf_hash != report["pdf_sha256"]:
            raise SystemExit("The PDF differs from its compiled hash: " + name)
        if expectation["logical_link_marks"] != report["expected_logical_link_marks"]:
            raise SystemExit("Link expectations differ: " + name)
        current = expectation["source_files_sha256"]
        stale = [p for p, h in current.items() if not (EDITION / p).is_file() or sha256((EDITION / p).read_text()) != h]
        if stale:
            raise SystemExit("Regenerate the reader and build manifest with current inputs before revalidation: " + name)
        previous = report.get("source_files_sha256", {})
        margin_actual=Counter(r["key"] for r in report.get("margin_content_routes",[]))
        margin_expected=expectation.get("running_margin_content_counts",{})
        report["margin_content_count_comparison"]={k:dict(expected=margin_expected.get(k,0),measured=margin_actual.get(k,0))
            for k in set(margin_expected)|set(margin_actual)}
        report["margin_content_counts_match"]=all(r["expected"]==r["measured"] for r in report["margin_content_count_comparison"].values())
        report["mechanical_gates_passed"]=mechanical_gates(report)
        if current == previous:
            report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
            print(name + ": input hashes are already current.")
            continue
        report.setdefault("original_compilation_source_files_sha256", previous)
        report["source_files_sha256"] = current
        stamp = datetime.now(timezone.utc).isoformat()
        proof = dict(reader=name, pdf_sha256=pdf_hash, source_sha256=source_hash, revalidated_utc=stamp,
            previous_inputs_sha256=sha256(json.dumps(previous, sort_keys=True)),
            current_inputs_sha256=sha256(json.dumps(current, sort_keys=True)),
            changed_inputs=" ".join(sorted(p for p in set(previous) | set(current) if previous.get(p) != current.get(p))),
            proof="Current regeneration produced exactly the compiled standalone TeX bytes; the PDF bytes and link expectations are unchanged. No compilation or visual inspection is inferred.")
        report.setdefault("input_revalidation_history", []).append(proof)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        history.append(proof)
        print(name + ": byte-identical regeneration proved; PDF retained.")
    if history:
        write_tsv(ledger, history)


if __name__ == "__main__":
    main()
