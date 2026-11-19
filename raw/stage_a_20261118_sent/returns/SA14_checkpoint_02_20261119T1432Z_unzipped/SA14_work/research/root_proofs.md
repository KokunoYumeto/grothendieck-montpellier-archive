# Mathematical checks of the Codex-only sheets

**Run SA14-20261119; checked 19 November 2026.** These are the consolidation's proof checks and counterexamples, not a proposed continuation of the research directions. Diplomatic statements, our reconstructions, and published theorems remain distinct in the claims register. The supplied objects are transcriptions: no assertion below decides what the ink says.

The finite symbolic calculations are in `scripts/root_computations.py`, with the full output in `outputs/root_computations.json`. That output contains both symbolic identities and explanatory records. A `passed` flag attached to an explanatory record is not a formal proof of its geometric assertions. The arguments below supply those assertions and their limits. The three other parts have separate proof and computation files.

## 1. Resolution quotients, completion, and descent

**C-SA14-601–606, 624–626, 676.** Suppose that a proper regular model X over a complete noetherian local base is an isomorphism over the puncture U. On a regular noetherian scheme, a line bundle is represented by a Cartier divisor. A divisor on U extends by the closure of its codimension-one components, which are Cartier on X. Thus restriction Pic(X)→Pic(U) is surjective. If a divisor restricts to a principal divisor on U, subtract the divisor of that rational function on X. What remains is supported on X minus U. This proves the divisor localization sequence used in the letter. The free generators are the *codimension-one* exceptional components; a component of higher codimension is not itself a divisor generator.

Proper formal existence over the complete noetherian base identifies invertible sheaves on X with compatible invertible sheaves on its infinitesimal thickenings. To see that algebraizing a coherent sheaf gives an invertible sheaf, apply the existence theorem to the compatible inverse bundles and their evaluation isomorphisms; alternatively, use the open local-freeness locus and properness. This use of EGA is a theorem application, not a proof here of formal existence. It does not by itself imply that the quotient by the exceptional lattice is a representable group scheme.

If an invertible ideal J has ample conormal L=J/J² on the exceptional closed scheme Z, then the successive kernels are J^(n+1)/J^(n+2)≅L^(n+1). For a square-zero thickening the map a↦1+a identifies the additive ideal with the multiplicative kernel of units. The long exact sequence places the kernel and obstruction of Pic(Z_(n+1))→Pic(Z_n) in H¹(Z,L^(n+1)) and H²(Z,L^(n+1)). Serre vanishing kills both for large n. This proves eventual stabilization **conditional on the positive model**. It does not prove the existence of that model for every resolution in the letter.

Over a nonclosed residue field the exceptional lattice is a Galois module, not in general a constant lattice. Applying rational points to a quotient sequence introduces H¹(k,D′). For a constant torsion-free lattice D′, a continuous homomorphism from a profinite group has finite image and is zero. For a twisted lattice that argument is unavailable: for example, H¹ of the sign action of a group of order two on Z is Z/2. Separately, a rational point of a Picard sheaf need not be represented by a line bundle: the relative Picard comparison has a Brauer boundary. Neither obstruction may be suppressed by writing a quotient of groups of rational points.

For a smooth projective curve C and an ample line bundle L, the formal zero-section thickenings in the line-bundle model have the same square-zero description, and H²(C,L^n)=0. Their positive-twist tangent layers are H¹(C,L^n). For a plane curve of degree d, Serre duality gives

\[
h^1(C,O_C(n))=h^0(C,O_C(d-3-n)),\qquad
\sum_{n\geq1}h^1(C,O_C(n))=\binom{d-1}{3}.
\]

The sum is zero for d≤3. It equals one for a quartic. Thus the manuscript's d≥6 example is sufficient, not a first possible degree. In positive characteristic this calculation supplies dimensions of successive additive layers, not an automatic splitting of the full group into vector groups.

