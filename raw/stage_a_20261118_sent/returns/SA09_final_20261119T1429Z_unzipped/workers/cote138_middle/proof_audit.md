# Cote 138, scans 46–89: independent mathematical checks

These are this run's proofs and conditional reconstructions. They are not transcribed proofs attributed to Grothendieck. All source locators use one-based lines in `MPL_138_046-089_transcription.tex`. Exact symbolic and finite outputs are in `outputs/computations.json`, produced by `programs/compute_middle.py`. The bounded enumerations corroborate the general arguments below; they do not replace them.

## 1. Dihedral quotient and its quadratic base change

Set

\[
 f_n(x)=\frac12-\frac14(x^n+x^{-n}),\qquad n\geq1.
\]

Its numerator and denominator have no common factor in characteristic zero, so its degree is \(2n\). Rotations \(x\mapsto\zeta x\), \(\zeta^n=1\), and inversion preserve it. They give \(2n\) distinct automorphisms, hence all deck transformations, since the extension degree is \(2n\). The equation for a fibre is quadratic in \(w=x^n\). Direct differentiation gives

\[
 f_n'(x)=-\frac{n(x^{2n}-1)}{4x^{n+1}}.
\]

The points \(x^n=1\) lie over 0, and those with \(x^n=-1\) over 1; each has ramification index 2. The two poles 0 and infinity have index \(n\). Thus the ramification sum is \(2n+2(n-1)=4n-2=2\deg(f_n)-2\), with no missing critical point. For \(n=1\), infinity is a value with two unramified preimages, so the branch set has two elements, not three. In characteristic dividing \(2n\), this calculation cannot be used unchanged.

For the quadratic base change \(u=\tfrac12-\tfrac14(z+z^{-1})\), the generic fibre product is

\[
 w^2-(z+z^{-1})w+1=(w-z)(w-z^{-1}).
\]

Its normalization has two rational components, parameterized by \(x\), with \(z=x^n\) or \(z=x^{-n}\). Each component has genus zero and maps with degree \(n\) to the \(z\)-line. It would be incorrect to call this fibre product connected, or to infer the genus of an unspecified wild base change from it. This verifies the concrete model behind the cancelled “facile” at scan 68.

## 2. The two conics, the cubic, and all odd powers

Write \(C:x^2+y^2+z^2=0\). For the displayed cubic

\[
 A=-x(x^2-3y^2),\quad B=y(y^2-3x^2),\quad Z=z^3,
\]

the machine-expanded sum is

\[
 A^2+B^2+Z^2=x^6+3x^4y^2+3x^2y^4+y^6+z^6.
\]

It is divisible by \(x^2+y^2+z^2\). If \(z\ne0\), the last coordinate is nonzero. If \(z=0\) on the conic, then \(y^2=-x^2\), with \(x\ne0\), and \(A=-4x^3\ne0\). Hence there is no projective basepoint. A polynomial identity on the conic is the required assertion; it is not an ambient identity equal to zero.

Over \(K=\mathbb Q(i)\), set \(u=(y-ix)/z\). The nontrivial field automorphism satisfies

\[
 \sigma(u)=\frac{y+ix}{z}=-u^{-1}.
\]

Compatibility of \(u\mapsto u^m\) with this descent datum is the equality \((-u^{-1})^m=-(u^m)^{-1}\), which holds exactly when \(m\) is odd. This is an assertion about this power-map family, not a classification of all conic endomorphisms.

For odd \(m>0\), write \((y-ix)^m=B_m-iA_m\), with integral homogeneous polynomials \(A_m,B_m\). Their norm is \((x^2+y^2)^m\), and therefore

\[
 A_m^2+B_m^2+z^{2m}=0\quad\text{on }C.
\]

At a point with \(z=0\), one of \(y-ix\), \(y+ix\) is nonzero, so \(A_m,B_m\) are not both zero. The resulting projective morphism has degree \(m\), since it becomes the power map on \(\mathbb P^1_K\). The script prints all polynomials for \(1\leq m\leq9\) and verifies their remainders; the norm/descent argument proves the general statement.

By contrast, \((1-t^2,2t,1+t^2)\) satisfies the **split** equation \(x^2+y^2-z^2=0\). Its positive-form value is \(2(1+t^2)^2\). Over \(\mathbb Q\), the positive conic has no real point, whereas the split conic does; they are not isomorphic over \(\mathbb Q\). Replacing \(z\) by \(iz\) works over \(K\). This is a reason to inspect the sign and the intended model on the scans, not permission to alter either.

## 3. Critical-value elimination and the candidate degree-six quotient

For \(f=p/q\) in characteristic zero with coprime \(p,q\), at a finite point \(a\) where \(q(a)\ne0\),

