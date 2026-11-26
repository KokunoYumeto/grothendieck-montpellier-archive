# The Galois side: GT̂, Ihara and the anabelian line, towards global Langlands

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 23 Nov 2026, at the main session's request. The note builds on
our files; the locators are given in each section. The runs are GPT-6 Astra (ChatGPT Pro mode).

**What decides each status.**
- Where I prove something here, the proof is written out (§1.1).
- Every other status is a check event already recorded in our intakes, named at the place.
- Literature statements without such an event carry no status. They are marked "(open at the source)".

**Fixed input.** Alpöge's theorem, RH for every Dirichlet L-function, ζ included (20 Nov 2026, formalized in Lean). It
is called A. Masullo's draft claim, GRH for the Hecke L-functions of every number field, is called M. Everything resting
on M is conditional.

## 1. The maps, written out

### 1.1 The arithmetic quotient of GT̂ (H17 Theorem 2)

**The objects.**
- GT̂, with Ihara's embedding G_Q → GT̂.
- Two cocycles on GT̂:
  - the multiplier λ: GT̂ → Ẑ^×, which extends the cyclotomic character χ;
  - ρ₂: GT̂ → Ẑ, defined by [β_F⁻¹] = (ρ₂, ρ₂) in F̂^ab. This is Nakamura–Schneps's ρ₂ (NS Def. 5.1, opened on
    23 Nov). It extends the Kummer cocycle κ₂ of the positive roots of 2: σ(2^{1/n}) = ζ_n^{κ₂(σ)}2^{1/n}.
- Λ₀ = {λ = 1, ρ₂ = 0}, the normalized elements.

**The H17 note** (hexagon:2611.00940; `reports_20261123/h17_note/h17_note_wb0007.tex`) proves:
- Theorem 2: GT̂ = Λ₀·G_Q;
- Λ₀ ⊂ Λ of Hatcher–Lochak–Schneps.

Check events: second reading `[ae4-23]` in `reports_20261123/h17_note/REVIEW_ae4ae3dc_v1.md`.

**Proved here: the quotient GT̂/Λ₀ is a Galois group, and ρ₂ mod 2 is Dirichlet.**

*Claim.*
- (a) On all of GT̂, ρ₂ ≡ ε₈∘λ (mod 2), where ε₈(λ) = 0 for λ ≡ ±1 (mod 8) and 1 for λ ≡ ±3 (mod 8). So the class of
  ρ₂ mod 2 in H¹(GT̂, F₂) is the pullback by λ of χ₈, the Dirichlet character of Q(√2).
- (b) Λ₀ is normal in GT̂.
- (c) GT̂/Λ₀ ≅ Gal(Q(μ_∞, 2^{1/∞})/Q). Through (λ, ρ₂) this is the subgroup
  {(λ, ρ) ∈ Ẑ^× ⋉ Ẑ(1) : ρ ≡ ε₈(λ) mod 2}, of index two in the semidirect product.

*Proof of (a).*
- Take F ∈ GT̂ and σ ∈ G_Q with χ(σ) = λ_F.
- Fσ⁻¹ has multiplier 1, so ρ₂(Fσ⁻¹) ∈ 2Ẑ. This is the note's Lemma 7(c), which I re-derived in the class-two quotient
  on 23 Nov.
- The cocycle law ρ₂(FG) = ρ₂(F) + λ_F ρ₂(G) gives ρ₂(F) = ρ₂(Fσ⁻¹) + κ₂(σ).
- Finally (−1)^{κ₂(σ)} = σ(√2)/√2. With √2 = ζ₈ + ζ₈⁻¹, this equals 1 if χ(σ) ≡ ±1 mod 8 and −1 if χ(σ) ≡ ±3 mod 8.

*Proof of (b).* For F ∈ Λ₀ and G ∈ GT̂:
ρ₂(GFG⁻¹) = ρ₂(G) + λ_G(ρ₂(F) + λ_F ρ₂(G⁻¹)) = ρ₂(G) + λ_G ρ₂(G⁻¹) = ρ₂(1) = 0, and λ(GFG⁻¹) = 1.

*Proof of (c).*
- Theorem 2 gives GT̂/Λ₀ = G_Q/(G_Q ∩ Λ₀). Here G_Q ∩ Λ₀ = {χ = 1, κ₂ = 0} = G_{Q(μ_∞, 2^{1/∞})}.
- For the image: the note's §5 shows that κ₂(G_{Q^ab}) = 2Ẑ, because 2^{1/n} ∈ Q^ab only for n ≤ 2.
- So for fixed λ the values κ₂(σ₀τ) = κ₂(σ₀) + λκ₂(τ), with τ ∈ G_{Q^ab}, fill κ₂(σ₀) + 2Ẑ = ε₈(λ) + 2Ẑ.

