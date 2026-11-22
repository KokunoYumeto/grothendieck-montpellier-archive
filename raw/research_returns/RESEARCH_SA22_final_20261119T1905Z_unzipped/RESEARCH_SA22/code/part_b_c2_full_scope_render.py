"""Render original C.2 sheets for the independent hypothesis-scope audit.

This is source preparation, not a mathematical finite check. No network requests.
"""
from pathlib import Path
import json
import time
import fitz

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
source = ROOT / "sources" / "cote68.pdf"
pages = [15, 16, 19, 20, 21, 22]
outputs = []
with fitz.open(source) as doc:
    for number in pages:
        target = ROOT / "qa" / f"part_b_c2_scan{number:03d}_scope.png"
        doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(target)
        outputs.append(str(target.relative_to(ROOT)))
result = {
    "scope": "Six original manuscript sheets rendered for visual reading; no mathematical test",
    "source": str(source.relative_to(ROOT)),
    "pdf_pages_one_based": pages,
    "outputs": outputs,
    "network_requests": 0,
    "runtime_seconds": time.perf_counter() - started,
}
output = ROOT / "code" / "part_b_c2_full_scope_render_output.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
