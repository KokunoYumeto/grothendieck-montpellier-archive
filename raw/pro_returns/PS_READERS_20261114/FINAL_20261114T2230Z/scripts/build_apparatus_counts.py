"""Rebuild apparatus counts and merge the typesetting histories.

Run from any directory.  Inputs and outputs are located relative to this script.
The existing merged history is retained, so a regenerated or emptied input TSV
does not erase an earlier recorded mechanical repair.  No checked source changes.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import re


PROJECT = Path(__file__).resolve().parents[1]
CANONICAL = [
    "reader", "page_key", "source_line", "what_was_wrong", "what_was_done", "source_id"
]
MERGED_FIELDS = CANONICAL + [
    "extra_fields_json", "source_files", "source_rows", "provenance_count",
    "source_records_json",
]
ALIASES = {
    "reader": ("reader", "form"),
    "page_key": ("page_key", "key"),
    "source_line": ("source_line", "line", "site", "place", "location"),
    "what_was_wrong": ("what_was_wrong", "problem", "reason", "before"),
    "what_was_done": ("what_was_done", "change", "action", "after"),
    "source_id": ("source_id", "id"),
}
FORMS = [
    ("diplomatic", "Diplomatic", "PS_EN_diplomatic", 0),
    ("reading", "Reading", "PS_EN_reading", 2),
    ("corrected_apparatus", "Corrected with apparatus", "PS_EN_corrected_apparatus", 1),
    ("master_annotated", "Annotated master, default mode", "PS_EN_master_annotated", 1),
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_tsv(path: Path):
    data = path.read_bytes()
    reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")), delimiter="\t")
    rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError(f"Unexpected extra TSV fields in {path.name}")
    return rows, reader.fieldnames or [], digest(data)


def atomic_text(path: Path, text: str):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def write_tsv(path: Path, fields, rows):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    atomic_text(path, output.getvalue())


def json_text(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_record(row):
    result = {}
    consumed = set()
    for target, names in ALIASES.items():
        selected = next((name for name in names if row.get(name, "") != ""), None)
        result[target] = row[selected] if selected else ""
        if selected:
            consumed.add(selected)
    if not result["reader"]:
        result["reader"] = "guide" if (
            result["page_key"].startswith("guide")
            or result["source_id"].startswith("TYPESET:guide:")
        ) else "all"
    if not any(result[k] for k in ("page_key", "what_was_wrong", "what_was_done")):
        raise ValueError(f"Unrecognized typesetting schema: {sorted(row)}")
    result["extra_fields_json"] = json_text({
        k: v for k, v in row.items() if k not in consumed and v != ""
    })
    return result


def merge_typesetting(project: Path):
    records = project / "records"
    destination = records / "TYPESETTING_FIXES.tsv"
    retained = []
    if destination.exists():
        old, _, _ = read_tsv(destination)
        for row in old:
            if not row.get("source_records_json"):
                raise ValueError("Existing merged history lacks recoverable provenance")
            retained.extend(json.loads(row["source_records_json"]))
    inputs = []
    current = []
    for path in sorted(records.glob("TYPESETTING_FIXES_*.tsv")):
        rows, fields, checksum = read_tsv(path)
        relative = path.relative_to(project).as_posix()
        inputs.append({"source": relative, "sha256": checksum,
                       "rows": len(rows), "fields": fields})
        for number, row in enumerate(rows, 1):
            current.append({"file": relative, "data_row": number,
                            "sha256": checksum, "record": row})

    # File-version and row identities preserve repeated operations on one line,
    # even when their generic canonical descriptions are identical.
    provenance = {json_text(item): item for item in retained + current}
    groups = {}
    for item in provenance.values():
        canonical = canonical_record(item["record"])
        identity = tuple(canonical[k] for k in CANONICAL + ["extra_fields_json"])
        group = groups.setdefault(identity, {"record": canonical, "sources": {}})
        group["sources"][json_text(item)] = item
    merged = []
    for identity in sorted(groups):
        group = groups[identity]
        sources = sorted(group["sources"].values(), key=lambda x: (
            x["file"], x["sha256"], x["data_row"]
        ))
        row = dict(group["record"])
        row.update({
            "source_files": json_text(sorted({x["file"] for x in sources})),
            "source_rows": json_text(sorted({f'{x["file"]}:{x["data_row"]}' for x in sources})),
            "provenance_count": len(sources),
            "source_records_json": json_text(sources),
        })
        merged.append(row)
    write_tsv(destination, MERGED_FIELDS, merged)
    audit = {
        "inputs": inputs,
        "current_input_rows": len(current),
        "retained_file_version_row_records": len(provenance),
        "merged_rows": len(merged),
        "output": "records/TYPESETTING_FIXES.tsv",
        "sha256": digest(destination.read_bytes()),
        "deduplication": "Exact canonical fields plus unmapped source fields. All original rows, source files, source hashes and 1-based TSV data rows remain in source_records_json.",
        "history": "Previously merged provenance is retained when an input file is regenerated or emptied. Repeated identical descriptions on one line are grouped, but their distinct input-row identities are preserved.",
        "location_mapping": "A source schema's site/place/location is kept in source_line when no source_line/line field exists; its original name and value remain in the complete original record.",
    }
    atomic_text(records / "TYPESETTING_FIXES_MERGE.json",
                json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    return audit


def build_counts(project: Path):
    records = project / "records"
    changes, _, changes_hash = read_tsv(records / "CHANGES_EN.tsv")
    manifest_bytes = (records / "BUILD_MANIFEST.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    metadata = json.loads((project.parent / "inputs/text/records/PAGES_PS.json").read_text())
    meta = {row["key"]: row for row in metadata}
    built = {row["key"]: row for row in manifest}
    ids = [row["source_id"] for row in changes]
    if len(ids) != len(set(ids)):
        raise ValueError("CHANGES_EN contains duplicate variant source IDs")
    counts_by_page = Counter()
    by_division = Counter()
    kinds = Counter()
    matrix = Counter()
    pages_with_entries = defaultdict(set)

    def division(key):
        return "Brown" if meta[key].get("text") == "brown" else meta[key]["cote"]

    page_counts = Counter(division(key) for key in built)
    for row in changes:
        key = row["place"].split(":L", 1)[0]
        if key not in built or key not in meta:
            raise ValueError(f"Change refers to an unbuilt source: {key}")
        if row["cote"] != meta[key]["cote"] or int(row["site"]) != int(meta[key]["site"]):
            raise ValueError(f"Change source coordinates disagree: {key}")
        part = division(key)
        counts_by_page[key] += 1
        by_division[part] += 1
        kinds[row["kind"]] += 1
        matrix[(part, row["kind"])] += 1
        pages_with_entries[part].add(key)
    for key, row in built.items():
        if counts_by_page[key] != row["variants"]:
            raise ValueError(f"Variant count disagrees with BUILD_MANIFEST: {key}")
    total = len(changes)
    forms = []
    for name, label, basename, expected_mode in FORMS:
        path = project / "readers" / (basename + ".tex")
        source = path.read_text()
        mode_match = re.search(r"\\def\\EditionMode\{([012])\}", source)
        if not mode_match or int(mode_match[1]) != expected_mode:
            raise ValueError(f"Unexpected edition mode: {basename}")
        entries = re.findall(r"\\psentry\{([^{}]+)\}", source)
        inventory = re.findall(r"\\psnumber\{([^{}]+)\}", source)
        if Counter(entries) != Counter(ids) or Counter(inventory) != Counter(ids):
            raise ValueError(f"Generated entry/inventory IDs disagree: {basename}")
        forms.append({"form": name, "label": label, "mode": expected_mode,
                      "variant_inventory": total,
                      "displayed_apparatus_entries": total if expected_mode == 1 else 0,
                      "tex": path.relative_to(project).as_posix(),
                      "sha256": digest(source.encode())})

    divisions = sorted((d for d in page_counts if d != "Brown"),
                       key=lambda d: int(d.split("-")[1]))
    if "Brown" in page_counts:
        divisions.append("Brown")
    brown = [meta[key] for key in built if division(key) == "Brown"]
    brown_scope = (f'134-2, archive sites {min(int(x["site"]) for x in brown)}–'
                   f'{max(int(x["site"]) for x in brown)}') if brown else "not included"
    data = {
        "source": "records/CHANGES_EN.tsv", "source_sha256": changes_hash,
        "build_manifest_sha256": digest(manifest_bytes),
        "source_pages": len(built), "unique_variants": total,
        "brown_scope": brown_scope, "forms": forms,
        "divisions": [{"division": d, "source_pages": page_counts[d],
                       "pages_with_entries": len(pages_with_entries[d]),
                       "variants": by_division[d]} for d in divisions],
        "kinds": [{"kind": kind, "total": kinds[kind],
                   "by_division": {d: matrix[(d, kind)] for d in divisions}}
                  for kind in sorted(kinds, key=str.casefold)],
    }
    atomic_text(records / "APPARATUS_COUNTS.json",
                json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    detail = []
    for d in divisions:
        for kind in sorted(kinds, key=str.casefold):
            count = matrix[(d, kind)]
            for form in forms:
                detail.append({"division": d, "kind": kind, "form": form["form"],
                               "variant_inventory": count,
                               "displayed_apparatus_entries": count if form["mode"] == 1 else 0})
    write_tsv(records / "APPARATUS_COUNTS.tsv",
              ["division", "kind", "form", "variant_inventory", "displayed_apparatus_entries"], detail)

    lines = ["# Apparatus counts", "",
        f"The current complete inventory contains **{total:,} distinct variants** across **{len(built):,} source pages**. "
        f"Brown's translation is counted separately ({brown_scope}); it is excluded from the main 134-2 row.", "",
        "Counts come from `records/CHANGES_EN.tsv`, one row per maximal editorial operation. "
        "The row IDs agree with `records/BUILD_MANIFEST.json` and with the entry and inventory definitions in all four generated TeX forms. "
        "Nested layers within one wholly cancelled or replaced passage remain within that entry and are not counted a second time.", "",
        "## By form", "",
        "| Form | Edition mode | Stored variant inventory | Displayed apparatus entries |",
        "| --- | ---: | ---: | ---: |"]
    for form in forms:
        lines.append(f'| {form["label"]} | {form["mode"]} | {total:,} | {form["displayed_apparatus_entries"]:,} |')
    lines.extend(["",
        "The stored inventory is shared by the generated sources. The diplomatic and reading modes display **zero apparatus entries**, despite retaining the variant definitions in their TeX. "
        f"The corrected reader and the annotated master in its default mode each display the same **{total:,} entries**. "
        "These are two presentations of the same inventory, not two sets to add together. Switching the master to diplomatic mode0 or reading mode2 displays zero apparatus entries while preserving its inventory.", "",
        "## By cote and form", "",
        "| Division | Source pages | Pages with entries | Inventory variants | Diplomatic entries | Reading entries | Corrected entries | Master mode1 entries |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for d in divisions:
        count = by_division[d]
        lines.append(f'| {d} | {page_counts[d]:,} | {len(pages_with_entries[d]):,} | {count:,} | 0 | 0 | {count:,} | {count:,} |')
    lines.append(f'| **Total** | **{len(built):,}** | **{len(counts_by_page):,}** | **{total:,}** | **0** | **0** | **{total:,}** | **{total:,}** |')
    lines.extend(["", "## By kind and cote", "",
        "Each count below is both a stored variant count and the displayed entry count in the corrected reader and master mode1. "
        "For every kind and every division, the diplomatic and reading displayed-entry count is zero. Kind labels are retained verbatim from the change ledger; similar labels have not been silently combined.", "",
        "| Kind | " + " | ".join(divisions) + " | Total |",
        "| --- | " + " | ".join("---:" for _ in divisions) + " | ---: |"])
    for kind in sorted(kinds, key=str.casefold):
        label = kind.replace("|", "\\|")
        lines.append("| " + label + " | " + " | ".join(f'{matrix[(d, kind)]:,}' for d in divisions) + f' | {kinds[kind]:,} |')
    lines.append("| **Total** | " + " | ".join(f'**{by_division[d]:,}**' for d in divisions) + f' | **{total:,}** |')
    lines.extend(["", "## Reproduction and provenance", "",
        "Run `python scripts/build_apparatus_counts.py` from the project, or invoke that script by its path from another directory, after rebuilding the readers. "
        "It verifies the ledger against the build manifest and generated TeX IDs, then regenerates this report and the full division × kind × form table in `records/APPARATUS_COUNTS.tsv`. "
        "Structured totals and source hashes are in `records/APPARATUS_COUNTS.json`.", "",
        f"Change-ledger SHA-256: `{changes_hash}`.", "",
        "The same command merges every `records/TYPESETTING_FIXES_*.tsv` schema into `records/TYPESETTING_FIXES.tsv`. "
        "The merged history preserves original rows, input-file hashes and data-row positions, including earlier generated repairs when later normalization empties their source file. "
        "Guide fixes and subsequently added normalization histories remain in scope. Its deduplication and input summary are in `records/TYPESETTING_FIXES_MERGE.json`.", ""])
    atomic_text(project / "APPARATUS_COUNTS.md", "\n".join(lines))
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=PROJECT)
    args = parser.parse_args()
    counts = build_counts(args.project)
    merged = merge_typesetting(args.project)
    print(json.dumps({"source_pages": counts["source_pages"],
                      "unique_variants": counts["unique_variants"],
                      "brown_scope": counts["brown_scope"],
                      "typesetting_input_rows": merged["current_input_rows"],
                      "typesetting_merged_rows": merged["merged_rows"],
                      "typesetting_retained_provenance": merged["retained_file_version_row_records"]}))


if __name__ == "__main__":
    main()
