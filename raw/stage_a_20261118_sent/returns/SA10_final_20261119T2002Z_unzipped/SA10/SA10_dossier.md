# SA10 — Espaces stratifiés

## Consolidated dossier, part 1

**Research date: 19 November 2026.** This dossier accounts for all **537 entries** in the supplied index. The five packages contain **207 supplied scan blocks**. Each entry was read with its actual transcription passage and the applicable supplied second-pass changes. The index and navigation programs supplied locators and completeness checks; they did not assign verdicts. The consolidated tables distinguish what Grothendieck writes, what a later source proves, and what this run reconstructs or checks.

The principal result is a more precise division of the programme. The papers contain substantial valid constructions, several promising but incompletely specified reconstruction questions, and a number of statements whose literal hypotheses are insufficient. Later work gives strong results under explicit controlled, conical, smooth or definable hypotheses. It does not make all the manuscript's different notions of tube, germ, deployment, stratification and moderate space interchangeable. The same distinction is needed within the papers: a successful sphere calculation does not prove the general gluing theorem, while a failure of an ordinary constructible-sheaf topos does not show that every category or groupoid diagram loses higher homotopy.

The most consequential corrections concern the ambient meaning of a cone neighborhood; marked data lost by cutting; disconnected overlaps in group amalgamation; reconstruction from only successor strata; pullback of removal sets defined by actual containments; and the missing finiteness needed for generic triviality in the moderate-model axioms. Every counterexample in the proof records checks the relevant hypotheses. Conditional interpretations are labelled as such, especially when a provisional prospace or topos construction has no fixed homotopy model.

## 1. Corpus, chronology and limits of the present part

| Package | Indexed entries | Supplied scan blocks | Mathematical coverage |
|---|---:|---:|---|
| `MPL_150_001-043` | 109 | 41 | Stratifications, conical and cylindrical neighborhoods, cutting, collars and the first internal-category presentation |
| `MPL_150_044-084` | 113 | 41 | Ordered deployments, component indices, heuristic geometric construction, tubular prospaces and flag gluing |
| `MPL_150_085-099+151_001-031` | 93 | 43 | Final flag/cohomology formulas, symmetric simplicial operations, flatness, provisional neighborhood topoi and two-piece reconstruction |
| `MPL_151_032-075` | 109 | 44 | Normal homotopy local triviality, the sphere and gerbes, closed-family/flag reconstruction, pair and triple tubes, base change |
| `MPL_152+120` | 113 | 38 | Word types and plane trees; coordinate axioms for moderate spaces and the final generic-triviality questions |
| **Total** | **537** | **207** | **All indexed entries in this part** |

The `TOPIC.md` orientation covers six cotes. They are all accounted for here, without generating verdicts for the other part:

| Cote | Catalogue description | Catalogue pages | Supplied Pro count in `TOPIC.md` | Treatment here |
|---|---|---:|---:|---|
| 150 | Espaces stratifiés et voisinages côniques / déploiement | 98 | 97 | Full supplied part-1 transcription and indexed notes |
| 151 | Topos stratifié (1981) | 74 | 72 | Full supplied part-1 transcription and indexed notes |
| 152 | Catégorie des types de mots, including plane trees | 12 | 13 | Full supplied part-1 transcription and indexed notes |
| 153 | Analyseurs | 10 | 11 | Other part; only the indexed earlier-run negative-search report is assessed as a report |
| 154 | Système de pseudo-droites | 175 | 174 | Other part; orientation only |
| 155 | Rigidité de catégories tensorielles? | 10 | 11 | Other part; no invented mathematical verdicts |

Cote **120** is not an extra topic folder silently added to the task: its 25 scans and notes are actually included in the indexed mixed package. Cote **121** and the other external cotes are inspected only where the indexed notes make comparisons or links. This is not a consolidation of all their research notes. No Codex transcription or Codex note file is present in the supplied material; the zero counts in `TOPIC.md` agree with that inventory.

The catalogue counts, scan positions, transcription coverage and manuscript foliation are different quantities. Cote 150 has 97 supplied blocks among positions 1–99; the early package omits positions 6 and 11. Cote 151 has 72 supplied blocks among positions 1–75. The count of 13 for cote 152 should not be forced to agree with the catalogue's 12 by suppressing a leaf. Covers, reused sheets, cancellations and uncertain manuscript numbers remain documentary items in the entry table.

The title in 150 and the retrospective passage in the *Esquisse* support a period of renewed work in **December 1981–January 1982**. They do not date each undated sphere or gerbe passage to December alone. Reused printed supports in 151 carry a **6 December 1990** date; an electronic print line in the mixed package carries **19 May 1982**. Those are evidence about their respective supports, not permission to date every mathematical paragraph in a folder. The uncertain title date in 120 remains governed by the supplied second pass. [SA10-6; SA10-468; SA10-815; Esquisse1984, §5]

For the later programme, the primary *Esquisse* is dated January 1984. Mumford's letter of 24 May 1984 documents circulation by that date; it does not establish the first circulation date. Its first print publication is in the 1997 Cambridge volume. Grothendieck's letter to Brown of 5 May 1982 is separate evidence for the earlier strata/tubes/junctions programme. The precise references and historical limits are in `parts/p1/primary_audit_global.md`.

## 2. Reading cote 150 in its own terms

### Stratifications and their order

The initial language is an indexed family of closed pieces and their exact open strata. The order convention is upper-set-open: specialization points toward larger strata. This matters for the variance of diagrams and for any comparison with another author's Alexandrov convention. A quotient preorder, a partial order after a separation condition, and an arbitrarily chosen order making a map continuous are different claims.

