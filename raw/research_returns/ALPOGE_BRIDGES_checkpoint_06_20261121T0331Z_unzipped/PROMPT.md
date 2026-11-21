**The attached files.** Besides this file there is one ZIP, `ALPOGE_RH_bridges_into_the_programme.zip`. Unpack it once: it holds every file named below. Every file is at the top level under its own name.

# ALPOGE_BRIDGES: the Riemann hypothesis and GRH, bridged into Grothendieck's programme

## The result, and why it is ours to use

We are all trained to treat claims about the Riemann hypothesis with care, because most come from a bad idea. This one
does not. On 20 November 2026 Levent Alpöge posted a four-page note and a complete Lean formalization of a proof of
the Riemann hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, found with Claude. Alpöge is
a number theorist (Bhargava's student; Harvard Society of Fellows; papers on integral points, monogenic fields and
effective Mordell).
- The file `ALPOGE_Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements. Those statements are
  defined in `ALPOGE_Statements.lean`; the Mathlib revision is in `ALPOGE_lakefile.toml`.
- A text scan of all 175,187 source files, `ALPOGE_LEAN_SCAN.tsv`, finds no sorry, axiom or native_decide.
- It has not been refereed. That is not our concern here. It is taken in as a research return, and its theorems are
  cited as theorems: L. Alpöge, *Remark*, https://alpo.ge/remark.pdf (attached as `ALPOGE_remark.pdf`), with the Lean
  archive at https://alpo.ge/lean.tar.gz.part01 to part14.

**Why it is mathematics about our programme.** Algebraic geometry, from Weil through Grothendieck's cohomology, trace
formula and motives, was built to reach the Riemann hypothesis. Deligne's purity is its proof over finite fields, and
Spec Z is cohomologically a 3-manifold (Artin-Verdier duality). GRH for Dirichlet L-functions is the Riemann hypothesis
for the twisted Tate motives χ ⊗ Q(n) over Q, since L(χ ⊗ Q(n), s) = L(χ, s + n). So it is the Riemann hypothesis for
every Artin-Tate motive over Q whose Artin part is abelian, the Dedekind zeta functions of abelian fields included. The
motivic part of Grothendieck's archive treats exactly these objects.

## The proof as a series of steps (from the note; bracketed readings are ours)

0. Stepanov's method for the Riemann hypothesis over function fields uses an auxiliary function vanishing to high
   multiplicity. Over Z multiplicity is not available ("differentiating whole numbers"). The replacement is a natively
   automorphic determinant, with multiplicity won by chaining theta lifts; for the von Mangoldt sum of length X the
   chain has length about X (page 1).
1. A Stepanov determinant.
2. A toy setting on a CM curve. The invariant derivation D satisfies D^p ≡ 0 for p inert in K, and D^a θ(0)/Ω^a is
   divisible by p^{a/p + a/p³ + ... − O(log a)} [p-adic CM periods].
3. qN = M^k + R: a count with the path quadric x_1x_2 + ... + x_{k−1}x_k, N wanted automorphic.
   - μ is automorphic from θ on the sixfold cover of GL_5, as a period integral of thetas.
   - The quadric lives on the CM curve C/Z[ω], the hexagonal lattice, taken "as Weil"; the Poincaré bundle on the edges
     gives thetas.
4. W(1_S) ≥ 0 by a determinant: Stepanov with multiplicity one; then a bootstrap.
5. The switch to Λ: Σ_{n≤X} Λ(n)(X/n − 1)_+ − X log X + (1 + γ)X, whose sign Guinand-Weil gives.
   - A variance test-function trick on Σ_{h,x} t(x_1)...t(x_k) e_q(h(x_1x_2 + ... + x_{k−1}x_k)).
   - Bertini gives a definite sign from middle cohomology, and R has square-root quality by iterating Parseval k times
     ("as Katz would say"). Opposite signs mean no cancellation of inverse roots: a sign-only proof of the Weil
     conjectures and of Deligne [purity by positivity].
   - In the background: Gabber's hypersurface in Katz's argument; Gauss sums of order #μ_K on the #μ_K-fold cover of
     GL_2, with their reciprocity; Gauss-sum cancellation replaced by iterated Parseval.
6. W(1_(0,1] + (~X^η)·1_(0,1/X]) ≥ 0 gives a zero-free region beyond 1 − η.
7. Determinants for W(·) containing Gan-Gross-Prasad periods: values 0 and 1 for interlacing weights, up to m for
   non-interlacing ones.
8. Iterated theta lifts U(X_0) → U(X_1) → ... → U(X_m) between totally definite unitary groups, π ↦ π ⊞ μ_j[t]. Each
   lift wins one order of multiplicity; m is taken like √X.
9. The norms of the lifts and the level; cancellation of the order-m terms, with divisibility proved through
   Chowla-Selberg, Weyl and the Siegel mass formula.
10. A lower bound for the divisibility of the m-fold iterated lift.
11. An Iwasawa tower, by analogy with pigeonholing over F_{q^n}/F_q.
12. The Rallis seesaw: the period of the iterated lift is a Bessel period, independent of the Hecke characters.
13. The Bost slope inequality.
14. The cost of each lift: one would stop at 2/3 a priori; a main term, transferred to a function field or killed by
    twisting; a "division".
15. An integral structure glued across Hecke characters (extra averaging).
16. A relative trace formula: through Cauchy-Schwarz, a bound on the norm of a projected Poincaré series, and
    approximate orthogonality of the columns of the integral structure.
17. The classes in H¹(o_E[1/ℓ], Q_ℓ/Z_ℓ(−e)) that twisting cannot kill, fought with a weakening of Vandiver. The
    vanishing of K-groups of Z follows; Lichtenbaum [twisted Tate coefficients: the motivic cohomology of number rings].
18. Covolumes, the index of theta series, congruences between lifts and forms.
19. The Iwasawa tower chosen with Behrend's construction.
20. GRH.
Asides in the note: a Siegel argument "strictly dominated by the (2,3,6)-triangle group trick" ("Stepanov without
multiplicity"); Bałaban's induction; F_1 à la Borger.

## Where it already meets the archive (our intakes of 20 Nov, attached as `INTAKE_*.md`)

- **Cote 1 (sheets 79-80, 111-112; attached):** Grothendieck's proof of the Hilbert-space trace formula. Ξ(√w)/Ξ(0) =
  det(1 − wB) with B trace class, and RH is equivalent to B ≥ 0.
- **The tame étale triangle with twists (−n), (−n−1)** (SA20, C.008): the weight structure of Deligne's local monodromy
  theorem (Weil II 1.8.4). In mixed characteristic it is the weight-monodromy conjecture.
- **The real Frobenius on Artin-Tate motives** (SA07, C.3.1): the Artin-Tate motives over R with trivial real Frobenius
  are sums of A(−1)^{⊗p}. On χ ⊗ Q(n), f_∞ = χ(−1)(−1)^n fixes the gamma factors, and GRH puts the zeros at
  Re s = 1/2 − n. The periods and transcendence of motives, cote 18 (attached).
- **Cotes 14 and 15:** his Theorem 3.1 at 14:38 and the "conjecture forte" of 15:100-106, now proved (Milne 1994). Pages
  attached.
- **Cote 134-8, the linear "Thm(?)"** (DER_LOCALIZERS): its motivic case is Voevodsky's A¹-localization, where Z(1)
  is born.
- **Forgetting a point on M̄_{g,n}** (RESIDUE H.3-H.6): purity and the decomposition theorem, with his entrance-path
  model locating the Dehn-twist monodromy.
- **The hexagons, caps and boundary lengths of cotes 67-68** (SA22; the section-6 maps 67/074-082 and 67/091 attached),
  and the Grothendieck-Teichmüller hexagon relation, against step 3's hexagonal C/Z[ω] and the (2,3,6) trick.
- **The surface 𝒳₂ of cote 154** (SA11; 154/120 attached), with point counts over finite fields.

## Background literature in the ZIP (LaTeX sources from arXiv)

- `MASULLO_GRH_the-music-of-the-primes.pdf`: a second, independent proof of GRH, "all human, with no AI", by Alessandro Masullo, posted on 20 Nov 2026 by Ravi Vakil (https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/). Vakil writes that Brian Conrad has studied it closely for months and that it is "so far looking good". It runs to 940 pages and only the PDF is posted, with no LaTeX source. It is an unfinished draft, with empty sections and gaps in the text (B. Naskręcki); Masullo is a former PhD student of Conrad's. Compare its route with Alpöge's, and use each to check and sharpen the other's bridges.
- `MASULLO_DIAGRAM_CROPS/`: the 73 drawn diagrams of that PDF (on 66 pages), each with the text above and below it, cut from the PDF at 1200 dpi in grayscale (`pNNN_k.png`; `MANIFEST.tsv` gives each crop's page and its box in PDF points). They are there for reading the diagrams; diagrams set with font arrows are not among them, and the PDF is the source for everything else.
- `LIT_Deligne_Goncharov_mixed_Tate_motives/`: Deligne-Goncharov, *Groupes fondamentaux motiviques de Tate mixte* (arXiv math/0302267).
- `LIT_Gan_Gross_Prasad_restriction_problems/`: Gan-Gross-Prasad, *Symplectic local root numbers, central critical L-values, and restriction problems* (arXiv 0909.2999); for steps 7 and 12.
- `LIT_Connes_Consani_Weil_positivity_archimedean/`: Connes-Consani, *Weil positivity and trace formula, the archimedean place* (arXiv 2006.13771).
- `LIT_Borger_lambda_rings_field_with_one_element/`: Borger, *Λ-rings and the field with one element* (arXiv 0906.3146); for the note's footnote 5.

## The task

Bridge these theorems into Grothendieck's programme, and resolve what they settle.

1. **The questions of Grothendieck and Deligne** that the cited statements, or the method of the proof, settle: find
   every one, state it as they state it with an exact locator (for the archive: cote and scan), and prove it or refute
   it.
2. **The method in algebraic geometry:** what purity by positivity, multiplicity by theta lifts, twisted Tate
   coefficients, the hexagonal CM curve and the Iwasawa tower give for Grothendieck's motives, weights, crystals, the
   anabelian programme and GT-hat, the Teichmüller tower, and the Dérivateurs.
3. **The life's work of others:**
   - the theorems proved under RH, or under GRH for Dirichlet L-functions, that now hold unconditionally: Montgomery,
     Selberg, Cramér, Littlewood, Bach, Lagarias-Odlyzko for abelian fields, the effective forms of Siegel's theorem,
     Miller, and the rest. Each with its author and an exact locator, and with what exactly it needs; where it needs more
     than the cited statements, what more.
   - the programmes built to reach RH (Weil positivity, Hilbert-Pólya, Connes and Connes-Consani, Deninger, F_1,
     Katz-Sarnak, de Branges, Li, Beurling-Nyman): what each criterion now states as a theorem, and what part stays open.
4. **What else this makes true in our programme that nobody has considered:** state each such statement, prove it, and
   rank the statements by what they settle.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted.

## How to work

The rule that governs everything below: push. Work on the main question first: the questions of Grothendieck and
Deligne that these statements settle. Give it most of the time. When one approach stalls, take the next one. Deliver
nothing while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: attack it,
never paper over it.

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
environment, once every 45 minutes of work, each under a new name, `ALPOGE_BRIDGES_checkpoint_<NN>.zip` with `NN`
counting up. Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a
checkpoint. Save checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every
deliverable written so far and everything that documents the work, so that a new session can continue from it and the
attached files. It is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each
checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `ALPOGE_BRIDGES_final.zip`, holding:
1. **The paper**, `ALPOGE_BRIDGES.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every question with its source and locator;
   - every cited result with an exact locator (Alpöge's by theorem name and file; the literature by work and statement
     number; Grothendieck's archive by cote and scan).
2. **`QUESTIONS.tsv`**, one row for each question found: id, who asked it, source and locator, the question as stated,
   its state (proved, with the finding ids; refuted, with the counterexample; or, if the session ends, its current
   gate), and the bridges used.
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change for each line of our programme and for the open places of the archive
   (cote and scan).

A return may be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach
tried with where it failed, and the next step.
