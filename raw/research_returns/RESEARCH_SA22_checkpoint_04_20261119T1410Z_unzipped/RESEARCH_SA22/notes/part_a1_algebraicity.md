# Algebraicity obstruction for the natural four-pointed cut component

## Proved statement

With four individual labels and one essential unoriented cut isotopy class
(represented geodesically), a connected cut-moduli component is

    H / <tau -> tau+2> = punctured unit disc.

The complex structure here is specified: forgetting the discrete cut class
is locally biholomorphic over M_0,4. This component cannot be the
analytification of any smooth connected finite-type complex algebraic curve.

## Derivation

The sphere's double cover branched at its four labels is an elliptic curve;
choose one ramification point as origin. The remaining points are its
nonzero two-torsion. Conversely quotient by minus one recovers the sphere.
Marked periods give tau in H. Holomorphicity follows locally from the
Legendre family and holomorphic dependence of its marked periods.

Farb--Margalit Propositions2.6--2.7 prove the lift of sphere mapping classes
and the correspondence of primitive torus slopes with essential sphere
curves. Fixing labels removes the two-torsion translations and restricts
the matrix to Gamma(2)/{+I,-I}. A fixed curve's primitive slope may be
chosen (1,0). Its stabilizer is exactly the matrices +/-[[1,2m],[0,1]],
so the quotient is H/<tau+2>. The exponential exp(pi*i*tau) gives the
punctured disc. The downstairs Dehn twist lifts to two twists around
parallel primitive torus curves, confirming the generator's factor two.

If this were an algebraic curve X, compactify smoothly. Let g be the genus
and r>=1 the number of points at infinity. Its fundamental group is free
of rank 2g+r-1. Being Z forces g=0,r=2, hence X=C*. This is impossible
because C* has universal cover C, while the punctured disc has cover H.
Liouville excludes a biholomorphism C->H.

The fixed labelled nodal target stratum has no component moduli and no
automorphisms, so its unrestricted nonzero tensor is C*. This proves the
category limitation independently of cap radii. It does not assert the
actual surgery formula is nonholomorphic merely because it is realanalytic.

## Opened original sources and exact locators

- Farb and Margalit, A Primer on Mapping Class Groups, full authored PDF:
  https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf
  Web ref turn633142309view0, targeted refs turn768119679view0/1.
  Printed pp55--57, Propositions2.6--2.7; source PDF zero-based pages71--73.
  Local sources/farb_margalit_2012.pdf/.txt also independently read.
- Hubbard and Koch, An Analytic Construction of the Deligne--Mumford
  Compactification, full author preprint:
  https://arxiv.org/pdf/1301.0062
  Web ref turn633142309view1; targeted refs turn768119679view2/3.
  Example2.3 p12 gives the marked torus period; Example7.2 pp25--26
  computes the parabolic cyclic quotient explicitly.
  Local sources/hubbard_koch.pdf/.txt independently read.

Both sources already have opened entries in the main source bib files,
keys FarbMargalit2012A567 and AHubbardKoch2014; no duplicate keys added.

## Related independent audits during this work

- B2: moving-pair Mumford two-form lemma and E*E generic counterexample
  checked directly against Mumford1969 pp197--203. An explicit scheme
  W_{n,e,d} over Qbar strengthens the descent argument; the B agent is
  incorporating it. Bloch's opened publisher excerpt pp3--4,9--11 contains
  all Abel--Jacobi, Albanese, and kernel facts actually used, so no full-book
  source gate remains for that proof.
- A2 arbitrary-collar proof: shape derivative k'=a-a'', residual bound
  ||R_n||2=O(sqrt(n)), integral23/4, doubled Bochner sign, H2->C0 correction,
  and order of quantifiers n fixed before epsilon checked independently.
  The negative and positive pointwise values both follow rigorously.
