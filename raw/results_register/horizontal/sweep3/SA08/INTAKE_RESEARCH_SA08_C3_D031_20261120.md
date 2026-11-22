# Intake of RESEARCH_SA08_C3_D031 (checkpoint 08): C.3 over Z, and the check of Caradot-Lin, Prop. 3.10 (D-031)

## 0. Return and scope

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt `pro_prompt_builds/RESEARCH_SA08_C3_D031/PROMPT.md`.
  That prompt was built on 19 Nov 2026 by Claude Opus 5.5 at effort max (agent a34c04448e8299803); its send folder is
  `TO_SEND/PRO/1_Archive_research_by_topic/14_SA08_C3_and_Caradot-Lin_check_day`.
- **The return read:** checkpoint 08,
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped`.
  - Its report opens with INCOMPLETE.
  - Its register, `RESEARCH_SA08_C3_D031_results.csv`, has 112 rows by run status: 104 proved, 3 known, 3 open and 2
    refuted.
- **Brief and rows.** The brief is `field_experts/intake_20261120/INTAKE_BRIEF.md`. My rows are all 112 rows of the
  run:
  - `PACKET_10`: AT21 ... AT11;
  - `PACKET_11`: AT12 ... B-001;
  - `PACKET_12`: B-002 ... A-L21.

  They hold about 16,300 proof lines in all.
- **Taken in by** Claude Opus 5.5 at effort max, agent a34c04448e8299803, on 20 Nov 2026, about 19:15-19:30 UTC. This
  agent built the prompt and took in its inputs (`SA08/INTAKE_RESEARCH_SA08_20261119.md`,
  `SA09/INTAKE_RESEARCH_SA09_20261119.md`).
- **Scope.** This is final, written on 20 Nov 2026 at about 21:15 UTC. The intake stopped under a 50,000-token cap set by
  the main session.
  - **Read in full and checked:**
    - B-001 (D-031), with its proof and its source: arXiv:2511.22614v4, §2.1, §3.5 Prop. 3.10 and its proof, and
      Theorem 3.15;
    - a search of the whole HTML text of v4 for citations of Prop. 3.10;
    - B-003 and B-004 (the corrected lifting criteria), with their proofs.
  - **Checked in part:**
    - B-006 and B-008 (the reach of D-031), against the source;
    - A-WF02 and A-L10, at the level of their printed statements, for the bridges (section 4).
  - **Statement level only**, from the register statement, the run status, the run's own check events and the report's
    outcome table: the other 107 rows. That is all of Part A, and B-002, B-005 and B-007.
  - **Not reached:**
    - the proofs of Part A, about 15,000 lines;
    - B-002, the free PD algebra with the extension bijection (B.4), on which the PD clauses of B-003 and B-004 rest;
    - the proofs of B-005 to B-008.
  - **Earlier intakes:** the sort (`SORTED/RESEARCH_SA08_C3_D031.tsv`, column earlier_intake) records none for any row
    of this run, so none is cited.

## 1. Verdicts

**Counts:**
- 3 rows confirmed with their proofs read in full: B-001, B-003 and B-004;
- 2 rows confirmed in part (the reach of D-031): B-006 and B-008;
- 107 rows not read in full, at the level of the statement;
- no gap found and no row refuted, within that scope.

**Part B: D-031 is confirmed.** Proposition 3.10 of Caradot and Lin is false as stated, over every nonzero ring.
- **The source.** §2.1: "We say that (M^*,d^*) is A-free if M^i is a free A-module for all i". This is a cochain
  convention, with d of degree 1.
- **Prop. 3.10** (§3.5):
  - Hypotheses: π: A'^* → A^* is a morphism of PD dg algebras, with PD dg ideals I' and I, "with the restriction
    π: I' → I being surjective".
  - Conclusion: "for any X^* ∈ Cplx(A)^free and any homomorphism ρ: X^* → I of complexes, there is a homomorphism of PD dg
    algebras ρ̃': TS_A(X^*) → A'^* such that ρ̃ = π ∘ ρ̃'".
  - Its proof: "As X^* is assumed to be free, there exists a lift ρ': X^* → I' such that ρ = π ∘ ρ'".
  - The run's rendering (B.1) is exact.
- **The counterexample, rechecked.** Take R' = k ⊕ E with E^{-2} = ku, E^{-1} = kv and du = v. Take R = k ⊕ kε, with
  ε in degree −2.
  - The ideals are square-zero, with γ_n = 0 for n ≥ 2. Every PD identity holds; for example dγ_2(u) = 0 = u·v.
  - π(u) = ε, π(v) = 0 is a PD dg map, surjective on the ideals in every degree.
  - X = kε is termwise free, and ρ = id.
  - A lift must send ε to cu with c = 1 (because of π) and with cv = 0 (because it is a chain map), so 1 = 0.
  - The failing step is the source's sentence quoted above. Termwise freeness gives a graded lift, not a chain lift.
- **Reach.**
  - Theorem 3.15 assumes that p^*: Q^* → A/I is a quasi-isomorphism, with Q^n = 0 for n > 0. Its visible proof does not
    use Prop. 3.10.
  - The text from §3.6 on cites Prop. 3.10 nowhere.
  - The π of D-031 is not a quasi-isomorphism: H(R') = k, while H(R) = k ⊕ kε. So Theorem 3.15 is untouched, as the run
    says (B-006, B-008).
  - Not checked: citations of Prop. 3.10 between Prop. 3.10 and Theorem 3.11; the proofs of B-003 and B-004 (the
    corrected criteria: contractible X for all such surjections, K-projective X for surjective quasi-isomorphisms); and
    B-005 to B-008.

- **Citations of Prop. 3.10.** These were checked on 20 Nov 2026, about 20:4x UTC.
  - A search of the whole HTML text of v4 (characters 0-157,000, in two fetches) finds Prop. 3.10 only in its own
    statement and proof (§3.5). Its proof cites Theorem 3.9.
  - Nothing in §3.6 cites it, before Theorem 3.11 or after, and neither do the later sections or the introduction. The
    abstract speaks of "many lifting properties" of the resolution in general.
  - So within v4 no other result rests on Prop. 3.10. D-031 reaches that proposition alone, and Theorem 3.15 has its own
    proof.
- **The corrected criteria B-003 and B-004 are confirmed:** targeted proof checks of both proofs in full,
  `sections/B_lifting_audit.tex` l.265-382.
  - **Setting.** π is surjective on the ideals, X has projective terms, ρ: X → J is a chain map, and
    K = ker(J' → J).
  - **B-003.**
    - For any graded lift g, the defect dg − gd lands in K. It is a cocycle of Hom_k(X, K), and its class
      o(ρ, π) ∈ H^1 Hom_k(X, K) does not depend on g: changing g by h ∈ Hom^0(X, K) changes the defect by ∂h.
    - Chain lifts exist exactly when o(ρ, π) = 0. They then form a torsor under the degree-0 cocycles of Hom(X, K).
  - **B-004 (1).** X lifts every chain map through every degreewise surjection if and only if X is contractible.
    - Necessity: the cone C(X) → X, (a, b) ↦ a, is degreewise surjective. A chain section s of it gives the contraction
      p·h_C·s, since d(p h_C s) + (p h_C s)d = p(d_C h_C + h_C d_C)s = 1.
    - Sufficiency: for a contraction h and a graded lift g, ℓ = dgh + ghd = ∂(gh) is a cocycle, and qℓ = ρ(dh + hd) = ρ.
  - **B-004 (2).** X lifts through every surjective quasi-isomorphism if and only if X is K-projective.
    - Sufficiency: the kernel of such a map is acyclic, so the class (B.7) vanishes.
    - Necessity: for acyclic Y the cone map C(Y) → Y is a surjective quasi-isomorphism, so every map from X to every
      shift of Y is null-homotopic.
  - **The PD forms.** Necessity comes from the square-zero functor S(Y) = (k ⊕ Y, Y, γ_{>1} = 0), sufficiency from the
    extension bijection (B.4).
  - **Not checked:** (B.4), which is B-002, and the cited Stacks Project Lemma 13.19.4, the standard fact that a
    bounded-above complex of projectives is K-projective.
  - **What they are.** These are the standard lifting properties of complexes: contractible complexes of projectives
    against all surjections, and K-projective ones against surjective quasi-isomorphisms. Here they are proved for the
    PD dg algebras of the source, so they give the corrected Prop. 3.10.
  - **In the example of B-001,** K = kv in degree −1, and (B.7) is the class of ε ↦ v, which no degree-0 element of
    Hom(X, K) can kill.

**Part A: C.3 is undecided at checkpoint 08.** This is at the level of the statement, from the run's outcome table.
- **Common sources over Z.** A-S09-29 reduces them exactly to countable sources and targets internal to E_ω^[d], with
  the single-disk first skeleton, global comparison through d, and rows through d+2 exact from the cutoff.
- **Terminal localization.** A-S09-30 proves it equivalent to the all-arrow localization of F_3,ω^[d].
- **SA09's tools.** RESEARCH_SA09's A2.2, A3.1 and A3.2 are re-proved (A-S09-01 to A-S09-03). Their application to
  arbitrary admissible theories is open (A-SA09); A-S09-04 refutes the raw row test.
- **Specified routes refuted:**
  - IC01-03, A-L01-03 and A-S09-09-12;
  - A-L07, A-S09-06-08, AT11-12 and A-S09-15;
  - A-L09, A-L11-12, A-S09-22 and A-S09-23;
  - A-WF01-02, A-S09-25, A-S09-26, A-S09-28 and AT28.
- **Repairs proved within stated ranges:**
  - AT01-27, A-SAT01 and A-P01;
  - A-L20-21, A-004-006, A-S09-24, A-S09-27 and A-S09-31.
- **Open:** A-CS, A-TL and A-SA09.

None of the Part A proofs was read by this intake.

**Part A, the main results at the level of the statement** (with "used by n", the number of rows that rest on each):
- **A-SAT01 (used by 7).** Countable PD closure and based saturation inside the fixed rational algebra kill all H^1
  above one fixed cutoff. They extend every specified torsion-free target map, and fix simplex 1 when it is integrally
  exact.
- **AT16 (used by 6).** An actual K(2)-parameter coefficient-tail quadratic repair, with simultaneous target maps by
  Ext^2(L/mL, S) = 0, a rational contraction, and a torsion-free quotient that leaves simplices 0 and 1 unchanged.
- **A-S09-24 (used by 5).** For each fixed d, both integral questions reduce to the proper full subcategory C^[d], with
  the free first skeleton and the coefficient comparison through d, by weight-tail functors and finite-word localization
  equivalences.
- **AT01 (used by 5).** The pure completed arithmetic sequence and its exact graded coefficient extension.
- **A-S09-27 (used by 4).** For each fixed d, the common-source assertion is equivalent to internal common sources in
  the proper full subcategory E^[d], with one common P(N).
- **A-004 to A-006 (A-004 used by 3).** Every admissible theory has an actual admissible replacement with a prescribed
  common free first skeleton, functorially (the functor R and natural transformations).
- **A-S09-09 and A-S09-12.** The cellular free simplicial PD resolution of S/I_2 has special cotangent π_2 elements of
  exact order p in weight 2p for every odd p; its weight-6 π_2 is Z/3. For every N ≥ 2, every p > 3(N−1) and every
  k ≥ 1, there are nonzero p-local classes in degree 2k−1 and weight p^k.
- **A-P01, A-L20, A-L21.** Exact order-p classes surviving every based saturation, at every prime, each with an actual
  next repair.
- **A-WF01 and A-WF02.** The de Rham-Witt completion kills the positive-weight coefficients (section 4).
- **The two gates.**
  - **A-S09-29:** common sources over Z are equivalent to common sources for countable sources and targets internal to
    E_ω^[d]. These keep the single-disk first skeleton, global comparison through d, and rows through d+2 exact from the
    cutoff; the target pair can share N.
  - **A-S09-30:** terminal localization over Z is equivalent to terminality in the all-arrow localization of
    F_3,ω^[d], whose countable objects have one, two or three first-skeleton disks per weight, global comparison through
    d, and one common row cutoff.
  - **What is open:** both gate assertions themselves (A-CS, A-TL), and the application of SA09's structures (A-SA09).

**Row by row:** see the appendix, generated by `intake_scripts/c3_d031_row_table.py` from
`SORTED/RESEARCH_SA08_C3_D031.tsv`. For each row it gives the id, run status, statement, proof locator, the run's check
events and the intake verdict.

## 2. What is new

- **Against the literature.**
  - B-001 refutes Prop. 3.10 of arXiv:2511.22614v4 as stated. Theorem 3.15 is not affected.
  - The corrected criteria B-003 and B-004 are checked (section 1). As statements about complexes they are the
    standard lifting properties: contractible complexes of projectives against all surjections, and K-projective ones
    against surjective quasi-isomorphisms. What is new is their PD form for the algebras of the source, which is the
    corrected Prop. 3.10. Prop. 3.10 itself is used nowhere else in v4.
- **Against our own results.**
  - D-031, found by RESEARCH_SA08, is now confirmed twice: by this run's B-001, and by this intake against the source.
  - For C.3, the gates are sharper than RESEARCH_SA08's C30, C32 and C34: exact reductions to countable proper
    subcategories (A-S09-27, A-S09-29, A-S09-30).
  - The run re-proves RESEARCH_SA09's A2.2, A3.1 and A3.2 independently. The SA09 intake had read A3.2 in full
    (INT-SA09-E08).

## 3. Implications

- **For the archive** (cote 136, scans 117-121): his uniqueness conjecture stays open over Z in both of its non-strict
  forms. Its strict form b) was already refuted (RESEARCH_SA08, C07). This checkpoint makes no claim about the ink of
  cotes 136 or 137.
  - [Cite ALPOGE_BRIDGES AQ-136-STRICT in place of C07, whose proof was never supplied: the strict form of (b) is false
    over every nonzero ring, Z included, by an explicit square-zero extension D = B ⋉ M with j₁ = (id, δ), δ the universal
    relative PD derivation (confirmed in the ALPOGE_BRIDGES part-2 intake). Reading caveat: the sheet writes « qui
    'égalise' » in quotation marks, so say "the strict form of (b) is false"; the homotopy form is not decided.
    (corrected 21 Nov 2026 after the intake of ALPOGE_BRIDGES part 2, Claude Opus 5.5 at effort high)]
- **For the programme.**
  - D-031 has now been checked, so the main session can decide whether to inform the authors (outreach plan).
  - The facts such a note can state are checked: Prop. 3.10 fails as stated, the counterexample, the failing step, and
    that Theorem 3.15 is unaffected.
  - B-003 and B-004 are checked, except for the extension bijection (B.4) of B-002. A note can therefore also
    state the corrected criterion: a chain lift exists exactly when the class (B.7) in H^1 Hom(X, ker) vanishes.
    The lift exists universally for contractible X (all maps surjective on the ideals), and for K-projective X
    (surjective quasi-isomorphisms).

## 4. Bridges

Criterion: step 4 of the brief as corrected on 20 Nov 2026. The road from Grothendieck's programme to the Riemann
hypothesis over finite fields runs here through the crystalline side:
- divided powers and crystalline cohomology (Berthelot);
- the de Rham-Witt complex (Illusie);
- Mazur's theorem that the Newton polygon lies above the Hodge polygon (Katz's conjecture), the p-adic face of the Weil
  bounds;
- Katz-Messing's proof that crystalline cohomology of smooth projective varieties over F_q satisfies Deligne's purity;
- Kedlaya's p-adic proof of the Weil bounds through rigid cohomology.

Below I state what the crystalline Frobenius, its slopes and purity (Deligne, *La conjecture de Weil* I, II) give for
the PD constructions of this run, and what its rows give back. Where a link carries nothing, I give the reason for that
row. RH and GRH are cited to Alpöge, *Remark*, 20 Nov 2026. The statements of A-WF02 and A-L10 are read in the paper;
their proofs are not.

**1. The coefficients are Tate twists; A-L10 is a slope bound.**

- **The Frobenius on the coefficients.** S = Γ_R(T), with T of weight one, is the integral homology of
  BG_m = CP^∞ (H_*(CP^∞; Z) is a divided-power algebra on the class of degree two). A Frobenius of the kind A-WF02
  classifies acts by F(T^[w]) = c^w T^[w] with c ∈ pR. For c = p, the weight-w line R·T^[w] is the F-crystal of the
  Tate twist (−w): its Frobenius is p^w, its slope is w, and it is pure of weight 2w.
- **What purity and Newton-above-Hodge give.** For Tate twists both hold with equality: |p^w| = (p)^{2w/2}, and the
  Newton slope w equals the Hodge level w (the ordinary case). So they fix the slope of weight w as w·v_p(c). This is at
  least w, with equality exactly when c/p is a unit.
- **The PD cochains of a simplicial set.** Their weight-w part is H^i(X; Z) ⊗ T^[w] (RESEARCH_SA08, R1, A-002, A-003),
  and the Frobenius acts on the coefficients only. Seen as the cohomology of a constant simplicial scheme of points over
  F_q, H^i(X) has Frobenius weight 0 in every degree: in Deligne's weight spectral sequence E_1^{a,b} = H^b(X_a)
  vanishes for b > 0. This is the situation of the dual complex of a semistable degeneration, Deligne's W_0. The
  Frobenius weight of H^i(X) ⊗ T^[w] is therefore 2w whatever i is. These are mixed Tate objects, and purity in the sense
  "H^i is pure of weight i" is not expected of them. Hence no row constrains an eigenvalue of a geometric Frobenius, and
  none is constrained by one.
- **A-L10 read through this.** The weight of a cotangent class is its slope divided by v_p(c). A-L10 then says: in a
  fixed homological degree n, the p-local special cotangent homology of S/I_N has slopes at most
  (N−1)(1+b_p(n))·v_p(c), where b_p(n) = max({n+1} ∪ {(n+2−2r)p^r : 1 ≤ r ≤ ⌊(n+1)/2⌋}).
  - This is a degree-wise slope bound, the PD-cotangent counterpart of the crystalline bound "the slopes of H^n lie in
    [0, n]". That bound comes from Newton-above-Hodge together with the symmetry λ ↔ n − λ, which purity gives.
  - The bound here grows like p^{⌊(n+1)/2⌋} instead of linearly in n. A-S09-12 shows that it cannot be made uniform in
    n: there are nonzero p-local classes in degree 2k−1 and weight p^k for every p > 3(N−1).
  - The row gives back this slope bound for the cotangent complex of a truncated divided-power algebra. Purity gives it
    only the normalization: slope equals weight when c = p.

**2. Frobenius saturation is the de Rham-Witt construction (A-WF01, A-WF02).**

- **What the rows do.** They apply the construction of Bhatt-Lurie-Mathew (*Revisiting the de Rham-Witt complex*): a
  Dieudonné algebra, its saturation Sat_F and the strict completion 𝒲Sat_F. For smooth algebras it recovers Illusie's
  WΩ^•. Here it is applied to the admissible PD theories, as a candidate completion.
- **Why positive weights get a positive slope.** The Dieudonné condition makes F congruent to the p-th power map, and
  T^p = p!·T^[p] ≡ 0 mod p. So F(T) ∈ pR, which is (WF.9): F(T^[w]) = c^w T^[w] with c ∈ pR. Every positive weight then
  has positive slope. In the strict completion, elements on which F^m is divisible by p^{mw} for all m become infinitely
  p-divisible. So 𝒲Sat_F keeps only the slope-0, unit-root part, which is weight 0, and kills every positive-weight
  coefficient (WF.10). A-WF01 computes the first case: the saturation makes the positive-weight H^0 rational.
- **Why de Rham-Witt keeps positive slopes for smooth varieties and not here.** For smooth varieties its Frobenius is the
  divided one, F = φ/p^i on i-forms, so the Hodge level is untwisted by the form degree. Illusie's slope spectral
  sequence puts the slopes of H^j(X, WΩ^i) in [i, i+1); together with Mazur's inequality this is how the Hodge levels
  bound the slopes from below. In the rows of this run the slope sits in the coefficient weight, and no form degree
  divides it out.
- **What purity gives here.** For the Tate coefficients the slope of weight w is exactly w (c = p up to a unit). So the
  Frobenius untwisted by weight, F/p^w on weight w, is a unit there. This is the normalization a crystalline-type
  completion for C.3 would need: a Frobenius twisted in the manner of Nygaard or Breuil-Kisin twists, not a Dieudonné
  algebra structure, whose congruence forbids the untwisting.
- **What the rows give back.** Within Dieudonné algebras, no weight-preserving Frobenius can complete an admissible
  theory with its coefficient comparison: the congruence to the p-th power forces positive slope on every positive
  weight, and the de Rham-Witt completion then removes the Tate coefficients. This closes the de Rham-Witt route to C.3
  as the run specified it, and names the change it would need, untwisting by p^w.

**3. Gluing over Spec Z (AT01; C30, C32 and C34 of RESEARCH_SA08; A-S09-24 to A-S09-30; the moving-prime rows A-S09-09,
A-S09-12, A-P01, A-L20, A-L21).**

- **The setting.** At each prime the local pieces live over Z_(p) and Z_p, where points 1 and 2 apply. The gates ask
  for these local pieces to glue over the arithmetic square of Z. AT01 is a pure exact sequence of coefficient modules;
  "pure" there means a pure submodule.
- **The obstruction is uniformity in p,** against classes of exact order p at every prime: in weight 2p (A-S09-09), in
  weight p^k and degree 2k−1 (A-S09-12), and in weight 2pb + 2p(p−1) + 1 (A-P01).
- **Where their orders come from.** They are p-adic valuations of factorials: T^w = w!·T^[w], and by Legendre's formula
  v_p(w!) first becomes positive at w = p.
- **The torsion that zeta values control in Tate twists over Z.** H^1(Z[1/p], Z_p(w)) has p-torsion exactly when
  (p−1) | w, since the cyclotomic character mod p has order p−1. For even w, H^2(Z[1/p], Z_p(w)) is measured by ζ(1−w),
  that is by Bernoulli numbers (Kummer's congruences, von Staudt-Clausen, Mazur-Wiles).
- **Why the rows' classes are not of that kind.** They do not follow that pattern. Weight 2p is ≡ 2 mod (p−1), so for
  p ≥ 5 they lie in weights where the cyclotomic torsion of the Tate twists vanishes. They exist for every odd prime,
  regular or not. They are the torsion of divided powers against ordinary powers, not torsion of zeta values.
- **Why RH and GRH give nothing.** They govern the zeros of ζ and L(s, χ) and through them the distribution of primes.
  Every torsion order in these rows is computed exactly, prime by prime, by Legendre's formula, and no row uses how the
  primes are distributed. So RH and GRH give these rows nothing, and the rows give nothing back to ζ or L-values.
- **Artin-Verdier.** Spec Z as a 3-manifold is the frame of the gates: a Mayer-Vietoris over Spec Q and the formal discs
  at the primes. The proved finite-prime cases (C16, C17) are the gluing over Spec Z[1/m]; the open case is all of
  Spec Z. But no duality H^i ↔ Ext^{3−i}(−, G_m) and no étale cohomology with Z(n) coefficients enters any row, so the
  3-manifold structure is not used.

**4. Zeta values, L-functions, motivic cohomology, K-theory, mixed Tate motives, periods, positivity.**

- **What the rows contain.** The only Tate structure in them is that of point 1: the coefficients Γ(T) = H_*(BG_m) and
  their Tate weights. No row computes motivic cohomology, K-groups, periods or special values. So, beyond point 1, the
  link carries nothing.
- **Where the programme meets these bridges directly.**
  - On the Witt and crystalline side of the archive, in SA17 (cotes 126-133, the Witt-Dieudonné-BT notebooks). There
    the slopes of the Dieudonné modules of p-divisible groups (Manin), with Katz-Messing and Mazur, are the p-adic face
    of the Weil bounds for abelian varieties.
  - In RESEARCH_SA08's B.8: Breen's Ext(G_a, G_a) and its Frobenius torsion.

## 5. Prompt updates (for a successor of this run)

- **Part B is finished.** This intake checked B-001, B-003 and B-004, and found that no other result of v4 cites
  Prop. 3.10. Drop Part B. Before a note to the authors cites B-003 and B-004, read B-002 once.
- **Part A:**
  - state the item through its new exact gates: A-S09-29 for common sources, and A-S09-30 (the localization of
    F_3,ω^[d]) for terminality;
  - carry the refuted routes of section 1 as tried-and-failed;
  - carry the pieces the run itself left unproved:
    - AT18-19 for general target data;
    - AT24-25: higher-simplex vertical exactness, and stability under later degree-four repairs;
    - AT27: the strict C34 truncation isomorphism;
    - A-L14-15: an actual free replacement of arbitrary targets;
    - A-S09-31: an all-simplex positive-degree comparison;
    - A-SA09.
- **Restore** from the newest checkpoint, or the final if one has come since cp08.
- **First, an intake reader for Part A's proofs.** It should take the rows the run rests on first: A-SAT01, AT16,
  A-S09-24, AT01, A-S09-27, A-S09-29, A-S09-30, A-004-006 and A-P01.

## Appendix: row-by-row table

| id | run status | statement | proof at | the run's check events | intake verdict |
|---|---|---|---|---|---|
| AT21 | Proved | Every simplex-two odd-one cell over the free even-disk first skeleton has an explicit closed-boundary presentation, with inverse strict PD maps fixing the old algebra and preserving all marked maps by transport. | sections/A_closed_boundary_cells.tex:4 | 6 events: independent referee x2; targeted proof check x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT21b | Proved | Explicit integral transgression elements give inverse resolved and iterated-saturation maps with exactly the prescribed edges AT140; for the actual local AS22 resolution they also give inverse degree-three-repair maps. | sections/A_closed_boundary_cells.tex:139 | 5 events: independent re-proof x1; construction and independent referee x1; inde | not read in full: statement level, with the run's own check events |
| A-S09-01 | Proved | Disk restriction fully faithfully reconstructs relatively left-exact functors over every commutative ring with the explicit finite-matrix kernel essential image | sections/A_cosimplicial.tex:14 | 1 events: independent re-proof x1 / last 2026-11-19T14:50:43Z GPT-6 Astra; effor | not read in full: statement level, with the run's own check events |
| A-S09-02 | Proved | The right-adjoint tests R_n have explicit integral normalized contractions; normalization has rank binomial(n+1,m); test category closed under tensor and all Gamma^p | sections/A_cosimplicial.tex:69 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| A-S09-03 | Proved | The full natural Gamma action on the cochain test functor F_X reconstructs and is reconstructed by the cosimplicial function ring Z^X for arbitrary simplicial X | sections/A_cosimplicial.tex:133 | 1 events: targeted proof check x1 / last 2026-11-19T14:50:43Z GPT-6 Astra; effor | not read in full: statement level, with the run's own check events |
| A-S09-04 | Proved | Raw row-test reconstruction fails to invert all admissible maps: a split square-zero admissible extension changes the disk value from zero to Z | sections/A_cosimplicial.tex:216 | 1 events: independent re-proof x1 / last 2026-11-19T14:50:43Z GPT-6 Astra; effor | not read in full: statement level, with the run's own check events |
| A-S09-05 | Known | Opened Horel derived adjunction and unit theorem give the mapping-space comparison on function rings; Mandell's opened statements have integral E-infinity cochains as input | sections/A_cosimplicial.tex:193 | 1 events: used and rechecked in this run x1 / last 2026-11-19T14:50:43Z GPT-6 As | not read in full: statement level, with the run's own check events |
| A-S09-06 | Proved | The underived left adjoint of shuffle denormalization sends Z^{Delta[1]} to ZxZ and fails to preserve the constant-function quasi-isomorphism | sections/A_rectification.tex:8 | 1 events: independent re-proof x1 / last 2026-11-19T15:35:52Z GPT-6 Astra; effor | not read in full: statement level, with the run's own check events |
| A-S09-07 | Proved | Alexander-Whitney totalization and the associative replacement Q have explicit noncommutative intermediate products | sections/A_rectification.tex:84 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| A-S09-08 | Proved | No model structure on all nonnegative augmented strict PD cochain DGAs over Z has underlying quasi-isomorphisms as weak equivalences and degreewise surjections as fibrations | sections/A_rectification.tex:143 | 1 events: independent re-proof x1 / last 2026-11-19T15:35:52Z GPT-6 Astra; effor | not read in full: statement level, with the run's own check events |
| A-S09-09 | Proved | The cellular free simplicial PD resolution of S/I_2 has special cotangent pi_2 elements of exact order p in every weight 2p for odd primes p; its weight-six pi_2 is Z/3 | sections/A_cotangent.tex:9 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| A-S09-10 | Proved | The same special cotangent complex has an explicit weight-nine integral pi_3 class nonzero over Z_(3) | sections/A_cotangent.tex:204 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| A-S09-11 | Proved | For the specified cellular resolution of S/I2 every odd p has nonzero p-local row-one homology in degree 2k-1 and weight p^k for all k>=2; no eventual fixed slope holds | sections/A_cotangent_unbounded.tex:3 | 2 events: targeted proof check x1; primary theorem opened and exact comparison p | not read in full: statement level, with the run's own check events |
| A-S09-12 | Proved | For every fixed N>=2 every p>3(N-1) and every k>=1 every cellular free simplicial PD S-resolution of S/I_N has nonzero p-local row-one homology in degree 2k-1 and weight p^k | sections/A_cotangent_all_truncations.tex:3 | 2 events: independent re-proof x1; new proof and finite chain certificate x1 / l | not read in full: statement level, with the run's own check events |
| A-S09-13 | Proved | Full integral bar integration exists for an odd disk with any common degree-zero PD factor z; dz need not vanish | sections/A_nonclosed_bar.tex:3 | 2 events: targeted proof check x1; new proof and exact universal certificate x1  | not read in full: statement level, with the run's own check events |
| A-S09-14 | Proved | Single-weight torsion H1 admits an explicit free all-simplex based saturation extending both target maps when the source simplex-zero complex is the coefficient group and source H0 is that group | sections/A_weightwise_saturation.tex:3 | 2 events: targeted proof check x1; new exact linear construction x1 / last 2026- | not read in full: statement level, with the run's own check events |
| A-S09-15 | Proved | Exact binomial Rees specialization maps have a rank-one quadratic obstruction to the specified strict PD coefficient lift | sections/A_binomial_deformation.tex:3 | 2 events: targeted proof check x1; new exact algebra calculation and primary-sou | not read in full: statement level, with the run's own check events |
| A-S09-16 | Proved | The vertex-period difference H1X->Z^{n+1}/diagZ is the exact obstruction to simultaneous degree-zero repair; a canonical pullback removes its kernel | sections/A_weightwise_period.tex:3 | 3 events: targeted proof check x2; new all-simplex construction and exact obstru | not read in full: statement level, with the run's own check events |
| A-S09-17 | Proved | The difference of rational coefficient residues gives tors H1X->constant Q/Z; an actual AT14 repair has nonzero residues in arbitrarily large weights | sections/A_coefficient_residue.tex:3 | 4 events: targeted proof check x2; new residue proof, explicit AT14 example, and | not read in full: statement level, with the run's own check events |
| A-S09-18 | Proved | Natural H4 of a free identity-disk PD algebra is S/2 tensor the doubled-weight odd one-form indecomposables | sections/A_low_cartier.tex:3 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-S09-19 | Proved | The common C21 partial source can retain P0=S and integral coefficient resolution in simplex1 with all original bounds and maps | sections/A_low_cartier.tex:107 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-S09-20 | Proved | All-weight low cohomology of a q4 two-cell repair is the exact kernel and cokernel of its S/2 class map | sections/A_low_repair.tex:3 | 1 events: independent referee x1 / last 2026-11-19 GPT-6 Astra; inherited effort | not read in full: statement level, with the run's own check events |
| A-S09-21 | Proved | A nonfree coefficient-tail PD algebra kills the tail of an independent H4 class without creating H1-H3; its actual target maps are exactly the displayed S-linear primitive pairs | sections/A_tail_low_repair.tex:3 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-S09-22 | Proved | The actual resolved coefficient-tail repair has an order-two H3 class surviving every based PD H1 saturation, including the independent quadratic twist | sections/A_saturated_tail_H3.tex:3 | 4 events: targeted proof check x2; independent referee x1; new exact lattice pro | not read in full: statement level, with the run's own check events |
| A-S09-23 | Proved | For N>=2 a second skeleton extending P(N) cannot have eventual row-one exactness when its one-forms are generated by zero-forms and their special differentials | sections/A_second_skeleton_obstruction.tex:3 | 4 events: targeted proof check x2; independent referee x1; new exact comparison  | not read in full: statement level, with the run's own check events |
| A-S09-24 | Proved | For each fixed d both integral uniqueness questions reduce to the proper full category with the A006 free first skeleton and coefficient comparison through degree d in every weight | sections/A_uniform_tail_reduction.tex:10 | 4 events: targeted proof check x2; independent referee x1; new actual category r | not read in full: statement level, with the run's own check events |
| A-S09-25 | Proved | Both unbounded-cutoff inverse towers T_N A and R T_N A have strict limit S and admit no cone from any admissible object | sections/A_tail_inverse_limit.tex:3 | 2 events: targeted proof check x1; new exact inverse-limit computation x1 / last | not read in full: statement level, with the run's own check events |
| A-S09-26 | Proved | The standard Hadamard image is strictly isomorphic to G tensor_S G; its full based PD closure in the entire rational Hadamard algebra is fixed and retains prime-power row-zero torsion | sections/A_hadamard_image.tex:25 | 3 events: targeted proof check x2; new exact common-target operation calculation | not read in full: statement level, with the run's own check events |
| A-S09-27 | Proved | For each fixed d the integral common-source assertion is equivalent to internal common sources in the proper full subcategory E^[d] with one free zero-form disk per first-skeleton weight, global vertical comparison through d, and horizontal | sections/A_single_disk_gate.tex:17 | 3 events: targeted proof check x2; new exact common-source reduction; proof comp | not read in full: statement level, with the run's own check events |
| A-S09-28 | Proved | For every d the all-arrow localization of E^[d] is nonterminal and its inclusion into C^[d] and A_Z is not faithful: an explicit endomorphism is detected by a prime-weight scalar germ but killed by actual doubled-skeleton maps | sections/A_single_disk_localization_obstruction.tex:8 | 3 events: targeted proof check x2; new exact localization obstruction and double | not read in full: statement level, with the run's own check events |
| A-S09-30 | Proved | The full countable category with first skeleton one of P_r(N), r=1,2,3 constant per object, global coefficient comparison through d and rows through d+2 exact from N has all-arrow localization equivalent to A_Z and lies properly between E_o | sections/A_three_disk_gate.tex:17 | 3 events: targeted proof check x2; new strict terminal-localization gate and ful | not read in full: statement level, with the run's own check events |
| A-S09-31 | Proved | Integral mixed-cell resolved sources admit actual integral H1-H3 cleanup in simplex two retaining the first skeleton and both target maps, with a compatible localized2 carrier and only2-power torsion-pair repairs after the original coeffici | sections/A_integral_mixed_cleanup.tex:3 | 3 events: independent referee x1; targeted proof check x1; new integral mixed-ce | not read in full: statement level, with the run's own check events |
| A-P01 | Proved | At every prime a specified degree-2p resolved-tail repair creates an exact order-p degree-two class surviving every based saturation stage, with an actual further projection-preserving repair | sections/A_deep_tail_H2.tex:3 | 3 events: independent re-proof x1; targeted proof check x1; independent full ref | not read in full: statement level, with the run's own check events |
| AT11 | Proved | Every coefficient tail detects a nonzero arbitrarily long Ext class after reduction modulo p; its corresponding top-cycle nullhomotopies necessarily reach the last syzygy module. | sections/A_descent_obstruction.tex:11 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT12 | Proved | One integral flat admissible target and a legitimate prescribed C21 partial-model diagram admit no local admissible completion preserving forms zero and one at any odd prime, while retaining explicit G→A→G. | sections/A_descent_obstruction.tex:171 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT26 | Proved | For the actual global free D2-cell family, the local carrier extends to a full strict simplicial PD homotopy, with an actual common reference algebra P tensor G_N followed by prescribed even-zero D2 disks. | sections/A_global_prism.tex:4 | 6 events: independent referee x2; independent re-proof x1; rendered visual proof | not read in full: statement level, with the run's own check events |
| AT19 | Proved | For the actual independent quadratic K2 disk, a row-one D3 filling gives resolved target lifts with zero secondary period and actual simultaneous relative q3 repair maps, including after the constructed saturation. | sections/A_horizontal_period_repair.tex:4 | 8 events: independent referee x3; targeted proof check x3; independent re-proof  | not read in full: statement level, with the run's own check events |
| A-H01 | Proved | A uniform coefficient tail annihilates horizontal homology of every form row once the degree-zero row has that tail exact in H0. | sections/A_horizontal_scaling.tex:3 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT22 | Proved | An actual integral free resolution containing the displayed finite chain has integral zero relative period for the specified quadratic secondary class, by a proved local-to-integral comparison of the same resolution and of relative complexe | sections/A_integral_period_transfer.tex:4 | 6 events: independent referee x2; independent re-proof x1; standalone syntax che | not read in full: statement level, with the run's own check events |
| AT29 | Proved | Actual integral completion through form three in every simplex and all eventual horizontal rows from actual 2-local reference paths and coefficient comparison after inverting two; all prescribed endpoint maps remain integral. | sections/A_integral_reference_completion.tex:4 | 4 events: targeted proof check x2; independent re-proof x1; independent referee  | not read in full: statement level, with the run's own check events |
| AT29b | Proved | The initial integral resolved extension of the actual global free D2-cell family satisfies AT29 and admits its all-simplex integral low-degree completion. | sections/A_integral_reference_completion.tex:298 | 4 events: targeted proof check x2; independent re-proof x1; independent referee  | not read in full: statement level, with the run's own check events |
| IC01 | Proved | Exact terms, differential and junction cohomology of the strict pullback P_<d ×_{A_<d} A | sections/A_integral.tex:3 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| IC02 | Proved | Strict splicing a quasi-isomorphism between contractible complexes can create H^{d-1}=k | sections/A_integral.tex:45 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| IC03 | Proved | Strict form splicing fails for an admissible square-zero disk extension of the integral standard theory | sections/A_integral.tex:67 | 2 events: independent re-proof x1; computation or formal certificate x1 / last 2 | not read in full: statement level, with the run's own check events |
| AT25 | Proved | The actual AT24 low-degree carrier cleanup extends to an arbitrary set of simultaneously resolved free C21 simplex-two odd cells with uniform weight bounds, including all mixed higher-arity H2/H3 classes; target maps, saturation carrier, fi | sections/A_mixed_cell_cleanup.tex:4 | 7 events: independent referee x3; targeted proof check x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT09 | Proved | The persistent arithmetic extension is realized in a finite-free admissible strict PD theory with no coefficient S-linear retraction at simplex0; an explicit map G→A still supplies a common source. | sections/A_nonsplit_theory.tex:4 | 2 events: independent re-proof x1; targeted proof check x1 / last 2026-11-19T17: | not read in full: statement level, with the run's own check events |
| AT23 | Proved | A genuine p-torsion three-class repaired by an actual AT14 two-cell extension produces order-r torsion in form2r at weight rw for every prime r; H1 saturation is unchanged, and an increasing-weight family gives unbounded new H4 two-torsion. | sections/A_prime_transfer.tex:4 | 8 events: independent referee x2; targeted proof check x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT27 | Proved | An actual common reference and path maps permit simultaneous all-simplex completion through d≤3 over Z or d≤2p−1 over Z_(p), with actual extensions of the prescribed maps, reference-controlled saturation and coherent horizontal restoration. | sections/A_reference_controlled_completion.tex:19 | 7 events: targeted proof check x2; independent referee x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT28 | Proved | The prescribed AT12 map has an actual global strict homotopy to a map through the fully admissible reference G, while every odd-prime strict form<2 completion remains impossible. | sections/A_reference_truncation_obstruction.tex:4 | 6 events: targeted proof check x2; independent referee x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT20 | Proved | For an actual relative Cartier cell with specified closed boundary dh and coefficient period ρ, explicit local reference forms and normalized quadratic disk data give simultaneous resolved target maps and original relative q3 repairs, inclu | sections/A_relative_period_repair.tex:4 | 5 events: targeted proof check x2; independent re-proof x1; construction and ind | not read in full: statement level, with the run's own check events |
| AT17 | Proved | The coefficient-tail quadratic repair extends prescribed D(2) boundary data using an actual simplex-one S-linear contraction, simultaneous target maps, a rational contraction, and a torsionfree quotient preserving H0 and simplices zero and  | sections/A_relative_resolved_tail.tex:4 | 5 events: targeted proof check x2; independent re-proof x1; independent referee  | not read in full: statement level, with the run's own check events |
| AT15 | Proved | An actual relative D(2) two-cell repair preserves simplices zero and one and has simultaneous target maps for q=2 and q≥4; q=3 has the explicitly computed necessary-and-sufficient edge-period residue. | sections/A_relative_weight_repairs.tex:49 | 7 events: independent referee x2; targeted proof check x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT15-restoration | Proved | After the constructed relative extension, the specified C21 horizontal restoration has fixed target-dependent bounds and preserves the coefficient H0, H1, rational vertical resolution and simplex-one integral resolution. | sections/A_relative_weight_repairs.tex | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT18 | Proved | The corrected resolved-tail H3 class has an exact relative-repair obstruction given by its modulo-two coefficient period; with the stated weight-s period comparison the residue is independent of every AT16 lift choice, and explicit zero-res | sections/A_resolved_tail_period.tex:4 | 7 events: independent referee x2; targeted proof check x2; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT16 | Proved | An actual K(2)-parameter coefficient-tail quadratic repair has simultaneous target maps by Ext²(L/mL,S)=0, a displayed rational contraction, and a torsionfree quotient preserving H0, simplices zero and one, and all lower weights. | sections/A_resolved_tail_repair.tex:67 | 6 events: independent referee x2; independent re-proof x1; LaTeX verification x1 | not read in full: statement level, with the run's own check events |
| AT16-comparison | Proved | The resolved tail algebra has an explicit surjective strict PD-DGA map to the two-term nonfree tail algebra, inducing a rational quasi-isomorphism; its linear generator comparison is an integral quasi-isomorphism. | sections/A_resolved_tail_repair.tex:306 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| A-001 | Proved | Exact normalization gives slice flasqueness and restriction surjectivity | sections/A_paths.tex:24 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19 GPT | not read in full: statement level, with the run's own check events |
| A-002 | Proved | Every admissible cospan has an admissible common-source refinement | sections/A_paths.tex:76 | 2 events: targeted proof check x2 / last 2026-11-19 GPT-6 Astra (OpenAI), Pro mo | not read in full: statement level, with the run's own check events |
| A-003 | Proved | Connected components coincide with the relation of admitting a common source | sections/A_paths.tex:161 | 2 events: independent re-proof x1; targeted proof check x1 / last 2026-11-19 GPT | not read in full: statement level, with the run's own check events |
| A-CS | Open; return INCOMPLETE | Existence of common admissible strict PD sources over Z for arbitrary two theories | sections/A_unresolved.tex:1 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-TL | Open; return INCOMPLETE | Terminality of the localization of integral admissible strict PD theories at all morphisms | sections/A_unresolved.tex:105 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-SA09 | Open; return INCOMPLETE | Application of the verified SA09 reconstruction structures to integral comparison or a separating invariant | sections/A_unresolved.tex:134 | none recorded for this id | not read in full: statement level, with the run's own check events |
| A-004 | Proved | Every admissible theory has an actual admissible replacement with a prescribed common free first skeleton | sections/A_skeleton_replacement.tex:27 | 2 events: independent referee x1; targeted proof check x1 / last 2026-11-19 GPT- | not read in full: statement level, with the run's own check events |
| A-005 | Proved | The common-source question reduces to pairs with the same specified first skeleton P(N) | sections/A_skeleton_replacement.tex:251 | 2 events: independent referee x1; targeted proof check x1 / last 2026-11-19 GPT- | not read in full: statement level, with the run's own check events |
| A-006 | Proved | Functorial first-skeleton replacement gives equivalent all-arrow localizations and equivalent common-source questions in a proper full subcategory | sections/A_functorial_skeleton.tex:18 | 4 events: targeted proof check x2; independent referee x1; independent full refe | not read in full: statement level, with the run's own check events |
| A-S09-29 | Proved | Countable actual subobjects preserve the free first skeleton and all exactness ranges in finite diagrams; their full inclusions induce equivalent localizations, giving proper countable internal gates for both integral questions | sections/A_countable_gate.tex:23 | 3 events: targeted proof check x2; independent full referee proof check x1 / las | not read in full: statement level, with the run's own check events |
| A-SAT01 | Proved | Countable PD closure and based saturation inside the fixed rational algebra kills all H1 above one fixed cutoff while extending every specified torsion-free target map and retaining simplices zero and one | sections/A_iterated_saturation.tex:3 | 5 events: targeted proof check x2; independent re-proof x1; independent referee  | not read in full: statement level, with the run's own check events |
| AT24 | Proved | For one actual free C21 simplex-two odd cell over Z_(2), the selected local carrier survives all homogeneous higher-arity degree-two and degree-three repairs and based saturation; iterating these actual maps gives coefficient comparison thr | sections/A_single_cell_cleanup.tex:4 | 8 events: targeted proof check x3; independent referee x3; independent re-proof  | not read in full: statement level, with the run's own check events |
| AT01 | Proved | Pure completed arithmetic sequence and its exact graded coefficient extension | sections/A_tail_completion.tex:31 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT02 | Proved | Complete graded Ext calculation of I_N into every shift of S=Γ_Z(T) | sections/A_tail_completion.tex:62 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT03 | Proved | Explicit nonsplit persistent coefficient-tail extension E_{c,N,j} | sections/A_tail_completion.tex:172 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT04 | Proved | Derived tail restriction comparison for all nonnegative source-weight shifts | sections/A_tail_completion.tex:224 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT05 | Proved | All degree-preserving Ext from nonnegative weight-torsion modules to S vanish; derived restriction to any weight tail is an isomorphism | sections/A_tail_completion.tex:257 | 2 events: independent re-proof x1; targeted proof check x1 / last 2026-11-19 GPT | not read in full: statement level, with the run's own check events |
| AT06 | Proved | The complete coefficient algebra Γ_Zp(T) has full graded injective dimension at most one; 0→S_p→S_Qp→E_p→0 is an injective resolution in nonnegative weights. | sections/A_tail_injective.tex:11 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT07 | Proved | An explicit two-term injective resolution proves that Γ_Z(T) has injective dimension exactly one in nonnegative weights. | sections/A_tail_injective.tex:125 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT08 | Proved | A concrete nonsplit extension by S has all terms nonnegative and free abelian in each weight. | sections/A_tail_injective.tex:200 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT10 | Proved | A nonfree PD-filtered polynomial Koszul closure contracts vertically and admits natural actual evaluation maps into arbitrary strict PD targets; split parameter inclusions have base-change-stable module contractions. | sections/A_tail_koszul.tex:19 | 3 events: targeted proof check x2; independent re-proof x1 / last 2026-11-19T17: | not read in full: statement level, with the run's own check events |
| AT10-lattice | Proved | The exact divided-power basis lattice is (product beta_i!)D_m; for p-local N=p^e the coefficient ideal D_m is exactly I_(mN). | sections/A_tail_koszul.tex | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| A-WF01 | Proved | The canonical supported weight Frobenius gives a Dieudonne algebra whose saturation rationalizes positive-weight H0 and whose completed saturation kills the original positive-weight coefficients | sections/A_weight_frobenius_saturation.tex:21 | 3 events: independent re-proof x1; used and rechecked in this run x1; targeted p | not read in full: statement level, with the run's own check events |
| A-WF02 | Proved | Every weight-preserving unital Dieudonne Frobenius with the stated coefficient H0 and vertex retractions has F(T^[w])=c^wT^[w], c in pR, and its canonical completed saturation kills every positive coefficient over Z, Z_(p) or Z_p | sections/A_all_weight_frobenius.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; independent full ref | not read in full: statement level, with the run's own check events |
| AT13 | Proved | A prescribed high-weight coefficient-tail cycle with a projective contractible simplicial parameter admits an actual finite-resolution PD repair with simultaneous target maps and unchanged horizontal bounds; for q≥2 its torsion quotient pre | sections/A_weight_repairs.tex:20 | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| AT14 | Proved | A high-weight cycle of form q≥2 with a projective contractible parameter admits a two-cell repair du=z and dv=mu−b that preserves rational coefficient exactness, H0=S, flatness and horizontal bounds, with simultaneous target maps. | sections/A_weight_repairs.tex:209 | 2 events: independent re-proof x1; code x1 / last 2026-11-19 GPT-6 Astra; inheri | not read in full: statement level, with the run's own check events |
| AT14-H1 | Proved | The two-cell repair preserves H1 for q≥3; for q2 its first affected weight has the exact new H1 kernel of M/mM→H2X. | sections/A_weight_repairs.tex | 1 events: independent re-proof x1 / last 2026-11-19 GPT-6 Astra; inherited effor | not read in full: statement level, with the run's own check events |
| B-001 | Refuted | Proposition3.10 is false over every nonzero ring; D-031 confirmed | sections/B_lifting_audit.tex:56 | 1 events: independent re-proof x1 / last 2026-11-19T15:53:... GPT-6 Astra (OpenA | confirmed: targeted proof check of the proof in full, and the statement checked against the source (arXiv:2511.22614v4, Section 2.1, Prop. 3.10 and its proof) |
| B-002 | Proved | Free strict PD algebra, explicit inclusion into TS, and graded cokernel copies of k[2] | sections/B_lifting_audit.tex:147 | 1 events: independent re-proof x1 / last 2026-11-19T15:53:... GPT-6 Astra (OpenA | not read in full: statement level, with the run's own check events |
| B-003 | Proved | Exact Hom¹ obstruction and complete set of strict chain/PD lifts | sections/B_lifting_audit.tex:276 | 1 events: independent re-proof x1 / last 2026-11-19T15:53:... GPT-6 Astra (OpenA | confirmed: targeted proof check of the proof in full (section 1); (B.4) of B-002 and the Stacks locator not opened |
| B-004 | Proved | Exact universal lifting criteria: contractible and K-projective respectively | sections/B_lifting_audit.tex:308 | 1 events: independent re-proof x1 / last 2026-11-19T15:53:... GPT-6 Astra (OpenA | confirmed: targeted proof check of the proof in full (section 1); (B.4) of B-002 and the Stacks locator not opened |
| B-005 | Known | Unbounded termwise-free acyclic Z/4 complex has a surjective quasiisomorphism with no section | sections/B_lifting_audit.tex:383 | 1 events: used and rechecked in this run x1 / last 2026-11-19T15:53:... GPT-6 As | not read in full: statement level, with the run's own check events |
| B-006 | Known | Free Tate resolution comparison over arbitrary commutative rings and module homotopies | sections/B_lifting_audit.tex:432 | 1 events: used and rechecked in this run x1 / last 2026-11-19T15:53:... GPT-6 As | reach of D-031 confirmed against the source (Thm 3.15 assumes a quasi-isomorphism; its visible proof does not use Prop. 3.10); the comparison proof itself not read in full |
| B-007 | Refuted | Strictly negative Tate resolution part need not be a differential ideal | sections/B_lifting_audit.tex:504 | 1 events: refuted, with the refined statement's id x1 / last 2026-11-19T15:53:.. | not read in full: statement level, with the run's own check events |
| B-008 | Proved | Conjugation by comparison maps yields inverse graded End cohomology algebra isomorphisms | sections/B_lifting_audit.tex:536 | 1 events: independent re-proof x1 / last 2026-11-19T15:53:... GPT-6 Astra (OpenA | reach of D-031 confirmed as for B-006; the proof itself not read in full |
| A-L01 | Proved | Every coefficient-tail inclusion fails to lift through the canonical free module epimorphism | sections/B_tail_obstruction.tex:20 | 2 events: independent re-proof x2 / last 2026-11-19T16:28:... GPT-6 Astra (OpenA | not read in full: statement level, with the run's own check events |
| A-L02 | Proved | Admissible finite-free target has a free-parameter cycle without any delayed S-linear primitive | sections/B_tail_obstruction.tex:68 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T16: | not read in full: statement level, with the run's own check events |
| A-L03 | Proved | Prescribed gamma2(dx) in an admissible integral target has no strict primitive on any full coefficient tail | sections/B_tail_obstruction.tex:277 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T16: | not read in full: statement level, with the run's own check events |
| A-L04 | Proved | Coefficient-scaled odd disks have explicit integral primitives and compatible maps from every p-local C18 closure | sections/B_scaled_closure.tex:18 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T16: | not read in full: statement level, with the run's own check events |
| A-L05 | Proved | Full integral regraded bar closure maps naturally to a target after a common PD coefficient scaling | sections/B_scaled_closure.tex:93 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T16: | not read in full: statement level, with the run's own check events |
| A-L06 | Proved | Independent divided-power coefficient parameters admit a full integral bar map; explicit higher S-balancing fails for that map | sections/B_scaled_closure.tex:328 | 2 events: independent re-proof x1; independent referee proof check x1 / last 202 | not read in full: statement level, with the run's own check events |
| A-L07 | Proved | A contractible free horizontal parameter can still lack prescribed delayed bar primitives in an admissible target | sections/B_contractible_parameter.tex:1 | 3 events: independent re-proof x1; computation or formal certificate x1; indepen | not read in full: statement level, with the run's own check events |
| A-L08 | Proved | Complete divided-power coefficients are injective relative to p-torsion-free graded modules; simplexwise coefficient-tail retractions cannot be simplicially compatible | sections/B_complete_relative.tex:3 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T17: | not read in full: statement level, with the run's own check events |
| A-L09 | Proved | Two actual AT14 attachments yield a full torsion-H1 saturation that changes horizontal homology | sections/B_full_saturation_failure.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L10 | Proved | For every fixed prime p, degree n and truncation N, special cotangent homology of a cellular PD resolution of S/I_N vanishes in weights above (N−1)(1+b_p(n)) | sections/B_fixed_degree_cotangent.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L11 | Proved | The actual AT16 resolved coefficient-tail PD algebra can acquire exact-order-two H1, including for an independent quadratic class; the augmentation comparison to the unresolved tail fails on H1 | sections/B_resolved_tail_lattice.tex:3 | 4 events: targeted proof check x1; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L12 | Proved | Full based PD H1 saturation of the actual resolved quadratic tail can retain exact-order-two H2 killed by the augmentation comparison | sections/B_saturated_degree_two.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L13 | Proved | A degree-three relative two-cell repair admits simultaneous target maps with a variable closed edge boundary exactly when the two fixed-boundary coefficient residues agree modulo m | sections/B_relative_period_alignment.tex:3 | 4 events: targeted proof check x1; independent re-proof x1; independent check by | not read in full: statement level, with the run's own check events |
| A-L14 | Proved | Every graded free module over Gamma_Fp(T) with generator weights bounded below is graded injective, with arbitrary multiplicity in every weight | sections/B_bounded_free_flatness.tex:3 | 3 events: targeted proof check x2; independent re-proof x1 / last 2026-11-19T19: | not read in full: statement level, with the run's own check events |
| A-L15 | Proved | A nonnegative termwise graded S-free cochain complex with split coefficient H0 and global H1 through Hd zero has S-flat B1 through B(d+1) and Z0 through Zd over Z or Z_(p) | sections/B_bounded_free_flatness.tex:84 | 2 events: targeted proof check x1; independent re-proof x1 / last 2026-11-19T19: | not read in full: statement level, with the run's own check events |
| A-L16 | Proved | Under A-L15 the arbitrary-module tensor comparison is exact below d and its degree-d defect is Tor_1(M^(d+1)/B^(d+1),N), with the coefficient summand split off when d=0 | sections/B_tensor_boundary_defect.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; independent full ref | not read in full: statement level, with the run's own check events |
| A-L17 | Proved | AT23 repaired partial source has coefficient cohomology through degree3 in every simplex, but actual base change S to S/2 has H3=(S/2)⟨2w⟩ in simplex2 | sections/B_partial_source_tensor.tex:3 | 4 events: targeted proof check x1; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L18 | Proved | The low-boundary flatness and exact tensor-defect conclusions of A-L15/16 hold for bounded-below termwise S-flat complexes with the same actual coefficient splitting and global low cohomology | sections/B_flat_boundary_extension.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; independent full ref | not read in full: statement level, with the run's own check events |
| A-L19 | Proved | For every prime p the actual A-P01 resolved-tail source after the entire based H1 PD saturation has a nonflat simplex-two zero-form S-module | sections/B_saturated_tail_nonflat.tex:3 | 3 events: targeted proof check x1; independent re-proof x1; independent full ref | not read in full: statement level, with the run's own check events |
| A-L20 | Proved | At p=3 the A-P01 source after its actual degree-two repair and saturation has a surviving exact-order3 H3 class at weight2s+13; its relative period vanishes for every actual target map in the explicit range, giving actual simultaneous next  | sections/B_p3_second_repair.tex:3 | 5 events: targeted proof check x2; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
| A-L21 | Proved | At every odd prime the specified A-P01 source after its degree-two repair has a surviving exact-order-p H3 class whose relative period vanishes for every actual target map in the stated range, with actual simultaneous next repairs | sections/B_odd_prime_second_repair.tex:3 | 5 events: targeted proof check x2; independent re-proof x1; computation or forma | not read in full: statement level, with the run's own check events |
