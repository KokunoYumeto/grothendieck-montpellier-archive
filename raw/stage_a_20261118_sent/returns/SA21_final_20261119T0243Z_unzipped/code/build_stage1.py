"""Serialize manually read and adjudicated entries. No heading-based verdicts.

Each A(...) below was authored after reading the entry and cited transcription.
The code handles schema, IDs, TSV escaping and coverage only.
"""
from pathlib import Path
import json,csv,datetime
W=Path(__file__).resolve().parents[1]
items=[]
def A(src,kind,cote,scans,lines,words,statement,reconstruction,reason,check='agrees'):
    items.append(dict(id=f'SA21-{len(items)+1}',sources=[f'MPL_156-1+156-2#{n}' for n in src],kind=kind,cote=cote,scans=scans,lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))

# Chapter I. These data are hand authored, not extracted verdicts.
A([1],'unpursued implication','156-1',[2],'49–55','forme de dim 0; ensemble discret; ens quotient',
 'A dimension-zero form is a discrete set. A model is a set L equipped with an equivalence relation, and its associated form is L/~. A recursive geometry in dimensions <=n is proposed, not constructed in these opening paragraphs.',
 'The quotient notation L/~ is modern notation for his explicit quotient. No higher-dimensional category is supplied here.',
 'The entry preserves the form/model distinction and confines the absence of a completed recursion to the supplied early pages.')
A([2],'other','156-1',[2,3,4,6],'59–101;112–132;214–228','ensemble des lieux; ensemble des segments; lieux intérieurs',
 'The revised data are sets L,S, a map I↦support(I)⊂L, and a map δ:S→P₂(L) with δI⊂support(I). Regular lieux are the union of support(I) minus δI; all other lieux are singular. These data alone do not specify a topology.',
 'support(I) denotes his tilde I. The abandoned extra relations in scans2–3 are excluded from the live data.',
 'All maps and the definition of regularity occur explicitly; the earlier L₀ data are within a deleted block.')
A([3],'other','156-1',[6],'230–241','Cette application est bijection',
 'F1: for each segment I, each endpoint x∈δI and each z∈support(I)∖{x}, exactly one segment J has support(J)⊂support(I) and δJ={x,z}. In particular Ixy=Iyx=I for δI={x,y}.',
 'This is an axiom, not an unproved theorem. It says nothing by itself about arbitrary internal pairs.',
 'The entry correctly restricts uniqueness to subsegments incident to an endpoint.')
A([4],'withdrawn in the same text','156-1',[6,24,25],'244–256;858–877','condition de divisibilité; divisible; réduit',
 'F2 originally assumes every segment has nonempty interior. For z internal to I with δI={x,y}, Ixz∩Iyz={z}, and every subsegment of I incident to z lies on one of these two sides. The later general network notion admits empty interiors and names the original nonemptiness condition divisibility.',
 'The uncertain marginal verb is not resolved. Admission of reduced graphs supplies independent textual evidence of the changed scope.',
 'The entry separates the retained separation conditions from the abandoned universal divisibility condition.')
A([5,24],'self-flagged step','156-1',[7,13],'299–337;561–565','Axiome des branches; relation d’équivalence; compléter F3',
 'For I,J incident to x, F3 gives initial subsegments which either coincide or meet only at x. The intended relation I~xJ is existence of a common nontrivial initial subsegment. The added F3′ requires common smaller initial segments within a fixed segment, so that these germs are transitive and their classes define Bx. In the nondivisible variant witnesses range over I∖{x}, not I°.',
 'The corrected semantic formula Ixz=Jxz follows the unambiguous dichotomy and scan23, but the printed uncertain formula at line322 is preserved in the readings table. Transitivity is checked separately, not inferred merely from a dichotomy.',
 'Both entries describe the same branch-equivalence and missing-local-filtering issue; #24 supplies its proof obligation.')
A([6,21],'other','156-1',[5,8],'161–166;360–366','on n’affirme pas égalité!',
 'F4: if support(I′)∩support(I″)=δI′∩δI″={z}, with z regular and other endpoints x,y, there is exactly one segment I with δI={x,y} and support(I)⊃support(I′)∪support(I″). Equality with that union is explicitly not required.',
 'In the order model the omitted lieux may be incomparable with z; this interpretation is additional explanation, not a replacement of the axiom.',
 'The warning is explicit in two places. #21 is merged as the same substantive limitation, not treated as a second theorem.')
A([7],'unproved claim','156-1',[9],'390–401','Équivalent à',
 'Under the preceding subdivision, branch and gluing assumptions, F5 (each regular x has exactly two branch classes) is asserted equivalent to F5′: the sets I° containing x form a filter base, meaning any two contain a third such interior.',
 'The strengthened branch convention is required when formalizing the equivalence. No cardinality bound on L or S follows.',
 'The two formulations are present; the page announces equivalence without a complete proof.')
A([8,40,41],'unproved claim','156-1',[8,9,23],'370–387;826–847','On n’exige pas; Ou encore; I∪J⊂K',
 'Weak F6 requires, for two segments sharing endpoint x and branch there, a segment K incident to x with I°∪J°⊂K°. Strong F6 instead requires I∪J⊂K. These are not equivalent at singular other endpoints. In the poset (Q∩[0,1))⊔{u,v}, with all rationals below both incomparable maxima and all comparable-pair intervals as segments, weak F6 holds but [0,u],[0,v] have no common containing segment. If the other endpoints are regular, extension beyond them followed by weak F6 gives strong containment.',
 'The named counterexample and repair are ideas of the earlier run (#40–41), independently rechecked here. They do not refute the special equal-endpoint lemma. The manuscript provides both distinct formulations and the regular-end qualification.',
 'The entries correctly identify a genuine hypothesis mismatch. Their examples are merged with the exact equivalence they test; all axiom checks are in audit/root_proofs.md.')
A([9,42],'other','156-1',[7,24,25],'313;858–877','réseau; noeuds; lignes; graphe réduit',
 'A réseau is the revised F1–F6 segment structure; singular lieux are nodes and regular incidence components are lines. Divisible means every I° is nonempty; reduced means every segment has support δI and Lr=∅. With branch witnesses adapted to nondivisible segments, reduced networks are simple undirected graphs S⊂P₂(L), without a finiteness assumption.',
 'The graph assertion uses the explicit witness revision on scan7. Reading the earlier interior-witness clause literally would reject nonempty reduced graphs.',
 '#42 explicates the same definitional revision as #9; it is not evidence that the graph claim is inconsistent after the revision.')
A([10,31],'unproved claim','156-1',[11,12,13,14],'444–577','biordre; Inversement; loc. bifiltr.',
 'A segment model with support L and two endpoints is asserted equivalent to a pair of opposite partial orders with distinct least and greatest elements, density, and local filtering in both directions: for x<y,z there is u with x<u≤y,z, and dually. Choosing the least endpoint defines x≤y by [x₀,x]⊂[x₀,y]. Segments correspond to comparable pairs with support [x,y].',
 'The quantifiers use the clear strict version at scan13, not the inconsistent later mixed strict/nonstrict formula. The converse concerns the strengthened pre-F6 segment axioms, not automatically either later global F6.',
 'The notes correctly preserve partial rather than total order and identify the missing local hypothesis; merging avoids counting the same reconstruction twice.')
A([11,47],'unproved claim','156-2',[2,3],'1092–1128','voisinage fermé; Cône; espace topologique compact',
 'For closed nonempty A⊂X, regular immersion means the collapsed point a∈X/A has a closed neighborhood V homeomorphic to a cone on a compact base B, with a the vertex and V∖B open. Uniform radial subcones Vt (0<t≤1) and their open interiors form cofinal neighborhood systems; their inverse images form such a system along A.',
 'The cofinality proof uses compactness of B. This is regular immersion in his terminology, not a smooth, algebraic or pointwise locally flat embedding. He explicitly adopts an apex-only cone for B=∅.',
 'Definition and neighborhood claim occur consecutively. #47 is the explanation of the compact-base requirement in #11.')
