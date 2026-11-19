"""Manual problem index: explicit requests, deferred steps, hopes and editorial doubts.
The tables serialize judgments made while reading the complete transcription.
New objections found by this review are directions, not invented authorial problems.
"""
import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
P=[]
def add(n,title,occ,as_he,plausible,state,why,worth,refs):
 P.append(dict(id=f'MP-SA12-{n}',title=title,occurrences=occ,as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open=why,worth=worth,refs=refs))
unknown='No opened source explains why this particular leaf was left unfinished; absence of a proof here is not evidence that the problem remained open later.'
add(151,'The duality, Künneth, Lefschetz and L-function programme',
 ['33/2:3–9; SA12-601'],
 'Develop torsion duality, the Künneth formula and Lefschetz; pass to ℓ-adic coefficients; apply the results to L-functions. This is a plan, with no particular rationality assertion on this leaf.',
 'For separated finite-type morphisms in the appropriate invertible-torsion setting, construct Rf!, cup products, trace and duality with their coherence; choose a separate ℓ-adic formalism before forming limits.',
 'SGA4 XVII5.4 (Künneth) and XVIII2–3 (trace and duality), published1973 from the1963–1964 seminar, directly develop the formalism. No exact L-function theorem is assigned to this introductory sentence.',
 unknown,'Worth using as the dossier’s organizing sequence; the sentence alone does not define a new theorem to pursue.', ['SA12_SGA4III'])
add(152,'Write the categorical algebraic–analytic comparison',
 ['33/6:175–181; SA12-604; CL-SA12-609'],
 'The margin proposes an equivalence for constructible torsion algebraic and analytic sheaves and says à rédiger.',
 'Analytification identifies the algebraically constructible finite étale category with the corresponding analytic category having algebraic stratifications; arbitrary analytic strata are too broad.',
 'SGA4 XI4 and XVI4.1 give finite-cover and cohomological comparison. The opened theorem XVI4.1 explicitly assumes proper f or constructible F. Stacks03RW specifies algebraic constructibility. A closed analytic exponential graph supplies the earlier run’s obstruction to arbitrary analytic strata, rechecked here.',
 unknown,'Worth an exact convention audit and comparison of the category statement with the published finite-cover theorem; the unrestricted variant is false.', ['SA12_SGA4III','SA12_Stacks03RW','SA12_Milne2013'])
add(153,'The two relative comparison maps over an analytic base',
 ['33/8:209–222; SA12-605; CL-SA12-610'],
 'For a finite-type relative scheme over a complex analytic space, prove both the displayed global-cohomology and higher-direct-image comparison maps are isomorphisms.',
 'First specify a category of relative schemes over analytic spaces and its étale topology. For algebraic bases over C, finite type plus constructible torsion coefficients gives the precise established specialization.',
 'SGA4 XVI4.1 proves the algebraic-base specialization with the correct properness/constructibility disjunction. Searches of SGA, primary comparison papers, and analytic/rigid literature did not identify the literal relative-analytic category and both assertions with these exact quantifiers.',
 'The source itself has not defined the relative category; this is a formulation obstacle evidenced by the leaf, not a historical claim about why research stopped.',
 'Worth a focused bibliographic and definitional investigation; do not advertise it as a surviving open comparison theorem.', ['SA12_SGA4III','SA12_Hansen2017'])
add(154,'Continuity from analytic neighbourhoods to the local ring',
 ['33/8:226–234; SA12-605; CL-SA12-611'],
 'After passing to the limit over neighbourhoods of y, the displayed analytic-local cohomology comparison should follow; the wording is conditional.',
 'Combine an established relative comparison with finite-presentation continuity in a precisely defined relative-analytic category; retain the base-change map to Spec O_Y,y.',
 'Stacks03Q9 Theorem59.53.1 verifies the corresponding algebraic strict-local continuity mechanism. SGA4 XVI4.1 alone does not establish arbitrary analytic-base continuity. No exact source for the full displayed conjunction was verified.',
 unknown,'Worth following jointly with MP-SA12-153, because changing the category or the limit changes the claim.', ['SA12_Stacks03Q9','SA12_SGA4III'])
