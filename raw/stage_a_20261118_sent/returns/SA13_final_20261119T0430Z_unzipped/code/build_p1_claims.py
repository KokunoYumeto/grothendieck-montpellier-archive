"""Manually authored claims, following complete reading of MPL_33_098-146.

The helper only serializes decisions; it does not infer verdicts or mathematical fates.
"""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable/shards/p1'
F='pro/MPL_33_098-146_transcription.tex'
pages={int(x['scan']):x for x in json.loads((ROOT/'work/pages.json').read_text()) if x['file']==F}
claims=[]
def C(n,items,scans,his,statement,status,cls,fate,refs,search,proof=None,confidence='high',date='Publication date is specified by the cited edition; first circulation not established.',authorship='Grothendieck handwritten working text',ranges=None):
    loc=[]
    for s in scans:
        p=pages[s];a,b=(ranges or {}).get(s,(p['start'],p['end']))
        loc.append(dict(file=F,cote=33,scan=s,start=a,end=b))
    computation={'kind':'No separate numerical computation; conceptual construction/proof obligation.',
                 'review':'The page argument and the exact scope of the cited result were compared.'}
    if proof:
        computation={'kind':'Symbolic argument and, where applicable, exact finite consistency calculation',
                     'proof':f'shards/p1/proofs.md#{proof}',
                     'code':'code/p1_compute.py','output':'outputs/p1_computations.json',
                     'scope':'The written proof supplies universal quantifiers; finite enumerations do not.'}
    claims.append(dict(id=f'C-SA13-{n:03}',items=[f'SA13-{i}' for i in items],cote=[33],scans=[f'33:{s:03}' for s in scans],lines=loc,his_statement=his,statement=statement,status_on_pages=status,computation=computation,**{'class':cls},fate=fate,fate_date=date,present_status='As of 2026-11-19: '+fate,refs=refs,confidence=confidence,search_ids=[search],source_authorship=authorship))

C(1,[2],[98],'D “échange” les foncteurs; immersion calculation preceding the slogan.',
  'Under bounded constructible torsion hypotheses admitting dualizing complexes, D_Y Rf_! ≅ Rf_*D_X and D_X Lf^* ≅ f^!D_Y; the other exchanges use biduality. This is a sufficient modern reconstruction, not all the hypotheses written on this continuation leaf.',
  'proof sketched','A','The published duality program is in SGA5 I; the relative formulation and dualizability criterion have later precise extensions. The fragment alone does not specify a universal six-functor theorem.',
  ['SGA5I','LuZheng2022','IllusieChronology2026'],'P1-S01',confidence='medium',date='SGA5 oral 1965–1966; final publication 1977. Lu–Zheng first arXiv 2020-05-18, publication 2022.')
C(2,[3],[100],'F plat ssi ... Hom(F,I) injectif pour tout I injectif.',
  'For modules on a commutative ringed topos, F is flat iff internal Hom(F,I) is injective for every injective I. Tensor–Hom adjunction and injective cogeneration prove both implications.',
  'stated without proof','A','The flat-resolution formalism appears in SGA4 XVII §4.1; the equivalence is independently checked here with the stated module-category hypotheses.',
  ['SGA4XVII'],'P1-S02','flat-adjunction',date='SGA4 XVII drafted 1968–1969 from 1964 lectures; published 1973.')
C(3,[3],[100,102],'Tout Module ... est quotient d’un plat; ... à degrés bornés supérieurement.',
  'Every module on a ringed topos is a quotient of a flat module. Bounded-above complexes admit bounded-above flat resolutions; these compute derived tensor on D^-.',
  'proof sketched','A','SGA4 XVII §4.1 supplies the derived tensor formalism. The modern K-flat treatment also allows unbounded complexes.',
  ['SGA4XVII','Stacks06YV'],'P1-S02','flat-adjunction',date='1973; no first circulation of this specific sheet established.')
C(4,[3,5],[102,104],'Associativité; commutativité ...; suite exacte; RHom(L⊗L′,M).',
  'Derived tensor is exact in each variable, associative and symmetric with Koszul sign (−1)^{ij}; it satisfies derived tensor–Hom adjunction in compatible boundedness ranges. A short exact sequence of inputs produces the usual distinguished triangle and long exact hyper-Tor sequence.',
  'stated without proof','A','The published construction is SGA4 XVII §4.1. Its signs are those of total complexes, checked algebraically here.',
  ['SGA4XVII','Stacks0FPP'],'P1-S02','graded-traces')
C(5,[4],[102,104,106],'f non nécessairement plat ... L(gf)^*=Lf^*Lg^*.',
  'For a morphism of ringed topoi, inverse image takes flat modules to flat modules. The derived pullback is monoidal and composition-compatible; no flatness of the morphism is required.',
  'open on the pages','B','The general construction and composition/tensor identifications are in Stacks §21.18. The marginal question has an affirmative answer.',
  ['Stacks06YV'],'P1-S02','flat-adjunction',date='Modern checked formulation accessed 2026-11-19; first circulation of the general result not determined.')
C(6,[5],[104],'Γ_X est de dim ... finie !',
  'If Γ has cohomological dimension ≤c, RΓ sends a complex bounded above by b to one bounded above by b+c. This allows the draft’s global hyper-Tor formalism on D^-; it is not a claim that unbounded derived RΓ fails to exist otherwise.',
  'stated without proof','A','The boundedness argument is the finite-column hypercohomology spectral sequence; compare SGA4 XVII §4.2.',
  ['SGA4XVII'],'P1-S02','amplitudes')
C(7,[5,6],[104,106],'RHom; Hom_D ... = H^0(RHom ...).',
  'For a bounded-above first input and bounded-below second input, an injective resolution of the second computes derived internal Hom; derived global Hom has H^0 equal to Hom in D. Modern K-injective resolutions give wider ranges.',
  'proof sketched','A','The bounded constructions agree with SGA4 XVII §4.2; the identification of morphisms uses H^0, which must not be omitted in scan144.',
  ['SGA4XVII','Stacks0FPP'],'P1-S02')
C(8,[6],[106],'Attention, ... f est plat; Lf^* ... adjoint ... Rf_*.',
  'Lf^* ⊣ Rf_* for ringed topoi. Under compatible ranges, Rf_* RHom_X(Lf^*L,K) ≅ RHom_Y(L,Rf_*K). Direct image preserves injectives by this elementary argument only when underived f^* is exact.',
  'corrected by himself later','B','The result survives the correction; the unrestricted injective-preservation argument does not. Stacks §21.18 uses the appropriate derived resolutions.',
  ['Stacks06YV'],'P1-S02','flat-adjunction',ranges={106:(143,177)})
