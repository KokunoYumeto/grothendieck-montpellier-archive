# H0K8 and H0KB — foundational entries

**Scope and attribution.** This entry covers the supplied zero-dimensional definition of form and the complete 156-3 span on networks through cuts, ordered tronçons, tame parts and their abstract relative calculus. Every item is in manuscript order. Short French phrases and close French paraphrases appear under **His words**; mathematical expansions, proofs, corrections and judgements are expressly this run's. A definition is decided through its well-definedness and stated properties. A programme is accompanied by separately decided precise versions; its label is not a substitute for deciding them.

**How to use the evidence.** `STATEMENTS.tsv` is the machine-readable register. `PROOFS.tex` is a LaTeX fragment containing full common proofs followed by a section for every statement ID, its application and second check. Counterexamples verify every relevant hypothesis. `READINGS.tsv` records decisive words, supplied readings, the ink, and the decision. `NOTES_VERDICTS.tsv` covers all six entries. `CHECK_EVENTS.tsv` distinguishes proof, independent re-proof, computation, use, and refutation. Reference keys below are resolved in `references.bib`; an unverified later manuscript is never treated as an opened primary source.

**Locators.** `156-3/024.8` means cote 156-3, supplied scan 024, physical text-line anchor 8 counted from the top of the manuscript text, excluding the handwritten page numeral and archive marks. Titles and dates count when on the text line; displayed formula baselines count. `m` denotes the margin attached to that baseline; an insertion belongs to its anchor. Compound locators list continuations. The handwritten page number in 156-3 is scan minus one. Closely packed additions can straddle baselines, so the quoted anchor and crop are also supplied in the reading register. The original scans are not duplicated in this package. The manuscript-style symbol ⊂ in the close paraphrases and tables denotes inclusion, not necessarily proper inclusion; proper inclusion is stated explicitly. The formulas in the proofs use the corresponding non-strict inclusion convention.

**Reading and checking limits.** All 41 supplied scans were directly viewed; decisive places were cropped and enlarged. No OCR was used on manuscripts. Searches of the complete supplied transcriptions located the other occurrences; one-dimensional F1–F6 material is linked under its proper object, not silently promoted to a completed definition of arbitrary forms. The finite computations are supplementary checks, not certificates for infinite or dense orders. A second proof in this package means a second argument by the same model in the requested single stream, not a claim of an external human review.

## H0K8 — forme

### 1. The object in his terms and in present language

**His terms.** A “forme de dim 0” is an “ensemble discret”, whose elements are its “lieux”. The margin distinguishes a “modèle”, carrying the equivalence relation “non disjoints”, from the associated quotient form. The surrounding heading proposes a construction by dimension.

**Present statement — ours.** The defined object is a set with the discrete topology. Its model is an equivalence relation on another set; its form is the set of equivalence classes, again regarded as discrete. The model is not its quotient: two equivalent places may determine a single place of the form. Neither finiteness nor nonemptiness is imposed here. The quotient's universal property is supplied in our proof, not quoted as a theorem written in the margin.

There is no defined general category of forms, no equivalence of all higher-dimensional models, and no recursive transition rule in this passage. This is a documentary limit on what is defined, not a claim that such a theory cannot be developed. The one-dimensional model axioms belong to H0KF; the pro-object questions in the contextual notes belong to H0KL.

### 2. Locations and dates, in his order

The decisive location is **156-1/002**, handwritten page 1, dated **5 June 1986**: the recursive heading at line 3, the zero-dimensional definition at line 6, and the model/quotient margin anchored there. The page then begins the dimension-one model. The supplied complete 156-1 transcription was searched for forme, modèle, dimension, lieux, quotient, and the model notation; the hits outside this base case concern the neighbouring segment/network objects. Cote 156-2, dated 6 June, is groundwork for ficelles used in H0KB, not a newly complete definition of arbitrary forms.

### 3. His statements and their disposition

#### H0K8.1 — 156-1/002.3

**His words (short quotations and close paraphrase).** Il propose une « construction récurrente » des formes par la dimension; la page commence par la dimension zéro puis passe aux modèles de dimension un.

**His state and date.** programme; 1986-06-05.

**Precise statement — ours.** A recursive definition of forms in all dimensions is requested. Higher stages, morphisms, equivalence of models and the recursion step are not defined here. The supported zero-dimensional versions are the next two rows.

**Status: programme.** Lemma Z identifies exactly the two defined constructions. A recursion would require its induction data and transition rule; these are absent. This row does not assert their nonexistence. The two precise versions below are separately decided.

**Reconstruction / correction — ours.** We separate an unfinished programme from its fully specified zero-dimensional base. No pro-object interpretation is inserted.

**Second check.** Documentary second check: search of the complete 156-1 transcription located the one-dimensional F1–F6 model axioms, whose object is H0KF; none supplies a category or recursive equivalence relation on general forms.

**Proof and confidence.** PROOFS.tex, section H0K8.1, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No verified completion of this exact recursion was located. The pro-object language belongs to neighbouring research planning, not this definition.

#### H0K8.2 — 156-1/002.6

**His words (short quotations and close paraphrase).** Une « forme de dim 0 » est un ensemble discret; ses éléments sont les « lieux » de la forme.

**His state and date.** stated; 1986-06-05.

**Precise statement — ours.** A zero-dimensional form is a set P equipped with the discrete topology. The sentence imposes neither finiteness nor nonemptiness.

**Status: True as written.** Lemma Z constructs the discrete topology \(\mathcal P(P)\) on any set and explains that this is a definition, with no further structure. The empty set and arbitrary cardinalities satisfy it.

**Reconstruction / correction — ours.** Our use of the discrete topology explicates « ensemble discret »; it does not equip the model L with a topology.

**Second check.** The diagonal equivalence relation on P produces the same object by the independent quotient construction in Z.

**Proof and confidence.** PROOFS.tex, section H0K8.2, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0K8.3 — 156-1/002.6m

**His words (short quotations and close paraphrase).** Un « modèle » est un ensemble L de lieux muni de la relation d’équivalence « non disjoints »; la forme du modèle est l’ensemble quotient.

**His state and date.** stated; 1986-06-05.

**Precise statement — ours.** For an equivalence relation ∼ on L, the associated form is the set L/∼, regarded as discrete. The model and its associated form are distinct constructions.

**Status: True as written.** Lemma Z proves existence, the equality criterion for classes, and the universal factorization property of \(q:L\to L/{\sim}\). A two-point model with all points equivalent has a one-point form, so identifying model and form is not licensed.

**Reconstruction / correction — ours.** The universal property is ours. The margin states the quotient itself; it states no pro-object construction.

**Second check.** The independent power-set image construction in Z avoids representatives and yields the same quotient.

**Proof and confidence.** PROOFS.tex, section H0K8.3, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

### 4. Groundwork and period language

The only mathematical prerequisites are a set, an equivalence relation and a quotient. The complete elementary construction is in PROOFS Z; the second construction realizes the quotient as an image in the power set and uses no choice of representatives. “Discrete” here means that every subset is open. There is no unspecified quotient topology on the model to preserve: the page gives the quotient as a set and calls the resulting form discrete.

EGA's topological language is relevant to the later network entry, but no EGA, SGA, FGA or Bourbaki theorem is needed to prove this elementary base case. No locator is fabricated for a published theory of these particular forms. In particular SGA's pro-object terminology cannot be inserted into this definition merely because the notes later propose a pro-object programme.

### 5. Subsequent status and present limits

The zero-dimensional construction is completely settled by the set-theoretic proof given here. The programme's supported base-case versions are both decided. The opened collected-works and author bibliographic sources did not supply a publication completing this exact dimension-by-dimension definition; this is a report of the search, not a proof of absence. Nothing in the verified EGA/SGA background turns the manuscript's model into a pro-object or completes its higher-dimensional recursion.

No fixed, fully specified higher-dimensional theorem is labelled open merely because the programme lacks its definitions. The programme row lists what additional definitions would be needed; its actual mathematical versions have their own rows and proofs. Our later research links, if any, are restricted to part 8.

### 6. Links to nearby objects

| Other tag | Relation | Evidence |
|---|---|---|
| H0KF | used by | 156-1/002.6 defines the zero-dimensional base, followed on the same scan by the dimension-one model. Nearby object H0KF owns the segment/end/branch axioms F1–F6; they are not a completed recursion of forms. |
| H0KL | same question elsewhere | Nearby H0KL is explicitly the notes’ P01–P16 programme on pro-objects and finite posets. No pro-object occurs in the zero-dimensional quotient definition. This is a comparison of programmes, not attribution to Grothendieck. |
| H0KB | used by | 156-3/002 uses the ensemble L des lieux and seeks cut data for network models; 156-1/002 separates underlying places, models and forms. No theorem equating the two tagged objects is asserted. |

### 7. The note entries: 1 verdict

**MPL_156-1+156-2#1.** Confirmed at 156-1/002.6 and the margin: discrete form, equivalence-relation model, quotient.

**Mathematical verdict — ours.** Confirmed for the zero-dimensional definition; corrected scope for the wider programme. Read in full. Model and form must remain distinct. No recursive definition in higher dimension, general category, or pro-object construction is supplied by this passage. The quotient proof and its independent power-set construction verify the precise base case.

**Placement.** H0K8.1; H0K8.2; H0K8.3; H0K8 groundwork and links. Correct object: H0K8; higher model and research-programme material links to H0KF/H0KL.

### 8. Our supplied research results, kept separate

The results folder was opened only after the substantive entry draft had been written; the UTC event is recorded in progress.log. It supplied no research-statement row bearing on these objects. CONSEQUENCES.tsv therefore has its header and no forced links. The proofs labelled ours in this entry are work of this run, not pre-existing results imported from that folder.

## H0KB — réseaux via découpages; tronçons; parties modérées

### 1. The object in his terms and in present language

**His terms.** On the set \(L\) of lieux, \(\mathfrak S_0\subset\mathfrak P_2(L)\) selects the “0-sphères plongées”. A finite “partie modérée” is a finite clique. Its “complémentaire modéré” \(C(T)\) contains only the points outside \(T\) that are compatible with every member. The relations \(R_T\) partition these complements, and each class is assigned a finite frontier. After provisional axioms he studies the ordered example: lignes, tronçons, sous-tronçons, closed tame parts, then pseudo-tronçons and general tame parts. Finally he abstracts their order, compatibility, complement and closure.

**Present framework — ours.** The central order is a **partial order**, not a linear order. Write **G** for the following exact package of his coherent quantified axioms:

1. \(L\) has at least two elements and is globally directed in both directions: every pair has a common lower and a common upper bound.
2. It is dense: \(a<b\) admits \(a<c<b\).
3. Its nonempty strict upper cones are downward directed: \(a<x,y\) admits \(a<z\leq x,y\); the dual holds for strict lower cones.

All later occurrences of G refer to this full list. Neither totality, completeness nor topological separation is implicit. The variable slips in an explanatory line do not erase the explicit filtered-cone clauses; both ink and correction are recorded.

For a finite chain \(t_1<\cdots<t_n\), the canonical \(R_T\)-classes are its strict gaps and exterior rays, with empty exterior rays omitted. These data recover strict betweenness by a disjointness test on two cut classes, then recover the order up to a simultaneous reversal after choosing one oriented pair. This is the main positive theorem. Our explicit anchored formulas provide a finite first-order recognition scheme for exactly this class, in every cardinality; they are not an axiom list attributed to the manuscript.

**The central failure and exact repair — ours.** His later calculus treats interval endpoints, compatible complements and least closed tame hulls as intrinsic to actual subsets. G does not ensure that. On \(\mathbb Q\times\{0,1\}\), strict comparison of rational heights satisfies every G axiom, but the two points of height zero give the same strict lower ray. It has two endpoint presentations and no least finite closed tame hull.

The exact additional all-rays condition is

\[
\tag{E}a=\sup\{x:x<a\},\qquad a=\inf\{x:a<x\}\quad(a\in L),
\]

with the empty-cone convention at an ambient extremum. Within G, **E is necessary and sufficient for every nonempty strict principal ray to have a least closed tame hull**. Under E the entire finite compatible interval calculus follows, including intrinsic endpoints, complement, closure, relative structure and tame components. E is not present in the original definition, and adding it is a substantive correction. Total orders satisfy it, but the repaired class also contains non-total orders.

Under G+E, finite compatible families sit in common finite Boolean algebras made from endpoint cells. Their join can fill points incomparable with an intermediate endpoint, so it need not be ordinary set union. Inclusion alone recovers compatibility: recover point atoms, test which pairs of atoms have joins, recover the compatible complement as a comparability polar, and use the three disjoint Boolean pieces. The proposed shortcut “a meet exists” fails even under E.

The canonical topology, the closed-subbasis topology, and their supremum are distinguished throughout. G can fail T₀; even T₀ G can fail sobriety; T₁ does not force totality. The narrower assertion for genuine ficelle lieux also fails: a compact tree with a side hair gives distinct loci with identical strict cones. Reverse-inclusion specialization is proved at targets satisfying the additional connected-component condition W_D, in particular at connected targets. The abstract relativization theorem is also valid when its explicitly stated axioms are assumed. Its hope that every clopen is universally compatible is false, as a six-element example shows. The separate claim that a family's generated Boolean algebra equals the whole endpoint subdivision algebra is false even on the real line.

### 2. Locations and dates, in his order

The archive title gives **8 June 1986**, sheet III. The body spans supplied scans **002–041**, handwritten pages **1–40**. Scan **022** begins the **9 June** continuation; no later date is invented for subsequent pages.

| Scans | Development |
|---|---|
| 002–006 | Cut data, finite cliques, tame complement, two forecasts and provisional axioms |
| 007–011 | Ordered lines and tronçons, endpoint cases and finite cuts |
| 011–017 | Recovery from betweenness and pair cuts; request for recognition axioms |
| 018–021 | Closed parts, normal forms, relative frontiers, joins, arbitrary-hull warning and cancelled ordinary difference |
| 022–024 | Relative difference; canonical topology, ficelle specialization and separation/closure questions |
| 025–032 | New boundary conventions, endpoint removal, pseudo-pieces, interstices, tame complement and order-only question |
| 033–034 | Concrete properties 1–7 and strengthened compatible Boolean blocks; algebraic interior/frontier |
| 035–039 | Conditional abstract relativization, clopens, spectra and tame components |
| 040–041 | Generated-subdivision claim, index slip, and unfinished recognition exercise with historical aside |

The supplement 156-2, scans 002–010, was obtained from the original archive solely to check the ficelle hypotheses invoked on 022–024. Its full theory remains H0KI/H0KJ. No mathematical assertions from later uninspected manuscript pages are silently added.

### 3. His statements and their disposition

#### H0KB.1 — 156-3/002.3

**His words (short quotations and close paraphrase).** Il veut « une autre axiomatique » de la structure de réseaux sur l’ensemble L des lieux, en termes de découpages.

**His state and date.** programme; 1986-06-08 (folder date).

**Precise statement — ours.** Specify tame pairs, equivalence relations on finite tame complements and their frontiers, with sufficient axioms to recognize networks. The general class is not yet axiomatized; the displayed provisional systems and the ordered-tronçon recognition problem are the supported precise versions.

**Status: programme.** Lemma N checks the provisional systems; lemmas R and A settle the exact ordered subclass. There is no defined general-network class whose equivalence to the earlier segment axioms can be inferred from this heading alone.

**Reconstruction / correction — ours.** The general programme remains descriptive; every explicit mathematical version below is separately decided.

**Second check.** Compared the data on scans 2–6 with the concluding exercise on 41: the latter explicitly restricts to the ordered situation.

**Proof and confidence.** PROOFS.tex, section H0KB.1, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.2 — 156-3/002.6

**His words (short quotations and close paraphrase).** S₀⊂P₂(L) est l’ensemble des « 0-sphères plongées »; une partie finie T est modérée si P₂(T)⊂S₀. Deux lieux égaux sont aussi en position relative modérée.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** A symmetric irreflexive graph on L specifies distinct compatible pairs; finite tame sets are its finite cliques, including the empty set and singletons. Reflexive compatibility adds equality.

**Status: True as written.** For any \(S_0\subseteq\mathcal P_2(L)\), the clique condition is well defined and hereditary under subsets. The union of two finite cliques is a clique precisely when every cross pair is equal or belongs to \(S_0\). This proves the stated relative-compatibility rule.

**Reconstruction / correction — ours.** His explanation through the earlier segment model is a link to H0KF, not a new axiom silently imposed here.

**Second check.** Independently inspect each two-element subset of the union: it lies in the first set, second set, or is a cross pair.

**Proof and confidence.** PROOFS.tex, section H0KB.2, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.3 — 156-3/002.10

**His words (short quotations and close paraphrase).** Dans l’axiomatique par les segments, une paire est modérée si un lieu est singulier, ou si les lieux réguliers sont sur des lignes différentes, ou sont les extrémités d’un segment dans la même ligne.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Given the earlier network data of singular places, regular lines, and two-ended segments, this rule constructs the symmetric graph S₀ on distinct places. It is an interpretation of the datum, not yet an equivalence theorem for the provisional cut axioms.

**Status: True as written.** Each of the three conditions is invariant under exchanging the two places. Restricting to two-element subsets excludes equality, and adding equality gives the reflexive compatibility relation already stipulated. Thus the construction of S₀ is well defined from those earlier data. Nothing in this bracket proves that arbitrary provisional cut systems arise from such segment networks; N supplies countermodels to weaker claimed consequences.

