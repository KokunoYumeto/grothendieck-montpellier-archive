# Alpöge's theorem pushed through Connes's programme: first pass (22 Nov 2026, ~00:5x-01:1x UTC)

By the main session (Claude Opus 5.5 at effort max), on the user's direction (22 Nov ~00:4x UTC): fixing Masullo's draft
looks less useful than "to ram the actual theorem by [Alpöge] through a [Connes] program and see what comes out" (the
user's "Lacan-Collins" is Alain Connes, with Consani). **A** = Alpöge's theorem: RH, and GRH for every Dirichlet
L-function (Lean, 20 Nov 2026). Status marks: **[std]** with source (locators from search results are marked "to verify"
where the numbering was not read in the paper itself), **[ours]**, **[reading]**, **[next]**.

## 1. What A is, in Connes's terms

1. **A is Weil positivity on the whole idele class group of Q** [std]. C_Q = Ẑ^× × R₊^*, so every Grössencharacter of
   Q is a Dirichlet character times |·|^{it}, and its L-function is a shifted Dirichlet L-function. Weil's criterion
   (Weil 1952) makes RH for this whole family equivalent to the positivity of Weil's quadratic form on C_Q. A gives it.
2. **A gives Connes's global trace formula for Q, in the form he states it** [std, checked in the LaTeX source 22 Nov
   ~01:3x UTC: Connes, Selecta Math. 5 (1999) 29-106, arXiv math/9811068]. Precisely: his **Theorem 5 (§VIII) is stated
   and proved for global fields of positive characteristic**: for h ∈ S(C_k) of compact support, the cut-off trace
   formula Trace(Q_Λ U(h)) = 2h(1) log'Λ + Σ_v ∫' h(u^{-1})/|1 − u| d*u + o(1) holds iff all L-functions with
   Grössencharakter on k satisfy RH (the proof of "formula ⟹ RH" goes through positivity of the Weil distribution).
   For number fields the end of §VIII gives "the analogue of Lemma 1, Theorem 5, and Lemma 3" with the map ψ ↦ ψ ⊗ 1_R
   and even functions on R, "which suffices when we deal with the Riemann zeta function"; the introduction states the
   equivalence for all Grössencharakter L-functions. So: for k = Q and ζ, A (RH) gives the global trace formula in
   Connes's stated form; for the Dirichlet-character components of C_Q = Ẑ^× × R₊^* the same analogue, written per
   character of Ẑ^×, is what A's GRH gives [next: write the per-character analogue out]. The semilocal trace formula
   (his Theorem 4, §VII) was proved there for every finite set of places; the global one was the open conjecture of
   the programme. For Q it now holds: the zeros are the absorption spectrum on the critical line, and the resonances off
   the line that the formulation allowed do not occur.
3. **A is RH for every number field that descends to F₁ in Borger's sense** [std, abstract checked in the LaTeX source
   22 Nov ~01:3x UTC; + reading]. Borger-de Smit (Bull. LMS 2008, arXiv 0801.2352): a Λ-ring finite étale over Q with an
   integral model as a Λ-ring is contained in a product of cyclotomic fields. The Dedekind zeta of an abelian field is a product of Dirichlet L-functions, so A gives RH for all
   of them; conversely A follows from RH for all ζ_{Q(μ_n)}. In Kapranov-Smirnov's language (F_{1^n} = {0} ∪ μ_n,
   F_{1^n} ⊗ Z = Z[μ_n]): **A ⟺ RH for the whole cyclotomic tower over F₁.**
4. **The boundary of A is the boundary of F₁-descent** [reading, on ALP_MACHINE AM-H03 (proved, intake-confirmed)].
   Alpöge's analytic interface supplies the window bound only for characters whose field embeds in a cyclotomic field
   (`IsChiField`): exactly Borger's Λ_Z-descent. The first fields beyond it are non-abelian; the first case of the
   user's phase programme, the cubic Kummer field Q(ω, ∛p) with L_K(s, χ_{p,3}) = ζ_{Q(∛p)}(s)/ζ(s), lies in no
   cyclotomic and no CM field (AM-H03). Its obstruction is the reflected coupling (complex conjugation inverts the phase),
   the dichotomy of SHAPES_CHECKED_AND_INTAKE section 3, S3.

## 2. The next rung, in the same terms

