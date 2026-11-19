"""Serialize the human/model-authored claims audit, not inferred from headings.
Sources were read with line numbers; fate statements come from opened references.
"""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]/'parts/a'
P='pro/MPL_93_047-091_transcription.tex:'
K='codex/K93-12_transcription.tex:'
claims=[]
def add(n,items,scans,lines,his,modern,status,cls,fate,date,refs,confidence='high',calc='',present=''):
    claims.append(dict(id=f'C-SA04-{n}',items=[f'SA04-{i}' for i in items],cote='93',scans=scans,
      lines=lines if isinstance(lines,list) else [P+lines],his_statement=his,statement=modern,
      status_on_pages=status,computation=({'program':'programs/a_computations.py','output':'outputs/a_computations.txt','detail':calc,'proof':'parts/a/proof_checks.md'} if calc else {'detail':'No numerical/formal computation asserted; source comparison and/or cited theorem as described.','proof':'parts/a/proof_checks.md'}),
      **{'class':cls},fate=fate,fate_date=date,present_status='As of 2026-11-19: '+(present or fate),refs=refs,confidence=confidence))

add(1,[13,17],[37,38,47,48],[K+'173–212',P+'24;28–32'],
 'Programme; foncteur D*; deux constructions',
 'For a base S on which p is locally nilpotent, a BT group has a finite locally free contravariant Dieudonné crystal, functorial under base change. After reduction to characteristic p it has F and V with FV=VF=p. The exponential/universal-extension and cohomological constructions must be compared; the manuscript only announces them.',
 'stated without proof; construction programme; the comparison heuristic is expressly labelled heuristic', 'A',
 'Exact published formulation in Grothendieck ICM1970 §3 pp432–433. Messing and Mazur–Messing developed the two constructions; de Jong1995 introduction pp5–6 explicitly records this history and the comparison. Modern prismatic classification is a different enlarged formalism, not a proof that the original ordinary-crystal functor is an equivalence on every base.',
 'ICM lecture1970/proceedings1971; Messing1972 and Mazur–Messing1974 as documented in de Jong1995; no manuscript date inferred.', ['GrothICM1970','deJong1995','AnschutzLeBras2023'])
add(2,[],[38],[K+'198–212'],'F:M^(p)→M; V:M→M^(p); VF=p id_M',
 'With the displayed arrows, FV=p id_M and VF=p id_M^(p). The displayed crystal functor is contravariant, hence its source requires BT(S)^op.',
 'false as transcribed at the level of domains; the possible ink error is undecided','E',
 'The standard typed identities are explicitly printed in Grothendieck ICM1970 §3 p433 and in Lau Definition6.1. Domain/codomain composition, not an arithmetic experiment, detects the reversal.',
 'Classical Dieudonné conventions; opened published formulations1971 and2010/2013.', ['GrothICM1970','Lau2013'],present='Mathematical domain mismatch certain; attribution to manuscript ink versus transcription remains unresolved.')
add(3,[],[39],[K+'218–220'],'Problème1: pleinement fidèle? image essentielle?',
 'For arbitrary characteristic-p schemes S, ask whether the ordinary crystalline Dieudonné functor on BT groups is fully faithful and identify its essential image. This is not restricted to regular or perfect S.',
 'open on the pages','C',
 'The unrestricted full-faithfulness hope has a negative answer: de Jong ICM1998 §2(x) p261 explicitly records failure over Fp[x,y]/(x²,xy,y²), referring to Berthelot–Messing4.4.1. The displayed ring is characteristic p and Noetherian, so it falls within the manuscript scope. The actual pair of BT groups is not reproduced by that source; this run uses the published negative result, not an independently certified counterexample. Positive exact replacements: de Jong–Messing1999 excellent lci full faithfulness, and Anschütz–Le Bras Theorem1.4.4/Remark1.4.7 quasi-syntomic classification. Arbitrary-base essential image is not identified by those theorems.',
 'Negative example published1990, documented1995/1998; positive1999; prismatic preprint2019, publication2023, erratum2025 does not alter main statements.', ['deJongICM1998','BerthelotMessing1990','deJongMessing1999','AnschutzLeBras2023','AnschutzLeBrasErratum2025'],confidence='high',present='General ordinary-crystal full faithfulness is false by the checked primary literature; precise positive hypotheses are essential. No global-open claim is inferred about formulations with extra divided or prismatic structure.')
add(4,[],[39,40],[K+'220–226'],'Problème2; base parfaite; groupes Λ_n-plats',
 'For a perfect characteristic-p base, classify finite flat p-primary groups and truncated BT groups by Witt Dieudonné modules. The finite flat category requires admissible torsion modules, whereas a level-n BT object corresponds to a finite projective W_n-module with additional level-one exactness and projective-cokernel conditions.',
 'open on the pages','B',
 'Lau §6 Definition6.1, Theorem6.4 and Corollary6.5 give the precise modern distinction. Bare finite-projective W_n-modules with only FV=VF=p are insufficient at level1; the text’s unspecified usual conditions cannot be discarded. Lau credits earlier unpublished work of Gabber; Berthelot’s perfect valuation-ring case is cited there.',
 'Lau arXiv v1 2010-06-14; JAMS26(2013)129–165; earlier Gabber circulation date not established.', ['Lau2013'],present='Established with the exact Dieudonné categories just specified; the anonymous phrase usual conditions is not treated as an explicit definition.')
add(5,[],[41],[K+'230–235'],'0→ω_G→D*(G)_S→t_G*→0',
 'The evaluated contravariant BT crystal has the canonical Hodge exact sequence 0→ω_G→D(G)_S→Lie(G^∨)→0, locally split as modules, natural in G and under base change. The local definition of t_G in the Codex witness is checked against the intended Lie/dual convention.',
 'stated without proof','A',
 'Grothendieck ICM1970 §4 p433 states the exact sequence, functoriality and base-change compatibility. Anschütz–Le Bras Remark1.4.2 gives the corresponding prismatic Hodge quotient and Remark1.4.3 the characteristic-p comparison.',
 'ICM1970/proceedings1971; prismatic2019/2023.', ['GrothICM1970','AnschutzLeBras2023'])
add(6,[9,10,18],[42,43,45,47,48],[K+'249–267;363–372',P+'10–14;34'],
 'prolongements ... correspondent; puissances divisées nilpotentes',
 'For a divided-power infinitesimal thickening S⊂S′, with locally nilpotent divided powers, deformations of a BT group are equivalent to lifts of its Hodge direct summand in the crystal evaluated at S′. The source also states variants when the group or its Cartier dual is infinitesimal. For abelian schemes the analogous filtration statement is tied to the BT comparison. The exponential passage from a lifted Lie submodule to a lifted vector subgroup and its quotient is deferred.',
 'stated without proof; exponential and quotient steps explicitly deferred','A',
 'Grothendieck ICM1970 §4 pp433–434 repeats the theorem and all three alternative qualifications. Its Remark1 expressly warns that without them filtrations need not determine lifts, already for the split ordinary height-two group. Messing’s proof is used precisely in de Jong1995 Proposition3.2.1. Katz Theorem1.2.1 proves the abelian/BT deformation equivalence over p-nilpotent nilpotent thickenings.',
 'Announced1970/published1971; Messing1972; Katz1981 gives Drinfeld’s proof of Serre–Tate.', ['GrothICM1970','deJong1995','Katz1981'],present='Established in the qualified Grothendieck–Messing setting. Unqualified divided-power thickenings are not covered.')
add(7,[],[43],[K+'269–271'],'Problème3; j’ai un candidat',
 'Seek a crystalline/linear formulation of deformations of finite locally free p-primary group schemes. The candidate alluded to on the page is not written there; it cannot be identified with a specific derived object.',
 'open on the pages; proposed candidate absent','C',
 'Illusie1985 introduction and the truncated-BT deformation theorem document established lifting results and the replacement of Grothendieck’s route by Raynaud embeddings in BBM. Anschütz–Le Bras §5.1 develops finite locally free groups in prismatic theory over quasi-syntomic rings. Neither source identifies this unwritten candidate or proves a formulation on every p-nilpotent base with no extra conditions.',
 'Grothendieck lecturesJune1971, reconstructed in Illusie1985; prismatic2019/2023.', ['Illusie1985','AnschutzLeBras2023'],confidence='medium',present='Substantial established theories exist; the literal candidate remains unidentifiable and the strongest arbitrary-base formulation is not declared settled.')
add(8,[24],[43,44,49],[K+'273–310',P+'54–58'],
 'Ker F=Im V; filtration canonique',
 'The Hodge filtration is related to the kernel/image of F,V after reduction to the characteristic-p base, with a Frobenius twist. Over a perfect ring the twist is invertible and the filtration is recovered uniquely. Over a general base, exactness and local freeness for realizable Dieudonné crystals are additional assertions, not consequences of cancelling p alone.',
 'proof sketched; relevant exactness/local freeness asserted','B',
 'Lau Definition6.1 and Lemma6.2 give an exact modern algebraic verification over perfect bases; Theorem6.4 identifies the realizable category. The general Hodge sequence is Grothendieck ICM §4. Our cancellation proof establishes the two mod-p kernel/image identities when the Witt module is p-torsion free; it does not establish arbitrary-base projectivity.',
 'Classical perfect-field case; perfect-ring result circulated2010/published2013.', ['Lau2013','GrothICM1970'],present='Correct in the specified perfect-ring and realizable-crystal settings; the module before reduction cannot have the printed nonzero kernel.')
