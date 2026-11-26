# An Erdős–Straus divisor weight on the mixed sextic prime and composite sums

The finite-order Eisenstein Hecke character \(\xi=\psi\lambda_+\), its degree-two induction \(V\), and the prime coefficients \(a(p)\) are those of `SEXTIC_ROUGH_AUDIT.md`. All prime factors below are good, meaning prime to \(2\cdot3\cdot269\). Fix a positive \(R\equiv3\bmod4\), and let
\[
 M_D(n)=\#\{1\le u,v\le D:(u,v)=(uv,4R)=1,\quad
       u\equiv1,\ v\equiv-1\bmod R,\quad uv\mid n+R\}.
\]
The pairs are ordered. Set \(z=(\log y)^2\) and fix a reduced residue class \(b_0\bmod m_0\). The following result also allows any one of the six fixed hard classes modulo 840.

**Claim.** On \(y<n\le2y,\ n\equiv b_0\bmod m_0\), give the allowed primes weight \(M_D(n)\Re a(n)\log n\), and give each good squarefree composite with all prime factors above \(z\) weight
\(M_D(n)\Re(\prod_{p\mid n}a(p))\log n\). The prime sum plus the composite sum is
\[
         O_{\xi,\epsilon}\bigl(D^2y^{1/2+\epsilon}\bigr)
\]
for every \(\epsilon>0\) and all sufficiently large \(y\). The estimate is uniform in the reduced class and modulus. In particular, for \(D=y^{o(1)}\) the error is \(O_{\xi,\epsilon}(y^{1/2+\epsilon})\). This joint estimate relates the fluctuations of the two marked sums. It imposes no bound of this order on either separately.

## A uniform norm-progression estimate

Write \(A(n)=\sum_{N\mathfrak a=n}\xi(\mathfrak a)\) with the fixed bad Euler factors deleted. For every \(m\ge1\) and \((b,m)=1\),
\[
  \sum_{\substack{n\le X\\ n\equiv b\bmod m}} A(n)
      \ll_{\xi,\epsilon} X^{1/2+\epsilon},\qquad X\ge1 . \tag{1}
\]
Here is a direct proof which also covers \(269\mid m\). Class number one expresses the ideal sum as a sum on the Eisenstein lattice divided by six. Fix a rational integer \(C\) divisible enough at \(2,3,269\) that the incomplete ray value on a generator, including the zero extension, is periodic modulo \(C\mathcal O_E\). The congruence on its norm and this ray weight together are periodic modulo \(Cm\mathcal O_E\).

Every full residue tile has zero weighted sum. In \((\mathcal O_E/Cm)^\times\) take \(t\) equal to \(1\) on the prime-power components away from 269 and reducing to a residue with \(\psi(t)\ne1\) at the inert prime 269. Existence follows from the finite Chinese remainder theorem, unit lifting, and the nontrivial cubic character on \(\mathbb F_{269^2}^{\times}\). The field \(E(\sqrt{2\sqrt{-3}})\) is unramified at 269, and its associated ray character has conductor supported above 2 and 3. The unit \(h=t/\bar t\) has norm one modulo \(Cm\), \(\lambda_+(h)=1\), and \(\psi(h)=\psi(t)^2\ne1\). Multiplication by \(h\) permutes the exact norm fibre without changing any excluded-prime condition and multiplies the weight by a fixed nontrivial root of unity. This proves cancellation also when the two moduli share the prime 269. All weights are unchanged under the six global units.

For \(m\le\sqrt X\), a disk of norm radius \(X\) meets \(O_C(\sqrt X/m+1)\) boundary tiles; its Euclidean radius is \(\sqrt X\). Each boundary tile contains at most \(C^2\) representatives for each residue modulo \(m\) with \(N\gamma=b\). The number of such residues is
\[
         \ll m\prod_{p\mid m}(1+1/p)\ll m(1+\log(2m)). \tag{2}
\]
To check (2), at a split \(p^k\) the fibre size is \(\varphi(p^k)\). At an inert \(p^k\) it is \(p^{k-1}(p+1)\). Indeed the finite-field norm is onto at \(k=1\), and each lift of a unit norm to the next power is possible because the residue-field trace \(x\mapsto\mathrm{Tr}(x)\) is onto in the linearized norm equation for \(1+p^k x\). This includes the inert prime 2. At the ramified prime 3 the image of the norm on residue units contains the squares of rational units. There are \(\varphi(3^k)/2\) such squares, so each nonempty fibre has at most \(2\cdot3^k\) elements. Multiply by the Chinese remainder theorem and bound \(\prod_{p\mid m}(1+1/p)\) by the harmonic sum over positive divisors of \(m\). The total boundary error is \(O_C(\sqrt X\log(2X))\) when \(m\le\sqrt X\).