C(9,[8],[110],'C’est peut-être vrai dès que Y est noethérien.',
  'The question is finite relative étale cohomological dimension of finite-type f with merely noetherian target, for the torsion coefficients under discussion. Finite-type schemes over a field are a proved subcase; finite-dimensional noetherian target and invertible ℓ are another. No assertion about absolute cd of an arbitrary ground field is inferred.',
  'open on the pages','C','The checked results cover the two stated subcases (Stacks59.96.2; Gabber–Illusie XVIII_A1.4). Merely noetherian targets without dimension or coefficient restrictions were not matched to a complete theorem in this search.',
  ['Stacks0F10','GabberIllusie2014'],'P1-S03',confidence='medium',date='2014 publication; an alternative Gabber argument is documented in an email of 2007-08-15, not asserted to be first circulation.')
C(10,[7],[108,112],'Tor ou Ext non bornés, même si X est un point géométrique.',
  'For A=Z/ℓ² and k=A/(ℓ), Tor_i^A(k,k)=Ext_A^i(k,k)=k for all i≥0. Thus finite coefficients do not imply finite homological dimension. Squarefree n is excluded from this witness since Z/n is then a product of fields.',
  'stated without proof','E','The obstruction is standard homological algebra; the earlier run’s periodic-resolution witness is verified directly. It is not a new open problem.',
  ['Stacks0656'],'P1-S04','periodic-tor',authorship='Manuscript warning; explicit example belongs to the earlier run')
C(11,[17],[112,120],'M à cohomologie localement constante, de t.f.; restriction ... inutile si f qu.cpt qu.sép.',
  'Ordinary projection holds for a perfect target complex on any ringed topos. The draft also proposes locally constant finite-type cohomology under finite relative cd; constant noetherian coefficients permit the bounded-above finite-free/way-out argument. The non-finite-type qcqs extension requires its colimit hypotheses to be supplied.',
  'proof sketched','C','The perfect case is Stacks21.50.1; SGA4 XVII5.2.11–12 verifies the constant-coefficient finite-cd mechanism. The unfinished “où” paragraph does not establish every broader range.',
  ['Stacks0944','SGA4XVII'],'P1-S05',confidence='medium')
C(12,[9,10],[112,114,116],'un isom. canonique bifonctoriel; Il faut vérifier ... fonctoriel.',
  'For compactifiable f and torsion coefficients, Rf_!L⊗^L M → Rf_!(L⊗^L f^*M) is an isomorphism in the bounded ranges written in the draft. Construction, naturality and independence from chosen resolutions are separate obligations.',
  'proof sketched','A','Exact published match: SGA4 XVII5.2.9. The missing pullbacks in the transcription are reading alarms, not altered text.',
  ['SGA4XVII'],'P1-S05',date='Published 1973; chapter drafted 1968–1969.')
C(13,[11],[116],'S’obtient en appliquant 2 fois la formule de projection.',
  'For compactifiable X→S and Y→S, torsion coefficient ring, and bounded-above L,M, Rh_!(pr_X^*L⊗^Lpr_Y^*M) ≅ Rf_!L⊗^LRg_!M, where h:X×_S Y→S. Base-change and coherence hypotheses are those of the compact-support formalism.',
  'proof sketched','A','Exact published match: SGA4 XVII5.4.3. Its two auxiliary compatibility verifications are admitted in the published exposition, not independently proved in this review.',
  ['SGA4XVII'],'P1-S05')
C(14,[11],[116],'F ou G plat ... R_!^if(F) ou R_!^jg(G) plats.',
  'In the sheaf specialization of C-SA13-013, one flat input ensures the underived external product computes the derived one, and flatness of one family of compact-support cohomology sheaves kills higher Tor in the Künneth spectral sequence.',
  'stated without proof','A','This is the flat-input/flat-output corollary of the checked derived Künneth formula, not a general direct-sum formula over Z/n.',
  ['SGA4XVII'],'P1-S05','amplitudes')
C(15,[12],[118,120],'si X ou Y propre ... sans hyp n premier à la car.',
  'Over a separably closed k, ordinary derived Künneth holds for finite-type X,Y and Z/n-complexes if one factor is proper, with no invertibility condition on n. The draft proves its bounded version; the cited modern result handles unbounded complexes in the finite-type setting.',
  'proof sketched','B','Exact modern match: Stacks59.97.2. The page’s separation from the duality proof is mathematically justified.',
  ['Stacks0F14'],'P1-S06')
C(16,[13],[118],'je pense qu’on doit encore avoir la formule ... n premier à la caractéristique.',
  'For finite-type X,Y over a separably closed field and n invertible in k, ordinary derived Künneth holds for Z/n-complexes with neither factor assumed proper.',
  'open on the pages','B','The conjectured formula is established in the precise form Stacks59.97.9. This check does not settle the conditional priority attribution to Verdier at scan120.',
  ['Stacks0F1P'],'P1-S06',date='Modern exact statement checked; first circulation/priority not established by the sources opened.')
C(17,[14],[118],'on n’a pas ... bon Künneth ... Z/pZ ... même pour H¹ [uncertain].',
  'For k algebraically closed of characteristic p, the class of xy in H¹_et(A²_k,F_p)=k[x,y]/(F−1) is not a sum of pullbacks of classes in H¹_et(A¹_k,F_p). Hence ordinary Künneth fails already in degree1.',
  'stated without proof','E','Artin–Schreier exactness gives a complete counterexample to unrestricted ordinary Künneth. The mixed-monomial proof below settles the mathematical example, not the uncertain ink reading.',
  ['Stacks0A3J'],'P1-S06','artin-schreier',authorship='Failure asserted by Grothendieck; explicit xy example supplied by the earlier run')
C(18,[16],[120],'la formule de projection n’est plus exacte ... Rf_*.',
  'For j:G_m→A¹ over an algebraically closed field, take Λ a finite field and M=j_!Λ. At the origin (Rj_*Λ)⊗^L M has zero stalk, whereas Rj_*(j^*M) has nonzero H⁰ stalk. Thus ordinary projection without a target hypothesis is false.',
  'proof sketched','E','The source’s support obstruction is valid; C-SA13-011 records the refined positive hypotheses. The counterexample checks all inputs and the boundary stalk.',
  ['Stacks0944'],'P1-S05','ordinary-projection',authorship='Manuscript support argument; explicit j supplied by the earlier run')
