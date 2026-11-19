# Mathematical checks for cotes III–V

Checks performed on 19 November 2026 by GPT-6 Astra Pro, child run cotes_156_3_5. These are ordinary mathematical arguments and explicitly identified finite computations. No proof assistant was run. A source statement merely read is not classified as a proof check.

## III: cut reconstruction and its boundaries

**C-SA21-3-001.** On {a,b,c}, let compatibility be reflexive and let the only distinct compatible pairs be a–c and b–c. Both singleton cuts are permitted. Their compatible complements are both {c}. The proof step selecting a point of one cut compatible with the other is therefore unavailable from these data. This does not refute a strengthened network system introduced elsewhere.

**C-SA21-3-005–007.** The on-page reconstruction proof fixes a comparable oriented pair and uses common upper and lower bounds to compare other pairs in one bounded interval. Inside that interval, its four-point lemma is a direct consequence of transitivity. For distinct a,b, density makes comparability equivalent to existence of a strict intermediate point. For a<b<c, the selected components for cuts {a,b},{b,c},{a,c} are respectively L_{>b}, L_{<b}, and (a,c). The first two are disjoint; their intersections with (a,c) contain points of (b,c) and (a,b), respectively. Thus the common endpoint of the unique disjoint pair is b. The local strict-cone assumptions are unused by this reconstruction argument. This is a targeted proof check, not a complete axiom characterization of possible cut relations.

**C-SA21-3-004,019.** For a chain of n internal cuts without ambient endpoints, there are two end rays and n−1 internal gaps. For a nonempty n-component moderated subset, its complement has n−1 internal interstices and either zero or one interstice at each end. Empty input must be treated separately. The finite output enumerates these cases but is not being used to infer the formula for arbitrary n.

**C-SA21-3-012.** Let A={0}∪{1/n:n≥1} in [0,1]. Any finite union of closed intervals and points containing A must contain a nondegenerate interval beginning at 0: otherwise finitely many closed components separated from 0 could contain only finitely many of the points. Inside that interval choose a closedly separated open gap between 1/(n+1) and 1/n. Removing that open gap preserves a finite closed-interval union containing A and makes it smaller. Thus no least such hull exists. The rational example in the code supplies exact sample endpoints; the argument is not based on numerical convergence.

### Two abstract tronçon counterexamples (C-SA21-3-015)

Let L=Q×{0,1} and define x≤y iff x=y or the first coordinate of x is strictly smaller. This is a partial order. Finite sets have common strict lower and upper bounds by choosing smaller/larger rational coordinates. Between distinct comparable points choose an intermediate rational coordinate. A nonempty strict upper cone is another such ordered set over an open rational ray; it is downward directed since the minimum of two coordinates still lies strictly above the cone threshold, allowing an intermediate rational lower bound. The dual assertion holds. Iterated strict upper/lower cones correspond to nonempty rational intervals/rays and have the same properties. Every generating strict interval/ray is a pullback of an ordinary rational interval/ray. Consequently twin points (q,0),(q,1) have exactly the same neighborhoods. Their common closure is the two-point fiber, an irreducible closed set with two generic points. Both T0 and sobriety fail.

Let L=R² and define x≤y iff x=y or x1<y1 and x2<y2. Antisymmetry and transitivity are immediate; coordinatewise minima minus1 and maxima plus1 give common bounds. Coordinate midpoints give density. Strict upper cones are open quadrants; two points in a quadrant have a common lower bound still in that quadrant by taking coordinate midpoints between its threshold and their coordinatewise minima. Dual arguments and the same construction in open rectangles establish recursive cone stability. Its strict order intervals are open rectangles; these form exactly a basis of the Euclidean topology. Thus the canonical topology is Hausdorff and all points are closed. The points (0,1),(1,0) are incomparable. This verifies every displayed tronçon hypothesis; the earlier tentative coordinatewise-weak-order example is discarded.

**C-SA21-3-020,024.** Take the horizontal sum of two four-element Boolean algebras, identifying only 0 and1; declare compatibility precisely within a block. This is a partial Boolean algebra, every pair of comparable elements is compatible, and complementary elements stay in their block. Atoms from different blocks have meet0 in the underlying order, though they are not compatible. Taking closure to be the identity satisfies the stated closure axioms; all elements are clopen, so universal compatibility of clopens fails. These are abstract-algebra counterexamples only, not claims about a realized Mod(L).