A([12],'other','156-2',[3,4,9],'1160–1223;1419','ficelle topologique; fermés, non ouverts',
 'A ficelle is (X,{A,B}) with disjoint closed nonopen ends, regularly immersed in X, and connected spaces (X∖A)/B and (X∖B)/A. It is reduced if both ends are points; orientation chooses one end. Neither connectedness of each end nor connectedness of X is stipulated in the unrestricted definition.',
 'The punctuation doubt in non-ouverts does not affect the negation. Nonemptiness follows because ∅ is open.',
 'The entry correctly resists adding the later suggested connected-end condition to the earlier definition.')
A([13],'other','156-2',[5,6,7,8,9,10],'1231–1278;1286–1331;1359–1367;1413–1452','Découpage; lieu; homeo. de raccordement',
 'An internal lieu C is a closed subset disjoint from A∪B for which X∖C splits into two open-and-closed sides containing A and B, each connected after collapsing its end; C is regularly immersed in X∖(A∪B). The closed cut pieces are closure(UA,C)∪C and closure(UB,C)∪C. Ends themselves are also lieux. Simultaneous cuts must be compatible in the defined stronger sense.',
 'The closure notation follows the clear scan6 notation, without deciding overwritten U/X glyphs on scan5. The finite-chain equivalence is indexed separately.',
 'The entry accurately combines the definition across its successive pages, retaining regular immersion and side conditions.')
A([14,79,80],'other','156-2',[15,16],'1580–1604;1620','Comp(Z)=Hom_cont(Z,{0,1}); lim→',
 'Comp(Z) is the Boolean ring of clopen subsets of Z, with symmetric difference and intersection. Riv(A,X)=colim_{V⊃A}Comp(V∖A) under restriction as neighborhoods shrink. Its elements are germs along the whole closed set A. They are not individual connected components and need not record all link topology.',
 'Boolean ring terminology restates his commutative idempotent F₂-algebra. The source uses both Riv and Rives.',
 'The three entries concern the same definition and the same π₀-versus-clopen correction; all are retained in one item.')
A([15,89],'other','156-2',[15,16,17,18],'1578;1622–1632;1642;1675–1677','ρ+ρ′=1; maille',
 'A birive is an unordered complementary pair β={ρ,ρ′} in Riv(A,X); for a nonzero ring its entries are distinct, and {0,1} is trivial. A maille additionally requires regular immersion and the stated ficelle conditions on the cut space; its orientation chooses one member of β. The definition replaces the earlier term boucle topologique.',
 'The existence of a complementary pair alone does not establish the geometric conditions. Full-cut/partial-cut equivalence has its own claim record.',
 '#89 adds the terminology history to the same distinction made in #15.')
A([16],'reading question','156-1;156-2',{'156-1':'1–27','156-2':'1–19'},'entire Pro transcription,1–1717','maille; Réalisations topologiques des réseaux',
 'No atelier/workshop is defined in cotes156-1–2. Maille on 156-2/17 is a different defined object. This negative finding has only that local scope; later cotes of the current dossier do define ateliers.',
 'The later cross-reference is supplied by this consolidation. It corrects a possible global use of the note, not the note’s explicitly limited wording.',
 'The entry itself limits the absence to 46 scans, so it is kept rather than refuted by the later atelier chapters.')
A([17],'withdrawn in the same text','156-1',[3,25,26,27],'87;881–1039','Je présume; au plus deux segments',
 'In the cancelled initial proposal, each adjacent endpoint pair is expected to determine at most two segments, with two exactly in a circle-like component. Later equal-endpoint intersection arguments remain unfinished; the cancelled classification is not an established theorem of final networks.',
 'Circle-like is left at the source’s undeveloped model-of-a-circle level, not identified with a homeomorphic circle.',
 'The deleted block and the unfinished later proof support the note’s distinction between an abandoned formulation and continuing interest.')
A([18],'self-flagged step','156-1',[3,4,7],'89;120–122;297','J’ignore; Si tilde I=tilde J alors I=J',
 'The initial data do not assume support injectivity. The author asks whether support and endpoints determine I, then asserts the stronger conclusion that equal supports imply equal segments, enabling S⊂P(L). This follows from F1–F2 once all their separation and side-containment clauses are used.',
 'The short derivation in audit/root_proofs.md is a proof supplied in this run, not one written at the corollary.',
 'The note accurately reports the chronology; its warning against assuming the conclusion is justified.')
A([19],'withdrawn in the same text','156-1',[2,3,10],'59–101;425–427','ne sont pas disjoints; relation d’équivalence',
 'A cancelled initial definition puts a non-disjointness equivalence relation on critical lieux and calls its quotient critical points. Scan10 later proposes an equivalence relation on singular lieux, without completing its interaction with segments or a quotient form.',
 'The two occurrences are related documentary evidence, not an established final quotient construction.',
 'The cancellation and later future tense support the note’s status; no completed theory is inferred.')
A([20],'withdrawn in the same text','156-1',[5,6,7,8,9],'145–206;230–401','décomposition; recollement; Filtration',
 'The crossed-out first F1–F3 draft mixes subdivision, small internal segments, gluing and containment of every finite interior subset in a smaller interior segment. The later live list is a new formulation, not the conjunction of all earlier clauses.',
 'A finite-set containment condition is stronger than a pointwise shrinking condition; this logical comparison is ours and the earlier note’s, not an additional axiom.',
 'The deleted blocks and reused numbering were read directly and support the documentary verdict.')
A([22],'unproved claim','156-1',[5,6,24,25],'175–178;254;864–877','I° est infini; condition de divisibilité',
 'Under universal nonempty interior and F1–F2, every nondegenerate segment has infinitely many internal lieux and infinitely many subsegments. Repeated subdivision gives arbitrarily many distinct points and segments. This fails for the later reduced-graph variant.',
 'The induction is re-proved in this run. It is conditional on divisibility, not an infinitude claim for every réseau.',
 'The note preserves exactly the hypothesis explicitly named by the source.')
A([23],'unproved claim','156-1',[6,7],'258–295','Cette application est injective; conditions équivalentes',
 'For S_I={J:support(J)⊂support(I)}, δ:S_I→P₂(support(I)) is injective. Its image contains all endpoint-incident pairs. An internal pair {u,v} is in the image iff v∈Ixu or v∈Iyu, equivalently u lies in the corresponding opposite initial/final subsegment based at v.',
 'The uncertain marginal extension to endpoint cases is not substituted into the statement; the main internal-pair assertion is clear. A proof uses F1–F2.',
 'The entry correctly avoids claiming every pair is admissible and identifies the order-reconstruction role.')
A([25],'unproved claim','156-1',[8,9],'369–387','prolongement; x régulier',
 'If x is a regular endpoint of I with other endpoint y, F1–F4 with the strengthened branch condition imply a larger segment J with endpoint y and x∈J°. If both endpoints are regular, a larger segment has I⊂J°.',
 'The author gives a proof sketch through an opposite branch and F4. The argument does not apply at arbitrary singular endpoints.',
 'The note follows the written proof sketch and correctly limits its use in repairing F6.')
A([26],'unpursued implication','156-1',[9],'402','parties modérées; F1):F4)',
 'For a tame category in which embedded compact arcs have finite local intersection behavior, taking all embedded arcs as segments supplies the intended F1–F4 examples. In a plane, distinct arc germs at a point need not reduce to two branches, so F5 is a real extra restriction.',
 'The plane example is explanatory. The manuscript does not define a tame category here, and the final F5/F6 wording remains uncertain; no theorem for arbitrary wild arcs is claimed.',
 'The note is appropriately qualified: it does not turn an unfinished marginal remark into a universal realization theorem.')
