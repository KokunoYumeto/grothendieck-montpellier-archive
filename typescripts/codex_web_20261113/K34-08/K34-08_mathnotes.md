# K34-08 — mathematical notes

Written after the transcription freeze at **2026-11-17T23:56:10+00:00**. These notes use only the supplied pages and the frozen transcription. They do not emend it. Quotations retain the writer’s abbreviations; ellipses in these notes merely shorten quotations and are not gaps in the transcription. Any interpretation resting on a doubtful, cancelled or overwritten reading is at most low confidence. Historical claims about what was then proved are reported as claims of these pages, not as statements about current mathematics.

## What the pages do

**Scan 133, §1.4 — passage to a strict localization.** The page presents a base-change diagram, expresses X′ and the relevant opens as limits, and writes stalks of the cycle objects as cohomology of a geometric generic fibre and then as direct limits. It specializes to U=X_eta and ends with an affineness observation. Some connecting strokes remain doubtful or lack arrowheads.

**Scans 134–136, §§2.1–2.3 — an affine Lefschetz bound.** The writer defines n_x from the components through x, states the initial vanishing bound, and seeks the improvement by dim closure{x}. After a cancelled finite-morphism approach, he chooses a transcendence basis, constructs a map to affine space over S, and passes to a strict localization S_1. The subsequent spectral-sequence argument is presented as completing the proof. Theorem 2.3 states the refined stalk bound, followed by a global sheaf-vanishing corollary. The parenthetical i/q and X_x/X_0 readings are kept separately.

**Scan 137, Corollary 2.5 — support and total degree.** The support of the vanishing-cycle sheaves is placed in the non-smooth locus Z of dimension d. The page combines the support bound p≤2d with the preceding dimension estimate to obtain a total-degree bound n+d+1, with a separate qualification for q=0. It then states vanishing of the cycle groups above that degree. Its coefficient definition has exponent nu, without a supplied plus-one.

**Scans 138–139, Corollary 2.6 and Remarque 2.7 — inertia and a projective argument.** The preceding conclusion is recast as a specialization isomorphism/epimorphism and trivial inertia action. A duality assertion gives the interval [n−d,n+d], especially degree n when d=0. The projective variant cuts by d+1 hyperplanes and uses a Gysin map and a comparison square. A cancelled explanatory paragraph is replaced by the diagram and marginal conclusion. The difference between codim d+1 and codim d is retained.

**Scan 139, Remarque 2.8 — a local cohomological-dimension question.** A strictly local scheme, a parameter t, and prime-to-residual-characteristic root covers are introduced. The writer asks whether the inverse-limit open U(infty) has cohomological dimension at most n−1. He explicitly contrasts this with the weaker n bound that the named standard conjecture would provide.

**Scans 140–141, §3.1 — a conditional lower-degree bound.** Rectified étale depth assumptions are imposed on the special and generic fibres. For projective flat X, hyperplane-section Lefschetz and a specialization square are used to claim an isomorphism below m−d−1 and injectivity at that degree, expressed as vanishing of Phi through m−d−1. The application is conditional on resolution assumptions. Only the opening formula of scan 141 remains live; the ensuing complete-intersection and inertia discussion is a cancelled draft.

**Scan 142, revised Remarque 3.2 — improvement and an example limiting it.** Part a) announces a later, conditional improvement for local complete intersections. Part b) says that pure dimension and the stated depth bounds alone do not give the extra degree. Its example identifies two distinct special-fibre points belonging to different components of a disjoint union of two projective lines. The explanation compares connectedness of the special and geometric generic fibres; the target cohomology degree in that sentence is a retained 0/1 reading doubt.

**Scan 143, §3.3 — transition to local statements and prerequisites.** The goal is local vanishing that implies the previous global results without projectivity. Local Lefschetz replaces global Lefschetz. The writer lists purity, resolution and local affine Lefschetz as required ingredients, then restricts the ensuing discussion according to their asserted availability.

