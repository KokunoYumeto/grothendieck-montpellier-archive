"""Build Pro research prompts 43-45 (21 Nov 2026, main session e0d20ada, Claude Opus 5.5 at effort max): the successors
of the three runs of 20-21 Nov that returned finals and have been taken in, from each intake's section 6 ("Prompt
updates"): 43 ZETA_NEXT (successor of 35 ZETA_TWO), 44 BR_PENCIL (of 27 GCT_GINEQ), 45 SIGN_NEXT (of 32 HODGE_SIGN).
The user, 21 Nov ~02:4x UTC: "were there no new prompts? ... I'm seeing no prompts in Pro at all after the one that were
already sent 2 hours ago." CX_GRH (28) gets no successor here: the night prompt 42 (GRH_NIGHT) catalogues the same
consequences.
usage: python -I -B build_prompts_43_45.py"""
import pathlib, re, shutil, subprocess, sys, zipfile, gzip, io, tarfile, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
RR = D / "grothendieck_archive_transcription_20261110/research_returns"
INT = D / "field_experts/intake_20261121/intakes"
SENT = Q / "SENT"
NAME_RE = re.compile(r"^(?P<run>.+?)_(?:checkpoint_(?P<cp>\d+)|final(?:_INCOMPLETE)?)_(?P<ts>\d{8}T\d{4}Z)(?:_unzipped)?$")
DL2 = S / "dl_43_45"

AG_LANG = """## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

"""
IMPL = ("4. **`IMPLICATIONS.md`**: what the findings change: for our programme on Grothendieck's work (cote and scan),\n"
        "   for our runs' open rows (run and statement id), and for the open conjectures named in the task.")


def hw(main_q, short, ag=True):
    t = how_to_work(main_q, short)
    if ag:
        t = t.replace(LANG_PARAGRAPH, AG_LANG)
        t, n = re.subn(r"4\. \*\*`IMPLICATIONS\.md`\*\*:.*?\(cote and scan\)\.", lambda m: IMPL, t, flags=re.S)
        assert n == 1, "template changed"
    return t


def newest(tag):
    best = None
    for d in RR.iterdir():
        m = NAME_RE.match(d.name) if d.is_dir() else None
        if m and m.group("run") == tag:
            key = (1, m.group("ts")) if m.group("cp") is None else (0, int(m.group("cp")))
            if best is None or key > best[0]:
                best = (key, d)
    return best[1]


def arxiv_tex(aid, folder):
    """the arXiv e-print (LaTeX) of aid, unpacked into DL2/folder; returns the folder"""
    out = DL2 / folder
    if out.exists():
        return out
    out.mkdir(parents=True)
    req = urllib.request.Request(f"https://arxiv.org/e-print/{aid}", headers={"User-Agent": "Mozilla/5.0 (research client)"})
    data = urllib.request.urlopen(req, timeout=60).read()
    try:
        with tarfile.open(fileobj=io.BytesIO(data)) as tf:
            for m in tf.getmembers():
                if m.isfile() and not m.name.startswith(("/", "..")) and ".." not in m.name:
                    if m.name.lower().endswith((".tex", ".bbl", ".bib", ".sty", ".cls")):
                        tf.extract(m, out)
    except tarfile.ReadError:
        (out / "main.tex").write_bytes(gzip.decompress(data))
    return out


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst))


def from_previous_zip(nn, out):
    """the attachments of the predecessor prompt, as sent"""
    prev = next(SENT.glob(f"{nn}_*"))
    put(prev / "PROMPT.md", out / f"PREVIOUS_PROMPT_{nn}.md")
    for z in prev.glob("*.zip"):
        with zipfile.ZipFile(z) as zf:
            for n in zf.namelist():
                if not n.endswith("/") and ".." not in n:
                    p = out / n
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes(zf.read(n))


def return_files(tag, out, names):
    d = newest(tag)
    lab = d.name.replace("_unzipped", "")
    for n in names:
        hits = list(d.glob(n)) or list(d.glob("*/" + n))
        for h in hits[:1]:
            put(h, out / f"RETURN_{lab}" / h.name)
    return lab


