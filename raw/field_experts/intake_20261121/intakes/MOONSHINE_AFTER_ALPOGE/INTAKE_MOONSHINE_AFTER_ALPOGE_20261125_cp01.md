# Intake: MOONSHINE_AFTER_ALPOGE (prompt 97), checkpoint 01 (24 Nov 2026, 20:45 UTC)

Intake by Claude Opus 5.5 at effort max (agent a74a9a15, a copy of the lambency-6 pass agent), 25 Nov 2026. The run is
GPT-6 Astra (ChatGPT Pro mode); its own check records say "effort not exposed" and all its checks are by instances of
the same model (CM worker, lattice worker, shadows worker, lattices worker, root). Running notes:
`<local>/Documents\agent_notes\a74a9a15292272046_NOTES.md`. My spot-check script and its output:
`spotchecks\sc1_offline_zeros.py`, `spotchecks\sc1_run.log` (this folder). Check events:
`INTAKE_MOONSHINE_AFTER_ALPOGE_20261125_CHECK_EVENTS.tsv` (this folder).

Return read: `research_returns\MOONSHINE_AFTER_ALPOGE_checkpoint_01_20261124T2045Z_unzipped` (the only checkpoint; nothing
newer in research_returns or Downloads). Prompt: `TO_SEND\PRO\1_Archive_research_by_topic\SENT\97_MOONSHINE_AFTER_ALPOGE\
PROMPT.md` (read in full). The run is still going: this is checkpoint 01, about 45 minutes after its stated start.

## The most interesting items, ranked by usefulness

1. **The main question is reduced to one explicit inequality, and the reduction is right.** The companion note "CM Hecke
   L-functions after Alpöge: finite phases and a prime-ideal window criterion" (12 pp.) proves (Thm 1.2): for unitary Hecke
   characters λ_j of an imaginary quadratic field with nonzero angular infinity type and weights a_j > 0, a one-sided bound
   G(x) ≤ C_θ x^θ on windows [Y, Y^{1+δ_θ}] (arbitrarily late) for the centered prime-ideal ramp sum
   G = Σ a_j Re{Σ_{Na≤x} Λ_K(a)λ_j(a)(x/Na − 1) + x L′/L(1, λ_j)}, for every θ ∈ (1/2, 1), implies RH for every L(s, λ_j).
   Cor 1.3: one such G for λ₁ = ψ₃₆N^{−1/2}, λ₂ = ψ₂₇N^{−1/2}, λ₃ = ψ₃₆³N^{−3/2} gives RH for 36a1, 27a, their common cube,
   and Sym³ η(6τ)⁴. The analytic step is Alpöge's own abstract Lean theorem `Deduction.landau_window`. **I checked it** against
   our local copy of his archive (hypotheses `PoleData`, `WindowHypU`, conclusion lines 83–85) and redid the Mellin identity
   and residues by hand: it holds (§2, check 1). The gate of the whole programme at this rung is now that one inequality.
2. **Zero-free half-planes for exactly our H1 targets already exist (Hexagon, Nov 2026), unknown to the atlas.** The run
   cites B. Hu, Hexagon 2610.00216v2 (Re s > 7/8 for unitary Weil L-functions, including nonzero infinity type), Z. Gao,
   Hexagon 2611.00334v1 (boundary (777 − √1081)/852 ≈ 0.8734), B. Liu, Hexagon 2611.00741v1, Thm 7.33 (θ ≈ 0.8733326 for
   every number field and every continuous unitary Hecke character), after OpenAI's "Quasi-Riemann Hypothesis" (30 Sep
   2026, Thm 1.1 p. 4: Re s > 7/8 for finite-order Hecke characters of Q(√−3) and all Dirichlet characters). If these hold,
   ψ₃₆, ψ₂₇, ψ³ already have zero-free half-planes. The run read their statements but did not audit them; neither did I.
   Atlas §3.2 H1 must cite them.
