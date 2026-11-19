"""Encode the manually read cote 33 review. No keyword-based verdict logic."""
import csv,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable/shards/p1';OUT.mkdir(parents=True,exist_ok=True)
P='MPL_33_098-146';F=f'pro/{P}_transcription.tex'
pages={int(p['scan']):p for p in json.loads((ROOT/'work/pages.json').read_text()) if p['file']==F}
items=[];entries=[]
def add(n,src,kind,scans,words,statement,reconstruction,check,reason,verdict='kept',ranges=None):
    locations=[]
    for s in scans:
        p=pages[s]; a,b=(ranges or {}).get(s,(p['start'],p['end']))
        locations.append(dict(file=F,cote=33,scan=s,start=a,end=b))
    item=dict(id=f'SA13-{n}',sources=[f'{P}#{v}' for v in src],kind=kind,cote=[33] if scans else [],scans=[f'33:{s:03}' for s in scans],lines=locations,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason)
    items.append(item)
    for k,e in enumerate(src):
        entries.append(dict(entry_id=f'{P}#{e}',item_id=item['id'],verdict=verdict if k==0 else 'merged',reason=reason+(' Same object or repeated register material as the first source.' if k else '')))
add(1,[1,2,70],'other',[],'No manuscript quotation: these entries describe the earlier run’s context.',
    'The context key and results register describe earlier projects, including LM7 E.23, LM4 D.12/F.7, LM7_PUSH C.6, WG H9, WG2 §2.1 #2, and S19. None is a claim of the supplied manuscript.',
    'Context files and underlying research runs are not supplied. Their reported statuses are retained as attributed leads only. Cote/scans in this register are not locators in the present transcription.',
    'agrees','Read all register rows; the notes themselves deny a mathematical status change. These repeated scope limits are consolidated.',ranges={})
add(2,[3],'unpursued implication',[98],'D “échange”',
    'For constructible torsion complexes in a context with a dualizing complex and the usual six functors, Verdier duality exchanges Rf_* with Rf_!, and Lf^* with f^!. A closed-immersion internal-Hom comparison is calculated on the sheet.',
    'The precise constructibility, boundedness and dualizing hypotheses are modern sufficient hypotheses, not all repeated in this continuation page.',
    'agrees','The immersion calculation is visible at lines 5–12; the exchange program follows at 18–25. A proof sketch is present, so this is not wholly unsupported.',ranges={98:(3,25)})
add(3,[4],'unproved claim',[100],'Tout Module $F$ ... est quotient d’un plat',
    'On a ringed topos every module admits a flat resolution; every bounded-above complex has a bounded-above flat resolution. Localizing their homotopy category at quasi-isomorphisms computes D^-, and tensoring flat resolutions defines derived tensor.',
    'The category is the category of sheaves of modules; flat generators are sheafified free modules on site objects. K-flat terminology is modern.',
    'agrees','Lines 51–60 assert all these steps; existence is sketched using A_U, while descent through quasi-isomorphisms is asserted.',ranges={100:(49,60)})
add(4,[5,6],'self-flagged step',[102,104,106],'est-ce vrai dans le contexte des topos généraux ?',
    'For any morphism of ringed topoi, pullback preserves flat modules; Lf^* exists, commutes with derived tensor, and satisfies L(gf)^*=Lf^*Lg^*. The initial flat-morphism restriction is later removed.',
    'The interpretation of the marginal question as attached to flat preservation/tensor compatibility is local syntactic evidence. The modern unbounded extension is not attributed to the draft.',
    'agrees','The margin at 102 qualifies the adjacent construction; 104 expressly introduces nonflat base change and 106 gives transitivity. They concern one construction, not a retraction.',ranges={102:(73,79),104:(119,125),106:(132,135)})
add(5,[7],'self-flagged step',[104],'que $\\Gamma_X$ est de dim ... finie !',
    'Finite cohomological dimension of Γ suffices to apply RΓ to bounded-above derived tensor products while preserving an upper bound; bounded-below injective resolutions give the stated RHom construction.',
    'This is a boundedness condition in the draft’s formalism. Modern unbounded derived functors can exist without it; no general nonexistence claim is inferred.',
    'agrees','The finite-dimension qualification is marginal at 94; the RHom range is separately stated at 108.',ranges={104:(90,123)})