**Reconstruction / correction — ours.** We preserve the earlier model’s terms. H0KF owns its F1–F6 axioms; H0KG/H0KH own the orientation and regular-network constructions. The bracket defines a graph from them without settling a converse.

**Second check.** The three alternatives are checked directly against the bracket on scan 2 and the definition of singular/regular places in the searched 156-1 model passages.

**Proof and confidence.** PROOFS.tex, section H0KB.3, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.4 — 156-3/003.4

**His words (short quotations and close paraphrase).** C_L(T) est l’ensemble des t∉T tels que T∪{t} soit modéré; il l’appelle « complémentaire modéré ».

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For a finite clique T, C(T)={x∈L∖T: every t∈T is compatible with x}. It can omit points outside T.

**Status: True as written.** Every two-point subset of \(T\cup\{x\}\) already lies in T or is \(\{t,x\}\). Thus the displayed condition is exactly the cross-pair condition, with x excluded from T. This proves both descriptions.

**Reconstruction / correction — ours.** No set-theoretic complement is substituted for the manuscript’s tame complement.

**Second check.** For a singleton in D, the other twin is outside T but outside C(T), explicitly checking that the word complement is qualified.

**Proof and confidence.** PROOFS.tex, section H0KB.4, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.5 — 156-3/003.6m

**His words (short quotations and close paraphrase).** Si T′⊂T, alors C(T)⊂C(T′).

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** T′⊂T implies C(T)⊂C(T′) for finite tame sets in any compatibility graph.

**Status: True as written.** If x avoids T and is compatible with every point of T, it avoids T′ and is compatible with every point of T′. This is lemma C.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Check the two requirements separately: nonmembership descends with subset inclusion, and the universal compatibility condition restricts.

**Proof and confidence.** PROOFS.tex, section H0KB.5, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.6 — 156-3/003.6m

**His words (short quotations and close paraphrase).** Il demande si T est connu par C(T), puis écrit « Oui » pour l’inverse de l’inclusion, et revient au NB : T est connu par C(T).

**His state and date.** sketched; 1986-06-08 (folder date).

**Precise statement — ours.** The proposed map T↦C(T) is injective and reflects reversed inclusion for arbitrary finite tame sets.

**Status: False.** In D of lemma D, distinct singleton twins have identical tame complements. All G hypotheses and their singleton tameness are verified there, so the failure persists in the intended ordered subclass. The strongest direct general-graph repair is: if S∪T is tame, then C(S)⊂C(T) iff T⊂S. For t∈T\S, compatibility of the union gives t∈C(S) but t∉C(T), a contradiction.

**Reconstruction / correction — ours.** Add the missing hypothesis S∪T tame. It is exactly the condition needed by his attempted witness argument; it is not present in the written assertion.

**Second check.** The twin computation checks equality point by point at height 0 and at every other height. The repaired converse is also verified by its explicit witness t.

**Proof and confidence.** PROOFS.tex, section H0KB.6, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.7 — 156-3/003.15

**His words (short quotations and close paraphrase).** Le NB écrit « s≠t ou {s;t}∈S₀ » pour la position relative modérée.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Taken literally, this makes all distinct points compatible and fails reflexivity. The preceding margin on scan 2 instead says s=t or {s,t}∈S₀.

**Status: Slip.** With \(S_0=\varnothing\) on a two-point set, the printed disjunction holds for the distinct pair, contrary to its definition, and fails for equal points. Replacing \(\ne\) by \(=\) gives exactly the finite-clique compatibility rule proved in H0KB.2.

**Reconstruction / correction — ours.** Our slip judgment: replace ≠ by =, using the explicit reflexive margin on 156-3/002.

**Second check.** The cropped sign agrees with the supplied ≠ reading; the correction is mathematical and supported by scan 2, not a transcription emendation.

**Proof and confidence.** PROOFS.tex, section H0KB.7, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.8 — 156-3/003.18;156-3/004.1

**His words (short quotations and close paraphrase).** Pour chaque T modéré fini, il donne une relation d’équivalence R_T dans C(T); pour chaque classe A, une partie Ȧ⊂T, appelée « frontière ».

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The data consist of arbitrary equivalence relations R_T on the specified domains and designated subsets ∂_T A⊂T. Calling their classes components makes no topological assertion.

**Status: True as written.** Equivalence relations partition each domain; an arbitrary subset of T may be assigned to each class. The indiscrete and discrete systems of N give explicit realizations. Empty domains carry the unique empty relation and have no classes.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The examples in N separately realize one-class and singleton-class choices, showing that no unseen topology is part of the definition.

**Proof and confidence.** PROOFS.tex, section H0KB.8, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.9 — 156-3/004.5

**His words (short quotations and close paraphrase).** « Je prévois » que c résulte de b, et que b résulte des R_ε pour ε∈S₀, après choix d’axiomes.

**His state and date.** hoped; 1986-06-08 (folder date).

**Precise statement — ours.** Find additional axioms under which frontiers are determined by partitions and all finite partitions by the two-point partitions. The unspecified additional axioms are part of the programme.

**Status: programme.** With unspecified axioms this is not a fixed implication. The next two rows test the displayed provisional axioms; R and A prove the ordered-troncon version with its actual canonical cuts.

**Reconstruction / correction — ours.** We do not refute the existence of a suitable eventual axiom system. We decide both supported provisional implications below.

**Second check.** The wording explicitly precedes « Axiomes provisoires » and does not claim the forthcoming short list is final.

**Proof and confidence.** PROOFS.tex, section H0KB.9, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.10 — 156-3/004.8

**His words (short quotations and close paraphrase).** Première prévision : la donnée c, les frontières Ȧ, résulte déjà de b, les relations R_T.

**His state and date.** hoped; 1986-06-08 (folder date).

**Precise statement — ours.** Precise provisional version: S₀ and all R_T determine all ∂_T A among systems satisfying Dec₁, Dec₂ and the finite-maximal-cut axiom displayed on scans 5–6.

**Status: False.** Lemma N gives two systems on Q with identical S₀ and identical indiscrete R_T; their frontiers are respectively empty and T. It verifies every provisional clause. The ordered-troncon correction is true: canonical gaps have exactly their adjacent cut points as frontiers, by C, and R recovers all gap data from pair cuts.

**Reconstruction / correction — ours.** This is our explicitly delimited version under the provisional axioms, not a reading that his unknown future axioms are refuted.

**Second check.** Independent frontier check in N is the identity S∩T=T in the nonempty-frontier system, versus the empty inclusion in the other.

**Proof and confidence.** PROOFS.tex, section H0KB.10, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.11 — 156-3/004.10

**His words (short quotations and close paraphrase).** Deuxième prévision : tous les R_T résultent des seuls R_ε pour les paires ε∈S₀.

**His state and date.** hoped; 1986-06-08 (folder date).

**Precise statement — ours.** Precise provisional version: the two-point partitions determine every finite-cut partition under the same displayed provisional axioms.

**Status: False.** Lemma N compares the all-indiscrete system with the system split by sign only at cuts of cardinality at least three. Both have empty frontiers and satisfy all provisional clauses; they agree on pair cuts but differ on triple cuts. The exact canonical ordered-troncon version is proved by R and A.

**Reconstruction / correction — ours.** Additional recognition axioms are necessary; A supplies a complete finite scheme for the ordered subclass.

**Second check.** The three cardinality cases in N check every possible refinement, including a two-point cut refined by a three-point one.

**Proof and confidence.** PROOFS.tex, section H0KB.11, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.12 — 156-3/005.1

**His words (short quotations and close paraphrase).** Si U est à la fois modérée finie et modérée cofinie, il prend S,T finis disjoints, S∪T modéré, et écrit que « tout u∈L modéré » par rapport à S est dans T; il en déduit S∪T maximal puis discret.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The argument needs C(S)=T: every point OUTSIDE S compatible with S lies in T. Its literal clause omits outside S, although relative compatibility was declared reflexive. With that repair and the proposed maximal-finite-cut axiom, S∪T=L and the structure is discrete.

**Status: Slip.** For a two-point complete graph with S={s}, T={t}, the intended C(S)=T holds, while the literal clause fails at u=s. The corrected equivalence is direct: S∪T tame gives T⊆C(S), and the repaired universal clause gives C(S)⊆T. Any point outside S∪T extending that clique would belong to C(S)=T, a contradiction; thus S∪T is maximal. Applying the explicitly proposed maximal-cut axiom gives the stated discrete conclusion. Conversely, a finite discrete structure has precisely these cofinite complements.

**Reconstruction / correction — ours.** Our omitted-convention judgment is supported by the immediately preceding definition of C(S), which excludes S. The supplied phrase is retained, not silently rewritten. The discreteness conclusion uses the proposed axiom, not the graph data alone.

**Second check.** The counterexample uses the explicit reflexive convention on scan 2. A second check compares each of the two inclusions in C(S)=T separately, then tests a hypothetical point extending S∪T.

**Proof and confidence.** PROOFS.tex, section H0KB.12, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.13 — 156-3/005.14

**His words (short quotations and close paraphrase).** La structure « discrète » a S₀=P₂(L), C_T=L∖T, R_T discrète et Ȧ=∅.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** These data define a coherent cut system for every set L. It satisfies Dec₁ exactly when L is finite, and always satisfies Dec₂.

**Status: True as written.** Lemma N verifies the equality partitions and empty frontiers. Applying Dec₁ to T=∅ proves necessity of finite L; a finite L makes every quotient finite. His data alone do not claim that an infinite discrete model obeys the later finiteness condition.

**Reconstruction / correction — ours.** We distinguish the valid definition from the restriction imposed one page later.

**Second check.** Count the singleton classes directly: |C(∅)/R_∅|=|L|.

**Proof and confidence.** PROOFS.tex, section H0KB.13, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.14 — 156-3/005.23

**His words (short quotations and close paraphrase).** « Axiome » : si T est une partie finie modérée maximale, alors T=L et L est discret.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** This is a proposed additional axiom: any maximal finite clique must equal L, with the discrete cut data. It is consistent, but is not a consequence of an arbitrary S₀.

**Status: True as written.** Finite discrete systems satisfy it; canonical G-orders have no maximal finite clique, since density inserts another point in any comparable gap and global bounds extend singleton or empty chains. Hence it holds vacuously there. The edge-plus-isolated-vertex graph in N shows why it must be imposed.

**Reconstruction / correction — ours.** Status concerns a coherent proposed axiom, not a theorem falsely derived from the preceding data.

**Second check.** Check the two cases independently: maximal finite clique in a finite complete graph is all of L; no finite chain in a nontrivial dense globally bidirected order is maximal.

**Proof and confidence.** PROOFS.tex, section H0KB.14, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.15 — 156-3/006.1;156-3/008.4m

**His words (short quotations and close paraphrase).** Les hypothèses de finitude sont « peut-être provisoires »; il note « refaire, sans se borner à une ligne ».

**His state and date.** programme; 1986-06-08 (folder date).

**Precise statement — ours.** Extend the line example to tronçons with possible endpoints and reassess finiteness. Supported versions are the G definition, endpoint cut counts and interval inheritance below.

**Status: programme.** G and C give the complete supported extension. The words propose no further quantified finiteness theorem. The discrete restriction is already decided in H0KB.13.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The later definition on 9 and the explicit endpoint cases on 11 supply the versions, so no unsupported higher-dimensional finiteness claim is invented.

**Proof and confidence.** PROOFS.tex, section H0KB.15, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.16 — 156-3/006.4

**His words (short quotations and close paraphrase).** Dec₁ : l’ensemble des composantes connexes de tout U=C(T) est fini.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Dec₁ is finiteness of each quotient C(T)/R_T. Canonical finite cuts in G satisfy it with at most |T|+1 classes.

**Status: True as written.** Lemma C explicitly lists the finite fibers, including the empty-cut case; there are at most n+1. This proves consistency and the claimed ordered realization.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The integer index x↦#{t∈T:t<x} has at most n+1 values.

**Proof and confidence.** PROOFS.tex, section H0KB.16, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.17 — 156-3/006.7

**His words (short quotations and close paraphrase).** Pour U=C(S), V=C(T), il écrit « U⊂V i.e. T⊂S ».

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The equivalence of these two conditions is proposed for arbitrary finite tame cuts. Only T⊂S⇒C(S)⊂C(T) holds without extra compatibility.

**Status: False.** Use the two singleton twins of D: C(S)=C(T), while neither singleton contains the other. The implication from cut inclusion is H0KB.5. If S∪T is tame, the converse is exactly the corrected witness argument in H0KB.6.

**Reconstruction / correction — ours.** Replace « i.e. » by the explicit assumption T⊂S, or require S∪T tame when asserting equivalence.

**Second check.** Direct equality at every height checks the counterexample without appealing to an abstract noninjectivity assertion.

**Proof and confidence.** PROOFS.tex, section H0KB.17, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.18 — 156-3/006.9

**His words (short quotations and close paraphrase).** Chaque classe A de U est contenue dans une unique classe B de V; de plus Ȧ∩T⊂Ḃ.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For T⊂S, canonical G-cut partitions refine under restriction, and their adjacent-cut frontiers satisfy ∂_S A∩T⊂∂_T B.

**Status: True as written.** Lemma C proves refinement by deleting some of the ordered cut points. A smaller gap lies between consecutive surviving old cuts, so lies in their unique gap. Any old cut retained as an adjacent endpoint of the smaller gap is one of those two bounding old cuts.

**Reconstruction / correction — ours.** The genuine refinement assertion is separated from the false preceding « i.e. ».

**Second check.** The integer-fiber description independently merges adjacent fibers when cuts are deleted.

**Proof and confidence.** PROOFS.tex, section H0KB.18, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.19 — 156-3/007.1

**His words (short quotations and close paraphrase).** Une « ligne ordonnée » est filtrante croissante et décroissante, sans plus grand ni plus petit élément, localement filtrante dans les deux sens et divisible.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** This is G without ambient extrema. It is a partial order; totality is not among its axioms.

**Status: True as written.** Lemma G expands every axiom. D and the strict-coordinate plane P satisfy them, proving that the class is nonempty and genuinely includes non-total orders.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** In D both global and local requirements reduce to rational-height interpolation; in P they reduce to two independent strict coordinate inequalities.

**Proof and confidence.** PROOFS.tex, section H0KB.19, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.20 — 156-3/007.8

**His words (short quotations and close paraphrase).** S₀ est l’ensemble des paires totalement ordonnées; Mod_f(L) est l’ensemble des drapeaux finis; un drapeau t₁<⋯<t_n donne n+1 composantes avec les points frontière indiqués.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For a nonempty finite chain on an endpoint-free G, C(T) has the n+1 strict gaps and their adjacent-cut frontiers; the empty chain has the one class L.

**Status: True as written.** Lemma C proves that the strict gaps partition C(T). Density makes internal gaps nonempty; absence of extrema makes both exterior gaps nonempty. The boundary assignments are precisely the neighboring cut points.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Count index fibers 0 through n, each realized; this independently gives n+1.

**Proof and confidence.** PROOFS.tex, section H0KB.20, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.21 — 156-3/008.1

**His words (short quotations and close paraphrase).** La structure ne change pas sous l’ordre opposé. Les tronçons fermés de la ligne sont [s,t], les demi-droites fermées et L; leurs réunions finies disjointes mutuellement modérées sont dites modérées.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The cut and finite closed-piece structures are invariant under simultaneous order reversal. Closed pieces may be singleton intervals; compatible disjoint finite unions have intrinsic components and finite frontier.

**Status: True as written.** Reversal exchanges left and right gaps, preserving their unordered partitions and endpoint sets. For closed pieces all finite endpoints belong to the pieces; the closed-part case of F proves uniqueness and the boundary-union rule without E.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Reversing each endpoint inequality leaves the interval subset unchanged and reverses only its presentation order.

**Proof and confidence.** PROOFS.tex, section H0KB.21, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.22 — 156-3/008.4m;156-3/018.1

**His words (short quotations and close paraphrase).** Un sous-tronçon fermé d’un tronçon est encore un tronçon pour le biordre induit; il permet ensuite de retirer des extrémités.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Every nondegenerate interval or nonempty ray of any endpoint type in G satisfies G in the induced order. Singleton pieces are separately called large or pseudo-tronçons.

**Status: True as written.** The interval-inheritance proof in G supplies internal common bounds from the local axioms at omitted endpoints, uses included endpoints where available, and inherits density and the smaller local cones. Nonempty strict intervals are nondegenerate by repeated interpolation.

**Reconstruction / correction — ours.** This assertion concerns order structure; it does not make these subsets topologically closed.

**Second check.** The finite-cone proof in G independently checks that both of two selected points have a common bound still inside the interval.

**Proof and confidence.** PROOFS.tex, section H0KB.22, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.23 — 156-3/009.4

**His words (short quotations and close paraphrase).** Les axiomes a), a′), b), c), d) définissent le « tronçon ordonné » : filtrations locales, bornes communes, divisibilité et card L>1.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** G is exactly the partial-order axiom list in the common proofs: nontrivial, globally upper and lower directed, order-dense, with every nonempty strict upper cone downward directed and every strict lower cone upward directed.

**Status: True as written.** Lemma G checks consistency, duality and the meaning of each filtering condition. The explanatory variable slips are recorded separately below; they do not replace the clearly stated filtering axiom.

**Reconstruction / correction — ours.** Our spelling-out of filtering uses the period nonempty convention; no endpoint regularity E is added to his definition.

**Second check.** Each of D, P and J independently realizes all five conditions.

