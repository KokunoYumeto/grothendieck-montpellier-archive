"""Sweep 3 tables (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max).
python -I -B sweep3_tsv.py SAnn  -> sweep3/SAnn/DEPENDS.tsv, CORRECTIONS.tsv, CHECK_EVENTS.tsv, DELIVERABLES.tsv
Data per topic in s3data_SAnn.py (DEPENDS, CORRECTIONS, CHECKS, READ, NOTE).
"""
import csv, sys, re, collections, importlib.util
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
H = Path(r"C:/Users/user/Documents/results_register/horizontal")
TOOLS = H / "sweep2/_tools_a28ea31f"
WHO = "Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3"
CENSUS = Path(r"C:/Users/user/AppData/Local/Temp/claude/f2c80a22394db22f/b68718a3-5179-4204-bc56-f8f64eac8af1/scratchpad/census.tsv")


def w(p, head, rows):
    with open(p, "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(head)
        for r in rows:
            wr.writerow([re.sub(r"\s+", " ", str(x)).strip() for x in r])


def ranges(nums):
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


def main(t):
    p = TOOLS / f"s3data_{t}.py"
    spec = importlib.util.spec_from_file_location("d", p)
    D = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(D)
    out = H / "sweep3" / t
    w(out / "DEPENDS.tsv", ["item", "relation", "uses_item", "basis", "page_that_shows_it", "note"], D.DEPENDS)
    w(out / "CORRECTIONS.tsv", ["where", "what", "correction", "reason", "by"], [list(c) + [WHO] for c in D.CORRECTIONS])
    w(out / "CHECK_EVENTS.tsv", ["id", "date_utc", "who", "how", "result", "where"],
      [[c[0], "2026-11-18", WHO, c[1], c[2], c[3]] for c in D.CHECKS])
    rows = list(csv.DictReader(open(CENSUS, encoding="utf-8"), delimiter="\t"))
    allcodex = {}
    for r in rows:
        if r["codex_folders"]:
            allcodex[(r["cote"], int(r["scan"]))] = r["codex_folders"]
    agg = collections.OrderedDict()
    for r in rows:
        if r["topic"] != t:
            continue
        k = (r["package"], r["cote"])
        a = agg.setdefault(k, {"scans": [], "words": 0, "open": 0, "cov": set(), "covn": 0})
        s = int(r["scan"])
        a["scans"].append(s)
        a["words"] += int(r["words"])
        a["open"] += int(r["open_marks"])
        if (r["cote"], s) in allcodex:
            a["covn"] += 1
            a["cov"].update(allcodex[(r["cote"], s)].split("+"))
    drows = []
    for (pkg, cote), a in agg.items():
        rd = D.READ.get((pkg, cote), ("not read in sweep 3", ""))
        passes = "Pro transcription and Pro notes (first pass)"
        if a["covn"]:
            passes += f"; Codex web transcription of {a['covn']} of {len(a['scans'])} pages ({', '.join(sorted(a['cov']))}) with Work math notes and Codex sheet notes"
        if pkg in getattr(D, "SECOND_PASS", {}):
            passes += "; " + D.SECOND_PASS[pkg]
        if a["covn"] >= 0.8 * len(a["scans"]):
            ready = f"after collation of the two transcriptions and the {a['open']} open readings"
        else:
            ready = f"after a second pass on the {a['open']} open readings"
        ready = D.READY.get((pkg, cote), ready)
        drows.append([t, pkg, cote, ranges(a["scans"]), len(a["scans"]), a["words"], a["open"], passes, rd[0], ready, rd[1]])
    for extra in getattr(D, "EXTRA_DELIV", []):
        drows.append([t] + list(extra))
    w(out / "DELIVERABLES.tsv", ["topic", "package_or_folder", "cote", "scans", "pages", "words", "open_readings",
                                 "passes", "read_in_sweep3", "edition_and_translation", "note"], drows)
    print(t, "depends", len(D.DEPENDS), "corrections", len(D.CORRECTIONS), "checks", len(D.CHECKS), "deliverables", len(drows))


if __name__ == "__main__":
    main(sys.argv[1])
