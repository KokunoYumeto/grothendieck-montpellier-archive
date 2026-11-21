# Addendum: ALPOGE_GCT checkpoint 03 (21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). Earlier intake: `INTAKE_ALPOGE_GCT_20261121.md` (checkpoint 01). The run is GPT-6 Astra (ChatGPT Pro mode);
its effort is not exposed.

## 0. Return read and scope

- Folder: `research_returns\ALPOGE_GCT_checkpoint_03_20261121T0117Z_unzipped`, assembled 01:17 UTC after about 2 h 15
  min of work. The run is still going. P-F30 (support contraction) is marked in progress, and the first three-hour
  review was due at about 03:02 CET.
- I read only what is new since checkpoint 01: the LEDGER entries after 00:47 CET and the QUESTIONS rows PL-Q23 to
  PL-Q39, Q-P-F16-*, Q-P-F17-*, Q-PH3 and Q-PH3-WEAK.
- **Read in full, with the proof:**
  - P-F14 and P-F15 (`work/positivity_torus.tex`);
  - P-F19 (`work/positivity_cubic_counterexample.tex`);
  - PLE-F8 (`work/positivity_actual_plethysm.tex`), up to the injectivity argument, which I read in part.
- **Read at the level of the statement:** P-F13, P-F16, P-F17, P-F18, P-F20 to P-F29.
- **Checked against GCT VI** (`supplied_sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`):
  - Hypotheses SH, PH2 and PH3 in the general form (labels `phsh`, `phph2`, `phph3`, l. 2783-2812);
  - the definition of rank(x) (l. 2883-2885);
  - the basic explicit homomorphisms (l. 2942-2953);
  - the specification of a torus character, item (4) (l. 3076-3080);
  - PH1's scope, which includes Problem 1.1.3 (l. 2763-2770).

## 1. Verdicts

**P-F19: the canonical clause of PH3 fails for ordinary plethysm with inner shape (3).** Targeted proof check, plus an
independent re-derivation and a computation. **Confirmed.**

The ray is μ = (3), λ = (n/g), π = det^{3/g} with g = gcd(n,3). Its stretching algebra is the invariant ring of
n-ary cubics, graded by degree/d₀. The argument runs in five steps:
- The point F_n = x₁²x₂ + x₂²x₃ + … + x_{n−1}²x_n + x_n³ is a smooth cubic. I reread the derivative argument.
- So the discriminant Δ, of degree n·2^{n−1}, does not vanish at F_n.
- Every homogeneous system of parameters therefore contains some q_i with q_i(F_n) ≠ 0. The reason: Δ^M lies in the
  ideal (q).
- Every invariant that is nonzero at F_n has stretch degree divisible by 2^{n−1}.
- So χ ≥ 2^{n−1}, while GCT VI's parameter is h = m² + n + 1 = O(n⁶).

I redid both proofs of the divisibility:
- The stabilizer proof. A = diag(ζ^{(−2)^i}) with ζ of order 3·2^{n−1} fixes F_n. det A = ζ^{S_n} with
  S_n = (1−(−2)^n)/3, which is odd and ≡ n mod 3, so det A has order 3·2^{n−1}/g. And P(a·F) = (det a)^{−3s/g}P(F).
- The weight recurrence. I computed it for n = 2..13: the minimal admissible s is exactly 2^{n−1}.
- Sanity check at n = 3: the Aronhold invariant T of degree 6 must vanish at the chain cubic. It does, since that
  cubic has an automorphism of order 4 (j = 1728).

Scope, as the run states it:
- It refutes the "More specifically" clause of Hypothesis 1.6.7 (GCT VI, l. 1484-1497): the modular index of the
  minimal positive form, coming from a lexicographically minimal h.s.o.p. of the canonical ring T.
- It does not refute the first clause: the existence of some positive rational form of small modular index.
- It gives no lower bound on the positivity or saturation index.
- Reading caveat: GCT VI's text says "h.s.o.p. of S" where the positive form is about T. The run uses the T of
  Sections 4.1.1-4.1.2 and discloses the inconsistency. Under the S reading the clause would not even yield a positive
  form for A(t). The T reading is the meaningful one.
- The chain forms are classical: Busé-Jouanolou, Example 4.12, with Demazure. Their use against PH3 appears to be new.

