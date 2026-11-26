# SA29 — Autour de La Longue Marche à travers la théorie de Galois

## Part 2: cotes 144, 145 and 148/1–28

**Status date: 19 November 2026.**

This dossier consolidates all **380 indexed entries** into **264 items**, **255 manuscript claim records** and **72 author-problem records**. It supplies the complete verdict ledger, searched literature fates, exact calculations and proofs, reading alarms, cross-references and **12 ranked follow-up directions**. The most useful result is the separation of the manuscript’s actual constructions and questions from convention errors, later completions and imported project claims.

## 1. Scope, sources and how to use this dossier

This is the consolidation of **part 2**, not a replacement for the eventual dossier of the entire topic. All 380 entries of the supplied `NOTES_INDEX.tsv` have been compared directly with their notes, the corresponding passages of the supplied transcriptions, and the applicable second-pass files. The five packages retain 242 scan blocks: 176 for cote 144, 38 for cote 145, and the first 28 of cote 148. A scan block is not necessarily a manuscript page: covers, reused printed paper, administrative notices and sparse sheets remain part of the inventory. The package boundaries are not boundaries between mathematical arguments.

The topic inventory below reproduces the scope of `TOPIC.md`. Its catalogue count and Pro count answer different questions and are not silently reconciled. “Other part” means that the folder is recorded for orientation and cross-reference, without attributing a new entry verdict or a mathematical examination of its absent text to this run.

| Cote | Catalogue subject | Catalogue pages | Pro pages in topic inventory | Treatment here |
|---|---|---:|---:|---|
| 141 | Théorie de Kumer ?; note Alexandre, bi-tenseur | 15 | 16 | Other part; no transcription supplied here |
| 142 | Action de Galois sur Teichmüller [147] | 121 | 119 | Other part; cross-reference target only |
| 143 | Paradigmes des courbes algébriques | 33 | 34 | Other part; cross-reference target only |
| 144 | Teichmülleries; notes and letters, 1981–1983 and undated | 183 | 176 | All four supplied packages, including the continuation into the combined file |
| 145 | Printemps 81 (vieille rédaction) [149] | 37 | 38 | Entire supplied package and both second-pass batches |
| 146 | Groupoïdes de Teichmüller and special Teichmüller groups | 133 | 123 | Other part; no endpoint inferred from its title |
| 147 | Structure à l’infini des M(g,n) | 189 | 188 | Other part; boundary-program comparison remains scoped |
| 148 | Teichmüller (1983) | 71 | 72 | Scans 1–28 only; the remaining pages are outside this part |
| 149 | Autour de La Longue Marche | 135 | 136 | Other part; context leads are distinguished from checked text |

`SA29_entries.tsv` is the complete entry ledger. `SA29_items.json` records what the earlier notes say about a common object or question. `SA29_claims.json` records the actual mathematical assertions, constructions, computations and explicit questions on the pages, including assertions the notes did not isolate. Thus an item can support several claims, and a claim can recur in several items or folders. A compound entry in the earlier notes is not artificially counted as one proposition. Conversely, repeated propositions are consolidated with all their occurrences retained.

Stable identifiers are intentionally not consecutive. The review ranges were reserved before reading, and later mergers preserve their canonical IDs. `audit/id_aliases.json` resolves every merged ID. The original package records remain in `review_A`, `review_B`, `review_C` and `review_R`; they preserve the source of each decision rather than competing with the consolidated root files. Explicit merger decisions are in `audit/merge_decisions.json`.

Three distinctions govern the edition. First, a statement on a page, the result in a later source, and a reconstruction by this run are separate fields. Second, a textual comparison is not a proof check: the check-event outcome says when only the notes and transcription were compared. Third, a mathematical inconsistency is evidence for a scan inspection, not authority to alter the ink. The input files were not edited. Current supplied second-pass readings take precedence over the original notes; there are no new image-based decisions in this dossier.

Full-file line numbers are used unless expressly described as page-local. Each record names its combined transcription or has an unambiguous package context. `audit/pages_navigation.json` maps the retained scan blocks to their full-file line ranges. In a consolidated record, scan labels are qualified by cote. The original package files retain their native locator conventions so that a source note can still be followed without guessing.

## 2. What the folders are doing, in their own order

### 2.1 Cote 144: finite actions, compactification and the structure at infinity

The opening sheets move among finite group actions, fixed sets, recognition of manifolds, and the compactification of moduli. These are not merely preliminaries to a group-presentation calculation. Grothendieck is testing how much geometry can be recovered from local symmetry, incidence and fundamental-group data. The proposed use of Smith theory needs its local homology and finite-group hypotheses stated; connectedness of a whole fixed set does not follow just from a local description. The wild involution and double-suspension examples belong to the topological category, while the proposed differentiable, nonconical ball actions require a separate formulation. The distinction between an actual manifold and a singular suspension is essential to the cone discussion. [SA29-6–8, SA29-33, SA29-34, SA29-36, SA29-38; C-SA29-1–3, C-SA29-21–24.]

His question about intersecting covering-theoretic paths is broader than a comparison with an already known loop bracket. The algebraic or étale construction, its arithmetic equivariance and its possible Tate-valued output all need definitions. A Goldman bracket is a useful comparison, but does not by itself supply those structures. Similarly, the unresolved word `prodisque|prodiscret` changes the proposed cohomological setting; the dossier does not choose one by mathematical preference. [SA29-10–12; C-SA29-4–5.]

The stable-curve material has a genuine continuation much later in cote 144. On scan 4, stability is introduced through finiteness of automorphisms, projectivity is questioned, and the parenthetical component test mentions rational components. Scans 182–183 explicitly add the genus-one qualification and formulate stability in terms of normalization branches and marks. The common modern criterion is

