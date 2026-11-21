# Independent audit of the strengthened sign argument

**Date:** 2026-11-21. **Checker:** `/root/q03_openness`, GPT-6 Astra Pro; effort not exposed. **Outcome: PASS**, with the hypotheses and scope stated below. This is a complete mathematical reconstruction and whole-proof reading, not a formal verification. No new claim of priority is made.

I read the complete statements and proofs SG-08, SG-09, and SG-10 in `agent_sign_strengthening.md`. I independently derived the Gysin degrees and twists, the effective remainder, the finite-fibre reduction, every Fourier exponent, the two limiting operations, and the affine-to-projective step. I also checked the extension to all compact-support degrees and general constructible coefficients. The useful geometric input is generic weak Lefschetz, including its control of the open boundary; smoothness by itself is insufficient.

The main argument can be written entirely for lisse sheaves on smooth affine schemes. This avoids making generic perverse restriction an additional unexplained input. The perverse formulation is valid too, but is not necessary for the coefficient theorem obtained by stratification.

## QG-01: the precise generic geometric input

Let $V$ be a smooth affine scheme of pure dimension $D>0$ over an algebraic closure of a finite field, let $\mathcal L$ be lisse, and let $z:V\hookrightarrow\mathbf A^s$ be a closed immersion. Fix an arbitrary regular function $f$ on $V$. For a variable affine linear function $A z+c$, put

\[
Y_{A,c}=\{f+A z+c=0\}\subset V.
\]

There is a dense open subset of the coefficient space on which $Y$ is smooth of dimension $D-1$ and the maps

\[
H^a(V,\mathcal L^\vee)\longrightarrow H^a(Y,\mathcal L^\vee|_Y)
\]

are isomorphisms for $a<D-1$ and injective for $a=D-1$. Empty components, if any, cause no problem; all nonempty components have the stated dimension. The weak Lefschetz assertion is Katz, *Affine Cohomological Transforms, Perversity, and Monodromy*, Corollary 3.4.1, pp. 180–181, with the fixed function $f$ and quasi-finite map $z$. For the smoothness assertion, use the graph closed immersion

\[
V\hookrightarrow\mathbf A^{s+1},\qquad v\mapsto(z(v),f(v)).
\]

Ordinary smooth Bertini applies to generic hyperplanes. The chart in the dual projective space on which the coefficient of the last coordinate is nonzero is a dense open, and normalization of that coefficient to $1$ gives exactly the family displayed above. Thus its generic member is smooth. This also shows that fixing the nondegenerate mixed terms below does not incorrectly assume that a special slice meets an unrelated good open.

Dualize the restriction maps using Poincaré duality for the smooth schemes $V$ and $Y$. One obtains Frobenius-compatible Gysin maps

\[
H_c^j(Y,\mathcal L|_Y)(-1)\longrightarrow H_c^{j+2}(V,\mathcal L)
\tag{G}
\]

which are surjective for $j=D-1$ and isomorphisms for $j>D-1$. Indeed the dual of restriction in degree $a$ has target degree $2D-a$, source degree (2$D-1$-a), and one residual twist $(-1)$. Thus $a=D-1$ corresponds to $j=D-1$, with an injection becoming a surjection. The direction and endpoint are essential.

### Why this input does not contain a weight theorem

Katz Appendix A.1–A.5, pp. 218–221, gives Deligne's proof of generic weak Lefschetz. I read this proof in full. Its ingredients are the universal hyperplane, generic base change, duality, quasi-finite preservation of the perverse support condition, and Artin's affine cohomological dimension theorem. At the last step it reduces to the vanishing of positive ordinary cohomology of a semiperverse complex on the affine complement of a projective hyperplane. There is no assertion about Frobenius eigenvalue absolute values in that proof.

The exact older locators used there are SGA 4 XVII 5.4.3 for compact-support Künneth, SGA 4½, *Théorèmes de finitude* 4.3 for duality, and 1.9 for generic base change. BBD 4.1.1, pp. 102–103, explicitly reformulates SGA 4 XIV 3.1; its dual is BBD 4.1.2. BBD 4.1.3, p. 103, gives perverse exactness for the two direct images of a quasi-finite affine morphism. These BBD statements were checked visually in the original scan, not inferred from an imprecise secondary citation.

For a perverse complex $P$ and a generic hyperplane section $i:Y\hookrightarrow V$, the additional generic purity identification is

