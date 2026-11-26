"""Manual claim records, authored after full source reading; not a keyword classifier."""

claim(601,[('A57-01',[3])],quote('A57-01',13,21),
'Let A be a complete noetherian local ring and f:X→Spec A a proper resolution, isomorphic over U=Spec A minus its closed point, with X regular and U schematically dense. Cartier divisors supported on X minus U give D→Pic(X)→Pic(U)→0; proper formal existence identifies Pic(X) with the compatible system of Pic(X_n). Only codimension-one exceptional components generate D; the blanket identification with every component of X_0 needs this qualification.',
'proof sketched','A','The divisor localization sequence is standard; formal existence is Grothendieck’s EGA III. The local-Picard application is developed explicitly by Lipman and Boutot. The two steps do not alone produce a representable quotient.',
['R_Lipman1976','R_Kollar2014','R_EGAIII1'],[3,15],
computation='Divisor restriction: extend a Cartier divisor from regular U by its codimension-one closure in regular X; its ambiguity is a divisor supported on X minus U. Formal existence applies to invertible sheaves and their inverses. See research/root_proofs.md §1.',
ref_locators={'R_Kollar2014':'§24, resolution and local Picard comparison','R_EGAIII1':'§5.1, existence theorem'})

claim(602,[('A57-01',[4,5,6])],quote('A57-01',81),
'For a non-separably-closed residue field, the exceptional divisor lattice is an étale Galois module obtained from the geometric exceptional components. Taking rational points of D→P→Q produces an H¹(k,im D) obstruction; replacing Pic(X_n) by its sheafified Picard functor adds a Brauer obstruction. Thus Q(k)=Pic(U) is not automatic. The text corrects the constant lattice to a twisted one.',
'corrected by himself later','B','Modern local Picard representability and Lipman’s exact sequence preserve the distinction between rational points of a Picard sheaf and actual line bundles. The source’s correction is essential; torsion-free constant lattices have H¹=0, whereas arbitrary twisted lattices need not.',
['R_Lipman1976','R_Kollar2014','R_Kleiman2005'],[3,15,24],
computation='The fppf long exact sequence for 0→D′→P→Q→0 gives the connecting obstruction. For constant torsion-free D′, continuous maps from a profinite Galois group have finite image and hence vanish. This argument does not apply to arbitrary Galois action. research/root_proofs.md §1.',
ref_locators={'R_Lipman1976':'Theorem 7.5','R_Kleiman2005':'Theorem 2.5 and comparison discussion'})

claim(603,[('A57-01',[6,7,8])],quote('A57-01',90),
'If a resolution admits an invertible ideal J defining the exceptional fibre set-theoretically and with ample conormal L=J/J² on Z, then the transition Pic(Z_{n+1})→Pic(Z_n) is eventually an isomorphism: H¹(Z,L^{n+1}) and H²(Z,L^{n+1}) vanish for large n. Hence its formal Picard pro-object stabilizes. The existence of such a J/model is a separate question in the source.',
'proof sketched','C','The vanishing implication follows from the square-zero units sequence and Serre vanishing. Lipman’s surface theory and the general local-Picard framework supply established cases, but the blanket assertion that every chosen resolution has this positive exceptional model was not identified in the searched sources.',
['R_Lipman1976','R_Kollar2014','R_Boutot1978'],[3,15],
computation='For I=J^{n+1}/J^{n+2}, the sequence 1→1+I→O*_{Z_{n+1}}→O*_{Z_n}→1 has 1+I≅I additively. Its H¹ and H² control kernel and obstruction. Eventual vanishing proves stabilization; it does not prove existence of J.',confidence='medium',
present='The conditional stabilization statement is established; the exact unrestricted model-existence assertion remains unverified in this bounded search.')

claim(604,[('A57-01',[7,8])],quote('A57-01',94,100),
'The map from exceptional divisors to NS of the special fibre is asserted to be injective, so that the divisor lattice embeds discretely and Pic(X)/D exists with the same connected component and Lie algebra. For normal surface singularities, negative definiteness of the exceptional intersection matrix proves the required injectivity. Higher dimensions require a negativity argument with precise projectivity hypotheses.',
'open on the pages','C','The normal surface case is classical and appears in the local-Picard literature. Kollár’s resolution description supports the quotient construction in his stated geometric setup. The exact generality of the handwritten expectation, especially without a projective birational model, was not established by the opened results.',
['R_Kollar2014','R_Lipman1975','R_Boutot1978'],[3,15],
computation='If a divisor vector d maps to zero in NS, its intersections with all exceptional curves vanish. A negative definite matrix has zero kernel, so d=0. This proves only the surface case described here.',confidence='medium')

claim(605,[('A57-01',[8,9,10,11])],quote('A57-01',122,127),
'Under the stabilized-resolution construction, Lie(Q)=H¹(X,O_X) injects into H¹(U,O_U)=H²_m(A). Vanishing of this local cohomology, for example depth A≥3, makes Q discrete. An intrinsic functor on all k-algebras, independence of resolution, and behavior under non-geometrically-regular scalar extension are separately left open; a chosen coefficient field is part of the construction.',
'open on the pages','B','Boutot and subsequent local-Picard theory give an intrinsic functor in specified noetherian geometric settings. Kollár’s Condition 3 requires S₂, pure dimension at least3 and essential finite type over a field, and explicitly invokes Boutot’s representability theorem. These hypotheses cannot be discarded to claim representability for every complete local ring in the manuscript.',
['R_Boutot1978','R_Kollar2014'],[3,15],
computation='The filtration of j_*O_U/O_X by L^{-n} gives the asserted H¹ injection when H⁰(Z,L^{-n})=0 for n≥1. Negative powers of an ample sheaf need the positive-dimensional-support assumptions; the statement is not justified for an arbitrary exceptional zero-dimensional component.',confidence='medium',
ref_locators={'R_Kollar2014':'Condition3, Theorem6, §24–25','R_Boutot1978':'chapters II and V; book metadata verified, exact theorem used through Kollár’s quotation'})

claim(606,[('A57-01',[11,12])],quote('A57-01',172,178),
'For A an artinian local ring with perfect residue field k and X proper over A, seek a locally algebraic group over k representing the appropriate Picard functor formed through Witt-vector/Greenberg base change, including mixed characteristic; actual Pic(X) must be compared with its k-points through the descent obstruction.',
'open on the pages','B','Lipman’s 1976 paper explicitly identifies Grothendieck’s September1969 letter as the problem it answers. Definition1.1, Theorem1.2 and §5 construct the locally algebraic Picard group and reconcile the fpqc/fppf formulations; Theorem7.5 controls rational points. This is a precise later match, not merely a similar topic.',
['R_Lipman1976'],[15],fate_date='Grothendieck letter: September1969, stated by Lipman; paper received15December1973, published28December1976.',
ref_locators={'R_Lipman1976':'Introduction; Definition1.1; Theorem1.2; §5; Theorem7.5'})

claim(607,[('K57-01',[15,17,18,19])],quote('K57-01',10,17),
'For line bundles on the products to which the cube theorem applies, the n-variable pullback is expressed by the base term to exponent (n−1)(n−2)/2, singleton terms to exponent2−n, and unordered pair terms to exponent1. The same cube identity yields [n]*L = L^{n(n+1)/2}⊗([-1]*L)^{n(n−1)/2}. Pair indices must be i<j; writing i≠j counts twice.',
'proof sketched','B','The cube and square theorems form the established Picard/abelian-variety formalism. Milne proves the cube theorem and its multiplication corollaries with properness hypotheses, and Murre treats the correspondence application. These are the exact opened publication endpoints; no exact own-author publication is asserted for this formula. The algebraic exponents have been independently recomputed here. ClassB is a publication-fate label, not a first-discovery attribution.',
['R_Milne2008','R_Murre1966'],[4,24,26],
computation='scripts/root_computations.py: cube_recurrence, cube_small_exponents, multiplication_binomial; saved outputs/root_computations.json. Inductive coefficient identity and n=1,2,3 checks agree after unordered-pair correction.',
ref_locators={'R_Milne2008':'§I.5, Theorem of the Cube and consequences','R_Murre1966':'§3(C), Corr and the cube theorem'})

claim(608,[('K57-01',[15,17,19,25,27])],quote('K57-01',38,44),
'For proper flat families with universally O_S as global functions and chosen basepoints, normalized line bundles on X×_S Y define correspondences; the product Picard functor splits into the factors and a normalized correspondence functor. Its infinitesimal rigidity uses H¹(O_{X×Y})=H¹(O_X)⊕H¹(O_Y), with the axes removing those two summands. Representability and base-change hypotheses must be kept.',
'proof sketched','B','Murre’s exposition of Grothendieck’s unramified-functor theory treats the correspondence functor and cube theorem explicitly. The checked publication is Murre’s; attribution to Grothendieck of the reported theory is preserved. The special abelian case is the familiar Hom(A,B∨) description. No assertion about arbitrary nonproper products is inferred.',
['R_Murre1966','R_Milne2008'],[4,24,26],
computation='The square-zero deformation class lies in H¹(O_X×Y)⊗I; its two restrictions are its Künneth components, so vanishing on both axes kills it. Higher-order uniqueness follows by successive square-zero extensions. research/root_proofs.md §2.',
ref_locators={'R_Murre1966':'§3(C), pp257–259, Corr functor'})

claim(609,[('K57-01',[25,27,29,31,33]),('K57-02',[35,37,39,41])],quote('K57-02',200,206),
'A smooth proper pointed family over a connected locally noetherian base, with an abelian fibre, is expected to carry a unique abelian-scheme law. The pages prove uniqueness via rigidity, sketch the infinitesimal extension of multiplication, and explicitly leave the DVR closedness step to be developed. The opened published theorem is stated for a projective family; its proper analogue needs the corresponding algebraic-space extension theorem.',
'proof sketched','C','The projective version is Mumford’s GIT Theorem6.14; Genestier–Ngô Theorem2.4.1 gives this statement and Proposition2.4.2/Lemma2.4.3 isolate the infinitesimal and DVR steps. These are exact matches for those steps. The broader proper scheme version was searched but is not certified here solely from the projective statement.',
['R_GIT1994','R_GenestierNgo'],[10,11,13],confidence='medium',
computation='For the first-order product deformation, H¹ of the product splits by Künneth, and the prescribed restrictions to the two identity axes determine both components; the H⁰ ambiguity is removed by the unit condition. This does not replace the DVR existence argument.',
ref_locators={'R_GenestierNgo':'Theorem2.4.1; Proposition2.4.2; Lemma2.4.3'})

claim(610,[('K57-02',[43,44])],quote('K57-02',268),
'The proposed characterization of torsion-dense smooth commutative groups by absence of additive factors is withdrawn: a nontrivial extension of an abelian variety by G_a in characteristic zero can still have Zariski-dense prime-to-characteristic torsion. For a nonzero vector-extension class by a one-dimensional vector group, the extension is anti-affine.',
'corrected by himself later','B','Brion’s classification of anti-affine groups supplies the later structural framework and includes characteristic-zero universal vector extensions. The source’s “no additive factor” necessity is explicitly rejected on the next sheet, not a surviving conjecture.',
['R_Brion2009'],[10,11],
computation='For 0→G_a→G→A→0 in char0, [n] is an isomorphism on G_a and G[n]→A[n] is an isomorphism. If the closure of all torsion were proper, its connected quotient would be an additive quotient of an anti-affine group, impossible because every regular map to an affine scheme is constant. research/root_proofs.md §3.',
fate_date='arXiv first27October2007; revised25June2008; journal publication2009.')

claim(611,[('K57-02',[44,45])],quote('K57-02',274,280),
'For a commutative flat group scheme of finite presentation, multiplication by n invertible on the base is étale; without flatness its n-torsion is unramified under the stated finite-type conditions. The transcription’s possible “non comm.” cannot be retained: the nth-power map of a noncommutative group need not be unramified.',
'false as stated','A','The commutative statement is part of SGA3 and FGA236 Theorem2.5. If the ambiguous word really says noncommutative, GL₂ in characteristic zero supplies a counterexample: the involution diag(1,−1) has a positive-dimensional conjugacy class of square roots of1. The ink remains undecided.',
['R_SGA3XI','R_FGA236'],[8,23],
computation='scripts/root_computations.py: noncommutative_power_counterexample. The conjugates [[1,−2u],[0,−1]] all square to I over k[u]; n=2 is invertible and GL₂ is smooth separated finite type. Thus every remaining hypothesis holds.',status_reason='Conditional refutation of the “noncommutative” reading; the commutative reading is correct.')

