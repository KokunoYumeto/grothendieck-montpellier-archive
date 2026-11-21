# F49 candidate: an intrinsic projector obstruction to global commutant integrality

Author: /root/grothendieck_dictionary. Date: 2026-11-21 UTC.

## 1. Exact claim and scope

There is an actual projector in the full F43 commutant, and hence an actual direct-summand projector in the framed coherent realization F46, which does not preserve the original unlocalized tensor lattice. This is an intrinsic operator statement: changing the basis of that same lattice cannot repair it. It strengthens the determinant diagnostic in F43, which by itself only tests its displayed basis.

The projector is excluded from VIII's specified dual global form by the definition of that form. No conjecture about the local crystal lattice is needed for this exclusion. The projector is nevertheless bar compatible and is regular at both boundary valuations in the explicitly stated tensor-coordinate lattices. Global integrality and those two boundary tests are different conditions.

This does not refute VIII's canonical-basis conjectures. Those conjectures do not say that every matrix unit of every localized commutant belongs to the designated global form. Nor does it refute the already constructed based rank-three example in revised IV. In particular, IV explicitly allows a different integral form. No impossibility is claimed for an alternate basis with only the named nonstandard generators, for a changed lattice, or for a smaller integral commutant.

## 2. Rings and actual tensor module

Write
\[
 R=\mathbf Q[v,v^{-1}],\quad F=\mathbf Q(v),\quad
 \delta=v+v^{-1},\quad D=\delta^2,\quad
 h=D-1=v^2+1+v^{-2}.
 \tag{L1}
\]
Let \(V_R=R^2\), \(W_R=R^2\), and
\[
 M_R=(V_R\otimes_R W_R)^{\otimes3}
     \cong V_R^{\otimes3}\otimes_R W_R^{\otimes3}.
 \tag{L2}
\]
This is the original tensor-monomial lattice. Everything below also proves the corresponding assertion over \(\mathbf Z[v,v^{-1}]\), because failure over \(R\) is already sufficient. Adjoining the constant \(i\) for F46 changes none of the arguments.

Use right-row matrices: row \(j\) gives the image of the \(j\)-th basis vector. On the ordinary three-dimensional weight space of \(V_F^{\otimes3}\) with ordered monomials
\[
 (m_{112},m_{121},m_{211}),
\]
the actual upper canonical basis displayed in IV Figure 1 is
\[
 c_{112}=m_{112},\qquad
 c_{121}=m_{121}-v^{-1}m_{112},\qquad
 c_{211}=m_{211}-v^{-1}m_{121}.
 \tag{L3}
\]
This unitriangular change preserves the global \(R\)-lattice.

The F43 ordinary decomposition has the highest-weight-three vector
\[
 b_1=v^2m_{112}+v m_{121}+m_{211},
\]
and its two complementary highest-weight-one multiplicity vectors
\[
 u_1=-(1+v^{-2})m_{112}+v m_{121}+m_{211},\qquad
 u_2=-v^{-1}m_{112}-v^{-2}m_{121}+\delta m_{211}.
 \tag{L4}
\]
Their rows in the canonical coordinates (L3) are
\[
 B_{\mathrm{can}}=
 \begin{pmatrix}
 h&\delta&1\\
 0&\delta&1\\
 0&1&\delta
 \end{pmatrix}.
 \tag{L5}
\]
In particular \(b_1=h c_{112}+u_1\).

The corresponding lower weight space has
\(b_2=v^2m_{122}+v m_{212}+m_{221}\), and the same two complementary rows with their order interchanged. Together with \(b_0=m_{111}\) and \(b_3=m_{222}\), these give the actual ordinary decomposition
\[
 V_F^{\otimes3}=(W_3\otimes\epsilon)\oplus(W_1\otimes U).
 \tag{L6}
\]
For completeness, the source coproduct yields
\[
 F b_0=b_1,\quad F b_1=\delta b_2,\quad F b_2=h b_3,\quad F b_3=0,
\]
\[
 E b_0=0,\quad E b_1=h b_0,\quad E b_2=\delta b_1,\quad E b_3=b_2,
\]
and the two \(W_1\) copies have \(Fg_+=g_-\), \(Eg_-=g_+\), with the other two actions zero. The actual ordinary Hecke generators act by \(\delta\) on \(\epsilon\) and on \(U\) by
\[
 c_1=\begin{pmatrix}\delta&0\\1&0\end{pmatrix},
 \qquad c_2=\begin{pmatrix}0&1\\0&\delta\end{pmatrix}.
 \tag{L7}
\]
These coordinate identities are the complete ordinary calculation already proved in F43; they identify the summands as actual invariant subspaces, rather than merely abstract modules with matching dimensions.