**What is transported.** Every invariant of GT̂ that factors through (λ, ρ₂) is a Galois invariant of the Kummer tower of
2 over Q. Everything else lives in Λ₀ ⊂ Λ, where the HLS formulas act on the whole pure tower.

**Where A enters.**
- The 1-dimensional characters of GT̂/Λ₀ that are trivial on Λ₀ factor through λ, together with ε₈∘λ. These are
  Dirichlet characters, and A governs their L-functions.
- Effectively: choose σ as a Frobenius at a small prime p, so that λ = p mod N and ρ₂ ≡ χ₈(p) mod 2 are prescribed.
  - This is a least-prime-in-progression problem modulo lcm(N, 8).
  - It is unconditional by A, through AN_GRH T07 (Lamzouri–Li–Soundararajan v3, Thm 1.1, as recorded in
    `intakes/AN_GRH/PRIMER_AN_GRH_20261123.md`). T01 (Bach) gives generators.
- **The boundary of A.** Prescribing ρ₂ mod 4 asks for a Frobenius in Q(i, 2^{1/4})/Q, whose group is D₄.
  - Its 2-dimensional representation is induced from a Kummer character ψ of Gal(Q(i, 2^{1/4})/Q(i)) ≅ C₄, so its
    L-function is the Hecke L-function L(s, ψ) over Q(i), the L-function of a weight-one dihedral theta series.
  - Effective Chebotarev there needs GRH for Hecke L-functions of Q(i), that is, M.
- The same boundary is recorded in AN_GRH: Hooley's theorem needs Dedekind GRH for Q(ζ_n, a^{1/n}), and K₃(2) already
  has the group S₃.

### 1.2 The two elliptic points and their CM characters (H17 Theorem 3; LM7_PUSH E.65; DELTA23 C4-C6)

**The objects.**
- B̂ = π₁^orb(M₁,₁), based at the cusp, ≅ Ĉ₂ ∐ Ĉ₃. Its generators s and r stabilize the two elliptic points:
  - j = 1728, the curve E₄: y² = x³ − x, with CM by Z[i];
  - j = 0, the curve E₃: y² = x³ + 1, with CM by Z[ω].
- The frames β_F and A_F conjugate s and r.
- Their level-12 images give two bits a₂, a₃, and δ = a₂ + a₃.

**The map on the Galois side** (DELTA23 C5, `[TPC]` in `intakes/DELTA23/INTAKE_DELTA23_20261121.md`, given C4).
- For σ ∈ G_{Q^ab}: W_σ = ρ₄(σ) and T_σ = κ(σ)ρ₃(σ), where ρ₃, ρ₄ are the adelic CM representations of E₃, E₄ and κ is
  the Kummer sign of r₀ = (3/4)^{1/4}.
- So the frames restrict, on Galois elements, to the two Hecke characters of Q(ω) and Q(i) attached to E₃ and E₄.
- DELTA23 C6 (`[TPC]`, given C4-C5): the frame image of the gentle group is N₃(4) × N₄(4), and the Galois image is the
  equal-parity subgroup of index two.

**What is compared.** By LM7_PUSH E.65 (E.65.13), the two bits on a Galois element are its action on one field:
Q(E₃[4]) = Q(i, r₀) = Q(x(E₄[3])).
- I verified the second equality on 23 Nov. The roots of 3x⁴ − 6x² − 1 are (√3 + 1)r₀/√3 and i(√3 − 1)r₀/√3, with
  √3 = 2r₀².
- The first equality and the E.1 sign identification are not checked (my review, point 4).

So δ = 0 on G_Q ∩ H is a class-field coincidence between the 4-division field of the j = 0 curve and the 3-division
x-field of the j = 1728 curve.

**What the H17 note transports.** Theorem 3 says δ = 0 on normalized GT̂.
- The mechanism is Proposition 18, the hexagonal self-similarity (Step 5).
  - For every E: y² = x³ + a₄x + a₆, the double cover branched at the four 3-division x-roots is Y² = Z³ + D/108,
    with D = 4a₄³ + 27a₆². This is the j = 0 curve again. I verified the identity on 22 Nov.
  - So M₁,₁ ≅ [(E₀ ∖ O′)/μ₆], with E₀: Y² = Z³ + 1.
