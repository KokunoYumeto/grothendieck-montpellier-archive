"""Create a new scheduled TRACE_DET checkpoint; never modify an earlier ZIP."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
START = datetime(2026, 11, 20, 23, 51, tzinfo=timezone.utc)
SKIP_NAMES = {"pdflatex.fmt", "pdftex.map", "pdflatex.log", "texsys.aux"}
SKIP_SUFFIXES = {".aux", ".toc", ".out", ".fmt", ".pyc"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    due = START + timedelta(minutes=45 * args.number)
    if now < due or now > due + timedelta(minutes=3):
        raise SystemExit(f"Not in scheduled checkpoint window: now={now}, due={due}")
    destination = ROOT / f"TRACE_DET_checkpoint_{args.number:02d}.zip"
    if destination.exists():
        raise SystemExit(f"Refusing to modify existing checkpoint: {destination}")
    items = {}
    for path in sorted((ROOT / "deliverables").glob("*")):
        if path.is_file() and path.suffix not in SKIP_SUFFIXES and path.suffix != ".log":
            items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for path in sorted((ROOT / "work").iterdir()):
        if path.is_file() and path.name not in SKIP_NAMES and path.suffix not in SKIP_SUFFIXES:
            items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for directory in ["library_helpers", "pdf_qa", "pdf_qa_final", "step6_tex_check"]:
        for path in sorted((ROOT / "work" / directory).rglob("*")):
            if path.is_file() and path.suffix not in SKIP_SUFFIXES:
                items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    # Source retrieval manifests are retained; external full-text caches and the
    # reproducible 239 MB public Lean archive are inputs, not duplicated here.
    for directory in ["programme_sources", "character_sources", "source_extra"]:
        for path in sorted((ROOT / "work" / directory).rglob("*")):
            if path.is_file() and path.suffix in {".json", ".tsv", ".md"}:
                items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    prompt = ROOT / "upload" / "PROMPT(20261120-235243).md"
    items["REQUEST.md"] = prompt.read_bytes()
    state = {"checkpoint": args.number, "created_utc": now.isoformat(),
             "scheduled_utc": due.isoformat(), "status": "ONGOING",
             "note": "All current deliverables and work documentation; draft proof parts may be newer than the compiled paper. No earlier checkpoint is nested. Reproducible external inputs and runtime files are excluded as documented in work/checkpoint_scope.md."}
    items["CHECKPOINT_STATE.json"] = (json.dumps(state, indent=2) + "\n").encode()
    manifest = "".join(f"{hashlib.sha256(data).hexdigest()}  {name}\n"
                       for name, data in sorted(items.items()))
    items["MANIFEST.sha256"] = manifest.encode()
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6) as archive:
        for name, data in sorted(items.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(destination) as archive:
        error = archive.testzip()
        if error:
            raise RuntimeError(f"ZIP CRC failure: {error}")
    result = {**state, "path": str(destination), "entries": len(items),
              "bytes": destination.stat().st_size,
              "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
