# The 270 Eisenstein directions for \(X^3-269\)

Let \(q=269\), \(\omega^2+\omega+1=0\), \(\mathcal O=\mathbb Z[\omega]\), and \(N(a+b\omega)=a^2-ab+b^2\). Because \(q\equiv2\bmod3\), it is inert and \(\mathcal O/q=\mathbb F_{q^2}\). Fix an identification of the three cube roots of unity in that field with their complex counterparts. Define \(\xi(\alpha)\) by lifting \(\alpha^{(q^2-1)/3}\) when \(q\nmid\alpha\), and by zero otherwise. Let \(w=\xi+\bar\xi\).

## Why a prime ideal gives the right direction

Cubing permutes \(\mathbb F_q^\times\). Hence \(\xi\) factors through \(\mathbb F_{q^2}^\times/\mathbb F_q^\times\), the cyclic group of order \(270\) underlying the projective line. Its kernel has order \(90\). Exactly 90 directions have \(w=2\) and 180 have \(w=-1\). Conjugation acts by inversion on the quotient and preserves \(w\). The units of \(\mathcal O\) are \(\{\pm1,\pm\omega,\pm\omega^2\}\). The rational signs are cubes, and \(\omega\) is a cube in \(\mathbb F_{q^2}^\times\) since \(9\mid q^2-1\). Thus \(\xi\) itself is independent of the choice of a generator of an ideal.