C(19,[18],[122,126],'traiter ... coefficients non cts sur une courbe ... termes locaux.',
  'For a proper smooth curve over an algebraically closed field, constructible ℓ-adic coefficients and an endomorphism with isolated suitably nondegenerate fixed points, a Lefschetz formula expresses the cohomological trace as a sum of local terms. A singular-coefficient formulation requires the actual local terms, not just stalk traces in all situations.',
  'open on the pages','A','Bourbaki279 announces the curve reduction and local formula; SGA5 III,III B,XII develop the terms. Illusie’s chronology documents the later compatibility work and distinguishes it from the earlier curve proof.',
  ['GrothendieckBourbaki279','SGA5III','SGA5','IllusieChronology2026'],'P1-S07',confidence='medium',date='Bourbaki talk December1964; collected publication1966. SGA5 final1977; compatibility proof spring1975.')
C(20,[18],[122,126,128],'rationalité des fonctions L; passage ... limite projective.',
  'For finite-type X/F_q and constructible Q_ℓ-sheaf F, ℓ≠char(F_q), the Euler product L(X,F,t) equals ∏_i det(1−tFr|H_c^i(X_bar,F))^{(−1)^{i+1}}, hence is rational over the coefficient field. Integrality and independence assertions require their separate hypotheses.',
  'open on the pages','A','Exact historical theorem: Bourbaki279 §5.1, with reduction to smooth projective curves in §§5.3–5.6. The determinant identity is a formal consequence of the trace identities.',
  ['GrothendieckBourbaki279'],'P1-S07','determinant-series',date='Talk December1964; collected volume1966. No earlier date inferred from the manuscript.')
C(21,[20],[124],'nombre des points fixes ... avec grain de sel.',
  'The Lefschetz number is a sum of local indices under appropriate compactness, finiteness and isolated fixed-point hypotheses. Replacing the indices by the bare number of fixed points is valid only when each local contribution is1.',
  'stated without proof','E','The qualification on the page is substantive. The cohomological correspondence version is developed in SGA5 III; current relative hypotheses are in Lu–Zheng.',
  ['SGA5III','LuZheng2022'],'P1-S07')
C(22,[23,24],[130],'pseudo-cohérents de Tor-dimension finie ... projectifs de type fini ... bornés.',
  'For a commutative ring A, a pseudo-coherent complex with finite Tor amplitude is perfect: it is quasi-isomorphic to a bounded complex of finite projective A-modules. For noetherian A, bounded-above pseudo-coherence means finite cohomology modules.',
  'stated without proof','A','The manuscript matches the perfect-complex framework of SGA5 VIII and SGA6; exact modern criterion checked in Stacks15.76.2.',
  ['SGA5VIII','Stacks0656'],'P1-S04','perfectness',date='SGA5 published1977; no date of first use of “perfect” inferred from these leaves.')
C(23,[24],[130],'ces conditions ... stables par mapping cylindre et par ⊗^L.',
  'Pseudo-coherent complexes and finite-Tor-amplitude complexes are each stable under shifts, cones and derived tensor (with compatible coefficient ring); their intersection is the thick tensor category of perfect complexes.',
  'stated without proof','A','Bounded finite-projective models verify the perfect part; Stacks15.76 and21.47 give the exact criterion and local version.',
  ['Stacks0656','Stacks08G8'],'P1-S04','perfectness')
C(24,[25],[132,134],'Tr_*u=Σ(−1)^iTr u_i ... stable par isomorphismes.',
  'For a perfect A-complex and its derived endomorphism, the supertrace on any bounded finite-projective model is well-defined, homotopy invariant and independent of the model. An acyclic bounded projective complex is split contractible, so its supertrace vanishes.',
  'proof sketched','A','The later page answers the existence obligation of scan132. Stacks64.10.2 provides a checked modern proof; this run redoes the cancellation argument.',
  ['Stacks03TI'],'P1-S04','graded-traces')
C(25,[26],[132,134],'additivité pour un mapping cylindre.',
  'For a strictly compatible endomorphism of a chain-map cone, supertrace(Cone(f))=supertrace(target)−supertrace(source). Equivalently, a degreewise exact sequence with compatible endomorphisms has additive trace.',
  'proof sketched','A','The strict cone assertion is correct. It must be kept distinct from C-SA13-026, the stronger assertion about an arbitrary endomorphism of an abstract distinguished triangle.',
  ['Stacks03TI','Stacks087J','IllusieChronology2026'],'P1-S04','graded-traces')
C(26,[26],[132],'Earlier-note extension: additivity for every endomorphism of a distinguished triangle.',
  'That extension is false even for perfect complexes over Q[ε]/ε². For A=R in degree1, B=[R --ε→ R] in degrees0,1, C=R in degree0, the endomorphisms (1+ε,1,1) form an endomorphism of the associated triangle but trA+trC−trB=−ε.',
  'false as stated','B','The counterexample is checked from Stacks110.65, including the connecting morphism. Refined statement: C-SA13-025. Illusie documents Ferrand’s1968 discovery and the filtered-category repair.',
  ['Stacks087J','IllusieChronology2026'],'P1-S04','triangle-counterexample',authorship='Claim of the earlier run, not an unrestricted assertion on the manuscript',date='Ferrand counterexample1968 as reported by Illusie; filtered repair discussed1974; publicationSGA5,1977.')
C(27,[25,27],[132,136],'Tr uv=Tr vu; Tr(u⊗^Lv)=Tr(u)Tr(v).',
  'Degree-zero endomorphisms of perfect complexes have cyclic trace, and trace is multiplicative under derived tensor. The graded analogue includes the Koszul sign; no ungraded cyclic rule is claimed for arbitrary degree morphisms.',
  'stated without proof','A','Finite-projective matrix identities prove the formulas; the categorical realization is the dual/contraction construction.',
  ['Stacks03TI','Stacks0FPP'],'P1-S04','graded-traces')
