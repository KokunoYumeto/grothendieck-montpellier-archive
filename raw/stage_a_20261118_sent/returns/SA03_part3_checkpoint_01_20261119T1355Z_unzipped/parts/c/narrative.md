# Cote91, scans99–143: consolidated commentary

## 1. Scope, evidence and the principal corrections

This segment covers all60 indexed entries of MPL_91_099-143 and the complete independent Codex leads and transcriptions K91-08, K91-09 and K91-10. It produces43 consolidated items and78 separately stated claims. Every indexed entry was read with the cited transcription. The complete Pro doubts file was also read. File-line locations refer to the actual supplied files; they are not invented manuscript line numbers. No scan or second-pass correction was supplied.

The leaves combine three bodies of work. First come schematic/constructible categories and the constructible topology, followed by a compact reduced envelope and Ind/pro comparisons. A Greenberg–Néron programme then studies thickness conditions and constructibility of images. Finally there are Laurent-unit stages and nilpotent coordinate changes. Reused Bourbaki typescripts interrupt these handwritten sequences: topological groups, exterior algebra, restricted Lie algebras and formal matrix groups. Archive order is retained for source location but does not give the printed typescripts' argument order or the chronology of the handwritten work. A dated letter elsewhere in cote91 cannot date these leaves.

The most consequential correction concerns scan110. Pro line343 makes a positive assertion that quasi-compact maps send constructible subsets to constructible subsets. K91-08 line407 reads the negative assertion. The positive statement fails for the affine map Spec Q(t)→Spec Q[t]; its image is the generic singleton. This is a conflict between witnesses, not an established false claim by Grothendieck. The nearby Pro instruction “les vérifier” also conflicts with Codex “sont vérifiées.” On108 the Pro warning that a pullback hypothesis is too restrictive conflicts with Codex saying it always holds for scheme morphisms. The latter agrees with the base-change argument.

Other corrections are equally bounded. The generic-point margin on106 may say uniqueness under T0 rather than a converse. Scan118 may be a heading about thick points, rather than an instruction to pose a problem. Scan135's nonisomorphism assertion requires a strict stage inequality; equality is identity. The symplectic phrase “in2n variables” is representation degree: the nearby GL(n) exercise explicitly distinguishes n variables from formal dimension n². That wording need not be an ink error. Nilpotent evaluation on an ideal must be kept separate from substitution in a truncated polynomial quotient.

These judgments appear individually in entries.tsv and items.json. Metadata, a title sheet, editorial task lists and withdrawn drafts produce no phantom mathematical assertions. The43 items are editorial units; the78 claims separate hypotheses and conclusions that cannot share one fate.

## 2. Reused inverse-limit topology: claims404–409

Scans100 and102 carry report285, printed pages12 and10. Their content is standard inverse-limit topology, not an identified new manuscript discovery. The following proofs were checked directly.

For a countable inverse system of nonempty sets with surjective transitions, fix a point at stage p, choose successive lifts, and define all earlier coordinates by transition maps. This constructs a compatible tuple over the chosen point. The countable Mittag-Leffler lemma is a broader published comparator: Stacks0597, Lemma10.86.3. It should not be invoked for arbitrary uncountable systems without a further argument.

Let compatible maps gα:Aα→Bα have dense image, and suppose every projection A=lim Aα→Aα is surjective. Any nonempty basic open cylinder in B is controlled by finitely many coordinates; a common upper index replaces those by one coordinate condition. Density at that index and surjectivity of the projection from A give a point in the cylinder. This proves density of g(A). Exactly the same argument shows that a subgroup K of lim Gα is dense in lim im(K→Gα). Equality is stronger: the finite-support subgroup of the product of copies of F2 is dense and proper.

For open surjective transition homomorphisms, a basic neighbourhood at stage β maps to an open neighbourhood at an earlier stage α. Surjectivity of limit projections identifies the image of the corresponding cylinder with that stage image. Hence the limit projections are open. Here the older term “homomorphisme sur” must include the topological quotient/open condition; algebraic surjectivity alone is insufficient.

Compatible subgroup limits are the same subsets whether formed in the subgroups or in the ambient product. Their initial topologies therefore agree. Kernels are defined coordinatewise, so commute with limits. Finite intersections of coordinate identity-neighbourhoods reduce to a single later-stage neighbourhood. These are proofs of the particular claims; reading a general chapter title would not have checked them.