add(6,[8,9],'withdrawn in the same text',[106],'Attention, ... $f$ est plat',
    'Lf^* is left adjoint to Rf_*; the sheafified adjunction is Rf_*RHom(Lf^*L,K)=RHom(L,Rf_*K). The argument that direct image preserves injectives uses flatness of f^* and is qualified on this sheet.',
    'The later generator/localization argument is a repair sketch, not an arbitrary Cartesian-base-change theorem. Modern K-injective/K-flat versions supply sufficient resolutions.',
    'agrees','Both the original calculation (149–154) and the correction (156) survive in the transcription; 160–177 gives internal and external Hom. Only the unrestricted proof is withdrawn.',ranges={106:(143,177)})
add(7,[10,12],'idea of the earlier run',[108,112],'même si $X$ ... un pt géométrique !',
    'For A=Z/ℓ² and k=A/ℓ, Tor_i^A(k,k)=k and Ext_A^i(k,k)=k for every i≥0. Thus bounded cohomology of finite modules need not imply bounded derived tensor or Hom.',
    'The periodic resolution is the earlier run’s explicit witness, not a formula on the manuscript. The draft warning must exclude squarefree n, for which Z/n is a product of fields.',
    'agrees','The notes already qualify the arithmetic scope. Their example instantiates the warning at 108/112 and is independently re-proved in computation notes.',ranges={108:(196,204),112:(337,339)})
add(8,[11],'self-flagged step',[110],'C’est peut-être vrai dès que $Y$ est noethérien',
    'The question is whether Rf_* has finite relative étale cohomological dimension for a finite-type morphism with merely noetherian target. The page gives finite-type-over-a-field or over Spec Z as sufficient cases.',
    'Coefficient restrictions and the finite-type scope are inherited from the surrounding torsion discussion; finite absolute cd(Y) is a different assertion. The merely-noetherian quantifier is not silently replaced by finite-dimensional.',
    'agrees','The subject of “peut-être” is f_* at 240–246. The display at 268–270 states the finite-type comparison cases.',ranges={110:(237,279)})
add(9,[13],'reading question',[112],'un isom. canonique bifonctoriel',
    'The intended typed comparison is Rf_!L ⊗^L M → Rf_!(L ⊗^L f^*M), for a compactifiable scheme morphism and torsion coefficients, with the indicated derived ranges.',
    'The pullback on M is a type-correct reconstruction. The duplicated small Rf_* display and missing pullbacks remain unchanged in the source.',
    'agrees','Lines 342–343 repeat the same side; 357–358 omits the pullback. These are concrete scan-review alarms, not proof of the reconstructed formula.',ranges={112:(341,378)})
add(10,[14],'self-flagged step',[114,116],'Il faut vérifier ... fonctoriel',
    'The projection comparison built from resolutions must descend to a natural transformation on the derived categories, independently of resolutions. The subsequent generator/proper-base-change reductions address invertibility.',
    'Naturality and the isomorphism test are separate proof obligations; the “O.K.” on 116 closes the generator calculation, not every omitted coherence diagram.',
    'agrees','The explicit verification request is at 427–429; the reduction follows, continuing at 491–503.',ranges={114:(414,450),116:(491,503)})
add(11,[15],'unproved claim',[116],'S’obtient en appliquant $2$ fois la formule de projection',
    'For compactifiable X→S and Y→S, quasi-compact S, torsion coefficient ring A, and bounded-above complexes L,M, Rh_!(pr_X^*L⊗^Lpr_Y^*M)=Rf_!L⊗^LRg_!M. For sheaves F,G, one flat input and one flat family of compact-support cohomology sheaves eliminate Tor terms.',
    'Pullbacks and coefficient ring are written explicitly in the modern statement. The flatness alternatives in the sheaf corollary are preserved.',
    'agrees','The derived formula and two-step proof indication are separate from the revised flat-sheaf corollary at 523–530.',ranges={116:(505,530)})
add(12,[16],'unpursued implication',[118,120],'si $X$ ... ou ... $Y$ propre sur $k$',
    'Over a separably closed field, for finite-type schemes X,Y with one proper and complexes of Z/n-modules, ordinary derived Künneth holds without requiring n invertible in k.',
    'The separably closed formulation is a modern strengthening of the page’s algebraically closed base. Arbitrary unbounded ranges require the modern finite-cd framework.',
    'agrees','The proof at 580–591 uses proper base change on the proper factor; 637–642 confirms the independence from a prime-to-characteristic assumption.',ranges={118:(565,597),120:(637,642)})