Elkik's henselian-pair comparison, at the exact locators in the bibliography, is a comparison on isomorphism classes of bundles and hence on Picard groups. It must not be strengthened to full faithfulness of line-bundle groupoids: units of a noncomplete ring and its completion can differ.

## 2. Cube identities and normalized correspondences

**C-SA14-607–608, 674, 678, 682.** With the cube normalization, the constant-term exponent in the n-factor formula satisfies Δ²α_n=1 and α_2=0, α_3=1. Hence α_n=(n−1)(n−2)/2. The singleton exponent is 2−n, and pair factors are indexed by *unordered* pairs. At n=3 these numbers recover the cube identity; using ordered pairs doubles the pair contribution. The program verifies the polynomial recurrence and the n=3,4,5 specializations. The multiplication formula combines n(n−1)/2 with the linear n term to give n(n+1)/2. These are exact identities, not evidence for unverified representability assumptions.

For pointed factors with universal H⁰(O)=O, restrictions to the two axes split off the Picard groups of the two factors from the Picard group of their product. The residual class is normalized along both axes and defines a divisorial correspondence. This description distinguishes normalization from a choice of universal line bundle. Finite étale subgroup rigidity likewise needs closed embeddings or a separated unramified ambient scheme: the étale double-origin trait has distinct sections agreeing generically. Infinitesimal rigidity of the residual factor does not by itself imply separatedness. In particular, Murre's Theorem 4 assumes the relevant separatedness; it cannot be cited as its proof. The general question and any modern extension of the letter's pre-ét argument are identified separately in C-SA14-674.

Product rigidity arguments require the actual domain and target of each factor map. In a noncommutative group, the correction to f by a second-factor map is an *ordered product* f·(f₂p₂)^−1, not an unqualified subtraction. In the abstract-functor sketch an open constancy locus becomes all of a connected base only after closedness is proved. The missing valuative condition therefore remains a mathematical gap; the listed functorial axioms cannot simply be regarded as an already proved rigidity criterion.

## 3. Group-theoretic counterexamples and finite radicial quotients

**C-SA14-610–614, 627–629, 680, 683, 686.** Over characteristic zero the matrix

\[
M(t)=\begin{pmatrix}1&-2t\\0&-1\end{pmatrix}
\]

has determinant −1 and square 1 for every t. Thus the square map on the smooth noncommutative group GL₂ has a positive-dimensional fibre. A power-map proposition using finiteness of its kernel cannot be transferred unchanged from commutative groups. This is a counterexample to the broadened reading, not a decision about the uncertain word in the transcript.

In characteristic p, μ_p is a connected closed nonsmooth subgroup of G_m. Its prime-to-p torsion is only the identity and is not schematically dense in μ_p. Therefore a definition requiring every connected closed subgroup scheme to satisfy a smooth torsion-rigidity condition needs an explicit subgroup restriction. Ordinary reducedness over an imperfect field is also distinct from geometric reducedness.

The homomorphism Spec k→α_p is topologically surjective, and both schemes are flat over k. It is not flat: as a k[t]/t^p-module, k is not flat. Consequently, “surjective” must mean more than topological surjectivity in the quoted flatness inference. A genuine fpqc quotient is sufficient for the descent step used there.

For the missing-flatness issue over a trait, let R=k[[π]] in characteristic p and let G=Spec R[x]/(πx,x^p), with additive comultiplication. The ideal is a Hopf ideal: Δ(πx)=πx⊗1+1⊗πx and Δ(x^p)=x^p⊗1+1⊗x^p. The unit subgroup H=Spec R is closed and flat. The generic fibre of G is the trivial affine group. Nevertheless x is nonzero π-torsion, so G/H=G is not flat. This checks every displayed hypothesis of the literal application and exhibits the needed extra hypothesis. It does not contradict the flat separated theorem in SGA 3 XVII, Appendix III.