## 3. The projector and its unavoidable denominator

Let \(p_V\) be the projector onto \(W_3\otimes\epsilon\) along \(W_1\otimes U\). On the weight space above it is uniquely specified by
\[
 p_V(b_1)=b_1,\qquad p_V(u_1)=p_V(u_2)=0.
 \tag{L8}
\]
In canonical and monomial coordinates its respective matrices are
\[
 [p_V]_{\mathrm{can}}=
 \begin{pmatrix}
 1&\delta/h&1/h\\
 0&0&0\\
 0&0&0
 \end{pmatrix},
 \qquad
 [p_V]_{\mathrm{mon}}=
 \frac1h
 \begin{pmatrix}
 v^2&v&1\\
 v&1&v^{-1}\\
 1&v^{-1}&v^{-2}
 \end{pmatrix}.
 \tag{L9}
\]
Indeed (L5) immediately gives the first matrix. For the second, put \(u=(v,1,v^{-1})\). The numerator is \(u^{\mathsf t}u\) and \(u u^{\mathsf t}=h\); it is an idempotent of rank one, fixes \(b_1=v u\), and kills both vectors in (L4). The lower weight space has the same matrix, and the endpoint weight spaces have projector one.

In particular
\[
 p_V(m_{112})=m_{112}+(\delta/h)c_{121}+(1/h)c_{211}
             =(v^2m_{112}+v m_{121}+m_{211})/h.
 \tag{L10}
\]
The coefficient of \(m_{211}\) is \(1/h\), which is not in \(R\). The Laurent polynomial \(h\) is not a unit: the units of \(R\) are exactly \(a v^j\), \(a\in\mathbf Q^\times\). Consequently
\[
 p_V(V_R^{\otimes3})\not\subseteq V_R^{\otimes3}.
 \tag{L11}
\]
This is also apparent in the canonical coordinates, since (L3) is unimodular over \(R\).

Set
\[
 p=p_V\otimes 1_{W_F^{\otimes3}}\in\operatorname{End}_F(M_F).
 \tag{L12}
\]
It commutes with both actual nonstandard generators
\[
 P_i=c_i^V\otimes c_i^W+
       (c_i^V-\delta)\otimes(c_i^W-\delta),
\]
because \(p_V\) commutes with both \(c_i^V\). It also commutes with all actual ordinary left \(E,F,K^{\pm1}\) operators on both factors, by (L6). Yet the image of
\(m_{112}\otimes m_{111}\) has coefficient \(1/h\) at
\(m_{211}\otimes m_{111}\). Thus \(p\notin\operatorname{End}_R(M_R)\).

If some \(R\)-basis of \(M_R\) made \(p\) an \(R\)-matrix, then \(p\) would preserve \(M_R\), a contradiction. More generally, no basis of this same lattice can make every one of the specified F43 commutant matrix units an \(R\)-matrix: the next section expresses \(p\) as their sum. This argument does not depend on the determinant of any proposed basis.

The failure survives every algebraic coefficient extension with the prescribed integral closure. If \(1/h\) were integral over \(R\), a monic equation, multiplied by a suitable power of \(h\), would give \(1\in hR\), contrary to \(h\) being a nonunit. Hence \(1/h\) is not in the integral closure of \(R\) in any algebraic extension of \(F\). The same argument applies after adjoining \(i\). If the parameter convention first adjoins \(v\) as a square root of the source parameter, integrality over the smaller Laurent ring would imply integrality over \(R\), and the conclusion is unchanged.

## 4. It is an actual F43/F46 projector

Over the localization used in F43, the multiplicity decomposition is
\[
 M=(W_3\otimes W_3\oplus W_1\otimes W_1)\otimes\epsilon_+
 \oplus(W_1\otimes W_1)\otimes\epsilon_-
\]
\[
 \hspace{5mm}\oplus
 (W_3\otimes W_1\oplus W_1\otimes W_3)\otimes N(\delta)
 \oplus(W_1\otimes W_1)\otimes N(D-2).
 \tag{L13}
\]
The multiplicity ranks are \(20,4,16,4\). In this specified ordering \(p\) selects the first 16 multiplicities in the \(\epsilon_+\) block and the first eight multiplicities in the \(N(\delta)\) block, and kills the other multiplicities. It is therefore a sum of diagonal matrix units of the full commutant
\[
 M_{20}\times M_4\times M_{16}\times M_4.
 \tag{L14}
\]
Its F43 matrix has only zero and one entries.