5. **Relative F₁: the cubic phase is F₁-descent over Z[ω]** [std + reading]. Over a number field K, Λ-structures with
   integral models are governed by the ray class (Deligne-Ribet) monoid of K (Borger-de Smit, "Lambda actions of rings
   of integers", arXiv 1105.4662): the descendable algebras are the abelian extensions of K. The Kummer field
   Q(ω, ∛p) is cyclic of degree 3 over K = Q(ω), so it descends to "F₁ over Z[ω]", the F_{1⁶}-level. ALP_MACHINE's own
   prescription for its gate ("a replacement must use ray-class reciprocity over K") is this change of base: Alpöge's
   Λ_Z (cyclotomic) host replaced by a Λ_{Z[ω]} (ray class) host. So the phase rung is purity one F₁-level up.
6. **Connes's programme for K = Q(ω)** [std: Connes 1999 is stated for global fields; reading]. The global trace
   formula for Q(ω) is equivalent to RH for every Grössencharacter of Q(ω), of finite order (the cubic and sextic
   residue characters, the Kummer case above) and of infinite order: the Hecke characters of the elliptic curves with CM
   by Z[ω], such as x³ + y³ = 1, whose characters are Weil's cubic Jacobi sums (Weil, Trans. AMS 73 (1952)). The units
   μ₆ fix the infinity types mod 6: the hexagon is the infinity-type constraint. The Bost-Connes system of a number
   field K (Ha-Paugam 2005; Laca-Larsen-Neshveyev 2009) has symmetry group Gal(K^ab/K) and partition function ζ_K, and
   it has arithmetic models through Borger's Λ-rings (Yalkinoglu, arXiv 1105.5022, appendix by Neshveyev). So the
   next rung has a ready Connes-side home: the BC system of Q(ω) and its global trace formula. Alpöge's own description of
   his method already uses this field: the curve C/Z[ω], the sixfold cover, Gauss sums of order #μ_K = 6.

## 2b. Two precise forms of the user's "neutrality" (22 Nov ~01:4x UTC)

10. **Colour neutrality is triviality on the global units** [std; reading]. A Grössencharacter χ = Π_v χ_v of K is
    trivial on K^× ⊃ μ_K, so Π_v χ_v(ζ) = 1 for every root of unity ζ in K. For K = Q (μ_Q = μ₂) this is
    χ_∞(−1) = χ_f(−1): the parity, the archimedean sign of the ES bridge (ES_AND_THE_RIEMANN_HYPOTHESES section 2), is
    the μ₂-neutrality of Dirichlet characters. For K = Q(ω) (μ_K = μ₆), with infinity type χ_∞(z) = (z/|z|)^{−k},
    Π_{v<∞} χ_v(ζ) = ζ^{k}: the μ₆-colour of the finite part equals the infinity type mod 6. A cubic residue character
    (·/π)₃ on (O/π)^× has colour (ω/π)₃ = ω^{(Nπ−1)/3}; it is a finite-order Hecke character only when that colour is
    neutralized at 3 (conductor at 1 − ω) or at infinity (infinity type k ≡ ±2 mod 6). Over Q(ω) the phase analogue of
    the ES pairing weights |Z_{S,χ}|² by χ(ζ), ζ ∈ μ₆, and counts pairs of divisors with d ≡ ζe: for ζ of order 3 or 6
    that is R | d² + de + e² or R | d² − de + e², the hexagonal form [next: whether this is an occupancy statement of the
    user's ES work over Z[ω]].
11. **One field carries the sign, the phase and Grothendieck's Δ: Q(ζ₁₂) = Q(i, ω)** [std; reading]. Its Galois group is
    (Z/12)^× = V₄, whose three nontrivial characters χ₋₄, χ₋₃, χ₁₂ have product 1. χ₋₄ is Connes-Consani's Gaussian
    avatar of F_{1²} (2609.00299, Prop. 7.5); χ₋₃ is the phase field Q(ω); χ₁₂ = χ₋₄χ₋₃ is Grothendieck's Δ on our
    record (DELTA23 intake L1: Δ = χ₁₂∘u). The user's ES work already lives there: its hexagonal quotient uses
    Q(X, Y) = X² − XY + Y² = N_{Q(ω)/Q}(X − ηY), and JT's quartic r⁴ − r²s² + s⁴ = s⁴Φ₁₂(r/s) = N_{Q(ζ₁₂)/Q}(r − sζ₁₂)
    is the norm form of this field (common_modulus_hexagon.tex, 12 Sep; the ES receiving frame is the (3, 4, ∞)
    triangle group of the period manuscript circulated by Alpöge). Q(ζ₁₂) is cyclotomic, so its zeta function
    ζ·L(χ₋₄)·L(χ₋₃)·L(χ₁₂) is pure by A; the first non-abelian step above it is a Kummer extension such as Q(ζ₁₂, ∛p),
    which is where A ends (section 1, item 4).

## 3. What A does not give, and what it gives the geometry

7. **Not the geometry** [reading]. A's proof is automorphic (theta lifts over CM fields, a Landau window). It does not
   construct Connes-Consani's square of the arithmetic site, its intersection theory or a Hodge index theorem.
8. **The inequality the geometry has to produce** [reading]. Weil's form on C_Q is now known to be positive, so any
   candidate intersection pairing on the square that reproduces Weil's form (the explicit formula as intersection
   numbers of the scaling correspondences) is automatically positive where Weil's is: the Hodge index inequality of the
   programme holds numerically for Q. Connes-Consani's positivity for test functions supported in [2^{-1/2}, 2^{1/2}]
   (Selecta 2021, the archimedean place) is the special case of the smallest window; for a window [λ^{-1}, λ] only the
   primes p^k ≤ λ² enter, so A is an infinite family of finite (semilocal) positivity statements, one per window, each
   now true.
9. **The F_{1²} twistor line** [std + ours]. Connes-Consani's Gaussian avatar (arXiv 2609.00299, Prop. 7.5: odd primes
   split by χ₋₄) has zeta function ζ(s)L(s, χ₋₄) = ζ_{Q(i)}(s): pure by A. Our counting construction's global zetas
   Π ζ(s − j)^{a⁺} L(s − j, χ₋₄)^{a⁻} (SPLIT_ZERO section 8) are all pure: A is Weil I for the sign-twisted Tate objects
   over F_{1²}.

## 4. Next

- **[next] A Pro prompt (ALP_CONNES)**: take A as given and push it through each structure of Connes's and
  Connes-Consani's programme (the global and semilocal trace formulas, the Weil windows, ζ-cycles and spectral triples,
  the prolate operator of Connes-Consani-Moscovici, the arithmetic and scaling sites, Riemann-Roch for Spec Z, the
  absolute twistor line, the Bost-Connes systems of number fields with Borger-Yalkinoglu models): what becomes a theorem,
  what construction becomes possible, and what the Q(ω) rung (section 2) requires; with the papers' LaTeX attached.
- **[next] Verify** the theorem numbers cited from search summaries (Connes 1999 §VIII; Borger-de Smit's statements)
  against the papers before any of this is written up.

Text written by AI is dedicated to the public domain under CC0 1.0.
