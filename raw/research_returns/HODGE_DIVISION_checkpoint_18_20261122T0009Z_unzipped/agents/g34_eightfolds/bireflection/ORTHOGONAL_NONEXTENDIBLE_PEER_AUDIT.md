# D-OL-09--11: independent whole-proof/source/code audit

**PASS on the complete frozen proof**, with a separate independent exact
supplement. No mathematical repair was found or requested.

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort
inherited/unexposed, HODGE_DIVISION. Actual independent supplement
completion: 2026-11-21 21:41:46.951351 UTC; final review record is
timestamped in CHECK_EVENTS.tsv.

Reviewed `agents/imprimitive/orthogonal_lowlevels/orthogonal_nonextendible_section.tex`,
SHA-256 `5f7e898c37be40cb4a17cd8ccbfdce9fa48b90d3c3beb40d0637fed620ae5bd4`.
I read the entire proof, the entire author program
`check_orthogonal_nonextendible.py`, its complete output, and the exact
generation/normalizer/descent interfaces in the previously reviewed
OL06--08 proof. This is not an audit of genuinely spin characters: the
representations here are ordinary representations of the natural Omega
groups, as explicitly stated by the author.

## 1. Rank-four commutators remove the extension requirement

The two opposite abelian line radicals generate the natural Omega
group, so their equal-dimensional invariant spaces intersect in zero
on a nontrivial irreducible module. Thus either radical has invariant
dimension at most half the full degree. This interface does not use
an extension of the representation to the full orthogonal group.

For a natural moving space of rank r at most four, adjoining dual
partners to its polar radical produces a nondegenerate container of
dimension at most 2r. Its perpendicular is fixed pointwise and, when
d>=22, contains a hyperbolic pair. On the complementary space of
dimension N=d-2, the fixed space has polar rank at least N-2r.
The quadratic counting error is bounded by q^(N/2), independently
of r in this range. Hence exactly the prior Gauss bound applies,
with the main term at most q^(N-3).

For q>=3, the resulting fixed-weight fraction is less than 1/8.
Prime-order nonfixed weight cycles then give support at least 7a/32.
This remains a statement about all ordinary module weight spaces;
their multiplicities are constant on the Omega-orbits because the
Levi action is present inside the group.

For a nonscalar linear compatible normalizer, at least one element of
the two radicals fails to commute with its natural implementing map.
The resulting commutator is an actual element of S, and its moving
rank is at most four. A nonidentity prime-order power remains of rank
at most four, cannot be a nonidentity scalar, and has rank at least
two by the determinant or Dickson criterion. This checks every
hypothesis of the preceding bound.

The representation identity for that commutator is exact. Subtracting
a scalar eigenvalue of maximal multiplicity from T bounds the ordinary
rank of the commutator minus identity by 2 nu(T). Taking a power cannot
increase projective support. Thus nu(T)>=7a/64. There is no appeal to
an unspecified O-extension, and no replacement of ordinary moving rank
by projective support in the wrong direction. Keeping the possible
rank-four commutator is essential.

## 2. Arbitrary field degree and semilinear descent

I rechecked the full prior natural-normalizer proof, including its
arbitrary-q outer-order comparison, centralizer calculation and lift
through a represented central quotient. Its order computation is not
restricted to the small fields of its former final application.

Taking a nonscalar power of prime order in PGL reduces the field part
to either trivial or prime order ell. In the latter case q=q0^ell.
The scalar power relation for the representation implies H^ell=cI
naturally: the possible discrepancy on S is central, perfectness kills
that central homomorphism, and the natural centralizer is scalar.
Commuting H with its power makes c belong to the fixed field.

Norm surjectivity rescales H to have ell-th power one; the norm-one
multiplier then permits rescaling the quadratic form. The explicit
fixed-vector spanning argument using independence of field
automorphisms works also when ell is the characteristic; it never
divides by ell. The descended form is nondegenerate over F_q0 and has
a hyperbolic pair in the dimensions at issue.

The fixed-weight count is bounded by q0^N, and the denominator is the
previous uniform lower orbit-size bound. I independently verified
the exponent identity
`ell-N(ell-1) = -18-(N-20)(ell-1)-19(ell-2)`.
It gives the asserted universal bound less than 1/4, for every prime
ell>=2 and every q0>=2. Field-orbit support is therefore at least
3a/16. Mixed graph-field lifts are included by the actual descent;
no compatible mixed operator is assumed separately compatible with
its diagonal or field factors.

## 3. Nonextendible even-characteristic characters

For an inner prime-order element fixing a hyperbolic pair, the fixed
space estimate remains valid for every moving rank. If the rank exceeds
N/2, the trivial error bound is already at most q^(N/2); if not, the
polar-rank argument applies. The q=2 endpoint is strictly below 5/16,
giving support at least 11a/64. The stronger, false 1/4 endpoint is
expressly not used.