The closed-family intersection equation is fundamental:

\[
X_i\cap X_j=\bigcup_{k\leq i,j}X_k.
\]

Together with local finiteness it supports the partition and quotient arguments. It does not, merely with nonempty closed pieces, make the labeling order faithful. Two comparable labels with the same nonempty closed piece give the elementary obstruction. Nonempty exact strata repair the argument; the density hypotheses in the surrounding discussion supply that condition in the stated setting. The dossier therefore separates a false isolated implication from the density-qualified statement that is valid. It also keeps pullback of the closed-family equations distinct from preservation of effectiveness, density or order reflection. [SA10-C001–SA10-C008; `parts/p1/proof_checks.md`, §1]

The order-theoretic cautions recur later. Boolean structure of each comparable interval does not make the whole incidence poset a Boolean lattice and does not create a global meet. The five-element example with two minima, two middle elements and one maximum has Boolean intervals, but the two middle elements have two incomparable common lower bounds. The correct meet calculation takes place inside a chosen interval. In the final 151 package, a rank function is assumed rather than proved. The second-pass general criterion for its existence is also too weak: equal chain lengths in comparable intervals do not control every cycle in the undirected Hasse graph. That latter error belongs to the checker, not to an assertion that Grothendieck made. [SA10-C043; SA10-C351]

### Absolute cones, ambient cones and uniform germs

For a map \(f:L\to Y\), the absolute conical object is a mapping cylinder with a radial action, fixed base and designated outer boundary. Its deformation retraction and its relative annular/collar formulas are valid. The point requiring care is the passage from this equipped space to a neighborhood embedded in another space \(X\).

The literal requirement that the cone be a neighborhood of \(Y\) does not ensure the asserted ambient frontier formula. A horizontal interval with a vertical branch attached halfway along it gives a compact Hausdorff counterexample: the interval is a cone neighborhood of its initial endpoint, but a contracted interval has the branch point in its ambient frontier as well as the expected radial endpoint. Requiring the cone minus its designated outer boundary to be open in \(X\) repairs the frontier argument and the corresponding collar/shrinking equivalence. This is a mathematical hypothesis correction, not an ink change. [SA10-C013, SA10-C014, SA10-C042; `parts/p1/proof_checks.md`, §3]

The germ relation uses **constant positive rescalings**. One may take a common smaller radius for finitely many requirements. An infinite family, or a neighborhood with radii tending to zero over a noncompact link, need not admit one uniform shrink. The ordinary neighborhood germ and this equipped constant-rescaling germ therefore require a comparison theorem before identification. The proofs retain precisely the compactness and finiteness used in each argument. [SA10-21; SA10-29; SA10-33]

### Cutting, marked bases and simultaneous compatibility

The cut-and-attach constructions carry much more than an unmarked space. They retain boundaries, collars, attaching maps, marked subsets and compatibility among radial actions. The text allows a conical marked subset to have extra base points beyond the image of its marked link. A cutting tuple that forgets those marked base points can identify two nonisomorphic marked objects. Keeping each \(Y_i=X_i\cap Y\), with the appropriate containment of the attaching image, repairs the data. Alternatively, an explicitly imposed purity condition removes the extra base points. [SA10-C015–SA10-C024; SA10-C044]

Purity itself must not be confused with a topological closure condition without checking the attaching image. A map from a discrete countable link into \(\{0\}\cup\{1/n:n\ge1\}\), with image omitting the limit point, separates the two conditions. Closedness of the relevant attaching image is sufficient for the equivalence; proper attachment into a Hausdorff base is one familiar way to obtain it. [SA10-C047; SA10-C048]

The strengthening from individual triviality to **one simultaneous trivialization of the marked family** is mathematically necessary. The zero section and the graph of the identity over a real interval are individually trivial sections of a trivial bundle, but meet in one fiber and not in neighboring fibers. A product chart preserving both would preserve their intersection pattern, which is impossible. The manuscript's repeated demands for simultaneous equisingularity and compatible retractions are substantive. They cannot be replaced by a list of separate bundle trivializations. [SA10-28; SA10-34; SA10-228]

### Deployment, flags and the internal category

The recursive presentation removes minimal pieces, equips their boundaries, and passes to a residual stratified space with new collars. Finite induction itself is valid. Existence of the required geometric cone data, independence of the chosen removal filtration, and equivalence of all proposed local/global presentations are additional claims. The pages sketch parts of the intersection verification; they do not close every equivalence-of-groupoids argument.

The later restart organizes deployed strata \(\Sigma_i\), pair spaces and higher flags. Cartesian concatenation is the familiar nerve condition for an internal category. It encodes composition, not automatically a geometric collar or a fibration. The object and arrow spaces have topology, so replacing the result by its finite label poset discards information. In the subsequent ordered presentation, the source, target, local immersion, properness, transversality, boundary and component conditions must each be retained. [SA10-46; SA10-48; SA10-53–SA10-55; SA10-202; Segal1968, §2]

Several earlier notes correctly diagnosed weak axioms, but later additions change the verdict. The weak common-lower-bound condition permits a diamond example with a nonflag intersection; the stronger noncomparability condition later imposed excludes it. The source-fibration argument for the component preorder has a correct variance-sensitive proof using the assumed source, despite a later sentence referring to the target. The manuscript's component argument becomes a partial order only after its additional exclusions; a general category is not retained as the final global index. [SA10-C101; SA10-C117; SA10-237–SA10-240]

## 3. Tubular prospaces and flag reconstruction

