"""Hand-authored claim records after complete reading, not keyword verdicts.
Imported by build_deliverables.py. Every location is resolved to the original
transcription's line numbers; the named scan remains the primary locator.
"""
from pathlib import Path
import re

ROOT=Path('/workspace/scratch/4017236f14bf')
TEXTS=ROOT/'sources/texts/codex'
CLAIMS=[]
EVENTS=[]
GROUPS={
 'order': {'searches':['S67-01','S67-04','S67-09','S67-10','S67-12'], 'refs':['Speed1968','Massas2023'], 'description':'complete join-prime/downset representation and complete homomorphism literature; Raney and de Jongh–Troelstra followed backwards; custom atelier wording also searched'},
 'atelier': {'searches':['S67-02','S67-03','S67-05','S67-11','S67-12'], 'refs':['CSGUnpublished','Malgoire2002','CruzMorales2021'], 'description':'exact VGF, atelier, magasin, multiombre, Prat and ML terminology; zbMATH/arXiv/MathOverflow/Numdam searches, Montpellier archive and CSG bibliographies'},
 'glue': {'searches':['S67-02','S67-05','S67-08','S67-11'], 'refs':['SGA4II','Esquisse1997','CSGUnpublished'], 'description':'atelier refinement/subdivision and gluing terms; SGA4 ExposéII §§1–2, EGA metadata/search and Esquisse §5 compared without equating their objects'},
 'triang': {'searches':['S67-05','S67-06'], 'refs':['Lojasiewicz1964','Baro2010','Esquisse1997'], 'description':'relative/simultaneous triangulation, Hironaka/Łojasiewicz bibliographies and normal triangulation; comparison made to exact extension/uniqueness hypotheses'},
 'support': {'searches':['S67-01','S67-07','S67-09','S67-10','S67-11','S67-12','S67-13'], 'refs':['LindenhoviusVetterlein2023','Janowitz1963','Ore1944'], 'description':'orthogonality closures, Dacey spaces, orthomodularity, Grothendieck virtual supports and singleton representations; Ore1944 primary article text checked in reproduction, original Dacey thesis sought but not obtained'},
 'simplicial': {'searches':['S67-01','S67-05','S67-06'], 'refs':['Stanley1991','Lojasiewicz1964'], 'description':'simplicial-poset Boolean interval characterization and subdivision/triangulation literature; exact weak criterion compared'},
}

def locations(cote,spec):
    out=[]; scans=[]
    for folder, selected in spec:
        name=f'J156-{cote}-{folder:02d}_transcription.tex'
        lines=(TEXTS/name).read_text().splitlines()
        marks=[(i+1,int(m.group(1))) for i,line in enumerate(lines) if (m:=re.search(r'\\scanpage\{(\d+)\}',line))]
        for j,(start,scan) in enumerate(marks):
            if scan in selected:
                end=marks[j+1][0]-1 if j+1<len(marks) else len(lines)
                out.append(f'{name}: scan {scan}, lines {start}–{end}')
                scans.append(scan)
    return out,sorted(set(scans))

def C(cote,num,spec,his,statement,status,group='atelier',cls='D',fate=None,refs=None,computation=None,confidence='medium',check=None,date=None):
    cid=f'C-SA21-{cote}-{num:03d}'
    lines,scans=locations(cote,spec)
    g=GROUPS[group]
    if fate is None:
        fate=f'No exact later published theorem with these atelier hypotheses was identified in {", ".join(g["searches"])} ({g["description"]}). The cited material supplies historical evidence or an explicitly limited comparison, not a resolution. D records this bounded negative search, not proof of absence.'
    CLAIMS.append(dict(id=cid,items=[],cote=f'156-{cote}',scans=scans,lines=lines,his_statement=his,
        statement=statement,status_on_pages=status,computation=computation or 'No numerical computation is asserted on these pages. Algebraic arguments are distinguished from the finite certificates; no machine verification is claimed unless identified here.',
        **{'class':cls},fate=fate,fate_date=date or {'searched_as_of':'2026-11-19','first_circulation':None,'publication':None},
        present_status=f'As of 2026-11-19: {check or status} Search family: {group}; exact hypotheses are stated in this record and formalism_and_checks.md.',refs=refs or g['refs'],confidence=confidence))
    EVENTS.append({'statement_id':cid,'date':'2026-11-19','who':'GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7','type':'carried as background without fault found','outcome':'Complete source passage and short note read. This event records use of the statement, not an independent proof. '+(check or status)})
    return cid

# Cote 156-6, all twelve supplied folders, scans2–94.
C(6,1,[(1,range(2,10)),(2,[12,15,17])],
  'Deployment and (1.20): “X≤Sup_i F_i ⇒ ∃i ...”; “F≤G ⇔ ~F⊂~G”.',
  'Under At1 and At2 with complete join-prime elementary figures, F↦~F is injective and order-reflecting, sends existing bounded joins to unions and nonempty meets to intersections, and identifies the subfigures of F with all lower subsets of ~F. Incidence X◁F means X∈M and X≤F; it is transitive but reflexive only on M. The local-to-global formulation is the analyst’s explicit restatement; VI12 strengthens the earlier IV definition.',
  'Proof/recall from earlier chapters; VI12 marginally corrects incidence from an order to a transitive nonreflexive relation.', 'order','E',
  'The complete join-prime representation mechanism predates1986: Speed1968 §4 CorollaryC and §5 final corollary pp727,730, tracing Raney1952 and Balachandran1953. Massas2023 Theorem2.30 gives the modern downset duality. The locally bounded atelier formulation is a direct restriction of this mechanism, not an identified separately published Grothendieck theorem.',confidence='high',check='Valid with the stronger complete join-prime definition. Do not transfer it unchanged to IV’s equality-only irreducibility.')
C(6,2,[(1,range(2,10)),(2,[10,11,13])],
  'Large and small shadows, multiombres, “un lieu est une figure non vide dont le seul raffinement non vide est elle-même”; (1.24).',
  'Given the two orders, define Omb(F)={X∈M:X≪F}, omb(F)=Omb(F)∩L, and the multiombres from the individual stratum shadows. L is the set of minimal nonzero refinement objects. Disjointness is compatibility plus zero face intersection. The stronger suggested characterization “a refinement supremum exists and refinement infimum is zero iff disjoint” is a separate unverified assertion, not part of these definitions.',
  'Definitions and elementary consequences; refinement-order characterization of disjointness explicitly marked “Vérifier” on scan13.',check='Definitions identifiable; the marked refinement-supremum equivalence is not independently proved here.')
C(6,3,[(3,[18,19,20]),(7,[56,57]),(8,[58])],
  'Finite-type figures and reconstruction from M with hereditary compatibility.',
  'For a poset M with reflexive symmetric compatibility hereditary under ≤, the candidate figures are finite unions of principal lower sets generated by compatible elements; joins are unions when compatible. To satisfy closure under every subfigure while keeping every figure of finite type, each lower subset of every admitted finitely generated ideal must itself be finitely generated. The latter requirement is an analyst-explicit hypothesis, and must not be silently inferred from finite generation of the original ideal.',
  'Construction stated and elaborated; finite type and finite deployment are not consistently separated.',check='Construction is conditional on hereditary finite generation. The unrestricted finite-type slogan is insufficient.')
C(6,4,[(2,[11,14]),(3,[21])],
  '(1.29) “G≪F ⇔ ∃F′ ... G≤F′≼F”; later “ne supposerai plus”.',
  'The earlier axiom generated refinement from face inclusion and subdivision. The revised theory takes ≤ and ≪ as independent nested partial orders and defines subdivision later through orthogonality profiles. Therefore generation of ≪ by ≤ and ≼ is no longer an asserted theorem of the revised axioms.',
  'Explicitly corrected/withdrawn by the author: marginal notes at VI11,14 point to the change on VI21.',check='Withdrawn within the manuscript; later claims must use the revised data.')
C(6,5,[(3,[22,23,24,25]),(4,[26,29])],
  '“grande multiombre”; admissibility, preservation of compatible operations and reflection of refinement.',
  'For At1–At7, assign to F the set figure {Omb(X):X≤F elementary}. At5 gives least receiving strata and nonempty open strata; At6 gives order reflection within compatible families; At7 supplies composition. The assignment is injective, preserves face order and existing joins/meets in a compatible ambient figure and disjointness, and reflects refinement. The converse reflection of arbitrary set-figure compatibility is not claimed: two incompatible lieux already obstruct it.',
  'Proof sketched across scans22–29; an initially missing At7 is added on scans27–28; set-theoretic compatibility questions left for later.',check='The construction and proof dependencies are recorded; no independent proof of every At* converse is claimed.')
C(6,6,[(4,[26,27,28,29])],
  'Maps φ_F:Omb(F)→~F and the need for “At7”.',
  'For X refining F, φ_F(X) is its least elementary receiving face. Under At7, these receiving maps compose along F′≪F: φ_F(X)=φ_F(φ_F′(X)) whenever X≪F′. Conversely the intended compositional property requires the transitivity of immediate refinement; it is not a consequence of At1–At6 alone in the pages.',
  'Proof sketched, with the missing axiom recognized and inserted.',check='Axiom dependency repaired by the author; composition is used only with At7.')
