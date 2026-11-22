#!/usr/bin/env python3
"""Collect saved program provenance without executing any research program.

Source docstrings describe intended scope, not proof of execution. Declared
output paths, reviewed filename aliases, and schema-matched saved stdout are
distinguished. Nested timings remain recorded fields; request/pass durations
are never relabelled as a whole-run elapsed time. Shared mutable artifacts do
not establish an original run count. The collector writes only its own table
and inventory, and may be imported by update_report.py.
"""
from pathlib import Path
import ast
import collections
import csv
import datetime
import hashlib
import json
import re
import time


# These aliases were checked against the actual write/call sites. A glob
# denotes preserved records from multiple runs, not a single aggregate run.
ALIASES = {
    "history/ROOT_requested_source_pages_initial.py": ["notes/ROOT_requested_source_pages_failure.md"],
    "A567_Crelle_public_catalogues.py": ["logs/A567_Crelle_public_catalogues.json", "logs/A567_Crelle_records.json"],
    "A567_IdRef_public_followup.py": ["logs/A567_IdRef_initial_fetch.json"],
    "A567_IdRef_publications.py": ["logs/A567_IdRef_publications_query.json"],
    "A567_classics_public_followup.py": ["logs/A567_classics_public_fetch.json"],
    "A567_pdf_range_extract.py": ["logs/A567_cote43_range_extract.json"],
    "A567_pdf_range_extract_83_85.py": ["logs/A567_cote43_83_85_range_extract.json"],
    "A567_pdf_range_extract_91_to97.py": ["logs/A567_cote43_91_to97_range_extract.json"],
    "B_IHES_Gabber_catalogue.py": ["logs/B_IHES_Gabber_tag.json"],
    "B_fetch_sources.py": ["logs/B_source_downloads.json"],
    "B_fetch_Suzuki_source.py": ["logs/B_Suzuki_source_fetch.json"],
    "B_fetch_rotthaus.py": ["logs/B_Rotthaus_fetch_receipt.json"],
    "B_validate_pdfs.py": ["logs/B_pdf_validation_receipts.json", "logs/B_pdf_validation_summary.json"],
    "B_build_ledger.py": ["logs/B_ledger_inventory.json"],
    "C_retrieve_earle_marden.py": ["logs/C_EarleMarden_retrieval_metadata.json"],
    "C_program_provenance.py": ["logs/C_program_provenance_runs/*.json"],
    "ROOT_fetch_Bhatt_algebraization.py": ["logs/ROOT_Bhatt_algebraization_fetch.json"],
    "ROOT_fetch_EGAI_newedition.py": ["logs/ROOT_EGAI_newedition_fetch.json"],
    "ROOT_fetch_EGA_SGA_public_corpus.py": ["logs/ROOT_EGA_SGA_public_corpus_fetch.json"],
    "ROOT_fetch_MondalReinecke.py": ["logs/ROOT_MondalReinecke_pdf_fetch.json", "logs/ROOT_MondalReinecke_source_fetch.json"],
    "ROOT_fetch_Nagata_sources.py": ["logs/ROOT_Nagata_sources_fetch.json"],
    "ROOT_fetch_constructible_sources.py": ["logs/ROOT_constructible_sources_fetch.json"],
    "ROOT_fetch_ring_sources.py": ["logs/ROOT_ring_sources_fetch.json"],
    "ROOT_render_constructible_sources.py": ["logs/ROOT_constructible_source_render.json"],
    "build_paper.py": ["logs/integrated_build_summary.json", "logs/build_runs/*/summary.json"],
    "consolidate_registers.py": ["logs/register_consolidation.json"],
    "merge_bibliography.py": ["logs/bibliography_merge.json"],
    "create_checkpoint.py": ["notes/checkpoint_*_inventory.json", "logs/checkpoint_*_save_receipt.json"],
    "record_review01.py": ["logs/progress_review_01.json"],
    "record_review02.py": ["logs/progress_review_02.json"],
    "record_review03.py": ["logs/progress_review_03.json"],
    "record_scheduled_review.py": ["logs/progress_review_0[4-9].json"],
    "record_visual_approval.py": ["logs/paper_visual_qa.json", "logs/visual_qa_runs/*.json"],
    "render_paper_qa.py": ["logs/paper_visual_qa_pending.json", "logs/paper_visual_qa.json", "logs/visual_qa_runs/*.json"],
    "render_supplementary_qa.py": ["logs/supplementary_qa_*.json"],
    "repair_rootless_font_map.py": ["logs/rootless_font_map_repair.json"],
    "update_report.py": ["logs/report_inventory.json"],
}

