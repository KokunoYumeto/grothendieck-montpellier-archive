# H17 note, second reader (v1)

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 23 Nov 2026. The note was written by the editor a49aabbf
(Claude Fable 5.2 at effort max) from mathematics by GPT-6 Astra (ChatGPT Pro mode). I did not edit the note. Check
events: `REVIEW_ae4ae3dc_v1_CHECK_EVENTS.tsv`.

## What the note settles, and whether it holds

**What it settles.** Nakamura and Schneps (Invent. Math. 2000) left open whether their relation (IV) cuts out a proper
subgroup of GT̂. Lochak-Nakamura-Schneps (arXiv:2602.12462, §1) still called this "unclear" in February 2026. The note
proves:
- **Theorem 1:** (IV) holds for every element of GT̂. So their subgroup IΓ is cut out by (III′) alone.
- **Theorem 2:** GT̂ = Λ₀·G_Q with Λ₀ ⊂ Λ. So, up to Galois elements, every element of GT̂ acts on the whole pure tower
  by the formulas of Hatcher-Lochak-Schneps.

Who gains:
- **Specialists in GT̂ and in anabelian geometry.** This concerns the open comparison G_Q ⊂ IΓ ⊂ GT̂, and it makes the HLS
  action available for GT̂ modulo Galois.
- **Our programme.** Theorem 3 and Corollary 4 settle H17 (Δ = 0 on GT̂), conditionally on the two cited properties of
  Δ (point 4 below).

**Whether it holds.** In the parts no one else had read, I found no mathematical error:
- Sections 4 and 8;
- the editor's rewritten proofs (Lemmas 9, 13 and 15, both halves of Proposition 11, Step 2 of Proposition 18);
- the decomposition in Theorem 2.

I followed every step, re-derived the matrix and braid identities myself, and opened Hoshi-Minamide-Mochizuki and
Nakamura-Schneps at the source.

The corrections below are about citation and precision. The one substantive caveat (point 4) concerns a remark
outside the theorems.

## 1. The parts refereed

**Theorem 2, the decomposition F = F_*σ (Section 5): correct.**
- **Normalization of ρ₂.**
  - NS §1 defines the Kummer 1-cocycle ρ₂: G_Q → Ẑ(1) of the *positive* roots of 2, by σ(2^{1/n}) = ζ_n^{ρ₂(σ)} 2^{1/n},
    with no factor.
  - NS Definition 5.1 extends it to GT̂ by g_F ≡ (xy)^{ρ₂(F)} mod F̂′, and notes that ρ₂(F) = ρ₂(σ) on Galois elements.
  - The note's Definition 6 and Lemma 7(a), (d) agree with this: g_F = β_F⁻¹.
  - I re-derived Lemma 7(c) in the class-two quotient. There [y,z] = [z,x] = [x,y], so (II) forces f ≡ 1, and
    g(y,x)⁻¹g(x,y) = [x,y]^{ρ²+2d} gives ρ ∈ 2Ẑ.
- **Reach of the cocycle.** The proof needs σ with the same λ and the same ρ₂; both are needed, since
  ρ₂(F_*σ) = ρ₂(F_*) + ρ₂(σ) when λ_{F_*} = 1.
  - On G_{Q^{ab}}, ρ₂ is a homomorphism with image exactly 2Ẑ. Its image lies in nẐ if and only if 2^{1/n} ∈ Q^{ab},
    which holds for n = 1, 2 only: √2 ∈ Q(μ₈), while Q(2^{1/4}, i) has group D₄.
  - So the image is 2Z₂ × ∏_{ℓ odd} Z_ℓ.
  - The value needed, ρ₂(Fσ₀⁻¹), lies in 2Ẑ by Lemma 7(c). So the √2 ∈ Q(μ₈) point is handled exactly.
- **The Λ half.**
  - The two forms f(u, v⁴) = f(u², v²) = f(u⁴, v) are correct.
  - Schneps p. 670 makes Π central modulo the centre. Π lies in the closed commutator subgroup and Ω = (abc)⁴ has degree
    12, so Π = 1.
  - The Fable referee re-proved Schneps's step on 18 Nov (event DR08).

**Section 4 (Theorem 1): correct.**
- **Lemma 9 (rewritten).** The deduction from Boggi-Zalesskii is correct:
  - (a) conjugate α(H) ⊂ P̂ ⋊ H into PH, and use P̂ ∩ Γ = P;
  - (b) the centralizer is the kernel of N → Aut(H), an open subgroup of the closure.

  I did not reopen BZ's hypotheses. The Fable referee opened BZ Theorem A on 18 Nov for p = 2.
- **The Klein configuration.** Kerckhoff realization, the Möbius normalization (a′ = −t, b′ = 1/t, C_± = ±i), the
  connectedness of Z and the half twist θ are all correct.
- **The two forgetting maps.** T(w) = 2(w+6)/(w−2) is an involution fixing −2 and 6. Only S exchanges the classes of d
  and z.
