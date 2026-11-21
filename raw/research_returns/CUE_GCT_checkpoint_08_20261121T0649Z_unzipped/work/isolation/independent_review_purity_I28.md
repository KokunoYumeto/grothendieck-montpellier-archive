# Independent whole-proof review: I-28

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:31:13Z.

Scope: complete reading of `I28_endpoint_geometry.tex`, together with the local-rank-test definitions and rank-two/rank-one stages in `I21_width3.tex`. This is a targeted independent agent proof reading and elementary rederivation, not a formal certificate or external peer review.

## Verdict: PASS

After normalizing the internal constants to identities, every internal invertible parameter domain contains zero. The nonzero decomposable left endpoint likewise gives an initial projective point and a curve closure containing that point. The successive projective image closures are irreducible closed subvarieties of the Grassmannian and form a nested chain. Each strict inclusion increases dimension. Keeping exactly the strict-growth parameter positions and setting the others to zero preserves the final image closure: at a retained stage, a dense previous image still has dense image under the regular family of invertible actions; at a nonretained stage, the identity at zero preserves the already equal closure. Nonzero endpoint values and invertible internal matrices ensure this reasoning does not lose the affine scalar vector through a zero representative.

The right endpoint constant supplies a nonzero linear functional. If it does not kill the final image, fixing the right variable at zero gives a nonzero restriction. If it does kill the image, that image lies in a proper hyperplane section of the Grassmannian, because coordinate decomposable wedges span the full exterior space. Its dimension is therefore at most `r(w-r)-1`. Nonvanishing of the original contraction ensures that some value of the right parameter gives a functional not vanishing on this same image; retaining that parameter consumes the one saved position. Only left decomposability is used, as stated.

The SV conclusion follows directly from the existence of a nonzero restriction on at most `r(w-r)` coordinate positions. It does not require a statement about the support of every lowest homogeneous monomial. Over a finite field the proof works after an extension supplying distinct interpolation nodes; polynomial nonvanishing and zero restrictions are unchanged by that extension.

For the width-three rank-two local tests of I-21, a chosen nonzero second-compound contraction has nonzero endpoint polynomial vectors. Each is univariate in its own endpoint variable, so its value at the common transcendental center is nonzero. A row of a second compound is decomposable; the right column need only be nonzero. Every internal rank-three factor remains invertible at that center. The proposition thus applies with `r=2,w=3`, including both endpoints, and two fresh SV pairs detect every selected test. Finitely many nonzero test polynomials have a nonzero product, while earlier rank-three minors survive by setting new amplitudes to zero. The already proved rank-one stage still uses six further pairs. Hence the eight-pair sampler and the stated interpolation cardinality follow with no new singular-profile assertion.

The earlier ten-pair theorem and its consequences remain correct; the new result only improves their parameter count. No claim of a polynomial dependence on growing width is made.