\[
2g_v-2+n_v>0
\]

on every normalization component, with a node contributing one branch on each of its two preimages. It gives an ample log dualizing line bundle and excludes infinitesimal automorphisms. These are established stable-curve facts, with Deligne–Mumford providing the primary historical framework. The item and claim have therefore been merged across the early and late packages. The projectivity question remains visible in its early occurrence. [SA29-16; C-SA29-9; DeligneMumford1969, Definition 1.1, Lemma 1.4 and §1.]

Several nearby questions have different answers. The stable-reduction and separatedness ingredients resolve the valuative question after their hypotheses are specified. For ordered markings, adjoining the boundary kills the Dehn twists that generate the relevant mapping-class group in the stated stable range, but this does not prove that the entire boundary itself is simply connected. An unordered quotient stack is a different object. Nor should the exceptional unmarked genus-one notation be silently replaced by a stable pointed moduli stack. Those latter statements have separate claim records because their objects or quantifiers are not determined by a familiar theorem nearby. [C-SA29-6–8, C-SA29-11–15.]

The generalized-Jacobian question has a concrete obstruction. Take a stable compact-type curve consisting of a rational central component meeting three elliptic tails at three nodes. Its dual graph is a tree and its generalized Jacobian is the product of the elliptic Jacobians. The smooth part of the central component is a three-punctured projective line. Any morphism from that open curve to the abelian variety extends across the omitted points and is constant; consequently the entire smooth locus cannot embed as proposed. All stability and compact-type hypotheses are checked in the proof record. This is an answer to the question as written, not evidence that the scan contains an incorrect letter. [SA29-17; C-SA29-10.]

The finite-action questions also require historical separation. Nielsen realization is an established theorem, but a proposed negatively curved invariant metric is a particular route, not an equivalent theorem with all the same geometric requirements. The Coxeter and quadratic-form notes contain tentative generalizations for which spherical, affine and hyperbolic cases must be kept distinct. The arithmetic and topological group examples in the correspondence are not all assertions by Grothendieck: authorship of Mazur’s letter and of the Deligne material is retained. [C-SA29-17–29.]

One especially useful correction concerns the group in Mazur’s letter. Under the displayed relations

\[
x^3=y^3=1,\qquad [x,y]\text{ central},
\]

centrality implies \([x,y]^3=[x^3,y]=1\). A normal form gives at most 27 elements, and the Heisenberg group over \(\mathbf F_3\) realizes all 27. Its commutator subgroup has order three, not infinite cyclic. The saved computation checks the generated group, the centre and the commutator explicitly. Separately, a contractible infinite-dimensional topological group can contain torsion: the norm-topology unitary group in Kuiper’s theorem supplies the relevant earlier example, with the topology indispensable. These two issues should not be conflated. [C-SA29-28–29; review_A computations and primary-source verification records.]

### 2.2 Cote 144: arithmetic comparison, discretifications and D-structures

The next line of work compares discrete topological structures with completed fundamental groups and arithmetic actions. The repeated symbol Gamma does not denote one object throughout. It can refer to a discrete mapping-class group, a geometric completion, an arithmetic preimage, an image quotient, an absolute Galois group, or a torsor-related object. Later it even denotes hemispheres or an elliptic lattice. The consolidated concordance preserves these local meanings and the undefined cases. [SA29-2.]

The point-forgetting sketch separates three questions that earlier project comparisons sometimes placed too close together: the geometric Birman sequence, injectivity of completed geometric monodromy, and recovery of an arithmetic quotient. For a pure four-punctured sphere, the pure group is a rank-two free group; the full four-point group has additional permutations and a Klein-four kernel over the projective modular group. An arrow written beside a familiar symbol does not decide which of these groups is meant. [SA29-3, SA29-406; C-SA29-31, C-SA29-33–34, C-SA29-312; FarbMargalit2012, Proposition 2.7 and §4.2.]

The dossier preserves the D-structure proposal as an attempt to retain a discrete position or a complex realization that completion may forget. Torsor twisting and transport of structure are valid constructions when their groups and actions are fixed. A bare torsor under one fixed group does not, however, provide the claimed fully faithful classification of all curves. The proposed arithmetic reconstruction therefore remains more than a formal torsor identity. [C-SA29-36–47.]

The transitivity assertion on scan 27 is still a live assertion. The subsequent discussion of left versus right action does not retract it. In particular, a report that the later page had already withdrawn the finite-index transitivity claim would erase the wrong proposition. The distinction between an embedding of a field and its restriction to the ground field also matters: automorphism orbits cannot be identified without specifying which restriction is fixed. These points are recorded as exact source-status corrections rather than as a blanket assessment of the D-structure programme. [SA29-86, SA29-93; C-SA29-48–49.]

Ideas involving mixed Hodge structures or complex structures on an abelianized group are kept under their actual attribution. Where an earlier run supplies a useful comparison or an elementary kernel lemma, that material remains available in the editorial-check register; its presence does not add an assertion to Grothendieck’s claims count.

### 2.3 Cote 144: modular matrices, braid groups and central lifts

The modular calculations are extensive and local conventions change. Exact integer matrices, reduced free words and a central normal form were used to check the written identities. A matrix quotient alone is insufficient when the discrepancy is an inner automorphism or a central winding number.

The common structure behind the repeated braid sheets is

\[
B_3=\langle a,b\mid aba=bab\rangle,
\quad s=aba,
\quad r=(ba)^{-1},
\quad z=s^2=r^{-3}.
\]

