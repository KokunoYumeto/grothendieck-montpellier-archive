"""Rebuild prompt 42 as the night prompt GRH_NIGHT (21 Nov 2026, main session, Claude Opus 5.5 at effort max), at the user's
word: "here's what you're gonna do this night. These are two real fun proofs. One is GRH, the other is GRH. Your task is
to literally just grind out everything that this implies, like boundless research task. Continue until you have
everything that you know follows, and that you can derive from them, and keep updating with zips so you can keep reading
along with your work"; "feed it everything we already know, but not necessarily as a, you know, work on this only, but as
a, this is what we already found." The first 42 (TWO_GRH, unsent) is kept in _staging_20261120/42_TWO_GRH_unsent_superseded.
usage: python -I -B build_prompt_42_night.py"""
import pathlib, re, shutil, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
F22 = S / "from_22"
MV = D / "reports_20261120/masullo_math/MASULLO_MATH_VERSION_20261121.md"
MIDX = D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md"
INT21 = D / "field_experts/intake_20261121/intakes"
RR = D / "grothendieck_archive_transcription_20261110/research_returns"
SW3 = D / "results_register/horizontal/sweep3"
INT20 = D / "field_experts/intake_20261120/intakes"

OLD = Q / "42_TWO_GRH_Alpoge_and_Masullo_set_against_each_other"
if OLD.exists():
    shutil.move(str(OLD), str(S / "42_TWO_GRH_unsent_superseded"))

AG_LANG = """## The language of the results

State every consequence also in the language of algebraic geometry and of Grothendieck's frameworks. Tate's thesis and
the adelic language sit beside his trace formula of cote 1, Weil's explicit formula, purity (Weil I and II), motives and
their L-functions, λ-rings, Shimura varieties and theta correspondences. Say where it lives in his texts: the archive by
cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result can be used
in our programme, whatever else comes of it.

"""
IMPL = ("4. **`IMPLICATIONS.md`**: what the consequences change: for our programme on Grothendieck's work (cote and scan),\n"
        "   for our runs' open rows (run and statement id), for the open conjectures.\n"
        "5. **`CONSEQUENCES.tsv`**, the catalogue, one row per consequence, with these columns:\n"
        "   - id; statement;\n"
        "   - input: Alpöge / Masullo (conditional) / both / neither, plus the extra input it needs;\n"
        "   - status: proved here / classical with an exact locator / conditional on what / open, with its gate;\n"
        "   - where the proof is;\n"
        "   - where it lives in our work.\n"
        "   Keep it current in every checkpoint, so it can be read along.")


def hw(main_q, short):
    t = how_to_work(main_q, short).replace(LANG_PARAGRAPH, AG_LANG)
    t, n = re.subn(r"4\. \*\*`IMPLICATIONS\.md`\*\*:.*?\(cote and scan\)\.", lambda m: IMPL, t, flags=re.S)
    assert n == 1, "template changed"
    return t


TEXT = f"""# GRH_NIGHT: everything that follows from the two proofs of 20 November 2026

This is tonight's whole task, and it is open-ended by design. Two proofs of generalized Riemann hypotheses appeared on
20 November 2026, one formalized and one a long draft. Grind out everything they imply: every consequence that follows
from them, that you know or can derive, each proved or located, and organized into one catalogue we can read along with
you as the checkpoints come in.

{ALPOGE}
{MASULLO}
**Masullo, readable.** `MASULLO_MATH_VERSION_20261121.md` gives each page of the draft: its prose from the PDF's text
layer, and each formula in LaTeX under its line. The formulas were transcribed by a model over an API (Claude Opus 5.5
at effort high, Message Batches API, 21 Nov 2026) from page images; the source is not public. So when a formula looks
wrong, it may be a mistranscription. Check the page in `MASULLO_the-music-of-the-primes.pdf` (same page number) before you
conclude that the draft is wrong, and say which you checked.

## The task

Derive everything that follows from the two results and from their methods. For each consequence, give:
- its statement;
- its exact input: GRH for Dirichlet L-functions (Alpöge, a theorem); GRH for Hecke L-functions (Masullo, conditional);
  or more, with what more;
- a proof, or the exact locator of a classical proof;
- where it lives in our work.

The territory, all of it:
1. **Number theory.** The theorems that were conditional on these GRH statements and are now theorems or conditional on
   Masullo only:
   - primes in progressions, least non-residues and primitive roots, class numbers, effective Chebotarev;
   - Artin's primitive-root conjecture (Hooley);
   - Montgomery's pair correlation and the random-matrix statistics of low-lying zeros;
   - moments, the Lindelöf consequences, zero-density.
   Each with its constants where the classical proof gives them.
2. **Algebraic geometry and motives.** The zeta functions of schemes over Z, Artin-Tate and CM motives, purity-type
   statements, special values and K-groups where the zeros bear on them, and what the methods (theta lifts, positivity,
   the adelic trace formula) prove on their own.
3. **Our programme on Grothendieck's work.** What changes in his texts (cote 1's trace formula, cote 16, cote 34, cote
   44, cote 149, the anabelian and Grothendieck-Teichmüller line) and in the open rows of our runs.
4. **Complexity.** Derandomization, Koiran's Nullstellensatz, factoring, primality, and geometric complexity theory.
5. **The two proofs against each other.** Each used on the other: Alpöge's mechanisms to check Masullo's steps; Masullo's
   adelic framework to carry Alpöge's method to Hecke characters. Then the two together on what neither reaches alone
   (GL_2, Artin holomorphy).

The links to each of these are real. No consequence needs to be a mere corollary to be worth deriving, so do not ask
whether a link holds: show how it works, prove what follows, and where a route meets an obstacle, locate it and take the
next route.

## What we already found (attached): use it, do not redo it

These are our results so far. They are background for you to build on, correct where wrong, and cite by file and id:
- our intakes of 20-21 Nov (`OURS_INTAKE_*.md`);
- the bridges run (`OURS_BRIDGES_*`);
- the Hodge sketch (`OURS_HODGE_BRIDGE_SKETCH_20261121.md`);
- the Δ sextic answer (`OURS_DELTA_SEXTIC_20261121.md`);
- our Fable agent's suggestions (`OURS_FABLE_PROGRAM_SUGGESTIONS_*.md`);
- the IMPLICATIONS and LEDGER files of tonight's returns (`RETURN_<TAG>_*.md`);
- `ORDER_tonight.md`, the questions put to other runs tonight. Other runs are working on those questions; you do not
  have to, but use and extend what any of them gives you.

## The attached files

- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `MASULLO_the-music-of-the-primes.pdf`, `MASULLO_MATH_VERSION_20261121.md` (read the caveat above),
  `MASULLO_STATEMENTS_INDEX.md`.
- The files named in the previous section.

{hw("the full catalogue of consequences of the two results and their methods, each proved or located with its exact input, kept current in CONSEQUENCES.tsv through every checkpoint.", "GRH_NIGHT")}"""