**Proof and confidence.** PROOFS.tex, section H0KB.23, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.24 — 156-3/009.6

**His words (short quotations and close paraphrase).** Les lignes explicatives de a), a′), b) portent des a là où les autres termes et quantificateurs demandent x, notamment a>a et a,y≤z<a.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The literal repeated-variable glosses are inconsistent or vacuous and do not express the two filtering conditions. Replace the stray a labels in the x positions by x, retaining the quantified base point a.

**Status: Slip.** The literal a>a antecedent can never hold, so cannot characterize downward directedness of a nonempty strict upper cone. The dual conclusion a≤z<a is impossible: on Q, x=−2,y=−1,a=0 satisfy the intended premise but no z satisfies that literal conclusion. The corrected glosses are exactly a<x,y⇒∃z(a<z≤x,y) and x,y<a⇒∃z(x,y≤z<a). They are equivalent to the filtering phrases by definition.

**Reconstruction / correction — ours.** These are explanatory pen slips; G is read from the explicitly named filtering properties, not weakened by vacuous antecedents.

**Second check.** The repeated variables and at least the contradictory dual conclusion are visible in the crop. The formulas are also checked against the unambiguous global-bounds display and the later inheritance arguments.

**Proof and confidence.** PROOFS.tex, section H0KB.24, including its cited full common proof. High for the logical correction; medium for individual a/x penforms, with the decisive contradictory placement retained in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.25 — 156-3/009.18;156-3/010.1

**His words (short quotations and close paraphrase).** Segment : deux extrémités; intervalle : aucune; demi-intervalle : une seule. L’opposé est du même type. ∂L est l’ensemble du plus petit et du plus grand élément existants.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Exactly one of the three endpoint types occurs; a half-interval has two orientations. ∂L has 0,1 or 2 elements, and reversal preserves it.

**Status: True as written.** In a globally directed poset a maximal element is greatest, and a minimal element least, as proved in G. There is at most one of each; they are distinct because |L|>1. The four existence patterns group into precisely the three named types.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Enumerate the two binary endpoint-existence choices; reversal exchanges the two one-end choices.

**Proof and confidence.** PROOFS.tex, section H0KB.25, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.26 — 156-3/010.15;156-3/011.1

**His words (short quotations and close paraphrase).** Pour un tronçon, S₀=Drap₂(L), Mod_f(L)=Drap(L), et C(S) contient les t∉S qui rendent S∪{t} totalement ordonné.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Finite tame sets are exactly finite chains, and C(S) consists of points outside S comparable to every point of S.

**Status: True as written.** The clique condition for distinct comparability is precisely totality of the restricted partial order. The cross-pair computation of H0KB.4 then gives the displayed C(S).

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Every pair in S∪{t} is tested separately; no transitive orientation needs to be chosen beyond the given order.

**Proof and confidence.** PROOFS.tex, section H0KB.26, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.27 — 156-3/011.6

**His words (short quotations and close paraphrase).** La liste des composantes porte des crochets fermés [s₁,s₂], …, [s_{n−1},s_n] au milieu des deux cônes stricts.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** The literal closed internal intervals contain cut points and cannot be classes in C(S). They must be the strict gaps (s_i,s_{i+1}).

**Status: Slip.** On Q with S={0,1}, the printed [0,1] contains 0,1, excluded from C(S). Replacing it by (0,1) gives the partition proved in C. The preceding list on scan 7 and the subsequent three-point calculation on 16 both use strict gaps.

**Reconstruction / correction — ours.** Our slip judgment is supported by his own domain C(S) and his correct lists on 7 and 16.

**Second check.** Cropped brackets are visibly closed; they are not silently transcribed as open. The integer-fiber proof verifies the corrected partition.

**Proof and confidence.** PROOFS.tex, section H0KB.27, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.28 — 156-3/011.13

**His words (short quotations and close paraphrase).** Il écrit « les seules non vides éventuelles » pour L_<s₁ si s₁ est le plus petit élément, et L_>s_n si s_n est le plus grand.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Only the exterior gaps can be empty; the left is empty exactly at an ambient minimum and the right exactly at an ambient maximum.

**Status: Slip.** For L=[0,1] and s₁=0 the displayed left tail is empty, directly contradicting the word non. Dropping non yields the claim in C. With n=0 there is one component L; with n=1 there are one or two nonempty tails; with n≥2 there are n−1 internal gaps plus the nonempty tails.

**Reconstruction / correction — ours.** Keep the visible words in the record; delete only « non » in the corrected mathematical statement.

**Second check.** The endpoint-existence characterization in G and density independently rule out every other empty gap.

**Proof and confidence.** PROOFS.tex, section H0KB.28, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.29 — 156-3/011.18

**His words (short quotations and close paraphrase).** Il dit récupérer le biordre du tronçon, donc a), b), c), à partir des paires modérées et des R_T pour T∈S₀.

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** For every G of any cardinality, distinct comparability and the canonical two-point cut equivalence relations determine its order up to simultaneous reversal, hence all canonical finite cuts and frontiers.

**Status: True as written.** Apply R2 to recover strict betweenness from the disjointness of the indicated two cut classes. Density supplies the nonempty alternative intersections. Recover reflexive comparability and N, select one oriented pair a<b, and apply R1. C then reconstructs every finite cut and its adjacent frontiers. All hypotheses are exactly G.

**Reconstruction / correction — ours.** The explicit anchored formula and all-cardinality proof are ours; the page gives the same strategy and its local lemma.

**Second check.** The independent two-orders orientation argument in R verifies uniqueness without reusing the reconstruction formula.

**Proof and confidence.** PROOFS.tex, section H0KB.29, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** Courcelle 2020, Definition 3.1 and Theorem 3.5(2), pp.3–6, proves the corresponding strong B-minimal reconstruction in his stated finite/countable universe. Our argument does not impose that restriction.

#### H0KB.30 — 156-3/012.2

**His words (short quotations and close paraphrase).** Le biordre est connu par R(a,b,c), « b est strictement entre a et c »; a et b distincts sont comparables ssi un c est entre eux.

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** In G, B(x,y,z)⇔x<y<z or z<y<x determines distinct comparability by ∃y B(x,y,z), and determines the order up to reversal.

**Status: True as written.** The forward implication to comparability is transitivity; the reverse is density. With this derived C, R1 reconstructs the oriented order. Global bounds and |L|>1 ensure an anchor pair exists.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Repeated interpolation between an existing comparable pair also proves the marginal observation that finite chains of arbitrary length exist. The independent proof in R verifies uniqueness.

**Proof and confidence.** PROOFS.tex, section H0KB.30, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.31 — 156-3/012.6m

**His words (short quotations and close paraphrase).** Le NB remplace l’entre-deux non strict par l’entre-deux strict ou « {a,b,c} est un drapeau de cardinal ≤2 ».

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** N(a,b,c) means a≤b≤c or c≤b≤a. The shorthand using only a two-element chain is too broad when a=c≠b.

**Status: Slip.** On Q, (a,b,c)=(0,1,0) satisfies the printed cardinality/chain condition but not N. The exact repair is B(a,b,c) or ((a=b or b=c) and C(a,c)). All equality patterns are covered: three equal, equal first two, equal last two; equal outer arguments require all three equal.

**Reconstruction / correction — ours.** An evident shorthand omission, judged against his explicit inequalities a≤b≤c or the reverse; the crop confirms the supplied ≤2 text.

**Second check.** Enumerate these four repetition patterns separately. This is independent of the proof of order reconstruction.

**Proof and confidence.** PROOFS.tex, section H0KB.31, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.32 — 156-3/013.1

**His words (short quotations and close paraphrase).** Choisir une origine a dans {a,b}; les cônes L_≤a, L_≥b et l’intervalle ]a,b[ sont déterminés par R. Pour u≤v, il faut et suffit des bornes x≤a, y≥b avec x≤u≤v≤y.

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** For fixed a<b, the D,U formulas and R1 of the common proof define the oriented order from B. Either of the two additional nonstrict betweenness conditions in his display suffices.

**Status: True as written.** Global directedness supplies x≤a,u and y≥b,v when u≤v. Conversely the two endpoint-between conditions place u,v in [x,y], and N(x,u,v) forces u≤v; its dual N(u,v,y) also suffices. This is proved in R without assuming u,v already comparable.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Exhaustive bounded-poset enumeration in check_finite.py verifies the relaxed formula on 408 finite posets and 6057 anchors; the independent mathematical proof in R handles all cardinalities.

**Proof and confidence.** PROOFS.tex, section H0KB.32, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.33 — 156-3/014.2

**His words (short quotations and close paraphrase).** Le lemme nomme x,y,u,v « trois éléments »; a) u,v sont entre x,y; b) u entre x,v, ou c) v entre u,y; d) x<y; alors x≤u≤v≤y.

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** For four named, not necessarily distinct elements, the displayed betweenness hypotheses imply the displayed chain; either b) or c) suffices.

**Status: Slip.** The literal word trois mismatches four names and cannot be a general restriction to three distinct points: 0<1<2<3 satisfies the intended lemma. Replace trois by quatre (allowing coincidences). R proves the implication, including the equality cases: the reverse orientation in N(x,u,v) can occur only when u=v=x.

**Reconstruction / correction — ours.** Only the count word is corrected; the lemma’s mathematical inequality is true as displayed.

**Second check.** The program checks all 38169 satisfied four-point antecedents in its bounded-poset sample. The direct inequality proof is independent and exhaustive for arbitrary posets.

**Proof and confidence.** PROOFS.tex, section H0KB.33, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.34 — 156-3/014.18;156-3/015.1

**His words (short quotations and close paraphrase).** Il note que la divisibilité a seulement servi à déduire les paires de l’entre-deux; si l’on donne les deux relations, la filtration croissante et décroissante suffit.

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** A nontrivial globally upper and lower directed poset is reconstructible up to reversal from comparability and strict betweenness, with no density or local cone filtering assumption.

**Status: True as written.** Use the given C to define N and R1. Its proof uses only common upper/lower bounds and an oriented comparable pair. A comparable distinct pair exists from common bounds of two distinct points.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The finite bounded-poset enumeration targets precisely this weakened statement; its samples are not misleadingly called dense tronçons.

**Proof and confidence.** PROOFS.tex, section H0KB.34, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.35 — 156-3/015.7;156-3/016.1