C(6,7,[(4,[30,31,32,33]),(5,[34])],
  'At*1–At*5 and equivalence with families of set figures.',
  'The claimed representation identifies At1–At7 ateliers with families of admissible set figures on M, stable under subfigures and compatible unions, containing their elementary subfigures, and satisfying the displayed coherent restriction/refinement axioms At*1–5. This is an isomorphism/groupoid-level assertion unless morphisms are separately defined. It uses the large multiombre, not the small one. Exact At* conditions remain the displayed source formulas; no unlisted axiom is supplied by reconstruction.',
  'Construction and converse sketched; author hopes no axiom was forgotten.',check='Identifiable reconstruction claim, not independently certified in full. The open completeness concern is MP-SA21-6-03.')
C(6,8,[(5,[35,36])],
  'Small shadows forget affine versus piecewise-linear structure on an interval.',
  'The small-multiombre map may identify distinct elementary figures with the same underlying lieux and closed-stratum pattern: different affine/PL structures on an interval can have identical point shadows. Thus local subfigure-lattice faithfulness does not entail global injectivity or reflection of refinement/compatibility.',
  'Counterexample explained; later reused at VII58.',check='The logical distinction between local lattice isomorphism and global injectivity is sound; the geometric example is carried as described, without constructing its whole ambient atelier.')
C(6,9,[(5,[36,37])],
  'Pseudodisks, missing linking data and a hoped-for reconstruction.',
  'The pages propose supplementing shadows of pseudodisks with incidence/linking information to recover geometry. They do not specify a category of pseudodisks, an exact invariant or a reconstruction equivalence with quantified hypotheses. This cannot be converted into a theorem without adding analyst-chosen definitions.',
  'Programmatic open suggestion.',cls='F',fate='Searches S67-03,05,06,11 found historical VGF discussion and Esquisse §5 dévissage, but no formulation identifying this particular proposed invariant. Esquisse supplies a related motivation, not the missing statement.',refs=['Esquisse1997','CSGUnpublished','CruzMorales2021'],check='Not identifiable as a precise theorem from these pages; retain as a problem/program, not a false result.')
C(6,10,[(5,[38,39,40,41]),(6,[42,43])],
  'Lower sub-ateliers; “spacieux” and Env.',
  'A nonempty lower subset F′⊆F inherits bounded joins and elementary decomposition, hence At1–At2. If it is also stable under every ambient bounded join, it is spacious in this passage’s sense. Such subsets correspond to lower subsets M′⊆M by F′={F:~F⊆M′}, provided all corresponding admitted figure supports are retained; Env denotes this saturation. At3 needs an additional compatibility-closure condition, isolated separately.',
  'Proof sketched; broad inheritance claim corrected at scan43.',check='At1–At2 inheritance checked directly from lowerness; At3 is excluded without Sousat2.')
C(6,11,[(5,[38]),(6,[43,44])],
  '“At1, At2, At3” inheritance corrected to “Sousat1, Sousat2”.',
  'A lower nonempty subfamily need not satisfy At3. Correct inheritance requires Sousat2: whenever F,G belong to the subfamily and each elementary X≤F, Y≤G has a common upper bound in that subfamily, F∪G belongs to it. With this and inherited orders, At4–At7 then restrict as stated.',
  'Author corrects the earlier claim. False without Sousat2; the added condition is explicit.',computation='check_finite_examples.py, lower_subfamily_At3_failure; all subsets of {0,1,2} of size≤2, F={0,1}, G={1,2}. Every elementary cross-pair has its union, but F∪G is absent.',confidence='high',check='Counterexample independently checked and finite certificate saved. Corrected statement retains Sousat2.')
C(6,12,[(6,[42,44,45])],
  'Spacious envelopes and large-shadow image as a subatelier.',
  'For a specified subatelier, Env adds the figures whose complete deployments lie in its elementary set. The correspondence with lower M′ uses the ambient family of figures, not arbitrary subsets of M. The large-shadow representation is asserted to have subatelier image; whether that image is spacious is explicitly uncertain and must remain separate.',
  'Envelope construction sketched; spaciousness of the large-shadow image left open.',check='Envelope and image claims distinguished. The scan45 F′/F″ formula ambiguity remains in readings.tsv.')
C(6,13,[(6,[48,49]),(7,[50])],
  'A homomorphism of lattices of closed sets should be inverse image of an order map; sobriety discussion.',
  'For arbitrary posets P,Q, every h:Down(Q)→Down(P) preserving all joins and all meets, including bottom and top, equals f⁻¹ for a unique monotone f:P→Q. Sobriety is not required under these complete-homomorphism hypotheses. A statement with only finite meet preservation is different and is not silently substituted.',
  'Posed and partly argued; the direction and sobriety qualification are unsettled in the prose.', 'order','E',
  'Massas2023 Theorem2.30 (printed p14) states the precise duality, attributed to Raney1952 and de Jongh–Troelstra1966; Speed1968 §4C gives the complete prime/complete homomorphism mechanism. Original older papers were sought but blocked. Independent proof is in formalism_and_checks.md §2.',confidence='high',check='Independently re-proved for all posets and complete homomorphisms; empty operations explicitly included.')
C(6,14,[(6,[46,47]),(7,[52])],
  'At8 makes the small-shadow map locally bijective on subfigures.',
  'Assume At1–At8. For a fixed figure F, every elementary stratum has a nonempty open small shadow by At8; its closed small-shadow figure therefore has the same face poset as ~F. The map from subfigures of F to subfigures of its small multiombre is an order/lattice isomorphism. This is a statement within one fixed F and does not assert global injectivity over all figures.',
  'Proof sketched and used in comorphism discussion.',check='Local character preserved; global claims separated in C-SA21-6-008 and C-SA21-7-018.')
C(6,15,[(7,[50,51]),(1,[8,9])],
  'At8 for trivial ateliers: “minimal” or “successeur” of a minimal element.',
  'If the two stratum orders coincide, x∈L and x≪°X force x=X. Thus At8/L1 holds iff every stratum is minimal, i.e. M is discrete. The weaker condition that each stratum is minimal or immediately succeeds a minimal one is false as an equivalent criterion.',
  'False early formulation; corrected by author in VII scan35 line100.',computation='check_finite_examples.py, trivial_order_At8_counterexample: two-element stratum chain0<1.',confidence='high',check='Refuted as initially stated; corrected formulation independently proved in formalism_and_checks.md §5.')
C(6,16,[(7,[51,52])],
  'For f:E′→E, define f*F from the nonempty inverse images of the strata.',
  'The written recipe that retains every nonempty closed-stratum inverse image does not always produce an admissible set figure: distinct nonempty closed preimages may exhaust a larger one and leave its open stratum empty. A possible repaired pullback discards strata whose open-stratum preimage is empty; this is explicitly an analyst reconstruction, not the transcribed formula.',
  'Construction asserted without this degeneracy being handled.',computation='check_finite_examples.py, naive_figure_pullback_counterexample: closed strata {a},{b},{a,b,c}, pullback along {a,b}⊂{a,b,c}.',confidence='high',check='False as written under the chapter’s nonempty-open-stratum admissibility. Source formula remains unchanged pending scan check.')
C(6,17,[(7,[52,53])],
  '“coplongement” and locally surjective maps of subfigure lattices.',
  'For a comorphism preserving the stipulated operations, if each subfigure of the image of F comes from a subfigure of F and the map reflects refinement, then equality of two images implies equality of the original figures: equality gives both refinement comparisons, and antisymmetry applies. The face-order reflection conclusion additionally uses compatibility/local lifting as in the passage.',
  'Definition and argument sketched.',check='The injectivity consequence from reflection of a partial order is immediate; the complete local lifting construction is not independently certified.')
C(6,18,[(7,[53,54,55,56,57]),(8,[58])],
  '“quasi-ensembliste” and Atens1.',
  'In this version, an At1–At8 atelier is quasi-set-like when its canonical small-multiombre map reflects refinement; it suffices to test elementary figures using At4. The ensuing image conditions include all singleton loci, closure under subfigures and the stratumwise compatibility condition. This is a dated definition: VII later separates local set representation, global injection and refinement reflection, and modifies set refinement to strict refinement.',
  'Definition and reconstruction conditions stated; terminology is revised later.',check='Do not merge this definition with the weaker conditions labelled quasi-set-like in later VII without recording the change.')
C(6,19,[(8,[58,59])],
  'Finite-type spacious quasi-set ateliers and geometric compatibility.',
  'In the finite-type setting with hereditary finite generation and small-multiombre refinement reflection, spaciousness of the image is equivalent to using exactly the ambient set-figure compatibility relation on elementary figures, rather than a stricter hereditary subrelation. The statement concerns an admitted family stable under subfigures; binary meets of multistrata require a common lower bound unless zero is explicitly adjoined.',
  'Claim/translation stated; unqualified meet language raises a reading alarm.',check='Hypotheses made explicit; scan59’s unrestricted meet wording is not adopted.')