add(9,[7,8],[44,45,47],[K+'321–353',P+'4–8'],
 'R¹ f_cris* O; H¹ de Rham; D*(A)=Lie E(A*)',
 'For an abelian scheme A/S, the degree-one relative crystalline realization is locally free, evaluates to relative de Rham H¹ on a suitable lift, and has the Hodge extension. Its universal-extension description is Lie E(A^∨), compatible with base change. In the Hodge quotient R¹f_*O_A the source cannot use O_S as a sheaf on A without an understood pullback.',
 'stated without proof; one structure-sheaf subscript and one A/A* occurrence are suspect','B',
 'de Jong1995 introduction p6 records the Mazur–Messing comparison theorem; Illusie Pisa lecture §5 pp18–20 identifies the universal extension and Hodge sequence. These establish the degree-one construction, while the exact crystalline site and conventions have to be carried through. No all-degree comparison is inferred.',
 'Mazur–Messing1974; historical account2013 lecture/published2015.', ['deJong1995','IllusiePisa2013'],confidence='high')
add(10,[],[45],[K+'343–345'],'sur une base affine ... toujours un prolongement',
 'An abelian scheme over the closed fibre of the relevant infinitesimal divided-power situation is asserted to admit a lift on an affine thickening. A polarization is not part of the stated lift. Interpret abelian scheme in the source’s proper smooth group-scheme convention; do not add a chosen ample bundle.',
 'stated without proof; attributed to Mumford/GIT','C',
 'For the p-nilpotent infinitesimal setting, Grothendieck–Messing filtration lifting plus Serre–Tate gives the local unobstructed lifting mechanism; Katz Theorem1.2.1 is exact for that comparison. The full cited Mumford/GIT statement and any extension to arbitrary characteristics or a prescribed polarization were not identified in the opened sources. The claim is not labelled false simply because polarized deformation dimensions differ.',
 'Serre–Tate result predates Katz1981; exact GIT locator unresolved.', ['Katz1981','GrothICM1970','Illusie1985'],confidence='medium',present='Established in the p-nilpotent infinitesimal scope used by the programme; the broader attribution and polarization requirements remain distinct.')
add(11,[],[46,47],[K+'378–400',P+'4–24'],
 'extension vectorielle universelle; cristalline; R¹f_cris* G_m',
 'Construct the universal vector extension E(A) of an abelian scheme, compare its values on nilpotent divided-power thickenings canonically and transitively, and identify the resulting Lie crystal. The displayed multiplicative crystalline cohomology expression requires its precise site and sheaf convention; it cannot be replaced without checking by the ordinary Picard functor.',
 'construction said to work; comparison isomorphisms and exponential step deferred','B',
 'Illusie’s Pisa lecture §5 explains the universal extension, its crystalline behavior and the role of modified definitions; de Jong1995 introduction matches the exponential and extension constructions to Messing/Mazur–Messing. The exact handwritten R¹G_m expression is retained as a formulation to collate, because ordinary R¹f_*G_m and crystalline R¹ are different objects. This run does not assert a degree-one line-bundle counterexample without checking existence of a crystalline structure.',
 'Grothendieck’s letters1966/1969 documented by Illusie; Messing1972/Mazur–Messing1974.', ['IllusiePisa2013','deJong1995'],confidence='medium')
add(12,[11,12],[47],'16–22','accouplement parfait; compatible avec les filtrations',
 'The contravariant degree-one realizations of A and A^∨ have a perfect duality pairing compatible with Hodge filtrations. On underlying crystals this relates the covariant and contravariant conventions; Frobenius-compatible duality must specify the Tate twist. The uncertain inserted vee in D_*(A)=LieE(A)≃D*(A*)^vee conflicts with applying the preceding formula to A*.',
 'stated without proof; uncertain dual exponent','B',
 'The universal-extension/Hodge duality is part of the degree-one crystalline comparison recorded by Mazur–Messing and reviewed in Illusie §5. The displayed definitions themselves establish the typing warning; they do not establish a canonical self-duality of A.',
 'Universal-extension comparison1974; direct mathematical convention check in this run.', ['IllusiePisa2013','deJong1995'],confidence='medium')
add(13,[15,20],[48],'28–42','D*(A(∞))≃R¹f_cris*O; E(A(∞))≃E(A)(∞)',
 'For p locally nilpotent, identify the BT crystal of A[p∞] with R¹f_cris*O_A, naturally under base change and compatible with Hodge filtrations. Likewise identify universal vector extensions as fppf group sheaves and as group-valued crystals. The p-primary torsion of a vector extension is not asserted to be a finite locally free BT group.',
 'stated without proof','B',
 'de Jong1995 introduction pp5–6 explicitly identifies the Mazur–Messing comparison as the abelian de Rham/BT-crystal comparison. The extension constructions are also traced there. The group-valued statement is interpreted in the same sheaf setting as the source, with the vector kernel kept separate from BT representability.',
 'Mazur–Messing, LNM370,1974; exact comparison history opened in de Jong1995.', ['deJong1995','IllusiePisa2013'],confidence='high')
add(14,[18],[48],'34','théorème de Serre-Tate ... méthode suivie par Messing',
 'If R has nilpotent p and I⊂R is nilpotent, abelian schemes over R are equivalent to triples consisting of an abelian scheme A0 over R/I, a BT group G/R, and an identification G modI≃A0[p∞]. The source proposes deriving this by nilpotence dévissage from the filtered deformation comparisons.',
 'proof sketched; proof route attributed to Messing','A',
 'Grothendieck ICM1970 §1 p432 states exactly the categorical theorem. Katz1981 Theorem1.2.1 provides the full general ring statement and Drinfeld’s elementary proof. This is an equivalence of marked deformation categories, not uniqueness of an unmarked lift.',
 'Serre–Tate theorem announced before1970; published ICM1971; Katz1981 says approximately16years earlier, not an exact first-circulation date.', ['GrothICM1970','Katz1981'])
add(15,[20],[48],'36–42','cristaux en groupes',
 'Promote the universal-extension torsion comparison from the evaluated fppf group sheaves to compatible group-valued crystals, with canonical transition isomorphisms. This is stronger than an isolated isomorphism on S.',
 'stated without proof','B',
 'The crystalline universal-extension formalism is developed in Messing/Mazur–Messing and identified in de Jong1995 introduction. Illusie §5 confirms the distinction between the extension and its Lie crystal. The exact all-thickenings descent is used as a literature result; it is not proved by our evaluated formula check.',
 '1972/1974.', ['deJong1995','IllusiePisa2013'],confidence='medium')
add(16,[22,50],[48,51],'46–48;110–112','Passage à la limite; Conjecture7 ... vers les',
 'The passage-to-the-limit heading and broader crystalline/p-adic conjecture are cancelled; Conjecture7 ends before its target category is supplied. No precise all-degree comparison theorem can be extracted from this incomplete sentence.',
 'corrected by himself later: local cancellation48/51; related forward/inverse questions survive51/53','F',
 'Grothendieck ICM1970 §5 p435 gives a surviving published broader programme, with arbitrary finite filtrations and relative bases. Fontaine/Colmez–Fontaine supply a precise rational comparison on specified admissible categories, but cannot identify the missing final words of this leaf.',
 'Published programme1971; admissibility theorem2000.', ['GrothICM1970','ColmezFontaine2000'],confidence='high',present='The fragment is not promoted to a complete conjecture; its surviving neighbours are C-SA04-21–25.')
add(17,[24,69],[49,54],'54–58;192','tout Cristal de Dieudonné ... admissible; équivalence',
 'Over a perfect characteristic-p ring, the appropriate finite-projective Witt FV-modules classify BT groups. The unique canonical Hodge filtration is part of this algebraic classification, not Fontaine admissibility of an arbitrarily chosen characteristic-zero filtration.',
 'stated without proof on49; invoked as a conditional input on54','B',
 'Lau Theorem6.4 establishes the perfect-ring equivalence and Corollary6.5 the finite-flat version, crediting Gabber. Its Definition6.1 makes the categories precise. The source’s use of admissible here must not be conflated with the later period-domain condition.',
 'Gabber result earlier unpublished, exact date unverified; Lau preprint2010/publication2013.', ['Lau2013'])
add(18,[26,27],[49],'60–64','ne pas fournir un champ; Hom⊗Q',
 'An additive crystalline realization extends to global p-isogeny localization. That global-Hom localization need not be a stack: on the disjoint union of Fp-points, componentwise p^{-n} endomorphisms of Qp/Zp fail to glue because their denominators are unbounded.',
 'proof sketched only for localization; stack defect explicitly noted','A',
 'Grothendieck ICM1970 §5 p434 uses global rationalized Hom. The precise non-stack example is an earlier-run inference independently reproved here. The correction is to use a suitable local/sheafified quasi-isogeny formulation or a bounded-denominator hypothesis; ordinary additive localization alone does not supply descent.',
 'Published definition1971; counterexample checked2026-11-19.', ['GrothICM1970'],present='The warning is correct and the stated example checks it. No claim that every local isogeny category automatically satisfies object descent is made.')
add(19,[28],[49],'66–73','Proposition (prouvée plus tard); immersion nilpotente',
 'Restriction across a nilpotent thickening with ideal annihilated by one power of p induces an equivalence on BT groups up to isogeny. The literal manuscript lacks a reliable global p-bound after cancelling quasi-compactness and prints puissance de J. Its exact non-quasi-compact version is therefore separated from the bounded statement.',
 'stated without proof; deferred; hypothesis reading unsettled','A',
 'Grothendieck ICM1970 §5 p434 states the bounded-p-ideal theorem explicitly. Katz Lemma1.1.3 proves the uniform lifting-of-multiples mechanism for nilpotent ideals. These sources justify the bounded theorem, not removal of all global bounds in a category with globally rationalized Hom.',
 'ICM1970/proceedings1971; Katz1981.', ['GrothICM1970','Katz1981'],confidence='high',present='Bounded-p-ideal theorem established; exact broad non-quasi-compact manuscript reading is not silently substituted for it.')
add(20,[29],[49,51],'73;108','VII10.8.2 de mes notes de Pise',
 'A theorem with this precise internal Pisa locator is invoked as a consequence, but its statement is not reproduced. The complete-base filtered functor is the likely surrounding subject, not an identified quotation of that theorem.',
 'stated without proof by cross-reference only','F',
 'Searched the exact locator, Grothendieck published-work bibliography, Montréal/ICM texts, Illusie’s Pisa account, and EGA/SGA-related search results. No opened source identified VII10.8.2. ICM §5 p435 is a demonstrable thematic counterpart, not a replacement identification.',
 'No exact date or bibliographic identity established.', ['GrothICM1970','IllusiePisa2013','GrothPublishedWorks'],confidence='low')