The final part of 150 introduces tubular pro-neighborhoods and intersections indexed by flags. The internal cofiltered neighborhood system and the external flag diagram are two separate indexing levels. Shrinking punctured disk neighborhoods illustrate why the distinction matters: their ordinary intersection is empty, while every punctured neighborhood retains a circle's homotopy type.

The pages assert comparisons with strata, restrictions to bands, colimits and a cohomological spectral sequence. A categorical colimit, a homotopy colimit and cohomological descent require different arguments. The notes sometimes supplied “homotopy” where the page wrote only a colimit, or treated objectwise equivalences as enough to identify all attaching maps. The consolidated claims restore the exact statement and record the extra hypotheses needed for a modern realization. [SA10-200; SA10-211–SA10-218; SA10-243–SA10-250]

There are also precise formula defects. The pair-piece covering list on 150/084 omits overlap cases when the two bands meet; the following all-flags system retains them. The boundary formula on 150/085 has a separate mismatch, exposed already by singleton and full-index cases. These are not interchangeable errors, and neither is repaired merely by calling the whole construction a hypercover. Source/target types, the direction of flag inclusions and the treatment of empty flags remain part of the reading table.

For actual locally finite closed covers, cohomological descent has a checked classical framework [Deligne1974, §5.3; SGA4Vbis, §4.1]. For actual open covers and hypercovers, modern homotopy-colimit results provide a different precise framework [DuggerPrimer, Proposition 22.1; DuggerIsaksen2004, Theorems 1.1–1.3]. Those results do not certify that an unspecified pro-neighborhood diagram meets their cover, matching, model and convergence hypotheses. The proof records identify the finite reindexing arguments that can be made directly and leave the genuine comparison obligations visible.

## 4. Cote 151: from categorical tests to the sphere

### Symmetric operations, flatness and covering comparisons

The early 151 leaves include low-degree symmetric simplicial operations, changing cyclic conventions and a proposed extension of Čech-type constructions. The finite relation calculations have been redone. A later presentation of the category of finite sets and symmetric simplicial sets supplies a useful exact comparison, but cannot settle an uncertain exponent or a changing generator convention in this manuscript [Grandis2001, §3 and Theorems 4.1–4.2]. The current historical name in the hypercover discussion is **Cartier**, not Cartan.

One question has a particularly close later theorem. The text asks whether a functor can make every finite-limit comparison epimorphic without preserving those limits. For finite-limit categories and **strong epimorphic comparisons for every finite diagram**, the comparisons are in fact isomorphisms. The short proof doubles a limit cone: the resulting comparison to the kernel pair is the diagonal, hence is both monic and strong epic. This makes the original comparison monic as well as strong epic. In a topos, the relevant epimorphisms satisfy this requirement. The exact later match was checked in Vitale's November 1994 thesis, Proposition 1.4.3 and Lemma 1.4.4, and Carboni–Vitale, Proposition 20, published in 1998. Earlier bibliographical leads are not promoted to an independently checked priority date. [SA10-C248]

The page's reduction of this condition to just epimorphic terminal/product/pullback tests is false. Taking orbits of a two-element group satisfies those tests but can fail an equalizer test. The saved exhaustive finite cases accompany the general orbit argument. Thus this counterexample refutes the proposed reduction, while the full all-finite-diagram question has the affirmative left-exactness theorem and therefore a negative answer to the possibility of such a counterexample. Confusing those scopes would reverse the conclusion of the literature search. [SA10-C247; `parts/p3/proofs.md`, §§5–6; Vitale1994; CarboniVitale1998; Tendas2024]

### The provisional neighborhood and its homotopy interpretation

The notation \(V_{Y,X}\) is introduced provisionally through a neighborhood/topos construction. The pages use it for a two-piece gluing diagram and later for normal homotopy local triviality. A literal pro-object of neighborhoods, a formal neighborhood, a punctured geometric neighborhood, a pro-topos, and an associated shape are distinct objects. The dossier neither rejects every version using a counterexample to one of them nor supplies a missing definition from later theory.

For one precise literal interpretation, the inclusion of a closed set into its neighborhood pro-homotopy system need not be an isomorphism. The Cantor example explains the obstruction: a continuous map from a finite-component neighborhood into the Cantor set has finite image, while a homotopy between self-maps of the Cantor set is pointwise constant. An inverse in that pro-homotopy category would therefore force an impossible finite-image identity. This does not refute a separate shape-theoretic or sheaf-theoretic comparison without matching its definitions. [SA10-C226 and the adjacent neighborhood claims; `parts/p3/proofs.md`]

The ordinary formal-spectrum comparison is similarly precise. In the adic setting inspected in EGA I, completion along the center is supported on that center; deleting all that support leaves nothing. A nonempty punctured object must use another construction. The EGA, SGA and modern formal-space locators are given in the global primary audit; the observation is not a general dismissal of analytic or étale tubular objects. [SA10-4; SGA4I8; SGA4IV9]

### Connected overlaps, normal fibrations and inertia

The group-amalgam formula on 151/031 lacks a connected-overlap condition. A circle with one point distinguished and a small arc neighborhood has connected global pieces but a punctured overlap with two components. A single-group amalgam misses the loop. The groupoid formulation handles the component information under its actual open-cover and basepoint hypotheses [Brown1967, Theorem 3.4]. The later 151/036 passage explicitly assumes the center, complement and punctured tube are connected; it repairs this particular missing hypothesis there. It does not retroactively make the weaker statement on 031 true. [SA10-C232; SA10-614]

