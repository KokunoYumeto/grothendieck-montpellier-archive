#!/usr/bin/env python3
"""Record translated-page provenance and exact mathematical-fragment parity."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
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


def main():
    records = []
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
            "status": "translated; awaiting final collation variants and edition QA",
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