P = {}

# ---------------------------------------------------------------------------------------------------------------- 43
P["43_ZETA_NEXT_effective_class_numbers_Lambda_schemes_and_the_non-CM_gate"] = ("ZETA_NEXT", f"""# ZETA_NEXT: effective class numbers from Alpöge's theorem, the bad fibres of Λ-schemes, and the non-CM gate

This prompt continues ZETA_TWO (our prompt 35). Its return (`RETURN_ZETA_TWO_final_*`) and our intake of it
(`INTAKE_ZETA_TWO_20261121.md`) are attached. Build on them and cite them by statement id. Do not redo what they settled:
the dependency tables of what needs Alpöge's theorem and what needs Masullo's are in `CONDITIONAL_AUDIT.tsv`, and
ZETA_TWO's IA01 audit stands.

{ALPOGE}
{MASULLO}
## The task

1. **Main question: effective Brauer-Siegel for normal fields from Alpöge's theorem, and what it makes effective.**
   Stark (Invent. Math. 23 (1974); the locators Lemma 8 and Theorem 1′ are to be checked) places every exceptional zero
   of the Dedekind zeta function of a normal number field K in the zeta function of a quadratic subfield, so in a
   quadratic Dirichlet L-function, where Alpöge's theorem excludes it. Our intake confirmed this reduction (ZETA_TWO
   IA05) at the level of its logic; its constants were read only at statement level.
   - State and prove the resulting effective lower bound for h_K R_K for every normal K, with explicit constants, and
     carry it through the Galois closure to CM fields of fixed degree.
   - Then decide which known proofs become effective with it: the Galois-orbit lower bounds for CM points in A_g
     (Tsimerman's proof of André-Oort with the averaged Colmez formula), and the Siegel-type class-number bounds for CM
     fields. For each, give the effective statement with its constants and its proof, or locate the step that stays
     ineffective and attack it.
2. **The bad fibres of Λ-schemes.** ZETA_TWO's ZT05 shows that ζ of Spec Z[1/p], which is a Λ-scheme, has the zeros
   2πik/log p on Re s = 0. So a Riemann hypothesis for Λ-schemes can only say that all non-real zeros and poles lie on
   the lines Re s ∈ ½Z. The conjecture to decide: for a Λ-scheme X, flat and of finite type over Z, every bad-fibre
   factor of the finite factor R_{{X,S}} of ZETA_TWO's ZT04 is a product of factors (1 − ζ p^{{j−s}})^{{±1}}, with ζ a root
   of unity and j ∈ Z. It holds for Spec Z[1/n], for the rings of integers of abelian fields and their localizations,
   and for split tori.
   - Prove it or refute it with a counterexample. Borger's Frobenius lifts at the bad prime p (ψ_p lifts the absolute
     Frobenius of the fibre X_p) are the tool to try first. DP_MULT's DP11 gives the criterion for a ring to be a
     Λ-ring (binomial rings).
   - For a proper flat Λ-scheme, decide whether Borger's splitting of the cohomology holds for RΓ_c(X_{{F̄_p}}) at the bad
     primes as well.
3. **The non-CM gate.** For X a curve or an abelian variety over Q, compute ZETA_TWO's ZT06 list exactly, using
   Faltings' semisimplicity, and name the non-CM L-functions on which the Riemann hypothesis for ζ_X then waits. Close
   ZT06's gap, the splitting of H^j into CM and non-CM summands, in every case where Faltings' theorems and Deligne's
   absolute Hodge cycles give it.

The links between these questions and the two proofs are real. Where a route meets an obstacle, locate it exactly and
take the next route; an obstacle is never an end point.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_35.md` and its attachments (Alpöge's note and Lean files, our bridges files, our
  intakes of 20 Nov, Deligne-Goncharov's LaTeX, Masullo's draft and our index of its statements).
- `RETURN_ZETA_TWO_final_*/`: the run's paper, registers and audits. `INTAKE_ZETA_TWO_20261121.md` with its check
  events.
- `RETURN_DP_MULT_*/`: the paper of the divided-powers run (DP11), with our intakes of it.
- `LIT_Borger_Lambda_rings_and_the_field_with_one_element/`: Borger, arXiv:0906.3146, LaTeX.

{hw("the effective Brauer-Siegel bound for normal fields from Alpöge's theorem with Stark's reduction, with explicit constants, and its consequences for CM points and class numbers.", "ZETA_NEXT")}""")

