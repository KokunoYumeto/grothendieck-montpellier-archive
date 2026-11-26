# The mixed sextic character on rough squarefree integers

Put \(E=\mathbb Q(d)\), \(d=\sqrt{-3}\), \(K=E(i)\), and \(u=\sqrt[4]{3}>0\). Write \(\psi\) for a nontrivial Kummer character of \(E(\sqrt[3]{269})/E\) and \(\lambda_\pm\) for the quadratic characters of \(E(\sqrt{\pm2d})/E\). Let \(\xi=\psi\lambda_+\), \(V=\mathrm{Ind}_{E}^{\mathbb Q}\xi\), and \(a(p)=\mathrm{tr}\,V(\mathrm{Frob}_p)\) at \(p\nmid2\cdot3\cdot269\). Either choice of \(\psi\) gives the same real-part test. The following calculations use the uncompleted finite Euler products.

## Descent and determinant

Squaring \((1\pm i)u\) gives \(\pm2d\), after choosing \(d=i\sqrt3\). Both square roots produce \(K(u)\) after adjoining \(K\). Neither radicand is a square in \(E\), since its valuation at the prime above 3 is one. Their product is 12, representing the class \(-1\) in \(E^\times/E^{\times2}\); \(i\notin E\). Thus the two quadratic characters are distinct and \(\lambda_-=\lambda_+(\chi_{-4}\circ N_{E/\mathbb Q})\). They are exchanged by the conjugation \(\tau\) of \(E\). Conjugation inverts \(\psi\). The restriction to \(K\) of \(\xi\) is the mixed sextic character \(\theta\), and index-two induction gives
\[
 L_K(s,\theta)=L_E(s,\psi\lambda_+)L_E(s,\psi\lambda_-)
              =L(s,V)\,\overline{L(\overline s,V)} .
\]
These are entire nontrivial Hecke factors; deleting the finitely many local factors above \(2,3,269\) in prime sums or sieve identities affects no critical-strip zero. Specifically, their finite-image inverse local polynomials have roots of modulus one in \(p^{-s}\). For complete Artin factorization retain inertia invariants at the bad primes.

At a split rational prime \(p\), the two cubic Frobenius values are \(\psi(\mathfrak p)\) and its inverse. The product of the two \(\lambda_+\)-values is the product of the quadratic residue symbols of \(2d,-2d\), namely \((12/p)\). At a prime inert in \(E\), the prime coefficient of the induction is zero. The determinant there is \(-\xi((p))\), where \(\psi((p))=1\) since the lift of Frobenius has transposition image in the cubic splitting group and its square is trivial. For the quadratic value in \(\mathbb F_{p^2}\) the quadratic residue symbol of \(2d\) equals the Legendre symbol of its norm 12. This follows by writing \((p^2-1)/2=(p+1)(p-1)/2\). In both cases
\[
 \det V(\mathrm{Frob}_p)=\chi_{-3}(p)(12/p)=\chi_{-4}(p).
\]
For a two-dimensional unitary matrix this gives \(\overline {a(p)}=\chi_{-4}(p)a(p)\).

* For \(p\equiv1\bmod12\), \(i,d,\sqrt3\) are in \(\mathbb F_p\). Since \(2d=(1+i)^2\sqrt3\), the quadratic factor is \(v(p)=3^{(p-1)/4}\in\{\pm1\}\). Consequently \(a(p)=v(p)t(p)\), where \(t(p)=2\) for a cubic residue 269 and \(-1\) otherwise.
* For \(p\equiv7\bmod12\), the two quadratic values are opposite. Thus \(a(p)\) is zero or \(\pm(\omega-\omega^2)=\pm i\sqrt3\).
* For \(p\equiv2\bmod3\) the induced trace is zero.

For \(\Re s>1\), the negative logarithmic derivative of the product of the two Eisenstein-field factors therefore has first-prime weights \(2\Re a(p)\log p\). Their only nonzero terms have \(p\equiv1\bmod12\).

## The sieve and its sign

The finite-order Hecke character \(\xi\) is nontrivial of order six. The Eisenstein integers have class number one, so its ideal sums reduce to lattice sums over generators, divided by six. The values on generators are periodic modulo a fixed conductor and trivial on units. Extending by zero at nonunits yields a zero-mean periodic function since the nontrivial residue character has zero sum on the residue-unit group. For exclusion of bad primes one may enlarge the modulus and extend the character by zero, with the same proof. The norm sublevel set is a disk in the complex embedding. All complete residue tiles cancel, and the boundary meets \(O(1+\sqrt X)\) tiles. Thus the imprimitive Dirichlet coefficients \(A(n)\) of \(L(s,V)\) sum to \(O(\sqrt X)\) for this fixed field and character.

