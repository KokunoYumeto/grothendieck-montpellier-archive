# Uniform characterization of all compact-test returns

MA-PR-009 is a sharp functional-analytic characterization, conditional on the exact arithmetic cost estimates. It does not establish those estimates or exhibit their failure.

For each compact support K, the eligible test space, optionally with g(0)=0, is a closed Fréchet subspace of D_K. Every attained block cost c_n is a continuous seminorm there, with continuity following from the fixed finite selector and the compact-support Mellin bound. If every test admits a return, PR006 gives pointwise finiteness of every Q_k = sup_n nu_n^k c_n. The complete-metric/Baire argument upgrades this to one finite derivative seminorm estimate for each fixed pair (K,k).

The converse is stronger than a separate selection for each test. Let X_n be the finite space of module maps B_n to J_n, with the actual norm ||L R_n|| on the whole Hilbert quotient. Let Y_n be the image of L -> pi_n L, with its exact attained quotient norm. This norm is c_n on the test multiplier datum. Its dimension is the sum over the block of max(0, 2r-m), at most d_n = O(log nu_n).

An Auerbach basis of Y_n and attained norm-one lifts give a fixed complex-linear section of norm at most dim Y_n. This is a section in the space of feasible homomorphism data, not a module section of J_n -> B_n. The logarithmic loss is absorbed by the rapid estimates. The resulting actual E-valued return family is jointly continuous on each fixed-support Fréchet space times Q_H, and a bounded test family has one bounded target disk and coefficients in every l^p.

The sections are chosen once for the width, so the assignment is coherent across supports. No additional inherited-LF-topology claim is needed.

If one fixed (K,k) admits no finite derivative estimate, every closed set {Q_k <= M} has empty interior. The same complete-metric argument proves that {Q_k = infinity} is dense G_delta. Each member lacks a return by PR006. The premise is not asserted for an arithmetic function, and no arithmetic close-pair configuration is invented.

The entire written proof was read after creation in two untruncated chunks. The review checked the precise closed Fréchet space, continuity and subadditivity of the minimum costs, the Baire neighborhood scaling, the actual finite quotient norm, exact image dimension, norm-one lifts, logarithmic section loss, coherent actual operator construction, bounded-family nuclear rescaling, and the residual failure argument. Author QA passed, and /root/pf26_audit subsequently passed a complete independent proof reading. Subsequent edits only split wide displays and clarified that the coherent assignment covers all eligible compact tests in the chosen class, preserving the optional g(0)=0 restriction.

Inputs are the already fully read PR006–008 proof and M18's adapted topology, entire-lift bound and Auerbach construction. The Baire and finite linear-section arguments are proved in the new module. Grothendieck placement remains the finite-length C[w] category, and the vector-space section does not split its truncated local extension. No new arithmetic positivity, zero-location conclusion, A, M, generic-edge assumption or outside preprint is used.
