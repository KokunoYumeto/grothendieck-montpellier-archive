"""Verify both recorded transcription states with standard Python, without writing any file.

Run this file in the unpacked delivery. Each witness row gives its zero-based
Unicode character offsets in the delivered page, with the end excluded. Walking
these spans backwards undoes the collation and recovers the independently
hashed frozen version.
"""
import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCANS = (3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20)

def recorded_hashes(lines, marker):
    position = next(i for i, line in enumerate(lines) if line.startswith(marker + " "))
    entries = {}
    for line in lines[position - len(SCANS) - 1:position]:
        digest, filename = re.fullmatch(r"([a-f0-9]{64})  (.+)", line).groups()
        entries[filename] = digest
    if len(entries) != len(SCANS) + 1:
        raise ValueError(f"Incomplete hash block at {marker}")
    return entries

def check(blob, filename, reference):
    if hashlib.sha256(blob).hexdigest() != reference[filename]:
        raise ValueError(f"SHA-256 mismatch for {filename}")

def main():
    log = (ROOT / "progress.log").read_text(encoding="utf-8").splitlines()
    frozen_hashes = recorded_hashes(log, "transcription frozen")
    delivered_hashes = recorded_hashes(log, "witness check done")
    by_scan = defaultdict(list)
    with (ROOT / "K39-01_witness_decisions.tsv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            by_scan[int(row["Scan"])].append(row)

    delivered_pages, frozen_pages = [], []
    for number in SCANS:
        name = f"pages/K39-01_39_scan{number:03}.tex"
        blob = (ROOT / name).read_bytes()
        check(blob, name, delivered_hashes)
        delivered_pages.append(blob)
        text = blob.decode("utf-8")
        boundary = len(text)
        for row in reversed(by_scan[number]):
            start = int(row["Delivered start (character)"])
            end = int(row["Delivered end (character)"])
            if not 0 <= start < end <= boundary or text[start:end] != row["Final reading"]:
                raise ValueError(f"Witness span does not match {name}, place {row['Place']}")
            text = text[:start] + row["Frozen reading"] + text[end:]
            boundary = start
        original = text.encode("utf-8")
        check(original, name, frozen_hashes)
        frozen_pages.append(original)

    name = "K39-01_transcription.tex"
    assembled = (ROOT / name).read_bytes()
    if assembled != b"".join(delivered_pages):
        raise ValueError("Assembled transcription differs from the ordered pages")
    check(assembled, name, delivered_hashes)
    check(b"".join(frozen_pages), name, frozen_hashes)
    total = sum(len(rows) for rows in by_scan.values())
    print(f"Verified {len(SCANS) + 1} frozen hashes and {len(SCANS) + 1} delivered hashes.")
    print(f"Reversed {total} witness entries to recover all frozen pages and their concatenation.")

if __name__ == "__main__":
    main()

