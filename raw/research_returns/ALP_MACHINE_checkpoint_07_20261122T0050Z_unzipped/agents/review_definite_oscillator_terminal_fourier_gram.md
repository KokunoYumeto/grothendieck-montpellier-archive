# Independent review of AM-DO-032

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC; inherited effort not separately exposed.

**Result: PASS**, at the precise finite-window scope of the saved proof. I read the complete saved `definite_oscillator_terminal_fourier_gram.md` and reconstructed the argument. I had previously read and independently checked the exact source definitions and support/norm calculations used in AM-DO-031; this review does not claim a fresh Lean build or an independent theta computation.

## Checks

1. The Y quotient consists of the actual permitted local residue classes. The CRT argument uses the same rational support and period modules already source-checked in DO031. Changing the representative changes the character argument by an integral element on the supported last row, so the finite function is unchanged.

2. At G the source condition is the degree-one case with `d_P=1`. The resulting pairing of `q^{-1}O/O` and `O/qO` is perfect. This hypothesis must not silently be applied to the newly enlarged degree-seven host at its ramified rational-29 places; DO032 explicitly retains the DO031 hypotheses, and its G calculation has that scope.

3. For Q, the limited-depth character annihilator is genuinely an `O`-submodule of its stated fractional domain. It contains `O`, and `psi(q^{-1})!=1` forces `-d_P<c_P<=0`. The multiplication arguments needed by the last-row Fourier family lie in the available depth `D_P>=2M`; no arbitrary extension of the local character is used. The radical is `q^M P^{c_P}O^a/q^MO^a`. Its size is `q^{-c_P a}`, and the quotient has size `q^{(2d_PM+c_P)a}`. The character integral contributes the full support volume `q^{d_PM a}`; the literal squared amplitude is `q^{-2Ma}`. This gives exactly `q^{(d_P-2)Ma}` and explains the stated duplicate vectors.

4. The tensor Gram is the common scalar kappa times the identity after duplicates are removed. Upper-matrix and T factors are fixed and nonzero, while all Y-dependence is in the last row. The value of kappa agrees with the independently checked DO031 norm. In the degree-one Q case, the counting-measure Fourier normalization and the Haar norm differ by the expected cell volume; neither has been substituted for the other.

5. Saturation uses Fourier group orders prime to 11, radical averaging of prime-to-11 order, and a unit coordinate of the fixed upper/T factor. These are integral splittings of the specified function lattice. They do not imply that its restricted Hermitian pairing is unimodular.

6. The 11-valuation of kappa consists exactly of the finite general-linear factors. The lifting-the-exponent formula is valid for the odd prime 11, and `t>=13`, `ord_11(q)<=10` gives the stated positive G contribution. With all chart scalars retained, the dual basis vector has denominator `v_11(kappa)`. The projector has the same exact denominator: the fixed-factor rank-one matrix contains a unit numerator, while the full last-row character projector has a prime-to-11 diagonal and denominator. This reasoning is about the chosen finite ambient coefficient window, not every possible oscillator detector.

7. With Hermitian pairings linear in the first argument, the displayed rank-one operator is `f_Y <.,f_Y>/kappa`. This gives the stated adjoint identity and `sum |ell(Tf_Y)|^2 = kappa ||Pi T^dagger ell^dagger||^2`. The argument is exact on the finite-dimensional image. It requires a nonzero projected adjoint for nonvanishing; it does not assert that condition or replace an automorphic terminal mass by a finite Gram scalar.

The separation between a saturated finite coefficient lattice, its nonunimodular restricted pairing, and the still-unidentified global detector lattice is correct and essential. No broader nonvanishing or MainX statement follows from this review.
