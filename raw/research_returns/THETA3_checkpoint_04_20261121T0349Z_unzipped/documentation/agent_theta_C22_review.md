# Independent complete review of THETA3-C22

**Reviewer:** GPT-6 Astra Pro, `/root/theta_032`, 21 November 2026; inherited effort label not exposed. I read the full saved `paper_C22.tex` and independently reconstructed its proof. **PASS at its actual tame reduced-theta normalization.**

The half-period is nontrivial, so its doubled lattice vector has sigma semicharacter -1. The quasiperiod multiplier and oddness of sigma give the displayed evenness identity with the correct sign. The i-stable lattice forces the weight-two coefficient e2* to vanish. Division by the specified tame algebraic sigma value is by a p-adic unit; this is the same torsion normalization already source-checked for C18.

The logarithmic second derivative is exactly -x(T+P(t)), integral on the identity residue disc. C19's invariant D^7 congruence therefore supplies the stated logarithmic-jet divisibility. I independently differentiated Dx=y, Dy=6x²-2 to get D⁴x=120x³-72x and D⁶x=5040x⁴-4032x²+144. Thus l8=-144 is a 7-adic unit. As a separate local check, x(T+z)=-1/wp(z), so the logarithmic second derivative is z²-z⁶/5+..., giving l4=2 and l8=-144 again.

The strict Bell surplus is essential and is valid. For even j=2,4,6 its lower bound is (7j-8)/48>0. For every even j≥10 the bound (41j-384)/336 is positive. Only j=8 has zero surplus. At n=8·7^r, the all-8 partition has multiplicity 7^r, hence shifted valuation 1/6. Every different nonzero Bell term contains another index, has positive total surplus and at least one base-7 digit across its multiplicities. It therefore has strictly larger valuation. The finite sum has a unique lowest term, so cancellation cannot increase its valuation.

Legendre's formula gives v7(n!)=(n-2)/6, since the base-7 digit sum of 8·7^r is two. Combining the coefficient valuation with this factorial gives exactly `(7^r-1)/6`, proving both the sharp asymptotic slope 1/48 and the failure of any larger slope with bounded loss.

I also read and ran the author's exact-rational series script `explore_sigma_derivative.py`. Its independent finite calculations confirm derivative valuations 0, 1 and 8 at n=8, 56 and 392. These calculations corroborate the proof but are not the basis for its assertion at all r.

The final qualification is correct: this tests the specified actual reduced theta section and integral differential. It is not by itself a counterexample to a theorem whose Host, degree, period normalization, tangent frame or jet hypotheses have not all been matched.

## Independent check of the p=5 and tensor-power additions

Read both additions in full. On y²=4x³−4, D⁴x=120x³−48 and l₆=−72 is a 5-adic unit. The strict surplus lower bound (19j−144)/120 is positive for every even j≥8; j=2,4 are positive and j=6 is the unique zero. The unique all-six Bell partition at n=6·5ʳ gives v₅(DⁿF(0))=(5ʳ−1)/4. For every positive d prime to p, Fᵈ has logarithmic derivatives d lⱼ, so all valuations and uniqueness arguments are unchanged. Both additions pass, with their explicit actual-theta normalization and no unmatched archive conclusion.
