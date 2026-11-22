# Independent whole-proof review of AM-DO-031

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

**PASS for the stated finite-function theorem and its precise limitations.** I read the complete saved report `definite_oscillator_terminal_xi.md`, reconstructed its support, norm and nonvanishing arguments, and directly read the displayed source definitions and the terminal-frame bridge. No Lean compilation or terminal theta-image computation was performed.

## Source/formula checks

The literal `PhiQ`, `PhiG`, and `PhiGS` in `FiniteSumNonzeroLargeDepth.lean`, lines 711–715 and 780–806, match the matrix orientation in the report: the terminal upper matrix has b−1 output rows and a input columns. The exact `entB_top` theorem removes all auxiliary-column scaling at the last edge. `locTop`, `xiOver`, and `xiLast` give the displayed product of `PhiTop` and `ftY`, with the negative additive-character sign and the Q amplitude \(q^{-\mathsf M a}\). The report correctly retains the piT scaling already contained in the prescribed terminal frame.

I read `ybSet`, `repY`, the exact Q-frame condition `DecoF`, and `PtAt.repY_mem`. These prove the Q representative bound without assuming an extra additive-character continuity theorem. The source depth clause is \(2\mathsf M\le D_P\), exactly what the last-row pairing needs. The report's extension to the finite local quotient is valid: rational local elements are dense, the quotient is finite, and additivity together with triviality on integral elements makes the value depend only on that quotient. Its finite-group character values are roots of unity.

The support/period indices retain \(d_P=v_P(q_P)\) at general Q-primes. Thus the support-row volume is \(q^{d_P\mathsf M a}\), while the actual complex amplitude square is \(q^{-2\mathsf M a}\). These give the stated Q norm and must not be merged into a uniformizer convention. At G, the source degree-one prime count and total degree force ramification index one, so its simplification is valid.

## Independent counting and Fourier checks

For the G factor I independently reconstructed the fixed residue entries from the literal `PhiGS` conditions, including the natural-number truncated subtraction and the permutation `symIdx`. The first block has \(r(r-1)/2-k\) free entries; the removed k entries were free upper-unipotent entries before the extra condition. The later diagonal blocks must be invertible because the whole determinant character is zero otherwise. The resulting exponent is
\[
C_G=\frac{r(r+1)}2+k+mrt+\frac{m(m-1)}2t^2.
\]
An independent exact finite position-counting calculation checked this expression against the source-shaped zero conditions for 18 rank-admissible choices. It includes \((m,k,t)=(2,6,13)\), giving \(C_G=385\). The output is `review_do031_support_count.json`; this is a residue-entry counting check, not an enumeration of all invertible matrices.

The Fourier normalization has denominator \(N=[L:L^-]\). Character orthogonality gives exactly the displayed inversion and Parseval factor \(1/N\); distinct support cosets are orthogonal. In the fixed position-translation convention, \(W_{-a_0}W_y\) has the function \(\psi(B(t-a_0,y))1_L(t-a_0)\), and its single-Heisenberg form has the central phase \(\psi(-B(a_0,y)/2)\). The coefficient-denominator and \(\ell^1\) bounds follow without a missing volume factor. The report explicitly retains the determinant/Jacobian when changing a nonintegral base frame.

The identity-block local matrices give raw values one at G and \(q^{-\mathsf M a}\) at Q, independently of the allowed representative. The T incidence equation is solvable because its row vector is nonzero. Additive CRT on a common fractional lattice produces a rational matrix in all the chosen local cosets and integral outside the selected primes; cancelling common-denominator valuations at the remaining primes is an additional finite congruence condition. Hence the exact nonzero raw value follows. If the auxiliary residue characteristics avoid 11, Fourier denominators are 11-units and this raw unit value proves primitivity of the finite coefficient vector.

The last distinction is essential and correctly preserved: a nonzero raw function or primitive finite vector does not imply that its selected theta sum is nonzero, nor that it has a unit pairing with the preceding automorphic image. The report leaves the selected operator, integral row normalization, terminal mass and MainX bounds open. The newly found `IsEtaT` obstruction is a separate arithmetic-host condition and is not bypassed by this finite realization.
