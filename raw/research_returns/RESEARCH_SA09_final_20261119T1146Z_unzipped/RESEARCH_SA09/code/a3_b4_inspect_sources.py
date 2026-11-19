"""Render the complete Schinzel correction and record precise Toën source locators."""
from pathlib import Path
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
rendered = []
with fitz.open(ROOT / "sources" / "schinzel_corr.pdf") as doc:
    for i, page in enumerate(doc):
        target = ROOT / "qa" / f"schinzel-correction-{i+1}.png"
        page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(target)
        rendered.append({"page": i+1, "file": str(target.relative_to(ROOT))})
source = ROOT / "sources" / "toen" / "epiga_vol4_Toen.tex"
lines = source.read_text().splitlines()
labels = ["\\label{p3}", "\\label{c4}", "\\label{c6}", "\\label{c7}"]
locators = []
for label in labels:
    hits = [i for i, line in enumerate(lines) if label in line]
    assert len(hits) == 1
    i = hits[0]
    j = i+1
    while j < len(lines) and not lines[j].startswith("\\end{"):
        j += 1
    locators.append({"label": label, "start_line": i+1, "end_line": j+1,
                     "statement": "\n".join(lines[i:j+1])})
result = {"rendered_schinzel_correction": rendered, "toen_locators": locators}
(ROOT / "logs" / "a3_b4_inspect_sources.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"rendered_pages": len(rendered), "toen_statements": len(locators)}))
