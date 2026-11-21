"""Build Pro research prompt 36, CUE_GCT (21 Nov 2026, main session, Claude Opus 5.5 at effort max), at the user's word,
~01:1x UTC: "Yeah, go for it. Like some CUE stuff ... the real question is how does this then go through geometric
complexity theory? That's the thing that makes it interesting right now." The random-matrix side of RH (pair correlation,
Katz-Sarnak, moments, quantum chaos) and Hoza's NL = UL (ECCC TR26-323, derandomized isolation), through GCT.
Reuses the shared blocks of build_prompts_24_29.py (ALPOGE, MASULLO, how_to_work with the AG language paragraph).
usage: python -I -B build_prompt_36.py"""
import gzip, io, pathlib, shutil, subprocess, sys, tarfile, time, urllib.request, zipfile
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
MIDX = D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md"
ARX = {"LIT_Bump_Gamburd_averages_of_characteristic_polynomials": "math-ph/0502043",
       "LIT_CFKRS_integral_moments_of_L-functions": "math/0206018",
       "LIT_Hughes_Rudnick_low-lying_zeros_linear_statistics": "math/0208230",
       "LIT_representation_theory_approach_to_moments_function_fields": "1810.01303",
       "LIT_Forbes_Shpilka_explicit_Noether_normalization_matrix_invariants": "1303.0084",
       "LIT_AGKS_hitting_sets_ROABP_basis_isolation": "1406.7535"}


def fetch(aid):
    d = DL / aid.replace("/", "_")
    d.mkdir(parents=True, exist_ok=True)
    b = d / "src.bin"
    if not b.exists():
        req = urllib.request.Request("https://arxiv.org/e-print/" + aid, headers={"User-Agent": "arxiv-source-fetch/1.0"})
        b.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        time.sleep(3)
    out = d / "src"
    if not out.exists():
        out.mkdir()
        raw = b.read_bytes()
        try:
            raw = gzip.decompress(raw)
        except OSError:
            pass
        try:
            with tarfile.open(fileobj=io.BytesIO(raw)) as t:
                for m in t.getmembers():
                    if m.isfile() and m.name.lower().endswith((".tex", ".bbl", ".bib", ".sty", ".cls")):
                        p = out / pathlib.PurePosixPath(m.name).name
                        p.write_bytes(t.extractfile(m).read())
        except tarfile.ReadError:
            (out / "main.tex").write_bytes(raw)
    return out


PAR36 = ("This prompt is one of a set run in parallel on what the two proofs of 20 November (Alpöge's, cited as a theorem; "
         "Masullo's, a draft) make true. Prompts 24-28 treat P versus NP through geometric complexity theory: Mulmuley's "
         "nonstandard Riemann hypothesis, plethysm, Kronecker coefficients, Grothendieck's inequality, and the GRH and ETH "
         "results in complexity. This one treats the random-matrix side of the zeros, and derandomized isolation, through "
         "geometric complexity theory. Keep to this prompt's questions; the others are asked there.\n")

