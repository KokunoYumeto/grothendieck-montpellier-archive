# The bigonal Galois-closure attempt: an exact conditional obstruction

Status: proved conditional calculation, with the geometric rational-spanning hypothesis retained. This is a method limit, not a decision of C.4 and not a qualifying change of its main gate. No priority claim is made.

## 1. Precisely opened primary input

Recillas, S., and Rodríguez, R. E. (2003), *Prym varieties and fourfold covers*, arXiv:math/0303155v1, §7.1, printed pp. 35–37, gives the bigonal construction for a ramified double cover of a hyperelliptic curve satisfying (7.25). In the case of four branch points over an elliptic curve, the two Pryms are dual polarized surfaces of type (1,2). Their natural norm–pullback maps are the polarization and its dual, and their composite is multiplication by two. The pullbacks from the two genus-three curves to the Galois closure are embeddings. The relevant injectivity criterion is Proposition 2.1, p. 4; polarization pullback is Theorem 2.5, pp. 5–7.

Primary URL: https://arxiv.org/pdf/math/0303155 . Local PDF and extracted text are `sources/recillas_rodriguez2003_fourfold.pdf` and `.txt`. Actual download runtime and SHA-256 are in `output/fetch_bigonal_source.json`. We have not asserted that the entire 78-page preprint was read. The bibliography on p. 77 identifies Pantazis's original paper, but we have not opened that original paper in this check.

## 2. An abstract integral lemma

Let A be a complex abelian surface with End(A)=Z and NS(A)=Zℓ, where ℓ is a primitive polarization of type (1,2). Put B=Â and denote the polarization homomorphisms by λ:A→B and η:B→A, normalized by ηλ=2 and λη=2. Let (J,θ) be a principally polarized abelian variety, and let

\[
i:A\hookrightarrow J,\qquad j:B\hookrightarrow J
\]

be embeddings. Write i†=îθ:J→B and j†=ĵθ:J→A. Suppose

\[
i^\dagger i=2\lambda,\quad j^\dagger j=2\eta,
\quad j^\dagger i=2\operatorname{id}_A,
\quad i^\dagger j=2\operatorname{id}_B,
\]

and suppose, separately, that

\[
\operatorname{Hom}(A,J)_{\mathbb Q}
=\mathbb Q i+\mathbb Q(j\lambda).
\tag{BG}
\]

Then every composite A→J→A is an even multiple of the identity, and the ideal of such scalars, after localization at two, is exactly 2Z_(2).

### Proof of the saturation step

We first show that i and jλ generate Hom(A,J) over Z_(2). If this were false, clear odd denominators in a missing element and obtain an actual homomorphism

\[
f=\frac{a i+b j\lambda}{2^e},\qquad e\geq1,
\]

where a and b are integers not both even. The pullback of θ has polarization class

\[
f^\dagger f
=\frac{2a^2+4ab+4b^2}{2^{2e}}\lambda.
\tag{BG.1}
\]

The coefficient is integral, since ℓ generates NS(A). If a is odd, the numerator in (BG.1) has two-adic valuation one, which is impossible. If a is even and b odd, its valuation is exactly two; hence e=1. Subtracting (a/2)i and using that b is odd would then make jλ divisible by two in Hom(A,J).

This last divisibility is impossible for an actual embedding j. Indeed, if 2g=jλ, surjectivity of [2] on A gives im(g)=im(2g)=j(B). Thus g factors through j, and λ is divisible by two in Hom(A,B), contrary to the primitivity of ℓ. This proves the asserted saturation.

Duality and the isogeny λ show that Hom(B,J)_Q is spanned by j and iη. The same argument, with A and B interchanged, gives

\[
\operatorname{Hom}(B,J)_{\mathbb Z_{(2)}}
=\mathbb Z_{(2)}j+\mathbb Z_{(2)}(i\eta).
\]

Taking θ-adjoints therefore gives

\[
\operatorname{Hom}(J,A)_{\mathbb Z_{(2)}}
=\mathbb Z_{(2)}j^\dagger+
\mathbb Z_{(2)}(\eta i^\dagger).
\]

For u=a i+bjλ and v=cj†+dηi†, direct composition gives

\[
vu=(2ac+4ad+4bc+4bd)\operatorname{id}_A.
\]

Every scalar is even, and j†i=2 realizes two. Since an integer belonging to 2Z_(2) is even, the same parity statement holds integrally. This proves the lemma.

## 3. Application and unverified extra hypothesis

For the bigonal Galois closure, take i and j to be the Prym embeddings followed by the two ramified pullbacks to its Jacobian. The primary norm–pullback identities yield all four displayed pairing identities: for example j†i is η composed with the bigonal map λ, hence [2]. In the elliptic/four-branch-point case the Galois closure has genus nine by Riemann–Hurwitz.

The extra hypothesis (BG) is equivalent here to saying that the remaining rational isotypic factors contribute no further copy isogenous to A. We have **not** proved that condition for every cover, or for a specified geometric generic cover, in this note. Under that condition the entire integral Hom construction fails, including maps other than the displayed norm and pullback. Without (BG), the calculation only excludes the span of the displayed maps. Neither statement excludes other Jacobians or the other étale covers of the original genus-three curve.

## 4. Independent check

The frobenius agent independently checked the saturation proof from the displayed hypotheses and supplied the image-factorization justification above. That check expressly did not include a fresh read of Recillas–Rodríguez or a proof of (BG). It is not recorded as a new numbered result or a main-gate closure.