add(21,[31],[49,51],'75;100–108','image essentielle; critère valuatif',
 'For noetherian p-adically complete A, characterize which filtered isocrystals arise from BT groups up to isogeny, and ask for a valuative criterion. A fixed-special-fibre deformation problem, a quasi-isogeny period space, and the full relative category are distinct versions.',
 'open on the pages','C',
 'Grothendieck ICM §5 p435 repeats the essential-image question. Colmez–Fontaine Theorem4.3 answers weak admissibility versus admissibility for filtered (phi,N)-modules over a complete discretely valued mixed-characteristic field with perfect residue field; N=0 gives the crystalline case. Hartl Theorems3.3/3.5 identify the analytic admissible locus for the stated Rapoport–Zink period morphism. Anschütz–Le Bras handles quasi-syntomic bases with prismatic objects. None is an unrestricted valuative criterion for the manuscript’s original category over arbitrary A.',
 'Question published1971; Colmez–Fontaine2000; Hartl arXiv2007/publication2008; prismatic2019/2023.', ['GrothICM1970','ColmezFontaine2000','Hartl2008','AnschutzLeBras2023'],confidence='high',present='Precisely stated field and prismatic versions are established; the original general relative valuative quantifier has not been matched to an exact theorem in this audit.')
add(22,[33],[49,51],'75;100;108','un ouvert de Zariski de la grassmannienne',
 'Ask whether realizable two-step filtrations on a fixed isocrystal form a Zariski-open subset of its Grassmannian, including the relative problem. The requested topology is Zariski.',
 'open on the pages','C',
 'Hartl Theorem1.2 gives analytic weakly-admissible openness; Theorem3.3 gives analytic admissible openness, and Example3.6 proves strict inclusion for nonclassical analytic points in a specific rank5 example. These do not establish the manuscript’s Zariski-openness assertion. ICM1970 p435 preserves that same question. No general negative Zariski theorem or explicit counterexample is claimed from analytic strictness alone.',
 'Question published1971; analytic results summarized2007/2008.', ['GrothICM1970','Hartl2008'],confidence='high',present='Analytic openness is established in exact stated settings; general Zariski openness in the original formulation is not certified here.')
add(23,[44],[51,53],'102–106;146–156','pas essentiellement surjectif; conditions de rangs',
 'The filtered realization is not essentially surjective onto all pairs of correct ranks. In the reconstructed Hodge convention, phi=diag(1,p), Fil¹=Ke0 has tH(D)=tN(D)=1 but tH(K0e0)=1>0=tN(K0e0). The unlabeled handwritten polygon comparison is not assigned an orientation beyond what is legible.',
 'non-surjectivity stated without proof; rank-only extension asked as a question','B',
 'Weak-admissibility inequalities in Colmez–Fontaine §4.1/Theorem4.3 give a precise necessary obstruction. The explicit rank2 example is the earlier run’s example, now independently recomputed. It refutes the rank-only realization criterion; it does not claim period functors are undefined on all nonadmissible inputs.',
 'Fontaine admissibility framework predates2000; Colmez–Fontaine theorem2000; explicit audit check2026.', ['ColmezFontaine2000'],calc='C23 exact Hodge/Newton number table; subobject inequality checked in proof_checks.md.')
add(24,[45,64],[48,51,53],'48;106;173–178','foncteur mystérieux; foncteur quasi-inverse; Hodge-Tate',
 'For K complete discretely valued of mixed characteristic with perfect residue field, recover rational crystalline representations from admissible filtered phi-modules and conversely via period rings; identify the BT subcategory by its Hodge weights together with the necessary integral/lattice realizability statement. Mere Hodge–Tate type is necessary and not by itself a classification.',
 'open on the pages; forward and inverse functors explicitly requested','B',
 'Colmez–Fontaine §4.1 constructs D_st(V)=(B_st⊗V)^G and V_st(D), and Theorem4.3 plus its corollary gives equivalence with weakly admissible filtered (phi,N)-modules. Setting N=0 gives the rational crystalline comparison. The BT origin is narrower than arbitrary semistable representations and retains weights/convention and lattice issues. Tate §4 gives the Hodge–Tate necessity. The source’s Galois tensor should be over the characteristic-zero field, not an unidentified W|V symbol.',
 'Tate1966 conference/publication1967; period theorem2000; no unsupported first-preprint date supplied.', ['ColmezFontaine2000','Tate1967'],present='The rational mysterious-functor programme is realized on the admissible crystalline category. The page does not justify replacing it by all Hodge–Tate representations or extracting a canonical integral lattice.')
add(25,[47,48],[51],'108','vers les faisceaux p-adiques constants tordus; A0 red',
 'For relative p-adically complete A, construct the étale p-adic local system on Spec(A[1/p]) attached to a realizable filtered isocrystal, with reduction/evaluation and descent data. It is stronger than checking each complete-valued-field point.',
 'open on the pages; some reduction/evaluation shorthand asserted','C',
 'Anschütz–Le Bras Theorem1.4.4 and §5.4 provide a precise modern classification and étale comparison for quasi-syntomic rings using admissible prismatic Dieudonné objects. Their Definition1.1.1 requires p-completeness, bounded p-power torsion and cotangent-complex amplitude[-1,0]. These hypotheses and the changed target objects cannot be erased to settle the exact arbitrary-noetherian-A filtered-crystal formulation. Grothendieck ICM §5 p435 explicitly asks for relative generalization.',
 'Published question1971; arXiv2019; Forum MathPi2023; erratum2025 concerns another proof and preserves main results.', ['GrothICM1970','AnschutzLeBras2023','AnschutzLeBrasErratum2025'],confidence='medium')
add(26,[49,50],[51],'110–112','Question ... cohomologie cristalline et p-adique',
 'The cancelled heading signals a wider cohomological comparison programme, but the following cancelled sentence does not specify its target. The precise claim recoverable here is only a programme extension from degree1/two-step filtrations to higher degrees.',
 'corrected by himself later: cancelled heading and incomplete conjecture','F',
 'Grothendieck ICM §5 final paragraph p435 explicitly broadens to Frobenius crystals with arbitrary finite filtrations and relative bases. This confirms the programme without supplying the missing local sentence. Modern p-adic comparison theorems are not entered as an exact fate of an unidentified assertion.',
 'ICM1970/proceedings1971.', ['GrothICM1970'],confidence='high')
add(27,[62],[53],'161–171','Th.(Tate); pleinement fidèle; à isom unique près',
 'If S is normal, integral and Noetherian with characteristic-zero function field K, restriction BT(S)→BT(K) is fully faithful. Over K the étale BT category is equivalent to continuous finite-free Zp representations. Unique extension is relative to a specified generic-fibre identification; an unmarked object can have automorphisms.',
 'stated without proof; explicitly attributed to Tate','E',
 'Tate1967 Theorem4 pp180–181 is the exact statement; Corollary1 gives the Tate-module Hom comparison. The marked uniqueness qualification is a categorical consequence of full faithfulness, not a strengthening to trivial automorphism groups.',
 'Driebergen conference1966; proceedings1967 pp158–183.', ['Tate1967'])
add(28,[64],[53],'173','type de Hodge-Tate',
 'The rational Tate module of a BT group over the ring of integers of the indicated complete mixed-characteristic field is Hodge–Tate with the two weights determined by the Lie group and its dual, after choosing covariant/contravariant conventions.',
 'stated without proof; attributed to Tate as a necessary condition','E',
 'Tate1967 §4, Theorem3 and corollaries, gives the Hodge–Tate decomposition. Colmez–Fontaine §4.1 identifies the stronger admissibility condition needed for a converse. A numerical Hodge–Tate weight list alone is not claimed sufficient.',
 '1966 conference/1967 publication.', ['Tate1967','ColmezFontaine2000'])
add(29,[68,69],[53,54],'180–192','la restriction ... car.nulle est inutile',
 'For a normal integral Noetherian scheme in characteristic p, restriction of BT groups to the generic point is fully faithful. The proposed route uses crystalline full faithfulness and perfect-base classification.',
 'open on the pages; conjectured; proposed reduction sketched','B',
 'de Jong1998 Corollary1.2 proves the DVR statement without a p-basis hypothesis; his ICM1998 Theorem2 states the normal-Noetherian-integral version and cites Tate’s p181 reduction. The full author-hosted paper and erratum were opened locally. The1999 erratum changes Lemma2.1(iii) and the definition of semistable reduction, not this theorem. Berthelot–Messing1979 §1 Lemma1 is an exact intermediate formulation of the manuscript’s strategy. The original SGA7I scan, IX Remark5.11 printedp386, explicitly records that removal of the characteristic restriction in5.8–5.10 depends on unrestricted Tate full faithfulness. That exact original passage was OCR-read and visually checked; the introduction itself was not independently collated.',
 'SGA7I IX5.11 published1972 explicitly records the remaining characteristic restriction; deJongInvent134(1998)301–333; erratumInvent138(1999)225. No manuscript date inferred.', ['deJong1998','deJongErratum1999','deJongICM1998','BerthelotMessing1979','SGA7I'],present='Settled positively in the exact normal Noetherian BT scope; the proof does not require the broader no-F crystal claim.')
add(30,[70],[54],'186–190','Cris loclib(S)→Cris loclib(η) pleinement fidèle?',
 'For every normal integral Noetherian characteristic-p S, ask full faithfulness of restriction for finite locally free ordinary crystals, without Frobenius. The exact crystalline base/site must also be specified.',
 'open on the pages','C',
 'Searches of de Jong’s1995/1998 papers, Berthelot–Messing1979, later prismatic work and exact generic-point/full-faithfulness terms found the nondegenerate-F theorem, not an exact theorem covering all ordinary crystals under these hypotheses. The ordinary-crystal question is stronger/different and is not resolved merely by forgetting F from a fully faithful F-category.',
 'F-version established1998; no exact general no-F fate identified through2026-11-19.', ['deJong1998','BerthelotMessing1979','AnschutzLeBras2023'],confidence='low',present='Exact no-F formulation remains unmatched in the literature search; this is not a claim that the world literature leaves it open.')
