# Independent complete review of MA-MO-031

Reviewer: GPT-6 Astra Pro, effort inherited/not externally exposed, MAS_ARTIN /root/s5_audit. Date: 2026-11-21 UTC.

## Outcome

PASS on the final 549-line module `reciprocal_growth_criterion.tex`, SHA25668882f373035f820459719ff216d93c6de3edc16c9eb7238cb9226c89c74e8d2. I read the entire original547-line written proof in four untruncated calls, independently checked every proof step, and then read the complete endpoint-normalization delta and affected conclusion. The author applied that requested clarification: throughout the section, a step equals1 far left and0 far right. This fixes the exact RS56 trace normalization without changing any formula or the main perturbation class.

## Checks actually performed

The actual compact-frequency core and both bounded-output compositions are defined before any extension claim. On that core jv is compact smooth, T_phi preserves Schwartz space, and multiplication by mA remains valid. The distinction between this actual difference and a sequential commutator whose intermediate inverse domain may fail is maintained.

For polynomial j, differentiating Aj=1 gives polynomial bounds for all derivatives. The divided-difference kernel then is Schwartz in the invertible coordinates(t,t−u). The Hermite expansion gives an absolutely summable rank-one representation and a continuous Schwartz-kernel-to-S1 estimate. The finite frequency cutoffs converge in Schwartz topology, hence trace norm. The normalized endpoint convention is necessary for the exact stated scalar trace and is now explicit.

For a fixed possibly complex nonzero g, q and w are fixed independently of the cutoff, with conjugation chosen so overline(mA)w=q. I recomputed the actual adjoint pairing with the inner product linear in its first entry. A bounded extension forces the smooth representing function H_phi to lie in L2 by Riesz representation on all compact smooth tests; this yields exactly jT_phi q in L2.

The Gevrey base step has an L2 inverse-domain vector because the off-support Fourier transform decays stretched exponentially, beating the generic reciprocal's exp(C log²) bound. Universal real perturbation domains imply domains for every real test by subtraction and scaling, and only then extend complex linearly. The explicit Baire/Fatou argument yields a finite derivative seminorm estimate. Since f is a nonzero entire Fourier transform, a compact subinterval without zeros exists; modulation of b/f gives the uniform polynomial local L2 reciprocal bound. The generic polynomial logarithmic derivative converts this to pointwise polynomial growth on the specified shrinking intervals. This use of genericity is explicit and essential.

If polynomial growth fails, the real bounded-norm sets are closed and have empty interior; their complement is a dense G_delta. The bad cutoff remains real and lies inside the original range-preserving perturbation neighborhood. The constructed v_R=eta_R H_phi/||eta_R H_phi|| is an actual normalized compact smooth vector, and its fixed output pairing diverges. The non-L2 character of H_phi gives divergence without needing monotonicity of eta_R.

For each core input, the literal two-composition finite-frequency operator equals chi_N K_circle(v) eventually, so it converges on that core. Uniform operator bounds would give a bounded extension of K_circle, contradicting the explicit vectors. Banach–Steinhaus excludes a bounded strong limit. The scalar traces still converge using only the separately checked logarithmic derivative bound, so no unjustified inference from trace convergence is made.

The conditional zero configuration is correctly separated from an arithmetic occurrence claim. Dividing by the full zero factor on a fixed pole-free disk and applying the maximum principle gives exactly the exponent m_n and reciprocal lower bound. Finite Euler factors are bounded above and away from zero on the fixed positive line. The stated growth condition forces nonpolynomial reciprocal growth but is not established by generic zero avoidance alone.

## Source and scope

I freshly reread the exact RS64 bound and its nearby disk-factor derivation in `regularized_frequency.tex`; that module was previously authored and fully checked in this run. The supplied MT-M18 source input was not freshly reread for this event and is not recorded as such. The full MO031 new proof uses no new external theorem beyond the explicitly proved functional-analytic steps and already checked analytic estimates.

The equivalence is for the stated universal neighborhood of normalized real cutoffs on the unrestricted one-sided fixed core. It does not decide a prescribed individual cutoff, assert actual failure of polynomial reciprocal growth, or transfer the countervectors into the completed theta ideal. The unconditional ideal return MO028 and the different full-source edge hypotheses remain compatible. No broader conclusion was accepted.

At23:11UTC I read the entire subsequently added A-scope paragraph and the revised remaining-gate sentence. I freshly reread the RS004 fixed-gap reciprocal proof throughRS36: A gives the fixed gap sigma−1/2, its finite Blaschke factors have a fixed positive lower bound, and their O(logT) number gives polynomial reciprocal growth. The positive conclusions are therefore established under stipulated A; the remaining analytic condition is undecided only without that input. This small delta passes. Final561-line hash26466188b4ef986c93327a3d0413e526884699e273ad99f4eb3434f2b1ec60cb.
