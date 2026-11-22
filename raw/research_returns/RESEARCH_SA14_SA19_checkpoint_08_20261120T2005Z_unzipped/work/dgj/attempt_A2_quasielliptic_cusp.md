# The quasi-elliptic cusp construction is excluded

**Status: proved numerical exclusion, submitted for independent review; not an A2 solution.**

Proposed route: a smooth quasi-elliptic surface f:S->C could have a smooth cusp multisection D->C of purely inseparable degree p. Pullback along that map kills suitable p-torsion from Pic(C). A Jacobian model has a zero section disjoint from D, but perhaps a non-Jacobian twist removes this obstruction. The following numerical argument rules out ampleness anyway when g(C)>=1.

Assume first that S is relatively minimal. The canonical bundle formula is

omega_S = f^*(omega_C tensor L^dual) tensor O_S(sum a_i P_i),

with R^1 f_*O_S=L directsum T, coefficients a_i>=0, and

deg(omega_C tensor L^dual)=2g-2+chi(O_S)+length(T).

For a smooth integral purely inseparable multisection D->C of degree r>=2, the two curves have the same genus g: over the perfect algebraically closed ground field the extension of one-variable function fields is a Frobenius extension (possibly iterated). Since D is horizontal, its intersection with every effective fibre component is nonnegative. Therefore

K_S.D >= r(2g-2+chi(O_S)).

For a quasi-elliptic surface, chi(O_S)>=(1-g)/3. Adjunction now gives

D^2 = 2g-2-K_S.D <= (2-5r/3)(g-1).

This is nonpositive for g>=1 and r>=2, so D cannot be ample. For a nonminimal smooth S, contract the vertical (-1)-curves to its relatively minimal model. The canonical class changes by an effective exceptional divisor; its intersection with horizontal D is nonnegative, while chi is unchanged, so the same inequality holds. Smoothness of D matters: replacing it by a singular cusp curve would introduce the arithmetic-genus defect.

In the intended cusp route r=p. If g=0, Pic(C)[p](k)=0, so no nontrivial class from the base exists. Thus the route fails in every case relevant to a nonzero pulled-back class, even for a non-Jacobian surface.

Primary sources opened:

- Christian Liedtke, *Algebraic Surfaces in Positive Characteristic*, arXiv0912.4291v4 (6April2013), Theorem5.6 pp23–24: canonical bundle formula, including nonnegative multiple-fibre coefficients and the torsion contribution. https://arxiv.org/pdf/0912.4291
- Toshiyuki Katsura and Natsuo Saito, *On the multicanonical systems of quasi-elliptic surfaces*, J.Math.Soc.Japan73(2021),1253–1261, p1255 after Proposition2.1: Alb(S)=J(C) and chi(O_S)>=(1-g)/3. https://www.jstage.jst.go.jp/article/jmath/73/4/73_1253/_pdf/-char/en
- William E.Lang, *Quasi-elliptic surfaces in characteristic three*, Ann.Sci.ENS(4)12(1979),473–500, Section2 Proposition2.1 p481 records the degree-p cusp multisection intersection with the general fibre. https://www.numdam.org/item/10.24033/asens.1373.pdf

No general assertion about arbitrary A2 pairs is derived. This is a closed construction route only.
