"""19 Nov 2026 (main session, Claude Opus 5.5 at effort max). The user, ~04:1x UTC: a Pro run silent for a few hours
ends at its last checkpoint ("intake the checkpoint as a final thing"); "Implement refill in the second pass ... don't
delete work". build_all_second_pass_20261117.py skips packages that have only checkpoints. This builds their second
pass: for every package in packages_done/ with no final return (returns/<PKG>_unzipped) but with checkpoint folders
(returns/<PKG>_checkpoint_NN[_label]_unzipped) whose newest is older than HOURS, and with no second pass yet (no files in
out/<PKG>, no prompts in prompts/PROMPT_<PKG>_*.md), it runs make_second_pass.py PKG --from <newest checkpoint>: the
checkpoint is Pro's final; each scan it lacks gets the existing Work or Codex reading as its first pass (REFILL in
make_second_pass.py). A sweep reading of the pages can be added by hand with --witness (see the RUNBOOK of 19 Nov).
usage: python -I -B build_stalled_second_pass_20261119.py [HOURS=3] [--dry]"""
import pathlib
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).resolve().parent
T = SP.parent
HOURS = float(next((a for a in sys.argv[1:] if not a.startswith("--")), 3))
dry = "--dry" in sys.argv
pat = re.compile(r"^(?P<pkg>.+)_checkpoint_(?P<n>\d+)(?:_\d{8}T\d{4}Z)?_unzipped$")
cps = {}
for r in (T / "returns").iterdir():
    m = pat.match(r.name)
    if m and r.is_dir():
        cps.setdefault(m["pkg"], []).append((int(m["n"]), r))
built, skipped = [], []
for pkg, lst in sorted(cps.items()):
    lst.sort()
    n, newest = lst[-1]
    why = None
    if (T / "returns" / f"{pkg}_unzipped").is_dir():
        why = "final filed"
    elif not any(d.is_dir() and d.name.endswith(pkg) for d in (T / "packages_done").iterdir()):
        why = "not in packages_done"
    elif (SP / "out" / pkg).is_dir() and any((SP / "out" / pkg).iterdir()):
        why = "second pass exists"
    elif list((SP / "prompts").glob(f"PROMPT_{pkg}_*.md")):
        why = "prompts built"
    elif (time.time() - newest.stat().st_mtime) / 3600 < HOURS:
        why = f"newest checkpoint younger than {HOURS} h"
    if why:
        skipped.append((pkg, f"cp{n:02d}", why))
        continue
    if dry:
        built.append((pkg, f"cp{n:02d}", "would build"))
        continue
    p = subprocess.run([sys.executable, "-I", "-B", str(SP / "make_second_pass.py"), pkg, "--from",
                        newest.relative_to(T).as_posix()], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=str(SP))
    built.append((pkg, f"cp{n:02d}", ("ok: " if p.returncode == 0 else "FAILED: ") + (p.stdout + p.stderr).strip()[-300:]))
for b in built:
    print("BUILT" if not dry else "DRY", *b)
for s in skipped:
    print("skip", *s)
