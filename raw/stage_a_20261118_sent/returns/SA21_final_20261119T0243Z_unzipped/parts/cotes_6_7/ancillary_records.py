"""Manually assessed reading alarms and checked cross-references.
The locator helper formats already selected source scans; it makes no verdicts.
"""
from claim_records import locations
READINGS=[];LINKS=[]
def loc(cote,folder,scan):
    lines,_=locations(cote,[(folder,[scan])])
    return lines[0] if lines else f'156-{cote}, scan{scan} (not supplied)'
def R(cote,folder,scan,reading,alternative,evidence,weight='high',confidence='medium'):
    READINGS.append(dict(cote=f'156-{cote}',scan=scan,line=loc(cote,folder,scan),reading=reading,
        alternative=alternative,evidence=evidence+' No scan inspected; this is an alarm, not an emendation.',weight=weight,confidence=confidence))
def L(source,target,what,evidence,kind='folder',notes=''):
    LINKS.append({'kind':kind,'from':source,'to':target,'what':what,'evidence':evidence,'note_ids':notes})

R(6,1,5,'(1.7) a comprehension of the form {X∈~F | Omb(X)}','{Omb(X):X∈~F}',
  'A multiombre is a family of subsets of M; the written comprehension mixes a predicate with the image operation.')
R(6,1,5,'(1.8) Multomb versus Omb in the asserted relation','Distinguish the family of stratum shadows from its union',
  'The codomain is Fig(M) for the former and P(M) for the latter; a type check is needed before reading the equality.')
R(6,3,22,'A tilde/deployment notation occurs where large shadow is needed','Omb(X), not ~X, if the subsequent refinement test is intended',
  'Deployment uses face order; the receiving map and refinement representation use the refinement lower set. The argument changes if these are interchanged.')
R(6,6,42,'M where the elementary set of the subatelier is intended','M′',
  'The correspondence is between the chosen subfamily and its own elementary objects, not all ambient elementary objects.')
R(6,6,45,'F′ and F″ interchanged in the subatelier/image formulas','Recheck primes against the inclusion and inverse-image directions',
  'One side refers to the subatelier while the other is its image; type and containment tests locate the ambiguity.')
R(6,7,50,'The upper stratum may be a successor of a minimal one in the At8 criterion','When ≪=≤, At8 forces every stratum itself minimal',
  'The two-element chain certificate contradicts the written successor criterion; VII35 explicitly states M=L. This may be an author error rather than a transcription error.','high','high')
R(6,7,51,'Discard only empty closed preimages in f*F','Possibly discard strata whose open preimages are empty',
  'The saved {a},{b},{a,b,c} counterexample makes the top open stratum empty after pullback. The suggested repair is analyst-owned.','high','high')
R(6,7,57,'Finite figure formula appears to omit compatibility','Require the generating strata to be pairwise compatible',
  'A union of incompatible elementary figures need not exist; preceding Atens conditions explicitly distinguish compatible families.')
R(6,8,59,'Unqualified existence of binary infima in M','Existence for lower-bounded pairs, or allow zero outside M',
  'Disjoint elementary figures have empty face intersection, which is not an elementary nonzero object.')
R(6,8,65,'Marginal At10: X≠Y, x≪°X, y≪°Y ⇒ x⊥y, without compatibility','Add X compatible Y',
  'The longer formulation on the same scan explicitly inserts compatibility; omitting it changes the class of ateliers.')
R(6,12,91,'Atens4 concludes X compatible Y after already assuming it','Conclusion X′ compatible Y′',
  'The whole proposition is a criterion for compatibility of the two refinements; the literal conclusion is tautological.')
R(6,12,92,'F′∈M in the boundary-subdivision extension formula','Possibly F′∈F (a general boundary figure)',
  'The boundary of an elementary figure usually has several maximal faces and is not itself elementary.')
R(6,12,92,'“unique” elementary figure with boundary F′, without ambient support','Add fixed support |X| and the intended equivalence convention, if present in ink',
  'Boundary alone does not determine an underlying ambient set or geometric filler. This could be a missing hypothesis in the mathematics.')
