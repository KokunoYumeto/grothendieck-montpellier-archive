# F43: an actual positive rank-three bimodule action, its bar, and exact categorical limits

Author: `/root/rectangular_and_theta`. Date: 2026-11-21 UTC. This is an explicit deduction from the actual F21 matrices, strengthened by a direct calculation of the ordinary left action and the actual tensor-product bar. It is not a claim of priority for a rank-three canonical basis: revised GCT IV already gives a more specifically based rank-three example. The statement here identifies exactly what this regular adapted basis does, including a positive path model and what that model fails to preserve.

## 1. Primary conventions and exact source locators

The supplied primary file is `sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`. Its complete contexts used below were read directly. The published arXiv PDF was freshly opened at https://arxiv.org/pdf/cs/0703110 and its first page identifies cs/0703110v4, 6 June 2013.

| Input | Exact locator |
|---|---|
| Upper canonical basis of the ordinary rank-eight tensor module, explicitly in tensor monomials | Figure 1, printed p.9; source lines 1043–1085, label `f c_111 example upper` |
| Ordinary quantum-group bar and coproduct | §4.1, equations (28)–(29), printed p.22; source lines 1754–1768, label `e U_q coproduct` |
| Tensor-monomial action and commuting ordinary left/right actions | §6.1, printed p.33; source lines 2303–2332 |
| Actual tensor bar and upper canonical basis | §6.2, Theorem 6.4, printed p.34; source lines 2344–2384 |
| Actual nonstandard generators | Definition 11.1, equation (93), with the consistent §3.1 normalization already used in F21 |
| Two-dimensional right-row modules | Proposition 11.14 and equation (110), pp.64–65 |
| The factor-swap extension and its sign representations | §13.1–§13.3; source lines 4383–4445 |
| Existing rank-three based construction | §19.1, Example 19.2, printed pp.132–133 |
| Warning about its changed integral form and local lattice | Paragraph after Conjecture 19.1, source lines 7968–7977 |

Fresh PDF refs: `turn233608546view0`–`turn233608546view3`; another agent independently recovered the same locators. For VIII the supplied `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex` was read at source lines 690–850 and 1380–1475: the prescribed bar, local lattices, duality and degree-minimizing globalization are additional data, not a declaration that any bar-fixed positive basis is canonical.

All modules below use the source's right-row convention for right generators. When a left linear operator is also displayed by rows, its row records its action on a basis vector; it commutes with the right action, with no change in the underlying left-module convention.

## 2. Statement: stronger than the right-action assertion alone

Put

\[
\Lambda=\mathbf Z[v,v^{-1}],\quad
\delta=v+v^{-1},\quad D=\delta^2,
\quad h=D-1=v^2+1+v^{-2},
\quad S=\Lambda[(2h)^{-1}].
\tag{P1}
\]

Let \(M_\Lambda=(\Lambda^2\otimes\Lambda^2)^{\otimes3}\) with the actual right nonstandard tensor action. There is an explicitly defined full-rank free sublattice \(L\subset M_\Lambda\), with basis \(\mathcal B\), such that:

1. \(L\otimes S=M_\Lambda\otimes S\). The change-of-row-basis determinant is \(\pm2^{12}h^{72}\), so this is a genuine basis of the actual tensor lattice after this finite localization. In particular it is regular at \(v=1\) in characteristic different from 2 and 3. Neither \(\delta\), \(D-2\), nor the colliding-root difference must be inverted for this assertion.
2. Both actual right generators \(P_1,P_2\) have matrices in \(\mathbf N[v,v^{-1}]\) on \(\mathcal B\).
3. The actual ordinary left operators \(E_V,F_V,E_W,F_W\), and the weight operators \(K_V^{\pm1},K_W^{\pm1}\), also have nonnegative Laurent matrices on this same basis.
4. Every vector of \(\mathcal B\) is fixed by the actual ordinary tensor-product bar from IV, not merely by a newly transported involution.
5. The full regular commutant of the right action is
\[
\mathcal C_S=\operatorname{End}_{A_S}(M_S)
\cong M_{20}(S)\times M_4(S)\times M_{16}(S)\times M_4(S).
\tag{P2}
\]
Its elementary matrix-unit basis acts by matrices with entries 0 or 1 on \(\mathcal B\), simultaneously with the above positive actions. Its multiplication constants are 0 or 1. This is an actual commutant action on the given module, not a trace-equivalent replacement.

