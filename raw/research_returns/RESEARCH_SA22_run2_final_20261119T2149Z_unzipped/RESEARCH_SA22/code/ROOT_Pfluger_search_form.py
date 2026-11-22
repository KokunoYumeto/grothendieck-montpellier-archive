"""Inspect the public catalogue query parameters in the downloaded client."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "literature/ROOT_Pfluger_current_publisher_app.js").read_text()
needle = '"/api/public/search/all"'
index = source.index(needle)
excerpt = source[index - 2400:index + 1000]
(ROOT / "logs/ROOT_Pfluger_search_form.txt").write_text(excerpt + "\n")
print(excerpt)