The centre is generated by \(z\); its image in \(SL_2(\mathbf Z)\) is \(-I\), so the kernel over \(SL_2(\mathbf Z)\) is generated by \(z^2\). The repeated question on scan 158 first verifies the equality of the two common powers and then asks the stronger question whether the square is primitive in the special-to-ordinary kernel. In the boundary-fixed one-holed-torus model, the two-chain relation identifies it with a single boundary twist. The equality and primitivity must not be counted as the same proof. [SA29-104, SA29-111; C-SA29-56–57, C-SA29-61; FarbMargalit2012, §9.2 and Proposition 3.19.]

The two-generator five-factor relation is equivalent to the braid relation under its stated substitution. It is not a five-point associator pentagon. The separate assertion that one commutator relation suffices is false under that literal presentation; an explicit finite quotient witnesses the deficiency. The valid braid presentation, its centre, and the rejected weakened presentation therefore have different claim records. [SA29-1, SA29-116; C-SA29-57, C-SA29-61–63.]

The central-sign comparison at scans 131 and 158 is another place where quotient calculations conceal a mistake. For the displayed automorphisms of the free group, the sixth power of rho is conjugation by the inverse commutator, while the fourth power of sigma is conjugation by the commutator. The later inverse sixth power is consistent. The dossier retains both locations, without inventing an explicit retraction sentence. [C-SA29-207–208; review_B exact Aut(F2) computations.]

The period calculations also distinguish a linear group from its effective projective action, and positive determinant from negative determinant. Complex conjugation is required for the latter action on the upper half-plane. Scalar transformations are exceptions to a naive negative-discriminant fixed-point criterion. The fixed-point formula and orientation/sign conflicts are preserved with exact test matrices and proposed scan checks. They are not repaired by globally changing all rho, sigma or period conventions. [C-SA29-64–69.]

