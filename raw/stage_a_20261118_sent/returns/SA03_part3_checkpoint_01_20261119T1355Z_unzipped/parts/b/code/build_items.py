"""Render manually adjudicated entries after complete line-by-line reading.

All content and verdicts below are authored judgments. Source parsing is used
only to verify coverage and attach the index's exact stable identifiers.
"""
from pathlib import Path
import csv,json,datetime
ROOT=Path(__file__).resolve().parents[1]
BASE='SA03_texts/pro/MPL_91_059-098_transcription.tex'
P='MPL_91_059-098'
items=[]; entries=[]; readlog=[]; events=[]
def add(n,sources,kind,scans,lines,words,statement,reconstruction,check,reason,verdicts=None):
    identifier=f'SA03-{n}'
    loc=[BASE+':'+x for x in lines]
    items.append(dict(id=identifier,sources=[f'{P}#{s}' for s in sources],kind=kind,cote='91',scans=scans,lines=loc,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for i,s in enumerate(sources):
        v,why=(verdicts or {}).get(s,('kept' if i==0 else 'merged',reason))
        entries.append(dict(entry_id=f'{P}#{s}',item_id=identifier,verdict=v,reason=why))
        readlog.append(dict(entry_id=f'{P}#{s}',source=BASE,lines='; '.join(lines),scans=','.join(map(str,scans)),reading='Full note entry and source passage read; overlapping K91-05/06/07 independently compared.',reason=why))
    events.append(dict(statement_id=identifier,date='2026-11-19',who='GPT-6 Astra Pro; effort inherited/not exposed; SA03-part3/b',type='used and rechecked in this run',outcome='Textual attribution/hypothesis check, not a proof certificate: '+reason))

add(201,[1],'other',[],[], '',
 'The citation key records the earlier run’s context, aliases and declared limits, not a statement by Grothendieck.',
 'No context packets or research-register originals are supplied here. Their quoted names are retained only as provenance leads.',
 'not on the page','The entry is an editorial source key. None of its novelty, planning or research-register labels can be promoted to a manuscript result.')
add(202,[2,4],'reading question',[59],['2-27'],
 '« est un isom. pour tt S′ »; « fini et plat »; « pour tout S′ non ramifié sur S »',
 'The proposed étale envelope T→T̄ has a universal mapping property into the specified étale/unramified test objects. This has left-adjoint variance, whereas restriction of scalars is a right adjoint. In the converse the text requires T finite flat over S and the map T→T̄ surjective and geometrically injective.',
 'The range of the first S′ must be inherited from the previous leaves. Finite flat cannot be silently replaced by finite locally free over an arbitrary base. Codex 59:7 reads a possible “Préciser” where Pro 59:13 reads “raison”.',
 'agrees','The Hom direction, nonramified clause and inserted flatness are explicit. Geometric injectivity is not unrestricted connectedness of fibres. The two witnesses disagree about a possible authorial precision request.',
 {4:('merged','The finite-flat and geometric-injectivity qualification belongs to the same envelope comparison as #2; retain both exact qualifiers.')})
add(203,[3],'reading question',[59],['2-27'],
 '« Il en résulte »; « Inversement »',
 'Scan 59 ends the preceding finite-étale/component-count criterion; the four-clause list reproduced by the note is a quotation from Hua’s interpretation, not a transcription of this single page.',
 'This run also has scans 50–58 in the preceding package, so the earlier run’s “unsupplied” boundary is historical, not a current missing-source claim. The preceding-package item owns the complete criterion.',
 'agrees','The note correctly limits its own image evidence. Its stated dependency is now checkable in the attached preceding transcription; merge at topic level with the earlier criterion.',
 {3:('corrected','Retain the source-boundary observation as the earlier run’s limitation; the preceding package is now supplied, so the complete criterion is no longer an unavailable-source problem.')})
add(205,[5],'other',[61],['29-59'],
 '« de nature locale »',
 'A covariant functor W:Sch/S→Sch is of local nature when it preserves open immersions and, under their identification as opens, arbitrary unions and pairwise intersections of open subsets.',
 'These are axioms for W, not for its partially defined right adjoint. The title is read “Set up général” in both current witnesses.',
 'agrees','All three locality axioms are written separately at lines 38,43–47,49–52; base change supplies Example I.')
add(206,[6],'reading question',[62],['61-81'],
 '« surjective, de noyau nilpotent »',
 'An augmented ring-scheme construction has a natural quotient O_{W(T)}→O_T with nilpotent kernel for every S-scheme T. This is additional structure beyond the general local ring-scheme example. The finite locally free universal-homeomorphism example realizes both base change and same-space ring-sheaf constructions.',
 'The numerical label III′/II′ is unresolved; it does not identify all Greenberg functors. The ring sheaf must make a scheme and functorial maps must be local.',
 'agrees','The augmentation direction and nilpotent-kernel condition are explicit at line 75; different labels do not justify modifying them.')
add(207,[7],'unproved claim',[62,63],['78-100'],
 '« foncteur adjoint (au sens de Kan) »; « il suffit … pour T affine »',
 'For a local W and Xfrak over W(S), a representing pair (X,α:W(X)→Xfrak) is a universal natural bijection Hom_S(T,X)≅Hom_{W(S)}(W(T),Xfrak). The bijection need only be checked on affines over affine opens of S, because both Hom functors satisfy Zariski gluing.',
 'Representability is conditional; no global right-adjoint existence theorem is asserted. The repeated T as target-base label in lines 85/99 is unresolved notation.',
 'agrees','The text asks whether the functor is representable and expressly restricts W^a to the subcategory where representatives exist. Affine testing is asserted with its locality reason, not fully expanded.')
add(208,[8],'other',[64],['102-117'],
 '« limites projectives finies »; « groupes, anneaux etc »',
 'Where the partial right adjoint W^a is defined, finite limits of represented objects are represented by the corresponding finite limits over S; W^a(Xfrak)×_S T represents the right adjoint for W restricted over T. Group and ring objects are transported through these finite-product identities.',
 'This follows directly by evaluating Hom on each T. Existence of the left side is the condition in the base-change formula; it is not a blanket representability assertion.',
 'agrees','The existence proviso follows the displayed formula at line 115 and the algebraic-object consequence occurs at 117.')
add(209,[9,13,14],'unproved claim',[65,66,67,68,69],['119-129','175-219'],
 '« préschéma d’anneaux générateur »; « schéma affine »; « C=colim C_i »',
 'Suppose W is local, sends affines to affines, and its ring functor on A-algebras is represented by an affine ring scheme Λ. For every affine W(S)-scheme Spec C, the functor B↦Hom_{W(A)-alg}(C,W(B)) is represented by an affine S-scheme. Finite equations give a zero fibre in Λ^r; arbitrary relations give the closed subscheme cut out by all relation coefficients; arbitrary C is a filtered union of finitely generated subalgebras.',
 'The all-relations step is the earlier run’s valid proof completion: finite generation need not mean finite presentation. The source itself completes the arbitrary-generator case by a colimit of representing coordinate rings. If Λ has v algebra generators and C has r, the representing algebra has at most vr generators.',
 'agrees','The finite-equation construction, finite-generator argument and general colimit argument are distinct written steps. Noetherianness is not required for forming an ideal generated by arbitrarily many relations.',
 {13:('merged','This is an explicitly editorial completion of the same affine representability proof, not a change from finite type to finite presentation.'),14:('merged','The next leaf supplies the arbitrary-C case. The transposition stroke in the first Hom display is preserved; its final universal property has the correct variance.')})
add(210,[10],'other',[66,67],['133-173'],
 '« covariant en Xfrak, contravariant en W′ »',
 'A natural transformation W′→W induces, wherever represented, W^a(Xfrak)→W′^a(Xfrak×_{W(S)}W′(S)); the construction is covariant in Xfrak and contravariant in W′.',
 'The base change of the target is essential. A link to particular changes of Greenberg level is a comparison task, not an identification made here.',
 'agrees','The two Hom maps are constructed separately and composed; the target base change is displayed at lines 137–140 and 164.')
add(211,[11],'self-flagged step',[67],['175-181'],
 '« que nous n’expliciterons pas »',
 'Translate the geometric locality axioms for an affine-preserving functor into explicit localization and overlap conditions on B↦W(B).',
 'A sufficient reconstruction must identify the images of distinguished opens and check a scheme structure plus local homomorphisms; representability by an arbitrary affine ring scheme alone does not do this.',
 'agrees','The translation is expressly deferred in line 179. It is distinct from the already stated geometric axioms and from an adjoint-existence theorem.')
add(212,[12],'reading question',[67],['175-181'],
 '« Foncteurs W spécial »; « affine sur S »',
 'The margin associates the adjective special with an affine ring-scheme realization of the local functor, subject to the already assumed scheme and locality conditions.',
 'This is partial definitional evidence, not a fully specified independent axiom system. Neither witness supports “no definition anywhere on the page”.',
 'agrees','Both Pro line 177 and Codex K91-05 line 144 preserve the marginal definition. Its opening connective remains uncertain.')
add(215,[15],'withdrawn in the same text',[69,79,80],['221-224','510-528'],
 'deleted « est affine »; live « de type fini … immersion fermée »',
 'The broad affine-morphism corollary at scan 69 is cancelled. The surviving inserted corollary concerns affine objects: closed immersions are preserved; finite-type maps are preserved if the ring generator is of finite type over S. General morphisms return only after the gluing argument on scans 79–80.',
 'The scope of the later one-line affine assertion is inherited and not fully restated. A cancellation is not a proof that the later strengthened theorem is false.',
 'agrees','The deleted block at 224 and the live insertion at 221–222 are unambiguous in both witnesses.')
add(216,[16],'reading question',[70],['226-246'],
 '« Lemme 1 »; « est un W(U′|U) »',
 'Given a representative X of Xfrak and Ufrak⊂Xfrak, an open U⊂X represents the subfunctor of maps landing in Ufrak when condition α identifies the corresponding factorization condition universally.',
 'The mathematically required conclusion is U≅W^a(Ufrak), with universal map W(U)→Ufrak; the written plain X and W(U′) are not silently corrected. Condition α must be interpreted for maps induced by T→X or else justified as a sufficient stronger condition.',
 'agrees','The note identifies the exact type errors at line 246; both witnesses preserve the same problematic formula.')
add(217,[17,18],'self-flagged step',[71,72,73,74],['248-331'],
 '« Il faut vérifier »; « s’identifie à l’identité »',
 'If the local representatives W^a(Xfrak_i), pairwise overlaps and triple overlaps exist as compatible opens, and every map W(T)→Xfrak locally lands in one Xfrak_i (β), these representatives glue to W^a(Xfrak). The overlap cocycle is the identity after identification with the representative of the triple intersection.',
 'The inserted triple-overlap condition and the locality axioms for W are required. The phrase “Aucune hypothèse” on scan 70 means no extra example-specific hypothesis, not abandonment of the original locality setup used in line 280.',
 'agrees','The requested cocycle check is immediately supplied at 270–274. The later universal-property proof uses β, local representing bijections and a common refinement.',
 {18:('merged','The source’s “Il faut vérifier” is followed by the verification on the same scan; this is not an unresolved open step.')})
add(219,[19],'reading question',[73,74],['307-331'],
 '« par factorisation »',
 'In the gluing proof, v|_{W(T_i)} factors through W(X_i)→Xfrak_i, producing u_i:T_i→X_i, which glue uniquely after refinement.',
 'The displayed final X_i at line 313 should be checked against Xfrak_i on the ink. It is a target-type discrepancy, not a gap in the otherwise indicated gluing mechanism.',
 'agrees','Both Pro 313 and Codex K91-06:35 print plain X_i. The preceding line 308 names Xfrak_i as the target open.')
add(220,[20,21],'unproved claim',[74,75,76],['344-356','393-405'],
 '« un morphisme fini est fermé »; « si … est loc. noeth. »',
 'Once Res_{S′/S}(Xfrak)=X exists, for Ufrak⊂Xfrak open the locus of parameters whose entire S′-fibre maps into Ufrak is X minus the image of the closed complement under the proper projection W(X)→X. It is open and represents the restriction to Ufrak. Finite locally free is the main case; scan 75 also states the proper-source version assuming X locally noetherian.',
 'Universal closedness and base change give the pointwise-fibre criterion. The locally noetherian condition is retained in the historical claim even though this elementary open-locus argument often works more broadly.',
 'agrees','The finite-map proof is abbreviated on 74 and concretely written at 398. Scan 75 assumes representability, so it is not an existence theorem for all proper sources.',
 {21:('merged','The proper-source corollary is the same conditional open-subobject mechanism, retaining both existence and the source’s locally-noetherian qualifier.')})
add(222,[22,63],'unproved claim',[61,62,67,75,78,79,80],['36-75','175-181','360-372','466-528'],
 '« Greenberg spécial »; « fini, loc. libre, … radiciel »; « de nature locale »',
 'For a special local Greenberg construction satisfying the affine-generator and same-space/nilpotent conditions, the right adjoint exists on every target scheme and is local. The same holds for base change by a finite locally free radicial map S′→S. Classical Greenberg functors are a published instance; their preservation theorems require the specified Artinian ring hypotheses.',
 'The general adjective special is not completely axiomatized on this leaf. The weak finite-type margin on 75 cannot be read as a definite added hypothesis. Modern Artinian Greenberg results establish a case, not automatic equality of all proposed frameworks.',
 'agrees','The theorem is explicitly restricted to two cases. The earlier note’s literature comparison correctly keeps its Artinian-ring hypotheses separate.',
 {63:('merged','The verified modern Greenberg comparison supplies a fate for the same existence/locality theorem, with scope limited to its actual §7 ring assumptions.')})
add(223,[23,24,65],'unproved claim',[75,76,77,78,79],['374-434','466-508'],
 '« partie finie »; « ayant ≤ n(s) éléments »; « préschéma »',
 'Let S′→S be finite locally free and n(s) the number of geometric points of its fibre. An S′-scheme Xfrak has a scheme Weil restriction if every subset of Xfrak_s of at most n(s) points lies in an affine open of Xfrak; more generally a covering containing every such possible section image glues the restrictions of the opens. Existing restrictions carry open immersions to open immersions.',
 'This uses the geometric-point reading of the uncertain margin. A sufficient all-finite-subsets condition is stronger than the particular finite images of sections in the proof. Modern algebraic-space existence without this affine-neighbourhood condition does not erase the scheme distinction.',
 'agrees','The finite-subset insertion is present at 386; the proof tests residue-field sections at 402–405; the cardinal bound is inserted at 424. Codex reads “rang géom.” in the margin, requiring an ink check.',
 {24:('merged','The bound refines the same representability criterion; geometric fibre cardinality, rank and scheme length must remain distinct.'),65:('merged','Algebraic-space existence is a comparison to this scheme criterion, not evidence that its target condition is superfluous.')})
add(225,[25,26],'unproved claim',[77],['436-457'],
 '« S loc. noeth. »; « une s.-famille finie »',
 'For S locally noetherian, S′→S finite locally free, and Xfrak/S′ of finite type with every finite subset in an affine open, Res_{S′/S}(Xfrak) is finite type. The auxiliary lemma selects a finite subfamily from a cover containing every subset of size ≤n. The displayed relative product argument establishes the fibrewise version directly.',
 'The claimed equivalence with a relative n-fold-product cover does not express subsets over different base points. The global lemma can instead be proved using the quasi-compact ordinary topological product |Xfrak|^n. This is a repair of the proof, not a counterexample to the finite-type corollary.',
 'agrees','The source includes the noetherian hypothesis and its finite-subfamily argument. The earlier note’s two-point test correctly isolates the relative/global mismatch.',
 {26:('merged','The two-point counterexample refutes only the written “l’hyp. signifie” equivalence; the finite-type theorem survives the fibrewise argument.')})
add(227,[27],'idea of the earlier run',[61,75,77],['38-52','360-366','459-460'],
 '« Le foncteur W^a n’est pas local en tous les cas »',
 'For S=Spec k nonempty, S′=S⊔S, and Xfrak=A¹_S⊔A¹_S over S′, each single component U_i has empty Weil restriction, whereas Res(Xfrak)=A¹_S×A¹_S. Thus restriction along a general finite locally free map does not preserve unions of target opens.',
 'The explicit counterexample belongs to the earlier notes. The manuscript has the warning but not this example; all schemes in the example are affine and the base map is finite étale of rank two.',
 'agrees','The literal warning is present. The example computes each Hom functor and does not confuse preservation of a covering family with preservation of an isomorphism.')
add(228,[28],'unproved claim',[78,79],['466-497'],
 '« (existe et) est une immersion fermée »',
 'For W of type I′ or special Greenberg, a closed immersion Xfrak→Yfrak induces a closed immersion under W^a; in type I′ the written finite-subset affine-neighbourhood condition on each fibre of Yfrak is retained. If Yfrak is quasi-projective over the intended base, a general immersion is treated by factoring it as closed then open.',
 'The ambiguous base S*|S′ is a reading issue. The modern representability category must remain schemes when comparing this statement.',
 'agrees','The extra target condition and existence insertion occur at 474/478; the affine reduction and closed/open factorization are written.')
add(229,[29],'unproved claim',[64,79],['104-117','499-508'],
 '« sous réserve que … existe »',
 'Under the same W hypotheses, if every finite subset of Xfrak lies in an affine open and f:Xfrak→Yfrak is separated, W^a(f) is separated, subject to existence of W^a(Yfrak) in type I′. Apply the closed-immersion statement to the diagonal, using preservation of fibre products.',
 'This is a proof sketch with explicit existence caveats; it is not a theorem that all target representatives automatically exist.',
 'agrees','The full caveat lies at 503–506, and the diagonal is named at 508.')
add(230,[30],'unproved claim',[69,75,79],['221-222','367-372','510-524'],
 '« Yfrak loc. noeth »; « de type fini »',
 'The final proposition states finite-type preservation for W of type I′ or special Greenberg, Yfrak locally noetherian, f finite type, and in case I′ an affine-neighbourhood condition on finite subsets of each f^{-1}(U) for affine U⊂Yfrak.',
 'For arbitrary affine ring generators an additional finite-type bound is needed, explicitly present earlier at 222 but not restated here. The Greenberg margin has competing readings: “inquiétude” (Pro) versus “rédiger cela/restreig. à cela” (Codex). Classical Artinian Greenberg is covered by modern results; the full generic scope is not secured by that fact.',
 'agrees','The note properly refuses to turn a doubtful margin into a retraction. Its modern comparison must not be expanded beyond the generator finiteness implicit in the earlier argument.')
add(231,[31],'unproved claim',[80],['526-528'],
 '« Comme dessus, pour morphismes affines »',
 'The source asserts preservation of affine morphisms under the preceding setup without restating exactly how much of it is inherited.',
 'An affine-local proof uses the affine representing construction over each represented target chart, then glues. This is a proposed proof strategy, not a written proof on scan 80.',
 'agrees','Only one proposition line occurs. The earlier register’s global “proved” description would overstate this leaf.')
add(232,[32],'title, date or page count',[81],['530-536'],
 '« Schémas localement compacts »',
 'A new cover title introduces the constructible/schematic-set programme. No date or manuscript page count occurs on this cover.',
 'The deleted earlier title is uncertain and differs in the two transcriptions. It does not date the live mathematical notes.',
 'agrees','The live two-line title is common to Pro and Codex; neither supports a total page count.')
add(233,[33],'unproved claim',[82],['538-574'],
 '« syst. fini d’équations »; « quasi-séparé quasi-compact »',
 'For a quasi-compact quasi-separated scheme X, a locally closed subset Z is constructible precisely when it is quasi-compact and locally, inside suitable affine opens, is the zero set of finitely many functions. The broader topological local-to-global criterion requires retrocompact neighbourhoods.',
 'Finite equations describe the underlying closed set or a suitable finite-presentation structure, not necessarily the reduced induced immersion. The compressed opening alternatives must not be converted silently into a different statement.',
 'agrees','The scheme hypotheses and finite-equation test are explicit at 570–574. The proof uses finite covering and transitivity of constructibility.')
add(234,[34],'unproved claim',[84],['628-643'],
 '« Il existe un ouvert quasi-compact U »; « U∩T≠∅ »',
 'For an irreducible closed T in a space with a basis of retrocompact open neighbourhoods (in particular a spectral scheme space), existence of a nonempty relatively open Z⊂T constructible in X is equivalent to existence of quasi-compact open U⊂X meeting T with U∖T quasi-compact.',
 'The spectral-space version has the needed quasi-compactness and retrocompactness. The precise general-topological hypothesis remains tied to the uncertain margin; no tear is inferred in the complete current text.',
 'agrees','Both current transcriptions contain condition (ii), including the nonempty intersection. Hua’s reported lost condition is an older witness limitation.')
add(235,[35],'other',[87],['686-723'],
 '« restriction aux préschémas réduits est fidèle »',
 'An atomic scheme is a disjoint union of spectra of fields. Such schemes embed fully faithfully in functors on fields. Sending X to the coproduct of its residue-field points remembers all field-valued points and is faithful on reduced source schemes, but loses nilpotent information.',
 'The deleted “pleinement” must not be restored for general reduced schemes. In the constructible category the pieces carry reduced scheme structures.',
 'agrees','The fully faithful assertion has a different domain from the later faithful one; the reduced-strata convention occurs explicitly at 723.')
add(236,[36],'reading question',[87,89],['716-723','789-797'],
 '« une partition »; inserted « finie »',
 'The local definition uses a partition of an affine open into locally closed constructible strata. The later characterization for quasi-compact quasi-separated X explicitly requires one finite affine constructible stratification.',
 'In the usual patch topology each constructible piece is clopen; compactness forces any disjoint constructible cover of a quasi-compact quasi-separated scheme to have finitely many nonempty members. Thus the earlier omission need not change the mathematics.',
 'agrees','The word finite is absent on 87 and inserted on 89. The compactness explanation is an editorial proof, not an inserted word.')
add(237,[37,48],'unproved claim',[89,95],['763-776','924-935'],
 '« Tous les foncteurs écrits commutent aux … finies »; « Produit fibré … Existe »',
 'The proposed category of quasi-compact quasi-separated schemes with finite piecewise morphisms on reduced locally closed constructible strata has finite limits; ordinary fibre products induce the corresponding categorical fibre products. Maps to atomic schemes/field-valued functors preserve these limits in their appropriate categories.',
 'Finite diagrams allow a single finite refinement of all source/target partitions. Reduction is interpreted in the reduced category, so an unreduced scheme fibre product is compared through its reduced piecewise object. This does not prove an infinite-limit statement.',
 'agrees','The marginal categorical assertion and later explicit product assertion coincide. The earlier notes correctly separate the finite-refinement argument from scan 97.',
 {48:('merged','The common-refinement explanation addresses the same finite-limit assertion as #37 and is labelled as the earlier run’s proof sketch.')})
add(238,[38],'unproved claim',[89],['789-795'],
 '« parties loc. fermées constructibles affines »',
 'Every constructible covering of a quasi-compact quasi-separated scheme admits a finite refinement by disjoint affine locally closed constructible strata. A map on atomic points is constructible exactly when it is a scheme morphism on such a refinement.',
 'For an arbitrary cover, first use compactness of the constructible topology, then finite Boolean refinement and affine refinement. Codex is less certain about the arbitrary-cover wording, but the stronger version has this proof.',
 'agrees','The note supplies the compactness step absent from the abbreviated source; finite global strata are expressly inserted at 795.')
add(239,[39],'unproved claim',[91],['827-842'],
 '« pour une structure … convenable »',
 'Inverse image under a constructible map between quasi-compact quasi-separated schemes carries constructible subsets to constructible subsets. Reduce to finitely many actual scheme morphisms on strata, then use inverse-image stability of constructibility and transitivity along locally closed constructible inclusions.',
 'A reduced stratum need not be a finitely presented immersion; the source’s suitable structure parenthesis should be read topologically, not as that false stronger assertion. Codex suggests “fragile … l’argument!” where Pro has “topologique …”.',
 'agrees','The construction of inverse images is correct with the stratum structures distinguished. The marginal reservation remains unresolved on ink.')
add(240,[40],'unproved claim',[87,91,93],['716-723','844-850','873-884'],
 '« isom de X_i sur Y_i »; « car il le fait ens. »',
 'An isomorphism in the schematic-set category is equivalent to a finite piecewise isomorphism of reduced locally closed constructible strata; affine strata may be chosen. Refine a constructible inverse and the original map by mutual inverse images.',
 'The reduced convention is inherited from 87. Set-theoretic factorization through a closed reduced stratum is valid for reduced source; it is false without this qualification for nilpotent sources.',
 'agrees','The note correctly identifies the missing repeated “red” and the structure-sensitive factorization step, while retaining the common-refinement proof.')
add(241,[41,43],'reading question',[93],['873-886','894-898'],
 '« Si X noethérien Y l’est »',
 'Finite piecewise isomorphism preserves noetherianness of the underlying topological space. It does not preserve noetherianness of the scheme’s rings, even for reduced schemes: B=k+xk[x,y] has a two-piece constructible model Spec(k[x,x^{-1},y]×k), but J=xk[x,y] has J/J²≅k[y], so B is not noetherian.',
 'The reduced counterexample is the earlier run’s construction. The margin may be defining “noetherian schematic set” by existence of a noetherian model rather than making the false literal ring assertion.',
 'agrees','The scheme/topology distinction is essential. The two reduced constructible strata are D(x) and V(x)_red, and the non-finite ideal argument is correct.',
 {43:('merged','The reduced example strengthens #41 without repairing the literal scheme-theoretic corollary by adding reducedness.')})
add(242,[42,45],'idea of the earlier run',[87,93],['716-723','886-900'],
 '« est de type fini »; « U_{i red} »',
 'A scheme morphism inducing a constructible isomorphism need not have finite type. Examples: Spec(k⊕M)→Spec k for infinite-dimensional square-zero M; and the reduced affine morphism Spec(k+xk[x,y])→Spec(k+x²k[x,y]), which is an isomorphism on D(x²) and on reduced closed complements but not finite type.',
 'These counterexamples are earlier-run ideas, independently checked here. Pro line 900 leaves Corollary 3 live; Codex K91-07:192 deletes the entire corollary. Hence mathematical refutation of its literal wording is secure, but attribution as a surviving claim or an authorial withdrawal awaits ink.',
 'overstates','The notes correctly refute the literal formula, but #45’s characterization of it as a surviving legible corollary is too definite once both attached witnesses are compared. No witness is silently preferred.',
 {42:('kept','The square-zero example correctly loses both scheme-noetherianness and finite type under reduction.'),45:('corrected','Keep the valid reduced counterexample; qualify live-versus-cancelled status because Codex marks the entire Corollary 3 deleted while Pro does not.')})
add(244,[44],'unproved claim',[93,95],['888-890','916-920'],
 '« Tout ens schématique … X affine »',
 'Every quasi-compact quasi-separated schematic set admits an affine scheme model by replacing it with the finite disjoint union of affine reduced constructible strata. A constructible morphism admits compatible affine source and target models; a piecewise finite-type morphism admits finite-type affine models.',
 'These are isomorphisms in the constructible category. They do not say that the original scheme is affine or that its given morphism has finite type.',
 'agrees','The corollaries concern schematic sets and compatible models. Their omission of a detailed proof does not turn them into ordinary-scheme assertions.')
add(246,[46],'reading question',[95],['916-920'],
 '« présentation finie ? »',
 'The text defines finite type intrinsically by a finite stratification and asks something about introducing or obtaining finite presentation in this category.',
 'The question’s logical force is undecided: Pro reads “cela implique …”, Codex K91-07:212 reads “est-il indiqué de définir la présentation finie ?”. These are different questions. No mathematical implication should be attributed securely until the scan is checked.',
 'overstates','The earlier note treats a plausible but weak reading as an implication question. The second attached witness supplies a coherent editorial alternative.',
 {46:('corrected','Retain a finite-presentation reading question, not a secure conjecture that finite type implies finite presentation.')})
add(247,[47],'unproved claim',[95],['920-935'],
 '« X=E⊔(X−E) »; « critère de factorisabilité »',
 'A constructible subset E of a schematic set X carries an intrinsic piecewise reduced object, and X decomposes as the categorical coproduct E⊔(X∖E). A constructible map factors through E exactly when its atomic image lies there.',
 'Independence of finite stratification follows by common refinement. Pro “universalité!” versus Codex “c’est ensembliste!” does not change the proposed factorization statement.',
 'agrees','The construction and factorization criterion are named on the page but not fully proved; it is not a clopen decomposition in the original Zariski topology.')
add(249,[49],'self-flagged step',[97],['960-997'],
 'deleted « Je dis que »; inserted « A-t-on »; « ??? »',
 'For an inverse system X_i of quasi-compact quasi-separated schemes with eventually affine transitions and X=lim X_i, does cons(X) represent the inverse limit of cons(X_i) in the finite-piece constructible category?',
 'Both Hom calculations are conditional on the categorical limit. Their difference is the order of an infinite inverse limit and a filtered colimit over finite partitions. No later generic Pro/Hom identity automatically removes it.',
 'agrees','Both witnesses securely change an assertion into a question and give the incompatible orders of limits. This is the package’s clearest genuine open question.')
add(250,[50,51],'idea of the earlier run',[97],['973-996'],
 '« une partition finie »',
 'For T=A¹_Q and X_n=A^n_Q with coordinate projections, the compatible constructible maps whose m-th coordinate is 1 at a distinct rational point a_m and 0 elsewhere do not arise from one constructible map T→Spec Q[t_1,t_2,…]. More generally the comparison’s image is exactly the compatible families admitting one common finite reduced constructible stratification on which all stage maps are scheme morphisms.',
 'The counterexample and exact image criterion belong to the earlier run. On the stratum containing the generic point of T, all coordinates vanish generically and hence identically, but a cofinite open contains some a_m. The positive criterion uses the ordinary scheme-limit universal property on each fixed reduced stratum.',
 'agrees','All stages and transitions satisfy the stated affineness and finiteness hypotheses. The argument refutes the canonical comparison, not existence of every possible categorical limit.',
 {51:('merged','The common-partition criterion is the precise conditional positive replacement for the same failed comparison in #50.')})
add(252,[52],'reading question',[97],['973-996'],
 '« cons X »',
 'Finite-piece constructible maps, field-valued natural transformations and affine maps into a constructible/absolutely-flat ring model have different finiteness quantifiers. An infinitely generated source ring can choose each coordinate in a different finite-stage partition ring.',
 'The note’s comparison to scans 114–115 requires those exact later constructions. A w-local scheme and the reduced constructible spectrum used in modern pro-étale constructions are also different objects.',
 'agrees','The scan-97 Hom formulas display a single partition for the entire map; they do not justify replacing it with coordinatewise finite partitions.')
add(253,[53],'unpursued implication',[97],['962-996'],
 '« u_{ij} est affine »',
 'Descent of a morphism into a finitely presented target through an affine inverse system is a separate theorem from the simultaneous finite-partition problem for infinitely many target stages.',
 'The later 136 comparison needs its own quasi-compactness, quasi-separatedness and finite-presentation assumptions. It cannot solve the scan-97 problem merely by sharing inverse-limit notation.',
 'agrees','The earlier note’s hypothesis distinction is correct; the counterexample at SA03-250 remains even when every individual X_n is affine of finite type.')
add(254,[54],'unproved claim',[83],['578-606'],
 '« Prendre une base dans V »; « e^{T(u⊗1+1⊗v)}=e^{Tu}⊗e^{Tv} »',
 'The reused printed exercise describes finite-dimensional scalar extension V⊗K((T)) by bounded-below Laurent series, its endomorphism algebra, and the formal exponential identity for commuting tensor factors in characteristic zero. A vector killed by u is fixed by exp(Tu).',
 'Finite dimensionality of V and the definition of V_(L) are missing on this fragment; they are necessary reconstruction hypotheses. The algebra application (e) stops mid-sentence. This is a printed source, not securely an original Grothendieck assertion.',
 'agrees','The note preserves the missing opening/ending and the explicit finite-dimensionality of W instead of manufacturing a complete exercise.')
add(255,[55],'unproved claim',[85],['647-684'],
 '« (ad x)^p.y=(ad x^p).y »',
 'For an associative algebra in characteristic p, left and right multiplication commute, giving (ad x)^n=Σ(-1)^{n−i} binom(n,i)L_x^iR_x^{n−i}; hence (ad x)^p=ad(x^p) and (ad x)^{p−1}(y)=Σ x^i y x^{p−1−i}. Polarization gives the printed f- and g-coefficient identities.',
 'The leading torn upper limit and the definition of f_k are not supplied by the fragment; the natural complete symmetrization interpretation is explicitly a reconstruction. Codex g_{i,k−1} versus Pro g_{i,k−i} is an index alarm.',
 'agrees','The identities are printed exercises with no source proof, not unverified steps personally marked in the handwriting.')
add(256,[56],'reading question',[88,90],['734-739','824-825'],
 '« pour tout z∈U »; « π(z)≠0 »',
 'The printed residual finite-dimensionality statement for U(sl(V)) cannot include z=0. The plausible corrected statement is: every nonzero element is detected by a finite-dimensional representation in characteristic zero.',
 'The nonzero qualifier is a mathematical candidate only. Both attached transcriptions retain the same impossible literal quantifier.',
 'agrees','Every linear representation sends zero to zero. The note’s test is decisive and does not justify inserting ink.')
add(257,[57],'reading question',[88],['741-754'],
 '« β(x′_i,x′_j)=δ_ij »',
 'The tensor associated to an invariant multilinear form via a nondegenerate invariant bilinear form is basis-independent when x′_j is the β-dual basis to x_i, namely β(x_i,x′_j)=δ_ij. The printed two-prime condition does not provide that dual basis and fails the one-dimensional rescaling test.',
 'Use the trivial action on Qe, β(e,e)=1 and f(e)=1: choosing x=e or x=2e while keeping x′=e changes the displayed tensor from e to 2e. This is the earlier run’s counterexample, checked here.',
 'agrees','Both transcriptions have two primes and the doubts file explicitly preserves them. The alternative remains a scan-check request.')
add(258,[58],'idea of the earlier run',[90],['812-822'],
 '« il faut et il suffit »; « sous-g-module »',
 'The printed equivalence Hom_g(M1,M2⊗N)≠0 ⇔ Hom_g(M2,M1⊗N*)≠0 is false for simple finite-dimensional M1,M2 and an arbitrary finite-dimensional N. For [h,e]=e over Q, N with h=diag(1,0), e=E12, M1 of weight 1 and M2 trivial, the first embedding exists but the reverse invariant space in M1⊗N* is zero.',
 'Tensor adjunction gives a quotient map M1⊗N*→M2, not an embedding M2→M1⊗N*. Complete reducibility is an additional sufficient repair. The example and repair are editorial, not a change to the printed source.',
 'agrees','The leaf assumes no semisimplicity. Both one-dimensional modules are simple, the matrices satisfy [h,e]=e, and the reverse common kernel is zero.')
add(259,[59],'unproved claim',[92,90],['853-869','805-810'],
 '« composantes semi-simple et nilpotente »',
 'A Lie action preserves symmetric and antisymmetric tensor submodules. Invariant bilinear multiplication tensors are exactly products on which the action acts by derivations. For a finite-dimensional vector space over a perfect field, additive tensor representations preserve Jordan decomposition; consequently the semisimple and nilpotent parts of a derivation of a not necessarily associative algebra are derivations.',
 'These are printed exercises. The perfect-field and finite-dimensional hypotheses matter; no Lefschetz operator or external lattice construction is present.',
 'agrees','The archive sequence 92→90→88 follows printed pages 137→138→139, and the derivation sentence continues from 92 onto 90.')
add(260,[60],'self-flagged step',[94],['903-912'],
 '« une proposition en forme et une rédaction moins cursive »',
 'The reused functional-analysis report requests a formal statement and fuller proof that bounded convergence on continuous multilinear maps between the indicated normed spaces is induced by an operator-type norm.',
 'The source begins mid-sentence; its exact ambient field/norm assumptions are incomplete. The strict first bound ||x1||<1 and weak remaining bounds must be retained. A general valued-field normalization is not silently replaced by the real/complex one.',
 'agrees','The wording is an editorial request, with uncertain personal authorship, rather than a conjecture in the constructible-geometry programme.')
add(261,[61],'self-flagged step',[96],['938-958'],
 '« l’appeler “stabilisateur” »',
 'For a continuous transitive action of a topological group G on E, the orbit map factors as the quotient G→G/H0 followed by a continuous bijection G/H0→E. The report asks whether to adopt the term stabilizer for H0.',
 'The available fragment does not yet assert the bijection is a homeomorphism. The report’s wording question is not an unresolved geometric-category quotient theorem.',
 'agrees','The title names a revision of Topologie Générale Chapter III; the definition of topological homogeneous space breaks off at the end.')
add(262,[62],'unproved claim',[98],['1000-1013'],
 '« sous-groupe partout dense »; « pas nécessairement g(G)=G′ »',
 'Let G be Hausdorff and let (Hα) be a directed filter basis of closed normal subgroups converging to the identity. The canonical G→lim G/Hα is a topological embedding with dense image; surjectivity need not hold (for example Z with its p-adic topology embeds densely in Z_p).',
 'The printed E where the filter is based must be checked against G. The complete proof of the embedding and density is on the page; only the non-surjectivity example is left as an exercise.',
 'agrees','The argument uses directedness, quotient surjectivity and VHα⊂V². This does not answer the different cons-limit problem on scan 97.')
add(264,[64],'unpursued implication',[61,67,75],['36-75','175-181','360-366'],
 '« de nature locale »',
 'Vanni’s 2025 thesis is a concrete modern lead for an axiomatic Greenberg construction in geometric categories; equality with the precise handwritten local-functor axioms has not been established by an abstract alone.',
 'This is a literature-comparison lead of the prior run. The official abstract was opened and checked; thesis-text retrieval and exact theorem matching remain distinct evidence tasks.',
 'agrees','The note limits itself to the abstract and explicitly declines a theorem-by-theorem equivalence; no novelty follows from the older search’s failure.')
add(266,[66],'unpursued implication',[89,91,93,95],['778-795','844-884','924-935'],
 '« isom. constructibles »; « X=E⊔(X−E) »',
 'For reduced separated finite-type k-schemes, a finite piecewise k-isomorphism gives equality of classes in the Grothendieck ring of varieties by applying the scissor relation to each locally closed piece.',
 'This restricted consequence is an earlier-run comparison, not an identification of arbitrary schematic sets with model-theoretic definable sets or with the project’s K_G(X).',
 'agrees','The finite-piece definitions support the restricted deduction. No numerical intersection or Lefschetz operation is written on these pages.')
add(267,[67],'unpursued implication',[84,87,89,91,93,95,97],['633-643','716-723','789-795','827-900','916-997'],
 '« application constructible »; « de type fini »',
 'The finite-partition language is an input to later Greenberg rational-map questions. It does not supply uniform bounds or a common partition for an inverse system without a further theorem.',
 'This is a cross-package dependency, not a settled result about the later valuation-ring or Greenberg promorphism. Later scans 126–132 must retain their own properness, boundedness and finite-index hypotheses.',
 'agrees','The current text explicitly questions the infinite-limit passage, so it cannot serve as an unconditional proof of the later contextual summary.')
add(268,[68],'other',[59,61,67,70,78,81,87,95,97],['2-27','29-528','530-536','686-723','916-997'],
 '« foncteur adjoint »; « Schémas localement compacts »',
 'The package contains an adjoint/representability programme and a separate constructible/schematic-set programme, plus reused printed mathematics. It does not contain the 1967 letter, K_G(X), a numerical pairing, a residue functional or a duality theorem.',
 'Book I placements and total-work estimates belong to absent project context, not to the pages. Counts distinguish 38 retained scans from any authorial page count.',
 'agrees','The full interval was read. The earlier planning note correctly refuses to infer missing subjects from generic words or printed tensor exercises.')
add(269,[69],'other',[98],['1005-1013'],
 '« système projectif »; « sous-groupe partout dense »',
 'The five named research-register entries LM7 E.23, FLAGGED_149 B9, LM1 D.11, LM4 D.12 and LM4 F.7 are external project leads. The current limit/topology results supply no comparison maps to their particular objects.',
 'Their reported statuses are not independently verified here; the underlying register files and target manuscripts are not attached in this part. Preserve them in the separate projects table.',
 'not on the page','The named external claims do not occur in the current manuscript. Reading a generic inverse-limit proof cannot check their arithmetic or group-theoretic conclusions.')
add(270,[70],'other',[61,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,93,95,97],['29-528','686-723','871-900','914-997'],
 '« de nature locale »; « A-t-on »',
 'The closing audit is an editorial synthesis of the locality, representability, gluing, preservation, constructibility and infinite-limit discussions already indexed above.',
 'It creates no additional mathematical claim. Its property list inherits the per-claim scope, the unresolved special-functor definition and the two independent witness conflicts on 93 and 95.',
 'understates','The table correctly distinguishes conditional existence and the open limit problem, but it predates the attached Codex evidence for the deletion of Corollary 3 and the editorial alternative on 95.',
 {70:('corrected','Retain as a synthesis, with the per-item witness conflicts and hypothesis qualifications carried through; do not count its rows as additional discoveries.')})

add(271,[],'self-flagged step',[77],['459-460'],
 'Pro: « n’est pas local … il n’existe pas »; Codex: « Cas où il n’existe pas même »',
 'The clipped lower edge may introduce a case in which the proposed right adjoint does not exist, beyond the explicit warning that it need not be local.',
 'No definite counterexample or universal nonexistence assertion is recoverable. The separate Codex lead is retained without inventing a Pro verdict row.',
 'agrees','Codex K91-06_notes.md:6 and K91-06_transcription.tex:144 preserve an existence lead which Pro 459–460 leaves partially illegible. Scheme-valued versus algebraic-space-valued restriction of scalars is a comparison, not an identification of the missing words.')
items[-1]['sources']=['codex/K91-06_notes.md:6']
items[-1]['lines'] += ['SA03_texts/codex/K91-06_transcription.tex:144']

for eid,src,ranges,scans,why in [
 ('K91-05','SA03_texts/codex/K91-05_transcription.tex','1-231','59,61-72','All thirteen sheets and the note file read; compared opening precision request, local-functor axioms and same-page cocycle check.'),
 ('K91-06','SA03_texts/codex/K91-06_transcription.tex','1-344','73-85','All thirteen sheets and notes read; compared type errors, qualifier on separatedness, clipped nonexistence lead and printed exercises.'),
 ('K91-07','SA03_texts/codex/K91-07_transcription.tex','1-302','87-98','All twelve sheets and notes read; compared deletion of Corollary3, presentation-finite wording, both limit questions and printed report provenance.'),
 ('cross58-59','SA03_texts/pro/MPL_91_019-058_transcription.tex','903-921','57-58','Read inherited finite π1-set and Rev ét internal-Hom test class; complete criterion owned by part a.'),
 ('cross97-99','SA03_texts/pro/MPL_91_099-143_transcription.tex','1-18','99','Read continuation of the two limit orders and the tentative geometric-category question.'),
 ('cross98-100','SA03_texts/pro/MPL_91_099-143_transcription.tex','19-39','100','Read immediately preceding printed report propositions23–24: density with surjective limit projections and openness of quotient maps.'),
 ('crossCons114-115','SA03_texts/pro/MPL_91_099-143_transcription.tex','396-451','114-115','Read later Cons sheaf/absolute-flat construction; distinguish it from the schematic-set inverse-limit failure.'),
 ('crossGreenberg126-132','SA03_texts/pro/MPL_91_099-143_transcription.tex','645-815','126-129,131-132','Read thickness doubts, restricted-Lie reuse of formula85 and later Greenberg rational-map programme, with its properness and boundedness qualifiers.'),
 ('crossPro136','SA03_texts/pro/MPL_91_099-143_transcription.tex','868-906','136','Read eventual-affine transition and quasi-compactness assumptions of pro-Hom statement; distinguish finite-presentation limit theorem from uniform partitions.')]:
 readlog.append(dict(entry_id=eid,source=src,lines=ranges,scans=scans,reading='Entire indicated actual transcription-file range read; no scans available.',reason=why))

def write_tsv(path,rows,fields):
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
(ROOT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
entries.sort(key=lambda x:int(x['entry_id'].split('#')[1]))
assert [int(x['entry_id'].split('#')[1]) for x in entries]==list(range(1,71))
write_tsv(ROOT/'entries.tsv',entries,['entry_id','item_id','verdict','reason'])
write_tsv(ROOT/'reading_log.tsv',readlog,['entry_id','source','lines','scans','reading','reason'])
write_tsv(ROOT/'item_events.tsv',events,['statement_id','date','who','type','outcome'])
print(json.dumps({'entries':len(entries),'items':len(items),'verdicts':{k:sum(x['verdict']==k for x in entries) for k in sorted(set(x['verdict'] for x in entries))}},indent=2))
