# Complete peer proof check of K-030

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `FINITE_STABILIZER_REDUCTION.tex`. The reviewer
contributed the initial Sylow/normalizer idea and an alternative Luna-chart
justification of generic stabilizer type. This is therefore a complete
peer check of the final written proof, not an independent rediscovery
of that part. The author's self-contained Hom-scheme rigidity argument
was independently reconstructed in this reading. The root is supplying
a separate whole-proof check.

## Finite-group lemma

The Frattini argument applies to the normal subgroup H in H semidirect
<phi>. Its Sylow-two normalizer maps onto the three-group quotient.
CRT extraction of the three-primary part preserves the chosen quotient
generator. The character extends across phi because phi preserves it.
The two-primary character coset in a Sylow-two subgroup is nonempty and
has two-power cardinality. A three-group permutation of this set has a
fixed point, producing exactly an invariant H-conjugacy class, not an
unjustified pointwise phi-fixed element.

## Generic full-stabilizer type

Finite stabilizer incidence is a quasi-finite finite-type morphism on
the locus considered, so its reduced fibre cardinality is constructible.
For a fixed finite group Gamma, tangent vectors to Hom(Gamma,L) are
one-cocycles, and the displayed average shows that each is a coboundary.
The conjugacy orbit dimension therefore equals the Zariski tangent
dimension. Local dimension lies between orbit and tangent dimensions,
so the Hom-scheme is regular there and that orbit is open locally.
All orbits are open; quasi-compactness gives finitely many. Finitely
many abstract groups of a fixed order then give finitely many subgroup
conjugacy types. Fixed-point incidence and Chevalley give their
constructible strata.

For tensor points with finite effective SL stabilizer, the full stabilizer
modulo the scalar kernel is finite because a nonzero homogeneous invariant
kills a power of its determinant character. On the stable locus quotient
fibres are single closed effective-SL orbits, so the invariant constructible
conditions descend to the parameter locus. This checks the precise scope
needed by the generic-type lemma.

## Normalizer and support reduction

The normalizer of H in Gbar semidirect C3 maps into the finite direct
product Aut(H) times C3, with kernel C_Gbar(H). Cyclic stability of the
generic conjugacy type gives surjectivity onto C3. A Sylow-three subgroup
of the finite image supplies an automorphism phi of three-power order
induced by an element g tau, preserving the determinant character.
The finite-group lemma then gives a two-primary element whose ambient
conjugacy class is tau-stable.

Scalar-torus power splitting gives a genuine finite two-power lift;
division by three modulo that order equalizes all three spectra. The
determinant of the common factor has order exactly M. The full P-F30
support theorem, product-torus margins and chain incidence independence
then place every point of the dense open locus on the chain. Closedness
extends this to the whole subvariety.

The exceptional-class corollary repeats the already checked equivariant
G0 dimension induction on the open finite-stabilizer locus. It makes no
coarse smoothness assertion for nontrivial finite stabilizers. Supports of
the triple terms remain in closures with no higher collision points, so
the integral no-collision argument is unchanged. The surviving stabilizer
exception is positive dimensional; K029's actual collision closures
remain. No all-n exact dyadic pole is claimed.
