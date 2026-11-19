# Proof and computation audit: cote 7:61–72 and cote 8:1–78

Run: SA15-20261119/root. Model: GPT-6 Astra Pro; effort setting not exposed.
This file distinguishes a proof, an exact finite check, a textual comparison, and a result taken from a reference. It does not certify the transcription against scans. Temporary P78 identifiers are mapped to final identifiers by `SA15_id_map.json`.

## 1. Compatible coefficients, inverse limits and nilpotent thickenings

For a closed immersion of affine schemes defined by a nilpotent ideal, a quasi-coherent module pulled back from the thicker scheme has sections given by a quotient module. Thus the transition maps on affine sections are surjective **when the inserted compatibility condition is imposed**. Quasi-coherence of a collection of unrelated modules is insufficient. A countable surjective inverse system of modules is Mittag–Leffler; its derived inverse limit has no degree-one obstruction. Passing from a levelwise Čech calculation to a total completed complex still requires the indicated boundedness or derived-totalization conventions. This is why the dossier retains the compatibility insertion on7:61 and does not generalize to every sheaf.

If I⊂J and the ideal J/I is nilpotent, choose a with J^a⊂I. Their adic systems are cofinal locally: J^{an}⊂I^n⊂J^n. Their formal completions therefore agree. This checks the completion step of the nilpotent-invariance argument, not the whole equivalence of infinitesimal topoi. The precise published statements are in Grothendieck1968 §5, and the modern derived comparisons are restricted as recorded in the claims.

For the dual-number test A=Q[ε]/ε², put C^n=A^{⊗(n+1)}, with d inserting1 in alternating positions. The augmentation ε:A→Q gives h(a₀⊗⋯⊗a_n)=ε(a₀)a₁⊗⋯⊗a_n. Cancellation of the inserted terms gives dh+hd=1 in the augmented complex. `check_root_math.py` constructs all matrices and checks this identity in degrees0–4 exactly. The written cancellation proves all degrees; the finite matrices merely corroborate it. It is an ordinary augmented Amitsur calculation, not proof of every analytic completion comparison.

## 2. What the closed-disc example does and does not prove

In Q_p⟨T⟩, the series f(T)=Σ_{r≥1}p^r T^{p^r−1} belongs to the Tate algebra since its coefficients tend to0. Every formal antiderivative has coefficient1 at T^{p^r}. These coefficients do not tend to0; hence no antiderivative lies in the closed-disc Tate algebra. The valuation table in `root_math.json` records this exact pattern. This refutes surjectivity of the global derivative on that algebra. It does **not** refute a sheaf-level Poincaré lemma for an unspecified finer topology, and does not decide the manuscript’s undefined non-Archimedean meaning of “flasque”.

## 3. Two-term complexes, BT1, and descent

A complex with cohomology H⁰=M and H¹=N is not specified by M,N alone: its truncation triangle has an attaching class in Ext²(N,M), after fixing cohomological conventions. Consequently the matching modules in the finite-group drawings do not automatically identify the complexes or their cross-triangle composites. The zero-composition axiom applies to successive arrows of **one** triangle; two connecting maps from different triangles can have a nonzero Yoneda product. No numerical experiment can determine the unidentified product on8:8.

Over a perfect field, α_p has one-dimensional Dieudonné module and F=V=0. Therefore dim ker F=1 while dim im V=0. It is killed by p but is not a truncated BT group of level1. This verifies the necessity of the inserted BT1 exactness condition on8:13.

On A=k[ε]/ε² in characteristic p, multiplication by ε is nonzero, while its ordinary Frobenius pullback is multiplication by ε^p=0. This proves that *ordinary* Frobenius pullback is not faithful on maps in this example. It does not prove that the manuscript’s potentially different crystalline functor is nonfaithful. The inference n=ω therefore requires identification of that functor and an actual descent argument. Oda’s perfect-field abelian theorem does not supply this automatically over all nonreduced bases.