A([27],'unproved claim','156-1',[9,10],'404–416;429–438','partie quelc.; les axiomes F1-F5 sont satisfaits',
 'The author asserts that for every L′⊂L, retaining precisely all ambient segments supported in L′ preserves F1–F5. This is false: F4 may require extra support outside L′ even though its two component segments and a regular joint remain inside L′.',
 'The refutation is provided by the earlier-run example in the next item and rechecked here; it is not a reading correction.',
 'The note accurately quotes the unrestricted assertion and locates the specific axiom at risk.')
A([28],'idea of the earlier run','156-1',[8,10],'360–366;429–438','on n’affirme pas égalité!',
 'Let L=(Q∩[0,1))⊕((Q∩(1,2))⊔(Q∩(1,2)))⊕(Q∩(2,3]), ordered within each chain and by the ordinal sum, with all nondegenerate comparable-pair intervals as segments. This satisfies strengthened F1–F5 and both F6 versions. For z=(3/2,0), L′=[0,z]∪[z,3] excludes the other middle chain. z remains regular, but its two retained adjacent intervals have no retained F4 composite.',
 'This construction is explicitly the earlier run’s idea, not Grothendieck’s. The old referenced memo was not attached; all hypothesis checks are reconstructed independently in audit/root_proofs.md.',
 'The text supplies the axiom and failed restriction claim, not the counterexample. Its attribution is preserved.', 'not on the page')
A([29],'idea of the earlier run','156-1',[8,10],'360–366;429–438','les axiomes F1-F5 sont satisfaits',
 'For inheritance under L′⊂L, closure under every ambient F4 composite of retained pieces with a joint regular in the restricted structure is necessary. Order-convex subsets of a fixed interval-poset model give a natural sufficient setting, but a general réseau inheritance theorem requires additional branch and regularity checks.',
 'The repair is proposed by the earlier run. The necessity follows from F4; general sufficiency is not asserted as proved.',
 'The entry correctly labels its full repair as tentative, rather than replacing the false manuscript assertion.', 'not on the page')
A([30],'reading question','156-1',[10,24,25],'425–427;864–877','S=∅ (i.e. si Lr=∅)',
 'Under divisibility, S=∅ iff Lr=∅. After empty-interior segments are admitted, only S=∅⇒Lr=∅ remains; a nonempty simple reduced graph has Lr=∅ and S≠∅.',
 'This is a version distinction, not evidence of an uncertain glyph.',
 'The note correctly prevents transporting the earlier equivalence into the revised axioms.')
A([32],'unproved claim','156-1',[15,16],'591–611','relation d’équivalence engendrée; somme directe',
 'On a regular model, the equivalence relation generated by pairs lying in a common segment defines incidence components. The model is the direct sum of its components, each regular. Connectivity means connectedness of this incidence/comparability relation, without a specified topology on L.',
 'Direct sum means disjoint union of lieu and segment data; no global directedness follows from connectivity.',
 'The note keeps the author’s combinatorial use of π₀ separate from an absent topology.')
A([33],'self-flagged step','156-1',[16,17,18],'613–674','Je n’ai pas la vérification ici; Si c’était faux',
 'For a nonempty regular connected model, the author proposes a unique coherent system identifying all endpoint pairs δI and branch pairs Bx, whose common quotient has two elements and separates each pair. He explicitly leaves verification open and says it would need to be an axiom if false. Even the claim of one or two quotient classes is qualified.',
 'The exact orientation transitions and F1–F6 version must be fixed before judging global orientability. No complete proof or countermodel is attributed here.',
 'The entry faithfully reports an explicit author-marked gap, rather than treating the displayed Th as proved.')
A([34],'idea of the earlier run','156-1',[16,17,18],'629–674','syst. transitif; exactement deux classes',
 'Model the prescribed bijections between two-element endpoint/branch sets as a transport graph. The quotient has two classes precisely when the induced transport around every closed walk is trivial, provided the graph is connected; a transposition identifies the two labels.',
 'This is the earlier run’s proof strategy. Reduction to a Z/2 monodromy test does not establish that the network axioms force trivial monodromy.',
 'The source motivates the strategy but does not contain this modern formulation.', 'not on the page')
A([35],'reading question','156-1',[18,19],'680–713','cas linéaire; transitive; cas circulaire',
 'After choosing an orientation, x<y means that a segment has origin x and end y. The linear case is defined by transitivity of this relation; it then yields an antisymmetric partial order. Total comparability is not asserted. Nontransitivity is called the circular case, without a completed classification.',
 'Linear here is his terminology, not a synonym for a total order or the real line.',
 'The defining distinction is explicit, and the note correctly avoids strengthening it.')
A([36],'reading question','156-1',[13,19],'561–563;709','si x≤y,z; x<u<y,z',
 'The literal revised implication x≤y,z⇒∃u(x<u<y,z) is impossible when y=x. A strict antecedent x<y,z is consistent with the earlier local-filtering formula. Ink or author revision must decide the intended reading.',
 'The strict alternative is mathematical diagnosis only. The transcription is unchanged.',
 'The equality specialization is an immediate contradiction and supports the note’s reading alarm.')
A([37,38,39],'withdrawn in the same text','156-1',[19,20,21,22,23],'709–816;826–847','n’est pas néc. filtrante croissante; F6',
 'Connectedness, local bidirectedness of strict cones and extension on both sides do not imply global directedness. The author’s attempted proof is withdrawn and replaced by an ordinal-sum fork. The earlier run’s precise instance Q⊕(Q⊔Q) has connected comparability graph and satisfies strengthened F1–F5 but incomparable upper arms have no common upper bound. F6 adds the missing common-extension condition within a branch.',
 'The rational-chain specialization is the earlier run’s reconstruction of the author’s mechanism; the displayed existential quantifier and unspecified family size in the general source example are retained as reading/formulation issues.',
 'All three notes concern the same failed local-to-global step and its remedy. The counterexample’s hypotheses are checked independently in the proof appendix.')
A([43],'unproved claim','156-1',[26],'1009–1020','On ne va pas exiger y régulier; en vertu de F6',
 'For two segments with the same endpoints {x,y}, distinct branches at y are claimed to imply distinct branches at x. The argument assumes a common containing segment K to invoke F1. This follows from strong F6; weak interior-F6 does not immediately retain a singular y.',
 'The two-distinct-maxima example refutes only general weak/strong equivalence, not this equal-endpoint lemma. The latter remains a separate proof obligation under weak F6.',
 'The note carefully identifies a gap in the written proof without asserting an unproved counterexample.')
A([44],'unproved claim','156-1',[26,27],'1022–1039','Je dis que I∩J={x,y}',
 'Two equal-endpoint segments with distinct endpoint branches are claimed to intersect only at their endpoints. The author starts a contradiction using a common internal t and F5, but the supplied text stops mid-branch formula.',
 'A completion must specify which F6 version supplies the preceding equal-endpoint lemma. No missing conclusion is inserted.',
 'The entry matches the physical stopping point in the supplied transcription.')
A([45,114],'unpursued implication','156-1;156-2',{'156-1':'24–27','156-2':'2–19'},'858–1039;1090–1712','Réalisations topologiques des réseaux',
 'Cote156-1 gives abstract interval data; cote156-2 begins with topological spaces and constructs ficelles, cutting orders, rives and mailles. These two cotes do not prove existence or uniqueness of a topological realization for every abstract F1–F6 network, or recovery of a space from its abstract réseau.',
 'This local absence claim is not extended to all later cotes. Later atelier realization and reconstruction proposals receive their own claims.',
 '#114 repeats the scope caution of #45 with the final symmetry stopping point; both were checked against the full two-cote text.')

