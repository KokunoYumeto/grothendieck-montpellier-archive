# Global C3: moving-prime germs and the limits of operation invariants

2026-11-19. Owner /root/automorphisms.
This is an investigation of the actual remaining global gate, not
a claim of either a C3 proof or a C3 counterexample.

## 1. Arithmetic localization does not detect a bounded-weight germ

Choose distinct primes p_w, one for each positive weight w. Put

    M_w=Z/p_w,   S^+ M=0.

This is a nonzero graded S=Gamma_Z(T)-module with unbounded support.
It is nonzero in the Serre quotient by modules whose weights have
one finite upper bound. Yet M tensor Q=0, and for each fixed prime p
the module M tensor Z_(p) has at most one nonzero weight. Its
bounded-weight germ therefore vanishes after every arithmetic
localization. This gives a precise failure of exchanging:

    for every prime p, there exists a weight bound N_p

with:

    there exists one weight bound N for all primes.

No choice of large finite maxima over primes proves the second
statement. The example is a module, not a generalized PD theory
and not an invariant distinguishing two admissible theories.

## 2. The larger localizing shadow quotient erases this phenomenon

Let T be the localizing Serre closure of bounded-weight modules,
as in the robust shadow quotient. The displayed M is a direct
sum of bounded-weight modules and therefore belongs to T.

More generally suppose a graded Z-linear S-module M has bounded
rational support and has bounded p-local support for each p.
Choose N such that the tail M_{>=N} is rationally zero. It is a
torsion abelian group, and decomposes naturally as the direct
sum of its p-primary submodules. The S action preserves this
decomposition. Each p-primary submodule is isomorphic to its
p-localization and hence has bounded weight support. The tail
belongs to T by closure under direct sums, and M/tail is bounded.
Thus M itself belongs to T.

Therefore arithmetic localization is conservative for this
particular zero-object question after taking the localizing
closure, but it is not conservative for the stronger uniform
bounded-weight germ. Shadow recovery in the larger quotient
can discard precisely the nonuniform information that must be
controlled in an actual eventual theory.

## 3. A fixed finitely generated operation group cannot carry a moving prime

Lemma. Let G be a fixed finitely generated abelian group and let
g_w be a sequence of its elements. If for every prime p the
elements g_w become zero in G tensor Z_(p) for all sufficiently
large w (with bound depending on p), then g_w=0 for all
sufficiently large w.

Proof. Let P be the finite set of torsion primes of G, and add
one arbitrary prime p_0 to detect the free part. The map

    G -> direct_sum_{p in P union {p_0}} G tensor Z_(p)

is injective. Take the maximum of the finitely many eventual
bounds for this detecting set. This proves the lemma.

The same proof works for any family of operation values
detected by one fixed finite prime set and an injective
localization of the torsionfree part. Finite generation is
a convenient sufficient condition.

## 4. Application to fixed ordinary primary operations

For fixed positive input degrees i_1,...,i_r and fixed output
degree j, a natural operation

    product_a H^{i_a}(-;Z) -> H^j(-;Z)

is determined by its value on the universal tuple in the
finite product of Eilenberg-MacLane spaces K(Z,i_a).
This follows directly by representing every input tuple and
pulling back the universal value; no additivity is required.

The representing abelian group

    G=H^j(product_a K(Z,i_a);Z)

is finitely generated. The primary source opened in this run
is Serre1953, Chapter I section6.1 (printed p264) and Chapter II
section6 Proposition8 (printed p271): for finitely generated
abelian Pi, the integral homology of K(Pi,n) is finitely
generated in each degree. The ordinary integral Kunneth and
universal coefficient sequences give the asserted finite
generation for a finite product and its cohomology.

Consequently, suppose an operation of this fixed type is
well-defined for weighted section cohomology, commutes with
coefficient localization, and is respected by theory maps.
The local comparison theorems identify its operation classes
for all sufficiently large weights at each fixed p. Restricting
the localized operation to the integral universal tuple
identifies that equality with equality in G tensor Z_(p).
The lemma above then identifies the integral operation germs
after one finite weight bound.

This rules out a difference in one such fixed primary
operation as the missing global C3 invariant. It does not
prove that every divided power on cochain cycles descends
to a cohomology operation: that separate well-definedness
condition is explicitly required. Nor does it establish
coherent choices of all operations or of comparison maps.

## 5. What this does and does not settle

Allowing the arity/output degree to grow changes the
representing group. The finite-prime lemma then gives
different bounds for different operations. This is
compatible with the definition of an eventual theory,
whose threshold already depends on form degree; it does
not itself create an obstruction at one fixed degree.

Families with coefficients F_p varying with p do not live
in one fixed representing group, so the lemma alone does
not cover them. The ordinary Bockstein, when the flatness
hypotheses give the coefficient exact sequence, is the
canonical connecting morphism and is preserved by strict
coefficient-linear comparison maps. It therefore does not
supply a freely adjustable invariant. No classification
of every coefficient-varying or higher coherent operation
is asserted here.

The known low-degree prime-weight class from C15 occurs
in a free coefficient-tail resolution that is not
admissible. It is a construction obstruction, not yet
an invariant of admissible theories. Likewise C31's
actual bar extension failure in an admissible target
occurs at a prescribed weight below the relevant
eventual threshold. Taking infinitely many copies in
unbounded weights while retaining their horizontal
classes would destroy eventual horizontal acyclicity.
That simple diagonal construction is therefore invalid.

## 6. Scope of C30/C32 as reductions

C30 proves a substantive arithmetic assembly theorem:
independent local repairs with strict agreement in low
form degrees assemble without an additional compatibility
condition between different primes. C32 also supplies
the common-source and homotopy-equalizer mechanism that
trivializes all localization loops.

Their repair hypothesis is sufficient, not proved
necessary. Ordinary local uniqueness does not imply
factorization under the specified entire partial model
P with actual low-degree isomorphisms. C32 further
requires those repairs for constant-cohomology targets
such as T_eq, whose vertical H1 is nonzero. Thus these
theorems isolate one concrete local construction whose
success would settle global C3; they do not establish
an equivalent or demonstrably easier reformulation.

## Primary-source receipt

sources/B_serre1953_classes.pdf
sources/B_serre1953_classes.txt
code/B_fetch_serre1953.py
logs/B_serre1953_fetch.json

Exact text locators: lines394-400 (finite-generation
class), lines761-770 (Proposition8 and its induction).
Printed locator: Annals of Mathematics58(1953),258-294,
Chapter I section6.1 p264; Chapter II section6,
Proposition8 p271.
Downloaded767254bytes, SHA256
a66c570ec4e7941cd50ed925f9265580f8ba3f61156497088020cc2d636a699d,
runtime10.171391184998356sec.
Author-hosted primary PDF at College de France opened.
Sadofsky's explanatory notes Corollary2.1 p4 were also
opened for orientation but are not the cited primary basis.
