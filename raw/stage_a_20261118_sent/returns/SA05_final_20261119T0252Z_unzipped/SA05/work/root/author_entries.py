#!/usr/bin/env python3
"""Explicit source-entry decisions, authored after passage review."""
import csv,json
from pathlib import Path
P=Path(__file__).resolve().parent
E='MPL_12_002-050'; M='MPL_12_051-098'
rows=[]
def e(pkg,n,item,verdict,reason): rows.append(dict(entry_id=f'{pkg}#{n}',item_id=f'SA05-{item}',verdict=verdict,reason=reason))
e(E,1,56,'corrected','The linear/nonlinear distinction is retained; Ayoub’s anabelian theorem is now published in2026 and uses a rich functor, not a bare profinite group. See SA05-56 and SA05-57.')
e(E,2,15,'corrected','Merged with the actual arithmetic-quotient passages. Exactness, geometric kernel, identity component and a rational/pointwise section are distinct; SA05-15 and SA05-16 retain the hypotheses.')
e(E,3,54,'kept','The letter dictionary is intentionally partial: cote16 is absent and this part supplies no new A–D definitions. Content-first comparison remains a valid constraint.')
e(E,4,1,'kept','Read all ten internal subnotes and scans2–4. Consolidated into SA05-1–8, including the cancelled level-invariance sentence, uncertain twist and conditional weak-Lefschetz/coniveau steps; no universal category construction is supplied.')
e(E,5,9,'corrected','Read N011–N031 and scans5–19. SA05-9–24 distinguish tensor reconstruction from its motive hypotheses, fibre torsors from period genericity, geometric from connected kernels, pointwise from group-scheme sections, and invariant from positive real forms.')
e(E,6,26,'corrected','Read N032–N048 and scans21–31. SA05-25–35 retain the exact finiteness/proper-or-excellent hypotheses, exact faithful versus full realization, missing purity shift and localization sign alarms, and the status of the cancelled coherent-realization proposal.')
e(E,7,36,'corrected','Read N049–N068 and scans31–41. SA05-36–44 distinguish weight, level and Tate-stable dimension filtrations; retain parity and Ext-index uncertainties; explicitly check the primitive-zero and small test-object computations.')
e(E,8,45,'corrected','Read N069–N089 and scans42–50. SA05-45–53 preserve E1 versus E2, cancelled versus surviving scissors claims, Ind-object existence, the nondominant-map retraction obstruction, curve and Enriques counterexamples and the author’s supersingular example.')
e(E,9,56,'corrected','Read N090–N101 and all cited current passages. SA05-1,20,23,54–60 incorporate bounded modern comparisons, unresolved scalar/nul reading, Oda’s exact hypotheses, and newly attached later pages; absent external contexts are not treated as verified endpoints.')

# Explicit decisions for the eleven introductory question notes.
e(M,1,60,'corrected','Source boundary updated: B12-01 includes the missing97–98 introduction and69 continuation; conflicting66/72 labels remain explicit. No original scans are available.')
e(M,2,1,'merged','Same conjectural motive-category construction as early N001/N090; cote16/CN/Hua endpoints named in the earlier note are not attached.')
e(M,3,20,'corrected','The central weight cocharacter is in the attached early pages; a Lefschetz sl2 Cartan is not central when its raising operator is nonzero. Envelope data do not embed the group; see also SA05-69.')
e(M,4,20,'merged','Duplicate central-weight versus Lefschetz-grading distinction; the early cote12 text now supplies the direct source.')
e(M,5,54,'merged','Same unresolved A–D dictionary as early#3; this page supplies no missing definitions.')
e(M,6,55,'kept','Retain only a thematic lead to absent cotes14/16; no explicit manuscript cross-reference at both endpoints is established.')
e(M,7,15,'corrected','The early fundamental-group pages are now attached, so the old outside-packet boundary is obsolete. Read the cancelled assertion and surviving conditional arithmetic sequence directly.')
e(M,8,15,'corrected','Kahn’s current version has Theorem5.10 and §10, replacing the note’s old numbering. Exactness requires the stated neutral fibre and descent hypotheses; it is not a period statement.')
e(M,9,57,'merged','No genericity/transcendence assertion occurs on the examined leaves; the formal torsor discussion is separate and is now matched to the attached early pages.')
e(M,10,57,'corrected','Huber’s period-torsor and genericity statements are checked at their current exact locators; existence of a tensor-isomorphism torsor does not establish the period conjecture.')
e(M,11,56,'merged','Same bounded Nori/Ayoub, motivated and six-operation comparisons as early N093; none constructs the whole postulated abelian category over arbitrary bases.')
e(M,12,56,'corrected','The distinct anabelian theorem has a2026 publication. Preserve its enriched functor target and the author’s separate unresolved derived-triviality assertion.')

