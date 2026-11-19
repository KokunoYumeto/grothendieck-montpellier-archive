"""Individually reconciled problem index; editorial questions are not upgraded to conjectures."""
def prob(n,title,ids,as_he,now,art,refs,worth,why='The supplied pages give no reason for abandonment. The recorded gap or question is the only authorial evidence.'):
    chosen=[next(i for i in items if i['id']==f'SA13-{j}') for j in ids]
    occ=[]
    for i in chosen:
        for loc in i['lines']:
            if loc not in occ:occ.append(loc)
    problems.append(dict(id=f'MP-SA13-{n}',title=title,occurrences=occ,as_he_states=as_he,
       plausible_today=now,state_of_art=art,why_open=why,worth=worth,refs=refs,items=[i['id'] for i in chosen]))

prob(60,'Henselian base and comparison only up to isogeny',[250],
 'Why isS henselian, and why is the introductoryell≠p comparison only up to isogeny?',
 'An integral comparison needs the two actual integral lattices and specialization maps; a rational comparison alone cannot determine their finite indices.',
 'SGA7IX3.5 and5.12 formulate henselian/inertia reduction criteria, but the editorial sentence being criticized is absent. No exact stronger integral theorem is identified.',
 ['SGA7IX'],'Worth a short source-collation task once the criticized draft is identified; there is no well-defined new theorem yet.')
prob(61,'Unsupported introduction and semistable-curve terminology',[251,252],
 'The introduction is said to rest on neither definitions nor theorems; a reference/definition for semistable reduction of a curve is requested, distinct from stable terminology.',
 'State the model, nodal-fibre condition and stability convention before comparing reduction theorems.',
 'SGA7IX3.5–3.6 distinguishes semistable reduction of abelian varieties. This is context, not an identification of the uncopied curve theorem or introductory assertion.',
 ['SGA7IX'],'Useful editorial repair; the missing draft controls which curve theorem belongs in the commentary.')
prob(62,'Categories, isogenies and infinitesimal hypotheses',[253,255],
 'Epimorphism is not the definition of isogeny; is the cited object formally unramified, and is the field separably closed?',
 'For abelian varieties use a surjective homomorphism with finite kernel. Keep formal unramifiedness, étaleness and separable closedness as separate hypotheses.',
 'Milne’s abelian-variety chapter supplies the standard isogeny setting. The leaf’s quasi-projectivity replacement and infinitesimal questions cannot be evaluated without the original sentence.',
 ['Milne1986Abelian'],'Worth exact editorial collation, rather than searching for a universal replacement theorem.')
prob(63,'Equality and sign of two pairing constructions',[254,275],
 'Has the A.M. pairing been checked against yours, including the later request to know the sign?',
 'Compare both finite-level morphisms under fixed rigidification, transposition and Tate-twist conventions; then prove compatible equality before taking the Tate limit.',
 'Deligne10.2.4 controls transposition sign;10.2.5 gives an explicit characteristic0 pairing. SGA7VIII2.3.11 and2.3.18 give finite-level sign formulas. None identifies the absent editorial pair of constructions automatically.',
 ['Deligne1974HodgeIII','SGA7VIII'],'High value: an elliptic-curve normalization followed by a categorical sign calculation can make this comparison concrete.')
prob(64,'Néron models under completion and limits',[257,277],
 'IsS a trait inRemark2.6(a); do the limits commute withNéron; where is completion compatibility proved?',
 'For an abelian variety over the fraction field of aDVR, apply the precise unramified/regular base-change theorem, including its completion case, before any broader inverse-limit assertion.',
 'Robert3.1.5 states index1 and separable-residue base change and citesBLR. BLR publisher identity is verified; the unspecified limit inRemark2.6(a) is not a theorem determined by this citation.',
 ['Robert2023','BLR1990'],'A bounded reference-and-hypothesis task is worthwhile; arbitrary limits require recovering the missing diagram.')
prob(65,'Torsion kernel and specialization',[258],
 'The kernel torsion should be a subgroup of the indicated unramified group; is the kernel zero-dimensional?',
 'The formal identityK[n]=ker(G[n]→H[n]) is valid. The proposed fibre inclusion needs the precise base, specialization and eta/s subscript.',
 'C-SA13-251 proves the formal identity. SGA7IX fixed-part/reduction framework does not uniquely recover the omitted specialization assertion; C-SA13-310 remains underidentified.',
 ['SGA7IX'],'Useful only after the scan and draft reference fix the fibres and group schemes.')
prob(66,'Choice of inertia and tubular-topos Néron picture',[259,260],
 'At least choose an inertia group whenS is not henselian; a tubular-neighbourhood ringed-topos interpretation is proposed.',
 'Choose a prolongation of the valuation toKsep. For henselianK useG_K→G_k and the associated morphism of classifying topoi; a relative-scheme equivalence needs additional ringed-topos data.',
 'SGA7IX3.5 passes to a henselization; Brinon–Conrad§1.1 supplies the standard Galois setup. The uncertaink/K in the tubular construction prevents an exact equivalence theorem.',
 ['SGA7IX','BrinonConrad2009'],'The inertia-choice correction is settled; the tubular construction merits work only after its intended category is reconstructed.')
