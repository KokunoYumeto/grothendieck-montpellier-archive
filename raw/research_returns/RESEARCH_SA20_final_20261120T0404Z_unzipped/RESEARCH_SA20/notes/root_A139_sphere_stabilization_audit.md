# Root audit of A.139

We read the complete numbered candidate in
`agents/singularities_duality/logs/A139_TOP_sphere_stabilization_draft.tex`.
The audit outcome is **PASS under the stated hypotheses**. We also read the
independent audit and checked the exact zero-section-fixing germ convention.

## Scope and actual map

For every integer n at least two the ordinary bottom-fixed, free-top TOP
concordance space of the standard sphere is the based homotopy fibre of the
actual product-with-a-line map from Y_n to Y_(n+1), where Y_n is the fibre of
BO(n) to BHomeo(R^n;0). We checked the entire model, including components.
This is a sphere calculation, not a calculation for arbitrary bases of
dimensions three and four.

The globalization input is the original Kuiper–Lashof I Lemma 3, printed
page 11 and proof pages 12–13, including the relative extension paragraph.
Root opened and read that original in the preceding source audit. The
published Salvatore–Turchin Section 3.4, equations (3.5)–(3.7), was also
opened: its common-neighborhood finite-parameter germs agree with the
specified convention. No excluded four-dimensional smooth delooping theorem
is being used.

We checked the following steps.

1. Global origin-fixing homeomorphisms map degreewise surjectively to
   zero-section-fixing germs. A kernel simplex has one common identity
   neighborhood. Sphere inversion converts it into a compactly supported
   family fixing the origin, and the Alexander contraction works with one
   common support and with the inverse family. This proves the weak
   equivalence on every component.
2. The point stabilizer of the sphere has the same germ group. Its kernel
   becomes compactly supported homeomorphisms without an extra fixed-point
   condition. The contraction remains valid.
3. The disk-to-germ Kan lifting argument is exactly the dimension-independent
   finite-mesh extension argument already audited in A.132. Its identity
   fibre is the filtered common-inner-ball model of the ordinary free-top
   sphere concordance space. The boundary restriction, its cone section,
   and relative Alexander kernel give the intermediate fibre of the radial
   cone homomorphism. No unproved restriction to identity components occurs.
4. Quotienting source and target by the common orthogonal group preserves
   the based fibre. The point-stabilizer quotient is the same sphere quotient:
   right cosets have representatives fixing the chosen point, with ambiguity
   exactly its orthogonal stabilizer. Local choices of rotations give the
   required continuity. Homotopy-orbit conventions give the same fibre
   statement.
5. The translations tau_(-sp) c(h) tau_(sp) are genuine origin-fixing group
   homomorphisms because c(h) fixes the ray through p. They fix the embedded
   O(n) exactly. The chart psi(u,t)=(1+t)(u,sqrt(1-|u|^2))-p has derivative
   identity, commutes with O(n), and conjugates the endpoint germ into the
   point germ of h times the identity line. The dilation path of this chart
   is a common-neighborhood path of local diffeomorphisms and their inverses.
   Thus the map is actual stabilization up to a specified based homotopy,
   rather than an unidentified arrow between equivalent spaces.

## Low-degree consequence and boundary

The corrected GGHKP Theorem 1.3 gives the five-connected stabilization of
Y_4. The opened Kirby–Siebenmann finite-rank TOP_5/PL_5 calculation and the
previously audited PL_5/O_5 vanishing identify the target stabilization in
degrees at most four. The fibre sequence therefore yields vanishing only
through degree three for P_TOP(S4). The parallel PL result uses A.128.
We explicitly checked that no vanishing of pi_4 is inferred without control
of the degree-five stabilization map.

This theorem does not on its own close an original task row. Its sphere
specialization is not assigned independent qualifying progress credit.
