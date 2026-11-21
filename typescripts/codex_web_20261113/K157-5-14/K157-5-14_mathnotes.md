# K157-5-14 — mathematical notes

These light notes cover scans **213–228**, manuscript pages **129–144**. The sixteen page files and assembled fragment were frozen at **2026-11-20 02:59:23 UTC**. The supplied `RESULTS_STATE.md` was then read in full, followed by the completed K157-5-13 and supplied K157-4-04 mathematical notes. Reporting the author's argument does not certify it. No reading below changes the frozen transcription.

## What the pages do

**U01 — Completing the presentation comparisons (213–216).** The proof begun in **K157-5-13 U06** continues by replacing a bounded diagram with its finite subdiagrams. A strict epimorphic family is described through pairwise fibre products; auxiliary arrows from the generating subcategory give another bounded presentation. The proof then treats coproducts and compares the conditions on the primed filtration. The source's bare limits, capped strokes and cancelled alternative descriptions remain visible.

**U02 — A generating-subcategory criterion (217).** Lemma 4.5.14 relates strict generation and closure under bounded colimits, presentations by sufficiently large filtered indexing categories, ordered presentations, and inclusion of the accessible-object subcategory. It displays the chain a implies b, b equivalent to b-prime, b-prime implies c, with an additional equivalence assertion under further hypotheses. Decorated M-zero in the opening and undecorated M-zero later are retained as written.

**U03 — The base-change case and covering families (218–221).** The author returns to cases A–C of 4.5.13, recalls SGA 4, and tentatively compares two exactness/universality conditions. A group example is accompanied by a slanted correction. Corollary 4.5.15 describes the primed filtration using bounded strict universal epimorphic families when filtered colimits commute with base change. Corollary 4.5.16 uses composition of such families to give a closure assertion.

**U04 — Describing M-pi by closure (221–222).** The transition says that M-pi itself has not yet been characterized as concretely as the two Filt classes. Proposition 4.5.17 identifies it with the smallest strictly full subcategory containing C and closed under colimits of the prescribed cardinality. The bracketed qualification distinguishes this closure from two narrower presentation descriptions. The converse argument invokes Lemma 4.5.14, a implies c.

**U05 — Returning to the proto-topos characterization (223–225).** Section 4.6 explicitly revisits the incomplete earlier proof of 4.3.6. The proposed route is PTA implies d implies c implies PTA. Proposition 4.6.1 starts from a small generating category of accessible objects, forms its closure under bounded colimits, and claims essential smallness, equality with the appropriate accessible-object class, and an Ind-prime presentation of M. The proof builds the closure by transfinite stages and chooses an ordinal above the cardinal threshold.

**U06 — Essential smallness and a disputed bound (225–227).** A lemma treats filtered colimits of essentially small categories and the operation of adjoining represented colimits. Scan 226 defines card red using a reduced equivalent category. A corollary gives a cardinal estimate for the transfinite closure; scan 227 sets out the successor and limit estimates. The margins explicitly qualify the argument and majoration. Their precise abbreviated wording and some nearby indices remain doubtful; this return does not validate the numerical bound.

**U07 — The canonical functor and full faithfulness (228).** The proof identifies C with M-pi-zero by the closure criterion, then formulates Lemma 4.6.1.3 about the canonical functor from an Ind-prime construction. A Hom calculation is offered for full faithfulness using accessibility of the objects of M-zero. The essential-surjectivity argument is not present in this batch; the page ends after the displayed calculation.

## Statements left without proof

| ID | Scan(s) | Author's words and local status |
|---|---|---|
| A01 | 217 | The lemma presents “On a donc les” implications and cites the earlier demonstration in its margin, “4.5.6”, “4⇒5”, “page 117”. It does not give a separate expanded proof of every arrow here. |
| A02 | 218 | “c'est rappelé dans la démonstration” invokes SGA 4 I 9.13. The external text is neither consulted nor verified in this task. |
| A03 | 225–226 | “Cela résulte du lemme suivant, immédiat” introduces the essential-smallness lemma and its bounds. The second clause's majoration is separately marked “n'est pas prouvée”. |
| A04 | 228 | “est une équivalence de catégories” is followed here by a full-faithfulness calculation only. The remaining part is outside the present scan range, not declared absent from the manuscript as a whole. |

## Questions and conjectures

