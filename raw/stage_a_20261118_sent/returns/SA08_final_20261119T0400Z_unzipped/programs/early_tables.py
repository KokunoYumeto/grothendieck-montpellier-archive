"""Write manually adjudicated early problems, reading alarms and checked links.
The data below were authored after passage reading; no cue-based adjudication.
"""
from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1];O=R/'work/early'
claims={c['id']:c for c in json.loads((O/'claims.json').read_text())}
items={i['id']:i for i in json.loads((O/'items.json').read_text())}
problems=[]
def p(n,title,cs,as_he,plausible,worth,why='The supplied pages leave the step open or sketch it; no checked source documents a specific reason for abandoning this exact question.'):
 cc=[claims[f'SA08-C{x:03}'] for x in cs]
 problems.append(dict(id=f'MP-SA08-{n:02}',title=title,occurrences=[{'claim':c['id'],'cote':'136','scans':c['scans'],'lines':c['lines']} for c in cc],as_he_states=as_he,plausible_today=plausible,state_of_art=[{'claim':c['id'],'class':c['class'],'exact_result':c['fate'],'refs':c['refs']} for c in cc],why_open=why,worth=worth,refs=sorted({r for c in cc for r in c['refs']})))
p(1,'Historical attributions and arithmetic scope',[1,3,4,5],
 'The outline queries whether the notion of differential forms is due to Poincaré and compresses analytic and arithmetic predecessors, including an uncertain base-scheme parenthesis.',
 'Keep priority and the exact arithmetic theorem separate; identify the named source before assigning a comparison theorem or torsion claim.',
 'Worth a bounded documentary check because it prevents a compressed lecture outline from becoming a false historical theorem.')
p(2,'The recalled Sullivan equivalence',[6,67,68],
 'The historical outline adds “sauf erreur” to simple connectivity and recalls a categorical recovery theorem.',
 'Rational nilpotent finite-type homotopy and its minimal models, with simply connected finite-type case as the clean baseline; no integral equivalence follows.',
 'The exact English donor is now identified, so further work is useful only to align its finiteness appendix and the precise category used in the lecture.')
p(3,'Cohomology for a general divided-power triple',[8,9],
 'The simplex algebra for (S,J,t) resolves S objectwise, but he expressly says its global cohomology is not generally ordinary S-cohomology.',
 'A comparison requires separate simplicial/section acyclicity; the universal weighted case and the later complete filtered case have their own hypotheses.',
 'Worth isolating the weakest useful acyclicity hypotheses because the construction itself exists for more triples than the comparison theorem.')
p(4,'Recovering cup products and divided-power information',[13,15],
 'He says sufficiently high shadows recover the ordinary cup pairing and seeks a derived multiplicative recovery retaining the extra structure.',
 'Cartan’s binomial-weight product recovers ordinary cohomological pairings; a monoidal derived shadow localization requires an additional construction.',
 'High value: state the tensor product and equivalences precisely, beginning with the ×2 pairing between first shadows.')
p(5,'Global specialization at T=1',[16,17],
 'The ordinary rational specialization is proposed, followed by a bracketed more general coefficient specialization.',
 'The coefficient quotient is k⊗Q; the global statement must specify direct sums versus products/completion and commute specialization with the relevant limits.',
 'High value and tractable: finite simplicial objects and an infinite discrete test separate the valid coefficient identity from global comparison.')
p(6,'Integral homotopy from virtual divided-power de Rham complexes',[18],
 'For connected simply connected spaces with degreewise finitely generated integral cohomology, he asks for an equivalence with suitable virtual PD de Rham objects.',
 'Specify the enhanced category and comparison functor; Mandell and Horel prove recovery for different E∞ and binomial targets, not this category.',
 'High interest, but one short run should only formulate a comparison on a bounded family of spaces.',
 'Pursuing Stacks §94 reports that other work and then personal commitments interrupted the earlier approach; it does not document a mathematical impossibility.')
p(7,'Operations beyond multiplicative automorphisms',[26,59,78],
 'He reports partial negative results for multiplicative automorphisms, leaves operations to explicate, and names Steenrod/Whitney-type operations.',
 'A higher-operation package may recover information absent from that restricted automorphism method; residual binary/PD operations alone are not certified complete.',
 'Worth developing after defining the target structure, with Cartan–Miller higher products as an exact comparison baseline.')
p(8,'Integral minimal models',[19],
 'He asks for Sullivan-like minimal models expressing homotopy groups and explicitly says he has done nothing in this direction.',
 'Compare to Ekedahl’s minimal numerical spaces for nilpotent finite-type spaces; do not identify numerical maps or their homotopy uniqueness with strict PD algebra uniqueness.',
 'Interesting but broad: first determine whether a small simply connected example admits compatible numerical and weighted PD models.')