out = Q / "42_GRH_NIGHT_everything_that_follows_from_the_two_proofs"
assert not out.exists(), out
out.mkdir(parents=True)
(out / "PROMPT.md").write_text(TEXT, encoding="utf-8")


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst))


files = {"ALPOGE_LEAN_MAP_20261120.md": AR / "ALPOGE_LEAN_MAP_20261120.md",
         "MASULLO_the-music-of-the-primes.pdf": MAS, "MASULLO_MATH_VERSION_20261121.md": MV, "MASULLO_STATEMENTS_INDEX.md": MIDX,
         "OURS_HODGE_BRIDGE_SKETCH_20261121.md": D / "reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md",
         "OURS_DELTA_SEXTIC_20261121.md": D / "reports_20261120/delta_sextic/DELTA_SEXTIC_20261121.md",
         "OURS_FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
         "OURS_FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md",
         "ORDER_tonight.md": Q / "ORDER.md"}
for n in ("QUESTIONS.tsv", "LEDGER.md", "IMPLICATIONS.md", "BRIDGES_20261120.tex"):
    files[f"OURS_BRIDGES_{n}"] = AR / "bridges" / n
for f in sorted(INT21.glob("*/INTAKE_*_20261121.md")):
    files["OURS_" + f.name] = f
for f in sorted(list(SW3.glob("SA*/INTAKE_RESEARCH_*_20261120*.md")) + list(INT20.glob("*/INTAKE_*_20261120.md"))):
    files["OURS_" + f.name] = f
newest = {}
for d in RR.iterdir():
    m = re.match(r"^(GCT_[A-Z]+|CX_GRH|ALPOGE_[A-Z]+|DELTA23|AN_GRH|K17|HODGE_SIGN|TRACE_DET|DP_MULT|ZETA_TWO|CUE_GCT|THETA3|HECKE_DIV|GHOSTS|JAC1964|DEG_L)_(?:checkpoint_(\d+)|final)", d.name)
    if m and d.is_dir():
        key = (1, 0) if m.group(2) is None else (0, int(m.group(2)))
        if m.group(1) not in newest or key > newest[m.group(1)][0]:
            newest[m.group(1)] = (key, d)
for tag, (k, d) in sorted(newest.items()):
    for n in ("IMPLICATIONS.md", "LEDGER.md", "QUESTIONS.tsv"):
        hits = list(d.glob(n)) or list(d.glob("*/" + n))
        if hits:
            files[f"RETURN_{tag}_{'final' if k[0] else 'cp%02d' % k[1]}_{n}"] = hits[0]
for n in ["ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "ALPOGE_LEAN_SCAN.tsv"]:
    put(F22 / n, out / n)
for n, src in files.items():
    if src.exists():
        put(src, out / n)
    else:
        print("MISSING", src)
print("attached", len(files) + 4, "files")
PY = sys.executable
r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("pack:", (r.stdout.strip().splitlines() or ["?"])[-1])
pm = out / "PROMPT.md"
for args in (["claude_tools/push_rule_pro_prompts.py", "--lint-math"], ["claude_tools/paper_completeness_lint.py"]):
    a = subprocess.run([PY, "-I", "-B", str(D / args[0]), *args[1:], str(pm)], capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    print(args[0], "->", (a.stdout.strip().splitlines() or ["?"])[-1])
    if "failing lint: 0" not in a.stdout and "failing: 0" not in a.stdout:
        print(a.stdout[-1500:])
print(", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip")))