| ID | Scan(s) | Words and question |
|---|---|---|
| Q01 | 218–219 | “J'ai l'impression”, “je doute que la condition B) soit tjs satisfaite”, and “je ne crois pas que” mark the proposed relation between B and C and the universality discussion as tentative. |
| Q02 | 219, slanted note | “c'est faux !” qualifies the example, followed by cancelled doubtful wording and “mais vrai dans le cas particulier plus bas”. The precise scope of the correction remains a reading-sensitive question; **low confidence** in any reconstruction beyond these words. |
| Q03 | 223 | The earlier proof is called “incomplète (et erronée”. The stated issue is the claim that the Filt-pi family is a cardinal filtration. The written qualification “si on n'admet que” is preserved; no missing negation is supplied. |
| Q04 | 225, slanted note | “? Un peu court. Il faut invoquer le fait que” the ordinal-index set is grand devant pi-zero. The note asks for a stronger justification of the factorization step. Its cancelled final parenthesis is not treated as a live hypothesis. |
| Q05 | 226–227, margins | “Cette majoration n'est pas prouvée” and “majoration” with doubtful “non prouvée” are explicit reservations. The probable “probablement fausse” wording contains uncertain words/abbreviations, so a precise falsity claim has **low confidence**. No counterexample is supplied here. |

## Slips

These are local consistency comparisons, not independent proofs of the propositions. The full reading/state questions remain in the doubts file.

**S01 — B versus D in the family count (221). Model diagnosis, medium confidence.** The source defines `B = coproduct B_alpha`, then writes `card D`, and immediately resumes “indexée par B”. The locally matching letter would be **B**. The final audit read a single-bowl D in that position; the transcription keeps it.

**S02 — The successor-stage index (227). Model diagnosis, medium confidence.** After assuming the estimate for C-alpha, the application of clause 2° again has `card red C_alpha`. The successor step described in 224 would call for **C-alpha-plus-one** at that point. The missing +1 is not added. This local index comparison does not certify the disputed majoration.

**S03 — Cardinal subscript in the opening conclusion (228). Model diagnosis, medium confidence.** The opening says **C=M-pi**, while Proposition 4.6.1's second conclusion on 224 and the rest of this paragraph use **M-pi-zero**. A zero would make those references agree. The written pi is preserved.

**S04 — Category name in the last Hom (228). Model diagnosis, medium confidence.** The canonical functor is displayed from **Ind-prime-pi-zero(M-zero)**, whereas the last Hom subscript reads **Ind-pi(M)**. The former is the locally expected category for the comparison; the latter has no visible prime or zeros. The note records the mismatch without repairing it.

**S05 — Reading questions, low confidence.** The first Hom colimit index on 228 is `j|i`, although x-i and the subsequent inverse limit suggest i. On 225, the factorizing functor's alpha and the succeeding C-alpha-plus-one do not match the nearby alpha-prime in an entirely secure way, and cancelled subscripts intervene. The lemma number and La/Toute state on 225, the corollary's C-zero/C and le/la on 226, and the internal reference 2/4 on 228 remain reading questions. No spelling, agreement, gender or number error is asserted from those doubtful endings.

The extra closing parenthesis in 213's powerset display and the open parenthesis in 223 are retained. Their visible punctuation is recorded in the doubts file; no missing text is reconstructed.

## Pointers

| ID | Scan(s) | Source reference or supplied-note connection |
|---|---|---|
| P01 | 213–218 | Continuation of 4.5.13; reference to 4.5.6 and, in 217's margin, “4⇒5”, “page 117”. This completes the batch-boundary thread recorded in **K157-5-13 A07 and U06**. |
| P02 | 218 | “SGA 4 I 9.13” and inserted “SGA 4 I 9”. These continue the comparison in **K157-5-13 U05 and P05**; no external reference was opened. |
| P03 | 222–223 | Lemma 4.5.14; the return to “th. 4.3.6”, with inserted “p. 70–71”. |
| P04 | 224 | “cf 4.4.16”, “page|pge 101” for the canonical functor's preservation condition. |
| P05 | 225–228 | The rewritten lemma numbering and references to 4.6.1.2 and 4.6.1.3 are retained with their local doubts; later clear references do not normalize earlier ink. |
| P06 | 223–228; supplied K157-4-04 | **K157-4-04 P01** records a reference to notes on accessible categories and filtrations; **K157-4-04 U02** discusses ordinary adjoints under related size/limit assumptions. The present construction belongs to that documentary theme, without identifying an otherwise unattested cross-reference or rechecking the earlier theorem. |

## Remarks of the model

**R01 — Relation to GALOIS B.13. High confidence as a scope comparison.** The supplied register leaves **GALOIS B.13** open for an arbitrary derivator satisfying only Der 1–4. Scan 223 explicitly assumes a generating subcategory S of accessible objects and the relevant colimit structure; the subsequent construction works under these concrete hypotheses. These pages give no passage from bare derivator axioms to those hypotheses. They therefore do not settle the register's open question. This continues the scope observation in **K157-5-13 R01**. The register's status is carried as supplied, not re-proved.

**R02 — Qualitative construction and quantitative estimate. Medium confidence as a documentary distinction.** The pages first seek a small category presenting M, then state a particular cardinal majoration. The explicit “n'est pas prouvée” on 226 should accompany any use of that estimate. It is not a certification that the qualitative construction fails; nor does the written calculation on 227 remove the author's reservation. Any assertion of falsity based on the doubtful marginal wording remains at low confidence.

**R03 — Limits of the comparison. High confidence as a description of this return.** The supplied FINMON, EXIT_TOWER and section-conjecture results are not used as mathematical premises here. No finite-model, tower or arithmetic conclusion is drawn from these categorical pages. The event ledger records only the narrow local comparisons S01–S04, the scope comparison R01, and the background status actually carried; the documentary summaries above are not counted as proof checks. No independent re-proof, computation, formal certificate, literature search or general error audit was performed.
