# Nori's integral pullback and the fixed geometric transporter

19 November 2026. This is an exact source and morphism audit for the unrestricted E.2 gate. No enlargement of the proved integral comparison scope is asserted.

## N1. Opened primary statements and their domains

Ruimy–Tubach, *Nori motives (and mixed Hodge modules) with integral coefficients*, accepted author version arXiv:2407.01462v3, 24 April 2026, has 72 pages. Section 4.1, printed p.39, fixes an algebraically closed subfield k of C. Proposition 4.1.3, p.40, identifies DN(-,Z) with the pullback of DN(-,Q) and the integral analytic geometric category over its rational counterpart. Proposition 4.1.5, p.41, gives the corresponding pullback of hearts. At a point the analytic finite objects are finitely generated abelian groups; the tensor unit and its finite sums and cofibres supply these objects. The displayed square was visually checked on the original p.40.

The same paper's Theorem 2.1.2, p.16, identifies torsion Nori motives over any subfield k of C with finitely generated torsion continuous Galois representations, through the actual Artin functor (2.1.A). Theorem 2.2.2, p.17, constructs the realization from etale motives and its compatibility with Betti and change of field. The algebraically closed hypothesis of the pullback is not removed by citing the separate existence of Betti realization over a general field.

Primary file: `work/sources_generation/ruimy_tubach_integral_nori2026v3.pdf`.
URL: https://arxiv.org/pdf/2407.01462v3 .
SHA256: bba9793a40e9df7192babfa79904647d591e3b2ee49991567a885ca14239562c.

## N2. The rational pure functor is explicit

Arapura's original author version arXiv:0801.0261v4, Theorem 6.4.1, printed pp.60–61, constructs the equivalence from motivated pure motives to pure rational Nori motives. Its construction sends each h_A^i(X) to the actual h_N^i(X), sends motivated correspondences by their realization, and commutes with Betti. The proof first treats algebraic cycles, the Lefschetz star, cup product and pushforward, then passes to projectors and Tate inverses. I read the complete theorem and proof in the original author PDF.

The authors' corrected Huber–Muller-Stach book, Theorem 10.2.7, printed pp.247–248, gives the faithful functors

    homological Grothendieck motives -> motivated motives -> pure rational Nori motives,

with the second an equivalence. The annotated proof and its adjacent errata were read. The correction to Proposition 10.2.1 uses degreewise cohomology diagrams, not an assumed algebraic total-cohomology Kunneth projector. The correction to Corollary 10.2.6 uses a kernel modulo an image. These corrections are retained when using the pure comparison. In tensor formulas, the cohomological degree and its Koszul commutativity signs are kept explicitly.

Thus the rational pure objects and their Betti functors have actual comparison maps. An equivalence with arbitrary absolute-Hodge morphisms is not being used. On the abelian subcategory the earlier motivated/absolute-Hodge identifications remain the ones already proved in the report.

Primary files:

* `work/sources_generation/arapura_motivic_sheaves2012v4.pdf`, https://arxiv.org/pdf/0801.0261v4 . SHA256 d42ba869387377a31ad6599d9a2d54a4156d497de018cd69b7c18baf7d5c4323.
* `work/sources_generation/huber_mueller_stach_periods_annotated2025.pdf`, author-annotated version 1 July 2025, https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch-errata.pdf . SHA256 6d08014f21a616abb4ba7e177effad4d15e4a215b0f234ce3a4605c20a02b731.

## N3. The pullback on finite free objects and on morphisms

Fix a small rational tensor subcategory C on which the preceding rational functor is defined. A finite free object of its integral Betti pullback for an embedding v is a triple

    (M, L, iota),  M in C,  L finite free over Z,
    iota: L tensor Q -> B_v(M) an isomorphism.

