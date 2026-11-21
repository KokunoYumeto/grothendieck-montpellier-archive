"""Build Pro research prompts 37-41, the Hodge line (21 Nov 2026, main session, Claude Opus 5.5 at effort max): the top
five of the ranked list in reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md §7, written by our Claude Fable
5.2 (effort max) expert. The user, 21 Nov: "Ranks the prompts it suggests. It did not read Masullo, Milne's report,
Markman"; "they are related, show how, and then see what we can do to use these new results to attack the problem."
Adds the sources the expert lacked: Milne's report (Hexagon 2611.00244v1), van Hoften-Sempliner (Hexagon 2610.00259v2),
Markman (arXiv 2502.03415), and Masullo's statements index.
usage: python -I -B build_prompts_37_41.py"""
import pathlib, re, shutil, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
TR = D / "grothendieck_archive_transcription_20261110/text_of_record/pages"
HS = D / "recent_results_20261110/papers/hodge_sources_20261121"
PK = D / "recent_results_20261110/proof_packs/032_The-rational-Hodge-conjecture-for-CM-abe"
SK = D / "reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md"
MIDX = D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md"
F22 = S / "from_22"

AG_LANG = """## The language of the results

State every finding in the language of algebraic geometry and of Grothendieck's frameworks: motives and correspondences,
algebraic cycles modulo homological and numerical equivalence, the standard conjectures, Hodge and ℓ-adic realizations,
Shimura varieties and their integral models, Hecke correspondences. For each finding, say where it lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator.

"""
IMPL = ("4. **`IMPLICATIONS.md`**: what the findings change: for the Hodge, Tate and standard conjectures; for Grothendieck's\n"
        "   texts by cote and scan; for the open rows of our runs (run and statement id).\n"
        "5. **`TRANSCRIPTION_NOTES.tsv`**: every place where the mathematics shows that our text of record misreads\n"
        "   Grothendieck's page: cote, scan, line, our reading, the reading required, the reason, how sure you are.")


def hw(main_q, short):
    t = how_to_work(main_q, short).replace(LANG_PARAGRAPH, AG_LANG)
    t, n = re.subn(r"4\. \*\*`IMPLICATIONS\.md`\*\*:.*?\(cote and scan\)\.", lambda m: IMPL, t, flags=re.S)
    assert n == 1, "template changed"
    return t


FRAME = """These links are real, and none of them is a mere corollary, or it would already be known. So the task is not to ask
whether they hold. It is to show exactly how they work, and then to use the new results to attack the open problem. Where
a route meets an obstacle, locate it exactly and attack it with the next tool the new results give. An obstacle is never
an end point.
"""
PAR = ("This prompt is one of five run in parallel on 21 November 2026 on the Hodge conjecture after the two GRH proofs "
       "of 20 November and OpenAI's proof of Hodge for CM abelian varieties. Statement labels (1.7, 2.1-2.5, T3-T9, 3.3-3.5, "
       "H8, H9) are those of the attached `HODGE_BRIDGE_SKETCH_20261121.md`, by our Claude Fable 5.2 (effort max) expert. "
       "The sketch is unchecked: use it as a map, never as a result. The others treat: the theta machine in three "
       "signatures (37), bounded division on Hecke orbits (38), ghost classes at primes (39), Grothendieck's 1964 "
       "Jacobians programme of cote 44 (40), degrees of cycles as L-values (41). Keep to this prompt's questions.\n")
