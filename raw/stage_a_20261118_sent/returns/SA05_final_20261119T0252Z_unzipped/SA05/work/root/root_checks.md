# Targeted mathematical checks for the root scope

Run: GPT-6 Astra Pro, current run, 19 November 2026. This document records actual arguments, not a claim that every cited paper was independently reproved. The finite calculations are in `programs/root_certificates.py` and its JSON output. A finite sample is labelled as such; the general argument, where supplied, is written below. Manuscript locators and the distinction between live and deleted text are in the item and claim tables.

## 1. Categories, fibre functors and central weights

**Finite-length decomposition and the unit.** In a semisimple finite-length category, write an object as a finite direct sum of simple objects with multiplicities. If each simple has a well-defined least nonnegative level, summing the isotypic components of each level is a canonical decomposition. This proves the formal decomposition claimed in SA05-C6, conditional on the existence and definition of the level. It does not construct those definitions. Likewise the Grothendieck group is free on the simple classes. The condition End(1)=k makes the tensor unit simple in this setting; it does not make the associated group connected. Rep_k(C2), in characteristic zero, is an explicit counterexample to that stronger inference.

**Faithful exact realization.** For an actual morphism f, exactness identifies the realization of ker(f) and coker(f) with the corresponding kernel and cokernel. Faithfulness detects the zero object: if its identity realizes as zero, its identity is zero. Hence an exact faithful functor reflects isomorphisms. There is no argument here for lifting a morphism in the target; that is fullness. This distinction is decisive for the projectors, inverse Lefschetz operators and correspondence maps in these pages.

**Ordinary versus super fibre functors.** The odd one-dimensional super vector space has categorical dimension −1 under the Koszul symmetry. A symmetric tensor functor to ordinary finite-dimensional vector spaces would preserve this trace, although the ordinary target dimension is a nonnegative integer. Thus rigidity, abelianness and End(1)=k do not by themselves give an ordinary fibre functor. Deligne1990 Theorem7.1 adds the appropriate characteristic-zero dimension/exterior-power criterion. Its theorem number is7.1, not8.17. For a finite-type Tannakian gerbe, a finite-type affine atlas over a field has a closed point with finite residue extension; this gives the intended finite-extension neutralization only after the Tannakian/finite-type premises are in place.

**Serre’s quaternion obstruction.** Let E be supersingular over an algebraic closure of a finite field. Its rational geometric endomorphism algebra is a quaternion division algebra D of dimension4 over Q. A faithful rational realization of h1(E) of dimension2 would inject D into End_Q(Q²)=M2(Q). An injective map between these two4-dimensional Q-algebras is an isomorphism, which is impossible because M2(Q) has zero divisors while D is a division algebra. This checks the stated obstruction, without denying nonneutral Tannakian descriptions or fibre functors over other coefficient fields. Relevant source: R-Milne1994.

**Central weight versus Lefschetz grading.** Put H=diag(1,−1) and L=E12. Direct multiplication gives [H,L]=2L. A central cocharacter has differential commuting with every group Lie element, so its differential cannot be this nonzero sl2 Cartan when L lies in the same Lie algebra. The calculation does not deny a Lefschetz action on cohomology; it denies the proposed identification of that action’s Cartan with the central weight operator. The program prints the full matrices.

**Invariant form versus positive form.** For the trivial group on R², the form diag(1,−1) is invariant and nondegenerate, but takes opposite signs on the two basis vectors. This supplies the exact missing positivity condition. No Hodge polarization is contradicted.

**Trace and characteristic coefficients.** In a rigid symmetric tensor category, a trace is the composite of coevaluation, the morphism tensored with the dual identity, symmetry and evaluation. A tensor realization preserving these structures preserves the trace. If End(1)=Q, the trace lies in Q. Characteristic coefficients can be expressed by exterior-power traces; in characteristic zero Newton identities give the equivalent power-trace expression. This is conditional on an actually constructed category and correctly typed contraction. It does not construct the correspondences that an l-adic calculation might suggest.

**Arithmetic quotient and kernels.** The formal exact sequence in DM6.23/Kahn5.10 has the group of the geometrically extended category as kernel. Calling it the identity component requires connectedness of that geometric group. A section on Q_l-valued points is a continuous representation with a compatibility property, not automatically a Q-morphism of affine group schemes. These are statement checks against opened theorem text; no full independent proof of Kahn’s descent theorem is claimed.

