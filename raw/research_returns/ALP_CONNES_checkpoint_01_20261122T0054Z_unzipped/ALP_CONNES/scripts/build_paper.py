#!/usr/bin/env python3
"""Compile the paper with the TeX trees available in this workspace."""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
out = root / "evidence"
out.mkdir(exist_ok=True)
env = dict(os.environ)
env["TEXMFDIST"] = "/usr/share/texlive/texmf-dist"
env["TEXMF"] = "{/usr/share/texlive/texmf-dist,/usr/share/texmf}"
env["TEXFORMATS"] = str(out)
if not (out / "pdflatex.fmt").exists():
    cmd = ["pdftex", "-ini", "-etex", "-interaction=nonstopmode",
           "-jobname=pdflatex", "-progname=pdflatex", "pdflatex.ini"]
    result = subprocess.run(cmd, cwd=out, env=env, capture_output=True, text=True)
    (out / "format_build_stdout.txt").write_text(result.stdout + result.stderr)
    if result.returncode:
        print("\n".join((result.stdout + result.stderr).splitlines()[-45:]))
        sys.exit(result.returncode)

passes = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for index in range(passes):
    cmd = ["pdftex", "-fmt=pdflatex", "-interaction=nonstopmode", "-halt-on-error",
           "-output-directory=evidence", "ALP_CONNES.tex"]
    result = subprocess.run(cmd, cwd=root, env=env, capture_output=True, text=True)
    log = result.stdout + result.stderr
    (out / "build_stdout.txt").write_text(log)
    if result.returncode:
        print("\n".join(log.splitlines()[-45:]))
        sys.exit(result.returncode)
    print(f"Pass {index+1}: " + next((line for line in log.splitlines()
                                     if line.startswith("Output written")), "completed"))
print("Build succeeded. Mathematical checks and visual inspection are separate.")
