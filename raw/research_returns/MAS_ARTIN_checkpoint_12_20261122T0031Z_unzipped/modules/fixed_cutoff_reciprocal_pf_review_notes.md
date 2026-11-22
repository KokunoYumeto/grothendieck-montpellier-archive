# Independent review of MA-MO-032

Reviewer: GPT-6 Astra Pro, MAS_ARTIN agent /root/pf26_audit.

Date: 2026-11-21. Complete written-proof reading finished before 23:27 UTC.

Reviewed file: fixed_cutoff_reciprocal_criterion.tex, all 526 lines, equations MA-MO.1100–1123 and the final arithmetic/framework scope. SHA256: 6903a24f09943d6595c09ec080d0d754f52b45f4d31334049ee256b8c2987020.

**Outcome: pass. No mathematical or scope correction requested.**

## Complete proof checks

1. **Nearby polynomial lower value.** The disk centered at \(2+iT\), with radius in \((12,13)\), lies in a fixed vertical strip and contains \(O(\log(2+|T|))\) zeros with multiplicity. Removing the entire finite Blaschke product leaves a zero-free holomorphic factor. Its polynomial boundary upper bound and the Euler lower bound at the center give a polynomial inverse bound on the inner half disk by Harnack. Averaging the integrable logarithmic singularities over the fixed interval \([c,2c]\) provides one ordinate \(t_T=T+v_T\), uniformly within a fixed distance of \(T\), at which the Blaschke product is only polynomially small. This argument does not assume a polynomial reciprocal estimate on the original full line, simplicity, or separation of zeros.

2. **Exact separated packets.** The predetermined normalized step has \(p(0)=-1\), so its ordinary off-diagonal kernel \(\kappa(v)=ip(v)/(2\pi v)\) is nonzero on a fixed small positive interval. The modulated test belongs to the same support space \(\mathscr D_{[1,2]}\) and has polynomial derivative seminorms. Polynomial bounds for \(A'\), the nearby lower value of \(A\), and \(j'/j\) give one polynomial packet width controlling all four complex ratios. With the inner product linear in its first variable, the stated output phase cancels the phase of \(A(t_T)j(T)\kappa(v_T)\). The double integral has the factor \(h_T(\int\alpha)^2\), and its real part gives the claimed lower bound. No unsigned-kernel-to-operator inference is used.

3. **Uniformity from the universal quantifier.** For each fixed compact-frequency core vector, both actual core terms depend continuously on the test in its fixed-support Fréchet topology. The sets \(F_n\) are closed, and Baire plus differences and homogeneity gives a single finite derivative estimate under the assertion that every test is bounded. Applying it to the modulation family proves the polynomial reciprocal bound. The real-test assertion legitimately complexifies before the complex packets are used.

4. **Positive branch and failures.** Polynomial growth of \(j\), together with \(Aj=1\) and the polynomial derivatives of \(A\), gives polynomial growth of every derivative of \(j\). The canceled kernel is therefore Schwartz in the independent coordinates \(t,t-u\), giving trace class and trace-norm convergence of the actual finite-frequency cutoffs. If the polynomial bound fails, the complement of the union of the closed \(F_n\) is a dense \(G_\delta\), over both real and complex tests. For a fixed bad test, the identity \(V_aK_N V_a^{-1}v=\chi_NK_g^\circ v\) on each fixed compact-frequency vector proves unbounded finite-operator norms. The separately established convergence of scalar traces is not confused with operator convergence.

5. **Gevrey cutoff and literal sequential domains.** For any fixed compact-frequency input, the off-support tails of both \(T_\phi v\) and \(T_\phi(jv)\) are controlled by the Gevrey decay of \(p(t-u)/(t-u)\). This decay dominates the known \(\exp(C\log^2(2+|t|))\) reciprocal bound. Thus \(M_jT_\phi v\) lies in the domain of \(M_A\), and \(T_\phi(jv)\) also lies in that domain. The two sequential compositions exist before subtraction. No Gevrey condition on the left smoothing test is required for these domain checks.

## Rechecked antecedents and limits of this review

I freshly reread the definitions and positive/domain argument of MA-MO-031, through its Schwartz-kernel and finite-cutoff comparison. I also freshly reread MA-RS-001's full generic-line/minimum-modulus proof, the definitions MA-RS.8–9, and the MA-RS-007 bounded-composition/kernel/trace and polynomial logarithmic-derivative argument through MA-RS.64. These are written module/interface rechecks; no new full primary-source audit is claimed.

The theorem is conditional on the polynomial reciprocal bound in its positive branch and on its failure in its negative branch. It asserts neither that an arithmetic reciprocal has nonpolynomial growth nor that a hypothetical bad packet belongs to the completed theta ideal. The fixed-cutoff universal-test criterion does not decide a single prescribed pair \(g,\phi\). Under the stipulated arithmetic input \(A\), the fixed horizontal gap supplies the positive branch through MA-RS-004.
