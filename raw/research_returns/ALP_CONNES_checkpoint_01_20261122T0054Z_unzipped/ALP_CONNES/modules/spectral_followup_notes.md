# Added moment paper and letter: findings and checks

The literal Q24 source is **Connes--Consani--Moscovici**, *On q-series and the moment problem associated to local factors*, arXiv:2403.01247, `followup_sources/LIT_CC_q_series_moment_problem_local_factors/pqfile1.tex`. The folder name omits the third author; the title and byline were checked in the LaTeX header. L26 is Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022, `followup_sources/LIT_Connes_RH_past_present_letter/rhready.tex`.

## What was already proved in Q24

Literal locators: Proposition `orthopol1` (the separate label `spec` follows its environment), Proposition `momentdet`, Proposition `momentssm` and equation `expth`, Proposition `expth3` and equation `normoments1`, Fact `keyfact`, Corollary `ansq1`, Theorem5.9 `integralitymain`, Proposition `similar`, equations `pmzg2` and `lambertrank1g`, Fact `keyfact2`, Lemmas `usefact2` and `keylem2`, Theorem `eigenthm`, Theorem `qthm`.

The two displayed Facts are observations that are proved later in the paper. They must not be left in the open-conjecture inventory. The determinant and Jacobi/characteristic coefficients have dyadic algebraic integrality; the individual eigenvalues of the Hankel correction matrices have coefficients in sqrt(2)*Q, with explicit odd denominators. The latter matrices are distinct from the Jacobi multiplication compressions.

The later section `diag`, equation `dn8` and Proposition `coeffq`, concerns explicit deformation coefficients of commutators, not a new RH equivalence. Its basic commutator definitions are consistent and are distinct from the incorrectly scaled `sigma(k)=N+c` assignment of S23 section5.2. The long q²/q³ coefficient formulas are not used as dependencies of this module.

## Added theorems and qualifications

- **AC-S14** proves graph-core density, strong-resolvent finite compression convergence, exact quadrature moments through degree2N-1, weak convergence, vanishing maximal atomic weights, and density of compression roots in the full real support. This works for finite Dirichlet local phases as well. It is unconditional.
- **AC-S15** records exactly the big-Witt logarithmic derivative and second finite difference, with source ghost sign convention `-q f'/f`. Formal coefficient integrality does not assign an etale cohomology object or arithmetic Frobenius.
- **AC-S16** proves that the mass-one, unscaled measures with all primes p<=X converge to delta0, with all fixed positive absolute moments tending to0. The proof was first obtained under A and then strengthened to unconditional using the classical PNT remainder. The key normalization is rho_X(t)=EulerProduct_X(t)/EulerProduct_X(0)<=1. The normalization integral has lower bound c X^(-1/4)(logX)^(-1/2). Uniform weighted prime estimates control eta<=|t|<=logX, and gamma tails beyond logX are O(X^(1/4-pi/2)(logX)^(a+1/2)) after normalization. There is no unaddressed intermediate-height gap. This result concerns the untwisted exhaustion only.
- **AC-S17** directly checks the first two heat coefficients for the zero-built operator. L26's full heat expansion is a cited background result, not independently rederived in its entirety here.
- **AC-S18** gives a genuine large-window limit without simple-even assumptions: the spectral projections for energies <=exp(-pi lambda²), extended by0 to whole-lineL2, tend strongly to identity. Their ranks diverge. For each K derivative the projected vector has an explicit weighted-L1 rate, hence Fourier convergence on every fixed closed horizontal strip. Density follows from exponential moments of |Xi|² and analytic Fourier uniqueness.
- **AC-S19** proves nonclosability of the global compact-test Weil form in unweighted whole-lineL2. It separately treats the union of finite-window closed-form domains and C_c∞, using smooth core approximants for the latter. This distinguishes the global setting from each closed finite window. The result explains why near-nullness does not select a ground eigenline.
- **AC-S20** completes the local eigenbranch construction with a Newton-slope/analytic implicit-function argument. The leading Gram determinants are nonzero because the first Lambert vectors evaluate independent polynomials of successive degrees. It proves convergence nearq0 for each fixed block, with no uniform radius claim.
- **AC-S21** identifies the central rescaling of the same prime exhaustion. Set C_X=sum p^(-1/2)(logp)^2/(1-p^(-1/2))^2~2sqrtX logX and s_X=sqrt(2C_X). The pushforward under t->s_X t converges in total variation and all fixed absolute moments to standard Gaussian. The proof controls the shrinking central region by exp(-c u²), the entire region 1/logX<=|t|<=MlogX by exp(-c sqrtX/log³X), and the remaining gamma tail with M chosen for the desired moment. Thus every fixed Jacobi coefficient satisfies a_n(X)^2~(n+1)/(4sqrtX logX), and the scaled full Jacobi operators converge strongly in resolvent to the Hermite/Gaussian operator. This is unconditional and specific to the displayed normalization.

## Primary PNT source actually verified

Lowell Schoenfeld, *Sharper bounds for the Chebyshev functions theta(x) and psi(x). II*, Mathematics of Computation30(134),1976,337--360.

Official PDF: https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf

Theorem11, equations(7.1)--(7.2), **printed p342**, gives the unconditional exponentially decaying remainder in sqrt(logx), which implies the logarithmic-power error used in AC-S16. Corollary1, equation(6.18), begins on **printed p339**, with its proof continuing on p340, and gives the stronger RH bound for pi(x). These locators were verified through the indexed primary PDF, not guessed from secondary accounts. The same volume's corrigendum corrects equation(7.4); AC-S16 uses(7.2), so that correction does not affect this argument. The original numerical inequalities inside Schoenfeld's proof are accepted as the published background theorem; they were not independently certified anew.

## Letter scope

Read sections `sectvW`, `sectxi`, `sectprolate`, `poisson`, `sectconv`, `miss`, `ultraviolet`, and `cmpro`, including full displayed theorem hypotheses, equations and narrative gates. Theorem `mainintro` assumes simple-even minimum. Section `miss` explicitly retains that condition and prolate-to-groundstate comparison. Equation `ku` repeats the scalar issue found in S25. Theorem `heatkernelintro`, equation `asymp`, concerns a zero-spectrum operator under RH; it is not an identification with the prolate operator. Trace assertions in `sectsemiloc` are handled by the trace agent.

No formal Lean check of A, numerical reproduction of the letter's tables, or comparison of all individual prolate eigenvalues with zeros was performed or claimed. The exact refined-count conflict stays in the explicitly unchecked note of the original module.

## Independent review performed for the trace module

All complete proofs AC-T01--AC-T14 were read. Source checks included the exact C99 VII.(4)--(13), TheoremVII.4 and CC20 `devil0`, `devil`, `sonine0`, `sonine1` normalization passages. The Gaussian-phase calculation, bounded-variation E_chi convergence, Mellin injectivity, inverse-Gram trace identity, finite-window form-core proof, strict positivity and compressed-translation norm were checked.

One wording correction was requested and accepted: AC-T11's rectangle is a sufficient uniform rectangular cutoff for the selected finite tensor factor, not an equivalence with arbitrary adelic norm cutoffs; smaller finite norm permits larger real fibers. The exact global comparison remains the stated T-CUT gate. No other defect was found in those new proofs. Their external source theorems and inherited MAS_ARTIN background results remain the named dependencies; this review does not claim to have re-proved all of them.