## 4. Relative deformation groups

For a specified map of deformation complexes A→B, the relative complex may be Fib(A→B)=Cone(A→B)[−1]. Shifting the convention shifts the labels Ext⁰, Ext¹, Ext². Once a deformation theory is established, these degrees respectively govern automorphisms, choices and obstructions in the usual convention. Merely writing the symbols does not establish vanishing in degree0. The source leaves the map and category unspecified, so the audit checks degrees and definitions without manufacturing a counterexample to a still undefined functor. In particular, the kernel on8:22 is not promoted to a group-scheme counterexample without a realization.

## 5. The canceled relative μ₂ calculation

Under the explicitly chosen global-to-all-finite-local Kummer interpretation, Q×/Q×²→∏_pQ_p×/Q_p×² is injective. If q is a square everywhere locally, each prime valuation is even; unique factorization gives q=±r² for r∈Q×. The negative sign fails to be a square in Q₃. The map μ₂(Q)→∏_pμ₂(Q_p) is injective as well. The exact sequence of the homotopy fibre then identifies its degree-one group with the cokernel of this diagonal sign map, **provided these are the actual complexes and product used**. No such interpretation of the handwritten A is forced. Vanishing of relative automorphisms establishes rigidity, not nonemptiness of a torsor groupoid. The manuscript block is canceled in its entirety.

## 6. Reused analytic facts

For a Banach-valued holomorphic f on a neighborhood of the closed unit disc with a zero of order≥k, g(z)=f(z)/z^k extends holomorphically at0. Applying continuous linear functionals and the scalar maximum principle gives ||g||≤M if ||f||≤M on the unit circle, hence ||f(z)||≤M|z|^k. For a smaller polydisc at distance≥ρ/2 from the boundary, Cauchy gives ||∂_j f||≤2M/ρ. Joining points by p coordinate segments bounds the difference by (2pM/ρ)||y−a||∞. This proves the displayed equicontinuity constant under the corrected containment; it cannot decide the printed P/A glyph.

Variation of argument is obtained by lifting a path in C× to its universal cover. An endpoint-fixed homotopy gives the same difference of lifted endpoints. Concatenation adds those differences and reversal negates them. Piecewise smooth approximation within a positive-distance neighborhood of the compact path image preserves its class and avoids0. These are checks of the standard facts in the reused paragraph, with no claim to identify its exact printed edition.

## 7. Ordinary extension matrices and rank-one gauge signs

Use column coordinates (x,y), so U=[[1,0],[L,1]] and F=[[p,0],[Φ,1]]. With σ the Frobenius pullback, F′=UFσ(U)^{-1} gives Φ′=Φ+pL−σL. For A=[[0,0],[ω,0]], the convention dU=UA−A′U gives ω′=ω−dL. Thus the upper-triangular matrices printed beside these coordinate formulas require a different basis order.

Let D₀(L)=(pL−σL,−dL) and D₁(Φ,ω)=(dω,σω−pω−dΦ). Pullback commutes with d, so D₁D₀=(0,−σdL+p dL−p dL+dσL)=0. The code additionally checks actual polynomial Frobenius substitutions for p=2,3,5, including σ(dt)=p t^{p−1}dt. Omitting this factor would be an incorrect test.

For a scalar Frobenius φ, horizontality is dlogφ=σω−ω. The gauge rule φ′=uφ/σu, ω′=ω−dlogu preserves it because dlogφ′=dlogφ+dlogu−σdlogu. The positive sign in the last complex on8:31 does not preserve it with the preceding conventions. Exact rational-function tests give a nonzero residual for that sign. No glyph is changed.

For square finite free matrices over a p-torsion-free ring, ΨΦ=p^iI makes Φ invertible after inverting p: determinant invertibility follows because detΨ detΦ=p^{ir}. Hence ΦΨ=p^iI there. Entrywise p-torsion-freeness descends the equality. Without that condition the argument does not descend. The isolated integer calculation expands exactly to i+2p. Curvature is dA+A∧A; if [A,A] is a graded commutator, it equals2A∧A, so the draft bracket convention must be fixed.

