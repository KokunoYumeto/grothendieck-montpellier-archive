#!/usr/bin/env python3
"""Reproduce the inventory for the completed readable-transcription audit.

This script hashes and counts the supplied files. It does not infer mathematical
absence from a search: the reading attestations and topic classifications below
record the completed human-readable analysis in audit_SA19H6.md.
"""
from pathlib import Path
import csv
import hashlib
import json
import time

started = time.perf_counter()
TASK = Path(__file__).resolve().parents[1]
ROOT = TASK.parents[1]
paths = [ROOT / p for p in (TASK / "outputs/c43_files.txt").read_text().splitlines()]
paths.sort(key=lambda p: int(p.stem[-3:]))

topics = [
    (1, 16, "Class field theory, ideles, reciprocity, local symbols"),
    (17, 23, "Adelic divisor complexes, Jacobians, Albanese pairings"),
    (24, 35, "Open Abel map; qualified Ext/cohomology comparison"),
    (36, 69, "Witt/descent notes; residual complexes and endomorphism algebras"),
    (70, 79, "Local Jacobians, local cohomology, torsor section extension"),
    (80, 82, "Augmented generalized-Jacobian and local-field Ext programme"),
    (83, 98, "Sites, categories, local duality, Neron functors"),
    (99, 121, "Tate/Serre duality, Greenberg functors, interspersed printed drafts"),
    (122, 142, "Curve duality and support cohomology; reused sheaf/flatness proofs"),
    (143, 146, "Local/global Galois cohomology duality and localization"),
    (147, 159, "Etale l-adic modules, fundamental groups, Serre Lie algebras"),
    (160, 170, "Hom/Ext tables and injectivity of extension-to-torsor map"),
    (171, 202, "Cartier duality, formal groups, Dieudonne modules, categories"),
    (203, 205, "Tate pairing, dual-abelian sections and Brauer obstruction"),
    (206, 208, "Local symbols and Albanese-kernel pairing"),
]
special = {
    27: "Boxed open Abel map, not an injectivity-on-points assertion",
    30: "Ext1 pullback injective; stronger bijective/surjective direction qualified by Il semble",
    34: "Higher comparison qualified by et sans doute",
    77: "Rational torsor section extends; different meaning of section",
    78: "Fundamental groups of valuation ring and local field",
    101: "Reused printed stable homotopy and intrinsic joins",
    103: "Reused printed Stiefel-manifold cross-sections",
    105: "Bibliography of reused homotopy text",
    113: "Decomposition/inertia subgroup generation",
    133: "Jacobian torsion and cohomological fundamental-group identifications",
    145: "H1 localization injectivity under stated Galois/class-number conditions",
    167: "Ext1-to-torsor-class injection, not rational-point sections",
    168: "Normalized torsor section becomes multiplicative",
    169: "Primitive torsor extension structure and reduced-base invariance",
    198: "Printer imprint and paper watermark",
    204: "Sections of Neron-Severi and dual abelian scheme",
    205: "Tate pairing and Brauer obstruction of line-bundle representatives",
    207: "Albanese map defines zero-cycle kernel and pairing",
}
rows = []
for path in paths:
    leaf = int(path.stem[-3:])
    raw = path.read_bytes()
    content = raw.decode("utf-8")
    topic = next(t for lo, hi, t in topics if lo <= leaf <= hi)
    rows.append({
        "scan": leaf,
        "source_path": str(path.relative_to(ROOT)),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "characters": len(content),
        "unsure_macros": content.count(r"\unsure{"),
        "illegible_macros": content.count(r"\illegible{"),
        "reader": "FHI (complete rereading expressly certified)" if 56 <= leaf <= 66 else "DGJ (complete readable transcription)",
        "date": "2026-11-20",
        "topic": topic,
        "near_match_note": special.get(leaf, ""),
        "finding": "No rational-point-to-fundamental-group-section injectivity argument found in readable supplied text",
    })
assert len(rows) == 195
assert len({r["scan"] for r in rows}) == 195
absent = sorted(set(range(1, 209)) - {r["scan"] for r in rows})
assert absent == [14, 39, 44, 83, 88, 99, 111, 127, 157, 166, 175, 179, 194]
with (TASK / "outputs/c43_audit.tsv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
summary = {
    "inventory_files": len(rows),
    "DGJ_full_read_files": sum(r["reader"].startswith("DGJ") for r in rows),
    "FHI_full_read_files": sum(r["reader"].startswith("FHI") for r in rows),
    "absent_scan_labels_not_inferred": absent,
    "bytes": sum(r["bytes"] for r in rows),
    "characters": sum(r["characters"] for r in rows),
    "uncertainty_macros": sum(r["unsure_macros"] for r in rows),
    "illegibility_macros": sum(r["illegible_macros"] for r in rows),
    "scope": "Readable supplied transcriptions only; no mathematical or historical absence inferred by this script",
    "runtime_seconds": round(time.perf_counter() - started, 6),
}
(TASK / "outputs/c43_audit_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
