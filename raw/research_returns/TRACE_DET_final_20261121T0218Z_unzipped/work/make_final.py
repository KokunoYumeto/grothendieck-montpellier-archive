"""Package the frozen TRACE_DET release once, then verify every payload hash.

The final ZIP is immutable: an existing destination is never overwritten.
External source caches, runtime files and all prior ZIPs are excluded.
This script checks release structure, not mathematical truth.
"""
from pathlib import Path
from datetime import datetime, timezone
import collections
import csv
import hashlib
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DELIVERABLES = ROOT / "deliverables" if (ROOT / "deliverables").is_dir() else ROOT
REQUIRED = [
    "TRACE_DET.tex", "TRACE_DET.pdf", "QUESTIONS.tsv", "LEDGER.md",
    "CHECK_EVENTS.tsv", "IMPLICATIONS.md", "TRANSCRIPTION_NOTES.tsv",
    "README.md", "EVIDENCE_INDEX.md",
]
SKIP_NAMES = {
    "pdflatex.fmt", "pdftex.map", "pdflatex.log", "texsys.aux",
    "format_build.log", "tectonic_build_1.log", "step6_ramare_page1.png",
    "final_release_receipt.json",
}
SKIP_SUFFIXES = {".aux", ".toc", ".out", ".fmt", ".pyc", ".zip"}


def table(data):
    return list(csv.reader(io.StringIO(data.decode()), delimiter="\t"))


def main():
    destination = ROOT / "TRACE_DET_final.zip"
    if destination.exists():
        raise SystemExit("Refusing to overwrite an existing final ZIP")
    items = {name: (DELIVERABLES / name).read_bytes() for name in REQUIRED}
    for path in sorted((ROOT / "work").iterdir()):
        if path.is_file() and path.name not in SKIP_NAMES and path.suffix not in SKIP_SUFFIXES:
            items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for directory in sorted((ROOT / "work").iterdir()):
        if directory.is_dir() and (directory.name.startswith("pdf_qa") or directory.name == "step6_tex_check"):
            for path in sorted(directory.rglob("*")):
                if path.is_file() and path.suffix not in SKIP_SUFFIXES:
                    items[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    prompt = ROOT / "upload" / "PROMPT(20261120-235243).md"
    if not prompt.exists():
        prompt = ROOT / "REQUEST.md"
    items["REQUEST.md"] = prompt.read_bytes()

    questions = table(items["QUESTIONS.tsv"])
    events = table(items["CHECK_EVENTS.tsv"])
    notes = table(items["TRANSCRIPTION_NOTES.tsv"])
    assert len(questions) == 80 and all(len(r) == 4 for r in questions)
    assert len(events) == 427 and all(len(r) == 6 for r in events)
    assert len(notes) == 17 and all(len(r) == 7 for r in notes)
    assert len({r[0] for r in questions[1:]}) == 79
    for event in events[1:]:
        assert "work/" + event[5] in items, event[5]
        assert event[5] != "root_independent_events.tsv"
    assert hashlib.sha256(items["TRACE_DET.tex"]).hexdigest() == "e059ae1ec4061ebce92588dc8245b964ccb32581cf1ba02da9b3d623e71e2e60"
    assert hashlib.sha256(items["TRACE_DET.pdf"]).hexdigest() == "3def7f81cdc8fe4da551a4bdb2ead726b956071047400bf6c564409e2e51fe7e"
    assert all(not name.endswith(".zip") and ".." not in Path(name).parts for name in items)
    assert not any("external_lean/" in name or name.endswith("lean.tar.gz") for name in items)

    now = datetime.now(timezone.utc)
    state = {
        "run": "TRACE_DET_20261121",
        "created_utc": now.isoformat(),
        "status": "INCOMPLETE",
        "status_scope": "Exact historical step1/4/full7 matching, direct finite-sign transfer, and manuscript-image attribution remain unresolved; completed findings retain their proved/refuted and conditional scopes.",
        "question_rows": len(questions) - 1,
        "check_events": len(events) - 1,
        "check_event_types": dict(collections.Counter(r[3] for r in events[1:])),
        "transcription_rows": len(notes) - 1,
        "pdf_pages": 81,
        "final_build": 23,
        "open_question_ids": [r[0] for r in questions[1:] if r[3].startswith("CURRENT")],
        "first_three_hour_review_due_utc": "2026-11-21T02:51:00+00:00",
        "three_hour_review_occurred": False,
        "no_movement_stop_triggered": False,
        "nested_checkpoints": False,
        "scope_note": "All required deliverables and research documentation are included. Reproducible external full-source caches and runtime files are excluded. Supplied attachments remain the input set for continuation. No Lean build or authorship authentication is claimed.",
    }
    if now >= datetime(2026, 11, 21, 2, 51, tzinfo=timezone.utc):
        raise SystemExit("Scheduled checkpoint/review boundary reached; update status before packaging")
    state["archive_entries_including_metadata_and_manifest"] = len(items) + 2
    items["RELEASE_STATE.json"] = (json.dumps(state, indent=2) + "\n").encode()
    checksums = {name: hashlib.sha256(data).hexdigest() for name, data in items.items()}
    items["MANIFEST.sha256"] = "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())).encode()
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name, data in sorted(items.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None, "ZIP CRC failure"
        assert set(archive.namelist()) == set(items)
        assert len(archive.namelist()) == len(set(archive.namelist()))
        for name, expected in checksums.items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == expected, name
        assert archive.read("MANIFEST.sha256") == items["MANIFEST.sha256"]
    result = {
        **state,
        "path": str(destination),
        "entries": len(items),
        "bytes": destination.stat().st_size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "zip_crc_and_all_payload_hashes": "PASS",
    }
    (ROOT / "work" / "final_release_receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
