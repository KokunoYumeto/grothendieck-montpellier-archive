# Independent audit of the root dossier

Reviewer: GPT-6 Astra Pro / inherited effort / agent16. Checked 19 November 2026, after completion of the assigned MPL_16+47+54+44 review. This file records an additional audit requested by the parent. No root-owned file was edited.

## Scope and result

I screened the root's 114 claim records and 39 problem records, read the complete R1–R11 argument file, and checked selected claims in detail against the supplied transcription and reopened primary references. This is an independent mathematical and attribution review, not a new exhaustive source review of the root's packages. The original owner retains responsibility for their complete entry coverage and literature-search records.

The substantive counterexamples in R6 and R8–R11 are valid under the hypotheses checked below. I found one clear source-status error and one unsupported extension from an analytic theorem to an abstract ringed-space statement, both in CL-SA18-11102. Two smaller changes concern the exact published locator for CL-SA18-11065 and the literature classification/origin fields of CL-SA18-11110a/b. I found no reason to weaken the independently checked counterexamples.

## Changes recommended to the parent

### 1. CL-SA18-11102: distinguish the proposed abstract Lemma B from its analytic applications

The source is `SA18_texts/codex/K55-01_transcription.tex`, cote55 scan14, absolute lines447–464. Lines447–453 give the assumptions, line456 asserts stabilization of increasing coherent submodules, line459 gives the noetherianity corollary, and lines462–464 propose an analytic-polyhedron application with “préciser ce point”. There is no proof argument in this passage. The claim's `status_on_pages` should therefore be **stated without proof**, or **open on the pages**, rather than **proof sketched**.

The current fate says that the unique-continuation condition forces global stabilization after local stabilization and that quasi-compactness provides a finite cover. The last step is sound only after one has proved a *fixed-neighborhood* stabilization result. Noetherian stalks give an index at each point, but do not by themselves give one neighborhood on which all subsequent equalities hold. Condition(v) is about sections of certain integral quotient sheaves on one neighborhood; the passage from that condition to stabilization of arbitrary coherent submodules is the unproved step. I have not disproved that abstract implication.

I reopened Siu's 1969 paper and visually read printed page483, Theorem1. It concerns a Stein compact subset of a possibly nonreduced complex analytic space, with noetherianity characterized by finiteness of the connected components of its intersections with analytic subvarieties defined near it. It is not stated for arbitrary ringed spaces with condition(v). The theorem and Frisch's semianalytic case establish analytic special cases, but they do not supply the omitted abstract argument merely by citation.

Recommendation: class **C**, explicitly separating the established analytic specialization from the abstract criterion whose proof has not been verified in this run. The corresponding problem MP-SA18-11036 already handles the distinction more carefully and should be kept consistent. A complete proof from precisely the written condition(v) would remove this audit limitation; a counterexample is not claimed.

Actual searches included both search engines and the exact queries retained in `research/root_audit_web.json`. No exact published abstract lemma was identified in those searches. Search results on noetherian schemes and analytic spaces have stronger hypotheses and were not treated as resolutions of the ringed-space statement.

### 2. CL-SA18-11065: class A is supported by XII Remark1.6

I reopened the primary SGA3 XII re-edition. **Remark1.6, PDF page3, printed page121, original page184**, states the existence of a smooth affine group over a DVR with generic fibre G_m and special fibre G_a. Thus class A is justified for the manuscript's existence assertion. XII1.7 and XII1.10 alone would only provide contextual support concerning ranks and maximal tori.

The explicit group law `x*y=x+y+3xy` on `Spec Z_(3)[x,(1+3x)^(-1)]` remains our reconstruction. It is not written in Remark1.6. The parent had already identified the separate correction from “proved there” to an asserted existence statement on the manuscript page. Add Remark1.6 to the claim's exact publication locator and preserve the reconstruction boundary.

### 3. CL-SA18-11110a/b: mathematical results are sound; literature classification needs qualification

