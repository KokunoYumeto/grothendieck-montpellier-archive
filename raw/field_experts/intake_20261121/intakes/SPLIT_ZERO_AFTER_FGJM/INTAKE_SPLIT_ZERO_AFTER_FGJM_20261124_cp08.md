# Intake of SPLIT_ZERO_AFTER_FGJM, checkpoint 08 (first return of prompt 93)

By Claude Fable 5.2 at effort max (agent a2fedc2a31aa5abb9, the Longue Marche field expert, who rebuilt prompt 93
on 23 Nov), for the main session 329fb1e6 (Claude Opus 5.5 at effort max). 24 Nov 2026, 11:25-11:5x UTC (machine clock). The run is
GPT-6 Astra (ChatGPT Pro mode); it says its effort label was not exposed, and that no human has checked it. Every
status below comes from a check I made in this task; where I only read a statement I say so.

## 0. Scope

- **Return:** `grothendieck_archive_transcription_20261110/research_returns/SPLIT_ZERO_AFTER_FGJM_checkpoint_08_20261124T0328Z_unzipped`
  (created 02:28:32 UTC; the run started 23 Nov 20:28 UTC and was still going). Five papers (30, 22, 33, 23 and 53
  pages), `REGISTER.tsv` (281 rows), `CHECK_EVENTS.tsv` (548 events, all by instances of the same model),
  `QUESTIONS.tsv` (30 rows), `LEDGER.md`, a workbench with 63 programs. Four movement reviews, each with movement.
- **Read whole:** README, LEDGER, QUESTIONS; all theorem statements of papers 1, 2, 4 and 5; the main theorems of
  paper 3 at statement level.
- **Read in full, every step followed:** paper 4 to its section 6 (Theorems 1.1 and 1.2 with all their lemmas, the
  read-one proposition, the Petersen example); paper 5: the cell theorem, the unrestricted lift, the Hecke bridge and
  the non-unimodality theorem; paper 2: the support-and-trace theorem with its two propositions; paper 1: the general
  action theorem, the direct-sum monoid with the two lemmas and the classification proof, the corollary on
  cancellative semimodules.
- **Recomputed with my own programs** (`checks/`): the Petersen example; the unrestricted rank-three table; the
  rank-three structure constant of GCT VIII in both sign readings.
- **Source opened at the locator:** GCT VIII, arXiv:0709.0751v2 (TeX). Not opened: FGJM Proposition 5.2, Jukna,
  Amano-Maruoka, Forsberg, Jerrum-Snir (the context guard stopped further literature); their use is reported from
  the run.
- **Statement level only:** paper 3 entirely; paper 1's sheaves, iterated and absorber extensions, Construction 3.5,
  lattice, group and monoid extensions; paper 2's quotient counting, Witt products, number-field and cyclotomic
  extensions, the Hurwitz certificate (not rerun); paper 4 after section 6; paper 5's sharp count 38, projective
  points, adeles, rank four, Kronecker counts.

## 1. Verdicts (my check events; ids are the run's)

