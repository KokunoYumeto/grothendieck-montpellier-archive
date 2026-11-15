"""Map every intermediate PDF to its exact final-reader replacement.

The manifest authorizes omission only from final delivery ZIPs. It never
deletes or alters a workspace or checkpoint file. Old sources, logs, PNGs,
observations and raster-equivalence audits remain in the records package.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

PROJECT = Path(__file__).resolve().parents[1]
STEMS = {"PS_EN_diplomatic", "PS_EN_corrected_apparatus", "PS_EN_reading",
         "PS_EN_master_annotated", "PS_GUIDE"}
MODES = {"0": "PS_EN_diplomatic", "1": "PS_EN_corrected_apparatus", "2": "PS_EN_reading"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    finals = {stem: PROJECT / "readers" / (stem + ".pdf") for stem in STEMS}
    hashes = {stem: digest(path) for stem, path in finals.items()}
    build_records = []
    for record in sorted((PROJECT / "logs").glob("*.json")):
        data = json.loads(record.read_text())
        if isinstance(data, dict):
            build_records.append((record, data))
    rows, evidence = [], []
    for pdf in sorted(PROJECT.rglob("*.pdf")):
        relative = pdf.relative_to(PROJECT).as_posix()
        if relative in {f"readers/{stem}.pdf" for stem in STEMS}:
            continue
        if not relative.startswith("qa/"):
            raise ValueError("Unclassified intermediate PDF: " + relative)
        tex = pdf.with_suffix(".tex")
        source = tex.read_text(errors="replace") if tex.exists() else ""
        mode = re.search(r"\\def\\EditionMode\{([012])\}", source)
        if pdf.stem in STEMS:
            stem = pdf.stem
        elif mode:
            stem = MODES[mode[1]]
        elif pdf.stem.endswith("_diplomatic"):
            stem = "PS_EN_diplomatic"
        else:
            raise ValueError("Cannot establish the edition mode of " + relative)
        old_sha = digest(pdf)
        if relative.startswith("qa/pre_final_visual_repairs/"):
            reason = ("Superseded complete predecessor used to establish raster-provenance evidence. "
                      "The named final PDF is its published replacement. Preserved actually-opened PNGs, original observations, "
                      "and hash-bound raster audits remain; extracted-delivery verification compares the current render with those old PNGs.")
        elif relative.startswith("qa/proofs/"):
            reason = ("Superseded isolated verification proof, including clean actually-viewed checks. "
                      "The complete final reader incorporates its source scope. Local TeX, logs, PNGs and observations remain; only this intermediate PDF is omitted.")
        elif relative.startswith("qa/build/"):
            reason = ("Superseded cote-scoped intermediate build, which may contain obsolete diagnostics or layout defects. "
                      "The complete final reader replaces its source scope. Associated sources, build logs, measurements and PNG evidence remain.")
        elif relative.startswith("qa/historical_guide_"):
            reason = ("Superseded historical guide layout. The complete final guide is the published replacement; "
                      "historical PNG observations and guide source/diagnostic records remain.")
        else:
            reason = ("Superseded diagnostic or isolated excerpt. The complete final reader replaces its source scope; "
                      "available TeX, logs, PNGs and observations remain as historical evidence.")
        reason += " Omission applies only to final delivery archives; workspace and immutable checkpoint bytes remain unchanged."
        replacement = finals[stem].relative_to(PROJECT).as_posix()
        rows.append({"path": relative, "bytes": pdf.stat().st_size, "sha256": old_sha,
                     "replacement": replacement, "replacement_sha256": hashes[stem], "reason": reason})
        related = []
        for record, data in build_records:
            if data.get("source") == tex.relative_to(PROJECT).as_posix() or data.get("pdf_sha256") == old_sha:
                related.append(record.relative_to(PROJECT).as_posix())
                if data.get("log") and (PROJECT / data["log"]).exists():
                    related.append(data["log"])
        evidence.append({"path": relative, "source_keys": re.findall(r"\\pssource\{([^{}]+)\}", source),
                         "adjacent_tex_retained": tex.relative_to(PROJECT).as_posix() if tex.exists() else None,
                         "retained_build_records_and_logs": sorted(set(related)),
                         "replacement": replacement})
    path = PROJECT / "records/FINAL_OMISSIONS.tsv"
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "bytes", "sha256", "replacement", "replacement_sha256", "reason"],
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    audit = {"policy": "Only the five published readers/*.pdf files occur in final delivery ZIPs. Exact-byte intermediate-PDF omissions are explicit supersessions, not file deletion.",
             "omission_manifest": path.relative_to(PROJECT).as_posix(), "omission_manifest_sha256": digest(path),
             "intermediate_pdfs_superseded": len(rows), "intermediate_pdf_bytes": sum(row["bytes"] for row in rows),
             "published_pdf_hashes": {finals[stem].relative_to(PROJECT).as_posix(): hashes[stem] for stem in sorted(STEMS)},
             "all_non_pdf_files_retained": True, "all_workspace_and_checkpoint_files_unchanged": True,
             "evidence": evidence}
    (PROJECT / "records/FINAL_OMISSIONS_AUDIT.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps({key: audit[key] for key in ["intermediate_pdfs_superseded", "intermediate_pdf_bytes", "omission_manifest_sha256"]}))


if __name__ == "__main__":
    main()