# ---------------------------------------------------------------------------------------------------------------- 44
P["44_BR_PENCIL_border_rank_of_det4_and_per4_by_multi-dimensional_substitution"] = ("BR_PENCIL", f"""# BR_PENCIL: border rank of the 4×4 determinant and permanent by substitution of more than one dimension

This prompt continues GCT_GINEQ (our prompt 27). Its return (`RETURN_GCT_GINEQ_final_*`) and our intake of it are
attached; cite them by finding id.

**Where it stands.** GCT_GINEQ proved, without norms (its F-23): the minimum over 0 ≠ u ∈ U_{{n,b}} of the border rank of
the residual u equals BR(T_b), hence BR(T_n) ≥ C(n,b)^s + BR(T_b) − 1, and this gives border rank ≥ 39 for the 4×4
determinant and permanent. Our intake confirmed all 23 findings with full proofs, and the run's scripts pass on rerun.
A literature check on 21 Nov 2026 (in `INTAKE_GCT_KRON_cp03_20261121.md`) found no published lower bound of 39 or more
for either polynomial: Farnsworth's 38 is for the symmetric border rank of the determinant (arXiv:1505.05079), the
catalecticant bound gives 36 for the permanent, and Landsberg-Teitler's 40 bounds the rank, not the border rank
(arXiv:0901.0487).

## The task

1. **Main question: substitution of more than one dimension (the intake's 5.1b) on the four families.** Determine the
   minimum, over the Grassmannian Gr(j, U_{{n,b}}), of the border rank of the residual pencil, through Koszul flattenings
   of the pencil, with an exact computation at n = 4, b = 2, j = 2. The aim is a lower bound above 39 for det_4 and
   per_4. Prove every bound you obtain, with its certificate.
2. **The SDP question.** Certify α(U) by the DPS hierarchy, with proved error bounds, for one residual image outside the
   four families (GCT_GINEQ's open row Q-30).
3. **Fields.** State and prove F-23 over every algebraically closed field, using F-18 (properness) and F-22 (the integral
   catalecticant).
4. **Orbits.** Treat the orbit-invariant version of α (the maximum over the GL orbit, through Kempf-Ness) against F-19.
5. **Literature.** Before any bound is called new, check it against the bounds on the border rank of det_n and per_n
   after Farnsworth (2015), and against Conner-Harper-Landsberg's border apolarity.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_27.md` and its attachments (Bürgisser-Ikenmeyer-Panova, Friedland-Lim, Landsberg's
  introduction to GCT, Pisier on Grothendieck's theorem, as LaTeX).
- `RETURN_GCT_GINEQ_final_*/`: the run's paper, registers, checks and scripts. `INTAKE_GCT_GINEQ_20261121.md` and
  `INTAKE_GCT_KRON_cp03_20261121.md`, with their check events.
- `LIT_Farnsworth_Koszul_Young_flattenings_det/` (arXiv:1505.05079) and `LIT_Landsberg_Teitler_ranks_of_polynomials/`
  (arXiv:0901.0487), as LaTeX.

{hw("a lower bound above 39 for the border rank of det_4 and per_4, by substitution of a subspace of dimension j > 1 in F-23 through Koszul flattenings of the residual pencil, with the computation at n = 4, b = 2, j = 2.", "BR_PENCIL", ag=False)}""")