**P-F14 and P-F15: the general Hypotheses 3.3.2(a) (SH), 3.3.3 (PH2) and 3.3.4 (PH3) fail as stated for subgroup
restriction (Problem 1.1.3).** Targeted proof check, against the source definitions. **Confirmed.**
- GCT VI's rank(x) is rank H + rank G + comb(λ) + comb(π) (l. 2883). It carries no bitlength of ρ.
- The basic explicit homomorphisms allow ⊕ of polynomial torus characters (l. 2944-2953).
- The combinatorial length of a torus character is dim H (item 4).
- The two embeddings: ρ_N = diag(t^{N+1}, t) into GL₂ gives the series 1/(1−T^N), with modular index N at rank 5.
  σ_N = diag(t, t³, t^{N+1}) into GL₃, with N odd, gives 1/((1−T²)(1−T^N)), with p = s = N−2 at rank 6 (via P-F10).
- I rechecked the monomial weight equations n + Nk = 2n and 2v + Nw = n.

These counterexamples are literal and cheap: the weights of the embedding are not in the parameter. That is a defect
in the statement of the hypothesis, not a deep obstruction. A corrected statement must include log of the embedding
weights. Even then, the run notes, the indices grow exponentially in that bitlength, so the correction must be a
genuine restriction of the class. The run is right on both points. These are new errata to GCT VI §3.3, so far as I
know.

**PLE-F8: the binary-dihedral ring is the actual canonical multiplicity algebra on the KM ray.** Targeted proof check,
plus computation. **Confirmed.**
- T_s = ker E ∩ (S_{4s})_{2s} is the highest-weight space.
- The identities j² + 4h³ = a²δ, E(δ) = E(h) = E(j) = 0 and z² = uv² + 4u⁴ were verified by sympy.
- The map U, V₀, Z ↦ u, v, z is a graded homomorphism.
- Injectivity: I read the algebraic-independence part. Equal Hilbert series (PLE-F5) then make the map an
  isomorphism.

**Statement level only:** P-F13, P-F16 to P-F18, P-F20 to P-F29.
- P-F13: finite reconstruction under a denominator promise.
- P-F16 to P-F18: fixed-embedding uniformity, finitely many inner embeddings for a fixed inner dimension.
- P-F20 to P-F22: transfer counterexamples, including Gorenstein ones.
- P-F23 to P-F29: the noncancellation and support classification on the weak-PH3 route.

I saw no fault in their statements. The weak PH3 clause is the run's live gate (Q-PH3-WEAK).

**Counts this round:** 4 read in full and confirmed (P-F14, P-F15, P-F19, PLE-F8); 0 refuted; 0 gaps; 15 at statement
level.

## 2. Does checkpoint 03 change note E1 (`reports_20261120/errata/NOTE_E1_Mulmuley_GCT_VI_draft.md`)?

- **The correction stands unchanged.** Theorem 1.6.1(d) as printed fails on the KM ray. The argument in E1 (1 + ct
  over two factors; φ(1), φ(2), φ(3), φ(4)) is the one checked in my first intake.
- **One point of precision.** The counterexample is the KM ray itself, through the source-index argument. The D₅
  quotient is its realization, not the counterexample.
- **E1 can be made stronger (PLE-F8).** The stretching algebra T of Theorem 1.6.1(c) on this ray *is* the D₅ ring
  ℂ[U,V,Z]/(Z² − UV² − 4U⁴), with its multiplication. Equal Hilbert series is not the strongest statement available.
  Suggested wording: "There the stretching algebra T of part (c) is isomorphic, as a graded algebra, to the invariant
  ring ℂ[x,y]^Γ …".
- **One sentence in E1 needs a qualifier.** E1 says that the run proves PH3 ⇒ PH2. That remains true. But checkpoint 03
  shows that the "More specifically" clause of PH3 (Hypothesis 1.6.7) is false (P-F19), and that the general-form SH(a),
  PH2 and PH3 of §3.3 are false as stated for Problem 1.1.3 (P-F14, P-F15).
  - If E1 mentions PH3 ⇒ PH2, it should say that the implication starts from the existence clause.
  - P-F19, P-F14 and P-F15 are better sent as a second note (E2) than added to E1. They concern different statements
    of GCT VI, and P-F19 is stronger mathematics.
  - Before E2, the gates in section 4 apply.

## 3. What is new

- **P-F19** is, to my knowledge, the first refutation of the canonical modular-index clause of PH3 for plethysm. Its
  mechanism is new and general: a point outside the null cone with a finite stabilizer whose determinant character has
  large order forces a large h.s.o.p. degree. Its ingredients are classical: chain cubics after Demazure, and the
  discriminant.
- **P-F14 and P-F15** are new as errata. They are elementary.
- **PLE-F8** upgrades PLE-F5 from equal Hilbert function to isomorphism of algebras.
- Against tonight's runs: GCT_PLETH does not touch PH3; there is no overlap.

## 4. Scope of the two proofs

No new finding uses RH, GRH, Alpöge or Masullo. All are unconditional.

## 5. How the findings bear on the open problems, and the attack they open