\[
 f'(a)=\frac{p'(a)q(a)-p(a)q'(a)}{q(a)^2}.
\]

If \(\lambda=f(a)\), criticality is equivalent to \(p(a)-\lambda q(a)=p'(a)-\lambda q'(a)=0\). Writing \(\lambda=p'/q'\) additionally assumes \(q'(a)\ne0\). The example \(p=x^2,q=1,a=0\) is a genuine critical point with \(q'=0\); it checks all the coprimality, characteristic and nonpole hypotheses while refuting unrestricted division. Local parameters at poles and infinity are needed for a global branch calculation (Stacks Project, §53.12, `M-Stacks0C1B`).

The earlier run proposes, for the unlabelled diagram at scan 78,

\[
 R(t)=\frac{27t^2(t-1)^2}{4(t^2-t+1)^3}.
\]

This formula is **not written on that leaf**. It is independently checked here as a candidate. Exact factorization gives

\[
 R-1=-\frac{(t-2)^2(t+1)^2(2t-1)^2}{4(t^2-t+1)^3},
\]

and

\[
 R'=-\frac{27t(t-2)(t-1)(t+1)(2t-1)}{4(t^2-t+1)^4}.
\]

The fibres over \(0,1,\infty\) have index patterns \((2,2,2),(2,2,2),(3,3)\), with ramification sum \(3+3+4=10\). Invariance under \(t\mapsto1-t\) and \(t\mapsto1/t\) is checked symbolically. Thus \(R\) is the quotient by the rational \(S_3\) acting on the three marked points. The agreement with the labels in the drawing supports, but cannot prove, authorial intention.

## 4. Groupoid coordinates and two scope failures

Choose one root \(a_i\) in each component of a groupoid \(C\) and arrows \(u_x:a_i\to x\), with \(u_{a_i}=1\). Every arrow \(g:x\to y\) has the unique expression

\[
 g=u_y(u_y^{-1}gu_x)u_x^{-1},
\]

where the middle factor belongs to \(\operatorname{Aut}_C(a_i)\). A functor with object map \(f_0\) is therefore uniquely determined by its homomorphisms \(\varphi_i\) on these groups and its invertible rays \(t_x=F(u_x)\). Conversely

\[
 F(g)=t_y\varphi_i(u_y^{-1}gu_x)t_x^{-1}
\]

preserves identities and composition, by cancellation of \(t_y^{-1}t_y\) and functoriality of \(\varphi_i\). This proves the coordinate proposition for an arbitrary target category: the specified rays must be invertible, because their preimages are. The root/ray description is also explicit in the GAP Groupoids manual, §§5.1 and 6.1 (`M-GAPGroupoids2026`).

For a groupoid target, isomorphisms on root groups together with a bijection on components yield full faithfulness and essential surjectivity. For a category target, root **unit groups** do not account for noninvertible arrows. The finite monoid \(M=\{0,1\}\), with 1 the identity and 0 absorbing, is a category with one object and trivial unit group. The functor from the trivial one-object groupoid passes the proposed object/component/vertex-group tests but misses 0. The monoid table and units are in the computation output. This refutes the abbreviated scan-61 corollary in the earlier arbitrary-target scope, while Stacks Lemma 4.2.19 supplies the general correct criterion (`M-Stacks02C3`).

For a connected groupoid, identify all Hom-sets with a root group using the chosen rays. Any permutation of objects then lifts, and root automorphisms and independent nonroot ray changes give the displayed object-fixing exact sequence and a choice-dependent splitting. For a disconnected groupoid with one object carrying group 1 and another carrying group \(C_2\), no automorphism exchanges those objects: an automorphism would induce an impossible group isomorphism \(1\cong C_2\). Hence connectedness, or appropriate component and isotropy conditions, is necessary. Its occurrence only in the cancelled setup at scan 60 is consequential.

## 5. Tame signatures and the cancelled wild paragraph

For a degree-\(N\) tame Galois cover \(\mathbb P^1\to Y\), Riemann–Hurwitz reads

\[
 -2=N\left(2g(Y)-2+\sum_i(1-1/d_i)\right).
\]

Nonnegativity of the ramification terms forces \(g(Y)=0\). Each inertia index divides \(N\) and is at most \(N\). With two branch points, \(2/N=1/d_1+1/d_2\), and each summand is at least \(1/N\), so both indices are \(N\). A nontrivial one-point tame cover is excluded by the same formula, since \(2/N=1+1/d\) and \(d\leq N\) force \(N=1\).

For three ordered indices \(2\leq a\leq b\leq c\), the condition is \(1/a+1/b+1/c>1\). If \(a\geq3\), the sum is at most 1; therefore \(a=2\). If \(b=2\), all \(c\geq2\) occur. If \(b=3\), then \(c<6\), giving 3, 4, 5. If \(b\geq4\), the sum is at most 1. For four or more branch points, \(\sum(1-1/d_i)\geq2\), contradicting strict positivity. This proves the classification without reliance on the script's cutoff 30. It matches the tame classification in Faber, §5 (`M-Faber2011`), and the differential formula in the Stacks Project.

