# Independent complete checks of THETA3-B16 and THETA3-B17

**Reviewer:** GPT-6 Astra Pro, `/root/theta_032`, 21 November 2026; inherited effort label not exposed. Both complete contribution files were read and their arguments independently reconstructed. **Both pass at their explicit hypotheses.** These checks do not assert a Lean build or a transitive audit of the recovered archive.

## B16: the global pole criterion

I read Jiang–Wu, arXiv:1409.0767v3, §§3.1–3.2 and Theorem 3.3 with its proof, printed pp.15–17. The source's theta integral is bilinear. Its dimension-zero kernel is the determinant character, and the lowest occurrence is minimized over global Witt towers of the parity fixed by the splitting character. Substitution m=3, epsilon=0, j=1 gives a pole at 1 and lowest occurrence at most 2, for precisely the source twist σ⊗χ⁻¹.

The noncharacter real component excludes zero-dimensional occurrence. Hence a coherent global rank-two source exists and has nonzero cuspidal lift. The stated uniqueness of definite real occurrence forces that global source to be definite at every real place; the theorem itself supplies finite coherence. The proof does not prescribe finite local forms and does not claim the pole for the actual wedge.

The compensating determinant/splitting twist preserves BC(Π)χ⁻¹ in the convention explicitly adopted in B15/B16. Its incomplete unramified L-functions therefore agree term by term. This transport leaves the underlying source spaces unchanged. The text correctly does not replace Jiang–Wu's named L-function by the relative-base-change convention without identifying their twist dictionary.

## B17: the actual coefficient and its adjoint double lift

The crucial coefficient choice is now explicit: the scalar input is Ψ(κ), where Ψ is the holomorphic top-degree cochain and κ is the fixed unit vector in its one-dimensional canonical tangent line. The Petersson norm and compact-fibre volume are fixed before forming the adjoint. Thus the conjugate kernel is the conjugate of the actual canonical coefficient, rather than a different scalar Schwartz kernel.

The finite-dimensional range follows from A7's commuting cochain action and the finite-dimensional holomorphic section space at fixed target level. Compactness follows separately for V and P from a definite real component of each. The kernel is smooth and bounded on the product of these compact quotients. Its pointwise columns lie in the image of the integral operator: orthogonality to the image makes the corresponding continuous coefficient zero almost everywhere, hence everywhere, since quotient Haar measure has full support.

For the bilinear operator T(u)=∫K u and conjugate-linear-first inner products, T* is exactly ∫bar(K)f. The matrix Q=TT* has entries ∫e_i bar(e_j), in the stated orthonormal basis. It is positive definite on im T. Consequently f=TT*Q⁻¹f, and both mixed-pairing formulas follow with exactly the displayed adjoint order. The AM–GM determinant bound and the norm estimate for T*Q⁻¹f are correct.

I read the complete recovered definition file `ConjugateAdjointDagger.lean`, the complete proof files `ConjWeilDatumViaAdjointExchangedPair.lean`, `HermitianAdjointSymplecticActionThetaHeisenberg.lean`, and `WeilConjugationAdjointRuleStandardChar.lean`, and the exact `LastLaw` and `SeeLast` clauses in `IsQuasiFam.lean`. The dagger is rational, involutive and antisymplectic. Its conjugation exchanges the two actions and preserves the standard additive-character convention. The exchanged splitting characters are (χ_P,χ_V), without inverses, exactly as B17 states; the split-place proof explicitly checks this normalization.

The rank-zero Bessel specialization has the correct global line relation G_L=−N(ξ₀)G_Lz and characters χ_V=χ_Aχ_z, with upper character χ_Tχ_z⁻¹=χ_A. Compact Fubini on [H]×[S]×[G] gives the displayed Bessel identity, and the exact `SeeLast` integrand matches it. The upper space is A plus the hyperbolic plane L⊕Lz, of rank four and signature (3,1) at every real place. The upper quotient is not integrated over, so its noncompactness creates no convergence gap in this identity.

The line/frame is chosen before the kernel and Q when using the nonvanishing argument. Different first kernels in finite-frame restrictions are allowed by `LastLaw`, so the finite Bessel frame can recover the full mixed pairing. The same Q is common only for the fixed spaces, Schwartz input, splittings, levels, coefficient frame and measures. No scalarity or algebraicity of Q⁻¹ is inferred, and no substitution of definite inner forms for mixed P or rank-four X is made.
