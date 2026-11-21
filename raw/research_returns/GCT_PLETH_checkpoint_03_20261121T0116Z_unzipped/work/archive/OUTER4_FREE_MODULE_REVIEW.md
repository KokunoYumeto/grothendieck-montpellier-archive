# Independent full review of the outer-four fiber and polytope formula

## Review outcome and scope

**PASS.** I read and checked the complete proofs in T-032 \(`general_chart_report.md`\), T-035–T-036 \(`outer4/four_fibers_report.md`\), and T-037 \(`outer4/full_outer4_report.md`, including A.29–A.31\). I also checked the exact complement pairing F.12–F.15, the Elliott character calculation H.5–H.7, the harmonic character table H.8–H.12, and the three \(S_3\) series P.10 used by T-037. The checks below establish the actual module maps, all character twists, saturation in the full oriented range, and the fixed positive lattice counts.

T-037 gives all coefficients \(p_{\mu,(n)}^\lambda\) with \(\mu\vdash4\), including all central cases. It supplies at most 108 tagged bounded rational polytopes in at most five variables; the bounds are 36 for the symmetric and exterior outer labels and 72 for \((2,2)\). The exact fixed-table identities and arithmetic checks were independently executed in `check_outer4_fixed_tables.py`; its receipt is `OUTER4_FIXED_TABLE_RECEIPT.json`. I did not rerun the other agent's 1,980-coefficient Murnaghan–Nakayama sweep and do not count that sweep as my own event.

The only wording correction requested during this review was an explicit redefinition of (a,b) after the complement operation. The author has made that correction in A.7. The original and retwisted \(q\)-actions were checked separately; T-037 uses the correct cancellation.

## A-024. Actual free decomposition of the incidence algebra

Write \(V=\mathfrak h_4\), with its invariant dot product, \(W=\Lambda^2V=V\otimes\operatorname{sgn}\), and
\[
R=\mathbf Q[q\in V,t\in W]/(f),\qquad f=q\cdot t.
\]
The notation identifies each self-dual representation with the corresponding polynomial generator space through the displayed invariant form. The generator \(f\) has bidegree ((1,1)) and character \(\operatorname{sgn}\). In particular \(\det V=\operatorname{sgn}\) and \(\det W=1\).

Let \(\ell_i=e_i-\frac14\mathbf1\). The two quadrics \(U\) vanishing on their four projective lines give, after the specified linear change of coordinates,
\[
A=\mathbf Q[q]/(U)
=\mathbf Q[X,Y,Z]/(X^2-Z^2,Y^2-Z^2).
\]
The monic reductions give an actual free \(\mathbf Q[Z]\)-basis (1,X,Y,XY). After inverting \(Z\), the ring maps isomorphically to the product of the four Laurent line rings indexed by \(X/Z,Y/Z\in\{1,-1\}\). Freeness over \(\mathbf Q[Z]\) makes the map to the product of the four polynomial line rings injective before localization. Thus no component or embedded contribution at the origin has been removed. The two displayed quadrics form a regular sequence in the polynomial ring: after quotienting by the first, the second is monic in \(Y\) and hence acts injectively.

On the \(i\)-th component, \(q=s\ell_i\) and \(f=s(\ell_i\cdot t)\). Both factors are nonzero in that component's polynomial domain. The product embedding therefore proves that multiplication by \(f\) on (A[t]) is injective. With \(\mathcal H=R/(U)\), the resulting exact Hilbert-series identity is
\[
\operatorname{Hilb}\mathcal H=(1-s^2)^2\operatorname{Hilb}R.
\]

Choose a rational section of \(R_{C,b}\to\mathcal H_{C,b}\) in each finite bidegree, and average it over the 24 elements of \(S_4\). This gives an actual equivariant section \(\sigma\). The multiplication map
\[
M:\operatorname{Sym}(U)\otimes\mathcal H\longrightarrow R,
\qquad p\otimes h\longmapsto p(U)\sigma(h)
\]
is surjective by repeatedly reducing modulo (\(U\)); every reduction lowers the \(q\)-degree by two. Its source and target have equal dimensions in every bidegree by the preceding series identity. Hence \(M\) is an equivariant \(\operatorname{Sym}(U)\)-linear isomorphism. This also proves algebraic independence of the two quadrics, and that they form a regular sequence in \(R\). It directly identifies
\[
(U)^kR_{c,b}
\simeq\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^jU\otimes\mathcal H_{c-2j,b}.
\]
There is no unproved choice of a multiplicative basis in this argument. The section is a linear section; its explicit averaged multiplication map supplies exactly the required free module structure.