**C-SA21-3-022,023.** The four Boolean input cases verify X∨Y=X+Y−XY in characteristic2. In a principal ideal below A, relative complement is A∧X′ and relative closure is A∧cl X; distributivity in each compatible Boolean block gives involutivity, extensivity, idempotence and preservation of compatible joins. Compatibility is retained because the axiom applies to the finite family containing A and the relevant elements. This checks the restriction proof under the explicitly strengthened finite-family axiom.

**C-SA21-3-026–027.** In R a single generator [0,1] produces a Boolean algebra with two atoms: [0,1] and its complement. The five boundary-adapted pieces are not all atoms of that generated algebra. More generally, atoms of an algebra generated by finitely many sets are the nonempty membership-vector classes. A boundary subdivision gives a finer compatible algebra; equality requires different subdivision pieces to have distinct membership vectors. This is our refinement, not a correction made to the ink.

## IV: representations and orthogonality

**C-SA21-4-003.** The circle stratified by a point p and its complement has closed strata {p},S¹. The family {S¹} is a set-theoretic subfamily but loses the original residual S¹ minus p. All manifold/density/local-finiteness hypotheses hold. The manuscript’s correction to lower subfamilies is necessary.

**C-SA21-4-011–012.** The family A_n=[0,1/n], n≥1, is closed under pairwise intersections, and every residual A_n minus ⋃_{m>n}A_m is nonempty. Their union omits0, so residuals do not partition the support. Every point needs a minimal containing member (β in V), or a well-founded membership order. Once such a member exists, the intersection/saturation conditions imply it is least and the residuals partition the support. The repaired condition is expressly added in V.

**C-SA21-4-026–028.** In M3 all joins exist, every element is a join of completely join-irreducible atoms, and compatibility is universal. Yet the atoms below a∨b are {a,b,c}, not {a,b}. Thus C1+C2 (even C3) do not turn joins into unions. For the converse subset-family claim, {∅,{a,b}} satisfies bounded-union closure, least containing members and nonemptiness; A_a=A_b, so the point-to-irreducible map is not injective. These exact finite assertions are enumerated by the code. Completely join-prime generators fix the first defect: p≤∨F_i implies p≤F_i for some i. A separating family fixes the second. VI scan12 explicitly adopts the former strengthening.

### Full seven-element figure certificate

This model is compared with Hua2026 §79, but the following figure-axiom check was performed independently in this run. Let M have vertices v0,v1,v2,v3 and edges e0,e1,e2, ordered by incidence v_i<e_i and v_{i+1}<e_i. Compatibility means existence of a common upper bound. Figures are compatible lower ideals of M. They are exactly the empty set, four singleton vertices, three adjacent vertex pairs, and three principal edge ideals: eleven figures.

Compatibility is reflexive, symmetric and hereditary under passage downwards. A family bounded by a figure has its union as join, giving C1. Each principal ideal is completely join-prime, and every figure is the union of its principal ideals, giving C2 in the stronger sense as well. Pairwise-compatible figures have compatible union, giving C3. The incidence poset is comparison-connected, hence the cross-component condition C4 holds vacuously. Every principal ideal has height at most1. These properties are checked over every relevant finite tuple/subfamily in `computations.py`; the output prints the figures and all closure sets.

Orthogonality is compatibility with no common lower element. The only distinct orthogonal pairs are adjacent vertices. Biorthogonal closure has exactly six fixed subsets:

∅, {v1}, {v2}, {v0,v2}, {v1,v3}, M.

For A={v0,v2}, B={v1}, C={v2}, B∨C=M, so A∧(B∨C)=A while (A∧B)∨(A∧C)={v2}. Distributivity fails. Taking subdivision to be equality verifies the subdivision requirements used at this stage by direct reasoning: restriction and extension are identities; a compatible gluing is the same original figure. This last sentence is a manual axiomatic check, not an executed formal certificate. No claim is made for any later strengthened moderation axiom.

The separately constructed five-cycle model has five vertices, five adjacent-edge elements, sixteen figures and twelve closed supports. Its explicit distributivity witness appears in the same output. It establishes the same negative conclusion without requiring the smaller model. Neither finite model proves that every ortholattice is realizable by these axioms.

**C-SA21-4-033.** For symmetric disjointness, A↦A⊥ is antitone and A⊂A⊥⊥; hence triple perpendicular equals single perpendicular, and biorthogonal closure is idempotent. Closed subsets have intersections as meets and closure of unions as joins. Irreflexivity yields A∩A⊥=∅; the union has full closure. This proves orthocomplementation, not distributivity.

**C-SA21-4-039.** In the two-element chain, the two nonempty ideals have the same empty orthogonal subset because compatibility is total and both contain the minimum. They therefore have equal virtual support despite proper inclusion.

