# Actual nontrivial-character PW synthesis at every polynomial weight

Date: 21 November 2026. Author/checker: GPT-6 Astra Pro, MAS_ARTIN /root/s5_audit. Effort is inherited and not externally exposed.

## Result and exact scope

MA-GW-004 is proved in character_weighted_pw.tex, equations MA-GW.45–83. The scope is 0<alpha<1/2, every s>=0, every primitive band Lambda>0, and additive smooth compact tests supported in (0,infinity). Characters are the nonprincipal primitive Dirichlet characters and the nontrivial finite-order Hecke characters over Q(zeta_3) with the actual source model proved in CGP001, including psi_269,3. There is no RH, A, M, generic-edge, simplicity or zero-separation hypothesis.

The actual half-line quotient retains all completed eta jets when beta<1/2+alpha and exactly the orders 2j<s−1 on the upper edge, capped by the zero multiplicity. Both its actual convolution and the actual ambient convolution after the weighted orthogonal quotient projection are trace class. The trace is independent of the finite band. Both orders of actual position/band limits are proved. Their difference has full multiplicity strictly to the left of the lower edge and only the unretained jet length on that edge, with a minus sign.

## Actual source, conductor and dual character

The invariant source band is Y=Q Lambda, where Q=|D_K|N(f_eta), and c=−log Y. In the actual reflected theta formula, the exact scalar simplifies to

w_K epsilon_eta^theta exp(zc) Q^(z−alpha) Lambda^(z+d)
= w_K epsilon_eta^theta Y^d Q^(−1/2),

with d=1/2−alpha. The phase is the already specified finite theta Fourier phase; it is not replaced by an unspecified root number.

The bounded causal symbol is Phi_eta(z)=L_K(z+d,bar eta)/(z+2)^N. A nontrivial finite vector already kills both adelic polar terms, so no factor z−(1/2+alpha) and no archimedean moment constraint belong here. Every source test, including one nonzero at frequency zero, has a(q)=exp(−dq)U(Lambda exp(−q)); all its derivatives decrease exponentially and it is flat at the band endpoint. Its exact image is the displayed nonzero scalar times T_phi (D+2)^N a. This treats every source test directly. The converse solves a gamma-kernel differential equation and truncates its solution in the weighted graph norm. No false annular Schwartz-density assertion is used.

The finite function on the reflected side is L(bar eta). Its completed functional equation sends its zero w to rho_eta=1−w, giving lambda_rho=rho_eta−(1/2+alpha). The proof explicitly checks the gamma factors on Re w>0, the absence of a polar factor, and the completed endpoint convention. The final divisor is eta's divisor.

## Actual operator proof

The proof supplies the full divided-difference resolvent construction and both domain-correct inverse identities on the actual quotient. It derives finite rank from the complete dual distributional ODE solution space of polynomial exponentials and proves the matching lower bound by the annihilating continuous jet chains.

The far-left resolvent estimate is O((1+|lambda|)^N), with one constant throughout the entire left region. This is one power larger than the pole-canceled zeta case. The M18 good-height lower bound is used only on one fixed central strip. S1 block summation, actual Bromwich inversion, far-left contour removal, and a positive-time approximate identity eliminate any residual quotient. A sufficiently high resolvent power is trace class; its left remainder is O(M^(N+1−q)).

The actual ambient lift retains the original polynomial/exponential weight. Its adjoint generator is W^−1(D W), with the complete graph domain and no artificial zero-endpoint condition. The full higher-order integration-by-parts formula retains both the endpoint at zero and the cusp at −c. Its bulk is a bounded operator times the trace-class resolvent power and its remaining terms are finite rank with graph-bounded traces.

## Checks actually completed

The entire 742-line finished proof was read after writing. That author reading passed all source constants, dual indices, actual domains, finite-rank arguments, global contour estimates, ghost elimination, endpoint/cusp signs, and both limits. Structural checking found 39 unique equation tags, no overlap with GW001–003, balanced proof and display environments. Root and pf26_audit subsequently completed independent whole-proof readings and both reported a pass. Root integrated the module. No independent input_audit review is claimed; that agent was assigned the negative-test operator extension.

For this extension, the complete CGP001–003 text was read, including its actual finite-vector, support, Poisson, condensation and Gram arguments. The full NT-Z10 fixed-character deduction and M18 selected-height/disk-Blaschke/Harnack proof were freshly reread. Those supply unconditional fixed-character estimates; no uniformity in field or conductor is inferred. The exact inherited Ramakrishnan–Valenza locators and the source/Grothendieck scope are recorded in the TeX. No new primary archive reading is claimed.

## Remaining joint-path issue

This theorem by itself proves two iterated limits and makes no uniform growing-band estimate. A separate actual-projection observation now offers a uniform slow-path extension: in the original weighted H, J_0 is contained in J_c for c<=0, so P_+ P_Zc=P_Z0 P_+ P_Zc. Positive compact convolution then factors every sufficiently far positive output tail through the fixed trace-class lift C_g P_Z0. PF26 is formalizing that new argument separately; it is not silently asserted by the present theorem.
