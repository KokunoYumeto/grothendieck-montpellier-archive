# Independent targeted review of the root T4 proof

Reviewer: /root/h9_height, GPT-6 Astra Pro, effort not exposed.
Run JAC1964-20261121, 2026-11-21. Source reviewed: entire
`work/root/T4_proof.tex` as present before addition of the announced
incidence-detection lemma.

## Recomputed items

* The Abel inverse can be written explicitly as
  `(b-1)! (L_theta^(b-1))^{-1} (a x 1)_*` on the mixed class. The
  projection formula and `a_*[C]=theta^(b-1)/(b-1)!` show its pullback
  recovers the original class.
* Product dimension is `b+2m-1`; primitive power is `b`; quadratic
  Lefschetz power is `b-1`. All terms containing h vanish because the
  A-component is primitive. Factor `(b-1)!` is positive.
* For the elliptic normalized incidence divisor
  `P=Delta-E x 0-0 x E`, write its mixed class as
  `-a_1 b_2+b_1 a_2`. Graded multiplication gives
  `pr_12*(P_13 P_23)=P_12`, and the diagonal degree is `-2`.
  Thus the stated incidence-to-polarization sign `(-1)^m` passes
  independently of a memorized Hodge-sign convention.
* The diagonal of the rigidified biextension class of L is `2 c1(L)`;
  the factor 1/2 in the rational divisor class is correct, including in
  characteristic 2 with rational coefficients.
* Curve pullback/projection gives the claimed degree formula. Nef plus
  nondegenerate implies ample on an abelian variety. The given index
  argument is consistent, conditional on its cited index theorem.

## Missing part found

The fragment referred to an incidence-detection lemma 'proved below', but
it was not included in the file at review time. The following proof was
sent to root, who owns the completed insertion:

Parameterize an algebraically trivial cycle by a pointed smooth projective
curve T. Apply the correspondence whose degree `2m-1` cohomological action
is zero, then any divisor-valued incidence test with smooth projective
parameter S. The resulting divisor on T x S has zero mixed H1 x H1
cohomological component. Hence its associated homomorphism
Alb(T) -> Pic^0(S)_red has zero Tate-module realization and is zero, by
faithfulness of Tate realizations on homomorphisms of abelian varieties.
Every incidence test vanishes, so the cycle lies in the incidence kernel.
This proves the correspondence acts by zero on Saito's incidence quotient.

## Scope of the check

This is a targeted whole-proof reading plus independent recomputation of
the transfer and sign. It is not a formal certificate, and it is not an
independent reconstruction of Saito's underlying existence/duality
theorems. Those remain cited source inputs. The proof passes once the
announced incidence-detection argument is supplied and its use of Saito's
incidence quotient is kept distinct from a universal regular algebraic
representative.
