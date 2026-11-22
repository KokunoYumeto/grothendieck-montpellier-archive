"""Retain observations only after actual individual viewing of all four CP32 images."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
pdf = root / "RESEARCH_SA15_paper.pdf"
expected = "406ade402449604644a2b030e0cc8a05508a0eb52ec119cddc8108009a6c562a"
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == expected
pages = [387, 388, 389, 390]
observations = {
    "387": "The preceding classification scope continues normally. Section 2.122, the Fermat/remainder definition and Lemma 2.443 are legible. DE-MF1 and DE-MF2 fit within the margins with intact sums, products and tags. The bottom proof continues without clipping or overlap.",
    "388": "The coefficient/support proof continuation and Lemma 2.444 are clean. The affine-line restriction and three-by-three determinant displays DE-MF3/4 have readable subscripts and complete tags. The final exact affine covariance paragraph and proof-end marker are fully visible; no glyph or margin defect.",
    "389": "The full-support/eight-support proof is entirely readable. DE-MF5 through DE-MF8, the three cubed equations, stabilizer definition and four zero-position orbits fit correctly. The a=0 and u=0 arguments, coordinate indices and bottom proof-end marker show no clipping, collision or missing math glyph.",
    "390": "Theorem 2.446, its equivalence DE-MF9 and the complete proof render cleanly. Remark 2.447 preserves certificate scope and the failed-identity correction history with readable path breaks and superscripts. Section 2.123 begins with sufficient introductory text below the heading; page continuation is normal."
}
images = {
    str(p): hashlib.sha256((root / f"outputs/qa32/page_{p:03d}.png").read_bytes()).hexdigest()
    for p in pages
}
now = datetime.now(timezone.utc).isoformat()
record = {
    "status": "PASS",
    "actual_utc": now,
    "pdf_sha256": expected,
    "pdf_pages": 714,
    "pages": pages,
    "method": "Each of the four final PNGs was individually opened using view_image and actually inspected. This record was written only after all four image outputs were observed.",
    "scope": "Visual layout of the complete new Moore/Fermat theorem and its adjoining section boundaries: text, displays, equation tags, proof continuations, glyphs, path wrapping and margins. No PDF or canonical-source edits.",
    "observations": observations,
    "image_sha256": images,
    "defects": []
}
dest = own / "CP32_visual_QA.json"
with dest.open("x") as out:
    json.dump(record, out, indent=2)
    out.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as out:
    out.write("\t".join([
        now, "CP32_actual_visual_QA", "actual_final_PNG_inspection",
        "outputs/qa32/page_387.png through page_390.png",
        "All four final images actually viewed; final PDF SHA256 verified",
        "PASS; no visual layout defect observed", str(dest.relative_to(root))
    ]) + "\n")
print(json.dumps({"status": "PASS", "actual_utc": now, "pages": pages,
                  "pdf_sha256": expected, "record": str(dest.relative_to(root))}))