p(9,'A structured Künneth formula',[20],
 'No product formula has been developed; he names possible failure of flatness over k{T}.',
 'A derived tensor comparison over Γ_k(T), together with its weight and operation compatibilities, is the plausible target; k-flatness alone is insufficient.',
 'High value: compute the first nontrivial Tor obstruction before proposing a general product theorem.')
p(10,'Dual chains, coefficients and arbitrary colimits',[21],
 'He proposes a dual object corepresenting all coefficient cochains, preserving structures, arbitrary colimits in X and base change.',
 'Coend/Yoneda corepresentability is formal once coefficient functors are fixed; full duals introduce completed PD products and require continuity or finite-weight controls.',
 'Worth a concrete formulation because later scans125–139 realize the promised coend but also expose the completion convention.')
p(11,'Existence of structured flasque replacements',[22],
 'Can every internal PD de Rham object be compared with a quasi-isomorphic object having flasque components, so that structured Rf_* can be defined?',
 'Specify a model/enhanced category and coefficient-stable acyclic resolutions; ordinary sheaf injective resolutions do not automatically preserve all PD operations.',
 'High interest; one run can test a small ringed site and identify which operations survive a known resolution.')
p(12,'Deligne’s cosimplicial-topos problem',[23],
 'The lecture recalls Deligne’s open rational structured-direct-image question for cosimplicial sets; scan91 gives a narrower “Non” to a proposed test-object example.',
 'Distinguish the broad structured RΓ problem from that particular test-embedding condition; the latter negative answer is not a general nonexistence theorem.',
 'Worth a documentary/formulation audit before importing modern rectification theorems.')
p(13,'The remembered paracompact construction',[24],
 'He recalls, with a qualification about memory, that a construction works for paracompact topological spaces.',
 'Identify the actual rational/smooth sheaf model and hypotheses; paracompactness alone does not produce every integral PD enhancement.',
 'A limited literature task could resolve the historical reference and prevent overstatement.')
p(14,'Does C or the larger D retain the whole invariant?',[25,26],
 'He asks whether C_DRpd or even the larger D already recovers the full cohomological multiplicative PD structure under finiteness hypotheses.',
 'Retain the quotient/kernel distinction and the retracted product assertion; completeness requires defined operations and a comparison to homotopy types.',
 'High conceptual interest, but the first task is to formulate the exact datum whose sufficiency is being asked.')
p(15,'Binomial rigidity and all-coefficient extension',[27,28,29,36,37,38],
 'The binomial lemmas and weighted recurrence are developed as the arithmetic mechanism recovering maps from their high tails.',
 'The full all-pairs and weighted-family rigidity statements hold for arbitrary abelian groups; the sparse lemma proves only the adjacent pair equality.',
 'The basic result is settled by the manuscript and independent proof here; useful further work is a clean reusable statement, not rediscovery.',
 'The manuscript supplies successive proofs and corrections; this is a completed local step, not evidence of abandonment.')
p(16,'Adjunction orientation and the nonnegative unit',[30,31,32,40,41,42],
 'He constructs truncation adjoints and claims extension of homogeneous maps, with changing degree conditions and an endpoint mismatch.',
 'Use Hom(τM,N)=Hom(M,ρN), the unit only in the stated nonnegative degrees, and a strict inequality at the lower-target cutoff.',
 'The repairs are tractable and mostly complete here; further work should standardize notation across the later categorical reprise.')
p(17,'Negligible modules and an infinite shadow quotient',[33,34],
 'The literal elementwise tail-annihilated class is called thick and an infinite localization/right-adjoint theory is sought.',
 'The literal class is not extension-closed in Γ_Fp(T)-modules; a bounded-support or suitably finiteness-restricted Serre category is needed before deriving a quotient.',
 'Highest priority: identify a correct abelian category before attempting its multiplicative or derived enhancement.')
p(18,'The induced-target tail Ext corollary',[35],
 'Ext^n_gr(τ_(N−i)S[−i],M⊗_kS)=0 for n>0,i≥0 is stated without an early proof; the later categorical reprise repeats it.',
 'It holds for arbitrary commutative k and every M in the nonnegative PD category. The exact coefficient left adjoint proves that i preserves injectives, repairing the special derived argument. The unrestricted categorical inference remains false.',
 'The exact theorem is now independently proved in this consolidation. Remaining value is a clean presentation and its application to a correctly defined quotient, not further numerical testing of arbitrary bases.',
 'No reason for abandonment is documented. The early page states the corollary; the later categorical argument lacks a general acyclicity hypothesis, but its special PD case has an exact-adjoint proof checked in this run.')