add(13,[17],'conjecture',[118],'je pense qu’on doit encore avoir la formule',
    'If X,Y are finite type over a separably closed field k and n is invertible in k, ordinary derived Künneth holds for Z/n-complexes even with neither factor proper.',
    'The text says algebraically closed; the stated modern theorem permits separably closed. Local duality is the proposed draft proof route, not a completed argument.',
    'agrees','The two-nonproper-factor expectation is explicit at 593–597, with its coefficient restriction.',ranges={118:(593,597)})
add(14,[18],'idea of the earlier run',[118],'à coefficients dans $\\mathbb Z/p\\mathbb Z$',
    'Over algebraically closed k of characteristic p, the Artin–Schreier class xy in H¹_et(A²,k;F_p) is outside the sum of the pullbacks from the two affine lines, so ordinary Künneth fails already in degree one.',
    'Read H¹_et(A²_k,F_p). The mixed-monomial argument is the earlier run’s example, independently checked here, while “même pour H¹” remains an uncertain ink reading.',
    'agrees','The handwritten failure claim is at 569–572. The example proves its strongest indicated degree-one interpretation without deciding the handwriting.',ranges={118:(565,572)})
add(15,[19],'reading question',[120],'aurait d’abord été établie par Verdier',
    'The page reports a conditional priority attribution for a Künneth formula proved using global duality.',
    'No exact priority theorem or date is reconstructed from the conditional verb; later historical accounts do not by themselves identify this draft’s referent.',
    'agrees','The hedged tense is essential and retained. This is a historical reading question, not an open mathematical conjecture.',ranges={120:(637,642)})
add(16,[20],'idea of the earlier run',[120],'ce qui n’est pas vrai si $f$ non propre',
    'For j:G_m→A¹ over an algebraically closed field and a finite field Λ, M=j_!Λ has zero boundary stalk, so (Rj_*Λ)⊗M has zero boundary stalk whereas Rj_*(j^*M) has nonzero H⁰ there. Thus unrestricted Rf_* projection fails.',
    'The explicit scheme and coefficient example is the earlier run’s realization of the page’s support obstruction.',
    'agrees','The support implication at 648–652 is exactly what the example violates. No failure of the Rf_! formula is alleged.',ranges={120:(644,652)})
add(17,[21],'unproved claim',[112,120],'lorsque $M_\\bullet$ est à cohomologie localement constante',
    'The draft asserts ordinary projection for locally constant finite-type cohomology in the presence of finite cohomological dimension; quasi-compact/quasi-separated hypotheses are offered to omit finite type. Over a constant noetherian coefficient ring and enough points, bounded-above pseudo-coherent locally constant targets admit a finite-free dévissage.',
    'The last sentence is a modern sufficient reconstruction, justified by the published way-out argument. Perfect-target projection is a secure different sufficient theorem, not an equivalence of these hypotheses.',
    'agrees','The paragraph stops at “où”; the small proposition’s finite-cd reservation remains. Local constancy is never identified with perfectness.',ranges={112:(341,347),120:(653,665)})
add(18,[22],'conjecture',[122,126],'rationalité des fonctions $L$',
    'The proposed curve application is a Lefschetz formula with singular constructible coefficients and explicit local terms, yielding the cohomological determinant formula for L-functions, without assuming resolution of singularities.',
    'Finite-field and ℓ-adic assumptions belong to the precise rationality theorem reconstructed in the claims map; the page sketches an application and does not specify them all.',
    'agrees','The hope on 122 continues at the top of 126. Neither sentence proves the local-term formula.',ranges={122:(702,708),126:(789,796)})
add(19,[23],'unpursued implication',[122],'je préfère en compléter les lignes essentielles',
    'The author chooses to finish biduality/local-duality and Lefschetz–Cartier foundations before detailed applications.',
    'This is a statement of research organization. It implies neither a theorem nor a connection to Hodge-index assertions in unrelated project registers.',
    'agrees','The preference and inserted identification of biduality with local duality are explicit at 710–721.',ranges={122:(710,721)})
add(20,[24],'unproved claim',[124],'avec grain de sel',
    'A Lefschetz number equals a sum of local fixed-point indices under the appropriate finiteness and fixed-locus hypotheses; isolated points need local multiplicities. The page promises a Verdier/coefficient-sheaf treatment.',
    'The precise derived correspondence framework is supplied separately; the schematic count on this page is not a universal cardinality formula.',
    'agrees','The qualifier immediately follows the count and the later exposition is expressly promised.',ranges={124:(759,772)})
