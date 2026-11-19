"""Serialize manually checked link decisions; external endpoints stay quarantined."""
import csv,json,pathlib
B=pathlib.Path(__file__).resolve().parents[1]
I={x['id']:x for x in json.loads((B/'items.json').read_text())}
C={x['id']:x for x in json.loads((B/'claims.json').read_text())}
R={x['key']:x for x in json.loads((B/'references.json').read_text())}
links=[]; leads=[]
def add(kind,fr,to,what,evidence,nums):
    ids=[f'SA14-{x}' for x in nums]
    links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=';'.join(sorted({s for i in ids for s in I[i]['sources']}))))
def folder(fr,to,what,evidence,nums):add('folder',fr,to,what,'Both supplied transcription endpoints read. '+evidence,nums)
folder('57:80–87; K57-04:156–294 and K57-05:1–22','57:89–94; MPL_57_089-132:1–100','Divisor dlog, principal-parts splitting and the relative obstruction sequence precede the Poincaré extension calculation.','C-SA14-001–010; no integrability is stated in the initial definition. The cancelled Guetta letter at82 does not date the mathematics.',[12,13,14,15])
folder('57:88; K57-05:39–67','57:91–94; MPL_57_089-132:21–100','The cancelled pullback-torsor interpretation and the surviving dual-torsor construction concern the same universal-extension programme.','C-SA14-142 is a separate cancelled question; the absolute-connection fragment at94 is C-SA14-010.',[13,14,15])
folder('57:97; MPL_57_089-132:119–154','57:99–100; MPL_57_089-132:156–234','The restriction table is followed by a geometric generic-hyperplane argument for affine groups.','C-SA14-011–025. Distinguish ordinary/general hyperplanes, the original k-defined source and geometric generic base change.',[17,18,19,20,21,22])
folder('57:100–101; MPL_57_089-132:225–256','57:126–129; MPL_57_089-132:688–771','Properness of the identity Picard component and descent/representability are related but require different hypotheses.','C-SA14-026–027 versus C-SA14-050–059. Normality is used in the first argument; no blanket representation claim is imported.',[23,24,36,37,38])
folder('57:102–103; MPL_57_089-132:258–312','57:107–108; MPL_57_089-132:378–415','The depth-two extension mechanism reappears in the relative divisor construction.','C-SA14-028–029 and C-SA14-035–036; both sheaf extension and descent data must be checked.',[25,26])
folder('57:104–110; MPL_57_089-132:314–481','57:112; MPL_57_089-132:494–550','The Seshadri-style parameter-space construction is followed by unresolved hypotheses on the induced relation.','C-SA14-030–041; universal openness of support is not automatically openness or flatness of the relation.',[26,27,28,29])
folder('57:115; MPL_57_089-132:581–605','57:126–129; MPL_57_089-132:688–771','The nonaffine-target counterexample and later proper descent both concern extending maps from a complement.','C-SA14-045 and C-SA14-050–059; the affine-target hypothesis cannot be discarded.',[31,36,37])
folder('57:121–125; MPL_57_089-132:634–686','57:126–129; MPL_57_089-132:688–771','Incidence and zero-class questions prepare the descent application, but do not prove it.','C-SA14-047–049 versus C-SA14-050–059; the incidence claim has no completed proof in the supplied text.',[33,34,35,36])
folder('57:127–128; MPL_57_089-132:707–753','57:129; MPL_57_089-132:755–771','Two-piece gluing and Picard representability are adjacent applications of descent.','C-SA14-051–059. The actual coupled equalizer is checked; substituting separate equalizers loses the gluing equation.',[36,37,38,39])
folder('57:226–231; MPL_57_226-270:1–111','57:254–260; MPL_57_226-270:537–706','The 6 July 1962 Hironaka letter summarizes the analytic Picard completion theorem later expanded in French.','C-SA14-070–082. The necessary-and-sufficient finite-length condition occurs in both; the finite-level image statement is separately quantified.',[11,46,47,48,49,50,51])
folder('57:235–245; MPL_57_226-270:171–440','57:258–260; MPL_57_226-270:647–706','The formal Picard ML argument supplies a key algebraic input for projectivity and comparison.','C-SA14-100–116 versus C-SA14-070–089. Finite generation of components alone does not imply ML.',[53,54,55,56,57,58,59,60])
folder('57:245; MPL_57_226-270:418–440','57:264–268; MPL_57_226-270:790–896','The formal projectivity corollary is reused in the analytic-local algebraic theorem.','C-SA14-085,087,089. Coherent formal existence and proper GAGA are different inputs; the abstract-formal case requires a compatible ample line bundle.',[60,63,69,79])
folder('57:229–231; MPL_57_226-270:65–111','57:260–268; MPL_57_226-270:682–896','The letter’s punctured-spectrum questions lead to the later resolution and exceptional-divisor argument.','C-SA14-090–099. Étale-neighborhood descent, henselization and direct descent to the original local ring remain distinct.',[65,66,67,68,69,70])
folder('57:227–228; MPL_57_226-270:8–63','57:239–245; MPL_57_226-270:279–440','The analytic exponential sequence and algebraic infinitesimal Picard ML proofs use different group-theoretic mechanisms.','C-SA14-080 and C-SA14-105–116. Oort’s nilpotent deformation input is not Oda’s later de Rham/Dieudonné result.',[16,46,55,56,57,58])
folder('57:232–234; MPL_57_226-270:113–169','57:236,238,240,242,244; MPL_57_226-270:195–215,235–277,303–323,353–377,400–416','Reused primary-decomposition and linear-system sheets are interleaved with the Picard handwriting.','C-SA14-118–134; printed/reused statements are not automatically Grothendieck’s new claims or dates for surrounding writing.',[88,90])
folder('57:247–253; MPL_57_226-270:450–535','57:265,267,269; MPL_57_226-270:812–833,854–867,898–911','The reused Zariski-main-theorem and calculus sheets constitute separate documentary sequences.','C-SA14-135–139; an incomplete lemma is retained as incomplete, while the bilinear product rule is independently checked.',[89,93])