The positive right matrices were already explicit in F21. Assertions 3–5 and the actual bar calculation strengthen the previously recorded scope. They do not identify the chosen basis or commutant matrix units with VIII's designated global bases.

## 3. Complete ordinary rank-eight calculation

Write \(\mathbf v_{ijk}\) for tensor monomials, and use the four vectors

\[
b_0=\mathbf v_{111},\quad
b_1=v^2\mathbf v_{112}+v\mathbf v_{121}+\mathbf v_{211},
\]
\[
b_2=v^2\mathbf v_{122}+v\mathbf v_{212}+\mathbf v_{221},
\quad b_3=\mathbf v_{222}.
\tag{P3}
\]

The remaining four vectors are

\[
u_{+,1}=-(1+v^{-2})\mathbf v_{112}+v\mathbf v_{121}+\mathbf v_{211},
\]
\[
u_{+,2}=-v^{-1}\mathbf v_{112}-v^{-2}\mathbf v_{121}+\delta\mathbf v_{211},
\]
\[
u_{-,1}=-v^{-1}\mathbf v_{122}-v^{-2}\mathbf v_{212}+\delta\mathbf v_{221},
\]
\[
u_{-,2}=-(1+v^{-2})\mathbf v_{122}+v\mathbf v_{212}+\mathbf v_{221}.
\tag{P4}
\]

These are exactly the F21 changes on the two three-dimensional weight spaces, with the two last rows interchanged for the second weight space. The determinant of the full change on \((\Lambda^2)^{\otimes3}\) is \(\pm h^4\), by the two determinants \(\det B_3=h^2\) already proved in F21.

Let \(W_3\) have basis \(b_0,b_1,b_2,b_3\), let \(W_1\) have basis \(g_+,g_-\), and let \(U\) have basis \(e_1,e_2\), identifying \(u_{\pm,j}=g_\pm\otimes e_j\).

Here the subscript on \(W_j\) is the \(\mathfrak{sl}_2\) highest weight: as polynomial \(GL_2\)-modules the two labels are \((3)\) and \((2,1)\), respectively. In particular \(W_1\) retains the determinant twist and total polynomial degree three. The actual ordinary right Hecke action is

\[
(\Lambda^2)^{\otimes3}\otimes S
=(W_3\otimes\epsilon)\oplus(W_1\otimes U),
\]
\[
c_i|_\epsilon=\delta,qquad
c_1|_U=\begin{pmatrix}\delta&0\\1&0\end{pmatrix},\quad
c_2|_U=\begin{pmatrix}0&1\\0&\delta\end{pmatrix}.
\tag{P5}
\]

The source coproduct is
\(\Delta(E)=E\otimes K^{-1}+1\otimes E\),
\(\Delta(F)=F\otimes1+K\otimes F\), with \(Kv_1=vv_1\), \(Kv_2=v^{-1}v_2\).
On a three-letter tensor word, \(E\) changes a 2 to a 1 with coefficient \(v^{-\sum_{\text{later positions}}\mathrm{wt}(i)}\); \(F\) changes a 1 to a 2 with coefficient \(v^{\sum_{\text{earlier positions}}\mathrm{wt}(i)}\), where \(\mathrm{wt}(1)=1\), \(\mathrm{wt}(2)=-1\). Substitution in (P3)–(P4) gives the entire left action:

\[
F b_0=b_1,\quad F b_1=\delta b_2,\quad F b_2=h b_3,\quad F b_3=0,
\]
\[
E b_0=0,\quad E b_1=h b_0,\quad E b_2=\delta b_1,\quad E b_3=b_2,
\]
\[
F g_+=g_-,\quad Fg_-=0,\quad Eg_-=g_+,\quad Eg_+=0.
\tag{P6}
\]

On \(b_j\), \(K\) acts by \(v^{3-2j}\); on \(g_\pm\), by \(v^{\pm1}\). It acts identically on the Specht factor \(U\). This verifies positivity of every named ordinary operator, with no generic semisimplicity argument replacing the integral matrix check.