# ---------------------------------------------------------------------------------------------------------------- 45
P["45_SIGN_NEXT_Grothendiecks_Hodge-index_route_after_the_sign-only_proof"] = ("SIGN_NEXT", f"""# SIGN_NEXT: Grothendieck's Hodge-index route after the sign-only proof of purity

This prompt continues HODGE_SIGN (our prompt 32). Its return (`RETURN_HODGE_SIGN_final_*`), our intake of it, and an
independent check of its proof are attached.

**What is settled.** HODGE_SIGN's SG-08 to SG-11 prove Deligne's purity theorem (Weil I, Théorème 1.6, and Weil II,
Théorème 3.3.1 over a point) by the sign-only route of Alpöge's footnote 3, without monodromy. The proof was checked
twice: by Claude Opus 5.5 at effort high, and independently by Claude Fable 5.2 at effort max, who re-proved every step and
took the generic weak Lefschetz input from Deligne's proof in the appendix of Katz's paper (A.3-A.5) instead of the
printed proof of Katz's Corollary 3.4.1 (`CHECK_a3ccbc11_20261121.md`). Cite SG-08 to SG-11, with GCT_NSRH's F03, as the
sign-only theorem; do not prove them again.

{ALPOGE}
## The task

1. **Main question: the next step of Grothendieck's Hodge-index route.** With purity proved without weights,
   Grothendieck's route in cote 16 (scans 049-050) needs his conjectures C(X) and I(X×X).
   - Attack his Proposition on scan 050: A(X) ⟺ C(Y) + A′(X×X)⁰ + A″(X×X)⁰. Where the critical-degree conditions hold
     (abelian varieties, through 032's Corollary 8.4; powers of CM elliptic curves, through SG-04), derive C and I.
   - Decide whether the sign-only identity, applied to X×X with correspondences as coefficients, gives Grothendieck's
     semisimplicity statement (scan 049). State exactly what positivity it would need, and prove what can be proved.
2. **Q2c (U-02).** It is closed by 032 (the rational Hodge conjecture for CM abelian varieties: OpenAI's result of
   6 Oct 2026, with a human proof by van Hoften and Sempliner, Hexagon 2610.00259) together with Milne 2002, Theorem 3.3.
   State it so, with the exact locators.
3. **Q6g (U-04, U-05).** HODGE_SIGN stopped at a gate here. Attack: the integral intertwiner, by the Fock model; the
   indices on the actual exterior model; and a test against the step-10 data with m = 2. A gate that depends on data not
   supplied is an item to construct, not a reason to deliver.
4. **Cote 44.** HODGE_SIGN's AR-01 refutes Theorem 5 of cote 44 (scan 004) as displayed: on P²×P², with
   Z = a² − ab + b² and the pencil diag(λ, λ+μ, λ+2μ), the generic member is the flag threefold, Z restricts to 0 there,
   and Z² = 3a²b². Prove the corrected Theorem 5, with the correction from the singular fibres when E = 0, and compute
   the contribution of each nodal fibre in this example.

The archive files are cited by their file names, which are our scan numbers.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_32.md` and its attachments (Alpöge's note and Lean files, cote 16, 34 and 44 scans,
  our bridges files, Fable's suggestions, the war-game hunches).
- `RETURN_HODGE_SIGN_final_*/`: the run's paper and registers. `INTAKE_HODGE_SIGN_20261121.md`, with its check events.
  `CHECK_a3ccbc11_20261121.md`, the independent check.
- `INTAKE_THETA3_20261121.md` and `INTAKE_HECKE_DIV_20261121.md`: our intakes of prompts 37 and 38 (the Fock model and
  bounded division).
- `032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf`, the van Hoften-Sempliner deposit
  (Hexagon 2610.00259) and Milne's report (Hexagon 2611.00244).

{hw("the next step of Grothendieck's Hodge-index route in cote 16: his Proposition on scan 050, and C and I where the critical-degree conditions hold.", "SIGN_NEXT")}""")