If a quotient in the family argument is already known to be finite flat and radicial, its rank is locally constant. A smooth radicial group fibre over a field has rank one: a finite smooth radicial scheme is a single reduced rational point. On a connected base the quotient consequently has rank one everywhere and is the unit group. This proves the final step **after** quotient existence and flatness. It does not establish the preceding spreading-out lemma.

Finally, the characteristic-zero conormal question has an exact published answer: SGA 3 VI B, Proposition 1.6. Its local finite-presentation hypothesis along the unit is explicit; flatness is a conclusion, not an added assumption. The published proof uses Ω_G/S=π*ω_G/S and EGA IV's characteristic-zero differential criterion. Our event is a targeted theorem check, not a new proof of that criterion.

## 4. Openness, proper fibres and finite type

**C-SA14-630, 684.** Work locally on a noetherian base, with a separated, locally finite-type, open morphism f:X→S and proper fibres. Noetherian induction reduces generic analysis to an integral base. The generic fibre is quasi-compact, so it is contained in a quasi-compact open V of X. The morphism V→S is separated and of finite type. Properness of its generic fibre spreads after shrinking S, by the standard limit/spreading theorem for proper morphisms. This is the substantive EGA input.

After shrinking, V→S is proper. The open immersion V→X is then proper, because X→S is separated; hence V is also closed in X. Its complement W is open. Since f is open, f(W) is open in the integral base. It misses the generic point because V contains the full generic fibre, so it is empty. Thus X=V over this base open. Restrict to the remaining proper closed subset of S and apply induction. Openness is preserved by this closed restriction: an open subset of the inverse image has the form O∩f^−1(Z), and its image is f(O)∩Z. This proves quasi-compactness locally over S, hence finite type.

The argument does not remove separatedness or openness, and the special constructible-subset generalization is not automatically a theorem about arbitrary sets. It needs the locally closed scheme structure and generization-lifting interpretation actually used in its proof. C-SA14-684 retains that qualification.

## 5. Conic, triple-line and relative Picard calculations

**C-SA14-617, 619, 632–635, 639, 645–647.** The surface Riemann–Roch threshold has a direct counterexample: on P² take H=O(1) and D=K=−3H. Then H·(D−K)=0 and χ(O(D))=1, but h⁰(O(D))=0. Thus the two nonstrict inequalities do not imply an effective divisor. The usual proof needs H·(D−K)>0 to kill h⁰(K−D), and χ(O(D))>0 to force h⁰(D)>0. Its eventual large ample twists still work.

For a smooth proper surface, b₁=b₃=2 dim Pic⁰_red. Therefore χ_top=2−2b₁+b₂ gives b₂=χ_top−2+4 dim Pic⁰_red. A complex abelian surface has Betti numbers 1,4,6,4,1 and χ_top=0, so the formula with coefficient two would give 2 instead of 6. SGA 6 XIII, Remark 5.3 supplies the direct published comparison.

In xy=tz² over a trait, the z=1 chart is xy=t and is regular; the other standard charts are regular as well. Let D₁,D₂ be the two components of the special fibre. Since D₁+D₂ is the divisor of t and the components meet transversely once, D₁²=D₂²=−1. Twisting by O(D₁) changes the bidegree by (−1,1). The total degree is unchanged. These calculations explain the special-fibre components in the many-origins Picard model and the sign alarm in the draft. The author's cancellation of “not representable” must be preserved: the eventual construction asserts representability, with nonseparatedness.

For the flat family xy(x+y+tz)=0 in P² over k[t], the homogeneous defining polynomial has leading monomial x²y with coefficient one. Division by this single monic polynomial leaves a k[t]-basis of standard monomials in each graded piece, proving flatness. At t=0 the special fibre is three concurrent lines. Its plane-cubic exact sequence gives χ(O_C)=0, and connectedness gives h⁰=1, hence h¹=1. The closed-component Čech complex used in the draft is k³→k³→k with ranks 2 and 1 and has H¹=0. A closed covering is not an acyclic open covering; its componentwise complex is not a resolution of O_C. The discrepancy is therefore a genuine failed calculation under the stated geometry.