In F46 let the coefficient base be its stated localization \(S\), and retain its framed target
\[
 K=S_{-1}^{20}\oplus S_i^4\oplus L_1^{16}\oplus L_2^4.
\]
The endomorphism
\[
 g=\operatorname{diag}(I_{16},0_4)\oplus0_4
   \oplus\operatorname{diag}(I_8,0_8)\oplus0_4
 \tag{L15}
\]
is a literal direct-summand projector of \(K\), both as a coefficient module and as the corresponding finite-support coherent sheaf on \(\mathbf P^1_S\). It commutes with the coordinate \(T\) and the chosen Frobenius. Under F46's postcomposition isomorphism
\[
 \operatorname{End}_F(K)\xrightarrow{\sim}
 \operatorname{End}_A\operatorname{Hom}_F(H,K),
\]
and the F43 multiplicity framing, it induces exactly \(p\). The branch comparison changes only the two-dimensional right factor, leaving all multiplicity selectors unchanged. Thus the pole is a concrete limitation of descent of this actual coefficient projector, not a claim that the coherent model lacks projectors.

## 5. Actual bar and two boundary regularities

The basis in (L5), the endpoints, and the lower weight analogue are fixed by the actual ordinary tensor-product bar, as verified from IV Figure 1 in F43. Both summands (L6) are bar stable; hence their projector \(p_V\), and therefore \(p\), commutes with that bar. This assertion does not claim that the bar fixes the tensor monomials.

The F46 coefficient bar can also be made compatible with the framed comparison: send \(v\) to \(v^{-1}\), fix \(i,x,T\), and use the displayed coordinate presentations. The coefficients \(D,\delta,h,\Delta,s,\lambda\) are invariant, and the comparison of a right block \(N(a)\), \(a=\delta,D-2\), with the F46 branch block has the invariant matrix
\[
 S_a=\begin{pmatrix}1&0\\-(a/D)^2&a/D\end{pmatrix}.
 \tag{L16}
\]
It is invertible on F46's base. Choose the ordered multiplicity frames of F43; then this supplies the corresponding actual bar on its Hom realization. The projector (L15) is fixed. This is a framed compatible bar, not a unique global basis selection.

Let \(A_0\) and \(A_\infty\) denote rational functions regular at \(v=0\) and at \(v=\infty\), respectively. In the monomial matrix (L9), every nonzero entry is \(v^j/h\) for \(-2\leq j\leq2\). It is regular at both boundaries: since
\[
 v^j/h=v^{j+2}/(v^4+v^2+1),
\]
its order at zero is nonnegative, and its order at infinity is \(2-j\geq0\). The endpoint entries are one. Thus \(p\) preserves each of the two explicitly specified monomial-coordinate lattices \(M_{A_0}\) and \(M_{A_\infty}\). On the displayed ordinary canonical-coordinate weight lattice the entries \(1,\delta/h,1/h\) are likewise regular at both boundaries.

No equality of these explicit lattices with VIII's conjectural dual local crystal lattice is asserted. The point is the precise weaker one: even an actual bar-compatible projector that passes both of these boundary regularity tests can fail the global Laurent form because of poles at finite nonzero zeros of \(h\).

## 6. Direct comparison with VIII's exact global form

Use \(\mathcal S\) for the nonstandard matrix-coordinate algebra to avoid confusion with the coefficient base. VIII defines its global form \(\mathcal S_{\mathbf Q}\) to be the \(K_{\mathbf Q}\)-subring generated by the generic matrix entries \(u^i_j\), where \(K_{\mathbf Q}\) is the integral closure of the Laurent parameter ring. For the degree-three Schur algebra
\(\mathcal A=(\mathcal S_3)^*\), its specified dual global form is
\[
 \mathcal A_{\mathbf Q}
 =\{a:\langle a,\mathcal S_{3,\mathbf Q}\rangle
          \subseteq K_{\mathbf Q}\}.
 \tag{L17}
\]

Here is the needed matrix-integrality assertion with its complete proof. Write the tensor coaction in the original basis \(e_J\) of \(X^{\otimes3}\):
\[
 e_J\longmapsto\sum_I e_I\otimes u_{I,J}.
\]
Each \(u_{I,J}\) is a degree-three product of the generating matrix entries, with the prescribed order, so belongs to \(\mathcal S_{3,\mathbf Q}\). The induced action of \(a\) has matrix entries \(\langle a,u_{I,J}\rangle\). By (L17) every entry is in \(K_{\mathbf Q}\). Therefore
\[
 \eta(\mathcal A_{\mathbf Q})
 \subseteq\operatorname{End}_{K_{\mathbf Q}}
               (X_{K_{\mathbf Q}}^{\otimes3}).
 \tag{L18}
\]
For \(X=V\otimes W\) with the direct-product ordinary quantum group, the chosen upper canonical basis of \(X\) is the four elementary products, so this is the same original tensor lattice after the stated scalar extension.

