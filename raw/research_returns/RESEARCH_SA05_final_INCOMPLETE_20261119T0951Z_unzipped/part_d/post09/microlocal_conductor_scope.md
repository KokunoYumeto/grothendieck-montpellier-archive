# Microlocal conductor theorems: exact scope of the C6 follow-up

19 November 2026. This is a bounded primary-source scope check, not an
independent proof audit of the entire cited papers and not movement on
the general C6 question. It was written separately during the CP09
compiled-file freeze.

## Saito: direct images

Primary: Takeshi Saito, *Characteristic cycles and the conductor of
direct image*, arXiv:1704.04832v4, 25 February 2020; published in
Journal of the American Mathematical Society 34 (2021), 369--410,
DOI 10.1090/jams/959.

Exact opened version:
<https://arxiv.org/html/1704.04832v4>.
The abstract, introduction, equation (2.15), Theorem 2.2.3 statement,
Corollary 2.2.4 statement and its short proof, and Theorem 2.2.5
statement were read. The entire alteration/transversality and
conductor proof was not audited.

Theorem 2.2.3 concerns a quasi-projective morphism of smooth schemes
over a perfect field, with curve target, proper support, and the stated
generic singular-support transversality. It is a geometric result,
not a mixed-characteristic arithmetic trait theorem.

There is also an essential distinction in its definition of the
conductor of a complex. Equation (2.15) is

    a_y(G) = rank(G on the generic open) - rank(G at y) + Sw_y(G),

where ranks and Swan conductors are alternating for a complex. The
closed term is the actual closed stalk of G. It is not automatically
the inertia invariants of the generic representation. Applying the
formula to a proper direct image gives the special-fibre contribution
already separated from the representation-theoretic Artin conductor
in the preceding vertical-blowup diagnostic. A supplied homogeneous
generic projector alone does not identify those two closed terms.

## Saito--Xiong--Yang: current microlocal construction

Primary: Takeshi Saito, Jiangnan Xiong, and Enlin Yang, *Singular
supports, characteristic cycles, and microlocalization of constructible
sheaves*, arXiv:2609.06625v3, 6 October 2026.
Exact opened version: <https://arxiv.org/html/2609.06625v3>.
The current author publication list links this work and says that the
earlier microlocal preprint is withdrawn and subsumed into it; no old
version is used here.

The abstract and introductory statements Theorems 1.0.1--1.0.3 were
read, as were the explicitly geometric conductor application in the
introduction and Theorem 4.8.2 with its complete local proof. That
proof compares the microlocal characteristic class with the cycle
class of the characteristic cycle, then pulls back by the zero
section, including faithfully flat extension of coefficient rings.
The preceding construction theorems and their dependencies were not
fully audited.

The base remains a perfect field. The new proper Bloch formula is
explicitly the geometric case. Extension to ell-adic coefficient
fields in Section 4.9 does not change that geometric base into a
mixed-characteristic trait or assert independence when ell varies.
The source therefore supplies no missing common tame invariant
dimension for an arbitrary arithmetic motivic summand.

## Saito: the genuinely mixed-characteristic support theorem

Primary: Takeshi Saito, *On singular supports in mixed characteristic*,
arXiv:2501.07965v2, 21 April 2025; published in Contemporary Mathematics
842 (2026), 213--260, DOI 10.1090/conm/842/16858. The publisher DOI
endpoint returned HTTP403; current publication metadata was checked
on the author's publication page instead.
Exact text read: <https://arxiv.org/html/2501.07965v2>.

The abstract and introduction, Theorem 2.4.12 and its displayed local
proof, and Corollary 2.4.13 were read. This is not a full audit of the
Radon-transform construction and all its earlier lemmas. Theorem
2.4.12 gives existence of the saturated relative singular support for
regular finite-type X over an excellent regular Z_(p)-scheme satisfying
the stated finiteness conditions. Corollary 2.4.13 requires the
specified zero cotangent map, and a further tensor micro-support
condition for the absolute singular support.

Neither displayed conclusion identifies singular supports for two
different realization primes. The existence of a support for each
coefficient sheaf is distinct from its independence of coefficients.
To turn this into C6 one would still need a cross-prime support or
local-acyclicity comparison for the projected motivic system. That
comparison is not supplied by these statements.

## Conclusion of this bounded attempt

The primary theorems do not bridge either missing step: identifying
the special-stalk conductor with generic inertia invariants, or proving
cross-prime compatibility for the relevant mixed-characteristic
intermediate extension. No theorem is refuted, and no universal
nonexistence or converse impossibility is asserted. Exact retrieved
HTML versions and hashes are preserved by
`code/fetch_microlocal_scope.py` and its output manifest.
