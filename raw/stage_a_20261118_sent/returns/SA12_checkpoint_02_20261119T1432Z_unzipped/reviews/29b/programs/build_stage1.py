#!/usr/bin/env python3
"""Serialize manually adjudicated cote-29 notes. No automatic classifications."""
import json,csv,pathlib,datetime
root=pathlib.Path(__file__).resolve().parents[1]
root.mkdir(parents=True,exist_ok=True)
items=[]; note_map=[]
pro='MPL_29_095-140_transcription.tex'
def add(n,kind,scans,lines,words,statement,reconstruction,check,reason):
    parent=1 if n<=15 else 2 if n<=35 else 3 if n<=50 else 4
    ident=f'SA12-{204+n}'
    items.append(dict(id=ident,sources=[f'MPL_29_095-140#{parent}'],kind=kind,cote='29',scans=scans,lines=lines if ':' in lines else pro+':'+lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    note_map.append(dict(internal_note=f'N{n:03}',item_id=ident,parent_entry=f'MPL_29_095-140#{parent}'))

# Each following judgment was made after reading the note and the cited transcript.
add(1,'unproved claim',[96,98],'38–51; 72','classe fondamentale de self-intersection',
    'A tame fundamental-group extension attached to a formal neighborhood is related to the normal-bundle class; its inertia kernel is a quotient of the prime-to-characteristic Tate module. The displayed sequence also includes the preceding second-homotopy boundary.',
    'A modern extension classification must retain the action of the base fundamental group and the boundary from pi_2. Centrality requires trivial action; the displayed page does not justify suppressing either datum.',
    'agrees','N001 correctly separates the self-intersection class, inertia quotient, and higher-homotopy obstruction. The exact ambient formal-cover category remains to be specified.')
add(2,'idea of the earlier run',[96],'38–51','',
    'The earlier run tests an arithmetic centrality extrapolation using F_4((u))/F_2((t)), u^3=t: the unramified Frobenius acts by inversion on tame inertia C_3.',
    'This is an independently checkable example supplied by the earlier run, not a counterexample written by Grothendieck and not a refutation of a geometrically trivialized Tate-module statement.',
    'agrees','N002 labels the example as an external diagnostic; the source page does not itself assert arithmetic centrality.')
add(3,'unproved claim',[96],'49–51','extension triviale',
    'The source calls an extension trivial after a pi_2-vanishing discussion. Vanishing of pi_2 alone removes one boundary map but does not imply that a central extension splits.',
    'A nonzero H^2 class of Z^2 gives a Heisenberg extension despite pi_2 of a torus being zero. This diagnoses the omitted obstruction, without supplying a geometric counterexample satisfying every unspecified formal-neighborhood hypothesis.',
    'agrees','N003 appropriately requests the normal-bundle Chern class and exact meaning of trivial before reading a splitting theorem into the line.')
add(4,'reading question',[96,98],'49–51; 72','mu_n',
    'For a P^1 boundary with self-intersection degree d, the indicated inertia is modeled by coker(d:T^(p-prime)→T^(p-prime)). For nonzero d it is cyclic of order the prime-to-p part of |d|; for d=0 it remains the full Tate module.',
    'The degree interpretation and the zero-degree exception are mathematical reconstructions. Neither witness decides the exact subscript on the roots-of-unity symbol.',
    'agrees','N004 correctly warns that a finite mu_n description requires a nonzero degree and a prime-to-characteristic convention.')
add(5,'conjecture',[98],'74–94','pi_2',
    'The page asks for arithmetic higher-homotopy information for Spec Z with prescribed missing primes and tameness conditions, in analogy with the preceding geometric sequence.',
    'A particular pro-p K(pi,1) result for an enlarged set of primes does not compute the full tame homotopy group for an arbitrary original set. The coefficient prime and real-place convention must be stated separately.',
    'agrees','N005 is a genuine question, not a calculation completed on the leaf.')
add(6,'reading question',[98],'88–94','sans doute',
    'A negative assertion about the arithmetic tame fundamental group is uncertain: the Pro witness includes a possible fini while the Codex witness does not. The following abelianization expression is sensitive to treatment of the infinite place.',
    'No reading is selected. A nonabelian tame extension can test a universal abelian claim; an abelianization computation cannot by itself settle the whole group.',
    'agrees','N006 identifies a substantive negation/scope ambiguity. The Codex disagreement strengthens the need for scan collation.')
add(7,'unproved claim',[100],'122–153','On va prouver',
    'For a henselian pair (X,Z) in the stated connected-cover sense and a strict normal-crossing divisor whose relevant indices are invertible, the page proposes a semiglobal Abhyankar description with commuting branch inertia images.',
    'Commutation among branch factors does not imply centrality in the full arithmetic fundamental group. The cover hypotheses and topology are part of the statement.',
    'agrees','N007 retains the local-to-global steps left at the bottom of the page and does not turn them into a finished proof.')
add(8,'unproved claim',[101],'154–206','On veut prouver',
    'The extension class of a prescribed tame cover is to correspond under a coefficient identification to the tuple of Kummer classes c_1(O(D_i)) modulo n.',
    'The coefficient identification is an input in the Codex witness (On se donne) but appears as a conclusion in Pro (On a donc). This changes the logical strength and is unresolved without the scan.',
    'understates','N008 is right about the unfinished programme but the independent witness reveals an additional assumption/conclusion reading issue.')
add(9,'unpursued implication',[101,103],'154–241','schémas formels',
    'The notes suggest variants of the tame-extension construction for formal schemes and locally ringed topoi.',
    'A general theorem requires the chosen cover topology, purity or local Kummer input, and coefficient system. The page supplies a direction, not those hypotheses.',
    'agrees','N009 correctly treats the variants as a programme rather than an automatic theorem for all topoi.')
add(10,'withdrawn in the same text',[103],'218–241','',
    'The source deletes a commutation/product-coefficient formulation while retaining a subsequent cohomological expression. Normality of inertia subgroups alone does not restore commutation.',
    'The earlier run uses the two normal cyclic subgroups generated by i and j in Q_8 to isolate this logical failure. The reason for the authorial deletion is not documented.',
    'agrees','N010 recognizes the cancellation; it does not establish that the author intended the Q_8 objection.')
add(11,'withdrawn in the same text',[104],'242–264','automorphismes',
    'The cancelled leaf states: if F and G are automorphisms of a finite-dimensional vector space and FGF^{-1}=G^q for an integer q>1, then G is quasi-unipotent. A finite permutation of its nonzero eigenvalues proves the assertion.',
    'Both attached witnesses say automorphisms; the earlier context reading endomorphisms is not used. A written semidirect-product description with multiplication by q on Z cannot literally be an action by automorphisms for q>1.',
    'agrees','N011 correctly preserves invertibility and distinguishes mathematical validity from physical cancellation; the semidirect-product phrase adds a separate reading alarm.')
add(12,'unproved claim',[105],'269–284','exact à gauche',
    'On a simply connected pointed setting, the finite-abelian-coefficient functor M↦H^2(X,M) is asserted left exact and prorepresentable. The proposed general construction passes to a universal procover.',
    'Left exactness follows from H^1(X,C)=0 for the coefficient quotient C in a short exact sequence. Prorepresentability also needs the finite-category/size framework. Identification with a homotopy progroup needs a separate homotopy construction.',
    'agrees','N012 does not equate the cohomological representing proobject with an already constructed pi_2 without further input.')
add(13,'reading question',[117,119,120],'622–630; C29-06_transcription.tex:5–34','prolongement',
    'Inertia is attached to a chosen extension of a cover across a boundary. An equivariant extension map sends a stabilizer into the target stabilizer; normalizations give a canonical setting when the hypotheses apply.',
    'The source says normalization of the open cover where normalization of the compactified base in its function field appears intended. This is an alarm only. The additional Codex pages provide the previously missing functoriality argument.',
    'understates','N013 was written with less local coverage; scans119–120 are now directly available in C29-06.')
add(14,'unproved claim',[121,122,123],'C29-06_transcription.tex:39–100','det N = ±p^r',
    'The pullback multiplicity matrix N between normal-crossing branches induces the map on prime-to-p tame Tate lattices. In the square case it is invertible exactly when its determinant is a signed p-power (±1 in characteristic zero).',
    'The subsequent Remords refines subgroup conjugacy to homomorphisms after choices of étale paths and a trivialization of the Tate sheaf. This is a statement about the inertia lattices, not injectivity of an arbitrary whole G→H.',
    'understates','N014 called this outside-package context. C29-06 now supplies the actual determinant statement and its qualification.')
add(15,'withdrawn in the same text',[100],'108–112','',
    'An isolated cancelled pro-l image/finite-index observation precedes the semiglobal argument.',
    'The coefficient topology and full claim are not recoverable from this fragment. Cancellation is visible, but its mathematical cause is not.',
    'agrees','N015 appropriately declines to infer a theorem or a reason for withdrawal.')
add(16,'reading question',[124],'641–649','Groupes infinitésimaux',
    'The cover identifies a group-theoretic dossier; its subtitle differs between Pro and Codex readings.',
    'The title does not itself date every enclosed sheet or settle whether the subtitle describes schemes, sets, or reused leaves.',
    'agrees','N016 remains a documentary reading question; Codex supplies competing words, not an authoritative correction.')
add(17,'unproved claim',[125,126],'C29-06_transcription.tex:110–112; MPL_29_095-140_transcription.tex:650–680','réduit',
    'The Serre-letter framework uses a category of finite groups closed under products, equalizers and images, an exact fibre-like functor, admissible infinitesimal-by-étale groups, and reducedness for pointed rigidity.',
    'The category and exactness axioms on scan125 are directly present in Codex. Their omission from the Pro interval must not turn the later conclusions into statements about all finite flat S-groups.',
    'understates','N017 recognized a missing beginning; the current attachment now provides it.')
add(18,'unproved claim',[126],'650–680','semi-direct',
    'Over a perfect field, a finite group scheme has the canonical reduced étale subgroup and connected infinitesimal kernel, giving a semidirect product.',
    'The action can be nontrivial, so the reconstruction is G^0⋊G_red with the appropriate orientation, not a direct product. Imperfect fields require separate care.',
    'agrees','N018 correctly keeps the perfect-field and semidirect qualifications.')
add(19,'unproved claim',[126,127,128],'650–680; C29-07_transcription.tex:5–21','éléments minimaux',
    'Pointed torsor classes Z(G) are proposed as an exact functor of the structural group in the specified category; descending-chain minimality and uniqueness yield a prorepresenting system of quotient groups.',
    'The proof is now visible on scans127–128. Its closure hypotheses are essential; arbitrary finite flat group schemes over a variable base do not have flat equalizers.',
    'understates','N019 is mathematically apt but no longer needs to treat the prorepresentability continuation as external context.')
add(20,'conjecture',[128,129],'C29-07_transcription.tex:21; MPL_29_095-140_transcription.tex:684','je conjecture',
    'The letter hopes for homotopy exactness and good variation of a fundamental group including infinitesimal covers in proper smooth/separable families.',
    'Homotopy exactness for Nori groups requires additional conditions; a single profinite flat group scheme recovering all geometric fibres is a stronger hope, later explicitly reported refuted in SGA1 X2.5.',
    'agrees','N020 correctly treats this as a hope, but modern homotopy criteria and the stronger family claim must have different fate records.')
add(21,'conjecture',[129],'686','produit',
    'For proper connected schemes over an algebraically closed field, the proposed infinitesimal fundamental group should satisfy a Künneth formula.',
    'Modern Nori product theorems retain reducedness and rational/geometric base points; an étale theorem for one proper factor does not automatically give the finite-group-scheme version.',
    'agrees','N021 supports a product conjecture, conditional on the proposed construction, not a proof in the letter.')
add(22,'unpursued implication',[129],'688–690','lim A[n]',
    'For an abelian variety A the expected fundamental group scheme is lim_n A[n], with the multiplication transition maps, and its Cartier dual is the corresponding direct limit of torsion on the dual variety.',
    'The dual formula uses Cartier duality and the principal torsion-pairing formalism, not an arbitrary identification A≅A-dual. The page gives a conditional consequence of the hoped-for theory.',
    'agrees','N022 keeps the transition maps and duality distinct.')
add(23,'unpursued implication',[129,130],'690–694','Witt',
    'The letter anticipates module descriptions and a three-piece structure for the p-primary theory, compared with prime-to-p Tate modules, including variation in families.',
    'Classical Dieudonné theory supplies exact operator/module categories over perfect fields; it does not by itself establish the unspecified uniform relative theory on this leaf.',
    'agrees','N023 rightly asks for the operator ring and category before treating the expectation as a theorem.')
add(24,'title, date or page count',[125,130],'C29-06_transcription.tex:106–112; MPL_29_095-140_transcription.tex:696','Mon cher Serre',
    'The Codex opening identifies the addressee and a date read 18.(6|8).1959; the letter closes with relative calendar remarks.',
    'The ambiguous month must be collated with the published correspondence or scan. Relative calendar language alone is not an independent date for the package.',
    'understates','N024 could not see the opening. Its caution remains correct, but the new local witness materially narrows the documentary question.')
add(25,'unproved claim',[137],'824–829','unique',
    'An admissible finite flat group has at most one infinitesimal normal subgroup with finite étale quotient.',
    'Reducedness of the base is not needed for this uniqueness: the map from one infinitesimal kernel into the other étale quotient is the identity because the inverse identity locus is clopen and contains every geometric point. Apply in both directions.',
    'agrees','N025 correctly separates kernel uniqueness from the later reduced-base rigidity requirement.')
add(26,'withdrawn in the same text',[137],'829–832','fidèlement plat',
    'The source corrects the direction of base change/descent for admissibility: it is preserved by base change, and the property descends under faithful flatness using uniqueness of the kernel.',
    'This does not make every finite flat group admissible. Marginal reducedness restrictions are preserved as written.',
    'agrees','N026 tracks the correction instead of quoting the cancelled direction.')
add(27,'unproved claim',[138],'835–841','sections',
    'For admissible finite torsors over a connected reduced base, a pointed morphism is rigid: agreement at the marked geometric point forces agreement everywhere.',
    'An arbitrary S-scheme does not have this property: sections0 and t of A^1_S coincide at t=0. The torsor and étale/infinitesimal conditions are essential, as is reducedness for infinitesimal sections.',
    'agrees','N027 correctly blocks removal of the torsor hypotheses.')
add(28,'reading question',[138],'846–848','minimal',
    'Minimality is meant to exclude reduction of a pointed G-torsor to a proper subgroup, but the displayed subgroup and contracted-product notation is malformed in both the relevant note and transcription.',
    'The intended formula would use a G-prime torsor P-prime with G-prime a proper subgroup and P-prime×_{G-prime}G≅P. This is an explicit reconstruction, not a correction of the ink.',
    'agrees','N028 identifies notation that must be resolved before interpreting the proof.')
add(29,'reading question',[138,139],'846–876','',
    'The glyph naming the pointed torsor functor varies among 0,1 and a fraktur letter in the witnesses.',
    'The audit uses Z as a neutral editorial name and records the original readings; this does not choose the ink.',
    'agrees','N029 is a genuine reading issue with limited mathematical impact once the functor is explicitly defined.')
add(30,'unproved claim',[139,140,141,142],'854–879; K29-09_transcription.tex:21–68','injectif',
    'The minimality argument claims injectivity Hom(G,G-prime)→Z(G-prime). It forms the equalizer H and a reduction R, asserting that R is an H-torsor.',
    'Existence of a scheme-theoretic fibre product is insufficient. H must remain in the chosen finite flat category and the reduction must be a torsor. Scan142 explicitly notices loss of reducedness after the torsor base change; its final appeal to uniqueness must therefore be read in its exact categorical setting.',
    'agrees','N030 identifies the substantive obligation. The continuation sharpens it rather than erasing it.')
add(31,'unproved claim',[140,141,142,143],'877–879; K29-09_transcription.tex:21–87','stable par produits ... par noyaux ... par images',
    'The restarted argument explicitly restricts to a category C of finite flat admissible S-groups closed under products, equalizers and images, then proposes a strict prorepresenting group.',
    'This category restriction is direct transcription evidence. It does not assert that the category of every finite flat S-group has the required closure properties.',
    'understates','N031 treated scans141–143 as unavailable context; the attachment contains them and their essential hypotheses.')
add(32,'idea of the earlier run',[139,141],'854–879; K29-09_transcription.tex:21–45','',
    'Over S=Spec k[t] in characteristic p, the equalizer of0 and multiplication by t on alpha_p has algebra k[t,T]/(T^p,tT), with generic fibre length1 and special fibre lengthp.',
    'This is an earlier-run counterexample to unrestricted flat-equalizer closure, not a counterexample inside a category assumed closed under such equalizers.',
    'agrees','N032 is a valid hypothesis diagnostic; its scope must not exceed the category it actually tests.')
add(33,'idea of the earlier run',[139,141,142],'854–879; K29-09_transcription.tex:21–68','',
    'On the cusp A=k[x,y]/(y^p−x^{p+1}), the pointed alpha_p torsor z^p=x is minimal among finite flat reductions, but distinct S-group maps0 and[x] give the same trivial pointed pushforward. The coincidence reduction is the nonflat normalization.',
    'All groups here vary over S; multiplication by x is not a constant k-group morphism. Thus the example refutes an unrestricted variable-base formulation, while it does not refute the constant-field category used in the Serre letter.',
    'agrees','N033 is retained with its precise domain and a separate algebraic verification.')
add(34,'other',[125,129],'C29-06_transcription.tex:106–112; MPL_29_095-140_transcription.tex:684–690','',
    'The finite-group-scheme programme is historically related in subject matter to Nori fundamental groups.',
    'Similarity of constructions does not establish priority, transmission, or influence. The dated Serre letter and opened later publications provide chronology only to the extent explicitly documented.',
    'agrees','N034 is a useful historiographic warning, not a mathematical priority claim.')
add(35,'idea of the earlier run',[126,129,139],'650–690; 854–879','',
    'The earlier notes link this group-scheme discussion to LM1 E11, LM1 E2 and MPL11 N063/N100 in their context packets.',
    'Those project sources are absent. The links are retained only as attributed leads in the separate our-projects table and are not used as mathematical evidence.',
    'agrees','N035 properly quarantines the external project context.')
add(36,'reading question',[108],'426–473','A+B=R',
    'The Chinese remainder passage uses comaximality to obtain intersection=product and the usual product decomposition. It does not assert the converse.',
    'The earlier context reading of a converse is false: (x)∩(y)=(xy) in k[x,y], but (x)+(y) is proper. The counterexample checks the earlier reading, not the valid source implication.',
    'agrees','N036 distinguishes the source CRT argument from an unsupported converse in prior context.')
add(37,'unproved claim',[110],'494–522','A connexe',
    'For connected A, comaximal ideals J,J-prime of A[T] whose product is generated by a monic P are asserted to have unique monic generators giving P=QQ-prime.',
    'Connectedness makes the ranks of the finite projective factors constant; characteristic polynomials of T then supply the generators. Over A=k×k, factor degrees can vary and no global monic generator need exist.',
    'agrees','N037 correctly retains the inserted connectedness hypothesis; omitting it produces a different and false statement.')
add(38,'self-flagged step',[110,111],'522–618','c’est vrai sur les',
    'The proof of existence of the monic factorization stops mid-sentence; the next retained page contains completion diagrams, not a completed proof.',
    'The connected-ring proof supplied in this audit is independent and explicitly labeled; it is not a recovered continuation.',
    'agrees','N038 accurately identifies the unfinished argument.')
add(39,'reading question',[133],'768–791','corps algébriquement clos',
    'The representability criterion tests invariance under extensions between algebraically closed fields, not arbitrary separable extensions of arbitrary fields.',
    'Spec C over R has no R-point but two C-geometric choices in the finite étale example; that diagnoses the stronger context reading, not the actual algebraically closed-field condition.',
    'agrees','N039 preserves the quantifier visible on the page.')
add(40,'unproved claim',[133],'768–791','conditions',
    'A functor is proposed to be represented by a separated quasi-finite étale object from limit compatibility, descent/localization, complete-local rigidity, separation and finite geometric fibres with algebraically closed extension invariance.',
    'The exact domain and all compatibility conditions matter. The leaf gives a criterion and beginnings of a construction, not a complete argument; later representability criteria must be compared clause by clause.',
    'agrees','N040 appropriately leaves the sufficiency proof as an obligation.')
add(41,'unproved claim',[135],'792–815','voisinages',
    'Local étale models over local schemes are to glue when they extend to neighborhoods with compatible identifications; the inserted neighborhood data are substantive.',
    'Without that data, compatible local schemes on A^1 can have image consisting only of the generic point and one closed point, which is not open and so cannot be the image of an étale morphism. This is a counterexample to the stripped formulation.',
    'agrees','N041 correctly refuses to omit the neighborhood extension condition.')
add(42,'unproved claim',[131],'699–716','F_G',
    'For a proper flat morphism with universally trivial direct image of O and a section, the page studies the relative functor of pointed finite étale G-torsors, with G fixed.',
    'This varies the base, unlike Z(G), which varies the structural group. The aside read Cas fini by Pro is Cas général in Codex; finite fibres and representability require a separate exact theorem.',
    'agrees','N042 correctly separates the two functors and records an unresolved scope word.')
add(43,'other',[95,97,99],'2–28; 52–68; 95–105','groupes diagonalisables',
    'Reused typescript states diagonalizable-group duality and kernels/cokernels, finite-presentation of the character Hom functor when H is finite type, n-torsion, and the graded-algebra description of torsors.',
    'These are identifiable with SGA3 VIII3.2–3.5 and §4. Modern editorial additions must not be attributed to the manuscript witness.',
    'agrees','N043 correctly identifies a published-text strand rather than a new conjectural development.')
add(44,'other',[109],'474–493','Ad majorem',
    'A humorous Bourbaki-related letter or text mentions Grothendieck as departed; it is documentary material interleaved with mathematics.',
    'The supplied leaf does not securely identify the writer or date. Its allusions cannot date surrounding mathematical leaves.',
    'agrees','N044 appropriately limits attribution and chronology.')
add(45,'other',[132,134,136],'752–767; C29-07_transcription.tex:26–79','rationality',
    'English sheets discuss fields of definition of linear subspaces, Plücker coordinates, graphs, and rationality of multilinear maps. The continuation order is I4 (136), I5 (134), I6 (132).',
    'The author is unidentified. The graph equation on scan136 changes a needed minus to plus in equation3; the preimage statement on132 also needs its function argument checked. These are scan alarms, not emendations.',
    'understates','N045 identifies the strand; the Codex pages permit direct checks and expose an additional sign issue.')
add(46,'other',[106],'319–356','17.4.10; 17.5.1',
    'Reused EGA IV typescript contains the fibrewise unramified criterion under local finite-presentation assumptions, and the local equivalences defining smoothness, including flatness plus geometric smoothness of fibres.',
    'The warning on the word lisse and the exact assumptions on both morphisms are retained. The cropped page does not contain the entire proof of every equivalence.',
    'agrees','N046 correctly treats this as a specific EGA passage with a partial proof window.')
add(47,'title, date or page count',[111,112,118],'523–640','Ramification',
    'The remaining pages include completion diagrams, a title, and a cancelled isolated formula, with no securely recoverable independent theorem.',
    'A diagram is not promoted to a claim merely because symbols resemble a known theorem.',
    'agrees','N047 appropriately records sparse documentary material.')
add(48,'reading question',[135],'792–815','',
    'The earlier context quote Je ne suis pas sûr is not supported by either attached witness at this place.',
    'Pro and Codex offer different positive connective phrases; neither justifies an authorial confession of doubt. The scan should settle the actual wording.',
    'agrees','N048 correctly rejects the unsupported quote without choosing a replacement.')
add(49,'other',[45,131],'699–716; K29-01_transcription.tex (scan45)','',
    'The earlier notes connect finiteness in the relative torsor functor to the finite-presentation discussion on cote29scan45.',
    'The connection is thematic until both exact categories and quantifiers are compared. The earlier scan is assigned to the cote29early audit.',
    'agrees','N049 is retained as a cross-folder comparison, not an automatic deduction.')
add(50,'other',[71,131],'699–716; MPL_29_049-094_transcription.tex (scan71)','',
    'Universal triviality of the direct image of O in the torsor discussion is compared with the Picard/family hypotheses on scan71.',
    'The two uses must be checked separately; neither implies representability of the other functor without its additional assumptions.',
    'agrees','N050 is a legitimate cross-reference lead whose exact source ends are recorded by the two reviewers.')
add(51,'reading question',[107],'387–417','pi_1(Z)=Z-hat^2',
    'A diagram labels Z as the spectrum of a complete local ring while assigning it a rank-two profinite fundamental group.',
    'For Z=Spec C[[x,y]], the ordinary étale fundamental group is trivial. A boundary complement or tame punctured neighborhood can have the displayed rank-two group, but that is a different object and may only be intended, not written.',
    'agrees','N051 correctly flags an object-level ambiguity rather than silently changing Z.')
add(52,'idea of the earlier run',[101,103,121],'154–241; C29-06_transcription.tex:39–53','',
    'A divisor root stack and a line-bundle root gerbe encode different stabilizer patterns: on A^1 with divisor0, the former has mu_n inertia only at0, while the latter has it everywhere.',
    'This is a modern interpretive comparison introduced by the earlier run. It cannot replace the cover category in the source without proof.',
    'agrees','N052 is retained as a carefully bounded comparison, not attributed to the manuscript.')
add(53,'idea of the earlier run',[101,125,126],'154–206; C29-06_transcription.tex:110–112; MPL_29_095-140_transcription.tex:650–680','',
    'The Kummer sequence with mu_n is exact in the fppf topology for any positive n; it is exact in the étale topology when n is invertible on the base.',
    'The distinction explains why finite flat group schemes are necessary in characteristic p. It is background used to compare two manuscript strands, not an assertion that their full constructions coincide.',
    'agrees','N053 states the topology change accurately.')
add(54,'idea of the earlier run',[105,181,182],'269–284; K29-11_transcription.tex (scans181–182)','',
    'The H^2 prorepresentability programme is compared in the earlier context with FINMON and S2COUNT models.',
    'Those models and results are absent. Their finite categories and second-homotopy constructions cannot be identified with the manuscript proabelian coefficient functor from names alone.',
    'agrees','N054 remains solely in the quarantined project-links table.')
add(55,'idea of the earlier run',[125,126,139,141],'C29-06_transcription.tex:110–112; MPL_29_095-140_transcription.tex:650–680,854–879; K29-09_transcription.tex:21–45','',
    'The restriction from arbitrary variable-base finite flat groups to a suitable field-defined category is related to modern obstructions in relative fundamental group schemes.',
    'The comparison uses the exact nonflat-equalizer example and opened relative-group literature. It does not claim that every modern relative existence question is settled.',
    'agrees','N055 has a sound local obstruction but deliberately limited global implications.')
add(56,'idea of the earlier run',[126,137,138],'650–680; 816–849','',
    'Over dual numbers k[epsilon]/epsilon^2 in characteristic p, the trivial alpha_p torsor has distinct sections0 and epsilon and a nonidentity pointed translation invisible at the geometric point.',
    'This verifies the role of reducedness in rigidity, while infinitesimal-kernel uniqueness from N025 remains valid without reducedness.',
    'agrees','N056 correctly separates two statements whose hypotheses differ.')

aggregates=[]
groups=[(1,1,15,'Tame inertia, Kummer classes, monodromy and second homotopy'),(2,16,35,'Infinitesimal groups, pointed torsors and minimality'),(3,36,50,'Local algebra, representability, gluing and documentary strands'),(4,51,56,'Further comparisons and hypothesis checks')]
for parent,lo,hi,title in groups:
    subset=items[lo-1:hi]
    aggregates.append(dict(id=f'SA12-{200+parent}',sources=[f'MPL_29_095-140#{parent}'],kind='other',cote='29',scans=sorted({s for i in subset for s in i['scans']}),lines='See individual N%03d–N%03d items and internal_note_map.tsv'%(lo,hi),his_words='',statement=f'Editorial umbrella entry: {title}. The source index counts this ### heading as one entry, while its #### notes N{lo:03}–N{hi:03} are individually adjudicated in SA12-{204+lo}–SA12-{204+hi}.',reconstruction='This is a concordance object, not an authorial mathematical assertion. Source-ID multiplicity is deliberate; no synthetic index verdict rows are added.',check='understates',check_reason='The umbrella must be atomized to preserve the different hypotheses, documentary readings, earlier-run ideas and Codex continuations. See the individual judgments.'))
allitems=aggregates+items
(root/'items.json').write_text(json.dumps(allitems,ensure_ascii=False,indent=2)+'\n')
with (root/'entries.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader()
    reasons=[
      'Corrected aggregate: retains N001–N015 separately; scans119–123 now supply direct inertia/determinant evidence, and Pro/Codex disagree on the coefficient-identification premise. No centrality or splitting is inferred without its hypotheses.',
      'Corrected aggregate: retains N016–N035 separately; Codex supplies the Serre-letter opening and scans141–143 restart. Variable-base counterexamples are not attributed to the restricted constant-field category.',
      'Corrected aggregate: retains N036–N050 separately; source CRT/connectedness hypotheses are preserved, Codex adds English-sheet evidence, and unsupported authorial doubt/date claims are removed.',
      'Corrected aggregate: retains N051–N056 separately; modern root-stack/Kummer comparisons and project leads are labeled earlier-run ideas, with the full-spectrum/punctured-spectrum ambiguity left for the scans.'
    ]
    for k,reason in enumerate(reasons,1):w.writerow(dict(entry_id=f'MPL_29_095-140#{k}',item_id=f'SA12-{200+k}',verdict='corrected',reason=reason))
with (root/'internal_note_map.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['internal_note','item_id','parent_entry'],delimiter='\t');w.writeheader();w.writerows(note_map)
out={'items':len(allitems),'index_verdicts':4,'internal_notes_checked':56,'written_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'stage1_summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