# Chapter II and comparisons. Formula strings use Unicode set difference.
A([46],'unproved claim','156-2',[2],'1092–1096','identifie ... à un sous-espace top.',
 'For closed A⊂X and any A⊂X′⊂X, the induced map X′/A→X/A is a topological embedding. Relatively closed saturated subsets of X′ are traces of closed saturated subsets of X: take their ambient closures, which still contain all of A or avoid it.',
 'The proof is completed here; the written final target “de X” is not silently replaced by X/A in the transcription.',
 'The note correctly supplies the missing argument without requiring normality; the target mismatch remains a scan question.')
A([48],'unproved claim','156-2',[3],'1145–1158','L’hyp. faite ... est locale; modéré compact',
 'Regular immersion of A is unchanged on replacing X by a neighborhood of A. The author also asserts it for compact tame subspaces of tame spaces, including compact subpolyhedra. For a finite simplicial pair (K,L), a regular neighborhood of |L| has mapping-cylinder structure, so collapsing |L| gives the required compact-base cone neighborhood.',
 'The finite polyhedral formulation is precise; the unrestricted tame assertion has no specified category in this page and is not inferred from pointwise conical stratifications.',
 'The note accurately separates a local shrinking argument from the broader unformalized tame assertion.')
A([49],'reading question','156-2',[3],'1128–1142','W′t=X−Vt',
 'Vt lies in X/A whereas Wt is its inverse image in X. The formula W′t=X−Vt mixes ambient spaces; X−Wt would give the intended exterior term in the subsequent disjoint decomposition.',
 'Replacing V by W is a suggested ink check only. No source reading is changed.',
 'The note identifies a concrete type mismatch in the literal formula.')
A([50],'unproved claim','156-2',[4],'1179–1198','c′⇒c; l’inverse ... fini',
 'For disjoint closed nonopen A,B, if every connected component of U=X∖(A∪B) has closure meeting both ends, then the two end-contracted punctured spaces are connected. Conversely, if U has finitely many components and those quotients are connected, each component closure must meet both ends.',
 'The finite-component reverse direction uses that components are then closed and open in U; no infinite-component converse is claimed.',
 'The entry preserves the explicit finiteness qualifier, and the proof is reconstructed separately.')
A([51],'unproved claim','156-2',[4],'1206;1214–1221','alors ... est une ficelle; ssi',
 'A ficelle is preserved by contracting a closed C⊂X∖(A∪B). Separately contracting A and B to distinct points preserves and reflects the ficelle conditions. Quotients preserve the required connectedness, and neighborhoods can be chosen off the other closed sets, leaving the local conic condition unchanged.',
 'This does not imply connectedness of the original space when the collapsed ends were disconnected. The quotient arguments are checked, not borrowed from a tame hypothesis.',
 'The two source assertions are correctly grouped as the contraction mechanism used by later proofs.')
A([52],'unproved claim','156-2',[4,5],'1223;1236–1245','Ficelle réduite est connexe',
 'If the ends are distinct nonisolated closed points a,b and X∖{a}, X∖{b} are connected, then X is connected: these two connected sets cover X and intersect in the nonempty interior. X∖{a,b} may be disconnected, as for a circle.',
 'Nonempty intersection follows from nonisolation: X cannot consist of the two closed points alone. No corresponding unrestricted nonreduced claim follows.',
 'The entry precisely limits the conclusion to reduced ficelles.')
A([53],'reading question','156-2',[5,6],'1253–1278;1286–1289','X_{A,C}=closure(U_{A,C})∪C',
 'The open side UA,C⊂X∖C and the closed cut piece XA,C=closure(UA,C)∪C are different spaces. Scan5 has uncertain overwritten U/X symbols; scan6 gives the closed-piece definition clearly.',
 'This distinction is used in proofs without deciding the order of pen revisions.',
 'The entry records a mathematically consequential notation ambiguity instead of harmonizing it.')
A([54],'unproved claim','156-2',[5],'1264–1278','de façon unique; Quand A,B connexes',
 'After contracting the two ends, the two sides of a lieu are the inverse images of the two connected components of X′∖C, one containing a and one b; hence they are unique. The original sides themselves are connected if A and B are connected.',
 'Connectedness of a quotient plus connectedness of its collapsed closed subset reflects connectedness, by a separation argument. The source’s additional connected-end clause is genuine.',
 'The note properly uses the explicit qualification as evidence that connected endpoints were not an earlier axiom.')
A([55],'reading question','156-2',[6],'1302–1308','X∖{c} ne serait pas connexe',
 'The contradiction proof constructs a nontrivial clopen subset of X∖{a}; its conclusion should contradict connectedness of X∖{a}. The written final X∖{c} is already expected to be disconnected by the cut.',
 'The alternative a for c is mathematical diagnosis, not an emendation.',
 'The note follows the proof’s actual ambient space and flags the exact terminal mismatch.')
A([56],'self-flagged step','156-2',[6,7],'1291–1311;1317–1324','il manque encore ... d) d’immersion locale',
 'The proposed closed cut pieces satisfy the first three ficelle conditions, but the author expressly requires an additional regular-immersion condition before calling them ficelles. He then imposes regular immersion of C in X∖(A∪B) and invokes the cone-gluing lemma.',
 'The intended covered-space lemma is distinguished from the more general, literally false statement printed on scan7.',
 'The note correctly distinguishes an acknowledged missing hypothesis from an automatic consequence of the first three conditions.')
A([57,58],'unproved claim','156-2',[7],'1317–1324','Z′∩Z″={c}; il f. et s.',
 'The literal assertion that c is conical in Z iff it is conical in closed Z′,Z″ meeting only at c omits that they cover a neighborhood. It is false for Z=Q, c=0, Z′={0,1}, Z″={0,−1}: c is isolated and hence conical in each piece, but Q has no compact neighborhood. With a neighborhood covered by two closed pieces meeting only at c, the cone statement has the intended wedge proof.',
 'The rational counterexample belongs to the earlier run; the full hypothesis check is repeated here. The cover hypothesis is a proposed repair, not recovered ink.',
 'The note and countertest address exactly the same missing ambient-cover condition and are merged.')
A([59],'unproved claim','156-2',[7],'1326–1338','Pour t assez petit; encore un lieu',
 'Sufficiently small boundary cross-sections of an endpoint cone are claimed to be internal lieux. The author also asserts that contracting a closed subset D wholly contained in one side preserves the ambient ficelle and its other cutting locus. The side contains its end, and the previous end-disjointness condition is deleted.',
 'The note reports the claims and requests tracking endpoint regularity. The current consolidation adds a finite tripod counterexample to the literal second claim when D meets an end; see C-SA21-2-017 and R-SA21-side-contraction. This is a current-run finding, not an earlier-note example.',
 'The note accurately reports both assertions and signals the need to check preservation. Its report does not itself prove the side-contraction claim; the new mathematical verdict is recorded separately.')
A([60],'other','156-2',[7,8,9,10],'1340–1348;1374–1377;1413–1417;1448','disjoint signifie que',
 'Distinct internal lieux C,D are called disjoint when D is a lieu of one of the two cut ficelles at C; the exchange lemma supplies symmetry. If either is an end, disjoint means distinct. This relation is stronger than C∩D=∅ and becomes strict comparability in the oriented cutting order.',
 'The alternating two-point separators on a circle supply a counterexample to replacing this relation with set disjointness; that is an earlier-run example, indexed separately.',
 'The definition and its symmetry dependency match the note exactly.')