claim(612,[('K57-02',[45,46,47,48,49])],quote('K57-02',300,306),
'Finite étale closed subgroup schemes in a separated unramified group over a connected locally noetherian base that agree on one fibre agree everywhere; closed embeddings or the historical separated scheme convention are essential. For smooth commutative separated groups with finite étale prime-power torsion that is schematically dense, equality of rigid subgroups and of homomorphisms is detected on one fibre. Effective descent then holds for a faithfully flat finite-type cover with geometrically connected fibres, subject to the displayed rigidity hypotheses.',
'proof sketched','A','SGA3 XI §6 gives the finite-level transporter and density mechanism with precise finiteness/flatness hypotheses. The primary-field-extension corollary is only sketched on the pages: spreading out a merely asserted rigid subgroup is not automatic from finite presentation.',
['R_SGA3XI'],[8,9,20],
computation='Equality of finite étale closed subgroups is open and closed in the connected base, using the open unramified diagonal and its closedness from separation. A nonseparated étale double-origin trait has distinct sections agreeing generically, so separation cannot be omitted. Equality at all torsion levels plus schematic density forces equality of closed subgroups. Descent compares the two pullbacks on S′×_S S′ under the source’s connected-fibre hypotheses.',
ref_locators={'R_SGA3XI':'Proposition6.1; Theorem6.2; Remark6.3'},present='The finite-level rigidity theorem is established. The manuscript’s full primary-extension spreading assertion is retained as a qualified open step, not silently supplied by this proof.')

claim(613,[('K57-03',[50,51,52])],quote('K57-03',1,8),
'The claim that a homomorphism from a rigid group has universally open kernel is withdrawn after a degeneration of a graph of a finite constant group. A fibrewise dimension argument does not prove flatness or openness of a kernel. Likewise topological surjectivity of a morphism of group schemes is weaker than faithful flatness.',
'corrected by himself later','B','The checked SGA3 chapters by Gabriel and Bertin carefully separate smooth, flat, unramified and schematic-image statements. These are later established developments by other authors, not an exact own-author publication identified here. The pages supply their own correction, so the discarded assertion is not credited as a theorem. The map Spec k→α_p is topologically surjective but not flat and confirms the latter distinction.',
['R_SGA3VIA','R_SGA3VIB'],[8,26,27],
computation='For R=k[t]/(t^p), k=R/(t) is not flat: tensoring the injection (t^{p−1})→R with k kills it while the source tensor remains nonzero. Both schemes have one topological point. research/root_proofs.md §3.')

claim(614,[('K57-03',[51,52,53,54,55,56,57,58])],quote('K57-03',28,36),
'“Very rigid” groups are studied through rigidity of their closed subgroups, dense prime-to-characteristic torsion and descent over primary extensions. Any formulation quantifying over all closed subgroup schemes must restrict the subgroup to be smooth if that is part of the rigidity definition: μ_p⊂G_m is a closed nonsmooth subgroup in characteristic p. The abelian and multiplicative-type smooth cases support the intended arguments.',
'open on the pages','C','SGA3 XI §6 establishes the density/transporters needed in controlled cases; Brion classifies anti-affine examples outside a simplistic no-additive-factor criterion. The exact new adjective and every unrestricted primary-descent assertion were not found as a theorem with identical hypotheses.',
['R_SGA3XI','R_Brion2009'],[8,10,20],confidence='medium',
computation='μ_p=Spec k[t]/(t^p−1) has a nonzero nilpotent t−1 over characteristic p, so is not smooth. This is a hypothesis audit, not a refutation of a version restricted to smooth subgroup schemes.')

claim(615,[('K57-03',[60,61,62,63]),('K59-02',[21,23])],quote('K57-03',279,283),
'For proper flat finitely presented X/S, cohomologically flat in degree0 with geometric H⁰=k, a family B⊂Pic^τ_{X/S} of maximal abelian subvarieties yields an Albanese torsor under B∨, universal for maps to abelian torsors and compatible with base change. The field case uses the maximal abelian subgroup, not the Chevalley abelian quotient of Pic⁰. Existence in arbitrary families is separately questioned.',
'open on the pages','B','Laurent–Schröer Theorem10.2 gives this precise criterion and construction; Theorem7.2 handles maximal abelian subvarieties under arbitrary field extension; Corollary10.5 gives the proper-field case with H⁰=k. The criterion explains why degeneration to nonproper Picard identity components prevents a blanket relative assertion.',
['R_LaurentSchroer2024','R_Kleiman2005'],[13,15],
fate_date='Paper received27June2023; published online20December2023; journal volume55(2024), article4. Earlier circulation not established.',
ref_locators={'R_LaurentSchroer2024':'Theorem7.2; Theorem10.2; Corollary10.5'})

claim(616,[('K57-03',[64])],quote('K57-03',407,415),
'Smooth fibres alone do not make a relative Picard scheme smooth over a nonreduced base. In characteristic zero, for smooth projective X/S the identity component Pic⁰ is smooth even for nonreduced S; the full Picard scheme can still have jumping components that are not flat. Vanishing H²(O_{X_s}) gives a separate sufficient criterion for smoothness near s.',
'open on the pages','B','Deligne’s Theorem5.5 proves cohomological local freeness and base change for smooth proper characteristic-zero families. Kleiman Remark5.21 applies it to Pic⁰, while Example5.22 exhibits the failure for the full Picard scheme, and Proposition5.19 proves the H² criterion. FGA236 Theorem3.5 also has a normal-fibre smoothness statement without reduced-base hypothesis.',
['R_Deligne1968','R_Kleiman2005','R_FGA236'],[23,24,25,26,28],
computation='The infinitesimal obstruction to extending a line bundle lies in H²(O)⊗I; its vanishing suffices. Constancy of h¹ in characteristic zero controls the identity component, not extension of every Néron–Severi class.',
ref_locators={'R_Deligne1968':'Theorem5.5, printedp123','R_Kleiman2005':'Proposition5.19; Remark5.21; Example5.22'})

claim(617,[('K57-04',[68,69])],quote('K57-04',84,90),
'For a smooth projective surface and ample H, Riemann–Roch proves h⁰(D)>0 if χ(O(D))>0 and H·(D−K)>0, since H⁰(K−D)=0. The nonstrict inequality transcribed on the page is insufficient. Applying the strict version to nH+Δ for n≫0 yields boundedness arguments for numerically trivial Δ.',
'false as stated','E','The surface Riemann–Roch/Matsusaka argument predates this working note; the precise nonstrict threshold is refuted here. FGA236’s addendum and SGA6 XIII establish the numerical/τ and finiteness conclusions with correct hypotheses.',
['R_FGA236Addendum','R_SGA6','R_Kleiman2005'],[23,24,27,28],
computation='scripts/root_computations.py: matsusaka_threshold_counterexample. X=P², H=O(1), D=K=−3H has H·(D−K)=0 and χ(O(D))=1 but h⁰(O(D))=0. The strict inequality excludes exactly the failed Serre-duality step.')

claim(618,[('K57-04',[68,69,70,71,72]),('A57-02',[73,74,75,76,77,78,79])],quote('K57-04',188,192),
'For a proper scheme over a field, numerical triviality of a line bundle equals τ-triviality; the geometric Néron–Severi group is finitely generated. In a proper finite-type family over a noetherian quasi-compact base, geometric NS ranks and torsion orders are uniformly bounded. Proper-surjective pullback, ample divisor restriction with fibre components dimension≥3, and [n] for n≠0 have the finiteness properties specified in the FGA addendum.',
'stated without proof','A','The FGA236 addendum(i),(ii),(iv)–(viii) states the exact finiteness and numerical assertions that the main exposé had left pending. SGA6 XII–XIII develops their proofs. The dating of the addendum must be distinguished from the May1962 original exposé and the18July1962 Murre letter.',
['R_FGA236Addendum','R_SGA6'],[23,27,28],
computation='No numerical shortcut replaces the finite-type theorem. The finite-curve degree criterion and τ equivalence are matched assertion-by-assertion to addendum(vii)–(viii).',
ref_locators={'R_FGA236Addendum':'(i)–(viii), collectionpp303–306','R_SGA6':'XII §1 and XIII §§3–5'})

claim(619,[('K57-04',[70])],quote('K57-04',153,163),
'For a smooth projective surface over an algebraically closed field and ℓ different from the characteristic, b₁=b₃=2 dim(Pic⁰_red), b₀=b₄=1, and b₂=c₂−2+4 dim(Pic⁰_red). The transcription omits the factor2 in the odd Betti numbers and consequently in the Euler-characteristic formula. The NS rank is bounded by b₂.',
'false as stated','B','The Picard–Igusa bound is part of the finiteness theory cited in FGA’s addendum. The omitted factors are detected independently on an abelian surface, without needing a disputed source attribution. This is a mathematical reading alarm, not an ink emendation.',
['R_FGA236Addendum','R_Milne2008','R_SGA6'],[4,23,38],
computation='scripts/root_computations.py: abelian_surface_betti. For a complex abelian surface, dimPic⁰=2 and Betti numbers(1,4,6,4,1), Euler characteristic0; the transcribed formula gives b₂=2 instead of6. SGA6 XIII Remark5.3, printedp652, explicitly has b₂=c₂−2+2b₁ and b₁=2dimPic, confirming the factor correction in a primary source.')

claim(620,[('A57-02',[73,74,75,76,77,78,79]),('K57-08',[133,135])],quote('A57-02',23,29),
'A proper surjective morphism X′→X over a field induces an affine morphism Pic_X→Pic_{X′}; over an integral noetherian base it is generically representable by quasi-affine morphisms of finite type. The direction is contravariant. Affineness over a field and generic relative quasi-affineness are distinct assertions; finite type alone is weaker than either.',
'open on the pages','A','Grothendieck’s conjecture in FGA232 Remark6.6 is proved in SGA6 XII, Raynaud written by Kleiman: Theorem1.1 gives generic relative representability and Corollary1.5 gives affineness over a field. The correspondence with the Murre letter is confirmed by Kleiman’s historical account, not inferred from a title.',
['R_SGA6','R_Kleiman2005','R_FGA236Addendum'],[24,26,27,28],
computation='Stein factorization and descent motivate the page’s proof sketch. The page135 arrow must be checked against pullback Pic(X)→Pic(X′); an arbitrary monomorphism of locally finite type groups is not automatically a closed immersion.',
ref_locators={'R_SGA6':'XII Theorem1.1; Corollaries1.2 and1.5','R_Kleiman2005':'Theorems4.18.2–5 and surrounding historical discussion'})

claim(621,[('A57-02',[74,75,77,78,79])],quote('A57-02',67,73),
'For proper X→S with S locally noetherian and coherent F, the functor of base changes on which F becomes flat is represented by an unramified S-scheme locally of finite type. This is universal flattening, not merely a stratification whose members separately make F flat. The requested extension beyond the projective case is real and necessary.',
'open on the pages','B','Murre’s May1965 Bourbaki exposé294, according to unpublished Grothendieck results, §3(A) Theorem2 and Corollary1 settles the proper case. ClassB records the checked publication under Murre’s authorship, while preserving its express attribution to Grothendieck. Stacks Lemma38.27.6 gives the current finite-presentation formulation. Without properness or purity, universal flattening can fail.',
['R_Murre1966','R_StacksFlattening'],[15,24,25,26,27],fate_date='TalkMay1965; collected-volume publication1966; no earlier circulation date independently established.',
ref_locators={'R_Murre1966':'§3(A), Theorem2 and Corollary1, collectionp253','R_StacksFlattening':'Tag05PS, Lemma38.27.6; tag052F, Example38.21.2'})

claim(622,[('K57-04',[86])],quote('K57-04',316,325),
'The associated-torsor sketch compares Hom sets for quotient G-sets and associated bundles but does not specify enough hypotheses for a universal full-faithfulness theorem. For a connected Galois finite étale torsor and constant finite group G, the usual equivalence with finite G-sets gives Hom_G(G/H,G/K)=(G/K)^H, equivalently cosets satisfying H⊂gKg^{-1}.',
'stated without proof','F','Searches through the opened SGA/functor references found the standard finite-étale interpretation, but the isolated source diagram does not identify its intended category. The restricted formula is our reconstruction, not a claim that the full source has been proved.',
['R_SGA3VIA','R_Murre1966'],[24,26,27],confidence='low',
computation='An equivariant map is determined by the image of H; that image gK must be fixed by every h∈H, exactly when g^{-1}Hg⊂K. No categorical equivalence is asserted outside the stated finite Galois setting.')

