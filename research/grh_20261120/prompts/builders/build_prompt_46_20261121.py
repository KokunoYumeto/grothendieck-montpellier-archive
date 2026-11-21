"""Prompt 46 HODGE_DIVISION (21 Nov 2026 ~07:xx UTC, main session e0d20ada, Claude Opus 5.5 at effort max), at the user's
word: "If you've reduced the fucking Hodge conjecture to a single arithmetic quantity, go fucking work on it." The
mathematics is the core written by the Hodge-line agent abcaba9b (Claude Opus 5.5 at effort high) from its attack
(reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md); the house frame (push rule, three-hour review,
checkpoints, CHECK_EVENTS) comes from how_to_work through build_prompts_43_45.py's helpers. Then pack_one_zip and both lints.
python -I -B build_prompt_46_20261121.py"""
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "build_prompts_43_45.py").read_text(encoding="utf-8")
g = {"__file__": str(HERE / "build_prompts_43_45.py"), "__name__": "helpers_43_45"}
exec(compile(src.split("\nP = {}")[0], "build_prompts_43_45.py", "exec"), g)
hw, newest, put, from_previous_zip, return_files, D, Q, INT = (g[k] for k in ("hw", "newest", "put", "from_previous_zip",
                                                                         "return_files", "D", "Q", "INT"))
HB = D / "reports_20261120/hodge_bridge"
core = (HB / "HODGE_DIVISION_PROMPT_CORE_20261121.md").read_text(encoding="utf-8")
core = core.split("## The target, in one sentence", 1)[1]
core = "## The target, in one sentence" + core
core = core.replace("attack file", "`HODGE_DIVISION_ATTACK_20261121.md`").replace("`division_attack_scripts\\`",
                                                                                   "`division_attack_scripts/`")
FOLDER = "46_HODGE_DIVISION_bounding_the_detector_degree_of_Weil_classes"
text = f"""# HODGE_DIVISION: bounding the detector degree of Weil classes

This prompt continues the Hodge line of 20-21 November 2026: our prompts 37 to 41 (THETA3, HECKE_DIV, GHOSTS, JAC1964,
DEG_L) and 45 (SIGN_NEXT). Their returns and our intakes of them are attached, with an attack on their reduction by
Claude Opus 5.5 at effort high (`HODGE_DIVISION_ATTACK_20261121.md`, with its check events and scripts).

**What is settled.** Algebraicity of a Hodge class on every fibre of a family is equivalent to a bounded division bound c_t
on one Zariski-dense set: one Hecke orbit, the CM points, or infinitely many primes. With the rational Hodge conjecture for
CM abelian varieties (032), the Hodge conjecture for abelian varieties is equivalent to the finiteness of the supremum of
c_t over the CM points of every special subvariety, and a counterexample would be a ghost. For Weil classes, c_t is
controlled by one integer, the detector degree δ_W. This run bounds it.

{core}
## The attached files

- `HODGE_DIVISION_ATTACK_20261121.md`, `HODGE_DIVISION_ATTACK_20261121_CHECK_EVENTS.tsv` and `division_attack_scripts/`:
  the attack this prompt continues.
- `RETURN_<RUN>_*/` for GHOSTS, HECKE_DIV, DEG_L, THETA3, JAC1964 and SIGN_NEXT: each run's paper and registers.
- `INTAKE_*`: our intakes of these runs, with their check events.
- `PREVIOUS_PROMPT_39.md` and its attachments (the GHOSTS prompt as sent, with its sources).
- `032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf`, the van Hoften-Sempliner deposit
  (Hexagon 2610.00259) and Milne's report (Hexagon 2611.00244).

{hw("a uniform bound for the detector degree δ_W of Weil classes on a Zariski-dense set of each Weil family, in the order of the targets above: Q(i) with n = 2, then n = 3, then n = 4 through G₃₄-covers, then n ≥ 5 through G(d,e,m).", "HODGE_DIVISION")}"""
out = Q / FOLDER
assert not out.exists(), out
out.mkdir(parents=True)
(out / "PROMPT.md").write_text(text, encoding="utf-8")
put(HB / "HODGE_DIVISION_ATTACK_20261121.md", out / "HODGE_DIVISION_ATTACK_20261121.md")
put(HB / "HODGE_DIVISION_ATTACK_20261121_CHECK_EVENTS.tsv", out / "HODGE_DIVISION_ATTACK_20261121_CHECK_EVENTS.tsv")
if (HB / "division_attack_scripts").is_dir():
    put(HB / "division_attack_scripts", out / "division_attack_scripts")
from_previous_zip("39", out)
for run in ("GHOSTS", "HECKE_DIV", "DEG_L", "THETA3", "JAC1964", "SIGN_NEXT"):
    return_files(run, out, ["*.tex", "QUESTIONS.tsv", "LEDGER.md", "IMPLICATIONS.md", "CHECK_EVENTS.tsv"])
    for f in sorted((INT / run).glob("INTAKE_*")):
        put(f, out / f.name)
for name, rel in (("032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf",
                   "recent_results_20261110/papers/032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf"),
                  ("Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf",
                   "recent_results_20261110/papers/hodge_sources_20261121/Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf"),
                  ("Hexagon_2611.00244v1_Milne_report.pdf",
                   "recent_results_20261110/papers/hodge_sources_20261121/Hexagon_2611.00244v1_Milne_report.pdf")):
    if (D / rel).exists() and not (out / name).exists():
        put(D / rel, out / name)
for sub in sorted(p for p in out.iterdir() if p.is_dir()):
    shutil.make_archive(str(out / sub.name), "zip", root_dir=sub)
    shutil.rmtree(sub)
PY = sys.executable
r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True,
                   text=True, encoding="utf-8", errors="replace")
print(FOLDER, "pack:", (r.stdout.strip().splitlines() or ["?"])[-1])
pm = out / "PROMPT.md"
for args in (["claude_tools/push_rule_pro_prompts.py", "--lint-math"], ["claude_tools/paper_completeness_lint.py"]):
    a = subprocess.run([PY, "-I", "-B", str(D / args[0]), *args[1:], str(pm)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print("  ", args[0], "->", (a.stdout.strip().splitlines() or ["?"])[-1])
    if "failing lint: 0" not in a.stdout and "failing: 0" not in a.stdout:
        print(a.stdout[-1500:])
print("  ", ", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip")))