- On fundamental groups, B̂ ≅ G₃ = q⁻¹⟨uv⟩ ⊂ Γ̂₁,₂, and Ψφ = Ad(h)φΦ_F.
- §9's parity algebra then reads a₃ ≡ k ≡ a₂. I re-derived it, with an exhaustive check over Z/12, on 22 Nov
  (`intakes/DELTA23/REFEREE_E49_A3_A7_20261122.md`).

**Where A enters.** It does not. The proof is finite-subgroup rigidity:
- Boggi–Zalesskii Theorem A at p = 2 and 3;
- Kerckhoff's realization;
- Hoshi–Minamide–Mochizuki Cor. C, opened on 23 Nov.

DELTA23's limit results show why this is needed:
- pronilpotent tests (F12);
- congruence tests (F18, `[TPC]`);
- cyclic covers (F21);
- fixed-target distribution relations (D1, `[TPC]`).

Each of these is blind to δ (`intakes/DELTA23/PRIMER_DELTA23_20261123.md` §3).

### 1.3 The anabelian line: cusp inertia and the weight-six class (RESEARCH_SA07 F.3.20, F.3.31-F.3.33; LM6 A.22)

**The objects.**
- The geometric π₁ of an affine hyperbolic curve over a number field.
- Closed procyclic subgroups whose arithmetic normalizer has open image.
- The common kernel R of all pro-ℓ quotients.
- Nakamura's universal arithmetic quotient in degree six, q_{g,6}: U_{g,6} → Q₆, which has rank 1 and character χ³
  (Nakamura 1996, (4.7.1)-(4.7.2), p. 117).

**The map.** Take a non-cuspidal z with open normalizer.
1. Nakamura 1994's full-class detector (Lemma 2.1.4, p. 96) gives a prime ℓ and a finite cover in which z has a nonzero
   ℓ-adic homology class a.
2. Then a normal core of genus ≥ 3, a rational cusp, and filling to a once-punctured curve.
3. A σ ∈ G_L(6) with q(D_σ) ≠ 0 acts on the line Q_ℓa with exponent one. So D_σ(a) = [Z₆, a] (FC.5b).
4. The single-line theorem (UC.1) says that q vanishes on U_{g,6} ∩ P_a. That is a contradiction.

**What our checks recorded.**
- `[F332]` and `[F3inputs]`, in `results_register/horizontal/sweep3/SA07/INTAKE_RESEARCH_SA07_2026112{1,2}_F3*`.
- The certificates of F.3.29, F.3.30, F.3.32 and F.3.34 were rerun.
- Nakamura 1994, 1995 and 1996 and Hain 1997 were opened at the source.
- F.3.24 and F.3.31 got a targeted proof check.
- F.3.33 was checked in part. Its printed statement is missing a clause.