claim(623,[('K57-05',[180,181,182,183]),('K57-10',[164])],quote('K57-05',78,84),
'An effective relative Cartier divisor is an invertible sheaf with a section that is a nonzerodivisor on each fibre, modulo multiplication by units. For proper flat X/S with universally f_*O_X=O_S and a cohomologically controlled sheaf L, the fibre of Div→Pic is the appropriate open part of the projectivized section module; for geometrically integral fibres every nonzero section is regular. Projective-bundle, local-freeness and base-change assertions require their separate hypotheses.',
'proof sketched','A','FGA’s divisor/Picard construction is developed in Kleiman §3, especially Theorem3.13 and Exercise3.14. The pages’ diagram of implications is valid in this controlled setting; it is not an unconditional assertion that every Div fibre is a projective bundle.',
['R_Kleiman2005','R_FGA232'],[4,24,26],
computation='The exact sequence0→O_X→L→N_D→0 yields the tangent sequence and the quotient of sections by units. The normal-sheaf obstruction is addressed separately in C-SA14-647.',ref_locators={'R_Kleiman2005':'Theorem3.13; Exercise3.14; Remark5.18'})

claim(624,[('K57-05',[185,186,187,188])],quote('K57-05',164,173),
'For the normal affine cone over a smooth projective variety X with an ample embedding L and the usual section-ring hypotheses, the local Picard group at the vertex is Pic(X)/Z[L]. The blowup/line-bundle model and excision of the zero section give the quotient. Normality, generation and the distinction between the whole punctured cone and the punctured local spectrum are essential.',
'proof sketched','B','Kollár §25 gives the standard cone computation and compares local and completed local Picard groups. EGA II §8.7–8.8 gives the actual cone/contraction hypotheses; the manuscript’s norm argument supplies its own local-global comparison rather than making every graded ring a cone of this form.',
['R_Kollar2014','R_EGAII'],[3,15,29],
computation='On the total space of L^{-1}, homotopy invariance for the regular base identifies Pic with Pic(X). Removing the zero section quotients by its Cartier class L, up to inverse convention. The localized-cone step additionally uses the model hypotheses.',
ref_locators={'R_Kollar2014':'Example25, cones','R_EGAII':'8.7.5;8.8.3–8.8.6'})

claim(625,[('K57-05',[189,190,191,192]),('K57-06',[193])],quote('K57-05',250,257),
'For a cone over a smooth projective curve C with polarization L, formal neighbourhoods of the exceptional curve have successive Picard kernels H¹(C,L^n), n≥1, because H²(C,L^n)=0. Over characteristic zero these give the unipotent correction to completion. For a smooth plane curve of degree d, the sum of these dimensions is binomial(d−1,3) for d≥4. The source’s d≥6 inequality is a sufficient example of failure of invariance, not the first possible degree.',
'proof sketched','B','The modern cone formulas in Kollár Example25 make the distinction between local and completed tangent spaces explicit. The finite positive-twist correction and the component quotient by the degree of L explain the curve case. Claims in higher dimension or positive characteristic need separate obstruction and group-structure analysis.',
['R_Kollar2014','R_Boutot1978','R_Elkik1973'],[3,15],
computation='scripts/root_computations.py: plane_cone_completion_layers. By Serre duality h¹(C,O_C(n))=h⁰(C,O_C(d−3−n)); for1≤n≤d−3 these equal binomial(d−1−n,2), summing to binomial(d−1,3). Quartics already give1; d<g−1 holds first at d=6.',confidence='high')

claim(626,[('K57-06',[194])],quote('K57-06',24,34),
'For a noetherian henselian pair(A,J), restriction from U=Spec A minus V(J) to the corresponding puncture of the J-adic completion induces a bijection on Picard groups. This is an isomorphism on isomorphism classes, not automatically an equivalence of categories with all Hom groups preserved.',
'open on the pages','B','Elkik III.1 Theorem3 and the corollary on pp573–574 establish the vector-bundle/Picard comparison. No isolated-singularity condition is required in the cited corollary. This answers the source’s henselization hope with the noetherian henselian-pair hypotheses.',
['R_Elkik1973'],[7,15],fate_date='Published1973; an earlier circulation date was not established.',ref_locators={'R_Elkik1973':'III.1 Theorem3, p569; corollariespp573–574'},
computation='Hypothesis comparison only: no computation is used. In particular this does not assert preservation of units, which would be needed for full faithfulness of the line-bundle groupoid.')

claim(627,[('K57-06',[196,198])],quote('K57-06',88,96),
'For a projective commutative group scheme with equal-dimensional fibres, the pages study the reduced identity abelian varieties and the finite quotient length σ. They propose flatness/constant-σ criteria for these fibrewise abelian varieties to form a subgroup scheme, and a tentative torsion-rank test with n divisible by σ². The sufficiency argument uses a reduced base and a Hilbert/valuative construction; those restrictions cannot be suppressed.',
'open on the pages','C','SGA3 develops relative identity components and finite subgroup schemes; Laurent–Schröer gives a precise modern criterion for families of maximal abelian subvarieties. Neither opened source was found to state the exact σ² rank test in the manuscript’s generality. The structural program is developed, but that numerical test remains unverified rather than declared solved.',
['R_SGA3VIB','R_LaurentSchroer2024'],[8,13,15,26,27],confidence='medium',
computation='The source’s diagram has unresolved labels and no universal rank formula can be recomputed faithfully without choosing them. The finite quotient length and reduced-base conditions are retained; numerical testing is not presented as a proof.',present='Established structural theory exists; the exact σ² criterion is not identified from the opened literature and is an ink/formulation task.')

claim(628,[('K57-06',[201,202,203,204])],quote('K57-06',288,295),
'For a group scheme locally of finite type over a field, G⁰ is an open normal subgroup of finite type and is geometrically irreducible; its component quotient is étale. Open subgroups are closed. Smoothness over a field is equivalent to geometric reducedness in this group setting; ordinary reducedness over an imperfect field is not sufficient.',
'proof sketched','B','SGA3 VIA Proposition2.3.1 and Proposition2.4, in Gabriel’s authored chapter, state the connected-component results over an artinian local base; the field assertions are their special case. This is credited to the later established treatment by another author. The edition explicitly corrects the geometric-irreducibility wording to refer to the residue-field fibre. General-base existence needs the separate hypotheses of VIB.',
['R_SGA3VIA','R_SGA3VIB'],[8,26,27],
computation='Translations carry a nonempty open subset of the identity component through the component; a quasi-compact open generating neighbourhood shows finite type. The source’s U² argument must use the irreducibility lemma first, not assume the desired conclusion.',ref_locators={'R_SGA3VIA':'2.3.1;2.4;2.4.1;§3 quotients'})

claim(629,[('K57-06',[203,204,205,206])],quote('K57-06',359,366),
'For a commutative locally algebraic group G over a field, its torsion-component subgroup is the inverse image of the torsion subgroup of π₀(G). Its union over exponent n is filtered by divisibility. If that locus is quasi-compact, only finitely many components occur and their torsion exponent is bounded. Tests involving a subgroup H require H to be of finite type; H=G otherwise makes such a test vacuous.',
'proof sketched','A','The component formalism and Pic^τ finiteness are established in SGA3 and FGA236’s addendum. This does not validate the literal criterion that one a^n be closed, which is vacuous on a discrete étale component scheme; that wording remains a reading alarm.',
['R_SGA3VIA','R_FGA236Addendum'],[23,26,27],
computation='A quasi-compact space mapping to a discrete étale component space has finite image. A finite set of torsion elements in an abelian group has a common annihilator, their least common multiple. This proves the bounded-exponent conclusion and explains the divisibility indexing.')

claim(630,[('K57-06',[208,209])],quote('K57-06',450,457),
'A separated, locally finite-type, open morphism over a locally noetherian base whose fibres are proper is of finite type. The page deletes the stronger word universally. Its argument spreads a proper generic fibre to a proper finite-type open piece, uses separation to make that piece closed in the ambient family, then uses openness and noetherian induction. It does not drop separation or openness.',
'proof sketched','A','This belongs to EGA’s fibrewise properness and openness criteria. Kleiman’s application cites EGA IV3 15.7.11. The source’s finite-type step can also be checked directly by the stated induction; the stronger conclusion of properness should only be attached with the full EGA hypotheses.',
['R_EGAIV3','R_Kleiman2005'],[25,27],
computation='Independent proof check in research/root_proofs.md §4: choose a quasi-compact open containing each generic fibre, shrink the base so it is proper, then its complement is open with open image missing the generic points. After shrinking it is empty; induct on the closed remainder.',confidence='medium')

claim(631,[('K57-07',[210,211,212])],quote('K57-07',3,10),
'The locus of components whose class is prime-to-residue-characteristic torsion is studied through [n], Kummer cohomology and constructibility. Under the page’s proper/controlled identity-component hypotheses it is quasi-compact or closed in the indicated circumstances. The argument with n invertible cannot by itself control p-primary components in characteristic p.',
'proof sketched','A','FGA236 distinguishes the prime-to-characteristic loci in its local properties; the addendum later gives full Pic^τ finiteness for proper schemes. SGA6 XIII develops the latter theorem. These later conclusions have stronger Picard-specific inputs than the isolated prime-to-p group argument.',
['R_FGA236','R_FGA236Addendum','R_SGA6'],[23,24,27,28],
computation='Kummer exactness0→μ_n→G_m→G_m holds étale-locally only for n invertible; the restriction is retained at every use. No extrapolation to p-torsion is made.')

claim(632,[('K57-07',[214,215,216,217,219])],quote('K57-07',88,96),
'For X⊂P²_{k[t]} given by xy−tz²=0, the total space is regular and flat. Its generic fibre is P¹ and its special fibre is two lines. Divisor classes have a special bidegree(p,q) and generic degree p+q; a vertical component has bidegree(−1,1), the other(1,−1). The opposite self-intersection sign transcribed later is inconsistent with their sum being a fibre.',
'proof sketched','A','The explicit family is a standard model for nonseparated relative Picard functors, as in FGA’s examples and subsequent Picard theory. The computations are independently redone here, and the conclusion is separated from the source’s withdrawn nonrepresentability claim.',
['R_FGA236','R_Kleiman2005'],[23,24,26],
computation='scripts/root_computations.py: conic_regular_chart and conic_vertical_intersections. On z≠0, t=xy gives a smooth affine plane; the other projective charts are regular. The components meet transversely once, (D₁+D₂)·D_i=0, hence D_i²=−1 and D₁D₂=1.')

claim(633,[('K57-07',[214,217,218,219])],quote('K57-07',156,164),
'The conic example’s Picard functor is ultimately described as a scheme with infinitely many origins in each fixed total-degree component. A proposed nonrepresentability conclusion is deleted on217 and the abandoned argument on218 is cancelled. Nonseparatedness survives; nonrepresentability does not survive in this example.',
'corrected by himself later','A','FGA/Picard theory includes nonseparated representable Picard schemes and also different examples representable only by algebraic spaces. The latter must not be substituted for this withdrawn argument. The final gluing by equal generic degrees is consistent with the bidegree calculation.',
['R_FGA236','R_Kleiman2005'],[23,24,26],
computation='Each special bidegree(p,d−p) defines one origin over t=0; away from0 they represent the same degree-d generic class and are glued. Two such origins cannot be separated, but this is a scheme obtained by gluing open copies of the base.',status_reason='Both the deleted “pas” and the cancelled intermediate argument are kept in the provenance; the final scan219 is the surviving conclusion.')

claim(634,[('K57-07',[220,221])],quote('K57-07',173,180),
'For a projective cone with the normality and section-ring hypotheses of the cone construction, Pic of the cone is generated by the hyperplane class in the absolute geometric situation. A relative formulation must retain classes pulled back from the base. The quadric degeneration has geometric/split generic Picard rank2 and singular cone Picard rank1; characteristic2 or a nonsplit quadric requires a separate statement.',
'stated without proof','B','EGA II8.8.3–8.8.6 supplies the contraction structure; standard cone/Picard calculations are recorded by Kollár. The rank-drop example is established under the stated split characteristic≠2 assumptions. The literal unqualified relative Pic=Z formulation is not accepted.',
['R_EGAII','R_Kollar2014'],[3,15,29],
computation='The exceptional divisor is contracted, so a line bundle descending from the resolution must have trivial restriction along the exceptional fibres; this leaves the hyperplane generator in the geometric projective cone. Base pullback gives an immediate omitted summand when Pic(S)≠0.',confidence='medium')