add(31,[71],[54],'190','ou du moins ... F-cristaux',
 'The fallback asks full faithfulness of restriction for F-crystals. A precise established form uses nondegenerate F-crystals over a characteristic-p DVR admitting a p-basis.',
 'open on the pages','B',
 'de Jong1998 Theorem1.1 gives exactly the DVR/p-basis/nondegeneracy theorem. His ICM1998 Theorem1 restates it. The source’s normal-Noetherian formulation and unspecified F-nondegeneracy are not suppressed; the proven DVR form is sufficient for the BT application after the documented reductions.',
 'Invent134(1998), Theorem1.1; author preprint date not independently established.', ['deJong1998','deJongICM1998'],present='Established with nondegeneracy and the stated DVR/p-basis hypothesis; no unqualified all-normal-base F-crystal theorem is claimed here.')
add(32,[72,69],[54],'192','ramené facilement ... k[[t]], k alg.clos',
 'For the BT Hom-extension problem, reduce to S=Spec(k[[t]]) with algebraically closed k, then use perfect-base Dieudonné full faithfulness plus a suitable crystalline Hom-extension theorem. It is not automatically a reduction for every ordinary-crystal question.',
 'proof sketched; conditional on explicit inputs','B',
 'Berthelot–Messing1979 §1 pp18–19, Lemma1, gives the same perfect-closure strategy and the k[[t]] reduction. de Jong1998 introduction identifies Tate1967 p181 as the reduction and explains why Theorem1.1 implies Corollary1.2. The proof route is therefore an exact historical link, not a merely analogous later theorem.',
 'Published1979 intermediate route; completed1998.', ['BerthelotMessing1979','deJong1998','Tate1967'])
add(33,[73],[54],'192','Modules avec connexions formelles',
 'On a formal lift of k[[t]], locally free crystals are described by suitable topologically quasi-nilpotent integrable connections; F-crystals additionally require a horizontal Frobenius map with the stated nondegeneracy. Ordinary arbitrary formal connections are not the same category.',
 'stated without proof; technical translation left implicit','B',
 'de Jong ICM1998 §1 pp259–260 describes the quadruple (M,∇,F,V) on a completed divided-power envelope, and the nondegenerate F variant. Berthelot–Messing1979 provides the crystalline formalism used in the proposed reduction. The formal-connection translation is established, but depends on the exact crystalline site and nilpotence conditions.',
 'Berthelot1974/BBM1982 formalism, summarized in opened1979/1998 sources.', ['deJongICM1998','BerthelotMessing1979'])

add(34,[35],[50],'87','x_n tend vers x',
 'The two displayed weighted sums are incompatible. With u_k=e and 0<gamma<1 the literal finite sums tend to1−gamma while the proposed infinite sum is1. A k−1 exponent in the finite sum repairs this calculation.',
 'false as transcribed; possible exponent misreading','E',
 'This is elementary geometric summation. The corrected weights appear in de Jeu–Jiang Proposition4.2 and Theorem4.4; the source is an anonymous cancelled exercise sheet, not a new theorem attributable to Grothendieck. No edition or exercise provenance was identified by the targeted factorization search.',
 'Cohen factorization1959; modern comparison2016online/2017volume; arithmetic rechecked2026.', ['deJeuJiang2017','Cohen1959'],calc='C34 symbolic finite sum and corrected sum.')
add(35,[34],[50,52],'87;139–141','z=xy; y∈overline(Az); norm(z−y)<δ',
 'A Banach algebra with a bounded left approximate identity admits Cohen factorization z=xy, with y in the closure of Az and arbitrarily close to z. The two printed preliminary defects prevent treating its literal induction as a complete proof.',
 'proof sketched on anonymous cancelled exercise sheet','E',
 'Cohen’s1959 Factorization in group algebras is verified bibliographically through the opened Numdam references. de Jeu–Jiang Theorem4.4 supplies the modern approximate simultaneous/power factorization under a bounded left approximate identity; its singleton case gives this form. The elementary continuity endpoint is independently checked, not the full corrupted induction.',
 'CohenDuke26(1959)199–205; modern paper firstonline2016-11-23/Positivity21(2017)633–672.', ['Cohen1959','ChivukulaHeckman1974','deJeuJiang2017'])
add(36,[36,37],[50],'89','f est un polynôme de degré≤α; limJ=c_ka_p',
 'An entire Banach-valued function with |p(theta)|·norm f(re^{i theta})≤Mr^alpha uniformly in theta, where p is a nonzero trigonometric polynomial, has degree≤floor(alpha). Its displayed unnormalized coefficient integral tends to2πc_ka_q, not c_ka_q.',
 'proof sketched; normalization computation false as printed','E',
 'The corrected conclusion follows from the coefficient extraction proved in proof_checks.md. Searches for the weighted formulation and original exercise provenance found general vector-valued Liouville and functional-calculus literature, but no exact source identification. The method is elementary Cauchy/Fourier theory; it is not labelled a new Grothendieck theorem.',
 'Classical complex-analysis method predates programme; exact reused exercise edition unidentified.', ['KurbatovKurbatovaOreshina2016'],calc='C36 Fourier normalization; general finite-sum extraction derived in proof_checks.md.')
add(37,[38],[50],'91','Prouver de même ... degré<α',
 'For integer alpha, the weighted uniform little-o(r^alpha) condition implies degree<alpha. Pointwise little-o together with the preceding uniform big-O dominating bound also suffices by dominated convergence. The page does not specify which mode is meant.',
 'stated without proof as an exercise; uniformity implicit','C',
 'The corrected sufficient formulations follow from the same exact Fourier extraction. Targeted searches of the weighted Liouville statement did not identify the exercise edition or a theorem resolving the strongest undominated raywise reading. The ambiguity is retained rather than replaced by an unproved stronger assertion.',
 'Classical method; exact exercise provenance unresolved.', ['KurbatovKurbatovaOreshina2016'],confidence='medium',calc='C36 coefficient formula used at q=alpha; proof_checks.md explains domination.')
add(38,[39],[50],'93','Alors x^n=0',
 'For a quasinilpotent x in a unital Banach algebra, the uniform weighted little-o growth bound with cos(theta)^n for (1−lambda x)^−1 implies x^n=0. The element inside the resolvent must be x, not an unrelated z.',
 'proof sketched by reference to preceding exercise','E',
 'The resolvent is entire and its Taylor coefficients are x^j, so the checked weighted Liouville argument proves this exact qualified statement. Pseudo-resolvent/functional-calculus sources confirm the underlying resolvent convention; no exact original exercise provenance was found.',
 'Classical resolvent and Liouville theory; provenance unidentified.', ['KurbatovKurbatovaOreshina2016'],calc='C36 Fourier extraction plus coefficients x^j; the analytic uniformity requirement is explicit.')
add(39,[40,41],[50],'95','norm a_n=o|O(n^α); degré<α+1',
 'The strict pole-degree bound is incompatible with the big-O reading. f(z)=(z−1)^−2 has inside coefficients n+1 and outside coefficients n−1 for n≥2, both O(n), but pole degree2. Little-o coefficients yield the epsilon boundary estimate after a finite/tail split.',
 'false as stated under big-O alternative; little-o reading undecided','C',
 'Exact scalar expansions and the hypotheses are checked in this run. The little-o boundary estimate is independently reproved; the truncated final exercise is not reconstructed as a complete theorem. Searches of weighted Liouville/pseudo-resolvent/factorization literature did not identify this exercise’s printed source.',
 'Elementary power-series theory; run check2026-11-19.', ['KurbatovKurbatovaOreshina2016'],calc='C39 exact inside/outside expansions; proof_checks.md finite/tail estimate.')
add(40,[42],[50],'95','(1−r^−1)^−1≤9R/(4cosθ)',
 'For z=(w−1/2)/(w+1/2), R=|w|≥1, the inside estimate has denominator cosθ>0. The outside estimate requires −cosθ or |cosθ|. At w=−2 the literal outside assertion reads5/2≤−9/2.',
 'false as transcribed; sign reading question','E',
 'The exact rational counterexample and the corrected general norm estimate are independently checked. The original anonymous exercise provenance was not found in the targeted complex-analysis/factorization search; no historical novelty is asserted.',
 'Elementary Cayley-transform algebra; rechecked2026.', [],calc='C40 rational counterexample; general factor9/4 bound in proof_checks.md.')
add(41,[43],[50],'95–96','et montrer que',
 'The exercise stops before specifying its final requested conclusion after the Cayley substitution. The preceding estimates are identifiable, but the missing assertion itself is not.',
 'open on the pages only in the sense of a truncated exercise, not an authorial conjecture','F',
 'Searches by the weighted-pole/Liouville statement and adjacent Cohen-factorization exercises did not identify the exact edition or continuation. The mathematical plausibility of a completion is not evidence for its wording.',
 'No provenance/date identified.', [],confidence='high')
add(42,[51],[52],'124–128','|lambda−lambda0| norm R(lambda)<1',
 'The local Neumann expansion needs |lambda−lambda0|·normR(lambda0)<1. The literal moving-point bound fails for R(lambda)=1/lambda on C*, lambda0=1,lambda=3: its bound2/3 is satisfied but series terms are(−2)^n.',
 'false as transcribed; corrected mathematical hypothesis identified','E',
 'Kurbatov–Kurbatova–Oreshina Theorem16/Corollary17 gives the exact local expression and expansion. Our scalar counterexample checks every hypothesis; the corrected Neumann argument is reproved in proof_checks.md. Original exercise edition remains unidentified.',
 'Classical resolvent theory; exact modern source arXiv2016-04-25.', ['KurbatovKurbatovaOreshina2016'],calc='C42 bound and divergent terms; corrected general proof in proof_checks.md.')
