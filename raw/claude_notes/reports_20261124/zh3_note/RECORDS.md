# ZH3 note: records (24 Nov 2026)

These records are kept by the writer and checker, Claude Opus 5.5 at effort high (agent afa2696b67cad55de). The note
was written at the request of the main session 329fb1e6 (Claude Opus 5.5 at effort max). Nothing has been posted.

**Files:**

| File | What it is |
|---|---|
| `zh3_note.tex` | source; SHA-256 35b8498c… |
| `zh3_note.pdf` | 9 pages; SHA-256 128c8f18… |
| `programs/enclose_trace_defect.py` | the rigorous enclosure program written for this note; SHA-256 e1b546bb… |
| `programs/enclosures_output.txt` | its output for all six rows, at 150 digits |
| `programs/replay_floating_point_flint.py`, `programs/replay_floating_point_mpmath.py` | the two earlier floating-point replays, not rigorous |
| `build_pass1-3.log`, `zh3_note.log` | the build logs |
| `render/` | page images at 60 dpi |
| `ZH3_CHECK_EVENTS.tsv` | check events |
| `HEXAGON_METADATA_ZH3.json` | metadata draft, no personal fields |

**Build:** three pdflatex passes (MiKTeX-pdfTeX 4.27), 0 overfull boxes, no undefined references. I rendered all 9
pages at 60 dpi and read them. After the last edit, which touched page 6 only, I rendered page 6 again and read it.

**Source of the mathematics:** a GPT-6 Astra (ChatGPT Pro mode) run on the simplicity of the zeta zeros (final of
23 Nov 2026, 22:19 UTC). The statements used and where they sit in it:
- thm:fd-arithmetic-complete, prop:fd-inertia-complete, prop:fd-certificate-size and the certificate table:
  `paper/sections/arithmetic_compressions.tex` and `inertia_density.tex`;
- lem:fd-multiplicity-log and cor:fd-global-growth-numeric: `global_growth_numeric.tex`;
- the heat-flow limit of the remark: thm:fd-limits in `finite_detection.tex`.

The note rewrites the proofs. It adds:
- the proof of density of the dyadic windows (Lemma 6), which the original cites from its "compression construction";
- the derivation of the explicit formula for H¹ test functions from Bombieri's form (Lemma 9);
- the pull-back argument for the integer form when G_N might be singular.

## 0. The gate: Suzuki's Hilbert–Schmidt convergence, opened at the source

- **Source.** M. Suzuki, *Spectral convergence associated with Weil's quadratic form*, arXiv:2610.32704, LaTeX
  `screwzzwolf_6.tex`, in `reports_20261122/extended_grand_rh/workshop_inputs/cp24_followup/Suzuki_number_field/`.
  Search path: I found nothing under `pro_prompt_builds/` (find, depth 6). I then searched the four
  `reports_2026112*` folders by name, depth 7, and checked the prompt-68 zip listing.
- **What Suzuki proves:**
  - §2.3, lines 735–751 of the source: C = D_lim^{-1} is Hilbert–Schmidt on the global completion, with
    ‖C‖²_{S₂} = Σ_{γ∈Γ} γ^{−2}, summed without multiplicity. Each distinct point of Γ is a simple eigenvalue of D_lim.
  - §2.3: Π_a → I strongly, where Π_a projects onto the completion of C_c^∞(−a, a); the subspaces are nested with
    dense union.
  - §4, (4.1): ‖Π_a C Π_a − C‖_{S₂} → 0, "by the standard approximation property of Hilbert–Schmidt operators".
  - Theorem 1.1 (the eigenvalues decrease to γ_n over distinct ordinates); Theorem 1.2 (the product over distinct
    ordinates); Theorem 3.3 (inverse compression).
  - §1, line 235: "The multiplicities of the zeros are not recovered by this product".
- **What the run uses:** "Suzuki's compression argument gives C_N → C in Hilbert–Schmidt norm" for projections onto
  the finite-dimensional dyadic spaces V_N. It cites density of ∪V_N "as proved in the compression construction".
- **Outcome.** The statement is not literally Suzuki's: his subspaces are infinite-dimensional and his density is
  for C_c^∞(−a, a). What holds:
  - the same argument applies verbatim to any nested family with dense union;
  - density of ∪_N S V_N in ℓ²(Γ, m) is true.

  The note proves it in Lemma 6 from three facts:
  1. the sampling bound |û(t)| ≤ ‖u′‖₁/|t|, which needs only Suzuki's (2.2);
  2. density of S C_c^∞, by a tempered-distribution argument;
  3. removal of the mean by a wide bump, plus piecewise-linear interpolation.

  The note also works directly in ℓ²(Γ, m), so it does not need Suzuki's isomorphism with the Q_W-completion (his
  citation of [Su25, Lemma 5.4]). **The theorem is unchanged.**