## 8. Filtration length and virtual good reduction

For ℓ≠p, the relevant condition is unipotence of inertia of the specified length. A finite-order unipotent linear operator over characteristic0 is the identity: its minimal polynomial divides both(T−1)^r and T^m−1, and the latter has a simple root at1. Passing to a finite-index inertia subgroup therefore does not create a genuinely shorter unipotence filtration once the full inertia action is already unipotent; the Zariski closure has the same unipotent group. Integral lattices are recovered by intersection with rational invariant subspaces and saturation. This checks the prime-to-p part of SGA7 IX Remark5.13.1. It does not equate the p-adic notion of extending a BT group with trivial inertia. The exact p-case is delegated to a dedicated literature/proof supplement, if one is established.

## 9. A-linear Dieudonné ranks, dimensions and Hom lattices

Let A have ramification index e and residue degree f over Z_p, and W=W(F_{p^f}). The tensor algebra A⊗_{Z_p}W splits into f copies of A. If Mν is free over A, then rank_W M=eΣνrank_A Mν. The transitive Frobenius permutation forces equal component ranks; total height ef gives rank1 on each component.

Write Fν as multiplication by π^{rν} times the chosen semilinear identification, with a final unit u. The condition V=pF^{-1} is integral gives0≤rν≤e. With the convention used in the draft, length_W(M/FM)=Σrν, since each successive A/π factor is the residue field of W. Thus dimension1 means exactly one rν=1 and the rest0. Then v_p(F^f)=1/e and the Newton slope is1/(ef). The dimension calculation presupposes the classical perfect-field Dieudonné equivalence; it is not an arbitrary-base argument.

For two such objects, commuting with F^f gives aϖ=ϖ′a. On a rank-one A-module, a nonzero scalar therefore requiresϖ=ϖ′. Starting with a scalar a₀ on component0, the intertwining equations propagate a_j=π^{s_j−s′_j}a₀, up to the already fixed unit convention, where s_j=Σ_{ν<j}rν. Integrality is v_π(a₀)≥max_j(s′_j−s_j), including j=0. This proves the minimal ideal exactly. In dimension1 it is A whenν≤ν′ andπA otherwise under this component ordering. The code exhausts a finite collection of exponent patterns and checks minimality; the recurrence proves all patterns.

For the effectivity assertion, assume the commuting A-linear operators a=F^f and b=V^f=p^fa^{-1} are integral over A. The A-algebra A[a,b] is finite: each generator satisfies a monic polynomial and they commute. Starting from any finite A-lattice L₀, let L=A[a,b]L₀. Add its finitely many translates F^iL and V^iL for0≤i<f. F and V preserve the resulting lattice: terminal powers act through a,b, and mixed words reduce using FV=p. It is finite and spans the isocrystal. This proves the stated common-integrality formulation. It does not justify Ω⊗_{Q_p}W, since W is not a Q_p-algebra.

## 10. Divided-power stability versus nilpotence

In a mixed-characteristic DVR, v_π(π^n/n!)=n−e v_p(n!). Legendre gives v_p(n!)=(n−s_p(n))/(p−1). If e≤p−1, the valuation is≥s_p(n)≥1 for n≥1, so the idealπA is stable under all rational divided powers. If e≥p, n=p gives valuation p−e≤0; stability inπA fails. For e=p−1 and n=p^r, the valuation is exactly1 for every r. These divided powers therefore do not vanish moduloπ² and are not topologically nilpotent. The finite table confirms the boundary for several primes and powers. The formula proves it for all primes and all r.

This is why the lift proof cannot simply invoke Grothendieck–Messing from the phrase “πA has divided powers”. In the low-ramification nilpotent situation the theorem applies with its other hypotheses; at the boundary one must choose another argument. Classical Lubin–Tate existence remains available independently.

