# Real and rational lifting of the prescribed CM comparison

Date: 2026-11-19. Agent: GPT-6 Astra / period_generation.
This proof was developed with an independent source/proof pass by
elliptic_splitting. It addresses the rational abelian subproblem, not the
full pure integral target E.2.3(d). Parent will decide integration and IDs.

## 1. Objects, groups, and the prescribed point

Fix Qbar inside C. Let Fcm be the compositum, inside Qbar, of K^ab for all
finite CM fields K. Fix sigma in Gal(Qbar/Fcm).

Use the category AV(Q) of pure abelian motives with absolute Hodge
correspondences, including Artin motives and Tate objects, as in
Milne2004 Section3. Its Betti group is G_AV,B over Q. Write G_CM,B for
the group of its CM/Artin subcategory, pi:G_AV,B -> G_CM,B for restriction,
and D=ker(pi).

E.2.6 constructs a prescribed rational point g_sigma in G_CM,B(Q).
On CM abelian varieties its maps are the actual algebraic isomorphisms
alpha_B:B -> sigma B whose action on every rational Tate module is
Galois transport sigma. It acts on finite geometric sets by x -> sigma x
and on the one Tate line by the identity.

The extension from algebraic correspondences to the absolute-Hodge
CM category has an exact primary theorem, not an assumed extension:
Milne1994, corrected author version Seattle2.pdf, Theorem3.15,
printedp41, states that for each CM motive M and representative r~(sigma)
of its reciprocity class there is a unique isomorphism alpha:M -> sigma M
carrying each labelled Hodge tensor s to sigma s and satisfying

    sigma(v)=alpha_f(r~(sigma)v) in the finite-adic realization.

The reflex field is CM or totally real. If E is totally real,
E(i) is CM and E^ab E(i)/E(i) is abelian, so E^ab is contained in
E(i)^ab and hence in Fcm. The same containment is immediate for CM E.
Thus sigma acts trivially on the relevant E^ab, the reciprocity class
is trivial, and r~=1 gives exactly the maps above. This proves their
naturality for all absolute Hodge tensors. Alternatively their equality
on finite-adic realizations and faithful Betti--étale comparison gives
the same naturality. No rational Hodge conjecture is used.

The fibre to be studied is the actual right D-torsor

    X_sigma=pi^(-1)(g_sigma).

The next two sections construct X_sigma(R), retaining the prescribed
CM point rather than allowing an arbitrary CM comparison.

## 2. Every finite diagram has a compatible real Hodge isometry

Take finitely many abelian varieties over Qbar, finitely many absolute
Hodge tensor maps on their cohomology, chosen polarizations, and finitely
many CM objects on which the required comparison is the prescribed alpha.
One product A of the abelian generators realizes all the tensor data;
include the projectors onto the factors and their labelled polarizations.
Include a product B of CM abelian generators for the finitely many
requested CM objects as additional factors of A. CM direct summands and
tensor constructions are recovered by their specified projectors.

Let V=H1(A(C),Q), with its integral lattice Lambda and its Hodge
homomorphism h. Let G=MT(V,h), and let X be the G(R)-conjugacy class of h.
The polarizations are Tate-valued; include the one Tate object throughout.
The connected Shimura domain X+ containing h is a G^ad(R)^+-orbit.
The indexed tensor family can be enlarged to cut out G, retaining every
original labelled tensor. All these Hodge tensors are absolute Hodge
because they belong to tensor constructions on abelian varieties.

The precise moduli bridge is:

* Milne corrected Seattle2 Example3.1, printedp36, constructs this
  Shimura datum and the level subgroup K(N) defined by Lambda and
  identity modulo N.
* Lemma3.29, printedpp45--46, proves that the defining condition
  (3.28.1) for the indexed Hodge tensors holds at every embedding over
  the reflex field once it holds at one.
* Theorem3.31, printedp46, identifies its canonical model with the
  moduli problem of an abelian motive, the indexed Hodge tensor family,
  and the level structure.
* The integral local system is explicit in the same source:
  (2.7.1)--(2.7.3), Proposition2.8, Example2.11 and Theorem2.12,
  printedpp23--25, construct the constant lattice Lambda on X and
  its quotient by Gamma(N), with the indexed horizontal tensors and
  constant level-N structure. Take N sufficiently divisible and
  divisible by3. Example3.1 p36 places S(N)=Gamma(N)\X as an open and
  closed part of Sh_K(N); Example3.7 p38 identifies K(N)-level with
  this integral level structure. Thus the endpoint lattice is the
  actual H1_Z lattice, not merely an isogeny-class representative.
  Equivalently the K(N)-orbit of the finite-adic level determines the
  lattice eta(Lambda tensor Zhat); intersecting it with the rational
  realization recovers Lambda. The conjugate level recovers the
  actual lattice of sigma A by this same formula.
  The one Tate line is included with its integral lattice as in
  Remark2.13, p25; its monodromy is an integral unit congruent to1
  modulo3, hence is1.

