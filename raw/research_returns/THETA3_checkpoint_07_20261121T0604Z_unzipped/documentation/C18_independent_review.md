# THETA3-C18: independent whole-proof review

Reviewer: GPT-6 Astra Pro, inherited effort not separately exposed, child /root/noncm_integral. Date2026-11-21.

Read the entire `work/paper_parts/C18.tex` and primary `work/external/KatagiriKobayashi_sigma2026.txt`, including the full construction and proof of Lemma3.3(1). The theorem passes with the following exact clarifications.

1. The analytic full-series equality s_T(t)=sigma_zT(lambda(t)) is Definition3.1 and Remark3.2, p9. Theorem2.7 pp7--8 supplies the algebraic sigma value and Taylor coefficient algebraicity. It should not alone be cited as the full-series identity.
2. The whole compatible division system need not come from one rational lattice lift. The source construction depends only on T_4N (Remark2.4(2), p6), and a rational lattice lift realizing that finite datum suffices. A finite extension containing E[4N²] suffices for the algebraic data.
3. The divisor of g_T on the smooth integral model has, near the special origin, only the simple horizontal pole and a possible integer multiple of the special fiber. Thus t*g_T=varpi^a*v with v a local unit. Evaluation on the identity section is the tame unit N^(-1)*sigma_alg(T), so a=0. Completion gives an integral unit h_T. The compositional inverse of[N] is integral and unit-linear because N is prime to p; u_T=(t/a_N(t))*h_T(a_N(t)) is therefore an integral unit with the claimed constant term.
4. The equal-degree cancellation and the C11 derivative bound are exact. The model identification to the height-two Katz coordinate remains an explicit hypothesis; good reduction alone does not provide it. The q^{-1}D(qf) connection formula is an identity and correctly isolates the remaining frame/connection gate.

## Stronger algebraic rationality argument

Let M be any common multiple of the finitely many tame torsion orders. Then a_N([M](t))=[M/N](t) as formal group endomorphisms. Substituting Definition3.1 and canceling the equal number of common sigma(lambda([M]t)) factors gives

R_{T,U}([M](t)) = (product_i [M/N_i]^*g_{T_i})(t) / (product_i [M/N'_i]^*g_{U_i})(t).

The right side is the completion of an explicit rational function on the domain elliptic curve of the finite étale isogeny[M], over the same finite torsion field. Its completion is an integral unit because the left side is the substitution of an integral unit by an integral formal-group endomorphism. No extra multiple ofM, complex embedding, or multiplier-character descent argument is necessary. Before pullback, R(t) may retain a torsion flat twist and is not asserted rational on the original elliptic curve.

The source unit lemma itself was read in full: its use of the relative Picard group, Pic(R)=0, tame disjointness, and invertibility of a rational function with zero local divisor is logically consistent under the stated smooth Weierstrass and prime-to-p hypotheses. This review carries that cited theorem as background, rather than claiming a new proof of the source.

## Authorized appended refinement: actual tensor derivatives

Parent authorized the addition to `paper_parts/C18.tex`. The full proof now shows B=D²logq=−x−D²logt is an explicit rational function integral in t²R[[t]], even though A=Dlogq need not be integral (the actual square-lattice p7 example has A=−5t³/3+11t⁷/7+…). Under the already stated exact height-two coordinate hypothesis, the higher logarithmic derivatives have the C11 bound with index shifted by2.

A separate Bell-polynomial argument proves the weaker positive slope for every integer d and integral v(t):

v_p(D^n(q^d v)(0)) ≥ max(0, v_p(n!)−n p/(p²−1)) = max(0,n/(p²−1)−s_p(n)/(p−1)).

The proof uses D^p(R[[t]])⊂pR[[t]], canonical evenness of q in the additive coordinate, logq starting in degree4, and the exact inequality v_p(j!)−floor((j−2)/p)+1/(p−1)≤jp/(p²−1) for evenj≥4. Equality occurs atj=p+1; all larger evenj satisfy a direct bound. Integer Bell polynomials give integrality of derivatives, and exponential Taylor coefficient convolution handles integralv. This applies to actual products/quotients of tame sigma sections of any integer tensor degree. Degreezero retains the stronger slopep/(p²−1); no exact Alpoge connection matching is claimed.

The root and theta agent each independently read and reconstructed the entire appended proof and reported pass. Finite exact checks, explicitly distinguished from the general proof, are saved in `check_C18_connection_Bell.py` and its output file.
