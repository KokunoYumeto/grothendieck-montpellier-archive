"""Keep the raw catalogue excerpt in the established source-cache location."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
old = root / "notes/geometry_schatten_hunter_faculty_section.txt"
new = root / "sources/geometry_schatten_hunter_faculty_section.txt"
assert old.exists() and not new.exists()
sha = hashlib.sha256(old.read_bytes()).hexdigest()
size = old.stat().st_size
old.rename(new)
assert hashlib.sha256(new.read_bytes()).hexdigest() == sha
note = root / "notes/geometry_schatten_inventory_date_audit.md"
text = note.read_text()
assert "notes/geometry_schatten_hunter_faculty_section.txt" in text
text = text.replace("notes/geometry_schatten_hunter_faculty_section.txt", "sources/geometry_schatten_hunter_faculty_section.txt")
text += "\nSource-cache relocation: the raw faculty-section excerpt was moved unchanged from its initial `notes/` path into `sources/`; exact old/new path and hash are preserved in `logs/geometry_schatten_excerpt_relocate.json`. The actual executed retrieval program and its initial output remain unchanged as historical records.\n"
note.write_text(text)
record = {"utc": datetime.now(timezone.utc).isoformat(), "old_path": str(old.relative_to(root)), "new_path": str(new.relative_to(root)), "bytes": size, "sha256": sha, "byte_for_byte_preserved": True, "reason": "Raw retrieved catalogue text follows the existing source-cache exclusion policy", "mathematical_movement": False}
(root / "logs/geometry_schatten_excerpt_relocate.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