A section e:S→X normalizes a line bundle L by L⊗f*(e*L)^−1. The inverse is essential. In the absence of a section, an fppf-local line bundle representing a Picard-sheaf point can have a Brauer obstruction to global descent. Rigidification handles automorphisms when universal f_*O_X=O_S; it does not erase a descent obstruction without hypotheses.

The earlier sheet actually has a finite Stein factor Σ→S, with φ:X→Σ and a section g:Σ→X (C-SA14-687). Assume φ_*O_X=O_Σ is preserved under every S-base change. Normalize by L⊗φ*(g*L)^−1. The resulting rigidified bundle has no nonidentity rigidified automorphism, by the universal global-functions condition; ordinary fpqc descent therefore makes its isomorphism-class functor Q a sheaf. A line bundle on Σ becomes trivial locally on S: a finite algebra over a local ring is semilocal and has trivial Picard group, and a generator extends after shrinking the base. Thus the kernel Pic(Σ_T)/Pic(T) of the raw quotient map sheafifies to zero and Q identifies with the relative Picard sheaf of X/S. Finiteness of Σ/S is used in this local-triviality argument; flatness of Σ/S is not required. The source's Pic-prime/Pic-star notation is not retroactively erased.

For a relatively very ample L with f_*L locally free of rank r and universal base change, projective frames form a PGL_r-torsor. They give complete marked embeddings into P^(r−1). Under universal H⁰(O)=O, a projective transformation fixing the marked embedding pointwise acts by a scalar on its complete space of sections and is the identity in PGL_r. Automorphisms of the *unmarked image* are a different stabilizer problem. Thus an unnecessary Aut(X)=0 hypothesis must not be imported into the marked-frame statement.

For an effective Cartier divisor D, use 0→O_X→O_X(D)→N_D→0. Its long exact sequence contains H⁰(N_D)→H¹(O_X)→H¹(O_X(D))→H¹(N_D)→H²(O_X). This fixes the terminal degree in the draft. The tangent and obstruction interpretations are those of FGA and the checked modern Picard reference.

The abbreviated generator argument on the reused adic-algebra page has an elementary test. Set A=k[ε]/ε² and B=A[t]. Products of a nilpotent coefficient with the variable cannot generate t over A, since modulo ε all such products vanish. Any intended generating list must keep both the original algebra generators and the nilpotent-ideal generators. This is conditional on the literal product-only reading, not a refutation of the published EGA finite-type theorem.

## 6. Punctured curves, compact support, and transgression

**C-SA14-640–642.** For a smooth proper geometrically connected curve C over a field, remove a finite étale nonempty divisor D (equivalently geometrically reduced in this curve setting), and write U=C−D. The localization sequence for compactly supported μ_n cohomology, with n invertible, places the boundary units in degree zero and H¹_c(U,μ_n) in an extension of the n-torsion of the generalized Jacobian associated with D. The generalized Jacobian has torus rank |D(\bar k)|−1 and abelian quotient Jac(C). The cyclotomic twist is retained. This is the field-level comparison of the checked MVW reference; it does not automatically prove the manuscript's arbitrary relative statement.

The low-degree transgression of a torsor is compared with the Kummer boundary of its class only after coefficient, variance, and sign conventions are fixed. The checked 2026 theorem concerns torsors under semiabelian varieties over a field, with n invertible. It is not described as a theorem for arbitrary relative curves or an automatic calculation of every differential of Rf_!μ_n. That remaining difference explains class C in C-SA14-641.

For a reduced proper connected curve over an algebraically closed field, normalization gives an exact sequence of units. If ν is the number of normalized components, δ_s the singularity defects and r_s the numbers of branches, the affine Picard kernel has dimension Σδ_s−ν+1. Its torus rank is Σ(r_s−1)−ν+1; the remaining dimension is Σ(δ_s−r_s+1). The arithmetic genus is Σg_i+Σδ_s−ν+1. For nodal curves δ_s=r_s−1, so the entire affine kernel is a torus of rank b₁ of the dual graph. For a cusp there is an additive contribution. For three concurrent plane lines δ=3, r=3, ν=3, giving a one-dimensional unipotent contribution, consistent with §5. The program checks these finite formulas on six examples.

