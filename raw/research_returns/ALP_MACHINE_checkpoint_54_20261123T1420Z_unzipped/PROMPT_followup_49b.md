# ALP_MACHINE, follow-up 1: the main question now, a chain of bounded length (22 Nov 2026)

This message changes the order of your work. Everything in the first message stands: the main questions, the rule on
finishing, the reviews against the dated ledger, the checkpoint ZIPs and CHECK_EVENTS.tsv. Record this change in the
same ledger and work to it from now on. Do not restart.

## Where the run stands (your checkpoint 29)

- Since checkpoint 25, your main questions Q1, Q2 and Q3 have not changed status, and Q4 is partly proved.
- All the movement since then is in one sufficient inequality, Re Σ w(h) > −1 + 2^{−230}, over supports s ≥ 18. The
  support floor of the all-top J⁵⁶ kernel rose from 12 to 18 (R057, R060, R062), while the uniform H8192 floor stays
  at 11. At support 18 the same count gives a positive exponent, so every further level needs a new argument. Even
  with the supports up to 168 exhausted, the inequality gives one finite nonvanishing statement. The global period,
  the arithmetic image, the 032 pairing and the DP44 sign stay open, as your own ledger says.
- Your strongest results stand: LIFT54 and LIFT55. Under Alpöge's formal size hypotheses (`SizesAt`, `SizeM`,
  `SizeK`), two lifts are impossible, the chain length m exceeds 2^7778, and m grows like x^{1/2+O(ε)}.

## The change: take this question, and stop the support-by-support exhaustion

**Can step 8 be carried out with a chain of bounded length? Prove it, by a replacement for `SizesAt` under which the
whole deduction of RH goes through with m bounded; or prove that within the theta-lift method the cost balance forces
m to infinity.**

LIFT54 and LIFT55 are theorems about the size interface as formalized. It is not a theorem that a proof by theta lifts
needs a long chain, and a changed interface may allow a short one. The routes not yet tried:

1. In the Lean dependency graph of the pinned commit, find every use of `SizeM`, `SizeK` and log f ≤ √r_S, and state for
   each the weakest inequality its consumer needs. This list is finite.
2. With m = x^μ, n = x^ν and k = x^κ, write every consumer's inequality as a linear constraint in the exponents, and
   solve the linear program for the infimum of μ. If it is 0, that gives a candidate interface. If it is positive, the
   solution is a certificate naming the binding steps: attack them one by one.
3. Find where the saving from √r_S enters, and test whether a larger rank step per lift (a jump in the Witt tower)
   gives the same saving in fewer lifts.
4. Prove the resulting theorem in Lean against the pinned commit: it is a short deduction from the definitions.
5. For the Kummer characters over Q(ω) (your Q3), run the same program before any construction: it says in advance
   which size interface that case needs.

Keep the signed kernel sum (the DO and R rows) as it stands. Work on it again only for a step that closes the
inequality outright.

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
three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every
checkpoint): every open row with its status, and for each main question its current gate (the strongest proved
reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller
gate. A raise of the support floor counts only if it closes the inequality. Restating the same gate, side results that
leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that
work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence
above about untried approaches.

## Masullo's draft

A. M. Masullo's GRH draft is not a proof. Nothing is presented as a fix, repair or completion of it. Where your text
says that consequences of his claims remain conditional, state them as conditional on GRH for the L-functions
concerned, an open hypothesis.

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
`ALP_MACHINE_checkpoint_<NN>.zip` with `NN` counting up from your last one. Never overwrite, rename or delete an earlier
checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no
other time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work;
it is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds
the current deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint,
and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs
and the final ZIP.

Text written by AI is dedicated to the public domain under CC0 1.0.
