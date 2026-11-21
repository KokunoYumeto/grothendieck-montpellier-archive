# DEG_L / bounded core index in a fixed CM isogeny class

Run DEG_L_20261121; author /root; GPT-6 Astra Pro; effort not exposed. B24 was written and whole-proof checked by root and independently by /root/rallis_t6 on 2026-11-21. The statement concerns polarization homomorphisms, or numerical polarization classes, rather than individual line bundles differing by a member of Picard degree zero.

## B24. Bounded core index gives finitely many polarized CM points

Fix a CM field $E$ of degree $2g$, a CM type $\Phi$, and a positive integer $V$. Consider complex polarized abelian varieties $(A,\iota,\lambda)$ with rank-one $E$-homology and this fixed CM type, where $\iota:E\to\operatorname{End}^0(A)$ is the given rational action, the Rosati involution of $\lambda$ restricts to complex conjugation on $E$, and $\deg\lambda=V^2$. Write
\[
 A=\mathbf C^g/\Phi(\Lambda),\qquad
 \Lambda^- =\{x\in\Lambda:\mathcal O_E x\subseteq\Lambda\},
 \qquad J(A,\iota)=[\Lambda:\Lambda^-].
 \tag{B24.1}
\]
These quantities are unchanged by replacing $\Lambda$ with an $E^\times$-multiple. Let $h_E$ be the ideal class number of $E$, and let $a_r(m)$ be the finite number of index-$m$ subgroups of $\mathbf Z^r$.

For every positive integer $B$, the number of $E$-linear polarized isomorphism classes with $J\le B$ is at most
\[
 h_E\left(\sum_{m=1}^B a_{2g}(m)\right)
       a_{2g}(V^2)\,2^g.
 \tag{B24.2}
\]
The same finiteness holds after imposing any fixed finite level structure. In particular every infinite set of distinct polarized CM points with these fixed field, type, and polarization-volume data has unbounded $J$. A bounded-$J$ subset cannot be dense in a positive-dimensional polarized moduli space.

Primitivity and simplicity are not needed for this finiteness statement. The later lower bounds B20--B22 still retain their own simplicity hypotheses.

### Proof

The full $\mathbf Z$-lattice $\Lambda^-$ is an invertible fractional $\mathcal O_E$-ideal: it is a nonzero full lattice stable under $\mathcal O_E$, and $\mathcal O_E$ is Dedekind. Nonzeroness follows, for example, by choosing a nonzero integer $c$ with $c\mathcal O_E\Lambda\subseteq\Lambda$. Its $E^\times$-homothety class is therefore one of $h_E$ possibilities. Fix one representative $I$ of each such ideal class and multiply $\Lambda$ by an element of $E^\times$ so that its core becomes $I$. Multiplication is complex linear for the fixed CM type, commutes with $E$, and transports the polarization without changing its degree.

For a fixed representative $I$, every remaining lattice satisfies
\[
 I\subseteq\Lambda\subset E,\qquad [\Lambda:I]=m\le B.
\]
There are exactly $a_{2g}(m)$ overlattices of a free rank-$2g$ lattice of index $m$. One way to see the equality with the subgroup count is to pass to dual lattices: an overlattice determines and is determined by an index-$m$ sublattice of $I^\vee$. For finiteness alone, $m\Lambda\subseteq I$ embeds $\Lambda/I$ into the finite group $m^{-1}I/I$. We may count every overlattice, even though some have core strictly larger than $I$; this only increases the upper bound. Thus at most $h_E\sum_{m\le B}a_{2g}(m)$ unpolarized $E$-linear isomorphism classes occur.

Fix one such $A$. A polarization homomorphism $\lambda:A\to A^\vee$ of degree $V^2$ is injective on integral first homology, and its image is an index-$V^2$ sublattice of $H_1(A^\vee,\mathbf Z)$. There are at most $a_{2g}(V^2)$ possibilities for this image. Discard those images not realized by a compatible polarization, and for each remaining image choose one compatible polarization $\lambda_0$ with that image.

