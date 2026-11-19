# C.3ay: critical ordinary injectivity in every positive characteristic

Status: finalized after full independent root and cycles proof/source audits.
Cycles certified11:31:19.776876UTC; root subsequently completed the full
typed proof, exact program and every output-case audit. Final file:
C3_positive_characteristic_critical_injectivity.tex. The former draft is
a comment-only pointer; the statement and original check events are registered.

## Exact scope

For every prime p and r>=2, the explicit normal excellent strict-local
cone of dimension2r has both source and divisor punctures regular.
An actual ordinary class of infinite order is killed by restriction
integrally. It remains a rational kernel. The coefficient field is
exactly the algebraic closure of Fpbar(E0), with the fixed all-prime
elliptic cubic of C.3x; no rational ordinary class over Fpbar itself
is asserted. The theorem makes no claim for N>=2r+1.

## Explicit choices and integral argument

The line bundle M on E has degree3 and is its plane O(1). Distinct
horizontal lines V-b_iW meet E in disjoint simple degree3 divisors:
exclude b_i^2+b_i=0 for p2, and4-27b_i^4=0 in odd characteristic.
A terminating finite-field enumeration specifies every constant.
The diagonal sections y_i(V-b_iW) have exactly3r reduced base points,
with the full local Jacobian independently diagonalized. No Bertini
choice is used in the final construction.

On the smooth incidence divisor the coefficient map factors through
the rank(r-1) universal quotient U_x. Its regular zero scheme is the
product of P_x^(r-1) with the finite base. The top-Chern class of
U_x^dual tensor A equals sum(-h)^j a^(r-1-j). Its product with the
elliptic Pic0 class is zero because that class restricts trivially to
each finite-base component. Pullback to the punctured cone imposes
h+a=0 and gives r a^(r-1)lambda=0. The same source class survives in
the exact integral quotient Pic(E)/Z(M^r); Pic0 injects by degree.
Multiplication by r is an integer Chow operation, also when p divides r.

The generic point minus the origin has infinite order because every
E0[n] is a finite group scheme over the constant field, including
p-primary kernels. Actual algebraic equivalence is supplied by the
line bundle O(Delta-{o}times E) on the fixed product E times E.
The normal degree-one Segre section ring and the all-characteristic
integral strict-cone injection C.3e supply the exact local objects.

## Fresh primary-source checks

- Stacks Lemma42.44.1, Tag0FA8, full statement and proof opened:
  https://stacks.math.columbia.edu/tag/0FA8 . A regular section of
  a rank(r-1) bundle gives its integral top Chern class. Its zero
  scheme, codimension and regular sequence are proved directly here.
- Stacks Lemma42.39.1, Tag02UB, full statement/proof and formula
 42.39.1.1 opened: https://stacks.math.columbia.edu/tag/02UB . In
  top degree the twisting coefficients are all1. The signs from the
  dual universal quotient are retained explicitly.
- Stacks Lemma42.36.2, Tag02TX, full statement and proof opened:
  https://stacks.math.columbia.edu/tag/02TX . Applied integrally
  twice to compute the exact graded quotient. These three primary
  locators are recorded in C3ay_references.bib.
- Milne, Abelian Varieties, corrected author version2January2022,
  complete49page PDF freshly opened:
  https://www.jmilne.org/math/xnotes/AVs.pdf . Proposition8.1p12 and
  Theorem8.2/proofpp13-14 were freshly read, including all-order
  finite group-scheme kernels. The existing D_MilneAbelian2022 key
  is reused. The initially tried singular AV.pdf path was inaccessible;
  the correct plural AVs.pdf was then successfully opened in full.

## Exact certificate and layout

code/check_positive_characteristic_critical_injectivity.py retains
six projective elliptic smoothness checks,24 finite-field horizontal
base cases,29 exact integer Chern identities and14 integral quotient
models. All pass, runtime0.4120008620011504seconds. The quotient
models use formal Pic=Z degree plus Z lambda, M=3 degree: Smith
normal form has one free factor and torsion3r, while an integer
functional evaluates the witness to r. These are algebraic checks,
not a claim that any finite-field point is non-torsion.

The complete draft passed its four-stage LuaLaTeX/BibTeX wrapper with
zero diagnostics, runtime2.41841830300109seconds. Source, complete
stdout/JSON and timestamped logs are retained. The independent
full proof/source reviews are now complete and passed. The final renamed
wrapper is recorded separately after completion.

Final renamed proof passed all four wrapper stages at 2026-11-19T11:35:18.897727+00:00, runtime2.543727807999seconds, zero diagnostics. Canonical final event retained separately.
