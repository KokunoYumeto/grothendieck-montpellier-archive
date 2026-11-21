# Purity and zero-statistics source ledger

Run: CUE_GCT-20261121-purity. Researcher: GPT-6 Astra Pro (`/root/purity_zero_status`); configured reasoning effort is not exposed. Sources below are background inputs or exact statement/hypothesis checks, not claimed independent verifications of entire literature proofs. Deductions P-01–P-11 appear in `findings.tex`; their identifiers designate development in this run and do not assert historical priority. Status deductions P-Z01/P-Z02 appear in `zero_status.tex`.

## Background IDs and exact locators

### P-B01 — Quadratic-character small bias

Alon, N., Goldreich, O., Håstad, J., & Peralta, R. (1992). Simple constructions of almost k-wise independent random variables. *Random Structures & Algorithms, 3*(3), 289–304. https://doi.org/10.1002/rsa.3240030308

Primary author copy: https://johanhastad.se/almostindep.pdf (19-page copy dated September 25, 1997). Exact locator: §4, Theorem 1 (Weil character bound), Construction 2, Proposition 2 and its proof, printed pp. 9–10 / PDF pages 9–10. P-02 uses only the monic squarefree case, and changes the arbitrary zero-character convention to +1; the same n/p error applies. Publication metadata checked against publisher and author page https://www.wisdom.weizmann.ac.il/~oded/p_aghp.html. Web refs: turn677747127view2, turn282302316view1, turn318993354search2.

### P-B02 — Curve point bound

Deligne, P. (1974). La conjecture de Weil. I. *Publications Mathématiques de l’IHÉS, 43*, 273–307. https://doi.org/10.1007/BF02684373

Primary scan: https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf. Exact locator: formula (1.5.1), p. 275, and Theorem (1.6), p. 276. Applying the trace formula to a smooth projective geometrically connected curve, with H⁰ of dimension 1, H¹ of dimension 2g, and H²=Q_l(−1), yields |#C(F_q)−(q+1)|≤2g√q. This recovers the classical curve theorem; no historical-priority claim is made for Deligne in dimension one. Web refs: turn677747127view0, turn282302316view0. The original theorem statement and trace formula were read, not the entire proof of Weil I.

### P-B03 — Trace formula and weights

Deligne, P. (1977). *Cohomologie étale (SGA 4½)* (Lecture Notes in Mathematics, Vol. 569). Springer. Exact locator: Rapport sur la formule des traces, Theorem 3.2 (trace formula); Theorem 3.1 and Proposition 3.3 give the determinant/L-function formulation. French primary-text transcription inspected: https://grothendiecksga.com/read/sga4.5/fr/II_3.html. Web ref: turn273425817view2.

Deligne, P. (1980). La conjecture de Weil. II. *Publications Mathématiques de l’IHÉS, 52*, 137–252. https://doi.org/10.1007/BF02684780. Exact locators: Theorem 3.3.1 and §3.3.10 for the compact-support weight bound; Theorem 3.5.3 for equidistribution. The large original PDF was not successfully opened through this tool; these exact locators were verified in the author-hosted Katz–Sarnak text below, §9.0.15, which states the needed result and explicitly cites both 3.3.1 and 3.3.10. No full-proof check of Weil II is claimed.

Katz, N. M., & Sarnak, P. (1999). *Random matrices, Frobenius eigenvalues, and monodromy* (American Mathematical Society Colloquium Publications, Vol. 45). American Mathematical Society. Author-hosted book: https://web.math.princeton.edu/~nmk/RMFEM.pdf. Exact locators: §§9.0.13–9.0.16, printed pp. 269–270 (duality, affine vanishing, trace formula, weights, geometric coinvariants); Theorem 9.2.6 (equidistribution under the stated monodromy hypotheses); §§9.1.5–9.1.7 for smooth proper cohomology and purity. Web refs: turn387134677view1, turn905674939view2, turn991829417view1. These sections/theorem were read; no claim of reading the entire book.

### P-B04 — Effective Chebotarev under Dedekind GRH