### The actual bar, not an invented one

In the ordered weight space \((112,121,211)\), IV Figure 1 gives the actual upper canonical basis

\[
c_{112}=\mathbf v_{112},\quad
c_{121}=\mathbf v_{121}-v^{-1}\mathbf v_{112},\quad
c_{211}=\mathbf v_{211}-v^{-1}\mathbf v_{121}.
\]

All three are fixed by the specified tensor-product bar. The coefficients of \((b_1,u_{+,1},u_{+,2})\) in this basis are

\[
\begin{pmatrix}h&\delta&1\\0&\delta&1\\0&1&\delta\end{pmatrix}.
\tag{P7}
\]

Every coefficient is bar invariant. The second weight space has the same formula, with the last two rows interchanged, by the second triple in Figure 1. The two endpoint monomials are also canonical and fixed. Thus all eight vectors are fixed by the source bar. This proves the claim directly rather than inferring bar invariance from positivity.

## 4. Full rank-three bimodule, determinant, and commutant

Regroup the actual tensor module as \((\Lambda^2)^{\otimes3}\otimes(\Lambda^2)^{\otimes3}\), apply (P5) in each factor, and apply the F21 matrix

\[
B_4=\begin{pmatrix}
\delta&-1&-1&\delta\\
0&-1&1&0\\
2-D&-\delta&-\delta&D\\
-D&\delta&\delta&D-2
\end{pmatrix}
\tag{P8}
\]

only to each Specht factor \(U\otimes U\). Its determinant is \(8h^2\). It gives \(\epsilon_+\oplus\epsilon_-\oplus N(D-2)\). The mixed \(\epsilon\otimes U\) factors give \(N(\delta)\), where

\[
N(a):\quad P_1=\begin{pmatrix}D&0\\a&0\end{pmatrix},\qquad
P_2=\begin{pmatrix}0&a\\0&D\end{pmatrix}.
\tag{P9}
\]

The resulting **bimodule** decomposition is

\[
M_S=(W_3\otimes W_3\oplus W_1\otimes W_1)\otimes\epsilon_+
\]
\[
\quad\oplus(W_1\otimes W_1)\otimes\epsilon_-
\quad\oplus(W_3\otimes W_1\oplus W_1\otimes W_3)\otimes N(\delta)
\]
\[
\quad\oplus(W_1\otimes W_1)\otimes N(D-2).
\tag{P10}
\]

The multiplicity ranks are \(20,4,16,4\). The left \(V\)- and \(W\)-operators act on the displayed corresponding \(W_j\) factors, by (P6); changing only the Specht factors by (P8) leaves their matrices unchanged. This proves simultaneous actual left/right positivity. The two right coefficients are \(D=v^2+2+v^{-2}\), \(a=\delta=v+v^{-1}\), or \(a=D-2=v^2+v^{-2}\), all positive Laurent polynomials.

The ordinary tensor bar for the direct-product quantum group is the product of the two ordinary tensor bars under this regrouping. This follows either from its quasi-R factors \(\Theta_V\Theta_W\), which act on separate factors, or directly from the source's product based-module construction. Formula (P8) has bar-invariant coefficients. Consequently every final basis vector remains fixed by the actual bar. The construction is compatible with \(E,F\) being bar fixed and \(K\) being sent to \(K^{-1}\).

For the determinant, the ordinary rank-eight change has determinant \(\pm h^4\). Its tensor square has determinant \(h^{64}\), using \(\det(T\otimes T)=\det(T)^{16}\). There are four copies of (P8), contributing \((8h^2)^4=2^{12}h^8\). Permutations only affect a sign. Thus the final determinant is exactly \(\pm2^{12}h^{72}\). The basis vectors all have coefficients in \(\Lambda\); their span is a free full-rank sublattice and becomes the actual entire lattice over \(S\).

For the commutant, the four generic simple types in (P10) are distinct, so every cross homomorphism over the domain \(S\) vanishes after passage to its fraction field and hence vanishes. Alternatively the central operator \((P_1-P_2)^2\) has scalars \(0,D(D-1),4(D-1)\) on the scalar, \(N(\delta)\), and \(N(D-2)\) sectors, respectively; these distinguish the sectors over the fraction field, and \(P_1\) distinguishes \(\epsilon_+\) from \(\epsilon_-\).