prob(67,'Contragredient and trace correction',[261],
 'The original statement was correct; the proposed contragredient correction is disputed, with a doubtful marginal response.',
 'Recover the exact representation and trace convention before deciding whether a contragredient changes the formula.',
 'SGA7IX4.3 and5.13 concern trace/reduction comparisons, but the isolated editorial dispute does not identify its assertion.',
 ['SGA7IX'],'A small archival comparison could resolve this; no independent mathematical conjecture is extracted.')
prob(68,'Prime-power terminology and missing references',[262],
 'Doesell-group mean killed byell or byell^n; is the trait strictly local; which reference justifies the paragraph?',
 'Distinguish finite exponentell-primary groups,ell-divisible systems andpro-ell objects explicitly.',
 'SGA7IX5.12 gives theBT/pro-ell setting. It does not resolve the draft’s local terminology without the cited paragraph.',
 ['SGA7IX'],'Useful glossary and bibliography repair; the alternative exponents affect the mathematics.')
prob(69,'Dirac-mass normalization',[263],
 'The page juxtaposes a function withf(e)=1 and one withf(e)=#G.',
 'State the measure: the first has mass1 under counting measure; the second has mass1 under normalized counting measure.',
 'C-SA13-309 andcomputations.py explicitly recompute the two normalizations. SGA7IX is the editorial setting, not a claimed exact publication of these uncopied formulas.',
 ['SGA7IX'],'Resolve when the draft trace formula is recovered; the elementary ambiguity itself is already settled.')
prob(70,'Proof4.7 outside the strictly local case',[264],
 'The editor distrusts the proof forn=2 and outside the strictly local situation.',
 'Check the actual degree-two argument over a henselian/non-strictly-henselian trait, retaining descent and residue-fieldGalois terms.',
 'SGA7IX reduction andBT results are precise comparators, but the text of draft4.7 is not attached; no counterexample is invented.',
 ['SGA7IX'],'Worth focused collation only; the present leaf is an editorial obligation, not a recovered theorem.')
prob(71,'Pro-object or inverse-limit scheme',[265],
 'Are the objects in(5.2.3.1) pro-objects or schemes, and why is connectedness deleted?',
 'Separate a projective system, its pro-category realization and a representable inverse limit; specify how connectedness enters the desired statement.',
 'SGA7IX5 andVIII1.3 use systems explicitly. The leaf’s remark je le dis supplies no visible definition or proof.',
 ['SGA7IX','SGA7VIII'],'This categorical distinction is essential to the later finite-system/Tate-limit correction and deserves a single glossary note.')
prob(72,'Characteristic-zero input through Tate',[267,273],
 'Draft6.6 usescharK=0 throughTate, whereas another residue-characteristic restriction may be removed; identify theSerre reference and6.6→5.13 dependency.',
 'Distinguishell≠p inertia criteria from mixed-characteristicBT good reduction. Do not replace good reduction byp-adic inertia semisimplicity.',
 'OriginalSGA7IX5.12.1 translatesBT notions into inertia conditions only forell≠p. IX5.13 allowsell=p whencharK=0 but concernsBT extension; Brinon–Conrad7.1.13 is a modernBT criterion. The abbreviatedSerre citation remains unexpanded.',
 ['SGA7IX','BrinonConrad2009'],'High value because it prevents a real hypothesis error; cross-linked with p2’sK34-04scan67 counterexample.')
prob(73,'Divisible, connected and discrete parts',[268,269],
 'The proof alternates betweenA0 beingell-divisible and not; a discrete part is missing. The claimed ordinary-factor lifting is challenged.',
 'Track connected,étale/discrete, multiplicative and abelian pieces separately, and distinguish algebraic subvarieties from formal orp-divisible subgroups.',
 'SGA7IX5.12–5.13 andRobert’s reduction chapter provide the establishedBT/abelian distinctions. The generically simple deformation sketched on36:006 refutes only an algebraic-subvariety lift once the family exists.',
 ['SGA7IX','Robert2023'],'Worth a precise counterexample task; the categorical distinction matters more than the informal word ordinary.')
prob(74,'Finite and toric parts of expected rank',[271],
 'It should be possible to define finite and toric parts of the right ranks up to isogeny.',
 'Fix the trait, group/pro-group, component conditions and expected rank formula before asking for a canonical construction or splitting.',
 'SGA7IX2 and5 develop such parts under explicit hypotheses, but the editor’s absent setup is not uniquely identified. No universal splitting statement is certified.',
 ['SGA7IX'],'Potentially useful for exact comparison with the published finite/toric filtration; presently an archival matching task.')