\[
i^!P\simeq i^*P(-1)[-2].
\]

It is a relative purity statement, not Frobenius-weight purity. A full proof is Wan–Zhang, *Hodge and Frobenius colevels of algebraic varieties*, Lemma 3.2, pp. 11–12; their Lemma 3.8 gives exactly the resulting Gysin map, surjective in target degree 1 and an isomorphism in target degrees at least 2. The proof uses universal incidence: both projections to projective space are smooth of relative dimensions differing by one; relative smooth purity gives the universal identity, and generic base change for exceptional pullback specializes it. A finite map is handled by proper base change and the conservative finite direct image; a quasi-finite map is factored into an open immersion followed by a finite map. The cited generic base-change locator there is SGA 4½, *Théorèmes de finitude*, Corollary 2.9. I read these proofs in full. The smooth-lisse proof of $G$, however, only needs Poincaré duality and Katz's restriction statement.

All these statements are geometric. After choosing a good hyperplane over the algebraic closure, all its finitely many coefficients lie in some finite extension. Once such a choice is made, it stays fixed over all subsequent extensions and all maps above commute with geometric Frobenius over that field of definition.

## QG-02: the effective remainder with no middle-concentration assumption

Let $U/\mathbf F_q$ be smooth affine of pure dimension $d\ge1$, and let $\mathcal F$ be lisse. Put $V=H_c^d(U_{\overline{\mathbf F}_q},\mathcal F)$. For an integer $k\ge2$, let $Z=U^k$, $D=kd$, and $\mathcal F_k=\mathcal F^{\boxtimes k}$. Choose a smooth affine hypersurface $Y\subset Z$ satisfying QG-01 for $\mathcal F_k^\vee$. Work over a finite field containing its coefficients; for this calculation rename that field $\mathbf F_q$.

For each $n\ge1$, set $Q=q^n$ and

\[
M_n=\sum_{u\in U(\mathbf F_Q)}\operatorname{Tr}(F_{u,Q},\mathcal F_u),\qquad
N_{k,n}=\sum_{y\in Y(\mathbf F_Q)}\operatorname{Tr}(F_{y,Q},(\mathcal F_k)_y),
\]
\[
R_{k,n}=Q N_{k,n}-M_n^k.
\]

Artin vanishing, applied to the dual lisse sheaf and combined with Poincaré duality, gives $H_c^j(U,\mathcal F)=0$ for $j<d$, and similarly $H_c^j(Y,\mathcal F_k|_Y)=0$ for $j<D-1$. Write

\[
T_b=H_c^{D+b}(Z,\mathcal F_k),\qquad
W_a=H_c^{D-1+a}(Y,\mathcal F_k|_Y),\qquad a,b\ge0.
\]

The trace formula and the convention that geometric Frobenius on $\overline{\mathbf Q}_\ell(-1)$ is $q$ give

\[
(-1)^{D-1}R_{k,n}
=\sum_{a\ge0}(-1)^a\operatorname{Tr}(F^n,W_a(-1))
 +\sum_{b\ge0}(-1)^b\operatorname{Tr}(F^n,T_b).
\tag{1}
\]

For $a\ge1$, $G$ identifies (W_a$-1$) with (T_{a+1}). Their coefficients in $1$ are opposite. The remaining virtual representation is

\[
[W_0(-1)]+[T_0]-[T_1].
\]

The border map $W_0(-1)\twoheadrightarrow T_1$ is surjective. Let $E_k$ be its kernel. Hence

\[
(-1)^{kd-1}R_{k,n}
=\operatorname{Tr}(F^n,V^{\otimes k})+\operatorname{Tr}(F^n,E_k).
\tag{2}
\]

Here $T_0=V^{\otimes k}$ by Künneth: every compact-support factor has degree at least $d$, so total degree $kd$ forces each degree to be $d$. Both summands on the right of (2) are actual finite-dimensional Frobenius modules. Neither compact cohomology of $U$ nor compact cohomology of $Y$ is asserted to be concentrated in a single degree. The higher degrees cancel because of the Gysin isomorphisms, and the first uncancelled excess is an actual kernel.

For the perverse convention, $K=\mathcal F[d]$, the same calculation reads