The endomorphism ring of each rank-two block is exactly \(S\). To see this without an integrality assumption from generic Schur's lemma, let \(X=\left(\begin{smallmatrix}u&v'\\w&z\end{smallmatrix}\right)\) commute with both matrices in (P9). Since \(a\ne0\) and \(S\) is a domain, the first equality forces \(v'=0\), the second forces \(w=0\), and then \(a(u-z)=0\) gives \(u=z\). This proves (P2). Its elementary matrix units send one multiplicity basis vector to another and preserve the right factor, so they have only 0/1 entries on (P10). They also commute with the bar, because the basis is bar fixed and their coefficients are integers.

This is the full integral commutant for this localized module. The known generic nonstandard Schur–Weyl theorem identifies its fraction-field algebra with the degree-three Schur action. No equality with every integral form of the dual FRT algebra, and no compatibility across all tensor degrees, is inferred.

## 5. All words: exact matrix products and trace formula

For \(i=1,2\), write \(P_i=u_i e_i^T\) in (P9), with
\(u_1=(D,a)^T\), \(u_2=(a,D)^T\).
Let \(w=i_1\cdots i_L\) be nonempty, and let \(t\) count its ordinary adjacent changes \(i_j\ne i_{j+1}\), \(1\le j<L\). Multiplication of rank-one matrices gives the **entire matrix**, not merely its trace:

\[
P_w=D^{L-1-t}a^t u_{i_1}e_{i_L}^T.
\tag{P11}
\]

For the trace, include the final cyclic comparison \(i_L\ne i_1\). Its cyclic transition count \(c\) is even, say \(c=2s\), because a cyclic binary word returns to its initial letter. Therefore

\[
\operatorname{Tr}_{N(a)}(P_w)=D^{L-2s}a^{2s},
\]
\[
\boxed{\operatorname{Tr}_{M}(P_w)
=20D^L+16D^{L-s}+4D^{L-2s}(D-2)^{2s}.}
\tag{P12}
\]

The empty word has trace 64. A one-letter-power word has trace \(40D^L\). For \(w=(12)^m\), (P12) gives \(20D^{2m}+16D^m+4(D-2)^{2m}\), as independently derived by the parent and the other reviewer. Every term in these formulas is coefficientwise nonnegative Laurent.

## 6. A finite-state graded positive path model for the actual action

Use the 64 states in \(\mathcal B\). For each chosen operator, replace an entry \(\sum_d n_d v^d\) by \(n_d\) directed edges of degree \(d\). Thus a \(P_1\) block has a loop at state 1 with degree multiset \(\{-2,0,0,2\}\) and an edge from state 2 to 1 with degrees \(\{-1,1\}\) or \(\{-2,2\}\); \(P_2\) is the reflected reset to state 2. Each scalar plus state has the same four-degree loop for each generator; the scalar minus states have no such edges. The ordinary left operators and commutant matrix units have the finite edges specified in (P6) and (P2).

For every word in these selected operators, its matrix entry from state \(s\) to state \(t\) is the generating polynomial of directed paths from \(s\) to \(t\) with that sequence of edge colors, graded by total degree. This follows by ordinary matrix multiplication and induction on word length. Closed paths give the ordinary matrix trace. Because the matrices are the actual conjugated operators, this realizes the actual action after localization, rather than substituting another pair with the same traces.

For explicitly written words of length \(L\), this is an efficient positive counting rule for these fixed-rank action coefficients. A right-generator step has at most four outgoing labeled edges, an \(E/F\) step at most three, and a \(K^{\pm1}\) or elementary commutant step at most one; every degree lies between \(-3\) and 3. There are at most \(4^L\) paths from a fixed starting state and at most \(64\cdot4^L\) closed paths in total. A path witness and the count therefore have \(O(L)\) bits. A dynamic program on the 64 states and accumulated degrees in \([-3L,3L]\) computes each requested coefficient in polynomial bit time; an encoded degree outside that range gives zero. This assertion uses the explicit word length, not run-length or binary-power compression, and fixes the tower rank at three. It does not give a rule for general Kronecker inputs or a succinct PH1 bound.

One can make the grading categorical without making an arithmetic claim. Let \(\mathcal V\) be the category of finite-dimensional \(\mathbf Z\)-graded vector spaces and let \(\mathcal V^{64}\) be its 64-fold product. For each matrix entry use the graded space having the indicated homogeneous basis, and define the corresponding exact functor by direct sums of tensor products with these spaces. Composition is path concatenation; the graded Grothendieck group is \(\Lambda^{64}\), with exactly the displayed action. A word has an actual finite trace object given by the direct sum of its diagonal kernel spaces. This gives all words from fixed finite graded kernels, but the resulting trace object depends on the word. It is not a trace of all words on one fixed finite Weil space under repeated parameter substitution.

The quadratic relation lifts by the elementary tensor symmetry: after a reset, a second identical letter contributes the degree polynomial \(D\). General linear algebra relations are asserted here on the Grothendieck group. A coherent lift of all nonstandard linear relations, prescribed 2-morphisms, or a functor from a designated GCT category is not proved by this construction.

There is a further grading distinction if one later adds arithmetic data. Formula (P12) contains only even powers of \(v\), so the substitution \(v=q^{n/2}\) has integral Tate exponents at the level of closed-word trace polynomials. The individual \(N(\delta)\) entries contain \(v^{\pm1}\), however, and that same substitution requires a weight-one Weil line or a half-Tate convention at the entry level. It is not automatically a geometric Tate object. Taking \(v=q^n\) instead uses one full Tate step, with a different normalization. No such arithmetic comparison is included in the formal graded assertion.

## 7. Why closure under arbitrary summands loses the actual order

This limit can be proved directly in the new positive embedding. On the faithful six-dimensional module containing one copy of each simple type, the matrices in (P9) for \(N(\delta)\) and \(N(D-2)\) become **identical** at \(v=1\). Therefore every element of the actual regular algebra generated by \(P_1,P_2\) has identical matrices on those two blocks after specialization. This remains true for the actual localized rank-ten algebra; no difference of the colliding roots is inverted.

In the semisimple matrix-functor category, however, the \(P_1\) kernel has a direct summand which is a single degree-zero loop at state 1 of the \(N(\delta)\) block and zero elsewhere. Its Grothendieck action is the matrix unit \(E_{11}\) supported only on that branch. At \(v=1\), it is nonzero on \(N(\delta)\) and zero on \(N(D-2)\). It therefore cannot be the action of an element of the actual regular algebra.

Thus closing this matrix-functor construction under all direct summands introduces operators outside the actual nonstandard order, even after removing all redundant multiplicity copies. This is a concrete collision obstruction, not merely a complaint that a category was unspecified. The positive action and the exact word functors survive; a summand-closed category retaining precisely the actual algebra requires additional restrictions or structure.

## 8. Two further exact boundaries of the positive basis

### The actual factor swap

When \(V=W\), let \(\tau\) interchange the two ordinary tensor factors. On the \(U\otimes U\) Specht factor, the first, third and fourth rows of (P8) are symmetric under interchange; its second row \((0,-1,1,0)\) is antisymmetric. Hence on the \(\epsilon_-\) multiplicity space \(W_1\otimes W_1\),

\[
\tau=-\operatorname{flip},\qquad \operatorname{Tr}(\tau)=-2.
\tag{P13}
\]

This agrees with IV's signed extension \(\mathcal X_{-(2,1)}\). No basis of this invariant four-dimensional summand can have a coefficientwise nonnegative Laurent matrix for \(\tau\), since its trace would be nonnegative when evaluated at \(v=1\). More generally the projector \(e_-\) onto this summand and \(\tau\) cannot both have nonnegative Laurent matrices in any single basis: \(\operatorname{Tr}(e_-\tau)=-2\). The positive commutant matrix-unit structure contains \(e_-\), so adjoining this particular named operator to its positive cone is impossible. This does not contradict a source based-module definition which permits the signed extension.

### Complementary generators

Set \(Q_i=DI-P_i\). Replacing the second vector of every rank-two right block by its negative makes both \(Q_i\) positive Laurent; it preserves bar invariance and the ordinary left positive matrices. Thus the corresponding positive assertion is also available in the complementary convention, using a different basis.

There is no basis with **both** pairs \(P_i,Q_i\) coefficientwise nonnegative Laurent: their off-diagonal entries are negatives of each other, so positivity would force every off-diagonal entry of every \(P_i\) to vanish. Then \(P_1,P_2\) would commute. They do not commute in (P9), for instance their \((1,2)\) commutator entry is \(Da\ne0\). This is limited to simultaneous positivity of these complementary operators, not a denial of either convention separately.

## 9. A strict center-basis obstruction

The parent suggested the following additional sharp test, whose proof is independent of the matrix-functor argument. Work over \(R=\mathbf Q[v,v^{-1}]_{(v-1)}\), and let \(C\) be the actual rank-two center, generically split and reduced with dual-number special fiber. There is no \(R\)-basis \(\{1,b\}\) with

\[
b^2=a(v)+c(v)b,\qquad a,c\in\mathbf N[v,v^{-1}].
\tag{P14}
\]

Indeed the characteristic polynomial of multiplication by \(b\) is \(T^2-cT-a\). In the dual-number fiber its discriminant is zero, so \(c(1)^2+4a(1)=0\). Nonnegative coefficients imply \(a(1),c(1)\ge0\), hence both vanish. A nonnegative Laurent polynomial vanishing at 1 is zero, so \(a=c=0\) identically. Then the generic algebra would be \(K[b]/b^2\), contradicting the actual split reduced generic fiber. This proves precisely the stated unit-containing rank-two basis obstruction.

The factor in F25, \((v-v^{-1})^2(D-1)\), has negative expanded Laurent coefficients but is of the factored kind considered in VIII. Consequently (P14) does not refute VIII's weaker signed-factor positivity convention or rule out every basis of the full algebra.

## 10. What remains outside this construction

The new basis is not a basis of the original global tensor-monomial \(\Lambda\)-lattice: its determinant is not a unit there. It also does not lie in the ordinary upper crystal lattice at infinity. For example \(b_1\otimes b_0\) has a \(v^2\) coefficient in the tensor-monomial basis and hence a pole at infinity. These are explicit failures of those *ordinary* lattice identifications. IV itself warns that its desired nonstandard integral form and local lattice differ from those ordinary ones, so these failures do not by themselves disprove an identification with some nonstandard lattice; that identification has not been established.

Bar invariance and positive action are insufficient to select the prescribed globalization. Multiplying every vector of any one complete isotypic sector by the bar-invariant unit \(h^r\), \(r\in\mathbf Z\), preserves all the displayed operator matrices, the commutant matrix units and the bar over \(S\), but changes its global lattice and behavior at infinity. Thus infinitely many bases meet these proved local properties. VIII's prescribed lattices, duality, crystal reduction and minimum-degree conditions are substantive extra choices.

Finally the matrix units in (P2) give a positive algebra basis of this fixed-degree commutant; they do not specify the dual FRT coordinate multiplication across degrees, VIII's opposite canonical basis, its structure constants, or a pure realization with the required path-output sign. The constructive conclusion is nonetheless stronger than mere trace positivity: the actual regular module, ordinary left/right operators, actual bar, and full regular commutant have a simultaneous explicit positive action in this rank-three case.

## 11. Verification record

- Every proof above is included, including the all-word rank-one calculation and the exact category/summand boundary.
- The ordinary eight-by-eight \(E,F\) matrices were independently derived from source equation (29) and conjugated exactly over \(\mathbf Q(v)\), confirming every entry in (P6).
- The matrix conversion (P7) was checked by exact multiplication against the source's explicit canonical basis matrix.
- The regular right-action matrices and determinants used from F21 were already independently checked; their factorwise use here proves the full determinant without a numerical 64-by-64 sample.
- The source's existing Example 19.2 is explicitly acknowledged. No claim of a new solution to the rank-three canonical-basis problem or of equivalence with that exact source basis is made.
- A fresh independent full review is requested before integration. Suggested check event: `F43-POSITIVE-BIMODULE-AUTHOR-PROOF`.
