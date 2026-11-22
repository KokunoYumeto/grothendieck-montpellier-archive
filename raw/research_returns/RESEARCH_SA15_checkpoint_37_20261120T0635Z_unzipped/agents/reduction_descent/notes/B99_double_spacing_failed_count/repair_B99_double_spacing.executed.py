from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json
own = Path(__file__).resolve().parents[1]
p = own/"B_valuation_one_irreducible_candidate.tex"
old = p.read_text()
number = old.count(r"\q\quad")
assert number == 7, number
new = old.replace(r"\q\quad", r"\qquad")
hist = own/"notes/B99_double_spacing_repair"
hist.mkdir(exist_ok=False)
(hist/"candidate.before.tex").write_text(old)
(hist/"candidate.diff").write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="candidate.before.tex", tofile=p.name)))
p.write_text(new)
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
record = {"actual_utc": datetime.now(timezone.utc).isoformat(),
          "kind": "typesetting-only repair of seven erroneous double spacing tokens",
          "before_sha256": hashlib.sha256(old.encode()).hexdigest(),
          "after_sha256": sha(p), "replacements": number,
          "scope": "Earlier spacing regex matched inside seven existing qquad commands. Restore them literally; mathematics and executed certificate/output unchanged."}
(hist/"record.json").write_text(json.dumps(record, indent=2)+"\n")
rec = own/"outputs/B99_candidate_record.json"
prior = json.loads(rec.read_text())
(hist/"B99_candidate_record.before.json").write_bytes(rec.read_bytes())
prior["candidate_sha256"] = sha(p)
prior["typography_delta"] = record
rec.write_text(json.dumps(prior, indent=2)+"\n")
print(json.dumps(record, indent=2))
