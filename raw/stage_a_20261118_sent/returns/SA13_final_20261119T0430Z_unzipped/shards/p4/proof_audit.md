# Mathematical checks for shard p4

Date: 19 November 2026. This audit distinguishes a proof supplied here from a statement found in a primary source. The frozen diplomatic transcriptions are never altered. Executable finite checks are in `code/computations.py` and their complete output is in `outputs/computations.txt`; those checks do not prove the geometric assertions in which the examples occur.

## 1. Quotients and the Reynolds identity

For a linearly reductive group, the projection onto invariants is natural for equivariant linear maps. If `r` is invariant, multiplication by `r` is equivariant, so naturality gives E(rf)=rE(f). This proves the identity used in C-SA13-400. Averaging the sign action on a polynomial ring in the executable example illustrates it. In positive characteristic, reductivity alone does not supply a Reynolds projection. This qualification is visible in the checked second edition of Mumford–Fogarty, Definition 1.5 and the proof of the affine quotient theorem.

The claims concerning proper actions, stabilizers and torsors are carried with the conventions of that source, not re-proved from the fragment. In particular its freeness is the action graph being a closed immersion. The example preceding Proposition 0.9 explicitly distinguishes this from merely trivial geometric stabilizers. The margin asking for flatness does not specify a complete flat-equivalence-relation theorem. An algebraic-space quotient theorem would require a represented relation and the relevant sheaf topology, and cannot silently fill that omission.

## 2. Biextensions and quadratic Picard formulas

The low-degree spectral sequence for the derived biextension description has the form

\[
0\to\operatorname{Ext}^1(P,\underline{\operatorname{Hom}}(Q,G))
\to\operatorname{Biext}^1(P,Q;G)
\to\operatorname{Hom}(P,\underline{\operatorname{Ext}}^1(Q,G))
\to\operatorname{Ext}^2(P,\underline{\operatorname{Hom}}(Q,G)).
\]

Consequently internal Hom vanishing, on every object of the site, kills both outer terms. The automorphisms are Hom(P⊗Q,G), which also vanish under that hypothesis. This checks the precise interpretation of C-SA13-405; global Hom vanishing would not suffice. The source for the derived interpretation is SGA7 VII3.6.5, and VIII1.1.4 and1.4 give the displayed consequence. The pointed-map hypotheses in VII2.9.4 remain necessary for the more geometric additivity and transpose claims C-SA13-406–407.

For an abelian variety and a line bundle L, the cube formula yields

\[
[n]^*L=L^{n(n+1)/2}\otimes([-1]^*L)^{n(n-1)/2}.
\]

In NS, inversion acts trivially and the two exponents add to n². Thus the parallelogram identity has a plus between the two terms on its left. The literal minus in 36:59 is false: take a nonzero ample class and u=1,v=0, obtaining 0=2[L]. An ample NS class is not torsion, so this is a counterexample within the intended geometric situation, not just a polynomial analogy. The finite integer calculation independently exhibits the same error. The direction of the displayed Δ arrow must also be checked on the scan.

For an extension 0→K→E→N→0 with projection h and an already supplied homomorphism s:N→E satisfying h∘s=2id, the map n↦(n,s(n)) splits its pullback along [2]. After inverting 2 this gives a splitting of the original extension. This is the conditional algebra behind C-SA13-409; it does not construct the unfinished functorial lift s on the manuscript's unstated base.

## 3. Haar measures, support limits and compact generation

Write Δ_U={H: H∩U={e}}. Directly from this definition,

\[
\Delta_U\cap\Delta_V=\Delta_{U\cup V},\qquad
\bigcup_j\Delta_{U_j}\subseteq\Delta_{\cap_jU_j}.
\]

The second inclusion is enough for the finite-cover argument on the reused sheet. The first identity disproves its literal intersection subscript. In discrete G=Z the finite sets U={0,±2}, V={0,±3} are relatively compact identity neighborhoods and H=2Z belongs to Δ_(U∩V) but not Δ_U. All hypotheses of this elementary counterexample are checked.

Here is the support argument behind C-SA13-413. Let nonzero positive right Haar measures μ_i on varying closed subgroups converge vaguely to μ≠0. If h is in supp μ, neighborhood positivity permits a subnet and h_i∈supp μ_i tending to h. Right translation on compactly supported test functions is continuous uniformly on a common compact set; vague convergence gives locally bounded masses there. Therefore invariance of μ_i under h_i passes to invariance of μ under h. Its nonempty closed support H is consequently stable under multiplication and inversion and contains e, hence is a closed subgroup; μ is a nonzero invariant Radon measure on H. Nets, rather than a metrizable-sequence reduction, are needed in the stated generality.

For compact generation, the propagation step is elementary: if a compact generating identity neighborhood L and compact K satisfy LK⊂KH, then L^aK⊂KH for every a by induction, and G=KH once the union of powers of L is G and e∈K. This is the essential use of compact generation in the cocompactness argument. Its necessity has an exact counterexample: G=⊕_(j≥1) Z with the discrete topology, H_n the subgroup spanned by the first n coordinates. Every finite subset is eventually contained in H_n, so H_n→G in the Chabauty topology. No G/H_n is compact, whereas G/G is compact. All these groups are unimodular.

The full normalized-slice compactness, semicontinuity of covolume, continuity on the cocompact locus, and uniform-discreteness compactness are checked against Bourbaki, Intégration VIII§5 nos.1–4, including Propositions1–8 and Theorems1–2. They are source checks, not consequences claimed solely from the short support argument. The retained draft's condition (L) excludes small discrete subgroups; the printed source states a condition using finite subgroups. Lie groups satisfy either through the no-small-subgroups property. This does not decide the cut-off word on the retained sheet.

## 4. Vertical divisors, Kummer theory and the Brauer obstruction

For a vector d=(d_1,…,d_r) of positive integers, elementary integral row operations send d to (g,0,…,0), g=gcd(d_i). Hence

\[
\Gamma=\mathbb Z^r/\mathbb Zd\simeq\mathbb Z^{r-1}\oplus\mathbb Z/g.
\]

Local factoriality identifies the component cycles with Cartier divisors; without it this entire lattice need not be the vertical Cartier-divisor group. Raynaud1970 §§6.1.3,6.1.11 and Theorem6.4.1 make that distinction. His equality uses E∩P^τ, whereas the manuscript sometimes uses P^0. Since P^0⊂P^τ, its kernel R is a cyclic subgroup of tors Γ, of order e dividing g; equality with all tors Γ is an additional assertion, automatic in the stated curve comparison but not supplied in arbitrary dimension.