A([61,63,66,100],'unproved claim','156-2',[8,9,10],'1364–1368;1421–1425;1452','Équiv. de Catégories; quintuplets; n+1 ficelles',
 'A ficelle with one internal lieu is asserted equivalent to two ficelles with a specified homeomorphism of chosen ends. For n ordered pairwise compatible internal lieux, the data are n+1 oriented ficelles and n endpoint homeomorphisms; n=2 is explicitly a quintuple. A precise categorical statement uses endpoint-preserving homeomorphisms commuting with all gluing maps, with cutting and pushout as quasi-inverse functors.',
 'The explicit morphism convention and induction are reconstruction; the source does not define them. The pieces and maps are geometrical data, not finite sets or an unlabeled incidence chain.',
 'Four entries concern the same family of cutting/gluing equivalences; all cardinalities, hypotheses and the doubtful repeated F₁ glyph are retained.')
A([62,76],'unproved claim','156-2',[8,13],'1374–1404;1506–1528','D est un lieu ... ssi C est un lieu',
 'For distinct internal lieux C,D, D is a lieu of F_{B,C} iff C is a lieu of F_{A,D}. The live proof contracts the four marked sets to points and re-associates X_{a,c}⊔c X_{c,d}⊔d X_{d,b}. The cancelled scan13 rehearsal is not an explicit refutation of the live scan8 lemma.',
 'Associativity is an ordinary pushout fact, while preservation of the ficelle conditions is part of the geometric proof obligation.',
 'The entries correctly distinguish a cancelled duplicate argument from an author-declared false assertion.')
A([64],'unproved claim','156-2',[9,10],'1427–1438','C≤D ssi F_C⊂F_D',
 'For an oriented ficelle with initial end A, let F_C be the family of lieux of F_{A,C}, with endpoint conventions. Define C≤D iff F_C⊂F_D, asserted equivalent to C∈F_D. Inclusion, or equality, of the underlying regions X_{A,C},X_{A,D} is expressly insufficient.',
 'The negative warning is secure although its overwritten local typography remains uncertain.',
 'The note accurately preserves the richer cutting-family order instead of replacing it by region containment.')
A([65],'unproved claim','156-2',[10],'1437–1448','filtrant décroissant; divisibilité',
 'The oriented lieu poset is claimed to have distinct minimum and maximum; for each x other than the maximum, {y:y>x} is downward directed, and dually below x; each x<y admits z with x<z<y. Compatible distinct lieux are exactly comparable ones.',
 'The construction should use common small endpoint collars in sub-ficelles. The assertion is geometrical and generally infinitary, not an order-theoretic tautology.',
 'The note reports the exact direction of each filtering clause and does not assert finite cardinality.')
A([67],'unproved claim','156-2',[11],'1463','connexe, et non réduit à un point; unique',
 'The compact-triangulable NB combines four claims: ficelle existence implies connectedness and nontriviality; connected nontrivial spaces of that class admit reduced ficelles; an interval has a unique reduced structure; it is the only reduced uniqueness exception. The first necessity fails with disconnected ends. The latter assertions hold for connected finite polyhedra, with proofs in this dossier.',
 'The bundled sentence is split into separate claim records so that one false part does not erase its true reduced statements.',
 'The note explicitly makes this separation and is accurate.')
A([68],'idea of the earlier run','156-2',[4,11],'1172–1223;1463','qu’il soit connexe',
 'For X=[0,1]×{−1,+1}, A={0}×{−1,+1}, B={1}×{−1,+1}, X is disconnected. All four ficelle axioms hold: ends are closed disjoint nonopen, endpoint contractions have two-arm compact-base cone neighborhoods, and each punctured quotient joins its two arms at the other collapsed end.',
 'This is the earlier run’s counterexample, not a manuscript example. The quotient maps (t,e)↦et and (t,e)↦e(1−t) and the finite graph certificate recheck all hypotheses.',
 'It refutes the exact nonreduced connectedness assertion while leaving the reduced theorem intact.', 'not on the page')
A([69,70],'unproved claim','156-2',[4,11],'1172–1181;1465–1473','les seules ... ficelles sur [0,1]',
 'The stated classification A=[0,α], B=[β,1], 0≤α<β≤1 (up to exchange), requires connected ends. Under the literal definition X=[0,1], A={0,1}, B={1/2} is also a ficelle: X/A is a circle, both punctured end-contracted spaces are connected open intervals, and the ends are conical. Thus the unrestricted classification is false.',
 'The counterexample is the earlier run’s idea and is independently rechecked. The connected-end repair follows because connected closed interval subsets are intervals and connectivity of punctured quotients forces the two outer ends.',
 'The two entries concern the same omitted hypothesis; the doubtful prime on β is an independent ink issue.')
A([71,72],'withdrawn in the same text','156-2',[11],'1473–1477','Faux → idiot!; Connexité',
 'Enlarging the ends of a ficelle to disjoint closed regularly immersed sets need not preserve a ficelle. On a tripod take two leaves A,B, then enlarge A to its closed arm including the central vertex. The enlarged end is connected, contractible and regularly immersed, but its complement has two components and collapsing the singleton B cannot join them.',
 'The author retracts the rule himself; the tripod is the earlier run’s explicit witness, checked here with all four hypotheses. It also defeats the proposed rescue by connected or contractible ends alone.',
 'The note reports an explicit retraction, and the companion example tests exactly the discarded rule.')
A([73],'withdrawn in the same text','156-2',[11],'1467–1480','soupçonne; Faux déjà dans le cas du segment!',
 'The conjecture that all oriented ficelle structures on a triangulable X are equivalent under the equivalence relation generated by coordinatewise endpoint inclusion is withdrawn. In the connected-end interval subfamily the two orientations form distinct classes, each with its minimal point-end pair. This exact count is not established for the unrestricted disconnected-end family.',
 'The two-class statement is a restricted elementary reconstruction, not the author’s universal conclusion.',
 'The note accurately preserves both the withdrawal and the limited scope of its explanatory count.')
A([74],'conjecture','156-2',[12],'1489–1496','il est bon de ... supposer',
 'To retain the cutting-order properties after restricting endpoints and lieux by an intrinsic property P, the author proposes also requiring P for the boundary of each relevant conic neighborhood on both sides. A uniform sufficient theorem for arbitrary P is not formulated or proved.',
 'A precise future formulation must specify a category and closure conditions on P under the actual collar/refinement operations.',
 'The entry correctly treats suggested sufficient hypotheses as a program, not an established all-P theorem.')
A([75],'unpursued implication','156-2',[12],'1494–1496','être ... réduit à un pt; segments top.',
 'Choosing P=being a point is said to give a theory of topological segments. The strongest secure reading is a special cutting theory with point ends, allowed lieux and side links, not an automatic classification of every ambient X as an interval.',
 'The final abbreviation ord./ind. is left uncertain. A connected-end pair alone would allow, for example, many noninterval spaces.',
 'The note appropriately avoids expanding an illustrative sentence into a global classification theorem.')
A([77],'unpursued implication','156-2',[13,14],'1530–1558','B^n; décompositions par des S^n',
 'Ball-shaped and sphere-shaped admissible loci illustrate the property-P cutting theory in I×B^n and in S^{n+1} with two marked points. Every proposed locus must still satisfy the separating-side and regular-immersion conditions; its abstract homeomorphism type alone is insufficient.',
 'No claim about all embeddings, wild embeddings or automatic local flatness is supplied.',
 'The notes match the examples and preserve the preceding admissibility conditions.')
A([78],'other','156-2',[14],'1568','On peut aussi exiger; C×]−1,1[',
 'A bicollar C×(−1,1), with its two half-products in the two cut pieces, is offered as an additional condition on an internal lieu. It is stronger than the original condition on a cone neighborhood after collapsing the entire C.',
 'A cone on three points distinguishes conical from interval neighborhoods at a vertex, but does not by itself provide an internal-lieu counterexample; the note explicitly says so.',
 'The source’s optional phrasing and the limited role of the explanatory example are correctly retained.')