prob(75,'Strict henselianity, excellence and an unread proof',[272,274],
 'Proof6.4 is disputed; pp61–61bis are expressly unread. IsS strictly henselian, and is excellence needed later?',
 'Record each hypothesis at the theorem that uses it; the two locality/excellence questions are independent.',
 'SGA7IX supplies precise published hypotheses for reduction theorems. The attached editorial leaf cannot establish which omitted proof uses excellence or strict henselianity.',
 ['SGA7IX'],'Useful editorial repair; do not turn an unread-page marker into evidence that the proof fails.')
prob(76,'Compatibility withR and the sign in9.5.8',[275],
 'Is9.3.3 compatible withR; should9.5.8 be checked up to sign?',
 'IdentifyR and both diagrams, then verify compatibility at the morphism level with a fixed transposition convention.',
 'SGA7VIII2.3 andDeligne10.2.4 show why sign data are structural. The absent formulas prevent resolution of this exact comparison.',
 ['SGA7VIII','Deligne1974HodgeIII'],'Worth merging with the concrete pairing-normalization taskMP-SA13-63 once the draft is recovered.')
prob(77,'Field extension over an already infinite field',[276],
 'Is an extension of the already infiniteK required in10.5.3; where are10.5.4’s checks?',
 'For the actual geometric construction distinguish a rational point in a nonempty open from a splitting field or separability requirement.',
 'SGA7IX is the cited context; no specific10.5.3 construction has been identified from the copied question, so no universal no-extension claim is made.',
 ['SGA7IX'],'A short exact-source task could settle it; infinitude alone is insufficient information.')
prob(78,'Extending a biextension through a trait via torsion',[278],
 'If the interlocutor was understood correctly, extension onell-primary torsion controls extension of the biextension.',
 'Formulate an equivalence of extension groupoids with fixed component, divisibility, representability andfinite-level compatibility hypotheses.',
 'SGA7VII–IX contain torsion and extension theory; VIII1.3 and2.2.8 identify finite torsion pairing data. Those statements alone do not prove the uncopied trait equivalence.',
 ['SGA7VII','SGA7VIII','SGA7IX'],'High value when matched to the precise published monodromy obstruction; do not substitute a Tate-module-only version.')
prob(79,'Lifts, rigidifications and the derived biextension class',[280,281,282],
 'The two splittings must coincide; why does the construction defineExt1(A⊗LA′,Gm)? The handwritten proof stops.',
 'Use complexes[M→G] in degrees−1,0 with a biextension onG×G′ and compatible trivializations onM×G′ andG×M′, agreeing onM×M′.',
 'DeligneHodgeIII10.2.1 proves the exact derived interpretation for such complexes on a topos. PreprintJanuary1972 and publication1974 are distinct dates. Internal latticeExt vanishing is local, not global.',
 ['Deligne1974HodgeIII','Deligne1972HodgePreprint'],'Established mathematics; a clear commentary matching the manuscript’s individual rigidifications is worthwhile.')
prob(80,'Exactness of the Tate inverse limit',[284,285],
 'Pass to the limit overn=ell^nu in the torsion realization sequences.',
 'First use the finite exact sequence0→G[n]→Vn→M/nM→0, then verify surjective transitions/ML on geometric realizations before taking limits.',
 'Deligne10.1–10.2 supplies the1-motive setting; Milne16 supplies compatible torsion systems. Arbitrary sheaf inverse limits or global sections need separate derived-limit control.',
 ['Deligne1974HodgeIII','Milne1986Abelian'],'A small proof task can close this under standard1-motive hypotheses; the unqualified sheaf version should remain conditional.')
prob(81,'Gluing finite torsion pairings',[286],
 'Local morphisms induced from the derived class should glue to a globally defined pairing.',
 'Check independence of lifts, compatibility on overlaps and transition powers before forming theell-adic pairing.',
 'Deligne10.2.5 gives an explicit characteristic0 construction. SGA7VIII2.2–2.3 supplies finite-level pairings and signs. These are exact comparators with their hypotheses retained.',
 ['Deligne1974HodgeIII','SGA7VIII'],'Worth a bounded explicit calculation; it complements, rather than follows solely from, the derivedExt class.')
prob(82,'Orthogonal graded pieces and perfectness',[287,289],
 'The induced pairings are those one expects; conclude perfectness from the filtration.',
 'Identify each graded pairing and prove the resulting filtered map to the dual is an isomorphism by induction on the filtration, over the actual coefficient ring.',
 'Deligne10.2.5–10.2.6 identifies dual1-motive pairings; Milne16 verifies the abelian part. The independent filtered proof is inreview.md; rank counts alone are inadequate.',
 ['Deligne1974HodgeIII','Milne1986Abelian'],'Useful commentary already largely settled; integral kernels and sign normalization remain the worthwhile details.')