For a free rank-one A-moduleΩ, Ω/pΩ has residue-field length e, while Ω/πΩ has length1. Thus a dimension-one cotangent identification with Ω/pΩ cannot hold literally whene>1. The possible replacementπ is an alarm for ink review. Similarly, if t=π^{−α}Ω∨, then duality givesω=π^αΩ andΩ=π^{−α}ω. This checks the sign inconsistency without choosing an overwritten mark.

## 11. Admissibility and tensor-category closure

For a one-dimensional filtered φ-module with φ=1, Fil⁰=D and Fil¹=D, Fil²=0, one has t_N=0 and t_H=1. It is not weakly admissible and therefore cannot represent a crystalline object under the rational admissible equivalence. This disproves an unrestricted existence reconstruction; the manuscript itself reserves existence.

For D=Q_p e₀⊕Q_p e₁, φ=diag(1,p), Fil¹=span(e₀+e₁), Fil⁰=D and Fil²=0, t_H(D)=t_N(D)=1. The only proper φ-stable lines are the two eigenspaces. Their induced t_H is0, while their t_N values are0 and1, so all weak-admissibility inequalities hold. Yet Fil¹ is not φ-stable. This checks why horizontality of Frobenius and preservation of the Hodge filtration are different conditions.

Finally φ=p on a line preserves its Z_p-lattice. The dual φ=p^{-1} cannot preserve any lattice p^aZ_p: it sends it to p^{a−1}Z_p. Hence a category defined only by effective F-stable lattices is not rigid. A fibre-functor assumption does not fix an undefined category.

## 12. Lubin–Tate periods and subgroup quantifiers

Tensoring an A-rank-one Tate module over A with C gives dimension1; tensoring over Z_p gives ef. Under a normal coefficient field the latter decomposes by embeddings. Its Galois action is semilinear: χσ(g)g(x). The tangent character identifies the structural embedding in the Hodge–Tate sequence. These consequences use Tate’s theorem as referenced; the theorem itself is not independently re-proved here.

If x,y≠0 satisfy the same eigen-equation g(x)=χ(g)x, then g(y/x)=y/x. Tate’s C^{G_K}=K therefore gives y/x∈K×. In particularπx is another solution even thoughπ∉A×. Equations alone give K× uniqueness, not A× uniqueness. An integral normalization could reduce the ambiguity but is absent from the formula.

The literal claim for every J⊂I fails at J={1}: every nonzero x works. For open inertia groups, use the product of the embedding characters and the norm relation on inertia, obtaining a nonzero cyclotomic-weight eigen-equation in the intended untwisted case. The exact result used is Tate1967 Theorem2, printedp176: vanishing of the twisted invariants when the character cuts out a potentially totally ramified Z_p-extension. To apply it to inertia rather than silently substitute a full-Galois statement, choose a finite extension L/K with I_L contained in J and pass to the completion of L’s maximal unramified extension. This is again a complete discretely valued field with perfect residue field; the nontrivial cyclotomic tower is totally ramified up to a finite step. Its continuous action on the completed algebraic closure is the inertia action, so Theorem2 gives C(m)^{I_L}=0 for m≠0 and therefore C(m)^J=0. This reduction is our explicit argument using Tate’s theorem; the theorem itself is not independently re-proved. An unramified character can intervene on the full G_K, so the norm identity is not asserted globally without qualification. This is a refinement of the quantifier, not an identification of the ink.

## 13. Jets and the reused manifold text

An origin-preserving k-jet R^p→R^q has q coefficients for each monomial of total degree1 throughk. The number is q(binomial(p+k,k)−1), including0 whenk=0. The printed formula counting also the constant monomial is wrong with origin preservation; p=q=k=1 already distinguishes1 from2. The code enumerates60 parameter triples. Source and target coordinate changes act by b∘c∘a^{-1}; the opposite expression is ill-typed whenp≠q.