The final original-image collation of SGA7 IX12.1–12.2 confirms the curve-only scope: printed465–469, physical PDF470–474. The implication chain in12.1(a) and the index-one conclusions in(b)–(d) are kept distinct from arbitrary-dimensional claims. There is also an error in the original printed formula12.1.5 onp466: it presents Z^I→Γ(S,E) as an isomorphism, omitting the principal-fibre relation Σd_i[X_i]. Take X=P¹_S; I has one element and E is trivial, so the literal assertion would be Z≅0. The correct vertical-divisor presentation is Z^I/Z(d_i). This source typo does not alter C-SA13-415, whose quotient and Smith reduction were independently proved and compared with Raynaud. It is recorded to prevent a precise page citation from being mistaken for approval of every printed formula on that page.

Tensoring the presentation Z --e→ Z→Z/e→0 with Z_l gives

\[
R\otimes\mathbb Z_\ell=\mathbb Z_\ell/e\mathbb Z_\ell
\simeq\mathbb Z/\ell^{v_\ell(e)}.
\]

Thus “Z/l” fails at e=l². Substitution of d for e is not licensed before the equality of vertical kernels has been established. Likewise, from 0→δ′→δ→δ″→0 one cannot infer δ[n]/δ′[n]=δ″[n]. With δ=Z/4, δ′={0,2}, n=2, the left group is zero and the right group is Z/2. This is why the manuscript's correction of the torsion sequence matters.

The numerical identity gcd(μ_i d_i)=gcd(μ_i)gcd(d_i) is false: (d_1,d_2)=(2,3), (μ_1,μ_2)=(1,2) gives 2 versus1. This example checks only arithmetic. It is not asserted to be a realizable proper regular model with those geometric multiplicities. Raynaud's index formula is retained with its geometric hypotheses, and the inserted factorization is left as an ink/hypothesis alarm.

The Picard–Brauer obstruction comes from the low-degree Leray/Hochschild–Serre sequence. A line-bundle class over the separable closure fixed by Galois can have an obstruction θ∈Br(K). If a zero-cycle has degree d, restriction to each of its residue fields followed by corestriction shows dθ=0. In particular a degree-one zero-cycle kills the obstruction. Colliot-Thélène–Skorobogatov, The Brauer–Grothendieck group, Proposition1.4.3 in the opened author version, proves that for a strictly henselian trait Br(K) is p-primary; when the residue field is algebraically closed it is zero. Proposition4.3.2 and Remark4.3.3 supply the descent sequence and degree-one splitting. These are scoped facts, not a proof of every p-primary amended formula in 36:61–71.

For n invertible on the base, the étale Kummer sequence computes n-torsion line bundles. In residue characteristic p the p-power Kummer sequence is exact in the flat topology, not on the small étale site. This topology must be specified before interpreting the manuscript's arbitrary-n insertion. Proper henselian finite-étale specialization (Stacks, Proposition58.9.1, Tag0A48) justifies the prime-to-p torsor lift; it does not by itself lift arbitrary μ_p-torsors as étale covers.

Bounded exponent alone does not make an inverse limit zero: a constant system Z/p with identity transition maps is a counterexample. The actual Kummer diagram for μ_(l^(ν+2))→μ_(l^(ν+1)), z↦z^l, has multiplication by l on the relevant Brauer terms. If all terms are killed by l^N, compatibility gives x_i=l^N x_(i+N)=0. This is the missing transition-map argument in C-SA13-420, not a counterexample to the correctly interpreted limit calculation.

## 5. Orthogonality and arithmetic weights

The full Tate-module orthogonality theorem is SGA7 IX2.4 under its henselian-trait and l≠p hypotheses. The arithmetic method described in IX2.6(a) gives the inclusion and explicitly does not give the equality. The manuscript's broader assertion of full orthogonality by that argument therefore needs qualification.

The weight separation itself does not need semisimplicity. If finite-dimensional vector spaces V,W carry F_V,F_W with relatively prime annihilating polynomials a,b, and uF_V=F_Wu, then a(F_W)u=0 and b(F_W)=0. A Bézout relation Aa+Bb=1 gives u=0. The source weights in the tensor product have complex absolute values q² or q^(3/2), while the target Tate twist has q. Distinct absolute values force coprimality. The exact Jordan-block example in the program illustrates the non-semisimple case; it does not calculate the whole geometric Frobenius representation.

A polarization may be used to compare the relevant Tate lattices after clearing a finite denominator: injectivity into the rational Tate module and torsion-freeness prevent a rationally vanishing integral pairing from becoming nonzero. At a finite level one can pass to a finite extension making a particular torsion group rational, but that extension may depend on the level ν. The quantifiers ∀ν∃K′ and ∃K′∀ν are different. The program's nonzero symplectic pairing shows why pointwise trivialization of finite-level Galois action cannot itself prove a pairing vanishes.

## 6. Weighted intersection lattices and component pairings

Let M be the symmetric intersection matrix and D=diag(δ_i). The manuscript's map is u=D^(-1)M, so it is D u, not necessarily u, that is symmetric. Its right null vector is the multiplicity vector d; its left relation uses Dd. In the example

\[
D=\operatorname{diag}(1,2),\quad
u=\begin{pmatrix}-2&2\\1&-1\end{pmatrix},\quad
Du=\begin{pmatrix}-2&2\\2&-2\end{pmatrix},
\]

one has u(1,1)^t=0 and (1,2)u=0. The weighted annihilator generated by (-2,1) pairs with [e_1] in Z²/Z(1,1) by -2, so this integral pairing has index2. Cancelling “parfait” is mathematically significant. In the unweighted case, ker(d·) is exactly Hom(Z^r/Zd,Z); this quotient is free precisely when gcd(d_i)=1.

For a free lattice L and an injective symmetric map u:L→L* with finite cokernel, define

\[
b(\bar a,\bar c)=\langle u_\mathbb Q^{-1}a,c\rangle\pmod{\mathbb Z}.
\]

Changing a by u(x) adds the integer ⟨x,c⟩, and similarly for c; symmetry is inherited. If a pairs integrally with every c∈L*, then u_Q^(-1)a∈L, so the induced map coker u→Hom(coker u,Q/Z) is injective and hence bijective by equal finite cardinalities. Rank one u=-m gives -ac/m modZ, tested exactly by the program. This proves the abstract discriminant assertion but not its identification with Grothendieck's geometric pairing. The latter is matched with the explicit hypotheses of Bosch–Lorenzini2002 Theorem4.6 and Corollary4.7; their imperfect-residue-field qualifications must remain visible.