C(28,[27],[134],'L→L^{∨∨}; (L⊗L′)^∨; RHom(L,M)=L^∨⊗M.',
  'For perfect L, the dual RHom(L,A) is perfect, biduality is an isomorphism, and RHom(L,M)≅L^∨⊗^LM for arbitrary M. Tensor duality for two perfect factors follows with the symmetric monoidal constraint.',
  'stated without proof','A','Exact modern dualizability statements: Stacks21.48.4. Finite-projective evaluation verifies the sheet’s formulas.',
  ['Stacks0FPP'],'P1-S04','graded-traces')
C(29,[27],[136],'RHom(M,L) et RHom(L,M) sont “duals” ... <u,v>.',
  'For perfect L,M, RHom(L,M) and RHom(M,L) are dual complexes via composition and trace. On degree-zero maps the pairing is tr(vu)=tr(uv). The expression at line932 must be membership in A, not equality to the set H⁰(A).',
  'proof sketched','A','The formula follows from the checked dual identification and rectangular-matrix cyclicity; the two notation alarms remain for scan review.',
  ['Stacks0FPP','Stacks03TI'],'P1-S04','graded-traces')
C(30,[21,22],[126,128,132,146],'conséquence formelle, par passage à la limite ... Z/ℓ^ν.',
  'A compatible perfect Z_ℓ-complex and endomorphism reduce to compatible finite-level supertraces, and the inverse-limit trace equals their compatible system; after tensoring with Q_ℓ it is the usual alternating trace. Mere finite-dimensional cohomology at every finite level is not sufficient data for this inference.',
  'open on the pages','A','The perfect-model comparison is immediate by reducing matrices; SGA5 V–VI is the published adic framework. This run does not identify an unrestricted derived inverse-limit theorem in the brief hope.',
  ['SGA5','Stacks03TI'],'P1-S07','adic-trace',confidence='medium')
C(31,[29],[138,140],'pour tout pt géom ... bornée par [N,M].',
  'On an étale ringed topos with enough points, a fixed Tor-amplitude interval holds iff it holds at every geometric stalk. “Each stalk has some finite interval” is weaker if no uniform interval is given.',
  'stated without proof','A','The fixed-interval assertion is a stalkwise test. The earlier run’s disjoint-union example separates it from nonuniform local finiteness.',
  ['Stacks08G8'],'P1-S04','amplitudes')
C(32,[30,31],[138,140],'[N+N′,M+M′]; Lf^* ... itou.',
  'Tor amplitudes add under derived tensor and are preserved by derived pullback of a complex with finite Tor amplitude. Cohomological interval [a,b] corresponds to homological interval [−b,−a]; the repeated endpoint letters in the transcription need checking.',
  'proof sketched','A','Tensoring bounded flat representatives proves the bounds; Stacks15.76.2 and21.18 provide the precise modern framework.',
  ['Stacks0656','Stacks06YV'],'P1-S04','amplitudes')
C(33,[31],[140],'∃ L′ ... plat ... L′_i=0 si i∉[N,N′].',
  'A complex with finite Tor amplitude [a,b] admits a flat representative supported in that interval; bounded cohomology alone admits a representative in the interval without guaranteeing flat terms. In the pseudo-coherent ring case the flat replacement may be chosen finite projective.',
  'stated without proof','A','The distinction on the page is correct; the perfect finite-projective version is Stacks15.76.2. Flat truncation uses the vanishing of the last Tor obstruction.',
  ['Stacks0656'],'P1-S04','perfectness')
C(34,[30],[140,142],'Anneau ... de torsion; [N−2d,M] (notation homologique!).',
  'For compactifiable f with fibres of dimension≤d, torsion coefficients and K of cohomological Tor amplitude[a,b], Rf_!K has Tor amplitude[a,b+2d]. In the page’s homological indexing this is[N−2d,M]. No prime-to-characteristic restriction is needed for this compact-support bound.',
  'proof sketched','A','The exact input results are SGA4 XVII5.2.8.1,5.2.9 and5.2.10. The full interval follows by combining projection with relative cd≤2d.',
  ['SGA4XVII'],'P1-S05','amplitudes')
C(35,[28,33],[136,140,142,144],'RΓ_X(A_X) ... ps. coh. et ... Tor-dim finie.',
  'For a compactifiable finite-type X over separably closed k and A a noetherian torsion coefficient ring, a bounded constructible complex of finite Tor amplitude has perfect compact-support cohomology. For proper X this is ordinary cohomology. Ordinary cohomology in greater generality needs separate finite-cd and finiteness assumptions.',
  'open on the pages','A','SGA4 XVII5.3.6–8 supply finiteness and5.2.10 supplies Tor control; combine with C-SA13-022. The draft develops the needed compact-support step at140–142.',
  ['SGA4XVII','Stacks0656'],'P1-S05','perfectness')
C(36,[32],[144],'Hom^0(F,G)=RΓ(RHom(F,G)); Hom^0_{X×Y}(...)=Hom^0(Rf_!F,Rg_*G).',
  'Read degree-zero derived Hom as H⁰RΓRHom. With constructibility, duality and the relevant adjunction/base-change hypotheses, product-space cohomological correspondences induce maps Rf_!F→Rg_*G. This fragment is not a universal equivalence for arbitrary sheaves and schemes.',
  'stated without proof','C','SGA5 III and Lu–Zheng formalize correspondences with explicit properness/dualizability. The missing H⁰ is a type error if read literally; no broader formula is silently supplied.',
  ['SGA5III','LuZheng2022'],'P1-S01',confidence='medium')
C(37,[33,34],[144],'F Tor-dim finie, non nécessairement ps. coh.; local pairing deleted.',
  'If proper pushforward is perfect, the induced endomorphism has a scalar trace. A sheaf complex of finite Tor dimension alone need not have perfect global cohomology: on a point an infinite free module has Tor dimension0 but no finite-projective scalar trace of the identity.',
  'corrected by himself later','C','The local construction is crossed out at144 and restarted at146 using finite-projective models. C-SA13-035 and038 are the precise positive forms; Lu–Zheng2.16 identifies the relative dualizability requirement.',
  ['Stacks0656','LuZheng2022'],'P1-S01','trace-finiteness',confidence='high')
C(38,[35,37],[146],'trace ... localement projectif de type fini; Σ(−1)^i Tr u_i.',
  'A locally perfect complex on a ringed space has an intrinsic internal trace RHom(L,L)→O. Composition produces the local pairing RHom(M,L)⊗RHom(L,M)→O. The second factor printed RHom(L,L) does not type-check for L≠M.',
  'proof sketched','A','The construction is the local finite-projective evaluation trace, glued by invariance; Stacks21.48.4 supplies the dualizable-object formulation.',
  ['Stacks0FPP'],'P1-S04','graded-traces')
