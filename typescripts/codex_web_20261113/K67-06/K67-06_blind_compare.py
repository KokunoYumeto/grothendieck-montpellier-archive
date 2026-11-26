"""Compare the blind crop readings with their manuscript loci. Run with Python 3."""

import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_table(name):
    with (ROOT / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def normalize(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace(r"\operatorname", r"\mathrm").replace(r"\textsuperscript", "")
    wrappers = (r"text|mathrm|mathbb|mathcal|mathscr|mathfrak|underline|uline|uuline|"
                r"unsure|deleted|inserted|margin|handwritten|underset|underbrace|"
                r"overset|substack|left|right|begin|end")
    s = re.sub(r'\\(?:' + wrappers + r')(?![A-Za-z])', "", s)
    s = re.sub(r"\\[ ,;!:]|\\(?:quad|qquad|textstyle|displaystyle)\b", "", s)
    return re.sub(r"[\s{}\[\]$^_~,:;.!?'’\x60\\]", "", s).casefold()


def witness_decisions():
    apparatus = (ROOT / "K67-06_doubts.md").read_text()
    _, sep, report = apparatus.partition("## Witness check")
    if not sep:
        return {}
    decisions = {}
    for line in report.splitlines():
        if not re.match(r"^\| [0-9]{3}-[0-9]{2} \|", line):
            continue
        row = line[2:-2].split(" | ")
        assert len(row) == 8
        decisions[row[0]] = (row[5], row[6])
    return decisions


def witness_text(ids, decisions):
    notes = []
    for mark in ids.split():
        key = mark.rstrip("*")
        result, final = decisions[key]
        if mark.endswith("*"):
            notes.append(f"{key} applies to the first occurrence. This later occurrence retains tau.")
        else:
            notes.append(f"{key}, {result} → {final}.")
            if key == "101-04":
                notes.append("The final symbol names the nontrivial torsor under the split family.")
    return " ".join(notes) or "—"


def cell(s):
    return s.replace("|", r"\|").replace("\n", " ")


def write_report():
    blind = read_table("K67-06_blind.tsv")
    alignments = read_table("K67-06_collation.tsv")
    lookup = {(r["scan"], r["place"]): r for r in alignments}
    decisions = witness_decisions()
    lines = [
        "# Comparison of independent crop readings",
        "",
        "Each row gives a difference between the first transcription and the independent crop reading. "
        "The audit decision records what the writer could make out on reinspection. "
        "Where the later witness check changed that decision or added an alternative, its locus and final text appear in the last column. "
        "The matching column reports a page-wide search for the audit's locator text after removing typesetting and punctuation. "
        "The handwritten words, signs and punctuation were adjudicated on the scan.",
        "",
        "| Scan | Place | Blind reading | First pass | Audit decision from the ink | Audit locator present on final page | Later witness decision at this locus |",
        "|---|---|---|---|---|---|---|",
    ]
    agreements = 0
    disagreements = 0
    missing = []
    page_text = {}
    for b in blind:
        k = (b["scan"], b["place"])
        if k not in lookup:
            missing.append(k)
            continue
        m = lookup[k]
        if m["status"] == "agreement":
            agreements += 1
            continue
        disagreements += 1
        if k[0] not in page_text:
            path = ROOT / "pages" / f"K67-06_67_scan{int(k[0]):03}.tex"
            page_text[k[0]] = normalize(path.read_text())
        found = normalize(m["check_in_page"]) in page_text[k[0]]
        row = [*k, b["what_the_crop_shows"], m["first_pass"], m["decision"], "yes" if found else "no"]
        last = witness_text(m.get("witness_loci", ""), decisions)
        lines.append("| " + " | ".join(map(cell, row)) + " | " + last + " |")
    lines += ["", f"{disagreements} disagreements. {agreements} agreements. {len(missing)} loci await alignment."]
    (ROOT / "K67-06_blind_compare.md").write_text("\n".join(lines) + "\n")
    return disagreements, agreements, len(missing)


if __name__ == "__main__":
    print(*write_report())