### Evaluation and every quotient piece

Evaluation at the actual affine vectors \(\ell_i\) is \(S_4\)-equivariant with no parity character. It gives \(A_0=\mathbf1\), \(A_1=V\subset\operatorname{Perm}_4\), and \(A_C=\operatorname{Perm}_4\) for all \(C\ge2\). An explicit surjectivity check is available without any projective scaling convention: put
\[
E_i(q)=2q_i^2-\tfrac16\sum_lq_l^2.
\]
Then \(E_i(\ell_j)=\delta_{ij}\); for \(C\ge2\), the homogeneous polynomial
\(E_i(q)(4q_i/3)^{C-2}\) has the same evaluations. The Hilbert series of \(A\) gives dimension four in all those degrees. In degree two the kernel of the evaluation quotient \(\operatorname{Sym}^2V\to\operatorname{Perm}_4\) is exactly \(U=[(2,2)]\). Its matching-plane realization gives \(\det U=\operatorname{sgn}\).

The nonzerodivisor just proved yields the exact equivariant sequence
\[
0\longrightarrow\operatorname{sgn}\otimes A_{C-1}\otimes\operatorname{Sym}^{b-1}W
\xrightarrow{f}A_C\otimes\operatorname{Sym}^bW
\longrightarrow\mathcal H_{C,b}\longrightarrow0.
\]
For \(C\ge3\), evaluation identifies the first map point by point with multiplication by \(\ell_i\cdot t\). The stabilizer \(S_3\) of \(\ell_i\) acts by sign on this line in \(W\), and its quotient is \(\mathfrak h_3\otimes\operatorname{sgn}\). The explicit rational area-form intertwiner identifies this quotient with \(\mathfrak h_3\). Thus the cokernel is
\(D_b=\operatorname{Ind}_{S_3}^{S_4}\operatorname{Sym}^b\mathfrak h_3\).

For \(C=2\), extend the source \(A_1=V\) to \(\operatorname{Perm}_4\). The extended map remains injective point by point, and has the preceding cokernel \(D_b\). The quotient of its image by the original image is
\(\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\), because \(\operatorname{Perm}_4/V=\mathbf1\). The resulting short exact sequence splits by an averaged projection.

For \(C=0\), the quotient is \(\operatorname{Sym}^bW\). For \(C=1\), the incidence multiplication removes the \(S_{(b,b,1)}V\) term from \(V\otimes\operatorname{Sym}^b(\Lambda^2V)\); the quotient is the Cartan term \(S_{(b+1,b)}V\). Twisting \(V=W\otimes\operatorname{sgn}\) contributes sign because (2b+1) is odd. The Elliott rule with Dynkin labels ((1,b)) gives \(\bigoplus_{L=1}^{b+1}H_L\), including \(b=0\). Consequently every row of A.5 follows by an actual exact sequence or intertwiner, with the sign in the \(C=1\) row required.

## A-025. Chart, fibers, saturation, and complement

### The general chart and the fiber valuations

In T-032 the centered-ratio chart is equivariant because row permutation fixes \(\mathbf1\), fixes \(u=\prod_i x_i\), and commutes with centering. Its flag-coordinate map is multiplication by the explicitly displayed products of first-column variables. A balanced monomial of weight \((n^m)\) and highest weight \(\lambda\) becomes
\(u^{n-\lambda_2}\) times a tail-flag monomial: the number of columns of height at least two is exactly \(\lambda_2\), and the remaining exponent of every \(x_i\) is \(n\). This proves the claimed surjectivity. The inverse chart prescribing nonzero \(u\), then choosing the \(x_i\) with that product and the remaining centered columns, proves injectivity on a dense open set. Polynomiality is precisely divisibility by the stated power of \(u\), and equality there extends as a polynomial identity. These are actual algebra maps.

For \(m=4\), the map gives \(q\in V\), \(t\in W\), and the determinant variable \(z\in\operatorname{sgn}\). At \(x_4=\varepsilon\), use the affine chart with \(q_4-q_1\ne0\). The two normal coordinates at \(\ell_4\) are
\[
\frac{q_j-q_1}{q_4-q_1}
=\frac{\varepsilon(r_j-r_1)}{S-\varepsilon r_1},\qquad j=2,3.
\]
Their leading coefficients vary independently. Setting the last entry of the third column to zero makes the limiting \(t_1,t_2,t_3\) depend on the first and third columns and \(S\), independently of those two normal coefficients; they range over the fiber \(\sum_{i=1}^3t_i=0\). The fourth column makes \(z\ne0\) on this same generic locus. Therefore the lowest nonzero transverse term cannot disappear upon substitution, and the \(x_4\)-valuation equals the ideal order at the generic point of the entire fiber. Each graded normal quotient is a vector bundle on the integral fiber, so a section vanishing at its generic point vanishes everywhere. This upgrades the generic valuation statement to membership in the full ideal power. Permutation equivariance supplies the other three fibers.