C(39,[36],[146],'“et borné” is deleted next to the finite-projective model.',
  'The finite alternating sum formula requires a bounded finite-projective model, or an explicitly justified replacement. A degreewise finite-free unbounded contractible complex already has no intrinsically defined infinite alternating sum of identity traces.',
  'corrected by himself later','B','The deletion is an editorial change whose mathematical intent remains ambiguous. Intrinsic trace survives for a perfect object even with an unbounded representative; only the literal infinite termwise summation rule fails. The contractible example refutes that interpretation, not the deletion itself. The precise trace statement is C-SA13-024/038.',
  ['Stacks03TI','Stacks0656'],'P1-S04','trace-finiteness',authorship='Mathematical consequence of a deleted qualification; intent remains an ink question')

# Typed reused leaves follow. Authorship must not be inferred from their archival location.
T='Typed reused source; individual authorship not established from the supplied leaf'
C(40,[39],[99],'Theorem4.6.6: H_x^p is an algebra ... kernel F_x^p.',
  'The displayed leading-homogeneous-part map from an algebra of operators to its model operators is asserted multiplicative with the specified kernel. The definitions of G^p, the operators J, their allowed kernels and composition are absent, so a precise theorem cannot be uniquely recovered.',
  'stated without proof','F','Exact-number, exact-phrase and author-family searches did not identify the source. Singular-integral symbol calculus is a subject lead, not a checked identification or a theorem-level match.',
  [],'P1-S08',confidence='low',authorship=T)
C(41,[39],[99],'S_x^p ... matrices ... (4.6.7) ξ(x)+∫ e^{iu·v}F_x(v)/||v||^m dV_v.',
  'The inner product identifies A_x^p⊗A_x^p with End(A_x^p), giving the algebra of binomial(m,p)-square smooth matrix functions. The proposed Fourier-integral symbol additionally needs the missing regularization, homogeneity and cancellation hypotheses; an ordinary integral is not justified by this leaf.',
  'stated without proof','F','The finite-dimensional matrix identification is elementary; the exact analytic construction remains unidentified after the same searches as C-SA13-040.',
  [],'P1-S08',confidence='low',authorship=T)
C(42,[40],[111,119,121],'e(S/R)=e_S(mS)/e_R(m); S=A_p for a finite R-algebra A.',
  'Here “local R-algebra” means localization of a finite R-algebra at a maximal ideal, not an arbitrary local finite-type algebra. Write S^e=S⊗_R S and S^f for its localization at the inverse image of m_S under multiplication. The text uses r(S/R)=e(S^f/S). The first definition section is absent; no more general scope is inferred.',
  'stated without proof','F','The mathematical conventions can largely be reconstructed from111,119,121. Auslander–Rim1963 is a real bibliographic candidate, supported by contemporary Williamson references, but the original article could not be collated; this is not a secure attribution.',
  ['AuslanderRim1963','Williamson1963'],'P1-S09',confidence='medium',authorship=T)
C(43,[40,42],[121],'Lemma2.1: T_R^f→T_S^f is an isomorphism if S/R unramified.',
  'For local finite R-algebras in C-SA13-042, unramified S/R makes the localized diagonal algebra T_R^f canonically isomorphic to T_S^f; in particular S_R^f≅S. The proof uses splitting of the multiplication epimorphism and the absence of nontrivial idempotents in a local ring.',
  'proved there','F','The page proof is valid with the stated finite-algebra convention. The missing introductory hypotheses and unavailable exact Auslander–Rim text prevent a complete historical identification; ordinary étale-diagonal statements are only comparisons.',
  ['AuslanderRim1963','Stacks025G'],'P1-S09','ramification',confidence='medium',authorship=T)
C(44,[40,42],[121,119],'Lemma2.2: completed S^f ≈ completed-S^f.',
  'For a noetherian local finite algebra, completing the diagonal-localized tensor algebra commutes with completing R and S, with the diagonal maximal ideal and the induced adic topology understood.',
  'proved there','F','The quotient-by-powers argument is checked on the pages. The exact reused-source identity remains unverified; general noetherian completion facts were checked independently in Stacks10.97.',
  ['AuslanderRim1963','Stacks00MC'],'P1-S09','ramification',confidence='medium',authorship=T)
C(45,[40,42],[119],'Lemma2.3: e_{S/R}(q)=length_S(S/mS), S flat.',
  'For a flat local finite algebra over a noetherian local ring and an ideal of definition q, the multiplicity ratio is length_S(S/m_RS). If it is also unramified the ratio is1. Tensoring a composition series gives the equality of length polynomials before leading coefficients are taken.',
  'proved there','E','This is a classical flat length/multiplicity calculation, re-proved here; the exact candidate source is not asserted identified. Stacks43.15 records the modern multiplicity conventions.',
  ['Stacks0AZU','AuslanderRim1963'],'P1-S09','multiplicity',authorship=T)
C(46,[40,42],[119,117],'Proposition2.4 a),b),c): unramified invariance and completion.',
  'For the diagonal index r: if S/R is unramified, r(S/R)=1 and r(T/R)=r(T/S); if T/S is flat and unramified, r(T/R)=r(S/R); and r(S/R)=r(S_hat/R_hat). These use the local-finite-algebra convention and the preceding diagonal/completion lemmas.',
  'proved there','F','The chain of equalities is present and type-checked. Its complete original publication context remains unverified, rather than being labelled an open Grothendieck problem.',
  ['AuslanderRim1963','Stacks00MC'],'P1-S09','ramification',confidence='medium',authorship=T)
C(47,[40,42],[117,115],'Proposition2.5: r(S/R)=r((US)_p/U).',
  'For normal local domains R⊂S and unramified local R-algebra U in a common overfield, localize US at a maximal ideal above those of S and U. The diagonal index is unchanged on passing from S/R to this extension over U, provided the finite-algebra hypotheses used by the text hold.',
  'proved there','F','The proof reduces to both parts of2.4 and the cited normal-base flatness assertion from missing §1. No independent proof of that missing assertion is claimed.',
  ['AuslanderRim1963'],'P1-S09','ramification',confidence='medium',authorship=T)