- **Proposition 10.** Checked line by line:
  - centralizers by Herfort-Ribes;
  - K₀ is free on z and d²;
  - the class of k is (4c, 2c), so s = 4c and t = −4c;
  - the lift through J with central (uv)³;
  - the character u ↦ 1, v² ↦ 0 gives e = −2c.
- **Proposition 11, the first half (rewritten).** Verified with x = u², y = v² = sxs⁻¹:
  - j(z) = x, j(d) = u⁻¹vu = x⁻¹s, j(a) = s;
  - j(d²) = u⁻¹v²u = x⁻¹y⁻¹, because (uv²)² = (uv)³ = 1 in B;
  - c₀Φ_F(c₀)⁻¹ = u⁻¹(sβs⁻¹β⁻¹)u^λ = u⁻¹fu^λ, because ϑ = Ad(s) and s² = 1 in B;
  - j(h) = u⁻¹fu;
  - hence jφj⁻¹ = Ad(u^{λ−1})Φ_F.
- **Proposition 11, the second half.** Verified: L(g) = 4c and L(b) = m − 2ρ₂ give 4(c − ρ₂) = 0.

**Section 6, the rewritten lemmas: correct.**
- **Lemma 13.** Re-derived:
  - the lower-left entries of UMU = MUM give γ(1+γ) = 0;
  - with γ = −1 the upper-left entries give β = (α−1)², and U^tLU^{−t} = [[1−t, t²], [−1, 1+t]];
  - modulo 4, U² and L² commute, so the image of F̂ is abelian and t ≡ 0;
  - modulo 3, the classes of U and L agree in SL₂(F₃)/Q₈, so t ≡ −ρ₂.
- **Lemma 15.**
  - ν = 1 + (ζ−1)φ = 1 + ωφ;
  - (b, ω^j)(ζ, −1)(b, ω^j)⁻¹ = (2b + ω^jζ, −1);
  - ker κ = 2𝓛̂ ⋊ {±1}, by index 12 = |A₄|;
  - so j = 0, b ≡ a₂ζ mod 2, and ν ≡ (−1)^{a₂} mod 4.

**Section 8, Proposition 18: correct.**
- **Step 2 (rewritten).**
  - C^+ → C is an isomorphism, since C^+ ∩ K₃ = C_{K₃}(ι) = 1.
  - Γ̂_{0,[8]} acts faithfully on Φ̂ [As], so an element of Ĉ^+ acting trivially on Π̂^+ maps to 1. To see this, remove
    the inner part, and use that an automorphism trivial on an open subgroup of a free profinite group is trivial.
  - So it lies in ⟨ι⟩, and it is 1.
  - C_{K̂₃}(ι) = 1 by Lemma 9(b).
  - Hence Ĉ ≅ C̄ and Ĉ/⟨ι⟩ = D̂.
- **Step 3.** Matches HMM (point 2 below).
- **Steps 1, 4, 5 and 6.** Followed.
  - Step 1: ε = det Θ^{ab} ≡ 1 mod 3.
  - Step 4: a centralizer of Γ̂_{0,5} in D̂₅ is trivial.
  - Step 5: the division-quartic identity, which I verified symbolically on 22 Nov.
  - Step 6: the conjugator.

**Precision points (no error in substance):**
- **(a) Step 6, line 809:** "The centralizer of uv in Γ̂_{1,1} is ⟨uv⟩ [HR]". Herfort-Ribes treats free products, and
  Γ̂_{1,1} is an amalgam. Strongest true form: *"Modulo the central involution, uv generates the order-three factor of
  Ĉ₂ ∐ Ĉ₃, whose centralizer is that factor [HR]; its preimage in Γ̂_{1,1} is ⟨uv⟩."*
- **(b) Proposition 8:** the order of Out(C₂ ∗ Z) is derived from Fouxe-Rabinovitch's generators, not stated in [FR].
  Say "by the generators of [FR]". The Fable referee checked Out(C₂ ∗ Z) = {1, ι, t, S} on 18 Nov.

## 2. Hoshi-Minamide-Mochizuki at the source

Y. Hoshi, A. Minamide, S. Mochizuki, *Group-theoreticity of numerical invariants and distinguished subgroups of
configuration space groups*, Kodai Math. J. 45 (2022), 295-348, doi:10.2996/kmj45301. Author PDF: "Numerical invariants
and distinguished subgroups of configuration spaces", kurims.kyoto-u.ac.jp/~motizuki.

**The statement.** Corollary C, in the introduction (author PDF p. 4; details in Corollary 2.8), specializes Corollary B
to (g, r) = (0, 3). The setting:
- Σ is one prime or all primes;
- X is a hyperbolic curve over an algebraically closed field of characteristic 0;
- n ≥ 2;
- Π_n is the maximal pro-Σ quotient of the fundamental group of the n-th configuration space.

