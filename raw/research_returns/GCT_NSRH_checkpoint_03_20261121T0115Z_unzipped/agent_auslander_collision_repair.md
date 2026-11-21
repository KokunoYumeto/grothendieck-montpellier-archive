# F40: a smooth proper corner realization of the actual collision algebra

Author: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**Status:** complete author proof, including an explicit projective diagonal resolution, actual algebra and module recovery, and the exact nonadmissibility limitation. Independent full review is requested before integration. The classical Auslander algebra and exceptional-collection facts are not claimed historically new; the construction is applied to the specific nonstandard collision fiber already identified in F19/F21.

## 1. The algebra and its multiplication

Let \(k\) be a field and

\[
B=k[\epsilon]/(\epsilon^2),\qquad T=B\oplus k,
\qquad \Gamma=\operatorname{End}_B(T).
\tag{A1}
\]

Write \(e_1,e_2\) for the two summand idempotents. Let \(a:k\to B\) send \(1\mapsto\epsilon\), let \(b:B\to k\) be the quotient, and write \(c=ab\). Multiplication is composition, with the right factor applied first. Thus

\[
a=e_1ae_2,\quad b=e_2be_1,\quad ba=0,\quad
c=ab=e_1ce_1\ne0,\quad c^2=0.
\tag{A2}
\]

The five elements \(e_1,e_2,a,b,c\) form a basis. All products of three arrows vanish. Indeed the four matrix Hom spaces have dimensions \(2,1,1,1\), and the given maps span them. Thus this presentation gives the actual five-dimensional endomorphism algebra; no quotient losing \(c\) has been taken.

The radical is \(J=\langle a,b,c\rangle\), with \(J^2=kc\), \(J^3=0\), and \(\Gamma/J=k^2\). The two right indecomposable projectives are

\[
P_1=e_1\Gamma=\langle e_1,a,c\rangle,
\qquad P_2=e_2\Gamma=\langle e_2,b\rangle.
\]

Let \(S_i=P_i/P_iJ\) denote the right simple modules.

## 2. Global dimension exactly two

Left multiplication by \(a\) embeds \(P_2\) in \(P_1\), sending \(e_2\mapsto a\) and \(b\mapsto c\). Its image is \(\operatorname{rad}P_1\). Left multiplication by \(b:P_1\to P_2\) sends \(e_1\mapsto b\) and kills \(a,c\). Its image is \(\operatorname{rad}P_2\) and its kernel is the preceding image. Consequently

\[
0\longrightarrow P_2\xrightarrow{a}P_1
 \longrightarrow S_1\longrightarrow0,
\tag{A3}
\]
\[
0\longrightarrow P_2\xrightarrow{a}P_1
 \xrightarrow{b}P_2\longrightarrow S_2\longrightarrow0
\tag{A4}
\]

are exact projective resolutions. Applying \(\operatorname{Hom}_\Gamma(-,S_2)\) to (A4) gives
\(\operatorname{Ext}^2_\Gamma(S_2,S_2)=k\), because \(\operatorname{Hom}(P_1,S_2)=0\) and \(\operatorname{Hom}(P_2,S_2)=k\). Thus the global dimension is at least two.

For the upper bound, every right module has the finite radical filtration
\(N\supset NJ\supset NJ^2\supset0\), whose quotients are direct sums of \(S_1,S_2\). Direct sums of (A3)–(A4) give projective dimension at most two for each quotient, and the projective-dimension bound is preserved under extensions. Therefore every right module has projective dimension at most two. In particular

\[
\operatorname{gldim}\Gamma=2.
\tag{A5}
\]

## 3. A complete finite projective diagonal resolution

Here is a direct smoothness proof that does not appeal to a general finite-global-dimension criterion. Tensor products in this section are over \(k\). Define the projective \(\Gamma\)-bimodules

\[
Q_0=(\Gamma e_1\otimes e_1\Gamma)
 \oplus(\Gamma e_2\otimes e_2\Gamma),
\]
\[
Q_1=(\Gamma e_1\otimes e_2\Gamma)_a
 \oplus(\Gamma e_2\otimes e_1\Gamma)_b,
\qquad
Q_2=\Gamma e_2\otimes e_2\Gamma.
\]

The subscripts label the two summands. Each is a direct summand of a finite free module over \(\Gamma\otimes\Gamma^{\mathrm{op}}\). Let \(\mu:Q_0\to\Gamma\) be multiplication, and define