A morphism to (M',L',iota') is a pair (f,q), where f is a rational motivic morphism M->M', q:L->L' is integral, and

    B_v(f) iota = iota' (q tensor Q).

For an actual geometric integral object N, its triple uses the actual Betti lattice Lambda_v(N) and the canonical rational comparison iota_v. This is the image of that object under the two functors in the pullback square. It is not a lattice selected after a rational comparison has been chosen.

Let t:B_v|_C -> B_w|_C be a specified rational tensor comparison. There is an exact map of pullback categories

    F_t(M,L,iota) = (M,L,t_M iota),   F_t(f,q)=(f,q).

The naturality equation for t proves that (f,q) remains a morphism: B_w(f)t_M iota = t_M' B_v(f)iota = t_M' iota' q_Q. The inverse is F_(t^-1); its tensor constraint follows from that of t. This is the precise functor supplied by rational transport plus lattice gluing.

For the original geometric object N, the embedded target lattice of F_t(N) is t_M(Lambda_v(N)). An isomorphism from F_t(N) to the original w-geometric triple with rational component id_M must have integral component

    q_Q = iota_w^-1 t_M iota_v.

It exists, with integral inverse, exactly when

    t_M(Lambda_v(N)) = Lambda_w(N).                         (N.1)

Consequently gluing constructs a lattice object for every rational comparison, while the fixed-object transporter still requires (N.1) for every original geometric object. The obstruction is exhibited by this equation in the pullback, not by an asserted separation of mathematical frameworks.

For a field automorphism sigma and conjugate geometric objects, replace the common abstract M by the actual base-change functor sigma^*M on the target. The same proof gives t_M Lambda_v(M)=Lambda_v(sigma^*M). This is the conjugate-target equation used in E.2.15–26.

## N4. A concrete CM comparison whose transported lattice is different

Let E/Qbar be y^2=x^3-x. Its homology lattice is a free rank-one Z[i]-module: it is torsion-free rank one over Z[i], and Z[i] is a principal ideal domain. Choose a generator, so Lambda=Z[i] in H_1(E,Q)=Q(i). The rational CM torus acts on the tensor category generated by H_1(E); multiplication by

    u=(3+4i)/5

has norm one and fixes the polarization's Tate multiplier. In the integral basis (1,i) its matrix is

       ( 3/5  -4/5 )
       ( 4/5   3/5 ),

with determinant one. Its rational inverse is multiplication by the conjugate u-bar. The vector u*1 is not in Z[i], so u Lambda != Lambda.

The pullback constructs the object (M,Lambda,u iota). The prescribed rational component id_M cannot identify it with (M,Lambda,iota) through an integral lattice isomorphism, because that component would require the displayed nonintegral matrix. An isomorphism with a different rational component changes the prescribed rational comparison and therefore does not lift u. This example is on the explicitly specified CM tensor subcategory; no extension of u to every mixed or pure motive is asserted.

## N5. Artin and finite-coefficient compatibility

For a genuine integral comparison on a fixed Nori object N, naturality with N -> N/n requires its reduction modulo n to be the same comparison on N/n. Theorem 2.1.2 identifies this torsion object and all its maps with the actual finite Galois representation. After the Artin restriction sigma is fixed, the required finite matrix is therefore the actual etale sigma-transport under the Betti/etale comparison. Arbitrarily changing the lattice in N3 does not verify this fixed-object equation; it changes the integral object being compared.

Over algebraically closed k, this also gives an elementary check on the full integral Nori category. Every torsion object is a constant finite abelian group. A tensor automorphism of Betti fixes the unit, its quotients Z/n, and every map Z/n -> T to every torsion object T. Since these maps realize all elements of T, it fixes T pointwise. For a finite free N, naturality with N -> N/n then gives T_N congruent to the identity modulo n for every n; hence T_N is the identity over Z. The same argument, after removing the torsion part, treats every finitely generated realization. This is a statement about the full category with its displayed quotient objects and all their morphisms.

The earlier pure integral diagram has its own specified geometric lattices and morphisms. Restriction from the full integral Nori realization to any such mapped diagram is an actual map of comparison sets; its surjectivity is a further extension problem. It is not supplied by the rational equivalence in N2 or by the object gluing in N3.

## Outcome

The opened theorems establish the rational pure bridge, the integral pullback, and the finite-coefficient Artin comparison. Their exact composite reduces the attempted gluing construction to (N.1) on the original geometric objects. No new solution of that unrestricted lattice equality or of the full-pure E.2 separation problem has been obtained by this route.