Write E=E(G,X). Milne's proof of Theorem3.33, printedp46, shows that E
is a subfield of a CM field; equivalently E is CM or totally real.
For completeness, a subfield of a CM field is CM or totally real:
pass to a CM Galois closure, where complex conjugation is central.
It preserves every intermediate subfield, acting there either trivially
(the field is totally real) or as its unique CM involution.
The field calculation in Section1 therefore gives E^ab contained in Fcm.

Choose the level using the actual torsion of A, so the resulting
algebraic point P has sigma-conjugate sigma P carrying precisely the
sigma-conjugate tensors and the sigma-transported level.
Deligne1979, Section2.6.1 and Theorem2.6.3 (Milne translation printedp46),
states that the action on geometric connected components factors through
Gal(E^ab/E). Since sigma fixes E^ab, P and sigma P lie in the same
connected component at this level. There is an analytic path between
them. Parallel transport in H1_Z gives an integral tensor isomorphism

    T_0:H1(A(C),Z) -> H1(sigma A(C),Z)

preserving every labelled tensor and the polarization, and compatible
with sigma on level N. In particular it preserves every factor projector.
There is no assertion that T_0 itself preserves the Hodge filtration.

### 2.1 Exact equality on the prescribed CM factor

The representation of G on H1(B) factors through the torus MT(B);
therefore its Hodge homomorphism is constant along X+ (conjugation in
that torus is trivial). The restriction T_0,B is consequently an
integral Hodge isomorphism B -> sigma B, as well as a polarization
isometry. It induces sigma on B[N]. The prescribed alpha_B has the
same properties, and also induces sigma on B[N]. Their quotient

    alpha_B^(-1) T_0,B

is a polarized integral Hodge automorphism of B that is the identity
modulo N. Such an automorphism is the identity for N>=3 (one may use
N divisible by3). Here is the needed proof. A polarized Hodge
automorphism preserves the positive definite form obtained by inserting
the Weil operator into the polarization. Its integral matrix therefore
belongs to a finite group. The subgroup 1+3 M_r(Z_3) has no torsion:
if U=I+3^s V with s>=1 and V nonzero modulo3 had prime order p,
binomial expansion modulo3^(s+1) rules out p unequal3; for p=3,

    U^3=I+3^(s+1)(V+3^s V^2+3^(2s-1)V^3)

has the bracket nonzero modulo3. Any nontrivial finite-order element
would have a power of prime order, giving the contradiction.
It follows that T_0,B=alpha_B exactly. The chosen sufficiently divisible
level was required to be divisible by3, so the displayed proof applies.

Thus the finite comparison has the specified CM restriction, not merely
some isomorphic restriction. Its action on Tate is the identity: the
level compatibility and sigma fixing roots of unity give multiplier1
modulo N, and parallel transport in the polarized family fixes the
labelled Tate orientation directly.

### 2.2 The Hodge correction preserves that restriction

Trivialize along the path. The source Hodge homomorphism h and the
pulled-back target T_0^(-1) h_{sigma A} T_0 lie in the same X+.
The homomorphism

    G^der(R)^+ -> G^ad(R)^+

is surjective. Its differential is an isomorphism, so the image is an
open subgroup of the connected target; hence it is the whole target.
Choose d in G^der(R)^+ whose conjugation carries h to
T_0^(-1) h_{sigma A} T_0. Then

    T=T_0 d

is a real Hodge isomorphism sending every labelled tensor to its
sigma-conjugate. It preserves the polarization because its similitude
character factors through G^ab and is trivial on G^der. For the same
reason d acts trivially on every CM representation, in particular
H1(B), so T_B=T_0,B=alpha_B. It also fixes the Tate line.
The adjustment d is real; its integrality is not asserted.

This proves the claimed finite-diagram real Hodge/polarization
comparison with the prescribed finite CM restriction.

## 3. Coherence on all abelian motives and all Artin blocks

Choose one polarization on each abelian variety A/Qbar. Let C_A be the
set of real Hodge isometries from H1(A) to H1(sigma A) for these
polarizations and their sigma-conjugates. Each C_A is nonempty by
Section2, and is compact: after choosing one isometry it is a closed
subgroup of the orthogonal group of the associated positive definite
real form. Form the product of all C_A.

For every absolute Hodge correspondence, factor projector, tensor
identification, duality map, cup product and chosen labelled
polarization, impose its naturality equation on the relevant factors.
These are closed equations involving finitely many coordinates.
For every CM generator also impose the equality T_B=alpha_B. Every
finite family of these equations has a solution by Section2, after
taking the product of its finitely many abelian generators and CM
generators. The product is compact, and the finite intersection
property gives a simultaneous solution.

The resulting maps on H1 extend by tensor products, exterior powers,
duality and the one fixed Tate line. Naturality for each specified
projector restricts the maps to its image. If two such presentations
represent the same motive, the transition isomorphism is another
absolute Hodge correspondence, whose naturality equation was included.
Consequently this construction gives a well-defined tensor isomorphism

    omega_B,R -> omega_B,R o sigma

on all abelian motives over Qbar, with all absolute Hodge morphisms,
and with its restriction on the CM subcategory exactly alpha.