\[
-R=\operatorname{Tr}(F^n,H_c^0(K)^{\otimes k})
 +\operatorname{Tr}(F^n,\ker(H_c^0(i^*K^{\boxtimes k}[-1])(-1)\to H_c^1(K^{\boxtimes k}))).
\]

The extra minus sign comes from $i^*K^{\boxtimes k}= (i^*K^{\boxtimes k}[-1])[1]$. Translating its trace function back to that of $\mathcal F$ gives exactly the sign in (2).

## QG-03: fixed bilinear edges, arbitrary vertex potentials, and the Fourier estimate

Assume for a fixed field embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ that

\[
|\iota\operatorname{Tr}(F_{u,Q},\mathcal F_u)|\le C Q^{w/2}
\tag{3}
\]

for every extension $\mathbf F_Q/\mathbf F_q$ and every rational point $u$. Fix a finite Noether normalization $\pi:U\to\mathbf A^d$. The normalization exists over the finite base field itself: Stacks Project, Lemma 10.115.4, tag 00OY, is an exact usable statement over an arbitrary field.

Choose $B$ generators of $\mathcal O(U)$ as a module over $\mathbf F_q[x_1,\ldots,x_d]$. Every geometric fibre of $\pi$ has length at most $B$, because its coordinate algebra is generated as a vector space by the specializations of these $B$ elements. In particular every rational fibre contains at most $B$ rational points. This assertion does not require $\pi$ to be étale, separable, or flat, and does not replace fibre length by the generic degree.

Choose affine coordinate generators $z_1,\ldots,z_s$ of $U$. For each $k\ge2$, fix invertible $d\times d$ matrices $B_1,\ldots,B_{k-1}$ over the base field; taking all of them to be the identity is enough. Define the fixed function

\[
f(u_1,\ldots,u_k)
=\sum_{i=1}^{k-1}\pi(u_i)^tB_i\pi(u_{i+1}).
\]

Let $g_i$ be a variable linear combination of the $s$ coordinate functions of vertex $i$, and let $c$ vary. By QG-01, coefficients can be chosen over some finite extension $\mathbf F_{q^{e_k}}$ so that

\[
Y:\quad f+\sum_i g_i+c=0
\tag{4}
\]

is smooth and satisfies the required weak Lefschetz statement. The products $U^k\hookrightarrow\mathbf A^{sk}$ are genuine closed immersions. This makes the displayed family a genuine hyperplane family. In the Noether coordinates the chosen vertex potentials need not have bounded degree; the estimate below only uses that each is a function of a single vertex.

Now work over $\mathbf F_Q$ with $Q=(q^{e_k})^n$, while keeping (4) fixed. Choose any nontrivial additive character $\psi:\mathbf F_Q\to\mathbf C^\times$. Character orthogonality gives

\[
Q N_{k,n}=M_n^k+\sum_{h\in\mathbf F_Q^\times}S_{h,n},
\]

where $S_{h,n}$ is the sum over $U(\mathbf F_Q)^k$ of the product of the trace functions multiplied by $\psi(h(f+\sum_i g_i+c))$. After grouping by the finite fibres of $\pi$, put

\[
a_{i,h,n}(x)=\sum_{\substack{u\in U(\mathbf F_Q)\\\pi(u)=x}}
\iota\operatorname{Tr}(F_{u,Q},\mathcal F_u)\,\psi(hg_i(u)).
\]

Then $\lVert a_{i,h,n}\rVert_\infty\le BCQ^{w/2}$. Each edge is the matrix

\[
A_{i,h}(x,y)=\psi(hx^tB_i y),\qquad x,y\in\mathbf F_Q^d.
\]

Orthogonality implies $A_{i,h}A_{i,h}^*=Q^dI$, because $h\ne0$ and $B_i$ is invertible. Thus its operator norm on the counting-measure $\ell^2$-space is $Q^{d/2}$. The endpoint vectors have norm at most $BCQ^{(w+d)/2}$; each of the $k-2$ internal diagonal multiplication operators has norm at most $BCQ^{w/2}$. The bilinear expression uses a transpose, rather than a Hermitian transpose, at one endpoint, but the same absolute Cauchy–Schwarz bound applies, equivalently after conjugating that endpoint vector.

There are $k-1$ edge operators. Therefore

\[
|S_{h,n}|\le (BC)^k Q^{kw/2+(k+1)d/2},
\]

and, since there are $Q-1<Q$ nonzero values of $h$,

