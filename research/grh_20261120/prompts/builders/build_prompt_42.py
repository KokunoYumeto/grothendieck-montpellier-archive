"""Build Pro research prompt 42, TWO_GRH (21 Nov 2026, main session, Claude Opus 5.5 at effort max), at the user's word:
"that is generally like a huge thing you can send over Pro as well. Basically, like take these, smash them together, see
what you get ... with the LaTeX now in hand" (the math version of Masullo's draft, made 21 Nov). Also: "make sure that
the agents are aware that it's transcribed by the API, and that if they think something is wrong, it could also just be
a mistranscription."
usage: python -I -B build_prompt_42.py"""
import pathlib, re, shutil, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
F22 = S / "from_22"
MV = D / "reports_20261120/masullo_math/MASULLO_MATH_VERSION_20261121.md"
MIDX = D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md"
INT = D / "field_experts/intake_20261121/intakes"
TR = D / "grothendieck_archive_transcription_20261110/text_of_record/pages"

AG_LANG = """## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks. Tate's thesis and the
adelic language of Masullo's draft sit beside the trace formula of cote 1, Weil's explicit formula, purity (Weil I and
II), motives and their L-functions, and Shimura varieties and theta correspondences. Say where each finding lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator. That way every result can be
used in our programme whatever the outcome of the main question.

"""
IMPL = ("4. **`IMPLICATIONS.md`**: what the findings change: for each of the two proofs; for the statements beyond both;\n"
        "   for Grothendieck's texts by cote and scan; for our runs (run and statement id).")


def hw(main_q, short):
    t = how_to_work(main_q, short).replace(LANG_PARAGRAPH, AG_LANG)
    t, n = re.subn(r"4\. \*\*`IMPLICATIONS\.md`\*\*:.*?\(cote and scan\)\.", lambda m: IMPL, t, flags=re.S)
    assert n == 1, "template changed"
    return t


