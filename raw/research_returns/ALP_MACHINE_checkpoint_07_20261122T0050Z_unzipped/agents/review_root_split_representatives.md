# Whole-proof review of AM-R-007

Reviewer: /root/lift_accounting, GPT-6 Astra Pro; ALP_MACHINE,
21 November 2026 UTC. Read the entire saved file
work/research/split_place_class_representatives.md, including its
scope and transport boundary. Outcome: PASS in the stated scope.

The proof correctly separates determinant weak approximation from
simply connected strong approximation. At a nonsplit place the
norm-one torus is compact, so only finitely many determinant-level
conditions remain. Hilbert 90 followed by weak approximation in E
does place one rational norm-one element in those finitely many
open cosets; no strong approximation for a torus with a finite
omitted set is being assumed.

The diagonal determinant section is valid in a Hermitian diagonal
basis, regardless of its signs. It is defined over F and proves
local/global surjectivity. The determinant image of an arbitrary
compact open is open because a sufficiently small neighborhood
under that section lies in the compact open. At almost all places,
the chosen basis and compact model are integral, giving the claimed
maximal norm-one units.

The factor order in (R7.6)–(R7.8) is correct. In particular,
strong approximation is applied to
$(aKa^{-1})\cap SU(\mathbb A_f)$, not to the original K. If
$h=\gamma u_0k''$, then
$g=s(t_0)\gamma(u_0a)(a^{-1}k''a)k$ has rational first factor,
split-supported middle factor and final factor in K. This avoids
commuting a nonrational determinant section past a rational SU
matrix.

I directly opened Rapinchuk's primary author exposition,
https://library.slmath.org/books/Book61/files/70rapi.pdf,
Theorem 2.3, printed p. 281 (PDF p. 13). Its hypotheses are
connected absolutely almost simple and simply connected, with
noncompact product over the finite omitted set. For SU(V), n≥2,
these hypotheses hold; the relative split place supplies
SL_n(F_v), hence noncompactness. Including all archimedean places
and that split place gives precisely the density used in (R7.7).
The argument choosing the omitted-place component of k'' to be
one is valid after the product-compact reduction.

For E=Q(ζ7), the standard determinant compact is the full integral
norm-one torus, and ALP-LIFT-09 (V2)–(V6) proves its finite class
number one in the needed adelic sense. Setting the determinant
split representative a=1 therefore yields the single-place
factorization at the unique place above11. The relative splitting
test uses <4>={1,2,4}, which does not contain −1; its image in the
real Galois quotient has order3. Both claims are correct.

The conditional transport statement appropriately retains common
rational left and compact right equivariance. The representative
theorem does not establish those laws for a fixed-base two-average
theta assignment. Its lack of denominator, index and height bounds
is explicitly retained. No modification to the proof is required.
The only editorial update is to replace the forthcoming parallel
finding reference by ALP-LIFT-09, (V2)–(V6).

This is a whole-proof targeted check, not a new proof of the
Kneser–Platonov theorem and not a formal verification.