C(6,20,[(8,[60,61,62])],
  'Disjointness of F,G need not survive F′≪F, G′≪G under At1–At8 alone.',
  'The text constructs selective compatibility: refinements A′≪A and an object B may have A compatible/disjoint with B while A′ is incompatible with B. Refinement-stability of disjointness therefore needs an additional axiom. To call this a full At1–At8 countermodel, the ambient atelier and interior lieux must also be supplied; the manuscript notes that issue.',
  'Counterexample idea and axiom discussion; not a fully enumerated model on the page.',check='Recorded as an obstruction sketch, not an exhaustively verified At1–At8 counterexample.')
C(6,21,[(8,[62,63,64,65])],
  'At9, Atens2, At9′ and At9″.',
  'At9 requires disjointness iff all underlying lieu pairs are disjoint; Atens2 adds disjointness of distinct lieux. At9′ tests compatibility by orthogonality of exclusive shadows after removing the common face; At9″ additionally restricts the common face to empty or elementary in the polyhedral case. The text claims each stronger criterion implies At9. L3/At10 requires distinct compatible strata; the marginal abbreviated formula omits compatibility and is not used without it.',
  'Axioms introduced, implications stated and partially explained.',check='Definitions and hypotheses distinguish the variants. Full axiom equivalences remain a bounded-search D result.')
C(6,22,[(8,[65]),(9,[66])],
  'Restriction F′|G and “Inf≪(F′,G)”.',
  'Under At1–At7, F′≪F and G≤F give a restriction with deployment {X≤F′:X≪G}. This is a subfigure of F′, refines G, and is the greatest common lower bound of F′ and G in refinement order. The fixed common ambient figure and face relation G≤F are essential.',
  'Proposition with proof across scan65–66.',check='Proof followed with At7’s receiving-stratum composition; no assertion of arbitrary refinement meets outside this setup.')
C(6,23,[(9,[66,67])],
  'Restriction is a complete homomorphism on subfigure lattices.',
  'For fixed F′≪F, the map G↦F′|G from subfigures of F to subfigures of F′ is the inverse-image map along the least-receiving-stratum map ~F′→~F. It preserves arbitrary joins and meets inside these complete local lattices, including empty operations.',
  'Proof from the stratum map.', 'order','E',
  'This operation is inverse image on downset lattices, the standard complete-homomorphism construction verified in Massas2023 Theorem2.30 and Speed1968 §4. Its atelier instantiation is proved locally in VI.',confidence='high',check='Independent set-theoretic check: inverse images preserve all unions and intersections.')
C(6,24,[(9,[67,68,69,70])],
  'At11: “recollement” of refinements.',
  'If F=∨_iF_i is an existing cover by subfigures and local refinements G_i≪F_i have equal restrictions on each F_i∩F_j, At11 asserts existence of a unique global refinement G≪F with G|F_i=G_i. The compatible union is the candidate global figure; existence for an infinite family is a real additional condition, not supplied by pairwise compatibility alone.',
  'Axiom and equivalent gluing formulation argued.', 'glue',check='Axiom/construction distinguished; SGA sheaf gluing is only a formal comparison, not a proof of existence in an arbitrary atelier.')
C(6,25,[(9,[68,69]),(10,[79,80]),(11,[81])],
  'At11′ and corrected implication diagrams.',
  'The binary compatibility criterion At11′ implies gluing over finite subfigure covers by induction. It does not imply arbitrary infinite gluing unless the corresponding increasing compatible joins exist. VI79–81 explicitly separates this existence condition into At11bis.',
  'Self-corrected diagrams; the original implication to infinite gluing is deleted.', 'glue',confidence='high',check='Finite versus infinite quantifiers preserved; the deleted stronger implication is not retained.')
C(6,26,[(9,[70,71])],
  'Refinement of a disjoint union as product of refinements.',
  'Assuming the relevant At11 gluing and disjointness stability, for an existing pairwise disjoint union F=∨_iF_i, restriction gives a bijection/order correspondence between refinements of F and compatible local refinements of all F_i, with inverse their union. An infinite product statement needs the infinite At11 existence hypothesis.',
  'Corollary/proof sketch of gluing.', 'glue',check='Conditional result, not an unconditional arbitrary-product assertion.')
C(6,27,[(9,[71,72])],
  'Discrete figures and the criterion for a collection of lieux to be a figure.',
  'A finite family of pairwise disjoint lieux has a discrete figure as its join under the stated compatibility axioms; its face lattice is the powerset of those lieux. For an arbitrary collection A⊆L, if its restrictions to all strata of an existing cover are admitted figures and compatible on overlaps, At11 produces the global figure. Infinite existence is not automatic.',
  'Examples and local criterion argued.', 'glue',check='Finite powerset conclusion elementary; infinite local-to-global conclusion retains At11.')
C(6,28,[(9,[73])],
  'A proper subfigure has an interior lieu outside it.',
  'Assume At8–At10 in addition to At1–At7. If G<F in face order, choose an elementary X≤F not≤G and an interior lieu x≪°X. The least-receiving-stratum and disjointness axioms separate x from G, giving a lieu of F outside its G shadow. The claim concerns a proper face subfigure, not an arbitrary refinement.',
  'Proof sketched by choosing a missing stratum.',check='Proof dependency tracked; the compatibility condition in At10 is retained.')
C(6,29,[(10,[74,75,76,77])],
  'At12: compatibility of refinements tested on the intersection.',
  'For compatible ambient figures F,G, local refinements F′≪F,G′≪G are compatible iff their restrictions to F∩G are compatible, under the proposed At12 axiom. At12 yields binary gluing/At11′ and the needed interior disjointness L3, but supplies no infinite-join existence.',
  'Axiom and implications argued; infinite implication later removed.', 'glue',check='Kept with its exact ambient compatibility and finite/infinite distinction.')
C(6,30,[(10,[77,78,79,80])],
  'At9_Σ unifies spacious and polyhedral compatibility.',
  'Choose a class Σ of allowed intersection face posets. Compatibility is prescribed by the exclusive-locus disjointness condition together with membership of the common-face poset in Σ. Taking all posets gives the spacious variant; restricting to empty or a poset with greatest element gives the elementary-intersection/polyhedral variant. The empty case must be included explicitly.',
  'Axiom scheme and diagram of implications; wording revised.',check='Scheme is identifiable; no canonical choice of Σ or saturation theorem is proved.')
C(6,31,[(11,[81]),(10,[80])],
  '“At11bis ... implique At11 moyennant At11′”.',
  'At11bis says that a directed increasing face family of refinements F_i′≪F has a face supremum if each restricted family F_i′|X, X≤F elementary, has a face supremum. Together with the finite compatibility/gluing criterion At11′ this recovers arbitrary At11; At11 implies At11bis. The stationarity version crossed out here is stronger than the retained local-supremum version.',
  'Equivalence stated with sketch; stationarity replaced by local existence.', 'glue',check='Versions distinguished. The complete independent finite-type special case is C-SA21-6-040.')
C(6,32,[(11,[82,83,84])],
  'At13/support witness inside the ambient figure.',
  'If F′≪F and some nonzero G is disjoint from F′ but not from F, the support-witness principle asks for such a G refining F; under L1/L2 one seeks a lieu witness. The reduced At13 formulation is for an elementary ambient X and uses a lieu disjoint from the refinement. The passage proves a reduction using restriction locality, rather than deriving the extra support axiom from At1–At7.',
  'Initially called axiom then proposition; reduced support axiom and proof scheme distinguished.', 'support',check='Conditional witness principle; the P4 certificate also checks the stated old AtSupp in its finite model.')
C(6,33,[(11,[83,84])],
  '“H∥F′ ⇔ H∥F′_G”.',
  'Under the disjointness locality hypotheses, if H≪G≤F and F′≪F, then H⊥F′ iff H⊥(F′|G). The fixed compatible ambient F and restriction hypothesis are essential. This lemma is used to move a support witness inside a chosen stratum.',
  'Lemma with argument by loci/restriction.', 'support',check='Used with L2 and locality; not stated for arbitrary unrelated H,G,F′.')
C(6,34,[(11,[84,85,86])],
  'Subdivision characterized by equal orthogonality profiles and maximality.',
  'For F′≪F, define F′≼F by ∀G, (G⊥F′ iff G⊥F). With the support-witness axiom and the preceding locality hypotheses, this is equivalent to F′ being maximal for face inclusion among refinements of F. The manuscript deletes maximality for refinement order; that would be a different, generally inappropriate statement.',
  'Proposition/definition; “maximal for ≪” corrected to maximal for ≤.', 'support',check='The distinction between the two maximality orders is essential and recorded.')
