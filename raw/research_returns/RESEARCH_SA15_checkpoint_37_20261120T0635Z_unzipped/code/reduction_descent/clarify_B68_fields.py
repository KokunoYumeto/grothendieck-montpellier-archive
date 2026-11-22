from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, difflib

base = Path(__file__).resolve().parents[1]
path = base / "B_initial_tame_sector_candidate.tex"
old = path.read_text()
assert hashlib.sha256(path.read_bytes()).hexdigest() == "382dbf5436c3dcfe6dae47ddc077259294b75ae4384d952c7922a6bffa7e2980"
(base / "notes/B_initial_tame_sector.before_field_typing.tex").write_text(old)
new = old.replace("it is a torsor under\n+the", "it is a torsor under\n+the") if False else old
assert r"the \(L\)-rational first-level module" in new
new = new.replace(r"the \(L\)-rational first-level module", r"the \(R\)-rational first-level module")
assert "If the special characters differ, their residual tame spectra\n+are disjoint." not in new
target = "If the special characters differ, their residual tame spectra\n+are disjoint.".replace("\n+", "\n")
assert target in new
new = new.replace(target, "If the special characters differ, their finite special inertia\n+eigenvalue orbits are disjoint.".replace("\n+", "\n"))
path.write_text(new)
(base / "notes/B68_field_typing.diff").write_text("".join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile="before_field_typing",tofile="corrected_candidate")))
record_path = base / "outputs/B68_candidate_record.json"
(base / "outputs/B68_candidate_record.before_field_typing.json").write_bytes(record_path.read_bytes())
record = json.loads(record_path.read_text())
record["candidate_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
record["field_typing_correction_utc"] = datetime.now(timezone.utc).isoformat()
record["field_typing_correction"] = "Root audit corrected first-level rationality in the wild point-field paragraph from L to R, and made disjoint spectra explicitly the finite special inertia orbits. Mathematical comparison arguments and exact program unchanged."
record_path.write_text(json.dumps(record,indent=2)+"\n")
with (base/"CHECK_EVENTS.tsv").open("a") as f:
    f.write("\t".join([record["field_typing_correction_utc"],"B68-field-typing","CANDIDATE_CORRECTED","Wild point-field torsor is under R-rational first-level module; disjoint spectra are special inertia orbits","B_initial_tame_sector_candidate.tex;notes/B68_field_typing.diff","Root requested precision corrections; exact prior candidate preserved; no program or inequality changed"])+"\n")
print(json.dumps({"actual_utc":record["field_typing_correction_utc"],"candidate_sha256":record["candidate_sha256"],"status":"CORRECTED_CANDIDATE"},indent=2))
