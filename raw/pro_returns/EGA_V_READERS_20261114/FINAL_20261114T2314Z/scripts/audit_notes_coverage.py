#!/usr/bin/env python3
"""Crosswalk supplied NOTES concerns to existing recorded scan decisions.

Exact textual or explicit numbered documentary matches are accepted. Similarity
only supplies follow-up candidates; it never establishes that a concern was read.
Reviewers may add explicit mappings in NOTES_CROSSWALK_REVIEWED.tsv.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from difflib import SequenceMatcher
import json
import fcntl
from pathlib import Path
import re
import unicodedata
from edition_core import read_tsv, write_tsv, sha256

EDITION = Path(__file__).resolve().parents[1]
SOURCES = (
    "transcription/ega_v_cote25/NOTES.tsv",
    "transcription/ega_v_cote24_blass/NOTES.tsv",
)


def normalized(text):
    text = unicodedata.normalize("NFC", text).casefold()
    text = text.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-"}))
    return re.sub(r"\s+", " ", text).strip().lstrip("- ").rstrip(". ")


def words(text):
    stop = {"the", "and", "that", "this", "with", "from", "which", "there", "page", "scan",
            "check", "read", "line", "typed", "handwritten", "source", "notes", "note"}
    return {x for x in re.findall(r"\w+", normalized(text)) if len(x) > 2 and x not in stop}


def main():
    decisions = read_tsv(EDITION / "CHECK_DECISIONS.tsv")
    bykey = defaultdict(list)
    byid = {r["id"]: r for r in decisions}
    for row in decisions:
        combined = " ".join(row.get(k, "") for k in ("transcription_reading", "image_reading", "decision", "reason", "category"))
        bykey[row["key"]].append((row, normalized(combined), words(combined)))
    review_path = EDITION / "records/NOTES_CROSSWALK_REVIEWED.tsv"
    with (EDITION / "records/NOTES_CROSSWALK.lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        reviewed = {r["concern_id"]: r for r in read_tsv(review_path)} if review_path.is_file() else {}
        for name in ("root", "middle", "late", "pipeline"):
            part = EDITION / "records" / ("NOTES_CROSSWALK_" + name + ".tsv")
            if not part.is_file():
                continue
            for row in read_tsv(part):
                prior = reviewed.get(row["concern_id"])
                if prior and (prior.get("decision_ids"), prior.get("reason")) != (row.get("decision_ids"), row.get("reason")):
                    raise SystemExit("Conflicting reviewed NOTES mapping: " + row["concern_id"])
                reviewed[row["concern_id"]] = row
        if reviewed:
            values = [reviewed[k] for k in sorted(reviewed)]
            fields = list(dict.fromkeys(k for row in values for k in row))
            write_tsv(review_path, values, fields)
        fcntl.flock(handle, fcntl.LOCK_UN)
    inventory = []
    invalid = []
    for relative in SOURCES:
        for source in read_tsv(EDITION.parent / "source" / relative):
            items = [x.strip() for x in source["notes"].split(" | ") if x.strip()]
            for ordinal, concern in enumerate(items, 1):
                key = source["key"]
                cid = f"{key}-N{ordinal:03}"
                target = normalized(concern)
                matches = []
                method = ""
                manual = reviewed.get(cid)
                if manual:
                    ids = manual.get("decision_ids", "").split()
                    if (ids and manual.get("reason", "").strip()
                        and manual.get("concern_sha256")==sha256(concern)
                        and all(x in byid and byid[x]["key"] == key for x in ids)):
                        matches = ids
                        method = "reviewer documentary crosswalk: " + manual["reason"]
                    else:
                        invalid.append(cid)
                if not matches:
                    for row, text, _ in bykey[key]:
                        if target and target in text:
                            matches.append(row["id"])
                    if matches:
                        method = "complete concern text occurs in the recorded decision"
                if not matches:
                    for row, _, _ in bykey[key]:
                        refs = re.findall(r"(?i)\bNOTES(?:\.tsv)?\s*(?:item\s*)?(?:#|no[.]?\s*)?(\d+)\b",
                                          row.get("transcription_reading", "") + " " + row.get("reason", ""))
                        if str(ordinal) in refs:
                            matches.append(row["id"])
                    if matches:
                        method = "explicit NOTES item number in this page's decision"
                candidates = []
                if not matches:
                    tokens = words(concern)
                    for row, text, record_tokens in bykey[key]:
                        overlap = len(tokens & record_tokens) / max(1, len(tokens))
                        sequence = SequenceMatcher(None, target, normalized(row.get("transcription_reading", ""))).ratio()
                        score = max(overlap, sequence)
                        if score >= .12:
                            candidates.append((score, row["id"]))
                    candidates.sort(reverse=True)
                inventory.append(dict(concern_id=cid, key=key, cote=source["cote"], site=source["site"],
                    source_file=relative, item=ordinal, concern=concern, concern_sha256=sha256(concern),
                    status="documentary match" if matches else "reviewer mapping required",
                    decision_ids=" ".join(dict.fromkeys(matches)), method=method,
                    candidate_decision_ids=" ".join(f"{identity}:{score:.3f}" for score, identity in candidates[:4])))
    records = EDITION / "records"
    write_tsv(records / "NOTES_COVERAGE.tsv", inventory)
    unmatched = [r for r in inventory if r["status"] != "documentary match"]
    write_tsv(records / "NOTES_UNMATCHED.tsv", unmatched, list(inventory[0]))
    counts = Counter(r["key"] for r in unmatched)
    summary = dict(source_pages=sum(len(read_tsv(EDITION.parent / "source" / p)) for p in SOURCES),
        concerns=len(inventory), documentary_matches=len(inventory) - len(unmatched),
        reviewer_mapping_required=len(unmatched), unmatched_by_page=dict(sorted(counts.items())),
        invalid_reviewed_mappings=invalid,
        decisions_sha256=sha256((EDITION / "CHECK_DECISIONS.tsv").read_text()),
        reviewed_mappings_sha256=sha256(review_path.read_text()) if review_path.is_file() else "",
        source_notes_sha256={p:sha256((EDITION.parent / "source" / p).read_text()) for p in SOURCES},
        note="Documentary coverage inventories existing decisions; it does not infer or create a visual inspection.")
    (records / "NOTES_COVERAGE_SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k not in ("unmatched_by_page", "note")}))


if __name__ == "__main__":
    main()