C(6,35,[(11,[85,86,87])],
  'Subdivision order, two-out-of-three and restriction/local gluing.',
  'Subdivision defined by refinement plus equality of orthogonality profiles is reflexive, antisymmetric and transitive. In a comparable chain F″≪F′≪F, equality of the endpoint profiles implies equality of all three when profile inclusion follows from disjointness stability. Subdivision restricts to faces and compatible local subdivisions glue under the preceding restriction and At11 assumptions.',
  'Formal properties argued; all depend on the established disjointness axioms.', 'support',check='Order properties followed; locality is conditional on the preceding lemmas and gluing existence.')
C(6,36,[(11,[87]),(12,[88])],
  'At14: extend a subdivision of a subfigure to the ambient figure.',
  'For G≤F and a subdivision G′≼G, the optional extension axiom asks for F′≼F whose restriction to G is G′. A hope for a canonical or least extension is stronger and is not proved. Relative triangulation theorems must be compared to the category and allowed subdivisions, not treated as this abstract axiom.',
  'Optional axiom; canonical least extension hoped for.', 'triang',check='Open on these pages. Standard simultaneous triangulation gives only related existence in specified geometric categories.')
C(6,37,[(12,[88,89])],
  'At14bis: leave the other strata unchanged.',
  'For an extension of G′≼G≤F, the strengthened proposal asks that the face poset outside G be unchanged, with the new boundary glued to the old exterior incidence pattern; uniqueness of the resulting figure is presumed rather than proved. This is stronger than existence of some triangulation extending boundary data.',
  'Optional strengthened axiom, explicitly not established in all examples.', 'triang',check='Not a consequence of the opened Łojasiewicz1964 or Baro2010 theorems; those do not assert this uniqueness or unchanged exterior.')
C(6,38,[(12,[89,90,92])],
  'At14ter / Atens fac5: an elementary figure with subdivided boundary.',
  'Given X elementary and F′≼∂X, the proposal seeks an elementary Y with boundary F′ and the same intended underlying support as X. The scan92 formula says “unique” but omits a fixed ambient support and ambiguously places F′ in M; those omissions cannot be repaired silently. Even with fixed support, existence depends on the permitted category of elementary figures.',
  'Open optional proposal; reading ambiguity; author rejects it for strict simplicial ateliers.', 'triang',check='No uniqueness theorem identified. The strongest plausible formulation requires explicit support and category hypotheses.')
C(6,39,[(12,[89,90,92])],
  '“pas vrai pour les ateliers simpliciaux”.',
  'For a strict simplicial atelier whose elementary objects are simplices, subdividing an edge in the boundary of a triangle gives more than three boundary vertices/edges. It cannot be the boundary of one2-simplex with its other strata unchanged. Thus the strong elementary-extension/unchanged-exterior axioms fail in this category, although ordinary triangulations of the filled triangle exist.',
  'Author’s counterexample/objection.', 'simplicial',confidence='high',check='Independent combinatorial check: boundary of a2-simplex has exactly3vertices and3edges; one boundary-edge subdivision has4of each. No claim against ordinary relative triangulation.')
C(6,40,[(12,[91]),(11,[81])],
  '“Cet axiome est vide ... de t.f. ... famille ... stationnaire”.',
  'Assume every admitted figure is a finite face join of completely join-prime elementary figures. If (F_i′) is directed increasing for face order, each F_i′≪F, and all restrictions F_i′|X have face suprema for X≤F elementary, then the family is eventually constant. This is the precise finite-type special case; neither arbitrary refinement-increasing families nor missing local suprema are covered.',
  'Brief assertion without proof; an initial analyst suspicion is withdrawn after checking the exact prime hypothesis.', 'order','E',
  'Finite joins of complete join-primes have the required compactness, a standard consequence of the pre1986 representation mechanism verified in Speed1968. The atelier-specific restriction step is independently proved in formalism_and_checks.md §3; no separately published exact formulation was found in S67-04,05,11,12.',confidence='high',check='Independently re-proved. The earlier “missing compactness” suspicion in reading_analysis.md is expressly withdrawn.')
C(6,41,[(12,[90,91,92])],
  'Translations Atens2, Atens2_Σ, Atens3, Atens4 and automatic At13.',
  'For the quasi-set image with distinct loci disjoint and the stipulated compatibility criterion, disjointness is disjointness of represented sets; Σ-compatible intersections translate the chosen intersection class; At11bis becomes stability under locally finite/increasing unions; and the old support-witness axiom is automatic by choosing a point in a proper set difference. The scan91 compatibility conclusion should concern X′,Y′; its displayed X,Y already occur in the hypothesis.',
  'Translations stated; some labels and variables revised/uncertain.',check='Conditional translations, not proof that every set-figure subfamily satisfies the axioms. The variable error is a reading alarm.')
C(6,42,[(12,[93,94])],
  '“épais”, “quasi-dense”, inheritance and saturation.',
  'A thick subatelier contains the required elementary refinements; a quasi-dense one meets the interiors needed to preserve lieux. Under the explicit lowerness/closure conditions the full lieu set and L1 descend. Inheriting L2 requires reflection of ambient disjointness (Sousat4), not merely preservation. The L3 argument also needs the direction of the interior-shadow inclusion corrected or checked on the scan. A saturation construction is only announced.',
  'Definitions and partial inheritance arguments; saturation deferred.',check='No unqualified inheritance theorem asserted; disjointness reflection and the reading issue are retained.')
C(6,43,[(5,[37,38]),(6,[47,48,49]),(7,[50,51,52])],
  'Morphisms, quasi-morphisms and comorphisms of ateliers.',
  'Maps of figure sets are proposed to preserve face and refinement orders and the specified existing joins/meets. A direct map of strata is not automatic: inverse image on local downset lattices produces contravariant stratum maps under complete-homomorphism hypotheses. The text changes between these directions and does not finish a single functor category. The exact complete-lattice lemma is separated as C-SA21-6-013.',
  'Definitions under revision; functorial formulation incomplete.',check='Retained as a construction problem; category equivalences elsewhere are interpreted only where morphisms are actually specified.')
C(6,44,[(2,[16,17]),(3,[18])],
  '“pré-admissibles”, smallest containing member and separation.',
  'Let A⊆P(M) cover M; suppose for each x the family of A-members containing x has a least member A_x, and x↦A_x is injective. Define y≤x iff y∈A_x. Then this is a partial order, every A-member is lower and A_x=↓x. Including the empty set makes the family preadmissible, not admissible in the nonempty-open-stratum sense. Further closure axioms are needed for an atelier.',
  'Construction stated and related to IV C1–C3.', 'order','E',
  'This is the standard specialization/minimal-neighbourhood construction for a separating family closed under its pointwise intersections. The exact downset representation is verified by Speed1968 and Massas2023. EGA search yielded only metadata, not an exact checked passage, so no EGA theorem is claimed.',confidence='high',check='Independent elementary verification: reflexivity from x∈A_x, transitivity from minimality, antisymmetry from separation.')

# Cote156-7. Supplied corpus starts at scan10, not at scan2.
C(7,1,[(1,[10,11,15,16,17]),(2,[18])],
  'AtC, AtD, AtD0; spacious and polyhedral compatibility criteria.',
  'Under the base atelier axioms, AtC says compatible local restrictions of refinements of compatible ambient figures imply compatible global refinements. AtD says disjointness of those refinements is equivalent to disjointness on the ambient common face; AtD0 is refinement stability of disjointness. The text claims AtC⇒AtD⇒AtD0, and AtD plus the spacious/polyhedral exclusive-piece criterion⇒AtC. The polyhedral branch includes the empty-or-elementary intersection hypothesis; the spacious one does not.',
  'Implications argued and diagrammed; versions revised in margins.', 'glue',check='Exact versions retained, without treating the changing diagrams as one fixed axiom list.')
C(7,2,[(1,[12,13]),(7,[59])],
  '“raffinement strict” replaces the earlier set-figure criterion.',
  'For set figures A,B, the strengthened/polyhedral refinement requires every closed stratum S of A and T of B to have S∩T either empty or a closed stratum/face of S, together with the intended refinement support condition. Ordinary containment of underlying supports is weaker. This repairs the earlier claim that small set shadows reflected geometric refinement; VII59 gives a counterexample when one forgets the strict condition.',
  'Explicit change of definition, with examples of non-strict geometric refinement.',check='Definition change cross-linked to VI52–53. No equivalence with the old weaker refinement is asserted.')
C(7,3,[(1,[14])],
  'Polyhedral posets and the duality lemma.',
  'Call I polyhedral if each pair having a common lower bound has an infimum. The four-element interpolation condition is self-dual. If every closed interval in I is inductive for the opposite order, the text derives polyhedrality of I^op from that of I; the reverse implication uses inductivity in I. Finite intervals satisfy both chain conditions. In the dual conclusion “greatest” must read “least upper bound”; otherwise the statement reverses the order.',
  'Lemma with a question mark and short order argument.', 'order',check='The interval chain-completeness hypotheses are retained. The suspected “plus grand”/“plus petit” reading is unresolved on ink.')