\[
d_1(x\otimes y)_a=xa\otimes y-x\otimes ay,
\qquad
d_1(x\otimes y)_b=xb\otimes y-x\otimes by,
\tag{A6}
\]

where the two terms land in the source and target vertex summands of \(Q_0\). Finally set

\[
d_2(x\otimes y)=(xb\otimes y)_a+(x\otimes ay)_b.
\tag{A7}
\]

These formulas define bimodule maps. Multiplication gives \(\mu d_1=0\), and

\[
d_1d_2(x\otimes y)=xba\otimes y-x\otimes bay=0
\]

by \(ba=0\).

We check exactness completely. The left ideals have bases
\(\Gamma e_1=\langle e_1,b,c\rangle\) and
\(\Gamma e_2=\langle e_2,a\rangle\), whereas the right ideals have the bases already displayed. Thus

\[
\dim Q_2=4,\qquad\dim Q_1=12,\qquad
\dim Q_0=13,\qquad\dim\Gamma=5.
\]

The map \(\mu\) is surjective. The following eight vectors belong to the image of \(d_1\):

\[
\begin{gathered}
a\otimes e_2-e_1\otimes a,\qquad
a\otimes b-e_1\otimes c,\qquad
b\otimes e_1-e_2\otimes b,\qquad
c\otimes e_1-a\otimes b,\\
b\otimes a,\qquad b\otimes c,\qquad
c\otimes a,\qquad c\otimes c.
\end{gathered}
\]

They are independent in the indicated vertex tensor bases. For example the first four have, respectively, unique coordinates at \(a\otimes e_2\), \(e_1\otimes c\), \(e_2\otimes b\), and \(c\otimes e_1\); the last four are separate remaining basis coordinates. Hence \(\operatorname{rank}d_1=8=\dim\ker\mu\).

The \(a\)-summand projection of \(d_2\) is the tensor product of the injection

\[
\Gamma e_2\longrightarrow\Gamma e_1,
\qquad x\longmapsto xb,
\qquad e_2\longmapsto b,\quad a\longmapsto c,
\]

with the identity of \(e_2\Gamma\). It is injective, so \(d_2\) is injective. Since \(\dim\ker d_1=12-8=4\), its image is the entire kernel. This proves the exact projective diagonal resolution

\[
0\longrightarrow Q_2\xrightarrow{d_2}Q_1
 \xrightarrow{d_1}Q_0\xrightarrow{\mu}\Gamma
 \longrightarrow0.
\tag{A8}
\]

Thus \(\Gamma\) is homologically smooth over \(k\). It is proper because it is finite dimensional. This proof works over any field; the condition \(\operatorname{char}k>3\) below comes from the actual nonstandard collision presentation.

## 4. Exact recovery of the actual rank-three algebra and module

Now let \(\operatorname{char}k>3\). The previously established actual collision algebra is

\[
A_1=k\times k\times M_2(B).
\]

Define

\[
\Lambda=k\times k\times M_2(\Gamma),\qquad
f=(1,1,I_2\otimes e_1).
\tag{A9}
\]

Then \(\dim_k\Lambda=22\), and its diagonal is perfect by (A8), matrix Morita equivalence, and finite products. Its global dimension is two. The corner is literally

\[
f\Lambda f=k\times k\times M_2(e_1\Gamma e_1)
 \simeq k\times k\times M_2(B)=A_1,
\tag{A10}
\]

with \(\epsilon\mapsto c=ab\ne0\). In particular no semisimplification occurs. All named generators from F19 are carried by this corner isomorphism: on the matrix block the normalized generators are the displayed matrices with \(z=3/4+c\), and the original generators are four times those idempotents.

Let \(P=f\Lambda\), a right projective \(\Lambda\)-module. Left multiplication identifies

\[
\operatorname{End}_\Lambda(P)=f\Lambda f=A_1.
\tag{A11}
\]

This exhibits the actual algebra as endomorphisms of an actual perfect object in the smooth proper category \(\operatorname{Perf}(\Lambda)\), including its nonzero nilpotent elements.

The actual 64-dimensional specialized tensor module from F21 is

\[
M_1\simeq\epsilon_+^{20}\oplus\epsilon_-^4
 \oplus S^{20},
\tag{A12}
\]

where \(S=k^2\) is the standard right row module for \(M_2(B)\), with \(\epsilon\) acting as zero. Let \(Q\) be the right \(M_2(\Gamma)\)-projective

\[
Q=(E_{11}\otimes e_2)M_2(\Gamma)
 \simeq(P_2,P_2).
\]