add(21,[25],'unpursued implication',[126],'Il ne serait pas admissible de se limiter à des corps',
    'Finite-level traces over Z/ℓ^ν must be defined on the cohomology complex because its cohomology modules need not be projective; passing only to F_ℓ loses information beyond a congruence modulo ℓ.',
    'This is the author’s stated arithmetic motivation. No trace of an arbitrary finite module over Z/ℓ^ν is inferred.',
    'agrees','The objection and the nonfree-cohomology difficulty are at 792–796; 128 introduces the complex remedy.',ranges={126:(792,796)})
add(22,[26,42],'unproved claim',[128,132,146],'par passage à la limite',
    'For a compatible uniformly bounded system of finite-projective Z/ℓ^ν-complexes and compatible endomorphisms, supertraces commute with reduction and define an element of Z_ℓ. Identifying geometric cohomology with such a system requires additional adic comparison.',
    'The algebraic sufficient mechanism is the earlier run’s idea. The manuscript’s expectation is broader and does not prove the inverse-limit comparison.',
    'agrees','The finite-level/adic hope is at 807; the later run’s matrix test is compatible with 847 and 1274 but adds an explicit uniform-perfect-model hypothesis.',ranges={128:(807,813),132:(845,849),146:(1271,1277)})
add(23,[27],'idea of the earlier run',[126,128,130,132],'remplacer le système des $H^i$ ... par le ... complexe',
    'For A=Z/ℓ², P=[A --ℓ→ A] in degrees 0,1 is perfect, H⁰(P)=H¹(P)=A/ℓ nonprojective, and tr(id_P)=1−1=0.',
    'This concrete example is not on the page; it explains the manuscript’s complex-level construction.',
    'agrees','The example obeys the finite-projective formula at 845–849 and does not confuse perfectness with projective cohomology.')
add(24,[28],'unproved claim',[130],'pseudo-cohérents de Tor-dimension finie',
    'Over a commutative ring, a bounded-above pseudo-coherent complex of finite Tor dimension is represented by a bounded complex of finite projectives; conversely such a representative has both properties. Over a noetherian ring pseudo-coherence in D^- is equivalent to finite cohomology modules.',
    'The modern name is perfect. On a general ringed site the criterion is local and does not assert a global finite-free representative.',
    'agrees','The criterion and closure under mapping cones/tensor are stated together at 826–828 without the truncation proof.',ranges={130:(826,830)})
add(25,[29],'unproved claim',[132,134],'stable par isomorphismes',
    'The supertrace of an endomorphism of a bounded finite-projective complex over a commutative ring depends only on its derived endomorphism. It is cyclic and multiplicative under tensor; coherent cone additivity recovers the alternating formula.',
    'The acyclic-complex cancellation and homotopy argument are the proof mechanism; no additivity for an arbitrary morphism of distinguished triangles is imported.',
    'agrees','The existence reduction at 871 continues at 885. The notes correctly recognize an addressed proof sketch, not an unresolved existence conjecture.',ranges={132:(841,871),134:(885,885)})
add(26,[30],'idea of the earlier run',[132],'d’additivité ... mapping cylindre',
    'Arbitrary endomorphisms of an abstract distinguished triangle of perfect complexes need not satisfy trace additivity. Mapping-cone or filtered enhancements with compatible chain data supply the valid form.',
    'The stronger false assertion is a possible overreading, not the manuscript’s stated theorem. The dual-number counterexample is a modern scope check.',
    'agrees','The manuscript explicitly names a mapping cylinder at 853. The warning correctly avoids refuting this narrower assertion.',ranges={132:(851,869)})
add(27,[31],'unpursued implication',[134,136],'comme une “contraction” au sens tensoriel',
    'A perfect complex L over a commutative ring has perfect dual L^∨, the bidual map is an isomorphism, and RHom(L,M)=L^∨⊗^L M. For perfect L,M the two Hom complexes are dual, giving cyclic trace pairings.',
    'The modern categorical language “dualizable” summarizes this finite-projective calculation; the overwritten Hom arguments at 136 are not normalized.',
    'agrees','The duality identities are at 887–904 and the contraction/supertrace calculation at 915–947.',ranges={134:(887,904),136:(915,947)})