3. **Single shadow components and all 24 Niemeier Epstein zeta functions have zeros off their lines (theorems).**
   Main paper Thm 1.2: a scalar shadow mixing two primitive characters has ≍ T zeros in every strip 3/4 < α < Re s < β ≤ 1 + ε,
   including infinitely many with Re s > 1 (Saias–Weingartner); this applies to S^X₁ = 5S₆,₁ + S₆,₅ at lambency 6. Thm 1.3:
   every rank-24 even unimodular Z_L(w) has ≍ T simple zeros in 23/2 < Re w < 12 (Nakamura–Pańkowski hybrid universality).
   **I found explicit zeros:** the Leech Epstein zeta function vanishes at w = 11.6084773365 + 78.7678190294 i (and five more
   below height 352, all with Re w ≈ 11.60–11.62); the lambency-6 component has zeros at s = (z+1)/2 with Re s = 0.7582
   (z = 0.5165 + 28.3079 i), 0.7819, 0.7396, … (eight with Im z < 181, i.e. Im s < 91). Each confirmed by the argument principle.
4. **A claimed correction to Cheng–Duncan–Mertens (JNT 277 (2025) 201–235).** In CDM's normalization φ₈|₄ = (y⁻¹ + y)q + …
   (their eq. 4.2.9) the run finds C_φ(−n) = a(n)/2 for n ≡ 3 mod 8 (Tunnell's a(n)), e.g. C_φ(−3) = 1, a(3) = 2, and a cusp
   parameter shifted by −4 ("C8 contains minus four φ"). Not checked by me or at the source by anyone outside the run;
   a correction letter is a candidate only after that check.
5. **Our atlas and pass, confirmed and sharpened.** Our C1 (twined shadow = Sym^k of V) is proved as Thm "Symmetric powers in
   the twined shadow" with Sym⁴ and the zero cases; B3, B14 proved; B4 with exact factors at 2 and 3; B6 Ogg cutoffs explicit
   (p > 7000 unconditionally, p > 4300 from Alpöge's theorem, 898 primes checked); B13 isogeny explicit; 129 planes give 18
   theta series (J is the single representative with k = 23058, t = 0, z = 14823/1241). Two refutations of our side:
   the order-6 residue action does not stabilize any single Leech neighbour (it permutes the six in two 3-cycles), and
   Alpöge's step-18 lattice has growing rank (not a Niemeier lattice).

## 1. Useful or not

Useful. The main question is not proved and no gate is strictly smaller than "an arithmetic one-sided prime-ideal
estimate", but the run (i) states the gate exactly and proves the analytic half by reducing it to Alpöge's formal theorem
(item 1), (ii) brings in the zero-free half-planes of Hu, Gao and Liu that bear directly on our H1 rung (item 2), and
(iii) turns three open questions of the atlas (single shadow components, Niemeier Epstein zeros, Ogg) into theorems.
Weakness: everything is same-model checked; the two zero theorems rest on published theorems whose statements the run
read but whose locators nobody else has checked (problems P1, P2).

## 2. What it proved (statements, hypotheses, checks)

Paper A: "Moonshine after Alpöge's theorem: Dirichlet shadows, off-line Epstein zeros, and CM reductions" (main.tex +
nine section files). Paper B: "CM Hecke L-functions after Alpöge: finite phases and a prime-ideal window criterion"
(cm_hecke_windows.tex, 12 pp.). Statement ids are the run's provisional ones.

| Statement | Exact content and hypotheses | Run's checks (GPT-6 Astra, ChatGPT Pro mode) | Checks by others |
|---|---|---|---|
| A Thm 1.1 (character constituents) | m ≥ 2, d \| 2m, χ odd mod 2m/d: L(Σ_r χ(r)S_{m,dr}, s) = 2d(4m/d²)^s L(2s − 1, χ); every component of every umbral shadow and twining is a finite combination; zeros of a nonzero G_{d,χ} in 1/2 < Re s < 1 lie on Re s = 3/4 (Alpöge) | targeted check; independent re-proof (same model); 303 untwined components by computation | none |
| A Thm (shadow zero classification) / Thm 1.2 | nonzero H = Σ c_r S_{m,r}; unique expansion D_c = Σ_ψ P_ψ L(·, ψ) (Dirichlet polynomials P_ψ); if two P_ψ ≠ 0: ≍ T distinct zeros in 3/4 < α < Re s < β ≤ 1 + ε; one P_ψ: zeros of P_ψ(2s−1) and L(2s−1, ψ) | independent re-proof granting Saias–Weingartner | **me: computation, 8 zeros off Re s = 3/4 for S^X₁ (check 3)** |
| A Thm l6-mixed | L(S^X₁, s) = 24^s{3(1 + 3^{1−2s})L(2s−1, χ₋₄) + 2(1 + 2^{1−2s})L(2s−1, χ₋₃)}; infinitely many zeros off 3/4 and in Re s > 1; same for S^X₅ | targeted check + re-proof | me: zeros exhibited in the critical strip; none with Re s > 1 below height 150 (consistent, not exhibited) |
| A Thm l6-sympowers (our C1) | V faithful 2-dim of GL₂(F₃) with trace √−2 on one order-8 class: det V = δ, a − 1 = tr Sym²V, b = tr Sym³V, a + c = 1 + tr Sym⁴V; V ⊗ Sym²V ≅ Sym³V ⊕ V ⊗ det V, V ⊗ det V ≅ V̄; −I acts by (−1)^k; isotypic combinations of every twining are multiples of the five Dirichlet constituents; at Frob_p of E with full mod-3 image δ = χ₋₃(p) | targeted check (class table) | our pass (l6_5, exhaustive, 48 elements; same statement) |
| A Thm 1.3 (Niemeier zeros) | L even unimodular, rank 24: Z_L = A ζ(w)ζ(w − 11) + (N₂(L) − A)L(Δ, w), A = 65520/691; for 23/2 < α < β < 12: c₁T ≤ #zeros ≤ c₂T, lower bound for simple zeros; reflected strip too | independent re-proof granting Nakamura–Pańkowski Main Thms 1–2, Thm E | **me: computation, six zeros of Z_Λ with Re w ≈ 11.60–11.62 (check 2)** |
| A Thm residue-eta (B3) | squares mod 840 = ⟨289⟩ ≅ C₆; Frame shapes d^{24/d}; η(dτ)^{24/d} newforms of levels 1, 4, 9, 36; CM by Q(√−3) exactly for d = 3, 6 = where the cubic character mod 7 is nontrivial | targeted check | our atlas X16 (computation) |
| A Prop residue symbols (B14) | κ(r) = (r/5)₄(r/π)₃, π = 2 − ω of norm 7 | targeted check | atlas X16f |
| A Thm primitive cube (B4) | ψ₃₆ (conductor 2√−3), ψ₂₇ (conductor 3), ψ₃₆³ = ψ₂₇³ = Ψ (conductor √−3); θ_{ψ36} = η(6τ)⁴, θ_Ψ = η(3τ)⁸, θ_{ψ27} = η(3τ)²η(9τ)²; L(Sym³f, s) = L(g, s)L(f, s − 1) with no omitted primes (factor (1 + 8·2^{−2s})^{−1} at 2, 1 at 3) | targeted + independent re-proof | atlas X15 (p < 400) |
| A Thm universal theta coordinates + Thm 129 | J_P = {x ∈ Λ : (x, P) ≡ 0 mod 3} for a totally isotropic plane P of Λ/3Λ: det 81, level 3, Θ = aE + bE(3τ) + xΔ + yΔ(3τ) + zF, a = 7381/66430, b = 59049/66430, z = (k − 2073aC)/102, x = −aC − z, y = 59049t − bC − 729z, t ∈ {0,…,8}; 129 representatives give 18 series | targeted, re-proof of the algebra; exact enumeration; orbit completeness carried as input | me: q²-coefficient algebra and J's z = 14823/1241 (check 4) |
| A weight-one eta forms | 29 Conway entries, 28 Frame shapes of weight one: 5 cuspidal dihedral, 23 Eisenstein | computation + re-proofs (Sturm) | none (not read by me) |
| A M₁₁ multiplicities | generalized Hurwitz class part for arbitrary conductor; explicit L(1, χ) bounds under Alpöge; CDM cusp shift −4; C_φ(−n) = a(n)/2 (n ≡ 3 mod 8) | independent re-proofs (same model) | none |
| A mock Mellin | regularized completed Mellin functional equation with explicit shadow correction; no Euler product, no RH | re-proof | none |
| A geometry | Fricke constants = glue orders (cusp divisors); explicit 2-isogeny y² = T₆(T₆+8)(T₆+9) → 24a1; Niemeier Θ_L vanishes at a CM point only for h = 30 (all 13 rational singular moduli incl. non-maximal orders); Ogg: r(p) < s(p) for p > 7000, and for p > 4300 under Alpöge; 13 equality primes | computation + re-proofs | none |
| B Thm 1.1 (finite phases) | F normalizes a finite Γ ⊂ GL(V), h = order of conj. by F, e = exponent: (sF)^{he} = F^{he}; trace bounds on (sF)^{hen} bound all eigenvalues of F; on y² = x³ + b, s = (ωx, y) commutes with Frobenius at good prime ideals of K; at rational p: FsF^{−1} = s^p, (sF)⁶ = F⁶ | targeted + re-proof; computation (p < 1000) | none |
| B Thm 1.2 + Cor 1.3 (window criterion) | item 1 above | targeted + independent re-proof granting Alpöge's abstract theorem and Hecke's continuation | **me: targeted proof check against the Lean statement (check 1)** |
| B Prop colour; Prop twist; Prop finite family; trace lattice; Prop auxiliary | ε(u) = u^{−m} on μ₆; type-6 twist leaves the colour; centre of GL₂(F₃) = ±1; E₃₆ ≅ E₂₇ over K(∛2), a_p(x³ + b) = −φ(b)(χ(b)J + χ(b)²J̄); no fixed finite Dirichlet family represents the angular sequence; det_Z = 3ⁿ(det H)², dual 𝔇^{−1}L^#; Hu's principal Euler factor = ζ_F(2)^{−1}L(6s − 3, χ)J(s) with J nonvanishing on Re s > 1/2; conditional iteration barrier 3/5 | targeted + re-proofs | none |

## 3. New against our atlas and the lambency-6 pass

- **Confirms:** B1 (now every lambency, every twining), B2, B3, B4, B14, B5 (Fricke), B13 (now an explicit isogeny), our C1
  (with Sym⁴ and the zero cases: S^X₁, S^X₅ are mixed on classes 1A, 2A, 2B, 3A, 6A and single-character on 4A, 8A, 8B),
  correction 4 of atlas §1.6 (the cubic twist by χ(2) between 36a1 and 27a; the cubes coincide).
- **Refines:** atlas §1.6 item 1 and G2 ("GRH places no zeros" for S^X₁) → theorem: off-line zeros, ≍ T of them in strips;
  G3 ("no zero statement for Z_L follows") → theorem: off-line zeros for all 24; B6 → explicit cutoffs 7000 / 4300 and the
  finite check; B4 → no omitted primes; B7 → all 13 rational singular moduli; theta coordinates of all 129 planes.
- **Contradicts / corrects:** (a) atlas B6 says "the class-number form and its proof are the atlas's": the run found the
  fixed-point class-number formula already in Ogg 1974 (p. 452); only the cutoffs and the finite check are new.
  (b) The residue generator acts on the rational space of N(A₅⁴D₄) and preserves J and both A₂¹² extensions, but permutes the
  six Leech extensions in two 3-cycles; only ⟨c³⟩ (order 2) stabilizes a Leech extension (refuted statement
  LAT-LEECH-FULL-ACTION). (c) Atlas §5 item 12 / M097 ("is the step-18 lattice Niemeier over Z[ω]?"): no; the formal family
  has k ≥ x^{9/2+…} and ranks N(j) = k + j(t + 1), unbounded (Lean `SizeK`, `Ranks.N`, `FamCore.Win_unb`). (d) Prompt line 124
  listed the umbral centre as a candidate order-3 operator: the centre is ±I (refuted CM-UMBRAL-CENTRE), as our pass had it.
  (e) Atlas §3.2 H1 calls the H1 L-functions "beyond": correct for RH, but zero-free half-planes Re s > 7/8 (Hu) and ≈ 0.8733
  (Liu) are claimed for them (item 2).
- **New beyond both:** the window criterion (item 1); the finite-family obstruction (no fixed finite set of Dirichlet
  characters can carry the angular prime sequence: frequencies are not roots of unity); the colour proposition (the μ₆
  colour sees the infinity type only mod 6); the continuation of Hu's principal Euler factor with the type-±12 factor; the
  C_φ = a/2 normalization.

## 4. Open: each main question's gate

- **Q1 (main): RH for L(s, ψ₃₆), L(s, ψ₂₇), L(s, Ψ = ψ³) and Sym³ η(6τ)⁴.** Gate: the one-sided window inequality
  G(x) ≤ C_θ x^θ on arbitrarily late [Y, Y^{1+δ}] for G = G_{λ₁} + G_{λ₂} + G_{λ₃} (B eq. (2.1)–(2.3)), for every θ ∈ (1/2, 1).
  Alpöge's arithmetic wrapper (`windowInequality_of_artinInputs`, `level_gm_le_on_family_scales`) produces such windows only
  for rational residue-class families; the angular prime-ideal weights need a new comparison. Approaches tried and where
  they stopped (ledger): local cubic commutation (local only); fixed finite Dirichlet families (impossible, proved); varying
  moduli (coefficient norm loses the half power, centering error uncontrolled); Hu's cubic-theta principal factor (exposes
  type ±12 factors; conditional iteration only to 3/5); cubic and ninth coefficientwise powers of normalized cubic Gauss
  sums (identities proved; the missing estimate is a signed diagonal correlation, individual bounds give only order X).
  No movement past the gate at checkpoint 01; the first timed review was due at about 23:00 UTC.
- **Q2–Q9:** stated proved in QUESTIONS.tsv except: zeros of Z_L in Re w > 12 (open), the distribution law of m₅₅(W_D)
  (needs central-value input), 129-orbit completeness and stabilizer orders (carried from S6_05, not re-proved).

## 5. Relations, the fleet included

- `fleet_lookup.py` finds no fleet lemma on Epstein, umbral, Niemeier, Leech, Hecke L-functions, GRH or zero-free regions
  (0 of 8977). The fleet meets this run only through the planes of atlas §2.1 (PG(2,3) etc.), which this run does not touch.
- Inside our programme: item 1 is the Hecke-character analogue of the ALP_MACHINE / ALP_CONNES window gates (H04.4 is the
  cubic Kummer analogue); item 2 bears on GRH_RUNGS §2 (GL₁/K) and on the OpenAI QRH reading already in our records;
  C1 and the Frobenius tower are now a theorem in a paper; the Niemeier zeros close atlas G3 and WEEK-029's kernel question
  (the Leech kernel ζ(w)ζ(w − 11) − L(Δ, w) has zeros off Re w = 6: w = 11.6085 + 78.768 i is one).

## 6. Candidates

- **Next prompt (most useful):** the window inequality itself, briefed with Alpöge's arithmetic wrapper (the Lean files
  named in B §5), the ALP_MACHINE window gates, and the zero-free-half-plane methods of Hu, Gao and Liu (whose principal
  factor B §6 continues). One prompt per gate; parsimonious with Pro slots.