claim(635,[('K57-07',[222,224])],quote('K57-07',192,203),
'The family of plane cubics xy(x+y+τz)=0 is flat over k[τ], including the concurrent triple-line fibre at τ=0. The proposed closed-cover Čech complex of the three structure sheaves does not generally compute O_X cohomology. At the concurrent fibre its naive complex has H¹=0, while H¹(O_X)=k for every plane cubic.',
'false as stated','E','The defect is the use of a closed cover as if it were an acyclic open cover. The plane-hypersurface exact sequence gives an independent counterexample under the displayed family’s hypotheses. Standard sheaf cohomology, rather than a later unproved conjecture, resolves the issue.',
['R_EGAIII1','R_Kleiman2005'],[24,29],
computation='scripts/root_computations.py: triple_lines_flatness, triple_line_cech_failure, plane_cubic_hilbert_polynomial. In0→O_P²(−3)→O_P²→O_X→0, H¹(O_X)=H²(O_P²(−3))=k. The naive k³→k³→k complex has kernel dimension2 and image dimension2 in degree1. Flatness over k[τ] follows because the cubic has coefficient1 on x²y, hence is primitive and its quotient has no base torsion; over a field every fibre is a cubic hypersurface.')

claim(636,[('K57-07',[223,225])],quote('K57-07',226,234),
'The reused printed text develops associated bundles (“fûts”), transitivity and functoriality for group actions. These are ancillary printed assertions, not newly proposed Picard theorems; their exact volume/edition and the intended class of bundles cannot be identified from the supplied fragments alone.',
'proved there','F','The general associated-bundle construction is standard and compatible with the quotient formalism of SGA3. Bibliographic searches did not identify the exact printed Bourbaki leaf. It remains an unidentified reused-source claim, with no new Grothendieck authorship or date assigned.',
['R_SGA3VIA'],[26,27],confidence='low',
computation='For a principal G-bundle P and G-set F, the contracted product P×^G F is compatible with equivariant maps F→F′; associativity of quotient relations proves transitivity in the usual setting. That reconstruction is not an identification of the missing printed source.')

claim(637,[('K57-08',[134])],quote('K57-08',60,69),
'For the Koszul cochain complex on f₁,…,f_r, multiplication by each f_i is null-homotopic. The direct-limit Koszul construction depends only on the radical/adic topology of the generated ideal; a unit ideal gives an acyclic augmented complex. The particular wedge/contraction signs must be consistent.',
'proof sketched','A','This is the Koszul/local-cohomology formalism developed in SGA2 and EGA. The source’s displayed homotopy is checked directly in exterior algebra, including all basis elements for three generators.',
['R_SGA2'],[3,15],
computation='scripts/root_computations.py: koszul_homotopy,24 symbolic identities. With d=Σ f_j e_j∧ and h_i=contraction by e_i, d h_i+h_i d=f_i id. IfΣa_i f_i=1, Σa_i h_i contracts the complex. Cofinal systems of powers justify radical invariance.')

claim(638,[('K57-08',[136])],quote('K57-08',110,119),
'The reused depth/Cohen–Macaulay/flatness lemmas must distinguish a Cohen–Macaulay finite module from a maximal Cohen–Macaulay module. Over a regular local ring, finite maximal Cohen–Macaulay modules are free; arbitrary Cohen–Macaulay modules need not be. Faithfully flat completion detects flatness of finite modules, with the noetherian hypotheses retained.',
'false as stated','E','These are standard commutative-algebra statements, not an original Picard claim. The missing maximality qualification is detected by a one-dimensional regular-local counterexample. The completed-flatness implication is preserved separately.',
['R_EGAIV4','R_EGAI'],[23,27,29],
computation='scripts/root_computations.py: CM_not_maximal_CM records the proof. For R=k[[t]], M=k is Cohen–Macaulay of dimension0 but is killed by t and hence not a nonzero free R-module. In the maximal case depth M=dim R and Auslander–Buchsbaum gives projective dimension0.')

claim(639,[('K57-08',[138,140]),('K57-10',[173,174,175,176,177,178,179])],quote('K57-10',205,212),
'For proper flat X/S with universal f_*O_X=O_S, the relative Picard functor is the fppf sheafification of T↦Pic(X_T)/Pic(T). A section g permits normalization L⊗f* (g*L)^{-1}, kills the Brauer obstruction and produces a rigidified description. Without a section, relative classes need not be represented by global line bundles. PicS→PicX→Pic_{X/S}(S)→H²(S,G_m) is the relevant low-degree exact sequence.',
'proof sketched','A','FGA’s descent construction and Kleiman’s Comparison Theorem2.5 establish this distinction. It is invalid to identify the raw absolute Picard group with the sheaf of relative classes, or to omit the inverse in normalization. A Brauer–Severi family supplies the standard obstruction to a universal Poincaré bundle.',
['R_FGA232','R_Kleiman2005'],[4,24,26],
computation='Pulling back L⊗f*(g*L)^{-1} along g gives the trivial bundle. In contrast L⊗f*g*L pulls back to(g*L)^2 and fails generally. The Leray low-degree sequence gives the obstruction term. research/root_proofs.md §5.')

claim(640,[('K57-08',[142,144,145])],quote('K57-08',238,246),
'Let X/S be a smooth proper geometrically connected curve and Y⊂X a finite étale divisor meeting every geometric fibre; set U=X\u2216Y and let E be the generalized Jacobian with torus Res_{Y/S}G_m/G_m. For n invertible on S, R¹f_!μ_n identifies with E[n] and R²f_!μ_n with Z/n, in the indicated relative convention. Nonempty punctures and invertibility of n are necessary.',
'proof sketched','B','The relative Kummer sequence and generalized Jacobian construction are established; Mazza–Voevodsky–Weibel §7 Proposition7.13 and Exercise7.14 give the relative-Picard calculation over a field. The relative family statement additionally uses proper/smooth base change and fibrewise comparison, with the source’s hypotheses retained.',
['R_MVW2006','R_HarariSzamuely2009'],[16,17,20],
computation='The torus has rank deg(Y/S)−1 geometrically; E[n] consequently has rank n^{2g+r−1}, agreeing with H¹_c(U,μ_n). The top class has rank1, and H⁰_c vanishes because every connected fibre has a puncture. See root_proofs.md §6.',confidence='medium')

claim(641,[('K57-08',[142,144,145])],quote('K57-08',300,310),
'The low-degree compact-support Leray transgression defines ξ_n∈H²(S,E[n]); the page asks whether it equals the Kummer boundary of the degree-one Picard torsor of the curve with Y pinched. The equality, including its sign, is a question on the pages, not a completed calculation.',
'open on the pages','C','Harari–Szamuely Proposition2.2 identifies the fundamental-group extension class with the ℓ-adic boundary of the Albanese torsor over a field. Petrov–Skorobogatov2026 Theorem5.1 identifies the low Postnikov class for a torsor under a semiabelian variety with its Kummer boundary. These closely match the mechanism, but do not alone prove the exact relative compact-support/pinched-curve identity over arbitrary S.',
['R_HarariSzamuely2009','R_PetrovSkorobogatov2026'],[17,18,20],
computation='A torsor cocycle a_στ and local n-division lifts produce the2-cocycle σb_τ−b_στ+b_σ; this is the Kummer boundary. To identify the manuscript ξ_n one must compare the compact-support complex and its sign conventions, a step not supplied by a cohomological rank calculation.',
fate_date='Harari–Szamuely first arXiv circulation2008, journal2009; Petrov–Skorobogatov online6August2026, journal volume25(2026).',confidence='medium')

claim(642,[('K57-08',[147,149]),('K57-09',[151,155])],quote('K57-09',61,70),
'For a proper reduced connected curve over an algebraically closed field, with c normalized components, local δ-invariants δ_p and branch counts r_p, the affine kernel of Pic⁰(C)→∏Pic⁰(C_i) has dimension Σδ_p−c+1. Its torus rank is Σ(r_p−1)−c+1 and its unipotent dimension Σ(δ_p−r_p+1). Pic⁰ is abelian exactly when the curve is seminormal and its incidence graph is a tree (compact type in the nodal case).',
'corrected by himself later','B','The normalization exact sequence and generalized Jacobian theory give these formulas. The manuscript repairs an earlier graph count by retaining branches; a literal lower bound δ≥2 would wrongly exclude an ordinary node, which hasδ=1 and2branches.',
['R_MVW2006','R_FGA236','R_Kleiman2005'],[16,23,24],
computation='scripts/root_computations.py: normalization_picard_dimensions. The quotient of local unit groups contributes torus dimension r_p−1 and additive dimensionδ_p−r_p+1; quotienting the c component constants by the diagonal removes c−1 torus dimensions. Examples checked: smooth curve, irreducible node, cusp, two components with one or two nodes.')

claim(643,[('K57-08',[148]),('K57-09',[150,152,156])],quote('K57-09',4,11),
'The interleaved English printed text proves projectivity of a compact analytic surface with two algebraically independent meromorphic functions, by resolving a meromorphic map and comparing the leading coefficient in a Riemann–Roch/Hilbert polynomial to force degree1. Its text matches Kodaira’s1960 article, §3 Theorem3.1 and proof; the exact physical edition of the reused leaf remains unidentified. It is not a new Picard conjecture.',
'proved there','E','The primary Collected Works III witness identifies article52 as On compact complex analytic surfaces I, Annals71(1960)111–152, received30June1959. Its Theorem3.1 removes the Kähler restriction of Chow–Kodaira1952 using Riemann–Roch for compact analytic surfaces. Publication and receipt dates do not date Grothendieck’s handwriting on the reused sheet.',
['R_ChowKodaira1952','R_Kodaira1960','R_KodairaCollected'],[23,25,26,28,36,38,39,41,42],
computation='If a generically finite map has degree e, the leading quadratic term of sections pulled from a high power is multiplied by e. Equality with the target leading term forces e=1; the analytic-to-algebraic and contraction steps require the theorem’s surface hypotheses.',confidence='medium')

claim(644,[('K57-09',[153,155])],quote('K57-09',112,121),
'For a connected stable nodal graph with vertex genera g_i, e edges, v vertices and valencesν_i, g=Σg_i+e−v+1 and the corresponding moduli stratum dimension is Σ(3g_i−3+ν_i)=3g−3−e. Unstable rational/elliptic components need their automorphism corrections. A sum over g_i≥1 plus a separate elliptic contribution double counts genus1 vertices.',
'proof sketched','B','Stable-curve deformation theory establishes this stratum dimension. Knudsen–Mumford’s moduli program is a later published framework, but the ambiguous F_i corrections and drawings on the source sheets are not treated as an identified general theorem.',
['R_KnudsenMumford1976','R_Kleiman2005'],[6,18,21],
computation='scripts/root_computations.py: stable_graph_moduli_dimension; substituteΣν_i=2e and arithmetic genus to obtain3g−3−e. The equality holds for stable graphs; it is not asserted for the unspecified unstable diagrams.',confidence='medium')

claim(645,[('K57-09',[154,159,161,163])],quote('K57-09',163,170),
'The reused EGA I leaves cover fibre-counting and local spreading(6.4.12,6.5.1), formal spectra, completed localizations and topologically finite-type algebras. Their standard printed statements are ancillary EGA claims. The handwritten proposed generators in the completed-localization argument require retaining both coefficient generators and the original algebra generators; products alone need not generate.',
'proof sketched','A','The original EGA I PDF was downloaded and compared at the printed locators. The standard topology and completed-fraction assertions are published; the suggested shortened generator proof is separately checked and cannot be justified by citing the printed statement alone.',
['R_EGAI'],[23,27,29],
computation='Take A=k[ε]/ε² and B=A[t]. The elementsεt and coefficient elements cannot generate t over A, since reducing moduloε gives only k. Thus replacing a full generator set by products c_i a_j is invalid if the intended list omits the a_j. This is a conditional reading alarm.',confidence='medium')

claim(646,[('K57-09',[158,160,162])],quote('K57-09',264,272),
'Assume universal f_*O_X=O_S and that f_*L is locally free of rank r and commutes with base change. Projective frames of f_*L form a PGL_r-torsor and, when L is relatively very ample, give complete-linear-system embeddings into P^{r−1}. The action on marked embeddings of a fixed X is free. Stabilizers of the unmarked Hilbert image are a different moduli problem and may contain automorphisms of X; Aut(X)=0 is not needed for freeness on the marked complete embeddings.',
'proof sketched','A','The Hilbert/Picard quotient construction is part of FGA and GIT. The source’s marginal automorphism condition and N versusN−1 labels mix the framed and unframed problems; those are recorded as reading/formulation alarms, not silently resolved.',
['R_FGA232','R_GIT1994','R_Kleiman2005'],[4,11,24,26],
computation='An element of PGL_r fixing a complete marked embedding pointwise acts as a scalar on the generating global sections, hence is the identity in PGL_r. Tensoring L by a base line bundle changes a vector frame but not the associated projective frame. Torsor base is S, not the embedded X.')