In characteristic \(p\), a finite \(p\)-subgroup of \(\operatorname{PGL}_2\) over an algebraically closed field is conjugate to translations by a finite \(\mathbb F_p\)-vector space (Faber, Lemma 4.3). This is the exact result used, not a blanket Borel reduction for every finite group. A finite **group** quotient of function fields is separable. For example, translations by \(\mathbb F_p\) fix \(t=x^p-x\); the polynomial \(X^p-X-t\) has derivative \(-1\), and the extension is separable of degree \(p\). Thus “inséparable” cannot describe this group quotient literally. The whole paragraph is cancelled, and the uncertain word's scope must remain a scan question.

## 6. Orientation, ends, and the marked homotopy statement

For a finite-type surface obtained by deleting finitely many points from a compact surface, punctured-disc neighbourhood filters distinguish the finitely many ends. A homeomorphism carries such filters to such filters and extends uniquely over the missing points. Applying the same construction to its inverse proves that the extension is a homeomorphism. This proves a statement about homeomorphism groupoids, not about arbitrary continuous maps.

For a closed orientable genus-\(g\) surface, \(H_1\cong\mathbb Z^{2g}\). Consequently

\[
 \operatorname{rank}(\Lambda^2H_1)^\vee=\binom{2g}{2}=g(2g-1).
\]

The orientation line has rank one. For \(g\geq2\), it cannot be isomorphic to the entire exterior-square dual. The proper datum is the primitive symplectic intersection form with values in the orientation line, or equivalently the cup product into \(H^2\). An isomorphism in genus one does not justify the statement in general. The proposed correction is mathematical, not diplomatic.

The mapping-class comparison uses the precise peripheral and orientation restrictions of the Dehn–Nielsen–Baer theorem (Farb & Margalit, 2012, Theorems 8.1 and 8.8; `M-FarbMargalit2012`). Hamstrom's Theorem 1.5.2 (1974; `M-Hamstrom1974`) records the identity-component homotopy groups for compact surfaces, including the torus exception; its compact-manifold conventions do not by themselves establish the open-annulus case.

The finite-marked homotopy-group assertion has an exact pre-1978 source. Quintas (1965, p. 721, Theorem (c), (h); `M-Quintas1965`) gives vanishing for punctured tori and for spheres with at least three punctures, in the compact-open topology. His equation (2.2), p. 722, identifies the positive-degree homotopy groups of the point-fixing identity component with those of the surface with one further puncture; p. 723 explicitly treats the torus. Thus a fixed point removes the open-annulus and torus exceptions at the level asserted here. Iteration handles further finite markings. The cited original McCarty theorem was not independently retrieved; the exact statement and its use were read in Quintas. This concerns the identity component, not the entire marked homeomorphism group.

For a stronger modern statement in a specified topology, Yagasaki (2000, Theorem 1.1, PDF p. 1; `M-Yagasaki2000`) proves contractibility for the identity component fixing a compact subpolyhedron of a connected noncompact separable PL surface except for his listed unmarked or plane exceptions. An open annulus with a nonempty finite fixed set is nonexceptional. His Lemma 2.1(i), PDF p. 2, also covers the marked compact torus. These results support the stated finite-type **homotopy-group/∞-groupoid interpretation** of the manuscript's “vérifier”; they do not establish contractibility in every topology or for arbitrary marking sets.

For a negatively curved surface, fixing a point can create point-pushing components even when the unmarked identity component is contractible. Thus one must discuss the identity component and the mapping-class group separately. Nothing here proves that the centralizer of a specified operator action is contractible. Neither an arbitrary infinite discrete marked set nor the undefined rigidification space of later scan 126 is covered by this argument.

## 7. Free profinite centre, multiplier, and arithmetic outer action

For every group \(G\), the kernel of \(G\to\operatorname{Aut}(G)\) by conjugation is \(Z(G)\). At free profinite rank one, \(G=\widehat{\mathbb Z}\), and the inner-action map is zero. At rank at least two, the centre is trivial. The rank-two proof opened in Belyi, §1, Lemma 1 and its corollary (`M-Belyi1980`), uses projectivity of the free profinite group to exclude a nonprocyclic closed abelian subgroup. The same lifting argument works for any finite free rank. If an element centralizes a primitive free generator \(x\), its closed subgroup with \(x\) is procyclic. The coordinate map to \(\widehat{\mathbb Z}\) taking \(x\) to 1 implies that \(x\) topologically generates that procyclic subgroup. Thus the centralizer is \(\overline{\langle x\rangle}\). Intersections for two independent free generators are trivial by abelianization. This supplies the required all-finite-rank extension, rather than citing a rank-two statement as though it already had that quantifier.

