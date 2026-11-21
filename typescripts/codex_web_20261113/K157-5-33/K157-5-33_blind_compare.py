"""Recreate the collation from the TSV, the original changed blocks and the page files."""
import csv
import html
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
KEY = "K157-5-33"
BLOCK = re.compile(r"^% (B\d+)\n(.*?)(?=^% B\d+\n|^% archive sheet number:|\Z)", re.M | re.S)


def block_map(text):
    blocks = {name: body.strip() for name, body in BLOCK.findall(text)}
    blocks["head"] = re.search(r"\\mspage\{(.*?)\}", text)[1]
    blocks["foot"] = re.search(r"^% archive sheet number: (.+)", text, re.M)[1]
    return blocks


def code(value):
    escaped = html.escape(" ".join(value.split())).replace("|", "&#124;")
    return "<code>" + escaped + "</code>"


def flattened(value):
    return re.sub(r"\s+", "", value).casefold()


def read(path, extension):
    return (path / f"{KEY}_{extension}").read_text(encoding="utf-8")


def main():
    ledger = [json.loads(line) for line in read(BASE, "collation.jsonl").splitlines()]
    originals = json.loads(read(BASE, "first_readings.json"))
    with (BASE / f"{KEY}_blind.tsv").open(encoding="utf-8", newline="") as source:
        witnesses = list(csv.DictReader(source, delimiter="\t"))
    pages = set()
    difference_count = 0
    records = []
    index = []
    for page in ledger:
        scan = page["scan"]
        assert scan not in pages, f"Duplicate page {scan}"
        pages.add(scan)
        page_text = (BASE / "pages" / f"{KEY}_157-5_scan{scan}.tex").read_text(encoding="utf-8")
        final = block_map(page_text)
        first = final | originals.get(str(scan), {})
        rows = [row for row in witnesses if int(row["scan"]) == scan]
        assert len(rows) == len(page["locators"]), f"Missing witness for {scan}"
        differences = {line: (before, after, why) for line, before, after, why in page["differences"]}
        assert len(differences) == len(page["differences"])
        assert set(differences).issubset(range(1, len(rows) + 1))
        first_text = "\n".join(first.values())
        records.append(f"\n## Scan {scan}\n")
        for number, (witness, locator) in enumerate(zip(rows, page["locators"]), 1):
            names = locator.split()
            assert all(name in final for name in names), (scan, locator)
            cited = " ".join(final[name] for name in names)
            reading = witness["what_the_crop_shows"]
            where = witness["place"]
            identifier = f"{scan}.{number:02}"
            if number in differences:
                before, after, why = differences[number]
                assert before in first_text, (identifier, "first", before)
                assert after in page_text, (identifier, "final", after)
                index.append(f"| {identifier} | {where} ({locator}) | {code(reading)} | {code(before)} | {code(after)} | {why} |")
                verdict = "See difference " + identifier
                difference_count += 1
            elif flattened(reading) in flattened(cited):
                verdict = "Literal match after space and case folding"
            else:
                verdict = "Graphic agreement on the identified material, by visual collation"
            records.extend([f"**{identifier} · {where} · {locator}.** {verdict}.",
                            f"\nBlind entry: {code(reading)}.\n",
                            f"Aligned page text: {code(cited)}.\n"])
    assert {int(row["scan"]) for row in witnesses} == pages, "Blind page missing from ledger"
    report = [
        "# Blind collation",
        f"\n{len(witnesses)} entries on {len(pages)} scans. {difference_count} entries diverged on a reading, placement or degree of certainty.",
        "\nThe TSV records a blind rereading by the same transcriber. It contains the words, symbols and descriptions entered before reopening the page files. The transcriber aligned each entry with the indicated blocks and returned to the crop to adjudicate differences. This script checks both quoted forms against the first and final readings and prints all of the alignments. Different notation, abbreviation or spacing in a descriptive witness can express the same reading. Changes found on rereading outside a listed disagreement are recorded separately in the page audit.",
        "\n## Adjudicated differences\n",
        "| Entry | Place | Blind observation | First transcription | Final transcription | Settlement on the image |",
        "|---|---|---|---|---|---|",
        *index, "\n## All independent observations and aligned source blocks", *records,
    ]
    (BASE / f"{KEY}_blind_compare.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"{len(witnesses)} witnesses; {difference_count} adjudicated differences; {len(pages)} scans")


if __name__ == "__main__":
    main()