\[
|R_{k,n}|\le (BC)^k Q^{k(w+d)/2+d/2+1}.
\tag{5}
\]

All factors depending on the vertex potentials have complex modulus one. Their variation with $i,h,n$ does not affect the estimate. The matrices may be fixed once and for all, and characteristic $2$ presents no obstruction: only the nondegeneracy of the bilinear pairings is used.

## QG-04: spectral extraction and the affine middle bound

The elementary spectral fact needed here concerns an actual, rather than virtual, representation. If an invertible complex linear operator $F$ has

\[
|\operatorname{Tr}(F^n)|\le A_0 R^n\quad(n\ge1),
\]

then every eigenvalue has modulus at most $R$. To prove it, the trace series

\[
\sum_{n\ge1}\operatorname{Tr}(F^n)z^{n-1}
=\sum_\lambda\frac{m_\lambda\lambda}{1-\lambda z}
\]

is analytic for (|z|<R^{-1}). The distinct eigenvalues $lambda$ have positive integer multiplicities $m_\lambda$, so the pole at $\lambda^{-1}$ cannot cancel. Consequently $|\lambda|\le R$. Jordan blocks do not change traces of powers; semisimplicity is unnecessary.

Apply this fact to the actual representation $V^{\otimes k}\oplus E_k$ in (2), and use (5). If $\alpha$ is an eigenvalue of the original $q$-Frobenius on $V$, then $\alpha^{e_k k}$ is an eigenvalue of this representation over $\mathbf F_{q^{e_k}}$. It follows that

\[
|\iota\alpha|^{e_k k}
\le q^{e_k[k(w+d)/2+d/2+1]},
\]

or

\[
|\iota\alpha|\le q^{(w+d)/2+(d/2+1)/k}.
\]

Let $k\to\infty$. This gives

\[
|\iota\alpha|\le q^{(w+d)/2}
\quad\text{on }H_c^d(U,\mathcal F).
\tag{6}
\]

The spectral argument is applied for all $n\ge1$ with $k$ fixed before taking $k\to\infty$. There is no requirement that $e_k$, the dimensions of $E_k$, or the Betti numbers of the hypersurfaces be uniformly bounded in $k$. The multiplicative constant ($BC$^k) is harmless in the all-$n$ spectral limit.

This completes a full independent proof of SG-09 from SG-08 and the explicitly cited geometric inputs. The only pointwise hypothesis used for fixed $\iota$ was the uniform trace bound (3). Pointwise eigenvalue bounds of weight at most $w$ imply (3) with $C=\operatorname{rank}\mathcal F$, or the maximum rank over the finitely many components.

## QG-05: every compact-support degree on a smooth affine scheme

Suppose $\mathcal F$ is lisse on smooth affine $U/\mathbf F_q$ of pure dimension $d$, with all pointwise Frobenius eigenvalues of $\iota$-absolute value at most $Q^{w/2}$. Then

\[
|\iota\alpha|\le q^{(w+i)/2}
\quad\text{for every eigenvalue on }H_c^i(U,\mathcal F).
\tag{7}
\]

Proof is by induction on $d$. For $d=0$, after a finite extension the scheme is a finite disjoint union of rational points. Only degree zero occurs, and the assertion is precisely the pointwise assumption. Descending the modulus through that finite extension is immediate.

For $d>0$, Artin vanishing and duality give $H_c^i(U,\mathcal F)=0$ for $i<d$. QG-04 handles $i=d$. Choose a generic smooth hyperplane section $H$ in an affine closed immersion of $U$, satisfying QG-01 for the dual sheaf, over a finite extension if necessary. It is smooth affine of dimension $d-1$, and the restriction of $\mathcal F$ has the same pointwise upper bound. For $i\ge d+1$, the map

\[
H_c^{i-2}(H,\mathcal F|_H)(-1)\longrightarrow H_c^i(U,\mathcal F)
\]

is surjective when $i=d+1$, and an isomorphism when $i\ge d+2$. Induction bounds eigenvalues on the untwisted source by $q^{(w+i-2)/2}$. Twisting by $(-1)$ multiplies their moduli by $q$, giving $q^{(w+i)/2}$. A quotient cannot acquire any new eigenvalue. This proves all remaining degrees. The passage through a finite field extension preserves the conclusion since $|\alpha^e|\le(q^e)^{(w+i)/2}$ is equivalent to (7).

