"""Serialize manually authored, passage-by-passage judgments; no inferred verdicts.

All ranges below are physical lines of the supplied Pro .tex, unless a Codex
filename is stated. The author read the complete Pro package and K93-10..12.
"""
from pathlib import Path
import csv,json,datetime
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parents[1]
SRC='SA03_texts/pro/MPL_93_002-046_transcription.tex'
items=[]; entries=[]; logs=[]
note_ranges={int(x['entry_id'].split('#')[1]):x for x in json.loads((OUT/'evidence/entry_ranges.json').read_text())}
def add(n,ns,kind,scans,lines,words,statement,reconstruction,check,reason,verdict='kept',per=None):
    ident=f'SA03-{n}'; sources=[f'MPL_93_002-046#{k}' for k in ns]
    items.append(dict(id=ident,sources=sources,kind=kind,cote=93,scans=scans,lines=[SRC+':'+lines],his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,k in enumerate(ns):
        v,r=(per or {}).get(k,(verdict if j==0 else 'merged into item',reason))
        entries.append(dict(entry_id=f'MPL_93_002-046#{k}',item_id=ident,verdict=v,reason=r))
        logs.append(dict(entry_id=f'MPL_93_002-046#{k}',notes_lines=f"{note_ranges[k]['note_line_start']}-{note_ranges[k]['note_line_end']}",transcription=SRC,lines=lines,scans=','.join(map(str,scans)),reading='Read entry and complete cited passage; compared overlapping Codex witness.',judgment=r))

add(601,[1],'title, date or page count',[3,27,28,29,30,32,34,37,38,46],'2-38;616-770;820-903;992-1246','COURBES ELLIPTIQUES : FORMULAIRE; Programme de la Théorie (Cristaux)',
'The Pro package contains 42 scan markers, including 19 formulary leaves, three Wanderley offprint pages, two English analysis fragments and nine programme leaves. The 235-page figure belongs to the catalogue. Context-register claims are earlier-run metadata, not manuscript mathematics.',
'Counts are our recount of the supplied transcription; attribution of every hand and the prior external register cannot be authenticated from these files. Codex supplies more of cote 93 than this Pro package.',
'agrees','Read the long introductory entry, its census and explicit-question tables against all 42 Pro scan markers. Its local scope is sound; its absent-context paths are leads, not evidence about those unseen sources.')
add(602,[2],'reading question',[3],'3-14','d’après J. Tate; mis au goût du jour par P. Deligne; G? = correction de Grothendieck',
'This is a reused Tate/Deligne formulary with a correction-marker rubric and a later bibliographical margin, not a wholly Grothendieck-authored treatise.',
'The 1968 IHES catalogue date and 1975 publication date date other witnesses, not these annotations.','agrees','The title, authorship and rubric are explicit. The note correctly refuses to authenticate every marginal mark.')
add(603,[3],'unproved claim',[3,5,6,7],'18-37;99-164','fibres géométriques … réduites irréductibles … genre arithmétique 1',
'For a proper flat finitely presented pointed family with geometrically reduced irreducible arithmetic-genus-one fibres and smooth section, geometric fibres are smooth elliptic, nodal rational or cuspidal rational; O(3e) embeds the family as a Weierstrass cubic locally on the base.',
'Modern hypotheses spell out the definition on scan 3. This is an assertion of the reused formulary, with the cubic argument on scans 6–7, not a new conjecture of Grothendieck.','agrees','The note correctly includes singular degenerations and distinguishes the initial assertion from later internal support.')
add(604,[4],'self-flagged step',[5,6],'99-128','réf; réf',
'Supply relative duality and cohomology/base-change references for a pointed genus-one family as in SA03-603: R¹p_*O(ne)=0 for n>0, p_*O(ne) has rank n and arbitrary base change, and the relative dualizing line is p*ω.',
'The two marks request references; they do not state counterexamples. Modern dualizing-complex indexing is kept separate in SA03-605.','agrees','Both reference marks are next to the duality/base-change paragraph; the note correctly identifies a deferred citation obligation.')
add(605,[5],'reading question',[5],'116-118','R^1p^! O_S',
'The displayed positive cohomological superscript needs collation with the convention for p!: with modern cohomological conventions p!O_S=ω_{E/S}[1] for a Gorenstein curve, hence its nonzero cohomology is in degree −1.',
'Modern shift convention, not a replacement of the diplomatic R¹.','agrees','Pro and Codex both retain a positive 1. Mathematics identifies an indexing issue but does not decide the ink.')
add(606,[6],'self-flagged step',[4],'60-75','Question : h=(du/u)^{⊗p−1} ? à l’∞',
'For the Tate generalized elliptic curve in characteristic p with canonical differential du/u, the Hasse section is (du/u)^(p−1), i.e. its q-expansion in that trivialization is 1.',
'The normalization and characteristic-p interpretation are made explicit; the sheet itself asks the question.','agrees','The question survives after the Hasse weight is changed to p−1. The note states a correctly normalized comparison, not a proof on the page.')
add(607,[7],'unpursued implication',[4],'79-88','Hasse : (−1)^n Σ binom(n,i)^2 λ^i',
'For odd p, n=(p−1)/2 and λ≠0,1, the coefficient of x^(p−1) in [x(x−1)(x−λ)]^n equals (−1)^n Σ_i binom(n,i)^2 λ^i. With the differential dx/(2y), this gives the Legendre Hasse scalar under the corresponding Cartier convention.',
'Coefficient extraction and smoothness exclusions are our explicit check; the printed scalar alone does not fix all Frobenius-semilinear conventions.','agrees','The polynomial and n occur on the page. The coefficient interpretation is correctly labelled as the earlier run’s deduction.')
add(608,[8],'reading question',[4],'90-93','λ = … 0 … 1728',
'The table combines residue classes p mod 12 with the exceptional values 0 and 1728 and an unresolved numerator. The natural comparison is a table of supersingular j-values, but the written λ and numerator remain unresolved.',
'Candidate j-table only; no repaired count is inserted into the transcription.','agrees','Both witnesses show the same suspicious label. A known supersingular formula cannot supply missing ink.')
add(609,[9],'idea of the earlier run',[4],'55-64;86-93','deg ω=1/24',
'If ω is the Hodge line on the compactified elliptic moduli stack and its characteristic-p Hasse section has simple supersingular zeros, its divisor yields Σ_[E]1/|Aut(E)|=(p−1)/24 for p≥5.',
'The stack convention, simple-zero premise and mass interpretation are the prior run’s reconstruction; the manuscript writes only the degree, weight and table.','agrees','The conditional reasoning is valid with the stated hypotheses. It is not a literal weighted-count assertion on the page.')
add(610,[10],'idea of the earlier run',[4,7,8,10],'42-45;166-215;259-263','c₄³−c₆²=1728Δ',
'The stated integral Weierstrass definitions satisfy c₄³−c₆²=1728Δ over Z[a₁,a₂,a₃,a₄,a₆]. Reduction to characteristic 2 or 3 must use Δ’s integral polynomial, not division by 1728.',
'Our exact symbolic check is supplied in code/check_computations.py; the warning about reduction is earlier-run commentary.','agrees','Scans 7–8 give the definitions and scan 10 explicitly asserts universality of the algebraic identity.')
add(611,[11],'reading question',[8],'195-203','−F(r,t)−sF_t(r,t)',
'The fourth transformed Weierstrass coefficient is algebraically −F_r(r,t)−sF_t(r,t), after u⁴ scaling. The transcript instead has F with no r derivative and a stray prime on (t+rs).',
'The derivative candidate follows by substituting x=u²x′+r, y=u³y′+su²x′+t; it is not an ink decision.','agrees','Direct expansion exposes the mismatch. Codex independently has the same missing derivative and marks the prime/dot uncertain.')
add(612,[12],'idea of the earlier run',[12],'318-337','la forme différentielle ne suffit plus jamais à rigidifier',
'In characteristic 2, for the ordinary smooth curve y²+xy=x³+a₂x²+a₆ with a₆ invertible, (x,y)↦(x,y+x) is a nonidentity pointed automorphism preserving dx/x.',
'This explicit example verifies failure of differential rigidification on the ordinary chart; it alone is not a proof of the word “jamais” for every curve.','agrees','The note correctly confines the example and does not generalize its proof beyond the stated chart.')
add(613,[13],'idea of the earlier run',[13],'349-378','Supposons qu’on ait même a₂=0; Supposons qu’on ait a₁=0',
'On nonreduced bases c₄=0 need not imply the stronger normal-form conditions a₂=0 in characteristic 3 or a₁=0 in characteristic 2: ε≠0 with ε²=0 gives counterexamples.',
'Dual-number examples are the earlier run’s check. The stronger hypotheses are explicitly present in the formulary.','agrees','The note preserves the distinction between nilpotence and vanishing rather than silently weakening the printed assumptions.')
add(614,[14],'reading question',[18],'477-481','j=12³ … j∼t²',
'Near j=1728 with 6 invertible the vanishing local coordinate is j−1728; j itself is a unit. A literal assertion j∼t² is false in that interpretation.',
'A translated-coordinate convention could explain the notation. No such convention is stated here, so j−1728 remains a collation candidate.','agrees','Both Pro and Codex omit the subtraction; the note identifies a real local-coordinate ambiguity.')
add(615,[15],'conjecture',[18],'469-489','Spec W(k)[j]^∧ ∼ M^∧/Aut(E)',
'For an elliptic curve E over a perfect field k, compare its formal deformation space over W(k), the action of its pointed automorphism group, and the completed coarse j-line. One must distinguish invariant-ring quotients from quotient stacks and account for the chosen residue field and completion.',
'The exact quotient category and completion are not defined on the page; the displayed isomorphism is a proposal, not a supplied proof.','agrees','The note accurately retains the question and does not treat wild characteristic as a tame invariant-theory calculation.')
add(616,[16,17,18],'idea of the earlier run',[8,13,18],'187-193;349-371;483-487','car 3 : 6 | v(j); car 2 : 12 | v(j)',
'For an equal-characteristic DVR with Δ a unit and j nonzero, v(j)=6v(b₂) in characteristic 3 and v(j)=12v(a₁) in characteristic 2. The families y²=x³+tx²−x over F₃[[t]] and y²+txy+y=x³ over F₂[[t]] attain 6 and 12. Over Z₃ and Z₂ the respective good-reduction examples y²=x³+x+1 and y²+2xy+y=x³ have v₃(j)=3 and v₂(j)=15.',
'The equal-characteristic qualification and all four examples are prior-run elaborations, rechecked here. The mixed-characteristic examples refute a stronger extension, not the margin as written.','agrees','All three entries concern the same divisibility and its exact boundary, and are merged. Integral invariant evaluation confirms every value; all discriminants are units in the asserted DVRs.')
add(619,[19,20],'self-flagged step',[18,19,20,22],'480-489;517-550;560-566','? semi direct de Z/3 par {±1 ±i ±j ±h|k}',
'Over an algebraically closed field the supersingular elliptic automorphism orders are 12 in characteristic 3 and 24 in characteristic 2. The char-2 full group is Q₈⋊C₃; the central [−1] acts trivially on the set of marked deformation classes, giving a plausible explanation for effective orders 6 and 12 in scan 18.',
'Identification of the sheet’s “group” with an effective deformation action is a reconstruction. Faithfulness of the remaining action is not proved by merely dividing the group order.','agrees','The note separates the question-marked quaternion interpretation from the prior run’s effective-stabilizer explanation. The two entries are one unresolved group-action question.')
add(621,[21],'withdrawn in the same text',[19,20],'502-505;524-530','[vrai seulement en faisceautisant !]',
'When c₄ and c₆ are units, the pointed automorphism sheaf is locally the constant two-element group; globally its sections may choose signs on each connected component. On a disjoint union of two nonempty such bases there are four sections.',
'The disconnected-base counterexample is our check of the handwritten correction, not a counterexample to the corrected sheaf statement.','agrees','The qualification is explicit beside Proposition 6.9(I); the ensuing proof’s global “pas plus de deux” must be read with that correction.')
add(622,[22],'unpursued implication',[15,16,17],'403-455','Isom … fini et non ramifié; revêtement étale de rang 2',
'For pointed genus-one curves without additive fibres, Isom is finite unramified. Equal j gives a surjective Isom scheme; away from j=0,1728 it is finite étale of degree 2. Its torsor may have no section over the original base; in characteristic 2 the equation is Artin–Schreier, not a μ₂-torsor.',
'Torsor language is a modern reformulation. Equality of j is not asserted to give a global isomorphism.','agrees','The note accurately reads the three parts of Proposition 6.3 and the different equations on scans 16–17.')
add(623,[23],'reading question',[12,17],'322;443-450','y²+xy=x³+a₂x+a₆',
'The model on scan 17 is referred back to (4.1), which has a₂x² on scan 12. The isomorphism equation on scan 17 also transforms the quadratic coefficient.',
'Missing exponent 2 is a mathematical candidate only.','agrees','Both independent witnesses retain the linear term on scan 17; the internal comparison gives a concrete collation target.')
add(624,[24],'reading question',[20,22],'532-562','(u′,s′,t′)∘(u,s,t)=(uu′,u′s+t′,u′³t+t′+u′²rs′)',
'The middle coordinate must depend on the two shear parameters s,s′, not on the translation t′. Composing T_(u,r,s,t)(x,y)=(u²x+r,u³y+su²x+t) explicitly determines the law once the order convention is fixed.',
'We record the full order-sensitive composition in the computation output; the typed tuple is left unchanged.','agrees','The prior note’s request is justified and is advanced here by an exact polynomial composition check.')
add(625,[25],'reading question',[21],'554-557','Cor : pour S|E plat sur Z … Γ(S,O_S)[…]',
'The sheet supplies a proposed hypothesis and an incomplete ring expression, but no completed conclusion. It cannot be registered as a theorem asserting an integral modular-form presentation over every such base.',
'No reconstruction of the missing conclusion is adopted.','agrees','The ellipsis is genuine transcript content; the note correctly prevents filling it from neighboring formulas.')
add(626,[26],'idea of the earlier run',[21,22,24,25],'555-614','Z/(2)[a₁,Δ]; Z/(3)[b₂,Δ]',
'The characteristic-2 modular-form ring has a weight-1 generator a₁ and the characteristic-3 ring a weight-2 generator b₂. Reduction of the integral ring generated in weights 4,6,12 cannot be onto those graded components.',
'This is a weight argument for failure of unrestricted base change, not an identification of the unfinished corollary on scan 21.','agrees','The note retains the correct separation between an established graded obstruction and a conjectural intended conclusion.')
add(627,[27],'unpursued implication',[23,24],'580-591','a₁ et ±b₂ sont les invariants de Hasse Witt',
'In characteristics 2 and 3 the Hasse–Witt scalar is respectively a₁ and a sign-normalized b₂ after fixing the invariant differential. Cartier on differential forms, Frobenius on H¹(O), and Cartier descent of connections are related but distinct constructions.',
'The sign and Frobenius twist require fixed conventions. The cross-project Cartier-descent comparison is a prior-run lead.','agrees','The page provides the small-prime assertion only; the note correctly avoids identifying all uses of the name Cartier.')
add(628,[28],'reading question',[14,16,17,19,20],'386-394;423;466;496;532;545','Δ est elliptique; (6.2); (3.6)',
'The subject “Δ” in a smoothness assertion should be checked against E; references to (6.1)–(6.4) in normal-form arguments appear to mean (5.1)–(5.4), and scan 16’s (3.6) points to Proposition 3.5.',
'These are internal-reference candidates, not silently repaired text.','agrees','The adjacent formulas expose the mismatches. Several are present in both witnesses and may be source typographical errors.')
add(629,[29],'other',[27,28,29,30,31,33],'616-818;841-874','Théorie axiomatique de l’orientation des variétés topologiques à bord',
'The Wanderley offprint and handwritten axioms form a local orientation-theory cluster within the folder, separate from the elliptic and crystalline texts.',
'Subject correspondence establishes a useful grouping, not the identity of every hand or a link to the arithmetic strands.','agrees','The printed title and handwritten sheaf/boundary data match the note’s local attribution and separation.')
add(630,[30],'idea of the earlier run',[28,29,31,33],'643-704;782-818;843-872','Exactitude; Séparation; Isomorphisme local; Anti-commutativité',
'Compare the offprint’s sheaf, separation, local boundary-isomorphism and opposition axioms with the handwritten six conditions. A point normalization plus boundary induction must supply the two-sheeted local system in each dimension.',
'Equivalence of the two axiom systems is a proposed proof task. It is not established by matching names.','agrees','The two systems distribute the boundary hypotheses differently; the earlier note is appropriately conditional.')
add(631,[31],'idea of the earlier run',[29,33],'687-695;856-862','anti-commutatif; deux rives différentes',
'In the oriented local model cut by x_m=0, outward-normal-first boundary conventions induce opposite orientations from the two halves.',
'This local sign verification is our check; it does not prove the global categorical equivalence of SA03-630.','agrees','The local computation supports exactly the opposition axiom and no more.')
add(632,[32],'reading question',[31],'813-818','rev. étale d’ordre 2 de X',
'For a locally flat codimension-one submanifold Y⊂X, the sheaf of local sides is based on Y. The following Hom sheaf is also on Y, whereas the parenthetical transcript says X.',
'Local flatness is the modern condition needed for a two-side local model; the base-letter alternative is Y, subject to ink review.','agrees','The note identifies a type mismatch. Neither witness provides a secure correction.')
add(633,[33],'unproved claim',[33],'864-872','une orientation … de tt X connexe … en un seul point',
'Two global sections of a sheaf with an open-and-closed equality locus over a connected space are equal if they agree at one point. This is uniqueness, not existence of a global orientation.',
'The elementary proof uses separation plus the sheaf’s étale-space description; nontrivial monodromy may still obstruct existence.','agrees','The statement is promised a posteriori on the page and is independently justified here.')
add(634,[34],'unproved claim',[28,29,30],'626-628;700-741','Si N≠4 … un (unique) isomorphisme',
'Wanderley asserts uniqueness of orientation theories on manifolds of dimensions ≤N when N≠4, using stability of orientation-preserving homeomorphisms of R^m for m≠4. The cutoff exception N=4 is not an exclusion of all higher-dimensional categories containing 4-manifolds.',
'Quinn’s later four-dimensional annulus input is distinct from checking Wanderley’s exact deduction. No new dimension-4 counterexample is asserted.','agrees','The quantifiers in the offprint match the note; the 1981 source cites its 1980 thesis for proofs.')
add(635,[35],'unproved claim',[30],'712-755','L.C.(V_m) → Π(m)-Ens … équivalence de catégories',
'For the category of m-manifolds and open embeddings, the offprint identifies separated sheaves with locally constant sheaves and with actions of the group completion of the embedding monoid; it also asserts the analogous Stokes-triple equivalence.',
'These are claims of Wanderley’s printed note. The thesis reference is a proof delegation, not a proof reproduced in the archive.','agrees','The note correctly retains the ambient category and group completion and avoids deducing the theorem from ordinary sheaf terminology alone.')
add(636,[36],'idea of the earlier run',[32,34],'820-839;875-902','T-fixed; sba(A,X)',
'The two English sheets concern an ergodic projection applied to finitely additive vector measures. Huff’s 1973 chapter is a bibliographical candidate, not a demonstrated textual attribution.',
'Attribution remains unconfirmed until a full-text collation matches notation and hypotheses; similar subject matter is insufficient.','agrees','Read both fragments in typescript order 34→32. Neither carries the title, author or opening theorem assumptions.')
add(637,[37],'unproved claim',[34,32],'877-902;822-833','Y=Y₁⊕Y₀',
'The fragment obtains a projection θ from a zero in the weak-operator closure of a semigroup, identifies its image as fixed vectors and kernel as vectors whose orbit closure contains 0, and then proves strong convergence using a directed absorption relation.',
'Without the missing semigroup lemma/order hypotheses this is not an unrestricted mean ergodic theorem. A conditional proof of the displayed estimate can still be checked.','agrees','The note accurately reports missing opening hypotheses; weak compactness by itself cannot justify the whole conclusion.')
add(638,[38],'reading question',[32],'822-830','||θ(y)=Σ α_i t_i(y)||<ε/(M+1)',
'The approximation in a norm-closed convex hull requires the norm of θ(y)−Σα_i t_i(y), not an equality inside the norm.',
'Minus sign is the candidate supported by the next displayed estimate, pending scan comparison.','agrees','Both Pro and Codex print equality; the immediately following calculation uses subtraction.')
add(639,[39],'unproved claim',[32],'835-839','This follows immediately from Proposition 1 below',
'The application claims a direct-sum decomposition of the indicated vector-measure space into countably additive and purely finitely additive parts, contingent on weak compactness and definitions stated on missing pages.',
'The supplied pair does not identify the range-space hypotheses. A scalar Yosida–Hewitt theorem cannot fill them.','agrees','The note correctly marks an incomplete application of an unidentified reused text.')
add(640,[40],'unpursued implication',[36],'904-989','G(z,f)=(−2f‴/f′+3(f″/f′)²)dz²',
'On a characteristic-zero coordinate chart with f′≠0, G=−2S(f)dz², where S(f)=f‴/f′−(3/2)(f″/f′)².',
'Schwarzian terminology and normalization are modern identification; the symbols c_f and the global domain remain underdetermined on this sheet.','agrees','The formula supports the exact factor −2; the note does not infer a global projective or arithmetic realization.')
add(641,[41],'withdrawn in the same text',[36],'909-958','c_exp f=c_f+deleted(3) df²',
'For f′≠0, G(z,exp(f))−G(z,f)=(df)². Two intermediate lines retain coefficient 3, but the final box cancels it; the exponential test gives coefficient 1.',
'We independently redo the derivative identity symbolically. Both retained draft and final corrected formulas are recorded.','agrees','The note’s same-page withdrawal is supported by explicit cancellation and the independent check.')
add(642,[42],'idea of the earlier run',[36],'964-989','invariant … π; γ.G(z,f)',
'If the domain coordinate change γ is Möbius and f∘γ=ρ(γ)∘f with ρ(γ) Möbius, the Schwarzian chain rule gives γ*G=G. Arbitrary domain coordinate changes introduce an additional Schwarzian term.',
'These equivariance hypotheses are the prior run’s reconstruction; the marginal words do not state them fully.','agrees','The conditional calculation is sound, while the source’s intended global action remains a reading problem.')
add(643,[43],'idea of the earlier run',[36],'929-965','−2f‴/f′+3(f″/f′)²',
'If f=y₁/y₂ for independent solutions of y″+q y=0, then S(f)=2q and G=−4q dz². A Picard–Fuchs identification additionally requires an actual geometric family and comparison with its periods.',
'The ODE construction is modern commentary; no such family is specified on scan 36. Other supplied Codex sheets explicitly discuss Picard–Fuchs equations, so the local nonidentification must not be extended to the whole cote.','agrees','The note is correct within its Pro-package scope; the broader dossier adds Codex-only evidence separately.')
add(644,[44],'idea of the earlier run',[36],'951-958','G(z,e^z)=dz²',
'The associated algebraic equation y″−y/4=0 over Z[1/2] has matrix A=((0,1),(1/4,0)); over F_p(z), p odd, ∇_D=D−A has p-curvature −A, since D^[p]=0 and A^p=A. It is nonzero and not nilpotent, including after projectivization.',
'This counterexample refutes only the inference “Schwarzian identity implies nilpotent p-curvature”; it does not refute any Gauss–Manin theorem or reduce the transcendental exponential modulo p.','agrees','The earlier run’s matrix calculation is rerun exactly; its scope is correctly restricted.')
add(645,[45],'idea of the earlier run',[23,36,38,46],'581;904-989;997-1245','Hasse Witt; G(z,f); cristal',
'Cartier descent for integrable connections requires zero p-curvature; geometric Gauss–Manin connections satisfy a nilpotence theorem under geometric hypotheses. A scalar Hasse invariant and either connection statement are different objects.',
'This is an external mathematical comparison, not a theorem jointly stated across these leaves.','agrees','The note’s distinction is essential; the more explicit later Cartier and p-curvature sheets are treated separately.')
add(646,[46],'idea of the earlier run',[4,18,36,44,45,46],'39-95;469-489;904-989;1165-1245','Question connexe; Théorie de déformations',
'A proposed bridge is to compare the associated-graded p-curvature of an actual Gauss–Manin connection with Frobenius-twisted Kodaira–Spencer, under Katz’s properness, local-freeness and degeneration hypotheses.',
'Application to scan 36 remains a research direction: no family identifying that equation is supplied in this package.','agrees','The prior note is a qualified external comparison, not a claim that the broad S20 programme was proved.')
add(647,[47],'idea of the earlier run',[4,44,45,46],'68-75;1165-1245','Q; R; extension vectorielle universelle',
'The q-expansions admit a Gauss–Manin/Serre-derivative comparison, and universal vector extensions admit a precise characteristic-zero Gauss–Manin description. These are distinct concrete routes between parts of the folder.',
'The two uses of exponential are not identified without further maps. The routes belong to the earlier run’s proposed investigations.','agrees','The manuscript anchors both ends; the note appropriately leaves the intended cross-cluster identification open.')
add(648,[48],'idea of the earlier run',[4,18,23,36,38,46],'39-95;469-489;581;904-1245','Formules utiles; Question connexe; G(z,f)',
'Comparisons with cotes 64 and 159 would require their actual deformation and projective-connection passages. They are not in this attachment, so cross-project assertions cannot be verified at both ends here.',
'S20 and register links are prior-run context leads, not archival cross-references. The larger supplied cote-93 continuation changes the package’s local coverage but supplies neither missing cote.','agrees','The note explicitly limits its conclusion to 42 Pro scans; the dossier preserves that evidentiary boundary.')
add(649,[49],'reading question',[37,38,39,40,41,42,43,44,45,46],'992-1246','Programme de la Théorie (Cristaux)',
'The sequence of numbered problems, deformation theorem and universal-extension construction corresponds to Chapter V of the Montreal Barsotti–Tate programme, from the 1970 course and published in 1974.',
'This identifies a textual parallel, not the date of these sheets or their annotations.','agrees','Distinctive headings and statements agree; documentary dates are attached to the published/course witnesses only.')
add(650,[50],'unproved claim',[38],'1008-1019','Crisloclib(S) ≃ Crisloclib(S₀)',
'For p locally nilpotent on S and S₀=V(p), the programme invokes invariance of locally free crystals on its absolute crystalline site and uses it to make D*(G) depend only on G₀.',
'The absolute site and divided-power conventions are essential. No claim of invariance of every relative or filtered crystalline theory is made.','agrees','The blank reference “cf. … plus haut” is real; the note correctly records an invoked prerequisite.')
add(651,[51],'reading question',[38],'1023-1035','V_MF_M=p id_M',
'Given F:M^(p)→M and V:M→M^(p), well-typed identities are VF=p id_(M^(p)) and FV=p id_M. The transcript has the object subscripts reversed.',
'This is type checking only; arrows or subscripts must be collated with the ink.','agrees','Both witnesses show the mismatch. The subsequent functor also omits the opposite-category mark present at its first occurrence.')
add(652,[52],'idea of the earlier run',[38,39],'1038-1043','permet de retrouver les fibres',
'Perfect-field Dieudonné classification recovers geometric fibres of a family; it does not by itself prove full faithfulness or descent of the family over an arbitrary characteristic-p base.',
'The logical separation is our check. The text itself immediately asks the stronger question.','agrees','The note reads the transition from “sentiment” to Problem 1 faithfully.')
add(653,[53,55],'self-flagged step',[39],'1041-1043','Le foncteur … est-il pleinement fidèle ?',
'Problem 1 asks full faithfulness of the crystalline Dieudonné functor for p-divisible groups over arbitrary characteristic-p bases. The unrestricted statement must be separated from positive results for locally p-based, locally complete-intersection or quasisyntomic bases and from enriched divided/prismatic targets.',
'The base-sensitive modern comparison is the earlier run’s addition, updated here through November 2026.','agrees','The two entries concern the same full-faithfulness question. The page is open, while later general-base counterexamples and qualified theorems prevent a single unqualified modern verdict.')
add(654,[54],'conjecture',[39,43,44],'1043;1113-1155','Son image essentielle … F-V-cristaux “admissibles”',
'The second part of Problem 1 asks whether the image is precisely the crystals admitting the canonical locally split filtration defined via φ*Fil¹=ker F. This is an existence/classification question beyond morphism recovery.',
'Modern admissible prismatic crystals or divided crystals are not silently identified with the manuscript’s old target.','agrees','The essential-image half is explicit and logically distinct from full faithfulness.')
add(656,[56],'conjecture',[39],'1045-1050','structures supplémentaires … filtration … catégorie dérivée',
'Seek extra data on finite-flat p-group crystals, plausibly a filtration on a suitable derived object, yielding a classification. The text has not defined this category or its morphisms.',
'A modern filtered derived/F-gauge comparison is evaluated in the claims and problems, rather than retroactively put into the manuscript.','agrees','The circled phrase and explicit admission of not having isolated the structure support the note’s programme status.')
add(657,[57],'self-flagged step',[39,41],'1050;1069','sans doute inutile si S₀ est parfait',
'Two marginal perfect-base qualifications concern, respectively, extra finite-group structures and the filtration formula. They are tentative and their targets must remain separate.',
'Codex reads “Sans doute inutile” on scan 41 where Pro has uncertain “formule inutile”; this is an additional witness disagreement, not a changed reading.','agrees','The note correctly separates the two locations, but its exact scan-41 wording is less secure than the mathematical claim.')
add(658,[58],'conjecture',[40],'1053-1057','plats sur Λ_n=Z/p^n Z; anti-équivalence',
'Over a perfect characteristic-p base, seek an anti-equivalence for finite locally free commutative p-groups flat as Λ_n-module sheaves and finite locally free W_n(O_S)-modules with the appropriate semilinear F,V relations, and derive the p-divisible-group classification by compatible truncations.',
'The phrase Λ_n-flat is retained; it is not replaced by the weaker condition p^nG=0, and the transition/limit argument is an additional obligation.','agrees','The inserted anti- and the flatness condition are present in both witnesses.')
add(659,[59],'reading question',[40],'1053-1055','car.p 0.',
'The positive-characteristic condition has a missing or unread comparison sign. The surrounding p-group and Witt-vector setting supports p>0, not characteristic zero.',
'p>0 is a candidate supported by a parallel edition and context, not a transcription change.','agrees','Both independent transcriptions leave the missing relation unresolved.')
add(660,[60],'reading question',[41],'1060-1067','t_(G*) … t_G=ω_(G*)^∨',
'The exact sequence and the prose use conflicting stars in the tangent notation. With t_H=Lie(H), the standard contravariant sequence is 0→ω_G→D*(G)_S→Lie(G*)→0.',
'Modern convention is supplied explicitly; the source may use a shifted naming convention or contain a slip.','agrees','The note correctly refuses to decide the star from familiarity alone.')
add(661,[61],'idea of the earlier run',[38,41,42],'1019;1060-1098','prolonge le sous-module Fil¹',
'An unfiltered crystal can remain fixed under a divided-power thickening while the Hodge subbundle varies; therefore nil-invariance of crystals is compatible with nontrivial group deformations.',
'This is a structural explanation, conditional on the cited deformation theorem.','agrees','The two source statements concern different amounts of structure and do not contradict each other.')
add(662,[62,63],'withdrawn in the same text',[41,42],'1060-1098','On prouvera; si S′ est à p. div. nil',
'For S with p locally nilpotent and a divided-power thickening S⊂S′, the announced functor sends a lift G′ to G and a locally direct-summand lift of ω_G in D*(G)_(S′). The final insertion requires nilpotent divided powers, or the stated infinitesimal/dual-infinitesimal alternative.',
'This is the corrected theorem as announced, not a proof on these pages. Ordinary nilpotence of the ideal is not interchangeable with PD nilpotence.','agrees','The two notes describe one theorem and its same-page narrowing; the full extra alternative must be checked in literature rather than erased.')
add(664,[64],'self-flagged step',[43],'1107-1111','Trouver variante … (j’ai un candidat)',
'Problem 3 asks for a deformation theorem for finite locally free commutative p-groups. The candidate is not given, and a single vector-bundle Hodge filtration is not stipulated as sufficient.',
'Modern finite-group derived classification is a later comparison, not the missing candidate.','agrees','The inserted problem and marginal finite-flat qualification are explicit.')
add(665,[65],'unproved claim',[43],'1121-1130','pour tout cristal de Dieud. M … suite … exacte',
'For every Dieudonné crystal, the programme claims that its reduction on characteristic-p PD thickenings has alternating F,V complex exact termwise and kernels/images locally free subcrystals.',
'Exactness, local freeness, and crystalline compatibility are three distinct obligations. “Every crystal” cannot be narrowed to those already coming from groups without changing the claim.','agrees','The inserted universal quantifier and announced “on prouvera mieux” are preserved.')
add(666,[66],'idea of the earlier run',[43],'1121-1130','FV=p, VF=p',
'If p is injective on modules P,Q and F:Q→P, V:P→Q satisfy FV=VF=p, cancellation gives exactness of the alternating reductions modulo p. Merely imposing F=V=0 in characteristic p shows why the relation FV=VF=0 alone is insufficient.',
'The zero-map example is a countermodel to stripped-down linear data, not a counterexample to the absolute-crystal claim.','agrees','The note correctly labels the added p-torsion-free lift hypothesis and limits its countermodel.')
add(667,[67],'idea of the earlier run',[43],'1127-1130','sous-cristaux en modules loc. libres',
'Over R=Z_p[x,y]/(xy−p), multiplication F=x,V=y satisfies FV=VF=p and R is p-torsion-free. Mod p, the complex is exact, but im(V)=(y) over F_p[x,y]/(xy) is not locally free or a direct summand at (x,y).',
'The example has no asserted crystal/Frobenius-descent structure; it refutes a linear-algebra shortcut, not the full crystalline theorem.','agrees','The annihilator (x) is nonzero, while (y) is nonzero at the node, establishing the claimed failure.')
add(668,[68,83],'unproved claim',[43,44],'1113-1155','la filtration est uniquement déterminée; φ a des propriétés de fidélité',
'The programme answers its own concern about forgetting a filtration by asserting that φ*Fil¹=ker F determines the locally split Hodge filtration uniquely; admissibility asks that such a subbundle exist.',
'The concern is withdrawn by an asserted descent result, not by a proof of full faithfulness or essential surjectivity. The actual crystalline φ must be retained.','agrees','C20 and C35 concern the same canonical-filtration argument. The objection and answer are both recorded; the proof remains deferred.',per={83:('merged into item','Merged with the canonical-filtration claim; its hypothetical objection is answered immediately on scans 43–44, not a negative solution of Problem 1.')})
add(669,[69],'idea of the earlier run',[44],'1143-1155','détermine sans ambiguité … Fil¹',
'Over k[ε]/(ε²), the distinct direct-summand lines (1,0) and (1,ε) become equal after ordinary Frobenius pullback. Thus ordinary Frobenius pullback is not faithful on subbundles over arbitrary nonreduced bases.',
'The example is outside the asserted crystalline-descent theorem and only rules out replacing its φ by ordinary Frobenius.','agrees','The note’s boundary is correct and its elementary countermodel is rechecked.')
add(670,[70],'unpursued implication',[44],'1157','Passage à la limite … séparés et complets … p-adique',
'Extend the theory to p-adically separated complete rings by compatible finite-level groups, crystals, filtrations and morphisms, with an effectivity/limit comparison.',
'The heading supplies a programme, not the limit theorem or its exact category.','agrees','The note correctly does not equate completeness with a proof of effectivity.')
add(671,[71],'idea of the earlier run',[44],'1162','isogénies … th. de Tate',
'The intended isogeny/Tate comparison needs a specified base and realization. Over an algebraically closed field of characteristic p, μ_(p∞) is nonzero but has zero geometric-point p-adic Tate module.',
'The counterexample concerns that specific realization only; later Codex scans 49–54 supply more explicit Tate questions and are linked separately.','agrees','The note’s warning is valid but does not identify the unspecified heading with a false theorem.')
add(672,[72],'idea of the earlier run',[41,44,46],'1064-1067;1163;1225-1243','Dualité',
'Compare Cartier duality, the crystal pairing, exchange of F and V, Tate twist and Hodge orthogonality, tracking G/G* and A/A* conventions.',
'This is an investigation proposed by the earlier run from a programme heading; it is not a compatibility theorem proved there.','agrees','The source contains the heading and the relevant starred formulas, but no proof of all compatibilities.')
add(673,[73],'unproved claim',[44,45,46],'1165-1189;1241-1243','R¹ f_(A cris)* O_(A cris); H¹_DR(A/S)',
'For an abelian scheme A/S, the absolute nilpotent-crystalline H¹ gives a locally free crystal whose evaluation on S is relative de Rham H¹, and whose evaluation on a permitted thickening is computed from a lift A′.',
'The nilpotent absolute site, variance, local freeness and compatible base change are retained. This is not an assertion about arbitrary cohomology on any site.','agrees','The note accurately separates the announced comparison from the proof obligations.')
add(674,[74],'unproved claim',[45],'1189-1191','il existe toujours un A′ pour S affine',
'An abelian scheme over an affine base admits a lift across the specified locally nilpotent PD thickening; no polarization is fixed. The text invokes Mumford without a precise locator.',
'The modern proof may follow from lifting locally split Hodge subbundles plus the deformation theorem; that does not identify the exact Mumford passage.','agrees','The note correctly keeps existence, polarization and canonical comparison distinct.')
add(675,[75],'reading question',[45],'1193-1202','R¹ f_*(O_S)',
'The degree-zero sheaf in the relative de Rham complex on A is O_A, so the Hodge exact sequence should end in R¹f_*O_A under modern conventions.',
'O_S could signal an implicit pullback convention or a source typo; the transcript remains unchanged.','agrees','Both witnesses retain O_S. The problem is not resolved by the repeated typo in a parallel edition.')
add(676,[76],'unproved claim',[45,46],'1208-1245','est une équivalence de catégories',
'Across a locally nilpotent divided-power thickening S⊂S′, the announced category of lifts of an abelian scheme A is equivalent to locally direct-summand lifts of its Hodge submodule in the evaluated crystal.',
'The Pro pages announce the inverse via universal extensions; Codex scan 47 continues it but still defers the exponential argument.','agrees','The note is correct about proof status in its package, and the present dossier adds the supplied continuation rather than treating it as absent.')
add(677,[77],'idea of the earlier run',[18,45],'469-481;1208-1218','paramètre régulier relatif; Fil¹',
'For fixed locally free ambient lift H and rank-g subbundle F in rank-2g H, lifts across a square-zero ideal I form locally a torsor under Hom(F,H/F)⊗I. Its rank is g², hence one in dimension one.',
'This checks tangent dimensions only; it proves neither a formal quotient by automorphisms nor global effectivity.','agrees','The prior run states the conditional linear algebra with correct restrictions.')
add(678,[78],'self-flagged step',[46],'1227-1239','à charge de définir … un système transitif d’isomorphismes canoniques',
'To make E(A′) on thickenings into a crystal, construct canonical transition isomorphisms for different abelian lifts, natural under base change and satisfying the cocycle condition.',
'Isomorphism classes alone do not define a crystal. The subsequent exponential construction is a promised method, not performed here.','agrees','The exact construction obligation is explicitly written and correctly identified by the note.')
add(679,[79],'unproved claim',[46],'1239','à isomorphisme unique près … ma vieille lettre à Tate',
'For the universal vector extension E(A) over a Q-scheme, the programme asserts unique smooth-group lifting, with identified reduction, over nilpotent and then general nil thickenings.',
'“Characteristic zero” is interpreted as all integers invertible for this modern comparison. The assertion is specific to E(A), not arbitrary smooth groups.','agrees','The note correctly isolates the strong rigidity and limit claims and the imprecise letter reference.')
add(680,[80],'idea of the earlier run',[46],'1239','un seul schéma en groupes lisses E′',
'A proposed first-order proof uses Rg_*O_(E(A))≃O_S over an affine Q-base and translation-invariant tangent bundle to kill deformation/obstruction groups; fixing the identity removes translation automorphisms.',
'Promoting pointed-scheme deformation theory to smooth-group rigidity, then to general nil thickenings, still requires compatibility and limit arguments.','agrees','The note is a qualified proof route, not an already completed proof.')
add(681,[81],'unpursued implication',[46],'1241-1243','E̲(A*)=R¹ f_(A cris)* G_m',
'The programme relates the crystal of the universal extension of A* to multiplicative cohomology on the absolute nilpotent crystalline site. Comparison with line bundles with integrable connection must track the Picard component and rigidification.',
'It must not be replaced by the ordinary full Picard sheaf R¹f_*G_m on S without checking components.','agrees','The dual abelian scheme and crystalline site are explicit and preserved by the note.')
add(682,[82],'reading question',[46,47],'1245; SA03_texts/codex/K93-07_transcription.tex:2-33','Quoi qu’il en soit … on',
'The Pro file stops mid-sentence, but this attachment includes its continuation in Codex scan 47: D*(A)=Lie E̲(A*) and a quotient description of the inverse deformation construction.',
'The Codex continuation is independent supplied evidence, not an interpolation from the published book. Its exponential step is still deferred.','understates','The note’s statement was true of its local Pro package; in this consolidated attachment the next page is available and must be used.','corrected')

assert sorted(int(e['entry_id'].split('#')[1]) for e in entries)==list(range(1,84))
(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
for name,rows,fields in [('entries.tsv',entries,['entry_id','item_id','verdict','reason']),('reading_log.tsv',logs,['entry_id','notes_lines','transcription','lines','scans','reading','judgment'])]:
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'outputs/items_build.txt').write_text(f'{now}\nManually authored items: {len(items)}\nEntries with individual read verdicts: {len(entries)} / 83\nNo keyword-derived verdicts.\n')
print((OUT/'outputs/items_build.txt').read_text())