R(6,12,94,'Interior-shadow containment used in the wrong direction for inheriting At10','Recheck which ambient/subatelier interior is included in the other',
  'Removing available proper faces can enlarge an interior; the proof needs the direction justified by the stated thickness hypothesis.')
R(7,1,14,'Two upper-bounded elements have a “plus grand élément” in the dual polyhedral condition','A least upper bound / plus petit majorant',
  'Order duality turns a greatest lower bound into a least upper bound, not a greatest element.')
R(7,1,15,'Inf≪(X,L) in the definition of X′_L','Inf≪(X′,L)',
  'The deployment displayed immediately afterwards consists of faces of X′ refining L.')
R(7,1,15,'G′=G′·L in the generalized compatibility proposition','G′_L=G′·L',
  'Otherwise the ambient refinement is equated to its restriction before the theorem compares them.')
R(7,3,26,'Lemma1 states X≤Y⇔X≪Y without a common ambient hypothesis','Restore compatibility or a common face upper bound',
  'Its proof applies ML1 to X,Y, which requires the missing ambient setup; otherwise it collapses the two deliberately distinct orders.')
R(7,3,27,'Open small shadows “forment une partition de X”','A partition of omb(X)',
  'The parts consist of lieux, while X is an elementary object; the union is the small shadow.')
R(7,3,27,'Y′ called the least element after the proof establishes Y≤Y′ for every receiver','Y is the least element',
  'The displayed inequality identifies Y, not the arbitrary Y′, as the least receiving face.')
R(7,4,35,'ML3 x∈L / x∉L uncertainty','x∈L',
  'ML3 is the locus receiving-face condition and is used for interior-locus coverage.')
R(7,4,37,'An elementary figure written {{X}}','↓X (or the corresponding principal figure), not a singleton unless X minimal',
  'The construction requires lower subsets; a singleton nonminimal stratum violates closure under faces.')
R(7,4,41,'LemmaA assumes X,Y≪Z before equating ≤ and ≪','Possibly X,Y≤Z or explicitly compatible',
  'Two unrelated refinements of one figure need not be compatible; the earlier local lemma required face-boundedness.')
R(7,6,52,'PratΛ6 has Z′≪Z and Z′≤X,Y','Z≪Z′≤X,Y',
  'A common-refiner lifting axiom must put the given Z below a common receiving face, not produce an unrelated refinement below Z.')
R(7,6,54,'“le seul axiome pas satisfait est AtL1” for arbitrary M','Retain the preceding proviso that every X lies above a minimal element for L2',
  'The same page states L2 is equivalent to this proviso; a descending chain with no minima violates it. Could be an author shortcut.','high','high')
R(7,6,56,'x=y / x≠y in the CL small-shadow argument','x≠y for disjoint distinct lieux',
  'The graph on point-like lieux is irreflexive; equality would give the opposite compatibility test.')
R(7,8,66,'cosupp_F(A)=cosupp_F(A)∩Λ with mismatched types','Recheck the left ambient subscript and A∩Λ argument',
  'One side must be the polar in Λ and the other the restriction of the polar in M/F. The printed equality cannot keep identical ambient types.')
R(7,8,71,'A point deployment has cardinal0','Cardinal1',
  'The singleton point is its own elementary stratum and has nonempty deployment.')
R(7,9,79,'A used where a subset of P is being complemented','|A|',
  'A is a collection of elementary figures; its represented union |A| is a subset of the point set P.')
R(7,9,74,'Clause(vi)b: for all x,y∈P a support separates them, without x≠y','Add x≠y',
  'No subset can contain and exclude the same point. The following quotient-by-indistinguishability normalization confirms that distinct points are intended.','high','high')
R(7,10,81,'|A|=supp(A) as an equality of different types','|A|=|supp(A)|',
  'The proof concerns the represented union of a closure, not equality between subsets of P and subsets of M.')
R(7,10,83,'J\P / J\|P| ambiguity in the two-strand endpoint calculation','Recheck whether the complement is taken in the endpoint set or in the space of pairs',
  'The domain changes between coordinate endpoints and pair loci; the rectangle computation is type-sensitive.')
R(7,12,99,'supp(A)=A′ in the P4 example','supp(A)={A}',
  'The graph A′—A—B—B′ gives {A}⊥={A′,B}, hence {A}⊥⊥={A}. The exact finite computation is saved.','high','high')
