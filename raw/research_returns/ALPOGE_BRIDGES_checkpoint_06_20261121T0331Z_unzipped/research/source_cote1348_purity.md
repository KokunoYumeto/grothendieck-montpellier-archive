# Cote 134-8: removing the ordinary injective-dimension hypothesis in two substantial ranges

Run: /root/source_and_masullo within ALPOGE_BRIDGES. Model: GPT-6 Astra Pro. Effort: not exposed. Date: 21 November 2026 UTC.

The complete statements and proofs are **F-SM-24 and F-SM-25** in source_cote1348_purity.tex. The target remains the connective derived category. The adjunction is precisely the B-resolution construction of BR-13405; no other model or derived adjunction is substituted.

## Positive result

The ordinary finite-injective-dimension assumption in BR-13404 can be replaced by either of two conditions:

1. Scalar projective modules have uniformly finite **pure-injective** dimension. This includes every countable scalar ring, and every scalar ring of cardinality aleph_t with finite t, by the known Gruson–Jensen/Kiełpiński–Simson cardinality theorem.
2. The scalar modules R(x,y) are **finitely generated projective**. Under this condition, the conclusion holds over every commutative scalar ring, without any dimension or cardinality hypothesis on that ring.

The proof retains the exact unit normalization and the interval's vanishing in degree zero and all higher degrees. It also states scalar tensor compatibility explicitly: the interval transformation on X tensor_k U is the scalar tensor of the transformation on X. This follows from a cocontinuous k-linear tensor product; it is not silently inferred for an unspecified tensor operation.

## The actual right adjoint determines the proof

Let B resolve the left ringoid module D, with B_n a coproduct of left representables. Every acyclic projective chain object has the locally finite disk decomposition

\[
P=\bigoplus_{n\ge0}D^{n+1}(Q_n)=\prod_{n\ge0}D^{n+1}(Q_n).
\]

Because the right adjoint preserves products, its image is exactly

\[
GP=\prod_{n\ge0}\operatorname{Hom}_k(B_n(-),Q_n)
  =\prod_{n\ge0}\prod_{a\in A_n} C_{x_a}(Q_n),
\qquad C_x(Q)(y)=\operatorname{Hom}_k(R(x,y),Q).
\]

This calculation is the reason to use relative pure injectivity. It assumes no preservation of coproducts by G.

The interval monomorphism is objectwise pure: tensoring its evaluation with any scalar U is another instance of the given interval monomorphism. If E is scalar pure injective, C_x(E) is injective with respect to such monomorphisms, by the evaluation/coinduction adjunction. Every product of these modules therefore splits its interval inclusion and is Lφ-acyclic.

For the first sufficient condition, resolve all the projective coefficients Q_n by pure injectives in a uniformly finite number of steps, apply coinduction, and take products. Coinduction is exact because R(x,y) is scalar projective. Products are exact in the module category. The result is a finite resolution of the actual GP by interval-acyclic modules.

For the second condition, use the pure embedding Q_n → Q_n^{++} into its character double dual. Local finite generation makes evaluation carry finitely presented ringoid modules to finitely presented scalar modules. The coinduced embeddings consequently become pure in the ringoid module category, and so does their product. The proof establishes directly that every Tor^R_j(D,−) preserves pure short exact sequences, by splitting the character-dual sequence and applying Ext. Thus GP is a pure submodule of an Lφ-acyclic product and is itself acyclic.

These conclusions discharge precisely BR-13403's counit test. They therefore establish the claimed equivalence for the specified adjunction.

## Primary source for the cardinality consequence

Chachólski, W., Neeman, A., Pitsch, W., & Scherer, J. (2018). Relative homological algebra via truncations. *Documenta Mathematica, 23*, 895–937. [Primary journal PDF](https://ems.press/content/serial-article-files/26419?nt=1).

**§9.2 and Theorem 9.2, p.926**, explicitly state the bound on pure global dimension and formulate its meaning using finite pure-injective dimensions. The article attributes the result to Kiełpiński–Simson (1975) and Gruson–Jensen (1973). This exact primary research statement was read directly; their original proofs were not reconstructed. genui{"citation":{"ref":"turn604814728view0"}}

For a finite scalar ring, the note applies the countably infinite case to k × Z and takes the first idempotent component. Purity and pure injectivity are componentwise for a product ring, so the same bound follows. Thus “countable” includes finite rings.

## A complete counterexample to one attempted extension

F-SM-25 proves that coinduction need not preserve scalar pure exactness under mere scalar projectivity of the ringoid hom modules. It uses k = Z, R = Z[t], and the pure sequence

\[
0\to\mathbb Z\to\widehat{\mathbb Z}\to\widehat{\mathbb Z}/\mathbb Z\to0.
\]

The finitely presented R-module R/(2t−1) has underlying scalar module Z[1/2]. An explicit map from Z[1/2] to the quotient is constructed by compatible residues of a nonintegral 2-adic number. It cannot lift to the profinite integers, because a lift's value at 1 would have zero 2-adic component. The evaluation/coinduction adjunction then proves that the coinduced short exact sequence is not pure over R.

This is a counterexample to the proposed preservation-of-purity inference. It is **not** a counterexample to Grothendieck's interval theorem: no interval satisfying the original vanishing is claimed for this one-object ringoid. Indeed its scalar ring Z already falls within the proved range.

## Exact unresolved remainder

For scalar rings without an available finite pure-injective-dimension bound and ringoids whose scalar hom modules are merely projective, the remaining condition is

\[
\operatorname{Tor}^R_j\!\left(D,
  \prod_{n\ge0}\prod_{a\in A_n}C_{x_a}(Q_n)\right)=0
\quad(j\ge0)
\]

for the actual resolution B and every sequence of projective Q_n. The pure-injective products on the containing side are known to be acyclic; the uncontrolled passage is back to these coinduced projective coefficients.

An infinite injective or pure-injective resolution does not immediately fix this: it introduces an infinite totalization or convergence requirement absent from the finite proof. No such limit interchange has been asserted. No counterexample satisfying all the original interval and normalization assumptions was obtained.

## Checking status

The drafter completely reread both proofs at **2026-11-21 00:52:28 UTC** and found no gap. The self-check covers the character-dual construction, the Tor argument, relative interval splitting, the exact product formula for G, both sufficient conditions, the finite-ring reduction, and every step of the explicit 2-adic nonlift. The record is a whole-proof self-reading, not an independent reproof of the cardinality theorem or a formal kernel check. Root has been asked to perform an independent complete reading.