A([81],'unproved claim','156-2',[15],'1592–1595','Riv(A,X)≃Comp(S_{A,X})',
 'For a regular immersion with a chosen compact cone base S, the rive algebra is canonically identified through that conic structure with Clop(S). Cofinal punctured cones are S×(0,t), and a clopen subset is constant along each connected radial fiber.',
 'The abstract germ algebra is intrinsic, but no uniqueness theorem for the topological type of every possible cone base is asserted.',
 'The note gives a valid local product/cofinality proof strategy and avoids recovering the whole link from its clopens.')
A([82],'unproved claim','156-2',[15,16],'1597–1604;1613–1620','bijective si X paracompact',
 'For a closed A in a paracompact Hausdorff X and a sheaf of k-modules F, the restriction map colim_{V⊃A}Γ(V,F)→Γ(A,F|A) is an isomorphism. It is injective without the paracompact hypothesis. Applied to i_*F₂ on X, it compares the rive ring to sections on A; interpreting Comp(Ã) additionally requires a precise relative spectrum convention.',
 'Hausdorffness is explicit in the opened modern sheaf reference’s convention. Its theorem verifies the section comparison, not every unspoken topological property of the manuscript’s cut space.',
 'The note correctly narrows the cited standard theorem to closed A and distinguishes the spectrum interpretation.')
A([83,84],'reading question','156-2',[15,17],'1602–1604;1645–1666','Ã=Spec(i_*F₂,U); Ã_i→A',
 'The page leaves the base of Spec implicit. A modern relative ringed-space spectrum over X, restricted above A, retains the map to A needed by the subsequent pushouts. For X=S¹×[−1,1], A=S¹×{0}, this relative Stone boundary is two circles; the étalé space of ring elements is four circles; Spec of the global rive algebra F₂² is two points.',
 'The relative-spectrum formalization and the cylinder test belong to the earlier run and are rechecked here. They are not a decision about the manuscript’s intended missing convention.',
 'The definition gap and its diagnostic example concern one issue. The two-circle/four-circle/two-point distinction is mathematically correct.')
A([85],'unproved claim','156-2',[16],'1620–1630','nulle ssi A est ouvert; ρ+ρ′=1',
 'For closed A, Riv(A,X) is the zero ring iff A is open: 0=1 in the filtered colimit iff some neighborhood has empty complement of A. In a nonzero Boolean ring, ρ and 1+ρ are distinct and define complementary clopens in its Stone spectrum; {0,1} is the trivial pair.',
 'This uses the zero-ring convention explicitly allowed on the page. A birive alone does not satisfy the geometric maille axioms.',
 'The elementary Boolean checks agree with the note and are rerun in code/root_checks.py.')
A([86],'idea of the earlier run','156-2',[16],'1622–1632','disconnect X loc.',
 'For two points A={p,q} in R², disjoint punctured-disk neighborhoods give Riv(A,R²)=F₂². A nontrivial global birive exists although each individual punctured disk is connected. Thus the author’s whole-A germ disconnection need not be pointwise separation at every a∈A.',
 'This is the earlier run’s diagnostic counterexample. It is not asserted to be a maille.',
 'The example tests the actual global germ definition and respects its additional geometric requirements.', 'not on the page')
A([87],'idea of the earlier run','156-2',[2,15],'1101–1104;1592–1595','espace topologique compact',
 'The cone vertex on Cantor space has compact link but an infinite Boolean algebra of clopen germs: the cylinder clopen partitions have unbounded finite size. Compactness alone does not imply finitely many rives.',
 'This example belongs to the earlier run, not the manuscript. It does not refute a separately imposed tame finiteness hypothesis.',
 'The claimed obstruction follows directly from the verified conic-link computation.', 'not on the page')
A([88],'idea of the earlier run','156-2',[15],'1592–1595','Comp(S_{A,X})',
 'Cone vertices with links S¹ and S² have the same rive ring F₂ because both links are connected, although their links have different homotopy types. The Boolean side algebra alone cannot reconstruct the full link.',
 'The earlier run’s example is bounded to this invariant and says nothing about equivalence of all enriched cuttings.',
 'The note correctly limits the negative conclusion to information actually forgotten.', 'not on the page')
A([90],'self-flagged step','156-2',[17],'1642–1643','régulièrement immergé; réciproq.',
 'The parenthesis asserts transfer of regular immersion from A⊂X to the full cut boundary and its two clopen parts. A doubtful marginal réciproq. may ask for a converse. A well-defined spectrum/cut model is needed before either direction becomes a precise theorem.',
 'No converse is manufactured from the abbreviation. The conic case is a test setting, not a resolution of the full unformalized assertion.',
 'The note keeps proof status and uncertain marginal scope separate.')
A([91],'unproved claim','156-2',[17],'1645–1666','Dec_β(A,X); A×β',
 'For a chosen birive, the proposed partial cut is the pushout which maps each of the two full spectral boundary pieces to a separate copy of A. Its map to X is asserted to be an isomorphism off A and to have the two marked copies Aρ,Aρ′ over A.',
 'The source’s pushout is retained literally. Its topology and embedding properties require a specified full-cut model; no universal maille conclusion follows from its set of fibers.',
 'The note accurately preserves the two whole copies and avoids collapsing the side labels.')
A([92],'unproved claim','156-2',[18],'1675–1677','ssi ... est une ficelle top.',
 'The author asserts that (A,β) is a one-node maille iff its partial cut with the two copies of A is a ficelle. This depends on regular-immersion and connectivity transfer between full and partial cuts. After admissibility, orientation is the choice of ρ∈β.',
 'The iff is a substantive equivalence, not merely a renaming of the earlier full-cut definition.',
 'The note correctly retains the unproved geometric transfer obligation.')
A([93],'self-flagged step','156-2',[18],'1678','se réduire au cas A₁,A₂ réduits à un point',
 'A marginal note suggests reducing nodes to points, but its opening and attachment are uncertain. Contraction preserves a node’s complement yet may change ambient connectedness and the connectedness of sides involving other contracted nodes; a blanket retroactive reduction is not warranted.',
 'The scope restriction is an editorial/mathematical caution, not a changed reading.',
 'The note correctly refuses to turn a doubtful marginal suggestion into a general reduction theorem.')
A([94,95],'unproved claim','156-2',[18,19],'1681–1712','définit à la fois β₁ et β₂; symétrique',
 'Two node-and-birive structures must have disjoint nodes, the second node must be a lieu after the first partial cut, and the resulting two sides must induce both given birives. The author asserts symmetry on exchange of the nodes; the text ends without proof. For disconnected nodes, the phrase “two connected components” requires qualification because earlier axioms ensure quotient connectedness.',
 'Simultaneous cutting is a possible proof method, not a construction supplied in these pages. The word comparables/compatibles stays uncertain.',
 'The definition and its immediately following symmetry assertion are consolidated with the exact unfinished endpoint.')
A([96,113],'idea of the earlier run','156-2',[15,16,17],'1582–1626;1645–1666','algèbre ... idempotente',
 'Every Boolean ring R is the filtered union of its finite Boolean subalgebras; n generators have at most 2^n atoms and at most 2^(2^n) elements. Spec R is a profinite space, the inverse limit of the finite discrete spectra of these subalgebras. For R=Riv(A,X), this reconstructs the global Stone spectrum only, not the relative boundary above A or X.',
 'The profinite consequence is the earlier run’s deduction from standard Boolean duality, independently checked here. It is not a manuscript theorem about forms.',
 '#113 repeats and limits #96’s same positive comparison. The atom bound, not a bound of 2^n on the algebra’s elements, is the correct count.', 'not on the page')