TEXT = f"""# TWO_GRH: Alpöge's proof and Masullo's draft, set against each other and combined

This prompt stands on its own; it runs beside our other research prompts on the two proofs (22-41).

{ALPOGE}
{MASULLO}
**Masullo, readable.** `MASULLO_MATH_VERSION_20261121.md` gives each page of the draft: its prose from the PDF's text
layer, and each formula in LaTeX under the line it sits on. The formulas were transcribed by a model over an API (Claude
Opus 5.5 at effort high, Message Batches API, 21 Nov 2026) from images of the pages; Masullo's source is not public. So
when a formula looks wrong, it may be a mistranscription rather than an error in the draft. Before you conclude that the
draft is wrong, check the page in `MASULLO_the-music-of-the-primes.pdf` (same page number), and say which you checked.

## The question

Two proofs of the Riemann hypothesis for families of L-functions appeared on the same day, by different routes:
- **Alpöge**, for ζ and Dirichlet L-functions. The route: a Stepanov determinant; p-adic divisibility of CM theta
  derivatives; a definite sign from middle cohomology; Gan-Gross-Prasad periods; iterated theta lifts between definite
  unitary groups; a relative trace formula; the Bost slope inequality.
- **Masullo**, for the Hecke L-functions of every number field. The route: adelic θ-functions; idelic zeta functions;
  periodic and orbital Schauder bases; a trace formula on the orbital pieces of a lifted convolution kernel; polar
  multiplicities; a discussion of the programmes of Connes and Deninger.

Their objects meet: theta functions, trace formulas, positivity, the place at infinity. These links are real; neither
proof is a corollary of the other, or that would already be known. So the task is not to ask whether they relate. It is
to show exactly how, and then to use the two together on what neither does alone. Where a route meets an obstacle,
locate it exactly and attack it with the next tool. An obstacle is never an end point.

## The task

1. **Side by side.** Set the two proofs against each other, step by step:
   - Alpöge's steps 0-20 (the note's pages 1-4, with the Lean files);
   - Masullo's chapters, by statement number (`MASULLO_STATEMENTS_INDEX.md`; the math version).

   For each meeting point, give the exact dictionary: Alpöge's theta lifts against Masullo's adelic θ-functions, the
   two trace formulas, the two positivity mechanisms, the treatment of multiplicity and of the archimedean place.
2. **What each gives the other.**
   - Use Alpöge's mechanisms, formalized in Lean, to check the steps of Masullo's draft and to repair the gaps you
     find. One of our runs reports that the draft's final numbered divisor theorem is unfinished; settle it.
   - Use Masullo's adelic framework to carry Alpöge's method from Dirichlet characters to the Hecke characters of every
     number field, step by step, with the places where the carrying needs new input stated and attacked.
3. **Beyond both.** With the two together, attack what each alone does not reach:
   - GRH for L-functions of GL_2 forms and of elliptic curves;
   - Artin's holomorphy conjecture. Under Masullo, Brauer induction already places every zero and pole of an Artin
     L-function in the strip on the line, so holomorphy is the gap;
   - the effective Chebotarev bounds;
   - the conditional theorems our intakes listed (Koiran's Nullstellensatz in AM, Evdokimov's factoring bound).
4. **Grothendieck's side.** Our intakes, our Fable agent's suggestions and the Hodge sketch (attached) found three
   meeting points:
   - cote 1's trace formula for trace-class operators;
   - the Hodge-index route of cote 16;
   - one theta machine in several signatures.

   Say what each of the two proofs and their combination does at these places.

## The attached files

- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`
  (our map of the Lean archive: the proof chain, its inputs and files).
- `MASULLO_the-music-of-the-primes.pdf` (the draft), `MASULLO_MATH_VERSION_20261121.md` (read the caveat above),
  `MASULLO_STATEMENTS_INDEX.md`.
- Our intakes of 21 Nov: `INTAKE_CX_GRH_20261121.md` (the exact GRH each complexity result needs) and
  `INTAKE_ALPOGE_BRIDGES_20261121.md`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`, `HODGE_BRIDGE_SKETCH_20261121.md`: unchecked leads
  from our agents.
- `ARCHIVE_1_scan078.tex` to `ARCHIVE_1_scan082.tex` and `ARCHIVE_1_scan110.tex` to `ARCHIVE_1_scan113.tex`: cote 1's
  trace formula.

{hw("the two proofs set against each other step by step, each used on the other (Alpöge's mechanisms to check and repair Masullo's draft; Masullo's adelic framework to carry Alpöge's method to Hecke characters), and their combination used on what neither reaches alone.", "TWO_GRH")}"""

out = Q / "42_TWO_GRH_Alpoge_and_Masullo_set_against_each_other"
assert not out.exists(), out
out.mkdir(parents=True)
(out / "PROMPT.md").write_text(TEXT, encoding="utf-8")


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst))


for n in ["ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "ALPOGE_LEAN_SCAN.tsv"]:
    put(F22 / n, out / n)
extra = {"ALPOGE_LEAN_MAP_20261120.md": AR / "ALPOGE_LEAN_MAP_20261120.md",
         "MASULLO_the-music-of-the-primes.pdf": MAS, "MASULLO_MATH_VERSION_20261121.md": MV, "MASULLO_STATEMENTS_INDEX.md": MIDX,
         "INTAKE_CX_GRH_20261121.md": INT / "CX_GRH/INTAKE_CX_GRH_20261121.md",
         "INTAKE_ALPOGE_BRIDGES_20261121.md": INT / "ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121.md",
         "FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
         "FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md",
         "HODGE_BRIDGE_SKETCH_20261121.md": D / "reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md"}
extra.update({f"ARCHIVE_1_scan{n:03d}.tex": TR / "1" / f"1_scan{n:03d}.tex" for n in list(range(78, 83)) + list(range(110, 114))})
for n, src in extra.items():
    if src.exists():
        put(src, out / n)
    else:
        print("MISSING", src)
PY = sys.executable
r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("pack:", (r.stdout.strip().splitlines() or ["?"])[-1])
pm = out / "PROMPT.md"
for args in (["claude_tools/push_rule_pro_prompts.py", "--lint-math"], ["claude_tools/paper_completeness_lint.py"]):
    a = subprocess.run([PY, "-I", "-B", str(D / args[0]), *args[1:], str(pm)], capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    print(args[0], "->", (a.stdout.strip().splitlines() or ["?"])[-1])
print(", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip")))
