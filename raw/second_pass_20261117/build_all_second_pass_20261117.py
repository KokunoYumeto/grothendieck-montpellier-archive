"""17 Nov 2026: prepare the Claude second pass of every returned Pro final that has not had one: run make_second_pass.py
for each (block prompts in second_pass/prompts/, images in second_pass/img/<PKG>/: extracted from the scans zip, or
rendered again from the source PDFs where the zip is gone). Skips checkpoints, the chat B runs (witnesses inside their
main package's prompts) and packages whose second pass exists (second_pass/out/<PKG>/). Log: BUILD_ALL_20261117.log.
usage: python -I -B build_all_second_pass_20261117.py"""
import pathlib
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).resolve().parent
T = SP.parent
pkgs = []
for r in sorted((T / "returns").iterdir()):
    if not r.name.endswith("_unzipped") or "checkpoint" in r.name or r.name.endswith("_chatB_unzipped"):
        continue
    pkg = r.name[: -len("_unzipped")]
    if (SP / "out" / pkg).is_dir() and any((SP / "out" / pkg).iterdir()):
        continue
    pkgs.append(pkg)
log = open(SP / "BUILD_ALL_20261117.log", "a", encoding="utf-8")
log.write(f"start {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())}: {len(pkgs)} packages\n")
fails = []
for pkg in pkgs:
    t0 = time.time()
    p = subprocess.run([sys.executable, "-I", "-B", str(SP / "make_second_pass.py"), pkg], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", cwd=str(SP))
    out = (p.stdout + p.stderr).strip().replace("\n", " | ")
    log.write(f"{pkg}\texit {p.returncode}\t{round(time.time() - t0)} s\t{out[:600]}\n")
    log.flush()
    if p.returncode:
        fails.append(pkg)
log.write(f"end {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())}: {len(pkgs) - len(fails)} built, failed: {fails}\n")
log.close()
print(len(pkgs), "packages;", len(pkgs) - len(fails), "built; failed:", fails)
