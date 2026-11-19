"""Preserve manually selected literal quotations for late claims C240–264,289–290.

The agent directly read E730–2162, including the continuation crossing 311/312,
then re-read the selected passages before preparing this list. The range list
below is a manual source-fidelity selection, not an automated mathematical
classification. This program extracts those selections without emendation and
checks exact provenance. The late agent independently checks and integrates them.
"""

from pathlib import Path
import csv
import datetime
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "work/middle"
SOURCE = "pro/MPL_136_282-327_transcription.tex"
WHO = "GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle"

# All entries are explicit selections made after reading the actual passages.
# Separate ranges are joined with a visible ellipsis; no silently amended ink.
SELECTIONS = {
    240: [(789, 794), (803, 806)],
    241: [(876, 882)],
    242: [(975, 983)],
    243: [(1017, 1017), (1155, 1164)],
    244: [(1140, 1144)],
    245: [(1187, 1192), (1205, 1208)],
    246: [(1286, 1289), (1293, 1298)],
    247: [(1346, 1361)],
    248: [(1467, 1472)],
    249: [(1533, 1542), (1559, 1559)],
    250: [(1608, 1627)],
    251: [(1681, 1681), (1683, 1683)],
    252: [(1888, 1895)],
    253: [(1734, 1737), (1924, 1927)],
    254: [(1749, 1752), (1916, 1916)],
    255: [(1922, 1922)],
    256: [(1924, 1927)],
    257: [(1928, 1928)],
    258: [(1930, 1933)],
    259: [(1937, 1946), (1955, 1959), (1961, 1967)],
    260: [(1983, 1983), (1989, 1997)],
    261: [(2015, 2017), (2038, 2041)],
    262: [(2068, 2071), (2075, 2077)],
    263: [(2079, 2082)],
    264: [(2148, 2152), (2154, 2157)],
    289: [(956, 960), (964, 973)],
    290: [(1221, 1224), (1229, 1236)],
}

source_path = ROOT / "sources/texts" / SOURCE
source_bytes = source_path.read_bytes()
source_text = source_bytes.decode("utf-8")
source_lines = source_text.splitlines()
source_sha256 = hashlib.sha256(source_bytes).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc)
claims = json.loads((ROOT / "work/late/claims.json").read_text())
claim_by_id = {claim["id"]: claim for claim in claims}

quotes = {}
audit = []
for number, ranges in SELECTIONS.items():
    claim_id = f"SA08-C{number}"
    assert claim_id in claim_by_id
    fragments = []
    locators = []
    for first, last in ranges:
        assert 1 <= first <= last <= len(source_lines)
        selected_lines = source_lines[first - 1 : last]
        fragment = "\n".join(selected_lines).strip()
        assert fragment and fragment in source_text
        preceding_scan = next(
            int(re.search(r"\\scanpage\{(\d+)\}", line).group(1))
            for line in reversed(source_lines[:first])
            if "\\scanpage{" in line
        )
        assert preceding_scan in claim_by_id[claim_id]["scans"]
        assert not any("\\scanpage{" in line for line in selected_lines)
        line_range = str(first) if first == last else f"{first}–{last}"
        fragments.append(fragment)
        locators.append({"file": SOURCE, "lines": line_range})
        audit.append(
            {
                "claim_id": claim_id,
                "file": SOURCE,
                "scan": preceding_scan,
                "lines": line_range,
                "literal_excerpt": fragment,
                "source_sha256": source_sha256,
                "audit": (
                    "Manually selected after direct reading; exact source fragment. "
                    "Deletion, insertion and uncertainty markers retained. "
                    "This is attribution/source-fidelity collation, not a mathematical proof."
                ),
            }
        )
    quotes[claim_id] = {
        "his_statement": " … ".join(fragments),
        "quotation_lines": locators,
    }

assert len(quotes) == 27
assert set(quotes) == {f"SA08-C{n}" for n in [*range(240, 265), 289, 290]}
(OUT / "late_quote_candidates.json").write_text(
    json.dumps(quotes, ensure_ascii=False, indent=2) + "\n"
)


def write_tsv(name, rows):
    with (OUT / name).open("w") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


write_tsv("late_quote_candidates_audit.tsv", audit)
events = [
    {
        "statement_id": claim_id,
        "date": now.date().isoformat(),
        "who": WHO,
        "type": "carried as background without fault found",
        "outcome": (
            "Literal author quotation selected after direct reading of the relevant "
            "E transcription and its adjoining continuation. Exact fragments and "
            "line/scan locators are saved in late_quote_candidates.json and its audit. "
            "Only source attribution and textual fidelity were checked by this event; "
            "it is not a mathematical proof or a new verdict on this late claim."
        ),
    }
    for claim_id in quotes
]
write_tsv("late_quote_candidates_events.tsv", events)

print(f"UTC: {now.isoformat()}")
print(f"Source: {SOURCE}; sha256={source_sha256}")
print(f"Saved {len(quotes)} claim quotations in {len(audit)} exact source fragments.")
print("Claims: SA08-C240–264 and SA08-C289–290.")
print("Every fragment is on a scan already listed by the corresponding late claim.")
print("Uncertainties, cancellations, questions and unfinished conditions are preserved.")
print("No mathematical judgments, source readings or other agents' files were altered.")
print(f"Candidates: {OUT / 'late_quote_candidates.json'}")