Put \(z=(\log y)^2\) and work on \(y<n\le2y\) with \(y\) sufficiently large. The product
\[
 F_z(s)=\prod_{\substack{p>z\\p\ {\rm good}}}(1+a(p)p^{-s})
 \quad=\quad L^{\rm good}(s,V)H_z(s)
\]
has squarefree, multiplicative coefficients \(f_z(n)=\prod_{p\mid n}a(p)\) on its allowed integers. At \(p>z\), with \(\delta=\chi_{-4}(p)\), the correcting polynomial in \(T=p^{-s}\) is
\[
 (1+aT)(1-aT+\delta T^2)=1+(\delta-a^2)T^2+a\delta T^3 .
\]
For \(p\le z\), the correction is \(1-aT+\delta T^2\) at good primes. Write \(h_z\) for the coefficients of \(H_z\). Using \(|a|\le2\), Chebyshev's bound and partial summation gives
\[
 \sum_{d\le X}\frac{|h_z(d)|}{\sqrt d}
 \ll \log^C(2X)\exp\!\left(C\frac{\sqrt z}{\log(2z)}\right).
\]
The linear term only enters for \(p\le z\). The first possible large-prime term contributes \(O(1/p)\) in this bound. Dirichlet convolution and the lattice estimate yield \(\sum_{n\le X}f_z(n)\ll\sqrt X\sum_{d\le X}|h_z(d)|/\sqrt d\). Holding \(z\) fixed while varying \(X\le2y\), partial summation on the dyadic interval gives the **complex** bound
\[
 \sum_{y<n\le2y} f_z(n)\log n\ll_\epsilon y^{1/2+\epsilon}.
\]
Take real parts. If \(P(y)=\sum_{y<p\le2y}\Re a(p)\log p\) and \(C(y)\) is the corresponding real-part sum on squarefree composites with at least two distinct good primes exceeding \(z\), then \(P(y)+C(y)=O_\epsilon(y^{1/2+\epsilon})\). For the induced \(K\)-character prime sum, use \(2P\) and \(2C\). An upper bound for the composite contribution corresponds to the lower bound for the prime contribution. This error respects the proposed sparse-window criterion with arbitrary positive exponent slack. It would not preserve an exact square-root limiting constant.

**The progression restriction is automatic on the product.** Every contributing prime factor is \(1\) or \(7\bmod12\), and \(\overline{f_z(n)}=\chi_{-4}(n)f_z(n)\). Terms with \(n\equiv7\bmod12\) have zero real part. For \(n\equiv1\bmod12\) there are an even number of \(7\bmod12\) factors and the full product is real. If there are \(2j\) such factors with nonzero \(a(p)=i\sqrt3\,\sigma_p\), their combined multiplier is \((-3)^j\prod\sigma_p\). Keeping only the real part of each prime coefficient before multiplying deletes genuine composite terms.

For example \(y=5000\) gives \(z\approx72.54\). The primes 79 and 103 both exceed \(z\), and their product 8137 belongs to the dyadic interval. Their trace product is \(+3\), although each real trace is zero. `verify_sextic_rough.py` evaluates the two independent residue symbols and checks determinant, conjugation, and the squarefree Euler convolution through 10,000. It verified every coefficient and all 1,226 good primes. This supplies a finite check of the formulas only.

## A rational twist cannot make the complete degree-two coefficient sequence real

Here “twist” means a fixed finite-order Dirichlet character \(\nu\). Restriction of \(V\) to \(G_E\) is \(\xi\oplus\xi^\tau\). Their quotient has order six: \(\xi^\tau/\xi=\psi^{-2}(\lambda_-/\lambda_+)\). It is conjugated to its inverse, so it cannot be the restriction of a Dirichlet character, which is invariant under conjugation. Therefore the only Dirichlet self-twists of \(V\) are the two trivial on \(G_E\), namely \(1,\chi_{-3}\). Both are indeed self-twists by index-two induction.

The determinant calculation gives \(V^\vee\simeq V\otimes\chi_{-4}\). If \(V\otimes\nu\) were self-dual, \(\nu^2\) would have to equal \(\chi_{-4}\) or \(\chi_{-4}\chi_{-3}=\chi_{12}\). Neither is a square of a Dirichlet character: evaluate at the element of \(\widehat{\mathbb Z}^{\times}\) which equals \(-1\) at 2 and \(1\) at every odd prime. It has order two, all squares evaluate to one there, and both target characters evaluate to \(-1\). Real traces on every good prime would imply self-duality by Chebotarev and equality of finite-group characters. Thus the passage to the real part of the full product, or to the pair of conjugate Hecke factors, is substantive.