add(28,[32],'self-flagged step',[136,140,142],'il faut savoir ... de Tor-dim finie',
    'To trace RΓ(X,A), one needs its pseudo-coherence and finite Tor dimension. The following Rf_! bound supplies compact-support control and supplies ordinary control for proper f.',
    'A separate finite-cd constant-noetherian-coefficient theorem can also control ordinary RΓ; the draft’s Rf_! calculation alone does not settle every nonproper case.',
    'agrees','The manuscript labels pseudo-coherence as known at 953, then proves the compact-support estimate at 1113–1129.',ranges={136:(950,953),140:(1074,1077),142:(1113,1129)})
add(29,[33],'idea of the earlier run',[138,140],'pour tout pt géom',
    'A fixed Tor-amplitude interval can be checked on all geometric stalks. Merely having some finite interval at each point does not imply a uniform interval: on a disjoint union of points put A in cohomological degree −n on component n.',
    'The example is the earlier run’s and is not a refutation of the fixed-interval assertion. On a quasi-compact space, local uniform bounds on a finite cover give a global bound.',
    'agrees','The same endpoint symbols occur before and after “tout pt géom”; the notes retain that quantifier.',ranges={138:(991,1017),140:(1054,1072)})
add(30,[34],'unproved claim',[140,142],'Ici, il faut que l’Anneau de base soit de torsion',
    'If f is compactifiable with geometric fibres of dimension ≤d, the coefficient ring sheaf is torsion and L has Tor-amplitude [a,b], then Rf_!L has amplitude contained in [a,b+2d]. In homological notation this is [N−2d,M].',
    'The precise conversion a=−M,b=−N is ours. The ordinary tensor in the transcribed proof is not silently changed to derived tensor.',
    'agrees','The inserted torsion condition at 1074 and shift with deleted +2d at 1114 are essential; the proof invokes projection/Künneth.',ranges={140:(1074,1077),142:(1113,1129)})
add(31,[35],'reading question',[138,140,142],'notation homologique!',
    'The Tor interval argument requires consistent endpoints, a single input complex, and either flat representatives or a derived tensor in the proof. Several surviving letters and decorations are inconsistent.',
    'Stage 4 lists N′/M, F/L and tensor alternatives without changing them. The well-typed amplitude theorem is a reconstruction.',
    'agrees','The literal N/N′/M switches and ordinary tensor are visible at 996–998,1054–1058,1076 and1118.')
add(32,[36],'reading question',[144],'correspondances cohomologiques de degré $0$',
    'For the product correspondence and suitable exceptional adjunction/base change, Hom(pr₁^*F,pr₂^!G) identifies with Hom(Rf_!F,Rg_*G); these are degree-zero morphism groups.',
    'The first right-hand expression must be H⁰RΓRHom to have the same type. This missing H⁰ is proposed, not inserted.',
    'agrees','Lines 1181–1195 compare Hom⁰ groups, while 1181 equates one to a whole complex. The surrounding words force the type alarm.',ranges={144:(1173,1195)})
add(33,[37],'idea of the earlier run',[144,146],'si $S$ discret',
    'A finite-projective global trace pairing requires perfectness of the pushforward objects; finite Tor dimension alone is insufficient, as an infinite-rank free vector space has Tor dimension zero but no finite-matrix trace of its identity.',
    'The infinite-rank example is a scope test. Inherited constructibility/finiteness might supply the omitted condition, so this is not a declaration that the intended theorem is false.',
    'agrees','144 adds Tor dimension only, whereas146 states pseudo-coherence as well. The distinction is real.',ranges={144:(1197,1206),146:(1261,1283)})
add(34,[38],'withdrawn in the same text',[144,146],'Cet accouplement est induit ... de nature locale',
    'A paragraph proposing a local pairing is cancelled on144;146 restarts with the trace of a pseudo-coherent finite-Tor complex and the cyclicity pairings.',
    'This is an expository withdrawal and restart. It does not disprove local pairings or establish a properness-free Lefschetz theorem.',
    'agrees','Both the full deletion at1207–1214 and restart at1261–1295 are recorded.',ranges={144:(1207,1214),146:(1261,1295)})
add(35,[39],'unproved claim',[146],'\\operatorname{sym}',
    'For perfect L,M on a ringed topos, evaluation defines RHom(L,L)→A and composition followed by trace is cyclic with the Koszul symmetry in the derived tensor category.',
    'Finite local projective representatives justify the calculation; the typo in the second Hom factor is held separately in Stage4.',
    'agrees','The finite-Tor and pseudo-coherence assumptions, trace diagram and cyclicity formula all occur on146.',ranges={146:(1261,1295)})