The chain rule shows that order-k contact is invariant under changes of differentiable coordinates. Substitution followed by degree truncation defines jet composition, and truncation is an algebra homomorphism for this operation, giving associativity. For k≥1 an invertible linear term allows recursive inversion degree by degree; at each degree the same invertible linear map solves for the next homogeneous term. For k=0 every pointed jet is the sole constant pointed jet, so a linear-term criterion is inapplicable. Truncation is surjective by adjoining zero coefficients at higher degree. For jets of bundle sections, fixing the lower jet leaves the degree-k homogeneous part, Sym^k(T*X)⊗E. In the differentiable characteristic-zero framework, derivatives/factorials identify these coefficients with jets; no characteristic-p derivative argument is imported.

Locally a multilinear section operation is determined by its values on a frame; these coefficient functions reconstruct the fibrewise map, and O-multilinearity makes changes of frame agree. Alternating/symmetric quotients require their own conventions. A transverse fiber product is locally the zero set of a map with surjective differential, so the implicit-function theorem gives the stated tangent kernel and dimension; its universal property follows from the set-theoretic fiber product. Constant-rank orbit maps give the local homogeneous-space assertion; the global orbit identification uses the source’s locally closed/countability hypotheses. The global complete-metric claim is conditional on the absent definition of the manifold category. These local proofs do not identify the historical draft number or fill missing typed pages.

## 14. Full faithfulness is not enough for the group envelope

Work over an algebraically closed field of characteristic0, with G=SL₂ and its upper triangular Borel B. Every finite-dimensional rational G-module is a direct sum of Sym^n(k²). For n>0 a B-invariant vector would have torus weight0 and be killed by the raising operator. If n is odd there is no weight0; if n is even, its weight-zero monomial has a nonzero raising derivative. Thus(Sym^n k²)^B=0 for n>0, exactly as for G, and invariants of the trivial module agree. Semisimplicity then gives W^B=W^G for every G-module W. Apply this to W=U∨⊗V: restriction Rep(G)→Rep(B) is fully faithful. It is exact, faithful and tensor-compatible.

But B is a proper closed subgroup of G. The standard two-dimensional B-module has its preserved first-coordinate line, whereas the standard G-module is irreducible. Thus the image is not closed under subobjects. This is a complete counterexample to the *formal implication* that full faithfulness alone identifies the algebraic envelope; it does not assert that the manuscript’s actual unspecified Galois functor is this example. Deligne–Milne Prop2.21 gives the correct subobject condition. The code checks invariants for n≤12 only as a finite corroboration of the all-n proof.

The late primary-source check André2023 Lem1.5 supplies another precise repair: if H is observable in G and restriction is fully faithful, then H=G. Indeed every H-module W embeds in a G-module V and is a quotient of another G-module V′; full faithfulness lifts V′→W→V to a G-map, so W is its G-stable image. Theorem2.1 proves observability for geometric ℓ-adic cohomology of smooth projective varieties over finitely generated fields. That arithmetic theorem has additional hypotheses; it cannot identify the draft’s undefined local p-adic functor by itself. The earlier notes already contained the Borel example; this run rechecks it and adds this literature comparison.

## 15. Torsor scaling, cocycles, Frobenius and real involution

A comparison isomorphism is a point of an Isom torsor, not canonically a group element. On a weight-i graded part, rescaling a chosen period byu multiplies the comparison byu^{-i}; with a right-action convention this is f_{uρ}=f_ρ∘i₁(u^{-1}). The omitted fρ in the printed formula is therefore material. In rank one, ifρ(e)=a andχ is the Tate character, thenu_g=g(a)/(aχ(g)). Direct cancellation givesu_{gh}=u_g g(u_h); the code verifies the rational identity.

