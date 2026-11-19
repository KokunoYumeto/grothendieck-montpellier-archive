#!/usr/bin/env python3
"""Serialize manually written source judgements. No keyword/headline verdict inference."""
import csv,json,datetime
from pathlib import Path
P=Path(__file__).resolve().parent
pkg='MPL_22+23_002-016'
src='sources/texts/pro/'+pkg+'_transcription.tex'
items=[]; entries=[]
def add(ns,kind,cote,scans,lines,quote,statement,reconstruction,check,reason,corrections=None):
    id='SA23-'+str(101+len(items))
    items.append(dict(id=id,sources=[f'{pkg}#{n}' for n in ns],kind=kind,cote=cote,scans=scans,lines=src+': '+lines,his_words=quote,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,n in enumerate(ns):
        verdict=('corrected' if corrections and n in corrections else ('kept' if j==0 else 'merged'))
        entries.append(dict(entry_id=f'{pkg}#{n}',item_id=id,verdict=verdict,reason=(corrections[n] if corrections and n in corrections else reason)))
    return id

add([1,5],'reading question',['22','23'],['22/018–021','23/002–003,008–009'],'631–785;1197–1208;1420–1428','Questions ouvertes; EGA IV, Calcul diff. (Compléments)',
 'These leaves witness local subjects and four questions, not a complete chapter plan. The earlier notes correctly decline to reconstruct absent cotes 48,91,127,128 and CSG U90d, but cote26 is supplied in the present dossier.',
 'The comparison inventory belongs to the earlier run. Present-run cote26 comparison must be made from H26-01, independently of those notes.','agrees','The actual covers and numbered questions support the limited inventory; none supplies the missing chapter list.',{5:'Corrected the earlier-run absence claim: cote26 is now supplied, although the other named archive witnesses remain absent.'})
add([2],'title, date or page count',['23'],['23/002'],'1197–1204','EGA IV, Calcul diff. (Compléments)',
 'The thirteen-chapter list quoted by the earlier run is a published EGA I comparison witness, not text found on these archive sheets.',
 'Chapter titles and 1960 dating require independent published-source verification. The four local covers cannot reconstruct that list.','not on the page','The entry explicitly takes its chapter list from an earlier context file; that file is absent, so its assertions are treated as external bibliographical claims, not manuscript testimony.')
add([3],'idea of the earlier run',['22','23'],['22/018,028,030','23/004–006,013,016'],'631–664;1045–1092;1142–1194;1212–1375;1615–1667;1744–1774','par descente comme dans 4.11; intersection complète',
 'Projective conormal calculations, Cohen-algebra descent, trace/norms and infinitesimal automorphisms provide comparison objects for planned EGA chapters V–XIII; no chapter assignment beyond the IV cover is written.',
 'All chapter allocations in P03 are the earlier run’s thematic crosswalk. No Picard representability, fundamental-group calculation or Weil-cohomology construction is stated here.','agrees','Reading the displayed objects verifies the limited mathematical comparisons and their explicit non-attribution to an unwritten chapter plan.')
add([4],'conjecture',['22'],['22/020–021'],'682–774','Est-il vrai; est-il ouvert?',
 'The list asks about geometric regularity versus local formal smoothness, ordinary versus discrete formal smoothness, openness/localization of fibrewise formal smoothness, and openness of flatness for noetherian maps.',
 'Modern “formal smoothness” translates the draft’s “formellement simple”; any claim of equivalence with regular morphisms includes flatness. The annotation OK and the doubtful margins are not complete proofs.','agrees','Four numbered questions and their qualifications are present exactly at the cited locations.')
add([6],'title, date or page count',['23'],['23/002'],'1197–1204','EGA IV',
 'EGA II and IV printed contents are bibliographical comparison witnesses, not recovered manuscript chapter plans.',
 'Titles, receipt date 22 July 1960, and IV sections16–21 are claims about external printed contents requiring source opening.','not on the page','The manuscript cover supplies IV only; the detailed contents and date are absent from this transcription.')
add([7],'title, date or page count',['22'],['22/002–004,006–008'],'3–6;117;154–158;268','Note de M. Jean-Pierre Jouanolou',
 'Both printed offprints are by Jean-Pierre Jouanolou. November note: journal date13 November1963, session4 November; January note: printed21 January1963, session14 January.',
 'No date for Grothendieck’s handwritten annotations follows from those publication inscriptions.','agrees','Both bylines and all four printed date inscriptions are explicit; preserving authorship prevents reassignment of printed theorems to the annotator.')
add([8],'other',['22'],['22/006'],'162–174','D_A(B) le B-module des différentielles',
 'For a commutative A-algebra B, Jouanolou’s D_A(B) is the universal module Ω¹_{B/A}, with the canonical isomorphism taking each universal db to db.',
 'The generator-by-generator inverse is an explanatory reconstruction; the source defines D as the differential module.','agrees','The opening notation fixes the universal differential object; no extra completed or separated topology is included in D.')
add([9],'reading question',['22'],['22/002'],'13–26','D(deleted A, inserted A/a); D(deleted A)',
 'The annotated Tor criterion needs Ω_{(A/a)/prime base} as the quotient-algebra module. The higher-Tor display has a deleted argument without a visible replacement.',
 'Supplying A/a in condition(c) is a mathematically motivated candidate, not an emendation. The printed regularity theorem is recorded separately with its reduced-quotient and flat-differential hypotheses.','agrees','The correction is explicit in(b) and incomplete in(c); the note accurately retains that incompleteness.')
add([10],'self-flagged step',['22'],['22/002'],'33–40','assez rare !; Séries formelles ??',
 'The margins question finiteness of separated differentials and applicability of the regularity/singular-locus criteria to formal power series. Ordinary Ω, its separated quotient, and its completion are distinct.',
 'The completion map Ω→lim Ω/mⁿΩ is a reconstruction of the comparison to investigate, not a written answer.','agrees','The two doubtful marginal cues occur beside the stated finiteness/freeness hypotheses; neither licenses dropping them.')
add([11],'reading question',['22'],['22/003'],'54–62','Le noyau ... est contenu dans l’intersection',
 'For noetherian local A, the printed lemma bounds the kernel of Â⊗Ω_A→Ω_Â by intersections from finite quotients; the semi-finite conclusion prints (Â) where a differential module is required.',
 'Candidate middle term Ω_Â is inferred from the transitivity sequence. No transcription change is made.','agrees','The page states the kernel lemma and the semfinite corollary without proof; line60 indeed omits D.')
add([12],'unproved claim',['22'],['22/003'],'66–74','ce qui nous paraît être une lacune',
 'Jouanolou claims that separability of the completed fraction field repairs a gap in Lang’s1952 proof that the fraction field of k{T}, for complete algebraically closed valued k, is C₁.',
 'This is Jouanolou’s printed historical assessment. A modern proof of C₁ does not by itself verify that assessment of Lang.','agrees','The alleged lacuna and its stated separability input are printed explicitly; the earlier note correctly leaves Lang’s actual argument to be examined.')
add([13],'withdrawn in the same text',['22'],['22/003–004'],'79–98','faux si on ne suppose pas A→B injectif ??; C⊃A !!!',
 'The analytic-reduction argument receives an injectivity correction from the lower margin of003 to the theorem continuation on004; a separate “faux” attaches to the localization explanation.',
 'The correction concerns the finite integral extension and passage to fraction fields; the scope of the isolated faux is not enlarged to all later corollaries.','agrees','Both locations are present; the proposed inclusion is inserted in the later theorem and the note does not declare all consequences false.')
add([14],'self-flagged step',['22'],['22/004'],'108–114','connu (Nagata); ?',
 'Finite normalization in a finite fraction-field extension is asserted under analytic integrality and separability of K_Â/K_A; the applications to localities, analytic localities and regular Hopf algebras have a question mark.',
 'The note’s completion-descent argument is an external comparison, not supplied proof of every proposed application.','agrees','The attribution and question mark are distinct annotations and are not interchangeable evidence.')
add([15],'reading question',['22'],['22/006–007'],'176–217','quasi-séparable lorsque D_A(B)=0; non ramifiée; !?',
 'Ω_{B/A}=0 means formal unramifiedness for discrete algebras. Equivalence with the finite-type geometric unramified condition needs the usual finite-type and residue-field qualifications; n=mB alone is insufficient without them.',
 'The square-zero difference-of-lifts derivation is a present explanatory proof of the universal-property comparison.','agrees','The note correctly preserves the printed term and its residue-field/finiteness context; the handwritten replacement is tentative.')
add([16],'unproved claim',['22'],['22/006–007'],'164–174;219–239','deux suites exactes ... Berger et Kunz',
 'The offprint asserts left exact residue cotangent sequences in the separable case and in the modified characteristic-p case, then derives a finite-module freeness criterion by equality of generic rank and residue dimension.',
 'The source’s injection A→B and integral local hypotheses must remain. The generic-rank argument is a reconstruction of the omitted proof.','agrees','The two denominators and the finiteness condition are actually written; the note does not replace them by an unconditional conormal sequence.')
add([17],'reading question',['22'],['22/008'],'252–258','K_b (resp. L_a) est séparable sur K_a (resp. L_b)',
 'The printed proposition reverses the residue-field inclusion: a local injection A→B induces L_a→L_b. The candidate hypothesis is separability of L_b over L_a.',
 'The reversal is a mathematical/textual anomaly, not a decision about ink.','agrees','All surrounding differential modules and dimension symbols use the forward residue extension; the literal reverse order is preserved.')
add([18],'unpursued implication',['22'],['22/008'],'260–266','il vaut mieux séparer',
 'For N=Ω_{B/A}, N/∩nⁱN injects into lim N/nⁱN. The printed assertion additionally replaces Ω by its separated quotient in the rank-implies-regularity proposition.',
 'Only the injection follows formally from the inverse-limit map’s kernel; the regularity criterion needs its own theorem.','agrees','The note distinguishes quotient, completion, and the additional regularity assertion.')
add([19],'unproved claim',['22'],['22/028'],'1060–1074','les restrictions ... coïncidant',
 'For a finite extension of the function fields/valuations intended by the reused text, componentwise sums of local traces and products of local norms agree with global trace/norm on diagonal principal répartitions.',
 'The missing earlier formulas(12),(13) must supply decomposition of K⊗K̂′ into local factors. The retained leaf does not state the full ambient valuation hypotheses.','agrees','The maps and their claimed compatibility are on the page, while their cited proof inputs are absent.')
add([20],'unpursued implication',['22'],['22/028,030'],'1053–1055;1083;1148–1187','extension du diviseur = diviseur de l’extension',
 'Pullback of a place P′ is Σe(P/P′)P; norm is pushforward P↦f(P/P′)P′. Compatibility with idèles/principal divisors and norm∘pullback=n use Σef=n.',
 'These are assertions in the retained text’s finite-function-field context, not a universal equality for arbitrary valuations with defect.','agrees','The note correctly identifies the exact degree identity used and does not claim its missing hypotheses are supplied.')
add([21],'unproved claim',['22'],['22/028'],'1075–1085','que l’on vérifie comme l’âne qui trotte',
 'The page asserts the trace projection formula, trace/norm after scalar extension, and tower transitivity. They reduce to linear trace, determinant norm and decomposition into completions.',
 'The local calculations supply the omitted verification only under the finite-degree hypotheses implicit in the reused text.','agrees','All five formulas are present, with verification explicitly abbreviated.')
add([22],'reading question',['22'],['22/028,030'],'1047–1092;1142–1194','5. Topologies sur l’espace des répartitions et sur le groupe des idèles',
 'Formula numbering orders reused page030 before028; the unfinished topology paragraph does not state the neighbourhood basis, and the clipped phrase does not determine the missing text.',
 'Reordering is a reading aid only; original scan order remains authoritative.','agrees','The retained formulas run31–38 then39–45, while the final word is truncated for-.')
add([23],'idea of the earlier run',['22'],['22/007'],'219–239','{K_b:K_a}−{L_b:L_a}',
 'A comparison to EGA’s cotangent-complex Euler characteristic may illuminate the printed rank formula, but the archive page does not state that identification or an intersection-theory chapter assignment.',
 'This remains the earlier run’s external context link; exact complexes and maps must be matched.','not on the page','The entry itself acknowledges that the complex comparison comes from the absent context edition, not this offprint.')
add([24],'self-flagged step',['22'],['22/010'],'298–315','j’ai oublié d’introduire un système fondamental',
 'The quotient systems B/I_iB and C/I_iC require all I_iB and I_iC closed for the displayed inverse-limit identifications.',
 'No completion assertion beyond the author’s corrected hypotheses is inferred.','agrees','The author explicitly inserts the quotient-system repair and all-ideals closedness condition.')
add([25],'self-flagged step',['22'],['22/010'],'311–320','sauf erreur ... quelque part au Chap III',
 'Under target flatness, an isomorphism modulo the defining ideal lifts to an isomorphism of associated graded modules through the displayed comparison square.',
 'The exact historical ChapterIII locator is a tentative authorial reference; the mathematical square can be checked separately.','agrees','The correction from B_i to C_i places flatness on the target; the tentative reference is not a proof citation.')
add([26],'unpursued implication',['22'],['22/011'],'331–349','M un A-module de présentation finie',
 'For finitely presented M, M⊗∏P_i≅∏(M⊗P_i). Under the page’s hypothesis that finite modules are finitely presented, products of flat modules are flat.',
 'Modern coherence gives a sharper general criterion; that strengthening is not attributed to this sheet.','agrees','The inserted finite ranks in the free presentation are essential and explicitly present in the proof.')
add([27],'unproved claim',['22'],['22/011'],'351–363','on voit facilement ... isomorphe à un produit',
 'A countable inverse system of projective A-modules with surjective transition maps has limit isomorphic, after chosen splittings, to P₀×∏ker(P_{n+1}→P_n); under the preceding ring hypothesis it is flat.',
 'The coordinate formula using chosen sections is the earlier run’s completion of the abbreviated proof; the isomorphism is not canonical.','agrees','Surjectivity, countable cofinality and projectivity are all stated, so each transition splits.')
add([28],'reading question',['22'],['22/012–013'],'370–427','B est formellement simple; Les B_i sont plats',
 'Read literally, Theorem4.6(ii) equates conditions already assumed for B with invertibility of u:B→C and is false. A=B=Q[ε]/ε², I=(ε), C=Q satisfies the source conditions and u₀=id, while u is not injective.',
 'Replacing selected B symbols by C is only a candidate correction suggested by the proof; no silent emendation is made.','agrees','All source hypotheses hold in this discrete artinian example, including projectivity/conditionP for B, closed ideals and adic completeness; the counterexample therefore targets the literal statement.')
add([29,34],'other',['22'],['22/013,016–018'],'433–472;557–570;596–664','algèbre ... de Cohen; je me répens un peu de la définition',
 'The draft’s broad Cohen-algebra definition is complete+P+formal simplicity; later editorial comments propose base-ideal completeness and reduction to the main local theorem. k[[t]]/k belongs to the broad draft definition but not a later field-fibre definition.',
 'This is a terminology/editorial history, not withdrawal of all established local results. The note34 heading overstates “withdrawn”: the author proposes a rewrite and a changed convention.',
 'overstates','The definition remains visible; the live editorial paragraph proposes adjustments rather than striking all associated assertions.',{34:'Corrected kind: editorial revision of the definition and organization, not wholesale withdrawal of Theorem4.13 or all Cohen-algebra results.'})
add([30],'unproved claim',['22'],['22/014'],'471–472','stable par extension de la base via produits tensoriels complétés',
 'Stability of the draft Cohen-algebra notion under completed base change is asserted without specifying hypotheses ensuring the completed tensor product stays noetherian and in the intended adic class.',
 'A theorem with noetherianity, appropriate completeness and finite residue-field conditions is a restricted published comparison; it cannot certify an unrestricted slogan.','agrees','The entire source assertion is the one-line “trivialité”; additional hypotheses are not written there.')
add([31],'self-flagged step',['22'],['22/014,016'],'474–483;557–570','nous ignorons s’il existe toujours une solution',
 'Lift a prescribed complete formally smooth A/I-algebra B₀ across a square-zero ideal I to a flat/formally smooth complete A-algebra B with specified reduction; the text only proves the separable-residue-field case.',
 'Different completeness topologies give different problems. General published complete-local existence must be distinguished from the broader draft formulation.','agrees','The ignorance statement precedes the explicit limited Corollary4.10.')
add([32],'reading question',['22'],['22/015'],'521–530','les B/J_n sont des modules plats sur A',
 'Powers of lifted regular parameters generate a cofinal ideal family; fibre regularity plus A-flatness yields A-flat quotients, projective when A is artinian. The source alternates I_n and J_n.',
 'Identifying I_n=J_n is a reconstruction. The regular-sequence flatness input is omitted on the page.','agrees','The note preserves the notational discrepancy while specifying the actual omitted flatness lemma.')
add([33],'withdrawn in the same text',['22'],['22/015–016'],'537–555','L’hypothèse faite est très probablement inutile; Serre vient de me dire',
 'A cancelled note expects the finite radicial-multiplicity assumption to be removable and reports Serre’s reference to MacLane1940.',
 'The report is neither an active theorem nor proof that the cited paper has the claimed full generality.','agrees','The whole bibliographical request and continuation are within deleted markup.')
add([35],'unpursued implication',['22'],['22/016–018'],'557–664','par descente comme dans 4.11',
 'For local noetherian A→B with the stated finite radicial-multiplicity or equal-maximal-ideal condition, the draft compares adic formal smoothness with flatness plus geometrically regular closed fibre using a finite free radicial base change and a complete model.',
 'Removal of the draft’s residue-field restriction belongs to the later theorem, not this proof as written.','agrees','The model, separable-residue-field reduction and descent of flatness are explicitly described.')
add([36],'conjecture',['22'],['22/020'],'682–688','Est-il vrai ... universellement régulière',
 'For a noetherian local algebra over a field, is geometric regularity equivalent to formal smoothness for its maximal-ideal topology? The bracketed extension to local maps additionally requires flatness.',
 'The note properly limits the short OK annotation; ordinary local formal smoothness must not be confused with discrete formal smoothness.','agrees','The question and its scope are readable; the annotation supplies no separate written proof.')
add([37,42],'conjecture',['22'],['22/020,022–023'],'690–709;800–847;853–884','Il est possible ... affirmative en car p>0, négative en car0; Je présume que',
 'The author asks whether adic formal smoothness persists for the discrete topology, conjecturing contrasting characteristic-p/zero behavior and a positive-dimensional characteristic-zero obstruction.',
 'The sign in dimA≥0 versus >0 and the attachment of Faux are unresolved. The infinite-coefficient argument does not prove the Q[[t]] case; that case needs its own proof.','agrees','The notes correctly separate the general hope, uncertain margin and proved special obstructions.')
add([38],'conjecture',['22'],['22/020–021'],'712–760','Lieu ... est-il ouvert? ... bons anneaux',
 'For a flat noetherian map A→B, is the locus where fibre local rings are formally smooth over their residue-field bases open? The source suggests good-ring hypotheses and a characteristic-zero resolution route.',
 'Finite presentation or suitable excellence hypotheses are not automatic from noetherianity. The phrase “bons anneaux” is not expanded into a fixed modern class without evidence.','agrees','The relative fibre formulation and qualifications are on the pages; the margin is a proposed route rather than a complete proof.')
add([39],'self-flagged step',['22'],['22/021'],'726–744','stable par localisation ?; Cf IV 2.10.1|2.40.1',
 'The source asks about localization stability of the preceding formal-smoothness/geometric-regularity condition; field-base geometric regularity localizes via localization of finite field-extension base changes.',
 'That elementary mechanism proves a field-base case, not the whole relative openness problem. The chapter locator’s digits remain a reading question.','agrees','The question and doubtful reference are present; the note correctly narrows the verified comparison.')
add([40],'conjecture',['22'],['22/021'],'762–774','Lieu ... B est plat sur A est-il ouvert?',
 'The flatness locus of an arbitrary map of noetherian rings is asked to be open; a reduction proposes nonempty flat opens in quotient domains A′⊂B′ with field generic fibre.',
 'Generic flatness under finite type does not settle the arbitrary-noetherian formulation. The proposed equivalence itself needs a separate proof.','agrees','No finite-type hypothesis is written; the note correctly refuses to insert it invisibly.')
add([41],'unproved claim',['22'],['22/022'],'820–847','En la complétant par les t_i, on trouve une p-base',
 'In characteristic p, a finite p-basis of the coefficient extension, together with finitely many variables, is proposed as a p-basis for K[[t₁,…,t_n]] over k, with the displayed coefficient/Frobenius comparison.',
 'The finite-basis and separability/Frobenius-injectivity assumptions must be retained. The cancelled unrestricted attempts are not active assertions.','agrees','The finite-dimensional Ω hypothesis and surviving conclusion are explicit; the note separates the cancelled broader versions.')
add([43,44,45],'unproved claim',['22'],['22/023–025'],'864–884;891–959','n’a pas d’inverse à gauche; A^{(I)}⊂A^I',
 'If dim_KΩ_{K/k}=∞ and A=K[[t₁,…,t_n]], n>0, then Ω_{K/k}⊗A→Ω_{A/k} has no A-linear retraction. A finite quotient of coefficient differentials kills all D(t_j), and a series with infinitely many independent coefficient differentials contradicts finite support.',
 'The manuscript gives the retraction obstruction. The earlier run additionally proves Ω_{A/k} nonprojective, using freeness over the local ring and the infinite-support diagonal argument; this is a supplied proof of the à-fortiori clause, not a verbatim argument on the sheet.','agrees','Reading the proof verifies the finite-dimensional quotient and componentwise truncation method; the earlier-run projectivity completion is labelled separately.')
add([46],'unpursued implication',['22'],['22/025'],'932–959','A^{(I)}⊂A^I',
 'The vector (tⁿ) belongs to the t-adic completion of a countable direct sum but not the direct sum itself. This explains why the coefficientwise derivation can exist in a completed target but not the discrete free target.',
 'The explicit completed vector and its role are the earlier run’s explanatory construction.','agrees','The direct-sum/product distinction is exactly the contradiction used on the page.')
add([47],'idea of the earlier run',['22'],['22/023'],'855–858','k=Q, ou k=C',
 'Q[[t]] is not formally smooth as a discrete Q-algebra: Ω/tΩ has dimension1, whereas Ω⊗Q((t)) has infinite dimension by uncountability and characteristic-zero transcendence degree; a projective module over the local ring would be free.',
 'This is the earlier run’s independent proof of one manuscript example, not the manuscript’s infinite-coefficient proof. It does not use Ω_{Q/Q}≠0.','agrees','The example is written; the proof is clearly labelled as supplied by the earlier run and mathematically distinguishes the two fibre ranks.')
add([48,49,51,53],'idea of the earlier run',['22'],['22/027,029'],'971–1034;1104–1138','Voici un contre; On peut aussi prendre',
 'The manuscript constructs k⊂K in characteristic p for which Ω_{k/(k∩K^p)}⊗K→Ω_K is not injective. In the explicit p=2 specialization K=F₂(x,b,c), y=b²x+c², k=F₂(x,y), k∩K²=k² and the kernel is K(dy−b²dx), which does not descend to a k-line. A finite variant uses F₄ and has degree4.',
 'Constants p=2 and F₄, the derivative calculation and intermediate field k(c) are earlier-run realizations of the written construction. The general source formula has coefficients a_i and pth roots.','agrees','The source really adjoins coefficient roots as well as the root of y−Σa_ix^i; these adjunctions explain the kernel and distinguish it from the shorter printed example in EGA.')
add([50],'idea of the earlier run',['22'],['22/027–029'],'1006–1034;1104–1138','K=F(x,a_1^{1/p},…,a_{p−1}^{1/p},(″)^{1/p})',
 'The earlier run alleges that EGA0.22.5.10(i), read with K=k(X^{1/p}+ZY^{1/p}) and no adjoining Z, gives a pure-transcendental extension rather than the claimed inseparable counterexample.',
 'This is an external printed-source discrepancy requiring independent reopening of EGA; it is not a manuscript misreading and no corrected generator list is attributed to the author.','not on the page','The archive text has the necessary coefficient adjunctions. The alleged printed omission concerns a distinct published source.')
add([52,80,81],'reading question',['22'],['22/024'],'899–907','Ω_{K/k}⊗_KA→Ω_{A/k} ... n’a pas d’inverse à gauche',
 'The earlier run reports reversed map labels, reversed Hom variance and topology wording in its supplied comparison edition of EGA0.20.5.7 and0.20.7.2–3. These files are not attached here.',
 'Original EGA can verify the correct maps; absence of the earlier comparison files prevents an independent byte/text comparison with those claimed errors. The manuscript’s left-inverse question itself is present.','not on the page','These are source-control reports about an absent earlier-run context edition, not errors established from the supplied manuscript alone.')
add([54],'unproved claim',['23'],['23/004–005'],'1214–1278','d’où l’isomorphisme',
 'For a smooth relative complete intersection X⊂P(E), E rankr+1 and codimensionp, the Euler and conormal exact sequences identify detΩ_{X/S}⊗det(J/J²) with f*detE⊗O_X(−r−1).',
 'The determinant construction via wedge lifts and the tensor-order convention are reconstructed explicitly; smoothness and regular immersion are indispensable.','agrees','The source has the relevant exact sequences, ranks and determinant map; the note preserves its leftward orientation.')
add([55],'unproved claim',['23'],['23/005'],'1280–1289','un hom qui existe en tous cas',
 'The bracket seeks a canonical morphism from Ω_X^n to the determinant line defined by arbitrary graded equation generators M_d, extending the smooth complete-intersection adjunction isomorphism.',
 'Existence can be constructed by the conormal wedge/Jacobian map, but isomorphism requires regularity/smoothness. The following isomorphism symbol must not silently apply to the full bracketed generality.','agrees','The note correctly separates the general morphism from the earlier isomorphism and identifies its compatibility obligations.')
add([56],'unpursued implication',['23'],['23/005'],'1301–1316','M ≃ L^{⊗6}',
 'For the elliptic cubic presentation with E filtered by O,L²,L³ and f*L=T_{X/S}, detE=L⁵ and adjunction yields M=L⁶.',
 'The exponent calculation is explicit; descent from X to S uses the elliptic scheme’s section/connected proper fibre context, which the short passage assumes rather than re-proves.','agrees','The note correctly computes2+3+1=6 without switching tangent and cotangent line conventions.')
add([57],'reading question',['23'],['23/006'],'1327–1347','(k−1)(r+1)',
 'The repeated coefficient-degree reading differs from the standard discriminant degree (r+1)(k−1)^r in r+1 variables. For plane cubics the two values are6 and12.',
 'The standard polynomial discriminant is a comparison object; the meaning of Φ and the ink’s exponent remain to be checked before changing the source.','agrees','All three occurrences in the supplied transcription use the shorter product; the discrepancy is real relative to the standard normalization.')
add([58],'unproved claim',['23'],['23/006'],'1337–1354','lisse sur S, sss δ est partout non nulle',
 'The universal discriminant cuts out the nonsmooth hypersurface locus; its pullback is invertible exactly when the family is smooth, with a correctly normalized integral discriminant and appropriate hypersurface family.',
 '“Nonzero everywhere” means invertible on every residue fibre, not merely a nonzero global section. The normalization over arbitrary residue characteristics must be specified externally.','agrees','The note correctly translates the open-subscheme lift and does not substitute a pointwise nonzero polynomial over the base ring.')
add([59],'reading question',['23'],['23/006'],'1357–1374','O(k|−k)⊗g*(M)→O',
 'A degree-k equation gives O(−k)⊗g*M→O, not a positive twist. On P¹ a nonzero linear equation gives O(−1)→O while Hom(O(1),O)=0.',
 'The negative sign is a mathematical candidate only; the cancelled dual marks also remain undecided.','agrees','The earlier ideal formula has −k and the final sign is explicitly doubtful; the comparison detects its mathematical effect.')
add([60],'unpursued implication',['23'],['23/007'],'1382–1415','integrability condition; φ(0)=0',
 'The reused English leaf gives a Maurer–Cartan-type integrability equation. For the unprimed quadratic expression, its derivative at φ=0 is ∂bar h.',
 'The linearization is the earlier run’s calculation; the source stops after introducing a tangent vector and does not supply the subsequent page, author or date.','agrees','The cut-off passage and doubtful stroke are accurately retained; no claimed archival attribution is justified by this leaf alone.')
add([61],'reading question',['23'],['23/009'],'1448–1453','log gg′=log g log g′',
 'The displayed product formula for commuting g,g′ is false literally: in Q[ε]/ε² with g=g′=1+ε, its two sides are2ε and0. The compatible identity is log(gg′)=logg+logg′.',
 'Addition is a mathematically compelled candidate; only a scan can decide whether the error belongs to ink or transcription.','agrees','The note tests the exact literal formula under every stated premise and leaves the transcription unchanged.')
add([62],'unproved claim',['23'],['23/010–011'],'1484–1547','exp applique π(U) dans γ(U)',
 'In a complete augmentation-adic Q-bialgebra with Iⁿ→0, exp/log biject primitive and group-like augmentation-zero/one elements; the induced product on primitives is BCH.',
 'The coalgebra calculation uses continuity and commuting tensor-factor terms. No unrestricted convergence is asserted outside this topology.','agrees','The page states the topology and verification task; termwise application of Δ proves the stated primitive/group-like implication.')
add([63],'reading question',['23'],['23/010'],'1505–1511','δT=T⊗T; dual top. de l’Algèbre du groupe Z',
 'Completing k[z,z⁻¹] at(z−1), with z=1+T, yields k[[T]] and reduced coproduct δT=T⊗T. A topological-dual identification requires an additional pairing and topology.',
 'The completion map is an explicit comparison supplied by the earlier run, not a proof of the ambiguous duality phrase.','agrees','The note correctly distinguishes a completion isomorphism from an unspecified dual construction.')
add([64],'reading question',['23'],['23/012'],'1585–1611','(U⊗I(Λ))∩I(U⊗Λ)',
 'For split augmentations U=k⊕I, Λ=k⊕J, the two augmentation kernels intersect in I⊗J; the ideal U⊗J is nilpotent if J is nilpotent.',
 'The transcribed extra Λ factor is a candidate reading error. The four-summand decomposition proves the intersection without flatness assumptions.','agrees','Both augmentation maps are in the passage, and unit splittings justify tensor inclusions even when modules are not flat.')
add([65],'unproved claim',['23'],['23/013'],'1629–1641','universellement exacte',
 'The map (kerδ)⊗J→ker(δ⊗J) is an isomorphism if J is flat or the primitive kernel sequence is universally exact. Flatness of Λ implies flatness of J because Λ=k⊕J.',
 'No general commutation of kernels and tensor products is claimed.','agrees','The note tracks precisely the two sufficient hypotheses written on the sheet.')
add([66],'reading question',['23'],['23/013'],'1642–1647','1+π₀(U⊗Λ)',
 'The displayed exponential target cannot generally be1+primitives: in U=Q[x], Λ=Q[t]/t³, exp(tx)−1=tx+t²x²/2 has nonzero reduced coproduct t²x⊗x.',
 'The candidate target is group-like γ₀ as already written at the page’s top; no reading is changed.','agrees','The counterexample satisfies characteristic0 and nilpotence, and directly tests the written destination.')
add([67,76],'reading question',['23'],['23/013'],'1649–1667','U≃U(g); hyperalgèbre de Cartier',
 'The abbreviated marginal checklist does not by itself force U to be the enveloping algebra of its primitives: R^{C₃} is cocommutative, has only the trivial real group-like and no primitives, yet dimension3. Cartier’s connected filtration axiom excludes it.',
 'The example refutes only the abbreviated checklist, not Cartier’s theorem or the earlier augmentation-adic hypotheses. The precise filtration is an external definition to verify.','agrees','The note explicitly states I²=I and confines its counterexample to the literal shortened checklist.')
add([68],'reading question',['23'],['23/013'],'1654–1662','le dual de g|U est un anneau local régulier',
 'The complete dual of U(g), for finite-dimensional g over characteristic0 and the PBW coalgebra filtration, is a formal power-series algebra; the vector-space dual g* alone has no canonical ring structure.',
 'U is a mathematically appropriate candidate for the doubtful letter, justified through symmetrization and continuous duality, not an ink decision.','agrees','The preceding enveloping-algebra sentence supports the comparison and the note correctly flags the missing pairing/topology.')
add([69],'unproved claim',['23'],['23/013'],'1660–1662','Un groupe alg. en car0 ... toujours lisse',
 'Every group scheme locally of finite type over a characteristic-zero field is smooth.',
 'Locally finite type is the modern precise scope of “groupe algébrique”; arbitrary group schemes are not silently included.','agrees','The note preserves the uncertain marginal words and gives the correctly scoped modern Cartier corollary.')
add([70,74],'idea of the earlier run',['23'],['23/014–016'],'1674–1700;1734–1774','dérivations nilpotentes; automorphismes unipotents',
 'For a uniformly nilpotent endomorphism ξ over a Q-algebra, ξ is a derivation of a bilinear product iff expξ preserves that product. The induced group law is BCH and reduces to addition for a square-zero parameter ideal.',
 'The proof on Hom(M⊗M,M), using the commuting nilpotent operators ξ∘−,−∘(ξ⊗1),−∘(1⊗ξ), is the earlier run’s verification of the written equivalence; the square-zero test is a specialization.','agrees','The uniform nilpotence guarantees finite exponential identities; the manuscript asserts the equivalence and the note supplies its proof without assuming associativity of the product.')
add([71],'unpursued implication',['23'],['23/014–015'],'1704–1731','un idéal (nilpotent)',
 'If Jⁿ=0 and Λ-linear u_i send M into JM, every ordered product of n such endomorphisms is zero. Thus the whole endomorphism ideal is nilpotent of exponent at mostn.',
 'This is stronger than pointwise nilpotence and follows by u(J^rM)⊂J^{r+1}M.','agrees','The source explicitly inserts both the common exponent and nilpotent-ideal qualification.')
add([72,73],'reading question',['23'],['23/016'],'1746–1774','B=A⊗kΛ; B⊗Λk≃Λ|A',
 'Restriction identifies Λ-derivations of A⊗Λ with k-derivations A→A⊗Λ, inverse D(a⊗λ)=λd(a); infinitesimal derivations have image A⊗J. Reduction B⊗Λk is A, not Λ.',
 'The explicit maps verify the Hom chain without a false Hom–tensor exchange; choosing A for the doubtful quotient symbol remains an ink question.','agrees','The base-change formula and the ambiguous target occur together; split augmentation identifies its kernel correctly.')
add([75],'idea of the earlier run',['23'],['23/007,014–016'],'1401–1415;1692–1700;1734–1774','integrability condition; automorphismes',
 'For a square-zero parameter ε, conjugation by1+εv sends ∂bar to∂bar+ε[∂bar,v], linking the linearized integrability equation to infinitesimal coordinate action.',
 'This is the earlier run’s mathematical comparison, not an explicit cross-reference or asserted historical connection in the manuscripts.','not on the page','Both endpoint objects exist, but neither leaf explicitly identifies them; the note correctly gives only medium archival relevance.')
add([77],'title, date or page count',['22','23'],['22/002–030','23/002–016'],'1–1195;1197–1777','Questions; Questions ouvertes; Discriminant etc; Exponentielle',
 'The retained Pro package has29 cote22 scans and15 cote23 scans, separate printed and manuscript pagination, and no author-written total-page declaration. “En deux pages ou trois” is a rewrite request.',
 'Counts are counts of supplied scan markers, not a statement about all pages in each catalogue folder.','agrees','Every quoted title and the rewrite-length phrase is present; the entry distinguishes retained extent from authorial pagination.')
add([78],'title, date or page count',['22','23'],['22/002–030','23/002–016'],'all scanpage/mspage markers','mspage24–32; mspage29 and26 on22/030',
 'Cote22 has lower labels1–29 with internal24–32 on010–018; cote23 has1–15 with reused English page3 at007. Duplicate27 on22/028 and29/26 on030 must remain separate observations.',
 'No renumbering or inferred missing leaves is imposed.','agrees','The marker sequences were compared directly; the coexistence of page systems explains the otherwise conflicting numbers.')
add([79],'title, date or page count',['22','23'],['22/002,004,006,008,015','23/002–016'],'3;117;154;268;542–543;1197–1777','13 novembre1963; Séance du14 janvier1963',
 'The offprint and bibliography dates belong to identified printed works; individual handwritten title sheets are undated in this transcription. Earlier catalogue ranges are metadata, not manuscript inscriptions.',
 'The present TOPIC metadata supplies folder descriptions but does not independently reproduce all ranges reported in the earlier README.','agrees','The note’s chronology restraint is justified by reading the actual dated headers and undated covers.')
add([82],'other',['22','23'],['22/003,015,024,027–029','23/007,013'],'66–74;537–543;891–959;971–1138;1382–1415;1649–1667','Lang; Mac-Lane; integrability condition',
 'The earlier run’s own search/verification limits, including absent Lang/MacLane texts, unknown integrability-leaf attribution and unverified project-register statuses, are provenance facts about that run.',
 'No earlier claim of visual inspection, Lean status or search completion is inherited as a present-run check event. Current source openings and calculations are logged separately.','not on the page','The entry accurately labels its research limits; these are neither mathematical assertions of Grothendieck nor evidence that present literature searches are complete.')

assert len(entries)==82,(len(entries),len(items))
assert len({r['entry_id'] for r in entries})==82
(P/'items.json').write_text(json.dumps(items,indent=2,ensure_ascii=False)+'\n')
with (P/'entries.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(entries,key=lambda x:int(x['entry_id'].split('#')[1])))
(P/'stage1_output.txt').write_text(f'{len(entries)} manually reviewed source entries; {len(items)} consolidated items. All note entries read against the relevant supplied Pro transcription; no verdict generated from a title/keyword match.\n')
print((P/'stage1_output.txt').read_text())