add(155,'The rigid-analytic comparison hope',
 ['33/8:224; SA12-606; CL-SA12-612'],
 'The relative comparison should also generalize to the rigid-analytic context, without specified field or coefficient hypotheses.',
 'For an affinoid algebra A in Hansen’s setting, compare torsion étale cohomology of Spec A and Spa A; separate this from a categorical equivalence or arbitrary relative direct-image comparison.',
 'Hansen, arXiv1708.07276 v1 (24August2017), Theorem1.7 proves the affinoid cohomological comparison for arbitrary torsion abelian sheaves. Its Conjecture1.8 concerns a stronger categorical statement. Huber’s1996 book, verified bibliographically, is explicitly cited by Hansen for the constant-sheaf and proper comparisons. The notebook’s unspecified generalization is only partly identifiable.',
 unknown,'Worth identifying the intended relative functor and coefficient restrictions before choosing which modern theorem or remaining question applies.', ['SA12_Hansen2017','SA12_Huber1996'])
add(156,'Complete the localization and support spectral sequences',
 ['33/12:346–355; 28:754–771; SA12-609; CL-SA12-617,638'],
 'Only headings for an exact sequence and a spectral sequence are written after the support functors; the edge consequence is used later.',
 'For closed i and complementary open j, use the localization triangle and E2^{pq}=H^p(Y,H^q_Y(F))⇒H^{p+q}_Y(X,F), with the usual bounded-below convergence.',
 'Stacks09XP §59.79 states the support formalism and spectral sequence. Hartshorne’s Local Cohomology, LNM41 (1967), explicitly derives from the Harvard fall1961 Grothendieck seminar, matching the dated margin at bibliographic level.',
 'This is an omitted exposition step, not evidence of an unresolved theorem; the leaf itself cites earlier support-cohomology sources.',
 'Worth filling as commentary because it explains exactly how the later edge map is obtained.', ['SA12_Stacks09XP','SA12_Hartshorne1967'])
add(157,'Define the local fundamental class',
 ['33/12:371; 22:575–598; 24:626–646; SA12-610; CL-SA12-633,634'],
 'Give the local fundamental class; later leaves supply the Kummer boundary of a regular equation and products for a regular sequence.',
 'For a regular immersion i:Y→X of codimension d with n invertible, construct cl_i in H^{2d}_Y(X,Z/n(d)), compatibly with regular local factorizations.',
 'SGA4 XVIII develops this construction; Riou, ExposéXVI §2.3, gives regular-immersion Gysin classes and their composition/excess properties. The codimension-one boundary is independently checked here. The initial request is partly answered within the same source.',
 'The request is followed by an actual construction at22–24; the independence proof remains asserted rather than supplied.',
 'Worth treating as one developing construction across the leaves, rather than several independent open problems.', ['SA12_SGA4III','SA12_Riou2014'])
add(158,'Absolute cohomological purity',
 ['33/14:409; 26:708–720; SA12-611; CL-SA12-619'],
 'Replace the smoothness hypothesis by regularity in the boxed absolute-purity problem, with qualifications involving good primes and resolution.',
 'For a regular noetherian scheme X and regular closed subscheme Y of pure codimension c, with n invertible on X, the canonical class identifies Ri!Z/n with Z/n(−c)[−2c].',
 'Gabber absolute purity is stated precisely in Riou XVI3.1.1. Riou’s introduction distinguishes Fujiwara’s2002 exposition from Gabber’s new proof announced2005; the seminar ran2006–2008, arXiv collection2012, printed book2014. The Fujiwara primary article was not successfully opened and is marked unverified.',
 'SGA4 XVI3.10 and XIX’s introduction explicitly connect the historical limitation to resolution of singularities and distinguish equal-characteristic zero from the unresolved general case at that time.',
 'Worth a historical theorem-to-draft comparison; the stated invertible-torsion regular-pair problem is now settled.', ['SA12_Riou2014','SA12_ILO2012','SA12_Fujiwara2002','SA12_SGA4III'])