TEXT = f"""# CUE_GCT: the random-matrix side of the Riemann hypothesis, and derandomized isolation, through geometric complexity theory

{PAR36}
{ALPOGE}
{MASULLO}
## Where things stand

- **Pair correlation (the Montgomery-Odlyzko law).** Montgomery (1973) proved, assuming RH, that the pair correlation
  of the zeros of ζ agrees with that of random unitary (GUE/CUE) eigenvalues for test functions whose Fourier transform
  has support in (−1, 1). Dyson recognised the random-matrix form, and Odlyzko's computations support the full
  conjecture. With Alpöge's theorem, Montgomery's theorem holds unconditionally.
- **Quantum chaos.** Berry and Keating (H = xp), and the Bohigas-Giannoni-Schmit conjecture, read the zeros as the
  spectrum of a quantized chaotic system without time-reversal symmetry, hence GUE statistics. Cite these from your
  knowledge with locators, and mark what you take from memory.
- **Families (Katz-Sarnak).** The low-lying zeros of families of L-functions follow the statistics of U(N), USp(2g) or
  O(N).
  - Over function fields this is a theorem, through Deligne's equidistribution theorem (Weil II) and the monodromy
    groups of families.
  - Over number fields it is proved for restricted support under GRH: Hughes-Rudnick for Dirichlet families (attached),
    and Iwaniec-Luo-Sarnak for GL_2 families, which needs GRH beyond Dirichlet and Hecke L-functions.
- **Moments.**
  - Keating and Snaith predict the moments of ζ from the moments of characteristic polynomials over the CUE. The
    Conrey-Farmer-Keating-Rubinstein-Snaith recipe is attached.
  - Bump and Gamburd (attached) show that averages of products of characteristic polynomials over U(N) are characters of
    irreducible representations of U(2k) with rectangular highest weight (N^k). So the CUE moment constants are
    dimensions of rectangular GL_(2k)-representations.
  - A representation-theoretic approach to moments over function fields is attached.
- **Invariant theory.** By Molien-Weyl, the Hilbert series of a ring of invariants is a Haar integral over the compact
  group of 1/det(1 − tρ(k)). The characteristic polynomial of the Keating-Snaith moments is this Molien denominator.
- **Geometric complexity theory.**
  - Multiplicities in the coordinate rings of the orbit closures of the determinant and the padded permanent;
    rectangular Kronecker and plethysm coefficients (Ikenmeyer-Panova); Bürgisser-Ikenmeyer-Panova's theorem that
    occurrence obstructions do not suffice.
  - GCT IV, VII and VIII: nonstandard quantum groups and their positivity.
  - GCT V: derandomized polynomial identity testing against explicit Noether normalization.
  - Forbes-Shpilka (attached): explicit Noether normalization for the ring of matrix invariants in quasi-polynomial
    time, through hitting sets for read-once algebraic branching programs (ROABPs).
- **Derandomized isolation.**
  - Hoza, *NL = UL* (ECCC TR26-323, posted 20 November 2026, attached): an explicit min-isolating weight-assignment
    generator for width-w length-n layered digraphs, with seed length O(log(wn)). With Reinhardt-Allender (SICOMP
    2000), it gives NL = UL. It derandomizes the isolation lemma of Mulmuley-Vazirani-Vazirani for paths.
  - Agrawal-Gurjar-Korwar-Saxena (attached): basis-isolating weight assignments give quasi-polynomial hitting sets for
    ROABPs; polynomial-size hitting sets are open.
  - Kabanets-Impagliazzo: derandomizing general PIT forces circuit lower bounds (NEXP ⊄ P/poly, or the permanent needs
    super-polynomial arithmetic circuits).
- **Pseudorandomness from purity.** Weil's bound for curves gives small-bias sets (the quadratic-character
  construction of Alon-Goldreich-Håstad-Peralta) and algebraic-geometry codes. Deligne's Ramanujan bound gives the
  Lubotzky-Phillips-Sarnak expanders. Dirichlet GRH, now a theorem, gives deterministic quadratic non-residues and square
  roots mod p in polynomial time (Bach's bound 2 log² p). Prompt 28 treats that last point; cite it, do not redo it.

## The task

1. **The rectangular bridge.** Compare Bump-Gamburd's rectangular characters (and the CFKRS recipe, its sum over swaps)
   with the rectangular shapes of geometric complexity theory: the rectangular Kronecker and plethysm coefficients, and
   the multiplicities in the coordinate rings of the orbit closures of det_n and of the padded permanent. Determine what
   the moment identities give for those multiplicities: identities, positive formulas, bounds or obstructions. Prove
   what holds and refute what does not.
2. **Haar integrals.** Write the multiplicities geometric complexity theory needs as Haar integrals over compact groups
   (Molien-Weyl; Kronecker coefficients through U(n) × U(m) ⊂ U(nm); plethysm through powers, after Rains's theorem on
   the eigenvalues of U^k). Decide what the methods of random-matrix theory prove about them, positivity above all:
   Weingarten calculus, the ratios recipe, Gelfand-Tsetlin and RSK counts.
3. **Isolation through geometric complexity theory.** Decide whether Hoza's min-isolating generator extends to
   basis-isolating weight assignments for width-w ROABPs, giving polynomial-size hitting sets. If it does, derive
   polynomial-time explicit Noether normalization for matrix invariants (Forbes-Shpilka) and its consequences in GCT V.
   If it does not, give the obstruction. State isolating weights as one-parameter subgroups: Gröbner degenerations to an
   initial monomial, and open cones of the normal fan of a Newton polytope.
4. **Pseudorandomness from purity.** Decide whether equidistribution of Frobenius (Deligne; the monodromy groups of
   Katz-Sarnak) gives explicit isolating weight families or hitting sets for ROABPs, as Weil's bound gives small-bias
   sets. Say what Dirichlet GRH (Alpöge), and conditionally Masullo's claim, add over number fields.
5. **What is now unconditional.** List the random-matrix statements about zeros that were proved under RH or GRH,
   with the GRH each uses. Mark each as unconditional by Alpöge, conditional on Masullo only, or beyond both, naming the
   missing statement.

## The attached files

- `LIT_Bump_Gamburd_averages_of_characteristic_polynomials/`, `LIT_CFKRS_integral_moments_of_L-functions/`,
  `LIT_Hughes_Rudnick_low-lying_zeros_linear_statistics/`, `LIT_representation_theory_approach_to_moments_function_fields/`,
  `LIT_Forbes_Shpilka_explicit_Noether_normalization_matrix_invariants/`, `LIT_AGKS_hitting_sets_ROABP_basis_isolation/`:
  LaTeX sources (arXiv).
- `LIT_Mulmuley_GCT_V_Noether_normalization/`, `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/`,
  `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/`, `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/`,
  `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`, `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`,
  `LIT_Landsberg_GCT_introduction_for_geometers/`: LaTeX sources.
- `ECCC_TR26-323_Hoza_NL_equals_UL.pdf` (no source posted).
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`; `MASULLO_STATEMENTS_INDEX.md`.
- `ARCHIVE_133_*.tex`: Grothendieck's pages on λ-operations and plethysm (cote 133), with `SA17_STUDY_cote133_lambda.md`.

{how_to_work("what the random-matrix side of the zeros (Bump-Gamburd's rectangular characters, Haar integrals and the moment recipes) proves about the rectangular Kronecker and plethysm multiplicities of geometric complexity theory, and whether Hoza's isolation generator gives polynomial-size hitting sets for ROABPs.", "CUE_GCT")}"""
TEXT = TEXT.replace("4. **`IMPLICATIONS.md`**", "5. **`TRANSCRIPTION_NOTES.tsv`**: every place where the mathematics shows that our text of record of cote 133 misreads\n   Grothendieck's page: cote, scan, line, our reading, the reading required, the reason, how sure you are.\n4. **`IMPLICATIONS.md`**", 1)

