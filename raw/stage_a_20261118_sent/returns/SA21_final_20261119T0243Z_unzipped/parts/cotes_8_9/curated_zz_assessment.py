# Manual literature decisions. Grouping below means the same checked comparison
# applies to each listed claim; it is not an automatic classification by keywords.
byid={c['id']:c for c in claims}
assessments={}
def F(numbers,cls,fate,refs,searches,present=None,confidence=None):
    for number in numbers.split():
        cid='C-SA21-'+number
        assert cid in byid and cid not in assessments,cid
        c=byid[cid]
        c['class']=cls;c['fate']=fate+' Search record: '+', '.join(searches)+'.';c['refs']=refs
        c['present_status']=present or ('As of 2026-11-19: retain the exact on-page status and hypotheses above; '+('no exact external treatment located in the documented searches, which does not establish nondevelopment.' if cls=='D' else 'the cited result has only the scope specified in the fate comparison.'))
        if confidence:c['confidence']=confidence
        assessments[cid]={'class':cls,'search_ids':searches,'refs':refs}

F('8-001 8-005 8-006 8-010 8-011 8-012 8-018 8-019 8-018R', 'D',
  'Exact French and English terminology searches located the archive, catalogue and Malgoire’s 2002 introductory seminar, but no published theorem with these carrier, compatibility and local-axiom packages. The seminar confirms discussion of the programme, not validation of these claims. The weakened-face issue is independently separated in our finite audit.',
  ['MontpellierSA21','CSGUnpublished','Malgoire2002'],['S01','S04','S07','S10','S12'])
F('8-009 8-009R','D',
  'No theorem that nonempty interior lieux imply relational disjointness detection in the stated geometric classes was located. Paseka–Vetterlein2025 Lemma2.3 supplies a precise sufficient density condition for support reduction, not this implication. The unrestricted implication fails in our four-stratum model, while the author’s practical-class qualification remains unspecified.',
  ['PasekaVetterlein2025','CSGUnpublished'],['S01','S04','S06','S10','S12'],present='As of 2026-11-19: L2⇒L1 is valid; unrestricted L1⇒L2 is false by our explicit model. The qualified practical expectation is not a precisely delimited external open problem.')
F('8-002','E',
  'The graph data are already explicit in Serre, Trees (1980), Chapter I §2.1 Definition1, p13: vertices, oriented edges, fixed-point-free reversal and source/target. This identifies the claimed dimension-one core before1986; it does not validate the separate dimension-two extension.',
  ['Serre1980'],['S08','S09','S11'],present='As of 2026-11-19: classical graph encoding; the signed-incidence convention is necessary for loops.',confidence='high')
F('8-003','F',
  'The pages do not specify the category of combinatorial cell complexes or attaching data, so the tentative equivalence cannot be matched as a precise theorem. Björner1984 Definition2.1 and Proposition3.1, pp8,11, characterize regular CW face posets under spherical lower-interval hypotheses; these are not the unspecified oriented maquettes with possible repeated incidence.',
  ['Bjorner1984','Serre1980'],['S08','S11','S13'],present='As of 2026-11-19: insufficiently identified two-dimensional equivalence; a related pre1986 regular-CW theorem is checked but is not a substitute.',confidence='low')
F('8-004 8-015 8-020','E',
  'The lower-set/intersection/union and principal-ideal mechanisms are classical order theory, represented in Birkhoff1948 Chapter IV §§1,7. The source specializes them to compatible lower sets; our E label concerns that mathematical mechanism and does not claim the word magasin or its full axiom package was already standard.',
  ['Birkhoff1948'],['S03','S04','S10'],present='As of 2026-11-19: standard order-theoretic construction, with the stated restriction to existing compatible joins and nonempty intersections.')
F('8-007 8-008 8-013','D',
  'SGA4 I, ExposéII Definition2.1 and Corollary2.4 give the pre1986 sheaf equalizer/gluing pattern. No result proving these precise magasin restriction maps, local refinement conditions and AtFil hypotheses was located. This is a comparison with a formal pattern, not an identification of the custom theorem with a published sheaf theorem.',
  ['SGA4I1972','Malgoire2002'],['S01','S04','S08','S09','S15'])