add(43,[53],[52],'131','d^nR/dlambda^n=(−1)^n n!R^(n+1)',
 'Every Banach-algebra pseudo-resolvent on an open domain is analytic and satisfies the displayed derivative identity for every n≥0, with no continuity hypothesis needed beyond the resolvent identity and the algebra topology.',
 'stated without proof as an exercise','E',
 'The local resolvent identity implies the convergent Neumann expression, then R′=−R² and induction. Kurbatov–Kurbatova–Oreshina Corollary17 is an exact modern reference, traced there to standard resolvent theory.',
 'Classical; opened modern formulation2016.', ['KurbatovKurbatovaOreshina2016'],calc='C43 symbolic derivatives orders0–6; all-order induction in proof_checks.md.')
add(44,[54],[52],'133','z²=0; j²=j; x∈jAj',
 'A pseudo-resolvent holomorphic at infinity has R(lambda)=z+j(lambda e−x)^−1, with z²=0,j²=j,zj=jz=0,x∈jAj. Its Laurent coefficients are c0=z,c1=j,c2=x,c_n=x^(n−1) for n≥2.',
 'proof sketched by Laurent coefficient comparison','E',
 'Kurbatov–Kurbatova–Oreshina Proposition23 states the exact same decomposition, with N=−z. The universal coefficient comparison is independently supplied in proof_checks.md. The saved matrix calculation is only a nontrivial example, expressly not a universal certificate.',
 'Classical pseudo-resolvent theorem, contemporary formulation arXiv2016.', ['KurbatovKurbatovaOreshina2016'],calc='C44 block example plus general Laurent coefficient derivation in proof_checks.md.')
add(45,[55],[52],'135','si et seulement si R(lambda0) inversible',
 'A pseudo-resolvent in a unital Banach algebra is the restriction of the resolvent of an element x iff it is invertible at one point; x=lambda0 e−R(lambda0)^−1, independent of the chosen point.',
 'stated without proof as an exercise','E',
 'Kurbatov–Kurbatova–Oreshina Proposition18 states this criterion. The two-sided inverse calculation follows directly from the resolvent identity and is independently checked in proof_checks.md; disconnected open domains cause no exception because the defining identity relates every pair of points.',
 'Classical; opened exact formulation2016.', ['KurbatovKurbatovaOreshina2016'])
add(46,[56],[52],'137','la fonction ... satisfait à(1)',
 'For x in a unital Banach algebra, sum_(n≥0)(lambda0−lambda)^n x^(n+1) is a pseudo-resolvent on |lambda−lambda0|·normx<1. It need not be an actual resolvent unless x is invertible.',
 'stated without proof as an exercise','E',
 'The convergent expression is x[1+(lambda−lambda0)x]^−1; its Hilbert identity is a polynomial identity in the commutative algebra generated by x. This matches the local construction in Kurbatov–Kurbatova–Oreshina Theorem16.',
 'Classical; exact source2016.', ['KurbatovKurbatovaOreshina2016'],calc='C46 universal rational identity; norm convergence separately justified.')
add(47,[57],[52],'139','norm(yw−u)<epsilon',
 'The printed conclusion fails for B=C,u=1,w=2,C=2,epsilon=1/2,gamma=0, regardless of eta. Replacing yw−u by yw−w gives the valid estimate norm(yw−w)≤2gamma·norm(uw−w) under the stated small-gamma bound and normalized unit norm.',
 'false as transcribed; likely target-symbol error','E',
 'The exact counterexample and corrected estimate are independently checked. de Jeu–Jiang Proposition3.8 provides the same inverse-approximation mechanism in modern factorization proofs; the original exercise provenance is not identified.',
 'Elementary perturbation estimate; factorization1959; exact modern comparison2016/2017.', ['deJeuJiang2017'],calc='C47 scalar counterexample; Neumann norm estimate in proof_checks.md.')

add(48,[],[44,45],[K+'321–372'],'Théorème de déformation pour les schémas abéliens',
 'For an arbitrary scheme S and a thickening S′ with locally nilpotent divided powers, the category of abelian schemes over S′ is equivalent to pairs of an abelian scheme A/S and a locally direct-summand lift of its Hodge filtration in D*(A) evaluated at S′. This is the unpolarized statement; no prime p is singled out.',
 'stated without proof; quasi-inverse construction deferred to universal extensions','A',
 'The exact theorem appears in GrothMontreal1974 ChapterV§4 printedp116, with the same arbitrary-base and locally nilpotent-PD hypotheses, followed by the universal-extension route onpp117–118. The p-nilpotent case is also obtained from the qualified BT theorem and Serre–Tate. The publication is an exact match to the assertion, not an independent proof supplied by this audit; modern support for the universal-extension construction is documented in de Jong1995 and Fonseca–Matthes2022.',
 'Montréal course1970, publication1974; manuscript composition date not inferred.', ['GrothMontreal1974','GrothICM1970','Katz1981','deJong1995','FonsecaMatthes2022'],present='Exact own-published deformation theorem identified. The unrestricted characteristic formulation is kept separate from the p-nilpotent BT equivalence and from polarized deformations.')
add(49,[],[46],[K+'394'],'un seul schéma en groupes lisses E′ ... isomorphisme unique',
 'In characteristic zero, the smooth group E(A), the universal vector extension of an abelian scheme, is asserted to admit a unique marked smooth-group lift across an infinitesimal thickening, and by passage to limits across a nil-thickening. The mark identifies the special restriction with E(A); an unmarked object can have automorphisms.',
 'stated without proof; attributed to an earlier letter to Tate','A',
 'GrothMontreal1974 ChapterV§4 p117 repeats the exact rigidity assertion and the letter attribution. Fonseca–Matthes2022 Theorem2.1 gives Rg_*O_E=O_S in characteristic zero and §§3.2–3.3 constructs the canonical D-group structure, providing modern precise parts of the crystalline-rigidity framework. This audit did not collate the earlier letter or independently establish the full nil-thickening uniqueness theorem from that vanishing.',
 'Exact publication1974 from course1970; earlier letter date not determined by this sentence. Modern preprint17January2022.', ['GrothMontreal1974','FonsecaMatthes2022','IllusiePisa2013'],confidence='medium',present='Exact own-published formulation found; modern crystalline rigidity framework identified. Strong all-nil-thickenings uniqueness is carried from the published statement, not claimed as a new proof here.')

# Euler and Postnikov: separate source assertions from earlier-run inferences.
add(50,[77,78],[56,66],'202–215;578','faisceautique [deleted]; singulière; si X compact',
 'The retained convention is singular cohomology. For compact X, compact-support singular cohomology defined by the direct limit over compact K⊂X of H*(X,X−K;k) equals H*(X;k), since K=X is terminal. General comparison with sheaf cohomology requires further local hypotheses.',
 'proved there for compactness; cohomology convention corrected by himself','E',
 'The compact equality is definitional and independently checked here. Verdier1973 §1 pp441–442 states the sheaf-theoretic compact-support Euler framework and its finiteness hypotheses; Hatcher2002 gives singular cohomology. These are compatible on the intended locally contractible finite-dimensional spaces, but the source correction cannot be erased on arbitrary locally compact spaces.',
 'Standard support formalism; no manuscript date inferred; exact published comparison framework1973.', ['Verdier1973','Hatcher2002'])
add(51,[79,108],[56,66],'217–221;580','chi_!(X)=chi_!(Y)+chi_!(X−Y)',
 'For a closed Y⊂X in a compact-support theory admitting the closed/open exact sequence, two of X,Y,X−Y having bounded finite-dimensional cohomology implies the third does, and chi_c(X)=chi_c(Y)+chi_c(X−Y). The first ambiguous alternative Y−Y in the summary must be checked on the ink.',
 'proof sketched from the long exact sequence; topological comparison hypotheses implicit','E',
 'Verdier1973 §1 prints the exact closed/open statement in sheaf cohomology. Alternating-sum cancellation is independently proved in proof_checks.md. It supplies a precise established refinement; it is not a proof that every literal singular-cohomology version on all locally compact spaces has the required sequence.',
 'Classical cohomological additivity; primary formulation1973.', ['Verdier1973','Hatcher2002'],present='Established in the stated support formalism and in the later finite-cell/conical setting after comparison; the unrestricted singular version remains underqualified.')
add(52,[80,109],[56,66],'223–232;582','X′,X″ fermés dans X de réunion X',
 'For an excisive cover X=X′∪X″ the Mayer–Vietoris sequence gives chi(X)=chi(X′)+chi(X″)−chi(X′∩X″), with the corresponding compact-support statement when its exact sequence exists. Three finite total cohomology groups imply the fourth; finiteness of X and X′∩X″ also implies finiteness of both pieces. Mere closedness is insufficient for singular excision.',
 'proof sketched; final summary omits the cover hypothesis','E',
 'Hatcher Theorem2.20 and the Mayer–Vietoris section establish the excisive form. The stronger finiteness follows degreewise by exactness. The literal summary without a cover is refuted by X=S¹ and X′=X″={point}: 0≠1+1−1. This counterexample satisfies closedness and all finiteness hypotheses.',
 'Classical singular/cohomological excision; exact textbook formulation2002.', ['Hatcher2002'],calc='C52 numerical Euler values; universal exact-sequence argument in proof_checks.md.')
add(53,[82,110],[56,66],'234–244;586–588','dominé homotopiquement; X sim X′',
 'If X is homotopy dominated by Y then H*(X;k) is a direct summand of H*(Y;k), so finite total cohomology descends. Homotopy equivalence preserves ordinary Euler number. Compact-support invariance needs a proper homotopy equivalence; arbitrary homotopy equivalence is insufficient.',
 'proof sketched; stronger support-equivalence notation not defined','E',
 'Hatcher Theorem2.10 proves ordinary homotopy invariance. Functoriality gives the split injection for domination. R≃point but chi_c(R)=−1≠1 refutes unrestricted compact-support invariance; both spaces meet the later conical-at-infinity finiteness conditions. The distinct printed equivalence symbols should not be normalized into one assertion.',
 'Classical; modern exact reference2002.', ['Hatcher2002'],calc='C53 compact-support counterexample values and direct-summand proof.')
