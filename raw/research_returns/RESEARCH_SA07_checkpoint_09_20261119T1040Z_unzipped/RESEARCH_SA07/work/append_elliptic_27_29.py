from pathlib import Path
tex=r'''

\begin{result}{A.4.27}{The exact G-function input for the elliptic primitive}{Proved}
Let $K$ be a number field, let $E:y^2=P(x)=4x^3-g_2x-g_3$ be smooth over $K$, and let $Q=(x_0,y_0)\in E(K)$ satisfy $y_0\ne0$. For every $a\in K$, the germ
\[
 F_a(t)=-\int_0^t\frac{x_0+s+a}{\sqrt{P(x_0+s)}}\,ds,
 \qquad \sqrt{P(x_0)}=y_0,
\]
is a $G$-function over $K$. In the coordinate $x=x_0+t$ it satisfies
\[
 2P(x)(x+a)F_a''+
 \bigl(P'(x)(x+a)-2P(x)\bigr)F_a'=0.
\]
For some integer $C\ge1$, the first $n$ Taylor coefficients have a common denominator dividing
\[
 (4C)^{n+1}\operatorname{lcm}(1,\ldots,n).
\]
If $x=\wp(u)$ and $x_0=\wp(u_0)$, the exact analytic expression is
\[
 F_a(x-x_0)=\zeta(u)-au-\zeta(u_0)+au_0.
\]
At $a=h$, its additive monodromy along an elliptic loop of period $\lambda$ is $c\bar\lambda$, and is nonzero whenever $\lambda\ne0$.
\end{result}
\begin{proof}
Write $P(x_0+t)=y_0^2(1+b_1t+b_2t^2+b_3t^3)$. The expansion
\[
 (1+z)^{-1/2}=
 \sum_{m\ge0}\frac{(-1)^m\binom{2m}{m}}{4^m}z^m
\]
computes the derivative of $F_a$. Choose $C$ clearing the denominators in $\mathcal O_K$ of the $b_i$, $(x_0+a)/y_0$, and $1/y_0$. The coefficient $e_n=[t^n]F_a'$ then satisfies $(4C)^{n+1}e_n\in\mathcal O_K$: each summand uses at most $n$ of the $b_i$ and one further cleared factor. Integration divides $e_{j-1}$ by $j$, proving the denominator bound. The least common multiple grows at most exponentially, and each complex conjugate of the algebraic derivative is analytic on a nonzero disc at zero. Cauchy's estimate therefore bounds all conjugates of the coefficients exponentially. Together with the displayed linear differential equation, these are precisely the $G$-function conditions. That equation follows by differentiating $F_a'=-(x+a)/\sqrt{P(x)}$ and clearing denominators.

The uniformization identity follows from $d\zeta=-x\,du$ and $du=dx/y$, with the constant fixed at $u_0$. Translation by $\lambda$ changes it by $\eta_\lambda-a\lambda$. The established identity $\eta_\lambda=h\lambda+c\bar\lambda$ proves the last assertion.
\end{proof}

The current arithmetic-holonomy theorem of Calegari--Dimitrov--Tang \cite[Theorem 2.5.1, pp.16--17]{EllCDT2024} imposes an explicit denominator template and a strict inequality comparing a holomorphic uniformizing map's conformal radius with its denominator exponent. Its numerator is an explicit Bost--Charles boundary double integral. A.4.27 verifies the elementary $G$-function input for every algebraic correction, while also computing the actual monodromy at $h$. A quantitative analytic improvement or a further product-formula relation specific to $h$ has not been established here. The source does not infer ordinary bounded denominators from the $G$-function condition. The related 2026 ICM article \cite{EllCDT2026} was also opened; no unverified application of its effective bounds is used.

\begin{result}{A.4.28}{Horizontal Hodge jets and an explicit CM denominator obstruction}{Proved}
In the Legendre family
\[
 E_t:y^2=4x(x-1)(x-t),\qquad
 \omega=dx/y,\quad \eta=x\,dx/y,
\]
the Gauss--Manin connection matrix, with columns giving the derivatives of the basis, is
\[
 C(t)=\begin{pmatrix}A&A\\ B&-A\end{pmatrix},\qquad
 A=\frac1{2(1-t)},\qquad B=-\frac1{2t(1-t)}.
\]
At $t_0=1/2$, the antiholomorphic class is $\eta-\omega/2$, and the short Weierstrass equation has $g_2=1$, $g_3=0$, and $h=0$. Its horizontal extension $F(s)\omega+G(s)\eta$, with $s=t-1/2$, is
\[
 G(s)=\sum_{m\ge0}
 \frac{\prod_{j=0}^{m-1}(4j+1)^2}{(2m)!}s^{2m},
 \qquad
 F(s)=\left(\frac12-2s^2\right)G'(s)
       -\left(\frac12+s\right)G(s).
\]
For every prime $p\equiv3\pmod4$, the coefficient $[s^{p+1}]G$ has $p$-adic valuation $-1$. Thus this actual algebraic CM Hodge splitting has horizontal Taylor coefficients with infinitely many denominator primes, and fails the $\omega(p)$-integrality condition of Lam--Litt.

More generally, at every algebraic nonsingular Legendre parameter and every nonzero algebraic initial vector in a positive symmetric power of its de Rham cohomology, the horizontal extension fails both integrality conditions of \cite[Theorem 4.1.1, p.21]{EllLamLitt2025}.
\end{result}
\begin{proof}
Differentiation at fixed $x$ gives
$\partial_t\omega=\omega/(2(x-t))$ and
$\partial_t\eta=\omega/2+t\partial_t\omega$.
For $R=x(x-1)/y$, direct differentiation gives
\[
 d_xR=\left(\frac{x-t}{2}
       -\frac{t(t-1)}{2(x-t)}\right)\omega.
\]
Modulo exact forms, these identities give the stated matrix, including its signs.
At $t=1/2$, the translation $x=X+1/2$ gives $y^2=4X^3-X$; hence $\eta-\omega/2=X\,dX/y$ is the antiholomorphic class by A.4.4.

Horizontal coefficient vectors satisfy $(F,G)'=-C(F,G)$. Eliminating $F$ gives
\[
 t(1-t)G''+(1-2t)G'-G/4=0,
 \qquad G(0)=1,\quad G'(0)=0
\]
where the last two values are at $s=0$. Equivalently,
$(1-4s^2)G''-8sG'-G=0$. Its coefficient recurrence is
\[
 [s^{2m+2}]G=\frac{(4m+1)^2}{(2m+2)(2m+1)}[s^{2m}]G,
\]
proving the formula and the expression for $F$.

For $m=(p+1)/2$, every numerator factor $4j+1$ is positive and below $2p$. None equals $p$, since $p\equiv3\pmod4$. Thus the numerator is a $p$-adic unit, whereas $(2m)!=(p+1)!$ has valuation one. There are infinitely many primes congruent to three modulo four: if they formed a finite list, a prime divisor congruent to three modulo four of four times their product minus one would be new. Consequently infinitely many denominator primes occur. If $\omega(p)/p\to\infty$, then $p+1\le\omega(p)$ for every sufficiently large prime; the exhibited coefficients also exclude $\omega(p)$-integrality.

For the general statement, take $R=\mathcal O_K[1/N]$ large enough to contain the algebraic initial data and to make $t_0$ and $1-t_0$ units. The Legendre family over $R[t,1/(t(1-t))]$ is smooth, projective, and nonisotrivial. Its $j$-function is nonconstant. The nonzero initial vector and every positive symmetric power therefore satisfy exactly the hypotheses of Lam--Litt's Theorem~4.1.1. This gives the asserted specialization of that proved theorem.
\end{proof}

The relationship to the complex splitting is explicit. In a locally constant Betti trivialization, the antiholomorphic period vector depends antiholomorphically on the base coordinate. Freezing its conjugate coordinate at the starting point gives its horizontal holomorphic continuation. Thus an algebraic $\xi+h\omega$ supplies the algebraic initial vector in A.4.28, with the scalar normalization fixed at that point. It does not supply integral horizontal jets; the displayed CM example disproves that inference. Lam--Litt's theorem consequently applies to this continuation with its stated hypotheses, while the original algebraicity question for $h$ remains unproved.

\begin{result}{A.4.29}{Division-polynomial data preserve the Gaussian parameter ambiguity}{Proved}
For any $a\in\C$, put $\theta_a(u)=e^{-au^2/2}\sigma(u)$ and
$\eta^{(a)}_\lambda=\eta_\lambda-a\lambda$. The normalized division polynomial $F_n$ satisfies
\[
 F_n(\wp(u),\wp'(u))
 =\frac{\sigma(nu)}{\sigma(u)^{n^2}}
 =\frac{\theta_a(nu)}{\theta_a(u)^{n^2}}.
\]
For every $u_0\in\Lambda\otimes\Q$, the normalized torsion constant likewise satisfies
\[
 e^{-\eta^{(a)}_{u_0}u_0/2}\theta_a(u_0)
 =e^{-\eta_{u_0}u_0/2}\sigma(u_0).
\]
Thus the map from the parameter $a$ to all division-polynomial quotients and these torsion constants is constant. The same quotient identities hold as formal series over every characteristic-zero coefficient field, including a $p$-adic field.
\end{result}
\begin{proof}
The Gaussian factors in the first quotient cancel because $(nu)^2=n^2u^2$. The sigma transformation law shows that the remaining quotient is elliptic. Its divisor is $[n]^*[O]-n^2[O]$, and its leading term is $n u^{1-n^2}$. As $t=-2x/y=u+O(u^2)$, this is exactly the normalization
\[
 \left.\frac{t^{n^2}F_n}{[n]^*t}\right|_O=1
\]
used in \cite[p.2]{EllKatagiriKobayashi2026}. Divisor and leading term uniquely determine the rational function, proving the first identity. Substitution of $\eta^{(a)}_{u_0}=\eta_{u_0}-au_0$ proves the second. The Gaussian cancellation is an identity of formal exponential series, proving its characteristic-zero formal version.
\end{proof}

Katagiri--Kobayashi's September~2026 primary preprint \cite[Theorem 1.3 and Corollary 1.4, pp.3--4]{EllKatagiriKobayashi2026} determines certain $p$-power subsequential limits of division-polynomial values in both ordinary and supersingular good reduction. Its algebraic sigma value is exactly the normalized torsion constant above \cite[Definition 2.3, Proposition 2.5, and Theorem 2.7, pp.6--7]{EllKatagiriKobayashi2026}. A.4.29 identifies the actual noninjective map through which these data pass. It does not identify the Gaussian parameter with the canonical complex value $h$, nor does it exclude a different construction using further data. The remaining H1 gate is unchanged.
'''
with Path('output/RESEARCH_SA07/sections/A_elliptic.tex').open('a') as f:f.write(tex)
with Path('work/elliptic_references.bib').open('a') as f:f.write(r'''
@misc{EllCDT2024,
 author={Frank Calegari and Vesselin Dimitrov and Yunqing Tang},
 title={The linear independence of $1$, $\zeta(2)$, and $L(2,\chi_{-3})$},year={2024},
 eprint={2408.15403},archivePrefix={arXiv},
 url={https://math.berkeley.edu/~ytang/L2chi.pdf},
 note={Opened and downloaded complete 218-page author-hosted primary manuscript. Theorem 2.5.1, pp.16--17, and Section 2.6, pp.17--18, read. Primary arXiv metadata separately opened: version 2, 16 September 2024. No unverified quantitative holonomy bound is claimed for the elliptic input.}
}
@incollection{EllCDT2026,
 author={Frank Calegari and Vesselin Dimitrov and Yunqing Tang},
 title={Arithmetic holonomy bounds and effective {Diophantine} approximation},
 booktitle={Proceedings of the International Congress of Mathematicians 2026},volume={3},pages={356--376},year={2026},publisher={SIAM},
 doi={10.1137/25M1806776},url={https://math.uchicago.edu/~fcale/papers/ICM.pdf},
 note={Opened and downloaded complete 20-page author-hosted primary article, bearing 2026 SIAM copyright; primary publisher metadata separately opened. Consulted for arithmetic-holonomy applicability, without asserting that its numerical hypotheses have been verified for H1.}
}
@misc{EllLamLitt2025,
 author={Yeuk Hay Joshua Lam and Daniel Litt},title={Algebraicity and integrality of solutions to differential equations},
 year={2025},eprint={2501.13175},archivePrefix={arXiv},url={https://arxiv.org/pdf/2501.13175},
 note={Opened and downloaded complete 93-page primary version 1, submitted 22 January 2025, manuscript dated 24 January 2025. Integrality and omega(p)-integrality defined on p.3; Theorem 4.1.1, p.21, explicitly requires a nonzero initial vector; its proof, p.24, read. The adjacent recurrence corollary is not used without the necessary nonzero-initial-data qualification.}
}
@misc{EllKatagiriKobayashi2026,
 author={Yu Katagiri and Shinichi Kobayashi},title={$p$-adic properties of division polynomials and algebraic sigma functions},
 year={2026},eprint={2609.07024},archivePrefix={arXiv},url={https://arxiv.org/pdf/2609.07024},
 note={Downloaded and read complete 17-page primary version 1, dated 7 September 2026. Division-polynomial normalization, p.2; Theorem 1.3 and Corollary 1.4, pp.3--4; Definition 2.3, Proposition 2.5, Theorem 2.7, pp.6--7; proof of the analytic normalization, p.8. Web PDF retrieval failed, but direct local primary download succeeded and was text-extracted.}
}
''')
with Path('work/agent_elliptic.md').open('a') as f:f.write(r'''

## 28. Lam–Litt and the actual CM horizontal continuation

**A.4.28 (proved).** For Legendre y²=4x(x−1)(x−t), basis ω=dx/y, η=xω, the Gauss–Manin matrix is C=[[A,A],[B,−A]], A=1/(2(1−t)), B=−1/(2t(1−t)). The reduction identity is d(x(x−1)/y)=((x−t)/2−t(t−1)/(2(x−t)))ω. At t0=1/2 the translation x=X+1/2 gives g2=1,g3=0,h=0; thus η−ω/2 is the actual anti-Hodge vector. Its horizontal extension V=(F,G), in s=t−1/2, has G=sum_m(prod_(j<m)(4j+1))²/(2m)! s^(2m), F=(1/2−2s²)G′−(1/2+s)G. Eliminating F gives (1−4s²)G″−8sG′−G=0 and proves the formula. For every prime p≡3mod4, coefficient degreep+1 has valuation−1: numerator factors lie below2p and exclude the only possible multiplep, denominator(p+1)! has valuation1. This proves infinitely many denominator primes and failure of omega(p)-integrality for an actual CM splitting with h=0.

Lam–Litt arXiv2501.13175v1, submitted22January2025, manuscript24January2025, complete93-page PDF opened/downloaded; primary abstract page confirms onlyv1 currently listed. Theorem4.1.1p21 and proofp24 read. It applies to every nonzero algebraic initial vector in positive Sym^n H1 of the nonisotrivial Legendre family, after choosing R=O_K[1/N] containing all data and makingt0,1−t0 units. The exact relation to h is horizontal continuation of ξ+hω in the Betti trivialization, obtained by freezing the antiholomorphic coordinate in the real-analytic Hodge vector. Algebraic initial data do not imply integral jets; the explicit CM example proves this directly. The adjacent Proposition4.0.1 omits a nonzero initial-value hypothesis (zero gives a trivial exception); we use the properly stated Theorem4.1.1 instead. No general conjecture from the source is used.

## 29. The Gaussian-invariant division-polynomial map

**A.4.29 (proved).** For every complex a and θ_a=e^(−au²/2)σ, the normalized division polynomial is F_n(P(u))=σ(nu)/σ(u)^(n²)=θ_a(nu)/θ_a(u)^(n²). The quotient is elliptic by sigma automorphy, has divisor[n]*O−n²O and leadingn u^(1−n²), uniquely fixing the stated rational normalization. The Gaussian cancellation is a formal characteristic-zero identity, hence also valid p-adically. Likewise η^(a)(u0)=η(u0)−a u0 gives exp(−η^(a)(u0)u0/2)θ_a(u0)=exp(−η(u0)u0/2)σ(u0). Thus the map a↦all division-polynomial quotients and normalized torsion constants is constant, an actual noninjective map. This says exactly what those data retain; it is not a categorical claim excluding any application through a different construction with additional data.

Primary Katagiri–Kobayashi arXiv2609.07024v1,7September2026, complete17-page primary PDF downloaded successfully despite web retrieval DisabledError. Text read at normalizationp2; Theorem1.3/Cor1.4pp3–4; Definition2.3,Prop2.5,Thm2.7pp6–7; proofp8. Its ordinary/supersingular p-power subsequential limits are expressed in the algebraic sigma constant appearing above, so these inspected limits preserve the Gaussian ambiguity. The exact complex reduced parameter a=h is not recovered by this map. H1 remains unchanged.

A.4.27–29 were integrated into the paper after checkpoint03. Their exact symbolic checks and eight CM prime-valuation samples are in `check_arithmetic_continuation.py` and `.out`, copied into the deliverable code directory. The infinite proofs are supplied independently of the finite samples. The CDT2024 primary arXiv metadata was opened and confirms version2,16September2024; the consulted author-hosted218-page manuscript has the same length.
''')
with Path('work/agent_elliptic_check_events.tsv').open('a') as f:
    rows=[
      ('A.4.27','independent re-proof','Algebraic derivative expansion gives explicit G-function ODE and denominator (4C)^(n+1)lcm(1,...,n); exact uniformization and nonzero h-monodromy computed.'),
      ('A.4.27','used and rechecked in this run','CDT2024 complete218pp primary manuscript Thm2.5.1pp16-17 read; strict conformal-radius and denominator hypotheses retained. ICM2026 primary article also opened.'),
      ('A.4.28','independent re-proof','Exact Legendre connection gives actual CM horizontal anti-Hodge vector at t=1/2; closed Taylor formula has valuation -1 at degree p+1 for every p=3mod4, proving infinitely many denominator primes.'),
      ('A.4.28','used and rechecked in this run','LamLitt2025v1 complete primary PDF Thm4.1.1p21 and proofp24 read; nonzero initial vector, smooth nonisotrivial family, and integrality hypotheses explicitly verified.'),
      ('A.4.29','targeted proof check','Gaussian cancellation and divisor/leading-term uniqueness identify the constant map from correction parameter to all division quotients and normalized torsion constants.'),
      ('A.4.29','used and rechecked in this run','KatagiriKobayashi2026v1 complete primary download17pp read: normalizationp2, Thm1.3/Cor1.4pp3-4, Definition2.3/Prop2.5/Thm2.7pp6-7.')]
    for sid,kind,out in rows:
        f.write('\t'.join((sid,'2026-11-19','OpenAI GPT-6 Astra; effort inherited; elliptic_splitting',kind,out))+'\n')
    for sid in ('A.4.27','A.4.28','A.4.29'):
        f.write('\t'.join((sid,'2026-11-19','OpenAI GPT-6 Astra; effort inherited; elliptic_splitting','computation or formal certificate','check_arithmetic_continuation.py verifies primitive ODE, Gauss-Manin reduction, horizontal CM series and eight exact prime valuations, plus Gaussian division/torsion cancellation; source/output copied.'))+'\n')
print('Appended A.4.27--29, bibliographies, source records, and check events.')