# Published-work links: an exact opened reference and its verified locator form the second endpoint.
pubs=[
(14,'PE_MazurMessing1974','I.2.6.7, printedp24; §3, p26 onward','The abelian universal-extension identification uses rigidified/integrable group-compatible connections; this is narrower than arbitrary connections.','C-SA14-001–010,142'),
(16,'PE_Oda1969','Corollaries5.11–5.12, printedpp131–132','Abelian de Rham/Dieudonné identification and a general smooth-proper injection; no arbitrary canonical splitting.','C-SA14-024–025; comparison itemSA14-16'),
(17,'PE_SGA2','ExposéXII.3.6,4.8–4.10','Conditional integral Picard restriction and stabilized neighborhoods; the no-vanishing question is retained.','C-SA14-011–018'),
(19,'PE_CotnerZavyalov2024','Theorems3.3.5,3.4.4; Corollary3.4.5; Examples3.3.6,3.4.6','Modern finite-commutative flat-cohomology/Picard Lefschetz results retain syntomic, strong-ampleness or Hodge hypotheses.','C-SA14-013–025'),
(23,'PE_FGAVI1962','§2, Theorem2.1, printedp231 and proofp232','Properness of Pic0 for a normal proper variety.','C-SA14-026'),
(24,'PE_Weibel1991','Proposition7.4, printedpp370–371','Normal noetherian schemes have the stated Laurent Picard invariance; evaluation at1 also checks injectivity.','C-SA14-027'),
(26,'PE_EGAIV4','§21.14.3, printedpp325–328; §21.14.4(iv), pp328–329','Published divisor/quotient construction with smoothness and normality assumptions, plus a product case with geometrically normal fibres.','C-SA14-030–038; this is a hypothesis comparison, not validation of every preliminary variant.'),
(37,'PE_FGAV1962','Proposition6.3 and Corollary6.4','The two-piece effective gluing result is an exact restricted descendant of the handwritten gluing argument.','C-SA14-051–054'),
(38,'PE_Stacks0D2C','Proposition99.11.8, tag0D2C','Proper flat finite-presentation and universal f_*O=O give a Picard algebraic space. A scheme conclusion needs more.','C-SA14-055–059'),
(41,'PE_FGAI1960','§B.1, Theorem2, Lemma1.2, printedp317; Theorem3, p318','Projective/quasiprojective descent with precise finite or quasi-finite cover hypotheses.','C-SA14-060–063'),
(42,'PE_FGAI1960','§B.1, Remark before Theorem2, printedp317','Nagata’s proper dimension-two noneffective descent example is mentioned; the handwritten inserted dimension/simple-point modification is not settled by that sentence.','C-SA14-061'),
(43,'PE_Stacks009E','Tag009E, Limits and colimits of sheaves','Sheaf limits are sectionwise.','C-SA14-064'),
(43,'PE_Stacks01AJ','Tag01AJ, Pushforward and pullback','Pushforward commutes with limits; its stalk formula is a neighborhood colimit, not generally one fibre.','C-SA14-065'),
(44,'PE_Stacks0913','Lemma15.30.6, tag0913','Čech cohomology as a colimit of Koszul complexes.','C-SA14-066'),
(46,'PE_Grauert1960','§6, HauptsätzeI,II,IIa, printedp59','Coherent direct images and formal/cohomological comparison supply inputs, not a quoted exact Picard iff theorem.','C-SA14-070–082'),
(47,'PE_Lojasiewicz1964','§3, Theorems1–2, printedpp463–464','Semianalytic triangulation; global abstract-space input is distinguished.','C-SA14-074'),
(47,'PE_Goresky1978','§5, Proposition, printedp199','Triangulation of abstract stratified objects supplies a global topological route once compatible stratification is available.','C-SA14-074'),
(55,'PE_KreschMathur2025','Theorem11.11; §§11.8–11.9','Actual Picard ML in characteristic zero; the NS and rational-point steps are separate.','C-SA14-100–116'),
(58,'PE_KreschMathur2025','Theorems1.1 and9.3','In the proper smooth complete-DVR characteristic-p setting, ML is equivalent to constant Néron–Severi rank; rank-jump examples prevent blanket extension.','C-SA14-115'),
(60,'PE_Formal1959','Exposé182, §3, Theorems1–4, printedpp196–198','Coherent formal existence and algebraization require their distinct hypotheses.','C-SA14-085; an abstract formal scheme is not silently treated as already algebraic.'),
(63,'PE_AbramovichTemkin2019','§6.3.4, printedp411; AppendixB and TheoremC.1.1, p419','Proper coherent GAGA over complex affinoid germs includes radius-zero analytic local germs.','C-SA14-087,089'),
(65,'PE_Mumford1961','Printedp16, exceptional-divisor quotient','The resolution formula for the punctured Picard group; this is not an identification of the letter’s unidentified formal nonalgebraizability example.','C-SA14-090–095'),
(69,'PE_Elkik1973','III.1, Theorem3, printedp569; Picard corollarypp573–574','For a noetherian henselian pair(A,J), compare the complement ofV(J) with the same complement after J-adic completion.','C-SA14-096; arbitrary different opens with m-adic completion remain separate C-SA14-097.'),
(90,'PE_WeilExtension','Milne Abelian Varieties, I Theorem3.2, printedp17','Rational maps from a nonsingular variety to an abelian variety extend. This checks the pencil’s Jacobian input; the exact VA edition is unidentified.','C-SA14-131'),
(93,'PE_StrictDerivative','Definition3.1, Theorem5.3, Remark5.7','Strict differentiability supplies the correct inverse-function setting over complete valued fields.','C-SA14-136'),
]
for num,key,loc,what,evidence in pubs:
    add('published work',f"{I[f'SA14-{num}']['lines']}; scans {','.join(map(str,I[f'SA14-{num}']['scans']))}",f"{key}: {loc}; {R[key]['url']}",what,'Primary endpoint opened/read in this run. '+evidence,[num])

