# A cubic cover on the signed twistor charts and its arithmetic fibers

Put \(a=269\), \(R=\mathbb Z[1/(3a)]\), \(\alpha^3=a\), \(F=\mathbb Q(\alpha)\), \(K=\mathbb Q(\omega)\) for a primitive cube root of unity \(\omega\), and \(E=FK\). Write \(\rho\) for the sum-zero representation on the three cube roots. There are three constructions with different base spaces: the cubic map on a signed twistor chart, its specialization at an arithmetic parameter, and commuting lifts of rational Frobenius on a fixed arithmetic fiber. The first two give actual geometric realizations of the cubic representation.

## 1. Cubing on the actual signed charts

In the two affine charts of Connes and Consani, send the spatial generator \(T\) (respectively \(T^{-1}\)) to its cube and fix \(J_\pm\) and \(\epsilon\). This respects \(J_\pm^2=\epsilon\) and \(J_-\mapsto \epsilon J\) on the overlap. On the generic chart the folding involution sends \(T\mapsto\epsilon T^{-1}\), \(J\mapsto J^{-1}\). Since \(\epsilon^3=\epsilon\), cubing the spatial coordinate commutes with the fold. It also commutes with every odd power operation on the generators. Thus it induces an equivariant self-map on the archimedean chart and its fold. In the displayed fiber-product definition of the sheaf on the global amalgam, its restriction to the common base fixes every element of \(\mathbf F_{1^2}\). Paired with the identity on the finite component it therefore gives the map on sections by acting componentwise. This gluing acts as the identity at the finite primes. It does not construct the desired arithmetic covering at those primes. [Connes–Consani, equations (9)–(13), Definition 7.1 and Proposition 7.5](https://arxiv.org/html/2609.00299v1)

On complex points the map is \(\pi(y)=y^3\). It differs from the authors' odd Frobenius at \(n=3\), which also acts on \(J\). Write \(\chi_4(n)=(-1)^{(n-1)/2}\) for odd \(n\). Proposition 7.5 gives
\[
 F_n(y)=\chi_4(n)y^{n\chi_4(n)},\qquad \sigma(y)=-1/\bar y .
\]
Consequently \(\pi F_n=F_n\pi\) and \(\pi\sigma=\sigma\pi\) on the entire sphere. On the punctured torus \(y\ne 0,\infty\), the three sheets have rotations \(r_\zeta(y)=\zeta y\), \(\zeta^3=1\). Calculation gives
\[
 F_n(r_\zeta y)=r_{\zeta^{n\chi_4(n)}}F_n(y),
 \qquad \sigma(r_\zeta y)=r_\zeta\sigma(y).
\]
The minus sign in the Frobenius for \(n\equiv3\bmod4\) changes which cubic character is transported.

| \(n\bmod12\) | Action on the three-point geometric fiber sent to the new fiber | Action on the two nontrivial cubic character lines |
|---|---|---|
| 1, 11 | bijective, deck rotation preserved | each line preserved |
| 5, 7 | bijective, deck rotation inverted | lines interchanged |
| 3, 9 | all three points have the same image | pullback on functions modulo constants is zero |

These assertions concern complex fibers, or the displayed torus and its three distinct roots in characteristic different from three. On functions, pullback always preserves constants. At \(3\mid n\) it can send a sum-zero function to a nonzero constant, so the zero assertion is on the quotient by constants, equivalently after projection back to the augmentation subspace. At the branch points \(0,\infty\) there is no étale three-sheet permutation fiber. The holomorphic rotations give cyclic geometric monodromy on the complex torus. Arithmetic conjugation before folding and the signed real structure after folding are different operations.

## 2. Honest arithmetic pushforward

The ordinary map of tori \(y^3=u\) over \(R\) is finite étale of degree three since \(y\) and \(3\) are units. At \(u=a\) its fiber has coordinate ring \(A=R[X]/(X^3-a)\). Its splitting cover has coordinate ring \(B=R[\omega,\alpha]\). Adjoining \(\omega\) and then \(\alpha\) gives finite étale extensions of degrees two and three. The connected generic field of the latter is \(E\). The cubic is Eisenstein at \(a\), has discriminant \(-27a^2\), and its nonsquare discriminant gives \(S_3\). Explicit generators are \(r(\alpha)=\omega\alpha,\ r(\omega)=\omega\) and \(c(\alpha)=\alpha,\ c(\omega)=\omega^{-1}\); thus \(crc=r^{-1}\). The degree-six connected cover is Galois with this group. The degree-three cover itself has this monodromy and trivial deck group. This distinction also follows from the stabilizer of a point in the three-letter action. [Stacks Project, Galois covers](https://stacks.math.columbia.edu/tag/03SF)

Over rational coefficient vector spaces, the direct image of the constant sheaf along the degree-three map has geometric stalk the permutation representation
\[
 \mathbf 1\oplus \rho .
\]
The two projections use the sum of the entries and their average. This degree is minimum for realizing \(\rho\) as a summand of a direct image of constants: every permutation action on at most two letters has abelian image, whereas \(\rho\) is faithful on \(S_3\). Trivializing \(\rho\) requires the degree-six splitting cover at minimum because its image has order six. With nonconstant rank-one coefficients, degree two instead suffices after extending the coefficient field to contain \(\omega\): over \(K\) the cubic character \(\theta\) of \(E/K\) induces \(\rho\) to \(\mathbb Q\). These are distinct minimality statements.

### The Gaussian folded orbit

There is an explicit rational form of the complex coordinate and the sign action in §1. Over \(\mathbb Q(i)\) descend the projective line by \(z\mapsto-1/\bar z\). A rational model is the conic \(C:X^2+Y^2+Z^2=0\) with \(z=(X+iY)/Z\). On \(Z\ne0\) one has \((X-iY)/Z=-1/z\). The cubic endomorphism descends explicitly as
\[
 [X:Y:Z]\longmapsto
 [X^3-3XY^2:3X^2Y-Y^3:Z^3].
\]
Indeed the first two coordinates are the real and imaginary polynomial components of \((X+iY)^3\), and their sum of squares is \((X^2+Y^2)^3=-Z^6\). On the complex torus this induces \(z\mapsto z^3\). This classical conic models the stated real structure. It makes no assumption identifying an entire spherical topos with the category of schemes over this conic.

The conic has no real point. A rational angular coordinate \(z=a\) on the split chart therefore does not give a rational point on \(C\). It gives a closed point of degree two, represented by
\[
 [a^2-1:-i(a^2+1):2a]
\]
and its conjugate, with split coordinates \(a\) and \(-1/a\). Its residue field is \(\mathbb Q(i)\), since \(a\ne0\) and \(a^2+1\ne0\). The inverse image under cubing has residue field \(\mathbb Q(i,\alpha)\). Indeed over \(\mathbb Q(i)\) the three roots above \(a\) are those of \(X^3-a\); this polynomial is irreducible there since \(F/\mathbb Q\) is cubic, \(E\cap\mathbb Q(i)=\mathbb Q\), and the \(S_3\) root action remains transitive. The latter intersection follows because \(K\) is the unique quadratic subfield of \(E\) and \(K\ne\mathbb Q(i)\).

Let \(\chi_{-4}\) denote the Gaussian quadratic character. As a representation of the rational Galois group the permutation sheaf of this degree-six point is
\[
 \operatorname{Ind}_{G_{\mathbb Q(i)}}^{G_{\mathbb Q}}
         \operatorname{Res}_{G_{\mathbb Q(i)}}^{G_{\mathbb Q}}(\mathbf1\oplus\rho)
 =(\mathbf1\oplus\rho)\otimes(\mathbf1\oplus\chi_{-4}).
\]
Thus the folded specialization supplies both \(\rho\) and \(\rho\otimes\chi_{-4}\). The nonabelian monodromy comes from the arithmetic fiber. A Gaussian sign character on its own supplies neither. This formula implies a quick check at good primes: the trace on all six letters is \((1+\chi_{-4}(p))\#\{x\in\mathbb F_p:x^3=a\}\).

Over \(U'=\operatorname{Spec}\mathbb Z[1/(6a)]\), the normalized Gaussian parameter \(\operatorname{Spec}\mathbb Z[i,1/(6a)]\) is finite étale; the pullback along that parameter is finite étale and has generic field \(\mathbb Q(i,\alpha)\). Calling its parameter an embedded étale degree-two subscheme requires two additional exclusions. The conjugate sections meet where \(a=-1/a\bmod p\). Here \(a^2+1=2\cdot97\cdot373\). Thus on \(U'\) one must also delete \(97,373\) to keep the two sections disjoint on every geometric fiber. At these two primes the normalized degree-two parameter still maps to the conic and still has an étale pullback from the punctured cubic map. The scheme-theoretic image in the conic has a collision of its sections. Inverting \(2\) is specific to the Gaussian étale parameter; the ordinary degree-three cover over \(R\) includes its good fiber at \(2\).

### A rational quotient that isolates the cubic

There is a positive descent step which recovers \(\rho\) separately from its Gaussian twist. The involution \(J_0(z)=-1/z\) commutes with \(\sigma\), with spatial cubing, and with every \(F_n\) for odd \(n\). This is the holomorphic involution on the classical conic, distinct from the imaginary chart generator \(J_\pm\). Its quotient coordinate \(r=z-z^{-1}\) satisfies
\[
 r(J_0z)=r(z),\qquad r(\sigma z)=\overline{r(z)} .
\]
It is therefore a rational coordinate on the quotient. On the conic it is \(2X/Z\); the quotient involution sends \(Y\) to \(-Y\). For every odd \(n\), both signs in the signed map give the same formula
\[
 r(F_n z)=z^n-z^{-n}=D_n(r,-1).
\]
The Dickson polynomial here is defined by \(D_0=2,\ D_1=r,\ D_{n+2}=rD_{n+1}+D_n\); its two auxiliary roots are \(z\) and \(-z^{-1}\). The odd operations commute under composition. For an odd prime \(p\), the identity reduces to \(D_p(r,-1)\equiv r^p\bmod p\), since \((z-z^{-1})^p=z^p-z^{-p}\) in characteristic \(p\), and substitution of the transcendental \(z-z^{-1}\) is injective.

In particular the spatial cubic on the quotient is \(D_3(r,-1)=r^3+3r\). Set \(r_0=a-a^{-1}\). In the fiber over this single rational point put \(x^3=a\) and \(r=x-x^{-1}\). Then
\[
 r^3+3r=r_0,\qquad x^2=rx+1,\qquad
 x=\frac{a-r}{r^2+1}.
\]
The denominator cannot vanish in characteristic zero for this fiber: \(r^2=-1\) would force \(a=r\) by the middle identity and \(x^3=a\). These formulas give \(\mathbb Q[r]/(r^3+3r-r_0)\cong F\). Hence the reduced degree-zero cohomology of this ordinary rational cubic fiber is precisely \(\rho\). On the six points upstairs, \(J_0\) interchanges the Gaussian sheets. Each pair has the same value of \(r\). The invariant projector \((1+J_0)/2\) selects \(\mathbf1\oplus\rho\); the other projector selects \(\chi_{-4}\oplus(\rho\otimes\chi_{-4})\). This construction retains the nonabelian character through the signed quotient. It acts on the family, and \(r_0\) itself is not a characteristic-zero fixed point of the odd Frobenius monoid.

The quotient also explains the two exceptional odd primes arithmetically. For the three conjugate roots \(x_i\),
\[
 \frac{(x_i-x_i^{-1})-(x_j-x_j^{-1})}{x_i-x_j}
    =1+\frac1{x_ix_j}.
\]
The product over the three pairs is \(1+a^{-2}\), since \(1/(x_ix_j)=x_k/a\) for the remaining root. This is the power-basis determinant for the order generated by \(r\) within the one generated by \(x\). Over \(\mathbb Z[1/(6a)]\) the latter is finite étale and normal. Consequently the local order index is exactly \(97\) at \(97\) and \(373\) at \(373\). The two discriminants are \(-27a^2\) and \(-27(a+a^{-1})^2\). At either prime \(a^2=-1\), \(p\equiv1\bmod3\), and \((-a)^3=a\), so the normalized cubic splits completely. The quotient polynomial instead reduces to \((r-a)^2(r+2a)\). Counting its distinct residue roots would give an incorrect local Artin factor at precisely these extra primes. Normalizing removes this error.

The determinant has a uniform odd-degree form. For odd \(n\) take the \(n\) roots \(x_j=\beta\zeta_n^j,\ \beta^n=a\) in characteristic zero. Among unordered pairs \(i\ne j\), each residue \(i+j\bmod n\) occurs \((n-1)/2\) times. Multiplying the pairwise ratios above gives \((1+a^{-2})^{(n-1)/2}\). Thus the change \(r=x-x^{-1}\) identifies the finite algebras of the two fibers \(x^n=a\) and \(D_n(r,-1)=a-a^{-1}\) over \(\mathbb Z[1/(a(a^2+1))]\). This statement uses a finite free algebra and does not require \(n\) to be a unit. Étaleness additionally requires the residue characteristic to be prime to \(n\).

### Classification of the finite invariant parameter sets

The preceding obstruction has a converse at the level of this explicit map. In characteristic zero a point \(r\) of the quotient affine line has finite orbit under the odd Dickson monoid if and only if \(r=z-z^{-1}\) for a root of unity \(z\). One implication follows at once from taking odd powers. For the other, finite orbit under \(D_3\) gives \(r(z^{3^i})=r(z^{3^j})\) for some \(j>i\), using any lift \(z\ne0\). The two solutions of \(x-x^{-1}=r(w)\) are \(w\) and \(-1/w\), counted with multiplicity. Thus either \(z^{3^j-3^i}=1\) or \(z^{3^j+3^i}=-1\); each forces \(z\) to be torsion. The same argument works when only exponents prime to six are allowed, by using the iterates of \(5\). The only simultaneous affine fixed point in characteristic zero is \(r=0\), because \(D_3(r)-r=r(r^2+2)\) and \(D_5(r)-r=r(r^2+1)(r^2+4)\). The point at infinity is also fixed on the projective quotient.

Every geometric point in the inverse cubic fiber over a finite-orbit parameter therefore has cyclotomic coordinates: take third roots of the corresponding roots of unity and apply \(x\mapsto x-x^{-1}\). For a finite Galois-stable collection of such parameters, one cyclotomic field contains the entire collection and all its inverse images. Its permutation action factors through an abelian group. This proves within this concrete construction why trying a larger *finite* invariant orbit cannot recover the nonabelian cubic. The parameter \(a-a^{-1}\) with \(a=269\) has infinite orbit, and its one arithmetic fiber already has the desired monodromy. The statement concerns geometric points and the reduced fibers; it imposes no conjectural restriction on unrelated signed objects.

## 3. The split zero records the cubic trace on the three sheets

Use precisely \(G(\mathbb Z)=\{\tau\}\sqcup\mathbb Z\) of the workshop, with \(\tau\) both the additive identity and multiplicative absorber. Denote the supported zero by \(e=0_{\mathbb Z}\), so \(e\ne\tau\), and let \(\epsilon=-1\) be supported. A permutation of the three geometric sheets gives a genuine matrix on the free \(G(\mathbb Z)\)-semimodule: a permutation entry has value \(1\), every missing entry has value \(\tau\). These matrices represent the entire nonabelian \(S_3\). If \(g\) acts on the sheets, write \(b_k\) for the diagonal trace of the matrix of \(g^k\). Then the split-zero amplitude \(v_k=\epsilon+b_k\) is supported and its ring value is \(\operatorname{tr}\rho(g^k)\).

| Permutation \(g^k\) | \(b_k\) in \(G(\mathbb Z)\) | \(v_k\) in \(G(\mathbb Z)\) | Ring value |
|---|---|---|---:|
| Identity | \(3\) | \(2\) | 2 |
| Transposition | \(1\) | \(e\) | 0 |
| Three-cycle | \(\tau\) | \(-1\) | −1 |

This computes a supported cancellation for a genuine cubic Artin local system. The quadratic sign twist multiplies \(v_k\) by \(\chi_{-4}(p)^k\) at a good prime. The Boolean character sends each \(v_k\), including \(e\), to one. The matrix-valued action or the supported amplitudes retain information that this scalar Boolean image loses. The sum-zero decomposition uses rational additive coefficients; the table is computed on the full split-zero permutation semimodule with one additional supported scalar. A semiring projector onto a rank-two free summand has not been presumed. The original definition is in Documents/math/work/claude_orientation_20260922/first_papers/split_zero_projective_monads_surcomplex.tex, lines 109–127.

## 4. Which Frobenius lifts the fixed fibers carry

For a good rational prime \(p\), a Frobenius lift on \(A\) means an \(R\)-algebra endomorphism reducing on the entire fiber modulo \(p\) to \(x\mapsto x^p\). Any such map on its generic field \(F\) is the identity: \(F\) is real and its other cubic roots are nonreal. The identity reduces to the required map precisely when each residue degree is one, namely precisely when \(p\) splits completely. Torsion-freeness then identifies the unique lift with the identity on \(A\). On the full Galois cover \(B\), a candidate automorphism would have to equal the Frobenius at every prime of \(E\) above \(p\). Indeed it must stabilize each prime above \(p\), and the finite étale hypothesis makes each decomposition group act faithfully on its residue field. Those Frobenius elements constitute one conjugacy class. They can all coincide exactly when they are central, and \(Z(S_3)=1\). So here too exactly the completely split rational primes have an individual lift, with unique lift the identity. In particular this particular fixed cover cannot have a family of lifts at all good odd rational primes. For example at \(p=13\), \(269^{4}\equiv9\bmod13\), so Frobenius is a three-cycle. At \(p=37\) the roots are \(7,33,34\), and the identity does lift.

Over \(K=\mathbb Q(\omega)\) the answer is positive. The cyclic cubic over \(\mathcal O_K[1/(3a)]\) has for each good prime ideal \(\mathfrak p\) a unique \(K\)-relative Frobenius lift. With \(q=N\mathfrak p\), the reduction of \(\mu_3\) is injective, and the multiplier is the unique \(\zeta_{\mathfrak p}\in\mu_3\) congruent to \(a^{(q-1)/3}\) modulo \(\mathfrak p\). The map fixes the base ring and sends \(\alpha\mapsto\zeta_{\mathfrak p}\alpha\). Its residue action is \(x\mapsto x^q\) on every component. The cyclic deck group ensures all such lifts commute. In particular the same cubic really has relative commuting Frobenius lifts over the Eisenstein base. Over \(\mathbb Q(i)\) the splitting group stays \(S_3\); the Gaussian sign base alone cannot create those relative cubic lifts. [Borger and de Smit, definitions of relative Frobenius and \(\Lambda\)-actions](https://arxiv.org/abs/1105.4662)

Finally a coordinate power map \(u\mapsto u^p\) is a Frobenius lift on the coordinate torus over \(\mathbb Z\) (fix the integer coefficients). It moves the characteristic-zero parameter \(a\) to \(a^p\); in the folded chart the image is \(F_p(a)\). Apart from the identity these leave the chosen Gaussian pair for \(a=269\). The square of covers in §1 therefore does not give an endomorphism of that fixed arithmetic fiber. One can realize nonabelian local monodromy, compute the exact Artin Euler factors, and produce the indicated Gaussian twist. An estimate on the distribution of the resulting Frobenius classes, or an interior purity theorem for their global \(L\)-function, requires further arithmetic input. The adelic-cover theorem of Connes and Consani takes finite **abelian** extensions of \(\mathbb Q\) as input. Its theorem therefore applies directly to \(K\) and \(\mathbb Q(i)\); extending it to the nonabelian splitting extension is a separate construction. [Connes–Consani, *Knots, primes and class field theory*](https://arxiv.org/abs/2501.06560)

