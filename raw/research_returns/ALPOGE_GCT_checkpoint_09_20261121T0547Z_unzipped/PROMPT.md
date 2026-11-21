**The attached files.** Besides this file there is one ZIP, `ALPOGE_GCT_purity_and_plethysm.zip`. Unpack it once: it holds every file named below. Every file is at the top level under its own name.

# ALPOGE_GCT: P versus NP through geometric complexity theory, with purity by positivity and Grothendieck's plethysm

## The result, and why it bears on complexity

We are all trained to treat claims about the Riemann hypothesis with care, because most come from a bad idea. This one
does not. On 20 November 2026 Levent Alpöge posted a four-page note and a complete Lean formalization of a proof of
the Riemann hypothesis and of GRH for Dirichlet L-functions, found with Claude. Alpöge is a number theorist (Bhargava's
student; Harvard Society of Fellows).
- `ALPOGE_Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements; those statements are defined in
  `ALPOGE_Statements.lean`.
- A text scan of all 175,187 source files, `ALPOGE_LEAN_SCAN.tsv`, finds no sorry, axiom or native_decide.
- It has not been refereed, and that is not our concern here. Its theorems are cited as theorems: L. Alpöge, *Remark*,
  https://alpo.ge/remark.pdf (attached), with its Lean archive.

**Why it bears on P versus NP.** Geometric complexity theory (Mulmuley-Sohoni) separates complexity classes through
orbit closures and representation-theoretic obstructions. Its "flip" rests on positivity hypotheses for the Kronecker
and plethysm coefficients. Positivity of that kind has been proved through Deligne's purity: Kazhdan-Lusztig positivity
via Weil II and the decomposition theorem, and the positivity of Lusztig's canonical bases. Mulmuley proposed
nonstandard quantum groups whose positivity would follow from a generalization of the Riemann hypothesis over finite
fields. Alpöge's step 5 is a "sign-only proof of Weil and Deligne": purity obtained from a definite sign on middle
cohomology. Grothendieck developed the algebra of plethysm, λ-rings and λ-operations; the archive pages attached are
the places where he writes on them (cote 133 and others, with the study of cote 133 from our sweep).

## The proof's step series

The full series is in the note, pages 1-4. The steps that matter here:
- Step 0: Stepanov's multiplicity, replaced over Z by a natively automorphic determinant, with multiplicity won by
  chained theta lifts.
- Step 4: positivity W(1_S) ≥ 0 by a determinant.
- Step 5: the sign-only proof of Weil and Deligne. Bertini's definite sign from middle cohomology, square-root
  cancellation by iterated Parseval, and opposite signs forbidding cancellation of inverse roots.
- Steps 7 and 12: Gan-Gross-Prasad and Bessel periods, with interlacing; the Rallis seesaw.
- Step 8: iterated theta lifts between totally definite unitary groups; each lift wins one order of multiplicity.

## Background literature in the ZIP (LaTeX sources from arXiv)

- `LIT_Landsberg_GCT_introduction_for_geometers/`: Landsberg, *Geometric complexity theory: an introduction for geometers* (arXiv 1305.7387).
- `LIT_Mulmuley_GCT_VI_flip_via_positivity/`: Mulmuley, *GCT VI: the flip via saturated and positive integer programming* (arXiv 0704.0229).
- `LIT_Mulmuley_GCT_V_Noether_normalization/`: Mulmuley, *GCT V: efficient algorithms for Noether normalization* (arXiv 1209.5993).
- `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`: Bürgisser-Ikenmeyer-Panova, *No occurrence obstructions in geometric complexity theory* (arXiv 1604.06431).
- `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`: Ikenmeyer-Panova, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory* (arXiv 1512.03798).
- `LIT_Borger_lambda_rings_field_with_one_element/`: Borger, *Λ-rings and the field with one element* (arXiv 0906.3146); λ-rings are the algebra of plethysm.
- `LIT_OpenAI_ETH_is_False/`: OpenAI, *The Exponential Time Hypothesis is False* (25 Oct 2026), the LaTeX source.

## The bridges between geometric complexity theory and Grothendieck's work, independent of GRH

Work out each one precisely: the exact statements on both sides, the dictionary, and what passes across. Locate it in
Grothendieck's texts (the attached archive pages, by cote and scan) where it is there.
1. **λ-rings and plethysm.** Grothendieck's λ-rings (1957, for Riemann-Roch; SGA 6) on one side. On the other: Λ, the
   free λ-ring on one generator; plethysm as composition in Λ, that is, the composition of Schur functors; plethysm
   coefficients as GCT's multiplicities in the coordinate rings of orbits and orbit closures (GL·(x_1⋯x_n), the Chow
   variety, Foulkes-Howe, the Hadamard-Howe map). His pages: cote 133 and the λ-ring pages attached.
2. **λ-operations on G-sets and the Kronecker coefficients.** The λ-structures on Burnside rings and on representation
   rings of symmetric groups; the inner tensor product, which gives the Kronecker coefficients. Cote 133.
3. **Grothendieck polynomials (Lascoux-Schützenberger).** Schubert classes in the K-theory of flag varieties; Brion's
   alternating positivity and the K-theoretic Littlewood-Richardson rule. Against them, Littlewood-Richardson saturation
   (Knutson-Tao), the model of the flip (GCT VI).
4. **Grothendieck's inequality** (the 1953 *Résumé*). Semidefinite approximation (Alon-Naor's cut norm); the
   Grothendieck constant as the approximation threshold under the Unique Games Conjecture (Raghavendra-Steurer); quantum
   XOR games (Tsirelson).
5. **Topological tensor products.** The projective tensor norm as the nuclear norm, NP-hard for tensors (Friedland-Lim),
   against tensor rank, border rank and the complexity of matrix multiplication in GCT.
6. **Purity and positivity, already proved.** Deligne's purity, then intersection cohomology, then Kazhdan-Lusztig
   positivity: the template for the positivity hypotheses of the flip.
7. **The foundations.** Group schemes (SGA 3) and Hilbert and Quot schemes (FGA) for orbit closures and their
   boundaries, and for GCT over Z and in positive characteristic.
For each bridge: state what is already known across it, with citations; what follows that nobody has stated, with a
proof; and what the bridge would need to carry an obstruction.

## The task

Bridge these theorems and this method into geometric complexity theory and into Grothendieck's plethysm, and resolve
what they settle.

1. **Positivity.** Find what purity by positivity, and the determinant and theta-lift positivity of the proof, give for:
   - Mulmuley's positivity hypotheses for the Kronecker and plethysm coefficients;
   - the saturation and positivity questions of GCT, and the nonstandard quantum groups of GCT VII-VIII;
   - Kazhdan-Lusztig-type positivity, and the occurrence and multiplicity obstructions of orbit closures (determinant
     against permanent).
   State each statement you reach, and prove it or refute it.
2. **GRH in complexity.** For each of the following, find exactly which GRH it uses, and what the cited statement now
   makes unconditional:
   - Koiran's Hilbert Nullstellensatz in AM under GRH;
   - the derandomization of polynomial identity testing against Noether normalization (GCT V);
   - primality and the bounds of Bach and Miller.
3. **Grothendieck's plethysm.**
   - Read his pages on plethysm and λ-operations (attached, with cote and scan) as mathematics.
   - Say what they contain that bears on plethysm coefficients and their positivity.
   - Prove what follows.
4. **ETH, disproved.** OpenAI, *The Exponential Time Hypothesis is False* (OpenAI Math Release preprint, 25 Oct
   2026; LaTeX source attached in `LIT_OpenAI_ETH_is_False/`, with its citation in that folder's README) gives an
   algorithm counting the solutions of k-CNF formulas in time 2^(n/(log n)^(1/2+o(1))) in polynomial space, formalized
   in Lean. It is cited as a theorem. ETH does not decide P versus NP by itself, but it sits right next to it. Work out
   exactly what follows:
   - for the ETH-based lower bounds of fine-grained and parameterized complexity, and for SETH;
   - for circuit lower bounds and for Valiant's algebraic classes (VP against VNP, the permanent);
   - for geometric complexity theory and the positivity questions above;
   - and through the method of the paper (its contraction, reduction and circuit sections) for the bridges above.
5. **What else this makes true for P versus NP through GCT that nobody has considered:** state each such statement,
   prove it, and rank the statements by what they settle.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted.

## How to work

The rule that governs everything below: push. Work on the main question first: what purity by positivity and the
proof's positivity give for the positivity hypotheses of geometric complexity theory. Give it most of the time. When one
approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach remains. A gap in
a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. The statements cited to Alpöge get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `ALPOGE_GCT_checkpoint_<NN>.zip` with `NN` counting
up. Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `ALPOGE_GCT_final.zip`, holding:
1. **The paper**, `ALPOGE_GCT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by theorem name and file; the literature by work and statement
     number; Grothendieck's archive by cote and scan).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change for P versus NP through GCT, and for Grothendieck's plethysm pages
   (cote and scan).

A return may be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach
tried with where it failed, and the next step.