claim(647,[('K57-10',[164])],quote('K57-10',4,13),
'For an effective Cartier divisor D with L=O_X(D), the exact sequence0→O_X→L→N_D→0 gives tangent space H⁰(N_D) to Div and H¹(O_X) to Pic. The differential lies in the long exact sequence; H¹(L)=0 gives the relevant smoothness criterion for Div→Pic, while H¹(N_D)=0 removes divisor obstructions. The next cohomology group after H¹(N_D) is H²(O_X), not H¹(O_X).',
'proof sketched','A','FGA’s infinitesimal Picard theory and Kleiman Remark5.18 give these tangent/obstruction descriptions. The terminal subscript error is exposed directly by the long exact sequence.',
['R_FGA236','R_Kleiman2005'],[23,24],
computation='Write the long exact sequence through H⁰(L)→H⁰(N_D)→H¹(O_X)→H¹(L)→H¹(N_D)→H²(O_X). This independent derivation fixes the cohomological degree without deciding the handwritten glyph.',ref_locators={'R_Kleiman2005':'Theorem5.11; Remark5.18'})

claim(648,[('K57-10',[165,166,167])],quote('K57-10',47,56),
'The pages define schematic density, use it for uniqueness of maps to separated targets and for rational/pseudo-morphisms with maximal domains. For reduced schemes, ordinary dense open subsets are schematically dense. The speculation that the sheaf of pseudofunctions is quasi-coherent is cancelled; it is not a surviving theorem. The reused completion-of-modules paragraph is standard adic algebra.',
'corrected by himself later','A','EGA’s schematic-density and rational-map formalism provides the published framework. The cancelled quasi-coherence assertion is kept only as a withdrawn step, and no general equivalence between rational maps and global sections of a quasi-coherent sheaf is inferred.',
['R_EGAI','R_EGAIV4'],[23,27,29],
computation='Two morphisms to a separated target have closed equalizer; if their agreement locus is schematically dense, the equalizer ideal is zero. For a reduced scheme, a section vanishing on a dense open is zero on each irreducible component. These checks do not prove quasi-coherence of pseudofunctions.')

claim(649,[('K57-10',[169,170,171])],quote('K57-10',111,120),
'For a normal noetherian integral scheme, codimension-one valuations detect regular rational functions, and thus regularity of rational maps to affine targets. A rational map to a proper target extends at codimension-one DVR points, but it may still have codimension-two indeterminacy. R₁ alone does not provide the global function-extension conclusion; S₂ is essential.',
'false as stated','E','The normality/Krull-domain and valuative-criterion statements are standard. The page’s deletion of “affine”, if intentional, invalidates the polar-divisor conclusion. Its R₁ variant must be separated from the valid proper-target codimension-one extension assertion.',
['R_EGAI','R_EGAII','R_EGAIV4'],[23,27,29],
computation='[x:y]:P²⇢P¹ has only the codimension-two basepoint[0:0:1], so a proper target does not force divisorial indeterminacy. Separately R=k+(x,y)²⊂k[x,y] is finite type and R₁, but x is regular at every height-one point and x∉R; it fails S₂. scripts/root_computations.py: R1_without_S2_counterexample; proof in root_proofs.md §7.')

claim(650,[('K58-01',[3,5])],quote('K58-01',11,15),
'The transcribed Lemma2 asserts connectedness of a hypersurface section of a punctured complete noetherian local spectrum from lower bounds on component dimensions alone. A connectedness hypothesis on the original puncture is missing if those are the only assumptions. Completeness and dimension bounds alone do not connect different branches meeting only at the removed closed point.',
'false as stated','A','SGA2 XIII2.1 gives the connectedness-dimension theorem with an explicit connectedness assumption. The isolated lemma as transcribed is refuted by a complete fibre-product local ring. The manuscript’s possible reliance on a preceding lemma is documented, not silently inserted into its statement.',
['R_SGA2'],[3,29,33,34,35],
computation='Let A=k[[x₁,x₂,x₃]]×_k k[[y₁,y₂,y₃]], equivalently the complete local quotient by all x_i y_j. Its puncture is a disjoint union of two punctured3-spaces, each of dimension2. For f=(x₁,y₁), the punctured section is a disjoint union of two nonempty punctured2-spaces. Every displayed noetherian/completeness/component-dimension hypothesis holds; connectedness fails.',ref_locators={'R_SGA2':'XIII Theorem2.1 and proof'})

claim(651,[('K58-01',[5,7,9]),('K58-02',[11,13])],quote('K58-01',47,59),
'Let A be complete noetherian local, X=Spec A and X′ its puncture. If every component of X′ has dimension at least k+1 and X′ is connected in dimension at least k, then cutting by m≤k elements of the maximal ideal leaves every punctured component of dimension at least k−m+1 and connectedness in dimension at least k−m. In particular each such cut is connected. Finite avoidance and reduction to normality/S₂ occur in the proof, not as additional hypotheses of this final topological theorem.',
'proof sketched','A','The published SGA2 XIII Theorem2.1 and its local Bertini discussion develop this argument, using Hartshorne III3.6. The corrected inequality on58:13 points toward the required lower connectedness bound; an opposite inequality would reverse the induction.',
['R_SGA2'],[3,33,35],
computation='Induction on the number of cuts lowers both the relevant component-dimension bound and connectedness bound by one; the finite avoidance set ensures the depth condition on each cut. This is a proof-structure check, not a numerical experiment.',ref_locators={'R_SGA2':'III3.6; XIII2.1–2.4'},confidence='medium')

claim(652,[('K58-02',[13,15,17])],quote('K58-02',91,100),
'Let A be complete noetherian local, X=Spec A and X′ its puncture, and k≥1. Exclude X irreducible of dimension0 or1. If every k-fold cut of X′ by elements of the maximal ideal is connected (with the source convention allowing an empty cut), then every irreducible component of X′ has dimension at least k+1 and X′ is connected in dimension at least k. The manuscript explicitly excludes the irreducible dimension1 case; the dimension0 exception is made explicit in the published formulation.',
'proof sketched','A','The paragraph immediately following SGA2 XIII Theorem2.1 states this converse, with exactly the irreducible dimension0/1 exception, and the subsequent proof reproduces the finite-avoidance/reordering argument on scan13. The published theorem does not add a depth hypothesis: normality/S₂ enters the proof after reduction. Uncertain manuscript inequality glyphs remain scan-review matters.',
['R_SGA2'],[33,34,35,40],confidence='high',fate_date='Seminar1962; published1968; revised electronic edition2005.',
computation='Direct comparison of the quantifiers, irreducible-component bound, connectedness bound and exceptional dimensions with SGA2 XIII2.1 and its following paragraph. The source’s ≤ at line75 reverses the induction and is separately flagged. See root_proofs.md §11.',ref_locators={'R_SGA2':'XIII Theorem2.1 and following converse; originalpp177–178; 2005editionpp139–140'})

claim(653,[('K58-02',[19])],quote('K58-02',252,266),
'For punctured spectra under the complete/local Lefschetz hypotheses, suitable low-codimension cuts induce a surjection on étale π₁, reducing the finite-generation question toward dimension2. Grothendieck conjectures that for a complete noetherian local ring with algebraically closed residue field, all components of dimension≥2 and connected puncture, the full étale fundamental group is topologically finitely generated.',
'open on the pages','C','SGA2 XIII3.1 records the full conjecture and XIII2.4/X treat the slicing mechanism. Suzuki Theorem1.2 proves finite generation of the maximal pro-nilpotent quotient under those hypotheses, hence of the abelian and pro-p quotients. The recent follow-up search found no result settling the full unrestricted group; special klt/F-regular or tame results do not settle it.',
['R_SGA2','R_Suzuki2023'],[13,29,33,35],
fate_date='Grothendieck–Serre letter1October1961, as identified by Suzuki; SGA2 publication1968; Suzuki arXiv4July2022, journal1November2023.',
computation='No finite calculation can certify finite generation of an arbitrary profinite group. The check compares quantifiers: full π₁ versus maximal pro-nilpotent quotient, and retains connectedness of the puncture and the component dimension bounds.',ref_locators={'R_Suzuki2023':'Conjecture1.1; Theorem1.2; introduction historical note'})

claim(654,[('K58-01',[4,6,8,10]),('K58-02',[12,14,16,18])],quote('K58-01',25,31),
'The reused Bourbaki Algebra leaves establish the elementary graded-module formalism: homogeneous components of generators generate a graded submodule; a finite graded module has homogeneous finite generators; graded quotients inherit the quotient grading; degree shifts, multigrading and composition of homogeneous maps obey addition of degrees. The finite-dimensional dual discussion is ancillary algebra and must retain its finiteness hypotheses.',
'proved there','E','These are standard printed algebra results rather than original Picard claims. The statements have direct componentwise proofs; the exact draft number354 is recorded as the witness, while an unverified draft-to-edition identification is not used to date the handwriting.',
['R_BourbakiAlgebra'],[33],
computation='If x=Σa_i m_i with each m_i homogeneous of degree d_i, its degreeλ component isΣ(a_i)_{λ−d_i}m_i. This proves closure of homogeneous components and all finite-generator assertions. Quotient degreeλ isM_λ/(M_λ∩N); the direct-sum decomposition proves the quotient assertion. Duals of infinite direct sums need products, which explains the finite-dimensional restriction.',confidence='high')

claim(655,[('K59-01',[2,3]),('K59-02',[15])],quote('K59-01',7,18),
'For proper flat finitely presented X/S with universally H⁰(O)=O_S, an abelian Picard identity component B, a Picard component P^δ and a local basepoint g, normalize the Poincaré bundle and take its determinant of cohomology M_g on P^δ. Relative perfectness (for example smooth or suitable lci proper data) is needed to define determinant pushforward functorially. Translation acts trivially on NS(P^δ), so the resulting class φ(δ) descends independently of g.',
'proof sketched','B','Knudsen–Mumford’s determinant functor gives the exact coherent-complex construction and base-change formalism; Mukai later develops the Fourier transform based on the same Poincaré kernel. A bare proper morphism does not automatically make every coherent pushforward perfect.',
['R_KnudsenMumford1976','R_Mukai1981','R_Alexeev2002'],[6,18,21,34,35],
computation='For a bounded locally free representative E•, det(E•)=⊗_i(det E^i)^{(−1)^i}. Tensoring by a base line bundle N multiplies this determinant by N^{Σ(−1)^i rank E^i}=N^χ. This is the computation behind the next claim.',
ref_locators={'R_KnudsenMumford1976':'I, determinant axiomspp23–24 and Theorem1p25 (PDF image checked)','R_Alexeev2002':'Theorem3.0.3, translation invariance on Pic⁰ and NS'})

claim(656,[('K59-01',[2,3,4]),('K59-02',[18])],quote('K59-01',65,75),
'Changing normalization from g to g′ twists the Poincaré family by the inverse of its evaluation at g′; its determinant changes by that line bundle to exponent−χ(δ). Consequently the associated map on the Albanese torsor changes by−χ times the difference of the two basepoints, for the standard determinant convention.',
'proof sketched','B','The determinant tensor rule and the theorem of the square establish the formula. Knudsen–Mumford supplies the canonical determinant construction; the sign follows from the inverse in normalization and is independently checked here, rather than read off an analogy with a theta divisor.',
['R_KnudsenMumford1976','R_Mukai1981'],[6,18,21],
computation='Normalize P_g′=P_g⊗p₂*N^{-1}. Then R p₂*(P_g′)=R p₂*(P_g)⊗N^{-1}; taking det givesM_g′=M_g⊗N^{−χ}. Every sign comes from the displayed inverse. research/root_proofs.md §8.')