Lagarias, J. C., & Odlyzko, A. M. (1977). Effective versions of the Chebotarev density theorem. In A. Fröhlich (Ed.), *Algebraic number fields* (pp. 409–464). Academic Press.

Original paper in a later TeXromancers transcription: https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf. Exact locator: Theorem 1.1, Corollary 1.2, formula (1.4), transcription p. 4. Corollary 1.2 assumes GRH for the Dedekind zeta function of L and provides an unramified prime in each conjugacy class with norm at most c₂(log Δ_L)²(log log Δ_L)⁴, with an effective absolute constant. L=Q is explicitly handled by prime 2. Bibliographic identity checked at author publication list https://websites.umich.edu/lagarias/PUBLICATIONS/zeta.html. Web refs: turn677747127view1, turn858301579view1. P-08 is a new conditional reduction using this background bound; it is not a claim that a suitable common arithmetic encoding exists for ROABPs.

### P-B05 — Montgomery supported pair correlation

Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. In *Analytic number theory* (Proceedings of Symposia in Pure Mathematics, Vol. 24, pp. 181–193). American Mathematical Society.

Author-hosted scan: https://public.websites.umich.edu/hlm/paircor1.pdf. Exact locator: §1, theorem and equations (1)–(4), pp. 181–182. RH is assumed at the opening. The weight is 4/(4+u²); normalization is T log T/(2π); the theorem gives the form factor uniformly on compact subintervals of |α|<1. P-Z01 is the Fourier consequence for compactly supported transforms in (−1,1), preserving the original weight and ordered-index diagonal convention. The full-support conjecture is distinguished in equations (11)–(12), pp. 183–184. Web ref: turn991829417view2. The needed theorem, normalization, and Fourier conversion were checked, not the complete 13-page proof.

### P-B06 — Hughes–Rudnick

Hughes, C. P., & Rudnick, Z. (2003). Linear statistics of low-lying zeros of L-functions. *The Quarterly Journal of Mathematics, 54*(3), 309–333. https://doi.org/10.1093/qmath/hag021

Primary supplied source: `sources/LIT_Hughes_Rudnick_low-lying_zeros_linear_statistics/main.tex`. Exact locators: Introduction (complex ordinates allowed, no GRH assumed, source lines 94–150); Definition 2.1 (admissible f, line 340); Theorem 3.1, label `thm:expectation` (line 383, support [−2,2]); Theorem 4.1, label `thm:Wf_variance` (line 505, support [−1,1]); Theorem 5.1, label `thm-L:Gaussian moments` (line 621, m<2/α); Theorem 8.1, label `thm:inf_less_1/4R` (line 1349); Corollary 8.2, label `thm:inf_less_1/4` (line 1454); Theorem 8.3, label `thm:pos_prop_small_zeros` (line 1484, β≥0.633). Definition x_{χ,j}=γ_{χ,j} log q/(2π); x_{χ,1} is the first nonnegative ordinate. Mean/variance/restricted moments are already unconditional analytic statements; §8 explicitly assumes Dirichlet GRH. Publication year verified as 2003, not 2004, using the primary OUP record and author publication list. Web refs: turn669156525search0, turn669156525search17.

### P-B07 — Rudnick–Sarnak

Rudnick, Z., & Sarnak, P. (1996). Zeros of principal L-functions and random matrix theory. *Duke Mathematical Journal, 81*(2), 269–322.

Primary paper copy: https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/rudnick-sarnak.pdf. Exact locators: Theorems 1.1–1.2, coefficient Hypothesis (1.7), and support condition Σ|ξ_j|<2/m. Theorem 1.1 permits complex ordinates in its smoothed analytic statistic; Theorem 1.2 adds target RH for the real-zero/unsmoothed form. The coefficient condition is required in the stated treatment for degree m>3. The m=1 Dirichlet/zeta instances are the instances discharged by stipulated Alpöge. Web ref: turn696136632view1. Statement/hypothesis audit, not full-paper proof verification.

### P-B08 — Iwaniec–Luo–Sarnak

Iwaniec, H., Luo, W., & Sarnak, P. (2000). Low lying zeros of families of L-functions. *Publications Mathématiques de l’IHÉS, 91*, 55–131. https://doi.org/10.1007/BF02698741

