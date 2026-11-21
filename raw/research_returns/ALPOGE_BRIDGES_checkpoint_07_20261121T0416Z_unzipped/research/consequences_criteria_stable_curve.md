# Universal stable curves: exact stack purity and decomposition

Research module `consequences_criteria`; GPT-6 Astra Pro; effort setting not exposed; 20 November 2026. This module uses established finite-field weight theory independently of the adopted Alpöge RH and Dirichlet GRH. New deductions below are supplied with complete proofs. No claim is made about independent reconstruction of the foundational BBD or stack six-functor theorems.

## CC-ST01. Verified stack theorem and its application

**Primary theorem.** Sun (2012), arXiv:1009.4398v3, Theorem 1.2, p. 3, treats proper morphisms of finite diagonal between finite-type stacks over a finite field with affine stabilizers. For a pure input, it gives a decomposition into shifted semisimple perverse cohomology **after extension to the algebraic closure**. The convention removing the subscript 0 is explicit in §1.3.3, p. 3. The weight calculation uses Proposition 3.9(iii), p. 8, and Theorem 3.5, p. 6; geometric semisimplicity and splitting are Theorems 3.11–3.12, p. 8, with the application proved in §3.13, p. 9. These are arXiv printed-page locators, not guessed journal-page translations. [Primary PDF](https://arxiv.org/pdf/1009.4398v3).

**Geometric hypotheses.** Let $g,n\geq0$ satisfy $2g-2+n>0$, let $q$ be a power of $p$, and let $\ell\ne p$. Set
$$
Y_0=\overline{\mathcal M}_{g,n,\mathbf F_q},\qquad
X_0=\overline{\mathcal M}_{g,n+1,\mathbf F_q},\qquad
\pi_0:X_0\longrightarrow Y_0,
$$
where the last marking is forgotten and the curve stabilized. Put $d=3g-3+n$ and $D=d+1$. Knudsen (1983), Corollary 2.6 and Theorem 2.7, p. 179, identify contraction and stabilization as inverse constructions and give the smooth proper moduli stacks with normal-crossing boundary. Knudsen (2012), introduction, pp. 1–2, explicitly verifies that $\pi_0$ is representable and is the universal stable curve, hence is proper and flat with geometrically connected nodal curve fibres. The local expression $t_i\mapsto xy$ is also printed in the proof of Knudsen's Theorem 2.7 on p. 179. [Original journal PDF](https://journals.msp.org/mscand/article/download/1622/1621/1653); [author's later clarification](https://arxiv.org/pdf/1106.1588v2).

With $\Lambda=\overline{\mathbf Q}_\ell$ and a fixed embedding $\iota:\Lambda\hookrightarrow\mathbf C$, define
$$
K_0=\Lambda_{X_0}[D]=\mathrm{IC}_{X_0},\quad
L_0=R\pi_{0*}K_0,\quad
P_{i,0}={}^p\!H^i(L_0).
$$
Then $L_0$ is pure of weight $D$, and $P_{i,0}$ is pure of weight $D+i$. After base change to $\overline{\mathbf F}_q$, there is a noncanonical isomorphism
$$
L\simeq\bigoplus_{i\in\mathbf Z}P_i[-i],
$$
and every $P_i$ is a semisimple perverse sheaf, hence a finite direct sum of intersection complexes of irreducible lisse sheaves on smooth locally closed substacks.

**Complete application proof.** Stability makes all geometric stabilizers finite, so they are affine. The moduli stacks are of finite type. Since $\pi_0$ is representable and proper, its relative diagonal is a closed immersion and therefore finite. Thus the hypotheses on the morphism in Sun's theorem hold; arbitrary Artin stacks would not suffice.

The dimension formula may be checked on the dense smooth-curve locus. The tangent space of a smooth pointed curve is $H^1(C,T_C(-\sum p_i))$. Stability gives $H^0(C,T_C(-\sum p_i))=0$, and Riemann–Roch gives its dimension $3g-3+n$. The normal-crossing boundary has empty interior, and the stack is smooth, so this is its dimension on every component. The total space has dimension $D=d+1$.

The constant sheaf on the smooth stack $X_0$ has weight zero. With cohomological shifts, $K_0$ is perverse and pure of weight $D$; equivalently, its unique ordinary cohomology sheaf sits in degree $-D$ and its Verdier dual is $K_0(D)$. Properness gives $R\pi_{0!}=R\pi_{0*}$ in this finite-diagonal setting. The upper and lower weight bounds of Sun's Proposition 3.9(iii) therefore give both inequalities needed for purity of $L_0$. His Theorem 3.5 gives the weights $D+i$. Finally, Theorems 3.11–3.12 give the asserted geometric decomposition and semisimplicity. The description of simple perverse objects is precisely the one used in Sun's Theorem 3.11, citing Laszlo–Olsson, Theorem 8.2(ii). This proves the stated application. $\square$

**Scope of the conclusion.** A pure complex need not have every ordinary stalk cohomology group pure of its cohomological degree. In particular, the statement about $R\pi_{0*}\Lambda$ being pure of weight zero does not assert that the $H^1$ of every nodal fibre is pure of weight one. The latter generally has both graph and normalization contributions. Neither arithmetic semisimplicity nor a Frobenius-equivariant choice of the displayed splitting follows merely by retaining Sun's conclusion over $\mathbf F_q$; the theorem explicitly takes the geometric base change. Decomposition is not a smooth-local property that can simply be descended from scheme charts: Sun gives a counterexample in his introduction, pp. 1–2.

## CC-ST02. Three perverse degrees and their endpoint summands

In the preceding situation, the only possibly nonzero $P_{i,0}$ have $i=-1,0,1$. Their weights are respectively $d,d+1,d+2$. Geometrically, the endpoints are
$$
P_{-1}\simeq\Lambda_Y[d],\qquad
P_1\simeq\Lambda_Y[d](-1).
$$
Consequently the constant-coefficient direct image admits a noncanonical geometric decomposition
$$
R\pi_*\Lambda_X\simeq
\Lambda_Y\;\oplus\;P_0[-d-1]\;\oplus\;\Lambda_Y(-1)[-2].
\tag{CC-ST.1}
$$
If $U=\mathcal M_{g,n,\overline{\mathbf F}_q}\subset Y$ is the smooth-curve locus, then
$$
P_0|_U\simeq (R^1\pi_*\Lambda)|_U[d].
$$
The middle perverse sheaf can include boundary-supported summands; equation (CC-ST.1) does not discard them.

**Complete proof.** Proper base change and the cohomological dimension of a proper curve give $R^j\pi_*\Lambda=0$ for $j\notin\{0,1,2\}$. Thus the ordinary cohomology of $L$ is zero outside degrees $-d-1,-d,1-d$. For each of these degrees $k$, the support has dimension at most $d\leq1-k$. The support criterion for the middle perverse $t$-structure therefore gives $L\in{}^pD^{\leq1}$. The criterion is checked on an étale atlas; relative dimension zero means no additional stack shift occurs.

Because $X$ is smooth of dimension $D$, Verdier duality gives $\mathbb D_XK=K(D)$. Proper duality then gives $\mathbb D_YL=L(D)$. Perverse duality interchanges ${}^pD^{\leq1}$ and ${}^pD^{\geq-1}$, and Tate twisting preserves these categories, so $L\in{}^pD^{\geq-1}$. Hence $P_i=0$ for $|i|>1$. The same vanishing holds before geometric base change, since that pullback is conservative and perverse exact. The weight assertions now follow from CC-ST01.

To identify $P_1$, use its geometric semisimplicity. A simple constituent with support of dimension $s$ restricts on a dense smooth part of that support to a nonzero lisse sheaf shifted by $s$. Its contribution through the direct summand $P_1[-1]\subset L$ therefore has nonzero ordinary cohomology in degree $1-s$. But $L$ has no ordinary cohomology above $1-d$. Consequently $1-s\leq1-d$, so $s=d$: every simple constituent of $P_1$ has full support on a component of $Y$.

Over $U$, smooth proper base change identifies $P_1|_U$ with $R^2\pi_*\Lambda[d]|_U=\Lambda_U[d](-1)$, since the fibres are geometrically connected smooth proper curves. A semisimple perverse sheaf whose constituents all have full support is the intermediate extension of its restriction to a suitable dense open. Since $Y$ is smooth and the local system just obtained is constant, this intermediate extension is $\Lambda_Y[d](-1)$, component by component. This gives $P_1$.

Perverse duality also gives $\mathbb D_YP_1=P_{-1}(D)$. On the smooth $d$-dimensional stack $Y$,
$$
\mathbb D_Y(\Lambda_Y[d](-1))=\Lambda_Y[d](d+1)=\Lambda_Y[d](D),
$$
so $P_{-1}=\Lambda_Y[d]$. Substitute these two identifications in $L\simeq P_{-1}[1]\oplus P_0\oplus P_1[-1]$ and shift by $-D$ to obtain (CC-ST.1). The same calculation of perverse degree on $U$ identifies the middle term with $R^1\pi_*\Lambda[d]$. Every asserted step has now been proved. $\square$

## CC-ST03. Why geometric semisimplicity does not imply arithmetic semisimplicity

Over $\operatorname{Spec}\mathbf F_q$, let Frobenius act on $\Lambda^2$ by
$$
F=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$
This is a continuous $\ell$-adic representation: the homomorphism $\widehat{\mathbf Z}\to\mathbf Z_\ell$ followed by $a\mapsto\left(\begin{smallmatrix}1&a\\0&1\end{smallmatrix}\right)$ provides it, with the generator chosen as geometric Frobenius. All eigenvalues are one, so the associated sheaf is punctually pure of weight zero. It is not arithmetically semisimple, since its only Frobenius-fixed line has no invariant complement. After pullback to $\operatorname{Spec}\overline{\mathbf F}_q$, the Galois action disappears and the sheaf is a sum of two constant rank-one sheaves. This fully explicit example shows why purity alone does not license the stronger arithmetic conclusion. It does not assert that the particular universal-curve decomposition has no arithmetic refinement.

## CC-ST04. Complete geometric support formula, including the separating boundary

Write $j:U=\mathcal M_{g,n,\overline{\mathbf F}_q}\hookrightarrow Y$ and $\mathbb V=(R^1\pi_*\Lambda)|_U$. For each irreducible separating boundary divisor $D\subset Y$, let $D^\circ$ be its open locus of curves with exactly one node. Let $\mathcal C_D\to D^\circ$ be the finite étale two-element cover that chooses one of the two irreducible components of the fibre. Define the rank-one local system
$$
\epsilon_D=\Lambda[\mathcal C_D]/\Lambda\mathbf 1.
$$
Here $\Lambda\mathbf1$ is the diagonal constant sub-local system of the component permutation local system. For a locally closed immersion $k_D:D^\circ\hookrightarrow Y$, the notation $(k_D)_{!*}$ means intermediate extension to its closure followed by the closed pushforward to $Y$.

There is a geometric isomorphism of semisimple perverse sheaves
$$
P_0\simeq j_{!*}(\mathbb V[d])\;\oplus\!
\bigoplus_{D\text{ separating}}(k_D)_{!*}\bigl(\epsilon_D[d-1]\bigr)(-1).
\tag{CC-ST.2}
$$
Thus substituting (CC-ST.2) into (CC-ST.1) determines every perverse support and its coefficient system. There are no simple constituents whose support has codimension at least two, and no constituent supported on a nonseparating boundary divisor. Intersection complexes in the formula can nevertheless have nonzero stalks on deeper boundary strata.

The local system $\epsilon_D$ is the sign of the permutation of the two components. If those components are distinguished by their genera or by the labelled markings, it is constant. In the standard labelled moduli problem, the only boundary type allowing exchange is $n=0$, $g$ even, with genera $g/2$ and $g/2$; there one must retain the component-exchange local system on the stack. A twist of weight two is essential: the coefficient system on $D^\circ$ is $\epsilon_D(-1)$, so its intermediate extension has perverse weight $2+(d-1)=d+1$.

**Complete proof.** A simple constituent of $P_0$ supported in dimension $s$ contributes ordinary cohomology to $L$ in degree $-s$ on a dense smooth part of its support. The upper ordinary degree bound $1-d$ from CC-ST02 forces $-s\leq1-d$, hence $s\geq d-1$. Every proper support is therefore a divisor. Since $P_0|_U=\mathbb V[d]$ is lisse in one ordinary degree, no such proper support meets $U$. The full-support sum is $j_{!*}(\mathbb V[d])$; all other possible constituents lie on boundary divisors.

Fix such a divisor and remove its intersections with other boundary branches and any smaller loci needed to make its restrictions lisse. On the resulting open set, write $i:D^\circ\hookrightarrow Y$ for the closed smooth divisor and $A=j_{!*}(\mathbb V[d])$. The intermediate-extension property gives ${}^pH^0(i^*A)=0$. Also $i^*A\in{}^pD^{\leq0}$. On the smooth $(d-1)$-dimensional divisor the perverse structure on lisse complexes is the ordinary structure shifted by $d-1$, so
$$
\mathcal H^{1-d}(i^*A)=0.
$$
The required intermediate-extension vanishing is stated for stacks in Laszlo–Olsson (2009), Lemma 6.1, author-preprint p. 10; only this vanishing implication is used here.

Taking ordinary cohomology in degree $1-d$ in the geometric decomposition of $L$ now gives, on $D^\circ$,
$$
(R^2\pi_*\Lambda)|_{D^\circ}\simeq
\Lambda_{D^\circ}(-1)\oplus E_D,
\tag{CC-ST.3}
$$
where $E_D[d-1]$ is the restriction of the sum of the divisor-supported constituents of $P_0$. The first term comes from $P_1[-1]$, and $P_{-1}[1]$ contributes nothing in this degree. No full-support middle term contributes by the vanishing just proved.

For a connected proper nodal curve, normalization identifies $H^2$ with the sum of $\Lambda(-1)$ over its irreducible components: the difference between the curve and its normalization is supported at finitely many nodes and has no cohomology in degree two. This identification is functorial, so over the one-node locus $R^2\pi_*\Lambda$ is exactly the component permutation local system with a Tate twist. A nonseparating node leaves the curve irreducible, giving a rank-one system; (CC-ST.3) then forces $E_D=0$.

A separating node gives precisely two components. Their monodromy permutation group is either trivial or the order-two group. In the trivial case, every rank-one quotient by a constant line is constant. In the order-two case, the constant subrepresentation is the unique invariant line, and the quotient is the sign representation. Since the coefficients have characteristic zero, these permutation representations are semisimple. Equation (CC-ST.3) therefore gives $E_D\simeq\epsilon_D(-1)$ in both cases. Intermediate extension uniquely determines each semisimple divisor-supported sum from this dense-open restriction, which proves (CC-ST.2).

Finally, a component exchange preserves genus and each labelled marking. It is impossible when the genera differ or when any labelled marking lies on either component. If $n=0$ and the two genera agree, the two components are unordered and their exchange is exactly the finite permutation character retained in $\epsilon_D$. This proves the last description and completes the proof. $\square$

## References

Knudsen, F. F. (1983). The projectivity of the moduli space of stable curves, II: The stacks $M_{g,n}$. *Mathematica Scandinavica, 52*, 161–199. https://doi.org/10.7146/math.scand.a-12001 . Original article, Corollary 2.6 and Theorem 2.7, p. 179, visually inspected at https://journals.msp.org/mscand/article/download/1622/1621/1653 .

Knudsen, F. F. (2012). *A closer look at the stacks of stable pointed curves* (arXiv:1106.1588v2). https://arxiv.org/abs/1106.1588v2 . Introduction, pp. 1–2, directly inspected. The version inspected supplies the author's clarification of the contraction/stabilization construction.

Laszlo, Y., & Olsson, M. (2009). Perverse $t$-structure on Artin stacks. *Mathematische Zeitschrift, 261*(4), 737–748. https://doi.org/10.1007/s00209-008-0348-z . Author preprint, Theorem 8.2(ii), p. 12: https://www.cmls.polytechnique.fr/perso/laszlo/articleweb/faisceaux-pervers.pdf . Statement directly inspected; its whole foundational proof is not reconstructed here.

Sun, S. (2012). Decomposition theorem for perverse sheaves on Artin stacks over finite fields. *Duke Mathematical Journal, 161*(12), 2297–2310. https://doi.org/10.1215/00127094-1723657 . Inspected version: https://arxiv.org/pdf/1009.4398v3 . Exact theorem and page locators are given above.
