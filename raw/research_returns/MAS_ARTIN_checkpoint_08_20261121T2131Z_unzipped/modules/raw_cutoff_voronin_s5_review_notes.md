# Raw Euler-conjugated cutoff: independent route and primary-input check

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

## Status of this record

This records an independent reconstruction and check of the proposed argument before root's complete written module is available. It is not a claim to have read a future module or to have re-proved the classical universality theorem. The route passes with the exact original disk normalization described below.

## Exact primary input actually read

Voronin, S. M. (1975). Theorem on the “universality” of the Riemann zeta-function. Mathematics of the USSR-Izvestiya,9(3),443–453. DOI:10.1070/IM1975v009n03ABEH001485.

Fresh retrieval returned the primary English article's parsed text. I read the complete unnumbered theorem in sectionI, printed443–444: a nonvanishing analytic target on a disk of radius r<1/4, continuous on its closure, can be uniformly approximated by zeta translated from the center3/4. Only existence of a real vertical translate is needed here. No positive-density or arbitrarily-large-shift enhancement is invoked.

Primary PDF locator, sectionI, printed443–444:

https://www.mathnet.ru/links/603f31128a8bf44eadd631d4e00fc83c/im2037_eng.pdf

A subsequent screenshot attempt redirected to the MathNet home page, so no fresh page-image inspection is claimed. The full classical proof remains declared background, as in MA-MO-001.

## Original disk suffices

Fix1/2<sigma<1. Put h=sigma−3/4 and choose |h|<r<1/4. For the nonzero entire Fourier transform p of phi', choose a sufficiently small d>0 with p(d) nonzero and h²+d²<r². The nonvanishing entire target

    f_M(z)=exp(−i M(z−h))

has value exp(Mv) at z=h+iv. Its minimum modulus on the closed original disk is exp(−Mr). Apply precisely the printed theorem with absolute error epsilon exp(−Mr). This gives a uniform relative error at most epsilon, with epsilon fixed and small. Both frequency windows of width2/M about T_M and T_M+d lie in that translated disk for large M. No translated-disk theorem centered at arbitrary sigma is assumed.

## Actual domain and cross-window norm

In the unitary weighted Fourier picture, let A(t)=zeta(sigma+it), j=1/A, and Phi=F_+ M_phi F_+^−1. On compact smooth frequency tests whose supports avoid the line zeros, jv is compact smooth, Phi(jv) is Schwartz, and A has polynomial growth. Therefore Q=M_A Phi M_j is an actual L2-valued composition on this dense core. No generic-line reciprocal estimate or domain assertion for J M_phi is needed.

Away from t=u its kernel is A(t)j(u)k(t−u), where k(v)=i p(v)/(2pi v). Let b be nonnegative, smooth, supported in(−1,1), and of L2 norm1. Put

    v_M(u)=sqrt(M)b(M(u−T_M)),
    w_M(t)=exp(i arg k(d))sqrt(M)b(M(t−T_M−d)).

Both vectors have norm1, and their supports are disjoint for large M. Consequently only the ordinary off-diagonal kernel enters their pairing; any delta or principal-value convention on the diagonal is irrelevant.

After t=T_M+d+eta/M and u=T_M+xi/M, the zeta ratio is

    exp(Md+eta−xi)(1+O(epsilon))

uniformly for |eta|,|xi|≤1. Continuity of k at d and sufficiently small fixed epsilon make the rotated integrand have real part at least a fixed positive multiple of

    exp(Md+eta−xi)b(eta)b(xi).

The two normalizations and two integration changes contribute exactly1/M. Thus the pairing, and hence the operator norm on the unit core vector, is at least c exp(Md)/M for a constant c>0 independent of M. This is a norm lower bound, not an inference from large pointwise kernel values.

## Finite Euler factors and scope

For a fixed finite S, E_S(sigma+it)=product_(p in S)(1−p^(−sigma−it)) is smooth, bounded, and bounded away from zero. Its multiplier and inverse preserve the core. The exact relation

    Q_S=M_E Q_empty M_E^−1

is a bounded invertible similarity, so the same obstruction applies. Since Phi is bounded, Phi−Q_S cannot have a bounded extension either.

The proof concerns the raw composition and its difference from the cutoff on this particular one-sided H_a. It does not refute a smoothed C_g composition, does not assign a literal J M_phi domain on an arbitrary nongeneric line, and does not identify all possible common-space completions. On the previously proved generic/Gevrey-cutoff core, the existing RS.21 identity supplies the literal commutator interpretation.

## Additional exact graph approximation from the actual smooth theta image

The compact-frequency vectors themselves need not be exponential Schwartz in the physical variable. This domain distinction can be removed for the same closed-multiplier composition by a moment-preserving approximation, without identifying a different geometric cutoff.

For a fixed core vector v, put q=jv in compact smooth frequency space. Choose h in Schwartz space with normalized Fourier transform

    F_+h(t)=q(t)/(1−sigma−it).

The denominator has no real zero because sigma<1. For epsilon>0 define

    H_epsilon(x)=exp(−epsilon x²−ax)h(x),
    F_epsilon=(partial_x+1/2)H_epsilon.

Then F_epsilon belongs to exponential Schwartz space and its Mellin moment at1/2 is zero, by integration by parts. Its weighted Fourier transform q_epsilon tends to q in Schwartz topology. Indeed multiplication of h by exp(−epsilon x²) converges to h in that topology, and the differential operator transforms to multiplication by1−sigma−it.

Consequently g_epsilon=Z_S F_epsilon belongs to the actual smooth theta image: MA-TR-101/MA-MO-001 supplies the original moment-zero theta identity, and each finite removed Euler factor is the finite translation operator I−p^(−1/2)U_(−log p), which preserves exponential Schwartz space. In the weighted Fourier picture,

    V_a g_epsilon=A q_epsilon -> v,
    V_a Q_S g_epsilon=A Phi q_epsilon -> A Phi q

in L2. Both convergences follow from polynomial growth of A and Schwartz convergence; Phi preserves Schwartz because phi and all its derivatives are bounded. Also J_S g_epsilon=F_epsilon on its actual multiplier domain.

Thus every core graph pair is in the graph closure of the same raw composition restricted to the original moment-zero smooth theta image. A bound on that image would imply the contradicted core bound. The output Z_S phi F_epsilon here is expressly the closed multiplier continuation; when phi F_epsilon has a nonzero polar moment, this does not assert that an unregularized geometric theta sum lies in H_a. This remaining output convention must stay explicit.