add(36,[40],'idea of the earlier run',[146],'\\deleted{et borné}',
    'The finite sum of degreewise traces cannot be applied to an arbitrary unbounded degreewise finite-free representative, even one quasi-isomorphic to zero. Infinitely many contractible two-term summands give such a representative.',
    'The intrinsic trace of the derived perfect object remains zero; the issue is the unqualified infinite representative formula.',
    'agrees','The boundedness phrase is deleted within the insertion at1271. The notes correctly refuse to restore it from mathematics.',ranges={146:(1271,1277)})
add(37,[41],'reading question',[146],'(v,u)\\longmapsto uv',
    'To compose M→L with L→M into End(M), the second factor must be RHom(L,M), whereas the transcription reads RHom(L,L).',
    'This is a type-based alternative only.',
    'agrees','The mismatch is precisely the second display at1289, adjacent to the correctly typed first display.',ranges={146:(1285,1295)})
add(38,[43],'unpursued implication',[130,134,136,138,146],'pseudo-cohérent',
    'These sheets assemble the perfect-complex trace mechanism that is compared with SGA6 I §8 and SGA5’s published trace formalism.',
    'Alignment of mathematical objects does not date the manuscript or identify it with a particular published exposé. Illusie’s chronology further cautions against identifying undated drafts with oral-seminar content.',
    'agrees','The stages perfectness→dual→trace are on the cited sheets. The notes explicitly label SGA6 as a collation target.')
add(39,[44],'reading question',[99],'Theorem 4.6.6.',
    'The reused English source asserts an operator-algebra homomorphism H_x:G^p→H_x^p with kernel F_x^p and gives the integral symbol formula (4.6.7).',
    'Definitions of G^p and the analytic hypotheses lie outside the sheet; this is not attributed to Grothendieck and no exact modern theorem is invented.',
    'agrees','Printed page72 and the English analytical context are independent of the handwritten trace sequence.',ranges={99:(29,42)})
add(40,[45],'unproved claim',list(range(101,112,2)),'under what circumstances this number is an integer',
    'The reused source studies integrality of e(S/R)=e_S(mS)/e_R(m), and gives finite-flat-dimension, normality/simple residue-extension and decomposition criteria. A “local algebra” is a localization of a finite algebra.',
    'Each separate lemma is recorded in the claims map with its source convention. It is an internally partly answered question of a separate author.',
    'agrees','The convention at310–311 is decisive; the reversed-page order contains the answers as well as the opening question.')
add(41,[46],'idea of the earlier run',[109,111,130,132,134],'\\sum_i(-1)^i',
    'Both the multiplicity proof and the perfect-complex trace proof use finite alternating invariants. A K₀ interpretation of their relation is a proposed comparison, not an equality of these invariants.',
    'The comparison originates in the earlier run. No cross-reference between the reused typescript and the handwriting occurs.',
    'agrees','The finite-resolution calculations at208–224 and845–885 support the analogy but not a stronger identification.')
add(42,[47],'unproved claim',[107,113,115],'The following lemma is well-known',
    'The multiplicity associativity lemma and finite-algebra rank formula are cited dependencies; the ramification index’s integrality, detection of unramifiedness, tower formula and inseparable-residue correction are followed by a proof.',
    'The missing numbered bibliography is not reconstructed by matching topic alone. Modern comparators and exact source limits are separately recorded.',
    'agrees','107 cites [11],115 cites [12], whereas Theorem2.7 begins on115 and continues on113.')
add(43,[48],'reading question',[105,109,111,131,135,139,143],'lemma 4.5',
    'The reused algebra proof contains an incorrect-looking lemma number, Tor punctuation, a polynomial terminal index, a tangency premise, “basis of R”, and a missing exponent in the blowup-chart proof.',
    'The proposed corrections in Stage4 are mathematical alarms. None decides the ink or silently rewrites the source.',
    'agrees','Each anomaly was compared with its actual equation and adjacent proof, including the reversed printed order.')
add(44,[49],'unproved claim',[123],'Diviseurs relatifs',
    'For flat locally finitely presented X→S the source defines Div_{X/S}=R_{X/S}^*/O_X^*, embeds it in the absolute divisor sheaf, and claims compatibility of relative principal divisors and restriction.',
    'R_{X/S} is defined in the missing §10.1. Its exact denominator/transversality convention is not replaced by an arbitrary modern one.',
    'agrees','The quotient, inclusions and reference to §3.2 are explicit at726–755; only source-dependent reconstruction is warranted.')