Once a pointed homotopy fibration has been constructed, the displayed long exact sequence and its low-degree consequences are standard. In particular, the fiber group maps into the total-space group with kernel given by the image of the connecting homomorphism from \(\pi_2\) of the base. The pages retain this map. A locally trivial link fibration does not generally make it vanish, and the external cote 149 discussion distinguishes local tubular extensions from the map into a global complement. The dossier preserves those different arrows instead of interpreting every meridian as injective. The proposed étale localization or completion remains a self-flagged step, with its prime and characteristic hypotheses unspecified. [SA10-605–SA10-610; SA10-63; SA10-475]

### What the sphere test corrects

The sphere passage has two different conclusions. First, the ordinary category for sheaves constructible with respect to a point and its complementary plane is the one-arrow category; its nerve is contractible and does not recover the sphere's second cohomology. That genuine failure remains. Second, the author withdraws the broader fear that the original diagram of pieces and their punctured overlap has lost the sphere. A suitable homotopy pushout of the two contractible pieces along a circle is the sphere, and the gerbe calculation detects its degree-two class. [SA10-601; SA10-619; SA10-620; SA10-621; SA10-467; SA10-473]

The exact algebra is elementary and has been independently checked in three package reviews. An automorphism of the split extension \(A\times\mathbb Z\), fixing \(A\) and the quotient, is

\[
(a,n)\longmapsto(a+n\alpha,n),\qquad\alpha\in A.
\]

Composition adds \(\alpha\). Hence the automorphism group is \(\operatorname{Hom}(\mathbb Z,A)\cong A\), matching \(H^2(S^2,A)\). Cellular and Mayer–Vietoris checks confirm the cohomology; finite cyclic-group computations check the formula as a reproducibility test. The proof for arbitrary \(A\) comes from the image of the integer generator, not from finite enumeration.

Gerbe descent uses equivalences and transformations between them. A set of equivalence classes or an ordinary one-category of central extensions must not be substituted for the whole gerbe 2-groupoid. The manuscript's weaker assumption \(\pi_2=0\) is enough for the stated degree-two class comparison in a connected CW setting; it is not an identification of every higher morphism. The successful example is followed by an explicit stop in verification and a general expectation. That general expectation remains a problem, rather than becoming a theorem by association with the calculation. [SA10-624; SA10-471; SA10-473; `parts/p4/proofs.md`, §8]

Treumann's pointed-sphere examples provide an exact later comparison between the ordinary exit category and the information retained at exit 2-level [Treumann2009, Examples 1.4 and 1.6]. Lurie's constructible space-valued sheaf theorem and exit/singular comparison require the explicit paracompactness, local singular-shape, conical and ascending-chain hypotheses in the inspected version [LurieHA2017, Theorem A.9.3 and Corollary A.9.4]. The conically smooth stratified homotopy hypothesis has its own category and localization [AFR2019]. These are substantial positive results; none is used to identify an undefined manuscript tube automatically with an exit construction.

## 5. The later closed-family and tube reconstruction in 151

The later restart deliberately works with general topological spaces. The locally finite closed-family equations imply that the exact strata partition the space and that the full closed-piece diagram has the correct set and topological colimit. Empty exact strata can be removed, but that optional reduction is not a standing assumption everywhere in the subsequent formulas. A relative proper/separated map from the disjoint pieces does not make its absolute relation closed in a product when the ambient space is not Hausdorff. The Sierpiński example exposes that distinction. [SA10-C209; SA10-C323; SA10-C331; `parts/p4/proofs.md`, §§1–2]

A finite abstract diagram of closed embeddings can also identify points within one piece in its colimit, even when the indexing poset has meets. The triangle-face example introduces a label switch around a cycle. Every structural map is injective, but the quotient identifies the two labels. An intersection or exactness condition is missing; the existence of meets in the index does not provide it. The finite certificate checks the functor, its order relation and every quotient class. [ `parts/p4/proofs.md`, §3 ]

### Actual containment is not stable under pullback

The removal set \(R_i\) is defined by whether a closed piece actually contains \(X_i\), rather than solely by the fixed index order. Pullback can create new containments or equalities. Therefore the removal set need not commute with base change, even though the original closed-family equations do.

The checked Boolean-diamond example gives two distinct tests. Pullback to one clopen point refutes the removal-set equation. That point lies outside the original tube, so the same test alone does not refute the tube comparison. Pullback to another clopen point makes all pulled-back closed pieces equal: the original tube has empty trace there, but the newly formed tube is the point. This second test really does refute tube base change with the literal definitions, even for a proper clopen immersion. The dossier does not conflate the two counterexamples. [SA10-C359; SA10-C361]

The separate union indexed by a fixed order interval does commute with pullback; its alternative description using actual containment may fail. Likewise, the formula involving intersections of two removed/retained unions is not repaired merely by exchanging one subscript. A strengthened finite example keeps every exact stratum nonempty and still refutes it. These are mathematical limits of the definitions, separate from the scan questions about the written indices.

### Adjacent strata do not supply every sheaf compatibility

The reconstruction from only the successor graph fails for the point–line–plane stratification. Put constant abelian sheaves on the displayed pieces except the line germ at the origin. On that germ take a sheaf whose origin stalk specializes by the identity to the negative branch and by zero to the positive branch. Its stalk and punctured restrictions give valid compatible data on all edges of the successor graph.

If a sheaf on the plane supplied those data, it would be constant away from the origin. A punctured disk is connected, so its sections restrict diagonally to the two line branches. The prescribed specialization, with one nonzero branch and one zero branch, cannot factor through that diagonal. This supplies a full counterexample to the stated category of compatible sheaf families, under the ordinary neighborhood/sheaf interpretation. A differently intended topos `Lim` would need its own definition before applying the example. The omitted nonadjacent or triple incidence data carry the missing compatibility. [SA10-C353; `parts/p4/proofs.md`, §6]

