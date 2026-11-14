#!/usr/bin/env python3
"""Record translated-page provenance and exact mathematical-fragment parity."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_edition import input_snapshot

PATTERN = re.compile(r"(?<!\\)\$(?:[^$]|\\\$)*?(?<!\\)\$|\\\[.*?\\\]", re.S)


def fragments(text):
    text = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))
    return [match.group() for match in PATTERN.finditer(text)]


def diagrams(text):
    """Return each complete diagram macro, including its exact TeX body."""
    result = []
    for match in re.finditer(r"\\diagram\{", text):
        depth = 1
        position = match.end()
        while position < len(text) and depth:
            char = text[position]
            escaped = position > 0 and text[position - 1] == "\\"
            if not escaped:
                depth += (char == "{") - (char == "}")
            position += 1
        if depth:
            raise ValueError("Unbalanced diagram macro")
        result.append(text[match.start():position])
    return result


def completion_status():
    """Describe completed evidence without creating an approval or inspection."""
    audit_path = ROOT / "records" / "AUDIT_PROGRESS.json"
    audit = json.loads(audit_path.read_text()) if audit_path.exists() else {}
    collated = (audit.get("status") == "complete" and audit.get("checked_pages") == 116
                and audit.get("collated_page_pairs") == 58 and not audit.get("errors")
                and len(audit.get("pages", [])) == 116)
    for page in audit.get("pages", []):
        path = ROOT / "checked_pages" / (page["key"] + ".tex")
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != page.get("sha256"):
            collated = False
    coverage_path = ROOT / "records" / "COLLATION_PAGE_COVERAGE.tsv"
    if coverage_path.exists():
        with coverage_path.open(newline="") as stream:
            coverage = list(csv.DictReader(stream, delimiter="\t"))
    else:
        coverage = []
    collated = collated and len(coverage) == 58
    for pair in coverage:
        for number in [1, 2]:
            path = ROOT / "checked_pages" / (pair[f"copy{number}_key"] + ".tex")
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != pair.get(f"copy{number}_checked_sha256"):
                collated = False
    if not collated:
        return "translated; awaiting final collation variants and edition QA"
    gate_path = ROOT / "records" / "RELEASE_VALIDATION.json"
    gate = json.loads(gate_path.read_text()) if gate_path.exists() else {}
    build_path = ROOT / "BUILD_INPUTS.json"
    build = json.loads(build_path.read_text()) if build_path.exists() else {}
    current = (bool(gate.get("passed")) and len(gate.get("documents", {})) == 8
               and build.get("input_sha256") == input_snapshot(ROOT))
    for name, record in gate.get("documents", {}).items():
        sources = list(ROOT.glob("*/" + name + ".tex"))
        if len(sources) != 1:
            current = False
            continue
        source = sources[0]
        pdf = source.with_suffix(".pdf")
        current = current and source.exists() and pdf.exists()
        if source.exists() and pdf.exists():
            current = current and hashlib.sha256(source.read_bytes()).hexdigest() == record.get("source_sha256")
            current = current and hashlib.sha256(pdf.read_bytes()).hexdigest() == record.get("pdf_sha256")
    if current:
        return "translation and two-copy collation complete; final edition validation passed for the current PDF hashes"
    return "translation and two-copy collation complete; awaiting final edition QA"


def main():
    records = []
    status = completion_status()
    for path in sorted((ROOT / "translated_pages").glob("*.tex")):
        source = ROOT / "checked_pages" / path.name
        french = source.read_text()
        english = path.read_text()
        french_math = fragments(french)
        english_math = fragments(english)
        if french_math != english_math:
            raise ValueError(f"Mathematical-fragment mismatch: {path.name}")
        if diagrams(french) != diagrams(english):
            raise ValueError(f"Diagram mismatch: {path.name}")
        for mark in ("unsure", "illegible"):
            if french.count("\\" + mark + "{") != english.count("\\" + mark + "{"):
                raise ValueError(f"Doubt-mark count mismatch: {path.name}, {mark}")
        if re.findall(r"\\scanpage\{([^}]+)\}", french) != re.findall(r"\\scanpage\{([^}]+)\}", english):
            raise ValueError(f"Scan-mark mismatch: {path.name}")
        records.append({
            "key": path.stem,
            "source": "checked_pages/" + path.name,
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "translation": "translated_pages/" + path.name,
            "translation_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "math_fragments": french_math,
            "diagram_fragments": diagrams(french),
            "translator_note_ids": re.findall(r"\\tnote\{([^}]+)\}", english),
            "variant_ids": re.findall(r"\\var\{.*?\}\{.*?\}\{.*?\}\{(V[^}]+)\}", english),
            "french_source_apparatus_ids": re.findall(r"\\frapparatus\{([^}]+)\}", english),
            "status": status,
        })
    (ROOT / "translated_pages" / "TRANSLATION_INDEX.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({
        "translated_pages": len(records),
        "mathematical_fragments": sum(len(row["math_fragments"]) for row in records),
        "diagrams": sum(len(row["diagram_fragments"]) for row in records),
        "translator_notes": sum(len(row["translator_note_ids"]) for row in records),
        "explicit_english_variants": sum(len(row["variant_ids"]) for row in records),
        "french_source_apparatus_notes": sum(len(row["french_source_apparatus_ids"]) for row in records),
    }))


if __name__ == "__main__":
    main()