| Result | What I did | Outcome |
|---|---|---|
| P4 Thm 1.1, the one-sided support bound (P4-Q2, P4-Q8) | every step: base and core, normal form, transposition count, the OR lemma, centres | **confirmed** |
| P4 Lemma 4.1, OR gates for nearly disjoint sums, AND gates allowed | every step | confirmed |
| P4 Thm 1.2 with Lemmas 3.1, 3.3 and Prop 3.2 (AC-1 steps (i)-(v), P4-Q1) | every step | confirmed |
| P4 Prop 2.1, Cor 2.2 (P4-002, P4-003): R_0[M] = (B[M], S ↦ R^S) | every step | confirmed |
| P4 Prop 6.1, read-one bound for every C4-free graph | every step | confirmed |
| P4 Example, Petersen (the fleet's L-meta-584) | recomputed | confirmed: 13 + 7 = 20 gates; edges 01, 05, 16, 69 have no quadratic witness |
| P2 Thm support and trace, Props effective quotient, Gaussian class | re-derived | confirmed |
| P1 Thm general action (FND-015) | both directions | confirmed |
| P1 Thm direct-sum monoid (FND-007), with the classification proof | every step | confirmed |
| P1 Cor cancellative (FND-012), against our H22 v3 (FND-013) | own argument | confirmed; **H22 v3 has two false sentences** |
| P5 Thm cell forces supported zeros | every step | confirmed |
| P5 Thm unrestricted lift (P5-016) | proof read; recomputed | confirmed: 1000 triples, 5,384 supported zeros, none at Σ |
| P5 Thm non-unimodality, Lemma Hecke bridge | proof read; third computation; source compared | confirmed; **GCT VIII's computer-check sentence is contradicted** |
| our Proposition 6 (counting consult, 21 Nov) | reread against the run's remark | **gap**: proved only when the bottom line stays an ideal |

Counts: 13 results confirmed (12 with the proof followed, two of them also recomputed; the Petersen example by
recomputation), 1 gap in our own earlier record, 1 false statement in our own note (two sentences of H22 v3), 1
published statement contradicted. I found no fault in the run's mathematics in
what I read. Everything else is unread by me and carries only the run's same-model checks.

## 2. What is new, usefulness first

1. **The exact count |E| + τ − 1 in a wider class than the fleet's L-meta-647** (paper 4, Thm 1.1). Good for: the
   fleet's main line, where 647 was a conjecture on 23 Nov; it is the "second reader" of our own paper proof
   (meta.md 5.1), in a stronger form. For a bipartite graph without a 4-cycle, among circuits whose formal monomials
   contain at most one distinct variable of one side, #OR ≥ |E| − 1 and #AND ≥ τ. Arbitrary powers are allowed, so
   every polynomial supported exactly on edges is covered. Consequence for 608 and 612: a bipartite counterexample
   must mix two distinct variables of X in one monomial and two of Y in one monomial.
2. **Our map AC-1 is proved, and credited correctly** (Thm 1.2). The support criterion is Jukna's (Lemma 1 of his
   read-k notes); R_0[M] for free M is FGJM Proposition 5.2; what is added is the inverse semiring T_V and the exact
   equality Mon(f_G) = min over Sup(G) of Arith(P). Good for: stating 606, 608, 612 as arithmetic questions.
3. **Supported zeros and edges covered only through x² = x are independent** (paper 4, Prop "distinct"; statement
   read). This answers question 4 of the prompt's direction block negatively: no bound transfers between the circuit
   problem and the dimension-ring problem by lifting alone. Program transfer along a homomorphism is exact.
4. **The link with Caviglia-Faul-Manuell-Mesiti exists now.** Z_0[q, q⁻¹] is the quotient of the effective sign
   classes by 1 = 2 + ε; a supported zero is k(1 + ε), with zeta ζ_{Q(i)}^k, so it fixes neither multiplicity nor
   realization; the degree-one slice belongs to the arithmetic realization, not to (Q, F). Good for: the recall
   report's open point, now closed in exact terms.
5. **Where 1 + ε is forced** (paper 5). Forced when the bottom line stays an ideal (support at Σ reaches weights ±3;
   least count 38 in the cell shape); not forced for unrestricted support tables; open for unrestricted dimension
   rings. Good for: the exact form of the project's statement on the gluing of the two sheets.
6. **GCT VIII, rank three: unimodality fails**, now proved in closed form and by three computations. Good for: a
   note to the author; it also separates positivity (holds) from a Lefschetz-type property (fails).
7. **Foundation:** semimodules over every inverse semiring are module diagrams for (Q, F); K_0(R_0) is free on
   connected labelled posets; further classifications (statement level). Good for: H22, whose open question this
   answers; anyone working after FGJM and CFMM.