A([97],'idea of the earlier run','156-2',[11],'1463','une structure de ficelle réduite',
 'Every connected finite polyhedron with more than one point admits a reduced ficelle. Choose two leaf vertices of a spanning tree of a finite triangulation’s one-skeleton. Removing either leaves the tree on the other vertices connected, and every punctured simplex attaches to those vertices. Small closed vertex stars are compact-base cones; neither endpoint is isolated.',
 'This is the earlier run’s elementary proof, re-proved here. It establishes the manuscript’s sufficiency in the finite-polyhedron setting, not a convention-independent assertion for all infinite triangulations.',
 'The source announces the result without this proof; attribution and bounded scope are retained.', 'not on the page')
A([98],'idea of the earlier run','156-2',[11],'1463','Si X est un segment cette str. est unique',
 'A connected nontrivial finite polyhedron has a unique unordered reduced-ficelle endpoint pair iff it is homeomorphic to [0,1]. In dimension≥2 there are infinitely many conical noncut interior points of a maximal simplex. A graph with a cycle also has infinitely many noncut points; a finite tree has precisely its leaves as noncut points and exactly two leaves iff it is an arc.',
 'The proof is the earlier run’s, independently checked. It is about reduced structures on the fixed underlying space, not uniqueness of all disconnected-end decorations or equivalence modulo automorphisms.',
 'The note correctly isolates the true reduced uniqueness statement from the false unrestricted interval classification.', 'not on the page')
A([99],'reading question','156-1;156-2',{'156-1':[2,6,24],'156-2':[8,9,10,15,16,17,18,19]},'49–55;230–256;858–877;1359–1712','construction récurrente; n homeo. de raccordement',
 'The first two cotes do not define forms as a pro-object of finite posets/categories. Finite chains of geometrically labeled cuts are present, but the proposed indexing category, bonding maps and a reconstruction equivalence are absent from this package.',
 'This tests the earlier context’s title-based conjecture, not a conjecture stated by Grothendieck here. The later ateliers are considered separately.',
 'The note’s limited absence claim agrees with the full package; it must not be globalized to later cotes.')
A([101,102],'idea of the earlier run','156-2',[5,8,9,10],'1231–1278;1374–1452','mutuellement disjoints',
 'Compatible chains ordered by retaining literal embedded cuts and adding new ones need not be directed. In a square with opposite vertical ends, a vertical cut and a small tilted cut are each admissible collared lieux but intersect. Even disjoint sets can fail compatibility: on a circle with ends a,b, take two-point separators at arc-coordinates (1/3,2/3) and (2/3,1/3); each is a lieu, but the second straddles both sides of the first.',
 'Both are earlier-run counterexamples to a particular proposed refinement order, not to a refinement category allowing isotopy, replacements or subdivided intersections. All ficelle and cone hypotheses are checked in audit/root_proofs.md.',
 'The two examples test the same directedness overclaim while distinguishing crossing from merely incompatible disjoint cuts.', 'not on the page')
A([103],'idea of the earlier run','156-2',[9,10],'1421–1452','partie totalement ordonnée',
 'A pro-object proposal requires a specified cofiltered category, objects of the target category, and functorial bonding maps, together with a specified reconstruction functor and equivalence notion. The finite number of cuts in each object supplies none of these global requirements by itself.',
 'This is the earlier run’s formal research specification, not a construction found in the manuscript.',
 'The note accurately lists missing data and makes no positive pro-object theorem claim.', 'not on the page')
A([104],'idea of the earlier run','156-2',[2,10],'1092;1437–1452','espace topologique; ens ordonné',
 'A directed inverse limit in Top of finite T₀ spaces and continuous bonding maps is spectral. If that limit is Hausdorff, its compact open basis is clopen, so a nontrivial connected Hausdorff space cannot be such a raw limit. This does not exclude a quotient of the limit or a weak/homotopy comparison.',
 'This is a standard-theorem deduction of the earlier run. Finite T₀ spaces are sober; continuous maps between finite spaces are spectral because every subset is quasicompact.',
 'The conclusion has the precise restricted interpretation stated in the note; no general impossibility of finite models follows.', 'not on the page')
A([105],'unpursued implication','156-2',[10],'1437–1452','ens ordonné',
 'Finite T₀ spaces/posets can model the weak homotopy types of finite simplicial complexes via McCord’s finite-space/order-complex comparison. A finite non-discrete poset is not equivalent to a finite discrete set for this purpose.',
 'The literature comparison belongs to the earlier run, not Grothendieck’s page; a manuscript-specific finite model and comparison map still need construction.',
 'The note correctly separates weak homotopy reconstruction from homeomorphism.', 'not on the page')
A([106],'unpursued implication','156-2',[10],'1452','n lieux intermédiaires',
 'Clader’s inverse system from iterated barycentric face-posets has an inverse limit homotopy equivalent to a finite simplicial complex and a quotient homeomorphic to it. The 2016 erratum repairs the continuity proof. No identification with Grothendieck’s compatible ficelle-cut chains is supplied.',
 'This is an external comparison, with the correction included; both raw-limit and quotient conclusions must be distinguished.',
 'The note’s modern result is verified against the opened paper and erratum, not inferred from its title.', 'not on the page')
A([107],'idea of the earlier run','156-1;156-2',{'156-1':[24,25,26],'156-2':[8,9,10]},'858–1024;1359–1452','réduit; Équiv. de Catégories',
 'Finite-space simple equivalences correspond to simple homotopy types of finite simplicial complexes in Barmak–Minian’s comparison. Applying that theorem to ficelle cuts would require a specified finite model and proof that the proposed geometric moves induce the required collapses/expansions.',
 'The application is an earlier-run idea, not established by the cited comparison theorem or the manuscript’s gluing equivalence.',
 'The entry correctly states a research target with a missing comparison functor.', 'not on the page')
A([108],'unpursued implication','156-2',[2,3,8,9,10,12,13,14],'1092–1158;1359–1452;1489–1568','voisinage conique; bords des vois. tub.',
 'The fully faithful exit-path construction in conically smooth stratified homotopy theory retains mapping-space/link information. It supplies a comparison framework under its own geometric hypotheses, not a theorem that an ordinary finite incidence category determines any ficelle up to homeomorphism.',
 'The comparison is the earlier run’s. No conically smooth stratification or exit functor is constructed for all objects on these pages.',
 'The note accurately preserves the modern theorem’s enriched and hypothesis-dependent scope.', 'not on the page')
A([109],'unpursued implication','156-2',[8,9,10,15,16,17],'1359–1452;1580–1666','découpage; Équiv. de Catégories',
 'Esquisse §5 discusses reconstruction using a boundary-bearing piece, a closed stratum and an attaching map, expressed as a pushout. This is a concrete conceptual parallel to the retained end spaces and gluing maps of ficelle cuts.',
 'The parallel is an inference, not an exact theorem identifying the two constructions or defining an atelier in cotes1–2.',
 'The note’s limited geometric comparison is supported by the opened primary text.', 'not on the page')
A([110],'idea of the earlier run','156-2',[8,9,10],'1364–1452','homeo. de raccordement',
 'Replacing gluing homeomorphisms by isotopy classes is an additional quotient operation. Esquisse §5, printed pp29–30, distinguishes the induced map on isotopy classes from the stronger homotopy-equivalence statement about isomorphism spaces; a cutting theory must specify which coherence data survive that replacement.',
 'This is an earlier-run research question, not an established deficiency of a particular constructed enhanced category.',
 'The source comparison is real, while the application remains explicitly unconstructed. The earlier note’s §6 locator is corrected to §5, printed pp29–30, for the Isom_T to Isom_T′ map.', 'not on the page')