The border value $i=d+1$ is covered by a surjection, not an isomorphism; surjectivity is sufficient for the bound. Omitting that border value would leave a genuine hole in an induction.

## QG-06: constructible sheaves and bounded constructible complexes

Let $X/\mathbf F_q$ be separated of finite type and let $\mathcal G$ be a constructible $\overline{\mathbf Q}_\ell$-sheaf. Assume all its pointwise Frobenius eigenvalues have $\iota$-absolute value at most $Q^{w/2}$. Then the conclusion (7) holds for $H_c^i(X,\mathcal G)$.

Here is the needed reduction explicitly. Nilpotents do not affect the étale topos, so replace $X$ by its reduction. Over the perfect field $\mathbf F_q$, each irreducible component has a dense smooth locus, and constructibility gives a dense locus on which $\mathcal G$ is lisse. Remove the intersections of distinct components and choose a dense affine open in the resulting smooth lisse locus of each component. Their disjoint union is an open stratum $S$ of $X$, each component of which is smooth affine and on which $\mathcal G$ is lisse. The closed complement has smaller dimension on each component. Repeating gives a finite closed filtration with strata finite disjoint unions of smooth affine schemes where the sheaf is lisse. Components of different dimensions can be handled separately in each stratum.

For the inclusion $j:S\hookrightarrow X$ and closed complement $i:Z\hookrightarrow X$, the localization triangle gives

\[
H_c^r(S,j^*\mathcal G)\longrightarrow H_c^r(X,\mathcal G)
\longrightarrow H_c^r(Z,i^*\mathcal G).
\]

Every eigenvalue in the middle occurs in one of the outer terms as a subquotient. Both outer groups are in the same degree $r$; no extra shift is introduced by this induction. QG-05 bounds each smooth affine stratum, and induction on the filtration yields the desired upper $w+r$ bound for $X$.

More generally let $K\in D_c^b(X,\overline{\mathbf Q}_\ell)$ and assume each ordinary cohomology sheaf $\mathcal H^b(K)$ has pointwise upper bound $w+b$. The compact-support hypercohomology spectral sequence

\[
E_2^{a,b}=H_c^a(X,\mathcal H^b(K))\Longrightarrow H_c^{a+b}(X,K)
\]

is Frobenius compatible and finite in each total degree. Its $E_2$-terms have upper bound $w+b+a$, so all subquotients contributing to total degree $n$ have upper bound $w+n$. Thus $H_c^n(X,K)$ has that bound. This is an upper absolute-value statement. A mixedness filtration, algebraicity of arbitrary coefficient eigenvalues, independence of $\ell$, and integral refinements are not silently included in its assertion.

## QG-07: smooth proper purity and the precise Weil-I scope

Let $X/\mathbf F_q$ be smooth proper of pure dimension $d$. Suppose $\mathcal F$ is lisse and pointwise $\iota$-pure of weight $w$. QG-06 gives upper bound $q^{(w+i)/2}$ on $H^i(X,\mathcal F)=H_c^i(X,\mathcal F)$. The dual sheaf is pointwise pure of weight $-w$, so it gives upper bound $q^{(-w+2d-i)/2}$ on $H^{2d-i}(X,\mathcal F^\vee)$. Poincaré duality pairs these two groups into $\overline{\mathbf Q}_\ell(-d)$. If $\alpha$ occurs in the first, then $q^d/\alpha$ occurs in the second. Its upper bound yields the opposite inequality

\[
|\iota\alpha|\ge q^d/q^{(-w+2d-i)/2}=q^{(w+i)/2}.
\]

Thus equality holds. Projectivity is not needed in this final deduction. The projective hyperplane induction in SG-10 is also correct independently: lower degrees use weak Lefschetz; middle-degree upper bounds use $H_c^d(U)\to H^d(X)\to H^d(H)$; duality supplies the lower bound; upper degrees are dual to lower degrees.

For constant coefficients the pointwise trace bound is $1$, independent of the embedding. The proof therefore establishes the absolute-value assertion for every embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. Algebraicity over $\mathbf Q$ can also be extracted: if an eigenvalue were transcendental over $\mathbf Q$, some such embedding could send it to a complex transcendental number of arbitrarily large modulus (choose a transcendence basis containing it, embed that basis algebraically independently, and extend to the algebraic closure), contradicting the common upper bound. Thus it is algebraic, and all its complex conjugates have the asserted modulus.