If no hyperbolic pair is fixed, an odd-prime-order element has a
nondegenerate fixed quadratic space of dimension at most two. For an
involution, the fixed polar rank is at least d-2r. Polar rank at least
four would provide a nondegenerate quadratic four-space and hence a
hyperbolic pair. Therefore r>=d/2-1. These give restricted natural
support at least 567 when d>=1136.

The published LST estimate is correctly applied to an irreducible
character inflated to the simply connected finite cover, with the
same natural orthogonal action. It does not require faithfulness.
In characteristic two the permitted scalar set mu2 is {1}; thus the
rank estimate is exactly the support in the published remark.
The resulting proportional support exceeds 11/64.

In even characteristic O/S has order two and has an involution
representative. An invariant irreducible S-module extends to O after
rescaling the intertwiner to square one. Thus nonextendibility is
equivalent to absence of a compatible operator in that outer coset.
Every linear similitude is a scalar times an isometry, so all compatible
linear normalizers in the nonextendible case are scalar times inner.
The previous arbitrary-field descent handles the other normalizers.
This completes the full-normalizer bound without an extension or
selfduality premise.

## 4. Actual source consequences and scope

The selfdual tensor-core module has a unique invariant bilinear form
line. If the entire inducing image preserved that form without a
multiplier, its character would be real-valued, contradicting the
original imaginary quadratic character field's inclusion in the
inducing character field. Hence two inertia multipliers are nontrivial
on a genus-zero cover and each moves at least half the full space.
Together with ten support costs this gives e<=64 for OL09.

The factor degree bound from the previously checked GLT theorem
exceeds that number. It first excludes genus at least two in the actual
Euler formula; genus one has at most six genuine marks and image
dimension at most six. Thus the genus-zero step is justified before
using the twelve-mark inequality.

For the nonextendible even-characteristic factors, the stronger uniform
support gives e<=96 without a bilinear-form premise. The degree lower
bound again contradicts it. Convolution handles factorwise operators;
the quarter-support tensor-cycle bound handles factor permutations.
Nonidentity scalar inertia moves the entire space.

Transitivity preserves the property of extending to O, since all
natural semilinear lifts normalize O. In the extendible case the full
O character is real and hence the factor is selfdual. Combining the
new bounds with the earlier q=2 extendible theorem proves exactly the
stated residual dimensions d<=21 for selfdual ordinary q>=3 and
d<=1134 for all ordinary even-q transitive cores. It proves neither
existence at those dimensions nor an exclusion of nonordinary spin
modules. The larger inducing character field is retained throughout.

## 5. Primary-source boundary

I used the already completely checked OL06--08 primary interfaces,
and reread the exact passages implementing generation, norm-orbits,
natural normalizers and arbitrary cyclic descent. Their sources are
Taylor's corrected author book; Li--Xia's complete outer Table 2.1;
and the stated GLT degree theorem. The prior separate whole-source
audit is documented in ORTHOGONAL_SUPPORT_PEER_AUDIT.md.

For the new numerical input I rechecked the actual published LST
conventions p.1907, Theorem 4.3.6 and its displayed estimate
pp.1917--1918, the complete proof already read in the HOS16 review,
especially its final parameter choice pp.1922--1923, and Remark 4.3.7
p.1923. The radical is sqrt(N/7), and the spin support refinement uses
mu2. The all-q gamma convention and inflation to the perfect cover
have the claimed scope. Source: Larsen--Shalev--Tiep, Annals of
Mathematics174(2011), 1885--1950,
https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf.
Local published copy: `sources/LST2011_Waring_published.pdf`.
No upstream Gluck proof reconstruction is claimed.

## 6. Independent exact supplement

Own files: `audit_orthogonal_nonextendible.py` and
`audit_orthogonal_nonextendible.json`. First execution PASS,
0.08303845799673581 seconds, at the timestamp above. No failed attempt.
The author program was read first, but no author code or inputs are
imported by this independent reconstruction.

The program verifies the rational inequalities via monotone endpoint
polynomials, the universal field-exponent identity by exact coefficient
arithmetic, all displayed source ceilings and thresholds, and an
alternative complete finite matrix reconstruction. It enumerates all
16,418 alternating four-by-four matrices over fields of sizes 2,3,5,
selects their 3,519 rank-two forms, and conjugates by a four-cycle
inside the Levi. Of these commutators, 2,400 have rank four. For one
such witness in each characteristic it directly verifies the quadratic
isometry equations, actual commutator identity, prime order, and fixed
hyperbolic pair in natural dimension ten. This differs from the
author's three selected dimension-24 witnesses.

The finite dimensions here certify identities and demonstrate the
rank-four phenomenon. They are not substituted for the universal
d>=22 proof. No general character tables, numerical representation
approximations or TeX compilation are used or claimed.