Over Q, all the Artin and nonconnected blocks are handled explicitly.
For a finite Q-scheme S, use the basis permutation e_x -> e_{sigma x}
on H0(S(C),R). For an abelian variety or a smooth projective product
defined over a finite L/Q, the underlying Q-scheme has Betti
decomposition over embeddings u:L -> Qbar. Send its u block to its
sigma u block by the constructed real map for that geometric abelian
motive. The multiplication and module actions of h0(Spec L) select
these blocks, and its diagonal sum e_u tensor e_u selects relative
tensor products, exactly as in E.2.3.

Naturality for Q-correspondences follows after base change to Qbar,
where each block equation has already been imposed. Equality after
this direct-sum decomposition is equality of the original real
linear maps. The Artin permutations commute with restriction of
embedding sets under finite field maps. Thus the maps are compatible
for different L and for all decompositions. On a Q-defined motive,
sigma-conjugation has its canonical identification with that same
motive, so the resulting maps give an element

    g_R in G_AV,B(R), with pi(g_R)=g_sigma.

This proves X_sigma(R) is nonempty, including the prescribed CM and
Artin restrictions. It does not impose geometric real-Frobenius
intertwining; E.2.7 gives the explicit reason that such an additional
requirement fails for the quartic witness.

## 4. The resulting rational abelian lift

For each finite prime ell, the Galois action of sigma on the étale
realization of all abelian motives over Q, carried through the
Betti--étale comparison, gives an element

    g_ell in G_AV,B(Q_ell).

It is natural for absolute Hodge correspondences through their étale
realizations and fixes all Q-defined tensor maps. On CM motives
Theorem3.15 with representative1 gives
pi(g_ell)=g_sigma tensor Q_ell. Hence X_sigma(Q_ell) is nonempty.
Section3 supplies the real point as well.

Milne2004, Proposition3.12 and the proof of Theorem3.13, printedp26,
show that D is a countable product of semisimple algebraic groups
whose geometric simple factors have covering index1 or2. The same
statement holds for its torsor twists. Proposition3.5, printedpp23--24,
gives injectivity of H1(Q,D_i) into the product of all local H1 for
each such algebraic factor. Corollary1.14, printedp9, identifies H1
of the countable product with the product of the H1 sets. Therefore

    H1(Q,D) -> product_v H1(Q_v,D)

is injective. The torsor class [X_sigma] is zero at every place,
by the actual points just constructed. It is therefore zero globally,
and X_sigma(Q) is nonempty.

This is a rational tensor lift in the absolute-Hodge abelian category.
It proves that the specified CM comparison has a rational extension
there, and in particular provides a rational abelian comparison for
the two quartic places in E.2.6. The rational point obtained by the
Hasse argument need not equal the constructed real Hodge point after
extension to R. No integral lattice preservation, no prescribed
ell-adic equality of that rational point, and no comparison on all
pure motives is proved.

## 5. Checks, limitations, and source access

The remaining main target is still E.2.3(d) for the full pure integral
diagram. E.2.9 imposes the projective Tate identities on every abelian
generator of an integral lift. The real correction and Hasse argument
above do not establish those identities for the rational lift.
E.2.10 exhibits exactly why finite congruence solvability alone cannot
supply their simultaneous solution. These explicit maps record the
coefficient and category transitions; this note is not counted as a
solution or a strict-ledger advance of the full pure integral question.

Sources independently opened by period_generation:

1. https://www.jmilne.org/math/xnotes/Seattle2.pdf .
   Corrected author's1994 manuscript, updated13Mar2018,72pages.
   (2.7.1)--(2.7.3), Proposition2.8, Example2.11 and Theorem2.12
   pp23--25; Example3.1 p36; Example3.7 p38; Theorem3.13 p40;
   Theorem3.15 p41;
   Lemma3.29 pp45--46; Theorem3.31 p46; proof of3.33 p46.
   Webrefs turn905602595view0, turn402736447view0/1/3,
   turn419992865view1/2, turn223910385view2,
   turn828445026view0/1.
2. https://www.jmilne.org/math/Documents/DeligneSV.pdf .
   Milne's translation of Deligne1979, corrected6Sep2020,52pages.
   Proposition2.1.14 p27 and its general Shimura-datum scope;
   Section2.6.1 and Theorem2.6.3 p46, component reciprocity.
   Webrefs turn905602595view1, turn402736447view2,
   turn223910385view0/1.
   The translator flags a reciprocity inversion misprint; only
   triviality on Gal(Qbar/E^ab) is used, so that convention has no effect.
3. https://www.jmilne.org/math/articles/2004cP.pdf .
   Original submitted author version2002/2003,34pages.
   Section3.1 exact Artin sequence p22; Proposition3.5 p23 with proofp24;
   Proposition3.12 and Theorem3.13 p26; Corollary1.14 p9.
   Webrefs turn419992865view0, turn636870960view0/1,
   turn655330826view1.

Elliptic_splitting independently supplied and read the exact Shimura
moduli/component locators and checked the finite CM equality and compact
real construction. Parent has been asked to audit before assigning an
integrated result number. The initial main source gates have been
replaced in this note by the displayed constructions, while the
integral/full-pure gate remains explicitly untouched.