Generic nonstandard Schur--Weyl duality identifies the full commutant with \(\eta(\mathcal A)\). Thus the actual \(p\) belongs to that generic algebra, but (L10)--(L12) and the nonintegrality of \(1/h\) imply
\[
                         p\notin\eta(\mathcal A_{\mathbf Q}).
 \tag{L19}
\]
The remark immediately after IV Theorem12.1 corrects its tensor-dual convention relative to §§8--10. Transposing that identification preserves the global matrix-entry criterion. The present projector is symmetric in the monomial coordinates (L9), on both weight blocks and the endpoints, so it is itself unchanged by that transpose. The direct coaction proof above is in its stated convention.
This is the exact comparison result. The localized commutant's elementary matrix-unit basis cannot be identified, under the actual action, with a basis of the designated global form, nor can all those matrix units even belong to that form. It does not say that some other basis of the designated form fails to exist.

VIII states the first inclusion (L18) in Proposition 2.4 and makes its additional local-lattice inclusion conditional on Conjecture 2.2. Its printed proof is a placeholder. The argument above proves the particular global inclusion used here directly from the definitions; it does not certify the unfilled proof or the conditional local assertion.

## 7. Source audit and existing construction

The supplied primary IV source was read in full for the relevant sections: Figure 1, §6.2/Theorem 6.4, §19.1/Conjecture 19.1 and its following remarks, and Example 19.2. The original arXiv PDF was freshly reopened and checked:

- IV, cs/0703110v4, 6 June 2013, Figure 1 p.9; Theorem 6.4 p.34; the paragraph after Conjecture 19.1 on p.131; Example 19.2 pp.132--133. URL https://arxiv.org/pdf/cs/0703110. Refs turn933095197view0 and turn995031330view0--2.
- VIII, 0709.0751v2, §2.1 p.5 for balanced triples; §2.2 p.7 for \(K_{\mathbf Q}\), pp.9--10 for the coordinate form and bar; §2.3 p.11 for the dual global form; Proposition 2.4 pp.12--13; Conjecture 2.5 p.13. The PDF has its own printed pagination; the web tool's P-number is zero-based. URL https://arxiv.org/pdf/0709.0751v2. Refs turn507957707view0, turn238738988view0--2, and turn855859398view0--2.

IV Example 19.2 supplies an explicit rank-three based construction satisfying its Conjecture 19.1 requirements. Its preceding discussion explicitly distinguishes the desired integral form and local lattice from the original tensor forms. Thus the present denominator is compatible with that source, not evidence against it. The result here concerns the extra simultaneous retention of the original global tensor lattice and the full specified F43/F46 commutant projectors.

## 8. Grothendieck translation and honest remaining gate

Over \(\operatorname{Spec}R\), the original tensor lattice gives a vector bundle. The rational idempotent \(p\) extends to a regular idempotent over the open set \(h\neq0\), where it splits that bundle. It fails to be an endomorphism of the original bundle over the whole parameter scheme, by its explicit \(1/h\) entry. EGA I, Theorem 1.3.7 p.86, Corollary 1.3.8 p.87, and Theorem 1.4.1 pp.90--92 are the precise affine module/sheaf framework; they do not assert this particular obstruction. The direct-summand/perfect-object language is compatible with SGA6 I, Definition 4.7 pp.121--122 and Example 4.8 p.122. Cote90 scan17 is an audited equivariant-module framework anchor only.

The coherent model can retain the actual bar after a frame is selected, and it has this actual projector. What fails is descent of the entire specified localized projector system to VIII's designated global form under the actual tensor comparison. One may change the integral form, restrict the operator algebra, or establish a different global-basis comparison. Purity of the separate chosen Weil coefficients supplies none of these changes automatically.

## 9. Check-event scope

The complete new operator, denominator, algebraic-extension, boundary-regularity, and dual-global-form arguments are proved above. Dependencies are the already checked actual F43 decomposition and F46 framed End/Hom identification; their use is explicit. The source's already known Example 19.2 is not reproved or claimed new. Independent whole-proof review and a generated-fragment match remain pending.
