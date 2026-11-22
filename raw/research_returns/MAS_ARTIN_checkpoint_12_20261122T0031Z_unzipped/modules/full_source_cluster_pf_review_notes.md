# Independent review of MA-MO-033

Reviewer: GPT-6 Astra Pro, MAS_ARTIN agent /root/pf26_audit.

Date: 2026-11-21.

Reviewed the complete 418-line written proof, then all final finite-prefix, reflection and centered-variable clarifications. Final proof version: full_source_cluster_obstruction.tex, 425 lines, MA-MO.1200–1221, SHA256 eff7eb6cac6e5cd060912dd5e0076eb15ae45281355289582d8078076e86d7a1.

**Outcome: pass.** The clarifications change no argument. There is no claim that the hypothetical cluster configuration occurs for an arithmetic Hecke function.

The subsequent status-only promotion was also read and passed: final status SHA256 a13cb6760e8d492f0f4961b9ed6d6f08fb3974bd12316ea1f200acdaade9800f. No mathematical text changed after the reviewed proof version.

## Complete proof verification

1. **Actual compact source and exact modulation.** I rederived the bilinear transpose with \(g_T=e^{-iT\cdot}g_0\), \(v_T=e^{iT\cdot}v_0\), and \(h_T=e^{-iT\cdot}h_0\). It gives \(C_{g_T^\vee}v_T=e^{iTx}k_0(x)\). Choosing the support in the final \(\log2\)-interval of the fixed real cutoff leaves precisely the unit ideal in \(\phi W\). The three expressions in1207 have the stated phases canceled, and the first two have uniform nonzero lower bounds for \(0<\delta\le\delta_0\). This remains valid when the cutoff is not monotone.

2. **Remainder and source-domain identities.** The supports controlling the exact dual-term vanishing and the compact double remainder are independent of \(T\). On that region the two ideal sums are finite, and modulation changes only their phases. The bound1208 is therefore uniform in \(T,\delta\). I freshly reread the actual original inverse, local source inclusion, support argument, bilinear transpose, compact remainder and paired Laplace formula in MO024 through567. No narrow inverse continuation replaces that identity.

3. **Sharp finite-orbit norm.** The modulation cancels inside the finite orbit integral to give the exact positive-amplitude formula1210. Its modulus is dominated by the infinite-orbit function, whose right tail is \(H_{h_T}(w)e^{-wx}\). Both exponentials in the sum norm give the tail integral \(e^{-2\delta x}(1+e^{-4ax})(1+x^2)^{s/2}\). Thus the norm is \(O(\delta^{-(s+1)/2})\), uniformly in \(T,\delta,L\). This is stronger than an estimate obtained by integrating translation norms, and the proof uses the exact vector. Every finite approximant is compact smooth and nonzero before normalization.

4. **Independent scalar convergence.** For each fixed \(\delta>0\), the closed-strip premise gives the strict positive gap needed for MO022 at \(b=a+\delta/2<1/2\). The orbit integrals converge in that wider sum norm. Its bounded original-source operator justifies the scalar Laplace limit without assuming boundedness at the target width \(a\). No estimate uniform as \(b\downarrow a\) is used. Holomorphic continuation of the previously proved wide identity then gives1212 on \(\Re w>a\).

5. **Baire and a fixed original-core sequence.** For each compact input, the actual source output depends continuously on the compact-support test. Closed operator-norm sublevel sets and Baire give one finite derivative estimate under the universal boundedness premise. Applying it to the modulations proves the stated necessary reciprocal bound. If that bound fails, the proof first chooses actual pairs \((T_n,\delta_n)\), then a finite truncation \(L_n\), and only then normalizes the genuine compact input. The lower bound1217 and polynomial modulation seminorms imply that the fixed-sequence bounded-output sets have empty interior. The real-test argument legitimately complexifies before using the complex modulations. No hypothetical unbounded operator is applied to a limiting non-core vector.

6. **Conditional cluster estimate and scope.** I rederived the upper finite-disk Blaschke factor estimate and the polynomial upper bound for the zero-free factor. Evaluating at \(z_n=a+d_n+iT_n\), with raw finite-\(L\) coordinate \(1/2+z_n\), gives a factor \(O(d_n)\) for every counted zero. The remaining factors have modulus at most one. The \(O(\log\nu(T_n))\) multiplicity count absorbs the fixed constant raised to \(k_n\), giving1221 with the correct exponent \(p-k_n\). The finite-prefix clarification ensures both \(d_n\le\delta_0\) and strict inclusion inside the left strip edge. The positive-support \(\eta\) family controls its right edge; the negative-support family gives the dual right-edge assertion by reflection. The proof does not infer both bounds from the positive-support family alone.

## Exact remaining limitations

The necessary bound is not asserted sufficient. The full-retention hypothesis by itself is not refuted for actual arithmetic data. The cluster implication requires its explicitly stated sequence; it can allow simple zeros, but none is constructed arithmetically. The restricted ideal return and the canonical whole-quotient return concern different domains and remain unchanged.

The source/interface rechecks above are written module rechecks. Earlier full primary Meyer/Tate audits remain inherited; this review does not claim to have repeated them.
