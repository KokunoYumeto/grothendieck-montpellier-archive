# A-022. The hyperbolic Stiefel–Whitney formula

Write `α∈H¹_et(X,Z/2)` for the Kummer class of `−1`, and let `c̄_j` denote the mod2 étale Chern class. For a rank-r vector bundle `E`, the formula appearing in the supplied study is

`w_t(H(E)) = Σ_{j=0}^r (1+αt)^(r−j) c̄_j(E)t^(2j)`.

The displayed hyperbolic formula holds for every scheme over `Z[1/2]`, by the explicit splitting morphisms proved below. The exact primary locator for the formula is Esnault–Kahn–Viehweg, *Coverings with odd ramification and Stiefel–Whitney classes*, Journal für die reine und angewandte Mathematik441 (1993), Proposition5.5, pp183–184. The actual author-hosted scan is https://page.mi.fu-berlin.de/esnault/preprints/helene/29-es_ka_vi.pdf . Section5.1, p179, starts with a scheme over `Z[1/2]`; section5.4, p182, introduces a regularity assumption. Thus the source directly establishes the displayed formula for regular schemes over `Z[1/2]`. Its result also covers metabolic bundles with the Chern classes of a Lagrangian. The proof here establishes the stated hyperbolic formula over arbitrary `Z[1/2]`-schemes. No characteristic-two version is claimed.

Both pages of the proposition and proof were visually read. The proof first computes the rank-two case using the complement of the isotropic quadric, then constructs an affine-bundle pullback splitting off a metabolic rank-two summand. The remaining Lagrangian fits in a vector-bundle exact sequence, and the Chern-class Whitney formula gives the displayed sum by induction. The injective étale-cohomology pullback descends the identity. Zibrowius, *Witt groups of curves and surfaces*, §1.4, equations(6)–(8), printedp8 (PDFpage9) in the author PDF, reproduces the formula and its first two components with this exact EKV locator. That exposition explicitly treats schemes over `Z[1/2]`; the regularity inherited from EKV§5.4 is recorded here rather than silently attributed away.

In particular,

`w₁(H(E))=rα`,

`w₂(H(E))=binom(r,2)α²+c̄₁(E)`.

For a line bundle `L`, the latter reduces to `w₂(H(L))=c̄₁(L)`. This line-bundle identity admits the following direct proof over every scheme over `Z[1/2]`, without the regularity assumption just identified in the source.

## The explicit line-bundle calculation

Let `p:U→X` be the open complement of the isotropic quadric in the projective bundle of lines in `H(L)=L⊕L∨`. Its tautological line `M` is nondegenerate. The first projection `M→p*L` is an isomorphism: at every geometric point the quadratic value of a tautological vector `(v,f)` is `f(v)≠0`, so both components are nonzero. A fibrewise nonzero map of line bundles is invertible. Orthogonal projection gives the actual decomposition

`p*H(L)=M ⊥ M^⊥`.

Set `x=w₁(M)`. The determinant form of `H(L)` has value `−1` in its canonical determinant trivialization; hence `w₁(M^⊥)=α+x`. The Whitney formula now gives

`p*w₂(H(L))=x(α+x)`.

For any symmetric line bundle with class `x∈H¹_et(U,Z/2)`, its ordinary first Chern class satisfies

`c̄₁(M)=x²+αx`.

This is Lemma5.3 of EKV, pp181–182, whose cocycle calculation uses only that2 is invertible. One can see the formula directly by writing transition signs as `(-1)^(a_ij)`, choosing local square roots of `−1`, and lifting these signs to fourth roots of unity. The Kummer coboundary has the two mod2 summands `a_ij a_jk` and `α_ij a_jk`, respectively the square and the cup product. Therefore

`p*w₂(H(L))=c̄₁(M)=p*c̄₁(L)`.

The pullback `p*:H*_et(X,Z/2)→H*_et(U,Z/2)` is injective by the orthogonal splitting principle, Zibrowius, *The gamma-filtration on the Witt ring of a scheme*, Proposition3.3, author version arXiv:1411.3198v2, pp19–20. Its proposition explicitly assumes a scheme over `Z[1/2]`, which is exactly the present scope. Injectivity gives the asserted equality on `X`.

## A direct splitting morphism for an arbitrary vector bundle

The same nonisotropic-line construction supplies the full higher-rank formula without an additional affine-bundle invariance theorem. Let `E` have rank `r>0` and form

`p:U=P_nd(H(E))→X`.

Let `M⊂p*E⊕p*E∨` be the tautological nondegenerate line. Its two projections give maps

`a:M→p*E`,

`b:p*E→M∨`.

The composite `β=b∘a:M→M∨` is an isomorphism: in a local generator `(v,f)` of `M`, it is multiplication by the invertible value `f(v)`. The nondegeneracy of the restricted hyperbolic symmetric form says that `2f(v)` is a unit; here2 is invertible. Therefore

`e=a∘β^(−1)∘b : p*E→p*E`

is an actual idempotent, since `e²=aβ^(−1)(ba)β^(−1)b=e`. It exhibits

`p*E=a(M) ⊕ ker(b)`.

Both summands are vector bundles, of ranks1 and `r−1`. In local coordinates the projector is `z↦v f(z)/f(v)`. Replacing `(v,f)` by `t(v,f)` leaves this projector unchanged, which also verifies the global gluing directly. The line `a(M)` is isomorphic to `M` through `a`.

Zibrowius Proposition3.3 and its first-step proof show that this particular `p` induces an injection on mod2 étale cohomology. Repeat the construction on `ker(b)`, reducing its rank by one at each step. After finitely many steps there is a composite morphism `q:Y→X` with injective pullback on mod2 étale cohomology and an actual direct-sum decomposition

`q*E=L₁⊕⋯⊕L_r`.

The direct-sum projections and their dual inclusions give the orthogonal isomorphism

`q*H(E) ≅ H(L₁) ⊥ ⋯ ⊥ H(L_r)`.

By the already proved line-bundle result and the Whitney identities,

`q*w_t(H(E))=∏_{i=1}^r(1+αt+c̄₁(L_i)t²)`.

Expanding by the set of indices that contribute their Chern term gives

`∏_{i=1}^r(1+αt+c̄₁(L_i)t²)=Σ_{j=0}^r(1+αt)^(r−j)c̄_j(q*E)t^(2j)`.

Naturality and the injectivity of `q*` descend this equality to `X`. Rank zero is the identity `1=1`, and a locally constant rank is treated on its open-and-closed rank pieces. This proves the full hyperbolic formula over every scheme over `Z[1/2]` through explicitly constructed bundle maps.

## What this resolves in the archive

Original Montpellier PDFpage4 was visually inspected and does contain the `c₁ ?` question. The study's proposed answer for `w₂(H(L))` and its full hyperbolic formula are correct over every scheme over `Z[1/2]`, as just proved. The arbitrary-ringed-topos question about an augmented completed lambda-ring target, recorded separately as A-Q080, still requires its multiplication and operations to be specified; these characteristic-class identities do not supply that missing target definition.

The printed rank-two proof on EKVp183 includes a sentence asserting an isomorphism on the unmodified Picard groups. That assertion is unnecessary for the direct argument above. For example, the complement for `H(L)` is the nonzero total space of a square of `L`, and the pullback kills `2[L]`; consequently an integral Picard-group isomorphism cannot be used in that generality. The independently verified argument uses the stated injective mod2 cohomology pullback and the actual line isomorphism instead.