add(159,'Relative purity over an arbitrary base',
 ['33/14:411; SA12-611; CL-SA12-620'],
 'There is also a relative purity theorem over an arbitrary base, with no full statement on this leaf.',
 'For a smooth pair Y⊂X over S of pure relative codimension c and n invertible, the support cohomology is concentrated in degree2c and has the canonical twist; formation commutes with base change.',
 'SGA4 XVI3.7–3.8.1, read in the opened full text, gives the smooth-pair statement and base-change corollary;3.10 identifies the twist using fundamental classes.',
 unknown,'Worth supplying the exact smooth-pair hypotheses; arbitrary regular pairs over arbitrary bases are a different assertion.', ['SA12_SGA4III','SA12_Riou2014'])
add(160,'Extension to normal-crossing divisors',
 ['33/14:415; SA12-612; CL-SA12-621'],
 'Extend the purity discussion to divisors with normal crossings; no formula is supplied.',
 'For a strict normal-crossing divisor in a regular scheme and invertible n, compute R^qj_*Z/n from the degree-one Kummer classes of the local branches, as the corresponding exterior algebra.',
 'Riou XVI3.1.3 gives the single regular divisor calculation and3.1.4 the strict normal-crossing exterior-algebra statement. Both result statements were opened.',
 unknown,'Worth identifying whether the leaf intends strict or étale-local normal crossings and fixing the branch-permutation descent.', ['SA12_Riou2014'])
add(161,'Constructibility without properness',
 ['33/16:462;18:482;48:1258–1261; SA12-615; CL-SA12-625'],
 'Expect the constructibility theorem for nonproper finite-type maps, with prime-to-characteristic torsion qualifications; later duality is used to obtain some ordinary-image constructibility.',
 'For finite-type f:Y→X with X noetherian quasi-excellent, n invertible on X and F constructible Z/n, all R^qf_*F are constructible and vanish for q sufficiently large.',
 'ILO XIII1.1.1 is the exact opened modern finiteness theorem. It circulated in arXiv1207.3648 (16July2012) from the2006–2008 seminar and appeared in2014. SGA4 XIX gives a historically narrower resolution-dependent setting. The scan48 partial-range shortcut is false (CL-SA12-678), even though the separate modern finiteness theorem is true.',
 'SGA4 XIX’s introduction explicitly identifies reliance on resolution in the original argument; it does not explain every editorial decision on these leaves.',
 'Worth matching the finiteness assumptions to the draft and distinguishing the theorem from the failed partial-duality inference.', ['SA12_ILO2012','SA12_SGA4III'])
add(162,'Independence from a regular sequence and admissible base change',
 ['33/24:642–646; 26:690–704; SA12-610; CL-SA12-634,635,636'],
 'The product class is said to be independent of the chosen regular equations; base change, intersection products and varying n are listed as properties, without their proofs.',
 'The canonical regular-immersion Gysin class is independent of presentation, natural for Tor-independent base change, multiplicative for transversal composition/intersection, and compatible with invertible torsion coefficients.',
 'Riou XVI2.3.1–2.3.2 supplies the general construction and excess formula, including zero-excess compatibility. SGA4 XVIII gives the published local/global programme. This review checks the divisor-unit case, not a complete reconstruction of the independence theorem.',
 unknown,'Worth a tightly scoped comparison of normalizations and signs, especially before using the classes in the trace diagram.', ['SA12_Riou2014','SA12_SGA4III'])
add(163,'The point class generates top compact-support cohomology',
 ['33/28:773–777; 30:823–830; SA12-621; CL-SA12-639,640'],
 'A theorem to be proved will show that the rational-point class is a basis of top compact-support cohomology and independent of the point; the curve case is recalled as checked.',
 'For smooth geometrically connected pure-d-dimensional X over separably closed k, n invertible and x∈X(k), trace identifies H_c^{2d}(X,Z/n(d)) with Z/n and sends cl_x to1.',
 'SGA4 XVIII2.9–2.10 supplies the normalized trace and geometric-fibre criterion;3.2.5 yields Poincaré duality. The source’s rationality and geometric-connectedness qualifications are retained.',
 'The text itself identifies this as a consequence of the forthcoming theorem, not a separate permanent conjecture.',
 'Worth using as a normalization test for the construction and for any comparison with the curve notes.', ['SA12_SGA4III','SA12_Milne2013'])
