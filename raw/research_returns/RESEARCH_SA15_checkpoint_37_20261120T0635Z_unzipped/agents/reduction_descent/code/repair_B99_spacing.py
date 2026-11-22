from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
p = own/"B_valuation_one_irreducible_candidate.tex"
old = p.read_text()
new, number = re.subn(r"(?<!\\)(q?quad)\b", lambda m: "\\"+m[1], old)
assert number == 15, number
hist = own/"notes/B99_spacing_repair"
hist.mkdir(exist_ok=False)
(hist/"candidate.before.tex").write_text(old)
(hist/"candidate.diff").write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="candidate.before.tex", tofile=p.name)))
p.write_text(new)
record = {"actual_utc": datetime.now(timezone.utc).isoformat(), "kind": "typesetting-only literal spacing escapes",
          "replacements": number, "before_sha256": hashlib.sha256(old.encode()).hexdigest(),
          "after_sha256": hashlib.sha256(new.encode()).hexdigest(),
          "scope": "No mathematical or certificate assertion changed."}
(hist/"record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
