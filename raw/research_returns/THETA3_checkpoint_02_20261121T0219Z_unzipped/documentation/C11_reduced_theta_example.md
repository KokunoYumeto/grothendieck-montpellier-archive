### C11: an actual normalized reduced theta need not be integral

The frame issue occurs for the usual normalized reduced theta, not only for an artificially chosen generic frame. Let E:y²=x³−x, omega=dx/(2y), and t=−x/y. The curve has good supersingular reduction at p=7; after y is replaced by2y this is exactly Bannai–Kobayashi arXiv:math/0610163v4 §4 pp49–50's example y²=4x³−4x. Their Example1.9 pp10–11 defines reduced theta theta(z)=exp(−e2* z²/2)sigma(z), theta'(0)=1. The square-lattice CM symmetry gives e2*=0, also explicitly recorded in their Figure1 p49. Thus theta=sigma for this algebraic differential normalization.

From t²=x/(x²−1) one gets x=(1+sqrt(1+4t⁴))/(2t²), y=−x/t, and hence

    omega=(1+4t⁴)^(-1/2)dt,
    lambda(t)=t−2t⁵/5+2t⁹/3+O(t¹³).

For the corresponding Weierstrass function, wp''=6wp²−2 gives

    wp(z)=z^(−2)+z²/5+z⁶/75+O(z¹⁰).

Using (log sigma)''=−wp and sigma'(0)=1 gives

    log(sigma(z)/z)=−z⁴/60−z⁸/4200+O(z¹²),
    sigma(z)=z−z⁵/60−z⁹/10080+O(z¹³).

Therefore exact composition yields

    theta(lambda(t))=t−5t⁵/12+1411t⁹/2016+O(t¹³).

Since2016=7*288 and7 does not divide1411, the t⁹ coefficient has7-adic valuation−1. Thus this actual normalized reduced-theta coefficient function is not integral at a good supersingular prime. The elementary computation uses no claim about an asymptotic radius of convergence. It shows that canonical analytic reducedness does not supply C11's integral-frame hypothesis. It does not contradict the accepted asymptotic statement in Alpöge's step2; identifying its theta and normalization remains a separate comparison.

The exact finite-series calculation is independently reproduced by `work/check_reduced_theta.py`, with output at `work/check_reduced_theta_output.txt`. The calculation is rational symbolic verification, not a Lean proof.