The \(x_i\) are pairwise nonassociate primes, so the individual valuations characterize divisibility by \(u^k\). The four fibers are disjoint, and the incidence projection is a projective-line bundle, hence flat. Their simultaneous order-\(k\) condition is exactly \(\pi^*\mathcal I_Z^k\). These facts establish the stated section-space model by the actual chart substitution.

### Character convention and orientation

T-035 initially uses \(q\in W\), so it has the outside twist \(\operatorname{sgn}^{c+d}\). Replacing that \(q\)-action by the original \(q\in V\) changes the degree-\(c\) section module by \(\operatorname{sgn}^c\). The two factors cancel and leave precisely \(\operatorname{sgn}^d\) in A.16 and A.9.

As an independent check that detects this sign, take \(n=4\), \(\lambda=(11,5,0,0)\), so \(c=5,k=1,b=d=0\). The original-action ideal piece is
\(U\otimes\operatorname{Perm}_4\oplus\operatorname{Sym}^2U\otimes V\).
It has dimension 17 and transposition trace 1. Independently, the balanced trace in \(s_{(11,5)}=h_{11}h_5-h_{12}h_4\), at cycle type ((2,1,1)), is the number of triples \(0\le x,y,z\le4\) with \(2x+y+z=11\), minus the corresponding number for 12. It is \(10-9=1\). An uncancelled extra sign would give (-1).

The complement map uses the nonzero Schur pairing
\(S_\lambda V_4\otimes S_{\widehat\lambda}V_4\to(\det V_4)^H\), obtained by complementary exterior columns. It is perfect by irreducibility and carries the balanced weight to the balanced weight for \(\widehat n=H-n\). Literal permutation matrices act on the target by \(\operatorname{sgn}^H\); self-duality of rational Specht modules gives exactly the conjugation rule in A.6. The operation exchanges the opposite gaps (a,b) and preserves \(c\). After redefining the gaps for the resulting partition, \(a\ge b\), and \(c-2k=(a-b)/2\ge0\) whenever \(k>0\). Thus every input reaches the proved saturation range in at most one complement operation.

### Saturation above the boundary

The two-quadric power resolution pulls back along the flat projection and becomes
\[
0\to\operatorname{Sym}^{k-1}U\otimes\det U\otimes
\mathcal O_{\mathcal F}(c-2k-2,b)
\to\operatorname{Sym}^kU\otimes\mathcal O_{\mathcal F}(c-2k,b)
\to\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(c,b)\to0.
\]
For \(c\ge2k+1\), the left degree is at least (-1). The incidence hypersurface sequence on \(\mathbf P^2\times\mathbf P^2\) proves \(H^1(\mathcal O_{\mathcal F}(a,b))=0\) for \(a\ge-1,b\ge0\): both ambient \(H^1\) and the preceding ambient \(H^2\) vanish, since the latter twists are at least (-2,-1). The same sequence identifies global sections with \(R_{a,b}\) for \(a\ge0\), and gives zero for \(a=-1\).

Global sections are therefore the cokernel of exactly the multiplication map obtained by extending the two-variable power-ideal resolution along \(\operatorname{Sym}(U)\to R\). A-024 proves that \(R\) is free over this polynomial algebra, so that extension is exact. Its cokernel is \((J_R^k)_{c,b}\). This proves equality with the sheaf section space by the same map, including the first endpoint \(c=2k+1\).

At \(c=2k\), the cohomology calculation in T-036 gives the extra summand
\[
\operatorname{sgn}\otimes\operatorname{Sym}^{k-1}U
\otimes\operatorname{Sym}^{b-1}W.
\]
The character can also be checked entirely in the original convention. Here \(H^2(\mathbf P(V),\mathcal O(-3))=\det V=\operatorname{sgn}\), while \(\det U=\operatorname{sgn}\); their product makes \(H^1(\mathcal I_Z^k(2k-1))=\operatorname{Sym}^{k-1}U\). The incidence injection itself has sign, supplying the displayed remaining character. An averaged projection splits the resulting exact sequence. Negative symmetric powers are zero; \(k=0\) is the ordinary whole-ring case and gives no correction. This proves A.9 for every oriented input.