add(45,[50],'unproved claim',[125],'If $K^*/V$ is tamely ramified',
    'The reused lemma asserts that a finite separable extension of the common function field, tame on a normal projective V, remains tame after a proper birational morphism V*→V of normal projective varieties over an algebraically closed field.',
    'The definition of tameness and referenced PartI lemmas are not supplied. A modern valuation-tame version is recorded as a sufficient comparison, not an exact identification.',
    'agrees','The proof is entirely by references; K* versus K′ is a genuine symbol alarm.',ranges={125:(781,783)})
add(46,[51],'reading question',[127,129],'a principal ideal domain',
    'The normalization of a one-dimensional noetherian local domain in its fraction field is a semilocal Dedekind domain and hence a PID; module finiteness is not required. If the original domain is complete, normalization is local.',
    'Noetherianity is the usual historical local-ring convention; the isolated sentence does not spell it out. “Only valuations” must mean nontrivial valuations centered at the maximal ideal.',
    'agrees','The original lemma and complete-case proof span129→127. The notes correctly avoid adding excellence or finite normalization.')
add(47,[52],'idea of the earlier run',[135],'then $R=k[[x_1,\\ldots,x_n]]$',
    'R=Q[x,y]_(x,y) is a two-dimensional equicharacteristic regular local ring with coefficient field Q and two parameters, but is not Q[[x,y]]. Completeness is a missing sufficient hypothesis in the isolated formulation.',
    'This refutes only the isolated wording if no earlier standing completeness convention applies. Countability distinguishes the rings.',
    'agrees','The parenthetical assertion at912 contains no completeness qualification on this sheet.',ranges={135:(912,912)})
add(48,[53],'idea of the earlier run',[135],'same characteristic so that $R$ has a coefficient field',
    'Q[x,y]_(x²−2,y) is regular local of dimension2, equicharacteristic0, and has residue field Q(√2), but no coefficient-field section because Q(x,y) contains no square root of2.',
    'This is a second independent conditional counterexample; completeness would give a coefficient field by Cohen’s theorem.',
    'agrees','The implication preceding the power-series parenthesis at912 requires its own qualification.',ranges={135:(912,912)})
add(49,[54],'unpursued implication',[139,141],'with respect to a maximal ideal',
    'An immediate quadratic transform of a regular local domain (R,m), dim n>1, is R[m/x] localized at a maximal ideal containing x, with x∈m\\m². The chart-changing lemma preserves this local ring and its dimension n.',
    'The maximal-centre convention excludes arbitrary nonclosed points of the exceptional divisor from this same dimension assertion.',
    'agrees','The maximal condition is explicit at1097–1104 and used at1042–1045.')
add(50,[55],'unpursued implication',[141,143],'there exists a generator $g$ of $G$',
    'Every specified generator of a finite cyclic quotient H of a finite cyclic group G lifts to a generator of G.',
    'This is an elementary finite-group statement. No consequence for the named profinite torsion or centralizer problems is asserted.',
    'agrees','The exponent construction begins at1158 and is completed on the earlier scan141; it checks by coprimality.')
add(51,[56],'idea of the earlier run',[145],'Il revient au même de dire que $m_y=m_xO_y$',
    'Finite separable residue-field extensions alone, even with flatness and local finite presentation, do not characterize étaleness. Spec(k[ε]/ε²)→Spec k satisfies those three literal conditions but is not étale; its fibre is nonreduced and m_y≠m_xO_y.',
    'The stronger criterion printed immediately afterward, including maximal-ideal equality, is the valid one. This is a scope/refinement check, not a refutation of étale theory.',
    'agrees','The counterexample checks every literal hypothesis at1243–1249 and distinguishes1251–1252.',ranges={145:(1240,1252)})
add(52,[57],'unproved claim',[145],'La démonstration ... sera donnée dans un instant',
    'The axiomatic small étale-topos source refers to a promised theorem/proof outside this sheet and states that an étale radicial morphism is exactly an open immersion.',
    'The adjacent package supplies more of this Roos-related source family. Its axioms must be read there; this isolated promise is not a conjecture of the handwriting.',
    'understates','The original note correctly described its package’s gap, but the current attachment also supplies neighboring source-family sheets in cote33. The single-page limitation is now local rather than corpus-wide.','corrected')
