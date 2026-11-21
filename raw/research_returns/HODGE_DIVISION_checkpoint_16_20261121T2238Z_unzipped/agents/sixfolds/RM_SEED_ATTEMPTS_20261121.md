# Further balanced RM seed attempts after SF-E816

Author/checker: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21. These are actual finite arithmetic tests and construction attempts. They do not construct a balanced semiregular object. No all-rank or all-lattice exclusion is inferred from a finite computation. The complete universal theorems SF-E815--E816 are recorded separately.

## 1. The common rank-one divisor shift and its actual HN limitation

If an integral divisor \(D\) has \(D^2=0\), then in the entire cohomology ring

\[
 e^{\beta+D}+e^{\beta-D}=2e^\beta.
\]

Consequently doubling the actual rank-32 character of SF-E815 permits every pair of line summands to be replaced by summands of classes \(\beta\pm kD\). For the common divisor \(D\) from the third elliptic factor of \(E_i^4\), the class \(X_0+2D\) has matrix \(\operatorname{diag}(1,1,1,-1)\), index one, and Euler characteristic \(-1\). Thus nonzero coherent degree-one extensions really occur outside the primitive class space.

There is nevertheless an exact restriction on the proposed two-slope repair. If the resulting bundle is an extension with all positive-slope summands as subobject and negative-slope summands as quotient, these are its actual canonical Harder--Narasimhan pieces. Inside either piece, the original primitive differences give Hom/Ext-one vanishing between unequal \(\beta\), so each HN piece splits canonically into its class blocks. All those blocks are actual equivariant objects for any coherent stabilizing translation/tensor action, even though they need not be summands of the full bundle.

In the doubled rank-32 model, the two blocks of shifted classes \(Z_++kD\) and \(-Z_++kD\) have rank one. Their ordinary cross Euler is 16. Supplied S-21's exact two-object scaling therefore gives \(|G|\mid16\). The whole ordinary self-Euler is 4096, so its invariant Euler is at least 256. If it were gluable and weakly semiregular, the balanced cap ranks would give

\[
 256\le\chi_G(E,E)=2e_0^G-2e_1^G+18\le2e_0^G+2,
\]

hence \(e_0^G\ge127\). This removes this fixed common-shift family as a simple-seed proposal. It does not exclude a sufficiently nonsimple repair. Root supplied this sharper HN observation; sixfolds independently checked all numerical factors and the actual HN/class-block scope.

An index-one two-line extension is a genuine control, but is not balanced. A nonzero extension of \(\mathcal O_X\) by the above index-one line bundle is an actual simple unstable bundle. The three triangle long exact sequences give the same dimensions \((1,8,12,8,1)\) as the index-two derived cone in SF-E814. Its cap rank is twelve. This control shows that stable-bundle obstructions must not be promoted to all unstable bundles; it is not counted as progress constructing the balanced input. A full separate canonical proof has not been entered for this control.

## 2. Exact signed exponential searches with the equivariance assumptions retained

These searches concern complexes whose cohomology sheaves are filtered by stable projectively flat factors with normalized classes in the primitive real-multiplication divisor space. They allow arbitrary bounded amplitude, repeated classes in different degrees, and arbitrary Postnikov data. In this setting, each cohomology sheaf has canonical actual equivariant normalized-class blocks. Their alternating direct sums \(U_\beta\) are actual equivariant perfect objects, with

\[
 [E]=\sum_\beta[U_\beta],\qquad
 \operatorname{ch}(U_\beta)=n_\beta e^\beta,\qquad n_\beta\in\mathbf Z.
\]

They are not asserted to be summands of \(E\). For \(\beta=aX_0+bY\), with \(Y=\sqrt d(x-y)\), the ordinary pair Euler is

\[
 \chi(U_\beta,U_\gamma)
   =n_\beta n_\gamma
     \bigl((a-c)^2-d(b-e)^2\bigr)^2,
 \quad\gamma=cX_0+eY.
\]

Every possible effective coherent action therefore has order dividing the gcd of these pair integers. This is a necessary condition; it does not construct such an action.

The script uses sign/conjugation orbits of lattice points \((a,b)\), together with the origin. Let \(w_j\) be the signed coefficient at each point of an orbit of size \(m_j\). Define