For a stable graph, Σν_i=2e and g=Σg_i+e−v+1. Thus Σ(3g_i−3+ν_i)=3g−3−e. The proof is arithmetic once the stable pointed-component dimensions are known. The draft's unspecified unstable corrections and drawings are not verified by this stable formula.

## 7. Normality, R₁, and rational maps

**C-SA14-638, 648–649.** On a normal noetherian integral scheme, regularity of a rational function is detected by codimension-one valuation rings, because normality is R₁ plus S₂. For an affine target this tests regularity of all coordinate functions. For a proper target, the valuative criterion extends a rational map over each codimension-one DVR, but codimension-two indeterminacy may remain. The map [x:y]:P²⇢P¹ is undefined only at [0:0:1]. Hence replacing an affine target by a proper one cannot preserve a conclusion that the indeterminacy is divisorial.

The ring R=k+(x,y)²⊂k[x,y] is generated by the monomials of degrees two and three, hence is a noetherian finite-type domain. Its normalization B=k[x,y] is finite over R: x and y are integral, satisfying T²−x² and T²−y², and B is generated as an R-module by 1,x,y. Its conductor contains (x,y)² and the normalization is an isomorphism away from the origin. Thus every height-one localization of R is regular, so R satisfies R₁. Yet x=x³/x² belongs to its fraction field, is regular at every height-one point, and is not in R. This explicitly demonstrates the missing S₂ condition.

The statement “Cohen–Macaulay over a regular local ring implies free” is correct for **maximal** Cohen–Macaulay finite modules. It is false for the unqualified module condition: over A=k[[t]], the module k has depth and dimension zero and is Cohen–Macaulay, but has t-torsion and is not free. The transcription must be checked for the intended ambient-depth convention.

If two maps to a separated target agree on a schematically dense open, their closed equalizer is all of the source: its defining ideal restricts to zero and injects into that restriction by schematic density. On a reduced scheme a dense open is schematically dense, component by component. These uniqueness checks do not imply that the sheaf of all pseudo-functions is quasi-coherent; that speculation is cancelled in the manuscript.

## 8. Determinants, Fourier signs, and rank

**C-SA14-655–663, 665–673.** Fix the determinant convention det RΓ=⊗_i(det H^i)^(−1)^i and a normalized Poincaré bundle. The degree-one term of the cohomological Fourier transform is obtained from exp(c₁(P)). On a product of g elliptic curves with polarization matrix A=diag(d₁,…,d_g), direct exterior-algebra integration gives rank χ=∏d_i and divisor class −adj(A). The program performs the full integration for g=1,2,3, including all wedge signs. It is a cohomological model, not a proof that the full Chow transform reverses all codimensions without a Beauville grading.

Consequently φ(φ(A))=(−1)^g det(A)^(g−2)A under this convention. The positive formula fails in odd dimension. If the author's det* convention is the inverse determinant, signs change; this is why the reading register demands a convention check rather than changing the text. On a curve, the ordinary determinant of the Poincaré transform gives the negative theta class with the chosen convention; its inverse gives the positive principal theta class.

The adjugate of diag(1,2,2) is diag(4,2,2). The original polarization class is primitive but the adjugate has content two. Thus the unconditional indivisibility statement fails in dimension three. Similarly, a type (1,2) polarization on a product of elliptic curves has χ=2 while its first integral coordinate is one, so it is not divisible by two in NS. Even Euler characteristic does not imply a half-polarization.