It has dimension four, and

\[
Q(I_2\otimes e_1)\simeq(P_2e_1)^2=(kb)^2\simeq S,
\tag{A13}
\]

as actual \(M_2(B)\)-modules, since \(bc=bab=0\). Define the right projective \(\Lambda\)-module

\[
\widetilde M=\epsilon_+^{20}\oplus\epsilon_-^4\oplus Q^{20}.
\]

It has dimension \(20+4+20\cdot4=104\). Corner restriction gives

\[
\widetilde M f\simeq M_1,
\qquad
\operatorname{Hom}_\Lambda(P,\widetilde M)
 \simeq M_1
\tag{A14}
\]

as right \(A_1\)-modules, where the right endomorphism action on Hom is precomposition. This is an action-preserving realization, not merely equality of dimensions or characters. Both \(P\) and \(\widetilde M\) are projective objects in the smooth proper category. The original tensor module kills the radical, as it already did in F19; the separate endomorphism algebra (A11) retains the radical faithfully.

## 5. The full embedding and the precise failure of admissibility

For the basic corner, the functor

\[
I:\operatorname{Perf}(B)\longrightarrow\operatorname{Perf}(\Gamma),
\qquad X\longmapsto X\otimes_B^{\mathbf L}e_1\Gamma
\tag{A15}
\]

is well defined: it sends the generator \(B\) to the right projective \(P_1\). The right adjoint on the ambient derived categories is corner restriction \(Y\mapsto Ye_1\), because \(e_1\Gamma\) is projective on the \(\Gamma\)-side. Its unit is the isomorphism

\[
(X\otimes_B^{\mathbf L}e_1\Gamma)e_1
 \simeq X\otimes_B^{\mathbf L}B\simeq X.
\]

Therefore \(I\) is fully faithful. Matrix Morita equivalence and the scalar factors give the same fully faithful embedding \(\operatorname{Perf}(A_1)\to\operatorname{Perf}(\Lambda)\).

The image is not right-admissible. Indeed \(P_2e_1=kb\simeq k\) is not perfect over \(B\): the resolution

\[
\cdots\xrightarrow{\epsilon}B\xrightarrow{\epsilon}B
 \xrightarrow{\epsilon}B\longrightarrow k\longrightarrow0
\]

is exact, and tensoring it with \(k\) gives \(\operatorname{Tor}^B_i(k,k)=k\) in every degree. If \(I\) had a right adjoint with values in \(\operatorname{Perf}(B)\), its value at \(P_2\) would represent the functor

\[
X\longmapsto\operatorname{Hom}_{D(B)}(X,k)
\]

on perfect \(X\). Evaluating at \(B[n]\) would make that representing perfect object have only one cohomology module, namely \(k\) in degree zero; naturality for \(\operatorname{End}_B(B)=B\) gives its usual \(B\)-action. It would therefore be isomorphic to \(k\) in \(D(B)\), a contradiction. The same component obstructs right admissibility for the actual \(A_1\) corner.

This distinction is essential. The original \(M_1\) is not perfect over \(A_1\), so (A14) is an exact corner recovery from a projective object, not an application of (A15) to \(M_1\). It does not identify the higher coherent self-Ext groups of \(M_1\) with those of \(\widetilde M\). It also does not reconstruct the relative order-two collision or the crossed extension modules in F25 from this single special fiber.

## 6. A direct exceptional decomposition and its Frobenius consequence

There is an elementary full exceptional pair in \(\operatorname{Perf}(\Gamma)\):

\[
\langle S_1,P_2\rangle.
\tag{A16}
\]

To verify the statement, \(\operatorname{End}(P_2)=e_2\Gamma e_2=k\), and all its positive self-Ext vanish because \(P_2\) is projective. Applying Hom into \(S_1\) to (A3) gives \(\operatorname{End}(S_1)=k\) and no positive self-Ext, since \(\operatorname{Hom}(P_2,S_1)=S_1e_2=0\). The same equality proves \(R\operatorname{Hom}(P_2,S_1)=0\), the required semiorthogonality. The triangle from (A3) recovers \(P_1\) from \(S_1,P_2\), so these objects generate the entire perfect category. Each single-object exceptional subcategory has both adjoints, given by the finite derived Hom complexes and their duals; thus this is an actual semiorthogonal decomposition into two copies of \(\operatorname{Perf}(k)\).

For a finite field \(k=\mathbb F_q\), the known additivity of noncommutative Chow motives under such a decomposition gives