The publisher and official Bourbaki bibliography were opened, and a companion agent's primary French reprint was personally read at ChapterIII section7 no1, introduction and Proposition1, printed III.57–59. This confirms the published framework, but the draft report285/Propositions23–24 numbering has not been matched exactly. The item and reference retain that limitation.

## 3. Patch topology and constructible categories: claims410–430

### The topological argument

Under the written retrocompact-open basis assumptions, the constructible topology is generated by the finite Boolean combinations of the basis opens. If x and y are distinguishable in the original T0 topology, choose a basis open U containing exactly one. U and its complement are disjoint patch opens separating them. Conversely, topologically indistinguishable points remain indistinguishable under Boolean combinations, so patch Hausdorffness implies T0. The restriction lemma on104–106 has two variables E and F; the ambiguous letter must not be erased.

Affine patch compactness can be checked without assuming the conclusion. For an ultrafilter on Spec A, let p consist of those a for which V(a) belongs to the ultrafilter. The identities for V(a+b), V(ab), and V(1) show that p is prime. Each basic patch condition D(a) or V(a) is decided according to membership of a in p, so this ultrafilter converges to p. T0 separation makes the limit unique. A finite affine cover of a qcqs scheme then gives compactness, because intersections of quasi-compact opens are quasi-compact and the induced patch topologies agree. A quasi-separated scheme has locally compact patch topology. These precise current statements are in Stacks08YF, Section5.23; EGAIV1.9 is the earlier scheme treatment.

For a patch-closed E, compactness is equivalent to containment in finitely many compact basis opens. One direction uses the original open cover; the other uses closedness inside a finite compact union. The closedness assumption matters. An abstract locally compact subspace need not be closed in its ambient space. This is why the locality question on107 is formulated as locality of patch closedness, not an unrestricted equivalence with local compactness.

To obtain a generic point of an irreducible closed Z, choose a compact patch basis open meeting Z. Its intersection with Z is patch closed. Nonempty original opens of Z have the finite-intersection property, including after intersection with this fixed basis open. Patch compactness gives a point lying in every nonempty open of Z, hence generic. T0 gives uniqueness. This verifies existence and uniqueness, not the uncertain converse assigned by one witness.

### Pullback, properness and images

Any scheme morphism pulls back a retrocompact open immersion to a retrocompact open immersion: quasi-compactness is stable under base change. Finite Boolean operations then give constructible pullback, locally as needed. Stacks054H, Lemma29.23.1, is an exact published counterpart. This explains why the negative margin reading on108 should be flagged.

Under the locally spectral hypotheses on108–110, quasi-compactness of a map can be tested on quasi-compact basis opens. Their preimages are compact patch subspaces, giving properness of the patch map. Conversely, properness pulls compact patch basis opens back to compact subsets, hence to quasi-compact subsets for the original topology. In locally compact Hausdorff spaces the relevant proper-map condition is equivalent to closedness with compact fibres. The source cites Bourbaki TopologieI section10 no2 Theorem1; that exact book passage was not independently recovered, so the proof here carries the mathematical verification.

This does not give constructible images. In Spec Q[t], a constructible set containing the generic point contains a nonempty Zariski open: one of its locally closed pieces contains the generic point, so that piece is open in a closed subset equal to the whole irreducible space. Every such nonempty open contains closed points. Therefore the generic singleton is not constructible. Spec Q(t)→Spec Q[t] is affine, hence quasi-compact, and its whole source is constructible. Every hypothesis of the counterexample is checked. The counterexample rejects the positive Pro reading, while Codex's negative reading is compatible with it.

The surviving corollary is valid. A constructible subset is patch clopen and compact. A continuous image in a Hausdorff patch space is compact and closed. It is therefore constructible precisely when it is also patch open. An open-basis argument makes “images of constructibles are constructible” equivalent to openness of the patch map in the stated compact setting. A compact Hausdorff surjection is a closed quotient map, so patch closedness and clopenness descend by inverse image. These are distinct claims420–421.

### The affine envelope on115

Write X=Spec A. For each finite partition P into reduced, locally closed, affine constructible pieces, take A_P to be the product of their section rings. Refinement gives restriction maps A_P→A_Q. These maps are injective: a section vanishing after restriction to a covering partition vanishes at every prime, and the source pieces are reduced. This says nothing about injectivity of A→A_P when A has nilpotents.

