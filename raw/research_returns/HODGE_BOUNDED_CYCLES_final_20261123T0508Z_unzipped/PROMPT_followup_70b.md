# HODGE_BOUNDED_CYCLES, follow-up 1: the paper as a reader will meet it (23 Nov 2026)

This message adds to the first one; everything in it stands: the main question, the rule on finishing, the reviews
against the dated ledger, the checkpoint ZIPs and CHECK_EVENTS.tsv. Record this message in the same ledger and work to
it from now on. Do not restart.

## Where the paper stands (your checkpoint 02)

The draft is good. It compiles to 40 pages with no overfull box and no undefined reference. Its proofs of the family
criterion, the Poincaré-pairing bound on the multiplier, the lifting from one place, the special families, the
quadratic extraction with exponent n(2n+1), the bound 48, and both stabilization theorems were read line by line by
an outside checker, who found no error. The equivalence is stated with the map induced by a morphism of Shimura data,
as it must be. No run name, internal id or path appears in the text.

What follows is what a reader still misses. Do these as part of the writing, while the research goes on.

## The opening

1. **The state of the field, first.** Voisin's Bourbaki exposé 1248 (January 2026), which the paper cites only for
   Lemma 2.9, is titled "La conjecture de Hodge pour les variétés abéliennes de dimension au plus 5". Open it and state
   in Section 1, before the theorems, exactly what is now known: for which abelian varieties the Hodge conjecture is a
   theorem, by whom (Markman's secant sheaves, and whoever else the exposé credits), with statement and page. Then say
   what this paper adds there: explicit degree bounds in dimension 4, and the criterion in every dimension.
2. **Eightfolds over Q(√−3).** Your register treats split eightfolds over that field as settled, but the paper cites
   neither Severn's Hexagon preprint 2610.00387 (unrefereed) nor any proof of it. Either prove that case in the paper,
   with every input opened, or cite the preprint with its status and say exactly what it claims, in Section 1 and in the
   section on what remains open. Do the same for the withdrawn OpenAI eightfold manuscript: one sentence on its status.
3. **Markman.** The paper says that Markman's ICM theorem gives algebraicity for split Weil sixfolds over every
   imaginary quadratic field and for all Weil fourfolds. Open the ICM text and the detailed preprint, and quote the
   exact statement and page, distinguishing what the published account proves from what it sketches.
4. **The abstract.** Say in it that the equivalence uses only published theorems, and that the recent proofs for CM
   abelian varieties are not inputs. Write "the Hodge conjecture", as the field does, in the abstract and the title.
5. **Why anyone should care.** Give this its own short paragraph in Section 1, at its true scope. If one accepts the
   unrefereed proofs for CM abelian varieties, the cycles exist at each CM point, and the Hodge conjecture for abelian
   varieties becomes exactly the passage from a bound at each point to one bound for all. For Weil classes the bound is
   class-independent, and explicit numbers exist in the cases listed.
6. **The credit, split exactly.** In one paragraph of Section 1, state what is not new, by statement and page:
   - the closed-locus and Baire argument (Cattani–Deligne–Kaplan, p. 483);
   - the qualitative dense-set criteria (Bhattacharjee–Bhattacharya, Hexagon 2610.00315v2, Lemmas 4.2–4.3 and
     Theorem 4.5);
   - the arithmetic criterion (Brünjes–Serpé, Theorem 3.4).
   Then say what is new here, in the same paragraph:
   - the special-family formulation with an arbitrary geometric place and auxiliary prime at each reduction;
   - the Poincaré-pairing bound on the multiplier, valid in every characteristic;
   - the quantitative Weil results.
   Keep "after Brünjes and Serpé" in the title only if their Theorem 3.4 is the engine of the arithmetic direction as
   you present it; otherwise credit them in the abstract and Section 1 and drop it from the title.

## The body and the end

7. **One paper, one status.** Every statement in the body is either proved in full there, or cited with its exact
   locator and status. The constructions you list as still under review (the cubic extraction for the Mumford family,
   the twisted Kuga–Satake reduction, the secant and cone report) enter the paper only when proved and checked, and
   until then they don't appear in it.
8. **The open questions** at the end: state the gate of the main question exactly. In particular say which split
   eightfold field is the first case needed, and what each restricted eightfold construction in the paper excludes.
9. **The closing note:** keep it, and name the check of this draft as "an outside reading of the proofs by Claude Opus
   5.5 at effort high, which found no error" once the paper is final, with your own re-proofs by the same model listed
   as such.
10. **Finished:** look at every page of the built PDF, and read the whole text twice, as the expert and as the
    newcomer. Write the deposit sheet with the place of each of the eight boxes.

## The research

The main question is unchanged: bounded detectors on split Weil families in every dimension, the first case needed
being split eightfolds over a field other than Q(√−3). Give it most of the time. The routes of the first message stand.
To them add one with a reduction already in the paper: detecting components of complete intersections in a fixed
|mθ| (your Section on the complete-intersection question). Over Q(i) in dimension 4 the paper's own argument has
m = 2. Find the analogue of van Geemen's quadric for split Gaussian sixfolds and eightfolds, or prove that no fixed m
works for a family of linear sections of that kind.

## How to work, and what counts as movement

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give
most of the time to the hardest item, the main question first. Partial results (cases proved, reductions,
computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item.
When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a
larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it
implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a
proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a
proof. An item is finished only when it is proved or refuted.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about
three hours of work, and every hour after that, review the work against a dated ledger (`LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved
reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller
gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that
work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence
above about untried approaches.

## Check events

For every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

## Checkpoints, as in the first message

Keep saving a checkpoint ZIP in the execution environment once every 45 minutes of work, each under a new name,
`HODGE_BOUNDED_CYCLES_checkpoint_<NN>.zip` with `NN` counting up from your last one. Never overwrite, rename or delete an earlier
checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no
other time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work;
it is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds
the current deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint,
and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs
and the final ZIP.

Text written by AI is dedicated to the public domain under CC0 1.0.
