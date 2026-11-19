# Finite graph constraints for the conditional C6 approach

AI-produced by GPT-6 Astra, root, current run, 19 November 2026. This is a proved linear-algebra lemma and an attempted application. It does not assert the missing geometric realization.

## The graph-rank lemma

Let all vector spaces be finite dimensional over a field F. Put E=U⊕W⊕V, where W collects any finite list of internal variables. Let R:E→C be a linear map. Suppose that projection of ker(R) to U⊕V has image exactly the graph of a linear map f:U→V. Internal variables need not be unique. Write π:E→V for the last projection. Then

\[
\operatorname{rank}f=\operatorname{rank}(R,\pi)-\operatorname{rank}R,
\]

where (R,π):E→C⊕V is the map with those two components.

Indeed π(ker R)=im f by the graph assumption. Rank-nullity applied to the restriction π|ker R gives

\[
\dim\pi(\ker R)
=\dim\ker R-\dim(\ker R\cap\ker\pi)
=\operatorname{rank}(R,\pi)-\operatorname{rank}R.
\]

The formula does not require R to be surjective and remains valid if U, V or any internal vertex is zero.

## Why finite inverse expressions have such graphs

A finite expression formed from given linear maps by composition, addition, rational scalar multiplication, direct sum and inversion of a map known to be an isomorphism can be expressed by finitely many linear constraints. Introduce one internal variable for each intermediate value. For an elementary map a, impose y−a x=0; for addition impose y−x1−x2=0; and for an inverse b^−1 impose b y−x=0. The invertibility assumption makes the latter equivalent to y=b^−1 x. Induction through the finite expression shows that the output is the prescribed f(u) for every input u. One may include redundant internal variables without affecting the graph-rank formula.

For example, with g:Z→A invertible, f:U→A, h:Z→V and k:U→V, the expression h g^−1 f+k is encoded by

\[
R(u,z,v)=(gz-fu,\;v-hz-ku).
\]

Its rank is therefore determined by the ranks of R and (R,π), whose entries use only f,g,h,k and identities; the inverse never occurs in a block matrix.

## Passage through cohomology

Suppose the elementary maps arise from common maps of finite complexes and that every finite block matrix of these chain maps has rank on cohomology determined independently of a coefficient realization. Apply the graph construction to the induced cohomology maps. Both R and (R,π) are again induced by finite block chain maps, so the graph-rank formula proves the same independence for every well-defined finite inverse expression.

For completeness, if a:C•→D• is a chain map, its rank on H^t is

\[
\operatorname{rank}H^t(a)
=\operatorname{rank}
\begin{pmatrix}d_C^t&0\\a^t&d_D^{t-1}\end{pmatrix}
-\operatorname{rank}d_C^t-\operatorname{rank}d_D^{t-1}.
\]

Projection of the displayed image to C^(t+1) has image im d_C^t and kernel a^t(ker d_C^t)+im d_D^(t−1). The image on cohomology is the quotient of that kernel by im d_D^(t−1). This proves the formula. No chain-level inverse or projector onto a cohomology group is constructed or needed.

## Proposed application and unresolved obligation

The finite-field correspondence-rank conjecture in van Dobben de Bruyn (2020, Theorem5.1 and Corollary5.2, pp17–18) controls block matrices of rational algebraic maps on weight-spectral-sequence strata. Takeshi Saito (2003, section2.4, author pp33–36) supplies common E1 maps for algebraic correspondences. The already-audited C6 proof uses these facts for a homogeneous algebraic projector.

A possible extension is to a motivated projector presented by algebraic operations and Hard-Lefschetz inverses. The graph lemma eliminates the inverse operation at the level of linear algebra. The remaining geometric obligation is to exhibit all operations, including tensor factors, cohomological degree selection, and semilinear inertia actions, in finite common diagrams of weight spectral sequences with the required algebraic E1 maps. It would be invalid to assume generic Künneth projectors algebraic, or merely to assert an algebraic E1 action for an arbitrary motivated correspondence. That obligation is being investigated separately.

For elementary normalized vertices H^(i+2r)(Z)(r), the weight-b part occurs in cohomological row-degree i−b of the row E1^(a,b+2r)(r). Thus different twists can be aligned without changing that row-degree. Tensor constructions and Lefschetz star on fixed algebraic classes still need an explicit account.

## Exact checks

The program code/check_rank_diagrams.py verifies the two identities over Q using exact SymPy arithmetic on 48 chain-map cases after nontrivial changes of basis and 48 finite inverse-expression graphs. It also adds unconstrained internal variables to test that uniqueness is unnecessary. Dimensions include zero and maps include rank-deficient cases. The retained JSON gives every input dimension, resulting rank, random seed, library version and runtime. These are finite consistency checks of the proved linear-algebra identities, not tests of the geometric obligation or the conjecture.

## References and opening status

Saito, T. (2003). Weight spectral sequences and independence of ℓ. *Journal of the Institute of Mathematics of Jussieu, 2*(4), 583–634. https://doi.org/10.1017/S1474748003000173. Opened: author PDF, complete section2.4, pp33–36, with the full proofs of Lemmas2.4.1–2.4.2, Corollary2.4.3 and Proposition2.4.4. Author URL: https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2.pdf.

van Dobben de Bruyn, R. (2020). The equivalence of several conjectures on independence of ℓ. *Épijournal de Géométrie Algébrique, 4*, Article16. https://doi.org/10.46298/epiga.2020.volume4.5570. Opened: published PDF, complete Theorem5.1 proof and Corollary5.2, pp17–18. Primary PDF: https://epiga.episciences.org/6931/pdf.