### Open restriction of the literal neighborhood prospace

Proper closed-map neighborhood cofinality has a short correct proof: the image of the closed complement of a neighborhood of the inverse-image center is closed and misses the original center. Its complement supplies an ambient neighborhood. This proof does not repair the separate false containment-defined removal formula.

For open restriction there is a sharper obstruction to the homotopy comparison asked on 151/075. Take the germ of the plane along the whole horizontal line, then remove the origin. It has cofinal punctured-strip stages, all connected and homotopy equivalent to a circle. If one first removes the origin and then forms the neighborhood germ of the punctured line, there are cofinal narrowing strips with two contractible components. The comparison already fails on pro-\(\pi_0\), from a constant two-point system to a singleton system. This conclusion is explicitly about the literal neighborhood-prospace interpretation. Density, smooth strata and a grading hold in the example; an alternative topos or shape construction requires a separate comparison. [SA10-C358; SA10-C367; `parts/p4/proofs.md`, §7]

These failures make the prospective successor-to-pair-to-triple programme intelligible, but do not prove that any particular enlarged list of pieces is sufficient. The problem index records the remaining coherence and functoriality requirements rather than supplying an unproved repair.

## 6. Cote 152: types of words, contour permutations and trees

The short word-type dossier works with marked disks, chords, cyclic orders, contours and plane trees. Several exact finite constructions are valid. With edge reversal \(\alpha\), vertex rotation \(v\), and boundary permutation \(b=v\alpha\), either pair \((\alpha,v)\) or \((\alpha,b)\) determines the other. All boundary cycles must be kept; a general ribbon graph need not have one contour. Isolated vertices require separate data because they have no darts. These are checked in fresh notation rather than used to force a reading of the manuscript's changing rho symbols.

A noncrossing pairing of a single cyclic contour gives a tree, and disjoint chords give a region-dual tree with one more region than chords. The leaf-removal proofs give the universal statements. Enumeration through six edges produces the familiar sequence 1, 2, 5, 14, 42, 132 and checks the permutation calculations. The code does not supply the missing definition of the recursive admissibility rule. [SA10-C402–SA10-C406; `parts/p5/math_checks.md`, §1; Cori1975, I–IV]

Two live rho formulas contradict one another if they use the same identified nonempty edge set. Cancellation would make the edge-reversal involution the identity. Which convention, identification or overwritten line changed remains a scan question. Likewise, contracting one edge requires an induced involution whose treatment of the remaining partner is not defined. The finite examples show why a familiar noncrossing rule cannot simply be substituted. The full category equivalence is therefore unidentifiable at the stated morphism level, despite the valid finite object correspondences. [SA10-C400; SA10-C401; SA10-C404]

The supplied second pass changes the evidential basis of several older remarks: the category adjective remains `isotypique|isotopique`; the uniqueness condition currently reads at most one, which is true though weaker than at most two; and the later revision forgets orientation rather than planarity. Simultaneous reversal of vertex cyclic orders must be distinguished from reversing them independently. These details determine the groupoid and its stabilizers, so are not merely terminological adjustments.

## 7. Cote 120: what the moderate axioms establish

### Coordinate algebra and finite gluing

Cote 120 first specifies families of subsets of finite scalar powers and coordinate-image, inverse-image, relative-preimage and product operations. It then defines maps by their graphs. The identities, composition, inverse graphs of bijections, finite limits and transport of structures can be checked directly. The nullary convention supplies a point without requiring a scalar constant to be admitted. Optional M0 admits the whole scalar line; it must remain distinct from the later compact-model setting. [SA10-C409–SA10-C414; SA10-C442–SA10-C444]

Finite colimits are conditional on finitely many scalar functions separating the set quotient. M6 supplies collapse coordinates and M7 supplies extensions, which suffice for the displayed pushouts. The current main diagram already contains two hooked inclusions. The one-hook strengthening is a separate margin and also has a direct proof. In the abstract proof the prescribed collapse value need not be zero; zero normalization belongs to the real-field example. The strict ind quotient and two-inclusion pushout follow by using cofinal stages with matching induced traces and proving injectivity of the transition maps. Arbitrary ind-monomorphisms are not thereby locally moderate subsets. [SA10-C415–SA10-C423; `parts/p3/p5_independent_audit.md`]

The scalar-object recognition proposal is less complete. A faithful conservative concrete functor, finite limits and embeddings into finite powers of a scalar object give the forward graph description. The converse must say whether it recovers the weak coordinate axioms or the stronger image-stable families. No precise opened source establishes the entire abbreviated converse without those distinctions. [SA10-C413; MP-SA10-202]

### Compactness, constants and separation

In the compact Hausdorff setting, compact graphs are continuous maps. The local-to-global argument uses a finite cover by moderate neighborhoods and a common target stage. The scalar-probe criterion uses the weak coordinate assumptions actually written; it is not necessary to import M11 into that earlier argument.

M11 makes the admitted scalar constants a subfield, but need not make it the whole real field. The real algebraic parameter subfield gives an explicit proper model. Ordinary compactness and definable compactness must also be separated over a noncomplete ordered field [PeterzilSteinhorn1999, Definition 1.1 and Theorem 2.1]. These distinctions prevent the parameter convention from disappearing in a comparison with modern definability.

