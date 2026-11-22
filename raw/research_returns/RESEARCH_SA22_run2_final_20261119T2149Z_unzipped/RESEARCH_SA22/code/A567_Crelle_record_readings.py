"""Record the completed source audit; no mathematical computation or new proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc).isoformat()
clock = time.perf_counter()
ledger = root / "notes/A567_sources.md"
events = root / "A567_CHECK_EVENTS.tsv"
before = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in (ledger, events)}
lines = ledger.read_text().splitlines()
replacements = {
    "15. **Nakamura (1990).**": (
        "15. **Nakamura (1990), two distinct originals.** The initial publisher, "
        "old DigiZeitschriften and author-mirror attempts did not obtain the bodies. "
        "On 19 November 2026 at 20:05 UTC, actual GDZ metadata search and advertised "
        "IIIF manifests supplied both originals: "
        "https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0405/LOG_0009.pdf "
        "(volume 405,117–130) and "
        "https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0411/LOG_0014.pdf "
        "(volume 411,205–216). Both bodies were OCR-read; original 405pp117–118 and "
        "411pp205–210,215 were visually checked. The 405 metabelian results retain "
        "their extra hypotheses. The 411 Definition3.3/Theorem3.4 is the original "
        "smooth-cusp criterion; Theorems5.10/6.1 reconstruct objects and the cusp "
        "permutation without asserting full realization of a prescribed group "
        "isomorphism. The main proof retains the previously opened, precisely "
        "scoped Stix input. Full reading/provenance comparison: "
        "notes/A567_Crelle_original_source_audit.md; original receipts/hashes: "
        "logs/A567_Crelle_article_pdfs.json."
    ),
    "16. **Ihara and Nakamura (1997),": (
        "16. **Ihara and Nakamura (1997), On deformation of maximally degenerate "
        "stable marked curves and Oda's problem.** Initial publisher metadata and "
        "official bibliography were opened (turn223293776view1,turn494147355view0) "
        "but did not supply the body. The public original was obtained at 20:05 UTC "
        "on 19 November 2026 from the advertised GDZ manifest: "
        "https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0487/LOG_0009.pdf . "
        "Bodypp125–151 was OCR-read; originalpp125–127,146–149 visually checked. "
        "Canonical parametrization retains both tangential structure and node "
        "ordering. Theorem2' compares Galois actions for the chosen deformation. "
        "Corollary4.2.2 proves Oda equality for n>=1, with the unpunctured case "
        "separately credited to Takao. The additional GDZcanvas is blank, resolving "
        "printed pagination as125–151. Exact scope: "
        "notes/A567_Crelle_original_source_audit.md."
    ),
}
replaced = []
for index, line in enumerate(lines):
    for prefix, replacement in replacements.items():
        if line.startswith(prefix):
            lines[index] = replacement
            replaced.append(prefix)
if len(replaced) != 2:
    raise RuntimeError(f"Expected exactly two old source entries, found {replaced!r}")
ledger.write_text("\n".join(lines) + "\n")
who = "GPT-6 Astra (OpenAI); inherited reasoning effort; run /root/geometry_a567; ChatGPT Pro mode"
date = datetime.now(timezone.utc).date().isoformat()
event_data = [
    ("A.6.Nakamura405-original", "used and rechecked in this run",
     "Original public GDZ article obtained; pp117–130 OCR-read and pp117–118 visually checked. Theorems A/B retain metabelian and extra field/unit hypotheses; Theorem C recovers the multiplicative-difference invariant only. No new full Isom-set theorem asserted. See notes/A567_Crelle_original_source_audit.md."),
    ("A:inertia-maximality", "used and rechecked in this run",
     "Original Nakamura411 pp205–216 OCR-read; pp205–210,215 visually checked. Definition3.3/Lemma3.1/Theorem3.4 proof confirms the number-field smooth-cusp criterion underlying the existing Stix input. No arbitrary singular maximality criterion or new proof claimed. See notes/A567_Crelle_original_source_audit.md."),
    ("L6", "used and rechecked in this run",
     "Original Ihara–Nakamura1997 pp125–151 OCR-read; pp125–127,146–149 visually checked. Theorem2' is chosen-deformation action-kernel comparison; Cor4.2.2 proves Oda equality for n>=1 using earlier opposite inclusion. Source does not itself prove every claim049a–c. Extra GDZcanvas blank; pagination125–151. See notes/A567_Crelle_original_source_audit.md."),
]
with events.open("a") as out:
    for statement_id, kind, outcome in event_data:
        out.write("\t".join((statement_id, date, who, kind, outcome)) + "\n")
report = {
    "started_at_utc": started,
    "finished_at_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": time.perf_counter() - clock,
    "scope": "Metadata recording only; no mathematical test, new re-proof, or source request",
    "source_entries_updated": len(replaced),
    "check_events_appended": len(event_data),
    "event_statement_ids": [entry[0] for entry in event_data],
    "before_sha256": before,
    "after_sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (ledger, events)},
    "read_scope": {
        "Nakamura405": {"ocr_pages": "117–130", "original_images": [117, 118]},
        "Nakamura411": {"ocr_pages": "205–216", "original_images": [205,206,207,208,209,210,215]},
        "IharaNakamura487": {"ocr_pages": "125–151", "original_images": [125,126,127,146,147,148,149], "blank_canvas_checked": 152},
    },
    "bibliography_keys": ["A567_Nakamura1990Metabelian", "A567_Nakamura1990", "A567_IharaNakamura1997"],
    "main_tex_edited": False,
}
destination = root / "logs/A567_Crelle_source_audit_record.json"
destination.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(report, indent=2, ensure_ascii=False))
