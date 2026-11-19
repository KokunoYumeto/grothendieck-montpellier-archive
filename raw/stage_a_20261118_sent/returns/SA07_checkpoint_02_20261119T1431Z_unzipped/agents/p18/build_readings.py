"""Manually selected mathematical reading alarms; no source is emended."""
from pathlib import Path
import csv
P=Path(__file__).parent
F='SA07_texts/pro/MPL_18_018-062_transcription.tex'
rows=[]
def R(scan,line,reading,alternative,evidence,weight='high',confidence='Mathematical alarm high; ink undecided without scans'):
 rows.append(dict(cote='18',scan=str(scan),line=F+':'+line,reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
R(19,'23;31','E_sigma^(2i|2p), and later E_sigma^i=H^(2i|i)',
 'Check all degree labels against codimensionp and total degree2p; do not propagate one uncertain label to every occurrence.',
 'The cycle map atL16 andL25 has codimensionp and lands inH2p. SA07-401–402; CL-SA07-402–403.')
R(19,'31','The lattice factor has exponent1, and conjugation changes the class by a single minus sign.',
 'Either the sentence is still restricted to the precedingp=1 example, or generalp requires exponentp and sign(−1)^p.',
 'Direct conjugation of(2πi)^−p gives(−1)^p. C01 and computations.md §1. Scope is as plausible as a transcription slip; neither is decided.')
R(21,'58','The supports-to-global arrow is labelled unsure{?}.',
 'Confirm whether the mark is an authorial question mark and whether it attaches only to this arrow.',
 'The following coefficient square is asserted to explain commutativity. A doubtful mark on one arrow cannot be expanded into a conjecture about every comparison. SA07-403.',
 'high','Ink uncertainty high; mathematical issue localized to arrow and shifts')
R(21,'58–65','The displayed supports/purity objects carry no visible[−2p] shift; the first lower scalar is1/(2πi).',
 'Check for suppressed degrees or a specializationp=1; the general regular-codimensionp version needs a2p shift and(2πi)^−p.',
 'The second square explicitly has exponentp atL65; CL-SA07-404 and computations.md §1 give the typed modern reconstruction.')
R(21,'69','transforme pas; a factor(2πi)^p en|en+ is needed for integral classes.',
 'Confirm the negative and the direction of the factor relative to the chosen analytic pushforward.',
 'With top=(2πi)^−p analytic, one must distinguish rescaling the map from rescaling its output. C01 and ST03Thm4.1 show why conventions matter.',
 'critical','Mathematical normalization must be fixed; the verb and factor direction remain ink questions')
R(21,'72–73','Cycles of codimensioni with a comparison factor indexedp.',
 'Check whetheri andp are intended to coincide, or one is a mistaken index.',
 'The displayed target isH2i and codimension controls both the degree and the period power. SA07-401; CL-SA07-402.')
R(22,'83','phi2*=psi1*∘phi1* andphi1*=psi2*∘phi2*.',
 'The declared domains suggest phi2*=phi1*∘psi1* and the analogous reversed composition, or different chart-map directions.',
 'phi_i*:P(M_i)→A whilepsi1*:P(M2)→P(M1); the literal composite is not typed. C14; CL-SA07-409. No formula is changed.')
R(23,'100–104','Relative codimensionp and uncertain target degree2i+2p.',
 'Confirmp=dimY−dimX and the+2p shift in both rows.',
 'For a proper map the Gysin degree isq+2dimY−2dimX. C01; CL-SA07-405. Reversing the relative-dimension convention reverses the period power.')
R(25,'133–135','z∈A^n(X^n×Y^m) acts in the same degree, and the inserted pushforward is an|top.',
 'Ifn=dimX, degree preservation is correct; the insertion usingP_top requires the compatible topological pushforward or an explicit scalar conversion.',
 'General action degree isq+2r−2dimX. C01 gives factor(2πi)^(dimX−r). SA07-405; CL-SA07-406.')
R(25,'140–143','Several indicesi|p and twistsinfty|0 are overwritten.',
 'Check each realization/twist independently; do not identify an infinity realization label with a Tate twist without the ink.',
 'The displayed comparison should have matching degree and coefficient realization. These labels determine which scalar cancellation is being claimed.',
 'high','Source marks multiple overwritten symbols; no preferred ink reading assigned')
R(25,'150','pr1^a|*',
 'A pullback star is the type-correct operator here.',
 'The correspondence formula first pulls a class fromX toX×Y. CL-SA07-406 and C01.')
R(25,'151','Exponent−n|−m on the pushforward-conversion factor.',
 'Forpr2:X×Y→Y it should encode−dimX, hence−n ifX has dimensionn; inspect the ink rather than choose by expectation.',
 'The cycle factor is(2πi)^−r and pushforward factor(2πi)^dimX. Cancellation is onlyr=dimX. C01; SA07-405.')
R(25,'156','The target onY isH^p(Y,Omega_X^bullet).',
 'Omega_Y^bullet is the type-correct de Rham complex onY, unless an omitted pullback is intended.',
 'The arrow is a correspondence operator into de Rham cohomology ofY. No such pullback is written. SA07-405.')
R(25,'156','The lower arrow is equated to(1/(2πi))^(n|m) timesxi_C(z).',
 'Check whether this label concerns the raw cycle-class map or the complete correspondence operator; the latter has no remaining factor whenr=dimX.',
 'The immediately precedingL149–151 cancels the cycle and trace factors. C01; CL-SA07-406.',
 'critical','Mathematical discrepancy high; attachment of the label requires scans')
R(28,'220','The alleged zero sum is writteny1+yq=0.',
 'The minimal positive relation argument needsy1+⋯+yq=0.',
 'The next negative-pairing argument and the publishedBourbaki ChVI§1no7Prop22 require every summand. computations.md §12; CL-SA07-447.')
R(28,'220','The index chosen for negative pairing may include1.',
 'The index must satisfy2≤j≤q.',
 'Summing(y1,yj) overj≥2 gives−||y1||²<0, whereas(y1,y1)>0. CL-SA07-447.')
R(28,'222','The last sum excludes a doubtful1|i but does not clearly exclude both replaced terms.',
 'After replacingy1 andyj byy1+yj, sum the remaining terms overi≠1,j.',
 'Otherwise the shortened relation double-counts a root. Exact publishedProp22 collated; no emendation. CL-SA07-447.')
R(29,'237','tous les éléments primitifs|possibles',
 'Confirm the noun and recover its ambient set; neither every nonzero vector nor primitivity in an unspecified lattice is a valid silent expansion.',
 'The coefficient in a fixed algebraic basis is an automorphic image of(2πi)^−1 and stays transcendental. SA07-407; CL-SA07-480; computations.md §1.',
 'critical','Ink unresolved; the mathematical restriction is certain')
R(29,'239','sousZ|Q-réseau',
 'ConfirmZ versusQ and any omitted tensor extension.',
 'An integral lattice and a rational subspace have different stabilizers and laterG(Z) ambiguity. SA07-408; CL-SA07-408.')
R(33,'292','The parenthesis sayssigma|tau respects the filtration.',
 'Tau, the de Rham descent conjugation, respects the filtration; sigma is explicitly said not to respect it.',
 'The preceding definitions andtau=fσ make the roles distinct. SA07-410; CL-SA07-411. This is a role-based alarm only.')
R(34,'319','f_R is d’ordre2, followed by claims about its image inG/G0.',
 'Check whether order dividing2 is intended at the level of an individual motive, and whether the group is the entire category or the one generated byM.',
 'The same text later studiesf∞=1 on some motives. The universal-real-category involution and its image on a subcategory need not have the same exact order. SA07-411; CL-SA07-416.',
 'high','Mathematical scope alarm; no assumption of an ink error')
R(35,'347–352','H^(*|0)(X(R),Q)=V∩W=V^f.',
 'Confirm the superscript and whetherX(R) denotes the real fixed locus or an intended quotient space. The usual real fixed-locus interpretation is false in general even after choosingH0.',
 'P1_R hasH1(RP1,Q)=Q butH1(CP1,Q)^f=0; SpecC/R has no real points but invariant BettiH0=Q. L522 explicitly uses the quotient. SA07-414; CL-SA07-469.',
 'critical','Counterexamples certain; intended notation requires scans')
R(35,'352','W^F|f',
 'The same rational involutionf should act on bothV andW, unless a distinctF was defined on missing material.',
 'W=V+⊕iV− is stable underf. C02; SA07-412.')
R(35,'357','isom comme foncteurop⊕-isant|⊗-isant',
 'The following explicit map is additive and fails tensor compatibility on the negative-negative summand.',
 'Its tensor defect isi²=−1. The last sentence explicitly says n’est pas compatible avec le produit tensoriel. C02; CL-SA07-412.')
R(35,'359','ne sont unsure{pas tensor-isom}',
 'Confirm the negative and the tentative Il semble; do not replace it by the affirmative tensor-isomorphism claim.',
 'The Artin sign object gives a rational-square obstruction while the Tate-only category behaves differently. CL-SA07-413; computations.md §2.',
 'critical','The supplied reading already favors the negative; no scan is available here')
R(36,'383–393','j2|j1, even-Tate classification, and central|Q tordu|comm. margin.',
 'Check the indices and words separately; retain the live even-Tate assertion apart from the deleted opening and the uncertain centrality box.',
 'A⊗Q(−1) is a counterexample to the unrestricted live classification, but does not settle the undefined marginalQ tordu. SA07-416–418; CL-SA07-418–419,473.',
 'critical','Mathematical counterexample certain; marginal reading unresolved')
R(37,'406','Rep(C|G)',
 'Rep(G) is the Tannakian representation category used in the surrounding paragraph.',
 'G=Aut⊗(T_B) is defined atL399. The letter affects the object on whichsigma_M is defined. SA07-410; CL-SA07-420.',
 'medium')
R(37,'411','structure mixte|réelle onM⊗_R C',
 'The argument reconstructs a real form fromtau=fσ; it does not construct a mixed Hodge structure.',
 'No weight filtration is introduced. SA07-410,415; CL-SA07-420.',
 'high')
R(38,'433–437','R(gamma|sigma)=R(beta,gamma)=R(beta,alpha)',
 'Confirm the variable and recover the relation expressinggamma fromalpha and the real pointbeta.',
 'The equality is elementary only whenbeta isR-rational and the torsor-composition relation is specified. CL-SA07-472; computations.md §2.',
 'medium','Algebraic implication conditional; variable reading unresolved')
R(38,'445–465','Whole normalizer/maximal-compact argument is inside deleted{…}.',
 'Confirm the deletion extent; do not read its assertions as live conclusions.',
 'SA07-419; CL-SA07-471. The live normalizer identity atL421 is a separate claim.',
 'critical','Deletion is explicit in supplied source; scans needed only to revise it')
R(39,'484','hom injectif|isom injectif R→C and deleted independence from topology.',
 'The unique continuous embedding ofR is intended; verify the deletion of topology independence and the distinction from choosingu for a fixed topology.',
 'The period lattice onP1 varies with abstract complex topology. CL-SA07-410 and C01. An isomorphismR≃C is impossible.',
 'high')
R(40,'531','H^(p,q)(X)⊂F^pH^q(X)',
 'The total cohomological degree should bep+q, with H^q(X,Omega^p) as the source.',
 'The Hodge-to-de Rham degree is the sum of sheaf degreeq and form degreep. CL-SA07-470; D71§2.2.')
R(41,'546','H_T^(p,q)(X)⊂F^p(H^q(X))',
 'Again checkH^(p+q) rather thanH^q.',
 'Same total-degree calculation asL531; the recurrence does not resolve the ink. CL-SA07-470.')
R(43,'589','complet discrètem. and residue-field characteristicp inserted.',
 'Confirm discreteness and whether characteristic zero of the valued field is implicit or explicit.',
 'These distinctions separate mixed-characteristic period-ring comparison from equal-characteristic crystalline theory. SA07-423; CL-SA07-422.',
 'high','Programme hypotheses depend on uncertain insertion')
R(44,'605','barK→barK*|barK_*',
 'Confirm the upper star versus lower direct-image notation and recover the missing definitions.',
 'The nearby argument alternates pullback and direct image; the actual source/target cannot be identified from this leaf alone. CL-SA07-467.',
 'high','No mathematically unique alternative without the antecedents')
R(45,'618','Elliptic curves non [barC,C′] [circle] isog.',
 'Check the exact nonisogeny condition as well as non-CM.',
 'dimG=7 and the productSL2×SL2 conclusion require two nonisogenous non-CM factors in the reconstructed setting. MZ99Cor3.9; CL-SA07-423.',
 'critical')
R(45,'628','trdegK overk(pi)≤5|4;K undefined locally.',
 'Confirm the digit and recover the fieldK before drawing any period-field conclusion.',
 'The displayedBorel dimension5 does not identifyK, and subtracting a transcendence degree requirespi to be transcendental over the correct base. CL-SA07-425.',
 'critical','Both ink and mathematical object are unresolved')
R(45,'632–649','DeletedCech construction with unsure derived functors and presheaf labels.',
 'Confirm the deletion boundaries and all check/hat notation; do not restore a general theorem from the wordEvident.',
 'The source lacks a precise map, site and conventions. CL-SA07-468; SA07-482.',
 'high','No mathematically forced reconstruction')
R(47,'680;684–690','Tensor-isomorphism labels are partly suppressed; Qhat=∏Ql is a full product.',
 'Confirm whetherIsom meansIsom⊗. Preserve the explicitly written full product until another convention is demonstrated.',
 'The torsor and quotient dimension require tensor isomorphisms under the indicatedG. A full product and restricted adele ring have different topologies. CL-SA07-426; SA07-430–431.',
 'critical','Type/topology alarms, not permission to insert a restricted-product prime')
R(49,'739–740','MarginalG géom. beside the finite-index claim.',
 'Determine which geometric group, cover or tensor subcategory is intended; do not silently replace it by the Mumford–Tate group of a Tate square.',
 'The Q(−2) infinite-index counterexample is conditional on the minimal rank-one category withoutQ(1). CM20’s Hodge-maximality distinction may matter. CL-SA07-427.',
 'critical','Undefined margin blocks an unqualified manuscript refutation')
R(51,'780','est|pas in the final motive-dependent commensurability sentence.',
 'Confirm the negative and its scope.',
 'The preceding strong-approximation implication is conditional;Gm fails density. The opposite reading can reverse the intended conclusion. CL-SA07-430; C07.',
 'critical')
R(51,'782–784','Undefined independence and A_fin=∏Zl.',
 'Recover the missing equivalence and whether the product means integral finite adeles, while other leaves use∏Ql.',
 'Arithmetic openness and rational-point density depend on the ring and topology. CL-SA07-431,442.',
 'critical','No forced expansion of independence or adele convention')
R(53,'815–834','Gal(k/k0) and a dotted semilinear action, withk of infinite transcendence degree.',
 'ConfirmAut(k/k0) versus arithmeticGal(k0bar/k0) at each occurrence and preserve the dot on the semilinear action.',
 'Only the finite realizations factor through the arithmetic quotient; fullAut(k/k0) is not the usual profinite absolute Galois group. CL-SA07-475.',
 'critical')
R(55,'870–879','Integral product∏G(Zl),Q corrected toZ,andOn vérifie|On considère.',
 'Check the integral coefficient corrections and the verb; existence of an integral tensor comparison is stronger than a rational comparison.',
 'DM12 torsor representability does not imply an integral point. CL-SA07-432; MP-SA07-224.',
 'critical')
R(55,'881','Fixingg_infty determines all finite components.',
 'Confirm which component is being fixed and the stated diagonalG(Z) ambiguity.',
 'For a faithful integral model, either one faithful component or all finite components kill the diagonal ambiguity; this conditional uniqueness does not prove existence. CL-SA07-433.',
 'high')
R(55,'890–900','Deleted assertion that every complex-place fiber has cardinal2.',
 'Confirm deletion; if retained anywhere, the conclusion needs conjugation to fixk0.',
 'The exact stabilizer isAut(k/k0)∩{1,c_v}, of size1 or2. CL-SA07-434; computations.md §9.',
 'critical')
R(57,'944–948','Cancelled superscripts tau|−1 onphi andpsi.',
 'Check that the live right-cocycle and inverted left-cocycle laws have exactly the displayed multiplication order and no surviving extra inverse.',
 'C08 verifies the two laws noncommutatively. A stray inverse changes the convention. CL-SA07-435.',
 'critical')
R(59,'971','psi|phi is a1-cocycle.',
 'With the standard left convention,psi=phi^−1;phi itself satisfies the explicitly written right convention.',
 'The choice affects the descended torsor action and coboundary formula. CL-SA07-435–436.',
 'critical')
R(59,'973','xi_(M,k0|infty)',
 'Confirm the de Rham fiber functor and coefficient field in the torsor identification.',
 'The two tensor functors must have a common base beforeIsom⊗ is a torsor overk0. CL-SA07-436.',
 'high')
R(59,'980–981','elle l’est déjà followed by unfinishedpi transcendant surk0.',
 'Confirm the continuation and its attachment; do not turn this into an unconditional arithmetic density theorem.',
 'The paragraph names a conjecture and stops; minimal curve descent does not settle minimal motive descent. CL-SA07-439–440.',
 'critical')
R(61,'1020','(sigma g)^−1g inserted in place ofg^−1g^sigma.',
 'Preserve both versions and the explicit au lieu de correction.',
 'Only the live expression satisfies the written right-cocycle convention. C08; CL-SA07-438.',
 'critical')
R(61,'1021','g n’est|g est déterminé mod multiplication parg0∈G(k0).',
 'Confirm the negative and whether the multiplication side is indicated. Forphi_sigma=(sigma g)^−1g, left multiplication ofg byG(k0) leavesphi unchanged; right multiplication conjugates it.',
 'Direct noncommutative substitution using the liveL1020 convention. CL-SA07-438; computations.md §10.',
 'critical')
R(61,'1027','g^sigma takes all generic values, then expressionsg^sigma g^−1 andag.',
 'Check inversion, order and the field over which genericity is asserted; do not replace the actual image by its generated subgroup.',
 'The actual-image criterion needsAut(k/k0) with enough transcendence degree. C15 distinguishes actual image and generated subgroup. CL-SA07-437,439.',
 'critical')
R(61,'1035','Target quotientGal(k/k0bar|k0bar/k0).',
 'The arithmetic quotient receiving restriction isGal(k0bar/k0); its kernel isAut(k/k0bar).',
 'This is the exact sequence needed for the finite-realization kernel inclusion. CL-SA07-475,481.',
 'critical')
R(61,'1031–1036','hom total intoG(A_c|C) and an open subgroup closure;Il me semble and marginal? survive.',
 'Confirm action versus cocycle, theA subscript and the intended topology; preserve the tentative language.',
 'A cocycle gives a homomorphism into a semidirect product, and Zariski density does not imply adelic or analytic openness. C18; CL-SA07-441–442.',
 'critical')
R(62,'1041','qu’une|ici une petite vérification;w…v→v′.',
 'Confirm the exact change of reference and whetherw orv′ is the new place.',
 'The following derivation assumesM_w^Z=gM_v^Z. Misidentifying source and target reverses the gauge formula. CL-SA07-443.',
 'high')
R(62,'1074;1078','Deleted formula ends withg_infty, while the live box ends withg_infty^−1.',
 'Preserve the correction; the live inverse is required.',
 'C08 free-word certificate provesphi_w=sigma(g)phi_vg^−1 and the finite cancellation. CL-SA07-443–444.',
 'critical')

with (P/'readings.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['cote','scan','line','reading','alternative','evidence','weight','confidence'],delimiter='\t')
 w.writeheader();w.writerows(rows)
print('Saved',len(rows),'mathematical reading alarms. No scan decisions or source emendations.')
