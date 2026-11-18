"""Requests for the English layer of the second-pass pages (17 Nov 2026 ~22 UTC, Claude Opus 5.5 at effort high).
Sources: second_pass/out/<package>/*_scan*.tex only (the Claude second pass), in the coordinator's priority order.
One request per page, GPT-6.1 Sol at reasoning effort max. usage: python -I -B prep2.py"""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
R = pathlib.Path(__file__).resolve().parent.parent
W = R / "_work2"
O = R.parent / "second_pass" / "out"
ORDER = ["MPL_144_168-184+148_001-028", "MPL_148_029-072", "MPL_149_001-090", "MPL_149_091-136", "MPL_143+141",
         "MPL_145", "MPL_146_001-099", "MPL_146_100-134", "MPL_147_003-047", "MPL_147_048-137", "MPL_147_138-190",
         "MPL_150_001-043", "MPL_150_044-084", "MPL_150_085-099+151_001-031", "MPL_151_032-075", "MPL_152+120",
         "MPL_105", "MPL_106+107"]
rows = ["id\tcote\tsource\tbytes\tpackage\torder"]
k = 0
for pkg in ORDER:
    for f in sorted((O / pkg).glob("*_scan*.tex")):
        m = re.search(r"_(\d+(?:-\d+)?)_scan(\d+)\.tex$", f.name)
        c, s = m.group(1), m.group(2)
        if re.fullmatch(r"\d{3}-\d{3}", c):  # single-cote package: MPL_149_001-090_scan001.tex
            c = re.match(r"MPL_(\d+)", pkg).group(1)
        oid = f"MPL_{c}_scan{s}"
        t = f.read_text(encoding="utf-8")
        (W / "prompt" / "user" / f"{oid}.txt").write_text(f"Cote {c}, scan {int(s)}.\n\n{t}", encoding="utf-8", newline="\n")
        k += 1
        rows.append(f"{oid}\t{c}\t{f.relative_to(R.parent).as_posix()}\t{len(t.encode('utf-8'))}\t{pkg}\t{k}")
(W / "files.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print(k, "pages")