**Scan 144, §4.1 — construction of the five schemes.** Starting from the punctured strict localization V, the page defines its special, generic and geometric generic fibres, the normalization S-bar as a limit, and V-bar by base change. It identifies the geometric generic open and the closed fibre, then invokes invariance of étale topoi under the specified residue-field extension. Cancelled formulas and two marginal sketches are retained, including the visibly rightward V_eta-to-V_bar_eta connector in the live sketch.

**Scan 145, diagram (4.2) and heading 3.5 — roles of the local schemes.** A two-row diagram records inclusions and vertical base-change maps. The text describes the topological or cohomological role of each of the five schemes. A small marginal formula identifies the higher cycle stalks with shifted cohomology of V_bar_eta and supplies the beginning of an exact sequence. The old section number 3.5 survives into the transcription.

**Scan 146, §§4.3–4.4 — inertia action and triangle (A).** The action of I on V-bar is introduced, with trivial action on the closed fibre and the indicated generic-fibre action. The writer specifies coefficients with exponent nu+1, describes an equivariant derived-category notation and its forgetful functor, and gives triangle (A) with a complex supported on the special fibre. The support complex is defined at the foot of the page; its interpretation continues on 147.

**Scan 147, triangle (A′) and comparisons — consequences of vanishing.** The support complex is related to the earlier cycle complex, and forgetting the action produces (A′). Under a stalk-vanishing hypothesis the page states a cohomological vanishing and comparison ranges. A long sideways note recasts these in local-cohomology terms. The m=+infty case leads to an asserted derived comparison isomorphism. The inequality, several marginal symbols and the intervening prose remain too uncertain to support a definitive reconstruction of every step.

**Scan 148, §4.5 — the second pair of triangles.** The opening paragraph interprets the preceding case as reducing the five-scheme picture to four. The closed-fibre inclusion produces a homomorphism and triangle (B), whose closed-fibre term is described with trivial action. Forgetting the action gives (B′). Both lower-left coefficient subscripts visibly end in unbarred V. An attempted continuation “Sous la condition (4.5.2)” is cancelled at the bottom.

## Statements left without proof

These are assertions for which these pages give a reference, a brief indication, or no separate argument; this is not a claim that they are unproved elsewhere.

- **135:** “on peut trouver une suite d’ ... t_1,...,t_r” whose images form the indicated transcendence basis; and “on peut donc supposer que les fibres ... sont de dim ≤ n−r”. The choices and shrinking are asserted.
- **136:** “S_{1 eta}=lambda est acyclique pour les nos premiers ≠ p (SGA 4 XV)”. The margin says “réf. inutile, on voit directement que ... est un pro-p-groupe”; that direct observation is not developed. The barred field in the marginal Galois expression is doubtful.
- **138:** “Procédant par dualité on trouve”, followed by Corollary 2.6. The duality argument itself is omitted.
- **138–139:** “Si ces derniers sont bien choisis, on peut supposer Y_0 lisse” and “le th. de Lefschetz affine SGA 4 XIV implique aisément ... de façon connue”. The hyperplane choice and the Gysin surjectivity/bijectivity are invoked without a full derivation.
- **140:** the global Lefschetz assertion is quoted “sous la forme SGA 1 XIV 4.6”, explicitly subject to resolution assumptions. The theorem is not proved here.
- **141, cancelled:** “Mais dans ce cas on peut améliorer la conclusion ...” appears in the crossed margin. The improvement is not proved in this draft; the first bound contains a reading doubt.
- **142:** “Nous verrons cependant plus bas ... au ... § 5” defers the sharper complete-intersection conclusion. In the example, “X satisfait les hypothèses avec m=n=1, d=0” is asserted without a detailed check of the depth hypotheses on this page.
- **144:** the projection “induit une équivalence des topos étales ... SGA4 VIII”. A residue-field reason is given, with the cited theorem supplying the topological conclusion.
- **146:** “On a alors un triangle exact” introduces (A). The page gives its terms and the support-complex definition, not a derivation of exactness.
- **147:** after (4.4.1), “alors” introduces (4.4.2); no separate justification of this step is written. The subsequent comparison is attributed to “la suite exacte associée à (A′)”. Interpretation of its first inequality is low confidence because its direction is marked doubtful.
- **148:** “qui s’insère dans un triangle exact” introduces (B); (B′) is then obtained by applying the forgetful functor. No proof of the first triangle’s exactness is included.