The conclusion: Out^{gF}(Π_n) is naturally the pro-Σ GT, and Out(Π_n) = GT × S_{n+3}, with S_{n+3} = Z_{Out}(GT).

**The use matches.** For (g, r) = (0, 3), Π_n is the pure group Γ̂_{0,n+3}. Step 3 needs n = 5, Σ = all primes and the
pure group Γ̂_{0,8}. These are exactly the hypotheses. Step 4 uses Z_{Out}(GT̂) = S_m for the triviality of the
permutation.

**Correction:** cite "[HMM, Corollary C (introduction) and Corollary 2.8]". The compatibility with forgetting points is
the note's (B3), not part of HMM's statement. The sentence in Step 3 already attributes it to (B3); keep it so.

## 3. The three references cited from memory

- **[A] M. P. Anderson**, *Exactness properties of profinite completion functors*, Topology 13 (1974), 229-239.
  - The bibliographic data agree with the works that cite it. I found no open copy.
  - The note cites no statement number. Its two uses are the full topology of the point-push kernels K and K₃.
  - Correction: cite the exact proposition, or cite the profinite Birman exact sequence where it is stated with a
    number.
- **[As] M. Asada**, *The faithfulness of the monodromy representations associated with certain families of algebraic
  curves*, J. Pure Appl. Algebra 159 (2001), 123-147.
  - The title, journal and volume are as I know them. I could not confirm the pages from the web.
  - The use, Γ̂_{0,n} acting faithfully on the completed fundamental group, is Asada's main theorem (genus 0 and 1).
    Cite it by its number.
- **[FR] D. I. Fouxe-Rabinovitch**, *Über die Automorphismengruppen der freien Produkte. I*, Mat. Sb. 8(50) (1940),
  265-276 (mathnet.ru sm6055).
  - Correct. Write the volume as 8(50).
  - On its use, see point (b) above.

## 4. LM7_PUSH E.65 and E.58, and Corollary 4

**Corollary 4 is correct as stated, with its hypothesis.** The unproved sentence is the claim that the run's Δ exists
on GT̂₀, is trivial on G_Q, and is nonzero.

**E.65 (LM7_PUSH checkpoint 09, `sections/E_cm_character_agent.tex`):**
- **The extension argument is correct.** It decomposes F = Hσ, uses that δ vanishes on G_Q ∩ H, proves conjugation
  invariance (E.65.16-17) through the normalizers of ⟨R₀⟩ and ⟨S⟩, and gets continuity by a compact quotient.
- **E.65's δ agrees with the note's δ on H₀.** On H₀, t = 0 forces U^{8ρ} ≡ I mod 12.
- **The Galois vanishing rests on (E.65.13):** Q(E₃[4]) = Q(i, r₀) = Q(x(E₄[3])), with r₀ = (3/4)^{1/4}.
  - I verified the second equality myself: the roots of 3x⁴ − 6x² − 1 are (√3+1)r₀/√3 and i(√3−1)r₀/√3, using
    √3 = 2r₀².
  - I did not verify the first equality, nor the E.1 sign identification of both bits with the action on r₀.

**E.58 (nonvanishing): not checked.** It constructs the element by relative pronilpotent lifting. That rests on LM7_PUSH
D.50, which no one outside the runs has checked.

**So the remark cannot be stated unconditionally yet.** The exact gap:
- Q(E₃[4]) = Q(i, r₀) and the E.1 sign identification, for the existence of Δ;
- E.58, for Δ ≠ 0 on GT̂₀.

Keep Corollary 4 as written. Mark the existence and nonvanishing of Δ as cited from LM7_PUSH E.65 and E.58, not
refereed. Or add one paragraph proving Q(E₃[4]) = Q(i, r₀) and the sign identification; that would settle the existence
part.

## 5. Is it new?

I found nothing since Lochak-Nakamura-Schneps (Feb 2026) that settles (IV) on GT̂ or GT̂ = IΓ. I searched the web,
arXiv, and hexagonmath.org by a domain-restricted search on 23 Nov.
- Minamide-Nakamura ([arXiv 1904.06749](https://arxiv.org/abs/1904.06749)) prove Out(B̂_n) ≅ GT̂ × (1 + n(n−1)Ẑ)^× for
  n ≥ 4, using HMM. That is related, but it says nothing on (IV).
- Basualdo Bonatto-Robertson ([arXiv 2606.01466](https://arxiv.org/pdf/2606.01466)) work with the Nakamura-Schneps
  subgroup and do not prove (IV) on GT̂.

The note claims no priority, rightly. It removes (IV) from the definition of the subgroup others act with.

## Verdict for posting

There is no mathematical obstacle in the parts I read. Before posting:
1. Make the citation corrections in points 1(a)-(b), 2 and 3.
2. Decide on point 4: cite E.65 and E.58 as unrefereed, or add the field-equality paragraph.

Section 7 (Lemmas 16 and 17, the HLS action on the mixed and low-genus groups) was not in my assignment. I read it only
as it enters Proposition 18.