Let B=colim_P A_P. Every b in B is represented at one finite partition. Refine each piece by the zero and nonzero loci of that representative; on the zero piece it is zero and on the nonzero piece it has an inverse. The resulting element c satisfies b²c=b and bc²=c. Thus B is absolutely flat. Any A-map to an absolutely flat ring R has a unique extension to each partition: the vanishing/nonvanishing subsets pull back to clopen pieces of Spec R, the reductions kill nilpotents, and the localizations invert exactly the required functions. These extensions are compatible. Hence B is the universal absolutely flat A-algebra.

Each Spec A_P has exactly the underlying points of X, with finer clopen partition topology. Compatible primes in the filtered system therefore give exactly the points of X. The resulting topology is generated by all constructible pieces, hence is the patch topology. A partition of all compact patch X into nonempty constructible pieces is automatically finite: its pieces form a disjoint open cover and a finite subcover exhausts it. The phrase “arbitrary partition” is therefore not alone a counterexample to the construction.

This is an exact object identification with Olivier's T(A), not merely a similarity of topics. Exp6, Propositions3–5, especially p6-04, supplies the pointwise-inverse presentation, the spectrum correspondence, absolute flatness and the universal property. The talks were20December1967 and3January1968; the volume was published in1968. Exp9, sectionII Proposition2, p9-09, globalizes the construction, with an affine surjective monomorphism T(X)→X and the right adjoint to inclusion of schemes whose local rings are fields. Its talk was14February1968. Olivier cites EGAIV1.9.16; Ferrand2003 section8.3 p581 independently connects T(X) to EGAI1971,7.2.14. Ferrand's footnote1 p554 records private versions circulated in1970 and a1971 thesis, distinct from the rewritten2003 publication. None of these dates by itself dates the archive leaves.

For a patch-closed E⊂X, take the closed subscheme of T(X) with underlying E and compose with T(X)→X. This is a quasi-compact monomorphism with image E. Conversely a qc scheme map has proconstructible image under the stated framework. This proves the stronger claim on111. It does not identify T(A) with the w-local cover A_w: Stacks096Y is used only for finite vanishing-pattern refinement.

A quasi-compact scheme with Hausdorff Zariski topology is affine. Choose finitely many affine opens. Each is compact, hence closed in the Hausdorff whole space. Successively subtract earlier clopen pieces to obtain a finite disjoint affine clopen cover. Their finite coproduct is affine. If the scheme is reduced, its zero-dimensional coordinate ring is absolutely flat. The word “compact” here is topological compact Hausdorff, not proper over a field.

### What the category diagrams do and do not prove

Constructible applications are residue-field-compatible maps induced by morphisms on reduced locally closed strata. Pullback of a target stratum is constructible on a source piece; finite common refinement proves composition. On qcqs domains, compact patch covers reduce locality to finite affine data. Restricted full faithfulness on114 can then be checked by evaluating a natural transformation on the model pieces and gluing compatible maps, provided the category really has the asserted model presentations. The missing ambient-category definition is retained as a condition.

Likewise, Hom between actual Ind presentations has the standard lim-in-source/colim-in-target formula. It does not permit exchanging those operations. Scan97, personally read at the cross-package endpoint, displays precisely that obstruction. One compatible constructible map to every finite target stage need not use a single finite partition for all stages. For T=A1_Q and target stages A^n, let coordinate m be the indicator of a distinct rational point a_m. Each finite tuple is piecewise regular. If a single finite constructible partition made all coordinates regular, its piece containing the generic point would contain an open set and infinitely many a_m; a regular function on its irreducible open part cannot be zero generically and one at a point. The contradiction preserves the quantifiers. The later affine-envelope and finite-presentation Hom theorems do not remove this obstruction.

## 4. Thickness, Greenberg points and the pro-Hom formula: claims431–446,453

The four conditions on126–128 must remain separate. “Maximal” is read in the generalization order, meaning generic in the fibre, not maximal ideal/closed point. If x_k is maximal in the fibre over x_i, any generalization in its fibre over x_j also lies over x_i, so no new generalization is possible. For (Ép)′, the entire fibre over x_i lies in the pullback of U_i and therefore in closure{x_j}; x_j itself belongs to the fibre. It is its unique generic point. This implication does not require a countable ML argument.

For affine-transition inverse limits, closure{x}=intersection_i π_i^−1(closure{x_i}). With noetherian stages every stage closure is constructible. If closure{x} is constructible, its patch-open complement is also compact. The complements of the displayed inverse images cover that complement, so finitely many suffice; a common upper index gives equality with a single stage pullback. The converse is constructible pullback. Stacks0A2Y, Lemma5.24.4, independently gives general constructible descent in spectral limits.

