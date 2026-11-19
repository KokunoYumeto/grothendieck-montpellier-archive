# Independent task-to-answer scope audit: A.6(a), especially 049(c)

Date:2026-11-19. Reviewer: GPT-6 Astra (OpenAI), agent `part_b_cycles`. This is a new scope audit, separate from the earlier proof audit of the model-system theorems. No root manuscript, report or shared ledger was edited.

## Decision

**I find no additional mathematical reconstruction gate forced by the literal wording of049(c), provided the report retains the explicit Isom-anabelian interpretation and the equal-characteristic-zero scope of the specialization theorem.** The current construction and proofs genuinely supply a definition, existence, a choice-independent system of compactifications, and compatible specialization of their finite-cover data. Their reconstruction assertion is a theorem on a specified Isom-anabelian class, not a theorem proving that arbitrary smooth varieties are anabelian.

The strongest justified report wording is:

> Definition and full marked model system proved in characteristic zero; equal-characteristic-zero logarithmic specialization proved; reconstruction on a specified Isom-anabelian class. A selected log-canonically polarized model is recovered only when its log canonical bundle is ample. No claim of arbitrary higher-dimensional special-fibre reconstruction from the pulled-back tangential Galois action is made.

If the task is instead interpreted as requiring the Isom theorem for a broader, independently defined geometric class whose anabelianity has not been proved, that extra statement must remain conditional or INCOMPLETE. The present model theorem does not establish its input. It would be inaccurate, however, to introduce that stronger universal assertion as though the original sheet explicitly demanded it.

## What the actual input says

I reread the original scan directly: `notes/original_scans_a567/crop049.png`, lower third of the page, archive foliation51. The matching unchanged transcription is `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex`, line1081:

