"""Verify the built prompts of batch_20261119/ (19 Nov 2026): for every row of ORDER.tsv, its folder is flat with at
most 20 files, every file is under 450 MB, PROMPT.md has no unfilled placeholder and passes
`claude_tools/push_rule_pro_prompts.py --lint-math`; rewrites the lint, files and MB columns from what it finds.
usage: python -I -B verify_batch.py
Written by Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026."""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wt_common as W  # noqa: E402
import build_batch as B  # noqa: E402

rows = B.rows_of(B.ORDER)
prompts = [B.BATCH / r["folder"] / "PROMPT.md" for r in rows]
lint = subprocess.run([sys.executable, "-I", "-B", str(W.LINT), "--lint-math"] + [str(p) for p in prompts],
                      capture_output=True, text=True, encoding="utf-8")
failing = {pathlib.Path(m).parent.name for m in re.findall(r"^FAIL (\S+PROMPT\.md)", lint.stdout, re.M)}
bad = 0
for r in rows:
    f = B.BATCH / r["folder"]
    files = [p for p in f.iterdir()]
    problems = []
    if any(p.is_dir() for p in files):
        problems.append("not flat")
    if len(files) > 20:
        problems.append(f"{len(files)} files")
    if any(p.stat().st_size >= 450e6 for p in files):
        problems.append("a file over 450 MB")
    t = (f / "PROMPT.md").read_text(encoding="utf-8")
    if re.search(r"\{[A-Z_]{3,}\}", t):
        problems.append("placeholder left")
    if f.name in failing:
        problems.append("lint")
    r["lint"] = "pass" if not problems else "FAIL " + ", ".join(problems)
    r["files"] = len(files)
    r["MB"] = round(sum(p.stat().st_size for p in files) / 1e6, 1)
    bad += bool(problems)
B.ORDER.write_text(W.tsv(rows, B.OCOLS), encoding="utf-8", newline="")
print(f"verified {len(rows)} prompts: {len(rows) - bad} pass, {bad} fail; lint: {lint.stdout.strip().splitlines()[-1]}; "
      f"{sum(float(r['MB']) for r in rows):.0f} MB")