The remaining arrow marked M.L. et I=N is not settled by citing Stacks0597. The set-system lemma gives a nonempty limit when all stages are nonempty and images stabilize. The manuscript must identify which fibre/image system has that property and how it supplies a dense open. Neither that identification nor the right-hand X′_i is secure. Under the additional ambient/noetherian interpretation, (Ép)′ gives a nonempty constructible relatively open part of closure{x}; this is a reconstruction, not an asserted full equivalence. The local prime-ideal fragment is meaningful with a list (f1,...,fn); a literal product would impose a different zero locus.

On131 the Greenberg point correspondence has a precise modern form over a complete DVR, with the stated perfectness restrictions in mixed characteristic: BGv6 Proposition18.2 identifies points of the Greenberg realization over a suitable perfect test algebra with points over its lifted valuation ring. The arXiv version history records first circulation31October2013 and a corrected proof in v6,19February2022. Completeness is not explicit on this leaf and is marked as an added hypothesis. An HTML rendering date is not used as a publication date.

A generic section into a proper target extends uniquely over a valuation ring. This supplies the stated set map, wherever a rational generic-fibre map is defined. Stacks0BX5, Lemma29.43.1, is the exact valuative comparator. A point map does not automatically give a morphism at a finite Greenberg level. Nor does a residue map into the perfection of k(x) automatically descend into k(x).

Accordingly, thick-image preservation, the residue-field inclusion, the finite-index promorphism and the bounded-simple constructible-image theorem remain classF: the exact statements cannot be identified from the retained definitions. This is not a declaration that the claims are false or open research problems. Greenberg1966 Theorem1 and its corollaries give linear approximation over a Henselian DVR. Sebag's2001 preprint, published2004, gives finite-level constructible cylinder images at4.3.12 and a bounded-Jacobian cylinder theorem at7.2.1–2, with a smooth source and explicit dimension and defect conditions. The manuscript's simple, ell|d invariant and finite index have not been shown to equal those conditions. The earlier H-G status is not adopted as proof.

The scheme Hom statement on136 is independently identifiable after a qualification. If target stages X_i are finitely presented over S, source stages Y_j are qcqs, and transitions are eventually affine, then

Hom(lim_j Y_j, lim_i X_i)
= lim_i Hom(lim_j Y_j,X_i)
= lim_i colim_j Hom(Y_j,X_i)
= Hom_Pro(Y,X).

The middle equality is Stacks01ZC, Proposition32.6.1. Quasi-separatedness makes finitely many local gluing equalities descend at one stage. The page explicitly inserts only quasi-compactness. The proof certifies the qcqs version, not the extra qc-only generality; no unsupported counterexample is claimed.

## 5. Laurent units: claims447–452

For n≥0 use variables a_i,b_i for i≥−n and impose, for every d≥−2n,

sum_(i+j=d) a_i b_j = δ_(d,0).

Each sum is finite. The resulting affine scheme Γ_n represents a Laurent series and its inverse with lower bound−n. Their union represents A((t))×. The i<n reading would contradict the variable range and eliminate ordinary units; i<−n is the mathematically consistent alternative. At n=0 the constant equation is a0b0=1, not zero. Recursively eliminating b_m yields Γ0=Spec Z[a0,a0^−1,a1,a2,...].

For −n≤ν≤n, the map Γ0→Γ_n multiplies the series by t^ν and its inverse by t^−ν. It is a closed immersion: impose a_i=0 belowν and b_i=0 below−ν; aνb−ν=1 and the remaining inverse coefficients are recursively determined. The finitely many such closed subschemes are disjoint, so their union Γ′_n is a closed immersion. At every field-valued point, a Laurent unit has a unique valuationν in this interval. Hence the immersion is surjective on underlying spaces. The source is reduced over Z, so it is Γ_n,red.

The endpoint copyν=−n is the principal open where a_−n is invertible; the inverse equations force all coefficients b_i below n to vanish. Theν=n case is symmetric. For |ν|<n, work over k[ε]/ε² and use

f=t^ν(1+εt^−1),  f^−1=t^−ν(1−εt^−1).

The bounds hold, the closed point lies in theν copy, but the point does not factor through that copy. An open immersion containing the closed point of this local dual-number scheme would contain the whole scheme. Thus the interior copy is not open. Passing to a residue field proves this after every nonempty base change.

