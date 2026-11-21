"""Rebuild the release check ledger from preserved per-agent event streams.

Five source columns are preserved by position.  The spelling alias
`used and rechecked` is normalized to the prompt's full category.  The
overwritten intermediate root_independent_events.tsv is deliberately excluded;
the restored determinant and Masullo streams are the authoritative copies.
This script validates record structure, not mathematical truth.
"""
from pathlib import Path
import collections
import csv

ROOT = Path(__file__).resolve().parent.parent
ALLOWED = {
    "targeted proof check",
    "independent re-proof",
    "computation or formal certificate",
    "used and rechecked in this run",
    "carried as background without fault found",
    "refuted, with the refined statement's id",
}

def main():
    streams = [p for p in sorted((ROOT / "work").glob("*events.tsv"))
               if p.name != "root_independent_events.tsv"]
    merged = []
    for source in streams:
        with source.open(newline="") as handle:
            records = list(csv.reader(handle, delimiter="\t"))
        if len(records[0]) != 5:
            raise ValueError((source.name, "invalid header", records[0]))
        for number, record in enumerate(records[1:], 2):
            if len(record) != 5 or any(not field.strip() for field in record):
                raise ValueError((source.name, number, record))
            if record[3] == "used and rechecked":
                record[3] = "used and rechecked in this run"
            if record[3] not in ALLOWED:
                raise ValueError((source.name, number, record[3]))
            merged.append(record + [source.name])
    output_directory = ROOT / "deliverables" if (ROOT / "deliverables").is_dir() else ROOT
    destination = output_directory / "CHECK_EVENTS.tsv"
    with destination.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["statement_id", "date", "who_model_effort_run", "type",
                         "outcome", "event_source"])
        writer.writerows(merged)
    print({"source_streams": len(streams), "events": len(merged),
           "types": dict(collections.Counter(r[3] for r in merged))})

if __name__ == "__main__":
    main()