**His words (short quotations and close paraphrase).** Pour a<b<c, les classes X_{ab},X_{bc},X_{ca} sont L_>b,L_<b,]a,c[; leurs intersections sont ∅,]b,c[,]a,b[. « On gagne ! »

**His state and date.** proved on the page; 1986-06-08 (folder date).

**Precise statement — ours.** For a distinct three-point chain, b is the middle point exactly when the class of c in C({a,b}) and the class of a in C({b,c}) are disjoint. The two other intersections are the nonempty adjacent gaps.

**Status: True as written.** Intersect the three displayed interval/ray sets directly. The two nonempty intersections use density. For each of the other choices of middle point relabel the triple, proving R2 for all six oriented orders.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The independent check enumerates the three possible middle labels rather than inferring them from a diagram. Reversal leaves all class intersections unchanged.

**Proof and confidence.** PROOFS.tex, section H0KB.35, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.36 — 156-3/017.1

**His words (short quotations and close paraphrase).** Il cherche la plus grande sous-catégorie pleine des ordres bidirigés non triviaux, divisibles, stable par les cônes stricts non vides et leurs duaux; elle existe, est autoduale, et ses objets sont les tronçons.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Among full classes of posets with global bounds, nontriviality, density and closure under nonempty strict cones, the largest class is exactly G.

**Status: True as written.** Every object in such a class has downward directed strict upper cones because those cones themselves are globally bidirected objects; the dual supplies the other local axiom. Thus the class is contained in G. Conversely G inherits itself on strict cones by lemma G, so it satisfies all requirements and is the largest class. Reversal is immediate.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** This is a two-containment proof; it avoids an unsupported size argument about unions of categories. Fullness merely takes all monotone maps between the objects.

**Proof and confidence.** PROOFS.tex, section H0KB.36, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.37 — 156-3/017.17;156-3/041.10

**His words (short quotations and close paraphrase).** « Il faudrait expliciter » les conditions sur R(a,b,c), et sur S₀ avec les R_ε; à la fin il renonce à expliciter tout l’exercice.

**His state and date.** programme; 1986-06-08; continued in the 1986-06-09 portion.

**Precise statement — ours.** Find intrinsic necessary and sufficient axioms for an unoriented tronçon’s betweenness or pair-cut data. The next two rows are the precise existence versions; no independence or minimality requirement is stated.

**Status: programme.** Lemma A supplies two explicit finite first-order recognition schemes. The programme row records what the text leaves unwritten; the two supported versions are fully decided below.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The concluding wording on 41 changes neither the data nor the demand for recognition; it questions the value of writing the full exercise, not the truth of the reconstruction theorem.

**Proof and confidence.** PROOFS.tex, section H0KB.37, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.38 — 156-3/017.17

**His words (short quotations and close paraphrase).** Version précise de la demande sur R(a,b,c) : donner les conditions qui définissent un biordre de tronçon.

**His state and date.** asked; 1986-06-08 (folder date).

**Precise statement — ours.** There exists an explicit finite first-order sentence in B whose models are exactly the strict betweenness structures of G-orders, in every cardinality.

**Status: True as written.** Use the full scheme A: define C,N,D,U,Q from B, existentially choose an anchor, impose every G axiom on the definable Q, and impose B exactly equal to strict Q-betweenness. Necessity is R1; sufficiency takes that Q as the constructed order. Every quantifier is over points, not over relations.

**Reconstruction / correction — ours.** This is our precise existence reading of his requested axiomatization and our solution, not an axiom list attributed to him.

**Second check.** The independent model-to-order and order-to-model substitutions in A check both directions and every axiom.

**Proof and confidence.** PROOFS.tex, section H0KB.38, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** Courcelle 2020, Theorem 3.6 and Proposition 5.1, concern the broader arbitrary-poset class; its non-finite-FO result does not contradict this restricted anchored G class.

#### H0KB.39 — 156-3/017.19;156-3/041.4

**His words (short quotations and close paraphrase).** Version précise de la demande sur S₀ et les R_ε dans C(ε).

**His state and date.** asked; 1986-06-08; continued in the 1986-06-09 portion.

**Precise statement — ours.** There exists an explicit finite first-order recognition scheme for a symmetric pair predicate S and a four-place pair-cut relation R(a,b;x,y), recognizing exactly canonical G pair cuts.

**Status: True as written.** A defines B by absence of a common point in the two relevant classes, applies the anchored G recognition clauses, and forces S and R to equal exactly comparability and the three gap equivalence relation of the constructed order. This proves necessity and sufficiency and yields all finite cuts by C.

**Reconstruction / correction — ours.** The recognition scheme is ours. It explicitly identifies the supplied predicates; it does not merely produce some unrelated order.

**Second check.** Direct substitution checks the domain restrictions, symmetry in the cut pair, equivalence on that domain, and the three-gap disjunction.

**Proof and confidence.** PROOFS.tex, section H0KB.39, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.40 — 156-3/018.1

**His words (short quotations and close paraphrase).** Il donne ∂I={a,b}, {a}, {b}, ∅ pour les sous-tronçons fermés; la marge précise « frontière relative », non bord absolu.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** Relative frontier omits an ambient extremum included in a non-singleton component, and retains an isolated singleton extremum. The first displayed formulas omit this exception.

**Status: Slip.** For L=[0,1] and I=L=[0,1], the first formula gives {0,1}, while the separate L case gives empty. The corrected rule removes ambient extrema in non-singleton components, exactly as written on scan 30; for a singleton it retains its point. The interval cases verify it directly.

**Reconstruction / correction — ours.** Our slip judgment uses the explicit relative-frontier margin and his later precise exception on 156-3/030. This is a combinatorial frontier, not yet a topological theorem.

**Second check.** Compare I=[0,1/2], I=L, and I={0}. These three cases independently force both the omission and the singleton exception.

**Proof and confidence.** PROOFS.tex, section H0KB.40, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.41 — 156-3/018.7

**His words (short quotations and close paraphrase).** Deux sous-tronçons fermés larges sont modérés si leurs frontières le sont; leur intersection est vide ou un tel sous-tronçon, et sa frontière est dans la réunion des frontières.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** In G, compatible closed intervals/rays/singletons have empty or closed-piece intersection, with relative frontier contained in the union of the input frontiers.

**Status: True as written.** Their finite endpoints form a chain; take the maximum lower bound and minimum upper bound. If these coincide the intersection is that singleton; if they cross it is empty; otherwise it is the indicated interval/ray. An internal new endpoint is an old one. At an ambient extremum a singleton intersection can occur only if one input already has that singleton frontier.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The direct endpoint intersection proof is independent of the finite-mask proof in F. No E is used because all finite endpoints are retained.

**Proof and confidence.** PROOFS.tex, section H0KB.41, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.42 — 156-3/018.17

**His words (short quotations and close paraphrase).** Après définition de la topologie par les intervalles, il affirme que, pour un pseudo-tronçon fermé, sa frontière combinatoire est la frontière topologique.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For all G, the displayed relative endpoints of a closed piece are its frontier in the canonical topology.

**Status: False.** In D, the singleton {a_0} has combinatorial frontier {a_0}, but its topological closure and frontier are {a_0,a_1}; its interior is empty. Thus the two frontiers differ. Under E, principal closed pieces are canonically closed and their only boundary points are their relative endpoints, by the neighborhood and closure proofs E and F.

**Reconstruction / correction — ours.** Add E for a theorem about all closed pieces. The author himself later separates the two notions on scans 25 and 30.

**Second check.** Compute the pulled-back rational topology explicitly. The extra twin is in every neighborhood of a_0, while no nonempty open set lies in the singleton.

**Proof and confidence.** PROOFS.tex, section H0KB.42, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.43 — 156-3/019.1

**His words (short quotations and close paraphrase).** Th : une réunion finie de pseudo-tronçons fermés disjoints et mutuellement modérés possède une famille I unique; ses T_i sont les composantes.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** A closed tame subset of G has a unique decomposition into nonempty pairwise compatible disjoint closed pieces.

**Status: True as written.** Compatible disjoint closed pieces are strictly separated: their facing endpoints are distinct and density supplies a missing point between them. The convex-separator proof in F then proves uniqueness by comparing two decompositions component by component. Empty union is uniquely empty.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The endpoint sweep gives the same components as maximal runs not separated by a strict missing gap. This second proof uses actual retained endpoints and needs no E.

**Proof and confidence.** PROOFS.tex, section H0KB.43, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.44 — 156-3/019.15

**His words (short quotations and close paraphrase).** Ẋ est la réunion des Ṫ_i; Ẋ=∅ ssi X=L ou X=∅.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** With the relative-endpoint convention, a closed tame union has frontier the finite disjoint union of component frontiers. It is empty exactly for the empty or full part.

**Status: True as written.** Uniqueness makes the union intrinsic. Different disjoint closed components have disjoint endpoint sets. Any nonempty proper component either has an internal endpoint or is an isolated singleton; that point contributes to the frontier. If none does, the sole component is L. This proves both directions.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Check rays, bounded intervals, singleton ambient endpoints and the full part separately. The correction of the earlier convention is already isolated in H0KB.40.

**Proof and confidence.** PROOFS.tex, section H0KB.44, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.45 — 156-3/019.20

**His words (short quotations and close paraphrase).** Deux parties fermées modérées sont en position relative modérée si leurs frontières le sont; X⊂Y implique cette position.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For closed tame subsets of G, compatibility is intrinsic and inclusion implies compatibility.

**Status: True as written.** Each X component lies in one Y component by the convex-separator argument. Since endpoints of closed pieces belong to the pieces, its finite endpoints lie between the containing component’s endpoints and compare with all other component endpoints through their strict order. Ambient extrema compare with every point.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Direct endpoint comparison gives the same conclusion as a common finite flag; this is the closed-piece case of F and uses no E.

**Proof and confidence.** PROOFS.tex, section H0KB.45, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.46 — 156-3/020.1

**His words (short quotations and close paraphrase).** Pour X,Y fermés modérés et mutuellement modérés, X∩Y est fermé modéré, X∨Y existe, et les frontières des deux sont contenues dans Ẋ∪Ẏ. Il étend ceci à une famille finie.

**His state and date.** sketched; 1986-06-08 (folder date).

**Precise statement — ours.** Compatible closed tame parts have global meet and join in the poset of closed tame parts; their frontiers use only the original endpoints. The operations preserve compatibility with any common compatible part.

**Status: True as written.** Intersect component pairs using the previous interval rule. For the join, sweep the common endpoint chain and merge all touching or overlapping closed pieces; any closed tame upper bound must contain each merged interval by convexity, hence this is least. New endpoints are selected from old endpoints, proving both frontier and compatibility assertions. Iterate for a finite family.

**Reconstruction / correction — ours.** At this point « parties modérées » denotes the closed-parts construction just defined; no later open-parts hull axiom is imported.

**Second check.** The independent finite-flag proof in F gives the same operations and establishes leastness among all closed tame upper bounds.

**Proof and confidence.** PROOFS.tex, section H0KB.46, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.47 — 156-3/020.12m

**His words (short quotations and close paraphrase).** « Attention » : une partie quelconque A n’a pas toujours de plus petit fermé modéré la contenant, déjà dans [0,1], avec une suite 1/n.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** There need not be a least finite union of closed intervals containing an arbitrary subset, even on [0,1].

**Status: True as written.** Lemma H proves this with A={0}∪{1/n:n≥1}. Every finite closed-interval cover contains [0,ε]; an irrational point inside it can be omitted by another finite closed tame cover of A. Thus no cover is least.

**Reconstruction / correction — ours.** The exact sequence with 0 included is our unambiguous realization of his example; omitting 0 still forces it in every closed cover.

**Second check.** The competing cover is explicitly [0,1/N] plus finitely many remaining sequence points; it verifies the direction of the leastness obstruction.

**Proof and confidence.** PROOFS.tex, section H0KB.47, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.48 — 156-3/020.18;156-3/021.1

**His words (short quotations and close paraphrase).** [a,b]∪_mod[b,c]=[a,c], mais la réunion ordinaire peut différer. L est totalement ordonné ssi L_≤b∪L_≥b=L pour tout b.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For a≤b≤c the closed tame join fills [a,c]; ordinary union equals it precisely when every point of [a,c] is comparable with b. The analogous all-rays property for every b characterizes total order.

**Status: True as written.** Any tame upper bound containing both touching intervals has one component containing them and, by convexity, [a,c]. The ordinary union is exactly the points of [a,c] comparable with b. A twin of b in D lies in [a,c] for outer heights a<b<c but in neither half. The global ray union is exactly the comparability set of b; requiring it to be L for every b is totality.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Evaluate membership on an arbitrary point rather than on endpoint masks. This separately checks the join/union distinction and both directions of the totality criterion.

**Proof and confidence.** PROOFS.tex, section H0KB.48, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.49 — 156-3/021.8

**His words (short quotations and close paraphrase).** Il barre la première affirmation : il existe un plus petit fermé modéré contenant X\Y, pour Y⊂X fermés modérés.

**His state and date.** cancelled; 1986-06-08 (folder date).

**Precise statement — ours.** The cancelled universal least-hull assertion for the ordinary difference of closed tame parts is false, even for some G satisfying E.

**Status: False.** Lemma H2 gives the regular split-line example X=L, Y=≤a on the first branch. Its ordinary difference contains the entire second branch. Every left-tail point p supplies a closed-ray cover ≥p; their intersection excludes the left tail, and no finite closed tame union inside it can cover the second branch all the way down to its unattained lower cut. Thus no least hull exists. All G and E axioms were verified in O.

**Reconstruction / correction — ours.** The statement is true on total G-orders, where ordinary and compatible difference agree; for general endpoint-regular G the correct replacement is C_mod(Y,X), as in the next row.

**Second check.** The compatible difference in the same example has the hull ≥a and omits the second branch. This independently checks that the author’s replacement really changes the set, and cannot prove the cancelled claim.

**Proof and confidence.** PROOFS.tex, section H0KB.49, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.50 — 156-3/021.10

**His words (short quotations and close paraphrase).** Il remplace X∖Y par C_mod(Y,X), les points de X hors Y en position modérée avec Y; il affirme l’existence de son plus petit fermé modéré Z⊂X.

**His state and date.** stated; 1986-06-08 (folder date).

**Precise statement — ours.** For closed tame Y⊂X in arbitrary G, C_mod(Y,X) is asserted to have a least closed tame hull Z, compatible with Y and containing every compatible closed part of X disjoint from Y.

**Status: False.** In D take X=L and Y=L_{≤a_0}. Its relative tame complement is the strict positive ray. By the dual of the complete D argument it has no least closed tame hull. Under E, the common-flag calculus makes C_mod(Y,X)=X∧Y′ tame and defines Z as its closure. Since X is closed, Z⊂X; closure preserves compatibility; every competing disjoint compatible part is already contained in C_mod(Y,X), hence in Z.

**Reconstruction / correction — ours.** E is the exact all-rays additional hypothesis. This is not the cancelled ordinary-difference claim, whose separate row is audited independently.

**Second check.** The independent topological characterization E gives Z as the canonical closure under E, and immediately proves leastness and Z⊂X.

**Proof and confidence.** PROOFS.tex, section H0KB.50, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.51 — 156-3/022.1

**His words (short quotations and close paraphrase).** F, frontière relative de Y dans X, est fini, modéré, contenu dans Z, sans point isolé de Z; C_mod(Y,X)=C_mod(F,Z).

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The preceding relative-difference construction has the finite-frontier description stated, wherever its required hull calculus is valid; the universal construction on all G is not valid.

**Status: False.** The same X,Y in D as H0KB.50 have no Z, so the claimed universal construction cannot be made. Under E work in a common endpoint chain: the relative complement consists of the gaps in X outside Y; its closure fills their adjacent excluded endpoints. These are exactly F, each adjacent to a nonempty gap and hence nonisolated by density. Removing F compatibly from Z recovers the original gaps.

**Reconstruction / correction — ours.** Complete corrected version: G+E, Y⊂X closed tame, Z=closure of X∧Y′, and F=relative frontier of Y in X.

**Second check.** Inspect the two facing endpoint flags for each gap. No isolated component can consist of a newly added frontier point, since every such point bounds a nonempty interval.

**Proof and confidence.** PROOFS.tex, section H0KB.51, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.52 — 156-3/022.8

**His words (short quotations and close paraphrase).** (9 juin) La base d’ouverts est ]a,b[, L_<a, L_>b; certaines demi-droites peuvent être omises quand l’extrémité correspondante n’existe pas.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** These strict intervals and rays form a topology basis in every G. Left rays are redundant if there is no minimum, and right rays if there is no maximum.

**Status: True as written.** Lemma P proves coverage and the intersection refinement by finite local filtering. If a point of a left ray has a predecessor, a bounded interval around it remains in that ray; absence of a minimum supplies such predecessors. The right case is dual.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The finite-cone lemma of G independently supplies the simultaneous lower and upper constraints needed for an intersection of several basic sets.

**Proof and confidence.** PROOFS.tex, section H0KB.52, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.53 — 156-3/022.12

**His words (short quotations and close paraphrase).** Une extrémité de L est fermée; en général un singleton n’est pas nécessairement fermé.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Any ambient least or greatest point is canonically closed. General points in G need not be closed.

**Status: True as written.** P constructs, around every other point, a strict-ray neighborhood missing the endpoint. In D a singleton’s closure is its two-point height fiber, so it is not closed.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The pulled-back rational topology in D directly verifies the negative clause, independently of the endpoint argument.

**Proof and confidence.** PROOFS.tex, section H0KB.53, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.54 — 156-3/022.16;156-3/023.1

**His words (short quotations and close paraphrase).** Pour les lieux d’une ficelle topologique, b∈cl{a} équivaut à b⊃a comme parties de H; l’égalité des adhérences équivaut à a=b, donc T₀.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For all genuine ficelles under the written 156-2 definitions, the canonical lieu specialization is claimed to be reverse inclusion of underlying closed subsets, and the lieu topology T₀.

**Status: False.** V gives a compact finite-tree ficelle: a main interval with a side hair attached at v=1/3. The loci D_s={3/4}∪[s,1]_hair are distinct regular closed lieux with exactly the same strict predecessors and successors. The full lieu order satisfies every G axiom, as V proves. Thus its topology is not T₀, and the claimed reverse-inclusion equivalence fails. V also proves the strongest retained implication, C⊂D⇒D∈cl{C}, the exact strict-cone specialization criterion, and the additional connected-component condition W_D that restores the converse. Connected target loci satisfy W_D.

**Reconstruction / correction — ours.** Our initial positive universal proof is withdrawn. A component-ficelle level cut need not be a global lieu. The corrected theorem assumes X_{A,D}/A and X_{B,D}/B connected, for the unpunctured component spaces, or the stronger sufficient condition that D is connected. These are additional hypotheses, not supplied ink. The real-segment case remains valid.

**Second check.** The complete tree classification gives the order formula V1 and computes the identical strict cones independently of neighborhood pictures. check_tree_ficelle.py separately computes relative connected components and end contractions on a finite grid; all 56,644 pair comparisons match V1. The continuous density/local-filtering proof is separate. The repaired theorem checks the missing global connectedness by a closed quotient with connected fibers.

**Proof and confidence.** PROOFS.tex, section H0KB.54, including its cited full common proof. High: original definitions and the unqualified promotion sentence were visually checked; the finite-tree model verifies every source hypothesis and all G axioms; an independent graph calculation confirms the order formula.

**Later status.** No opened later source settles the exact universal claim. The counterexample and connected-component repair are this run’s results. The general order-reconstruction comparison with Courcelle does not impose topological T₀.

#### H0KB.55 — 156-3/023.3

**His words (short quotations and close paraphrase).** Il ne sait pas si le caractère T₀ vaut « pour tout tronçon ».

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every G with its canonical topology is T₀.

**Status: False.** D satisfies every G axiom but its equal-height twins have identical neighborhoods. V strengthens this to actual lieux of a compact finite-tree ficelle. Under E the canonical topology is T₁. More exactly, P proves T₀ iff x↦(L_<x,L_>x) is injective; this is a necessary and sufficient order-language correction.

**Reconstruction / correction — ours.** E is a sufficient positive repair for all G. The exact strict-cone injectivity criterion is proved in P. A general ficelle is not a valid automatic T₀ repair.

**Second check.** The height projection realizes the entire canonical topology as the pullback of Q, so no possible canonical open distinguishes the twins.

**Proof and confidence.** PROOFS.tex, section H0KB.55, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.56 — 156-3/023.4

**His words (short quotations and close paraphrase).** Il demande si un tronçon est sobre : toute partie fermée irréductible aurait un point générique.

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every G is sober; even the stronger restricted question whether every T₀ G is sober has a negative answer.

**Status: False.** The nondegenerate-interval model J in P is G and T₀. Its irreducible closed family F={I:0∈I} has no generic point because the intersection of its members is the excluded degenerate interval {0}. All hypotheses and irreducibility are proved in P. A valid correction is the Hausdorff case: two distinct points of an irreducible closed set have disjoint neighborhoods meeting it, impossible; thus such a set is a singleton and has its unique generic point.

**Reconstruction / correction — ours.** EGA I 0_I 2.1.1–2.1.3 and SGA4 IV 4.2.1 supply the period meanings of irreducible, generic point, T₀ and sober.

**Second check.** The explicit shrinking family [−1/n,1/n] independently proves the obstruction. The Hausdorff repair is a direct argument, not a purported implication T₁⇒sober.

**Proof and confidence.** PROOFS.tex, section H0KB.56, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.57 — 156-3/023.8

**His words (short quotations and close paraphrase).** Si L est totalement ordonné, les points sont fermés, L est séparé, et [a,b], L_≥a, L_≤a sont fermés.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The canonical topology of a totally ordered G is Hausdorff; every principal closed interval and ray is topologically closed.

**Status: True as written.** For x<y insert c with x<c<y. The strict rays below and above c are disjoint neighborhoods. Complements of closed rays are opposite strict rays, and the complement of [a,b] is the union of the two exterior strict rays. This is P.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The same conclusion follows from E for closedness and direct order separation for Hausdorffness; total dense orders satisfy E as proved in P.

**Proof and confidence.** PROOFS.tex, section H0KB.57, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.58 — 156-3/023.8m

**His words (short quotations and close paraphrase).** À propos de « les pts sont fermés », il ajoute « réciproque ? ».

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** If every point in the canonical topology of G is closed, must the order be total?

**Status: False.** The reflexive strict-coordinate order on R² in P satisfies every G axiom and has the Euclidean canonical topology, yet (0,1) and (1,0) are incomparable. P proves the exact replacement: for every x≠y, it is not the case that both L_<x⊂L_<y and L_>x⊂L_>y. Equivalently a strict predecessor or successor separates the ordered pair. This condition is necessary and sufficient for T₁ and does not assert totality.

**Reconstruction / correction — ours.** Use the exact componentwise strict-cone antichain criterion in P. The weak coordinate order from the prior sweep fails G; the strict-coordinate model checks every local cone condition.

**Second check.** The two-coordinate proof separately verifies both local cone axioms, correcting the earlier sweep’s invalid weak-product example.

**Proof and confidence.** PROOFS.tex, section H0KB.58, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.59 — 156-3/023.12;156-3/024.1

**His words (short quotations and close paraphrase).** Il définit une autre topologie dont [a,b] et les demi-droites fermées sont une sous-base de fermés, puis note que ]a,b[ ne veut plus être ouvert.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The principal closed pieces generate a topology τ_c by arbitrary intersections of finite unions. It need not contain the canonical topology τ.

**Status: True as written.** Any family of subsets is a closed subbasis once finite unions and arbitrary intersections, including empty operations, are allowed. In P every basic τ_c-open contains (n,−n) for all sufficiently large n, so none can lie in a bounded open rectangle. Such a rectangle is τ-open, hence τ⊄τ_c.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Check the escape point against each kind of closed generator: bounded interval, lower ray, upper ray. This verifies the whole finite-union argument.

**Proof and confidence.** PROOFS.tex, section H0KB.59, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.60 — 156-3/024.3

**His words (short quotations and close paraphrase).** Pour la topologie borne sup, il liste des ouverts stricts, les complémentaires des demi-droites fermées, puis [a,b] sans complément; il dit « base ».

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The supremum topology is generated by the union of the two open subbases; the final generator must be L∖[a,b], and finite intersections give a basis.

**Status: Slip.** On R both original topologies are the usual order topology, but declaring [0,1] open strictly refines it. Thus the literal list is not their supremum. Taking complements of every closed-subbasis member, and finite intersections with canonical basic opens, is exactly the defining least topology containing both.

**Reconstruction / correction — ours.** Our correction uses the preceding phrase « topologie borne sup » and the two adjacent complemented ray generators.

**Second check.** The crop confirms the missing complement. The real-line test distinguishes the literal topology from the intended join independently of any non-total example.

**Proof and confidence.** PROOFS.tex, section H0KB.60, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.61 — 156-3/024.8

**His words (short quotations and close paraphrase).** « Aura-t-on » cl(]a,b[)=[a,b] dans la topologie borne sup ?

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For every G and a<b, the closure of the strict interval in τ∨τ_c equals the closed endpoint interval.

**Status: False.** In D choose a_0 at height 0, its twin a_1, and b_0 at height 1. The τ_c-closed interval [a_1,b_0] contains (a_0,b_0) and omits a_0, so a_0 is not in its closure in the join topology. Under E, τ_c⊂τ and the join is τ; E and local filtering prove the desired closure equality.

**Reconstruction / correction — ours.** E is our proved sufficient repair; the source’s intended join topology is used, after the separate generator slip is corrected.

**Second check.** The genuine segment-ficelle counterexample in V gives the same failure with actual closed interval lieux, independently of D.

**Proof and confidence.** PROOFS.tex, section H0KB.61, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.62 — 156-3/024.9

**His words (short quotations and close paraphrase).** Il demande cl(L_<a)=L_≤a si a n’est pas minimum, et la formule duale si a n’est pas maximum.

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The two nonempty strict-ray closure identities are asserted in τ∨τ_c for arbitrary G.

**Status: False.** In D the negative ray below a_0 lies in the τ_c-closed ray ≤a_1, which excludes a_0. Thus its closure misses a_0; the dual construction refutes the other identity. Nonextremality is satisfied. Under E both equalities hold by the local-neighborhood accumulation argument, and the join topology is τ.

**Reconstruction / correction — ours.** The endpoint qualifications are preserved exactly; they are insufficient without an additional condition such as E.

**Second check.** The two strict rays are nonempty at every rational height, so the counterexample does not exploit an omitted endpoint qualification.

**Proof and confidence.** PROOFS.tex, section H0KB.62, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.63 — 156-3/024.15

**His words (short quotations and close paraphrase).** Pour montrer a∈cl(]a,b[), il suffit que tout ouvert élémentaire contenant a contienne ]a,ε[ avec a<ε<b.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For the intended subbasis of τ∨τ_c, that property is sufficient for a to lie in the closure; the property itself need not hold.

**Status: True as written.** A neighborhood contains a finite intersection of elementary opens. Suppose each contains (a,ε_i) with a<ε_i<b. Local downward filtering above a gives a common lower bound d>a of the ε_i, and density gives a<e<d. Then the nonempty interval (a,e) lies in every elementary open and in (a,b). Hence every neighborhood meets (a,b).

**Reconstruction / correction — ours.** The sufficient implication is separated from the false universal premise in the next row.

**Second check.** This proof explicitly handles finite intersections, which a subbasis-only argument would otherwise leave unjustified.

**Proof and confidence.** PROOFS.tex, section H0KB.63, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.64 — 156-3/024.19

**His words (short quotations and close paraphrase).** « Mais c’est faux déjà » pour les lieux d’une ficelle; il propose un ouvert élémentaire complémentaire d’un [x,y] contenant tout ]a,b[ mais pas a.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** There exists a genuine ficelle lieu poset and an elementary join-topology neighborhood of a that misses the whole interval (a,b).

**Status: True as written.** In V, H=[0,1], a=[3/10,1/2], b={4/5}, x={2/5}. Then x<b and a∉[x,b], but every z with a<z<b lies in [x,b]. Its complement is the required neighborhood. V verifies that all these are lieux under the actual 156-2 definition and that all G conditions hold.

**Reconstruction / correction — ours.** This confirms his narrower example; it is not merely a non-ficelle counterexample to the general question.

**Second check.** Independently check the endpoint inequalities r(a)=1/2<l(z) and r(x)=2/5<l(z); equality cases for x,a are excluded because they overlap.

**Proof and confidence.** PROOFS.tex, section H0KB.64, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.65 — 156-3/025.1

**His words (short quotations and close paraphrase).** Il revient à la topologie initiale et appelle néanmoins [a,b], les demi-droites et L sous-tronçons « fermés », « par abus de langage »; les points sont admis comme larges.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** From here “closed” in the tame calculus means a finite closed-endpoint presentation, not necessarily closed in τ. Large/pseudo pieces additionally allow singletons.

**Status: True as written.** The distinction is coherent: the closed-parts calculus F uses order endpoints only, while D shows these need not be τ-closed. The retained definition makes no false topological promise.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Compare the explicit abuse-of-language sentence with the cancelled attempted topological-boundary definition below it and the warning on scan 30.

**Proof and confidence.** PROOFS.tex, section H0KB.65, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.66 — 156-3/026.1

**His words (short quotations and close paraphrase).** Il pose ∂T égal au « bord absolu », l’ensemble des plus petit et plus grand éléments de T; ∂{a}={a}, ∂[a,b]={a,b}.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For a nonempty closed pseudo-piece T, its absolute boundary is the set of its existing least and greatest elements; singleton and bounded-interval formulas follow.

**Status: True as written.** Least and greatest elements are unique when they exist. For [a,b], a is least and b greatest; if a=b the set is the singleton. This is precisely the stated definition, distinct from relative frontier.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Directly evaluate L of each of the three endpoint types; its absolute boundary is its ambient extrema, not always empty.

**Proof and confidence.** PROOFS.tex, section H0KB.66, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.67 — 156-3/026.9

**His words (short quotations and close paraphrase).** Il écrit ∂L_≥a=∂L_≤a={a}, avec la marge « sans exclure le cas a∈∂L ».

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The literal absolute-boundary ray formulas omit a possible opposite ambient extremum.

**Status: Slip.** For L=[0,1] and a=1/2, the absolute boundary of L_{≥a} is {a,1}, not {a}; that of L_{≤a} is {0,a}. The correct formulas adjoin the ambient maximum or minimum when it exists, with repetitions removed. They follow immediately from the extremum definition.

**Reconstruction / correction — ours.** Our slip correction follows the immediately preceding absolute-boundary definition; it is not a reversion to relative frontier.

**Second check.** The scan margin expressly retains endpoint cases; it does not eliminate this counterexample with a strictly internal a.

**Proof and confidence.** PROOFS.tex, section H0KB.67, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.68 — 156-3/026.11

**His words (short quotations and close paraphrase).** Il compare frontière relative et bord absolu, puis encadre ∂T=(Ṫ∩T) ⊔ (T∩∂L), après avoir barré une exception pour les singletons.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Ordinary union gives the correct relation between the two boundaries for a closed piece. The displayed disjoint-union assertion fails for a singleton at an ambient extremum.

**Status: Slip.** In L=[0,1], T={0} has absolute and relative boundary {0}. Both summands in the boxed formula are {0}, so they are not disjoint. Ordinary union remains correct in every case. Alternatively restore the cancelled singleton exception and use disjoint union only for non-singletons.

**Reconstruction / correction — ours.** The earlier exception is visibly cancelled and the union mark visibly underlined/disjoint; the literal formula is retained as a slip, not silently repaired.

**Second check.** For a non-singleton piece, relative frontier omits precisely its ambient extreme endpoints; for a singleton it retains its sole point. These two cases prove the corrected rule.

**Proof and confidence.** PROOFS.tex, section H0KB.68, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.69 — 156-3/026.20;156-3/026.20m

**His words (short quotations and close paraphrase).** Les tronçons sont T′=T\α, α⊂∂T; la marge dit « Cette écriture est unique » et que T est le plus petit fermé contenant T′.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every nonempty open/half-open interval has a unique closed-endpoint presentation and a least closed tame hull under G.

**Status: False.** In D, V=L_{<a_0}=L_{<a_1} has two presentations (≤a_i)\{a_i}; D proves that it has no least closed tame hull. Under E, cofinality and coinitiality of interval interiors force the actual endpoints, giving the unique presentation and least hull. E is also necessary for the universal ray-hull claim.

**Reconstruction / correction — ours.** E is the exact additional all-rays hypothesis, stronger and sharper than merely assuming totality. Empty pieces must be excluded from uniqueness.

**Second check.** The independent canonical-topology characterization in E yields the same hulls under E and proves their leastness among closed tame supersets.

**Proof and confidence.** PROOFS.tex, section H0KB.69, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.70 — 156-3/026.23

**His words (short quotations and close paraphrase).** Dans la liste des tronçons ouverts, l’encre exclut a=ω pour L_<a et a=α pour L_>a.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Nonempty strict lower rays require a different from the least element α, and nonempty strict upper rays require a different from the greatest element ω. The two written exclusions are reversed.

**Status: Slip.** In L=[0,1], the written a≠ω condition allows a=0 in L_<a, giving the empty set, and wrongly excludes a=1 although L_<1 is nonempty. The upper-ray case is dual. By G a point with no strict predecessor is the least element; conversely a least element has no predecessor. This proves the exact corrected exclusions, and the dual proves the upper-ray condition.

**Reconstruction / correction — ours.** Our correction reverses the two endpoint symbols. Witness H prints the mathematically corrected exclusions; the crop shows the opposite order, recorded explicitly in READINGS.tsv.

**Second check.** Directly check the four rays at 0 and 1. Then use the global-lower-bound proof that a minimal point must be least, which checks the general claim independently.

**Proof and confidence.** PROOFS.tex, section H0KB.70, including its cited full common proof. High for the mathematical correction; high for the two enlarged endpoint glyphs, compared with α and ω elsewhere on the pages.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.71 — 156-3/027.1

**His words (short quotations and close paraphrase).** Les intervalles stricts et demi-droites strictes sont dits ouverts; il écrit ]a,b] et [b,a[ pour les demi-ouverts, puis note le cas d’une extrémité ambiante.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The second half-open interval should be [a,b), for a<b. Strict intervals/rays are τ-open; an interval beginning at the ambient minimum is also τ-open when its other endpoint is omitted.

**Status: Slip.** With 0<1 in Q, [1,0) is empty and is not the intended nonempty half-open piece. Replace it by [0,1). The basis definition proves strict openness. If a=min L, [a,b)=L_{<b}; dually at a maximum. Hence his following qualification is correct.

**Reconstruction / correction — ours.** The bracket/endpoint reversal is ours to correct; the scan and supplied text record [b,a[. The apparent “exactly the open ones” is read with his immediate exception, not as an unqualified biconditional.

**Second check.** The example at the ambient minimum distinguishes the classification by endpoint notation from topological openness.

**Proof and confidence.** PROOFS.tex, section H0KB.71, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.72 — 156-3/027.12

**His words (short quotations and close paraphrase).** Un pseudo-tronçon est un point ou un tronçon; pour T′=T\α il pose ∂T′=∂T, en précisant qu’il ne s’agit pas du bord absolu induit.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The construction is asserted to define an intrinsic endpoint set for each actual subset T′, equal to the endpoints of its associated closed hull.

**Status: False.** The two presentations of V in D give respectively endpoint sets {a_0} and {a_1}, so the function on subsets is not well defined. Under E, the unique infimum/supremum endpoints proved in E make it intrinsic; F then supplies the pseudo-piece calculus.

**Reconstruction / correction — ours.** Keep the distinction between pseudo-boundary and absolute induced boundary; E corrects the intrinsicness failure without conflating them.

**Second check.** The ambiguity survives before any algebraic operation is attempted: compare the two endpoint sets directly.

**Proof and confidence.** PROOFS.tex, section H0KB.72, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.73 — 156-3/027.17

**His words (short quotations and close paraphrase).** Il commence « on aura encore » une relation entre ∂T′, sa frontière relative et ∂L, puis laisse des points de suspension; la marge distingue le bord absolu.

**His state and date.** programme; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Complete the intended absolute-endpoint/relative-frontier formula for pseudo-pieces. Supported precise version under E: relative frontier removes included ambient ends in non-singleton pieces and retains isolated singleton ends.

**Status: programme.** The incomplete display does not supply a determinate universal identity to refute. The precise endpoint/frontier rule is proved in F and is written explicitly on scan 30. The intrinsic-endpoint claim under G is separately refuted in H0KB.72.

**Reconstruction / correction — ours.** The supported precise rule is included as the correction in H0KB.84 and proved there.

**Second check.** The crop preserves the ellipsis and the distinction between dotted frontier and absolute-boundary notation. No set equality is invented from the unfinished line.

**Proof and confidence.** PROOFS.tex, section H0KB.73, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.74 — 156-3/027.18m

**His words (short quotations and close paraphrase).** Il note que les points frontière sont les bornes inférieure et supérieure dans L quand elles existent, et qu’une borne supérieure existe ssi le pseudo-tronçon est majoré.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every bounded pseudo-piece in G has an actual supremum/infimum equal to its displayed finite endpoint; its endpoint set is empty only for a full endpoint-free L.

**Status: False.** In D the negative strict ray is bounded by both twins at height 0 but has no supremum: any supremum would have to be below both twins and bound all negative heights, which is impossible. The dual refutes the infimum clause. Under E, the cofinality argument gives the exact displayed endpoints and the asserted classification of empty boundary.

**Reconstruction / correction — ours.** The implication “has a supremum ⇒ bounded” is always true. E supplies the missing converse for these pieces.

**Second check.** Use the cofinal sequence of negative heights and inspect all possible heights of a candidate supremum. This independently excludes both a negative candidate and either zero-height twin.

**Proof and confidence.** PROOFS.tex, section H0KB.74, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.75 — 156-3/027.19

**His words (short quotations and close paraphrase).** Deux pseudo-tronçons sont modérés si ∂T∪∂T′ est totalement ordonné.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** This rule is asserted to define compatibility of actual pseudo-piece subsets, independently of presentations.

**Status: False.** Take V=L_{<a_0}=L_{<a_1} in D and Y={a_0}. The presentation with endpoint a_0 makes V compatible with Y; the presentation with endpoint a_1 does not. Under E endpoints are unique and the rule is well defined, with the complete F calculus.

**Reconstruction / correction — ours.** Correct either by retaining presentations as data, which changes the object, or by imposing E to preserve his intended actual-subset object. We prove the latter.

**Second check.** The two presentations are identical as subsets and differ only in the omitted endpoint; both satisfy the manuscript’s construction.

**Proof and confidence.** PROOFS.tex, section H0KB.75, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.76 — 156-3/028.1

**His words (short quotations and close paraphrase).** Deux pseudo-tronçons en position relative modérée ont une intersection vide ou pseudo-tronçon, avec ∂(T∩T′)⊂∂T∪∂T′.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For compatible endpoint presentations, the intersection has the max/min endpoint formula. As an intrinsic assertion about actual subsets on all G, it inherits the endpoint ambiguity.

**Status: False.** D supplies actual subsets for which even the compatibility premise and claimed endpoint conclusion depend on the chosen presentation, as H0KB.75 shows. Under E, intersect the two intervals by choosing their larger lower endpoint and smaller upper endpoint; tied endpoints are retained iff both input flags retain them. Empty and singleton cases follow, and every surviving endpoint is old.

**Reconstruction / correction — ours.** The algebraic intersection formula is valid for fixed compatible presentations; E makes the manuscript’s claimed subset-level statement well defined.

**Second check.** The endpoint-pair computation independently agrees with the normalized-mask intersection identity in F.

**Proof and confidence.** PROOFS.tex, section H0KB.76, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.77 — 156-3/028.4

**His words (short quotations and close paraphrase).** T<T′ signifie t<t′ pour tout t∈T,t′∈T′; c’est transitif. Il ajoute que cela implique la position relative modérée et la disjonction.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For nonempty actual pieces the relation is transitive and implies disjointness. Its assertion of intrinsic endpoint compatibility under G is not valid without the preceding well-definedness repair.

**Status: False.** Transitivity follows by choosing an element of the intermediate nonempty piece; disjointness follows from irreflexivity. For endpoint compatibility in D, let T be the ray below height 0 presented with endpoint a_0 and T′={a_1}. Then every point of T is <a_1, but the endpoint pair a_0,a_1 is incomparable. Under E actual sup/inf bounds compare and all endpoints are compatible, proving the full corrected assertion.

**Reconstruction / correction — ours.** Retain nonemptiness and add E for the full endpoint assertion; the transitive/disjoint part needs no E.

**Second check.** The explicit example checks strict order on every point by height, while its two displayed boundary points have the same height and are distinct.

**Proof and confidence.** PROOFS.tex, section H0KB.77, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.78 — 156-3/028.10

**His words (short quotations and close paraphrase).** Après T<T′, il écrit que T, étant majoré, « a un plus grand élément a »; la phrase duale parle ensuite de ∂T′.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The literal maximum-of-T assertion fails for open pieces. The nearby reasoning needs the greatest endpoint of its closed hull, namely sup T.

**Status: Slip.** On R take T=(0,1), T′=(2,3). They are strictly ordered, T is bounded, and has no greatest element. Its supremum is 1, the greatest endpoint of the closed hull. Under E every bounded pseudo-piece has that supremum by E. Without E, even the supremum claim fails as separately recorded in H0KB.74.

**Reconstruction / correction — ours.** Our correction replaces “greatest element of T” by “greatest endpoint / sup T”, without pretending this fixes the independent missing-E problem.

**Second check.** The crop confirms that the first surviving noun is T, while the next clause explicitly uses ∂T′; this supports the local pen-slip judgment.

**Proof and confidence.** PROOFS.tex, section H0KB.78, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.79 — 156-3/028.17

**His words (short quotations and close paraphrase).** T≪T′ renforce T<T′ en excluant le raccordement; il l’exprime par l’existence d’un x avec T⊂L_<x et T′⊂L_>x.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Use the intrinsic definition T≪T′ iff there is a strict separator x. It is transitive and forces disjoint, strictly ordered nonempty pieces. Where actual endpoint bounds exist, it is precisely non-raccordement.

**Status: True as written.** If T≪T′≪T″, any separator of T,T′ lies below every point of T′ and hence below every point of T″, so also separates T,T″. The exact endpoint equivalence is proved in H under the explicit actual-bounds assumption on the next page.

**Reconstruction / correction — ours.** A variable written a in the first cone of the last display is read as the locally quantified x in the corrected formula; the typo is recorded in READINGS.tsv.

**Second check.** The separator definition uses only actual subsets, so it is immune to the endpoint ambiguity. We do not identify it with a presentation-dependent relation without the bounds hypothesis.

**Proof and confidence.** PROOFS.tex, section H0KB.79, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.80 — 156-3/029.2

**His words (short quotations and close paraphrase).** « Conditions équivalentes (si a=Sup T, b=Inf T′) » : a) T<T′ sans raccordement; b) il existe un strict séparateur.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Assume the actual supremum a of T and actual infimum b of T′ exist. Then strict separation is equivalent to a<b, or a=b excluded from both pieces. This holds in G without E.

**Status: True as written.** H proves a≤b and computes all strict separators as [a,b] with a removed if a∈T and b removed if b∈T′. Density makes this set nonempty exactly in the stated cases. This proves the two-way implication with the manuscript’s inserted si retained.

**Reconstruction / correction — ours.** We explicitly preserve the supplied conditional; an unconditional bound-existence assertion is a different, false row.

**Second check.** Check all four endpoint-retention combinations independently. The actual-bound hypothesis is visually confirmed and never omitted in a counterexample.

**Proof and confidence.** PROOFS.tex, section H0KB.80, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.81 — 156-3/029.7

**His words (short quotations and close paraphrase).** Il ajoute un pseudo-tronçon S entre T,T′ se raccordant à chacun, unique, avec ∂S={a,b}; S est l’ensemble de tous les stricts séparateurs.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under the preceding actual-bounds assumption, the strict-separator subset exists with the stated interval formula. The further intrinsic endpoint/raccordement claims need not follow in arbitrary G.

**Status: False.** In D take T={a_0}, T′={b_0}, heights 0 and 1. Their actual sup/inf are a_0,b_0, so the inserted hypothesis holds. The separator set is the strict height interval, whose lower and upper bounds include both endpoint twins and have no infimum/supremum. Its intrinsic ∂ is not {a_0,b_0}. Under E, H proves the unique separator piece and both raccordements by its forced endpoint flags.

**Reconstruction / correction — ours.** The set formula for S is retained. E makes its endpoint interpretation and uniqueness valid.

**Second check.** This counterexample keeps the actual sup/inf of T,T′, so it refutes only the added conclusion about S, not the valid a)⇔b) theorem.