For n′>n≥|i| set m=n′−|i|. The pair t^i(1+εt^−m), t^−i(1−εt^−m) belongs to Γ_n′ but not Γ_n, because one negative exponent has size n′. It lies in valuation component i. This proves strict-stage nonisomorphism over every nonempty base. At n′=n the map is identity, refuting the literal≥ boundary. No source reading is changed.

The earlier-run example1+εt^−1 demonstrates nilpotent structure. It never refuted topological surjectivity of Γ′_1→Γ1; ring-valued surjectivity and surjectivity of underlying spaces are different. Osipov–Zhu, section2 Lemma2.1, gives the established Laurent-unit factorization into negative nilpotent, valuation, constant-unit and positive factors. Its first preprint was2013, revised2014, journal2016. The bounded Γ_n assertions above are our direct proofs, not quotations of that lemma.

## 6. Nilpotent coordinates: claims454–460

If m^(N+1)=0, every monomial of total degree>N vanishes on m^n. Thus evaluation uses a finite jet. Suppose the constant vector lies in m and the linear coefficient matrix is invertible over a local ring. Modulo m² the map is an invertible affine map. If a solution is known modulo m^r, change it by δ∈(m^r/m^(r+1))^n. The change in the output is the linear matrix timesδ: every nonlinear derivative has a factor in m and contributes only at the next level. Solve the correction uniquely, and induct to m^(N+1)=0. The same argument proves injectivity.

For augmentation-preserving automorphisms of A[t1,...,tn]/(t)^(N+1), constants vanish and the linear determinant must be a unit. Recursive degree correction constructs the inverse; higher coefficients are unrestricted. This is a represented coefficient-open functor. The condition det≠0 over arbitrary rings may denote the scheme open D(det), which is correct. It is false only if read as a nonzero ring element: t↦2t is not invertible over Z.

With a square-zero ideal I, the differenceδ of two algebra lifts satisfiesδ(bb′)=bδ(b′)+b′δ(b), because the product of their differences lies in I²=0. Thus existing lifts form a torsor under the derivation module, as in Stacks04FJ, Lemma37.9.5. Smoothness supplies existence in the usual setting. An identification with a tensor product of a tangent module needs the relevant projectivity and base-change hypotheses; the undeclared symbol on142 is not silently defined.

Quadratic substitution was recomputed exactly. The constant, linear and quadratic coefficients are

c0=a′0+a′1a0+a′2a0²,
c1=a′1a1+2a′2a0a1,
c2=a′1a2+a′2a1²+2a′2a0a2.

The omitted terms are2a′2a1a2t³+a′2a2²t⁴. The linear coefficient confirms the doubtful2. Dropping the remainder needs the actual evaluation or quotient relation.

In A=Q[ε]/ε³, substitution t↦t+ε does not preserve(t³): modulo ε³ and t³, its cube is3εt²+3ε²t, a nonzero combination of basis monomials. Translation remains a perfectly valid bijection of the nilpotent ideal m. This counterexample targets the naive truncated-algebra interpretation, not the evaluation construction.

## 7. Reused exterior and Lie algebra: claims461–478

For M=⊕M_i, send each summand into the corresponding factor of the graded tensor product⊗^g Λ(M_i). Degree-one generators anticommute across factors and square to zero, so the exterior universal property gives a map Λ(M)→⊗^gΛ(M_i). The reverse map comes from the inclusions. Both composites fix the generators; hence they are inverse. Expanding by degree gives the direct-sum formula, and sorting multilinear terms gives the shuffle signs. Naturality is equality on generators.

A splitting M=N⊕P gives a splitting of Λ(N)→Λ(M); the complementary positive-P-degree terms are the ideal generated by P. Every positive-degree element involves finitely many generators, say r, so its(r+1)st power vanishes. This is elementwise nilpotence; the entire positive ideal need not be nilpotent for infinite-rank M. Under the written split-intersection hypotheses decompose M=A⊕B⊕C⊕D with N=A⊕B and P=A⊕C. The multidegree decomposition shows Λ(N)∩Λ(P)=Λ(A). Ordered wedge bases follow first for finite free modules and then by the filtered union over finite subsets of the basis. Stacks00DM supplies exact current standard counterparts; Bourbaki AlgebraIII section7 no7–8 is the publication concordance.