## 7. The formal A-families: axioms and exact deductions

The two drafts rename axioms and change from a field to a ring. Every deduction below uses the content of H (closure under inverse formal coordinate maps) and D (closure under Hasse divided derivatives), not an ambiguous letter alone. The choice of constant ring A_0 is part of the structure.

### Constants, substitution and minimal examples

Unital rings containing coordinates and closed under zero-constant substitution contain prime-ring polynomials. Unit-reflection then supplies inverses of nonzero prime-ring constants when the ambient coefficient ring is a field, hence its prime field. Thus with k=Q the family Z[t_1,…,t_n] satisfies the coordinate, ring, composition and ordinary differentiation axioms but does not contain1/2. The first draft's minimum P[t] under a,b,d is false if c has genuinely been removed and P still means the prime field. This is a complete family, not just a one-variable subring. With unit-reflection included, localization of prime-field polynomials at polynomials nonzero at the origin is required.

A continuous formal substitution allows finitely many nilpotent input constants: their generated ideal is nilpotent, so in each prescribed coefficient and adic precision only finitely many terms contribute. Translation by such constants is an automorphism. Evaluation at1 has no such meaning in k[[s]]: Σs^j cannot be evaluated by a finite sum in general. The exact Z/8 example verifies the finite-nilpotence mechanism, not unrestricted evaluation.

### What H alone gives, and what requires D

If h∈A_n has zero constant, apply H to

\[
(t,s)\longmapsto (t,(1+h(t))(1+s)-1).
\]

Its inverse evaluated at s=0 yields (1+h)^(-1)-1∈A_n. For b∈A_n the same applies to bh, so the augmentation ideal lies in Jac(A_n). H alone need not reflect all ambient units. A full counterfamily is

\[
k=\mathbb Q,\quad A_0=\mathbb Z,\quad
A_n=\mathbb Z+(t_1,\ldots,t_n)\mathbb Q[[t_1,\ldots,t_n]].
\]

It is a unital ring family containing coordinates, closed under the allowed zero-constant substitutions. Its allowed coordinate automorphisms have zero constant, and their formal inverses again have zero constant with rational coefficients, hence belong to the family. Nevertheless2 is invertible in k[[t]] and not in A_n. This refutes the strong H-only assertion with every family hypothesis checked. It does not satisfy D, since extracting a rational positive-degree coefficient can leave A_0.

If D is also assumed and f∈A_n is an ambient unit, invert the triangular coordinate map (t,s)↦(t,f(t)s). The inverse's last coordinate is f(t)^(-1)s. Applying the first Hasse derivative in s and then s=0 gives f^(-1)∈A_n. This repairs the manuscript's inadmissible s=1 shortcut.

For a monic polynomial whose two residue factors are coprime, the coefficient map multiplying the two monic factors has linearization (a,b)↦a g+f b. Its determinant is the resultant, a unit by coprimality. Applying H to this coefficient-coordinate map produces the unique lifted factorization. Together with the Jacobson-ideal result this is the henselian-pair mechanism. The one-equation implicit-function argument is the same augmented-map construction (t,z)↦(t,P(t,z)) followed by zero evaluation.

### Derivatives, flatness and geometric constructions

Hasse derivatives satisfy D_aD_b=binomial(a+b,a)D_(a+b), the product formula, and εD_αf=a_α. These identities prove coefficient descent and stability under composition of chartwise differential operators. In a Q-algebra ordinary derivative closure and Hasse derivative closure coincide because α! is invertible. “Characteristic0” alone is weaker: Z[t,t²/2] is stable under the ordinary derivative but its second Hasse derivative of t²/2 is1/2. This one-variable ring is only a counterexample to that bare algebraic inference; it has not been claimed to satisfy all the A-family composition and H axioms. In characteristic p, D(t^p)=0 whereas the p-th Hasse derivative is1.

If the margin's d means differentiation alone, k=Q and A_n=Q[t_1,…,t_n] satisfy it, but completion is not faithfully flat: the nonzero A_1-module A_1/(1-t) becomes zero over Q[[t]]. If d includes H, this example is inadmissible because inverse coordinate maps need not be polynomial. The stronger H+D question is therefore not refuted by this example. It remains separated in the problem index.

An A-transverse fibre product follows by an augmented inverse-function construction if H is present. The early assertion before H has a missing dependency. Once an A-chart exists, the normal-neighborhood, coefficient, graph, principal-parts and differential-operator constructions reduce to the displayed finite Taylor identities. These are local verifications. Global projective-module descent and arbitrary finite-module versions are not inferred from them. Likewise a quotient criterion must refer to the target space and an effective relation with the stated smooth/chart hypotheses; the undecided X/X′ subscripts affect its meaning.

### Flows, BCH and Frobenius

Over a characteristic-zero field the formal ODE recursion determines a unique formal solution. Adding time as a coordinate converts a nonautonomous field ξ(t,x) into the autonomous field ∂_t+ξ. Closure of that solution in A is the additional flow axiom, not a consequence of existence in k[[t,x]]. The elementary exp, log and trigonometric identities were recomputed to the recorded order.

The algebraic-power-series family is not flow closed: exp(t) is not algebraic over k(t) in characteristic0. For completeness, suppose a polynomial relation among e^(it) exists with coefficients in k(t), of minimal number of terms; normalize its constant coefficient to1. Differentiating removes that term. Minimality forces each remaining coefficient a_i to satisfy a_i′+i a_i=0. A nonzero rational function cannot have nonzero constant logarithmic derivative: at a finite zero or pole it has a pole, and at infinity its logarithmic derivative tends to0. This is a contradiction.

For the class-two Heisenberg BCH law, (x,y,z)*(x′,y′,z′)=(x+x′,y+y′,z+z′+(xy′-yx′)/2). Associativity is the bilinear cocycle identity B(a,b)+B(a+b,c)=B(b,c)+B(a,b+c). The exhaustive finite rational check illustrates that identity. It is not a proof that general BCH coefficients belong to the manuscript's chosen A-family after Ado's theorem. In particular a formal time1 evaluation needs its own justification.

A submersion's vertical vector fields are closed under bracket because they annihilate every pulled-back function. Conversely Bolsinov–Zuev2009 Theorem2 supplies independent formal first integrals for a constant-rank involutive distribution over a characteristic-zero field. That ambient theorem does not automatically put the first integrals in A. The manuscript's Pfaff and integral-quotient axioms therefore retain content beyond ordinary formal Frobenius.