prob(83,'Curve duality and characteristic-p coefficients',[293,294],
 'The table compares roots of unity,constant coefficients andFrobenius kernels/cokernels; their coefficient symbols remain uncertain.',
 'For a smooth proper geometrically connected curve use the correct Kummer or Artin–Schreier sequence, topology, degree term andfinite-flat Cartier dual.',
 'SGA4XVIII1 supplies the relative curve-duality setting; Stacks03PK and0A3J state the exact coefficient sequences. Thep-coefficienti_p/alpha_p andzeta/mu symbols need ink checks.',
 ['SGA4XVIII','Stacks03PK','Stacks0A3J'],'Worth a scan-supported coefficient table; do not infer coefficient identity from expected duality.')
prob(84,'Picard, Albanese and the direct-limit coefficient',[296,297,298],
 'Kummer comparisons are passed to inductive and projective limits, withQ written in the direct-limit formula.',
 'For the standard inclusionscolimZ/n=Q/Z; the corresponding cohomology statement needs connected Picard andtorsionNS terms distinguished.',
 'Milne15–16 andKummer theory give the finite systems. The rational coefficient is incompatible with the indicated torsion limit under standard conventions; C-SA13-274 andreadings.tsv record the alarm without editing the source.',
 ['Milne1986Abelian','Stacks03PK'],'High-value scan check becauseQ versusQ/Z changes the object completely.')
prob(85,'Abelian torsors and singular Picard duality',[299,300,307],
 'GeneralizeH1(X,A) and itsPicardExt comparison to singularX; higherPicard terms appear.',
 'Keep the smooth-base torsion theorem separate from singular extensions. Specifyétale/fppf topology, Picard complex andrelative versusabsolute cohomology.',
 'SGA4XVIII1.2.9(b),p497 gives torsionH1(X,A) for smoothX andabelianA viaRaynaudXIII2.6. A nodal curve glued by infinite-ordertranslation gives an explicit nontorsion torsor; theRealBrauer example only refutes the absoluteH^{≥2}(Gm)=0 reading.',
 ['SGA4XVIII','MOAbelianTorsion','Stacks03R1','MehidiPoiret2025'],'Substantial and worthwhile only after choosing a precise singular-duality statement; the unrestricted formula is not a settled theorem.')
prob(86,'Affine coefficients and Cartier-dual Picard formula',[302],
 'For affineG, shouldH1(X,G) be described byHom of a dual group intoPic?',
 'The finite locally free relative formula isR1f_*G=Hom(GD,Pic_X/S) under proper flatfinite-presentation anduniversal f_*O=O. Arbitrary affineG needs a different dual object.',
 'Raynaud1970Picard6.2.1,p50 is exact. Mehidi–Poiret2025 extends a finite-flat nodal framework; neither proves the unrestricted absoluteformula. Ga has nontrivial infinitesimal characters, so pointwise arguments do not refute formal duality.',
 ['Raynaud1970Picard','MehidiPoiret2025'],'Worth a modern precise reformulation, beginning with the finite-flat case and a carefully defined formal dual.')
prob(87,'Exchanging cohomology and internalHom/Ext; higherPicard',[304,305,307],
 'The Hom/H1 andExt/H1 comparisons carry question marks; a proposed degree2 direct sum is explicitly denied.',
 'Build the derived comparison first and retain all spectral-sequence differentials and filtration extensions. Forfinite freelatticegamma theHom exchange is elementary.',
 'Stacks20.43 gives a bounded local-to-globalExt model; Deligne10.2.1 supplies the complex-biextension context. The unspecified site andadjunction prevent identifying the broad abutment in the draft.',
 ['Stacks0BQP','Deligne1974HodgeIII','SGA4XVIII'],'High value as a formulation task; the first step is fixing the exact functors, not guessing a direct-sum formula.')
prob(88,'Cancelled birational extension of a divisor',[306],
 'A whole argument extending a divisor from a dense open through a birational map is cancelled.',
 'Normality gives codimension-one control; local factoriality is needed to turn every extendedWeil divisor into aCartier divisor. The intended Picard theorem must first be recovered.',
 'The independent codimension-one argument is analysed inreview.md. No exact printed theorem with the missing hypotheses was identified in the searched references.',
 ['Robert2023'],'Low priority until the intended theorem is identified; cancellation is evidence against treating the paragraph as a completed proof.',
 'The author strikes out the entire proof, but gives no surviving explicit reason for the cancellation.')
prob(89,'Shriek adjunction and shifted abelian duality',[309,310],
 'Define or interpretf!,f^! and a shifted duality beside higherPicard objects.',
 'State the categories, dualizing complex, shifts and adjunction maps explicitly. The pointed-map splitting alone does not determine a six-functor theorem.',
 'SGA4XVIII develops a precise duality framework; Deligne10.2.1 gives a narrower derived biextension theorem. Neither is automatically the unfinished statement on36:043–044.',
 ['SGA4XVIII','Deligne1974HodgeIII'],'A coherent reconstruction could be valuable, but the first task must be a source-based definition audit.')