\[
 A=\sum_jm_jw_j(a_j^2+db_j^2),\quad
 B=\sum_jm_jw_j(a_j^2-db_j^2),\quad
 C=\sum_jm_jw_j(a_j^2-db_j^2)^2.
\]

Orbit symmetry kills all odd components and the Galois-antisymmetric component. The exact equations \(B=0\), \(N=A^2/C\), \(q=C/A\), and the choice of the origin coefficient to make total rank \(N\), verify the **entire** character

\[
 Nv_q=N(1-q\theta_+^2/2)(1-q\theta_-^2/2).
\]

The ordinary self-Euler is \(4A^2\). Denominators of the virtual coefficients are cleared, common scalar factors removed, and every pair gcd and full moment identity is checked exactly.

The actual outputs are:

| Search | Eligible parameter cases | Best lower bounds for invariant Euler | Necessary candidates with bound at most four |
|---|---:|---|---:|
| Two or three sign/conjugation orbits, coordinate bound three, rational weight parameter bound three | 22,067 across \(d=2,3,5,6,10,13,17\) | 128, 96, 60, 384, 3200, 364, 612, respectively | 0 |
| The same search plus four orbits, the two free coefficients in \(\{-2,-1,1,2\}\), coordinate bound three | 49,250 across \(d=2,3,5\) | 128, 96, 60, respectively | 0 |

These are parameter-case counts, not counts of distinct characters. The second search includes its two/three-orbit cases, so the rows must not be added as disjoint searches. The files are rm_signed_class_search.py, rm_signed_class_search_output.json, and rm_signed_four_orbit_search_output.json. Every output states that no actual object, action, or semiregularity has been constructed or checked. A qualifying future signed candidate would still need at least three cohomological degrees with class overlaps to escape SF-E816, and actual derived products rather than assumed formality.

### A numerical refinement of SF-E815

There is a small exact improvement within the already reviewed seven-class model. Its actual equivariant objects of classes \(X_0\) and \(Z_+\) have virtual ranks \(2k\) and \(k\). Their difference is \(Y\), of norm \(-2\), so their pair Euler is \(8k^2\). Hence \(|G|\mid8k^2\), the invariant self-Euler is at least 128, and the same CY4 inequality gives \(e_0^G\ge63\). This improves the former bound 31. It is only a quantitative refinement of that obstruction, not a new main-gate claim. The complete written refinement awaits its own review before the canonical statement is changed.

## 3. Full-character congruences on explicit even or nonmaximal RM lattices

To seek an actual small-Euler character, we changed the normalized rational character, rather than merely tensor an old one by a divisor exponential. Let \(r>0\), let \(\theta\) have product \(D\), and let \(\eta=\theta_U\) for \(U^2=d\). Put

\[
 t=\frac{rq}{4}\left(\theta^2+\frac{\eta^2}{d}\right).
\]

For a prospective character \(e^{\ell/r}r v_q\), its complete components are

\[
 \begin{aligned}
 \operatorname{ch}_0&=r,&\operatorname{ch}_1&=\ell,\\
 \operatorname{ch}_2&=\frac{\ell^{[2]}}r-t,&
 \operatorname{ch}_3&=\frac{\ell^{[3]}}{r^2}-\frac{\ell t}{r},\\
 \operatorname{ch}_4&=\frac{\ell^{[4]}}{r^3}
       -\frac{\ell^{[2]}t}{r^2}+\frac{k}{4r}[\mathrm{pt}],
 & k&=4D(rq)^2\in\{2,4\}.
 \end{aligned}
\]

Here divided exterior powers of integral two-forms are integral. In particular the ch-two condition is necessary for every perfect object on a torus. For the field-five test below, every failure in ch-three has a denominator five; this is impossible already because \(6\operatorname{ch}_3\) is an integral polynomial in Chern classes. Thus no negative conclusion below depends on a general assertion identifying the entire topological or algebraic Chern-character lattice.

All first Chern classes tested lie in the full sixteen-dimensional integral \((1,1)\)-lattice of \(E_i^4\): four diagonal forms and the real and imaginary off-diagonal Hermitian forms. Their coefficients are taken modulo \(r\); changing a representative by \(r\) times an integral divisor is a line-bundle twist and preserves the relevant integrality conditions.

### 3.1. A degree-two polarization for \(\mathbf Q(\sqrt2)\)

Take