If \(p\ne3,q\) and \(p\equiv1\bmod3\), choose \(\pi\) above \(p\) primary, so \(\pi\equiv\pm1\bmod3\). The rational prime \(q\equiv-1\bmod3\) is primary in this convention. Cubic reciprocity gives \((q/\pi)_3=(\pi/q)_3\). If the adopted convention requires the residue \(+1\bmod3\), use \(-q\) and the \(+1\) associate of \(\pi\). The signs are cubes and all units disappear on the \(q\)-side. The cubic condition on the left is exactly solvability of \(x^3=269\bmod p\). Hence \(t(p)=w(\pi)\). Either prime over \(p\) works. This uses the reciprocity law, independently of any prime-equidistribution estimate. [Jori Merikoski, §2, Lemma 4](https://arxiv.org/abs/2012.05675)

There is also a direct local check at the exceptional primes. The relation \((1-\omega)^2=-3\omega\) implies \(\xi(1-\omega)=1\), since its square is one and its order divides three. In \(\mathbb Q_3\), \(269\equiv-1\bmod9\) is a cube: cubing maps \(1+3\mathbb Z_3\) onto \(1+9\mathbb Z_3\) by the 3-adic logarithm, and \(-1\) is a cube. At \(q\) the Kummer extension over \(\mathbb Q(\omega)\) is totally ramified by Eisenstein. These give the Hecke Euler factors \((1-3^{-s})^{-1}\) and \(1\) respectively.

## Cancellation before the primality condition

For every \(M\ge1\), every residue \(a\bmod M\) and \(L=\operatorname{lcm}(q,M)\),
\[
 \sum_{\substack{0<N\alpha\le X\\ N\alpha\equiv a\bmod M}}\xi(\alpha)
       =O\!\left(L\sqrt X+L^2\right).
\tag{1}
\]
The implied constant is absolute. To prove it, choose a unit \(v\) in \(\mathcal O/L\) which is noncubic modulo \(q\). Such a unit lifts by the Chinese remainder theorem from any noncube modulo \(q\), choosing a unit lift at each prime power. Let \(u=v/\bar v\) in this finite ring. Then \(Nu=1\) modulo \(L\) and \(\xi(u)=\xi(v)^2\ne1\), since conjugation acts on \(\mu_3\) by inversion. Multiplication by \(u\) permutes each fibre of the norm condition and multiplies its character sum by \(\xi(u)\); that sum must vanish. The same zero holds for \(w\). This argument includes \(q\mid M\) and non-unit norm classes.

Tile the complex plane by half-open fundamental parallelograms for \(L\mathcal O\), with edges \(L\) and \(L\omega\). Each contains exactly \(L^2\) lattice points. All complete cells in the disk of radius \(\sqrt X\) contribute zero. A cell crossing the boundary lies in the annulus with radii \(\max(0,\sqrt X-\sqrt3L)\) and \(\sqrt X+\sqrt3L\), since its diameter is \(\sqrt3L\). Divide the annular area by \(\sqrt3 L^2/2\) and multiply by the maximum cell weight \(L^2\). This gives (1), also for \(X<L^2\). The origin has character zero. Subtracting at \(X=y,2y\) gives the same order on dyadic norm shells.

## The exact extra term introduced by prime filtering

Write \(\xi(\mathfrak a)\) for the ideal character, possible because \(\mathcal O\) is Euclidean and the character kills all six units. Let \(A(n)=\sum_{N\mathfrak a=n}\xi(\mathfrak a)\). A full oriented lattice-shell sum of \(w\) equals \(12A(n)\): each ideal has six generators and conjugation makes the shell sum of \(\xi\) real. The integer Euler factor at \(p\equiv1\bmod3\) is \((1-t(p)p^{-s}+p^{-2s})^{-1}\). At an inert \(p\ne q\) it is \((1-p^{-2s})^{-1}\). Together with the two exceptional factors these give \(L(s,\rho)=\zeta_{\mathbb Q(\sqrt[3]{269})}(s)/\zeta(s)\).

Let \(\Lambda_\rho\) be the Dirichlet coefficients of \(-L'/L\), including all ramified factors. Ordinary Dirichlet convolution gives the exact identities
\[
    \Lambda_\rho*A=A\log,\qquad
    \Lambda_\rho=(A\log)*A^{-1},\qquad
    A^{-1}(n)=\sum_{N\mathfrak d=n}\mu_{\mathcal O}(\mathfrak d)\xi(\mathfrak d).
\tag{2}
\]
They follow by differentiating the absolutely convergent Dirichlet series and inverting its Euler product. In particular \(\Lambda_\rho(p)=t(p)\log p\) at good primes. The term that periodic-block cancellation does not handle is the ideal Möbius weight in \(A^{-1}\).

One can bound the short part of this inverse sum explicitly. Fix \(q,M\) and restrict to norm \(1\bmod M\). In (2), terms with \(N\mathfrak d\le D\le X\) contribute
\[
 O_{q,M}\big(\sqrt{XD}\log(2X)\big).
\tag{3}
\]
For a given \(\mathfrak d\) with norm prime to \(M\), the remaining ideal norm lies in the single residue class \((N\mathfrak d)^{-1}\bmod M\). Divide (1) by six and use partial summation to insert the log weight. This bounds the inner sum by \(O_{q,M}(\sqrt{X/N\mathfrak d}\log(2X))\) for \(N\mathfrak d\le X\). The number of ideals of norm at most \(D\) is \(O(D)\) by the same disk count without a character, so \(\sum_{N\mathfrak d\le D}(N\mathfrak d)^{-1/2}=O(\sqrt D)\). Ideals of noninvertible norm make no contribution to this residue class. The same argument gives (3) on the dyadic shell \(X<N\mathfrak a\le2X\) by subtraction.

Taking \(D\) to be a fixed power of \(\log X\) makes the short part small enough for the prime-window criterion. The longer Möbius-weighted contribution still needs control on those windows. Equations (1)–(3) prove unrestricted lattice cancellation and a short-divisor estimate. They do not give the prime estimate.

## Exact finite checks

`check_eisenstein_slopes.py` uses only the Python standard library. It verifies all 270 directions, the six unit actions and conjugation on every one of the 72,360 nonzero field elements, and all 268 nonzero norm fibres. Each such fibre has exactly 90 elements of each character value. It compares the lattice formula with direct modular cubic residuacity at all 247 split primes up to 3,600. It then checks (2) at all 3,599 integers from 2 to 3,600 by comparing the coefficients of each prime logarithm as integers.