add(164,'Existence and uniqueness of the normalized global trace',
 ['33/32:863–871; 34:890–908; SA12-618; CL-SA12-643,644'],
 'Construct the canonical trace for smooth compactifiable pure-dimensional morphisms, characterized by base change, composition, isomorphisms and the P¹ Kummer normalization.',
 'For such f:X→S of dimension d and n invertible, construct Tr_f:R^{2d}f!Z/n(d)→Z/n; geometric connectedness and nonemptiness of fibres give an isomorphism.',
 'SGA4 XVIII2.9 and2.10.1 are the exact opened construction and fibre criterion. Literal ordinary connectedness is insufficient, as the finite étale C/R example shows.',
 unknown,'Worth a proof-location and normalization audit; existence is established, while the source itself leaves the uniqueness argument unwritten.', ['SA12_SGA4III','SA12_Stacks03SH'])
add(165,'Re-express the local/global class compatibility in the derived category',
 ['33/36:923–959; 46:1192–1195; SA12-623,648; CL-SA12-645'],
 'The corrected support/trace diagram will be expressed more easily and completely with derived categories; global duality is introduced as a title only.',
 'For a regular immersion of smooth S-schemes, the fundamental-class Gysin map intertwines the smooth trace maps after the codimension shift and twist.',
 'SGA4 XVIII2–3 and Riou XVI2.5.13 give the published trace/Gysin comparison. The overwritten diagram’s individual arrows are not certified as transcribed; the derived formulation is a stated reconstruction.',
 'The source itself says the derived category will simplify the statement, providing an explicit editorial reason for deferral.',
 'Worth developing as a commentary diagram after checking the ink; it is an exact bridge between the local and global parts of the programme.', ['SA12_SGA4III','SA12_Riou2014'])
add(166,'Flat resolutions for derived inverse image',
 ['33/38:1004–1036; SA12-624; CL-SA12-646'],
 'Later notes will construct Lf* on D− using flat resolutions instead of projectives; finite Tor dimension is required for the stated boundedness extension.',
 'K-flat resolutions define unbounded derived inverse image; exact pullback and finite Tor dimension yield the stated restrictions to bounded categories.',
 'Stacks06YV §21.18 gives the modern construction. SGA4 XVII4 gives the classical derived formalism; the modern unbounded method is not attributed retrospectively to the leaf.',
 'The text explicitly explains the issue: useful projectives need not exist, and without finite Tor dimension D+ is not preserved.',
 'Worth locating the promised later construction; no new abstract existence theorem is needed.', ['SA12_Stacks06YV','SA12_SGA4III'])
add(167,'Realization of the allowed Coxeter diagrams',
 ['33/7:186–202; 15:425–441; 17:467–479; 21:541–570; 35:915–920; SA12-627,645; CL-SA12-652,654'],
 'After deriving diagram restrictions, show all remaining possibilities are realized by finite reflection groups; the later root-system pages are to provide these realizations.',
 'For the finite connected Coxeter types, construct positive-definite reflection representations; for crystallographic types use explicit reduced root systems.',
 'Coxeter1934 §9 and the classification tables predate this draft’s likely period; received1933, published1934. Bourbaki Lie IV–VI (1968) is the later standard reference. The exact n°391 typescript identity and date remain unproved.',
 'The source explicitly postpones realization until the classification candidates have been listed; this is exposition order.',
 'Worth connecting the nonconsecutive source pages in their original order and checking the omitted types, not treating the classical classification as an open problem.', ['SA12_Coxeter1934','SA12_Bourbaki1968'])
add(168,'Reducedness and irreducibility of the lattice shells',
 ['33/19:497–501; 27:738–751; 31:845–858; SA12-629; CL-SA12-656,661,664,665'],
 'The lattice-shell criterion produces roots; reducedness and irreducibility remain to be checked in the concrete cases.',
 'A finite spanning norm shell stable under the integral reflection formulas is reduced; irreducibility follows from the connectedness of the supplied simple-root diagram.',
 'The exact rational program enumerates the E6/E7/E8 roots, verifies reflection stability and the connected Gram matrices, and checks the supplied simple-root/weight data. Bourbaki1968 and SGA3 XXI provide the published classification framework.',
 'The deferral is a local verification instruction inside reused exposition, not evidence of an open research conjecture.',
 'Worth retaining as a reproducible certificate and as a way to detect numerical transcription errors.', ['SA12_Bourbaki1968','SA12_SGA3XXI'])
