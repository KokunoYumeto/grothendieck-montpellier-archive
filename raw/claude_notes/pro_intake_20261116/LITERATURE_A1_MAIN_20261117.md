# Literature check for ANABELIAN_SUCCESSOR A1 (the main session's part of the first check)

Claude Opus 5.5 at effort max (main session), 17 Nov 2026 ~00:2x UTC. Method: three web searches and the arXiv
abstract pages; no paper read in full. This complements the expert's file EXPERT_A1_ANABELIAN_20261117.md (Claude
Fable 5.2 at effort max, copy ab3f12f2 of the Longue Marche expert), whose brief left the literature to me.

## What exists

1. **Saidi-Tamagawa 2009**, "A prime-to-p version of Grothendieck's anabelian conjecture for hyperbolic curves over
   finite fields of characteristic p > 0", Publ. RIMS 45 (2009) 135-186; arXiv 0801.1452. This is the prime-to-p
   theorem (Sigma = all primes except p). The exceptional set appears here: the abstract page says the prime-to-p case
   is more subtle because of it. The run cites it (AR_ST2009: Def. 1.10, Cor. 1.11, Lemma 1.7, Prop. 1.8(vi),
   Rem. 3.13).
2. **Saidi-Tamagawa 2017**, "A refined version of Grothendieck's anabelian conjecture for hyperbolic curves over finite
   fields", arXiv 1708.08773; J. Algebraic Geom. 27 (2018). It "ignores" a small set of primes, defines exceptional
   elements, calls a map almost injective when its exceptional set is finite, and gives a bijection between the
   complements of the exceptional sets. The run cites it (AR_ST2017: Props. 2.11-2.12).
3. **Wakabayashi 2016**, "On the cuspidalization problem for hyperbolic curves over finite fields", Kyoto J. Math. 56
   (2016) 125-164; arXiv 1507.00622. Main result, per the abstract: any Frobenius-preserving isomorphism between the
   geometrically pro-l fundamental groups of hyperbolic curves with one given point removed induces an isomorphism
   between the geometrically pro-l fundamental groups of the curves with other points removed. This is a pro-l
   cuspidalization over finite fields, close to the run's cuspidally pro-r step (AG.40, AG.41). **The run does not cite
   it** (no hit in its bibliography or its paper).
4. **Mochizuki 2007**, "Absolute anabelian cuspidalizations of proper hyperbolic curves", J. Math. Kyoto Univ. 47(3)
   (2007) 451-539, with his two-page "Comments" of February 2014 (on his RIMS page). The run cites both. Its
   bibliography note says the 2014 corrections do not touch the configuration-fiber statement that AG.39 bears on. The
   run's text (geometric_section.tex l. 4188-4197) says that the statement "requires a quotient-convention or
   source-scope reconciliation with AG39", and that A1's proof does not use it. My searches found no erratum or later
   discussion of that statement.
5. **Recent work on configuration-space sections** (titles only, not opened): arXiv 2505.06826, "The absolute anabelian
   geometry of virtual curves arising from sections of arithmetic fundamental groups of configuration spaces" (2025);
   arXiv 2604.23485, "The absolute anabelian geometry of virtual curves of arbitrary genus" (April 2026). The run cites
   neither.
6. **AnabLab** (github.com/AnabLab/kb): an AI-run knowledge base of anabelian geometry. Bots (anablab-researcher,
   anablab-supervisor, Codex researchers) add restated published results with their sources. Its PR #72 (merged) adds
   Saidi-Tamagawa 2009 and states "New mathematics: None". It is not a source for A1. It is a project that may want our
   checked results later; per the outreach rule, only after the check and on the user's yes.

## What I did not find

No source from 2018 to 2026, in two searches (not exhaustive), proves that the exceptional set E_C is empty for
Sigma = {l != p}, or proves the universal injectivity A1. So, as far as these searches go, A1 would be new.

## For the next prompt that uses A1 (with the expert's items)

- Compare AG.40/AG.41 with Wakabayashi 2016 at its main theorem. Does it already give the cuspidal step, or the step
  for a single prime l? Does anything in it conflict with the run's "maximal cuspidally pro-r" quotient?
- Open Mochizuki 2007 at the configuration-fiber statement and the 2014 comments. Decide whether AG.39 contradicts the
  statement as published, or only a reading of it, and whether any published proof rests on the full pro-Sigma
  exactness for Sigma = all primes except p.
- Check A1 against Saidi-Tamagawa 2017 Props. 2.11-2.12: their finiteness results for E_C must be consistent with its
  emptiness. Note any case where they exhibit or allow a non-empty E_C.

Sources: https://arxiv.org/abs/0801.1452 ; https://arxiv.org/abs/1708.08773 ; https://arxiv.org/abs/1507.00622 ;
https://www.semanticscholar.org/paper/Absolute-anabelian-cuspidalizations-of-proper-Mochizuki/da05d0dd4673083c0310a50fd7e74f04f4e4284a ;
https://arxiv.org/pdf/2505.06826 ; https://arxiv.org/pdf/2604.23485 ; https://github.com/AnabLab/kb/pull/72

## The expert's item K1, checked in the source (main session, Claude Opus 5.5 at effort max, 17 Nov 2026 ~00:5x UTC)

The expert (EXPERT_A1_ANABELIAN_20261117.md, section 3.1) named one outside input of real weight: AG.40
(geometric_section.tex lines 4024-4033) uses Saidi-Tamagawa 2009, Proposition 1.8 (vi), for "every closed point
after its finite constant extension". I opened the arXiv LaTeX source of 0801.1452 (latest version; copy in
pro_intake_20261116/sources_A1/arxiv_0801.1452/main.tex):

- Definition 1.3 (iii): an element is exceptional for a map f when mu_f(f(a)) > 1. Definition 1.5: E_U~ is the
  exceptional set of D-bar, the map from the closed points of the universal geometrically pro-Sigma cover
  (X~_U)^cl to Sub-bar(Pi_U).
- Sub-bar(Pi_U) is the direct limit of Sub(H) over the open subgroups H. The paper identifies it with the
  commensurability classes of closed subgroups (source lines 540-546). So exceptional means "the decomposition group
  is commensurate with that of another point". That is the strong notion, and it is the one AG.40 needs.
- Remark 1.2: D-bar and I-bar are "essentially unchanged if we replace U by any covering corresponding to an open
  subgroup of Pi_U". This includes the finite constant extensions. So E_U~ is one set for all constant extensions at
  once.
- Proposition 1.8 (vi) (source line 748): if Sigma is cofinite, the quotient E_U~/Pi_U is finite. For
  Sigma = all primes except p, Sigma is cofinite. (X~_U)^cl/Pi_U = X^cl, so only finitely many closed points of X are
  exceptional, and finitely many geometric points over them.

**Verdict on K1: the published statement gives what AG.40 uses.** Outside a finite set of closed points, valid for
every finite constant extension, a decomposition subgroup (even up to commensurability) belongs to one point only.
This was the expert's main condition, and the step stands. What remains of the expert's list is K2-K6: (AG.39.15),
the rest of AG.41 step 3 with the arithmetic comparison, AG.42, a finite test by program, and AR.9. Also the second
reader of AG.41, which the expert asks for before anything is said in public.

Caveat on numbering: I checked the arXiv text. The run cites the journal version (Publ. RIMS 45 (2009)). The numbering
of Proposition 1.8 should be compared there when the next prompt opens it (item K1 stays in the prompt as a check
while working).