HODGE = """## The Hodge results cited

- **OpenAI family 032:** the rational Hodge conjecture for every complex CM abelian variety, in every dimension and
  codimension, with a Lean statement. Attached as `OPENAI_032_*.pdf`, with its companion papers.
- **van Hoften-Sempliner:** a human proof following that work, *The Hodge Conjecture for CM abelian varieties* (Hexagon
  2610.00259v2). Attached.
- **Milne:** *On the Hodge, Tate, and standard conjectures for abelian varieties* (Hexagon 2611.00244v1). It derives the
  Tate conjecture for abelian varieties over finite fields and the Hodge standard conjecture for all abelian varieties.
  Attached.
- **Markman:** the Hodge conjecture for abelian fourfolds of Weil type (arXiv 2502.03415). LaTeX attached.
"""
COMMON = ["ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "ALPOGE_LEAN_SCAN.tsv"]


def files_common(extra):
    d = {"HODGE_BRIDGE_SKETCH_20261121.md": SK,
         "OPENAI_032_The-rational-Hodge-conjecture-for-CM-abelian-varieties.pdf": PK / "032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf",
         "OPENAI_032_Weil-classes-and-Hodge-classes-on-abelian-powers.pdf": PK / "032_Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026.pdf",
         "HEXAGON_2610.00259v2_vanHoften_Sempliner.pdf": HS / "Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf",
         "HEXAGON_2611.00244v1_Milne_report.pdf": HS / "Hexagon_2611.00244v1_Milne_report.pdf",
         "LIT_Markman_Hodge_abelian_fourfolds_2502.03415": HS / "LIT_Markman_Hodge_abelian_fourfolds_2502.03415",
         "ALPOGE_LEAN_MAP_20261120.md": AR / "ALPOGE_LEAN_MAP_20261120.md",
         "MASULLO_STATEMENTS_INDEX.md": MIDX}
    d.update(extra)
    return d


def arch_all(cote):
    return {f"ARCHIVE_{f.name}": f for f in sorted((TR / str(cote)).glob("*.tex"))}


P = {}
P["37_HODGE_THETA_three_signatures"] = ("THETA3", f"""# THETA3: one theta machine in three signatures: Alpöge's definite lifts, the cycles of 032, and the integral models

{PAR}
{ALPOGE}
{MASULLO}
{HODGE}
## The question

Our expert found that the proof of Hodge for CM abelian varieties (032) and Alpöge's proof run on the same machine: theta
lifts of Hecke characters of a CM field to unitary groups.
- 032 works at signature (n,1), on ball quotients, where a lift is a cycle.
- Alpöge works at totally definite signature, where a lift gives periods and a positive determinant.
- The sketch's Route 1 adds the integral models as a third setting.

{FRAME}
## The task

1. **The machine, exactly.** Set 032 §§4-6 beside the theta-lift statements of Alpöge's archive (paths in
   `ALPOGE_LEAN_MAP_20261120.md`). Write the dictionary: the Hecke characters, the unitary groups and their signatures,
   the seesaw pairs, the Rallis inner product, the non-vanishing statements. Prove the sketch's 1.7.
2. **An explicit non-vanishing.** Give 032's non-vanishing of the relevant theta lifts an explicit lower bound, by
   bringing in Alpöge's definite-signature positivity (steps 4, 7 and 8: determinants, interlacing periods,
   multiplicity won lift by lift).
3. **Beyond CM.** Use the machine at signature (n,1) for Hodge classes whose source is not CM. Push it as far as it goes.
4. **Integral models.** Carry the comparison to the integral models (Kudla-Rapoport type) where the sketch's Route 1
   points.

## The attached files

- `HODGE_BRIDGE_SKETCH_20261121.md` (Route 1, 1.6, 1.7).
- `OPENAI_032_*.pdf`, `HEXAGON_*.pdf`, `LIT_Markman_*/`.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `MASULLO_STATEMENTS_INDEX.md`.

{hw("the exact dictionary between 032's theta lifts at signature (n,1) and Alpöge's at definite signature (1.7), and its use to give 032's non-vanishing an explicit lower bound and to reach Hodge classes with non-CM sources.", "THETA3")}""",
    COMMON, files_common({}))

P["38_HODGE_HECKE_DIVISION_bounded_division_on_Hecke_orbits"] = ("HECKE_DIV", f"""# HECKE_DIV: from CM to every abelian variety: bounded division on Hecke orbits

{PAR}
{ALPOGE}
{MASULLO}
{HODGE}
## The question

Our expert reduced the passage from CM abelian varieties (032) to every abelian variety to one gate: bounded division.
Hodge holds on a special family exactly when the Hodge classes along the Hecke orbit of one CM point have algebraic
representatives of bounded degree and bounded denominator. Equivalently, their complexity stays bounded over the primes.
032's Remark 8.5 already gives algebraicity modulo every good prime.

{FRAME}
## The task

1. **The reduction.** Prove the sketch's 2.1-2.4 in full.
2. **The first case.** Carry out the sketch's T5 on the fourfolds isogenous to E^4, with E = ℂ/ℤ[ω], from Markman's
   construction (attached). Compute the degrees and denominators along the Hecke orbit.
3. **The main question.** Attack bounded division on the Hecke orbit of E^8. Bring in what the new results give on the
   arithmetic of Hecke orbits:
   - equidistribution of Hecke orbits, effective under GRH: Alpöge for Dirichlet characters, Masullo's claim, marked
     conditional, for Hecke characters;
   - Faltings heights of CM points by Colmez's formula, with L'/L of Hecke characters;
   - the positivity of Alpöge's step 5.
4. Wherever the bound is reached, state what follows for the Hodge conjecture on that family.

## The attached files

- `HODGE_BRIDGE_SKETCH_20261121.md` (Route 2, 2.1-2.5, T5).
- `OPENAI_032_*.pdf` (Remark 8.5), `HEXAGON_*.pdf` (Milne's report on Tate and the standard conjectures),
  `LIT_Markman_Hodge_abelian_fourfolds_2502.03415/`.
- `ALPOGE_remark.pdf`, Lean files, `MASULLO_STATEMENTS_INDEX.md`.

{hw("bounded division on the Hecke orbit of E^8 (E = ℂ/ℤ[ω]): the degrees and denominators of algebraic representatives of the Hodge classes along the orbit, attacked with Markman's construction, effective equidistribution under the two GRH results, and Colmez's heights.", "HECKE_DIV")}""",
    COMMON, files_common({}))

P["39_HODGE_GHOST_CLASSES_at_supersingular_and_ordinary_primes"] = ("GHOSTS", f"""# GHOSTS: Hodge classes as ghosts: algebraic at every good prime, and the least complexity of their representatives

{PAR}
{ALPOGE}
{HODGE}
## The question

A ghost is a class that passes every local test (here: algebraic modulo every good prime, by 032's Remark 8.5 and its
CM transport) and whose global status is the question. Our expert proposes to measure, prime by prime, the least
complexity of the representative t_v, at supersingular and at ordinary primes. That measure is how the local algebraicity
of Remark 8.5 becomes the bounded-division gate of Route 2.

{FRAME}
## The task

1. Prove the sketch's 2.5.
2. Check 032's Remark 8.5 with its CM transport.
3. Carry out T9.
4. For the Weil class of the sketch's T5, compute the least complexity of t_v at supersingular and at ordinary primes,
   as a function of v.
5. Use the arithmetic the new results give (the effective distribution of supersingular and ordinary primes in the
   relevant families, under the two GRH results) to bound that complexity uniformly. Then carry the bound to Route 2's
   gate.

## The attached files

- `HODGE_BRIDGE_SKETCH_20261121.md` (2.5, T5, T9).
- `OPENAI_032_*.pdf`, `HEXAGON_*.pdf`, `LIT_Markman_*/`.
- `ALPOGE_remark.pdf`, Lean files, `MASULLO_STATEMENTS_INDEX.md`.

{hw("the least complexity of the representatives t_v of the Weil class of T5 at supersingular and ordinary primes as a function of v, bounded uniformly, and carried to the bounded-division gate.", "GHOSTS")}""",
    COMMON, files_common({}))

P["40_HODGE_JACOBIANS_1964_cote_44_every_characteristic"] = ("JAC1964", f"""# JAC1964: Grothendieck's 1964 programme on Jacobians (cote 44) after 032: Th. 4 in every characteristic, H9, and the arithmetic sibling

{PAR}
{ALPOGE}
{HODGE}
## The question

Cote 44 (1964) is Grothendieck's programme of seven theorems on intermediate Jacobians, with a height formula. Our
expert sketches the following, via 032's Cor. 8.4:
- Th. 4 holds for abelian varieties in every characteristic (the sketch's 3.4);
- an arithmetic sibling with a sign set against Th. 5 (3.5);
- hunch H9 reads Th. 5 as the Mordell-Weil lattice formula in codimension m, for the Beilinson-Bloch height.

Cote 16, the ring of correspondences, carries the positivity: no. 7, scans 34-40 and 49-50.

{FRAME}
## The task

1. Prove 3.4: Th. 4 of cote 44 for abelian varieties in every characteristic.
2. Prove H9 (a) and (b) (the hunches file is attached).
3. Prove 3.5, the arithmetic sibling with its sign against Th. 5. Use Alpöge's sign-only positivity (step 5) and the
   Bost slope inequality (step 13) where they bear.
4. Say which of the seven theorems of cote 44 are now proved, for which varieties and in which characteristics, and
   attack the next one.

## The attached files

- The pages of cote 44 (`ARCHIVE_44_*.tex`) and cote 16 (`ARCHIVE_16_*.tex`).
- `WARGAME_MATH_HUNCHES_20261112.md` (H8, H9); `HODGE_BRIDGE_SKETCH_20261121.md` (Route 3, 3.3-3.5).
- `OPENAI_032_*.pdf` (Cor. 8.4), `HEXAGON_*.pdf`, `LIT_Markman_*/`.
- `ALPOGE_remark.pdf`, Lean files.

{hw("Th. 4 of cote 44 for abelian varieties in every characteristic (3.4), with H9 (a), (b), and then the arithmetic sibling 3.5 with its sign against Th. 5.", "JAC1964")}""",
    COMMON, files_common({**arch_all(44), **arch_all(16),
                          "WARGAME_MATH_HUNCHES_20261112.md": D / "grothendieck_archive_montpellier/WARGAME_MATH_HUNCHES_20261112.md"}))

P["41_HODGE_DEGREES_ARE_L_VALUES_Rallis_and_semiregularity"] = ("DEG_L", f"""# DEG_L: the degrees of the 032 cycles as L-values (Rallis), and the semiregularity of the 032 surface

{PAR}
{ALPOGE}
{MASULLO}
{HODGE}
## The question

The cycles of 032 are theta lifts. By the Rallis inner product formula, their self-intersections and degrees are special
values of L-functions of Hecke characters. That is where the two GRH proofs meet the Hodge conjecture directly: the size
of those L-values controls the degrees, and with them the bounded-division gate of the sketch's Route 2. Semiregularity
of the 032 surface (T7) is what lets the cycles deform along families.

{FRAME}
## The task

1. Prove the sketch's T6: the degree of the 032 cycle by the Rallis inner product formula, as an explicit L-value.
2. Bound those degrees, and their variation along Hecke orbits, with the new results. Mark what is unconditional by
   Alpöge (Dirichlet), what is conditional on Masullo (Hecke), and what needs more.
3. Prove T7: the semiregularity of the 032 surface. Use it to deform the cycles along the special families of Route 2.
4. Carry 2 and 3 to bounded division (Route 2) wherever they reach it.

## The attached files

- `HODGE_BRIDGE_SKETCH_20261121.md` (T6, T7, Route 2).
- `OPENAI_032_*.pdf`, `HEXAGON_*.pdf`, `LIT_Markman_*/`.
- `ALPOGE_remark.pdf`, Lean files, `ALPOGE_LEAN_MAP_20261120.md`, `MASULLO_STATEMENTS_INDEX.md`.

{hw("the degree of the 032 cycles as an explicit L-value by the Rallis inner product formula, bounded with the two GRH results along Hecke orbits, together with the semiregularity of the 032 surface, carried to bounded division.", "DEG_L")}""",
    COMMON, files_common({}))


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst))


built = []
for name, (short, text, from22, extra) in P.items():
    out = Q / name
    if out.exists():
        print("EXISTS, skipped:", out); continue
    out.mkdir(parents=True)
    (out / "PROMPT.md").write_text(text, encoding="utf-8")
    for n in from22:
        put(F22 / n, out / n)
    for n, src in extra.items():
        if not src.exists():
            print("MISSING", src); continue
        put(src, out / n)
    for sub in sorted(p for p in out.iterdir() if p.is_dir()):
        with zipfile.ZipFile(out / (sub.name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(sub.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(sub).as_posix())
        shutil.rmtree(sub)
    built.append(out)
PY = sys.executable
for out in built:
    r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    pm = out / "PROMPT.md"
    a = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/push_rule_pro_prompts.py"), "--lint-math", str(pm)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace").stdout.strip().splitlines()
    b = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/paper_completeness_lint.py"), str(pm)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace").stdout.strip().splitlines()
    zs = ", ".join(f"{z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip"))
    print(f"{out.name}: math {a[-1] if a else '?'} | paper {b[-1] if b else '?'} | ZIP {zs}")