For \(X=\mathbb P^1_{\mathbb Q}\) minus \(\nu+1\) distinct rational points, SGA 1, IX, Theorem 6.1 (`M-SGA1`) provides the arithmetic exact sequence. Its quotient acts on the geometric group only up to inner automorphisms without a basepoint choice. At a puncture a local cover \(v^n=t\) has inertia \(v\mapsto\zeta_n v\), and coefficient conjugation transforms this to \(v\mapsto\zeta_n^{\chi(\sigma)}v\). Hence the multiplier is the cyclotomic character, uniformly at the rational punctures. That character is onto \(\widehat{\mathbb Z}^{\times}\): the compatible finite cyclotomic automorphisms form \(\operatorname{Gal}(\mathbb Q^{\mathrm{cyc}}/\mathbb Q)\), and automorphisms extend to the algebraic closure. Compactness makes the inverse-limit surjectivity precise.

Topological orientation-preserving permutations of the punctures realize \((s,1)\), and the rational arithmetic action realizes \((1,u)\) for each unit \(u\). Combining them proves surjectivity onto the product \(S_{\nu+1}\times\widehat{\mathbb Z}^{\times}\). It does not prove that the arithmetic subgroup equals the full automorphism group. In rank two, Belyi explicitly checks the common multiplier; Bortnovskyi et al. (2024/2026), Remark 1.3 (`M-BDHPE2026`), independently emphasizes this arithmetic route to multiplier surjectivity.

For \(\mu_5\), exponentiation by 2 has cycles \((1)(\zeta,\zeta^2,\zeta^4,\zeta^3)\). Every nonidentity cyclic translation on the five roots is a five-cycle. This is a complete finite witness that the cyclic target \(\mu_n\) cannot represent the cyclotomic automorphism action in general. A missing \(\operatorname{Aut}\) or unit marker is plausible, not decided.

For rational Möbius maps, arithmetic transport commutes with the geometric outer action. In particular \(1-t\) and \(1/t\) generate an \(S_3\) commuting with the arithmetic action on the triply punctured line. Guillot's exact comparison (2014, §5.6, Lemma 5.19 and Proposition 5.20; `M-Guillot2014`) is with the gentle \(\widehat{GT}_0\) centralizer formulation. Adding a pentagon is extra structure. The 2026 BGT reconstructions explicitly add their own compatibility assumptions (Collas, 2026, Definition 4.3 and Theorem 4.5; `M-Collas2026`). None of these results licenses an unrestricted identification of every peripheral outer group with \(G_{\mathbb Q}\).

## 8. Conditional reversal calculation

Let \(a=\lambda_0\), \(P_j=\lambda_1\cdots\lambda_j\), and \(P_\nu=a^{-1}\). The lower-index-1 version of the proposed reversal has

\[
 t(\lambda_i)=P_{\nu-i}\lambda_{\nu-i+1}P_{\nu-i}^{-1}\quad(1\leq i\leq\nu),\qquad t(a)=a.
\]

Telescoping gives

\[
 t(P_k)=P_\nu P_{\nu-k}^{-1}=a^{-1}P_{\nu-k}^{-1}.
\]

For \(k=\nu\), this is \(a^{-1}\), so the product relator is preserved. Applying the same formula twice yields

\[
 t^2(P_k)=a^{-1}P_k a,
\]

and hence \(t^2=\operatorname{Inn}(a^{-1})\). Because its square is an automorphism, \(t\) is itself an automorphism. For \(\nu\geq2\), its permutation on the abelianized free generators is nontrivial, so its outer class has exactly order two; this displayed based lift is not a strict involution. For \(\nu=1\), the displayed reversal is the identity. The lower-index-0 reading instead leaves the reduced relator \(a\lambda_1^{-1}a^{-1}\lambda_1\), which is nontrivial for \(\nu\geq2\). The script reduces these words independently for ranks 2 through 9; the displayed algebra proves the stated all-rank assertions.

This neither decides the ink nor rules out a different strict involutive lift. For example, in rank two a different generator convention can exhibit a genuine swap involution. The correct conclusion is about this displayed lift only.

## 9. Scope of the computations

The script uses exact SymPy polynomial arithmetic, integer/fraction arithmetic, permutation cycles, and a free-group stack reduction with inverses represented by signed integers. It has no floating-point root tests and no web access. Each finite test range is printed. Source judgments, literature classes and merger decisions are authored in separate files; no keyword or heading classifier produces them. A failed reader invocation lacking `--output` occurred before the corrected invocation; it did not alter a source or data record and is documented in the session operations log.