The literal lattice and the editorial replacement are mathematically different examples. The current two class-B assignments cite our 2026 diagnosis/reconstruction plus Poincaré complete reducibility. Those facts do not, by themselves, establish an exact later literature development of either lattice statement. The literal product observation uses classical algebra; the recognition of the error in this particular transcription is this run's check. The intended nonprojective-extension existence claim requires an exact historical existence reference if its class B is meant as a documented fate.

The parent should preserve both proved conclusions, qualify the B classification unless an exact literature match is supplied, and make the origin field of the alternative explicit: **author's existence goal; present editorial construction**. MP-SA18-11039 already distinguishes the two examples in its prose. No alteration of the literal transcription is warranted.

## Independently confirmed mathematical checks

### R1–R5: correspondences, configuration spaces, quadrics and cones

I checked the degree/order conventions and the stated qualifications in the correspondence argument. The bipartite graph excess rank is the cycle rank, with Euler/top-Chern classes arising before any replacement by an Euler characteristic. The configuration argument's graph count and the sorted zero-sum cone's positive gap-coefficient decomposition are consistent. None supplies a new general standard-conjecture theorem.

The two middle ruling classes on a smooth split even-dimensional quadric have the stated parity-dependent intersection matrix. Their difference has square `(-1)^nu 2[pt]`. The punctured-cone groups agree with the Gysin sequence, including the Z/2 term in the odd-dimensional-quadric case. The projective-cone shift and its extra hyperplane factor in products have been kept distinct from the local-support shift. The affine quadric's topological model as a tangent bundle gives the stated signed compact-to-ordinary middle pairing. The ramified base change `t=s^2` indeed kills the quadratic monodromy while retaining the stated weak family hypotheses, so those hypotheses alone cannot force nontrivial monodromy.

### R6: nested tori do not have the claimed general Weyl-subquotient relation

For the diagonal maximal torus D in SL4, the one-dimensional R has cocharacter `(3,1,-1,-3)` and the two-dimensional T is the kernel of `(1,2,-7,4)`. The dot product is zero. The character is primitive in the SL4 character lattice, since the differences from its fourth entry have gcd1; hence T is connected. Both R and T have distinct coordinate weights, so their centralizers equal D.

Any normalizer therefore acts through S4. The stabilizer of the line generated by R's weights has order2, given by reversal. The stabilizer of the line generated by T's defining character, modulo the all-ones character, is trivial: its entries sum to zero, eliminating an additive shift; primitivity permits only a sign, and the negatives do not form the same multiset. Thus W(R)=C2 and W(T)=1. The maximal-T repair follows from conjugacy of maximal tori inside the connected centralizer of R. The publication repeats the broad statement but its proof uses maximality; the existence of a publication does not validate the broad form.

### R8: augmentation filtration and degree two

The restriction of GW(F)→W(F) identifies the rank-zero ideal J with the even-rank ideal I: the kernel is generated by the hyperbolic plane h of rank2, and subtracting half the rank times h produces the unique rank-zero representative. This is multiplicative, so it identifies the powers and their successive quotients.

The degree-two Stiefel–Whitney term of `(<a>-1)(<b>-1)` is the cup symbol `(a)(b)`. The real-place binary-coefficient argument recovers the number of negative squares only when the rank coordinate is retained. The full ungraded Clifford-algebra example correctly shows that a raw relative Clifford class is not automatically the normalized second Stiefel–Whitney invariant.

I independently reopened **Milnor1970 Theorem4.1, printed pages331–332**, and checked that it expressly proves the degree-one and degree-two K-theory-to-Witt-graded maps bijective. Consequently the root's two-step explanation in CL-SA18-11085 is correct: Milnor supplies that identification, while the separate Merkurjev theorem identifies the degree-two symbols with Galois cohomology. I did not independently reopen Merkurjev in this supplementary audit, and do not record a new verification event for that source.

### R9: the RP2 counterexample and the repaired equivalence