- **The explicit formula.** The run cites CCM, *Zeta spectral triples*, (3.2)–(3.7), which I did not open. I used
  Bombieri's form instead, as recorded in Connes–Consani, *Weil positivity and trace formula, the archimedean place*,
  Appendix "Explicit formula" (LaTeX `weil-compo.tex` from the prompt-68 inputs). With f(e^y) = e^{−y/2}h(y) it gives
  exactly the run's formula, constants included; I derived this by hand (Lemma 9).

## 1. Literature, with exact locators

| Source | Locator read | How it bears |
|---|---|---|
| Suzuki, arXiv:2610.32704 (LaTeX) | §1 (Theorems 1.1–1.2, line 235 on multiplicities); §2.1 (2.1)–(2.3); §2.3 (whole); §3.3 (setup of Theorem 3.3); §4 (4.1), (4.2), (4.5) and the remark | the Hilbert space, C, HS convergence, distinct ordinates; multiplicities explicitly not recovered |
| Connes–Consani, *Weil positivity and trace formula, the archimedean place* (LaTeX) | Introduction, (explicit form); Appendix "Explicit formula", Bombieri's form and W_ℝ, W_p | the explicit formula used in Lemma 9 |
| Bombieri, *The Riemann hypothesis* (Clay) | not opened; cited through Connes–Consani | — |
| Alpöge, remark.pdf; Lean blog post | not opened in this task; cited as a theorem, as instructed | RH |
| Alpöge–Furman, arXiv:2608.13637 | abstract page (v2, 19 Aug 2026) | proportions ≥ 2/3 simple, ≥ 5/6 distinct, unconditional; "rank-trace inequality applied to a finite compression of Weil's Hermitian form". No fixed-height criterion, no trace powers, no Suzuki in the abstract |
| Lamzouri, arXiv:2609.02882 | abstract page (v2) | same proportions, one Hilbert-space inequality; credits the internal Claude version for the proportions |
| Mori, Zenodo 24281606 | record page | −log λ_min(√μ) ≤ Cμ^{6/5} log μ(1 + log log μ) under RH alone; a barrier: such bounds force distinct-zero proportions |
| Groskin, arXiv:2607.02828 | abstract page | finite Galerkin truncations of the Weil form; no multiplicity |
| Kim et al., arXiv:2607.24830 | abstract page | numerical realization of Suzuki's operator; no multiplicity |
| Platt–Trudgian, arXiv:2004.09765 | abstract page | RH to 3·10^12; the abstract says nothing about simplicity, and the note claims none |
| de Bruijn (1950), Newman (1976), Rodgers–Tao (2020) | **not opened** | cited only in the heat-flow remark, for the family H_t |
| Johansson, Arb (2017); ball integration (2018) | not opened; software references | — |
| Hexagon, search "simple zeros" (24 Nov) | 6 hits: Cáceres 2610.00688, 2610.00661, 2610.00343, 2610.00161 (RH criteria from Dirichlet partial sums); Baggins 2610.00486, 2610.00483 (heat-evolved random polynomials) | none on multiplicity tests |
| Hexagon, "Weil quadratic form" | 1 hit: Hackfort 2610.00346 (analytic ranks of elliptic curves) | unrelated |
| Hexagon, "multiplicity zeta zeros" | 0 hits | — |
| Hexagon, "de Bruijn-Newman" | 1 hit: Cáceres 2610.00207 | unrelated |
| Web searches: Suzuki's paper and multiplicities; "finite test simplicity zeta compression Weil" | 24 Nov | found the four arXiv items above and Alpöge–Furman/Lamzouri; no exact finite criterion for simplicity at a fixed height |

## 2. Checks, by model and effort

- **Claude Opus 5.5 at effort high (this agent):**
  - **Proofs, by targeted proof check:** Theorem 1 (23 Nov, cp03 intake), Theorem 2 (24 Nov, final intake), the
    multiplicity lemma (23 Nov). The note's rewritten proofs (Lemmas 5–9, Proposition 8) are mine, written and checked
    24 Nov.
  - **The certificate, three computations:**
    1. a floating-point mpmath replay of rows 1–4 (23 Nov);
    2. a floating-point Arb replay of rows 1–6, plus the integer count ι_N(T) = n(T) at 39.913, 62.413 and 97.632
       (24 Nov);
    3. **a rigorous Arb enclosure of all six rows** by `enclose_trace_defect.py` (24 Nov). It is independently
       written: from the note's formulas, not from the original programs.

    All three agree with the original computation's upper bounds to 10 or more digits.