For a perfect complex F on a curve, of virtual rank ρ and determinant degree c, and a line bundle L of degree d, multiply ch(LF)=ρ+(ρd+c)η by td(C)=1+(1−g)η, where η²=0. This yields χ(LF)=ρ(1−g+d)+c. The Poincaré degree-one contribution is likewise multiplied by ρ. For a rank-two trivial bundle on an elliptic curve and a degree-one L, the actual Euler characteristic is two, whereas the rank-one formula in the draft gives one. These checks identify the missing rank factor.

The determinant construction is additive in the K₀ coefficient F. Its dependence on the line-bundle class δ is generally polynomial: on an abelian g-fold the adjugate term scales by m^(g−1) under δ↦mδ. For g=3, φ(2δ)=4φ(δ), not 2φ(δ). Thus a displayed “additive” arrow must not be interpreted as tensor additivity in δ without further restriction.

Mukai's tensor/translation identity is used in the actual direction printed in the primary article: tensoring by the degree-zero bundle indexed by β corresponds to pullback by t_β on the transform. Define h_M(β)=t_β* M⊗M⁻¹. Then l_g(λ+β)−l_g(λ)=+h_M(β), directly: the new family at x is the old family at x+β. The support of a pulled-back divisor moves by −β, but this does **not** introduce a further minus into the Picard-class difference, because h_M already uses pullback. If the manuscript's tilde map instead uses image translation, so that tilde_M(β)=t_(−β)* M⊗M⁻¹=−h_M(β), the same formula reads −tilde_M(β). An inverse Poincaré kernel also changes the dictionary. This corrects an internal convention inconsistency found by independent cross-review; it does not decide the ink or alter a transcription.

Write Q=Alb¹(X), P=Pic_X^δ, and R=Pic_B^{φ(δ)}. Under the preceding convention the normalized determinant map is equivariant by (−χ,+h) in its two variables. Consequently an actual coherent equivariant map identifies R with (−χ)_*Q+h_*P, and gives a section of R+χQ−h_*P. The manuscript's displayed product R+χQ+tilde_*P agrees if tilde=−h. Without that dictionary its exact signed product is not certified. Moreover, an equality of H¹ torsor classes supplies only existence of an isomorphism; the canonical isomorphism requires the determinant normalization and its compatible descent data. These are the reasons C-SA14-657 remains a qualified class C comparison problem.

For Chow groups, Beauville's formula is CH^p_(s)→CH^(g−p+s)_(s). The simpler g−p rule applies only to the grade-zero part. A computation in cohomology cannot establish the simpler rule for every algebraic cycle.

Finally, the universal pointed genus-one curve has its origin divisor of degree one and canonical class of degree zero. The origin cannot be an integral multiple of the canonical class. This refutes an unrestricted marked genus-one version of the Franchetta statement; the checked theorem for g≥3 is kept at its actual scope. The principal theta-torsor construction is separately matched to Alexeev's explicit evaluation-at-zero construction. Results about arbitrary polarization types are not substituted for that principal theorem.

## 9. Annihilating integers and torsor trivializations

**C-SA14-657, 664, 666.** For g≥2 put a_λ=χλ^g−λ^(g−1). Every odd prime dividing all a_λ would divide both χ−1 (λ=1) and χ+1 (λ=−1), hence cannot exist. In fact these two values show the common gcd divides gcd(χ−1,2). If χ is even, a_1 is odd and the gcd is one. If χ is odd, every a_λ is even: for even λ the factor λ^(g−1) is even, and for odd λ the factor χλ−1 is even. Therefore

\[
\gcd_{\lambda\in\mathbb Z}(\chi\lambda^g-\lambda^{g-1})
=\gcd(\chi-1,2).
\]

Setting χ=1 gives gcd(λ^g−λ^(g−1))=2. The program checks a finite range as a corroboration; the argument above proves the unrestricted integer claim. The manuscript's `ppcm` cannot express this annihilator deduction: an lcm would not give the stated integer two.

The same upper bound holds if λ is restricted to positive integers. Modulo a_1=χ−1, the values a_2 and a_3 reduce to 2^(g−1) and 2·3^(g−1), whose gcd is 2 for g≥2. Their common gcd therefore divides gcd(χ−1,2), and the parity argument supplies equality. Thus the use of λ=−1 is convenient but not an extra source hypothesis.