The isolated cohomology exercise has a safe sufficient proof. If a chain map T is invertible and T=dρ+ρd, then T commutes with d and h=T^−1ρ satisfies dh+hd=1. All cohomology vanishes. The omitted representation-theoretic antecedents are not restored from this abstract lemma.

For a free restricted Lie algebra g in characteristic p, put φ(x)=x^p−x^[p] in U(g). The restricted identity makesφ(x) central. Ordinary PBW, with a totally ordered basis bλ, shows that products b^βφ(b)^γ, 0≤βλ<p, have leading PBW monomial b^(β+pγ), with unit diagonal. This triangular change gives a basis of U(g). The ideal generated by theφ(bλ) has the basis elements withγ≠0; the quotient therefore has the restricted PBW basis and contains g injectively. Its universal property is the quotient universal property. Ardizzoni's preprint Example4.6 p12 is a checked modern field comparator, not a proof of the more general free-ring version. It circulated2010, appeared online2011 and in the journal2012.

The identity

D(x^p)=sum_(j=0)^(p−1) x^jD(x)x^(p−1−j)=(ad x)^(p−1)D(x)

follows from the Leibniz rule and binomial coefficients modulo p. It proves the associative restricted-derivation assertion. A derivation of g extends to the restricted quotient exactly when it preserves the defining ideal, giving the stated condition. The characteristic and freeness hypotheses are retained.

For the two-variable formal law on139, write the first coordinate multiplicatively as1+x1. The action on the second coordinate is multiplication by(1+x1)^p=1+x1^p. Multiplicativity and Frobenius prove associativity and the inverse formula. Interchanging X,Y changes the second coordinate by x1^p y2−y1^p x2, so the law is noncommutative; this difference has degree p+1≥3 and its quadratic antisymmetrization is zero. Thus the Lie algebra is abelian. Exact polynomial checks for p=2,3,5,7 supplement this general proof, rather than prove it for all primes.

The formal completion of GL_n at identity has U+V+UV law. Left translation differentiates to(I+U)E_ij, giving the displayed invariant fields and matrix-unit brackets. Their pth powers are derivations in characteristic p; checking generators yields X_ii^p=X_ii and X_ij^p=0 for i≠j. For a formal group homomorphism, the tangent derivation is first evaluated at the identity and then extended invariantly. The raw expression D(v∘F) otherwise has the wrong codomain. The printed row/column convention is not reversed.

For Sp_2n, write X in n-by-n blocks. XᵀJ+JX=0 gives S=−Pᵀ and Q,R symmetric, including characteristic2. Dimension is n²+n(n+1)=n(2n+1). For the orthogonal chart, set B=R^−1S with S skew and R symmetric invertible. Then BᵀR=−RB and

(I+B)ᵀR(I+B)=(I−B)ᵀR(I−B).

This proves orthogonality of U=(I−B)^−1(I+B). When2 is invertible, (U−I)(U+I)^−1=B, proving the inverse Cayley formula and the formal chart of dimension n(n−1)/2. The determinant-open conditions are essential. The off-leaf continuation and blank AlgèbreIX exercise references are not invented.

## 8. Literature and verification boundaries

The bibliography has29 checked links, with verification scope in each annote. A verified bibliographic page is not a verified inaccessible theorem. Large EGA and Bourbaki PDF failures, blocked zbMATH reviews and inaccessible AMS text are recorded. Exact mathematical checks use opened primary texts and stable Stacks locators; literature gaps are not converted into classD. ClassA is not assigned merely because a result occurs in EGA: later-than-these-leaves chronology is not established. Reused textbook material is classE as inherited background, without a claim about the author's original discovery dates.

The33 reading flags are proposals for a later scan run. The16 problem entries distinguish confirmed questions, conditional unfinished steps, withdrawn formulations and uncertain question marks. They do not imply16 presently open research problems.

All25 links are endpoint audits. Internal archive endpoints and exact accessible publication comparisons were read on both sides. Historical references whose PDFs were inaccessible are explicitly limited. Thirteen other-project links are retained in their own category: their cited full returns are not supplied, so those second endpoints cannot be checked and no reported project status is changed. That is a documented source boundary, not a completed external verification.

The computation program and its output retain23 groups of exact checks. Finite examples and identity checks are distinguished from general proofs above. CHECK_EVENTS records the type actually performed: source comparison, targeted hypothesis check, independent proof, or computation. The ranked directions select future work; no new research programme beyond the checks needed for this consolidation is developed here.
