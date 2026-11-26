"""Compare each image-only TSV entry with its own location in the returned page.

Run this script beside the audit, TSV and pages directory. It writes the report
in that same directory. It never writes to a transcription or to the blind TSV.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREFIX = "K68-02"
# One page-source line per entry in that sheet's blind TSV, in original order.
PAGE_LINES = {
    "017": [4, 5, 4, 4, 6, 7, 10, 11, 16, 21, 24, 31, 26, 37, 39, 41, 44, 47, 52, 54, 55],
    "018": [2],
    "019": [2, 4, 4, 6, 6, 6, 6, 6, 6, 9, 9, 15, 19, 19, 19, 19, 22, 22, 24, 26, 44, 46, 47],
    "020": [2, 2, 4, 6, 6, 8, 13, 13, 15, 20, 20, 22, 28, 32, 36, 42, 44, 44, 46, 48, 50],
    "021": [2, 2, 4, 8, 8, 8, 12, 20, 29, 32, 38, 38, 40, 42, 48, 47, 52, 56, 57],
    "022": [3, 3, 3, 7, 11, 16, 18, 20, 26, 28, 32, 34, 39, 48, 56, 60, 63, 71, 71, 73],
    "024": [38, 6, 16, 18, 25, 29, 27, 33, 31, 35, 35, 37, 37],
    "025": [34, 3, 10, 12, 14, 16, 16, 20, 22, 28, 31, 31, 31, 33],
    "026": [29, 2, 2, 2, 4, 4, 4, 4, 4, 6, 10, 15, 18, 20, 20, 20, 22, 25],
    "027": [18, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 8, 8, 16, 16],
    "028": [33, 4, 8, 13, 19, 19, 19, 19, 19, 19, 19, 21, 24, 24, 28, 28, 30],
    "029": [11, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10],
    "030": [23, 4, 8, 8, 8, 10, 16, 16, 16, 16, 18, 18, 20, 22],
    "031": [35, 2, 2, 2, 2, 6, 9, 11, 11, 11, 11, 11, 21, 25, 25, 31, 33],
    "032": [18, 2, 2, 4, 6, 6, 6, 8, 8, 8, 8, 8, 10, 13, 14, 17, 17],
}
MARKUP = re.compile(r"\\(unsure|illegible|inserted|deleted|uline|uuline|margin|text|mathrm|textit|handwritten)\{")


def argument(source, start):
    depth = 1
    at = start + 1
    while depth:
        if source[at] == "\\":
            at += 2
            continue
        depth += (source[at] == "{") - (source[at] == "}")
        at += 1
    return source[start + 1:at - 1], at


def primary(body):
    if re.fullmatch(r"\|[^|]+\|", body):
        return body
    return re.split(r"(?<!\\)\|", body, maxsplit=1)[0]


def visible(source):
    """Keep struck and inserted writing. Compare the primary doubtful reading."""
    parts = []
    while match := MARKUP.search(source):
        parts.append(source[:match.start()])
        body, end = argument(source, match.end() - 1)
        if match[1] == "unsure":
            body = primary(body)
        parts.append(visible(body))
        source = source[end:]
    return "".join(parts) + source


def normal(source):
    """Ignore typesetting syntax that does not distinguish the written marks."""
    source = visible(source)
    source = re.sub(r"\\(?:left|right|quad|qquad)(?![a-zA-Z])|\\[,;! ]", "", source)
    source = re.sub(r"\\(?:lvert|rvert)(?![A-Za-z])", "|", source)
    source = re.sub(r"\\mathrm\s+([a-zA-Z])", r"\1", source)
    source = re.sub(r"\\overline\s*(?:\{([A-Z])\}|([A-Z]))", lambda m: r"\bar " + (m[1] or m[2]), source)
    source = re.sub(r"([_^])\{([a-zA-Z0-9*]|\\[a-zA-Z]+)\}", r"\1\2", source)
    source = re.sub(r"\\(mathcal|mathfrak|mathscr|mathbb)\s*(?:\{([A-Za-z]+)\}|([A-Za-z]))",
                    lambda m: "〈" + m[1] + ":" + (m[2] or m[3]) + "〉", source)
    return "".join(source.replace("$", "").replace("&", "").replace("~", " ").replace("{}", "").split())


def table_rows(audit):
    """Read the explicit first-pass decisions and the localized excerpts."""
    decisions, excerpts = {}, {}
    scan = mode = None
    for line in audit.splitlines():
        if line.startswith("## Scan "):
            scan = line.split()[-1]
        if line == "**Differences from the blind record**":
            mode = "first"
        elif line == "## Local comparison after the witness review":
            mode = "extra"
        elif line == "### Page locations used for comparison":
            mode = "excerpt"
        elif line.startswith(("**", "##")):
            mode = None
        if not mode or not line.startswith("| "):
            continue
        fields = [x.replace(r"\|", "|") for x in line[2:-2].split(" | ")]
        if fields[0] in ("Place", "Scan", "---"):
            continue
        if mode == "first":
            place, initial, _, decision = fields
            decisions[scan, place] = initial, decision
        elif mode == "extra":
            sheet, place, initial, decision = fields
            decisions[sheet, place] = initial, decision
        else:
            sheet, place, number, excerpt = fields
            excerpts[sheet, place] = int(number), excerpt.strip("`")
    return decisions, excerpts


def cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ")


def row(*values):
    return "| " + " | ".join(map(cell, values)) + " |"


def code(value):
    fence = "`" * (1 + max((len(x) for x in re.findall(r"`+", value)), default=0))
    return fence + " " + value + " " + fence


def main():
    audit = (ROOT / f"{PREFIX}_audit.md").read_text(encoding="utf-8")
    decisions, excerpts = table_rows(audit)
    with (ROOT / f"{PREFIX}_blind.tsv").open(encoding="utf-8", newline="") as stream:
        records = list(csv.DictReader(stream, delimiter="\t"))
    compared = []
    seen = set()
    for scan, line_numbers in PAGE_LINES.items():
        entries = [r for r in records if r["scan"] == scan]
        page = (ROOT / "pages" / f"{PREFIX}_68_scan{scan}.tex").read_text(encoding="utf-8").splitlines()
        for item, line_no in zip(entries, line_numbers, strict=True):
            key = scan, item["place"]
            blind = item["what_the_crop_shows"]
            line = page[line_no - 1]
            if key in excerpts:
                anchor_line, scope = excerpts[key]
                if anchor_line != line_no or scope not in line:
                    raise ValueError(f"Page location changed at {key}, line {line_no}")
                same = normal(blind) == normal(scope)
            else:
                scope = line
                same = normal(blind) in normal(scope)
            seen.add(key)
            if key in decisions or not same:
                initial, decision = decisions.get(key, ("See audit for this line", "A difference needs review."))
                compared.append((scan, item["place"], line_no, code(blind), initial, decision, code(scope), "agrees" if same else "differs"))
    if len(seen) != len(records) or not decisions.keys() <= seen or not excerpts.keys() <= seen:
        raise ValueError("A scan or named comparison is missing")
    report = [
        "# Comparison of blind readings", "",
        f"The TSV contains {len(records)} image-only readings on {len(PAGE_LINES)} sheets. The table gives all {len(compared)} places with a recorded disagreement or a difference at the returned location. Entries are in manuscript order. The last column compares the blind wording with the primary returned reading and includes writing under a strike. A row can agree in the end even where its first-pass wording differed.", "",
        "Page lines refer to the individual LaTeX files. The returned excerpt preserves the cancellation, insertion, font and uncertainty commands. The comparison ignores spacing and equivalent TeX grouping. An equivalent rendering may therefore have an earlier difference recorded. The dated page audits and the final witness table give the successive ink readings.", "",
        row("Scan", "Place", "Page line", "Blind reading", "First-pass page", "Decision on the crop", "Returned excerpt", "Final comparison"),
        row(*(["---"] * 8)),
        *(row(*values) for values in compared)
    ]
    (ROOT / f"{PREFIX}_blind_compare.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"{len(records)} blind entries, {len(compared)} itemized comparisons")


if __name__ == "__main__":
    main()