The individual characteristic polynomials' integrality, rationality, and independence of $\ell$ should be attached using their stated formal background, not described as consequences of the pole lemma alone. Deligne *Weil I*, (1.7) implies (1.6), is an exact published locator for that formal completion. No assertion about a Hodge polarization or the Hodge standard conjecture follows merely from the effective trace representation (2). No RH or Dirichlet-GRH input is used in the proof above; accepting those hypotheses does not alter this dependency statement.

## Check boundaries and source record

1. The result is a reconstruction from established étale-cohomological foundations, including generic base change, Artin vanishing, trace formula, Künneth and duality. These are cited background, not all re-proved from their foundations here.
2. I checked complete local proofs for the effective trace, Fourier estimate, spectral extraction, all-degree induction, stratification, and duality conclusion. I read all of SG-08–10 and all of Katz A.1–A.5. No flaw was found in the strengthened route.
3. I checked the statements and complete short proofs of Wan–Zhang Lemmas 3.2 and 3.8. SGA 4½ Corollary 2.9 was verified as their precise citation; its original passage was not independently read in this audit. Katz's separate 1.9 locator was read in Katz's proof. These two source-read events must not be described as a full rereading of SGA 4½.
4. I checked BBD 4.1.1–4.1.3 in the original scan, printed pp. 102–103. Its cited SGA 4 XIV 3.1 proof is background; it was not independently reread.
5. The abandoned middle-concentration route is unnecessary. The initial proposed (j_!) step itself is sound when $j$ is affine: BBD 4.1.3 (and 4.1.10$i$) makes (j_!) perverse exact. An affine chart intersection with a projective closure is such an affine open immersion. A generic hypersurface satisfying only smoothness, without the weak Lefschetz condition, is not covered.

### Primary source URLs

- Katz ACT: <https://web.math.princeton.edu/~nmk/old/ACT.pdf>, Corollary 3.4.1, pp. 180–181; Appendix A.1–A.5, pp. 218–221. Local cache `reference_cache/sign_gate/Katz_ACT.pdf` and `.txt`.
- BBD: <https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/faisceaux_pervers.pdf>, 4.1.1–4.1.3, pp. 102–103; 4.1.10, p. 106. Local original scan `reference_cache/sign_gate/BBD.pdf`.
- Wan–Zhang: <https://zhangdingxin.gitlab.io/math/pdf/improved-ew.pdf>, Theorem 3.1, Lemmas 3.2, 3.8–3.9, pp. 11–14; verified as an independent proof of the particular generic-purity/Gysin formulation, not as an input of its colevel theorems.
- Noether normalization: <https://stacks.math.columbia.edu/tag/00OY>, Lemma 10.115.4.
- Deligne, *La conjecture de Weil. I*: <https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf>, (1.6)–(1.7).

## Final parent-text check

After writing the reconstruction above, I read the complete section_main.tex, SHA-256 ba7b504a76a40b1797ec697ce201175707f8f315f500f5158809f26b3f44a04f.

The full mathematical statements and proofs HS-01, HS-02, HS-03, SG-08, SG-09, SG-11, SG-10, HS-04, HS-04B, and HS-05 all pass. In particular SG-11 is a full proof of the general constructible compact-support upper inequality, and its use of the first Gysin surjection is correct. The proof can be made wholly explicit by taking the smooth affine lisse filtration described in QG-06; such a filtration supplies its open stratum unions.

The HS-04B final scope is also correct. Its base lisse sheaf lives on the smooth affine curve A1 minus the two points 1 and -1; its compact-support cohomology equals that of its extension by zero to A1. On the special section xy=1, the tensor restriction becomes geometrically constant up to the unramified factor epsilon. The required ordinary restriction is already not an isomorphism in degree zero: the product has no invariant sections for the external Kummer sheaf, while the section does. Thus this example violates the actual weak Lefschetz hypothesis and only refutes smoothness alone. The initial constant-sheaf example is correctly described as compatible with effective Gysin cancellation, and refutes middle concentration only.

The final HS-06 source-provenance paragraph was read, but I did not independently rerun its inventory, wrapper hash comparisons, or declaration searches. These claims remain the responsibility of their recorded source checks; my event is explicitly background, not a Lean certificate.