**Proof and confidence.** PROOFS.tex, section H0KB.81, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.82 — 156-3/029.15

**His words (short quotations and close paraphrase).** Si T est « minoré strictement », ses minorants stricts forment le pseudo-tronçon interstitiel gauche, sans minorant, caractérisé par raccordement; dualement à droite.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under the intrinsic endpoint calculus, the exterior gap exists exactly when a strict bound exists. Its “without a lower bound” description must mean without a strict lower bound.

**Status: Slip.** On L=[0,1], take T=[1/2,1]. Its strict lower bounds form [0,1/2), which has the lower bound 0 but no strict lower bound. Thus the literal “sans minorant” is false. With strict understood, H gives the exterior-ray formula and characterization under E; the independent G endpoint failure remains in H0KB.74.

**Reconstruction / correction — ours.** Restore the strict qualifier consistently. Endpoint intrinsicness still uses the separately stated E repair.

**Second check.** The manuscript explicitly inserts “strictement” and “minorants stricts” in the preceding lines, providing the local convention needed for this repair.

**Proof and confidence.** PROOFS.tex, section H0KB.82, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.83 — 156-3/030.1

**His words (short quotations and close paraphrase).** Les drapeaux finis Φ de pseudo-tronçons pour ≪ donnent X_Φ=⋃T_i; l’application Φ↦X_Φ est injective. Les T_i sont ses composantes, pas pour la topologie canonique.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Using strict-separator ≪ and actual nonempty convex pseudo-pieces, finite component decompositions are unique, even without E.

