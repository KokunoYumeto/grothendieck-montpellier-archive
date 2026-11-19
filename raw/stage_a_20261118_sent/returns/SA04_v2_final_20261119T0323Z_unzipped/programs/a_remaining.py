"""Serialize authored problem, reading, link and reference registers.
No verdict or mathematical status is inferred automatically.
"""
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parents[1]/'parts/a'
OUT.mkdir(parents=True,exist_ok=True)
P='cote93, pro/MPL_93_047-091_transcription.tex'
K='cote93, codex/K93-12_transcription.tex'
problems=[]
def prob(n,title,occ,his,today,art,why,worth,refs):
    problems.append(dict(id=f'MP-SA04-{n:02d}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs))
prob(1,'Full faithfulness and essential image of ordinary Dieudonné crystals',
 [K+', scans39–44, lines218–310; C-SA04-3,8'],
 'Problem1 asks full faithfulness on every characteristic-p base and whether its image is precisely the admissible FV-crystals; the proposed admissibility is existence of the canonical direct-summand Hodge filtration.',
 'Retain the exact base and the precise extra structures: perfect-ring Dieudonné equivalence, excellent lci full faithfulness, or the quasi-syntomic prismatic equivalence are established formulations. Ordinary crystals on arbitrary bases cannot be assumed fully faithful.',
 'As of2026-11-19: de Jong ICM1998 §2(x) explicitly records the Berthelot–Messing counterexample over Fp[x,y]/(x²,xy,y²). Lau6.4 settles perfect rings; de Jong–Messing1999 gives excellent-lci full faithfulness; Anschütz–Le Bras1.4.4 gives quasi-syntomic prismatic classification. Their structures/hypotheses differ.',
 'The manuscript says the missing finite-flat theory would clarify the problem. The published counterexample explains failure of the unrestricted hope; no historical reason for abandonment beyond that is inferred.',
 'Worth a focused comparison of the handwritten admissibility condition with precise divided/prismatic data, because simply citing modern classification hides the lost hypotheses.',
 ['deJongICM1998','BerthelotMessing1990','deJongMessing1999','Lau2013','AnschutzLeBras2023'])
prob(2,'Finite flat and truncated Dieudonné theory',
 [K+', scans39–40, lines220–226; C-SA04-4'],
 'Develop a theory for arbitrary finite locally free p-groups, possibly using a filtration on a derived object; over perfect S, give the anti-equivalence for groups flat over Z/p^n and locally free Witt modules with usual FV conditions.',
 'Over perfect rings use admissible torsion Dieudonné modules for all finite p-groups and level-n projective Dieudonné modules with the exact level-one kernel/image and projectivity conditions for truncated BT groups. Over broader bases extra divided/prismatic structure is essential.',
 'Lau2013 Definition6.1, Theorem6.4 and Corollary6.5 give exact perfect-ring categories. Anschütz–Le Bras2023 §5.1 treats finite locally free p-primary groups in the quasi-syntomic setting.',
 'The text expressly says the additional structures have not been isolated and speculates about a derived filtration. No identification with a modern construction is asserted without a comparison.',
 'Worth an expository reconstruction of the category distinction; a few hours can establish an exact dictionary, not a new arbitrary-base classification.',
 ['Lau2013','AnschutzLeBras2023'])
prob(3,'Deformation theory for finite flat p-groups',
 [K+', scan43, lines269–271; C-SA04-7'],
 'Find a variant of the BT deformation theorem for finite locally free p-groups; the margin says there is a candidate but supplies none.',
 'Fix a finite flat/truncated-BT category and nilpotent PD thickening; formulate deformations with the extra structures required by a chosen established theory. The unwritten candidate cannot be recovered uniquely.',
 'Illusie1985 reconstructs Grothendieck’s truncated-BT deformation theorem and discusses the proof route. Anschütz–Le Bras §5.1 provides a later finite-flat classification on quasi-syntomic bases, rather than a theorem on every base mentioned by the manuscript.',
 'Illusie’s introduction explicitly explains how Raynaud’s local embedding result simplifies the route through BBM; the source itself says only that a candidate exists.',
 'Worth locating the candidate in adjacent seminar material before proposing any new theorem, because the present leaf does not determine its statement.',
 ['Illusie1985','AnschutzLeBras2023'])
prob(4,'Nilpotent invariance up to isogeny and global bounds',
 [P+', scan49, lines60–73; C-SA04-18,19'],
 'Prove later that restriction across a nilpotent immersion induces equivalence on the globally localized BT categories; quasi-compactness is cancelled and the phrase power of J is doubtful.',
 'Require a single p-power annihilating the ideal, as in the published theorem, or formulate a genuinely local quasi-isogeny category and prove its descent. Local denominators do not glue automatically in Hom⊗Q.',
 'GrothICM1970 §5 p434 gives the bounded-p-ideal theorem. Katz1.1.3 proves uniform lifting of multiples. The disjoint-union example in proof_checks.md independently shows global Hom localization is not a stack.',
 'The page itself flags the stack defect; no source explains why quasi-compactness was cancelled. The mathematical issue is a global denominator bound, not a visual decision about the cancellation.',
 'High value for the companion: fix the exact global category and inspect the p/J glyph before quoting the invariance theorem.',
 ['GrothICM1970','Katz1981'])
prob(5,'Essential image, valuative testing and Zariski openness',
 [P+', scans49,51, lines75;100–108; C-SA04-21–23'],
 'Characterize realizable filtered isocrystals over noetherian p-adically complete rings; ask for a valuative criterion and a Zariski-open Grassmannian locus of admissible two-step filtrations.',
 'Over a complete mixed-characteristic DVR with perfect residue field, weak admissibility is the exact rational criterion; period-domain families require a specified analytic topology and a distinction between classical and general analytic points. A general Zariski-open locus is a different statement.',
 'Colmez–Fontaine §4.1 Theorem4.3 proves weakly admissible equals admissible for filtered(phi,N)-modules over the stated valued fields. Hartl2008 Theorems1.2,3.3,3.5 and Example3.6 give analytic loci and their strict difference at nonclassical points with fixed residue field Fp-bar. These do not settle the exact universal Zariski/valuative wording.',
 'The manuscript acknowledges that rank conditions are insufficient. The sources show why field-point criteria do not automatically identify the relative analytic space; no claim of worldwide openness is made for every reformulation.',
 'Worth isolating the smallest exact Zariski claim and an explicit isocrystal example before expanding the relative question.',
 ['ColmezFontaine2000','Hartl2008'])
prob(6,'The mysterious period functor and its inverse',
 [P+', scans48,49,51,53, lines48;73;106;175–178; C-SA04-24'],
 'Construct explicitly the natural Galois realization of a realizable filtered isocrystal and a quasi-inverse; the local cancellation on48 does not cancel the surviving later questions.',
 'For K complete mixed-characteristic discretely valued with perfect residue field, use D_cris and V_cris on crystalline Qp representations and weakly admissible filtered isocrystals. A rational functor does not choose a Zp lattice.',
 'Colmez–Fontaine Theorem4.3 and its corollary give the semistable equivalence; the N=0 subcategory is crystalline. The source’s two-step BT setting is a restricted weight range, not every filtered isocrystal.',
 'The text calls the construction mysterious but gives no sociological reason for delay. Later period-ring methods give the precise algebraic answer.',
 'Worth a compact notation dictionary from the page to the period-ring functors, including covariance and twists.',
 ['ColmezFontaine2000','GrothICM1970'])
prob(7,'Relative p-adic local systems from filtered crystals',
 [P+', scan51, line108; C-SA04-25'],
 'For general noetherian p-adically complete A, map realizable filtered isocrystals to p-adic locally constant sheaves on Spec(A[1/p]), allowing unspecified additional conditions.',
 'State the base and linear category precisely; for quasi-syntomic bases use prismatic Dieudonné crystals and their étale realization. Pointwise Galois representations alone do not provide transport/descent.',
 'Anschütz–Le Bras §5.4 Proposition5.4.2 identifies the Frobenius-fixed prismatic realization with the dual finite-level generic-fibre local system of a BT group on the associated adic v-site. This is an exact modern relative construction but in a different specified formalism.',
 'No historical reason is documented. The mathematical obstruction to an immediate fieldwise solution is compatibility over the base and the essential-image conditions.',
 'Worth comparing sites and covariance for one formally smooth affine base; a few hours can establish a reliable example rather than every noetherian-base theorem.',
 ['AnschutzLeBras2023','Hartl2008'])
prob(8,'Which Galois lattices arise from BT groups?',
 [P+', scan53, lines173–178; C-SA04-28'],
 'Determine the essential image in Galois modules; Hodge–Tate conditions are recorded as necessary, followed by the filtered-crystal inverse question.',
 'Separate integral Zp lattices, rational crystalline representations and Hodge–Tate representations. Hodge–Tate alone is insufficient; the precise integral BT criterion needs an integral crystalline theory and specified weights.',
 'Tate1967 §4 Theorem3 establishes the Hodge–Tate decomposition for BT groups. Colmez–Fontaine gives rational crystalline admissibility. Anschütz–Le Bras gives the integral BT classification on quasi-syntomic bases and its generic-fibre comparison.',
 'The source does not claim Hodge–Tate sufficiency; no explanation of abandonment is present.',
 'Worth an exact integral-versus-rational comparison with the source’s covariance convention; this prevents a false claim that rational periods recover a unique lattice.',
 ['Tate1967','ColmezFontaine2000','AnschutzLeBras2023'])
prob(9,'Tate full faithfulness in equal characteristic',
 [P+', scans53–54, lines180–184; C-SA04-29'],
 'Remove the characteristic-zero function-field restriction in Tate’s generic-fibre full-faithfulness theorem on normal noetherian integral bases.',
 'The same BT full-faithfulness conclusion holds with no characteristic restriction; normality and the noetherian condition remain.',
 'de Jong1998 Corollary1.2 proves the DVR characteristic-p case; its introduction explains the reduction to this case. de Jong ICM1998 Theorem2 states the normal noetherian integral-base conclusion. The1999 erratum corrects an auxiliary lemma/definition and leaves these theorem statements unchanged.',
 'The manuscript proposes a crystalline route conditionally. The1998 proof establishes the missing theorem; the erratum identifies an actual kernel issue rather than a failure of full faithfulness.',
 'Settled: worth documenting the exact1998 theorem and1999 correction, not recasting it as an open research direction.',
 ['deJong1998','deJongErratum1999','deJongICM1998','Tate1967'])
prob(10,'Generic restriction for ordinary locally free crystals',
 [P+', scan54, lines186–190; C-SA04-30'],
 'Is generic restriction fully faithful for all locally free crystals over a normal noetherian integral characteristic-p base?',
 'A theorem must specify the crystalline site, integrality/isogeny level and any convergence hypotheses. Do not infer it by forgetting the Frobenius condition in a theorem for F-crystals.',
 'de Jong1998 Theorem1.1 concerns nondegenerate F-crystals over a characteristic-p DVR with a p-basis. Searches of Numdam, arXiv, zbMATH-indexed results and backward references did not identify an exact theorem or a complete counterexample for the broader ordinary-crystal wording.',
 'The source immediately offers the weaker F-crystal question. That indicates awareness of a possible missing structure; no further reason is documented.',
 'Worth a precise local restatement and a low-rank extension/counterexample search, because the current broad question is not answered by the cited F-crystal theorem.',
 ['deJong1998','deJongICM1998','BerthelotMessing1979'])
prob(11,'Generic restriction for F-crystals',
 [P+', scan54, line190; C-SA04-31'],
 'At least establish the generic full-faithfulness statement for F-crystals.',
 'For a DVR of characteristic p admitting a p-basis and nondegenerate Frobenius, generic restriction of F-crystals is fully faithful. A global extension beyond that setting needs its own reduction theorem.',
 'de Jong1998 Theorem1.1 is the exact local theorem; de JongICM1998 §1 defines nondegenerate as kernel and cokernel killed by a p-power. The erratum does not modify Theorem1.1.',
 'The page weakens the question but does not supply a proof; later crystalline analysis addresses the local case.',
 'Worth recording the p-basis and nondegeneracy qualifiers in the companion; broader research should start from the precise local/global gap.',
 ['deJong1998','deJongErratum1999','deJongICM1998'])
prob(12,'Reduction to formal connections and the perfect closure',
 [P+', scan54, lines184–192; C-SA04-32,33'],
 'Reduce to a one-variable complete local ring over an algebraically closed field, express crystals as modules with formal connections, and descend from the perfection using a faithful Dieudonné theory.',
 'Keep quasi-nilpotence, continuity, the crystalline lift and horizontal nondegenerate Frobenius; k[[t]] must be distinguished from k((t)). The group theorem’s reduction does not automatically establish all ordinary-crystal variants.',
 'Berthelot–Messing1979 §1 Lemma1 describes the perfect-closure strategy and its field case; de Jong1998 introduction gives the precise Tate reduction and Theorem1.1 the F-crystal result. Lau6.4 supplies perfect-ring classification.',
 'The source explicitly makes the route conditional on Problem1 and says it seems to imply the desired result. No completed reduction is printed there.',
 'Worth a dependency diagram with each category and local hypothesis; the first concrete task is to collate the Laurent/power-series glyph.',
 ['BerthelotMessing1979','deJong1998','Lau2013'])
prob(13,'Exponential construction and crystalline universal extensions',
 [K+', scan46, lines378–398',P+', scans47–48, lines10–42; C-SA04-1,6,11–15'],
 'Construct transitive canonical identifications between universal extensions of different lifts; explain the exponential lifting of vector subgroups, the abelian quotient and the comparison with the cohomological BT construction.',
 'Use locally nilpotent divided powers for the deformation equivalence and the precise universal-extension/sheaf sites. The vector extension and its Lie crystal must remain distinct objects.',
 'de Jong1995 introduction pp5–6 attributes the exponential construction to Messing and its comparison with degree-one abelian cohomology to Mazur–Messing. Illusie Pisa §5 describes the universal-extension mechanism and its historical letters. The exact R¹crys Gm notation requires site/convention collation.',
 'These pages explicitly defer the two constructions and mark the abelian-to-BT passage heuristic; the later sources document how they were developed.',
 'Worth a faithful comparison of the two constructions and the A/A-dual conventions, rather than claiming the short quotient paragraph is already a proof.',
 ['deJong1995','IllusiePisa2013','GrothICM1970'])
prob(14,'The deformation theorem and its nilpotence qualifications',
 [K+', scans42–43, lines249–267',P+', scans47–48, lines10–34; C-SA04-6'],
 'Lift BT groups by lifting their Hodge direct summands; the inserted qualification allows nilpotent divided powers or a connected group/connected dual.',
 'Retain one of those qualifications and marked deformation data; do not replace the categorical theorem by uniqueness of an unmarked lift.',
 'GrothICM1970 §4 pp433–434 states the qualified theorem and Remark1 gives failure without the hypotheses even for an ordinary split height-two group. de Jong1995 Proposition3.2.1 invokes MessingV1.6 in the nilpotent-PD form; Katz1.2.1 supplies Serre–Tate.',
 'The correction is visibly inserted on the page, and the published warning supplies the mathematical reason. The audit does not manufacture a new counterexample without reproducing its full crystalline logarithm calculation.',
 'Settled but essential editorial work: preserve the inserted hypotheses in every later use.',
 ['GrothICM1970','deJong1995','Katz1981'])
prob(15,'The unresolved Pisa cross-reference',
 [P+', scan49, line73; C-SA04-20; SA04-29'],
 'The isogeny invariance proposition is said to imply VII10.8.2 of the Pisa notes.',
 'First identify the referenced version and exact proposition before reconstructing the logical implication.',
 'The CSG published-work list and Illusie’s Pisa historical account were opened; title/locator searches did not identify VII10.8.2. It is not replaced by a different theorem with a similar subject.',
 'This is a source-identification gap; no mathematical open theorem can yet be extracted from the bare reference.',
 'Worth one archival bibliography task, because a correct match could connect the isogeny warning to a precise earlier statement.',
 ['GrothPublishedWorks','IllusiePisa2013'])
prob(16,'Fibration multiplicativity and local-system finiteness',
 [P+', scans60,62,66, lines363–411;452–465;602–610; C-SA04-57–59'],
 'Prove the local-system Euler lemma needed by the fibration spectral sequence; later ask whether the relative-polyhedral restriction can be omitted within E_infinity.',
 'Finite CW homotopy type of the base is sufficient for ordinary Euler multiplicativity with finite-total-cohomology fibre. A compact-support theorem needs its own support/direct-image hypotheses. Constant-coefficient finiteness alone is insufficient.',
 'Morin1962 Lemma1 gives the finite-cell local-system complex. West1977 Corollary5.3 supplies finite homotopy type for the compact ANRs arising under the specified cone interpretation. The telescope counterexample fully refutes only the broad provisional ordinary version.',
 'The text explicitly identifies the local-system gap and later narrows the base; that is a mathematical correction in the manuscript itself.',
 'Worth reconstructing the final conical-case argument with all support comparisons; one run can complete the finite-type ordinary case and expose the remaining compact-support inputs.',
 ['Morin1962','West1977','Hatcher2002'])
prob(17,'The finite-cover alternative to cellular finiteness',
 [P+', scan62, lines448–465; C-SA04-60'],
 'Use arbitrarily fine finite covers with finite intersections to prove the local-system Euler lemma and its homological ordinary analogue.',
 'Require a finite excisive cover or an acyclic resolution computing the chosen cohomology and refine it to trivialize the local system; finite intersection cohomology alone must be connected to that resolution.',
 'Verdier1973 provides the support setting and Morin1962 the established finite-cell sufficient condition. The precise ambiguous cover-label formulation was not located as a named theorem in the searched primary sources.',
 'The page states a route without writing the cover spectral sequence or the required comparison hypotheses.',
 'Worth a short technical lemma once the cover convention is fixed; start with open good covers and then test the manuscript’s closed-cover reading.',
 ['Verdier1973','Morin1962'])
prob(18,'Triangulation of recursive conical spaces',
 [P+', scan62, lines471–500; C-SA04-62–64'],
 'List low-dimensional conical models, cancel a compact dimension-three triangulation clause, and doubt compact triangulation in dimension four.',
 'Separate finite CW homotopy type from homeomorphic triangulation and manifold links from arbitrary singular links. Compact metric conical spaces have finite homotopy type under the recursive interpretation; compact4-manifolds need not be triangulable.',
 'West Corollary5.3 proves the homotopy-finiteness input. Manolescu2015 §2.2 records Moise’s3-manifold theorem and the E8 four-dimensional obstruction. The exact broad singular-link low-dimensional triangulation claim remains a source/proof gap in this audit.',
 'Pro records the deletion; Codex fails to mark it, so scans must settle the editorial discrepancy. No motive for the deletion is assigned.',
 'Worth checking the definitions and deletion first; further work should target a precise singular-link theorem rather than invoke Moise indiscriminately.',
 ['West1977','Manolescu2015'])
prob(19,'The compact conical core',
 [P+', scan64, lines527–533; C-SA04-66,67'],
 'Verify that cutting away an open half-cone leaves a compact conical member and that the punctured space retracts onto it.',
 'With compact recursive links stable under joins, the boundary charts and explicit radial homotopy prove the two claims.',
 'The local cone-product argument and radial formula are independently supplied in proof_checks.md; West applies only after the compact-metric ANR hypotheses are checked. No scan decision is implied about C/E notation.',
 'The source says vérifier for the boundary-class assertion and omits the deformation homotopy.',
 'Worth retaining as a short companion proof, because the end-defect and uniqueness claims depend on it.',
 ['West1977','Hatcher2002'])
prob(20,'Axiomatic uniqueness on E_infinity',
 [P+', scan66, line627; C-SA04-70'],
 'Ask whether the first five axioms determine the Euler functions on every object of E_infinity; the separate main statement asserts existence.',
 'Affirmative under the compact-metric recursive-cone interpretation: compactification and core have finite CW homotopy models, and subtraction at the compactification point determines compact supports.',
 'West Corollary5.3 plus Morin’s finite-cell calculation gives the conditional modern completion written in proof_checks.md. A wider category without those hypotheses is not claimed settled.',
 'The author explicitly says he does not know uniqueness; the manuscript supplies no finite-homotopy-type theorem.',
 'High interest and high feasibility: write the exact definition and dependency proof; this can become a clean self-contained companion result.',
 ['West1977','Morin1962','Hatcher2002'])
prob(21,'First Postnikov class of a loop space',
 [P+', scan83, lines1607–1626; C-SA04-80–84'],
 'For X=Omega Y, question a zero after k1∈H³(pi1,pi2) and draw possible successive cohomology-suspension lifts.',
 'The ambient group need not vanish, and one loop does not force the class to vanish. Two compatible loopings force the first class to vanish, but do not give a natural splitting in the original space.',
 'Arlettaz2000 Theorem7.6/Corollary7.7 prove double-loop vanishing/splitting; the1990 article’s publisher record dates receipt9June1987 and revision15April1988, publicationJanuary1990. Baues–Conduché1995 Theorem1.9 forbids a natural splitting; §§4–5 realize the independently checked single-loop counterexample.',
 'The leaf is a scratch diagram with no proof. The supplied text does not determine which vanishing was intended, so this remains an ink/grammar question even though the alternatives have different mathematical answers.',
 'Worth a short annotated diagram explaining the three distinct assertions and the extra delooping hypothesis.',
 ['Arlettaz2000','Arlettaz1990','BauesConduche1995'])
prob(22,'Denominators of the analytic differential invariant',
 [P+', scan72, lines747–754; C-SA04-121'],
 'Show that a rational differential expression regular on all étale coordinate pairs has denominator only a monomial in first derivatives.',
 'For a universal finite-jet rational function over a coefficient domain, poles restricted to a1b1=0 force the reduced denominator to divide a power of a1b1. One must justify the passage from variable analytic coefficients to that universal jet statement.',
 'The localized-polynomial-ring argument is independently given in proof_checks.md. DeligneI§5 supplies the actual third-order cocycle, but not this classification of all admissible expressions. Searches found no exact additional theorem matching the printed coefficient convention.',
 'The source explicitly says this ought to be shown; the normalization of the jet-function category is left implicit.',
 'Worth a small algebraic lemma plus a jet-realization lemma; this is the first concrete step toward the larger classification.',
 ['Deligne1970','BouarroudjOvsienko1998'])
prob(23,'Analytic uniqueness and redundancy of local surjectivity',
 [P+', scans72–73, lines774–777;802–831; C-SA04-121'],
 'Every admissible cocycle should be a nowhere-zero scalar multiple of G; étale naturality should make the scalar universal, and rigidity axiom d should imply local surjectivity e.',
 'Fix finite jet order, rationality, analytic sheaf naturality and projective invariance, then prove a precise relative jet-group cocycle classification. Scalar constancy is a final step after classification, not its substitute.',
 'Bouarroudj–Ovsienko1998 §1.2 gives the smooth Diff+(S1), PSL2-relative uniqueness. Ovsienko1993 recalls continuous real-line cohomology. Deligne proves the particular analytic torsor. None by itself proves all the manuscript’s local-complex operator quantifiers; the2025 MO thread was a search lead only.',
 'The page asserts the classification while marking the redundant-axiom step as something to verify; no historical explanation is documented.',
 'High mathematical interest, medium feasibility: a few hours can fix the category and classify low jet orders, but should not promise the unrestricted theorem.',
 ['BouarroudjOvsienko1998','Ovsienko1993','Deligne1970'])
prob(24,'Integral universal uniqueness of G0',
 [P+', scan73, lines888–897; C-SA04-123'],
 'The integral Hasse operator should have coefficients in Z and be unique up to sign under the universal conditions.',
 'Separate the proved integral cocycle identity from a universal recipient/classification statement; specify base change, locality, finite jet order, target module and surjectivity/generation. Only then do units of Z give the sign ambiguity.',
 'The integral construction and characteristic2/3 tests are certified in a_computations.py. Deligne’s theta=S/6 explains characteristic-zero normalization. Classical relative smooth cohomology supplies an analogue, while no exact all-base theorem matching the printed quantifiers was located. Companion claimsC201–203 treat distinct coherent-target/fixed-p formulations.',
 'The source offers a formula and examples, but no classification argument. Later nearby question marks and counterexamples concern different quantifier choices and must not be collapsed into this statement.',
 'Highest-interest algebraic direction: formulate the universal jet-group problem and compute its low-order module over Z before making an all-base uniqueness claim.',
 ['Deligne1970','BouarroudjOvsienko1998'])

readings=[]
def rd(scan,line,reading,alternative,evidence,weight='high',confidence='high'):
    readings.append(dict(cote='93',scan=str(scan),line=line,reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
rd(38,'Codex K93-12:206','VF=p id_M; FV=p id_M^(p)','Exchange identity subscripts or exchange arrow labels','Displayed F:M^(p)→M and V:M→M^(p) fix domains; C-SA04-2. No ink decision.')
rd(38,'Codex K93-12:210','BT(S0)→FV-Cris','BT(S0)^op→FV-Cris','The surrounding functor is explicitly contravariant; line186 has the opposite-category superscript.')
rd(38,'Codex K93-12:194','BT(S0)^op→Crisloclib(S)_0','A restriction/target notation or BT(S)^op may be intended','The preceding crystal-site equivalence alone does not identify arbitrary BT(S) with BT(S0); later deformation theory retains Hodge data.','medium','medium')
rd(41,'Codex K93-12:232–235','t_G=omega_(G*)^vee; quotient t_(G*)','Use t_G=omega_G^vee for Lie(G), or adjust quotient/star convention','With the given definition the quotient has the wrong Lie-group label relative to the standard Hodge sequence; C-SA04-5.','high','medium')
rd(45,'Codex K93-12:349','R¹ f_*(O_S)','R¹ f_*(O_A)','f has source A; ordinary Hodge sequence has H¹(A,O_A), not a sheaf with the base subscript.','high','high')
rd(47,'Pro:6–8','E(A*) in display, E(A) in next sentence','Make the dual convention consistent','The Lie extension used by D*(A) is that of A dual; both witnesses preserve the switch. SA04-8.')
rd(47,'Pro:16','D_*(A)≃D*(A*)^vee (uncertain inserted vee)','Possibly omit vee, or change preceding definition','Applying D*(A)=LieE(A*) to A* gives LieE(A), already D_*(A). No canonical self-duality without polarization. SA04-11.','high','medium')
rd(49,'Pro:54–58','Ker F_M=Im V_M on M_o|0','Read on the mod-p realization, with Frobenius twist','F is injective on the p-torsion-free Witt module; nontrivial Hodge kernel appears after reduction. SA04-24.')
rd(49,'Pro:66–70','annulé par une puissance de J; quasi-compact deleted','Possibly power of p; inspect deletion scope','Published GrothICM§5p434 requires one p-power killing ideal; global-Hom localization needs uniform denominators. SA04-28.')
rd(50,'Pro:87','gamma(1−gamma)^k in finite sum','gamma(1−gamma)^(k−1)','u_k=1 makes the finite expression tend to1−gamma, while the proposed infinite sum is1; exact programC35.')
rd(50,'Pro:89','limJ=c_k a_q','limJ=2pi c_k a_q, or normalize integral by1/(2pi)','Direct Fourier integration; scalar f=z^q and weight1 already distinguish. SA04-37.')
rd(50,'Pro:91–93','little-o as r→infinity without stated angular uniformity; z|x','Uniform little-o, or prior uniform big-O plus pointwise little-o; same x throughout','Dominated Fourier extraction needs control in theta; quasinilpotent inverse series coefficients are x^j. SA04-38,39.','high','medium')
rd(50,'Pro:95','a_n,b_n=o|O(n^alpha)','Little-o is consistent with strict degree bound','(z−1)^−2,alpha1 satisfies big-O but has pole degree2, contradicting degree<2. ProgramC39.')
rd(50,'Pro:95','outside-disk bound with positive cos(theta)','Minus cos(theta) or absolute value','w=−2 gives positive5/2≤−9/2; exact Cayley calculationC40.')
rd(52,'Pro:126–129','|lambda−lambda0| normR(lambda)<1','Use normR(lambda0)','R(lambda)=1/lambda,lambda0=1,lambda3 satisfies2/3<1 but Neumann terms(−2)^n. ProgramC42.')
rd(52,'Pro:139','norm(yw−u)<epsilon','norm(yw−w)<epsilon','u1,w2,C2,gamma0,epsilon1/2 satisfies all hypotheses for everyeta but error1. Corrected Neumann estimate in proof_checks. C47.')
rd(53,'Pro:173–178','unlabelled Hodge slope list; W|V tensor symbol','Collate covariance/weight ordering and tensor factor','Two-step Hodge dimensions alone do not imply weak admissibility; the inverse-period functor changes with dual convention. No preferred symbol supplied.','high','medium')
rd(54,'Pro:192','k[(t)]|k[[t]]','Power-series ring k[[t]] if local extension problem is intended','The argument asks extension across the closed point; k((t)) is already the generic field. SA04-72.','high','medium')
rd(58,'Pro:304','compactness comparison by b)','Possibly a)','Axiom a is the compactness comparison; b is closed/open additivity. SA04-135.','low','high')
rd(58,'Pro:310–313','chi(R^n)=...=(−1)^n','chi_!(R^n)','Odd n contradicts ordinary contractibility and the preceding correct table. ProgramC54.')
rd(60,'Pro:376–398','ordinary chi/H symbols inside compact-support spectral calculation','Restore support exclamation marks where that calculation requires them','Source distinguishes chi andchi_!; local-system compact-support formula and ordinary formula have different hypotheses. SA04-91.','high','medium')
rd(62,'Pro:448–465','ambiguous cover-condition letter; homology/cohomology subscripts','Inspect cover label and H_p versus H^p with dual local system','Inserted homology indexing avoids an unjustified ordinary-cohomology dualization; exact meaning depends on the cover convention. SA04-94,95.','high','medium')
rd(62,'Pro:471–493','C_(n−1)|E_(n−1); margin espaces discrets','Compact-link class and finite discrete base, if recursive finiteness is intended','Infinite discrete spaces have infinite H0; compactness and local cone charts are needed for ANR finiteness. No definition silently rewritten. SA04-98.','high','medium')
rd(62,'Pro:489; Codex K93-08:68','Pro deletes compact dimension-three triangulation, Codex retains it','Inspect whether clause is actually struck','Witness disagreement changes authorial status; the mathematical distinction between finite homotopy type and triangulation does not decide the ink. SA04-100.')
rd(66,'Pro:580','chi_!(Y|X−Y), first alternative yielding Y−Y','chi_!(X−Y)','Original scan56 formula, and X=R,Y=empty, reject Y−Y. Codex has X−Y. SA04-108.')
rd(66,'Pro:582','X′,X″ closed in X, cover omitted','Add X=X′∪X″ if an omission is confirmed','X=S1,bothpiecespoint violates the literal formula; scan56 includes de réunion X. SA04-109.')
rd(66,'Pro:586–588','two different equivalence symbols for ordinary/support invariance','Ordinary homotopy versus proper homotopy or a stronger equivalence','R≃point yet chi_c differs; source does not define the second relation here. SA04-110.','high','medium')
rd(72,'Pro:788; scan73 Pro:852','c(f)−c(g) versus c(g)−c(f)','Consistent torsor-action sign convention','Either convention works after reversing the action, but mixed conventions reverse G. SA04-143.')
rd(73,'Pro:913–915','G0(t,t²)=dt²/(2t)','dt²/(4t²)','Hassejets(2t,1,0) give1/(4t²) wherever2t is invertible; programC122. SA04-158.')
rd(83,'Pro:1610','k1∈H³(pi1,pi2) ?=0','Question may concern k1, or the ambient group','The group reading fails even for an infinite loop space; class reading needs two loops, while the source only writes one. Neither mathematical fact resolves the punctuation. SA04-122.','high','low')

links=[]
def link(kind,src,dst,what,evidence,notes):links.append(dict(kind=kind,**{'from':src,'to':dst},what=what,evidence=evidence,note_ids=notes))
link('folder','93 scan38–46 (CodexK93-12:181–400)','93 scans47–48 (Pro:4–46)','Same crystalline/abelian programme continues through the universal extension, its Lie crystal and BT comparison.','Both source sequences read line by line; sentence at K93-12:400 continues intoPro47. No manuscript date inferred.','MPL_93_047-091#7–21')
link('folder','93 scan49 (Pro:73–75)','93 scan53 (Pro:161–178)','The later Tate supplement explicitly directs association with the mysterious filtered-crystal functor.','Scan53 marginal instruction and forward/inverse questions read; scan49 names the essential image and Pisa result.','MPL_93_047-091#29–33,#61,#65–67')
link('folder','93 scan52 (Pro:139–141)','93 scan50 (Pro:87)','Cancelled Cohen-factorization exercise continues across reverse scan order.','Endpoint and approximant induction read in both passages; no authorship of reused exercise sheets assumed.','MPL_93_047-091#34,#35,#57–59')
link('folder','93 scan60 (Pro:363–411)','93 scans62,66 (Pro:448–465;602–610)','Provisional fibration argument acquires local-system and relative-polyhedral qualifications.','Both conditional proofs and later restriction checked; ordinary telescope counterexample applies to the broad version.','MPL_93_047-091#90–97,#112')
link('folder','93 scan62 (Pro:471–503)','93 scans64,66 (Pro:527–546;618–627)','Recursive cone class, compact core, end-defect and final uniqueness question form one dependency chain.','Definitions and flagged core step read at both ends; modern ANR completion marked reconstruction.','MPL_93_047-091#98–114')
link('folder','93 scan72 (Pro:716–831)','93 scan73 (Pro:834–928)','Analytic projective cocycle and torsor lead to Hasse coefficients and integral normalization.','Both formulas and opposite difference conventions checked; the factor12 identity is separately certified.','MPL_93_047-091#136–160')
link('folder','93 scan73 (Pro:888–928)','93 scan74 (Pro:949–982)','Integral universal claim is followed by coherent-target pushout and fixed-characteristic qualifications.','Opening scan74 source read in overlap; agent b suppliesC201–203. These are different quantifiers, not one merged theorem.','MPL_93_047-091#152–160; companionentries#161ff')
link('published work','93 scans38–43;47–48','GrothICM1970 §3–4, pp432–434','Dieudonné construction, Hodge filtration, qualified deformation theorem and Serre–Tate comparison.','Six-page published text downloaded/OCRread; hypotheses compared, including nilpotentPD or infinitesimal group/dual.','MPL_93_047-091#7–21')
link('published work','93 scan49 (Pro:60–75)','GrothICM1970 §5 p434','Global isogeny localization and nilpotent invariance.','Published theorem uses an ideal killed by one p-power; this supplies a hypothesis comparison, not an ink correction.','MPL_93_047-091#26–33')
link('published work','93 scans49,51 (Pro:75;100–112)','GrothICM1970 §5 p435','Essential-image, Zariski openness, forward/inverse period functor and broader filtered programme.','Both primary formulations read; published text does not turn analytic openness into the requested Zariski theorem.','MPL_93_047-091#31–33,#44–50')
link('published work','93 scans53–54 (Pro:165–192)','Groth1966 §1 p63, TheoremB and following conjectural sentence','Tate char0 genericfullfaithfulness and suggestion that the characteristic restriction is superfluous.','Primary GDZ scanOCRread; text explicitly creditsTate and singles out charp. Root owns separate c100 use of this article.','MPL_93_047-091#62–75')
link('published work','93 scan54 (Pro:184–192)','SGA7I ExposéIX Remark5.11, printedp386; Berthelot–Messing1979 §1','Equal-characteristic generic extension and a crystalline/perfect-closure route.','Primary Berthelot–Messing §1 and de Jong1998/ICM1998 explicitly state the SGA7 question. The original SLMath/MSRI SGA7I scan was subsequently opened: IX5.11 explicitly says removal of the characteristic restriction in5.8–5.10 depends on unrestricted Tate full faithfulness. Exact original proof passages5.8–5.11 were read at printedpp382–386. The AI-edited page was only a discovery aid; the introduction was not independently collated.','MPL_93_047-091#68–75')
link('published work','93 scans72–73 (Pro:716–855)','Deligne1970 I§5 pp29–36, especially5.8–5.12','Same projective2-jets, quadratic torsor, Schwarzian cocycle and second-order differential equation.','Exact theta=S/6 versus sourceG=−2S normalization compared; integral universality not attributed toDeligne.','MPL_93_047-091#136–150')

# Project context is a separate kind/table. Its external packets are not supplied
# in this audit, so both-end verification cannot be claimed for them.
link('our projects','MPL_93_047-091#33,#47; noteslines361,445','R: MPL_15_195-228+18_002-017 P03 (18/005); context/hua_project/93.modern.tex IV','Earlier-run context compares admissible filtrations and a relative period functor.','The current note’s assertion and c93 passage were checked. External cote18/project packet absent and outside scope; destination remains an explicitly unverified lead, not an established folder link.','MPL_93_047-091#33,#47')
link('our projects','MPL_93_047-091#76,#117; noteslines619,629,875','RESULTS_STATE MPL_93_002-046 O01 andE26; README S20','Earlier notes place Euler, orientation and Galois themes beside a proposed Gauss–Manin/Cartier unity.','Currentc93 leaves55–68 checked; root owns earlierc93 originals. S20 is identified by the note itself as a planning hypothesis, not a matching result. ExternalRESULTS_STATE not present.','MPL_93_047-091#76,#117')
link('our projects','MPL_93_047-091#116; notesline869','RESULTS_STATE FINMON C2-CP2','Finite face-poset model is a thematic lead toward finite-category models.','The finite-poset implication is checked under finite-homotopy-type hypotheses. FINMON destination is absent, and no arrow-minimization claim is proved.','MPL_93_047-091#116')

def write_tsv(name,fields,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

# Publication parallel read after the first source register was serialized.
link('published work','93 scans38–48 (CodexK93-12:181–400;Pro:4–42)','GrothMontreal1974 ChapterV §§1–5, printedpp107–120','Exact published programme parallel: Problems1–3, Hodge admissibility, abelian deformation, universal extension and BT comparison.','Primary scan OCR collated. Printed111 retains qualifications;116 states arbitrary-base abelian theorem;117 char0rigidity;118 lacks the doubtful extra vee;119–120 matches the Pro continuation. Course1970/publication1974 does not date these leaves.','MPL_93_047-091#7–21,#24–25')
for _r in readings:
    if _r['scan']=='47' and _r['line']=='Pro:16':_r['evidence']+=' Published Montréalp118 has no extra vee; this is an additional textual witness, still not an ink decision.'
    if _r['scan']=='38' and _r['line']=='Codex K93-12:206':_r['evidence']+=' Montréalp108 prints correctly typed identity subscripts.'
    if _r['scan']=='38' and _r['line']=='Codex K93-12:210':_r['evidence']+=' Montréalp108 retains the opposite-category superscript.'
problems[12]['state_of_art']+=' Exact own-published parallel now collated: GrothMontreal1974 V§4 pp116–118, including char0 unique marked smooth-group lifting of E(A); the full nil-thickening proof is carried from that published assertion, not independently reproduced here.'
problems[12]['refs']+=['GrothMontreal1974','FonsecaMatthes2022']

if __name__=='__main__':
    (OUT/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
    write_tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
    write_tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
    print(json.dumps({'problems':len(problems),'readings':len(readings),'links':len(links)}))