Two literal claims are too strong. A subset of a compact moderate part need not itself be compact: \((0,1)\subset[0,1]\) is sufficient. A tuple of defining functions for \(Y\) and their products with separating coordinates cannot separate two points inside \(Y\), since all tuple coordinates vanish there. It does separate the complement and distinguishes it from the collapsed class. The explicit endpoint example checks the false stronger wording under all relevant compact semialgebraic hypotheses. The latter issue survives the supplied correction of the axiom range to M1–M7. [SA10-C429; SA10-C433; SA10-C434]

### Why M1–M11 do not already give a tame finiteness theory

The family of **all compact subsets** of finite-dimensional real spaces satisfies the literal M1–M11 block, with optional M0 omitted. Coordinate images, relative inverse images, products and unions preserve compactness; a distance tuple collapses a closed subset; metric extension supplies M7; compact intervals give the local scalar conditions; and restricted field operations and inversion supply M11. The empty-subset case of collapse has an explicit tuple with empty inverse image of its prescribed collapse value. This model contains a Cantor set. Its admission is not evidence that Grothendieck intended every compactum as moderate; it proves that the selected axioms alone do not exclude them.

The Boolean presentation in early cote 121 has additional closure, relative interior, descending rarity and connected-component conditions. The recursion terminating a locally closed decomposition uses those hypotheses. Later 121 drafts add finite and relative triangulation requirements. The all-compact countermodel does not satisfy those extra clauses. Likewise, equality with local completion on a compact space needs a basis of admitted opens; the next page itself warns against dropping that condition. [SA10-477; SA10-480–SA10-485; SA10-C440; SA10-C441]

Modern dictionaries clarify possible models without identifying the evolving drafts automatically. Van den Dries–Miller's geometric-category correspondence and Schürmann's comparison with Nash categories and X-systems have precise field, finiteness and ambient-locality hypotheses. The integer subset of the line is locally semialgebraic at every finite point but fails the corresponding compactification-boundary test. A statement about affine local membership is therefore weaker than one about an entire geometric category. [vdDM1996, §§2–3 and Appendix B; Schuermann2002, Theorem 0.1]

### The final triviality question has three different outcomes

For a single continuous map of compact definable real models, a finite trivializing partition is established. Refining it and deleting its boundaries produces the rare compact exceptional set of the question. Taking the closure of a trivialization graph gives the requested compact relation; the text does not require a single-valued continuous extension over the boundary. A simultaneous marked-subset version also handles the nested test \(Z\subset X\subset Y\times[0,1]\). [SA10-C435; SA10-C437; Coste1999, Theorem 5.22]

This single-map conclusion does **not** follow from M1–M11 alone. In the all-compact model, send ternary Cantor digits to binary digits. This is a continuous map onto the interval. Every interior dyadic fiber has two points, while every nondyadic fiber has one. Any remaining open interval after deletion of a compact nowhere-dense set contains both. Consequently even a set-theoretic product description on the connected component is impossible. The full axiom check and the fiber argument were independently reviewed. [MP-SA10-204; `parts/p5/math_checks.md`, §§5–6]

For finite diagrams, global simultaneous natural-isomorphism triviality already fails in compact semialgebraic geometry. A diagram containing an identity and a parameterized circle rotation forces conjugacy of rotations; their order is invariant, and finite-order and infinite-order parameters occur in every interval. A four-arrow finite poset encodes the same obstruction, with proper arrows. Individual-arrow isotopy is weaker and remains possible. This explains why the unresolved word “essentially” changes the truth value of the question. [SA10-C436; MP-SA10-205]

Finally, the local privileged-partition conjectures in cote 121 use product **open embeddings** upstairs, not explicitly full inverse images of base neighborhoods. The global diagram example does not by itself refute those local quantifiers. Existence of some finite partition, a unique coarsest privileged partition, and compatibility across a proper finite system remain different requirements. [SA10-C439; MP-SA10-208]

## 8. What later work supplies, as of November 2026

The bibliography records the exact result used and separates first documented circulation, a preprint version, online publication and volume publication where the evidence permits. It does not assign a first-circulation date merely because a search found a later PDF.

| Manuscript aim | Checked positive framework | Limit of the match |
|---|---|---|
| Controlled tubes and simultaneous local triviality | Mather's circulated 1970 notes, first printed in 2012; controlled and proper stratified-submersion statements | The stratumwise hypotheses cannot be replaced by ambient smoothness alone; arbitrary topological stratifications are not covered. |
| Conical neighborhoods and resolution | AFT2017, Corollary 7.3.7 and Propositions 8.2.3/8.2.5; smooth-atlas and fibered-corner comparison in ABP2025v2 | These impose specific conically smooth or resolution structures. AFT's adjacent remark warns that the naive continuous analogue fails. |
| Sheaf and higher homotopy reconstruction | Treumann2009; LurieHA2017; AFR2019; the precise two-stratum/vanishing-topos comparison inspected in the p4 source audit | Different coefficient levels and geometric hypotheses; no automatic identification of the provisional manuscript limit. |
| Cohomological versus homotopy descent | SGA4Vbis and Deligne1974; Dugger–Isaksen for actual topological hypercovers | The input must satisfy the corresponding descent or matching conditions. |
| All-finite epimorphic comparisons | Vitale1994 and CarboniVitale1998 | The exact all-finite hypothesis works; the manuscript's three-test reduction does not. |
| Definable generic triviality and extension | Coste1999, Theorem 5.22; AschenbrennerFischer2011, Lemma 6.6 | Specified definable structures and closed-domain conditions; not arbitrary compact families. |
| Compact PL/definable comparisons | Shiota2010, Theorem 2.1 and its complement; Shiota2014; ShiotaII, Supplement and Theorem 4 | Object existence, isotopy of a given map and all-degree relative parameter comparisons are different strengths. |