If a torsor class is killed by all a_λ, Bezout gives annihilation by their gcd. A zero cohomology class means a section exists; it does not select a canonical section. Comparing canonical trivializations requires compatible isomorphisms and normalization. Accordingly, the exact three-torsor comparison in C-SA14-657 and the comparison of doubled canonical classes in C-SA14-666 are not declared proved merely from this gcd computation.

## 10. Koszul and graded-module checks

**C-SA14-637, 654, 675.** For the cochain Koszul differential d=a∧−, contraction ι_i satisfies dι_i+ι_i d=a_i Id. The program verifies all eight exterior basis vectors in rank three for all three contractions. The standard graded anti-commutation identity proves the formula over any commutative ring and any rank. If one a_i is a unit, a_i^−1ι_i is a contracting homotopy.

The reused graded-module pages define a direct-sum grading, regroup it along a monoid homomorphism, and express tensor and Hom gradings componentwise. The checks are type checks and finite-support checks: an element in a direct sum has finite support; homogeneous components add their degrees under multiplication or tensor product; an unrestricted product of Hom components must not silently be replaced by a direct sum unless finite-support conditions apply. The surrounding labels do not identify a unique prepublication Bourbaki edition, so only the mathematical statements and the checked published background are claimed.

For the reused regular-ring example, maximal ideals of a polynomial ring over a DVR can have different heights: (π,T) has height two, whereas (πT−1) has quotient equal to the fraction field and has height one. Regularity is a local property at each maximal ideal, not a claim that all maximal ideals have a common height. This is the point retained in C-SA14-675.

## 11. Connectedness under cuts and the converse

**C-SA14-650–653.** Completeness and lower bounds on component dimensions do not suffice for connectedness of a puncture. Let

\[
A=k[[x_1,x_2,x_3,y_1,y_2,y_3]]/(x_i y_j:1\le i,j\le3).
\]

It is the fibre product of two complete regular local rings over k. Its two components meet only at the closed point. The puncture is a disjoint union of two nonempty punctured three-spaces; all components of the puncture have dimension two. The element f=x₁+y₁ cuts each branch in a nonempty punctured two-space. Thus the punctured section remains disconnected while all the literal noetherian, completeness and component-dimension requirements of the isolated lemma hold. This is a counterexample only to the lemma read without a prior connectedness assumption.

SGA 2 XIII, Theorem 2.1 starts with explicit connectedness in dimension at least k and the component bound at least k+1 on X′. It gives the corresponding k−m bounds after m≤k cuts. The paragraph immediately following it gives the converse from connectedness of every k-fold cut, excluding an irreducible X of dimension zero or one. This matches the converse on the manuscript's scan 13 and its attempted proof on scans 15 and 17. Normality and S₂ enter the proof after reduction; they are **not extra hypotheses in the final complete-local topological statement**. The reversed inequality at line 75 is separately a reading alarm.

The complete local fundamental-group conjecture is a different question. Suzuki's verified result concerns the maximal pro-nilpotent quotient. Finite generation of that quotient does not imply finite generation of an arbitrary profinite group, so the full conjecture is not marked solved by that theorem.

## 12. Published-result limits maintained in the registers

Some checks appropriately stop at a precise theorem boundary. The projective one-abelian-fibre theorem in GIT and Genestier–Ngô is not by itself a proof of every proper-family formulation. SGA 6 XII distinguishes generic relative quasi-affineness from affineness over a field. Its historical question about relative affineness is not evidence that the question remains open in 2026. Modern local Picard results assume the exact S₂, pure-dimension and geometric hypotheses recorded in their claims; tangent vanishing alone proves neither representability nor countability. The conormal criterion, by contrast, has an exact SGA 3 match and is classified accordingly. These are deliberate differences in evidential strength, not omitted calculations.