# Keys are paths relative to code/, not basenames. Preserved historical
# versions were executed at their original paths; moving them into history/
# does not make a later same-output-name receipt evidence for that old run.
HISTORICAL_RUNS = {
    "history/ROOT_requested_source_pages_initial.py": {
        "failure_note": "notes/ROOT_requested_source_pages_failure.md",
        "original_program_path": "code/ROOT_requested_source_pages.py",
        "scope": "Initial source-page execution rendered eleven images, then the four-worker OCR batch failed with subprocess.TimeoutExpired. The aggregate JSON write was never reached. The failure note preserves the exception; the overall runtime and original start timestamp were not retained.",
        "partial_scope_note": "The preserved failure note reports eleven rendered page images and identifies the failing Knudsen–Mumford PDF page 3 OCR command. No completed OCR-batch count is claimed.",
        "unreached_output_path": "logs/ROOT_requested_source_pages.json",
        "timing_caution": "The 55-second value is a subprocess timeout limit, not a measured total elapsed time. The later render-only receipt and its duration belong to a separate execution and are deliberately not associated with this historical program.",
    },
}

# These current files are shared/modified after their initial generator runs.
# Their existence and present row count cannot certify that earlier run.
SHARED_ARTIFACTS = {
    "A_metadata.py": ["A_results.csv", "A_CHECK_EVENTS.tsv"],
    "C_metadata.py": ["C_results.csv", "C_CHECK_EVENTS.tsv", "C_references.bib"],
    "C_reconcile_metadata.py": ["C_results.csv", "C_CHECK_EVENTS.tsv"],
    "C_constructible_metadata_update.py": ["C_results.csv", "C_CHECK_EVENTS.tsv", "C_references.bib"],
    "organize_root_sections.py": ["sections/part_A1234.tex"],
    "render_supplementary_qa.py": ["logs/paper_visual_qa_pending.json"],
}

COUNTS = re.compile(r"count|checks?|assert|enumerat|tested|cases|pairs|convolutions|queries|requests|downloads|attempts|_order$|orders$|involutions|klein_groups|^chain$|^reflection$|^cone$|^alignment$|kernel_covariance|^files$|^entries$|^rows$|pdf_pages|outcome_rows|file_count", re.I)
TIMING = re.compile(r"(?:^|_)(?:seconds?|secs?|milliseconds?|ms|time_s|time_ms)$|^(?:elapsed|runtime|duration|time)$|(?:^|_)(?:elapsed|runtime|duration)_(?:s|ms)$", re.I)
STAMP = re.compile(r"(?:utc|timestamp|started_at|finished_at|recorded_at|checked_at|^date$)", re.I)
SCOPE = re.compile(r"^(?:scope(?:_limit)?|purpose|description|proof_boundary|run_note|certificate|kind|status|outcome|method|mode|warning|note)$", re.I)
COLLECTION = re.compile(r"^(?:results|records|requests|queries|receipts|checks|cases|outputs|files|rows|entries|passes|rendered_pages|points|involutions|normalizer_orders|involution_matrices|nonsplit_slope_orbits|unit_image|P1_points)$", re.I)