claim(657,[('K59-01',[4,5,6]),('K59-02',[18,19,20,21])],quote('K59-01',177,187),
'Put Q=Alb¹(X), P=Pic_X^δ, R=Pic_B^{φ(δ)}, and define h(β)=t_β* M⊗M^{-1} for the determinant line M. With the positive Poincaré kernel and the standard determinant, the two equivariances are −χ on Q and +h on P. Thus the contracted A-torsor R+χQ−h_*P is trivialized by a coherently normalized determinant map. The manuscript instead writes R+χQ+tilde(φ(δ))_*P and explicitly requests a sign check; matching that display requires tilde(φ(δ))=−h or a correspondingly opposite kernel convention.',
'open on the pages','C','The determinant, Albanese and torsor ingredients are established in Knudsen–Mumford, Mukai and Alexeev. The exact three-torsor formula is not located verbatim as a named theorem in the searched sources. The modern signed relation follows conditionally from the explicitly fixed equivariance conventions, but the manuscript’s tilde/determinant dictionary and its claimed canonical trivialization are not certified by a torsor-class equality alone.',
['R_KnudsenMumford1976','R_Mukai1981','R_Alexeev2002','R_PoonenStoll1999'],[6,18,20,21,31,35],
computation='C-SA14-656 gives −χ in the basepoint variable, and C-SA14-669 gives +h in the Pic⁰ variable with h defined by pullback. An equivariant map Q×P→R identifies R with (−χ)_*Q+h_*P; subtracting gives R+χQ−h_*P. If the manuscript tilde denotes −h, its displayed plus sign agrees. The actual chosen isomorphism and normalization, not just equality in H¹(S,A), are needed for a canonical trivialization. See root_proofs.md §§8–9 and parts/lfunctions/cross_review_root_655_673.md.',confidence='medium')

claim(658,[('K59-01',[6,7,8]),('K59-02',[16,17])],quote('K59-01',209,224),
'Under Grothendieck–Riemann–Roch hypotheses, put a=Td(T_X)exp(δ), and let D=c₁(P) be the normalized Poincaré class. Then χ(δ)=∫_X a_n and c₁(det R p₂*(P⊗L))=(1/2)p₂*(a_{n−1}D²). With a perfect coefficient F, replace a bych(F)Td(T_X)exp(δ). This is the degree-two cohomological formula, not an assertion that all Chow components vanish.',
'proof sketched','A','The GRR formalism is developed in SGA6 and the Fourier calculus in Mukai/Beauville. The source’s coefficient and degree extraction are independently checked; the possible missing rank term a₀ on59:17 is recorded separately.',
['R_SGA6','R_Mukai1981','R_Beauville1983','R_Beauville1986'],[18,20,21,27,28,30],
computation='D has bidegree(1,1) in H¹(X)⊗H¹(B). To obtain outputdegree2 after integrating overdimX=n, the only term isD²/2 timesa_{n−1}. scripts/root_computations.py: fourier_grr_sign expands the exterior algebra in dimensions1–3 and checks coefficients and signs.')

claim(659,[('K59-01',[9])],quote('K59-01',285,300),
'For a smooth proper curve of genus g and a degree-d line bundle, χ=1−g+d. The associated NS class of det RΓ of the normalized Poincaré family is the negative of the canonical theta class for the standard determinant-of-cohomology convention. The source calls it the positive theta class while also flagging sign uncertainty; the discrepancy is conditional on determinant and translation conventions.',
'open on the pages','B','Mukai’s Fourier construction and the classical theta determinant description supply the established interpretation. Poonen–Stoll identifies the associated polarization torsor with Pic^{g−1}. The exact sign of Grothendieck’s symbol is left to the source convention, not silently rewritten.',
['R_Mukai1981','R_PoonenStoll1999','R_Alexeev2002'],[6,18,20,35],
computation='scripts/root_computations.py: fourier_grr_sign dimension1 givesp₂*(D²/2)=−θ. Riemann–Roch givesχ=d+1−g. Replacing det by its inverse reverses the theta sign, which is why this is a convention alarm rather than an unconditional ink refutation.',confidence='medium')

claim(660,[('K59-01',[10])],quote('K59-01',317,326),
'The conjecture that universal-curve Picard sections are generated by the canonical class has a strong Franchetta formulation for the generic curve of genus g≥3: Picard-scheme rational points are generated by K; pointed versions add the marked points. The literal genus1 variant with a marked point is false, since K has degree0 whereas O(mark) has degree1. The stack/coarse-moduli distinction matters in low genus.',
'open on the pages','B','Schröer Theorem5.1 proves the strong statement in arbitrary characteristic for g≥3, following Mestrano/Kouvidakis in characteristic zero and Arbarello–Cornalba for the weak form. The opened source does not justify transplanting that theorem to the source’s marked genus1 case or to an unspecified genus2 coarse universal family.',
['R_Schroer2003','R_FringuelliPirisi2019'],[4,23,29,30,31],
fate_date='Schröer arXiv19March2002; revised6February2003; journalInternat.J.Math.14(2003)371–396. Earlier characteristic-zero antecedents are distinguished in the cited paper.',
computation='scripts/root_computations.py: universal_pointed_genus_one_counterexample. On the universal pointed elliptic curve,degK=0 anddegO(e)=1, so no integral multiple ofK equalsO(e).',ref_locators={'R_Schroer2003':'Theorem5.1 and introduction'})

claim(661,[('K59-01',[10])],quote('K59-01',328,341),
'The Fourier transform exchanges intersection and Pontryagin products and squares to(−1)^g[−1]*. It sends cohomological codimension p to g−p, but on Chow groups the precise rule is CH^p_s→CH^{g−p+s}_s in Beauville’s grading. Thus an unqualified assertion that the entire CH^p goes toCH^{g−p} is too strong.',
'stated without proof','B','Mukai1981 Theorem2.2 proves the derived inversion formula; Beauville1983/1986 establishes the Chow transform and its grading. The actual image of Beauville1986 printedp648 was inspected: Proposition2(b) gives the shifted codimension formula.',
['R_Mukai1981','R_Beauville1983','R_Beauville1986'],[6,18,20,21],
computation='The exterior-algebra check in scripts/root_computations.py verifies the cohomological transform and its signs for diagonal polarizations. It is not a formal certificate for the full derived or Chow theorem.',fate_date='Mukai paper received9October1979, published1981; Beauville conference1982/publication1983; refined grading1986.',ref_locators={'R_Mukai1981':'Theorem2.2','R_Beauville1986':'Propositions1 and2(b), p648'})

claim(662,[('K59-01',[10,11])],quote('K59-01',345,362),
'For a nondegenerate divisor class δ on a g-dimensional abelian variety and the standard negative determinant transform φ, the corresponding homomorphisms satisfy φ̃(δ)∘δ̃=−χ(δ)id. With δ′=−φ(δ), one hasχ(δ′)=χ(δ)^{g−1} andδ″=χ(δ)^{g−2}δ. However φ(φ(δ))=(−1)^gχ(δ)^{g−2}δ; the transcribed unsigned formula fails in odd dimension.',
'false as stated','B','Mukai/Beauville Fourier identities yield the normalized adjugate formula. The two notationsδ′=−φ(δ) andφ∘φ cannot be interchanged without a parity factor. This is an explicit formal calculation, with nondegeneracy and sign conventions stated.',
['R_Mukai1981','R_Beauville1983'],[6,18,20],
computation='scripts/root_computations.py: fourier_grr_sign and double_phi_parity fordimensions2,3,4. For diagonalδ=(d_i),χ=∏d_i andφ(δ)_i=−∏_{j≠i}d_j. Composing gives(−1)^gχ^{g−2}d_i. Atg=3 andall d_i=1 the claimed positive formula has the wrong sign.')

claim(663,[('K59-01',[11])],quote('K59-01',363,372),
'The assertion that a dual polarization obtained by the adjugate construction is always primitive is false, even when the original class is primitive. On a product of pairwise nonisogenous elliptic curves with type(1,2,2), the adjugate polarization has diagonal type(4,2,2) and is divisible by2 in NS.',
'false as stated','B','The established polarization-type formalism distinguishes a polarization from a primitive one. The Fourier/adjugate construction is valid; the extra primitiveness claim is not. Modern moduli of polarized abelian varieties fix a polarization type, not merely the Euler characteristic.',
['R_Mukai1981','R_Alexeev2002','R_Laga2025'],[18,30,31,35],
computation='scripts/root_computations.py: dual_polarization_primitive_counterexample. On pairwise nonisogenous complex elliptic factors, NS is the diagonal Z³, so gcd(1,2,2)=1 andgcd(4,2,2)=2 prove both primitiveness and failure exactly.')

claim(664,[('K59-01',[12,13,14])],quote('K59-01',418,430),
'The torsor annihilator calculation uses the greatest common divisor, not the least common multiple, ofλ^g−λ^{g−1}. For g≥2 that gcd is2. More generallygcd_λ(χλ^g−λ^{g−1})=gcd(χ−1,2). These are annihilator statements about a torsor class; they do not by themselves choose a canonical section.',
'proof sketched','B','Poonen–Stoll’s polarization-torsor class and the canonical2λ construction agree with the2-torsion conclusion. The arithmetic gcd is independently proved here; the literal “ppcm” must be checked on the scan.',
['R_PoonenStoll1999','R_Alexeev2002'],[6,18,31,35],
computation='scripts/root_computations.py: torsor_annihilator_gcd checks many values; the proof is separate. Everyλ^{g−1}(λ−1) is even; evaluatingλ=−1 gives±2. Forχλ^g−λ^{g−1}, λ=1 givesχ−1 andλ=−1 gives±(χ+1), so the gcd divides2 andχ−1; parity gives equality. research/root_proofs.md §9.')

claim(665,[('K59-01',[14])],quote('K59-01',490,502),
'Even Euler characteristic of a polarization does not imply divisibility of its NS class by2. A polarization of type(1,2) on a product of nonisogenous elliptic curves hasχ=2 and primitive divisor class. A vanished2-torsion obstruction or an even degree is not the same as a square root of the line bundle.',
'false as stated','B','The standard polarization-type description and the modern torsor literature distinguish these invariants. Fringuelli–Pirisi’s universal Picard computation further shows that a canonical class inducing2λ need not have a universal square root without level conditions.',
['R_PoonenStoll1999','R_FringuelliPirisi2019','R_Laga2025'],[6,29,30,31],
computation='scripts/root_computations.py: even_chi_not_twodivisible. NS(E₁×E₂)=Z² for nonisogenous complex elliptic curves;δ=(1,2) hasχ=2 butδ∉2NS. Every geometric and positivity hypothesis is satisfied.')

claim(666,[('K59-01',[13,14]),('K59-02',[28])],quote('K59-01',456,468),
'For a polarizationλ:A→A∨, the Poincaré pullback(1,λ)*P canonically represents2λ, with the usual rigidification. The source asks whether its independently constructed section of the doubled polarization torsor agrees with this canonical one. Existence of a section and equality of two canonical constructions are distinct questions.',
'open on the pages','C','Poonen–Stoll §4 and Alexeev Remark3.0.11 give the canonical doubled-polarization class. The source’s proposed comparison is not identified verbatim in the searched literature. It can only be claimed after comparing rigidifications and the translation/inversion conventions, not from2c_λ=0 alone.',
['R_PoonenStoll1999','R_Alexeev2002','R_Laga2025'],[6,18,31,35],
computation='The square theorem givesφ_(1,λ)*P=λ+λ∨=2λ for symmetricλ. This proves the class represented. It does not by itself identify an arbitrary section ofPic^{2λ} with the Poincaré section.',confidence='medium')

claim(667,[('K59-02',[15,16,17])],quote('K59-02',7,17),
'Replacing O_X by a relatively perfect complex F makes the determinant construction additive in distinguished triangles, hence inK₀(X). It is generally polynomial of degree g−1 in a divisor classδ on a g-dimensional abelian variety, so it is not a homomorphismNS(X)→NS(B) under tensor product when g≥3. On59:17 the sum of Chern-character terms must include the rank terma₀.',
'false as stated','B','Knudsen–Mumford proves determinant additivity in complexes; Mukai/Beauville gives the polynomial Fourier expression. The claim of additivity inδ conflates the additiveK-group inputF with the multiplicative line-bundle inputexpδ.',
['R_KnudsenMumford1976','R_Mukai1981','R_Beauville1986'],[6,18,20,21],
computation='For a principally polarized abelian3-fold,φ(2δ)=4φ(δ), whereas additivity would require2φ(δ). The nonzero adjugate calculation in C-SA14-662 supplies an explicit example. Atg=1, dropping a₀ removes the entire degree-two Fourier contribution.')

