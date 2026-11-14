#!/usr/bin/env python3
"""Place reviewed French-source apparatus IDs at their English clauses.

These markers record French corrections whose English wording is unchanged.
They are not English textual variants. Anchors are manually aligned to the
checked clauses; the script requires a unique literal match before writing.
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
ANCHORS = {
    "V-FR-004-001": "inadequate",
    "V-FR-006-001": "on surfaces.",
    "V-FR-006-002": r"\uline{of automorphisms of a most concrete profinite group}",
    "V-FR-007-001": "even indispensable",
    "V-FR-009-001": "covering)",
    "V-FR-014-001": r"ramified only at 0, 1, $\infty$",
    "V-FR-017-001": "did indeed find the supposition crazy",
    "V-FR-012-001": "It admits",
    "V-FR-013-001": "rigidified by the three points 0, 1",
    "V-FR-024-001": "new charms",
    "V-FR-024-002": "by specializing the icosahedron",
    "V-FR-016-001": "a more conceptual direction",
    "V-FR-025-001": "these are characteristics 2 and 5",
    "V-FR-027-001": "singular algebraic variety",
    "V-FR-027-002": "spherical",
    "V-FR-034-001": "or simply",
    "V-FR-035-001": "apart from comparison\ntheorems",
    "V-FR-028-001": "rigidification",
    "V-FR-028-002": "the points of these multiplicities",
    "V-FR-028-003": "being identified",
    "V-FR-015-001": "what exactly are the conjugates",
    "V-FR-019-001": "is known up to isomorphism",
    "V-FR-032-001": "Hironaka's semianalytic spaces",
    "V-FR-033-001": r"restrictive of all, that of ``piecewise $\bar{\mathbb{Q}}_r$-algebraic spaces''",
    "V-FR-033-002": r"the ``$\infty$-isotopy'' categories",
    "V-FR-035-002": "any tame map",
    "V-FR-036-001": "in just as canonical a way",
    "V-FR-036-002": "any theory of tubular neighborhoods",
    "V-FR-038-001": "I had reached",
    "V-FR-038-002": "has not progressed",
    "V-FR-039-001": "of tame spaces,",
    "V-FR-043-001": "in various spaces",
    "V-FR-044-001": r"every $\unsure{\sourceglyph{119A}}$-manifold",
    "V-FR-026-001": "even succeeds in bringing it out",
    "V-FR-046-001": "products of Eilenberg-Maclane spaces",
    "V-FR-042-001": "first task was to draw out",
    "V-FR-045-001": "the manuscript",
    "V-FR-045-002": "out of desperation",
    "V-FR-048-001": "has moreover recurred",
    "V-FR-010-002": "is equipped with a canonical cellular decomposition",
    "V-FR-050-001": "who have worked with me during",
    "V-FR-052-001": "more than a single piece of work",
    "V-FR-029-001": "and homeomorphisms of such pairs",
    "V-FR-040-001": "scheme-theoretic\ncompactifications",
    "V-FR-054-001": "escaped me until now",
    "V-FR-055-001": r"even $\mathbb{Z}$",
    "V-FR-059-001": r"space $X_*$",
    "V-FR-059-002": "which is endowed",
    "V-FR-059-003": "is a ``bordering'' embedding.",
}


def main():
    variants = json.loads((ROOT / "editorial_variants.json").read_text())
    pending = {}
    rows = []
    missing = []
    for variant in variants:
        ident = variant["id"]
        path = ROOT / "translated_pages" / (variant["key"] + ".tex")
        if variant.get("english_variant_needed") or not path.exists():
            continue
        if ident not in ANCHORS:
            missing.append(ident)
            continue
        english = pending.get(path, path.read_text())
        anchor = ANCHORS[ident]
        marker = r"\frapparatus{" + ident + "}"
        if marker not in english:
            count = english.count(anchor)
            if count != 1:
                raise ValueError(f"Expected one English anchor for {ident}; found {count}")
            english = english.replace(anchor, anchor + marker, 1)
        if english.count(marker) != 1:
            raise ValueError(f"Duplicate source-apparatus marker: {ident}")
        pending[path] = english
        rows.append([
            ident, variant["key"],
            variant["old"].replace("\n", r"\n"),
            variant["new"].replace("\n", r"\n"),
            anchor.replace("\n", r"\n"),
            "French correction explained; English wording unchanged",
        ])
    if missing:
        raise ValueError("Unaligned French correction IDs: " + ", ".join(missing))
    for path, english in pending.items():
        path.write_text(english)
    with (ROOT / "translated_pages" / "FRENCH_APPARATUS_ALIGNMENT.tsv").open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["variant_id", "key", "french_page_reading", "french_corrected_reading", "english_anchor", "status"])
        writer.writerows(rows)
    print(json.dumps({"french_source_apparatus_markers": len(rows), "translated_pages_touched": len(pending)}))


if __name__ == "__main__":
    main()