## Questions and conjectures

- **139, Remarque 2.8:** “Est-il vrai que la dim. cohomologique de U(∞), pour des coefficients premiers à ... p, est ≤ n−1 ?” The stated conjectural comparison would give “≤ n, et non n−1 !”. This is the explicit mathematical question in the batch.
- **140, 142–143:** the writer conditions the Lefschetz applications on resolution and the other listed ingredients. Scan 142 says “sous réserve de conjectures rappelées ... tout à l’heure 3.3)”; scan 143 says “nous supposons que nous disposons des ingrédients que nous venons d’expliciter”. These are prerequisites, not additional conjectures formulated in full here.
- **147, reading question only:** the frozen opening has `\underline\Phi_\nu^{q\unsure{?|2|\varepsilon}}`. If the tiny sign is a question mark, it records a notation doubt. The alternative readings prevent confidently listing it as an authorial conjecture. Confidence low.
- **146, cancelled and doubtful:** “Il semble que” survives only as an uncertain reading under cancellation in the opening revision. It is not treated as a live conjecture.

## Slips

No entry below changes the transcription. The corrected forms are suggestions based on these pages alone.

| Scan and location | Frozen wording or notation | Suggested correction | Confidence and reason |
|---|---|---|---|
| 134, §2.2 | “les deux formules (2.1.1) et (2.1.2) sont identiques” | Probably “(2.1.2) et (2.1.3)” | Medium. The stated n_x=dim_x X_0 makes the latter two displayed bounds agree; (2.1.1) is the unrefined bound. |
| 136, theorem 2.3 parenthesis | q in the assertion, then i in “à fortiori” | Probably q in that parenthesis | Medium. It appears to continue the same degree bound. The separate X_x/X_0 glyph cannot support more than a low-confidence correction. |
| 138, Remarque 2.7 | Y_0 of codim d+1, then Y of codim d | Probably codim d+1 for Y | Medium. The same paragraph chooses d+1 hyperplanes and writes the Gysin shift 2(d+1). |
| 140; 141 cancelled paragraph | “SGA 1 XIV 4.6”; “SGA 1 XIV 5.6” | Possibly SGA 2 XIV | Low. Scan 143 explicitly cites SGA 2 XIV in the related local discussion, but no external bibliography has been consulted, and the second occurrence is cancelled. |
| 141, cancelled conclusion | “la conclusion de 2.6, plus fort” | “plus forte”, if it modifies conclusion | Low. This is an agreement suggestion on cancelled text, not a repaired transcription. |
| 145, heading | “3.5.” | Possibly “4.2.” | Low. It stands in section 4 between 4.1 and 4.3; retained earlier numbering is another explanation. |
| 146, insertion | “(3.4)” | Possibly (4.1.2) or (4.1.3) | Low. The relevant normalization and base change are displayed on 144, but the writer could refer to material outside this batch. The insertion is itself partly doubtful. |
| 148, two support coefficients | `(\Lambda_\nu)_{V_{\bar\eta},V}` | Possibly `(\Lambda_\nu)_{V_{\bar\eta},\bar V}` | Medium. The surrounding cohomology and displayed open inclusion are on V-bar. Both written final V’s lack a bar. |

Two differences are deliberately **not classified as established slips**: the coefficient exponent nu on 137 versus nu+1 on 146, and the hat/bar/plain-eta ambiguity in the four-item list on 148. The former may be a change of indexing; the latter is a reading uncertainty. Likewise, the 0/1 exponent on 142 and the uncertain phrase on 147 do not justify a confident error claim.