prob(130,'Witt stable part versus Frobenius fixed points',[311,312,313],
 'A cancelled stable-part pairing is replaced by Frobenius fixed-point expressions involvingW_n andW_infinity.',
 'Use thefiniteArtin–Schreier–Witt sequence withgeometric base conventions, and state inverse-limit continuity before comparingW-stable andétale fixed parts.',
 'Stacks0A3J gives theH0 obstruction atlevelp;SGA7XXII1 definessemilinear stableparts;Oda1969 provides thePicard/Dieudonné trail. The draft’sW_infinity notation is not uniquely identified.',
 ['Stacks0A3J','SGA7XXII','Oda1969'],'Worth an exact finite-level formulation; the arithmeticH0 term is already a concrete check.')
prob(131,'Arithmetic versus geometric fundamental group and torsion-free object',[314,315,316],
 'The inverse-limit notation is read arith; the page saysA has no torsion whileusingtorsion ofA.',
 'Use thegeometric fundamentalgroup/Tate module of a pointed abelian variety; an arithmetic fundamental group includesGalois. Check whether the torsion-free object isNS(A), notA.',
 'Milne15.3 and16 verify the geometriccover and pairing statements. Apositive-dimensionalA hasell-torsion for everyell≠char, giving a decisive reading alarm.',
 ['Milne1986Abelian'],'High-value scan check; these two changes affect the claimed realizations, not just typography.')
prob(132,'Reconstructing biextensions from restriction and finite pairings',[317,320,321],
 'GivenP′⊂P anddivisibleQ, recover the biextension from its restriction andthe compatible finite torsion pairings; iterate in both variables.',
 'Formulate an equivalence of Picardgroupoids withthe finite-level system retained andthe exact asymmetric divisibility hypotheses stated.',
 'SGA7VIII1.3,1.4 and2.2.8 identifyTor/torsion data;VII2.7 gives the long exact biextension framework. The full categoricalgluing proposition withthe manuscript’s exact hypothesis is not certified merely by these component results.',
 ['SGA7VII','SGA7VIII','Deligne1974HodgeIII'],'High value: a derived-category proof with explicitmorphisms could settle the exact surviving reconstruction statement.')
prob(133,'When Tate limits lose finite biextension data',[322],
 'The projective-system statement does not work after passing to modules without strongerdivisibility hypotheses.',
 'Retain the compatible family of pairings; seek sufficient hypotheses under which this family is recovered faithfully fromthe Tate modules.',
 'C-SA13-295 givesP=Z/ell,Q=G=Q_l/Z_l:TP=0 butBiext1(P,Q;G)≠0. SGA7VIII1.3 explicitly uses systems. This confirms a real distinction, not merely a notational preference.',
 ['SGA7VIII','Deligne1974HodgeIII'],'A bounded exact criterion forfaithfulness of the limit functor would be worthwhile; the basic counterexample is already checked.',
 'The author explicitly retracts the unqualified module formulation and retains finite pairings without passage to the limit.')
prob(134,'Primitive torsors, extension laws and generalizedNS',[324,326,327,329],
 'Under rigidity, aretorsors withzero-section trivialization exactlyextensions when theirclasses areprimitive; what is theNS quotient?',
 'Assume universalvanishing of allpointed mapsA_T→G_T. Then a normalizedprimitive multiplication is unique andcoherent; identify the quotient withclassicalNS only undergeometric hypotheses.',
 'The independent proof inreview.md verifiesfullfaithfulness, image andLeraysplitting. SGA7VII–VIII is thepublished extension/Picard setting; thedirectcontinuation36:054–058 ischecked inlinks.',
 ['SGA7VII','SGA7VIII','Stacks0BQP'],'Worth a clear categorical commentary; the exact rigidity hypothesis is the central correction.')
prob(135,'Identify the reused Lie-algebra source',[330,331,332,336],
 'The notes seek the origin of printedpage98,no316, with exponentialderivations andLevi factors.',
 'Locate the exact edition before attributing the page;retainfinite-dimensionalcharacteristic0 hypotheses for the standardLie assertions.',
 'HigherLeibniz,exp(adN),idealpreservation andLeviimages are independently checked. TheBourbaki family is only an unverifiedbibliographic candidate, not an attribution.',
 ['BourbakiLieCandidate'],'A short bibliographicfingerprint task is worthwhile; it should notbe confused with reproving the standard mathematics.')
prob(136,'IdentifyT.F and compare Čech conventions',[333,334,335,336],
 'The reusedtypescripts citeT.F.II§5Th10.2 andwarn that equivalence depends onP(empty)=0.',
 'Fix the covering-sieve convention andempty-object value, then compareexact definitions;left exactness is the surviving correction.',
 'Stacks21.10 verifies the modern sheaf/presheafinjective comparison. Godement1958 remains an unverifiededition candidate; the preciseT.F reference is not recovered.',
 ['Stacks03AV','Godement1958Candidate'],'Useful exact-source work; the empty-cover convention can alterČechH0 even when ordinary sheafcohomology agrees.')