## 2. Tate bookkeeping, Grothendieck groups and scissors

The convention fixed by the pages is wt(Q(-1))=2, hence wt(M(r))=wt(M)−2r. A pure effective weight-i object becomes weight n after twist r=(i−n)/2, provided that integer exists. Integral Tate twists preserve weight parity. Thus an odd-weight h1 cannot become weight zero by such a twist. The program separately records the unit, Q(-1) and h1(E).

The early D filtration is stated to be stable under Tate twists, so both1 and Q(-1) have D-level0. The later generating-dimension filtration is a different construction: the fact that P1 has dimension1 is not a contradiction to early D-level0. The dossier never identifies these filtrations solely because they share the letterD.

For K0 of a finite-length category, a simple object gives an independent basis element. If the Tate object is invertible, tensoring by it permutes this basis and cannot be a zero divisor. If only an effective subcategory is used, injectivity needs the stated full-faithfulness/cancellation hypothesis. This argument does not apply to the Lefschetz class in K0(Var), which is another ring.

The literal primitive-zero subtraction inspected in the source removes every candidate from itself. The finite set calculation confirms the empty result at the boundary. A meaningful primitive rule retaining the unit must have an exception or altered index; choosing that repair is not a transcription correction made here. Similarly, an additive basis by Tate strings does not specify products of primitive constituents: multiplication structure constants remain necessary.

For compact Euler characteristic, the basic checks are χc(P1)=1+L and χc(A1)=L, with additivity for P1=A1⊔point. For a smooth proper genus-g curve the virtual class is1−h1(C)+L; changing from cohomological degree j to weight i=j+ρ multiplies an alternating sum indexed by i by(−1)^ρ. Gillet–Soulé’s characteristic-zero theorem gives a precise target category and the scissors/product identities. It is not an isomorphism from varieties to their motivic classes.

For a regular immersion of codimension d, the formula i!1=1(-d)[-2d] has both a Tate twist and a cohomological shift. Omitting the shift fails already for a closed point in a smooth curve: local cohomology is in degree2. The separate arithmetic duality shift2n+1 is not a correction to geometric purity; it includes a one-dimensional arithmetic direction in its own theory.

## 3. Birational and reconstruction obstructions

**A section is nondominant.** Take a positive-genus smooth projective curve C over an algebraically closed characteristic-zero field, and a rational point of P1. The section s:C→C×P1 is nondominant, while projection p satisfies p∘s=id_C. Any functorial invariant with γ1(C)≠0 therefore cannot send every nondominant rational map to zero: the composite induced by p and s would be zero and identity simultaneously. This checks all relevant dimensions and does not rely on a numerical sample. It refutes the unrestricted sentence, not a possible more narrowly graded statement.

**Field maps into polynomial rings: a conditional notation alarm.** If R,R′ are fields and a unital ring map R→R′[t1,…,tn] is given with a literal polynomial-ring target, every nonzero element of R and its inverse map to mutually inverse polynomials. The only units of a polynomial ring over a field are nonzero constants. Hence the image lies in R′. However, the manuscript says “extension transcendante pure” at early lines1763–1766 and uses L0[t] for a field of transcendence degree n at1799–1801. Its brackets can therefore denote a rational-function field. The units argument does not refute that intended stabilization and is retained only to prevent a modern literal-polynomial reading. The curve counterexample below applies to the intended rational-function interpretation. Also mutual field embeddings are not, without more data, a stable-birational isomorphism theorem.

**Howe’s genus-two example.** R-Howe2005 Theorem1 gives

\[
(t+1)y^2=(2x^2-t)\bigl(4t^2x^4+4(t^2+t+1)x^2+1\bigr)
\]

for the curves C(t), with t(t²−1)(t²+1)≠0 and characteristic≠2. At t=2 over C the product is30, so all exclusions hold and none of the characteristic11 exceptions applies. The theorem gives geometrically nonisomorphic C(2),C(−2) with isomorphic unpolarized Jacobians. If a dominant rational map from C(−2)×P^m to C(2) existed, restricting to a general rational fibre would give a constant map to the positive-genus target; hence it factors through C(−2). Resolve the rational map between the smooth projective curves. Riemann–Hurwitz is2=2d+R with d≥1,R≥0, forcing d=1 and R=0. This would be an isomorphism, contradiction. The unpolarized adjective is essential; no contradiction with Torelli is claimed. The program checks the elementary degree inequality only; Howe supplies the existence theorem.