## 8. Weierstrass division over a general complete linear topology

Let A be separated and complete for a linear topology, F=Σa_i z^i, a_N a unit and a_0,…,a_(N-1) topologically nilpotent. For each open ideal I, work in B=A/I. The finitely many lower coefficients generate a nilpotent ideal J of B. Consider

\[
\theta:B^N\oplus B[[z]]\longrightarrow B[[z]],\qquad
(b_0,\ldots,b_{N-1},Q)\longmapsto\sum_{i<N}b_i z^i+FQ.
\]

Modulo J, write F=z^N U with U a unit **series**, not merely its constant term. Every series has a unique remainder of degree<N and a unique quotient by z^NU, so θ modJ is bijective. Each J-adic graded piece has the same decomposition, because multiplication by U is invertible there. The ideal J is finitely generated, so J^a B[[z]]=(J^a B)[[z]]. Since J is nilpotent, finite induction on this filtration proves θ bijective; no infinite-module Nakayama shortcut is being used. Uniqueness makes these solutions compatible as I varies, and A[[z]]=lim_I(A/I)[[z]] gives the desired division over A.

Regularity of F follows from uniqueness with zero remainder. Dividing z^N by F produces a monic polynomial P with lower coefficients topologically nilpotent and a quotient that is a unit; this gives F=UP and uniqueness. The statements match Strickland, FPFP Theorem33.1/Corollary33.2; the nilpotent-coefficient precursor is Formal schemes and formal groups, Lemma5.14/Corollaries5.15–5.16.

The executable Z/8 example F=2+4z+z²+z³ gives P=6+2z+z² and U=7+z. Modulo2 one has F=z²(1+z), showing exactly why the final manuscript α must be a full unit series if the argument is to work. The code checks the quotient with a longer buffer than the asserted precision, and records both the precision and the nilpotent perturbation used.

## 9. Scope of this audit

Statements certified here by direct algebra are explicitly distinguished from theorems used through checked primary sources. None of the finite calculations certifies proper base change, absolute purity, constructibility, resolution of singularities, or comparison of geometric component pairings. Their hypotheses and exact published matches are recorded in the claims, references and search log. Source identity is not an assertion of authorship or manuscript priority.

## 10. Codex conventions: the support complex and its one-degree shift

Write `Φman` only in this review for the manuscript's Φ. Its finite-extension support construction gives the triangle

\[
\Phi_{\mathrm{man}}\longrightarrow\Lambda_{X_s}
 \longrightarrow R\Psi\Lambda\longrightarrow\Phi_{\mathrm{man}}[1].
\]

The usual modern definition instead has `RΦ=Cone(Λ→RΨ)`. Consequently `Φman=RΦ[−1]` and `H^i(Φman)=R^{i−1}Φ`. This is forced independently by K34-05 formulas(1.9),(2.5)--(2.6) and K34-08 lines434--458; it is not a conjectural emendation. At a geometric special point with strict localization X′,