out = Q / "36_CUE_GCT_random_matrices_and_isolation_through_GCT"
assert not out.exists(), out
out.mkdir(parents=True)
(out / "PROMPT.md").write_text(TEXT, encoding="utf-8")


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst))


for n, aid in ARX.items():
    put(fetch(aid), out / n)
for n in ["LIT_Mulmuley_GCT_V_Noether_normalization", "LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm",
          "LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions", "LIT_Landsberg_GCT_introduction_for_geometers",
          "ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "SA17_STUDY_cote133_lambda.md"]:
    put(F23 / n, out / n)
for f in sorted(F23.glob("ARCHIVE_133_*.tex")):
    put(f, out / f.name)
for n, src in {"LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker": DL / "cs_0703110/src",
               "LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm": DL / "0709.0749/src",
               "LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups": DL / "0709.0751/src",
               "ECCC_TR26-323_Hoza_NL_equals_UL.pdf": D / "recent_results_20261110/papers/ECCC_TR26-323_Hoza_NL_equals_UL.pdf",
               "MASULLO_STATEMENTS_INDEX.md": MIDX}.items():
    if src.exists():
        put(src, out / n)
    else:
        print("MISSING", src)
for sub in sorted(p for p in out.iterdir() if p.is_dir()):
    with zipfile.ZipFile(out / (sub.name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(sub.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(sub).as_posix())
    shutil.rmtree(sub)
PY = sys.executable
r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("pack:", (r.stdout.strip().splitlines() or ["?"])[-1], r.stderr.strip()[-300:])
pm = out / "PROMPT.md"
for args in (["claude_tools/push_rule_pro_prompts.py", "--lint-math"], ["claude_tools/paper_completeness_lint.py"]):
    a = subprocess.run([PY, "-I", "-B", str(D / args[0]), *args[1:], str(pm)], capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    print(args[0], "->", (a.stdout.strip().splitlines() or ["?"])[-1])
    if "failing lint: 0" not in a.stdout and "failing: 0" not in a.stdout:
        print(a.stdout[-2000:])
print(", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip")))