A related exact comparison unifies the mixed fundamental-group constructions at 144/50, 129–130, 173 and 145/16–17. For mixed arrows \(x\to y\), write \((\ell,g)\) with \(\ell:gx\to y\). Their composition is \((\ell'\circ g'\ell,g'g)\). At a basepoint, the convention \(\ell:a\to g^{-1}a\) is converted by \(\ell\mapsto g\ell\); the forward convention \(k:a\to ga\) is converted by inversion of the path. These conversions were checked by endpoints and by the multiplication laws. The resulting group retains stabilizers; it is not automatically the fundamental group of the coarse orbit space. [SA29-133; C-SA29-70.]

### 2.4 Cote 144: cartes, three-point covers and finite colouring obstructions

The cartographic programme starts with cells, flags, involutions and isotopy, then passes to weighted triangles and coverings. The distinction between ordinary and weighted cartes is structural. The weighted group is \(C_2*C_2*C_2\); its even subgroup is free of rank two. The ordinary group adds the indicated peripheral square relation and becomes \((C_2\times C_2)*C_2\). A weighted flag is an actual coloured triangular face, not automatically a triangle in the barycentric subdivision of a different ordinary map. [SA29-138; C-SA29-72.]

The asserted categorical equivalence needs its objects and morphisms fixed. The written freeness conditions do not enforce the early exclusion of a circle component. A four-flag example satisfies those involution conditions but yields the excluded circle. Folded edges also change the relation between full flags, positive flags and edge counts. The algebraic action category has a formal full subcategory when the extra relation is imposed; transferring that statement to geometric cartes still requires the same geometric morphisms on both sides. [SA29-137, SA29-145, SA29-147, SA29-148, SA29-149, SA29-158; C-SA29-71, C-SA29-75, C-SA29-79.]

The transition from 144/61 to 62 is a continuation of one argument. Finite monodromy sets for the punctured sphere give finite covers, which extend across the three punctures; the pulled-back real equator gives the weighted cellulation. The real-descent and signature versions then develop through scan 77. A relation \(\rho_i^{\nu_i}=1\) imposes divisibility of local monodromy orders, not equality of every local degree with \(\nu_i\). The complex covering equivalence and descent to \(\overline{\mathbf Q}\) are different theorems. [SA29-159; C-SA29-80, C-SA29-151–160; SGA1, XII, Theorem 5.1; Oesterle2003, §§1.1, 1.9–1.10.]

The colour-transport construction deserves to be retained as its own mathematical result. Transporting the three labels across a triangulation gives an \(S_3\)-cover away from the vertices. Odd valence produces transposition monodromy. When the cover is unramified and a compatible face bicolouring trivializes the sign quotient, the remaining obstruction is a \(C_3\)-torsor class. The assumptions on orientation and the chosen sign trivialization are needed for that reduction. This is more precise than an unconditional claim that every triangulation is three-colourable. [C-SA29-162–164.]

Two easily missed assertions fail in their literal generality. A faithful action with finite stabilizers need not be properly discontinuous: an irrational rotation action gives the counterexample. Also, extendability of a labelled cyclic action alone does not uniquely determine the labelled sphere; at order five, multipliers \(\zeta\) and \(\zeta^2\) are inequivalent. The next page’s angle normalization removes that ambiguity. The final map records the false statement and the actual later strengthening together. [C-SA29-159, C-SA29-165.]

### 2.5 Cote 144: filling, correspondence, complex multiplication and cylinder models

The filling calculations at scans 103–115 operate on specified fundamental groups and extensions. In the attempted ambient extension for filling zero, the element to be killed is conjugate to another element the proposed target keeps nontrivial. Normal closure therefore supplies a direct obstruction. This is a stronger and more useful diagnosis than calling the whole diagram unclear. It does not imply a theorem about all outer automorphisms under filling. The inverse word at scan 115 has a separate missing initial rho, detected in the full free-product normal form. [SA29-203; C-SA29-185 and the related filling records; C-SA29-249.]

The letters and CM notes continue across a package boundary. The theorem is present at scan 123; it is not missing merely because the preceding package ends at 121. Its quantifier fixes the reflex field, and its inverse norm convention follows the direction of the displayed level structure. The determinant description is the reflex norm of a CM type, not a field norm between necessarily nested fields. The integral-lattice discussion also needs compatibility and the condition that the local lattices are standard almost everywhere. [SA29-210, SA29-213–219; C-SA29-197–203.]

The later theorem for arbitrary field automorphisms changes the CM type and uses the corresponding cocycle. It is not obtained by deleting “fixes the reflex field” from the earlier formula. Milne’s retrospective account dates Tate’s partial result to April 1981, Deligne’s advance to July 1981, and the first writing and distribution of that account to September 1981. Those dates are separated from later publication and from the undated manuscript letter. The date on a different Deligne letter is not transferred to the CM material. [C-SA29-237; Milne1981, opening historical account; MilneCM2020, §§1 and 9.]

The free and profinite group material in the correspondence is similarly typed. The discrete Nielsen–Schreier statement does not say that every closed subgroup of a free profinite group is free profinite. Jarden’s Theorem 16.1, printed page 306, supplies the particular free-profinite facts used here, including torsion-freeness, the primitive-generator centralizer and centrelessness consequences. That page was inspected as an image because text extraction did not supply the theorem. Verification of that statement is distinct from an independent proof of the whole paper. [C-SA29-190–191, C-SA29-238; Jarden’s reference-check record.]

The full lift over \(GL_2(\mathbf Z)\) also requires an action on its infinite cyclic kernel: determinant-negative elements invert the generator. The kernel is central only over \(SL_2(\mathbf Z)\). Calling the whole lift a central extension would erase the explicit inversion relation on scan 131. [SA29-224; C-SA29-206.]

The cylinder pages distinguish actions on the strip, descent to an annulus, restriction to its boundary, and passage to isotopy classes. These have different kernels. In the affine strip formula \(f_{a,b}(t,s)=(t+as+b,s)\), the annulus deck kernel is \(f_{0,n}\), not \(f_{1,n}\). In the rotation sector, finite-order boundary rotations force a rational slope and a root-of-unity constant. That characterization fails for all affine symmetries, because reflections with irrational parameters can still have order two. A restricted boundary-fixing subgroup has even twist number, while the larger affine group contains a primitive unit twist. [C-SA29-215–224.]

The late cylinder involution on 144/170 is another literal conflict: after the displayed deletion the active formula is the identity, which cannot conjugate a nontrivial twist to its inverse. A pointwise test distinguishes the two maps. The appropriate next action is an ink check and a local convention check, not a global sign change. [SA29-423; C-SA29-303.]

### 2.6 Cote 144: the final genus-one lift calculations and maquettes

At scans 174–177, the scalar defect has a composition law depending on the multiplier. Expanding the displayed polynomial gives

\[
11\nu_0-11\nu_2\nu_3-6\nu_2+4\nu_3=0.
\]

The reduction to \(11\nu_0=0\) holds if the other two parameters vanish, exactly as in the later conditional parenthesis; that parenthesis does not prove their vanishing. No unsupported range for \(\nu_3\) has been imported: the full supplied cote 144 was searched and no such range was found. The coordinate calculation in the determinant semidirect product is valid, but it is not by itself an injectivity theorem for the author’s larger special group. Over the special-linear part, the extension is a direct product; its profinite centre includes the independently selectable local signs in \(\mu_2(\widehat{\mathbf Z})\). [C-SA29-306–309.]

The corrected central exponents on scan 177 have a forced algebraic form once the divisibility and torsion-free central hypotheses are supplied. Their arithmetic check does not settle the remaining noncentral epsilon identity. A cancelled square calculation is not counted as an additional live conjecture, and the commutator calculation left blank on 175 has a later completion on 177. Enriquez’s elliptic construction gives a precise modern comparison, not an automatic identification of this normalization. [C-SA29-305, C-SA29-310–311; MP-SA29-101, MP-SA29-104; Enriquez2014, Proposition 2.20 and Theorem 8.4.]

The tower on scan 180 writes ranks \(\nu-3\), \(\nu\) and \(g+\nu\), and questions \(\Lambda_g\simeq\mathbf Z\). Chosen disjoint twists give commuting groups, but a curve system is additional data. Neither the written ranks nor standard pants decompositions establish the proposed canonicity or define Lambda. This remains an identification problem rather than a newly announced theorem about canonical commuting subgroups. [SA29-408; C-SA29-314; MP-SA29-102.]

The maquette records vertices for normalization components, edges for nodes, flags for branches and marks, and vertex genera. For a connected nodal curve,

\[
g=\sum_v g_v+m+1-s,
\qquad
\sum_v(3g_v-3+n_v)=3g-3+n-m.
\]

Both formulas are independently derived in the proof notes. The branch-to-node map has exactly two preimages per node; the stronger statement on scan 183 supersedes the earlier weak inequality. A different surjectivity claim fails: the flag-to-component map is not onto for a smooth unmarked stable curve of genus at least two, which has no flags. These two maps must not be repaired together. [SA29-418, SA29-431, SA29-433–434; C-SA29-315, C-SA29-317–319.]

### 2.7 Cote 145: peripheral automorphisms, rectifiers and the geometric restart

Cote 145 begins with cover realizations and descent, then studies automorphisms of the rank-two free group with its three peripheral classes. Some preliminary assertions need a restricted geometric category: equality of covering degrees follows from a nonzero Euler characteristic for hyperbolic curves, but not for arbitrary varieties. The objects represented at one prescribed covering degree need not form a subgroup. The cancelled descent fragment on scan 4 is not an active definition of a global Gamma. [C-SA29-451–458.]

The early peripheral formulas give necessary equations, scalar constraints and gauge changes. To characterize automorphisms they must also retain topological generation. In a finitely generated profinite group, surjectivity makes an endomorphism an automorphism, but the displayed peripheral conditions do not make that hypothesis disappear. The question of an effective criterion for the relevant full profinite solutions is therefore separated from a completed Lie-algebra or pronilpotent theorem. [C-SA29-455, C-SA29-464–469.]

The author then restarts geometrically. Paths are composed as functions, the loop order is explicitly reversed, and several earlier expressions must be translated rather than copied. The mixed group and its finite symmetry quotient are concrete geometric objects. The positive extension is \(C_2*C_3\), while the real preimage is the three-involution weighted cartographic group. The latter agrees with the group in cote 144 under the exact dictionary

\[
\rho_0=l_0=\tau_\infty\tau_1,\quad
\rho_1=l_1=\tau_0\tau_\infty,\quad
\rho_\infty=l_\infty=\tau_1\tau_0.
\]

This is a verified cross-folder identification of presented groups and generators. It does not identify the full peripheral automorphism group with the much smaller geometric extension. [SA29-138, SA29-621; C-SA29-70, C-SA29-72, C-SA29-477–485.]

Several local computations correct the earlier notes or expose literal errors. The epsilon generators do generate rho in the corrected model: an explicit word gives it. An early half-turn trial is superseded, but its old displayed images remain stale. A later relator already fails in the finite quotient \(S_3\times C_2\). In the rectifier description, ambiguity is multiplication on the correct side, the composition law is order-sensitive, and the action on a rectifier must not be omitted from the covariance formula. Each of these tests is carried out in a group where the relevant noncommutativity survives. [C-SA29-472, C-SA29-479, C-SA29-482, C-SA29-487–492.]

The decorated group has different kernels over peripheral Aut and over peripheral Out. The first retains the three procyclic framing coordinates; the second also retains the inner automorphisms. The scan 33 margin confusing those projections is not used as a theorem. The ascending product criterion on scan 36 conflicts with the later descending convention and even excludes the identity. In contrast, the following descending pure-power implication is genuinely his own question, marked as an exercise: a unit exponent satisfying that relation is forced to be one. Its proof in the earlier notes is an annotation to an actual manuscript assertion, so the claim remains in the claims map. [C-SA29-489, C-SA29-495–500.]

The final pages distinguish strict commutation of decorated lifts from commutation modulo inner automorphisms. The local cusp transposition has no order-two lift with the required peripheral normalization. Interior fixed-point sections and the signed section do exist for their different stabilizer data; they do not remove this cusp-normalization obstruction. A formal tuple multiplication law does not remove it either. A full presentation of the integral framing extension remains a deferred task. [C-SA29-494, C-SA29-501–505.]

The second-pass layer makes several consequential reading corrections: \(H_n\) on scan 2, the compatible \(\varphi\) on scan 4, the doubled centralizer symbol on scan 24, and the scalar reading on scan 10. In particular, the earlier objection built on an exponent \(pq\) must be withdrawn when the current reading is \(q\). The current whole-package Gamma census is 75; the second checked-notes block retains an earlier count of 78, superseded by the three scan-4 reading changes. [SA29-2; the cote-145 rows of `SA29_readings.tsv`.]

### 2.8 Cote 148, scans 1–28: toric boundaries, exceptional elliptic curves and privileged paths

The boundary-rotation sheet bears the date 29 November 1983. It constructs a rotation extension and then uses markings to split related groups. The claimed embedded \(\mathbf R^I\) requires exclusions: the disk has trivial relative mapping-class group, and the two annulus boundary twists are dependent. The fixed subgroup of the marking torus consists of coordinates constant on each orbit of the boundary permutation action; it is only the diagonal when that action is transitive. For multimarkings, permutations must preserve the coordinate orders. These are separate qualifications, with disk, annulus and unequal-order examples in the proofs. [SA29-402, SA29-409, SA29-435–437; C-SA29-320–323; FarbMargalit2012, Lemma 2.1 and Proposition 2.4.]

The exceptional elliptic curves are treated as torsor-like groupoids with pointed automorphism groups \(\mu_4\) and \(\mu_6\), represented by the square and Eisenstein lattices. The exact torsion actions and fixed points are checked by integer lattice matrices. The square torus and its doubled cell structure have counts \((1,2,1)\) and \((4,8,4)\); the quotient by sign has \((4,4,2)\). The hexagonal triangulation gives \((1,3,2)\), then \((4,12,8)\), and the sign quotient gives the tetrahedral sphere \((4,6,4)\). The origin-fixing order-six group descends to a vertex stabilizer of order three; the full affine action on the four two-torsion points is larger. [C-SA29-324–332; Milne2021EC, IV, Proposition 7.13 and Remark 7.18.]

The exponential on scan 11 lacks the imaginary unit required to give the claimed sixth root. The cube-root definition on scan 9 includes it. The lattice on scan 9 is also once named with the symbol used for its ambient vector space; the following quotient is already correctly written. These are narrowly located alarms, not reasons to replace all symbols in the elliptic section. [SA29-441; C-SA29-329; reading rows at148/9 and148/11.]

The red tetrahedral refinement on scan 18 passes its incidence checks: 22 vertices, 48 edges and 28 faces, with 24 triangles and four hexagons. Both the face-side and vertex-valence totals are 96. The elementary path types and several composite counts can also be checked. What is not supplied is the promised complete relation system. The common barycentric refinement on scan 19 is a further comparison, not automatically the same red refinement. The second-pass readings concerning non-digons and adjacent positions remain authoritative. [C-SA29-332–334; MP-SA29-105–107.]

On scan 20, the action of \(S_4\) on the three pair partitions has Klein-four kernel and the same sign character; the orientation-torsor comparison is therefore valid. The upper mapping-class diagram has a standard interpretation once pure/full groups are distinguished. The lower subgroup slash and its quotient remain insufficiently identified. A finite congruence calculation supports a candidate complement, but does not decide the ink or uniqueness. [C-SA29-335–337; MP-SA29-108.]

The remaining sheets mix valid dimension counts, unfinished slots and genuinely conflicting enumerations. The four displayed configuration families total 17, whereas a later line explicitly gives 14; the dossier does not force them into one count without a common definition. The dimension-two constructions at \(M_{0,5}\) and \(M_{1,2}\) are blank. The three-involution Coxeter presentation is the extended modular group. The dessin correspondence gives models over \(\overline{\mathbf Q}\); it does not make every complex Belyi curve descend to \(\mathbf Q\). The double-cover diagrams satisfy Riemann–Hurwitz with four simple branch points under the coherent edge reading. A separate two-hexagon/nine-edge/six-vertex count fails the closed-surface incidence test. The last two-hexagon/six-edge/four-vertex count has Euler characteristic zero, but Euler characteristic alone does not verify the gluing as a torus. [C-SA29-339–345; Oesterle2003, Theorem 1; MileaShelleyWeissman2019, §1.]

## 3. What the earlier notes got right, and what must change

The earlier notes were useful in identifying local questions, collecting generator names and noticing unfinished constructions. Many of their cautions about missing hypotheses were justified. Their weakness was uneven control of conventions and of the boundary between manuscript evidence and their own project context. The consolidated records retain useful ideas while correcting their attribution.

The most consequential corrections are these:

| Earlier tendency or reading | Consolidated decision | Main records |
|---|---|---|
| Read a two-generator five-factor relation as evidence of a five-point pentagon | It is a braid relation; the supplied five-point construction slots are unfinished | SA29-1; C-SA29-57, C-SA29-339–340 |
| Treat Gamma as a globally fixed arithmetic or geometric group | Retain local definitions, current second-pass symbols and undefined nodes | SA29-2 |
| Use a geometric filling theorem as proof of a full peripheral or arithmetic quotient statement | Specify the source, target, completion, distinguished-point stabilizer and kernel separately | SA29-3, SA29-203, SA29-412; C-SA29-31–34 |
| Count a later left/right-action correction as withdrawal of D-structure transitivity | The transitivity assertion remains live | C-SA29-48–49 |
| Carry an equality of matrices into a free or central extension | Check reduced words or the central coordinate; several inner/central discrepancies survive | C-SA29-56–63, C-SA29-208, C-SA29-308 |
| Treat the CM theorem as missing because one package ends | The letter continues and states it on144/123 | C-SA29-197–203 |
| Infer a general quotient from faithful finite-isotropy action | Proper discontinuity is a separate requirement | C-SA29-159 and its refinement |
| Retain the scan10 exponent objection in145 after the second pass | Withdraw the old objection; current exponent isq | SA29-617–618 and the relevant reading row |
| Omit the geometric restart’s reversed peripheral order | Keep the two conventions and translate; the later ascending criterion fails | SA29-621; C-SA29-499–500 |
| Treat every blank, question mark or printed question as a live author problem | Separate later completions, cancellations, affirmative OK, and reused examination paper | SA29-454–456; problem register |
| Treat all finite-count discrepancies as optical errors | Keep a mathematical alarm and await the scan; some counts concern different objects | C-SA29-339, C-SA29-343–345 |

The earlier runs’ quotient lemmas, Euler-count deductions, Hodge comparisons and proposed connections remain useful material. Where they are not assertions of the manuscript, they are retained as editorial checks or research leads and excluded from the author-claim count. Refined statements produced by a counterexample also have their own stable records. This makes the refutation reproducible without attributing the repair to the original page.

## 4. Literature status as of 19 November 2026

The claim map gives the exact searched fate for every retained claim. The accompanying search ledger records the grouped claim IDs, source family, actual query, opened source, result and hypothesis match. Searches included arXiv, zbMATH Open and indexed zbMATH results, MathOverflow, Numdam, EGA/SGA, Grothendieck’s published-work catalogues and author bibliographies. Failed access is recorded. Some zbMATH and publisher endpoints did not return usable text; a failed request is not represented as a read theorem. Backward references were followed where later sources supplied a better route.

The A–F field is a literature classification, not a truth value. `status_on_pages` and `present_status` must be read with it. For a claim containing a corrected classical construction, the fate narrative specifies which formulation is established and which literal formula is refuted. Class D means that the particular statement or construction was not identified as developed in the recorded searches; it is not a novelty certificate. Class F means that the missing object, reading or quantifier prevents a definite identification. In particular, a page with a question mark is not automatically a modern open problem.

### 4.1 Established ingredients and exact qualifications

Stable reduction, stability and projectivity, the complex finite-cover/étale comparison, the Birman and capping sequences, the modular amalgam, braid centres, annulus twists, finite Möbius classifications, CM theory and the basic permutation model of maps all have established frameworks. The dossier uses those frameworks with their actual hypotheses. It does not present the whole manuscript as either novel conjecture or solved exercise. Exact local errors and undefined global objects remain visible alongside the standard ingredients.

The Belyi distinction is particularly important here. Finite three-point covers over the complex numbers belong to the topological/algebraic covering dictionary. Descent of the resulting curve to the algebraic numbers is the arithmetic theorem. Descent to the rational numbers is stronger and generally false. The genus-one discussion similarly distinguishes the automorphisms fixing the origin from translations and their semidirect product. [SGA1, XII, Theorem 5.1; Oesterle2003, §1.10; Milne2021EC, IV, §7.]

### 4.2 Congruence, arithmetic faithfulness and the scope of recent results

The geometric congruence question in cote 144 remains distinct from arithmetic quotient recovery. Boggi’s 2026 paper proves a centralizer result under a congruence condition for the quotient surface; its stated corollary applies when the quotient has genus at most two. It does not settle the unrestricted mapping-class congruence subgroup problem. The paper appeared online on 23 September 2026, after the first arXiv circulation in August 2024. The conditional all-genus result of Henry Wilton, with an appendix by Alessandro Sisto, assumes that all word-hyperbolic groups are residually finite. These restrictions are part of the fate of C-SA29-33, not small print to be discarded.

Hoshi–Mochizuki’s Corollaries 6.4–6.5 give the trivial-intersection consequence for the arithmetic and geometric monodromy images of ordered hyperbolic moduli over number fields or p-adic local fields. Over an arbitrary characteristic-zero field, the corresponding statement is the weaker containment in the kernel of the map to the absolute Galois group of the rationals. Their formulation separates this issue from injectivity of the full monodromy map and connects the remaining injectivity with the geometric congruence problem. It is a precise modern comparison for the arithmetic-image question, not proof that every peripheral automorphism belongs to the arithmetic image. [C-SA29-34 and its references, exact printed locators 66–67.]

For the peripheral questions in cote 145, the completion and the number of marked points matter. Furusho’s pentagon-to-hexagon theorem concerns its specified pronilpotent setting; it does not settle the unrestricted full profinite automorphism criterion asked here. The first arXiv version is dated 6 February 2007, while the Annals publication is 2010. Harbater–Schneps includes an automorphism condition and symmetry, and the higher-point results must not be substituted for the rank-two free-profinite question. Lochak’s 2025 discussion explicitly retains invertibility and says that no effective profinite criterion is known in that formulation. [C-SA29-465, C-SA29-486; Furusho2010; HarbaterSchneps2000, §0.1; Lochak2025, §4, equation(4.1).]

The 2026 Lochak–Nakamura–Schneps preprint constructs the stated GT actions on the full profinite groups of closed surfaces and surfaces with one marked point for positive genus. Its first arXiv circulation is 12 February 2026. Its final discussion leaves compatibility with the entire Lego system as further work. This is a material advance in the surrounding subject, while remaining different from proving the author’s particular local word normalization or completing his unwritten privileged-path relations. [LochakNakamuraSchneps2026, Theorem 1.1 and §8.]

### 4.3 The low-dimensional reconstruction programme

The Esquisse formulates the dimension-one generators/dimension-two relations perspective. Bakalov–Kirillov proves connectedness and simple connectedness for its specified marking complexes; the preprint first circulated on 10 September 1998 and the journal article appeared in 2000. Those theorems are appropriate comparison targets for the unfinished path systems, but an identification needs an explicit object and move dictionary. The Esquisse’s count of twelve pieces has a different scope from the local 17/14 discrepancy in cote148. [GrothendieckEsquisse1984, §2; BakalovKirillov2000, Main Theorem4.24 and Theorem5.1.]

Basualdo Bonatto–Robertson’s 2026 preprint adds a modular-operad formulation. Its v2 Theorem 4.9 gives the Nakamura–Schneps monoid inclusion; units act faithfully. Proposition 6.14 gives the resulting action on the tower of profinite homotopy 1-types. The comparison with the full geometric étale homotopy model is an equivalence after genus≤1 truncation in Proposition 6.22. The two constructions are not identified in all genera. The recorded dates are first arXiv submission on 31 May, v2 submission on 8 October, and the PDF’s internal date of 12 October 2026; no journal publication was verified. This supplies a further comparison framework, without identifying the manuscript’s unfinished paths. [BasualdoBonattoRobertson2026, pp.41, 57, 59–62; audit/BBR2026_report.md.]

Enriquez’s elliptic work supplies a section of the relevant elliptic GT construction and an arithmetic action compatible with the linear part. Its dates are separated: arXiv circulation on 4 March 2010, online journal publication on 26 September 2013, and volume publication in 2014. It gives a disciplined target for comparing the genus-one lifts, not evidence that the scalar calculation on144/177 already proves all of that theory. [Enriquez2014, §2.6, Proposition2.20, and Theorem8.4.]

## 5. Author problems, reading alarms and cross-references

The problem register contains the author’s questions, hopes, doubts and expressly deferred work. It includes questions that are resolved later on the same pages or by established theory, because the purpose is to locate and explain his open steps, not to publish an inflated list of current open conjectures. Each problem separates the strongest formulation supported by his words from a plausible modern formulation. Historical explanations of why an issue was dropped are given only when a source says so; otherwise the field explicitly records that the reason is unknown.

The strongest candidates for a focused follow-up concern the exact genus-one lift dictionary, the unfinished privileged-path relations and their common subdivision, the lower four-point diagram, and a precise formulation of the peripheral centralizer/generation question. Some tasks are editorial closures: the completed commutator calculation, ordinary matrix blanks, known class-field precision and the pure-power exercise. The ranked list states both mathematical interest and what a few-hour run can realistically accomplish. It does not develop those projects in this dossier.

The reading register deliberately mixes two kinds of evidence without conflating them: authoritative supplied second-pass resolutions, and new mathematical alarms awaiting scans. It records a proposed alternative only with its evidence and dependence weight. A false formula can arise from an authorial slip, a transcription error, an unfinished convention change or a missing hypothesis. The algebra does not decide which explanation is paleographically correct.

All local links in the consolidated comparison table were checked at both supplied endpoints. Published-work links give an opened source and an exact locator where one was recoverable. The separately retained project table contains earlier-run leads, including named LM, Dérivateurs, S6 and other run labels. An unavailable endpoint remains labelled unavailable. A project register’s “proved” label is not used as evidence for an absent theorem.

One public comparison became available during the run: the Carmona transcription of the first part of La Longue Marche. Its front matter identifies an underlying1981 text and calls the edition provisional; no edition date or concordance to the LM_140 project scans was established. In§32, printedpp224–226, induced surjectivity is separated from the uncertain kernel-equality/bijectivity step. In§35, printedpp272–278, ordinary outer faithfulness is distinguished from stronger quotient statements, with explicit deferred group-theoretic ingredients. This checked textual comparison does not validate the numerical scan references395–399 or491/493/496 used by the earlier runs. [GrothendieckLMCarmonaUndated; SA29-412, SA29-417.]

No material from the other six cotes, the unsupplied remainder of148, or the absent project registers has been fabricated to close these links. The dossier records the failed retrievals and the exact surviving lead so that the eventual whole-topic merger can complete those endpoint comparisons with the appropriate source files.

## 6. Verification and reproducibility

The calculations are exact wherever the claim is exact: integer and rational matrix products, reduced free words, free-product or central normal forms, finite permutation quotients, symbolic polynomial expansions and finite lattice actions. A finite test is used as a counterexample or a specified finite certificate; it is not promoted to a proof of an unrestricted profinite statement. The written proofs supply the normal-form bounds, universal properties or geometric hypotheses that finite output alone would not establish.

The three package computation families and the late-cote root computations are retained with their outputs. False outputs are purposeful witnesses to literal identities or rejected alternatives, not unexplained failed tests. The package summaries distinguish those from the checks that pass. The exact number of false computation rows is not a count of independent manuscript errors: several rows can test the same error, a rejected reading or two generator images of one word.

`CHECK_EVENTS.tsv` records the statement, date, reviewer/run identity, event type and outcome. Model effort is described as not independently observable rather than invented. A later literature theorem whose statement and hypotheses were read is not labelled independently reproved. Counterexamples identify a refined statement; those records are collected in `audit/refined_statements.json`. Earlier-run and supporting editorial lemmas are in `audit/editorial_checks.json`. The alias map keeps events referring to pre-merger IDs usable.

The bibliography’s `note = {verified}` means that a URL or DOI was opened. It does not mean that every proof in the work was checked. `audit/reference_checks.json` distinguishes metadata access, a read theorem statement, a hypothesis comparison and a targeted proof check. Unopened backward-reference leads remain `unverified` and are not the sole support for a claimed resolution.

The compact audit preserves search requests, source identifiers, URLs, access failures, read ranges and hashes. It excludes the supplied attachment bodies, downloaded books and papers, and long duplicated retrieval excerpts. The calculation programs and this run’s proof notes are included in full. The source-reading and retrieval scripts can be rerun with the original attachment extracted under `sources/` and with appropriate network access. The final validation checks entry coverage, ID resolution, claim-search coverage, bibliography keys, event targets, source immutability and archive integrity; the results are saved with the dossier.

## 7. Counts

The following counts are computed from the final consolidated tables. They count records, not pages, independent theorems, newly discovered errors or currently open research problems. The source-entry total is fixed at380. Editorial checks and refined statements are reported separately so they cannot inflate the manuscript claims count.

| Category | Count |
|---|---|
| Indexed source entries | 380 |
| Retained scan blocks read | 242 |
| Package items before cross-package consolidation | 283 |
| Consolidated items | 264 |
| Explicit item-merger groups | 11 |
| Manuscript claim records | 255 |
| Author-problem records | 72 |
| Reading-register rows | 156 |
| Link rows, including explicitly unavailable project leads | 359 |
| Bibliography entries | 76 |
| Unverified backward-reference bibliography entries | 2 |
| Check events | 1057 |
| Claim-search ledger rows | 243 |
| Retained claims covered by search ledger | 255 |
| Separate editorial/supporting checks | 8 |
| Separately addressable refined statements | 53 |
| Ranked directions | 12 |

### Entry verdicts

| Category | Count |
|---|---|
| kept | 227 |
| merged | 107 |
| corrected | 45 |
| withdrawn | 0 |
| rests on a misreading | 1 |

### Item kinds

| Category | Count |
|---|---|
| conjecture | 9 |
| idea of the earlier run | 30 |
| other | 12 |
| reading question | 44 |
| self-flagged step | 35 |
| title, date or page count | 12 |
| unproved claim | 89 |
| unpursued implication | 20 |
| withdrawn in the same text | 13 |

### Claim classes

| Category | Count |
|---|---|
| A | 0 |
| B | 14 |
| C | 23 |
| D | 14 |
| E | 176 |
| F | 28 |

A: own later published work; B: developed by others into established results; C: partly developed; D: exact development not identified in the recorded searches; E: established earlier theory, with literal errors and corrected comparators distinguished in the fate field; F: not identifiable from the supplied reading/definition.

### Primary status on the pages

| Category | Count |
|---|---|
| proved there | 29 |
| proof sketched | 79 |
| stated without proof | 56 |
| corrected by himself later | 10 |
| false as stated | 35 |
| open on the pages | 46 |

Mixed records are counted once by their declared primary status. A proof-sketch record can contain an isolated erroneous formula, and a question can be answered in a later occurrence; the full status and present-status fields preserve those distinctions. This table is not an error census or a count of presently open problems.

### Links by kind

| Category | Count |
|---|---|
| folder | 97 |
| our projects | 224 |
| published work | 38 |

The our-projects rows are also supplied separately in `SA29_project_links.tsv`. Rows with an unavailable endpoint are leads with a recorded retrieval limit; they are not included by implication among completed two-endpoint mathematical comparisons.