prob(137,'Relative cycle classes and proper intersections',[346],
 'Cycleclasses require restrictive hypotheses andthe writtenintersections mustmake sense.',
 'Work first withsmoothprojectivevarieties overa field andrationalChowgroups, orstate explicitrelativecycle-class hypotheses. Check thefibrewise codimension sign on the scan.',
 'SGA7IIXX1.6 is thedirectpublishedcounterpart andretainscycle-class assumptions; it does not license the literal≤n iftheargumentrequiresproperintersection.',
 ['SGA7XX'],'A scan check andshorthypothesis comparison can fully clarify thispart of the argument.')
prob(138,'Algebraic inverse and the lift-to-characteristic0 parenthesis',[347],
 'Conditiona is expected fromstandardconjectures;the parenthesis claimsLambdaalgebraic forpolarizedlifts tocharacteristic0.',
 'Algebraicity ofthe inverseLefschetzcorrespondence is the separateLefschetzstandardconjecture; hardLefschetz orlifting alone doesnotprove it.',
 'SGA7IIXX3.3–3.4,Milne2022 andAnconaEtAl2025 explicitly preserve thisdistinction; the2025 theorem proves specialHK/Lagrangian cases.',
 ['SGA7XX','Milne2022Standard','AnconaEtAl2025'],'Thegeneralconjecture istoo broadforone run; auditingthisparenthesis is both feasible andimportant.')
prob(139,'Curve-level motivic summand versus a cohomological condition',[348],
 'Conditionb is interpreted as absenceof the largestlevel1submotive ofcoker(i*), assumingmotivic yoga.',
 'Use theprecisecorrespondence-generated subspace anditsGaloisstability; do notassume anunconstructedmotivicprojector.',
 'SGA7IIXX3.2 gives thecohomological version. ACV2017 modelsoddcohomology byabelianvarieties underexplicitmaximalgeometricconiveau assumptions, not in everymotiviccategory.',
 ['SGA7XX','AchterCasalainaVial2017'],'Worth a terminologyreconciliation acrossrealizations; no newgeneralstandardconjecture should be claimed.')
prob(140,'Can shrinking the regular base be omitted?',[350],
 'The restriction toanonemptyopen is probablyunnecessary.',
 'First retainshrinking,finiteextension andtrace;removing itrequires extension ofcycles/correspondences andcontrol ofboundaryLerayclasses.',
 'SGA7IIXX4.4 usesfiniteextension,normalization andnonemptyopens in theactualpublishedargument. Noexactunconditionalno-shrinking theorem wasidentified.',
 ['SGA7XX'],'A good boundedresearch question afterfixingrelativecycleclasses; boundaryobstructions should be tested first.')
prob(141,'Griffiths injection and the precise quotient conclusion',[351,352,353],
 'The blow-upcalculation iscalledtrivial;theGriffithsgroup is said tocontain primitivealgebraiccohomology.',
 'UseXVIII5.8.4/7 with(LV),(A), thenXX4.1and5.1. Record thecanonicalquotientofasubgroup andthe resultingdimensioninequality.',
 'Theexactpublishedtheorems settle theproperlyhypothesizedclaims. Acanonicalembedding doesnotcome fromtheargument;anabstractQ-vector-spaceembedding isnoncanonical.',
 ['SGA7XVIII','SGA7XX'],'Establishedresult deserving precisecommentary, withlittle need fornewresearch.')
prob(142,'High-degree vanishing cohomology in positive characteristic',[354,364,366],
 'Sufficientlygeneralhigh-degreepencils shouldhave no curve-levelvanishingpart;7.4strengthens this tomaximallevelin alldimensions.',
 'Distinguish positivecoherentHasse–Witt rank,unboundedrank,andabsenceofpositivecorrespondenceconiveau;thelast followsfromenoughunitroots afteraccountingforfixedambientfactors.',
 'KatzSGA7XXI1.4 provesnonnilpotenceforCMsections;XXI4.2 provesnonconiveau forcompleteintersections. Koblitz1975I§5Theorem2 givesstable-rankgrowth. Theprecisegeneralunit-rootdeduction isanalysed inreview.md without claiming the strongerall-traces theorem.',
 ['SGA7XXI','SGA7XX','Koblitz1975'],'Highinterest: one researchrun canwrite theexactmodern deduction andidentify its earliestpublication, avoidingthemanuscript’s tracegap.')
prob(143,'Specialization of motivic level',[357],
 'Theauthor cannotshowingeneral, evenassumingstandardconjectures, thatleveldecreases underspecialization.',
 'For a fixedcorrespondence realization,spread itoveranopenafterfiniteextension. A theorem ateveryspecialization requires agood-reduction orcycle-extension mechanism.',
 'SGA7IX5.13 givesabelian/BTgoodreduction;SGA7XXI2.2 givesfinite-fieldconiveaudivisibility. Neither is a universal theorem for anundefinedmotiviccategory.',
 ['SGA7IX','SGA7XXI'],'Worth formulatingfor oneprecise categoryandfamily; theunqualifiedquestion istoo ambiguous for a yes/nofate.')