## A-026. Exact fixed tags, lattice counts, and arithmetic

The harmonic trace series on the five classes are
\[
\frac{1+q}{(1-q)^2},\quad\frac1{1+q},\quad\frac1{1+q},\quad
\frac{1+q}{1+q+q^2},\quad\frac{1+q}{1+q^2}.
\]
They follow by dividing \(1-q^2\) by the characteristic polynomial on \(W\). Using the explicit five-row character table and class sizes (1,6,3,8,6), I checked every rational identity giving the stated \(E_\tau\) numerator over \((1-q^4)(1-q^6)\). I also checked all three \(S_3\) averages giving \(F\), all 75 relevant tensor entries by character inner products, and the induction branching giving \(G\). All entries of the tensor table are zero or one.

The Elliott proof H.5–H.7 is a full character calculation: its finite geometric sum distinguishes both parities, the extra \(\delta/(1+z)\) term cancels from \(P(z)-z^{-1}P(z^{-1})\), and the remaining six monomials match the specialized Weyl numerator. Thus the use of its ((1,b)) specialization in A.5 has no unproved branching step.

In the positive module sum, put \(C=c-2j\). The terms with \(C\ge3\) are exactly A.25, with \(j=f+2x_2+3x_3\) recoverable uniquely from each lattice point. Odd \(c\) leaves \(C=1\), producing A.27 and its required label conjugation. Even \(c\) leaves \(C=0\), and also \(C=2\) precisely when \(c\ge2k+2\); these give the displayed A.26 term and the two A.5 terms. At \(c=2k\), only the boundary correction remains in addition to \(C=0\). Consequently A.28 neither omits nor duplicates any summand.

The exact numbers of fixed tags are:

| Target label | A.25 | A.26 or A.27 | Full even bound |
|---|---:|---:|---:|
| ((4)), \((1^4)\) | 6 | 12 | 36 |
| ((2,2)) | 12 | 24 | 72 |
| ((3,1)), ((2,1,1)) | 18 | 36 | 108 |

Every variable has a positive coefficient in an equality or upper bound. Thus each listed region is a bounded rational polytope. Its constants are (O\(n\)), including after complement, and the matrices are fixed.

The elementary scalar formulas A.29–A.31 are also correct. Splitting \(y=2t+e\) proves the arithmetic-progression formula for \(P(N)=\#\{2x+3y\le N\}\); the \(T_e=-1\) endpoint contributes zero. The weight-2 coordinate in A.26 is the uniquely determined slack variable after division by two. For A.27 the lower exclusion is exactly \(P(\lfloor-e/2\rfloor)\), including \(e=0\), where it removes \(L=0\). I directly enumerated the scalar formulas for \(-12\le N\le120\) and all 310 intervals \(0\le b\le30,0\le e\le9\), in addition to the algebraic proofs.

Each fixed template count is \(O((n+1)^3)\); its free count has dimension at most three. The finite number of arithmetic operations uses integers of \(O(\log(n+2))\) bits. Thus the stated schoolbook \(O((\log(n+2))^2)\) arithmetic bound follows for the coefficient evaluator. The witness enumerator is separately output-dependent, as its implementation states.

### Endpoint checks

- \(n=0\), \(\lambda=0\): \(c=b=d=k=0\). Only \(\mathsf W_\mu(0,0)\) survives, giving 1 for \(\mu=(4)\) and zero for the other four labels, exactly the Schur functors of the one-dimensional \(\operatorname{Sym}^0\).
- \(b=0\): every term with (b-1) vanishes; the \(C=1\) row is the correct standard \(V\), since \(\operatorname{sgn}\otimes H_1=V\).
- \(c=0\): \(k=0\), and only the degree-zero quotient piece remains.
- \(c=1\): \(k=0\), and the only term is \(\mathsf L_{\nu'}(0,b)\).
- \(c=2k+1\): the bulk interval is empty, so only the \(C=1\) term remains.
- \(c=2k\): the bulk and \(C=2\) terms are absent; the two \(\mathsf W\) terms give exactly the boundary sequence.
- Valid partitions with more than four parts have zero coefficient: four successive horizontal-strip additions produce at most four rows in the ambient tensor power, and the Schur symmetrizer maps the requested outer functor into that power.

All these checks use the exact maps or formulas above. No unresolved module, saturation, parity, or positive-count gate remains for outer degree four in the stated family. This review makes no assertion of historical novelty.