p(19,'Negative-degree maps and infinite divisibility',[43,44,45,46,47],
 'The negative-degree recurrence is used to factor maps through the intersection of all integer multiples, called the largest divisible part.',
 'The literal intersection factorization and torsion-base vanishing survive; the p-local coherent-root chain yields a divisible submodule, but infinite height alone does not.',
 'Worth a clean classification of negative maps after repairing the target language and retaining cross-generator syzygies.')
p(20,'Existence and uniqueness of Stokes integration',[49,50,54],
 'The induction on scan54 leaves existence and uniqueness to establish; scan56 continues the proof, and later pages assemble the natural chain map.',
 'Cartan1976 Theorem2 gives the exact natural integration under objectwise resolution and vanishing above simplex dimension.',
 'This is an established completed step; only the abelian-category formal variant and notation need bounded checking.',
 'The following manuscript pages supply the promised argument, and the published theorem gives the exact result.')
p(21,'Arbitrary coefficient presheaves',[52,53],
 'After the locally constant case he says the tensor resolution should work without local constancy and explicitly marks this for verification.',
 'The literal arbitrary-presheaf statement is false on the simplicial circle; use local systems or a genuinely coefficient-acyclic resolution.',
 'Resolved negatively as stated; the useful next task is to characterize a natural larger coefficient category.')
p(22,'Multiplicativity of integration',[55],
 'The integration comparison’s multiplicative properties are left for study.',
 'Cartan1976 Theorem3 proves multiplicativity on cohomology under flat-cycle hypotheses; strict chain multiplicativity is stronger.',
 'The cohomological problem has a precise published solution; higher coherent compatibility is a separate direction.')
p(23,'Canonical splittings of the simplicial sequences',[60],
 'He asks for simple canonical splittings and discusses a uniquely determined special case p=q=1.',
 'Separate projective existence from natural choice; the special Hom-vanishing gives uniqueness only after existence.',
 'A short run could compute low weights and determine the naturality obstruction, making this a concrete subsidiary task.')
p(24,'Test embeddings with tensor-stable acyclicity',[61,63],
 'Choose k→Φ with flat quotient and positive divided/exterior powers acyclic after tensoring with every sheaf; this is the condition de De Rham.',
 'The resulting conditional comparison is plausible/standard in the free simplicial case; existence in arbitrary ringed topoi is an additional question.',
 'High value: test named topoi and state whether acyclicity is absolute, on every slice, or relative to a fixed f.')
p(25,'Relative derived direct images',[62],
 'The same test-object calculation is asserted more generally for f_* and Rf_*.',
 'Require f_*-acyclicity with the needed coefficient and base-change stability; absolute Γ-acyclicity is insufficient.',
 'Worth a local counterexample-or-criterion task that separates absolute from relative hypotheses.')
p(26,'Independence of comparison maps',[64],
 'For λu=μu=u′ he asks what can be said of the two resulting maps and develops common enlargements.',
 'Common enlargement may identify maps after localization; connectedness, simple connectedness and higher coherence are different assertions.',
 'High value after the admissible category is fixed; a short run can audit the two-map equalization argument.')
p(27,'Universal coefficient quasi-isomorphisms',[65],
 'A comparison is declared universally quasi-isomorphic after ordinary Γ_k(T)-linear coefficient tensoring, followed by an unfinished proof.',
 'A derived tensor statement with explicit flatness/acyclicity conditions is the plausible target; ordinary k-flatness does not suffice.',
 'High priority because this is needed before transporting the whole structure across coefficient rings.')
p(28,'The special category and its localization',[66,64],
 'Special structures are defined and all fixed-base, marked-parameter morphisms are called quasi-isomorphisms; a category of fractions is proposed.',
 'Exclude degree0 from the vanishing axiom, retain fixed k and T, and separately prove existence and coherence; later111–121 makes the groupoid uniqueness question explicit.',
 'Worth completing the definitions first; a bare category of fractions is not by itself an enhanced homotopy theory.')
p(29,'The withdrawn cochain argument on scan48',[79],
 'A crossed-out argument is followed by the tentative reading “faux déjà pour M=0”; the complete proposition being withdrawn is obscured.',
 'Retain the withdrawal and do not infer a universal counterexample until the relevant ink and quantifiers are recovered.',
 'This is a scan-check task, not a research theorem; the supplied transcription cannot determine its exact former claim.',
 'The text itself withdraws the attempt; no reason beyond the partly legible M=0 remark can be certified.')