add(169,'Eight cases, nine types and the promised plates',
 ['33/15:425–441; 17:477–479; 21:541–570; SA12-645; CL-SA12-654'],
 'The editorial plan names nine types and platesII–X, then promises eight following numbered cases; ranks and exceptional identifications must be kept separate.',
 'Recover the source table of contents and determine whether low-rank coincidences or grouped families account for the count; do not equate a count of subdivisions with manuscript page count.',
 'Bourbaki’s1968 root-system chapters and the publisher’s chapter metadata are verified, but the exact source plates and n°391 draft were not recovered. Coxeter1934 gives a comparison classification, not this editorial numbering.',
 'No evidence beyond the fragment’s local editorial organization explains the count.',
 'Worth source collation; the apparent count mismatch does not by itself refute a classification.', ['SA12_Bourbaki1968','SA12_Coxeter1934'])
add(170,'Whether and where to define hyperalgebras and formal morphisms',
 ['33/9:237–257; SA12-636; CL-SA12-666'],
 'The reused Tribu n°62 editorial sheet says it is undecided whether to define hyperalgebras generally and assigns formal-coordinate morphisms to another chapter.',
 'This is a choice of exposition, not a conjecture that hyperalgebras exist. The antisymmetrized quadratic part of a formal group law defines its tangent Lie bracket under the usual hypotheses.',
 'Bourbaki Lie II–III has a1972 original publication, verified bibliographically. Wehler2017 supplies a primary authored formal-group account, but the exact Tribu n°62 source and missing earlier formulas are unidentified.',
 'The wording itself describes editorial placement and levels of calculation.',
 'Worth identifying the Tribu sheet and preserving the editorial nature of the question; not a new mathematical research direction.', ['SA12_Bourbaki1972','SA12_Wehler2017'])
add(171,'Formal-point sorites and the restricted final surjectivity',
 ['33/9:257–277; SA12-637; CL-SA12-667'],
 'One could add functor-of-points identities, square-zero tangent description and the sequence G(J)→G(A)→G(A/J); the final surjectivity is restricted to finite-dimensional G or open J. Add Proposition4(i),(ii).',
 'For a specified complete topological algebra and a formal affine space/group with the relevant coordinate lifting property, establish these identities and retain the stated finite-dimensional/open-ideal condition for lifting.',
 'Bourbaki Lie III is a verified bibliographic comparison; the unseen definitions of formal kernels and topological completed tensor products prevent an exact theorem identification. No unrestricted surjectivity is inferred from ordinary smoothness slogans.',
 'The passage is an editorial proposal to insert statements whose definitions and antecedent Proposition4 lie on absent source pages.',
 'Worth recovering the source context before attempting a theorem or counterexample.', ['SA12_Bourbaki1972'])
add(172,'The cancelled EGA implication without separation',
 ['33/47:1199–1204; SA12-642; CL-SA12-675'],
 'The whole crossed sheet says b⇒c without separation is unknown for arbitrary n, while the reverse fails even for n=1. Neither b nor c appears in the supplied leaves.',
 'First recover the exact preceding conditions and the meaning of separation in this filtration context; only then formulate or test the implication.',
 'EGA IV4 (1967), §19.6, is securely matched at bibliographic and heading level. Stacks061M/067M distinguish modern regularity conditions but cannot identify the missing b and c. The large primary PDF could not be opened; no exact result match is claimed.',
 'The antecedents are physically absent from the attached fragment. The cancellation is not proof of mathematical withdrawal or later resolution.',
 'Worth the highest-priority source recovery for this reused leaf; no mathematical verdict is justified before the antecedents are read.', ['SA12_EGAIV4','SA12_Stacks061M','SA12_Stacks067M'])
(O/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(P)} manually assessed problems; IDs {P[0]["id"]}–{P[-1]["id"]}.')
