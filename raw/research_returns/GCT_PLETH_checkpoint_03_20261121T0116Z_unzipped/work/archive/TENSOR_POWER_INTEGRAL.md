# A-012. Integral completion of archive cote 133, scan 028

This completes the exact-K₀ gate left in A-007. The asserted identity holds on every commutatively ringed topos `(X,A)`, with `K₀` formed from finite locally free modules of bounded rank and short-exact-sequence relations. The integral construction below specifies both the map and the exact category. It does not assert polynomial independence of the Young generators in a modular representation ring.

## Statement and conventions

Let `K_n(X)=K₀(BS_(n,X),A)`, the exact Grothendieck group of finite locally free `A`-modules with `S_n` action, and put `K_*(X)=⊕_(n≥0)K_n(X)`. Products from degrees `a,b` to `a+b` are external tensor product followed by induction from `S_a×S_b` to `S_(a+b)`. A class of `K₀(X)` acts on each `K_n(X)` by tensor product with trivial `S_n` action.

For a partition `ν=(ν_1,…,ν_l)` of `n`, define the actual Young permutation module

`ρ_ν = [A[S_n/(S_(ν_1)×⋯×S_(ν_l))]]`.

The orbit basis identifies this with the product of the degree-`ν_i` trivial classes. Let `m_ν` be the ordinary monomial symmetric function, expressed as its integral polynomial in the elementary functions. For every `ξ∈K₀(X)`,

\[
\tau^n(\xi)=\sum_{\nu\vdash n}m_\nu(\xi)\,\rho_\nu
\quad\text{in }K_n(X).
\tag{A12.1}
\]

On an effective class `[E]`, `τⁿ([E])=[E^⊗n]` with the place-permutation action. On virtual classes, `τ` is the homomorphism from addition in `K₀(X)` to the degree-completed multiplicative group `1+∏_(n>0)K_n(X)` constructed below.

## Primary integral input and its exact translation

K. Akin, D. A. Buchsbaum, J. Weyman, *Schur functors and Schur complexes*, Adv. Math. 44 (1982), 207–278, DOI 10.1016/0001-8708(82)90039-1. The original paper was downloaded from the author's current research page and inspected in full around the relevant statements. Local copies: `ABW1982.pdf`, `ABW1982.txt`.

- Theorem II.2.16, printed p.232, supplies a universal free basis of each Schur module by standard tableaux.
- Theorem III.1.4, printed pp.245–246, supplies a natural filtration of `Symⁿ(F⊗G)` by `GL(F)×GL(G)` submodules, with associated graded `⊕_(η⊢n)L_η(F)⊗L_η(G)`.

The paper uses exterior-row notation: `L_(a)=Λᵃ`. To match the partition convention of the archive and Macdonald, **define** `S_λ^int=L_(λ′)`. This is an explicit conjugation of the indexing partition. After this relabeling, its standard tableau basis has weight multiplicities `K_(λν)`, the usual Kostka integers, and the Cauchy associated graded is `⊕_(λ⊢n)S_λ^int(F)⊗S_λ^int(G)`.

Every graded factor is finite free over Z. The filtration is defined by natural exterior-diagonalization and symmetric-multiplication maps, so it is stable under change of bases and scalar extension. Exactness over Z with free successive quotients is preserved by arbitrary base change. Applied locally to free sheaves and glued by this naturality, it gives the same filtration on a commutatively ringed topos. This is the precise transfer used here.

## Three weight extractions from the same filtration

Take `W=Z^n`, with its standard diagonal torus and permutation-matrix `S_n`. Write

`C_λ=(S_λ^int(W))_(1,…,1)`.

This is a finite free Z-lattice with `S_n` action: permuting the torus weights fixes the all-ones weight. No identification of `C_λ` with an irreducible module is required. Taking a torus weight is exact over Z, since a torus comodule is a direct sum of its weight modules, by SGA 3 I Proposition 4.7.3.

**First extraction: the tensor power.** The `W`-weight `(1,…,1)` component of `Symⁿ(E⊗W)` is equivariantly isomorphic to `E^⊗n` through

`e_1⊗⋯⊗e_n ↦ (e_1⊗w_1)⋯(e_n⊗w_n)`.

Permuting the `w_i` is the place-permutation action through this map. Extracting that weight from the Cauchy filtration gives

