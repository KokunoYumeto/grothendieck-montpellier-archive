"""Compare saved blind readings to the aligned manuscript loci. Run with Python 3."""
from pathlib import Path
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parent
PREFIX = "K64-05"
def tsv(suffix):
    with (ROOT / (PREFIX + suffix)).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def source_span(lines, spec):
    indices = []
    for term in spec.split(","):
        first, _, last = term.partition("-")
        indices.extend(range(int(first) - 1, int(last or first)))
    return "\n".join(lines[index] for index in indices)

def excerpt(span, cue):
    text = " ".join(span.split())
    if len(text) <= 145:
        return text
    position = text.casefold().find(cue.replace("’", "'").casefold())
    start = max(0, position - 40)
    end = min(len(text), start + 145)
    return ("…" if start else "") + text[start:end] + ("…" if end < len(text) else "")

def code_span(value):
    marker = chr(96)
    runs = re.findall(marker + "+", value)
    fence = marker * (1 + max((len(run) for run in runs), default=0))
    pad = " " if value.startswith(marker) or value.endswith(marker) else ""
    return fence + pad + value + pad + fence

def main():
    blind = tsv("_blind.tsv")
    alignment = tsv("_blind_alignment.tsv")
    if [(r["scan"], r["place"]) for r in blind] != [(r["scan"], r["place"]) for r in alignment]:
        raise ValueError("The blind register and its line alignment differ.")
    chunks = ["# Blind reading comparison", "",
        "The blind entries were saved from the scans before reopening each page. "
        "The passages below include disagreements and places where a second look was needed to distinguish agreement from difference. "
        "The decision records what was visible at that stage. The current excerpt also reflects any subsequent witness check. "
        "The two TSV files give the complete register and its page-line alignment. "
        "The comparison aligns each English description of strokes with its LaTeX passage.", "",
        "The [page-by-page audit](K64-05_audit.md) prints all 43 first-pass edits as before and after readings. "
        "It also records the individual formula and margin checks.", ""]
    previous = None
    settled = 0
    for b, a in zip(blind, alignment):
        n = int(a["scan"])
        page = ROOT / "pages" / f"{PREFIX}_64_scan{n:03}.tex"
        span = source_span(page.read_text(encoding="utf-8").splitlines(), a["lines"])
        if hashlib.sha256(span.encode()).hexdigest() != a["page_span_sha256"]:
            raise ValueError(f"Page differs from aligned edition at {n}, {a['place']}")
        if not a["crop_decision"]:
            continue
        if n != previous:
            chunks.extend([f"## Scan {n}", ""])
            previous = n
        settled += 1
        chunks.extend([f"### {a['place']} · L{a['lines']}", "",
            "**Blind reading.** " + b["what_the_crop_shows"], "",
            "**First-pass excerpt.** " + code_span(a["first_pass_excerpt"]), "",
            "**Decision on the ink.** " + a["crop_decision"], "",
            "**Current page excerpt.** " + code_span(excerpt(span, a["cue"])), ""])
    chunks.extend(["## Coverage", "", f"{len(blind)} aligned places on 13 scans. "
        f"{settled} decisions are given above. Each current source span matched its recorded SHA-256.", ""])
    (ROOT / (PREFIX + "_blind_compare.md")).write_text("\n".join(chunks), encoding="utf-8")
    return len(blind), settled
if __name__ == "__main__":
    total, settled = main()
    print(f"Compared {total} places, {settled} recorded decisions.")