- **The original computation:** a program by GPT-6 Astra (ChatGPT Pro mode), python-flint 0.9.0 / Arb at 120 digits,
  with rigorous integration and a preconditioned positive-definiteness residual below 2·10^−94. It passes levels 1–6.
  The run's own records also contain a proof-read of that program and a re-run of levels 1–3 by the same program;
  that re-run is not independent.
- **Not done:** an independent re-proof of Theorems 1–2 by an agent other than me. The run's same-model re-proofs
  exist, but are not ours.

## 3. Pass for neighbouring work

The kind is **needs a pass**: Alpöge–Furman, Lamzouri and Mori use finite compressions or windows of the Weil form,
and they give proportions or eigenvalue bounds.
- I read their abstracts, not their bodies.
- War-game: their statements are about proportions; ours are exact equivalences at a fixed height and a certificate.
  A body-level reading of Alpöge–Furman could show a rank–trace identity close to our integer form (Theorem 2),
  which counts eigenvalues of the compression above 1/T. That would not touch Theorem 1, but the credit paragraph
  should then name it.
- **Gate:** read Alpöge–Furman §§ on the "rank-trace inequality" before posting.

## 4. Five Hexagon tests

| Test | State |
|---|---|
| 1. Complete | Every result in the note is proved in it, except the heat-flow limit of Remark 10, which is labelled as not proved and not used. The certificate is a stated computation with its programs. |
| 2. Self-contained | Inputs are cited at locators opened: Suzuki (§2.3, (2.2), (4.1)), Bombieri's explicit formula through Connes–Consani's appendix, Alpöge's theorem as a theorem, Arb as software. The de Bruijn–Newman papers are cited only in the remark and were not opened. |
| 3. Stable | The run is final. The literature search found no prior finite criterion for simplicity at a fixed height. Gate: Alpöge–Furman body (§3). |
| 4. Checked | Proofs: targeted checks and rewriting by me; the certificate is rigorous twice, by two independently written programs. **Missing:** an independent re-proof of Theorems 1–2 by another agent. |
| 5. Of interest now | Suzuki's paper (Oct 2026) explicitly leaves multiplicities open; Alpöge's theorem makes the RH-conditional framework unconditional; simplicity is the active question (Alpöge–Furman, Lamzouri, Knausgård, Mori, all 2026). |