C(48,[40,42],[115],'Lemma2.6: e_R(q)[S:R]=Σ e_{S_M}(qS_M)[κ(M):κ(R)].',
  'The valid general identity uses d-dimensional multiplicities, d=dim R, for a finite algebra over a noetherian local domain; components of smaller dimension contribute zero. For a finite local domain containing R, it gives e(S/R)=rank_R(S)/[κ(S):κ(R)]. If e on each component means its own-dimension multiplicity, R×κ(R) over a DVR refutes the unqualified general formula.',
  'stated without proof','E','Modern normalization and associativity are checked in Stacks43.15.2–3. The source cites this as known; its omitted §1 may already fix the ambient-dimension convention, so no ink error is decided.',
  ['Stacks0AZU','AuslanderRim1963'],'P1-S09','multiplicity',authorship=T)
C(49,[40,42],[115,113],'Theorem2.7: r=[US:U]; r=1 iff unramified; tower law; r=e[κ(S):κ(R)]_i.',
  'For normal noetherian local domains R⊂S⊂T that are local finite algebras, the index r equals the field degree after a transporter U, is a positive integer, detects unramifiedness, multiplies in towers and equals the multiplicity ratio times the inseparable residue degree. “Transporter” additionally requires unramified U/R, finite local US/U and purely inseparable residue extension, as the proof spells out.',
  'proof sketched','F','The visible proof checks these implications assuming the existence/flatness assertions cited from missing §1. The real Auslander–Rim1963 candidate was searched through publisher and later references; exact theorem collation was blocked, so archival/source identification remains limited.',
  ['AuslanderRim1963','Williamson1963'],'P1-S09','ramification',confidence='medium',authorship=T)
C(50,[40,42],[111],'Lemma3.1: finite weak hd gives finite hd after completion.',
  'For a local finite algebra S over noetherian local R, finite flat dimension of S over R implies that S_hat is finite over R_hat and has finite projective dimension. This does not hold for arbitrary local finite-type algebras merely by the word “local”.',
  'proved there','E','The page uses finite algebra plus localization and completion. Modern faithful flatness and perfectness criteria give the same argument.',
  ['Stacks00MC','Stacks0656'],'P1-S09','multiplicity',authorship=T)
C(51,[40,41],[111,109],'Proposition3.2: e(S/R)=Σ(−1)^i length_S Tor_i^R(S,κ(R)).',
  'Under C-SA13-050, the multiplicity ratio is the finite Euler characteristic of Tor, hence an integer. The finite-module case uses a finite free resolution and the residue-field length factor; the general local-finite-algebra case follows after completion.',
  'proved there','E','The complete symbolic calculation is re-executed in the proof notes, including the residue-degree factor. This is a classical Euler-characteristic identity, not a trace on an arbitrary infinite resolution.',
  ['Stacks0AZU','Stacks0656','AuslanderRim1963'],'P1-S09','multiplicity',authorship=T)
C(52,[40,41],[109],'Corollary3.3: r(S/R) is an alternating Tor-length sum if w.hd_S S^f<∞.',
  'Apply C-SA13-051 to S→S^f to obtain r(S/R)=Σ(−1)^i length_{S^f}Tor_i^S(S^f,κ(S)). Flat localization of S^e then gives the second expression. The transcription’s punctuation inside Tor cannot be read literally.',
  'stated without proof','E','The corollary is an immediate substitution into the checked identity; the localized-tensor step is verified, with the missing comma recorded as a reading alarm.',
  ['Stacks0AZU','AuslanderRim1963'],'P1-S09','multiplicity',authorship=T)
C(53,[40,42],[109],'Lemma3.4: R normal, S finite local domain, simple residue extension ⇒ e(S/R) integer.',
  'Choose α lifting a residue generator. Normality of R makes its monic minimal polynomial lie in R[T], so R[α] is finite free; residue degree divides its rank by the finite-flat length formula. The rank tower then proves integrality for S/R.',
  'proved there','E','The argument is checked directly from the printed proof and multiplicity identity. It requires the simple residue extension and the finite-domain hypotheses, not just normal R.',
  ['Stacks0AZU','AuslanderRim1963'],'P1-S09','multiplicity',authorship=T)
C(54,[40,42],[107],'Lemma3.5: a prime contracting to0 gives dim S=dim R.',
  'For normal noetherian local domain R and a local finite algebra S having a prime over0, dim S=dim R; its full-dimensional primes are exactly the primes contracting to0. Going down is used for the domain quotients, while finite integral extensions give the opposite dimension bound.',
  'proved there','E','The dimension proof is checked under the old finite-algebra convention. It is not true with “local algebra” reinterpreted as arbitrary finite-type algebra.',
  ['AuslanderRim1963'],'P1-S09','ramification',authorship=T)
C(55,[40,42],[107],'Lemma3.6: e_E(q)=Σ length(E_p)e_{R/p}(q).',
  'For noetherian local R, finite E and d=dim R, e_q(E,d)=Σ_{dim R/p=d} length_{R_p}(E_p)e_q(R/p,d). Using e_q(E,dim Supp E) instead would fail when dim E<d; this convention is not present on the excerpt.',
  'stated without proof','E','Exact modern statement and proof: Stacks43.15.3. The source calls it well known and cites missing reference[11].',
  ['Stacks0AZU'],'P1-S09','multiplicity',authorship=T)
C(56,[40,42],[107,105,103],'Proposition3.7: R normal, κ(S)/κ(R) simple ⇒ e(S/R) integer.',
  'The integrality in C-SA13-053 extends from finite S to local finite-algebra domains S, using a normal closure, an unramified decomposition-ring extension and multiplicity associativity. Normality of S is not assumed in this proposition.',
  'proof sketched','F','The visible reduction and arithmetic were followed, but its normal-closure/decomposition-ring preliminaries and exact original publication are missing. This is retained as a source-dependent classical claim, not an open question of Grothendieck.',
  ['AuslanderRim1963','Stacks0AZU','Williamson1963'],'P1-S09','ramification',confidence='medium',authorship=T)
C(57,[40,42],[103,101],'Theorem3.8: decomposition of r(S/R) into integers.',
  'For the local-domain extension of the page, diagonal multiplicity is the sum over generic components of the diagonal-local algebra of generic lengths times the component multiplicity ratios. The indicated ratios are integers under the normal-base/simple-residue hypotheses proved just before; separability of the fraction-field extension forces generic lengths1.',
  'proof sketched','F','Associativity explains the displayed decomposition, but missing definitions of the diagonal components and the earlier normality conventions limit the exact archival quantifiers. Auslander–Rim remains a checked bibliographic lead, not a full-text match.',
  ['AuslanderRim1963','Stacks0AZU'],'P1-S09','ramification',confidence='medium',authorship=T)