**Enriques surface.** Over C, a smooth projective Enriques surface has b1=b3=0,b2=10 and p_g=0. The exponential sequence/Lefschetz(1,1) theorem makes H² rationally algebraic. Choose a rational divisor basis and its inverse intersection matrix. The associated divisor correspondences, together with the degree-zero/top projectors, give its rational homological motive as1⊕Q(-1)^10⊕Q(-2). Thus the positive non-Tate primitive pieces vanish in this interpretation. Its canonical class has order2 and its Kodaira dimension is0. A dominant rational map from P² would, after resolution, make its nonzero pluricanonical sections inject into those of a rational surface, which have none. Hence it is not unirational in characteristic zero. This checks the chosen surface, coefficient field, equivalence relation and birational property; it says nothing comparable about its integral or full Chow motive. R-Dolgachev2016 supplies the surface facts.

**The author’s supersingular product.** For a supersingular elliptic E over an algebraically closed field, A=E×E is superspecial, NS(A) has rank6 and b2(A)=6. Thus its degree-two rational realization is algebraic. But b1(A)=4, so this is not an example in which every positive primitive invariant vanishes. Abelian varieties contain no rational curves (R-MilneAV2008 I.3.9); a ruled surface has a dominating family of rational curves. Thus A is not ruled. The precise graded-quotient obstruction must be distinguished from the Enriques all-Tate example and from Larsen–Lunts’s characteristic-zero stable-birational quotient.

## 4. Frobenius, weights and two explicit geometric counterexamples

**Envelopes and Lie algebras.** The standard SL2 representation is irreducible; explicitly the elementary upper/lower unipotents, their products and the identity span all four matrix units. GL2 contains SL2 and has the same full associative envelope. Solving commutation with the two elementary nilpotent matrices gives only scalars in both cases. Therefore neither the associative envelope nor its commutant identifies the subgroup.

For a compact l-adic analytic group acting continuously on a finite-dimensional space, a vector fixed by the analytic Lie algebra is fixed by a sufficiently small exponential neighbourhood, hence by an open subgroup. The converse follows by differentiation. Finite field extensions correspond to open subgroups of the Galois group, proving the finite-extension invariant assertion. This proof concerns the analytic Lie algebra.

Consider a Frobenius with polynomial T²−T+5, rootsα,β. Its discriminant is−19, αβ=5, and α+β=1. In the quadratic field the ideals(α) and(β) are distinct primes over5: reducing the polynomial modulo5 gives distinct roots0 and1. A multiplicative relationα^aβ^b=1 forces a=b=0 by valuations at these primes. Hence the algebraic torus generated by this Frobenius has dimension2. Its compact procyclic l-adic closure, for l≠5, has analytic dimension1 after passage to a torsion-free open subgroup; it is infinite because the eigenvalues are not roots of unity. This is the exact distinction between analytic and algebraic Lie targets, not a numerical logarithm calculation. The program checks the companion matrix, polynomial, trace and discriminant.

**Roots of unity.** If an algebraic integer and all its conjugates have absolute value1, the coefficients of the minimal polynomials of all its positive powers are integers bounded in terms of the fixed degree. Only finitely many such polynomials and roots occur, so two powers coincide and the number is a root of unity. This does not remove unipotent monodromy: matrices1+nN withN²=0 are an infinite subgroup with all eigenvalues1. To infer a finite semisimple image from arithmetic Frobenius data one also needs density and a uniform order bound. The manuscript’s separate semisimplicity/Tate input must not be lost.

**P1.** The literal scan51 claim Hc^i(X)∈weight≤dimX fails for X=P1,i=2: the group is Q_l(-1), Frobenius q and weight2, while dimX=1. P1 is smooth, proper, nonempty and geometrically connected. No singularity, nonproperness or coefficient variation causes this failure.

