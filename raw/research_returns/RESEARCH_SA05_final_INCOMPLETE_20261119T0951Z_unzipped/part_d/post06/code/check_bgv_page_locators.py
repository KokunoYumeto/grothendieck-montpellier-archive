"""Locate exact numbered statements in the archived primary PDF extraction."""
from pathlib import Path
import json

base = Path(__file__).resolve().parents[1]
pages = (base / "sources/BindaGallauerVezzani2024V2.txt").read_text().split("\f")
needles = [
    "Lemma 2.13.", "Lemma 2.17.", "Lemma 2.31.", "Proposition 2.32.",
    "Proposition 4.13.", "Corollary 4.14.", "Proposition 4.25.",
    "Corollary 4.33.", "Remark 4.61.",
]
result = {needle: [i + 1 for i, page in enumerate(pages) if needle in page] for needle in needles}
result["scope"] = "All occurrences, including cross-references; the first statement occurrence was checked against the primary text."
target = base / "output/bgv_page_locators.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