(O/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

readings=[]
def r(scan,line,reading,alternative,evidence,weight='high',confidence='high'):
 readings.append(dict(cote='136',scan=str(scan),line=line,reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
r(8,'A tex180–185','Φ_{*k}→k as the displayed augmentation direction','The diagonal k→Φ_{*k} defines Ψ=Φ/k','The quotient and later exact sequence require the injection; no manuscript scan supplied.')
r(9,'A tex211–215','si p=0 after si p≠0','p≠0 in the second acyclicity sentence','Γ⁰Φ=k_* is the exceptional constant object; scan231 tex1400–1420 supports positive complementary degree only.')
r(10,'A tex230–244','H⁰(X,k)⊗k{T} in formulas followed by H^q','H^q with fixed total-weight truncation','The fixed-weight comparison includes arbitrary cohomological degree q≤w; the first two H⁰ occurrences cannot express it literally.')
r(25,'A tex658–674','tensor over S in the shadow coefficient expression','tensor over k where the coefficient module has only a k-action','The induced module M⊗_kS and its grading determine the well-typed base ring.')
r(26,'A tex685–694','Hom adjunction with τ and ρ reversed','Hom(τM,N)≅Hom(M,ρN)','Q[T] tail test distinguishes the two orientations; later250 tex600–655 writes the correct adjunction.')
r(27,'A tex705–718','possible unit without explicit lower bound on i','retain 0≤i≤N−1 and nonnegative reconstruction','Negative-degree maps into Q[T] tails show that an all-Z-graded unit is stronger and false.')
r(28,'A tex751–761','c_{k,k−i}','c_{i,k−i}=binom(k,i)','For i=1,k=2 the intended coefficient is2 whereas c_{2,1}=3; theorem statement and scan275 use the former.')
r(29,'A tex768–790','Z_p in localization/unit discussion','Z_(p), if localization rather than p-adic completion is intended','The proof uses only inversion of integers prime to p; it does not use completeness. Notation must be checked on ink.','medium','medium')
r(32,'A tex909–926','zero versus unit in the high-index coefficient condition','p-unit/nonzero modulo p in the prime-local step','Bezout/uniqueness uses an invertible coefficient at J=p^r−1; a zero coefficient cannot establish it.','high','medium')
r(33,'A tex932–975','deleted one-generator tail claim','keep cancelled status; no literal mathematical repair asserted','Over F2, deleting the degree-N generator does not generate the same tail at N=3.')
r(34,'A tex980–1002','w′=p+w′ or similarly repeated symbol','a non-self-referential new cutoff','The displayed equality cannot hold for a positive increment p; exact alternative needs ink.','medium','low')
r(35,'A tex1008–1031','unfinished (n+1)! line','no completion supplied','The subsequent p-typical unit computation is complete but cannot fill the abandoned line.','medium','high')
r(39,'A tex1144–1178','degree threshold being corrected on page','retain corrected target-cutoff condition','Every source degree must land at or above target cutoff; binomial coefficients remain essential.')
r(41,'A tex1220–1242','α≤j≤β−d','α≤j<β−d','F2,α1,β3,d1 multiplication by T is nonzero but the extra endpoint would kill it; executable witness saved.')
r(43,'A tex1304–1352','de degré d with output p^s−d','degré −d for positive d','Scan45 and later299 recurrence show the negative shift. Do not identify both uses of d silently.')
r(43,'A tex1304–1325','monomials with no visible digit bounds','0≤i_a<p, finite support','The stated lower-weight equivalence requires base-p digits; arbitrary exponents violate it.')
r(43,'A tex1325–1352','the listed p-typical relations treated as sufficient','necessary relations only unless cross-generator syzygies are added','T_(r+1)e_r−T_re_(r+1) survives the displayed presentation over F2 but maps to0 in the tail.')
r(45,'A tex1385–1417','intersection ∩nN called the largest divisible submodule','separate infinite height from coherent divisible chains','The saved group <x,y_n | px=0,p^ny_n=x> has intersection Z/p, not divisible. This may be an authorial error rather than misread ink.')
r(45,'A tex1413–1417','earlier modernization says both Hom targets identical','current transcription distinguishes N_S and N_{0S}','The frozen transcription already has the distinct targets; do not import the modernization’s proposed textual defect.','medium','high')
r(46,'A tex1438–1446','Fil¹E=E, Fil⁰E=F, Fil^(−1)E=0','modern decreasing convention reverses the ±1 endpoints','The same literal formula is in SGA7 printed494/PDF499, while printed498 says the toric jump is−1. Published source inconsistency confirmed; manuscript ink remains unchecked.')
r(48,'B tex35–79','faux déjà pour M=0 (tentative)','retain tentative reading and cancelled context','The proposition being withdrawn is too obscured to reconstruct uniquely.','high','low')
r(50,'B tex110–162','right-adjoint evaluation indexing','product indexed by Hom_Δ([n],[p]) for u_{n*}(M)_p','For contravariant presheaves, right adjunction to evaluation at n uses maps p→n in Δ^op, i.e. n→p in Δ. Distinguish from the other Kan extension.')
r(58,'B tex515–532','Hom(Δ^op,Ens) for the slice presheaf category','Hom((Δ/X)^op,Ens)','The next sentence itself supplies Δ/X; the displayed equivalence is missing the parameter.')
r(59,'B tex553–559','ker(Z^K→Z^(I×J))','ker(Z^K→Z^I⊕Z^J)','Original SGA7 printed472/PDF477 has the same defect; nodal-triangle matrices give ranks0 versus1. Source-level mathematical alarm, not a proved transcription error.')
r(62,'B tex616–679','sheaf/co-sheaf variance and sum/product notation in a cancelled diagram','right Kan extension uses products, left Kan extension sums','Adjunction and direction of restriction determine the two constructions; the deleted diagram is not a settled formula.','medium','medium')
r(75,'B tex1250–1269','flasque si p≥0','positive complementary degree p>0','The p=0 constant corner has H¹ on a circle; scan76 says épi si p≠0.')
r(76,'B tex1310–1314','épi si p≠0','retain the exceptional p=0 range','This qualifying line controls the preceding broad inequality and should not be dropped.','high','high')
r(89,'B tex1915–1922','Γ*(Ψ|Φ)⊗Λ*Ψ','Γ*Φ⊗Λ*Ψ','Scans80/83 define the construction with Φ in the divided-power factor; exact glyph still needs ink.')
r(94,'B tex2118–2155','vanishing for every exterior degree','vanishing only in positive exterior degree','Degree0 is separately Γ_k(T), so an all-degree vanishing contradicts the first axiom.')
r(94,'B tex2149–2155','q≤j≤i (q|0 uncertain)','0≤j≤i in total/exterior notation','The weighted comparison has exterior degree j bounded by total weight i; lower bound q is not otherwise defined here.')
r(94,'B tex2150–2160','complementary degree j|i','total degree minus exterior degree','Scan81 states the convention; no formula from the later context decides the glyph.')

def tsv(name,rows,fields):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv('readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])

links=[]
def link(kind,fr,to,what,evidence,notes):
 stable=['MPL_136_'+('002-046' if v[0]=='A' else '047-094')+'#'+v[1:] for v in notes.split()]
 links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids='; '.join(stable)))
link('folder','136 scans8–10;A tex165–244','136 scans227,231,233;189–234tex1170–1232,1337–1420,1444–1481','Weighted cohomology and actual simplicial contraction','Both passages read: later normalization of Φ is the identity k→k, then the exceptional last term and smart truncation are written explicitly.','A12 A14 A16 B32')
link('folder','136 scan7;A tex133–160','136 scans219–222;189–234tex925–1028','PD Poincaré algebra','Both passages read: the later rank-one/flat-module reduction explains the coefficient-free divided-power differential.','A10')
link('folder','136 scan8;A tex165–198','136 scans215,217;189–234tex777–800,824–884','Parity and graded PD axioms','Both endpoints read; alternation is exterior parity, and the later text specifies strict commutation for mixed parity PD formulas.','A13 B62')
link('folder','136 scans7,12;A tex133–160,261–274','136 scans233,235–241;189–234tex1482–1495 and235–281tex2–243','General triple versus complete filtered comparison','Both endpoints read; later insertion requires grS≅k{T} and retracts an unfiltered formula.','A11 A21')
link('folder','136 scans13,16;A tex279–329;B91tex2023–2050','136 scans100,111–121;095–141tex131–175,416–448,479–518,556–585,604–624,646–685','Flasque/test-object and admissible-theory program','Both endpoints read. The later flat-plus-flasque shortcut is marked false; uniform bounds and a connected/simply-connected localization groupoid become explicit questions.','A26 A35 A36 B43 B45')
link('folder','136 scan15;A tex305–322','136 scans123–139;095–141tex687–773,773–824,850–913,932–1066,1100–1164,1201–1242','Dual corepresenting chains and completed coefficients','Both supplied endpoints read: later coend and coefficient duality use completed PD series. References to153–160 cannot be checked because those transcriptions are not supplied.','A31 A32 A33 A34')
link('folder','136 scans23–27;A tex589–740','136 scans244,250,252;235–281tex248–301,600–655,721–794','Finite shadows and truncation adjoints','Both endpoints read; later formulas separate q⊣i⊣τ⊣ρ and retain the nonnegative unit.','A51 A52 A56 A57 A58 A61 A74 A76')
link('folder','136 scan26;A tex697–700','136 scan256;235–281tex887–921','Two negligible-module notions','Both endpoints read; bounded support is thick, but elementwise tail-annihilation is a different class and is not automatically extension-closed.','A59 A60')
link('folder','136 scan27;A tex729–733','136 scan265;235–281tex1308–1342','Identical induced-target Ext assertion','Both exact formulas read; later attempted derived-functor deduction needs an acyclicity audit, so neither occurrence is erased.','A62')
link('folder','136 scans27–34;A tex737–1002','136 scans275,277;235–281tex1582–1625,1662–1727','Weighted recurrence and coefficient-uniform proof','Both endpoints read; recurrence coefficients and representability via an integral relation module recur.','A63 A64 A68 A70')
link('folder','136 scans41–45;A tex1245–1417','136 scan299;282–327tex668–716','Negative-degree recurrence','Both endpoints read: c_(i,l)ξ_(i+l)=c_(i−d,l)ξ_i. Later notation does not remove the infinite-height/divisible distinction.','A79 A82 A83 A84 A86')
link('published work','136 scans49,51,53;B tex86–107,169–197,257–290','Sullivan1975 author typescriptpp6,5,4','Exact reused English donor','Full original PDF and author bibliography opened; paragraphs and TheoremB match. Tokyo1973 lecture and1975 publication distinguished.','B59 A6')
link('published work','136 scans8–10,69,81–83;A tex165–244;B tex939–987,1530–1645','Cartan1976 §§3–7 pp264–271','Published weighted comparison and integration','Theorem1 separates both acyclicity conditions; Theorem2 gives additive integration; Theorem3 gives cohomological multiplicativity; §7 matches the weighted Γ construction.','A1 A12 A16 A18 B18 B32 B33')
link('published work','136 scans36,38,46;A tex1035–1054,1124–1138,1422–1446','SGA7IX1972 §§13.4.2–18 pp494–498','Exact reused analytic/Hodge donor','Published PDF pages499–503 collated; source indices retained. Donor source predates new PD work.','A91 A92 A93 A94 A95 A96')
link('published work','136 scans55,71,73;B tex366–388,1065–1087,1140–1158','SGA7IX1972 end10.4/11.0 and11.6.4–9 pp448,457–458','Exact reused monodromy/component donor','Published PDF453,462–463 read.','B60')
link('published work','136 scans57,59,61,63;B tex480–507,541–559,594–609,688–710','SGA7IX1972 §§12.1.6–10,12.3.1–14 pp467,470–473','Exact reused Picard/Néron donor','Published PDF472,475–478 read;12.3.10 product-target defect visually confirmed.','B60')
link('published work','136 scans90,92;B tex1972–1994,2058–2093','SGA7IX1972 §§13.3.9–16,13.4.1 pp492–493','Exact reused analytic extension donor','Published PDF497–498 collated.','B60 A91')
link('published work','136 scans13–18;A tex279–365','GrothendieckPS1983 §94 originalpp339–342;§124p521','Retrospective and distinction of approaches','Both endpoints read in full arXiv text; PD, diagonal-category and unipotent approaches remain distinct.','A25 A26 A35 A98 B62 B57')
link('published work','136 scan9;A tex211–215;B78,80,83','GrothendieckPS1983 §111 originalpp455–456','Homotopy versus nonlinear derived invariance','Both endpoints read; projectivity caveat concerns a different generalization.','A14 B63')
link('published work','136 scans69,80–83;B tex974–987,1488–1645','GrothendieckPS1983 §§119–120 originalpp501–507','Divided powers, binomial operations and W2','Both endpoints read; the later polynomial-extension counterexample is not transferred without a functor comparison.','B56 B55 B65 B66')
link('published work','136 scans58–64,81,91;B tex515–749,1530–1578,2023–2050','GrothendieckPS1983 §§127,135–136,138–139 originalpp536–537,563–568,581–582,590–591','Coefficients, slices and derived operations','Both endpoints read; coefficient and section scopes are not interchangeable.','B11 B50 B58 B64 B67 B68')

# The target project files are not attachments. Preserve named leads without
# pretending a two-endpoint mathematical comparison has been performed.
for to,what,notes in [
 ('WG2 §2.4 #5; README S11(i); WG2 §Week #3','Lecture/history/application planning; no named new de Rham topos or Fourier example established','A3 A4 A5 A91 A94 A98 A99 B62 B60 B61'),
 ('follow-ups @305; gap g1048','Integral homotopy and derived multiplicative shadow program','A1 A18 A20 A25 A26 A27 A28 A29 A30 A59 A60 A62'),
 ('follow-ups @304','Filtered binomial comparison lead','A19 B55'),
 ('gap g1004','Admissible-theory uniqueness and coherence','A26 A35 A36 B38 B40 B41 B45'),
 ('g1031; g1034; g1035; g1041; g1080 (within gap g1048)','Earlier runs label finite-tail/linear repairs settled; those labels are not independent proof','A51 A52 A57 A58 A61 A63 A64 A74 A85'),
 ('Hua findings136-pd-de-rham-shadows; Hua findings136-shadow-full-faithfulness; hua_project/136.modern.tex','Modernization and candidate statements; actual supplied manuscript determines parity, quantifiers and errors','A12 A13 A15 A17 A51 A62 A65 A82 A83 A87'),
 ('MPL_150_085-099+151_001-031 H05','Only title and three scan locators supplied in the notes; full question unavailable','A90 A100'),
 ('MPL_121_001-048 Q1; MPL_152+120 Q1-06','Definition of ombre; no definition of tubulure found here','A89'),
 ('MPL_133 B10','Abelian-variety/Fourier application speculation; donor faces do not establish it','A91 A93 A94 A99 B60 B61'),
 ('WG H6; GALOIS G.6; GALOIS E.11; BISITE D.12','Enhanced recovery/direct-image analogies only','A98 B45 B57 B58'),
 ('GALOIS D.2; BISITE A.19; BISITE C.1','Local-system and slice coefficient scope leads','B50 B58 B64'),
 ('MPL_134-8_043-087 R033; PRETOT A.1','Separate tensor-acyclicity/projectivity audit lead','B63 B67'),
 ('PRETOT A.12; TOTASPH C.10; TOTEX2 D.1; EXIT_TOWER E.49; LM7_PUSH E.3; ANABELIAN_SUCCESSOR A.3; FINMON C2-CP2','Explicit non-links: the earlier notes warn against importing these results by shared words','A43 A59 A75')]:
 link('our projects','Early notes and the manuscript loci in the named item records',to,what,'The source note and its manuscript passage were checked. The named project/context target file is not supplied; this is an unverified context lead, not a checked result or asserted cross-project implication.',notes)
tsv('links.tsv',links,['kind','from','to','what','evidence','note_ids'])
tsv('project_links.tsv',[x for x in links if x['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])

events=[]
who='GPT-6 Astra Pro; effort not exposed by runtime; SA08/early'
def event(s,t,out,checker=None):events.append(dict(statement_id=s,date='2026-11-19',who=checker or who,type=t,outcome=out))
for i in items.values():event(i['id'],'used and rechecked in this run','Read all source note entries and the cited actual transcription passages; '+i['check']+': '+i['check_reason']+' This event is textual collation, not an independent proof.')
for c in claims.values():event(c['id'],'used and rechecked in this run','Statement/hypotheses collated with manuscript and the exact source/search scope in fate. '+c['computation'])
for n in [8,14,16,27,29,32,36,37,38,40,41,43,45,47,50]:event(f'SA08-C{n:03}','independent re-proof','General proof recorded in work/early/proofs.md; finite computations are supporting checks, not the universal argument.')
event('SA08-C080','targeted proof check','Substituting dx=0 in the stipulated differential PD identity proves that γ_n(x) is a cycle. No representative-independence assertion follows from that substitution alone.')
event('SA08-C081','independent re-proof','Homogeneity and T^[1]T^[3]=4T^[4]=0 show the PD ideal generated by T^[3] has zero degree4 overF₂; higher PD powers begin in degree6. Thus it differs from the full tail, exactly as the manuscript correction requires.')
for n,refined in [(31,'SA08-C032'),(33,'MP-SA08-17'),(42,'SA08-C041'),(44,'SA08-C045'),(46,'SA08-C045'),(53,'SA08-C052'),(75,'SA08-C075 mathematical reconstruction')]:event(f'SA08-C{n:03}','refuted, with the refined statement’s id','Literal strengthened statement refuted; refined statement: '+refined+'. Exact counterexample and hypotheses in proofs.md and linked output.')
event('SA08-C035','targeted proof check','Critically reviewed root/tail_ext_restricted_proof.md; characteristic-p arbitrary-module and rational cases validated, including coinduction degree and telescope. This earlier partial check is superseded in scope by the separate exact-left-adjoint proof.')
event('SA08-C035','independent re-proof','Independently checked late/proofs.md §5: coefficient presentation, unit binomial normalization at ℓ^r−1, all relations in the cofinal colimit, prime-local exactness, preservation of injectives and derived finite-tail vanishing. Covers arbitrary commutative k and arbitrary M in the nonnegative category.')
event('SA08-C035','targeted proof check','Root independently read late/proofs.md §§3–8 and verified the exact L argument including all presentation relations and binomial units; root message 2026-11-19 accepted full arbitrary-k nonnegative Ext theorem. This is not a published fate identification or novelty claim.','GPT-6 Astra Pro; effort not exposed by runtime; SA08/root (review communicated to early)')
event('SA08-C035','computation or formal certificate','early_exact_adjoint.py and early_exact_adjoint_output.json check7770 coefficient-presentation identities,3640 transition identities and607 prime-local binomial units exactly. The general exactness proof is structural and separately recorded.')
for n in [8,10,13,14,16,27,28,29,31,33,36,37,38,39,42,43,44,46,50,75]:event(f'SA08-C{n:03}','computation or formal certificate','Exact saved program/output: early_computations.py→early_computations_output.json, or C075 early_sga_graph.py→early_sga_graph_output.json. Scope is the finite cases/identities specified there.')
for key,outcome in {
 'Cartan1976':'Full §§1–7 read; Theorems1–3 and §7 weighted comparison matched. No strict multiplicativity inferred.',
 'Sullivan1975':'Original typescriptpp4–9 and author bibliography read; exact donor identified, finite-type appendix not independently audited.',
 'Sullivan1977':'Parent opened complete original; §§7,8,10 used as later full development, not independently re-proved here.',
 'NagpalSnowden2017':'Author preprint§8.1 Th8.3 andRemark8.4,§9 Props9.5,9.7–9.9 read; target and completeness restrictions retained.',
 'Horel2024':'Current author versionTheorems5.4/6.1 read; connected nilpotent finite-type hypothesis and binomial target retained.',
 'Ekedahl2002':'ArXivTh2.9 and following uniqueness discussion read; numerical category distinguished from PD algebra.',
 'Cenkl1989':'§5Theorem2 and earlier higher-product setup read; universal ordinary comparison hypotheses retained.',
 'SGA7IX1972':'Relevant original donor pages collated; graph target and Hodge-index discrepancies visually confirmed as published-source issues.',
 'GrothendieckPS1983':'Actual §§94,111,119–120,124,127,135–136,138–139 passages read; conceptual links retained with separate approaches.',
 'Grothendieck1966':'Theorems1 and1′ pp95–96 read; smooth finite-type complex hypotheses and1963letter/1966publication separated.',
 'Lucas1878':'OriginalNumdampp51–52 opened; digit congruence is explicit onp52.',
 'Stacks2026':'Official category-cohomology and divided-power pages opened; used as standard definitions, not evidence for the exact proposed PD enhancement.',
 'DGMS1975':'Original introduction and §5 pp262–269 read; compact Kähler hypotheses, decomposition and conjugate filtration retained. Earlier Hodge theory is background, while the paper proves the stronger formality result.',
 'GarvinEtAl1998':'Full eight-page original read independently after late-agent download. Proposition3.2, Remark3.3(i), Theorem4.2 checked. Use p<q, never infer the endpoint from Theorem4.3 wording.',
 'CenklPorter1982':'Original printed10–11 visually inspected: Proposition1 p<q with binomial product, Theorem1 DASH extension, Theorem2 wedge-i products. This confirms the exact higher-operation comparison without identifying all manuscript structures.',
 'CenklPorter1984':'Original printed35/44 visually inspected and official PDF opened. Q_q inverts primes≤q; Theorem4.1 q≥1, all p, finite-type simplicial complex with cubical subdivision.',
}.items():event(key,'used and rechecked in this run',outcome)
for n in [23,38,105,106,111]:event(f'SA08-{n}','independent re-proof','The corresponding differential identity, integer-valued leading coefficient, factorial-colimit calculation or ordinary-cohomology obstruction is proved in work/early/proofs.md and supported where applicable by saved exact computations. This is the earlier-run mathematical idea checked here, not an assertion newly attributed to the manuscript.')
for key,outcome in {
 'deRham1931':'Original bibliographic record verified; complete analytic proof not independently re-proved.',
 'CartanStein1952':'Original exposé18 TheoremsA/B opened; proof in following exposé not independently audited.',
 'Roby1963':'Primary original available and root checked free divided powers; standard algebra used with independent calculations here, not a claim of a new general polynomial-law proof.',
 'EGAIV4':'Primary metadata verified; theorem citations17.9.1 and21.8.5 followed through SGA7 IX only.',
 'Miller1978':'Metadata and prepublication existence verified through original Cartan/Garvín references; exact full theorem not independently asserted here.',
 'Swan1975':'Metadata verified in original Garvín reference9; rational theorem supported by Cartan/Sullivan, no independent Swan proof check.',
 'Mandell2006':'Root opened original MainTheorem andTheorem0.1; hypotheses and faithful-not-full conclusion retained as external result.',
 'InfiniteHeightMO2022':'Opened exact presentation in discussion; its mathematical properties independently proved here.',
}.items():event(key,'carried as background without fault found',outcome)
tsv('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
print(json.dumps({'problems':len(problems),'readings':len(readings),'links':len(links),'check_events':len(events)},indent=2))