C(7,4,[(1,[14,15])],
  '“simplexe combinatoire” iff finite polyhedral with a greatest element and at least two predecessors at each nonminimal element.',
  'The claimed equivalence is false. The nonempty face poset of a square is finite, has a greatest element, has infima for pairs with nonempty common lower set, and each nonminimal face has at least two immediate predecessors; it is not the poset of all nonempty subsets of its four minimal elements. The correct simplicial condition is that each principal interval, with a bottom adjoined, be Boolean.',
  'Claim with induction sketch; no self-correction in the supplied VII pages.', 'simplicial','D',
  'Search S67-01 located Stanley1991 §1 p319, which states the Boolean-interval definition and its relation to simplicial complexes. It does not prove the weaker criterion here. No exact publication of the manuscript criterion was found; the present finite counterexample settles its falsity under the written hypotheses.',computation='check_finite_examples.py, square_simplex_counterexample:9 nonempty faces versus15 nonempty subsets of4 minima; all hypotheses exhaustively checked.',confidence='high',check='False as stated; corrected Boolean-interval formulation is explicitly an analyst comparison.')
C(7,5,[(2,[18,19])],
  'Atfil and two corollaries, including refinement-increasing families.',
  'Atfil now requires a directed face-increasing family F_i≪F whose restrictions to every elementary face X≤F are eventually constant, and asserts existence of its face supremum. With AtC, gluing refinements is claimed. A further corollary replaces face-increasing by refinement-increasing and possibly changes the supremum order; the margin itself asks which version is intended. This is distinct from VI81’s weaker local-supremum hypothesis.',
  'Axiom, corollaries and an unresolved marginal variant.', 'glue',check='No proof supplied here of the refinement-increasing variant; the two orders and two local-finiteness formulations are kept separate.')
C(7,6,[(2,[19,20])],
  'AtSupp, stronger common-refiner question, and AtensD.',
  'The old support-witness principle asks, when Y⊥G but Y not⊥F with G≪F, for a witness inside F. The stronger question asks for a nonzero Y′ refining both Y and F. AtensD explicitly imposes F⊥G iff no elementary object refines both. It implies x⊥F iff x does not refine F for a lieu x, all distinct lieux are disjoint, and the weaker AtSupp. The text notes the stronger common-refiner property is essentially set-like and not generally expected.',
  'Stronger version questioned, then isolated as a restrictive axiom; corollaries argued.', 'support',check='Do not promote AtensD to a consequence of the base axioms.')
C(7,7,[(2,[20,21,22,23,24]),(5,[46,47])],
  'L1–L3, CL and the four equivalent systems.',
  'With the common At1–At7 background, the manuscript compares: (a)L1,L2,L3,CL; (b)L1,L2,D,C; (c)L1,CL,D; (d)L1,L2,C,D0, with either consistently spacious or consistently polyhedral C/CL and the corresponding intersection requirement. L1 means ∀X∃x∈L, x≪°X; it does not demand a proper interior refinement. The displayed implication proofs use restriction locality and least receiving strata.',
  'Equivalence diagrams and proof sketches, revised at VII46–47.',check='Equivalence retained with all common background and the fixed choice of variant; not independently checked in every direction.')
C(7,8,[(2,[22,23])],
  'Restriction of a lieu, and zero restriction iff disjointness.',
  'For a lieu x refining an ambient figure F and P≤F, the restriction x|P is x iff x≪P and is empty otherwise. Under AtD, for G≪F, G|P=0 iff G⊥P. These are local statements with a common ambient F; without that hypothesis an empty common face does not establish disjointness.',
  'Lemma and extension argued.',check='The lieu dichotomy follows from minimality; the extension retains AtD.')
C(7,9,[(3,[26,27,28,29,30]),(4,[35,41])],
  'ML1 strengthened; Lemmas1–2 and least receiving strata.',
  'The retained ML1 lifting condition is: if Z≪X, X′≤X, x∈L and x≪Z,X′, there is Z′≤Z with x≪Z′≪X′; if Z≤X one may require Z′≤X′. Together with nonempty interior lieux (ML2) and an interior receiving face for every lieu (ML3), it yields least receiving strata for arbitrary Z≪X and the local interior-shadow criteria. Lemma1’s global equivalence X≤Y⇔X≪Y⇔interior-shadow intersection requires a common compatible/face-bounded ambient situation; the written opening omits it and the proof invokes ML1 as if it were available.',
  'ML1 explicitly strengthened at scan28; source Lemma1 and VII41 LemmaA have a hypothesis alarm.',check='Reconstruction with a common face upper bound is labelled as such. No unconditional equality of the two orders is inferred.')
C(7,10,[(3,[30,31,32,33]),(4,[34])],
  'Compatibility from exclusive locus shadows; Lemmas3–7.',
  'Define K=↓X∩↓Y and omb(K)=∪_{Z∈K}omb(Z). Say X compatible Y iff every x∈omb(X)\omb(K) is orthogonal to every y∈omb(Y)\omb(K). Under the strengthened ML0–ML5, the manuscript proves compatibility is reflexive, symmetric and hereditary under faces, common face-bounded pairs are compatible, compatible refinement implies face inclusion, compatible receiving strata are unique, and the relation restricted to L is the original graph relation plus equality.',
  'Sequence of lemmas with proofs/sketches.',check='All lemmas depend on the strengthened lifting condition and L1; not attributed to the weaker initial ML1.')
C(7,11,[(4,[34,35,36,37,38])],
  '“Théorème-Scholie”: ML0–ML5 reconstruction.',
  'Given nested partial orders ≤,≪ on M, L the ≪-minimal elements, and a symmetric irreflexive graph on L, impose ML1’s strengthened lifting; ML2 interior-locus nonemptiness; ML3 interior-face coverage; and ML5: Y≤X, x∈omb(X)\omb(Y), y∈omb(Y) imply x⊥y. The compatible lower subsets of M, ordered by inclusion and with stratumwise ≪, form the maximal spacious atelier with L1–L3 and CL(spac), inducing the original elementary data. Conversely such an atelier gives these conditions.',
  'Theorem with a cumulative proof; converse asserted by translating axioms.',check='Precise candidate equivalence identified. Full independent verification of the equivalence is outside the checks actually performed; no exact published counterpart found.')
C(7,12,[(4,[36,37,38]),(7,[61]),(14,[114])],
  'Other admitted figure families; finite-type/finite figures determined by M.',
  'Once the elementary structure is fixed, an atelier is specified by a lower family of compatible lower subsets covering M, containing empty and closed under finite compatible unions. All finite deployments are forced if principal ideals are finite. For figures merely of finite type (finite unions of principal ideals), existence also needs every lower subfigure to remain finitely generated; finite type alone does not say each deployment is finite. The statement that every finite compatible subset is a figure must include lowerness.',
  'Construction/classification stated; finite formula omits a lowerness condition at VII114.',check='Finite-deployment and finite-generation assertions separated; missing lowerness and hereditary finite generation are explicit repairs.')
C(7,13,[(4,[39])],
  'Choice of a graph Γ between Γ₀ and all pairs of lieux.',
  'For fixed nested orders satisfying the non-graph ML conditions, the permitted orthogonality graphs must contain all pairs forced by face/exclusive-shadow disjointness and may be enlarged subject to the same axioms. Taking the complete graph on distinct lieux gives set-like disjointness, but does not itself prove that the small-multiombre map is globally injective or reflects refinement.',
  'Graph-choice observation and prospective interpretation.',check='The last distinction is demonstrated later by the nonfaithful set representations in VII58–59.')
C(7,14,[(4,[40,41]),(5,[42,43,44]),(6,[52,53])],
  'Replace L by a dense Λ; MΛ0–MΛ5 and PratΛ.',
  'Let Λ⊆M meet the interior-refinement class of every X. Replace point/locus tests by Λ-tests, keep compatible-order reflection and the lifting condition for common Λ-refiners of compatible strata. Under the complete displayed MΛ/PratΛ axioms the compatible lower-set construction is claimed to recover an atelier. Λ=M is allowed and makes density automatic; Λ=L recovers the divisibility case. The compatibility lifting axiom cannot be dropped merely by keeping an orthogonality graph on Λ.',
  'Generalization proposed and proposition sketched; formulas revised, including a reversed arrow in PratΛ6.',check='Full displayed axiom set required; the PratΛ6 direction is flagged for ink checking.')
C(7,15,[(5,[44,45,48,49]),(6,[50])],
  'Attempt to reconstruct compatibility from Λ-disjointness alone: “Non cf49”.',
  'The attempted derivation of compatibility and the common-shadow intersection formula from only a dense Λ and a disjointness graph is withdrawn. Additional locality/lifting axioms are needed to ensure Omb(F)∩Omb(G)=Omb(F∩G) for compatible F,G and the restriction-disjointness lemma. The canceled VII45 and49 alternatives are not a proved reconstruction.',
  'Explicit cancellation and recognition of a missing implication at scans48–50.',check='Withdrawn proof route preserved, rather than merged into the successful stronger theorem.')
