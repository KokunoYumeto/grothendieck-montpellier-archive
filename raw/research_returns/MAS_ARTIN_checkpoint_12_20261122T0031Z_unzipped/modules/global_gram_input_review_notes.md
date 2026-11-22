# Independent review of the actual finite Gram transport

Reviewer: GPT-6 Astra Pro, MAS_ARTIN /root/input_audit. Date: 21 November 2026. All five complete GP004–008 arguments in global_gram.tex were read, together with the complete GP001–003 prerequisite module. The proofs pass. Seven accurately scoped events are saved in global_gram_input_review_events.tsv.

## The two Gram operators have distinct norms

The half-line ratio R=w/w_+ lies between1 and exp(4alpha max(-c,0)), independently of the polynomial weight. Thus i*Ri has a bounded inverse, and i(i*Ri)^(-1)i*R is exactly the orthogonal projection for the global weighted norm. The ordinary Hardy projector has a different orthogonality relation. The proof that the two differ is sound: equality would make the model-space complement reduce R, its spectral interval projections would localize a reproducing-kernel exponential to every subinterval of(0,-c), and density would force a positive delay, contrary to the independently checked finite theta range.

The direct frequency parametrization uses an auxiliary ordinary even-L2 band norm. Its closed theta map can be unbounded without contradicting the first bounded Gram inverse. The cosine-packet lower bound is specific to that auxiliary norm. The module keeps this distinction explicit.

## Exact finite kernel and domains

For T u(t)=2 t^(-1/2) sum_n u(n/t), the pairing with T v gives measure4 dt/t². Substitution y=m/t and the even source norm2 integral_0^Lambda produce exactly the coefficient2/m in GP.66. Convolution contributes r^(1/2). Substitution z=nry/m gives the kernel2 chi(m/y) w(log(m/y)) h(mz/(ny))/sqrt(mnyz). Nonzero terms satisfy m<=Lambda b and n<=Lambda b/r_-, while y>=1/b and z>=r_-/b. The latter bounds justify smooth cutoffs before treating the compact square; the possible weight cusp is only a bounded multiplication factor. Hence the bounded trace-class extension of the core form is established before cyclic traces are used.

The graph-core argument is sufficient to place A Tbar u in Dom(Tbar*) and identify Tbar* A Tbar u=K u on Dom(Tbar). Spectral calculus puts the entire source in the domain of Tbar(G+epsilon)^(-1/2), so no unverified adjoint product is needed in the principal factorization. Compact-output convergence extends the finite Poisson expression to graph-domain vectors. Finite Mobius inversion then proves injectivity, with countably many dilation null sets handled correctly.

## Trace transport and its limits

F_epsilon=Tbar(G+epsilon)^(-1/2) is a contraction and converges with its adjoint to the actual polar isometry V. For fixed trace-class A, finite-rank approximation proves both A F_epsilon F_epsilon* -> A Q_Lambda and F_epsilon* A F_epsilon -> V* A V in trace norm. Cross-space cyclicity therefore gives an actual finite-level trace transport, rather than a numerical match of eigenvalue sums. The exact comparison with the additive-band candidate retains both Gram resolvents. The fixed-data Fredholm determinant identity follows from finite-rank Sylvester identities and trace-norm continuity.

The zero intersection with the same-coordinate additive-band range is also correct: the actual finite theta range vanishes below1/Lambda, whereas an additive finite-band representative is entire. The positive radial weight factor preserves vanishing on this interval. This rules out only the displayed same-coordinate candidate. It does not exclude the nonlocal transport just constructed, prove a nonzero trace difference for every test, or supply an asymptotic geometric remainder estimate.

No new zero-location hypothesis is used. The remaining assertions are properly limited: no LF continuity of Gram resolvents, no common nuclear LF presentation, no representation intertwining and no expanding-cutoff determinant limit are claimed.

## Source scope

The review freshly read the supplied text of Masullo Definitions7.3.2.1 and7.3.2.3, the adjoining support discussion, and Definitions11.2.1.1 and11.2.1.3. Their rational one-place specialization gives the stated Fourier-band range and its orthogonal closure. This review did not newly render those pages and does not certify the source's unrepaired global nuclear lift. The existing complete GP003 proof supplies the precise shifted Hardy range; its Laplace normalization was checked directly from its reproducing kernel and agrees with GP.45.
