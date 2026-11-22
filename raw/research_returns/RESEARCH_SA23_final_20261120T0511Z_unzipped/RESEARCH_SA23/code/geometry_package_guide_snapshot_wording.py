"""Keep preparation claims dated in the eventual final-package guide."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
path = root / "notes/geometry_final_package_README.md"
before = hashlib.sha256(path.read_bytes()).hexdigest()
text = path.read_text()
replacements = [
    ("# Final-package preparation — no final archive created", "# Final-package guide and preparation record"),
    ("This is packaging work. It does not constitute mathematical movement and\ndoes not determine whether the formal stopping rule has triggered.", "This guide records packaging preparation and gives creation and restoration\ninstructions. Packaging does not constitute mathematical movement or decide\nwhether the formal stopping rule has triggered. The dated preparation\nsnapshots below are historical records; actual final creation, if performed,\nis established by its verified creation result and generated manifest."),
    ("No archive-creation branch was executed. Writers must be quiescent for the\nlater final run", "The 03:36:48 UTC preparation audit executed no archive-creation branch.\nWriters must be quiescent for an actual final run"),
    ("Current duplicate paths in this\nsnapshot are logs and an empty note; no executable code or TeX input is\nlost as a direct-path alias.", "At the initial preparation snapshot, duplicate current paths were logs\nand an empty note; no executable code or TeX input was a direct-path alias.\nThe actual final manifest records the aliases at creation time."),
    ("## Later creation command, only after the stopping rule triggers\n\nThe branch below is prepared but **has not been run**:", "## Creation command, after the stopping rule is documented\n\nAfter the formal stopping decision, create the final package with:"),
    ("The creation branch was independently code-reviewed but\nwas not executed, as required by the parent instruction.", "The preparation-only audits described above independently reviewed this\nbranch without executing it. A later successful creation must be evidenced\nby its verified result and generated manifest; this guide does not assert\nthat creation has occurred.")
]
for old, new in replacements:
    assert text.count(old) == 1, old
    text = text.replace(old, new, 1)
path.write_text(text)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation only; no mathematical movement or archive creation", "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "historical_estimates_preserved": True, "permanent_no_archive_assertion_removed": True}
(root / "logs/geometry_package_guide_snapshot_wording.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