**Status: True as written.** If a convex piece from one decomposition met two pieces in another, a separator between them would lie between two of its points and hence belong to it, but would be absent from the union. Thus each piece lies in a single piece of the other decomposition; reverse the roles to conclude equality. This is F.

**Reconstruction / correction — ours.** We retain the intrinsic separator definition of ≪. “Components” is explicitly a tame, not topological, term.

**Second check.** The two-containment argument is independent of endpoint uniqueness; hence the earlier endpoint counterexample does not refute this proposition.

**Proof and confidence.** PROOFS.tex, section H0KB.83, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.84 — 156-3/030.16

**His words (short quotations and close paraphrase).** Fr(X)= (⋃∂T_i)\ε; ε retire les extrémités ambiantes appartenant à une composante non ponctuelle, mais non les points isolés.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The formula defines an intrinsic finite relative frontier of an actual tame subset only if its component endpoint sets are intrinsic. It is correct under G+E with the stated singleton exception.

**Status: False.** The one-component set V in D has two different endpoint presentations, giving different frontier sets; there are no ambient extrema to remove. Under E, F proves unique endpoints, and removing exactly the included ambient ends of non-singleton components yields the displayed relative frontier.

**Reconstruction / correction — ours.** No topological frontier is substituted. The page itself warns that this frontier is not for the canonical topology.

**Second check.** The interval cases L, a proper ray, an internal singleton and an ambient-end singleton independently verify every clause of the corrected formula.

**Proof and confidence.** PROOFS.tex, section H0KB.84, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.85 — 156-3/031.1

**His words (short quotations and close paraphrase).** Un point est modéré avec X s’il l’est avec chaque T_i, donc avec ⋃∂T_i, ou avec Fr(X); tout point de X et tout point frontière a cette propriété.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** With intrinsic endpoints, point compatibility is equivalent to comparability with all component endpoints; removing ambient extrema does not change it. Points of X and its frontier satisfy it.

**Status: False.** The presentation-dependent V in D makes even this relation on actual subsets ambiguous. Under E, a point in one component lies between its endpoints and is strictly ordered from all other components; a frontier point belongs to the common endpoint chain. Ambient extrema are universally comparable, so they may be removed. These observations prove every stated implication.

**Reconstruction / correction — ours.** E repairs the well-definedness; the elementary endpoint comparison is otherwise correct.

**Second check.** Check an interior point, an omitted endpoint, and an ambient extremum separately. The same comparisons give the all-points polar formula O1 for outside points.

**Proof and confidence.** PROOFS.tex, section H0KB.85, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.86 — 156-3/031.8

**His words (short quotations and close paraphrase).** X′=C_mod(X) est modéré et est la plus grande partie modérée disjointe de X en position modérée avec X.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The indicated construction is asserted to define a subset-level complement for every G, with the stated maximality.

**Status: False.** On D the complement of {a_0} equals that of {a_1}; applying the claimed endpoint rule to that common set is ambiguous. Thus the full intrinsic complement construction cannot have the asserted properties. Under E, F proves that the gap part is tame and contains every compatible disjoint tame part. O1 independently identifies it as the polar of all points of X for distinct comparability.

**Reconstruction / correction — ours.** Use G+E for the actual-subset calculus. The qualified complement is still generally smaller than L∖X.

**Second check.** The endpoint-gap proof and the all-points polar proof are independent descriptions of exactly the same subset under E.

**Proof and confidence.** PROOFS.tex, section H0KB.86, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.87 — 156-3/031.14

**His words (short quotations and close paraphrase).** Pour X=T₁∪⋯∪T_n, X′ est formé des n−1 tronçons interstitiels et des deux interstitiels extérieurs quand ils existent.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The complement has precisely the consecutive internal gap pieces and the existing exterior pieces, provided the intrinsic endpoint calculus is valid.

**Status: False.** The general G construction fails already for the shared complement of the twin singletons in D; its advertised endpoint data are ambiguous. Under E, the finite flag F lists exactly the unselected runs between selected component runs; H identifies each such run with its separator formula. No further component is possible.

**Reconstruction / correction — ours.** G+E is the proved corrected version; n=0 is handled separately by ∅′=L.

**Second check.** The direct separator inequalities of H reproduce the same list without using the Boolean complement mask.

**Proof and confidence.** PROOFS.tex, section H0KB.87, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.88 — 156-3/032.1

**His words (short quotations and close paraphrase).** Il donne n′∈{n−1,n,n+1}, puis le tableau selon T₁ minoré et T_n majoré.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** In the corrected calculus, n′=n−1+e_-+e_+ for n>0, where e_± record strict exterior bounds. The unqualified bounds in the printed table are insufficient at ambient extrema.

**Status: Slip.** For X=L=[0,1], n=1 and n′=0, but the literal last line sees both a lower and upper bound and gives n′=2. Replace minoré/majoré by strictly minoré/majoré. H proves the corrected count by enumerating n−1 internal gaps and two optional exterior gaps. For X=∅, n=0,n′=1.

**Reconstruction / correction — ours.** Restore the strict qualifier inherited from scan 29. The broader missing-E construction issue is recorded in the preceding complement rows.

**Second check.** The cropped first line reads non minoré (not non majoré); the numerical tests at ∅, L and a proper internal interval check all count possibilities.

**Proof and confidence.** PROOFS.tex, section H0KB.88, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.89 — 156-3/032.14m

**His words (short quotations and close paraphrase).** « Cette relation est-elle déductible de la relation d’ordre » sur M=Mod(L) ?

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** On the originally claimed all-G subset calculus the relation need not be well defined. On the exactly repaired G+E calculus, inclusion alone determines compatibility.

**Status: False.** D refutes the claimed premise of an intrinsic relation on all G. The strongest repaired answer is positive, with a complete proof O: atoms are singleton parts; two distinct atoms admit a join iff their points are comparable; formula O1 recovers tame complement as the polar of that graph; the three-piece Boolean decomposition then characterizes compatibility purely by inclusion, bounds and the recovered complement.

**Reconstruction / correction — ours.** The positive reconstruction under E is ours. A rejected singleton-adjunction attempt is documented in WORK_LOG and is not used in the accepted proof.

**Second check.** The atomic-join obstruction is checked by strictly truncating every proposed upper bound of an incomparable pair. The polar formula is independently verified against the endpoint-gap complement in F.

**Proof and confidence.** PROOFS.tex, section H0KB.89, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.90 — 156-3/032.14m

**His words (short quotations and close paraphrase).** Il propose « p.ex. {X,Y} mod ssi X∧Y existe ??? ».

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Existence of a greatest lower bound in the inclusion poset characterizes compatibility.

**Status: False.** Use the regular split line of O, which satisfies both G and E. Singleton parts on the two incomparable branches are incompatible, but their intersection ∅ is their global greatest lower bound. O verifies all order and endpoint axioms. The correct order-only criterion is the atomic-polar/Boolean-decomposition criterion in H0KB.89.

**Reconstruction / correction — ours.** The broader recovery question is not refuted by this failed proposed shortcut.

**Second check.** No arbitrary intersection theorem is needed: the only subset of two distinct singletons is ∅, so it is unconditionally their meet.

**Proof and confidence.** PROOFS.tex, section H0KB.90, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.91 — 156-3/033.1

**His words (short quotations and close paraphrase).** Propriété 1 : M possède le plus petit élément ∅ et le plus grand L, noté aussi 1.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The inclusion poset of actual tame subsets has bottom ∅ and top L.

**Status: True as written.** The empty component family gives ∅, and the single full piece gives L. Every actual subset lies between them. This assertion is unaffected by endpoint ambiguity.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The statement is checked directly in both D and the endpoint-regular examples.

**Proof and confidence.** PROOFS.tex, section H0KB.91, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.92 — 156-3/033.3

**His words (short quotations and close paraphrase).** Propriété 2 : X⊂Y implique {X,Y} modéré.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Inclusion implies the intrinsic tame compatibility relation on all of M.

**Status: False.** In D the ray V below the two twins is contained in the closed ray ≤a_1, but its presentation with endpoint a_0 is incompatible with that closed ray. The same subset has a compatible alternative presentation, demonstrating the intrinsicness failure. Under E the containment proof in F compares actual component infima/suprema and proves the property.

**Reconstruction / correction — ours.** G+E is the corrected all-parts version; G alone suffices for closed parts.

**Second check.** The closed-only version was proved separately; the counterexample uses precisely an omitted endpoint, so the two results do not conflict.

**Proof and confidence.** PROOFS.tex, section H0KB.92, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.93 — 156-3/033.4

**His words (short quotations and close paraphrase).** Propriété 3 : les éléments compatibles ont infimum et supremum; il ajoute la distributivité pour une famille mutuellement modérée.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The displayed meet/join and finite distributive laws are asserted for the intrinsic compatible-subset calculus on every G.

**Status: False.** The compatibility premise is not well defined on actual subsets in D, so the stated universal structure is not constructed. Under E, F embeds every finite compatible family in a common normalized-cell Boolean algebra; its meet is actual intersection, its join is normalized union and is globally least. Boolean distributivity follows there.

**Reconstruction / correction — ours.** The repaired assertion is finite distributivity. No arbitrary infinite join or completeness claim is inserted; such joins need not exist even on R.

**Second check.** The independent endpoint sweep verifies leastness beyond a chosen block, preventing an unwarranted inference from local to global joins.

**Proof and confidence.** PROOFS.tex, section H0KB.93, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.94 — 156-3/033.7

**His words (short quotations and close paraphrase).** Propriété 4 : un plus grand compatible disjoint X′ existe; il est l’unique complément compatible, et X↦X′ est une anti-involution.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The all-G actual-subset construction is asserted to have the stated complement, involution and order-reversal properties.

**Status: False.** In D, distinct singleton twins have the same prescribed complement. No involution can take two different inputs to the same output. Under E, F proves maximality and uniqueness inside every common endpoint flag and global maximality by containment; bitwise complement is involutive, and refinement proves the order reversal globally. O independently identifies the complement as a graph polar.

**Reconstruction / correction — ours.** G+E supplies the full corrected complement calculus, not merely an arbitrary choice of one presentation.

**Second check.** The twin equality directly refutes injectivity of an involution. Under E, antitonicity also follows from formula O1 by restriction of the universal comparison condition.

**Proof and confidence.** PROOFS.tex, section H0KB.94, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.95 — 156-3/033.8m

**His words (short quotations and close paraphrase).** Le renforcement marginal exige que les éléments mutuellement modérés engendrent, par ∧,∨,′, une algèbre de Boole, finie si la famille est finie.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The intrinsic concrete all-G structure is asserted to have compatible Boolean blocks. As an independent abstract postulate this is coherent and is explicitly assumed later.

**Status: False.** D refutes the intrinsic complement needed for this universal concrete claim. Under E, F constructs common finite endpoint-cell blocks and their refinement embeddings, proving all Boolean identities and finiteness for finite generators. The abstract model M in lemma M separately shows the strengthened postulate is consistent.

**Reconstruction / correction — ours.** The concrete failed assertion is distinguished from the valid abstract hypothesis on scan 34.

**Second check.** For finite flags, distinct masks are distinguished by a point in a nonempty cell. This checks injectivity of the Boolean realization, not merely its symbolic identities.

**Proof and confidence.** PROOFS.tex, section H0KB.95, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.96 — 156-3/033.13

**His words (short quotations and close paraphrase).** La compatibilité est inchangée si l’on remplace l’un ou les deux termes par leur complément; il donne les deux lois de De Morgan.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** In the intended actual-subset structure, complement preserves compatibility in either argument and obeys the two De Morgan laws for compatible pairs.

**Status: False.** On all G the operation is not intrinsic, by D. Under E, complementation keeps the same endpoint chain and Boolean NOT interchanges AND and OR in F, proving the laws. The same claims hold as part of the abstract assumptions in M.

**Reconstruction / correction — ours.** The printed union-like glyph in one De Morgan formula means the tame join in the immediately stated algebraic context, not ordinary set union.

**Second check.** The exhaustive Boolean truth-table check through eight cells independently verifies both identities; the endpoint proof establishes that those cells actually model the corrected calculus.

**Proof and confidence.** PROOFS.tex, section H0KB.96, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.97 — 156-3/033.19

**His words (short quotations and close paraphrase).** Propriété 5 : ∅ et 1 appartiennent à M_f, les parties fermées modérées.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The empty and full parts are closed in the manuscript’s combinatorial sense.

**Status: True as written.** They are respectively the empty union and the closed full piece. This proves the property without invoking any topology or E.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** Both are also topologically closed in every topology, but that independent fact is not needed for the stated combinatorial convention.

**Proof and confidence.** PROOFS.tex, section H0KB.97, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.98 — 156-3/033.20

**His words (short quotations and close paraphrase).** Propriété 6 : chaque X∈M a un plus petit Y∈M_f avec X⊂Y; on pose Y=X̄.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every tame actual subset in G has a least closed tame hull.

**Status: False.** D supplies the strict negative ray V, a single pseudo-piece, with no such hull. Lemma E proves the exact repair: within G, the existence of least closed tame hulls for all nonempty strict principal rays is equivalent to E. Under E, F proves all finite tame parts have least hulls. Thus E is necessary and sufficient for this universal hull assertion.