# These hand-written tuples follow N001–N064 in the supplied index. Grouping and
# verdicts are mathematical/editorial decisions, not keyword classifiers.
decisions=[
 (61,'corrected','Two filtrations remain distinct; add the literal Hc²(P1) weight counterexample omitted from this note.'),
 (62,'merged','Coefficient-dependent bounds consolidated with N030/N031/N064; the lisse Legendre counterexample requires the stated unrestricted reading.'),
 (48,'merged','Same withdrawn birational-isomorphism question as early N074–N077; retain the cancellation on scan52.'),
 (51,'merged','Same failure of reconstruction from an unpolarized Jacobian/isogeny invariant as early N083/N084; explicit Howe example checked.'),
 (63,'kept','Tate is an explicit premise of the K0 realization argument, not an optional modern gloss.'),
 (36,'merged','Same closed-point arithmetic weight test as early N049–N051; retain the finite-type-over-Z model.'),
 (64,'kept','Separate direct Frobenius integrality from the conjectural effectivity converse and retain Frobenius convention.'),
 (65,'kept','Root-of-unity eigenvalues do not remove unipotent monodromy; the manuscript’s conditional semisimplicity input remains visible.'),
 (66,'kept','The author explicitly rejects the naive fundamental-group filtration; this is an open reformulation step.'),
 (67,'kept','The semisimple double-centralizer calculation is conditional on identifying the commutant with correspondence spans.'),
 (67,'merged','Same double-centralizer argument; preserve the limitation to Q_l-spans rather than individual cycles.'),
 (68,'kept','Finite-extension invariants match the analytic Lie algebra under the compact l-adic analytic representation hypotheses.'),
 (69,'kept','SL2/GL2 envelope example is an earlier-run elucidation, not an assertion of Grothendieck.'),
 (46,'merged','Cancelled coniveau draft joins early N071/N078/N079; no cancellation is removed.'),
 (70,'kept','The l-independent Lie-object proposal is conjectural and has an unresolved choice of Lie algebra target.'),
 (70,'merged','Finite-field analytic versus Zariski dimensions give an explicit warning against conflating the two targets.'),
 (58,'corrected','The note’s live scalar wording conflicts with the parallel Codex witness, which retains nul and deletes scalar wording. No choice is made; both enter Stage4.'),
 (71,'kept','Absolute cohomology is a list of desired properties, not a completed derived construction.'),
 (72,'kept','Cancelled reused base-change typescript retained as documentary evidence, without inventing a complete EGA theorem from two lines.'),
 (73,'kept','Degree-one Yoneda interpretation remains a hope on the page.'),
 (71,'merged','Finite-dimensionality and rational comparison belong to the same proposed absolute theory.'),
 (73,'merged','Higher effaceability doubt and proposed Ind-motive enlargement qualify the preceding extension hope.'),
 (71,'merged','Same H0 and comparison axioms; distinguish absolute cohomology from realization cohomology.'),
 (74,'kept','The cycle target and degree indices are kept rational, with the transcription alternatives listed separately.'),
 (74,'merged','The algebraic-closure vanishing and later odd-unit value conflict under the written restriction maps.'),
 (75,'corrected','Add the actually attached B12-01 scan69 continuation and its unfinished cup-product construction.'),
 (76,'kept','Hochschild–Serre even/odd pieces use Tate and semisimplicity separately.'),
 (76,'merged','Odd-degree noncanonicity and restriction-by-degree belong to the same calculation; the direct limit is checked.'),
 (77,'corrected','Parallel Pro/K12-05 and B12-01 witnesses disagree on72 versus66; preserve the likely freeness-label error without emendation.'),
 (62,'merged','The printed[-2,1] interval is a weaker consequence; it is not itself refuted by the sharper[-2,0] consequence.'),
 (62,'merged','Weight zero and Frobenius invariance remain different conditions.'),
 (78,'kept','The Tate-module weight sign conflicts with its defining twist and the scan76 calculation; retained as a reading alarm.'),
 (79,'kept','Kummer exposes an actual Sha-type finiteness condition, not a formal consequence of weights.'),
 (79,'merged','The weight-zero invariant warning is the same obstruction to removing the Sha term.'),
 (80,'kept','The omitted quotient in continuous lattice H1 is independently checked on the trivial lattice.'),
 (80,'corrected','Retain the visible bijective-to-finite-kernel revision and add the analogous finite-error issue in degree-zero sections.'),
 (81,'kept','The constant-Jacobian degree-two term is nonzero; keep the dual/twist required for the endomorphism tensor.'),
 (82,'kept','Brauer surjectivity is doubly questioned and its Picard/Leray/period-index hypotheses are not supplied.'),
 (83,'kept','Higher-degree finiteness needs base and finite-cotype assumptions; the margin gives no uniform proof.'),
 (79,'merged','The BSD comparison is the same rank-and-finiteness programme; it is not the full leading-term formula as stated.'),
 (81,'merged','Surviving scan82 vanishing contradicts surviving scan78 computation; no visible withdrawal is invented.'),
 (84,'kept','Prime-to-p finite-error qualification is already on the manuscript page and agrees with the local-duality scope.'),
 (85,'kept','Units, Picard and Brauer terms remain separate; Kummer requires l invertible.'),
 (86,'kept','Residue exact sequence gives corank r−1, including zero for one puncture.'),
 (87,'kept','SNC proper singular example is an earlier-run construction, independently recomputed; smoothness is not silently dropped from the positive theorem.'),
 (88,'kept','Parity and the assumed semisimple setting are retained in the positivity axioms.'),
 (88,'merged','Cone topology is interpreted only after real scalar extension, explicitly as reconstruction.'),
 (89,'kept','Opposite cross-term Tate twist is present in both witnesses and enters the scan-reading queue.'),
 (90,'kept','Orthogonal splitting is a conditional implication, not a construction of the category or proof of positivity.'),
 (91,'kept','The weight-zero counterexample has verified nontrivial Hodge types; effective level-zero is a different condition.'),
 (92,'kept','Cone axioms can supply simple twisted self-duality; division-algebra endomorphisms remain noncommutative in general.'),
 (93,'kept','Field-to-ring change alters the exact category; finite length and finite projectivity are not interchangeable.'),
 (94,'kept','The zero-eigenvalue kernel is established explicitly, with the automorphism/quotient repairs kept separate.'),
 (95,'kept','One-dimensional tests fix the reciprocal sign and exponent convention mathematically; ink remains undecided.'),
 (96,'kept','Characteristic-p ghost noninjectivity is checked with p copies of an invertible identity.'),
 (97,'kept','The invariant determines a virtual semisimplified class, not Jordan structure; no blanket Frobenius semisimplicity is assumed.'),
 (97,'merged','The sign(-1)^ρ is forced when the author reindexes cohomological degree by weight.'),
 (98,'kept','The birational cutoff retains the coefficient weight and the prescribed geometric hypotheses.'),
 (98,'merged','Components and Albanese up to isogeny are the limited top-degree content, not a reconstruction theorem.'),
 (99,'kept','The relative L-function hypothesis question survives; its exact adjective variants go to Stage4.'),
 (60,'corrected','The scan96 cover is followed by an attached B12-01 introduction97–98. Its1964 retrospective method date is not the typescript date.'),
 (71,'merged','Same absolute-theory comparison: the finite-field pattern alone does not identify an entire later cohomology theory.'),
 (59,'merged','Oda comparison is shared with early N098; its perfect-field and pointed-scheme hypotheses do not prove Sha finiteness.'),
 (62,'merged','Legendre family is the explicit coefficient counterexample; exact trace formula and duality are checked, not just numerical samples.')
]
assert len(decisions)==64
for n,(item,verdict,reason) in enumerate(decisions,13): e(M,n,item,verdict,reason)
e(M,77,100,'kept','Visible revisions checked individually against deletion/insertion markup; mathematical repair is not represented as a changed reading.')
e(M,78,100,'merged','Same editorial distinction between cancelled drafts and surviving contradictions, especially77/79 versus78/82.')
e(M,79,60,'corrected','Scope updated against all attached Pro/Codex leaves, including early and later parts and reused faces; absence of scans and external context remains explicit.')

with (P/'entries.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(rows)
assert len(rows)==88 and len({x['entry_id'] for x in rows})==88
print(json.dumps({'entries':len(rows),'verdicts':{v:sum(x['verdict']==v for x in rows) for v in sorted({x['verdict'] for x in rows})}}))