**Left before posting:**
1. The main session reads every page.
2. An independent re-proof of Theorems 1 and 2 by a fresh agent, given only the statements and Suzuki's §2.3.
3. Read the body of Alpöge–Furman (rank–trace inequality) and adjust the credit paragraph if needed.
4. Push `programs/` and these records to the workbench cited as [16] (https://github.com/KokunoYumeto/zeta-and-l-functions-workbench),
   or change [16] to the records page used for Hexagon works.
5. Decide whether Remark 10 (heat flow, unchecked companion result) stays. It is labelled, but the user may prefer
   it out.

## 5. Whom to write to when it is posted

All unsent; no drafts yet.
- **Masatoshi Suzuki:** the note answers his remark that multiplicities are not recovered, using his compressions.
- **Levent Alpöge** (and R. Furman), optional: their theorem is the input; their compression method is neighbouring.

## Update of 24 Nov 2026 (~13:xx UTC): the three gates; supersedes §§2–4 where they differ

This update was written by Claude Opus 5.5 at effort high (agent afa2696b67cad55de), at the request of the main
session 329fb1e6 (Claude Opus 5.5 at effort max).

**Files now:**
- `zh3_note.pdf`: 11 pages; SHA-256 b0c72445ac265e2c5c9ef443f48219bcd73c66246ab0919bc426991dcf6366ef.
- `zh3_note.tex`: SHA-256 45c677c0….
- Build: three pdflatex passes, 0 overfull boxes, no undefined references. I rendered the changed pages 3 and 8–11 at
  60 dpi and read them.
- `sources/` holds the opened sources:
  - Alpöge–Furman, e-print and v2 PDF;
  - Borcea–Brändén, arXiv:math/0607416v6;
  - Rodgers–Tao, arXiv:1801.05914v5.

**§2 Checks: added.**
- **Gate 1, Alpöge–Furman's body** (arXiv:2608.13637v2). I read §§1–4 in full: Theorem A p. 1, §1.2 pp. 2–3, §1.3 p. 3,
  Lemmas 3.1–3.4 p. 5, Propositions 4.1–4.3 and Corollary 4.5 pp. 6–7.
  - Their matrix is the restriction of W to about N(T,2T) modulated copies of one window on [T,2T] (a Gabor family,
    §2.3). On-line zeros give rank-one positive forms with trace m_ρ; off-line pairs give signature-(1,1) blocks
    (Prop. 4.1); the negative-index observation is credited to Bombieri (§1.3).
  - Rank–trace (Lemma 3.2) plus Montgomery's second moment give the proportions.
  - No operator with the zeros as spectrum, no trace powers, no exact count at a fixed height.
  - **Nothing there states or implies Theorem 1 or Theorem 2.** What is theirs: the principle "rank or positive index
    sees distinct zeros, trace sees multiplicity" (Prop. 4.1), and the pull-back of inertia (Lemma 3.1), which our
    Theorem 2 uses.
  - The credit and context paragraphs are rewritten with these locators.
- **Gate 2, the heat flow.** Remark 10 is replaced by §8 "The backward heat flow", Proposition 10:
  lim_{a↓0} a·j_*(−a) = γ_*²/2. The statement "With Theorem 1 this reads …" is kept.
  - I checked the source proof, thm:fd-limits (Jensen part, with its cone estimate), step by step, and found no
    failing step.
  - The proof is written into the note in full.
  - One simplification: j_* takes values in [1, ∞], so neither Newman's boundary nor Rodgers–Tao's Λ ≥ 0 is needed
    (F_a > 0 on [0, ∞) because Φ > 0, elementary). De Bruijn (1950) and Newman (1976) are therefore no longer cited.
  - Opened at their locators: Rodgers–Tao §1 (1)–(4), for the definitions of H_t and H₀ = Ξ(·/2)/8; Borcea–Brändén
    Theorem 2(b), p. 5 of the arXiv version, for the stability criterion.
- **Gate 3, the workbench.** The folder `workbench_upload/finite-arithmetic-simplicity-test/` is prepared:
  - README (programs, what each computes, rigour, model and effort; the certificate table; agreement);
  - `enclose_trace_defect.py` and `enclosures_output.txt`;
  - the two floating-point replays, with headers free of internal names.

  I scanned it for local paths and internal ids. Reference [15] (formerly [16]) now points to
  https://github.com/KokunoYumeto/zeta-and-l-functions-workbench/tree/main/finite-arithmetic-simplicity-test.
  **Not pushed:** publishing to a public repository needs the user's own word in chat, which a session message
  cannot give. Until it is pushed, that link is dead.

**§3 Pass for neighbouring work: done.** See Gate 1. The war-game finds no overlap with Theorems 1–3 or Proposition 10.

**§4 Five tests, updated.**
1. **Complete:** every result in the note is proved in it, the heat-flow limit included.
2. **Self-contained:** the inputs are cited at opened locators: Suzuki, Connes–Consani/Bombieri, Borcea–Brändén,
   Rodgers–Tao (definitions only), and Alpöge's theorem as a theorem.
3. **Stable:** the literature search and the Alpöge–Furman pass are done.
4. **Checked:** the independent re-proof of Theorems 1–2 is with agent a25c2acb. Proposition 10 has my targeted check
   only, and is not in that re-proof.
5. **Of interest now:** unchanged.

**Left before posting:**
1. The push of the workbench folder, on the user's word.
2. The re-proof result.
3. The main session's reading. The note grew from 9 to 11 pages, and §8 is new.
4. Optional: an independent check of Proposition 10.

## Update of 24 Nov 2026 (~13:xx UTC): the re-proof's three points
The independent re-proof (Claude Opus 5.5 at effort high, agent a25c2acb) confirms Theorems 1-2 with no gap. Its three points are applied: the trapezoid constant 2a+2h; an explicit sentence on singular G_N; the proof that the b_j form a basis, taken from the re-proof and credited in the note on method. Section 8 is not edited, pending a25c2acb's check of Proposition 10. PDF: 12 pages, SHA-256 ee23dbac3d40c5159d32f33bbd0ed27f35018a5ed245c2f7fdb2428eb761b9a2; 0 overfull; all reflowed pages read.

## Update of 24 Nov 2026 (~13:4x UTC): Proposition 10 independently confirmed
Agent a25c2acb (Claude Opus 5.5 at effort high) checked Proposition 10 step by step and opened Borcea-Branden Thm 2(b) and Rodgers-Tao (1)-(4); no error (independent_reproof/PROP10_CHECK.md). Its wording points W1 (local-form hypothesis) and W2 (H_2(R) = real stable) are applied, and the note on method records the check. PDF: 12 pages, SHA-256 579ee3eaf8c94310efebeb230c26fa43d4cdae8970bf4a03da2f052d24eaf5df; 0 overfull; pages 9-12 read.
