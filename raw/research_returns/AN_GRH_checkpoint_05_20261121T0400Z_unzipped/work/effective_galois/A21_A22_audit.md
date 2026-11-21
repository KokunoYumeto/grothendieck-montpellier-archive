# A21–A22: complete proof and source audit

Date: 2026-11-21. Author/rechecker: GPT-6 Astra Pro,
/root/effective_galois; reasoning effort is not exposed.

## Files and final checksums

- A21_GENERIC_ODD_TORSION.tex:
  edfc8cb14ee02980e82de31d9b857eed2fa62ca29707ad997ae2696b54c51111.
- A22_FINITE_SUPPORT_AVOIDANCE.tex:
  ee6d60103cf89c721fd69c577d1fa953dd971d91c28057be135fdcc5887452a1.
- A21_A22_BIB.tex: bibliography fragment. OzmanPries2019 already
  occurs in the parent's main bibliography and should not be duplicated.

Both complete current proofs were reread after the corrections listed
below. Author/rechecker outcome: **PASS**. The parent independently read
both complete proofs and reported PASS. The GT sibling independently
read both complete proofs and reported PASS, with the terminology
correction recorded below. No numerical certificate is required or
claimed for these two symbolic arguments.

## A21: exact mathematical content

For either genus-two stratum of positive 2-rank, every geometric
generic curve has no nonzero odd-order point on its Raynaud theta
support. This includes all prime powers and all composite odd orders.
Every connected odd cyclic cover of that geometric generic curve
therefore has ordinary whole new factor.

The proof uses published single-prime monodromy, proves the finite
product independence, and then gives a direct intersection
contradiction. It does not assert that the prime-degree
Ozman–Pries degeneration proof was already published for arbitrary
composite degrees.

### Checked points

1. **Generic monodromy, including a possibly nonnormal original
   stratum.** Ozman–Pries explicitly states irreducibility of the
   full level-ell torsor in the proof of Proposition 4.3. Pullback
   along tricanonical frames has geometrically integral GL5 fibres,
   so that torsor remains irreducible. Restriction to a smooth
   dense scheme open preserves irreducibility. Thus the generic
   mod-ell Galois image is full. The closed l-adic image is full
   by the published lifting theorem. This avoids the generally
   invalid shortcut that any smooth open of an irreducible
   nonnormal base has the same fundamental group.

2. **The Frobenius twist.** Relative Frobenius gives a power-of-two
   isogeny between the two Jacobians, hence an odd-adic
   similitude isomorphism. Full symplectic monodromy is preserved
   by that conjugacy.

3. **Joint monodromy.** Each odd local finite symplectic group is
   perfect. Its congruence kernel is an ell-group; every simple
   quotient must therefore be nonabelian and factor modulo ell.
   The unique possible simple quotient is PSp4(F_ell). The
   displayed orders strictly increase at distinct primes. The
   proof gives the two-factor Goursat argument and the induction
   for a product; it does not assume linear disjointness.

4. **Exact order and translation.** Local primitive vectors extend
   to symplectic bases; Chinese remainders give transitivity at
   any odd n. If one exact-order-n point is on theta, Galois
   invariance puts all such points there. The points
   e1 + j(n/ell)e2 retain exact order n because the first
   coordinate is 1, for every exponent of ell in n. There are
   ell distinct points in theta intersect theta+T, contradicting
   the genus-two bound 2. The bound is reproved by
   Riemann–Roch and uniqueness of an effective degree-one divisor.

5. **Whole new factor.** For an n-torsion cover line M, every
   nontrivial M^i is of nonzero odd order. With
   L_i=(M^i)^(1), the identity F*L_i=M^(2i) and the
   B-sequence give an injective map between one-dimensional
   H1 spaces. Multiplication by two permutes all nontrivial
   characters, including imprimitive ones. Thus the complete
   nontrivial sum has stable rank n-1, and the whole Prym is
   ordinary. No Artin primitive-root condition is needed for
   this generic statement.

## A22: exact mathematical content

For every finite set S of odd primes, for either 2-rank 1 or 2,
there is a genus-two curve over a finite field whose theta support
has no nonzero geometric torsion point with order supported on S.
All exponents and mixed products are excluded. Such curves can
be found inside every prescribed nonempty moduli open.

This is a uniform finite-support obstruction across varying curves.
It is not an assertion that any one finite-field curve avoids every
odd order, and it does not decide the variable-prime incidence gate.

### Checked points

1. **Finite incidence.** In a smooth characteristic-two curve
   family, B is a relative line bundle. The translated Abel map
   R -> O(R) B^-1 exists without a rational section. Its proper
   image is the relative theta support. Intersection with the
   nonzero finite etale N-torsion has closed finite image on the
   base. A21 makes this a proper closed set, so only finitely
   many incidence conditions are removed.

2. **Scheme and constants.** Tricanonical frames provide a smooth
   geometrically integral affine scheme with a universal family.
   All data descend to a finite constant field, which is enlarged
   to contain mu_(N^2). The full joint geometric image at N^2
   makes the symplectic frame torsor geometrically connected and,
   by smoothness, geometrically integral.