Primary scan: https://www.numdam.org/item/10.1007/BF02698741.pdf. Exact locators: §1 standing RH convention p. 56; Theorems 1.1–1.3 for cuspidal GL₂ target families; Theorems 1.4–1.5 for symmetric-square GL₃ target families; Theorem 1.9 and Theorem 1.10/Hypothesis S (both p. 66); §4, pp. 88–89, on auxiliary symmetric-square/Rankin–Selberg individual prime sums and their averaged replacements. The proof does not justify declaring all the auxiliary individual RH assumptions irreducibly necessary: the authors explicitly remove some by averaging in the claimed ranges. Conversely, the target cuspidal and symmetric-square RH is not Dirichlet or one-dimensional Hecke-character GRH. Web refs: turn167264000view0, turn651032895view0, turn651032895view1, turn651032895view2, turn114835679view1, turn890935485view0. Statement and dependency audit only.

### P-B09 — Conditional Hecke-family example

Gao, P., & Zhao, L. (2020). One-level density of low-lying zeros of quadratic and quartic Hecke L-functions. *Canadian Journal of Mathematics, 72*(2), 427–454. https://doi.org/10.4153/S0008414X1900021X

Primary preprint: https://arxiv.org/pdf/1708.01701 (v3, March 22, 2019). Exact locators: Theorem 1.1, p. 3, quadratic Q(i) family with support (−2,2), symplectic one-level density; Theorem 1.3, p. 3, quartic family with support (−20/19,20/19), unitary density; Lemma 2.8, p. 9, auxiliary nonprincipal Hecke-character prime sum under GRH. These dependencies are covered conditionally by the user-stated Masullo Hecke GRH, not by Dirichlet GRH alone. Web refs: turn696136632view2, turn858301579view3, turn394727321view0.

### P-B10 — Function-field moment limitations

Sawin, W. (2020). A representation theory approach to integral moments of L-functions over function fields. *Algebra & Number Theory, 14*(4), 867–906. https://doi.org/10.2140/ant.2020.14.867

Primary supplied source: `sources/LIT_representation_theory_approach_to_moments_function_fields/main.tex`; arXiv https://arxiv.org/abs/1810.01303. Exact locators: Hypothesis 1.3, label `hypo`, line 77; Theorem 1.4, label `main`, line 85; Remark 1.9(1),(5), lines 204–224. The theorem assumes H(n,r,tilde r,w), n>2max(r,tilde r)+1, and characteristic ≠2 if n=4 or 5. Its error includes q^((w−n)/2) C_{r,tilde r}^n n^(r+tilde r). Remark 1.9(5) obtains w=n−1 from duality, hence O(q^(−1/2)) with other parameters fixed. Remark 1.9(1) retains stronger cohomology and uniform Betti-number gates for general stronger degree-aspect/ratio/correlation conclusions. The paper also proves an unconditional unbalanced case in Corollary 1.8 (source line 156, repeated later at label `combined-result`, line 941), with r_-=1 and error sqrt(q)*(q^{−(p−2r)/(2pr)}*(r+2)^{r+1})^n*n^{r+1}, under the stated n/characteristic conditions. This restricted degree-aspect result must not be omitted. Publisher PDF metadata: https://msp.org/ant/2020/14-4/ant-v14-n4-p03-s.pdf; web refs turn404601268search12, turn404601268search0. The original source is supplied, so no current universal claim about all later function-field moment literature is inferred from its 2020 discussion.

### P-B11 — CFKRS and CUE distinction

Conrey, J. B., Farmer, D. W., Keating, J. P., Rubinstein, M. O., & Snaith, N. C. (2005). Integral moments of L-functions. *Proceedings of the London Mathematical Society, 91*(1), 33–104. https://doi.org/10.1112/S0024611504015175

Primary supplied source: `sources/LIT_CFKRS_integral_moments_of_L-functions/integralmoments2v.tex`. Exact locators: §1.5, `sec:mainconjectures`, from source line 883; Conjecture 1.5.1, `thm:zeta2kconjecture`, line 919; exact finite-N CUE Theorem 1.5.2, `thm:UN2k`, line 968. The recipe itself is §2.1. The rectangular/CUE agent owns detailed numbering and the exact matrix-integral derivation. The arithmetic conjecture is not obtained merely by discharging RH/GRH in unrelated supported zero-statistics theorems.

