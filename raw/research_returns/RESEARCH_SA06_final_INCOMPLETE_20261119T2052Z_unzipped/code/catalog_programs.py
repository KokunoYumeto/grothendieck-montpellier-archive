"""Collect all contributed programs and exact outputs into the code deliverable.

Original executable locations remain authoritative.  Byte-identical copies
under code/retained_programs satisfy the consolidated code-folder delivery
requirement without altering the relative paths used by the original programs.
No third-party source PDF, source extraction or rendered page is copied.
"""
from pathlib import Path
import ast
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "code" / "retained_programs"
programs = sorted((ROOT / "code").glob("*.py")) + sorted((ROOT / "agents").glob("*/code/*.py"))
files = set(programs)
for directory in (ROOT / "agents").glob("*/code"):
    files.update(path for path in directory.iterdir()
                 if path.is_file() and path.suffix in {".out", ".json", ".txt"})
for directory in (ROOT / "agents").glob("*/output"):
    files.update(path for path in directory.iterdir()
                 if path.is_file() and path.suffix in {".out", ".json", ".txt"}
                 and not path.name.startswith("grabowski-")
                 and "compile" not in path.name and "_check.out" not in path.name)
files.update(path for path in (ROOT / "code").glob("*.json")
             if path.is_file() and path.name != "program_files_output.json")
files.update(path for path in (ROOT / "code" / "timing_runs").glob("*.txt") if path.is_file())
records = []
for path in sorted(files):
    relative = path.relative_to(ROOT)
    if relative.parts[0] == "agents":
        copy = DEST / relative
        copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, copy)
        collected = str(copy.relative_to(ROOT))
    else:
        collected = str(relative)
    body = path.read_bytes()
    records.append({"original": str(relative), "collected": collected,
                    "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
index = ["# Program and output index", "",
         "All source programs are listed below. Contributor programs and their outputs also have byte-identical copies under `code/retained_programs/`; use the original locations in the table for execution so that relative input and output paths retain their documented meaning. Root programs already reside in `code/`.", "",
         "Exact finite certificates establish only the scope stated in each program and its mathematical proof. Retrieval and layout scripts supply provenance and verification, not mathematical theorems. Instrumented durations are in the original outputs or `code/computation_timing_output.json`; the full timing-run stdout is retained. A still-running retrieval has no completed result and is not evidence of inspection.", "",
         "| Executable source location | Stated scope |", "|---|---|"]
for path in programs:
    try:
        doc = ast.get_docstring(ast.parse(path.read_text())) or "See program and accompanying report."
    except SyntaxError:
        doc = "Source being edited; inspect before executing."
    scope = doc.splitlines()[0].replace("|", "\\|")
    index.append(f"| `{path.relative_to(ROOT)}` | {scope} |")
index += ["", "The complete program/output correspondence, hashes and consolidated paths are in `code/program_files_output.json`. Bibliographic retrieval records retain failed attempts as well as later successful openings.", ""]
(ROOT / "code" / "PROGRAM_INDEX.md").write_text("\n".join(index))
(ROOT / "code" / "program_files_output.json").write_text(json.dumps(records, indent=2))
print(json.dumps({"programs": len(programs), "retained_files": len(records)}))
