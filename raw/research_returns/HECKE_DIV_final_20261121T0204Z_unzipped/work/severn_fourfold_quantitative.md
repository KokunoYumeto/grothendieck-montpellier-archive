# Explicit fourfold corollary of the quantitative split-eightfold bound

Run HECKE_DIV_20261121; /root/markman, GPT-6 Astra Pro; 2026-11-21; effort setting not exposed. This is a new derived corollary, using the SQ bound in `severn_quantitative.md` and the root's integral seed certificate. It is separate from Markman's classical fourfold theorem and does not claim that Markman's paper states a numerical cycle bound.

Let A vary in the fixed split K=Q(ω) Weil fourfold family with integral O_K-action and polarization θ_A. Let Δ_A be the product of its elementary divisors. Let F be the fixed principally polarized balanced E⁴ seed, and choose the integral Weil class β=u_F from `integral_seeds.json`:

    β²=6,
    β=[C⁺]−[C⁻],       degθ_F C⁺≤80, degθ_F C⁻≤80.

The product A×F, with product K-action and polarization θ_A+θ_F, is a split K-eightfold with polarization elementary-divisor product Δ_A. Both factor Hermitian forms have a half-dimensional rational isotropic subspace, so their direct sum does too. All integral K-actions remain integral.

Let t be a nonzero rational flat Weil section on the fourfold family. Choose a positive integer q with qt integral and put T=(qt)², a positive integer. Let P₈ be the rational projector onto the eightfold Weil plane computed in the root's P1 and independently in SQ8, and let δ denote its checked integral denominator. Set

    t₈=(1/3)P₈(t external-product β).

Write t=t_σ+t_σbar and β=β_σ+β_σbar in their two complex determinant eigenlines. On H⁸(A×F), P₈ keeps the two extreme products, so

    P₈(t external-product β)
      =t_σ external-product β_σ + t_σbar external-product β_σbar.

The self-products of β_σ and β_σbar vanish by exterior degree, while ∫_F β_σβ_σbar=β²/2=3. Therefore contraction with β gives exactly t:

    pr_(A),*(t₈ cup pr_F*β)=t.

The same calculation gives t₈²=t²/3. In particular

    q₈=3δq,
    q₈t₈=δP₈((qt) external-product β) is integral,
    T₈=(q₈t₈)²=3δ²T.

These sections are flat. After the finite cover trivializing the Weil local system, a fibre value of t₈ extends to a flat section of the full eightfold family; its restriction to the product family is the indicated section. The universal SQ bound therefore applies with Δ=Δ_A, q_t=q₈, T=T₈.

Let D₈(Δ_A) be the explicit effective-seed degree from SQ1 and M its checked integral-projector degree multiplier. Put B=M D₈(Δ_A). The bound from SQ9 is

    C₈=B⁴(3δq+12δ²T+4).

Thus on every product A×F one has an integer N≤C₈ and integral effective four-cycles Z⁺,Z⁻ of degrees at most C₈ satisfying

    N t₈=[Z⁺]−[Z⁻].

Intersect with pr_F*C⁺ and pr_F*C⁻, and push to A. The proper intersections can be achieved by translating the cycles C⁺ and C⁻ inside F, which changes neither their cohomology nor their degree. Generic translates are proper: for every irreducible component of Z, the incidence condition z_F∈C+a has the expected dimension because translations act transitively on F. Successive components and their finite collection can be handled simultaneously.

Here is a uniform degree bound for the resulting effective two-cycles. If C is an effective two-cycle on the principal fourfold F, translation averaging represents its class by a constant strongly positive (2,2)-form α_C. With the invariant Kähler form ω_F, volume1, one has the pointwise positive-form inequality

    0≤α_C≤(degθ_F C/4) ω_F².

Indeed, its trace against ω_F²/2! is deg(C)/2!, and every unit rank-one positive (2,2)-form is bounded by ω_F²/2!. For an effective four-cycle Z on A×F this implies

    degθ_A pr_(A),*(Z · pr_F*C)
      =∫_Z ω_A² α_C
      ≤(deg C/4)∫_Z ω_A²ω_F²
      ≤(deg C/24) deg_(θ_A+θ_F)Z
      ≤(deg C)deg_(θ_A+θ_F)Z.

The last deliberately loose bound is sufficient and independent of any choice of translate. A component whose projection to A has smaller dimension pushes to zero.

The positive part of the final signed representative is the sum of the pushforwards of Z⁺·C⁺ and Z⁻·C⁻, and the negative part uses Z⁺·C⁻ and Z⁻·C⁺. Each has degree at most160C₈. Since contraction with β sends t₈ to t, this proves

    Nt=[Y⁺]−[Y⁻],       N≤C₈,       degθ_A Y⁺,degθ_A Y⁻≤160C₈.

A single explicit bounded-complexity constant is therefore

    C₄=160 [M D₈(Δ_A)]⁴ (3δq+12δ²T+4).

For t=0 the zero cycle suffices. The statement covers the fixed **split** integral K-fourfold family. The extension to arbitrary fourfold Hodge classes remains Markman's qualitative theorem; this corollary does not assert a numerical bound for them.

Check events: independently recomputed the two complex-eigenline contractions, integrality of q₈t₈, and T₈; independently proved the positive-current intersection bound and generic-translation properness. Full proof read sequentially after writing. A second reader is requested. The root's β seed is a separate exact integral cycle certificate.