C(7,16,[(6,[51,52,53,54])],
  'Prat1–Prat6 define the preatelier elementary data.',
  'A preatelier consists of two nested partial orders and a reflexive symmetric face-hereditary compatibility relation. Require: transitive interior refinement; a least receiving face for each Z≪X; uniqueness of compatible receiving strata; and compatible refinement⇒face inclusion. These data reconstruct maximal compatible lower-set figures and determine finite-figure ateliers, with the necessary finite principal-ideal condition. PratL′ substitutes locus tests and the disjointness graph, while Pratpol requires common compatible face intersections to be empty or principal.',
  'Axiom translation and reconstruction claim.',check='Different Prat/PratΛ/PratL′ presentations retained; no omitted hypotheses imported from the canceled graph-only attempt.')
C(7,17,[(6,[54]),(4,[35])],
  'Trivial preatelier with ≪=≤ and universal compatibility.',
  'For any poset M, take ≪=≤, every pair compatible and figures Down(M). Then Prat1–6 hold, disjointness is empty intersection, and the displayed D,C(spac),Fil,Supp properties hold. L2 is equivalent to every element lying above some minimal element; L3 holds; L1 holds exactly when M is discrete. Therefore the sentence “only L1 fails” needs the stated minimal-cofinality hypothesis and is not true of an arbitrary poset.',
  'Example analyzed; the page itself states the L2 proviso before the overbroad concluding sentence.', 'order',check='Direct order analysis. Infinite descending chains without minima refute the unqualified L2/“only L1” conclusion.')
C(7,18,[(6,[55,56,57]),(7,[58,59])],
  'Conditions(i),(ii) for an embedding in set figures, then counterexamples.',
  'A canonical set-figure map that is locally an isomorphism on subfigure lattices and reflects both refinement and compatibility implies L1–L3, CL(spac) and pairwise disjoint distinct lieux. Conversely those axioms give the local isomorphisms, but need not give global injection, compatibility reflection or refinement reflection. The affine/PL interval example disproves injection; if injection is added, compatibility reflection is recovered by CL, while strict/polyhedral refinement still need not be reflected.',
  'Attempted converse corrected through explicit counterexamples on scans58–59.',check='All three failures and the added-injectivity repair are kept separate. No false global embedding theorem retained.')
C(7,19,[(7,[60,61])],
  'Pratquas1–4 and the hoped sufficiency of quasi-set data.',
  'The four proposed quasi-set axioms retain nested orders, interior lieu coverage/least receivers, and the indicated shadow-intersection/lifting conditions. They are intended to define the common spacious/polyhedral elementary structure when lieux are points. The text says “à déduire” and “il semblerait”; it does not prove that the formulation captures every future geometric requirement. General infinite ateliers still require a choice of admitted figure family.',
  'Tentative simplification, not a finished universal adequacy theorem.',check='Identifiable proposed construction, with adequacy left open.')
C(7,20,[(7,[62,63])],
  'Support systems on figures and on elementary objects.',
  'A class of figures closed under refinement and existing face joins is determined by the elementary objects it contains: F is in it iff every X≤F is in it. Conversely a refinement-lower class of elementary objects determines such a figure class by this criterion. The correspondence is A↦A∩M and the appropriate Env extension, using At4 and elementary decomposition.',
  'Proposition/construction with argument.', 'support',check='The class of support systems in this preliminary correspondence is distinguished from the later orthoclosed virtual supports.')
C(7,21,[(7,[63,64,65])],
  'cosupp, supp and the complete lattice of supports.',
  'For a symmetric irreflexive relation on M, define A⊥ and A⊥⊥. Then A↦A⊥⊥ is an extensive monotone idempotent closure; closed subsets form a complete ortholattice with ∧=∩, ∨=closure of union, orthocomplement A⊥, bottom empty and top M. On the full figure set, bottom includes the zero figure. A∩B⊥=empty does not generally imply A⊆B, and distributivity is a separate question.',
  'Formal calculation proved/sketched; converse and distributivity queried.', 'support','E',
  'Ore1944 Theorems1–2 pp495–496 and Theorem8 p503 establish the closure/Galois construction from a binary relation; section4 p500 discusses polarities. Primary article text was opened in a reproduction after the AMS URL failed. Janowitz1963 p1241 verifies the older ortholattice/orthomodular distinction. This establishes the pre1986 background; Lindenhovius–Vetterlein2023 gives the modern exact orthogonality-closed-set account.',confidence='high',check='Independent algebraic check of closure identities and complete ortholattice operations; no Boolean conclusion.',date={'first_circulation':'Ore1944 p493 identifies1941 Chicago lectures; manuscript received1943-11-13','publication':'1944-05 for Ore;1963 for Janowitz','searched_as_of':'2026-11-19'})
C(7,22,[(8,[66,67])],
  'DisjΛ and support lattices recovered by intersection with Λ.',
  'Suppose Λ⊆M detects disjointness: for every F,G, F⊥G iff every Λ-refiner of F is disjoint from G (and, by symmetry, the corresponding two-sided test). Then S↦S∩Λ identifies the orthoclosed support lattice on M with that on Λ, inverse A↦cl_M(A). With L2, Λ=L is valid, so supports depend only on the locus orthogonality graph. The source formula at scan66 has a type/side typo, separately flagged.',
  'Theorem/formal proof using polarities.', 'support',confidence='high',check='Independent proof follows by expressing each orthogonality test through Λ and taking double orthogonals; no arbitrary dense subset suffices without DisjΛ.')
C(7,23,[(8,[67,68])],
  'In the quasi-set case, supports are P(L).',
  'Under L2 and the assumption that distinct lieux are pairwise orthogonal, the polar on subsets of L is ordinary complement, so every subset of L is orthoclosed. Hence Σ_M≅P(L) as complete Boolean algebras. L2 is essential to transfer this conclusion from L back to M.',
  'Corollary and point-set interpretation.', 'support','E',
  'This is the elementary complete-graph polarity, and the powerset/complete atomic Boolean algebra identification is stated in Massas2023 Theorem2.29 with older duality context. It is a pre1986 standard special case, not a later resolution of arbitrary VGF supports.',refs=['Massas2023','LindenhoviusVetterlein2023'],confidence='high',check='Independently checked: A⊥=L\A, so A⊥⊥=A.')
C(7,24,[(8,[69,70,71,72])],
  'Elementary intervals/points for an arbitrary ordered set I; “tous les axiomes ... sauf AtL1”.',
  'The proposed interval atelier has point strata and closed intervals [a,b], with face inclusions and refinement by subintervals. For a total order with the stated coherent interval figures, L1 means each nondegenerate interval has an interior point. The written extension to an arbitrary poset I and assertion of all other axioms need additional control of intersections and incidence; the supplied pages do not verify those conditions. The total-order interpretation is an analyst restriction, not a silent replacement.',
  'Example/program and broad assertion without full verification.',check='The arbitrary-poset generality remains unverified; no finite counterexample with every intended interval axiom is claimed here.')
C(7,25,[(8,[71,72])],
  'Points plus formal open interval cells as a set representation.',
  'To distinguish intervals with empty interior, introduce formal cells in addition to existing points and represent each interval by its point and cell constituents. This separates endpoint/open-cell information missing from the locus representation. A canonical construction for every poset, with exact compatibility/refinement reflection, is requested rather than completed.',
  'Construction idea and open canonical-realization question.',check='Exact choices and axioms not fully specified; retain as a construction problem, not a proved representation theorem.')
C(7,26,[(9,[73])],
  'P(~F) and pullback along a refinement.',
  'For each figure F, the power set P(~F) is a local complete Boolean algebra. A refinement F′≪F gives the least-receiving-stratum map ~F′→~F and therefore a complete Boolean homomorphism by inverse image. This local Boolean algebra must not be identified without proof with the sublattice of global virtual supports generated by the strata.',
  'Formal construction.', 'order','E',
  'Inverse image of subsets preserves arbitrary unions, intersections and complements; this is the standard powerset construction, related to Massas2023 Theorem2.29. The global-support comparison is a separate manuscript conjecture, refuted in C-SA21-7-045 under the stated generality.',confidence='high',check='Independent elementary check; local/global distinction explicit.')
C(7,27,[(9,[73,74,75])],
  'Support realization M→P(P), axioms(i)–(vi).',
  'Seek a set P and subsets |X| for X∈M such that refinement is monotone; compatible intersections are unions of common-face supports; X⊥Y iff |X|∩|Y|=empty; subdivision has equal support; every support is the union of supports of its lieux; and the supports cover and separate P. The suggestion that some conditions follow from others is explicitly a question. A realization with nonpoint lieux need not separate points.',
  'Axiom program and possible redundancies discussed.', 'support',check='No full existence/uniqueness theorem is proved; each clause remains part of the proposed realization problem.')
C(7,28,[(9,[76,77])],
  'Relations between represented subsets and virtual supports.',
  'Assume the exact disjointness representation X⊥Y iff |X|∩|Y|=empty and extend |A|=∪_{X∈A}|X|. Then |A|⊆|B| implies A⊥⊇B⊥ and cl(A)⊆cl(B). If B is orthoclosed, cl(A)⊆B implies |A|⊆|B|. Thus closed supports embed order-preservingly into subsets via union, but equality |cl(A)|=|A| is an additional statement.',
  'Implications proved by disjointness tests.', 'support',confidence='high',check='Independent polarity argument checked. No equality of arbitrary unions with their closure images is assumed.')
