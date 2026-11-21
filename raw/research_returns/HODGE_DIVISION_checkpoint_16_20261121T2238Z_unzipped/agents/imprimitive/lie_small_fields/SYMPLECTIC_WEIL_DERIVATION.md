# Symplectic Weil normalizers: current derivation

**Status: new author derivation, not yet independently audited or promoted to a theorem.** 2026-11-21, `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not exposed. Work is paused temporarily for the parent-requested E817 audit. No classification of all small-field Lie cores is claimed.

## Proposed main-gate consequence

Let an irreducible normal core be a central product of symplectic groups in odd characteristic, acting on tensor products of their complex Weil constituents of degrees `(q^n ± 1)/2`, `n >= 2`. The proposed universal bound is

`nu(g) >= e/5`

for every nonscalar element of the full finite linear normalizer, allowing scalar factors, field automorphisms and permutations of the quasisimple factors. If established as below, the actual intermediate-Hurwitz identity and rank-nine requirement give

`12 ceil(e/5) <= 2e+6`.

This forces `e <= 15` and, among integers at least four, leaves only `4,5,9,10,15`. The only symplectic Weil degrees with `n >= 2` among these are `4,5` from `Sp4(3)`. Every tensor product of two or more such factors has degree at least sixteen and is excluded. Thus this would reduce the entire unbounded-rank symplectic Weil subfamily to the already studied inducing dimensions four and five. No nonsplitness or inducing-field equality enters this numerical obstruction.

## Inner elements: sharper trace estimate

For the full Weil character `omega` of degree `q^n` on `Sp(2n,q)`, the standard exact formula is

`|omega(x)|^2 = q^{dim_Fq ker(x-1)}`.

The two parity constituents satisfy `chi(x) = (omega(x) ± c omega(-x))/2`, with a scalar `c` of modulus one. Write `d_+` and `d_-` for the dimensions of the natural ±1 eigenspaces. They have disjoint intersection, so their sum is at most `2n`. If one is `2n-1`, the other is zero: the algebraic multiplicity of ±1 in a symplectic matrix is even, hence that first eigenvalue already has algebraic multiplicity `2n`. Otherwise both dimensions are at most `2n-2`.

Consequently, for a noncentral element,

`q^(d_+/2) + q^(d_-/2) <= max(q^(n-1/2)+1, q^(n-1)+q) = q^(n-1/2)+1`,

where the final comparison follows from `q^(n-1) >= sqrt(q)+1` for `q>=3,n>=2`. Therefore

`|chi(x)|/chi(1) <= (q^(n-1/2)+1)/(q^n-1)`.

This removes the factor-two loss in the coarse nontransvection bound used in GT2012 Lemma3.6.

For `q>=5,n>=2`, the ratio is less than `9/16 < 3/5`: write it as `q^(-1/2)+(1+q^(-1/2))/(q^n-1)` and use `q^(-1/2)<1/2`, `q^n>=25`. For `q=3,n>=4`, its maximum is `(27 sqrt(3)+1)/80 < 239/400 < 3/5`, using `sqrt(3)<26/15`. The elementary trace/eigenspace inequality then gives `nu >= e/5`.

At `q=3,n=3`, the degrees are13 and14 and the same ratio is less than `2/3`. Thus `nu>e/6`, so integrality gives `nu>=3>=e/5`. At `q=3,n=2`, the degrees are4 and5 and the trivial nonscalar bound `nu>=1` suffices.

## Diagonal and field automorphisms

For a symplectic group in odd characteristic and rank at least two, the expected full outer structure is diagonal times field; graph exceptions occur in characteristic two and are outside this family. A precise published primary locator for this full automorphism statement still needs to be retained in the final proof, including the small `Sp4(3)` case and exceptional-cover qualifications.

The outer diagonal involution exchanges the two Weil constituents of each degree. This can be proved directly in the Schrödinger model: a transvection acts by multiplication by `psi(b x_1^2/2)`. Its full trace is `q^(n-1) G(b)`, where the nonzero quadratic Gauss sum changes sign when `b` is multiplied by a nonsquare. The parity-twisted trace is independent of `b`, since the parity operator fixes only zero. Thus each fixed-degree constituent distinguishes the two diagonal-conjugate transvection classes.

Every field automorphism preserves both Weil square classes. To see this and control its trace, write `q=p^f`, choose the additive character from `Tr_Fq/Fp(a x)`, and regard the natural `Fq` space as a `2nf`-dimensional `Fp` symplectic space with alternating form `Tr(a <x,y>)`. For Frobenius `sigma:x -> x^p`, choose `t in Fq*` with `t^2=a^p/a`, possible because `p-1` is even. Then `t sigma` preserves the trace alternating form and induces the required field automorphism on `Sp(2n,q)`. It belongs to `Sp(2nf,p)` and its full Weil representation restricts to the chosen full Weil representation of `Sp(2n,q)`. The parity summands are preserved.

For a semilinear element with nontrivial field component `sigma^k`, put `d=gcd(f,k)`. Its fixed vectors have dimension at most `2n` over `Fp^d`: a minimal linear dependence over `Fq` among fixed vectors, after applying semilinearity, proves that independence over the fixed field implies independence over `Fq`. The same bound holds after multiplying the semilinear element by minus one. Hence both full Weil traces have absolute value at most `p^(nd) <= q^(n/2)`, and each parity constituent has ratio at most

`2 q^(n/2)/(q^n-1)`.

Here a nontrivial field component forces `q>=9`, so `q^n>=81` and the ratio is at most `18/80 < 3/5`. This yields `nu>=e/5` for the field cosets as well. Schur's lemma makes every other linear intertwiner for the same automorphism a scalar multiple of this model, preserving `nu`. Since pure field automorphisms preserve the constituents and diagonal automorphisms exchange them, no diagonal-field product stabilizes a constituent.

The key published inputs still to locate with exact proof scope are the full Weil construction/absolute trace identity and the complete automorphism structure. The elementary trace estimates and semilinear fixed-space argument above are new deductions and must be independently checked before theorem status.

## Tensor products and factor permutations

For a tensor product without factor permutation, a nonscalar factor with eigenspace codimension at least one fifth of its degree gives the same fraction for the whole tensor product. For a nontrivial factor cycle, the weighted word-orbit argument already proved in D-SPOR-03 gives codimension at least one quarter of the whole degree. This is stronger than required. Transitive conjugation makes factors isomorphic and of the same degree, but equality is not needed for the factorwise argument.

## Sources actually inspected so far

- Guralnick–Tiep2012, published JEMS14, Lemmas3.5–3.6 and their complete proofs on pp627–628, plus the full classical-group discussion pp628–631. The full Weil trace construction is cited there to earlier published sources.
- Gluck–Magaard2006, *Absolute fourth moments and finiteness of linear groups*, Communications in Algebra34,3387–3407, DOI10.1080/00927870600788448; complete author text at <https://www.academia.edu/29518749/Absolute_Fourth_Moments_and_Finiteness_of_Linear_Groups>. Read the introduction/main theorem and Section2 Weil facts and proofs through Proposition2.4. The main theorem needs a small-fourth-moment hypothesis absent from our problem and is **not** used as a general normalizer bound. Section2 states the exact full Weil trace formula and diagonal exchange facts.
- Liebeck, *Character ratios for finite groups of Lie type, and applications*, author PDF <https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf>, Section2.2: the general fixed-field/high-rank estimates depend on natural support and do not by themselves give the required uniform prescribed-inertia bound. The existence-only Guralnick–Malle result is likewise not used.