C(58,[40,42],[101],'Corollary3.9 ... galois ... inertia group.',
  'In the normal Galois case of the page, r(S/R) is the number of the relevant generic branches of the diagonal-local algebra, hence the order of the inertia group. This is the modified index r=e·inseparable residue degree, not always the ordinary ramification multiplicity e.',
  'proof sketched','F','The Galois counting interpretation is consistent with the preceding decomposition. Williamson’s paper confirms the contemporary inertia context but does not identify every theorem on these reused leaves.',
  ['AuslanderRim1963','Williamson1963'],'P1-S09','ramification',confidence='medium',authorship=T)
C(59,[40,42],[101],'Proposition3.10 begins and continues beyond the supplied leaf.',
  'Only the opening hypotheses of the next proposition survive in this package; its missing conclusion cannot be recovered as a unique claim. No theorem is supplied from expectations about ramification theory.',
  'stated without proof','F','Exact-title/source-family/backward-reference searches did not supply a collatable original page. This is an identified truncation, not a claim with an invented fate.',
  ['AuslanderRim1963'],'P1-S09',confidence='low',authorship=T)
C(60,[44],[123],'Div_{X/S}=R_{X/S}^*/O_X^*; restriction; principal; order.',
  'For flat locally finitely presented X/S, the page defines relative Cartier divisors through a sheaf of relative rational functions from missing §10.1, gives restriction/principal maps and an effective order. The exact denominators cannot be inferred uniquely. For the standard effective version, D is Cartier and flat over S, hence remains Cartier after arbitrary base change.',
  'stated without proof','C','EGAIV21.15 is the published comparison identified by Stacks31.19.2. The modern effective theorem is checked; identification with the excerpt’s full quotient sheaf remains conditional on the missing §10.1.',
  ['Stacks056P','EGAIV4'],'P1-S10',confidence='medium',authorship=T)
C(61,[45],[125],'Lemma6: tame over V ⇒ tame over V* for a proper birational map.',
  'For a finite separable function-field extension and normal projective birational models, tameness tested at all relevant valuations is unchanged by replacing the model. A divisor-only interpretation on a singular model is a different claim; the excerpt refers to an absent PartI definition and propositions.',
  'stated without proof','F','Abhyankar’s Tame coverings II is a bibliographic candidate; its text was not accessible for comparison. The scope of “tamely ramified” prevents an unconditional claim-level identification.',
  ['Abhyankar1960II'],'P1-S11',confidence='low',authorship=T)
C(62,[46],[127,125],'Lemma5: n(s)=binomial(n+s−1,n).',
  'For n-dimensional noetherian regular local R containing a coefficient field k, dim_k R/m^s=binomial(n+s−1,n) for s≥1 and0 for s=0. The associated graded ring is k[X_1,…,X_n], so monomials of total degree<s form a basis.',
  'proved there','E','The combinatorial calculation is re-executed exactly. It is a classical regular-local-ring fact; no new result or author attribution is inferred from its reuse.',
  ['Stacks0AZU','Stacks0C0S'],'P1-S12','regular-local',authorship=T)
C(63,[46],[129,127],'Lemma4: normalization ... principal ideal domain ... finitely many primes; complete ⇒ n=1.',
  'For a one-dimensional noetherian local domain, its integral closure in its fraction field is a semilocal Dedekind domain, hence a PID; if the original ring is complete it has one maximal ideal. The nontrivial valuation rings dominating R are its discrete valuation localizations; the trivial valuation ring K must be excluded.',
  'proof sketched','E','Krull–Akizuki and semilocal rank-one freeness give the first conclusion (Stacks10.120.18,10.78.7). The Hensel factorization argument for the complete case is checked on the page. Finiteness as an R-module is not claimed.',
  ['Stacks09IG','Stacks02M9'],'P1-S12','regular-local',authorship=T)
C(64,[47,48],[137,135],'(A Rbar)∩R=A; A principal iff A Rbar principal; K∩Rbar=R.',
  'For a noetherian local domain R with domain completion embedded in a common fraction overfield (as for regular local R), completion contracts every extended ideal; an ideal is principal iff its extension is; and Frac(R)∩R_hat=R. Faithful flatness gives contraction, and minimal generator counts give principality descent.',
  'proved there','E','The proof is rechecked under the necessary domain/completion embedding convention. Stacks10.97.3 supplies faithful flatness; the isolated equality ybar=mbar^q is a type error requiring scan review.',
  ['Stacks00MC'],'P1-S12','regular-local',authorship=T)
C(65,[48],[135],'R and R/M have the same characteristic so that R has a coefficient field.',
  'Equicharacteristic alone does not give a coefficient field in a noncomplete regular local ring. R=Q[x,y]_(x²−2,y) is regular of dimension2 and has residue field Q(√2), but no subfield mapping isomorphically to that residue field, since Q(x,y) contains no square root of2.',
  'false as stated','E','Cohen’s complete-local theorem gives the repaired sufficient hypothesis; refutation is of the isolated implication, since a missing standing completeness assumption could explain the excerpt. Refined statement C-SA13-067.',
  ['Stacks032A','Stacks0C0S'],'P1-S12','coefficient-field',authorship=T)
C(66,[47],[135],'then R=k[[x_1,…,x_n]].',
  'A noetherian regular local ring with a coefficient field need not equal its power-series completion. Q[x,y]_(x,y) is a counterexample: it is countable, whereas Q[[x,y]] is uncountable. Complete equicharacteristic regular local rings do have the stated power-series form.',
  'false as stated','E','Exact positive theorem: Stacks10.160.10, tag0C0S. The text’s parenthesis needs a standing completeness assumption, not a silent correction of the transcription. Refined statement C-SA13-067.',
  ['Stacks0C0S'],'P1-S12','coefficient-field',authorship=T)
