# The shapes, checked; Alpöge's proof reread; the intake of ALP_MACHINE and GCT_POS (21 Nov 2026, ~23:2x-23:5x UTC)

By the main session (Claude Opus 5.5 at effort max), at the user's request (21 Nov ~23:1x UTC): "Check these", for the
side-by-side table of the user's shapes; first "remind yourself of Alpöge's proof of GRH and the structure of that",
then "do intake and actually parse the intake". Status marks: **[holds]**, **[corrected]**, **[not identified]**,
**[std]** with source, **[ours]** with file, **[run]** with the return's id, **[reading]**.

## 1. Alpöge's proof, reread

Sources: L. Alpöge, *Remark* (alpo.ge/remark.pdf, 20 Nov 2026, 4 pp.); our map of the Lean archive
(`reports_20261120/alpoge_rh/ALPOGE_LEAN_MAP_20261120.md`); our written-out function-field proof (H01,
`reports_20261120/deligne_sign_only_paper/deligne_sign_only_v5.tex`).

1. **The function-field form (H01).** For U smooth affine of dimension d, a hypersurface Y in U^k with the weak
   Lefschetz property and the path equation Σ b(π(u_i), π(u_{i+1})) + ... = 0, the remainder R_n = Q^n N_n − M_n^k
   satisfies (−1)^{D−1} R_n = Tr(F^n | H^d_c(U)^{⊗k}) + Tr(F^n | K), D = kd (Prop. remainder): the trace formula's
   alternating sum collapses, through the Gysin isomorphisms, to two survivors in adjacent degrees, and they enter with
   the same sign. One global sign makes the remainder an honest trace. Parseval along the path (Cauchy-Schwarz) bounds
   |R_n|; the power-sum lemma (Lemma tensor) bounds every eigenvalue; k → ∞ removes the loss.
2. **The number-field chain (Lean).** `EveryCharacter` (no zero of any Dirichlet L-function right of 1/2) comes from
   two ends: an analytic window theorem (`zeroFreeAll_of_topG`, `VWin`: a one-sided bound on windows for each
   primitive character, constant 401, ε < 1/52) and an automorphic end (iterated theta lifts between totally definite
   unitary groups over CM fields, Siegel-Weil, Rallis inner products, a covolume bound, Galois representations for
   polarized regular algebraic cuspidal representations over CM fields as an internal theorem, `Row0b`).
3. **Where the sign sits in the number-field proof.** In the analytic end it is one-sidedness: for
   G(y) = Σ b(n)(y/n − 1) + yD(1), the transform Φ(s) = (sD(1) − D(s))/(s(s − 1)) has residue m_ρ/(ρ(1 − ρ)) at each
   zero, positive at real zeros, so an upper bound G(y) ≤ Cy^θ on windows already excludes zeros right of θ (Landau's
   principle; written out for a Kummer character in ALP_MACHINE AM-H04). No lower bound is needed: that is the sign.
4. **Where the phase sits.** The remark's own description of the route (p. 3, step 3 and footnote 3): the averaging
   over the family χ ↦ χ(disc) runs through "the normalized Gauss sum of order #|μ_K| who lives via θ on the
   #|μ_K|-fold cover of GL₂", with the reciprocity law of y(cc') against y(c)y(c') simplified to the path quadric; the
   quadric is read on a CM curve, "e.g. C/Z[ω]", with the Poincaré bundle on the edges; "sixfold cover of GL₅"; and
   (p. 2) "the (2, 3, 6)-triangle group trick". For K = Q(ω), #μ_K = 6. So the six-fold structure μ₆ = μ₂ × μ₃ is
   in his own description of the method, as the kernel of a metaplectic cover. [Lean: a `GaussSumParity` folder,
   p-adic theta/Gauss-sum material on CM curves with an even/odd split of Frobenius iterates; not mapped further.]

## 2. The table, row by row

