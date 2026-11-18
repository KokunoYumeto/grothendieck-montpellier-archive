"""Prepare the raw English translation of Montpellier archive pages (cotes 103-107, 134-1), one request per page.
17 Nov 2026, Claude Opus 5.5 at effort high, for GPT-6.1 Sol at reasoning effort max.
Sources: first-pass pages (returns/MPL_105_unzipped, returns/MPL_106+107_unzipped: no second-pass page exists yet,
second_pass/out/MPL_105 and MPL_106+107 are empty on 17 Nov) and the Codex web returns for 103, 104 and 134-1
(codex_web_20261113/returns/H103-01, H104-01, H104-02, H134-01; listed in packages_work/CODEX_COVERED_SCANS.tsv).
usage: python -I -B prep.py"""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent.parent / "_work"
T = W.parent.parent
SRC = [("105", T / "returns/MPL_105_unzipped/pages"), ("106+107", T / "returns/MPL_106+107_unzipped/pages"),
       ("103", T / "codex_web_20261113/returns/H103-01/out/pages"),
       ("104", T / "codex_web_20261113/returns/H104-01/out/pages"),
       ("104", T / "codex_web_20261113/returns/H104-02/out/pages"),
       ("134-1", T / "codex_web_20261113/returns/H134-01/out/pages")]
rows = ["id\tcote\tsource\tbytes"]
for cote, d in SRC:
    for f in sorted(d.glob("*.tex")):
        m = re.search(r"_(\d+(?:-\d+)?)_scan(\d+)\.tex$", f.name)
        c, s = m.group(1), m.group(2)
        oid = f"MPL_{c}_scan{s}"
        t = f.read_text(encoding="utf-8")
        (W / "prompt" / "user" / f"{oid}.txt").write_text(f"Cote {c}, scan {int(s)}.\n\n{t}", encoding="utf-8", newline="\n")
        rows.append(f"{oid}\t{c}\t{f.relative_to(T).as_posix()}\t{len(t.encode('utf-8'))}")
(W / "files.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print(len(rows) - 1, "pages")