A([111],'idea of the earlier run','156-2',[8,9,10],'1364–1452','catégorie des ficelles; ens ordonné',
 'Finitely many cuts per object do not make the category of geometric cutting data finite. General finite categories also have endomorphism and automorphism data absent from posets; extending a poset comparison therefore requires a separate theorem.',
 'This logical distinction belongs to the earlier run. Some other-project endpoints invoked in its Context paragraph were recovered in neighbouring context selections; their exact scope and access limits are recorded separately in SA21_project_leads.tsv. None supplies the missing extension theorem.',
 'The note makes no unsupported extension theorem and is kept with its contextual leads segregated.', 'not on the page')
A([112],'idea of the earlier run','156-2',[10,12,13,14],'1452;1489–1568','n+1 ficelles orientées',
 'For Y=S¹ or S², the product ficelle Y×[0,1] with end fibers and chosen horizontal fiber cuts has the same abstract finite chain of cut indices for any selected times. The labeled pieces retain different homotopy types. Thus forgetting those labels loses information.',
 'This earlier-run example does not assert that the full posets of all lieux in the two products are isomorphic.',
 'The note’s bounded information-loss conclusion is correct and independently checked.', 'not on the page')
A([115,121],'other','none',[],'notes.md 937–941 and1190–1196','',
 'The old run describes a supplied planning README and RESULTS_STATE register, with mixed unreviewed and reviewed statuses and many absent underlying returns. Its original package48 context files and older records/*.md proof appendices are not among the present attachments and were not recovered. Two neighbouring context packages were subsequently retrieved and read: their selected register rows and reproduced passages verify some named endpoints, with the exact limits recorded in SA21_project_leads.tsv.',
 'This is provenance about the earlier run, not a fact on a Grothendieck page. Reported statuses cannot be promoted to verified mathematical results.',
 'The two entries describe the same context-provenance boundary. They are retained as documentary items. Selected textual endpoints have been checked independently; a register status is never treated as a checked proof.', 'not on the page')
A([116],'other','156-1;156-2',{'156-1':'2–27','156-2':'2–19'},'notes.md943–974; transcription49–1712','Je présume; J’ignore; Il faut voir; Faux',
 'The composite SF01–SF26 checklist distinguishes genuine open questions, abandoned assertions, intended revisions, explicit limitations, uncertain marginal abbreviations and final unproved assertions. Its substantive topics are indexed separately in the claim/problem tables rather than counted as 26 new independent claims.',
 'The old SF line references use separate page files. The current dossier uses 1-based physical lines of the single merged transcription and preserves cote/scan for cross-identification.',
 'Every SF row was compared with the corresponding read passage. Scope and statuses agree; line-number convention is corrected for this supplied file.')
A([117],'title, date or page count','156-1;156-2',{'156-1':'1–27','156-2':'1–19'},'1–1043;1045–1717','5 juin; 6 Juin; 7 juin; 26; 18',
 'The two Pro cotes contain 27 and19 scan markers including one institutional cover each, hence26 and18 manuscript sheets. Cote1 opens 5June1986 (year uncertain in ink); cote2’s ficelle section is6June and its boucle/rive section7June. Réseau is named7June in cote1. Cote1 has two divergent pagination strands; cote2 runs to18 with a cancelled doubtful7 before12. No written total page-count sentence occurs.',
 'Counts are derived from supplied scan markers, not attributed as manuscript wording. Later cotes have a separate actual-coverage ledger.',
 'The full T01–T11 record and both pagination tables agree with the transcription; uncertainty is preserved.')
A([118],'other','none',[],'notes.md1118–1134','',
 'The nine old register problems LM4 C.12; RESIDUE E.6,C.8,F.6,I.7,J.2,J.3; EXIT_ONE_TYPE P3c-general; PATHS C.10 concern other projects. The current cotes1–2 give no solution to those exact operator-group, relative-category, algebraic-completion, path, localizer or lax-comma problems.',
 'The two recovered neighbouring registers contain six full Open statement rows, a truncated LM4 C.12 row and the exact EXIT_ONE_TYPE P3c-general run-summary endpoint; RESIDUE E.6 is still absent. Those reported statuses do not establish the problems’ present mathematical status. The return proofs themselves were not independently verified in this endpoint audit.',
 'The entry’s deliberate negative scope comparison is retained. Each of its nine named targets is individually accounted for in SA21_project_leads.tsv, with source locators and access limits.', 'not on the page')
A([119],'title, date or page count','156-1;156-2',{'156-1':[2,24],'156-2':[2,15]},'44–53;858;1086–1090;1576–1578','Vers une géométrie des formes; Réalisations topologiques des réseaux',
 'The manuscript titles and June1986 dates identify the two archival cotes. Scan locators are preferable to the conflicting manuscript pagination; the old per-page transcription-line convention differs from the merged-file convention used here.',
 'The primary citation is to the supplied diplomatic transcription; scans themselves were not inspected in this run.',
 'The bibliographic titles match the title pages; the new line-locator convention is stated explicitly.')
A([120],'other','none',[],'notes.md1146–1188','',
 'The earlier run’s public bibliography comprises Ayala–Francis–Rozenblyum; Barmak–Minian; Clader and erratum; Gillam; Esquisse; McCord; Schapira; and four distinct Stacks references. Each is independently reopened in this consolidation, and the exact theorem/version used is recorded in SA21_references.bib and the search ledger.',
 'This is an audit of external references, not a manuscript claim. Verification of a URL is distinct from proof verification of its theorem.',
 'The bibliography is retained as one documentary entry, with checked results separately logged.', 'not on the page')
A([122],'other','156-1;156-2',{'156-1':[16,17,18,26,27],'156-2':[8,10,17,18,19]},'629–674;1017–1039;1364–1452;1642–1712','pas la vérification ici; symétrique',
 'The old run distinguishes its own examples and proposed repairs from manuscript assertions and leaves the orientation theorem, weak-F6 equal-endpoint argument, fully specified cutting equivalences and final symmetry as separate proof obligations. Literature comparisons do not alter doubtful ink.',
 'The referenced old proof appendices are not attached; examples used here are independently checked and receive new check events.',
 'This limits-of-comparison entry agrees with the cited open proof endpoints and is retained as an audit boundary.')

if __name__=='__main__':
    (W/'parts/root').mkdir(exist_ok=True,parents=True)
    (W/'parts/root/items_stage1_current.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    entries=[]
    corrections={110:'Correct the Esquisse locator for Isom_T to Isom_Tprime to section5, printedpp29–30 (not section6); the conceptual comparison remains valid.',116:'The SF checklist is accurate; convert its old per-page line convention to merged-transcription physical lines.',119:'Titles and dates agree; update the old per-page source-line convention to the current merged file.'}
    for item in items:
        for j,entry in enumerate(item['sources']):
            n=int(entry.rsplit('#',1)[1]); verdict='corrected' if n in corrections else ('kept' if j==0 else 'merged into '+item['id'])
            entries.append(dict(entry_id=entry,item_id=item['id'],verdict=verdict,reason=corrections.get(n,item['check_reason'])))
    entries.sort(key=lambda r:int(r['entry_id'].rsplit('#',1)[1]))
    assert len(entries)==122 and len({e['entry_id'] for e in entries})==122
    assert {int(e['entry_id'].rsplit('#',1)[1]) for e in entries}==set(range(1,123))
    (W/'SA21_items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (W/'SA21_entries.tsv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');wr.writeheader();wr.writerows(entries)
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (W/'progress.log').open('a') as f:f.write(now+'\tSTAGE1_REFRESH\tAll122 read verdicts serialized into '+str(len(items))+' manually consolidated items; source qualifications and endpoint audit incorporated.\n')
    output=f'{len(items)} manually authored items; {len(entries)} source entries covered exactly once; all required IDs present.'
    (W/'outputs/stage1_build.txt').write_text(output+'\n');print(output)