R(7,12,99,'cosupp A∪B without clear grouping','cosupp(A∪B), if the calculation of the common polar is intended',
  'The polar of a union is the intersection of polars; (cosupp A)∪B is a different set.')
R(7,13,104,'Stability conclusion repeats X|°|Y','Conclusion X′|°|Y′',
  'The axiom is meant to transmit interior disjointness under immediate refinements; repeating the hypothesis is vacuous.')
R(7,14,114,'Finite figures listed as all finite pairwise compatible subsets','Finite pairwise compatible lower subsets',
  'AtM1 requires lowerness, and singleton {X} for nonminimal X otherwise supplies an immediate counterexample.','high','high')

# Author cross-references within the fully read VI–VII corpus.
L(loc(6,2,14),loc(6,3,21),'Refinement no longer generated by face inclusion plus subdivision','Explicit marginal reference to manuscript p20; source and target read. C-SA21-6-004.')
L(loc(6,2,17),'156-4 scans54–57: J156-4-07 lines81–160; scan59: J156-4-08 lines44–64','VI recalls IV C1–C3 as At1–At3','Both endpoints read directly. IV scan54 defines equality-only irreducibility; VI12 explicitly strengthens it to complete join-primality. The recall is not a license to identify the definitions.')
L(loc(6,4,30),'156-4 scans55–56: J156-4-07 lines106–151; scan59: J156-4-08 lines44–64','Reference to Corollary2, converse remark and C3','Both endpoints read. The uncertain IV/V label is most naturally IV by the matching proposition numbers; ink not decided.')
L(loc(6,5,38),loc(6,6,43),'Lower-family inheritance corrected by Sousat2','Both passages read; three-point certificate proves why the correction matters. C-SA21-6-011.')
L(loc(6,5,41),'156-4 scan54, J156-4-07 line100','Deleted proof recalls irreducibility definition','Both endpoints read. The source block is canceled, and the earlier weak definition differs from VI12; preserve the deletion.')
L(loc(6,6,43),loc(6,3,22)+'; '+loc(6,4,28),'Inheritance of At4–At7 cites manuscript pp21,27','Both target axiom passages read; At7 is the added transitivity of immediate refinement.')
L(loc(6,7,50),loc(6,6,45),'Trivial ateliers reference manuscript p44','Both endpoints read; the At8 successor assertion is separately corrected by VII35.')
L(loc(6,7,51),loc(6,6,48),'Morphisms definition at manuscript p47','Both endpoints read; direction of stratum maps is the issue, not a completed functor category.')
L(loc(6,7,52),loc(6,6,48),'Marginal perplexity about the inverse direction of stratum maps','Both endpoints read. C-SA21-6-043.')
L(loc(6,7,53),loc(6,6,47),'Small-shadow local bijection (1.53), manuscript p46','Both endpoints read. Local subfigure-lattice bijection is not global injection.')
L(loc(6,7,53),loc(7,1,13),'Marginal “correctif GFVI p12” likely points to the later strict-refinement repair','Both VI13 and VII13 checked. VII13 supplies the actual corrective statement; VI13 is a relation discussion. Chapter numeral uncertain; this is an unresolved reference-reading alarm, not an emendation.')
L(loc(6,7,54),loc(6,5,35),'Comparison to exampleB, manuscript p34','Both endpoints read; affine structure versus underlying set shadows.')
L(loc(6,7,56),loc(6,6,43),'Sousat1–2 recalled from manuscript p42','Both endpoints read; nonempty lowerness and compatibility closure are distinct.')
L(loc(6,8,60),loc(6,7,56),'Set-like finite-type axioms, manuscript p55','Both endpoints read; compatibility on elementary figures is an additional relation.')
L(loc(6,8,63),loc(6,9,73),'Converse criterion promised at manuscript p72','Both endpoints read; missing-subfigure separation by an interior lieu uses the locus axioms.')
L(loc(6,8,65),loc(6,9,73),'At10 marginal reference to manuscript p72','Both endpoints read; compatibility condition matters in both.')
L(loc(6,9,70),loc(6,9,67),'Gluing corollary recalls earlier construction on manuscript p66','Both endpoints read; arbitrary-cover existence depends on At11.')
L(loc(6,9,72),loc(6,8,60),'Relation(1.58), manuscript p59','Both endpoints read; disjointness/compatibility relation in the earlier axiom discussion.')
L(loc(6,10,78),loc(6,10,74),'At12 implies proposition of manuscript p73','Both endpoints read; compatibility of refinements controlled on their overlap.')
L(loc(6,10,78),loc(6,9,70),'Corollary2, manuscript p69, restricted to finite index sets','Both endpoints read; the finite qualifier is explicit and later infinite inference canceled.')
L(loc(6,11,82),loc(6,8,60),'Support witness proof recalls(1.58), manuscript p59','Both endpoints read; disjointness stability is part of the supporting argument.')
L(loc(6,7,50)+'; '+loc(6,7,51),loc(7,4,35),'Author’s later correction of At8 when ≪=≤','Both endpoints read. VII35 line100 says M=L discrete; the saved two-element chain refutes the earlier successor version.')
L(loc(7,1,13),'156-5 scans20–21, J156-5-03 lines38–79','Strict refinement strengthens the set-refinement definition in V ms19–20','Both endpoints directly read. V has least receiver plus intersections as unions of faces; VII asks each intersection to be empty or a face of the source stratum.')
L(loc(7,1,13),loc(6,7,53),'New strict-refinement reflection replaces VI ms52 criterion','Both endpoints read; the source’s VI/II ambiguity is retained but VI53 matches the quasi-set embedding claim.')
L(loc(7,2,23),loc(7,5,46),'Implication diagram redone at manuscript p45','Both endpoints read; compare the same spacious/polyhedral branch consistently.')
L(loc(7,2,24),loc(7,2,18),'AtC implication cites the NB at manuscript p17','Both endpoints read; reduced AtD variant and exclusive-piece criterion.')
L(loc(7,3,27),'156-7 scan7 (manuscript p6), absent from supplied Codex files','AtM4 receiving-stratum formulation is cited','Source read; exact target cannot be checked because VII scans2–9 were not supplied. This row is an explicitly unresolved link, not a completed both-end verification.')
L(loc(7,3,33),loc(7,3,30),'Lemma2 Corollary4, manuscript p29','Both endpoints read; transitivity/least receiving stratum used in compatibility proof.')
L(loc(7,4,36)+'; '+loc(7,4,38),loc(7,3,30),'Compatibility definition(1), manuscript p29','Both endpoints read; uses exclusive locus shadows and the common lower-face deployment.')
L(loc(7,4,39),loc(7,2,19),'AtSupp reference, manuscript p18','Both endpoints read; witness principle weaker than the later absorption axiom.')
L(loc(7,4,39),loc(6,7,53),'Uncertain VI/VII ms52 reference in the set-like discussion','Both candidate nearby topics checked; VI53 is the quasi-set definition, VII53 is the PratL′ list. Treat the chapter reading as unresolved, not as a proved identification.')
L(loc(7,4,41),loc(7,3,29),'Corollaries1–3 at manuscript p28','Both endpoints read; local ambient hypotheses must survive the abbreviated reformulation.')
L(loc(7,5,42),loc(7,3,31),'Reasoning on manuscript p30','Both endpoints read; Λ-generalization needs the same common-refiner lifting that locus proofs used.')
L(loc(7,5,42),loc(7,3,33),'Lemma6 at manuscript p32','Both endpoints read; uniqueness of compatible receiving strata.')
L(loc(7,5,46),loc(7,2,23),'Comparison with old implication diagram, manuscript p22','Both endpoints read; replacement of loci by dense Λ.')
L(loc(7,5,48),loc(7,5,43)+'; '+loc(7,4,35),'Earlier MΛ conditions and ML5 graph condition','Both endpoints read. Source recalls manuscript pp42,34 before the failed simplification.')
L(loc(7,5,48),loc(7,6,50),'“Non, cf plus bas p49” withdraws graph-only inference','Both endpoints read; missing common-shadow/restriction implication explicitly recognized.')
L(loc(7,6,50),loc(7,5,43),'Proposition at manuscript p42 after adding MΛ6','Both endpoints read; the strengthened list makes the intended recovery tautological at the cost of the extra axiom.')
L(loc(7,6,51),loc(7,2,24)+'; '+loc(7,2,23)+'; '+loc(7,5,46)+'; '+loc(7,5,47),'Algebraic axioms and implication-diagram recap','Both endpoints read; “spacious” now includes AtC(spac), a terminology change.')
L(loc(7,6,52),'156-7 scan7 (manuscript p6), absent from supplied files','Prat translation refers to the earlier AtM list','Source read; target absent. Explicit supplied-corpus limitation; no reconstruction masquerades as a checked target.')
L(loc(7,6,52),loc(7,5,43),'PratΛ refers to manuscript p42','Both endpoints read; dense-Λ version retains compatibility data.')
L(loc(7,6,53),loc(7,4,35),'PratL′ refers to manuscript p34','Both endpoints read; graph/locus presentation of ML theorem.')
L(loc(7,6,55),loc(6,7,52)+'; '+loc(6,5,41),'Embedding and spacious-image definitions cite VI ms51,40','Both endpoints read. Later VII58–59 retracts the global converse.')
L(loc(7,6,55),loc(7,5,46),'Four equivalent systems at manuscript p45','Both endpoints read; additional distinct-locus disjointness is explicitly imposed.')
L(loc(7,7,65),loc(7,7,62),'Support correspondence induced by bijections of manuscript p61','Both endpoints read; figure/elementary support-system restriction and Env.')
L(loc(7,8,68),loc(7,7,64)+'; '+loc(7,7,65),'Earlier support operations, manuscript pp63–64','Both endpoints read; the quasi-set case becomes ordinary Boolean complement while the general case does not.')
L(loc(7,8,71),'156-3 scan9, J156-3-01 lines288–321','Explicit III manuscript p8 reference to an ordered tronçon','Both endpoints directly read. III requires directedness and strict interpolation, not an arbitrary poset; VII’s broader interval claim cannot import those hypotheses silently.')
L(loc(7,11,92),loc(7,12,96),'Margin strengthens disjoint interiors to orthogonal interiors, manuscript p95','Both endpoints read; essential for the support-closure argument.')
L(loc(7,12,100),loc(7,11,87),'Corollary at manuscript p86 used when redefining X°','Both endpoints read. VII87 absorption is optional and later criticized; its hypothesis must not disappear in the notation change.')
L(loc(7,13,103),loc(7,6,52),'MagΛ uses old PratΛ axioms at manuscript p51 with Λ=M','Both endpoints read; this is a change of primitive disjointness data, not merely a renaming.')
L(loc(7,14,111),'156-8 scan8, J156-8-01 lines237–266','Final VII Mag1–4 recapitulated at start of VIII','Both endpoints directly read; neighbouring reader independently confirmed. VIII explicitly cites VII ms110.')
L(loc(7,9,74),'156-8 scan42, J156-8-06 lines5–46','External support realization revisited in VIII','Both endpoints directly read. VIII explicitly cites VII ms73 and changes to the primitive interior-disjointness setting; clauses are not identical.')

# Published-work comparisons: exact endpoints checked, status of match explicit.
L(loc(6,5,36)+'; '+loc(6,5,37),'Esquisse1997 §5, printed pp25–27 (primary French PDF, PDF pp20–22)',
  'Canonical pieces and extra gluing data for stratified spaces',
  'Both passages read. Conceptual link only: Esquisse discusses decomposition and isotopy choices, not the exact pseudodisk/At* reconstruction.',kind='published work')
L(loc(6,9,67)+'; '+loc(6,9,68),'SGA4II Definition2.1 (sheaf matching-family bijection)',
  'Formal comparison of local compatible data and unique gluing',
  'Both passages read. Analyst comparison, not a claim that atelier At11 follows from a theorem in SGA4 or that the same geometric object occurs there.',kind='published work')
L(loc(7,13,101),'Récoltes et Semailles reused typescript fragment, marked A6 in the transcription',
  'Canceled prose reused as writing paper; no mathematical dependence',
  'The verso fragment was fully read in the supplied transcription. A matching published R&S page was not identified/opened, so this is an explicitly unresolved material link, not a checked mathematical Stage5 link.',kind='published work')