C(7,29,[(9,[78,79])],
  'Only inclusions for lattice operations; Hyp gives complement equality.',
  'Under a disjointness representation, images of virtual-support meets, joins and complements initially satisfy only the displayed inclusions. Add Hyp: for every collection A⊆M and every p outside |A|, some Y contains p and is orthogonal to every X∈A. Then |A⊥|=P\|A|, double orthogonal closure preserves represented unions, and the virtual-support lattice maps to a complete Boolean algebra of subsets. The universal quantifier over all A is material.',
  'Formal implications and sufficient condition proved/sketched.', 'support',check='Hyp is a strong separation condition, not derived from the earlier geometric axioms.')
C(7,30,[(10,[80,81,82])],
  'Hyp′: each point is represented by a singleton support; ΣM≅P(P).',
  'Assume X⊥Y iff |X|∩|Y|=empty and for every p∈P there exists X_p with |X_p|={p}; also supports cover P. Then every subset of P is a union of represented singleton supports, Hyp holds, and S↦|S| is an isomorphism from the complete orthoclosed support lattice to P(P). Consequently P can be recovered as its atoms. This is a theorem under these assumptions, not proof that every atelier admits such a representation.',
  'Proposition/argument with possible redundancies questioned.', 'support','E',
  'The resulting complete atomic Boolean representation is standard before1986; Massas2023 Theorem2.29 states the exact powerset/atoms duality. The implication from the displayed singleton/disjointness assumptions is independently checked here. General non-Boolean orthogonality spaces do not satisfy these assumptions.',refs=['Massas2023','LindenhoviusVetterlein2023'],confidence='high',check='Independently re-proved by complement tests with X_p; the two-strand example is not a counterexample because Supp1 fails there.')
C(7,31,[(10,[81,82])],
  'The remaining support realization axioms should be automatic.',
  'After the singleton/disjointness result, the text presumes that the other desired compatibility-intersection and subdivision clauses may follow. This requires specific links between refinement, face incidence and the represented orthogonality relation; the Boolean-lattice conclusion alone supplies none of those links. No exact redundancy theorem is established on these pages.',
  'Explicitly presumed/unproved.', 'support',check='Open implication problem; separate from the proved singleton Boolean theorem.')
C(7,32,[(10,[82])],
  'Two-strand example and marginal correction: Supp1 fails.',
  'In the two-strand/ficelle model, a lieu can have a disconnected endpoint support; disjoint endpoint sets do not force the geometric disjointness relation of the lieu. The natural endpoint-set assignment therefore violates Supp1 (the iff between geometric disjointness and set disjointness). The model cannot be used against a theorem that assumes Supp1.',
  'Author explicitly corrects the tempting natural realization in the margin.', 'support',confidence='high',check='Hypothesis failure preserved; this prevents a false refutation of C-SA21-7-030.')
C(7,33,[(10,[82,83,84])],
  'Two strands: singleton supports, rectangles and failure of a distributive identity.',
  'For pairs (a,b) with orthogonality when both coordinates lie strictly on the same side, the double-orthogonal closure of two crossing pairs can be a rectangle rather than their two-point union. A third pair in that rectangle yields S₃∧(S₁∨S₂)≠(S₃∧S₁)∨(S₃∧S₂). This establishes a relation-level distributivity obstruction. It does not by itself establish nonmodularity, nor verify every geometric atelier axiom.',
  'Computation and proposed geometric counterexample; natural realization simultaneously corrected.', 'support',computation='check_finite_examples.py, two_strand_grid_computation:5×5 grid, z1=(1,3), z2=(3,1), z3=(2,2); closure of first two is3×3 rectangle. Dense-order geometric generalization is not exhaustively certified.',confidence='high',check='Finite polarity calculation reproduced; geometric realization and modularity claims explicitly limited.')
C(7,34,[(10,[85,86]),(11,[87])],
  'Open support of a stratum as support minus boundary cosupport.',
  'A proposed virtual open stratum is supp(X)∩cosupp(∂X). The desired decomposition of closed support into its face/open contributions and equality with the support generated by interior lieux require an absorption/local-complement law; they do not follow solely from orthocomplementation. The pages explore these equalities rather than prove them in full.',
  'Open formulas and reductions.', 'support',check='Kept conditional; the later P4 obstruction shows why an unconditional Boolean interpretation is unsafe.')
C(7,35,[(11,[87,88,93])],
  'AtSupp1 absorption; later margin calls it artificial.',
  'AtSupp1 asks: if Y∈supp(X) and Y is disjoint from the boundary of X, then Y≪X. A stronger form concerns arbitrary virtual differences. This is an optional extra axiom; the later26June margin says it is artificial and not generally valid. Whenever VII93 uses it to identify an open interior with a closed support, the conditional phrase “Si on admet” must be retained.',
  'Proposed axiom, later criticized/withdrawn as a general expectation.', 'support',check='Optional absorption is not included in the P4 countermodel’s verified hypotheses; that model fails it.')
C(7,36,[(11,[88,89])],
  'Virtual differences and recovering refinement from incidence and disjointness.',
  'The proposal seeks to define refinement recursively from face incidence and a disjointness relation on virtual differences, using stronger absorption. No complete recursive definition with termination/well-foundedness hypotheses is supplied; the empty-intersection alternative on scan89 is canceled. This is a reconstruction program rather than an established theorem.',
  'Tentative construction and canceled alternative.', 'support',check='Identifiable goal with incomplete formal specification; no external exact realization found.')
C(7,37,[(11,[90]),(12,[100])],
  'Strong interior X° and later change to supp of interior lieux.',
  'Initially X°={Y∈M:Y≪X and Y⊥∂X}. This is stronger than immediate refinement Y≪°X and must not be conflated with it. At VII100 the notation changes to the support closure generated by interior lieux; equality of these two versions depends on earlier optional absorption and is not automatic. The claim records preserve which version each formula uses.',
  'Definition, then a consequential notational change.', 'support',check='Version distinction enforced; no equality is silently inserted.')
C(7,38,[(11,[90,91])],
  'Lemma1: total disjointness detected by strong interiors of all faces.',
  'Under L2,L3 and D0, X⊥Y iff for every face X′≤X and Y′≤Y, all elements of the strong interiors X′° and Y′° are pairwise disjoint, provided the interior-locus coverage used in the proof is available. The implication from interior tests to all locus tests uses the receiving-face decomposition, not merely nonemptiness of one interior.',
  'Lemma with proof via lieux and boundary separation.', 'support',check='Proof hypotheses kept explicit; not asserted in the later framework where interiors may be empty.')
C(7,39,[(11,[90,91,92])],
  'Lemma2: immediate refinement and strong-interior containment.',
  'For Y≪X under the stated L1–L3/locality hypotheses, immediate refinement Y≪°X is characterized by Y°⊆X°, using nonempty interior loci to recover the least receiving stratum. Strong containment Y∈X° is characterized by requiring (Y′)°⊆X° for every face Y′≤Y. Empty-interior cases invalidate the detection argument and are excluded here.',
  'Lemma and corollaries with argument.', 'support',check='Y≪X and L1 are retained; the statement is not extended to unrelated strata or empty-interior ateliers.')
C(7,40,[(11,[91,92])],
  'Finite-dimensional nonempty strong interiors imply L1.',
  'For an atelier with finite descending face dimension and the preceding strong-interior/locus decomposition properties, the text argues inductively that nonempty strong interiors in every elementary figure force an interior lieu, hence L1; the converse follows from L1 and disjointness of distinct compatible face interiors. “Finite-dimensional” is a well-founded induction hypothesis here, not merely a finite cardinality of the ambient point set.',
  'Inductive argument sketched.', 'support',check='Well-foundedness and previous locality properties are necessary; no unrestricted infinite-dimensional equivalence claimed.')
C(7,41,[(11,[92,93]),(12,[96])],
  'Distinct compatible strata have orthogonal strong interiors.',
  'Assuming L1–L3 and D0 in the strong-interior version, for distinct compatible X,Y, every U∈X° is disjoint from every V∈Y°. Consequently the support closures generated by these interiors are orthogonal in the virtual-support lattice. Merely set-disjoint interiors would not suffice.',
  'Proof/reformulation, with full orthogonality emphasized at scan96.', 'support',check='The compatibility hypothesis and passage from sets to their orthoclosures are preserved.')
C(7,42,[(11,[93]),(12,[94,95,96,97])],
  'A↦S_A for subsets of the strata of one compatible figure.',
  'For a fixed figure F₀ and A⊆~F₀, put S_A=cl(∪_{X∈A}X°), with the specified interior convention and L1/locality. The nonzero pairwise orthogonal interior contributions give an order embedding A↦S_A and preservation of arbitrary joins. For lower A, the intended identification is the ordinary support of the corresponding subfigure. Preservation of intersections and the relative-complement formula are extra claims, not a consequence of these established parts.',
  'Order/join properties argued; full Boolean conclusion proposed then challenged.', 'support',check='Partial result separated from the false relative-complement claim. Empty interior contributions would destroy injectivity.')