F('8-014 8-021 8-024 8-025','D',
  'The ordered-family, least-membership and representation mechanisms were compared with Birkhoff1948 order/polarity results and exact programme searches. No publication of these exact indexed-figure equivalences was located; generic poset or lattice representation results do not supply the missing magasin hypotheses.',
  ['Birkhoff1948','CSGUnpublished'],['S01','S03','S04','S10','S12'])
F('8-026','D',
  'Exact terminology and indexed-support searches did not locate these two infinite-family counterexamples in external literature. They are nevertheless fully established internally by the explicit natural-number-tail model in this audit; class D records only the bounded external-search outcome.',
  ['Birkhoff1948','CSGUnpublished'],['S01','S03','S04','S12'],present='As of 2026-11-19: the two weakened implications are refuted; the complete indexed-family proposition is unaffected.',confidence='high')
F('8-016 8-017','D',
  'No exact publication of the polyhedral-refinement construction or its stricter figure compatibility was located. Björner1984 §2.3 explains the meet-semilattice distinction for simplicial face posets, a relevant pre1986 comparison but not a theorem about these refinement relations. The circle-with-two-arcs example remains an internal illustration.',
  ['Bjorner1984','Malgoire2002'],['S01','S07','S11','S13'])
F('8-022 8-023 8-028 8-029 8-031','D',
  'No exact treatment of the face-bijective versus optional-face-bijection comorphisms, zero elementary images, or induced-submagasin axioms was located. Orthoset morphisms in Paseka–Vetterlein2025 forget incidence and face transport, so they do not settle these questions. The dated marginal weakening is retained as source evolution.',
  ['PasekaVetterlein2025','CSGUnpublished','Malgoire2002'],['S01','S04','S06','S07','S12'])
F('8-027','D',
  'Inverse-image and projection-formula identities are familiar set operations, but no external theorem for the author’s rule deleting strata with empty interior pullback was located. SGA4’s sheaf formalism does not identify this particular set-figure construction, and it is not used as a claimed resolution.',
  ['SGA4I1972','CSGUnpublished'],['S01','S04','S09','S12','S15'])
F('8-030 8-030R','D',
  'The proposed extension was compared with order-theoretic join-generation and exact atelier searches; no exact external treatment was located. Our two-stratum counterexample establishes that monotonicity without image compatibility is insufficient. General lattice-generation principles cannot remove this missing premise.',
  ['Birkhoff1948','CSGUnpublished'],['S01','S03','S04','S12'],present='As of 2026-11-19: the unrestricted elementary-map extension is false; retain only the qualified join/meet criteria and the separately labelled counterexample.',confidence='high')
F('8-032 8-033 8-036 8-037 8-038 8-039','D',
  'No exact external theorem for these external-support representations or full-faithfulness axioms was located. Birkhoff1948 verifies the polarity background, but an order embedding of a support ortholattice into a powerset need not preserve its meets or complement. Malgoire2002 names supports/shadows and refinements without supplying these results. The author’s 2July correction and local-in-one-figure Boolean scope are preserved.',
  ['Birkhoff1948','Malgoire2002','CSGUnpublished'],['S01','S03','S04','S07','S12'])
F('8-034 9-022 9-025','E',
  'Birkhoff1948 Chapter IV §5 Theorem9 and its Corollary, pp54–56, prove closure by double polarity and the symmetric/antireflexive complete ortholattice structure; the same section includes the null-element variant. §6 Theorem10 gives the Galois-connection abstraction. Complete-ortholattice reconstruction from its orthogonality is also checked directly in our audit; Paseka–Vetterlein2025 Proposition2.4/Remark2.5 states the modern version. The elementary support mechanism was therefore known before1986.',
  ['Birkhoff1948','PasekaVetterlein2025'],['S03','S04','S06','S14'],present='As of 2026-11-19: established complete ortholattice theory; no global Boolean or locale conclusion follows.',confidence='high')
F('8-035','B',
  'Paseka–Vetterlein2025 Lemma2.3 gives the same restriction/double-polar inverse isomorphisms when every ambient singleton has the same perpendicular as a subset of the smaller orthoset. Under MogL2 take that subset to be omb°X in the lieux, adjoining a universal zero if desired. Thus the precise support-reduction theorem has an explicit later established generalization. This is an independent mathematical match, not evidence of historical influence; its broad polarity mechanism is older (Birkhoff1948). The manuscript’s deferred two-set generalization is ordinary polarity in that older source.',
  ['PasekaVetterlein2025','Birkhoff1948'],['S03','S04','S06','S14'],present='As of 2026-11-19: the support restriction theorem is covered by an explicit later orthoset lemma under matched hypotheses; no conclusion about all additional atelier structure.',confidence='high')