**Reconstruction / correction — ours.** This is the central missing hypothesis of the later calculus; it is not a harmless endpoint convention.

**Second check.** The independent canonical-topology characterization in E computes the same hull as the closure of a finite union of interval pieces.

**Proof and confidence.** PROOFS.tex, section H0KB.98, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.99 — 156-3/033.20m

**His words (short quotations and close paraphrase).** Par passage au complémentaire, il définit X°=(overline(X′))′.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** If the stipulated complement and closure axioms 1–7 hold, this formula defines the greatest open element below X, where open means complement of a closed element.

**Status: True as written.** Order reversal gives (c(X′))′≤X. It is open by definition. If U≤X is open, then U′ is closed and X′≤U′, so c(X′)≤U′ and U≤(c(X′))′. This proves the greatest-open property using only the abstract axioms.

**Reconstruction / correction — ours.** This is a valid conditional algebraic definition. The claim that every original G supplies its hypotheses is separately refuted in H0KB.94 and H0KB.98.

**Second check.** Apply the same order-reversal argument twice to verify idempotence and monotonicity of interior.

**Proof and confidence.** PROOFS.tex, section H0KB.99, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.100 — 156-3/033.22

**His words (short quotations and close paraphrase).** Pour X,Y compatibles, l’adhérence vérifie overline(X∨Y)=X̄∨Ȳ.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The all-G closure construction preserves finite compatible joins.

**Status: False.** Closure is not defined for every tame X in D, so the asserted universal operation fails. Under E, F proves closure fills omitted endpoint cells and merges touching runs. Applying it before or after normalized union selects exactly the same occupied cells and forced endpoints. Therefore the displayed equality holds.

**Reconstruction / correction — ours.** The exact domain correction is G+E; an infinite-join version is neither stated nor inferred.

**Second check.** Independently, canonical topological closure under E commutes with finite unions of component intervals; normalizing a compatible join imposes the same outer closed endpoints.

**Proof and confidence.** PROOFS.tex, section H0KB.100, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.101 — 156-3/033.24

**His words (short quotations and close paraphrase).** Propriété 7 : si X,Y sont modérés, X̄,Y le sont, donc aussi X,Ȳ et X̄,Ȳ.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The universal tame closure preserves compatibility.

**Status: False.** The D ray has no closure in the stated sense, refuting the universal construction. Under E closure introduces no endpoint outside the old finite endpoint chain. Hence all the displayed pairs remain compatible, by F.

**Reconstruction / correction — ours.** G+E proves the concrete property; M treats the abstract conditional separately.

**Second check.** The relative abstract proof M uses this as an explicit hypothesis; it is not deduced from the incomplete G construction.

**Proof and confidence.** PROOFS.tex, section H0KB.101, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.102 — 156-3/034.1

**His words (short quotations and close paraphrase).** Il forme Fr X=X̄∧overline(X′), puis (Fr X)′=X°∨(X′)°.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under the stipulated abstract axioms 1–7, the frontier meet is defined and its complement has the displayed De Morgan expression.

**Status: True as written.** X is compatible with X′. Applying closure compatibility twice makes c(X),c(X′) compatible, so their meet exists. De Morgan gives its complement as c(X)′∨c(X′)′, which is exactly (X′)°∨X°.

**Reconstruction / correction — ours.** The conditional identity is true; finite geometric frontier requires the corrected concrete realization.

**Second check.** The Boolean identity was independently checked on all finite masks through eight cells. This is an algebraic identity, not a claim that an arbitrary topological frontier is tame.

**Proof and confidence.** PROOFS.tex, section H0KB.102, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.103 — 156-3/034.4

**His words (short quotations and close paraphrase).** La propriété spéciale de dimension un relie la compatibilité de X,Y à celle de Fr X,Fr Y; la fin répète Fr X∪Fr X.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For the intrinsic interval calculus, X,Y are compatible iff their finite relative frontiers form a chain together. The last repeated X should be Y. The universal all-G realization is not well defined.

**Status: False.** D gives ambiguous frontiers, so the subset-level assertion is not meaningful on all G. Under E, F says compatibility is exactly comparability of component endpoints; relative frontier deletes only ambient extrema, which are comparable to everything. This proves the equivalence. The ordinary union of the two finite frontier sets is then tame.

**Reconstruction / correction — ours.** The substantial repair is E. The repeated Fr X in the final union is a subsidiary pen slip, documented in READINGS.tsv.

**Second check.** Independently add back all ambient extrema: doing so changes neither the chain property nor compatibility. This checks the effect of the relative-boundary exception.

**Proof and confidence.** PROOFS.tex, section H0KB.103, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.104 — 156-3/034.11

**His words (short quotations and close paraphrase).** Dans le cas envisagé, X⊂X•, X=X•, et X fini sont équivalents; X• désigne la frontière, et X°=∅ signifie rare.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For all tame X in the claimed concrete structure, empty tame interior, equality with its frontier and finiteness are equivalent.

**Status: False.** On arbitrary G the required universal complement/closure structure fails by D. Under E, F proves the exact equivalence: every nondegenerate component contains a strict open interval by density, so empty tame interior forces all components to be singletons. Conversely a finite tame set is closed, has empty interior, and equals its finite frontier, including ambient singleton ends.

**Reconstruction / correction — ours.** This is a statement about tame interior and finite endpoint sets, not about arbitrary nowhere-dense subsets of the canonical topology.

**Second check.** The independent endpoint sweep verifies that a change of selected interval state leaves a frontier point, while a singleton has no interval cell in its interior.

**Proof and confidence.** PROOFS.tex, section H0KB.104, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.105 — 156-3/034.16

**His words (short quotations and close paraphrase).** Il prend désormais un ensemble ordonné M satisfaisant 1)–7), avec 4) renforcé, et écrit X+Y=(X∨Y)∧(X∧Y)′, XY=X∧Y, X∨Y=X+Y−XY.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** On every compatible Boolean block, the displayed operations give its Boolean ring; xy=x characterizes x≤y. Incompatible pairs have no ring operation stipulated.

**Status: True as written.** Lemma M identifies finite compatible subalgebras with subsets of their atoms. Addition is symmetric difference, multiplication intersection; the two-bit truth table proves all displayed formulas, with characteristic two so minus equals plus. Every identity involves finitely many elements and is checked in their Boolean block.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The independent truth-table program verifies the identities through eight atoms. The formula for order is also the direct subset condition x∩y=x.

**Proof and confidence.** PROOFS.tex, section H0KB.105, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.106 — 156-3/035.1

**His words (short quotations and close paraphrase).** Pour A∈M, il pose M_A={Y:Y⊂A}, avec l’ordre et la modération induits; les fermés sont X=X̄∧A, équivalemment X=Z∧A pour Z fermé compatible avec A.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under the explicit abstract axioms, this defines a coherent relative structure; the two closedness criteria are equivalent.

**Status: True as written.** M proves equivalence. If X=A∧Z with Z closed, monotonicity of the least-closed-upper-bound operation gives c(X)≤Z, hence X≤A∧c(X)≤A∧Z=X. Conversely use Z=c(X), compatible with A by axiom 7 and X≤A.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The second proof views A∧− on a common Boolean block as passage to its principal ideal. The equivalence uses only the leastness of closure, not an unproved meet-preservation property.

**Proof and confidence.** PROOFS.tex, section H0KB.106, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.107 — 156-3/035.12

**His words (short quotations and close paraphrase).** Dans 1), le plus petit élément relatif est ∅ mais le plus grand est écrit X, bien que l’ambient relatif soit maintenant A.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The top of M_A is A. The surviving X is the variable from the earlier cancelled notation.

**Status: Slip.** In the two-element Boolean algebra take A=1 and X=0. Then X is not the largest element below A. For arbitrary A the defining order interval has top A and bottom 0 by direct inclusion.

**Reconstruction / correction — ours.** Replace X by A; the stray M_Y later on the page likewise means M_A in the explicitly repeated condition Y⊂A.

**Second check.** The crop shows the surviving X while the surrounding indices have been changed to A, confirming a pen slip rather than a new convention.

**Proof and confidence.** PROOFS.tex, section H0KB.107, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.108 — 156-3/035.13

**His words (short quotations and close paraphrase).** Les infimum et supremum relatifs restent ceux de M; le complémentaire relatif de X est X′∧A, plus grand Y⊂A compatible avec X et disjoint de X.

**His state and date.** proved on the page; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** For compatible X,Y≤A, their global meet/join lie in M_A and remain its bounds. The relative complement is A∧X′.

**Status: True as written.** M proves the bound claim since A is an upper bound and the global join is least; the meet is below X. Any relative compatible disjoint Y is ≤X′ and ≤A, hence ≤A∧X′. The latter itself is disjoint and compatible, in the Boolean block of X,A.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The principal-ideal Boolean calculation independently verifies its complement equations and relative involutivity.

**Proof and confidence.** PROOFS.tex, section H0KB.108, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.109 — 156-3/036.1

**His words (short quotations and close paraphrase).** Les opérations relatives s’obtiennent en remultipliant par A; on trouve un idéal d’une algèbre de Boole, lui-même algèbre de Boole.

**His state and date.** proved on the page; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every compatible family in M_A generates a Boolean algebra with top A, obtained inside a common global Boolean block by intersecting with A. Relative complements preserve compatibility.

**Status: True as written.** Adjoin A to the compatible family; comparable pairs ensure all its members are compatible with A. The strengthened block axiom gives a common Boolean algebra. Its principal ideal below A has relative complement A∧X′ and top A, and the inherited meets and joins are global relative bounds.

**Reconstruction / correction — ours.** The proof concerns a principal ideal, which has unit A; it does not claim every Boolean ideal has a unit. The isolated horizontal stroke after 1_M is preserved in READINGS.tsv; the preceding closure operation is visibly cancelled. This row asserts the explicitly named Boolean operations. The closure operation is separately proved by the leastness argument in the following row.

**Second check.** The map X↦A∧X is a Boolean homomorphism to that principal ideal; checking complement explicitly proves the claimed operation correspondence.

**Proof and confidence.** PROOFS.tex, section H0KB.109, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.110 — 156-3/036.18;156-3/037.1

**His words (short quotations and close paraphrase).** Les fermés relatifs contenant X sont A∧Y avec Y fermé contenant X; le plus petit donne overline(X)^{M_A}=A∧overline(X)^M.

**His state and date.** proved on the page; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The relative closure is c_A(X)=A∧c(X), and relative 0,A are closed.

**Status: True as written.** M proves that A∧c(X) is relatively closed using the equivalent description, contains X, and lies below every A∧Y with Y closed containing X. The two extrema satisfy the defining fixed-point condition.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The same formula follows from the least-closed-upper-bound universal property without reproducing the page’s sequence of calculations.

**Proof and confidence.** PROOFS.tex, section H0KB.110, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.111 — 156-3/037.3

**His words (short quotations and close paraphrase).** Il calcule la préservation des supremums par l’adhérence relative, puis vérifie la compatibilité de overline(X)^A avec Y. « OK ».

**His state and date.** proved on the page; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Relative closure preserves compatible finite joins and compatibility; consequently the complete structure on M_A satisfies all abstract axioms 1–7.

**Status: True as written.** For compatible X,Y≤A, axiom 7 makes A,c(X),c(Y) pairwise compatible. Distributivity in their common Boolean block gives A∧(c(X)∨c(Y))=(A∧c(X))∨(A∧c(Y)). The same block shows A∧c(X) compatible with Y. Combined with the previous relative rows, every axiom is verified.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The principal-ideal homomorphism proof in M independently yields the join identity. The finite six-element model also checks nontrivial relativizations computationally.

**Proof and confidence.** PROOFS.tex, section H0KB.111, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.112 — 156-3/037.12

**His words (short quotations and close paraphrase).** M est « connexe » si les seuls X ouverts et fermés sont ∅ et 1.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Connectedness here is triviality of the clopen algebra of a structured partial Boolean poset; it is a definition and does not assert topological connectedness.

**Status: True as written.** Open means complement of a closed element under the stipulated axioms. Thus the condition is well defined. The two extrema are always clopen; requiring no others gives the displayed definition, including the allowed trivial structure 0=1.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** The later interval example and the explicit “not for the canonical topology” note on scan 30 confirm this scope.

**Proof and confidence.** PROOFS.tex, section H0KB.112, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.113 — 156-3/037.16

**His words (short quotations and close paraphrase).** « On s’attend » qu’un X ouvert et fermé soit modéré avec tout Y.

**His state and date.** hoped; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under abstract axioms 1–7 with the strengthened Boolean-block postulate, every clopen element is universally compatible.

**Status: False.** The six-element horizontal sum in M satisfies every stated axiom with identity closure. All six elements are clopen, but a and b from different blocks are incompatible. The strongest direct correction is to add universal compatibility of clopens as a separate centrality hypothesis; the following Boolean and spectral conclusions then hold, as M proves.

**Reconstruction / correction — ours.** This refutation is of the explicitly abstract hope, not a failure caused by the earlier G endpoint gap.

**Second check.** check_finite.py enumerates all axioms and every pairwise compatible subset of this model. The written block-by-block verification independently checks the same hypotheses.

**Proof and confidence.** PROOFS.tex, section H0KB.113, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.114 — 156-3/037.18

**His words (short quotations and close paraphrase).** « S’il en est ainsi », les ouverts-fermés engendrent une algèbre de Boole; les éléments de son spectre jouent le rôle de composantes connexes.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** If clopens are universally compatible, they form a Boolean algebra. Its ultrafilter/Boolean-ring spectrum records consistent clopen choices; a literal geometric component interpretation requires additional structure.

**Status: True as written.** M proves closure under joins, complements and hence meets, and gives the ultrafilter topology with its separation and compactness proof, explicitly using the Boolean prime ideal theorem for arbitrary infinite algebras. The phrase “jouent le rôle” is retained as interpretation, not an unstated geometric representation theorem.

**Reconstruction / correction — ours.** The conditional “S’il en est ainsi” is decisive and preserved. We do not mark the conditional false merely because its hoped-for premise fails in general.

**Second check.** Finite cases require no choice: spectra are exactly the atoms, as the next row proves. This separates the algebraic conclusion from the interpretive phrase.

**Proof and confidence.** PROOFS.tex, section H0KB.114, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.115 — 156-3/038.1

**His words (short quotations and close paraphrase).** Si l’algèbre de Boole est finie et 0≠1, les composantes sont les ouverts-fermés non nuls minimaux; si 0=1 la structure est vide.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** A finite nontrivial clopen Boolean algebra has atoms as its spectral points and algebraic components. The trivial Boolean algebra has empty spectrum.

**Status: True as written.** Every nonzero element of a finite Boolean algebra contains a minimal nonzero atom. Distinct atoms are disjoint and their join is 1, or its nonzero complement would contain another atom. An ultrafilter contains exactly one atom and consists of its upper elements. The principal clopen algebra below an atom is {0,a}.

**Reconstruction / correction — ours.** Our expansion of the displayed definitions and their hypotheses; no additional claim is attributed to the manuscript.

**Second check.** A direct truth-table model as subsets of the finite atom set proves the same classification and the empty-spectrum exception.

**Proof and confidence.** PROOFS.tex, section H0KB.115, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.116 — 156-3/038.8

**His words (short quotations and close paraphrase).** Pour A=X_Φ=⋃T_i dans Mod(L), les composantes connexes relatives sont les pseudo-tronçons composants T_i.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The concrete component identification is asserted for the all-G relative closure calculus. It is correct under G+E.

**Status: False.** In D a component can fail to have a closed tame hull, so the required relative structured M_A is not supplied by the original construction. Under E, H proves each T_i clopen in A: its endpoint closure meets A exactly in T_i. Each T_i has no nontrivial tame clopen part. Hence the relative clopen algebra has precisely the T_i as its finitely many atoms.

**Reconstruction / correction — ours.** These are tame components. A rational interval can be topologically disconnected while remaining a single tame component.

**Second check.** The finite-flag closure-mask proof independently shows a relative clopen mask must be constant throughout each T_i.

**Proof and confidence.** PROOFS.tex, section H0KB.116, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.117 — 156-3/039.1

**His words (short quotations and close paraphrase).** Pour a), il suffit de overline(T_i)∧A=T_i; le NB dit que l’adhérence modérée d’un pseudo-tronçon est le fermé associé, puis s’arrête à a∈∂T∖T…

**His state and date.** sketched; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Every pseudo-piece has its associated closed piece as its least tame closure, and separated components remain relatively closed.

**Status: False.** D supplies a single open ray with two purported closed pieces and no least one. Under E, E proves the unique endpoint closure; the strict separator between different components excludes every newly filled endpoint from the other components, so closure(T_i)∩A=T_i.

**Reconstruction / correction — ours.** The omitted endpoint step is supplied as our proof under E; the dots do not constitute a proof on the page.

**Second check.** The topological characterization E independently computes the closure. The finite-flag argument verifies relative closedness without assuming a completion at the ellipsis.

**Proof and confidence.** PROOFS.tex, section H0KB.117, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.118 — 156-3/039.13

**His words (short quotations and close paraphrase).** Pour b), il réduit à T=L; une frontière modérée vide force X=∅ ou X=L. Il conclut « OK ».

**His state and date.** proved on the page; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** Under the concrete calculus’s hypotheses, a pseudo-tronçon is connected in the tame sense. The valid corrected realization is G+E.

