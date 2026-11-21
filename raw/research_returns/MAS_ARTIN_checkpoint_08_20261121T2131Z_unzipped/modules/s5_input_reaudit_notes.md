# Adversarial verification of the S5 Fourier-rigidity inputs

Date: 21 November 2026. Checker: GPT-6 Astra Pro, /root/s5_audit, MAS_ARTIN. Effort is inherited and not externally exposed.

This pass tests the arithmetic and analytic inputs of the combined closing argument rather than repeating its harmonic-analysis proof. No missing premise was found within the explicitly specified Calegari family and the exact real-axis hypothesis R_B. R_B itself remains an unproved general premise.

## Genuine data, including bad places

Booker Definition 1.3(A1)–(A4), author page 3, and Examples 1.4(2)–(3), author page 4, concern the actual finite Euler factors and the completed divisor. Calegari Theorem 1.1 supplies a tempered cuspidal degree-five comparison. Its finite parameters have modulus at most one; the Artin parameters are finite-image eigenvalues on inertia invariants, also of modulus at most one. At every prime, including the ramified primes, the logarithmic-coefficient difference therefore satisfies |f_R(p^j)|≤10(log p)p^(−j/2), with zero coefficients off prime powers. This directly gives every logarithmic pointwise decay requirement in A1 and Σ_(n≤x)|f_R(n)|²=O((log x)^3), by comparison with Σ_(n≤x)(log n)^2/n. No unproved Ramanujan assertion is needed beyond the tempered representation supplied in this particular theorem.

The finite bad set includes the ramification of both actual functions. Its coefficients may have either sign or be complex. A1 gives finite total variation along each fixed prime progression; the proof does not assume positivity there or silently delete them.

The signed divisor is the difference of the actual completed divisors, with integer orders at every point. Brauer meromorphic continuation of the Artin function suffices. Polynomial total multiplicity growth follows from the finite Brauer combination of Hecke functions and the automorphic count, as also covered by Booker's examples. No global Artin holomorphy is assumed to establish A3.

## Exact gamma equality and constants

At each real place of E, Calegari's finite-image two-dimensional parameter is odd, hence 1⊕sgn. The Sym^4(det)^−2 construction has three trivial and two sign constituents. E/Q splits at infinity, so its real descent has exactly that parameter. W has complex-conjugation trace one in dimension five, hence the same multiplicities. Both gamma factors are Γ_R(s)^3 Γ_R(s+1)^2. Thus the entire gamma kernel K_R vanishes, rather than merely its degree.

After this equality, the remaining conductor contribution is retained: f_R(1)=−(1/2)log(q_π/q_W), so the zero-frequency atom +2f_R(1)δ_0 is −log(q_π/q_W)δ_0. A constant root number contributes neither a divisor nor a logarithmic derivative. No conductor equality is assumed before the datum-vanishing conclusion.

## The explicit formula and whole completed support

Subtracting the two genuine data preserves the full A4 identity. The source's minus-sum convention starts at n=1, giving FT_+(−μ)=2f_R(1)δ_0 plus the signed prime-power atoms. The Hermitian-test identity extends complex-linearly as written in FQ001. At every good exceptional prime the exact ratio is P_W/P_π=((1+T)/(1−T))², which gives f_R(p^j)=4(log p)p^(−j/2) for odd j and zero for even j. The finite bad correction remains intact.

The final application now needs only the sufficient S508 conclusion that the positive Euler-series abscissa is at most 1/2. A hypothetical abscissa in (1/2,1) contradicts R_B by Landau, while an abscissa below 1/2, including a nonpositive one, is already sufficient. Convergence of the positive prime coefficients gives the absolutely convergent, nonzero Euler logarithm in Re s>1/2. The bad logarithms converge there by A1.

Exact gamma cancellation leaves only a nowhere-zero conductor exponential in the completed comparison. Therefore it has no divisor in Re s>1/2, including s=1. Its completed functional equation reflects the entire signed divisor, eliminating the open left half-plane including s=0. No endpoint polar masses were omitted. The earlier separate Tauberian estimate is not needed for this final support argument.

## Hypotheses and scope boundary

Only Calegari's two stated family hypotheses are used: complex conjugation of type 2B and unramified Frobenius at 5 of type 2B. No additional condition at 3 is introduced. The real-place construction was checked against the attached primary LaTeX and its publisher page locators. The earlier Sasaki applicability check remains as recorded; this pass does not claim to have re-proved the deep modularity, symmetric-power, or base-change inputs.

Datum vanishing forces equality of all normalized standard Euler factors, including bad primes, and the conductor atom. It does not by itself identify all ramified Weil–Deligne data. The exact S508 all-place comparison criterion supplies the stated comparison conclusion in its verified scope.

The remaining real-axis hypothesis concerns a quadratic Hecke function over the nonabelian sextic field F. Pullback of its character from a quadratic character over Q does not make its induced representation abelian: it is η⊕W. The new MA-RB-001 proves an explicit endpoint part under A, but not the full R_B interval.
