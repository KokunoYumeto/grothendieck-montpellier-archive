# Independent whole-proof review of AM-DO-033

Reviewer: GPT-6 Astra Pro, /root/lift_accounting, ALP_MACHINE.
Reviewed file: definite_oscillator_steinberg_first_input.md, DO33.1–20.
Result: PASS in the stated old-host, auxiliary-first-input scope.

I read the complete file, not only the statement or summary. I independently checked the source action, finite metric, compact extraction, exact valuation factors, and the finite diagnostic. The conclusion is an actual nonzero selected first lift with a genuine initial generic-unipotent input at G. It does not identify the raw PhiG array or the later integral image lattice.

## Checks

The finite Steinberg vector is correctly normalized in the flag metric. Applying its generic character sum to the alternating Weyl vector kills each nonlongest cell because the stabilizer contains a simple root with nontrivial character. The remaining cell has exactly |U| distinct flags. Thus the generic vector norm is |U|, and its normalized matrix coefficient has denominators only powers of q. This statement does not treat the classical ue basis as orthogonal.

The actual split source action is the genuine left action
\[
 \omega(g)f(X)=\eta(\det g)^{-1}|\det g|^{b/2}f(Xg).
\]
The free residue orbit X0 GL_a is preserved by the integral source compact. The determinant correction eta(det t) in DO33.6 cancels the oscillator factor exactly, giving the claimed Steinberg action on v'. The orbit is free, so no stabilizer consistency condition is missing.

With each residue cell of measure q^{-ab}, finite Schur orthogonality gives
\[
 \|\mathcal E(v')\|^2=q^{-ab}|GL_a(\mathbf F_q)|\,\|v'\|^2/d_\tau.
\]
The displayed raw norm, the product Gamma_G, and its expanded q-power are correct. The raw vector has value1 at X0. The normalized finite Fourier transform uses q^{-ab}; its phases are roots of unity and q is an11-unit. All coefficients are11-integral, and Fourier inversion at X0 forces their minimum valuation to be0. This is stronger than merely asserting a nonzero complex auxiliary vector, but it still concerns that raw auxiliary Schwartz vector.

The DO030 step is used in its correct form: the fixed auxiliary Fourier operator is applied to the actual permitted29 half-orbit, and simultaneous jets detect one nonzero selected value. The explicit level threshold retains the number s_G of nonzero Fourier coefficients. It does not identify a predetermined raw auxiliary test. The finite G compact acts in a pure Steinberg type, and the29 action commutes with it.

The source class-supported function is well-defined because the principal29 level gives a trivial rational stabilizer at that class. Retaining the full compacts at G is legitimate when the function is allowed to vary by their matrix coefficient; no principal-G index is needed. The two compact orthogonality factors are exactly d_rho^{-1} and d_G^{-1}, and the supporting class has volume I_a(M)^{-1}. This proves both the nonzero extracted value and the source norm in DO33.17. The literal bilinear theta integral uses the conjugated compact coefficient as its automorphic input; consequently its right unipotent type is psi_U^{-1}, as required by RecLevel.lean50–52.

The passage to an actual irreducible automorphic constituent does not discard the finite Steinberg hypothesis. Projection commutes with the compact action, and its restriction to a nonzero irreducible compact copy is injective. Since finite Steinberg has a Borel-fixed line, the resulting local constituent has an Iwahori-fixed vector. This is the precise initial input needed in LIFT19, not an assertion of sphericality.

The normalization accounting retains every displayed factor:
\[
 \Theta_{\rm unit}(1)
 =\frac{C^{2ab}a_\lambda}
          {\sqrt{\Gamma_G}\sqrt{I_a(M)d_\rho d_G}},
\qquad
 v_{11}(d_G)=0.
\]
The11-valuation of Gamma_G is the sum of v11(q_v^i-1). It need not vanish; the example q113,a6 has a nonzero value. The finite-input square-root normalization is therefore not silently called an11-unit. The real polynomial/Gaussian norm remains the separate R011 factor. No local content conclusion for the entire automorphic image follows from these scalar formulas.

## Primary/source reading

I directly read Steinberg(1957), Theorems1–2 and the basis corollary, pp.348–350, in the publisher PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1A82E966D7A0832A4FD80689E5F67CAE/S0008414X00044709a.pdf/prime-power-representations-of-finite-linear-groups-ii.pdf.

I directly read Geck(2015), Theorem2.1 and Corollary2.3, pp.3–5:
https://arxiv.org/pdf/1504.04157.

I read the exact inverse source type in the pinned
Formalism/LocalToGlobal/Columns/RecLevel.lean50–52 and the initial HX/SX/lamX declaration in GenericUnipotentCharacter.lean437–452. The finite-family and simultaneous-jet comparison are the accepted DO029/030 inputs; they were not replaced by an unrestricted interpolation assertion.

## Executed finite diagnostic

I reran definite_oscillator_steinberg_certificate.py. It returned PASS for GL2(F3), b3, with nontrivial determinant splitting:
group order48, Steinberg dimension3, generic norm squared3, raw Schwartz norm squared16/729, Fourier quotient729, nonzero coefficients378, full-rank value1, and all group covariance identities verified.
The same run reported v11(|GL6(F113)|)=1 and the corresponding281/337 values0.

This is an independent whole-proof review and a replayed finite normalization diagnostic. It is not a formal proof assistant check.

