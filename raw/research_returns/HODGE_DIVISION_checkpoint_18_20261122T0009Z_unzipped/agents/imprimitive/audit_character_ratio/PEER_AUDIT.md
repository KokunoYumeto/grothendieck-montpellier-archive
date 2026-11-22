# Independent whole-proof audit: D-BI-18 and D-BI-18a

Reviewer: /root/imprimitive, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. Date: 2026-11-21, approximately 16:02–16:07 UTC.

**Result: PASS.** This is a whole mathematical proof review plus an independent exact finite arithmetic reconstruction. It does not reprove the published character estimate of Gluck.

## Material actually read

I read every paragraph of `agents/g34_eightfolds/bireflection/character_ratio_section.tex`, its complete `check_character_ratio.py`, its bibliography, and the full prior `essential_selfdual_section.tex` containing D-BI-09. I freshly opened the publisher's complete paper:

H. Duyan, Z. Halasi and K. Podoski, *Random bases for coprime linear groups*, J. Group Theory **23** (2020), 133–157, DOI 10.1515/jgth-2019-0043, [publisher PDF](https://www.degruyterbrill.com/document/doi/10.1515/jgth-2019-0043/pdf).

I read Definition 2.3 and the complete proof of Lemma 2.4 on printed pp.137–138, the complete Lemma 3.1 and proof on p.139, and Theorem 4.1(2), its attribution paragraph, and Remark 4.2 on p.141. The paper supplies the precise bound max{1/(sqrt(q)−1),9/q} for q>9 and attributes it to Gluck. The present audit retains that estimate as a published input. The source's finite-field surrounding application does not restrict its stated ordinary complex character bound.

## Mathematical checks

1. The actual intermediate cover and Frobenius reciprocity give the six-dimensional complex multiplicity variation, even when its coefficient field is larger than the original quadratic field. The pointed-curve dimension and Euler characteristic argument eliminates positive base genus and gives r≥12, total moving rank 2e+6. This is a necessary consequence of an actual factorization of the variation; no sufficiency or dominance is inferred from dimension.

2. For a nonscalar core element, the largest-eigenspace trace estimate is |chi(x)|≥e−2nu(x). Normality and irreducibility supply a nontrivial commutator for every nonscalar normalizing element. Its moving rank is at most twice the normalizing element's largest-eigenspace codimension. A nontrivial scalar commutator has moving rank exactly e, so it is handled correctly, rather than being assigned codimension nu=0. These facts prove nu(g)≥e(1−c)/4. For scalar multiples of core elements the stronger direct bound e(1−c)/2 applies.

3. Nonidentity scalar inertia has moving rank e and satisfies each required lower bound. Summation and integer ceilings yield the displayed inequalities. I checked every rearrangement, the strict c<1/5 endpoint, all six small-q maxima, the q≥16 and q≥29 scalar cases, and the extraspecial zero-trace argument. For the latter, the subgroup is represented faithfully because it is an actual subgroup of the matrix image.

4. For a commuting central product, irreducibility gives the tensor-product character; a tensor of invertible operators is scalar only when every factor is scalar. Hence the maximum of the individual ratio constants is valid. No normal irreducible core is assumed to exist in cases outside the theorem's hypotheses.

5. Essential self-duality has nontrivial multiplier: otherwise the finite character is real, incompatible with the inclusion of the original imaginary quadratic character field in the inducing character field. Product one and generation force at least two inertias with nontrivial multiplier. Their fixed spaces are isotropic for the nondegenerate bilinear form, so each moves at least ceil(e/2). The remaining ten entries satisfy the core estimate. This yields e(3−5c)≤12. At q≥19, c<1/2 gives e<24; D-BI-09 then removes the stated primitive nonsplit range e≥9. The final Schur-lemma argument correctly promotes a core-invariant bilinear form to a similitude form for its normalizer.

## Independent finite arithmetic

`independent_check.py` imports no author code. It intersects exact rational intervals on which a ceiling is constant, rather than using the author's loop over degrees. Its first executed run passed and wrote `independent_check.json`.

- Small-q maximal degrees: 87,45,33,21,15,15 at q=29,31,32,37,41,43.
- q≥47 necessary degrees: 3,4,9.
- Extraspecial necessary degrees: 3,4.
- Scalar-only q≥16 necessary degrees at the weakest bound: 3,4,9.
- ESD q=19 integer candidates: 4,5,6,7,14,15; the continuous upper bound is 19.

The calculation is a certificate of arithmetic only. It does not certify existence of groups, generating tuples, or dominant components at any surviving degree.