prob(144,'Does Frobenius divisibility characterize curve level?',[358],
 'Divisibility byq^{n−1} may beequivalenttolevel1.',
 'Necessity followsfromintegrality andtheTatetwist. Sufficiency requiresalgebraiccorrespondences andbelongs togeneralizedTate/coniveautheory.',
 'SGA7XXI2.1–2.2 prove thenecessarydirection. Milne’sstandard-conjecture discussion isconditional;noexactunconditionalconverse wasfound.',
 ['SGA7XXI','Milne2022Standard'],'Deep buttoo broadforafewhours; firstrestrict totheactualvanishingrepresentationandknownspecialcases.')
prob(145,'Strong versus subspace traces in theorem7.1',[359,367,372],
 'Thewhole-traceclaim ismarkedunproved;aninsert allowsaninvariantsubspace,andstrongconsequences aredeleted.',
 'Separate thetwostatements. Theweakassertion alone givesneithernon-p-groupimage norvariationofwhole-spacetrace.',
 'Thetrivial-groupFp^{p−1}example independentlyrefutes theimplication. SGA7XXII1 andKoblitz1975 do notstate theevery-whole-trace assertion.',
 ['SGA7XXII','Koblitz1975'],'Veryhigh editorialvalue;thelogicalgap is settled,while the stronggeometricstatement merits itsownliteraturetask.',
 'Theauthor explicitly writesnotprovedunderthisstrongform andcrossesouttheclaimedconsequences;this is direct evidenceof retraction oftheproof, notoffalsehoodofthetheorem.')
prob(146,'Every residue on every dense parameter open',[360,361,364],
 'Cor7.2 claimseverypoint-countresiduemodp onanynonemptyopen andsays itsproof is equivalenttostrong7.1.',
 'Chebotarev realizesconjugacyclasses oftheactualfiniteGaloisimage;itrequires thedesiredwhole-spacetrace andappropriatearithmeticconstant-fieldcompatibility.',
 'SGA7XXII3.1–3.2 giveexacttracecongruence. Theweaksubspacelemma doesnotfulfillChebotarev’sinput;noexactgeneralsource forthefulldistribution assertionwasidentified.',
 ['SGA7XXII','Koblitz1975'],'Worth a separatefinite-monodromyresearchtask; the point-count congruencealone doesnotsettleit.',
 'Themargin explicitlysaysthecorollary isnotprovedanddependson theunprovedstrongform.')
prob(147,'Cohen–Macaulay vanishing and stable-rank spreading',[362,363,371],
 'Negative-twistvanishing andEGAIII7 areinvoked;reductiontofinitefields iscalledwithoutdifficulty.',
 'UseCMduality,Serrevanishing andtheeffectiveCartierrestrictionsequence;shrink forconstantstablerankbeforeforming thefiniteétaleFp-representation.',
 'Koblitz1975I§2,Lemma4 explicitlychecksflatness/basechangeandgenericstable-ranksemicontinuity. SGA7XXII1 suppliessemilinearFrobeniusfixedloci. Thesevalidateprecisepieces,notallstrongtracequantifiers underarbitraryspreading.',
 ['Koblitz1975','SGA7XXII'],'A usefultechnicalappendix isfeasible; theall-traces reductionremains aseparateclaim.')
prob(148,'Correspondence niveau and support coniveau',[366],
 'Thetwofiltrationdefinitions shouldagree, buttheargumentwoulduseresolutionofsingularities.',
 'Specifyproperness,smoothness andcoefficients. Forpropersmoothcomplexvarieties withQ-coefficients,equality followsfromDeligne;integralprojectiveandrationalopenversions canfail.',
 'Benoist–Ottem2021 introduction andTheorem1.1 explicitlystate thisboundary andconstructcounterexamples. SGA7XXI2.2 provesdivisibility forthecorrespondencefiltration;arbitrarypositive-characteristicintegral equalityisnotinferred.',
 ['BenoistOttem2021','SGA7XXI','Deligne1974HodgeIII'],'Highvalue as a precisehypothesismap; a generalnewproofis not thegoal ofone run.')