**Status: False.** The claimed all-G structure fails as recorded in H0KB.98, so its universal connectedness deduction lacks its defined closure/interior. Under E the full proof is H: a nonempty proper tame subset has an internal endpoint in its frontier; a singleton is immediate. Empty frontier therefore forces the empty or full part.

**Reconstruction / correction — ours.** The argument is valid after the structure is repaired. It is not a claim that arbitrary open interval subsets are connected in τ.

**Second check.** The independent finite-cell proof in H checks that any nonconstant relative mask creates a frontier point.

**Proof and confidence.** PROOFS.tex, section H0KB.118, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.119 — 156-3/040.1

**His words (short quotations and close paraphrase).** Pour une famille finie compatible, S=⋃X_α•={t₁<⋯<t_n}; il affirme que l’algèbre de Boole engendrée a pour composants les points t_i et les intervalles de la subdivision, et est connue par S.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The Boolean algebra generated by the given family is asserted to be the full endpoint-cell algebra determined by the union of their frontiers.

**Status: False.** Lemma B gives the counterexample X=[0,1] on R: one generator yields four elements and two atoms, whereas its five-cell subdivision gives 32 elements. The exact correction identifies generated atoms as joins of cells with equal generator-membership vectors; equality with the full cell algebra holds iff those vectors distinguish every cell. Two generators considered separately with the same singleton frontier also show S alone does not determine the generated algebra.

**Reconstruction / correction — ours.** This is a substantive false claim even on a total real interval; E does not fix it.

**Second check.** The truth-table argument in B and the explicit program count independently verify both the counterexample and the exact corrected classification.

**Proof and confidence.** PROOFS.tex, section H0KB.119, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.120 — 156-3/040.13

**His words (short quotations and close paraphrase).** Dans la liste après {t₂}, l’intervalle est écrit ]t₁,t₃[.

**His state and date.** stated; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The subdivision cell after {t₂} is (t₂,t₃), not (t₁,t₃). Empty exterior cells are omitted.

**Status: Slip.** For t₁=0<t₂=1<t₃=2, (t₁,t₃) contains t₂ and overlaps the preceding cell, so is not a subdivision cell. Replacing the lower index by 2 restores the disjoint ordered list C and F.

**Reconstruction / correction — ours.** A local index slip, separate from H0KB.119.

**Second check.** The crop confirms the surviving lower index 1. Direct membership of t₂ supplies the literal counterexample, independent of the generated-algebra error.

**Proof and confidence.** PROOFS.tex, section H0KB.120, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** No exact later publication by Grothendieck was verified for this particular claim. Its present mathematical disposition is recorded here; no priority claim is made.

#### H0KB.121 — 156-3/041.10

**His words (short quotations and close paraphrase).** Il pense que le cas totalement ordonné et divisible a été traité depuis longtemps, « Hilbert ? », au moins par la relation d’entre-deux.

**His state and date.** asked; 1986-06-09 (continuation dated on 156-3/022; no later date supplied).

**Precise statement — ours.** The historical existence claim is correct: linear order can be reconstructed and axiomatized from betweenness in literature predating 1986. The tentative attribution to Hilbert is not certified here.

**Status: Known.** Huntington and Kline (1917), sections 1 and 4, printed pp.302--303 and 322, give independent postulate systems for betweenness; section 5, p.324, constructs a linear order after choosing two base elements. The source PDF was opened and the construction read. The totally ordered dense case is a special case, with density added as the existence of a middle point for every distinct comparable pair.

**Reconstruction / correction — ours.** The word Hilbert remains a question on the page; absence of a verified Hilbert locator is not a refutation of the correctly verified “done long ago” claim.

**Second check.** Our direct R reconstruction independently proves the dense directed instance. The source’s actual all-points linear-order setting is matched; no claim about arbitrary partial orders is inferred from it.

**Proof and confidence.** PROOFS.tex, section H0KB.121, including its cited full common proof. High for mathematics; decisive wording checked in READINGS.tsv.

**Later status.** Huntington–Kline 1917, Transactions AMS 18(3), 301–325, DOI 10.1090/S0002-9947-1917-1501071-5, §5 p.324; Courcelle 2020 handles a specified partial-order setting much later.

### 4. Groundwork, period meanings, and implicit steps

**Filteredness.** [SGA 4 I, Exposé I 2.7](https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf), original p.15, supplies the period categorical convention. For a poset, parallel-arrow equalization is automatic, leaving nonemptiness and upper bounds for finite subsets. Apply this to the opposite order for lower bounds. His global requirements and strict-cone requirements are separate; they must all be checked. In particular the weak coordinatewise product order on \(\mathbb R^2\) fails a local strict-cone axiom. The strict-both-coordinates order used in our counterexample satisfies it.

**Irreducibility, generic points and sobriety.** [EGA I (1960), 0_I 2.1.1–2.1.3](https://www.numdam.org/item/PMIHES_1960__4__5_0/), original p.21, defines the relevant topological notions. [SGA 4 I, IV 4.2.1–4.2.2](https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf), original pp.336–338, gives sobriety and specialization. We use: a nonempty closed irreducible set has a unique generic point in a sober space. In the T₀ interval countermodel the family of all nondegenerate intervals containing zero is irreducible closed and has no generic point. T₁ alone is never used to infer sobriety. The positive Hausdorff case is proved directly.

**Four distinct uses of boundary and closure.** The finite-cut frontier is a subset of the cut; relative frontier deletes ambient extrema of non-point components; absolute boundary is the set of actual least/greatest elements; the later pseudo-boundary retains endpoints of the associated closed presentation even if omitted from the subset. Canonical topological closure is yet another operation. Scan 25 expressly allows the word “closed” by abuse of language. These notions are translated, not equated on terminology alone. E is what makes the intended subset-level endpoint closure coherent; it also implies the principal closed rays are canonically closed. Under E the supremum of the two manuscript topologies is the canonical topology, without asserting that the two original topologies themselves are equal.

**Ficelles.** The original [156-2 manuscript](https://grothendieck.umontpellier.fr/156-2.pdf), scans 004–007, supplies closed ends, connectedness after the specified contractions and regular immersion by closed conical neighborhoods on compact bases. PROOFS V verifies a compact finite-tree counterexample to the universal specialization and T₀ claims. The gap is the unqualified promotion of component-ficelle lieux to global lieux. It proves the surviving containment implication and restores the converse under the explicit unpunctured-component connectedness condition W_D; connected target lieux satisfy that condition. The real segment example checks the source hypotheses and realizes his failed neighborhood argument. This does not claim every G arises from a ficelle.

**Compatible Boolean blocks.** The margin on scan 33 strengthens the abstract assumptions to finite compatible families in a common Boolean algebra. The relative theorem on scans 35–37 uses that assumption explicitly. Our proof passes to a principal Boolean ideal with unit (A), then proves the relative closure by its least-upper-bound property. It does not assume arbitrary closure is a Boolean homomorphism. The six-element horizontal sum verifies every axiom but has noncentral clopens. Conditional Stone spectra are explained by ultrafilters; the infinite compactness argument explicitly assumes the Boolean prime ideal theorem. Finite spectra need no choice and are the atoms.

**Period comparisons.** [Huntington–Kline (1917), §5 p.324](https://scispace.com/pdf/sets-of-independent-postulates-for-betweenness-2noe2llolk.pdf) gives the historical two-base-point reconstruction for total order; §§1 and 4, pp.302–303 and 322, give postulate systems. This supports “done long ago” without certifying “Hilbert?”. [Pillay–Steinhorn (1984), §2 p.160](https://scispace.com/pdf/definable-sets-in-ordered-structures-4pgckcca61.pdf) supplies the pure dense-linear-order quantifier-elimination example. It identifies the total-order finite-interval special case, not the general partial-order object. No FGA or Bourbaki theorem is invoked without a needed and verified match.

### 5. Later and present status

The closest verified later order-theoretic match is [Courcelle (2020), Definition 3.1 and Theorem 3.5, pp.3–5](https://www.numdam.org/item/10.1051/ita/2020007.pdf). The G hypotheses supply middle points and connectedness through common bounds; the paper's finite/countable convention is retained when comparing its theorem. Our anchor formula and independent orientation proof establish the manuscript theorem in every cardinality. The finite first-order recognition scheme here is restricted to G. Courcelle's Theorem 3.6 and Proposition 5.1, pp.6–10, concern broader arbitrary-poset betweenness; their scope is different.

The supplied SA21 report records a later change of words at 156-7/071: the closed parts become “modérées” and the wider class “constructibles”. That scan was not inspected in this run and its separate bibliography item is marked unverified. A terminology change does not by itself repair the endpoint-hull theorem. No opened later source is claimed to establish that false universal statement.

**Present disposition — ours.** The main reconstruction and recognition problems have complete proofs. The central hull construction is refuted under G and proved under the exact additional E condition. Topological separation and sobriety questions have checked countermodels, including a genuine compact-tree ficelle counterexample. The precise additional condition W_D and the segment case have positive proofs. Compatibility is recovered from inclusion in the corrected concrete calculus, while the meet criterion is refuted. Abstract relativization is proved; clopen centrality and the generated-algebra claim are refuted with explicit corrections. The cancelled ordinary-difference assertion remains false even under E, and has the valid total-order/compatible-difference replacements stated in its proof.

There is no remaining undecided **precise supported item** in this entry. The unaxiomatized general network and higher-dimensional form programmes remain recorded as programmes; every exact version supported by these pages is separately decided. This does not claim that all future versions of those programmes have been solved, or that the proofs written here are new in the literature. Search scope and failed access routes are documented in `records/LITERATURE_LOG.md`.

### 6. Links to nearby objects

| Other tag | Relation | Evidence |
|---|---|---|
| H0KH | same question elsewhere | Nearby H0KH treats reconstruction/orientation in segment network models; 156-3/011.18–017 and /041 reconstruct an ordered tronçon from cuts. The latter’s full G hypotheses are stated and checked here. |
| H0KG | uses | Nearby H0KG isolates filtering F6 and local/global distinctions. The separate global and local axioms on 156-3/007 and /009 are all needed; weak product order fails the local strict-cone axiom. |
| H0KF | uses | 156-3/002.10 interprets tame pairs using singular places, regular lines and segment endpoints of the earlier model. The bracket is a map from those data to S₀, not an equivalence theorem. |
| H0KI | uses | 156-3/022.16–024 invokes the lieux of a ficelle. Original 156-2/002–008 definitions give the genuine compact-tree counterexample in V; the universal T₀/specialization assertion fails, while the connected-component repair and segment example are proved. |
| H0KJ | uses | Nearby H0KJ covers ordered cuts and gluing. The conical level-cut construction from 156-2/007 underlies PROOFS V. Its actual two closed sides cover the cone; no unrestricted cone-gluing theorem is assumed. |
| H0KK | same question elsewhere | Nearby H0KK concerns clopen Boolean algebras, rives and Stone spectra; 156-3/037.18–038 gives a conditional spectral component interpretation. The shared Boolean language is precise, not an identification of spaces. |
| H0KC | used by | Nearby H0KC is the next Analysis situs draft on contrées, Cont 1–5 and a presumed Boolean algebra. 156-3/033–037 supplies a predecessor partial Boolean/closure scheme. Only the supplied catalogue/context relation is claimed. |
| H0K9 | same question elsewhere | SA21 reports 156-7/071 renames the closed parts modérées and all parts constructibles in the atelier development. This is a documentary context link; that later scan was not supplied or independently inspected here. |
| H0KD | same question elsewhere | Nearby H0KD concerns order comparisons in the 156-5 Sorite ensembliste. The order/inclusion distinction of 156-3/032 is a concrete earlier occurrence; no exact later theorem is claimed. |
| H0KE | same question elsewhere | Nearby H0KE is the symmetric viewpoint/magma of an ordered set. 156-3/011–017 forgets orientation through betweenness and cut partitions. This is a precise question-level relation, not a proven equivalence of the later magma. |
| H0KA | uses | Title/date/pagination evidence: sheet III dated 8 June 1986, continuation at scan 022 dated 9 June. Scan numbers exceed handwritten page numbers by one in 156-3. |
| H00K | special case | The finite compatible interval calculus of 156-3/030–034 is a one-dimensional example relevant to the earlier category-level tame-topology axioms in nearby H00K; this run proves the example only under E. |
| H00M | same question elsewhere | Nearby H00M concerns later tame-topology drafts and adapted partitions. The finite cut/closure scheme here is a related partition question; no unseen later axiom is imported. |
| H05H | special case | Our comparison only: on a dense TOTAL order without endpoints, finite unions of intervals with parameters and points are precisely one-variable definable sets in pure order, by DLO quantifier elimination (Pillay–Steinhorn 1984, §2 p.160). General partial G-orders are not o-minimal structures by this argument. |
| H05X | same question elsewhere | Nearby H05X explicitly records the notes’ comparison with o-minimality. The restricted total-order comparison is in this entry’s groundwork; it is not Grothendieck’s claim. |
| H0CI | same question elsewhere | Nearby H0CI asks whether full tame-topology axioms are o-minimal axioms. 156-3 supplies only an interval/partial-Boolean prototype; the strict plane and doubled line rule out replacing every G by a linear-order model. |
| H0KJ | contradicts | The unqualified component-lieu promotion on 156-2/008.3–4, in the neighbouring cut/gluing development, fails for the terminal-hair example: a two-point conical cut is a lieu of the left component but leaves three global complement components. This is the exact gap in the initial proposed proof of 156-3/022.16; V gives the counterexample and W_D repair. |

### 7. The note entries: 5 verdicts

**codex:J156-3-01#1.** Confirmed: 003.6m Oui/inverse; 004 forecasts; 006 provisional finiteness; 008 margin reworking the line example.

**Mathematical verdict — ours.** Corrected: faithful reservations, but complement reflection is refuted; the two provisional uniqueness forecasts are refuted under the displayed axioms. Read in full. D checks every intended ordered hypothesis for the converse failure; N checks all provisional clauses for the two forecasts. The future-axiom programme itself is not refuted. The ordered subclass is solved by R/A.

**Placement.** H0KB.6; H0KB.9; H0KB.10; H0KB.11; H0KB.15; H0KB.23. Correct object: H0KB.

**codex:J156-3-02#1.** Confirmed: 013–014 reconstruction proof reaches OK; 017.17 recognition task is not written out.

**Mathematical verdict — ours.** Confirmed for reconstruction after the local non-strict convention and pen slips are separated; precise recognition versions now proved in this run. Read in full. The earlier il reste remark is cancelled and should not be treated as a surviving proof gap. The explicit anchor formula, independent orientation proof and finite computation agree. All-cardinality recognition is our construction.

**Placement.** H0KB.29; H0KB.32; H0KB.33; H0KB.38; H0KB.39. Correct object: H0KB.

**codex:J156-3-03#1.** Confirmed: 023 T₀/sobriety and converse questions; 024 interval closure question, cancelled qualifications, and ficelle failure.

**Mathematical verdict — ours.** Corrected: all-G T₀ and sobriety are refuted; T₁ does not force totality; generic interval closure fails. The universal ficelle specialization/T₀ assertion is refuted by an actual finite-tree ficelle; the segment-ficelle neighborhood-failure assertion remains confirmed. Read in full. The strict plane replaces the invalid weak product-order idea. The T₀ nondegenerate-interval model proves the stronger nonsobriety result. Original 156-2 definitions were obtained and checked before asserting a ficelle example. The final source audit withdrew an overstrong conical-cut promotion step and replaced it with the complete tree counterexample and the proved W_D repair.

**Placement.** H0KB.54; H0KB.55; H0KB.56; H0KB.58; H0KB.61; H0KB.64. Correct object: H0KB, using H0KI groundwork.

**codex:J156-3-04#1.** Confirmed at 032.14m: broad recovery from inclusion, then the proposed meet criterion with ???.

**Mathematical verdict — ours.** Corrected and separated: the meet criterion is refuted even under E; the broader recovery problem is positively solved under the exact repaired G+E calculus. The original all-G subset relation fails to be intrinsic. Read in full. The failure of a suggested criterion is not the failure of definability. The accepted proof uses atomic joins, the comparability polar and a Boolean disjoint decomposition. The earlier singleton-adjunction attempt was invalid and was explicitly withdrawn.

**Placement.** H0KB.89; H0KB.90; PROOFS O; correction history in WORK_LOG. Correct object: H0KB.

**codex:J156-3-05#1.** Confirmed: 036–037 relativization, 037 clopen hope, 039 ellipsis, 041 exercise/Hilbert?. Scan 040 audited in the continuous span.

**Mathematical verdict — ours.** Confirmed for the conditional abstract relative theorem; clopen centrality refuted; general closure claim refuted with exact E repair; generated-algebra claim refuted; precise recognition exercise proved; historical linear betweenness Known. Read in full. The six-element model satisfies even the strengthened Boolean-block axiom. The dots on 039 are not a proof. The one-generator algebra has four elements, not the full thirty-two-element subdivision algebra. Verified historical source is Huntington–Kline, not the tentative Hilbert attribution.

**Placement.** H0KB.109; H0KB.111; H0KB.113; H0KB.117; H0KB.119; H0KB.121. Correct object: H0KB; spectral comparison links to H0KK.

### 8. Our supplied research results, kept separate

The results folder was opened only after the substantive entry draft had been written; the UTC event is recorded in progress.log. It supplied no research-statement row bearing on these objects. CONSEQUENCES.tsv therefore has its header and no forced links. The proofs labelled ours in this entry are work of this run, not pre-existing results imported from that folder.