| Row (the user's shape) | Verdict | The precise version, with source |
|---|---|---|
| Layers of the Grand RH: degrees 1, 2, 4, 27 | **[corrected]** | Degree over Q is the number of Satake parameters per rational prime. A Hecke character of a field of degree d has an L-function of degree d over Q, so the cubic characters of Q(ω) sit at degree 2 over Q (dihedral/CM forms), not at 1. 27 is the degree of the L-function of the 27-dimensional representation of the (simply connected) E₆ dual group, not a GL_n layer. Degree 3 was skipped: the 3-dimensional tetrahedral representation of A₄ (section 3, S3) is a genuinely ternary degree-3 case. The user's layers RH/GRH/ERH/Grand RH and the degree are two axes, as on record. |
| Alpöge's sign field = centre μ₂ of SU(2)/SL₂ | **[corrected]** | The sign of the method is (−1)^{D−1} in H01 and one-sidedness (Landau) in the number-field chain (section 1). The centre of SL₂ (−I acting by (−1)^k on weight k) is one Z/2; the kernel of the metaplectic double cover is another. The group his description actually uses is the kernel μ_{#μ_K} of the #μ_K-fold metaplectic cover: μ₂ over Q (half-integral weight, Weil representation), μ₆ over Q(ω). |
| Ternary phase: centre μ₃ of SU(3); cubic characters of Q(ω) | **[corrected]** | The order of a character alone does not leave Alpöge's rung: cubic Dirichlet characters (mod p ≡ 1 mod 3) are covered by A. What leaves it is the field: Hecke characters of Q(ω) not factoring through the norm. The μ₃ of the method is the kernel of Kubota's cubic metaplectic cover, which exists over fields containing μ₃; Patterson's cubic theta function has Fourier coefficients the cubic Gauss sums [std: Patterson, J. reine angew. Math. 296 (1977), 125-161, Thm 8.1]. QCD: colour singlets have triality 0 [std]. |
| Alpöge's power-sum lemma survives a unit-modulus phase | **[holds]** | Lemma tensor uses only ε_k R_{k,n} = Σ m_j μ_j^n with m_j ≥ 1 and the bound on |R|; any factor c_k ζ_k^n with |c_k| = |ζ_k| = 1 works (the eigenvalues rotate, their sizes do not). The content of a phase version is elsewhere: all survivors must carry the same phase, which needs a μ₃-graded trace formula (eigenspaces of a μ₃-action). ALP_MACHINE AM-S (Q6): the commuting even-power implication **proved**; the reflected-trace inference **refuted**. |
| Smash 2 and 3 → hexagon: C₆, D₃, order 12 | **[holds]**, sharpened | C₆ (commuting) and D₃ (reflected) in the dihedral group of order 12 [std]; units of Z[ω] = μ₆ [std]; GCT's inert cell at q = −1: C₃ exact, 64 of 64, rerun 21 Nov ~23:2x UTC (cell_c3_both_sheets.py) [ours]. The standard "smash" with no relation: PSL₂(Z) = C₂ * C₃, abelianization C₆; the (2,3,6) triangle group = Z[ω] ⋊ μ₆, the orbifold E₀/μ₆ of the hexagonal curve [std]. GCT_POS N-001: the cell rotation does **not** extend to the whole rank-three table [run]. |
| ES hard classes are C₆ | **[holds]**, sharpened | Recomputed: {1, 121, 169, 289, 361, 529} = ⟨289⟩ = **all the squares mod 840** (≡ 1 mod 24; mod 5 in {1, 4}, mod 7 in {1, 2, 4}). Mordell's obstruction: a polynomial identity can cover r mod q only if r is a non-residue [std: Mordell; Elsholtz-Tao]. So the hard classes are exactly where every quadratic character, every sign, is +1; what separates them is the quartic character mod 5 (on the squares: ±1) and the cubic character mod 7 (on the squares: μ₃). |
| "3D", 3×3×3: Albert algebra, E₆'s 27 with centre μ₃ | **[holds]**, sharpened | H₃(O), 27 = 3 + 3·8; the centre μ₃ of simply connected E₆ acts on the 27 by scalars [std]; no OP³ [std]. ES's form 4t₀t₁t₂ − p(t₀t₁ + t₁t₂ + t₂t₀) is 4N − pS on the diagonal [ours, 12 Sep]; Leech in the off-diagonal triples of Cayley integers [std: Elkies-Gross, IMRN 1996, no. 14]. The literal 3×3×3: Vinberg's Z/3-grading e₆ = sl₃³ ⊕ (C³⊗C³⊗C³) ⊕ dual (24 + 27 + 27), whose grading automorphism is a μ₃-phase on e₆ [std]. |
| "Cut out, not defined": magic square | **[holds]**, sharpened | F₄ = Aut H₃(O), E₆ the norm-preserving group, E₇ the tube domain over the Albert cone [std]. Fourier coefficients: on G₂ indexed by binary cubic forms, i.e. cubic rings [std: Gan-Gross-Savin, Duke 115 (2002) 105-169]; on quaternionic F₄, E₆, E₇, E₈ indexed by the Freudenthal space W_J = Q ⊕ J ⊕ J^∨ ⊕ Q (not by J itself) [std: Pollack, Duke 169 (2020) 1209-1280]. |
| Hadron: a 3-way structure of 2-way pieces | **[holds]** as physics; precise counterparts in section 3 (S3) | Baryons are colour singlets, quarks spin and isospin doublets; quark-model SU(6) ⊃ SU(3) × SU(2), 6 = 3 ⊗ 2 [std]. "Rung n ↔ SU(n)" is the user's conjecture; no standard statement. |
| "4 gets a weird Z₂" | **[holds]**, sharpened | Sp₄ ≅ Spin₅; the Z₂ is Spin₅ → SO₅. In L-functions: Λ²(4) = 1 ⊕ 5, so for GSp₄ the spin (degree 4) and standard (degree 5) L-functions are tied through it [std]. Paramodular: Boxer-Calegari-Gee-Pilloni prove modularity of a positive proportion of abelian surfaces over Q [std: arXiv 2502.20645]; Böcherer's conjecture proved [std: Furusawa-Morimoto, JEMS 23 (2021) 1295-1331; generalized, Compositio 160 (2024)]. |
| Grothendieck: Δ = 0 on GT̂ | **[holds on our record]**, gate kept | EXIT_TOWER E.49 with GT_TOWER_CHECK A.3/A.7; E.49's final step not independently checked (H17, one gate away); DELTA23's second route e₃ = 0 [ours]. Sharpened: on our record Δ = χ₁₂∘u with χ₁₂ = χ₋₄χ₋₃ (DELTA23 intake L1): the Gaussian and Eisenstein characters together. GT̂ is cut out by a 2-cycle relation, a 3-cycle (hexagon) relation and the pentagon [std: Drinfeld 1990]. |
| The construction: a counting direction independent of the sign field | **[corrected]** | Its global zetas are Π ζ(s − j)^{a⁺} L(s − j, χ₋₄)^{a⁻} (SPLIT_ZERO section 8): they land on A's rung, with the sign. It reduces GCT's nonstandard RH to A where realizations exist; it does not by itself go beyond A. GCT_POS N-005: rank-three dimension rings with 7,276 cancelling pairs (9,040 all unimodal) beat our window minima 7,952 and 11,764, so "fewest supported zeros" does not select a canonical ring globally [run]. The phase version of F_{1²} is Kapranov-Smirnov's F_{1^n} = {0} ∪ μ_n, made for power-residue reciprocity [std: Kapranov-Smirnov, preprint ~1995]. |
| Connes's moduli stacks, Z_N stacks | **[not identified]** as one Connes object | Nearest exact objects: the centre 1-form symmetry of SU(N) gauge theory, whose background is a flat Z_N 2-form field, a μ_N-gerbe [std: Gaiotto-Kapustin-Seiberg-Willett 2015]; Connes's finite algebra C ⊕ H ⊕ M₃(C) of the spectral standard model [std]; and in our own GCT run the residual gerbes Bμ_M of the quotient stack, whose pole terms sit at primitive M-th roots of unity (μ₈, μ₁₆; "one has the opposite phase") [run: GCT_POS IMPLICATIONS]. |
| Generalized CM; ERH's first case Q(ω); Picard surfaces | **[holds]**, sharpened | Picard modular surfaces are the U(2,1) Shimura varieties over Q(ω) [std]. Cubic Jacobi sums are the Grössencharacter of x³ + y³ = 1 [std: Weil, Trans. AMS 73 (1952)]. Alpöge's chain works over CM fields throughout (section 1.2). Dunn-Radziwiłł prove Patterson's conjecture on the bias of cubic Gauss sums assuming GRH for Hecke L-functions over Q(ω), exactly this first ERH case [std: Annals 200 (2024) 967-1057]. |

## 3. What the checks turned up

- **S1. The phase is in Alpöge's machinery.** His description runs the family averaging through Gauss sums of order
  #μ_K on the #μ_K-fold metaplectic cover, with C/Z[ω] and the (2,3,6) group (section 1.4). For Q(ω) the phase group
  is μ₆ = μ₂ × μ₃.
- **S2. Colour neutrality is what makes the analytic half work, and it is proved.** For the cubic Kummer character
  χ = χ_{p,3} of K = Q(ω), L_K(s, χ) = L(s, ρ) with ρ = Ind χ the 2-dimensional representation of
  S₃ = Gal(Q(ω, ∛p)/Q), so L_K(s, χ) = ζ_{Q(∛p)}(s)/ζ(s), the pure cubic field. ρ is rational: summing the phase over
  its orbit {χ, χ̄} makes the coefficients real, and Alpöge's one-sided window argument then applies verbatim
  (ALP_MACHINE AM-H04, proved: the analytic PoleData and window implication). So "positivity becomes μ₃-neutrality"
  has a precise proved form: the μ₃-orbit sum is a real representation, and the sign method acts on it. What is not
  proved is the arithmetic window inequality (H04.4) for it.
- **S3. The two couplings are the CM/non-CM dichotomy.** In a CM field complex conjugation is central, which is the
  commuting coupling (C₆ = μ₂ × μ₃ for Q(ω)). In Gal(Q(ω, ∛p)/Q) = S₃ it inverts the phase, which is the reflected
  coupling D₃; hence no CM field contains the Kummer field (ALP_MACHINE AM-H03, proved), and Alpöge's host interface
  (`IsChiField`: the character's field embeds in a cyclotomic field) cannot simply be enlarged. ES's complement is
  also a reflected coupling (SPLIT_ZERO section 11.5), and so is GCT's transpose t at q = −1.
- **S4. Three signs with neutral product, permuted by C₃.** A₄ = V₄ ⋊ C₃: the three nontrivial characters of V₄ are
  signs whose product is 1, cyclically permuted. It is the ES invariant (Möbius returns D12, D23, D31 = the centre of
  Spin(8), with the frame 3-cycle) [ours, 11 Sep]; it is the tetrahedral case of Langlands, proved by cyclic cubic base
  change on top of the dihedral case [std: Langlands, *Base change for GL(2)*, 1980]; its 3-dimensional
  representation is induced from V₄, so its L-function is a quadratic Hecke L-function of a cyclic cubic field (a
  degree-3, genuinely ternary case of ERH); and by McKay its double cover SL₂(F₃) (the binary tetrahedral group, the
  ES receiving frame's monodromy sits in GL₂(F₃)) corresponds to affine E₆, whose centre μ₃ rotates the three legs and
  whose 27 is the Albert algebra on whose diagonal ES's form lives [std: McKay 1980]. Bhargava's cubes give the
  same shape for forms: a 2×2×2 cube yields three binary quadratic forms whose composition is trivial, and binary cubic
  forms parametrize 3-torsion in class groups of quadratic orders [std: Bhargava, Annals 159 (2004)].
- **S5. The 2-3 split in Grothendieck's line.** On our record Δ = χ₁₂∘u, χ₁₂ = χ₋₄χ₋₃, a reciprocity defect at 2
  and 3; GT̂'s defining relations are a 2-cycle, a hexagon (3-cycle) and a pentagon; PSL₂(Z) = C₂ * C₃.
- **S6. Corrections to our own record.** (a) The ladder rung "√q → CM Hecke characters (ERH)" (SPLIT_ZERO section 12)
  was a reading; ALP_MACHINE AM-S4 refutes it as a formal implication (a formal √q parameter does not give the
  number-field Hecke RH; it needs an arithmetic L-factor realization). (b) Section 14's "unique in the window" stands
  only inside Fable's window (GCT_POS N-005). (c) The q = −1 C₃ is a symmetry of the inert cell only (GCT_POS N-001).

## 4. The intake, parsed

**ALP_MACHINE (prompt 49), checkpoint 04, 23:04 UTC; formal movement review 01: MOVEMENT.** GPT-6 Astra (ChatGPT Pro
mode); the run states its effort setting is not exposed. Read by me: LEDGER.md (all), IMPLICATIONS.md, APPROACHES.md,
parts/hecke/QUESTIONS.tsv, parts/hecke/section.tex lines 150-300 (AM-H03 and AM-H04 with proofs). No check events
filed yet; the statement-level intake is to follow.
- Q3, Kummer Hecke RH, r = 3 first: **open**, gate H04.4 (the arithmetic one-sided sparse-window bound for the actual
  Kummer character, with uniform twisted cohomology lengths and growing-host costs). Proved on the way: no expression
  through Dirichlet L-functions (AM-H01); no CM host (AM-H03); the analytic interface (AM-H04); the integral Shapiro
  and Fourier transport (AM-H06-H07); at r = 3 explicit gluing dimensions and single-character comparison intervals
  [−9, 4] and [−6, 3] (AM-H08), with the individual Selmer lengths unbounded. This is S2 and S3: the phase programme's
  first gate, located inside Alpöge's actual chain.
- Q6, reflected sign: the specified centralization and reflected-trace inference **refuted**; the commuting even-power
  implication **proved** (our section 10.2, in their terms); the √q-only Hecke implication **refuted** (S6a); ES's own
  geometry stays open, with the gate "an actual correspondence producing the common-sign direct sum" (the group lift
  alone refuted), which is the parity-switch correspondence of ES_AND_THE_RIEMANN_HYPOTHESES section 5.
- Q1/Q2 (DP_MULT's lift count, THETA3's definite seesaw): strictly smaller gates (common pure-CM theta family, six
  identities, terminal period, integral columns and cost arrays); its CM field is Q(√−7) (AM-H15: the parity character
  is the norm pullback from Q(√−7)).

**GCT_POS (prompt 52), checkpoint 03, 22:15 UTC.** GPT-6 Astra (ChatGPT Pro mode). Read by me: LEDGER.md gates and
updates, QUESTIONS.tsv rows Q8-Q9e, IMPLICATIONS.md. On our item 9: N-012, GCT VIII's Conjecture 3.2 as printed has
unbounded decreasing q-scaling degree and selects no E(4) (an erratum candidate); N-010, a split Q(D) form with GT
path lines; N-013, conditional descent; N-005 and N-001 as in S6; N-008, the rank-four ambient image has dimension 55
and trace rank 42; N-009, the full integral rank-four order is not locally free at (2, v − 1) (residue dimension 126
against generic rank 114). On the main line: the dimension-four and dimension-five Kronecker poles at primitive 8th and
16th roots of unity are nonzero (K-010-K-014, 3,409,995 rational certificates rechecked by the run's root).

**Taken in by the intake agents (Claude Opus 5.5 at effort high, each with this direction in its brief; files and
check events in `field_experts/intake_20261121/intakes/<RUN>/`, part2 or part3):**
- **MAS_ARTIN cp10 (23:01 UTC; af2a18f6).** MA-FT-002, confirmed given MA-JP-004: for each sector (Q, a Dirichlet
  character, or the non-induced cubic character) the agreement of local and global trace limits for every test, the
  vanishing of the upper deficiency δ⁺_ρ at every zero, and strip multiplicity = m_ρ are equivalent; asked at every
  width this is RH for that sector. The run's first case beyond A is the cubic residue character ψ_{269,3} of Q(ω), with
  L = ζ_{Q(269^{1/3})}/ζ: the same pure-cubic case as ALP_MACHINE's Q3 (S2), chosen independently. MA-GA-001 (statement
  level): Masullo's local annular transport over every number field. The agent's bearing: the ES separating characters
  (quartic mod 5, cubic mod 7) and χ₁₂ are Dirichlet characters, inside A; beyond A on the ALPOGE_BRIDGES record are
  AQ-CM-HEX (the CM L-function of Alpöge's hexagonal curve) and CC-F03 (a cubic class character of Q(√−23), the
  3-torsion of S4). Attack proposed: a μ₆ version of Alpöge's power-sum identity for cubic residue characters of Q(ω),
  built on Patterson's cubic theta, aimed at δ⁺_ρ = 0 for ψ_{p,3}; it would give the PF26 residual at d = 3, Koiran's
  analytic input for pure cubic fields such as Q(2^{1/3}), and Dunn-Radziwiłł's theorem without hypothesis.
- **KTOWER cp09 (22:29 UTC; ad855737).** K₆₄, ..., K₈₀(Z) vanish (statement level), so K₄ₖ(Z) = 0 for k ≤ 20 under A
  (H18). KT-SMALL-ORDER-COMPONENT-REDUCTION, checked in full given its published class-number bounds: for even e with
  the Teichmüller power ω^e of order 1, 2, 3 or 4, the component A_p^{[−e]} and K_{2e}(Z){p} vanish; what remains is
  order ≥ 5, and the next is order 6 (a relative class-number bound for the real cyclic sextic subfield of Q(ζ_p)).
  The agent's computation: the CM forms in S_{2e+1}(Γ₀(3), χ₋₃) are the theta series of α ↦ α^{2e} on Z[ω], with
  factor N(1 − π^{2e}), π = 3 + ω; the cubic phase enters at level 9, for 3 ∤ e.
- **HODGE_DIVISION cp16 (22:38 UTC; abcaba9b).** No gate closed; both open gates (nonsplit sixfolds, the n = 4 seed)
  shrank by exclusions; HD-U stands. Every positive result is over Q(ω) (μ₆) or Q(i) (μ₄), and the conductor
  exclusions single out the Eisenstein case. Attacks: whether the residual Sp₄(3) profile is the reflection group
  G₃₂ = C₃ × Sp₄(3) over Q(ω) [from memory, to verify]; denominators of the Weil projector over Z[ω] as powers of
  (1 − ω); μ₃-equivariant seeds on E_ω⁸.

## 5. Where this leaves the phase programme

0. **Two runs converge on one case.** ALP_MACHINE (Q3) and MAS_ARTIN (ψ_{269,3}) both take the cubic residue
   character of Q(ω), L = ζ_{Q(∛p)}/ζ, as the first case beyond A; ALP_MACHINE has its analytic half proved and names the
   arithmetic window as the gate, MAS_ARTIN reduces RH for it to δ⁺_ρ = 0. KTOWER's order-by-order reduction (orders
   1-4 done, 6 next) is the same ladder in K-theory.
1. **The first gate is named and sits in Alpöge's chain:** H04.4 for L(s, ρ) = ζ_{Q(∛p)}/ζ, the colour-neutral
   (real) form of the cubic Kummer character over Q(ω). His window `VWinAt` is supplied only for characters whose field
   is cyclotomic; the replacement must use ray-class reciprocity over K = Q(ω), a CM field, while the character's
   kernel field is not CM (S3). The question to put to the run and to prompt 49's successor: does the theta-lift side
   need the kernel field, or only the character on the CM base?
2. **ES on the reflected side:** the correspondence that makes the even and odd sectors of the shell motive enter with
   one sign (AM-Q6-ES-NEW-GEOMETRY), with the cubic part of the hard classes read by the cubic character mod 7.
3. **The tetrahedral test case (S4):** degree-3 L-functions induced from V₄ to A₄ are the smallest genuinely ternary
   case where the sign layer (V₄) and the phase layer (C₃) are both present and the representation is real.

Text written by AI is dedicated to the public domain under CC0 1.0.