**Legendre family.** Let U=A1−{0,1} over F5 and f:E→U be y²=x(x−1)(x−λ), with the smooth projective completion of each fibre. This is a smooth proper family of elliptic curves; V=R1f_*Q_l is lisse, rank2, pure of weight1 for l≠2,5. Its geometric monodromy has no invariant vector. The exact all-extension trace formula in Stacks tag03VA gives Hc0=Hc2=0 and

\[
\operatorname{Tr}(F^n\mid H_c^1(U_{\bar{\mathbf F}_5},V))
 =1+(-1)^{(5^n-1)/2}=2\quad(n\geq1).
\]

Consequently the semisimplified eigenvalue multiset on Hc1 is{1,1}. This conclusion follows from all n and finite-dimensionality, not from the five numerical sample fields in the program. The elliptic polarization gives V^∨≃V(1). Poincaré duality on the smooth curve gives

\[
H^1(U_{\bar{\mathbf F}_5},V)
 \simeq H_c^1(U_{\bar{\mathbf F}_5},V^\vee)^\vee(-1).
\]

Twist(1), dual, and twist(-1) turn the eigenvalue1 into5². Thus H1 has weight4, exceeding the proposed sharp constant-coefficient upper bound after the naive shift byρ=1. For V(2), the coefficient weight is−3 and the eigenvalues on geometric H1 are1. Since H0 is zero, Hochschild–Serre identifies arithmetic H1 with the nonzero invariant subspace. Even without assuming semisimplicity of this H1, an operator all of whose eigenvalues are1 has a nonzero kernel ofF−1. This refutes the proposed forbidden coefficient-weight window. The program verifies the point-count identity in five prime fields as an arithmetic sanity check only.

The displayed i=1 interval[-2,1] is not itself a contradiction: the preceding inequalities imply[-2,0], a subset of[-2,1]. The alarm is about the intended sharp endpoint, not logical entailment. Separately, a pure weight-zero space can have roots of unity other than1, so weight zero is not the same as an invariant subspace.

**Proper singular SNC example.** Let D⊂P³/Fq be the union of its four coordinate planes, and X=D×P¹. Every stratum is split over Fq: fourP² components, sixP¹ double intersections, four point triple intersections, and no quadruple intersection. The cohomological descent spectral sequence has rows

| Stratum degree | Dimensions in Čech degrees0,1,2 | Differential ranks | Surviving Čech cohomology |
|---|---|---|---|
|0|4,6,4|3,3|dimensions1 in degree0 and1 in degree2|
|2|4,6,0|3,0|dimensions1 in degree0 and3 in degree1|
|4|4,0,0|0,0|dimension4 in degree0|

The program constructs the signed incidence matrices and checks their products and ranks. Frobenius isq^(j/2) in rowj. Higher differentials vanish by bidegree or distinct weights. Therefore H²(D) has one weight-zero and one weight-two class, H³(D)=Q_l(-1)^3, H⁴(D)=Q_l(-2)^4. Künneth gives H³(X)=Q_l(-1)^3 and H⁴(X)=Q_l(-1)⊕Q_l(-2)^5. After twist(1), the arithmetic Hochschild–Serre sequence contributes three coinvariants fromH³ and one invariant fromH⁴, so dimH⁴(X,Q_l(1))=4. X is proper of finite type and singular, with l invertible. This refutes the unrestricted proper-scheme question, while the smooth proper version follows from pure weights and is not refuted.

## 5. Absolute cohomology, Kummer and arithmetic comparisons

For a finite-dimensional Frobenius spaceW, the arithmetic cohomology complex is represented byF−1 in the relevant continuous l-adic/Weil setting. Its degree-zero term isker(F−1), and degree-one termcoker(F−1). Equal dimensions do not make the natural map between them an isomorphism. ForF=\(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\), both dimensions are1, butker(F−1) equalsim(F−1), so the natural map iszero. The program compares this with a semisimple diagonal example. Thus the page’s additional semisimplicity assumption is mathematically necessary for that natural identification.

For a trivial rational coefficient on the discrete Weil groupZ, H0=H1=Q. Restricting to the subgroupnZ multiplies the chosen degree-one class byn. Since multiplication by every positive integer is invertible onQ, the direct limit over these restrictions remainsQ. Continuous cohomology of the profinite completion with discreteQ instead has H1=0: a continuous map from a compact group to discreteQ has finite image, hence zero. These are different theories, and the manuscript cannot simultaneously impose their conflicting outcomes with its written continuity and restrictions. Geisser7.1(c) is an exact later rational Weil-étale comparison, not a license to identify the entire manuscript axiom package with it.