If \(m>\sqrt X\), at most \(1+X/m\) possible integer norms occur. Each has at most \(\tau(n)\ll_\epsilon n^\epsilon\) ideals, by elementary prime splitting in a quadratic field. This proves (1) uniformly in the remaining range. Even the coarser bound \(O_\xi(m\sqrt X)\) suffices for a subpower choice of \(D\); (2) removes the modulus loss in (1).

## Application to the weights

Use \(F_z=L^{\rm good}(s,V)H_z\) and the estimate \(\sum_{d\le X}|h_z(d)|/\sqrt d\ll(\log(2X))^C\exp(C\sqrt z/\log(2z))\) from the unweighted proof. On a reduced residue class \(b\bmod m\), divisors \(d\) sharing a prime with \(m\) cannot contribute. For each remaining divisor the complementary sum is in the reduced class \(bd^{-1}\bmod m\), so (1) bounds the squarefree coefficient sum uniformly in \(m\) by
\[
 X^{1/2+\epsilon}\sum_{d\le X}|h_z(d)|/\sqrt d .
\]
Freeze \(z=(\log y)^2\) as \(X\) varies in the dyadic interval. Partial summation inserts \(\log n\); the Euler correction and the logarithm cost \(y^{o(1)}\). Starting (1) with a smaller positive exponent therefore gives \(O_{\xi,\epsilon}(y^{1/2+\epsilon})\) for the log-weighted sum on each reduced progression.

For each admissible \((u,v)\), combine \(n\equiv b_0\bmod m_0\) with \(n\equiv-R\bmod uv\). There is either no solution or a single class modulo \(\operatorname{lcm}(m_0,uv)\); that class is reduced, because \(b_0\) is reduced and \((uv,R)=1\). Sum the uniform bound over at most \(D^2\) ordered pairs. The prime and composite pieces partition the resulting squarefree sum. Its real part gives the claim. In a composite term prime factors congruent to \(7\bmod12\) can occur in pairs; the real part is taken after multiplying, as in the unweighted identity.

## Why the prime marks count actual Type II decompositions

For a prime \(p\equiv1\bmod12\) with \(p>R\), write \(a=(p+R)/4\) and \(S=pa\). Since \((uv,4)=1\), the congruence \(uv\mid p+R\) implies \(uv\mid a\). Also \(R\mid u+v\). Thus
\[
       H=\frac{pa}{uv}\,\frac{u+v}{R},\qquad
       b=Hu,\qquad c=Hv
\]
are positive integers, with \(p\mid H\). They satisfy \(1/b+1/c=R/(pa)\), so \(1/a+1/b+1/c=4/p\). Exactly two denominators are divisible by \(p\); indeed \(p\nmid a\). The ratio \(b:c=u:v\) is already reduced, so each admissible ordered mark has a different ordered denominator pair. These marks give a lower bound on the shell's decompositions. The marking congruences retain only selected divisor pairs.

For \(R=3\), \((u,v)=(1,11)\), and \(p\equiv1\bmod840\), the extra progression is \(p\equiv8401\bmod9240\). At \(D=11\) it gives exactly one mark throughout this progression. The possible \(u\) are 1 and 7, and the possible \(v\) are 5 and 11. Neither 5 nor 7 divides \(p+3\), while 11 does. The mark gives
\[
      (a,b,c)=\left((p+3)/4,\quad p(p+3)/11,\quad p(p+3)\right).
\]
All four mixed quartic/cubic Frobenius sectors have positive prime density even after imposing that extra progression. In the previously identified Galois compositum the commutator is the relative \(C_6\) over \(K\), and hence its maximal abelian subfield is \(K\). The cyclotomic field of 9240 contains \(K\), and the selected residue class restricts trivially to \(K\). Chebotarev in the fibre product gives the four relative frequencies \(1/6,1/6,1/3,1/3\), conditionally on the selected progression, in the order \((+,2),(-,2),(+,-1),(-,-1)\). The following individual primes give exact examples:

| Quartic sign | Cubic trace | Prime |
|---:|---:|---:|
| \(+1\) | \(2\) | 45,361 |
| \(-1\) | \(2\) | 451,921 |
| \(+1\) | \(-1\) | 63,841 |
| \(-1\) | \(-1\) | 26,881 |

`check_sextic_shell_weight.py` verifies primality, the two residue symbols, all four rational decompositions, 58 additional distinct ordered marks, and the reduced local norm-fibre counts for prime powers including \(3^4\), \(2^5\) and 269. The Chebotarev assertion uses the fixed progression; it makes no uniform density assertion as the cutoff \(D\) grows. The weighted estimate and the Type II identity use no RH.