F('8-040 8-041 8-042 8-043 8-044 8-046 8-047 8-048 8-049 8-050 8-051 8-052','C',
  'Jenča2023 (preprint16June2022) §4 uses exactly the interval-containment and separation formulas on PROPER nondegenerate intervals, proves the finite orthogonal-family flag lemma (4.1), and gives support results including Theorems4.10 and4.12 under finite-bounded/bounded hypotheses. Grothendieck additionally includes point strata, incidence, arbitrary endpoint patterns and polygon support formulas. Those extra claims, H-dependencies and flagged proof obligations are not resolved by Jenča’s results; no exact full match was located in the further programme searches.',
  ['Jenca2023','Birkhoff1948','CSGUnpublished'],['S01','S03','S04','S05','S06','S07','S14'])
F('8-045 8-045R','D',
  'No external publication of this five-stratum calculation was located. Comparison with Jenča’s proper-interval model is insufficient because the disputed computation concerns a POINT stratum. Our exact calculation refutes the printed singleton cosupport but confirms the independent whole-figure counterexample.',
  ['Jenca2023','CSGUnpublished'],['S01','S04','S05','S14'],present='As of 2026-11-19: printed singleton computation false under the given formulas; C-SA21-8-045R supplies the corrected computation without deciding the ink.',confidence='high')
F('9-001','D',
  'Exact searches for ateliers, contrées and spatios located historical presentation and catalogue material, not a proof of the full taxonomy diagram. The diagram itself explicitly leaves moderation/spatiality/faithfulness and LS=S∩Div questioned; these remain reading-qualified proposals until the later IX treatment is reconciled.',
  ['CSGUnpublished','Malgoire2002'],['S01','S04','S07','S10','S12'])
F('9-002','C',
  'The lattice-theoretic part is classical: a distributive ortholattice is Boolean. Paseka–Vetterlein2025 Lemma2.9 characterizes when singleton closures are atoms, giving a precise modern criterion relevant to the lieu question. Neither this criterion nor complete distributivity proves that all atelier lieux meet it, or that moderation implies faithfulness; no exact theorem for those added implications was located.',
  ['Birkhoff1948','PasekaVetterlein2025'],['S03','S04','S06','S14'])
F('9-003 9-004 9-005 9-007 9-008 9-009 9-010 9-011 9-012 9-013 9-014 9-015','C',
  'Jenča2023 §4 supplies an independently published proper-interval orthogonality model with the same endpoint-separation formula and chain-type calculations; §5 relates it to the Kalmbach construction. It omits Grothendieck’s point strata, formal half intervals, whole-interval symbol, boundary conventions and residual atelier structure. Consequently it does not settle the complete complement calculus or its draft inconsistencies; the exact full statements were not found in the documented searches.',
  ['Jenca2023','CSGUnpublished'],['S01','S04','S05','S06','S07','S14'])
F('9-006','C',
  'Paseka–Vetterlein2025 Lemma2.3 proves the generic dense-suborthoset support isomorphism with an explicit perpendicular-detection hypothesis. This matches the claimed support mechanism, but does not validate the inconsistent draft half-interval formulas on IX10 or prove that those particular data satisfy density.',
  ['PasekaVetterlein2025','Birkhoff1948'],['S03','S04','S06','S14'])
F('9-016 9-017 9-018','D',
  'Programme and orthogonality-category searches did not locate these exact incidence/refinement direct-sum or residual-subatelier statements. Orthoset subspaces alone lack the carrier-lifting condition. The triangle counterexample and the large-residual carrier argument were checked directly in our audit.',
  ['PasekaVetterlein2025','Malgoire2002','CSGUnpublished'],['S01','S04','S06','S07','S12'])