## V: admissible families and topology

For an admissible family, let A_x be the least member through x. Define x≤y iff x∈A_y. Reflexivity and transitivity follow directly from leastness. Its equivalence classes are the residuals, and its principal lower sets are exactly the distinct family members. Conversely principal lower sets of any preorder have this property. This checks the set-family/preorder translation, including arbitrary cardinality. Lower subfamilies correspond to closed induced subspaces; refinement is monotonicity of the support inclusion. Infima are intersections of the restricted preorders. Infinite infima require the initial structure in Alexandrov spaces, not an assertion that an arbitrary ordinary initial topology is Alexandrov.

**C-SA21-5-008.** Exhaustive enumeration on L={a,b} gives seven admissible figures and five elementary figures. Their comparison graph has three components: { {{a}}, {{a},{a,b}} }; { {{b}}, {{b},{a,b}} }; and the isolated figure {{a,b}}. Thus the connectedness assertion is false. The proposed external product of {{a}} and {{b}} produces {{a},{b},{a,b}}; its top residual is empty, so it is not admissible. All input figures and their disjoint supports are checked.

**C-SA21-5-020.** Let F={{a,b}}, G=G′=∅ and F′={{a},{a,b}}. Both families are admissible; their supports coincide and the preorder of F′ refines the indiscrete preorder of F. Every old outside closed stratum is retained. Nevertheless the residual of {a,b} shrinks from {a,b} to {b}, and the map of strata has two preimages over the old single stratum. Thus condition d does not imply b or c. This gap is distinct from the author’s later explicit counterexample to leastness.

### General least-extension theorem (C-SA21-5-023–027)

Let T be closed in (S,τ), U=S minus T, and σ finer than τ restricted to T. Consider subsets X satisfying: X∩U is closed in U; X∩T is σ-closed; and clτ(X∩U)∩T⊂X∩T. Arbitrary intersections preserve all three conditions because closure is monotone, and finite unions preserve them because closure preserves finite unions. These subsets therefore form the closed sets of a topology. They are equivalently A∪B with A τ-closed in S and B σ-closed in T: the forward expression uses A=clτ(X∩U), B=X∩T; the reverse direction follows from A closed and B⊂T.

This topology is finer than τ and induces σ. Any finer extending topology must make every A and every B closed, because T stays closed and its induced topology is σ; hence it must make A∪B closed. The constructed topology is least. Its closure of X is clτ(X∩U)∪clσ(X∩T), by the preceding closed-set description and minimality. In particular all subsets of U keep their old closures. Conversely preservation of those closures, together with the prescribed induced topology on T, determines all closures by the finite-union law. This proves the corrected characterization. Replacing the union in the last displayed formula by an intersection makes even the closure of a nonempty singleton fail extensivity.

For original finality, a τ*-closed X whose trace on T is τ|T-closed is τ-closed because X=clτ(X∩U)∪(X∩T). In the Alexandrov case the old relations ending in U are retained, the order on T is replaced by σ, and no relation starts in U and ends in T. This yields the exact poset replacement construction and its extension property.

**C-SA21-5-026.** The author’s three-point counterexample is recomputed on all eight subsets. Original τ identifies u,a and puts both below b; T={u,a}; σ is discrete. The least extension retains u<b and a<b. The alternative retaining only a<b is finer, induces σ on T, has the same induced topology on U={b}, and recovers τ by the stated finality test. Its closure of {b} is {a,b}, while the least extension’s is all of S. The ambiguity in the drawn arrow is not resolved without scans.

**C-SA21-5-029.** For the canonical replacement K→I, fibers outside the replaced lower ideal are singleton. The inverse image of ↓i for i outside that ideal has greatest element i, because every lifted j′ in it satisfies j′≤i by construction. Hence it is contractible. Within the ideal the inverse image is exactly the given one. The Quillen comparison applies to these principal-ideal nerves. It does not supply an interpretation of every possible “universal weak equivalence” phrase on the page.

## Scope limits

The geometrical pseudodisk examples are not specified sufficiently here to reconstruct a complete countermodel with all later axioms. The two-order minimality problem is left open. No claim that a source was formalized follows from an author’s report or from reading Lean text. The check-event table distinguishes this from executed Python certificates.

## Named refinements and scoped obstructions