# ------------------------------------------------------------------------------------------------------- attachments
EXTRA = {
    "ZETA_NEXT": lambda out: (
        from_previous_zip("35", out),
        return_files("ZETA_TWO", out, ["ZETA_TWO.tex", "QUESTIONS.tsv", "LEDGER.md", "IMPLICATIONS.md", "CHECK_EVENTS.tsv",
                                       "CONDITIONAL_AUDIT.tsv", "TRANSCRIPTION_NOTES.tsv"]),
        return_files("DP_MULT", out, ["*.tex", "QUESTIONS.tsv", "LEDGER.md"]),
        [put(f, out / f.name) for f in sorted((INT / "ZETA_TWO").glob("INTAKE_*")) + sorted((INT / "DP_MULT").glob("INTAKE_*"))],
        put(arxiv_tex("0906.3146", "Borger"), out / "LIT_Borger_Lambda_rings_and_the_field_with_one_element")),
    "BR_PENCIL": lambda out: (
        from_previous_zip("27", out),
        put(newest("GCT_GINEQ"), out / ("RETURN_" + newest("GCT_GINEQ").name.replace("_unzipped", ""))),
        [put(f, out / f.name) for f in sorted((INT / "GCT_GINEQ").glob("INTAKE_*")) + sorted((INT / "GCT_KRON").glob("INTAKE_GCT_KRON_cp03*"))],
        put(arxiv_tex("1505.05079", "Farnsworth"), out / "LIT_Farnsworth_Koszul_Young_flattenings_det"),
        put(arxiv_tex("0901.0487", "LandsbergTeitler"), out / "LIT_Landsberg_Teitler_ranks_of_polynomials")),
    "SIGN_NEXT": lambda out: (
        from_previous_zip("32", out),
        return_files("HODGE_SIGN", out, ["HODGE_SIGN.tex", "QUESTIONS.tsv", "LEDGER.md", "IMPLICATIONS.md", "CHECK_EVENTS.tsv",
                                         "TRANSCRIPTION_NOTES.tsv", "SOURCE_CORRECTIONS.tsv", "VERIFICATION.md"]),
        [put(f, out / f.name) for f in sorted((INT / "HODGE_SIGN").glob("INTAKE_*")) + sorted((INT / "THETA3").glob("INTAKE_*"))
         + sorted((INT / "HECKE_DIV").glob("INTAKE_*"))],
        put(D / "reports_20261120/deligne_sign_only_check/CHECK_a3ccbc11_20261121.md", out / "CHECK_a3ccbc11_20261121.md"),
        put(D / "recent_results_20261110/papers/032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf",
            out / "032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf"),
        put(D / "recent_results_20261110/papers/hodge_sources_20261121/Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf",
            out / "Hexagon_2610.00259v2_vanHoften_Sempliner_CM_Hodge.pdf"),
        put(D / "recent_results_20261110/papers/hodge_sources_20261121/Hexagon_2611.00244v1_Milne_report.pdf",
            out / "Hexagon_2611.00244v1_Milne_report.pdf")),
}

PY = sys.executable
for folder, (tag, text) in P.items():
    out = Q / folder
    assert not out.exists(), out
    out.mkdir(parents=True)
    (out / "PROMPT.md").write_text(text, encoding="utf-8")
    EXTRA[tag](out)
    # pack_one_zip.py packs top-level files and the contents of ZIPs, not folders: zip every folder first
    for sub in sorted(p for p in out.iterdir() if p.is_dir()):
        shutil.make_archive(str(out / sub.name), "zip", root_dir=sub)
        shutil.rmtree(sub)
    r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    print(folder, "pack:", (r.stdout.strip().splitlines() or ["?"])[-1])
    pm = out / "PROMPT.md"
    for args in (["claude_tools/push_rule_pro_prompts.py", "--lint-math"], ["claude_tools/paper_completeness_lint.py"]):
        a = subprocess.run([PY, "-I", "-B", str(D / args[0]), *args[1:], str(pm)], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        print("  ", args[0], "->", (a.stdout.strip().splitlines() or ["?"])[-1])
        if "failing lint: 0" not in a.stdout and "failing: 0" not in a.stdout:
            print(a.stdout[-1200:])
    print("  ", ", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in out.glob("*.zip")))