Let $\lambda$ be any other compatible polarization with the same image and put
\[
 u=\lambda_0^{-1}\lambda\in\operatorname{End}^0(A).
\]
Compatibility means $\lambda e=\overline e^{\vee}\lambda$ for every $e\in E$, and the same identity holds for $\lambda_0$. Consequently $u$ commutes with $E$. Since $H_1(A,\mathbf Q)$ has rank one over $E$, its $E$-linear endomorphism algebra is $E$ itself; hence $u\in E$. Symmetry of the two polarizations makes $u$ self-adjoint for the Rosati involution of $\lambda_0$, so in fact $u\in F:=E^+$. Their positivity makes $u$ totally positive. Concretely, the positive Hermitian forms on the $\Phi$-coordinates have positive ratios equal to the real embeddings of $u$.

Equality of the two image lattices gives $u\Lambda=\Lambda$. If
\[
 R_F=\{b\in F:b\Lambda\subseteq\Lambda\},
\]
then $R_F$ is an order in $F$ and $u\in R_F^{\times,+}$. For every $b\in R_F^\times$, multiplication by $b$ is an actual $E$-linear automorphism of $A$. Its pullback sends the polarization $\lambda_0u$ to $\lambda_0ub^2$, because $b$ is Rosati self-adjoint and commutes with $u$. Thus square classes of $R_F^\times$ suffice to count polarized isomorphism classes over this one image lattice.

The group $R_F^\times$ is a subgroup of $\mathcal O_F^\times$. Dirichlet's unit theorem implies that it is a finitely generated abelian group of rank at most $g-1$, and its torsion is contained in $\{1,-1\}$. Therefore
\[
 [R_F^\times:(R_F^\times)^2]\le2^g.
\]
The totally positive subgroup has no more cosets modulo these squares. This proves the polarization count and hence (B24.2). A fixed finite level structure has only finitely many choices on each polarized variety. The final assertions follow immediately from finiteness. QED.

### Consequence for the degree and division gates

For the simple reference and fixed generic Weil data in B21--B22, a bounded-degree source family yields reduced transported witnesses of degree at least $c\sqrt J$, with an explicit positive $c$ after B22. B24 proves that the alternative of a bounded core index does not describe an infinite polarized CM Hecke set with these fixed data. Thus the fixed-reference, bounded-source construction cannot supply a uniform effective witness bound on such an infinite set, in particular on a dense positive-dimensional Hecke orbit. This is still a restriction on the construction, not a lower bound for all cycles on the targets. The proof does not assert any Hecke-orbit density theorem and does not require one for this implication.

The field and CM type stay fixed. Allowing them to vary is outside (B24.2). Picard-degree-zero changes of a line bundle do not change the polarization homomorphism or any degree used here; they must not be counted as new polarized moduli points.

### Exact background and framework placement

- Milne, *Algebraic Number Theory*, version 3.08, Theorems 4.3--4.4, printed pp.70--71, gives ideal class finiteness; Theorem 5.1, printed p.85, gives finite generation and rank of units. Original author source: <https://www.jmilne.org/math/CourseNotes/ANT.pdf>. The exact statements and the short proof of Theorem 4.4 were read. These classical results are imported, not reproved.
- The CM lattice model and the Rosati metric convention are those already checked in B19.1 and T6.17. The image-lattice and square-class counting argument above is supplied in full for the form needed here; it does not invoke an unlocated finiteness theorem for polarizations.
- Grothendieck framework: polarized abelian schemes and the intersection form, cote 44, PDF scan 2 / archive footer 1, Theorem 4; birigidified line bundles and polarization homomorphisms in SGA7 I, Exposé VII, Example 2.9.5 p.175 and Remark 2.9.6 p.176. These are framework placements, not claims that B24 or a CM counting theorem is stated on those pages.

### Check status

Author and independent reviewer /root/rallis_t6 have read the complete proof, including the rank-one centralizer argument, same-image automorphism, real-unit squares, and the distinction between a line bundle and a polarization homomorphism. The reviewer independently reopened the exact Milne class-number and unit statements. Both checks passed with the explicit Rosati compatibility retained, including in imprimitive types. No numerical computation or proof-assistant verification is claimed.