8. **Rank four** (statement level): the order generated by P_1, P_2, P_3 has generic rank 114 and is free after
   inverting an integer M exactly when 6 divides M. Good for: the GCT line's E(4) question.
9. **K-theory of the one-zero C*-algebras** (paper 3, statement level): the boundary sequence of K_1 is nonsplit
   exactly for two or more finite primes; every finite order occurs as torsion in K_1 for some four odd primes, and
   with at most three primes the torsion is two-primary. Good for: the place-balancing strand of the workbench.

Against our own results: 1 contains meta.md 5.1; 2 proves AC-1; 5 corrects Proposition 6; 6 is the independent
re-run the research note asked for. Against the literature: the run credits Jukna, Jerrum-Snir, Schnorr,
Amano-Maruoka (whose proof of their Theorem 5 already has the flat count), Forsberg, Ramachandran, Levinson and
Frisk-de Gosson; it claims no novelty from failed searches.

## 3. Scope of the inputs

Alpöge's theorem is used in paper 2 only for shifted Dirichlet factors, which is its scope. Nothing uses Hecke or
Artin L-functions. Papers 1, 3, 4 and the algebra of paper 5 use no analytic input.

## 4. Integration

Applied (7 edits, logged in `INTEGRATION_SPLIT_ZERO_AFTER_FGJM_20261124.tsv`, backups in
`integration_backups/20261124/SPLIT_ZERO_AFTER_FGJM/`): the correction after Proposition 6 in the counting consult;
two notes in the research note (section 4, and section 8 item 6 marked done); one in the Connes-Consani-terms file
(section 12, item 2); S6(d)-(f) in the shapes file; an addendum to the recall report; a new file
`reports_20261123/h22_note/CORRECTION_NEEDED_20261124.md`.

For the main session (7 rows in the same log): H22 v3 → v4 (two sentences); the board; the two fleet-map files; the
successor of 93; the candidates register.

## 5. Prompt updates (for a successor of 93 or its final)

- Replace "the bottom cell cannot be split (Proposition 6)" by the corrected form, and ask the open case: must an
  unrestricted dimension ring have cancelling pairs at Σ; does the run's interval support table have an effective
  lift.
- The circuit gate: a monomial mixing distinct marked variables on both sides; the run's reductions (terminal
  product, common masks, private mask, co-occurrence) name what a counterexample must evade.
- Rank four: a positive basis over Z[1/6][v, v⁻¹]; the classification of torsion in K_1; projectives over a general
  (Q, F).
- Tell the run that H22 v3's two sentences are corrected, and give it the fleet's formal statement of L-meta-647.

## 6. Hexagon readiness

| Finding | Complete | Self-contained | Stable | Checked | Interest | Gate left |
|---|---|---|---|---|---|---|
| One-sided bound (paper 4) | yes | yes | at risk: the fleet may settle 647 any hour | run + this intake | high | read 647's formal statement and status; open Amano-Maruoka and Jukna |
| GCT VIII unimodality | yes | yes | yes | three computations | high for GCT | the e-mail first |
| Foundation extensions (paper 1) | yes | yes | the run continues | two theorems by this intake | medium | fix H22 v3; literature on Clifford semimodules |
| Support and trace (paper 2) | yes | yes | yes | this intake | low alone | fold into H22 or paper 2 |
| Rank four, K-theory | yes | yes | moving | run only | medium | an independent check |

## 7. Board candidates (columns of HEXAGON_BOARD.tsv)