C(67,[47,48],[135,133,131,129],'Lemma3: a form of Weierstrass Preparation Theorem; unique y′ and unit η.',
  'Let R=k[[x_1,…,x_n]], n>1, S=k[[x_2,…,x_n]], and0≠y of order b. If its initial form is nonzero on the x_1-axis, then y=uP for a unique unit u and distinguished monic P∈S[x_1] of degree b; its coefficients satisfy the order constraints forced by ord(y)=b.',
  'proof sketched','E','The classical complete-local Weierstrass theorem is the precise reconstruction. The manuscript’s uniqueness calculation is rechecked; the candidate Abhyankar source remains uncollated and its missing standing hypotheses are not supplied as original text.',
  ['Stacks032A','Abhyankar1960II'],'P1-S12','weierstrass',confidence='medium',authorship=T)
C(68,[47,48],[135,133,129],'If the line ... is tangential to z then ... non-tangential to t.',
  'The stated divisor corollary is valid with “non-tangential to z”: if z∈S[x_1] and t is a nonunit factor in R, then its normalized distinguished polynomial divides z in S[x_1]. The literal tangential→non-tangential implication is false, e.g. z=t=x_2.',
  'false as stated','E','The proof explicitly uses the non-tangential version and Weierstrass uniqueness. Refined statement is this same claim with that hypothesis; the ink must decide whether the word was dropped by transcription.',
  ['Abhyankar1960II'],'P1-S12','weierstrass',authorship=T)
C(69,[47],[133,129],'if k infinite or λ_R(e)≤2=n ... a non-tangential line.',
  'A nonzero homogeneous initial form has a nonvanishing direction over an infinite field. For two variables and degree≤2, it also has one over every field: a nonzero binary form of degree≤2 cannot vanish on all of P¹(k), which has at least3 points.',
  'proof sketched','E','The elementary projective-line argument is independently checked, including all binary quadratics over F₂. The phrase “projective plane” is insufficiently precise for the written counting argument.',
  ['Abhyankar1960II'],'P1-S12','weierstrass',authorship=T)
C(70,[49],[125,143],'Lemma7: a∈S iff x_1^q a∈M^q; a∈x_1S iff x_1^q a∈M^{q+1}.',
  'For a domain R⊂K, nonzero x_1 and M=(x_1,…,x_n), S=R[x_2/x_1,…,x_n/x_1], the two membership equivalences hold for some integer q≥0. Homogenizing a polynomial expression proves both directions.',
  'proved there','E','The complete algebraic proof is re-executed. The x_1b at143:1147 needs exponent q for the next line, and F/f is an independent notation alarm.',
  ['Abhyankar1960II'],'P1-S12','blowup',authorship=T)
C(71,[50],[143,141],'Lemma8: every generator of a cyclic quotient lifts to a generator.',
  'For a surjection of finite cyclic groups C_m→C_n and gcd(u,n)=1, there is w≡u mod n with gcd(w,m)=1. The source chooses v=n∏_{p|m,p∤u}p and w=u+v; this works prime by prime.',
  'proved there','E','The written construction is proved for all finite cyclic groups and checked in45150 finite cases up to m=300. It is a classical fact, with no need for a cyclic-order coprimality assumption.',
  ['Abhyankar1960II'],'P1-S12','cyclic-generators',authorship=T)
C(72,[49],[141],'An immediate quadratic transform ... maximal ideal containing x; regular of dimension n.',
  'For regular noetherian local R of dimension n>1, localize the blowup chart R[m/x] at a maximal ideal containing x, where x∈m minus m². The resulting ring is regular local of dimension n, centered at m. Localization at an arbitrary nonmaximal point would not preserve dimension n.',
  'stated without proof','E','The chart construction is classical; the page cites a missing Lemma1. The modern blowup-chart calculation is checked, while exact attribution to the candidate source remains unverified.',
  ['Abhyankar1960II'],'P1-S12','blowup',confidence='medium',authorship=T)
C(73,[49],[139,141],'Lemma9: for any minimal basis z_j, some z_i gives the same chart; mR*=z_iR*; R*≠R.',
  'For an immediate quadratic transform as in C-SA13-072, choose a parameter z_i of minimal value for a valuation centered at m*. Then all z_j/z_i lie in R*, the localization is unchanged, the extended maximal ideal is principal, z_i is a parameter of R*, and R*≠R because m is not principal for n>1.',
  'proof sketched','E','The valuation/unit argument is checked on139; the continuation is missing, so the final equality is independently completed from localization and chart universal properties.',
  ['Abhyankar1960II'],'P1-S12','blowup',confidence='medium',authorship=T)
C(74,[51],[145],'flat ... locally finite presentation ... residue fields finite separable.',
  'Flat and locally finitely presented with finite separable residue extensions is not sufficient for étaleness: Spec(Q[ε]/ε²)→Spec Q satisfies those conditions and is not unramified. A correct local criterion also asks that the maximal ideal of the fibre local ring be zero, or equivalently that the fibre be étale at the point.',
  'false as stated','A','EGAIV’s étale criteria and Stacks29.37.8/15 include the fibre condition. ClassA records the match in Grothendieck’s publication, not authorship of this unidentified reused leaf. The supplied leaf is refuted literally; the omitted condition is a scan-review question. Refined criterion appears in the modern statement here.',
  ['Stacks03PC','Stacks02GH','EGAIV4'],'P1-S13','etale',authorship=T)
C(75,[51],[145],'Lemma5: an étale radicial morphism is an open immersion.',
  'For a morphism of schemes, being an open immersion is equivalent to being étale and universally injective. No separatedness assumption needs to be added.',
  'stated without proof','A','Exact theorem checked: Stacks41.14.1; it also gives the flat-monomorphism-of-finite-presentation characterization. ClassA marks the published EGA match; authorship and relative dating of the reused leaf remain unknown.',
  ['Stacks025G','EGAIV4'],'P1-S13','etale',authorship=T)
C(76,[52],[145],'axiomatic conditions for a topos, continued on the neighboring typed sheets.',
  'The fragment gives categorical exactness/generator conditions in a topos characterization, not a new geometric assertion. The adjacent package supplies more of the same typed exposition; the isolated last sentence is not a complete axiom system.',
  'stated without proof','F','The comparison is with the axiomatic topos material continued at33:147ff, whose references are reviewed in the p2 claims. Only the actual overlap is linked; the missing complete theorem is not reconstructed from its heading.',
  [],'P1-S14',confidence='medium',authorship=T)
def save():
    (OUT/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
    print(f'p1: {len(claims)} manually reviewed claims saved')
if __name__=='__main__':save()
