# K17-GL2-CONDUCTOR — completed argument and source resolution

Date: 2026-11-21. Author: root, GPT-6 Astra Pro, effort not exposed.
Status: exact coefficient-prime compatibility source recovered in Saito’s own survey, section2c Theorem3 p9 (suams.pdf); the final proof is gl2_conductor_section.tex. Original1997 publisher PDF was not recovered and no original theorem number is invented.

Let e>=1, ell>3, and let rho satisfy the actual pinned-source predicate
Adm2A(iota,e,6). It supplies a continuous irreducible representation W of
G_Q, a classical cuspidal eigenform of weight 2e+1, and an attachment of
R=W chi_ell^(-e) to that eigenform. The representation rho is conjugate to
1 direct-sum W|G_E, for E=Q(sqrt(-3)). The level assertion is the literal
Level(ell,6,(e,-e),W), and the determinant of W has cyclotomic weight zero.

## 1. Characters and attachment

In characteristic zero, fixing mu6 is equivalent to fixing mu3. Thus the
source's global KillsMu6 characters are exactly characters of the quotient
Gal(Q(mu3)/Q), of order two. Over a characteristic-zero coefficient field
they are either trivial or the quadratic character chi_-3. This applies
to every character witnessing both parts of Level.

Let f be the primitive normalized eigenform associated to the simultaneous
eigensystem in the source's Newform. Its primitive level divides the source
level; the source's new/minimal-level clause excludes a proper divisor.
The source attachment asserts semisimplicity and equality of characteristic
polynomials at all but finitely many geometric Frobenius elements.
Chebotarev density and Brauer-Nesbitt therefore identify R with the
semisimple Deligne representation of f. It can consequently be defined over
a finite extension of Q_ell; in particular local flags and characters may
be considered over a finite coefficient extension as well. Its determinant
is epsilon chi_ell^(-2e), where epsilon is the finite nebentypus of f.
Since f has odd weight, epsilon(-1)=-1.

## 2. Away from the coefficient prime

At q != ell, the source level gives the actual inertia representation of W
as a direct sum of two characters, each 1 or chi_-3. The same is true of R,
because the ell-adic cyclotomic character is unramified at q. Finite inertia
implies that the monodromy operator in WD_q(R) is zero: on an open inertia
subgroup the representation is literally the identity, so its logarithm is
zero. Thus WD is unramified at every q not in {3,ell}. At3 its inertia is a
direct sum of 1/chi_-3 characters, with zero monodromy. These characters are
tame, because their order is2 and the residue characteristic is3.

Carayol1986, section0.7, Theorem(A), pp410-411, identifies this full local
Weil-Deligne representation with the parameter of f at every q != ell.
The extra discrete-series hypothesis in section0.3 is imposed only when
[F:Q] is even; it is absent for F=Q. Artin conductors therefore agree with
the primitive automorphic conductors at all these primes.

## 3. At the coefficient prime

Local-global compatibility for classical modular forms at ell, including
potential semistability, is Saito1997 (exact primary locator under audit).
The Saito2000 supplement, Theorem3, pp429-430, concerns weight-monodromy;
it is not alone a substitute for the local-global compatibility theorem.
The Saito2009 Hilbert paper as written assumes degree>1 and is not directly
being cited for F=Q.

The ordinary flag of W has characters kappa_1,kappa_2 whose restrictions
to inertia at ell are chi_ell^e and chi_ell^(-e), because chi_-3 is
unramified there. Hence the characters in the induced flag of R are
delta_1 and delta_2 chi_ell^(-2e), with delta_i unramified and continuous.
The image of a continuous unramified character of the profinite group G_Qell
is compact; its value on Frobenius is therefore an ell-adic unit. Each
rank-one character is crystalline, has trivial WD inertia, and has a
single Frobenius slope. The two slopes differ in absolute value by2e.

Apply the exact functor D_pst to the flag, over a common sufficiently large
finite extension over which R is semistable. The WD Frobenius eigenvalues
are those of the two graded rank-one objects. In the usual arithmetic
Frobenius convention the relation between monodromy and Frobenius is
N phi = ell phi N (or ell^f after passage to the maximal unramified field).
A nonzero N in dimension two forces the two slopes to differ by1.
Since 2e>=2, this is impossible. Thus N=0. WD inertia has finite image and
both one-dimensional graded characters are trivial, so finite-group
semisimplicity in characteristic zero makes the whole inertia action
trivial. Consequently WD_ell(R) is unramified with zero monodromy.
Local-global compatibility implies f is unramified at ell.

This argument uses the actual ordinary flag and its separated weights,
not a general assertion that arbitrary potentially semistable extensions
of crystalline characters are crystalline.

## 4. Exact conductor and character

The nebentypus epsilon is now unramified at all finite primes except3 and
its inertia at3 has order at most2 and conductor exponent at most1.
Therefore its primitive Dirichlet conductor divides3. Its odd parity
forces epsilon=chi_-3. At3 the determinant of the WD inertia is accordingly
chi_-3. Among two characters each equal to1 or chi_-3, exactly one is
chi_-3. Their tame Artin conductor is1; N=0 adds nothing. Thus f has
primitive conductor exactly3 and belongs to
S_(2e+1)(Gamma_0(3),chi_-3).

## 5. Trace normalization

Let p split in E, p != 3,ell, and choose arithmetic Frobenius sigma at a
prime of E above p. Its image in G_Q is arithmetic Frobenius at p. The
source uses geometric Frobenius sigma^(-1), and
R(sigma^(-1))=p^e W(sigma^(-1)). The attachment and local compatibility
give iota tr R(sigma^(-1))=a_p(f). Consequently

    iota tr rho(sigma^(-1)) = 1 + a_p(f)/p^e.

For e6 this is precisely the full weight13 conductor3 space in
K17-GL2-MODEL. Its complete T7 polynomial therefore covers every admissible
rank-two-branch trace.

## Audit resolution, 2026-11-21 04:21 UTC

Saito, Galois representations in arithmetic geometry, section2c Theorem3 p9, with complete definitions pp7–8 and proof outline p9, explicitly states full Frobenius-semisimplified WD compatibility for classical modular forms over Q. Root and archive read the complete section and visually verified pages8–9. Colmez–Fontaine author version section4.1 Proposition4.2 p23 gives exactness; section3.3 p21 gives N lowering slopes by1; section4.2 Proposition4.4 and its full rank-one proof p24 give the character calculation. The following historical checklist is retained as superseded working history.

## Original audit checklist (resolved by the sources above)

1. Recover the exact primary Saito1997 local-global theorem statement.
2. Record exact standard references for the D_pst properties used in the
   elementary slope argument (or cite the corresponding closed pinned
   source statement, retaining all its hypotheses).
3. Independent whole-proof read, final TeX readback, and root event log.