### P-B12 — Quantum-chaos sources; memory qualification

Bohigas, O., Giannoni, M. J., & Schmit, C. (1984). Characterization of chaotic quantum spectra and universality of level fluctuation laws. *Physical Review Letters, 52*, 1–4. https://doi.org/10.1103/PhysRevLett.52.1

Berry, M. V., & Keating, J. P. (1999). The Riemann zeros and eigenvalue asymptotics. *SIAM Review, 41*(2), 236–266. https://doi.org/10.1137/S0036144598347497

Berry, M. V., & Keating, J. P. (1999). H=xp and the Riemann zeros. In J. P. Keating, D. E. Khmelnitskii, & I. V. Lerner (Eds.), *Supersymmetry and trace formulae: Chaos and disorder* (pp. 355–367). Plenum Press. Author-institution bibliographic record: https://research-information.bris.ac.uk/en/publications/ih-xpi-and-the-riemann-zeros/.

The symmetry-class connection was recalled from memory and is explicitly marked that way in the paper. Publication locators and the SIAM abstract's H_cl=XP speculation were verified against primary publication/author records (turn669156525search2, turn669156525search4; APS DOI above). No uninspected chapter or equation number is claimed. The stipulated statements do not construct a specified differential or pseudodifferential Hamiltonian with the desired arithmetic spectral interpretation. The paper explicitly distinguishes this from the elementary abstract diagonal self-adjoint operator obtained by inserting the already-given real zero ordinates into its definition.

### P-B13 — User-stipulated inputs and limits of the attachments

Alpöge: `sources/ALPOGE_Main.lean` and `sources/ALPOGE_Statements.lean`. Read the actual exported declarations `riemannHypothesis`, `riemannZeta_eq_zero_re`, `LFunction_ne_zero_of_half_lt_re`, `LFunction_eq_zero_re`, and `LFunction_eq_zero_re_of_isPrimitive`, and their statement predicates. These are used as stipulated theorem input; imports were not rebuilt, and this ledger is not a truth audit.

Masullo: `sources/MASULLO_STATEMENTS_INDEX.md` only. The prompt attributes Hecke GRH to §1.2; this section's numbered statement/full proof is not present in the supplied index. Theorem 13.3.1.1, indexed PDF p. 522, is a trace-formula claim; its following malformed row contains editorial placeholders. Conjecture 14.1.2.1, p. 529, concerns general automorphic GL_n GRH/GSH and is explicitly a conjecture. Proposition 14.1.2.3, p. 531, assumes Conjectures 14.1.2.1 and 14.1.2.2. These entries do not validate a general automorphic theorem. All uses of M remain conditional on the user-stated Hecke claim, with no invented theorem number or proof check.

### P-B14 — Explicit conductor budget

Grothendieck, A. (1977). Formule d’Euler–Poincaré en cohomologie étale (I. Bucur, rédaction). In *Cohomologie l-adique et fonctions L (SGA 5)* (Lecture Notes in Mathematics, Vol. 589), Exposé X. Springer. Exact locators: Theorem 7.1, Corollary 7.12, formula (7.13). Primary-text English transcription inspected: https://grothendiecksga.com/read/sga5/en/X-7.html (turn343029532view0); its French counterpart did not load in this tool. The l-adic formula used in P-06 is explicitly stated in the author-hosted Katz–Sarnak book, proof of Lemma 10.1.12, printed p. 296 (turn387134677view0). That formula plus h_c^0=0 and h_c^2=δ_ij gives the exact conductor expression; the whole SGA proof is not claimed independently verified.

### P-B15 — Rank-one measurements and energy distortion

Cai, T. T., & Zhang, A. (2015). ROP: Matrix recovery via rank-one projections. *The Annals of Statistics, 43*(1), 102–138. https://doi.org/10.1214/14-AOS1267