\[
[E^{\otimes n}]=\sum_{\lambda\vdash n}[S_\lambda^{\mathrm{int}}(E)]\,[C_\lambda]
\quad\text{in }K_n(X).
\tag{A12.2}
\]

**Second extraction: the integral Young relation.** Apply (A12.2) to `E=Z^n`, now equipped with its own diagonal torus, and select the weight `ν` padded by zeroes. The tensor-word basis on the left is the set of words with each letter `j` appearing `ν_j` times. Its permutation action is the Young coset action, since the stabilizer of the ordered word is `∏_jS_(ν_j)`. On the right, the standard tableau basis gives a free weight module of rank `K_(λν)`. Therefore, already over Z,

\[
\rho_\nu=\sum_{\lambda\vdash n}K_{\lambda\nu}[C_\lambda].
\tag{A12.3}
\]

This proof uses the exact filtration; it does not infer integral equality from rational characters.

**Third extraction: the class of the integral Schur functor.** Return to `Symⁿ(E⊗W)` and take an arbitrary `W`-weight `ν`. The left side is the tensor product `⊗_jSym^(ν_j)(E)`, and the graded factors on the right have multiplicities `K_(λν)`. Hence

\[
h_\nu(E)=\sum_{\lambda\vdash n}K_{\lambda\nu}[S_\lambda^{\mathrm{int}}(E)].
\tag{A12.4}
\]

Here `[Symᵃ(E)]=h_a(E)` follows from the exterior/symmetric Koszul identity in exact K₀, including in positive characteristic. The corresponding symmetric-function identity is `h_ν=Σ_λK_(λν)s_λ`. The Kostka matrix is integral triangular with diagonal entries one, so its transpose is invertible over Z. Comparing and inverting (A12.4) gives

`[S_λ^int(E)]=s_λ(E)`.

This proves the needed Schur/λ polynomial dictionary without a character-injectivity assumption over Z or a semisimplicity assumption.

Now substitute into (A12.2) and use `s_λ=Σ_νK_(λν)m_ν`, followed by (A12.3):

`Σ_λs_λ(E)[C_λ]=Σ_νm_ν(E)Σ_λK_(λν)[C_λ]=Σ_νm_ν(E)ρ_ν`.

This proves (A12.1) on effective classes for every commutatively ringed topos in the declared exact category.

## Exact-sequence relations and virtual classes

For `0→E′→E→E″→0`, filter `E^⊗n` by the number of factors in `E′`. The associated graded degree with `a` such factors is

`Ind_(S_a×S_(n−a))^(S_n)((E′)^⊗a ⊗ (E″)^⊗(n−a))`.

The submodules and quotients are finite locally free: this is checked after a local splitting of the original sequence, and the filtration itself is natural and `S_n` stable. Thus, with the induction product,

`τ(E)=τ(E′)τ(E″)`.

Consequently `τ` descends to the exact Grothendieck group and extends to differences by inversion of a series with constant term one.

Define `Φ_n(ξ)=Σ_(ν⊢n)m_ν(ξ)ρ_ν`. The universal alphabet-splitting identity

`m_ν(x+y)=Σ_(α∪β=ν)m_α(x)m_β(y)`

and the actual induction identity `ρ_αρ_β=ρ_(α∪β)` give `Φ(ξ+η)=Φ(ξ)Φ(η)`. The alphabet identity is an integral symmetric-function identity and evaluates in the special λ-ring `K₀(X)` of SGA 6 VI Theorem 3.3. Thus `Φ` is the same kind of homomorphism as `τ`. They agree on effective classes by the preceding proof, hence on their entire group completion. This proves (A12.1) for all `ξ`.

## Consequences for the audit

The polynomial `Σ_(α_1,…,α_n)` on scan 028 is exactly `m_ν`, with `ν=(1^α_1⋯n^α_n)`, in every characteristic under the exact-K₀ convention now fixed. This is a proved current-run reformulation using the known ABW integral filtration. The page's direct-summand margin remains refuted by A-007's rank-two example; the equality established here lives in the exact Grothendieck group. The modular relation `ρ_1²=2ρ_2` in exact `R_(F_2)(S_2)` also remains valid: no independence of the `ρ_ν` was used in the proof.

The unsigned-subset counterexample A-001 and the split quadratic counterexample A-003 are unaffected. Their explicit comparison maps still determine the exact targets of the identities.