3. **Twisting and Frobenius.** The target matrix is diagonal
   ((1+ell),(1+ell),(1+ell)^(-1),(1+ell)^(-1))
   modulo ell^2, in the basis order e1,e2,f1,f2.
   It is symplectic, has order ell, is identity modulo ell,
   and its difference from identity divided by ell is invertible.
   The full target has order N. The twisted arithmetic descent
   action on frames is F(v) gamma^(-1). Finite affine Galois
   descent is effective. A rational point of the fixed twist
   over degree m with m=1 mod N gives F^m(v)=v gamma.
   Lang–Weil supplies such points for every sufficiently large
   m, so a degree in this progression exists. Minimal degree
   of the point is irrelevant: the resulting curve is considered
   over the chosen degree-m field.

4. **No extra rational primary exponents.** Lifting the frame to
   T_ell gives Phi-I=ell A_ell with A_ell invertible. The
   kernel on (Q_ell/Z_ell)^4 is exactly ell-torsion.
   Therefore J(F_Q){S}=J[N], including all mixed squarefree
   orders.

5. **All geometric exponents.** A19 applies with d=1 because
   Phi fixes every J[ell]. It places every geometric S-primary
   theta point in the rational subgroup J[N], whose nonzero
   points were excluded by the finite incidence open.

## Exact sources opened in this audit

### Achter–Pries, 2008

Monodromy of the p-rank strata of the moduli space of curves,
IMRN 2008, Art. rnn053, DOI 10.1093/imrn/rnn053.

Primary author PDF:
https://www.math.colostate.edu/~achter/math/prm0508.pdf

Verified: Theorem 4.5 (author p14); Section 5.1,
Lemmas 5.1 and 5.2 (author pp17–18).
Web refs:
turn816328545view1, turn709161711view2.

The proof of Application 5.9 (author p20) was also read as a
comparison for the smooth-open method, but its stated g>=3
application is not invoked as a genus-two theorem.

### Ozman–Pries, 2019

Ordinary and almost ordinary Prym varieties, Asian Journal of
Mathematics 23(3), 455–478, DOI 10.4310/AJM.2019.v23.n3.a5.

Primary published PDF:
https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0003/AJM-2019-0023-0003-a005.pdf

Verified: Theorem 4.2 and complete proof of Proposition 4.3,
printed p465. In particular the full symplectic level cover,
not only the nonzero torsion-point cover, is explicitly
asserted irreducible.
Web refs:
turn780184238view0, turn164487118view0, turn173741818view1.

### Landesman–Swaminathan–Tao–Xu, 2017

Lifting subgroups of symplectic groups over Z/ell Z,
Research in Number Theory 3, Article 14,
DOI 10.1007/s40993-017-0078-6.

Primary published text:
https://link.springer.com/article/10.1007/s40993-017-0078-6

Verified: Theorem 1, exact hypotheses and conclusion;
Proposition 1(b), exact statement and whole immediate proof.
The published proposition numbering is used; the current
arXiv version has different numbering.
Web refs:
turn709161711view0, turn780184238view1.

The complete general lifting theorem is cited, not independently
reproved. No claim is made to have rerun its authors' Magma
computations.

### Hall, 2015

Classical Groups and Geometry, author notes, version 6 May 2015.
Theorem 12.26, printed p173, PDF page179.

Primary author PDF:
https://users.math.msu.edu/users/halljo/classes/MTH913_S15/cgg_2015-05-06.pdf

Verified: perfectness, center ±I and projective simplicity with
the exact small exceptions, none of which is Sp4(F_ell) for odd ell.
Web refs:
turn816328545view2, turn709161711view3.

### Effective affine descent

Stacks Project Lemma 35.37.1, Tag 0245:
https://stacks.math.columbia.edu/tag/0245

The exact statement and full proof were read.
Web ref: turn948338109view0.

Poonen, Rational points on varieties, Theorem 4.3.5 and
Corollary 4.4.6 (pp101,104) were also read as a compatible
Galois-descent formulation, but Stacks 0245 is the direct
citation used in A22.

### Lang–Weil form actually used

Bjorn Poonen, Rational points on varieties, Graduate Studies in
Mathematics 186, AMS 2017, Theorem 7.7.1(ii)–(iii), printed p222,
with the immediate proof on pp222–223.

Author PDF:
https://math.mit.edu/~poonen/papers/Qpoints.pdf

Verified: finite-type scheme formulation, geometrically irreducible
fibre asymptotic, and nonempty rational points for sufficiently
large finite fields. Applying it to the fixed twist over its
fixed constant field gives points over every sufficiently large
extension degree.
Web refs: turn173741818view0, turn976609302view0.

An attempt to open the 1954 original through the AMS/DOI link
did not return the paper. No claim to have inspected that
original is made; the exact author-book theorem above is the
verified input.

## Corrections made before final checksums

- The published LSTX title was corrected from Z_ell to Z/ell Z;
  the theorem and proposition used were unchanged.
- A22 initially used the inaccurate phrase “geometric generic
  fibre is connected.” GT pointed out that a geometric fibre
  of a finite etale cover is split. The final source correctly
  says that the restriction over the algebraic closure of the
  constant field to the generic point of the base is connected.
  This is exactly the generic monodromy consequence used.
- Added the explicit Stacks citation and the unambiguous
  symplectic basis order e1,e2,f1,f2.

No changes were made in the parent's final directory.
