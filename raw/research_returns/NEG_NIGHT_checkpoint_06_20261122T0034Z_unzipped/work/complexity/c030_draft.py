"""NN-C030: deterministic smooth specialization from pairwise homogeneity."""

def append_c030(add,E,SGATRACE,VV):
    sga1={'source':'SGA1, ExposeII, Section4',
          'locator':'Theorem4.10(iii) and Corollary4.12, the homogeneous hypersurface Jacobian criterion used through NN-C024',
          'url':'https://grothendiecksga.com/read/sga1/fr/II-4.html'}
    weil={'source':'Deligne, La conjecture de Weil I, PMIHES43(1974),273--307',
          'locator':'Theorem1.6, printedp276, smooth projective finite-field purity',
          'url':'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf'}
    katz={'source':'Katz, Algebraic Solutions of Differential Equations, Invent.Math.18(1972),1--118',
          'locator':'Rank-one Special Case2.3.7.17, printedp36; exact Cech calculation supplied in NN-C023',
          'url':'https://web.math.princeton.edu/~nmk/old/algsoln.pdf'}
    inputs=[{'source':'NN-C023','locator':'incidence-rail factorization F=z0 P, with each rail pair of degree two and parity coefficient c'},
            {'source':'NN-C024','locator':'complete quadratic Artin--Schreier field-tower construction and semilinear-versus-q-linear Frobenius computation'},
            sga1,katz,SGATRACE,weil,VV,dict(E,locator='Theorem1.1, inherited original-formula evaluator')]
    add('NN-C030','NEG_NIGHT-03',
        'Pairwise homogeneity gives a deterministic smooth finite-field parity reduction',
r'''The randomized finite-field specialization in NN-C024 can be replaced by a deterministic polynomial-time construction on the actual incidence-rail encoding of NN-C023. Given a Boolean formula, construct a smooth projective hypersurface over an explicitly presented finite field $\mathbb F_{2^b}$, where $b=O(r^2)$ and its factored degree-$r$ equation has polynomial description length. The top coherent cohomology has its known one-dimensional basis, and its $2^b$-power Frobenius scalar is exactly the original satisfying-assignment parity $c$.

More precisely, let $r=2M+1\geq3$ and let
\[
 F=z_0P(z_{1,0},z_{1,1},\ldots,z_{M,0},z_{M,1})
\]
be nonzero over $\mathbb F_2$, with $P$ homogeneous of degree two in every displayed pair. Put
\[
 H=z_0^r+\sum_{e=1}^M(z_{e,0}^r+z_{e,1}^r),
 \quad d=\operatorname{ord}_r(2),\quad D=dr.
\]
Every parameter $a$ for which $V(H+aF)$ is singular lies in $\mathbb F_{2^D}$. Choose a power of two $b>D$ with $b\leq2D$ and an explicitly constructed field element $\theta$ of absolute degree $b$. Then $V(H+\theta F)$ is smooth. Its top absolute Frobenius has semilinear coefficient $\theta c$, while its field-linear Frobenius scalar is $c$.

Consequently scalar extraction, and equivalently point-count parity on this encoded class, is parity-counting complete under deterministic polynomial-time reductions. A polynomial-time algorithm for either would give $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$. E gives the inherited subexponential evaluator. This closes the deterministic finite-field smooth-specialization gate in NN-C024; it does not construct canonical GCT objects.''',
        inputs,
r'''We first prove the singular-parameter assertion for every nonzero $P$ with the stated pairwise homogeneity; no factorization or complexity assumption is needed for this geometric lemma. Work in a fixed algebraic closure of $\mathbb F_2$. The odd integer $r$ is one in this field, so the partial derivatives of $H$ are the corresponding $(r-1)$st powers. The zero parameter gives the smooth Fermat hypersurface. Suppose $H+aF$ has a singular projective point for some $a$.

At such a point, $z_0$ cannot be zero. If it were, all rail partial derivatives of $F=z_0P$ would vanish, and the zero-gradient equations would force every rail coordinate to be zero. This is not a projective point. Normalize $z_0=1$. The $z_0$ derivative now gives
\[
                              1+aP=0.
\]
Thus $a\ne0$, $P\ne0$, and $aP=1$ at the normalized point. If both coordinates of any rail pair were zero, pairwise degree two would force $P=0$. This too is impossible.

Euler's identity in one rail pair reads
\[
 z_{e,0}\frac{\partial P}{\partial z_{e,0}}
 +z_{e,1}\frac{\partial P}{\partial z_{e,1}}=2P=0.
\]
Multiply its two zero-gradient equations by their corresponding rail coordinates and add. The displayed identity yields
\[
                         z_{e,0}^r=z_{e,1}^r.
\]
Neither coordinate can be zero, since then both would be zero. Therefore
\[
              s_e=z_{e,0}\ne0,\qquad
              t_e=z_{e,1}/z_{e,0},\qquad t_e^r=1.
\]
Since $r$ is odd, $2$ is invertible modulo $r$ and its multiplicative order $d$ exists, with $d\leq\varphi(r)\leq r-1$. Put $q_0=2^d$. As $r$ divides $q_0-1$, every $r$th root of unity lies in the field $K=\mathbb F_{q_0}$. Thus all $t_e$ lie in $K$.

Pairwise homogeneity gives an identity
\[
 P(s_1,s_1t_1,\ldots,s_M,s_Mt_M)
                 =\left(\prod_e s_e^2\right)C(t_1,\ldots,t_M),
\]
where $C(t)=P(1,t_1,\ldots,1,t_M)$ has coefficients in $\mathbb F_2$. Each polynomial $z_{e,0}\partial P/\partial z_{e,0}$ is also homogeneous of degree two in every pair. Hence its normalized value is $(\prod_j s_j^2)C_e(t)$ for a polynomial $C_e$ over $\mathbb F_2$. Since $P\ne0$, $C(t)\ne0$. Multiplying the $z_{e,0}$ zero-gradient equation by $z_{e,0}$ and using $aP=1$ shows
\[
            s_e^r=
            \frac{z_{e,0}\,\partial P/\partial z_{e,0}}{P}
                  =\frac{C_e(t)}{C(t)}\in K^*.
\]

Every such $s_e$ lies in $K'=\mathbb F_{q_0^r}$, with no Kummer extension oracle required. Indeed $s_e^{r(q_0-1)}=1$. The integer $r(q_0-1)$ divides $q_0^r-1$: after dividing by $q_0-1$, the remaining sum $1+q_0+\cdots+q_0^{r-1}$ is divisible by $r$ because $q_0\equiv1\pmod r$. Thus $s_e^{q_0^r-1}=1$. The roots of $X^{q_0^r}-X$ form the unique field with $q_0^r$ elements in the algebraic closure, so $s_e\in K'$. Also $K\subset K'$, because $d$ divides $dr$. All coordinates of the normalized singular point therefore lie in $K'$, and
\[
                         a=1/P\in K'=\mathbb F_{2^{dr}}.
\]
This proves the claimed confinement of all bad parameters. It is stronger than a bound on the number or total degree of bad parameters: their individual field of definition is contained in one explicitly bounded finite field. The proof uses the multihomogeneous rail structure; it makes no such claim for arbitrary degree-$r$ forms.

We next construct a parameter outside this bad field with polynomial bit cost. Compute $d$ by repeated doubling modulo $r$ until the residue one returns; this takes at most $r$ steps and polynomial time in $r$. Compute $D=dr$ and choose the least power of two $b>D$. Then $b\leq2D\leq2r^2$. There is no need to construct the possibly non-power-of-two-degree field $\mathbb F_{2^D}$ itself.

Use the explicit quadratic tower proved in NN-C024: beginning with $\mathbb F_2$, at each degree $j=1,2,4,\ldots,b/2$, find a basis element of trace one in the current field and adjoin a root of $Y^2+Y+u$. Such an element exists because the absolute trace is a nonzero linear functional, and the polynomial is irreducible because $\operatorname{Tr}(y^2+y)=0$. Basis evaluation, squaring and arithmetic have polynomial cost in $b$. Let $\theta$ be the final adjoined root. It lies outside the preceding field of degree $b/2$. Its absolute degree divides $b$; every proper divisor of the power of two $b$ divides $b/2$, and every element of such degree belongs to that preceding field. Hence $\theta$ has absolute degree exactly $b$. In particular $\theta\notin\mathbb F_{2^D}$, since an element of the latter has degree at most $D<b$. The polynomial $H+\theta F$ is therefore smooth by the singular-parameter lemma.

The tower and its basis are an explicit field presentation of polynomial length. If one monic irreducible polynomial is required, compute the first linear dependence of $1,\theta,\ldots,\theta^b$ by linear algebra in the tower basis. Its degree is $b$ by the preceding argument, so it is the minimal polynomial; the same computations give the change to a power basis. This remains polynomial in $b=O(r^2)$. The parameter is nonzero because it has degree $b>1$. No random choice, smoothness test, discriminant expansion, or enumeration of the bad field is used.

We verify that the encoding always meets the geometric lemma. In NN-C023 each incidence rail pair occurs once in its clause factor and once in its variable-consistency factor. Every monomial in each of those factors uses exactly one member of the pair. Thus their product $P$ has degree exactly two in that pair, and it is independent of the extra coordinate $z_0$. The factors are nonzero over $\mathbb F_2$, so $P\ne0$. There are $2M+1=r$ total coordinates, and $F=z_0P$ is homogeneous of total degree $r$. The general hard instances therefore satisfy every hypothesis above, even when their target coefficient $c$ is zero.

For the elementary exceptional source inputs that NN-C023 handled by a non-rail cubic, first compute their parity directly. An empty clause has parity zero; a formula with no declared variables has its single assignment explicitly testable. Replace such an instance by one of two fixed one-variable formulas: the positive unit clause $x$, with parity one, or the two contradictory unit clauses $x$ and $\neg x$, with parity zero. Both have nonempty incidence sets and the same rail construction just proved. This replacement is made only for cases whose answer is already directly known. For ordinary inputs, unused variables can be made incident by the tautological factors in NN-C023, which preserve the exact count. Thus no oracle for the hard parity is used in any edge case.

The equation $H+\theta F$ has polynomial circuit description: the rail product is already succinct, and each pure $r$th power is computed by repeated squaring and multiplication. It is nonzero because $F$ is divisible by $z_0$ whereas the rail terms of $H$ are not. Its hypersurface in $\mathbb P^{r-1}_{\mathbb F_{2^b}}$ is projective, and the zero-gradient criterion proves geometric smoothness. The nontrivial coherent group, in degree $r-2$, is the known line of NN-C023. Its absolute Frobenius is semilinear, with matrix coefficient
\[
          [z_0\prod_e z_{e,0}z_{e,1}](H+\theta F)=\theta c.
\]
The pure powers in $H$ make no contribution to this squarefree monomial. Iterating semilinear Frobenius $b$ times gives the field-linear scalar
\[
                   (\theta c)^{1+2+\cdots+2^{b-1}}
                      =(\theta c)^{2^b-1}=c.
\]
This uses $\theta\ne0$ and $c\in\{0,1\}$. Thus the deterministic smooth specialization preserves the hard entry exactly, rather than only its nonvanishing with some probability.

SGA7 II XXII3.1--3.2 give the same full congruence as in NN-C024,
\[
 \#X(\mathbb F_{2^b})\equiv1+c\pmod2,
 \qquad Z(X/\mathbb F_{2^b},T)\equiv\frac{1-cT}{1-T}\pmod2.
\]
Deligne's Theorem1.6 applies to every produced hypersurface, so these are genuine smooth projective finite-field realizations with pure l-adic cohomology. That theorem is an imported classical input, not a purity conclusion inferred from the congruence.

The construction is now a deterministic polynomial-time reduction from parity-3-SAT. On the encoded family scalar membership in $\oplus\mathrm P$ follows from the factor-choice verifier for $c$ in NN-C023. Point-count parity also lies in $\oplus\mathrm P$ directly: guess a projective coordinate vector in the explicit field, require its first nonzero coordinate to equal one, and verify the equation. This normalization gives exactly one representative per rational point, and $rb=O(r^3)$ guessed bits suffice. The complement by one in the displayed formula is an elementary parity-output conversion. Hence the asserted parity-completeness holds under deterministic reductions. A polynomial-time scalar or parity algorithm gives $\mathrm P=\oplus\mathrm P$; Valiant--Vazirani then gives $\mathrm{NP}=\mathrm{RP}$, as recorded in NN-C006. This strengthens the randomized-promise consequence in NN-C024.

E computes $c$ from the original source formula, keeping its original variable parameter and its stated density dependence. The field construction and the displayed geometric description add only polynomial overhead in the formula size. Neither the $rb$ projective-point witness length nor the full l-adic Betti number is substituted into that sharper original-formula evaluator. A and M are unused in this construction.''',
        'Complete singular-parameter confinement, deterministic field construction and preserved-Frobenius proof; independent review pending.',
r'''The open finite-field specialization gate of NN-C024 is closed for its actual hard rail family. Smoothness, properness, finite base field, a specified rank-one coherent basis and a deterministic construction now coexist with a parity-complete Frobenius entry. This original construction has field degree at most quadratic in the succinct hypersurface parameter. NN-C031 subsequently removes the growing-field limitation by incidence padding over fixed F4; the present bound is retained as the historical general-parameter result. No polynomial bound on total l-adic rank is asserted. The result strengthens the conditional algorithmic consequence to $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$, rather than merely a randomized reduction. It proves no unconditional complexity lower bound, no VP/VNP separation, and no realization of a GCT canonical basis.''',
r'''Let $P\in\mathbb F_2[z_{e,0},z_{e,1}]$ be nonzero of degree two in each of $M$ pairs, and put $r=2M+1$, $F=z_0P$. In the Fermat pencil $H+uF$, every singular geometric fiber occurs at a parameter in the one finite field $\mathbb F_{2^{r\operatorname{ord}_r(2)}}$. The proof is the pairwise Euler identity, normalization at $z_0=1$, and the resulting root-of-unity and power equations above. A parameter of absolute degree greater than that bounded field degree therefore gives a smooth projective fiber; a quadratic Artin--Schreier tower supplies such a parameter with degree $O(r^2)$ and a polynomial-length presentation.

For the incidence-rail polynomials, the proper smooth fiber has $H^0(\mathcal O)=\mathbb F_{2^b}$ and one other nonzero coherent group, a canonically based line in degree $r-2$. Absolute Frobenius has semilinear coefficient $\theta c$, and the linearized field Frobenius has scalar $c$, the original parity count. The complete Cech proof is NN-C023 and the classical smooth formula is Katz2.3.7.17, p36. SGA1 II4.10(iii)/4.12 is the smoothness interface, SGA7 II XXII3.1--3.2 gives the proper zeta congruence, and Deligne Weil I1.6 gives purity of the actual l-adic realizations. These provide an exact deterministic finite-field geometric dictionary for the hard coefficient. A purity or existence theorem does not evaluate it, and the construction supplies no canonical identification with GCT multiplicities.''',
        inputs)