\[
U(\Gamma)_{\mathbb Q}\simeq U(k)_{\mathbb Q}^{\oplus2},
\qquad
U(\Lambda)_{\mathbb Q}\simeq U(k)_{\mathbb Q}^{\oplus4}.
\tag{A17}
\]

Tabuada states this additivity in Example12.3, p.24. His Frobenius-enriched TP functor, §6.2 equation(6.9), p.16, carries (A17) to an isomorphism with Frobenius, not merely a dimension equality. The point comparison in §7 equations(7.1)–(7.4), p.17, consequently gives

\[
TP_0(\Lambda)[1/p]\simeq K^4\quad\text{with }F_0=1,
\qquad TP_1(\Lambda)[1/p]=0,
\tag{A18}
\]

where \(K=\operatorname{Frac}W(k)\). There is no arithmetic Jordan ambiguity. In particular the noncommutative Weil statement holds for this smooth replacement.

The source also confirms the conclusion through its general connective smooth proper theorem: Theorem2.12, p.8, and its proof equation(12.6), p.26. That formula identifies the motive with the sum of the simple residue-field motives; here the residue fields are all \(k\). The direct exceptional proof above suffices for this special case. We do not assert nilinvariance for arbitrary nonsmooth dg algebras or identify the motive of the nonsmooth \(A_1\) with an object of the same smooth proper Chow category.

The source hypotheses match exactly: \(\Lambda\) is a finite-dimensional algebra concentrated in degree zero, hence connective and proper; (A8) and Morita invariance prove smoothness. The finite field supplies the stated cyclotomic Frobenius construction. Tabuada's Theorem2.13 is another applicable finite-dimensional smooth-algebra theorem, but it is not needed here. The general source theorems are cited inputs, not fully reproved.

## 7. What this repairs and what remains

F39's direct smoothness failure is repaired at the level of an explicit larger category. The actual collision algebra is an endomorphism algebra of a projective object, and its actual specialized tensor module is a Hom space between two projective objects, with all specified corner actions recovered. A nonzero nilpotent survives inside that smooth proper category. Hence F39 cannot be promoted to an assertion that no smooth categorical model can retain the collision algebra.

The coefficient spectrum of the entire smooth category is nevertheless the four unit eigenvalues in (A18). No theorem here identifies that spectrum with a based multiplication coefficient, with the nonstandard tensor-module action on an \(\ell\)-adic space, or with a positive canonical basis. TP is an invariant of the category and is not automatically a faithful realization of every object, morphism, or specified corner action. Moreover (A15) is not admissible, so its existence does not place the nonsmooth category inside the smooth proper motivic category as a direct summand. The relative family, its collision order, and a comparison preserving the required based operations remain additional tasks.

## 8. Grothendieck dictionary and exact source record

The construction uses affine endomorphism algebras, projective modules, perfect diagonals, and idempotent corners. These fit the affine coherent-module and perfect-complex dictionary of EGA and SGA6. Its modern smooth dg and noncommutative Chow/TP framework is explicitly Tabuada's cited theory. The archived projector and conditional semisimplicity notes are vocabulary anchors only; no Auslander construction or nonstandard comparison is attributed to those leaves.

Primary source: Gonçalo Tabuada, *Noncommutative Weil conjecture*, arXiv:1808.00950v7. Inspected file identifies version7 as 6 December2019, with manuscript date9 December2019. URL: https://arxiv.org/pdf/1808.00950 .

Exact inspected locators: §5.1 pp.13–14 (smooth/proper); §6.2 equation(6.9), p.16 (enriched TP); §7 equations(7.1)–(7.4), p.17; Example12.3 p.24 (semiorthogonal additivity); Theorem2.12 p.8 and proof(12.6) p.26. The latter cites Raedschelders–Stevenson for its general connective motive decomposition; their original general proof was not read here and is not needed for our explicit exceptional pair.

Search references reopened or newly retrieved in this check: `turn608497332view0`, `turn698137661view0`, `turn698137661view2`, `turn698137661view3`, `turn722522903view1`, `turn820210169view0`.

All new elementary claims (A1)–(A16), including the full diagonal resolution, action-preserving corner construction, and non-right-admissibility proof, are provided in full above. The motives/TP implication (A17)–(A18) is a stated application of the precisely cited known machinery. A next lead, not a result here, is a relative Auslander order built from \(C\oplus L_1\oplus L_2\), or intermediate collision orders, that might retain F25's order-two deformation information.