For the constant C structure sheaf on RP2, coherence follows from locally constant finite matrices and all stalks are fields. Coherent modules are finite local systems. Both representations of the order-two fundamental group have H1=0: their cellular differentials are respectively `(0,2)` and `(-2,0)`. The sign system is nonzero with no global sections. Thus every hypothesis of the main Lemma A is met and its equivalence conclusion fails.

The marginal variant adds different hypotheses and is not refuted by this example. The repair using global generation is valid: quasi-compactness makes the global generating sets finite, coherence gives a coherent kernel, a second finite generating set gives a global finite presentation, and H1 vanishing gives the needed exact sections functor. This checks the categorical argument and its consequences for stalk flatness and coherence of the global ring.

### R10: literal torus, alternative torus, and dimension error

The literal lattice contains `ik e2` after subtracting its first generator from its fourth, so it is a product of elliptic lattices. In the manuscript's proposed proof, a lattice vector with zero first coordinate invalidates the inference from that coordinate.

For the different lattice generated by `(1,0),(i,0),(0,1),(k,i)`, with k real irrational, projection onto the second coordinate has elliptic kernel and quotient. A complementary elliptic line would give two real-independent projected Gaussian integers `z=c+id` and `z'=c'+id'` and force `k(dc'-d'c)` to lie in Q(i). The integer coefficient is nonzero, so k would be rational. This contradiction, together with Poincaré complete reducibility, proves nonprojectivity of the replacement. The determinant and independence hypotheses are correct.

For the dimension example, the two minimal primes of `k[x,y,z,w]/(xz,xw)` are `(x)` and `(z,w)`. After the stated semilocalization, both components have dimension2 and both retained maximal primes have height2, while the component `(z,w)` has a saturated chain of length1 ending at Q and the other component gives a length2 chain there. Essential finite type over a field supplies catenarity. The counterexample has all the weaker printed assumptions and pinpoints the missing componentwise equicodimensionality. The parameter-ideal repair of the local height argument is also valid; generating the maximal ideal itself by dimA elements would be false.

### R11: coherent-ring elimination counterexample

The coherence proof for the infinite product of copies of `k[[u,v]]` is sound. Over each regular local ring of dimension2, the kernel of a finite row is finite free of uniformly bounded rank; padding bases produces finitely many generators for the product kernel. This proves coherence by the finite-row criterion and does not assert that arbitrary products of coherent rings are coherent.

The coordinate contraction `(u-vT,v^n)∩k[[u,v]]=(u,v)^n` follows from the explicitly given truncated-power-series substitution. The reverse inclusion follows from the finite geometric-series identity. Coordinate idempotents lift each individual polynomial witness to the product ring, so the projection of the global contraction onto coordinate n is exactly `(u,v)^n`. A fixed finite global generating set would bound the minimal generator numbers n+1, an impossibility. No uniform bound on the degrees of the individual idempotent-supported lifts is needed. Thus the one-variable counterexample and the degree-zero obstruction are valid.

## Merge decisions

I agree with the parent's clarification: root SA18-11028 is an operation-level comparison and remains distinct from the direct hyperplane item16032; root11029 is a representation-level comparison and remains distinct from16029; root11030 is the earlier run's idempotent-completion construction and remains distinct from the Karoubi reused leaf16107. Appropriate links should connect them. Root11001 and root11057 are genuine overlaps with16024 and16069 respectively.

The parent is separately fixing EGA IV.1 versus IV.2 references and the exact SGA3 XIV containment locators. This audit does not duplicate those work items or represent their completion as mine.

## Audit evidence

Actual supplemental query requests, opened URLs, exact locators and access limits are in `research/root_audit_web.json`. Supplemental check events are in `root_audit_CHECK_EVENTS.tsv`; they are kept separate from the completed package's314 events to avoid silently changing package counts. The serialization script and its output are retained as `scripts/record_root_audit.py` and `outputs/root_audit_counts.json`. All mathematical judgments above were made individually; the script only records them.
