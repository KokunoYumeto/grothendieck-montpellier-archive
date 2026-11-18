"""Compile the batch-K Work returns that the audit found with LaTeX errors, keep their logs, and tally the error kinds
(18 Nov 2026, the main session, Claude Opus 5.5 at effort max). Reads AUDIT_K_RETURNS_<date>.tsv; writes the logs to
audit_compile_logs_<date>/<ID>.log and a tally to stdout. No shell escape; each compile in a temporary folder.
usage: python -I -B tools/compile_errors_k.py [DATE]"""
import collections
import csv
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

CW = pathlib.Path(__file__).resolve().parent.parent
PRE = pathlib.Path(sys.argv[sys.argv.index("--preamble") + 1]) if "--preamble" in sys.argv else None
TAG = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else ""
pos = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and sys.argv[i - 1] not in ("--preamble", "--tag")]
D = pos[0] if pos else "20261118"
LUA = shutil.which("lualatex")
OUT = CW / f"audit_compile_logs_{D}{TAG}"
OUT.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(CW / f"AUDIT_K_RETURNS_{D}{TAG}.tsv", encoding="utf-8"), delimiter="\t"))
bad = [r for r in rows if r["compile_errors"] not in ("", "0")]
kinds, undefined, per = collections.Counter(), collections.Counter(), {}
for r in bad:
    fid = r["id"]
    out = CW / "returns" / fid / "out"
    if not out.is_dir():
        continue
    with tempfile.TemporaryDirectory() as tmp:
        for f in out.iterdir():
            if f.is_file() and f.suffix in (".tex", ".sty"):
                shutil.copy(f, tmp)
        if (out / "pages").is_dir():
            shutil.copytree(out / "pages", pathlib.Path(tmp) / "pages")
        if PRE:
            shutil.copy(PRE, pathlib.Path(tmp) / "PREAMBLE.tex")
        try:
            subprocess.run([LUA, "-no-shell-escape", "-interaction=nonstopmode", f"{fid}_standalone.tex"], cwd=tmp,
                           capture_output=True, timeout=180)
        except subprocess.TimeoutExpired:
            per[fid] = ["timeout"]
            continue
        log = pathlib.Path(tmp) / f"{fid}_standalone.log"
        if not log.exists():
            per[fid] = ["no log"]
            continue
        lg = log.read_text(encoding="utf-8", errors="replace")
        shutil.copy(log, OUT / f"{fid}.log")
    errs = re.findall(r"^! (.*)$", lg, flags=re.M)
    per[fid] = errs
    for e in errs:
        k = re.sub(r"\d+", "N", e.strip())[:70]
        kinds[k] += 1
    for m in re.finditer(r"^! Undefined control sequence\.\s*\n.*?(\\[A-Za-z@]+)\s*$", lg, flags=re.M):
        undefined[m.group(1)] += 1
    for m in re.finditer(r"^! (?:LaTeX|Package \w+) Error: (?:Environment|Unknown) (\S+) undefined", lg, flags=re.M):
        undefined[m.group(1)] += 1
print("returns compiled again:", len(per))
print("error kinds:")
for k, v in kinds.most_common(25):
    print(f"  {v:5d}  {k}")
print("undefined commands and environments:")
for k, v in undefined.most_common(30):
    print(f"  {v:5d}  {k}")
first = {fid: (e[0][:90] if e else "") for fid, e in per.items()}
print("first error per return (no PDF ones first):")
for r in sorted(bad, key=lambda r: r["pdf_pages"] not in ("", "0")):
    if r["id"] in first:
        print(f"  {r['id']:10s} pdf {r['pdf_pages'] or '-':>3s}  {first[r['id']]}")