F('9-019 9-020','D',
  'Ehrhard’s Finiteness spaces, author preprint20October2003, §1 p4, published2005, gives a finite-intersection polarity and downward/finite-union closed families. This is a useful comparison, but its objects and duality omit the magasin carrier/compact-stratum axioms. No exact development of this compactology or the proposed Borel–Lebesgue/richness axiom was located; analogy alone is not coded as resolution.',
  ['Ehrhard2005','CSGUnpublished'],['S04','S06','S07','S09','S10','S12'])
F('9-021 9-023 9-024 9-026 9-027','D',
  'Exact searches found the programme’s names and later exposition but no published theorem reconstructing the complete ordered-deployment/face-refinement atelier structure. The ortholattice part is standard, while the independent face order and compatibility are additional data. AtSpat(Σ) is therefore not identified with an arbitrary known locale, topos or orthoset category.',
  ['Birkhoff1948','PasekaVetterlein2025','CSGUnpublished','Malgoire2002'],['S01','S04','S06','S07','S10','S12','S14'])
F('9-028','C',
  'Paseka–Vetterlein2025 Proposition2.4 reconstructs an orthoposet’s MacNeille completion from a join-dense orthoset; for complete Σ it gives exactly the support-reconstruction core. Grothendieck’s additional face-closed collection of ordered spatial figures is not treated there. Our direct proof verifies the dense case without invoking the subsequently failed unrestricted functoriality claim.',
  ['PasekaVetterlein2025','Birkhoff1948'],['S03','S04','S06','S14'],present='As of 2026-11-19: support core has an exact modern counterpart; full atelier representation checked by direct reconstruction under the stated face-closure and join-density hypotheses.',confidence='high')
F('9-029 9-030 9-030R','C',
  'Paseka–Vetterlein2025 Definition3.1, Lemmas3.5–3.7 and Theorem6.7 establish closure compatibility and a functor for ADJOINTABLE single-valued orthoset maps. Mere disjointness-preserving correspondences, as initially used here, do not satisfy these statements; our finite counterexample and the author’s complement counterexample show why extra hypotheses matter. The later result does not supply the full arbitrary-correspondence or atelier-morphism theory.',
  ['PasekaVetterlein2025','Birkhoff1948'],['S03','S04','S06','S08','S14'],present='As of 2026-11-19: unrestricted formulas fail; adjointability gives a verified later sufficient hypothesis for closure/functoriality, without automatic complement preservation.',confidence='high')

assert set(assessments)==set(byid),sorted(set(byid)-set(assessments))
(OUT/'claim_search_map.json').write_text(json.dumps(assessments,ensure_ascii=False,indent=2)+'\n')

# Refinement of on-page status versus independent audit outcomes.
byid['C-SA21-8-030']['computation']='Own finite counterexample to the unrestricted extension: C-SA21-8-030R, proof_audits.md §G and computations_output.txt. Other join/meet assertions retain their individual source qualifications.'
byid['C-SA21-8-018']['computation']='The claimed full equivalence fails if the written comparable-pair axiom is the entire condition; exact separating model C-SA21-8-018R. A spatial-figure well-typedness premise could restore the missing condition.'
byid['C-SA21-9-030']['computation']='Two distinct exact counterexamples in computations.py: author’s nonsurjective injection refutes complement preservation; C-SA21-9-030R refutes the weaker closure formula. Valid inclusion re-proved in proof_audits.md §C.'
byid['C-SA21-9-028']['computation']='Independent direct polarity proof using join-density, proof_audits.md §B; no appeal to the failed general sorite.'
byid['C-SA21-9-012']['computation']='2n+1 strata gives 2^(2n+1) subsets; exact support enumerations for chain models n=1,2,3 give8,32,128. This is not a general arbitrary-poset proof.'

# Date/status of bibliographical matches is distinct from mathematical confidence.
for r in readings:
    if r['line']=='J156-9-08:109-115':
        r['evidence']='The displayed condition is weaker than modern strict irreflexivity, but Birkhoff1948 chIV§5 explicitly uses antireflexive in this same broader null-element sense. Terminological cross-reference, not an ink correction or authorial mathematical error.'
        r['weight']='low';r['confidence']='high'

# Required links-kind vocabulary. Detailed change type remains in the explanation.
for link in links:
    if link['kind'] not in ['folder','published work','our projects']:
        link['what']='['+link['kind']+'] '+link['what'];link['kind']='folder'
