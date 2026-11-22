# Quadratic Hecke shared-zero route: exact failed applications

Date: 2026-11-21. Author: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

Status: targeted literature and hypothesis check. No new theorem, no new zero-location conclusion, and no reduction of the current shared-zero gate. This note does not assert that no other method or theorem could settle it.

## The exact arithmetic question

Retain the specified Calegari family, E=L^(A5), F=L^(F20), H=EF, and B=zeta_H/zeta_F=L_F(s,eta_F)=C L_W, with C=L_Q(s,eta). The current checked result MA-RB-002 says that comparison failure forces a real gamma in (1/2,1), an integer k>= 1, B(gamma)=L_(V eta)(gamma)L_X(gamma)=0, and ord_gamma zeta_L>= 9k. MA-RB-008 confines it further to gamma<=1/2+sqrt(script-J_(Delta,1)) whenever script-J is positive. The question here is whether the additional input A supplies nonvanishing throughout this remaining interval from the special quadratic description of B.

Under A, the quadratic Dirichlet factor C has no off-center zero in (0,1), and neither does zeta_E=zeta_Q C. This does not give the same conclusion for B over the sextic field F: the actual induction identity is Ind_(G_F)^(G_Q)(eta_F)=eta+W. The pullback of a rational quadratic character therefore retains the unresolved nonabelian factor. These identities and their all-prime scope are the settled MA-S5.1 / GRH_NIGHT MT-S506(S506.6), MT-S508(S508.2); no finite-character certificate was rerun.

## 1. Real-simple-zero descent does not apply to the residual zero

Heilbronn's Theorem 1 states that, for a finite normal extension K/k, a real simple zero of zeta_K is a zero of the zeta function of the compositum of the quadratic extensions of k contained in K. For L/Q this compositum is E, so A excludes such simple zeros. The residual zero, however, has multiplicity at least 9k in zeta_L. Applying the theorem to H/F also supplies no exclusion: that extension is already quadratic, so its quadratic compositum is H itself. The simplicity issue was already identified in MA-RB-001; this fresh primary check does not count as new progress.

Source: Heilbronn, H. (1973). On real zeros of Dedekind zeta-functions. *Canadian Journal of Mathematics, 25*(4), 870–873. Theorem 1,p. 870. https://doi.org/10.4153/CJM-1973-090-3 . Primary PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C5957B0EA95C11C03686CE62D407E1DC/S0008414X00050926a.pdf/on-real-zeros-of-dedekind-functions.pdf . The theorem hypotheses and introductory scope were inspected. The parsed four-page proof has incomplete formula extraction; no new full source-proof certification is claimed.

## 2. Hecke zero-free and zero-repulsion estimates remain near 1

For Hecke characters modulo an ideal q of a number field K, Zaman's Theorem 1.1 gives a conductor-scaled rectangle sigma>= 1-c/D, |t|<=1, with at most one zero counted with multiplicity; D=log d_K+(3/4)log Nq+n_K nu(n_K), and the stated largeness hypothesis is required. A surviving exceptional zero and its character are real. For order 2 the displayed c is 0.1227. This permits precisely the real character type of eta_F. Theorem 1.4 is a repulsion theorem conditional on a real zero 1-lambda1/D sufficiently close to 1; in the quadratic case its stated quantitative alternatives require lambda1<=0.1227 or the stronger lambda1<=10^(-10). Neither statement supplies exclusion throughout the residual interval above 1/2. In particular, arbitrary gamma in that interval cannot be inserted while discarding the small-lambda1 premise.

Source: Zaman, A. (2016). *Explicit estimates for the zeros of Hecke L-functions* (arXiv:1502.05679v4, 29 March 2016), Theorems1.1 and1.4,printed pp. 2 and 4; Corollary 1.2/region discussion,p. 3. https://arxiv.org/pdf/1502.05679 . Exact statements and hypotheses were read; the 53-page proofs were not independently audited or applied.

## 3. Available Rankin–Selberg exceptional-zero results have the same scope limitation

Ramakrishnan and Wang define a Landau–Siegel zero by a conductor-dependent interval(1-C/log M,1). Their Theorem A concerns Rankin–Selberg functions of two cuspidal GL2 representations and explicitly retains certain quadratic-character exceptions. Their symmetric-fourth-power discussion likewise excludes Landau–Siegel zeros, not arbitrary real zeros in (1/2,1). Thus this source cannot provide the requested interval-wide shared-zero exclusion merely from known low-degree automorphy. Its proof may use holomorphy of an auxiliary quotient on(1/2,1), but that is not the zero-free conclusion of the theorem.

Source: Ramakrishnan, D., & Wang, S. (2001). *On the exceptional zeros of Rankin–Selberg L-functions* (arXiv:math/0108054v1, 8 August 2001), Introduction and Theorem A,printed pp. 1–2; symmetric-fourth-power scope discussion,pp. 3–5. https://arxiv.org/pdf/math/0108054 . These statements and the accompanying explanation were read; no new full proof audit or applicability theorem is claimed.

## Further scope checks and outcome

The already proved signatures are F: (2,2), H: (4,4); E is real and every real place of F splits in H. Thus H/F is not a totally imaginary quadratic extension of a totally real field. Results assuming that CM situation cannot be invoked here without a separate replacement argument. The completed B has root number +1 and gamma factor Gamma_R(s)^4 Gamma_R(s+1)^2 (MA-RB.15). Those nonvanishing gamma factors and the functional equation pair gamma with 1-gamma and preserve its order; they do not exclude that pair.

No inspected theorem removes the shared-zero condition B(gamma)=L_(V eta)(gamma)L_X(gamma)=0 on the remaining interval. No universal comparison of every literature constant with script-J is claimed. The useful conclusion of this check is narrower: the simple-zero, near 1, or CM hypotheses needed by these proposed applications are not supplied by A and the present comparison data. MA-RB-008 remains the current smaller arithmetic gate. No new conjecture or equivalent reformulation is promoted as progress.