## Pointers

No external text was opened. These are the writer’s pointers, including cancelled and questionable ones.

| Scans | His words / written reference | Role on these pages |
|---|---|---|
| 133 | “Plus généralement, dans 1.1.1.” | Internal affineness observation; number retained. |
| 134 | “dans (1.4.2)”; “SGA 4 XIV ---” | Initial affine bound. |
| 136 | “D’après 2.1.1.”; “(SGA 4 XV)”; “réf. inutile”; cancelled “SGA 4 IX” | Base-change bound, acyclicity and rejected global dimension argument. |
| 137 | “(III 1.)”; “SGA 4 X”; “en vertu de 2.3.”; doubtful “cf. 1” | Support, cohomological dimension and global cycle groups. |
| 138 | “2.5 (et de 2.6)”; “SGA 4 XIV”; “intervertir avec 2.8” | Projective alternative and editorial relocation note. |
| 139 | “SGA 4 XVI ---”; “La conjecture standard SGA 4 XIV” | Smooth proper comparison and local dimension question. |
| 140 | “Cf SGA 1 XIV ---”; “SGA 1 XIV 4.6”; “SGA 4 XVI ---” | Depth, global Lefschetz and specialization. |
| 141, cancelled | “SGA 1 XIV 5.6”; “compte tenu de 2.7”; “On comparera avec la conclusion de 2.6” | Rejected complete-intersection/inertia discussion. |
| 142 | “au ... § 5”; “tout à l’heure 3.3)”; cancelled doubtful “dans (2.2)” | Deferred strengthening and prerequisites. |
| 143 | “SGA 2 XIV 4.5”; “SGA 4 XIV, XVI, XIX” | Local Lefschetz and its ingredients. |
| 144 | “SGA4 VIII” | Equivalence of étale topoi. |
| 145 | “par (4.2.1)” | Marginal cycle-stalk sequence; written number retained. |
| 146 | inserted “(3.4)” | Local action/construction pointer, uncertain destination. |
| 147 | “introduit dans II 1”; “(4.1.2)”; “(4.4.5)” | Earlier cycle complex and local comparisons. |
| 148, cancelled | “Sous la condition (4.5.2)” | Abandoned continuation. |

## Remarks of the model

- **Model remark — high confidence:** the cancelled draft on 141 is followed by a live revised Remarque 3.2 on 142. Treating the cancelled statements as settled conclusions would erase an explicit feature of the manuscript’s development.
- **Model remark — high confidence:** the text’s progression is from an upper-degree bound obtained through affine Lefschetz, to a conditional lower-degree discussion, then to a local five-scheme construction and exact triangles. This organizational observation follows the visible headings and transitions; it adds no theorem.
- **Model remark — medium confidence:** triangles (A)/(A′) and (B)/(B′) are presented as two complementary comparisons of the same local picture, with and without I-action. The page explicitly applies a forgetful functor in each pair; the exact meaning of the questionable support subscript on 148 still requires care.
- **Model remark — low confidence:** the two coefficient definitions may use shifted index conventions. The visible difference is certain, but its explanation is not stated; it is not evidence for correcting either page.
- **Model remark — low confidence / reading question, 147 near (4.4.3):** the frozen first inequality is `i\unsure{\leq|\geq}m-1`. The adjoining bijectivity range and exact-sequence language favour leq, but the filled ink does not settle it. No change has been made after the freeze.
- **Model remark — low confidence / reading question, 147 final paragraph:** the frozen word is `\unsure{précision|prévision|positivité}`. None is secure enough to support an interpretation of the m=+infty example. This line should be rechecked before using the example mathematically.
- **Model remark — low confidence / reading question, 148 four-item list:** the frozen third subscript is `\unsure{\hat\eta|\bar\eta|\eta}`. The preceding construction suggests plain eta in that position, but the pointed mark is visible. The transcription has not been normalized to the expected list.

No proof, literature search or derivation beyond these short internal comparisons was undertaken for these notes.