Primary author-hosted article: https://tony-cai.com/assets/pdf/papers/ROP.pdf. Exact locators: Definition 2.1, Theorems 2.1–2.2, p. 107, for the ℓ₁ measurement condition; §2.2, pp. 108–110; Lemma 2.1, p. 109, for failure of constant-distortion ℓ₂ restricted isometry with subambient sampling in the Gaussian rank-one matrix model. The lemma's proof is assigned by the paper to supplementary material, which was not read. This is a relevant predecessor, not an attribution of the exact weighted tensor statement P-09 to the paper. P-09 has its own complete deterministic trace proof. Web refs: turn851314685view0, turn170484496view1, turn637901333view2.

### P-B16 — Width-one kernels as completely entangled subspaces

Parthasarathy, K. R. (2004). On the maximal dimension of a completely entangled subspace for finite level quantum systems. *Proceedings of the Indian Academy of Sciences—Mathematical Sciences, 114*(4), 365–374. https://doi.org/10.1007/BF02829441

Primary author preprint: https://arxiv.org/pdf/quant-ph/0405077. Exact locators: Proposition 1.3, Proposition 1.4, and Theorem 1.5, preprint pp. 4–6. Read both complete proposition proofs and the theorem deduction. The Vandermonde product-vector construction is the diagonal polynomial-evaluation construction in P-10; the optimal codimension is Σ_i(d_i−1)+1. The elementary arbitrary-node annihilator and the tensor-train kernel/conditioning formulation are written out in P-10. Publication metadata corroborated by https://repository.ias.ac.in/36155/. Web refs: turn637901333view0, turn698733368view0, turn444985646search1. The later sections on perfectly entangled subspaces were not reviewed.

### P-B17 — Tensor-train ranks and closed coefficient classes

Oseledets, I. V. (2011). Tensor-train decomposition. *SIAM Journal on Scientific Computing, 33*(5), 2295–2317. https://doi.org/10.1137/090752286

Primary published article copy: https://users.math.msu.edu/users/iwenmark/Teaching/CMSE890/TENSOR_oseledets2011.pdf. Exact locators: §2, definition and equation (2.1); Theorem 2.1 and complete rank-factorization proof, pp. 2298–2299. These were read. Corollary 2.4, p. 2300, also records closedness/existence for bounded TT ranks; its proof was read. P-10 uses only exact rank factorization, homogeneous minor equations, compactness, and the elementary parameter upper bound. No numerical TT-SVD algorithm was implemented or certified. Web refs: turn637901333view1, turn698733368view1, turn698733368view2; publisher metadata turn444985646search2.

## Scope of citation checks

The bibliography distinguishes primary text, author-hosted copies, publisher metadata, later transcriptions, supplied source files, and memory-based explanations. Numerical theorem labels derived from supplied LaTeX use the source's shared theorem counters; integration should preserve the source label as a second locator. This ledger does not certify source completeness, detect unseen subsequent literature, or claim formal verification.

### P-B18 — Source of the rank-profile mechanism used in the fully proved width-three specialization

Liu, Y. (2026, November 19). *Black-box identity testing for affine orbits of read-once oblivious algebraic branching programs* (Version 1, Hexagon 2611.00634v1) [Unrefereed preprint]. https://hexagonmath.org/2611.00634v1

Primary PDF: https://hexagonmath.org/pdf/2611.00634v1 . Read Theorem 3.2 and Lemmas 3.3–3.6 completely, printed pp. 5–7, and the interpolation-pair construction in §3.4, pp. 9–10. Independently derived the profile-{0,2,3} support-four specialization and reviewed the complete standalone I-21 proof. P-12 uses that proved specialization, not an acceptance of the entire preprint. No full general-width, affine-orbit, or later-section certification is claimed. The host explicitly labels this primarily AI-generated text and marks no parts human-understood; version1 is CC BY4.0. Its provenance describes OpenAI-assisted formulation, proof development/review, drafting, and checks. This is a Hexagon identifier, not an arXiv identifier. The host policy says dissemination is not a correctness/novelty judgment: https://hexagonmath.org/about . Web refs inspected here: turn877817596view0, turn754880818view0, turn830526403view0, turn643684521view1.