add(54,[83,84,85,86,135],[56,58,66],'247–251;286–314;592','chi(pt)=1; chi(S^n)=1+(−1)^n',
 'For n≥0, chi(empty)=0, chi(point)=1, finite disjoint unions add, chi(R^n)=1, chi_c(R^n)=(−1)^n and chi(S^n)=1+(−1)^n. The ordinary symbol in the last Euclidean calculation must be the compact-support one for odd n; compactness invokes axiom a rather than b.',
 'proved there by hemispherical induction; final support symbol false as transcribed','E',
 'The sphere recurrence and base case are checked for all n by induction; compactification gives the Euclidean support value. Hatcher cellular homology and Theorem2.44 are exact classical counterparts; Morin1962 §2 treats R^n as a one-cell relative complex for compact supports.',
 'Standard Euler theory; compact-support cellular source1962; textbook2002.', ['Hatcher2002','Morin1962'],calc='C54 recurrence and ordinary/support values for n=0..8; general induction in proof_checks.md.')
add(55,[87],[58,66],'316–320;623–625','filtration de l’espace X',
 'For a finite closed filtration whose successive strata are f_i copies of R^i, chi_c(X)=sum_i(−1)^i f_i. Closedness/excision of the filtration is a necessary part of the precise modern statement.',
 'proof sketched by induction; filtration qualification implicit','E',
 'Morin1962 §2 Lemma1, printedpp45–46, computes compact-support cohomology by cellular cochains; the formula follows by Euler cancellation. Hatcher Theorem2.44 is the compact CW counterpart. This run gives the finite-filtration proof; it does not extend the formula to an arbitrary partition into cells without frontier/excision conditions.',
 'Finite cellular Euler theory classical; explicit opened local-coefficient compact-support source1962.', ['Morin1962','Hatcher2002'])
add(56,[88,89],[60,66],'354–361;597–598','Künneth pour H_*; pour H^*_!',
 'Over a field k, finite total ordinary cohomology of X and Y implies the product has finite total cohomology and chi(X×Y)=chi(X)chi(Y), using homological Künneth and then duality. Compact-support multiplicativity holds when its Künneth comparison applies; in particular for finite relative cellular spaces.',
 'proof sketched using Künneth; support-theory hypotheses implicit','E',
 'The ordinary homological product theorem in Hatcher, chapter3 Künneth discussion, has no dual-of-infinite-tensor gap when homology is finite-dimensional. Morin1962 §2 gives product cells of dimensions r+s and the cellular support complex, which proves the finite relative-cell form. The broad arbitrary-space support assertion is not inferred from that cell proof.',
 'Classical Künneth/cellular Euler formula; opened1962 and2002 formulations.', ['Hatcher2002','Morin1962'],calc='C56 finite Euler polynomial products; general tensor-complex argument in proof_checks.md.')
add(57,[90,91,96],[60,62,66],'363–398;454–465;602–610','chi(X)=chi(Y)chi(F); sous réserve',
 'The provisional ordinary fibration formula assumes locally trivial X→Y with fibre F and finite constant-coefficient total cohomology. These conditions alone do not imply multiplicativity; finite cohomology for the intervening local systems is an additional issue.',
 'proof sketched conditionally; narrowed by himself on scan66 to relative-polyhedral bases','C',
 'The finite-cell version is standard and appears in C-SA04-58. The earlier notes’ locally finite RP^n telescope supplies a complete counterexample to the broad version: Y≃K(C2,1), its contractible double cover X and two-point fibre are locally compact, all have finite rational total cohomology, yet 1≠1·2. The local-system failure is C-SA04-59. Searches located the classical cell/spectral-sequence framework, not a theorem validating the broad quantifiers.',
 'Classical refined theorem; counterexample independently checked2026-11-19.', ['Hatcher2002','Morin1962'],calc='C57 finite-group rational averaging and Euler values; full telescope hypothesis check in proof_checks.md.',present='Broad constant-coefficient version false; later finite-type refinement established. This is not a counterexample to the final conical-end question.')
add(58,[90,91],[60,66],'363–398;602–610','tout au moins si Y est un polyèdre relatif',
 'For a locally trivial fibration with finite-total-cohomology fibre and a base of finite CW homotopy type, the ordinary Euler number multiplies. A compact-support version holds with the appropriate locally constant direct images, finite relative-cell base and finite compact-support fibre cohomology. The all-conical-base extension is explicitly questioned.',
 'proof sketched through a finite spectral sequence; final broader question open on pages','B',
 'Morin1962 Lemma1 gives the needed local-system cellular calculation; the finite bounded spectral sequence then proves the formula. West1977 Corollary5.3 supplies finite CW homotopy types for compact metric ANRs, so our specified recursive conical interpretation and compact-core retraction also yield the ordinary extension. This modern completion uses hypotheses the manuscript leaves in its recursive definitions; the general compact-support direct-image comparison is a separate input.',
 'Cellular framework1962; finite-ANR theorem1977; conditional reconstruction2026.', ['Morin1962','West1977','Hatcher2002'],present='Established finite-type ordinary theorem; conditional conical completion under the explicit compact-metric recursive interpretation. No unqualified compact-support theorem for arbitrary locally compact fibrations is asserted.')
add(59,[92,95,96],[60,62],'392–411;452–465','chi(Y,F)=b chi(Y)',
 'A rank-b local system on a finite relative cellular space has compact-support Euler number b chi_c(Y). The ordinary identity holds on finite CW homotopy types. It fails if finite constant-coefficient cohomology is the only finiteness condition.',
 'proof sketched for compact supports by cells; ordinary extension qualified and deferred','E',
 'Morin1962 §2 Lemma1 is an exact primary local-coefficient cellular statement. A finite cellular complex has b times as many coefficient dimensions; alternating cancellation proves the identity. On the rational RP^n telescope the sign local system has zero cohomology by finite-group averaging, while rank1 times ordinary chi is1, checking the missing-hypothesis warning.',
 'Classical cellular theorem; explicit primary compact-support source1962.', ['Morin1962','Hatcher2002'],calc='C59 group-cohomology values; finite-cell proof in proof_checks.md.')
add(60,[94],[62],'448–450','recouvrements arbitrairement fins finis',
 'A compact base with arbitrarily fine finite covers whose finite intersections have finite support cohomology is proposed as an alternative to a cell filtration. To use it, covers must be excisive and refined to trivialize the given local system, and the associated finite cover spectral sequence must compute the chosen cohomology.',
 'stated without proof; exact cover-condition label doubtful','C',
 'Morin1962 verifies the finite-cell sufficient condition and Verdier1973 gives the support formalism, but neither proves the exact terse arbitrary-fine-cover criterion as written. Under an excisive cover resolving the sheaf and trivializing coefficients, the finite Čech double complex proves the Euler statement; absent those conditions the page’s wording remains incomplete. Searches of Numdam and general primary sources did not identify a uniquely matching theorem.',
 'Classical cover spectral sequences; exact source formulation unmatched as of2026-11-19.', ['Morin1962','Verdier1973'],confidence='medium')
add(62,[98,102],[62],'471–500','X est loc. contractile',
 'Under the compact-Hausdorff recursive cone convention with finite recursive dimension and compact links, compact conical spaces are metrizable, locally contractible finite-dimensional ANRs and consequently have finite CW homotopy type and finite cohomology over every field. Infinite discrete spaces do not belong to the compact finite base class.',
 'proof sketched by induction/local contractibility; notation C versus E ambiguous','B',
 'West1977 Corollary5.3 proves compact metric ANRs have finite-polyhedral homotopy type. The recursive chart argument supplies the prerequisites in the explicitly stated interpretation. It gives homotopy finiteness, not triangulability of the original space. The manuscript’s varying C/E notation prevents treating the modern compact convention as a transcription decision.',
 'West1977; no date assigned to manuscript.', ['West1977'],confidence='high')
add(63,[100,130],[62],'483–491','1-complexes topologiques; loc. triangulables',
 'Finite zero-dimensional compact links give finite-star one-dimensional cone charts; cones on compact finite graphs give local two-dimensional triangulations. Global triangulation of arbitrary compact singular two-dimensional members and the ensuing local higher-dimensional assertions need separate compatible-link arguments. The compact dimension-three clause is deleted in Pro.',
 'some elementary local implications sketched; global dimension-three clause withdrawn in same text','C',
 'The elementary finite-star/cone implications are directly checked. Manolescu2015 §2.2 verifies Moise’s manifold dimension-three theorem and separates the dimension-four failure, but that theorem does not establish the general singular recursive-link claims. The exact broad singular low-dimensional classification was not identified in the opened primary sources; neither positive nor negative global verdict is fabricated.',
 'Moise1952 as documented in Manolescu2015; exact singular extension unmatched.', ['Manolescu2015'],confidence='medium')
add(64,[101],[62],'491–493','pas clair qu’ils sont triangulables',
 'Does every compact four-dimensional locally conical space admit a triangulation? Even the subclass of closed topological four-manifolds gives a negative answer.',
 'open on the pages','B',
 'Manolescu2015 §2.2 records Freedman’s E8 manifold and Casson’s obstruction to its triangulation. It is compact and a topological manifold, so every point has an R4 chart, itself a cone on S3. These check its membership in the source’s locally conical class. The obstruction is used from the literature, not reproved by the chart check.',
 'E8 manifold1982; Casson nontriangulability attribution documented in2015; precise first circulation of Casson argument not established here.', ['Manolescu2015'],present='Negative answer established; not a refutation of a manuscript theorem, since the page expresses doubt.')