- **A reading task:** audit Hu 2610.00216v2, Gao 2611.00334, Liu 2611.00741 (statements, dependencies, numerical
  certificates) before the atlas or any paper of ours cites their half-planes as facts.
- **Corrections to our records:** atlas B6 credit to Ogg 1974; B4 exact local factors; §5 item 12 answered (growing rank);
  the Leech-neighbour action (two 3-cycles); §3.2 H1 with the zero-free half-planes; LAMBENCY6_PASS C5 unaffected.
- **Hexagon:** not yet. The run's main paper is a candidate when the run ends and its two zero theorems' sources are
  checked (P1, P2); a short note on the Leech Epstein zeros with the explicit first zeros is possible but is an application
  of Nakamura–Pańkowski (low novelty).
- **Letter:** to Cheng, Duncan and Mertens on the factor two and the cusp shift, drafted only after a check at the source.

## 7. Problems, each with the exact passage

- **P1 (attribution to verify).** A `shadows.tex` l. 126–129: "Their main theorem \cite[pp.~335--336]{SW2009} supplies
  η > 0 and upper and lower linear zero-counting bounds in every strip 1/2 < σ₁ < σ₂ ≤ 1 + η for D_c." Saias–Weingartner's
  theorem as usually stated concerns Re s > 1; the strips inside the critical strip may need another source (results via
  joint universality). Not on disk; not checked by me. The conclusion is consistent with my numerics (check 3).
