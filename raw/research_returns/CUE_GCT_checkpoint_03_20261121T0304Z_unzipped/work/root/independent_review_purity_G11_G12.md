# Independent targeted proof review: G-11 and G-12

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Review completed: 2026-11-21, 02:04 UTC. The entire written proofs in `g11_g12_fragment.tex` were read, then reread after the positive-projective-dimension and positive-degree-invariants wording repairs. This is an independent agent's mathematical proof reading and targeted rederivation of the calculations below. It is not a formal verification, an external peer review, or an independent proof of every background theorem.

## Overall result

**PASS, for the stated characteristic-zero scope and the explicit, very large degree progression.** G-11 gives strict rectangular multiplicity gaps for the specified unpadded and lightly padded cones. G-12 proves that this rectangular sector cannot extend to or beyond the stated padding boundary. The exact boundary proof uses the already checked ternary determinantal containment, not a claim about arbitrary four-row multiplicities.

## G-11: complete proof checks

1. **Common stable Fermat point.** The diagonal-plus-cycle pencil has exactly the two relevant perfect matchings. Factoring the two binary sums supplies the displayed Fermat form in both cones; the determinant cycle has sign `(-1)^(n-1)`. Under the invariant Hermitian metric, normalized pure-power monomials have diagonal average exponent `n/4` and no off-diagonal infinitesimal transition between supported monomials. The moment map is therefore zero. For `n >= 3`, all mixed monomials in the infinitesimal action are distinct, so the stabilizer Lie algebra vanishes. In characteristic zero this makes the stabilizer finite. Kempf–Ness then gives the stable point used in both cones.

2. **Padded moment-map witness and its exact range.** Writing `a=n-m`, the proposed positive weights are `(m-3a)/(4m), n/(4m), n/(4m), n/(4m)`. They sum to one and give average exponent `n/4` in each variable. Positivity is exactly `3a<m`. Support differences cannot be roots when `m>=4`, so all off-diagonal moment-map components vanish. The normalized monomial constants only change nonzero coefficients of the diagonal Fermat-type residual form; they do not affect its two-matchings representation.

3. **Direct stabilizer computation.** From `a L_0 q+x_0 D_A q=0`, reduction modulo `x_0` forces `L_0=d_0 x_0`: the residual ternary polynomial is nonzero and the polynomial ring is a domain. Then `D_Aq=-a d_0q`. Distinct mixed monomials force every off-diagonal coefficient to vanish. The `x_0^m` coefficient forces `(m+a)d_0=0`, hence `d_0=0`; the other pure powers force the other diagonal entries to vanish. This proves finite stabilizer without assuming smoothness of the padded form.

4. **Affine quotient dimension.** The stable locus is a nonempty open subset and its image is open. The fibers there are precisely the 15-dimensional `SL_4` orbits. The dimension-of-fibers formula therefore gives `dim C[X]^SL4 = dim X -15`. This step uses the stable locus; it does not identify arbitrary polynomial-invariant and rational-invariant dimensions without a hypothesis. The ambient invariant ring surjects onto the invariant coordinate rings because invariants are exact for a linearly reductive group in characteristic zero.

5. **Generator bound and conventions.** Derksen's original Example 2.1 specializes to `beta_n=6 binom(n+3,3)n^30`. The dual representation convention is harmless because the contragredient is obtained by an automorphism of `SL_4`. The number `T_n` bounds the dimension of all coefficient polynomials of positive degree at most `beta_n`, so it bounds a choice of homogeneous generators. No assertion of computational feasibility is needed.

6. **Veronese generation.** Every generator degree divides `B_0=beta_n!`. Removing pure blocks leaves residual degree `hB_0` with `0<=h<T_n`. A monomial of degree `k E_n`, with `E_n=4T_nB_0`, has `4kT_n-h` pure blocks. The residual monomial and `4T_n-h` blocks form one factor of degree `E_n`; the remaining blocks form `k-1` such factors. This applies to spanning monomials and survives quotienting. Consequently both Veronese rings are standard graded domains, with unchanged Krull dimension.

7. **Projective degree and small-dimension endpoint.** The determinant-pencil substitution gives homogeneous coordinate polynomials of degree `nE_n` and a dominant rational map onto the invariant Proj. Surjectivity of the affine quotient and dominance of the pencil map justify the target image. I also read the complete G-10 image-degree argument: generic target hyperplanes cut image points in the attained open set; the relevant pullback components are bounded by the weak iterated Bézout degree bound, allowing base components and improper intersections. It yields `deg Y <= (nE_n)^dim Y`. The revised proof explicitly avoids Chardin's positive-dimensional endpoint issue: block padding embeds `D_{4,4}` of dimension 34 into `D_{n,4}`, and the stable quotient has dimension at least 19, hence its Proj has dimension at least 18.

8. **Hilbert comparison and constants.** Chardin's bound gives the displayed upper bound after replacing `s` by `u_n-1` and the degree by `Q_n`. Linear Noether normalization of the standard graded permanent or padded invariant ring supplies the lower bound. The binomial ratio is exactly `(k+u_n)/u_n`; `k>=u_n(Q_n-1)+1` makes this strictly larger than `Q_n`. All integers in the displayed progression are positive when `n>=4`.