1. **What positivity GCT can still ask for** has narrowed again. Homogeneous PH1 is gone (P-K1). The canonical PH3
   clause is gone (P-F19). The general-form index hypotheses are gone as stated (P-F14, P-F15). What remains:
   - the existence clause of PH3: some positive form of small modular index (Q-PH3-WEAK);
   - PH2 itself, possibly proved directly;
   - shifted counting.

   P-F19 also locates the obstacle exactly. Large stabilizers at stable points inflate h.s.o.p. degrees, but they do
   not obviously inflate the poles of the Hilbert series. The question is whether the ordinary Hilbert series of the
   cubic invariant ring has a pole of order growing like 2^{n−1}. The run is on it (P-F23 to P-F29); one comparison is
   left.
2. **Next attack (weak PH3).** For the cubic family, compute the poles of the Hilbert series via the Molien-Weyl
   integral, localized at the fixed points of the torus action on the stable locus (Luna slice at F_n). The order of a
   pole at a primitive root of unity of order d is bounded by the dimension of the fixed locus of the elements of order
   d in the stabilizers. A pole of order ≥ 1 at a root of unity of order 2^{n−1}, with a nonzero residue, would refute
   weak PH3 as well. A vanishing residue would point to weak PH3 holding for this family.
3. **Correcting §3.3.** The parameter must contain log max |weight of ρ|. P-F14 and P-F15 then show that even this is
   not enough. The successor should propose and test a corrected hypothesis for torus-restriction families, for
   example indices bounded by a polynomial in rank(x) times the largest weight.
4. **Purity.** PLE-F8 shows that even the actual multiplicity algebra, with a positive multiplicative basis, a flat
   integral model and pure Tate fibres, breaks homogeneous PH1. A purity route has to aim at shifted counting or at
   index bounds that depend on the weights.

## 6. Integration (no edits made outside this folder)

- **Note E1:** apply the wording change and the qualifier in section 2.
- **New draft note E2** (to Mulmuley, only on the user's word): P-F19 against the canonical clause of Hypothesis 1.6.7,
  and P-F14/P-F15 against Hypotheses 3.3.2(a), 3.3.3 and 3.3.4 as stated, with the reading caveat on S versus T.
- **HEXAGON_CANDIDATES.md, H02:** replace its headline by P-F19 (see section 7); keep the Theorem 1.6.1(d) erratum as
  part of the package.
- **Successor prompt of ALPOGE_GCT:**
  - state P-F14, P-F15, P-F19 and PLE-F8 as settled;
  - make the main question weak PH3 for the cubic family, by the pole computation in 5.2;
  - make the second question a corrected form of the §3.3 hypotheses.
- **Language of algebraic geometry.** P-F19 is fully geometric: the stretching ring is the invariant ring of the
  space of cubic hypersurfaces, and the h.s.o.p. is a finite map from the GIT quotient
  Proj = P(Sym³V*)//SL_n to a weighted projective space. The point F_n is a stable point whose stabilizer acts on the
  fibre of the line bundle of stretch degree 1 by the character (det A)^{3/g}, which has
  order exactly 2^{n−1} (computed from ord(det A) = 3·2^{n−1}/g, in both cases g = 1 and g = 3). In Grothendieck's terms, the
  restriction of the polarization to the residual gerbe at the image point is not trivialized below that degree. That
  forces every finite projection to have a coordinate of that degree. The run states the stabilizer calculation but
  not this geometric reading; the translation above is short and should go into the successor.

## 7. Hexagon readiness

Candidate **P-F19 + P-F14/P-F15 + the Theorem 1.6.1(d) erratum** (a short note: "Three of GCT VI's positivity
hypotheses fail as stated"). The five tests:
1. **Complete:** yes. Every proof is short and complete; I checked all three.
2. **Self-contained:** yes. Inputs: GCT VI (exact locators above), the classical cubic discriminant (Busé-Jouanolou
   Def. 4.6, Prop. 4.7, Example 4.12), and Kahle-Michałek for the ray (not yet opened by us).
3. **Stable:** not yet. The run is live and its weak-PH3 work (P-F23 to P-F30) may strengthen P-F19 into a refutation
   of the existence clause, or bound it. A literature search is also needed: Kahle-Michałek; Mulmuley's later
   statements of PH3; Ikenmeyer, Panova, Walter and others since 2016.
4. **Checked:** one intake proof check, plus my independent re-derivation of the divisibility and the n = 2..13
   computation. That meets the rule's minimum. A second reader of P-F19 would make it firm.
5. **Of interest now:** moderate to high in the GCT community, since it refutes a stated flip hypothesis. It is not
   timely in the sense of a race.

**Gate left:** the run's final, then the literature search. One gate from passing tests 1-4. Test 5 is moderate, so
this is not a flag-at-once item.