claim(668,[('K59-02',[16])],quote('K59-02',68,87),
'On a smooth proper curve, for a vector bundle F of rankρ and degree c, and a degree-d line bundle L, χ(F⊗L)=ρ(1−g+d)+c, and the theta NS class of its determinant family isρ times that forO_X. The transcribed formulas1−g+d+c and unchangedφ are correct only in rank1; the paragraph starts with rankρ and then drops it.',
'false as stated','B','GRR and the determinant tensor formalism establish the rank-weighted statement. The final observation that detF yields a degree-c Picard section survives after subtractingρ copies of the original torsor relation.',
['R_KnudsenMumford1976','R_SGA6','R_Mukai1981'],[6,18,21,27,28],
computation='scripts/root_computations.py: perfect_complex_curve_rr. ForF=O⊕O on an elliptic curve anddegL=1,χ(F⊗L)=2 but the transcribed rank-one expression gives1;ρ=2,c=0 and every smooth/proper hypothesis holds. The D² term of GRR has coefficientρ.')

claim(669,[('K59-02',[18,19,20])],quote('K59-02',142,159),
'For the positive Poincaré Fourier transform, Φ(L⊗P_β)=t_β*Φ(L). If M=det Φ(L) and h_M(β)=t_β*M⊗M^{-1}, then l_g(λ+β)−l_g(λ)=+h_M(β). The support of t_β*D moves by−β, but this does not introduce a second minus into h_M, which already uses pullback. A formula with −tilde(φ(δ))(β) agrees when the tilde map is defined by image translation, equivalently by t_{−β}*; an inverse Poincaré kernel likewise changes the dictionary. The page twice asks to verify these signs.',
'open on the pages','B','Mukai §3, equation(3.1), gives the exact tensor/translation exchange. The modern statement is established after the kernel and pullback conventions are fixed. The source’s ambiguous sign and tilde convention remain a reading/formulation question; the manuscript’s exact signed three-torsor formula is separately retained in classC, C-SA14-657.',
['R_Mukai1981','R_KnudsenMumford1976'],[6,18,21],
computation='ForP_x,β⊗P_x≅P_{x+β}; hence the new family atx is the old family atx+β, so M(λ+β)=t_β*M(λ). Dividing byM(λ) gives +h_M(β). If tilde_M(β)=t_{−β}*M⊗M^{-1}=−h_M(β), the same identity reads −tilde_M(β). This explicit dictionary corrects an earlier reconstruction in this run; no source transcription is altered. research/root_proofs.md §8.',ref_locators={'R_Mukai1981':'§3, equation(3.1)'})

claim(670,[('K59-02',[20,21,23])],quote('K59-02',237,249),
'The construction extends from the whole abelian Picard identity component to a specified homomorphismi:B→Pic_{X/S}, with B abelian, and a B-torsorP mapping equivariantly to a Picard component. The corresponding dual torsorQ receivesX; determinant equivariance yields the same contracted-torsor relation. Universality among all commutative group targets is a separate question and needs extra hypotheses.',
'open on the pages','B','The Albanese/Picard correspondence for abelian torsors is established by the published duality construction, with a modern precise relative formulation in Laurent–Schröer Theorem10.2. For proper connected X over a field, maps to affine schemes factor throughH⁰(O_X), but this does not automatically settle every relative or nonsmooth group target.',
['R_LaurentSchroer2024','R_Alexeev2002','R_Kleiman2005'],[13,15,24,35],
computation='A mapX→an abelian torsor underB∨ pulls back the Poincaré biextension to a family parametrized byB; conversely that rigidified family reconstructs the torsor map by duality. The basepoint-change rule is the same as C-SA14-656.',confidence='medium')

claim(671,[('K59-02',[23,24,25])],quote('K59-02',320,335),
'For a smooth proper curve, the Albanese degree-one torsor identifies withPic¹ and its duality with the Jacobian is the canonical autoduality. Whether the manuscript’s mapc equalsλ_Θ or−λ_Θ depends on whether its Abel map isx↦O(x−x₀) orx↦O(x₀−x), and on translation conventions. The page’s proposed negative/symmetric sign is unfinished.',
'open on the pages','B','The canonical principal polarization and Pic^{g−1} theta torsor are established; Kleiman Remark5.26 explicitly uses the negative Abel conventionL⊗O(−Γ). Poonen–Stoll and Alexeev give the torsor form. These sources resolve the mathematics once the convention is fixed, but do not decide the ambiguous handwritten sign.',
['R_Kleiman2005','R_PoonenStoll1999','R_Alexeev2002'],[6,24,35],
computation='Replacing the Abel map by its negative composes its induced dual map with[−1], so the polarization comparison changes sign. The symmetry of a polarization is preserved. A sign cannot be inferred just from the word“canonical”.',confidence='medium')

claim(672,[('K59-02',[26,27,28])],quote('K59-02',360,368),
'A principally polarized abelian scheme(A,λ) canonically determines anA-torsorP together with a relative effective theta divisorΘ, unique up to the corresponding equivariant isomorphism. TakeP=Pic_A^λ with theA-action identified throughλ; the normalized Poincaré bundle has a rank-one section bundle and evaluation at0 definesΘ. For a Jacobian,P=Pic^{g−1}(C) andΘ=W_{g−1}.',
'proof sketched','B','Alexeev Construction3.0.5, Lemma3.0.6, Corollary3.0.7 and3.0.10 give precisely this construction and equivalence of groupoids. It does not require a global theta line bundle onA itself. Laga2025 shows that an unrestricted analogous assertion for every nonprincipal polarization is false in general.',
['R_Alexeev2002','R_PoonenStoll1999','R_Laga2025'],[6,29,30,31,34,35],
fate_date='Alexeev first arXiv18May1999, journalMay2002; Laga first28October2025, v2 6November2025, no journal publication established.',
computation='For a principal polarizationχ(L)=1 and higher cohomology vanishes fibrewise for ampleL, so p_*P is a line bundle. Its evaluation at the zero section cuts a relative divisor. Any theta pair maps equivariantly to this torsor and the map is an isomorphism. This is a targeted proof check of Alexeev’s argument.',ref_locators={'R_Alexeev2002':'3.0.5–3.0.10, pp664–665','R_Laga2025':'TheoremsA–C; §2.4'})

claim(673,[('K59-02',[27,28])],quote('K59-02',389,410),
'The inverse theta pair yields an involution on the theta torsor and a canonical section of its doubled contracted torsor. For a Jacobian this is L↦K_C⊗L^{-1} onPic^{g−1}, and the doubled section isK_C. The source’s final question asks comparison with the separate canonical section ofPic^{2λ}; that comparison still requires compatible rigidifications.',
'open on the pages','B','Serre duality/Riemann–Roch makes the Jacobian involution andK_C identification exact; Poonen–Stoll’s2-torsion class and Alexeev’s canonical doubled-polarization class are compatible endpoints. The last symbol-level identification is isolated as C-SA14-666 rather than declared proved merely because both classes exist.',
['R_PoonenStoll1999','R_Alexeev2002'],[6,18,35],
computation='For degL=g−1, Riemann–Roch givesh⁰(L)=h⁰(K_C⊗L^{-1}), so the involution preservesW_{g−1}. In the contracted productPic^{g−1}×^J Pic^{g−1}≅Pic^{2g−2}, the pair(L,K_C⊗L^{-1}) maps toK_C independently ofL. This proves the canonical doubled torsor section in the curve case.')

claim(674,[('A57-02',[20,21,22,23]),('K57-01',[29,31,33])],quote('A57-02',25),
'The normalized correspondence functor for two proper flat families with universalH⁰(O)=O_S is expected to be separated even when the whole Picard functor is not. The Murre letter gives the projective/representable cases and suggests a fundamental-group specialization route for the remaining case. The valuative proof using a vertical divisor assumes geometric integrality or normality where stated.',
'open on the pages','C','Murre’s §3(C) Theorem4 explicitly ASSUMES separatedness to prove representability and calls the unrestricted separatedness assertion a problem. It gives sufficient cases when either factor has separated Picard functor, for instance geometrically integral fibres. The modern Bertolin–Galluzzi Theorem1.1 treats extensions of abelian schemes by tori and cites Raynaud LNM119 III Proposition4.3. The Raynaud chapter metadata was opened, but that proposition was not accessible directly. Modern Picard algebraic-space representability alone does not supply the unchecked generic-constant-to-special-constant step for a possibly nonseparated target. The general letter question is therefore not declared settled or certified currently open; the precise unclosed dependency is recorded in parts/picard_early/supplement_root_audit.md.',
['R_Murre1966','R_FGA232','R_Kleiman2005','R_BertolinGalluzzi2020','R_Raynaud1970Corr'],[4,24,25,26,43,44,55],
computation='For a normal family over aDVR with integral special fibre, a vertical Cartier divisor is an integral multiple of the whole special fibre, which is principal. This proves triviality in that case. Without geometric integrality, separate components can carry nontrivial vertical classes, as C-SA14-632 shows.',confidence='medium')

claim(675,[('K57-06',[197,199])],quote('K57-06',125,133),
'Reused printed commutative algebra discusses regular local rings, dimension, systems of parameters, catenarity, finite-type extensions and Hilbert–Samuel degree. The displayed example allows closed maximal ideals of different heights in a regular ring that is not a finite-type algebra over a field: for aDVRV with uniformizerπ, V[T] has maximal ideals(π,T) of height2 and(πT−1) of height1.',
'proved there','E','These are standard commutative-algebra assertions; the finite-type-field equidimensionality statement does not apply to theDVR base example. The exact Nagata1956 bibliographic reference on the reused leaf needs edition-level identification and is not used as a handwriting date.',
['R_EGAIV4','R_EGAI'],[23,27,29,30],
computation='V[T]/(π,T)=k, whileV[T]/(πT−1)=V[1/π]=Frac(V), so both ideals are maximal. The first has a chain(0)⊂(π)⊂(π,T); the second is principal nonzero prime and has height1. The regularity ofV[T] is preserved under polynomial extension.',confidence='medium')

claim(676,[('A57-01',[13])],quote('A57-01',198),
'Construct a locally finite-type local Picard scheme without assuming that the punctured spectrum is regular, either by finding a proper modification on which all punctured line bundles extend or by descending line bundles from a resolution. Test whether H²_m(A)=0 implies that Pic(U) is countable and, over a separably closed coefficient field, invariant under separable extension after completed scalar extension.',
'open on the pages','C','Boutot representability and Kollár’s precise S₂, pure-dimension≥3, essential-finite-type setting establish the geometric local-Picard framework without regularity of the puncture. The unrestricted complete-local-ring formulation and every proposed countability or scalar-extension assertion are not consequences of that quoted theorem. They remain qualified formulation questions here.',
['R_Boutot1978','R_Kollar2014','R_Lipman1976'],[3,15,36],confidence='medium',
computation='The tangent vanishing H²_m(A)=0 implies discreteness only after representability and the tangent identification have been established. A locally finite-type discrete group scheme need not be countable merely from its local finiteness; the component-countability step requires an additional boundedness or presentation argument.',
ref_locators={'R_Kollar2014':'Published Condition1.3, §3.3–3.4; preprint Condition3, §24–25'},
present='Developed for the cited geometric hypotheses; no unrestricted complete-local-ring theorem or counterexample was established by the recorded search.')

claim(677,[('A57-02',[74])],quote('A57-02',64),
'Find a proper-surjective family over a one-dimensional base for which pullback on Picard functors is quasi-affine but not affine, preferably either a birational morphism between smooth projective families or a finite morphism between normal projective families. The latter is linked to the effectivity of finite descent data.',
'open on the pages','D','The opened SGA6/Murre/Kleiman results distinguish generic relative quasi-affineness from affineness over a field. The bounded search did not locate an example satisfying either of these two specific configurations; this is a recorded non-identification, not a claim that modern mathematics has no example.',
['R_SGA6','R_Murre1966','R_Kleiman2005'],[24,26,27,28,36],confidence='medium',
computation='No candidate example is asserted, so no counterexample check is claimed. The requested endpoints and hypotheses are recorded verbatim before any modern reformulation.',
present='No exact matching counterexample identified in the searched sources; worth a focused literature check after the final SGA6 hypothesis comparison.')