C(7,43,[(12,[97,98])],
  'Formal ortholattice lemma marked “Faux”; Lemma3 for S⊥S′.',
  'In an arbitrary complete ortholattice, pairwise orthogonal nonzero elements need not make the sublattice generated by their joins a Boolean sublattice with inherited relative complements. In particular S⊥S′ does not force S′=(S∨S′)∧S⊥. The displayed general lemma is false; this equation is an orthomodular-law instance and requires a stronger hypothesis.',
  'Author marks the formal lemma false and supplies a counterexample at scan99.', 'support','B',
  'Exact later independent counterexample: Lindenhovius–Vetterlein2023 Example3.3 uses the same P4 orthogonality graph and nonorthomodular six-element lattice. Janowitz1963 p1241 already states the distinguishing orthomodular axiom. No historical dependence is inferred; the later example confirms the precise failure, while the stronger law was known before1986.',computation='check_finite_examples.py, path_graph_local_support_counterexample. Complete list of six closed subsets can also be read in the opened 2023 Example3.3.',confidence='high',check='Refuted; an orthomodularity hypothesis would repair this particular relative-complement identity, not automatically every atelier realization claim.',date={'first_circulation':'2022-07-19 arXiv2207.09148 metadata; exact Example3.3 presence in v1 not checked because fetch failed','publication':'2023-03-10','searched_as_of':'2026-11-19'})
C(7,44,[(12,[99])],
  'The four objects A′,A,B,B′ form his counterexample.',
  'For the path orthogonality graph A′—A—B—B′, the orthoclosed subsets are empty, the full set, {A}, {B}, {A′,B}, {A,B′}. Thus {A}∨{B}=T but T∩{B}⊥={A,B′} differs from {A}. The transcribed supp(A)=A′ is inconsistent with the graph and is flagged as a reading alarm; the graph calculation itself is unambiguous.',
  'Author’s explicit counterexample and computation.', 'support','B',
  'Lindenhovius–Vetterlein2023 Example3.3 is an exact graph-and-lattice match, not merely a similar topic. It is independently established there; no transmission from this manuscript is asserted. First preprint date is recorded separately from the checked published version.',computation='check_finite_examples.py and finite_checks_output.json, P4 closure values; all sets in the calculation obtained by exhaustive double orthogonals.',confidence='high',check='Computation reproduced and matched to opened primary Example3.3.',date={'first_circulation':'2022-07-19 preprint metadata, v1 content not verified','publication':'2023-03-10','searched_as_of':'2026-11-19'})
C(7,45,[(12,[99,100]),(2,[20,21,22])],
  'After the counterexample, hope that “au moins ... AtL1” rescues the local Boolean assertion.',
  'The local relative-complement law S_{A\B}=S_A∩S_B⊥ remains false even for an At1–At7 atelier satisfying L1–L3, D, D0, C(spac), CL(spac) and the old AtSupp. Take figures to be all cliques of the P4 graph, both orders inclusion and M=L singleton figures. Identity is an interior refinement, so the written L1 holds. For F₀={A,B}, B₀={B}, left support is {A}, right support is {A,B′}. Optional AtSupp1 absorption is not satisfied and is not included.',
  'Renewed conjectural rescue after a self-refutation; no proof.', 'support','D',
  'Searches S67-01,07,09–12 found the exact P4 orthogonality example in Lindenhovius–Vetterlein2023 but no publication checking these manuscript atelier axioms or the proposed L1 rescue. The present exhaustive certificate establishes the counterexample under the enumerated hypotheses. This is an analyst result, not a claimed later published VGF theorem.',computation='check_finite_examples.py exhaustively checks all listed conditions including strong complete join-primality and non-strict L1; finite_checks_output.json contains every pass and the failed equation. formalism_and_checks.md §4 gives clause-by-clause proof and the AtSupp1 limitation.',confidence='high',check='False under the explicitly checked hypotheses. No counterexample claimed to a version adding AtSupp1.')
C(7,46,[(12,[100]),(13,[101])],
  'Subdivision contributions recover the interior support; point realization formula.',
  'For F≼X, the support generated by the interior contributions of those strata of F receiving in the interior of X is claimed to equal the interior support of X, using L2 and equality of support profiles. Under a singleton realization the desired formula is |X°|=|X|\|∂X|, but the page’s argument visibly proves one inclusion before asserting the equality. The interior convention and any absorption assumption must be fixed.',
  'Lemma/argument; equality in the realization interpretation not fully justified.', 'support',check='Support-join statement and stronger set-difference equality distinguished; unresolved converse recorded as an open step.')
C(7,47,[(13,[102])],
  'Without L1, simplicial open supports can vanish.',
  'In a trivial simplicial atelier with ≪=≤ and lieux the vertices, the virtual support of a simplex is determined by its vertices; the union of boundary supports already contains those vertices for every positive-dimensional simplex. Hence the attempted virtual open support can be zero although the elementary stratum is nonempty. This motivates taking interior disjointness as primitive instead of reconstructing it from lieux.',
  'Example and explicit change of direction.', 'support',confidence='high',check='Independent elementary check for any simplex of dimension≥1. This is a failure of the chosen locus support invariant, not a claim that the geometric open simplex is empty.')
C(7,48,[(13,[102,103,104,105,106]),(14,[111])],
  'Primitive interior disjointness and derived compatibility/disjointness.',
  'Let δ be symmetric irreflexive on M and stable under immediate refinements. Assume distinct faces of a common elementary object are δ-related. Define X compatible Y iff every exclusive face X′∈↓X\↓Y and Y′∈↓Y\↓X satisfies δ; define X⊥Y iff every face X′≤X,Y′≤Y satisfies δ. Then X⊥Y iff X,Y are compatible and have no common face. The text derives face-heredity of compatibility and the common-refiner lifting property using least receiving strata.',
  'Propositions and proof sketches, with an index typo in the stability formula.',check='Primitive δ and total disjointness are distinct. The formula must involve X′δY′ after refinement; the transcription’s repeated XδY is flagged.')
C(7,49,[(13,[106,107]),(14,[108,109])],
  'Mag6″ and equivalence with L1–L3 plus C(spac).',
  'Add δ(X,Y) iff every interior lieu of X is disjoint from every interior lieu of Y. Irreflexivity then forces L1 (otherwise the universal condition is vacuous for X=X); the preceding derived-disjointness formula gives L2, and common-face interior disjointness gives L3. Conversely an atelier with L1–L3 and C(spac) recovers compatibility from this δ. An equivalence of categories is written, but morphisms are not specified here; the verified formulation is an equivalence of structures up to isomorphism.',
  'Argument and asserted equivalence, followed by the decision to abandon the divisibility restriction.',check='The vacuity argument checked directly. Full categorical language is restricted until a morphism definition is supplied.')
C(7,50,[(14,[110,111,112,113,114])],
  'Final Mag1–Mag4 and AtM1–AtM4.',
  'A magasin has nested partial orders ≤,≪; each Z≪X has a least face X′≤X receiving Z; an irreflexive symmetric δ preserved by immediate refinement; and δ between any distinct faces of one X. Figures are compatible lower subsets with compatibility derived from exclusive faces. An associated atelier chooses a nonempty family of these lower subsets, covering M, closed under lower subfigures and under unions exactly for compatible pairs; refinement is stratumwise. At1–At2 use the strong complete join-prime definition from VI12. The earlier canceled Mag list on VII110 is not the final system.',
  'Final reconstruction/axiom formulation, preceded by canceled drafts.',check='Exact final definitions consolidated; full proof of every axiom equivalence not claimed beyond the manuscript’s argument.')
C(7,51,[(14,[114]),(7,[61])],
  'Magfin and the unique atelier with finite figures.',
  'If every principal face ideal ↓X is finite, the finite compatible lower subsets of M form the unique associated atelier all of whose deployments are finite. Conversely such an atelier forces every ↓X finite. The displayed formula at VII114 omits “lower”; without it singleton subsets containing a nonminimal stratum violate AtM1. This lowerness is an analyst-explicit repair pending scan verification.',
  'Claim and short explanation; formula-level omission.',check='Corrected statement directly follows from principal ideals and finite compatible unions; literal formula is incomplete.')
C(7,52,[(13,[104,105]),(14,[111])],
  'Common-refiner lifting forced by δ and least receiving strata.',
  'If Z refines compatible X,Y, take its least receiving faces X₀≤X,Y₀≤Y. If they were distinct exclusive faces, compatibility and stability of δ under immediate refinement would imply ZδZ, contradicting irreflexivity. Hence the receiving faces must be reconciled through a common face, yielding the stated common-refiner lifting. The argument uses δ-stability on both variables and the least, not merely a minimal, receiving face.',
  'Proof sketch leading to the final reduced axiom system.',check='Logical role of leastness and δ-stability recorded; no substitution of the canceled minimal-receiver axiom.')