> c) S'inspirant des compactifications MD des M_(g,nu), définir ce que c'est qu'une compactification anabélienne d'une variété lisse anabélienne (sur un corps K de car.0, qu'on peut supposer être de type fini sur Q). Comportement par spécialisation ???

The word **anabélienne** qualifies the input smooth variety. The sheet requests a definition inspired by Deligne–Mumford compactifications and asks about specialization. It supplies no formal axiom of uniqueness, minimality, reconstruction of every chosen model, anabelianity of every boundary stratum, or reconstruction of a higher-dimensional singular fibre from a tangential action alone. Those are conceivable strengthened questions, but are not written assertions.

The prompt at line182 asks, for each049(a),(b),(c) and NB048, for the proved statement answering it with derivation from sources. Lines137–151 and242–248 prohibit silently replacing an assertion by a convenient special case or using unchecked hypotheses. Consequently every substantive restriction must remain visible, but the audit must also avoid inventing a more demanding assertion than the actual input.

## Exact correspondence between demand and proved result

| Demand or interpretation | Result actually proved | Scope assessment |
|---|---|---|
| Define a compactification carrying the boundary/normal information suggested by MD | `part_a6.tex:212–229` defines a smooth proper SNC pair, its strata, normal tori and global tangential finite-cover functors. | A definite mathematical category is supplied. A chosen vector is extra data, not secretly obtained from the bare group. |
| Existence in arbitrary dimension | `A6-SNC-existence`, lines231–235, uses Temkin1.1.15 with Y0=Y=U over Spec(k). | All smooth separated finite-type characteristic-zero varieties; no dimension or quasi-projectivity bound. Thus it applies to every input member of the specified anabelian class. |
| Avoid dependence on a distinguished compactification | `A6-model-system`, `part_a6_model_system.tex:7–116`, proves nonempty cofiltered common domination, uniqueness of arrows, and canonical marked pro-system. | All smooth geometrically connected separated finite-type characteristic-zero U. It does not claim the pro-object is a single proper scheme. |
| Arithmetic reconstruction of that model system | `A6-model-system(iii)`, lines29–35 and105–116. | Explicitly assumes the interior class is Isom-anabelian. The existing adjective on the sheet is formalized this way. A compatible group isomorphism first recovers U→V, which then induces the complete reindexing/extension of model systems. No analogous anabelian assumption is imposed on the strata. |
| Recover a single distinguished geometric model | `A6-canonical-compactification`, `part_a6.tex:280–320`. | True when the SNC compactification has ample log canonical bundle; its Proj is then intrinsic. Existence of such an ample smooth model for every anabelian variety is not established or used. |
| Specialization | `A6-log-specialization`, lines240–275, and `A6-model-specialization`, model-system lines131–241. | Actual proper log-regular models of the same generic open over the same R=k[[t]], with k of characteristic zero. Full finite covers are tame because every relevant residue characteristic is zero. The theorem compares cover categories and augmented groups; it does not reconstruct each chosen special-fibre scheme from them. |
| Compatibility between choices of degeneration model | `A6-model-specialization`, lines179–239. | Common refinements exist over this excellent characteristic-zero trait; comparison functors are normalized by restriction to the fixed U and preserve the augmentation and same framed section. No comparison with an unrelated k-compactification is asserted. |

The adjective “complete” for the model system means the category of all such marked models and its associated pro-object, not that every term has become a distinguished choice. The full model category can be constructed after recovering U. Passing to a cofinal subsystem does not select one model or one normal frame.

## Are the anabelian hypotheses actually established anywhere they are applied?

Yes for the named examples, with the stated limits. I independently reopened the published original:

- Hoshi, *The Grothendieck Conjecture for Hyperbolic Polycurves of Lower Dimension* (2014), https://www.ms.u-tokyo.ac.jp/journal/pdf/jms210201.pdf . Corollary3.18, originalpp203–204, states the exact bijection for hyperbolic orbi-polycurves over a sub-p-adic field when either dimension is at most4. Its definition3.17 and full deduction were read. Web refs `turn622008988view0`, `turn139747514view0`. Ordinary hyperbolic polycurves are included. A finitely generated field over Q is sub-p-adic after embedding its finite algebraic extension of a rational function field in a finite extension of Q_p(t1,...,tr).
- Carlson's2026 **preprint**, https://arxiv.org/html/2604.24898v1 , TheoremA=3.11, gives the Isom theorem for ordinary hyperbolic polycurves of every dimension over sub-p-adic fields. Theorem3.11 and its final proof from Corollary3.16 and Hoshi's polynondegenerate Hom theorem were reopened: `turn622008988view1`, `turn139747514view1`. The explicit preprint status is retained. This source is not silently made a published theorem or extended to arbitrary smooth varieties.

The proof of `A6-model-system` is independent of Carlson: its first two parts hold without anabelianity, and its reconstruction part expressly names the Isom input. Neither it nor the specialization theorem applies the Hoshi/Carlson Isom theorem to arbitrary k((t))-varieties. The specialization theorem does not require generic or special fibres to be anabelian. Therefore there is no hidden use of a sub-p-adic hypothesis for the Laurent-series field.

The earlier independent proof audit `notes/part_b_a6_model_system_audit.md` already opened and verified Temkin1.1.11/1.1.15 and HoshiLog Corollary3.9/PropositionA.10 with the exact total-space/trait hypotheses. This scope audit reread the manuscript's uses of those inputs; it does not merely rely on a previous “Proved” label.

## What definitely does not follow

1. The Isom-anabelian input is not a conclusion of the model-system construction. If membership in that class is only conjectured for a proposed new family, reconstruction for that family remains conditional. The construction does not provide a universal geometric recognition criterion for anabelian varieties.
2. A chosen SNC compactification is not recovered from the bare group of its open. The existing six-versus-seven-boundary-component blowup example already refutes that statement, even for a product of two hyperbolic curves over Q.
3. A chosen higher-dimensional logarithmic special-fibre **scheme** is not recovered from the finite-cover category or from the pulled-back tangential G_k action. The theorem gives an equivalence of those categories across modifications, not equivalence of the underlying schemes.
4. The current specialization result is equal-characteristic zero. It must not be described as an unrestricted mixed-characteristic or wild-ramification theorem. In mixed characteristic, one must formulate the appropriate tame/prime-to-residue-characteristic cover category and retain actual log-regular-model hypotheses; full-cover invariance would be false in general.
5. Neither specialization-stability of anabelianity nor anabelianity of all boundary strata is proved. They are not used in the displayed arguments.

## Explicit obstruction to a stronger special-fibre reconstruction claim

There is a complete geometric counterexample, so the arbitrary chosen-model version is not merely an unknown gate. Put R=Q[[t]], F=Q((t)), and take X=(P1_R)^2 with the six horizontal boundary divisors and the vertical special fibre. The generic open is U=(P1 minus{0,1,infinity})²_F. Blow up the closed boundary point (x,y,t)=(0,0,0). This is a smooth center in the regular three-dimensional total space. In the x-chart, y=xv and t=xu, so the reduced total boundary has equation xvu=0; the other two charts are analogous. Thus the blown-up total space is regular with SNC boundary, proper and flat over R, and has exactly the same generic open U.

The old special fibre is irreducible P1×P1. The new special fibre has two reduced irreducible components: the strict transform Bl_point(P1×P1) and the exceptional P2, meeting in P1. They are not isomorphic special-fibre schemes. Nevertheless `A6-model-specialization` gives the same finite Kummer-etale cover category over G_F, and after pulling back along the same t-frame the same tangential extension over G_Q. The construction also descends to the trait Q[t]_(t); its generic interior over Q(t) is an actual dimension-two hyperbolic polycurve covered by Hoshi's published Isom theorem. Thus the nonuniqueness is not an artifact of starting with an unproved anabelian geometric example.

At the parent's request this counterexample was subsequently appended as the fully proved numbered proposition `A6-special-fibre-counterexample` at the end of `sections/part_a6_model_system.tex`, stable at13:59:23UTC. The exact finite chart certificate `code/part_b_special_fibre_checks.py` checked all3 substitutions and15 assertions, including SNC supports, unimodular torus exponents and multiplicity-one vertical factors, in0.38060833100098534seconds. Its JSON output is retained. Properness, regularity at all points, global component identifications and the augmented finite-cover equivalence are proved in the manuscript, not asserted as conclusions of the finite computation. Separate results/events are in `checks/part_b_a6_counterexample_results.csv` and `checks/part_b_a6_counterexample_events.tsv`. The parent independently read the proof and agreed. The complete model-system theorem avoids the obstruction by retaining every model and distinguishing a chosen model from its cover data.

## Other portions of A.6(a)

The audit also reread the actual formulations for049(a),(b) and NB048. `A6-anabelian` explicitly uses a framed logarithmic/admissible group, K finitely generated over Q, stable hyperbolic components, nonzero normal tensors, and prescribed labels. Its proof verifies the component sub-p-adic input rather than assuming every singular scheme is anabelian. The ordinary-group reading is separately refuted. The bare procyclic criterion is refuted by the explicit subgroups mI; the corrected graphicity theorem is distinguished from a general assertion that every maximal invariant procyclic group is geometric. NB048 is not silently identified with a theorem that there are exactly three conjugacy classes. No scope inflation was found in those written statements in this review.

This is a task-scope audit, not a new independent reproof of every cited combinatorial-anabelian source. The detailed prior proof reviews and source locators remain the evidence for those deductions.

## Report recommendation

The current dedicated049(c) row already says that anabelian reconstruction is conditional, and the manuscript explicitly limits all stronger claims. To prevent an abbreviated summary from overstating the result, add **equal-characteristic-zero** before “specialization” and say **on a specified Isom-anabelian class** rather than leaving “conditional” unexplained. On that explicitly declared interpretation of the sheet's word “anabelian,” I would not add a new INCOMPLETE reconstruction gate. If the root decides to promise an additional broader geometric class, its Isom theorem must be separately proved or listed as a genuine remaining gate. The unconditional model geometry itself is complete.

## Current integration status, 19 November2026 at14:10UTC

Any historical statement that this counterexample was not yet numbered or that its certificate had not yet executed described the **preintegration** draft only. The current manuscript contains the fully proved numbered proposition `A6-special-fibre-counterexample`; `code/part_b_special_fibre_checks.py` has executed successfully on **3 charts and15 assertions**, with its exact output and0.38060833100098534second runtime preserved. The counterexample's mathematical proof and its scope limitations are fully integrated; no mathematical gate is carried forward merely because of that obsolete drafting status. The parent and the independent C reviewer both read the integrated proposition and found no mathematical gap.