def lead(label,nums,target,what,status='quarantined: external endpoint not supplied or independently checked'):
    ids=[f'SA14-{n}'for n in nums]
    leads.append(dict(kind='other project',**{'from':'; '.join(i+': '+I[i]['lines']for i in ids),'to':target},what=what,evidence=status,note_ids=';'.join(sorted({s for i in ids for s in I[i]['sources']})),run_names=label))
lead('CN F6–F8; WG2 §2.4 #4; same-cote first pass F01–F02',[1,2,3],'CT cote47:7–8; CN F6–F8; SC/SN57:283–288,294,297,310','The proposed derived Poincaré Fourier morphism, admitted vanishing lemma and actual unit-fibre map are three separate proof tasks. These packages provide no completed witness.')
lead('CN D08; WG2 §2.3 #12 and §2.4 #4; SN J01',[4],'CT cote44:2 Theorem1; SC/SN57:275–277,306','Ordinary Picard and descent do not construct the all-codimension parameter-cycle kernel.')
lead('CN D09–D10; WG2 §2.3 #12 and §2.4 #4; SN J02',[5],'CT cote44:2 Theorem2 and44:8; SC/SN57:285,291–292,313','Degree-one calculations do not supply the proposed half-odd-Betti-number bound in every codimension.')
lead('CN D08/D11; WG2 §2.3 #12 and §2.4 #4; SN J03',[6],'CT cote44:2 Theorem3 and44:8; SC/SN57:276–277,283–286,313','Pic0 and Albanese endpoints do not establish higher Jacobian representatives or complementary-degree duality.')
lead('CN D13; WG H9; WG2 §2.3 #12 and §2.4 #4; SN J04',[7],'CT cote44:2 Theorem4 and44:9; SC/SN57:280–281','Lifting an already ample line bundle does not prove positivity of the particular middle-Jacobian correspondence.')
lead('CN D12; WG H9; WG2 §2.3 #12 and §2.4 #4; SN J05',[8],'CT cote44:4 Theorem5; SC/SN57:289–290,314–315','No Néron–Tate/intersection height formula, vertical correction or sign computation occurs here.')
lead('WG2 §2.3 #12 and §2.4 #4; SN J06; Hua H pp96–102',[9,17,19],'CT cote44:4 Theorem6; SC/SN57:309(h)','Divisor-level hyperplane comparison does not imply the all-codimension fixed-factor assertion.')
lead('CN D14; WG2 §2.3 #12 and §2.4 #4; SN J07/P04',[10],'CT cote44:6 Theorem7; SC/SN57:275,314–315','Picard torsion/component arguments do not identify numerical and tau equivalence for arbitrary cycles.')
lead('WG2 §2.4 #4 chronology; SC §9 T07',[11],'CT cote44:8 dateline12.8.1964; SC57:299,301,303 Tribu material','Only the Hironaka letter’s6July1962 date is local evidence. The other dateline and reused-page dates cannot date undated neighboring handwriting.')
lead('Hua modernized reading H79–93; CN D01; SC D07; WG2 §1.1 #3',[12,13,14,15],'CT cote54:3; context/hua_project/57.modern.tex; SC57:287–288,294','Hua’s interpretation and a mixed-class calculation are useful proposed comparisons, not diplomatic witnesses or completion of the unfinished mixed identity.')
lead('Hua/CN; SC D04,D05,D07,D08',[16],'CT cote54:3,5–7; SC57:285–288,291–292,294,297,309–311','The Oda primary result was independently opened, but its alleged relation to these absent contextual files is not verified.')
lead('Hua finding57-analytic-pic-completion-criterion; RS; H57 §§1–2',[46,47,48,49,50,51,55,60,62,63],'context/hua_project/57.modern.tex; context/notes/RESULTS_STATE.md','The source asserts a theorem and an iff; this corrects the notes’ report of a conjecture label without pretending to have opened or edited the external register.')
lead('Hua finding57-generic-hyperplane-h1-injective; RS; H57',[19,20,21,22],'context/hua_project/57.modern.tex; context/notes/RESULTS_STATE.md','The manuscript’s original-field source and its uncertain group/topology must be retained when comparing the proposed finding.')
lead('WG H1,H2,H9; WG2 §1.1 #3,§2.3 #12,§2.4 #4; RS',[1,4,7,8,9,46,55,65,68],'context/notes/RESULTS_STATE.md; CR research-context orientation','Unchecked hunches and planning items remain contextual leads. No reviewed external project result is inferred from a shared keyword.')
lead('SN P02/P03; Hua H57; RS',[46,49,67,69],'context/same_cote_57/MPL_57_271-315_notes.md; scans271–274','Later same-cote first-pass notes reportedly distinguish finite-image descent from full completion comparison. Until the other part supplies a checked endpoint, this is a quarantined cross-part lead.')
for name,rows,fields in [('links.tsv',links,['kind','from','to','what','evidence','note_ids']),('project_leads.tsv',leads,['kind','from','to','what','evidence','note_ids','run_names'])]:
    with (B/name).open('w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
(B/'outputs/build_links.json').write_text(json.dumps({'checked_links':len(links),'quarantined_leads':len(leads)},indent=2)+'\n')
