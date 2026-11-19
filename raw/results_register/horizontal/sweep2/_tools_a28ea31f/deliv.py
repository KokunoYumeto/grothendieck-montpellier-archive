"""Sweep 3 deliverables census (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max).
For each transcription of the deep topics: per page, words and open-reading markers; Codex folder coverage.
python -I -B deliv.py macros | census
"""
import re, glob, sys, collections, csv
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
PRO = {"SA15": ["MPL_5+6_001-037", "MPL_6_038-067+7_001-060", "MPL_7_061-072+8_001-078", "MPL_8_079-081+9+4+100"],
       "SA05": ["MPL_11_002-042", "MPL_11_043-058+56", "MPL_12_002-050", "MPL_12_051-098", "MPL_12_099-149", "MPL_12_150-168+15_002-033", "MPL_15_139-194"],
       "SA06": ["MPL_14_002-044", "MPL_14_087-132", "MPL_15_034-086", "MPL_15_087-138", "MPL_15_170-194r"],
       "SA07": ["MPL_15_195-228+18_002-017", "MPL_18_018-062"]}
CODEX = {"SA15": ["K4-01", "K8-01", "K9-01", "K9-02"],
         "SA05": ["K11-01", "K11-02", "K11-03", "K11-04", "K12-01", "K12-02", "K12-03", "K12-04", "K12-05", "K12-06", "K12-07", "K12-08", "K12-09",
                  "K14-01", "K14-07", "K15-03", "K15-04", "K15-09", "K15-10", "K16-01", "K16-03", "K16-04", "K18-01", "K18-02", "K18-03", "K18-04",
                  "B10-01", "B10-02", "B10-03", "B10-04", "B10-05", "B10-06", "B10-07", "B10-08", "B10-09", "B10-10", "B12-01", "B12-02",
                  "H13-01", "J13-01", "J13-02", "J13-03", "J13-04", "J13-05"],
         "SA06": ["K14-02", "K14-03", "K14-04", "K14-05", "K14-06", "K14-08", "K14-09", "K15-02", "K15-05", "K15-06", "K15-07", "K15-08", "B15-01", "B15-02", "B15-03"],
         "SA07": ["K10-01", "K10-02", "K10-03", "K10-04", "K10-05", "K10-06", "K10-07", "K16-02", "K19-01", "K19-02", "K19-03", "K19-04", "K19-05", "K19-06"]}
DOUBT = re.compile(r"\\(unsure|illegible|unclear|doubt|gap|uncertain)\b")


def pages(pkg):
    fs = sorted(glob.glob(str(T / "returns" / f"{pkg}_unzipped" / "**" / "pages" / "*.tex"), recursive=True))
    if not fs:
        fs = sorted(glob.glob(str(T / "returns" / f"{pkg}*_unzipped" / "**" / "pages" / "*.tex"), recursive=True))
    out = []
    for f in fs:
        m = re.search(r"_(\d+)_scan(\d+)\.tex$", f)
        if m:
            out.append((m.group(1), int(m.group(2)), f))
    return out


def macros():
    c = collections.Counter()
    for pkg in PRO["SA15"][:1]:
        for _, _, f in pages(pkg):
            c.update(re.findall(r"\\[a-zA-Z]+", open(f, encoding="utf-8").read()))
    print(c.most_common(40))


def codex_cov(folder):
    inv = T / "codex_web_20261113/returns" / folder / "out" / f"{folder}_inventory.csv"
    cov = set()
    if inv.exists():
        for r in csv.DictReader(open(inv, encoding="utf-8")):
            try:
                cov.add((r["cote"].strip(), int(r["scan"])))
            except Exception:
                pass
    return cov


def census():
    rows = []
    for t in PRO:
        cov = {}
        for f in CODEX[t]:
            for k in codex_cov(f):
                cov.setdefault(k, []).append(f)
        for pkg in PRO[t]:
            for cote, scan, f in pages(pkg):
                s = open(f, encoding="utf-8").read()
                rows.append((t, pkg, cote, scan, len(s.split()), len(DOUBT.findall(s)), "+".join(cov.get((cote, scan), []))))
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["topic", "package", "cote", "scan", "words", "open_marks", "codex_folders"])
    for r in rows:
        w.writerow(r)


if __name__ == "__main__":
    {"macros": macros, "census": census}[sys.argv[1]]()