For a discrete finite-rank latticeM with finite continuous action, use0→M→M_Q→M_Q/M→0. The rational module has vanishing positive continuous cohomology for the relevant profinite finite-action calculation, by averaging and passage through finite quotients. Hence

\[
H^1(\pi,M)= (M_Q/M)^\pi/\operatorname{im}(M_Q^\pi).
\]

WithM=Z trivial, the numerator isQ/Z and the denominator isallQ/Z, soH1=0. The missing quotient is therefore decisive. In degree zero, replacing a finitely generated section group by its rational lattice also forgets finite torsion: A(Fq) may be nonzero whileA(Fq)⊗Q=0.

For an abelian schemeA/S and l invertible, Kummer gives

\[
0\longrightarrow A(S)\widehat\otimes\mathbf Z_l
\longrightarrow H^1(S,T_lA)
\longrightarrow T_lH^1(S,A)\longrightarrow0
\]

with the usual limit hypotheses; rationalizing isolatesV_lH1(S,A) as the obstruction to the expected rational-point equality. Its vanishing is equivalent to finiteness of the l-primary group only with the appropriate finite-cotype condition. Weight zero alone does not force invariants to vanish. Kato–Trihan’s precise global-function-field theorem relates finiteness of one primary Sha part to the BSD rank equality and then the full BSD formula; the arbitrary-base expectation is broader.

For a proper smooth positive-genus curve C/Fq and the constant Jacobian J, geometric H¹(C) paired with V_lJ=T_lJ⊗Q_l gives the degree-two arithmetic contribution through Hochschild–Serre. With the correct dual/polarization twist, Tate’s Hom theorem identifies the relevant invariant/coinvariant piece with End_{Fq}(J)⊗Q_l. The identity is nonzero. This is the content of the author’s scan78 example and contradicts the later blanket scan82 vanishing in the same rational comparison interpretation. It does not assert that every integral torsor group equals this vector space.

This also refutes literal vanishing of H²(C,A) for A=J×C. Milne ADT II.5.1 gives that H¹(C,A) is torsion with cofinite-type ell-primary part, so its ell-adic completion is finite. Since C is proper, inverse Kummer in (5.2.1) yields 0→H¹(C,A)^∧_ell→H²(C,T_ell A)→T_ell H²(C,A)→0. Tensoring with Q_ell removes the first term and identifies V_ell H²(C,A) with the nonzero rational group above. No Sha-finiteness assumption is used. The independent program of cote12c exhibits C=J given by y²=x³+3x+2 over F5: it has five points, Frobenius polynomial T²−T+5 and an endomorphism contribution of dimension2. See work/cote12c/root_crossreview.md and outputs/crosscheck_root.json for the complete independent calculation.

For G_m, Kummer separately gives unit completion, Picard torsion and the Brauer Tate module. Over a proper smooth geometrically connected curve overFq, Br(C)=0. IfU is obtained by removingr≥1closed points, the residue sequence on its prime-to-p part has the form

\[
0\to\operatorname{Br}(U)(l)\to
\bigoplus_{x\in C\setminus U}\mathbf Q_l/\mathbf Z_l
\xrightarrow{\sum\operatorname{inv}_x}\mathbf Q_l/\mathbf Z_l\to0.
\]

Here each summand is identified with the local Brauer group using its normalized invariant, and the displayed map is their sum. Each summand maps isomorphically to Q_l/Z_l; no multiplication by the residue degree is inserted in these coordinates. Thus the corank is r−1, and for one removed point the group is zero. The program checks the all-ones row rank for r=1,…,6; the exact residue sequence, not those samples, proves the general formula. The primary reference is Milne ADT II.2.1–2.2(a).

Local duality over a nonarchimedean field with finite residue field gives the qualified prime-to-p finiteness statement for the Weil–Châtelet group. The1970 paper originally has a restriction; the1972 addendum explicitly removes it. Neither theorem supplies the false global vanishing on scan82.