\[
0\to\Phi^0_{\mathrm{man},x}\to\Lambda
\to H^0(X'_{\bar\eta},\Lambda)
\to\Phi^1_{\mathrm{man},x}\to0,
\qquad
\Phi^i_{\mathrm{man},x}=H^{i-1}(X'_{\bar\eta},\Lambda)\quad(i\ge2).
\]

Thus a disconnected local geometric generic fibre is measured in manuscript degree1; an isolated relative-dimension-n lci singularity has its usual middle vanishing cycles in manuscript degree n+1. In the proper case the same triangle after global sections is the specialization triangle. Without properness, a global comparison with cohomology of the special fibre needs additional hypotheses; the sheaf/stalk definition remains available. Original SGA7 XIII1.3 and2.1.4 and Illusie2021 §1.1 are the checked modern conventions. Original XIII2.1.9, printed104/PDF110, supplies a particular compactification comparison with a relative normal-crossing boundary and tame coefficient behaviour. It is not an unconditional assertion for every open compactification.

For the inverse-limit step, an inverse system of finite abelian groups is Mittag--Leffler: for each fixed stage, its descending family of images is a descending family of subgroups of a finite group, hence stabilizes. Its first derived inverse limit vanishes. Applying this to the relevant kernels in the finite-coefficient exact sequence makes inverse limit exact. A bounded diagonal of the finite-coefficient spectral sequence can likewise be handled with its finite filtrations. This argument justifies the limit of global groups and the displayed `limν H^p(...)`; it does not identify that expression with ordinary sheaf cohomology of a naive inverse-limit sheaf. C805 preserves the author's explicit reservation about adic constructibility and systems.

If the support consists of finitely many closed geometric points, a sheaf on that support has no positive-degree cohomology and its global sections are the finite direct sum of its stalks. The hypercohomology spectral sequence therefore collapses to the direct-sum formula used in C809. This statement requires the finite-support hypothesis; it is not a claim about arbitrary zero-dimensional non-quasi-compact supports.

## 11. A ramification index is not always a field degree

For a finite map of traits, pullback of the closed Cartier divisor is e times the new closed divisor. The Gysin generator therefore pulls back by e. This follows from the divisor class, or from the Kummer boundary of a uniformizer. It does not require the finite extension to be totally ramified in the stronger sense that its field degree is e. Riou2014 XVI §§1--3 supplies the purity/Gysin framework used here.

Here is a counterexample with every relevant hypothesis stated. Fix a prime p and let k be a separable closure of `F_p(a)`. The element a has no p-th root in k: a purely inseparable root is not in a separable algebraic extension. Set

\[
R=k[[\pi]],\qquad B=R[u]/(u^p-\pi u-a).
\]

R is a complete strictly henselian DVR. The monic polynomial makes B finite free of rank p over R. Its reduction is the irreducible polynomial `u^p−a`, so B is local, its maximal ideal is generated by π, and its residue field has degree p over k. Since B has dimension1 and its maximal ideal needs one generator, it is a regular local ring, hence a DVR and a domain. The generic polynomial has derivative `−π≠0`, so `L=Frac(B)` is separable over `K=Frac(R)`, of degree p. Yet π is still a uniformizer of B, so e=1. For example, with p=2 and ℓ=3, multiplication by the field degree and multiplication by e differ already modulo3.

This refutes the unrestricted degree multiplier in C807. It does not refute the intended smooth-acyclicity argument. At any finite stage, adjoining sufficiently high ℓ-power roots of a uniformizer multiplies the support generator by an ℓ-power that annihilates the fixed finite coefficient group. These extensions are separable and tame because ℓ≠p. They can be taken after any chosen finite extension, so every class in the filtered support colimit is killed. Purity then gives smooth local acyclicity and the usual proper smooth specialization comparison. The repaired argument needs the killing extensions, not equality between every ramification index and every field degree.

## 12. Purity, residues, continuous wild invariants and filtration lengths

Absolute purity is used as a checked theorem, not proved by a finite computation. Riou2014 XVI3.1.1 applies to a codimension-c regular closed immersion between noetherian regular schemes with n invertible, and identifies the extraordinary inverse image with `Λ(−c)[−2c]`. No excellence hypothesis is added. Along a flag of regular divisors, transitivity gives the codimension shift and twist. A locally constant coefficient on the ambient X can be included by tensoring. The localization sequence then has Gysin source `H^{i−2c}(Y,F(−c))`, not cohomology of X in that source position.

For a principal divisor on a strictly local regular scheme, its line bundle has zero first Chern class. In the normal-crossing induction, use the Kummer classes of the chosen equations, the Gysin projection formula and the residue map. Once the coefficient sheaf extends from X, it is constant after strict localization, and the induction gives the exterior algebra on the degree-one Kummer classes, supported on the appropriate intersections. This is the precise context in which the principal-divisor restriction step is used.

The degree-one calculation does not need the higher purity theorem: a regular local A is factorial, and `A[1/(a1⋯ar)]` remains factorial. Its units are a unit of A times a product of integer powers of the parameters, and its Picard group is zero. Hensel's lemma makes the units of A n-divisible for n invertible. The Kummer sequence therefore gives the r degree-one generators. Higher exterior powers require the purity/residue argument. The live complement identity is `X−⋃Di=⋂(X−Di)`; the cancelled union of opens is not restored. The equivalence between the divisor-support formulation and the Rj* formulation follows directly from `i_*Ri!Λ→Λ→Rj_*Λ`, using the degree-two concentration; it also explains the degree and twist alarms in C824--829.

The broader interpretation with an arbitrary locally constant F on a partially punctured open is false. Let k be algebraically closed of characteristic p, let `X=Spec k[[x,y]]`, `U′=D(x)`, and `D′=V(y)∩U′`. The Artin--Schreier cover

\[
q:T\to U',\qquad z^p-z=y/x
\]

is finite étale and connected. Indeed, in the x-adic valuation of the fraction field, `y/x` has valuation−1. If b has negative valuation, `b^p−b` has valuation divisible by p; if it has nonnegative valuation, so does `b^p−b`. Hence the equation has no rational root, and an Artin--Schreier polynomial of prime degree with no root is irreducible. On D′ the equation becomes `z^p−z=0` and splits into p copies. For `F=q_*Z/ℓ`, ℓ≠p,

\[
H^0(U',F)=\mathbf Z/\ell,
\qquad H^0(D',F)=(\mathbf Z/\ell)^p.
\]

Restriction is diagonal, not an isomorphism. C833 therefore leaves the carried coefficient convention as a reading problem: the inherited “F extends to X” interpretation repairs the use; it is not decided by claiming to have read the absent ink.

For the explicitly admitted cup/residue square, fix the boundary normalization `res κ(t)=1`. The connecting map is a graded derivation. With a left factor α extending across the divisor, `res(α∪κ(t))=(−1)^degα α|D`; writing the Kummer factor first yields the equivalent convention without this displayed sign. Projection/Gysin compatibility follows by applying the module structure to the localization triangle. Riou XVI3.4.8 and§4 explicitly compare conventions, including a negative sign for a root-torsor convention. The manuscript's unsigned square cannot be checked by silently mixing those choices.

If P is pro-p and M is a discrete continuous ℓ-primary torsion P-module with ℓ≠p, invariants are exact. To lift an invariant element through a surjection, start with any lift. Its P-orbit is finite by continuity. The finite subgroup quotient acting on that orbit is a p-group; averaging over it and dividing by its order gives an invariant lift. This proves exactness, and higher continuous P-cohomology vanishes. For a continuous representation of P on a finite free `Zℓ`-module, reduction moduloℓ has finite image, and its congruence kernel is pro-ℓ. A group that is both pro-p and pro-ℓ is trivial, so the P-image is finite. The two assertions have different coefficient hypotheses and are not conflated.

Finally, if `0=F_{−1}⊂F_0⊂⋯⊂F_i=M` is stable under g and g acts trivially on each quotient, then `(g−1)F_j⊂F_{j−1}`. Iterating gives `(g−1)^{i+1}M=0`. The first-quadrant total-degree-i spectral sequence has at most i+1 such pieces. This proves the stated exponent from that filtration; it neither splits the filtration nor proves integral saturation. A full Jordan block shows that the length i+1 cannot be reduced merely from these hypotheses.

## 13. The published nilpotence bound and its original printed error

The original SGA7I3.4 on printedp12/PDF17 was inspected as an image. It really prints `q′=min(q,maximum number of crossing components)` in the exponent. In degree0 this would give exponent0, so it cannot be the intended general formula on nonzero cohomology. The discrepancy is in the published original, not only in a recent digital retyping.

Illusie2021 Theorem2.3 states the general geometric monodromy exponent i+1. In the log-smooth normal-crossing setting, Illusie2002 Corollary8.4.4 and formula(8.4.4.1), printedp311, give the sharper exponent `min(q+1,r)`, where r is the supremum of the ranks of the characteristic group `M_X^gp/O_X^*`. For a simple normal-crossing divisor this is the maximum number of local branches. An appropriate common multiple of the finite tame permutation orders is used before taking the unipotent operator. The manuscript's open-subgroup formulation and this finite-order removal are compatible.

The filtration argument in §12 independently proves the q+1 part. Neither that argument nor the primary-source match settles the extra integral “pure/saturated” qualifier in C819. The incomplete Griffiths reference likewise remains class F. A general later theorem with a matching conclusion does not identify a particular unnamed source.

## 14. Root covers, exterior cohomology and the multiplicity lattice

Let A be a noetherian strictly henselian regular local ring, let `a1,…,ar` be part of a regular system of parameters and let m be invertible in A. In

\[
B=A[T_1,\ldots,T_r]/(T_1^m-a_1,\ldots,T_r^m-a_r)
\]

the monomials with each exponent less than m form an A-basis, so the rank is `m^r`. The closed fibre has one point, so B is local and henselian with the same separably closed residue field. Its maximal ideal is generated by the `T_i` and the remaining parameters of A; its dimension remains `dim A`. Thus B is regular and a domain. On the complement of the parameters, the cover is finite étale with independently rotating roots, so its group is `μ_m^r`. This proves the missing-power repair and connectedness, rather than inferring them merely from notation.

Kummer classes of the original parameters pull back to m times those of the roots. Exterior multiplication gives `m^q` in degreeq. At fixed `Λ=Z/n`, a further root cover whose root degree is divisible by n kills each positive-degree class. Taking all prime-to-p roots, continuity of étale cohomology under affine inverse limits gives `H^0(U∞,Λ)=Λ` and `H^q(U∞,Λ)=0` for q>0. This acyclicity statement concerns these constant prime-to-p torsion coefficients. It does not assert p-primary acyclicity or acyclicity of each finite stage.

For a closed subgroup H of the abelian Kummer lattice G, descent along the pro-torsor identifies cohomology of `U∞/H` with continuous group cohomology of H. The associated Γ-cover is described by continuous induction from `im(G→Γ)`. On an infinite profinite coset space, its degree-zero functions are locally constant functions; taking all set-theoretic functions instead would be wrong. The action of G/H on H-cohomology is by conjugation, hence trivial here because G is abelian. If imG is normal, the quotient Γ/imG acts faithfully on its locally constant functions whenever Λ is nonzero: distinct points of a profinite space are separated by a clopen subset, whose characteristic function is moved. For n=1 all these coefficient modules vanish and the kernel assertion fails. This is the explicit edge case in C842.

For a fixed ℓ≠p, a closed subgroup of `Zℓ^r` is a `Zℓ`-submodule because closure makes the action of ℓ-adic scalar limits available. Since `Zℓ` is a discrete valuation ring, it is free of rank s≤r. In the completed group algebra, the regular sequence given by the s elements `γ_i−1` supplies the Koszul resolution of the trivial module. Applying Hom to trivial finite ℓ-primary coefficients makes its differentials zero. The induced cup structure is the exterior algebra on continuous Homs, including when ℓ=2; ordinary graded commutativity alone would not establish the square-zero assertion at2. Other prime factors have exact invariants. This supplies the cohomology formula used in C844.

If `t=∏a_i^{m_i}`, chosen compatible roots give the character map

\[
\varphi:G\longrightarrow\Gamma,\qquad
(\lambda_i)\longmapsto\sum_i m_i\lambda_i.
\]

Bézout's identity identifies its image with `dΓ`, `d=gcd(m_i)`. When some multiplicity is positive, the index is the prime-to-p part of d. With all multiplicities zero the image is0 and has infinite index; the finite-index language then has no application. For a global divisor, use the lcm M of its **positive vertical** multiplicities. Every local gcd divides M, so MΓ acts trivially on the local tame sheaves. Horizontal multiplicities are0 and must be omitted from the lcm. The checks in the executable file verify these formulas in several finite quotients; the Bézout argument proves the general claim.

## 15. Resolution, constructibility and wild tameness have different fates

The manuscript's resolution argument is mathematically intelligible: after a proper modification with regular normal-crossing boundary, the explicit root calculation gives constructible tame sheaves; proper direct image and the Leray filtration return constructibility on the original space. A single subgroup chosen from the resolved model's multiplicities works for every coefficient exponent. At total degreeq the live proof uses q+1 pieces, not the abandoned quadratic count. The cancelled sum `Σ_{i=0}^q(i+1)` equals `(q+1)(q+2)/2`; its printed `q(q+1)/2` is arithmetically different, but neither is needed by the surviving argument.

Original SGA7 XIII2.3.1, printed110/PDF116, gives the resolution-based torsion finiteness theorem in equal characteristic zero. Deligne's SGA4½ Finitude3.2, printed244/PDF248, explicitly improves that theorem and XIII2.4.2 and proves constructibility over the strictly henselian trait in its coefficient setting. Both original pages were visually checked. Adic systems require the compatible system formalism; this torsion theorem alone is not cited as a complete proof of every adic assertion. Similarly, original XIII2.1.12 gives completion invariance with an excellent trait, and equal-characteristic-zero base-change invariance. The manuscript's broader sentence that passage to completion makes every excellence issue harmless is not certified from that result.

The geometric hope of arbitrary-characteristic resolution remains a separate proposition. The search recorded Temkin2024 and its explicit local-uniformization context; it did not turn alterations into an isomorphic-over-U regular modification. The source comparison for C850 is therefore limited and current-status qualified.

The wild-inertia question has a much more precise later answer. The checked Rapoport--Zink, Nakayama and Illusie sources apply to their normal-crossing/log-smooth settings, with the coefficient prime invertible. Illusie2002 Corollary8.4.3 includes the open stratum of trivial log structure in a proper log-smooth fs scheme; it is not restricted to vertical log structures. This matters when the draft has horizontal boundary. Triviality of wild inertia on the sheaves passes to proper cohomology: apply the exact invariant functor of §12 to the relevant filtration, or use its exactness on the equivariant derived construction. A finite p-group cannot act nontrivially through a unipotent ℓ-primary extension when p≠ℓ. This explains the global conclusion without mistaking trivial wild action for trivial tame monodromy.

## 16. Affine dimension bounds and the high specialization range

For the first bound in C859, shrink around x to exclude components not meeting x. Each pointed affine étale neighbourhood then has generic fibre of dimension at most n_x; an affine open U retains affineness after these changes. Affine Lefschetz over the separably closed generic field bounds its cohomology by n_x. Filtered continuity gives the same bound on the strict localization. For C860, replace X by the schematic closure of its reduced generic fibre and use proper base change for that closed immersion; the generic sheaf is unchanged, and the nearby-cycle complex on X is the pushforward from the closure. Flatness over the trait and the local dimension formula give the asserted comparison with special-fibre dimensions. This reduction does not identify the discarded vertical components with a nonzero nearby-cycle contribution.

For the refined bound, take r residue functions forming a transcendence basis of k(x)/k. The resulting map to `A^r_S` sends x to the generic point of its special fibre, and its strict localization S1 is a trait. At x the relative fibre dimension is `n−r`; upper semicontinuity permits shrinking so that all relevant fibres have at most that dimension. Apply the first affine bound over S1, then the geometric-generic smooth-base-change acyclicity to descend the bound to the original strict-local geometric fibre. This is the proof structure read in original SGA7 I4.2; it is not a claim that the cancelled finite Noether-normalization attempt was completed.

The affine stalk calculation uses the **geometric** generic fibre of the strict localization. The literal ordinary generic field cannot be substituted. Already with relative dimension0, a strict henselian DVR with uniformizer π has a nonzero class of π in `K*/K*ℓ=H^1(K,μℓ)`: valuation moduloℓ detects it. Thus its absolute Galois group is not pro-p. Original SGA7 I4.2 proof(a), printedp14, retains the geometric generic fibre in the transcendence-basis reduction. This verifies the lost-bar reading alarm C862.

With `n=dim Xη`, a pointwise bound on the dimension of the closure of x gives, for q≥1,

\[
\dim\operatorname{Supp}\Phi_{\mathrm{man}}^q
 \le\min(d,n+1-q),
\]

where d bounds the nonsmooth special locus. A constructible sheaf supported in dimension e over a separably closed field has cohomology only through degree2e. Hence a possibly nonzero term has `p≤2min(d,n+1−q)`. If `q≤n+1−d`, then `p+q≤2d+q≤n+d+1`. If `q≥n+1−d`, then `p+q≤2n+2−q≤n+d+1`. This proves the optimization, and the executable enumeration checks its boundary. The q=0 term must separately vanish, as in the flat generically dense setting, or satisfy `2d≤n+d+1`; the latter is precisely `d≤n+1`. It is not automatically equivalent to a bound on the whole special-fibre dimension.

Let `B=n+d+1`. If `Φman^i=0` for i>B, the specialization sequence gives an isomorphism in degrees i>B and a surjection at i=B. Since inertia is trivial on special-fibre cohomology, it is trivial on generic cohomology in degrees i≥B. If the geometric generic fibre is also smooth proper and pure of dimensionn, Poincaré duality transfers this to `i≤n−d−1`; the tame Tate twist is trivial over the strict henselian base with prime-to-p roots of unity. Thus nontrivial monodromy can occur only in `[n−d,n+d]`. The extra smoothness and pure-dimensionality are necessary to this particular duality argument.

For the hyperplane alternative, d+1 sufficiently general hyperplanes avoid the d-dimensional bad locus. The resulting smooth relative complete intersection has generic dimension `n−d−1` and codimension `c=d+1` in X. Gysin shifts the source degree by2c and twists by c. Weak Lefschetz plus duality makes the map surjective from degree `i≥n−d−1`, hence onto generic cohomology from degree `i+2c≥n+d+1`, agreeing with the preceding boundary. A codimension d label would be inconsistent with both calculations. Existence of the indicated section uses the stated projective/Bertini situation, not an arbitrary affine family.

## 17. A negative answer to the general infinite-root dimension question

The exact primary input is Orgogozo, *Dimension cohomologique : raffinements et compléments*, Astérisque363--364 (2014), ExposéXVIII_B §§2.1--2.4. For any chosen invertible prime ℓ, it constructs a **regular noetherian strictly local** ring A of dimension2 and a nonzero nonunit F with

\[
H^3(U,\mathbf Z/\ell)\ne0,\qquad U=\operatorname{Spec}A[1/F].
\]

The construction is nonexcellent. Its defining divisor becomes an ℓ-fold regular divisor in the completion, explaining the vanishing Gysin multiplier in the source's proof. These are the facts imported from that primary example. No complete copy of its construction is included in this dossier.

The following tower argument is our deduction. Since A is strictly local and ℓ is invertible, all roots of unity of order prime to its residue characteristic exponent p are already present in A. For each such m,

\[
U_m=\operatorname{Spec}A[1/F,T]/(T^m-F)
\]

is a finite étale μ_m-torsor over U: T is invertible and the derivative `mT^{m−1}` is invertible. Torsor status does not require connectedness. The compatible inverse limit `U∞=lim U_m` is affine and is a pro-étale torsor for `Γ=∏_{q≠p}Z_q(1)`. Its ℓ-cohomological dimension as a profinite group is1. Continuous Cartan--Leray gives

\[
E_2^{a,b}=H^a_{\mathrm{cont}}\!left(\Gamma,
H^b(U_\infty,\mathbf Z/\ell)\right)
\Longrightarrow H^{a+b}(U,\mathbf Z/\ell).
\]

One obtains this from the finite étale torsor descent sequences and filtered continuity; the cohomology modules carry their discrete continuous Γ-action. Columns a>1 vanish. If the manuscript's proposed bound `cdℓ U∞≤dim A−1=1` were true, rows b>1 would vanish as well, leaving no term in total degree3. This contradicts the nonzero primary example. Therefore `cdℓ U∞≥2`. In fact at least one of `H^2(U∞,Z/ℓ)` or `H^3(U∞,Z/ℓ)` must be nonzero, by the same two-column argument.

This resolves the question negatively in its written arbitrary-noetherian generality. It does not refute the earlier regular-parameter normal-crossing calculation in §14: Orgogozo's F does not give that setup. It also does not assert that every quasi-excellent refinement is open or false. The accompanying Illusie XVIII_App theorem and its quasi-excellent contrast are recorded only at their verified scope.

## 18. Rectified depth, the low boundary and the pinching example

The manuscript's rectified depth adds the dimension of the point's closure **in the relevant fibre** to its local depth. Consequently a single global lower bound has to hold at every point. The SGA1 XIV references on these leaves point mathematically to SGA2 XIV, as the original SGA7 I4.5 cross-references confirm. The global Lefschetz application supplies isomorphisms below `a=m−d−1` and injections at a for restriction to the smooth complete intersection.

The specialization square then has bottom horizontal arrow an isomorphism. Below a both vertical arrows are isomorphisms, so the upper specialization is an isomorphism. At a the left vertical arrow is injective; if an element maps to zero under upper specialization, its image below is zero, so it is zero. Thus upper specialization is injective at a. The cone sequence in §10 gives `Φman^i=0` for i≤a. The boundary is an injection, not an unexplained surjection.

For the lci improvement, flatness and finite presentation let the lci condition of the special fibre lift to a neighbourhood of that fibre. In a proper family over a trait the closed complement of this neighbourhood has closed image; if it misses the closed point, it is empty. Thus the relevant relative lci condition is global in the stated proper setup. Illusie2003 §§2.6--2.10 supplies the general-trait depth and perversity theorem. With relative dimensionn, usual `RΦΛ[n]` is perverse. A perverse complex supported in dimension≤d has ordinary cohomology sheaves in degrees≥−d, so its global cohomology is also zero below−d. It follows that usual vanishing cycles vanish in degrees `<n−d`, hence the manuscript complex vanishes for `i≤n−d`. This nonisolated-support deduction is ours from the precise perverse statement; isolated support is the explicitly cited Corollary2.10 case.

Here is a concrete model for the weaker-depth counterexample. Let R be a strict henselian DVR with residue field k and parameter π. Locally the pinching ring is

\[
B=R[x]\times_kR[y]
 \cong R[X,Y,T]/(XY,TY,(T-\pi)X,T(T-\pi)),
\]

where `X=(x,0)`, `Y=(0,y)`, `T=(π,0)`. The embedding in the product proves R-torsion-freeness, hence flatness over the DVR. In the generic fibre `T/π` is an idempotent and `B_K=K[x]×K[y]`. In the closed fibre

\[
B/\pi B=k[X,Y,T]/(XY,TX,TY,T^2).
\]

Its underlying curve has two branches meeting at one point, and T is a nonzero square-zero element annihilated by the maximal ideal there. The embedded structure is essential: the closed fibre is not lci.

A proper version is obtained from the graded fibre product
`R[u1,v1]×_{k[z]}R[u2,v2]`, mapping each ui to z and vi to0, and taking Proj. Its degree-zero ring is finite over R and its graded ring is generated by finitely many degree-one elements over that ring; hence it is projective over R. Its standard common-u patch is the displayed B. Its finite map from the disjoint union of two copies of `P¹_R` glues only the chosen special points. Therefore the generic fibre has two connected components and the special fibre is connected. Nilpotents do not change étale cohomology, so `H0(Xs,Λ)=Λ` maps diagonally to `H0(Xbarη,Λ)=Λ²`. The cokernel is Λ, and the cone sequence shows `Φman¹≠0`.

For the rectified-depth≥1 assertion on the fibres, at their generic points the closure term is1 and local depth is nonnegative. At a closed point of a curve with no zero-dimensional irreducible component, a section of the constant sheaf supported only at that point is zero, so local étale depth is at least1. The connected nodal underlying special curve satisfies this, while the embedded nilpotent does not alter its étale topos. Thus the example satisfies the weak depth condition without becoming a counterexample to the flat-lci improvement.

## 19. Two localization triangles and a missing uniform premise

Let X′ be the strict localization at the special geometric point x, let `V=X′−{x}`, and base change to the integral closure Sbar of S in Kbar. The special base change is purely inseparable on residue fields and induces an equivalent étale topos; it is not necessarily a scheme isomorphism. Its cohomology has trivial inertia. Inertia acts continuously on the equivariant complexes; the manuscript's admissible modules are interpreted with this continuity condition.

For the generic open `j:Vbarη→Vbar` and special closed `i:Vs→Vbar`, triangle A is

\[
R\Gamma(V_s,\Phi_{\mathrm{man}})\to
R\Gamma(\bar V,\Lambda)\to
R\Gamma(V_{\bar\eta},\Lambda)\to.
\]

It comes from the support/localization triangle `i_*Ri!Λ→Λ→Rj_*Λ→`. To make its first term vanish below m, it suffices that `H^q(Φman)|Vs=0` for q<m. The first-quadrant hypercohomology sequence then has no term of total degree<m. The long exact sequence gives an isomorphism `H^i(Vbar)→H^i(Vbarη)` for `i<m−1` and an injection at `i=m−1` (also, trivially, in the lower isomorphism range).

Vanishing of a stalk at the **omitted** x is not that hypothesis. A simple sheaf countermodel makes the logical point: on a trait, the extension by zero from the generic open of a nonzero constant sheaf has zero closed stalk but nonzero cohomology on the puncture. This is a countermodel to the inference about sheaves, not a claim that every such sheaf is realized by nearby cycles. Original SGA7 I4.5 proof(1) explicitly imposes the needed condition at the generizations in the punctured fibre. C879 accordingly certifies the repaired statement and labels the literal inference false.

Support at x must be taken inside Xbar. The punctured Vbar omits x, so `H_x^i(Vbar,Λ)` would vanish by definition. The strict-local ambient cohomology and its localization sequence give reduced `H^{i−1}(Vbar,Λ)` for the actual support group; in low degree the augmentation `Λ→H0(Vbar)` must be retained. Comparing this with §10 gives the claimed shifted local comparison in its proper low-degree range. If x is an isolated nonsmooth point along the special fibre, the support complex vanishes at every point of Vs, and triangle A is an equivariant quasi-isomorphism on its latter two terms. Merely saying x is nonsmooth gives no such conclusion.

Triangle B instead comes from the other localization sequence,

\[
j_!\Lambda\longrightarrow\Lambda\longrightarrow i_*\Lambda\longrightarrow,
\]

and after global sections reads

\[
R\Gamma(\bar V,j_!\Lambda)\to R\Gamma(\bar V,\Lambda)
\to R\Gamma(V_s,\Lambda)^{\mathrm{triv}}\to.
\]

Its first term is extension-by-zero cohomology, not special-fibre support cohomology. Keeping A and B distinct is necessary before any duality or depth comparison. These are exact derived constructions; the executable checks concern the degree ranges only.

## 20. Properness belongs to the global specialization comparison

The local sheaf triangle

\[
\Phi_{\mathrm{man}}\longrightarrow\Lambda_{X_s}\longrightarrow R\Psi\Lambda
\longrightarrow\Phi_{\mathrm{man}}[1]
\]

exists without properness. The hypercohomology spectral sequence on the special fibre likewise exists without properness. To identify its global target with the cone comparing the cohomology of the entire special and geometric generic fibres, the construction on these pages uses **X/S proper** and proper base change. An open generic stratum U is allowed inside this proper X; this does not make the ambient properness dispensable.

The failure without that hypothesis is explicit. Let S be a strictly henselian trait with algebraically closed residue field k, let Λ=Z/ℓ with ℓ invertible on S, and remove from P¹_S a single k-point of its closed fibre. The resulting X→S is smooth, being an open subscheme of a smooth S-scheme. Consequently all its local vanishing cycles are zero. Its special fibre is A¹_k and its geometric generic fibre is P¹_Kbar. The two H² groups are respectively zero and Λ(−1), so the unrestricted global comparison would be false. No assertion about failure of local smooth acyclicity is involved.

This checks the carried properness in C-SA13-802,804,809,812,815. Finite support still collapses the hypercohomology spectral sequence without properness; properness is needed only to call the resulting direct sum the defect of the whole-fibre specialization map. The local-versus-global distinction is consistent with the nearby-cycle definitions and proper comparison in P4_SGA7IIntro §2 and P4_Illusie2021 §§1.1–1.2. This paragraph is an independent mathematical check prompted by the cross-shard audit, not an additional claim of a newly discovered manuscript error.