The following identifiers name the precise surviving conclusions of checks already given above. They are not additional claims attributed to the manuscript, and they do not introduce unproved repairs. Existing positive refinements retain their claim IDs: **C-SA21-3-027** (finite Boolean membership atoms), **C-SA21-4-027** (join-prime representation), **C-SA21-4-035** (valid nondistributive figure countermodels), and **C-SA21-5-027** (least topology extension with preservation of outside closures). These are the corresponding refined-statement IDs in the event ledger.

### R-SA21-3-001

**Scope restriction for C-SA21-3-001.** From a reflexive symmetric compatibility relation alone, a finite compatible cut T is not determined by C(T)={x outside T: x is compatible with every t∈T}. The three-point model above establishes the failure. No general positive repair or sufficient strengthened network axiom is proved here; the model does not purport to satisfy a later axiom system not present in that assertion.

### R-SA21-3-015

**Negative answers within the displayed abstract-tronçon axioms.** Such a tronçon need not have a T0 or sober strict-interval topology, and a Hausdorff strict-interval topology with closed singletons does not force total order. The two fully checked infinite models above establish these separate conclusions. No necessary-and-sufficient replacement condition for T0, sobriety or totality is claimed.

### R-SA21-3-020

**Abstract obstruction, with the geometric question retained.** In an abstract partial Boolean algebra, the existence of an underlying-order meet does not imply compatibility: atoms in different blocks of the horizontal sum have meet0 and are incompatible. This refutes only the extension of the proposed criterion to all partial Boolean algebras. It does not settle the criterion for a specific tronçon realization Mod(L).

The false substatement addressed by this check has the explicit ledger anchor **C-SA21-3-020#abstract-generalization**: “In every partial Boolean algebra, existence of a meet implies compatibility.” The manuscript's more specific geometric question is not marked as refuted by that example.

### R-SA21-3-024

**Abstract closure-algebra obstruction.** Identity closure on the horizontal sum of two Boolean blocks satisfies the closure requirements checked above, makes every element clopen, and leaves cross-block atoms incompatible. Thus those abstract assumptions alone do not imply universal compatibility of clopens. No countermodel for a separately specified geometric realization, and no new sufficient extra axiom, is supplied.

The scoped false substatement has ledger anchor **C-SA21-3-024#abstract-closure-generalization**: “The displayed abstract partial-Boolean closure assumptions force every clopen element to be compatible with every element.” This scope is narrower than any unverified statement about all intended geometric realizations.

### R-SA21-4-028

**The exact injectivity qualification already used in the check.** Let a family F of subsets of M have a least member A_x containing each x. Then x↦A_x is injective if and only if F separates points. More precisely, A_x=A_y if and only if x and y belong to exactly the same members of F. Indeed every member containing x contains A_x; conversely membership in both A_x and A_y forces the two least members to coincide. This is the separation qualification already recorded in C-SA21-4-028, not a new theorem repairing every other part of the representation package.

### R-SA21-4-039

**The author's valid obstruction to strict support separation.** C1–C4 with identity subdivisions do not imply that every proper subfigure has a different virtual support. The two nonempty ideals of the two-element chain have the same empty cosupport. No strengthened universal separation theorem is proved here.

The false withdrawn substatement has ledger anchor **C-SA21-4-039#withdrawn-universal-separation**: “Under C1–C4 and identity subdivisions, every K<F has supp(K)≠supp(F).” The record C-SA21-4-039 itself states the valid obstruction and is checked as such, not refuted.

### R-SA21-5-008

**Two negative conclusions for the literal set-family construction.** On a two-point underlying set, the five elementary admissible figures have three comparison components. The transcribed external union product of the two singleton figures contains {a},{b},{a,b}, with empty residual for the last member, so it is not admissible. These refute the universal connectedness claim and the literal union construction. No alternative product or restriction restoring connectedness is proved; a possible different reading remains an ink question.

### R-SA21-5-020

**Failure of the common-closed-stratum implication.** Retaining every old outside closed stratum does not by itself preserve the outside residual strata or make the outside target map bijective. The already checked example F={{a,b}}, F′={{a},{a,b}}, G=G′=∅ has retained closed support and changed residual. No new sufficient strengthening of condition d is claimed. This obstruction remains distinct from the later leastness counterexample.

### Existing corrected least-extension statement and its withdrawn target

The ledger anchor **C-SA21-5-026#withdrawn-four-test-characterization** names the false assertion that the four weak extension tests characterize the least topology. **C-SA21-5-026** records the author's valid counterexample and is independently checked, not refuted. The existing refined statement **C-SA21-5-027** requires preservation of the original closure of every subset of U together with the prescribed topology on T; its proof is already given in the least-extension section above.
