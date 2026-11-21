# Independent whole audit of unconditional D-HES-01–03

**Result: PASS.** The complete new elementary argument removes the unverified Gluck–Magaard 1998 proper-parabolic premise. No step in the current theorem uses that premise.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed.
- Run: HODGE_DIVISION; audit recorded at **2026-11-21 18:52:19 UTC**, read directly from the clock tool. The complete proof review and symbolic run were finished before this timestamp.
- Whole proof: `agents/imprimitive/lie_small_fields/higher_even_symplectic_section.tex`.
- Frozen reviewed SHA-256: `72e295707440f2e06e39658d2b3528f61d9587227e99e6f18196b075515dbc3c`.
- The entire written proof was read. The new subgroup construction and its constants were also independently derived before the canonical text was available.

## Degree and source inputs

The degree bound uses only the Sp8(2) and Sp10(2) endpoint tables, both with explicit ATLAS provenance. The separately computed Köhler Sp12(2) table is not an essential premise of this all-rank theorem. Restriction of a faithful representation to a block Sp10(2) subgroup has a nontrivial constituent, giving degree at least155. The embedded GL_n(2) normalizer is transitive on all nonzero characters of its elementary abelian row subgroup, so faithfulness gives the second lower bound 2^(n−1)−1. These arguments apply to every nontrivial representation in the stated simple-group domain, not only to Weil representations.

The exact simple-group, multiplier and outer-automorphism statements were previously freshly read in Gluck–Magaard2006 author p25 and HHM Chapter5 Table1. Gow1981 theorem p583 and the complete invoked symplectic proof in §3 pp589–591 were freshly read in the earlier audit. The published Liebeck survey definitions and Theorem2.4(i), author pp2–4, state the unipotent3/4 bound used here. Its different nonunipotent estimate is never substituted. These readings retain their exact earlier source status; no fresh verification of Gluck's original1995 proof or GM1998 is claimed.

## New elementary parabolic construction

For an isotropic subspace R on which h acts nontrivially, the operators N_B defined by symmetric matrices are injectively parameterized: the pairing map from the natural space to R* is surjective. Isotropy gives N_B N_C=0. Symmetry and characteristic two give the symplectic identity for I+N_B, so the group is elementary abelian. The conjugation law B↦ABAᵗ is correct. Its action is nontrivial because over F2 the diagonal of vvᵗ recovers v. This construction needs no h-stable isotropic complement.

If h fixes R pointwise, averaging a dual vector f0 over its odd prime order produces an h-fixed f with pairing b(e,f)=1. The orthogonal complement W0 of this hyperbolic plane is h-stable and h acts nontrivially on it. The displayed q(v,c) operators preserve the symplectic form. Their product is q(v+w,c+d+b(v,w)). In characteristic two this law is commutative and squares to the identity. Thus the line radical really is an elementary abelian group, despite the quadratic choice of its coordinates. Conjugation is q(v,c)↦q(hv,c).

In both cases Maschke's theorem supplies the sum of all nontrivial simple F2⟨h⟩ summands. This subgroup U is nonzero and has no h-fixed points. A nontrivial odd-order action cannot occur on a one-dimensional F2 vector space, so |U|≥4. The proof is valid for arbitrary natural dimension in its stated range.

## Weight-orbit estimate

Every nonidentity element of U is an involution, hence unipotent. The verified3/4 character bound gives dim V^U≤3a/4+a/(4|U|)≤13a/16. The dual action on U* has no nontrivial fixed character. Since h has prime order p, every nontrivial orbit has length p. The h action cyclically permutes equal-dimensional weight spaces and h^p=1, so each pth-root eigenvalue occurs in exactly one pth of every orbit-sum dimension. Adding the whole U-invariant space as an upper bound gives support at least (1−1/p)(a−dim V^U)≥a/8. This is a bound on every eigenspace, not only the eigenvalue1 space.

## Elliptic case and all-element support

The primary decomposition is complete. Non-self-reciprocal primary spaces are isotropic; a nonzero1-eigenspace supplies an invariant isotropic line. Each remaining self-reciprocal polynomial has degree2d. The trace-pairing construction defines a nondegenerate Hermitian form over F_(2^(2d))/F_(2^d), with exactly the displayed sesquilinearity and conjugate-symmetry identities. If its dimension were at least two, norm surjectivity supplies an isotropic vector, and the entire field line would be an invariant isotropic subspace for the original symplectic form. Thus every such polynomial occurs with multiplicity one.

Its centralizer is consequently the product of norm-one scalar groups, of order at most3^n. Character column orthogonality and the elementary degree bounds give the strict3/4 ratio. The n=5,6 cases use155; the n=7 squared inequality is34992<35721. The explicit polynomial x²+2x−2 proves the induction for every later rank. All nonidentity powers of a prime-order element generate the same group, so the Fourier bound applies to every eigenspace and gives the stronger a/6 support in the elliptic case.

An involution has support (a−|χ(h)|)/2≥a/8. Passing to a nonidentity prime-order power decreases projective support, so the lower bound passes back to every nonidentity element. The Sp8(2) endpoint has the stronger a/5 bound. No proper-parabolic character formula, GM1998 statement or finite-to-infinite sample extrapolation remains.

## Full normalizers and geometric conclusion

The proof handles arbitrary mixed products of the permitted simple groups. Trivial outer automorphism groups make each factor-preserving intertwiner a scalar times a core operator. Tensor convolution cannot increase the maximum normalized eigenspace multiplicity beyond that of a nonscalar factor. The weighted-cycle proof gives quarter support for a genuine factor permutation, and arbitrary scalar phases do not change projective support. Nonidentity scalar inertia has full actual moving rank.

Reality of the core characters gives a unique nondegenerate invariant bilinear-form line on the full irreducible tensor representation. The full normalizer preserves that line. Its multiplier is nontrivial because otherwise all inducing-group traces would be real, contradicting inclusion of the original imaginary quadratic field. This uses field inclusion, not equality. The actual intermediate-cover factorization rules out positive genus for a rank-nine period image. In genus zero the generating product-one tuple must have at least twelve genuine branches and moving-rank sum2e+6. At least two multiplier values are nontrivial; each costs at least half the degree. The other ten cost at least e/8. Hence e≤24, contradicting e≥35. The argument does not use determinant, reflection, primitivity or tensor-indecomposability assumptions.

## Independent exact checks

`audit_higher_even_elementary.py` and `.json` were independently written and actually run, PASS in **0.041217 seconds**. They check generic symbolic line-radical matrices for W0 dimensions2,4,6, their symplectic identity, exact group law, commutativity and exponent two; generic symmetric-shear identities for R dimensions1,2,3; all averaging constants; the initial elliptic inequalities; the universal induction polynomial; and the final degree ceiling24. These finite symbolic identities support the separately reviewed universal proof and are explicitly not presented as an all-rank finite sample.

The previously saved independent complete endpoint reconstruction checks756 rows and271785 entries, but the current theorem only needs its ATLAS Sp8/Sp10 portion. No character table was newly constructed by these checks. No TeX compilation is claimed.
