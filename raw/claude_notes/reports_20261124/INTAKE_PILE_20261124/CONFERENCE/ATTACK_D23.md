# Attack-read of LM8_PUSH D.23 (Session 6)

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6.
- **Object:** the global part of "Fermat's theorem for Selmer sections, for every odd exponent".
- **Where it is:** LM8_PUSH checkpoint 17, `answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped\sections\D.tex`, in
  `<local>/Documents\longue_marche_pro_pilot_20261104\`:
  - D.22: lines 1580-1635;
  - D.23: statement at lines 1637-1650, proof at lines 1651-1925.
- **Check events:** `ATTACK_D23_CHECK_EVENTS.tsv`.
- **Computations:** `checks\attack_d23_checks.py`, with its output in `checks\attack_d23_checks.out`. They use exact
  arithmetic, except for the L-values, which are series with stated tail bounds.

I read D.23 in full in order to break it. I opened every input it cites at its source, except Kriz–Li (not needed, see
§3.6), and I recomputed every number it uses for n = 3, 5, 7.

## Verdict

**D.23's global part holds.** I found no mathematical gap. It needs two repairs before it goes into a paper, and
neither touches the mathematics.

1. **The modularity step cites the qualitative form of Serre's conjecture** (lines 1795-1803). The step cites
   Khare–Wintenberger (I), Theorem 9.1, as "the precise Serre modularity theorem".
   - That theorem reads "Assume Hypothesis (H). Then Serre's conjecture is true." It is proved through (D_r) and their
     Theorem 3.4, whose conclusion is that ρ̄ "is modular", i.e. arises from some newform.
   - Kisin's Corollary (0.2), which completes it, has the same form: "Then ρ̄ is modular."
   - D.23 uses a newform of weight k(ρ̄) = 2 and level N(ρ̄) | 2. That is the refined form. For odd residue
     characteristic it follows from the qualitative form by the known passage to the optimal level and weight. Khare
     and Wintenberger recall that passage in their §1.1, and their Theorem 1.2(2) supplies its last case, in
     characteristic 2.
   - **Repair:** cite Khare–Wintenberger (I) and (II) and Kisin for modularity, and Ribet (Invent. Math. 100, 1990),
     Edixhoven (Invent. Math. 109, 1992) and Diamond ("The refined conjecture of Serre", 1995) for the level and
     weight. Open them at their exact statements when the paper is written.
2. **The statement of D.23 joins a theorem and a conditional corollary.** "Every Selmer section is cuspidal", and the
   description of the Selmer sections as three disjoint packets, are unconditional. "Every full section is Selmer"
   rests on D.56, the local point-or-cusp theorem (the stipulated p-adic section theorem of 6 Oct), and on the real
   section theorem. Neither is part of the global argument, and I did not check them. A paper must state the two
   separately (§1).

Session 6 asked whether D.23 is a proof. For the global part, yes. The weakest steps are the modularity citation and
the finite-support argument (§3.1). I attacked the finite-support argument hardest, because it is D.23's own condensed
argument and it sits next to an erratum of Stoll. It survives.

## 1. The statement that may go into a paper

**Theorem (Fermat's theorem for Selmer sections).**
- **Setting:** let n ≥ 3 be odd, and let U_n ⊂ P²_Q be the affine Fermat curve X^n + Y^n + Z^n = 0, XYZ ≠ 0. Its
  rational cusps are y₁ = (0 : −1 : 1), y₂ = (−1 : 0 : 1) and y₃ = (1 : −1 : 0).
- **Hypothesis:** let s be a section of π₁(U_n) → G_Q such that, for every place v of Q, the restriction of s to
  G_{Q_v} is either induced by a Q_v-point of U_n or contained in the decomposition group of a Q_v-rational cusp. For
  v = ∞ this means a real point or a real cusp.
- **Conclusion:** s is a cuspidal section at one of y₁, y₂, y₃.
- **The Selmer sections:** they are the disjoint union of the three packets S_{π₁(U_{n,y_i}/Q)}. Each packet is a
  torsor under H¹(Q, Ẑ(1)), the profinite completion of Q^×.

**Corollary (conditional).** Assume that every section of π₁(U_n) → G_Q is Selmer. This would follow from a p-adic
point-or-cusp theorem for U_n and its section neighbourhoods over every Q_p, together with the real section theorem
(D.56). Then the set of all sections is the disjoint union of the three packets.

**Inputs of the theorem:**
- Serre's conjecture in its refined form (repair 1);
- Stoll, Theorem 8.2 and Corollary 8.8, with his 2017 errata;
- Mazur, Theorem (8);
- Serre 1987, §2.8, Proposition 4;
- Stix, Proposition 8, Theorem 14 and Remark 15(2), for the packets.

## 2. The argument and what I checked

| Step (D.tex lines) | Content | Check |
|---|---|---|
| Finite-support argument (1651-1698) | If at every finite place the local points of a Selmer section lie in a finite Z ⊂ X, the section is a point or cusp section; hence the same holds when the compactification maps nonconstantly to a proper W with W(A_Q)^{f-cov}_• = W(Q) | Re-proved (§3.1). Stoll Thm 8.2 read at the source |
| Residual representation, local points (1699-1724) | ρ̄_s through the Legendre family, det = χ̄_ℓ; (D.23.1) v_p(j) = 8v_p(2) − 2ℓ\|v_p(a)\|; at 2 always potentially multiplicative; at odd p good, or Tate with ℓ \| v_p(q) | Re-derived by hand; agrees with Steklov Lemma 5.11 and Lemma 5.12 |
| Local cusps (1726-1735) | (D.23.2) [q(s)]_ℓ = [2⁻⁸]_ℓ at all three cusps and for every section in the packet | Recomputed for n = 3, 5, 7, 9, 11 (§4). The twist at the cusp over λ = ∞ depends on the section (§3.2) |
| Local consequences (1737-1777) | Unramified at odd p ≠ ℓ; finite flat at ℓ, hence weight 2 (Serre §2.8 Prop. 4); tame at 2, conductor exponent ≤ 1 | Serre Prop. 4 read at the source; the rest re-derived |
| Patching and modularity (1779-1805) | A global quadratic character twists away the local twists; level \| 2, weight 2; irreducible ⇒ absolutely irreducible; Serre ⇒ S₂(Γ₀(1 or 2)) ≠ 0, false | KW (I) §1.1, §3, §9 and Kisin pp. 1-2 read: **repair 1**. S₂(Γ₁(N)) = 0 for N \| 2, so the nebentypus remark is not needed |
| Lift and map to X₀(4ℓ) (1806-1842) | Reducible ⇒ the section lifts to the component W₀ of U_ℓ ×_tripod Z_ℓ; W₀ → Y₀(4ℓ) nonconstant; (D.23.3) g(X₀(4ℓ)) = (ℓ−3)/2 | (φ′)⁻¹⟨Q⟩ cyclic of order 4 re-derived; index, cusps and genus computed for ℓ ≤ 23 |
| Stoll for X₀(4ℓ) (1835-1842) | X₀(4ℓ)(A_Q)^{ab}_• = X₀(4ℓ)(Q) | Stoll Cor 8.8 read at the source (§3.4); analytic rank 0 of 20a1, 14a1, 26a1 and 26b1 computed |
| Excluding points (1843-1873) | Diagonal characters 1 and χ̄_ℓ; after the twist (and the dual isogeny) Z/2 ⊕ Z/2ℓ ⊂ E(Q)_tors, impossible by Mazur (8) for ℓ ≥ 5 | Mazur (8) read at the source; argument re-derived |
| n = 3 (1874-1904) | F₃ ≅ v² + v = u³ − 7 (Cremona 27a1) ≅ y² = x³ − 432; E(Q) = the three cusps | Identity, cusp images, point counts and L(27a1, 1) computed (§4) |
| Composite n, packets (1905-1925) | U_n → U_ℓ finite étale; intersect with the cusp decomposition group; packets by Stix | Re-derived; Stix Prop 8, Thm 14 and Rmk 15(2) read at the source |

## 3. Where I attacked

### 3.1 The finite-support argument

This is D.23's own argument, and it is written tightly. Steklov has the same step as an unread proposition
("prop:finitedescentmoduli"), and Stoll's erratum concerns exactly the real places of such an argument. I re-proved it
as follows.
- **Neighbourhoods.** Take a characteristic open N ⊂ π₁(U_Q̄) and put H_N = s(G_Q)·N. The H_N are cofinal among open
  subgroups containing s(G_Q), and their intersection is s(G_Q). The curves X_{H_N} are geometrically connected, and
  those of genus ≥ 1 are cofinal.
- **The lifted section is Selmer.** If s|G_{Q_v} = γ s_x γ⁻¹, then D_{γx̃} ⊂ H, so the image of γx̃ in U_H is
  Q_v-rational and induces the lift. For a cusp, D_c̃ ∩ H surjects onto G_{Q_v}, so the cusp below is rational.
- **The adelic point lies in the finite-descent set.** It lies in X_H(A)^{f-cov}_•: evaluate each torsor on s, and at a
  cusp use that the torsor is étale over the cusp. This set is contained in the ab set.
- **Stoll's Theorem 8.2.** Stoll, Theorem 8.2 (arXiv math/0606465, §8, label BM0) reads: "if P ∈ C(A_k)^ab is such that
  P_v ∈ Z(k_v) for a set of places v of k of density 1, then P ∈ Z(k)", for C of genus ≥ 1 and Z finite.
  - The errata of 29 Mar 2017, §3, say that the proof of Proposition 8.5 (the deduction from a map to W) fails at real
    places. The repair is this density-one form, which uses only the finite places.
  - D.23 uses exactly that form (lines 1669-1675).
- **Passing to the limit.** Because X_H(Q) → X_H(Q_p) is injective, the rational point given at each level is unique,
  so the points are automatically compatible; no compactness argument is needed. A compatible system of cosets g_H·H
  with g_H⁻¹ D_x̃ g_H ⊂ H gives g with g⁻¹ D_x̃ g ⊂ ⋂H = s(G_Q). So s is the section of a point, or, if x is a cusp, lies
  in its decomposition group.

**Result:** sound.

### 3.2 The local conditions

**The cusp constant.**
- D.22.2, q(s) = κ(a) + e·κ_t(s) for q = a·t^e·h with h ∈ 1 + tk[[t]], is right. A principal unit has an m-th root for
  every m.
- At all three rational cusps 1/j = 2⁻⁸ t^{2n}(1 + O(tⁿ)); computed exactly in §4.
- Since e = 2ℓ, every section in a packet has the class [2⁻⁸] mod ℓ, as (D.23.2) states.

**A point D.23 leaves implicit.**
- At the cusp over λ = ∞ the Legendre family is a ramified quadratic twist of the Tate curve. There −c₄/c₆ ≈
  −1/(4λ) = s^ℓ/4, an odd power of the parameter, and the local monodromy is −T^{2ℓ}.
- So the quadratic character in "a quadratic twist of the Tate extension" depends on the section's tangent class. This
  is Steklov's ε_s, Proposition 4.5.
- The patching handles it, because any local quadratic character on inertia is allowed. A paper should say so.

**At 2.**
- Every Q₂-point has v₂(j) = 8 − 2ℓ·m with m ≥ 1. At 2 one of v₂(a) ≠ 0 or v₂(b) > 0 holds, since a, b both units would
  give a^ℓ + b^ℓ + 1 ≡ 1 (mod 2).
- So the representation is a twisted Tate representation. After the twist, inertia acts unipotently, through a quotient
  of order ℓ, which is tame.
- The conductor exponent is therefore ≤ 1, both at points and at cusps (v₂(2⁻⁸) = −8 ≢ 0 mod ℓ).

**At ℓ.** The good-reduction case gives the finite flat E[ℓ], and the Tate case with ℓ | v(q) gives a unit Kummer class.
Serre's Proposition 4 (§2.8, "Conditions pour que k = 2") gives k = 2 if and only if det ρ̄|I = χ and ρ̄ is finite at p.

**Result:** sound.

### 3.3 The modularity step

The mathematics is right:
- ρ̄′ is odd with det = χ̄_ℓ;
- the complex-conjugation argument gives absolute irreducibility;
- the level divides 2 and the weight is 2;
- S₂(Γ₁(1)) = S₂(Γ₁(2)) = 0, since Γ₁(2) = Γ₀(2) and X₀(2) has genus 0.

The citation is not: see repair 1. The hypothesis (H) of Khare–Wintenberger (I), §9, is a 2-adic modularity lifting
statement. Kisin's abstract says his Theorem (0.1) "proves hypothesis (H) of Khare-Wintenberger".

### 3.4 Stoll's Corollary 8.8 for X₀(4ℓ)

Stoll's Corollary 8.8 (label ModCurves) reads: "If C/Q is one of the modular curves X₀(N), X₁(N), X(N) and such that the
genus of C is positive, then C is excellent w.r.t. abelian coverings." By Definition 6.1(6), that means
X(k) = X(A_k)^ab_•. So D.23's gloss, "equality with the rational points, not merely their adelic closure", is accurate.

Stoll's proof:
- for N divisible by a prime p = 11 or p ≥ 17, it maps X₀(N) to X₀(p), using Mazur's analytic-rank-zero factor of
  J₀(p);
- for the other minimal levels it uses Stein's tables;
- in both cases it then applies Theorem 8.6.

For N = 4ℓ the levels in play are 20, 14 and 26 for ℓ = 5, 7, 13. L(20a1, 1), L(14a1, 1), L(26a1, 1) and L(26b1, 1)
are all nonzero (§4).

Errata §2, item (6), states that the curve statements about C(A_k)^{f-ab} remain valid.

**Result:** holds.

### 3.5 Excluding points

The argument is right and checks the diagonal characters correctly:
- at 2, the semisimplification is trivial on inertia;
- at ℓ, the supersingular case is excluded because its inertia representation is irreducible;
- Minkowski's theorem applies to the character that is trivial at ℓ.

Mazur's Theorem (8) (Publ. IHES 47, introduction) allows Z/2 × Z/2ν only for ν ≤ 4. So Z/2 ⊕ Z/10 and Z/2 ⊕ Z/14 are
excluded, and ℓ = 5 and ℓ = 7 are covered without Y₁(ℓ)(Q) = ∅.

### 3.6 n = 3 and composite n

**n = 3.** The substitution u = −3Z/(X+Y), v = (9(X−Y)/(X+Y) − 1)/2 gives v² + v − (u³ − 7) = 27(X³+Y³+Z³)/(X+Y)³.
- The curve is Cremona 27a1, with discriminant −3⁹.
- #E(F₅) = 6 and #E(F₇) = 9, so the torsion divides 3.
- The cusps go to O, (3, −5) and (3, 4).
- L(27a1, 1) = 0.58887958343 ≠ 0.

The identification with X₀(27) through Kriz–Li §10.1 (not opened by me) is not needed. Stoll's Corollary 6.4, that a
modular abelian variety of analytic rank zero is excellent, applied to 27a1 gives the same equality.

**Composite n.** The power map U_n → U_ℓ is finite étale. The image section is Selmer and hence cuspidal, and
π₁(U_n) ∩ D_c is the decomposition group of a rational cusp above c.

**Result:** sound.

## 4. Small exponents by computation

All of the following is in `checks\attack_d23_checks.out`, and every assertion passes.

| What a computation decides | Result |
|---|---|
| Leading term of 1/j at X/Z = 0, Y/Z = 0, Z/X = 0, n = 3, 5, 7, 9, 11 | 2⁻⁸ t^{2n}, next term at t^{3n}, at every cusp (D.22.3) |
| κ(2⁻⁸) mod ℓ at 2 | −8 ≡ 1, 2, 6 (mod 3, 5, 7): ramified at 2 for n = 3, 5, 7 |
| κ(2⁻⁸) mod ℓ at odd p | 2⁻⁸ is not an ℓ-th power mod p for p = 7 (ℓ = 3), 11 (ℓ = 5), 29 (ℓ = 7), 23 (ℓ = 11), 53 (ℓ = 13): the cusp representation is non-split and unramified there |
| n = 3 | F₃ → 27a1 identity; cusps → O, (3,−5), (3,4), each of order 1 or 3; #E(F₅) = 6, #E(F₇) = 9 |
| Analytic rank 0 (root number +1, checked by independence of the cut parameter) | L(27a1,1) = 0.588879583428; L(20a1,1) = 0.470729190327; L(14a1,1) = 0.330223659344; L(26a1,1) = 0.515576651277; L(26b1,1) = 0.620965349549 (tails < 10⁻⁵²) |
| (D.23.3) | Index 6(ℓ+1), 6 cusps, ν₂ = ν₃ = 0, g(X₀(4ℓ)) = (ℓ−3)/2 for ℓ = 3, …, 23; g(X₀(10)) = 0 |
| E.10 | y² − xy − 4y = x³ − 4x²: Δ = −1664 = −2⁷·13; multiples of (0,0): (4,8), (2,2), (2,4), (4,0), (0,4), O, so (0,0) has exact order 7 |

So n = 5 rests on X₀(20), which has genus 1 and Jacobian of analytic rank 0. Steklov's X₀(10) has genus 0, which is
why his method stops at ℓ ≥ 7. n = 7 rests on X₀(28) → X₀(14), and n = 3 on 27a1.

## 5. The two Steklov errors, as our runs state them, rechecked

Source: Benjamin Steklov, *Fermat's Last Theorem for Selmer sections*, arXiv:2602.17746v2. I opened the TeX of v2.
Statement numbers follow his shared counter and agree with the runs' citations.

**(a) The cusp divisibility.**
- **Our runs:**
  - LM8_PUSH D.22: "The divisibility assertion in Steklov's Proposition 4.6, and its use to split the residual
    representation in Proposition 5.10, are false as written." Its formula is q(s_O) = κ(256⁻¹), of 2-adic valuation
    −8.
  - FERMAT_SUCCESSOR A.4 (checkpoint 06, `deliverable\sections\A_main.tex`): q(s) = −8κ(2) over Q₂ for ℓ = 5, which
    is nonzero in H¹(Q₂, μ₅).
- **At the source:** Proposition 4.6 states q(f(s)) ∈ e·H¹(k, Ẑ(1)). Its proof identifies V_y^∧ → (A¹)^∧_∞ with
  Spec k((1/j^{1/e})) → Spec k((1/j)). That requires the leading coefficient of 1/j to be an e-th power in k. At the
  Fermat cusps it is 2⁻⁸ with e = 2ℓ, so the proposition is false there.
- **Its use:** in the proof of Proposition 5.10, it yields ρ̄_{s₀,ℓ} ≅ diag(χ̄_ℓ, 1) ⊗ ε. That is false: the class
  [2⁻⁸] is ramified at 2, and it is non-split at the odd primes in §4.
- **Rechecked:** confirmed.
- **Refinement for the paper and for the e-mail:**
  - The conclusion of Proposition 5.10, that every cuspidal section is ℓ-Fermat, still holds. Steklov's
    Definition 5.8 asks only for n₂ ≤ 4 at 2, the true exponent is ≤ 1, and the conditions at the other primes hold by
    §3.2.
  - So error (a) breaks a proof, not a conclusion.
  - With Proposition 5.10 re-proved as in D.23, Steklov's Theorem A stands for ℓ ≥ 11. His Corollary 5.6 already has
    that range.

**(b) The seven-torsion.**
- **Our runs:** LM6 E.10 and FERMAT_SUCCESSOR A.9 state: "The claim Y₁(7)(Q) = ∅ used in the last sentence of
  Steklov's Theorem 5.14 is false", by (0,0) of order 7 on y² − xy − 4y = x³ − 4x².
- **At the source:** Case 2 of the proof of Theorem 5.14 (which is Theorem A, "ℓ ≥ 7") says: "By Mazur's Torsion
  Theorem [Theorem (8)] the stacks Y₁(ℓ) ≅ Y(μ_ℓ) have no Q-points for ℓ ≥ 7." This is false at ℓ = 7, since Mazur's
  list contains Z/7.
- **Rechecked:** confirmed by the computation in §4.
- **Steklov's own range:** his Corollary 5.6 has ℓ ≥ 11.
- **Consequence:** as printed, ℓ = 7 is unproved. D.23's full-2-torsion argument repairs it.

Minor, for the e-mail: in the proof of Lemma 5.12, Case 2, "8v_p(2) − |v_p(λ′)|" lacks the factor 2. The final value
is right.

## 6. Beyond Steklov, exponent by exponent

| Exponent | Steklov 2602.17746v2 | D.23 |
|---|---|---|
| Prime ℓ ≥ 11 | Claimed. The proof needs Proposition 5.10 re-proved (error a); the result stands | Proved independently; the correction D.22 is ours |
| ℓ = 7 | Claimed. The proof fails at the Mazur step (error b) | Proved (Z/2 ⊕ Z/14) |
| ℓ = 5 | Not claimed (X₀(10) has genus 0) | Proved (X₀(20), Z/2 ⊕ Z/10) |
| ℓ = 3 | Not claimed | Proved (F₃ ≅ 27a1) |
| Composite odd n | Not stated | Proved: new where every prime factor is 3, 5 or 7; otherwise from the ℓ ≥ 11 case by the same covering |
| The Selmer section set | Not stated | Three disjoint H¹(Q, Ẑ(1))-torsors (Stix) |
| All sections | — | Conditional on the local theorem D.56 |

## 7. Not checked here

- D.56 and the real section theorem. They are outside the global part.
- Ribet 1990, Edixhoven 1992 and Diamond 1995, the references for repair 1. I have not opened them.
- Stoll's own inputs for Corollary 8.8 (Mazur's rank-zero factor of J₀(p) and Stein's tables). I carried them as
  published background; §4 covers the five curves used here.
- Steklov's "prop:finitedescentmoduli", which D.23 does not use.
- Kriz–Li §10.1, which is not needed (§3.6).

## 8. On prompt 3

From this read the answer is yes. D.23's global part is a proof. Prompt 3 should ask for four things:
- the statement of §1, with the unconditional theorem and the conditional corollary kept separate;
- repair 1;
- the remark of §3.2 on the twist at the cusp over λ = ∞;
- the corrections to Steklov as in §5. In particular, the paper should say that error (a) does not affect his
  conclusion for ℓ ≥ 11 once Proposition 5.10 is re-proved, and that ℓ = 7 is unproved as printed.