Shah supplies a precise finite-poset reconstruction theorem: a stratified infinity-topos is recovered as the right-lax limit of its associated toposic locally cocartesian fibration. Its fibers are infinity-topoi and its pushforwards are accessible and left exact; bounded coherence is not required. This gives a substantial established formulation of the gluing programme, first posted in October 2021 and published in 2026. Matching the manuscript's particular tube data with this gluing object remains a separate comparison. [Shah2026, Definition 5.11 and Theorems 5.13/5.22; SA10-C354; `evidence/root_reference_audit.md`]

The 2026 update also includes the inspected second version of the Albin–Banagl–Piazza preprint, dated **5 November 2026**, following its 2025 first submission. Its smooth-atlas, fibered-corner and Thom–Mather comparisons provide a particularly useful contemporary dictionary. They do not prove that the weak abstract deployment axioms in 150 already satisfy those geometric hypotheses. [ABP2025v2, Theorems 2.10, 2.13 and 5.2]

The *Esquisse* asks for comparison of isomorphism spaces and their homotopy types, not only a bijection of homeomorphism classes. The compact Hauptvermutung and isotopy results give substantial affirmative content. The precise higher statement would still need compatible relative straightening over every parameter simplex, with the already prescribed faces and marked subobjects fixed. The dossier does not infer that all of those extension conditions follow from a theorem about one map. Noncompact comparison also requires the standard representatives and boundary collars actually used in the source. [SA10-17; SA10-486–SA10-492; SA10-C264]

The literature classes are evidence categories, not originality rankings. **A** would require an exact later result in Grothendieck's published work; a restatement of a programme in the *Esquisse* is insufficient. **B** records a matched established result, with its scope. **C** states the precise partial development or remaining qualification. **D**, when used, is only the outcome of the recorded bounded search. **E** includes elementary consequences of already available topology, category theory and algebra; it does not claim that the manuscript's exact notation had appeared earlier. **F** means the claim cannot yet be identified precisely from the available text. An exact modern theorem, a useful analogous framework and a failed search are never counted as the same evidence.

## 9. What the earlier notes got right and wrong

The notes were especially useful in locating unproved transitions, preserving cross-folder pointers, testing the sphere and the moderate axioms, and distinguishing individual triviality from simultaneous compatibility. Several explicit earlier-run examples survive independent checking. They are still identified as those runs' ideas rather than quoted as authorial claims.

The major corrections fall into five groups:

- **Superseded readings.** The current two hooks, the weak M1 subscript, M1–M7, Cartier, the missing word `discrète`, the `½-simpliciales` prefix, and the revised orientation wording remove or alter older objections. The supplied second-pass reading is retained even when the resulting formula is mathematically ill-typed.
- **Overstated scope.** A colimit was sometimes strengthened to a homotopy colimit; a modern compact theorem to a complete tame-category equivalence; a successful example to a general reconstruction; or an approximate catalogue date to a precise leaf date.
- **Missing hypotheses.** Ambient interior, marked base data, a closed attaching image, simultaneous products, nonempty exact strata, a connected overlap, an admitted-open basis and genuine finite-diagram conditions each affect a concrete argument.
- **Incorrect repairs.** Replacing one subscript does not fix the removed-union intersection formula. The first base-change counterexample refutes the removal set but needs a different pullback point to refute the tube. The second-pass rank criterion needs a Hasse-cycle condition beyond comparable intervals.
- **Unverified contextual status.** A named project register's “Proved” or “Refuted” label is evidence of what that earlier note reported. It is not a proof in these manuscripts or an independently verified result of the present dossier.

The reading table distinguishes active mathematical alarms from old alarms explicitly closed by the supplied second pass. No image reading was decided here. A mathematically forced alternative may be an authorial slip, an omitted hypothesis, or an error in the transcription; only the next scan-based review can distinguish them. The line and scan locators preserve that task without silently changing the diplomatic text.

## 10. Links, source access and the separate project leads

The archive links connect concrete passages: the conical/cylindrical constructions in 150; the analytic and flag language in 147; the normal/tubular and inertia comparison in 149; the 1975 recollement/cone letter; the different algebraic and conformal occurrences of “shadows”; and the changing moderate presentations in 120 and 121. A shared noun is not a mathematical identification. External public French transcriptions were read as text witnesses, and their footer-to-scan convention was checked. They do not authorize new claims about the ink.

One easily misdirected citation is now resolved: the “Str∞ p. 84” reference on **151/059** points to **cote 147, official scan 177, public-witness footer 176, author page 84**. The preceding filtered-normal-bundle formula and following canonical fundamental-groupoid comparison confirm the match. The exact endpoints are recorded in the link table and `parts/p4/integration_notes.md`.

The published-work links were checked at the relevant EGA I, SGA4 I/IV/Vbis, formal-moduli Bourbaki, *Esquisse* and correspondence locators. The source audits distinguish an established theorem from a programme, an exercise or a retrospective historical statement. The SGA ind/pro results are invoked with their finite-limit, finite-colimit and size hypotheses; a generic appeal to “SGA” is not a replacement for those conditions.

The named external project registers were not part of the attachment. An attempt to locate them found Personal Context disabled, no exact-title result, and unrelated results on broader and exact-content retries. This is an access/retrieval limit, not evidence that the registers do not exist. Their source-note assertions and available manuscript endpoints were checked; the register endpoints and their reported theorem statuses remain **unverified attributed leads** in `SA10_project_leads.tsv` and the corresponding `our projects` rows. This is the explicit exception to two-ended source verification, rather than a claim that the absent endpoint was inspected.