- **P2 (locators to verify).** A `niemeier_zeros.tex` l. 58–64 and 83–85: "Main Theorem~1 of Nakamura--Pa\'nkowski
  \cite[arXiv v4, p.~4]{NP2016} now supplies a lower bound proportional to T ..." and "Theorem~E ... p.~5". Not on disk;
  the hypotheses as stated (nonmonomial polynomial with Dirichlet-series coefficients absolutely convergent on Re z > 1/2)
  are met; the conclusion is confirmed numerically for the Leech lattice (check 2).
- **P3 (unaudited inputs).** B §6 l. 634–639: "We have checked the statements, their cited dependencies, and the local
  calculation used below, but have not independently audited their full analytic proofs or the numerical certificates
  named in Liu's text." Correctly scoped, but the abstract's framing of the note around Hu's construction depends on them.
- **P4 (published-paper correction unverified).** A `tunnell_normalization.tex` l. 13–17: "C_φ(−n) = ½a(n) (n ≡ 3 mod 8).
  In particular C_φ(−3) = 1 whereas a(3) = 2." and CHECK_EVENTS "CDM theta correction and cusp shift ... C8 contains minus
  four phi; literal assertion of odd-discriminant vanishing is false". A claim of error in a published paper, same-model
  checked only.
- **P5 (gloss of the remark).** B l. 55–57: "Alpöge's announcement describes the sixfold metaplectic cover and the Eisenstein
  CM curve in its third step". The remark's step 3 says a theta "on sixfold cover of GL₅" and reads the quadric on C/Z[ω];
  "metaplectic" and the GL₂ cover belong to footnote 3. Minor; B §5 cites the GL₅ wording correctly elsewhere.
- **P6 (records).** CHECK_EVENTS names "GPT-6 Astra Pro; effort not exposed" throughout; our naming is "GPT-6 Astra
  (ChatGPT Pro mode)". Many events are re-proofs "from statement alone" by sibling workers of the same run: record them as
  same-model re-proofs, never as independent checks.
- **P7 (draft state).** CONTINUE.md: "The main draft compiles, but its final visual review and two complete readings are
  not yet finished." The main paper is not deliverable at checkpoint 01.

## What I did not read

The bodies of `weight_one.tex`, `class_numbers.tex`, `geometry.tex`, `mock_mellin.tex`, `all_lambencies.tex`,
`eta_signed_mellin.tex`, `mason_theta.tex` beyond l. 330; the workbench check folders (INDEPENDENT_*.md, programs, the 129
certificates); the PDFs (not rendered). Not opened: the sources Saias–Weingartner 2009, Nakamura–Pańkowski 2016, Hu, Gao,
Liu, OpenAI QRH, Cheng–Duncan–Mertens (none on disk except CDM inside the prompt ZIP; my context limit stopped further
source reading). Statements in §2 and §3 for those parts are as the run records them.