prob(149,'Special Frobenius representation and the generic-point hypothesis',[367],
 'Lemma7.8 asserts the special representation occurs inside the one at any generization t after an open subgroup; it reduces without proof to an integral henselian base with generic point t.',
 'Require t to be the generic point of a normal integral base, or require a normal specialization closure and preservation of the special residue representation. Normality of the ambient S alone is insufficient.',
 'C-SA13-355 is refuted by S=Spec F3[x,x^-1,y], F(v)=xv^3, t generic on y²=x(x−2)², s=(2,0): the generic fixed representation is trivial and the special image is C2. C-SA13-363 proves the repaired generic-point case via the étale fixed locus, its henselian finite part, and descent. Stacks0BTN,04GK,02LP and SGA7XXII1 are the opened exact comparators.',
 ['SGA7XXII','Stacks0BTN','Stacks04GK','Stacks02LP'],'High value for source commentary: check whether the ink intended a generic point or normal specialization closure; the literal arbitrary-point theorem is false.',
 'The manuscript supplies only the henselian reduction. The lost normality of a specialization closure explains precisely why that reduction is invalid in the literal generality.')
prob(150,'Arbitrary rational-point count and the numerical degree bound',[368,369],
 'Lemma7.6 prescribesexactlyNpointsforallsufficientlylarged andtheproofsuggests anexplicitthreshold.',
 'High-degreehomogeneousinterpolationatallX(k′)points provesexistenceafterfiniteextension. Theclaimedsharperbound needs asame-degreepoint-selection constructionandtheinequalityN≤r d1^n.',
 'SGA7XXI1.2–1.4 validatesnorm-formconstructionsforzero/onepoint;Koblitzusesrelatedsingularsections. Thegeneralexistenceproof isgivenindependentlyinreview.md,withno unsupportedbound.',
 ['SGA7XXI','Koblitz1975'],'Worth a boundedimprovementtask: firstfindthebestcorrectbound for fixeddegreeanddimension.')
prob(151,'Norm forms and singular sections',[370],
 'Theauxiliaryforms have nontrivialdegree butno rationalzero,andgeometricallysplitintolinearfactors.',
 'Restrict a finite-fieldnorm to aninjectivelinearsubspace;thecompositionmakes thezero setanintersectionoverk butusuallyreducible/singulargeometrically.',
 'SGA7XXI1.2 explicitlyuses suchforms;thegeneralnormproof andfiniteexamples areindependentlychecked. Smoothness cannotbe addedtoLemma7.6’sconstruction.',
 ['SGA7XXI'],'Theconstruction issettled;commentary shouldexplainwhy itnecessitatesthelargeproper-sectionopen.')
prob(152,'Two traces and better coprime-degree bounds',[372],
 'Two traceswouldsufficeforthegeometricapplication;coprimeproductdegrees mightimprovethebound.',
 'Requiretwo whole-spacetraces. Coprimeintegersgenerateallsufficientlylargeintegersafterlowerbounds,butdisjointgeometriczero setsareadditionaldata.',
 'Thep-grouptracelemma andcoin-argument areindependentlyproved;SGA7XXI/Koblitzdonotverifythemanuscript’spreciseimprovedbound.',
 ['SGA7XXI','Koblitz1975'],'A concretefinite-fieldconstructionproblem isfeasible;do notmergeitwiththeunprovedstrongmonodromyclaim.')
prob(153,'Heuristic crystalline comparison heading',[373],
 'Relationsheuristiquesbetweencrystalline,quasi-/topo-crystallineandvanishingcohomology;notesgiventoBerthelot.',
 'No theorem can be stated untilthemissingnotes andtheuncertainprefixareidentified.',
 'Oda1969 andSGA7XXII providecontextbutnoexactstatementto match. Thepagecontainsaprogrammeheadingonly.',
 ['Oda1969','SGA7XXII'],'Low prioritymathematically untilthenotes arefound;highprovenancevalue forlocating theBerthelotcontinuation.')
prob(154,'The omitted global compatibility of f_!',[295],
 'The programme proposes a localf_! and asksforitsglobalcompatibility.',
 'Fix thetopologies,relativeobjects,coefficients andthelocal-to-globalcomparison beforeasserting anadjunction.',
 'SGA4XVIII is a precise laterdualityframework,buttheunfinished36:037programmeisnot identifiedwithaspecific theorem.',
 ['SGA4XVIII'],'A formulationtask isworthwhile onlywiththeadjacentPicardprogramme; no standalone theorem isrecoverable.')
prob(155,'Ordinary factor lifting and a generically simple deformation',[269],
 'Thelargestordinarysubvarietyneednotlift;deform anordinaryellipticfactortimesanonordinaryone toasimpleabeliansurface.',
 'Construct anabelianscheme withthisspecialfibre andgeometricallysimplegenericfibre;thenanordinaryelliptic algebraicsubvarietycannotlift. FormalandBTsubgroups aredifferentquestions.',
 'Thepage’scontradictionisvalidconditionalonthefamily. Koblitz1975IVdeformation/p-rankstrataandtheSGA7IXreductionframework areprimaryleads,butthisrunhasnotcertifiedtheexactfamilywiththerequiredliftingnotion.',
 ['Koblitz1975','SGA7IX'],'Highvalue forone researchrun: anexplicitfamily ormodulitheoreticexistenceproof wouldturnthearchive sketchintoacompletecounterexample.')