| id | line | result | stage | scope | interest | checks | gates_left | next | source |
|---|---|---|---|---|---|---|---|---|---|
| S93a | complexity (fleet) | Exact count \|E\| + τ − 1 for edge functions of bipartite C4-free graphs among circuits whose formal monomials have at most one distinct variable of one side; contains L-meta-647 | G2 | bounded | high | run (separate instances); this intake, step by step; our earlier paper proof (Claude Opus 5.5 at effort max) | 647's formal statement and present status; Amano-Maruoka 2004 and Jukna opened | editor after the gate; file with the fleet on the user's word | paper4, Thm 1.1 |
| S93b | GCT | GCT VIII's rank-three unimodality assertion fails in both sign readings; positivity holds | N | bounded | high | Claude Opus 5.5 at effort high (21 Nov); run; this intake (third method, source compared) | the user's word on the e-mail | send EMAIL_DRAFT_Mulmuley_20261124.md | paper5; E4_RANK_FOUR |
| S93c | foundation (with H22) | Semimodules over every inverse semiring are module diagrams for (Q, F); K_0(R_0) is free on connected labelled posets | G2 | cluster with H22 | medium | run; this intake | H22 v3's two sentences; literature; second reader for the other classifications | decide: H22 v4 or a second note | paper1 |
| S93d | GCT | The rank-four order of the nonstandard Hecke algebra is free after inverting M exactly when 6 divides M; generic rank 114 | G2 | moving | medium | run only | independent check; comparison with GCT IV 11.8 | wait for the final | paper5 |
| S93e | operator algebras | K_1 of the semilocal one-zero C*-algebras: nonsplit boundary sequence exactly for two or more primes; every finite torsion order with four odd primes, two-primary torsion for at most three | G2 | moving | medium | run only | a reader of paper 3 | wait for the final | paper3 |

## 8. For the P versus NP fleet (maps, not graded)

| Our result | Fleet nodes | Translation | Work to complete |
|---|---|---|---|
| paper 4, Thm 1.1 | **L-meta-647** (conjecture on 23 Nov), 738, 739, 720, 655 | 647 is the syntactic degree-one case; the theorem also allows products of wires in the same marked variable | compare 647's formal statement (is the free side fixed?); Lean: the base/core normal form and the centre lemma |
| paper 4, Lemma 4.1 | **L-meta-529**, 270 | the OR-only form of 529 that our map proposed: sums with pairwise intersections ≤ 1 need Σ(\|S_i\| − 1) OR gates even with AND gates and constants | a variant of the fleet's proof of 529; file as a lemma |
| paper 4, Thm 1.2 | 606, **608**, 612 | Mon(f_G) = min over Sup(G) of Arith(P); line-degree = degree of P_C | a definitional lemma (formal polynomial, support criterion), with Jukna credited |
| paper 4, Prop 6.1 | **613** (checked) | the flat count; its literature source is the proof of Amano-Maruoka's Theorem 5 | add the attribution |
| paper 4, Petersen | **584** (checked) | four edges are covered only by monomials with a square; #OR ≥ \|E\| − 1 fails, the total does not | none; it explains why 608 needs a joint charge |
| paper 4, sections 9-10 | 608, 612; searches 650, 655, 582 | a minimum counterexample has no terminal product of the stated kind, no common mask, no private mask; with H_X C4-free every output monomial has at most three distinct marked variables | prune the SAT encodings |
| paper 4, example on PG(2,3) | 270, 666, 667, 739 | singleton agreement does not give the OR count: 33 < 39 | none; a caution for promise versions |
| paper 5, rank four; Kronecker counts | the fleet's GCT programme | no node found by title; not searched further | propose nodes after the final |

## 9. Corrections

- **Published work:** GCT VIII (arXiv:0709.0751v2), subsection "Positivity" of the rank-three section. Draft:
  `EMAIL_DRAFT_Mulmuley_20261124.md`. The constant is printed in the paper's own figure.
- **Our own:** Proposition 6 of the counting consult (gap); H22 v3, source lines 89 and 227; the translation note's
  section 9.2 on decoding. The run also corrects twenty statements of the first papers and the corpus (its register
  rows with status "refuted"); I did not check those.
- **The notes in the ZIP:** the run recorded that our notes are personal and returned none of them.

## 10. Paths

- This intake, its check events, the integration log, the primer and the e-mail draft:
  `field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/`.
- My programs and the fetched source: `checks/` there.