9. **Rectangular extraction and ambient transfer.** In fixed coefficient degree `d`, the polynomial `GL_4` irreducibles have total weight `nd`; precisely the determinant power of shape `(nd/4)^4` is trivial on `SL_4`. Its representation dimension is one, so invariant dimensions equal the corresponding multiplicities. Divisibility follows from `4|E_n`. The transfer to the original ambient variable space uses the previously checked first-four-variable highest-weight space, not restriction of the entire ambient representation to `GL_4`, which would create unrelated invariant summands.

10. **Padding ranges.** The numerical dimension hypotheses supplied by R-14/R-16 imply the strict quotient dimension gap. The examples `n=m+1, m>=8` and fixed `1<rho<sqrt(5)/2` satisfy the additional stability requirement `n<4m/3` in their stated ranges. No bound polynomial in a variable width or a practical multiplicity algorithm is asserted.

## G-12: complete proof checks

For a nonzero padding form, a `GL_4` coordinate change takes it to `x_0`. This is legitimate for the homogeneous invariant ideal and the determinant cone. Under `diag(t^3,t^-1,t^-1,t^-1)`, a monomial with residual `x_0` exponent `j` has weight `3a-m+4j`.

* If `3a>m`, every weight is positive, so the one-parameter limit is zero. Every positive-degree invariant vanishes on all projected padded forms and hence on their closure. Exactness identifies their invariant coordinate ring with `C`; its positive-degree pieces vanish. The revised wording now states this correctly.
* If `3a=m`, the limit is `x_0^a q(0,x_1,x_2,x_3)`. Ternary determinantal containment, followed by block padding and closure, puts this limit in `D_{n,4}`. Any ambient invariant vanishing on `D_{n,4}` has the same value on the original form and its limit, hence vanishes on the projected padded cone. The direction of invariant-ideal containment is correct: the determinant invariant coordinate ring surjects onto the padded invariant coordinate ring. This gives the degreewise inequality and, by the same highest-weight argument, the claimed full ambient rectangular inequality.

The proof covers the integer equality case and the elementary ternary degrees. It does not exclude general nonrectangular four-row gaps.

## Primary-source reading and exact locators

* Derksen, H. (2001). Polynomial bounds for rings of invariants. *Proceedings of the American Mathematical Society, 129*(4), 955–963. https://doi.org/10.1090/S0002-9939-00-05698-7 . Original PDF: https://bpb-us-e1.wpmucdn.com/sites.northeastern.edu/dist/7/497/files/2020/12/A.I.a.7.pdf . Read Theorem 1.1, Proposition 1.2, and Example 2.1 on printed p. 956, including the specialization calculation. I did not independently reprove the general bounds.
* Losev, I. V. (2006). *The Kempf–Ness theorem and invariant theory* [Preprint]. https://arxiv.org/pdf/math/0605756 . Read Theorem 4 on p. 1 and its complete short proof on p. 2, together with the moment-map definition. This does not constitute an independent proof of the Hilbert–Mumford background used by that proof.
* Mukai, S. (2003). *An introduction to invariants and moduli* (W. M. Oxbury, Trans.). Cambridge University Press. https://www.math.ens.psl.eu/~benoist/refs/Mukai.pdf . Independently read Theorem 5.9 on printed p. 164; Proposition 5.10 and its complete short proof on pp. 164–165; Definition 5.12 on p. 165; Proposition 5.15 and Theorem 5.16 with their local arguments on p. 166; and Corollary 5.17 on p. 167. Printed pages 164–167 correspond to zero-based PDF pages 184–187. Theorem 5.9 was checked as a background statement; its earlier separation and orbit-closure prerequisites were not wholly reread.
* Chardin, M. (1989). Une majoration de la fonction de Hilbert et ses conséquences pour l'interpolation algébrique. *Bulletin de la Société Mathématique de France, 117*(3), 305–318. https://www.numdam.org/article/BSMF_1989__117_3_305_0.pdf . Checked the unnumbered main theorem on printed p. 306, including the geometrically reduced/equidimensional and positive projective dimension hypotheses. The invariant Proj here is integral over `C`, hence meets them. I did not independently verify the entire general Hilbert-bound proof and its divided-derivative background.

## Dictionary follow-up

The EGA-II correction to Proposition 2.5.2 is now present in both `grothendieck.tex` and `sources.md`; this resolves the earlier requested locator correction. The newly added G-11/G-12 dictionary paragraphs preserve the characteristic-zero scope of moment maps and exact invariants.

One separate wording correction was requested for the P-12 dictionary paragraph: nonvanishing on a nonlinear width-three class does not, by itself, establish set-theoretic injectivity on that class, because a difference can have larger width. The exact proven statement is that the pullback annihilates no nonzero member of the specified class. Likewise the trace dual extracts transformed rows whose rational span equals the original coefficient-row span, rather than individually recovering each original multivariate coefficient row.
