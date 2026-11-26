"""Build the report from the blind ledger, its audited alignment and the final page files."""
import csv
from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STEM = "K62-04"
TICK = chr(96)

def read_tsv(suffix):
    with (ROOT / (STEM + suffix)).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file, delimiter="\t"))

def cell(value):
    return value.replace("|", r"\|").replace("\n", " ")

def literal(value):
    return TICK + cell(value) + TICK

def identity(row):
    return row["scan"], row["place"]

def build():
    blind = read_tsv("_blind.tsv")
    align = read_tsv("_blind_alignment.tsv")
    assert [identity(r) for r in blind] == [identity(r) for r in align]
    assert len({identity(r) for r in align}) == len(align)
    scans = sorted({r["scan"] for r in blind})
    pages = {n:(ROOT / "pages" / f"{STEM}_62_scan{n}.tex").read_bytes() for n in scans}
    history = (ROOT / "progress.log").read_text(encoding="utf-8").splitlines()
    for n, data in pages.items():
        name = f"pages/{STEM}_62_scan{n}.tex"
        assert f"sha256 witness {sha256(data).hexdigest()} {name}" in history

    counts = Counter(r["scan"] for r in align if r["difference"] == "yes")
    entries = Counter(r["scan"] for r in blind)
    half = (len(scans)+1)//2
    scan_rows = []
    for a, b in zip(scans[:half], scans[half:]):
        scan_rows.append(f"| {int(a)} | {entries[a]} | {counts[a]} | {int(b)} | {entries[b]} | {counts[b]} |")
    out = [
        "# Blind readings compared with the page files", "",
        f"Of {len(blind)} independent crop readings, {sum(counts.values())} differed from the first-pass transcription at the recorded place. The differences include graphic details and equivalent TeX spellings. A page-by-page count follows.", "",
        "| Scan | Read blind | Differed | Scan | Read blind | Differed |",
        "|---|---:|---:|---|---:|---:|", *scan_rows, "",
        "The first-pass column quotes the disputed part. The next column gives the decision made when the crop was read again during the audit. The final column quotes the same place in the witness-checked page file. Its line numbers refer to the TeX source. An alternative or a deletion can remain in the final text even when one blind reading agrees. The full ledger, including agreements, is in K62-04_blind.tsv.", "",
        "| Scan | Place | Blind reading | First-pass excerpt | Settlement on the crop | Final excerpt |",
        "|---|---|---|---|---|---|"
    ]
    for entry, record in zip(blind, align):
        assert record["difference"] in {"yes","no"}
        if record["difference"] == "no":
            continue
        n, place = identity(record)
        data = pages[n]
        left, right = int(record["final_start"]), int(record["final_end"])
        assert 0 <= left < right <= len(data), (n, place)
        fragment = data[left:right].decode("utf-8")
        line = data[:left].count(b"\n") + 1
        if fragment.startswith("% slanted\n"):
            line += 1
            fragment = fragment.removeprefix("% slanted\n")
        fields = [str(int(n)), cell(place), literal(entry["what the crop shows"]),
                  literal(record["first_pass"]), cell(record["settlement"]),
                  f"line {line} · "+literal(fragment)]
        out.append("| "+" | ".join(fields)+" |")
    (ROOT / (STEM+"_blind_compare.md")).write_text("\n".join(out)+"\n",encoding="utf-8")
    print(f"{len(blind)} entries; {sum(counts.values())} differences, each located in the final text.")

if __name__ == "__main__":
    build()