The searches used primary author pages, arXiv, Numdam, publisher records, MathOverflow for discovery, the archive inventory, EGA/SGA and author bibliographies. Direct zbMATH access and some original articles or books were incomplete. Those limits are recorded per search scope and reference. Where a modern exposition gives the exact theorem used, the dossier cites that opened theorem and marks an inaccessible original separately. No “not developed” conclusion rests merely on the absence of a first title hit.

## 11. Research tasks and use of the dossier

The ranked directions in `SA10_directions.md` specify the source items, claims and problems, the exact intended result, what is already known, and the first concrete step. They separate genuine open formulations from companion-writing work whose mathematics is already settled. A short run can often resolve a definition, a diagram's exact hypotheses, or the scope of a theorem; it cannot responsibly be promised the full tame-isotopy or general gluing programme.

No listed direction is developed here. The new proofs and counterexamples in the records check claims or hopes already present in the supplied notes and transcriptions. Their purpose is to make the subsequent tasks start from a corrected statement.

The consolidated tables are authoritative. The local package tables remain as work documentation, and the alias file records every cross-package identification. Thus a proof's original identifier can still be traced without counting the same object twice. Counts and the structural validation result follow below.


## 12. Final counts and validation

The counts below describe the authoritative consolidated files. All **537 indexed entries** occur exactly once in the entry table and exactly once among the items’ source lists. There are **400 retained items**, after 17 explicit cross-package merge groups reduced 421 locally reviewed records by 21. The five exact claim merge groups reduce 282 local records to **276 claim records**; two exact problem merges reduce 75 local records to **73 problems**. Composite synopses and distinct qualified constructions remain explicitly labelled; these are record counts, not a count of independent theorems.

### Entry verdicts

| Verdict | Entries |
|---|---|
| kept | 296 |
| merged | 115 |
| corrected | 108 |
| withdrawn | 11 |
| rests on a misreading | 7 |
| Total | 537 |

A cross-package duplicate receives `merged` when its former verdict was `kept`. A substantive correction, withdrawal or misreading retains that verdict and names the canonical item. Thus an important textual correction is not erased by the merge operation.

### Items by kind

| Kind | Items |
|---|---|
| conjecture | 10 |
| unproved claim | 87 |
| unpursued implication | 69 |
| idea of the earlier run | 62 |
| reading question | 47 |
| self-flagged step | 48 |
| withdrawn in the same text | 22 |
| title, date or page count | 21 |
| other | 34 |
| Total | 400 |

### Claims by literature class

| Class | Meaning | Records |
|---|---|---|
| A | Exact result in his own later published work | 0 |
| B | Matched established development by others | 12 |
| C | Partial development or a precisely stated qualification | 96 |
| D | No development found in the recorded bounded search | 0 |
| E | Earlier standard framework or elementary consequence | 143 |
| F | Exact assertion not identifiable from the available text | 25 |
| Total |  | 276 |

The zero in A does not deny the later programme’s continuity, and the zero in D is not evidence that every manuscript question was developed. The scope of a located theorem was kept separate from an exact identification; incompletely specified questions remain C or F as their records explain.

### Claims by primary page-status category

| Reporting category | Records |
|---|---|
| proof sketched | 80 |
| false as stated or under the specified literal reading | 27 |
| proved there | 25 |
| stated without proof | 57 |
| corrected by himself later | 17 |
| definition or additional axiom | 3 |
| open on the pages | 44 |
| written numerical computation | 1 |
| earlier-run example, modern benchmark or present reconstruction | 22 |
| Total | 276 |

This is a manually assigned reporting crosswalk, saved in `SA10_claim_status_index.tsv`. Each claim’s full `status_on_pages` retains its mixed cases, cancellations and hypothesis qualifications. “Open on the pages” is a historical status; it does not mean open in November 2026. The 22 explicitly nonauthorial records retain earlier-run diagnostics, modern benchmarks or this run’s refinements without attributing them to the manuscript. Literal-reading refutations remain conditional where the ink or convention is uncertain.

### Problems, readings, directions, links and evidence

| Record set | Count |
|---|---|
| Problems | 73 |
| Reading-table records | 144 |
| Active mathematical or reading alarms | 108 |
| Optional lexical check | 1 |
| Closed reading/scope provenance records | 35 |
| Ranked future directions | 12 |
| Archive-folder links | 59 |
| Published-work links | 31 |
| Attributed project leads in their separate table | 49 |
| Bibliography records | 85 |
| References with an opened source or metadata record | 76 |
| Explicitly unverified original references | 9 |
| Check events | 1023 |

The 35 closed reading records comprise 33 supplied-second-pass closures and two resolved scope/provenance records. The active total includes mathematically diagnosed formula or hypothesis defects as well as undecided readings. It must not be presented as 108 newly discovered transcription errors. `SA10_reading_status.tsv` records the decision for every row; no exact duplicate alarm was found across the disjoint package page ranges. The 49 project leads retain the access exception stated in §10.

| Check-event type | Events |
|---|---|
| used and rechecked in this run | 718 |
| independent re-proof | 129 |
| targeted proof check | 66 |
| refuted, with the refined statement's id | 27 |
| computation or formal certificate | 59 |
| carried as background without fault found | 24 |

The final structural gate verifies complete index coverage, unique and resolving identifiers, all required fields, complete source mapping, bibliographic links, recorded literature-search scopes and check events for every retained item and claim. The source-identity check confirms that every extracted original file is byte-for-byte unchanged from the supplied ZIP. These checks establish documentary completeness and consistency; mathematical evidence remains in the individually scoped proofs, counterexamples, computations and source audits.