def _safe_value(node, bindings):
    """A tiny path-expression reader; never eval/exec source code."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (str, int)):
        return node.value
    if isinstance(node, ast.Name):
        return bindings.get(node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        left, right = _safe_value(node.left, bindings), _safe_value(node.right, bindings)
        if isinstance(left, (str, Path)) and isinstance(right, str):
            return Path(left) / right
    if isinstance(node, ast.Attribute):
        value = _safe_value(node.value, bindings)
        if isinstance(value, Path) and node.attr == "parent":
            return value.parent
        if isinstance(value, Path) and node.attr in ("name", "stem", "suffix"):
            return getattr(value, node.attr)
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Attribute) and node.value.attr == "parents":
        value, index = _safe_value(node.value.value, bindings), _safe_value(node.slice, bindings)
        if isinstance(value, Path) and isinstance(index, int):
            try:
                return value.parents[index]
            except IndexError:
                return None
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "Path" and len(node.args) == 1:
            value = _safe_value(node.args[0], bindings)
            return Path(value) if isinstance(value, (str, Path)) else None
        if isinstance(node.func, ast.Attribute):
            value = _safe_value(node.func.value, bindings)
            if isinstance(value, Path) and node.func.attr in ("resolve", "absolute"):
                return value
            if isinstance(value, Path) and node.func.attr == "with_suffix" and node.args:
                suffix = _safe_value(node.args[0], bindings)
                return value.with_suffix(suffix) if isinstance(suffix, str) else None
    return None


def declared_outputs(tree, source_path, root):
    bindings = {"__file__": source_path, "root": root, "ROOT": root, "BASE": root}
    assignments = [n for n in ast.walk(tree) if isinstance(n, ast.Assign)]
    conflicted = set()
    for _ in range(5):
        for node in assignments:
            value = _safe_value(node.value, bindings)
            if value is None:
                continue
            for target in node.targets:
                if not isinstance(target, ast.Name) or target.id in conflicted:
                    continue
                old = bindings.get(target.id)
                if old is not None and old != value:
                    bindings.pop(target.id, None)
                    conflicted.add(target.id)
                else:
                    bindings[target.id] = value
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        value = None
        if isinstance(node.func, ast.Attribute) and node.func.attr in ("write_text", "write_bytes"):
            value = _safe_value(node.func.value, bindings)
        elif isinstance(node.func, ast.Attribute) and node.func.attr == "open":
            mode = _safe_value(node.args[0], bindings) if node.args else None
            mode = next((_safe_value(k.value, bindings) for k in node.keywords if k.arg == "mode"), mode)
            if isinstance(mode, str) and any(c in mode for c in "wax"):
                value = _safe_value(node.func.value, bindings)
        elif isinstance(node.func, ast.Name) and node.func.id == "open" and len(node.args) >= 2:
            mode = _safe_value(node.args[1], bindings)
            if isinstance(mode, str) and any(c in mode for c in "wax"):
                value = _safe_value(node.args[0], bindings)
        if not isinstance(value, (str, Path)) or str(value).startswith(("http:", "https:")):
            continue
        path = Path(value)
        if not path.is_absolute():
            path = (root.parent / path) if path.parts and path.parts[0] == root.name else (root / path)
        try:
            relative = str(path.relative_to(root))
        except ValueError:
            continue
        if path.suffix.lower() not in (".json", ".jsonl", ".csv", ".tsv", ".txt", ".md", ".tex", ".bib"):
            continue
        if relative.startswith(("literature/", "build/")):
            continue
        found.append((relative, node.lineno))
    return found


def nested_facts(value):
    out = {"durations": [], "timestamps": [], "counts": [], "scopes": [], "collection_sizes": [], "boolean_results": []}
    def visit(obj, path="$", parent_key="", check_context=False):
        if isinstance(obj, dict):
            if check_context and obj and all(isinstance(v, bool) for v in obj.values()):
                out["boolean_results"].append({"path": path, "stored_flags": len(obj), "true": sum(obj.values()), "false": len(obj) - sum(obj.values())})
            for key, child in obj.items():
                child_path = path + "." + str(key)
                context = check_context or bool(re.search(r"checks?|assert", str(key), re.I))
                if isinstance(child, (list, dict)) and COLLECTION.search(str(key)):
                    out["collection_sizes"].append({"path": child_path, "stored_members": len(child)})
                visit(child, child_path, str(key), context)
        elif isinstance(obj, list):
            if path == "$":
                out["collection_sizes"].append({"path": "$", "stored_records": len(obj)})
            for index, child in enumerate(obj):
                visit(child, f"{path}[{index}]", parent_key, check_context)
        elif isinstance(obj, (str, int, float, bool)) or obj is None:
            if STAMP.search(parent_key) and isinstance(obj, str):
                out["timestamps"].append({"path": path, "value": obj})
            elif TIMING.search(parent_key) and not isinstance(obj, bool):
                if isinstance(obj, (int, float)) or (isinstance(obj, str) and re.fullmatch(r"[+\-]?\d+(?:\.\d+)?(?:[eE][+\-]?\d+)?", obj)):
                    out["durations"].append({"path": path, "value": obj})
            if isinstance(obj, (int, float)) and not isinstance(obj, bool) and (COUNTS.search(parent_key) or check_context):
                if not TIMING.search(parent_key):
                    out["counts"].append({"path": path, "value": obj})
            if SCOPE.search(parent_key) and isinstance(obj, str):
                out["scopes"].append({"path": path, "value": obj})
    visit(value)
    return out


def read_output(path, root, evidence, role):
    raw = path.read_bytes()
    result = {"path": str(path.relative_to(root)), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "association": evidence, "role": role}
    if path.suffix in (".csv", ".tsv"):
        rows = list(csv.reader(raw.decode("utf-8").splitlines(), delimiter="\t" if path.suffix == ".tsv" else ","))
        result.update(format="delimited_current_artifact", current_data_rows=max(0, len(rows)-1), fields=rows[0] if rows else [], caution="Current artifact count; not an original execution count")
        return result
    if path.suffix in (".json", ".jsonl"):
        try:
            data = json.loads(raw)
            result["format"] = "json"
        except (json.JSONDecodeError, UnicodeDecodeError):
            try:
                data = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
                result["format"] = "json_lines"
            except (json.JSONDecodeError, UnicodeDecodeError):
                result.update(format="unparsed_saved_record", parse_warning="Not valid JSON/JSON-lines; no counts or timing inferred")
                return result
        if (path.name == "C_program_provenance_inventory.json" or path.parent.name == "C_program_provenance_runs") and isinstance(data, dict):
            # Do not attribute the inspected programs' historical metrics to
            # this administrative collector, or recursively copy its old table.
            data = {k: v for k, v in data.items() if k != "programs"}
        result["facts"] = nested_facts(data)
    else:
        result.update(format="current_text_artifact", caution="Saved text/artifact; no execution time inferred from its contents or filesystem timestamps")
    return result


def _scope(doc, facts):
    parts = [" ".join(doc.split())] if doc else []
    for item in facts:
        if item["path"].split(".")[-1] in ("scope", "scope_limit", "proof_boundary", "purpose", "mode"):
            value = " ".join(item["value"].split())
            if value not in parts:
                parts.append(value)
    return parts


def legacy_association_snapshot(root):
    """Apply only the former file-matching/scalar-reading rule, without edits."""
    missing, empty, matched = [], [], 0
    for source in sorted((root / "code").glob("*.py")):
        stem = source.stem
        paths = [p for p in (root / "logs").glob("*.json") if p.stem in (stem, stem.removesuffix("_checks")) or (stem == "B_fetch_sources" and p.name == "B_source_downloads.json")]
        special = {"build_paper": "integrated_build_summary.json", "consolidate_registers": "register_consolidation.json", "merge_bibliography": "bibliography_merge.json"}
        if stem in special:
            paths = [root / "logs" / special[stem]]
        if not paths:
            missing.append(str(source.relative_to(root)))
            continue
        matched += 1
        facts = []
        for path in paths:
            try:
                data = json.loads(path.read_text())
                if isinstance(data, dict):
                    facts.extend((key, value) for key, value in data.items() if ("time" in key or "second" in key or "check" in key or "count" in key or key in ("scope", "outcome")) and not isinstance(value, (list, dict)))
            except (OSError, ValueError, UnicodeDecodeError):
                pass
        if not facts:
            empty.append(str(source.relative_to(root)))
    return {
        "scope": "Former top-level-only algorithm applied read-only to the same current file snapshot; nested historical scripts were outside that old algorithm's scope. No inspected program is rerun.",
        "programs_with_old_filename_matches": matched,
        "programs_without_old_filename_matches": missing,
        "matched_programs_without_old_top_level_scalar_facts": empty,
        "nested_programs_omitted_by_old_algorithm": [str(p.relative_to(root)) for p in sorted((root / "code").rglob("*.py")) if p.parent != root / "code"],
    }


def collect(root):
    started = time.perf_counter()
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    programs = []
    for source_path in sorted((root / "code").rglob("*.py")):
        program_key = str(source_path.relative_to(root / "code"))
        historical = HISTORICAL_RUNS.get(program_key)
        text = source_path.read_text()
        row = {"program": str(source_path.relative_to(root)), "source_sha256": hashlib.sha256(text.encode()).hexdigest(), "outputs": [], "missing_declared_outputs": []}
        try:
            tree = ast.parse(text)
            row["source_docstring"] = ast.get_docstring(tree) or ""
        except SyntaxError as exc:
            row.update(source_docstring="", parse_warning=str(exc), evidence_status="Source present; syntax could not be inspected, and no execution is inferred")
            programs.append(row)
            continue
        candidates = {}
        for pattern in ALIASES.get(program_key, []):
            paths = sorted(root.glob(pattern))
            if program_key == "C_program_provenance.py":
                paths = paths[-1:]
            for path in paths:
                if program_key == "record_visual_approval.py" and path.name.endswith("_not_approved.json"):
                    continue
                if historical and str(path.relative_to(root)) == historical["failure_note"]:
                    candidates[str(path.relative_to(root))] = ("Preserved actual failure/exception note identifies this archived source version; not a successful aggregate output or a later run's receipt", "preserved_failure_note")
                elif program_key == "A567_Crelle_public_catalogues.py" and path.name == "A567_Crelle_records.json":
                    candidates[str(path.relative_to(root))] = ("Source owner identified three imported fetch(job) calls for returned GDZ record links; this is a helper-call discovery receipt, not a separate standalone script execution", "imported_helper_receipt")
                else:
                    candidates[str(path.relative_to(root))] = ("Reviewed output-path alias in source or preserved multi-run records", "saved_record")
        # The historical failure never reached its aggregate write. Inferring
        # output paths using its new archive location would also change root.
        declared = [] if historical else declared_outputs(tree, source_path, root)
        for name, line in declared:
            if program_key == "C_program_provenance.py":
                # Its preceding immutable run is linked above; the current
                # self-record cannot contain its own future final-file hash.
                continue
            if (root / name).exists():
                role = "saved_record" if name.startswith("logs/") and Path(name).suffix in (".json", ".jsonl", ".txt") else "mutable_artifact"
                candidates.setdefault(name, (f"Declared write target, source line {line}", role))
            else:
                row["missing_declared_outputs"].append({"path": name, "line": line})
        for name in SHARED_ARTIFACTS.get(program_key, []):
            if (root / name).exists():
                candidates[name] = ("Reviewed shared output; subsequently modified, so no original-run attribution follows from its existence", "mutable_artifact")
        same_stem = root / "logs" / (source_path.stem + ".json")
        if not historical and same_stem.exists() and str(same_stem.relative_to(root)) not in candidates:
            try:
                saved = json.loads(same_stem.read_text())
                keys = set(saved) if isinstance(saved, dict) else {k for x in saved if isinstance(x, dict) for k in x} if isinstance(saved, list) else set()
                strings = {n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)}
                emits = any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "print" for n in ast.walk(tree))
                if emits and len(keys & strings) >= 2:
                    candidates[str(same_stem.relative_to(root))] = ("Same-stem saved stdout record and matching emitted JSON fields; no saved launch command/source-version binding asserted", "saved_stdout")
                else:
                    row["unresolved_same_stem_record"] = str(same_stem.relative_to(root))
            except (ValueError, UnicodeDecodeError):
                row["unresolved_same_stem_record"] = str(same_stem.relative_to(root))
        if program_key == "fetch_sources.py":
            for path in sorted((root / "logs").glob("fetch_*.json")):
                try:
                    data = json.loads(path.read_text())
                except (ValueError, UnicodeDecodeError):
                    continue
                if isinstance(data, dict) and {"url", "target", "started_utc", "seconds", "outcome"}.issubset(data):
                    candidates[str(path.relative_to(root))] = ("Generic fetch receipt matches this helper's emitted schema; exact launch/source-version association was not retained", "schema_associated_record")
        for name, (evidence, role) in sorted(candidates.items()):
            try:
                row["outputs"].append(read_output(root / name, root, evidence, role))
            except (OSError, ValueError, UnicodeDecodeError) as exc:
                row.setdefault("read_warnings", []).append({"path": name, "error": repr(exc)})
        records = [o for o in row["outputs"] if o["role"] != "mutable_artifact"]
        if records:
            row["evidence_status"] = "Saved records linked by the stated source-path/schema evidence; source presence alone is not execution proof"
        elif row["outputs"]:
            row["evidence_status"] = "Current declared artifacts exist; a unique original execution receipt/time is not established"
        else:
            row["evidence_status"] = "Source present only; no saved execution/output association established"
        scope_facts = [f for o in records for f in o.get("facts", {}).get("scopes", [])]
        row["scope"] = _scope(row["source_docstring"], scope_facts)
        row["recorded_duration_fields"] = sum(len(o.get("facts", {}).get("durations", [])) for o in records)
        if historical:
            row["historical_execution"] = historical
            if any(o["role"] == "preserved_failure_note" for o in records):
                row["evidence_status"] = "Failed historical execution documented by the preserved exception note; no successful aggregate OCR receipt or overall runtime retained"
                row["scope"].append(historical["scope"])
                row["documented_partial_scope"] = historical["partial_scope_note"]
            else:
                row["evidence_status"] = "Historical source present, but the expected preserved failure note is missing; execution evidence must be restored before attributing this run"
            row["own_elapsed_time_recorded"] = False
            row["own_elapsed_time_note"] = "This failed historical execution's total elapsed time and original start timestamp were not retained."
            row["timing_caution"] = historical["timing_caution"]
            row["recorded_duration_fields"] = 0
        if program_key == "record_visual_approval.py":
            row["timing_caution"] = "The seconds field belongs to rendering, inherited into the approval record; no duration of the act of visual inspection/approval was recorded"
            row["own_elapsed_time_recorded"] = False
            row["own_elapsed_time_note"] = "The approval script's own elapsed time was not recorded; inherited rendering/build duration fields are retained only in the inventory."
            row["inherited_duration_fields"] = row["recorded_duration_fields"]
            row["recorded_duration_fields"] = 0
        if program_key == "render_paper_qa.py":
            row["timing_caution"] = "Archived approval records retain rendering duration; current and archived copies may duplicate the same run, and are not summed"
        if program_key == "build_paper.py":
            row["timing_caution"] = "Per-pass durations remain per-pass; current and archived copies may duplicate a build and are not summed"
        if program_key == "C_program_provenance.py":
            row["timing_caution"] = "The linked inventory is the preceding saved collector run; its collector_elapsed_seconds is administrative collection time, not any inspected mathematical program's runtime"
        if program_key == "create_checkpoint.py":
            row["timing_caution"] = "Only checkpoint durations actually present in the saved receipts are shown; missing runs' elapsed times are not inferred from their creation/save timestamps"
        programs.append(row)
    inventory = {
        "created_utc": stamp,
        "scope": "Read-only collection of actual saved provenance; no research program, mathematical certificate, source fetch, or visual approval executed",
        "program_count": len(programs),
        "programs_with_linked_saved_records": sum(any(o["role"] != "mutable_artifact" for o in r["outputs"]) for r in programs),
        "programs_with_only_mutable_artifacts": [r["program"] for r in programs if r["outputs"] and all(o["role"] == "mutable_artifact" for o in r["outputs"])],
        "programs_with_no_linked_output": [r["program"] for r in programs if not r["outputs"]],
        "programs_without_recorded_elapsed_time": [r["program"] for r in programs if not r.get("recorded_duration_fields")],
        "unresolved_associations": [{"program": r["program"], "path": r["unresolved_same_stem_record"]} for r in programs if "unresolved_same_stem_record" in r],
        "schema_only_associations": [{"program": r["program"], "path": o["path"]} for r in programs for o in r["outputs"] if o["role"] == "schema_associated_record"],
        "legacy_comparison": legacy_association_snapshot(root),
        "programs": programs,
        "collector_elapsed_seconds": time.perf_counter() - started,
    }
    return inventory


def _cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ")


def _short(value, limit):
    value = " ".join(str(value).split())
    return value if len(value) <= limit else value[:limit - 1] + "…"


def _grouped(items, limit=8):
    groups = collections.OrderedDict()
    for item in items:
        key = re.sub(r"\[\d+\]", "[*]", item["path"])
        value = item.get("value", item.get("stored_records", item.get("stored_members")))
        groups.setdefault(key, []).append(value)
    result = []
    for key, values in list(groups.items())[:limit]:
        unique = list(dict.fromkeys(str(v) for v in values))
        value = ", ".join(unique[:5]) + (f"; first five distinct values shown from {len(values)} saved values" if len(unique) > 5 else f"; {len(values)} saved values" if len(values) > 5 else "")
        result.append(f"`{key}`={value}")
    if len(groups) > limit:
        result.append(f"{len(groups)-limit} further recorded fields in the linked inventory")
    return result


def render_table(inventory):
    lines = [
        "The table below distinguishes source-declared scope, saved execution/output evidence, and current shared artifacts. A source file alone is not treated as an executed run. Counts labelled ‘stored’ describe the saved data, not additional assertions executed by this audit. Request/pass durations and timestamps are not substituted for a whole-program elapsed time. Missing elapsed time is stated explicitly.",
        "",
        "The complete paths, association reasons, source/output hashes, nested scope/count/timing fields, and unresolved associations are in `logs/C_program_provenance_inventory.json`; the standalone table is `notes/C_program_provenance_table.md`. No mathematical program was rerun to prepare this inventory.",
        "",
        "| Program | Scope and execution evidence | Saved output records | Recorded counts and timings |",
        "|---|---|---|---|",
    ]
    for row in inventory["programs"]:
        scope = _short(" ".join(row.get("scope", [])), 420) or "No module docstring; use the linked source and records for scope."
        outputs = row["outputs"]
        links = ["`" + o["path"] + "`" for o in outputs[:4]]
        if len(outputs) > 4:
            links.append(f"{len(outputs)-4} further paths in the inventory")
        if not links:
            links = ["No output association established; source-only entry"]
        records = [o for o in outputs if o["role"] != "mutable_artifact"]
        counts = [x for o in records for x in o.get("facts", {}).get("counts", [])]
        sizes = [x for o in records for x in o.get("facts", {}).get("collection_sizes", [])]
        durations = [x for o in records for x in o.get("facts", {}).get("durations", [])]
        booleans = [x for o in records for x in o.get("facts", {}).get("boolean_results", [])]
        summary = ["Recorded counts: " + "; ".join(_grouped(counts, 8)) + "."] if counts else []
        if sizes:
            summary.append("Stored collection sizes: " + "; ".join(_grouped(sizes, 4)) + ".")
        if not summary:
            summary = ["No numerical run/check count recorded in linked receipts."]
        if booleans:
            flags = [f"`{b['path']}`: {b['stored_flags']} stored flags ({b['true']} true, {b['false']} false)" for b in booleans[:3]]
            summary.append("Saved result flags, not a newly executed assertion count: " + "; ".join(flags) + ".")
        if row.get("own_elapsed_time_recorded") is False:
            summary.append(row.get("own_elapsed_time_note", "This program's own elapsed time was not recorded."))
        elif durations:
            summary.append("Recorded duration fields: " + "; ".join(_grouped(durations, 4)) + ". Values keep the units and scope named in their source fields; no cross-record sum is called elapsed time.")
        else:
            summary.append("Elapsed time not recorded/established in the linked saved outputs.")
        for output in outputs:
            if "current_data_rows" in output:
                summary.append(f"Current `{output['path']}`: {output['current_data_rows']} data rows; not an original-run count.")
        if row.get("documented_partial_scope"):
            summary.append(row["documented_partial_scope"])
        if row.get("timing_caution"):
            summary.append(row["timing_caution"])
        lines.append("| " + " | ".join(map(_cell, ["`" + row["program"] + "`", scope + " " + row["evidence_status"], "; ".join(links), " ".join(summary)])) + " |")
    return lines


def computation_table(root):
    """Refresh only this helper's provenance artifacts and return table lines."""
    root = Path(root)
    current = root / "logs/C_program_provenance_inventory.json"
    if current.exists():
        previous = json.loads(current.read_text())
        previous_stamp = re.sub(r"[^0-9]", "", previous["created_utc"].split("+")[0])
        archive = root / "logs/C_program_provenance_runs" / (previous_stamp + ".json")
        archive.parent.mkdir(exist_ok=True)
        if not archive.exists():
            archive.write_bytes(current.read_bytes())
    inventory = collect(root)
    lines = render_table(inventory)
    (root / "logs/C_program_provenance_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")
    (root / "notes/C_program_provenance_table.md").write_text("# Program provenance inventory\n\nSnapshot: " + inventory["created_utc"] + "\n\n" + "\n".join(lines) + "\n")
    return lines


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    computation_table(root)
    saved = json.loads((root / "logs/C_program_provenance_inventory.json").read_text())
    print(json.dumps({k: v for k, v in saved.items() if k != "programs"}, indent=2))