add(65,[103],[62,66],'500–503;618','chi_!(X)=chi(hat X)−1',
 'For X=hat X−{omega}, where hat X is a compact finite-cohomology conical compactification and the closed/open comparison is valid, X has finite compact-support cohomology and chi_c(X)=chi(hat X)−1.',
 'proved there by closed/open additivity','E',
 'This is the one-point instance of Verdier1973 §1 additivity; the finite-dimensionality follows from its long exact sequence. West supplies a sufficient finite-cohomology condition for the intended compactification. No end-link smoothness or orientability is required.',
 'Classical compact-support additivity; exact opened source1973.', ['Verdier1973','West1977'])
add(66,[104],[64],'527–531','On vérifie; vérifier',
 'Removing an open half-cone around the compactification vertex leaves a compact core in the recursive conical category, provided that category is closed under the link/join constructions in its cone charts.',
 'self-flagged step; proof omitted','C',
 'The local boundary model is a link chart times a half interval; products of cones are cones on joins. This run checks that local construction and compactness. West’s theorem then applies if the recursive compact-metric interpretation is retained. The literature search found no exact named theorem fixing the manuscript’s ambiguous C/E recursive class, so this is an explicit reconstruction rather than a universal claim about every possible reading.',
 'Elementary cone construction; ANR consequence1977; reconstruction2026.', ['West1977'],confidence='medium')
add(67,[105],[64],'533','X′ sim X',
 'The punctured compactification strongly deformation retracts onto the truncated core: in a cone chart the radial coordinate is sent to (1−t)r+t max(r,1/2), and outside the collar the map is the identity.',
 'stated without proof; radial argument indicated','E',
 'The formula is continuous, positive for r>0, fixed for r≥1/2, and therefore glues to the identity. This supplies an independent proof of the exact local-topological statement. Hatcher’s homotopy invariance theorem supplies its cohomological consequence; searching produced no need for a later special theorem.',
 'Elementary deformation-retract argument; checked2026-11-19.', ['Hatcher2002'],calc='C67 radial endpoint/fixedness checks; general continuity and gluing in proof_checks.md.')
add(68,[106],[64,66],'535–546;619','chi(X)−chi_!(X)=chi(S_omega)',
 'With a compact finite-cohomology core, an end cone and an excisive intersection equal up to homotopy to the compact link S_omega, ordinary minus compact-support Euler number equals chi(S_omega).',
 'proved there from Mayer–Vietoris and the proposed core properties','E',
 'The exact-sequence identities in C-SA04-51/52, the contractible cone and radial retraction prove the displayed formula. Verdier’s additivity and Hatcher’s homotopy invariance are the primary formal inputs. R^n gives 1−(−1)^n=chi(S^(n−1)), with the zero-dimensional convention treated separately. The formula is not asserted for nonconical ends.',
 'Standard end/core consequence of Euler theory; checked2026.', ['Verdier1973','Hatcher2002'],calc='C68 Euclidean end examples; universal core/cone proof in proof_checks.md.')
add(69,[111],[66],'623–625','uniquement déterminées',
 'On finite relative polyhedra the first five axioms and point normalization determine the Euler functions, using finite cell decompositions, compact comparison and the finite compact-core argument for ordinary cohomology.',
 'proof sketched by finite filtration','E',
 'Finite-cell induction is supplied in proof_checks.md; Morin1962 Lemma1 and Hatcher Theorem2.44 identify the resulting value with cohomological Euler characteristic. Infinite polyhedra without a finite type assumption are outside this proof.',
 'Classical cellular Euler characterization; sources1962/2002.', ['Morin1962','Hatcher2002'])
add(70,[113],[66],'627','j’ignore si ... caractérisés ... tout E_infinity',
 'Do the first five axioms uniquely characterize the two Euler functions on the full intended conical-at-infinity category? A sufficient modern formulation uses compact metric recursively conical compactifications and cores of finite CW homotopy type.',
 'open on the pages; existence is asserted separately, not uniqueness','B',
 'Under the explicit compact-metric recursive interpretation, West Corollary5.3 gives finite-polyhedral homotopy models of compactification and core. Ordinary homotopy invariance fixes their values, and closed/open subtraction fixes compact supports. This is a conditional modern solution assembled here, not a located published theorem with the manuscript’s notation. A broader reading lacking these ANR hypotheses is not claimed settled.',
 'West1977 input; reconstructed proof2026-11-19.', ['West1977','Morin1962','Hatcher2002'],confidence='medium',present='Affirmative under the stated recursive interpretation; the exact class must be fixed before assigning an unconditional answer to the handwritten question.')
add(71,[115],[56,58,66],'202;318;625','k corps',
 'For finite relative cellular spaces, and for spaces whose Euler number is identified with a finite CW model, the Euler number is independent of the coefficient field. Betti numbers and membership in broader finite-cohomology classes may depend on the field.',
 'unpursued implication; statement belongs to earlier notes, not an explicit source assertion','E',
 'The integral alternating cell count proves field independence, as in Hatcher Theorem2.44 and Morin Lemma1. This inference is included to audit its use, expressly separated from claims written by the author.',
 'Classical cell formula; earlier-run implication rechecked2026.', ['Hatcher2002','Morin1962'])
add(72,[116],[62],'497–500','espaces loc. côniques',
 'A finite simplicial homotopy model yields a finite face-poset model through its order complex, the barycentric subdivision. This does not bound a smallest model or identify it with the original space homeomorphically.',
 'unpursued implication proposed by earlier notes','B',
 'West supplies the finite-polyhedral homotopy model under compact-ANR hypotheses; the face-chain description of barycentric subdivision supplies the poset model. The cross-project minimality suggestion has no proof in the source and is kept as a separate project lead.',
 'Finite-model input1977; earlier-run inference checked2026.', ['West1977','Hatcher2002'],confidence='high')

add(80,[122,124],[83],'1607–1610','k1 in H³(pi1(X),pi2(X)) ?=0',
 'The ambient H³ group need not vanish even for an infinite loop space: X=K(C2,1)×K(C2,2) has first Postnikov invariant zero but H³(C2;C2)=C2. The grammar of the handwritten question does not decide whether the zero concerns the class or its containing group.',
 'open on the pages; group-vanishing reading false','E',
 'The normalized finite group-cochain enumeration here is complete and gives the nonzero group. Baues–Conduché §5.1–5.2 locates the first k-invariant in precisely this cohomology group and classifies two-types by it. The product’s k-class is zero by its product construction. This counterexample verifies the earlier-run interpretation warning, not the ink.',
 'Classical group cohomology; checked example2026; exact primary two-type formulation1995.', ['BauesConduche1995'],calc='C80 complete normalized C2 cochain enumeration in degrees2–4.')
add(81,[122,125],[83],'1611–1626','exists k′1 in H4(K(pi1(X),2),pi2(X))',
 'For a connected loop CW-type, the first Postnikov invariant is a cohomology suspension from the first relevant invariant of its delooping. An additional compatible delooping is needed for the next displayed lift; one loop hypothesis does not imply the whole tower.',
 'proof sketched by a diagram; iteration hypotheses unstated','B',
 'Arlettaz2000 §7 Lemma7.4, Proposition7.5 and Theorem7.6 spell out the suspension mechanism and its double-loop consequence. Baues–Conduché §§4.5–4.7 realizes the same passage by reduced quadratic modules and crossed modules. These exact statements explain both what the diagram supports and why a single-loop vanishing conclusion is too strong.',
 'Double-loop result published1990; detailed survey2000; algebraic modelpreprint1995.', ['Arlettaz2000','BauesConduche1995'])
add(82,[126],[83],'1613–1615','H5(K(pi1(X),3),pi2(X))',
 'The first Postnikov invariant of a connected double loop space vanishes; its two-type is a product K(pi1,1)×K(pi2,2). The whole space need not split, and its ambient H³ group need not vanish.',
 'unpursued implication of two compatible lifts; stronger than the top-line single-loop hypothesis','B',
 'Arlettaz2000 Theorem7.6 and Corollary7.7 state the exact vanishing and two-type splitting, using Proposition7.5 on double cohomology suspension. The survey cites Arlettaz1990, The first k-invariant of a double loop space is trivial, Arch.Math.54,84–92. The original DOI fetch failed, so the 1990 work is bibliographically checked through the opened primary survey, not independently read.',
 'Publication1990; survey2000; exact preprint-first-circulation date not established.', ['Arlettaz2000','Arlettaz1990'],present='Established with the double-loop hypothesis; no conclusion of a natural splitting is added.')
add(83,[127],[83],'1607–1610','X=Omega Y',
 'A connected single-loop space can have a nonzero first k-invariant. The earlier-run model has M=Z, L=Z⊕C4, boundary(m,b)=2m and quadratic w(x,y)=(0,xy mod4); its associated crossed module has pi1=C2,pi2=C4 with trivial action and k represented by value2 on(1,1,1).',
 'counterexample supplied by earlier notes to one possible reading, not written by the author','B',
 'All reduced-quadratic identities are checked algebraically and the complete normalized C2 cochain enumeration verifies the cocycle is nonzero. Baues–Conduché §4.5 and commutative diagram4.7 identify the corresponding simply connected3-type and its loop2-type. That realization theorem is used, not computationally certified. The counterexample establishes the single/double distinction.',
 'Algebraic realization primary preprint1995; example rechecked2026-11-19.', ['BauesConduche1995'],calc='C83 full finite cohomology check plus universal reduced-quadratic identities in proof_checks.md.')
add(84,[129],[83],'1610–1615','k1',
 'Even when a double-loop two-type splits, one cannot in general choose such a splitting naturally in the delooped space. This is a caution introduced by the earlier notes, not an authorial question on this page.',
 'unpursued implication of the earlier run','B',
 'Baues–Conduché Theorem1.9 gives the exact obstruction to natural splitting of the loop-type functor. Its hypotheses and target are a naturality assertion, distinct from Arlettaz’s objectwise two-type decomposition.',
 'MPIpreprint95-112,1995; later publication date not established in this audit.', ['BauesConduche1995','Arlettaz2000'])