Let q be a chosen trivialization and φ(q)=qb, whereφ actsσ-semilinearly. Replacingq byqg givesb′=g^{-1}bσ(g), not ordinary conjugation. A ramified de Rham field needs an explicitσ lift before this notation makes sense. For the real involution, if c_B²=1 and conjugation compatibility reads bar(c)=c c_B, then F∞=c c_B c^{-1} has square1 and bar(F∞)=F∞. These are conditional identities; they do not establish existence of the entire motivic realization system.

## 16. Purity and the twist

For an effective Cartier divisor locally cut out byt withn invertible, the Kummer exact sequence0→μ_n→G_m→G_m→0 assigns the divisor a local class in H²_Y(X,μ_n). Purity for a smooth pair of codimension1 identifies this support group withZ/n. Thus, with untwisted inputZ/n, the canonical exceptional pullback isZ/n(−1)[−2]. For codimensionc, composing divisor classes multiplies the twists and adds degree, givingZ/n(−c)[−2c]. Omitting the twist requires a specified trivialization of roots of unity. This checks the algebra of the draft’s transitivity and does not re-prove the global purity theorem. Published smooth-pair purity and the historically resolution-dependent general regular case are kept separate.

## 17. Convolution and its endpoint

Under any fixed convention in which the typed bound ||ε_x*f||_p≤w(x)||f||_p holds, Minkowski yields ||μ*f||_p≤(∫w(x)d|μ|(x))||f||_p whenever the right side is finite. Strong continuity for finitep follows first for continuous compactly supported functions, then by density and local uniform boundedness of translations. Atp=∞ this argument applies to the **norm closure** of those functions, exactly the restricted space written on the page. It does not apply to allL∞: f=1_[0,∞) onR has ||f(·−h)−f||∞=1 for everyh>0.

For an explicit convention check on an abelian unimodular group withλ multiplicative, Fubini on compactly supported functions gives ∫λ(z)(μ*f)(z)dz=(∫λ(x)dμ(x))(∫λ(y)f(y)dy), after the substitutionz=x+y (multiplicative notation analogous). Dual pairing similarly gives∫(μ*f)(z)g(z)dz=∫f(y)[∫g(x+y)dμ(x)]dy. Hölder and density extend the identities in the correspondingL^p/L^q ranges. Nonunimodular left/right Haar conventions introduce modular factors; because the preceding definitions are absent, the full weighted dual identity is recorded conditionally rather than falsely “verified” by this special case. The stray integral sign andp/q mismatch remain reading alarms.

## 18. Co-Lie complex of multiplicative type

For M=Z^r, D(M)=G_m^r is smooth and its co-Lie module isO^r=M⊗O in degree0. For a finite presentation0→Z^a→Z^b→M→0, Cartier duality gives a presentation by tori; the conormal/torus cotangent calculation at the identity yields[O^a→O^b] in degrees−1,0. This is M⊗^L_ZO. Functoriality makes these local identifications descend with the character sheaf. Bergh–Rydh PropB.4 proves the more general stack/sheaf version; the independent argument here covers the stated finite-type local setting.

For μ_n, write its coordinate algebraO[t,t^{-1}]/(t^n−1). The equation is monic and regular in the Laurent polynomial algebra. Pulling the cotangent complex back tot=1 gives[O --n→O]. Ifn is a unit it is acyclic; ifn=p overF_p the differential is zero, and bothH^{-1},H⁰ areO. This explicitly tests degrees and shows why ordinary tensor is insufficient. Associativity of derived tensor follows by taking flat/free resolutions on both sides; it is the coefficient-change calculation continued on8:79.

## Limits of this audit

No Lean checker, proof assistant or external formal certificate was executed. Exact SymPy/rational computations are reproducible algebraic checks with the stated finite scope. Cited classification, comparison, GAGA and purity theorems were matched at explicit locators, not re-proved wholesale. Undefined categories, unidentified numerical drawings and missing manuscript continuations remain labeled as such. A mathematical contradiction raises a scan-review entry; it does not change a diplomatic reading.