claim(678,[('K57-01',[25,26,27,28,29])],quote('K57-01',372),
'The product-rigidity proof has two lemmas: a proper Stein morphism f:X→Y and a map to a separated locally finite-type Y-scheme whose image on X_y is finite give a unique factorization through Y near y; and the finite-image locus for a universally open finite-type source is closed. Together with the page’s connected-fibre assumptions, maps from products into a separated group split into normalized factors. A map from an abelian scheme to a group, carrying zero to zero, is a group homomorphism; the pointed multiplication law is unique.',
'proof sketched','C','The usual rigidity lemma and its abelian-scheme consequences are established in Milne and the abelian-variety literature. The page’s edits leave an undefined hypothesis c) and mixed noncommutative additive notation. The two local lemmas can be justified in the displayed noetherian setting, but the entire changing product theorem is not represented as a uniquely fixed published statement.',
['R_Milne2008','R_Murre1966','R_GenestierNgo'],[4,10,11,41,42,44],confidence='medium',
computation='For the Stein lemma, the scheme-theoretic image is proper overY and quasi-finite near y, hence finite there. Its finite structure algebra injects into f_*O_X=O_Y and contains O_Y, so it is O_Y. For the closed-locus lemma, reduce a specialization to aDVR; an irreducible finite-type closure with finite generic fibre has dimension1 and zero-dimensional special fibre. Ordered multiplication must replace addition for a noncommutative target.')

claim(679,[('A57-02',[20])],quote('A57-02',9,11),
'If the equivalence relation R=X×_Y X defined by a morphism is flat over X, under the stated locally finite-presentation or locally noetherian finite-type hypotheses, the fpqc quotient factors X→Z→Y with the first arrow faithfully flat locally of finite presentation and the second a monomorphism. Uniqueness is uniqueness of the quotient sheaf, not a choice of schematic image.',
'stated without proof','B','Murre §3(A) Corollary2 gives exactly the finite-type locally-noetherian version and its flat relation criterion, as an application of universal flattening. ClassB records this checked publication, which expressly reports unpublished results of Grothendieck; it does not transfer mathematical priority to Murre. The source’s local finite-presentation extension is kept distinguished from that printed formulation.',
['R_Murre1966','R_StacksFlattening'],[41,42,44],
computation='After a candidate quotient is represented, its uniqueness follows because X→Z is an fpqc cover and the two projections ofR impose exactly the sheaf coequalizer relation. The existence step is the cited flattening theorem, not deduced merely from point-set quotienting.',ref_locators={'R_Murre1966':'§3(A), Corollary2, collectionp254'})

claim(680,[('A57-02',[20])],quote('A57-02',13),
'The Raynaud quotient discussion over aDVR must require flatness of G when concluding that G/H is flat, and separation when inferring affineness from an affine generic fibre. In the established form, a flat separated finite-type group over aDVR with affine generic fibre is affine. Quotients by flat closed subgroups over a henselianDVR are representable under the stated local finite-type hypotheses.',
'false as stated','B','SGA3 XVII AppendixIII C.2.1 explicitly includes flatness and separation for the affineness conclusion; C.3.1 gives the henselianDVR quotient result. Anantharaman1973, Theorem4C, supplies the cited quotient framework. The source’s missing G-flatness cannot be repaired by the flatness of H alone.',
['R_SGA3XVII','R_Anantharaman1973','R_Murre1966'],[41,42,43,44],
computation='LetR=k[[π]] in charp>0 andG=Spec R[x]/(πx,x^p) with additive comultiplication. H=e=SpecR is a flat closed subgroup; G_t is trivial and affine. ButG/H=G has nonzeroπ-torsion x and is not flat. Thus the literal flatness conclusion fails with every written hypothesis; addingG-flatness removes this example.',
status_reason='The counterexample addresses a missing hypothesis in the transcribed quotient application; it does not refute Raynaud’s correctly stated theorem.')

claim(681,[('K57-01',[16])],quote('K57-01',61,66),
'The sheet sketches a moduli functor of invertible sheaves with a marked section and vanishing higher direct images. Local freeness and base change of H⁰ require the usual proper-flat or perfect-complex hypotheses, not just the isolated notation R^if_*L=0. The final quotient diagram ends before its claimed equivalence is formulated.',
'stated without proof','F','FGA’s Div/Pic construction explains the likely setting, but the cancelled block and unfinished final equivalence do not specify an independently identifiable theorem. The sheet is indexed as a separate underdetermined construction instead of being silently absorbed into a stronger representability theorem.',
['R_FGA232','R_Kleiman2005'],[24,26,40],confidence='low',
computation='Under proper flat finite-presentation hypotheses and fibrewise higher-cohomology vanishing, a perfect complex concentrated in degree0 gives a locally free pushforward with base change. Those hypotheses are a reconstruction; the source fragment alone does not supply them.')

claim(682,[('K57-01',[30,31,32])],quote('K57-01',467,478),
'For proper flat X/S with universal H⁰(O_X)=O_S, the pages seek a functorial rigidity criterion: fibrewise constancy of a map X→G should spread to an open locus and become constant over a connected base once a closedness condition holds. Formal representability, adic-limit compatibility, filtered limits and fpqc descent are proposed; a valuative criterion is left blank.',
'open on the pages','C','Murre’s representability theorem supplies a precise list of conditions for separated unramified functors, and ordinary representable group targets satisfy standard rigidity results. It does not automatically validate the draft with its missing valuative condition. The finite-image and product lemmas in C-SA14-678 identify the representable part.',
['R_Murre1966','R_Milne2008'],[41,42,44],confidence='medium',
computation='An open constancy locus in a connected base need not be the whole base. The proof needs its asserted closedness. The blank at source line472 is therefore a genuine missing premise, not an editorial omission that can be ignored.')

claim(683,[('K57-03',[53,54,55,56,57,58])],quote('K57-03',196,218),
'Over a perfect ground field and a geometrically irreducible parameter scheme, the proposed rigidity argument reduces a family of closed subgroups with rigid generic identity component to a fixed smooth subgroup plus a finite radicial subgroup of the quotient. Flatness should descend across the quotient; a flat family with one smooth fibre then has trivial radicial quotient throughout. Earlier primary-extension steps concern supports before full subgroup schemes.',
'proof sketched','C','SGA3 gives the quotient and torsion-rigidity mechanisms, but the exact broad family statement depends on the manuscript’s admitted spreading lemma and its changing very-rigid definition. The quotient-descent step is valid for an fpqc quotient; a merely topologically surjective homomorphism is insufficient, as C-SA14-613 records.',
['R_SGA3XI','R_SGA3VIA','R_SGA3VIB'],[8,9,20,26,27],confidence='medium',
computation='For a finite flat radicial quotient over a connected base, its rank is locally constant. A smooth radicial fibre is the identity, of rank1; hence every fibre and the whole quotient has rank1. This proves the last corollary once existence and flatness of the quotient are established; it does not prove the initial support-spreading assertion.')

claim(684,[('K57-06',[209])],quote('K57-06',474,480),
'A locally constructible subset Z in a separated locally finite-type family, with proper fibres and the stated lifting of generizations, is relatively quasi-compact. The subset must have the locally closed scheme interpretation used in the proof; a bare topological assertion of proper fibres is not enough to manufacture that structure.',
'proof sketched','C','The page gives the same noetherian-induction mechanism as the preceding finite-type criterion, now using generization lifting to eliminate a complementary piece with empty generic fibre. The precise constructible-subset formulation was not located verbatim in the opened EGA references, so only the argument under its explicit scheme interpretation is accepted.',
['R_EGAIV3','R_Kleiman2005'],[25,27],confidence='medium',
computation='After spreading a proper generic piece Z′, separation makes Z′ closed inX; the chosen quasi-compact open makes it also relatively open inZ. A point of the complement would lift to a generic point of that complement by the assumed generization property, contrary to emptiness of the generic fibre. Noetherian induction then supplies quasi-compactness.')

claim(685,[('K57-04',[71,72])],quote('K57-04',154),
'The page asks whether the recorded finiteness results recover an external equivalence criterion (ii), via fibrewise injectivity of a Néron–Severi-type morphism. The referenced statements(i),(ii),(iii) are not fully reproduced, so this exact question cannot be identified simply with the finite-type Picard pullback theorem.',
'open on the pages','F','SGA6 XIII supplies numerical/τ equivalence, degree tests and uniform NS bounds; XII supplies Picard pullback representability. The missing text of the externally numbered criterion prevents a precise assertion-by-assertion identification of this further implication.',
['R_SGA6','R_FGA236Addendum'],[23,27,28,38],confidence='low',
computation='No proof is claimed for a proposition whose hypotheses and numbered antecedent are not supplied. The surrounding established finiteness assertions remain separately classified in C-SA14-618 and C-SA14-620.')

claim(686,[('K57-03',[64])],quote('K57-03',414,422),
'Let S have residue fields of characteristic zero and let G/S be a group scheme locally of finite presentation along the unit section e. Then G is smooth along e if and only if its conormal module ω_G/S=e*Ω_G/S is locally free. No prior flatness of G is added. This is the general group-scheme question on the page, distinct from the nearby Picard-specific smoothness question.',
'open on the pages','B','SGA3 VI B Proposition1.6 (Bertin) gives the exact equivalence, with local finite presentation along the unit stated explicitly. The proof identifies Ω_G/S with the pullback of ω_G/S and applies EGA IV4 16.12.2 and17.12.5. The field case is separately recorded as Corollary1.6.1. ClassB credits Bertin’s authored chapter, although it appears in Grothendieck’s seminar.',
['R_SGA3VIB','R_EGAIV4'],[46],confidence='high',fate_date='SGA3 seminar1962–1964; published1970. Earlier circulation of this particular proposition was not independently established.',
computation='Hypothesis-by-hypothesis comparison with the primary SGA3 VI B Proposition1.6. This is a targeted theorem check, not an independent proof of the EGA smoothness criterion.',ref_locators={'R_SGA3VIB':'Proposition1.6; originalprintedp327; editorPDFp6/currentp202'})

claim(687,[('K57-08',[138,140])],quote('K57-08',127,141),
'Let f:X→S factor as X→Σ→S, with Σ→S finite and O_Σ→φ_*O_X an isomorphism preserved after every S-base change. Suppose g:Σ→X is a section of φ. Then Q(T)=Pic(X_T)/Pic(Σ_T) is the functor of g_T-rigidified line bundles up to isomorphism and is an fpqc sheaf. It identifies with the fppf-sheafified relative Picard functor of X/S, because line bundles on the finite scheme Σ_T become trivial Zariski locally on T. Flatness of Σ/S is not needed. The source’s successive Pic-prime and Pic-star conventions are preserved as historical stages, rather than identified without explanation.',
'proof sketched','A','The FGA descent/comparison framework establishes the rigidified Picard description. This more general finite-Stein-factor version is explicitly present on57:138–140 and is not reduced to the special case Σ=S. The normalization and sheaf-identification implications have also been independently re-proved in this run.',
['R_FGA232','R_Kleiman2005'],[4,24,26,40],confidence='high',
computation='Normalize by L⊗φ_T*(g_T*L)^−1. Universal φ_*O=OΣ kills every rigidified automorphism, so fpqc descent is effective and unique. Over a local base, a finite algebra is semilocal and has trivial Picard group; a chosen line-bundle generator extends after shrinking. Thus Pic(Σ_T)/Pic(T) sheafifies to zero and the quotient Q agrees with Pic_{X/S}. No finite-flat hypothesis onΣ/S enters this proof. See root_proofs.md §5.')

# Explicit, manually chosen corrections after comparing each quotation with its claim.
# These attach provenance only; no script infers mathematical judgments from text.
_quotations={
 608:('K57-01',38,44),613:('K57-03',65,69),614:('K57-03',28,36),
 615:('K57-03',364,367),618:('K57-04',146,148),619:('K57-04',128,133),
 620:('A57-02',42,42),621:('A57-02',66,66),628:('K57-06',271,285),
 630:('K57-06',446,450),632:('K57-07',114,122),633:('K57-07',104,104),
 634:('K57-07',139,142),635:('K57-07',225,229),636:('K57-07',197,197),
 638:('K57-08',103,103),639:('K57-08',136,141),642:('K57-09',33,38),
 644:('K57-09',101,108),645:('K57-09',160,162),646:('K57-09',431,441),
 647:('K57-10',41,49),648:('K57-10',78,89),653:('K58-02',266,273),
 655:('K59-01',19,35),656:('K59-01',49,55),657:('K59-01',169,175),
 661:('K59-01',319,323),662:('K59-01',360,368),663:('K59-01',373,373),
 673:('K59-02',399,409)}
for _c in CLAIMS:
    _n=int(_c['id'].rsplit('-',1)[1])
    if _n in _quotations:
        _a,_lo,_hi=_quotations[_n]
        _c['his_statement']=quote(_a,_lo,_hi)
        _c['quote_lines']={'file':str(SOURCE[_a].relative_to(ROOT)),'first':_lo,'last':_hi}
    # Long physical lines remain in the preserved transcript; an ellipsis is explicit.
    if len(_c['his_statement'])>1400:
        _c['his_statement']=_c['his_statement'][:1400]+' […]'