add(120,[136,143,149,150],[72,73],'716–800;834–855','G(f,g)+G(g,h)=G(f,h); isomorphisme',
 'For local étale coordinates on a smooth complex analytic curve, G(f,g)=−2(S(g)−S(f))dt² is a natural quadratic-differential cocycle invariant under constant homographies. Equal G with a common reference gives equality up to a constant homography, and matching2-jets gives equality on a connected domain. The quotient sheaf of projective coordinates is a torsor under quadratic differentials; local surjectivity follows from the Schwarzian differential equation.',
 'stated without proof; formula supplied on73, torsor sign conventions differ between72 and73','E',
 'Deligne1970 I§5, Lemma5.2, Proposition5.8 and §§5.9–5.12 give the exact projective-connection, quadratic-torsor and differential-equation descriptions. His theta=S/6, so the source normalization is G=−12theta for a single coordinate. Dumas2009 §3.1–3.2 states the standard equation u″+(q/2)u=0 whose solution ratio has Schwarzian q. Classical Schwarzian theory predates this undated leaf; the 1969 seminar date belongs to Deligne’s text, not the manuscript.',
 'Classical; Deligne Harvardseminar autumn1969, publication1970; Dumaspreprint2009.', ['Deligne1970','Dumas2009'],calc='C120 universal Schwarzian/Hasse composition and Möbius zero; analytic ODE argument in proof_checks.md.',present='Established locally as sheaf/torsor statements; no global solution or preferred section is implied.')
add(121,[137,141],[72,73],'747–754;774–777;802–831','G′=phi G; il suffit de supposer d)',
 'Classify every rational finite-order differential cocycle on analytic coordinate sheaves satisfying the printed projective rigidity/naturality conditions as a nowhere-zero scalar multiple of G; under full étale naturality the scalar is universal. The source also claims only first-jet denominators are needed and local-surjectivity axiom e follows from d.',
 'stated without proof; denominator reduction and redundancy explicitly self-flagged','C',
 'Bouarroudj–Ovsienko1998 §1.2 proves the familiar unique smooth Diff+(S1) quadratic-differential cocycle vanishing on PSL2, and Ovsienko1993 recalls the real-line continuous-cohomology formulation. Those categories and regularity assumptions do not by themselves prove the manuscript’s rational local-complex-sheaf classification. A universal polynomial localization proves the denominator conclusion once pole support and arbitrary jet realization are specified. Searches, including backward references and the2025 MathOverflow discussion, did not identify an exact theorem covering every printed quantifier or e-from-d. This is a literature-match gap, not a claim of worldwide openness.',
 'Classical relative Schwarzian cohomology; sources1993/1998; exact matching search2026-11-19.', ['BouarroudjOvsienko1998','Ovsienko1993','Deligne1970'],confidence='medium',present='Existence/torsor theory established; exact admissible-operator classification and redundant-axiom claim require a separate precise proof or reference.')
add(122,[153,158],[73],'883–928','G0=1/12 G; D_t^(n)',
 'For Hasse derivatives over any commutative base with invertible first jets, Q(f)=−D3f/D1f+(D2f/D1f)² gives G0(f,g)=(Q(g)−Q(f))dt², an integral projectively invariant quadratic cocycle. In characteristic0 G=12G0. The square test is1/(4t²), not the printed1/(2t), on2t invertible. The cube test2/(3t²) is on3t² invertible and vanishes in characteristic2. Nonzero tests in characteristics2/3 are t+t² and t+t³ respectively.',
 'formula stated and tests computed; square test false as transcribed','B',
 'The universal Hasse-jet identity is independently reduced to zero over the integral localized polynomial ring, so reduction in every characteristic is justified. Deligne I§5.9 gives the characteristic-zero version theta=−Q and fixes factor12. Searches on Hasse/Schwarzian/integral natural operators located no primary all-base uniqueness theorem; this claim is the verified construction only, while uniqueness is C-SA04-123 and the later coherent-target assertions belong to C-SA04-201 onward.',
 'Classical characteristic-zero normalization1970; exact integral identity and special-characteristic tests checked2026-11-19.', ['Deligne1970'],calc='C122 integral composition, homography identity, factor12, square/cube and characteristic2/3 certificates; all in saved program/output.')
add(123,[152],[73],'888–897','coefficients dans Z; unicité au signe près',
 'Among the author’s unspecified class of all-base natural integral Hasse differential operators with the stated universal property, G0 should be unique up to a unit of Z, hence up to sign. The conclusion requires classification of all such operators and a precise target/category; nonzero examples alone prove neither.',
 'stated without proof; integral classification asserted','C',
 'The opened classical Schwarzian literature establishes characteristic-zero projective cocycles and the group-cohomological smooth analogue. Deligne’s 1/6 normalization explains the primitive integral candidate but does not classify all base-natural operators. Searches in arXiv, Numdam, the referenced bibliography and the2025 uniqueness discussion found no exact all-base universality theorem with these quantifiers. Fixed-characteristic and coherent-target versions have further qualifications recorded by the companion audit; this exact global formulation remains a reference/proof gap in this dossier.',
 'Exact integral formulation undated in manuscript; searched as of2026-11-19.', ['Deligne1970','BouarroudjOvsienko1998'],confidence='medium',present='Integral construction established by C-SA04-122; the proposed universal uniqueness is not certified, and no assertion of general research openness is made.')

# Exact publication collation performed after the initial claim register.
for _c in claims:
    _n=int(_c['id'].rsplit('-',1)[1])
    if _n in {1,3,4,5,6,7,8,9,10,11,12,13,14,15}:
        _loc={1:'V§1 andV§4–5 pp107–120',3:'V§1 pp108–109',4:'V§1 p109',5:'V§2 p110',6:'V§2 p111 andV§4 pp116–118',7:'V§2 p112',8:'V§3 pp112–114',9:'V§4 pp114–118',10:'V§4 p115',11:'V§4 p117',12:'V§4 p118',13:'V§5 pp119–120',14:'V§5 p120',15:'V§5 p120'}[_n]
        _c['refs'].append('GrothMontreal1974')
        _c['fate']+=' Exact publication collation: GrothMontreal1974 Chapter'+_loc+' repeats the corresponding programme assertion/question; this is documentary publication evidence, not an additional proof.'
        _c['present_status']+=' The exact Montréal parallel is now identified at '+_loc+'.'
    if _n in {9,11,12,13,15}:_c['class']='A'
    if _n==1:_c['statement']+=' Under the crystalline nilpotent-reduction equivalence, the underlying crystal depends only on G modulo p; this does not identify the categories of BT groups before and after reduction without Hodge data.'
    if _n==8:
        _c['class']='C'
        _c['statement']+=' Codex43 explicitly asserts exactness and locally free subcrystals for every Dieudonné crystal, not just those already known to arise from a BT group.'
        _c['present_status']+=' That stronger all-crystal quantifier is repeated in Montréalpp112–113 but is not established here beyond the precise perfect-ring/realizable cases; publication of the programme is not a proof.'
    if _n==58:_c['statement']=_c['statement'].replace('a locally trivial fibration','a numerable locally trivial fibration (in particular over the metrizable conical bases considered here)')
    if _n in {62,70}:
        _c['refs'].append('GuilbaultMoran2019')
        _c['fate']+=' The local-contractibility-to-ANR input was checked explicitly in Guilbault–Moran2019 Proposition2.9 p298, under their separable metric and locally compact assumptions.'
    if _n==82:
        _c['fate']+=' The publisher page subsequently opened confirms receipt9June1987, revision15April1988 and publicationJanuary1990; the full1990proof was still not read.'
        _c['fate_date']='Received1987-06-09, revised1988-04-15, publishedJanuary1990; exact separate preprint circulation date not established.'
    if _n in {42,43,45,46}:
        _c['fate']+=' Backward reference verified: Kurbatovet al. reference67 is Hille–Phillips1957, whose §5.8 theorems are explicitly cited for these pseudo-resolvent statements; the original book was not opened.'
        _c['refs'].append('HillePhillips1957')
    if _n==41:
        _c['fate']+=' A final exact-wording search produced a lead to Bourbaki2019 I§2 exercise30. Publisher metadata is verified, but the exercise text was only visible in an indexed non-authoritative reproduction after primary full-text access failed. This does not supply a verified completion of the archive sentence.'
        _c['refs'].append('Bourbaki2019')

# Manual page-status adjudication to the six requested labels. The more precise
# source assessment is retained inside the existing computation field; no cue or
# keyword classifier is used. Earlier-run implications remain explicitly labelled.
_status_groups={
 'proved there':[50,54,65,68],
 'proof sketched':[8,14,18,32,35,36,38,44,51,52,53,55,56,58,59,62,67,69,81],
 'corrected by himself later':[16,26,57,63],
 'false as stated':[2,34,39,40,42,47,122],
 'open on the pages':[3,4,7,21,22,24,25,29,30,31,41,64,66,70,80],
 'stated without proof':[1,5,6,9,10,11,12,13,15,17,19,20,23,27,28,33,37,43,45,46,48,49,60,71,72,82,83,84,120,121,123]
}
_status_map={n:label for label,numbers in _status_groups.items() for n in numbers}
assert len(_status_map)==sum(len(ns) for ns in _status_groups.values())==len(claims)
for _c in claims:
    _n=int(_c['id'].rsplit('-',1)[1])
    _c['computation']['source_page_assessment']=_c['status_on_pages']
    _c['status_on_pages']=_status_map[_n]
    if _n in {71,72,82,83,84}:
        _c['his_statement']='[Earlier-run implication, not an explicit assertion by the manuscript author; source anchor follows.] '+_c['his_statement']
        _c['computation']['source_page_assessment']+=' The standardized status stated without proof refers to the supplied earlier-note statement, not to attribution of this implication to the manuscript.'

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'claims':len(claims),'ids_unique':len({c['id'] for c in claims})==len(claims)}))