add(53,[58],'idea of the earlier run',list(range(101,122,2))+list(range(125,144,2)),'No identification of author in these surviving typescript passages.',
    'Auslander–Rim (1963) and Abhyankar (1960, PartII) are proposed source-identification leads. The embedded S01–S15 table repeats already covered authorial flags and adds no independent manuscript claim.',
    'Metadata verification alone cannot settle textual identity. Each repeated self-flagged step is represented in the substantive item/problem records rather than counted again.',
    'agrees','Read the full entry including the following S-table. Its candidate attribution is expressly low confidence; the claims map preserves that limit.')
add(54,[59,60],'title, date or page count',list(range(98,147)),'\\mspage{97} ... \\mspage{145}',
    'The package has49 transcribed scans, alternating25 handwritten subject pages and24 reused typed pages. Small foliation runs97–145; printed page19 at125 is not a total length.',
    'These are transcription/source-accounting observations, not a new inspection of the absent scans. No handwriting attribution for the foliation is supplied.',
    'agrees','All49 scan markers and foliation endpoints were counted/read; no cover or explicit authorial total is transcribed.')
add(55,[61],'title, date or page count',[100,108,122],'Formulaire faisant intervenir',
    'Circled26 heads the derived-tensor/D^- Formulaire; circled1,2,3 divide ringed-topos generalities, Künneth and the application/foundation program.',
    'Numbers identify sections, not page totals. Uncertain intervening wording at108 remains uncertain.',
    'agrees','Headings and markers are visible at46–49,200 and701.')
add(56,[62],'title, date or page count',[124],'Généralités sur Lefschetz',
    'Circled30 introduces Lefschetz–Verdier preliminaries; the heading replaces a deleted Künneth by Lefschetz.',
    'This is a running heading, not a separate title sheet or total.',
    'agrees','Lines758–761 preserve the heading and deletion.',ranges={124:(758,761)})
add(57,[63],'title, date or page count',[138],'Complexes de Tor-dimension finie sur un préschéma',
    'Circled31 heads the Tor section; the preceding margin refers back to30 and partial traces.',
    'The back-reference is to the preceding section, not a total or independent manuscript.',
    'agrees','The margin and title are explicitly transcribed at987–989.',ranges={138:(987,989)})
add(58,[64],'title, date or page count',[144,146],'Formule de Lefschetz-Verdier.',
    'Circled32 and letters a,b organize the Lefschetz–Verdier section, which continues beyond146.',
    'The neighboring package’s148 supplies letterc and further continuation; no completion statement is inferred from146.',
    'agrees','Both headings and the final cyclicity equality were read.')
add(59,[65],'title, date or page count',list(range(101,122,2)),'3. Decomposition of Ramification Index',
    'The reused ramification source is in reverse printed order:3.6→3.1 then2.5→2.1 as scan numbers increase.',
    'Read proofs in source order for mathematics, retain scan order for archival locators. These labels are not total page counts.',
    'agrees','Each of the11 printed section/page identifiers was checked.')
add(60,[66],'title, date or page count',[99,123,125,127,129,131,133,135,137,139,141,143,145],'11. Diviseurs relatifs.',
    'Other reused identifiers are operator page72, relative-divisor §11, algebra pages19,18,17,16,15,14,13,22,21,20, and étale-topos page12.',
    'Numerical adjacency does not identify authorship or a shared source; no explicit total is present.',
    'agrees','The entire listed sequence was read against scan markers and printed headings.')
add(61,[67,68,69],'other',[100,110,118,130,142,145],'No additional manuscript statement: bibliography and comparison table.',
    'The earlier run’s bibliography and Stacks table supply candidate exact comparison locators; they do not certify references for this run.',
    'All references used in the present dossier are independently opened or explicitly marked unverified. Source identity leads remain distinct from theorem matches.',
    'agrees','Read every comparison/bibliography row; repeated theorem leads map to existing items and claims rather than adding duplicate mathematics.')

(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
with (OUT/'entries.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
assert len(entries)==70 and len({e['entry_id'] for e in entries})==70
(OUT/'reading_log.tsv').write_text('reviewer\tpackage\tentries_read\ttranscription_lines_read\tdoubts_read\tmethod\nroot\t'+P+'\t1–70\t1–1297 (full; truncated display gaps reread)\t1–320 plus transcription uncertainties\tSemantic comparison of full entries with full passages; source-reading outputs retained\n')
print(json.dumps({'package':P,'entries':len(entries),'items':len(items),'verdicts':{v:sum(e['verdict']==v for e in entries) for v in sorted({e['verdict'] for e in entries})}},indent=2))