**What is transported.** An open normalizer forces the weight-six Galois class. The class is a mixed-Tate object:
weight 6 and χ³ is the Tate twist Q_ℓ(3), the extension class of degree 3 in the Ihara Lie algebra (its relation to
K₅(Z) and Soulé's character: open at the source). The single-line algebra kills it.

**Where A enters.** It does not. The weight argument uses purity of curves (Weil) and the arithmetic quotient, not
L-functions.

### 1.4 Ihara's program and the Eisenstein ideal (K17; H06b = hexagon:2611.00939)

**The objects.**
- The pro-p outer Galois action on π₁(P¹ ∖ {0, 1, ∞}), with kernel field Ω_p^*.
- Ω_p, the maximal pro-p extension unramified outside p.
- Sharifi's map ϖ, from the plus part of the homology of X₁(p) relative to the cusps to H²(Z[1/p, μ_p], Z_p(2))^+.

**The map** (K17-VANDIVER-KERNEL; `intakes/K17/PRIMER_K17_20261123.md`, checked by ad855737, Claude Opus 5.5 at effort
high, with Wake–Wang-Erickson and Fukaya–Kato carried). Vandiver at p gives:
- X^+ = 0;
- ϖ an isomorphism (Wake–Wang-Erickson, Prop. 2.2.6 and Cor. 5.1.1-5.1.2);
- cup products of p-units generating H² (Fukaya–Kato §7.1.10);
- odd cups spanning H²(P, F_p).

The pole theorem then separates Magnus coefficients, and Ω_p^* = Ω_p. The Greenberg version, with X^+ finite, is the
deposited Ihara paper. At p = 2 the run proves Ω₂^* = Ω₂ by moments and the Amice transform (K17-P2-MOMENT).

**What is transported.** The Eisenstein quotient of GL₂ at level p (through ϖ) controls the H² relations, and those
control the relations of the pro-p Galois Lie algebra of the thrice-punctured line.

**Where A enters, through Alpöge's step 17** (K17-S17, checked). The Lean Selmer bound `OneCharU_s` gives
length S_ℓ(Q, 2k) ≤ 2Σ_ρ v_ℓ(tr ρ(s) − t), over the admissible 3-dimensional Galois representations ρ.
- These ρ come from compact U(3) forms and from S₁₃(Γ₀(3), χ₋₃).
- The strict Selmer group is dual to K_{4k}(Z){ℓ}.
- This yields K₁₂(Z) = 0 and the range k ≤ 12.

So a U(3) automorphic computation, reached through Alpöge's theta-lift chain (step 8), bounds a GL₁ Selmer group.

## 2. Towards global Langlands: the rungs

| Rung | Our objects | Our results (status as recorded) | A or M |
|---|---|---|---|
| GL₁/Q (Dirichlet) | λ on GT̂; ρ₂ mod 2 = ε₈∘λ; the cyclotomic coordinate of every finite level of GT̂₀ | §1.1 (a)-(c) proved here; AN_GRH T01, T07 | A: effective realization |
| GL₁ over K = Q(i), Q(ω), Q(μ_{2^k}) (Hecke characters) | the CM frames at the elliptic points; ρ₂ mod 2^k (k ≥ 2); Ψ₃/2 (the Kummer bit of 3^{1/4}) | H17 Thm 3 (δ = 0); DELTA23 C5-C6 | effective forms need M |
| GL₂/Q dihedral (theta series = automorphic induction from the rung above) | the same data, seen in GL₂: the CM newforms of E₃, E₄; the weight-one theta series of the D₄ Kummer field | the identification is the induction formula; no run result beyond §1.1 | M |
| GL₂/Q Eisenstein (level p) | Sharifi's ϖ; Ihara's kernel field | K17-VANDIVER-KERNEL; H06b (Greenberg) | none |
| U(3) (theta lifts, Alpöge step 8) | admissible 3-dimensional ρ controlling K_{4k}(Z) | K17-S17, K₁₂(Z) = 0 | A's archive (`OneCharU_s`) |
| Mixed Tate (Ext¹ of GL₁ objects) | the weight-six class χ³; Soulé-type classes | RESEARCH_SA07 F.3.31-F.3.32 | none |
| Orbifold torsion of the modular curve | the elliptic points, finite subgroups C₂², C₃², C₂ | H17 Thm 1, Thm 3 | none |

**Functoriality instances.**
- **Automorphic induction from K to GL₂/Q.** The CM frames, and the Kummer layer ρ₂ mod 2^k, k ≥ 2.
- **Theta lifts between unitary groups.** Alpöge step 8, used in K17.
- **Base change Q → Q(μ_N).** The cyclotomic tower in which GT̂'s finite levels are tested (AN_GRH T02-T05).

**The trace formula.** It appears only as a permutation trace (DELTA23 P18, `[TPC]`). Multiplier-one GT̂ permutes the
Nielsen classes C^n/G compatibly with the Drinfeld action. On a Galois element the fixed points of that permutation are
the Galois-stable covers in an isolated Hurwitz orbit. Over finite fields, their count would be a Frobenius trace on the
Hurwitz space.

**The next rungs, as concrete statements:**
1. **Effective H17 decomposition, under M.** For k ≥ 2, under GRH for the Hecke L-functions of Q(μ_{2^k}), give an
   explicit X(N, k) such that every (λ mod N, ρ₂ mod 2^k) in the image of (c) is realized by Frobenius elements at
   primes p ≤ X(N, k). The first case is k = 2: the order-4 Kummer characters of Q(i).
2. **GT̂ and Hecke correspondences.** For F ∈ Λ₀ and N ≥ 2, Φ_F preserves the closure of Γ₀(N) in B̂ up to conjugation,
   and commutes, up to inner automorphisms, with the two degeneracy maps Γ̂₀(N) → B̂ (z ↦ z and z ↦ Nz).
   - The congruence part is DELTA23 F18 (`[TPC]`): gentle elements act innerly on the congruence completion.
   - The second degeneracy map is conjugation by diag(N, 1), outside PSL₂(Z). It asks whether Φ_F extends to the
     completion of the commensurator. That is the GL₂ Hecke rung for GT̂.
3. **Ihara beyond Vandiver and Greenberg** (K17 open row Q3-IRREG). The remaining plus characters need the Eisenstein
   ideal where the Hecke algebra is not Gorenstein. T-INTEGRAL37, the failure of integral odd generation at p = 37 in
   weight 32 (McCallum–Sharifi Thm 9.7, statement level), is the test case.

## 3. Structural notes: the same mechanism twice

**(i) Symmetry eigenspaces read modulo a small prime.**

| | H17 | Ihara/Sharifi |
|---|---|---|
| Group acting | μ₆ = Aut(E₀) on the CM lattice 𝓛̂ = Ẑ[ω] | Gal(Q(μ_p)/Q) = (Z/p)^× on class groups and H² |
| Eigenspace | the line ker(R + I) mod 3, on which a₃ is read | the ω^k-eigenspaces, the plus part X^+ |
| Parity | Lemma 15: ν ≡ 1 mod 3, ν ≡ (−1)^{a₂} mod 4 | odd cups span H²(P, F_p) "by parity" |
| Conclusion | δ = 0 | Ω_p^* = Ω_p |

The dictionary: "the CM unit ν ∈ Ẑ[ω]^× acting on the eigenline" corresponds to "the Teichmüller character on the
cyclotomic eigenspace". In both, a global statement is decided by a parity on one eigenspace of a finite cyclic group of
automorphisms.

**(ii) The A/M boundary at a Kummer extension.**
- §1.1: ρ₂ mod 2 is Dirichlet (χ₈), while ρ₂ mod 4 is dihedral over Q(i).
- AN_GRH: Hooley's theorem needs Dedekind GRH for Q(ζ_n, a^{1/n}).

In both, the cyclotomic part, GL₁/Q, is governed by A. The Kummer part is GL₁ over a cyclotomic field, induced to GL₂
or GL_d over Q, and is governed by M. The boundary is the first non-abelian Kummer layer: D₄ for 2^{1/4}, S₃ for 2^{1/3}.

**(iii) Finite-subgroup rigidity as against pronilpotent blindness.** H17 is a torsion phenomenon.
- δ passes every pronilpotent, congruence, cyclic-cover and distribution test (DELTA23 F12, F18, F21, D1).
- It is decided only by the finite subgroups C₂², C₃², C₂ of profinite mapping class groups (Boggi–Zalesskii).
- In the project's terms, Δ ≠ 0 on GT̂₀ is a ghost in the gentle group: invisible to every graded or pro-unipotent test,
  seen only at the orbifold points.
- The anabelian line has the reverse pattern. R (§1.3) is invisible to every pro-ℓ quotient, and is reached by passing
  to finite covers (Nakamura's detector) and then a pro-ℓ weight argument.

## 4. What it suggests, most promising first

1. **The structure of GT̂ over its arithmetic quotient.**
   - By §1.1(c), GT̂ is an extension of Gal(Q(μ_∞, 2^{1/∞})/Q) by the normal subgroup Λ₀ ⊂ Λ.
   - Next: compute H¹(Λ₀, F₂)^{GT̂}, i.e. the quadratic characters of Λ₀ invariant under GT̂.
   - Compare it with the countably infinite family of quadratic characters vanishing on GT̂ (GT_TOWER_CHECK B.2.25,
     LM8_PUSH C.30, recorded in the DELTA23 intake).
   - The question: which of them come from Λ₀, and which from the gap GT̂₀ ∖ GT̂?
2. **GT̂ and the degeneracy maps of Γ₀(N)** (rung 2, statement 2). Start at N = 2, 3, where Γ₀(N) contains the elliptic
   stabilizers' conjugates, and test on the finite quotients used in DELTA23 P17-P18.
3. **The effective decomposition (rung statement 1)**, at k = 2. Write down the Hecke characters of Q(i) cutting out
   Q(i, 2^{1/4}) and their conductors. Then state the least-prime bound under M with explicit constants.
4. **Ihara at the remaining plus characters** (K17 Q3-IRREG), through the non-Gorenstein Eisenstein ideal; p = 37 is the
   test case.
5. **The supersingular algebra (−1, −3) at 3 as an invariant of the frame pair** (DELTA23's open thread). Both frame bits
   are 3-adic (DELTA23 L8, `[TPC]`). Find a single invariant of (T₃, W₃) with values in Br(Q₃)[2] that reads (−1)^δ.