\[
 A=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
 U=\operatorname{diag}(A,A),\quad
 H=\operatorname{diag}(2I+A,I).
\]

The Hermitian matrix \(H\) is positive, commutes with \(U\), and has determinant two. The self-Euler-two window requires \(rq=1/2\), and \(t^2=[\mathrm{pt}]\). The exact Hodge-lattice search gives:

- Rank four: every one of 65,536 first-Chern residues modulo two was checked; none has the required divided-square residue.
- Rank eight: 156 of the 65,536 residues satisfy the first congruence; none lifts to the next necessary congruence modulo four.

These fixed-rank residue checks are exhaustive within the stated Hodge lattice. No all-rank conclusion is drawn.

### 3.2. A nonmaximal-at-two isogeny of the same datum

Pull the preceding forms back by
\(T=\operatorname{diag}(1+i,1,1+i,1)\), an isogeny of degree four. The new polarization product is eight. Normalize \(t'=T^*t/2\); then the self-Euler remains two and \(rq'=1/4\). The transported field operator is rational, and twice it is integral; this is a different integral order situation.

- Rank eight: no first-Chern residue among the 65,536 modulo-two residues passes the first congruence.
- Rank sixteen: 156 residues pass modulo two, but no complete second-Chern-character lift survives. The exact recursive run checks 412 lifting nodes and exhausts its branches.

The scripts and outputs are rm_integral_character_search.py, rm_integral_character_search_output.json, and rm_integral_character_nonmax02_output.json. The configured branch bound is 100,000; neither actual run reaches it. Their outputs explicitly record exhaustive true for these particular ranks, and no constructed object.

### 3.3. The unramified-at-two field \(\mathbf Q(\sqrt5)\), rank five

On the principal CM product use
\(U=\operatorname{diag}(A_5,A_5)\), where
\(A_5=\left(\begin{smallmatrix}1&2\\2&-1\end{smallmatrix}\right)\).
For self-Euler four, \(rq=1\). The second-Chern congruence at five restricts the evaluated Hermitian matrix to fixed two-dimensional row and column spaces. Modulo five, \(A_5\) is the outer product of \((1,2)\) with itself. The matrices are therefore \(PKP^t\), with \(K\in M_2(\mathbf F_5)\) of determinant three. There are exactly 120 such matrices, and all are checked.

All 120 satisfy ch-two integrality in rank five. Every one has a denominator five in ch-three. Hence none is the Chern character of an actual perfect object. This is the full explicit fixed-rank test, not an obstruction for all ranks or all integral RM lattices. Files: rm_field5_character_search.py and rm_field5_character_search_output.json.

### 3.4. A nonmaximal-at-five degree-twenty-five isogeny

Pull the field-five principal datum back by
\(T=\operatorname{diag}(2+i,1,2+i,1)\), of degree twenty-five. Normalize \(t'=T^*t/5\); the product is now twenty-five, \(rq'=1/5\), and the desired self-Euler is four. Rank twenty-five clears the initial denominators.

At the chosen embedding \(i\mapsto2\) modulo five, the prescribed matrix has column basis \((e_1,e_3)\) and row basis \((3,4,0,0),(0,0,3,4)\). Again the 120 determinant-three matrices give all candidates in these fixed rank-two spaces. All 120 satisfy the first congruence modulo five, and none lifts to the required congruence modulo twenty-five. Each failed linear system has a saved explicit annihilating row vector: it kills all sixteen coefficient columns and pairs nontrivially with the target. The script checks these identities exactly before recording failure.

Files: rm_field5_nonmax_character_search.py and rm_field5_nonmax_character_search_output.json. No entire-field, all-rank, or all-isogeny inference is made. The nonmaximal order and even-degree routes remain open beyond these concrete unsuccessful data.

## 4. Remaining actual construction problem

No integral small-Euler character, actual balanced bundle, or actual higher-amplitude balanced complex has emerged from these tests. The remaining alternatives include more general nonmaximal RM lattices, other even polarization types, genuinely twisted inputs, unstable bundles with different mixed HN factors, or overlapping-class complexes with at least three cohomological degrees and actual nontrivial derived products. These alternatives are not asserted to work. The newly checked SF-E816 obstructions and the explicit counterexample to a blanket overlap inference remain the rigorous boundaries for the next construction.
