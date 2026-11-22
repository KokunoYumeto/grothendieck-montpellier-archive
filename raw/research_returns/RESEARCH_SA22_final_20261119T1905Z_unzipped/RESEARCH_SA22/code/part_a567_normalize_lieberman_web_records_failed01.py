#!/usr/bin/env python3
"""Normalize eight existing Lieberman web records; no network operations."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path("/workspace/scratch/9c53b536a97f/RESEARCH_SA22")
CACHE = Path("/workspace/scratch/9c53b536a97f/source_reading/recorded_web_search")
NAMES = [
    "part_a567_lieberman_public_collections_queries.json",
    "part_a567_lieberman_ranicki_home.json",
    "part_a567_lieberman_ranicki_indexes.json",
    "part_a567_lieberman_ranicki_collection.json",
    "part_a567_lieberman_ranicki_signature_index.json",
    "part_a567_lieberman_ranicki_targeted_search.json",
    "part_a567_lieberman_ranicki_catalog.json",
    "part_a567_lieberman_ranicki_catalog_find.json",
]
OUTCOMES = [
    "Three exact public-collection/author-title queries found the Ranicki home and later or unrelated citations; no target original passage.",
    "Read actual public Ranicki home and identified its advertised Papers, Surgery bits, and Signatures links.",
    "Read the advertised Papers and Surgery bits pages; Papers is Ranicki's own bibliography, not a complete server inventory.",
    "Read the advertised historical surgery notes collection; no Lieberman target entry.",
    "Read Signatures collection, and found no Lieberman match in the Papers and historical notes pages.",
    "Two exact targeted searches yielded unrelated B.B.Lieberman and later Kahn references plus an actual public catalogue URL; no target original.",
    "Opened the actual public bibliography catalogue, with15147 extracted lines; did not claim to read every entry manually.",
    "Full extracted catalogue text had no match for Lieberman, Numerical and, or Hodge manifolds; this is not a server-wide absence claim.",
]

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def dump_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

def parse_sources(result):
    sources = []
    text_blocks = [c["text"] for c in result.get("content", [])
                   if c.get("type") == "text" and "text" in c]
    for text in text_blocks:
        blocks = re.split(r"\n-{50,}\n", text)
        for block in blocks:
            ref = re.search(r"【(turn[^】]+)】", block)
            if not ref:
                if block.strip():
                    raise ValueError("Unparsed nonempty source block")
                continue
            first = block.strip().splitlines()[0]
            title_url = re.match(r"^(.*?)\s*\((https?://.*)\)$", first)
            if not title_url:
                raise ValueError("Unparsed source heading: " + first)
            entry = {
                "source_ref": ref.group(1),
                "heading": title_url.group(1).strip(),
                "url": title_url.group(2),
            }
            line_count = re.search(r"Total lines: (\d+)", block)
            if line_count:
                entry["reported_extracted_total_lines"] = int(line_count.group(1))
            command = re.search(r"Source: (open|click|find)\((\{.*?\})\);", block)
            if command:
                entry["command"] = {
                    "name": command.group(1),
                    "arguments": json.loads(command.group(2)),
                }
            headings = re.findall(r"^L\d+: (#{1,6} .*)$", block, flags=re.M)
            if headings:
                entry["displayed_headings"] = headings
            no_match = re.search(r'^No matching text found for "(.*?)"$', block, flags=re.M)
            if no_match:
                entry["find_outcome"] = {
                    "matched": False, "pattern": no_match.group(1)
                }
            sources.append(entry)
    return sources

prepared = []
normalized_at = datetime.now(timezone.utc).isoformat()
for name, outcome in zip(NAMES, OUTCOMES):
    path = BASE / "code" / name
    original = path.read_bytes()
    data = json.loads(original)
    if "result" not in data:
        raise RuntimeError("Already normalized or unexpected schema: " + name)
    sources = parse_sources(data["result"])
    record = {k: v for k, v in data.items() if k != "result"}
    commands = [s["command"] for s in sources if "command" in s]
    if name == NAMES[0]:
        commands = [{"name": "system2_search_query", "queries": data["queries"]}]
    elif name == NAMES[5]:
        commands = [{"name": "system1_search_query", "queries": data["queries"]}]
    record.update({
        "record_schema": "bounded_web_execution_metadata_v1",
        "commands": commands,
        "commands_scope": "Exact query payloads or commands recovered from the original tool source metadata; rendering options are not reconstructed.",
        "reported_source_count": len(sources),
        "reported_source_count_scope": "Number of returned source blocks in this saved output, not search-engine total hits.",
        "sources": sources,
        "tool_is_error": data["result"].get("isError", False),
        "bounded_outcome": outcome,
        "named_original_status": "UNREAD; no source-gate or mathematical status change.",
        "normalization": {
            "performed_at_utc": normalized_at,
            "operation": "Metadata-only replacement of an existing saved web output; no web request or mathematical test.",
            "raw_cache_path": str(CACHE / name),
            "raw_cache_sha256": sha(original),
            "raw_cache_bytes": len(original),
            "omitted_from_deliverable": "Full raw search/open/find text bodies; preserved verbatim in outside source cache.",
        },
    })
    normalized = dump_bytes(record)
    prepared.append((name, original, normalized, record))

CACHE.mkdir(parents=True, exist_ok=True)
manifest = []
for name, original, normalized, record in prepared:
    cache_path = CACHE / name
    if cache_path.exists():
        if cache_path.read_bytes() != original:
            raise RuntimeError("Raw-cache collision: " + str(cache_path))
    else:
        cache_path.write_bytes(original)
    if sha(cache_path.read_bytes()) != sha(original):
        raise RuntimeError("Cache verification failed: " + name)
    path = BASE / "code" / name
    path.write_bytes(normalized)
    if path.read_bytes() != normalized:
        raise RuntimeError("Replacement verification failed: " + name)
    manifest.append({
        "deliverable_record": str(path.relative_to(BASE)),
        "raw_cache_path": str(cache_path),
        "raw_cache_bytes": len(original),
        "raw_cache_sha256": sha(original),
        "normalized_bytes": len(normalized),
        "normalized_sha256": sha(normalized),
        "original_tool_call_seconds": record.get("tool_call_seconds"),
        "reported_source_count": record["reported_source_count"],
    })
manifest_path = BASE / "code" / "part_a567_lieberman_web_normalization_manifest.json"
manifest_path.write_bytes(dump_bytes({
    "operation": "Normalization only; no searches rerun, no mathematical checks, no changes to source-scope outcomes.",
    "normalized_at_utc": normalized_at,
    "records": manifest,
    "record_count": len(manifest),
    "raw_total_bytes": sum(r["raw_cache_bytes"] for r in manifest),
    "normalized_total_bytes": sum(r["normalized_bytes"] for r in manifest),
}))
print(json.dumps({
    "record_count": len(manifest),
    "raw_total_bytes": sum(r["raw_cache_bytes"] for r in manifest),
    "normalized_total_bytes": sum(r["normalized_bytes"] for r in manifest),
    "manifest": str(manifest_path),
    "source_counts": {r["deliverable_record"]: r["reported_source_count"] for r in manifest},
}, ensure_ascii=False))