## 6. Positivity and endomorphism rings

If a pairing onN restricts nondegenerately toM⊂N, the mapN→M^∨⊗Q(-ρ) has a section supplied by the inverse of the restricted pairing. Its kernel isM^⊥, givingN=M⊕M^⊥. The proposition is conditional on nondegeneracy of the restriction. Positive cones with nonempty interior and no zero degeneracy supply twisted self-duality of each simple object; Schur’s lemma then separates different isotypic blocks. Their endomorphism algebras are division algebras, not necessarily fields. None of this constructs the category or proves positivity of algebraic cycles.

For an elliptic curveE/C, h1 has Hodge types(1,0),(0,1). Its dual has types(−1,0),(0,−1), soEnd(h1) has types(−1,1),(0,0)twice,(1,−1). All have weight0, but the off-diagonal types rule out a trivial vector-space object. The program enumerates these tensor types. A level-zero/effectivity premise would be a different statement.

Over a fieldk, finite-dimensional endomorphisms form the finite-length category of torsionk[t]-modules. Its simple objects arek[t]/(P), for monic irreducibleP. ThereforeK0 is freely generated by those simples. ForP=t, the operator iszero anddet(1−tu)=1, but its rank is1, so the class isnonzero. For every otherP the reciprocal polynomialt^deg(P)P(1/t), normalized at0, is a distinct irreducible factor. Unique factorization proves that the kernel ofL=det(1−tu)^−1 is exactlyZ[(k,0)]. Restricting to invertible operators excludesP=t and makesL injective; quotienting out that class also works. This is an independent proof of the field case, with Almkvist’s general finite-projective theorem checked through WeibelII7.4.3.

OverZ, the finite projective moduleZ has infinite length andZ/p has finite length but isnot projective. Thus the field-to-ring edit changes the exact category. The general theorem is not proved by transplanting the field’s simple classification.

For a one-dimensional scalar operatora, λ_t=1+at andσ_t=(1−at)^−1; henceσ_t=1/λ_{−t}. Under the sameL convention, multiplicityc_P gives a reciprocal factor with exponent−c_P. Formally,

\[
t\frac{L'(t)}{L(t)}=\sum_{n\geq1}\operatorname{Tr}(u^n)t^n.
\]

This identity remains valid in characteristicp. Forp copies of the identity, however,L=(1−t)^−p=(1−t^p)^−1≠1 while every tracep vanishes. The integer rank of the class isp, so this is a nonzeroK0 class and an invertible-operator example. The loss is distinct from the zero-eigenvalue kernel.

FinallyI2 andJ2=\(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\) have the sameL=(1−t)^−2 and all power traces2, whileJ2 isnot diagonalizable. The invariant records a virtual semisimplification, not Jordan extension data. The program checks matrices and powers, and the displayed formulaJ2^n=I+nN proves the assertion for every n in characteristic zero.

## 7. Coarse and relative L-function boundaries

For a smooth proper n-fold with constant coefficients overFq, top cohomology is the component permutation representation twisted(-n). The next degree is dual toH1 twisted(-n). Tate’s theorem recovers the corresponding Albanese isogeny class from its Frobenius module. It does not recover a principal polarization, a curve, or a variety. Lower-dimensional boundary contributions lie below the stated coarse top-weight range under the relevant constant/coefficient hypotheses. For general lisse coefficients, the Legendre check shows why one cannot silently reuse all sharper constant-coefficient bounds.

The relative construction on scan95 also quotients by factors supported on proper closed subsets of the base. The page expressly asks which smooth/proper hypotheses are needed, and the witnesses differ in the adjective list. The search found modern birational-motive localizations and the2026 Balkan–Schreieder invariant of function-field cohomology, but neither is asserted to settle this exact draft quotient. This is a bounded negative literature result, not proof that no development exists.

## Limits of the certificates

The programs certify finite matrix ranks, finite-field point samples, formal power-series coefficients, parity, and small test cases. General descent, Kummer, purity, Tannakian reconstruction, WeilII and new2026 theorems are not claimed to have formal certificates produced in this run. Their exact statements and hypotheses were read in the sources listed in the reference ledger. The independent arguments above are the only claims assigned an independent-reproof event. No scan image was available and no diplomatic transcription was altered.
